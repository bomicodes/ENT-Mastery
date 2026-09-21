#!/usr/bin/env python3
"""Fail closed if the v40.9 pleomorphic-adenoma risk counseling disappears."""

import sys

import runtime_entry_pasha


DOMAIN = "Thyroid / Parathyroid / Salivary"
TOPIC = "Pleomorphic Adenoma / Warthin Tumor"


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
    text = " ".join(str(row.get(field) or "") for field in ("manage", "teach"))
    sources = " ".join(str(source) for source in row.get("source_basis") or [])
    required = ("1.5%", "9.5%-10%", "3.2%", "1.4%-7.3%", "high-grade CXPA", "duration")
    missing = [token for token in required if token not in text]
    if missing:
        print("FAIL: missing transformation-risk teaching: " + ", ".join(missing))
        return 1
    if "Eneroth" not in sources or "Levyn" not in sources or "10.1001/jamaoto.2023.3212" not in sources:
        print("FAIL: historical and contemporary transformation-risk provenance must remain attached")
        return 1
    if not row.get("transformation_risk_reviewed_v409"):
        print("FAIL: v40.9 review metadata missing")
        return 1

    print(
        "PASS: pleomorphic adenoma retains historical board figures, contemporary CXPA "
        "detection rates, uncertainty language, and primary-source provenance."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
