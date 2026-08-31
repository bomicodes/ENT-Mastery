#!/usr/bin/env python3
"""v34.3 — fail closed on skin-graft vascularity semantics in the final Render assembly."""

import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Facial Plastics / Trauma"
TOPIC = "Skin Graft Selection"


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

    if "avascular cutaneous coverage" in blob:
        failures += fail("ambiguous 'avascular cutaneous coverage' wording reappeared")
    if "without its own vascular pedicle" not in blob and "without an intrinsic blood supply" not in blob:
        failures += fail("skin graft is no longer defined as nonvascularized tissue transfer")
    if "vascularized recipient bed" not in blob:
        failures += fail("recipient-bed vascularity requirement is missing")
    if "flap transfers tissue with its own blood supply" not in blob and "vascular pedicle" not in blob:
        failures += fail("graft-versus-flap vascular distinction is missing")
    if "avascular recipient surface" not in blob:
        failures += fail("avascular-bed reconstructive stop rule is missing")
    if not row.get("facialplastics_graft_vascular_semantics_v343"):
        failures += fail("v34.3 live marker missing")

    sources = " ".join(str(x) for x in row.get("source_basis") or []).lower()
    for token in ("cummings", "k.j. lee", "pasha", "schwartzberg", "statpearls"):
        if token not in sources:
            failures += fail(f"missing provenance token {token!r}")

    if failures:
        print(f"\nSkin-graft vascularity semantic gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: final Render assembly defines skin graft as nonvascularized transfer onto a vascularized recipient bed, distinct from flap perfusion.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
