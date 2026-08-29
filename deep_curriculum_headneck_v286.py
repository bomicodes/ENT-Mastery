"""v28.6 — source-grounded neck dissection Concept Hub rebuild.

Separates oncologic neck-dissection planning/technique from complication recognition and
rescue so the two canonical cards stop repeating the same anatomy and become a true
resident-to-chief progression.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


NECK_DISSECTION_REBUILD_V286 = {
    "neck dissection": {
        "recognize": (
            "Recognize NECK DISSECTION as regional oncologic surgery whose indication and extent are determined by the PRIMARY SITE, clinical nodal status, expected lymphatic drainage, prior treatment, and whether the neck is being treated electively or therapeutically. Do not reduce the operation to memorizing levels I-V. First ask: is the neck cN0 or cN+, which nodal basins are at meaningful risk, is disease unilateral or bilateral, and is surgery part of primary treatment or salvage? A clinically negative neck can still harbor occult metastasis, whereas a bulky node with extranodal extension or fixation may require a different operative and adjuvant strategy than a small mobile node."
        ),
        "localize": (
            "Localize the operation using LYMPH-NODE LEVELS and the nonlymphatic structures that define its classification. Level I is submental/submandibular (IA/IB); II-IV follow the upper, middle, and lower internal-jugular chain; V is the posterior triangle, with additional retropharyngeal, parotid, facial, central-compartment, and superior-mediastinal basins used when the primary-site drainage demands them. In classic terminology, RADICAL neck dissection removes levels I-V plus sternocleidomastoid muscle, internal jugular vein, and spinal accessory nerve; MODIFIED RADICAL preserves one or more of those nonlymphatic structures; SELECTIVE neck dissection preserves one or more nodal levels that a radical dissection would remove; EXTENDED dissection removes additional lymphatic groups and/or nonlymphatic structures. Describe what levels and structures were actually removed rather than relying on an ambiguous eponym."
        ),
        "workup": (
            "Before choosing a neck dissection, establish the mucosal/skin/salivary/thyroid primary and histology, perform complete head-and-neck examination, and define cervical disease with high-quality contrast imaging; ultrasound/FNA or core biopsy is useful when a node needs tissue confirmation, and PET/CT is added when staging or an occult primary warrants it. Translate imaging into a surgical map: involved levels, size/number of nodes, radiographic extranodal extension, carotid/IJV/SCM/CN XI or deep-muscle involvement, contralateral disease, and prior radiation/surgery. The planned field should follow disease biology rather than a generic template. For surgically treated oral cavity SCC, ASCO recommends ipsilateral levels IA, IB, II, III for the cN0 elective neck and IA, IB, IIA, IIB, III, IV for a therapeutic cN+ selective dissection; lateralized oropharyngeal cancers treated with upfront surgery generally require ipsilateral levels II-IV."
        ),
        "manage": (
            "Choose the LEAST MORBID ONCOLOGICALLY ADEQUATE neck treatment. Elective treatment is justified when occult nodal risk is high enough that observation is unsafe or unreliable; therapeutic dissection addresses known nodal disease. For oral cavity SCC, a high-quality elective or therapeutic dissection should provide an adequate pathologic nodal yield—ASCO uses at least 18 nodes as a quality benchmark. Consider contralateral treatment when the primary approaches/crosses midline or has bilateral drainage, and integrate the operation with expected postoperative radiation or chemoradiation rather than viewing surgery in isolation. In a previously irradiated neck, after definitive chemoradiation, do not perform a routine planned neck dissection when modern response assessment shows complete nodal response; reserve salvage surgery for persistent or progressive disease according to multidisciplinary evaluation."
        ),
        "operate": (
            "Operate by preserving normal function WITHOUT compromising clearance. Raise appropriately vascularized flaps, identify the boundaries of the selected nodal levels, and remove the fibrofatty lymphatic packet in a controlled fashion while deliberately identifying or protecting key structures: marginal mandibular nerve and facial vessels around level IB; hypoglossal and lingual nerves; carotid artery/vagus/IJV; spinal accessory nerve as it crosses level II and enters the posterior triangle; phrenic nerve and brachial plexus deep to level IV/V; and the thoracic duct at the low LEFT neck. Preserve CN XI, IJV, and SCM when not grossly involved; sacrifice is an oncologic decision, not a requirement of every comprehensive dissection. For transoral oropharyngeal surgery performed with neck dissection, ASCO recommends ligating at-risk feeding vessels to reduce severity/incidence of postoperative hemorrhage. Before closure, obtain hemostasis, inspect the low neck for lymphatic leakage when relevant, and document the exact levels and structures removed/preserved."
        ),
        "teach": (
            "Chief/boards framework: PLAN THE NECK FROM THE PRIMARY AND NODAL BIOLOGY, then name the operation from what you actually removed. Radical = I-V + SCM + IJV + CN XI; modified radical preserves at least one of those nonlymphatic structures; selective preserves one or more nodal levels; extended removes more than the radical template. Oral cavity cN0 surgery classically includes IA-III, oral cavity cN+ IA-IV, and lateralized surgically treated oropharynx II-IV. Adequacy is not simply incision size: correct basins, oncologic clearance, nodal yield, and preservation of uninvolved critical structures are the quality targets. Keep postoperative deficits and rescue algorithms in the separate NECK DISSECTION COMPLICATIONS card—this card is about deciding and executing the cancer operation correctly."
        ),
        "tags": [
            "neck dissection", "cervical lymph node levels", "radical neck dissection",
            "modified radical neck dissection", "selective neck dissection", "oral cavity SCC",
            "oropharyngeal SCC", "spinal accessory nerve", "18 lymph nodes", "neck management"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cervical lymphatic anatomy, neck-dissection classification, indications, surgical technique, and oncologic principles",
            "K.J. Lee's Essential Otolaryngology, 12e — neck levels, patterns of spread, neck-dissection terminology, and operative anatomy",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — neck-dissection levels, classification, indications, and surgical landmarks",
            "Robbins et al., Arch Otolaryngol Head Neck Surg 2008 — American Head and Neck Society consensus terminology/classification for neck dissection",
            "ASCO Clinical Practice Guideline: Management of the Neck in Squamous Cell Carcinoma of the Oral Cavity and Oropharynx, J Clin Oncol 2019 — evidence-based elective/therapeutic levels, nodal-yield quality benchmark, bilateral treatment, and post-CRT neck management",
        ],
    },
    "neck dissection complications": {
        "recognize": (
            "Recognize NECK DISSECTION COMPLICATIONS by TIME COURSE and THREAT, not by repeating the operative anatomy. In the first hours, an expanding hematoma, airway compromise, brisk drain bleeding, neurologic change, or major vascular event is an emergency. Over the next days, look for chyle leak, wound infection/dehiscence, salivary/pharyngeal fistula, flap compromise, venous thrombosis, and cranial/cervical nerve deficits. Later morbidity is often functional: shoulder pain/weakness despite an anatomically preserved spinal accessory nerve, cervical fibrosis, sensory disturbance, lymphedema, and restricted range of motion. The first triage question is whether the problem threatens AIRWAY, VASCULAR CONTROL, FLAP/PHARYNGEAL INTEGRITY, or long-term function."
        ),
        "localize": (
            "Localize the complication from the DEFICIT. Shoulder droop, weak abduction, scapular winging, and trapezius atrophy point to CN XI traction/injury, especially after level IIB or V work; marginal mandibular injury causes lower-lip asymmetry; hypoglossal injury causes ipsilateral tongue weakness/deviation; vagal injury may cause vocal-fold paralysis, dysphagia, or aspiration; sympathetic-chain injury produces Horner syndrome; phrenic injury elevates the hemidiaphragm; brachial-plexus injury produces upper-extremity motor/sensory deficits. Milky drain output that increases after enteral fat strongly suggests a CHYLE leak, classically after low LEFT level-IV dissection where the thoracic duct terminates near the venous angle, although right-sided lymphatic leaks can occur. A tense neck with respiratory symptoms is a hematoma until proven otherwise."
        ),
        "workup": (
            "Work up the suspected complication with the minimum test that answers the urgent question. A rapidly expanding postoperative neck hematoma with airway symptoms is a CLINICAL diagnosis—do not delay decompression for CT. New dysphonia, aspiration, or vagal concern warrants flexible laryngoscopy. For suspected chyle leak, inspect drain character and volume/trend and confirm uncertain cases with drain triglycerides and/or chylomicrons; monitor electrolytes, albumin/nutritional status, and volume depletion when output is significant. Duplex/CT venography can evaluate suspected IJV thrombosis when the result will change care. Persistent focal weakness should be documented with a focused cranial-nerve and shoulder examination; EMG is a later localization/prognostic tool rather than an immediate postoperative requirement. In irradiated or contaminated wounds, maintain a low threshold to evaluate for fistula and threatened carotid exposure."
        ),
        "manage": (
            "Match initial management to severity. For a stable LOW-VOLUME chyle leak, maintain drainage, reduce long-chain dietary fat using a low-fat/medium-chain-triglyceride strategy when oral/enteral feeding is appropriate, replace fluid/electrolyte/protein losses, and reassess output daily; octreotide is frequently used as an adjunct, but evidence and dosing protocols vary. Higher-volume or persistent leaks are less likely to resolve with diet alone and should trigger earlier escalation rather than prolonged nutritional depletion. Shoulder dysfunction benefits from EARLY directed physiotherapy/range-of-motion and strengthening even when CN XI was anatomically preserved, because traction neurapraxia can still produce clinically important weakness. Treat infection, fistula, thrombosis, and neuropathic pain according to the involved structure rather than with a generic 'post-neck-dissection' pathway."
        ),
        "operate": (
            "Return to the OR immediately for an expanding hematoma with airway/vascular threat or uncontrolled surgical bleeding; open the neck promptly if needed to relieve compression while securing the airway and definitive hemostasis. For persistent/high-output chyle leak, escalate early to definitive control—options include neck re-exploration with ligation of the leaking duct/lymphatic tissue, thoracic-duct embolization, or thoracoscopic thoracic-duct ligation depending on output, timing, prior surgery, free-flap/wound status, and local expertise. When re-exploring the low neck, avoid blind clamping near the phrenic nerve, brachial plexus, subclavian vessels, and venous angle. Major carotid exposure/blowout risk, pharyngocutaneous fistula, or flap-threatening infection requires multidisciplinary reconstructive/vascular planning rather than simple bedside wound care."
        ),
        "teach": (
            "Chief/boards framework: COMPLICATIONS = LOCALIZE THE INJURED STRUCTURE + DECIDE WHETHER IT IS AN EMERGENCY. Hematoma with airway threat: decompress/control now, not CT first. Milky high-output drain after low-left neck dissection: think thoracic-duct chyle leak; low-output disease may close with drainage/nutritional measures, while persistent or high-output leakage deserves earlier procedural control. CN XI morbidity can occur despite nerve preservation, especially after IIB/V manipulation, so shoulder surveillance and early rehabilitation matter. This card intentionally does NOT reteach which nodal levels belong in each cancer operation—the companion NECK DISSECTION card owns oncologic planning; this card owns recognition, localization, and rescue of morbidity."
        ),
        "tags": [
            "neck dissection complications", "postoperative hematoma", "chyle leak", "thoracic duct",
            "spinal accessory nerve", "shoulder syndrome", "vagal injury", "hypoglossal nerve",
            "phrenic nerve", "Horner syndrome", "carotid blowout", "physiotherapy"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — neck-dissection complications, cranial/cervical nerve morbidity, chyle leak, hematoma, and wound complications",
            "K.J. Lee's Essential Otolaryngology, 12e — postoperative neck-dissection complications and anatomic localization",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — practical complication recognition and management after neck dissection",
            "Harris et al., J Laryngol Otol 2020 systematic review — evidence supporting postoperative physiotherapy for shoulder dysfunction after neck dissection",
            "Nutritional management of chyle leak after head and neck surgery, systematic review, 2023 — output-aware conservative nutrition and limits of evidence",
            "Improving the management of cervical chyle leak following neck dissection, J Laryngol Otol 2025 — volume-based escalation including thoracic duct ligation/embolization for persistent moderate/high-output leaks",
        ],
    },
}


def apply_headneck_neck_dissection_rebuild_v286(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = NECK_DISSECTION_REBUILD_V286.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v286"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
