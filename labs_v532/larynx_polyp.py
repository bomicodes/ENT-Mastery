# labs_v532/larynx_polyp.py: added after viewing in Chrome (2026-11-01). License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'laryngeal-endoscopy'
CASES = [
    {
        "id": "lx_giant_polyp_v532",
        "level": 3,
        "concept_id": "larynx:vocal-fold-polyp",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/a8dc/6230337/d432ca2f802c/cpcem-02-361-g001.jpg",
        "image_credit": "Chida Y, Inokuchi R, Kumada Y, Shinohara K. Clin Pract Cases Emerg Med. 2018;2(4):361–362 (CC BY 4.0) — Image A–B",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6230337/",
        "prompt": "A 38-year-old heavy smoker has six months of breathlessness, wheeze and hoarseness and has been treated for asthma. Panel A is a sagittal neck CT; panel B is laryngoscopy. Describe what you see and where the obstruction is.",
        "answer": "Panel A shows a soft-tissue mass at the glottis, just below the epiglottis, narrowing the airway column. Panel B shows a large, smooth, pale, pedunculated mass arising from one vocal fold and filling most of the glottic opening, leaving only a small posterior airway. This is a giant vocal fold polyp; the 'asthma' was fixed upper-airway obstruction.",
        "why": "Most polyps are small and cause only hoarseness, but a large pedunculated polyp can ball-valve into the glottis and cause stridor that is mistaken for asthma. Wheeze that does not respond to asthma treatment, especially with hoarseness, should prompt a look at the larynx.",
        "reason_prompt": "How would you secure the airway before removing this lesion?",
        "reason_answer": "Plan the airway with anesthesia before any induction: the mass may obstruct completely once tone is lost. Options are awake tracheostomy under local anesthesia (what the authors did), or a carefully planned induction with jet ventilation or a small tube and a surgeon ready for an emergency surgical airway. Then remove the polyp by direct microlaryngoscopy and send it for histology.",
        "teach_prompt": "Teach a junior the clue that separates fixed upper-airway obstruction from asthma.",
        "teach_answer": "Asthma is expiratory, variable and responds to bronchodilators. A fixed upper-airway lesion gives stridor or monophonic wheeze that does not respond, often with voice change; the flow-volume loop flattens. When those features appear, look at the larynx.",
        "follow": "Why must a large 'polyp' in a heavy smoker always go to histology?",
        "follow_answer": "Benign polyps and early carcinoma share the same risk factor and can look alike, especially when large or irregular; only histology excludes dysplasia or carcinoma.",
        "mcq": {
            "question": "A heavy smoker treated for asthma for 6 months has worsening breathlessness and hoarseness. The CT and laryngoscopy are shown. What is the safest next step?",
            "choices": [
                "Increase inhaled steroids and add a long-acting bronchodilator",
                "Rapid-sequence induction and standard intubation, then excision",
                "Secure the airway (for example awake tracheostomy under local) and then excise by microlaryngoscopy",
                "Voice therapy and reflux treatment for 3 months"
            ],
            "answer": 2,
            "explanation": "A large pedunculated glottic polyp is causing fixed upper-airway obstruction. Secure the airway in a controlled way first (awake tracheostomy under local anesthesia in this case, or a planned shared-airway technique), then remove it by microlaryngoscopy and send it for histology. A standard induction risks complete obstruction.",
            "domain": "Laryngology / Voice / Swallowing",
            "topic": "Giant vocal fold polyp"
        },
        "verify_note": "PMC6230337: Creative Commons Attribution 4.0 link on the article page; legend 'A) Sagittal cervical computed tomography showing a hypodense mass below the epiglottis (arrow). B) Laryngoscopy showing an elevated vocal polyp (arrowhead).' Text: giant vocal cord polyp, resected after tracheostomy under local anesthesia. Image viewed in Chrome."
    }
]
