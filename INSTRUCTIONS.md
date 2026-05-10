# Adaptive Study Engine — LLM Instructions

This file is the behavioral contract between you (a study learner) and the
LLM helping you study. It tells the LLM how to read state, how to ask
questions, how to handle "don't know," and how to log sessions.

The engine itself is topic-agnostic. The active syllabus lives in
`resources/objectives.yaml`. Edit *that* to change topic — not this file.

---

## Quick Start for the LLM

1. Read this file (you just did).
2. Read `resources/objectives.yaml` — canonical syllabus (domains, sections, topics).
3. Read `tracking/performance.json` — per-topic accuracy/level/confidence.
4. Read `tracking/domain-coverage.json` — per-domain coverage and accuracy.
5. Read `tracking/velocity-tracker.json` — sessions, accuracy trend, projections.
6. Read `study-plan/adaptive-schedule.md` — auto-generated today's plan, weak
   topics, untouched topics, acronym priorities.
7. Read `tracking/acronyms.json` — confidence-tagged glossary.
8. The factual source lives at `external/source-repo/` (a git submodule the
   user adds per project). Per-section markdown extracts live in
   `resources/source-content/`. Index: `resources/indexes/source-section-map.json`.
9. Run the quiz, then log it: `python3 scripts/log-session.py …`
   (see "After every session" below).

---

## Hard Rules (Non-Negotiable)

### Quiz Design

- Every question MUST have 4 options + **"Don't know"** as a 5th option.
- "Don't know" tracks as 0% and flags the topic for priority review.
- Random guessing is strictly worse than "Don't know" — never omit the option.

### Acronym / Term Handling

- **Scenario-first only.** Never present bare "What does X stand for?"
  flashcards.
- Embed the acronym (or unfamiliar term) in a realistic scenario 3+ times
  before quizzing the abbreviation alone.
- When a new acronym appears, write the full name in parentheses on first
  use per session.

### Adaptive Difficulty

- Per-topic level: L1 = definition, L2 = applied scenario, L3 = complex /
  tricky edge case.
- **Correct** → increase level (max L3).
- **Wrong** → same level + immediate contextual explanation.
- **Don't know** → decrease level (min L1) + instant reveal + re-quiz next session.

### Factual Grounding

- Every wrong answer MUST cite an entry from
  `resources/indexes/source-section-map.json`: which section, which
  subsection ID, which markdown file under `resources/source-content/`.
- Never explain from memory alone. Read the indexed markdown when explaining
  a miss.
- If a topic isn't in the index, the index is incomplete — flag it; do NOT
  invent content.
- If the source's wording diverges from the consensus / official phrasing on
  a point, log it in `docs/SOURCE-ERRATA.md` (markdown, not `tracking/`).
  Re-read that file during the final pre-exam pass — the live exam uses the
  official wording, not the guide's.

---

## After Every Session

Log the session via the script (do NOT hand-edit JSON):

```bash
python3 scripts/log-session.py \
  --date YYYY-MM-DD \
  --domain D1 \
  --time-min 30 \
  --questions-file /tmp/today.jsonl \
  --note "morning-quiz"
python3 scripts/generate-schedule.py
git add tracking/ study-plan/adaptive-schedule.md
git commit -m "Session N: D1, X/Y correct, readiness Z%"
```

`/tmp/today.jsonl` is JSONL with one question per line:

```json
{"topicId":"1.1","question":"...","userAnswer":"...","correctAnswer":"...","correct":true,"dontKnow":false,"level":1,"sourceSection":"S1","acronyms":["EXAMPLE"]}
```

`log-session.py` recomputes accuracy / confidence / level for every touched
topic, rolls up domain coverage, recomputes projections, and validates
everything against schemas before swapping files. If validation fails, no
files are modified.

---

## System Files

| File | Purpose |
|------|---------|
| `INSTRUCTIONS.md` | This file (LLM contract) |
| `CLAUDE.md` | AI-specific operational rules |
| `tracking/velocity-tracker.json` | Sessions, accuracy trend, projections |
| `tracking/performance.json` | Per-topic state |
| `tracking/domain-coverage.json` | Per-domain rollup |
| `tracking/acronyms.json` | Confidence-tagged acronym glossary |
| `tracking/question-history.jsonl` | Append-only question log (spaced repetition) |
| `study-plan/adaptive-schedule.md` | Auto-generated daily plan |
| `resources/objectives.yaml` | Canonical syllabus (domains/sections/topics) — source of truth |
| `resources/indexes/source-section-map.json` | Generated index linking domains → sections → content files |
| `resources/source-content/*.md` | Extracted study content (regenerate via `scripts/build-index.py`) |
| `external/source-repo/` | Per-topic factual-source submodule (added by the user) |
| `schemas/*.schema.json` | JSON schemas for all tracking files |
| `scripts/*.py` | Automation: see `docs/SCHEMA.md` for the full pipeline |
| `examples/` | Worked example profiles (currently: `security-plus/`) |

---

## Phase Planning

The engine doesn't impose a study plan; it generates one from current state
in `study-plan/adaptive-schedule.md` after each session. The schedule
prioritizes:

1. Untouched topics in domains with the highest blueprint weight.
2. Topics flagged from "Don't know" or wrong answers.
3. Topics with the oldest `lastStudied` (spaced repetition).
4. Acronyms with `confidence: low`.

If you want week-by-week phasing, add it to a separate `study-plan/` doc;
the auto-generated `adaptive-schedule.md` will defer to current state.

---

## Topic Profiles

This engine is topic-agnostic. To swap topics:

1. Replace `external/source-repo` with a new submodule
   (`git submodule add … external/source-repo`).
2. Rewrite `resources/objectives.yaml` with new domains, weights, and
   section mappings. Domain IDs are free-form (e.g. `D1`, `AWS-COMPUTE`,
   `VOCAB-A1`); weights should sum to 1.0.
3. Run `scripts/build-index.py` to regenerate content + index.
4. Run `scripts/reset-tracking.py --exam-date YYYY-MM-DD` to seed tracking.
5. (Optional) Add topic-specific rules to this file or a sibling
   `INSTRUCTIONS.<topic>.md`.

See `CONTRIBUTING.md` and `docs/SCHEMA.md` for details, and
`examples/security-plus/` for a complete worked profile.
