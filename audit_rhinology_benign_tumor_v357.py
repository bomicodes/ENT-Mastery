#!/usr/bin/env python3
"""v35.7 — fail closed on lesion-specific Benign Sinonasal Tumor Framework depth."""
import sys
import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGET = "Benign Sinonasal Tumor Framework"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def fail(msg):
    print("FAIL: " + msg)
    return 1


def flat(row):
    return " ".join(str(row.get(f) or "") for f in FIELDS).lower()


def has_alt(text, alternatives):
    return any(all(token.lower() in text for token in alt) for alt in alternatives)


def main():
    data = production.runtime_entry.data
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    failures = 0

    if len(rows) != 42:
        failures += fail(f"Rhinology canonical inventory changed: {len(rows)} != 42")
    names = [str(r.get("topic") or "") for r in rows]
    if len(names) != len(set(names)):
        failures += fail("Rhinology canonical inventory contains duplicate topic names")

    predecessor = [r for r in rows if str(r.get("topic") or "") == "Unilateral Sinonasal Disease"]
    if len(predecessor) != 1 or not predecessor[0].get("source_grounded_v356"):
        failures += fail("v35.6 Unilateral Sinonasal Disease predecessor marker was lost")

    found = [r for r in rows if str(r.get("topic") or "") == TARGET]
    if len(found) != 1:
        failures += fail(f"expected exactly one exact-live {TARGET!r} row; found {len(found)}")
    if failures:
        print(f"RHINOLOGY_BENIGN_TUMOR_V357_FAILED|{failures}")
        return 1

    row = found[0]
    if not row.get("source_grounded_v357"):
        failures += fail("target missing v35.7 source marker")
    review = row.get("deliberate_review_v357") or {}
    for stage in ("foundation", "application", "senior_decision"):
        if not str(review.get(stage) or "").strip():
            failures += fail(f"target missing deliberate-review stage {stage}")

    expected_id = data._v6_item_id(DOMAIN, TARGET)
    if data._v6_item_id(DOMAIN, row.get("topic")) != expected_id:
        failures += fail("Benign Sinonasal Tumor Framework canonical ID drift")

    text = flat(row)
    groups = {
        "IP biologic distinction": (("inverted papilloma", "locally aggressive", "malignant"),),
        "IP attachment-directed surgery": (("attachment", "underlying bone", "surveillance"), ("attachment", "bone", "recurrence")),
        "JNA phenotype": (("juvenile nasopharyngeal angiofibroma", "adolescent male", "epistaxis"),),
        "JNA no-casual-biopsy bailout": (("do-not-casually-biopsy", "hemorrhage"), ("do-not-casually-biopsy", "vascular")),
        "JNA vascular planning": (("vascular planning", "embolization"),),
        "osteoma observation": (("osteoma", "incidental", "not itself an indication"), ("osteoma", "serial observation", "asymptomatic")),
        "osteoma intervention boundary": (("outflow obstruction", "orbital", "risk-benefit"), ("outflow", "deformity", "orbital")),
        "operative bailout": (("stop routine biopsy", "vascular", "skull base"),),
        "nonduplication handoff": (("v35.6", "unilateral sinonasal disease", "lesion-specific"),),
    }
    for label, alternatives in groups.items():
        if not has_alt(text, alternatives):
            failures += fail(f"target missing {label}: {alternatives}")

    source_text = " ".join(str(x) for x in (row.get("source_basis") or [])).lower()
    for token in ("cummings", "k.j. lee", "pasha", "pmid 37658764", "10.1002/alr.23262", "pmid 42207510", "10.1001/jamaoto.2026.1185"):
        if token not in source_text:
            failures += fail(f"target missing traceable source provenance {token!r}")

    if failures:
        print(f"RHINOLOGY_BENIGN_TUMOR_V357_FAILED|{failures}")
        return 1

    print(f"RHINOLOGY_BENIGN_TUMOR_CANONICAL_ID_V357|{TARGET}={expected_id}")
    print("PASS: exact benign sinonasal tumor card fail-closes IP attachment/surveillance, JNA vascular-biopsy danger, and osteoma observation/intervention decisions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
