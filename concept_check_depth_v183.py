"""v18.3 Concept Check depth layer entrypoint.

The cohort is selected by the live-canonical backlog audit and applied through
the v17.8 production canonical resolver. This stable depth filename keeps every
v18.3 change under the repository-wide ``*_depth_v*.py`` CI watch.
"""

from concept_check_task_alignment_v183_runtime import apply_concept_check_task_alignment_v183

__all__ = ["apply_concept_check_task_alignment_v183"]
