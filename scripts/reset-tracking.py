#!/usr/bin/env python3
"""Reset tracking/ to a clean zero-baseline from resources/objectives.yaml.

DESTRUCTIVE: overwrites tracking/{velocity-tracker,performance,domain-coverage,
acronyms}.json and truncates tracking/question-history.jsonl. Run once on
project setup, or whenever you want to re-baseline.

Usage:
    python3 scripts/reset-tracking.py --exam-date 2026-05-25
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
OBJECTIVES_YAML = REPO_ROOT / "resources" / "objectives.yaml"
TRACKING_DIR = REPO_ROOT / "tracking"


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"  wrote {path.relative_to(REPO_ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exam-date", required=True, help="ISO date, e.g. 2026-05-25")
    args = parser.parse_args()

    try:
        date.fromisoformat(args.exam_date)
    except ValueError:
        print(f"ERROR: --exam-date must be ISO format YYYY-MM-DD", file=sys.stderr)
        return 1

    with OBJECTIVES_YAML.open() as f:
        objectives = yaml.safe_load(f)

    TRACKING_DIR.mkdir(exist_ok=True)

    velocity = {
        "examDate": args.exam_date,
        "sessions": 0,
        "sessionHistory": [],
        "accuracyTrend": [],
        "projections": {
            "coverageAtExamDate": None,
            "rolling7DayAccuracy": None,
            "readiness": None,
            "riskLevel": None,
            "recommendedDailyMinutes": None,
            "recommendedQuestionsPerDay": None,
        },
    }
    write_json(TRACKING_DIR / "velocity-tracker.json", velocity)

    performance_topics = {}
    domain_topics: dict[str, list[str]] = {d: [] for d in objectives["domains"]}
    for section in objectives["sections"]:
        domain_id = section["domain"]
        for sub in section["subsections"]:
            topic_id = sub["id"]
            performance_topics[topic_id] = {
                "title": sub["title"],
                "domain": domain_id,
                "questionsAnswered": 0,
                "correctAnswers": 0,
                "accuracy": None,
                "level": 1,
                "confidence": "unknown",
                "lastStudied": None,
                "streak": 0,
            }
            domain_topics[domain_id].append(topic_id)
    write_json(TRACKING_DIR / "performance.json", {"topics": performance_topics})

    domain_coverage = {
        "version": objectives["version"],
        "domains": {
            domain_id: {
                "name": objectives["domains"][domain_id]["name"],
                "weight": objectives["domains"][domain_id]["weight"],
                "topicIds": sorted(domain_topics[domain_id]),
                "topicsStudied": 0,
                "quizAccuracy": None,
                "lastStudied": None,
            }
            for domain_id in objectives["domains"]
        },
    }
    write_json(TRACKING_DIR / "domain-coverage.json", domain_coverage)

    write_json(TRACKING_DIR / "acronyms.json", {"acronyms": {}})

    history_path = TRACKING_DIR / "question-history.jsonl"
    history_path.write_text("")
    print(f"  wrote {history_path.relative_to(REPO_ROOT)} (empty)")

    print(f"\nReset complete. {len(performance_topics)} topics across "
          f"{len(domain_topics)} domains.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
