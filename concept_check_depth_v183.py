"""v18.3 Concept Check depth-selection entrypoint.

The post-completion curriculum has no incomplete canonical ladder domain.  This
stable depth filename keeps the deterministic live-canonical backlog audit under
the repository-wide ``*_depth_v*.py`` CI watch without mutating content.
"""

from audit_concept_check_depth_backlog_v183 import main

__all__ = ["main"]
