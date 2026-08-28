"""v26.7 — Sleep Surgery deliberate ladder pass 4 and domain closure.

Closes the six exact canonical Sleep Surgery concepts not yet protected by the
v26.6 15-topic gate. Strong v13.7 cases are preserved and upgraded in place
with explicit learning-stage metadata and individualized distractor reasoning;
only the genuinely missing stages are added.
"""
DOMAIN = "Sleep Surgery"

REUSED = {
    "v137_slp_02": ("Circadian Rhythm Sleep-Wake Disorders", "foundation"),
    "v137_slp_03": ("Down Syndrome Pediatric HNS", "application"),
    "v137_slp_06": ("Lingual Tonsil / Tongue-Base Obstruction", "application"),
    "v137_slp_07": ("Narcolepsy / Central Hypersomnolence Recognition", "foundation"),
    "v137_slp_10": ("Palatal Surgery Selection for OSA", "application"),
    "v137_slp_12": ("Restless Legs / Periodic Limb Movement Disorders", "foundation"),
}

REUSED_REASONS = {
    "v137_slp_02": [
        "Correct. A stable late sleep window with normal sleep when allowed is a circadian-timing phenotype, not evidence of upper-airway obstruction.",
        "OSA requires an obstructive sleep-breathing phenotype; delayed sleep timing alone does not establish it.",
        "Narcolepsy causes central hypersomnolence and characteristic REM phenomena rather than a consistently delayed preferred sleep window.",
        "Central apnea is a respiratory-event disorder and does not explain a reproducible delayed sleep schedule.",
    ],
    "v137_slp_03": [
        "Correct. Pediatric HNS is a phenotype-selected therapy: residual OSA severity, anatomy, DISE pattern, comorbidity and current candidacy criteria all matter.",
        "Implantation without confirming the current obstructive physiology and airway pattern risks treating the wrong mechanism.",
        "Persistent OSA after adenotonsillectomy is common in selected high-risk children and does not eliminate other evidence-based treatments.",
        "Adult palatal operations are not a default solution for the multilevel hypotonia and tongue-base obstruction common in Down syndrome.",
    ],
    "v137_slp_06": [
        "Correct. Lingual tonsillectomy directly targets documented lingual-tonsil obstruction when it is a meaningful residual site.",
        "Repeat adenoid surgery does not address a tongue-base target when there is no clinically important adenoid regrowth.",
        "Septoplasty may improve nasal airflow but does not remove vallecular obstruction from hypertrophic lingual tonsil tissue.",
        "A surgically addressable residual site exists; the decision is whether its expected benefit justifies the airway and swallowing risks.",
    ],
    "v137_slp_07": [
        "Correct. Cataplexy with irresistible daytime sleep episodes should trigger a central-hypersomnolence evaluation, generally using appropriately prepared overnight PSG and MSLT when indicated.",
        "Palatal surgery treats retropalatal obstruction and does not treat narcolepsy.",
        "Daytime sleepiness is not specific for OSA; the history here contains features much more characteristic of narcolepsy.",
        "Nasal steroids may help inflammatory nasal obstruction but do not address cataplexy or central hypersomnolence.",
    ],
    "v137_slp_10": [
        "Correct. Contemporary palatal surgery should be selected to match the demonstrated collapse pattern and the rest of the airway phenotype.",
        "Tongue-base surgery is not automatically indicated when the dominant target is isolated palatal collapse.",
        "DISE can materially refine collapse pattern and procedure selection in appropriately selected surgical candidates.",
        "Nasal surgery can improve breathing or PAP tolerance but is not a universal cure for pharyngeal OSA.",
    ],
    "v137_slp_12": [
        "Correct. The urge-to-move pattern that worsens at rest in the evening and improves with movement is classic for restless legs syndrome; iron status and medication contributors are actionable.",
        "UPPP treats selected pharyngeal obstruction and has no role in a sensorimotor leg disorder without an obstructive target.",
        "HNS treats selected obstructive sleep apnea and does not treat restless legs syndrome.",
        "Insomnia can coexist with RLS, but labeling the symptom alone misses the specific and potentially treatable sensorimotor disorder.",
    ],
}


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


VIGNETTES_V267 = [
    # Circadian Rhythm Sleep-Wake Disorders: preserve the strong v137 foundation.
    _q("v267_sleep_circ_app", "Circadian Rhythm Sleep-Wake Disorders", "application",
       "A resident reports chronic difficulty falling asleep before 2-3 AM but sleeps a normal duration and feels well when allowed to wake late. Airway examination is unremarkable and there is no convincing snoring or witnessed apnea history. What is the best next step?",
       ["Characterize sleep timing with history and a sleep diary or actigraphy and use circadian-timed behavioral/light interventions rather than ordering airway surgery", "Schedule DISE because any daytime fatigue implies occult obstruction", "Offer UPPP for insomnia", "Start nocturnal oxygen without sleep evaluation"], 0,
       "A consistent delayed sleep window with otherwise restorative sleep is a circadian-timing problem until another disorder is demonstrated. Sleep logs or actigraphy can document the pattern, and treatment depends on appropriately timed schedule, light and sometimes melatonin strategies rather than anatomic airway intervention.",
       ["Correct. Document the clock-time phenotype and treat the circadian mechanism.", "DISE is useful for selected obstructive surgical planning, not for diagnosing a circadian phase disorder without an OSA phenotype.", "UPPP does not correct circadian misalignment and can add morbidity without a target.", "Oxygen does not reset circadian phase and is not indicated from this history."],
       "When sleep is normal at the patient's preferred clock time, ask whether the clock—not the airway—is the disorder.",
       "How would rotating night shifts or irregular days off complicate interpretation of the sleep diary?", "sleep_interpretation"),
    _q("v267_sleep_circ_snr", "Circadian Rhythm Sleep-Wake Disorders", "senior_decision",
       "A patient referred for sleep surgery because of 'CPAP failure and fatigue' has only mild obstructive events on a well-performed PSG but a markedly delayed sleep phase, chronic sleep restriction for work, and normal alertness on vacations when allowed a later schedule. What is the best senior decision?",
       ["Do not escalate anatomic OSA surgery simply to treat fatigue; address insufficient sleep and circadian misalignment and reassess what symptoms are actually attributable to obstruction", "Perform multilevel sleep surgery because CPAP was not tolerated", "Implant HNS for fatigue regardless of obstructive burden", "Ignore sleep timing because PSG already measured AHI"], 0,
       "Surgical candidacy requires both a surgically correctable obstructive phenotype and a realistic symptom target. When sleepiness is better explained by chronic sleep restriction and circadian mismatch, more airway surgery may not improve the patient's complaint.",
       ["Correct. Senior sleep-surgery judgment includes recognizing when the symptom generator is nonanatomic.", "PAP intolerance alone does not create an indication for irreversible airway surgery when obstruction is mild and another cause of fatigue is stronger.", "HNS requires appropriate obstructive physiology and candidacy; fatigue alone is not an indication.", "AHI does not explain every form of sleepiness, and clock-time history remains essential."],
       "A sleep surgeon should be willing to say: the airway may not be the reason this patient is tired.",
       "What objective or diary-based improvement would support treating the circadian problem before reconsidering residual OSA therapy?", "senior_decision"),

    # Down Syndrome Pediatric HNS: preserve the existing application case.
    _q("v267_sleep_ds_hns_fnd", "Down Syndrome Pediatric HNS", "foundation",
       "Why can obstructive sleep apnea persist after adenotonsillectomy in a child with Down syndrome?",
       ["Multilevel obstruction from relative macroglossia, tongue-base collapse, hypotonia, craniofacial anatomy and other sites may remain after adenotonsillar tissue is removed", "Adenotonsillectomy always cures Down syndrome OSA", "All residual events are central by definition", "Persistent OSA proves the original surgery was technically inadequate"], 0,
       "Down syndrome OSA is frequently multilevel. Adenotonsillectomy can improve obstruction yet leave tongue-base, supraglottic, craniofacial or hypotonia-related collapse that requires renewed phenotype assessment.",
       ["Correct. Residual OSA often reflects persistent multilevel anatomy and neuromuscular tone rather than one missed adenotonsillar target.", "Adenotonsillectomy is important but does not guarantee cure in a high-risk multilevel phenotype.", "Residual events must be classified from PSG; they are not automatically central.", "Persistent disease can occur despite technically successful surgery because the remaining obstruction is elsewhere."],
       "In Down syndrome, successful adenotonsillectomy can still leave a different obstructive airway behind.",
       "Which residual sites are especially useful to assess with DISE before choosing another operation?", "boards"),
    _q("v267_sleep_ds_hns_snr", "Down Syndrome Pediatric HNS", "senior_decision",
       "A child with Down syndrome has persistent sleep symptoms after adenotonsillectomy. Repeat PSG now shows substantial nocturnal hypoventilation with relatively little obstructive burden, and DISE does not show a convincing HNS-responsive tongue-base pattern. What is the best senior decision?",
       ["Do not force HNS into a nonmatching phenotype; evaluate and treat the hypoventilation and other causes of symptoms before reconsidering obstruction-directed surgery", "Implant HNS because prior adenotonsillectomy failed", "Increase the total AHI by counting hypoventilation as obstruction to meet surgical criteria", "Perform tongue-base reduction despite the absence of a defined target"], 0,
       "Pediatric HNS remains an obstruction-directed therapy. When the dominant residual problem is hypoventilation or the airway phenotype is unfavorable, treatment should redirect to the actual physiology instead of using prior surgery failure as the indication for another device.",
       ["Correct. Device therapy should match the current mechanism, not the historical diagnosis.", "Failure of one airway operation does not establish candidacy for a different one.", "Hypoventilation is not an obstructive apnea and should not be relabeled to manufacture candidacy.", "Tongue-base surgery without a demonstrated obstructive target exposes the child to risk without a clear mechanism of benefit."],
       "Residual pediatric OSA care is phenotype-driven; HNS is not the automatic next step after adenotonsillectomy.",
       "How would major weight change, new central events, or progressive pulmonary disease alter longitudinal device candidacy?", "senior_decision"),

    # Lingual tonsil / tongue-base obstruction: preserve the v137 application case.
    _q("v267_sleep_lingual_fnd", "Lingual Tonsil / Tongue-Base Obstruction", "foundation",
       "A child remains obstructed after adenotonsillectomy. Which finding most strongly supports lingual tonsil tissue as a meaningful residual target?",
       ["Endoscopic or DISE evidence that hypertrophic lingual tonsil tissue fills the vallecula and contributes to tongue-base obstruction", "A normal tongue base with isolated nasal congestion", "Central apneas without respiratory effort", "A normal airway study with only restless legs symptoms"], 0,
       "Lingual tonsil hypertrophy is a recognized cause of residual pediatric OSA, particularly after prior adenotonsillectomy and in selected syndromic patients. Treatment should follow documented obstruction rather than the mere presence of lymphoid tissue.",
       ["Correct. The target is not simply visible tissue; it is tissue demonstrated to contribute to obstruction.", "Isolated nasal disease does not establish a lingual-tonsil surgical target.", "Central events are a respiratory-drive problem rather than a lingual-tonsil obstruction phenotype.", "Restless legs symptoms do not localize obstruction to the tongue base."],
       "For residual OSA, prove that the lingual tonsil is obstructing—not merely present.",
       "What other tongue-base or supraglottic findings can coexist with lingual tonsil hypertrophy on DISE?", "boards"),
    _q("v267_sleep_lingual_snr", "Lingual Tonsil / Tongue-Base Obstruction", "senior_decision",
       "A medically complex child has severe residual OSA with DISE-confirmed lingual tonsil and tongue-base obstruction. Lingual tonsillectomy is planned. Which perioperative issue should most influence the senior operative plan?",
       ["Anticipate postoperative tongue-base edema, bleeding, dysphagia and airway compromise and choose monitoring/intubation strategy according to severity and comorbidity", "Treat the operation like routine office tonsil debridement because the palatine tonsils are already gone", "Plan same-day discharge regardless of baseline severity", "Avoid discussing swallowing because lingual tonsil surgery cannot affect it"], 0,
       "Tongue-base surgery occurs in a confined airway and can produce edema, bleeding and swallowing dysfunction. Severe OSA, syndromic anatomy, pulmonary disease and the extent of multilevel surgery should determine postoperative airway and monitoring strategy.",
       ["Correct. Operative success includes planning for the airway after the obstruction has been surgically manipulated.", "The tongue base has different postoperative airway consequences from an office procedure or uncomplicated superficial debridement.", "Disposition should be risk-based rather than automatic.", "Lingual tonsil and tongue-base surgery can cause pain and dysphagia and deserves explicit counseling and monitoring."],
       "For tongue-base surgery, the postoperative airway is part of the operation.",
       "What findings would make planned postoperative intubation or ICU-level observation more reasonable?", "OR_prep"),

    # Narcolepsy / central hypersomnolence: preserve the v137 recognition case.
    _q("v267_sleep_narc_app", "Narcolepsy / Central Hypersomnolence Recognition", "application",
       "A patient with excessive daytime sleepiness is being considered for MSLT. They sleep only five hours nightly and have untreated moderate OSA. What is the best interpretation strategy?",
       ["Correct insufficient sleep and adequately treat the competing sleep disorder before relying on MSLT, because both can create misleading sleepiness and REM-latency findings", "Perform MSLT immediately and diagnose narcolepsy from any short sleep latency", "Offer airway surgery solely to make the MSLT normal", "Diagnose narcolepsy from daytime sleepiness alone"], 0,
       "MSLT is highly context dependent. Inadequate sleep, untreated OSA, circadian misalignment and medications can confound sleep latency and sleep-onset REM periods, so appropriate preparation and treatment of competing causes are essential.",
       ["Correct. A technically performed test can still be clinically invalid if the patient is sleep deprived or has untreated competing disease.", "Short latency is nonspecific when sleep debt and untreated OSA are present.", "Airway surgery is not performed to normalize a diagnostic test; obstruction should be treated for its own indications.", "Daytime sleepiness has a broad differential and does not by itself diagnose narcolepsy."],
       "Before trusting an MSLT, make sure the patient had a fair chance to be normally alert.",
       "Which medication classes can suppress or rebound REM and complicate MSLT interpretation?", "sleep_interpretation"),
    _q("v267_sleep_narc_snr", "Narcolepsy / Central Hypersomnolence Recognition", "senior_decision",
       "An adult has technically successful OSA surgery with a postoperative PSG showing well-controlled obstruction, yet disabling sleep attacks and cataplexy persist. What is the best senior response?",
       ["Stop escalating airway surgery and refer for central hypersomnolence evaluation because the persistent symptom phenotype is no longer explained by obstruction", "Perform another palatal procedure because sleepiness remains", "Assume the postoperative PSG is wrong because symptoms persist", "Implant HNS despite controlled obstruction"], 0,
       "Persistent sleepiness after effective OSA treatment requires a differential that includes insufficient sleep, medications, mood disorders and central hypersomnolence. Cataplexy is a particularly strong clue that further airway enlargement is the wrong treatment mechanism.",
       ["Correct. Re-establish the cause of symptoms before exposing the patient to another irreversible intervention.", "Additional palatal surgery is unlikely to treat cataplexy or central sleep attacks when obstruction is already controlled.", "Symptoms can arise from more than one sleep disorder; an improved PSG and persistent symptoms are not mutually exclusive.", "HNS treats selected obstruction and is not indicated when obstruction is already controlled."],
       "Residual sleepiness after successful OSA therapy is a diagnostic problem before it is a surgical failure.",
       "What history distinguishes true cataplexy from nonspecific weakness, syncope, or fatigue?", "senior_decision"),

    # Palatal Surgery Selection: preserve the v137 application case.
    _q("v267_sleep_pal_select_fnd", "Palatal Surgery Selection for OSA", "foundation",
       "What is the main reason modern palatal surgery for OSA should not be chosen from AHI alone?",
       ["Different patients have different velum collapse patterns and multilevel anatomy, so procedure selection should match the demonstrated mechanism while preserving speech and swallowing function", "AHI directly identifies which palatal muscle is collapsing", "Every patient benefits most from the same classic UPPP", "Palatal surgery is independent of airway anatomy"], 0,
       "The AHI quantifies event burden but does not localize collapse. Awake examination and, in selected surgical candidates, DISE can identify anteroposterior, lateral or concentric palatal behavior and competing tongue-base/lateral-wall targets.",
       ["Correct. Severity and anatomic mechanism answer different clinical questions.", "AHI does not provide spatial collapse anatomy.", "A universal palatal operation ignores major differences in collapse pattern and functional risk.", "Palatal operations deliberately alter airway anatomy and therefore must be anatomy-specific."],
       "AHI tells you how much OSA; collapse phenotype helps tell you what operation might make sense.",
       "Which palatal functional complications should be considered when choosing how aggressively to alter the velopharynx?", "boards"),
    _q("v267_sleep_pal_select_snr", "Palatal Surgery Selection for OSA", "senior_decision",
       "A PAP-intolerant patient has severe OSA. DISE shows complete concentric velum collapse plus major lateral-wall collapse and only minor tongue-base obstruction. What is the best senior surgical principle?",
       ["Build a phenotype-directed plan for the dominant palatal/lateral-wall collapse and do not choose conventional HNS or tongue-base surgery simply because they are available", "Implant conventional HNS solely because the AHI is severe", "Perform isolated tongue-base reduction because any tongue motion is abnormal", "Choose nasal surgery alone as definitive therapy"], 0,
       "Severe OSA does not make every procedure appropriate. Complete concentric palatal collapse is an unfavorable pattern for conventional unilateral HNS candidacy, and a minor tongue-base finding should not distract from the dominant palatal/lateral-wall mechanism.",
       ["Correct. The dominant collapse mechanism should drive procedure selection and counseling.", "Conventional HNS candidacy depends on more than AHI and includes the collapse phenotype.", "Minor tongue-base collapse is not the primary target in this study.", "Nasal surgery may improve nasal breathing or PAP tolerance but is not a dependable sole treatment for severe pharyngeal collapse."],
       "Do not let the availability of a device become the indication for the device.",
       "How would major retrognathia or multilevel collapse shift the discussion toward skeletal advancement or combined treatment?", "senior_decision"),

    # RLS / PLMD: preserve the v137 recognition case.
    _q("v267_sleep_rls_app", "Restless Legs / Periodic Limb Movement Disorders", "application",
       "A patient has classic restless legs symptoms and a low ferritin with no anemia. Which management principle is most appropriate?",
       ["Address iron deficiency when appropriate and review aggravating medications and sleep habits before escalating symptom-directed pharmacotherapy", "Offer tongue-base surgery", "Ignore iron because hemoglobin is normal", "Treat with supplemental oxygen"], 0,
       "Brain iron availability can be relevant to restless legs syndrome even without frank anemia. Management includes correcting contributing iron deficiency when appropriate and reviewing medications or behaviors that worsen symptoms.",
       ["Correct. Treat reversible contributors before assuming the disorder requires more invasive or complex therapy.", "Tongue-base surgery does not treat a sensorimotor leg disorder.", "Normal hemoglobin does not exclude low iron stores relevant to RLS.", "Oxygen does not treat the urge-to-move mechanism of RLS."],
       "For RLS, iron stores can matter even when the CBC looks normal.",
       "Which antidepressant, antihistamine, or dopamine-blocking exposures can worsen symptoms in susceptible patients?", "sleep_management"),
    _q("v267_sleep_rls_snr", "Restless Legs / Periodic Limb Movement Disorders", "senior_decision",
       "A patient with treated OSA remains a poor sleeper. PSG shows frequent periodic limb movements, but the patient denies an urge to move the legs or evening sensory symptoms. What is the best senior interpretation?",
       ["Do not equate a PSG limb-movement index with restless legs syndrome; determine whether movements are clinically significant, medication-related, secondary to another disorder, or incidental before assigning treatment", "Diagnose restless legs syndrome from PSG alone", "Perform repeat airway surgery because sleep quality remains poor", "Assume every limb movement requires dopaminergic therapy"], 0,
       "RLS is a clinical diagnosis, whereas periodic limb movements are a PSG observation that can occur with or without a clinically important disorder. Treatment should follow symptoms, consequences and contributing causes rather than an isolated number.",
       ["Correct. Separate the clinical sensorimotor syndrome from an electrophysiologic observation.", "RLS requires the characteristic clinical urge-to-move phenotype and is not diagnosed by PSG alone.", "Persistent poor sleep after controlled OSA should not automatically be labeled recurrent obstruction.", "Medication decisions require a clinical disorder and risk-benefit assessment, not merely the presence of movements."],
       "Just as AHI is not the whole patient, a limb-movement index is not the diagnosis.",
       "How would untreated OSA, serotonergic medications, renal disease or iron deficiency alter the significance of the limb movements?", "senior_decision"),
]


def apply_learning_ladders_v267(challenges, item_id_fn):
    by_id = {str(q.get("id")): q for q in challenges if q.get("id")}
    reused = 0
    for qid, (topic, stage) in REUSED.items():
        row = by_id.get(qid)
        if row is None:
            raise RuntimeError(f"v267 missing reusable case {qid}")
        choices = list(row.get("choices") or [])
        reasons = list(REUSED_REASONS[qid])
        if len(choices) != len(reasons):
            raise RuntimeError(f"v267 rationale mismatch for {qid}")
        row.update({
            "domain": DOMAIN, "topic": topic, "concept_id": item_id_fn(DOMAIN, topic),
            "learning_stage": stage, "why_wrong": reasons,
            "ladder_reviewed": True, "_coverage_reviewed_v211": True,
        })
        if not row.get("concept_id"):
            raise RuntimeError(f"v267 orphan reusable topic {topic}")
        reused += 1

    existing = set(by_id)
    added = 0
    for q in VIGNETTES_V267:
        if q["id"] in existing:
            continue
        row = dict(q)
        row["concept_id"] = item_id_fn(DOMAIN, row["topic"])
        if not row["concept_id"]:
            raise RuntimeError(f"v267 orphan topic {row['topic']}")
        challenges.append(row)
        existing.add(row["id"])
        added += 1
    return {"reused": reused, "added": added, "reviewed_topics": 6}
