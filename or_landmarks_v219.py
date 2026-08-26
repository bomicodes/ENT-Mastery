"""v21.9 procedure-specific anatomy for selected laryngology/swallowing OR cases.

Replaces the broad laryngology family landmark list where the operative corridor is
framework, injection, or pharyngoesophageal rather than generic endolaryngeal work.
"""

TARGETS = [
    {
        "slug": "medialization-thyroplasty",
        "title_terms": ("medialization", "thyroplasty"),
        "landmarks": [
            "thyroid cartilage ala, thyroid notch, and inferior border for external framework orientation",
            "true vocal-fold level projected onto the thyroid ala",
            "inner thyroid perichondrium",
            "paraglottic space and thyroarytenoid muscle medial to the thyroplasty window",
            "cricothyroid membrane/joint region inferiorly",
            "arytenoid and vocal process when posterior-gap or height correction is being considered",
        ],
    },
    {
        "slug": "injection-laryngoplasty",
        "title_terms": ("injection", "laryngoplast"),
        "landmarks": [
            "true vocal fold and free vibratory edge",
            "thyroarytenoid muscle/paraglottic space as the augmentation target",
            "vocal process and posterior glottis for anterior-posterior gap orientation",
            "ventricle and false vocal fold as superior endoscopic landmarks",
            "superficial lamina propria, which should not be intentionally injected for bulk medialization",
            "cricothyroid membrane or thyroid-cartilage landmarks according to the selected percutaneous approach",
        ],
    },
    {
        "slug": "zenker-diverticulotomy",
        "title_terms": ("zenker",),
        "landmarks": [
            "Zenker pouch and true esophageal lumen",
            "common diverticular septum",
            "cricopharyngeus muscle within the septal target",
            "Killian dehiscence between thyropharyngeus and cricopharyngeus",
            "posterior hypopharyngeal/cervical esophageal wall",
            "recurrent laryngeal nerve and cervical esophageal planes when an open approach is used",
        ],
    },
    {
        "slug": "cricopharyngeal-myotomy",
        "title_terms": ("cricopharyngeal", "myotomy"),
        "landmarks": [
            "inferior pharyngeal constrictor/thyropharyngeus",
            "cricopharyngeus muscle at the pharyngoesophageal segment",
            "proximal cervical esophageal longitudinal/circular muscle",
            "intact pharyngoesophageal mucosa immediately deep to the myotomy",
            "recurrent laryngeal nerve in the tracheoesophageal groove/laryngeal entry region",
            "thyroid, trachea, and carotid-sheath relationships defining the cervical exposure",
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


def apply_or_landmarks_v219(registry):
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
        op["landmarks_v219"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
