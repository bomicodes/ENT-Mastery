"""ENT Mastery v46.2 -- Learning-ladder gapfill: Pediatric Otolaryngology.

Adds foundation/application/senior_decision Clinical Challenge vignettes for
the 3 Pediatric Otolaryngology topics flagged by audit_domain_ladder_inventory_v217.py
as having no deliberately-reviewed ladder row (recently-added topics that never
got this pass). Grounded in each topic's existing Deep Curriculum content --
no new clinical facts or numbers introduced beyond what that content already
states.
"""
from copy import deepcopy

DOMAIN = "Pediatric Otolaryngology"

NEW_QUESTIONS = [   {   'id': 'v462_peds_pierrerobin_fnd',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Pierre Robin Sequence',
        'stem': 'A newborn is noted to have a small, retruded lower jaw, a tongue that appears to '
                'fall backward into the pharynx, and a U-shaped cleft of the soft and hard palate. '
                'The infant has intermittent inspiratory noisy breathing that worsens with supine '
                'positioning and feeding difficulty. Which diagnosis best explains this triad?',
        'choices': [   'Pierre Robin sequence',
                       'Isolated bifid uvula without airway involvement',
                       'Choanal atresia as an isolated finding',
                       'Laryngomalacia unrelated to jaw or palate anatomy'],
        'answer': 0,
        'explanation': 'Micrognathia, glossoptosis, and upper-airway obstruction, often together '
                       'with a U-shaped cleft palate, define Pierre Robin sequence. The mandibular '
                       'hypoplasia pushes the tongue posteriorly, producing tongue-base '
                       'obstruction rather than a primary laryngeal problem, and the same crowding '
                       'of the oral cavity by the tongue can impede palatal fusion.',
        'why_wrong': [   'Correct.',
                         'A bifid uvula alone does not explain micrognathia, glossoptosis, or '
                         "obstructive breathing, and this infant's palate finding is a full "
                         'U-shaped cleft, not an isolated bifid uvula.',
                         'Choanal atresia is a distinct anterior nasal airway problem and does not '
                         'by itself produce micrognathia or a U-shaped cleft palate.',
                         "Laryngomalacia is a laryngeal-level diagnosis, whereas this infant's "
                         'obstruction is described as tongue-base level from a hypoplastic '
                         'mandible, not a primary laryngeal problem.'],
        'board_pearl': 'Micrognathia plus glossoptosis plus a U-shaped cleft palate is the classic '
                       'Pierre Robin triad, and the obstruction is at the tongue base, not the '
                       'larynx.',
        'curveball': 'Why does the cleft palate in Pierre Robin sequence tend to have a U shape '
                     'rather than the V shape seen in many isolated cleft palates?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-pierre-robin-sequence',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        'focus': 'boards',
        'curveball_answer': 'In Pierre Robin sequence, mandibular hypoplasia displaces the tongue '
                            'posteriorly and superiorly early in development, and the posteriorly '
                            'lodged tongue mechanically blocks the palatal shelves from fusing in '
                            'the midline, leaving a wide, U-shaped defect. This is distinct from '
                            'an isolated cleft palate, where the shelves fail to approximate for '
                            'other reasons and the resulting cleft is typically narrower and '
                            'V-shaped.'},
    {   'id': 'v462_peds_pierrerobin_app',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Pierre Robin Sequence',
        'stem': 'A 2-week-old with micrognathia and glossoptosis is referred for cleft palate '
                'repair. The parents ask whether the palate can simply be repaired now so feeding '
                'improves. The infant has never had a formal assessment of breathing during sleep '
                'or feeding, and no airway endoscopy has been performed. What is the most '
                'appropriate next step?',
        'choices': [   'Proceed directly to palate repair, since palate closure is the definitive '
                       'treatment for Pierre Robin sequence',
                       'Assess breathing across sleep and feeding, obtain polysomnography or gas '
                       'exchange evaluation as needed, evaluate swallowing, and characterize the '
                       'airway obstruction level by endoscopy before committing to a treatment '
                       'pathway',
                       'Discharge home with instructions for casual prone positioning to relieve '
                       'tongue-base obstruction',
                       'Schedule tracheostomy as the default first intervention for all infants '
                       'with this presentation'],
        'answer': 1,
        'explanation': 'The airway and nutritional status must be quantified before any definitive '
                       'intervention is chosen. This means assessing breathing during sleep and '
                       'feeding, obtaining polysomnography or gas-exchange data when indicated, '
                       'evaluating swallowing, and characterizing obstruction level with '
                       'endoscopy, along with screening for an associated syndrome such as '
                       'Stickler syndrome. Palate repair is deferred until the airway and growth '
                       'are stabilized, since airway and nutrition come first.',
        'why_wrong': [   'Palate repair follows airway and growth stabilization in Pierre Robin '
                         'sequence; it is not the first or definitive step, and proceeding without '
                         'first quantifying obstruction risks a decompensated airway.',
                         'Correct.',
                         'Home sleep and positioning plans must follow specialist-directed '
                         'guidance rather than casual prone-position advice, and safe-sleep '
                         'recommendations for infants must still be respected.',
                         'Tracheostomy is reserved for persistent significant obstruction selected '
                         'by obstruction level, comorbidity, and institutional expertise; it is '
                         'not a default first intervention before the obstruction has even been '
                         'characterized.'],
        'board_pearl': 'In Pierre Robin sequence, quantify the airway and nutrition first, and '
                       'identify multilevel or syndromic disease, before choosing a tongue, '
                       'mandible, or tracheostomy solution.',
        'curveball': 'What clinical and genetic features should prompt evaluation for Stickler '
                     'syndrome in an infant with Pierre Robin sequence, and why does that '
                     'distinction matter?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-pierre-robin-sequence',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        'focus': 'OR_prep',
        'curveball_answer': 'Isolated Pierre Robin sequence and syndromic forms differ in '
                            'prognosis, so phenotype (for example, associated ocular, joint, or '
                            'hearing findings) and genetic testing are used to evaluate for '
                            'syndromes such as Stickler syndrome. Recognizing a syndromic form '
                            'matters because it can change expected clinical course, the '
                            'multidisciplinary team involved, and long-term monitoring needs, even '
                            'though the immediate airway-first approach to management is similar.'},
    {   'id': 'v462_peds_pierrerobin_snr',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Pierre Robin Sequence',
        'stem': 'An infant with Pierre Robin sequence has persistent, significant upper-airway '
                'obstruction despite optimized positioning and feeding support, with obstruction '
                'localized to the tongue base by endoscopy and no additional multilevel airway '
                'disease identified. The family and craniofacial team are discussing definitive '
                'surgical options. Which statement best reflects how the decision among mandibular '
                'distraction, tongue-lip adhesion, and tracheostomy should be made?',
        'choices': [   'Mandibular distraction should never be used in Pierre Robin sequence '
                       'because it does not address glossoptosis',
                       'Tracheostomy should always be chosen first because it is the most '
                       'definitive way to secure the airway regardless of other findings',
                       'The choice should be selected based on obstruction level, comorbidities, '
                       'and institutional expertise, rather than defaulting to a single procedure '
                       'for every infant with persistent obstruction',
                       'Tongue-lip adhesion is contraindicated whenever any airway obstruction is '
                       'present'],
        'answer': 2,
        'explanation': 'When significant obstruction persists despite non-surgical measures, the '
                       'choice among mandibular distraction, tongue-lip adhesion, and tracheostomy '
                       'is individualized based on the level of obstruction, associated '
                       'comorbidities (including multilevel or syndromic airway disease), and '
                       'institutional expertise, rather than applying one procedure uniformly. '
                       'This reflects the same airway-first, obstruction-level-driven reasoning '
                       'used earlier in the pathway, now applied to surgical decision-making.',
        'why_wrong': [   'Mandibular distraction is a recognized option specifically aimed at '
                         'correcting the mandibular hypoplasia that produces glossoptosis by '
                         'advancing the mandible and repositioning the tongue base forward; it is '
                         'not excluded from consideration.',
                         'Tracheostomy is one option selected for appropriate cases, not a '
                         'universal first choice; the decision depends on obstruction level, '
                         'comorbidity, and institutional expertise.',
                         'Correct.',
                         'Tongue-lip adhesion is one of the surgical options considered for '
                         'persistent significant obstruction; it is not categorically '
                         'contraindicated by the mere presence of obstruction, since that '
                         'obstruction is the reason surgery is being considered.'],
        'board_pearl': 'There is no single default operation for persistent obstruction in Pierre '
                       'Robin sequence; obstruction level, comorbidity, and institutional '
                       'expertise together guide the choice among mandibular distraction, '
                       'tongue-lip adhesion, and tracheostomy.',
        'curveball': 'If endoscopy in this infant instead showed multilevel airway obstruction '
                     'beyond the tongue base, how should that finding change the pre-operative '
                     'discussion?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-pierre-robin-sequence',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        'focus': 'postoperative_call',
        'curveball_answer': 'Identifying multilevel or syndromic airway disease before choosing a '
                            'tongue, mandible, or tracheostomy solution is part of the core '
                            'teaching for this condition. A finding of obstruction beyond the '
                            'tongue base means a single-level procedure aimed only at glossoptosis '
                            '(such as mandibular distraction or tongue-lip adhesion) may not '
                            'resolve the obstruction, and the discussion should reassess whether '
                            'tracheostomy or a combined approach is more appropriate given the '
                            'added level(s) of disease.'},
    {   'id': 'v462_peds_nasaldermoid_fnd',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Nasal Dermoid Cyst',
        'stem': 'A toddler is brought in for a small pit on the midline of the nasal dorsum with '
                'an occasional protruding hair and a history of recurrent sebaceous drainage and '
                'low-grade swelling at the same spot. There is no history of trauma. What is the '
                'most likely diagnosis?',
        'choices': [   'A benign nevus of the nasal skin',
                       'Simple epidermal inclusion cyst of the nasal tip unrelated to embryologic '
                       'tracts',
                       'Allergic rhinitis with nasal crusting',
                       'Nasal dermoid cyst'],
        'answer': 3,
        'explanation': 'A congenital midline nasal dorsal pit, tract, mass, hair, or recurrent '
                       'sebaceous drainage is the classic presentation of a nasal dermoid, arising '
                       'from trapped ectoderm along the embryologic prenasal or foramen cecum '
                       'pathway. This cutaneous tract can variably approach or cross the skull '
                       'base, which is why the midline location and these specific features (pit, '
                       'hair, recurrent drainage) matter diagnostically.',
        'why_wrong': [   'A nevus is a pigmented skin lesion and does not account for a pit, a '
                         'hair, or a draining tract.',
                         'The midline location, protruding hair, and recurrent sebaceous drainage '
                         'are specifically described as suggesting a dermoid tied to a congenital '
                         'embryologic tract, not an unrelated simple inclusion cyst.',
                         'Allergic rhinitis does not produce a midline dorsal pit, a hair, or a '
                         'tract with recurrent sebaceous drainage.',
                         'Correct.'],
        'board_pearl': 'A midline nasal dorsal pit with a hair or recurrent drainage is a nasal '
                       'dermoid until proven otherwise, and the concern is not merely cosmetic.',
        'curveball': 'Why is the exact embryologic pathway (prenasal space and foramen cecum) '
                     'relevant to why this lesion can reach the skull base, whereas an off-midline '
                     'nasal skin lesion generally would not?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-nasal-dermoid-cyst',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        'focus': 'boards',
        'curveball_answer': 'Trapped ectoderm along the embryologic prenasal and foramen cecum '
                            'pathway is what leaves behind a cutaneous tract that variably '
                            'approaches or crosses the skull base in nasal dermoids. Because this '
                            'pathway runs in the midline from the nasal dorsum toward the anterior '
                            'skull base, a lesion along it can have intracranial or dural '
                            'extension. A lesion off the midline is not associated with this '
                            'specific embryologic tract and does not carry the same '
                            'intracranial-extension concern.'},
    {   'id': 'v462_peds_nasaldermoid_app',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Nasal Dermoid Cyst',
        'stem': 'A 3-year-old has a midline nasal dorsal pit with a small tuft of hair and a '
                'history of recurrent drainage, now clinically quiet. The referring clinic '
                'performed an office biopsy of the tract before referral. On review, you are asked '
                'how this case should have been, and should now be, worked up prior to definitive '
                'treatment. What is the best approach?',
        'choices': [   'Image before any biopsy or probing, using MRI to best evaluate '
                       'intracranial and dural extension and thin-cut CT selectively for bony '
                       'detail that changes operative planning, distinguishing this from '
                       'encephalocele or nasal glial heterotopia before proceeding',
                       'No imaging is needed since the diagnosis is already established clinically '
                       'by the pit and hair',
                       'Office biopsy or blind probing of the tract is an acceptable first step to '
                       'confirm the diagnosis before imaging',
                       'CT alone is sufficient and MRI adds no additional information for this '
                       'lesion'],
        'answer': 0,
        'explanation': 'The board-level safety rule for a midline pediatric nasal mass is to image '
                       'before incision, because the tract may communicate with the skull base. '
                       'MRI best evaluates intracranial and dural extension, while thin-cut CT '
                       'adds bony detail selectively when it will change operative planning; '
                       'imaging is also used to distinguish a dermoid from an encephalocele or '
                       'nasal glial heterotopia. Blind probing or office biopsy should be avoided '
                       'precisely because of the risk of unrecognized intracranial communication.',
        'why_wrong': [   'Correct.',
                         'Even when the external findings strongly suggest a dermoid, imaging is '
                         'required before definitive treatment specifically to assess for '
                         'intracranial or dural extension and to rule out mimics such as '
                         'encephalocele, which clinical appearance alone cannot reliably exclude.',
                         'Blind probing or office biopsy of a midline nasal tract should be '
                         'avoided; the safety principle is to image before incision or biopsy '
                         'given the possibility of skull-base communication.',
                         'MRI and thin-cut CT provide complementary information (intracranial and '
                         'dural extension versus bony detail), and both are used selectively '
                         'rather than relying on CT alone.'],
        'board_pearl': 'Image before incision: MRI for intracranial and dural extension, thin-cut '
                       'CT selectively for bony detail, and never biopsy a midline nasal mass '
                       'blindly in the office.',
        'curveball': 'How does imaging help distinguish a nasal dermoid from a nasal glial '
                     'heterotopia or an encephalocele, and why does that distinction change '
                     'management?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-nasal-dermoid-cyst',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        'focus': 'OR_prep',
        'curveball_answer': 'Imaging (particularly MRI) is used to distinguish a nasal dermoid, '
                            'which follows the prenasal/foramen cecum tract and may show a '
                            'cutaneous connection with variable intracranial extension, from a '
                            'nasal glial heterotopia (heterotopic glial tissue without a '
                            'CSF-containing communication) or an encephalocele (a herniation of '
                            'intracranial contents, often pulsatile and CSF-connected). This '
                            'distinction matters because it determines whether skull-base and '
                            'neurosurgical planning is required, and it guides safe surgical '
                            'approach so that an unrecognized encephalocele is not treated as a '
                            'simple skin lesion.'},
    {   'id': 'v462_peds_nasaldermoid_snr',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Nasal Dermoid Cyst',
        'stem': 'A child with a known nasal dermoid tract develops acute redness, tenderness, and '
                'swelling over the lesion consistent with infection, shortly before a scheduled '
                'definitive excision. The family asks whether surgery should proceed now or be '
                'delayed. Imaging previously suggested the tract approaches, but does not clearly '
                'cross, the skull base. What is the best next step in management?',
        'choices': [   'Continue simple observation indefinitely, since infection episodes will '
                       'resolve on their own and do not affect long-term risk',
                       'Treat the acute infection first when it is clinically safe to do so, then '
                       'proceed to complete excision of the cyst and tract with an approach '
                       'matched to its extent, involving skull-base and neurosurgical planning '
                       'given the suspected proximity to the skull base',
                       'Proceed with excision during the acute infection without any modification '
                       'to the surgical plan',
                       'Abandon plans for excision altogether now that infection has occurred '
                       'once'],
        'answer': 1,
        'explanation': 'Acute infection should be treated first when clinically safe, since '
                       'operating through active infection is not the preferred approach. '
                       'Observation alone does not eliminate the risk of recurrent infection or '
                       'growth, so it is not a substitute for definitive treatment. Because '
                       'imaging suggested proximity to the skull base, complete excision of the '
                       'cyst and tract should be planned with an approach matched to its extent '
                       'and with skull-base and neurosurgical planning for suspected intracranial '
                       'disease, rather than treating this as a straightforward superficial '
                       'excision.',
        'why_wrong': [   'Observation does not eliminate the risk of recurrent infection or '
                         'growth, so deferring definitive treatment indefinitely after an '
                         'infection is not appropriate management.',
                         'Correct.',
                         'Operating through active, acute infection is avoided when it can safely '
                         'be treated first; the acute infection should be addressed before '
                         'proceeding to definitive excision.',
                         'A single infection episode does not eliminate the need for definitive '
                         'treatment; the underlying cyst and tract still carry ongoing recurrence '
                         'and growth risk and, given possible skull-base proximity, warrant '
                         'complete excision with appropriate planning.'],
        'board_pearl': 'Infection is treated first when safe to do so, but it is a reason to '
                       'proceed carefully to definitive excision, not a reason to abandon it; '
                       'observation never eliminates the recurrence or growth risk of a nasal '
                       'dermoid.',
        'curveball': 'If intraoperative findings show the tract clearly crossing the skull base, '
                     'how does that change the surgical team and approach compared with a tract '
                     'that stops short of the skull base?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-nasal-dermoid-cyst',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        'focus': 'postoperative_call',
        'curveball_answer': 'Suspected or confirmed intracranial disease requires skull-base and '
                            'neurosurgical planning, meaning a tract that clearly crosses the '
                            'skull base should involve a combined otolaryngology and neurosurgical '
                            'approach so that the intracranial component can be addressed safely, '
                            'rather than being managed as an isolated extracranial excision. A '
                            'tract that stops short of the skull base can generally be managed '
                            'with an approach matched to that more limited extent, but excision '
                            'must still remove the complete cyst and tract to avoid recurrence.'},
    {   'id': 'v462_peds_hemangiomaphace_fnd',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Infantile Hemangioma / PHACE Syndrome',
        'stem': 'A 6-week-old infant has a small, bright red, raised lesion on the cheek that was '
                'not present at birth but appeared in the first weeks of life and has been growing '
                'since. The parents ask what this represents. What is the most likely diagnosis, '
                'and what is its expected natural course?',
        'choices': [   'A pigmented birthmark that will remain unchanged in size for life',
                       'A vascular malformation that is fully formed at birth and grows '
                       'proportionally with the child without a proliferative phase',
                       'Infantile hemangioma, which typically appears in early infancy, '
                       'proliferates, and then involutes over time',
                       'A bacterial skin infection requiring only oral antibiotics'],
        'answer': 2,
        'explanation': 'Infantile hemangiomas are GLUT-1-positive vascular tumors that appear in '
                       'early infancy, proliferate, and then involute, distinguishing them from '
                       'vascular malformations that are present fully formed at birth. This '
                       "lesion's timing (appearing after birth, in the first weeks of life) and "
                       'growth pattern are characteristic of infantile hemangioma rather than a '
                       'malformation or another skin process.',
        'why_wrong': [   'A pigmented birthmark does not proliferate as an actively growing red '
                         'vascular lesion in the way described.',
                         'This describes a vascular malformation, which is present fully formed at '
                         'birth, unlike infantile hemangioma, which is not fully present at birth '
                         'and instead appears in early infancy and proliferates.',
                         'Correct.',
                         "There is no description here of a bacterial infection, and this lesion's "
                         'appearance and growth pattern in early infancy are characteristic of '
                         'infantile hemangioma, not infection.'],
        'board_pearl': 'Infantile hemangiomas are not present at birth; they appear in early '
                       'infancy, proliferate, then involute, which distinguishes them from '
                       'congenital vascular malformations.',
        'curveball': 'What clinical feature would most raise concern that a hemangioma is not just '
                     'a focal skin lesion, and instead a marker for an underlying syndrome?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-infantile-hemangioma-phace-syndrome',
        'learning_stage': 'foundation',
        'ladder_reviewed': True,
        'focus': 'boards',
        'curveball_answer': 'A large segmental facial or scalp hemangioma is the feature that '
                            'raises concern for PHACE rather than representing only a cosmetic '
                            'problem. Segmental distribution, as opposed to a small focal lesion, '
                            'is associated with posterior-fossa, arterial, cardiac, eye, and '
                            'ventral developmental anomalies, which is why segmental facial '
                            'lesions prompt further syndromic evaluation.'},
    {   'id': 'v462_peds_hemangiomaphace_app',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Infantile Hemangioma / PHACE Syndrome',
        'stem': 'A 2-month-old has a large, segmental hemangioma covering much of one side of the '
                'face and extending onto the scalp. The family is eager to start oral propranolol '
                'immediately based on what they read online. Before starting treatment, what is '
                'the most appropriate next step?',
        'choices': [   'Reassure the family that no further workup is needed because segmental '
                       'distribution has no clinical significance beyond appearance',
                       'Start oral propranolol immediately at a standard starting dose with no '
                       'further evaluation, since focal lesions and segmental lesions are managed '
                       'identically',
                       'Proceed straight to surgical excision as first-line therapy for a large '
                       'segmental facial hemangioma',
                       'Obtain MRI/MRA of the head and neck, echocardiography or aortic-arch '
                       'assessment, and an ophthalmologic examination, with multidisciplinary '
                       'review, because the large segmental distribution raises concern for PHACE'],
        'answer': 3,
        'explanation': 'While typical focal lesions are clinical diagnoses that may be observed or '
                       'treated without extensive workup, a large segmental facial or scalp '
                       'hemangioma raises concern for PHACE syndrome. For PHACE risk, the '
                       'recommended workup is MRI/MRA of the head and neck, echocardiography or '
                       'aortic-arch assessment, ophthalmologic examination, and multidisciplinary '
                       'review, all performed before treatment decisions, because in PHACE the '
                       'cerebrovascular and cardiac anatomy must be assessed to allow '
                       'individualized, cautious initiation and titration of propranolol.',
        'why_wrong': [   'A large segmental facial or scalp hemangioma is specifically described '
                         'as a possible marker for PHACE syndrome, which is not merely cosmetic, '
                         'so further evaluation is required rather than reassurance alone.',
                         'Segmental lesions carrying PHACE risk are not managed identically to '
                         'typical focal lesions; the segmental distribution specifically triggers '
                         'the additional pre-treatment workup described.',
                         'Surgery has a selected role for specific indications such as urgent '
                         'focal compromise, residual deformity, ulceration, or lesions unsuitable '
                         'for medication; it is not the first-line therapy here ahead of medical '
                         'management and workup.',
                         'Correct.'],
        'board_pearl': 'A large segmental facial hemangioma is a syndrome marker, not just a '
                       'bigger version of a focal lesion, and PHACE workup should precede '
                       'propranolol initiation.',
        'curveball': 'Why does confirming or excluding PHACE-associated cerebrovascular disease '
                     'change how propranolol is initiated, compared with starting propranolol for '
                     'a typical focal hemangioma?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-infantile-hemangioma-phace-syndrome',
        'learning_stage': 'application',
        'ladder_reviewed': True,
        'focus': 'OR_prep',
        'curveball_answer': 'Oral propranolol is first-line systemic therapy for high-risk '
                            'hemangiomas, but in PHACE the cerebrovascular and cardiac anatomy '
                            'must be assessed so that initiation and titration can be '
                            'individualized and cautious, reflecting the theoretical concern that '
                            'beta-blockade could affect blood pressure and flow in the setting of '
                            'arterial or cardiac anomalies. This is different from a typical '
                            'high-risk focal hemangioma without PHACE features, where propranolol '
                            'can be started as first-line therapy without this same '
                            'cerebrovascular and cardiac anatomic assessment driving the titration '
                            'plan.'},
    {   'id': 'v462_peds_hemangiomaphace_snr',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'Infantile Hemangioma / PHACE Syndrome',
        'stem': 'An infant with a known large segmental facial hemangioma and confirmed '
                'PHACE-associated cerebrovascular disease has been started cautiously on oral '
                'propranolol with a slow, individualized titration. Several weeks later, the '
                'hemangioma has partially responded, but there is now airway compromise from an '
                'associated subglottic component, along with residual ulceration on the skin '
                'lesion. The team is deciding on next steps. What is the best approach?',
        'choices': [   'Directly assess the airway and coordinate control of the airway component, '
                       'while considering surgery or laser for the residual ulceration and lesions '
                       'unsuitable for medication, in coordination with ongoing cautious, '
                       'individualized propranolol management given the PHACE cerebrovascular '
                       'disease',
                       'Discontinue propranolol entirely and rely solely on observation, since the '
                       'lesion has already partially responded',
                       'Manage the airway compromise with tracheostomy as the only acceptable '
                       'option without further direct airway assessment',
                       'Treat only the ulceration surgically and defer any specific attention to '
                       'the airway component since the facial lesion is improving'],
        'answer': 0,
        'explanation': 'Airway disease in this setting requires direct airway assessment and '
                       'coordinated control, and this must proceed even while systemic medical '
                       'therapy for the hemangioma continues, especially given that PHACE requires '
                       'cautious, individualized propranolol dosing due to the cerebrovascular '
                       'anatomy. Surgery or laser has a selected role for indications such as '
                       'ulceration or lesions unsuitable for medication, which applies here to the '
                       'residual ulcerated component. Overall improvement of the facial lesion '
                       'does not substitute for directly addressing an airway component or '
                       'unresolved ulceration.',
        'why_wrong': [   'Correct.',
                         'Observation alone is not the described approach once airway compromise '
                         'and ulceration are present; these findings call for direct airway '
                         'assessment/coordinated control and consideration of surgery or laser for '
                         'select findings such as ulceration, not simply stopping treatment and '
                         'watching.',
                         'Airway disease requires direct airway assessment and coordinated '
                         'control; tracheostomy is not described as the only acceptable option '
                         'without first assessing the airway directly, and other interventions may '
                         'be appropriate depending on findings.',
                         'Partial improvement of the facial lesion does not mean the airway '
                         'component can be safely deferred; airway disease specifically requires '
                         'direct assessment and coordinated control regardless of how the visible '
                         'facial lesion is responding.'],
        'board_pearl': 'Improvement of the visible facial hemangioma does not mean airway or '
                       'ulceration issues can be ignored; each has its own indication for direct '
                       'assessment or intervention.',
        'curveball': 'Why does PHACE-associated cerebrovascular disease specifically make '
                     'cautious, individualized propranolol titration important, rather than just '
                     'following a single standard weight-based dosing protocol?',
        'tier': 'Curated learning ladder',
        'mode': 'Vignette',
        'concept_id': 'v6-pediatric-otolaryngology-infantile-hemangioma-phace-syndrome',
        'learning_stage': 'senior_decision',
        'ladder_reviewed': True,
        'focus': 'postoperative_call',
        'curveball_answer': 'In PHACE, cerebrovascular and cardiac anatomy must be assessed, and '
                            'propranolol initiation and titration should be individualized and '
                            'cautious, reflecting the theoretical hemodynamic concerns raised by '
                            'beta-blockade in the presence of arterial anomalies. This is why the '
                            'approach for PHACE differs from a single fixed weight-based protocol '
                            'used for a typical hemangioma without these associated vascular '
                            'findings, and why ongoing coordination with the multidisciplinary '
                            'team matters as therapy continues.'}]


def apply_deep_curriculum_ladder_pediatric_v462(data_module, app_module=None):
    existing = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(existing, list):
        raise RuntimeError("v46.2: CLINICAL_CHALLENGES_V119 unavailable")
    existing_ids = {q.get("id") for q in existing}
    added = 0
    cases = list(existing)
    for q in NEW_QUESTIONS:
        if q["id"] in existing_ids:
            raise RuntimeError(f"v46.2: duplicate id {q['id']!r}")
        cases.append(q)
        added += 1
    data_module.CLINICAL_CHALLENGES_V119 = cases
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {"questions_added": added}
