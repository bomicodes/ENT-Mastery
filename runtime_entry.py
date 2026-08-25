"""Production entrypoint for lightweight runtime integrations.

Keeps generated app.py stable while making high-value practice banks discoverable
through global search. wsgi performs all curriculum/vignette merges first.
"""

import wsgi

app = wsgi.app
data = wsgi.data
app_mod = wsgi._app_module

_original_search_index = app_mod._canonical_search_index


def _canonical_search_index_v150():
    rows = list(_original_search_index())
    seen = {(r.get("type"), r.get("url")) for r in rows}

    bank_rows = [
        {
            "type": "Practice bank",
            "title": "Clinical Challenges",
            "subtitle": f"{len(data.CLINICAL_CHALLENGES_V119)} board-style vignettes",
            "url": "/clinical-challenges",
            "text": "clinical challenges board vignettes overnight call OR prep postoperative call clinical reasoning",
        },
        {
            "type": "Practice bank",
            "title": "Concept Checks",
            "subtitle": f"{len(data.CONCEPT_CHECKS_V112)} recall questions",
            "url": "/concept-checks",
            "text": "concept checks recall questions active recall knowledge checks boards",
        },
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
        rows.append({
            "type": "Concept Check",
            "title": str(q.get("topic") or "Concept Check"),
            "subtitle": str(q.get("domain") or "ENT"),
            "url": url,
            "text": str(prompt) + " " + " ".join(str(x) for x in choices),
        })
        seen.add(key)
    return rows


app_mod._canonical_search_index = _canonical_search_index_v150

# Temporary v15.9 audit emission: lets the content audit inspect the real
# post-merge production curriculum. Removed after the audit log is captured.
try:
    import audit_deep_curriculum_v159
    print("V159_RUNTIME_AUDIT_BEGIN")
    audit_deep_curriculum_v159.main()
    print("V159_RUNTIME_AUDIT_END")
except Exception as _audit_exc:
    print(f"V159_RUNTIME_AUDIT_ERROR|{type(_audit_exc).__name__}|{_audit_exc}")
