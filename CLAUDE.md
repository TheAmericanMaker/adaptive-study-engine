# CLAUDE.md — AI Assistant Instructions

This file provides guidance specifically for AI assistants (Claude, ChatGPT,
or any LLM) working with this repository.

## Primary Directive

When asked to help study, read **INSTRUCTIONS.md** first. It contains the
behavioral contract, file map, and session-logging command. This file
supplements it with AI-specific guidance.

## State Management Rules

1. **Never hallucinate source content.** Every quiz question and explanation
   must trace to an entry in `resources/indexes/source-section-map.json`. If
   a topic isn't indexed, surface the gap and stop — do NOT invent content.
   The factual source lives at `external/source-repo/` (per-project submodule);
   extracted markdown is under `resources/source-content/`.

2. **Update tracking via scripts only.** Do NOT hand-edit JSON files in
   `tracking/`. After every session run:

   ```bash
   python3 scripts/log-session.py --date <YYYY-MM-DD> --domain <id|mixed> \
       --time-min <N> --questions-file <path-to-jsonl> [--note "..."]
   python3 scripts/generate-schedule.py
   ```

   The script atomically updates all tracking files, recomputes projections,
   and runs `validate-tracking.py` before swapping. If validation fails, no
   files are touched.

3. **Validate before commit.** Run `python3 scripts/validate-tracking.py`;
   if it fails, fix the cause (don't bypass the check). CI runs the same
   check on every push.

4. **Git discipline.** Stage tracking + schedule together:

   ```bash
   git add tracking/ study-plan/adaptive-schedule.md
   git commit -m "Session N: <domain> <correct>/<total>, readiness <pct>%"
   git push
   ```

## Quiz Design Constraints

- Every question MUST have a "Don't know" option.
- **Scenario-first for acronyms / unfamiliar terms.** Never ask "What does X
  stand for?" first. Embed the term in a realistic scenario, then reveal the
  expansion.
- **Adaptive difficulty.** Respect `performance.json` `level` per topic. If
  correct at L3, ask a trick variant. If wrong / don't-know at any level,
  drop to L1 next time.

## Error Recovery

If tracking files are missing or corrupted:

1. Check `git log` — revert to last known good state with
   `git checkout HEAD -- tracking/`.
2. If git history is also bad, run
   `python3 scripts/reset-tracking.py --exam-date YYYY-MM-DD` (DESTRUCTIVE
   — wipes to zero baseline).
3. Always notify the user when recovering from bad state.

If the source-repo submodule is missing:

1. Run `git submodule update --init --recursive`.
2. Run `python3 scripts/check-source-repo.py` to verify.
3. If extraction is needed, run `python3 scripts/build-index.py`.

## Performance Patterns

`scripts/log-session.py` applies these automatically; documented here so the
LLM-side feedback to the user can match.

| User Score | Next Action |
|------------|-------------|
| ≥ 80% at current level (no don't-knows) | Increase difficulty (L+1, capped at 3), reduce frequency (spaced repetition) |
| 60–79% | Maintain level, re-expose in next session |
| < 60% or any "Don't know" | Decrease level (L-1, floor 1), priority flag, inject supplemental explanation from source |

## Source Material Access

The factual source lives under `external/source-repo/` — a per-project
submodule that the user adds when they pick a topic. Pre-extracted into
`resources/source-content/section-NN-*.md` by `scripts/build-index.py`. Use
`resources/indexes/source-section-map.json` to look up which file/section a
topic maps to.

## Portability

This same structure works for any topic with a syllabus + factual source.
See `INSTRUCTIONS.md` § Topic Profiles, `CONTRIBUTING.md`, and
`docs/SCHEMA.md` for the porting checklist. A worked example lives under
`examples/security-plus/`.
