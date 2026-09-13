"""v20.31 — learner-facing Concept Checks for Allergic Rhinitis and Local Allergic Rhinitis.

The canonical Deep Curriculum cards are already clinically strong and source-grounded. This
cohort fills the learner-path gap exposed by the v31.2 audit: neither exact canonical topic had a
matching Concept Check. It adds two free-response resident-level cases without creating or
renaming any Deep Curriculum topic.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"

AR_ID = "v6-rhinology-allergy-skull-base-allergic-rhinitis-ar"
LAR_ID = "v6-rhinology-allergy-skull-base-local-allergic-rhinitis-lar"

CORE_TEXTBOOKS = [
    {
        "type": "textbook",
        "citation": "Cummings Otolaryngology–Head and Neck Surgery, 7th ed. (2021), connected Google Drive full-volume copy ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t. Cross-referenced for allergic-rhinitis pathophysiology, diagnostic testing, medical therapy, immunotherapy principles, and structural-versus-inflammatory decision-making.",
    },
    {
        "type": "textbook",
        "citation": "Pasha R, Golub JS. Otolaryngology–Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Cross-referenced for practical allergic-rhinitis diagnosis, testing, pharmacotherapy, and immunotherapy teaching.",
    },
    {
        "type": "textbook",
        "citation": "K.J. Lee's Essential Otolaryngology, 12th ed. (2019), connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Cross-referenced for durable rhinology/allergy examination, testing, medical-management, and operative-boundary principles.",
    },
]

AR_SOURCES = CORE_TEXTBOOKS + [
    {
        "type": "guideline",
        "citation": "Seidman MD, et al. Clinical Practice Guideline: Allergic Rhinitis. Otolaryngol Head Neck Surg. 2015;152(1 Suppl):S1-S43. DOI 10.1177/0194599814561600. AAO-HNSF guidance for diagnosis, clinically relevant allergy testing, intranasal steroids, antihistamines, immunotherapy referral, and avoiding routine sinonasal imaging for uncomplicated AR.",
    },
    {
        "type": "consensus",
        "citation": "Wise SK, et al. International Consensus Statement on Allergy and Rhinology: Allergic Rhinitis – 2023. Int Forum Allergy Rhinol. 2023. DOI 10.1002/alr.23090. Current evidence synthesis for AR phenotypes, diagnosis, testing, pharmacotherapy, immunotherapy, and procedural boundaries.",
    },
    {
        "type": "guideline",
        "citation": "Gurgel RK, et al. Clinical Practice Guideline: Immunotherapy for Inhalant Allergy. Otolaryngol Head Neck Surg. 2024;170(S1):S1-S42. DOI 10.1002/ohn.648. Supports allergen immunotherapy for appropriately selected patients with clinically relevant inhalant allergy and emphasizes anaphylaxis readiness and evidence-based AIT delivery.",
    },
]

LAR_SOURCES = CORE_TEXTBOOKS + [
    {
        "type": "consensus",
        "citation": "Wise SK, et al. International Consensus Statement on Allergy and Rhinology: Allergic Rhinitis – 2023. Int Forum Allergy Rhinol. 2023. DOI 10.1002/alr.23090. Includes local allergic mechanisms/phenotypes and distinguishes clinical allergy from systemic sensitization alone.",
    },
    {
        "type": "position_paper",
        "citation": "Augé J, et al. EAACI Position paper on the standardization of nasal allergen challenges. Allergy. 2018;73(8):1597-1608. DOI 10.1111/all.13416. Nasal allergen challenge is an established tool for suspected local allergic rhinitis when history suggests allergy despite negative systemic testing.",
    },
    {
        "type": "guideline",
        "citation": "Gurgel RK, et al. Clinical Practice Guideline: Immunotherapy for Inhalant Allergy. Otolaryngol Head Neck Surg. 2024;170(S1):S1-S42. DOI 10.1002/ohn.648. Used for contemporary immunotherapy safety and patient-selection boundaries; evidence for LAR-specific AIT should be individualized rather than assumed from systemic sensitization guidance.",
    },
]

CHECKS = [
    {
        "id": "cc-v231-rhinology-allergic-rhinitis-ar",
        "domain": DOMAIN,
        "topic": "Allergic Rhinitis",
        "canonical_topic": "Allergic Rhinitis",
        "concept_id": AR_ID,
        "prompt": "A 24-year-old with allergic rhinitis (hay fever), including seasonal allergic rhinitis or perennial allergic rhinitis, has sneezing, nasal itching, clear rhinorrhea, and congestion that track with cat exposure. What testing is actually useful, what is first-line controller therapy, when should allergen immunotherapy enter the plan, and when would nasal surgery be addressing a different problem rather than the allergy itself?",
        "question": "A 24-year-old with allergic rhinitis (hay fever), including seasonal allergic rhinitis or perennial allergic rhinitis, has sneezing, nasal itching, clear rhinorrhea, and congestion that track with cat exposure. What testing is actually useful, what is first-line controller therapy, when should allergen immunotherapy enter the plan, and when would nasal surgery be addressing a different problem rather than the allergy itself?",
        "choices": [],
        "answer": None,
        "answer_text": """### Allergic rhinitis — connect the symptom pattern to clinically relevant IgE, then treat the inflammatory disease

**Testing should answer a clinical question.** Allergic rhinitis is an IgE-mediated nasal inflammatory disorder; a compatible exposure-linked history is the starting point. Use skin-prick testing or serum allergen-specific IgE when the diagnosis is uncertain, empiric treatment has failed, or identifying a clinically relevant allergen would change avoidance or immunotherapy decisions. A positive test proves sensitization, not causation: the result must fit the history. Routine broad panels and routine sinus CT do not improve an otherwise straightforward allergic-rhinitis diagnosis.

**Intranasal corticosteroid therapy is the core controller for persistent or congestion-predominant disease.** Technique and adherence matter. Second-generation oral or intranasal antihistamines are useful especially for itching and sneezing; saline and targeted exposure reduction can be adjuncts. Avoid turning topical decongestants into chronic therapy because rebound rhinitis can create a second problem.

**Immunotherapy is a disease-modifying option, not the next automatic step after a positive test.** Consider SCIT or appropriate SLIT when symptoms remain important despite avoidance/pharmacotherapy, when the patient prefers a disease-modifying strategy, or when medication burden is problematic, provided the clinically relevant allergen is identified and safety considerations are addressed. The 2024 inhalant-allergy guideline emphasizes appropriate patient selection and the ability to recognize and manage anaphylaxis.

**Surgery does not treat IgE-mediated inflammation.** Septoplasty, turbinate surgery, nasal-valve surgery, or other procedures may be reasonable for a separately demonstrated structural obstruction after medical optimization, but a positive allergy test is not a surgical indication and surgery should not be presented as curing allergic rhinitis. Senior decision-making separates the inflammatory target from coexisting anatomy rather than using one to explain the other.
""",
        "search_aliases": ["allergic rhinitis", "hay fever", "seasonal allergic rhinitis", "perennial allergic rhinitis", "AR"],
        "source_refs_v230": AR_SOURCES,
        "evidence_distinction_v231": "Durable textbook principles define IgE-mediated disease, exam, and structural boundaries. AAO-HNSF AR guidance anchors testing and first-line treatment; ICAR-AR 2023 provides the broader current evidence synthesis; the 2024 inhalant-allergy CPG updates immunotherapy selection and safety.",
        "learner_experience_v231": {"deep_curriculum": True, "concept_check": True, "daily_curriculum": True, "sources_visible": True},
    },
    {
        "id": "cc-v231-rhinology-local-allergic-rhinitis-lar",
        "domain": DOMAIN,
        "topic": "Local Allergic Rhinitis",
        "canonical_topic": "Local Allergic Rhinitis",
        "concept_id": LAR_ID,
        "prompt": "A 31-year-old has reproducible pollen-triggered sneezing, itching, watery rhinorrhea, and congestion with negative skin testing and negative serum IgE. How should you reason through local allergic rhinitis (LAR), also called localized allergic rhinitis or entopy, what test can establish local allergen reactivity, and what should negative systemic testing not make you do?",
        "question": "A 31-year-old has reproducible pollen-triggered sneezing, itching, watery rhinorrhea, and congestion with negative skin testing and negative serum IgE. How should you reason through local allergic rhinitis (LAR), also called localized allergic rhinitis or entopy, what test can establish local allergen reactivity, and what should negative systemic testing not make you do?",
        "choices": [],
        "answer": None,
        "answer_text": """### Local allergic rhinitis — negative systemic testing does not automatically mean nonallergic rhinitis

**Local allergic rhinitis (LAR) is a clinical phenotype in which allergic-type symptoms and local nasal allergen reactivity can occur despite negative skin testing and negative serum specific IgE.** The key senior-resident move is to preserve the phenotype in the differential instead of relabeling every systemically test-negative patient as nonallergic rhinitis.

**Recheck the history and competing phenotypes first.** Confirm reproducible allergen-linked symptoms and distinguish medication effects, irritant/vasomotor nonallergic rhinitis, NARES/eosinophilic disease, chronic rhinosinusitis, and structural obstruction. Systemic skin or serum testing still helps define whether conventional systemic sensitization is present, but negative results do not exclude LAR.

**Nasal allergen challenge/provocation is the reference clinical tool for demonstrating local allergen reactivity when the distinction matters.** EAACI standardized nasal allergen challenge methodology and specifically includes local allergic rhinitis among its diagnostic indications. This is generally a specialist-level test rather than a reason to repeat progressively broader serum panels.

**Management follows the demonstrated phenotype and the patient's burden.** Intranasal corticosteroid and/or antihistamine therapy is reasonable for allergic-pattern nasal inflammation. Allergen immunotherapy for LAR has a smaller and less standardized evidence base than conventional systemic-sensitization AR, so selection should be individualized in an allergy/rhinology setting rather than inferred from a negative blood test alone. Most importantly, negative systemic allergy testing is not a shortcut to surgery: septal deviation, turbinate hypertrophy, or nasal-valve dysfunction still requires its own anatomic diagnosis and indication, and surgery does not establish or erase local allergic disease.
""",
        "search_aliases": ["local allergic rhinitis", "localized allergic rhinitis", "LAR", "entopy", "negative skin testing", "negative serum IgE", "nasal allergen challenge"],
        "source_refs_v230": LAR_SOURCES,
        "evidence_distinction_v231": "Textbooks provide durable allergic-rhinitis physiology and differential diagnosis. ICAR-AR 2023 supports the local-versus-systemic allergy framework; EAACI provides the standardized nasal allergen challenge method. LAR-specific immunotherapy evidence is kept separate from the stronger general AIT guideline evidence.",
        "learner_experience_v231": {"deep_curriculum": True, "concept_check": True, "daily_curriculum": True, "sources_visible": True},
    },
]


def apply_rhinology_allergy_concept_checks_v231(checks, deep_modules, v6_item_id):
    """Append the two missing exact-canonical checks once and fail visibly on link drift."""
    existing = {str(q.get("id") or "") for q in checks or []}
    added, link_mismatch = [], []
    deep_by_id = {
        v6_item_id(domain, module.get("topic")): module
        for domain, modules in (deep_modules or {}).items()
        for module in (modules or [])
        if module.get("topic")
    }
    for check in CHECKS:
        if check["concept_id"] not in deep_by_id:
            link_mismatch.append(check["id"])
            continue
        if check["id"] not in existing:
            checks.append(dict(check))
            existing.add(check["id"])
            added.append(check["id"])
    return {"added": added, "link_mismatch": link_mismatch, "expected": [q["id"] for q in CHECKS]}
