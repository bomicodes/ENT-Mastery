"""v22.1 procedure-specific anatomy for selected pediatric-airway OR Tomorrow cases.

Replaces broad pediatric-airway family landmarks where the operative corridor is
supraglottic, posterior laryngotracheal, or full diagnostic airway endoscopy.
"""

TARGETS = [
    {
        "slug": "supraglottoplasty",
        "title_terms": ("supraglottoplasty",),
        "landmarks": [
            "epiglottis and vallecular orientation",
            "aryepiglottic folds",
            "cuneiform/corniculate cartilages and redundant arytenoid mucosa",
            "interarytenoid/posterior supraglottic mucosa",
            "true vocal folds and anterior commissure as inferior safety boundaries",
            "arytenoid mucosa and cricoarytenoid joint region, which should not be excessively denuded bilaterally",
        ],
    },
    {
        "slug": "peds-ltr",
        "title_terms": ("laryngotracheal reconstruction",),
        "landmarks": [
            "thyroid cartilage, cricoid cartilage, and upper tracheal rings",
            "anterior cricoid arch and posterior cricoid plate",
            "posterior glottis and cricoarytenoid joints",
            "recurrent laryngeal nerve entry regions posterolateral to the cricoid framework",
            "esophageal mucosa immediately posterior to the posterior cricoid plate",
            "anterior/posterior cartilage graft beds and planned ETT/stent relationship",
        ],
    },
    {
        "slug": "laryngotracheal-cleft-repair",
        "title_terms": ("laryngotracheal", "cleft"),
        "landmarks": [
            "interarytenoid region and posterior commissure",
            "posterior cricoid plate and posterior laryngeal framework",
            "posterior tracheal membranous wall according to cleft extent",
            "anterior esophageal wall immediately behind the cleft",
            "separate airway and esophageal mucosal edges for layered repair",
            "recurrent laryngeal nerve regions lateral to the posterior laryngotracheal framework",
        ],
    },
    {
        "slug": "direct-laryngoscopy-bronchoscopy",
        "title_terms": ("direct laryngoscopy", "bronch"),
        "landmarks": [
            "epiglottis and supraglottic structures",
            "true vocal folds, anterior commissure, and posterior commissure",
            "subglottis and complete cricoid ring",
            "cervical and thoracic tracheal rings with posterior membranous wall",
            "carina",
            "right and left mainstem bronchi when complete bronchoscopy is indicated",
        ],
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in target["title_terms"]):
            return slug, op
    return None, None


def apply_or_landmarks_v221(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        desired = list(target["landmarks"])
        if list(op.get("landmarks") or []) != desired:
            op["landmarks"] = desired
            changed.append(slug)
        op["landmarks_v221"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
