"""v20.19 — exact-live Cranial Nerve Examination / Skull Base Localization depth cohort.

The clinical payload was previously validated on the superseded v20.18 branch. This
wrapper intentionally re-homes that content as v20.19 so the live v20.18 Sinonasal
Malignancy cohort remains immutable.
"""
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v219_payload import QIDS, CID, TOPIC, ANSWER, SOURCE_REFS_V218, COHORT as _OLD

SOURCE_REFS_V219 = SOURCE_REFS_V218

def _promote(p):
    q = dict(p)
    for old, new in (
        ("depth_layers_v218", "depth_layers_v219"),
        ("common_traps_v218", "common_traps_v219"),
        ("deliberate_review_v218", "deliberate_review_v219"),
        ("source_refs_v218", "source_refs_v219"),
        ("evidence_distinction_v218", "evidence_distinction_v219"),
        ("audit_profile_v218", "audit_profile_v219"),
    ):
        q[new] = q.pop(old)
    q["deliberate_review_v219"] = q["deliberate_review_v219"].replace("v20.17 production backlog", "validated pre-collision backlog")
    return q

COHORT = {qid: _promote(p) for qid, p in _OLD.items()}

def apply_concept_check_task_alignment_v219(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    fields = (
        "prompt", "answer_text", "explanation", "board_pearl",
        "depth_layers_v219", "common_traps_v219", "deliberate_review_v219",
        "source_refs_v219", "evidence_distinction_v219", "audit_profile_v219",
    )
    for qid, p in COHORT.items():
        q = by.get(qid)
        if q is None:
            missing.append(qid); continue
        m = _find_module(q, deep_modules, v6_item_id)
        topic = str(m.get("topic") or "") if m else ""
        cid = v6_item_id(q.get("domain"), topic) if m and q.get("domain") else None
        persisted_cid = q.get("concept_id")
        if m is None or topic != p["canonical_topic"] or cid != p["concept_id"] or (persisted_cid is not None and persisted_cid != cid):
            link_mismatch.append(qid); continue
        q["concept_id"] = cid
        q["canonical_topic"] = topic
        for field in fields:
            q[field] = p[field]
        q["choices"] = []
        q["answer"] = None
        q["task_alignment_v219"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
