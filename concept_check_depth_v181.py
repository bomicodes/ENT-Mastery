"""Compatibility entrypoint for the v18.1 Concept Check depth repair.

Kept under the repository's *_depth_v*.py CI watch pattern so this second
artifact-confirmed depth cohort also exercises the complete repository coverage
and quality suite in addition to its dedicated task-specific hard gate.
"""

from concept_check_task_alignment_v181 import apply_concept_check_task_alignment_v181

__all__ = ["apply_concept_check_task_alignment_v181"]
