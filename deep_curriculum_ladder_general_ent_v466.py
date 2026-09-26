"""ENT Mastery v46.6 -- Learning-ladder gapfill: General ENT / Emergencies.

Adds foundation/application/senior_decision Clinical Challenge vignettes for
the 3 General ENT / Emergencies topics flagged by
audit_domain_ladder_inventory_v217.py as having no deliberately-reviewed ladder
row (recently-added topics that never got this pass). Grounded in each topic's
existing Deep Curriculum content -- no new clinical facts or numbers introduced
beyond what that content already states.
"""
from copy import deepcopy

DOMAIN = "General ENT / Emergencies"

NEW_QUESTIONS = [   {   'id': 'v466_gent_necktrauma_fnd',
        'domain': 'General ENT / Emergencies',
        'topic': 'Penetrating and Blunt Neck Trauma',
        'stem': 'A young man arrives after a stab wound to the lateral neck. On exam there is '
                'active arterial bleeding from the wound with an expanding hematoma and early '
                'hypotension. He is otherwise following commands. What is the most appropriate '
                'immediate step?',
        'choices': [   'Proceed directly to operative/endovascular management for hemorrhage '
                       'control without a routine imaging delay',
                       'Obtain a CTA of the neck before any other intervention',
                       'Probe the wound at the bedside to identify the bleeding vessel',
                       'Discharge instructions after simple wound closure since he is '
                       'neurologically intact'],
        'answer': 0,
        'explanation': 'Active arterial bleeding, an expanding hematoma, and shock from a neck '
                       'injury are hard signs. Hard signs mandate immediate operative or '
                       'endovascular control rather than routine imaging delay, and the wound '
                       'should never be blindly probed or clamped.',
        'why_wrong': [   'Correct.',
                         'Obtaining imaging first delays control of a hard-sign injury and risks '
                         'exsanguination.',
                         'Blindly probing or clamping a neck wound is explicitly unsafe and can '
                         'worsen vascular or aerodigestive injury.',
                         'Active hemorrhage with an expanding hematoma and shock is a hard sign '
                         'requiring operative control, not discharge.'],
        'board_pearl': 'Hard signs (active arterial bleeding, expanding hematoma, shock, '
                       'bruit/thrill, major airway compromise, air bubbling from the wound, or an '
                       'evolving focal neurologic deficit) go straight to operative or '
                       'endovascular control -- they do not wait for imaging.',
        'curveball': 'The same patient instead has only a nonexpanding hematoma and mild dysphonia '
                     'with stable vital signs. How does the initial step change?',
        'curveball_answer': 'SOFT SIGNS PATHWAY -- a nonexpanding hematoma, dysphonia, dysphagia, '
                            'minor hemoptysis, or subcutaneous emphysema are soft signs. In a '
                            'stable patient, soft signs are worked up with selective CTA based on '
                            'mechanism and findings, with serial examinations, rather than '
                            'mandatory operative exploration.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-penetrating-and-blunt-neck-trauma',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'overnight_call'},
    {   'id': 'v466_gent_necktrauma_app',
        'domain': 'General ENT / Emergencies',
        'topic': 'Penetrating and Blunt Neck Trauma',
        'stem': 'A hemodynamically stable patient sustains a penetrating injury with a trajectory '
                'crossing the cricoid-to-mandibular-angle region. There are no hard signs, but she '
                'reports minor hemoptysis and has subcutaneous emphysema on exam. CTA of the neck '
                'is unremarkable. What is the most appropriate next step?',
        'choices': [   'Clear her for discharge because CTA was negative',
                       'Add contrast evaluation and/or esophagoscopy given the trajectory and soft '
                       'signs, since CTA alone cannot exclude all esophageal injuries',
                       'Proceed to mandatory operative neck exploration based on the zone alone',
                       'Blindly clamp the wound tract to rule out a vascular injury'],
        'answer': 1,
        'explanation': 'Even with a negative CTA, a concerning trajectory plus soft signs '
                       '(hemoptysis, subcutaneous emphysema) should prompt additional evaluation '
                       'for esophageal/aerodigestive injury, because CTA alone cannot exclude all '
                       'esophageal injuries when trajectory, symptoms, air, or CT changes remain '
                       'suspicious.',
        'why_wrong': [   'A negative CTA does not exclude esophageal injury when trajectory and '
                         'symptoms remain concerning; discharge would be premature.',
                         'Correct.',
                         'Stable penetrating trauma is now commonly managed with a selective, '
                         'no-zone pathway rather than mandatory exploration based on zone alone.',
                         'Blind clamping or probing of a neck wound is unsafe and is explicitly '
                         'discouraged regardless of stability.'],
        'board_pearl': 'A negative CTA is reassuring but not definitive for the aerodigestive '
                       'tract -- persistent trajectory concern or soft signs like air or '
                       'hemoptysis warrant contrast study and/or esophagoscopy.',
        'curveball': 'What historical approach to Zone II penetrating injuries has this selective, '
                     'no-zone strategy largely replaced?',
        'curveball_answer': 'The older doctrine of mandatory operative exploration for all Zone II '
                            'penetrating injuries has been replaced, in stable and selected '
                            'patients, by CTA-based observation and serial examination rather than '
                            'routine exploration.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-penetrating-and-blunt-neck-trauma',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'boards'},
    {   'id': 'v466_gent_necktrauma_snr',
        'domain': 'General ENT / Emergencies',
        'topic': 'Penetrating and Blunt Neck Trauma',
        'stem': 'A patient with blunt neck trauma from a steering-wheel injury has stridor, '
                'worsening voice change, and palpable laryngeal crepitus. Suspicion for '
                'laryngotracheal disruption is high. The airway team wants to secure the airway as '
                'quickly as possible. What is the safest immediate airway decision?',
        'choices': [   'Perform reflexive rapid-sequence intubation across the suspected injury',
                       'Delay any airway intervention until CTA is complete',
                       'Use a controlled airway plan with expert surgical backup, avoiding '
                       'reflexive intubation across a suspected laryngotracheal separation',
                       'Perform bedside cricothyrotomy through the suspected zone of disruption as '
                       'the default first step'],
        'answer': 2,
        'explanation': 'When laryngotracheal disruption is suspected, a controlled airway plan '
                       'with expert surgical backup is required, and reflexive intubation across a '
                       'suspected separation is an explicit trap that can convert a partial injury '
                       'into a complete one or lose the airway entirely.',
        'why_wrong': [   'Reflexive intubation across a suspected laryngotracheal separation is an '
                         'explicitly named trap and can worsen the injury or lose the airway.',
                         'Major airway compromise is a hard sign; a threatened airway should not '
                         'wait for imaging to be completed.',
                         'Correct.',
                         'Cricothyrotomy through a disrupted segment is not the default plan; a '
                         'controlled, expert-backed approach with exposure selected by trajectory '
                         'is preferred over blindly instrumenting the injured segment.'],
        'board_pearl': 'Suspected laryngotracheal disruption is an airway emergency that demands a '
                       'controlled plan with surgical backup -- reflexive intubation across the '
                       'injury is a classic senior-level trap.',
        'curveball': 'If this same patient instead has a demonstrated vascular injury with ongoing '
                     'hemorrhage rather than airway disruption, how should the operative exposure '
                     'be chosen?',
        'curveball_answer': 'OPERATIVE EXPOSURE -- obtain proximal and distal vascular control '
                            'when possible, and select the surgical exposure based on the injury '
                            'trajectory rather than simply enlarging the contaminated entry wound; '
                            'inspect and repair or drain associated pharyngeal, esophageal, and '
                            'airway injuries at the same time.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-penetrating-and-blunt-neck-trauma',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'OR_prep'},
    {   'id': 'v466_gent_necfasc_fnd',
        'domain': 'General ENT / Emergencies',
        'topic': 'Cervical Necrotizing Fasciitis',
        'stem': 'A patient develops rapidly progressive neck swelling and pain out of proportion '
                'to exam a few days after a dental infection, along with systemic toxicity and '
                'skin duskiness. What should this presentation immediately raise concern for?',
        'choices': [   'Simple cellulitis that will respond to oral antibiotics alone',
                       'An allergic reaction to a recent dental medication',
                       'A benign reactive lymph node requiring only observation',
                       'Cervical necrotizing fasciitis requiring urgent evaluation'],
        'answer': 3,
        'explanation': 'Rapidly progressive neck pain or swelling, systemic toxicity, pain out of '
                       'proportion, skin duskiness, bullae, or crepitus after an odontogenic or '
                       'pharyngeal infection should trigger immediate concern for cervical '
                       'necrotizing fasciitis.',
        'why_wrong': [   'Simple cellulitis does not typically produce systemic toxicity, pain out '
                         'of proportion, or skin duskiness; these are red flags for a deeper '
                         'necrotizing process.',
                         'An allergic reaction does not produce pain out of proportion or skin '
                         'duskiness in this pattern; the described findings point to a necrotizing '
                         'soft-tissue infection.',
                         'A reactive node would not explain systemic toxicity, pain out of '
                         'proportion, or skin duskiness.',
                         'Correct.'],
        'board_pearl': 'Pain out of proportion to exam, systemic toxicity, and skin duskiness '
                       'after an odontogenic/pharyngeal source are the classic tip-off for '
                       "cervical necrotizing fasciitis -- do not anchor on 'just cellulitis.'",
        'curveball': 'If crepitus is absent on exam, does that make necrotizing fasciitis less '
                     'likely?',
        'curveball_answer': 'No -- this is a clinical diagnosis, and gas may be absent even when '
                            'necrotizing fasciitis is present; absence of crepitus or gas on '
                            'imaging should not be used to exclude the diagnosis when the clinical '
                            'picture (rapid progression, toxicity, pain out of proportion) is '
                            'concerning.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-cervical-necrotizing-fasciitis',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'overnight_call'},
    {   'id': 'v466_gent_necfasc_app',
        'domain': 'General ENT / Emergencies',
        'topic': 'Cervical Necrotizing Fasciitis',
        'stem': 'A patient with rapidly progressive neck swelling, systemic toxicity, and pain out '
                'of proportion is being evaluated. A contrast CT of the neck and chest is obtained '
                'because she is currently stable. No gas is seen on the scan, and there is no '
                'discrete drainable abscess. How should this finding be interpreted?',
        'choices': [   'This remains a clinical diagnosis; a reassuring or gas-negative scan '
                       'should not be used to wait for a discrete abscess before pursuing '
                       'operative source control',
                       'A reassuring scan without gas or a discrete abscess excludes necrotizing '
                       'fasciitis and supports outpatient antibiotics',
                       'The absence of gas means this is simple cellulitis and antibiotics alone '
                       'are curative',
                       'CT should be repeated in 48 hours before making any management decision'],
        'answer': 0,
        'explanation': 'Cervical necrotizing fasciitis is a clinical diagnosis. CT (when the '
                       'patient is stable) helps map extent, including danger-space/mediastinal '
                       'extension, without delaying source control -- but gas may be absent, and '
                       'clinicians should not wait for a discrete abscess or a reassuring scan '
                       'before moving to operative debridement when the clinical picture is '
                       'concerning.',
        'why_wrong': [   'Correct.',
                         'A gas-negative or reassuring scan does not exclude the diagnosis; '
                         'waiting for a discrete abscess or reassuring imaging risks a lethal '
                         'delay.',
                         'Antibiotics cannot replace debridement in necrotizing fasciitis; they '
                         'are adjunctive, not curative, once the diagnosis is suspected.',
                         'Repeating CT in 48 hours introduces exactly the kind of delay that rapid '
                         'progression plus toxicity makes dangerous.'],
        'board_pearl': 'CT maps extent (including possible mediastinal spread) in a stable '
                       'patient, but it is a clinical diagnosis -- do not let a gas-negative or '
                       'abscess-negative scan delay operative source control.',
        'curveball': 'How does this discrimination differ from working up a patient who instead '
                     'has a well-localized, fluctuant neck abscess without systemic toxicity or '
                     'rapid progression?',
        'curveball_answer': 'A localized fluctuant abscess without toxicity or rapid progression '
                            'is managed by drainage of that discrete collection with targeted '
                            'antibiotics; cervical necrotizing fasciitis, by contrast, presents '
                            'with rapid progression, systemic toxicity, and pain out of '
                            'proportion, spreads along fascial planes with thrombosis of small '
                            'vessels, and requires immediate wide debridement rather than drainage '
                            'of a single collection.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-cervical-necrotizing-fasciitis',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'boards'},
    {   'id': 'v466_gent_necfasc_snr',
        'domain': 'General ENT / Emergencies',
        'topic': 'Cervical Necrotizing Fasciitis',
        'stem': 'A patient with suspected cervical necrotizing fasciitis is being resuscitated, '
                'has broad-spectrum antibiotics started, and the airway is being secured. The '
                'surgical team is deciding on timing of debridement while imaging is still '
                'pending. What is the correct senior-level decision?',
        'choices': [   'Wait for imaging results before mobilizing the operating room, since '
                       'antibiotics have already been started',
                       'Proceed to immediate wide debridement to viable, bleeding tissue with '
                       'drainage of all involved spaces, without waiting for a discrete abscess or '
                       'a completed scan',
                       'Manage medically with antibiotics and ICU support alone, reserving surgery '
                       'only if the patient deteriorates further',
                       'Perform a small incisional biopsy only, then wait for pathology before '
                       'deciding on debridement extent'],
        'answer': 1,
        'explanation': 'Antibiotics cannot replace debridement. Once the clinical picture is '
                       'concerning, the correct decision is immediate wide surgical debridement to '
                       'viable, bleeding tissue with drainage of all involved spaces and a plan '
                       'for serial re-exploration, rather than waiting for a scan or a discrete '
                       'abscess to declare itself.',
        'why_wrong': [   'Delaying the OR for imaging sacrifices time in a disease where delay to '
                         'source control is lethal; labs and cultures should be drawn while '
                         'mobilizing the OR, not instead of it.',
                         'Correct.',
                         'Antibiotics and ICU support are necessary adjuncts, but they cannot '
                         'replace debridement in necrotizing fasciitis.',
                         'A limited biopsy delays definitive source control; the correct approach '
                         'is immediate wide debridement, not a staged diagnostic incision.'],
        'board_pearl': 'Do not wait for a discrete abscess or a reassuring scan -- rapid '
                       'progression plus systemic toxicity makes delay to operative source control '
                       'lethal, and debridement must be wide with planned serial re-exploration.',
        'curveball': 'If intraoperative or CT findings suggest extension into the danger space '
                     'toward the mediastinum, how should the operative plan change?',
        'curveball_answer': 'Thoracic extension (for example, descending necrotizing mediastinitis '
                            'via danger-space spread) requires an early thoracic-surgery drainage '
                            'strategy in addition to cervical debridement, rather than treating '
                            'the neck in isolation.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-cervical-necrotizing-fasciitis',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'OR_prep'},
    {   'id': 'v466_gent_fb_fnd',
        'domain': 'General ENT / Emergencies',
        'topic': 'Ear and Nasal Foreign Body Removal',
        'stem': 'A toddler is brought in with witnessed insertion of a small object into the nose, '
                'followed by unilateral foul rhinorrhea. Anterior rhinoscopy confirms a visible '
                'foreign body. What is the guiding principle for the removal attempt?',
        'choices': [   'Attempt removal repeatedly with whatever instrument is on hand until it '
                       'comes out',
                       'Irrigate the nose immediately regardless of the object type',
                       'The safest first attempt is the best attempt -- choose the tool by the '
                       "object's shape before proceeding",
                       'Delay any attempt until formal imaging is obtained'],
        'answer': 2,
        'explanation': 'The safest first attempt is the best attempt: match the technique to the '
                       "object's geometry (forceps for graspable objects, hook/curette or balloon "
                       'behind smooth objects, suction when suitable, or positive pressure for '
                       'selected nasal cases) rather than repeatedly retrying with a mismatched '
                       'tool.',
        'why_wrong': [   'Repeated mismatched attempts increase trauma and reduce the chance of a '
                         'safe first removal.',
                         'Irrigation is not a default first step and is unsafe for certain objects '
                         '(batteries, swelling organic material, or suspected tympanic '
                         'perforation).',
                         'Correct.',
                         'Imaging is selective and must not delay removal, particularly for '
                         'tissue-destructive objects like batteries.'],
        'board_pearl': 'For foreign bodies, the first attempt should be the best attempt -- pick '
                       "the right tool for the object's shape rather than repeatedly probing with "
                       'the wrong one.',
        'curveball': 'What single feature of the object, if present, changes this from a routine '
                     'removal into an emergency requiring immediate action?',
        'curveball_answer': 'A button battery (or paired high-powered magnets) changes the '
                            'calculus: these are tissue-destructive emergencies -- batteries '
                            'generate alkaline electrical injury and magnets compress tissue -- '
                            'and should be removed immediately rather than managed as a routine, '
                            'unhurried foreign-body case.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-ear-and-nasal-foreign-body-removal',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'overnight_call'},
    {   'id': 'v466_gent_fb_app',
        'domain': 'General ENT / Emergencies',
        'topic': 'Ear and Nasal Foreign Body Removal',
        'stem': 'A child has a disc-shaped object lodged in the nasal cavity, confirmed on exam to '
                'be a button battery. The family asks whether the object can simply be observed '
                'until it passes or removed electively in clinic later this week. What is the '
                'correct response?',
        'choices': [   'Observation is reasonable since most nasal foreign bodies pass '
                       'spontaneously',
                       'Elective removal in clinic in a few days is acceptable since the child is '
                       'currently asymptomatic',
                       'Irrigate the nose first to try to flush the battery out before considering '
                       'other options',
                       'The battery must be removed immediately because it is tissue-destructive, '
                       'and irrigation should be avoided'],
        'answer': 3,
        'explanation': 'Button batteries are explicitly called out as tissue-destructive '
                       'emergencies causing alkaline electrical injury, and must be removed '
                       'immediately regardless of symptoms. Irrigation is specifically avoided for '
                       'batteries. Imaging or delay must not postpone battery removal.',
        'why_wrong': [   'Observation is not appropriate for a battery; ongoing electrical injury '
                         'continues even without current symptoms.',
                         'Elective delay risks worsening tissue injury; batteries require '
                         'immediate removal, not scheduled outpatient removal.',
                         'Irrigation is explicitly avoided for batteries because it does not stop, '
                         'and may worsen, the electrical injury process.',
                         'Correct.'],
        'board_pearl': 'Discriminate battery/magnet foreign bodies from ordinary organic or inert '
                       'objects early -- batteries and paired magnets are tissue-destructive and '
                       'demand immediate removal, with irrigation avoided.',
        'curveball': 'If the object were instead a piece of swelling organic material (such as a '
                     'bean) rather than a battery, would irrigation be an appropriate technique?',
        'curveball_answer': 'No -- irrigation is also avoided for swelling organic material (it '
                            'can cause further swelling and impaction), as well as for suspected '
                            'tympanic membrane perforation; technique should still be matched to '
                            'object type rather than defaulting to irrigation.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-ear-and-nasal-foreign-body-removal',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'boards'},
    {   'id': 'v466_gent_fb_snr',
        'domain': 'General ENT / Emergencies',
        'topic': 'Ear and Nasal Foreign Body Removal',
        'stem': 'A young child has a deeply impacted aural foreign body adjacent to the tympanic '
                'membrane. Two prior bedside attempts by another provider have failed and the '
                'child is now uncooperative and distressed. What is the appropriate senior-level '
                'decision?',
        'choices': [   'Proceed to controlled microscopic/endoscopic removal with sedation or '
                       'anesthesia given failed attempts, poor cooperation, and proximity to a '
                       'critical structure',
                       'Continue repeated bedside attempts with progressively more force until the '
                       'object is retrieved',
                       'Declare the object unretrievable and refer for outpatient follow-up in '
                       'several weeks',
                       'Attempt irrigation to flush the object out despite its proximity to the '
                       'tympanic membrane'],
        'answer': 0,
        'explanation': 'Deep/impacted objects, poor cooperation, adjacent critical structures '
                       '(like the tympanic membrane), and failed prior attempts are each named '
                       'indications to move to controlled microscopic or endoscopic removal with '
                       'sedation or anesthesia, limiting further traumatic bedside retries.',
        'why_wrong': [   'Correct.',
                         'Repeated forceful bedside attempts in an uncooperative child near the '
                         'tympanic membrane risk traumatic injury and are explicitly discouraged.',
                         'This is not an unretrievable or low-urgency situation; a foreign body '
                         'adjacent to the tympanic membrane in a distressed child should prompt '
                         'escalation to controlled removal, not open-ended delay.',
                         'Irrigation is not favored when there is risk to tympanic membrane '
                         'integrity; safety of the technique for the specific site and material '
                         'must be confirmed first.'],
        'board_pearl': 'Failed attempts, poor cooperation, depth/impaction, or proximity to '
                       'critical structures (like the TM) are the senior-level triggers to move '
                       'from bedside retrieval to controlled sedated/anesthetized removal -- limit '
                       'traumatic retries.',
        'curveball': 'After removal under controlled conditions, what should be done before '
                     'considering the case complete?',
        'curveball_answer': 'Re-examine the ear (or nose) afterward for injury or retained '
                            'fragments -- removal alone is not the endpoint; confirming there is '
                            'no residual trauma or leftover material is part of safe completion of '
                            'the case.',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-general-ent-emergencies-ear-and-nasal-foreign-body-removal',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        '_coverage_reviewed_v211': True,
        'focus': 'OR_prep'}]


def apply_deep_curriculum_ladder_general_ent_v466(data_module, app_module=None):
    existing = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(existing, list):
        raise RuntimeError("v46.6: CLINICAL_CHALLENGES_V119 unavailable")
    existing_ids = {q.get("id") for q in existing}
    added = 0
    cases = list(existing)
    for q in NEW_QUESTIONS:
        if q["id"] in existing_ids:
            raise RuntimeError(f"v46.6: duplicate id {q['id']!r}")
        cases.append(q)
        added += 1
    data_module.CLINICAL_CHALLENGES_V119 = cases
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {"questions_added": added}
