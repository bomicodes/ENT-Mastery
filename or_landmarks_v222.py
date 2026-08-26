"""v22.2 procedure-specific anatomy for selected rhinology OR Tomorrow cases.

Replaces the broad sinus-family danger-structure list where the operative corridor
is septal, maxillary, or medial orbital rather than a generic endoscopic sinus case.
"""

TARGETS = [
    {
        "slug": "septoplasty",
        "title_terms": ("septoplasty",),
        "landmarks": [
            "quadrangular cartilage and perpendicular plate of the ethmoid",
            "vomer and maxillary crest",
            "mucoperichondrial/mucoperiosteal flaps on each side of the septum",
            "dorsal and caudal L-strut required for structural support",
            "anterior nasal spine and caudal septal attachment",
            "keystone region where septal cartilage joins the upper lateral cartilages and nasal bones",
        ],
    },
    {
        "slug": "maxillary-antrostomy",
        "title_terms": ("maxillary", "antrostomy"),
        "landmarks": [
            "middle turbinate and uncinate process",
            "ethmoid infundibulum and hiatus semilunaris",
            "natural maxillary ostium, which must be incorporated into the antrostomy",
            "nasolacrimal duct anterior to the safe antrostomy enlargement",
            "lamina papyracea/orbit superior-lateral to the maxillary ostium region",
            "posterior fontanelle/accessory ostium when present, joined to the natural ostium to avoid recirculation",
        ],
    },
    {
        "slug": "orbital-abscess",
        "title_terms": ("orbital", "abscess"),
        "landmarks": [
            "lamina papyracea and periorbita",
            "medial rectus muscle immediately lateral to the medial orbital wall",
            "ethmoid roof/skull base superiorly",
            "anterior and posterior ethmoid arteries at the frontoethmoidal region",
            "optic nerve/orbital apex as the posterior danger zone",
            "adjacent ethmoid, maxillary, and frontal drainage pathways according to the infectious source",
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


def apply_or_landmarks_v222(registry):
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
        op["landmarks_v222"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
