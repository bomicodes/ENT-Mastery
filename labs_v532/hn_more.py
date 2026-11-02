# labs_v532/hn_more.py: added 2026-11-01 after viewing each image in Chrome. License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'head-neck-imaging'
CASES = [
    {
        "id": "hn_pleomorphic_t2_v545",
        "level": 2,
        "concept_id": "hn:pleomorphic-adenoma-mri",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/195e/11260653/d0a0df7234ce/cureus-0016-00000062791-i03.jpg",
        "image_credit": "Sudabattula K, Zade A, Tote D, et al. Cureus. 2024;16(6):e62791 (CC BY 4.0) — Fig. 3",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11260653/",
        "prompt": "Axial T2-weighted MRI of a slowly enlarging, painless parotid mass in an adult (box). The facial nerve works normally. Describe the lesion's signal and margins.",
        "answer": "A well-circumscribed, lobulated mass in the left parotid (box) that is markedly hyperintense on T2 and darker on T1. A sharply marginated, T2-bright parotid mass in an adult with normal facial nerve function is the classic MRI appearance of pleomorphic adenoma. In this patient it involved both the superficial and deep lobes.",
        "why": "Pleomorphic adenoma is the most common salivary neoplasm. Its high T2 signal reflects myxoid chondroid stroma. Low T2 signal, ill-defined margins, perineural spread or facial weakness should raise concern for malignancy.",
        "reason_prompt": "Why is MRI preferred over CT for this mass, and what must it show before surgery?",
        "reason_answer": "MRI defines soft-tissue margins, signal and deep-lobe or parapharyngeal extension better than CT. It also shows perineural spread along the facial nerve. Before surgery it should define the relationship to the plane of the facial nerve (a superficial versus deep lobe location, often judged against the retromandibular vein) and any parapharyngeal component.",
        "teach_prompt": "Teach a junior why pleomorphic adenoma is not shelled out (enucleated).",
        "teach_answer": "It has an incomplete capsule with finger-like extensions (pseudopodia). Enucleation or capsule rupture leaves tumor behind, causing multinodular recurrence that is much harder to treat. Excise it with a cuff of normal tissue, usually by superficial or partial parotidectomy with facial nerve dissection.",
        "follow": "What is the approximate risk of malignant transformation over time, and what is the tumor called if that happens?",
        "follow_answer": "About 1.5 percent in the first 5 years, rising to near 10 percent after 15 years: carcinoma ex pleomorphic adenoma.",
        "mcq": {
            "question": "An adult has a painless parotid mass with normal facial nerve function. MRI shows a well-circumscribed, lobulated lesion that is very bright on T2, as here. FNA suggests pleomorphic adenoma. What is the best treatment?",
            "choices": [
                "Enucleation through a small incision",
                "Parotidectomy with facial nerve identification and an intact capsule",
                "Observation with yearly MRI because it is benign",
                "Primary radiotherapy"
            ],
            "answer": 1,
            "explanation": "Pleomorphic adenoma is excised with a cuff of normal tissue, by superficial or partial parotidectomy with facial nerve dissection. Enucleation or capsule rupture risks multinodular recurrence because of capsular pseudopodia. Observation leaves a risk of growth and malignant transformation over time.",
            "domain": "Thyroid / Parathyroid / Salivary",
            "topic": "Pleomorphic adenoma MRI"
        },
        "verify_note": "PMC11260653: 'Creative Commons Attribution License CC-BY 4.0' on the article page; Fig. 3 legend 'T2WI axial MRI image. Highlighted area shows the physical presentation of parotid gland tumor'. The article is a pleomorphic adenoma of the superficial and deep lobes. Image viewed in Chrome.",
        "variant_type": "interpret"
    },
    {
        "id": "hn_submand_sialolith_ct_v545",
        "level": 2,
        "concept_id": "hn:sialolithiasis",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/1eda/6504031/3e0aba518d92/cureus-0011-00000004180-i01.jpg",
        "image_credit": "Arifa SP, Christopher PJ, Kumar S, et al. Cureus. 2019;11(3):e4180 (CC BY) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6504031/",
        "prompt": "A patient has recurrent swelling under the jaw that comes on with meals. Axial (top) and sagittal (bottom) non-contrast CT. What do the arrows show, and where?",
        "answer": "A dense, well-defined calcification (sialolith) in the submandibular gland and duct region (arrows) on both views. Non-contrast CT is very sensitive for calcified stones.",
        "why": "About 80 to 90 percent of salivary stones are in the submandibular system, because its saliva is thicker and more alkaline and Wharton's duct runs uphill. Swelling at mealtimes (salivary colic) is the classic history.",
        "reason_prompt": "How does stone position change the treatment?",
        "reason_answer": "A distal stone that can be felt near the duct opening can be removed through the mouth by opening the duct (sialodochotomy). Small mobile stones can be removed with sialendoscopy. Larger proximal or hilar stones may need combined endoscopic and transoral approaches. Gland excision is reserved for intraglandular stones or failures, because it risks the marginal mandibular, lingual and hypoglossal nerves.",
        "teach_prompt": "Teach a junior why you should not inject contrast for this question.",
        "teach_answer": "Contrast can mask a small calcified stone against enhancing vessels and tissue. A non-contrast, thin-section CT is the test of choice to look for calculi; add contrast only if you are also looking for an abscess or a mass.",
        "follow": "What two nerves run close to the submandibular duct in the floor of the mouth?",
        "follow_answer": "The lingual nerve, which crosses beneath the duct (lateral to medial), and the hypoglossal nerve, which lies deeper and below.",
        "mcq": {
            "question": "A patient has painful swelling under the jaw that occurs when eating. Non-contrast CT shows the finding indicated by the arrows. Which statement is correct?",
            "choices": [
                "Most salivary stones arise in the parotid gland",
                "Gland-preserving options such as sialendoscopy or a transoral approach are first-line for an accessible ductal stone",
                "Contrast-enhanced CT is better than non-contrast CT for detecting stones",
                "Submandibular gland excision is the standard first treatment for any stone"
            ],
            "answer": 1,
            "explanation": "Most stones (80 to 90 percent) occur in the submandibular system. Accessible ductal stones are treated with gland-preserving approaches such as sialendoscopy or transoral removal. Non-contrast thin-section CT is the best test for calculi, and gland excision is kept for intraglandular stones or failures.",
            "domain": "Thyroid / Parathyroid / Salivary",
            "topic": "Submandibular sialolithiasis"
        },
        "verify_note": "PMC6504031: Creative Commons Attribution License statement on the article page; Fig. 1 legend 'Axial and sagittal view of computed tomography showing sialolith.' Title: sialolithiasis of the submandibular gland. Image viewed in Chrome.",
        "variant_type": "interpret"
    },
    {
        "id": "hn_parathyroid_mibi_v545",
        "level": 3,
        "concept_id": "hn:parathyroid-localization",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/3cf7/6854700/c2c015dd397e/13256_2019_2257_Fig2_HTML.jpg",
        "image_credit": "Al-Hassan MS, Mekhaimar M, El Ansari W, et al. J Med Case Rep. 2019;13:332 (CC BY 4.0) — Fig. 2",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6854700/",
        "prompt": "A patient has hypercalcemia with an elevated PTH. These are 99mTc-sestamibi images at 20 minutes and 2 hours (anterior views of the neck, then the neck and chest). Compare early and late images.",
        "answer": "Both the thyroid and the right-sided focus take up tracer early. At 2 hours the thyroid activity has washed out, but the right lower focus persists. Focal retained uptake on the delayed images is the signature of a hyperfunctioning parathyroid adenoma (here a giant right adenoma). The chest views show no mediastinal focus.",
        "why": "Sestamibi is retained longer in mitochondria-rich parathyroid adenomas than in thyroid tissue. That differential washout is why dual-phase imaging works; SPECT/CT adds 3D localization.",
        "reason_prompt": "Does a positive scan establish the diagnosis of primary hyperparathyroidism?",
        "reason_answer": "No. The diagnosis is biochemical (high or inappropriately normal PTH with hypercalcemia, after excluding familial hypocalciuric hypercalcemia). Imaging only localizes the gland to plan a focused operation. A negative scan is not a reason to withhold surgery from a patient who meets criteria.",
        "teach_prompt": "Teach a junior two causes of a false-positive sestamibi scan.",
        "teach_answer": "Thyroid nodules (especially oxyphilic or Hürthle-cell lesions) and reactive lymph nodes can retain tracer. That is why ultrasound or SPECT/CT is paired with sestamibi to confirm the focus is outside the thyroid.",
        "follow": "Where else should you look when the scan is negative or shows an ectopic gland?",
        "follow_answer": "The thymus and anterior mediastinum (inferior glands), the tracheoesophageal groove and retroesophageal space (superior glands), the carotid sheath, inside the thyroid, and undescended near the carotid bifurcation. 4D-CT can help.",
        "mcq": {
            "question": "A patient with primary hyperparathyroidism has dual-phase sestamibi imaging. The thyroid washes out by 2 hours, but a right lower neck focus persists, as shown. What does this pattern most likely represent?",
            "choices": [
                "A multinodular goiter",
                "A hyperfunctioning parathyroid adenoma",
                "Normal parathyroid glands",
                "Thyroid cancer metastatic to a lymph node"
            ],
            "answer": 1,
            "explanation": "Retained focal uptake after thyroid washout is the classic appearance of a parathyroid adenoma, because adenomas hold sestamibi longer than thyroid tissue. Normal parathyroids are not seen on sestamibi. Thyroid nodules can cause false positives, so correlate with ultrasound or SPECT/CT.",
            "domain": "Thyroid / Parathyroid / Salivary",
            "topic": "Parathyroid sestamibi localization"
        },
        "verify_note": "PMC6854700: CC BY 4.0 link on the article page; Fig. 2 legend 'Early and late 99mTc-sestamibi scintigraphy parathyroid scan images of neck and mediastinum anteriorly at 20 minutes and 2 hours showing increased focal uptake suggestive of right giant parathyroid adenoma'. Image viewed in Chrome.",
        "variant_type": "interpret"
    }
]
