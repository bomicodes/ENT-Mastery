"""v23.1+ procedure-specific thyroid/parathyroid anatomy for OR Tomorrow.

Later reviewed reoperative endocrine anatomy is chained here so the runtime anatomy
hook remains atomic.
"""

from or_landmarks_v232 import apply_or_landmarks_v232

TARGETS = [
    {
        "slug": "total-thyroidectomy",
        "title_terms": ("total", "thyroidectomy"),
        "landmarks": [
            "superior thyroid pole and external branch of the superior laryngeal nerve near the superior thyroid vessels",
            "recurrent laryngeal nerve from the tracheoesophageal groove to its laryngeal entry near the cricothyroid joint",
            "superior parathyroid near the posterior upper/mid thyroid and inferior parathyroid near the lower pole/thyrothymic tract",
            "inferior thyroid artery branches and parathyroid vascular pedicles",
            "Berry ligament at the posteromedial thyroid-tracheal attachment where the recurrent nerve is especially vulnerable",
            "trachea, esophagus, and carotid sheath defining the medial, posterior, and lateral limits of capsular dissection",
        ],
    },
    {
        "slug": "thyroid-lobectomy",
        "title_terms": ("thyroid", "lobectomy"),
        "landmarks": [
            "superior thyroid pole and external branch of the superior laryngeal nerve",
            "middle thyroid vein and lateral thyroid capsule used for medial rotation",
            "recurrent laryngeal nerve in the tracheoesophageal groove and at the laryngeal entry point",
            "superior and inferior parathyroid glands with their terminal vascular pedicles",
            "Berry ligament and posteromedial thyroid attachment to the trachea",
            "thyroid isthmus and contralateral tracheal surface defining the planned unilateral extent",
        ],
    },
    {
        "slug": "parathyroidectomy",
        "title_terms": ("parathyroidectomy",),
        "landmarks": [
            "recurrent laryngeal nerve and tracheoesophageal groove",
            "superior parathyroid embryologic position posterior to the upper/mid thyroid, usually dorsal to the recurrent nerve plane",
            "inferior parathyroid pathway near the lower pole and thyrothymic tract with greater positional variability",
            "inferior thyroid artery and terminal glandular vascular pedicle",
            "thyrothymic ligament/thymus, retroesophageal space, carotid sheath, and superior mediastinal direction as ectopic search pathways",
            "thyroid capsule and adjacent fat/lymph nodes that can mimic parathyroid tissue during focused exploration",
        ],
    },
    {
        "slug": "four-gland",
        "title_terms": ("four-gland", "parathyroid"),
        "landmarks": [
            "both recurrent laryngeal nerves and bilateral tracheoesophageal grooves",
            "expected superior parathyroid positions posterior to each upper/mid thyroid lobe",
            "expected inferior parathyroid positions from each lower pole through the thyrothymic tract",
            "inferior thyroid arteries and individual parathyroid vascular pedicles",
            "thyrothymic ligaments/thymic tongues, retroesophageal space, carotid sheaths, and mediastinal descent for missing glands",
            "remaining well-vascularized parathyroid tissue that must be preserved when subtotal resection is planned",
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


def apply_or_landmarks_v231(registry):
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
        op["landmarks_v231"] = "procedure-specific"
        resolved.append(slug)
    v232 = apply_or_landmarks_v232(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v232": v232}
