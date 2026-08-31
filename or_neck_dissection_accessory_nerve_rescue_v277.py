"""v27.7 neck-dissection spinal-accessory-nerve preservation and rescue layer.

Adds a chief-level CN XI commitment point, low-trauma dissection principles, immediate
injury reconstruction logic, and postoperative shoulder-rescue choreography without
making routine nerve monitoring a universal requirement.
"""

ACCESSORY_NERVE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Koliarakis I et al. Spinal accessory nerve anatomy in the posterior cervical triangle: a systematic review with meta-analysis. Clin Anat. 2024;37:441-456.",
    "Elsawi RS et al. Surgical treatment of trapezius palsy: a systematic review. Shoulder Elbow. 2020;12(3):153-162.",
    "McGarvey AC et al. Intra-operative monitoring of the spinal accessory nerve: a systematic review. J Laryngol Otol. 2014;128(9):746-751.",
    "Intra-operative neuromonitoring and electrophysiological nerve stimulation for the spinal accessory and marginal mandibular nerve during neck dissection: a scoping review. J Laryngol Otol. 2026.",
]

TARGETS = [{
    "slug": "neck-dissection",
    "title_terms": ("neck", "dissection"),
    "setup": [
        "Make spinal accessory nerve status an explicit commitment point before level II/posterior-triangle dissection. In a selective or modified radical neck dissection, preserve CN XI when it is not directly invaded; radical sacrifice should be an oncologic decision for true nerve involvement rather than a routine price of nodal clearance. Anticipate anatomic variation around the internal jugular vein and SCM/posterior triangle instead of relying on a single landmark.",
        "Once CN XI is identified, preserve function as well as continuity: minimize circumferential skeletonization, traction, thermal spread, crush, and devascularizing dissection. When exposure requires mobilization, handle the surrounding tissue rather than repeatedly grasping the nerve. Handheld stimulation/monitoring can be useful in selected distorted, reoperative, bulky, or uncertain fields, but current evidence is heterogeneous and does not justify delaying safe visual dissection or treating monitoring as mandatory for every neck dissection.",
        "If CN XI is inadvertently transected and the ends are identifiable, stop further traction/thermal injury, define healthy proximal and distal nerve, and obtain timely reconstructive expertise. Favor immediate tension-free primary neurorrhaphy when a clean repair can be achieved; if a gap prevents a tension-free coaptation, use an appropriate interposition graft rather than stretching the nerve. If oncologic sacrifice is planned because the nerve is invaded, discuss the functional consequence and reconstructive/rehabilitative plan before division when circumstances allow.",
    ],
    "postop": [
        "Do not equate an anatomically preserved CN XI with normal function. New shoulder droop, scapular dyskinesis/winging, pain, weak shrug, or impaired abduction after neck dissection should trigger documented shoulder examination and early rehabilitation/physical therapy to preserve motion and reduce secondary pain/stiffness. Persistent severe deficit after suspected injury warrants focused electrodiagnostic and peripheral-nerve evaluation; delayed nerve repair or tendon-transfer strategies may be appropriate in selected chronic trapezius palsy rather than passive observation indefinitely.",
    ],
    "sources": ACCESSORY_NERVE_SOURCES,
    "marker": "neck_dissection_accessory_nerve_rescue_v277",
}]


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
    out = list(values or []); changed = False
    for text in reversed(additions or []):
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text); changed = True
    return out, changed


def _append_unique(values, additions):
    out = list(values or []); known = {str(x).strip().lower() for x in out}; changed = False
    for text in additions or []:
        key = str(text).strip().lower()
        if key and key not in known:
            out.append(text); known.add(key); changed = True
    return out, changed


def apply_or_neck_dissection_accessory_nerve_rescue_v277(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"]); continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op["sources"], c3 = _append_unique(op.get("sources"), target["sources"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2 or c3: changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
