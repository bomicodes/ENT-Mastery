"""v35.2 — source-grounded Allergy Testing and Allergen Immunotherapy depth.

Reuses the existing Rhinology/Allergy curriculum and adds only high-consequence testing,
AIT selection, safety, regulatory, and duration decisions. Durable principles are grounded
in Cummings 7e, K.J. Lee 12e, and Pasha 6e; current decisions are cross-checked against
Rhinitis 2020, the 2024 AAO-HNSF Inhalant Immunotherapy CPG, and current FDA SLIT labeling.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")
CORE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — allergy testing interpretation, clinically relevant sensitization, and allergen immunotherapy principles",
    "K.J. Lee's Essential Otolaryngology, 12e — practical allergy testing and immunotherapy selection/safety",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — resident-level allergy workup and SCIT/SLIT counseling",
]

def _sources(*extra): return list(CORE_SOURCES) + list(extra)

PATCHES = {
    "Allergy Testing & Interpretation": {
        "recognize": "Recognize that a positive skin or serum specific-IgE test documents SENSITIZATION, not automatically clinically causal allergy. Testing is most useful when the exposure history and symptom pattern make IgE-mediated disease plausible and the result will change avoidance, medication strategy, diagnosis, or allergen-immunotherapy selection. Do not equate total IgE, eosinophilia, or broad screening panels with identification of a culprit allergen.",
        "localize": "Localize the diagnostic question before choosing a test: seasonal/perennial exposure correlation, upper-airway versus asthma manifestations, and whether systemic sensitization is expected. Negative conventional systemic testing does not by itself prove nonallergic rhinitis; strongly allergen-linked symptoms can raise local allergic rhinitis, while NARES and nonallergic rhinopathy remain distinct competing phenotypes.",
        "workup": "Choose SKIN-PRICK TESTING or SERUM ALLERGEN-SPECIFIC IgE selectively. Skin testing provides rapid in-vivo assessment but requires interpretable controls and consideration of medications/skin disease that can blunt results; serum specific-IgE is useful when skin testing is unsafe, impractical, or uninterpretable. Interpret either test against the clinical exposure history. Avoid indiscriminate inhalant or food panels, and do not use total IgE or eosinophil counts as substitute culprit-allergen tests. When systemic tests are negative despite a compelling localized allergen history, consider specialist evaluation for local allergic rhinitis rather than simply labeling the patient nonallergic.",
        "manage": "Use results to change care, not to accumulate sensitization labels. Counsel avoidance only for clinically relevant exposures; optimize disease-directed pharmacotherapy and reserve AIT consideration for patients with clinically meaningful allergic disease plus confirmed relevant sensitization. Do not order serial skin or serum testing merely to prove that ongoing immunotherapy is working when symptoms and exposures are stable; the 2024 inhalant-immunotherapy guideline advises against routine efficacy retesting unless clinical circumstances change.",
        "operate": "Allergy testing does not create a surgical indication. If obstruction, polyposis, CRS, septal deviation, or valve dysfunction is present, decide surgery on the objective structural/inflammatory disease and expected benefit, not on the size of a wheal or a serum IgE class. A positive allergy test should never distract from unilateral bleeding, mass, CSF leak, or other dangerous alternatives requiring separate workup.",
        "teach": "Senior model: first ask whether the history predicts IgE-mediated disease and whether the answer will change management. Then select an interpretable test and require CLINICAL RELEVANCE before acting. A positive test without exposure-linked symptoms is sensitization; a negative systemic test with compelling localized symptoms may require phenotype refinement, not diagnostic closure. Testing is a decision tool, not a diagnosis generator.",
        "tags": ["allergy testing", "skin-prick testing", "specific IgE", "sensitization", "clinical relevance", "local allergic rhinitis"],
        "source_basis": _sources("Rhinitis 2020: A Practice Parameter Update (AAAAI/ACAAI Joint Task Force) — selective testing and rhinitis phenotype interpretation", "Clinical Practice Guideline: Immunotherapy for Inhalant Allergy (AAO-HNSF, 2024) — clinically relevant allergen selection and avoidance of routine efficacy retesting"),
    },
    "Allergen Immunotherapy — SCIT / SLIT": {
        "recognize": "Recognize ALLERGEN IMMUNOTHERAPY (AIT) as disease-modifying treatment for appropriately selected IgE-mediated inhalant allergy, not a reflex escalation for any positive test. Candidacy requires clinically meaningful symptoms/exposure plus confirmed relevant sensitization, inadequate control or unacceptable burden with avoidance/pharmacotherapy, or a patient preference for disease-modifying therapy after informed discussion.",
        "localize": "Localize the treatment decision to the responsible allergen and route. Treat clinically relevant allergens rather than every positive sensitization. SCIT and SLIT differ in administration, adherence, systemic-reaction profile, convenience, cost/coverage, and available allergen formulations; route choice should be shared rather than presented as interchangeable dosing of the same product.",
        "workup": "Before starting AIT, confirm relevant sensitization and assess comorbid ASTHMA and current control because uncontrolled asthma increases severe systemic-reaction risk. Review medications/comorbidities that alter anaphylaxis risk or its treatment and confirm the patient can follow the selected regimen. Anyone performing allergy skin testing or administering AIT must be able to recognize and treat ANAPHYLAXIS. Do not initiate or give AIT through uncontrolled asthma or an acute systemic illness without reassessment.",
        "manage": "For SCIT, use a supervised protocol with appropriate post-injection observation and readiness to treat systemic reactions. For SLIT, distinguish FDA-APPROVED TABLETS for specific allergens/indications from compounded aqueous SLIT drops, which are not FDA-approved products for allergic rhinitis in the United States. Current FDA ODACTRA labeling covers house-dust-mite-induced allergic rhinitis with or without conjunctivitis in patients 5–65 years with confirmed HDM sensitization; follow the current product label for contraindications, first-dose supervision, and epinephrine preparedness. When AIT is effective, plan a disease-modifying course of at least about 3 YEARS before individualized continuation/cessation decisions rather than treating it as a short medication trial.",
        "operate": "AIT is not an operative therapy and does not replace surgery for a separate objective structural problem or appropriately selected CRS/polyposis indication. Conversely, septoplasty or sinus surgery does not eliminate clinically relevant allergic sensitization. Coordinate rather than substitute therapies when both inflammatory allergy and structural disease materially contribute.",
        "teach": "Senior model: the highest-risk AIT errors are treating a laboratory result instead of a patient, dosing through uncontrolled asthma, and being unprepared for anaphylaxis. Select the clinically relevant allergen, choose SCIT versus SLIT with route-specific counseling, follow FDA labeling for approved SLIT products, and judge efficacy clinically rather than by serial allergy-test normalization. Effective AIT is usually a multi-year commitment, with at least ~3 years before individualized duration decisions.",
        "tags": ["allergen immunotherapy", "SCIT", "SLIT", "anaphylaxis", "asthma", "FDA", "ODACTRA", "three years"],
        "source_basis": _sources("Clinical Practice Guideline: Immunotherapy for Inhalant Allergy (AAO-HNSF, 2024) — candidacy, asthma assessment, anaphylaxis preparedness, relevant-allergen selection, SCIT/SLIT education, no routine efficacy retesting, and minimum effective-course framework", "FDA ODACTRA current prescribing information — HDM allergic rhinitis indication ages 5–65, confirmed sensitization, severe allergic-reaction precautions and epinephrine preparedness"),
    },
}

def apply_rhinology_allergy_testing_ait_depth_v352(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        topic = str(module.get("topic") or "")
        payload = PATCHES.get(topic)
        if payload is None: continue
        for field in FIELDS: module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v352"] = True
        module["deliberate_review_v352"] = {
            "foundation": "clinically relevant sensitization, test/route physiology and indications",
            "application": "selective test interpretation, AIT candidacy, asthma and anaphylaxis safety",
            "senior_decision": "SCIT/SLIT/FDA distinctions, duration/retesting restraint and structural-disease boundaries",
        }
        patched.append(topic)
    expected, actual = set(PATCHES), set(patched)
    if actual != expected:
        raise RuntimeError(f"v35.2 canonical patch-target mismatch: missing={sorted(expected-actual) or 'none'} unexpected={sorted(actual-expected) or 'none'}")
    if app_module is not None: app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
