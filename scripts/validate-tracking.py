#!/usr/bin/env python3
"""Validate tracking files against schemas and check cross-file integrity.

Used by CI and as a preflight by log-session.py. Exit non-zero on any
problem and print a clear list of issues.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
TRACKING = REPO_ROOT / "tracking"
SCHEMAS = REPO_ROOT / "schemas"
RESOURCES = REPO_ROOT / "resources"

FILES = [
    ("velocity-tracker.json", "velocity-tracker.schema.json"),
    ("performance.json", "performance.schema.json"),
    ("domain-coverage.json", "domain-coverage.schema.json"),
    ("acronyms.json", "acronyms.schema.json"),
]


def load_json(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def validate_schemas(errors: list[str]) -> dict[str, dict]:
    loaded: dict[str, dict] = {}
    for filename, schema_filename in FILES:
        data_path = TRACKING / filename
        schema_path = SCHEMAS / schema_filename
        if not data_path.exists():
            errors.append(f"{filename}: missing")
            continue
        if not schema_path.exists():
            errors.append(f"{schema_filename}: missing")
            continue
        try:
            data = load_json(data_path)
            schema = load_json(schema_path)
        except json.JSONDecodeError as exc:
            errors.append(f"{filename}: invalid JSON - {exc}")
            continue
        validator = Draft7Validator(schema)
        for err in validator.iter_errors(data):
            path = ".".join(str(p) for p in err.absolute_path) or "(root)"
            errors.append(f"{filename}:{path}: {err.message}")
        loaded[filename] = data

    history_path = TRACKING / "question-history.jsonl"
    if history_path.exists():
        with history_path.open() as f:
            schema = load_json(SCHEMAS / "question-history.schema.json")
            validator = Draft7Validator(schema)
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(
                        f"question-history.jsonl:{line_no}: invalid JSON - {exc}"
                    )
                    continue
                for err in validator.iter_errors(entry):
                    errors.append(
                        f"question-history.jsonl:{line_no}: {err.message}"
                    )
    else:
        errors.append("question-history.jsonl: missing")
    return loaded


def validate_cross_refs(loaded: dict[str, dict], errors: list[str]) -> None:
    """Check referential integrity across files."""
    if "performance.json" not in loaded or "domain-coverage.json" not in loaded:
        return

    perf = loaded["performance.json"]
    cov = loaded["domain-coverage.json"]

    perf_topics = set(perf["topics"].keys())
    cov_topics: set[str] = set()
    for domain_id, domain in cov["domains"].items():
        cov_topics.update(domain["topicIds"])
        for topic_id in domain["topicIds"]:
            if topic_id not in perf_topics:
                errors.append(
                    f"domain-coverage.json:{domain_id}.topicIds: "
                    f"'{topic_id}' missing from performance.json"
                )
            else:
                expected_domain = perf["topics"][topic_id]["domain"]
                if expected_domain != domain_id:
                    errors.append(
                        f"performance.json:topics.{topic_id}.domain: "
                        f"'{expected_domain}' but listed under "
                        f"{domain_id} in domain-coverage.json"
                    )

    for topic_id in perf_topics:
        if topic_id not in cov_topics:
            errors.append(
                f"performance.json:topics.{topic_id}: "
                f"not referenced by any domain-coverage.json domain"
            )

    for domain_id, domain in cov["domains"].items():
        if domain["quizAccuracy"] is not None and domain["lastStudied"] is None:
            errors.append(
                f"domain-coverage.json:{domain_id}: quizAccuracy "
                f"set but lastStudied is null (phantom-data class of bug)"
            )

    for topic_id, topic in perf["topics"].items():
        if topic["accuracy"] is not None and topic["lastStudied"] is None:
            errors.append(
                f"performance.json:topics.{topic_id}: accuracy "
                f"set but lastStudied is null"
            )

    objectives_path = RESOURCES / "objectives.yaml"
    if objectives_path.exists():
        with objectives_path.open() as f:
            objectives = yaml.safe_load(f)
        objective_topics = set()
        for section in objectives["sections"]:
            for sub in section["subsections"]:
                objective_topics.add(sub["id"])
        unknown = perf_topics - objective_topics
        if unknown:
            errors.append(
                f"performance.json: topics {sorted(unknown)} "
                f"not present in objectives.yaml"
            )


def main() -> int:
    errors: list[str] = []
    loaded = validate_schemas(errors)
    validate_cross_refs(loaded, errors)

    if errors:
        print(f"FAIL: {len(errors)} validation issue(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"OK: {len(loaded)} tracking files valid, "
        f"{sum(len(v.get('topics', v.get('acronyms', []))) for v in loaded.values() if isinstance(v.get('topics'), dict) or isinstance(v.get('acronyms'), dict))} "
        f"entries cross-checked"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
