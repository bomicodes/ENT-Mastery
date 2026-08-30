"""v29.9 — source-grounded CRSsNP versus CRSwNP Concept Hub rebuild.

Separates the two canonical CRS phenotype cards into distinct clinical jobs. CRSsNP owns
objective CRS diagnosis without polyposis, secondary-cause search, maximal topical therapy,
and anatomy-directed ESS. CRSwNP owns polyp/type-2 phenotype recognition, smell/asthma/AERD
risk, recurrence biology, steroid-sparing escalation, biologics, and phenotype-informed surgery.
"""

import re

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


CRS_REBUILD_V299 = {
    "crssnp": {
        "recognize": (
            "Recognize CHRONIC RHINOSINUSITIS WITHOUT NASAL POLYPS (CRSsNP) as inflammatory sinonasal disease lasting at least 12 weeks with compatible symptoms AND objective evidence of inflammation, but without endoscopically visible nasal polyps. Symptoms alone are not enough: typical complaints include obstruction/congestion, anterior or posterior drainage, facial pressure/fullness and impaired smell, but these overlap substantially with rhinitis, migraine, neuralgia and structural nasal disease. The absence of polyps is a phenotype label, not proof of a single mechanism; CRSsNP is biologically heterogeneous and should not be reduced to 'chronic bacterial sinus infection.'"
        ),
        "localize": (
            "Localize both the DISTRIBUTION of disease and the likely DRIVER. Nasal endoscopy and CT can distinguish limited ostiomeatal disease from diffuse pansinus inflammation and reveal purulence, edema, scarring, odontogenic patterns, unilateral disease, prior surgical obstruction or an anatomic contributor. A unilateral maxillary-predominant process should trigger an odontogenic/foreign-body/tumor differential rather than being managed as routine bilateral inflammatory CRS. Recurrent infections, unusual organisms, bronchiectasis, childhood onset or refractory disease should reopen immune deficiency, cystic fibrosis/CFTR-related disease and primary ciliary dyskinesia. The key contrast with CRSwNP is that the visible polyp/type-2 recurrent-polyp phenotype is absent, so treatment escalation is usually driven by objective disease burden, symptoms, anatomy and secondary causes rather than biologic eligibility."
        ),
        "workup": (
            "Confirm CRS with objective inflammation by nasal endoscopy and/or sinus CT after establishing the greater-than-12-week symptom pattern; document prior treatment and symptom/QOL burden rather than ordering CT for every episode of facial pressure. Endoscopy should assess edema, purulence, crusting, scarring and the middle meatus; culture is most useful when purulence is present in refractory disease or when prior antibiotics make empiric selection unreliable. Evaluate allergy or immune function selectively when history or refractory disease makes the result actionable. For unilateral disease, dental symptoms, focal maxillary opacification, epistaxis, severe pain, cranial neuropathy or a mass, pursue the corresponding odontogenic or neoplastic workup instead of assuming routine CRSsNP."
        ),
        "manage": (
            "Anchor long-term therapy in HIGH-VOLUME SALINE IRRIGATION and a TOPICAL INTRANASAL CORTICOSTEROID, with attention to delivery technique and adherence. Treat a defined contributor—such as allergic rhinitis, odontogenic infection or immune deficiency—rather than reflexively cycling antibiotics. Antibiotics are not a universal chronic maintenance treatment; short culture-directed courses may be appropriate for selected acute bacterial exacerbations with purulence, and prolonged macrolide therapy is an option only in selected CRSsNP patients because the evidence, optimal regimen and responder phenotype are uncertain. Reassess objective disease and the dominant symptom before labeling medical therapy a failure, especially when facial pain is out of proportion to endoscopic/CT inflammation."
        ),
        "operate": (
            "Offer ENDOSCOPIC SINUS SURGERY when appropriately selected CRSsNP remains symptomatic with objective disease despite reasonable disease-specific medical therapy, or when anatomy/secondary pathology creates a clear surgical indication. The operative objective is not simply to remove mucosa: open the diseased sinus pathways, restore ventilation/drainage, obtain access for postoperative topical therapy, preserve functional mucosa when possible and correct a focal driver such as obstructed odontogenic disease. Extent should match disease distribution and prior anatomy rather than applying the same operation to every CT. Postoperative saline, topical corticosteroid therapy and endoscopic debridement/follow-up remain part of the treatment—not evidence that surgery 'failed.'"
        ),
        "teach": (
            "Chief/boards framework: CRSsNP = >=12 WEEKS OF COMPATIBLE SYMPTOMS + OBJECTIVE INFLAMMATION + NO POLYPS. Do not diagnose CRS from symptoms alone and do not call chronic facial pressure 'sinusitis' when objective disease is absent. Search for unilateral/odontogenic and systemic drivers when the pattern is atypical. First-line chronic therapy is topical—saline plus intranasal steroid—not endless antibiotics. ESS is anatomy- and disease-directed when symptoms and objective inflammation persist despite appropriate therapy; unlike severe CRSwNP, current biologic treatment pathways are not a routine CRSsNP escalation strategy."
        ),
        "tags": [
            "CRSsNP", "chronic rhinosinusitis without nasal polyps", "objective inflammation",
            "nasal endoscopy", "sinus CT", "saline irrigation", "intranasal corticosteroid",
            "odontogenic sinusitis", "endoscopic sinus surgery", "secondary CRS"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — CRS definition, phenotype, endoscopy/CT evaluation, secondary causes, medical treatment, and ESS principles",
            "K.J. Lee's Essential Otolaryngology, 12e — chronic rhinosinusitis diagnosis, differential diagnosis, medical therapy, and operative principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — CRS workup, topical therapy, antibiotics, and surgical pearls",
            "ICAR-RS 2021 — objective CRS diagnosis, CRSsNP phenotype, medical options, and evidence-based surgical management",
            "AAO-HNSF Clinical Practice Guideline: Adult Sinusitis Update, 2025 — objective confirmation and evidence-based chronic rhinosinusitis management",
            "AAO-HNSF Clinical Practice Guideline: Surgical Management of Chronic Rhinosinusitis, 2025 — candidacy, patient-centered surgical decision-making, and postoperative management",
        ],
    },
    "crswnp": {
        "recognize": (
            "Recognize CHRONIC RHINOSINUSITIS WITH NASAL POLYPS (CRSwNP) as chronic inflammatory sinonasal disease with objective BILATERAL inflammatory polyposis in the usual phenotype. Patients often emphasize nasal obstruction and loss of smell more than pain, and recurrent polyps, asthma and NSAID-exacerbated respiratory disease (AERD/N-ERD) should immediately suggest a strong type-2 inflammatory phenotype. A unilateral 'polyp,' bloody mass, severe focal pain or cranial neuropathy is not routine CRSwNP until proven otherwise—consider inverted papilloma, malignancy, antrochoanal polyp, fungal disease or another focal process."
        ),
        "localize": (
            "Localize CRSwNP beyond the word POLYP: define endoscopic polyp burden, CT distribution, olfactory-cleft involvement, prior surgical cavities and lower-airway comorbidity. Most Western severe/recurrent CRSwNP is type-2 dominant, but phenotype does not perfectly equal endotype; eosinophilia, total IgE, asthma/AERD and recurrence history help characterize inflammatory burden rather than independently establishing the diagnosis. Distinguish routine bilateral inflammatory polyposis from AFRS, cystic-fibrosis-associated polyposis and unilateral neoplasm. The practical contrast with CRSsNP is that recurrent diffuse polyposis and type-2 disease open a steroid-sparing BIOLOGIC pathway in addition to topical therapy and surgery."
        ),
        "workup": (
            "Confirm polyps by nasal endoscopy and define extent with CT when planning treatment or surgery. Document smell loss, asthma control, prior systemic-corticosteroid exposure, previous ESS/polyp recurrence, medication adherence and quality-of-life burden because these factors determine escalation. Ask specifically about respiratory reactions to aspirin/NSAIDs and asthma to identify AERD/N-ERD. CBC eosinophils and total IgE may help phenotype severe disease and select/monitor some biologic pathways, but there is no single biomarker that replaces clinical diagnosis. Biopsy an atypical unilateral, friable, necrotic or otherwise suspicious lesion rather than assuming every polypoid mass is inflammatory."
        ),
        "manage": (
            "Use HIGH-VOLUME SALINE and TOPICAL INTRANASAL CORTICOSTEROID as the chronic foundation; after surgery, high-volume steroid irrigations can improve drug delivery into opened sinus cavities. A short systemic corticosteroid burst can provide temporary relief in selected severe flares, especially smell/obstruction, but repeated bursts create cumulative toxicity and should trigger a steroid-sparing strategy rather than becoming maintenance therapy. Coordinate asthma/AERD care and consider aspirin desensitization in appropriately selected AERD patients. For severe uncontrolled CRSwNP despite standard medical and often surgical therapy, biologics targeting type-2 pathways are established add-on options; current U.S. options include dupilumab, omalizumab, mepolizumab and, since 2025, tezepelumab. Choice should account for prior surgery, systemic-steroid need, smell loss, asthma phenotype, biomarkers when relevant, dosing/cost and patient preference."
        ),
        "operate": (
            "ESS in CRSwNP is both DISEASE CLEARANCE and DRUG-DELIVERY surgery: remove obstructing polyps, open involved sinuses widely enough for ventilation and topical access, preserve healthy mucosa and create a postoperative cavity that can be medically maintained. Counsel that surgery does not erase the inflammatory endotype and recurrence is common, especially with severe type-2 disease/AERD, so topical anti-inflammatory maintenance is mandatory. In severe recurrent disease, the decision is not 'surgery OR biologic' in the abstract: compare symptom burden, prior ESS quality and durability, systemic-steroid dependence, asthma/AERD, biologic eligibility, cost/access and the likelihood that revision surgery will improve topical access. Steroid-eluting implants are an option for selected postoperative recurrent polyp disease."
        ),
        "teach": (
            "Chief/boards framework: CRSwNP = OBJECTIVE CRS + POLYPS, commonly with smell loss and a TYPE-2/asthma/AERD signal. Bilateral inflammatory polyps are common; a unilateral mass deserves a tumor/fungal/antrochoanal differential. Topical steroid + saline remain foundational even after ESS. Repeated oral-steroid bursts are a warning that disease control is poor. ESS improves anatomy and topical access but does not cure the inflammatory biology; biologics are for appropriately selected severe uncontrolled CRSwNP, not routine mild polyposis and not generic CRSsNP. Know the current U.S. biologic landscape—dupilumab, omalizumab, mepolizumab and tezepelumab—and select therapy using phenotype, comorbidity, prior surgery, steroid burden, access and patient goals."
        ),
        "tags": [
            "CRSwNP", "chronic rhinosinusitis with nasal polyps", "type 2 inflammation",
            "anosmia", "asthma", "AERD", "endoscopic sinus surgery", "steroid irrigation",
            "dupilumab", "omalizumab", "mepolizumab", "tezepelumab", "biologics"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — nasal polyposis, CRS inflammatory phenotypes, AERD, topical/systemic therapy, and ESS",
            "K.J. Lee's Essential Otolaryngology, 12e — CRSwNP diagnosis, differential diagnosis, medical therapy, and surgical management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — nasal polyposis, AERD, steroid therapy, ESS, and recurrence pearls",
            "ICAR-RS 2021 — CRSwNP definition, type-2 disease, topical/systemic corticosteroids, steroid-eluting implants, surgery, and biologic evidence",
            "AAO-HNSF Clinical Practice Guideline: Surgical Management of Chronic Rhinosinusitis, 2025 — surgical candidacy and patient-centered CRS management",
            "AAO-HNS Rhinology & Allergy Education Committee, Spring 2026 biologics update — contemporary U.S. CRSwNP biologic landscape including tezepelumab",
        ],
    },
}


def apply_rhinology_crs_rebuild_v299(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = CRS_REBUILD_V299.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v299"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
