"""ENT Mastery v46.1 -- Learning-ladder gapfill: Thyroid / Parathyroid / Salivary.

Adds foundation/application/senior_decision Clinical Challenge vignettes for
the 3 Thyroid / Parathyroid / Salivary topics flagged by
audit_domain_ladder_inventory_v217.py as having no deliberately-reviewed ladder
row (recently-added topics that never got this pass). Grounded in each topic's
existing Deep Curriculum content -- no new clinical facts, numbers, or grading
systems introduced beyond what that content already states.
"""
from copy import deepcopy

DOMAIN = "Thyroid / Parathyroid / Salivary"

NEW_QUESTIONS = [   {   'id': 'v461_tps_dequervain_fnd',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'Subacute (de Quervain) Thyroiditis',
        'stem': 'A 34-year-old woman presents two weeks after an upper respiratory viral illness '
                'with a painful, tender thyroid gland, low-grade fever, and new palpitations with '
                'mild heat intolerance. She has no prior thyroid history.',
        'choices': [   'Subacute (de Quervain) granulomatous thyroiditis',
                       'Graves disease',
                       'Acute suppurative thyroiditis from bacterial infection',
                       'Papillary thyroid carcinoma'],
        'answer': 0,
        'explanation': 'A painful, tender thyroid following a viral-like illness, with fever and '
                       'transient thyrotoxic symptoms, is the classic pattern of subacute '
                       'granulomatous (de Quervain) thyroiditis: inflammatory follicular '
                       'disruption releases stored hormone, producing destructive thyrotoxicosis '
                       'rather than increased synthesis.',
        'why_wrong': [   'Correct.',
                         'Graves disease produces thyrotoxicosis from increased hormone synthesis '
                         'and is not classically painful or preceded by a viral prodrome.',
                         'Bacterial suppurative thyroiditis is rare, usually presents with a more '
                         'toxic/septic picture, and is not the pattern suggested by a preceding '
                         'viral illness with transient thyrotoxicosis.',
                         'Thyroid carcinoma typically presents as a painless nodule or mass, not '
                         'an acutely tender gland after a viral illness.'],
        'board_pearl': 'Pain, high inflammatory markers, thyrotoxicosis, and low '
                       'radioactive-iodine uptake form the classic de Quervain pattern -- '
                       'anticipate the thyrotoxic-to-hypothyroid-to-recovery sequence.',
        'curveball': 'What basic labs and inflammatory markers should be checked first in this '
                     'patient?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-subacute-de-quervain-thyroiditis',
        'learning_stage': 'foundation',
        'curveball_answer': 'Check TSH/free hormones along with ESR or CRP. The combination of '
                            'biochemical thyrotoxicosis with markedly elevated inflammatory '
                            'markers supports destructive thyroiditis; ultrasound or biopsy is '
                            'reserved for atypical or focal findings, not routine cases.',
        'ladder_reviewed': True,
        'focus': 'boards'},
    {   'id': 'v461_tps_dequervain_app',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'Subacute (de Quervain) Thyroiditis',
        'stem': 'A patient has a tender goiter, elevated free T4, and suppressed TSH. The '
                'referring physician is deciding between Graves disease and subacute (de Quervain) '
                'thyroiditis before starting treatment.',
        'choices': [   'Start antithyroid drugs empirically for either diagnosis, since management '
                       'is identical',
                       'Order a radioactive-iodine uptake study: low uptake favors destructive '
                       'thyroiditis, high uptake favors Graves disease',
                       'Diagnose based on gland tenderness alone and skip any confirmatory testing',
                       'Obtain fine-needle aspiration of the entire gland as the first '
                       'discriminating test'],
        'answer': 1,
        'explanation': 'Low radioactive-iodine uptake during thyrotoxicosis distinguishes '
                       'destructive thyroiditis (hormone leaking from damaged follicles) from '
                       'Graves disease (uptake is high because synthesis is increased). This '
                       'distinction changes management directly: antithyroid drugs work in Graves '
                       'but do not help destructive thyroiditis.',
        'why_wrong': [   'Management is not identical: antithyroid drugs treat Graves disease but '
                         'do not help de Quervain thyroiditis, which is destructive rather than '
                         'driven by increased synthesis.',
                         'Correct.',
                         'Tenderness supports subacute thyroiditis but is not by itself a '
                         'validated way to separate the two diagnoses when confirmatory testing is '
                         'available.',
                         'Ultrasound or biopsy is reserved for atypical or focal findings, not '
                         'used as the first-line discriminator between Graves disease and '
                         'destructive thyroiditis.'],
        'board_pearl': 'Low uptake with thyrotoxicosis means the hormone is leaking out, not being '
                       'made faster -- that single concept separates destructive thyroiditis from '
                       'Graves disease.',
        'curveball': 'The uptake study confirms de Quervain thyroiditis. The patient has '
                     'significant adrenergic symptoms and gland pain. How should these be managed?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-subacute-de-quervain-thyroiditis',
        'learning_stage': 'application',
        'curveball_answer': 'Treat pain with NSAIDs and reserve corticosteroids for severe or '
                            'refractory inflammation. Beta blockade addresses adrenergic symptoms; '
                            'antithyroid drugs do not help, since the process is destructive, not '
                            'synthetic. Follow the patient through the expected transient '
                            'hypothyroid phase, since uncommon permanent hypothyroidism can occur.',
        'ladder_reviewed': True,
        'focus': 'boards'},
    {   'id': 'v461_tps_dequervain_snr',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'Subacute (de Quervain) Thyroiditis',
        'stem': 'A patient was diagnosed with de Quervain thyroiditis two months ago and treated '
                'supportively. She now has a persistent, firm, focal area in the gland that has '
                'not resolved despite an otherwise typical clinical recovery, and no longer looks '
                'like the original diffuse tender process.',
        'choices': [   'Start antithyroid medication indefinitely because thyrotoxicosis is '
                       'expected to recur',
                       'Reassure the patient that all de Quervain thyroiditis leaves a permanent '
                       'firm residual and no further workup is needed',
                       'Reopen the diagnostic evaluation for the persistent focal lesion rather '
                       'than assuming ongoing subacute thyroiditis',
                       'Proceed directly to total thyroidectomy without further evaluation'],
        'answer': 2,
        'explanation': 'There is no routine surgical role in de Quervain thyroiditis, and the '
                       'expected course is a thyrotoxic-to-hypothyroid-to-recovery sequence. A '
                       'persistent focal lesion, failure to follow that expected course, abscess '
                       'concern, or compressive progression should prompt the clinician to reopen '
                       'the diagnosis rather than continue to attribute the finding to subacute '
                       'thyroiditis.',
        'why_wrong': [   'Antithyroid drugs do not treat de Quervain thyroiditis at any stage, '
                         'since the thyrotoxicosis is destructive rather than synthetic in origin.',
                         'A persistent focal abnormality is not an expected feature of the typical '
                         'de Quervain course and should not be dismissed as a routine residual.',
                         'Correct.',
                         'There is no routine surgical role in de Quervain thyroiditis; jumping to '
                         'thyroidectomy without first reopening the diagnostic evaluation skips '
                         'the needed step.'],
        'board_pearl': 'The expected de Quervain course is thyrotoxic, then hypothyroid, then '
                       'recovery -- anything that deviates from that pattern, especially a '
                       'persistent focal finding, earns a fresh diagnostic look, not reassurance.',
        'curveball': 'What specific findings, beyond a persistent focal lesion, should make a '
                     'clinician reconsider the diagnosis during follow-up of presumed subacute '
                     'thyroiditis?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-subacute-de-quervain-thyroiditis',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Failure to follow the expected thyrotoxic-to-hypothyroid-to-recovery '
                            'course, concern for an abscess, or compressive progression should '
                            'each reopen the diagnosis rather than being treated as an expected '
                            'variant of subacute thyroiditis.',
        'ladder_reviewed': True,
        'focus': 'postoperative_call'},
    {   'id': 'v461_tps_hashimoto_fnd',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'Hashimoto Thyroiditis',
        'stem': 'A 45-year-old woman is found on routine exam to have a painless, firm, diffusely '
                'enlarged thyroid gland. She reports fatigue and mild cold intolerance, and '
                'outside labs obtained by her primary physician are notable for an elevated TSH.',
        'choices': [   'Graves disease',
                       'Subacute (de Quervain) thyroiditis',
                       'Acute suppurative thyroiditis',
                       'Hashimoto (chronic lymphocytic) thyroiditis'],
        'answer': 3,
        'explanation': 'Hashimoto thyroiditis commonly presents with a painless, firm, diffuse '
                       'gland, hypothyroid symptoms, or incidental biochemical/ultrasound '
                       'abnormalities. Chronic autoimmune lymphocytic injury progressively '
                       'destroys follicles and can produce either goitrous or atrophic disease.',
        'why_wrong': [   'Graves disease causes thyrotoxicosis with a suppressed TSH, the opposite '
                         'biochemical pattern from the elevated TSH described in this case.',
                         'De Quervain thyroiditis is classically painful and tender, follows a '
                         'viral illness, and produces transient thyrotoxicosis rather than a '
                         'painless hypothyroid picture.',
                         'Acute suppurative thyroiditis is an infectious process, not the diffuse '
                         'painless gland described here.',
                         'Correct.'],
        'why_wrong_note': None,
        'board_pearl': 'A painless, firm, diffusely enlarged gland with hypothyroid labs is the '
                       'classic Hashimoto presentation -- confirm with TSH/free T4 and supportive '
                       'anti-TPO antibodies.',
        'curveball': "What is the recommended treatment for this patient's overt hypothyroidism?",
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-hashimoto-thyroiditis',
        'learning_stage': 'foundation',
        'curveball_answer': 'Levothyroxine is used for overt hypothyroidism, with subclinical '
                            'disease treatment individualized. Monitor clinically and evaluate any '
                            'new focal or rapidly enlarging area rather than repeatedly measuring '
                            'antibodies.',
        'ladder_reviewed': True,
        'focus': 'boards'},
    {   'id': 'v461_tps_hashimoto_app',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'Hashimoto Thyroiditis',
        'stem': 'A patient with known, longstanding Hashimoto thyroiditis and stable levothyroxine '
                'dosing is noted at a routine visit to have a new dominant nodule within the gland '
                "that has grown rapidly over recent weeks, distinct from the patient's usual "
                'diffuse heterogeneous texture.',
        'choices': [   'Evaluate the new dominant, rapidly growing nodule on its own merits rather '
                       "than attributing it to the patient's known Hashimoto disease",
                       'Attribute the finding to Hashimoto thyroiditis and simply continue routine '
                       'antibody monitoring',
                       'Increase the levothyroxine dose and reassess the nodule in one year',
                       'Reassure the patient that diffuse heterogeneity from Hashimoto disease '
                       'explains any focal change'],
        'answer': 0,
        'explanation': "Do not dismiss a dominant nodule or rapidly growing mass as 'just "
                       "Hashimoto.' Diffuse heterogeneity alone is not an FNA indication, but a "
                       'new dominant or rapidly enlarging focal finding must be risk-stratified '
                       'independently, since chronic autoimmune background disease does not '
                       'protect against a separate suspicious process.',
        'why_wrong': [   'Correct.',
                         'Repeatedly measuring antibodies does not address a new focal finding and '
                         'is not the appropriate response to a rapidly growing nodule.',
                         'Levothyroxine dosing addresses hypothyroidism, not a focal structural '
                         'change, and delaying evaluation by a year is not appropriate for a '
                         'rapidly growing nodule.',
                         'Diffuse heterogeneity from chronic lymphocytic thyroiditis does not '
                         'explain or excuse a distinct dominant, rapidly growing nodule, which '
                         'should be evaluated on its own.'],
        'board_pearl': 'Risk-stratify the focal finding on its own merits -- a background of '
                       'Hashimoto thyroiditis is not a reason to dismiss a new dominant or rapidly '
                       'growing nodule.',
        'curveball': 'Ultrasound shows the dominant area is now markedly enlarged compared with '
                     'prior imaging. What diagnosis should be urgently considered, and how is it '
                     'worked up?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-hashimoto-thyroiditis',
        'learning_stage': 'application',
        'curveball_answer': 'Rapid enlargement warrants urgent lymphoma evaluation, often with '
                            'core biopsy and flow/cytogenetic studies, because lymphoma arising in '
                            'a background of chronic lymphocytic thyroiditis is primarily treated '
                            'nonsurgically rather than by upfront surgery.',
        'ladder_reviewed': True,
        'focus': 'boards'},
    {   'id': 'v461_tps_hashimoto_snr',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'Hashimoto Thyroiditis',
        'stem': 'A patient with chronic Hashimoto thyroiditis has a large goiter causing '
                'progressive dysphagia and a sensation of neck pressure. Core biopsy of a '
                'separately identified focal lesion confirms thyroid lymphoma rather than a '
                'suspicious epithelial nodule.',
        'choices': [   'Proceed with total thyroidectomy as the primary treatment for the lymphoma',
                       'Refer for nonsurgical treatment of the lymphoma, reserving surgery for the '
                       'compressive goiter component if it independently requires it',
                       'Manage both the compressive symptoms and the lymphoma with levothyroxine '
                       'dose escalation alone',
                       'Defer any treatment until the patient develops overt airway obstruction'],
        'answer': 1,
        'explanation': 'Lymphoma arising in the setting of Hashimoto thyroiditis is primarily '
                       'treated nonsurgically once confirmed by core biopsy with flow/cytogenetic '
                       'studies. Surgery in Hashimoto disease is reserved for selected compressive '
                       'goiter or independently suspicious disease, so the compressive component '
                       'and the lymphoma are managed along separate pathways rather than treating '
                       'the mass as a single surgical problem.',
        'why_wrong': [   'Thyroid lymphoma is primarily treated nonsurgically; upfront total '
                         'thyroidectomy is not the appropriate primary treatment once lymphoma is '
                         'confirmed.',
                         'Correct.',
                         'Levothyroxine treats hypothyroidism, not lymphoma or mechanical '
                         'compression from goiter, and does not substitute for definitive '
                         'management of either problem.',
                         'Progressive dysphagia from a compressive goiter should not be left until '
                         'frank airway obstruction develops; the compressive component should be '
                         'assessed for whether it independently requires intervention.'],
        'board_pearl': 'When lymphoma is found in a Hashimoto gland, treat the lymphoma '
                       'nonsurgically and judge the compressive goiter component on its own merits '
                       '-- do not default to thyroidectomy as the answer for either problem.',
        'curveball': 'Why is core biopsy with flow/cytogenetic studies preferred over standard FNA '
                     'when lymphoma is suspected in a Hashimoto gland?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-hashimoto-thyroiditis',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Rapid enlargement in a Hashimoto gland should trigger urgent lymphoma '
                            'evaluation, and that evaluation is often built around core biopsy '
                            'with flow/cytogenetic studies so that the diagnosis is established '
                            'with the tissue and studies needed to guide primarily nonsurgical '
                            'treatment, rather than relying on a nodule-focused sampling approach '
                            'alone.',
        'ladder_reviewed': True,
        'focus': 'postoperative_call'},
    {   'id': 'v461_tps_ebsln_fnd',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'External Branch of the Superior Laryngeal Nerve Injury',
        'stem': 'A professional singer undergoes an uncomplicated total thyroidectomy. '
                'Postoperatively her gross vocal-fold motion is normal on exam, but she reports '
                'she can no longer hit her high notes, has lost vocal projection, and tires '
                'quickly when singing.',
        'choices': [   'Unilateral recurrent laryngeal nerve paralysis',
                       'Bilateral recurrent laryngeal nerve paralysis',
                       'External branch of the superior laryngeal nerve (EBSLN) injury',
                       'Normal expected postoperative voice change requiring no further '
                       'evaluation'],
        'answer': 2,
        'explanation': 'After thyroid or neck surgery, loss of high pitch, projection, and vocal '
                       'endurance with preserved gross vocal-fold motion suggests EBSLN injury, '
                       'especially in a professional voice user. The EBSLN powers cricothyroid '
                       'tension, so injury changes pitch control without producing the classic '
                       'gross motion abnormality seen with recurrent laryngeal nerve paralysis.',
        'why_wrong': [   'Unilateral recurrent laryngeal nerve paralysis also produces vocal-fold '
                         'motion impairment, which is specifically preserved in this case.',
                         'Bilateral recurrent laryngeal nerve paralysis would be expected to cause '
                         'vocal-fold motion abnormality, often with airway compromise, not '
                         'preserved gross motion with isolated pitch/projection loss.',
                         'Correct.',
                         'Normal vocal-fold motion does not exclude laryngeal nerve injury; these '
                         'specific symptoms in a professional voice user should be evaluated, not '
                         'dismissed as expected.'],
        'board_pearl': 'Normal vocal-fold motion does not exclude laryngeal nerve injury -- ask '
                       'about high notes, projection, fatigue, and occupational voice demands.',
        'curveball': 'What test is the most specific confirmatory study for EBSLN injury when the '
                     'result will change counseling or treatment?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-external-branch-of-the-superior-laryngeal-nerve-injury',
        'learning_stage': 'foundation',
        'curveball_answer': 'Cricothyroid laryngeal EMG is the most specific confirmatory test '
                            'when the result will change counseling or treatment. Stroboscopy may '
                            'show subtle asymmetry but is not diagnostic on its own.',
        'ladder_reviewed': True,
        'focus': 'boards'},
    {   'id': 'v461_tps_ebsln_app',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'External Branch of the Superior Laryngeal Nerve Injury',
        'stem': 'During thyroidectomy for a large goiter, the surgeon is dissecting the superior '
                'pole and finds that the EBSLN crosses the superior thyroid vessels at, or just '
                'below, the upper edge of the superior pole, essentially within the planned '
                'ligation field of the superior pedicle.',
        'choices': [   'This anatomic relationship has no bearing on injury risk during '
                       'thyroidectomy',
                       'Cernea type 1, the lowest-injury-risk course',
                       'Cernea type 2a, a moderate-injury-risk course crossing less than 1 cm '
                       'above the pole',
                       'Cernea type 2b, the highest-injury-risk course, which is more common in '
                       'large glands or goiters'],
        'answer': 3,
        'explanation': "The Cernea classification describes the EBSLN's course relative to the "
                       'superior thyroid pole/vessels and predicts injury risk during '
                       'thyroidectomy. Type 2b crosses at or below the upper edge of the superior '
                       'pole, often within the ligation field of the superior pedicle, carrying '
                       'the highest injury risk, and is more common in large glands or goiters -- '
                       'exactly the anatomy described here.',
        'why_wrong': [   'The Cernea classification exists specifically because this anatomic '
                         'relationship predicts injury risk during thyroidectomy.',
                         'Type 1 crosses the vessels more than 1 cm above the superior pole and '
                         'carries the lowest risk, which does not match a nerve crossing at or '
                         "below the pole's upper edge.",
                         'Type 2a crosses less than 1 cm above the pole with moderate risk, which '
                         'is a higher position than the at-or-below-the-pole course described in '
                         'this case.',
                         'Correct.'],
        'board_pearl': 'Knowing the likely Cernea type before ligating the superior pedicle is '
                       'part of deliberate nerve preservation, not just careful dissection in '
                       'general.',
        'curveball': 'What operative technique should the surgeon use to reduce EBSLN injury risk '
                     'when handling the superior pedicle in this setting?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-external-branch-of-the-superior-laryngeal-nerve-injury',
        'learning_stage': 'application',
        'curveball_answer': 'Prevention requires capsular upper-pole dissection, individual vessel '
                            'control, and visual/monitoring-assisted nerve preservation when '
                            'feasible, rather than mass ligation of the superior pedicle.',
        'ladder_reviewed': True,
        'focus': 'OR_prep'},
    {   'id': 'v461_tps_ebsln_snr',
        'domain': 'Thyroid / Parathyroid / Salivary',
        'topic': 'External Branch of the Superior Laryngeal Nerve Injury',
        'stem': 'Six months after thyroidectomy, a professional voice user has confirmed isolated '
                'EBSLN injury on cricothyroid laryngeal EMG, with persistent loss of pitch range '
                'and projection despite this being well beyond the acute postoperative period. She '
                'asks about a definitive surgical repair to restore her prior voice.',
        'choices': [   'Counsel that no standard restorative operation exists for isolated EBSLN '
                       'injury, and focus management on voice therapy for compensation and safe '
                       'vocal loading',
                       'Offer immediate laryngeal reinnervation surgery as the standard '
                       'restorative procedure for isolated EBSLN injury',
                       'Recommend recurrent laryngeal nerve exploration and repair, since that is '
                       'the standard approach to any postoperative laryngeal nerve injury',
                       'Tell her that recovery is impossible and further voice therapy would not '
                       'be of value'],
        'answer': 0,
        'explanation': 'No standard restorative operation exists for isolated EBSLN injury. '
                       'Management centers on observation and voice therapy for compensation, '
                       'projection, and safe vocal loading, with recovery and functional impact '
                       'varying by patient -- an important distinction from recurrent laryngeal '
                       'nerve injury, where different management frameworks apply.',
        'why_wrong': [   'Correct.',
                         'There is no standard restorative operation for isolated EBSLN injury; '
                         'reinnervation procedures are not the established answer for this '
                         'specific nerve injury.',
                         'This is an EBSLN injury, not a recurrent laryngeal nerve injury, so '
                         'recurrent laryngeal nerve exploration is not the relevant intervention.',
                         'Recovery and functional impact vary, and voice therapy remains the '
                         'mainstay of management, so telling the patient nothing further can help '
                         'is not accurate.'],
        'board_pearl': 'For isolated EBSLN injury, voice therapy for compensation, projection, and '
                       'safe vocal loading is the mainstay -- there is no standard restorative '
                       'operation to counsel toward instead.',
        'curveball': 'How would you counsel this patient differently before her original surgery '
                     'if her EBSLN course had been identified as Cernea type 2b intraoperatively?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-thyroid-parathyroid-salivary-external-branch-of-the-superior-laryngeal-nerve-injury',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Knowing the likely Cernea type before ligating the superior pedicle '
                            'is part of deliberate nerve preservation, not just careful dissection '
                            'in general -- a type 2b course (crossing at or below the pole, more '
                            'common in large glands/goiters) would prompt more deliberate capsular '
                            'dissection and individual vessel control, and would support '
                            'counseling the patient preoperatively about a higher baseline injury '
                            'risk given her voice demands.',
        'ladder_reviewed': True,
        'focus': 'OR_prep'}]

# Remove helper key accidentally left on one dict during drafting (not part of schema).
for _q in NEW_QUESTIONS:
    _q.pop("why_wrong_note", None)


def apply_deep_curriculum_ladder_tps_v461(data_module, app_module=None):
    existing = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(existing, list):
        raise RuntimeError("v46.1: CLINICAL_CHALLENGES_V119 unavailable")
    existing_ids = {q.get("id") for q in existing}
    added = 0
    cases = list(existing)
    for q in NEW_QUESTIONS:
        if q["id"] in existing_ids:
            raise RuntimeError(f"v46.1: duplicate id {q['id']!r}")
        cases.append(q)
        added += 1
    data_module.CLINICAL_CHALLENGES_V119 = cases
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {"questions_added": added}
