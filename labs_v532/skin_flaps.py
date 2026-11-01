# labs_v532/skin_flaps.py: added after viewing in Chrome (2026-11-01). License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'skin-recon'
CASES = [
    {
        "id": "sk_bilobed_tip_v532",
        "level": 3,
        "concept_id": "skin:bilobed-flap",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b84c/7760386/6691cfb4565e/medicina-56-00639-g008.jpg",
        "image_credit": "Losco L, Bolletta A, Pierazzi DM, et al. Medicina (Kaunas). 2020;56(12):639 (CC BY 4.0) — Fig. 8",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7760386/",
        "prompt": "A 64-year-old has a basal cell carcinoma of the nasal tip, leaving a 1.4 cm defect. Panel (a) shows the flap marked before surgery; panel (b) is 12 months later. Name the flap and explain the design drawn in (a).",
        "answer": "It is a laterally based bilobed flap. The primary lobe is the same size as the defect and sits next to it; the secondary lobe is narrower, triangular and about 1.5 times as tall, and is placed where the skin is looser (the upper sidewall and dorsum). The defect is filled by the first lobe, the first lobe's donor site by the second lobe, and the second lobe's donor site is closed directly. The total arc of rotation is kept to about 90 to 100 degrees.",
        "why": "The bilobed flap moves the tension away from the stiff nasal tip skin to the looser upper nose, giving a good match in color and thickness for defects up to about 1.5 cm on the lower third of the nose.",
        "reason_prompt": "Which complications does the bilobed flap typically cause on the nose, and how do you reduce them?",
        "reason_answer": "Trapdoor (pincushion) deformity, alar notching or retraction, and dog-ears. Reduce them by keeping the total rotation to about 90 to 100 degrees (the Zitelli modification), undermining widely in the submuscular plane, excising the standing cone at the pivot point, and placing the flap away from the alar rim.",
        "teach_prompt": "Teach a junior when to choose a bilobed flap over a skin graft or a forehead flap on the nose.",
        "teach_answer": "A bilobed flap suits lower-third defects up to about 1.5 cm in patients with enough upper nasal skin laxity. A full-thickness graft is simpler but often a poorer match on the thick, oily tip. Larger defects, deep ones or those needing structural or lining support usually need a paramedian forehead flap.",
        "follow": "Why must margins be confirmed before a flap is raised for skin cancer?",
        "follow_answer": "A flap rearranges the surrounding tissue, so any residual tumor is hidden and spread under the flap; margin control (Mohs surgery or frozen sections) should come first.",
        "mcq": {
            "question": "A 1.3 cm defect of the nasal tip after Mohs surgery is to be closed with the flap shown. To reduce the risk of a trapdoor deformity and alar distortion, which design principle is most important?",
            "choices": [
                "Make the secondary lobe larger than the primary lobe",
                "Limit total rotation to about 90 to 100 degrees and undermine widely in the submuscular plane",
                "Rotate the lobes through 180 degrees",
                "Avoid undermining to protect the blood supply"
            ],
            "answer": 1,
            "explanation": "The Zitelli modification limits total rotation to about 90 to 100 degrees, and wide submuscular undermining reduces trapdoor deformity and distortion of the free alar margin. The secondary lobe is narrower than the primary lobe.",
            "domain": "Facial Plastics / Trauma",
            "topic": "Bilobed flap"
        },
        "verify_note": "PMC7760386: Creative Commons Attribution 4.0 link on the article page; Fig. 8 legend 'Bilobed flap. (a) Preoperative picture... BCC of the nasal tip. A laterally based bilobed flap was planned to repair the skin defect (1.4 cm)... (b) The 12-month postoperative picture'. Eyes are masked in both panels. Image viewed in Chrome."
    },
    {
        "id": "sk_nasolabial_ala_v532",
        "level": 4,
        "concept_id": "skin:nasolabial-flap",
        "variant_type": "interpret",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/b84c/7760386/d7bcd14e7e7d/medicina-56-00639-g009.jpg",
        "image_credit": "Losco L, Bolletta A, Pierazzi DM, et al. Medicina (Kaunas). 2020;56(12):639 (CC BY 4.0) — Fig. 9",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7760386/",
        "prompt": "A 68-year-old has had a melanoma of the nasal ala excised, leaving a full-thickness defect. Panels (a) to (d) show the reconstruction. Which three layers must be rebuilt, and where does each come from in this case?",
        "answer": "Lining, structural support and external skin. Here a nasolabial (cheek) flap was thinned and folded on itself to provide both lining and external cover (b), and a cartilage graft from the ear was shaped to support the ala and keep it from collapsing (b). Stage I (c) inset the flap with the donor site closed primarily along the nasolabial fold; a second stage divides and refines the flap. Panel (d) shows the result at 12 months.",
        "why": "A full-thickness alar defect fails if any of the three layers is missing: without lining the flap contracts, and without cartilage support the ala notches and collapses on inspiration.",
        "reason_prompt": "What are the drawbacks of the nasolabial flap for alar reconstruction?",
        "reason_answer": "It usually needs two stages; the cheek skin is bulky, causing a pincushion effect or blunting of the alar groove; it can flatten the nasolabial fold on that side; and it may carry hair in men. For larger or more complex defects, a paramedian forehead flap gives more reliable coverage.",
        "teach_prompt": "Teach a junior the options for nasal lining in full-thickness defects.",
        "teach_answer": "A folded or turn-in flap (as here), hinged local tissue, a septal mucoperichondrial flap, a full-thickness skin graft under a well-vascularized cover flap, or a free flap for very large defects. Lining is the layer most often forgotten.",
        "follow": "For melanoma, what must be settled before a staged flap reconstruction?",
        "follow_answer": "Clear margins on permanent sections (and staging, including sentinel node assessment when indicated), because a flap moves tissue and would hide residual disease.",
        "mcq": {
            "question": "After excision of an alar tumor, there is a full-thickness defect of the ala. Which plan best restores form and function?",
            "choices": [
                "Full-thickness skin graft alone",
                "Healing by secondary intention",
                "Reconstruct lining, add cartilage support and provide skin cover (for example a folded nasolabial flap with an ear cartilage graft)",
                "Primary closure under tension"
            ],
            "answer": 2,
            "explanation": "Full-thickness alar defects need all three layers: lining, structure (usually an ear cartilage graft) and cover. Without lining or support, the ala contracts, notches and collapses.",
            "domain": "Facial Plastics / Trauma",
            "topic": "Nasolabial flap"
        },
        "verify_note": "PMC7760386: Creative Commons Attribution 4.0 link on the article page; Fig. 9 legend 'Nasolabial folded flap... melanoma of the nasal ala... full-thickness defect in two stages... A cartilage graft... from the left auricle... Stage I... 12-month postoperative'. Eyes are masked in all panels. Image viewed in Chrome."
    }
]
