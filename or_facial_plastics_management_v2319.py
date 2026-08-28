"""v23.19 facial-plastics OR Tomorrow management review.

Adds reconstruction selection and postoperative flap/graft rescue to seven facial-plastic
procedures that remained generic-only after the full OR audit. Existing design anatomy
and operative sequences remain intact.
"""

TARGETS = [
    {
        "slug": "bilobed-flap",
        "title_terms": ("bilobed",),
        "setup": [
            "Before a bilobed nasal flap, confirm that local tissue recruitment is appropriate for the defect's size, depth and subunit and identify whether exposed cartilage/bone, missing lining or structural support requires more than skin coverage. Design the pivot and both lobes around available laxity while explicitly assessing alar rim/soft-triangle distortion risk; a technically closable defect is not a good bilobed-flap indication if closure will retract the nostril margin or cross critical subunit boundaries poorly.",
        ],
        "postop": [
            "After bilobed reconstruction, assess color, capillary refill, temperature and progressive swelling rather than assuming all duskiness is routine bruising. Expanding hematoma, tense venous congestion or rapidly worsening pallor can threaten the flap and merits early intervention; later pincushion/trapdoor deformity, standing-cone distortion or alar retraction should be evaluated as vector/scar problems rather than simply waiting indefinitely for edema to resolve.",
        ],
        "marker": "bilobed_flap_management_v2319",
    },
    {
        "slug": "cervicofacial-flap",
        "title_terms": ("cervicofacial",),
        "setup": [
            "Before a cervicofacial advancement/rotation flap, map the defect, anticipated arc of rotation, distal perfusion and closure vectors and decide whether the defect can be closed without excessive lower-eyelid or oral commissure traction. Review prior radiation, scars, smoking and vascular comorbidity, and choose the dissection plane with awareness of facial-nerve branches and the need to preserve a broad, well-perfused flap base.",
        ],
        "postop": [
            "After cervicofacial flap reconstruction, an expanding hematoma, progressive distal duskiness/pallor, blistering or wound-edge necrosis requires prompt perfusion and tension assessment. Specifically reassess lower-eyelid position and oral commissure because ectropion or distortion can emerge as edema resolves and scar contraction develops even when the flap survives.",
        ],
        "marker": "cervicofacial_flap_management_v2319",
    },
    {
        "slug": "forehead-flap",
        "title_terms": ("forehead", "flap"),
        "setup": [
            "Before a paramedian forehead flap, reconstruct the nasal defect in layers: determine skin cover, internal lining and cartilage/bony support needs before designing the flap. Plan pedicle laterality/width around the supratrochlear vascular axis, account for prior forehead scars or vascular injury and counsel that this is usually a staged reconstruction with later thinning/contouring and pedicle division rather than a single definitive operation.",
        ],
        "postop": [
            "After forehead-flap transfer, monitor the entire flap and pedicle for venous congestion, arterial insufficiency, compression, twisting and hematoma. Abrupt color/temperature or capillary-refill deterioration should trigger immediate assessment of pedicle geometry and external compression; later revision planning should address contour, lining/support and scar without dividing or aggressively thinning the pedicle before vascular autonomy is established.",
        ],
        "marker": "forehead_flap_management_v2319",
    },
    {
        "slug": "melolabial-flap",
        "title_terms": ("melolabial",),
        "setup": [
            "Before a melolabial/nasolabial flap, define whether the target defect involves external cover only or also alar lining/support, and select a superiorly or inferiorly based design according to reach and vascular reliability. Plan the inset so donor closure and flap bulk do not elevate or retract the ala, narrow the nostril or distort the oral commissure.",
        ],
        "postop": [
            "After melolabial reconstruction, progressive congestion, pallor, hematoma or excessive tension at the inset requires early flap assessment. Once healed, reassess alar position, nostril symmetry, airway and contour because trapdoor/pincushion deformity or alar retraction can reflect flap thickness and scar vector despite complete survival.",
        ],
        "marker": "melolabial_flap_management_v2319",
    },
    {
        "slug": "otoplasty",
        "title_terms": ("otoplasty",),
        "setup": [
            "Before otoplasty, analyze the specific deformity—underdeveloped antihelical fold, conchal excess/depth, lobular prominence, asymmetry or a combination—and match the correction to that anatomy rather than applying one maneuver to every prominent ear. Document baseline asymmetry and skin/cartilage quality and plan correction that avoids over-set ears or excessive conchal-mastoid narrowing.",
        ],
        "postop": [
            "Severe increasing auricular pain, tense swelling or asymmetry after otoplasty should raise concern for hematoma, which threatens cartilage and can lead to deformity if untreated. Progressive erythema, drainage or cartilage tenderness suggests infection/perichondritis; later recurrence, overcorrection, contour irregularity or suture extrusion should be assessed separately from early postoperative edema.",
        ],
        "marker": "otoplasty_management_v2319",
    },
    {
        "slug": "septorhino",
        "title_terms": ("septorhinoplasty",),
        "setup": [
            "Before functional septorhinoplasty/nasal-valve repair, separate each contributor to obstruction: septal deviation, internal/external valve narrowing or dynamic collapse, turbinate disease and external framework deformity. Document baseline photographs and airway findings, review prior trauma/surgery and define which structural grafting or osteotomy maneuvers are needed while preserving or rebuilding dorsal/caudal septal support rather than treating the case as an extended septoplasty alone.",
        ],
        "postop": [
            "After septorhinoplasty, rapidly progressive obstruction with septal swelling, uncontrolled epistaxis, fever, severe pain, visual symptoms or clear unilateral rhinorrhea requires targeted evaluation for hematoma/abscess, bleeding, orbital complication or CSF leak rather than routine reassurance. Long-term airway or cosmetic assessment should wait for appropriate edema resolution, but persistent valve collapse, synechiae, septal perforation, graft displacement/warping or structural asymmetry requires an anatomic explanation rather than repeated decongestant therapy alone.",
        ],
        "marker": "septorhinoplasty_management_v2319",
    },
    {
        "slug": "skin-graft-face",
        "title_terms": ("skin", "graft"),
        "setup": [
            "Before facial skin grafting, confirm that the recipient bed is vascular enough to support a graft and choose full- versus split-thickness tissue based on defect depth, contour, contraction risk, color/texture match and donor morbidity. Exposed avascular cartilage or bone without perichondrium/periosteum, active infection or an uncorrected contour/support problem may require a different reconstructive strategy rather than simply a thicker graft.",
        ],
        "postop": [
            "Early graft survival depends on immobility and contact with the recipient bed: hematoma/seroma, shear, infection or a poorly secured bolster can cause partial or complete loss and should be addressed promptly. Later contraction, contour depression, pigment/texture mismatch or eyelid/nasal-margin distortion should be assessed as reconstructive sequelae rather than graft 'failure' alone, particularly near free margins where contracture can impair function.",
        ],
        "marker": "facial_skin_graft_management_v2319",
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
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_facial_plastics_management_v2319(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
