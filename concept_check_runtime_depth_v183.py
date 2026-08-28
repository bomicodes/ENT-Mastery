"""v18.3 live Concept Check depth runtime.

This module deliberately matches the repository-wide ``*_depth_v*.py`` CI path
watch. It is the production application layer for the v18.3 cohort, so changes
to canonical resolution or runtime normalization cannot bypass the full audit.

The v17.8 contract permits canonical_topic to be absent when the production
resolver maps a Concept Check exactly to a live Deep Curriculum module and its
persisted concept_id agrees. The all-domain oral-board contract also requires
an explicit question mark, which is normalized without weakening that gate.
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

        # Preserve v17.8 review/source metadata and exact canonical linkage.
        # Replace only the deliberately reviewed pedagogic fields.
        q["prompt"] = str(payload["prompt"]).strip()
        if "?" not in q["prompt"]:
            q["prompt"] = q["prompt"].rstrip(".") + "?"
        for key in (
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
