"""v22.4 procedure-specific anatomy for selected reconstruction OR Tomorrow cases.

Replaces broad reconstruction-family landmarks where microsurgical transfer, local
nasal flap design, facial reanimation, and auricular framework reconstruction depend
on different operative structures and danger zones.
"""

TARGETS = [
    {
        "slug": "free-flap-basics",
        "title_terms": ("free", "flap"),
        "landmarks": [
            "selected flap's named arterial pedicle and accompanying venous outflow",
            "recipient neck artery with healthy adventitia and adequate length for tension-free microvascular inflow",
            "recipient vein and internal/external jugular system relationship for unobstructed venous drainage",
            "pedicle course from flap to recipient vessels without twist, kink, compression, or acute angulation",
            "mandibular edge, drain paths, and closure planes that can compress the pedicle after inset",
            "donor-site motor/sensory nerves and critical tendons or bone structures that should be preserved during harvest",
        ],
    },
    {
        "slug": "bilobed-flap",
        "title_terms": ("bilobed", "flap"),
        "landmarks": [
            "primary nasal defect and adjacent lax skin reservoir",
            "shared pivot point and common flap base",
            "first and second lobe arcs with tension distributed across both donor sites",
            "subdermal vascular plexus preserved within the flap thickness",
            "alar rim/soft triangle and nearby free margins vulnerable to distortion",
            "nasal aesthetic-subunit boundaries and standing-cone sites that influence final contour",
        ],
    },
    {
        "slug": "facial-nerve-reanimation",
        "title_terms": ("facial", "reanimation"),
        "landmarks": [
            "facial nerve main trunk/pes anserinus and usable distal facial branches",
            "zygomatic and buccal divisions supplying smile musculature",
            "masseteric nerve on the deep surface of masseter when used as a donor",
            "hypoglossal nerve in the upper neck when used for hypoglossal-facial transfer",
            "interposition nerve-graft course between healthy proximal/donor and distal recipient fascicles",
            "parotid/cheek soft-tissue bed where coaptations must lie without tension, twist, or external compression",
        ],
    },
    {
        "slug": "microtia-reconstruction",
        "title_terms": ("microtia",),
        "landmarks": [
            "contralateral helix, antihelix, conchal bowl, tragus, and lobule used to template auricular position and contour",
            "temporoparietal fascia and superficial temporal vascular axis when vascularized fascial coverage is required",
            "mastoid/periauricular skin envelope and planned framework pocket",
            "costal cartilage synchondrosis and perichondrial planes used for framework harvest",
            "pleura deep to the rib donor site as the major harvest danger structure",
            "framework base, projection, and lobule relationship that determine final auricular position",
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


def apply_or_landmarks_v224(registry):
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
        op["landmarks_v224"] = "procedure-specific"
        resolved.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
