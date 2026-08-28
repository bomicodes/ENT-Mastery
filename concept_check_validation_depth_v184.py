"""CI routing sentinel for the fully integrated v18.4 Concept Check depth state.

This file intentionally matches the repository-wide ``*_depth_v*.py`` watch.
It does not mutate runtime content; the production cohort is applied by
concept_check_final_clinical_gate_v179 via concept_check_depth_v184.
"""

from concept_check_depth_v184 import apply_concept_check_task_alignment_v184

__all__ = ["apply_concept_check_task_alignment_v184"]
