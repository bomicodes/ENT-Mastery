"""v29.4 — keep neck-dissection operative judgment distinct from complication rescue.

The canonical Head & Neck Oncology curriculum intentionally contains both
"Neck Dissection" and "Complications of Neck Surgery". Their staged ladders are
already clinically complementary, so this pass preserves the questions rather
than manufacturing new difficulty. It strengthens the one reused foundation
rationale that remained generic and marks the two ladders with explicit semantic
roles for regression testing.
"""

DOMAIN = "Head & Neck Oncology"
OPERATIVE_TOPIC = "Neck Dissection"
COMPLICATION_TOPIC = "Complications of Neck Surgery"

OPERATIVE_IDS = (
    "v128_hn_03",
    "v219_hn_neck_app",
    "v219_hn_neck_snr",
)
COMPLICATION_IDS = (
    "v231_hn_neckcomp_fnd",
    "v231_hn_neckcomp_app",
    "v231_hn_neckcomp_snr",
)

FOUNDATION_WHY = [
    "Correct. Level IIb lies posterosuperior to the spinal accessory nerve, so clearing this basin requires direct manipulation/retraction of CN XI and is a classic shoulder-morbidity risk point.",
    "Dividing the omohyoid in level IV is inferior to the level-IIb accessory-nerve danger zone; its key nearby concerns are lower-neck lymphatic and vascular anatomy rather than direct IIb CN XI manipulation.",
    "Identifying the facial artery in level I is part of submandibular-triangle dissection and does not directly expose the level-IIb segment of the spinal accessory nerve.",
    "Ligation of the superior thyroid artery is thyroid/superior-pole vascular work and is anatomically unrelated to clearing level-IIb nodal tissue around CN XI.",
]


def apply_hn_neck_semantic_alignment_v294(challenges, id_fn):
    by_id = {str(q.get("id") or ""): q for q in challenges}
    operative_cid = id_fn(DOMAIN, OPERATIVE_TOPIC)
    complication_cid = id_fn(DOMAIN, COMPLICATION_TOPIC)

    missing = [qid for qid in OPERATIVE_IDS + COMPLICATION_IDS if qid not in by_id]
    if missing:
        raise RuntimeError("v29.4: expected neck semantic cases missing: " + ",".join(missing))

    for qid in OPERATIVE_IDS:
        q = by_id[qid]
        if q.get("concept_id") != operative_cid:
            raise RuntimeError(f"v29.4: {qid} operative canonical link drift: {q.get('concept_id')!r} != {operative_cid!r}")
        if not q.get("ladder_reviewed"):
            raise RuntimeError(f"v29.4: {qid} lost ladder_reviewed metadata")
        q["semantic_role_v294"] = "operative_selection_anatomy_and_oncologic_extent"
        q["deliberate_review_v294"] = "Preserved strong neck-dissection ladder; protected operative selection/anatomy from postoperative-complication duplication."

    for qid in COMPLICATION_IDS:
        q = by_id[qid]
        if q.get("concept_id") != complication_cid:
            raise RuntimeError(f"v29.4: {qid} complication canonical link drift: {q.get('concept_id')!r} != {complication_cid!r}")
        if not q.get("ladder_reviewed"):
            raise RuntimeError(f"v29.4: {qid} lost ladder_reviewed metadata")
        q["semantic_role_v294"] = "postoperative_complication_recognition_and_rescue"
        q["deliberate_review_v294"] = "Preserved strong complication ladder; protected postoperative rescue from duplicating neck-dissection indication/anatomy decisions."

    # This reused v12.8 foundation item was clinically useful but one distractor
    # rationale still used a generic 'not the key maneuver' explanation. Upgrade
    # every option to anatomy-specific reasoning without changing the question.
    by_id["v128_hn_03"]["why_wrong"] = list(FOUNDATION_WHY)
    by_id["v128_hn_03"]["rationale_depth_v294"] = True

    return {
        "operative_concept_id": operative_cid,
        "complication_concept_id": complication_cid,
        "operative_ids": list(OPERATIVE_IDS),
        "complication_ids": list(COMPLICATION_IDS),
        "rationale_upgraded": ["v128_hn_03"],
    }
