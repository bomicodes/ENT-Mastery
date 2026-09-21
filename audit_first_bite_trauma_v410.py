#!/usr/bin/env python3
"""Fail closed if the v41.0 first-bite trauma nuance disappears."""

import sys

import runtime_entry_pasha


DOMAIN = "Thyroid / Parathyroid / Salivary"
TOPIC = "First-Bite Syndrome"


def main():
    rows = [
        row
        for row in runtime_entry_pasha.runtime_entry.data.DEEP_MODULES_V6.get(DOMAIN, [])
        if row.get("topic") == TOPIC
    ]
    if len(rows) != 1:
        print(f"FAIL: expected one {TOPIC} row; found {len(rows)}")
        return 1

    row = rows[0]
    text = " ".join(str(row.get(field) or "") for field in ("diagnose", "teach"))
    sources = " ".join(str(source) for source in row.get("source_basis") or [])
    required = (
        "blunt or penetrating parotid",
        "deep-lobe or retromandibular parotid injury",
        "need not be confined to the deep lobe",
        "cervical sympathetic",
        "sparsely documented",
        "Superficial bruising alone is not the classic mechanism",
        "CTA/MRA",
        "occult deep parotid",
    )
    missing = [token for token in required if token not in text]
    if missing:
        print("FAIL: missing trauma-context safeguards: " + ", ".join(missing))
        return 1
    if "10.1007/s11916-021-00950-7" not in sources or "Direct evidence" not in sources:
        print("FAIL: review provenance and external-trauma evidence limit must remain attached")
        return 1
    metadata = row.get("trauma_context_reviewed_v410") or {}
    if "sparsely documented" not in str(metadata.get("external_trauma") or ""):
        print("FAIL: v41.0 trauma evidence calibration metadata missing")
        return 1

    print(
        "PASS: first-bite syndrome includes anatomically plausible trauma, explicitly sparse "
        "evidence, targeted examination/imaging, and occult-lesion safeguards."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
