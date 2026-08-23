ENT Mastery v10.0.7 — Search / Concept Hub Hotfix

Root cause from Render traceback:
NameError: _canonical_search_index is not defined

Fixes:
- Restores a modern canonical search index built only from the integrated curriculum,
  cases, interpretation labs, OR Tomorrow, and current evidence catalog.
- Curriculum search results now link to stable concept-ID routes.
- Makes /search fail-safe rather than returning 500 if one source record is malformed.
- Makes Concept Hub template dictionary access tolerant of missing optional fields.

This patch is intended to be applied on top of v10.0.6.
