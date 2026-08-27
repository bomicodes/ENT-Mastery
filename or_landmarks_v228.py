"""v22.8 procedure-specific anatomy for selected sleep-surgery OR Tomorrow cases.

Replaces broad sleep/airway family landmarks for hypoglossal-nerve stimulation and
hyoid/genioglossus procedures with the structures that govern nerve selection,
implant placement, airway-vector surgery, and donor-site safety.
"""

TARGETS = [
    {
        "slug": "hypoglossal-nerve-stimulation",
        "title_terms": ("hypoglossal",),
        "exclude_terms": ("reanimation",),
        "landmarks": [
            "posterior belly of digastric and submandibular upper-neck corridor used to localize the hypoglossal nerve",
            "main hypoglossal nerve trunk and distal branching pattern into protrusor versus retrusor tongue branches",
            "genioglossus/protrusor branch territory selected for inclusion within the stimulation cuff",
            "hyoglossus region and lingual neurovascular structures, which should not be injured during distal nerve dissection",
            "intercostal muscle planes and pleura at the respiratory-sensing lead site",
            "subcutaneous generator pocket and tunneled lead course, which must remain free of sharp angulation or compression",
        ],
    },
    {
        "slug": "hyoid-genioglossus",
        "title_terms": ("hyoid", "genioglossus"),
        "exclude_terms": (),
        "landmarks": [
            "genial tubercle and genioglossus attachment on the lingual mandibular cortex",
            "mandibular tooth roots and mental/inferior-alveolar neurovascular structures defining safe osteotomy limits",
            "hyoid body and greater cornua",
            "hypoglossal nerve coursing superior to the hyoid and deep to the digastric/stylohyoid region",
            "superior laryngeal neurovascular structures and thyrohyoid membrane near the hyoid suspension field",
            "thyroid cartilage or mandibular fixation target used to establish the planned anterior/superior hyoid vector",
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


def apply_or_landmarks_v228(registry):
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
        op["landmarks_v228"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
