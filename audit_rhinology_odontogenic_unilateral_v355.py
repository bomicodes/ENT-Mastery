#!/usr/bin/env python3
"""v35.5 — fail closed on exact-live CRSsNP odontogenic/unilateral decision depth."""
import sys
import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "CRSsNP"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def fail(msg):
    print("FAIL: " + msg)
    return 1


def flat(row):
    return " ".join(str(row.get(f) or "") for f in FIELDS).lower()


def sources(row):
    return " ".join(str(x) for x in (row.get("source_basis") or [])).lower()


def main():
    data = production.runtime_entry.data
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    failures = 0
    if len(rows) != 42:
        failures += fail(f"Rhinology canonical inventory changed: {len(rows)} != 42")
    matches = [r for r in rows if str(r.get("topic") or "") == TOPIC]
    if len(matches) != 1:
        failures += fail(f"expected exactly one exact-live {TOPIC!r} row; found {len(matches)}")
        print(f"ODONTOGENIC_UNILATERAL_V355_FAILED|{failures}")
        return 1
    row = matches[0]
    canonical_id = data._v6_item_id(DOMAIN, TOPIC)
    if data._v6_item_id(DOMAIN, row.get("topic")) != canonical_id:
        failures += fail("CRSsNP canonical ID drift")
    if not row.get("source_grounded_v350"):
        failures += fail("CRSsNP lost v35.0 predecessor source marker")
    if not row.get("source_grounded_v354"):
        failures += fail("CRSsNP lost v35.4 predecessor source marker")
    if not row.get("source_grounded_v355"):
        failures += fail("CRSsNP missing v35.5 source marker")
    if not row.get("deliberate_review_v355"):
        failures += fail("CRSsNP missing v35.5 deliberate-review metadata")

    t = flat(row)
    semantic_groups = {
        "unilateral focal-source trigger": (("unilateral", "maxillary", "focal-source"), ("unilateral", "maxillary", "odontogenic")),
        "dental history": (("implant", "extraction", "oroantral"), ("endodontic", "implant", "sinus-lift")),
        "CT dental inspection": (("periapical", "periodontal", "sinus floor"),),
        "ENT plus dental confirmation": (("ent", "confirm", "dental", "confirm"), ("confirm the sinus", "dental evaluation")),
        "antibiotics not source control": (("repeated antibiotics", "not definitive"), ("antibiotics", "source control")),
        "individualized sequencing": (("no", "rigid", "dental-first", "ess-first"), ("no universal", "dental-first", "ess-first")),
        "oroantral/foreign-body management": (("foreign", "oroantral", "dental"),),
        "unilateral bailout": (("neoplasm", "invasive fungal", "orbital"), ("tumor", "invasive fungal", "intracranial")),
    }
    for label, alternatives in semantic_groups.items():
        if not any(all(token in t for token in alt) for alt in alternatives):
            failures += fail(f"CRSsNP missing {label}: {alternatives}")

    s = sources(row)
    for token in ("cummings", "k.j. lee", "pasha", "diagnosing odontogenic sinusitis", "management of odontogenic sinusitis", "2024"):
        if token not in s:
            failures += fail(f"CRSsNP missing source provenance {token!r}")

    if failures:
        print(f"ODONTOGENIC_UNILATERAL_V355_FAILED|{failures}")
        return 1
    print(f"RHINOLOGY_ODONTOGENIC_UNILATERAL_V355_CANONICAL_ID|{TOPIC}={canonical_id}")
    print("PASS: exact-live CRSsNP now fail-closes odontogenic/unilateral recognition, dual-specialty confirmation, source control, individualized sequencing and atypical-disease bailout")
    return 0


if __name__ == "__main__":
    sys.exit(main())
