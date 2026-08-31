#!/usr/bin/env python3
"""v34.6 — fail closed on eyelid/periocular OCS rescue in final Render assembly."""

import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Facial Plastics / Trauma"
TOPIC = "eyelid reconstruction"


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def main():
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [row for row in rows if norm(row.get("topic")) == TOPIC]
    if len(matches) != 1:
        return fail(f"expected exactly one live canonical eyelid reconstruction record, found {len(matches)}")

    row = matches[0]
    blob = " ".join(str(row.get(k, "")) for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
    failures = 0

    checks = {
        "OCS recognition": ("orbital compartment syndrome", "proptosis", "relative afferent pupillary defect"),
        "vision-centered monitoring": ("visual acuity", "color vision", "pupils"),
        "do-not-delay-imaging stop rule": ("do not delay", "ct"),
        "standard emergency decompression": ("lateral canthotomy", "inferior cantholysis"),
        "compression/hematoma release": ("constricting dressing", "hematoma"),
        "mandatory post-decompression reassessment": ("reassess", "visual function"),
        "failed-decompression escalation": ("remains tight", "further orbital exploration/decompression"),
        "parallel hemostatic correction": ("coagulopathy", "in parallel"),
    }
    for label, tokens in checks.items():
        if not all(token in blob for token in tokens):
            failures += fail(f"missing {label}: {tokens}")

    if not row.get("facialplastics_eyelid_ocs_rescue_v346"):
        failures += fail("v34.6 live marker missing")

    sources = " ".join(str(x) for x in row.get("source_basis") or []).lower()
    for token in ("cummings", "k.j. lee", "pasha", "papadiochos", "mei"):
        if token not in sources:
            failures += fail(f"missing provenance token {token!r}")

    if failures:
        print(f"\nEyelid OCS rescue gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: final Render assembly contains explicit eyelid/periocular OCS recognition, immediate decompression, reassessment, escalation, and source trail.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
