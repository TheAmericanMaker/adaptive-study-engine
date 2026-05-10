#!/usr/bin/env python3
"""Atomically log a study session and update all tracking files.

Reads a JSONL questions file (one question per line) and updates:
  - tracking/velocity-tracker.json      (session record + recomputed projections)
  - tracking/performance.json           (per-topic accuracy/level/confidence)
  - tracking/domain-coverage.json       (per-domain rollup)
  - tracking/acronyms.json              (timesSeen/lastSeen/confidence)
  - tracking/question-history.jsonl     (append new entries)

All updates are written to .tmp files, validated with validate-tracking.py,
then atomically swapped in. If validation fails, no files are modified.

Usage:
    python3 scripts/log-session.py \\
        --date 2026-05-05 \\
        --domain D1 \\
        --time-min 30 \\
        --questions-file /tmp/session.jsonl \\
        [--note "diagnostic"]

Each line of --questions-file (JSONL):
    {"topicId":"1.1","question":"...","userAnswer":"...","correctAnswer":"...",
     "correct":true,"dontKnow":false,"level":1,
     "sourceSection":"S1","sourceFile":"resources/source-content/section-01-...md",
     "acronyms":["CIA"]}
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import date as date_cls, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRACKING = REPO_ROOT / "tracking"
VALIDATE_SCRIPT = REPO_ROOT / "scripts" / "validate-tracking.py"


def load_json(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def parse_questions(path: Path) -> list[dict]:
    questions: list[dict] = []
    with path.open() as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                questions.append(json.loads(line))
            except json.JSONDecodeError as exc:
                print(
                    f"ERROR: {path}:{line_no} invalid JSON - {exc}",
                    file=sys.stderr,
                )
                sys.exit(2)
    return questions


def confidence_for(accuracy: float, dont_know: bool) -> str:
    if dont_know or accuracy < 0.6:
        return "low"
    if accuracy < 0.8:
        return "medium"
    return "high"


def update_topic(topic: dict, results: list[dict], session_date: str) -> None:
    correct = sum(1 for r in results if r["correct"])
    answered = len(results)
    topic["questionsAnswered"] += answered
    topic["correctAnswers"] = topic.get("correctAnswers", 0) + correct
    if topic["questionsAnswered"] > 0:
        topic["accuracy"] = round(
            topic["correctAnswers"] / topic["questionsAnswered"], 4
        )
    topic["lastStudied"] = session_date

    any_dont_know = any(r.get("dontKnow") for r in results)
    session_accuracy = correct / answered if answered else 0
    topic["confidence"] = confidence_for(session_accuracy, any_dont_know)

    if session_accuracy >= 0.8 and not any_dont_know:
        topic["level"] = min(3, topic["level"] + 1)
    elif session_accuracy < 0.6 or any_dont_know:
        topic["level"] = max(1, topic["level"] - 1)

    streak = topic.get("streak", 0)
    for r in results:
        if r["correct"]:
            streak = streak + 1 if streak >= 0 else 1
        else:
            streak = streak - 1 if streak <= 0 else -1
    topic["streak"] = streak


def recompute_domain_coverage(coverage: dict, performance: dict) -> None:
    perf_topics = performance["topics"]
    for domain_id, domain in coverage["domains"].items():
        topic_ids = domain["topicIds"]
        studied = [t for t in topic_ids if perf_topics[t]["questionsAnswered"] > 0]
        domain["topicsStudied"] = len(studied)

        if studied:
            total_q = sum(perf_topics[t]["questionsAnswered"] for t in studied)
            total_correct = sum(perf_topics[t]["correctAnswers"] for t in studied)
            domain["quizAccuracy"] = round(total_correct / total_q, 4) if total_q else 0.0
            last_dates = [perf_topics[t]["lastStudied"] for t in studied if perf_topics[t]["lastStudied"]]
            domain["lastStudied"] = max(last_dates) if last_dates else None
        else:
            domain["quizAccuracy"] = None
            domain["lastStudied"] = None


MIN_SESSIONS_FOR_EXTRAPOLATION = 3
MIN_DAYS_SPAN_FOR_EXTRAPOLATION = 3


def recompute_projections(velocity: dict, coverage: dict) -> None:
    sessions = velocity["sessionHistory"]
    if not sessions:
        velocity["projections"] = {
            "coverageAtExamDate": None,
            "rolling7DayAccuracy": None,
            "readiness": None,
            "riskLevel": None,
            "recommendedDailyMinutes": None,
            "recommendedQuestionsPerDay": None,
        }
        return

    total_topics = sum(len(d["topicIds"]) for d in coverage["domains"].values())
    studied_weighted = sum(
        d["weight"] * (d["topicsStudied"] / len(d["topicIds"]))
        for d in coverage["domains"].values()
        if d["topicIds"]
    )
    current_coverage = round(studied_weighted, 4)

    studied_topics = sum(d["topicsStudied"] for d in coverage["domains"].values())

    first_date = date_cls.fromisoformat(sessions[0]["date"])
    today = date_cls.fromisoformat(sessions[-1]["date"])
    days_span = (today - first_date).days + 1
    exam_date = date_cls.fromisoformat(velocity["examDate"])
    days_remaining = max((exam_date - today).days, 0)

    # Only extrapolate a coverage projection once we have enough signal to
    # estimate a real per-day rate. With one session on one day, topics/day
    # is meaningless (it equals topics-touched-in-that-session). Until the
    # threshold is met, project current coverage forward unchanged — honest
    # rather than optimistic.
    if (
        len(sessions) >= MIN_SESSIONS_FOR_EXTRAPOLATION
        and days_span >= MIN_DAYS_SPAN_FOR_EXTRAPOLATION
    ):
        topics_per_day = studied_topics / days_span
        projected_topics = studied_topics + topics_per_day * days_remaining
        coverage_projected = (
            min(1.0, projected_topics / total_topics) if total_topics else None
        )
    else:
        coverage_projected = current_coverage

    accuracies = [s["score"] for s in sessions[-7:]]
    rolling_acc = round(sum(accuracies) / len(accuracies), 4) if accuracies else None

    readiness = (
        round(coverage_projected * rolling_acc, 4)
        if coverage_projected is not None and rolling_acc is not None
        else None
    )

    if readiness is None:
        risk = None
    elif readiness < 0.7:
        risk = "HIGH"
    elif readiness < 0.9:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    if readiness is not None and days_remaining > 0:
        gap = max(0.0, 0.95 - readiness)
        rec_minutes = int(min(120, max(30, gap * 200)))
        avg_q_per_min = (
            sum(s["questions"] for s in sessions) /
            max(sum(s["timeSpentMin"] for s in sessions), 1)
        )
        rec_questions = max(5, int(rec_minutes * avg_q_per_min))
    else:
        rec_minutes = None
        rec_questions = None

    velocity["projections"] = {
        "coverageAtExamDate": coverage_projected if coverage_projected is None else round(coverage_projected, 4),
        "rolling7DayAccuracy": rolling_acc,
        "readiness": readiness,
        "riskLevel": risk,
        "recommendedDailyMinutes": rec_minutes,
        "recommendedQuestionsPerDay": rec_questions,
    }


def atomic_write(path: Path, data: dict | str) -> None:
    payload = data if isinstance(data, str) else json.dumps(data, indent=2, sort_keys=True) + "\n"
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as f:
            f.write(payload)
        os.replace(tmp, path)
    except Exception:
        Path(tmp).unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="Session date YYYY-MM-DD")
    parser.add_argument("--domain", required=True, help="domain id from objectives.yaml, or 'mixed'")
    parser.add_argument("--time-min", type=int, required=True)
    parser.add_argument("--questions-file", type=Path, required=True)
    parser.add_argument("--note", default=None)
    args = parser.parse_args()

    try:
        date_cls.fromisoformat(args.date)
    except ValueError:
        print("ERROR: --date must be YYYY-MM-DD", file=sys.stderr)
        return 1

    questions = parse_questions(args.questions_file)
    if not questions:
        print("ERROR: no questions found in questions-file", file=sys.stderr)
        return 1

    velocity = load_json(TRACKING / "velocity-tracker.json")
    performance = load_json(TRACKING / "performance.json")
    coverage = load_json(TRACKING / "domain-coverage.json")
    acronyms = load_json(TRACKING / "acronyms.json")

    by_topic: dict[str, list[dict]] = {}
    for q in questions:
        by_topic.setdefault(q["topicId"], []).append(q)

    for topic_id, results in by_topic.items():
        if topic_id not in performance["topics"]:
            print(f"ERROR: unknown topicId '{topic_id}' (not in performance.json)", file=sys.stderr)
            return 1
        update_topic(performance["topics"][topic_id], results, args.date)

    for q in questions:
        for term in q.get("acronyms", []) or []:
            entry = acronyms["acronyms"].setdefault(term, {
                "expansion": "",
                "timesSeen": 0,
                "lastSeen": None,
                "confidence": "unknown",
            })
            entry["timesSeen"] += 1
            entry["lastSeen"] = args.date
            if q.get("dontKnow") or not q.get("correct"):
                entry["confidence"] = "low"
            elif entry["confidence"] in ("unknown", "low"):
                entry["confidence"] = "medium"

    correct = sum(1 for q in questions if q["correct"])
    score = correct / len(questions)
    topic_ids = sorted(by_topic.keys())
    session_record = {
        "date": args.date,
        "domain": args.domain,
        "score": round(score, 4),
        "questions": len(questions),
        "timeSpentMin": args.time_min,
        "topicIds": topic_ids,
    }
    if args.note:
        session_record["note"] = args.note
    velocity["sessions"] += 1
    velocity["sessionHistory"].append(session_record)
    velocity["accuracyTrend"].append(round(score, 4))
    velocity["accuracyTrend"] = velocity["accuracyTrend"][-30:]

    recompute_domain_coverage(coverage, performance)
    recompute_projections(velocity, coverage)

    history_lines = []
    for q in questions:
        entry = {
            "date": args.date,
            "topicId": q["topicId"],
            "question": q["question"],
            "userAnswer": q.get("userAnswer"),
            "correctAnswer": q["correctAnswer"],
            "correct": bool(q["correct"]),
            "dontKnow": bool(q.get("dontKnow", False)),
            "level": int(q["level"]),
        }
        if "sourceSection" in q:
            entry["sourceSection"] = q["sourceSection"]
        if "sourceFile" in q:
            entry["sourceFile"] = q["sourceFile"]
        history_lines.append(json.dumps(entry, sort_keys=True))

    history_path = TRACKING / "question-history.jsonl"
    existing = history_path.read_text() if history_path.exists() else ""
    new_history = existing + ("" if not existing or existing.endswith("\n") else "\n") + "\n".join(history_lines) + "\n"

    backup_dir = Path(tempfile.mkdtemp(prefix="tracking-backup-"))
    for fname in ["velocity-tracker.json", "performance.json", "domain-coverage.json", "acronyms.json", "question-history.jsonl"]:
        if (TRACKING / fname).exists():
            shutil.copy2(TRACKING / fname, backup_dir / fname)

    try:
        atomic_write(TRACKING / "velocity-tracker.json", velocity)
        atomic_write(TRACKING / "performance.json", performance)
        atomic_write(TRACKING / "domain-coverage.json", coverage)
        atomic_write(TRACKING / "acronyms.json", acronyms)
        atomic_write(TRACKING / "question-history.jsonl", new_history)

        validate = subprocess.run(
            [sys.executable, str(VALIDATE_SCRIPT)],
            capture_output=True,
            text=True,
        )
        if validate.returncode != 0:
            for fname in os.listdir(backup_dir):
                shutil.copy2(backup_dir / fname, TRACKING / fname)
            print("ERROR: validation failed; restored from backup", file=sys.stderr)
            print(validate.stdout, file=sys.stderr)
            print(validate.stderr, file=sys.stderr)
            return 1
    finally:
        shutil.rmtree(backup_dir, ignore_errors=True)

    proj = velocity["projections"]
    print(f"Session logged: {args.date} {args.domain} {correct}/{len(questions)} ({score:.0%}) in {args.time_min}min")
    print(f"  topics touched: {', '.join(topic_ids)}")
    if proj["readiness"] is not None:
        sessions_n = len(velocity["sessionHistory"])
        first = date_cls.fromisoformat(velocity["sessionHistory"][0]["date"])
        last = date_cls.fromisoformat(velocity["sessionHistory"][-1]["date"])
        days_span = (last - first).days + 1
        extrapolating = (
            sessions_n >= MIN_SESSIONS_FOR_EXTRAPOLATION
            and days_span >= MIN_DAYS_SPAN_FOR_EXTRAPOLATION
        )
        basis = "extrapolated" if extrapolating else f"current-only (need {MIN_SESSIONS_FOR_EXTRAPOLATION} sessions across {MIN_DAYS_SPAN_FOR_EXTRAPOLATION} days for velocity projection)"
        print(f"  readiness: {proj['readiness']:.0%}  risk: {proj['riskLevel']}  rec: {proj['recommendedDailyMinutes']}min/day, {proj['recommendedQuestionsPerDay']}q/day")
        print(f"  projection basis: {basis}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
:
    sys.exit(main())
