# labs_v532/ctmri_more.py: CT/MRI lab image cases. v54.7 (2026-11-01): the pediatric retropharyngeal
# abscess case now uses contrast CT (the diagnostic study) in place of the lateral neck film, and adds the
# Kawasaki-disease mimic from the same paper. License and legend confirmed on the PMC page; images viewed in Chrome.
LAB = None
TARGET_LAB = 'ct-mri'
CASES = [
    {
        "id": "ct_rpa_ring_v547",
        "level": 2,
        "concept_id": "ct:retropharyngeal-abscess",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d07c/9749284/1689b86bf07f/12969_2022_778_Fig2_HTML.jpg",
        "image_credit": "Chen YC, Pan HG, Jia DS, Wang HC, et al. Pediatr Rheumatol Online J. 2022;20:115 (CC BY 4.0) — Fig. 2",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9749284/",
        "prompt": "A young child has fever, neck pain, reduced neck movement and drooling. Panels (a) axial and (b) sagittal are contrast-enhanced neck CT; (c) and (d) are MRI. Describe the CT finding at the arrows: where is it, and what is its wall doing?",
        "answer": "A large fluid collection fills the retropharyngeal space behind the pharynx and in front of the prevertebral muscles, with marked mass effect pushing the airway forward and a rim of ring enhancement around it. A low-density collection with an enhancing wall is a retropharyngeal abscess. The MRI panels show the same left-sided collection with ring enhancement.",
        "why": "Contrast CT is the study that makes the diagnosis and drives treatment. It separates a drainable abscess (low-density center, enhancing rim, mass effect) from cellulitis or phlegmon and from retropharyngeal edema. It also shows spread toward the danger space and mediastinum or the carotid space. A lateral neck film can only show widened prevertebral soft tissue.",
        "reason_prompt": "How does the CT change the plan?",
        "reason_answer": "Phlegmon or a small collection can be treated with IV antibiotics and observation, with repeat imaging if there is no improvement in 24 to 48 hours. A sizeable rim-enhancing abscess, airway compromise or failure to improve calls for drainage, usually transoral. Extension into the mediastinum, carotid space involvement (jugular thrombosis, carotid erosion) or airway narrowing raises the urgency.",
        "teach_prompt": "Teach a junior the CT signs that separate a true abscess from retropharyngeal edema.",
        "teach_answer": "An abscess has a defined low-density collection with a complete enhancing rim and mass effect, often off to one side where the lateral retropharyngeal nodes are. Edema (from reactive inflammation, lymphadenitis or Kawasaki disease) is a smooth, bilateral, fluid-density widening that fills the space without a rim or mass effect. Edema does not need drainage.",
        "follow": "Why do retropharyngeal abscesses cluster in children under about 5?",
        "follow_answer": "The lateral retropharyngeal lymph nodes (of Rouvière) drain the nasopharynx, adenoids, sinuses and middle ear and regress later in childhood. Suppuration of these nodes after an upper respiratory infection is the usual cause.",
        "mcq": {
            "question": "A febrile 3-year-old with neck pain and limited neck movement has a contrast-enhanced CT showing a low-density retropharyngeal collection with a complete enhancing rim and mass effect on the airway, as here. The airway is stable. What is the best next step?",
            "choices": [
                "Discharge on oral antibiotics",
                "IV antibiotics and drainage of the abscess (usually transoral), with close airway monitoring",
                "Lumbar puncture",
                "IVIG and aspirin"
            ],
            "answer": 1,
            "explanation": "A low-density collection with ring enhancement and mass effect is a drainable retropharyngeal abscess. Start IV antibiotics and drain it (usually transorally), monitoring the airway closely. Small collections or phlegmon can be tried on IV antibiotics alone. IVIG belongs to Kawasaki disease, which can mimic this picture but shows edema without a rim.",
            "domain": "Pediatric Otolaryngology",
            "topic": "Retropharyngeal abscess CT"
        },
        "verify_note": "PMC9749284: CC BY 4.0 link on the article page; Fig. 2 legend 'Neck radiological findings of retropharyngeal abscess without KD. a, b Axial and sagittal enhanced neck CT images showing a large collection filling the retropharyngeal space. There is a marked mass effect and ring enhancement. c, d Axial T2fs MR image and axial postGd T1fs MR image showing a left-sided retropharyngeal fluid collection... with significant ring enhancement'. Image viewed in Chrome. The age and history in the stem are illustrative."
    },
    {
        "id": "ct_kd_rp_mimic_v547",
        "level": 4,
        "concept_id": "ct:retropharyngeal-edema-kawasaki",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d07c/9749284/df976fd0bba0/12969_2022_778_Fig1_HTML.jpg",
        "image_credit": "Chen YC, Pan HG, Jia DS, Wang HC, et al. Pediatr Rheumatol Online J. 2022;20:115 (CC BY 4.0) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9749284/",
        "prompt": "A young child with high fever and neck pain was sent in as a possible retropharyngeal abscess. Panels (a, b) are contrast CT and (c, d) MRI. Compare the retropharyngeal finding (arrows) with a true abscess: is there a rim?",
        "answer": "The retropharyngeal space is widened by a low-density, fluid-like area, but there is no significant ring enhancement and no defined walled collection. MRI shows fluid and soft-tissue edema, again without a rim. This is retropharyngeal edema, not an abscess. In this child it was the first sign of Kawasaki disease.",
        "why": "Kawasaki disease can present with fever, neck pain, cervical lymphadenopathy and retropharyngeal edema before the other features appear. Recognizing the missing rim on imaging avoids unnecessary drainage and delays to IVIG, which prevents coronary artery aneurysms.",
        "reason_prompt": "Which clinical clues should make you think of Kawasaki disease in this setting?",
        "reason_answer": "Fever lasting 5 days or more that does not respond to antibiotics, plus any of: bilateral non-exudative conjunctival injection, red cracked lips or strawberry tongue, a polymorphous rash, swelling or redness of the hands and feet (later peeling), and unilateral cervical lymphadenopathy. Inflammatory markers are high. Ask for an echocardiogram and involve pediatrics early.",
        "teach_prompt": "Teach a junior why 'no rim, no drainage' is the key decision on this CT.",
        "teach_answer": "Drainage needs a walled collection. A retropharyngeal hypodensity without an enhancing rim or mass effect is edema or early phlegmon. It is treated medically and re-imaged if the child does not improve. In a child with persistent fever despite antibiotics, consider Kawasaki disease rather than taking them to the OR.",
        "follow": "What is the treatment that prevents the main complication of Kawasaki disease, and what is that complication?",
        "follow_answer": "IVIG (with aspirin), given ideally within 10 days of fever onset, which reduces the risk of coronary artery aneurysms.",
        "mcq": {
            "question": "A 4-year-old with 6 days of fever, unilateral neck swelling and neck pain has not improved on IV antibiotics. CT shows widening of the retropharyngeal space with low density but no enhancing rim, as here. She also has red cracked lips and bilateral conjunctival injection. What is the most appropriate next step?",
            "choices": [
                "Transoral incision and drainage",
                "Evaluate for Kawasaki disease (echocardiogram, inflammatory markers) and treat with IVIG if confirmed",
                "Switch to a broader-spectrum antibiotic and repeat CT in 1 week",
                "Biopsy the retropharyngeal tissue to exclude lymphoma"
            ],
            "answer": 1,
            "explanation": "Retropharyngeal edema without ring enhancement, persistent fever unresponsive to antibiotics, and mucocutaneous signs point to Kawasaki disease mimicking a retropharyngeal abscess. Drainage is not indicated without a walled collection. Prompt evaluation and IVIG lower the risk of coronary aneurysms.",
            "domain": "Pediatric Otolaryngology",
            "topic": "Kawasaki disease mimicking retropharyngeal abscess"
        },
        "verify_note": "PMC9749284: CC BY 4.0 link on the article page; title 'Clinical features of Kawasaki disease initially mimicking retropharyngeal abscess'; Fig. 1 legend 'Neck radiological findings of KD initially presenting as retropharyngeal abnormality. a, b Axial and sagittal enhanced neck CT images showing a widening of the retropharyngeal space with a hypodense area without significant ring enhancement (arrow). c, d Axial T2fs MR image and sagittal postGd T1fs MR image showing a retropharyngeal fluid collection with soft tissue oedema without significant ring enhancement'. Image viewed in Chrome. The vignette details are illustrative."
    }
]
