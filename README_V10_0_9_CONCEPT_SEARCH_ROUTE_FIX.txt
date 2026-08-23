ENT Mastery v10.0.9 — Concept Search / Route Fix

Root cause:
`from data import *` does not import names beginning with an underscore. The search
index and Concept Hub were both calling `_v6_item_id`, so every curriculum concept
row was silently skipped by the search index and concept-ID routing could fail.

Also, the v10.0.8 search edit accidentally removed the OR Tomorrow helper functions
`_norm_or_text`, `_or_rank`, and `_related_or_gaps`.

Fixes:
- explicitly imports `_v6_item_id` from data;
- restores/preserves OR Tomorrow helper functions;
- indexes the 309 Deep Curriculum concepts correctly;
- strongly prioritizes exact curriculum-concept matches;
- adds AOE and SCC synonym handling;
- keeps record-level fault isolation for optional search surfaces.

Static verification confirms both Acute Otitis Externa and Laryngeal SCC have stable
concept IDs in the current curriculum.
