"""v51.0 Anatomy for each OR case: a focused surgical-anatomy review for every OR Tomorrow operation.

Content lives in ``anatomy_cases_v510/<batch>.py`` as ``CASES = {or_slug: {...}}``. Adds
``/anatomy/case/<slug>``, an "Anatomy by OR case" index at the top of the Anatomy Atlas, and a
"Review the anatomy" link on each OR Tomorrow card (via the ``anatomy_case_v510`` Jinja global).
"""
import importlib
import pkgutil

REQUIRED = ("title", "region", "summary", "layers", "landmarks", "danger")
REGION_ORDER = ["Otology / Neurotology", "Rhinology / Skull Base", "Head & Neck Oncology",
                "Thyroid / Parathyroid / Salivary", "Laryngology / Voice / Swallowing",
                "Pediatric Otolaryngology", "Facial Plastics / Trauma", "Sleep Surgery",
                "General ENT / Emergencies"]


def load_cases():
    import anatomy_cases_v510
    cases, rejected = {}, []
    for info in sorted(pkgutil.iter_modules(anatomy_cases_v510.__path__), key=lambda i: i.name):
        try:
            batch = getattr(importlib.import_module("anatomy_cases_v510." + info.name), "CASES", {})
        except Exception:
            rejected.append(info.name)
            continue
        for slug, c in batch.items():
            if isinstance(c, dict) and all(k in c for k in REQUIRED):
                cases[slug] = dict(c, slug=slug)
            else:
                rejected.append(slug)
    return cases, rejected


def install_anatomy_cases_v510(data, app_mod, app):
    from flask import render_template, abort
    cases, rejected = load_cases()
    registry = getattr(data, "OR_PREP_REGISTRY", {}) or {}
    atlas = {x.get("topic"): x for x in (getattr(app_mod, "ANATOMY_ATLAS_V97", None) or [])}
    by_atlas = {}
    for c in cases.values():
        for t in c.get("atlas_topics") or []:
            by_atlas.setdefault(t, []).append(c)

    def grouped():
        out = {}
        for c in sorted(cases.values(), key=lambda c: c["title"]):
            out.setdefault(c["region"], []).append(c)
        return [(r, out[r]) for r in REGION_ORDER if r in out] + \
               [(r, v) for r, v in out.items() if r not in REGION_ORDER]

    def anatomy_case(slug):
        c = cases.get(slug)
        if c is None:
            abort(404)
        maps = [atlas[t] for t in c.get("atlas_topics") or [] if t in atlas]
        return render_template("anatomy_case_v510.html", c=c, maps=maps, or_card=registry.get(slug),
                               region_cases=[x for x in grouped_dict().get(c["region"], []) if x["slug"] != slug])

    def grouped_dict():
        return dict(grouped())

    app.jinja_env.globals["anatomy_case_v510"] = cases.get
    app.jinja_env.globals["anatomy_case_groups_v510"] = grouped
    app.jinja_env.globals["anatomy_cases_for_map_v510"] = lambda topic: by_atlas.get(topic, [])
    if "anatomy_case_v510" not in app.view_functions:
        served = getattr(app, "_got_first_request", False)
        if served:
            app._got_first_request = False
        try:
            app.add_url_rule("/anatomy/case/<slug>", "anatomy_case_v510", anatomy_case)
        finally:
            if served:
                app._got_first_request = True
    else:
        app.view_functions["anatomy_case_v510"] = anatomy_case
    result = {"cases": len(cases), "rejected": rejected,
              "or_cards_without_anatomy": sorted(set(registry) - set(cases))[:200]}
    data.ANATOMY_CASES_V510 = result
    return result
