#!/usr/bin/env python3
"""v35.6 — fail closed on the exact Odontogenic + Unilateral canonical cards."""
import sys
import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGETS = ("Odontogenic Sinusitis", "Unilateral Sinonasal Disease")
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def fail(msg):
    print("FAIL: " + msg)
    return 1


def flat(row):
    return " ".join(str(row.get(f) or "") for f in FIELDS).lower()


def sources(row):
    return " ".join(str(x) for x in (row.get("source_basis") or [])).lower()


def has_alt(text, alternatives):
    return any(all(token.lower() in text for token in alt) for alt in alternatives)


def main():
    data = production.runtime_entry.data
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    failures = 0

    if len(rows) != 42:
        failures += fail(f"Rhinology canonical inventory changed: {len(rows)} != 42")
    topic_names = [str(r.get("topic") or "") for r in rows]
    if len(topic_names) != len(set(topic_names)):
        failures += fail("Rhinology canonical inventory contains duplicate topic names")

    # Predecessor protection: v35.5 must still be active on its exact CRSsNP target.
    crs = [r for r in rows if str(r.get("topic") or "") == "CRSsNP"]
    if len(crs) != 1 or not crs[0].get("source_grounded_v355"):
        failures += fail("v35.5 CRSsNP predecessor marker was lost")

    matches = {topic: [r for r in rows if str(r.get("topic") or "") == topic] for topic in TARGETS}
    for topic, found in matches.items():
        if len(found) != 1:
            failures += fail(f"expected exactly one exact-live {topic!r} row; found {len(found)}")

    if failures:
        print(f"RHINOLOGY_EXACT_ODS_UNILATERAL_V356_FAILED|{failures}")
        return 1

    ods = matches["Odontogenic Sinusitis"][0]
    uni = matches["Unilateral Sinonasal Disease"][0]

    for topic, row in (("Odontogenic Sinusitis", ods), ("Unilateral Sinonasal Disease", uni)):
        if not row.get("source_grounded_v356"):
            failures += fail(f"{topic} missing v35.6 source marker")
        review = row.get("deliberate_review_v356") or {}
        for stage in ("foundation", "application", "senior_decision"):
            if not str(review.get(stage) or "").strip():
                failures += fail(f"{topic} missing deliberate-review stage {stage}")
        expected_id = data._v6_item_id(DOMAIN, topic)
        if data._v6_item_id(DOMAIN, row.get("topic")) != expected_id:
            failures += fail(f"{topic} canonical ID drift")

    ods_text = flat(ods)
    ods_groups = {
        "causal dental-source foundation": (("causally linked", "dental pathology"), ("dental-source", "sinusitis")),
        "unilateral suspicion not proof": (("unilateral", "maxillary", "not proof"), ("unilateral", "maxillary", "raise suspicion")),
        "targeted dental history": (("endodontic", "extraction", "implant", "oroantral"),),
        "CT dental inspection": (("periapical", "periodontal", "sinus floor"),),
        "dual-specialty diagnosis": (("ent confirms sinusitis", "dental", "confirms"), ("ent", "confirms", "dental provider", "confirms")),
        "antibiotics not source control": (("repeated antibiotics", "not definitive", "source control"),),
        "individualized sequencing": (("do not teach", "universal", "dental-first", "ess-first"), ("individualize", "dental", "ess")),
        "oroantral/foreign body source management": (("displaced dental material", "oroantral", "dental/oral surgery"),),
        "complicated bailout": (("orbital", "intracranial", "urgent"),),
        "atypical unilateral bailout": (("neoplasm", "invasive fungal", "destructive", "necrotic"),),
    }
    for label, alternatives in ods_groups.items():
        if not has_alt(ods_text, alternatives):
            failures += fail(f"Odontogenic Sinusitis missing {label}: {alternatives}")

    uni_text = flat(uni)
    uni_groups = {
        "phenotype not diagnosis": (("diagnostic phenotype", "not a diagnosis"),),
        "broad unilateral differential": (("odontogenic", "fungal", "benign", "malignancy", "foreign body"),),
        "red-flag history": (("epistaxis", "facial numbness", "vision", "cranial neuropathy"),),
        "endoscopy plus CT localization": (("nasal endoscopy", "ct", "dentition", "destructive bone"),),
        "MRI mass/extension mapping": (("contrast-enhanced mri", "skull-base", "orbital", "perineural"),),
        "cause-directed management": (("route management to the cause", "odontogenic", "fungal", "tumor"),),
        "unsafe biopsy bailout": (("before reflexively biopsying", "vascular", "intracranial", "office biopsy"),),
        "urgent invasive/orbital/neuro bailout": (("necrosis", "orbital", "cranial neuropathy", "intracranial"),),
    }
    for label, alternatives in uni_groups.items():
        if not has_alt(uni_text, alternatives):
            failures += fail(f"Unilateral Sinonasal Disease missing {label}: {alternatives}")

    for topic, row in (("Odontogenic Sinusitis", ods), ("Unilateral Sinonasal Disease", uni)):
        source_text = sources(row)
        for token in ("cummings", "k.j. lee", "pasha"):
            if token not in source_text:
                failures += fail(f"{topic} missing textbook provenance {token!r}")

    ods_sources = sources(ods)
    for token in ("pmid 33583151", "10.1002/alr.22777", "pmid 32506807", "10.1002/alr.22598", "10.1038/s41368-024-00278-z", "pmid 39428206"):
        if token not in ods_sources:
            failures += fail(f"Odontogenic Sinusitis missing traceable source provenance {token!r}")

    uni_sources = sources(uni)
    if "acr appropriateness criteria" not in uni_sources or "sinonasal disease" not in uni_sources:
        failures += fail("Unilateral Sinonasal Disease missing ACR suspected-mass imaging provenance")

    if failures:
        print(f"RHINOLOGY_EXACT_ODS_UNILATERAL_V356_FAILED|{failures}")
        return 1

    for topic in TARGETS:
        print(f"RHINOLOGY_EXACT_CANONICAL_ID_V356|{topic}={data._v6_item_id(DOMAIN, topic)}")
    print("PASS: exact canonical Odontogenic Sinusitis and Unilateral Sinonasal Disease cards now fail-close diagnosis, source control, imaging, safe-tissue and complication bailouts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
