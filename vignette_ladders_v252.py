"""v25.2 — Laryngology / Voice / Swallowing deliberate ladder pass 3.

Reuses five strong v12.8 diagnostic foundations rather than duplicating them,
then adds only the missing application and senior-decision layers. Canonical
linkage is explicit because two retained foundations intentionally use older
display labels that are reconciled to the live registry.
"""
DOMAIN = "Laryngology / Voice / Swallowing"

FOUNDATIONS_V252 = {
    "v128_lar_04": "Reinke Edema",
    "v128_lar_05": "Presbyphonia",
    "v128_lar_06": "Muscle Tension Dysphonia",
    "v128_lar_09": "Vocal Fold Sulcus / Scar",
    "v128_lar_10": "Inducible Laryngeal Obstruction / PVFM",
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


VIGNETTES_V252 = [
    # Reinke edema
    _q(
        "v252_lar_reinke_app", "Reinke Edema", "application",
        "A 52-year-old smoker with bilateral Reinke edema has a markedly deep voice but no stridor. There is no suspicious focal lesion. Which initial management best addresses the disease rather than only the sound of the voice?",
        ["Smoking cessation plus voice/irritant optimization, reserving phonomicrosurgery for persistent function-limiting disease", "Immediate bilateral aggressive stripping of the vocal-fold cover", "Botulinum toxin injection into both posterior cricoarytenoid muscles", "Permanent tracheostomy because the edema cannot regress"], 0,
        "Reinke edema reflects chronic injury of the superficial lamina propria, strongly associated with smoking and phonatory irritation. Risk-factor control is part of treatment; surgery is considered when voice burden, airway burden, or persistent bulky disease justifies it.",
        ["Correct. Treating tobacco exposure and phonatory contributors reduces ongoing injury and improves the durability of any later surgery.", "Aggressive stripping risks scar and loss of pliable cover; tissue-preserving phonomicrosurgery is the operative principle when surgery is needed.", "PCA botulinum toxin weakens the principal vocal-fold abductor and is not treatment for Reinke edema.", "Most patients do not require a permanent airway; airway intervention depends on actual obstruction severity."],
        "For Reinke edema, smoking cessation is disease treatment—not merely perioperative advice.",
        "What laryngoscopic finding would make you biopsy rather than assume all polypoid change is benign?", "boards"),
    _q(
        "v252_lar_reinke_snr", "Reinke Edema", "senior_decision",
        "A patient with massive bilateral Reinke edema now has exertional stridor and is scheduled for suspension microlaryngoscopy. The glottic inlet is visibly narrowed. What is the best senior-level operative principle?",
        ["Plan the airway with anesthesia before induction and use conservative, staged, epithelium-preserving debulking when needed rather than maximizing bilateral tissue removal", "Assume routine intubation will always be easy because the lesion is benign", "Excise the entire superficial lamina propria down to vocalis muscle on both sides", "Perform bilateral cordotomy as the standard first operation"], 0,
        "Bulky Reinke edema can become an airway problem and can make induction/intubation less predictable. The operation must protect both the airway and the vibratory cover; excessive bilateral resection can create stiffness, webs, and lasting dysphonia.",
        ["Correct. Airway planning and conservative tissue preservation matter more than achieving a perfectly flat fold in one sitting.", "Benign pathology does not guarantee a safe airway; lesion bulk and glottic aperture determine risk.", "Deep bilateral stripping sacrifices the vibratory layer and greatly increases scar risk.", "Cordotomy is an airway-widening operation for selected glottic immobility, not routine treatment of superficial polypoid edema."],
        "In massive Reinke edema, think airway first and vibratory preservation second; cosmetic-looking overresection can permanently worsen voice.",
        "If one side contains an irregular leukoplakic focus in a heavy smoker, how would that alter specimen handling and oncologic caution?", "OR_prep"),

    # Presbyphonia
    _q(
        "v252_lar_presby_app", "Presbyphonia", "application",
        "An older adult has bilateral vocal-fold atrophy, bowing, and a spindle-shaped gap with bothersome weak voice. There is no neurologic motion deficit or mucosal lesion. What is the best first treatment strategy?",
        ["Behavioral voice therapy directed at breath support, efficient closure, and compensatory hyperfunction", "Immediate recurrent-laryngeal-nerve exploration", "Long-term complete voice rest", "Posterior cordotomy"], 0,
        "Presbyphonia is usually approached first with voice therapy because many patients improve by optimizing respiratory support and phonatory efficiency. Augmentation is reasonable when glottic insufficiency remains functionally important despite therapy or when the patient needs additional closure.",
        ["Correct. Therapy addresses the functional consequences of age-related atrophy without committing the patient to a procedure.", "Symmetric age-related bowing with preserved motion does not suggest an RLN lesion needing exploration.", "Prolonged silence does not reverse vocal-fold atrophy and can worsen conditioning.", "Cordotomy enlarges the posterior airway and would worsen glottic insufficiency."],
        "Presbyphonia is a glottic-insufficiency problem; start by improving efficiency, then add closure when needed.",
        "Which symptoms or asymmetric findings would make you reopen the diagnosis instead of attributing dysphonia to age?", "boards"),
    _q(
        "v252_lar_presby_snr", "Presbyphonia", "senior_decision",
        "A highly communicative older patient has persistent breathy dysphonia from bilateral atrophy despite excellent voice-therapy participation. The patient is unsure whether more permanent medialization would provide enough benefit. What is the most useful next strategy?",
        ["Use office injection augmentation as a therapeutic trial and reassess voice, effort, cough, and patient-reported benefit before considering a durable framework procedure", "Perform bilateral arytenoidectomy", "Promise that permanent thyroplasty will restore a youthful mucosal wave", "Stop treatment because age-related atrophy cannot be improved"], 0,
        "A temporary or intermediate-duration augmentation can test how much of the disability comes from glottic insufficiency and whether improved closure meaningfully helps. That information can guide whether repeat injection or durable bilateral medialization is worthwhile.",
        ["Correct. Trial augmentation converts an uncertain anatomic hypothesis into patient-specific functional information.", "Arytenoidectomy enlarges the airway and is directionally opposite to treatment of atrophic glottic insufficiency.", "Medialization can improve closure but does not reverse all age-related vibratory changes or guarantee a youthful voice.", "Presbyphonia is treatable when symptoms warrant intervention; age alone is not a reason to withhold rehabilitation."],
        "When the expected benefit of durable medialization is uncertain, a reversible augmentation trial can be a decision tool.",
        "How would significant dysphagia, poor cough, or pulmonary disease change the value you place on improved glottic closure?", "senior_management"),

    # Muscle tension dysphonia
    _q(
        "v252_lar_mtd_app", "Muscle Tension Dysphonia", "application",
        "A teacher has supraglottic squeeze and fluctuating dysphonia. Before labeling this primary muscle-tension dysphonia and prescribing therapy alone, what is the most important diagnostic step?",
        ["Look carefully for an underlying glottic insufficiency, subtle paresis, mucosal lesion, or other driver of compensatory hyperfunction", "Diagnose primary MTD whenever supraglottic compression is visible", "Order a temporal-bone CT as the only evaluation", "Inject botulinum toxin into the PCA muscles immediately"], 0,
        "Supraglottic hyperfunction is a behavior, not a complete diagnosis. It may be primary, but it commonly compensates for glottic insufficiency, subtle paresis, or a mucosal lesion; stroboscopic and functional examination should search for the driver.",
        ["Correct. Treating secondary hyperfunction without recognizing its cause can leave the patient symptomatic.", "Supraglottic compression is nonspecific and can be compensatory.", "Temporal-bone imaging does not answer the key phonatory-mechanics question.", "PCA botulinum toxin can impair abduction and is not routine treatment for MTD."],
        "Do not confuse the visible compensation with the disease that forced the compensation.",
        "What stroboscopic closure pattern would make you suspect subtle unilateral paresis beneath apparent muscle tension?", "boards"),
    _q(
        "v252_lar_mtd_snr", "Muscle Tension Dysphonia", "senior_decision",
        "A professional voice user has persistent supraglottic hyperfunction despite skilled voice therapy. Stroboscopy now shows a small persistent glottic gap and asymmetric phase suggesting subtle unilateral paresis. What is the best next decision?",
        ["Reframe the problem as secondary hyperfunction and treat the underlying glottic insufficiency—potentially with a diagnostic/therapeutic augmentation—while continuing targeted therapy", "Escalate neck muscle exercises indefinitely without addressing closure", "Perform bilateral cordectomy", "Diagnose spasmodic dysphonia solely because therapy did not cure the symptoms"], 0,
        "Failure of appropriate therapy should trigger diagnostic reassessment. When hyperfunction is compensating for inadequate closure, improving the closure can reduce the need for supraglottic squeeze and make behavioral therapy more effective.",
        ["Correct. The senior move is to revise the mechanism when new evidence shows secondary rather than primary hyperfunction.", "More therapy directed at the compensation alone may fail if the glottic driver remains untreated.", "Cordectomy would worsen glottic insufficiency and has no role here.", "Therapy failure alone does not diagnose laryngeal dystonia; spasmodic dysphonia has characteristic task-specific voice breaks."],
        "A treatment failure can be diagnostic information: reassess whether the muscle tension is primary or compensatory.",
        "When would laryngeal EMG add useful information in a suspected subtle paresis?", "senior_management"),

    # Vocal-fold sulcus/scar
    _q(
        "v252_lar_sulcus_app", "Vocal Fold Sulcus / Scar", "application",
        "A patient with focal vocal-fold scar has a rough breathy voice, reduced mucosal wave, and a persistent glottic gap despite voice therapy. Which intervention is most useful before promising a scar-directed operation?",
        ["Consider trial augmentation to determine how much symptom burden improves by correcting closure even though mucosal stiffness remains", "Strip the epithelium until a normal wave appears", "Perform posterior cordotomy", "Treat the abnormal wave with antibiotics"], 0,
        "Scar and sulcus combine two problems: stiffness of the cover and, in many patients, glottic insufficiency. Augmentation can test and treat the closure component even though it does not restore a normal superficial lamina propria.",
        ["Correct. Separating the closure problem from the stiffness problem helps set realistic expectations and choose the least destructive next step.", "Aggressive epithelial stripping creates additional scar and can worsen vibration.", "Cordotomy enlarges the glottis and would worsen insufficiency.", "Vocal-fold scar is not an infectious process treated with antibiotics."],
        "For scar, ask two separate questions: how stiff is the cover, and how much of the disability is from incomplete closure?",
        "If augmentation improves loudness but roughness persists, what does that teach you about the remaining vibratory limitation?", "boards"),
    _q(
        "v252_lar_sulcus_snr", "Vocal Fold Sulcus / Scar", "senior_decision",
        "A singer with longstanding sulcus vocalis asks for an operation that will reliably restore a normal mucosal wave. Voice therapy and trial augmentation improved effort but not the focal stiffness. What is the best counseling and treatment principle?",
        ["Explain that scar-directed surgery has variable outcomes; individualize between continued rehabilitation, augmentation/medialization, and selected scar-directed techniques while avoiding promises of normal vibration", "Guarantee complete restoration after epithelial excision", "Perform increasingly deep resections until the fold becomes flexible", "Recommend no treatment of any kind because scar is untreatable"], 0,
        "There is no uniformly restorative operation for vocal-fold scar or sulcus. Procedures may improve closure or selected aspects of vibration, but manipulation of the lamina propria can also worsen scarring. Goals and risk tolerance are central, especially for professional voice users.",
        ["Correct. Chief-level management is expectation-sensitive and often staged because the biology of scar limits predictability.", "No operation can guarantee restoration of normal layered microstructure and wave.", "Deeper resection increases tissue injury and scar rather than reliably improving pliability.", "Rehabilitation, augmentation, medialization, and selected scar-directed procedures can all be useful in carefully chosen patients."],
        "Scar surgery is a risk-benefit conversation about improvement, not a promise to recreate normal lamina propria.",
        "How would a contralateral normal fold and excellent closure change your willingness to manipulate the scarred side?", "senior_management"),

    # ILO / PVFM
    _q(
        "v252_lar_ilo_app", "Inducible Laryngeal Obstruction / PVFM", "application",
        "A collegiate runner has reproducible inspiratory stridor only at peak exercise and has not improved with escalating asthma therapy. Baseline laryngoscopy is normal. What is the best next diagnostic strategy?",
        ["Provocation that reproduces symptoms, ideally continuous laryngoscopy during exercise when available, to document dynamic laryngeal obstruction", "Diagnose refractory asthma without observing the larynx during symptoms", "Perform direct laryngoscopy under general anesthesia only", "Order a static neck radiograph and stop the workup if it is normal"], 0,
        "ILO is dynamic and the larynx may look normal at rest. Reproducing the trigger while visualizing the larynx is especially useful for exercise-induced disease and helps prevent further unnecessary asthma escalation.",
        ["Correct. The diagnostic target is the laryngeal behavior during the event, not the normal resting anatomy.", "Asthma may coexist, but repeated treatment failure plus inspiratory symptoms should prompt direct testing for ILO.", "General anesthesia removes the physiologic trigger and may normalize the dynamic obstruction.", "A normal static radiograph cannot exclude intermittent glottic or supraglottic obstruction."],
        "If the disease is inducible, the test often needs to induce it.",
        "How do glottic versus supraglottic exercise-induced obstruction patterns affect what you teach the patient?", "boards"),
    _q(
        "v252_lar_ilo_snr", "Inducible Laryngeal Obstruction / PVFM", "senior_decision",
        "A patient with known ILO arrives during a dramatic episode with inspiratory noise and throat tightness. Oxygen saturation is normal, air movement is adequate, and the patient can phonate; prior episodes resolve with coached breathing. What is the best senior-level approach?",
        ["Maintain airway vigilance while using reassurance and coached rescue-breathing/SLP techniques, and avoid reflexive intubation unless objective evidence shows true airway failure or another dangerous diagnosis", "Intubate every known ILO episode immediately", "Give repeated antibiotics because inspiratory stridor is usually bacterial", "Perform permanent tracheostomy to prevent future episodes"], 0,
        "Most ILO episodes are frightening but self-limited when gas exchange and airway patency remain adequate. Calm coaching and learned breathing strategies can abort attacks, while the clinician simultaneously watches for evidence that this episode is not benign ILO.",
        ["Correct. The challenge is avoiding iatrogenic escalation without becoming complacent about a genuinely deteriorating airway.", "Automatic intubation can create harm in a patient whose dynamic obstruction is resolving and whose ventilation is intact.", "ILO is not a bacterial infection and antibiotics do not address its mechanism.", "Permanent airway surgery is not routine therapy for episodic functional/dynamic laryngeal obstruction."],
        "Known ILO should reduce reflexive airway intervention—not eliminate airway assessment.",
        "Which findings—hypoxemia, progressive fatigue, fixed obstruction, edema, foreign body, or inability to ventilate—would force you to abandon the ILO assumption?", "overnight_call"),
]


def apply_learning_ladders_v252(challenges, item_id_fn):
    """Promote strong v12.8 foundations and merge missing Laryngology layers."""
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    tagged = []
    for qid, canonical_topic in FOUNDATIONS_V252.items():
        q = by_id.get(qid)
        if not q:
            raise RuntimeError(f"v25.2 missing reviewed foundation {qid}")
        expected = item_id_fn(DOMAIN, canonical_topic)
        q["concept_id"] = expected
        q["canonical_topic"] = canonical_topic
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        q["_coverage_reviewed_v211"] = True
        tagged.append(qid)

    existing = set(by_id)
    added = []
    for source in VIGNETTES_V252:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = item_id_fn(DOMAIN, q["topic"])
        q["canonical_topic"] = q["topic"]
        challenges.append(q)
        existing.add(q["id"])
        added.append(q["id"])
    return {"tagged_foundations": tagged, "added": added}
