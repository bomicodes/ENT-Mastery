"""v21.3 procedure-changing preoperative decisions for laryngeal and pediatric airway cases.

Adds only high-confidence factors that can change candidacy, approach, extent, airway
planning, or postoperative disposition. The operative choreography remains in the
existing procedure-sequence layers.
"""

TRACHEAL_RESECTION_TEXT = "In addition to stenosis length, determine whether a tension-free resection is anatomically feasible: review distance from the cricoid and thoracic inlet/innominate region, prior tracheostomy or resection, neck/chest radiation and need for release maneuvers; coordinate the intraoperative ventilation strategy and backup airway before induction rather than discovering an unresectable or unsafe airway after exposure."

TARGETS = [
    {
        "slug": "conservation-laryngectomy",
        "title_terms": ("conservation", "laryng"),
        "text": "Before planning conservation laryngectomy, confirm that oncologic extent and function permit preservation: define subglottic, pre-epiglottic/paraglottic, cartilage, arytenoid/cricoarytenoid-unit and extralaryngeal involvement, document vocal-fold/arytenoid mobility, and assess pulmonary reserve, swallowing/aspiration risk and ability to participate in rehabilitation. A nonfunctional required cricoarytenoid unit or disease that cannot be cleared with appropriate margins should redirect the plan rather than be forced into a conservation operation.",
    },
    {
        "slug": "transoral-laser-laryngeal-cancer",
        "title_terms": ("transoral", "laser", "laryngeal"),
        "text": "Confirm that the tumor can be completely exposed transorally and map anterior-commissure, subglottic, paraglottic, cartilage and arytenoid involvement on endoscopy/imaging before choosing laser resection; inadequate exposure or disease requiring unsafe deep/cartilage margins should trigger an alternate oncologic approach rather than piecemeal compromise.",
    },
    {
        "slug": "supraglottoplasty",
        "title_terms": ("supraglottoplasty",),
        "text": "Confirm that clinically important symptoms are attributable to laryngomalacia rather than another airway or swallowing disorder; review feeding/aspiration history, weight gain, oxygen/OSA burden and neurologic/cardiopulmonary comorbidity, and plan complete airway endoscopy when indicated because synchronous lesions and severe comorbidity can change both the operation and postoperative level of care.",
    },
    {
        "slug": "laryngotracheal-cleft-repair",
        "title_terms": ("laryngotracheal", "cleft"),
        "text": "Define cleft type/length and aspiration physiology before repair using endoscopic assessment plus swallow/feeding history; review pulmonary morbidity, reflux/esophageal disease and prior feeding interventions, because limited type I disease may be managed differently from deeper clefts and larger defects require a deliberate open-versus-endoscopic and postoperative airway/feeding plan.",
    },
    {
        "slug": "direct-laryngoscopy-bronchoscopy",
        "title_terms": ("direct laryngoscopy", "bronch"),
        "text": "Before shared-airway endoscopy, define the suspected lesion and physiologic airway risk from symptoms, prior airway history/endoscopy and imaging when relevant; agree with anesthesia on spontaneous versus controlled ventilation and rescue strategy before induction, especially when critical stenosis, foreign body, mediastinal mass effect or difficult reintubation is possible.",
    },
    {
        "slug": "tracheal-resection",
        "title_terms": ("tracheal", "resection"),
        "text": TRACHEAL_RESECTION_TEXT,
    },
    {
        "slug": "ctr",
        "title_terms": ("cricotracheal", "resection"),
        "text": TRACHEAL_RESECTION_TEXT,
    },
]


def _prepend_unique(values, text):
    out = list(values or [])
    marker = text[:64].lower()
    if any(marker in str(x).lower() for x in out):
        return out, False
    out.insert(0, text)
    return out, True


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        title = str((op or {}).get("title", "")).lower()
        if all(term in title for term in target["title_terms"]):
            return slug, op
    return None, None


def apply_or_preop_decision_v213(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], did_change = _prepend_unique(op.get("setup"), target["text"])
        op["preop_decision_v213"] = True
        resolved.append(slug)
        if did_change:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}