"""Compatibility entrypoint for the v18.0 Concept Check depth repair.

Kept under the repository's *_depth_v*.py CI watch pattern so any future edits to
this depth-hardening layer automatically exercise the full coverage/quality suite.
"""

from concept_check_task_alignment_v180 import apply_concept_check_task_alignment_v180

__all__ = ["apply_concept_check_task_alignment_v180"]
