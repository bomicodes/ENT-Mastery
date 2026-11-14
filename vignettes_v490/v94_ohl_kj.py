"""v94: oral hairy leukoplakia (confirmation, meaning, management); Killian-Jamieson diverticulum."""

IMM = "v6-general-ent-emergencies-immunocompromised-host-in-otolaryngology"
ZD = "v6-laryngology-voice-swallowing-zenker-diverticulum"

VIGNETTES = [
    {
        "topic": "Immunocompromised Host in Otolaryngology",
        "concept_id": IMM,
        "stem": "A 34-year-old man with no known medical history has painless, white, vertically ridged plaques on both lateral borders of the tongue that do not wipe off and did not change with a course of fluconazole. Biopsy shows hyperparakeratosis with ballooned epithelial cells and little inflammation, and in situ hybridization is positive for Epstein-Barr virus. Which statement about this diagnosis is most accurate?",
        "choices": [
            "Human papillomavirus is the causative agent",
            "It most often arises on the buccal mucosa",
            "It is premalignant and should be excised with margins",
            "A confirmed diagnosis almost always reflects systemic immunosuppression, so he should be tested for HIV",
        ],
        "answer": 3,
        "explanation": "This is oral hairy leukoplakia, caused by Epstein-Barr virus replication in the tongue epithelium and confirmed by biopsy with in situ hybridization for EBV. It almost always occurs with systemic immunosuppression: HIV most often, but also organ transplant immunosuppression, chemotherapy or steroids. In a patient with no known cause, the key next step is HIV testing. The lesion is not premalignant and needs no specific treatment; it usually regresses once immunity is restored, for example with antiretroviral therapy.",
        "why_wrong": [
            "Epstein-Barr virus, not human papillomavirus, causes oral hairy leukoplakia.",
            "The lateral border of the tongue is the typical site; the dorsum, buccal mucosa and floor of mouth are less common.",
            "It is not premalignant; management is diagnosis and treatment of the underlying immunosuppression, not excision.",
            "Correct.",
        ],
        "board_pearl": "Oral hairy leukoplakia = EBV on the lateral tongue, confirmed by biopsy with EBV in situ hybridization; it almost always means immunosuppression, so test for HIV. Not premalignant; regresses with antiretroviral therapy.",
        "curveball": "His HIV test is negative. What else should you look for?",
        "curveball_answer": "Other causes of immunosuppression: organ or stem-cell transplant drugs, chemotherapy, systemic or high-dose inhaled corticosteroids, hematologic malignancy, or another immunodeficiency. It is rare but reported in apparently immunocompetent people, so the history and a basic immune workup guide the search.",
        "learning_stage": "application",
        "focus": "diagnosis",
    },
    {
        "topic": "Zenker Diverticulum",
        "concept_id": ZD,
        "stem": "A 70-year-old woman with mild dysphagia has a barium esophagram showing a 2-cm pouch projecting laterally to the left from the anterolateral wall of the cervical esophagus, just below the cricopharyngeal bar. She is referred for endoscopic stapler diverticulotomy. What is the main concern with this plan?",
        "choices": [
            "The pouch is too large for the stapler",
            "This is a Killian-Jamieson diverticulum, and its neck lies near where the recurrent laryngeal nerve enters the larynx",
            "Endoscopic stapling is contraindicated in patients over 65",
            "Lateral pouches always contain carcinoma",
        ],
        "answer": 1,
        "explanation": "A pouch arising below the cricopharyngeus from the anterolateral cervical esophagus, lateral to the longitudinal muscle, is a Killian-Jamieson diverticulum, not a Zenker diverticulum (which arises in the posterior midline above the cricopharyngeus through Killian's dehiscence). The recurrent laryngeal nerve runs close to the Killian-Jamieson space as it enters the larynx, so dividing the common wall endoscopically risks the nerve. Symptomatic pouches are traditionally managed by transcervical diverticulectomy with the nerve identified and protected; small asymptomatic ones can be observed. Endoscopic division has been reported in selected cases at experienced centers but is not the default.",
        "why_wrong": [
            "At 2 cm the issue is not size but the location and the nearby recurrent laryngeal nerve.",
            "Correct.",
            "Age alone does not contraindicate endoscopic treatment; for Zenker diverticulum, endoscopic stapling is often favored in older patients.",
            "Carcinoma in a diverticulum is rare; it is a reason to inspect the pouch, not the main concern here.",
        ],
        "board_pearl": "Killian-Jamieson diverticulum: anterolateral, below the cricopharyngeus, next to the recurrent laryngeal nerve entry point, so open transcervical excision with nerve protection rather than routine endoscopic stapling.",
        "curveball": "How do you tell the two pouches apart on the lateral view of the esophagram?",
        "curveball_answer": "A Zenker pouch arises posteriorly above the cricopharyngeal bar and hangs behind the esophagus. A Killian-Jamieson pouch arises below the bar from the anterolateral wall, so on the frontal view it projects to the side (often the left) and on the lateral view it overlaps the esophagus rather than sitting behind it.",
        "learning_stage": "application",
        "focus": "anatomy",
    },
]
