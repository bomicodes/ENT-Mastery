# labs_v532/swallow_more.py: added after viewing in Chrome (2026-11-01). License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = "swallow"
CASES = [
    {
        "id": "sw_cp_bar_v532", "level": 3, "concept_id": "swallow:cricopharyngeal-bar", "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/225e/10124148/6438497b534c/cureus-0015-00000036663-i03.jpg",
        "image_credit": "Pittala K, Reinhart N, Sujka JA, Velanovich V, DuCoin CG. Cureus. 2023;15(3):e36663 (CC BY) — Fig. 3",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10124148/",
        "prompt": "Lateral barium swallow in an older adult with solid-food dysphagia felt in the throat. Describe the contour of the posterior pharyngoesophageal junction (arrow) before naming the finding.",
        "answer": "A smooth, shelf-like indentation of the posterior wall at the pharyngoesophageal junction (about the C5–C6 level) narrows the column of barium: a cricopharyngeal bar, the radiographic sign of a cricopharyngeus that does not relax or open fully.",
        "why": "A bar marks upper esophageal sphincter dysfunction, the same physiology that can lead to a Zenker diverticulum. It can also be incidental, so it is treated only when it matches the symptoms.",
        "reason_prompt": "How do you tell a bar from a Zenker diverticulum and from an esophageal web on the same study?",
        "reason_answer": "A bar indents the posterior wall without an outpouching. A Zenker diverticulum is a barium-filled pouch above the cricopharyngeus, through Killian's dehiscence. A web is a thin, often anterior, shelf just below the sphincter.",
        "teach_prompt": "Teach the treatment ladder for a symptomatic bar.",
        "teach_answer": "Rule out a neurologic cause and assess the pharyngeal squeeze. Then dilation or botulinum toxin to test the response, and cricopharyngeal myotomy (endoscopic, open or per-oral endoscopic) for a durable result.",
        "follow": "Why does a weak pharyngeal squeeze change how you counsel a patient before myotomy?",
        "follow_answer": "Myotomy lowers outflow resistance but cannot add pharyngeal propulsion; with poor pharyngeal contraction the benefit is smaller and aspiration risk must be weighed.",
        "mcq": {"question": "A 72-year-old has solid-food dysphagia localized to the throat. The lateral barium swallow shown has a smooth posterior indentation at the pharyngoesophageal junction with no outpouching. Which treatment gives the most durable relief if symptoms match?",
                "choices": ["Proton pump inhibitor alone", "Cricopharyngeal myotomy", "Fundoplication", "Esophageal stent"], "answer": 1,
                "explanation": "This is a cricopharyngeal bar from a non-relaxing upper esophageal sphincter. Dilation or botulinum toxin can help short term, but cricopharyngeal myotomy (endoscopic, open or per-oral) gives the most durable relief in symptomatic patients.",
                "domain": "Laryngology / Voice / Swallowing", "topic": "Cricopharyngeal bar"},
        "verify_note": "PMC10124148: 'distributed under the terms of the Creative Commons Attribution License' in Copyright and License information; Fig. 3 legend 'Case 2: Barium swallow study showing the presence of a cricopharyngeal bar.' Image viewed in Chrome.",
    },
]
