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


def _foundation_rationale(choice, is_correct):
    """Build anatomy-specific reasoning from the live option after any prior shuffle."""
    text = str(choice or "")
    lower = text.lower()
    if "ii b" in lower or "iib" in lower or ("spinal accessory" in lower and "level ii" in lower):
        reason = (
            "Level IIb lies posterosuperior to the spinal accessory nerve, so clearing this basin "
            "requires direct manipulation/retraction of CN XI and is a classic shoulder-morbidity risk point."
        )
    elif "omohyoid" in lower or "level iv" in lower:
        reason = (
            "Dividing the omohyoid in level IV is inferior to the level IIb accessory-nerve danger zone; "
            "its key nearby concerns are lower-neck lymphatic and vascular anatomy rather than direct IIb CN XI manipulation."
        )
    elif "facial artery" in lower or "level i" in lower or "submandibular" in lower:
        reason = (
            "Identifying the facial artery in level I is part of submandibular-triangle dissection and does not "
            "directly expose the level IIb segment of the spinal accessory nerve."
        )
    elif "superior thyroid" in lower:
        reason = (
            "Ligation of the superior thyroid artery is thyroid/superior-pole vascular work and is anatomically "
            "unrelated to clearing level IIb nodal tissue around CN XI."
        )
    else:
        reason = (
            "This maneuver does not represent the level IIb dissection around the spinal accessory nerve; "
            "localize the nodal level and the structure actually being manipulated before assigning the morbidity risk."
        )
    return ("Correct. " if is_correct else "") + reason


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

    # The reused v12.8 foundation item may have already had its choices reordered
    # before this semantic repair runs. Generate each rationale from the live option
    # and use the live answer index so choice/rationale alignment survives shuffling.
    foundation = by_id["v128_hn_03"]
    choices = list(foundation.get("choices") or [])
    try:
        answer = int(foundation.get("answer"))
    except (TypeError, ValueError):
        answer = -1
    if not 0 <= answer < len(choices):
        raise RuntimeError("v29.4: v128_hn_03 invalid live answer index")
    foundation["why_wrong"] = [
        _foundation_rationale(choice, i == answer) for i, choice in enumerate(choices)
    ]
    foundation["rationale_depth_v294"] = True
    foundation["rationale_alignment_v294"] = "live_choice_and_answer_index"

    return {
        "operative_concept_id": operative_cid,
        "complication_concept_id": complication_cid,
        "operative_ids": list(OPERATIVE_IDS),
        "complication_ids": list(COMPLICATION_IDS),
        "rationale_upgraded": ["v128_hn_03"],
    }
