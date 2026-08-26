"""v21.2 focused preoperative decision points for OR Tomorrow.

Targets cases where the operative sequence is already procedure-specific but the
night-before plan should explicitly include findings that can change approach,
extent, counseling, or multidisciplinary preparation.
"""

TARGETED_SETUP = {
    "superficial-parotidectomy": [
        "Define tumor location relative to the facial nerve/deep lobe from imaging and exam, document baseline facial function, and review cytology/pathology when available; facial weakness, fixation, skin involvement, nodal disease, or deep-lobe/parapharyngeal extension should change oncologic planning rather than being treated as a routine superficial parotidectomy."
    ],
    "total-parotidectomy": [
        "Document baseline facial-nerve function and map tumor relationship to the nerve, deep lobe/parapharyngeal space, skull base and neck nodes; if nerve invasion is suspected, plan proximal/distal control, possible nerve sacrifice/reconstruction, and the required neck/reconstructive exposure before incision."
    ],
    "submandibular-gland-excision": [
        "Clarify inflammatory/stone disease versus neoplasm before surgery and review imaging for floor-of-mouth/duct, mandibular and nodal relationships; document baseline tongue mobility/sensation when disease is extensive and plan oncologic neck management rather than simple gland excision when malignancy is suspected."
    ],
    "sialendoscopy": [
        "Review stone size, number and location and whether disease is intraductal versus intraparenchymal; anticipate that a large, impacted or hilar stone may require a combined approach rather than endoscopy alone, and account for lingual-nerve risk in posterior submandibular duct work."
    ],
    "jugular-foramen-tumor": [
        "Before choosing the skull-base corridor, document CN IX-XII function, voice/swallow and aspiration status, hearing/facial function, and tumor relationship to the jugular bulb, carotid artery, dura and brainstem; for a hypervascular paraganglioma, review vascular imaging and multidisciplinary embolization/vascular-control strategy when appropriate."
    ],
    "translabyrinthine-skull-base": [
        "Confirm that the hearing-sacrificing translabyrinthine corridor matches the patient's preoperative hearing status and treatment goal; review facial-nerve function and MRI/CT anatomy, and plan abdominal/fascial graft or other CSF-leak closure resources before opening the temporal bone."
    ],
    "retrosigmoid-skull-base": [
        "Document serviceable hearing, facial function, vestibular symptoms and lower-cranial-nerve status before surgery; review tumor size/CPA-brainstem relationship and internal-auditory-canal extension so the team can define hearing-preservation intent, monitoring, drilling requirements and postoperative aspiration risk."
    ],
    "middle-fossa-skull-base": [
        "Confirm the indication for a hearing-preservation middle-fossa corridor from audiometry and lesion/IAC anatomy; review temporal-lobe, labyrinth/cochlea, geniculate/facial-nerve and petrous-carotid relationships and define facial/cochlear monitoring and CSF-leak closure strategy before surgery."
    ],
}


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:56].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_preop_decision_v212(registry):
    changed, missing = [], []
    for slug, additions in TARGETED_SETUP.items():
        op = (registry or {}).get(slug)
        if not op:
            missing.append(slug)
            continue
        op["setup"], did_change = _prepend_unique(op.get("setup"), additions)
        op["preop_decision_v212"] = True
        if did_change:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETED_SETUP), "missing": missing}
