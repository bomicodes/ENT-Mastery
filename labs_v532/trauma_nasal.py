# labs_v532/trauma_nasal.py: added after viewing in Chrome (2026-11-01). License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'facial-trauma-ct'
CASES = [
    {
        "id": "ft_nasal_bone_fx_v532",
        "level": 2,
        "concept_id": "trauma:nasal-bone-fracture",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/f353/12863636/e1f0f50921b5/cureus-0018-00000102841-i01.jpg",
        "image_credit": "Anirudh PB, Babu P, Sakalecha AK. Cureus. 2026;18(2):e102841 (CC BY 4.0) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12863636/",
        "prompt": "A 24-year-old was punched in the nose 2 days ago. This is an axial CT through the nasal bones. Describe the finding.",
        "answer": "One nasal bone (at the arrow) has a cortical break with a step-off: its lower segment is displaced inward relative to the upper part, so that side of the bony vault is depressed. The opposite nasal bone is intact. This is a displaced unilateral nasal bone fracture.",
        "why": "The nasal bones are the most commonly fractured facial bones. The decision to reduce depends on the clinical deformity and airway, not on the CT alone; imaging matters most when you suspect a more complex injury (septal, naso-orbito-ethmoid or orbital).",
        "reason_prompt": "What must you look for on examination that changes management today?",
        "reason_answer": "A septal hematoma: a boggy, bluish swelling of the septum that must be drained urgently to prevent cartilage necrosis, abscess and saddle nose. Also check for CSF rhinorrhea, telecanthus or a widened nasal root (naso-orbito-ethmoid injury), and eye movements and vision.",
        "teach_prompt": "Teach a junior when and how a simple nasal fracture is reduced.",
        "teach_answer": "Reassess once the swelling settles, usually at 3 to 7 days, and perform closed reduction within about 2 weeks (sooner in children) if there is a visible deformity or new obstruction. Reduce immediately only if swelling is minimal. Fractures with major septal deviation or ones that are found late may need open septorhinoplasty.",
        "follow": "Is CT required for every suspected isolated nasal fracture?",
        "follow_answer": "No. Isolated nasal fractures are a clinical diagnosis; imaging is for suspected additional injuries or medicolegal documentation. This study used CT as its reference standard and also tested ultrasound, which can show the same step-off.",
        "mcq": {
            "question": "Two days after a punch, a patient has the CT finding shown and a visibly deviated nose with marked swelling. The septum looks straight with no swelling. What is the most appropriate plan?",
            "choices": [
                "Open septorhinoplasty this week",
                "Reassess in 3 to 7 days when the swelling settles, with closed reduction within about 2 weeks if deformity persists",
                "No follow-up, because nasal fractures always heal straight",
                "Immediate open reduction and internal fixation with plates"
            ],
            "answer": 1,
            "explanation": "With marked swelling and no septal hematoma, the usual plan is to reassess at 3 to 7 days and perform closed reduction within about 2 weeks if there is a deformity or obstruction. Plate fixation is not used for simple nasal fractures.",
            "domain": "Facial Plastics / Trauma",
            "topic": "Nasal bone fracture"
        },
        "verify_note": "PMC12863636: 'open access article distributed under the terms of the Creative Commons Attribution License' on the article page; Fig. 1 legend 'Axial computed tomography scan of a displaced nasal bone fracture... cortical disruption and displacement.' Image viewed in Chrome. The age and history in the case stem are illustrative."
    }
]
