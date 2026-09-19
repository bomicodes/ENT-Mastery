"""Selective source-verified laryngopharyngitis Daily Curriculum repairs.

Rehomes three bounded prompt/answer pairs from the older v38.1 work without
importing that stale branch. Canonical topics and challenge fields are unchanged.
"""

DAILY_OVERRIDES = {
    ("Acute / Chronic Laryngopharyngitis", "localize"): (
        "How do duration, distribution, fold motion, focal lesions, systemic symptoms, and exposure history localize laryngopharyngeal inflammation without mistaking malignancy, paresis, or another disorder for laryngitis?",
        "Acute diffuse erythema and edema after viral symptoms or heavy voice use may fit a self-limited inflammatory process, but appearance alone is nonspecific. Document tobacco and inhalational exposure, medication use, immune status, voice demand, swallowing symptoms and time course, then examine fold motion and the full mucosal surface. A focal ulcer, leukoplakia, mass, unilateral stiffness, impaired motion, neck node, hemoptysis, weight loss, progressive dysphagia or persistent dysphonia should redirect evaluation toward neoplasm, paresis, scar, infection or another cause rather than a chronic-laryngitis label.",
    ),
    ("Acute / Chronic Laryngopharyngitis", "operate"): (
        "When does suspected laryngopharyngitis require operative examination or biopsy, and how should tissue be obtained without causing unnecessary vibratory scar?",
        "Uncomplicated diffuse inflammation is generally managed by treating the demonstrated cause, supportive care and follow-up rather than routine microlaryngoscopy. Operative examination or biopsy is appropriate when a persistent or progressive focal lesion, ulceration, leukoplakia, focal stiffness, unexplained impaired motion, airway concern, or inadequate office visualization leaves important pathology unresolved. Map the lesion and obtain representative tissue while preserving uninvolved epithelium and superficial lamina propria when oncologically safe; a nondiagnostic superficial sample should not override a persistently concerning clinical lesion.",
    ),
    ("Acute / Chronic Laryngopharyngitis", "teach"): (
        "How would you teach laryngopharyngitis as a descriptive inflammatory phenotype rather than a diagnosis that automatically justifies antibiotics, steroids, or reflux therapy?",
        "Begin with cause and time course: viral infection, phonotrauma, smoke or chemical exposure, inhaled medication, candidiasis, allergy, bacterial disease, immune dysfunction and reflux-related injury require different evidence and treatment. Erythema and edema are nonspecific and do not by themselves prove bacterial infection or reflux. Use symptoms, exposures, laryngeal visualization, motion, stroboscopy when useful, and evolution over time to narrow the mechanism. Persistent dysphonia or a focal, unilateral, stiff, ulcerated or progressive abnormality must reopen the differential rather than accumulate empiric antibiotics, steroids or reflux medication without an established indication.",
    ),
}


def apply_daily_curriculum_laryngology_selective_v383(items):
    stats = {"daily_pairs": 0, "topics": set()}
    for item in items:
        key = (item.get("topic"), item.get("stage"))
        override = DAILY_OVERRIDES.get(key)
        if not override:
            continue
        prompt, answer = override
        item["daily_prompt"] = prompt
        item["prompt"] = prompt
        item["answer"] = answer
        stats["daily_pairs"] += 1
        stats["topics"].add(item.get("topic"))
    stats["topics"] = len(stats["topics"])
    return stats


def install_daily_curriculum_laryngology_selective_v383(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v383():
        items = original_get_items()
        apply_daily_curriculum_laryngology_selective_v383(items)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v383
    app_module._adaptive_question = lambda item: item.get("daily_prompt") or item.get("prompt") or ""
    sample = get_adaptive_items_v383()
    return {"item_stats": apply_daily_curriculum_laryngology_selective_v383(sample)}
