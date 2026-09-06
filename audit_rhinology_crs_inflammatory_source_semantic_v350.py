#!/usr/bin/env python3
"""v35.0 — fail closed on final-production CRS inflammatory decision/source depth."""
import sys
import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPICS = ("CRS Phenotyping", "AERD", "CRSsNP", "CRSwNP", "AFRS")
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
 "CRS Phenotyping": [(("objective", "endoscopy"), ("objective", "ct")), (("phenotype", "endotype"),), (("biologic", "without nasal polyps"), ("biologic", "crssnp")), (("topical", "corticosteroid"),)],
 "AERD": [(("asthma", "crswnp", "cox-1"),), (("aspirin desensitization", "atad"),), (("biologic", "individual"), ("biologic", "patient")), (("challenge", "controlled"),)],
 "CRSsNP": [(("objective", "inflammation"),), (("antibiotic", "not"), ("avoid", "antibiotic")), (("biologic", "without nasal polyps"), ("biologic", "crssnp")), (("ess", "topical"),)],
 "CRSwNP": [(("asthma", "aerd"),), (("systemic", "steroid"),), (("biologic", "ess"),), (("topical", "therapy"),)],
 "AFRS": [(("eosinophilic", "mucin"),), (("fungal", "invasion"),), (("ess", "topical"),), (("dupilumab", "2026"),)],
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
        if not row.get("source_grounded_v350"): failures += fail(f"{topic}: missing v35.0 source-grounded marker")
        if not row.get("deliberate_review_v350"): failures += fail(f"{topic}: missing deliberate-review metadata")
        s = sources(row); t = text(row)
        for token in ("cummings", "k.j. lee", "pasha", "adult sinusitis update", "2025", "surgical management of chronic rhinosinusitis"):
            if token not in s: failures += fail(f"{topic}: missing source provenance {token!r}")
        for groups in REQ[topic]:
            if not require(t, groups): failures += fail(f"{topic}: missing semantic group {groups}")
    afr = by_topic.get("AFRS") or {}
    if "2026" not in sources(afr) or "dupilumab" not in sources(afr): failures += fail("AFRS: missing explicit post-textbook 2026 dupilumab indication trail")
    crswnp = by_topic.get("CRSwNP") or {}
    if "tezepelumab" not in sources(crswnp) or "2025" not in sources(crswnp): failures += fail("CRSwNP: missing 2025 tezepelumab update trail")
    if failures:
        print(f"CRS_INFLAMMATORY_V350_FAILED|{failures}"); return 1
    print("RHINOLOGY_CRS_V350_CANONICAL_IDS|" + "|".join(f"{k}={v}" for k,v in ids.items()))
    print("PASS: final-production CRS phenotype/AERD/CRSsNP/CRSwNP/AFRS retain textbook provenance, current-guidance distinctions, deliberate-review metadata and senior decisions")
    return 0

if __name__ == "__main__": sys.exit(main())
