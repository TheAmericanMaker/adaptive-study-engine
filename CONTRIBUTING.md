# Contributing to the Adaptive Study Engine

Thank you for helping improve this system. Contributions welcome in four
areas.

## 1. Framework Improvements

If you improve the adaptive algorithm, tracking schema, or scheduling logic:

1. Fork and branch.
2. Update the relevant schema in `schemas/` if the data shape changes.
3. Update `scripts/log-session.py` and `scripts/validate-tracking.py` to match.
4. Open a PR with before/after numbers (e.g., "with the new level-decay
   formula, simulated readiness reaches 0.9 in 14 sessions vs 19
   previously").
5. CI must pass (`scripts/validate-tracking.py`).

## 2. New Example Profiles

The bundled `examples/security-plus/` profile shows what a complete, working
topic profile looks like. New examples are welcome:

1. Create `examples/<topic-slug>/` with at minimum:
   - `objectives.yaml` (canonical syllabus)
   - `README.md` (one-paragraph what + which source repo + how to activate)
2. Optionally include sample question banks under
   `examples/<topic-slug>/question-banks/`.
3. **Do NOT commit copyrighted study material** into the example folder.
   Reference the source repo by URL in `objectives.yaml.sourceRepo`; users
   add it themselves via `git submodule add`.

## 3. Reference Repo Suggestions

If you've found a factual source repo that works well for a given topic but
you're not building a full profile yourself, you can still help: open a PR
adding a row to [`docs/REFERENCE-REPOS.md`](docs/REFERENCE-REPOS.md). The
bar for inclusion (license, stability, coverage) is documented in the
catalog itself.

## 4. Porting to a New Topic in Your Own Fork

The schema is intentionally topic-agnostic. To use the engine for AWS, a
language exam, coding interviews, etc.:

0. **Pick a source repo.** Check [`docs/REFERENCE-REPOS.md`](docs/REFERENCE-REPOS.md)
   for vetted options for your topic. If none exist, find your own (any
   structured factual source works) and submit it back via PR so the next
   person doesn't have to rediscover it.
1. **Add the source.** Replace `external/source-repo` with the new factual
   source:

   ```bash
   git submodule deinit external/source-repo  # if previously set
   git rm external/source-repo                # if previously set
   git submodule add <new-repo-url> external/source-repo
   ```

2. **Write `resources/objectives.yaml`.** Start from
   `resources/objectives.yaml.example`. Domain IDs are free-form strings;
   weights should sum to 1.0. The schemas in `schemas/` no longer assume any
   specific domain count.
3. **Adapt `scripts/build-index.py` if needed.** The default extractor
   handles `SECTION N`-style markers in PDFs and any DOCX in the source
   repo. If your source has different section markers, override
   `sourceFiles.sectionRegex` in `objectives.yaml`. For radically different
   formats (e.g. JSON, HTML), add a new ingestion script under `scripts/`.
4. **Reset tracking.** `python3 scripts/reset-tracking.py --exam-date YYYY-MM-DD`
   regenerates `tracking/*.json` from your new `objectives.yaml`.
5. **(Optional) Adjust `INSTRUCTIONS.md`** with topic-specific rules (e.g.
   service categories for AWS, vocabulary buckets for languages).
6. If your fork is generally useful, consider opening a PR back here adding
   it under `examples/<topic-slug>/`.

## Code of Conduct

- **Scenario-first, always.** No bare acronym flashcards.
- **"Don't know" is sacred.** Never remove it.
- **Factual grounding over speed.** A wrong quiz answer with no source
  citation is a bug.
- **Respect velocity alerts.** The system flags HIGH risk for a reason —
  fix the cause, don't suppress the alert.
- **Schema-validated state.** Don't bypass `validate-tracking.py`; if it
  complains, the data is wrong, not the validator.

## License

By contributing, you agree that your contributions will be licensed under
the MIT License.
