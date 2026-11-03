"""v61.0: one page per operation.

Some curriculum topics *are* an operation (Sphenoidotomy, Neck Dissection, Medialization
Thyroplasty...) and duplicated the matching OR Tomorrow card with similar-but-different text.
Residents look for operative material in OR Tomorrow, so for each pair below:

* the OR card shows the curriculum topic's teaching inline (background anatomy and disease,
  then decisions/workup/teaching), plus that topic's practice questions, Daily Path and mastery;
* the curriculum topic page redirects to the OR card;
* search lists the operation once (the OR card).

The curriculum topic itself stays canonical: its questions, concept checks, flashcards, mastery
and Daily Path scheduling keep the same concept_id. Only where it is *read* changes.
Disease topics (Otosclerosis, Peritonsillar Abscess...) stay in the curriculum and keep their
links to OR cards.
"""
import re
from urllib.parse import quote

R, H, T, P, L, F, S, G, O = ("Rhinology / Allergy / Skull Base", "Head & Neck Oncology", "Thyroid / Parathyroid / Salivary",
                             "Pediatric Otolaryngology", "Laryngology / Voice / Swallowing", "Facial Plastics / Trauma",
                             "Sleep Surgery", "General ENT / Emergencies", "Otology / Neurotology")

MERGE_V610 = {
    (R, "Ethmoidectomy"): "endoscopic-sinus-surgery",
    (R, "Endoscopic Maxillary Antrostomy"): "maxillary-antrostomy",
    (R, "Sphenoidotomy"): "sphenoidotomy",
    (R, "Frontal Sinusotomy / Draf Procedures"): "draf",
    (R, "Epistaxis Surgical Control"): "spa-ligation",
    (R, "Endoscopic CSF Leak Repair / Nasoseptal Flap"): "csf-nasoseptal",
    (O, "Cochlear Implant Surgery"): "cochlear-implant",
    (H, "Neck Dissection"): "neck-dissection",
    (H, "Total Laryngectomy"): "total-laryngectomy",
    (H, "Free-Flap Monitoring / Compromise / Salvage"): "free-flap-takeback",
    (H, "Open Partial / Conservation Laryngectomy"): "conservation-laryngectomy",
    (H, "Transoral Laser Microsurgery for Laryngeal Cancer"): "transoral-laser-laryngeal-cancer",
    (T, "Central Neck Dissection"): "central-neck",
    (T, "Reoperative Thyroid Surgery"): "reop-thyroid",
    (T, "Sialendoscopy"): "sialendoscopy",
    (P, "Laryngotracheal Reconstruction"): "peds-ltr",
    (P, "Microtia Reconstruction"): "microtia-reconstruction",
    (L, "Medialization Thyroplasty"): "medialization",
    (L, "Injection Laryngoplasty"): "injection-laryngoplasty",
    (L, "Posterior Cordotomy / Arytenoidectomy"): "cordotomy",
    (L, "Microlaryngoscopy"): "microflap",
    (F, "Otoplasty"): "otoplasty",
    (F, "Bilobed Flap"): "bilobed-flap",
    (F, "Cervicofacial Flap"): "cervicofacial-flap",
    (F, "Forehead Flap / Nasal Reconstruction"): "forehead-flap",
    (F, "Functional Septorhinoplasty"): "septorhino",
    (S, "Hypoglossal Nerve Stimulation"): "hypoglossal-stimulator",
    (S, "Palatal Surgery"): "reconstructive-palate",
    (G, "Deep Neck Abscess Drainage"): "deep-neck-drain",
    (T, "Four-Gland Parathyroid Exploration"): "four-gland",
    (T, "Submandibular Gland Excision"): "submandibular-gland",
    (L, "Transnasal Esophagoscopy"): "transnasal-esophagoscopy",
    (L, "Arytenoid Adduction / Reinnervation"): "arytenoid-adduction",
    (S, "Maxillomandibular Advancement"): "mma",
    # v62.0 new OR cards (or_cards_v620)
    (R, "Revision FESS"): "revision-fess",
    (R, "Endoscopic Pituitary / Anterior Skull Base Approach"): "endoscopic-pituitary",
    (P, "Supraglottoplasty"): "supraglottoplasty",
    (T, "Completion Thyroidectomy"): "completion-thyroidectomy",
}

BACKGROUND_KEYS = ("overview", "physiology", "pathophysiology")
DECISION_KEYS = ("recognize", "workup", "manage", "operate", "teach")


def install_or_merge_v610(app, data, app_mod):
    from flask import redirect, request

    registry = getattr(app_mod, "OR_PREP_REGISTRY", {}) or {}
    modules = {(d, m.get("topic")): m for d, ms in data.DEEP_MODULES_V6.items() for m in ms}
    sections_fn = getattr(data, "topic_sections_v470", None) or app.jinja_env.globals.get("topic_sections_v470")
    by_slug, merged = {}, {}
    for (domain, topic), slug in MERGE_V610.items():
        if slug in registry and (domain, topic) in modules:
            by_slug.setdefault(slug, []).append((domain, topic))
            merged[(domain, topic)] = slug
    data.OR_MERGE_V610 = merged

    def or_href(slug):
        return "/case-tomorrow?q=" + quote(registry[slug]["title"])

    # Disease topics behind each operation (TOPIC_OR_MAP_V470 reverse + the card's linked_topic).
    related_by_slug = {}
    for topic, slugs in (getattr(data, "TOPIC_OR_MAP_V470", {}) or {}).items():
        for slug in slugs or []:
            for (d, t) in modules:
                if t == topic and (d, t) not in merged:
                    related_by_slug.setdefault(slug, []).append((d, t))
    for slug, op in registry.items():
        lt = op.get("linked_topic")
        if lt:
            found = app_mod._find_deep_module_v94(op.get("domain", ""), lt.replace("-", " "))
            key = (found[0], found[1].get("topic")) if found and found[1] else None
            if key and key not in merged and key not in related_by_slug.get(slug, []):
                related_by_slug.setdefault(slug, []).append(key)

    def merged_curriculum_for(prep):
        """Curriculum teaching to show inline on an OR card: the operation's own topic (merged)
        first, then up to three disease topics behind it."""
        out = []
        slug = (prep or {}).get("slug")
        keys = [(k, True) for k in by_slug.get(slug, [])] + [(k, False) for k in related_by_slug.get(slug, [])[:3]]
        for (domain, topic), is_merged in keys:
            mod = modules[(domain, topic)]
            secs = sections_fn(mod) if sections_fn else []
            cid = app_mod._v6_item_id(domain, topic)
            n = sum(1 for q in data.CLINICAL_CHALLENGES_V119 if q.get("concept_id") == cid)
            out.append({
                "domain": domain, "topic": topic, "concept_id": cid, "question_total": n, "merged": is_merged,
                "background": [s for s in secs if s["key"] in BACKGROUND_KEYS],
                "decisions": [s for s in secs if s["key"] in DECISION_KEYS],
                "source_basis": mod.get("source_basis") or [],
            })
        return out

    def merged_or_for(domain, topic):
        slug = merged.get((domain, topic))
        return {"slug": slug, "title": registry[slug]["title"], "href": or_href(slug)} if slug else None

    app.jinja_env.globals["merged_curriculum_v610"] = merged_curriculum_for
    app.jinja_env.globals["merged_or_v610"] = merged_or_for

    # --- curriculum topic pages for merged operations open the OR card instead
    def _wrap(endpoint, resolve):
        view = app.view_functions.get(endpoint)
        if not view:
            return

        def wrapped(*a, **kw):
            key = resolve(*a, **kw)
            if key in merged and request.args.get("curriculum") != "1":
                return redirect(or_href(merged[key]), code=302)
            return view(*a, **kw)

        wrapped.__name__ = getattr(view, "__name__", endpoint)
        app.view_functions[endpoint] = wrapped

    def _by_query(*a, **kw):
        found = app_mod._find_deep_module_v94(request.args.get("domain", ""), request.args.get("topic", ""))
        return (found[0], found[1].get("topic")) if found and found[1] else None

    def _by_id(concept_id=None, *a, **kw):
        for key in merged:
            if app_mod._v6_item_id(*key) == concept_id:
                return key
        return None

    _wrap("concept_hub", _by_query)
    _wrap("concept_hub_id", _by_id)

    # --- search lists the operation once: drop the duplicate curriculum-concept row
    orig_index = getattr(app_mod, "_canonical_search_index", None)
    if orig_index:
        titles = {t for (_, t) in merged}

        def index_v610(*a, **kw):
            rows = orig_index(*a, **kw)
            return [r for r in rows if not (r.get("type") == "Curriculum concept" and r.get("title") in titles)]

        app_mod._canonical_search_index = index_v610

    # --- rank pages above individual questions: OR card, then topic page, then items
    orig_score = getattr(app_mod, "_search_score_v1009", None)
    if orig_score:
        boost = {"OR Tomorrow": 1500, "Curriculum concept": 800, "Progressive case": 200}

        def score_v610(row, q):
            sc = orig_score(row, q)
            if sc <= 0:
                return sc
            title = str(row.get("title") or "").lower()
            words = [w for w in str(q or "").lower().split() if len(w) > 2]
            ql = str(q or "").lower().strip()
            if ql and re.search(r"\b" + re.escape(ql) + r"\b", title):
                return sc + boost.get(row.get("type"), 0)
            if ql and ql in title:
                return sc + boost.get(row.get("type"), 0) * 2 // 3
            if words and all(w in title for w in words):
                return sc + boost.get(row.get("type"), 0) // 2
            return sc

        app_mod._search_score_v1009 = score_v610

    return {"merged": len(merged), "or_cards_with_merged_topic": len(by_slug),
            "or_cards_with_curriculum": len(set(by_slug) | set(related_by_slug))}
