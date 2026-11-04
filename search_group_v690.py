"""v69.0: search shows each topic's practice questions once.

Search used to list every matching question as its own row, so a query like "septoplasty"
showed "Septal Deviation" twelve times. Question rows (Clinical Challenge, Concept Check) are now
grouped by topic into one row that links to that topic's practice set, placed where the topic's
best-scoring question ranked. Pages (OR cards, topics, cases, atlas, Pasha) are unchanged.
"""
from urllib.parse import quote

GROUPED = {"Clinical Challenge": "/clinical-challenges?topic=", "Concept Check": "/concept-checks?topic="}


def install_search_group_v690(app, app_mod):
    from flask import request, render_template

    def search_v690():
        q = request.args.get("q", "").strip().lower()
        rows = []
        try:
            index = app_mod._canonical_search_index()
            if q:
                scored = []
                for r in index:
                    s = app_mod._search_score_v1009(r, q)
                    if s > 0:
                        scored.append((s, r))
                scored.sort(key=lambda x: (-x[0], 0 if x[1].get("type") == "Curriculum concept" else 1, str(x[1].get("title", ""))))
                groups, out = {}, []
                for s, r in scored:
                    typ = r.get("type")
                    if typ in GROUPED:
                        key = (typ, r.get("title"))
                        if key in groups:
                            groups[key]["n"] += 1
                            continue
                        g = {"row": dict(r), "n": 1, "first_url": r.get("url")}
                        groups[key] = g
                        out.append(g)
                    else:
                        out.append({"row": r, "n": None})
                for g in out:
                    if g["n"] is None:
                        rows.append(g["row"])
                        continue
                    row = g["row"]
                    domain = str(row.get("subtitle") or "").split(" · ")[0]
                    if g["n"] > 1:
                        row["url"] = GROUPED[row["type"]] + quote(str(row.get("title") or ""))
                        label = "practice questions" if row["type"] == "Clinical Challenge" else "concept checks"
                        row["subtitle"] = f"{domain} · {g['n']} {label}"
                        row["type"] = "Practice questions" if row["type"] == "Clinical Challenge" else "Concept checks"
                    rows.append(row)
                    if len(rows) >= 80:
                        break
                rows = rows[:80]
        except Exception:
            app.logger.exception("Search failed")
            rows = []
        return render_template("search.html", q=q, results=rows)

    if "search" in app.view_functions:
        app.view_functions["search"] = search_v690
    return {"grouped_types": sorted(GROUPED)}
