"""v26.3 — Sleep Surgery deliberate ladder pass 1.

Adds five exact canonical Sleep Surgery topics with complete foundation ->
application -> senior-decision ladders. Reuses the repository's existing HNS/DISE
OR-management framework and adds the missing PSG interpretation, PAP troubleshooting,
activation/programming, candidacy, escalation, and nonresponse decision layers.
"""
DOMAIN = "Sleep Surgery"


def _q(qid, topic, stage, stem, choices, answer, explanation, reasons, pearl,
       curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": reasons,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True, "_coverage_reviewed_v211": True,
    }


VIGNETTES_V263 = [
    _q("v263_sleep_adultpsg_fnd", "Adult PSG Interpretation", "foundation",
       "An adult PSG shows recurrent airflow cessation with continued thoracoabdominal effort, followed by arousal and oxygen desaturation. What type of respiratory event is this?",
       ["Obstructive apnea", "Central apnea", "Sleep-related hypoventilation", "Periodic limb movement"], 0,
       "Obstructive apnea is defined by absent or markedly reduced airflow while respiratory effort persists. Central apnea lacks respiratory effort during the event.",
       ["Correct. Persistent effort against absent airflow identifies an obstructive event.", "Central apnea requires absent inspiratory effort during the airflow pause.", "Hypoventilation is sustained inadequate ventilation, generally assessed with CO2 rather than isolated discrete obstructive pauses.", "Limb movements may fragment sleep but do not create this airflow-effort pattern."],
       "On PSG, airflow plus respiratory effort separates obstructive from central events.",
       "How would mixed apnea appear across the beginning and end of the same event?"),
    _q("v263_sleep_adultpsg_app", "Adult PSG Interpretation", "application",
       "A patient has AHI 18/h but nearly all events occur supine; nonsupine AHI is 3/h. Oxygenation is otherwise preserved. What interpretation is most useful for management planning?",
       ["This is position-dependent OSA, so positional susceptibility should be incorporated into treatment selection and counseling", "The overall AHI proves every sleep position is equally abnormal", "The study is diagnostic of central sleep apnea", "The PSG cannot guide non-PAP treatment selection"], 0,
       "The global AHI should be interpreted with event phenotype, sleep stage, body position, oxygen burden, symptoms, and study quality. Marked supine dependence can materially change treatment options.",
       ["Correct. The positional distribution is clinically meaningful rather than an incidental table entry.", "A global average can hide major positional heterogeneity.", "Central sleep apnea depends on central-event burden, not supine predominance of obstructive events.", "PSG phenotype is important when matching behavioral, device, and surgical strategies."],
       "Do not stop at the AHI: ask where, when, and what kind of events produced it.",
       "How would severe REM-predominant obstruction alter interpretation if little REM sleep was captured?", "sleep_interpretation"),
    _q("v263_sleep_adultpsg_snr", "Adult PSG Interpretation", "senior_decision",
       "A referral for upper-airway surgery arrives with an AHI of 32/h, but 20/h are central apneas and the tracing shows periodic breathing. What is the best senior decision?",
       ["Do not treat the AHI as purely anatomic OSA; clarify the central-event mechanism and optimize sleep/medical evaluation before selecting obstructive-airway surgery", "Proceed directly to multilevel airway surgery because the total AHI exceeds 30/h", "Ignore respiratory effort channels and use oxygen nadir alone", "Perform DISE and assume any collapse seen explains the central events"], 0,
       "A high total AHI can be misleading when central events comprise a substantial fraction. Upper-airway surgery does not correct absent central respiratory drive, so event composition must be resolved first.",
       ["Correct. Surgery should target a demonstrated obstructive mechanism, not a summary index detached from event type.", "The numeric AHI alone does not establish an obstructive surgical target.", "Oxygen nadir is important risk information but cannot distinguish central from obstructive pathophysiology.", "DISE demonstrates dynamic upper-airway collapse under sedation; it does not explain central respiratory-drive failure."],
       "Before operating on OSA, confirm that the disease you are treating is actually obstructive.",
       "Which cardiac, neurologic, medication, altitude, and PAP-related causes should be considered when central events dominate?", "senior_management"),

    _q("v263_sleep_dise_fnd", "DISE", "foundation",
       "What is the primary purpose of drug-induced sleep endoscopy in an adult being considered for sleep surgery?",
       ["Characterize the level, pattern, and configuration of dynamic upper-airway collapse to help match therapy to phenotype", "Measure the patient's AHI directly", "Replace the diagnostic sleep study", "Determine daytime pulmonary function"], 0,
       "DISE is a dynamic anatomic phenotyping tool. It complements, rather than replaces, objective sleep testing and awake examination.",
       ["Correct. DISE helps localize and characterize collapse during a sleep-like state.", "AHI is derived from sleep testing, not endoscopic observation alone.", "DISE does not establish the full physiologic diagnosis or severity of sleep-disordered breathing.", "Pulmonary function testing evaluates a different physiologic question."],
       "DISE answers 'where and how does the airway collapse?'—not 'how severe is the OSA?'.",
       "Why can awake Mueller maneuver findings differ from DISE findings?"),
    _q("v263_sleep_dise_app", "DISE", "application",
       "During DISE, an HNS candidate demonstrates complete concentric collapse at the velum plus substantial lateral pharyngeal-wall collapse. What is the best interpretation?",
       ["The collapse phenotype may be poorly matched to standard unilateral hypoglossal stimulation and should trigger candidacy/adjunctive-strategy reassessment rather than automatic implantation", "Any tongue-base motion guarantees HNS success", "The velum pattern is irrelevant if the AHI is high", "Proceed because DISE findings should never change treatment choice"], 0,
       "HNS candidacy depends on a compatible collapse phenotype in addition to physiologic and patient factors. DISE also reveals multilevel patterns that may explain limited response to a single targeted therapy.",
       ["Correct. A mismatched palatal/lateral-wall phenotype is a treatment-selection issue, not a technicality.", "Response depends on whole-airway mechanics, not simply visible tongue movement.", "Collapse configuration can directly affect expected treatment response.", "The purpose of DISE is precisely to refine anatomic treatment selection."],
       "A procedure can be technically feasible yet biologically mismatched to the collapse pattern.",
       "How can jaw thrust or mouth closure maneuvers during DISE provide hypothesis-generating information without becoming a perfect outcome predictor?", "OR_prep"),
    _q("v263_sleep_dise_snr", "DISE", "senior_decision",
       "During DISE the patient becomes deeply sedated, develops prolonged apnea and severe desaturation, and the collapse pattern appears dramatically worse than earlier in the examination. What is the best next step?",
       ["Prioritize oxygenation/airway rescue and recognize that excessive sedation can distort the phenotype; do not keep scoring an unsafe, nonrepresentative state", "Continue the examination until every airway subsite has been scored regardless of oxygenation", "Increase sedative dose to make collapse even more obvious", "Interpret the deepest-sedation pattern as automatically most physiologic"], 0,
       "DISE requires a safe, reproducible sleep-like sedation plane. Excessive sedation can exaggerate airway collapsibility and undermine both safety and interpretability.",
       ["Correct. Patient safety and validity both require abandoning an unsafe or clearly over-sedated state.", "A complete score is not worth preventable hypoxemic injury.", "More sedation worsens both physiologic distortion and airway risk.", "The most dramatic collapse is not necessarily the most representative natural-sleep phenotype."],
       "DISE is an anesthetic-airway procedure as well as a diagnostic examination; rescue readiness is part of the test.",
       "What preprocedure features should change sedation planning or the threshold for aborting DISE?", "senior_management"),

    _q("v263_sleep_hns_fnd", "Hypoglossal Nerve Stimulation", "foundation",
       "What is the therapeutic mechanism of standard unilateral hypoglossal nerve stimulation for OSA?",
       ["Synchronize stimulation of selected hypoglossal motor branches with respiration to improve tongue position and upper-airway patency", "Paralyze the tongue during inspiration", "Stimulate the recurrent laryngeal nerve to abduct both vocal folds", "Create continuous positive airway pressure through an implanted pump"], 0,
       "HNS recruits tongue protrusor/stabilizing musculature in a respiratory-timed pattern to enlarge or stiffen the pharyngeal airway in selected patients.",
       ["Correct. Effective stimulation aims for useful tongue protrusion/stiffening without excessive discomfort or retrusion.", "Tongue paralysis would worsen rather than treat pharyngeal obstruction.", "The recurrent laryngeal nerve is not the therapeutic target for OSA HNS.", "HNS is neuromodulation, not an implanted PAP device."],
       "HNS works by neuromuscular airway recruitment, not by mechanically splinting the airway with pressure.",
       "Why does selective branch capture matter more than simply placing a cuff anywhere on CN XII?"),
    _q("v263_sleep_hns_app", "Hypoglossal Nerve Stimulation", "application",
       "Before HNS implantation, which combination most directly determines whether the therapy is a rational match?",
       ["Objective OSA phenotype including central-event burden, PAP intolerance/failure, current candidacy criteria, DISE collapse pattern, anatomy and patient-specific surgical/device factors", "AHI alone", "BMI alone", "Patient preference without objective sleep testing"], 0,
       "HNS selection is multidimensional. The repository's existing OR framework correctly avoids treating one historical payer cutoff as universal and instead requires current criteria plus physiologic and anatomic fit.",
       ["Correct. Candidacy combines disease type/severity, prior therapy, dynamic anatomy, and practical device considerations.", "AHI is necessary context but cannot establish collapse compatibility or central-event proportion by itself.", "Body habitus matters but is not a stand-alone candidacy test.", "Preference is important only after the diagnosis and expected benefit/risk are established."],
       "HNS candidacy is a phenotype decision, not a single-number threshold.",
       "How should prior neck surgery, baseline tongue weakness, implanted hardware, or major weight change alter preoperative planning?", "OR_prep"),
    _q("v263_sleep_hns_snr", "Hypoglossal Nerve Stimulation", "senior_decision",
       "Several hours after HNS implantation, a patient develops increasing neck swelling, dysphagia, muffled speech, and new oxygen requirement. What is the best senior response?",
       ["Urgently evaluate for expanding hematoma/airway compromise and device-related surgical complications; secure the airway and obtain source control as clinically indicated", "Assume stimulation intolerance even though the device has not been activated", "Send the patient home because tongue discomfort is expected", "Increase stimulation amplitude"], 0,
       "Early postoperative neck swelling with airway or swallowing change is a surgical emergency until proven otherwise. HNS activation occurs later; acute deterioration should not be mislabeled a programming problem.",
       ["Correct. Airway protection and hematoma evaluation take priority over routine postoperative pathways.", "Programming cannot explain pre-activation progressive neck swelling.", "Routine discomfort does not justify ignoring evolving airway symptoms.", "Increasing amplitude is irrelevant before activation and dangerous as a distraction from surgical rescue."],
       "Separate implantation complications from later programming problems: timing tells you which problem set matters.",
       "How would new pleuritic chest pain or hypoxemia shift concern toward sensing-lead pleural injury or pneumothorax?", "senior_management"),

    _q("v263_sleep_pap_fnd", "PAP Troubleshooting", "foundation",
       "A patient with otherwise well-controlled OSA stops CPAP because of nasal dryness and congestion but reports clear symptomatic benefit when able to wear it. What is the best first principle?",
       ["Identify and treat the specific tolerance barrier—interface, humidification, nasal disease, pressure comfort, or leak—before labeling PAP a treatment failure", "Declare PAP permanently ineffective", "Proceed directly to multilevel surgery", "Increase pressure without reviewing the download"], 0,
       "PAP intolerance is often modifiable. Troubleshooting begins by separating efficacy from adherence and identifying the reason the patient cannot use an otherwise effective therapy.",
       ["Correct. Nasal care, humidification and interface optimization may restore effective use.", "Inability to tolerate a correctable side effect is not the same as physiologic nonresponse.", "Surgery is not the first answer to every fixable PAP barrier.", "Blind pressure escalation can worsen leak, discomfort, aerophagia, or emergent central events."],
       "Ask whether PAP fails to work or the patient cannot tolerate how it is being delivered.",
       "Which nasal examination findings are most worth correcting before concluding that PAP is unusable?"),
    _q("v263_sleep_pap_app", "PAP Troubleshooting", "application",
       "A PAP download shows high residual AHI, large unintentional leak, and events clustered during periods of leak. What is the best next step?",
       ["Correct mask/interface leak and reassess reliable residual-event data before escalating pressure or abandoning PAP", "Assume every residual event represents untreated fixed airway obstruction", "Immediately refer for MMA without checking interface fit", "Ignore the leak because device event detection is never affected by it"], 0,
       "Large leak can reduce delivered pressure, fragment sleep, and degrade automated event detection. The data must be made trustworthy before major therapeutic conclusions are drawn.",
       ["Correct. Fix the measurement/delivery problem first, then reassess residual physiology.", "Residual indices during major leak can be misleading.", "Major surgery should not be selected from unreliable PAP-download data alone.", "Leak is both a therapeutic and signal-quality problem."],
       "Bad PAP data can create bad surgery decisions; make the download interpretable before acting on it.",
       "How would persistent residual central events after leak correction change the next diagnostic step?", "sleep_interpretation"),
    _q("v263_sleep_pap_snr", "PAP Troubleshooting", "senior_decision",
       "A patient with obstructive OSA starts PAP and now has frequent central apneas that were minimal on the diagnostic study. He is asymptomatic and the pattern is new during titration. What is the best senior approach?",
       ["Recognize possible treatment-emergent central sleep apnea, review pressure/leak/medications and clinical context, and arrange appropriate sleep follow-up rather than reflexively sending the patient for upper-airway surgery", "Interpret the new central events as proof of tongue-base obstruction", "Increase pressure indefinitely until all events disappear", "Stop evaluating because any AHI improvement is adequate"], 0,
       "Treatment-emergent central events require physiologic reassessment. Some patterns resolve, while persistent clinically important central apnea may require a different management pathway than anatomic OSA.",
       ["Correct. The event type changed, so the treatment logic must change with it.", "Central apnea is not explained by a fixed tongue-base lesion.", "Excessive pressure can aggravate instability in susceptible patients.", "Residual event composition matters even if the total AHI is lower."],
       "When PAP changes obstructive events into central events, do not keep treating the old phenotype by habit.",
       "Which features would make you investigate heart failure, opioids, neurologic disease, altitude exposure, or other causes of central instability?", "senior_management"),

    _q("v263_sleep_hnsprog_fnd", "HNS Activation / Programming", "foundation",
       "Why is HNS activation generally separated from the day of implantation?",
       ["The surgical sites need time to heal before systematic stimulation testing and programming begin", "The hypoglossal nerve cannot conduct impulses for months after any surgery", "The device is intended to remain permanently off", "Activation is unnecessary if implantation was technically successful"], 0,
       "Implant healing and device programming are distinct phases. Activation establishes a comfortable functional stimulation window after early surgical recovery.",
       ["Correct. Early recovery is for wound/device integrity; programming follows on a planned pathway.", "Normal nerve conduction does not require months of recovery simply because a cuff was implanted.", "The therapeutic device must be activated to treat OSA.", "A technically successful implant still requires individualized programming and outcome reassessment."],
       "Implantation puts the system in place; programming turns that hardware into therapy.",
       "What should be examined before first activation if the patient reports new tongue weakness or dysphagia?"),
    _q("v263_sleep_hnsprog_app", "HNS Activation / Programming", "application",
       "At activation, low amplitudes produce comfortable midline tongue protrusion, but higher amplitudes cause painful tongue pulling and sleep disruption. What is the best programming principle?",
       ["Use the lowest effective, comfortable stimulation range and optimize electrode configuration/timing rather than assuming more amplitude always produces better therapy", "Set the device permanently to the highest tolerable amplitude", "Ignore tongue motion as long as the generator turns on", "Schedule revision surgery before trying programming adjustments"], 0,
       "HNS programming balances airway effect, comfort and adherence. Excess stimulation can cause discomfort, awakenings, maladaptive tongue motion, and poorer use despite technically intact hardware.",
       ["Correct. Programming seeks effective recruitment, not maximal electrical output.", "Highest amplitude can worsen adherence and does not guarantee favorable airway mechanics.", "Tongue motion provides important information about branch capture and recruitment pattern.", "Noninvasive programming optimization should precede revision when the system is otherwise intact."],
       "For HNS, stronger stimulation is not automatically better stimulation.",
       "How can electrode configuration change tongue recruitment even at similar amplitude?", "device_management"),
    _q("v263_sleep_hnsprog_snr", "HNS Activation / Programming", "senior_decision",
       "Months after HNS activation, adherence is excellent but the residual AHI remains high. Device interrogation is normal and the tongue visibly protrudes. What is the best senior next step?",
       ["Systematically reassess programming, sleep-state/position response, weight change and residual collapse phenotype—often with targeted titration or repeat anatomic evaluation—before declaring the implant a failure", "Explanted the device immediately because visible tongue motion proves programming cannot help", "Increase amplitude without limit", "Assume persistent OSA is unrelated to anatomy or sleep position"], 0,
       "Nonresponse can reflect programming, unfavorable recruitment, residual palatal/lateral-wall collapse, positional disease, weight change, or another sleep phenotype. Normal hardware function does not guarantee optimal physiologic effect.",
       ["Correct. Troubleshooting should localize the failure mechanism before revision or abandonment.", "Visible protrusion is necessary information but does not prove whole-airway opening or optimal timing.", "Unlimited amplitude can reduce comfort and worsen recruitment without correcting the actual collapse pattern.", "Residual OSA often remains phenotype-dependent and should be re-characterized."],
       "HNS nonresponse is a diagnostic problem: decide whether the issue is hardware, programming, recruitment, residual anatomy, or sleep physiology.",
       "When would imaging, repeat DISE, sensing-lead evaluation, or surgical revision become appropriate?", "senior_management"),
]


def apply_learning_ladders_v263(challenges, concept_id_fn):
    """Append only missing v26.3 cases and attach exact canonical concept IDs."""
    existing = {str(q.get("id")) for q in challenges}
    added = 0
    for source in VIGNETTES_V263:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return added
