#!/usr/bin/env python3
"""v35.8 — exact-live Deep Curriculum provenance/rendering audit, seeded by SNHL.

Fail closed for the exact SNHL repair and the 325-topic contract. Also emit the complete
live source-metadata backlog so subsequent cohorts are selected from real production data
rather than lexical guesses. The broader backlog is intentionally reported, not globally
blocked in this first source-completeness cohort; each subsequent patch can retire exact
canonical entries without destabilizing already-completed domain gates.
"""

from pathlib import Path
import re
import sys

import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Otology / Neurotology"
TARGET = "sensorineural hearing loss"


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def fail(message):
    print(f"FAIL: {message}")
    return 1


def main():
    deep = getattr(data, "DEEP_MODULES_V6", {}) or {}
    all_rows = [(domain, row) for domain, rows in deep.items() for row in (rows or [])]
    failures = 0

    # Preserve the canonical production contract while adding provenance.
    if len(all_rows) != 325:
        failures += fail(f"canonical Deep Curriculum count changed: expected 325, found {len(all_rows)}")

    rows = deep.get(DOMAIN, []) or []
    target_rows = [row for row in rows if norm(row.get("topic")) == TARGET]
    if len(target_rows) != 1:
        failures += fail(
            f"expected exactly one exact-live canonical {TARGET!r} in {DOMAIN}; "
            f"found {len(target_rows)}: {[row.get('topic') for row in target_rows]}"
        )
    else:
        row = target_rows[0]
        if not row.get("source_grounded_v358"):
            failures += fail("SNHL live canonical record did not receive v35.8 provenance patch")
        source_lines = [str(x) for x in (row.get("source_basis") or []) if str(x).strip()]
        sources = " ".join(source_lines).lower()
        if len(source_lines) < 7:
            failures += fail(f"SNHL source_basis too shallow: {len(source_lines)} entries")
        for token in (
            "cummings", "pasha", "k.j. lee", "18qgoaazhvh", "14e4iy4xcj", "112c9y0fb1",
            "sudden hearing loss", "age-related hearing loss", "cochlear implant alliance", "fda", "otof",
        ):
            if token not in sources:
                failures += fail(f"SNHL source trail missing {token!r}")

        metadata = row.get("source_metadata_v358") or {}
        if metadata.get("canonical_link") != {"domain": DOMAIN, "topic": row.get("topic")}:
            failures += fail("SNHL canonical source metadata is not linked to the exact live domain/topic")
        review = row.get("deliberate_review_v358") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(review.get(layer) or "").strip():
                failures += fail(f"SNHL deliberate-review metadata missing {layer}")
        if len(review.get("traps") or []) < 6:
            failures += fail("SNHL individualized trap set is too shallow")

        combined = " ".join(str(row.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        for token in (
            "air-bone gap", "sudden", "retrocochlear", "mri", "corticosteroid", "intratympanic",
            "hearing aids", "cochlear-implant", "device-specific", "otarmeni",
        ):
            if token not in combined:
                failures += fail(f"SNHL clinical depth missing discriminator {token!r}")

    # Verify that source metadata is visible on the actual Deep Curriculum UI path.
    template = Path("templates/curriculum_depth.html").read_text(encoding="utf-8")
    compact = re.sub(r"\s+", " ", template)
    if "m.source_basis" not in compact or "for s in m.source_basis" not in compact or "Source basis" not in compact:
        failures += fail("Deep Curriculum renderer does not surface live m.source_basis entries")

    # Emit the exact-live source backlog for clinically prioritized successor cohorts.
    missing = []
    incomplete = []
    for domain, row in all_rows:
        sources = [str(x).strip() for x in (row.get("source_basis") or []) if str(x).strip()]
        if not sources:
            missing.append((domain, str(row.get("topic") or "")))
            continue
        joined = " ".join(sources).lower()
        textbook_hits = sum(token in joined for token in ("cummings", "pasha", "k.j. lee"))
        if textbook_hits < 2:
            incomplete.append((domain, str(row.get("topic") or ""), textbook_hits))

    print(f"SOURCE_COMPLETENESS_TOTAL={len(all_rows)}")
    print(f"SOURCE_MISSING_COUNT={len(missing)}")
    print(f"SOURCE_INCOMPLETE_TEXTBOOK_COUNT={len(incomplete)}")
    for domain, topic in missing:
        print(f"SOURCE_BACKLOG_MISSING\t{domain}\t{topic}")
    for domain, topic, hits in incomplete:
        print(f"SOURCE_BACKLOG_INCOMPLETE\t{domain}\t{topic}\tcore_textbook_hits={hits}")

    if failures:
        print(f"\nDeep Curriculum source-completeness v35.8 FAILED with {failures} issue(s).")
        return 1

    print("PASS: exact-live SNHL is clinically deep, textbook/current-evidence traceable, and source_basis is rendered; global source backlog emitted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
