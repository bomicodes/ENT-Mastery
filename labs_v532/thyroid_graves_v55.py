# labs_v532/thyroid_graves_v55.py: added 2026-11-01 (v55). License and legend confirmed on the PMC page; image viewed in Chrome.
LAB = None
TARGET_LAB = 'thyroid-ultrasound'
CASES = [
    {
        "id": "us_thyroid_inferno_v55",
        "level": 2,
        "concept_id": "thyroid:graves-doppler",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/95bd/2841467/afffc793d75a/ASM-29-323-g001.jpg",
        "image_credit": "Aldasouqi S, Sheikh A, Klosterman P. Ann Saudi Med. 2009;29(4):323 (CC BY) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2841467/",
        "prompt": "A 30-year-old woman has palpitations, weight loss and a low TSH with high free T4. Color Doppler of the thyroid is shown. Describe the vascular pattern and what it suggests.",
        "answer": "Diffuse, intense flow throughout the gland parenchyma, the 'thyroid inferno'. In a hyperthyroid patient, diffuse hypervascularity points to Graves disease, an overactive gland driven by TSH-receptor antibodies, rather than painless or subacute thyroiditis, where flow is normal or reduced.",
        "why": "The key distinction in thyrotoxicosis is overproduction (Graves, toxic nodules) versus release of stored hormone (thyroiditis). It decides between antithyroid drugs, radioiodine or surgery and supportive care. Doppler flow, TSH-receptor antibodies and, when needed, radioiodine uptake make that distinction.",
        "reason_prompt": "When is thyroidectomy preferred for Graves disease?",
        "reason_answer": "Large goiter with compression, suspicious or malignant nodules, moderate-to-severe active orbitopathy (radioiodine can worsen it), pregnancy planning in the near term, coexisting hyperparathyroidism, patient preference, or failure or intolerance of antithyroid drugs. Patients are made euthyroid first, and potassium iodide is often given before surgery to reduce gland vascularity.",
        "teach_prompt": "Teach a junior why preoperative potassium iodide is used before thyroidectomy for Graves disease.",
        "teach_answer": "Iodide transiently blocks hormone release (the Wolff-Chaikoff effect) and reduces the gland's blood flow and friability, the same hypervascularity seen on this Doppler, making the dissection safer.",
        "follow": "What finding would make you think of thyroiditis instead of Graves in a thyrotoxic patient?",
        "follow_answer": "Low or normal Doppler flow, low radioiodine uptake, negative TSH-receptor antibodies, a painful tender gland with a high ESR (subacute), or recent pregnancy (postpartum thyroiditis).",
        "mcq": {
            "question": "A thyrotoxic patient has diffuse, intense intraparenchymal color Doppler flow throughout the thyroid, as here. Which test result would most strongly confirm the likely diagnosis?",
            "choices": [
                "Low radioiodine uptake",
                "Positive TSH-receptor antibodies",
                "Elevated thyroglobulin with low uptake",
                "High ESR with a tender gland"
            ],
            "answer": 1,
            "explanation": "Diffuse hypervascularity ('thyroid inferno') in thyrotoxicosis suggests Graves disease, which is confirmed by TSH-receptor antibodies (or diffusely increased uptake). Low uptake, a tender gland with a high ESR, or low vascularity point to thyroiditis, in which preformed hormone leaks out.",
            "domain": "Thyroid / Parathyroid / Salivary",
            "topic": "Graves disease Doppler"
        },
        "verify_note": "PMC2841467: Creative Commons Attribution License statement on the article page; Fig. 1 legend 'Ultrasound of the thyroid showing an intense vascularity on color Doppler that is consistent with an \"inferno\"'. Article: Doppler ultrasonography in the diagnosis of Graves disease. Image viewed in Chrome. The vignette details are illustrative."
    }
]
