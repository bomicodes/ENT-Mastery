# labs_v532/peds_dermoid.py: added after viewing in Chrome (2026-11-01). License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'peds-congenital'
CASES = [
    {
        "id": "pc_nasal_dermoid_mri_v532",
        "level": 3,
        "concept_id": "peds:nasal-dermoid",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/028c/11827921/1b0cddf5bf42/cureus-0017-00000077490-i02.jpg",
        "image_credit": "Wassef D, Patel D, Gravina A, Manzi B. Cureus. 2025;17(1):e77490 (CC BY 4.0) — Fig. 2",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11827921/",
        "prompt": "A 3-year-old has a recurrent midline pit on the nasal dorsum after an earlier excision. This is a coronal T2 MRI. The lower arrow points at the nasal septum and the upper arrow at the anterior skull base. What do you see, and why does it matter?",
        "answer": "There is a cystic lesion in the upper nasal septum (lower arrow), the residual nasal dermoid, and a separate lesion at the anterior skull base (upper arrow). Before re-excision, the surgeon has to know what lies at the skull base and whether a tract runs up through the foramen cecum and crista galli, because that decides whether a combined intracranial approach with neurosurgery is needed.",
        "why": "Nasal dermoid sinus cysts come from ectoderm trapped along the path of the embryonic dural diverticulum, so they can track from the dorsal skin through the septum to the foramen cecum and dura. Incomplete excision causes recurrence, as in this child.",
        "reason_prompt": "Why is MRI the key study, and what does CT add?",
        "reason_answer": "MRI shows the cyst, the tract and any intracranial component without radiation. CT shows the bony signs of a tract: a widened foramen cecum, a bifid or enlarged crista galli. They are complementary, and many surgeons get both before operating.",
        "teach_prompt": "Teach a junior the three midline nasal masses and the one move you never make.",
        "teach_answer": "Dermoid (a pit, sometimes with a hair, firm and non-compressible), glioma (firm, non-pulsatile, no connection or only a fibrous stalk) and encephalocele (soft, compressible, enlarges with crying: positive Furstenberg sign). Never biopsy or incise a midline nasal mass before imaging, because it may contain brain or CSF.",
        "follow": "In this recurrent case, what did the authors use to remove the whole tract?",
        "follow_answer": "A combined open rhinoplasty and vertical dorsal incision, which exposes the tract from the skin down through the septum so it can be removed in one piece.",
        "mcq": {
            "question": "A child has a midline nasal dorsum pit with a hair protruding from it. What is the next step?",
            "choices": [
                "Incision and drainage",
                "Needle biopsy in clinic",
                "MRI (with or without CT) to look for an intracranial tract before planning excision",
                "Observation until adolescence"
            ],
            "answer": 2,
            "explanation": "A pit with a hair is the classic sign of a nasal dermoid sinus. Image first, to look for a tract to the foramen cecum or dura; then excise the whole cyst and tract, with a combined intracranial approach if the tract extends there. Never drain or biopsy before imaging.",
            "domain": "Pediatric Otolaryngology",
            "topic": "Nasal dermoid sinus cyst"
        },
        "verify_note": "PMC11827921: 'open access article distributed under the terms of the Creative Commons Attribution License' on the article page; Fig. 2 legend 'Coronal T2 weighted image demonstrating the cyst in the nasal cavity/septum as well as the separate intracranial lesion.' Image viewed in Chrome."
    }
]
