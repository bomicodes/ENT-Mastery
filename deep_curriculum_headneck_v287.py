"""v28.7 — source-grounded salvage head & neck oncology Concept Hub rebuild.

The live canonical inventory has one salvage card, "Salvage Surgery After Radiation / Chemoradiation".
This rebuild therefore teaches two distinct clinical jobs inside that one canonical Hub:
1) broad salvage candidacy, irradiated-field operative planning, reconstruction, and complication mitigation;
2) the post-definitive-CRT response branch: response assessment, confirmation of residual/recurrent disease,
   PET-directed neck management, and selection of surgery versus nonsurgical salvage.

A second payload key is retained as a reusable post-CRT sublayer, but when no separate live canonical module
exists it is folded into the broad salvage Hub rather than remaining unreachable source content.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _append_unique(existing, addition, heading):
    existing = str(existing or "").strip()
    addition = str(addition or "").strip()
    if not addition or addition in existing:
        return existing
    return existing + f"\n\n{heading}: " + addition


SALVAGE_REBUILD_V287 = {
    "salvage surgery after radiation chemoradiation": {
        "recognize": (
            "Recognize SALVAGE SURGERY as potentially curative resection of persistent, recurrent, or second-primary head-and-neck cancer in a field previously treated with radiation and/or chemoradiation. The key resident-level distinction is that salvage is not simply 'repeat the original operation later': prior treatment changes tissue vascularity, fibrosis, wound healing, airway exposure, vessel quality, swallowing reserve, reconstructive options, and the expected complication profile. Before discussing an operation, determine whether disease is truly localized and resectable, whether distant metastasis or unresectable skull-base/carotid/prevertebral involvement changes intent, and whether the patient has enough functional reserve to benefit from a high-morbidity curative attempt."
        ),
        "localize": (
            "Localize salvage disease in THREE dimensions: ANATOMIC EXTENT, PRIOR TREATMENT FIELD, and FUNCTIONAL CONSEQUENCE. Map the recurrent primary relative to carotid artery, prevertebral fascia, skull base, mandible, larynx/hypopharynx, tracheostoma, cranial nerves, and previously reconstructed tissue; map nodal disease by level and relationship to major vessels; and reconstruct the prior radiation portals, operation, flap, neck dissection, and vessel exposure. A small mucosal recurrence in mobile tissue is a different salvage problem from a fixed ulcerated recurrence abutting carotid in a fibrotic neck. Prior treatment history is therefore part of localization, not merely background information."
        ),
        "workup": (
            "Confirm recurrence whenever feasible before committing to morbid salvage. Perform complete endoscopic examination, obtain contrast-enhanced cross-sectional imaging of the primary and neck, and use PET/CT when it meaningfully evaluates regional/distant disease or helps define occult recurrence. Biopsy suspicious mucosal or nodal disease unless the clinical situation requires immediate operative management. Review the ORIGINAL pathology, stage, surgery, radiation dose/fields, systemic therapy, interval from treatment, prior wound complications, feeding-tube/tracheostomy dependence, and reconstructive history. Assess nutrition, dentition when relevant, pulmonary/cardiac reserve, baseline speech/swallowing, and carotid/vessel status. Multidisciplinary review is essential because reirradiation, systemic therapy, immunotherapy, clinical trial, or palliation may be preferable when surgery cannot achieve meaningful oncologic clearance."
        ),
        "manage": (
            "Select salvage surgery when an R0/R1-intent resection with acceptable morbidity is realistically achievable and the patient understands the trade-off between cure probability and functional cost. Favor surgery for technically resectable isolated locoregional recurrence when durable control is plausible, especially after prior full-dose radiation limits further radiotherapy options. Do not equate 'technically operable' with 'appropriate': short disease-free interval, major comorbidity, poor performance status, carotid/prevertebral/skull-base fixation, extensive distant disease, or an operation that cannot deliver meaningful control may shift the recommendation toward nonsurgical therapy or symptom-focused care. Prehabilitate nutrition, tobacco/alcohol cessation, pulmonary status, and swallowing when time permits, and plan reconstruction before incision rather than after the defect appears."
        ),
        "operate": (
            "Operate with a SALVAGE FIELD mindset. Expect obliterated planes and devascularized tissue; identify major vessels and nerves deliberately rather than relying on familiar primary-surgery planes. Resect to oncologically sound margins while minimizing unnecessary devascularization. In heavily irradiated defects, bring in WELL-VASCULARIZED NONIRRADIATED TISSUE early—often free tissue transfer or a robust regional flap—to separate the pharynx from great vessels, protect exposed carotid, reconstruct mucosa/skin, and reduce fistula or wound breakdown risk. Anticipate difficult airway management, pharyngocutaneous fistula, infection, carotid exposure/blowout, poor bone healing, and flap-vessel challenges. Vessel-depleted neck planning may require preoperative review of recipient vessels and alternate recipient sites. The reconstructive plan is part of the cancer operation, not a secondary cosmetic step."
        ),
        "teach": (
            "Chief/boards framework: SALVAGE = CONFIRM DISEASE → EXCLUDE UNCURABLE EXTENT/DISTANT SPREAD → RECONSTRUCT PRIOR TREATMENT → ASK WHETHER COMPLETE RESECTION IS WORTH THE MORBIDITY → BRING HEALTHY VASCULARIZED TISSUE INTO THE IRRADIATED FIELD. Prior radiation changes everything: fibrosis obscures planes, vessels and mucosa heal poorly, fistula and carotid complications are more dangerous, and reconstruction frequently becomes mandatory. The broad salvage framework is about CANDIDACY, FIELD RISK, and RECONSTRUCTION; after definitive CRT, add the response-directed neck-management branch rather than reflexively operating on the pretreatment nodal stage."
        ),
        "tags": [
            "salvage surgery", "recurrent head and neck cancer", "irradiated neck", "reirradiation",
            "free flap", "vessel depleted neck", "pharyngocutaneous fistula", "carotid blowout",
            "recurrent squamous cell carcinoma", "salvage reconstruction"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent head-and-neck cancer, salvage oncologic surgery, irradiated-field complications, and reconstruction",
            "K.J. Lee's Essential Otolaryngology, 12e — recurrent head-and-neck malignancy and salvage surgical principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — practical salvage evaluation, operative risk, and reconstruction pearls",
            "NCCN Clinical Practice Guidelines in Oncology: Head and Neck Cancers — management options for persistent/recurrent locoregional disease after prior radiation, including surgery when resectable",
            "AHNS/major contemporary salvage-surgery literature — prognostic importance of resectability, disease-free interval, patient selection, vascularized reconstruction, and complication mitigation in previously irradiated fields",
        ],
    },
    "salvage surgery after chemoradiation": {
        "recognize": (
            "Recognize the POST-DEFINITIVE-CHEMORADIATION problem: has the patient achieved a complete response, or is there biopsy/imaging/endoscopic evidence of RESIDUAL or later RECURRENT locoregional disease that now needs salvage? After organ-preservation CRT, persistent primary-site disease, a persistently abnormal node, new progressive focal uptake/mass, worsening ulceration, pain, bleeding, cranial neuropathy, or progressive dysphagia/airway symptoms should trigger recurrence evaluation. A post-treatment neck mass alone is not proof of viable tumor because fibrosis and treatment-related change can persist."
        ),
        "localize": (
            "Localize the suspected failure as PRIMARY-SITE residual/recurrent disease, NODAL residual/recurrent disease, BOTH, or DISTANT progression. Then distinguish a persistent abnormality soon after CRT from a true later recurrence after an interval response. At the primary site, correlate endoscopic mucosal findings with deep-space imaging because submucosal recurrence may be occult. In the neck, ask whether the suspicious node is metabolically active/progressive and whether it threatens carotid, skin, cranial nerves, or deep musculature. This localization determines whether salvage is transoral/local, open composite, laryngectomy/pharyngectomy, neck dissection, combined primary-plus-neck surgery, or not surgically curable."
        ),
        "workup": (
            "Use structured RESPONSE ASSESSMENT rather than reflex planned surgery. Clinical/endoscopic examination plus appropriately timed post-treatment imaging is standard; PET/CT performed roughly 12 weeks after definitive CRT is commonly used for nodal response assessment because earlier scans have more inflammatory false positives. When PET/CT shows complete metabolic response and examination is reassuring, routine planned neck dissection is generally avoided. Equivocal or progressive findings require short-interval imaging, ultrasound-guided FNA/core biopsy, direct laryngoscopy/biopsy, or another targeted test according to site and urgency. Before salvage, restage the chest/distant sites and review prior radiation fields/doses and chemotherapy because a technically resectable neck recurrence in the setting of disseminated disease may not warrant morbid surgery."
        ),
        "manage": (
            "Manage according to RESPONSE. Complete clinical/metabolic nodal response after definitive CRT: observe with surveillance rather than performing a routine planned neck dissection. Confirmed resectable residual or recurrent primary-site disease: discuss salvage resection appropriate to the involved subsite and functional cost. Confirmed persistent/recurrent nodal disease without distant progression: salvage neck dissection may provide regional control when complete resection is achievable. Equivocal early imaging should not automatically trigger surgery; use targeted reassessment because inflammatory uptake can resolve. Unresectable recurrence, distant disease, or prohibitive morbidity shifts management toward systemic therapy, reirradiation in selected patients, clinical trial, or palliative care."
        ),
        "operate": (
            "Tailor the operation to the FAILURE PATTERN rather than repeating the pretreatment plan. Salvage neck dissection after CRT is performed through fibrotic tissue with increased risk to carotid, vagus, hypoglossal nerve, phrenic nerve, CN XI, thoracic duct, skin, and wound healing; preserve uninvolved structures when oncologically safe but prioritize complete gross resection. Primary-site salvage may require transoral resection, open partial surgery, total laryngectomy, pharyngolaryngectomy, or composite resection depending on site/extent. Anticipate the need for vascularized tissue reinforcement—particularly around pharyngeal closure or exposed great vessels—to reduce fistula and catastrophic wound complications. A salvage laryngectomy patient with heavily irradiated tissue should have the reconstructive strategy discussed before incision."
        ),
        "teach": (
            "Chief/boards post-CRT decision tree: DO NOT DO A PLANNED NECK DISSECTION JUST BECAUSE A NODE USED TO BE POSITIVE. Assess response first. A reassuring examination plus complete metabolic response on appropriately timed PET/CT supports surveillance; persistent/progressive or biopsy-proven locoregional disease triggers salvage evaluation. Response assessment → confirm viable disease when needed → restage → salvage only the persistent/recurrent site that remains curably resectable. PET is a decision aid, not pathology, and early inflammatory uptake can mislead."
        ),
        "tags": [
            "salvage after chemoradiation", "post treatment PET CT", "planned neck dissection",
            "residual disease", "recurrent disease", "salvage neck dissection", "salvage laryngectomy",
            "organ preservation", "complete metabolic response", "PET NECK trial"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — post-treatment response assessment, recurrent disease, salvage neck dissection, and salvage primary-site surgery",
            "K.J. Lee's Essential Otolaryngology, 12e — chemoradiation response, persistent/recurrent disease, and salvage treatment",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — post-CRT surveillance and salvage operative pearls",
            "NCCN Clinical Practice Guidelines in Oncology: Head and Neck Cancers — post-treatment assessment and management of persistent/recurrent locoregional disease",
            "Mehanna et al., N Engl J Med 2016 (PET-NECK) — PET/CT-guided surveillance after chemoradiation avoids routine planned neck dissection without compromising survival in appropriately selected advanced nodal disease",
            "ASCO Clinical Practice Guideline: Management of the Neck in Squamous Cell Carcinoma of the Oral Cavity and Oropharynx, J Clin Oncol 2019 — response-assessment principles and avoidance of routine neck dissection after complete response to definitive chemoradiation",
        ],
    },
}


def apply_headneck_salvage_rebuild_v287(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    broad_module = None
    narrow_module = None
    for module in modules:
        key = _norm(module.get("topic"))
        payload = SALVAGE_REBUILD_V287.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v287"] = True
        patched.append(module.get("topic"))
        if key == "salvage surgery after radiation chemoradiation":
            broad_module = module
        elif key == "salvage surgery after chemoradiation":
            narrow_module = module

    folded_post_crt = False
    if broad_module is not None and narrow_module is None:
        post = SALVAGE_REBUILD_V287["salvage surgery after chemoradiation"]
        broad_module["workup"] = _append_unique(broad_module.get("workup"), post["workup"], "POST-CRT RESPONSE ASSESSMENT")
        broad_module["manage"] = _append_unique(broad_module.get("manage"), post["manage"], "POST-CRT RESPONSE-DIRECTED MANAGEMENT")
        broad_module["operate"] = _append_unique(broad_module.get("operate"), post["operate"], "POST-CRT SALVAGE OPERATIVE BRANCH")
        broad_module["teach"] = _append_unique(broad_module.get("teach"), post["teach"], "POST-CRT BOARD DECISION TREE")
        tags = list(broad_module.get("tags") or [])
        for tag in post.get("tags") or []:
            if tag not in tags:
                tags.append(tag)
        broad_module["tags"] = tags
        sources = list(broad_module.get("source_basis") or [])
        for source in post.get("source_basis") or []:
            if source not in sources:
                sources.append(source)
        broad_module["source_basis"] = sources
        broad_module["post_crt_response_sublayer_v287"] = True
        folded_post_crt = True

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched), "post_crt_folded_into_live_salvage": folded_post_crt}
