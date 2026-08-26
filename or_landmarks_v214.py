"""v21.4 procedure-specific anatomy landmarks for salivary OR Tomorrow cases.

The v19 family profile intentionally provided broad salivary anatomy, but that leaves
parotid and submandibular cases displaying each other's landmarks. This layer replaces
that family list only for reviewed salivary procedures so the night-before anatomy is
case-specific rather than additive boilerplate.
"""

TARGETS = [
    {
        "slug": "superficial-parotidectomy",
        "title_terms": ("superficial parotid",),
        "landmarks": [
            "facial nerve trunk and upper/lower divisions",
            "tragal pointer and tympanomastoid suture",
            "posterior belly of digastric",
            "sternocleidomastoid and mastoid tip",
            "retromandibular vein and external carotid branches",
            "Stensen duct when encountered by the resection",
        ],
    },
    {
        "slug": "total-parotidectomy",
        "title_terms": ("total parotid",),
        "landmarks": [
            "facial nerve trunk, pes anserinus, and peripheral branches",
            "tragal pointer and tympanomastoid suture",
            "posterior belly of digastric",
            "retromandibular vein and external carotid artery",
            "deep lobe/parapharyngeal space interface",
            "Stensen duct and masseteric surface as dictated by tumor extent",
        ],
    },
    {
        "slug": "submandibular-gland-excision",
        "title_terms": ("submandibular gland",),
        "landmarks": [
            "marginal mandibular nerve",
            "facial artery and facial vein",
            "mylohyoid posterior border",
            "lingual nerve and submandibular ganglion",
            "Wharton duct",
            "hypoglossal nerve",
        ],
    },
    {
        "slug": "sialendoscopy",
        "title_terms": ("sialendosc",),
        "landmarks": [
            "duct papilla and natural duct lumen",
            "main duct and branch-point anatomy",
            "Wharton duct relationship to the lingual nerve for posterior submandibular work",
            "Stensen duct course across masseter and through buccinator for parotid work",
            "stone/stenosis location relative to hilum and intraparenchymal branches",
        ],
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        title = str((op or {}).get("title", "")).lower()
        if all(term in title for term in target["title_terms"]):
            return slug, op
    return None, None


def apply_or_landmarks_v214(registry):
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
        op["landmarks_v214"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
