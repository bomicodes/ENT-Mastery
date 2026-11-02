# labs_v532/ctmri_more.py: added 2026-11-01 after viewing each image in Chrome. License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'ct-mri'
CASES = [
    {
        "id": "ct_rpa_lateral_film_v545",
        "level": 2,
        "concept_id": "ct:retropharyngeal-abscess",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/79f6/2740087/c3567e64f173/1757-1626-0002-0000006460-001.jpg",
        "image_credit": "Mydam J, Thiagarajan P. Cases J. 2009;2:6460 (CC BY 3.0) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2740087/",
        "prompt": "A 9-month-old has fever, irritability, decreased feeding and reluctance to move the neck. A lateral neck radiograph is taken. Look at the soft tissue in front of the upper cervical spine (arrow).",
        "answer": "The prevertebral (retropharyngeal) soft tissue in front of the upper cervical vertebrae is markedly thickened, pushing the airway forward (arrow). In an infant with fever and neck stiffness this indicates a retropharyngeal abscess; CT confirmed one, which in this child came from a mastoid abscess.",
        "why": "In children, prevertebral soft tissue wider than about 7 mm at C2, or more than half the vertebral body width, is abnormal. The film must be taken in true lateral position, with the neck extended, during inspiration, because flexion or crying can falsely widen it.",
        "reason_prompt": "What do you do next?",
        "reason_answer": "Contrast-enhanced CT of the neck to separate cellulitis or phlegmon from a drainable abscess (rim enhancement) and to look for spread to the mediastinum or carotid space. Start IV antibiotics and assess the airway. Small abscesses or phlegmon may respond to antibiotics; larger ones, or those that fail to improve, are drained, usually transorally.",
        "teach_prompt": "Teach a junior why retropharyngeal abscess is mostly a disease of young children.",
        "teach_answer": "The retropharyngeal lymph nodes (of Rouvière) drain the nasopharynx, adenoids, sinuses and middle ear and regress after about age 5. Suppuration of these nodes after an upper respiratory infection is the usual cause in toddlers; in adults, trauma or a foreign body is more typical.",
        "follow": "Which space lies behind the retropharyngeal space, and why does it matter?",
        "follow_answer": "The danger space, between the alar and prevertebral fascia. It runs from the skull base to the diaphragm, so infection there can spread straight into the posterior mediastinum.",
        "mcq": {
            "question": "An infant with fever, decreased feeding and neck stiffness has a lateral neck radiograph showing marked widening of the prevertebral soft tissue at C2, as here. What is the best next step?",
            "choices": [
                "Reassure and discharge, because infants normally have thick prevertebral tissue",
                "Contrast-enhanced CT of the neck and IV antibiotics, with airway assessment",
                "Lumbar puncture only",
                "Barium swallow"
            ],
            "answer": 1,
            "explanation": "Widened prevertebral soft tissue in a febrile infant with neck stiffness suggests a retropharyngeal infection. Contrast CT separates phlegmon from a drainable abscess and shows any spread, while IV antibiotics start and the airway is assessed. A poorly positioned film can falsely widen the space, but the clinical picture here demands imaging.",
            "domain": "Pediatric Otolaryngology",
            "topic": "Retropharyngeal abscess"
        },
        "verify_note": "PMC2740087: CC BY 3.0 link on the article page; Fig. 1 legend 'Plain radiograph lateral view of the neck taken at time of presentation showing retropharyngeal abscess.' Title: 'A nine month old child with retropharyngeal abscess secondary to mastoid abscess...'. Image viewed in Chrome.",
        "variant_type": "interpret"
    }
]
