"""v21.7 otology-specific OR Tomorrow planning and postoperative priorities.

Adds high-yield decision points that are not captured by a generic otology profile:
hearing-based candidacy, disease-control versus reconstruction sequencing, and
postoperative findings that should trigger urgent otologic reassessment.
"""

TARGETS = [
    {
        "slug": "stapedotomy",
        "title_terms": ("staped",),
        "setup": [
            "Review the current audiogram before stapes surgery: confirm a conductive or mixed loss compatible with stapes fixation, quantify the air-bone gap and bone-conduction reserve, and review speech discrimination and the contralateral ear. Atypical findings, substantial sensorineural asymmetry, congenital/anatomic concern, or revision surgery should lower the threshold for temporal-bone imaging and reconsideration of diagnosis/approach rather than routine primary stapedotomy.",
            "Explicitly counsel regarding the small but consequential risk of postoperative sensorineural hearing loss/deafness, vertigo, taste disturbance, tympanic-membrane injury and facial-nerve injury; hearing in the opposite ear materially affects risk tolerance and operative planning.",
        ],
        "postop": [
            "After stapes surgery, expected transient disequilibrium should improve rather than progress; sudden hearing deterioration, severe or worsening vertigo, new facial weakness, persistent otorrhea/clear drainage, or marked disequilibrium with pressure-induced symptoms warrants urgent otologic reassessment for inner-ear injury, prosthesis problem or perilymphatic leak rather than routine reassurance.",
            "Protect the reconstruction during early healing with the surgeon's dry-ear and pressure precautions; avoid forceful Valsalva/nose blowing or other activities that create abrupt middle-ear pressure until cleared, and obtain the planned postoperative audiogram after healing rather than judging success from immediate subjective hearing alone.",
        ],
    },
    {
        "slug": "tympanoplasty",
        "title_terms": ("tympanoplast",),
        "setup": [
            "Review preoperative audiometry, perforation size/location, middle-ear status, contralateral ear and Eustachian-tube/ventilation context; active infection, cholesteatoma, ossicular disease or poor middle-ear aeration changes the operative goal and may require disease eradication or staged reconstruction rather than a simple membrane repair.",
        ],
        "postop": [
            "Postoperatively, protect the graft from water and abrupt pressure change according to the surgeon's protocol; worsening otalgia, purulent drainage, fever, new facial weakness, severe vertigo or sudden hearing decline is not routine packing discomfort and warrants prompt evaluation.",
        ],
    },
    {
        "slug": "ossiculoplasty",
        "title_terms": ("ossiculoplast",),
        "setup": [
            "Before ossiculoplasty, correlate the conductive deficit with tympanic-membrane status, middle-ear aeration and the expected malleus/incus/stapes anatomy; define whether the stapes superstructure is present and mobile because this determines partial versus total reconstruction. In an infected, poorly aerated or cholesteatomatous ear, prioritize durable disease control and consider staged reconstruction rather than forcing a definitive prosthesis into an unfavorable middle ear.",
        ],
        "postop": [
            "New or progressive vertigo, sudden sensorineural hearing change, facial weakness or severe pain/drainage after ossiculoplasty warrants urgent evaluation for inner-ear injury, infection or prosthesis-related complication; persistent conductive loss later should prompt assessment for displacement, extrusion, scar fixation or recurrent middle-ear disease rather than assuming the prosthesis simply 'did not work.'",
        ],
    },
    {
        "slug": "cholesteatoma",
        "title_terms": ("cholesteat",),
        "setup": [
            "Review the current audiogram and facial-nerve function and map disease extent on temporal-bone imaging when indicated, specifically looking for ossicular erosion, tegmen/dural exposure, labyrinthine fistula, facial-canal erosion and mastoid anatomy. Decide deliberately between canal-wall-up and canal-wall-down strategy based on disease extent, anatomy, follow-up reliability and ability to achieve complete clearance rather than treating the choice as a technical preference alone.",
            "Define the surveillance strategy before surgery: when canal-wall-up or hidden-recess disease leaves meaningful residual risk, plan second-look surgery and/or non-echo-planar diffusion-weighted MRI according to the operative strategy and local protocol.",
        ],
        "postop": [
            "After cholesteatoma surgery, document facial function and vestibular/hearing symptoms early; new facial weakness, severe vertigo/nystagmus, sudden sensorineural hearing loss, CSF-like drainage, meningitic symptoms or significant wound infection requires urgent otologic reassessment.",
            "Long-term management is part of the operation: canal-wall-down cavities require reliable microscopic cleaning/water precautions as appropriate, while canal-wall-up cases require planned surveillance for residual or recurrent cholesteatoma rather than symptom-driven follow-up alone.",
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


def apply_or_otology_management_v217(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        did_change = False
        op["setup"], c = _prepend_unique(op.get("setup"), target["setup"])
        did_change = did_change or c
        op["postop"], c = _prepend_unique(op.get("postop"), target["postop"])
        did_change = did_change or c
        op["otology_management_v217"] = True
        resolved.append(slug)
        if did_change:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
