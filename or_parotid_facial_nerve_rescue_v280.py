"""v28.0 — parotid facial-nerve commitment, reconstruction, and eye-rescue layer.

Adds a focused chief-level decision layer to the existing superficial and total
parotidectomy OR Tomorrow cases. It does not replace the established landmark or
operative sequence; it protects the irreversible facial-nerve decision, unexpected
transection bailout, and immediate postoperative functional rescue.
"""

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — parotid neoplasms, facial-nerve anatomy, parotidectomy, and facial reconstruction principles",
    "K.J. Lee's Essential Otolaryngology, 12e — salivary-gland neoplasms, parotid surgery, and facial-nerve principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — Salivary Gland Malignancy, Salivary Gland Surgery, and Facial Reconstruction Techniques",
    "ASCO Clinical Practice Guideline: Management of Salivary Gland Malignancy, J Clin Oncol 2021 — preserve an intact facial nerve when a safe tumor-nerve plane exists; resect branches that are grossly encased/involved by confirmed malignancy or associated with impaired preoperative movement; avoid major nerve resection on an indeterminate diagnosis alone",
    "Saad et al., JPRAS Open 2026 systematic review — immediate/single-stage reconstruction after oncologic facial-nerve sacrifice; reported restoration of tone, oral competence, ocular protection, and selected dynamic function",
    "Fernandez-Diaz et al., J Plast Reconstr Aesthet Surg 2026 systematic review — immediate facial-nerve reconstruction after malignant parotidectomy; direct repair/grafting and nerve-transfer options matched to available stumps and defect",
]

TARGETS = (
    "superficial-parotidectomy",
    "total-parotidectomy",
)

SETUP = [
    "Make the FACIAL-NERVE COMMITMENT before irreversible division. Document baseline movement by division/functional region and reconcile examination, imaging, and tissue diagnosis. For a confirmed parotid malignancy with intact preoperative facial function, preserve the nerve when an oncologically sound dissection plane can be created. Facial-nerve resection is appropriate when a branch is grossly encased/involved by confirmed malignancy or preoperative weakness reflects tumor involvement; do not sacrifice a functioning nerve solely because an indeterminate frozen or needle diagnosis makes malignancy possible.",
    "If nerve sacrifice is reasonably anticipated, plan the reconstruction before cutting: identify whether a usable proximal stump and distal targets will remain, estimate the neural gap, and coordinate graft/nerve-transfer/static or dynamic reanimation and ocular-protection needs with the oncologic and reconstructive team. Anticipated postoperative radiation is not by itself a reason to abandon immediate repair/reanimation when otherwise appropriate.",
]

STEPS = [
    "When tumor approaches the facial nerve, slow the dissection and establish whether a true separable plane exists before converting adherence into intentional nerve sacrifice. Preserve an uninvolved branch without unnecessary circumferential skeletonization, traction, crush, or thermal injury. Facial-nerve monitoring can assist identification and functional feedback, especially in distorted anatomy, but it does not replace direct anatomic dissection or justify dividing a visually uncertain structure.",
    "If the nerve is unexpectedly transected, STOP further traction and energy injury, identify and protect healthy proximal and distal ends, and define the actual defect before continuing the specimen dissection. Favor tension-free primary neurorrhaphy when healthy ends approximate without stretch; use an interposition cable graft when a gap prevents tension-free coaptation. If the proximal facial-nerve stump is unavailable or the distal targets/resection pattern make grafting inadequate, transition deliberately to an appropriate nerve-transfer and/or static/dynamic facial-reanimation plan rather than leaving the deficit unaddressed by default.",
]

POSTOP = [
    "Document facial function immediately after surgery by region, including forehead movement, eye closure/corneal protection, midface, oral commissure excursion, and oral competence; do not record only 'facial nerve intact.' Unexpected weakness after an anatomically preserved nerve warrants serial focused examination and review of the intraoperative event/monitoring rather than an automatic assumption of transection, because traction, edema, ischemia, and neurapraxia can produce early dysfunction.",
    "Incomplete eye closure is an OCULAR-SURFACE PROBLEM now, not a later cosmetic issue: institute lubrication and nighttime closure/moisture protection immediately, escalate to ophthalmology when exposure symptoms, corneal findings, poor Bell phenomenon, impaired corneal sensation, or severe paralysis increases risk, and use temporary/procedural eyelid protection when conservative measures are insufficient. After planned sacrifice or a recognized major injury, arrange early facial-nerve/reanimation follow-up so eye protection, oral competence, reinnervation strategy, and adjuvant oncologic therapy proceed in parallel.",
]


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:80].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        if text not in out:
            out.append(text)
            changed = True
    return out, changed


def apply_or_parotid_facial_nerve_rescue_v280(registry):
    changed, missing = [], []
    for slug in TARGETS:
        op = (registry or {}).get(slug)
        if not op:
            missing.append(slug)
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), SETUP)
        op["steps"], c2 = _prepend_unique(op.get("steps"), STEPS)
        op["postop"], c3 = _prepend_unique(op.get("postop"), POSTOP)
        op["sources"], c4 = _append_unique(op.get("sources"), SOURCES)
        op["parotid_facial_nerve_rescue_v280"] = True
        if c1 or c2 or c3 or c4:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "missing": missing}
