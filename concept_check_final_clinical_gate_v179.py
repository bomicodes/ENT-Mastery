"""Final clinical-stem normalization plus exact-live v20.29 successor alignment.

The validated v20.28 implementation is preserved in the adjacent source module. This
thin successor wrapper appends v20.29 after that complete ordered pipeline so no
predecessor cohort or clinical-frame behavior is reconstructed or weakened.
"""
import concept_check_final_clinical_gate_v179_source_v228 as _base
from concept_check_final_clinical_gate_v179_source_v228 import *
from concept_check_depth_v229 import apply_concept_check_task_alignment_v229


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
    return results
