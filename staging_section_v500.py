"""v50.0 Head & Neck Staging: TNM tables, memory hooks, stage-based treatment algorithms and
"stage this case" drills for each head and neck cancer site.

Site content lives in ``staging_v500/<site>.py`` as one ``SITE`` dict per file. Routes:
``/staging`` (index grouped by region) and ``/staging/<slug>`` (one site).
"""
import importlib
import pkgutil

GROUP_ORDER = ["Mucosal sites", "Larynx & hypopharynx", "Sinonasal & skull base", "Neck",
               "Salivary & thyroid", "Skin"]
REQUIRED = ("slug", "name", "group", "ajcc", "t", "n_clinical", "m", "stage_groups", "algorithm")


def load_sites():
    import staging_v500
    sites, rejected = [], []
    for info in sorted(pkgutil.iter_modules(staging_v500.__path__), key=lambda i: i.name):
        try:
            site = getattr(importlib.import_module("staging_v500." + info.name), "SITE", None)
        except Exception:  # a broken data file must never take the site down
            rejected.append(info.name)
            continue
        if not isinstance(site, dict) or not all(k in site for k in REQUIRED):
            rejected.append(info.name)
            continue
        site = dict(site)
        site["drills"] = [d for d in site.get("drills", [])
                          if isinstance(d.get("choices"), list) and len(d["choices"]) >= 2
                          and isinstance(d.get("answer"), int) and 0 <= d["answer"] < len(d["choices"])]
        sites.append(site)
    sites.sort(key=lambda s: (GROUP_ORDER.index(s["group"]) if s["group"] in GROUP_ORDER else 99,
                              s.get("order", 50), s["name"]))
    return sites, rejected


def install_staging_v500(data, app):
    from flask import render_template, abort
    sites, rejected = load_sites()
    by_slug = {s["slug"]: s for s in sites}

    def grouped():
        out = []
        for s in sites:
            if not out or out[-1][0] != s["group"]:
                out.append((s["group"], []))
            out[-1][1].append(s)
        return out

    def staging_index():
        drills = sum(len(s["drills"]) for s in sites)
        return render_template("staging_index.html", groups=grouped(), site_count=len(sites), drill_count=drills)

    def staging_site(slug):
        site = by_slug.get(slug)
        if site is None:
            abort(404)
        i = sites.index(site)
        return render_template("staging_site.html", s=site, groups=grouped(),
                               prev_site=sites[i - 1] if i > 0 else None,
                               next_site=sites[i + 1] if i + 1 < len(sites) else None)

    if "staging_index_v500" not in app.view_functions:
        # Audits import this entrypoint after another module has already served a test request;
        # Flask then refuses new rules. Production installs at import time, before any request.
        served = getattr(app, "_got_first_request", False)
        if served:
            app._got_first_request = False
        try:
            app.add_url_rule("/staging", "staging_index_v500", staging_index)
            app.add_url_rule("/staging/<slug>", "staging_site_v500", staging_site)
        finally:
            if served:
                app._got_first_request = True
    else:
        app.view_functions["staging_index_v500"] = staging_index
        app.view_functions["staging_site_v500"] = staging_site
    result = {"sites": len(sites), "rejected": rejected, "drills": sum(len(s["drills"]) for s in sites)}
    data.STAGING_V500 = result
    return result
