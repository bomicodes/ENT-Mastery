SITE = {
    "slug": "cutaneous-scc",
    "name": "Cutaneous Carcinoma of the Head and Neck (cSCC)",
    "group": "Skin",
    "order": 200,
    "ajcc": "AJCC 8th edition",
    "applies_to": "Cutaneous squamous cell carcinoma and other non-melanoma skin carcinomas (BCC, adnexal carcinomas) of the head and neck, including the vermilion lip. Excludes Merkel cell carcinoma, melanoma and eyelid carcinoma, which have their own chapters. AJCC 8 has no TNM chapter for cSCC outside the head and neck.",
    "big_picture": "T is size (2 and 4 cm) plus high-risk features. Deep invasion (>6 mm or beyond subcutaneous fat), qualifying perineural invasion or minor bone erosion each make T3 regardless of size. Gross bone/marrow invasion is T4a and skull base is T4b. Nodes use the mucosal head and neck system, including ENE (clinical N3b; pN2a for a single ENE+ node ≤3 cm). Any N2-N3 makes Stage IV. The parotid is the first-echelon basin for much of the face and scalp. The Brigham and Women's (BWH) alternative T system predicts nodal metastasis and death better at the T2/T3 level, so it is commonly reported alongside AJCC.",
    "whats_new": [
        "AJCC 8 created a head and neck-specific chapter ('Cutaneous carcinoma of the head and neck'), adding depth >6 mm/invasion beyond subcutaneous fat, PNI and minor bone erosion as T3 criteria.",
        "Nodal staging now matches mucosal head and neck sites, including ENE (cN3b; pN2a/pN3b).",
        "C-POST (Rischin et al., NEJM 2025): adjuvant cemiplimab after surgery and postoperative RT in high-risk cSCC improved DFS (HR 0.32; 24-month DFS 87.1% vs 64.1%). FDA approved it October 8, 2025.",
        "Cemiplimab (2018) and pembrolizumab (KEYNOTE-629) are approved for locally advanced or metastatic cSCC not curable by surgery or RT."
    ],
    "t": [
        ["TX", "Primary tumor cannot be assessed"],
        ["Tis", "Carcinoma in situ"],
        ["T1", "<2 cm in greatest dimension"],
        ["T2", "≥2 cm but <4 cm in greatest dimension"],
        ["T3", "≥4 cm, OR minor bone erosion, OR perineural invasion, OR deep invasion"],
        ["T4a", "Gross cortical bone/marrow invasion"],
        ["T4b", "Skull base invasion and/or skull base foramen involvement"]
    ],
    "t_extra": [
        {"title": "T3 definitions", "rows": [
            ["Deep invasion", "Invasion beyond the subcutaneous fat, OR >6 mm (measured from the granular layer of adjacent normal epidermis to the base of the tumor)"],
            ["Perineural invasion (T3)", "Tumor in the nerve sheath of a nerve lying deeper than the dermis or measuring ≥0.1 mm in caliber, OR clinical/radiographic involvement of a named nerve without skull base invasion or transgression"]
        ]},
        {"title": "BWH (Brigham and Women's) alternative T staging", "rows": [
            ["Risk factors", "Diameter ≥2 cm; poorly differentiated histology; PNI of nerve ≥0.1 mm; invasion beyond subcutaneous fat (excluding bone, which is T3)"],
            ["BWH T1", "0 risk factors"],
            ["BWH T2a", "1 risk factor"],
            ["BWH T2b", "2-3 risk factors (most nodal metastases and deaths occur in T2b/T3)"],
            ["BWH T3", "≥4 risk factors or bone invasion"]
        ]}
    ],
    "n_clinical": [
        ["NX", "Regional nodes cannot be assessed"],
        ["N0", "No regional lymph node metastasis"],
        ["N1", "Single ipsilateral node ≤3 cm, ENE(-)"],
        ["N2a", "Single ipsilateral node >3 cm but ≤6 cm, ENE(-)"],
        ["N2b", "Multiple ipsilateral nodes, none >6 cm, ENE(-)"],
        ["N2c", "Bilateral or contralateral nodes, none >6 cm, ENE(-)"],
        ["N3a", "Any node >6 cm, ENE(-)"],
        ["N3b", "Any node(s) with clinically overt ENE(+)"]
    ],
    "n_pathologic": [
        ["pN1", "Single ipsilateral node ≤3 cm, ENE(-)"],
        ["pN2a", "Single ipsilateral node ≤3 cm ENE(+); OR single ipsilateral node >3 cm but ≤6 cm ENE(-)"],
        ["pN2b", "Multiple ipsilateral nodes, none >6 cm, ENE(-)"],
        ["pN2c", "Bilateral or contralateral nodes, none >6 cm, ENE(-)"],
        ["pN3a", "Any node >6 cm, ENE(-)"],
        ["pN3b", "Single ipsilateral node >3 cm ENE(+); OR multiple ipsilateral, contralateral or bilateral nodes with any ENE(+); OR a single contralateral node of any size ENE(+)"]
    ],
    "m": [
        ["M0", "No distant metastasis"],
        ["M1", "Distant metastasis"]
    ],
    "stage_groups": [
        ["Stage 0", "Tis N0 M0"],
        ["Stage I", "T1 N0 M0"],
        ["Stage II", "T2 N0 M0"],
        ["Stage III", "T3 N0 M0; T1-T3 N1 M0"],
        ["Stage IV", "T1-T3 N2 M0; any T N3 M0; T4 any N M0; any T any N M1"]
    ],
    "stage_groups_pathologic": [],
    "memory_hooks": [
        "'2-4-6'. Size cutoffs are <2 and <4 cm, and depth >6 mm (or beyond the fat) makes T3.",
        "'Any one high-risk feature makes T3': ≥4 cm, deep, PNI, or minor bone erosion.",
        "'Point-one or below the dermis': PNI counts for T3 only if the nerve is ≥0.1 mm or deeper than the dermis, or a named nerve is involved clinically or on imaging.",
        "'Minor erosion = T3, gross cortex or marrow = T4a, skull base or foramen = T4b'.",
        "'N2 = Stage IV'. Any N2 or N3, any T4, or M1 is Stage IV, just as in mucosal head and neck cancer (single Stage IV, no A/B/C).",
        "BWH counts risk factors: 0 = T1, 1 = T2a, 2-3 = T2b, 4 or bone = T3. Think 'Big (≥2 cm), Bad cells (poorly differentiated), Below the fat, Bundle (nerve ≥0.1 mm)'.",
        "'Check the parotid'. Temple, forehead, scalp, ear and cheek primaries drain to intraparotid nodes, so a parotid mass in a patient with prior facial skin cancer is metastatic cSCC until proven otherwise."
    ],
    "algorithm": [
        {"stage": "Low-risk localized (I, BWH T1)",
         "treatment": "Standard excision with 4-6 mm clinical margins, or Mohs. Destructive methods (C&E) only for low-risk tumors outside terminal-hair areas.",
         "notes": "No imaging or SLNB is needed. Follow with skin surveillance."},
        {"stage": "High-risk localized (II-III, BWH T2b/T3, deep, PNI, poorly differentiated, recurrent, immunosuppressed)",
         "treatment": "Mohs or excision with complete margin assessment (PDEMA), and imaging (CT/MRI) for suspected deep, bone or perineural spread. Adjuvant RT for positive margins that cannot be re-excised, extensive/named-nerve PNI, T3-T4, or other very high-risk features.",
         "notes": "SLNB for high-risk cSCC is investigational/contested. Get an MRI for clinical named-nerve PNI (V2, V3, VII) to map spread toward the skull base."},
        {"stage": "Regional nodal disease (III-IV)",
         "treatment": "Excise the primary + parotidectomy (superficial or total, if intraparotid nodes are at risk or involved) + neck dissection, followed by postoperative RT. Add concurrent chemotherapy only selectively (contested; extrapolated from mucosal SCC).",
         "notes": "C-POST: after surgery + postoperative RT, give adjuvant cemiplimab to high-risk patients (nodal: ENE with the largest node ≥20 mm, or ≥3 involved nodes regardless of ENE; non-nodal: in-transit metastases, T4 (bone-invasive) lesion, clinical or radiologic named-nerve perineural invasion, or locally recurrent tumor with ≥1 additional poor prognostic feature). RT had to be completed 2-10 weeks before randomization. DFS HR 0.32, FDA-approved October 8, 2025. Overall survival data are immature, so check transplant and autoimmune status first."},
        {"stage": "Locally advanced unresectable or metastatic",
         "treatment": "First line: PD-1 inhibitor, either cemiplimab (Migden NEJM 2018) or pembrolizumab (KEYNOTE-629). Use RT for local control. Cetuximab or platinum chemotherapy is reserved for patients unsuitable for immunotherapy.",
         "notes": "Neoadjuvant cemiplimab before surgery for resectable stage II-IV (Gross NEJM 2022: pCR 51%) is an emerging/contested option. Solid-organ transplant recipients face a risk of graft rejection on PD-1 therapy."}
    ],
    "pitfalls": [
        "AJCC 8 cSCC sizes are written '<2 cm', '≥2 to <4 cm' and '≥4 cm'. A tumor exactly 2.0 cm is T2 and exactly 4.0 cm is T3. The CAP cSCC head and neck protocol (v1.1.0.0) and Radiopaedia write '≤2 cm' and '>4 cm' instead, so expect this boundary to be inconsistent across sources and avoid relying on an exactly 2.0 or 4.0 cm case.",
        "Not all PNI counts. A nerve <0.1 mm within the dermis does not make T3. Clinical or radiographic named-nerve involvement without skull base invasion makes T3, while skull base invasion or foramen involvement makes T4b.",
        "Minor bone erosion is T3. Gross cortical/marrow invasion is T4a.",
        "Pathologic ENE in a single ipsilateral node ≤3 cm is pN2a (Stage IV), not pN1. Clinically overt ENE makes cN3b.",
        "This chapter does not apply to Merkel cell carcinoma, melanoma or eyelid carcinoma, nor to cSCC outside the head and neck.",
        "C-POST cemiplimab is ADJUVANT after surgery and RT for high-risk features. Advanced-disease cemiplimab is for patients not curable by surgery or RT. Do not mix up the two indications."
    ],
    "drills": [
        {"case": "A 74-year-old man has a 2.5 cm scalp cSCC. Pathology shows invasion 7 mm from the granular layer, still within the subcutaneous fat. No PNI. Neck exam and imaging are negative.",
         "question": "What is the AJCC 8 stage?",
         "choices": ["Stage II", "Stage III", "Stage I", "Stage IV"],
         "answer": 1,
         "explanation": "Size alone would be T2, but deep invasion >6 mm makes T3. T3 N0 M0 = Stage III."},
        {"case": "A 1.5 cm cheek cSCC shows perineural invasion of a 0.05 mm nerve located within the dermis. Margins are clear. N0 M0.",
         "question": "What is the T category?",
         "choices": ["T3 (perineural invasion)", "T2", "T1", "T4b"],
         "answer": 2,
         "explanation": "PNI makes T3 only if the nerve is deeper than the dermis or ≥0.1 mm in caliber, or a named nerve is involved clinically or on imaging. A 0.05 mm intradermal nerve does not qualify, so size <2 cm = T1 (Stage I)."},
        {"case": "A 3.0 cm preauricular cSCC (no high-risk features) has a single 2.4 cm intraparotid node on CT with no clinical or radiographic ENE. No distant disease.",
         "question": "What is the clinical stage?",
         "choices": ["Stage III", "Stage II", "Stage IV", "Stage I"],
         "answer": 0,
         "explanation": "T2 (≥2 to <4 cm). A single ipsilateral node ≤3 cm without ENE = N1. T1-T3 N1 M0 = Stage III."},
        {"case": "After parotidectomy and neck dissection for a 1.5 cm temple cSCC, pathology shows a single 2.0 cm intraparotid node with microscopic ENE. All other nodes are negative.",
         "question": "What is the pathologic N category and stage?",
         "choices": ["pN1, Stage III", "pN3b, Stage IV", "pN2a, Stage III", "pN2a, Stage IV"],
         "answer": 3,
         "explanation": "A single ipsilateral node ≤3 cm with ENE = pN2a. T1-T3 N2 = Stage IV."},
        {"case": "A 3.5 cm cSCC of the cheek is poorly differentiated, with no PNI and invasion confined to the dermis/subcutis. N0.",
         "question": "What is the BWH T category?",
         "choices": ["BWH T1", "BWH T2a", "BWH T2b", "BWH T3"],
         "answer": 2,
         "explanation": "BWH risk factors present: diameter ≥2 cm and poorly differentiated = 2 factors = T2b. (AJCC 8: T2, Stage II.)"},
        {"case": "A recurrent forehead cSCC has spread along V1 on MRI with tumor reaching the superior orbital fissure.",
         "question": "What is the AJCC T category?",
         "choices": ["T4b", "T3", "T4a", "T2"],
         "answer": 0,
         "explanation": "Skull base invasion and/or skull base foramen involvement = T4b. Named-nerve involvement WITHOUT skull base transgression would be T3."},
        {"case": "A 68-year-old immunocompetent man has parotidectomy, neck dissection and postoperative RT for cSCC with 4 involved nodes, one with ENE. Restaging shows no residual disease, and RT finished 4 weeks ago.",
         "question": "Which adjuvant therapy is supported by phase 3 data?",
         "choices": ["Adjuvant cetuximab", "Adjuvant cemiplimab (C-POST)", "Adjuvant carboplatin/paclitaxel", "No further therapy is supported by any trial"],
         "answer": 1,
         "explanation": "C-POST enrolled high-risk cSCC (ENE with the largest node ≥20 mm, ≥3 involved nodes, in-transit metastases, T4, named-nerve PNI, or recurrent tumor with another risk feature) 2-10 weeks after completing postoperative RT. This patient qualifies by having ≥3 involved nodes. Cemiplimab improved DFS (HR 0.32; 24-month DFS 87.1% vs 64.1%) and is FDA-approved (October 2025)."},
        {"case": "An 80-year-old has a 7 cm unresectable cSCC of the scalp invading the outer table, with in-transit nodules and lung metastases. ECOG 1, no transplant or autoimmune disease.",
         "question": "What is the preferred first-line systemic therapy?",
         "choices": ["Cisplatin/5-FU", "Cetuximab", "Cemiplimab (PD-1 inhibitor)", "Vismodegib"],
         "answer": 2,
         "explanation": "Cemiplimab (or pembrolizumab) is first line for advanced/metastatic cSCC not curable by surgery or RT, with response rates around 45-50%. Vismodegib is for BCC."}
    ],
    "sources": [
        ["AJCC Cancer Staging Manual, 8th ed (2017), Ch 15 Cutaneous Carcinoma of the Head and Neck", ""],
        ["Radiopaedia: Cutaneous carcinoma of the head and neck staging (AJCC 8)", "https://radiopaedia.org/articles/cutaneous-carcinoma-of-the-head-and-neck-staging"],
        ["PathologyOutlines: Cutaneous SCC (AJCC 8 pT and BWH staging)", "https://www.pathologyoutlines.com/topic/skintumornonmelanocyticscc.html"],
        ["Rischin D, et al. Adjuvant Cemiplimab or Placebo in High-Risk Cutaneous Squamous-Cell Carcinoma (C-POST). N Engl J Med. 2025. doi:10.1056/NEJMoa2502449 (ASCO Post summary)", "https://ascopost.com/news/june-2025/adjuvant-cemiplimab-in-high-risk-cutaneous-squamous-cell-carcinoma/"],
        ["JNCCN 360: C-POST trial eligibility (nodal and non-nodal high-risk features)", "https://jnccn360.org/advanced-skin-cancers/news/c-post-trial-cemiplimab-rwlc-after-surgery-for-high-risk-squamous-cell-skin-cancer"],
        ["FDA approves cemiplimab-rwlc for adjuvant treatment of cSCC (Oct 8, 2025)", "https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-cemiplimab-rwlc-adjuvant-treatment-cutaneous-squamous-cell-carcinoma"],
        ["Migden MR, et al. PD-1 Blockade with Cemiplimab in Advanced Cutaneous Squamous-Cell Carcinoma. N Engl J Med. 2018;379:341-351", ""],
        ["Gross ND, et al. Neoadjuvant Cemiplimab for Stage II to IV Cutaneous Squamous-Cell Carcinoma. N Engl J Med. 2022;387:1557-1568", ""],
        ["Jambusaria-Pahlajani A, Karia PS, Schmults CD, et al. BWH alternative staging system. JAMA Dermatol 2013 / J Clin Oncol 2014", ""],
        ["AJCC Current Staging System 2026 (cutaneous carcinoma of head and neck remains 8th edition)", "https://www.facs.org/media/c5ik5tkr/ajcc-current-staging-system-2026.pdf"],
        ["NCCN Clinical Practice Guidelines: Squamous Cell Skin Cancer, 2026", ""],
        ["NCI MedGen: Head and Neck Cutaneous Squamous Cell Carcinoma AJCC v8 stage definitions (T1 <2 cm; T2 ≥2 to <4 cm; T3 ≥4 cm)", "https://ncbi.nlm.nih.gov/medgen/1614442"],
        ["CAP Protocol: Cutaneous Squamous Cell Carcinoma of the Head and Neck, v1.1.0.0 (AJCC 8; Dec 2024)", "https://documents.cap.org/protocols/HN.SCC_1.1.0.0.REL.CAPCP.pdf"],
        ["American College of Mohs Surgery: AJCC 8 changes for cSCC (fellow-in-training perspective)", "https://www.mohscollege.org/about-acms/news/winter-2017-enewsletter/fit"],
        ["ASCO Post: Cemiplimab as adjuvant therapy for high-risk cSCC (C-POST eligibility incl. ENE with node ≥20 mm)", "https://ascopost.com/news/august-2025/use-of-cemiplimab-as-adjuvant-therapy-for-high-risk-cutaneous-squamous-cell-carcinoma"],
        ["Targeted Oncology: Defining high-risk cSCC, C-POST criteria explained (Oct 2025)", "https://www.targetedonc.com/view/defining-high-risk-cscc-c-post-patient-criteria-explained"]
    ],
    "verify_notes": "Reviewer check (2026-10-29). Confirmed: the T size wording T1 <2 cm, T2 ≥2 to <4 cm, T3 ≥4 cm from the NCI MedGen AJCC v8 definitions and the Mohs College AJCC 8 summary; T3 deep-invasion and PNI definitions, T4a/T4b and pN1-pN3b from the CAP cSCC head and neck protocol v1.1.0.0, which uses '≤2 cm'/'>4 cm' wording, so the pitfall now flags the discrepancy. C-POST: DFS HR 0.32, the 2-10 week RT window and the October 8, 2025 approval (FDA page), and the eligibility, including ENE with the largest node ≥20 mm and ≥3 nodes (ASCO Post, JNCCN 360, Targeted Oncology). Corrected: the C-POST eligibility, which lacked the ≥20 mm node threshold for ENE and the named-nerve qualifier for PNI; added the RT timing window. Still unconfirmed: clinical N wording was not quoted from a cSCC-specific source (it follows the general AJCC 8 head and neck system); Migden 2018, KEYNOTE-629 and Gross 2022 figures and NCCN 2026 margin guidance were not re-read."
}
