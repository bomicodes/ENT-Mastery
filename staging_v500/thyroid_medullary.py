SITE = {
    "slug": "thyroid-medullary",
    "name": "Thyroid: Medullary Carcinoma",
    "group": "Salivary & thyroid",
    "order": 130,
    "ajcc": "AJCC 8th edition",
    "applies_to": "Medullary thyroid carcinoma (parafollicular C-cell origin), sporadic or hereditary (MEN2A, MEN2B, familial MTC). AJCC 8 Chapter 74.",
    "big_picture": "MTC uses the thyroid T and N definitions but has its own stage groups and NO age split. The nodal compartment drives stage. Central (N1a) disease is Stage III. Lateral (N1b) disease, or gross invasion of neck structures (T4a), is Stage IVA. Calcitonin and CEA are the tumor markers, and RET status (germline and somatic) decides prophylactic surgery timing and selpercatinib eligibility. RAI and TSH suppression play no part, because C-cells do not take up iodine.",
    "whats_new": [
        "AJCC 8 gave MTC its own chapter (Ch 74), separate from differentiated/anaplastic thyroid.",
        "T3 split as for DTC: T3a >4 cm intrathyroidal; T3b gross ETE into strap muscles only.",
        "Level VII (upper mediastinal) nodes are N1a.",
        "Selpercatinib, a selective RET inhibitor, received traditional FDA approval (September 2024) for advanced/metastatic RET-mutant MTC needing systemic therapy, in patients aged ≥2 years. It is based on LIBRETTO-531, which showed superior PFS vs cabozantinib or vandetanib (HR 0.28)."
    ],
    "t": [
        ["TX", "Primary tumor cannot be assessed"],
        ["T0", "No evidence of primary tumor"],
        ["T1a", "≤1 cm, limited to the thyroid"],
        ["T1b", ">1 cm but ≤2 cm, limited to the thyroid"],
        ["T2", ">2 cm but ≤4 cm, limited to the thyroid"],
        ["T3a", ">4 cm, limited to the thyroid"],
        ["T3b", "Gross ETE invading only strap muscles, any size"],
        ["T4a", "Moderately advanced: gross ETE into nearby neck tissues (subcutaneous soft tissue, larynx, trachea, esophagus, or recurrent laryngeal nerve), any size"],
        ["T4b", "Very advanced: extension toward the spine (prevertebral fascia) or into nearby large blood vessels (encasing carotid artery or mediastinal vessels), any size"]
    ],
    "t_extra": [
        {"title": "ATA 2015 RET risk levels (hereditary MTC) and prophylactic thyroidectomy timing", "rows": [
            ["Highest (ATA-HST)", "RET M918T (MEN2B). Total thyroidectomy in the first year of life (ideally the first months)."],
            ["High (ATA-H)", "RET C634 and A883F. Total thyroidectomy at or before age 5, timed by serum calcitonin."],
            ["Moderate (ATA-MOD)", "Other RET mutations. Start calcitonin/ultrasound screening around age 5, and operate when calcitonin rises (or in childhood if the family prefers not to do prolonged surveillance)."]
        ]}
    ],
    "n_clinical": [
        ["NX", "Regional nodes cannot be assessed"],
        ["N0a", "One or more cytologically or histologically confirmed benign nodes"],
        ["N0b", "No radiologic or clinical evidence of locoregional nodal metastasis"],
        ["N1a", "Level VI or VII (pretracheal, paratracheal, prelaryngeal/Delphian, upper mediastinal), unilateral or bilateral"],
        ["N1b", "Unilateral, bilateral, or contralateral lateral neck (levels I-V) or retropharyngeal nodes"]
    ],
    "n_pathologic": [],
    "m": [
        ["M0", "No distant metastasis"],
        ["M1", "Distant metastasis"]
    ],
    "stage_groups": [
        ["Stage I", "T1 N0 M0"],
        ["Stage II", "T2-T3 N0 M0"],
        ["Stage III", "T1-T3 N1a M0"],
        ["Stage IVA", "T4a any N M0; T1-T3 N1b M0"],
        ["Stage IVB", "T4b any N M0"],
        ["Stage IVC", "Any T, any N, M1"]
    ],
    "stage_groups_pathologic": [],
    "memory_hooks": [
        "'Medullary has no birthday'. No age-55 split, unlike DTC.",
        "Nodes climb the stages: N0 is I/II, central N1a is III, lateral N1b is IVA.",
        "'Lateral = IVA = T4a'. A small MTC with lateral neck nodes is staged the same as one grossly invading the trachea.",
        "'2B or not 2B, operate before 1 year': M918T (MEN2B) means the highest risk and thyroidectomy in infancy. C634 (MEN2A) means thyroidectomy by age 5.",
        "'Pheo first': always exclude pheochromocytoma (plasma or urine metanephrines) before any thyroid or neck surgery in MTC.",
        "'Calcitonin + CEA = the MTC tumor markers'. Thyroglobulin is useless, and RAI and TSH suppression do nothing.",
        "'Selpercatinib Selects RET'. Use a selective RET inhibitor first line for RET-mutant advanced MTC, ahead of the older multikinase drugs vandetanib and cabozantinib."
    ],
    "algorithm": [
        {"stage": "Preoperative workup (all)",
         "treatment": "Serum calcitonin and CEA, neck ultrasound (central and lateral), germline RET testing, and biochemical screening for pheochromocytoma (plasma free or urine fractionated metanephrines) and hyperparathyroidism (calcium/PTH). Add cross-sectional imaging (neck/chest CT, liver MRI) when nodes are involved or calcitonin is above about 500 pg/mL.",
         "notes": "Resect a pheochromocytoma first (after alpha-blockade) before thyroidectomy."},
        {"stage": "Localized (I-II), no lateral nodes on imaging",
         "treatment": "Total thyroidectomy with prophylactic central (level VI) neck dissection (ATA 2015).",
         "notes": "Prophylactic lateral neck dissection based on calcitonin level alone is CONTESTED. Some surgeons use thresholds (e.g., calcitonin >20 → consider ipsilateral lateral; >200 → consider contralateral lateral)."},
        {"stage": "Node-positive (III, IVA from N1b)",
         "treatment": "Total thyroidectomy with central neck dissection plus therapeutic lateral neck dissection (levels II-V) of involved compartments.",
         "notes": "Adjuvant EBRT is selective (gross residual disease, extensive ENE, or high-risk features) and its benefit is contested. There is no role for RAI ablation or TSH suppression. Give levothyroxine replacement only."},
        {"stage": "Post-operative surveillance",
         "treatment": "Check calcitonin and CEA about 3 months after surgery. Undetectable calcitonin means biochemical cure. Calculate calcitonin/CEA doubling times serially.",
         "notes": "A calcitonin doubling time <6 months predicts poor survival, and >2 years is favorable. Image when calcitonin is above about 150 pg/mL."},
        {"stage": "Advanced / metastatic (IVB-IVC), progressive or symptomatic",
         "treatment": "Test RET (germline + somatic). If RET-mutant, first choice is selpercatinib (LIBRETTO-531, PFS HR 0.28 vs cabozantinib/vandetanib). If RET wild-type or intolerant, use cabozantinib or vandetanib (multikinase). Treat focal lesions with surgery, EBRT, SBRT or ablation.",
         "notes": "Low-volume, slowly rising markers with stable imaging can be observed. Calcitonin elevation alone does not justify a systemic drug. Pralsetinib is another selective RET inhibitor, but its US MTC indication was withdrawn."}
    ],
    "pitfalls": [
        "There is no age split in MTC. A 30-year-old with T1 N1b MTC is Stage IVA (vs Stage I for the same TNM in PTC).",
        "Lateral neck nodes (N1b) make Stage IVA even with a small intrathyroidal primary. Central nodes (N1a) make Stage III.",
        "Always rule out pheochromocytoma before thyroid surgery. Every new MTC needs germline RET testing, even when it appears sporadic (about 25% are hereditary).",
        "RAI, thyroglobulin and TSH suppression have no role in MTC.",
        "MEN2B (M918T) means thyroidectomy in the first year of life. MEN2A C634 means thyroidectomy by age 5. Moderate-risk mutations are timed by calcitonin.",
        "Calcitonin can be falsely elevated by renal failure, PPIs, hypergastrinemia and heterophile antibodies. Interpret it together with imaging and CEA."
    ],
    "drills": [
        {"case": "A 44-year-old has a 1.6 cm sporadic MTC with biopsy-proven level III lateral neck nodes. No distant disease.",
         "question": "What is the AJCC 8 stage?",
         "choices": ["Stage I", "Stage III", "Stage IVA", "Stage II"],
         "answer": 2,
         "explanation": "T1b N1b M0. For MTC, T1-T3 N1b = Stage IVA. There is no age split, so 'Stage I under 55' does not apply."},
        {"case": "A 58-year-old has a 2.8 cm intrathyroidal MTC with two positive paratracheal (level VI) nodes. No lateral or distant disease.",
         "question": "What is the stage?",
         "choices": ["Stage II", "Stage III", "Stage IVA", "Stage IVB"],
         "answer": 1,
         "explanation": "T2 N1a M0 = Stage III (T1-T3 with central N1a)."},
        {"case": "A 50-year-old has a 4.6 cm MTC confined to the thyroid, with negative central and lateral necks on dissection.",
         "question": "What is the stage?",
         "choices": ["Stage I", "Stage IVA", "Stage III", "Stage II"],
         "answer": 3,
         "explanation": "T3a (>4 cm intrathyroidal) N0 M0. For MTC, T2-T3 N0 = Stage II."},
        {"case": "A 2-year-old's father has MEN2B. Genetic testing shows the child carries RET M918T. Calcitonin is mildly elevated.",
         "question": "What is the appropriate management?",
         "choices": ["Total thyroidectomy now (ATA highest-risk mutation; ideally done in the first year of life)", "Annual calcitonin monitoring, with surgery at age 5", "Lobectomy with central neck dissection", "Selpercatinib"],
         "answer": 0,
         "explanation": "M918T is ATA highest risk. Thyroidectomy is recommended in the first year of life, so this child is already overdue and needs surgery now by an experienced surgeon."},
        {"case": "A 46-year-old has newly diagnosed MTC on FNA with a calcitonin of 900 pg/mL. Blood pressure is labile and she has episodic headaches.",
         "question": "What is the next step before thyroidectomy?",
         "choices": ["Radioactive iodine uptake scan", "Thyroglobulin level", "Plasma free (or 24-h urine) metanephrines", "Sestamibi scan"],
         "answer": 2,
         "explanation": "Exclude pheochromocytoma before any MTC surgery (possible MEN2A). If present, resect it first after alpha-blockade."},
        {"case": "A 63-year-old has progressive, symptomatic metastatic MTC in the liver and bone. Tumor NGS shows a somatic RET M918T mutation. No prior systemic therapy.",
         "question": "What is the preferred first-line systemic therapy?",
         "choices": ["Radioactive iodine", "Selpercatinib", "Lenvatinib", "Doxorubicin"],
         "answer": 1,
         "explanation": "Selpercatinib is FDA-approved for advanced RET-mutant MTC and showed superior PFS to cabozantinib/vandetanib in LIBRETTO-531 (HR 0.28). RAI plays no part in MTC."},
        {"case": "Three months after total thyroidectomy with central neck dissection for a T2 N1a MTC, calcitonin is undetectable and CEA is normal.",
         "question": "What is the most appropriate next step?",
         "choices": ["Adjuvant RAI ablation", "TSH-suppressive levothyroxine dosing", "Surveillance with calcitonin/CEA (e.g., every 6-12 months) and levothyroxine replacement to euthyroid range", "Adjuvant external-beam RT"],
         "answer": 2,
         "explanation": "Undetectable calcitonin means biochemical cure. Follow the markers. TSH suppression and RAI do not affect C-cells."}
    ],
    "sources": [
        ["AJCC Cancer Staging Manual, 8th ed (2017), Ch 74 Thyroid - Medullary", ""],
        ["PathologyOutlines: Thyroid staging (AJCC 8 medullary and anaplastic stage groups)", "https://pathologyoutlines.com/topic/thyroidstaging.html"],
        ["Wells SA Jr, Asa SL, Dralle H, et al. Revised American Thyroid Association Guidelines for the Management of Medullary Thyroid Carcinoma. Thyroid. 2015;25(6):567-610", ""],
        ["FDA: FDA approves selpercatinib for medullary thyroid cancer with a RET mutation (Sept 27, 2024)", "https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-selpercatinib-medullary-thyroid-cancer-ret-mutation"],
        ["Hadoux J, Elisei R, Brose MS, et al. Phase 3 Trial of Selpercatinib in Advanced RET-Mutant Medullary Thyroid Cancer (LIBRETTO-531). N Engl J Med. 2023;389:1851-1861", ""],
        ["AJCC Current Staging System 2026 (medullary remains 8th edition)", "https://www.facs.org/media/c5ik5tkr/ajcc-current-staging-system-2026.pdf"],
        ["NCCN Clinical Practice Guidelines: Thyroid Carcinoma (Medullary), 2026", ""],
        ["Precision Medicine Online: Roche, Blueprint withdraw Gavreto (pralsetinib) RET-mutant MTC indication (2023)", "https://www.precisionmedicineonline.com/regulatory-news-fda-approvals/roche-blueprint-medicines-withdraw-gavreto-ret-mutant-medullary"]
    ],
    "verify_notes": "Reviewer check (2026-10-29). Confirmed: the AJCC 8 MTC stage groups (I T1N0; II T2-T3 N0; III T1-T3 N1a; IVA T4a any N or T1-T3 N1b; IVB T4b; IVC M1) and the T4a/T4b wording from PathologyOutlines; the selpercatinib approval and LIBRETTO-531 PFS HR 0.28 from the FDA page; the 2023 withdrawal of the US pralsetinib MTC indication from Precision Medicine Online. All drills re-derived and correct; no table corrections were needed. Still unconfirmed: whether the T1a-T3b wording is verbatim identical to DTC (PathologyOutlines says 'similar'); the ATA 2015 RET risk timing, calcitonin thresholds (500 and 150 pg/mL, and the contested 20/200 lateral-neck thresholds) and doubling-time cutoffs were not re-read from Wells 2015; the NCCN 2026 thyroid PDF was not read."
}
