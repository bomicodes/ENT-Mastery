"""v28.8 — add the missing post-CRT response-management layer to the live salvage ladder.

The live H&N canonical inventory contains one salvage concept:
"Salvage Surgery After Radiation / Chemoradiation". Its existing foundation,
application, and senior-decision cases are clinically strong and are preserved.
This pass adds one distinct application/management case for the board-relevant
post-definitive-CRT response algorithm that the v28.7 Concept Hub introduced but
could not attach to a nonexistent second canonical card.
"""

DOMAIN = "Head & Neck Oncology"
TOPIC = "Salvage Surgery After Radiation / Chemoradiation"
QID = "v225_hn_salv_postcrt_app"


def apply_hn_salvage_ladder_alignment_v288(challenges, item_id_fn):
    cid = item_id_fn(DOMAIN, TOPIC)
    if not cid:
        raise RuntimeError("v28.8 missing live salvage canonical topic")
    existing = next((q for q in challenges if q.get("id") == QID), None)
    payload = {
        "id": QID,
        "domain": DOMAIN,
        "topic": TOPIC,
        "concept_id": cid,
        "learning_stage": "application",
        "stem": (
            "A patient with bulky node-positive oropharyngeal SCC completes definitive chemoradiation. "
            "At approximately 12 weeks, examination is reassuring and PET/CT shows complete metabolic response "
            "in the previously involved neck. What is the best neck-management principle?"
        ),
        "choices": [
            "Proceed with a planned neck dissection because the neck was node-positive before treatment",
            "Use surveillance rather than routine planned neck dissection after a reassuring complete response, reserving biopsy/re-imaging or salvage surgery for equivocal, persistent, or progressive disease",
            "Repeat PET/CT within 48 hours to prove the result before making any decision",
            "Perform salvage laryngectomy even though the primary site and neck have responded",
        ],
        "answer": 1,
        "explanation": (
            "After definitive chemoradiation, neck management is response-directed rather than based only on pretreatment nodal stage. "
            "A reassuring examination and complete metabolic response on appropriately timed PET/CT support surveillance instead of routine planned neck dissection. "
            "Equivocal or progressive findings require targeted reassessment—such as short-interval imaging, ultrasound-guided sampling, or direct biopsy according to site—before selecting salvage."
        ),
        "why_wrong": [
            "Pretreatment nodal burden alone does not mandate planned neck dissection after a complete post-treatment response; this would expose a responding patient to unnecessary surgery in an irradiated neck.",
            "Correct. Appropriately timed response assessment can safely direct surveillance, while suspicious residual or recurrent disease is confirmed and restaged before salvage is chosen.",
            "Repeating PET/CT almost immediately adds no useful biologic interval and does not resolve the inflammatory false-positive problem that makes very early post-treatment imaging difficult to interpret.",
            "Laryngectomy treats selected persistent or recurrent laryngeal disease; it is not indicated for a patient with reassuring primary-site and nodal response after definitive chemoradiation.",
        ],
        "board_pearl": (
            "After definitive CRT, do not perform a neck dissection simply because the neck used to be positive: assess response first. "
            "Complete metabolic response supports surveillance; persistent/progressive disease triggers targeted confirmation and salvage evaluation."
        ),
        "curveball": (
            "If the 12-week PET/CT is equivocal rather than clearly positive or negative, why can short-interval reassessment or targeted tissue sampling be preferable to reflex neck dissection?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "focus": "boards",
        "ladder_reviewed": True,
        "management_layer_v288": True,
    }
    if existing is None:
        challenges.append(payload)
        return {"added": 1, "updated": 0, "id": QID}
    existing.update(payload)
    return {"added": 0, "updated": 1, "id": QID}
