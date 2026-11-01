# labs_v532/larynx_more.py: added after viewing in Chrome (2026-11-01). License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = "laryngeal-endoscopy"
CASES = [
    {
        "id": "lx_reinke_v532", "level": 2, "concept_id": "larynx:reinke-edema", "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/461c/9249694/62e5f2a79ba9/405_2022_7377_Fig2_HTML.jpg",
        "image_credit": "Grigaliute E, Fiamingo MN, Albanese PG, La Mantia I. Eur Arch Otorhinolaryngol. 2022;279(8):4053–4059 (CC BY 4.0) — Fig. 2",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9249694/",
        "prompt": "The left panel is a long-time smoker's larynx before surgery; the right panel is the same larynx after treatment and voice therapy. Describe the vocal folds on the left before naming anything.",
        "answer": "Left: both membranous vocal folds are diffusely swollen, pale and polypoid along their whole length, the classic appearance of Reinke's edema (polypoid corditis), with edema in the superficial lamina propria. Right: after phonosurgery the fold edges are straight and the glottis is clear.",
        "why": "Reinke's edema is bilateral and diffuse, unlike a focal polyp. It lowers vocal pitch, which women in particular notice, and is strongly tied to smoking; very large folds can narrow the airway.",
        "reason_prompt": "What is the first treatment, and when is surgery added?",
        "reason_answer": "Smoking cessation, reflux control and voice therapy come first. Surgery (microflap through a lateral incision with removal of the gelatinous material, or microdebrider in some centers) is offered for persistent voice problems or airway narrowing, ideally after the patient has stopped smoking. Treating one side at a time is often advised to lower the risk of an anterior web.",
        "teach_prompt": "Teach how to tell Reinke's edema from a vocal fold polyp in one sentence.",
        "teach_answer": "Reinke's is bilateral, diffuse and full-length in a smoker; a polyp is usually a single, focal lesion on one fold.",
        "follow": "What finding would make you biopsy rather than simply treat Reinke's edema?",
        "follow_answer": "Leukoplakia, erythroplakia, asymmetric stiffness or loss of mucosal wave, or a focal mass: these raise concern for dysplasia or carcinoma, which shares the smoking risk factor.",
        "mcq": {"question": "A 58-year-old woman who smokes has a voice that has deepened over several years. Laryngoscopy shows the findings in the left panel. What is the most appropriate first step?",
                "choices": ["Immediate bilateral stripping of the vocal folds", "Smoking cessation, reflux treatment and voice therapy",
                            "Radiation therapy", "Injection medialization of both vocal folds"], "answer": 1,
                "explanation": "Diffuse bilateral polypoid swelling in a smoker is Reinke's edema. Treatment starts with stopping smoking, controlling reflux and voice therapy; microflap surgery is reserved for persistent symptoms or airway compromise, and stripping is avoided because it scars the vibrating layer.",
                "domain": "Laryngology / Voice / Swallowing", "topic": "Reinke's edema"},
        "verify_note": "PMC9249694: Creative Commons Attribution 4.0 link on the article page; Fig. 2 legend 'Vocal cords before the microdebridement and at the post-operative follow-up after the speech therapy'. Image viewed in Chrome.",
    },
]
