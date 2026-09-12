"""Final clinical-stem normalization plus exact-live v20.30 successor alignment.

The validated v20.29 implementation remains the complete predecessor. v20.30 appends a
learner-facing ONB/esthesioneuroblastoma management pathway to the exact Sinonasal Malignancy
canonical after all prior cohorts, so fallback normalization cannot silently hide it.
"""
import concept_check_final_clinical_gate_v179_source_v228 as _base
from concept_check_final_clinical_gate_v179_source_v228 import *
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v229 import apply_concept_check_task_alignment_v229
from concept_check_depth_v230 import apply_concept_check_task_alignment_v230


def _reassert_onb_search_aliases_v230(checks, deep_modules, v6_item_id):
    """Keep all learner synonyms in the live canonical Deep Curriculum search text.

    The search index intentionally indexes learner-facing Deep Curriculum prose rather than hidden
    metadata. Therefore the historical alias ``esthesioblastoma`` is repeated in the recognize layer
    instead of being stored only in ``search_aliases``.
    """
    qid = "cc-v112-rec-rhinology-allergy-skull-base-sinonasal-malignancy"
    q = next((x for x in checks if str(x.get("id") or "") == qid), None)
    module = _find_module(q, deep_modules, v6_item_id) if q else None
    if not module:
        return False
    addition = (
        "ONB terminology: esthesioneuroblastoma and olfactory neuroblastoma are synonyms for the "
        "same olfactory-neuroepithelial malignancy; the historical alias esthesioblastoma may also "
        "appear in older literature and should resolve to this same canonical topic."
    )
    current = str(module.get("recognize") or "")
    if "esthesioblastoma" not in current.lower():
        module["recognize"] = (current.rstrip() + ("\n\n" if current.strip() else "") + addition).strip()
    return True


def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    results = _base.apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id)
    alignment_v229 = apply_concept_check_task_alignment_v229(checks, deep_modules, v6_item_id)
    results["task_alignment_v229"] = alignment_v229
    results["post_alignment_reframed_v229"] = _base._reassert_clinical_contract(
        checks,
        alignment_v229.get("repaired", []),
        results.get("unresolved", []),
        "post_alignment_clinical_frame_v229",
    )
    alignment_v230 = apply_concept_check_task_alignment_v230(checks, deep_modules, v6_item_id)
    results["task_alignment_v230"] = alignment_v230
    results["post_alignment_reframed_v230"] = _base._reassert_clinical_contract(
        checks,
        alignment_v230.get("repaired", []),
        results.get("unresolved", []),
        "post_alignment_clinical_frame_v230",
    )
    results["onb_search_aliases_v230"] = _reassert_onb_search_aliases_v230(checks, deep_modules, v6_item_id)
    return results
