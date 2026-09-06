#!/usr/bin/env python3
"""v35.1 — fail closed on final-production nonallergic-rhinitis and olfaction decision/source depth."""
import sys
import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
NAR_TOPIC = "Nonallergic Rhinitis / Rhinitis Medicamentosa"
TOPICS = (NAR_TOPIC, "Olfactory Dysfunction")
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def fail(msg):
    print("FAIL: " + msg); return 1

def text(row):
    return " ".join(str(row.get(f) or "") for f in FIELDS).lower()

def sources(row):
    return " ".join(str(x) for x in (row.get("source_basis") or [])).lower()

def require(t, groups):
    return any(all(token in t for token in group) for group in groups)

REQ = {
    NAR_TOPIC: [
        (("intranasal antihistamine", "intranasal corticosteroid"),),
        (("ipratropium", "watery rhinorrhea"), ("ipratropium", "gustatory")),
        (("local allergic rhinitis", "nares"),),
        (("csf", "unilateral"),),
        (("surgery", "structural"), ("procedures", "refractory")),
    ],
    "Olfactory Dysfunction": [
        (("conductive", "sensorineural"),),
        (("psychophysical", "testing"),),
        (("ct", "mri"),),
        (("olfactory training",),),
        (("safety counseling",),),
        (("smoke", "detectors"), ("smoke", "spoiled food")),
    ],
}


def main():
    # Audit the real Render/final-production boundary, never the earlier runtime assembly.
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
            failures += fail(f"missing exact live canonical topic {topic}"); continue
        if data._v6_item_id(DOMAIN, row.get("topic")) != ids[topic]:
            failures += fail(f"{topic}: canonical ID drift")
        if not row.get("source_grounded_v351"):
            failures += fail(f"{topic}: missing v35.1 source-grounded marker")
        if not row.get("deliberate_review_v351"):
            failures += fail(f"{topic}: missing deliberate-review metadata")
        s = sources(row); t = text(row)
        for token in ("cummings", "k.j. lee", "pasha"):
            if token not in s:
                failures += fail(f"{topic}: missing textbook provenance {token!r}")
        if topic == NAR_TOPIC and not any(x in t for x in ("irritant", "weather", "gustatory", "rhinitis medicamentosa")):
            failures += fail(f"{NAR_TOPIC}: missing phenotype/trigger framework")
        for group in REQ[topic]:
            if not require(t, group):
                failures += fail(f"{topic}: missing semantic group {group}")
    nar = by_topic.get(NAR_TOPIC) or {}
    if "rhinitis 2020" not in sources(nar) or "practice parameter" not in sources(nar):
        failures += fail(f"{NAR_TOPIC}: missing Rhinitis 2020 practice-parameter trail")
    olf = by_topic.get("Olfactory Dysfunction") or {}
    if "icar:olfaction" not in sources(olf) or "2022" not in sources(olf):
        failures += fail("Olfactory Dysfunction: missing ICAR:Olfaction source trail")
    if failures:
        print(f"RHINOLOGY_NONALLERGIC_OLFACTION_V351_FAILED|{failures}"); return 1
    print("RHINOLOGY_NONALLERGIC_OLFACTION_V351_CANONICAL_IDS|" + "|".join(f"{k}={v}" for k,v in ids.items()))
    print("PASS: final-production Nonallergic Rhinitis / Rhinitis Medicamentosa and Olfactory Dysfunction retain textbook provenance, consensus guidance, deliberate-review metadata and senior decision semantics")
    return 0

if __name__ == "__main__": sys.exit(main())