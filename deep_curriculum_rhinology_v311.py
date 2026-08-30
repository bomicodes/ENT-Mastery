"""v31.1 — source-grounded Allergic Rhinitis vs Local Allergic Rhinitis rebuild.

The two cards intentionally perform different jobs:
- Allergic Rhinitis owns classic systemic IgE-mediated diagnosis, severity assessment,
  evidence-based pharmacotherapy, testing, and allergen immunotherapy selection.
- Local Allergic Rhinitis owns the difficult-rhinitis phenotype with negative systemic
  sensitization testing, nasal allergen challenge confirmation, and the limits of
  currently available local-IgE testing and treatment evidence.

Applied at the production entrypoint after generated curriculum load and before
Concept Check regeneration.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")
DOMAIN = "Rhinology / Allergy / Skull Base"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


REBUILD_V311 = {
    "allergic rhinitis": {
        "recognize": (
            "Recognize classic allergic rhinitis (AR) as an allergen-triggered, IgE-mediated nasal disease. The high-yield symptom cluster is sneezing, nasal itching, clear anterior/posterior rhinorrhea, and congestion, often with itchy/watery eyes. History must connect symptoms to plausible exposure; a positive skin or serum test proves sensitization, not by itself clinically relevant allergy. Classify burden by intermittent versus persistent symptoms and by effect on sleep, school/work, exercise, and quality of life rather than relying only on the old seasonal/perennial labels. Asthma, conjunctivitis, atopic dermatitis, and other type-2 disease frequently coexist, so AR is part of a unified-airway assessment rather than an isolated nose diagnosis."
        ),
        "localize": (
            "Use phenotype and exposure pattern to identify the inflammatory compartment and distinguish AR from mimics. Pale/edematous mucosa and watery secretions support allergy but are not diagnostic. Unilateral obstruction, recurrent epistaxis, purulence, severe facial pain, a mass, or CSF-like unilateral watery drainage should redirect the workup away from routine AR. Medication effects, rhinitis medicamentosa, infectious rhinitis, nonallergic rhinopathy, hormonal/drug-induced rhinitis, occupational disease, CRS, structural obstruction, and local allergic rhinitis belong in the differential. Classic AR is defined by systemic evidence of relevant allergen sensitization; if the history is strongly allergen-patterned but skin-prick and serum allergen-specific IgE testing are negative, do not simply relabel the patient 'nonallergic'—that discordant phenotype belongs to the separate Local Allergic Rhinitis card."
        ),
        "workup": (
            "Start with history plus focused nasal/ocular examination. Perform allergy testing when the diagnosis is uncertain, empiric treatment fails, or identifying a culprit will change avoidance or immunotherapy decisions. Skin-prick testing and serum allergen-specific IgE are the standard systemic sensitization tools; interpret only allergens that fit the exposure history. Routine total IgE, broad indiscriminate food panels, sinus CT, or nasal cultures do not diagnose uncomplicated AR. Nasal endoscopy is appropriate when structural disease, polyps, chronic rhinosinusitis, unilateral findings, bleeding, or another diagnosis is suspected. ICAR-AR 2023 emphasizes that symptoms plus clinically relevant sensitization establish the diagnosis; sensitization without exposure-linked symptoms is not equivalent to AR."
        ),
        "manage": (
            "Match treatment to symptom burden and patient goals. Allergen avoidance is useful when a specific, feasible exposure intervention exists, but avoidance alone is rarely enough for persistent disease. Intranasal corticosteroids are the most effective single medication for overall nasal symptom control; technique and adherence matter. Second-generation oral or intranasal antihistamines are useful especially for itching/sneezing/rhinorrhea; intranasal antihistamine plus intranasal steroid provides greater control when monotherapy is inadequate. Saline irrigation is a low-risk adjunct. Avoid routine first-generation sedating antihistamines and prolonged topical decongestants because of cognitive/anticholinergic effects and rhinitis medicamentosa, respectively. Treat coexisting asthma and ocular disease as part of the same airway phenotype."
        ),
        "operate": (
            "Escalation in AR is immunologic or anatomy-directed—not 'sinus surgery for allergy.' Offer allergen immunotherapy (SCIT or evidence-supported SLIT products) to appropriately selected patients with clinically relevant sensitization whose symptoms remain important despite avoidance/pharmacotherapy, who prefer disease-modifying treatment, or who wish to reduce long-term medication burden; counsel regarding time commitment and systemic-reaction risk. Inferior turbinate reduction can improve persistent obstructive symptoms from hypertrophy after optimized medical therapy but does not treat the underlying allergic sensitization. Septoplasty addresses structural obstruction, not AR itself. Refractory watery rhinorrhea may prompt evaluation for additional rhinitis phenotypes and selected posterior nasal nerve-directed therapy rather than escalating allergy medication indefinitely."
        ),
        "teach": (
            "Boards/rounds framework: SYMPTOMS + RELEVANT SYSTEMIC SENSITIZATION = classic AR. A positive skin test without matching symptoms/exposure is sensitization, not necessarily disease. First-line high-value therapy for persistent global nasal symptoms is an intranasal corticosteroid; add/integrate intranasal antihistamine when control is inadequate. Immunotherapy requires a clinically relevant allergen target. CT does not diagnose AR and surgery does not cure allergy. The discriminator from Local Allergic Rhinitis is systemic testing: classic AR has relevant skin-prick and/or serum specific-IgE evidence, whereas LAR presents with an allergy-like history despite negative systemic sensitization tests and requires a different diagnostic pathway."
        ),
        "tags": ["allergic rhinitis", "IgE", "skin prick testing", "specific IgE", "intranasal corticosteroid", "intranasal antihistamine", "allergen immunotherapy", "SCIT", "SLIT", "unified airway"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — allergic rhinitis, nasal allergy evaluation, and medical/immunologic management",
            "K.J. Lee's Essential Otolaryngology, 12e — rhinology/allergy evaluation and allergic rhinitis management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Allergy and Rhinitis chapter",
            "International Consensus Statement on Allergy and Rhinology: Allergic Rhinitis 2023 (ICAR-AR 2023)"
        ],
    },
    "local allergic rhinitis": {
        "recognize": (
            "Recognize local allergic rhinitis (LAR) when the clinical story behaves like allergy—reproducible sneezing, itching, watery rhinorrhea and/or congestion with a plausible aeroallergen exposure—but standard skin-prick testing and serum allergen-specific IgE show no systemic sensitization. LAR reflects a localized nasal allergic response and should not be used as a synonym for generic nonallergic/vasomotor rhinitis. The phenotype can occur in adults and children and may coexist with asthma or conjunctival symptoms. The key resident-level clue is DISCORDANCE: a compelling allergen-linked history with negative conventional systemic allergy tests."
        ),
        "localize": (
            "Localize the diagnostic problem to the nasal mucosa rather than assuming an occult systemic allergy. LAR has evidence of local type-2/allergic reactivity despite absent systemic atopy on conventional testing. Differentiate it from nonallergic rhinopathy, which is more often provoked by temperature change, odors, smoke, irritants, exercise, foods/alcohol, or nonspecific autonomic triggers and lacks a reproducible allergen-specific nasal response. Also exclude medication-related disease, rhinitis medicamentosa, CRS, occupational rhinitis, structural obstruction, and other unilateral/red-flag processes. Mixed phenotypes exist, so one irritant trigger does not exclude local allergy."
        ),
        "workup": (
            "Do not diagnose LAR solely because skin and serum testing are negative. First document a convincing allergic-pattern history and negative systemic sensitization testing to the suspected allergen(s). When confirmation will change management and expertise/testing is available, nasal allergen challenge/provocation is the reference diagnostic test: reproduction of objective and symptom responses to a specific nasal allergen supports LAR. The AAAAI Rhinitis, Rhinosinusitis and Ocular Allergy Committee work-group recognizes nasal allergen challenge as a diagnostic application for LAR, while also noting that protocols and availability vary. Nasal allergen-specific IgE and basophil activation testing can support local allergy in research/specialty settings, but sensitivity and standardization are insufficient for them to replace a properly performed challenge in routine practice."
        ),
        "manage": (
            "Treat confirmed or strongly suspected LAR initially with the same symptom-directed tools that work for AR: intranasal corticosteroid, intranasal or second-generation oral antihistamine as appropriate, saline, and targeted exposure reduction when a reproducible culprit is known. The diagnostic label matters because it prevents an allergy-pattern patient with negative systemic testing from being dismissed as nonspecific 'vasomotor rhinitis.' Reassess technique, adherence, structural disease, CRS, and mixed triggers when symptoms remain uncontrolled. Unlike classic AR, do not select an immunotherapy allergen simply from a positive systemic test—the systemic test is negative by definition, so treatment must be anchored to convincingly demonstrated local allergen relevance."
        ),
        "operate": (
            "LAR rarely creates an operative indication by itself. Procedures should target a separate anatomic or symptom mechanism: turbinate reduction for persistent hypertrophic obstruction after optimized medical therapy, septoplasty for structural obstruction, or selected posterior nasal nerve-directed treatment for refractory chronic rhinorrhea after phenotype reassessment. Allergen immunotherapy for LAR is an evolving specialty area: trials suggest benefit in selected challenge-confirmed patients, but the evidence base and product/selection framework are less mature than for conventional systemic-sensitization AR. Treat it as an individualized allergy-specialist decision rather than a universal boards-level standard."
        ),
        "teach": (
            "Boards/rounds discriminator: ALLERGY-LIKE HISTORY + NEGATIVE SKIN/SERUM sIgE does not automatically equal nonallergic rhinitis. Think LAR when exposure specificity is persuasive; confirm with nasal allergen challenge when the result will matter and testing is available. Do not call isolated nasal IgE a universally standardized gold-standard clinical test, and do not infer LAR from negative systemic tests alone. Classic AR and LAR share symptoms and local type-2 biology, but their diagnostic evidence differs: AR demonstrates relevant systemic sensitization; LAR demonstrates allergen-specific nasal reactivity without conventional systemic sensitization."
        ),
        "tags": ["local allergic rhinitis", "LAR", "nasal allergen challenge", "nasal allergen provocation", "negative skin testing", "negative serum specific IgE", "nasal IgE", "nonallergic rhinitis differential"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — rhinitis differential diagnosis and allergy evaluation",
            "K.J. Lee's Essential Otolaryngology, 12e — rhinology/allergy evaluation and chronic rhinitis differential",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Allergy and Rhinitis chapter",
            "International Consensus Statement on Allergy and Rhinology: Allergic Rhinitis 2023 (ICAR-AR 2023)",
            "AAAAI Rhinitis, Rhinosinusitis and Ocular Allergy Committee Work Group Report: Nasal allergen challenge, J Allergy Clin Immunol 2023"
        ],
    },
}


def apply_rhinitis_rebuild_v311(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = REBUILD_V311.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v311"] = True
        module["semantic_role_v311"] = (
            "classic systemic IgE-mediated allergic rhinitis diagnosis and treatment"
            if key == "allergic rhinitis"
            else "systemic-test-negative but allergen-reactive nasal phenotype requiring local confirmation"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
