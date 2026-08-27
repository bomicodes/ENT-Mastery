"""v23.2 procedure-specific anatomy for reoperative thyroid/parathyroid OR Tomorrow cases."""

TARGETS = [
    {
        "slug": "reop-thyroid",
        "title_terms": ("reoperative", "thyroid"),
        "landmarks": [
            "prior thyroid bed and scarred strap-muscle/capsular planes, where normal tissue planes may be obliterated",
            "recurrent laryngeal nerve identified from a less-scarred segment such as the lower tracheoesophageal groove or laryngeal entry point before dissecting dense Berry-region scar",
            "cricothyroid joint and laryngeal entry region of the recurrent nerve as a fixed superior landmark",
            "remaining superior/inferior parathyroid tissue and vascular pedicles, which may be displaced or scar-adherent after prior surgery",
            "Berry ligament/tracheal attachment and posteromedial thyroid remnant where nerve adherence is common",
            "carotid sheath, trachea, and esophagus defining lateral, medial, and posterior boundaries when scar distorts the thyroid bed",
        ],
    },
    {
        "slug": "reop-parathyroid",
        "title_terms": ("reoperative", "parathyroid"),
        "landmarks": [
            "recurrent laryngeal nerve approached from an unscarred or less-scarred segment before mobilizing tissue in the prior exploration bed",
            "tracheoesophageal groove and laryngeal entry point as fixed nerve landmarks when prior clips/scar distort expected parathyroid planes",
            "thyrothymic tract/thymic tongue, retroesophageal space, carotid sheath, and superior mediastinum as ectopic or missed-gland pathways",
            "prior clips, scar, and residual thyroid tissue used only as orientation aids rather than substitutes for direct nerve identification",
            "remaining viable parathyroid tissue and its blood supply, particularly important after prior multigland exploration",
            "esophagus, trachea, and carotid sheath delimiting deep reoperative search planes and protecting against blind scar dissection",
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


def apply_or_landmarks_v232(registry):
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
        op["landmarks_v232"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
