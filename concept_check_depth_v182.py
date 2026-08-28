"""v18.2 Concept Check depth layer entrypoint.

This stable depth-module name keeps the post-completion Concept Check repair under
the repository-wide ``*_depth_v*.py`` CI watch while the implementation remains
focused in ``concept_check_task_alignment_v182.py``.
"""

from concept_check_task_alignment_v182 import apply_concept_check_task_alignment_v182

__all__ = ["apply_concept_check_task_alignment_v182"]
