#!/usr/bin/env python3
"""v35.2 — fail closed on final-production allergy-testing/AIT source and decision depth."""
import sys
import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPICS = ("Allergy Testing & Interpretation", "Allergen Immunotherapy — SCIT / SLIT")
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")

def fail(msg): print("FAIL: " + msg); return 1
def text(row): return " ".join(str(row.get(f) or "") for f in FIELDS).lower()
def sources(row): return " ".join(str(x) for x in (row.get("source_basis") or [])).lower()
def any_group(t, groups): return any(all(token in t for token in g) for g in groups)

REQ = {
    "Allergy Testing & Interpretation": [
        [("sensitization", "clinical"), ("sensitization", "symptom")],
        [("skin-prick", "serum", "specific ige"), ("skin", "serum", "specific ige")],
        [("food panel",), ("indiscriminate", "panel")],
        [("total ige", "eosinophil")],
        [("local allergic rhinitis", "negative")],
        [("serial", "testing", "immunotherapy"), ("routine", "efficacy", "retesting")],
    ],
    "Allergen Immunotherapy — SCIT / SLIT": [
        [("clinically relevant", "sensitization")],
        [("asthma", "uncontrolled")],
        [("anaphylaxis", "recognize", "treat"), ("anaphylaxis", "preparedness")],
        [("scit", "slit")],
        [("fda-approved", "aqueous", "not fda-approved"), ("fda", "compounded aqueous")],
        [("odactra", "5", "65")],
        [("3 years",), ("three years",), ("3 years", "duration")],
    ],
}

def main():
    data = production.runtime_entry.data
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(r.get("topic") or ""): r for r in rows}
    failures = 0
    if len(rows) != 42: failures += fail(f"Rhinology canonical inventory changed: {len(rows)} != 42")
    ids = {topic: data._v6_item_id(DOMAIN, topic) for topic in TOPICS}
    for topic in TOPICS:
        row = by_topic.get(topic)
        if not row:
            failures += fail(f"missing exact live canonical topic {topic}"); continue
        if data._v6_item_id(DOMAIN, row.get("topic")) != ids[topic]: failures += fail(f"{topic}: canonical ID drift")
        if not row.get("source_grounded_v352"): failures += fail(f"{topic}: missing v35.2 source-grounded marker")
        if not row.get("deliberate_review_v352"): failures += fail(f"{topic}: missing deliberate-review metadata")
        s, t = sources(row), text(row)
        for token in ("cummings", "k.j. lee", "pasha"):
            if token not in s: failures += fail(f"{topic}: missing textbook provenance {token!r}")
        for groups in REQ[topic]:
            if not any_group(t, groups): failures += fail(f"{topic}: missing semantic group {groups}")
    testing = by_topic.get(TOPICS[0]) or {}; ait = by_topic.get(TOPICS[1]) or {}
    if "rhinitis 2020" not in sources(testing) or "2024" not in sources(testing): failures += fail("Allergy Testing: missing Rhinitis 2020 / 2024 AIT guidance trail")
    if "immunotherapy for inhalant allergy" not in sources(ait) or "2024" not in sources(ait): failures += fail("AIT: missing 2024 inhalant-immunotherapy guideline trail")
    if "fda" not in sources(ait) or "odactra" not in sources(ait): failures += fail("AIT: missing current FDA ODACTRA source trail")
    if failures:
        print(f"RHINOLOGY_ALLERGY_TESTING_AIT_V352_FAILED|{failures}"); return 1
    print("RHINOLOGY_ALLERGY_TESTING_AIT_V352_CANONICAL_IDS|" + "|".join(f"{k}={v}" for k,v in ids.items()))
    print("PASS: exact final-production Allergy Testing and SCIT/SLIT concepts retain textbook/current-guidance provenance and senior decision semantics")
    return 0

if __name__ == "__main__": sys.exit(main())
