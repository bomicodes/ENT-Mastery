# labs_v532/sinus_ip_v55.py: added 2026-11-01 (v55). License and legend confirmed on the PMC page; image viewed in Chrome.
LAB = None
TARGET_LAB = 'sinus-ct'
CASES = [
    {
        "id": "sx_ip_ccp_mri_v55",
        "level": 4,
        "concept_id": "sinus:inverted-papilloma-mri",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8d2c/10552979/799c249915c1/ms9-85-5171-g003.jpg",
        "image_credit": "Mahat A, Yadav GK, Neupane D, et al. Ann Med Surg. 2023;85:5171 (CC BY 4.0) — Fig. 3",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10552979/",
        "prompt": "An adult with unilateral nasal obstruction and a polypoid mass has contrast-enhanced T1 MRI, axial (A) and coronal (B). Look at the internal texture of the enhancing mass (arrows).",
        "answer": "A unilateral enhancing mass filling the nasal cavity and maxillary/ethmoid region with alternating bands of high and low signal: a convoluted, striated or cerebriform pattern. That pattern is strongly associated with sinonasal inverted papilloma.",
        "why": "On MRI, the convoluted cerebriform pattern separates inverted papilloma from inflammatory polyps and from retained secretions. On CT, focal hyperostosis often marks the tumor's attachment site. Loss of the cerebriform pattern in part of the mass, bone destruction, or invasion beyond the sinus raises concern for squamous cell carcinoma, which occurs in a minority of cases.",
        "reason_prompt": "How do imaging findings guide the operation?",
        "reason_answer": "Identify the site of attachment (CT hyperostosis or the MRI pedicle) and the true extent of the tumor separate from obstructed secretions. Then plan an endoscopic approach that reaches the attachment, with subperiosteal removal and drilling of the underlying bone. Frontal, lateral maxillary or extensive disease may need extended endoscopic or combined approaches.",
        "teach_prompt": "Teach a junior why a unilateral nasal polyp in an adult needs imaging and biopsy.",
        "teach_answer": "Unilateral disease is a different differential from bilateral polyposis: inverted papilloma, malignancy (SCC, adenocarcinoma, melanoma, olfactory neuroblastoma), JNA in adolescent males, encephalocele and fungal disease. Image (CT, often MRI) before biopsy to exclude a vascular lesion or encephalocele.",
        "follow": "Why must inverted papilloma be followed long term after resection?",
        "follow_answer": "Recurrence is common when the attachment site is not fully cleared, and synchronous or metachronous squamous cell carcinoma can develop. Long-term endoscopic follow-up is standard.",
        "mcq": {
            "question": "An adult with a unilateral nasal mass has contrast MRI showing alternating bands of enhancing and nonenhancing tissue inside the mass (a convoluted, cerebriform pattern), as here. What is the most likely diagnosis?",
            "choices": [
                "Antrochoanal polyp",
                "Sinonasal inverted papilloma",
                "Allergic fungal rhinosinusitis",
                "Juvenile nasopharyngeal angiofibroma"
            ],
            "answer": 1,
            "explanation": "A convoluted cerebriform enhancement pattern in a unilateral sinonasal mass is the classic MRI appearance of inverted papilloma. Focal hyperostosis on CT often marks the attachment site. Loss of the pattern or bone destruction should raise concern for associated squamous cell carcinoma.",
            "domain": "Rhinology / Allergy / Skull Base",
            "topic": "Inverted papilloma MRI"
        },
        "verify_note": "PMC10552979: CC BY 4.0 link on the article page; Fig. 3 legend 'Axial section image of MRI nose and PNS on T1W sequence post enhancement (A), Coronal section image of MRI nose and PNS on T1W sequence post enhancement (B)'; article text describes a 'convoluted striated/cerebriform pattern' in this locally aggressive inverted papilloma. Image viewed in Chrome."
    }
]
