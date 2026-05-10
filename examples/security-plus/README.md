# Example Profile — CompTIA Security+ SY0-701

A complete, working profile for the [Adaptive Study Engine](../../README.md)
mapped to the [PacktPublishing CompTIA Security+ SY0-701 Full Training
Guide](https://github.com/PacktPublishing/CompTIA-Security-SY0-701-Full-Training-Guide).

## What's here

- `objectives.yaml` — the full SY0-701 syllabus (5 domains, 16 source
  sections, 119 topics) wired to the Packt study guide.
- `indexes/source-section-map.json` — pre-built index linking domains →
  sections → content files. Generated from `objectives.yaml` plus the Packt
  guide.
- `source-content/*.md` — extracted markdown for each section of the Packt
  guide. Reproducible by running `scripts/build-index.py` after adding the
  Packt repo as a submodule.
- `question-banks/sample-diagnostic.jsonl` — a 22-question diagnostic
  question bank covering all five domains, suitable as a first-session
  baseline quiz.
- `SOURCE-ERRATA.md` — points where the Packt guide's wording diverges from
  the consensus / official CompTIA phrasing. Re-read before the live exam.

## Activate this profile

From the project root:

```bash
# Copy the syllabus into the engine's expected location
cp examples/security-plus/objectives.yaml resources/objectives.yaml

# Either copy the pre-built artifacts...
cp examples/security-plus/indexes/source-section-map.json \
   resources/indexes/source-section-map.json
cp -r examples/security-plus/source-content/. resources/source-content/

# ...or rebuild them yourself from the Packt source:
git submodule add https://github.com/PacktPublishing/CompTIA-Security-SY0-701-Full-Training-Guide \
                  external/source-repo
python3 scripts/build-index.py

# Initialise tracking with your exam date
python3 scripts/reset-tracking.py --exam-date 2026-05-25
python3 scripts/generate-schedule.py
```

Then point your LLM at `INSTRUCTIONS.md` and start studying. Run a baseline
session with the sample question bank:

```bash
python3 scripts/run-practice-exam.py \
  --bank examples/security-plus/question-banks/sample-diagnostic.jsonl \
  --length 22 \
  --output /tmp/diagnostic.jsonl
python3 scripts/log-session.py --date $(date +%F) --domain mixed \
  --time-min 30 --questions-file /tmp/diagnostic.jsonl --note diagnostic
```
