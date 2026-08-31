#!/usr/bin/env python3
"""v34.8 — fail closed on phenotype-specific Head & Neck Oncology source trails."""

import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Head & Neck Oncology"


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def main():
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    merkel = [row for row in rows if "merkel" in str(row.get("topic") or "").lower()]
    if not merkel:
        return fail("no live Merkel cell carcinoma concept found")

    failures = 0
    for row in merkel:
        sources = " ".join(str(x) for x in row.get("source_basis") or []).lower()
        for token in ("cummings", "k.j. lee", "pasha"):
            if token not in sources:
                failures += fail(f"{row.get('topic')}: missing connected textbook source {token!r}")
        if "merkel cell carcinoma" not in sources:
            failures += fail(f"{row.get('topic')}: missing disease-specific Merkel guideline/review source")
        if "esmo-euracan" not in sources:
            failures += fail(f"{row.get('topic')}: missing ESMO-EURACAN Merkel guideline")
        if "kimball" not in sources or "2026" not in sources:
            failures += fail(f"{row.get('topic')}: missing contemporary head-and-neck Merkel review")

        # The prior v34.8 bug routed Merkel through the SCC bucket. An SCC source can coexist
        # only if separately justified, but it must never be the disease-specific source added
        # by the saturation layer.
        if (
            row.get("source_saturated_v348")
            and "squamous cell skin cancer, 2026" in sources
            and "nccn clinical practice guidelines in oncology: merkel cell carcinoma" not in sources
        ):
            failures += fail(f"{row.get('topic')}: Merkel source trail is still misrouted to cutaneous SCC")

    if failures:
        print(f"\nHead & Neck source-saturation gate FAILED with {failures} issue(s).")
        return 1

    print(f"PASS: {len(merkel)} live Merkel concept(s) retain Cummings/K.J. Lee/Pasha plus disease-specific Merkel guidance and contemporary review provenance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
