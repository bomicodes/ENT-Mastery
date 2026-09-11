"""v20.26 exact-live ENT Fluids / Electrolytes / Nutrition depth cohort.

Rehomes the previously source-grounded clinical teaching onto the validated v20.25
production lineage without merging the stale audit branch. Textbook identities were
reconfirmed in connected Google Drive on 2026-09-11; current guidance remains separated
from durable textbook physiology.
"""
from copy import deepcopy
from concept_check_board_repair_v177 import _find_module
import concept_check_fluids_source_v223 as _src

QIDS = _src.QIDS
CID = _src.CID
TOPIC = _src.TOPIC
PROMPT = _src.PROMPT
ANSWER = _src.ANSWER
TRAPS = list(_src.TRAPS)

SOURCE_REFS_V226 = deepcopy(_src.SOURCE_REFS_V223)
for _ref in SOURCE_REFS_V226:
    if isinstance(_ref, dict) and _ref.get("type") == "textbook":
        _ref["citation"] = str(_ref.get("citation") or "") + " Source identity reconfirmed in connected Google Drive on 2026-09-11."

_base = deepcopy(_src.COHORT[QIDS[0]])
_base.pop("depth_layers_v223", None)
_base.pop("common_traps_v223", None)
_base.pop("deliberate_review_v223", None)
_base.pop("source_refs_v223", None)
_base.pop("evidence_distinction_v223", None)
_base.pop("task_alignment_v223", None)
_base["depth_layers_v226"] = {
    "foundation": "Fluid compartments; resuscitation versus maintenance versus replacement; volume assessment; sodium, potassium, magnesium and phosphate physiology; and oral/enteral/parenteral nutrition hierarchy.",
    "application": "Adult and pediatric maintenance prescriptions, postoperative hyponatremia reasoning, safe electrolyte correction, quantified-loss replacement, head-and-neck cancer nutrition and refeeding prevention.",
    "senior_decision": "Recognize shock, symptomatic sodium emergencies, dangerous potassium derangements, refeeding physiology, airway or hemorrhage problems masquerading as fluid issues, and know when to stop formula-based treatment and escalate.",
}
_base["common_traps_v226"] = TRAPS
_base["deliberate_review_v226"] = {
    "priority": "high",
    "review_after_days": [2, 7, 21, 60],
    "reason": "high-frequency inpatient/OR management with low-frequency but catastrophic sodium, potassium, refeeding and airway-adjacent failure modes",
}
_base["source_refs_v226"] = SOURCE_REFS_V226
_base["evidence_distinction_v226"] = (
    "Durable textbook physiology (volume status, compartment reasoning, classic maintenance calculations and enteral-first principles) is retained. "
    "Current guidance supersedes older reflexive hypotonic pediatric maintenance practice: AAP recommends isotonic maintenance fluid for most postoperative children within scope. "
    "Adult NICE quantities are initial routine-maintenance frameworks, not resuscitation targets. ASPEN refeeding criteria and ESPEN cancer-nutrition guidance update monitoring and feeding decisions. "
    "Cummings source identity is traceable in the connected Drive corpus, but whole-volume extraction is size-limited; no unsupported Cummings-specific numeric prescription is asserted."
)
_base["task_alignment_v226"] = True
COHORT = {QIDS[0]: _base}


def apply_concept_check_task_alignment_v226(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, patch in COHORT.items():
        q = by.get(qid)
        if q is None:
            missing.append(qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != patch["canonical_topic"] or cid != patch["concept_id"]:
            link_mismatch.append(qid)
            continue
        for key, val in patch.items():
            if key != "canonical_topic":
                q[key] = val
        q["choices"] = []
        q["answer"] = None
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
