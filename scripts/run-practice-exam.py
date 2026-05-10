#!/usr/bin/env python3
"""Run a timed, weighted practice exam from a question bank.

Reads a JSONL question bank (one question per line), samples per the domain
weights declared in `resources/objectives.yaml`, runs an interactive timed
quiz in the terminal, and writes a results JSONL compatible with
`scripts/log-session.py`.

Bank line format:
    {"topicId":"1.1","question":"...","options":{"A":"...","B":"...","C":"...","D":"..."},
     "correctAnswer":"B","level":1,"sourceSection":"S1",
     "sourceFile":"resources/source-content/section-01-...md","acronyms":["CIA"]}

Usage:
    python3 scripts/run-practice-exam.py \\
        --bank resources/question-banks/full-bank.jsonl \\
        --length 90 \\
        --time-limit-min 90 \\
        --output /tmp/practice-exam-2026-05-05.jsonl

Then log via:
    python3 scripts/log-session.py --date 2026-05-05 --domain mixed \\
        --time-min <elapsed> --questions-file /tmp/practice-exam-2026-05-05.jsonl \\
        --note "practice-exam"

Exit codes: 0 = completed, 1 = bad input, 2 = user aborted.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PERFORMANCE = REPO_ROOT / "tracking" / "performance.json"
OBJECTIVES_YAML = REPO_ROOT / "resources" / "objectives.yaml"


def load_domain_weights() -> dict[str, float]:
    """Read domain weights from resources/objectives.yaml."""
    import yaml  # local import: only needed at runtime

    if not OBJECTIVES_YAML.exists():
        print(
            f"ERROR: {OBJECTIVES_YAML.relative_to(REPO_ROOT)} missing. "
            "Cannot determine domain weights.",
            file=sys.stderr,
        )
        sys.exit(1)
    with OBJECTIVES_YAML.open() as f:
        objectives = yaml.safe_load(f) or {}
    domains = objectives.get("domains") or {}
    weights = {d: float(meta["weight"]) for d, meta in domains.items()}
    if not weights:
        print("ERROR: no domains declared in objectives.yaml", file=sys.stderr)
        sys.exit(1)
    return weights


def load_bank(path: Path) -> list[dict]:
    bank: list[dict] = []
    with path.open() as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                q = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"ERROR: {path}:{line_no} invalid JSON - {exc}", file=sys.stderr)
                sys.exit(1)
            for field in ("topicId", "question", "options", "correctAnswer", "level"):
                if field not in q:
                    print(f"ERROR: {path}:{line_no} missing field '{field}'", file=sys.stderr)
                    sys.exit(1)
            if q["correctAnswer"] not in q["options"]:
                print(f"ERROR: {path}:{line_no} correctAnswer not in options", file=sys.stderr)
                sys.exit(1)
            bank.append(q)
    return bank


def topic_to_domain(performance: dict) -> dict[str, str]:
    return {tid: t["domain"] for tid, t in performance["topics"].items()}


def sample_weighted(
    bank: list[dict],
    length: int,
    weights: dict[str, float],
    topic_domain: dict[str, str],
    rng: random.Random,
) -> list[dict]:
    by_domain: dict[str, list[dict]] = defaultdict(list)
    for q in bank:
        d = topic_domain.get(q["topicId"])
        if d is None:
            print(
                f"WARN: topicId '{q['topicId']}' not in performance.json — skipping",
                file=sys.stderr,
            )
            continue
        by_domain[d].append(q)

    target = {d: max(1, round(weights[d] * length)) for d in weights}
    drift = sum(target.values()) - length
    if drift > 0:
        for d in sorted(target, key=lambda k: weights[k]):
            if drift == 0:
                break
            if target[d] > 1:
                target[d] -= 1
                drift -= 1
    elif drift < 0:
        for d in sorted(target, key=lambda k: -weights[k]):
            if drift == 0:
                break
            target[d] += 1
            drift += 1

    selected: list[dict] = []
    for d, n in target.items():
        pool = by_domain.get(d, [])
        if not pool:
            print(f"WARN: no bank questions for domain {d} — under-sampling", file=sys.stderr)
            continue
        if len(pool) < n:
            print(
                f"WARN: domain {d} has {len(pool)} questions, need {n} — using all + repeating none",
                file=sys.stderr,
            )
            selected.extend(pool)
        else:
            selected.extend(rng.sample(pool, n))

    rng.shuffle(selected)
    return selected


def format_seconds(s: float) -> str:
    m, s = divmod(int(s), 60)
    return f"{m}m{s:02d}s"


def ask(question: dict, idx: int, total: int, time_left: float | None) -> tuple[str, bool, float]:
    print()
    print("=" * 70)
    header = f"Question {idx}/{total}  (topic {question['topicId']}, L{question['level']})"
    if time_left is not None:
        header += f"  [time left: {format_seconds(time_left)}]"
    print(header)
    print("=" * 70)
    print(question["question"])
    print()
    for letter in ("A", "B", "C", "D"):
        if letter in question["options"]:
            print(f"  {letter}. {question['options'][letter]}")
    print("  X. Don't know")
    print()
    start = time.monotonic()
    while True:
        try:
            raw = input("Your answer [A/B/C/D/X]: ").strip().upper()
        except EOFError:
            print()
            return "X", True, time.monotonic() - start
        if raw in {"A", "B", "C", "D", "X"}:
            elapsed = time.monotonic() - start
            return raw, raw == "X", elapsed
        print("Please enter A, B, C, D, or X.")


def explain(question: dict) -> None:
    src_section = question.get("sourceSection", "?")
    src_file = question.get("sourceFile", "?")
    print(f"  Correct answer: {question['correctAnswer']} — {question['options'][question['correctAnswer']]}")
    print(f"  Source: {src_section} ({src_file})")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bank", type=Path, required=True, help="Path to question bank JSONL")
    parser.add_argument("--length", type=int, default=90, help="Number of questions (default: 90)")
    parser.add_argument(
        "--time-limit-min",
        type=int,
        default=90,
        help="Total time limit in minutes (default: 90; set 0 for untimed)",
    )
    parser.add_argument("--output", type=Path, required=True, help="Where to write results JSONL")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible sampling")
    parser.add_argument(
        "--no-explain",
        action="store_true",
        help="Suppress per-question feedback (closer to real exam conditions)",
    )
    args = parser.parse_args()

    if not args.bank.exists():
        print(f"ERROR: bank not found: {args.bank}", file=sys.stderr)
        return 1
    if not PERFORMANCE.exists():
        print(f"ERROR: performance.json not found at {PERFORMANCE}", file=sys.stderr)
        return 1

    bank = load_bank(args.bank)
    if not bank:
        print(f"ERROR: bank is empty: {args.bank}", file=sys.stderr)
        return 1

    performance = json.loads(PERFORMANCE.read_text())
    topic_domain = topic_to_domain(performance)
    rng = random.Random(args.seed)

    weights = load_domain_weights()
    questions = sample_weighted(bank, args.length, weights, topic_domain, rng)
    if not questions:
        print("ERROR: sampling produced 0 questions — bank may not match performance.json topics", file=sys.stderr)
        return 1

    time_limit = args.time_limit_min * 60 if args.time_limit_min > 0 else None
    print(f"\nPractice exam: {len(questions)} questions", end="")
    if time_limit:
        print(f", {args.time_limit_min} min time limit")
    else:
        print(" (untimed)")
    print("Type X for 'Don't know'. Ctrl-D to abort.\n")

    started = time.monotonic()
    results: list[dict] = []
    aborted = False
    for i, q in enumerate(questions, 1):
        if time_limit and (time.monotonic() - started) >= time_limit:
            print(f"\n*** Time limit reached after {i-1} questions. ***")
            break
        time_left = time_limit - (time.monotonic() - started) if time_limit else None
        answer, dont_know, _q_elapsed = ask(q, i, len(questions), time_left)
        correct = (not dont_know) and answer == q["correctAnswer"]
        if not args.no_explain and not correct:
            explain(q)
        elif not args.no_explain and correct:
            print("  Correct.")
        results.append({
            "topicId": q["topicId"],
            "question": q["question"],
            "userAnswer": None if dont_know else q["options"][answer],
            "correctAnswer": q["options"][q["correctAnswer"]],
            "correct": correct,
            "dontKnow": dont_know,
            "level": q["level"],
            "sourceSection": q.get("sourceSection", ""),
            "sourceFile": q.get("sourceFile", ""),
            "acronyms": q.get("acronyms", []),
        })

    elapsed = time.monotonic() - started
    correct_n = sum(1 for r in results if r["correct"])
    dk_n = sum(1 for r in results if r["dontKnow"])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        for r in results:
            f.write(json.dumps(r, sort_keys=True) + "\n")

    print()
    print("=" * 70)
    print(f"Practice exam complete: {correct_n}/{len(results)} correct ({correct_n/max(len(results),1):.0%})")
    print(f"Don't know: {dk_n}    Time: {format_seconds(elapsed)}")
    by_domain_score: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for r in results:
        d = topic_domain.get(r["topicId"], "?")
        by_domain_score[d][1] += 1
        if r["correct"]:
            by_domain_score[d][0] += 1
    print("\nBy domain:")
    for d in sorted(by_domain_score):
        c, t = by_domain_score[d]
        print(f"  {d}: {c}/{t} ({c/t:.0%})")
    print(f"\nResults written to: {args.output}")
    print("Log this session with:")
    print(
        f"  python3 scripts/log-session.py --date $(date +%F) --domain mixed "
        f"--time-min {int(elapsed/60) or 1} --questions-file {args.output} "
        f"--note 'practice-exam'"
    )
    return 2 if aborted else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(2)
