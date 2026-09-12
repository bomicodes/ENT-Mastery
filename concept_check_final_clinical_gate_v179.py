"""Final clinical-stem normalization plus exact-live v20.30 successor alignment.

The validated v20.29 implementation remains the complete predecessor. v20.30 appends a
learner-facing ONB/esthesioneuroblastoma management pathway to the exact Sinonasal Malignancy
canonical after all prior cohorts, so fallback normalization cannot silently hide it.
"""
import concept_check_final_clinical_gate_v179_source_v228 as _base
from concept_check_final_clinical_gate_v179_source_v228 import *
from concept_check_depth_v229 import apply_concept_check_task_alignment_v229
from concept_check_depth_v230 import apply_concept_check_task_alignment_v230


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
    return results
