"""v29.8 — sharpen the live NOE application layer without adding redundant volume.

The existing ladder already preserves strong MCT anatomy and complex craniofacial
sequencing. This alignment upgrades only the application decision so residents
must distinguish a comminuted tendon-bearing type II central fragment from true
type III MCT avulsion and choose fixation versus canthopexy accordingly.
"""

TARGET_ID = "v258_fpt_noe_app"


def apply_facial_noe_management_alignment_v298(challenges, item_id_fn):
    target_cid = item_id_fn("Facial Plastics / Trauma", "NOE Fracture")
    updated = []
    for q in challenges:
        if q.get("id") != TARGET_ID:
            continue
        q.update({
            "domain": "Facial Plastics / Trauma",
            "topic": "NOE Fracture",
            "concept_id": target_cid,
            "learning_stage": "application",
            "stem": (
                "CT after central midface trauma shows a comminuted NOE injury, but the medial "
                "canthal tendon remains firmly attached to a sizeable central bone fragment. The "
                "fragment itself can be anatomically reduced to stable surrounding bone. Which "
                "classification-and-management principle is most appropriate?"
            ),
            "choices": [
                "This is a type II pattern: restore the central facial skeleton and rigidly stabilize the tendon-bearing fragment; reserve canthopexy for an attachment that cannot be reliably restored with that fragment",
                "This is a type III pattern by definition, so detach the intact medial canthal tendon from its fragment and perform transnasal canthopexy in every case",
                "The medial canthal tendon is irrelevant once comminution is present; reduce only the nasal dorsum and accept the intercanthal distance",
                "Because the tendon remains attached to bone, no operative restoration of central facial width or nasal projection is necessary",
            ],
            "answer": 0,
            "explanation": (
                "Markowitz type II NOE fractures are comminuted, but the medial canthal tendon remains "
                "attached to a meaningful bony fragment. If that tendon-bearing fragment can be reduced "
                "and stabilized in the correct three-dimensional position, fixation can restore canthal "
                "position without deliberately converting the injury into a soft-tissue repair. Type III "
                "denotes avulsion of the medial canthal tendon from bone and requires canthal reattachment; "
                "severe type II comminution may also require canthopexy when the native fragment cannot be "
                "reliably stabilized. In either pattern, reconstruction must restore central facial width, "
                "nasal projection, and the medial orbital framework rather than treating the dorsum alone."
            ),
            "why_wrong": [
                "Correct. Type II is defined by comminution with the MCT still attached to a sizeable fragment; stable anatomic fixation of that fragment preserves the native tendon-bone relationship, with canthopexy added only when that relationship cannot be reliably restored.",
                "Type III requires MCT avulsion from its bony insertion. An intact tendon on a usable fragment is not type III, and intentionally detaching it discards a reconstructive advantage.",
                "The MCT is central to NOE classification and telecanthus. Dorsal reduction alone can leave persistent widened intercanthal distance and medial orbital malposition.",
                "An attached tendon does not make a displaced comminuted NOE complex stable. The central buttresses, intercanthal position, and nasal projection still require anatomic restoration when the fracture is operative.",
            ],
            "board_pearl": (
                "NOE classification follows the MCT-bearing central fragment: type I = single large fragment; "
                "type II = comminuted but tendon still attached to a usable fragment; type III = tendon avulsed "
                "from bone. Fix the stable tendon-bearing fragment when you can; reconstruct the tendon attachment when you cannot."
            ),
            "curveball": (
                "If the same CT showed the tendon completely avulsed from bone with severe central comminution, "
                "how would the fixation plan and need for transnasal canthopexy change?"
            ),
            "focus": "OR_prep",
            "ladder_reviewed": True,
            "_coverage_reviewed_v211": True,
            "_semantic_review_v298": True,
        })
        updated.append(q.get("id"))
    return {"updated": updated, "concept_id": target_cid}
