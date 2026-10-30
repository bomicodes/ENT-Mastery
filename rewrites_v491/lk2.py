# v491 rewrites: locked questions rewritten with their audits (lk2)
REWRITES = {'v254_lar_polycyst_snr': {'stem': 'A 34-year-old female voice teacher has 14 months of hoarseness and vocal fatigue '
                                   'despite 3 months of voice therapy. Stroboscopy shows a left mid-membranous '
                                   'subepithelial cyst with a segment of absent mucosal wave and a small reactive '
                                   'lesion on the right fold. During microflap dissection, the superior cyst wall is '
                                   'densely fused to the deep superficial lamina propria next to the vocal ligament, '
                                   'while the rest separates cleanly. What is the best intraoperative decision?',
                           'choices': ['Free the cyst where a plane exists and accept a tiny adherent wall remnant',
                                       'Excise the adherent wall with a 1 mm cuff of surrounding lamina propria',
                                       'Remove the overlying epithelium en bloc with the cyst to ensure clearance',
                                       'Marsupialize the cyst into the airway and leave the entire cyst wall in place'],
                           'answer': 0,
                           'explanation': 'The superficial lamina propria is the pliable cover that makes the mucosal '
                                          'wave; once it is stripped off the vocal ligament, it heals as stiff scar '
                                          'that can sound worse than the original cyst. Microflap surgery therefore '
                                          'removes the lesion in its own plane and does not take a margin, because '
                                          'this is not an oncologic resection. Where the wall is fused to the deep '
                                          'cover, a minute remnant carries a modest recurrence risk, while chasing it '
                                          'guarantees permanent vibratory loss. The reactive contralateral lesion is '
                                          'usually left to resolve with therapy.',
                           'why_wrong': ['Correct.',
                                         'A cuff of normal lamina propria is an oncologic margin concept that trades a '
                                         'benign lesion for permanent stiffness and scar.',
                                         'Sacrificing the epithelium leaves a raw surface over the vibratory edge, '
                                         'inviting web formation, fibrosis and a poorer mucosal wave.',
                                         'Leaving the whole wall of an intracordal cyst behind carries a high '
                                         'recurrence rate and does not restore normal vibration.'],
                           'board_pearl': 'Phonosurgery removes the lesion, not a margin: preserve superficial lamina '
                                          'propria, because cover scar is worse than a small remnant.',
                           'curveball': 'Six weeks later, stroboscopy shows a stiff, adynamic segment at the excision '
                                        'site without a visible bulge. How does this differ from recurrence?',
                           'curveball_answer': 'Segmental stiffness without a focal bulge points to scar or lamina '
                                               'propria loss, not a recurrent mass. Treat it with voice therapy and '
                                               'serial stroboscopy while the scar matures over months; early '
                                               're-excision only adds injury. A recurrent mass instead shows a new '
                                               'subepithelial swelling with mass effect and may warrant re-excision '
                                               'once it is confirmed.'},
 'v256_lar_rad_dys_fnd': {'stem': 'A 64-year-old man treated with chemoradiation for p16-positive tonsil cancer 6 '
                                  'years ago has slowly progressive coughing with meals, 45-minute mealtimes and 5 kg '
                                  'weight loss. Surveillance PET/CT and laryngoscopy show no recurrent tumor or '
                                  'stenosis. FEES shows heavy residue in the valleculae and pyriform sinuses, reduced '
                                  'epiglottic inversion and delayed cough after penetration. Which mechanism best '
                                  'explains his dysphagia?',
                          'choices': ['Isolated cricopharyngeal spasm with preserved pharyngeal contraction and '
                                      'hyolaryngeal excursion',
                                      'Presbyphagia from normal aging of the swallow musculature, unrelated to prior '
                                      'treatment effects',
                                      'Late radiation fibrosis and lower cranial neuropathy weakening pharyngeal and '
                                      'laryngeal motion',
                                      'Persistent mucositis and odynophagia carried over from the original '
                                      'chemoradiation treatment course'],
                          'answer': 2,
                          'explanation': 'Late radiation-associated dysphagia develops months to years after treatment '
                                         'as fibrosis stiffens the constrictors, tongue base and suprahyoid muscles, '
                                         'and late lower cranial neuropathy reduces motor drive and laryngopharyngeal '
                                         'sensory feedback. The deciding clues are diffuse residue, poor epiglottic '
                                         'inversion and a delayed cough, which show weak propulsion, reduced excursion '
                                         'and blunted sensation rather than one focal obstruction. Instrumental study '
                                         'defines the physiology, and the negative surveillance matters because '
                                         'recurrent tumor must be excluded before blaming fibrosis.',
                          'why_wrong': ['Isolated UES spasm causes residue mainly in the pyriform sinuses with good '
                                        'pharyngeal strength, not diffuse residue with weak inversion.',
                                        'Aging alone does not produce this degree of progressive residue and weight '
                                        'loss in an irradiated field; the treatment history explains it.',
                                        'Correct.',
                                        'Acute mucositis heals within weeks to months after treatment and does not '
                                        'explain a progressive problem beginning years later.'],
                          'board_pearl': 'Late radiation dysphagia is fibrosis plus neuromuscular and sensory loss; '
                                         'exclude recurrence, then define physiology instrumentally.',
                          'curveball': 'Which symptoms or findings would make recurrent tumor or chondroradionecrosis '
                                       'a competing diagnosis rather than fibrosis alone?',
                          'curveball_answer': 'New unilateral otalgia, odynophagia, hemoptysis, foul breath, a neck '
                                              'mass, a newly fixed vocal fold, laryngeal edema or exposed cartilage '
                                              'should raise recurrence or chondroradionecrosis. These features call '
                                              'for prompt endoscopy, contrast CT or PET/CT and biopsy when a target is '
                                              'seen, rather than swallow therapy for presumed fibrosis.'},
 'v256_lar_rad_dys_app': {'stem': 'A 69-year-old man treated with chemoradiation for base-of-tongue cancer 5 years ago '
                                  'has had two right lower lobe pneumonias in 6 months. He reports a wet voice after '
                                  'drinking and solids sticking in the neck. A bedside water swallow screen on the '
                                  'ward was passed. Surveillance PET/CT 1 year ago was negative, and laryngoscopy '
                                  'shows pooled secretions with no mass. Which next step best guides management?',
                          'choices': ['Serial empiric esophageal dilation, since a radiation stricture explains the '
                                      'sticking sensation',
                                      'Instrumental swallow study, with endoscopy and imaging targeted to any stenosis '
                                      'or recurrence',
                                      'Gastrostomy placement with strict NPO status to eliminate further aspiration '
                                      'pneumonia',
                                      'Repeat bedside clinical swallow evaluation using a larger 3-ounce water '
                                      'challenge'],
                          'answer': 1,
                          'explanation': 'Recurrent pneumonia years after chemoradiation suggests aspiration, and late '
                                         'radiation dysphagia often causes silent aspiration because sensation is '
                                         'reduced. A passed bedside screen therefore does not exclude it. FEES or a '
                                         'modified barium swallow shows whether the failure is residue, delayed airway '
                                         'closure, reduced excursion or poor UES opening, and which strategies work. '
                                         'The sticking sensation also warrants targeted evaluation for stenosis or '
                                         'structural recurrence, because dilation helps only a demonstrated narrow '
                                         'segment and new tumor changes everything.',
                          'why_wrong': ['Dilation treats only a demonstrated stenotic segment and does not address '
                                        'weak propulsion or poor airway protection causing the pneumonias.',
                                        'Correct.',
                                        'A feeding tube does not prevent aspiration of saliva or refluxed feeds, and '
                                        'NPO status adds disuse atrophy without defining the problem.',
                                        'Bedside screens miss silent aspiration, which is common after radiation '
                                        'because laryngopharyngeal sensation and the cough reflex are blunted.'],
                          'board_pearl': 'Recurrent pneumonia after head and neck radiation: get an instrumental '
                                         'swallow study; a passed bedside screen is not reassurance.',
                          'curveball': 'The study shows severe pharyngeal weakness with only modest UES narrowing. How '
                                       'does that change the expected value of dilation or myotomy?',
                          'curveball_answer': 'It lowers it. Dilation or cricopharyngeal myotomy improves flow only '
                                              'when a tight or noncompliant UES is the main barrier. With a weak '
                                              'pharyngeal pump, opening the UES moves little bolus and residue '
                                              'remains, so focus on targeted exercises, posture and diet strategies, '
                                              'and reserve UES procedures for clear outflow obstruction on study.'},
 'v256_lar_rad_dys_snr': {'stem': 'A 62-year-old man is 7 years disease-free after chemoradiation for laryngeal '
                                  'cancer. Despite 18 months of swallow therapy, strict NPO status and gastrostomy '
                                  'feeding, he has had four aspiration pneumonias this year, two requiring ICU care. '
                                  'FEES shows absent laryngeal sensation, poor glottic closure and continuous '
                                  'secretion aspiration. He says avoiding another ICU stay matters more to him than '
                                  'speaking with his own larynx. What is the best next step?',
                          'choices': ['Cricopharyngeal myotomy to reduce pharyngeal residue and limit the secretion '
                                      'aspiration',
                                      'Convert gastrostomy to jejunostomy feeding to stop the recurrent aspiration '
                                      'pneumonias',
                                      'Place a cuffed tracheostomy tube to seal the airway against further secretion '
                                      'aspiration',
                                      'Restage, then hold a team goals-of-care discussion about definitive '
                                      'aspiration-control surgery'],
                          'answer': 3,
                          'explanation': 'Life-threatening aspiration that persists despite optimized rehabilitation '
                                         'and nonoral feeding is the threshold for considering aspiration-prevention '
                                         'surgery such as laryngotracheal separation or functional laryngectomy. The '
                                         'deciding clues are aspiration of his own secretions, absent sensation and '
                                         'repeated ICU admissions. Because these operations are effectively '
                                         'irreversible and remove laryngeal voice, the decision first reconfirms '
                                         'cancer control and swallow physiology, then rests on multidisciplinary '
                                         'counseling built around patient priorities, which he has stated clearly.',
                          'why_wrong': ['Myotomy addresses UES outflow, not absent sensation and glottic incompetence, '
                                        'so continuous secretion aspiration would persist.',
                                        'Jejunal feeding may reduce refluxed feed aspiration but does not stop '
                                        'aspiration of saliva, which is driving his pneumonias.',
                                        'A cuff does not create a seal; secretions leak past it, and the tube can '
                                        'further impair laryngeal elevation and cough.',
                                        'Correct.'],
                          'board_pearl': 'Intractable secretion aspiration after cancer therapy: confirm disease '
                                         'control, then discuss definitive aspiration-prevention surgery with goals of '
                                         'care.',
                          'curveball': 'Which findings make laryngotracheal separation or another definitive '
                                       'aspiration-control procedure more rational than further rehabilitation trials?',
                          'curveball_answer': 'Aspiration of secretions rather than only food, absent '
                                              'laryngopharyngeal sensation, recurrent pneumonia or ICU admission '
                                              'despite NPO status and tube feeding, no meaningful gain after an '
                                              'adequate therapy trial, confirmed cancer control and a patient who '
                                              'accepts losing laryngeal voice all favor definitive surgery. Voice is '
                                              'then restored with alaryngeal methods, and surgery in the irradiated '
                                              'field needs careful wound-healing planning.'},
 'v113-oto-02': {'stem': 'A 41-year-old man has 1 year of hearing his own voice loudly in the left ear, hearing his '
                         'eye movements and footsteps, and brief oscillopsia when he coughs or hears loud music. The '
                         'tympanic membranes are normal. A 512 Hz Weber lateralizes left. Audiometry shows a left '
                         'low-frequency air-bone gap with bone thresholds of -5 dB at 250 Hz, type A tympanograms and '
                         'present acoustic reflexes. Which diagnosis best unifies these findings?',
                 'choices': ['Stapedial otosclerosis',
                             'Patulous eustachian tube',
                             'Superior canal dehiscence',
                             'Perilymphatic fistula'],
                 'answer': 2,
                 'explanation': 'A dehiscence over the superior canal creates a third mobile window. Sound energy is '
                                'shunted away from the cochlea, worsening air conduction, while the lower inner-ear '
                                'impedance improves bone conduction, sometimes below 0 dB. That produces an air-bone '
                                'gap with a normal middle ear. Bone-conduction hyperacusis explains hearing eye '
                                'movements and footsteps, and sound- or pressure-evoked canal stimulation explains '
                                'oscillopsia with coughing. Present acoustic reflexes are the key discriminator, '
                                'because the stapes still moves normally.',
                 'why_wrong': ['Otosclerosis fixes the stapes, so acoustic reflexes are absent, and it does not cause '
                               'sound-evoked oscillopsia or supranormal bone thresholds.',
                               'Patulous tube autophony involves breathing sounds and improves when lying down; it '
                               'does not create a conductive gap with present reflexes.',
                               'Correct.',
                               'A perilymph fistula causes fluctuating sensorineural loss and pressure vertigo, not '
                               "supranormal bone conduction or hearing one's own eye movements."],
                 'board_pearl': 'Air-bone gap with present acoustic reflexes and bone conduction better than 0 dB: '
                                'think third window, not otosclerosis.',
                 'curveball': 'What CT plane and physiologic test would you use to support the diagnosis before '
                              'discussing repair?',
                 'curveball_answer': 'Use submillimeter temporal-bone CT reformatted in the plane of the superior '
                                     'canal (Pöschl) and orthogonal to it (Stenvers), plus VEMP testing. A low cVEMP '
                                     'threshold or increased oVEMP amplitude supports third-window physiology. '
                                     'Symptoms, physiology and dedicated CT should agree before repair is offered, '
                                     'because CT alone can overcall a thin bony roof.'},
 'v136_oto_13': {'stem': 'A 52-year-old woman is undergoing retrosigmoid resection of a 2.5 cm vestibular schwannoma '
                         'with facial EMG monitoring. While the capsule is retracted medially near the brainstem, the '
                         'monitor begins sustained high-frequency train activity that continues for several seconds '
                         'after the retraction stops. Stimulation at 0.05 mA proximally gave a brisk response earlier '
                         'in the case. What is the best immediate response?',
                 'choices': ['Pause dissection, release retraction, irrigate, and recheck the proximal stimulation '
                             'threshold',
                             'Ask anesthesia for a dose of neuromuscular blocker to stop the train activity and keep '
                             'operating',
                             'Continue at the same site, since trains are expected during capsule handling near the '
                             'brainstem',
                             'Raise stimulation current to 2 mA to confirm a response, then resume dissection at the '
                             'same site'],
                 'answer': 0,
                 'explanation': 'Sustained trains, unlike brief bursts from contact, signal ongoing mechanical or '
                                'thermal stress on the facial nerve and correlate with postoperative weakness. '
                                'Monitoring is a closed-loop warning system: stop the provoking maneuver, release '
                                'traction, irrigate with warm saline and check whether the proximal threshold has '
                                'risen, which would indicate conduction block at the dissection site. Only after the '
                                'signal settles should the surgeon resume, possibly changing direction of dissection '
                                'or accepting a near-total resection.',
                 'why_wrong': ['Correct.',
                               'Neuromuscular blockade abolishes EMG responses, so it blinds the monitor at the moment '
                               'the nerve is under the most stress.',
                               'Sustained trains are a warning sign of nerve injury, not routine background activity, '
                               'and continuing the same maneuver compounds it.',
                               'A response at high current proves only distal excitability and can falsely reassure '
                               'while proximal conduction is failing.'],
                 'board_pearl': 'Sustained facial EMG trains: stop, release traction, irrigate, recheck threshold; '
                                'never paralyze the patient to silence the monitor.',
                 'curveball': 'After the trains settle, the resident asks how free-run EMG and stimulated thresholds '
                              'provide different information about this nerve. What do you answer?',
                 'curveball_answer': 'Free-run EMG is a continuous warning channel: bursts or trains signal '
                                     'mechanical, thermal or electrical irritation but do not quantify function. '
                                     'Stimulated EMG confirms the mapped nerve and trends the current needed for a '
                                     'response; a rising proximal threshold or lost proximal response suggests '
                                     'impaired conduction once technical causes are excluded, and a low threshold at '
                                     'closure predicts good function.'},
 'v144_oto_22': {'stem': 'A 44-year-old woman has 3 months of pulse-synchronous whooshing in the right ear. It quiets '
                         'when she presses on the right side of her neck or turns her head to the right. She has a BMI '
                         'of 38 and new morning headaches. Otoscopy shows a normal tympanic membrane, and audiometry '
                         'is symmetric and normal. Which next step is most appropriate?',
                 'choices': ['Reassurance and sound therapy, since otoscopy and audiometry are normal',
                             'Referral for cognitive behavioral therapy for bothersome tinnitus',
                             'MRI of the internal auditory canals alone, as for asymmetric tinnitus',
                             'CT venography or MRI with MRV, plus a dilated fundus examination'],
                 'answer': 3,
                 'explanation': 'The first branch point in tinnitus is pulsatile versus nonpulsatile. Pulsatile '
                                'tinnitus has a structural or vascular differential and warrants targeted imaging, '
                                'unlike symmetric nonpulsatile tinnitus. Suppression with ipsilateral jugular '
                                'compression or head turning points to a venous source, and obesity with headaches '
                                'suggests idiopathic intracranial hypertension with transverse sinus stenosis, a '
                                'dehiscent sigmoid plate or a diverticulum. Venous imaging defines these, and '
                                'fundoscopy looks for papilledema, which would threaten vision.',
                 'why_wrong': ['Normal otoscopy and hearing do not exclude venous or arterial causes of pulsatile '
                               'tinnitus, which need targeted imaging.',
                               'CBT treats distress from primary subjective tinnitus but is not a substitute for '
                               'evaluating a likely structural vascular cause.',
                               'IAC MRI looks for vestibular schwannoma and does not image the transverse and sigmoid '
                               'sinuses that this pattern implicates.',
                               'Correct.'],
                 'board_pearl': 'Pulsatile tinnitus is a separate pathway: phenotype it on exam, then image arterial '
                                'or venous causes accordingly.',
                 'curveball': 'On review, a red retrotympanic mass is now visible behind an intact drum. What '
                              'dangerous office maneuver should be avoided?',
                 'curveball_answer': 'Do not biopsy, needle or myringotomize a red retrotympanic mass in the office. A '
                                     'glomus tumor, aberrant carotid artery or high dehiscent jugular bulb can bleed '
                                     'catastrophically. Obtain temporal-bone CT and contrast MRI or angiography first '
                                     'to characterize the lesion and its vascular relationships before any '
                                     'intervention.'},
 'v124_ped_06': {'stem': 'A 14-year-old boy has had intermittent mucoid drainage from a tiny skin opening on the right '
                         'side of his neck since early childhood, with three infections treated with antibiotics. The '
                         'opening sits at the junction of the middle and lower thirds of the anterior border of the '
                         'sternocleidomastoid, and a firm cord can be felt ascending from it. The midline neck and '
                         'thyroid are normal. Which diagnosis is most likely?',
                 'choices': ['Thyroglossal duct cyst with fistula',
                             'Second branchial cleft sinus tract',
                             'Fourth branchial pouch sinus tract',
                             'Scrofulous lymphadenitis with sinus'],
                 'answer': 1,
                 'explanation': 'Second branchial cleft anomalies are the most common branchial anomalies, and their '
                                'external opening lies along the anterior border of the sternocleidomastoid, '
                                'classically in the lower third. A lifelong pit with mucoid drainage and a palpable '
                                'ascending cord is the deciding pattern. Excision follows the tract upward between the '
                                'internal and external carotid arteries, over the hypoglossal and glossopharyngeal '
                                'nerves, toward the tonsillar fossa. Infection is treated first, and complete excision '
                                'after inflammation settles prevents recurrence.',
                 'why_wrong': ['Thyroglossal duct remnants are midline and move with swallowing or tongue protrusion; '
                               'this opening is lateral along the muscle border.',
                               'Correct.',
                               'Fourth pouch anomalies usually present as left-sided recurrent neck abscess or '
                               'suppurative thyroiditis from the pyriform sinus, rarely a skin pit.',
                               'Mycobacterial lymphadenitis drains through a violaceous node in a young child, not a '
                               'lifelong pit with a cord-like tract.'],
                 'board_pearl': 'Lifelong draining pit along the lower anterior SCM border: second branchial cleft '
                                'sinus; tract runs between the carotids.',
                 'curveball': 'The tract appears to pass between the internal and external carotid arteries. Which '
                              'branchial anomaly does that course suggest, and why does it matter surgically?',
                 'curveball_answer': 'A tract between the internal and external carotid arteries is classic for a '
                                     'second branchial cleft anomaly, because it lies deep to second-arch structures '
                                     'and superficial to third-arch structures. It predicts a deep course toward the '
                                     'tonsillar fossa, placing the carotids and the hypoglossal and glossopharyngeal '
                                     'nerves at risk, so define the tract and consider stepladder incisions.'},
 'v140_ped_06': {'stem': 'A 4-month-old boy with severe laryngomalacia, poor weight gain and feeding desaturations '
                         'underwent bilateral aryepiglottic fold division and arytenoid mucosal trimming 2 days ago. '
                         'His inspiratory stridor is much improved and he is comfortable at rest. He now coughs, '
                         'chokes and desaturates to 88% during bottle feeds. He is afebrile and his chest is clear. '
                         'What is the best next step?',
                 'choices': ['Instrumental swallow study and feeding modification, such as thickened or paced feeds',
                             'Return to the operating room for revision supraglottoplasty of residual collapse',
                             'Continue standard feeds and discharge, since postoperative cough resolves on its own in '
                             'days',
                             'Start empiric high-dose acid suppression and continue the same feeding regimen'],
                 'answer': 0,
                 'explanation': 'New coughing and desaturation with feeds after supraglottoplasty, while stridor at '
                                'rest has improved, points to postoperative dysphagia and aspiration rather than '
                                'airway failure. Edema and altered supraglottic sensation can impair airway protection '
                                'for days to weeks, especially in infants with neurologic or syndromic comorbidity. An '
                                'instrumental swallow study (FEES or videofluoroscopy) defines the problem and which '
                                'consistency is safe, and feeding strategies bridge recovery.',
                 'why_wrong': ['Correct.',
                               'Stridor is improved and he is comfortable at rest, so the problem is airway protection '
                               'during feeds, not residual obstruction.',
                               'Discharging on unchanged feeds risks aspiration pneumonia when the aspiration has not '
                               'been defined or managed.',
                               'Reflux may coexist, but acid suppression does not treat impaired airway protection or '
                               'make thin liquids safe.'],
                 'board_pearl': 'Feeding cough after supraglottoplasty is usually dysphagia, not failed surgery: study '
                                'the swallow and modify feeds.',
                 'curveball': 'Which neurologic or syndromic comorbidities increase the risk of persistent aspiration '
                              'after supraglottoplasty?',
                 'curveball_answer': 'Neurologic impairment, hypotonia, cerebral palsy, developmental delay, genetic '
                                     'or craniofacial syndromes, prematurity and pre-existing dysphagia raise the '
                                     'chance that aspiration persists. Define baseline swallowing before surgery and '
                                     'counsel families that correcting supraglottic collapse does not correct '
                                     'neuromotor disease, so feeding therapy or tube feeding may still be needed.'},
 'v152_ped_01': {'stem': 'A 3-month-old girl with repaired esophageal atresia and tracheoesophageal fistula has known '
                         'severe tracheomalacia. On the ward she becomes agitated during a feed, develops a harsh '
                         'expiratory noise and turns cyanotic with SpO2 of 70%. Repositioning and face-mask oxygen do '
                         'not help, and she has marked chest wall effort with poor air movement. What is the immediate '
                         'management priority?',
                 'choices': ['Give nebulized albuterol to reverse the bronchospasm causing her harsh expiratory noise',
                             'Take her straight to the OR for rigid bronchoscopy to define the collapsing segment',
                             'Calm her and give bag-mask positive pressure with PEEP while calling the airway team',
                             'Give nebulized racemic epinephrine and dexamethasone for presumed airway edema'],
                 'answer': 2,
                 'explanation': 'This is a dying spell: agitation raises intrathoracic pressure, the malacic trachea '
                                'collapses in expiration, and hypoxemia drives more agitation. Positive pressure with '
                                'PEEP acts as a pneumatic stent that holds the airway open, so calming the infant and '
                                'applying bag-mask CPAP is the immediate rescue. Senior airway and ICU help is called '
                                'in parallel, with intubation if positive pressure fails. Recurrent events then drive '
                                'dynamic evaluation and consideration of aortopexy or tracheopexy.',
                 'why_wrong': ['Beta-agonists relax airway smooth muscle and can worsen dynamic collapse in malacia; '
                               'this noise is expiratory collapse, not bronchospasm.',
                               'Diagnostic bronchoscopy matters later, but moving a hypoxemic infant to the OR delays '
                               'the pneumatic stenting she needs now.',
                               'Correct.',
                               'Racemic epinephrine and steroids treat subglottic edema or croup, which do not explain '
                               'expiratory collapse in known tracheomalacia.'],
                 'board_pearl': 'Tracheomalacia dying spell: positive pressure is the pneumatic stent; avoid '
                                'beta-agonists, which can worsen collapse.',
                 'curveball': 'Bronchoscopy later shows dominant anterior vascular compression. Which operative '
                              'concept becomes particularly relevant?',
                 'curveball_answer': 'Dominant anterior vascular compression shifts treatment toward relieving that '
                                     'relationship, often aortopexy and/or anterior tracheopexy, rather than posterior '
                                     'tracheopexy alone, which addresses posterior membrane intrusion. Define the '
                                     'vascular anatomy with dynamic bronchoscopy and CT angiography or '
                                     'echocardiography before choosing the operation.'},
 'v243_ped_tm_fnd': {'stem': 'An 8-month-old boy has a harsh barking cough, expiratory wheeze that does not improve '
                             'with albuterol, and noisy breathing that worsens with crying and colds. Inspiration is '
                             'quiet. Awake flexible laryngoscopy is normal. Bronchoscopy under spontaneous ventilation '
                             'shows normal C-shaped rings but more than 50% anterior-posterior narrowing of the distal '
                             'trachea during expiration and cough, with full reopening on inspiration. Which diagnosis '
                             'is most likely?',
                     'choices': ['Congenital tracheal stenosis',
                                 'Primary tracheomalacia',
                                 'Reactive airway disease',
                                 'Subglottic stenosis'],
                     'answer': 1,
                     'explanation': 'Tracheomalacia is excessive dynamic collapse of the tracheal wall. Intrathoracic '
                                    'airways narrow in expiration as pleural pressure rises, so an intrathoracic '
                                    'malacic segment gives expiratory noise, a barking cough and wheeze that '
                                    'bronchodilators do not relieve. The deciding clue is dynamic collapse that '
                                    'reopens on inspiration with normal rings, seen on bronchoscopy with preserved '
                                    'spontaneous breathing. Many mild cases improve with growth as the cartilage '
                                    'stiffens.',
                     'why_wrong': ['Congenital stenosis from complete rings is a fixed narrowing that does not reopen '
                                   'on inspiration, and the rings here are normal C-shaped cartilage.',
                                   'Correct.',
                                   'Asthma-type wheeze responds to bronchodilators, whereas this wheeze is unchanged '
                                   'and bronchoscopy shows dynamic tracheal collapse.',
                                   'Subglottic stenosis is extrathoracic and fixed, producing biphasic or inspiratory '
                                   'stridor rather than isolated expiratory collapse.'],
                     'board_pearl': 'Expiratory wheeze unresponsive to bronchodilators plus barky cough in an infant: '
                                    'suspect tracheomalacia; confirm with dynamic bronchoscopy.',
                     'curveball': 'An outside bronchoscopy done under deep anesthesia with positive-pressure '
                                  'ventilation was read as normal. Why can that study underestimate or alter malacia?',
                     'curveball_answer': 'Deep anesthesia reduces respiratory effort, and positive-pressure '
                                         'ventilation acts as a stent that holds the airway open, masking the '
                                         'spontaneous expiratory collapse that defines malacia. Dynamic bronchoscopy '
                                         'should be done with spontaneous breathing preserved, assessing the airway '
                                         'through the respiratory cycle and with cough when possible.'},
 'v242_ped_ear_app': {'stem': 'A 30-month-old girl has had mild left ear pain for 1 day, controlled with ibuprofen, '
                              'and a temperature of 38.2 C. The left tympanic membrane is bulging, opaque and '
                              'immobile, and the right is normal. There is no otorrhea, no antibiotic use in the past '
                              'month and no penicillin allergy. Her parents can return or call any time and would '
                              'rather avoid antibiotics if that is safe. What is the best management?',
                      'choices': ['Amoxicillin-clavulanate for 10 days, because bulging confirms bacterial AOM',
                                  'Ofloxacin otic drops alone to treat the middle ear without systemic exposure',
                                  'Analgesia only, with a recheck in 3 months for persistent middle-ear fluid',
                                  'Analgesia with observation for 48-72 hours and a rescue amoxicillin plan'],
                      'answer': 3,
                      'explanation': 'This is nonsevere unilateral AOM: mild otalgia for less than 48 hours and '
                                     'temperature below 39 C in a child older than 24 months. The AAP guideline allows '
                                     'either immediate antibiotics or initial observation with a defined rescue plan '
                                     'through shared decision-making when follow-up is reliable. Pain control comes '
                                     'first in both pathways. Amoxicillin is started if she worsens or fails to '
                                     'improve within 48-72 hours. This is a disease-treatment decision, not a tube '
                                     'question.',
                      'why_wrong': ['Antibiotics are acceptable but not required here, and amoxicillin, not '
                                    'amoxicillin-clavulanate, is first-line without recent amoxicillin use.',
                                    'Topical drops do not reach the middle ear through an intact tympanic membrane, so '
                                    'they do not treat AOM.',
                                    'A 3-month recheck is the watchful-waiting plan for OME; acute infection needs a '
                                    '48-72 hour safety net.',
                                    'Correct.'],
                      'board_pearl': 'Nonsevere AOM at 24 months or older: observation with a 48-72 hour rescue plan '
                                     'or immediate amoxicillin are both valid.',
                      'curveball': 'How would bilateral disease in a 12-month-old, otorrhea, severe otalgia, fever of '
                                   '39 C or higher, or unreliable follow-up change the plan?',
                      'curveball_answer': 'Each removes the observation option. Children 6 months or older with '
                                          'otorrhea or severe symptoms, and those 6 to 23 months with bilateral AOM, '
                                          'should receive immediate antibiotics. Unreliable follow-up also favors '
                                          'immediate treatment. Use high-dose amoxicillin, for 10 days if younger than '
                                          '2 years or severe.'},
 'v242_ped_ear_snr': {'stem': 'A 5-year-old boy started amoxicillin 4 days ago for right acute otitis media. He now '
                              'has a temperature of 39.4 C, worsening pain, and right postauricular erythema and '
                              'tenderness with the auricle pushed forward and outward and the postauricular crease '
                              'lost. There is no fluctuance, facial weakness, headache, neck stiffness or lethargy. '
                              'The right tympanic membrane is bulging. What is the best next step?',
                      'choices': ['Switch to high-dose amoxicillin-clavulanate and recheck in clinic within 48-72 '
                                  'hours',
                                  'Proceed directly to cortical mastoidectomy before giving any intravenous '
                                  'antibiotics',
                                  'Admit for IV antibiotics and urgent ENT care, with myringotomy and contrast CT by '
                                  'response',
                                  'Obtain brain MRI with venography and hold antibiotics until the imaging is '
                                  'reviewed'],
                      'answer': 2,
                      'explanation': 'Postauricular erythema, tenderness and auricular protrusion after AOM define '
                                     'acute mastoiditis, a complication rather than ordinary treatment failure. The '
                                     'child is admitted for IV antibiotics with early ENT involvement. Myringotomy, '
                                     'often with a tube, drains the middle ear and provides culture. Contrast CT is '
                                     'obtained when abscess or intracranial complication is suspected or when he fails '
                                     'to improve within about 48 hours. Many uncomplicated cases settle without '
                                     'mastoidectomy, and imaging findings guide escalation to drainage or surgery.',
                      'why_wrong': ['Outpatient oral escalation treats this as routine AOM failure and undertreats an '
                                    'established mastoid infection with postauricular signs.',
                                    'Uncomplicated mastoiditis often responds to IV antibiotics and middle-ear '
                                    'drainage; mastoidectomy is reserved for abscess, complication or failure.',
                                    'Correct.',
                                    'Antibiotics should not be delayed for imaging in a febrile child, and MRV is for '
                                    'suspected sinus thrombosis, which is not yet suggested.'],
                      'board_pearl': 'Acute mastoiditis: admit, give IV antibiotics, drain the middle ear, and image '
                                     'for suspected complications or poor response.',
                      'curveball': 'Which findings would prompt urgent contrast imaging and earlier drainage or '
                                   'mastoidectomy rather than IV antibiotics alone?',
                      'curveball_answer': 'Postauricular fluctuance suggesting subperiosteal abscess, facial palsy, '
                                          'abducens palsy or retro-orbital pain, vertigo, severe headache, neck '
                                          'stiffness, lethargy or other neurologic signs, or no improvement after '
                                          'about 48 hours of IV therapy. Obtain contrast CT, adding MRI or MRV for '
                                          'intracranial or sinus thrombosis concerns, and proceed to drainage, tube '
                                          'placement and mastoidectomy as the findings dictate.'},
 'v243_ped_sgh_snr': {'stem': 'A 3-month-old girl with a chin and lower-lip hemangioma has a posterolateral subglottic '
                              'hemangioma narrowing the airway by about 60% on endoscopy. After 3 weeks of propranolol '
                              'at 2 mg/kg/day, taken reliably and well tolerated, her biphasic stridor and retractions '
                              'are worsening, and she desaturates to 85% with feeds despite high-flow nasal cannula in '
                              'the PICU. What is the best escalation?',
                      'choices': ['Operative airway endoscopy with airway control and adjunctive treatment planned',
                                  'Double the propranolol dose and continue high-flow support while awaiting effect',
                                  'Circumferential CO2 laser ablation of the subglottis as the definitive rescue',
                                  'Add oral prednisolone and discharge home with continuous pulse oximetry'],
                      'answer': 0,
                      'explanation': 'Progressive obstruction despite an adequate, tolerated propranolol course means '
                                     'medical therapy is not controlling this lesion fast enough. Physiologic '
                                     'compromise overrides watchful continuation. The safe step is a controlled airway '
                                     'assessment in the OR to secure the airway and reassess the lesion, with adjuncts '
                                     'such as intralesional steroid, targeted debulking or a temporary tracheostomy if '
                                     'needed, while propranolol continues. Lesions that do not respond should also '
                                     'prompt reconsideration of the diagnosis.',
                      'why_wrong': ['Correct.',
                                    'Propranolol is dosed at 2 to 3 mg/kg/day; doubling adds bradycardia, hypotension '
                                    'and hypoglycemia risk without securing a failing airway.',
                                    'Circumferential laser injury of the infant subglottis carries a high risk of '
                                    'subglottic stenosis and is not appropriate rescue therapy.',
                                    'Discharging an infant who is desaturating on high-flow support is unsafe, and '
                                    'adding steroids does not secure the airway.'],
                      'board_pearl': 'Propranolol is first-line for airway hemangioma; worsening obstruction despite '
                                     'it needs operative airway assessment and rescue planning.',
                      'curveball': 'Her parents ask whether surgery can be avoided entirely. Which findings would make '
                                   'tracheostomy or operative debulking reasonable despite propranolol?',
                      'curveball_answer': 'Escalate beyond propranolol when airway compromise is unstable, the drug is '
                                          'contraindicated or not tolerated, or an adequate course fails to control a '
                                          'focal obstructing lesion. Endoscopic debulking or open excision can give '
                                          'rapid relief for selected focal lesions; tracheostomy is a rescue or bridge '
                                          'for otherwise unmanageable obstruction rather than routine first-line '
                                          'treatment.'},
 'v245_ped_hl_app': {'stem': 'A 5-month-old girl failed automated ABR newborn screening in both ears. Diagnostic ABR '
                             'at 2 months showed bilateral moderately severe sensorineural loss with absent OAEs and '
                             'normal tympanometry, and hearing aids were fitted at 3 months. Newborn dried blood spot '
                             'CMV PCR was negative. She was born at term, has no dysmorphic features, and there is no '
                             'family history of hearing loss. Which next step in her etiologic evaluation is most '
                             'appropriate?',
                     'choices': ['High-resolution temporal-bone CT as the first etiologic test, before any genetic '
                                 'testing',
                                 'Broad laboratory screen including thyroid, syphilis, autoimmune and renal studies',
                                 'Repeat ABR at 12 months to confirm the loss before starting etiologic evaluation',
                                 'Comprehensive hearing-loss gene panel and ophthalmology referral, with ongoing '
                                 'amplification'],
                     'answer': 3,
                     'explanation': 'Genetic causes account for about half of congenital sensorineural loss, and '
                                    'comprehensive gene panels have the highest diagnostic yield in nonsyndromic '
                                    'infants once congenital CMV is excluded, which it was here. Ophthalmology screens '
                                    'for Usher syndrome and other eye findings that change counseling. Imaging is '
                                    'selected for cochlear implant planning or when genetics is unrevealing. '
                                    'Throughout, amplification and early intervention continue, because language '
                                    'access cannot wait for an etiology.',
                     'why_wrong': ['CT is targeted rather than first-line, chosen for implant planning or unrevealing '
                                   'genetics, and adds radiation without changing initial care.',
                                   'Untargeted laboratory panels have very low yield in nonsyndromic infant hearing '
                                   'loss and are not recommended routinely.',
                                   'The loss is already confirmed and aided; delaying the etiologic workup gains '
                                   'nothing and can miss actionable diagnoses.',
                                   'Correct.'],
                     'board_pearl': 'Infant SNHL with negative CMV: comprehensive genetic testing first, ophthalmology '
                                    'screening, imaging when it changes management.',
                     'curveball': 'How would auditory neuropathy physiology change counseling about behavioral '
                                  'thresholds and cochlear implantation?',
                     'curveball_answer': 'Auditory neuropathy preserves OAEs or the cochlear microphonic while ABR '
                                         'synchrony is absent or abnormal, so behavioral thresholds can fluctuate and '
                                         'speech understanding is often much worse than the audiogram predicts. '
                                         'Counsel around functional language access, and consider implantation for '
                                         'persistently poor benefit from amplification rather than threshold alone.'},
 'v246_ped_tubes_fnd': {'stem': 'A healthy 3-year-old boy with normal development has bilateral otitis media with '
                                'effusion first documented 4 months ago. Both tympanic membranes remain dull and '
                                'immobile, with type B tympanograms. Age-appropriate audiometry shows a 35 dB '
                                'conductive hearing loss in both ears, and his parents notice he turns the television '
                                'up. He has had no acute infections this year. What is the best management?',
                        'choices': ['Prescribe a 3-month course of intranasal steroid spray',
                                    'Offer bilateral tympanostomy tubes after counseling',
                                    'Continue watchful waiting with recheck in 3 to 6 months',
                                    'Adenoidectomy with myringotomy, without tube placement'],
                        'answer': 1,
                        'explanation': 'Bilateral OME lasting 3 months or longer with documented hearing difficulty is '
                                       'the core guideline indication for offering bilateral tympanostomy tubes. The '
                                       'deciding clues are chronicity plus functional consequence, not the presence of '
                                       'fluid at one visit. Watchful waiting is appropriate for OME under 3 months or '
                                       'chronic OME without hearing loss or symptoms. Medical therapies do not clear '
                                       'effusion durably, and adenoidectomy is not routine for a first surgery in a '
                                       'child under 4 without a separate adenoid indication.',
                        'why_wrong': ['Intranasal and systemic steroids are not recommended for OME because any '
                                      'benefit is short-lived and does not prevent surgery.',
                                      'Correct.',
                                      'Surveillance fits chronic OME without hearing loss; with documented bilateral '
                                      'hearing difficulty, tubes should be offered.',
                                      'Myringotomy alone closes within days, and adenoidectomy is not added for a '
                                      'first surgery under 4 years without an adenoid indication.'],
                        'board_pearl': 'Bilateral OME for 3 months or longer with documented hearing difficulty: offer '
                                       'bilateral tympanostomy tubes.',
                        'curveball': 'How would a baseline speech-language delay or another developmental risk factor '
                                     'lower your threshold for intervention?',
                        'curveball_answer': 'An at-risk child, such as one with speech-language delay, autism, Down '
                                            'syndrome, craniofacial anomaly or permanent hearing loss, should have '
                                            'hearing tested promptly when OME is diagnosed rather than after 3 months. '
                                            'Tubes are an option when the effusion is unlikely to resolve quickly, '
                                            'because even mild fluctuating loss can compound baseline communication '
                                            'vulnerability.'},
 'v246_ped_tubes_app': {'stem': 'A 2-year-old boy has had four episodes of acute otitis media in the past 6 months, '
                                'each diagnosed by his pediatrician with a bulging drum and treated with antibiotics; '
                                'the last was 5 weeks ago. Today both tympanic membranes are translucent and mobile, '
                                'tympanograms are type A, and there is no middle-ear effusion in either ear. '
                                'Development and hearing are normal. His parents request tubes. What is the best '
                                'recommendation?',
                        'choices': ['Defer tubes and reexamine at the next episode or if effusion develops',
                                    'Offer bilateral tubes, since the episode history meets recurrent AOM criteria',
                                    'Start daily amoxicillin prophylaxis through the respiratory virus season',
                                    'Adenoidectomy alone to reduce the frequency of future otitis episodes'],
                        'answer': 0,
                        'explanation': 'Recurrent AOM becomes a tube indication only when middle-ear effusion is '
                                       'present in one or both ears at the candidacy examination. The 2022 guideline '
                                       'recommends against tubes for recurrent AOM with no middle-ear effusion, '
                                       'because these children often have normal tube function between episodes and '
                                       "gain little. The deciding clue is today's normal ears and type A tympanograms. "
                                       'Reassessment during or soon after the next episode can show whether effusion '
                                       'persists.',
                        'why_wrong': ['Correct.',
                                      'The episode count alone is not enough; without effusion at assessment, the '
                                      'guideline recommends against tympanostomy tubes.',
                                      'Long-term prophylactic antibiotics are not recommended for recurrent AOM '
                                      'because of resistance, adverse effects and modest benefit.',
                                      'Adenoidectomy is not a first procedure for recurrent AOM in a 2-year-old '
                                      'without a separate nasal or adenoid indication.'],
                        'board_pearl': 'Recurrent AOM with no middle-ear effusion at the candidacy visit: do not place '
                                       'tubes; reassess at the next episode.',
                        'curveball': 'How would the recommendation change if unilateral or bilateral effusion were '
                                     'present at the candidacy visit?',
                        'curveball_answer': 'Then the guideline recommends offering bilateral tympanostomy tubes, even '
                                            'when the effusion is only in one ear, because current effusion marks '
                                            'ongoing middle-ear disease. Counsel about otorrhea, treated with topical '
                                            'drops, early extrusion, persistent perforation and the possibility of '
                                            'repeat tubes.'},
 'v246_ped_tubes_snr': {'stem': 'A 4-year-old girl with Down syndrome has had bilateral otitis media with effusion for '
                                'at least 6 months, with type B tympanograms and narrow ear canals. Her expressive '
                                'language is well behind her receptive skills, and speech therapy notes inconsistent '
                                'responses. One audiogram today shows only a mild 25 dB conductive loss, and her '
                                'parents ask whether surgery can wait. What is the best recommendation?',
                        'choices': ['Defer tubes until repeat audiometry shows a conductive loss greater than 40 dB',
                                    'Place long-term T-tubes as the first set, since Down syndrome predicts prolonged '
                                    'dysfunction',
                                    'Offer short-term tubes given her developmental risk, with close audiology '
                                    'follow-up',
                                    'Perform myringotomy with aspiration only, avoiding tubes in her narrow ear '
                                    'canals'],
                        'answer': 2,
                        'explanation': 'Children with Down syndrome are at increased risk for speech and language '
                                       'problems, so persistent OME carries a disproportionate developmental cost and '
                                       'tubes are a guideline option when the effusion is unlikely to resolve. '
                                       'Fluctuating loss, a type B pattern for 6 months and the language gap matter '
                                       'more than one mild audiogram. A short-term tube remains the default first '
                                       'choice, with close audiologic follow-up, while hearing aids are a reasonable '
                                       'alternative when tubes are not feasible.',
                        'why_wrong': ['Waiting for a larger threshold ignores her at-risk status and fluctuating loss, '
                                      'which already threaten language development.',
                                      'Long-term tubes carry higher perforation and otorrhea rates and are reserved '
                                      'for repeat surgery or a specific need, not routine first placement.',
                                      'Correct.',
                                      'Myringotomy alone closes within days and does not provide durable ventilation '
                                      'for chronic effusion.'],
                        'board_pearl': 'At-risk children with persistent OME: judge by developmental and hearing '
                                       'trajectory, not one mild audiogram; tubes are an option.',
                        'curveball': 'When would concurrent adenoidectomy become reasonable in a child undergoing '
                                     'repeat tube surgery?',
                        'curveball_answer': 'Adenoidectomy is reasonable with repeat tubes, or with a first set at age '
                                            '4 or older, because it lowers the chance of further OME and repeat '
                                            'surgery. It is also indicated for separate adenoid problems such as nasal '
                                            'obstruction or chronic adenoiditis. In Down syndrome, also screen for '
                                            'obstructive sleep apnea and take cervical spine precautions.'},
 'v246_ped_cranio_fnd': {'stem': 'A 10-month-old girl with an isolated, unrepaired cleft of the soft and hard palate '
                                 'is seen before palatoplasty. Both tympanic membranes are dull, retracted and '
                                 'immobile, tympanograms are type B, and ABR shows mild bilateral conductive loss. The '
                                 'external ears and canals are normal, and she has had no acute ear infections. Which '
                                 'mechanism best explains her middle-ear disease?',
                         'choices': ['Adenoid hypertrophy blocking the torus tubarius and both eustachian tube '
                                     'orifices',
                                     'Abnormal tensor veli palatini insertion impairing active eustachian tube opening',
                                     'Congenital ossicular fixation that occurs together with clefting of the palate',
                                     'Recurrent bacterial otitis from impaired mucosal immunity in clefting syndromes'],
                         'answer': 1,
                         'explanation': 'The tensor veli palatini is the main active dilator of the eustachian tube, '
                                        'and it normally pulls on a continuous palatal aponeurosis. In cleft palate it '
                                        'inserts along the cleft margin instead, so each swallow fails to open the '
                                        'tube. Middle-ear gas is absorbed, negative pressure develops, and effusion '
                                        'follows, which is why OME is nearly universal. The deciding clues are '
                                        'retracted drums and type B tympanograms without acute infections. Tubes are '
                                        'often placed at palatoplasty, but repair does not reliably cure the '
                                        'dysfunction.',
                         'why_wrong': ['Infant adenoids are small, and OME in cleft palate stems from tube muscle '
                                       'dysfunction rather than mechanical blockage by lymphoid tissue.',
                                       'Correct.',
                                       'Ossicular fixation causes a conductive loss with a normal, mobile drum, not '
                                       'retracted immobile drums with type B tympanograms.',
                                       'She has had no acute infections; the disease here is persistent effusion from '
                                       'ventilation failure, not recurrent bacterial otitis.'],
                         'board_pearl': 'Cleft palate OME: the tensor veli palatini cannot open the eustachian tube; '
                                        'palate repair does not reliably fix it.',
                         'curveball': 'Why does this physiology make longitudinal audiology important even after an '
                                      'initially successful set of tubes?',
                         'curveball_answer': 'Palatal muscle dysfunction can sustain eustachian-tube dysfunction '
                                             'through childhood, so effusion can recur after a tube extrudes even when '
                                             'the first set restored hearing. Longitudinal audiology detects recurrent '
                                             'conductive loss during speech-language development and guides further '
                                             'ventilation or hearing support, while serial otoscopy watches for '
                                             'retraction pockets and cholesteatoma.'},
 'v136_rhi_04': {'stem': 'An 11-year-old boy has had a daily wet cough since infancy and needed oxygen in the NICU for '
                         'respiratory distress despite a term birth. He has had three sets of ear tubes for chronic '
                         'otorrhea. CT shows pansinusitis, chest CT shows bronchiectasis, and his heart and abdominal '
                         'organs are normally positioned. Sweat chloride is 18 mmol/L. Which evaluation is most '
                         'appropriate next?',
                 'choices': ['Saccharin transit test to measure mucociliary clearance time across the nasal cavity',
                             'Skin-prick testing to inhalant allergens with a serum total IgE measurement',
                             'Complete bilateral FESS now, since diffuse sinus disease is the main driver',
                             'Nasal nitric oxide measurement with genetic testing for primary ciliary dyskinesia'],
                 'answer': 3,
                 'explanation': 'Lifelong wet cough, unexplained neonatal respiratory distress at term, chronic '
                                'otitis, pansinusitis and bronchiectasis form the classic primary ciliary dyskinesia '
                                'phenotype. A normal sweat chloride makes cystic fibrosis unlikely, so the next step '
                                'is a PCD-specific evaluation. Nasal nitric oxide is markedly low in most PCD and is a '
                                'good screening test in cooperative children, and genetic panels, high-speed video '
                                'microscopy and ciliary electron microscopy confirm it. Normal organ position does not '
                                'exclude PCD, because only about half have situs inversus.',
                 'why_wrong': ['The saccharin test needs prolonged cooperation, is unreliable in children and cannot '
                               'establish PCD; it has been replaced by specific testing.',
                               'Allergy testing does not explain neonatal distress, bronchiectasis and lifelong wet '
                               'cough, which point to a mucociliary disorder.',
                               'Surgery may later improve drainage and topical access, but it does not diagnose or '
                               'correct the underlying ciliary defect.',
                               'Correct.'],
                 'board_pearl': 'Early CRS with bronchiectasis, neonatal distress and chronic otitis: think CF or PCD; '
                                'normal sweat chloride turns to nasal NO.',
                 'curveball': 'His younger sister has the same respiratory history. What laterality finding on her '
                              'chest radiograph would point to Kartagener syndrome?',
                 'curveball_answer': 'Situs inversus totalis occurs in about half of patients with primary ciliary '
                                     'dyskinesia, because nodal cilia set left-right asymmetry in the embryo; its '
                                     'combination with sinusitis and bronchiectasis is Kartagener syndrome. Heterotaxy '
                                     'with congenital heart disease can also occur, and normal laterality does not '
                                     'exclude PCD.'},
 'v136_rhi_17': {'stem': 'A 47-year-old woman has 3 months of deep right-sided headache and posterior nasal drainage. '
                         'In clinic, you pass a 0 degree endoscope along the floor, then medial to the middle '
                         'turbinate toward the choana, looking for purulence from the right sphenoid. The septum is '
                         'straight and the posterior middle turbinate is visible. Where is the natural sphenoid ostium '
                         'most reliably found?',
                 'choices': ['Lateral to the middle turbinate, behind the ethmoid bulla face',
                             'In the inferior meatus, under the anterior inferior turbinate',
                             'Medial to the superior turbinate, about 1.5 cm above the choana',
                             'Lateral to the superior turbinate, inside the posterior superior meatus'],
                 'answer': 2,
                 'explanation': 'The sphenoid drains into the sphenoethmoidal recess, the narrow space between the '
                                'septum and the superior turbinate. Its natural ostium lies medial to the posterior '
                                'superior turbinate, roughly 1 to 1.5 cm above the choanal arch along the face of the '
                                'sphenoid. Following the choana upward along the septum and identifying the superior '
                                'turbinate are therefore the key steps. Posterior ethmoid cells drain lateral to the '
                                'superior turbinate into the superior meatus, which is a common source of confusion.',
                 'why_wrong': ['Behind the bulla lies the retrobullar recess of the middle meatus, which drains '
                               'anterior ethmoid cells rather than the sphenoid.',
                               'The inferior meatus receives the nasolacrimal duct at Hasner valve; no sinus drains '
                               'there.',
                               'Correct.',
                               'The superior meatus drains the posterior ethmoid cells; the sphenoid ostium is medial '
                               'to the superior turbinate.'],
                 'board_pearl': 'The sphenoid ostium sits medial to the superior turbinate in the sphenoethmoidal '
                                'recess, above the choana.',
                 'curveball': 'If she later needs sphenoidotomy with inferior enlargement of this ostium, which major '
                              'artery is at risk posteriorly near the sphenopalatine foramen?',
                 'curveball_answer': 'The sphenopalatine artery exits the sphenopalatine foramen behind the posterior '
                                     'attachment of the middle turbinate. Its posterior lateral nasal branch and the '
                                     'posterior septal branch, which crosses the sphenoid face below the ostium, '
                                     'should be anticipated when enlarging the sphenoid inferiorly or working near the '
                                     'posterior middle turbinate.'},
 'v208_rhi_anat_snr': {'stem': 'A 55-year-old man with recurrent polyps is undergoing his third endoscopic sinus '
                               'surgery. The middle turbinate was partially resected before, and polyps and scar have '
                               'erased the usual middle-meatal landmarks. A thin horizontal partition lies above the '
                               'posterior ethmoid dissection, and you cannot tell whether it is a residual cell wall '
                               'or skull base. Navigation registered with 2.5 mm accuracy. What is the safest next '
                               'move?',
                       'choices': ['Remove the partition if the navigation probe tip reads just below the skull base',
                                   'Stop and re-localize from fixed landmarks such as the maxillary roof and sphenoid',
                                   'Clear the partition with a microdebrider, since its thinness suggests a cell wall',
                                   'End the operation and treat medically, since the revision anatomy is too '
                                   'distorted'],
                       'answer': 1,
                       'explanation': 'Revision surgery removes the landmarks primary surgery relies on, so loss of '
                                      'orientation near the skull base is a reason to stop and re-map rather than push '
                                      'on. Fixed structures survive: the maxillary sinus roof marks the orbital floor '
                                      'and a safe height, the medial orbital wall stays lateral, and the sphenoid '
                                      'sinus can be entered low and medially to find the skull base. That skull base '
                                      'is then followed posterior to anterior. Navigation supplements this but cannot '
                                      'resolve a structure within its own error margin.',
                       'why_wrong': ['Registration error of a few millimeters is larger than the margin at the skull '
                                     'base, so the probe alone cannot clear the partition.',
                                     'Correct.',
                                     'Thinness does not distinguish a cell wall from skull base, and a powered '
                                     'instrument there risks CSF leak and intracranial injury.',
                                     'Orientation can usually be re-established safely from fixed landmarks; '
                                     'abandoning the case leaves treatable disease and repeats the risk later.'],
                       'board_pearl': 'Lost orientation in revision ESS: stop, re-establish fixed landmarks, find '
                                      'skull base in the sphenoid, and work posterior to anterior.',
                       'curveball': 'The resident asks which fixed landmarks remain especially useful in a cavity like '
                                    'this, after prior uncinectomy and ethmoidectomy. What do you teach?',
                       'curveball_answer': 'The maxillary sinus roof seen through a wide antrostomy marks the orbital '
                                           'floor height; the medial orbital wall defines the lateral limit; the '
                                           'choana and sphenoid face lead to the sphenoid ostium and skull base; and '
                                           'the septum stays medial. Identify the skull base in the sphenoid or '
                                           'posterior ethmoid first, then follow it anteriorly.'},
 'v136_rhi_21': {'stem': 'A 5-year-old girl has had 4 months of daily purulent rhinorrhea, nasal obstruction, snoring '
                         'and nighttime cough despite saline, an intranasal steroid and two antibiotic courses. '
                         'Endoscopy shows a large adenoid filling most of the choanae with purulent debris, and mild '
                         'middle-meatal edema without polyps. She grows normally and has no lower-airway disease or '
                         'unusual infections. What is the most appropriate first surgical step?',
                 'choices': ['Adenoidectomy, with or without maxillary sinus irrigation',
                             'Bilateral balloon dilation of the maxillary sinus ostia',
                             'Bilateral maxillary antrostomies and anterior ethmoidectomies',
                             'Inferior turbinate reduction to improve nasal airflow'],
                 'answer': 0,
                 'explanation': 'In younger children, the adenoid is both a bacterial reservoir, often carrying '
                                'biofilm, and a cause of posterior nasal obstruction, so removing it improves many '
                                'cases of medically refractory pediatric CRS. The deciding clues are failed '
                                'appropriate medical therapy, a large infected adenoid and no polyps or host disorder '
                                'that would change the pathway. Maxillary irrigation with culture can be added. '
                                'Endoscopic sinus surgery is reserved for persistent, objectively confirmed disease '
                                'after adenoid-directed treatment.',
                 'why_wrong': ['Correct.',
                               'Balloon dilation is not a default first operation in children and does not treat the '
                               'adenoid reservoir driving her symptoms.',
                               'Formal sinus surgery is a later step for disease that persists after adenoidectomy, '
                               'not the first operation in a typical young child.',
                               'Turbinate reduction does not address the purulent adenoid or the sinus inflammation '
                               'causing her chronic drainage and cough.'],
                 'board_pearl': 'Medically refractory pediatric CRS in a young child: adenoidectomy, often with '
                                'maxillary irrigation, comes before ESS.',
                 'curveball': 'What history would make CF or PCD evaluation important before escalating surgery?',
                 'curveball_answer': 'Nasal polyps in a child, which suggest CF until proven otherwise, Pseudomonas '
                                     'cultures, failure to thrive or steatorrhea, neonatal respiratory distress at '
                                     'term, chronic wet cough or bronchiectasis, situs anomalies and chronic otorrhea '
                                     'all warrant a host evaluation. That means sweat chloride or CFTR genetics, and '
                                     'nasal nitric oxide with genetic testing for PCD.'},
 'v144_rh_17': {'stem': 'A 7-year-old boy has 6 months of nasal obstruction, mouth breathing and thick postnasal '
                        'drainage despite daily saline, an intranasal steroid and a 3-week antibiotic course. A '
                        'lateral neck radiograph shows a large adenoid, and endoscopy confirms adenoid hypertrophy '
                        'with mucopurulence. CT shows mild maxillary and ethmoid mucosal thickening. His parents ask '
                        'about the sinus surgery they read about online. Which plan is most appropriate?',
                'choices': ['Six more weeks of oral antibiotics before any surgical discussion',
                            'Endoscopic sinus surgery directed by the CT, with adenoid sparing',
                            'Repeat sinus CT in 3 months to decide whether surgery is warranted',
                            'Adenoidectomy with maxillary irrigation and culture as an adjunct'],
                'answer': 3,
                'explanation': 'The adenoid is the central pediatric reservoir and obstructing tissue, so '
                               'adenoidectomy is the usual first operation for medically refractory CRS in a young '
                               'child, with maxillary irrigation and culture as a common adjunct. Mild CT thickening '
                               'does not mandate ESS, and CT findings in children must be read with the symptoms. The '
                               'deciding clues are an adequate medical trial, an infected obstructing adenoid and '
                               'limited sinus disease. ESS is reserved for persistent objective disease afterward.',
                'why_wrong': ['Repeating or prolonging antibiotics without a new phenotype rationale adds resistance '
                              'and adverse effects after an adequate trial has failed.',
                              'Formal ESS is a later step after adenoid-directed treatment in a typical child and '
                              'ignores the obstructing adenoid.',
                              'Serial CT adds radiation without new decision value, because the decision rests on '
                              'symptoms and endoscopy after medical failure.',
                              'Correct.'],
                'board_pearl': 'Pediatric CRS: prove the phenotype, address the adenoid first, and keep ESS for '
                               'persistent objective disease.',
                'curveball': 'At adenoidectomy, the adenoid turns out to be small, but there is purulence in the '
                             'middle meatus. How does that change counseling?',
                'curveball_answer': 'A small adenoid lowers the expected benefit of adenoidectomy alone, because the '
                                    'reservoir is less likely to be the driver. Irrigate and culture the maxillary '
                                    'sinus, counsel that symptoms may persist, and if they do, reassess with endoscopy '
                                    'and CT, screen for host factors, and consider limited ESS targeted to the '
                                    'diseased sinuses.'},
 'v208_rhi_pedscrs_snr': {'stem': 'A 7-year-old girl has persistent purulent rhinorrhea and nasal obstruction 9 months '
                                  'after adenoidectomy and maximal medical therapy. CT shows diffuse pansinus '
                                  'opacification. Her history includes respiratory distress requiring oxygen after a '
                                  'term birth, a daily wet cough since infancy, recurrent otorrhea after tubes and '
                                  'bronchiectasis on chest CT. Sweat chloride was normal. What should happen before '
                                  'extensive sinus surgery?',
                          'choices': ['Proceed with complete sphenoethmoidectomy and frontal sinusotomy for the '
                                      'diffuse CT disease',
                                      'Give a 6-week course of IV antibiotics through a PICC line to clear the sinus '
                                      'infection',
                                      'Perform revision adenoidectomy, since adenoid regrowth commonly explains '
                                      'surgical failure',
                                      'Evaluate for primary ciliary dyskinesia and coordinate pulmonary care, then '
                                      'tailor surgery'],
                          'answer': 3,
                          'explanation': 'Persistent pediatric CRS with neonatal respiratory distress at term, '
                                         'lifelong wet cough, chronic otorrhea and bronchiectasis is a mucociliary '
                                         'disorder until proven otherwise, and normal sweat chloride points toward '
                                         'primary ciliary dyskinesia. Confirming it with nasal nitric oxide and '
                                         'genetic or ciliary testing changes pulmonary care, family counseling and '
                                         'expectations from surgery. Sinus surgery may still help drainage and topical '
                                         'access, but it should target defined disease and cannot correct the '
                                         'clearance defect.',
                          'why_wrong': ['Diffuse CT disease in a suspected host disorder calls for diagnosis first; '
                                        'adult-style complete ESS without it misses the driver.',
                                        'Prolonged IV antibiotics carry line and resistance risks and do not address '
                                        'the underlying ciliary clearance defect.',
                                        'Meaningful adenoid regrowth is uncommon, and revision adenoidectomy ignores '
                                        'the systemic lower-airway features that point to PCD.',
                                        'Correct.'],
                          'board_pearl': 'Refractory pediatric CRS with lower-airway and ear disease: evaluate CF or '
                                         'PCD before escalating surgery.',
                          'curveball': 'Which laterality or fertility findings can further support a primary ciliary '
                                       'dyskinesia phenotype?',
                          'curveball_answer': 'Situs inversus totalis in about half of patients, or heterotaxy with '
                                              'congenital heart disease and spleen anomalies, supports PCD because '
                                              'nodal cilia set laterality. Later in life, male infertility from '
                                              'immotile sperm and reduced female fertility or ectopic pregnancy add '
                                              'support, as do affected siblings. Low nasal nitric oxide with genetic '
                                              'or ciliary testing confirms the diagnosis.'},
 'v136_rhi_23': {'stem': 'A 46-year-old woman had endoscopic sinus surgery for chronic rhinosinusitis without polyps 2 '
                         'years ago at another hospital. She reports persistent facial pressure and congestion and '
                         'asks to schedule revision surgery. She has not brought records, has used her saline rinses '
                         'only occasionally, and describes headaches with light sensitivity. Office endoscopy has not '
                         'yet been done. What is the most important next step?',
                 'choices': ['Schedule image-guided revision, since recurrent symptoms imply residual cells',
                             'Define the failure mechanism with endoscopy, records, adherence, and fine-cut CT',
                             'Start dupilumab for presumed type 2 inflammation recurring after surgery',
                             'Give 3 weeks of antibiotics with oral steroids, then revise if her symptoms persist'],
                 'answer': 1,
                 'explanation': 'Persistent symptoms after sinus surgery do not automatically mean failed surgery. '
                                'Revision evaluation starts by naming the failure mechanism: residual cells, scar or '
                                'ostial stenosis, recirculation, recurrent inflammatory disease, an odontogenic '
                                'source, poor topical therapy, or a nonrhinogenic cause such as migraine. Her '
                                'headaches with photophobia, uncertain adherence and missing records are the deciding '
                                'clues. Endoscopy, prior operative notes and pathology, and a fine-cut CT define '
                                'whether a correctable target exists.',
                 'why_wrong': ['Revising without a defined target risks repeating the failure, especially when '
                               'migraine features suggest a nonrhinogenic symptom source.',
                               'Correct.',
                               'Biologics are indicated for severe CRS with nasal polyps; she has CRS without polyps '
                               'and no phenotype assessment yet.',
                               'Empiric antibiotics and steroids do not establish the mechanism and can mask the '
                               'objective findings needed for planning.'],
                 'board_pearl': 'Before revision ESS, name the failure mechanism; persistent symptoms do not equal '
                                'failed surgery.',
                 'curveball': 'Her records arrive and mention a separate posterior fontanelle antrostomy. What CT or '
                              'endoscopic finding would suggest maxillary recirculation?',
                 'curveball_answer': 'Endoscopy shows mucus leaving the natural ostium and re-entering the sinus '
                                     'through a separate posterior or fontanelle opening, creating a loop. CT shows '
                                     'two separate openings in the medial maxillary wall, often with a residual '
                                     'uncinate hiding the natural ostium. The fix is joining the openings into one '
                                     'antrostomy that includes the natural ostium.'},
 'v142_rhi_04': {'stem': 'A 52-year-old man with aspirin-exacerbated respiratory disease has recurrent nasal polyps '
                         'despite maintenance steroid irrigations and is scheduled for his third endoscopic sinus '
                         'surgery. Both middle turbinates were partially resected, the right lamina papyracea appears '
                         'thinned, and the frontal recesses are scarred. Navigation is available. Which preoperative '
                         'step most improves the safety of this revision?',
                 'choices': ['Triplanar CT review mapping residual cells, skull base, orbit, and frontal pathway',
                             'Rely on intraoperative navigation to find each landmark as it appears in the scarred '
                             'field',
                             'Plan complete resection of both middle turbinate remnants to widen exposure and access',
                             'Obtain contrast MRI to separate polyps from secretions and map the operative anatomy'],
                 'answer': 0,
                 'explanation': 'Revision surgery is riskier because landmarks may be absent or displaced, so the CT '
                                'becomes an active surgical map. Reviewing fine-cut images in axial, coronal and '
                                'sagittal planes identifies residual partitions, the height and slope of the skull '
                                'base, lamina dehiscence, the frontal drainage pathway, and the prior surgical '
                                'defects. Each step then has a planned landmark. Navigation supplements that plan but '
                                'does not replace understanding the anatomy, and AERD recurrence still needs ongoing '
                                'medical or aspirin-desensitization strategy.',
                 'why_wrong': ['Correct.',
                               'Navigation has registration error and cannot interpret anatomy; without a preoperative '
                               'map, the surgeon cannot recognize a misleading reading.',
                               'Removing the remnants destroys a useful medial landmark and invites crusting and '
                               'frontal scarring rather than improving safety.',
                               'MRI shows soft tissue well but not the fine bony partitions and skull-base anatomy '
                               'needed for revision dissection.'],
                 'board_pearl': 'Revision ESS: plan from triplanar CT as a surgical map; navigation supplements '
                                'anatomy, never replaces it.',
                 'curveball': 'Which stable landmarks are especially useful when the middle turbinate has been '
                              'partially resected?',
                 'curveball_answer': 'The maxillary sinus roof and orbital floor seen through the antrostomy, the '
                                     'medial orbital wall, the choana and sphenoid face with the sphenoid ostium, the '
                                     'skull base identified in the sphenoid, and the nasal septum. Remnants of the '
                                     "middle turbinate's vertical attachment still mark the medial boundary of the "
                                     'frontal recess and should be preserved.'},
 'v209_rhi_revision_snr': {'stem': 'A 58-year-old man has 10 months of right-sided foul purulent drainage after ESS. '
                                   'Endoscopy shows a widely patent right maxillary antrostomy that includes the '
                                   'natural ostium, an open ethmoid cavity, and pus draining from the maxillary sinus. '
                                   'The operative note confirms complete uncinectomy. CT shows right maxillary '
                                   'opacification and a periapical lucency at the first molar root with a dehiscent '
                                   'sinus floor. What is the best next step?',
                           'choices': ['Revision antrostomy enlarged into a mega-antrostomy for gravity drainage',
                                       'Culture-directed oral antibiotics for 6 weeks as the definitive treatment',
                                       'Dental treatment of the molar, without revising the patent sinus cavity',
                                       'Revision ESS with frontal sinusotomy to address residual frontal recess cells'],
                           'answer': 2,
                           'explanation': 'Revision surgery should correct the mechanism of failure, not repeat a '
                                          'prior operation. A patent antrostomy and ethmoid cavity plus unilateral '
                                          'foul pus and a periapical lucency with a dehiscent floor identify an '
                                          'odontogenic source. Source control belongs at the tooth through endodontic '
                                          'treatment or extraction. Sinus revision is considered only if disease '
                                          'persists after dental care or another correctable sinonasal target appears. '
                                          'Re-dissecting patent anatomy adds scar and risk without treating the cause.',
                           'why_wrong': ['The drainage pathway is already open, and enlarging it does not remove the '
                                         'infected tooth that keeps reseeding the sinus.',
                                         'Antibiotics may calm the infection but cannot cure it while the dental '
                                         'source remains untreated.',
                                         'Correct.',
                                         'There is no frontal disease or residual frontal cell described; operating '
                                         'there treats an absent target.'],
                           'board_pearl': 'Persistent unilateral maxillary pus with a patent antrostomy: look for an '
                                          'odontogenic source and treat the tooth.',
                           'curveball': 'What operative-record and CT findings help distinguish residual uncinate, '
                                        'recirculation, stenosis and nonrhinogenic failure?',
                           'curveball_answer': 'Residual uncinate shows on CT and endoscopy as a retained flange '
                                               'hiding the natural ostium. Recirculation shows two separate openings '
                                               'with a mucus loop. Stenosis is a scarred, narrowed opening that the '
                                               'operative note says was made wide. Nonrhinogenic failure shows patent '
                                               'cavities, normal endoscopy and a clear CT despite ongoing pain, '
                                               'pointing to migraine or neuralgia.'},
 'v136_rhi_26': {'stem': 'A 49-year-old woman is undergoing endoscopic sphenoidotomy for a fungal ball in a '
                         'well-pneumatized sellar-type sphenoid sinus. The natural ostium has been opened medially, '
                         'and the resident wants to enlarge it further superiorly and laterally with a Kerrison '
                         'rongeur to improve the view. The CT shows thin bone over the lateral sinus wall. Which '
                         'structures make this enlargement potentially catastrophic?',
                 'choices': ['Vidian nerve and maxillary nerve canal',
                             'Optic nerve and internal carotid artery',
                             'Posterior septal artery and choana',
                             'Cribriform plate and olfactory nerve fibers'],
                 'answer': 1,
                 'explanation': 'The lateral sphenoid wall carries the optic nerve superolaterally and the internal '
                                'carotid artery inferolaterally, with the opticocarotid recess between them. Both '
                                'canals can be thin or dehiscent, especially in a well-pneumatized sellar sphenoid. '
                                'Uncontrolled superior or lateral enlargement can cause blindness or carotid '
                                'hemorrhage. Safe enlargement proceeds medially and inferiorly from the natural ostium '
                                'under direct vision, guided by preoperative CT review of pneumatization and septal '
                                'insertions.',
                 'why_wrong': ['The vidian and maxillary canals lie in the floor and inferolateral recess; injury '
                               'causes dry eye or numbness, not catastrophe.',
                               'Correct.',
                               'The posterior septal artery crosses the sphenoid face inferiorly; it bleeds with '
                               'inferior enlargement but is controllable with cautery.',
                               'The cribriform plate lies in the anterior skull base medial to the ethmoid roof, well '
                               "away from the sphenoid's lateral wall."],
                 'board_pearl': 'Sphenoid lateral wall: optic nerve above, carotid below; enlarge medially and '
                                'inferiorly from the natural ostium.',
                 'curveball': 'In recovery, she says the vision in one eye seems dim. What visual symptoms after '
                              'sphenoid surgery require immediate evaluation, and what do you do?',
                 'curveball_answer': 'Any new decrease in vision, color desaturation, visual field loss, afferent '
                                     'pupillary defect, or diplopia with proptosis needs immediate ophthalmology '
                                     'review and imaging. Remove packing, check for orbital hematoma needing lateral '
                                     'canthotomy, and obtain CT for a bone fragment or hematoma compressing the optic '
                                     'nerve. Steroids or decompression for direct optic injury remain debated.'},
 'v144_rh_21': {'stem': 'A 61-year-old man has 6 months of deep vertex headache. Nasal endoscopy is normal. CT shows '
                        'complete opacification of the left sphenoid sinus with central hyperdensity and fine '
                        'calcifications, and an intersinus septum that deviates toward the left lateral wall. '
                        'Endoscopic sphenoidotomy is planned for a presumed fungal ball. Which preoperative imaging '
                        'review matters most before entering the sinus?',
                'choices': ['Confirming T2 signal void on MRI, which can replace bony review on the CT',
                            'Measuring the Keros depth of the olfactory fossa to plan the safe sphenoid entry point',
                            'Tracing the anterior ethmoid artery on coronal images before sphenoidotomy',
                            'Mapping optic and carotid canal dehiscence, Onodi cells, and septal insertions'],
                'answer': 3,
                'explanation': 'The sphenoid can expose or dehisce the optic nerve and internal carotid artery, and '
                               'intersinus septa often insert onto the carotid canal, so twisting one can tear the '
                               'artery. An Onodi cell can carry the optic nerve above and lateral to the sphenoid and '
                               'mislead the surgeon. The deviated septum is the deciding clue that insertion must be '
                               'traced before instrumentation. Triplanar CT is the bone map, and MRI is added for soft '
                               'tissue or skull-base questions.',
                'why_wrong': ['MRI signal void supports a fungal ball but does not show the thin bony canals and '
                              'septal insertions that determine safe dissection.',
                              'Keros depth describes the anterior skull base at the olfactory fossa and ethmoid roof, '
                              'not sphenoid danger anatomy.',
                              'The anterior ethmoid artery matters in frontal recess and ethmoid surgery, not isolated '
                              'sphenoidotomy through the recess.',
                              'Correct.'],
                'board_pearl': 'Before any sphenoidotomy, trace septal insertions to the carotid and optic canals and '
                               'look for an Onodi cell.',
                'curveball': 'Entering transnasally rather than through the ethmoids, where is the natural sphenoid '
                             'ostium relative to the superior turbinate in this patient?',
                'curveball_answer': 'It lies medial to the superior turbinate in the sphenoethmoidal recess, about 1 '
                                    'to 1.5 cm above the choanal arch. Removing the inferior third of the superior '
                                    'turbinate improves access, and the ostium is then widened medially and '
                                    'inferiorly, away from the optic nerve and carotid artery on the lateral wall.'},
 'v209_rhi_sphenoid_snr': {'stem': 'A 57-year-old woman is undergoing endoscopic drainage of a sphenoid mucocele. '
                                   'Preoperative CT shows an intersinus septum inserting directly onto a prominent '
                                   'left carotid canal with thin bony covering. After the anterior face is opened, the '
                                   'septum partly blocks the view of the left lateral recess, but the mucocele '
                                   'contents can be suctioned and the cavity marsupialized around it. What is the best '
                                   'operative decision?',
                           'choices': ['Remove the septum with through-cutting forceps after confirming it on '
                                       'navigation',
                                       'Drill the septum flush with the carotid prominence for symmetric exposure',
                                       'Leave the carotid-attached septum in place and clear the disease around it',
                                       'Fracture the septum laterally with an elevator to open the lateral recess'],
                           'answer': 2,
                           'explanation': 'Septa that insert on the carotid canal transmit force to a thin or '
                                          'dehiscent covering, so twisting, fracturing or drilling them can injure the '
                                          'artery. The goal is durable marsupialization of the mucocele, not a '
                                          'symmetric cavity. Because the contents can be cleared without touching the '
                                          'attachment, the safest choice is to leave that segment alone. Any septal '
                                          'reduction should stop well short of the carotid, and only under direct '
                                          'control if truly needed for the disease.',
                           'why_wrong': ['Through-cutting avoids torque, but cutting at the insertion still risks '
                                         'carotid injury and is unnecessary when disease is cleared.',
                                         'Drilling flush to a thin carotid prominence risks breaching the canal to '
                                         'gain symmetry that offers no therapeutic benefit.',
                                         'Correct.',
                                         'Fracturing transmits force directly to the carotid canal and is the classic '
                                         'mechanism of internal carotid laceration.'],
                           'board_pearl': 'Never torque or fracture a sphenoid septum attached to the carotid canal; '
                                          'clear the disease around it.',
                           'curveball': 'What immediate steps are required if brisk arterial bleeding suggests '
                                        'internal carotid injury during endoscopic sphenoid surgery?',
                           'curveball_answer': 'Call for help and alert anesthesia, keep the airway secure, and '
                                               'maintain normotension with blood available. Use two surgeons with '
                                               'large suction to see the bleeding point, then apply a crushed muscle '
                                               'patch or targeted packing rather than packing blindly. Proceed '
                                               'urgently to angiography for endovascular repair or sacrifice, and '
                                               'repeat angiography later for pseudoaneurysm.'},
 'v143_rhi_03': {'stem': 'A 44-year-old man had a maxillary antrostomy at another hospital a year ago but still has '
                         'right purulent rhinorrhea. Endoscopy shows a wide opening in the posterior fontanelle and an '
                         'anterior uncinate remnant. Mucus streams out from behind the remnant, flows back over it and '
                         're-enters the sinus through the posterior opening. CT confirms the residual uncinate and two '
                         'separate medial wall openings. Which revision step corrects the problem?',
                 'choices': ['Remove the residual uncinate and join the natural ostium to the existing opening',
                             'Enlarge the posterior opening further back toward the palatine bone and choana',
                             'Create an inferior meatal antrostomy to give the sinus gravity-dependent drainage',
                             'Perform an endoscopic modified medial maxillectomy to open the sinus widely'],
                 'answer': 0,
                 'explanation': 'Maxillary cilia drive mucus toward the natural ostium regardless of where other '
                                'openings are. An antrostomy that does not include the natural ostium lets mucus exit '
                                'through it and re-enter through the surgical opening, causing recirculation and '
                                'persistent infection. The deciding clue is the visible mucus loop with a residual '
                                'uncinate hiding the true ostium. Removing the remnant and connecting the two openings '
                                'into a single antrostomy restores one physiologic drainage pathway.',
                 'why_wrong': ['Correct.',
                               'Enlarging the wrong opening keeps it separate from the natural ostium, so the '
                               'recirculation loop continues.',
                               'Inferior meatal openings oppose mucociliary flow, which still goes to the natural '
                               'ostium, so they create another recirculation path.',
                               'Medial maxillectomy is reserved for tumor or refractory disease and is excessive when '
                               'a single connection solves the mechanism.'],
                 'board_pearl': 'Maxillary recirculation: connect the accessory opening to the true natural ostium '
                                'rather than enlarging the wrong window.',
                 'curveball': 'Where is the nasolacrimal duct relative to the anterior maxillary antrostomy, and how '
                              'does that constrain enlargement?',
                 'curveball_answer': 'The nasolacrimal duct runs in bone just anterior to the natural maxillary '
                                     'ostium, within a few millimeters of it. Anterior enlargement with a backbiter '
                                     'beyond hard lacrimal bone risks duct injury and epiphora, so widen the '
                                     'antrostomy posteriorly and inferiorly along the fontanelle under direct vision.'},
 'v206_rhi_max_app': {'stem': 'A 33-year-old woman with chronic maxillary rhinosinusitis is undergoing primary ESS. CT '
                              'showed a moderate Haller cell narrowing the left infundibulum. After the uncinate is '
                              'incised, a round opening into the maxillary sinus is seen in the posterior fontanelle, '
                              'behind where the natural ostium is expected. The natural ostium itself has not yet been '
                              'identified. What is the safest next step?',
                      'choices': ['Enlarge the visible opening posteriorly and inferiorly, since it drains the sinus',
                                  'Open the Haller cell laterally to find the infundibulum before going further',
                                  'Leave both openings untouched to protect the nasolacrimal duct anteriorly',
                                  'Locate the natural ostium behind the uncinate remnant and join both openings'],
                      'answer': 3,
                      'explanation': 'Accessory ostia in the posterior fontanelle are common and easily mistaken for '
                                     'the natural ostium. Enlarging only the accessory opening leaves two separate '
                                     'openings and sets up recirculation. The natural ostium lies in the infundibulum '
                                     'behind the uncinate, angled superiorly and medially, so the remaining uncinate '
                                     'is removed, the ostium found with a probe, and the two connected into one '
                                     'antrostomy. The Haller cell is approached under direct vision because it borders '
                                     'the orbital floor.',
                      'why_wrong': ['Mucociliary flow still goes to the natural ostium, so enlarging only the '
                                    'accessory opening creates recirculation.',
                                    'Blind lateral dissection through the Haller cell before finding the ostium risks '
                                    'entering the orbit at the floor.',
                                    "Leaving the natural ostium obstructed fails the operation's goal, and careful "
                                    'identification does not require anterior duct-risk dissection.',
                                    'Correct.'],
                      'board_pearl': 'Find and incorporate the natural maxillary ostium; an accessory opening alone '
                                     'invites recirculation.',
                      'curveball': 'How can a Haller cell or lateralized uncinate distort the expected location of the '
                                   'infundibulum and natural ostium?',
                      'curveball_answer': 'A Haller cell narrows and elevates the infundibulum along the orbital '
                                          'floor, while a lateralized uncinate can lie against the lamina and hide the '
                                          'corridor. The natural maxillary ostium remains behind and lateral to the '
                                          'uncinate in the infundibulum; find it directly and avoid an isolated '
                                          'accessory opening or orbital injury while searching laterally.'},
 'v207_rhi_frontal_snr': {'stem': 'A 50-year-old man with chronic rhinosinusitis with polyps is undergoing a Draf IIa '
                                  'frontal sinusotomy. After removing the agger nasi and a supra-agger cell, the '
                                  'frontal outflow is open and mucosa-lined but narrow, about 4 mm. Further widening '
                                  'would require circumferential drilling of the frontal beak with mucosal loss near '
                                  'the skull base and anterior ethmoid artery. What is the best decision?',
                          'choices': ['Drill the frontal beak circumferentially for the largest possible diameter',
                                      'Accept the patent mucosa-lined outflow and optimize postoperative care',
                                      'Convert to a Draf III to create a common frontal drainage cavity',
                                      'Proceed to osteoplastic flap obliteration of the frontal sinus'],
                          'answer': 1,
                          'explanation': 'The goal of frontal surgery is durable drainage and topical access, not '
                                         'maximal diameter. Circumferential drilling strips mucosa from a narrow '
                                         'outflow, which heals with osteitis, neo-osteogenesis and scar contracture, '
                                         'the most common cause of iatrogenic frontal stenosis. It also brings the '
                                         'drill toward the skull base and anterior ethmoid artery. With the '
                                         'obstructing cells removed and a mucosa-lined pathway open, the senior '
                                         'decision is to stop and rely on careful postoperative care.',
                          'why_wrong': ['Circumferential mucosal loss in the narrow recess promotes restenosis and '
                                        'adds skull-base and arterial risk for little functional gain.',
                                        'Correct.',
                                        'A Draf III is reserved for failed prior frontal surgery or specific disease, '
                                        'not a first operation that has already achieved patency.',
                                        'Obliteration is a salvage operation for unreconstructable outflow and removes '
                                        'the possibility of endoscopic surveillance.'],
                          'board_pearl': 'Frontal recess: a patent mucosa-lined pathway beats a large denuded one; '
                                         'preserve mucosa to prevent stenosis.',
                          'curveball': 'Which postoperative debridement and topical-therapy principles help maintain '
                                       'frontal patency after technically adequate surgery?',
                          'curveball_answer': 'Maintain a usable frontal corridor with high-volume saline irrigation, '
                                              'topical steroid delivered by rinse, and targeted debridement of '
                                              'obstructing crust, clot or early synechiae without stripping healthy '
                                              'mucosa. Control the polyp inflammation, treat early scar promptly, and '
                                              'reassess endoscopically rather than probing blindly if narrowing '
                                              'persists.'},
 'v208_rhi_turb_snr': {'stem': 'A 45-year-old woman still has bilateral nasal obstruction 1 year after septoplasty and '
                               'submucosal inferior turbinate reduction. Her NOSE score is 75. Endoscopy shows a '
                               'straight septum and small, healthy inferior turbinates. On deep inspiration, the upper '
                               'lateral cartilages and lateral nasal walls collapse inward, and supporting the lateral '
                               'wall with a curette at the internal valve markedly improves her breathing. What is the '
                               'best next step?',
                       'choices': ['Functional rhinoplasty with lateral wall support, such as spreader or batten '
                                   'grafts',
                                   'Revision inferior turbinate resection to widen the remaining airway further',
                                   'Endoscopic posterior septoplasty for a deviation missed on anterior rhinoscopy',
                                   'A trial of intranasal steroid and azelastine for persistent mucosal congestion'],
                       'answer': 0,
                       'explanation': 'Persistent obstruction after technically adequate septal and turbinate surgery '
                                      'requires reassessing the mechanism. The deciding clues are small, healthy '
                                      'turbinates, a straight septum, visible inspiratory collapse and improvement '
                                      'with targeted lateral wall support, which localize the problem to dynamic '
                                      'internal valve and lateral wall weakness. Spreader grafts or flaps widen and '
                                      'stiffen the internal valve, and batten or lateral crural grafts support the '
                                      'lateral wall. Removing more turbinate would not correct the collapse.',
                       'why_wrong': ['Correct.',
                                     'The turbinates are already small; further resection does not stop valve collapse '
                                     'and risks crusting, dryness and empty nose symptoms.',
                                     'Endoscopy showed a straight septum, and a posterior deviation would not explain '
                                     'collapse that improves with lateral wall support.',
                                     'Medical therapy treats mucosal swelling, but this obstruction is structural and '
                                     'dynamic, with small turbinates and visible collapse.'],
                       'board_pearl': 'Obstruction after septoplasty and turbinate reduction: look for dynamic valve '
                                      'collapse before removing more turbinate.',
                       'curveball': 'How would improvement with lateral wall support during examination influence '
                                    'functional rhinoplasty planning?',
                       'curveball_answer': 'Targeted support localizes the failing segment. Improvement when the '
                                           'internal valve area is supported favors spreader grafts or flaps, while '
                                           'improvement with support of the alar or lateral wall favors batten or '
                                           'lateral crural strut grafts. An absorbable lateral wall implant is an '
                                           'office option for selected patients, and photographs and NOSE scores '
                                           'document the baseline.'},
 'v208_rhi_objective_snr': {'stem': 'A 39-year-old man has a NOSE score of 80 with constant bilateral obstruction. '
                                    'Endoscopy shows a straight septum and normal turbinates, but the lateral nasal '
                                    'walls collapse visibly on moderate inspiration, and targeted support of the '
                                    'internal valve with a cotton-tipped applicator relieves his symptoms. '
                                    'Rhinomanometry shows only mildly increased resting resistance. How should the '
                                    'rhinomanometry result influence his surgical plan?',
                            'choices': ['It excludes clinically meaningful obstruction, so surgical treatment should '
                                        'be declined',
                                        'It indicates mucosal rather than structural obstruction, favoring inferior '
                                        'turbinate reduction',
                                        'It supplements but does not override the concordant dynamic exam favoring '
                                        'valve surgery',
                                        'It suggests an unreliable symptom report, so a psychological screen should '
                                        'come first'],
                            'answer': 2,
                            'explanation': 'Perceived nasal obstruction reflects resistance, cross-sectional geometry, '
                                           'mucosal airflow sensation and dynamic collapse. Resting rhinomanometry '
                                           'measures pressure-flow resistance during quiet breathing and can '
                                           'underestimate collapse that appears with stronger inspiration. Objective '
                                           'tests quantify selected components but provide no universal surgical '
                                           'threshold. Here, visible collapse, a high NOSE score and relief with '
                                           'targeted support form a concordant mechanism, so discordance is '
                                           'information rather than a veto.',
                            'why_wrong': ['A mildly abnormal resting study does not exclude dynamic collapse, which '
                                          'occurs with stronger inspiration than quiet breathing.',
                                          'Rhinomanometry does not separate mucosal from structural causes without '
                                          'decongestion, and his turbinates are normal on exam.',
                                          'Correct.',
                                          'Poor correlation between symptoms and airflow tests is expected physiology, '
                                          'not evidence of an unreliable or psychological complaint.'],
                            'board_pearl': 'Objective airflow tests inform but do not overrule a concordant dynamic '
                                           'exam; plan surgery on the mechanism.',
                            'curveball': 'Why can a nonspecific Cottle maneuver overestimate benefit compared with '
                                         'targeted lateral wall support?',
                            'curveball_answer': 'Pulling the cheek laterally widens the internal valve, lateral wall '
                                                'and vestibule all at once, and it improves airflow in many people '
                                                'without obstruction. A modified Cottle, supporting specific areas '
                                                'from inside with a curette or cotton tip, localizes which segment '
                                                'fails and predicts which graft will help.'},
 'v208_rhi_smell_snr': {'stem': 'A 52-year-old woman lost her sense of smell during a COVID-19 infection 14 months ago '
                                'and now has parosmia with coffee and onions. Validated smell testing is in the '
                                'anosmic range. Endoscopy shows clear olfactory clefts, sinus CT is normal, and she '
                                'has no head trauma, neurologic symptoms or unilateral nasal findings. She asks for '
                                'sinus surgery to open her smell area. What is the best counseling decision?',
                        'choices': ['Offer endoscopic sinus surgery with olfactory cleft opening to improve odor '
                                    'access',
                                    'Decline surgery and continue structured olfactory training with safety counseling',
                                    'Prescribe a 3-week oral prednisone taper to reduce olfactory neuroepithelial '
                                    'injury',
                                    'Order brain MRI first and postpone any counseling until the results are '
                                    'available'],
                        'answer': 1,
                        'explanation': 'Postviral olfactory loss is sensorineural: the virus damages sustentacular '
                                       'cells and receptor neurons, and recovery depends on regeneration. With open '
                                       'clefts and a normal CT, surgery has no conductive target and cannot restore '
                                       'smell. Structured olfactory training is the low-risk, evidence-supported '
                                       'rehabilitation, and parosmia often reflects regeneration. Counseling covers '
                                       'prognosis and household safety. Imaging is reserved for red flags such as '
                                       'unilateral findings, trauma or neurologic signs.',
                        'why_wrong': ['With open olfactory clefts and a normal CT, there is no obstruction to remove, '
                                      'so surgery adds risk without benefit.',
                                      'Correct.',
                                      'Systemic steroids target inflammatory or conductive loss; without that target '
                                      'their benefit is unproven and side effects are real.',
                                      'MRI is for red flags; with a clear postviral history and no focal findings, it '
                                      'should not delay training and counseling.'],
                        'board_pearl': 'Postviral anosmia with normal endoscopy and CT: olfactory training and safety '
                                       'counseling, not sinus surgery.',
                        'curveball': 'What household safety counseling is important for patients who cannot reliably '
                                     'detect smoke, gas or spoiled food?',
                        'curveball_answer': 'Install and regularly test smoke and carbon monoxide detectors on every '
                                            'floor, consider a natural gas detector or electric appliances, label and '
                                            'date stored food and discard by date, and ask others to check food, gas '
                                            'leaks and personal hygiene. Review occupational exposure to hazardous '
                                            'fumes as well.'},
 'v212_rhi_ar_found': {'stem': 'A 19-year-old college student has had sneezing fits, nasal and palatal itch, clear '
                               'watery rhinorrhea and congestion every April and May for 3 years, with itchy, watery '
                               'eyes. Symptoms improve when she returns home in summer. She uses oxymetazoline for a '
                               'day or two during bad weeks. During symptoms, exam shows pale, boggy inferior '
                               'turbinates with clear secretions and no purulence. Which diagnosis best fits?',
                       'choices': ['Seasonal allergic rhinitis',
                                   'Nonallergic vasomotor rhinitis',
                                   'Recurrent viral rhinosinusitis',
                                   'Rhinitis medicamentosa'],
                       'answer': 0,
                       'explanation': 'Allergic rhinitis is an IgE-mediated rhinitis tied to exposure: sneezing, nasal '
                                      'itch, watery rhinorrhea and congestion, often with ocular itch. The deciding '
                                      'clue is the reproducible seasonal pattern in spring, typical of tree pollen, '
                                      'plus ocular symptoms and pale edematous mucosa. History and exam make the '
                                      'diagnosis, and testing is reserved for uncertainty, poor response or planned '
                                      'immunotherapy. An intranasal corticosteroid is first-line for symptoms that '
                                      'affect quality of life.',
                       'why_wrong': ['Correct.',
                                     'Vasomotor rhinitis is triggered by temperature, odors or irritants without itch, '
                                     'ocular symptoms or a reproducible pollen season.',
                                     'Viral infections are not tied to the same months every year and usually bring '
                                     'sore throat, malaise and resolution within 10 days.',
                                     'Medicamentosa follows prolonged daily decongestant use; one or two days of '
                                     'oxymetazoline does not produce rebound congestion.'],
                       'board_pearl': 'Sneezing, itch and watery rhinorrhea in a reproducible season with ocular '
                                      'symptoms: allergic rhinitis, diagnosed clinically.',
                       'curveball': 'Which features would make you test for a specific allergen rather than treat '
                                    'empirically?',
                       'curveball_answer': 'Test with skin-prick or serum specific IgE when the diagnosis is '
                                           'uncertain, symptoms fail adequate empiric therapy, identifying the trigger '
                                           'would change avoidance, such as a pet, or immunotherapy is being '
                                           'considered. Test only plausible inhalants, because sensitization without '
                                           'symptoms is common.'},
 'v212_rhi_lar_app': {'stem': 'A 32-year-old man has reproducible sneezing, nasal itch, watery rhinorrhea and '
                              'congestion within minutes of cleaning dusty rooms, and symptoms improve with an '
                              'intranasal steroid. Properly performed skin-prick testing and serum specific IgE to '
                              'dust mite and other inhalants are negative twice. A specialty clinic found no '
                              'detectable nasal specific-IgE. Confirming an allergen-driven mechanism would change his '
                              'counseling about allergen-directed therapy. Which test best establishes local allergic '
                              'rhinitis?',
                      'choices': ['Repeat skin-prick testing with an expanded panel of inhalant extracts',
                                  'Empiric immunotherapy, using symptom response as the diagnostic test',
                                  'Nasal allergen challenge with dust mite under specialist monitoring',
                                  'Sinus CT looking for mucosal thickening that supports local allergy'],
                      'answer': 2,
                      'explanation': 'Local allergic rhinitis is an allergic phenotype with negative routine systemic '
                                     'testing but a localized nasal allergen-specific response. A controlled nasal '
                                     'allergen challenge reproducing symptoms and objective changes is the most direct '
                                     'confirmation. Nasal specific-IgE supports the diagnosis when present, but its '
                                     'limited sensitivity and unstandardized collection mean a negative assay does not '
                                     'exclude it. The deciding clue is a convincing exposure history that would change '
                                     'therapy. Negative systemic tests alone do not establish LAR.',
                      'why_wrong': ['Broader systemic panels test the wrong compartment; LAR is defined by negative '
                                    'systemic sensitization, so more skin tests add nothing.',
                                    'Immunotherapy for LAR is a specialist option only after the responsible local '
                                    'allergen is confirmed, not a diagnostic trial.',
                                    'Correct.',
                                    'Sinus CT shows mucosal thickening from many causes and cannot demonstrate a local '
                                    'IgE-mediated allergen response.'],
                      'board_pearl': 'LAR: allergic history, negative systemic tests, and a positive nasal allergen '
                                     'challenge; nasal IgE has limited sensitivity.',
                      'curveball': 'The nasal challenge to dust mite is positive. Is allergen immunotherapy a '
                                   'reasonable option for him?',
                      'curveball_answer': 'Yes, in a specialist setting. Randomized trials of subcutaneous '
                                          'immunotherapy in confirmed LAR, mainly to dust mite and grass pollen, show '
                                          'fewer symptoms, less medication use and better challenge tolerance. The '
                                          'evidence base is smaller than for systemic allergic rhinitis, so counsel '
                                          'accordingly and optimize intranasal steroid and antihistamine therapy '
                                          'first.'},
 'v212_rhi_lar_snr': {'stem': 'A 66-year-old man has bilateral watery rhinorrhea that drips when he walks into cold '
                              'air, smells perfume or eats spicy food. He has no nasal or ocular itching, sneezing '
                              'fits or seasonal pattern. Skin-prick and serum specific IgE testing are negative. Exam '
                              'shows normal mucosa without polyps or crusting, and the drainage is equal on both '
                              'sides. Which interpretation and plan are most appropriate?',
                      'choices': ['Local allergic rhinitis; arrange nasal allergen challenge testing to confirm',
                                  'Nonallergic rhinopathy; trial of intranasal ipratropium before trigger exposures',
                                  'Possible CSF leak; send the drainage for beta-2 transferrin and obtain fine-cut CT',
                                  'False-negative allergy tests; start subcutaneous immunotherapy to dust mite'],
                      'answer': 1,
                      'explanation': 'Irritant-, temperature- and food-triggered watery rhinorrhea without itch, '
                                     'sneezing paroxysms or allergen linkage is nonallergic rhinopathy, including '
                                     'gustatory and cold-air rhinitis, which are common in older adults. The mechanism '
                                     'is neural and glandular hyperreactivity, not IgE. Local allergic rhinitis keeps '
                                     'an allergic phenotype despite negative systemic tests, which this patient lacks. '
                                     'Intranasal ipratropium blocks the cholinergic glandular secretion that dominates '
                                     'his symptoms.',
                      'why_wrong': ['LAR requires an allergic phenotype with itch and sneezing tied to an allergen; '
                                    'negative tests alone do not make that diagnosis.',
                                    'Correct.',
                                    'Bilateral rhinorrhea triggered predictably by eating and cold air does not fit a '
                                    'CSF leak, which is usually unilateral and positional.',
                                    'Immunotherapy requires clinically relevant sensitization; treating nonspecific '
                                    'triggers this way is not supported.'],
                      'board_pearl': 'Watery rhinorrhea from cold air, odors or food without itch is nonallergic '
                                     'rhinopathy; ipratropium targets it.',
                      'curveball': 'His symptoms are worst at dinner and with hot soup. Which history features would '
                                   'make gustatory rhinitis particularly likely?',
                      'curveball_answer': 'Profuse, clear bilateral rhinorrhea beginning within minutes of eating hot '
                                          'or spicy food, often with sweating, in an older adult with no other nasal '
                                          'symptoms and a normal exam. Prior facial surgery or trauma can rarely cause '
                                          'similar symptoms. Ipratropium spray used before meals usually controls it.'},
 'v416_rhi_csf_oncall_disposition': {'stem': 'At 2 AM, a 46-year-old woman with a BMI of 41 calls about several weeks '
                                             'of intermittent clear drainage from the right nostril that increases '
                                             'when she bends forward. She has had no head trauma or sinonasal or '
                                             'skull-base surgery. She is afebrile and denies severe headache, neck '
                                             'stiffness, visual change, confusion or weakness. She is reliable and can '
                                             'return quickly. What is the best on-call disposition?',
                                     'choices': ['Admission tonight for lumbar drain placement and planned urgent '
                                                 'endoscopic skull-base repair',
                                                 'Prophylactic antibiotics now, with routine rhinology clinic '
                                                 'follow-up in 2 to 3 months',
                                                 'Emergency department visit tonight for CT cisternography with '
                                                 'intrathecal contrast imaging',
                                                 'Expedited outpatient skull-base visit, with fluid collection for '
                                                 'beta-2 transferrin, CT, and precautions'],
                                     'answer': 3,
                                     'explanation': 'A stable, reliable patient with an intermittent suspected '
                                                    'spontaneous leak and no danger features does not need overnight '
                                                    'admission, but she needs an expedited pathway rather than routine '
                                                    'follow-up. Outpatient steps are beta-2 transferrin on collected '
                                                    'fluid, thin-cut high-resolution CT with MRI as indicated, '
                                                    'meningitis return precautions, avoiding nose blowing and '
                                                    'straining, and pneumococcal vaccination per current CDC/ACIP '
                                                    'guidance. Her obesity raises concern for intracranial '
                                                    'hypertension. Fever, meningismus, altered mental status, acute '
                                                    'trauma or a recent postoperative leak would change the '
                                                    'disposition.',
                                     'why_wrong': ['No surgical emergency is present, and repair should follow '
                                                   'confirmation and localization rather than an unconfirmed overnight '
                                                   'admission.',
                                                   'Routine prophylactic antibiotics are not recommended, and a 2 to 3 '
                                                   'month wait leaves a possible meningitis risk unevaluated.',
                                                   'Cisternography is a selective second-line localization study and '
                                                   'is not needed tonight for a stable patient.',
                                                   'Correct.'],
                                     'board_pearl': 'Stable suspected CSF leak: expedited outpatient beta-2 '
                                                    'transferrin and CT with precautions; danger features mean '
                                                    'same-day care.',
                                     'curveball': 'If the caller instead has fever, meningismus, severe headache, '
                                                  'confusion, a new deficit, acute trauma or active drainage soon '
                                                  'after skull-base surgery, what changes?',
                                     'curveball_answer': 'Those features remove her from the stable outpatient branch. '
                                                         'Direct immediate emergency or same-day operative-team '
                                                         'assessment, evaluate for meningitis and intracranial '
                                                         'complication, obtain urgent imaging as indicated, and admit '
                                                         'when findings or monitoring warrant. Do not wait for an '
                                                         'outpatient beta-2 transferrin result.'},
 'v141_slp_06': {'stem': 'A 62-year-old man with severe obstructive sleep apnea, AHI 38 on diagnostic PSG, started '
                         'CPAP at 11 cm H2O. Eight weeks later, his download shows 6.5 hours of nightly use, low leak, '
                         'and a residual AHI of 18 that is mostly central apneas, which were rare on the diagnostic '
                         'study. He still feels unrefreshed. He takes no opioids, and his heart function is unknown. '
                         'What is the best next step?',
                 'choices': ['Increase the CPAP pressure by 2 to 3 cm H2O to eliminate the residual events',
                             'Refer for hypoglossal nerve stimulation evaluation, given the residual AHI',
                             'Sleep medicine review of pressure, mode and contributors, including an echocardiogram',
                             'Uvulopalatopharyngoplasty to address residual events driven by palatal collapse'],
                 'answer': 2,
                 'explanation': 'Central apneas that emerge on CPAP after obstructive events are controlled define '
                                'treatment-emergent central sleep apnea. Many cases fade with continued use, but '
                                'persistence at 8 weeks with ongoing symptoms needs physiologic reassessment rather '
                                'than treatment as pharyngeal collapse. Review whether the pressure is too high and '
                                'consider bilevel with a backup rate or adaptive servo-ventilation. Look for '
                                'contributors such as heart failure, opioids or stroke. An echocardiogram matters '
                                'before choosing ASV.',
                 'why_wrong': ['Excess pressure can provoke central events, so raising CPAP may worsen '
                               'treatment-emergent central apnea rather than fix it.',
                               'Hypoglossal stimulation treats obstructive collapse and is not appropriate when '
                               'central events make up a large share of the AHI.',
                               'Correct.',
                               'Palatal surgery addresses obstruction, which CPAP already controls; it cannot treat '
                               'central apneas from unstable ventilatory control.'],
                 'board_pearl': 'New central apneas on CPAP: think treatment-emergent central apnea, reassess pressure '
                                'and mode, and check cardiac function.',
                 'curveball': 'Which cardiac condition changes the safety of some adaptive servo-ventilation '
                              'strategies?',
                 'curveball_answer': 'Avoid adaptive servo-ventilation for predominant central sleep apnea in '
                                     'symptomatic chronic heart failure with reduced left ventricular ejection '
                                     'fraction, classically LVEF 45% or less, because SERVE-HF showed higher '
                                     'cardiovascular mortality in that group. Confirm the ejection fraction and use an '
                                     'alternative strategy when it is reduced.'},
 'v267_sleep_ds_snr': {'stem': 'A 15-year-old boy with Down syndrome has persistent snoring and daytime sleepiness 2 '
                               'years after adenotonsillectomy. He could not tolerate CPAP. Repeat PSG shows an '
                               'obstructive AHI of 9 with sustained end-tidal CO2 above 55 mm Hg for 40% of sleep time '
                               'and baseline SpO2 of 91%. DISE shows complete concentric collapse at the velum. His '
                               'BMI is 36. What is the best decision?',
                       'choices': ['Treat the hypoventilation with bilevel ventilation and evaluate its medical '
                                   'drivers',
                                   'Proceed with hypoglossal nerve stimulation, as persistent OSA meets the pediatric '
                                   'labeling',
                                   'Perform lingual tonsillectomy and tongue-base reduction for multilevel collapse',
                                   'Repeat DISE with a different sedation protocol to try for a favorable pattern'],
                       'answer': 0,
                       'explanation': 'Hypoglossal nerve stimulation is an obstruction-directed therapy with a narrow '
                                      'pediatric Down syndrome label: ages 13 to 18, AHI roughly 10 to 50 after '
                                      'adenotonsillectomy, PAP failure, and no complete concentric palatal collapse. '
                                      'This teen fails on AHI and on DISE pattern, and his dominant problem is '
                                      'sustained hypoventilation. That calls for ventilatory support such as bilevel '
                                      'PAP with mask desensitization, plus evaluation of obesity, hypothyroidism and '
                                      'lung disease. HNS would not treat the hypoventilation.',
                       'why_wrong': ['Correct.',
                                     'Complete concentric velar collapse and an AHI below 10 fall outside the labeled '
                                     'criteria, and HNS does not treat hypoventilation.',
                                     'DISE shows velar concentric collapse, not a tongue-base target, so lingual '
                                     'surgery would address the wrong level.',
                                     'Repeating DISE to manufacture a favorable pattern ignores the hypoventilation '
                                     'that dominates his physiology.'],
                       'board_pearl': 'Pediatric Down syndrome HNS is a narrow labeled pathway; treat hypoventilation '
                                      'and mismatched phenotypes directly.',
                       'curveball': 'How would new central events or pulmonary disease alter his candidacy for upper '
                                    'airway stimulation?',
                       'curveball_answer': 'HNS treats obstructive collapse, not central apnea or primary gas-exchange '
                                           'failure. New central events, worsening hypoventilation or significant '
                                           'pulmonary disease call for repeat phenotyping, CO2 and oxygen assessment, '
                                           'and medical or ventilatory management before any upper airway stimulation '
                                           'is considered or intensified.'},
 'v299_sleep_peds_psg_mgt': {'stem': 'A 4-year-old boy with snoring, witnessed pauses and 3+ tonsils is scheduled for '
                                     'adenotonsillectomy. PSG shows an obstructive AHI of 12 events per hour and an '
                                     'oxygen saturation nadir of 82%. He has no obesity, syndrome, craniofacial '
                                     'anomaly or neuromuscular disease, and his parents hope he can go home the same '
                                     'day. How should the PSG change the postoperative disposition plan?',
                             'choices': ['Same-day discharge, because the oxygen nadir has not fallen below 80 percent '
                                         'on the study',
                                         'Same-day discharge, because the age criterion applies only to children '
                                         'younger than 3',
                                         'Planned PICU admission with postoperative intubation until airway edema '
                                         'settles',
                                         'Overnight inpatient monitoring, because the AHI alone meets the severe OSA '
                                         'definition'],
                             'answer': 3,
                             'explanation': 'The AAO-HNSF tonsillectomy guideline recommends overnight inpatient '
                                            'monitoring after tonsillectomy for children younger than 3 years or with '
                                            'severe OSA, defined as AHI of 10 or more obstructive events per hour, '
                                            'oxygen nadir below 80%, or both. The criteria are joined by or, not and. '
                                            'This 4-year-old meets the severe OSA criterion by AHI alone, so the PSG '
                                            'changes his disposition even though his nadir is above 80% and he has no '
                                            'comorbidity.',
                             'why_wrong': ['Severe OSA is AHI of 10 or more, a nadir below 80%, or both; he meets the '
                                           'AHI criterion alone.',
                                           'Age is an independent trigger; being older than 3 does not cancel the '
                                           'severe OSA indication for monitoring.',
                                           'Routine postoperative intubation is not indicated for uncomplicated severe '
                                           'pediatric OSA; monitored overnight observation is the standard.',
                                           'Correct.'],
                             'board_pearl': 'Overnight monitoring after tonsillectomy: age younger than 3, or severe '
                                            'OSA (AHI 10 or more, nadir below 80%, or both).',
                             'curveball': 'How would the disposition change for a 5-year-old with AHI 6 and oxygen '
                                          'nadir 77%, or for a 2-year-old with only mild OSA?',
                             'curveball_answer': 'Both need overnight inpatient monitoring. The 5-year-old meets the '
                                                 'severe OSA definition by the nadir below 80% even though the AHI is '
                                                 'moderate. The 2-year-old qualifies by age alone, because being '
                                                 'younger than 3 is an independent trigger whatever the PSG severity.'},
 'v137_tps_05': {'stem': 'A 63-year-old woman has primary hyperparathyroidism with calcium 11.4 mg/dL, PTH 98 pg/mL, a '
                         'kidney stone and osteoporosis, and she wants surgery. Neck ultrasound, sestamibi SPECT/CT '
                         'and 4D CT do not localize an adenoma. She has no family history of endocrine disease, no '
                         'lithium use and normal 24-hour urine calcium excretion. Which operative strategy is most '
                         'appropriate?',
                 'choices': ['Observation with yearly calcium and bone density until imaging localizes',
                             'Bilateral four-gland exploration by an experienced parathyroid surgeon',
                             'Selective venous sampling for PTH before any neck exploration is offered',
                             'Empiric thyroid lobectomy to remove a possible intrathyroidal adenoma'],
                 'answer': 1,
                 'explanation': 'Localization imaging chooses an approach but does not make the diagnosis or decide '
                                'whether surgery is indicated. She meets surgical criteria with a stone and '
                                'osteoporosis, and the biochemistry confirms primary hyperparathyroidism. Negative '
                                'imaging raises the chance of multigland disease or a small or ectopic adenoma, so '
                                'systematic bilateral exploration based on embryologic gland positions, with '
                                'intraoperative PTH as an adjunct, cures most patients in experienced hands. Normal '
                                'urine calcium argues against familial hypocalciuric hypercalcemia.',
                 'why_wrong': ['Negative imaging is not a reason to withhold surgery from a patient who meets '
                               'operative criteria with end-organ disease.',
                               'Correct.',
                               'Venous sampling is invasive and reserved for reoperative cases with failed noninvasive '
                               'localization, not a first operation.',
                               'Lobectomy without finding a gland is a later step for a missing gland, not a primary '
                               'strategy before exploration.'],
                 'board_pearl': 'Negative localization does not cancel indicated parathyroid surgery; it calls for '
                                'bilateral four-gland exploration.',
                 'curveball': 'How does suspected multigland disease change the value of a focused approach?',
                 'curveball_answer': 'Suspected multigland disease lowers the reliability of a focused single-gland '
                                     'operation. Plan bilateral identification and assessment of all glands, use '
                                     'intraoperative PTH as an adjunct rather than a substitute for anatomy, and '
                                     'anticipate ectopic or supernumerary glands if the hormone level does not fall '
                                     'adequately.'},
 'v137_tps_08': {'stem': 'A 52-year-old man has fatigue, bone pain and a calcium of 14.8 mg/dL with PTH more than ten '
                         'times the upper limit. A firm, fixed left neck mass is palpable, and laryngoscopy shows left '
                         'vocal fold paralysis. Ultrasound shows a 3.5 cm lobulated hypoechoic mass behind the left '
                         'thyroid lobe with irregular margins. After medical calcium control, which operative '
                         'principle is most important?',
                 'choices': ['En bloc resection with the ipsilateral thyroid lobe, avoiding capsular rupture',
                             'Focused parathyroidectomy, dissecting the gland cleanly off the thyroid capsule',
                             'Preoperative FNA of the mass to confirm carcinoma before defining the extent',
                             'Bilateral four-gland exploration followed by subtotal parathyroidectomy'],
                 'answer': 0,
                 'explanation': 'Severe hypercalcemia, very high PTH, a palpable fixed mass and recurrent laryngeal '
                                'nerve paralysis signal parathyroid carcinoma. The first operation offers the best '
                                'chance of cure, so it should be planned as a cancer operation: en bloc removal of the '
                                'tumor with the ipsilateral thyroid lobe and any invaded tissue, including a nerve '
                                'already paralyzed and encased. Capsular rupture seeds the bed and is a major cause of '
                                'local recurrence, which is very hard to control later.',
                 'why_wrong': ['Correct.',
                               'Shelling the gland out as for an adenoma risks capsular rupture and positive margins, '
                               'leading to seeding and recurrence.',
                               'FNA of a suspected carcinoma risks seeding the tract and rarely distinguishes '
                               'carcinoma, which is defined by invasion.',
                               'This is a single invasive tumor, not multigland hyperplasia; subtotal '
                               'parathyroidectomy misses the oncologic goal.'],
                 'board_pearl': 'Suspected parathyroid carcinoma: en bloc resection at the first operation, avoiding '
                                'capsular rupture; no FNA.',
                 'curveball': 'What biochemical problem often dominates care in recurrent or metastatic parathyroid '
                              'carcinoma?',
                 'curveball_answer': 'Severe PTH-mediated hypercalcemia, rather than tumor bulk, usually drives '
                                     'morbidity and death. Control calcium with hydration, calcimimetics such as '
                                     'cinacalcet, and bisphosphonates or denosumab, while assessing whether resection '
                                     'or another tumor-directed treatment can reduce the hormone-producing burden.'},
 'v236_tps_ptca_fnd': {'stem': 'A 39-year-old man is referred for primary hyperparathyroidism found during workup of '
                               'fatigue and kidney stones. He had an ossifying fibroma of the mandible removed at age '
                               '25. Calcium is 13.6 mg/dL and PTH is eight times the upper limit. A firm 3 cm mass is '
                               'palpable low in the right neck, and his voice has become slightly breathy. Which '
                               'diagnosis is most likely?',
                       'choices': ['Large parathyroid adenoma',
                                   'MEN1 multigland hyperplasia',
                                   'Parathyroid carcinoma',
                                   'Tertiary hyperparathyroidism'],
                       'answer': 2,
                       'explanation': 'Parathyroid carcinoma is rare, but profound hypercalcemia with several-fold PTH '
                                      'elevation, a palpable firm neck mass and possible recurrent laryngeal nerve '
                                      'involvement should raise suspicion. Benign adenomas are usually small, soft, '
                                      'nonpalpable and produce milder hypercalcemia. The jaw tumor history points to '
                                      'hyperparathyroidism-jaw tumor syndrome from germline CDC73 mutation, which '
                                      'carries a markedly increased carcinoma risk. Suspicion should drive planning '
                                      'for en bloc resection.',
                       'why_wrong': ['Typical adenomas cause milder hypercalcemia and are rarely palpable or invasive; '
                                     'a jaw tumor history points to CDC73-related disease.',
                                     'MEN1 causes multigland hyperplasia with milder calcium elevation and pituitary '
                                     'or pancreatic tumors, not jaw fibromas or a palpable invasive mass.',
                                     'Correct.',
                                     'Tertiary disease follows long-standing secondary hyperparathyroidism, usually '
                                     'from kidney failure, which he does not have.'],
                       'board_pearl': 'Calcium above 13-14 with very high PTH, a palpable mass or nerve palsy: suspect '
                                      'parathyroid carcinoma; jaw tumors mean CDC73.',
                       'curveball': 'The referring physician offers to arrange an ultrasound-guided FNA of the neck '
                                    'mass first. Why should suspected parathyroid carcinoma generally not undergo '
                                    'routine needle biopsy?',
                       'curveball_answer': 'Needle biopsy can seed tumor along the tract, breach the capsule and cause '
                                           'hemorrhage or fibrosis that hides invasion planes. It rarely separates '
                                           'adenoma from carcinoma, because the diagnosis rests on invasion. Use the '
                                           'biochemical phenotype and imaging to plan an intact en bloc resection '
                                           'instead.'},
 'v235_tps_indet_fnd': {'stem': 'A 45-year-old woman has a 2.2 cm solid, hypoechoic thyroid nodule with smooth margins '
                                'and no calcifications, rated ACR TI-RADS 4. She has no radiation history or family '
                                'history of thyroid cancer, and her TSH is normal. FNA is read as Bethesda III, atypia '
                                'of undetermined significance, with adequate cellularity. Which statement best '
                                'describes what this result means for her care?',
                        'choices': ['The nodule should be treated as malignant, so total thyroidectomy is the '
                                    'appropriate next step',
                                    'The nodule carries low enough risk for routine ultrasound surveillance in 12 to '
                                    '24 months',
                                    'The aspirate is inadequate and should be reported and managed as a nondiagnostic '
                                    'sample',
                                    'Cytology cannot classify the nodule, so risk must be refined by repeat FNA, '
                                    'molecular testing or lobectomy'],
                        'answer': 3,
                        'explanation': 'Bethesda III and IV are indeterminate categories: cytology alone cannot call '
                                       'the nodule benign or malignant. The 2023 Bethesda system gives AUS an average '
                                       'malignancy risk of about 22%, varying with local prevalence. Management '
                                       'therefore combines ultrasound pattern, size, clinical risk and patient '
                                       'preference, and choices include repeat FNA, molecular testing when its result '
                                       'would change management, or diagnostic lobectomy. The deciding clue is '
                                       'adequate cellularity with atypia, which is not the same as malignancy or a '
                                       'failed sample.',
                        'why_wrong': ['An indeterminate result is not cancer; total thyroidectomy without further risk '
                                      'refinement overtreats most of these nodules.',
                                      'Routine surveillance fits Bethesda II benign cytology; AUS carries an '
                                      'intermediate risk that needs refinement first.',
                                      'The sample had adequate cellularity; nondiagnostic, Bethesda I, means '
                                      'insufficient cells, which is a different category.',
                                      'Correct.'],
                        'board_pearl': 'Bethesda III or IV means indeterminate risk, not a diagnosis; refine with '
                                       'repeat FNA, molecular testing or lobectomy.',
                        'curveball': 'Why does local malignancy prevalence change the positive and negative predictive '
                                     'value of a molecular test?',
                        'curveball_answer': 'Predictive values depend on prevalence. With the same sensitivity and '
                                            'specificity, a higher pretest malignancy prevalence raises the positive '
                                            'predictive value and weakens the reassurance of a negative result; a '
                                            'lower prevalence does the reverse. Interpret the result with ultrasound, '
                                            'cytology and the local population tested.'}}
