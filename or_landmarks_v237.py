"""v23.7 procedure-specific anatomy for arytenoid adduction in OR Tomorrow."""

TARGETS = [
    {
        "slug": "arytenoid-adduction",
        "title_terms": ("arytenoid", "adduction"),
        "landmarks": [
            "posterior thyroid ala and posterior thyroid border defining the external framework corridor",
            "cricoid lamina and cricoarytenoid joint immediately deep/posterior to the thyroid framework",
            "muscular process of the arytenoid as the traction-suture target",
            "vocal process and true vocal-fold position as the functional endpoint of arytenoid rotation",
            "pyriform sinus mucosa medial to the posterior framework exposure, which should remain intact",
            "recurrent laryngeal nerve laryngeal-entry region and posterior laryngeal soft tissues, which should not be blindly dissected or entrapped by the adduction suture",
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


def apply_or_landmarks_v237(registry):
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
        op["landmarks_v237"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
