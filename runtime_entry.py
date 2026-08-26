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
LEARNING_LADDERS_V169 = apply_learning_ladders_v169(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

# v17.0: second Otology ladder batch.
from vignette_ladders_v170 import apply_learning_ladders_v170
LEARNING_LADDERS_V170 = apply_learning_ladders_v170(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

# v17.1: third Otology ladder batch.
from vignette_ladders_v171 import apply_learning_ladders_v171
LEARNING_LADDERS_V171 = apply_learning_ladders_v171(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

# v17.2: fourth Otology ladder batch.
from vignette_ladders_v172 import apply_learning_ladders_v172
LEARNING_LADDERS_V172 = apply_learning_ladders_v172(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

# v17.3: fifth Otology ladder batch.
from vignette_ladders_v173 import apply_learning_ladders_v173
LEARNING_LADDERS_V173 = apply_learning_ladders_v173(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

# v17.4: sixth Otology ladder batch.
from vignette_ladders_v174 import apply_learning_ladders_v174
LEARNING_LADDERS_V174 = apply_learning_ladders_v174(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

# v17.5: seventh Otology ladder batch.
from vignette_ladders_v175 import apply_learning_ladders_v175
LEARNING_LADDERS_V175 = apply_learning_ladders_v175(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

# v17.6: finish the remaining v13.6 Otology foundations.
from vignette_ladders_v176 import apply_learning_ladders_v176
LEARNING_LADDERS_V176 = apply_learning_ladders_v176(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

data.CLINICAL_CHALLENGE_BY_ID_V119 = {
    q["id"]: q for q in data.CLINICAL_CHALLENGES_V119 if q.get("id")
}
app_mod.CLINICAL_CHALLENGES_V119 = data.CLINICAL_CHALLENGES_V119
app_mod.CLINICAL_CHALLENGE_BY_ID_V119 = data.CLINICAL_CHALLENGE_BY_ID_V119

# v17.8: restore clinically distinct disease entities that historical
# canonicalization may have collapsed into comparison nodes.
from deep_curriculum_distinct_entities_v178 import apply_distinct_entities_v178

DISTINCT_ENTITIES_V178 = apply_distinct_entities_v178(data)

# v16.2: repair the full Concept Check bank after all Deep Curriculum runtime
# enrichments have loaded, so repaired recall answers come from the final live
# canonical curriculum rather than stale source text.
from concept_check_repair_v162 import apply_concept_check_repair_v162

CONCEPT_CHECK_REPAIR_V162 = apply_concept_check_repair_v162(
    data.CONCEPT_CHECKS_V112,
    data.DEEP_MODULES_V6,
    data._v6_item_id,
)

# v17.7: replace generic framework-retrieval prompts with clinical board-style
# questions. Existing credible clinical MCQs are preserved, while nonclinical
# prompts become patient vignettes with an explicit canonical reveal answer.
from concept_check_board_repair_v177 import apply_concept_check_board_repair_v177

CONCEPT_CHECK_BOARD_REPAIR_V177 = apply_concept_check_board_repair_v177(
    data.CONCEPT_CHECKS_V112,
    data.DEEP_MODULES_V6,
    data._v6_item_id,
)

# v17.8: second-pass curation across every ENT domain. All live Concept Checks
# are reviewed against a domain-specific clinical standard. Structurally weak
# MCQs are converted to focused oral-board vignettes rather than retaining
# mismatched distractor levels.
from concept_check_domain_curation_v178 import apply_concept_check_domain_curation_v178

CONCEPT_CHECK_DOMAIN_CURATION_V178 = apply_concept_check_domain_curation_v178(
    data.CONCEPT_CHECKS_V112,
    data.DEEP_MODULES_V6,
    data._v6_item_id,
)

# v17.9: use word-boundary clinical markers to catch any false-positive that
# slipped through v17.8's heuristic (for example "ct " embedded in "tract").
from concept_check_final_clinical_gate_v179 import apply_final_clinical_gate_v179

CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179 = apply_final_clinical_gate_v179(
    data.CONCEPT_CHECKS_V112,
    data.DEEP_MODULES_V6,
    data._v6_item_id,
)

_rebuilt_concept_checks_v179 = {
    q["id"]: q for q in data.CONCEPT_CHECKS_V112 if q.get("id")
}
if isinstance(getattr(data, "CONCEPT_CHECK_BY_ID_V112", None), dict):
    data.CONCEPT_CHECK_BY_ID_V112.clear()
    data.CONCEPT_CHECK_BY_ID_V112.update(_rebuilt_concept_checks_v179)
else:
    data.CONCEPT_CHECK_BY_ID_V112 = _rebuilt_concept_checks_v179

if isinstance(getattr(app_mod, "CONCEPT_CHECK_BY_ID_V112", None), dict):
    app_mod.CONCEPT_CHECK_BY_ID_V112.clear()
    app_mod.CONCEPT_CHECK_BY_ID_V112.update(_rebuilt_concept_checks_v179)
else:
    app_mod.CONCEPT_CHECK_BY_ID_V112 = data.CONCEPT_CHECK_BY_ID_V112

_original_search_index = app_mod._canonical_search_index


def _canonical_search_index_v150():
    rows = list(_original_search_index())
    seen = {(r.get("type"), r.get("url")) for r in rows}
    bank_rows = [
        {"type": "Practice bank", "title": "Clinical Challenges", "subtitle": f"{len(data.CLINICAL_CHALLENGES_V119)} board-style vignettes", "url": "/clinical-challenges", "text": "clinical challenges board vignettes overnight call OR prep postoperative call clinical reasoning"},
        {"type": "Practice bank", "title": "Concept Checks", "subtitle": f"{len(data.CONCEPT_CHECKS_V112)} board-recall questions", "url": "/concept-checks", "text": "concept checks board recall questions clinical vignettes active recall knowledge checks boards"},
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
