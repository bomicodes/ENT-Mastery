"""v36.6 — deepen exact Systemic Disease of the Nose / Sinuses canonical topic.

This bounded successor preserves the 42-topic Rhinology inventory and existing host-factor CRS
separation. It adds clinically useful systemic-inflammatory/destructive reasoning, learner-visible
aliases, senior surgical boundaries, and traceable connected-textbook/current-guideline sources to
the exact live canonical row. No canonical topic is added, removed, or renamed.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGET = "Systemic Disease of the Nose / Sinuses"

CONNECTED_TEXTBOOKS = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — connected Google Drive full-volume copy ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022) — connected Google Drive file ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — connected Google Drive file ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
]

AUTHORITATIVE_GUIDANCE = [
    "Chung SA, et al. 2021 ACR/Vasculitis Foundation Guideline for Management of ANCA-Associated Vasculitis. Arthritis Care Res. 2021;73:1088-1105. DOI 10.1002/acr.24634.",
    "Crouser ED, et al. Diagnosis and Detection of Sarcoidosis: An Official ATS Clinical Practice Guideline. Am J Respir Crit Care Med. 2020;201:e26-e51.",
    "Wallace ZS, et al. 2019 ACR/EULAR Classification Criteria for IgG4-Related Disease. Arthritis Rheumatol. 2020;72:7-19. DOI 10.1002/art.41120. Classification criteria support structured clinicopathologic reasoning but are not a stand-alone diagnostic test.",
    "Khosroshahi A, et al. International Consensus Guidance Statement on Management and Treatment of IgG4-Related Disease. Arthritis Rheumatol. 2015;67:1688-1699. DOI 10.1002/art.39132.",
]


def _append(row, field, addition, anchor):
    current = str(row.get(field) or "")
    if anchor.lower() not in current.lower():
        row[field] = (current.rstrip() + ("\n\n" if current.strip() else "") + addition).strip()


def apply_rhinology_systemic_disease_v366(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(row.get("topic") or ""): row for row in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(
            f"v36.6 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}"
        )
    if TARGET not in by_topic:
        raise RuntimeError(f"v36.6 missing exact canonical target: {TARGET!r}")

    row = by_topic[TARGET]

    _append(
        row,
        "recognize",
        "Systemic-inflammatory/destructive phenotype: refractory 'CRS' with persistent crusting, bloody discharge or epistaxis, ulceration, septal perforation, progressive saddle-nose change, or disease extending beyond an ordinary mucosal pattern should trigger a systemic diagnosis rather than another empiric sinus-treatment cycle. Searchable aliases include granulomatosis with polyangiitis (GPA; legacy Wegener granulomatosis), eosinophilic granulomatosis with polyangiitis (EGPA; legacy Churg-Strauss), sarcoidosis, IgG4-related disease, destructive sinonasal disease, septal perforation, saddle nose, and vasculitis. GPA clues include pulmonary, renal, otologic, orbital and subglottic disease. EGPA clues include asthma plus eosinophilia with sinonasal/polyposis disease and neuropathic, pulmonary, cutaneous or cardiac features. Tumefactive orbital/lacrimal/salivary involvement can support IgG4-related disease; granulomatous sinonasal disease requires infectious and other mimics to remain visible.",
        "systemic-inflammatory/destructive phenotype",
    )
    _append(
        row,
        "workup",
        "Workup is phenotype- and organ-directed, not an ANCA-or-serum-marker shortcut. For destructive disease, document endoscopic distribution and obtain CT; use MRI when orbit, skull base, perineural, intracranial or tumefactive soft-tissue extension is a question. Ask about pulmonary symptoms/hemoptysis, renal disease, neuropathy, asthma/eosinophilia, skin disease and medication/exposure history; obtain urinalysis/renal function, CBC with differential/eosinophils, inflammatory markers and chest evaluation when clinically indicated. PR3-/MPO-ANCA can support AAV but a positive result does not replace clinicopathologic synthesis and a negative result does not exclude disease, particularly EGPA. Biopsy viable active tissue when tissue is needed, coordinate pathology for vasculitic/granulomatous/fibroinflammatory patterns, and exclude infection, cocaine/levamisole injury, foreign material and malignancy before assigning a systemic inflammatory label. Sarcoidosis requires a compatible syndrome with granulomatous evidence when needed and exclusion of alternative granulomatous causes. IgG4-related disease requires clinical, imaging and pathologic correlation; serum IgG4 alone is not diagnostic.",
        "an ANCA-or-serum-marker shortcut",
    )
    _append(
        row,
        "manage",
        "Management follows the systemic disease and threatened organs. Coordinate rheumatology and, as indicated, pulmonology, nephrology, allergy/immunology, ophthalmology or other involved specialties rather than treating the nose in isolation. AAV treatment is systemic immunosuppression selected by disease severity and organ threat; ENT care manages local consequences and obtains diagnostic tissue without delaying systemic rescue for organ-threatening disease. Sarcoidosis and IgG4-related disease likewise require systemic clinicopathologic assessment before disease-directed medical therapy. Keep the separate canonical CF/PCD and immunodeficiency-associated CRS pathways separate rather than duplicating those host-factor algorithms here.",
        "management follows the systemic disease",
    )
    _append(
        row,
        "operate",
        "Senior operative boundary: serial ESS is not a diagnostic or therapeutic reflex for unexplained destructive systemic disease. Define the purpose of surgery before entering the OR: obtain representative biopsy, drain/source-control a true infectious complication, debride nonviable tissue when disease-specific care requires it, improve topical access in selected controlled disease, or correct fixed obstruction after the systemic process is understood. Avoid elective reconstructive correction of septal/saddle deformity during active destructive inflammation; reconstruct when disease control is durable enough to protect the repair. Escalating tissue loss, orbital/skull-base extension, airway involvement, pulmonary hemorrhage or renal injury is a systemic rescue problem, not a reason for progressively wider routine FESS.",
        "serial ESS is not a diagnostic",
    )
    _append(
        row,
        "teach",
        "Teaching synthesis: when the nose looks destructive rather than merely inflamed, widen from 'sinusitis' to systemic disease and dangerous mimics. The resident should be able to name GPA, EGPA, sarcoidosis and IgG4-related disease; identify pulmonary/renal/neurologic/orbital/airway clues; explain why ANCA or serum IgG4 is supportive rather than independently diagnostic; choose safe tissue and systemic evaluation; and state the limited, purpose-driven role of sinonasal surgery after the disease process is defined.",
        "when the nose looks destructive",
    )

    sources = list(row.get("source_basis") or [])
    for source in CONNECTED_TEXTBOOKS + AUTHORITATIVE_GUIDANCE:
        if source not in sources:
            sources.append(source)
    row["source_basis"] = sources
    row["source_grounded_v366"] = True
    row["source_metadata_v366"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TARGET},
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "guidance": [
            "ACR/VF AAV guideline 2021 DOI 10.1002/acr.24634",
            "ATS Sarcoidosis diagnosis guideline 2020",
            "ACR/EULAR IgG4-RD classification criteria 2019/2020 DOI 10.1002/art.41120",
            "International IgG4-RD consensus guidance DOI 10.1002/art.39132",
        ],
        "scope": "systemic inflammatory/destructive sinonasal phenotype; CF/PCD and immunodeficiency remain separate canonical host-factor topics",
    }

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TARGET], "count": 1}
