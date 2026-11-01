# labs_v532/tbone_atresia.py: added after viewing in Chrome (2026-11-01). License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'temporal-bone-imaging'
CASES = [
    {
        "id": "tb_aural_atresia_tmj_v532",
        "level": 4,
        "concept_id": "tb:aural-atresia",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/fdd2/9993528/7831f091d66b/40463_2022_615_Fig2_HTML.jpg",
        "image_credit": "Yang L, Chen P, Liu Y, Yang J, Zhao S. J Otolaryngol Head Neck Surg. 2023;52:24 (CC BY 4.0) — Fig. 2",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9993528/",
        "prompt": "A teenager has had conductive hearing loss in one ear since birth, with a near-normal auricle but no ear canal on that side. Axial (top) and coronal (bottom) temporal bone CT. Compare the two sides. What is missing on the affected side, and what is sitting where the canal should be?",
        "answer": "On the affected side (the right arrow on each image) there is no external auditory canal: the tympanic part of the temporal bone has not developed, so there is no bony canal or tympanic ring. The mandibular condyle sits further back than normal (retroposition), in the space where the canal should be. The other side (left arrow) has a normal tympanic bone and an aerated canal. The middle ear and mastoid on the affected side are still aerated.",
        "why": "Congenital aural atresia is assessed with the Jahrsdoerfer score, but this study showed a subgroup in whom the condyle occupies the would-be canal, so a canal cannot be drilled even when the score is favorable.",
        "reason_prompt": "If the Jahrsdoerfer score is 8, why might canaloplasty still be the wrong operation here?",
        "reason_answer": "The score grades the middle ear, ossicles and inner ear. It does not account for the TMJ. When the condyle is displaced back into the canal position, there is no safe room for a new canal, and drilling risks the TMJ. The authors concluded that conventional hearing reconstruction could not be done in these patients and offered a bone-conduction hearing aid, a Bonebridge or Vibrant Soundbridge implant, or no intervention for mild loss. They suggest adding TMJ position to the preoperative assessment.",
        "teach_prompt": "Teach a junior the CT checklist for aural atresia before atresiaplasty.",
        "teach_answer": "Stapes present? Oval and round windows open? Middle ear space size, mastoid pneumatization, malleus-incus complex, incus-stapes connection, and the facial nerve course (often displaced, with the mastoid segment more anterior and lateral). Also note the inner ear, any canal cholesteatoma, and the TMJ position relative to the would-be canal.",
        "follow": "What happens to the facial nerve's course in atresia that makes drilling risky?",
        "follow_answer": "The mastoid segment of the facial nerve is often displaced anteriorly and laterally and can cross the planned canal path, so preoperative CT mapping and facial nerve monitoring are essential.",
        "mcq": {
            "question": "A patient with unilateral congenital aural atresia has a Jahrsdoerfer score of 8, but CT shows the mandibular condyle displaced posteriorly into the expected canal position. Which statement is most accurate?",
            "choices": [
                "A high score guarantees a good canaloplasty result regardless of the TMJ",
                "TMJ retroposition can rule out conventional atresiaplasty; bone-conduction or active middle ear implant options are preferred",
                "The condyle should be resected to make room for the canal",
                "Cochlear implantation is the standard treatment"
            ],
            "answer": 1,
            "explanation": "In this series, retroposition of the condyle into the canal space meant conventional canal reconstruction could not be done despite high Jahrsdoerfer scores. Hearing was managed with bone-conduction aids, a Bonebridge or Vibrant Soundbridge, or observation for mild loss.",
            "domain": "Otology / Neurotology",
            "topic": "Congenital aural atresia"
        },
        "verify_note": "PMC9993528: Creative Commons Attribution 4.0 link on the article page; Fig. 2 legend 'Temporal bone HRCT of patient No. 13 in the axial and coronal sections. Right arrow, undeveloped tympanic portion of the temporal bone and retrodisplaced mandibular condyle; left arrow, normal tympanic portion of the contralateral ear.' Conclusions quoted from the abstract. Image viewed in Chrome. The age in the case stem is illustrative."
    }
]
