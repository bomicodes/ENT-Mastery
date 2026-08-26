"""v22.3 procedure-specific anatomy for selected facial-trauma OR Tomorrow cases.

Replaces broad facial-trauma family landmarks where orbital-floor and frontal-sinus
operations depend on different danger structures and reconstructive boundaries.
"""

TARGETS = [
    {
        "slug": "orbital-floor",
        "title_terms": ("orbital", "floor"),
        "landmarks": [
            "infraorbital rim and orbital floor",
            "infraorbital groove/canal and infraorbital nerve",
            "periorbita and prolapsed orbital fat",
            "inferior rectus and inferior oblique muscles",
            "maxillary sinus immediately below the orbital floor",
            "stable posterior and medial bony ledges needed to support reconstruction without extending blindly toward the orbital apex/optic nerve",
        ],
    },
    {
        "slug": "frontal-sinus-trauma",
        "title_terms": ("frontal", "sinus", "trauma"),
        "landmarks": [
            "frontal sinus anterior table and supraorbital rim",
            "posterior table and adjacent frontal-lobe dura",
            "frontal sinus outflow tract/frontal recess",
            "interfrontal sinus septum and sinus mucosal recesses",
            "supraorbital and supratrochlear neurovascular structures",
            "anterior cranial fossa/orbital roof relationship at the inferior-posterior sinus boundaries",
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


def apply_or_landmarks_v223(registry):
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
        op["landmarks_v223"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
