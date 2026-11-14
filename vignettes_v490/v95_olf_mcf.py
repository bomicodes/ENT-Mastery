"""v95: smell loss as an early sign of neurodegenerative disease; facial nerve risk of the middle fossa approach."""

OLF = "v6-rhinology-allergy-skull-base-olfactory-dysfunction"
VS = "v6-otology-neurotology-vestibular-schwannoma"

VIGNETTES = [
    {
        "topic": "Olfactory Dysfunction",
        "concept_id": OLF,
        "stem": "A 71-year-old man reports that food has tasted bland for about 3 years. Nasal endoscopy is normal and he has no history of sinus disease, head injury or recent viral illness. Smell testing confirms moderate hyposmia. His wife notes that his handwriting has become smaller, and on examination he has a subtle resting tremor of the right hand. What is the most appropriate interpretation?",
        "choices": [
            "Age-related smell loss only; reassure and recheck in a year",
            "Chronic rhinosinusitis without polyps is the likely cause despite the normal endoscopy",
            "Smell loss can be an early sign of Parkinson disease; refer to neurology",
            "Smell loss is unrelated to neurologic disease; obtain a sinus CT",
        ],
        "answer": 2,
        "explanation": "Smell loss is common with age, affecting about half of adults aged 65 to 80, but it is also one of the earliest features of Parkinson disease, often preceding the motor signs by years. It is also common in Alzheimer disease, Lewy body dementia and multiple sclerosis. With a resting tremor and micrographia, his hyposmia should prompt neurology referral rather than reassurance or sinus imaging.",
        "why_wrong": [
            "Presbyosmia is common, but a resting tremor and small handwriting point to a neurodegenerative cause that needs evaluation.",
            "Normal endoscopy and no sinonasal symptoms make chronic rhinosinusitis unlikely.",
            "Correct.",
            "Olfactory loss is closely linked to neurodegenerative disease; a sinus CT is not the next step here.",
        ],
        "board_pearl": "Unexplained hyposmia in an older adult can be an early sign of Parkinson or Alzheimer disease: look for tremor, rigidity, slowing and memory change, and refer to neurology.",
        "curveball": "Besides neurologic disease, what else does smell loss in older adults predict?",
        "curveball_answer": "Higher mortality, independent of other health factors, and safety risks such as failing to detect smoke, gas leaks or spoiled food. It is also associated with depression and lower quality of life, so counsel on smoke and gas detectors and food dating.",
        "learning_stage": "application",
        "focus": "diagnosis",
    },
    {
        "topic": "Vestibular Schwannoma",
        "concept_id": VS,
        "stem": "A 45-year-old woman with a 9-mm intracanalicular vestibular schwannoma, 100% word recognition and a strong wish to keep her hearing chooses surgery. You are counseling her about a middle cranial fossa approach compared with retrosigmoid and translabyrinthine approaches. Which statement about facial nerve risk is most accurate?",
        "choices": [
            "The middle fossa approach carries the lowest risk of facial weakness because the tumor is small",
            "The middle fossa approach carries the highest risk of facial weakness, because the facial nerve lies on the superior surface of the tumor in the surgeon's path",
            "Facial nerve risk is identical across all three approaches",
            "Only the translabyrinthine approach puts the facial nerve at risk",
        ],
        "answer": 1,
        "explanation": "Through the middle fossa, the surgeon approaches the internal auditory canal from above, where the facial nerve lies in the anterosuperior canal, so it sits between the surgeon and a tumor arising from the inferior vestibular nerve and must be worked around. Comparisons of approaches report the highest rate of facial weakness with the middle fossa route, much of it early and temporary, which is part of the tradeoff for its better hearing preservation in small intracanalicular tumors with good hearing. The translabyrinthine and retrosigmoid approaches reach the tumor without crossing the nerve first.",
        "why_wrong": [
            "Small tumor size favors hearing preservation through the middle fossa, but the nerve's position still makes facial weakness more common.",
            "Correct.",
            "Risk differs by approach because the nerve's relationship to the surgeon's path differs.",
            "All three approaches put the facial nerve at risk; the translabyrinthine route actually exposes it early and reliably at the fundus.",
        ],
        "board_pearl": "Middle fossa approach: best hearing preservation for small intracanalicular tumors with good hearing, but the highest facial nerve risk, because the nerve lies on top of the tumor in the surgical path.",
        "curveball": "Which tumor arising from which nerve makes the middle fossa approach harder?",
        "curveball_answer": "A tumor from the inferior vestibular nerve lies below the facial nerve, so the surgeon must work around the nerve to reach it; a superior vestibular nerve tumor is easier to remove from above. Tumors reaching the lateral fundus also favor the middle fossa over retrosigmoid for hearing preservation.",
        "learning_stage": "mastery",
        "focus": "surgery",
    },
]
