"""v23.10 cochlear-implant OR Tomorrow planning and postoperative rescue.

Adds procedure-specific candidacy, imaging/device planning, and postoperative red flags
for cochlear implantation. Operative choreography and anatomy remain in existing
reviewed layers.
"""

TARGETS = [
    {
        "slug": "cochlear-implant",
        "title_terms": ("cochlear", "implant"),
        "setup": [
            "Before cochlear implantation, verify that the current audiologic profile and aided performance support implantation rather than relying on unaided thresholds alone. Review speech-recognition testing, hearing-aid use/optimization, communication goals, contralateral-ear status, expected rehabilitation, and whether single-sided deafness, asymmetric loss, residual low-frequency hearing, or bilateral severe loss changes the counseling and electrode/hearing-preservation strategy.",
            "Review temporal-bone imaging for cochlear patency and malformation, facial-nerve course, mastoid/middle-ear anatomy, prior surgery, ossification or labyrinthitis history, and any finding that could alter the round-window/facial-recess approach. Confirm device side, manufacturer/electrode plan, vaccination status according to current cochlear-implant guidance, and whether MRI needs or anatomic factors affect implant selection/positioning.",
            "Set expectations that surgery provides access to auditory input rather than immediate normal hearing: postoperative programming and auditory rehabilitation are integral to outcome. In children, coordinate developmental/language and educational goals; in adults, document realistic speech-perception expectations and the implications of prolonged auditory deprivation or major cochlear/nerve abnormality.",
        ],
        "postop": [
            "After cochlear implantation, new facial weakness, severe or progressive vertigo, sudden major change in residual hearing, clear otorrhea/rhinorrhea, meningitic symptoms, expanding postauricular swelling, wound breakdown or device exposure is not routine postoperative discomfort and warrants prompt otologic assessment for nerve injury, inner-ear complication, CSF leak, infection or hematoma.",
            "Persistent erythema, fluctuance, drainage, skin thinning or pain over the receiver-stimulator should raise concern for implant-site infection or threatened extrusion rather than being managed indefinitely as superficial dermatitis. Deep device infection or exposure may require operative management and, in selected cases, explantation rather than repeated oral antibiotics alone.",
            "If activation or later performance is unexpectedly poor, do not assume the patient simply needs more time. Confirm device integrity and programming, electrode position when indicated, auditory-nerve/cochlear factors, rehabilitation participation, and interval medical problems; sudden loss of implant function or new neurologic/vestibular symptoms warrants expedited device and clinical evaluation.",
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


def apply_or_cochlear_implant_management_v2310(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["cochlear_implant_management_v2310"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
