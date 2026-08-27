"""v23.0 procedure-specific anatomy for salivary OR Tomorrow cases."""

TARGETS = [
    {
        "slug": "superficial-parotidectomy",
        "title_terms": ("superficial", "parotid"),
        "landmarks": [
            "tragal pointer, tympanomastoid suture, and posterior belly of digastric as complementary facial nerve trunk landmarks",
            "facial nerve trunk at the stylomastoid foramen, pes anserinus, and upper/lower divisions within the gland",
            "retromandibular vein and external carotid artery deep to the facial-nerve plane",
            "Stensen duct and masseter anteriorly",
            "greater auricular nerve over the sternocleidomastoid when oncologically preservable",
            "parotid fascia and superficial-lobe plane used to lift gland tissue away from facial-nerve branches",
        ],
    },
    {
        "slug": "total-parotidectomy",
        "title_terms": ("total", "parotid"),
        "landmarks": [
            "facial nerve trunk, pes anserinus, and complete intraparotid branching pattern",
            "deep lobe/parapharyngeal extension medial to the facial-nerve branches",
            "retromandibular vein and external carotid artery within the deep gland",
            "styloid process and parapharyngeal carotid-space relationships medially for deep-lobe disease",
            "Stensen duct and masseter anteriorly",
            "proximal and distal facial-nerve segments needed for oncologic control or reconstruction when nerve invasion is present",
        ],
    },
    {
        "slug": "submandibular-gland-excision",
        "title_terms": ("submandibular", "gland"),
        "landmarks": [
            "marginal mandibular branch superficial to the submandibular fascia near the mandibular border",
            "facial vein and facial artery wrapping the gland at its posterolateral surface",
            "mylohyoid muscle separating superficial and deep portions of the submandibular space",
            "lingual nerve looping around the submandibular ganglion and duct superiorly",
            "Wharton duct coursing anteriorly in the floor of mouth",
            "hypoglossal nerve deep/inferior to the duct on the hyoglossus surface",
        ],
    },
    {
        "slug": "sialendoscopy",
        "title_terms": ("sialendosc",),
        "landmarks": [
            "submandibular or parotid duct papilla and main duct lumen selected for endoscopic entry",
            "Wharton duct relationship to the lingual nerve in the posterior floor of mouth for submandibular work",
            "Stensen duct course over the masseter and through buccinator for parotid work",
            "duct branch-point anatomy, stenotic segments, and stone location relative to the hilum and intraparenchymal ducts",
            "floor-of-mouth mucosa and sublingual gland during combined transoral submandibular stone approaches",
            "adjacent lingual nerve territory as the key neural structure at risk during posterior ductotomy",
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


def apply_or_landmarks_v230(registry):
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
        op["landmarks_v230"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
