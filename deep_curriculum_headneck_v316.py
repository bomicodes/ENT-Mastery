"""v31.6 — source-grounded salvage surgery Concept Hub rebuild.

Separates the irradiated-field operative/reconstructive card from the post-CRT
oncologic-selection card. They intentionally share prior-treatment context but answer
different resident/boards questions: HOW to operate safely after radiation versus WHO
should undergo curative-intent salvage after definitive chemoradiation.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


SALVAGE_SURGERY_REBUILD_V316 = {
    "salvage surgery after radiation": {
        "recognize": (
            "Use this card for the OPERATIVE BIOLOGY OF THE PREVIOUSLY IRRADIATED FIELD, not for deciding whether recurrent cancer deserves salvage. Prior RT produces fibrosis, microvascular injury, impaired tissue oxygenation/perfusion, lymphatic disruption, friable vessels, poor healing, and obliterated planes. Translate that biology into the complications that matter to the surgeon: pharyngocutaneous or salivary fistula, wound breakdown, infection, exposed great vessels, stenosis/stricture, delayed healing, flap problems, and potentially catastrophic carotid blowout. Risk rises further with malnutrition, anemia, hypothyroidism, tobacco exposure, diabetes, prior tracheostomy, extensive mucosal resection, and heavily treated neck tissues."
        ),
        "localize": (
            "Map the PRIOR TREATMENT FIELD before incision. Review radiation dose/fields, prior operations and neck dissections, scars, tracheostomy, fistula history, and available recipient vessels. Distinguish a limited cutaneous/soft-tissue salvage from a contaminated pharyngeal defect, circumferential pharyngoesophageal reconstruction, mandibular/skull-base exposure, or salvage laryngectomy because tissue requirements and vascular risk differ. Anticipate that the ipsilateral facial/superior thyroid/lingual/transverse cervical systems or jugular veins may be scarred, ligated, irradiated, or unavailable; plan contralateral or alternative recipient vessels before committing to a free flap."
        ),
        "workup": (
            "This card's workup is PREOPERATIVE RISK AND RECONSTRUCTIVE PLANNING after oncologic resectability has already been established. Review prior RT plan and operative notes; obtain appropriate contrast imaging to understand tumor-vessel relationships and neck anatomy; assess nutrition/weight loss, CBC, renal function, albumin/prealbumin only as contextual nutritional markers, thyroid function after neck irradiation, glycemic control, smoking, pulmonary reserve, dentition when relevant, and donor-site suitability. If carotid encasement/exposure or vessel-depleted neck is possible, involve reconstructive and vascular/interventional expertise early. Do not order a generic thrombophilia panel or prophylactic vessel study without a clinical indication."
        ),
        "manage": (
            "Optimize what is modifiable before surgery: nutrition, hydration, anemia when clinically actionable, thyroid dysfunction, diabetes, tobacco cessation, infection, and airway planning. Counsel explicitly that salvage in an irradiated field carries substantially higher wound/fistula morbidity than primary surgery and may require prolonged enteral feeding, wound care, reoperation, or flap reconstruction. Build postoperative plans around airway protection, salivary diversion/feeding, drain and wound surveillance, early recognition of fistula, and protection of exposed carotid or great vessels. A small leak over healthy tissue and a leak tracking to an irradiated exposed carotid are not equivalent problems."
        ),
        "operate": (
            "OPERATIVE PRINCIPLE: replace or reinforce compromised irradiated tissue with WELL-VASCULARIZED NONIRRADIATED TISSUE when the defect/risk justifies it. Preserve viable skin and mucosa, handle fibrotic tissue gently, obtain meticulous hemostasis, separate contaminated pharyngeal/salivary spaces from carotid and hardware, and avoid placing tenuous closures directly over great vessels. In salvage total laryngectomy, contemporary meta-analysis supports strongly considering pedicled or free vascularized tissue rather than reflex primary closure because flap-assisted closure lowers pharyngocutaneous fistula risk. Choose onlay reinforcement versus patch/tubed reconstruction according to mucosal deficiency; have a recipient-vessel strategy and backup before flap ischemia begins."
        ),
        "teach": (
            "Chief/boards discriminator: AFTER RADIATION = THINK TISSUE QUALITY. The question is not merely 'can I remove the recurrence?' but 'what will safely heal after I remove it?' Prior radiation means fibrosis + hypovascularity + poor healing; therefore anticipate fistula, vessel exposure and reconstructive difficulty, optimize the host, and bring vascularized tissue when primary closure would leave a high-risk irradiated wound. Keep this distinct from 'Salvage Surgery After Chemoradiation,' which owns oncologic selection and restaging after definitive CRT failure."
        ),
        "tags": ["salvage surgery", "radiation", "irradiated neck", "pharyngocutaneous fistula", "vascularized tissue", "free flap", "pectoralis flap", "carotid blowout", "vessel-depleted neck"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent head and neck cancer, salvage surgery, irradiated-field complications, and reconstruction",
            "K.J. Lee's Essential Otolaryngology, 12e — recurrent head and neck cancer, salvage procedures, and reconstructive principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — salvage head and neck surgery, complications, and reconstruction",
            "Paleri et al., Laryngoscope 2024 network meta-analysis — vascularized tissue lowers pharyngocutaneous fistula rates after salvage total laryngectomy compared with primary closure",
        ],
    },
    "salvage surgery after chemoradiation": {
        "recognize": (
            "Use this card for ONCOLOGIC SELECTION AFTER DEFINITIVE CHEMORADIATION FAILURE. First decide whether this is persistent disease, a true locoregional recurrence after response, a treatment-related change, or distant/metastatic progression. Salvage surgery can provide the principal curative option for selected resectable persistent/recurrent HNSCC after CRT, but not every radiographic abnormality should trigger a morbid operation. Selection depends on anatomic resectability, absence/control of distant disease, disease-free interval, recurrent T/N burden, prior treatment, performance status, nutrition/comorbidity, expected postoperative function, and whether an R0 resection is realistically achievable."
        ),
        "localize": (
            "Restage the RECURRENCE, not the old cancer. Define mucosal/submucosal extent, cartilage/bone involvement, nodal levels, extranodal extension when assessable, carotid/skull-base/prevertebral relationships, and distant disease. Site matters: a small mobile laryngeal recurrence, bulky base-of-tongue recurrence crossing compartments, isolated neck disease, and skull-base recurrence do not share the same salvage operation or probability of clear margins. For HPV-associated oropharyngeal disease, biology may be more favorable in some recurrences, but HPV status does not override resectability, metastatic burden, or functional cost."
        ),
        "workup": (
            "Confirm a salvageable target with examination/endoscopy, contrast CT and/or MRI as anatomy requires, and whole-body staging (often PET/CT) before committing to major surgery. Routine post-CRT response PET/CT is generally delayed to roughly 12 weeks or later because earlier inflammatory uptake reduces specificity; an equivocal early response may warrant interval reassessment rather than automatic neck dissection when the patient is clinically stable. Obtain tissue confirmation when imaging/exam is equivocal or histology would change management, but do not force an unsafe biopsy of a clearly progressive, imminently threatening lesion. Review the original pathology, RT dose/fields, systemic therapy, and multidisciplinary alternatives."
        ),
        "manage": (
            "Discuss every plausible pathway in multidisciplinary conference: curative-intent salvage surgery when an R0 resection with acceptable morbidity is achievable; systemic therapy for unresectable recurrent/metastatic disease according to tumor biomarkers and prior therapy; selected reirradiation or other local therapy in appropriate patients; clinical trial; or symptom-directed palliative care. Separate technical resectability from BENEFIT: an operation that removes gross disease but predictably leaves positive margins, severe nonrecoverable function, or delays more appropriate systemic treatment may not be worthwhile. Shared decision-making must include voice, swallow, airway, appearance, feeding-tube/tracheostomy dependence, complication risk, and realistic probability of durable control."
        ),
        "operate": (
            "The oncologic goal is an R0 EN BLOC SALVAGE appropriate to the recurrent site's anatomy, with neck dissection when there is clinically involved regional disease or when the chosen salvage operation/site-specific oncologic strategy warrants it. Do not perform elective radicalization simply because the neck was previously irradiated. Before incision, define the margin plan and abortability thresholds—unreconstructable carotid involvement, prohibitive skull-base/prevertebral extension, disseminated disease discovered during staging, or inability to achieve meaningful gross clearance should trigger reconsideration rather than heroic R1/R2 surgery. Reconstruction of the irradiated defect is critical but is owned in detail by the companion 'After Radiation' card."
        ),
        "teach": (
            "Chief/boards discriminator: AFTER CHEMORADIATION FAILURE = THINK SELECTION + RESTAGING + R0. Ask: Is disease truly persistent/recurrent? Is it locoregionally confined? Is it resectable to negative margins? Will the patient survive and function well enough to benefit? What are the systemic/reirradiation alternatives? Salvage surgery remains potentially curative in carefully selected resectable disease, whereas unresectable or metastatic recurrence generally moves toward systemic/local palliative strategies. Keep the companion radiation card focused on HOW the irradiated wound is safely reconstructed."
        ),
        "tags": ["salvage surgery", "chemoradiation", "recurrent HNSCC", "persistent disease", "PET CT", "resectability", "R0 margin", "multidisciplinary tumor board", "reirradiation"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent/persistent HNSCC, salvage surgery selection, and reconstruction after definitive therapy",
            "K.J. Lee's Essential Otolaryngology, 12e — recurrent head and neck malignancy and salvage treatment principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — recurrent head and neck cancer evaluation and salvage management",
            "ASCO recurrent/metastatic HNSCC guidance — systemic therapy/biomarker framework when recurrence is not appropriately salvageable by surgery",
            "Contemporary post-treatment PET/CT literature — response imaging around 12-13 weeks after CRT and selective repeat imaging for equivocal response",
        ],
    },
}


def apply_salvage_surgery_rebuild_v316(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = SALVAGE_SURGERY_REBUILD_V316.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v316"] = True
            module["semantic_role_v316"] = (
                "irradiated-field operative biology, complication prevention, and vascularized reconstruction"
                if key == "salvage surgery after radiation"
                else "post-chemoradiation recurrence restaging, resectability, and curative-salvage selection"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
