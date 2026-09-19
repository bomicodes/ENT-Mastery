"""v38.0 - Muscle Tension Dysphonia: the card was not hedge-heavy so much as
simply underdeveloped -- one or two sentences per field where comparable
Laryngology cards run full paragraphs. This is a different failure mode from
the "framework named, no numbers" pattern fixed in v37.2-v37.9, but it's the
same underlying problem the user first raised: a resident landing on this
card cannot actually do anything with it clinically.

Added: the primary-vs-secondary classification, the actual laryngoscopic
exam findings that document supraglottic squeeze, and named voice-therapy
techniques, none of which existed anywhere in the card before.

Reviewed and confirmed NOT gaps in this same pass (left untouched):
Intracranial Complications of Sinusitis, First-Bite Syndrome, Ranula,
External Auditory Canal Cholesteatoma, CSF Rhinorrhea, Odontogenic
Sinusitis, Age-Related Hearing Loss/Presbycusis, Completion Thyroidectomy,
Benign Vocal Fold Lesions -- all nine were read in full and are already
well-operationalized. The broadened scan's remaining ~90 flagged fields are
increasingly false positives (qualitative recognize/localize language that
is legitimately qualitative), so this closes out this round of review.

Idempotent: checks a marker string before appending.
"""

MTD_TOPIC = "Muscle Tension Dysphonia"

MTD_RECOGNIZE = (
    "Excess supraglottic/phonatory tension may be primary (no identifiable organic driver -- "
    "often related to vocal misuse, stress, or compensatory habituation after a resolved "
    "illness) or secondary (compensation for an underlying glottic lesion, paresis, reflux, or "
    "another organic process that made phonation effortful). The distinction matters because "
    "primary MTD responds to voice therapy alone, while secondary MTD will recur or "
    "plateau until the underlying driver is treated."
)

MTD_WORKUP = (
    "Stroboscopy and expert voice evaluation; actively search for the reason the patient is "
    "compensating. On exam, MTD classically shows anteroposterior supraglottic compression "
    "(false vocal folds and arytenoids squeezing toward the epiglottis), true-fold "
    "hyperadduction with a strained voice quality, elevated laryngeal position on palpation, "
    "and reduced thyrohyoid space. Palpate the strap muscles and thyrohyoid space for "
    "tenderness/elevation as part of the exam, not just the endoscopic view. Document whether "
    "the glottis is otherwise structurally normal once the squeeze is accounted for -- if a "
    "true lesion, paresis, or fixation is visible despite the compensatory pattern, this is "
    "secondary MTD and the primary problem drives management."
)

MTD_MANAGE = (
    "Voice therapy is central; treat an underlying lesion/paresis when present. Effective "
    "voice therapy techniques include manual circumlaryngeal massage/laryngeal reposturing to "
    "reduce elevated laryngeal position, resonant voice therapy (e.g. Lessac-Madsen Resonant "
    "Voice Therapy) to shift phonation toward an easier, forward-focused production, and "
    "vocal function exercises to rebalance laryngeal muscle effort. Address contributing "
    "reflux, allergy, or vocal-hygiene factors in parallel rather than treating tension in "
    "isolation."
)

MTD_TEACH = (
    "Supraglottic squeeze is a behavior/finding, not automatically the primary diagnosis. "
    "Boards/chief framework: MTD = PRIMARY (behavioral/compensatory, therapy-responsive) vs "
    "SECONDARY (compensating for a real organic lesion). Look past the squeeze to the true "
    "glottis before committing to a diagnosis of primary MTD, and treat the underlying driver "
    "in secondary disease or voice therapy alone will underperform."
)


def apply_mtd_depth_v380(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            if module.get("topic") != MTD_TOPIC:
                continue

            recognize = module.get("recognize", "") or ""
            if "primary (no identifiable organic driver" not in recognize:
                module["recognize"] = MTD_RECOGNIZE

            workup = module.get("workup", "") or ""
            if "anteroposterior supraglottic compression" not in workup:
                module["workup"] = MTD_WORKUP

            manage = module.get("manage", "") or ""
            if "circumlaryngeal massage" not in manage:
                module["manage"] = MTD_MANAGE

            teach = module.get("teach", "") or ""
            if "PRIMARY (behavioral/compensatory" not in teach:
                module["teach"] = MTD_TEACH

            tags = module.setdefault("tags", [])
            for tag in ("primary vs secondary MTD", "anteroposterior supraglottic compression",
                        "circumlaryngeal massage", "resonant voice therapy"):
                if tag not in tags:
                    tags.append(tag)

            patched.append(module.get("topic"))

    if not patched:
        raise RuntimeError("v38.0: could not find the canonical Muscle Tension Dysphonia topic")

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6

    return {"patched": patched, "count": len(patched)}
