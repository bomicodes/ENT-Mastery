"""Final clinical-stem normalization plus exact-live v20.28 successor alignment.

The validated v20.27 implementation is preserved in the adjacent source module. This
thin successor wrapper appends v20.28 after that complete ordered pipeline so no
predecessor cohort or clinical-frame behavior is reconstructed or weakened.
"""
import concept_check_final_clinical_gate_v179_source_v227 as _base
from concept_check_final_clinical_gate_v179_source_v227 import *
from concept_check_depth_v228 import apply_concept_check_task_alignment_v228

# Explicit private-helper export for successor wrappers.
_reassert_clinical_contract = _base._reassert_clinical_contract


def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    results = _base.apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id)
    alignment_v228 = apply_concept_check_task_alignment_v228(checks, deep_modules, v6_item_id)
    results["task_alignment_v228"] = alignment_v228
    results["post_alignment_reframed_v228"] = _reassert_clinical_contract(
        checks,
        alignment_v228.get("repaired", []),
        results.get("unresolved", []),
        "post_alignment_clinical_frame_v228",
    )
    return results
