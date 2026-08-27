"""v22.7 procedure-specific anatomy for surgical tracheostomy OR Tomorrow.

Replaces broad airway-family landmarks with the anterior cervical structures that
actually govern safe tracheal exposure, tube placement, hemorrhage risk, and rescue.
"""

TARGETS = [
    {
        "slug": "tracheostomy",
        "title_terms": ("tracheostomy",),
        "exclude_terms": ("laryngectomy", "tracheoesophageal puncture", "tep"),
        "landmarks": [
            "thyroid notch, cricoid cartilage, and midline anterior trachea for surface orientation",
            "strap muscles and avascular midline raphe over the pretracheal plane",
            "thyroid isthmus crossing the upper tracheal rings and requiring retraction or division according to exposure",
            "second through fourth tracheal rings as the usual surgical window region, avoiding an unnecessarily high opening near the cricoid",
            "recurrent laryngeal nerves in the posterolateral tracheoesophageal grooves, protected by remaining in the anterior midline",
            "innominate artery at the lower cervical/upper mediastinal trachea as the critical inferior vascular danger structure, especially with a low tracheostomy",
        ],
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if not all(term in hay for term in target["title_terms"]):
            continue
        if any(term in hay for term in target.get("exclude_terms", ())):
            continue
        return slug, op
    return None, None


def apply_or_landmarks_v227(registry):
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
        op["landmarks_v227"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
