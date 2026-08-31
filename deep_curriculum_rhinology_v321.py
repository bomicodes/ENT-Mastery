"""v32.1 — source-grounded allergic rhinitis versus local allergic rhinitis rebuild.

Keeps conventional systemic IgE-mediated allergic rhinitis as the broad disease/therapy
framework while making local allergic rhinitis (LAR) an advanced diagnostic phenotype:
allergic symptoms with negative systemic sensitization but demonstrable local nasal
allergen reactivity. The intent is to prevent LAR from collapsing into either generic AR
or the nonallergic-rhinitis exclusion bucket.
"""

import re

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


RHINITIS_REBUILD_V321 = {
    "allergic rhinitis": {
        "recognize": (
            "Recognize conventional ALLERGIC RHINITIS (AR) as exposure-linked IgE-mediated nasal inflammation producing some combination of sneezing, nasal itching, clear rhinorrhea and congestion, often with ocular itching/tearing and an atopic history. Seasonal versus perennial labels describe exposure pattern; intermittent/persistent symptoms and severity describe clinical burden. Pale or edematous turbinates can support the phenotype but are not diagnostic. A convincing history matters because sensitization on skin or serum testing without symptom correlation is not the same as clinically relevant allergy."
        ),
        "localize": (
            "Localize the problem immunologically and anatomically. In classic AR, clinically relevant aeroallergen sensitization is demonstrable systemically by skin-prick testing or serum allergen-specific IgE when testing is indicated. Also identify the dominant symptom compartment—itch/sneeze, watery rhinorrhea, obstruction, ocular symptoms—and comorbid asthma, conjunctivitis, sleep disturbance or sinus disease because these change treatment priorities. Do not force every chronic rhinitis patient into this card: if allergic symptoms persist despite NEGATIVE skin testing and serum specific IgE, consider LOCAL ALLERGIC RHINITIS before labeling the patient nonallergic; if triggers are odors, temperature, eating or medication without allergen-specific biology, pursue the nonallergic-rhinitis pathway."
        ),
        "workup": (
            "AR is primarily a clinical diagnosis. Obtain skin-prick testing or serum allergen-specific IgE when the diagnosis is uncertain, empiric treatment fails, or defining the relevant allergen will change avoidance or immunotherapy. Interpret testing against the exposure history rather than treating every positive result. Routine food-allergy panels, sinus CT, nasal cytology and broad laboratory testing are not part of uncomplicated AR evaluation. Examine for structural obstruction, polyps, purulence, unilateral disease and medication-related rhinitis when the course is atypical. Ask about asthma symptoms before immunotherapy and before assuming upper-airway treatment alone is sufficient."
        ),
        "manage": (
            "Match treatment to burden and dominant symptoms. For persistent AR, an INTRANASAL CORTICOSTEROID is preferred foundational monotherapy; correct spray direction away from the septum and adherence often matter more than switching molecules. Second-generation oral or intranasal antihistamines are useful for itch/sneeze/rhinorrhea; an intranasal antihistamine plus intranasal steroid provides additional benefit when monotherapy is inadequate. Ipratropium is symptom-directed for refractory watery rhinorrhea. Montelukast is not preferred first-line AR therapy and should generally be reserved for inadequate response/intolerance to alternatives or selected patients with concomitant asthma. Limit topical decongestants because of rebound-risk and avoid depot parenteral corticosteroids for routine AR. Use allergen-reduction measures when a specific clinically relevant exposure is identified rather than prescribing burdensome generic avoidance lists."
        ),
        "operate": (
            "There is no operation that treats the IgE mechanism of AR. Surgery is reserved for a SEPARATE structural problem—such as clinically important septal deviation or inferior-turbinate hypertrophy that remains obstructive despite appropriate medical therapy—and should be counseled as treatment of airflow obstruction, not a cure for allergy. For disease modification, offer or refer for ALLERGEN IMMUNOTHERAPY when symptoms remain inadequately controlled with medical therapy/avoidance or the patient prefers immunomodulation, using only allergens that are clinically relevant and confirmed by appropriate testing. Before AIT, assess asthma control and safety; uncontrolled asthma is a major contraindication to initiation."
        ),
        "teach": (
            "Chief/boards framework: CLASSIC AR = ALLERGIC SYMPTOMS + CLINICALLY RELEVANT SYSTEMIC SENSITIZATION when testing is needed. History decides whether a positive test matters. Persistent disease: intranasal steroid first; add an intranasal antihistamine when needed, rather than reflexively stacking oral agents. AIT is disease-modifying for appropriately selected, test-confirmed inhalant allergy. The deliberate boundary is LOCAL AR: allergic symptoms with negative skin/serum testing require a local nasal-allergy question, not an automatic diagnosis of nonallergic rhinitis."
        ),
        "tags": ["allergic rhinitis", "IgE", "skin prick testing", "serum specific IgE", "intranasal corticosteroid", "intranasal antihistamine", "allergen immunotherapy", "SCIT", "SLIT"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — allergic-rhinitis pathophysiology, differential diagnosis, testing, and medical management framework",
            "K.J. Lee's Essential Otolaryngology, 12e — allergy testing, rhinitis pharmacotherapy, local nasal IgE, and immunotherapy",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — allergic response, rhinitis differential, intranasal therapy, and immunotherapy pearls",
            "Rhinitis 2020 Practice Parameter Update — diagnosis, preferred intranasal therapy, combination therapy, local AR, and medication safety",
            "AAO-HNSF Clinical Practice Guideline: Immunotherapy for Inhalant Allergy, 2024 — candidacy, asthma/safety screening, clinically relevant allergen selection, and treatment duration",
        ],
    },
    "local allergic rhinitis": {
        "recognize": (
            "Recognize LOCAL ALLERGIC RHINITIS (LAR, historically 'entopy') when the phenotype LOOKS allergic—reproducible sneezing, itching, watery rhinorrhea and/or congestion after a plausible aeroallergen exposure—but conventional systemic testing is negative. LAR is not simply 'mild AR' and is not synonymous with idiopathic/vasomotor rhinitis: the defining concept is a LOCAL nasal type-2/IgE-mediated response without demonstrable systemic sensitization by standard skin-prick or serum specific-IgE testing."
        ),
        "localize": (
            "Localize the immune response to the NASAL MUCOSA. The boards-level discriminator is: classic AR has clinically relevant systemic sensitization; LAR has negative systemic sensitization but reproducible local allergen reactivity; nonallergic rhinitis lacks evidence that a specific allergen is driving either systemic or local IgE-mediated disease. NARES can also have negative systemic allergy testing but is defined by prominent nasal eosinophilia rather than a positive allergen-specific nasal challenge. Mixed phenotypes exist, so a negative skin test should trigger phenotype refinement rather than a reflex label."
        ),
        "workup": (
            "Suspect LAR only after a careful exposure-linked allergic history and appropriately performed NEGATIVE skin-prick and serum allergen-specific IgE testing. NASAL ALLERGEN PROVOCATION/PROVOCATION TESTING is the key confirmatory reference method in expert practice: a relevant allergen reproduces symptoms with an objective nasal response. Nasal allergen-specific IgE can support local sensitization, but collection/assay methods and normative thresholds are less standardized, so a negative nasal-sIgE assay does not reliably exclude LAR and it should not replace a well-performed provocation test. Nasal cytology may help identify NARES but does not by itself diagnose LAR. Availability of nasal provocation is limited, so referral to an allergy/rhinology center may be necessary when confirmation would change management."
        ),
        "manage": (
            "Treat symptomatic LAR initially with the same evidence-based topical principles used for allergic nasal inflammation—intranasal corticosteroid, intranasal antihistamine when appropriate, saline and targeted avoidance of an identified provoking allergen—while preserving the diagnostic distinction. Do not prescribe allergen avoidance or immunotherapy from an uncorrelated environmental panel when systemic tests are negative. The management-changing value of confirming LAR is that a SPECIFIC provoking allergen can be identified rather than leaving the patient in a nonspecific 'nonallergic' bucket."
        ),
        "operate": (
            "LAR has no primary surgical treatment. Operate only on an independently demonstrated structural contributor to obstruction, with the same counseling used in conventional AR that surgery changes anatomy rather than the mucosal immune phenotype. ALLERGEN IMMUNOTHERAPY for confirmed LAR is promising and supported by a small body of randomized trials/meta-analysis, especially SCIT in carefully selected patients, but the evidence base is far smaller and shorter-term than for conventional systemic-sensitization AR. Teach it as a specialist option after objective allergen confirmation—not as an automatic standard for every patient with negative skin testing."
        ),
        "teach": (
            "Chief/boards discriminator: ALLERGIC SYMPTOMS + NEGATIVE SKIN/SERUM IgE does NOT automatically equal nonallergic rhinitis. Ask whether there is demonstrable LOCAL allergen reactivity. LAR = negative systemic sensitization + positive/reproducible nasal allergen response; nasal sIgE may support but is not a universally standardized standalone rule-out test. NARES = negative systemic tests + nasal eosinophilia, not necessarily allergen-specific reactivity. Treat symptoms topically, and reserve allergen-specific immunotherapy discussion for objectively confirmed, specialist-selected LAR because its evidence base is promising but less mature than conventional AR."
        ),
        "tags": ["local allergic rhinitis", "LAR", "entopy", "nasal allergen provocation", "nasal specific IgE", "negative skin testing", "nonallergic rhinitis differential", "NARES"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — allergic/nonallergic rhinitis framework and objective nasal-testing context",
            "K.J. Lee's Essential Otolaryngology, 12e — local allergic rhinitis, nasal provocation testing, and nasal specific IgE",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — allergic versus nonallergic rhinitis differential and topical management",
            "Rhinitis 2020 Practice Parameter Update — contemporary recognition of local allergic rhinitis within the chronic-rhinitis differential",
            "Hoang et al., Rhinology 2022 systematic review/meta-analysis — limited but positive evidence for allergen-specific immunotherapy in LAR",
            "Tan & Tan 2025 review — current diagnostic emphasis on negative systemic sensitization with positive nasal provocation",
        ],
    },
}


def apply_rhinology_allergic_rebuild_v321(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = RHINITIS_REBUILD_V321.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v321"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
