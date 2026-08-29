"""v29.7 — semantic alignment for allergic rhinitis vs local allergic rhinitis.

The v28.5 Concept Hub correctly distinguishes conventional systemic allergic rhinitis
from local allergic rhinitis (LAR), but the staged LAR application vignette still
stopped at recognizing that LAR *could* explain an allergic phenotype with negative
systemic testing.  This repair preserves the existing foundation and senior cases and
upgrades only that application layer to the clinically important confirmation step.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGET_ID = "v212_rhi_lar_app"
TOPIC = "Local Allergic Rhinitis"


def apply_rhinology_rhinitis_semantic_alignment_v297(challenges, item_id_fn):
    touched = []
    for q in challenges:
        if q.get("id") != TARGET_ID:
            continue

        q.update({
            "domain": DOMAIN,
            "topic": TOPIC,
            "concept_id": item_id_fn(DOMAIN, TOPIC),
            "learning_stage": "application",
            "stem": (
                "A 32-year-old has reproducible seasonal sneezing, nasal itching, watery rhinorrhea, "
                "and congestion, but properly performed skin-prick testing and serum allergen-specific "
                "IgE are repeatedly negative. At a specialty clinic, nasal allergen-specific IgE is also "
                "negative, yet the exposure history remains highly convincing and confirming an "
                "allergen-driven mechanism would change counseling about allergen-directed therapy. "
                "Which test best establishes local allergic rhinitis?"
            ),
            "choices": [
                "A controlled nasal allergen challenge/provocation test demonstrating a reproducible local nasal response",
                "Label the patient nonallergic solely because skin testing and serum specific-IgE are negative",
                "Begin empiric SCIT to several suspected allergens and use symptomatic improvement as the diagnostic test",
                "Obtain routine sinus CT; mucosal thickening would confirm local IgE-mediated allergy",
            ],
            "answer": 0,
            "explanation": (
                "Local allergic rhinitis is an allergic-rhinitis phenotype without demonstrable systemic "
                "sensitization in which a controlled nasal allergen challenge demonstrates a local allergen-specific "
                "response. Nasal specific-IgE can support the diagnosis when detected, but its sensitivity is limited; "
                "a negative nasal assay therefore does not exclude LAR. The application-level decision is not merely "
                "to name LAR after negative systemic testing, but to know when and how the local mechanism can be "
                "confirmed before committing the patient to allergen-directed treatment."
            ),
            "why_wrong": [
                "Correct. A reproducible positive nasal allergen challenge in the setting of an allergic phenotype and negative routine systemic sensitization testing is the key confirmatory test for LAR.",
                "Negative systemic testing does not by itself prove nonallergic rhinitis; it is precisely the setting in which a local allergen response may need to be investigated.",
                "Response to immunotherapy is not a diagnostic test, and empiric multi-allergen SCIT without a supported causal allergen exposes the patient to treatment burden and systemic-reaction risk without first establishing the mechanism.",
                "Sinus CT can evaluate structural disease or chronic rhinosinusitis when clinically indicated, but mucosal thickening is nonspecific and cannot demonstrate local allergen-specific IgE physiology.",
            ],
            "board_pearl": (
                "LAR is not 'allergy symptoms plus a negative blood test.' Think allergic phenotype + negative routine "
                "systemic sensitization + a demonstrable local nasal allergen response; nasal provocation is the key "
                "confirmatory concept, while nasal specific-IgE has limited sensitivity."
            ),
            "curveball": (
                "How would cold-air, perfume, or gustatory rhinorrhea without itching or exposure-specific sneezing "
                "shift the differential toward nonallergic/neurogenic rhinitis instead?"
            ),
            "tier": "Curated learning ladder",
            "mode": "Vignette",
            "focus": "boards",
            "ladder_reviewed": True,
            "semantic_review_v297": True,
        })
        touched.append(TARGET_ID)

    return {"touched": len(touched), "ids": touched, "topic": TOPIC}
