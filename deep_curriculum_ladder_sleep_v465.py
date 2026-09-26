"""ENT Mastery v46.5 -- Learning-ladder gapfill: Sleep Surgery.

Adds foundation/application/senior_decision Clinical Challenge vignettes for
the 3 Sleep Surgery topics flagged by audit_domain_ladder_inventory_v217.py as
having no deliberately-reviewed ladder row (recently-added topics that never
got this pass). Grounded in each topic's existing Deep Curriculum content --
no new clinical facts or numbers introduced beyond what that content already
states.
"""
from copy import deepcopy

DOMAIN = "Sleep Surgery"

NEW_QUESTIONS = [   {   'id': 'v465_sleep_nasalcpap_fnd',
        'domain': 'Sleep Surgery',
        'topic': 'Nasal Surgery as a CPAP-Adherence Adjunct',
        'stem': 'A patient with OSA on CPAP reports needing a high pressure setting, frequent '
                'mouth leak, and dry-mouth discomfort each morning. Nasal endoscopy shows a '
                'deviated septum and inferior turbinate hypertrophy. What is the best framework '
                'for considering nasal surgery in this patient?',
        'choices': [   'Nasal surgery is offered as an adjunct to improve CPAP tolerance and '
                       'adherence, not as a stand-alone cure for OSA',
                       'Nasal surgery is expected to normalize the AHI on its own and can replace '
                       'PAP therapy',
                       'Nasal obstruction is irrelevant to CPAP tolerance and should not change '
                       'the treatment plan',
                       'Nasal surgery should be withheld until the patient has already abandoned '
                       'CPAP entirely'],
        'answer': 0,
        'explanation': 'Elevated nasal resistance increases the work of breathing against a CPAP '
                       'circuit and promotes mouth leak and pressure intolerance. Correcting the '
                       'site of nasal obstruction (septum, turbinates, or nasal valve) can lower '
                       'the required therapeutic pressure and improve subjective tolerance and '
                       'nightly usage hours, but it does not by itself normalize the AHI. It is '
                       'best understood as an adherence adjunct.',
        'why_wrong': [   'Correct.',
                         'Septoplasty, turbinate reduction, and nasal valve surgery rarely '
                         'normalize the AHI by themselves and do not substitute for PAP therapy.',
                         'Elevated nasal resistance is precisely what increases work of breathing '
                         'against a CPAP circuit and drives mouth leak and pressure intolerance -- '
                         'it is directly relevant.',
                         'Addressing a contributing, correctable cause of CPAP intolerance while '
                         'the patient is still engaged with therapy is preferable to waiting until '
                         'adherence has already failed.'],
        'board_pearl': 'This is an adherence adjunct, not a stand-alone OSA treatment -- measure '
                       'success in CPAP usage hours per night and tolerated pressure, not in AHI '
                       'reduction from the nasal surgery alone.',
        'curveball': 'What two specific bedside/office maneuvers help localize which nasal site is '
                     "contributing to this patient's obstruction?",
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-sleep-surgery-nasal-surgery-as-a-cpap-adherence-adjunct',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        'curveball_answer': 'Nasal endoscopy assesses the valve, septum, and turbinates directly, '
                            'and the Cottle maneuver screens specifically for nasal valve '
                            'collapse. Both help determine whether the internal/external nasal '
                            'valve, the septum, or the turbinates is the correctable site before '
                            'choosing the corrective procedure.'},
    {   'id': 'v465_sleep_nasalcpap_app',
        'domain': 'Sleep Surgery',
        'topic': 'Nasal Surgery as a CPAP-Adherence Adjunct',
        'stem': "A patient with OSA is referred for 'CPAP failure.' History reveals the mask fits "
                'well and there is no claustrophobia, but the patient cites a very high required '
                'pressure, frequent mouth leak, and poor nightly usage. On exam, a positive Cottle '
                'maneuver is noted with visible internal nasal valve collapse. Which next step '
                'best confirms that nasal obstruction is plausibly driving this adherence problem '
                'before proceeding to surgery?',
        'choices': [   'Proceed directly to functional nasal valve surgery without reviewing any '
                       'CPAP usage data',
                       "Correlate exam findings with the patient's own CPAP titration data "
                       '(therapeutic pressure required, residual leak, nightly usage hours) to '
                       'confirm nasal obstruction is a plausible contributor rather than another '
                       'cause',
                       'Assume mask fit is the cause and reorder a different mask style only',
                       'Discontinue CPAP entirely before any further workup'],
        'answer': 1,
        'explanation': 'The workup for CPAP intolerance thought to be nasal in origin requires '
                       'correlating nasal endoscopy and Cottle maneuver findings with the '
                       "patient's actual CPAP titration data -- pressure required, leak, and usage "
                       'hours -- to confirm that nasal obstruction, rather than mask fit or '
                       'unrelated pressure intolerance, is the plausible driver before committing '
                       'to surgery.',
        'why_wrong': [   "Skipping correlation with the patient's own titration data risks "
                         "operating on a positive exam finding that isn't actually the cause of "
                         "this patient's adherence problem.",
                         'Correct.',
                         'The history and exam here (positive Cottle maneuver, valve collapse) '
                         'already point toward a nasal contributor, so mask fit alone should not '
                         'be assumed without correlating the objective CPAP data.',
                         "Discontinuing therapy abandons the patient's OSA treatment rather than "
                         'addressing a correctable contributor to intolerance.'],
        'board_pearl': 'A positive exam finding is not enough on its own -- confirm it against the '
                       "patient's actual CPAP pressure, leak, and usage data before attributing "
                       'intolerance to the nose.',
        'curveball': "If this patient's positive Cottle maneuver is the dominant finding, which "
                     'corrective procedure is specifically indicated in addition to standard '
                     'septal/turbinate work?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'OR_prep',
        'concept_id': 'v6-sleep-surgery-nasal-surgery-as-a-cpap-adherence-adjunct',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        'curveball_answer': 'A functional nasal valve procedure is added when a positive Cottle '
                            'maneuver or endoscopic collapse identifies the valve as a '
                            'contributing site, alongside standard septoplasty and inferior '
                            'turbinate reduction technique as indicated.'},
    {   'id': 'v465_sleep_nasalcpap_snr',
        'domain': 'Sleep Surgery',
        'topic': 'Nasal Surgery as a CPAP-Adherence Adjunct',
        'stem': 'After successful septoplasty, turbinate reduction, and nasal valve repair, a '
                "patient's CPAP-required pressure drops and nightly mask tolerance clearly "
                'improves, but a repeat sleep study still shows a persistently elevated AHI. The '
                "patient asks whether the nasal surgery 'didn't work' and whether it should be "
                'repeated. What is the best senior-level response?',
        'choices': [   'Conclude that PAP therapy should be abandoned since surgery did not fix '
                       'the AHI',
                       'Tell the patient the nasal surgery failed because the AHI did not '
                       'normalize and plan to repeat the same nasal procedure',
                       'Explain that the nasal surgery achieved its actual goal -- improving CPAP '
                       'tolerance and lowering required pressure -- and that AHI reduction was '
                       'never the expected endpoint of the nasal procedure itself; continue to '
                       'optimize PAP therapy',
                       'Attribute the persistent AHI to a technical error in the nasal surgery '
                       'without further evaluation'],
        'answer': 2,
        'explanation': "The classic teaching error is conflating nasal surgery's adherence-adjunct "
                       'goal with an OSA-cure goal. Success here is measured in CPAP usage hours '
                       'and tolerated pressure, which did improve; the nasal procedure was never '
                       'expected to normalize the AHI on its own, since it treats only nasal '
                       'resistance and not the airway collapse sites responsible for obstructive '
                       'events during sleep.',
        'why_wrong': [   'PAP therapy is now better tolerated and at a lower pressure; that is an '
                         'improvement in the treatment plan, not a reason to abandon it.',
                         'Persistent AHI elevation does not indicate the nasal surgery failed at '
                         'its actual purpose -- it was never intended to resolve the AHI by '
                         'itself.',
                         'Correct.',
                         'Attributing the unchanged AHI to a technical nasal surgical error '
                         'without evaluation misidentifies the entire premise of what the nasal '
                         'procedure treats.'],
        'board_pearl': 'Boards/chief framework: this is an adherence adjunct, not a stand-alone '
                       'OSA treatment -- conflating nasal-surgery success with AHI reduction is '
                       'the classic teaching error to avoid.',
        'curveball': 'Historically, what was the original teaching-point rationale for even '
                     'considering nasal surgery in an OSA patient who was already an established '
                     'CPAP user?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'postoperative_call',
        'concept_id': 'v6-sleep-surgery-nasal-surgery-as-a-cpap-adherence-adjunct',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        'curveball_answer': 'The rationale is that elevated nasal resistance increases the work of '
                            'breathing against the CPAP circuit and promotes mouth leak and '
                            'pressure intolerance -- correcting the obstructive site was expected '
                            'to make the mechanically necessary pressure easier to deliver and '
                            'tolerate, not to treat the underlying collapse causing OSA itself.'},
    {   'id': 'v465_sleep_epiglottopexy_fnd',
        'domain': 'Sleep Surgery',
        'topic': 'Adult Epiglottic Collapse / Epiglottopexy',
        'stem': "An adult labeled a 'CPAP failure' and 'surgery-refractory' has a normal awake "
                'flexible laryngoscopy exam. Drug-induced sleep endoscopy (DISE) reveals posterior '
                'prolapse of the epiglottis against the posterior pharyngeal wall. What does this '
                'finding represent?',
        'choices': [   'An artifact of the DISE procedure that should be disregarded',
                       'A normal anatomic variant that does not contribute to airway obstruction',
                       "Evidence that the patient's obstruction must be exclusively velar in "
                       'origin',
                       'Epiglottic collapse, a dynamic, sleep-state-dependent obstruction site '
                       'that is easy to miss on awake exam and is classified within the epiglottis '
                       'component of the VOTE DISE system'],
        'answer': 3,
        'explanation': 'During sleep, negative inspiratory pressure can cause the epiglottis '
                       'itself to fold posteriorly, obstructing the laryngeal inlet independent of '
                       'or in combination with other collapse sites. This is the epiglottis '
                       'component of the VOTE (velum, oropharynx, tongue base, epiglottis) DISE '
                       'classification, and it is a dynamic finding not reliably reproduced on '
                       'awake exam.',
        'why_wrong': [   'DISE is the recognized diagnostic tool specifically because this '
                         'dynamic, sleep-state-dependent finding is not reliably seen on awake '
                         'exam; it is not an artifact to dismiss.',
                         'Posterior epiglottic prolapse against the pharyngeal wall during DISE is '
                         'an obstruction site, not an incidental variant.',
                         'Epiglottic collapse can occur independent of, or in combination with, '
                         'velar collapse -- it does not by itself confirm the velum as the source.',
                         'Correct.'],
        'board_pearl': 'Do not assume palate or tongue-base collapse explains every case of '
                       'surgical or CPAP failure -- DISE-confirmed epiglottic collapse is a '
                       'distinct, correctable obstruction pattern that changes the operative plan.',
        'curveball': 'Why is awake flexible laryngoscopy insufficient to reliably identify this '
                     'finding?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-sleep-surgery-adult-epiglottic-collapse-epiglottopexy',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        'curveball_answer': 'Epiglottic collapse is a dynamic, sleep-state-dependent phenomenon '
                            'driven by negative inspiratory pressure during sleep; it is not '
                            'reliably reproduced in the awake state, which is exactly why DISE -- '
                            'performed under sedation approximating the sleep state -- is the key '
                            'diagnostic tool for identifying it.'},
    {   'id': 'v465_sleep_epiglottopexy_app',
        'domain': 'Sleep Surgery',
        'topic': 'Adult Epiglottic Collapse / Epiglottopexy',
        'stem': 'A patient with OSA has failed PAP therapy and has already undergone palate '
                'surgery without improvement. DISE now shows the epiglottis is the major '
                'contributing site of obstruction, with mild residual tongue-base collapse also '
                'noted. What is the most appropriate next management step?',
        'choices': [   'Surgical correction targeting the epiglottis (such as epiglottopexy or '
                       'partial epiglottectomy), generally alongside treatment of the other '
                       'DISE-identified obstruction site for best results',
                       'Repeat the same palate surgery a second time since the epiglottis is not a '
                       'treatable site',
                       'Declare the patient untreatable and offer no further surgical options',
                       'Proceed to epiglottis surgery alone while deliberately ignoring the '
                       'tongue-base finding on DISE'],
        'answer': 0,
        'explanation': 'When epiglottic collapse is a major or sole contributor and PAP therapy or '
                       'other measures fail or are not tolerated, surgical correction targeting '
                       'the epiglottis is considered. Epiglottopexy (suturing the epiglottis '
                       'anteriorly to the tongue base or vallecula) or partial epiglottectomy are '
                       'the established options, generally combined with treatment of other '
                       'DISE-identified obstruction sites for best results.',
        'why_wrong': [   'Correct.',
                         'The epiglottis is a recognized, distinct, correctable obstruction site; '
                         'repeating palate surgery does not address it.',
                         'A DISE-identified, correctable obstruction pattern with an established '
                         'surgical option (epiglottopexy or partial epiglottectomy) means the '
                         'patient is not untreatable.',
                         'Treating only the epiglottis while deliberately disregarding a '
                         'co-identified obstruction site on the same DISE contradicts the '
                         'principle of treating all DISE-identified sites for best results.'],
        'board_pearl': 'Epiglottopexy anteriorly sutures the epiglottis to the tongue base or '
                       'vallecula specifically to prevent posterior prolapse -- know this '
                       'mechanism when choosing it over partial epiglottectomy.',
        'curveball': 'What exam/workup limitation makes it likely that this epiglottic '
                     'contribution would have been missed before DISE was performed?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'OR_prep',
        'concept_id': 'v6-sleep-surgery-adult-epiglottic-collapse-epiglottopexy',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        'curveball_answer': 'Epiglottic collapse is a dynamic, sleep-state-dependent finding that '
                            'is not reliably reproduced on awake flexible laryngoscopy, so a '
                            'patient can have a normal-appearing awake exam and still be missed '
                            "and mislabeled as a 'CPAP failure' or 'surgery-refractory' case "
                            'without DISE.'},
    {   'id': 'v465_sleep_epiglottopexy_snr',
        'domain': 'Sleep Surgery',
        'topic': 'Adult Epiglottic Collapse / Epiglottopexy',
        'stem': 'A patient who failed CPAP underwent palate and tongue-base procedures with only '
                'partial improvement in symptoms. He is now referred for consideration of '
                'epiglottopexy. How should its role relative to other sleep-surgery options be '
                'framed for this patient?',
        'choices': [   'Epiglottopexy should be offered automatically to every patient who fails '
                       'palate and tongue-base surgery, regardless of DISE findings',
                       'Epiglottopexy is targeted specifically at epiglottis-driven obstruction '
                       'identified on DISE; it is indicated when the epiglottis is a distinct or '
                       'contributing collapse site, not as a generic salvage procedure to try '
                       'after other surgeries have failed without re-confirming the epiglottis is '
                       'actually involved',
                       'Epiglottopexy replaces the need for DISE entirely in surgical failures',
                       'Epiglottopexy is contraindicated in any patient who has already had other '
                       'sleep surgery'],
        'answer': 1,
        'explanation': "Epiglottopexy's role is defined by DISE-confirmed epiglottic collapse as a "
                       'distinct or contributing obstruction site -- it is not a reflexive next '
                       'step after failure of palate/tongue-base surgery. The senior-level '
                       'decision is to re-evaluate with DISE to confirm the epiglottis is actually '
                       'contributing before choosing this procedure, rather than assuming its role '
                       'based on prior surgical failure alone.',
        'why_wrong': [   'Offering epiglottopexy without re-confirming epiglottic involvement on '
                         'DISE ignores that its indication is specifically DISE-identified '
                         'epiglottic collapse, not simply prior surgical failure.',
                         'Correct.',
                         'DISE remains the key diagnostic tool for identifying epiglottic '
                         'collapse; epiglottopexy is a treatment for a DISE-identified finding, '
                         'not a substitute for the diagnostic step itself.',
                         'Prior sleep surgery at other sites does not contraindicate '
                         'epiglottopexy; the epiglottis can be a distinct or contributing site '
                         'independent of, or in combination with, other collapse patterns.'],
        'board_pearl': 'Boards/chief framework: do not assume palate or tongue-base collapse '
                       'explains every case of surgical or CPAP failure -- re-confirm with DISE '
                       'before choosing epiglottopexy, since its role is tied to a DISE-identified '
                       'finding, not to failure of other procedures alone.',
        'curveball': 'If DISE in this patient shows epiglottic collapse together with persistent '
                     'tongue-base collapse, how should the operative plan be framed?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'postoperative_call',
        'concept_id': 'v6-sleep-surgery-adult-epiglottic-collapse-epiglottopexy',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        'curveball_answer': 'Surgical correction should target the epiglottis (epiglottopexy or '
                            'partial epiglottectomy) alongside treatment of the other '
                            'DISE-identified obstruction site -- here, the persistent tongue-base '
                            'collapse -- since combined treatment of all identified sites gives '
                            'the best results rather than treating the epiglottis in isolation.'},
    {   'id': 'v465_sleep_trach_fnd',
        'domain': 'Sleep Surgery',
        'topic': 'Tracheostomy as Definitive OSA Therapy',
        'stem': 'A patient with severe OSA and life-threatening cardiopulmonary complications '
                '(severe hypoxemia, cor pulmonale, refractory arrhythmia) has failed or cannot '
                'tolerate CPAP/BiPAP and other surgical options. What makes tracheostomy '
                'mechanistically different from every site-specific OSA surgery?',
        'choices': [   'It targets only epiglottic collapse, like epiglottopexy',
                       'It corrects only the nasal component of obstruction, like septoplasty',
                       'It bypasses the entire upper airway obstruction -- nasal, palatal, '
                       'tongue-base, and supraglottic/laryngeal -- below the level of collapse',
                       'It works by increasing pharyngeal muscle tone during sleep'],
        'answer': 2,
        'explanation': 'Unlike any site-specific OSA surgery, which corrects or bypasses '
                       'obstruction at one particular level (nose, palate, tongue base, or '
                       'epiglottis/larynx), tracheostomy bypasses the entire upper airway '
                       'obstruction below the level of collapse. This is why it is considered the '
                       "historical benchmark of 'cure' for OSA.",
        'why_wrong': [   'That describes epiglottopexy, which addresses only epiglottis-driven '
                         'obstruction, not the entire upper airway.',
                         'That describes nasal surgery, which addresses only nasal resistance, not '
                         'the entire upper airway.',
                         'Correct.',
                         'Tracheostomy does not work by any change in pharyngeal muscle tone; it '
                         'works by bypassing the obstructed segment entirely.'],
        'board_pearl': "Know tracheostomy as the historical benchmark of 'cure' against which "
                       'every other OSA intervention is measured, because it bypasses the '
                       'obstruction entirely rather than treating one collapse site.',
        'curveball': "Before CPAP existed, what was tracheostomy's original role in OSA treatment?",
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-sleep-surgery-tracheostomy-as-definitive-osa-therapy',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        'curveball_answer': 'Historically, tracheostomy was the original definitive OSA treatment '
                            'before CPAP existed, and it remains, mechanistically, the single most '
                            'reliably effective intervention because it bypasses the obstruction '
                            'entirely rather than treating one collapse site.'},
    {   'id': 'v465_sleep_trach_app',
        'domain': 'Sleep Surgery',
        'topic': 'Tracheostomy as Definitive OSA Therapy',
        'stem': 'A patient with confirmed severe OSA on polysomnography has documented failure of '
                'PAP therapy and of prior site-specific surgical options. Before proceeding to '
                'tracheostomy, what should the workup specifically confirm?',
        'choices': [   'Nothing further, since severe cardiopulmonary complications alone are '
                       'sufficient to proceed without any additional workup',
                       'Only the polysomnography severity, since prior treatment history and '
                       'stoma-care candidacy are not part of the workup',
                       "Only whether the patient's neck anatomy allows stoma creation, without "
                       'confirming PAP/surgical failure first',
                       'OSA severity by polysomnography, documented failure or intolerance of PAP '
                       'therapy and other surgical options, and candidacy for stoma creation and '
                       'long-term tracheostomy care (neck anatomy, obesity, caregiver support, and '
                       'capacity for ongoing stoma management)'],
        'answer': 3,
        'explanation': 'The workup for tracheostomy as definitive OSA therapy requires confirming '
                       'OSA severity with polysomnography, documenting failure or intolerance of '
                       'PAP therapy and other surgical options, and specifically assessing '
                       'candidacy for stoma creation and long-term tracheostomy care -- including '
                       "neck anatomy, obesity, caregiver support, and the patient's or family's "
                       'capacity for ongoing stoma management.',
        'why_wrong': [   'Even in severe cardiopulmonary disease, the workup should still confirm '
                         'severity, prior treatment failure, and candidacy for long-term stoma '
                         'management before proceeding.',
                         'Documented failure of PAP therapy and other surgical options, and '
                         'candidacy for stoma creation and care, are explicitly part of the '
                         'required workup, not optional additions.',
                         'Confirming OSA severity and documented treatment failure must occur '
                         'alongside, not instead of, assessing stoma-care candidacy.',
                         'Correct.'],
        'board_pearl': 'Tracheostomy candidacy is judged on more than airway severity alone -- '
                       'stoma-care capacity (patient and caregiver) is part of the workup, not an '
                       'afterthought.',
        'curveball': 'What operative strategy allows this patient to preserve daytime speech and '
                     'swallowing while still resolving nocturnal obstruction?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'OR_prep',
        'concept_id': 'v6-sleep-surgery-tracheostomy-as-definitive-osa-therapy',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        'curveball_answer': 'A fenestrated or capped tube worn during the day with nocturnal '
                            'deflation/opening is a common strategy that preserves daytime speech '
                            'and swallowing function while still resolving nocturnal obstruction.'},
    {   'id': 'v465_sleep_trach_snr',
        'domain': 'Sleep Surgery',
        'topic': 'Tracheostomy as Definitive OSA Therapy',
        'stem': 'A patient with severe OSA, cor pulmonale, and refractory arrhythmia has failed '
                'CPAP/BiPAP and other surgical options. A junior resident argues tracheostomy is '
                'now purely of historical interest and should not be offered. How should this be '
                'corrected at the senior-decision level, and what should candidacy assessment '
                'weigh?',
        'choices': [   'Tracheostomy remains a genuinely appropriate option in select severe, '
                       'refractory, high-risk patients today; it is reserved as a last resort '
                       'given quality-of-life burden and stoma-care demands, so candidacy '
                       'assessment must weigh confirmed treatment failure against the '
                       "patient's/family's capacity for long-term stoma management, not dismiss it "
                       'as obsolete',
                       'Agree that tracheostomy is obsolete and should never be offered regardless '
                       'of disease severity',
                       'Offer tracheostomy to any OSA patient regardless of whether PAP or other '
                       'surgical options have been tried',
                       'Offer tracheostomy solely based on cor pulmonale without confirming '
                       'failure of PAP and surgical options'],
        'answer': 0,
        'explanation': 'Tracheostomy is reserved as a last resort today because of its '
                       'quality-of-life burden and stoma-care demands, but it remains a genuinely '
                       'appropriate option in select severe, refractory, high-risk patients -- not '
                       'merely of historical interest. The senior-level decision requires weighing '
                       "documented failure of PAP and other surgical options against the patient's "
                       "and family's capacity for ongoing stoma management before offering it.",
        'why_wrong': [   'Correct.',
                         'The topic explicitly states tracheostomy is not merely of historical '
                         'interest and remains a genuinely appropriate option in select severe, '
                         'refractory, high-risk disease.',
                         'Bypassing confirmed failure of PAP and other surgical options before '
                         'offering the most invasive definitive option skips a required step in '
                         'candidacy assessment.',
                         'Cardiopulmonary severity alone does not substitute for documenting '
                         'failure or intolerance of PAP and prior surgical options, which the '
                         'workup requires.'],
        'board_pearl': 'Know its narrow but real modern indication in severe, refractory, '
                       'high-risk disease -- tracheostomy is the historical benchmark of cure, not '
                       'an obsolete relic.',
        'curveball': 'Why is tracheostomy considered the benchmark against which every other OSA '
                     "intervention's effectiveness is measured?",
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'overnight_call',
        'concept_id': 'v6-sleep-surgery-tracheostomy-as-definitive-osa-therapy',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        'curveball_answer': 'Because it bypasses the obstruction entirely -- nasal, palatal, '
                            'tongue-base, and supraglottic/laryngeal -- below the level of '
                            'collapse, rather than treating one collapse site, it produces '
                            'near-complete resolution of obstructive events when the obstruction '
                            "is bypassed, making it the mechanistic benchmark of 'cure' against "
                            'which site-specific surgeries are compared.'}]


def apply_deep_curriculum_ladder_sleep_v465(data_module, app_module=None):
    existing = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(existing, list):
        raise RuntimeError("v46.5: CLINICAL_CHALLENGES_V119 unavailable")
    existing_ids = {q.get("id") for q in existing}
    added = 0
    cases = list(existing)
    for q in NEW_QUESTIONS:
        if q["id"] in existing_ids:
            raise RuntimeError(f"v46.5: duplicate id {q['id']!r}")
        cases.append(q)
        added += 1
    data_module.CLINICAL_CHALLENGES_V119 = cases
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {"questions_added": added}
