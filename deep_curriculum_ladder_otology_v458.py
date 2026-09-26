"""ENT Mastery v45.8 -- Learning-ladder gapfill: Otology / Neurotology.

Adds foundation/application/senior_decision Clinical Challenge vignettes for
the 7 Otology / Neurotology topics flagged by audit_domain_ladder_inventory_v217.py
as having no deliberately-reviewed ladder row (recently-added topics that never
got this pass). Grounded in each topic's existing Deep Curriculum content --
no new clinical facts, numbers, or grading systems introduced beyond what that
content already states.
"""
from copy import deepcopy

DOMAIN = "Otology / Neurotology"

NEW_QUESTIONS = [   {   'id': 'v458_oto_exostoses_fnd',
        'domain': 'Otology / Neurotology',
        'topic': 'EAC Exostoses / Osteoma (Canalplasty)',
        'stem': 'A 34-year-old avid cold-water surfer presents with bilateral, multiple, smooth, '
                'broad-based bony prominences narrowing the medial external auditory canal (EAC). '
                'He reports occasional trapped water after surfing but no pain, drainage, or '
                'hearing complaints, and both TMs are visualized without difficulty. What is the '
                'most appropriate next step?',
        'choices': [   'Observation, with counseling on cold-water exposure reduction and '
                       'protective earplugs/hood use',
                       'Immediate bilateral canalplasty to prevent future obstruction',
                       'High-resolution CT temporal bone to stage the lesions before any decision',
                       'Referral for biopsy to exclude EAC cholesteatoma'],
        'answer': 0,
        'explanation': 'This is the classic pattern of exostoses ("surfer\'s ear") from cold-water '
                       'exposure: bilateral, multiple, smooth, broad-based bony prominences. With '
                       'a patent, dry, self-cleaning canal and no attributable symptoms, the '
                       'correct management is observation plus counseling on exposure reduction '
                       'and protective gear, not prophylactic surgery, imaging, or biopsy.',
        'why_wrong': [   'Correct.',
                         'Surgery is not justified by imaging or appearance alone without symptoms '
                         'or an access/surveillance problem; this asymptomatic, patent canal does '
                         'not meet surgical indications.',
                         'Typical asymptomatic exostoses need no routine imaging; CT is reserved '
                         'for severe occlusion, suspected erosion/cholesteatoma, or preoperative '
                         'planning.',
                         'There is no focal otalgia, otorrhea, exposed/eroded bone, or soft-tissue '
                         'mass here to suggest cholesteatoma or neoplasm, so biopsy is not '
                         'indicated.'],
        'board_pearl': 'Incidental smooth bilateral exostoses plus a patent, dry, self-cleaning '
                       'canal = observation, not prophylactic canalplasty.',
        'curveball': 'How would the appearance and typical laterality differ if this were a '
                     'solitary EAC osteoma instead of exostoses?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-otology-neurotology-eac-exostoses-osteoma-canalplasty',
        'learning_stage': 'foundation',
        'curveball_answer': 'EAC osteoma is usually a solitary, unilateral, discrete or '
                            'pedunculated bony mass, often near a tympanosquamous or '
                            'tympanomastoid suture -- unlike the bilateral, multiple, broad-based '
                            'pattern typical of exostoses. Both are typical patterns rather than '
                            'absolute rules, and both can be incidental.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_exostoses_app',
        'domain': 'Otology / Neurotology',
        'topic': 'EAC Exostoses / Osteoma (Canalplasty)',
        'stem': 'A 52-year-old with a history of chronic swimming presents with a unilateral '
                'obstructing lesion in the medial EAC, but unlike his prior visits, he now reports '
                'disproportionate focal otalgia and scant otorrhea, and you note a small area of '
                "exposed, eroded-appearing bone at the lesion's edge. What should this change in "
                'your management?',
        'choices': [   'Continue to treat this as routine exostoses with observation only',
                       'Recognize this as a key trap: focal otalgia, otorrhea, and exposed/eroded '
                       'bone suggest EAC cholesteatoma rather than simple exostoses, and pursue '
                       'further evaluation',
                       'Proceed directly to elective canalplasty without further workup',
                       'Attribute the findings to keratosis obturans and manage with observation'],
        'answer': 1,
        'explanation': 'The curriculum explicitly flags this as a key trap: not every obstructing '
                       'canal lesion is an exostosis. Focal otalgia, otorrhea, exposed/eroded '
                       'bone, or disproportionate pain should prompt assessment for EAC '
                       'cholesteatoma rather than reflexive reassurance. Keratosis obturans '
                       'instead causes an obstructing keratin plug with usually concentric canal '
                       'widening, not focal bone erosion -- a distinct pattern from this '
                       'presentation.',
        'why_wrong': [   'Ignoring new pain, drainage, and bone erosion risks missing EAC '
                         'cholesteatoma, which changes imaging, biopsy, and extent-of-surgery '
                         'decisions.',
                         'Correct.',
                         'Jumping to surgery without characterizing a focally eroding lesion skips '
                         'the workup needed to know what you are actually operating on.',
                         'Keratosis obturans classically causes concentric widening from an '
                         'obstructing keratin plug, not focal bone erosion -- this presentation '
                         'does not fit that pattern.'],
        'board_pearl': 'Focal bone erosion in the EAC is a different problem from simple exostoses '
                       'and warrants cholesteatoma or malignancy evaluation.',
        'curveball': 'What specific imaging and exam findings would help distinguish keratosis '
                     'obturans from EAC cholesteatoma in an obstructed canal?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-otology-neurotology-eac-exostoses-osteoma-canalplasty',
        'learning_stage': 'application',
        'curveball_answer': 'Keratosis obturans causes an obstructing keratin plug and usually '
                            'concentric canal widening, whereas EAC cholesteatoma causes focal '
                            'bone erosion. This distinction changes imaging, biopsy decisions, and '
                            'the extent of surgery -- concentric widening favors keratosis '
                            'obturans managed with debridement, while focal erosion favors '
                            'cholesteatoma requiring more extensive evaluation and surgical '
                            'clearance.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_exostoses_snr',
        'domain': 'Otology / Neurotology',
        'topic': 'EAC Exostoses / Osteoma (Canalplasty)',
        'stem': 'You are planning canalplasty for a patient with recurrent obstruction-related '
                'otitis externa from broad-based exostoses. Critically, this is his only hearing '
                'ear after contralateral profound loss. During the case, the exostoses are so '
                'extensive that the anterosuperior canal wall, posteroinferior canal wall, and '
                'medial landmarks toward the TM are all difficult to identify with confidence. '
                'What is the best course of action?',
        'choices': [   'Continue drilling toward the presumed TM location using anatomic '
                       'estimates, since the case must be completed',
                       'Switch immediately to an osteotome only, since it is uniformly safer than '
                       'a drill in every scenario',
                       'Stop or change the surgical approach and consider additional exposure or '
                       'CT-guided planning rather than speculative drilling, while having already '
                       'discussed the small but consequential risk of iatrogenic sensorineural '
                       'hearing loss preoperatively',
                       'Abandon canalplasty permanently and refer for cochlear implantation '
                       'instead'],
        'answer': 2,
        'explanation': 'When landmarks are unsafe or unclear, the key trap is blind or speculative '
                       'drilling -- additional exposure or CT-guided planning is safer. This is '
                       'especially critical in an only-hearing ear, where the small but '
                       'consequential risk of iatrogenic sensorineural hearing loss must be '
                       'explicitly discussed with the patient beforehand, and intraoperative '
                       'caution must be even higher given the stakes. Osteotome versus drill '
                       'involves genuine tradeoffs in published cohorts (perforation, '
                       'sensorineural loss, and restenosis rates differ by technique), not a '
                       'universal safety hierarchy, so switching techniques is not itself a '
                       'substitute for safe technique when landmarks are lost.',
        'why_wrong': [   'Blind drilling toward presumed landmarks when anatomy is uncertain is '
                         'the highest-stakes error described for this operation, especially near '
                         'the facial nerve, TMJ, and TM/ossicles.',
                         'Osteotome versus drill involves real, published tradeoffs in '
                         'complication rates rather than one technique being universally safer; '
                         'this alone does not resolve a loss of surgical landmarks.',
                         'Correct.',
                         'Abandoning the case outright is an overcorrection; the appropriate step '
                         'is safer exposure or imaging-guided planning, not permanently forgoing a '
                         'symptomatic-indication procedure or unrelated cochlear implantation.'],
        'board_pearl': 'The high-stakes error in canalplasty is blind medial drilling: '
                       'posterior-inferior risks the facial nerve, anterior risks the TMJ, and '
                       'medial risks the TM/ossicles -- when landmarks are lost, get more exposure '
                       "or imaging, don't guess.",
        'curveball': 'How should informed consent differ for canalplasty in an only-hearing ear '
                     'compared with a routine bilateral-hearing patient?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'OR_prep',
        'concept_id': 'v6-otology-neurotology-eac-exostoses-osteoma-canalplasty',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'In an only-hearing ear, counseling must explicitly and separately '
                            'address the small but consequential risk of iatrogenic sensorineural '
                            'hearing loss from surgery near the medial canal/TM/ossicles, since '
                            'any loss here would functionally deafen the patient -- a materially '
                            'different risk calculus than in a patient with normal contralateral '
                            'hearing where the same complication would not be as devastating.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_ramsayhunt_fnd',
        'domain': 'Otology / Neurotology',
        'topic': 'Ramsay Hunt Syndrome (Herpes Zoster Oticus)',
        'stem': 'A 61-year-old presents with acute unilateral facial weakness, severe otalgia, and '
                'grouped vesicles on the pinna and in the external auditory canal. He also reports '
                'new tinnitus and mild vertigo. Which diagnosis best fits this presentation?',
        'choices': [   'Bell palsy',
                       'Malignant otitis externa',
                       'Acute otitis media with mastoiditis',
                       'Ramsay Hunt syndrome (herpes zoster oticus)'],
        'answer': 3,
        'explanation': 'Acute unilateral facial weakness with severe otalgia and vesicles of the '
                       'pinna, canal, or oropharynx is the classic presentation of Ramsay Hunt '
                       'syndrome, with hearing loss, tinnitus, or vertigo reflecting adjacent '
                       'vestibulocochlear nerve involvement from varicella-zoster reactivation in '
                       'the geniculate ganglion.',
        'why_wrong': [   'Bell palsy does not classically feature vesicles or the severe otalgia '
                         'and audiovestibular symptoms described here.',
                         'Malignant otitis externa typically occurs in diabetic or '
                         'immunocompromised patients with granulation tissue and skull-base '
                         'osteomyelitis, not a vesicular rash with facial palsy.',
                         'There is no mention of otorrhea, TM findings, or mastoid signs pointing '
                         'to an infectious middle-ear/mastoid process; the vesicular rash and '
                         'facial palsy pattern instead point to zoster.',
                         'Correct.'],
        'board_pearl': 'Ear pain plus facial palsy warrants a careful search for vesicles on the '
                       'pinna, canal, or oropharynx to identify Ramsay Hunt syndrome.',
        'curveball': 'If no vesicles are found on exam, does that rule out Ramsay Hunt syndrome?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-otology-neurotology-ramsay-hunt-syndrome-herpes-zoster-oticus',
        'learning_stage': 'foundation',
        'curveball_answer': 'No. The absence of vesicles does not exclude the diagnosis -- this '
                            'can represent zoster sine herpete, where facial palsy and '
                            'audiovestibular symptoms occur without a visible rash. Ear pain plus '
                            'palsy still warrants a careful search for vesicles, but their absence '
                            'does not rule out the syndrome.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_ramsayhunt_app',
        'domain': 'Otology / Neurotology',
        'topic': 'Ramsay Hunt Syndrome (Herpes Zoster Oticus)',
        'stem': 'A patient presents with acute facial weakness and severe otalgia but no visible '
                'vesicles anywhere on exam. You are trying to decide how confidently you can call '
                'this Bell palsy versus Ramsay Hunt syndrome (zoster sine herpete). How should '
                'this distinction be approached, and what should guide further workup?',
        'choices': [   'Recognize that absent vesicles does not exclude zoster sine herpete, '
                       'document House-Brackmann grade and eye closure, obtain audiometry if '
                       'hearing symptoms are present, and reserve MRI or electrodiagnostics for '
                       'atypical, severe, or nonrecovering cases',
                       'Since no vesicles are visible, this must be Bell palsy and no further '
                       'consideration of zoster is needed',
                       'Obtain MRI and electrodiagnostic testing routinely on every acute facial '
                       'palsy regardless of severity',
                       'Assume Ramsay Hunt syndrome definitively and initiate facial nerve '
                       'decompression'],
        'answer': 0,
        'explanation': 'The diagnosis is clinical, and the curriculum specifically notes that '
                       'severe ear pain with palsy should prompt consideration of zoster sine '
                       'herpete even without visible vesicles. The standard workup is exam-based '
                       '(House-Brackmann grade, eye closure) plus audiometry when hearing symptoms '
                       'are present, reserving MRI or electrodiagnostics for atypical, severe, or '
                       'nonrecovering cases rather than routine use.',
        'why_wrong': [   'Correct.',
                         'The absence of vesicles does not exclude zoster sine herpete; severe '
                         'otalgia with palsy should still raise this possibility.',
                         'MRI and electrodiagnostics are reserved for atypical, severe, or '
                         'nonrecovering cases, not obtained routinely for every acute facial '
                         'palsy.',
                         'Facial nerve decompression is not routine in Ramsay Hunt syndrome '
                         'because evidence supporting it is insufficient, and this decision should '
                         'not be made before basic clinical workup regardless of presumed '
                         'diagnosis.'],
        'board_pearl': 'Severe otalgia with facial palsy should raise concern for zoster sine '
                       'herpete even without visible vesicles -- the diagnosis of Ramsay Hunt '
                       'syndrome remains clinical.',
        'curveball': 'How does the expected facial recovery prognosis for Ramsay Hunt syndrome '
                     'generally compare with Bell palsy, and why does this distinction matter for '
                     'counseling?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-otology-neurotology-ramsay-hunt-syndrome-herpes-zoster-oticus',
        'learning_stage': 'application',
        'curveball_answer': 'Ramsay Hunt syndrome generally has a worse facial recovery prognosis '
                            'than Bell palsy. This matters for counseling because patients with '
                            'Ramsay Hunt syndrome should be prepared for a higher likelihood of '
                            'persistent deficit and the possible later need for exposure '
                            'protection, rehabilitation, chemodenervation, or facial reanimation '
                            'depending on recovery and denervation duration.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_ramsayhunt_snr',
        'domain': 'Otology / Neurotology',
        'topic': 'Ramsay Hunt Syndrome (Herpes Zoster Oticus)',
        'stem': 'A patient with Ramsay Hunt syndrome and House-Brackmann grade VI facial palsy is '
                'seen 8 months after onset with no meaningful facial recovery and poor eye closure '
                'on the affected side. The family asks whether facial nerve decompression should '
                'now be performed to improve outcome. How should this be addressed?',
        'choices': [   'Recommend facial nerve decompression now, since surgery is the standard '
                       'next step for any nonrecovering palsy',
                       'Explain that facial nerve decompression is not routine in Ramsay Hunt '
                       'syndrome because evidence is insufficient, and instead focus on exposure '
                       'protection, rehabilitation, chemodenervation, or facial reanimation based '
                       'on the degree of recovery and duration of denervation',
                       'Reassure the family that recovery will still occur spontaneously and no '
                       'intervention is needed',
                       'Refer only for hearing aid evaluation, since the audiovestibular symptoms '
                       'are the primary long-term concern'],
        'answer': 1,
        'explanation': 'The curriculum is explicit that facial nerve decompression is not routine '
                       'in Ramsay Hunt syndrome because supporting evidence is insufficient. For '
                       'persistent deficits at this stage, management shifts to exposure '
                       'protection (given poor eye closure), rehabilitation, chemodenervation, or '
                       'facial reanimation options tailored to recovery status and denervation '
                       'duration -- not reflexive decompression surgery.',
        'why_wrong': [   'Decompression is specifically not considered routine in Ramsay Hunt '
                         'syndrome given insufficient evidence; recommending it as a default next '
                         'step misrepresents the evidence base.',
                         'Correct.',
                         'At 8 months with grade VI palsy and poor eye closure, false reassurance '
                         'risks corneal injury and delays appropriate exposure protection and '
                         'reanimation planning.',
                         'While audiovestibular symptoms may also need attention, poor eye closure '
                         'with a nonrecovering grade VI palsy is the more urgent issue requiring '
                         'exposure protection and reanimation planning, not deferral to hearing '
                         'aid evaluation alone.'],
        'board_pearl': 'Persistent facial deficits after Ramsay Hunt syndrome are managed with '
                       'exposure protection, rehabilitation, chemodenervation, or reanimation -- '
                       'not routine decompression, since evidence for decompression is '
                       'insufficient.',
        'curveball': 'What is the most time-urgent concern in a patient with poor eye closure from '
                     'facial palsy, regardless of the underlying cause?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'postoperative_call',
        'concept_id': 'v6-otology-neurotology-ramsay-hunt-syndrome-herpes-zoster-oticus',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Corneal exposure and injury from inadequate eye closure is the most '
                            'time-urgent concern in facial palsy of any cause. Meticulous corneal '
                            'protection (lubrication, taping, moisture chamber, or surgical '
                            'options such as eyelid weighting when severe) should be started '
                            'immediately and is not something to delay while awaiting facial nerve '
                            'recovery.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_facialschwannoma_fnd',
        'domain': 'Otology / Neurotology',
        'topic': 'Facial Nerve Schwannoma',
        'stem': 'A patient has slowly progressive ipsilateral facial weakness over many months, '
                'with imaging showing a middle-ear mass and smooth enlargement of the fallopian '
                'canal. Facial function is relatively preserved despite the mass being of moderate '
                'size. What should be high on the differential?',
        'choices': [   'Cholesteatoma with erosion of the ossicular chain only',
                       'Acute Bell palsy',
                       'Facial nerve schwannoma',
                       'Otosclerosis'],
        'answer': 2,
        'explanation': 'Slowly progressive, recurrent, or fluctuating ipsilateral facial weakness '
                       'with a middle-ear or internal-auditory-canal mass, or facial function '
                       'discordant with tumor size, should raise suspicion for facial nerve '
                       'schwannoma. Smooth fallopian-canal enlargement with multisegment '
                       'enhancement helps distinguish it from other temporal-bone and '
                       'cerebellopontine-angle lesions.',
        'why_wrong': [   'Isolated cholesteatoma with ossicular erosion does not typically produce '
                         'smooth fallopian-canal enlargement with multisegment enhancement, and '
                         'would more classically present with conductive hearing loss rather than '
                         'progressive facial weakness discordant with mass size.',
                         'Bell palsy is an acute, typically rapidly evolving palsy without an '
                         'associated mass or fallopian-canal enlargement, and recurrent same-side '
                         'palsy or failure of presumed Bell palsy to recover should itself prompt '
                         'imaging.',
                         'Correct.',
                         'Otosclerosis causes progressive conductive hearing loss from stapes '
                         'fixation, not facial nerve dysfunction or a fallopian-canal mass.'],
        'board_pearl': 'Facial function discordant with tumor size, or failure of presumed Bell '
                       'palsy to recover, should prompt imaging for facial nerve schwannoma.',
        'curveball': 'Along what course can a facial nerve schwannoma arise, and how does that '
                     'affect distinguishing it from other lesions?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-otology-neurotology-facial-nerve-schwannoma',
        'learning_stage': 'foundation',
        'curveball_answer': 'The tumor can arise along any facial-nerve segment. Smooth '
                            'fallopian-canal enlargement and multisegment enhancement on imaging '
                            'help distinguish it from other temporal-bone and '
                            "cerebellopontine-angle lesions that do not follow the nerve's course "
                            'in this characteristic way.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_facialschwannoma_app',
        'domain': 'Otology / Neurotology',
        'topic': 'Facial Nerve Schwannoma',
        'stem': 'A patient was diagnosed with Bell palsy 4 months ago and was told to expect '
                'recovery. She now returns with recurrent weakness on the same side after a brief '
                'partial improvement. What is the most appropriate next step?',
        'choices': [   'Reassure her that Bell palsy recurrences on the same side are expected and '
                       'no further workup is needed',
                       'Proceed directly to facial nerve resection given recurrent symptoms',
                       'Start a second course of oral corticosteroids without imaging',
                       'Obtain contrast MRI (with temporal-bone CT as needed) to evaluate for a '
                       'structural cause such as facial nerve schwannoma, since recurrent '
                       'same-side palsy or failure of presumed Bell palsy to recover warrants '
                       'imaging'],
        'answer': 3,
        'explanation': 'Recurrent same-side palsy or failure of presumed Bell palsy to recover is '
                       'specifically flagged as a trigger for imaging to look for a structural '
                       'cause such as facial nerve schwannoma. Contrast MRI maps neural and '
                       'soft-tissue extent, and temporal-bone CT defines fallopian-canal and '
                       'ossicular involvement when needed.',
        'why_wrong': [   'Recurrent same-side facial weakness is not an expected feature of '
                         'typical Bell palsy and should not be dismissed without evaluation.',
                         'Resection is not the first step and is not favored when facial function '
                         'is preserved; intact function argues against reflexive excision, and '
                         'imaging/counseling must precede any operative decision.',
                         'Repeating steroids without imaging risks missing a structural lesion '
                         'driving the recurrent presentation.',
                         'Correct.'],
        'board_pearl': "Counsel from the patient's present facial function, not tumor size alone, "
                       'and remember that resection often risks facial deterioration.',
        'curveball': "If MRI confirms a small facial nerve schwannoma and the patient's facial "
                     'function is currently good, what is the most appropriate management '
                     'approach?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-otology-neurotology-facial-nerve-schwannoma',
        'learning_stage': 'application',
        'curveball_answer': 'Observe small or slowly growing tumors with useful facial function '
                            'using serial examination, audiometry, and MRI. Stereotactic radiation '
                            'or surgery is individualized by growth, symptoms, hearing, location, '
                            'age, and goals, rather than being reflexively pursued for a tumor '
                            'with preserved function.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_facialschwannoma_snr',
        'domain': 'Otology / Neurotology',
        'topic': 'Facial Nerve Schwannoma',
        'stem': 'A patient with a known facial nerve schwannoma along the tympanic and mastoid '
                'segments currently has good facial function (House-Brackmann II) but the tumor '
                'has shown clear interval growth on serial MRI, and it is beginning to encroach on '
                'the ossicular chain with early conductive hearing loss. How should the surgeon '
                'frame the decision-making with the patient?',
        'choices': [   'Individualize the decision among continued observation, stereotactic '
                       'radiation, or surgery (decompression, nerve-sparing debulking, or '
                       'resection with repair/grafting/transfer) based on growth, symptoms, '
                       'hearing, location, age, and goals, explicitly counseling that resection '
                       'often risks major facial deterioration despite currently intact function',
                       'Recommend immediate complete resection with nerve grafting, since growth '
                       'on imaging alone mandates surgery',
                       'Because facial function is still good, defer any discussion of '
                       'intervention indefinitely regardless of growth',
                       'Proceed to radiosurgery without further discussion, since it is uniformly '
                       'preferred over surgery for any growing facial nerve schwannoma'],
        'answer': 0,
        'explanation': 'Management is individualized by growth, symptoms, hearing, location, age, '
                       'and goals rather than dictated by any single factor. Even with documented '
                       'growth, options include continued observation, stereotactic radiation, or '
                       'various surgical strategies (decompression, nerve-sparing debulking in '
                       'selected anatomy, or resection with primary repair, grafting, or nerve '
                       'transfer). Because resection often risks major facial deterioration, '
                       'intact function argues against reflexive excision, so this tradeoff must '
                       'be explicitly discussed even when growth or emerging hearing loss makes '
                       'observation alone less comfortable.',
        'why_wrong': [   'Correct.',
                         'Growth on imaging alone does not mandate resection; intact facial '
                         'function argues against reflexive excision given the risk of facial '
                         'deterioration.',
                         'Interval growth with emerging ossicular involvement is a meaningful '
                         'change that should prompt reassessment and discussion, not indefinite '
                         'deferral.',
                         'There is no basis for treating radiosurgery as uniformly preferred over '
                         'surgery in every case; the choice is individualized based on the same '
                         'set of patient- and tumor-specific factors.'],
        'board_pearl': 'Facial nerve schwannoma management is a tradeoff conversation, not a '
                       'single algorithm: intact function argues against reflexive excision even '
                       'when a tumor is growing.',
        'curveball': 'What operative options exist when resection is ultimately chosen, and how do '
                     'they differ in expected facial outcome?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'OR_prep',
        'concept_id': 'v6-otology-neurotology-facial-nerve-schwannoma',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Options include decompression, nerve-sparing debulking in selected '
                            'anatomy, radiosurgery, or resection with primary repair, grafting, or '
                            'nerve transfer. Resection often risks major facial deterioration '
                            'compared with nerve-sparing or observational strategies, which is why '
                            "the choice should be tailored to the patient's current function and "
                            'goals rather than defaulting to complete excision.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_ansd_fnd',
        'domain': 'Otology / Neurotology',
        'topic': 'Auditory Neuropathy Spectrum Disorder',
        'stem': 'An infant with a history of prematurity and hyperbilirubinemia has speech '
                'understanding that seems disproportionately poor relative to behavioral '
                'audiometric thresholds, with results that also fluctuate between visits. Which '
                'diagnosis should be suspected?',
        'choices': [   'Simple conductive hearing loss from otitis media with effusion',
                       'Auditory neuropathy spectrum disorder (ANSD)',
                       'Typical sensorineural hearing loss from cochlear hair cell damage alone',
                       'Normal hearing with a behavioral testing artifact'],
        'answer': 1,
        'explanation': 'ANSD should be suspected when speech understanding is disproportionately '
                       'poor or fluctuating relative to behavioral thresholds, especially in the '
                       'setting of risk factors such as prematurity, hyperbilirubinemia, '
                       'neuropathy, or family history -- exactly as described here.',
        'why_wrong': [   'Conductive loss from effusion does not typically produce '
                         'disproportionately poor speech understanding relative to thresholds in '
                         'this described pattern, and effusion is not mentioned here.',
                         'Correct.',
                         'In ANSD, outer-hair-cell function is preserved while inner-hair-cell, '
                         'synaptic, or auditory-nerve transmission is dys-synchronous -- this is a '
                         'distinct pattern from ordinary hair-cell-mediated sensorineural loss.',
                         'The described mismatch between thresholds and speech understanding, '
                         'combined with known risk factors, argues against dismissing this as '
                         'normal hearing or artifact.'],
        'board_pearl': 'The signature of ANSD is preserved cochlear receptor activity with '
                       'disordered neural synchrony -- suspect it when speech understanding does '
                       'not match the audiogram.',
        'curveball': 'What specific test findings confirm the diagnosis of ANSD?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-otology-neurotology-auditory-neuropathy-spectrum-disorder',
        'learning_stage': 'foundation',
        'curveball_answer': 'Confirm a present cochlear microphonic and/or otoacoustic emissions '
                            '(OAEs) together with an absent or markedly abnormal ABR, recognizing '
                            'that OAEs may disappear over time. This is supplemented with '
                            'behavioral audiology, speech perception testing, genetics, and MRI of '
                            'the cochlear nerves.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_ansd_app',
        'domain': 'Otology / Neurotology',
        'topic': 'Auditory Neuropathy Spectrum Disorder',
        'stem': 'A child with confirmed ANSD (present cochlear microphonic, absent ABR) has '
                'completed a trial of appropriately fitted hearing aids and remote-microphone '
                'technology, with close functional monitoring, but continues to make limited '
                'progress in speech and language despite thresholds that would predict some '
                'benefit from amplification. What should guide the next management decision?',
        'choices': [   'Rely on the audiogram alone; since thresholds suggest amplification should '
                       'work, continue the same hearing aid trial indefinitely',
                       'Diagnose a permanent ceiling on communication ability and discontinue '
                       'further intervention',
                       'Base escalation on functional speech-language progress rather than the '
                       'audiogram alone, and consider cochlear implantation now that appropriately '
                       'fitted amplification has failed to support speech and language',
                       'Switch immediately to auditory-brainstem-implant evaluation without '
                       'confirming cochlear-nerve status first'],
        'answer': 2,
        'explanation': 'Escalation of management in ANSD should be based on functional '
                       'speech-language progress, not a single audiogram, since thresholds alone '
                       'do not predict benefit in this disorder. When appropriately fitted '
                       'amplification fails to support speech and language, cochlear implantation '
                       'should be considered as the next step.',
        'why_wrong': [   'Thresholds alone do not predict benefit in ANSD; persisting with the '
                         'same approach despite documented functional failure ignores the guidance '
                         'to base decisions on functional progress.',
                         'A trial of amplification failing to produce expected progress is an '
                         'indication to escalate care, not to conclude that no further benefit is '
                         'possible.',
                         'Correct.',
                         'Auditory-brainstem-implant evaluation is reserved for selected centers '
                         'and follows confirmation that cochlear-nerve integrity is severely '
                         'deficient; it should not bypass cochlear implantation evaluation and '
                         'cochlear-nerve confirmation first.'],
        'board_pearl': 'In ANSD, escalate based on functional speech-language progress, not '
                       'thresholds alone -- amplification failure to support language is the '
                       'trigger for cochlear implant evaluation.',
        'curveball': 'What imaging or diagnostic step should be confirmed before pursuing cochlear '
                     'implantation in ANSD, and why does it matter?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-otology-neurotology-auditory-neuropathy-spectrum-disorder',
        'learning_stage': 'application',
        'curveball_answer': 'Confirm cochlear-nerve integrity with MRI of the cochlear nerves '
                            'before pursuing cochlear implantation, because severe cochlear-nerve '
                            'deficiency predicts limited benefit from a standard cochlear implant '
                            'and may instead prompt auditory-brainstem-implant evaluation in '
                            'selected centers.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_ansd_snr',
        'domain': 'Otology / Neurotology',
        'topic': 'Auditory Neuropathy Spectrum Disorder',
        'stem': 'A child with ANSD is being evaluated for cochlear implantation after failed '
                'amplification trials. MRI raises concern for severe cochlear-nerve deficiency on '
                'the side being considered for implantation. The family strongly wants to proceed '
                'with a standard cochlear implant on that side regardless. How should you counsel '
                'them?',
        'choices': [   'Proceed with a standard cochlear implant on that side as requested, since '
                       'ANSD patients generally have preserved cochlear-nerve function by '
                       'definition',
                       'Recommend bilateral standard cochlear implantation simultaneously without '
                       'addressing the nerve-deficiency finding',
                       'Tell the family no further intervention is possible and discontinue the '
                       'workup entirely',
                       'Explain that severe cochlear-nerve deficiency predicts limited benefit '
                       'from a standard cochlear implant, and discuss auditory-brainstem-implant '
                       'evaluation in selected centers as the more appropriate next step for this '
                       'specific finding'],
        'answer': 3,
        'explanation': 'While ANSD as a category is defined by dys-synchronous rather than absent '
                       'auditory-nerve transmission, cochlear-nerve integrity must specifically be '
                       'confirmed before implantation, because severe cochlear-nerve deficiency on '
                       'imaging predicts limited benefit from a standard cochlear implant and may '
                       'prompt evaluation for an auditory-brainstem implant at a center equipped '
                       'to offer it. This is a senior-level counseling point: family preference '
                       'does not override a structural finding that changes expected device '
                       'benefit.',
        'why_wrong': [   'ANSD does not guarantee normal cochlear-nerve anatomy; imaging showing '
                         'severe deficiency specifically predicts limited benefit from a standard '
                         'implant regardless of the underlying ANSD diagnosis.',
                         'Proceeding with bilateral standard implantation without addressing a '
                         'specific concern for severe cochlear-nerve deficiency risks a '
                         'poor-benefit outcome that the workup was designed to anticipate.',
                         'Family desire and a concerning imaging finding do not by themselves mean '
                         'no options remain; auditory-brainstem-implant evaluation in selected '
                         'centers is the described next avenue.',
                         'Correct.'],
        'board_pearl': 'Confirm cochlear-nerve integrity before cochlear implantation in ANSD -- '
                       'severe deficiency changes the entire device conversation toward '
                       'auditory-brainstem-implant evaluation.',
        'curveball': "What risk factors in a child's history should raise suspicion for ANSD in "
                     'the first place, prompting this whole workup pathway?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'postoperative_call',
        'concept_id': 'v6-otology-neurotology-auditory-neuropathy-spectrum-disorder',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Prematurity, hyperbilirubinemia, neuropathy, or a family history of '
                            'similar findings should raise suspicion for ANSD, particularly when '
                            'speech understanding is disproportionately poor or fluctuating '
                            'relative to behavioral thresholds.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_vernet_fnd',
        'domain': 'Otology / Neurotology',
        'topic': 'Vernet Syndrome (Jugular Foramen Syndrome)',
        'stem': 'A patient presents with loss of gag reflex and posterior-tongue taste on one '
                'side, hoarseness with vocal-fold paralysis and dysphagia, and ipsilateral '
                'shoulder droop with weak head-turn to the opposite side. Tongue movement and '
                'strength are normal bilaterally. Which cranial nerve syndrome best fits this '
                'pattern?',
        'choices': [   'Vernet syndrome (jugular foramen syndrome)',
                       'Collet-Sicard syndrome',
                       'Villaret syndrome',
                       'Orbital apex syndrome'],
        'answer': 0,
        'explanation': 'This is the classic Vernet syndrome pattern: ipsilateral CN IX '
                       '(gag/taste), X (hoarseness, vocal-fold paralysis, dysphagia), and XI '
                       '(trapezius/sternocleidomastoid weakness causing shoulder droop and weak '
                       'head-turn) palsy from a lesion at the jugular foramen, where these three '
                       'nerves exit the skull base together. CN XII (tongue) is explicitly spared '
                       'here, which rules out syndromes that add hypoglossal involvement.',
        'why_wrong': [   'Correct.',
                         'Collet-Sicard syndrome adds CN XII (hypoglossal) involvement to this '
                         'picture, which would produce tongue weakness or deviation -- not present '
                         'here since tongue movement and strength are normal.',
                         'Villaret syndrome adds Horner syndrome (from sympathetic-chain '
                         'involvement in the retroparotid space) on top of the full IX-XII picture '
                         '-- neither Horner findings nor CN XII involvement are described here.',
                         'Orbital apex syndrome involves CN II, III, IV, VI, and V1 with visual '
                         'and ocular findings, which is an entirely different anatomic region and '
                         'nerve set from this presentation.'],
        'board_pearl': 'IX + X + XI at the jugular foramen with sparing of XII = Vernet syndrome; '
                       "this is the base of the lower-cranial-nerve 'syndrome ladder.'",
        'curveball': 'What are the most common underlying causes of Vernet syndrome that should be '
                     'sought on workup?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-otology-neurotology-vernet-syndrome-jugular-foramen-syndrome',
        'learning_stage': 'foundation',
        'curveball_answer': 'Typical causes include glomus jugulare paraganglioma, '
                            'lower-cranial-nerve schwannoma, metastasis, or skull-base meningioma '
                            '-- all of which can compress the jugular foramen where IX, X, and XI '
                            'exit together.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_vernet_app',
        'domain': 'Otology / Neurotology',
        'topic': 'Vernet Syndrome (Jugular Foramen Syndrome)',
        'stem': 'A patient has the IX, X, XI palsy pattern of Vernet syndrome, but on closer '
                'examination also has ipsilateral tongue weakness with deviation toward the weak '
                'side when protruded, though no ptosis, miosis, or anhidrosis is present. How '
                'should this modify the diagnosis and anatomic localization?',
        'choices': [   'This remains Vernet syndrome, since tongue findings are not clinically '
                       'significant',
                       'This is now Collet-Sicard syndrome, since CN XII (which exits separately '
                       'through the hypoglossal canal) is also involved, extending the lesion '
                       'beyond the jugular foramen alone -- and the absence of Horner findings '
                       'argues against Villaret syndrome',
                       'This is Villaret syndrome, since any additional cranial neuropathy beyond '
                       'IX-XI qualifies',
                       'This finding suggests orbital apex syndrome and warrants urgent '
                       'ophthalmologic evaluation'],
        'answer': 1,
        'explanation': 'Adding hypoglossal (XII) involvement to the IX, X, XI picture specifically '
                       'defines Collet-Sicard syndrome, since CN XII exits separately through the '
                       "hypoglossal canal rather than the jugular foramen -- meaning the lesion's "
                       'extent has grown beyond the jugular foramen alone. Villaret syndrome '
                       'requires the additional finding of Horner syndrome from cervical '
                       'sympathetic-chain involvement in the retroparotid space, which is '
                       'explicitly absent here (no ptosis, miosis, or anhidrosis).',
        'why_wrong': [   'New ipsilateral tongue weakness with deviation is a significant finding '
                         'that specifically reclassifies the syndrome and implies a larger lesion '
                         'extent.',
                         'Correct.',
                         'Villaret syndrome specifically requires Horner syndrome (ptosis, miosis, '
                         'anhidrosis) from sympathetic-chain involvement, which is explicitly '
                         'absent in this vignette; tongue involvement alone defines Collet-Sicard, '
                         'not Villaret.',
                         'There are no visual, ocular motility, or V1 findings described, so '
                         'orbital apex syndrome is not suggested by this presentation.'],
        'board_pearl': "Build the lower-cranial-nerve 'syndrome ladder': IX+X+XI = Vernet; add XII "
                       '= Collet-Sicard; add Horner (sympathetic chain) = Villaret. This ladder is '
                       'a classic oral-board discrimination question.',
        'curveball': 'Anatomically, why does adding CN XII involvement imply the lesion is not '
                     'confined to the jugular foramen alone?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-otology-neurotology-vernet-syndrome-jugular-foramen-syndrome',
        'learning_stage': 'application',
        'curveball_answer': 'CN XII exits the skull base separately through the hypoglossal canal, '
                            'not the jugular foramen. A lesion causing CN XII palsy in addition to '
                            'IX, X, and XI must therefore extend beyond the jugular foramen itself '
                            'to also affect the hypoglossal canal, which is the anatomic basis for '
                            'calling this Collet-Sicard syndrome rather than Vernet syndrome.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_vernet_snr',
        'domain': 'Otology / Neurotology',
        'topic': 'Vernet Syndrome (Jugular Foramen Syndrome)',
        'stem': 'Imaging in a patient with Vernet syndrome reveals a hypervascular jugular foramen '
                'mass consistent with glomus jugulare paraganglioma. The patient has significant '
                'medical comorbidities, and the lesion is small with slow growth on prior imaging. '
                'The team is deciding among observation, radiosurgery, and surgical resection, and '
                'a biopsy has been proposed to confirm histology before deciding. What is the most '
                'appropriate senior-level plan?',
        'choices': [   'Proceed directly to office or clinic biopsy of the mass to confirm '
                       'histology before any further planning',
                       'Proceed to surgical resection immediately regardless of comorbidities, '
                       'since resection is always preferred for jugular foramen masses',
                       'Favor observation given the small size, slow growth, and significant '
                       'comorbidities, since resection risks worsening existing '
                       'lower-cranial-neuropathy, while ensuring vascular imaging has already '
                       'characterized the lesion (biopsy of a suspected paraganglioma requires '
                       'this hypervascularity be addressed first, not performed as a routine '
                       'confirmatory step)',
                       'Choose stereotactic radiosurgery as the only acceptable option in all '
                       'jugular foramen paraganglioma cases'],
        'answer': 2,
        'explanation': 'For a small, asymptomatic or slow-growing jugular foramen lesion in an '
                       'older or comorbid patient, observation is favored, since resection risks '
                       'worsening existing lower-cranial-neuropathy. Vascular imaging is mandatory '
                       'before biopsying a suspected paraganglioma given its hypervascularity -- '
                       'this is a key trap, not a routine step to be performed casually in clinic. '
                       'The decision among observation, radiosurgery, and resection should be '
                       'individualized by lesion type, growth, and symptom burden, not dictated by '
                       'a single default option.',
        'why_wrong': [   'Vascular imaging is mandatory before biopsying a suspected paraganglioma '
                         'given its hypervascularity; proceeding straight to biopsy without this '
                         'workup is explicitly flagged as a key trap.',
                         'Observation is favored for small, slow-growing lesions in comorbid '
                         'patients specifically because resection risks worsening existing '
                         'lower-cranial-neuropathy; resection is not always the preferred option.',
                         'Correct.',
                         'Management is individualized by lesion type, growth, and symptom burden; '
                         'radiosurgery is one option among several, not the sole acceptable choice '
                         'in every case.'],
        'board_pearl': 'Vascular imaging is mandatory before biopsying a suspected paraganglioma '
                       'given its hypervascularity, and observation is favored for small, '
                       'slow-growing jugular foramen lesions in comorbid patients since resection '
                       'risks worsening existing lower-cranial-neuropathy.',
        'curveball': 'If surgical resection is ultimately chosen for a jugular foramen tumor, what '
                     'perioperative issue must be proactively planned for given the lower cranial '
                     'nerves at risk?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'OR_prep',
        'concept_id': 'v6-otology-neurotology-vernet-syndrome-jugular-foramen-syndrome',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Plan for perioperative airway/aspiration management, including '
                            'possible vocal-fold medialization and a feeding plan, since resection '
                            'can worsen voice and swallow function by further compromising the '
                            'lower cranial nerves (IX, X, XI) at the jugular foramen.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_gradenigo_fnd',
        'domain': 'Otology / Neurotology',
        'topic': 'Gradenigo Syndrome (Petrous Apicitis)',
        'stem': 'A child recovering from acute otitis media develops otorrhea, retro-orbital and '
                'facial pain in a trigeminal (V1) distribution, and new diplopia from inability to '
                'abduct one eye. Which diagnosis best explains this triad?',
        'choices': [   'Simple recurrent otitis media without complication',
                       'Orbital apex syndrome',
                       'Cavernous sinus syndrome',
                       'Gradenigo syndrome (petrous apicitis)'],
        'answer': 3,
        'explanation': 'The classic triad of otorrhea/otitis media, retro-orbital or facial pain '
                       'in a V1 distribution, and ipsilateral CN VI (abducens) palsy causing '
                       'diplopia and inability to abduct the eye, arising as a complication of '
                       'acute otitis media or mastoiditis extending to the petrous apex, defines '
                       'Gradenigo syndrome.',
        'why_wrong': [   'The combination of otorrhea, V1 pain, and a new isolated CN VI palsy is '
                         'not simple uncomplicated otitis media; it represents a specific '
                         'complication requiring imaging and directed treatment.',
                         'Orbital apex syndrome also affects vision (CN II) and typically involves '
                         'CN III/IV in addition to VI, which is a broader deficit than the '
                         'isolated CN VI palsy described here.',
                         'Cavernous sinus syndrome typically involves multiple cranial nerves '
                         '(III, IV, VI, V1, V2 ± Horner), not an isolated abducens palsy arising '
                         'specifically from otitis media/mastoiditis extension to the petrous '
                         'apex.',
                         'Correct.'],
        'board_pearl': 'Otorrhea + retro-orbital (V1) pain + isolated CN VI palsy after otitis '
                       'media/mastoiditis = Gradenigo syndrome.',
        'curveball': 'Anatomically, why is it specifically the abducens nerve that is affected '
                     'rather than other nearby cranial nerves?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-otology-neurotology-gradenigo-syndrome-petrous-apicitis',
        'learning_stage': 'foundation',
        'curveball_answer': 'CN VI travels through Dorello canal beneath the petroclinoid ligament '
                            'immediately adjacent to the petrous apex, so inflammation from '
                            'petrous apicitis compresses or irritates the abducens nerve '
                            'specifically at this anatomic bottleneck. Adjacent trigeminal '
                            'ganglion/Meckel cave involvement produces the accompanying facial '
                            'pain.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_gradenigo_app',
        'domain': 'Otology / Neurotology',
        'topic': 'Gradenigo Syndrome (Petrous Apicitis)',
        'stem': 'A patient with suspected Gradenigo syndrome also has vision loss and involvement '
                'of multiple additional cranial nerves beyond CN VI, including CN III and V1/V2 '
                'sensory loss, raising concern that this might instead be cavernous sinus syndrome '
                'or orbital apex syndrome. What is the key discriminating feature that should '
                'guide the diagnosis, and why does this matter for imaging and treatment?',
        'choices': [   'Recognize that Gradenigo syndrome specifically involves the abducens nerve '
                       'alone via Dorello canal at the petrous apex, whereas broader multi-nerve '
                       'or visual involvement points toward orbital apex or cavernous sinus '
                       'syndrome, which changes the anatomic target of imaging and the '
                       'differential',
                       'There is no meaningful clinical difference between these syndromes, so the '
                       'distinction does not affect management',
                       'Assume this is still Gradenigo syndrome and manage with myringotomy tube '
                       'placement alone regardless of the additional findings',
                       'Order only a temporal bone CT and avoid MRI, since intracranial extension '
                       'is not a concern in this differential'],
        'answer': 0,
        'explanation': 'The curriculum explicitly frames this as a discriminator boards use: '
                       'Gradenigo syndrome is specifically the abducens nerve, not the whole '
                       'cavernous sinus or orbital apex, because Dorello canal at the petrous apex '
                       'is the anatomic bottleneck. Broader involvement (vision loss, multiple '
                       'additional nerves) should redirect the differential and imaging target '
                       'toward orbital apex syndrome or cavernous sinus syndrome rather than '
                       'assuming petrous apicitis alone.',
        'why_wrong': [   'Correct.',
                         'The distinction meaningfully changes the anatomic differential, required '
                         'imaging, and downstream management -- it is not a trivial difference.',
                         'Additional multi-nerve and visual findings beyond isolated CN VI palsy '
                         'should prompt reconsideration of the diagnosis rather than reflexively '
                         'continuing to treat as isolated petrous apicitis.',
                         'Contrast MRI is specifically used to assess dural enhancement, venous '
                         'sinus involvement, and exclude abscess or further intracranial extension '
                         '-- it should not be omitted, especially when the picture is broader than '
                         'isolated Gradenigo syndrome.'],
        'board_pearl': 'Gradenigo syndrome is specifically the abducens nerve, not the whole '
                       'cavernous sinus or orbital apex -- broader deficits should redirect the '
                       'differential.',
        'curveball': 'What imaging findings would specifically support petrous apicitis as the '
                     'underlying process in this patient?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-otology-neurotology-gradenigo-syndrome-petrous-apicitis',
        'learning_stage': 'application',
        'curveball_answer': 'Temporal bone CT assesses petrous apex opacification or erosion, '
                            'while contrast MRI assesses dural enhancement, venous sinus '
                            'involvement, and excludes abscess or further intracranial extension. '
                            'Ophthalmology evaluation helps characterize the diplopia.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_gradenigo_snr',
        'domain': 'Otology / Neurotology',
        'topic': 'Gradenigo Syndrome (Petrous Apicitis)',
        'stem': 'A patient with Gradenigo syndrome from acute mastoiditis has been started on IV '
                'antibiotics with myringotomy and tube placement for source control, but after '
                'several days shows no clinical improvement and repeat imaging suggests persistent '
                "significant apicitis. The patient's hearing on that side is already profoundly "
                'impaired. What is the most appropriate next step, and which surgical corridor '
                'consideration is relevant?',
        'choices': [   'Continue the same IV antibiotic regimen indefinitely without considering '
                       'surgical drainage, since medical therapy is always sufficient given more '
                       'time',
                       'Pursue surgical drainage via a petrous apicectomy corridor, and note that '
                       'a translabyrinthine approach becomes a reasonable option specifically '
                       'because the ear is already deaf, alongside retrolabyrinthine or '
                       'infralabyrinthine alternatives chosen based on hearing status and '
                       'pneumatization pattern',
                       'Proceed to definitive translabyrinthine surgery regardless of hearing '
                       'status, since it is the universally preferred corridor',
                       'Discontinue antibiotics and observe, since petrous apicitis without '
                       'improvement typically resolves spontaneously'],
        'answer': 1,
        'explanation': 'Failure to improve on medical management, or significant apicitis, '
                       'warrants surgical drainage. Petrous apicectomy corridors -- '
                       'retrolabyrinthine, infralabyrinthine, or translabyrinthine -- are chosen '
                       'based on hearing status and pneumatization pattern. Critically, a '
                       'translabyrinthine approach is a reasonable option specifically in an '
                       'already-deaf ear, since it sacrifices residual hearing that does not exist '
                       'to preserve in this case, while protecting the facial nerve, carotid '
                       'artery, and jugular bulb regardless of approach.',
        'why_wrong': [   'Failure to improve on IV antibiotics with source control is a specific '
                         'indication described for surgical drainage, not for continuing the same '
                         'regimen indefinitely.',
                         'Correct.',
                         'The translabyrinthine corridor is specifically favored in an '
                         'already-deaf ear, not universally preferred regardless of hearing '
                         'status; approach selection is guided by hearing status and '
                         'pneumatization pattern.',
                         'Significant apicitis that fails to improve on medical management is '
                         'explicitly described as warranting surgical drainage, not observation '
                         'alone.'],
        'board_pearl': 'Failure to improve, abscess, or significant apicitis after medical '
                       'management of Gradenigo syndrome warrants surgical drainage, with corridor '
                       'choice guided by hearing status and pneumatization pattern.',
        'curveball': 'What structures must be specifically protected during a petrous apicectomy, '
                     'regardless of which corridor is chosen?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'overnight_call',
        'concept_id': 'v6-otology-neurotology-gradenigo-syndrome-petrous-apicitis',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Regardless of the specific corridor (retrolabyrinthine, '
                            'infralabyrinthine, or translabyrinthine), the labyrinth (when hearing '
                            'preservation is relevant), facial nerve, carotid artery, and jugular '
                            'bulb must all be protected during petrous apicectomy.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_glomus_fnd',
        'domain': 'Otology / Neurotology',
        'topic': 'Glomus Tumor / Paraganglioma',
        'stem': 'A patient reports pulsatile tinnitus, and otoscopy reveals a reddish, '
                'vascular-appearing mass behind an intact tympanic membrane with an associated '
                'conductive hearing loss. Pneumatic otoscopy causes the mass to blanch. What is '
                'the most likely diagnosis?',
        'choices': [   'Granulation tissue from chronic otitis media',
                       'Simple middle-ear effusion',
                       'Jugulotympanic paraganglioma (glomus tympanicum or glomus jugulare)',
                       'Cholesteatoma'],
        'answer': 2,
        'explanation': 'Pulsatile tinnitus with a reddish or bluish mass behind an intact TM, '
                       'often with conductive hearing loss, suggests a jugulotympanic '
                       'paraganglioma. A positive Brown sign (blanching of the mass with pneumatic '
                       'otoscopy) supports a vascular middle-ear lesion over a simple effusion or '
                       'granulation tissue.',
        'why_wrong': [   'Granulation tissue is a described mimic that the Brown sign specifically '
                         'helps exclude in favor of a vascular lesion.',
                         'A simple effusion does not classically blanch with pneumatic otoscopy (a '
                         'positive Brown sign) or present with pulsatile tinnitus in this vascular '
                         'pattern.',
                         'Correct.',
                         'Cholesteatoma typically presents with a keratin debris-containing mass '
                         'and possible erosion, not a reddish, blanching, pulsatile vascular mass '
                         'behind an intact TM.'],
        'board_pearl': 'Pulsatile tinnitus plus a reddish, blanching middle-ear mass is a '
                       'paraganglioma until proven otherwise -- do not biopsy a suspected glomus '
                       'tumor in clinic.',
        'curveball': 'From what structures do these tumors classically arise?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-otology-neurotology-glomus-tumor-paraganglioma',
        'learning_stage': 'foundation',
        'curveball_answer': "These tumors arise from paraganglion cells along Jacobson's nerve "
                            "(tympanic branch of CN IX, on the cochlear promontory) or Arnold's "
                            'nerve, or from the adventitia of the jugular bulb. Glomus tympanicum '
                            'stays confined to the middle ear/promontory, while glomus jugulare '
                            'arises from the jugular bulb and can extend through the temporal bone '
                            'toward the carotid canal, jugular foramen, and posterior fossa.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_glomus_app',
        'domain': 'Otology / Neurotology',
        'topic': 'Glomus Tumor / Paraganglioma',
        'stem': 'A patient with a confirmed jugulotympanic paraganglioma is found on CT temporal '
                'bone to have permeative erosion of the jugular plate, and MRI shows a classic '
                "'salt-and-pepper' enhancement pattern with extension toward the jugular foramen. "
                'Which statement about workup is most appropriate at this point?',
        'choices': [   'Proceed to an in-clinic needle biopsy to confirm histology before further '
                       'imaging',
                       'Order only a chest x-ray to complete staging, since paragangliomas do not '
                       'have a hereditary component',
                       'No further workup is needed since the imaging appearance alone is '
                       'sufficient to finalize a treatment plan',
                       'This pattern favors glomus jugulare rather than glomus tympanicum, and '
                       "given the tumor's likely hereditary potential, family history, biochemical "
                       'screening for catecholamine secretion, and genetic counseling/testing '
                       'should be pursued, with catheter angiography considered for preoperative '
                       'planning'],
        'answer': 3,
        'explanation': 'Permeative jugular plate erosion favors glomus jugulare (versus a '
                       'promontory-confined lesion favoring tympanicum), and the classic '
                       "'salt-and-pepper' pattern on MRI reflects flow voids in a vascular tumor. "
                       'Because a substantial proportion of these tumors are hereditary '
                       '(paraganglioma-pheochromocytoma syndromes, most often SDHB/SDHD and also '
                       'SDHC), family history, biochemical screening for catecholamine secretion, '
                       'and genetic counseling/testing should be pursued. Catheter angiography '
                       'with preoperative embolization is used for large, vascular tumors to '
                       'reduce operative blood loss.',
        'why_wrong': [   'A suspected paraganglioma should never be biopsied in clinic given its '
                         'hypervascularity; vascular imaging and characterization must come first.',
                         'These tumors do have a meaningful hereditary component (SDHB/SDHD/SDHC), '
                         'which should prompt family history-taking and genetic '
                         'counseling/testing, not be dismissed.',
                         'Imaging characterizes anatomic extent but does not substitute for '
                         'genetic/hereditary workup or planning for vascular control, both of '
                         'which materially change management.',
                         'Correct.'],
        'board_pearl': 'Always screen for a hereditary paraganglioma syndrome (SDHB/SDHD/SDHC) -- '
                       'it changes counseling, surveillance, and the threshold for looking for '
                       'synchronous or metastatic disease.',
        'curveball': 'Which specific hereditary paraganglioma gene carries higher '
                     'malignant/metastatic potential and should lower the threshold for full-body '
                     'staging?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'boards',
        'concept_id': 'v6-otology-neurotology-glomus-tumor-paraganglioma',
        'learning_stage': 'application',
        'curveball_answer': 'SDHB carries higher malignant/metastatic potential and should lower '
                            'the threshold for full-body staging compared with other '
                            'paraganglioma-associated genes such as SDHD or SDHC.',
        'ladder_reviewed': True},
    {   'id': 'v458_oto_glomus_snr',
        'domain': 'Otology / Neurotology',
        'topic': 'Glomus Tumor / Paraganglioma',
        'stem': 'A patient has a tympanojugular paraganglioma classified as modified Fisch Class '
                'C2, with involvement extending toward the carotid canal, and lower cranial nerves '
                'IX-XII are currently functioning normally. The tumor is large and hypervascular. '
                'How should the surgical team approach planning?',
        'choices': [   'Recognize this as a Class C tumor requiring a lateral skull-base approach '
                       'with proximal-to-distal vascular control, involving a multidisciplinary '
                       'neurotology/neurosurgery/vascular team, since jugular bulb and lower '
                       'cranial nerve (IX-XII) preservation drive the approach as much as tumor '
                       "removal, and consider preoperative embolization given the tumor's "
                       'vascularity',
                       'Proceed with a simple transcanal removal, since this approach works for '
                       'all Fisch classes',
                       'Skip preoperative embolization since it provides no meaningful benefit in '
                       'vascular tumors of this size',
                       'Treat this identically to a Class A glomus tympanicum tumor confined to '
                       'the middle ear'],
        'answer': 0,
        'explanation': 'Modified Fisch classification stages extent and guides the operative plan: '
                       'Class C (tympanojugular, extending beyond the tympanomastoid space toward '
                       'the carotid canal/foramen lacerum, subclassified C1-C4 by carotid '
                       'canal/ICA involvement) requires a lateral skull-base approach with '
                       'proximal-to-distal vascular control and typically a multidisciplinary '
                       'team, since preserving the jugular bulb and lower cranial nerves (IX-XII) '
                       'is as important as tumor removal. Preoperative embolization meaningfully '
                       'reduces blood loss in vascular tumors and should be considered here.',
        'why_wrong': [   'Correct.',
                         'Simple transcanal removal is appropriate only for small Class A/B tumors '
                         'confined to the middle ear or tympanomastoid compartment, not for a '
                         'Class C tympanojugular tumor.',
                         'Preoperative embolization meaningfully reduces blood loss in vascular '
                         'tumors and should specifically be considered for a large, hypervascular '
                         'lesion like this one.',
                         'Class A tumors are managed transcanally or via a transmastoid approach; '
                         'a Class C tumor with carotid canal extension requires a fundamentally '
                         'different lateral skull-base approach and multidisciplinary planning.'],
        'board_pearl': 'Classify (Fisch A-D) before deciding treatment, since class drives both '
                       'approach and morbidity risk; preoperative embolization meaningfully '
                       'reduces blood loss in vascular tumors.',
        'curveball': 'Why is class D specifically distinguished from class C in the modified Fisch '
                     'classification, and what does that distinction signal about surgical risk?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'focus': 'OR_prep',
        'concept_id': 'v6-otology-neurotology-glomus-tumor-paraganglioma',
        'learning_stage': 'senior_decision',
        'curveball_answer': 'Class D denotes intracranial extension, graded by dural displacement '
                            '(De/Di), distinguishing it from Class C tumors that remain '
                            'extracranial but extend toward the carotid canal/foramen lacerum. '
                            'Intracranial extension in Class D signals a higher-risk, more complex '
                            'resection typically requiring closer neurosurgical involvement for '
                            'dural and intracranial management beyond the lateral skull-base work '
                            'needed for Class C alone.',
        'ladder_reviewed': True}]


def apply_deep_curriculum_ladder_otology_v458(data_module, app_module=None):
    existing = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(existing, list):
        raise RuntimeError("v45.8: CLINICAL_CHALLENGES_V119 unavailable")
    existing_ids = {q.get("id") for q in existing}
    added = 0
    cases = list(existing)
    for q in NEW_QUESTIONS:
        if q["id"] in existing_ids:
            raise RuntimeError(f"v45.8: duplicate id {q['id']!r}")
        cases.append(q)
        added += 1
    data_module.CLINICAL_CHALLENGES_V119 = cases
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {"questions_added": added}
