# labs_v532/tbone_more.py: added 2026-11-01 after viewing each image in Chrome. License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'temporal-bone-imaging'
CASES = [
    {
        "id": "tb_chol_dwi_v545",
        "level": 4,
        "concept_id": "tb:non-epi-dwi",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/e2fc/6836394/e604f357140a/40463_2019_384_Fig1_HTML.jpg",
        "image_credit": "Choi DL, Gupta MK, Rebello R, et al. J Otolaryngol Head Neck Surg. 2019;48:58 (CC BY 4.0) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6836394/",
        "prompt": "A patient had a canal-wall-up tympanomastoidectomy for cholesteatoma. (A) Axial CT; (B) axial non-EPI diffusion-weighted MRI. What does each study show, and which answers the clinical question?",
        "answer": "CT (A) shows low-density soft tissue filling the attic, aditus and epitympanum (black arrow), which is nonspecific: it could be scar, granulation, fluid or cholesteatoma. Non-EPI DWI (B) shows a bright focus of restricted diffusion there (white arrow), which is characteristic of recurrent cholesteatoma. The MRI answers the question.",
        "why": "Keratin debris restricts diffusion, while granulation tissue and scar do not. Non-EPI techniques (such as HASTE or PROPELLER) reduce skull-base artifact and can detect cholesteatomas down to about 2 to 3 mm. That makes them a surveillance alternative to planned second-look surgery after canal-wall-up procedures.",
        "reason_prompt": "When does a negative non-EPI DWI not settle the question?",
        "reason_answer": "Very small pearls (under about 2 to 3 mm) can be missed, and motion or susceptibility artifact can degrade the study. Repeat imaging at intervals, and correlate with the clinical picture and otoscopy.",
        "teach_prompt": "Teach a junior what CT still adds when MRI is the better test for recurrence.",
        "teach_answer": "CT maps the bone: ossicular erosion, scutum, tegmen, lateral semicircular canal fistula and facial canal dehiscence. These guide surgical planning even when MRI is what identifies the cholesteatoma.",
        "follow": "Why are echo-planar (EPI) DWI sequences less useful here?",
        "follow_answer": "EPI DWI suffers susceptibility artifact at the air-bone interfaces of the temporal bone and has lower resolution, so small cholesteatomas are missed. Non-EPI sequences avoid much of this.",
        "mcq": {
            "question": "After a canal-wall-up tympanomastoidectomy, CT shows nonspecific soft tissue in the attic. Which study best distinguishes recurrent cholesteatoma from scar or granulation tissue?",
            "choices": [
                "Contrast-enhanced CT",
                "Non-echo-planar diffusion-weighted MRI",
                "Echo-planar diffusion-weighted MRI",
                "Repeat CT in 6 months"
            ],
            "answer": 1,
            "explanation": "Cholesteatoma restricts diffusion and appears bright on non-EPI DWI, while scar and granulation tissue do not. Non-EPI sequences reduce skull-base susceptibility artifact and detect small lesions, which EPI DWI often misses. CT cannot tell soft-tissue types apart by density.",
            "domain": "Otology / Neurotology",
            "topic": "Non-EPI DWI for recurrent cholesteatoma"
        },
        "verify_note": "PMC6836394: CC BY 4.0 link on the article page; Fig. 1 legend 'Patient with recurrent cholesteatoma following a canal-wall up tympanomastoidectomy. A) Axial unenhanced small field of view CT image demonstrates low density soft tissue... B) Axial 3 mm thick PROPELLER non-EPI DWMRI shows avid restricted diffusion... within the recurrent cholesteatoma'. Image viewed in Chrome.",
        "variant_type": "interpret"
    },
    {
        "id": "tb_noe_skullbase_v545",
        "level": 4,
        "concept_id": "tb:necrotizing-otitis-externa",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/c981/12584588/d393307199e8/cureus-0017-00000095710-i01.jpg",
        "image_credit": "Mahadevaswamy Susheela MK, Okunlola AO, Sufrian S, et al. Cureus. 2025;17(10):e95710 (CC BY 4.0) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12584588/",
        "prompt": "An older patient with poorly controlled type 2 diabetes has weeks of severe right otalgia and otorrhea despite topical drops. Axial CT at the skull base. Compare the right temporal bone and petrous region with the left.",
        "answer": "On the right (left side of the image) there is bone destruction of the temporal bone extending to the petrous apex and skull base, while the left is intact. In this setting it represents skull base osteomyelitis from necrotizing (malignant) otitis externa.",
        "why": "Necrotizing otitis externa, usually from Pseudomonas aeruginosa, spreads from the canal through the fissures of Santorini and the tympanomastoid suture to the skull base. Cranial neuropathies (VII first, then IX to XII) mark advanced disease.",
        "reason_prompt": "How do you confirm the diagnosis and monitor treatment?",
        "reason_answer": "Diagnose clinically: granulation at the bony-cartilaginous junction, pain out of proportion, a high ESR or CRP and a diabetic or immunocompromised host. Culture or biopsy the granulation, both to guide antibiotics and to exclude carcinoma. CT shows bone erosion and MRI shows soft-tissue and marrow extent. Follow treatment with symptoms, ESR or CRP and gallium or MRI, because bone changes on CT lag behind healing.",
        "teach_prompt": "Teach a junior the treatment backbone.",
        "teach_answer": "Prolonged anti-pseudomonal antibiotics (often 6 to 8 weeks: ciprofloxacin, or IV agents such as ceftazidime or piperacillin-tazobactam for severe or resistant disease), strict glucose control, aural toilet, and surgery only for sequestrum, abscess or biopsy. Persistent disease despite treatment calls for re-biopsy to exclude malignancy.",
        "follow": "Which cranial nerve is most often affected first, and why?",
        "follow_answer": "The facial nerve, at the stylomastoid foramen, which lies directly in the path of spread from the canal floor to the skull base.",
        "mcq": {
            "question": "A patient with poorly controlled diabetes has weeks of severe otalgia, canal granulation at the bony-cartilaginous junction and a raised ESR. CT shows the skull base destruction seen here. What is the most likely organism and the core treatment?",
            "choices": [
                "Staphylococcus aureus; 10 days of oral antibiotics",
                "Pseudomonas aeruginosa; prolonged anti-pseudomonal antibiotics with glucose control, guided by culture",
                "Aspergillus; topical antifungal drops alone",
                "Streptococcus pneumoniae; myringotomy"
            ],
            "answer": 1,
            "explanation": "Necrotizing otitis externa is usually caused by Pseudomonas aeruginosa. It is treated with weeks of culture-guided anti-pseudomonal therapy, strict glycemic control and aural toilet, with biopsy to exclude carcinoma. Fungal causes occur but need systemic antifungal treatment, not drops alone.",
            "domain": "Otology / Neurotology",
            "topic": "Necrotizing otitis externa"
        },
        "verify_note": "PMC12584588: 'Creative Commons Attribution License CC-BY 4.0' on the article page; Fig. 1 legend 'CT of the head showing tissue destruction of the right petrous apex and skull base'. Title: type 2 diabetes with complex necrotizing external otitis. Image viewed in Chrome. The age and history in the stem are illustrative.",
        "variant_type": "interpret"
    }
]
