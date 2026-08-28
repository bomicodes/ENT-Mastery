"""v18.3 Concept Check depth layer entrypoint.

The cohort is selected by the live-canonical backlog audit and implemented in a
separate task-alignment layer. This stable depth filename keeps every v18.3
change under the repository-wide ``*_depth_v*.py`` CI watch.
"""

from concept_check_task_alignment_v183 import apply_concept_check_task_alignment_v183

__all__ = ["apply_concept_check_task_alignment_v183"]
