"""v21.5 procedure-specific anatomy for selected head-and-neck OR Tomorrow cases.

The v19 head-and-neck family profile intentionally supplies broad landmarks. For
major operations with very different dissection planes, replace that family list
with anatomy that directly governs the planned operation.
"""

TARGETS = [
    {
        "slug": "total-laryngectomy",
        "title_terms": ("total", "laryngectomy"),
        "landmarks": [
            "hyoid bone, thyroid cartilage, and cricoid cartilage",
            "superior thyroid pedicle and superior laryngeal neurovascular bundle",
            "pyriform sinuses and pharyngeal constrictor musculature",
            "pre-epiglottic and paraglottic spaces as dictated by tumor extent",
            "cervical trachea and planned permanent tracheal stoma",
            "carotid sheaths lateral to the laryngopharyngeal specimen",
        ],
    },
    {
        "slug": "neck-dissection",
        "title_terms": ("neck", "dissection"),
        "landmarks": [
            "sternocleidomastoid muscle and investing fascia",
            "spinal accessory nerve (CN XI)",
            "internal jugular vein and carotid artery/vagus nerve",
            "hypoglossal nerve and posterior belly of digastric",
            "phrenic nerve and brachial plexus on the deep cervical fascia",
            "thoracic duct on the left at the venous angle/low neck",
        ],
    },
    {
        "slug": "oral-composite",
        "title_terms": ("oral", "composite"),
        "landmarks": [
            "mandible and mandibular periosteum/inferior alveolar canal when involved",
            "lingual nerve",
            "hypoglossal nerve",
            "lingual artery and floor-of-mouth vascular pedicles",
            "Wharton duct and sublingual/submandibular space anatomy",
            "tongue-base, mylohyoid, and adjacent pharyngeal musculature according to tumor extent",
        ],
    },
    {
        "slug": "conservation-laryngectomy",
        "title_terms": ("conservation", "laryngectomy"),
        "landmarks": [
            "thyroid cartilage, cricoid cartilage, and hyoid bone",
            "anterior commissure and Broyles ligament region",
            "pre-epiglottic and paraglottic spaces",
            "arytenoid and cricoarytenoid unit",
            "pyriform sinus and tongue-base mucosal margins",
            "recurrent laryngeal nerve entry region relative to the preserved functional unit",
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


def apply_or_landmarks_v215(registry):
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
        op["landmarks_v215"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
