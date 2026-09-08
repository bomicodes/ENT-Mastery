#!/usr/bin/env python3
"""v35.4 — fail closed on exact-live CRSsNP secondary host-factor depth."""
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
        print(f"SECONDARY_CRS_HOST_V354_FAILED|{failures}")
        return 1
    row = matches[0]
    canonical_id = data._v6_item_id(DOMAIN, TOPIC)
    if data._v6_item_id(DOMAIN, row.get("topic")) != canonical_id:
        failures += fail("CRSsNP canonical ID drift")
    if not row.get("source_grounded_v350"):
        failures += fail("CRSsNP lost v35.0 predecessor source marker")
    if not row.get("source_grounded_v354"):
        failures += fail("CRSsNP missing v35.4 source marker")
    if not row.get("deliberate_review_v354"):
        failures += fail("CRSsNP missing v35.4 deliberate-review metadata")

    t = flat(row)
    semantic_groups = {
        "humoral screen": (("quantitative", "igg", "iga", "igm"),),
        "functional antibody assessment": (("vaccine", "pneumococcal", "antibody"), ("antigen-specific", "vaccine")),
        "IgG subclass guardrail": (("igg-subclass", "not", "diagnose"), ("igg-subclass", "not", "exclude")),
        "immune referral": (("allergy/immunology", "abnormal"), ("allergy/immunology", "severe", "unusual")),
        "CF diagnostic pathway": (("sweat chloride", "cftr"),),
        "PCD phenotype": (("bronchiectasis", "laterality", "infertility"), ("neonatal", "laterality", "mucociliary")),
        "PCD multimodal testing": (("nasal nitric oxide", "genetics", "tem"),),
        "no single PCD rule-out": (("no single", "rules out pcd"), ("no single negative", "pcd")),
        "host/sinus parallel management": (("host disorder", "sinonasal", "parallel"),),
        "surgery non-cure boundary": (("surgery", "not a cure", "cftr"), ("ess", "does not cure", "mucociliary")),
        "diagnostic bailout": (("refractory", "ask why"), ("treatment repeatedly fails", "host factor")),
    }
    for label, alternatives in semantic_groups.items():
        if not any(all(token in t for token in alt) for alt in alternatives):
            failures += fail(f"CRSsNP missing {label}: {alternatives}")

    s = sources(row)
    for token in ("cummings", "k.j. lee", "pasha", "adult sinusitis update", "2025", "primary immunodeficiency", "cystic fibrosis foundation", "primary ciliary dyskinesia", "ers/ats"):
        if token not in s:
            failures += fail(f"CRSsNP missing source provenance {token!r}")

    if failures:
        print(f"SECONDARY_CRS_HOST_V354_FAILED|{failures}")
        return 1
    print(f"RHINOLOGY_SECONDARY_CRS_V354_CANONICAL_ID|{TOPIC}={canonical_id}")
    print("PASS: exact-live CRSsNP retains v35.0 depth and now fail-closes immune/CF/PCD secondary-host workup, multidisciplinary management and diagnostic bailout decisions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
