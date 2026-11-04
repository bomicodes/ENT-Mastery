"""v69.0: one OR Tomorrow card per operation.

"DLB" (Direct Laryngoscopy / Bronchoscopy) duplicated "direct-laryngoscopy-bronchoscopy"
(Direct Laryngoscopy & Bronchoscopy / Airway Evaluation): same setup, post-op and
complications text, two entries in the OR list and in search. The DLB card's unique attending
questions are folded into the kept card, the duplicate is removed from the live registry, and
old links or searches for it open the kept card.
"""
import re

ALIASES_V690 = {"DLB": "direct-laryngoscopy-bronchoscopy"}


def _norm(s):
    return " ".join(re.findall(r"[a-z0-9]+", str(s or "").lower()))


def install_or_dedupe_v690(app, data, app_mod):
    from flask import request, redirect, url_for
    registry = data.OR_PREP_REGISTRY
    removed, alias_queries = [], {}
    for dup, keep in ALIASES_V690.items():
        a, b = registry.get(keep), registry.get(dup)
        if not a or not b:
            continue
        seen = {_norm(q) for q, _ in (a.get("attending_followup") or [])}
        merged = [list(p) for p in (a.get("attending_followup") or [])]
        for q, ans in (b.get("attending_followup") or []):
            if _norm(q) not in seen:
                merged.append([q, ans]); seen.add(_norm(q))
        a["attending_followup"] = merged
        for k, v in b.items():
            if k.endswith("_v2317") and k not in a:
                a[k] = v
        alias_queries[_norm(dup)] = a.get("title") or keep
        alias_queries[_norm(b.get("title"))] = a.get("title") or keep
        registry.pop(dup, None)
        removed.append(dup)
    if getattr(app_mod, "OR_PREP_REGISTRY", None) is not registry:
        getattr(app_mod, "OR_PREP_REGISTRY", {}).pop("DLB", None)

    view = app.view_functions.get("case_tomorrow")
    if view and alias_queries and not getattr(view, "_dedupe_v690", False):
        def case_tomorrow_v690(*a, **kw):
            q = _norm(request.args.get("q"))
            if q in alias_queries:
                return redirect(url_for("case_tomorrow", q=alias_queries[q]))
            return view(*a, **kw)
        case_tomorrow_v690._dedupe_v690 = True
        app.view_functions["case_tomorrow"] = case_tomorrow_v690
    return {"removed": removed}
