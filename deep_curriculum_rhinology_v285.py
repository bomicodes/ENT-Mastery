"""v28.5 — source-grounded allergic rhinitis Concept Hub rebuild.

Separates conventional systemic allergic rhinitis from local allergic rhinitis (LAR)
so the two canonical cards teach different diagnostic evidence, testing logic, and
treatment escalation rather than repeating the same rhinitis phenotype.
"""

import re

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


RHINITIS_REBUILD_V285 = {
    "allergic rhinitis": {
        "recognize": (
            "Recognize conventional ALLERGIC RHINITIS (AR) as an IgE-mediated nasal syndrome in which exposure to a clinically relevant allergen produces sneezing, nasal itching, watery rhinorrhea and/or congestion, often with ocular itching or tearing. The history should establish timing, seasonality or perennial exposure, trigger correlation, severity and quality-of-life impact rather than relying on pale turbinates alone. Ask about asthma, atopic dermatitis, conjunctivitis, sleep-disordered breathing and recurrent sinonasal/ear symptoms because AR commonly travels with other atopic and upper-airway disease. Purulent drainage, unilateral bleeding, severe facial pain, anosmia with polyposis, or a unilateral mass should reopen the differential rather than being absorbed into an 'allergy' label."
        ),
        "localize": (
            "Localize the disease immunologically and anatomically: conventional AR reflects allergen-specific IgE sensitization that is demonstrable systemically by skin-prick testing and/or serum specific-IgE when testing is indicated, with the nasal mucosa serving as the symptomatic target organ. Classify the clinically important phenotype by intermittent versus persistent exposure pattern, symptom burden and dominant complaint (itch/sneeze/rhinorrhea versus obstruction), then identify structural contributors such as septal deviation or inferior-turbinate hypertrophy that may coexist but do not create IgE-mediated disease. The key contrast with LOCAL allergic rhinitis is that conventional AR has evidence of SYSTEMIC sensitization to a relevant allergen."
        ),
        "workup": (
            "Diagnosis is usually clinical first. Perform a focused nasal examination/endoscopy when anatomy, polyps, chronic rhinosinusitis or another lesion is in question. Obtain and interpret allergen-specific IgE testing (skin or blood) when empiric treatment fails, the diagnosis is uncertain, or identifying a causal allergen will change avoidance or immunotherapy decisions; interpret sensitization only in the context of exposure and symptoms because a positive test without clinical correlation is not synonymous with disease. Do NOT routinely order sinus CT for a straightforward AR presentation, and do not use food-allergy panels as a routine rhinitis workup. If classic allergy symptoms persist despite negative systemic testing, do not automatically call the patient 'nonallergic'—consider LAR and other nonallergic phenotypes."
        ),
        "manage": (
            "Match therapy to the dominant symptom and disease burden. Intranasal corticosteroid is preferred monotherapy for persistent or quality-of-life-limiting AR; correct spray technique and adherence before declaring failure. Second-generation oral antihistamines are useful when itching and sneezing dominate, while an intranasal antihistamine is an effective topical option. For inadequate control, combined intranasal corticosteroid plus intranasal antihistamine has additive efficacy. Saline irrigation and targeted exposure reduction can be adjuncts when a relevant trigger is known. Do not use montelukast as routine first-line AR monotherapy, avoid depot systemic corticosteroid injections, and limit topical decongestants because of rebound congestion risk."
        ),
        "operate": (
            "Escalation in AR is usually IMMUNOLOGIC before surgical. Offer or refer for allergen immunotherapy when there is documented clinically relevant sensitization and symptoms remain inadequately controlled with medication/environmental measures, medication is poorly tolerated, or the patient values disease-modifying treatment; the 2024 inhalant-allergy guideline emphasizes selecting allergens that correlate with history and testing and using shared decision-making between SCIT and appropriate SLIT options. Surgery does not cure IgE sensitization. Inferior-turbinate reduction is reasonable for persistent nasal airway obstruction with enlarged turbinates after adequate medical therapy, and septoplasty addresses a true structural component—not the allergic mechanism itself."
        ),
        "teach": (
            "Chief/boards framework: conventional AR = COMPATIBLE PHENOTYPE + clinically relevant SYSTEMIC IgE sensitization when testing is needed. Start with history and exam; test when uncertainty, treatment failure or immunotherapy planning makes the result actionable; do not obtain routine imaging. Persistent disease: INTRANASAL CORTICOSTEROID is the anchor; add intranasal antihistamine when needed. Immunotherapy requires a causal allergen, not merely a positive panel. Most importantly, a negative skin test/serum sIgE does not prove the symptoms are nonallergic—an AR-like phenotype with negative systemic testing is exactly where LOCAL allergic rhinitis enters the differential."
        ),
        "tags": [
            "allergic rhinitis", "systemic sensitization", "specific IgE", "skin-prick testing",
            "intranasal corticosteroid", "intranasal antihistamine", "allergen immunotherapy",
            "inferior turbinate hypertrophy", "rhinitis differential"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — allergic rhinitis pathophysiology, diagnosis, differential diagnosis, and management",
            "K.J. Lee's Essential Otolaryngology, 12e — allergic rhinitis presentation, allergy testing, and medical treatment",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — rhinologic allergy evaluation and treatment pearls",
            "AAO-HNSF Clinical Practice Guideline: Allergic Rhinitis, 2015 — diagnosis, selective specific-IgE testing, avoidance of routine imaging, intranasal steroids, antihistamines, immunotherapy, and turbinate reduction",
            "Dykewicz et al., J Allergy Clin Immunol 2020 — Rhinitis 2020 practice parameter: INCS-preferred persistent AR therapy, INCS + intranasal antihistamine combination, and pharmacologic safety",
            "AAO-HNSF Clinical Practice Guideline: Immunotherapy for Inhalant Allergy, 2024 — evidence-based candidacy and delivery principles for inhalant allergen immunotherapy",
        ],
    },
    "local allergic rhinitis": {
        "recognize": (
            "Recognize LOCAL ALLERGIC RHINITIS (LAR) when the patient has a reproducible allergic-rhinitis phenotype—classically sneezing, itching, watery rhinorrhea and congestion with suspected aeroallergen exposure—but standard skin-prick testing and serum specific-IgE are negative. LAR is not simply a synonym for idiopathic/nonallergic rhinitis and should not be diagnosed from symptoms alone. The conceptual clue is a patient who behaves clinically 'allergic' while conventional systemic sensitization testing does not explain the phenotype."
        ),
        "localize": (
            "Localize LAR to a NASAL mucosal allergen-specific immune response without demonstrable systemic atopy by routine skin/serum testing. Local production of allergen-specific IgE and a type-2 inflammatory response can occur within the target organ, so a negative systemic test does not exclude an allergen-driven nasal reaction. Keep LAR separate from conventional AR (systemic sensitization present), nonallergic rhinopathy/vasomotor rhinitis (no demonstrated allergen-specific mechanism), NARES/eosinophilic phenotypes, medication/hormonal rhinitis and chronic rhinosinusitis. 'Dual allergic rhinitis' describes conventional systemic AR to some allergens plus a local allergic response to additional allergens."
        ),
        "workup": (
            "First confirm that routine systemic testing is genuinely negative for allergens suggested by the history and exclude structural disease, chronic rhinosinusitis and major nonallergic mimics. Where specialty testing is available, a controlled NASAL ALLERGEN CHALLENGE/PROVOCATION TEST demonstrating a reproducible local response is the reference method used to establish LAR in contemporary literature. Nasal allergen-specific IgE can support local sensitization, but limited sensitivity and lack of broad standardization mean a negative nasal sIgE assay does not exclude LAR. Do not diagnose LAR merely because symptoms respond to an antihistamine or steroid; treatment response is nonspecific."
        ),
        "manage": (
            "Treat the symptomatic nasal phenotype with the same high-value topical tools used for other inflammatory rhinitis: intranasal corticosteroid for persistent inflammatory symptoms and/or an intranasal antihistamine, with combination topical therapy when monotherapy is inadequate. Saline and exposure reduction are reasonable adjuncts when a reproducible culprit is identified. The diagnostic distinction still matters because it prevents the false conclusion that all negative systemic allergy testing equals nonallergic rhinitis and because it can influence specialist counseling and consideration of allergen-directed therapy."
        ),
        "operate": (
            "LAR itself has no operation; procedure selection should target a separate structural problem rather than the local IgE mechanism. Allergen immunotherapy for carefully confirmed LAR is an evolving specialist strategy: controlled studies, particularly with grass pollen and house-dust-mite sensitization, suggest benefit, but the evidence base and routine testing infrastructure are substantially less mature than for conventional systemic AR. Do not launch empiric SCIT/SLIT from symptoms plus negative systemic testing alone. If surgery is contemplated for obstruction, document the independent anatomic indication and continue to manage the inflammatory rhinitis phenotype."
        ),
        "teach": (
            "Chief/boards framework: LAR = ALLERGIC PHENOTYPE + NEGATIVE routine systemic sensitization + POSITIVE local nasal allergen response when formally confirmed. The trap is equating negative skin/serum testing with 'nonallergic rhinitis.' Conventional AR is systemically test-positive; LAR is locally allergen-responsive; idiopathic/nonallergic rhinopathy lacks proof of allergen-specific activation. Nasal allergen challenge is the key confirmatory concept, while nasal sIgE is supportive but not sufficiently sensitive to stand alone. Immunotherapy is promising in confirmed LAR but is not the same evidence-standard pathway as immunotherapy for conventional AR."
        ),
        "tags": [
            "local allergic rhinitis", "LAR", "nasal allergen challenge", "nasal provocation test",
            "nasal specific IgE", "negative skin testing", "negative serum IgE", "dual allergic rhinitis",
            "nonallergic rhinitis differential"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — rhinitis phenotypes, nasal allergy mechanisms, differential diagnosis, and management",
            "K.J. Lee's Essential Otolaryngology, 12e — allergic and nonallergic rhinitis evaluation and treatment framework",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — rhinitis differential diagnosis and topical treatment principles",
            "Dykewicz et al., J Allergy Clin Immunol 2020 — Rhinitis 2020 practice parameter, including local allergic rhinitis and distinction from nonallergic rhinitis",
            "Campo & Canonica, J Allergy Clin Immunol Pract 2024 — contemporary definition of LAR as an AR phenotype with negative systemic IgE testing and positive nasal allergen challenge",
            "AAO-HNSF Clinical Practice Guideline: Immunotherapy for Inhalant Allergy, 2024 — conventional inhalant-allergy immunotherapy framework used to distinguish established AR candidacy from evolving LAR-specific evidence",
        ],
    },
}


def apply_rhinology_rhinitis_rebuild_v285(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = RHINITIS_REBUILD_V285.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v285"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
