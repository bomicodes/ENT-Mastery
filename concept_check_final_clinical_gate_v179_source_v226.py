"""Validated v20.26 final clinical-stem normalization and ordered Concept Check depth hardening."""
import concept_check_final_clinical_gate_v179_source_v225 as _base
from concept_check_final_clinical_gate_v179_source_v225 import *
from concept_check_depth_v226 import apply_concept_check_task_alignment_v226


def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    results = _base.apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id)
    alignment_v226 = apply_concept_check_task_alignment_v226(checks, deep_modules, v6_item_id)
    results["task_alignment_v226"] = alignment_v226
    results["post_alignment_reframed_v226"] = _base._reassert_clinical_contract(
        checks,
        alignment_v226.get("repaired", []),
        results.get("unresolved", []),
        "post_alignment_clinical_frame_v226",
    )
    return results
