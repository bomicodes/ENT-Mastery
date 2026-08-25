"""Production entrypoint for lightweight runtime integrations.

Keeps generated app.py stable while making high-value practice banks discoverable
through global search. wsgi performs all curriculum/vignette merges first.
"""

import wsgi

app = wsgi.app
data = wsgi.data
app_mod = wsgi._app_module

# v16.9: deliberate learning-ladder curation begins with five Otology concepts.
from vignette_ladders_v169 import apply_learning_ladders_v169

LEARNING_LADDERS_V169 = apply_learning_ladders_v169(
    data.CLINICAL_CHALLENGES_V119,
    data._v6_item_id,
)

# v17.0: continue the deliberate Otology pass with the next five concepts.
# Run after v16.9 and before the final reliability snapshot.
from vignette_ladders_v170 import apply_learning_ladders_v170

LEARNING_LADDERS_V170 = apply_learning_ladders_v170(
    data.CLINICAL_CHALLENGES_V119,
    data._v6_item_id,
)
data.CLINICAL_CHALLENGE_BY_ID_V119 = {
    q["id"]: q for q in data.CLINICAL_CHALLENGES_V119 if q.get("id")
}
app_mod.CLINICAL_CHALLENGES_V119 = data.CLINICAL_CHALLENGES_V119
app_mod.CLINICAL_CHALLENGE_BY_ID_V119 = data.CLINICAL_CHALLENGE_BY_ID_V119

# v16.2: repair the full Concept Check bank after all Deep Curriculum runtime
# enrichments have loaded, so repaired recall answers come from the final live
# canonical curriculum rather than stale source text.
from concept_check_repair_v162 import apply_concept_check_repair_v162

CONCEPT_CHECK_REPAIR_V162 = apply_concept_check_repair_v162(
    data.CONCEPT_CHECKS_V112,
    data.DEEP_MODULES_V6,
    data._v6_item_id,
)

_rebuilt_concept_checks_v162 = {
    q["id"]: q for q in data.CONCEPT_CHECKS_V112 if q.get("id")
}
if isinstance(getattr(data, "CONCEPT_CHECK_BY_ID_V112", None), dict):
    data.CONCEPT_CHECK_BY_ID_V112.clear()
    data.CONCEPT_CHECK_BY_ID_V112.update(_rebuilt_concept_checks_v162)
else:
    data.CONCEPT_CHECK_BY_ID_V112 = _rebuilt_concept_checks_v162

if isinstance(getattr(app_mod, "CONCEPT_CHECK_BY_ID_V112", None), dict):
    app_mod.CONCEPT_CHECK_BY_ID_V112.clear()
    app_mod.CONCEPT_CHECK_BY_ID_V112.update(_rebuilt_concept_checks_v162)
else:
    app_mod.CONCEPT_CHECK_BY_ID_V112 = data.CONCEPT_CHECK_BY_ID_V112

_original_search_index = app_mod._canonical_search_index


def _canonical_search_index_v150():
    rows = list(_original_search_index())
    seen = {(r.get("type"), r.get("url")) for r in rows}
    bank_rows = [
        {"type": "Practice bank", "title": "Clinical Challenges", "subtitle": f"{len(data.CLINICAL_CHALLENGES_V119)} board-style vignettes", "url": "/clinical-challenges", "text": "clinical challenges board vignettes overnight call OR prep postoperative call clinical reasoning"},
        {"type": "Practice bank", "title": "Concept Checks", "subtitle": f"{len(data.CONCEPT_CHECKS_V112)} recall questions", "url": "/concept-checks", "text": "concept checks recall questions active recall knowledge checks boards"},
    ]
    for row in bank_rows:
        key = (row["type"], row["url"])
        if key not in seen:
            rows.append(row)
            seen.add(key)
    for q in data.CONCEPT_CHECKS_V112:
        qid = str(q.get("id", ""))
        if not qid:
            continue
        url = "/concept-check/" + qid
        key = ("Concept Check", url)
        if key in seen:
            continue
        choices = q.get("choices") or []
        prompt = q.get("question") or q.get("prompt") or q.get("stem") or ""
        rows.append({"type": "Concept Check", "title": str(q.get("topic") or "Concept Check"), "subtitle": str(q.get("domain") or "ENT"), "url": url, "text": str(prompt) + " " + " ".join(str(x) for x in choices)})
        seen.add(key)
    return rows


app_mod._canonical_search_index = _canonical_search_index_v150

# v16.8: final reliability pass after all curriculum and practice-bank mutation is complete.
from reliability_v168 import apply_reliability_v168

RELIABILITY_V168 = apply_reliability_v168(app, data, app_mod)
