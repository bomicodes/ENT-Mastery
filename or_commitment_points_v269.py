"""v26.9 chief-level commitment-point and bailout layer for OR Tomorrow.

Adds explicit stop/convert/stage logic where an operation can become unsafe or
oncologically unsound despite an otherwise correct sequence. Existing anatomy,
steps, and complication content remain authoritative and are only supplemented.
"""

TARGETS = [
    {
        "slug": "stapedotomy",
        "title_terms": ("staped",),
        "postop": [],
        "setup": [
            "Know the bailout before entering the vestibule: if the footplate becomes grossly mobile/floating, repeated manipulation risks inner-ear injury—stop escalating force, stabilize/seal the oval-window interface as appropriate, and prioritize hearing preservation over completing the planned prosthesis reconstruction. Likewise, an unexpected high-flow perilymph/CSF gusher changes the operation from routine fenestration to controlled sealing and leak management; do not keep enlarging or repeatedly instrumenting the vestibule simply to finish the original plan.",
            "If intraoperative findings are inconsistent with stapes fixation—for example an unexpectedly mobile stapes or another ossicular abnormality that better explains the conductive loss—reassess the diagnosis before creating a fenestra. Completing a stapedotomy despite loss of the original indication is not a neutral choice.",
        ],
    },
    {
        "slug": "cochlear-implant",
        "title_terms": ("cochlear", "implant"),
        "setup": [
            "Make electrode resistance a stop-and-reassess point, not a cue to push harder. If the array does not advance with expected low resistance, withdraw enough to inspect the round-window/cochleostomy exposure and insertion vector, confirm that the opening is adequate and the electrode has not folded or entered a false passage, and redirect or revise access under direct visualization. Repeated force risks basilar-membrane/osseous-spiral-lamina trauma, scalar translocation, tip fold-over and loss of residual hearing; an incomplete but atraumatic insertion is preferable to blindly forcing the array to the planned depth.",
            "Unexpected brisk clear-fluid egress or anatomy suggesting a cochlear malformation changes the operation to controlled CSF/perilymph-leak management. Maintain control of the access site, insert only as safely permitted by the anatomy, obtain a secure soft-tissue seal around the electrode, and reassess the planned insertion rather than repeatedly enlarging or instrumenting the cochlea. If the facial nerve or another critical structure makes the usual facial-recess/round-window trajectory unsafe, widen exposure or choose a deliberate alternative access strategy rather than working blindly around the nerve.",
            "Before closing, treat abnormal telemetry or concern for tip fold-over/malposition as a reason to investigate while the field is still accessible. Recheck electrode position and device integrity with the available intraoperative tools and revise when a correctable placement problem is demonstrated; do not close simply because the array is physically inside the cochlea.",
        ],
        "postop": [],
    },
    {
        "slug": "cholesteatoma",
        "title_terms": ("cholesteat",),
        "setup": [
            "Let disease clearance determine the final mastoid strategy. If epitympanic, retrofacial, sinus-tympani, anterior-epitympanic or other hidden disease cannot be safely and reliably cleared with the canal wall intact, convert the plan rather than leaving known keratinizing disease merely to preserve canal-wall anatomy; canal-wall-down or staged disease-control strategies are legitimate bailouts when complete clearance and dependable surveillance cannot otherwise be achieved.",
            "A labyrinthine fistula, dehiscent/exposed facial nerve, tegmen/dural defect or major venous-sinus exposure changes the dissection from routine matrix removal to structure-preservation choreography. Stop blind traction and powered instrumentation at the danger zone, define the involved structure, work under direct magnified visualization, and modify the extent/timing of matrix removal and reconstruction to protect hearing, facial function, dura/CSF containment and venous control. The goal remains safe disease eradication, not mechanically stripping matrix from a critical structure at any cost.",
        ],
        "postop": [],
    },
    {
        "slug": "parotidectomy",
        "title_terms": ("parotidectomy",),
        "setup": [
            "Make the facial-nerve commitment point explicit before dissection: a functioning nerve that is not grossly invaded should be preserved whenever oncologically feasible, whereas proven/gross malignant invasion may require planned segmental sacrifice with immediate reconstruction when technically possible. Dense adherence alone is not a reason for casual nerve sacrifice; if the oncologic extent was not anticipated, pause and reassess margins, pathology, reconstruction options and whether the planned operation should be extended or staged.",
        ],
        "postop": [],
    },
    {
        "slug": "parotid-total",
        "title_terms": ("total", "parotid"),
        "setup": [
            "Before committing to facial-nerve sacrifice in total parotidectomy, distinguish gross malignant invasion from difficult but separable adherence. Preserve an uninvolved functioning nerve when oncologically sound; when invasion requires sacrifice, define proximal/distal viable ends and reconstructive options before completing the defect so nerve grafting or reanimation is not an afterthought.",
        ],
        "postop": [],
    },
    {
        "slug": "transoral-laser-laryngeal-cancer",
        "title_terms": ("transoral", "laser", "laryngeal"),
        "setup": [
            "Treat inadequate exposure or inability to obtain a meaningful deep margin as a conversion/abort point, not an invitation to make a piecemeal oncologically compromised resection. Reassess whether a wider endoscopic resection, open partial/total laryngeal approach, or nonsurgical oncologic strategy is required; the operation should change when the margin goal cannot be met safely through the planned corridor.",
        ],
        "postop": [],
    },
    {
        "slug": "tors",
        "title_terms": ("tors",),
        "setup": [
            "If exposure, vascular proximity, depth of invasion or inability to orient an adequate deep margin makes the robotic corridor oncologically or hemostatically unsafe, undock and change the plan rather than forcing completion transorally. Conversion can mean transcervical vascular control, an alternate open approach, staged diagnostic resection, or a nonsurgical oncologic strategy depending on the disease; preserving the original approach is never more important than safe margin and hemorrhage control.",
        ],
        "postop": [],
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


def apply_or_commitment_points_v269(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["commitment_points_v269"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
