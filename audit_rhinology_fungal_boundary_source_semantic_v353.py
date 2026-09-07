#!/usr/bin/env python3
"""v35.3 — fail closed on final-production fungal-rhinosinusitis boundary depth."""
import sys
import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPICS = ("Fungal Ball", "AFRS", "Invasive Fungal Rhinosinusitis")
PATCHED = ("Fungal Ball", "Invasive Fungal Rhinosinusitis")
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def fail(msg): print("FAIL: " + msg); return 1
def text(row): return " ".join(str(row.get(f) or "") for f in FIELDS).lower()
def sources(row): return " ".join(str(x) for x in (row.get("source_basis") or [])).lower()
def any_group(t, groups): return any(all(token in t for token in g) for g in groups)

REQ = {
    "Fungal Ball": [
        [("noninvasive", "no tissue invasion"), ("noninvasive", "without", "invasion")],
        [("unilateral", "maxillary"), ("unilateral", "sphenoid")],
        [("pathology", "tissue", "vascular invasion"), ("tissue", "vascular invasion")],
        [("systemic antifungal", "not", "standard"), ("not", "prolonged systemic antifungal")],
        [("fungal ball", "afrs", "invasive")],
    ],
    "Invasive Fungal Rhinosinusitis": [
        [("tissue", "angioinvasion"), ("tissue invasion", "vascular")],
        [("neutrop",), ("diabetes", "ketoacidosis")],
        [("biopsy", "histopath"), ("histopathologic", "tissue invasion")],
        [("ct", "mri", "orbital"), ("ct", "mri", "intracranial")],
        [("systemic antifungal", "debrid"), ("antifungal", "source control")],
        [("re-debrid",), ("serial", "reassessment")],
        [("black eschar", "do not"), ("not require black eschar",)],
    ],
}


def main():
    data = production.runtime_entry.data
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(r.get("topic") or ""): r for r in rows}
    failures = 0
    if len(rows) != 42:
        failures += fail(f"Rhinology canonical inventory changed: {len(rows)} != 42")
    ids = {topic: data._v6_item_id(DOMAIN, topic) for topic in TOPICS}
    for topic in TOPICS:
        row = by_topic.get(topic)
        if not row:
            failures += fail(f"missing exact live canonical topic {topic}")
            continue
        if data._v6_item_id(DOMAIN, row.get("topic")) != ids[topic]:
            failures += fail(f"{topic}: canonical ID drift")
        s = sources(row)
        for token in ("cummings", "k.j. lee", "pasha"):
            if token not in s:
                failures += fail(f"{topic}: missing textbook provenance {token!r}")
    for topic in PATCHED:
        row = by_topic.get(topic) or {}; t, s = text(row), sources(row)
        if not row.get("source_grounded_v353"):
            failures += fail(f"{topic}: missing v35.3 source-grounded marker")
        if not row.get("deliberate_review_v353"):
            failures += fail(f"{topic}: missing deliberate-review metadata")
        if "icar" not in s or "2021" not in s:
            failures += fail(f"{topic}: missing ICAR-RS 2021 source trail")
        for groups in REQ[topic]:
            if not any_group(t, groups):
                failures += fail(f"{topic}: missing semantic group {groups}")
    afrs = by_topic.get("AFRS") or {}
    if not afrs.get("source_grounded_v350"):
        failures += fail("AFRS: v35.0 predecessor source-grounded marker lost")
    afrs_t = text(afrs)
    for groups in [
        [("not invasive",), ("without invasion",), ("absence of tissue invasion",)],
        [("allergic mucin", "fungal"), ("eosinophilic", "fungal")],
    ]:
        if not any_group(afrs_t, groups):
            failures += fail(f"AFRS: lost comparator semantic group {groups}")
    ifr = by_topic.get("Invasive Fungal Rhinosinusitis") or {}
    if "ecmm" not in sources(ifr) or "mucormycosis" not in sources(ifr):
        failures += fail("Invasive Fungal Rhinosinusitis: missing ECMM/MSG-ERC mucormycosis guidance trail")
    if failures:
        print(f"RHINOLOGY_FUNGAL_BOUNDARY_V353_FAILED|{failures}")
        return 1
    print("RHINOLOGY_FUNGAL_BOUNDARY_V353_CANONICAL_IDS|" + "|".join(f"{k}={v}" for k,v in ids.items()))
    print("PASS: exact final-production Fungal Ball/AFRS/Invasive Fungal Rhinosinusitis boundary retains textbook/current-guidance provenance and senior decision semantics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
