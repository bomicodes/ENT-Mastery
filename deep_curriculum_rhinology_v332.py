"""v33.2 — distinguish systemic allergic rhinitis from local allergic rhinitis.

Keeps the common parent disease focused on clinically relevant systemic sensitization and
management, while making local allergic rhinitis an advanced diagnostic phenotype for
patients with an allergic history but negative conventional skin/serum testing.
"""

import re

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


ALLERGIC_RHINITIS_V332 = {
    "recognize": (
        "Recognize ALLERGIC RHINITIS as an exposure-linked IgE-mediated rhinitis: sneezing, nasal itching, clear rhinorrhea and congestion, often with ocular itching/tearing and an atopic context. Pattern matters more than a pale turbinate alone. Ask when symptoms occur, where they occur, which exposures reproduce them, whether they are intermittent or persistent, and how they affect sleep, school/work, asthma and quality of life. Purulence, unilateral obstruction/bleeding, prominent pain, crusting, medication overuse or a non-exposure-linked vasomotor pattern should reopen the differential rather than be forced into an allergy label."
    ),
    "localize": (
        "Localize conventional allergic rhinitis as a TYPE-I HYPERSENSITIVITY process in which inhaled allergen cross-links allergen-specific IgE on mast cells, producing an early histamine-predominant response and a later inflammatory phase involving eosinophils and other mediators. The clinically useful concept is a UNITED AIRWAY: asthma, conjunctivitis and sinonasal disease may coexist, so poor nasal control can matter beyond the nose. Do not confuse sensitization with disease: a positive skin test or serum-specific IgE is relevant only when the allergen fits the patient's exposure-linked symptoms."
    ),
    "workup": (
        "Make the diagnosis primarily from HISTORY + EXAM. Use skin-prick testing or serum allergen-specific IgE when the diagnosis is uncertain, empiric treatment is inadequate, identifying the trigger will change avoidance or therapy, or immunotherapy is being considered. Test only plausible inhalant allergens and interpret results in clinical context because asymptomatic sensitization and cross-reactivity occur. Routine sinus CT, broad food panels, total IgE, nasal cytology and indiscriminate laboratory testing do not establish ordinary allergic rhinitis. If the story is strongly allergic but conventional systemic testing is negative, do not simply relabel the patient 'nonallergic'—consider LOCAL ALLERGIC RHINITIS and other rhinitis phenotypes."
    ),
    "manage": (
        "Treat to the dominant symptom burden and patient preference. Environmental measures should target a confirmed or strongly suspected relevant exposure rather than demand unrealistic global avoidance. INTRANASAL CORTICOSTEROIDS are first-line for persistent or quality-of-life-limiting disease, with correct technique and regular use emphasized. Second-generation oral or intranasal antihistamines are useful particularly for sneezing/itching/rhinorrhea; intranasal antihistamine plus intranasal steroid is a rational escalation when monotherapy is inadequate. Saline may improve comfort and mucus clearance. Avoid routine depot/systemic steroids and prolonged topical decongestants. Assess asthma when suggested by the history."
    ),
    "operate": (
        "Allergic rhinitis is not primarily a surgical disease. Surgery addresses a separate structural problem—such as fixed septal obstruction or persistent turbinate hypertrophy—after the inflammatory component has been recognized and medically treated; it does not eliminate the underlying allergen-specific immune response. For symptoms inadequately controlled with medical therapy/avoidance, or when the patient prefers disease-modifying treatment, offer or refer for ALLERGEN IMMUNOTHERAPY when clinically relevant sensitization is established and contraindications/risk are addressed. Do not use a positive allergy test alone as an indication for surgery or immunotherapy."
    ),
    "teach": (
        "Boards/chief model: ordinary ALLERGIC RHINITIS requires three things to line up—ALLERGIC SYMPTOMS + PLAUSIBLE EXPOSURE + CLINICALLY RELEVANT SENSITIZATION. Skin/serum testing supports that relationship; it does not replace the history. Treat inflammation first, especially with intranasal steroid, then escalate symptom-specific therapy or allergen immunotherapy when appropriate. The key handoff to the companion concept is: allergic phenotype + NEGATIVE conventional systemic testing is not automatically nonallergic rhinitis; think LOCAL ALLERGIC RHINITIS when the exposure story remains convincing."
    ),
    "tags": ["allergic rhinitis", "type I hypersensitivity", "skin testing", "serum specific IgE", "intranasal corticosteroid", "allergen immunotherapy", "united airway"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — allergic-rhinitis immunobiology, phenotype/differential, diagnostic testing, and medical/immunotherapy framework",
        "K.J. Lee's Essential Otolaryngology, 12e — allergy testing, systemic versus nasal specific IgE, intranasal corticosteroids, antihistamines, and immunotherapy",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — allergic-rhinitis symptoms, allergy testing, pharmacotherapy, comorbid asthma, and immunotherapy",
        "AAO-HNSF Clinical Practice Guideline: Allergic Rhinitis, 2015 — clinical diagnosis, selective specific-IgE testing, intranasal steroid/antihistamine treatment, and immunotherapy referral",
        "AAO-HNSF Clinical Practice Guideline: Immunotherapy for Inhalant Allergy, 2024 — candidacy, relevant-allergen selection, shared decision-making, and immunotherapy safety",
    ],
}


LOCAL_ALLERGIC_RHINITIS_V332 = {
    "recognize": (
        "Recognize LOCAL ALLERGIC RHINITIS (LAR) when the HISTORY BEHAVES LIKE ALLERGY—reproducible sneezing, itching, watery rhinorrhea/congestion with a plausible inhalant exposure—but standard skin-prick testing and serum allergen-specific IgE are negative. LAR is not simply 'mild allergic rhinitis' and is not synonymous with generic nonallergic/vasomotor rhinitis. The defining concept is a localized nasal allergic response without demonstrable systemic sensitization by conventional testing."
    ),
    "localize": (
        "Localize the abnormality to the NASAL MUCOSA: allergen exposure can generate a local IgE/type-2 inflammatory response even when circulating allergen-specific IgE and skin testing are negative. This explains why an apparently classic pollen/dust-mite exposure history can conflict with conventional testing. Keep LAR distinct from NARES, where nasal eosinophilia is present without evidence that a specific allergen is driving a local IgE response, and from nonallergic rhinopathy, which is typically triggered by nonspecific stimuli such as temperature, odors or irritants."
    ),
    "workup": (
        "Do not diagnose LAR merely because systemic tests are negative. First confirm that the symptom pattern is genuinely exposure-linked and exclude medication-induced rhinitis, structural disease, CRS, NARES and nonallergic rhinopathy. In a specialist setting, a controlled NASAL ALLERGEN PROVOCATION TEST showing a reproducible local response is the most direct confirmatory test when available. Nasal allergen-specific IgE can support the diagnosis, but collection/assay methods are not standardized enough for a negative nasal IgE result to reliably exclude LAR. Conventional serum/skin tests remain negative by definition of the phenotype being considered."
    ),
    "manage": (
        "Treat the symptomatic nasal inflammation similarly to allergic rhinitis: intranasal corticosteroid is a strong baseline choice, with intranasal or second-generation oral antihistamine added according to symptom pattern; targeted avoidance is reasonable when a reproducible local trigger has been established. The important management distinction is diagnostic discipline—do not order progressively broader systemic allergy panels expecting LAR to become positive, and do not tell the patient that negative systemic testing proves symptoms are 'not allergic.'"
    ),
    "operate": (
        "LAR has no routine operative treatment. Surgery is reserved for an independent structural problem after the inflammatory phenotype has been addressed. Allergen immunotherapy for carefully confirmed LAR has supportive clinical-trial evidence and is described in specialty literature/texts, but it is a SPECIALIST-SELECTED strategy rather than something to prescribe solely from symptoms plus negative systemic testing; establish the responsible local allergen and discuss the less mature evidence base compared with conventionally sensitized allergic rhinitis."
    ),
    "teach": (
        "Boards/chief discriminator: ALLERGIC RHINITIS = allergic phenotype + clinically relevant SYSTEMIC sensitization. LOCAL ALLERGIC RHINITIS = allergic phenotype + NEGATIVE skin/serum testing + evidence of a LOCAL nasal allergen response. NONALLERGIC RHINOPATHY = symptoms driven mainly by nonspecific triggers without an allergen-specific mechanism. NARES = nonallergic systemic testing with prominent nasal eosinophilia. The trap is treating 'negative allergy testing' as a single diagnosis; it is only the start of the phenotype split."
    ),
    "tags": ["local allergic rhinitis", "LAR", "nasal allergen provocation", "nasal specific IgE", "negative skin testing", "NARES", "nonallergic rhinitis"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — rhinitis phenotyping and local versus systemic allergic mechanisms",
        "K.J. Lee's Essential Otolaryngology, 12e — local allergic rhinitis, nasal specific IgE, nasal provocation testing, and distinction from NARES",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — allergic versus nonallergic rhinitis differential and treatment framework",
        "International/allergy literature on local allergic rhinitis — nasal allergen provocation as the key confirmatory method and limitations of nasal-specific IgE assays",
        "AAO-HNSF Clinical Practice Guideline: Immunotherapy for Inhalant Allergy, 2024 — use clinically relevant allergen identification and safe specialist selection when considering immunotherapy",
    ],
}


def apply_rhinology_allergic_lar_distinction_v332(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        topic = _norm(module.get("topic"))
        payload = None
        if topic == "allergic rhinitis":
            payload = ALLERGIC_RHINITIS_V332
        elif topic == "local allergic rhinitis":
            payload = LOCAL_ALLERGIC_RHINITIS_V332
        if payload is None:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v332"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
