# labs_v532/thyroid_more.py: added 2026-11-01 after viewing each image in Chrome. License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'thyroid-ultrasound'
CASES = [
    {
        "id": "us_ptc_tirads5_v545",
        "level": 3,
        "concept_id": "thyroid:ptc-us-features",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/439c/5501791/bd47784ebd3f/41598_2017_5153_Fig1_HTML.jpg",
        "image_credit": "Zhang Q, Liu BJ, Ren WW, et al. Sci Rep. 2017;7:4899 (CC BY 4.0) — Fig. 1 (focus on panels a and b)",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5501791/",
        "prompt": "A 54-year-old woman has a thyroid nodule. Panel (a) is grayscale ultrasound and panel (b) is color Doppler (panels c and d are the surgical histology and a molecular assay). Score the nodule's features in panel (a) before naming anything.",
        "answer": "Solid composition, hypoechoic, irregular and ill-defined margins, with contact and involvement of the thyroid capsule (arrowhead), and coarse calcifications casting acoustic shadows. On Doppler (b) the flow is both internal and peripheral. This combination of features is high suspicion (ACR TI-RADS 5 range), and pathology confirmed papillary thyroid carcinoma.",
        "why": "TI-RADS scores composition, echogenicity, shape, margins and echogenic foci separately. Capsule contact matters beyond the score: abutment or bulging of the capsule raises concern for extrathyroidal extension, which changes the extent of surgery.",
        "reason_prompt": "Which feature here should change how you plan the operation, not just whether you biopsy?",
        "reason_answer": "Capsule involvement. It raises the possibility of extrathyroidal extension. Look carefully at the strap muscles, trachea and recurrent laryngeal nerve region, map the central and lateral neck nodes before surgery, and consider cross-sectional imaging if gross invasion is suspected.",
        "teach_prompt": "Teach a junior why vascularity is not scored in ACR TI-RADS.",
        "teach_answer": "Doppler flow patterns overlap too much between benign and malignant nodules to add reliable risk information, so ACR TI-RADS leaves vascularity out. The grayscale features and size thresholds drive the FNA decision.",
        "follow": "At what size would a TI-RADS 5 nodule meet the ACR threshold for FNA?",
        "follow_answer": "1.0 cm or larger (follow-up imaging is advised for TR5 nodules from 0.5 to 0.9 cm).",
        "mcq": {
            "question": "A 1.4 cm thyroid nodule has the ultrasound appearance in panel (a): solid, hypoechoic, irregular margins, coarse shadowing calcifications and contact with the thyroid capsule. What is the most appropriate next step?",
            "choices": [
                "Repeat ultrasound in 12 months",
                "Ultrasound-guided FNA, with a careful look for extrathyroidal extension and abnormal neck nodes",
                "Radioactive iodine uptake scan to decide on FNA",
                "Total thyroidectomy without tissue diagnosis because the features are diagnostic"
            ],
            "answer": 1,
            "explanation": "These features place the nodule in the high-suspicion TI-RADS 5 range, and at 1.4 cm it exceeds the 1.0 cm FNA threshold. Capsule contact should prompt evaluation for extrathyroidal extension, and a nodal survey belongs in the same ultrasound. An uptake scan is for suppressed TSH, and surgery is planned after cytology, not instead of it.",
            "domain": "Thyroid / Parathyroid / Salivary",
            "topic": "High-suspicion thyroid nodule"
        },
        "verify_note": "PMC5501791: CC BY 4.0 link on the article page; Fig. 1 legend 'A 54-year-old woman with papillary thyroid carcinoma. (a) A solid, hypoechogenic, irregular and ill-defined nodule with capsule contact and involvement... macrocalcifications with acoustic shadow... (b) rich blood flow distributed internally and peripherally on color Doppler'. Image viewed in Chrome.",
        "variant_type": "interpret"
    }
]
