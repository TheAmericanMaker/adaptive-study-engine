# Source Errata & Exam-vs-Source Discrepancies

Items where the Packt SY0-701 study guide (`external/source-repo/`)
diverges from the consensus CompTIA / industry phrasing. Review before
the live exam — the exam will use CompTIA's wording, not the guide's.

CLAUDE.md forbids hand-editing `tracking/` JSON, so this file is the
durable record. Re-read this list during the final pre-exam pass.

---

## D1 — General Security Concepts

### 1.1 — DAD triad: "Deniability" vs "Destruction"/"Denial"

- **Source phrasing** (`resources/source-content/section-01-summarize-fundamental-security-concepts.md:33-41`):
  DAD = **D**isclosure, **A**lteration, **Deniability**.
- **Issue:** the source's own description of the third leg ("dos, ddos,
  ransomware") is denial-of-service behavior, not deniability. The
  guide labels it incorrectly.
- **Consensus / likely exam phrasing:** DAD = **D**isclosure,
  **A**lteration, **Destruction** (some references say **Denial**).
- **Action on exam:** if both "Destruction" and "Deniability" appear as
  options, prefer **Destruction**. "Deniability" in security typically
  refers to plausible deniability or non-repudiation gaps — a different
  concept entirely.
- **Logged from:** diagnostic Q4, 2026-05-05.
