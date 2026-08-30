"""v30.5 — source-grounded neck-dissection Concept Hub separation.

Keeps two clinically related cards deliberately nonredundant:
* Neck Dissection owns oncologic indication, extent, nodal levels, laterality, and quality.
* Neck Dissection Complications owns prevention, recognition, localization, and rescue of morbidity.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


NECK_DISSECTION_V305 = {
    "neck dissection": {
        "recognize": "Recognize neck dissection as REGIONAL ONCOLOGIC THERAPY, not a generic neck operation. Start with the primary site, cT/cN status, HPV/EBV context when relevant, imaging, prior treatment, and probability/distribution of occult or gross nodal disease. Decide whether the neck needs elective treatment, therapeutic treatment, salvage after radiation/chemoradiation, or observation. A clinically N0 neck can still require treatment when occult-metastatic risk is substantial; conversely, a previously irradiated neck with a complete appropriate post-treatment response should not undergo routine planned dissection merely because it was node-positive before therapy.",
        "localize": "Localize disease by cervical nodal LEVEL and expected drainage pattern before choosing the operation. Know Ia/Ib, IIa/IIb, III, IV, Va/Vb and the central/retropharyngeal basins; map gross ENE, fixation, carotid/skull-base involvement, and relation to CN XI, IJV and SCM. Primary-site biology determines elective levels: oral cavity commonly emphasizes I-III (with IV added for therapeutic node-positive disease), while lateralized oropharyngeal disease commonly emphasizes II-IV. Midline approach, contralateral nodal risk, multistation disease and unusual posterior/scalp drainage can expand laterality or levels.",
        "workup": "Stage the primary and neck with high-quality cross-sectional imaging and tissue diagnosis appropriate to the presentation; use PET/CT in the settings where it changes staging or post-treatment response assessment. For a surgical plan, explicitly document cN0 versus cN+, laterality, suspicious levels, radiographic ENE, prior radiation/surgery, and whether major nonlymphatic structures are invaded. Do not choose selective versus comprehensive dissection from node size alone. After definitive chemoradiation, response-directed imaging at an appropriate interval is central to deciding whether salvage neck dissection is necessary.",
        "manage": "Choose the smallest operation that remains ONCOLOGICALLY COMPLETE. Selective neck dissection removes only nodal groups at meaningful risk while preserving uninvolved nonlymphatic structures; modified radical dissection is comprehensive while preserving one or more of CN XI/IJV/SCM; radical neck dissection removes levels I-V with CN XI, IJV and SCM and is now reserved for disease that truly requires sacrifice. Treat the contralateral neck when primary-site/midline or nodal features create meaningful contralateral risk. Pathology then informs adjuvant therapy through nodal burden, ENE and other high-risk features.",
        "operate": "Operate by oncologic boundaries, not by memorized labels alone. Design exposure that permits en bloc clearance of intended levels, identify and preserve CN XI, IJV, SCM and other nerves/vessels unless directly involved, and orient specimens by level for pathologic accountability. Avoid unnecessary IIb, V, or nonlymphatic-structure dissection when oncologically safe because morbidity rises with extra manipulation. For oral cavity and oropharyngeal SCC, a high-quality dissection includes the guideline-specified levels and adequate nodal yield; ASCO uses at least 18 lymph nodes as a quality benchmark in the relevant surgical scenarios. If a structure is grossly invaded, oncologic clearance can appropriately supersede preservation.",
        "teach": "Chief/boards framework: PRIMARY SITE + NODAL STATUS + EXPECTED DRAINAGE -> LATERALITY + LEVELS + STRUCTURES THAT CAN BE PRESERVED. Know the difference between selective, modified radical and radical neck dissection, but answer the clinical question by disease distribution. For oral cavity SCC, ASCO recommends ipsilateral elective dissection for cT2-4 cN0 and generally for cT1 cN0, with levels Ia-Ib-II-III for elective surgery and Ia-Ib-IIa-IIb-III-IV for a therapeutic selective dissection; lateralized oropharyngeal upfront surgery commonly uses II-IV. This card ends once the correct oncologic operation is chosen and performed; postoperative nerve, lymphatic, vascular and wound rescue belongs to the complications card.",
        "tags": ["neck dissection", "selective neck dissection", "modified radical neck dissection", "radical neck dissection", "cervical nodal levels", "occult metastasis", "ENE", "neck management", "ASCO"],
        "source_basis": ["Cummings Otolaryngology—Head and Neck Surgery, 7e — cervical metastasis, neck dissection classification, indications and operative anatomy", "K.J. Lee's Essential Otolaryngology, 12e — cervical lymphatics and neck dissection", "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Cancer of the Neck / Neck Dissection", "ASCO Clinical Practice Guideline: Management of the Neck in Squamous Cell Carcinoma of the Oral Cavity and Oropharynx (JCO 2019) — indications, levels, laterality, nodal-yield quality metrics and post-CRT response-directed neck management"],
    },
    "neck dissection complications": {
        "recognize": "Recognize complication patterns EARLY and tie each to the structure at risk. Shoulder pain, droop and weak abduction suggest spinal accessory neuropraxia/injury even when CN XI was anatomically preserved. Lower-lip asymmetry suggests marginal mandibular weakness; tongue deviation suggests XII; dysphonia/dysphagia may reflect X; elevated hemidiaphragm suggests phrenic injury; ptosis/miosis suggests sympathetic-chain injury. Milky drain output that rises with enteral fat suggests chyle leak, classically after low left-neck dissection. Expanding hematoma, brisk drain blood, airway change, neck swelling, sepsis/wound breakdown, venous congestion, or sentinel hemorrhage after radiation demand immediate escalation.",
        "localize": "Localize morbidity to the dissection level and structure: CN XI is vulnerable in IIb and posterior triangle/V; marginal mandibular nerve near level Ib and the facial vessels; XII crosses the carotid region toward the tongue; vagus lies in the carotid sheath; phrenic nerve lies on anterior scalene deep to the transverse cervical plane; sympathetic chain is posterior/deep to the carotid sheath; thoracic duct terminates near the left venous angle and is most vulnerable in low level IV. Bilateral IJV sacrifice or thrombosis can cause severe craniofacial edema and intracranial venous hypertension. Distinguish routine postoperative edema from hematoma, lymphatic leak, infection, venous obstruction or salivary contamination.",
        "workup": "Work up the COMPLICATION rather than restaging the cancer. Serial focused cranial-nerve and shoulder examination is often more useful than indiscriminate imaging. For suspected chyle, inspect output in relation to feeding and use drain triglyceride/chylomicron testing when the appearance or diagnosis is uncertain. Expanding hematoma or active hemorrhage is primarily a clinical emergency; obtain CTA only when the patient is stable enough and imaging will guide control. Duplex/CT venography can assess suspected IJV thrombosis when clinically important. Evaluate wound breakdown for fistula/salivary contamination, infection, exposed great vessels and prior-radiation risk.",
        "manage": "Match rescue to severity and physiology. Begin early shoulder physical therapy for accessory-nerve dysfunction and distinguish traction neuropraxia from transection. Low-output chyle leaks can often be treated with drainage, pressure selectively, dietary fat restriction/MCT or enteral modification and escalation based on output/trajectory; persistent high-output leaks, metabolic compromise or failure of conservative therapy should prompt operative or interventional control rather than prolonged depletion. Treat hematoma/airway compromise with urgent decompression and hemostasis. Manage wound infection/fistula with drainage, culture-directed antibiotics when indicated, nutrition and protection of exposed vessels; a sentinel bleed in a radiated infected neck is carotid blowout until proven otherwise.",
        "operate": "PREVENTION is part of the operation: identify CN XI and limit traction; remain on safe fascial planes around marginal mandibular, XII, X, phrenic and sympathetic structures; preserve IJV/SCM/nerves when oncologically appropriate; ligate lymphatic channels carefully in low left level IV; achieve meticulous hemostasis and protect major vessels with vascularized tissue when risk is high. If a thoracic-duct leak is found, control the leaking channel(s) securely and consider adjunctive local measures; if a nerve is transected and recognized, repair/graft when feasible. Expanding hematoma, uncontrolled chyle, major vessel exposure/rupture, or threatened carotid requires decisive operative/endovascular rescue rather than observation.",
        "teach": "Chief/boards framework: COMPLICATION = STRUCTURE + LEVEL + TIMING + RESCUE. IIb/V -> CN XI/shoulder; Ib -> marginal mandibular; low left IV -> thoracic duct; carotid sheath -> X/IJV; anterior scalene -> phrenic; posterior sheath -> sympathetic chain. Preservation does not equal zero morbidity—CN XI traction alone can cause shoulder syndrome. In a previously irradiated neck, wound breakdown and a sentinel bleed sharply raise concern for carotid blowout. This card does not reteach which nodal levels should be dissected; it starts after the operation is selected and focuses on preventing, recognizing and rescuing morbidity.",
        "tags": ["neck dissection complications", "spinal accessory nerve", "shoulder syndrome", "chyle leak", "thoracic duct", "marginal mandibular nerve", "hypoglossal nerve", "phrenic nerve", "IJV thrombosis", "carotid blowout"],
        "source_basis": ["Cummings Otolaryngology—Head and Neck Surgery, 7e — neck dissection operative anatomy and complications", "K.J. Lee's Essential Otolaryngology, 12e — cervical surgical anatomy, nerve/vascular/lymphatic complications", "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Neck Dissection complications", "ASCO Clinical Practice Guideline: Management of the Neck in Squamous Cell Carcinoma of the Oral Cavity and Oropharynx (JCO 2019) — morbidity-minimizing high-quality neck dissection principles"],
    },
}


def apply_headneck_neck_dissection_rebuild_v305(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = NECK_DISSECTION_V305.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v305"] = True
        module["semantic_role_v305"] = (
            "oncologic_extent_and_quality" if _norm(module.get("topic")) == "neck dissection"
            else "complication_prevention_recognition_and_rescue"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
