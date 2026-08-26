"""v21.6+ procedure-specific anatomy for selected otology OR Tomorrow cases.

Replaces the broad otology family landmark list for operations where the operative
corridor and danger structures differ enough that a generic ear list is misleading.
Later reviewed laryngology/swallowing landmarks are chained here so the existing
runtime anatomy hook remains atomic.
"""

from or_landmarks_v219 import apply_or_landmarks_v219

TARGETS = [
    {
        "slug": "stapedotomy",
        "title_terms": ("staped",),
        "landmarks": [
            "long process/lenticular process of the incus",
            "stapes head, crura, and footplate in the oval window",
            "pyramidal eminence and stapedius tendon",
            "tympanic segment of the facial nerve above the oval window",
            "chorda tympani in the posterior mesotympanum",
            "promontory and round-window niche as inferior orientation landmarks",
        ],
    },
    {
        "slug": "cochlear-implant",
        "title_terms": ("cochlear", "implant"),
        "landmarks": [
            "tegmen, sigmoid sinus, posterior external auditory canal wall, and lateral semicircular canal",
            "short process of the incus/incus buttress for facial-recess orientation",
            "mastoid segment of the facial nerve",
            "chorda tympani forming the lateral boundary of the facial recess",
            "round-window niche and membrane",
            "cochlear promontory and basal-turn entry trajectory",
        ],
    },
    {
        "slug": "cholesteatoma",
        "title_terms": ("cholesteat",),
        "landmarks": [
            "tegmen tympani/mastoideum and middle-fossa dura",
            "sigmoid sinus",
            "lateral semicircular canal and labyrinth",
            "mastoid and tympanic segments of the facial nerve",
            "incus short process, antrum, and epitympanum",
            "facial recess, sinus tympani, and other hidden middle-ear recesses",
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


def apply_or_landmarks_v216(registry):
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
        op["landmarks_v216"] = "procedure-specific"
        resolved.append(slug)
    v219 = apply_or_landmarks_v219(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v219": v219}
