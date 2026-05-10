#!/usr/bin/env python3
"""Extract source materials referenced by resources/objectives.yaml into
indexable markdown.

Reads:
  - resources/objectives.yaml         (canonical structure + source file refs)
  - external/source-repo/*.pdf,*.docx,*.txt   (your factual source material)

Writes:
  - resources/source-content/<section-id>.md   (one per source section)
  - resources/indexes/source-section-map.json  (domain -> sections -> file)

Idempotent: re-running produces stable output.

Configuration (in resources/objectives.yaml):

    sourceFiles:
      studyGuide: "<filename>.pdf"        # optional; will be split by sectionRegex
      acronyms:   "<filename>.pdf"        # optional
      sectionRegex: '^\\s*SECTION\\s+(\\d+)\\s*-?\\s*$'   # optional; default shown

If `studyGuide` is omitted, this script will not attempt to split a study
guide; only DOCX files in external/source-repo/ are extracted, and per-section
markdown is written from `sections[].sourceFile` references.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SUBMODULE = REPO_ROOT / "external" / "source-repo"
OBJECTIVES_YAML = REPO_ROOT / "resources" / "objectives.yaml"
CONTENT_DIR = REPO_ROOT / "resources" / "source-content"
INDEX_OUT = REPO_ROOT / "resources" / "indexes" / "source-section-map.json"

DEFAULT_SECTION_REGEX = r"^\s*SECTION\s+(\d+)\s*-?\s*$"


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", text).strip("-")


def pdftotext(pdf_path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def docx_to_text(docx_path: Path) -> str:
    try:
        from docx import Document  # local import: only needed when DOCX present
    except ImportError:
        print(
            "WARN: python-docx not installed; skipping DOCX extraction. "
            "Install with: pip install python-docx",
            file=sys.stderr,
        )
        return ""
    doc = Document(str(docx_path))
    return "\n".join(p.text for p in doc.paragraphs)


def split_study_guide(text: str, section_regex: str) -> dict[int, str]:
    """Return {section_number: body_text} from a study guide.

    The pattern is configurable via ``sourceFiles.sectionRegex`` in
    objectives.yaml. The default expects ``SECTION N`` markers on their own
    line. The first capture group must be the section number.
    """
    pattern = re.compile(section_regex, re.MULTILINE)
    matches = [(m.start(), int(m.group(1))) for m in pattern.finditer(text)]
    sections: dict[int, str] = {}
    for i, (start, num) in enumerate(matches):
        end = matches[i + 1][0] if i + 1 < len(matches) else len(text)
        sections[num] = text[start:end].strip()
    return sections


def main() -> int:
    if not OBJECTIVES_YAML.exists():
        print(
            f"ERROR: {OBJECTIVES_YAML.relative_to(REPO_ROOT)} missing. "
            "Copy resources/objectives.yaml.example and fill it in.",
            file=sys.stderr,
        )
        return 1

    with OBJECTIVES_YAML.open() as f:
        objectives = yaml.safe_load(f)

    source_files = objectives.get("sourceFiles", {}) or {}
    study_guide_name = source_files.get("studyGuide")
    acronyms_name = source_files.get("acronyms")
    section_regex = source_files.get("sectionRegex", DEFAULT_SECTION_REGEX)

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_OUT.parent.mkdir(parents=True, exist_ok=True)

    section_bodies: dict[int, str] = {}
    if study_guide_name:
        if not SUBMODULE.is_dir():
            print(
                "ERROR: external/source-repo/ missing but objectives.yaml "
                "references a studyGuide. Add the source repo as a submodule "
                "or remove sourceFiles.studyGuide.",
                file=sys.stderr,
            )
            return 1
        print(f"Extracting study guide: {study_guide_name}")
        text = pdftotext(SUBMODULE / study_guide_name)
        section_bodies = split_study_guide(text, section_regex)
        print(f"  Found {len(section_bodies)} body sections")

    if acronyms_name:
        print(f"Extracting acronyms: {acronyms_name}")
        acronyms_text = pdftotext(SUBMODULE / acronyms_name)
        (CONTENT_DIR / "acronyms-source.md").write_text(
            f"# Acronyms\n\n"
            f"_Source: external/source-repo/{acronyms_name}_\n\n"
            f"```\n{acronyms_text}\n```\n"
        )

    if SUBMODULE.is_dir():
        print("Extracting DOCX files...")
        for docx_path in sorted(SUBMODULE.glob("*.docx")):
            slug = slugify(docx_path.stem)
            text = docx_to_text(docx_path)
            (CONTENT_DIR / f"docx-{slug}.md").write_text(
                f"# {docx_path.stem}\n\n"
                f"_Source: external/source-repo/{docx_path.name}_\n\n"
                f"{text}\n"
            )

    print("Writing per-section markdown...")
    section_map = {}
    written_files = []
    for section in objectives["sections"]:
        section_num = section["sourceSection"]
        body = section_bodies.get(section_num, "")
        if study_guide_name and not body:
            print(
                f"  WARN: no body found for source section {section_num}",
                file=sys.stderr,
            )

        slug = slugify(section["title"])
        out_name = f"section-{section_num:02d}-{slug}.md"
        out_path = CONTENT_DIR / out_name

        sub_index = "\n".join(
            f"- {sub['id']} {sub['title']}" for sub in section["subsections"]
        )
        source_file = section.get("sourceFile", study_guide_name or "")
        body_md = (
            f"# Section {section_num}: {section['title']}\n\n"
            f"_Domain {section['domain']} · Source: external/source-repo/"
            f"{source_file}_\n\n"
            f"## Subsections\n{sub_index}\n\n"
            f"## Content\n\n```\n{body}\n```\n"
        )
        out_path.write_text(body_md)
        written_files.append(out_name)

        section_map[section["id"]] = {
            "sourceSection": section_num,
            "title": section["title"],
            "domain": section["domain"],
            "contentFile": f"resources/source-content/{out_name}",
            "originalFile": f"external/source-repo/{source_file}",
            "subsections": [
                {"id": sub["id"], "title": sub["title"]}
                for sub in section["subsections"]
            ],
        }

    domain_to_sections: dict[str, list[str]] = {}
    for section_id, info in section_map.items():
        domain_to_sections.setdefault(info["domain"], []).append(section_id)

    output = {
        "version": objectives["version"],
        "sourceRepo": objectives.get("sourceRepo", ""),
        "domains": {
            domain_id: {
                "name": objectives["domains"][domain_id]["name"],
                "weight": objectives["domains"][domain_id]["weight"],
                "sections": sorted(domain_to_sections.get(domain_id, [])),
            }
            for domain_id in objectives["domains"]
        },
        "sections": section_map,
    }
    INDEX_OUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")

    print(f"\nWrote {len(written_files)} section files to {CONTENT_DIR}")
    print(f"Wrote index to {INDEX_OUT.relative_to(REPO_ROOT)}")
    for domain_id, sections in sorted(domain_to_sections.items()):
        print(f"  {domain_id}: {', '.join(sorted(sections))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
