# labs_v532/airway_laryngomalacia.py: added after viewing in Chrome (2026-11-01). License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'airway-bronchoscopy'
CASES = [
    {
        "id": "aw_laryngomalacia_v532",
        "level": 2,
        "concept_id": "airway:laryngomalacia",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/efa0/3299329/c61d9ca2e12c/IJPED2012-753526.001.jpg",
        "image_credit": "Landry AM, Thompson DM. Int J Pediatr. 2012;2012:753526 (CC BY) — Fig. 1a–c",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3299329/",
        "prompt": "A 6-week-old has noisy inspiratory breathing that is worse when feeding, crying and lying on the back. The figure shows three endoscopic views (the authors' labels are on the image). Describe the anatomy in (a) and (b), and what was done in (c).",
        "answer": "(a) The epiglottis is curled into an omega shape. (b) A tubular epiglottis with redundant mucosa over the arytenoids that prolapses into the glottis on inspiration. (c) After supraglottoplasty, the redundant supra-arytenoid tissue has been removed and the airway is open. These are the findings of laryngomalacia: inspiratory collapse of floppy supraglottic tissue.",
        "why": "Laryngomalacia is the most common cause of stridor in infants. The diagnosis is made by awake flexible laryngoscopy, watching the supraglottis collapse on inspiration; the static shape of the epiglottis alone is not diagnostic, because an omega epiglottis is also seen in infants without symptoms.",
        "reason_prompt": "Which features make you offer supraglottoplasty instead of watchful waiting?",
        "reason_answer": "Most infants have mild disease that resolves by 12 to 18 months. Surgery is for severe disease: failure to thrive or poor weight gain from feeding difficulty, apneas or cyanotic episodes, significant obstructive sleep apnea, pulmonary hypertension or cor pulmonale, or severe retractions. Treat reflux, which often coexists, and look for a second airway lesion when the course is atypical.",
        "teach_prompt": "Teach a junior the three anatomic patterns of laryngomalacia.",
        "teach_answer": "Prolapse of redundant arytenoid mucosa; short aryepiglottic folds, often with a curled (omega or tubular) epiglottis; and posterior collapse of the epiglottis. Many infants have more than one. Supraglottoplasty is tailored to the pattern: trim the arytenoid mucosa, divide the aryepiglottic folds, or perform an epiglottopexy.",
        "follow": "When should you do a full airway endoscopy rather than rely on flexible laryngoscopy alone?",
        "follow_answer": "When symptoms are severe, the course is atypical (for example biphasic stridor, a hoarse or weak cry, or no improvement) or surgery is planned, because a meaningful minority (often quoted around 15 to 20 percent) have a second airway lesion such as subglottic stenosis or tracheomalacia.",
        "mcq": {
            "question": "A 3-month-old with the endoscopic findings in panels (a) and (b) is feeding well, gaining weight and has no apneas or cyanosis. What is the best management?",
            "choices": [
                "Supraglottoplasty now",
                "Tracheostomy",
                "Observation, reflux management if symptomatic, and regular weight checks",
                "Repeat endoscopy under general anesthesia every 3 months"
            ],
            "answer": 2,
            "explanation": "Mild laryngomalacia (stridor without feeding difficulty, poor growth, apnea or cyanosis) is managed expectantly, with reflux treatment when indicated and growth monitoring; most cases resolve by 12 to 18 months. Supraglottoplasty is for severe disease.",
            "domain": "Pediatric Otolaryngology",
            "topic": "Laryngomalacia"
        },
        "verify_note": "PMC3299329: 'open access article distributed under the Creative Commons Attribution License' on the article page; legend '(a) Omega-shaped epiglottis. (b) A tubular-shaped epiglottis along with redundant supra-arytenoid tissue which is obstructing the glottis during inspiration. (c) the site of redundant supra-arytenoid tissue after surgical removal.' Image viewed in Chrome."
    }
]
