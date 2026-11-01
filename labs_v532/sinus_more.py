# labs_v532/sinus_more.py: added after viewing in Chrome (2026-11-01). License and legends confirmed on the PMC page.
LAB = None
TARGET_LAB = "sinus-ct"
_SRC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12085865/"
_CRED = "Subbiah NK, Bakshi SS, Arumugam S, Ghoshal JA. Cureus. 2025;17(4):e82506 (CC BY 4.0)"
CASES = [
    {
        "id": "sx_concha_types_v532", "level": 2, "concept_id": "sinus:concha-bullosa", "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2579/12085865/3e5cfe88f773/cureus-0017-00000082506-i02.jpg",
        "image_credit": _CRED + " — Fig. 2", "image_source": _SRC,
        "prompt": "Three coronal sinus CTs (A, B, C), each with an arrow on the middle turbinate. Describe where the air is in each turbinate before naming the variant.",
        "answer": "All three show middle turbinate pneumatization (concha bullosa): A is lamellar (air only in the vertical lamella), B is bulbous (air only in the bulbous inferior part), and C is extensive (both the lamella and the bulb are aerated).",
        "why": "An extensive or bulbous concha can crowd the middle meatus and ostiomeatal complex and is a common incidental finding; it matters when it narrows drainage in a symptomatic patient.",
        "reason_prompt": "When and how is a concha bullosa treated?",
        "reason_answer": "When it contributes to obstruction or disease, typically by removing the lateral half of the bulla (lateral resection) while keeping the medial lamella and attachment, which preserves the turbinate as a landmark and limits lateralization.",
        "teach_prompt": "Teach the three types in one line.",
        "teach_answer": "Lamellar means air in the vertical plate, bulbous means air in the bulb, extensive means both.",
        "follow": "Which other finding often accompanies a large concha bullosa on the same CT?",
        "follow_answer": "Septal deviation away from the concha, toward the opposite side.",
        "mcq": {"question": "On the coronal CTs shown, panel C has air in both the vertical lamella and the bulbous part of the middle turbinate. What type of concha bullosa is this?",
                "choices": ["Lamellar", "Bulbous", "Extensive", "Paradoxical middle turbinate"], "answer": 2,
                "explanation": "Pneumatization of both the lamella and the bulb is the extensive type. Lamellar involves only the vertical lamella, bulbous only the inferior bulb; a paradoxical turbinate is a curvature variant, not pneumatization.",
                "domain": "Rhinology / Allergy / Skull Base", "topic": "Concha bullosa"},
        "verify_note": "PMC12085865: 'Creative Commons Attribution License CC-BY 4.0' in Copyright and License information; Fig. 2 legend 'variation in middle turbinate pneumatization A: lamellar type; B: bulbous type; C: extensive type (concha bullosa)'. Image viewed in Chrome.",
    },
    {
        "id": "sx_cells_haller_agger_onodi_v532", "level": 3, "concept_id": "sinus:air-cells", "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2579/12085865/7fbc0aeed661/cureus-0017-00000082506-i03.jpg",
        "image_credit": _CRED + " — Fig. 3", "image_source": _SRC,
        "prompt": "Three coronal sinus CTs, each with an arrow on an air cell (A, B, C). Localize each cell relative to the orbit floor, the middle turbinate attachment and the sphenoid before naming it.",
        "answer": "A: a Haller (infraorbital ethmoid) cell along the orbital floor above the maxillary sinus, narrowing the infundibulum. B: an agger nasi cell, the most anterior ethmoid cell in front of and above the middle turbinate attachment. C: an Onodi (sphenoethmoidal) cell, a posterior ethmoid cell pneumatized above the sphenoid, close to the optic nerve.",
        "why": "These three are core CLOSE-checklist variants: Haller and agger nasi cells shape maxillary and frontal drainage, and the Onodi cell puts the optic nerve, sometimes the carotid, at risk during posterior ethmoid and sphenoid surgery.",
        "reason_prompt": "Which of the three carries the highest risk of a serious complication, and how do you avoid it?",
        "reason_answer": "The Onodi cell: mistaking it for the sphenoid sends dissection toward the optic nerve in its wall. Enter the true sphenoid medially and inferiorly via the natural ostium and keep away from the cell's superolateral wall.",
        "teach_prompt": "Teach where each cell sits in a breath.",
        "teach_answer": "Haller under the orbit, agger nasi in front of the middle turbinate, Onodi above the sphenoid next to the optic nerve.",
        "follow": "Why does the agger nasi cell matter for frontal sinus surgery?",
        "follow_answer": "It forms the anterior boundary of the frontal recess; opening its roof (the 'cap') is usually the key step to exposing the frontal sinus drainage pathway.",
        "mcq": {"question": "On the coronal CTs shown, the cell in panel C is a posterior ethmoid cell pneumatized above the sphenoid sinus. Which structure is most at risk if it is mistaken for the sphenoid during surgery?",
                "choices": ["Infraorbital nerve", "Anterior ethmoidal artery", "Optic nerve", "Nasolacrimal duct"], "answer": 2,
                "explanation": "An Onodi (sphenoethmoidal) cell can carry the optic nerve, and sometimes the carotid, in its wall; mistaking it for the sphenoid leads dissection toward the optic nerve. The infraorbital nerve relates to Haller cells and the orbital floor.",
                "domain": "Rhinology / Allergy / Skull Base", "topic": "Sinus air cells (Haller, agger nasi, Onodi)"},
        "verify_note": "PMC12085865: CC BY 4.0; Fig. 3 legend 'types of air cells A: Haller cell; B: agger nasi cell; C: Onodi cell'. Image viewed in Chrome.",
    },
]
