#!/usr/bin/env python3
"""v34.8 — fail closed on phenotype-specific Head & Neck Oncology source trails."""

import sys
import runtime_entry_pasha
from deep_curriculum_headneck_v348 import _guideline_sources


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

        if (
            row.get("source_saturated_v348")
            and "squamous cell skin cancer, 2026" in sources
            and "nccn clinical practice guidelines in oncology: merkel cell carcinoma" not in sources
        ):
            failures += fail(f"{row.get('topic')}: Merkel source trail is still misrouted to cutaneous SCC")

    # Guard the phenotype router itself even if the canonical inventory changes. Mucosal
    # melanoma must never fall through to the cutaneous-melanoma NCCN family.
    mucosal_probe = " ".join(_guideline_sources("Sinonasal Mucosal Melanoma")).lower()
    for token in ("head and neck cancers", "mucosal melanoma", "moya-plana", "refcor", "thariat"):
        if token not in mucosal_probe:
            failures += fail(f"mucosal-melanoma router missing disease-specific source token {token!r}")
    if "cutaneous melanoma" in mucosal_probe:
        failures += fail("mucosal-melanoma router incorrectly falls through to cutaneous melanoma guidance")

    # If a live mucosal-melanoma concept exists, verify the final Render assembly carries the
    # same distinction rather than only testing the helper in isolation.
    mucosal_live = [
        row for row in rows
        if "melanoma" in str(row.get("topic") or "").lower()
        and any(token in str(row.get("topic") or "").lower() for token in ("mucosal", "sinonasal", "nasal", "oral"))
    ]
    for row in mucosal_live:
        sources = " ".join(str(x) for x in row.get("source_basis") or []).lower()
        for token in ("cummings", "k.j. lee", "pasha", "mucosal melanoma", "refcor"):
            if token not in sources:
                failures += fail(f"{row.get('topic')}: missing mucosal-melanoma provenance token {token!r}")
        if row.get("source_saturated_v348") and "cutaneous melanoma, 2026" in sources and "refcor" not in sources:
            failures += fail(f"{row.get('topic')}: live mucosal melanoma remains misrouted as cutaneous melanoma")

    if failures:
        print(f"\nHead & Neck source-saturation gate FAILED with {failures} issue(s).")
        return 1

    print(
        f"PASS: {len(merkel)} live Merkel concept(s) retain disease-specific provenance; "
        f"mucosal-melanoma routing is separated from cutaneous melanoma"
        + (f" across {len(mucosal_live)} live mucosal-melanoma concept(s)." if mucosal_live else ".")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
