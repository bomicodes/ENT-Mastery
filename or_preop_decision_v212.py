"""v21.2+ focused OR Tomorrow decision and anatomy enrichments.

Targets cases where the operative sequence is already procedure-specific but the
night-before plan should explicitly include findings that can change approach,
extent, counseling, or multidisciplinary preparation. Later reviewed OR enrichments
are chained here so runtime integration remains atomic with the existing planner hook.
"""

from or_preop_decision_v213 import apply_or_preop_decision_v213
from or_landmarks_v214 import apply_or_landmarks_v214
from or_otology_management_v217 import apply_or_otology_management_v217
from or_laryngology_management_v218 import apply_or_laryngology_management_v218
from or_pediatric_airway_management_v220 import apply_or_pediatric_airway_management_v220
from or_reconstruction_management_v225 import apply_or_reconstruction_management_v225

TARGETS = [
    {
        "slug": "superficial-parotidectomy",
        "title_terms": ("superficial parotid",),
        "text": "Define tumor location relative to the facial nerve/deep lobe from imaging and exam, document baseline facial function, and review cytology/pathology when available; facial weakness, fixation, skin involvement, nodal disease, or deep-lobe/parapharyngeal extension should change oncologic planning rather than being treated as a routine superficial parotidectomy.",
    },
    {
        "slug": "total-parotidectomy",
        "title_terms": ("total parotid",),
        "text": "Document baseline facial-nerve function and map tumor relationship to the nerve, deep lobe/parapharyngeal space, skull base and neck nodes; if nerve invasion is suspected, plan proximal/distal control, possible nerve sacrifice/reconstruction, and the required neck/reconstructive exposure before incision.",
    },
    {
        "slug": "submandibular-gland-excision",
        "title_terms": ("submandibular gland",),
        "text": "Clarify inflammatory/stone disease versus neoplasm before surgery and review imaging for floor-of-mouth/duct, mandibular and nodal relationships; document baseline tongue mobility/sensation when disease is extensive and plan oncologic neck management rather than simple gland excision when malignancy is suspected.",
    },
    {
        "slug": "sialendoscopy",
        "title_terms": ("sialendosc",),
        "text": "Review stone size, number and location and whether disease is intraductal versus intraparenchymal; anticipate that a large, impacted or hilar stone may require a combined approach rather than endoscopy alone, and account for lingual-nerve risk in posterior submandibular duct work.",
    },
    {
        "slug": "jugular-foramen-tumor",
        "title_terms": ("jugular foramen",),
        "text": "Before choosing the skull-base corridor, document CN IX-XII function, voice/swallow and aspiration status, hearing/facial function, and tumor relationship to the jugular bulb, carotid artery, dura and brainstem; for a hypervascular paraganglioma, review vascular imaging and multidisciplinary embolization/vascular-control strategy when appropriate.",
    },
    {
        "slug": "translabyrinthine-skull-base",
        "title_terms": ("translabyrinthine",),
        "text": "Confirm that the hearing-sacrificing translabyrinthine corridor matches the patient's preoperative hearing status and treatment goal; review facial-nerve function and MRI/CT anatomy, and plan abdominal/fascial graft or other CSF-leak closure resources before opening the temporal bone.",
    },
    {
        "slug": "retrosigmoid-skull-base",
        "title_terms": ("retrosigmoid",),
        "text": "Document serviceable hearing, facial function, vestibular symptoms and lower-cranial-nerve status before surgery; review tumor size/CPA-brainstem relationship and internal-auditory-canal extension so the team can define hearing-preservation intent, monitoring, drilling requirements and postoperative aspiration risk.",
    },
    {
        "slug": "middle-fossa-skull-base",
        "title_terms": ("middle fossa",),
        "text": "Confirm the indication for a hearing-preservation middle-fossa corridor from audiometry and lesion/IAC anatomy; review temporal-lobe, labyrinth/cochlea, geniculate/facial-nerve and petrous-carotid relationships and define facial/cochlear monitoring and CSF-leak closure strategy before surgery.",
    },
]


def _prepend_unique(values, text):
    out = list(values or [])
    marker = text[:56].lower()
    if any(marker in str(x).lower() for x in out):
        return out, False
    out.insert(0, text)
    return out, True


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        title = str((op or {}).get("title", "")).lower()
        if all(term in title for term in target["title_terms"]):
            return slug, op
    return None, None


def apply_or_preop_decision_v212(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], did_change = _prepend_unique(op.get("setup"), target["text"])
        op["preop_decision_v212"] = True
        resolved.append(slug)
        if did_change:
            changed.append(slug)
    v213 = apply_or_preop_decision_v213(registry)
    v214 = apply_or_landmarks_v214(registry)
    v217 = apply_or_otology_management_v217(registry)
    v218 = apply_or_laryngology_management_v218(registry)
    v220 = apply_or_pediatric_airway_management_v220(registry)
    v225 = apply_or_reconstruction_management_v225(registry)
    return {
        "changed": changed,
        "count": len(changed),
        "targets": len(TARGETS),
        "resolved": resolved,
        "missing": missing,
        "v213": v213,
        "v214": v214,
        "v217": v217,
        "v218": v218,
        "v220": v220,
        "v225": v225,
    }
