"""v20.34 — integrated Concept Check for Systemic Disease of the Nose / Sinuses."""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Systemic Disease of the Nose / Sinuses"
QID = "cc-v234-rhinology-systemic-disease-nose-sinuses"

SOURCE_REFS = [
    {"type":"textbook","citation":"Cummings Otolaryngology–Head and Neck Surgery, 7th ed. (2021), connected Google Drive copy ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t. Cross-referenced for destructive/systemic sinonasal disease, biopsy, differential diagnosis, and operative principles."},
    {"type":"textbook","citation":"Pasha & Golub, Otolaryngology–Head & Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Cross-referenced for resident-facing systemic sinonasal differential and workup."},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology, 12th ed., connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Cross-referenced for durable vasculitic/granulomatous sinonasal principles and surgery boundaries."},
    {"type":"guideline","citation":"Chung SA, et al. 2021 ACR/Vasculitis Foundation Guideline for Management of ANCA-Associated Vasculitis. Arthritis Care Res. 2021;73:1088-1105. DOI 10.1002/acr.24634."},
    {"type":"guideline","citation":"Crouser ED, et al. Diagnosis and Detection of Sarcoidosis: An Official ATS Clinical Practice Guideline. Am J Respir Crit Care Med. 2020;201:e26-e51."},
    {"type":"consensus","citation":"Wallace ZS, et al. 2019 ACR/EULAR Classification Criteria for IgG4-Related Disease. Arthritis Rheumatol. 2020;72:7-19. DOI 10.1002/art.41120; used as structured clinicopathologic support, not a stand-alone diagnostic test."},
]

PROMPT = (
    "An adult patient referred for 'refractory chronic sinusitis' has months of bloody crusting, a new septal perforation, "
    "progressive nasal deformity, otitis, fatigue, and microscopic hematuria. As the senior resident, why is another routine "
    "FESS the wrong reflex, how should you organize the systemic/destructive differential, what workup and biopsy strategy "
    "should you choose, and how should sinonasal surgery be used once GPA, EGPA, sarcoidosis, IgG4-related disease, infection, "
    "exposure injury, and malignancy are considered?"
)

ANSWER = """### Destructive sinonasal disease — stop treating the phenotype as routine CRS

**Recognize the pivot.** Bloody crusting, ulceration, septal perforation or saddle-nose change plus extra-sinonasal findings is a systemic/destructive phenotype. GPA is especially concerning here because destructive sinonasal disease can coexist with otologic, pulmonary, renal, orbital or subglottic involvement. EGPA becomes more likely with asthma/eosinophilia plus neuropathic, pulmonary, skin or cardiac disease. Sarcoidosis and IgG4-related disease remain clinicopathologic diagnoses; infection, cocaine/levamisole or other exposure injury, foreign material and malignancy must remain active mimics.

**Work up organs, not just sinuses.** Perform focused endoscopy and CT, adding MRI for orbit/skull base/perineural/intracranial or tumefactive soft-tissue questions. Ask about hemoptysis, dyspnea, urinary change, neuropathy, asthma/eosinophilia, rash and medication/exposure history. In an appropriate phenotype obtain CBC/differential, renal function and urinalysis, inflammatory markers, PR3-/MPO-ANCA and chest assessment. ANCA supports AAV but does not replace clinicopathologic synthesis; ANCA-negative disease exists, particularly in EGPA. Serum IgG4 alone does not diagnose IgG4-RD.

**Get tissue deliberately.** When biopsy is needed, sample viable active tissue likely to answer the question, coordinate pathology for vasculitic, granulomatous and fibroinflammatory patterns, and obtain appropriate infectious studies when infection is plausible. Sarcoidosis requires compatible disease plus exclusion of alternative granulomatous causes.

**Define the role of surgery before operating.** Sinonasal surgery may provide representative tissue, treat a true infectious complication, debride nonviable tissue when disease-specific care requires it, improve topical access in selected controlled disease, or relieve fixed obstruction after the systemic process is understood. Serial ESS is not a diagnostic trial for unexplained destructive disease. Elective reconstruction of septal/saddle deformity should generally wait for durable control of active destructive inflammation.

**Senior synthesis:** this patient needs systemic evaluation and multidisciplinary disease control, not progressively wider routine FESS. Threatened kidney, lung, orbit, skull base or airway changes the urgency and should trigger coordinated systemic rescue.
"""

CHECK = {
    "id": QID,
    "domain": DOMAIN,
    "topic": TOPIC,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "question": PROMPT,
    "choices": [],
    "answer": None,
    "answer_text": ANSWER,
    "explanation": ANSWER,
    "reviewed_all_domains_v178": True,
    "review_basis_v178": "Dedicated v20.34 systemic-sinonasal learner-path repair; exact live canonical linkage, destructive phenotype, systemic workup, tissue strategy, surgery boundary, and visible sources reviewed.",
    "curated_v177": True,
    "converted_to_oral_board_v178": True,
    "search_aliases": ["systemic disease of the nose", "GPA", "granulomatosis with polyangiitis", "Wegener granulomatosis", "EGPA", "Churg-Strauss", "sarcoidosis", "IgG4-related disease", "destructive sinonasal disease", "septal perforation", "saddle nose", "vasculitis"],
    "source_refs_v230": SOURCE_REFS,
    "learner_experience_v234": {"deep_curriculum": True, "concept_check": True, "daily_curriculum": True, "sources_visible": True},
}


def apply_rhinology_systemic_concept_check_v234(checks, deep_modules, v6_item_id):
    module = next((m for m in (deep_modules or {}).get(DOMAIN, []) or [] if str(m.get("topic") or "") == TOPIC), None)
    if module is None:
        return {"added": [], "link_mismatch": [QID], "expected": [QID]}
    if QID in {str(q.get("id") or "") for q in checks or []}:
        return {"added": [], "link_mismatch": [], "expected": [QID]}
    q = dict(CHECK)
    q["concept_id"] = v6_item_id(DOMAIN, TOPIC)
    checks.append(q)
    return {"added": [QID], "link_mismatch": [], "expected": [QID]}
