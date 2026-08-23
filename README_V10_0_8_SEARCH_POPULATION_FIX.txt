ENT Mastery v10.0.8 — Search Population Fix

The v10.0.7 search route no longer 500ed, but a malformed record in any downstream
search source could still abort _canonical_search_index() before it returned the
already-built curriculum rows. Because /search catches that exception, the result
appeared as a misleading empty search.

v10.0.8:
- isolates indexing errors at the record/source level;
- guarantees the Deep Curriculum is indexed first and retained;
- adds acronym/synonym search (SCC, OSA, SSNHL, BPPV, CRS, FESS, RLN, HNS, CI, TMJ, etc.);
- adds modest fuzzy matching for title variants/typos;
- changes the empty-state copy so it no longer claims a known topic is unpopulated.

Static verification confirms Laryngeal SCC exists in the current curriculum.
