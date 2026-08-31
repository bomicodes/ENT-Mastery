#!/usr/bin/env python3
"""v34.5 — fail closed on forehead-flap vascular compromise rescue in final Render assembly."""

import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Facial Plastics / Trauma"
TOPIC = "Forehead Flap Nasal Reconstruction"


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def main():
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [row for row in rows if str(row.get("topic", "")).strip().lower() == TOPIC.lower()]
    if len(matches) != 1:
        return fail(f"expected exactly one live {TOPIC!r} record, found {len(matches)}")

    row = matches[0]
    blob = " ".join(str(row.get(k, "")) for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
    failures = 0

    checks = {
        "venous-vs-arterial recognition": ("venous congestion", "pale, cool"),
        "mechanical rescue": ("release constricting", "pedicle twist", "hematoma"),
        "mandatory reassessment": ("reassess",),
        "operative escalation": ("operative reassessment",),
        "nontraumatic bailout": ("do not repeatedly needle",),
        "selective leech salvage": ("medicinal leech", "selective salvage adjunct"),
        "Aeromonas/blood-loss safety": ("aeromonas", "blood loss"),
        "pedicle-division stop rule": ("do not divide", "perfusion or healing is questionable"),
    }
    for label, tokens in checks.items():
        if not all(token in blob for token in tokens):
            failures += fail(f"missing {label}: {tokens}")

    if not row.get("facialplastics_forehead_rescue_v345"):
        failures += fail("v34.5 live marker missing")

    sources = " ".join(str(x) for x in row.get("source_basis") or []).lower()
    for token in ("cummings", "k.j. lee", "pasha", "boissiere", "herlin", "moubayed", "gates"):
        if token not in sources:
            failures += fail(f"missing provenance token {token!r}")

    if failures:
        print(f"\nForehead-flap rescue gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: final Render assembly contains explicit forehead-flap compromise recognition, mechanical rescue, escalation, adjunct safety, and pedicle-division stop logic.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
