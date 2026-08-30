"""v31.7 — source-grounded neck dissection Concept Hub separation.

Separates oncologic neck-dissection selection/extent from complication recognition,
prevention, and rescue. The cards intentionally share surgical anatomy but answer
different resident/boards questions: WHAT neck operation is oncologically appropriate
versus WHAT went wrong after the operation and how to respond.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


NECK_DISSECTION_REBUILD_V317 = {
    "neck dissection": {
        "recognize": (
            "Use this card for ONCOLOGIC INDICATION, LATERALITY, AND EXTENT—not for memorizing a complication list. Start with the primary site, clinical N status, nodal levels involved or at risk, prior treatment, and whether surgery is elective, therapeutic, or salvage. A cN0 oral cavity neck, a lateralized surgically treated oropharynx, bulky multilevel cN+ disease, thyroid lateral-neck metastasis, cutaneous SCC to parotid/upper neck, and a post-CRT PET-positive neck require different operations. Do not treat 'neck dissection' as one fixed template."
        ),
        "localize": (
            "Localize disease by CERVICAL NODAL LEVEL and expected lymphatic drainage. Know the operative landmarks: level I around the submandibular/submental triangles; II from skull base to hyoid around the upper jugular chain with IIa/IIb divided by the spinal accessory nerve; III and IV along the middle/lower jugular chain; V in the posterior triangle; VI/VII in the central/superior mediastinal compartment when relevant. Determine ipsilateral versus bilateral risk from site, midline proximity/crossing, and nodal burden. Imaging should answer which levels are abnormal, whether nodes threaten carotid/IJV/cranial nerves, and whether disease extends outside a selective field."
        ),
        "workup": (
            "Define the primary and neck before choosing the dissection: complete head-and-neck examination/endoscopy as appropriate, contrast CT and/or MRI for nodal anatomy, FNA/core confirmation when it will change management, and distant staging when indicated by stage/biology. Classify cN0 versus cN+ and review prior RT/neck surgery. For oral cavity SCC treated surgically, ASCO supports elective ipsilateral dissection for most cT1-4 cN0 disease; a high-quality cN0 dissection includes Ia, Ib, II, and III, whereas therapeutic cN+ dissection generally extends through IV and can include V for multistation disease. For lateralized upfront-surgery oropharyngeal SCC, levels II-IV are the core ipsilateral field. These are disease-specific examples—not universal level recipes."
        ),
        "manage": (
            "Choose the least morbid operation that adequately treats nodal disease. SELECTIVE neck dissection removes defined lymphatic levels while preserving uninvolved nonlymphatic structures; MODIFIED RADICAL removes levels I-V while preserving one or more of spinal accessory nerve, internal jugular vein, and sternocleidomastoid; RADICAL removes levels I-V plus SAN, IJV, and SCM. Preserve SAN/IJV/SCM when oncologically safe; sacrifice an involved structure for clearance rather than to satisfy a historical label. Plan bilateral treatment only when contralateral risk warrants it. Pathologic nodal burden, extranodal extension, primary-tumor risk features, and dissection quality then feed the separate adjuvant-therapy decision."
        ),
        "operate": (
            "OPERATIVE PRINCIPLE: oncologic clearance with deliberate identification/preservation of structures not requiring sacrifice. Mark planned levels and boundaries; identify and protect marginal mandibular nerve, hypoglossal/vagus/phrenic nerves, sympathetic chain, brachial plexus, carotid system, IJV, and especially SAN as the field requires. Ligate lymphatics carefully low in level IV and inspect for chyle before closure. Do not chase an arbitrary node count at the expense of anatomy, but recognize surgical quality: ASCO uses at least 18 lymph nodes as a quality benchmark for oral cavity and surgically treated oropharyngeal dissections. Alter the field for gross disease rather than applying an elective selective template to a therapeutic neck."
        ),
        "teach": (
            "Chief/boards discriminator: NECK DISSECTION = WHY, WHICH SIDE, WHICH LEVELS, AND WHICH STRUCTURES MUST BE REMOVED FOR CANCER. Start with subsite + cN status + drainage + laterality, then select a selective/MRND/RND extent. Preserve SAN/IJV/SCM unless oncologically involved. Keep postoperative shoulder weakness, chyle, hematoma, neuropathy, wound failure, and vascular rescue in the companion 'Neck Dissection Complications' card."
        ),
        "tags": ["neck dissection", "cervical lymph nodes", "nodal levels", "selective neck dissection", "modified radical neck dissection", "radical neck dissection", "cN0 neck", "cN+ neck", "spinal accessory nerve"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cervical lymphatic anatomy, neck-dissection classification, indications, and technique",
            "K.J. Lee's Essential Otolaryngology, 12e — cervical nodal levels and neck-dissection principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — neck dissection anatomy, classification, and operative planning",
            "ASCO Clinical Practice Guideline: Management of the Neck in Squamous Cell Carcinoma of the Oral Cavity and Oropharynx (JCO 2019) — disease-specific indications, levels, laterality, and surgical-quality benchmarks",
            "Contemporary neck-dissection nomenclature consensus — radical, modified radical, and selective dissection terminology should communicate lymphatic levels and preserved nonlymphatic structures",
        ],
    },
    "neck dissection complications": {
        "recognize": (
            "Use this card for PREVENTION, EARLY RECOGNITION, AND RESCUE after neck dissection. Time matters. Immediate expanding neck swelling, respiratory distress, brisk drain output, hypotension, or neurologic change can signal hematoma/bleeding and demands urgent assessment. Milky drain output that rises after enteral fat suggests chyle leak. Shoulder droop, pain, weak abduction, and scapular dyskinesis suggest spinal accessory dysfunction even when the nerve was anatomically preserved. Hoarseness, tongue weakness, diaphragmatic dysfunction, Horner syndrome, lower-lip asymmetry, or brachial-plexus deficits localize other nerve injuries."
        ),
        "localize": (
            "Localize the complication to the structure at risk: SAN in level II/posterior triangle -> trapezius denervation/shoulder syndrome; marginal mandibular nerve near level Ib -> lower-lip asymmetry; hypoglossal -> ipsilateral tongue weakness; vagus/RLN -> dysphonia and possible aspiration; phrenic over anterior scalene -> hemidiaphragm elevation; sympathetic chain -> Horner syndrome; brachial plexus -> upper-extremity motor/sensory deficit. Low level IV dissection risks thoracic-duct/lymphatic injury—classically left, but right-sided lymphatic leaks occur. IJV injury/thrombosis, carotid exposure, pneumothorax, salivary contamination, and wound/flap compromise have different rescue priorities."
        ),
        "workup": (
            "Match testing to the suspected complication. Airway-threatening hematoma is a CLINICAL emergency—do not delay decompression/OR control for routine imaging. For suspected chyle, inspect drain character and trend volume in relation to feeding; triglyceride/chylomicron testing can help when appearance is equivocal. New dysphonia/aspiration warrants laryngeal examination; suspected phrenic injury can be evaluated with chest imaging/diaphragm motion; focal neurologic deficits require directed examination and selective imaging. Persistent shoulder dysfunction needs functional assessment rather than reassurance that 'the SAN was preserved.' Fever, salivary drainage, flap change, or exposed vessel should trigger targeted wound/infection and vascular assessment."
        ),
        "manage": (
            "Treat the complication, not a memorized drain number. Hematoma with airway compromise -> immediate airway/wound control and hemostasis. Chyle leak -> quantify output/trend, protect the wound, use a low-fat/MCT strategy or temporary enteral modification as appropriate, replace fluid/electrolyte/protein losses, and escalate selectively with interventional lymphatic procedures or operative control for persistent/high-output or clinically consequential leaks; contemporary reviews emphasize heterogeneous evidence and no single universal volume threshold. SAN-related shoulder dysfunction benefits from early physiotherapy/shoulder rehabilitation. Treat infection, fistula, IJV thrombosis, pneumothorax, nerve injury, or carotid exposure according to severity and involve reconstructive/vascular/interventional teams early when great-vessel protection is threatened."
        ),
        "operate": (
            "PREVENTION/RESCUE PRINCIPLE: know where morbidity is created. Preserve SAN vascularity and avoid unnecessary traction; protect marginal mandibular, hypoglossal, vagus, phrenic, sympathetic chain, and brachial plexus; control small lymphatics meticulously near the venous angle; raise intrathoracic/intra-abdominal pressure before closure when a low-neck lymphatic injury is suspected. Repair a recognized chyle leak intraoperatively. For postoperative persistent leak, re-exploration/ligation, local muscle coverage, or image-guided lymphatic embolization are options chosen by output, trajectory, patient physiology, wound/flap risk, and local expertise—not an automatic one-size-fits-all cutoff."
        ),
        "teach": (
            "Chief/boards discriminator: NECK DISSECTION COMPLICATIONS = WHAT STRUCTURE WAS INJURED, HOW URGENT IS IT, AND WHAT IS THE RESCUE? Airway-threatening hematoma is immediate; SAN dysfunction causes the classic shoulder syndrome and deserves rehabilitation; low-neck lymphatic injury causes chyle and requires trend-based nutritional/interventional escalation; cranial/cervical nerve findings localize by anatomy. Do not turn this card back into a selective-vs-radical classification lesson—that belongs to 'Neck Dissection.'"
        ),
        "tags": ["neck dissection complications", "spinal accessory nerve", "shoulder syndrome", "chyle leak", "thoracic duct", "hematoma", "cranial nerve injury", "internal jugular vein", "carotid exposure"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — neck-dissection complications, nerve injury, chyle leak, wound and vascular complications",
            "K.J. Lee's Essential Otolaryngology, 12e — neck-dissection morbidity and surgical anatomy",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — neck-dissection complications and postoperative management",
            "Ganesan et al., 2024 comprehensive review of chyle leak after head and neck surgery — individualized conservative, interventional, and operative escalation; no single evidence-based universal algorithm",
            "Harris et al., 2020 systematic review — physiotherapy benefits shoulder dysfunction after neck dissection in most included prospective studies",
        ],
    },
}


def apply_neck_dissection_rebuild_v317(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = NECK_DISSECTION_REBUILD_V317.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v317"] = True
            module["semantic_role_v317"] = (
                "oncologic indication, laterality, nodal-level selection, and dissection extent"
                if key == "neck dissection"
                else "post-neck-dissection complication localization, urgency, prevention, and rescue"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
