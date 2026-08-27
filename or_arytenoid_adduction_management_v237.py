"""v23.7+ arytenoid-adduction OR Tomorrow planning and postoperative rescue.

Later pediatric adenotonsillar management is chained here so the existing decision
hook remains atomic.
"""

from or_adenotonsillar_management_v238 import apply_or_adenotonsillar_management_v238

TARGETS = [
    {
        "slug": "arytenoid-adduction",
        "title_terms": ("arytenoid", "adduction"),
        "setup": [
            "Before arytenoid adduction, confirm the cause, duration and recovery potential of unilateral vocal-fold immobility and define the glottic-gap pattern with flexible laryngoscopy/stroboscopy. A substantial posterior gap or vertical height mismatch is the key anatomic problem this operation addresses; decide deliberately whether concurrent type I medialization is needed rather than assuming either procedure alone will correct the entire insufficiency.",
            "Document baseline voice, cough effectiveness, swallowing/aspiration symptoms, contralateral vocal-fold mobility and airway reserve. Review prior neck/framework surgery and counsel that the operative endpoint is improved posterior closure and arytenoid height/rotation without excessive adduction that compromises the airway or swallowing.",
        ],
        "postop": [
            "After arytenoid adduction, new stridor, increasing work of breathing, progressive neck swelling or rapidly worsening dysphagia requires urgent airway and laryngoscopic assessment for edema, hematoma or excessive medialization rather than routine observation.",
            "Reassess voice, vocal-fold position and swallowing after healing. Persistent posterior insufficiency or height mismatch suggests undercorrection/suture-vector or arytenoid-position problems, whereas marked airway narrowing, strained voice or worsened swallowing raises concern for overadduction or combined-framework overcorrection.",
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


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:64].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_arytenoid_adduction_management_v237(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["arytenoid_adduction_management_v237"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v238 = apply_or_adenotonsillar_management_v238(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v238": v238}
