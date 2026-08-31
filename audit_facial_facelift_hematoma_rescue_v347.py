#!/usr/bin/env python3
"""v34.7 — fail closed on facelift expanding-hematoma rescue in final Render assembly."""

import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Facial Plastics / Trauma"
TOPIC = "aging face injectables resurfacing"


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def main():
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [row for row in rows if norm(row.get("topic")) == TOPIC]
    if len(matches) != 1:
        return fail(f"expected exactly one live canonical Aging Face / Injectables / Resurfacing record, found {len(matches)}")

    row = matches[0]
    blob = " ".join(str(row.get(k, "")) for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
    failures = 0

    checks = {
        "expanding hematoma recognition": ("rapidly progressive", "swelling", "expanding hematoma"),
        "stable-versus-tension distinction": ("small, stable, nonexpanding", "tense or enlarging"),
        "flap perfusion consequence": ("skin-flap perfusion", "necrosis"),
        "airway-aware escalation": ("airway", "cervical swelling"),
        "prompt decompression and evacuation": ("prompt decompression", "evacuation"),
        "definitive source control": ("identify and control the source", "hemostasis"),
        "parallel physiologic correction": ("hypertension", "coagulopathy", "concurrently"),
        "post-rescue flap reassessment": ("reassess flap", "reaccumulation"),
    }
    for label, tokens in checks.items():
        if not all(token in blob for token in tokens):
            failures += fail(f"missing {label}: {tokens}")

    if not row.get("facialplastics_facelift_hematoma_rescue_v347"):
        failures += fail("v34.7 live marker missing")

    sources = " ".join(str(x) for x in row.get("source_basis") or []).lower()
    for token in ("cummings", "k.j. lee", "pasha", "azzi", "stewart", "baker", "ramanadham"):
        if token not in sources:
            failures += fail(f"missing provenance token {token!r}")

    if failures:
        print(f"\nFacelift expanding-hematoma rescue gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: final Render assembly contains explicit facelift expanding-hematoma recognition, urgent decompression/evacuation, definitive hemostasis, flap reassessment, and source trail.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
