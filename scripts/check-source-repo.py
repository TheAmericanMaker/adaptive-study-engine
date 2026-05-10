#!/usr/bin/env python3
"""Verify external/source-repo/ contains the files declared by
resources/objectives.yaml under `sourceFiles:`.

Used as a precondition by other scripts. Exits non-zero with remediation
instructions if the source repo (or any expected file) is missing.

If `sourceFiles` is omitted from objectives.yaml, this script just confirms
the submodule directory exists and contains at least one file.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SUBMODULE_PATH = REPO_ROOT / "external" / "source-repo"
OBJECTIVES_YAML = REPO_ROOT / "resources" / "objectives.yaml"


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    print(
        "\nRemediation:\n"
        "  git submodule update --init --recursive\n"
        "  python3 scripts/check-source-repo.py",
        file=sys.stderr,
    )
    sys.exit(1)


def main() -> None:
    if not SUBMODULE_PATH.is_dir():
        fail(f"source repo missing at {SUBMODULE_PATH}")

    expected: list[str] = []
    if OBJECTIVES_YAML.exists():
        with OBJECTIVES_YAML.open() as f:
            objectives = yaml.safe_load(f) or {}
        source_files = objectives.get("sourceFiles") or {}
        for key in ("studyGuide", "acronyms"):
            name = source_files.get(key)
            if name:
                expected.append(name)

    for name in expected:
        if not (SUBMODULE_PATH / name).is_file():
            fail(f"expected file missing: {name}")

    if not any(SUBMODULE_PATH.iterdir()):
        fail(f"{SUBMODULE_PATH} is empty")

    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=SUBMODULE_PATH,
        capture_output=True,
        text=True,
    )
    detail = ""
    if head.returncode == 0:
        detail = f" (commit {head.stdout.strip()[:12]})"

    print(
        f"OK: {SUBMODULE_PATH.relative_to(REPO_ROOT)} present"
        + (f" with {len(expected)} declared file(s)" if expected else "")
        + detail
    )


if __name__ == "__main__":
    main()
