"""Distractor-specific why-wrong repairs for Sleep Surgery."""

WHY_WRONG_FIXES = {
    "v141_slp_01": [
        "Central sleep apnea is characterized by absent respiratory effort during events; this PSG shows mostly obstructive events with normal CO2, not the effort-absent pattern of central apnea.",
        "Sleep-related hypoventilation is defined by sustained CO2 elevation; this study explicitly shows normal CO2, ruling out a hypoventilation pattern.",
        "An overall AHI of 18/hour with marked positional variation represents clinically significant sleep apnea, not a normal study.",
        "Correct.",
    ],
    "v141_slp_02": [
        "Correct.",
        "Turbinate reduction addresses nasal airflow, a much less impactful site for severe multilevel retropalatal/retrolingual collapse; it would not be expected to meaningfully treat this patient's severe OSA.",
        "Performing tonsillectomy regardless of anatomy ignores whether tonsillar tissue is actually a significant contributor to this patient's obstruction, which is described as multilevel with retrognathia, not simply tonsil-driven.",
        "This patient has severe, PAP-intolerant OSA with an anatomic phenotype well suited to a skeletal surgical option; declining any surgery would deny an effective treatment for disabling disease.",
    ],
    "v141_slp_03": [
        "Correct.",
        "Positional therapy is most effective in patients with a true positional phenotype and low nonsupine AHI; it is not a universal cure for all severe OSA, especially disease that persists in the lateral position.",
        "Positional therapy is a reasonable, non-invasive option specifically for appropriately selected positional OSA patients; stating it is contraindicated in every patient overstates its risks.",
        "Ongoing reassessment is needed because adherence can wane and weight/disease can progress over time; no follow-up risks missing a return of unaddressed disease.",
    ],
    "v141_slp_04": [
        "Correct.",
        "BPPV is a vestibular positional vertigo disorder entirely unrelated to breathing, CO2 levels, or sleep-disordered breathing.",
        "Isolated positional OSA is characterized by discrete obstructive events that vary with body position, not the sustained CO2 elevation and daytime hypercapnia described here.",
        "Narcolepsy is a central hypersomnolence disorder related to abnormal REM regulation, unrelated to hypercapnia or breathing mechanics during sleep.",
    ],
    "v141_slp_05": [
        "Maximizing amplitude in a patient already experiencing painful stimulation would worsen discomfort and could further reduce adherence rather than solving a problem more likely related to programming parameters than insufficient intensity.",
        "Correct.",
        "Explantation is a drastic, irreversible step that skips the standard troubleshooting process (reprogramming, electrode configuration adjustment) that often resolves early comfort issues.",
        "Early device titration and comfort issues are common and typically improve with continued follow-up and adjustment; stopping follow-up would abandon the patient during exactly the period when refinement is most needed.",
    ],
    "v141_slp_06": [
        "Central apneas are not caused by insufficient pressure treating upper-airway obstruction; increasing CPAP pressure further would not resolve central events and could cause discomfort without addressing the actual mechanism.",
        "Correct.",
        "Palatal surgery treats anatomic pharyngeal obstruction; it has no mechanism to address central apneas, which arise from a ventilatory control problem, not airway collapse.",
        "Persistent central events, even after obstructive control, represent a real physiologic finding that can affect health and treatment efficacy; ignoring them risks undertreating a distinct breathing pattern.",
    ],
    "v143_slp_01": [
        "This PSG explicitly shows absent respiratory effort, the hallmark of central, not obstructive, events; performing UPPP would not address a central/hypoventilation mechanism.",
        "Tonsillectomy addresses obstructive lymphoid tissue; it has no mechanism to correct a central apnea/hypoventilation pattern with absent respiratory effort and sustained hypercapnia.",
        "Sustained hypercapnia is a critical finding indicating a ventilatory (gas-exchange) problem rather than simple obstruction; ignoring this data would miss the actual underlying mechanism.",
        "Correct.",
    ],
    "v143_slp_02": [
        "Correct.",
        "Explanting without first investigating correctable causes (programming, electrode position, residual collapse pattern) abandons a potentially salvageable therapy before a structured evaluation has been performed.",
        "Increasing amplitude despite discomfort risks worsening tolerance and adherence without necessarily improving airway opening, since nonresponse may stem from causes other than insufficient stimulation intensity.",
        "Weight and anatomy can and do change over time and may explain evolving therapy response; assuming they cannot change would miss a potentially correctable contributor to nonresponse.",
    ],
    "v143_slp_03": [
        "The palatine tonsils have presumably already been addressed in the prior adenotonsillectomy, and DISE now shows a different site driving obstruction; repeating an already-completed procedure would not address the actual demonstrated obstruction site.",
        "Nasal fracture reduction addresses nasal bone trauma, an entirely unrelated structure and problem with no connection to lingual tonsil hypertrophy or tongue-base obstruction.",
        "Correct.",
        "DISE specifically identifies the site of obstruction; ignoring this direct anatomic evidence and choosing surgery randomly abandons a rational, evidence-based approach.",
    ],
    "v143_slp_04": [
        "Pediatric PSG interpretation uses much lower AHI thresholds for abnormality than adults; an AHI under 15 is not automatically normal in a child and can still represent clinically significant obstructive sleep apnea.",
        "Central events in children have many possible causes and are not automatically diagnostic of epilepsy, which has entirely different diagnostic criteria and testing.",
        "Oxygen desaturation data provide important information about the physiologic significance of respiratory events and are a standard, relevant part of PSG interpretation in children.",
        "Correct.",
    ],
    "v143_slp_05": [
        "Correct.",
        "Sleep surgery outcomes depend on matching the procedure to the specific anatomic collapse pattern; applying the same operation to every patient regardless of individual DISE findings ignores this phenotype-driven principle.",
        "BMI and collapse pattern are established factors that influence surgical candidacy and expected outcomes; ignoring them would risk offering surgery to patients unlikely to benefit.",
        "Hypoglossal nerve stimulation is specifically not recommended for complete concentric palatal collapse, as it does not address that particular collapse pattern.",
    ],
    "v146_slp_01": [
        "There is no mention of snoring, witnessed apneas, or objective testing confirming OSA; refreshed, normal-quality sleep when allowed to follow their natural late schedule is inconsistent with untreated severe sleep apnea.",
        "Narcolepsy is characterized by excessive daytime sleepiness and sleep attacks regardless of when the patient sleeps; this teenager sleeps and feels normal when aligned with their preferred schedule, which does not fit narcolepsy.",
        "Restless legs syndrome involves an urge to move the legs, particularly at rest, and has no relationship to the timing of sleep onset described in this circadian pattern.",
        "Correct.",
    ],
    "v146_slp_02": [
        "Persistent OSA after adenotonsillectomy in a child with Down syndrome is often driven by multilevel obstruction beyond the tonsils/adenoids; automatically repeating the same procedure does not address these other contributing sites.",
        "Persistent severe OSA carries real health risks and requires further evaluation and management; ignoring it would leave a significant, potentially treatable condition unaddressed.",
        "A single procedure applied uniformly to every child does not account for the multilevel, patient-specific obstruction pattern common in Down syndrome, which typically requires individualized treatment.",
        "Correct.",
    ],
    "v146_slp_03": [
        "OSA does not typically cause cataplexy, sleep paralysis, or hypnagogic hallucinations; these are specific features pointing to a central hypersomnolence disorder, not obstructive sleep apnea alone.",
        "Correct.",
        "Delayed sleep-wake phase disorder involves a shifted sleep timing with normal sleep quality when aligned to the patient's preferred schedule; it does not cause cataplexy, sleep paralysis, or hallucinations.",
        "BPPV is a vestibular positional vertigo disorder entirely unrelated to sleep attacks, cataplexy, or hypnagogic phenomena.",
    ],
    "v146_slp_04": [
        "Palatal surgery outcomes depend on the specific anatomic collapse pattern demonstrated for each individual patient; applying the identical operation to every patient ignores this phenotype-driven principle.",
        "Correct.",
        "DISE directly identifies the site and pattern of airway collapse and is specifically what should guide procedure selection; stating it never matters contradicts the fundamental rationale for phenotype-directed surgery.",
        "Palatal surgery addresses anatomic pharyngeal obstruction; it has no mechanism to treat central sleep apnea, which arises from a ventilatory control problem, not airway collapse.",
    ],
    "v146_slp_05": [
        "Middle-ear pressure relates to Eustachian tube function and has no established relationship to restless legs syndrome symptoms.",
        "Thyroid nodule size is an unrelated structural finding with no established connection to the sensorimotor mechanism underlying restless legs syndrome.",
        "Correct.",
        "Nasal septal angle relates to nasal airflow and has no established relationship to the urge-to-move-legs symptom pattern characteristic of RLS.",
    ],
    "v146_slp_06": [
        "Septoplasty addresses nasal septal deviation, an entirely different anatomic site from the tongue-base/lingual-tonsil obstruction demonstrated on DISE; it would not be expected to resolve dominant tongue-base collapse.",
        "DISE directly demonstrates the site and pattern of this patient's obstruction; ignoring this evidence abandons a rational, targeted approach to selecting the appropriate procedure.",
        "Routine epiglottis removal in every case is an overly aggressive, non-individualized approach that does not specifically match this patient's demonstrated obstruction pattern.",
        "Correct.",
    ],
}


def apply_why_wrong_fix_sleep_v1(data_module):
    """Overwrite why_wrong for the fixed ids. Returns count actually updated."""
    byid = {q.get("id"): q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")}
    updated = 0
    missing = []
    for qid, new_why_wrong in WHY_WRONG_FIXES.items():
        q = byid.get(qid)
        if q is None:
            missing.append(qid)
            continue
        if len(new_why_wrong) != len(q.get("choices") or []):
            raise ValueError(
                f"{qid}: fix has {len(new_why_wrong)} entries but question has "
                f"{len(q.get('choices') or [])} choices"
            )
        q["why_wrong"] = new_why_wrong
        updated += 1
    if missing:
        print(f"why_wrong_fix_sleep_v1: {len(missing)} ids not found: {missing}")
    return updated
