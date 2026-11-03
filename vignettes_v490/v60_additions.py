"""v60: one Anaplastic Thyroid Cancer item, replacing the lymphoma question re-filed under
Primary Thyroid Lymphoma (it was mislabeled), so the topic keeps >=7 board-style items."""

VIGNETTES = [
    {
        "topic": "Anaplastic Thyroid Cancer",
        "concept_id": "v6-thyroid-parathyroid-salivary-anaplastic-thyroid-cancer",
        "stem": "A 70-year-old man has a rapidly enlarging thyroid mass. Core biopsy shows anaplastic thyroid carcinoma, and staging shows multiple lung metastases. He has mild dysphagia, a normal voice, and no stridor; flexible laryngoscopy shows mobile vocal folds and a patent airway, and CT shows mild tracheal deviation without luminal narrowing. The team is discussing his airway while molecular results are pending. What is the most appropriate airway plan?",
        "choices": [
            "Elective tracheostomy now, before the tumor grows further",
            "Prophylactic endotracheal intubation until systemic therapy starts",
            "No prophylactic tracheostomy; close airway monitoring within a goals-of-care plan",
            "Tracheal stent placement now to prevent future obstruction",
        ],
        "answer": 2,
        "explanation": "In anaplastic thyroid carcinoma without airway compromise, the ATA guideline advises against routine prophylactic tracheostomy. A tracheostomy through or beside a rapidly growing tumor is technically difficult, can delay systemic therapy, and often worsens quality of life without improving survival. The airway should instead be watched closely, with a clear plan for urgent intervention, while staging, molecular testing for targets such as BRAF V600E, and goals-of-care discussions proceed. This patient has a patent airway and mobile vocal folds, so there is no current indication to secure it.",
        "why_wrong": [
            "Prophylactic tracheostomy in a patient with a patent airway adds morbidity and delays systemic therapy without a survival benefit.",
            "Prophylactic intubation is not indicated with a patent airway and carries its own risks, including difficult extubation.",
            "Correct.",
            "Stents are used for established obstruction in selected patients, not to prevent obstruction in a patent airway.",
        ],
        "board_pearl": "Anaplastic thyroid cancer with a patent airway: no prophylactic tracheostomy; monitor closely while molecular testing and goals-of-care decisions proceed.",
        "curveball": "If he developed stridor with a fixed vocal fold and tracheal narrowing, how would the decision change?",
        "curveball_answer": "Airway compromise changes the question to how and whether to secure the airway. Options include awake fiberoptic intubation, tracheostomy (sometimes awake, in an experienced team), or stenting, chosen in light of his goals, prognosis, and whether rapid systemic therapy such as BRAF-targeted treatment could shrink the tumor.",
        "learning_stage": "application",
        "focus": "management",
    },
]
