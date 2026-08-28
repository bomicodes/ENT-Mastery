"""v18.3 runtime adapter: apply the selected cohort through live canonical resolution.

The v17.8 contract intentionally permits canonical_topic to be absent on a
Concept Check row when the production resolver can map it exactly to a live
Deep Curriculum module and the persisted concept_id agrees.  This adapter uses
that same resolver instead of turning an optional denormalized field into a new
source of truth.
"""

from concept_check_board_repair_v177 import _find_module
from concept_check_task_alignment_v183 import COHORT


def apply_concept_check_task_alignment_v183(checks, deep_modules, v6_item_id):
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    repaired = []
    missing = []
    link_mismatch = []

    for qid, payload in COHORT.items():
        q = by_id.get(qid)
        if q is None:
            missing.append(qid)
            continue

        module = _find_module(q, deep_modules, v6_item_id)
        domain = str(q.get("domain") or "")
        resolved_topic = str(module.get("topic") or "") if module else ""
        resolved_cid = v6_item_id(domain, resolved_topic) if module and domain else None
        if (
            not module
            or resolved_topic != payload["canonical_topic"]
            or resolved_cid != payload["concept_id"]
            or q.get("concept_id") != resolved_cid
        ):
            link_mismatch.append(qid)
            continue

        # Preserve v17.8 review/source metadata and canonical linkage. Replace
        # only the deliberately reviewed pedagogic fields.
        for key in (
            "prompt",
            "answer_text",
            "explanation",
            "board_pearl",
            "depth_layers_v183",
            "common_traps_v183",
            "deliberate_review_v183",
        ):
            q[key] = payload[key]
        q["task_alignment_v183"] = True
        q.pop("choices", None)
        q.pop("answer", None)
        q.pop("why_wrong", None)
        repaired.append(qid)

    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}


__all__ = ["apply_concept_check_task_alignment_v183"]
