"""Focused question-answer alignment and curveball repairs for Daily Curriculum v37.1.

Reconciled onto current production after the newer question-quality and domain-specific
why-wrong layers. This first bounded cohort fixes high-value prompt/answer mismatches
without changing canonical topics or the challenge distractor-reasoning fields.
"""

DAILY_OVERRIDES = {
    ("MEN2 / RET", "teach"): (
        "In a patient with MEN2 who is preparing for thyroidectomy, which associated tumor must be excluded first, and why does the order matter?",
        "Exclude pheochromocytoma before thyroid surgery. An unrecognized catecholamine-secreting tumor can cause a life-threatening hypertensive crisis during anesthesia or manipulation, so biochemical evaluation and treatment of pheochromocytoma precede thyroidectomy.",
    ),
    ("Ethmoidectomy", "manage"): (
        "When does ethmoidectomy enter the CRS treatment pathway, and how should disease extent determine the operation?",
        "Offer surgery for appropriately selected objective ethmoid disease that remains burdensome despite suitable medical therapy or when a complication demands source control. Match the dissection to disease and access needs, preserve mucosa and reliable landmarks, and discuss continued postoperative topical therapy rather than presenting surgery as a cure for the inflammatory phenotype.",
    ),
    ("Juvenile Nasopharyngeal Angiofibroma", "teach"): (
        "Why should an adolescent boy with recurrent epistaxis and a hypervascular nasopharyngeal mass be characterized radiographically before office biopsy?",
        "The classic clinical and imaging pattern can establish a presumptive diagnosis, while office instrumentation can cause severe hemorrhage. Contrast CT and MRI define nasal, pterygopalatine, infratemporal, orbital, skull-base, and intracranial extent and vascular relationships before angiography, embolization, or resection planning.",
    ),
    ("Epistaxis", "teach"): (
        "How would you teach a junior to triage epistaxis by patient stability and likely bleeding source rather than by the amount of blood visible at one moment?",
        "Begin with airway and hemodynamics, anticoagulant or bleeding risk, and resuscitation needs; then clear clot, use vasoconstriction and directed examination to distinguish an accessible anterior source from persistent posterior or unidentified bleeding. Escalate recurrent or significant bleeding to packing, endoscopic arterial control, or embolization according to stability and source.",
    ),
}

RECOGNITION_PROMPTS = {
    "Septal Deviation": "A patient has persistent unilateral nasal obstruction despite decongestion. Examination shows a fixed septal spur narrowing the symptomatic side, without a mass or dynamic lateral-wall collapse. What is the most likely diagnosis?",
    "Septal Hematoma": "After nasal trauma, a child develops progressive bilateral obstruction. Examination shows soft, boggy, fluctuant swelling on both sides of the septum that does not shrink with decongestion. What is the most likely diagnosis?",
}


def apply_daily_curriculum_quality_v371(items):
    stats = {"daily_pairs": 0, "recognition_prompts": 0}
    for item in items:
        key = (item.get("topic"), item.get("stage"))
        override = DAILY_OVERRIDES.get(key)
        if override:
            prompt, answer = override
            item["daily_prompt"] = prompt
            item["prompt"] = prompt
            item["answer"] = answer
            stats["daily_pairs"] += 1
        if item.get("stage") == "recognize" and item.get("topic") in RECOGNITION_PROMPTS:
            prompt = RECOGNITION_PROMPTS[item["topic"]]
            item["daily_prompt"] = prompt
            item["prompt"] = prompt
            stats["recognition_prompts"] += 1
    return stats


def install_daily_curriculum_quality_v371(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v371():
        items = original_get_items()
        apply_daily_curriculum_quality_v371(items)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v371
    app_module._adaptive_question = lambda item: item.get("daily_prompt") or item.get("prompt") or ""
    sample = get_adaptive_items_v371()
    return {"item_stats": apply_daily_curriculum_quality_v371(sample)}
