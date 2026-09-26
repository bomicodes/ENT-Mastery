"""v46.7: OR-prep "attending follow-up" depth gap-fill for a single late-added card.

or_prep_attending_followup_gapfill_v432.py (2026-09-22) brought 42 thin OR-prep
cards from 2 to >=3 attending-followup Q&A pairs. "Maxillomandibular Advancement"
was added to OR_PREP_REGISTRY the next day (2026-09-23, deep-audit resolution log
#5/#6) and so never received that pass -- it was the sole remaining card still at
2 pairs when the full registry was re-surveyed on 2026-09-25. This adds one new,
card-specific Q&A pair, grounded directly in the card's own danger/postop fields
(re-read in full immediately before authoring). No new cards, fields, or
source_basis citations are added -- this is assessment-depth parity, matching the
v432 pattern exactly.
"""

NEW_FOLLOWUP_BY_TITLE = {
    "Maxillomandibular Advancement": [
        "Why does the airway still need close monitoring right after an operation designed to enlarge it?",
        "The skeletal advancement enlarges the airway, but combined maxillary and mandibular osteotomies "
        "can cause acute soft-tissue edema or bleeding that transiently narrows it. If rigid "
        "maxillomandibular fixation is used, it also limits emergency oral access, so airway monitoring and a "
        "rescue plan (release of fixation, surgical airway availability) should be arranged before the patient "
        "leaves the OR, not improvised if obstruction develops.",
    ],
}


def apply_or_prep_mma_followup_gapfill_v467(data_module, app_module=None):
    orp = data_module.OR_PREP_REGISTRY
    result = {"updated": []}

    by_title = {card.get("title"): card for card in orp.values() if isinstance(card, dict)}

    for title, pair in NEW_FOLLOWUP_BY_TITLE.items():
        card = by_title.get(title)
        if card is None:
            raise RuntimeError(f"v46.7: OR-prep card missing from registry: {title}")
        followups = card.setdefault("attending_followup", [])
        existing_questions = {q for q, _ in followups}
        if pair[0] not in existing_questions:
            followups.append(pair)
            result["updated"].append(title)

    if app_module is not None:
        app_module.OR_PREP_REGISTRY = orp
    return result
