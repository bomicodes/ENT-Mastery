"""v27.8 neck-dissection vagus, hypoglossal, and phrenic nerve commitment/rescue layer.

Adds chief-level preservation-versus-sacrifice decisions, immediate transection bailout,
and deficit-specific postoperative rescue without making neuromonitoring a universal mandate.
"""

CRITICAL_NERVE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "American Head & Neck Society. Neck Dissection. Patient/clinical education resource; accessed 2026.",
    "Scharpf J et al. Critical Review and Consensus Statement for Neural Monitoring in Otolaryngologic Head, Neck, and Endocrine Surgery. Otolaryngol Head Neck Surg. 2022;166(6):1001-1020.",
    "Lee MF et al. The phrenic nerve; the forgotten nerve in head and neck surgery. ANZ J Surg. 2023;93:2494-2499.",
    "Hoshal SG, Solis RN, Bewley AF. Nerve grafts in head and neck reconstruction. Curr Opin Otolaryngol Head Neck Surg. 2020;28(5):346-351.",
    "Lemke A et al. The Role of Nerve Tension on Nerve Repair Success. J Hand Surg Glob Online. 2024.",
]

TARGETS = [{
    "slug": "neck-dissection",
    "title_terms": ("neck", "dissection"),
    "setup": [
        "Make vagus, hypoglossal, and phrenic nerve status explicit commitment points when the planned neck levels, bulky nodes, extranodal extension, prior treatment, or imaging place them at risk. Preserve an anatomically and functionally intact CN X, CN XII, and phrenic nerve when not directly invaded; if tumor truly requires nerve sacrifice, treat that as an oncologic commitment with the expected voice/swallow/respiratory consequence and rehabilitation or reconstructive plan discussed before irreversible division when circumstances allow.",
        "Protect function as well as continuity. Define the expected course before traction or thermal work in a distorted field: CN X within the carotid sheath, CN XII crossing the carotid region toward the tongue, and the phrenic nerve on the anterior scalene/deep posterior-triangle plane. Do not skeletonize, cauterize immediately against, or repeatedly traction a nerve merely to prove it has been seen. Neural stimulation/monitoring may be considered when anatomy is distorted or when the result could change the operation, but it does not replace visual anatomic dissection and is not a universal requirement for every neck dissection.",
        "If CN X, CN XII, or the phrenic nerve is inadvertently transected, stop further traction and thermal injury, identify and protect healthy proximal and distal ends, document the injured nerve, and obtain reconstructive expertise early. When a meaningful motor nerve repair is appropriate and both ends are usable, favor a clean tension-free primary neurorrhaphy; if a gap makes that impossible, use an appropriate graft/reconstructive strategy rather than stretching the nerve to force end-to-end coaptation. Planned oncologic sacrifice and accidental transection are different events and should not be normalized as equivalent.",
    ],
    "postop": [
        "Map a new deficit to the nerve instead of documenting generic 'cranial nerve weakness.' CN XII injury produces ipsilateral tongue weakness/deviation with dysarthria and oral-phase dysphagia; obtain a focused tongue examination and early speech/swallow assessment when function is clinically affected, with aspiration and nutrition planning for substantial or bilateral deficits.",
        "After suspected high vagal injury, new dysphonia plus palatal/pharyngeal weakness, impaired cough, dysphagia, or aspiration should trigger flexible laryngeal examination and swallow-focused assessment rather than assuming an isolated recurrent-laryngeal deficit. Escalate airway protection, pulmonary hygiene, nutrition, and laryngology/SLP rehabilitation to the physiologic deficit; bilateral vocal-fold immobility or progressive airway compromise is an airway emergency, not a routine postoperative voice problem.",
        "After lower-neck/posterior-triangle dissection, unexplained dyspnea, orthopnea, hypoxemia, or reduced ventilatory reserve should include phrenic neuropraxia/paralysis in the differential alongside pneumothorax, atelectasis, edema, and cardiopulmonary causes. Evaluate diaphragmatic position and motion with chest imaging and diaphragm ultrasound or fluoroscopic sniff testing when appropriate. Bilateral dysfunction or unilateral paralysis in a patient with limited pulmonary reserve deserves early respiratory support/escalation; persistent symptomatic paralysis should be referred for diaphragm-focused management rather than dismissed as expected neck-dissection morbidity.",
    ],
    "sources": CRITICAL_NERVE_SOURCES,
    "marker": "neck_dissection_critical_nerve_rescue_v278",
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


def apply_or_neck_dissection_critical_nerve_rescue_v278(registry):
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
