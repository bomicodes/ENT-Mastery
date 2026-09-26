"""ENT Mastery v46.3 -- Learning-ladder gapfill: Laryngology / Voice / Swallowing.

Adds foundation/application/senior_decision Clinical Challenge vignettes for
the 3 Laryngology / Voice / Swallowing topics flagged by
audit_domain_ladder_inventory_v217.py as having no deliberately-reviewed ladder
row (recently-added topics that never got this pass). Grounded in each topic's
existing Deep Curriculum content -- no new clinical facts or numbers introduced
beyond what that content already states.
"""
from copy import deepcopy

DOMAIN = "Laryngology / Voice / Swallowing"

NEW_QUESTIONS = [
    # ---------------------------------------------------------------
    # Laryngopharyngeal Reflux (LPR)
    # ---------------------------------------------------------------
    {
        "id": "v463_laryn_lpr_fnd",
        "domain": DOMAIN,
        "topic": "Laryngopharyngeal Reflux (LPR)",
        "learning_stage": "foundation",
        "stem": "A 45-year-old presents with chronic hoarseness, frequent throat clearing, a globus sensation, and a dry cough. She has no classic heartburn. Laryngoscopy shows mild posterior erythema and edema. What is the most accurate way to frame this presentation?",
        "choices": [
            "This symptom cluster and exam finding are diagnostic of LPR and PPI therapy should be started as definitive treatment",
            "This symptom cluster is nonspecific -- it overlaps allergy, voice overuse, and other laryngeal disorders -- and posterior erythema/edema alone cannot diagnose LPR",
            "The absence of heartburn rules out any reflux contribution entirely",
            "Posterior erythema is a finding unique to reflux and confirms the diagnosis"
        ],
        "answer": 1,
        "explanation": "Chronic hoarseness, throat clearing, globus, and cough are nonspecific and commonly overlap allergy, voice-use disorders, sensory neuropathy, and other laryngeal conditions. Posterior erythema or edema alone cannot diagnose LPR, since no symptom or laryngoscopic sign uniquely localizes symptoms to reflux.",
        "why_wrong": [
            "Treating the exam and symptoms as diagnostic skips the step of assessing competing causes that the workup requires.",
            "Correct.",
            "Lack of typical GERD symptoms does not rule out extraesophageal reflux contribution -- it changes the recommended workup pathway (favor objective testing) rather than excluding the diagnosis.",
            "No laryngoscopic sign, including posterior erythema, uniquely localizes symptoms to reflux."
        ],
        "board_pearl": "Avoid turning nonspecific throat symptoms or erythema into a reflex diagnosis of LPR -- establish whether reflux is objectively or clinically plausible before committing to long-term acid suppression.",
        "curveball": "This patient has isolated extraesophageal symptoms without typical GERD. What should be favored before a prolonged PPI trial?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngopharyngeal-reflux-lpr",
        "ladder_reviewed": True,
        "focus": "boards",
        "curveball_answer": "For isolated extraesophageal symptoms without typical GERD, objective ambulatory reflux testing should be favored before committing to a prolonged PPI trial; endoscopy should be tailored to GI indications rather than performed reflexively.",
    },
    {
        "id": "v463_laryn_lpr_app",
        "domain": DOMAIN,
        "topic": "Laryngopharyngeal Reflux (LPR)",
        "learning_stage": "application",
        "stem": "A 52-year-old with chronic throat clearing and mild dysphonia also reports typical heartburn and regurgitation after meals. Posterior laryngeal erythema is present. Which management approach best fits this presentation?",
        "choices": [
            "Proceed directly to antireflux surgery given the laryngeal findings",
            "A time-limited PPI trial is reasonable since typical GERD symptoms coexist, understanding that symptomatic response is not itself diagnostic",
            "No treatment is indicated because laryngeal findings are never treated empirically",
            "Order objective ambulatory reflux testing before any treatment is considered, regardless of the coexisting typical GERD symptoms"
        ],
        "answer": 1,
        "explanation": "When typical GERD symptoms coexist with laryngeal complaints, a time-limited PPI trial is a reasonable initial step, along with meal timing, weight, and trigger modification. However, response to the trial does not confirm the diagnosis -- if treatment fails, escalation should stop and the phenotype should be reconsidered rather than assumed to be reflux.",
        "why_wrong": [
            "Antireflux surgery is reserved for objectively proven reflux with appropriate symptom correlation and foregut evaluation, not as a first step based on laryngeal findings alone.",
            "Correct.",
            "Empiric management (meal timing, weight/trigger modification, a time-limited PPI trial) is appropriate when typical GERD symptoms coexist.",
            "Favoring objective testing before treatment is the approach for isolated extraesophageal symptoms without typical GERD -- here, typical GERD symptoms are present, supporting a reasonable empiric trial first."
        ],
        "board_pearl": "A PPI trial can be reasonable when typical GERD symptoms coexist, but a symptomatic response is not diagnostic of LPR -- stop escalating empiric therapy and reconsider the phenotype when treatment fails.",
        "curveball": "The patient returns after 8 weeks of PPI therapy with no improvement in throat clearing or dysphonia. What should happen next?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngopharyngeal-reflux-lpr",
        "ladder_reviewed": True,
        "focus": "boards",
        "curveball_answer": "Treatment failure should prompt stopping escalation of acid suppression and reconsidering the phenotype -- reassessing for competing causes of the laryngeal symptoms (allergy, voice-use disorder, sensory neuropathy, or another laryngeal disorder) rather than assuming reflux and further intensifying PPI therapy.",
    },
    {
        "id": "v463_laryn_lpr_snr",
        "domain": DOMAIN,
        "topic": "Laryngopharyngeal Reflux (LPR)",
        "learning_stage": "senior_decision",
        "stem": "A patient has been on escalating PPI doses for a year for presumed LPR, with persistent throat clearing and globus but no typical GERD symptoms, and no objective reflux testing was ever performed. As the supervising senior, how should this case be redirected?",
        "choices": [
            "Continue escalating acid suppression indefinitely since the symptoms have not resolved",
            "Refer directly for antireflux surgery given the chronicity of symptoms",
            "Step back, reassess competing causes of the laryngeal symptoms, and pursue objective evidence that reflux is actually present before continuing to treat it as the primary diagnosis",
            "Add a second acid-suppressing agent without further workup"
        ],
        "answer": 2,
        "explanation": "A year of escalating empiric therapy without objective confirmation, in a patient without typical GERD symptoms, is exactly the scenario the teaching point warns against: nonspecific throat symptoms should not become a reflex diagnosis. The senior-level decision is to stop the reflexive escalation, reassess competing causes (allergy, voice-use disorder, sensory neuropathy, other laryngeal disease), and establish whether reflux is objectively or clinically plausible.",
        "why_wrong": [
            "Continued escalation without response or objective diagnosis repeats the error of treating nonspecific symptoms as confirmed reflux.",
            "Antireflux surgery is reserved for objectively proven reflux with appropriate symptom correlation and foregut evaluation -- not for unexplained throat symptoms alone, which is the situation here.",
            "Correct.",
            "Adding therapy without addressing the diagnostic uncertainty perpetuates the same reflexive approach rather than correcting it."
        ],
        "board_pearl": "A year of unresponsive empiric PPI therapy for unexplained throat symptoms is a signal to reopen the diagnosis, not to escalate treatment further.",
        "curveball": "If ambulatory reflux testing now comes back objectively positive and symptoms correlate, what treatment pathway becomes appropriate?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngopharyngeal-reflux-lpr",
        "ladder_reviewed": True,
        "focus": "postoperative_call",
        "curveball_answer": "With objectively proven reflux and appropriate symptom correlation, and after appropriate foregut evaluation, antireflux surgery becomes an appropriate consideration -- it is reserved for this scenario rather than for unexplained throat symptoms alone.",
    },
    # ---------------------------------------------------------------
    # Laryngeal Electromyography (LEMG)
    # ---------------------------------------------------------------
    {
        "id": "v463_laryn_lemg_fnd",
        "domain": DOMAIN,
        "topic": "Laryngeal Electromyography (LEMG)",
        "learning_stage": "foundation",
        "stem": "A patient has a motionless right vocal fold after thyroid surgery, and it is unclear whether this represents true recurrent laryngeal nerve paralysis or mechanical fixation of the cricoarytenoid joint. What test is classically indicated to help distinguish these two possibilities?",
        "choices": [
            "Laryngeal electromyography (LEMG)",
            "Repeat flexible laryngoscopy alone, without any additional testing",
            "Videofluoroscopic swallow study",
            "Pure-tone audiometry"
        ],
        "answer": 0,
        "explanation": "A motionless or hypomobile vocal fold of uncertain cause -- true neurogenic paralysis versus mechanical fixation such as cricoarytenoid joint fixation or posterior glottic scar -- is the classic indication for laryngeal EMG.",
        "why_wrong": [
            "Correct.",
            "Laryngoscopy alone shows immobility but cannot reliably distinguish neurogenic paralysis from mechanical fixation; that distinction is LEMG's specific role.",
            "Swallow studies assess swallowing function/aspiration risk, not the neurogenic-versus-mechanical question for vocal fold immobility.",
            "Audiometry evaluates hearing and is unrelated to vocal fold immobility."
        ],
        "board_pearl": "A motionless fold is not automatically a 'paralyzed' fold -- LEMG's job is to separate neurogenic from mechanical causes of immobility.",
        "curveball": "Which muscle complex does LEMG typically sample, and what additional muscle can be sampled separately to assess a different nerve?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "ladder_reviewed": True,
        "focus": "boards",
        "curveball_answer": "LEMG samples the thyroarytenoid-lateral cricoarytenoid (TA-LCA) complex, usually via a percutaneous approach through the cricothyroid membrane, and can separately sample the cricothyroid muscle to assess external branch of the superior laryngeal nerve (EBSLN) function.",
    },
    {
        "id": "v463_laryn_lemg_app",
        "domain": DOMAIN,
        "topic": "Laryngeal Electromyography (LEMG)",
        "learning_stage": "application",
        "stem": "LEMG is performed on a patient with a fixed-appearing vocal fold. The study shows normal motor unit recruitment. How should this finding be interpreted, and what should be done next?",
        "choices": [
            "Normal recruitment despite fixed-appearing motion points toward a mechanical cause and should prompt confirmation with laryngeal exam/palpation of the cricoarytenoid joint under anesthesia",
            "Normal recruitment confirms complete recurrent laryngeal nerve paralysis and reinnervation surgery should proceed immediately",
            "Normal recruitment means the study was technically inadequate and must be repeated before any conclusions are drawn",
            "Normal recruitment indicates active denervation requiring urgent injection augmentation"
        ],
        "answer": 0,
        "explanation": "Normal motor unit recruitment despite fixed-appearing motion points toward a mechanical cause of immobility rather than denervation, and should be confirmed with laryngeal examination and palpation of the cricoarytenoid joint under anesthesia.",
        "why_wrong": [
            "Correct.",
            "Normal recruitment is inconsistent with denervation from paralysis -- it points away from a neurogenic cause, not toward proceeding with reinnervation surgery.",
            "Normal recruitment is a valid, interpretable finding on LEMG, not evidence of a failed study.",
            "Active denervation is indicated by fibrillation potentials with reduced or absent voluntary recruitment -- the opposite of what is described here."
        ],
        "board_pearl": "Normal recruitment on LEMG in a fixed-appearing fold should redirect the workup toward mechanical causes (joint fixation, posterior glottic scar), confirmed by exam under anesthesia.",
        "curveball": "What LEMG pattern would instead suggest ongoing but disorganized reinnervation, and what does that pattern imply for prognosis?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "ladder_reviewed": True,
        "focus": "OR_prep",
        "curveball_answer": "Polyphasic, synkinetic reinnervation potentials indicate ongoing but disorganized reinnervation -- a pattern associated with a worse chance of normal, purposeful motion returning, even though it may still eventually stabilize the airway (adductor synkinesis).",
    },
    {
        "id": "v463_laryn_lemg_snr",
        "domain": DOMAIN,
        "topic": "Laryngeal Electromyography (LEMG)",
        "learning_stage": "senior_decision",
        "stem": "A patient underwent LEMG only 4 days after a suspected nerve injury and the study showed no fibrillation potentials, which was initially read as reassuring for an intact nerve. As the senior clinician, how should this result be handled?",
        "choices": [
            "Accept the study as definitive proof of an intact nerve and discharge the patient from further laryngology follow-up",
            "Recognize that fibrillation potentials take time to develop, so testing performed very early after injury can be falsely reassuring, and plan reassessment after several weeks before relying on the study",
            "Immediately proceed to laryngeal reinnervation surgery based on this early reassuring result",
            "Discount LEMG entirely as unhelpful in this patient going forward"
        ],
        "answer": 1,
        "explanation": "Because fibrillation potentials take time to develop, testing performed very early after injury can be falsely reassuring. Many practices favor obtaining LEMG only after several weeks have passed so the study is not misread as normal. The senior-level decision here is to avoid over-reading a too-early study and to plan a properly timed reassessment.",
        "why_wrong": [
            "An early study without fibrillations can be falsely reassuring and should not be treated as definitive.",
            "Correct.",
            "Proceeding to reinnervation surgery based on a potentially falsely reassuring early study risks acting on prognosis data that has not yet had time to become accurate.",
            "LEMG remains useful for diagnosis, prognosis, and timing of intervention when performed at an appropriate interval -- the problem is the timing of this particular study, not the modality itself."
        ],
        "board_pearl": "Do not over-read a study performed too soon after injury -- a falsely normal-looking early exam can mislead both diagnosis and counseling.",
        "curveball": "If a properly timed repeat LEMG shows a favorable prognostic pattern, how might that change the management plan compared with a poor-prognosis pattern?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "ladder_reviewed": True,
        "focus": "senior_decision",
        "curveball_answer": "A favorable prognosis on LEMG may support observation or early reinnervation surgery. A poor-prognosis pattern -- or a patient who cannot wait for possible recovery -- may favor proceeding directly to injection augmentation or framework medialization rather than deferring treatment on the chance of spontaneous recovery. LEMG results help guide selection and timing among injection laryngoplasty, framework (type I) medialization thyroplasty, and laryngeal reinnervation (e.g., ansa cervicalis-to-recurrent laryngeal nerve transfer).",
    },
    # ---------------------------------------------------------------
    # Laryngocele
    # ---------------------------------------------------------------
    {
        "id": "v463_laryn_cele_fnd",
        "domain": DOMAIN,
        "topic": "Laryngocele",
        "learning_stage": "foundation",
        "stem": "A patient who plays a wind instrument reports a neck mass that enlarges with straining and Valsalva, along with mild hoarseness. What diagnosis should be suspected over a simple lymph node or lipoma, and how is it defined?",
        "choices": [
            "Laryngocele -- an abnormal air-filled dilation of the laryngeal saccule (the appendix of the laryngeal ventricle, between the false and true vocal folds)",
            "A simple reactive lymph node, since Valsalva-related enlargement is a nonspecific finding with no diagnostic significance",
            "A thyroglossal duct cyst, which classically enlarges with Valsalva",
            "A branchial cleft cyst, which is defined as an air-filled dilation of the laryngeal saccule"
        ],
        "answer": 0,
        "explanation": "A neck or laryngeal mass that enlarges with Valsalva, straining, coughing, or playing a wind instrument -- sometimes with hoarseness, cough, globus, or airway symptoms -- suggests a laryngocele rather than a simple lymph node or lipoma. A laryngocele is defined as an abnormal air-filled dilation of the laryngeal saccule, the appendix of the laryngeal ventricle, located between the false and true vocal folds.",
        "why_wrong": [
            "Correct.",
            "Valsalva-related enlargement is a specific and recognized clue pointing toward laryngocele, not a nonspecific or meaningless finding.",
            "Thyroglossal duct cysts are midline neck masses related to thyroid descent, not defined by Valsalva-related enlargement or the laryngeal saccule.",
            "A branchial cleft cyst is a distinct congenital neck lesion; the air-filled saccule definition specifically describes a laryngocele, not a branchial cleft cyst."
        ],
        "board_pearl": "Valsalva- or wind-instrument-related enlargement of a laryngeal/neck mass should raise suspicion for laryngocele rather than a routine lymph node or lipoma.",
        "curveball": "How are internal, external, and combined laryngoceles distinguished anatomically?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngocele",
        "ladder_reviewed": True,
        "focus": "boards",
        "curveball_answer": "Internal laryngocele stays confined within the thyrohyoid membrane in the paraglottic space. External laryngocele herniates through the thyrohyoid membrane (typically via the superior laryngeal neurovascular hiatus) into the neck. Combined (mixed) laryngocele has both components.",
    },
    {
        "id": "v463_laryn_cele_app",
        "domain": DOMAIN,
        "topic": "Laryngocele",
        "learning_stage": "application",
        "stem": "A 60-year-old smoker is found to have what appears to be a straightforward internal laryngocele on laryngoscopy. Before planning marsupialization, what must be done and why?",
        "choices": [
            "Proceed directly to endoscopic marsupialization since the laryngoscopic appearance is classic for laryngocele",
            "Obtain CT of the neck/larynx and direct laryngoscopy with mucosal assessment, because laryngoceles can coexist with an obstructing glottic or supraglottic tumor at the saccule outlet",
            "Obtain only a chest X-ray, since laryngoceles are not associated with any occult malignancy",
            "Defer all imaging and treat empirically with antireflux therapy first"
        ],
        "answer": 1,
        "explanation": "CT of the neck/larynx is essential and should be obtained before treating the mass as benign. Laryngoceles coexist with an obstructing glottic or supraglottic squamous cell carcinoma at the saccule outlet in a clinically meaningful minority of cases, so imaging plus direct laryngoscopy with mucosal assessment must actively exclude an underlying tumor rather than assume the mass is purely a laryngocele.",
        "why_wrong": [
            "Proceeding straight to marsupialization based on appearance alone skips the required step of excluding an underlying tumor.",
            "Correct.",
            "Laryngoceles are specifically associated with occult obstructing tumors at the saccule outlet, and a chest X-ray does not evaluate the larynx for this.",
            "Antireflux therapy does not address the key diagnostic requirement here, which is excluding malignancy before treating the mass as benign."
        ],
        "board_pearl": "Never work up a laryngocele in isolation from the cancer question -- imaging plus laryngoscopy to exclude malignancy comes before marsupialization or excision, not after.",
        "curveball": "If imaging and laryngoscopy instead confirm an associated laryngeal malignancy at the saccule outlet, how does that change management of the laryngocele itself?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngocele",
        "ladder_reviewed": True,
        "focus": "OR_prep",
        "curveball_answer": "Any laryngocele found in association with a laryngeal malignancy is treated according to the cancer, rather than being managed as an isolated benign saccular lesion.",
    },
    {
        "id": "v463_laryn_cele_snr",
        "domain": DOMAIN,
        "topic": "Laryngocele",
        "learning_stage": "senior_decision",
        "stem": "A patient has a combined (mixed) laryngocele with both an internal paraglottic component and a component herniating through the thyrohyoid membrane into the neck. It is symptomatic and enlarging. As the senior surgeon planning the operation, what approach is required and why?",
        "choices": [
            "Endoscopic marsupialization alone, since this technique reliably addresses both internal and external components",
            "Observation only, since combined laryngoceles are managed identically to small asymptomatic internal laryngoceles",
            "Open excision through the thyrohyoid membrane via a lateral neck approach, because the external component is not reliably addressed endoscopically",
            "No treatment is possible for combined laryngoceles regardless of symptoms"
        ],
        "answer": 2,
        "explanation": "External and combined laryngoceles typically require open excision through the thyrohyoid membrane via a lateral neck approach, since the external component is not reliably addressed endoscopically. Endoscopic marsupialization is standard for internal laryngoceles alone. Symptomatic, enlarging, or airway-threatening laryngoceles warrant intervention rather than observation.",
        "why_wrong": [
            "Endoscopic marsupialization is standard for internal laryngoceles, but it does not reliably address the external component of a combined laryngocele.",
            "Observation is appropriate for small, asymptomatic internal laryngoceles, not for a symptomatic, enlarging combined laryngocele.",
            "Correct.",
            "Combined laryngoceles are treatable; symptomatic or enlarging lesions warrant intervention, typically open excision for the external component."
        ],
        "board_pearl": "The external component of an external or combined laryngocele is not reliably addressed endoscopically -- plan an open approach through the thyrohyoid membrane for these.",
        "curveball": "Before finalizing this operative plan, what must already have been excluded, and why does that sequencing matter?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-laryngology-voice-swallowing-laryngocele",
        "ladder_reviewed": True,
        "focus": "senior_decision",
        "curveball_answer": "An underlying obstructing glottic or supraglottic tumor at the saccule outlet must already have been excluded by imaging (CT of the neck/larynx) and direct laryngoscopy with mucosal assessment. This sequencing matters because a laryngocele can be the presenting sign of malignancy, and any laryngocele found in association with a laryngeal malignancy is treated according to the cancer rather than with routine marsupialization or excision.",
    },
]


def apply_deep_curriculum_ladder_laryngology_v463(data_module, app_module=None):
    existing = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(existing, list):
        raise RuntimeError("v46.3: CLINICAL_CHALLENGES_V119 unavailable")
    existing_ids = {q.get("id") for q in existing}
    added = 0
    cases = list(existing)
    for q in NEW_QUESTIONS:
        if q["id"] in existing_ids:
            raise RuntimeError(f"v46.3: duplicate id {q['id']!r}")
        cases.append(q)
        added += 1
    data_module.CLINICAL_CHALLENGES_V119 = cases
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {"questions_added": added}
