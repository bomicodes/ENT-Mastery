"""v26.6 — Sleep Surgery deliberate ladder pass 3.

Adds five exact canonical physiology-heavy topics with complete foundation ->
application -> senior-decision ladders. Emphasizes PSG interpretation, central
versus obstructive physiology, hypoventilation recognition, and postoperative
phenotype-directed management before additional upper-airway surgery.
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


VIGNETTES_V266 = [
    _q("v266_sleep_peds_psg_fnd", "Pediatric PSG Interpretation", "foundation",
       "When interpreting a pediatric polysomnogram, which principle is most important before labeling the study normal from an AHI that would look low in an adult?",
       ["Use pediatric scoring and severity context because children can have clinically meaningful obstructive disease at event rates that would be trivial in adults", "Apply adult AHI thresholds to every child", "Ignore arousals and gas exchange if the total AHI is low", "Assume snoring without apneas excludes pediatric OSA"], 0,
       "Pediatric sleep-disordered breathing is not interpreted with adult thresholds alone. Event burden, obstructive pattern, arousals, oxygenation, carbon dioxide, age, comorbidity and symptoms all matter.",
       ["Correct. Pediatric interpretation requires pediatric rules and clinical context.", "Adult thresholds can undercall clinically important pediatric disease.", "Gas exchange and arousal burden can identify important disease not captured by a single summary number.", "Primary snoring and OSA exist on a spectrum; absence of obvious apneas does not by itself establish normal physiology."],
       "In children, read the channels and phenotype first; do not let an adult mental model of AHI erase pediatric disease.",
       "How would trisomy 21, neuromuscular disease or craniofacial syndromes lower your threshold for concern even with a modest obstructive index?", "sleep_interpretation"),
    _q("v266_sleep_peds_psg_app", "Pediatric PSG Interpretation", "application",
       "A 6-year-old has an obstructive AHI of 2.8/hour, frequent snoring and arousals, and symptoms of sleep-disordered breathing. What is the best interpretation?",
       ["This can represent clinically meaningful pediatric OSA; integrate symptoms, exam, gas exchange and comorbidity rather than dismissing the study because the AHI is below adult treatment thresholds", "The study is normal because the AHI is below 5/hour", "The child has central sleep apnea because the AHI is low", "Only oxygen nadir determines whether pediatric OSA exists"], 0,
       "A pediatric obstructive index in this range may be abnormal and clinically relevant. Management depends on phenotype, symptoms, adenotonsillar/craniofacial anatomy, gas exchange and risk factors rather than an adult AHI cutoff.",
       ["Correct. The pediatric diagnosis and management decision are contextual, not an adult-threshold transplant.", "An adult cutoff of 5/hour should not be used to declare a symptomatic child normal.", "A low total AHI does not imply central physiology; event type comes from effort and airflow signals.", "Oxygen nadir is important but is only one component of pediatric PSG interpretation."],
       "A low-single-digit pediatric obstructive AHI may still matter; severity and treatment are not synonymous.",
       "What additional concern would sustained hypercapnia create if the obstructive event index remained only mildly elevated?", "sleep_interpretation"),
    _q("v266_sleep_peds_psg_snr", "Pediatric PSG Interpretation", "senior_decision",
       "After adenotonsillectomy, a syndromic child remains sleepy. Repeat PSG shows few obstructive events but sustained carbon-dioxide elevation and oxygen desaturation. What is the best senior response?",
       ["Do not reflexively schedule more upper-airway surgery; evaluate sleep-related hypoventilation and its pulmonary, neuromuscular, medication or ventilatory-control causes and coordinate appropriate ventilatory management", "Repeat adenotonsillectomy because symptoms persist", "Call the PSG normal because obstruction improved", "Treat only the oxygen saturation with supplemental oxygen without evaluating ventilation"], 0,
       "Residual symptoms after airway surgery can reflect a different physiology. Persistent hypercapnia points toward hypoventilation, for which additional anatomic surgery may be ineffective or harmful if the underlying ventilatory problem is missed.",
       ["Correct. The postoperative phenotype must be re-established before another operation.", "Repeat surgery without an obstructive target does not address sustained hypoventilation.", "Improved obstruction does not normalize abnormal ventilation.", "Oxygen can improve saturation while leaving carbon-dioxide retention untreated and can obscure the underlying ventilatory failure."],
       "After pediatric OSA surgery, a changed PSG phenotype should change the treatment plan.",
       "Which children warrant planned postoperative monitoring because residual obstruction or hypoventilation risk is high despite technically successful surgery?", "senior_decision"),

    _q("v266_sleep_central_events_fnd", "Central Events / Hypoventilation", "foundation",
       "What PSG feature most directly separates a central apnea from an obstructive apnea?",
       ["Central apnea lacks respiratory effort during absent airflow, whereas obstructive apnea retains respiratory effort against a blocked airway", "Central apnea always has louder snoring", "Obstructive apnea always causes a lower oxygen nadir", "Only event duration distinguishes the two"], 0,
       "Airflow alone cannot distinguish event mechanism. Respiratory-effort channels are essential: absent effort supports a central event, while persistent or paradoxical effort supports obstruction.",
       ["Correct. Effort is the key physiologic discriminator.", "Snoring suggests upper-airway vibration and is not a defining feature of central apnea.", "Desaturation severity overlaps and does not define event mechanism.", "Duration contributes to scoring criteria but does not by itself distinguish central from obstructive physiology."],
       "When reading PSG, ask what the chest and abdomen are doing while airflow disappears.",
       "How would mixed apnea appear across the event and why does that matter when interpreting a central-apnea index?", "sleep_interpretation"),
    _q("v266_sleep_central_events_app", "Central Events / Hypoventilation", "application",
       "A postoperative sleep study after upper-airway surgery shows a markedly improved obstructive index but persistent desaturation with long periods of elevated transcutaneous CO2 rather than discrete apneas. What is the best interpretation?",
       ["The dominant remaining problem may be sleep-related hypoventilation rather than recurrent focal upper-airway collapse", "The operation necessarily failed anatomically", "The patient has positional OSA by definition", "CO2 data should be ignored if the AHI improved"], 0,
       "Hypoventilation is sustained inadequate ventilation with hypercapnia, not simply a cluster of scored apneas. AHI can improve while clinically important gas-exchange failure persists.",
       ["Correct. Sustained CO2 elevation points to a ventilatory problem that needs its own differential and treatment.", "Anatomic failure should be demonstrated rather than inferred from nonobstructive gas-exchange abnormalities.", "Positional OSA requires a position-dependent obstructive phenotype.", "Carbon-dioxide data can be decisive when AHI does not explain the patient's gas-exchange burden."],
       "A normalizing AHI does not equal normal breathing if CO2 is persistently abnormal.",
       "What awake blood-gas, pulmonary-function, medication and neuromuscular findings would you review before choosing nocturnal ventilatory support?", "sleep_interpretation"),
    _q("v266_sleep_central_events_snr", "Central Events / Hypoventilation", "senior_decision",
       "A patient referred for additional sleep surgery has severe nocturnal hypoxemia, chronic opioid use, frequent central events and sustained hypercapnia with little evidence of upper-airway obstruction. What is the best senior decision?",
       ["Defer additional anatomic sleep surgery and redirect evaluation toward ventilatory-control and hypoventilation management, including medication review and sleep/pulmonary expertise", "Perform multilevel airway surgery because the oxygen nadir is severe", "Use DISE severity to decide whether central events are important", "Assume all sleep-disordered breathing improves with tissue removal"], 0,
       "Severe gas-exchange abnormality does not automatically imply surgically correctable obstruction. Central events and hypoventilation require mechanism-specific evaluation; anatomic surgery should have a demonstrated obstructive target.",
       ["Correct. The treatment mechanism must match the physiologic disorder.", "A low oxygen nadir can occur in nonobstructive ventilatory failure and does not establish a surgical target.", "DISE visualizes dynamic upper-airway collapse but does not diagnose central respiratory-drive failure.", "Tissue removal cannot correct absent respiratory drive or global hypoventilation."],
       "The most important sleep-surgery decision is sometimes recognizing that the problem is not surgical.",
       "How would obesity hypoventilation, COPD overlap or neuromuscular weakness alter the ventilatory strategy?", "senior_decision"),

    _q("v266_sleep_csa_fnd", "Central Sleep Apnea / Treatment-Emergent CSA", "foundation",
       "Which description best fits treatment-emergent central sleep apnea?",
       ["Obstructive events improve with PAP, but clinically important central events emerge or persist during therapy after the obstructive component is treated", "Any central apnea seen before PAP is started", "Snoring that continues despite nasal surgery", "Hypercapnia caused by a blocked tracheostomy"], 0,
       "Treatment-emergent CSA is recognized when therapy relieves obstruction but central instability becomes apparent during PAP. It is a ventilatory-control phenotype, not simply persistent snoring or any preexisting central event.",
       ["Correct. The central events appear or persist in the setting of treated obstruction.", "Preexisting central apnea can be primary or secondary CSA and is not by itself treatment-emergent.", "Snoring does not define central apnea.", "A blocked tracheostomy is a mechanical airway emergency, not treatment-emergent CSA."],
       "When PAP fixes the obstruction but the breathing pattern becomes central, stop treating the residual number as if it were still OSA.",
       "Why can treatment-emergent CSA improve over time in some patients, and what features would make you investigate another cause sooner?", "sleep_interpretation"),
    _q("v266_sleep_csa_app", "Central Sleep Apnea / Treatment-Emergent CSA", "application",
       "A patient with severe OSA starts PAP. Download and titration data show excellent control of obstruction and leak, but a new high central-apnea burden appears. What is the best next step?",
       ["Confirm the event phenotype and contributing causes such as excessive pressure, heart failure, opioids or altitude, then manage the central disorder rather than simply escalating obstructive pressure", "Increase pressure repeatedly until every central event disappears", "Refer directly for tongue-base surgery", "Ignore the central index because PAP is being used"], 0,
       "Once obstruction and leak are controlled, persistent central events should trigger confirmation and etiologic review. More pressure can worsen instability in some patients and surgery does not treat absent respiratory effort.",
       ["Correct. Verify the signal and mechanism, then tailor therapy to the central physiology and cause.", "Indiscriminate pressure escalation can fail or worsen treatment-emergent instability.", "Tongue-base surgery addresses anatomic obstruction, not central events with absent effort.", "A high residual central burden can be clinically meaningful and should not be ignored."],
       "Residual PAP AHI must be decomposed into obstructive versus central events before changing therapy.",
       "When would adaptive servo-ventilation require special caution because of the patient's cardiac phenotype?", "sleep_interpretation"),
    _q("v266_sleep_csa_snr", "Central Sleep Apnea / Treatment-Emergent CSA", "senior_decision",
       "An OSA patient is sent for HNS after 'PAP failure.' Review of the titration shows minimal residual obstruction but persistent central apneas. What is the best senior response?",
       ["Do not implant HNS for a predominantly central residual disorder; clarify the central-apnea cause and optimize appropriate sleep-medicine therapy", "Proceed because HNS treats any elevated AHI", "Use DISE to prove the central apneas are obstructive", "Implant HNS and increase amplitude until respiratory effort returns"], 0,
       "HNS recruits upper-airway dilator muscles and requires an obstructive target. Predominantly central residual events represent a mismatch between therapy and mechanism.",
       ["Correct. Device candidacy depends on the obstructive phenotype, not the total AHI alone.", "An elevated AHI can be driven by central events that HNS cannot correct.", "DISE assesses upper-airway collapse and cannot convert absent respiratory effort into obstruction.", "Stimulation can alter upper-airway tone but does not restore central respiratory drive."],
       "For HNS candidacy, always look past the total AHI to the central-event burden.",
       "How would mixed OSA and CSA change counseling if the obstructive component remains substantial but the central burden is not negligible?", "senior_decision"),

    _q("v266_sleep_hypovent_fnd", "Sleep-Related Hypoventilation", "foundation",
       "Which physiologic measurement is most important when PSG suggests sleep-related hypoventilation?",
       ["Carbon-dioxide monitoring or an appropriate surrogate, because hypoventilation is defined by inadequate ventilation with sustained hypercapnia rather than oxygen desaturation alone", "Snoring volume", "AHI alone", "Number of limb movements"], 0,
       "Sleep-related hypoventilation is a ventilation disorder. Sustained CO2 elevation is central to recognition; oxygen saturation can fall for many reasons and cannot by itself establish hypoventilation.",
       ["Correct. CO2 provides the direct physiologic clue that ventilation is inadequate.", "Snoring reflects airway vibration and does not measure ventilation.", "AHI can be low despite severe sustained hypoventilation.", "Limb movements are unrelated to defining hypoventilation."],
       "Hypoxemia asks whether oxygen is low; hypoventilation asks whether ventilation is inadequate and CO2 is rising.",
       "Why can supplemental oxygen make the saturation look better while leaving the core ventilatory disorder untreated?", "sleep_interpretation"),
    _q("v266_sleep_hypovent_app", "Sleep-Related Hypoventilation", "application",
       "An obese patient has daytime hypercapnia and overnight sustained CO2 elevation with desaturation, while the obstructive AHI is only modest. What should rise to the top of the differential?",
       ["Obesity-related hypoventilation physiology, after excluding other causes of alveolar hypoventilation, rather than assuming the gas-exchange burden is explained by mild OSA alone", "Primary snoring", "Isolated positional OSA", "A purely nasal obstruction problem"], 0,
       "Awake hypercapnia plus sleep-related hypoventilation in obesity should prompt evaluation for obesity hypoventilation syndrome after considering alternative pulmonary, neuromuscular, medication and metabolic causes.",
       ["Correct. The degree and persistence of hypercapnia require a ventilatory diagnosis beyond mild obstructive event burden.", "Primary snoring does not cause chronic awake hypercapnia.", "Positional obstruction does not explain sustained daytime carbon-dioxide retention.", "Nasal obstruction may affect airflow or PAP tolerance but does not explain global alveolar hypoventilation."],
       "If CO2 is high while awake, the problem has moved beyond ordinary isolated OSA.",
       "How would chronic opioid use, restrictive lung disease or neuromuscular weakness change the differential and device choice?", "sleep_interpretation"),
    _q("v266_sleep_hypovent_snr", "Sleep-Related Hypoventilation", "senior_decision",
       "A patient with neuromuscular weakness, orthopnea and nocturnal hypercapnia is referred for palatal surgery because of snoring. What is the best senior plan?",
       ["Prioritize assessment and treatment of ventilatory muscle failure and nocturnal hypoventilation; perform upper-airway surgery only if a separate clinically important obstructive target is demonstrated", "Perform palatal surgery first because snoring proves obstruction is the main problem", "Treat with oxygen alone and ignore CO2", "Use AHI alone to choose the operation"], 0,
       "Neuromuscular hypoventilation can be life-threatening and is not corrected by palatal tissue surgery. Ventilatory support and disease-specific evaluation take priority unless a distinct obstructive lesion is also present.",
       ["Correct. The dominant physiology is ventilatory failure, so treatment must support ventilation.", "Snoring is nonspecific and does not override objective hypercapnic ventilatory failure.", "Oxygen alone does not provide ventilation and may mask persistent CO2 retention.", "AHI may underrepresent sustained hypoventilation and cannot select an operation by itself."],
       "A surgeon should not confuse an audible airway symptom with the dominant physiologic disorder.",
       "Which perioperative respiratory risks would make elective surgery particularly hazardous in a patient with weak cough and marginal ventilatory reserve?", "OR_prep"),

    _q("v266_sleep_positional_fnd", "Positional OSA", "foundation",
       "What is the key concept behind positional OSA?",
       ["Obstructive disease is substantially worse in one sleep position, usually supine, so body position is part of the phenotype rather than a trivial PSG detail", "Central apneas occur only while prone", "Any patient who snores while supine has severe OSA", "Position replaces the need to examine sleep stage and event type"], 0,
       "Position can materially change pharyngeal collapsibility and the measured obstructive burden. A positional phenotype can influence counseling and treatment selection, especially when nonsupine disease is limited.",
       ["Correct. Position can identify a modifiable contributor to obstruction.", "Central events are defined by effort, not by a specific body position.", "Supine snoring alone does not establish OSA severity.", "Position is one dimension of PSG interpretation and must be integrated with stage, event type and gas exchange."],
       "Always look at the supine and nonsupine breakdown before calling residual OSA uniformly severe.",
       "How can inadequate nonsupine sleep time make a positional conclusion unreliable?", "sleep_interpretation"),
    _q("v266_sleep_positional_app", "Positional OSA", "application",
       "After successful multilevel OSA surgery, PSG shows a residual AHI of 13/hour overall, 28/hour supine and 2/hour nonsupine with adequate time recorded in both positions. What is the most useful interpretation?",
       ["The residual disease is strongly positional, making a positional strategy a reasonable lower-morbidity option before assuming another operation is required", "The surgery failed completely because the total AHI is above normal", "The patient now has central sleep apnea", "Repeat the identical operation because supine events prove scar formation"], 0,
       "The positional breakdown reveals a treatment-relevant phenotype hidden by the total AHI. If nonsupine sleep is reliably near-normal, positional therapy may address the residual burden without immediate revision surgery.",
       ["Correct. Treat the phenotype that remains after surgery.", "A meaningful surgical response can coexist with residual disease that is now amenable to another modality.", "Central apnea requires absent respiratory effort; position dependence alone does not establish central physiology.", "Supine recurrence does not prove scar-related technical failure or justify repeating the same operation."],
       "A single total AHI can hide a very different postoperative treatment problem.",
       "How would the recommendation change if nearly all nonsupine sleep occurred in N2 but the patient's severe events clustered in supine REM?", "sleep_interpretation"),
    _q("v266_sleep_positional_snr", "Positional OSA", "senior_decision",
       "A patient requests major revision sleep surgery for residual OSA. The only postoperative PSG contains 12 minutes of nonsupine sleep and labels the disease 'positional.' What is the best senior response?",
       ["Question the robustness of the positional label and obtain enough reliable phenotype data before using it to avoid or justify a major revision operation", "Accept the label without reviewing sleep time by position", "Proceed directly to MMA because the total AHI remains elevated", "Assume positional therapy will work because any nonsupine epoch was recorded"], 0,
       "Position-specific indices can be unstable when exposure to one position is minimal. Major treatment decisions should not rest on a denominator too small to represent the patient's habitual sleep.",
       ["Correct. Adequate sampling and clinically coherent interpretation are required before committing to a major treatment pathway.", "A positional label is only as reliable as the underlying position-specific sleep exposure and scoring.", "MMA may be effective in selected patients but should not be chosen from an inadequately characterized residual phenotype.", "A few minutes of nonsupine sleep cannot establish durable response to positional therapy."],
       "Before making a big surgical decision from a PSG ratio, inspect the denominators.",
       "When would home sleep testing be insufficient to answer the residual-phenotype question because CO2, sleep stage or central-event characterization is essential?", "senior_decision"),
]


def apply_learning_ladders_v266(challenges, concept_id_fn):
    existing = {q.get("id") for q in challenges}
    added = 0
    for source in VIGNETTES_V266:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return added
