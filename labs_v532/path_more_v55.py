# labs_v532/path_more_v55.py: added 2026-11-01 (v55). License and legend confirmed on the PMC page; image viewed in Chrome.
LAB = None
TARGET_LAB = 'pathology'
CASES = [
    {
        "id": "path_acinic_v55",
        "level": 3,
        "concept_id": "path:acinic-cell-carcinoma",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/ddd3/12234930/6fb497db1528/12105_2025_1808_Fig2_HTML.jpg",
        "image_credit": "Chowdhury AN, DeSando S, Aly FZ. Head Neck Pathol. 2025;19:82 (CC BY 4.0) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12234930/",
        "prompt": "Parotid mass, H&E: (A) low power of the whole nodule, (B) high power. Describe the cells in B and name the tumor.",
        "answer": "Sheets of large polygonal cells with abundant granular, basophilic cytoplasm and round nuclei, recapitulating serous acinar cells. This is acinic cell carcinoma, a malignant salivary tumor that occurs mostly in the parotid.",
        "why": "Acinic cell carcinoma is usually low grade but malignant. It can recur late and occasionally metastasizes, as in this case, where it spread years later to the heart. It stains with DOG1 and is PAS-positive and diastase-resistant (zymogen granules). Most mammary analogue (secretory) carcinomas were once classified as acinic cell carcinoma; they carry an ETV6-NTRK3 fusion and lack zymogen granules.",
        "reason_prompt": "How is it treated, and why does follow-up need to be long?",
        "reason_answer": "Complete excision by parotidectomy with facial nerve preservation unless the nerve is involved. Neck dissection is added for clinical nodal disease or high-grade transformation, and adjuvant radiation for close or positive margins, high grade or advanced stage. Recurrence and metastasis can appear more than 10 years later, so follow-up is long term.",
        "teach_prompt": "Teach a junior the two special stains or markers that support acinic cell carcinoma.",
        "teach_answer": "PAS-positive, diastase-resistant cytoplasmic zymogen granules, and DOG1 positivity. If the tumor is S100- and mammaglobin-positive with an ETV6 rearrangement, think secretory carcinoma instead.",
        "follow": "Which salivary malignancy is the most common in children and adults, and which is second in children?",
        "follow_answer": "Mucoepidermoid carcinoma is the most common salivary malignancy in both; acinic cell carcinoma is the second most common in children.",
        "mcq": {
            "question": "A parotid tumor shows sheets of polygonal cells with abundant granular basophilic cytoplasm, as here, with PAS-positive diastase-resistant granules and DOG1 positivity. Which statement about this tumor is correct?",
            "choices": [
                "It is benign and needs only enucleation",
                "It is malignant and can recur or metastasize many years later, so follow-up is long term",
                "It always carries an ETV6-NTRK3 fusion",
                "It arises most often in minor salivary glands of the palate"
            ],
            "answer": 1,
            "explanation": "Acinic cell carcinoma is a usually low-grade salivary malignancy, mostly in the parotid. It can recur or metastasize late (this patient had cardiac metastasis), so treatment is complete parotidectomy and follow-up is long. ETV6-NTRK3 defines secretory carcinoma, its main mimic.",
            "domain": "Thyroid / Parathyroid / Salivary",
            "topic": "Acinic cell carcinoma histology"
        },
        "verify_note": "PMC12234930: CC BY 4.0 link on the article page; Fig. 1 legend 'Histology images of original parotid gland tumor: A) Low power magnification, B) High power magnification'; text: 'acinar cells with basophilic cytoplasm, prominent nucleoli... morphologically consistent with acinic cell carcinoma'. Image viewed in Chrome."
    },
    {
        "id": "path_enb_v55",
        "level": 4,
        "concept_id": "path:olfactory-neuroblastoma",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2ea4/3943513/5417448c08da/1746-1596-9-10-3.jpg",
        "image_credit": "von Zeidler SV, Guidi R, Alencar RCG, et al. Diagn Pathol. 2014;9:10 (CC BY 2.0) — Fig. 3",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3943513/",
        "prompt": "A sinonasal mass invading the oral cavity was biopsied. (A, B) H&E; the lower panels are immunostains for NSE, synaptophysin and vimentin. Describe the tumor and what the stains tell you.",
        "answer": "Islands and cords of small, uniform round-to-spindled blue cells with hyperchromatic nuclei in a fibrous stroma, strongly positive for the neuroendocrine markers NSE and synaptophysin. A small round blue cell tumor of the sinonasal tract with neuroendocrine differentiation is olfactory neuroblastoma (esthesioneuroblastoma), here with an atypical presentation into the mouth.",
        "why": "The sinonasal small round blue cell differential includes olfactory neuroblastoma, sinonasal undifferentiated carcinoma, neuroendocrine carcinoma, lymphoma, melanoma, rhabdomyosarcoma and NUT carcinoma. Immunostains separate them: ENB is synaptophysin/chromogranin-positive with S100-positive sustentacular cells and is usually negative or only weakly positive for keratin.",
        "reason_prompt": "What staging and grading systems matter, and what is the standard treatment?",
        "reason_answer": "Kadish (modified) or Dulguerov staging for extent and the Hyams histologic grade (I to IV) for prognosis. Standard treatment is complete resection, endoscopic or open craniofacial, including the cribriform plate and often the overlying dura and olfactory bulb. Adjuvant radiation follows for most, with neck management for nodal disease, which can appear late.",
        "teach_prompt": "Teach a junior the classic site and the classic rosette.",
        "teach_answer": "It arises from olfactory epithelium high in the nasal vault near the cribriform plate. Homer Wright pseudorosettes (tumor cells around fibrillary neuropil) and Flexner-Wintersteiner true rosettes are characteristic, though not always present, as in this specimen.",
        "follow": "Why does the neck need long-term surveillance?",
        "follow_answer": "Cervical nodal metastases develop in a meaningful minority, sometimes many years after treatment, and are a major cause of treatment failure.",
        "mcq": {
            "question": "A nasal vault mass near the cribriform plate shows small round blue cells in nests that are strongly synaptophysin-positive, as here. Which treatment approach is standard?",
            "choices": [
                "Primary chemotherapy alone",
                "Complete resection including the cribriform plate (endoscopic or craniofacial), usually followed by radiation",
                "Observation with serial MRI",
                "Endoscopic debulking of the nasal component only"
            ],
            "answer": 1,
            "explanation": "Olfactory neuroblastoma is treated with complete resection that includes the cribriform plate (and often the dura and olfactory bulb), typically followed by adjuvant radiation. Kadish/Dulguerov stage and Hyams grade guide prognosis. Chemotherapy is reserved for advanced or high-grade disease.",
            "domain": "Rhinology / Allergy / Skull Base",
            "topic": "Olfactory neuroblastoma histology"
        },
        "verify_note": "PMC3943513: CC BY 2.0 license on the article page; title 'Atypical esthesioneuroblastoma invading oral cavity'; Fig. 3 legend 'Histopathological and immunohistochemical findings. (A) ...islands and cords composed of small cells displaying either basaloid or fusiform morphology... (B) ...pleomorphic and hyperchromatic nuclei. The cells... were strongly positive for enolase (NSE), synaptophysin (SYN) and vimentin'. Image viewed in Chrome."
    }
]
