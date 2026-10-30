"""v491 rewrites: Laryngology / Voice / Swallowing part 1 (lar1)."""

REWRITES = {'v11_lar_01': {'stem': 'A 47-year-old woman has a breathy voice and coughs with thin liquids 3 '
                        'days after total thyroidectomy. Intubation was a single uncomplicated '
                        'pass, and the operative note records loss of the left nerve-monitoring '
                        'signal after dissection near the ligament of Berry. Laryngoscopy shows '
                        'the left fold immobile in a paramedian position with a glottic gap; the '
                        'right fold abducts fully, and she has no stridor. What is the most likely '
                        'diagnosis?',
                'choices': ['Left recurrent laryngeal nerve paralysis',
                            'Left arytenoid dislocation from intubation',
                            'Bilateral paralysis with right-sided recovery',
                            'External superior laryngeal nerve branch injury'],
                'answer': 0,
                'explanation': 'Loss of signal on intraoperative neuromonitoring after dissection '
                               'at the ligament of Berry, where the recurrent laryngeal nerve '
                               'enters the larynx, localizes the injury. The RLN supplies every '
                               'intrinsic muscle except the cricothyroid, so the fold rests '
                               'paramedian, leaves a glottic gap, and causes breathy voice and '
                               'thin-liquid aspiration. A smooth single-pass intubation makes '
                               'arytenoid dislocation unlikely, and full right abduction without '
                               'stridor excludes a bilateral process. Next steps are documenting '
                               'the gap and aspiration risk and planning for possible recovery.',
                'why_wrong': ['Correct.',
                              'Dislocation follows traumatic or difficult intubation; a smooth '
                              'single pass plus signal loss at the nerve entry point favors neural '
                              'injury.',
                              'The right fold abducts fully and the airway is quiet, so there is '
                              'no evidence the right nerve was ever involved.',
                              'External branch injury impairs cricothyroid tension and high pitch '
                              'but leaves both folds mobile without a glottic gap or aspiration.'],
                'board_pearl': 'RLN injury leaves a paramedian immobile fold; external SLN injury '
                               'leaves mobile folds with lost high pitch.',
                'curveball': 'The nerve monitor signal returned at the end of the case after a '
                             'temporary drop. How does that change your counseling about recovery?',
                'curveball_answer': 'Return of signal before closure suggests a neurapraxic, '
                                    'nontransecting injury with a good chance of spontaneous '
                                    'recovery, usually over weeks to a few months and occasionally '
                                    'up to 12 months. Counsel her that recovery is likely, follow '
                                    'motion with serial laryngoscopy, and treat aspiration or '
                                    'voice disability in the meantime with therapy or temporary '
                                    'injection rather than permanent medialization.'},
 'v116-lar-03': {'stem': 'A 66-year-old man who smoked for 40 years has 2 months of breathy '
                         'dysphonia and coughing with liquids. He has had no neck, chest, or spine '
                         'surgery and no recent intubation. Laryngoscopy shows the left fold '
                         'immobile in a paramedian position with no mucosal lesion. The neck is '
                         'soft without masses, and cranial nerve examination is otherwise normal. '
                         'What is the most appropriate next step?',
                 'choices': ['Laryngeal EMG to confirm an idiopathic neuropathy',
                             'Voice therapy with repeat laryngoscopy in 6 months',
                             'Contrast CT from the skull base through the aortic arch',
                             'Contrast CT of the neck from the hyoid to clavicles'],
                 'answer': 2,
                 'explanation': 'Unexplained unilateral paralysis is a finding that demands a '
                                'cause. The left recurrent laryngeal nerve descends with the '
                                'vagus, loops under the aortic arch at the aortopulmonary window, '
                                'and climbs the tracheoesophageal groove, so lung cancer, '
                                'mediastinal nodes, thyroid and esophageal tumors, and skull base '
                                'lesions can all present this way. In a heavy smoker without '
                                'iatrogenic explanation, contrast CT covering the entire course is '
                                'the key study before labeling the paralysis idiopathic or '
                                'planning permanent treatment.',
                 'why_wrong': ['EMG can help with prognosis or fixation, but it cannot find a '
                               'tumor compressing the nerve and does not replace imaging.',
                               'Waiting 6 months in a heavy smoker with unexplained paralysis '
                               'risks delaying diagnosis of a thoracic or neck malignancy.',
                               'Correct.',
                               'Stopping at the clavicles misses the intrathoracic course of the '
                               'left nerve, where lung and mediastinal tumors cause paralysis.'],
                 'board_pearl': 'Unexplained left vocal fold paralysis: image skull base to aortic '
                                'arch before calling it idiopathic.',
                 'curveball': 'CT is normal. How should the absence of an identified cause shape '
                              'the timing of augmentation?',
                 'curveball_answer': 'With a normal scan the paralysis is presumed idiopathic, and '
                                     'many idiopathic cases recover within 6 to 12 months. For '
                                     'aspiration or significant voice disability, offer temporary '
                                     'injection augmentation now rather than waiting. Defer '
                                     'permanent thyroplasty until the recovery window passes or '
                                     'EMG shows a poor prognosis, and keep reexamining for a '
                                     'late-appearing cause.'},
 'v249_lar_uvfp_fnd': {'stem': 'A 61-year-old man has a weak, breathy voice and coughs when '
                               'drinking water 1 week after anterior cervical discectomy and '
                               'fusion through a right neck approach. He has no stridor and has '
                               'never had voice trouble. Stroboscopy shows a bowed right fold that '
                               'neither abducts nor adducts, a persistent glottic gap, and marked '
                               'false fold squeezing on phonation. Which diagnosis best fits?',
                       'choices': ['Primary muscle tension dysphonia after anesthesia',
                                   'Recurrent laryngeal nerve paralysis from retraction',
                                   'Adductor spasmodic dysphonia unmasked by surgery',
                                   'Bilateral vocal fold paresis from cuff pressure'],
                       'answer': 1,
                       'explanation': 'Anterior cervical spine surgery injures the recurrent '
                                      'laryngeal nerve through retractor compression or stretch, '
                                      'often combined with endotracheal cuff pressure against the '
                                      'nerve as it enters the larynx. A fold that neither abducts '
                                      'nor adducts, with a glottic gap and aspiration of thin '
                                      'liquids, is a paralysis. The false fold squeeze is '
                                      'compensatory hyperfunction, not a primary disorder; '
                                      'treating the gap usually relieves it. Immobility is a '
                                      'finding, so follow-up should confirm the expected '
                                      'iatrogenic cause and track recovery.',
                       'why_wrong': ['Supraglottic squeeze here compensates for a gap from an '
                                     'immobile fold; primary MTD requires normal fold motion and '
                                     'closure.',
                                     'Correct.',
                                     'Spasmodic dysphonia causes task-specific strained breaks '
                                     'with normal mobility, not a fixed immobile fold with a gap.',
                                     'Only the right fold is immobile and the airway is quiet, so '
                                     'the findings are unilateral rather than bilateral.'],
                       'board_pearl': 'Supraglottic squeeze over an immobile fold is compensation '
                                      'for the gap, not primary muscle tension dysphonia.',
                       'curveball': 'At follow-up he also has right palatal droop, nasal '
                                    'regurgitation, and pooling in the right piriform sinus. What '
                                    'does that imply?',
                       'curveball_answer': 'Palatal weakness, pharyngeal pooling, and reduced '
                                           'supraglottic sensation point to a high vagal lesion '
                                           'above the pharyngeal and superior laryngeal branches, '
                                           'not an isolated RLN injury from neck retraction. That '
                                           'is not explained by the spine approach, so image the '
                                           'skull base and upper neck. High vagal injury causes '
                                           'worse dysphagia, often needs earlier medialization, '
                                           'and may need arytenoid adduction for the posterior '
                                           'gap.'},
 'v249_lar_uvfp_app': {'stem': 'A 58-year-old woman has 5 weeks of breathy voice after a viral '
                               'illness. An outside physician obtained a normal MRI of the brain '
                               'and a normal thyroid ultrasound and labeled the left vocal fold '
                               'paralysis idiopathic. She has no prior surgery but a 20 pack-year '
                               'smoking history and mild weight loss. Laryngoscopy confirms left '
                               'fold immobility without a mass. Which region most needs imaging '
                               'next?',
                       'choices': ['Jugular foramen and posterior skull base',
                                   'Cerebellopontine angle and internal auditory canal',
                                   'Retropharyngeal space above the hyoid bone',
                                   'Aortopulmonary window and upper mediastinum'],
                       'answer': 3,
                       'explanation': 'The left recurrent laryngeal nerve hooks beneath the aortic '
                                      'arch beside the ligamentum arteriosum, so the '
                                      'aortopulmonary window and upper mediastinum are the most '
                                      'common sites of occult compressing disease such as lung '
                                      'cancer, nodal metastases, and aortic aneurysm. Her brain '
                                      'MRI and thyroid ultrasound leave that segment unstudied, '
                                      'and smoking with weight loss raises concern for thoracic '
                                      'malignancy. Imaging should cover the vagus and recurrent '
                                      'nerve from skull base to the aortic arch before accepting '
                                      'an idiopathic label.',
                       'why_wrong': ['Jugular foramen lesions usually cause multiple cranial '
                                     'neuropathies, and a normal brain MRI already images much of '
                                     'this region.',
                                     'Cerebellopontine angle lesions produce hearing loss and '
                                     'imbalance, not isolated vocal fold paralysis, and were '
                                     'covered by her MRI.',
                                     'A retropharyngeal lesion is possible but far less likely '
                                     'than thoracic disease given her left side, smoking, and '
                                     'weight loss.',
                                     'Correct.'],
                       'board_pearl': 'The left RLN loops under the aortic arch, so left paralysis '
                                      'requires imaging of the mediastinum.',
                       'curveball': 'The paralysis is on the right instead. How does that change '
                                    'the inferior extent of imaging?',
                       'curveball_answer': 'The right recurrent nerve loops beneath the subclavian '
                                           'artery at the thoracic inlet, so it has no aortic arch '
                                           'segment. Imaging should still run from the skull base '
                                           'to the right subclavian loop and lung apex, where '
                                           'apical lung tumors, thyroid disease, and cervical '
                                           'nodes cause right paralysis. The left side requires '
                                           'extension deeper into the mediastinum.'},
 'v249_lar_uvfp_snr': {'stem': 'A 63-year-old woman has a severely breathy voice and coughs with '
                               'every sip 6 weeks after left upper lobectomy. The nerve was not '
                               'seen divided. FEES shows thin-liquid aspiration with a weak cough, '
                               'and she was treated for pneumonia last week. The left fold is '
                               'immobile and paramedian with a moderate gap. What is the best '
                               'intervention now?',
                       'choices': ['Medialization thyroplasty with a permanent implant',
                                   'Ansa cervicalis to recurrent laryngeal nerve reinnervation',
                                   'Temporary injection augmentation with a resorbable gel',
                                   'Thickened liquids and reassessment of motion in 9 months'],
                       'answer': 2,
                       'explanation': 'Her nerve was not seen divided, so spontaneous recovery '
                                      'remains possible, yet aspiration has already caused '
                                      'pneumonia. Temporary injection laryngoplasty medializes the '
                                      'fold within days, restores glottic closure for cough and '
                                      'swallow, and does not prevent or mask neural recovery. '
                                      'Permanent framework surgery is deferred until recovery is '
                                      'unlikely. Significant aspiration is an indication for early '
                                      'intervention rather than waiting out the 6 to 12 month '
                                      'recovery window, particularly after lung resection with '
                                      'reduced pulmonary reserve.',
                       'why_wrong': ['Permanent medialization is premature when the nerve may '
                                     'recover, though it becomes reasonable once recovery is '
                                     'unlikely.',
                                     'Reinnervation restores tone only after months and does not '
                                     'protect her airway during the period of active aspiration.',
                                     'Correct.',
                                     'Diet modification alone leaves the glottic gap open, and '
                                     'waiting months risks more pneumonia in a patient with '
                                     'reduced lung capacity.'],
                       'board_pearl': 'Aspiration from recent unilateral paralysis: inject '
                                      'temporarily now, and decide on permanent surgery later.',
                       'curveball': 'After injection she still has a large posterior gap and the '
                                    'paralyzed fold sits higher than the other. What would you '
                                    'consider if recovery fails?',
                       'curveball_answer': 'A large posterior gap and vertical level mismatch are '
                                           'not corrected well by injection or thyroplasty alone, '
                                           'which mainly medialize the membranous fold. Arytenoid '
                                           'adduction rotates the vocal process medially and down '
                                           'to close the posterior glottis and level the folds, '
                                           'usually combined with medialization thyroplasty. This '
                                           'geometry is typical of high vagal or thoracic injury.'},
 'v11_lar_02': {'stem': 'A 52-year-old woman is extubated after total thyroidectomy for a large '
                        'substernal goiter and within minutes develops high-pitched inspiratory '
                        'stridor and suprasternal retractions. Her voice is surprisingly clear. '
                        'Oxygen saturation is 91% on face mask. Bedside flexible laryngoscopy '
                        'shows both vocal folds resting near the midline with almost no abduction '
                        'on inspiration and no hematoma. What is the immediate concern?',
                'choices': ['Glottic airway obstruction from bilateral fold immobility',
                            'Tracheomalacia from long-standing goiter compression',
                            'Wound hematoma causing laryngeal venous congestion',
                            'Hypocalcemic laryngospasm from parathyroid injury'],
                'answer': 0,
                'explanation': 'Paramedian folds preserve voice because they still meet for '
                               'phonation, but they leave only a slit for inspiration, so stridor '
                               'appears soon after extubation. Laryngoscopy showing midline folds '
                               'that fail to abduct after bilateral thyroid surgery points to '
                               'bilateral recurrent laryngeal nerve injury or neurapraxia. This is '
                               'an airway emergency: reintubation with a small tube or '
                               'tracheostomy comes first, followed later by deciding whether the '
                               'paralysis is temporary or permanent.',
                'why_wrong': ['Correct.',
                              'Tracheomalacia after goiter is uncommon and causes collapse below '
                              'the glottis, while laryngoscopy here shows the obstruction at the '
                              'folds.',
                              'No hematoma is present, and a hematoma would not explain midline '
                              'folds that fail to abduct with inspiration.',
                              'Hypocalcemic laryngospasm typically appears a day or more later '
                              'with paresthesias or tetany, not minutes after extubation.'],
                'board_pearl': 'Bilateral paramedian paralysis: good voice, poor airway; secure '
                               'the airway before anything else.',
                'curveball': 'She is reintubated and stable, but a leak test fails twice over a '
                             'week. What temporary and irreversible airway options would you '
                             'discuss?',
                'curveball_answer': 'Tracheostomy is the reversible bridge that allows time for '
                                    'possible nerve recovery, which can take up to about 12 '
                                    'months. Glottic suture lateralization is another reversible '
                                    'option. Irreversible widening with posterior cordotomy or '
                                    'partial arytenoidectomy should wait until recovery is '
                                    'unlikely, because it trades a better airway for a breathier '
                                    'voice and some aspiration risk.'},
 'v116-lar-01': {'stem': 'A 59-year-old man has inspiratory stridor 2 weeks after total '
                         'thyroidectomy. He was intubated for 9 days after surgery because of '
                         'postoperative pneumonia and needed two reintubations. Flexible '
                         'laryngoscopy shows both folds near the midline with minimal abduction '
                         'and erythematous granulation between the arytenoids. Neuromonitoring '
                         'signal was normal on both sides at the end of surgery. Which possibility '
                         'most needs exclusion before diagnosing bilateral nerve paralysis?',
                 'choices': ['Adductor laryngeal dystonia triggered by intubation',
                             'Bilateral superior laryngeal nerve traction injury',
                             'Inducible laryngeal obstruction from postoperative anxiety',
                             'Posterior glottic scar fixing the cricoarytenoid joints'],
                 'answer': 3,
                 'explanation': 'Bilateral immobility is a finding, not a mechanism. His preserved '
                                'monitoring signal argues against nerve injury, while prolonged '
                                'intubation with reintubations and interarytenoid granulation '
                                'suggest posterior glottic injury that can scar or ankylose the '
                                'cricoarytenoid joints. Mechanical fixation looks like paralysis '
                                'on flexible laryngoscopy, but treatment differs: scar release or '
                                'posterior grafting instead of waiting for nerve recovery. Direct '
                                'laryngoscopy with arytenoid palpation and, if helpful, laryngeal '
                                'EMG separate the two.',
                 'why_wrong': ['Laryngeal dystonia produces task-specific phonatory spasms with '
                               'normal respiratory abduction, not fixed midline folds with '
                               'stridor.',
                               'Superior laryngeal nerve injury affects cricothyroid pitch control '
                               'and sensation but does not cause midline folds or inspiratory '
                               'stridor.',
                               'Inducible laryngeal obstruction is episodic and the folds abduct '
                               'normally between episodes, unlike this persistent immobility.',
                               'Correct.'],
                 'board_pearl': 'Bilateral immobility after prolonged intubation: palpate the '
                                'arytenoids before calling it nerve paralysis.',
                 'curveball': 'Under anesthesia the arytenoids move freely on palpation. What does '
                              'laryngeal EMG add at this point?',
                 'curveball_answer': 'Free passive mobility excludes joint fixation, which makes '
                                     'neurogenic paralysis the working diagnosis. EMG then grades '
                                     'denervation: fibrillations and absent motor units suggest a '
                                     'poor prognosis, while polyphasic reinnervation potentials or '
                                     'preserved recruitment predict recovery. That helps decide '
                                     'between waiting with a tracheostomy and earlier permanent '
                                     'glottic widening.'},
 'v135_lary_01': {'stem': 'A 45-year-old woman has rising inspiratory stridor in the recovery unit '
                          '40 minutes after total thyroidectomy. Her neck is flat with no swelling '
                          'and the drain output is minimal. She speaks in full sentences but is '
                          'using accessory muscles, and oxygen saturation is falling to 89%. '
                          'Laryngoscopy shows both folds near the midline with minimal abduction. '
                          'What is the immediate priority?',
                  'choices': ['Bilateral injection augmentation to improve cough strength',
                              'Secure the airway now and determine recovery potential later',
                              'Laryngeal EMG to separate neural injury from fixation',
                              'Urgent neck exploration to inspect both recurrent laryngeal nerves'],
                  'answer': 1,
                  'explanation': 'This patient has a critically narrow glottis with escalating '
                                 'work of breathing and falling saturation. Airway control by '
                                 'reintubation with a small tube or tracheostomy comes before any '
                                 'diagnostic or functional decision. Whether the injury is '
                                 'neurapraxia, which may recover over weeks to months, or '
                                 'permanent paralysis is decided once she is safe. A flat neck '
                                 'with low drain output argues against hematoma, so the folds '
                                 'themselves are the obstruction.',
                  'why_wrong': ['Injection medializes the folds and would worsen an already '
                                'narrowed glottic airway in bilateral paralysis.',
                                'Correct.',
                                'EMG helps with prognosis but it is an elective study that should '
                                'not delay securing a deteriorating airway.',
                                'Reexploration may matter if transection is suspected, but it is '
                                'not the first step while she is hypoxic and stridorous.'],
                  'board_pearl': 'New stridor with bilateral midline folds after thyroidectomy: '
                                 'secure the airway first, then sort out prognosis.',
                  'curveball': 'Twelve months later EMG shows no reinnervation and she remains '
                               'tracheostomy dependent. What are the trade-offs of posterior '
                               'cordotomy or arytenoidectomy?',
                  'curveball_answer': 'Both widen the posterior glottis enough for many patients '
                                      'to be decannulated, but each removes glottic tissue '
                                      'permanently. Expect a breathier, weaker voice and some risk '
                                      'of aspiration, especially after more extensive or bilateral '
                                      'resection. Start with a unilateral, limited procedure and '
                                      'revise if the airway is still inadequate, matching the '
                                      'extent to how much she values voice versus airway.'},
 'v249_lar_bvfi_fnd': {'stem': 'A 38-year-old woman had total thyroidectomy with central neck '
                               'dissection for papillary carcinoma 4 days ago. Since discharge she '
                               'has developed noisy breathing with exertion and at night, but her '
                               'husband says her voice sounds normal. Saturation at rest is 96%. '
                               'Flexible laryngoscopy shows both folds resting in a paramedian '
                               'position with no abduction on sniffing and no mucosal lesion. What '
                               'is the immediate concern?',
                       'choices': ['A critically narrowed airway from bilateral fold paralysis',
                                   'Unilateral paralysis with full compensation by the other fold',
                                   'Supraglottic edema from extended neck dissection',
                                   'Phonotraumatic nodules from postoperative throat clearing'],
                       'answer': 0,
                       'explanation': 'Both folds sit paramedian and fail to abduct, the pattern '
                                      'of bilateral recurrent laryngeal nerve injury after central '
                                      'neck surgery. Because the folds meet at midline, voice is '
                                      'preserved, which falsely reassures patients and clinicians, '
                                      'but the inspiratory airway is a narrow slit that can '
                                      'decompensate with exertion, sleep, or a respiratory '
                                      'infection. Airway adequacy is the priority, and her '
                                      'admission and airway plan come before the later '
                                      'differential of neurogenic paralysis versus mechanical '
                                      'fixation.',
                       'why_wrong': ['Correct.',
                                     'Neither fold abducts on sniff, so this is bilateral '
                                     'immobility; a unilateral paralysis would leave one fold '
                                     'moving normally.',
                                     'Supraglottic edema would show swollen arytenoids and false '
                                     'folds rather than isolated failure of fold abduction.',
                                     'Nodules cause hoarseness with mobile folds; they cannot '
                                     'explain exertional stridor with absent abduction.'],
                       'board_pearl': 'A normal voice with exertional stridor after thyroidectomy '
                                      'suggests bilateral paramedian paralysis.',
                       'curveball': 'Her stridor is stable and she declines tracheostomy. Which '
                                    'examination later distinguishes neurogenic paralysis from '
                                    'scar or joint fixation?',
                       'curveball_answer': 'Direct laryngoscopy under anesthesia with palpation of '
                                           'each arytenoid tests passive cricoarytenoid mobility '
                                           'and reveals interarytenoid or posterior commissure '
                                           'scar. Freely mobile arytenoids point to neurogenic '
                                           'paralysis, while restricted motion or scar indicates '
                                           'mechanical fixation. Laryngeal EMG adds evidence of '
                                           'denervation or reinnervation when the mechanism or '
                                           'prognosis remains uncertain.'},
 'v249_lar_bvfi_app': {'stem': 'A 64-year-old man has had stridor and failed decannulation since a '
                               '4-week ICU stay for septic shock 5 months ago. He had a '
                               'percutaneous tracheostomy on day 14. Flexible laryngoscopy shows '
                               'both folds near midline with minimal abduction and a smooth band '
                               'of mucosa between the vocal processes, but whether the joints are '
                               'fixed is unclear. What is the best next diagnostic step?',
                       'choices': ['Contrast CT from the skull base through the aortic arch',
                                   'Videostroboscopy to assess the mucosal wave of each fold',
                                   'Direct laryngoscopy with palpation of both arytenoids',
                                   'Repeat flexible laryngoscopy after a trial of PPI'],
                       'answer': 2,
                       'explanation': 'After prolonged intubation, bilateral immobility may be '
                                      'neurogenic, mechanical from posterior glottic scar or joint '
                                      'ankylosis, or both. The mucosal band between the vocal '
                                      'processes suggests a posterior glottic synechia, and '
                                      'flexible laryngoscopy cannot test passive mobility. Direct '
                                      'laryngoscopy with palpation of each arytenoid defines scar '
                                      'and fixation and also allows inspection of the subglottis '
                                      'and the tracheostomy site for coexisting stenosis. '
                                      'Laryngeal EMG supplements palpation when a neurogenic '
                                      'component remains possible.',
                       'why_wrong': ['Imaging the nerve course suits unexplained paralysis, but '
                                     'this history points to intubation injury that needs '
                                     'mechanical assessment.',
                                     'Stroboscopy assesses vibratory mucosa and closure, not '
                                     'whether the cricoarytenoid joints can move passively.',
                                     'Correct.',
                                     'Reflux treatment does not reverse a mature posterior glottic '
                                     'scar, and repeating office laryngoscopy cannot answer the '
                                     'mechanical question.'],
                       'board_pearl': 'Palpation under anesthesia separates cricoarytenoid '
                                      'fixation from paralysis; EMG adds neural information.',
                       'curveball': 'Palpation shows a dense interarytenoid scar band but both '
                                    'arytenoids move once it is divided. How does that change the '
                                    'operative plan?',
                       'curveball_answer': 'A scar band tethering mobile joints is a Bogdasarian '
                                           'type I or II posterior glottic stenosis, so the plan '
                                           'is endoscopic division of the scar with mucosal '
                                           'advancement flaps to limit restenosis, not destructive '
                                           'widening. Preserved joint mobility and intact nerves '
                                           'mean abduction may return after release, protecting '
                                           'voice and swallowing. Fixed joints would instead '
                                           'require posterior cricoid grafting or cordotomy.'},
 'v249_lar_bvfi_snr': {'stem': 'A 57-year-old female schoolteacher has had a tracheostomy for 3 '
                               'years after bilateral vocal fold paralysis from total '
                               'thyroidectomy. Laryngoscopy shows both folds paramedian; EMG at 14 '
                               'months showed denervation without reinnervation. She speaks well '
                               'with valve occlusion, has no aspiration, and wants decannulation '
                               'but worries about losing her teaching voice. What is the best '
                               'plan?',
                       'choices': ['Bilateral total arytenoidectomy in one single-stage operation',
                                   'Unilateral posterior cordotomy with staged revision if needed',
                                   'Bilateral thyroarytenoid botulinum toxin to widen the glottis',
                                   'Medialization thyroplasty to improve vocal efficiency'],
                       'answer': 1,
                       'explanation': 'With permanent bilateral paralysis, any static widening '
                                      'procedure trades phonatory resistance and some airway '
                                      'protection for inspiratory airflow. Starting with a limited '
                                      'unilateral posterior cordotomy or partial arytenoidectomy '
                                      'can achieve decannulation for many patients while '
                                      'preserving more voice. Revision or contralateral surgery is '
                                      'added only if the airway remains inadequate. Her strong '
                                      'voice demands and lack of aspiration favor the least '
                                      'resection that will allow decannulation, with honest '
                                      'counseling about breathiness.',
                       'why_wrong': ['Extensive bilateral resection at once maximizes airway but '
                                     'carries the highest risk of breathy voice and aspiration for '
                                     'a voice-dependent teacher.',
                                     'Correct.',
                                     'Toxin weakens the adductors only temporarily and does not '
                                     'create a durable airway in permanent bilateral paralysis.',
                                     'Medialization narrows the glottis and would worsen her '
                                     'airway; it treats insufficiency, not bilateral paramedian '
                                     'obstruction.'],
                       'board_pearl': 'Bilateral paralysis surgery trades voice for airway; start '
                                      'unilateral and limited, then revise if needed.',
                       'curveball': 'She asks about options that might widen the airway without '
                                    'removing tissue. When would reinnervation or laryngeal pacing '
                                    'be considered?',
                       'curveball_answer': 'Selective reinnervation, such as phrenic nerve '
                                           'branches to the posterior cricoarytenoid with adductor '
                                           'denervation, aims to restore inspiratory abduction '
                                           'without resection, but it is offered at few centers '
                                           'and results vary. Implanted laryngeal pacing of the '
                                           'posterior cricoarytenoid remains investigational or '
                                           'limited in availability. Both need viable muscle and '
                                           'joints, so they are discussed as alternatives at '
                                           'specialized centers.'},
 'v11_lar_03': {'stem': 'A 46-year-old female call center manager has 18 months of strained, '
                        'strangled voice breaks that are worse on the telephone and with '
                        "vowel-initial words such as 'eggs' and 'apple.' Her voice is nearly "
                        'normal when she laughs, whispers, or sings. Laryngoscopy shows '
                        'intermittent hyperadduction of the true and false folds during connected '
                        'speech with normal motion at rest and no lesion. What is the most likely '
                        'diagnosis?',
                'choices': ['Primary muscle tension dysphonia',
                            'Essential tremor of the larynx',
                            'Abductor spasmodic dysphonia',
                            'Adductor spasmodic dysphonia'],
                'answer': 3,
                'explanation': 'Adductor spasmodic dysphonia is a focal laryngeal dystonia with '
                               'involuntary adductor spasms during speech. The deciding clue is '
                               'task specificity: breaks cluster on voiced sounds and '
                               'vowel-initial words, worsen with stress and telephone use, and '
                               'nearly disappear with laughing, whispering, and singing, which use '
                               'different motor programs. Muscle tension dysphonia is typically '
                               'consistent across tasks. The larynx looks structurally normal with '
                               'normal motion between spasms, so diagnosis rests on perceptual '
                               'testing and task-based examination.',
                'why_wrong': ['Primary muscle tension dysphonia usually strains the voice '
                              'consistently across speech, singing, and laughter rather than '
                              'sparing specific tasks.',
                              'Laryngeal tremor causes rhythmic regular oscillation present on '
                              'sustained vowels and at rest, not irregular task-specific breaks.',
                              'Abductor dysphonia causes breathy breaks on voiceless consonants, '
                              'not strained breaks on vowel-initial voiced words.',
                              'Correct.'],
                'board_pearl': 'Adductor SD: strangled breaks on voiced and vowel-initial words, '
                               'spared by whispering, laughing, and singing.',
                'curveball': 'She also has a regular 5 Hz voice tremor that persists on sustained '
                             'vowels and quiet breathing. What should you consider before '
                             'injecting toxin?',
                'curveball_answer': 'A regular oscillation that persists on sustained vowels and '
                                    'at rest suggests essential vocal tremor, alone or with '
                                    'dystonia. Examine the palate, pharynx, and larynx during '
                                    'sustained phonation and look for limb or head tremor. Tremor '
                                    'responds less predictably to thyroarytenoid toxin, so set '
                                    'expectations and adjust dosing and targets to the observed '
                                    'pattern.'},
 'v141_lar_03': {'stem': 'A 52-year-old male pastor has 3 years of choppy, strained voice breaks '
                         'that make sermons exhausting. Breaks occur on voiced sounds, worsen with '
                         'stress, and nearly disappear when he whispers or laughs. Laryngoscopy '
                         'shows intermittent adductor spasms with normal fold structure and '
                         'mobility. Six months of voice therapy gave little benefit, and he wants '
                         'the most effective procedural option. What is the standard first-line '
                         'procedural therapy?',
                 'choices': ['Selective adductor denervation and reinnervation',
                             'Bilateral posterior cricoarytenoid botulinum toxin',
                             'EMG-guided thyroarytenoid botulinum toxin injection',
                             'Type II lateralization thyroplasty'],
                 'answer': 2,
                 'explanation': 'Botulinum toxin chemodenervation of the thyroarytenoid and '
                                'lateral cricoarytenoid complex is the standard first-line '
                                'procedural treatment for adductor spasmodic dysphonia. Toxin '
                                'blocks acetylcholine release, weakening the dystonic adductors '
                                'for about 3 to 4 months, so it must be repeated. Doses are '
                                'titrated to balance fluent voice against the expected early '
                                'breathiness and mild thin-liquid dysphagia. Surgical options such '
                                'as selective denervation-reinnervation or type II thyroplasty are '
                                'reserved for patients who want a durable alternative after toxin.',
                 'why_wrong': ['Denervation-reinnervation surgery is a durable second-line option '
                               'for selected patients, not the initial procedural treatment.',
                               'The posterior cricoarytenoid is the abductor and is targeted for '
                               'abductor dysphonia, not adductor spasms.',
                               'Correct.',
                               'Type II thyroplasty is a surgical alternative used mainly in some '
                               'centers; toxin remains the standard first procedure.'],
                 'board_pearl': 'Adductor SD: thyroarytenoid toxin every 3 to 4 months is the '
                                'standard; expect transient breathiness.',
                 'curveball': "His brother has breathy breaks on words such as 'puppy' and "
                              "'hockey.' Which muscle is targeted in that phenotype?",
                 'curveball_answer': 'Breathy breaks on voiceless consonants suggest abductor '
                                     'spasmodic dysphonia, treated with botulinum toxin into the '
                                     'posterior cricoarytenoid, the only abductor. Inject one side '
                                     'first or stage bilateral doses, because weakening both '
                                     'abductors can narrow the glottic airway and cause stridor. '
                                     'Response is usually less complete than with '
                                     'adductor-targeted injection.'},
 'v255_lar_sd_fnd': {'stem': 'A 39-year-old male attorney has 2 years of a tight, effortful voice '
                             'with abrupt stoppages in mid-sentence, most noticeable in court. '
                             "Reading 'We mow our lawn all year' provokes frequent breaks, but "
                             'counting from 60 to 70 is fluent. He sings in a choir without '
                             'difficulty. Flexible examination shows no mass and normal fold '
                             'mobility between breaks. What is the most likely diagnosis?',
                     'choices': ['Adductor laryngeal dystonia',
                                 'Abductor laryngeal dystonia',
                                 'Glottic insufficiency from paresis',
                                 'Psychogenic functional aphonia'],
                     'answer': 0,
                     'explanation': "The all-voiced sentence 'We mow our lawn all year' provokes "
                                    'adductor spasms, whereas counting from 60 to 70, loaded with '
                                    "voiceless 's' and 'x' sounds, does not. That pattern "
                                    'localizes the dystonia to the adductors. Preserved singing, '
                                    'normal mobility between breaks, and no lesion fit adductor '
                                    'laryngeal dystonia, also called adductor spasmodic dysphonia. '
                                    'Diagnosis is clinical, based on perceptual testing with '
                                    'voiced versus voiceless loaded sentences combined with '
                                    'endoscopy during connected speech.',
                     'why_wrong': ['Correct.',
                                   'Abductor dystonia is provoked by voiceless-loaded tasks such '
                                   'as counting from 60 to 70, which is fluent in this patient.',
                                   'Paresis causes a weak breathy voice with a gap and asymmetry, '
                                   'not strained task-specific stoppages with normal mobility.',
                                   'Functional aphonia is usually a whisper or loss of voice with '
                                   'preserved cough, not task-specific spasms that spare singing.'],
                     'board_pearl': 'Voiced-loaded sentences provoke adductor breaks; '
                                    'voiceless-loaded sentences such as counting 60 to 70 provoke '
                                    'abductor breaks.',
                     'curveball': 'His breaks occur mainly on counting from 60 to 70 and on '
                                  "'puppy,' with breathy segments. How does that change the "
                                  'phenotype?',
                     'curveball_answer': 'Breaks provoked by voiceless consonants with breathy '
                                         'segments indicate abductor laryngeal dystonia, where the '
                                         'posterior cricoarytenoid spasms and opens the glottis '
                                         'during speech. Confirm by observing abductor spasms '
                                         'endoscopically on voiceless words. Treatment shifts to '
                                         'toxin into the posterior cricoarytenoid, often '
                                         'unilateral first, while monitoring for airway '
                                         'restriction.'},
 'v255_lar_sd_app': {'stem': 'A 68-year-old female retired nurse with adductor spasmodic dysphonia '
                             'confirmed by perceptual testing and endoscopy remains significantly '
                             'limited despite voice therapy. She has COPD and was hospitalized '
                             'last winter for aspiration pneumonia, and FEES shows trace '
                             'penetration with thin liquids at baseline. She asks to begin '
                             'botulinum toxin treatment. Which initial dosing approach is most '
                             'appropriate?',
                     'choices': ['Standard full bilateral thyroarytenoid doses at the first visit',
                                 'Posterior cricoarytenoid injection to avoid breathiness',
                                 'Defer toxin and proceed to selective denervation surgery',
                                 'Low-dose unilateral thyroarytenoid injection, then titrate'],
                     'answer': 3,
                     'explanation': 'Toxin into the thyroarytenoid and lateral cricoarytenoid '
                                    'complex is standard therapy, but its expected side effects '
                                    'are a breathy voice and transient thin-liquid aspiration from '
                                    'weakened glottic closure. Her COPD, prior aspiration '
                                    'pneumonia, and baseline penetration make that period '
                                    'dangerous. Starting with a low unilateral or carefully '
                                    'reduced dose, then titrating to response, controls spasms '
                                    'while limiting aspiration. Pairing injection with swallowing '
                                    'precautions and close follow-up is the safest path.',
                     'why_wrong': ['Full bilateral doses risk weeks of glottic incompetence and '
                                   'aspiration in a patient with poor reserve and prior pneumonia.',
                                   'The posterior cricoarytenoid is an abductor; injecting it does '
                                   'nothing for adductor spasms and could narrow her airway.',
                                   'Surgery is reserved for toxin failures or patients seeking '
                                   'durability, not a first step before a cautious toxin trial.',
                                   'Correct.'],
                     'board_pearl': 'Toxin for adductor SD weakens closure; start low and '
                                    'unilateral when aspiration risk is high.',
                     'curveball': 'After a unilateral low dose she has fluent speech for 10 weeks '
                                  'with no dysphagia. How would you adjust future injections?',
                     'curveball_answer': 'A good response without dysphagia supports continuing '
                                         'the same unilateral low dose and timing reinjection to '
                                         'her symptom return, usually around 3 to 4 months. If '
                                         'benefit wears off early or spasms persist, raise the '
                                         'dose in small steps or alternate sides before moving to '
                                         'bilateral injection. Track voice-related quality of life '
                                         'and swallowing at each visit.'},
 'v255_lar_sd_snr': {'stem': 'A 61-year-old man has received bilateral thyroarytenoid botulinum '
                             'toxin for presumed adductor spasmodic dysphonia for 6 years with '
                             'fading benefit despite steadily higher doses. He now notes head '
                             'shaking. Endoscopy shows rhythmic oscillation of the palate, '
                             'pharyngeal walls, and larynx at about 5 Hz on sustained vowels, plus '
                             'irregular breaks during speech. What is the best next step?',
                     'choices': ['Escalate the bilateral dose until breaks are abolished',
                                 'Re-phenotype the disorder for coexisting vocal tremor',
                                 'Test for neutralizing antibodies against the toxin',
                                 'Refer for psychotherapy as a functional voice disorder'],
                     'answer': 1,
                     'explanation': 'Rhythmic oscillation across the palate, pharynx, and larynx '
                                    'on sustained vowels, together with head tremor, indicates '
                                    'essential tremor, which can coexist with or mimic dystonia. '
                                    'Thyroarytenoid toxin targets adductor spasms but treats '
                                    'multilevel tremor only partly, so higher doses bring more '
                                    'breathiness without better control. The right move is to '
                                    'reexamine perceptually and endoscopically, map which '
                                    'structures oscillate, and tailor therapy to the observed '
                                    'pattern, possibly adding systemic tremor treatment through '
                                    'neurology.',
                     'why_wrong': ['Raising doses targets only the adductor component and '
                                   'increases breathiness and dysphagia while the tremor persists.',
                                   'Correct.',
                                   'Antibody resistance is uncommon with standard laryngeal doses '
                                   'and would not explain new rhythmic multilevel oscillation and '
                                   'head tremor.',
                                   'The rhythmic oscillation and head tremor are organic '
                                   'neurologic signs, not evidence of a functional voice '
                                   'disorder.'],
                     'board_pearl': 'Fading toxin response with rhythmic oscillation on sustained '
                                    'vowels: look for essential vocal tremor.',
                     'curveball': 'Which tasks and anatomic levels would you deliberately examine '
                                  'to separate dystonic breaks from tremor?',
                     'curveball_answer': "Have him sustain an 'ee' vowel, whisper, and read voiced "
                                         'and voiceless sentences while you watch the palate, '
                                         'pharyngeal walls, base of tongue, supraglottis, and '
                                         'folds. Tremor is regular and appears on sustained vowels '
                                         'and often at rest across several levels. Dystonic breaks '
                                         'are irregular, task-specific, and confined to connected '
                                         'speech at the glottis.'},
 'v11_lar_04': {'stem': 'A 73-year-old man has 2 years of progressive dysphagia for solids, '
                        'regurgitation of food he ate hours earlier, foul breath, and coughing '
                        'when he lies down at night. He has lost 3 kg. Examination of the oral '
                        'cavity, oropharynx, and larynx is normal, and there is no neck mass. '
                        'Which study best demonstrates the suspected structural disorder?',
                'choices': ['Barium esophagram',
                            'High-resolution esophageal manometry',
                            'Flexible laryngoscopy with FEES',
                            'Contrast-enhanced CT of the neck'],
                'answer': 0,
                'explanation': 'Regurgitation of undigested food eaten hours earlier, halitosis, '
                               'and nocturnal cough in an older adult are classic for Zenker '
                               'diverticulum, a pulsion pouch through Killian dehiscence above the '
                               'cricopharyngeus. A barium esophagram is the standard diagnostic '
                               'study: it shows the posterior pouch, its size and neck, retained '
                               'contrast, and the cricopharyngeal bar, which guides choice between '
                               'endoscopic and open repair. It also screens the rest of the '
                               'esophagus for coexisting disease.',
                'why_wrong': ['Correct.',
                              'Manometry measures sphincter pressures and relaxation but does not '
                              'image the pouch or define its size for treatment planning.',
                              'FEES shows residue and aspiration in the hypopharynx but cannot '
                              'outline a pouch lying behind the esophagus.',
                              'CT may incidentally show a fluid-filled pouch but defines its size, '
                              'neck, and emptying poorly compared with contrast swallow.'],
                'board_pearl': 'Regurgitated undigested food and halitosis in an older adult: '
                               'order a barium esophagram for Zenker diverticulum.',
                'curveball': 'The pouch is only 1.5 cm and he has a stiff, kyphotic neck. How do '
                             'pouch size and exposure affect choosing endoscopic versus open '
                             'treatment?',
                'curveball_answer': 'Rigid endoscopic stapling needs good neck extension and a '
                                    'pouch of at least about 3 cm so the stapler can divide the '
                                    'common wall completely. A small pouch with poor exposure '
                                    'suits flexible endoscopic septotomy or Z-POEM, or an open '
                                    'cricopharyngeal myotomy with or without diverticulopexy. Very '
                                    'large pouches often do better with open diverticulectomy and '
                                    'myotomy.'},
 'v116-lar-02': {'stem': 'A 78-year-old woman has a year of food sticking high in her throat, '
                         'gurgling in the left neck after meals, and regurgitating pills swallowed '
                         'the previous evening. Her family notes foul breath and frequent throat '
                         'clearing. Cervical auscultation reveals a gurgle after a water swallow, '
                         'and laryngoscopy shows pooled secretions in both piriform sinuses. Which '
                         'diagnosis best fits?',
                 'choices': ['Achalasia of the lower esophageal sphincter',
                             'Oropharyngeal dysphagia from tongue weakness',
                             'Pharyngoesophageal pulsion diverticulum',
                             'Laryngopharyngeal reflux with globus sensation'],
                 'answer': 2,
                 'explanation': 'A Zenker diverticulum forms when high pressure above a poorly '
                                'compliant cricopharyngeus pushes mucosa through Killian '
                                'dehiscence, the weak triangle between the thyropharyngeus and the '
                                'cricopharyngeus. The pouch stores food and pills for hours, then '
                                'empties back into the pharynx, causing delayed regurgitation, '
                                'halitosis, aspiration, and the classic neck gurgle. Pooled '
                                'secretions in the piriform sinuses reflect overflow. Pills '
                                'regurgitated the next morning are a strong clue to a storage '
                                'pouch.',
                 'why_wrong': ['Achalasia causes retrosternal dysphagia and regurgitation from a '
                               'dilated distal esophagus, not cervical gurgling and high food '
                               'sticking.',
                               'Tongue weakness causes oral-phase difficulty with bolus control, '
                               'not delayed regurgitation of intact pills hours later.',
                               'Correct.',
                               'Reflux can cause throat clearing and globus but does not store and '
                               'regurgitate undigested food or pills.'],
                 'board_pearl': 'Delayed regurgitation of undigested food or pills plus neck '
                                'gurgling suggests Zenker diverticulum.',
                 'curveball': 'Which partition is divided during endoscopic treatment, and when '
                              'might an open approach be preferred?',
                 'curveball_answer': 'Endoscopic diverticulotomy divides the common party wall '
                                     'between pouch and esophagus, which contains the '
                                     'cricopharyngeus, so the cut is both septotomy and myotomy. '
                                     'An open approach is favored for poor neck extension, very '
                                     'small pouches where the wall is too short to divide, very '
                                     'large pouches, or suspicion of carcinoma in the pouch.'},
 'v253_lar_zenker_fnd': {'stem': 'A 70-year-old man has progressive dysphagia, regurgitation, '
                                 'halitosis, and two pneumonias in the past year. A barium swallow '
                                 'shows a 3-cm contrast-filled pouch projecting posteriorly from '
                                 'the pharyngoesophageal junction at C5-C6, arising just above a '
                                 'prominent cricopharyngeal bar and retaining contrast after the '
                                 'swallow. What is the diagnosis?',
                         'choices': ['Killian-Jamieson diverticulum',
                                     'Zenker diverticulum',
                                     'Epiphrenic diverticulum',
                                     'Lateral pharyngeal pouch'],
                         'answer': 1,
                         'explanation': 'A posterior pouch arising above the cricopharyngeus at '
                                        'the pharyngoesophageal junction is a Zenker diverticulum. '
                                        'It is a pulsion false diverticulum of mucosa and '
                                        'submucosa herniating through Killian dehiscence, between '
                                        'the oblique thyropharyngeus and the horizontal '
                                        'cricopharyngeus, driven by a poorly compliant upper '
                                        'esophageal sphincter. Retained contrast explains '
                                        'regurgitation and aspiration pneumonia. Treatment must '
                                        'divide the cricopharyngeus, because removing the pouch '
                                        'without myotomy leaves the underlying high pressure and '
                                        'allows recurrence.',
                         'why_wrong': ['Killian-Jamieson diverticula arise anterolaterally below '
                                       'the cricopharyngeus near the recurrent nerve entry, not '
                                       'posteriorly above it.',
                                       'Correct.',
                                       'Epiphrenic diverticula arise in the distal esophagus above '
                                       'the diaphragm, far below this cervical location.',
                                       'Lateral pharyngeal pouches protrude through the thyrohyoid '
                                       'membrane, usually in wind players, not posteriorly above '
                                       'the cricopharyngeus.'],
                         'board_pearl': 'Zenker: posterior pulsion pouch through Killian '
                                        'dehiscence above the cricopharyngeus; myotomy is '
                                        'essential.',
                         'curveball': 'Why does it matter during myotomy that the pouch arises '
                                      'above rather than below the cricopharyngeus?',
                         'curveball_answer': 'Because a Zenker pouch arises above the '
                                             'cricopharyngeus, dividing the party wall or the '
                                             'posterior muscle relieves the obstructing sphincter '
                                             'directly while staying in the midline away from the '
                                             'recurrent nerves. A Killian-Jamieson pouch lies '
                                             'below and lateral to the cricopharyngeus near where '
                                             'the recurrent nerve enters the larynx, so endoscopic '
                                             'division risks nerve injury and open repair is often '
                                             'preferred.'},
 'v253_lar_zenker_app': {'stem': 'A 79-year-old woman with a symptomatic 2.5-cm Zenker '
                                 'diverticulum and recurrent aspiration pneumonia has severe '
                                 'cervical kyphosis from ankylosing spondylitis and a small mouth '
                                 'opening. Her neck cannot extend, and the anesthesiologist rates '
                                 'her airway as very difficult. She has heart failure with reduced '
                                 'ejection fraction. Which treatment approach is best?',
                         'choices': ['Rigid transoral stapled diverticulotomy under anesthesia',
                                     'Diverticulectomy without cricopharyngeal myotomy',
                                     'Serial bougie dilation of the upper esophageal sphincter',
                                     'Flexible endoscopic septotomy or Z-POEM under sedation'],
                         'answer': 3,
                         'explanation': 'Rigid endoscopic stapling requires neck extension and '
                                        'adequate mouth opening to expose the party wall, which '
                                        'she lacks. Flexible endoscopic septotomy or a tunneling '
                                        'Z-POEM divides the septum and cricopharyngeus through a '
                                        'flexible scope without rigid exposure, often with less '
                                        'anesthetic stress, which suits a frail patient with heart '
                                        'failure. Whatever the approach, the essential element is '
                                        'a complete cricopharyngeal myotomy. Open repair remains '
                                        'an option in centers without flexible expertise when the '
                                        'patient can tolerate it.',
                         'why_wrong': ['Rigid stapling depends on exposure that her fused kyphotic '
                                       'neck and small mouth opening make impossible to achieve '
                                       'safely.',
                                       'Removing the pouch without myotomy leaves the '
                                       'high-pressure sphincter in place and invites recurrence or '
                                       'leak.',
                                       'Dilation stretches the sphincter only briefly and does not '
                                       'eliminate the pouch that stores food and causes '
                                       'aspiration.',
                                       'Correct.'],
                         'board_pearl': 'Poor neck extension with Zenker: choose flexible '
                                        'endoscopic or open repair, and always include myotomy.',
                         'curveball': 'How do very small or very large pouches change the '
                                      'technical pros and cons of endoscopic approaches?',
                         'curveball_answer': 'A very small pouch, under about 2 to 3 cm, leaves '
                                             'too little common wall for a stapler to divide '
                                             'fully, so flexible septotomy, Z-POEM, or open '
                                             'myotomy work better. A very large pouch can be '
                                             'divided endoscopically but may leave a residual sump '
                                             'and is often handled better with open '
                                             'diverticulectomy or diverticulopexy plus myotomy.'},
 'v253_lar_zenker_snr': {'stem': 'A 74-year-old man is admitted after endoscopic stapled '
                                 'diverticulotomy for a 4-cm Zenker diverticulum. Eight hours '
                                 'later he has a temperature of 38.6 C, heart rate of 118, '
                                 'worsening neck and chest pain, and crepitus over the left neck. '
                                 'Oral intake has not started. Which management step is most '
                                 'appropriate now?',
                         'choices': ['Clear liquids and oral analgesics with reassessment tomorrow',
                                     'Return to the OR for open diverticulectomy and myotomy',
                                     'NPO, IV antibiotics, and urgent contrast imaging for leak',
                                     'Begin a PPI and discharge with outpatient esophagram'],
                         'answer': 2,
                         'explanation': 'Fever, tachycardia, worsening neck and chest pain, and '
                                        'crepitus hours after diverticulotomy indicate '
                                        'pharyngoesophageal perforation with possible '
                                        'mediastinitis until proved otherwise. He should be made '
                                        'NPO, given broad-spectrum IV antibiotics, and imaged '
                                        'urgently with contrast esophagram or CT with oral '
                                        'contrast to define the leak. Stable contained leaks may '
                                        'be managed nonoperatively, but free extravasation, '
                                        'abscess, or sepsis requires drainage or operative source '
                                        'control. Delay increases mortality.',
                         'why_wrong': ['Starting oral intake despite signs of perforation would '
                                       'contaminate the neck and mediastinum further and worsen '
                                       'sepsis.',
                                       'Immediate open repair may be needed later, but imaging '
                                       'first defines whether the leak is contained or needs '
                                       'drainage.',
                                       'Correct.',
                                       'His systemic signs are inconsistent with routine '
                                       'postoperative odynophagia, so discharge would miss a '
                                       'dangerous leak.'],
                         'board_pearl': 'Fever, tachycardia, and crepitus after Zenker repair mean '
                                        'perforation until proven otherwise; NPO, antibiotics, '
                                        'contrast imaging.',
                         'curveball': 'CT shows a small contained leak at the staple line without '
                                      'mediastinal fluid, and he stabilizes. How would you manage '
                                      'it?',
                         'curveball_answer': 'A small contained leak in a stable patient can be '
                                             'managed nonoperatively with NPO status, IV '
                                             'antibiotics, nutrition through a nasogastric or '
                                             'enteral tube, and repeat contrast study before '
                                             'resuming oral intake. Watch closely for fever, '
                                             'rising white count, or new collections, which would '
                                             'require cervical drainage or mediastinal source '
                                             'control.'},
 'v11_lar_05': {'stem': 'A 50-year-old man has exertional dyspnea and inspiratory stridor 4 months '
                        'after a 3-week intubation for necrotizing pancreatitis. His voice is '
                        'nearly normal. Flexible laryngoscopy shows both folds abducting only a '
                        'few millimeters with pale scar at the posterior commissure. Laryngeal EMG '
                        'of both thyroarytenoid and posterior cricoarytenoid muscles shows normal '
                        'recruitment without fibrillations. Which diagnosis should be considered?',
                'choices': ['Posterior glottic stenosis with cricoarytenoid fixation',
                            'Bilateral recurrent laryngeal nerve paralysis',
                            'Bilateral abductor laryngeal dystonia',
                            'Idiopathic subglottic stenosis below the cricoid'],
                'answer': 0,
                'explanation': 'Prolonged intubation places the tube against the posterior '
                               'glottis, where pressure ischemia ulcerates the interarytenoid '
                               'mucosa and cricoarytenoid joints and heals as scar. The result is '
                               'mechanical limitation of abduction that looks like bilateral '
                               'paralysis. Normal EMG recruitment in both the adductors and the '
                               'posterior cricoarytenoid shows the nerves are intact, and '
                               'posterior commissure scar is visible, so posterior glottic '
                               'stenosis with joint fixation is the leading diagnosis. Operative '
                               'palpation confirms it.',
                'why_wrong': ['Correct.',
                              'Normal recruitment without fibrillations in both adductors and '
                              'abductors argues strongly against bilateral recurrent nerve '
                              'paralysis.',
                              'Dystonia produces task-specific spasms during speech, not '
                              'persistent limitation of abduction with visible posterior scar.',
                              'Subglottic stenosis narrows the airway below mobile folds; it does '
                              'not restrict fold abduction or scar the posterior commissure.'],
                'board_pearl': 'Limited abduction after intubation with normal EMG suggests '
                               'posterior glottic stenosis, not bilateral paralysis.',
                'curveball': 'Under anesthesia both arytenoids are fixed on palpation. How does '
                             'that confirm a mechanical cause and change strategy compared with '
                             'nerve paralysis?',
                'curveball_answer': 'Fixed arytenoids on passive palpation prove mechanical '
                                    'fixation, because a denervated joint still moves freely when '
                                    'pushed. Bilateral fixation corresponds to Bogdasarian type IV '
                                    'disease, which rarely responds to simple scar division. '
                                    'Options include posterior cricoid split with a rib cartilage '
                                    'graft or posterior cordotomy or arytenoidectomy, often with a '
                                    'temporary tracheostomy. Waiting for nerve recovery has no '
                                    'role.'},
 'v113-lar-01': {'stem': 'A 34-year-old woman has a breathy voice and weak cough immediately after '
                         'emergency surgery that required three intubation attempts with a rigid '
                         'stylet. She has no neck surgery history. On day 5, laryngoscopy shows an '
                         'immobile right fold with an anteriorly tilted, edematous arytenoid and a '
                         'height mismatch. Laryngeal EMG of the right thyroarytenoid shows normal '
                         'voluntary recruitment. Which diagnosis is most likely?',
                 'choices': ['Right recurrent laryngeal nerve neurapraxia from cuff',
                             'Right vocal process granuloma limiting adduction',
                             'Right cricoarytenoid rheumatoid arthritis flare',
                             'Right arytenoid dislocation from intubation trauma'],
                 'answer': 3,
                 'explanation': 'A traumatic, multi-attempt intubation followed immediately by '
                                'breathy voice, an edematous anteriorly displaced arytenoid, and a '
                                'height mismatch suggests arytenoid dislocation. The deciding clue '
                                'is normal EMG recruitment in the thyroarytenoid: the nerve is '
                                'intact, so the immobility is mechanical. Cuff-pressure '
                                'neurapraxia would show reduced or absent recruitment. Early '
                                'recognition matters because closed reduction under anesthesia '
                                'works best soon after injury, before joint fibrosis.',
                 'why_wrong': ['Cuff injury compresses the recurrent nerve and would reduce '
                               'recruitment, which conflicts with the normal EMG in this patient.',
                               'A granuloma takes weeks to form at the vocal process and does not '
                               'immobilize the fold immediately after intubation.',
                               'Rheumatoid cricoarytenoid arthritis occurs in patients with '
                               'systemic disease and is not triggered by a single traumatic '
                               'intubation.',
                               'Correct.'],
                 'board_pearl': 'Immobile fold after traumatic intubation with normal EMG: think '
                                'arytenoid dislocation and reduce early.',
                 'curveball': 'How does timing affect the value of closed reduction if arytenoid '
                              'dislocation is suspected?',
                 'curveball_answer': 'Closed reduction under general anesthesia, using a '
                                     'laryngoscope or blade to reposition the arytenoid, works '
                                     'best within the first days to weeks before scar ankylosis '
                                     'develops. Success falls with delay, although reduction is '
                                     'still sometimes attempted weeks later. If the joint becomes '
                                     'fixed, treatment shifts to voice therapy and medialization '
                                     'procedures.'},
 'v128_lar_07': {'stem': 'A 47-year-old man has stridor 3 months after a 16-day intubation for '
                         'COVID-19 pneumonia and remains tracheostomy dependent. Laryngoscopy '
                         'shows both folds near the midline with minimal abduction. He is taken '
                         'for microlaryngoscopy to decide between a nerve and a scar mechanism. '
                         'Which finding under anesthesia best indicates posterior glottic stenosis '
                         'rather than bilateral recurrent laryngeal nerve paralysis?',
                 'choices': ['Free passive arytenoid motion with smooth posterior mucosa',
                             'Restricted passive arytenoid motion with interarytenoid scar',
                             'Bowed membranous folds with a spindle-shaped glottic gap',
                             'Granulation on both vocal processes with mobile joints'],
                 'answer': 1,
                 'explanation': 'Posterior glottic stenosis is mechanical, so the decisive '
                                'operative test is passive mobility. When the surgeon pushes each '
                                'arytenoid laterally with a probe or laryngoscope tip, scar or '
                                'ankylosis resists the motion, and an interarytenoid band or '
                                'posterior commissure scar is often visible. In neurogenic '
                                'paralysis the joints move freely despite no active abduction. '
                                'Passive mobility testing under anesthesia also shows whether one '
                                'or both joints are fixed, which guides choice of procedure.',
                 'why_wrong': ['Free passive movement with normal posterior mucosa is the pattern '
                               'of neurogenic paralysis, not mechanical stenosis.',
                               'Correct.',
                               'Bowing and a spindle gap reflect atrophy or paresis causing '
                               'insufficiency, not posterior fixation causing obstruction.',
                               'Vocal process granulation with mobile joints is a contact lesion '
                               'and does not explain bilateral immobility near midline.'],
                 'board_pearl': 'Passive arytenoid palpation under anesthesia distinguishes '
                                'fixation from paralysis.',
                 'curveball': 'Palpation is equivocal because of edema and a stiff scope view. '
                              'What can laryngeal EMG add?',
                 'curveball_answer': 'EMG tests whether the thyroarytenoid and posterior '
                                     'cricoarytenoid muscles have neural input. Normal recruitment '
                                     'with absent abduction points to mechanical fixation, while '
                                     'fibrillations and reduced or absent motor units indicate '
                                     'denervation. Mixed findings suggest both scar and nerve '
                                     'injury, which is common after prolonged intubation and '
                                     'affects prognosis and the choice of procedure.'},
 'v135_lary_03': {'stem': 'A 55-year-old woman has persistent stridor 6 months after a 4-week ICU '
                          'stay for ARDS with a tracheostomy placed on day 18. Laryngoscopy shows '
                          'both folds near the midline. Laryngeal EMG shows normal recruitment '
                          'bilaterally. At microlaryngoscopy, palpation shows both arytenoids '
                          'barely move, and a thick scar fills the posterior commissure. What is '
                          'the most likely diagnosis?',
                  'choices': ['Posterior glottic stenosis with bilateral joint fixation',
                              'Bilateral recurrent laryngeal nerve paralysis with synkinesis',
                              'Supraglottic stenosis from tracheostomy cuff injury',
                              'Cricoarytenoid ankylosis from relapsing polychondritis'],
                  'answer': 0,
                  'explanation': 'After weeks of intubation, pressure necrosis of the posterior '
                                 'glottis heals as dense interarytenoid and posterior commissure '
                                 'scar that can fuse both cricoarytenoid joints. Normal EMG '
                                 'recruitment rules out denervation, and both arytenoids barely '
                                 'move on palpation, which proves mechanical fixation. Together '
                                 'this is posterior glottic stenosis with bilateral joint '
                                 'fixation, Bogdasarian type IV. Treatment targets scar and joint '
                                 'mechanics rather than waiting for nerve recovery.',
                  'why_wrong': ['Correct.',
                                'Synkinesis follows nerve injury and shows abnormal EMG patterns; '
                                'it does not cause dense posterior scar or fixed joints on '
                                'palpation.',
                                'Tracheostomy cuff injury causes stenosis at or below the stoma, '
                                'not supraglottic scar fixing the arytenoids.',
                                'Relapsing polychondritis causes recurrent auricular and nasal '
                                'chondritis; nothing here suggests systemic disease rather than '
                                'intubation injury.'],
                  'board_pearl': 'Normal EMG plus fixed arytenoids after prolonged intubation '
                                 'equals posterior glottic stenosis.',
                  'curveball': 'What operative options can improve her airway, and what voice and '
                               'swallowing trade-offs should be discussed?',
                  'curveball_answer': 'Options include endoscopic scar division with mucosal '
                                      'flaps, posterior cricoid split with rib cartilage grafting '
                                      'by endoscopic or open approach, and posterior cordotomy or '
                                      'arytenoidectomy. Grafting can widen the airway while '
                                      'preserving more voice but may require a stent or '
                                      'tracheostomy for a period. Destructive widening produces a '
                                      'breathier voice and greater aspiration risk than expansion '
                                      'procedures.'},
 'v251_lar_pgs_fnd': {'stem': 'A 44-year-old man has progressive exertional dyspnea 3 months after '
                              'a 10-day intubation with an 8.0 tube following a motorcycle crash. '
                              'His voice is close to normal. A junior resident calls the bilateral '
                              'immobility seen on laryngoscopy recurrent nerve paralysis, although '
                              'the patient had no neck or chest surgery. Why should posterior '
                              'glottic stenosis be considered first?',
                      'choices': ['Intubation commonly stretches both recurrent nerves',
                                  'Posterior scar typically causes a weak breathy voice',
                                  'Tube pressure on the posterior glottis can scar the joints',
                                  'Office laryngoscopy reliably shows joint fixation'],
                      'answer': 2,
                      'explanation': 'The endotracheal tube rests in the posterior glottis between '
                                     'the arytenoids. Pressure above capillary perfusion causes '
                                     'ischemic ulceration of the interarytenoid mucosa and '
                                     'cricoarytenoid joints, and healing produces scar that '
                                     'tethers or ankyloses the joints. Both folds then fail to '
                                     'abduct, mimicking bilateral paralysis. Without neck or chest '
                                     'surgery, there is no ready explanation for bilateral nerve '
                                     'injury, while prolonged intubation with a large tube is a '
                                     'strong risk factor for posterior stenosis.',
                      'why_wrong': ['Intubation can injure a recurrent nerve through cuff '
                                    'pressure, but bilateral nerve injury is far less common than '
                                    'posterior scar.',
                                    'Posterior stenosis limits abduction while adduction is '
                                    'preserved, so the voice is usually good, as in this patient.',
                                    'Correct.',
                                    'Flexible examination often cannot separate fixation from '
                                    'paralysis; operative palpation or EMG is usually needed.'],
                      'board_pearl': 'The tube sits posteriorly; posterior glottic stenosis is a '
                                     'mimic of bilateral paralysis after intubation.',
                      'curveball': 'The resident asks which posterior laryngeal pressure points '
                                   'are most vulnerable during his kind of prolonged intubation. '
                                   'What do you tell him?',
                      'curveball_answer': 'The tube presses hardest on the medial surfaces of the '
                                          'arytenoids and vocal processes, the interarytenoid '
                                          'mucosa over the posterior commissure, and the posterior '
                                          'cricoid plate in the subglottis. Ulceration at these '
                                          'sites causes interarytenoid scar, joint ankylosis, and '
                                          'posterior subglottic stenosis. Large tubes, long '
                                          'duration, movement, and hypotension increase the risk.'},
 'v251_lar_pgs_app': {'stem': 'A 62-year-old woman has been tracheostomy dependent for 5 months '
                              'after a prolonged ICU stay for sepsis with 21 days of intubation. '
                              'Flexible laryngoscopy shows both folds near midline with subtle '
                              'posterior commissure thickening. She had no thyroid, neck, or chest '
                              'surgery. The team debates bilateral paralysis versus fixation '
                              'before planning decannulation. Which evaluation most directly '
                              'resolves the mechanism?',
                      'choices': ['Contrast CT of the vagus nerve course to the aortic arch',
                                  'Microlaryngoscopy with arytenoid palpation and scar assessment',
                                  'Repeat flexible laryngoscopy after a month of voice therapy',
                                  'Pulmonary function testing with a flow-volume loop study'],
                      'answer': 1,
                      'explanation': 'Mechanism determines treatment. Under anesthesia, direct '
                                     'palpation tests passive cricoarytenoid mobility, while '
                                     'magnified inspection shows interarytenoid or posterior '
                                     'commissure scar and coexisting subglottic or stomal stenosis '
                                     'common after prolonged intubation. Freely mobile joints with '
                                     'no scar point to neurogenic paralysis, whereas resistance or '
                                     'scar indicates posterior glottic stenosis. Laryngeal EMG '
                                     'adds useful information when a neurogenic component remains '
                                     'possible, as in critical illness polyneuropathy. Office '
                                     'examination alone often cannot make this distinction.',
                      'why_wrong': ['Imaging the nerve course is for unexplained paralysis; her '
                                    'history points to intubation injury that needs mechanical '
                                    'assessment.',
                                    'Correct.',
                                    'Therapy does not change a fixed scar, and repeating flexible '
                                    'examination cannot test passive joint mobility.',
                                    'Flow-volume loops can show fixed obstruction but cannot tell '
                                    'joint fixation from paralysis or define the scar.'],
                      'board_pearl': 'Before glottic airway surgery for bilateral immobility, '
                                     'palpate the arytenoids under anesthesia.',
                      'curveball': 'How would dense interarytenoid scar with mobile joints differ '
                                   'from ankylosed joints in operative planning?',
                      'curveball_answer': 'A scar band or posterior commissure scar with mobile '
                                          'joints, Bogdasarian types I and II, can often be '
                                          'divided endoscopically with mucosal flaps, allowing '
                                          'abduction to recover. Ankylosed joints, types III and '
                                          'IV, do not move after scar division, so patients '
                                          'usually need posterior cricoid expansion grafting or a '
                                          'static widening procedure such as cordotomy or '
                                          'arytenoidectomy.'},
 'v251_lar_pgs_snr': {'stem': 'A 41-year-old female choir director has been tracheostomy dependent '
                              'for 2 years with mature posterior glottic stenosis after intubation '
                              'for meningitis. Microlaryngoscopy shows a dense posterior '
                              'commissure scar; the left arytenoid moves passively, and the right '
                              'is fixed. EMG is normal. She wants decannulation and ranks her '
                              'singing voice highly. What is the best operative strategy?',
                      'choices': ['Bilateral total arytenoidectomy in a single stage',
                                  'Left posterior cordotomy with tracheostomy retained',
                                  'Serial balloon dilation of the posterior glottis',
                                  'Scar release with posterior cricoid expansion grafting'],
                      'answer': 3,
                      'explanation': 'Her stenosis is heterogeneous: mature posterior scar with '
                                     'one fixed and one mobile joint, Bogdasarian type III, and '
                                     'intact nerves. Releasing the scar and expanding the '
                                     'posterior glottis with a cartilage graft widens the airway '
                                     'while preserving the vibrating membranous folds and the '
                                     'residual mobility of the left joint, which best protects her '
                                     'singing voice. Destructive procedures such as cordotomy or '
                                     'arytenoidectomy enlarge the airway but trade away voice '
                                     'quality and some airway protection.',
                      'why_wrong': ['Bilateral arytenoidectomy removes the structures she needs '
                                    'for voice and protection and is excessive for a partly mobile '
                                    'glottis.',
                                    'Cordotomy on the mobile left side sacrifices the best '
                                    'remaining function and leaves the true problem, posterior '
                                    'scar, unaddressed.',
                                    'Simple dilation of mature posterior scar gives only brief '
                                    'benefit and does not create durable abduction or '
                                    'decannulation.',
                                    'Correct.'],
                      'board_pearl': 'Match the operation to the scar and joint pattern; expansion '
                                     'preserves voice better than destruction.',
                      'curveball': 'When would a reconstructive scar-release approach be '
                                   'preferable to destructive posterior widening?',
                      'curveball_answer': 'Reconstruction is preferred when at least one joint '
                                          'retains mobility, the nerves are intact, the patient '
                                          'values voice, and she can tolerate a staged course with '
                                          'a temporary stent or tracheostomy. Destructive widening '
                                          'is better for bilateral ankylosis with poor '
                                          'reconstructive potential, frail patients who need a '
                                          'single reliable procedure, or after failed expansion.'},
 'v11_lar_06': {'stem': 'A 32-year-old female worship leader has 8 months of hoarseness and loss '
                        'of her upper range despite 3 months of voice therapy. Stroboscopy shows a '
                        'unilateral rounded swelling on the right mid-membranous fold with a '
                        'focally reduced mucosal wave over it, a small fibrous bump on the '
                        'opposite fold at the contact point, and an hourglass closure. Which '
                        'diagnosis is more likely than bilateral nodules?',
                'choices': ['Bilateral fibrotic nodules with asymmetric bulk',
                            'Bilateral sulcus vergeture with a spindle gap',
                            'Unilateral cyst with a contralateral reactive lesion',
                            'Early bilateral Reinke edema of the free edge'],
                'answer': 2,
                'explanation': 'Nodules are bilateral, symmetric, and superficial, with largely '
                               'preserved mucosal wave, and they often shrink with therapy. Here a '
                               'unilateral rounded lesion with a focal reduction in wave suggests '
                               'a subepithelial cyst within the superficial lamina propria, and '
                               'the smaller fibrous bump opposite it is a reactive contact lesion. '
                               'Persistence after therapy also fits. Distinguishing the two '
                               'matters because a cyst usually needs microflap excision, whereas '
                               'the reactive lesion often resolves once the cyst is removed.',
                'why_wrong': ['Nodules are symmetric with preserved wave; marked asymmetry and '
                              'focal wave reduction point to a different lesion.',
                              'Sulcus produces a linear furrow and stiffness along the fold rather '
                              'than a rounded mass at one point.',
                              'Correct.',
                              'Reinke edema is diffuse polypoid swelling along the whole fold in '
                              'smokers, not a focal rounded lesion.'],
                'board_pearl': 'Asymmetric lesion with focal wave loss plus a contralateral bump '
                               'suggests a cyst with a reactive lesion.',
                'curveball': 'The lesion is a cyst with a markedly reduced wave. Why does that '
                             'change surgical technique and counseling compared with a soft polyp?',
                'curveball_answer': 'A cyst lies within the superficial lamina propria, so it must '
                                    'be dissected out through a microflap with the wall intact, '
                                    'preserving overlying epithelium and surrounding lamina '
                                    'propria. A polyp is usually superficial and can be trimmed '
                                    'flush. Counsel that cyst removal carries higher risk of '
                                    'residual stiffness and recurrence if wall remains, and that '
                                    'recovery takes longer.'},
 'v141_lar_05': {'stem': 'A 28-year-old female mezzo-soprano has 10 months of hoarseness, loss of '
                         'pianissimo singing, and vocal fatigue. Stroboscopy shows a smooth, '
                         'white-yellow rounded mass beneath intact epithelium in the left '
                         'mid-membranous fold with a focally absent mucosal wave and incomplete '
                         'closure. She completed 4 months of voice therapy with good technique but '
                         'no change. What is the most reasonable next step?',
                 'choices': ['Microflap excision preserving the overlying epithelium',
                             'Flush excision of the lesion with the overlying mucosa',
                             'Steroid injection into the lesion and repeat therapy',
                             'Continued voice rest and therapy for a further 6 months'],
                 'answer': 0,
                 'explanation': 'A white subepithelial mass with focal absence of wave that '
                                'persists despite adequate therapy is a mucous retention or '
                                'epidermoid cyst. True cysts rarely regress, because the problem '
                                'is a structural lesion rather than technique. Phonomicrosurgery '
                                'through a microflap, made with an incision lateral to the lesion, '
                                'allows dissection of the intact cyst wall while preserving '
                                'overlying epithelium and the surrounding superficial lamina '
                                'propria. That approach limits postoperative scar, which matters '
                                'most in a singer.',
                 'why_wrong': ['Correct.',
                               'Removing the overlying mucosa sacrifices normal epithelium and '
                               'lamina propria and raises the risk of scar and stiffness.',
                               'Steroid injection can shrink inflammatory lesions such as nodules '
                               'but rarely eliminates a true cyst with an epithelial wall.',
                               'Further rest and therapy are unlikely to help a cyst that has '
                               'already failed adequate therapy with good technique.'],
                 'board_pearl': 'True cysts persist after therapy; remove them through a microflap '
                                'with the cover preserved.',
                 'curveball': 'She plans to return to performing within a week of surgery. Why is '
                              'structured postoperative voice rehabilitation important after her '
                              'cyst excision?',
                 'curveball_answer': 'Brief voice rest lets the epithelium seal, then guided '
                                     'therapy rebuilds efficient technique so she does not return '
                                     'to the patterns that injured the fold or compensate with '
                                     'excess tension. Graded return to singing protects healing '
                                     'lamina propria while it remodels, and therapy helps her '
                                     'regain flexibility and range. Patients who skip '
                                     'rehabilitation have more fatigue and more lesion '
                                     'recurrence.'},
 'v254_lar_benign_fnd': {'stem': 'A 36-year-old male high school teacher has 5 months of '
                                 'hoarseness and voice fatigue by the end of the day. He does not '
                                 'smoke. Flexible laryngoscopy under continuous light shows a '
                                 'small whitish bump on the left mid-membranous fold, but whether '
                                 'it is a superficial lesion or a deeper stiff one is unclear. '
                                 "Which test best characterizes the lesion's effect on vibration?",
                         'choices': ['High-resolution neck CT',
                                     'Laryngeal electromyography',
                                     'Office biopsy under topical anesthesia',
                                     'Videostroboscopy'],
                         'answer': 3,
                         'explanation': 'Fold vibration is too fast to see under continuous light. '
                                        'Videostroboscopy uses flashes timed to the fundamental '
                                        'frequency to create an apparent slow-motion picture of '
                                        'the mucosal wave, showing amplitude, symmetry, '
                                        'periodicity, closure pattern, and how the lesion affects '
                                        'vibration. A superficial nodule or polyp leaves the wave '
                                        'mostly intact, whereas a cyst, scar, sulcus, or '
                                        'epithelial dysplasia produces focal stiffness. The '
                                        'findings guide the choice among therapy, surgery, and '
                                        'biopsy.',
                         'why_wrong': ['CT shows cartilage and deep spaces but cannot assess the '
                                       'mucosal wave or distinguish small benign mucosal lesions.',
                                       'EMG evaluates nerve and muscle function and does not '
                                       'characterize a mucosal lesion or its effect on vibration.',
                                       'Biopsy is premature for a likely benign lesion without '
                                       'risk factors, and it can scar the vibratory cover.',
                                       'Correct.'],
                         'board_pearl': 'Stroboscopy shows mucosal wave; focal wave loss suggests '
                                        'cyst, scar, or deeper epithelial disease.',
                         'curveball': 'Stroboscopy shows a focal absent wave over the lesion. How '
                                      'does that change your concern for cyst, scar, or dysplasia?',
                         'curveball_answer': 'An absent or markedly reduced wave means the lesion '
                                             'has invaded or stiffened the superficial lamina '
                                             'propria rather than sitting on top of it. In a '
                                             'nonsmoker that favors a cyst or scar; in a smoker, '
                                             'or with leukoplakia or an irregular surface, it '
                                             'raises concern for dysplasia or early carcinoma and '
                                             'lowers the threshold for excisional biopsy.'},
 'v254_lar_benign_app': {'stem': 'A 25-year-old female preschool teacher and weekend bar singer '
                                 'has 4 months of hoarseness. Stroboscopy shows a small soft '
                                 'swelling on the right mid-membranous free edge with preserved '
                                 'wave, mild contralateral thickening, and supraglottic squeeze. '
                                 'She shouts over children daily, drinks little water, and has no '
                                 'airway symptoms, smoking history, or leukoplakia. What is the '
                                 'best initial management?',
                         'choices': ['Microlaryngoscopic excision followed by voice therapy',
                                     'Voice therapy with hygiene and load reduction, then reassess',
                                     'Two weeks of strict silence followed by a voice recheck',
                                     'Oral corticosteroid taper with reflux treatment'],
                         'answer': 1,
                         'explanation': 'Small benign phonotraumatic lesions often shrink when '
                                        'collision forces fall. Voice therapy addresses '
                                        'inefficient technique and supraglottic squeeze, while '
                                        'hygiene and reduced load target the shouting and '
                                        'dehydration that drive injury. Preserved mucosal wave, a '
                                        'soft lesion, and no red flags make conservative treatment '
                                        'reasonable first. Reassessment with stroboscopy after '
                                        'several weeks of therapy shows whether a residual '
                                        'structural lesion, rather than behavior, is still '
                                        'limiting voice and whether phonomicrosurgery is needed.',
                         'why_wrong': ['Surgery before therapy risks recurrence because the '
                                       'behaviors that caused the lesion remain unchanged.',
                                       'Correct.',
                                       'Brief silence may calm acute swelling, but without therapy '
                                       'her shouting and technique will reinjure the fold.',
                                       'Steroids and reflux medication do not address phonotrauma '
                                       'and are not indicated without specific inflammatory '
                                       'findings.'],
                         'board_pearl': 'Benign phonotraumatic lesions: voice therapy first; '
                                        'surgery for persistent structural disease.',
                         'curveball': 'Which findings would make you bypass prolonged conservative '
                                      'management and obtain tissue diagnosis?',
                         'curveball_answer': 'Leukoplakia, erythroplakia, an irregular or '
                                             'ulcerated surface, a lesion off the striking zone, a '
                                             'stiff segment without phonotrauma, progressive '
                                             'growth, tobacco or heavy alcohol exposure, '
                                             'hemoptysis, airway symptoms, or neck nodes all '
                                             'suggest dysplasia or cancer. These findings call for '
                                             'microlaryngoscopy with excisional biopsy rather than '
                                             'months of therapy.'},
 'v254_lar_benign_snr': {'stem': 'A 30-year-old female touring singer completed 4 months of '
                                 'skilled voice therapy but still has hoarseness, loss of high '
                                 'notes, and fatigue. Stroboscopy shows a persistent sessile '
                                 'translucent polyp on the left mid-membranous free edge with '
                                 'surrounding normal mucosa. She is scheduled for '
                                 'microlaryngoscopy. Which operative principle best protects her '
                                 'long-term voice?',
                         'choices': ['Minimal cold excision sparing normal epithelium',
                                     'Excision with a 1-mm margin of surrounding mucosa',
                                     'CO2 laser vaporization of the polyp base',
                                     'Subepithelial steroid injection into the lesion'],
                         'answer': 0,
                         'explanation': 'Voice quality depends on the layered fold: pliable '
                                        'epithelium over a gel-like superficial lamina propria, '
                                        'which slides over the vocal ligament. Phonomicrosurgery '
                                        'removes only the lesion, using a microflap or flush '
                                        'trimming with cold instruments, and spares normal '
                                        'epithelium, the superficial lamina propria, and the '
                                        'ligament. Excess mucosal removal, deep thermal injury, or '
                                        'ligament trauma replaces a treatable polyp with permanent '
                                        'stiffness, which is far harder to fix than the original '
                                        'lesion.',
                         'why_wrong': ['Correct.',
                                       'Benign polyps need no margin, and removing surrounding '
                                       'mucosa exposes lamina propria and promotes scar and '
                                       'stiffness.',
                                       'Laser vaporization can be used with care, but deep thermal '
                                       'spread at the base risks injuring the lamina propria and '
                                       'ligament.',
                                       'Steroid injection helps some inflammatory lesions, but a '
                                       'persistent sessile polyp after therapy usually needs '
                                       'excision.'],
                         'board_pearl': 'Phonomicrosurgery removes the lesion only and protects '
                                        'the epithelium, superficial lamina propria, and ligament.',
                         'curveball': 'How should you counsel her when complete removal and '
                                      'maximal mucosal preservation are in tension?',
                         'curveball_answer': 'Explain that the goal is the best voice, not a '
                                             'perfectly flat fold. A small residual or later '
                                             'recurrence can be treated, whereas scar from '
                                             'aggressive removal is hard to reverse. Agree before '
                                             'surgery that you will favor preservation when the '
                                             'lesion blends into the lamina propria, and plan '
                                             'therapy and follow-up stroboscopy afterward.'},
 'v113-lar-02': {'stem': 'A 4-year-old boy has 6 months of progressive hoarseness and, over the '
                         'past month, noisy breathing during play. He was born vaginally to a '
                         'mother who had genital warts during pregnancy. He is afebrile and '
                         'growing normally. Flexible laryngoscopy shows multiple exophytic, '
                         'grapelike lesions with punctate vascular cores on both true vocal folds '
                         'and the anterior commissure. Which diagnosis is most likely?',
                 'choices': ['Bilateral phonotraumatic vocal nodules',
                             'Subglottic hemangioma of infancy',
                             'Recurrent respiratory papillomatosis',
                             'Laryngeal tuberculosis with granulation'],
                 'answer': 2,
                 'explanation': 'Multifocal exophytic, grapelike lesions with punctate vascular '
                                'cores are the appearance of recurrent respiratory papillomatosis, '
                                'a benign epithelial neoplasm caused mainly by HPV 6 and 11. '
                                'Juvenile disease is linked to vertical transmission, classically '
                                'from a mother with genital warts at vaginal delivery. The true '
                                'folds and anterior commissure are common sites. Progressive '
                                'hoarseness that advances to stridor in a young child should '
                                'prompt urgent endoscopy because papillomas can obstruct the '
                                'airway.',
                 'why_wrong': ['Nodules are smooth, symmetric, and confined to the mid-membranous '
                               'striking zone and do not cause stridor.',
                               'Infantile hemangioma is a smooth subglottic mass in the first '
                               'months of life, not exophytic lesions in a 4-year-old.',
                               'Correct.',
                               'Laryngeal tuberculosis is rare in a well child without fever, '
                               'cough, or exposure, and it usually ulcerates rather than forming '
                               'papillary clusters.'],
                 'board_pearl': 'Grapelike lesions with vascular cores in a hoarse child: RRP from '
                                'HPV 6 and 11.',
                 'curveball': 'Why is repeated conservative debulking preferred over aggressive '
                              'deep resection in this child?',
                 'curveball_answer': 'HPV persists in normal-looking surrounding mucosa, so even '
                                     'complete removal does not cure RRP and recurrence is '
                                     'expected. Aggressive or deep resection, especially at the '
                                     'anterior commissure, causes webs, scar, and stenosis that '
                                     'worsen voice and airway more than the disease itself. The '
                                     'goal is a safe airway and usable voice with the least '
                                     'injury, using microdebrider or careful laser debulking.'},
 'v113-lar-03': {'stem': 'A 70-year-old man has a year of solid-food dysphagia and a sensation of '
                         'food lodging at the level of the cricoid. He has no weight loss or '
                         'neurologic symptoms. Videofluoroscopy shows strong tongue-base '
                         'retraction and pharyngeal stripping wave but a narrow, delayed opening '
                         'of the pharyngoesophageal segment with residue above it. There is no '
                         'pouch. Which mechanism is most likely?',
                 'choices': ['Global pharyngeal constrictor weakness',
                             'Cricopharyngeal muscle dysfunction',
                             'Delayed initiation of the pharyngeal swallow',
                             'Distal esophageal outflow obstruction'],
                 'answer': 1,
                 'explanation': 'Upper esophageal sphincter opening requires cricopharyngeal '
                                'relaxation, hyolaryngeal traction, and adequate bolus pressure. '
                                'Here pharyngeal drive is strong yet the pharyngoesophageal '
                                'segment opens narrowly and late, leaving residue just above it, '
                                'so the limiting site is a noncompliant or poorly relaxing '
                                'cricopharyngeus. This is the physiology of cricopharyngeal '
                                'dysfunction, often with a bar on imaging. Strong propulsion '
                                'predicts a good response to sphincter-directed treatment.',
                 'why_wrong': ['Global weakness causes diffuse vallecular and pyriform residue '
                               'with a poor stripping wave, which is strong in this patient.',
                               'Correct.',
                               'Delayed initiation causes premature spill and aspiration before '
                               'the swallow, not residue above a narrow sphincter.',
                               'Distal obstruction causes retrosternal sticking, while this '
                               "patient's residue sits at the pharyngoesophageal segment."],
                 'board_pearl': 'Strong pharyngeal drive with poor UES opening suggests a '
                                'cricopharyngeal problem amenable to sphincter treatment.',
                 'curveball': 'Before referring him for myotomy, which tests help separate '
                              'impaired sphincter relaxation from weak pharyngeal propulsion?',
                 'curveball_answer': 'High-resolution pharyngeal manometry measures UES relaxation '
                                     'pressure, residual pressure, and intrabolus pressure, and '
                                     'quantifies pharyngeal contractile strength. Videofluoroscopy '
                                     'shows hyolaryngeal excursion, stripping wave, and the extent '
                                     'of opening. High intrabolus pressure with strong contraction '
                                     'suggests a stiff sphincter, whereas weak contraction '
                                     'predicts less benefit from myotomy.'},
 'v141_lar_06': {'stem': 'A 76-year-old woman has 2 years of progressive solid-food dysphagia with '
                         'residue felt low in the throat. Videofluoroscopy shows a prominent '
                         'posterior cricopharyngeal bar at C5-C6 with residue above it, normal '
                         'hyolaryngeal elevation, and a strong pharyngeal stripping wave. '
                         'Manometry confirms elevated UES residual pressure. Endoscopy shows no '
                         'mass. Which treatment options are appropriate?',
                 'choices': ['Proton pump inhibitor with a dysphagia diet alone',
                             'Thyroplasty to improve airway protection during swallow',
                             'Percutaneous gastrostomy with no oral intake',
                             'Dilation, botulinum toxin, or cricopharyngeal myotomy'],
                 'answer': 3,
                 'explanation': 'With an obstructing bar, elevated residual pressure, and good '
                                'pharyngeal drive, the cricopharyngeus is the limiting physiology. '
                                'Dilation is quick but often temporary. Botulinum toxin weakens '
                                'the muscle for months and serves as a diagnostic trial, though it '
                                'can briefly worsen dysphagia if it diffuses. Cricopharyngeal '
                                'myotomy, endoscopic or open, gives the most durable result. The '
                                'choice depends on durability needed, fibrosis, comorbidity, and '
                                'patient preference, after excluding a mass or Zenker pouch.',
                 'why_wrong': ['Acid suppression and diet changes do not relieve a mechanically '
                               'noncompliant sphincter shown on manometry.',
                               'Thyroplasty treats glottic insufficiency, which is not her '
                               'problem; her limitation is sphincter opening.',
                               'Gastrostomy is excessive when her pharynx is strong and the '
                               'obstruction is treatable.',
                               'Correct.'],
                 'board_pearl': 'Treat cricopharyngeal dysfunction with dilation, toxin, or '
                                'myotomy once mechanism is confirmed.',
                 'curveball': 'Her sister has a similar bar but also a weak stripping wave. When '
                              'does poor pharyngeal propulsion predict limited benefit from '
                              'myotomy?',
                 'curveball_answer': 'If the pharynx cannot generate pressure, as in advanced '
                                     'neuromuscular disease, post-radiation fibrosis, or stroke '
                                     'with weak constrictors, a looser sphincter still leaves '
                                     'diffuse residue because no force moves the bolus. Manometry '
                                     'with weak pharyngeal contraction or fluoroscopy with poor '
                                     'stripping and diffuse residue predicts limited gain. Myotomy '
                                     'also removes a barrier against reflux.'},
 'v253_lar_cp_fnd': {'stem': 'A 67-year-old man is referred for cricopharyngeal myotomy after '
                             'videofluoroscopy described impaired upper esophageal sphincter '
                             'opening. Review of the study shows reduced anterior-superior hyoid '
                             'excursion, vallecular residue, and a faint cricopharyngeal '
                             'indentation. He had a brainstem stroke 6 months ago. Which statement '
                             'is most important before labeling this isolated cricopharyngeal '
                             'dysfunction?',
                     'choices': ['A visible cricopharyngeal bar proves a myotomy will help',
                                 'UES opening is controlled by the cricopharyngeus alone',
                                 'Opening also depends on hyolaryngeal traction and bolus drive',
                                 'Manometry is unnecessary if fluoroscopy shows a bar'],
                     'answer': 2,
                     'explanation': 'The UES does not open by relaxation alone. The '
                                    'cricopharyngeus must relax, the suprahyoid muscles must pull '
                                    'the hyolaryngeal complex anteriorly and upward to distract '
                                    'the sphincter open, and the tongue base and constrictors must '
                                    'drive the bolus through. After a brainstem stroke, reduced '
                                    'hyoid excursion and vallecular residue mean the opening '
                                    'deficit may be secondary to weak traction and propulsion. '
                                    'Localizing the physiology avoids a myotomy that leaves the '
                                    'true deficit untreated.',
                     'why_wrong': ['Many asymptomatic older adults have bars, and a bar does not '
                                   'show that the sphincter is the limiting problem.',
                                   'Opening is a coordinated event that needs hyolaryngeal '
                                   'traction and bolus pressure in addition to relaxation.',
                                   'Correct.',
                                   'Manometry or careful fluoroscopic analysis is useful because a '
                                   'bar alone does not localize the physiologic deficit.'],
                     'board_pearl': 'UES opening needs relaxation, hyolaryngeal traction, and '
                                    'bolus pressure; poor opening is not always the '
                                    'cricopharyngeus.',
                     'curveball': 'The referring physician still favors surgery. How can '
                                  'generalized pharyngeal weakness after his stroke make a myotomy '
                                  'less effective?',
                     'curveball_answer': 'With weak constrictors and tongue-base retraction, '
                                         'little pressure pushes the bolus, so a lower-resistance '
                                         'sphincter does not empty the pharynx. Residue stays in '
                                         'the valleculae and piriform sinuses and may still be '
                                         'aspirated after the swallow. Myotomy also removes some '
                                         'protection against regurgitation, so benefit may be '
                                         'small and aspiration can worsen.'},
 'v253_lar_cp_app': {'stem': 'A 72-year-old woman with solid-food dysphagia has a focal '
                             'cricopharyngeal bar on videofluoroscopy with strong pharyngeal '
                             'stripping, normal hyolaryngeal excursion, and a normal esophagus. '
                             'After an office balloon dilation to 18 mm, she eats meat comfortably '
                             'for 4 months before symptoms return. She asks what this means for '
                             'future treatment. What does her response suggest?',
                     'choices': ['The UES is a key limiting site, supporting more durable '
                                 'treatment',
                                 'Recurrence shows the bar is unrelated to her swallowing problem',
                                 'Her symptoms most likely reflect early esophageal achalasia '
                                 'instead',
                                 'Further sphincter treatment is unlikely to help after this '
                                 'response'],
                     'answer': 0,
                     'explanation': 'When propulsion and hyolaryngeal traction are favorable, '
                                    'symptom relief after a reversible UES-directed intervention '
                                    'supports the hypothesis that sphincter resistance drives her '
                                    'dysphagia. Return of symptoms after months is expected, '
                                    'because dilation stretches but does not divide the muscle. '
                                    'Her response justifies repeat dilation, botulinum toxin, or a '
                                    'durable cricopharyngeal myotomy, with the choice guided by '
                                    'how long relief lasts, her comorbidities, and her goals.',
                     'why_wrong': ['Correct.',
                                   'Relief after treating the bar suggests it is relevant; '
                                   'recurrence reflects the temporary nature of dilation, not '
                                   'irrelevance.',
                                   'Achalasia involves the lower sphincter with retrosternal '
                                   'symptoms, and her esophagus was normal on study.',
                                   'A good temporary response predicts benefit from durable '
                                   'sphincter treatment rather than excluding it.'],
                     'board_pearl': 'Temporary relief after UES dilation supports the sphincter as '
                                    'the cause and predicts myotomy benefit.',
                     'curveball': 'What features would make you hesitate before a durable myotomy '
                                  'despite her temporary benefit?',
                     'curveball_answer': 'Hesitate with severe gastroesophageal reflux or a large '
                                         'hiatal hernia, because myotomy removes the barrier '
                                         'against regurgitation and aspiration of refluxate. Also '
                                         'hesitate with progressive neuromuscular disease, weak '
                                         'pharyngeal contraction, poor cough or airway protection, '
                                         'or prior radiation that impairs healing. Repeat dilation '
                                         'or toxin may be safer in these patients.'},
 'v253_lar_cp_snr': {'stem': 'A 74-year-old man with advanced progressive supranuclear palsy has '
                             'recurrent aspiration pneumonia. Videofluoroscopy shows a weak '
                             'stripping wave, diffuse vallecular and piriform residue, aspiration '
                             'of residue after the swallow with no cough, and only modest '
                             'narrowing at the UES. The inpatient team asks for cricopharyngeal '
                             'myotomy to fix the swallow. What is the best decision?',
                     'choices': ['Perform endoscopic myotomy because his UES is narrowed',
                                 'Inject botulinum toxin to release the sphincter now',
                                 'Offer medialization to improve laryngeal closure',
                                 'Advise that myotomy is unlikely to make his swallow safe'],
                     'answer': 3,
                     'explanation': 'Myotomy helps when sphincter resistance is the dominant '
                                    'limitation and upstream propulsion can benefit from it. In '
                                    'advanced neurodegenerative disease with a weak pharynx, '
                                    'diffuse residue, silent aspiration, and only modest UES '
                                    'narrowing, the main failures are propulsion and airway '
                                    'protection. Lowering UES resistance does not supply force or '
                                    'sensation and may add reflux aspiration. The discussion '
                                    'should instead address goals, nutrition, oral care, and '
                                    'alternative feeding plans.',
                     'why_wrong': ['Modest narrowing is not the main problem, and myotomy does not '
                                   'restore pharyngeal strength or sensation.',
                                   'Toxin carries the same limitations as myotomy here and may '
                                   'worsen dysphagia through diffusion into weak constrictors.',
                                   'Medialization treats glottic insufficiency, which is not the '
                                   'dominant problem in his diffuse sensorimotor failure.',
                                   'Correct.'],
                     'board_pearl': 'Myotomy does not fix a weak pharynx or poor airway '
                                    'protection; treat the dominant physiology.',
                     'curveball': 'When could a limited dilation or botulinum trial still be '
                                  'reasonable for palliation in a patient like him?',
                     'curveball_answer': 'A trial is reasonable when residue clearly collects '
                                         'above a tight sphincter, when the patient or family '
                                         'values comfort feeding, and when the goal is fewer '
                                         'episodes of choking or regurgitation rather than safe '
                                         'swallowing. Dilation is low risk and reversible. Define '
                                         'the target symptom beforehand and stop if there is no '
                                         'meaningful benefit.'},
 'v113-lar-04': {'stem': 'A 52-year-old man has 6 weeks of a raw, scratchy sensation on the left '
                         'side of his throat and mild hoarseness after a 5-day intubation for '
                         'urosepsis. He has never smoked. Laryngoscopy shows a smooth, pink, '
                         'rounded lesion arising from the left vocal process with normal fold '
                         'mobility and no other mucosal abnormality. Which diagnosis is most '
                         'likely?',
                 'choices': ['Mid-membranous vocal fold polyp after intubation',
                             'Intubation granuloma of the vocal process',
                             'Early squamous carcinoma of the posterior glottis',
                             'Arytenoid chondritis from prolonged tube contact'],
                 'answer': 1,
                 'explanation': 'The vocal process of the arytenoid lies at the posterior glottis, '
                                'where the endotracheal tube presses and where thin '
                                'mucoperichondrium overlies cartilage. Tube pressure ulcerates the '
                                'mucosa, and exuberant healing forms a smooth pink granuloma, '
                                'typically appearing weeks after intubation. Throat discomfort and '
                                'mild hoarseness are common, and mobility is normal. A smooth, '
                                'rounded posterior lesion in a nonsmoker soon after intubation '
                                'fits a benign granuloma, though atypical features would call for '
                                'biopsy.',
                 'why_wrong': ['Polyps arise at the mid-membranous striking zone from phonotrauma, '
                               'not on the cartilaginous vocal process after intubation.',
                               'Correct.',
                               'Carcinoma is irregular or ulcerated and is uncommon in a nonsmoker '
                               'with a smooth lesion that appeared after intubation.',
                               'Chondritis causes painful swelling and erythema over the '
                               'arytenoid, often with fever, not a smooth pedunculated mass.'],
                 'board_pearl': 'Smooth lesion on the vocal process weeks after intubation: think '
                                'intubation granuloma.',
                 'curveball': 'The granuloma recurs after two excisions and he has frequent throat '
                              'clearing. What would make you avoid a third excision?',
                 'curveball_answer': 'Recurrence after excision means the injury mechanism '
                                     'persists, so another excision is likely to fail. Treat the '
                                     'drivers instead: voice therapy to reduce hard glottal attack '
                                     'and throat clearing, and treat reflux or cough when present. '
                                     'Inject botulinum toxin into the thyroarytenoid to reduce '
                                     'vocal process contact if the lesion still recurs, and '
                                     'reserve excision for airway compromise or diagnostic doubt.'},
 'v145_lar_15': {'stem': 'A 40-year-old woman has a throat ache that radiates to the left ear, '
                         'worse with talking, 7 weeks after a 10-hour spine operation under '
                         'general anesthesia. She clears her throat often and has occasional '
                         'heartburn. Laryngoscopy shows a smooth, sessile, pale lesion on the left '
                         'vocal process with normal mobility and no ulceration. She has never '
                         'smoked. What is the best initial management?',
                 'choices': ['Voice therapy with reflux and throat-clearing control',
                             'Microlaryngoscopic excision of the lesion with biopsy',
                             'Inhaled corticosteroid and a week of complete voice rest',
                             'CO2 laser excision followed by botulinum toxin injection'],
                 'answer': 0,
                 'explanation': 'Vocal process granulomas arise when the thin mucoperichondrium '
                                'over the arytenoid ulcerates and keeps being traumatized. After '
                                'intubation, ongoing contact from throat clearing, hard glottal '
                                'attack, and reflux irritation can sustain the lesion. Initial '
                                'treatment removes these drivers with voice therapy, behavioral '
                                'control of throat clearing, and treatment of reflux when symptoms '
                                'suggest it. Many granulomas then regress over weeks to months. '
                                'Excision alone recreates the mucosal wound and often leads to '
                                'recurrence.',
                 'why_wrong': ['Correct.',
                               'Excision of a typical granuloma without addressing contact and '
                               'irritation often recurs, and biopsy is not needed without atypical '
                               'features.',
                               'A short course of voice rest does not address throat clearing and '
                               'reflux, and inhaled steroids can irritate the larynx.',
                               'Laser excision with toxin is reserved for refractory or recurrent '
                               'lesions, not a first-line approach for a typical granuloma.'],
                 'board_pearl': 'Treat the cause of vocal process granuloma first; excision alone '
                                'often recurs.',
                 'curveball': 'She returns in 2 months and the lesion looks different. What '
                              'feature would make biopsy more urgent to exclude malignancy?',
                 'curveball_answer': 'Biopsy is urgent for an ulcerated or irregular surface, '
                                     'leukoplakia, growth beyond the vocal process, impaired fold '
                                     'mobility, a lesion without an intubation or contact '
                                     'explanation, heavy tobacco or alcohol use, hemoptysis, or '
                                     'neck adenopathy. These features suggest carcinoma or a '
                                     'specific granulomatous disease rather than a benign contact '
                                     'granuloma.'},
 'v254_lar_gran_fnd': {'stem': 'A 58-year-old man has a lump-in-the-throat sensation and mild '
                               'hoarseness 5 weeks after a 2-day intubation for coronary bypass '
                               'surgery. He has never smoked. Laryngoscopy shows a smooth, red, '
                               'lobulated lesion projecting from the medial surface of the right '
                               'arytenoid at the posterior end of the true fold. Both folds move '
                               'normally. What is the most likely diagnosis?',
                       'choices': ['Contact ulcer with carcinoma',
                                   'Laryngeal papilloma',
                                   'Vocal process granuloma',
                                   'Interarytenoid pachyderma'],
                       'answer': 2,
                       'explanation': 'A smooth, red, lobulated lesion on the medial arytenoid at '
                                      'the posterior end of the fold is the vocal process, the '
                                      'classic site of contact and intubation granulomas. The tube '
                                      'rests on the thin mucoperichondrium there, causing '
                                      'ulceration that heals with granulation tissue over several '
                                      'weeks. Normal mobility and smooth contour are reassuring, '
                                      'and his recent intubation explains the lesion. Atypical '
                                      'findings such as irregularity, ulceration, or tobacco '
                                      'exposure would lower the threshold for biopsy.',
                       'why_wrong': ['Carcinoma is irregular, ulcerated, or infiltrative and '
                                     'usually occurs in smokers, which does not match this smooth '
                                     'lesion.',
                                     'Papillomas are exophytic grapelike clusters, usually at '
                                     'squamociliary junctions, not a solitary smooth lesion on the '
                                     'vocal process.',
                                     'Correct.',
                                     'Pachyderma is thickened interarytenoid mucosa from reflux or '
                                     'irritation, not a lobulated mass on one vocal process.'],
                       'board_pearl': 'Vocal process granulomas sit posteriorly on the arytenoid, '
                                      'unlike nodules and polyps in the mid-membranous fold.',
                       'curveball': 'Which atypical features should trigger biopsy rather than '
                                    'assuming a benign granuloma?',
                       'curveball_answer': 'Biopsy if the lesion is irregular, ulcerated, firm, or '
                                           'covered with leukoplakia, if it extends beyond the '
                                           'vocal process, if fold mobility is reduced, or if '
                                           'there is no intubation or contact history. Heavy '
                                           'tobacco or alcohol use, hemoptysis, weight loss, or '
                                           'neck adenopathy also raise concern for carcinoma or '
                                           'specific granulomatous disease such as tuberculosis.'},
 'v254_lar_gran_app': {'stem': 'A 45-year-old male sales manager has a vocal process granuloma 2 '
                               'months after a 4-day intubation for pneumonia. It is smooth, '
                               'pedunculated, and unchanged from 6 weeks ago. He speaks loudly at '
                               'a low pitch, has frequent hard glottal attacks, and clears his '
                               'throat many times an hour. He has no airway symptoms or suspicious '
                               'features. What management best reduces recurrence risk?',
                       'choices': ['Cold-steel excision at the stalk followed by voice rest',
                                   'Voice therapy targeting glottal attack and throat clearing',
                                   'Long-term high-dose PPI as the sole treatment',
                                   'Botulinum toxin to the arytenoid adductors as first line'],
                       'answer': 1,
                       'explanation': 'Granulomas recur when the posterior contact and irritation '
                                      'that sustain them persist. His loud, low-pitched voice, '
                                      'hard glottal attacks, and constant throat clearing '
                                      'repeatedly hammer the vocal process. Voice therapy that '
                                      'softens onset, raises pitch slightly, and replaces clearing '
                                      'with silent swallows removes the mechanical driver. Reflux '
                                      'or cough should be treated selectively when present. '
                                      'Surgery is reserved for airway obstruction, diagnostic '
                                      'uncertainty, or refractory lesions, often combined with '
                                      'continued therapy.',
                       'why_wrong': ['Excision without addressing his contact behaviors is likely '
                                     'to recur, and the lesion is not causing airway or diagnostic '
                                     'concern.',
                                     'Correct.',
                                     'Acid suppression may help when reflux contributes, but it '
                                     'does not correct the phonatory trauma that drives his '
                                     'lesion.',
                                     'Toxin is used for refractory or recurrent granulomas after '
                                     'first-line behavioral treatment fails, not before therapy is '
                                     'tried.'],
                       'board_pearl': 'Most granulomas respond to correcting contact forces and '
                                      'throat clearing; surgery is a last resort.',
                       'curveball': 'When would airway symptoms, growth pattern, or oncologic '
                                    'uncertainty justify earlier operative evaluation?',
                       'curveball_answer': 'Operate earlier for stridor or exertional dyspnea from '
                                           'a large lesion, rapid growth despite therapy, an '
                                           'atypical appearance such as ulceration, irregularity, '
                                           'or leukoplakia, a lesion outside the vocal process, or '
                                           'a patient with tobacco exposure. Excision then serves '
                                           'airway relief and tissue diagnosis, combined with '
                                           'continued voice therapy and possibly toxin.'},
 'v254_lar_gran_snr': {'stem': 'A 48-year-old female litigator has a large left vocal process '
                               'granuloma that recurred twice after technically complete excision, '
                               'despite 6 months of voice therapy, reflux treatment, and stopping '
                               'throat clearing. Pathology both times showed benign granulation '
                               'tissue. Stroboscopy shows forceful posterior glottic contact '
                               'during speech. The lesion is growing again. What is the best next '
                               'strategy?',
                       'choices': ['Third excision with a wider margin of surrounding mucosa',
                                   'External beam radiation to the posterior glottis',
                                   'Discontinue follow-up because pathology was benign',
                                   'Botulinum toxin into the left thyroarytenoid muscle'],
                       'answer': 3,
                       'explanation': 'Recurrence after adequate excision and adequate behavioral '
                                      'and reflux treatment signals that forceful vocal process '
                                      'contact persists. Botulinum toxin into the ipsilateral '
                                      'thyroarytenoid, sometimes bilateral, weakens adduction so '
                                      'the vocal processes do not strike each other with force, '
                                      'allowing the mucosa to heal. Toxin may be given alone or '
                                      'after a further excision, alongside continued therapy. '
                                      'Repeating the same operation with a wider margin enlarges '
                                      'the wound over cartilage and invites recurrence.',
                       'why_wrong': ['A wider excision enlarges the injury over the arytenoid '
                                     'perichondrium and does not change the contact force that '
                                     'caused recurrence.',
                                     'Low-dose radiation has been reported for refractory cases, '
                                     'but it carries risks and is not the next step before toxin.',
                                     'Benign pathology does not remove the need for follow-up when '
                                     'a growing lesion may still obstruct the airway.',
                                     'Correct.'],
                       'board_pearl': 'Refractory vocal process granuloma: reduce contact force '
                                      'with thyroarytenoid botulinum toxin.',
                       'curveball': 'The lesion becomes ulcerated, firm, and infiltrative despite '
                                    'prior benign pathology. How does your plan change?',
                       'curveball_answer': 'A change in character means the earlier benign '
                                           'pathology no longer reassures. Perform '
                                           'microlaryngoscopy with deep biopsy of the abnormal '
                                           'area, look for squamous carcinoma, tuberculosis, '
                                           'fungal infection, or vasculitis, and image the larynx '
                                           'if there is concern for deep invasion. Treatment then '
                                           'follows the new diagnosis rather than the granuloma '
                                           'pathway.'},
 'v113-lar-05': {'stem': 'A 64-year-old man coughs with thin liquids and has had two pneumonias '
                         'since a supraglottic laryngectomy for carcinoma 4 months ago. He eats '
                         'soft solids reasonably well. The surgical team wants to know whether '
                         'material enters the airway, at what phase, and whether a chin tuck or '
                         'supraglottic swallow helps. Which study best answers these questions?',
                 'choices': ['Bedside water swallow screening test',
                             'Chest CT for aspiration pneumonia',
                             'Videofluoroscopic swallow study',
                             'High-resolution pharyngeal manometry'],
                 'answer': 2,
                 'explanation': 'After supraglottic laryngectomy, airway protection depends on the '
                                'remaining true folds, arytenoids, and base of tongue, so '
                                'aspiration is common early on. Videofluoroscopy shows the bolus '
                                'throughout the oral, pharyngeal, and cervical esophageal phases. '
                                'It reveals whether aspiration happens before, during, or after '
                                'the swallow and lets the clinician test compensatory maneuvers '
                                'such as the chin tuck and supraglottic swallow, plus diet '
                                'changes, in real time. That is exactly the information needed to '
                                'plan rehabilitation.',
                 'why_wrong': ['Bedside screening detects some aspiration but misses silent '
                               'aspiration and cannot define timing or test maneuvers.',
                               'CT shows lung consequences of aspiration but tells nothing about '
                               'swallowing physiology or effective strategies.',
                               'Correct.',
                               'Manometry measures pharyngeal and sphincter pressures but does not '
                               'show bolus flow, aspiration, or response to maneuvers.'],
                 'board_pearl': 'VFSS shows aspiration timing across phases and lets you test '
                                'compensatory maneuvers in real time.',
                 'curveball': 'When would FEES add complementary information rather than duplicate '
                              'the fluoroscopic question?',
                 'curveball_answer': 'FEES directly shows pooled secretions, laryngeal sensation, '
                                     'and mucosal anatomy, and it can be done at the bedside, '
                                     'repeated without radiation, and used for biofeedback. It is '
                                     'especially useful for secretion management, fatigue over a '
                                     'meal, and sensory testing. Its limitation is white-out '
                                     'during the swallow, so it cannot show the moment of '
                                     'aspiration or the oral and esophageal phases.'},
 'v141_lar_01': {'stem': 'A 59-year-old man coughs during thin liquids 6 weeks after transoral '
                         'robotic resection of a base-of-tongue carcinoma. Videofluoroscopy shows '
                         'thin liquid spilling into the valleculae and entering the airway before '
                         'the swallow triggers, while nectar-thick liquid and purée remain safe. '
                         'Pharyngeal clearance after the swallow is good. Which rehabilitation '
                         'approach is most appropriate?',
                 'choices': ['Chin tuck with thickened liquids and swallow-trigger exercises',
                             'Nothing by mouth with long-term gastrostomy feeding',
                             'Effortful swallow and liquid wash for post-swallow residue',
                             'Prophylactic antibiotics during all oral liquid intake'],
                 'answer': 0,
                 'explanation': 'Aspiration before the swallow means delayed initiation: liquid '
                                'reaches the pharynx before the airway closes. Thicker liquids '
                                'slow bolus flow and give the swallow time to start, and a chin '
                                'tuck narrows the airway entrance and widens the valleculae to '
                                'hold the bolus. Sensory and timing exercises target the '
                                'underlying delay. Because thick liquids are safe and post-swallow '
                                'clearance is good, he can eat by mouth with these strategies and '
                                'repeat imaging guides liberalization.',
                 'why_wrong': ['Correct.',
                               'He swallows thickened liquids and purée safely, so stopping all '
                               'oral intake is unnecessary and harms quality of life.',
                               'Effortful swallow and liquid wash target residue after the '
                               'swallow, which is not his problem; his aspiration is premature.',
                               'Antibiotics do not prevent aspiration and are not a substitute for '
                               'treating the swallowing mechanism.'],
                 'board_pearl': 'Aspiration timing defines the fix: before the swallow suggests '
                                'delayed trigger; after suggests residue.',
                 'curveball': 'Repeat study shows his aspiration now occurs after the swallow from '
                              'vallecular residue. How does therapy change?',
                 'curveball_answer': 'Post-swallow aspiration from residue reflects weak '
                                     'tongue-base retraction or pharyngeal drive rather than a '
                                     'delayed trigger. Therapy shifts to effortful swallow, '
                                     'tongue-base strengthening such as Masako and tongue-hold '
                                     'exercises, multiple swallows, and alternating solids with '
                                     'liquids to clear residue. Thickening may increase residue '
                                     'and help less here.'},
 'v249_lar_dysphagia_fnd': {'stem': 'A 49-year-old woman has new coughing during drinks 1 week '
                                    'after anterior cervical fusion at C4-C6. Laryngoscopy shows '
                                    'normal fold mobility. Videofluoroscopy shows prevertebral '
                                    'swelling, reduced hyoid elevation, incomplete epiglottic '
                                    'inversion, and penetration of thin liquid to the folds during '
                                    'the swallow. A resident asks what protects the airway in a '
                                    'normal swallow. Which mechanism matters most?',
                            'choices': ['Glottic closure alone during the pharyngeal phase',
                                        'Cricopharyngeal contraction during swallow onset',
                                        'Soft palate elevation to seal the nasopharynx',
                                        'Sequenced laryngeal closure with hyolaryngeal elevation'],
                            'answer': 3,
                            'explanation': 'Airway protection is a coordinated sequence, not one '
                                           'flap. The true folds close first, then the false folds '
                                           'and arytenoids tilt forward, the hyolaryngeal complex '
                                           'rises and moves anteriorly beneath the tongue base, '
                                           'the epiglottis inverts, and the pharynx drives the '
                                           'bolus into an opening sphincter. Her prevertebral '
                                           'swelling limits hyolaryngeal elevation and epiglottic '
                                           'inversion, so penetration occurs despite normal fold '
                                           'mobility. Rehabilitation and time for swelling to '
                                           'resolve target that sequence.',
                            'why_wrong': ['Glottic closure is important, but this patient '
                                          'penetrates despite normal fold mobility because '
                                          'elevation and inversion fail.',
                                          'The cricopharyngeus relaxes during the swallow; '
                                          'contraction at onset would obstruct the bolus rather '
                                          'than protect the airway.',
                                          'Velopharyngeal closure prevents nasal regurgitation but '
                                          'does not protect the larynx from aspiration.',
                                          'Correct.'],
                            'board_pearl': 'Airway protection needs fold closure, hyolaryngeal '
                                           'elevation, epiglottic inversion, and timely pharyngeal '
                                           'drive.',
                            'curveball': 'How does impaired laryngeal sensation increase '
                                         'aspiration risk even when motor closure looks '
                                         'reasonable?',
                            'curveball_answer': 'Sensation through the internal branch of the '
                                                'superior laryngeal nerve triggers the swallow on '
                                                'time and fires the cough when material enters the '
                                                'vestibule. Without it, swallows start late, '
                                                'residue goes unnoticed, and aspiration is silent, '
                                                'so pneumonia can occur despite reasonable motor '
                                                'closure. Test sensation during FEES and teach '
                                                'intentional strategies such as volitional cough '
                                                'and multiple swallows.'},
 'v249_lar_dysphagia_app': {'stem': 'A 68-year-old man has coughing with liquids and a wet voice '
                                    'after a right lateral medullary infarct 5 days ago. He has '
                                    'right palatal weakness, reduced right pharyngeal contraction, '
                                    'and pools secretions. The stroke team must know whether '
                                    'material enters the airway, when that happens relative to the '
                                    'swallow, and which head positions improve safety. What is the '
                                    'best test?',
                            'choices': ['Repeat bedside 3-ounce water swallow challenge test',
                                        'Instrumental swallow study chosen for the question',
                                        'Chest radiograph to assess for early aspiration',
                                        'Flexible laryngoscopy for vocal fold mobility only'],
                            'answer': 1,
                            'explanation': 'Lateral medullary stroke damages the nucleus ambiguus '
                                           'and causes severe pharyngeal dysphagia with frequent '
                                           'silent aspiration. Bedside tests cannot reliably '
                                           'define whether, when, or how aspiration occurs. An '
                                           'instrumental study is needed: videofluoroscopy shows '
                                           'the bolus across all phases and tests head turn or '
                                           'chin tuck, while FEES shows secretion pooling, '
                                           'sensation, and residue at the bedside and can be '
                                           'repeated. The choice depends on the clinical question '
                                           'and how stable the patient is.',
                            'why_wrong': ['Water challenges detect only overt cough and miss '
                                          'silent aspiration common after lateral medullary '
                                          'stroke.',
                                          'Correct.',
                                          'A chest radiograph may show pneumonia but cannot define '
                                          'swallowing physiology or test protective strategies.',
                                          'Mobility assessment alone does not answer whether '
                                          'boluses are aspirated or which maneuvers help.'],
                            'board_pearl': 'When bedside screening cannot define aspiration, use '
                                           'VFSS or FEES chosen for the question.',
                            'curveball': 'What features would make FEES especially useful here, '
                                         'and which phase can VFSS show that FEES cannot?',
                            'curveball_answer': 'FEES suits him because it can be done at the '
                                                'bedside, shows pooled secretions and sensory '
                                                'deficits directly, can test real food, and can be '
                                                'repeated often as he recovers. VFSS shows the '
                                                'oral phase, the moment of the swallow when FEES '
                                                'whites out, upper sphincter opening, and '
                                                'esophageal clearance, which FEES cannot display.'},
 'v249_lar_dysphagia_snr': {'stem': 'An 82-year-old woman with advanced dementia and frailty has '
                                    'had four aspiration pneumonias in a year despite thickened '
                                    'liquids and speech therapy. FEES shows pooled secretions in '
                                    'the laryngeal vestibule before any food is given, aspiration '
                                    'of saliva with no cough, and absent laryngeal sensation. Her '
                                    'family asks the team to make swallowing safe. What is the '
                                    'best next step?',
                            'choices': ['Goals-of-care meeting covering risk and feeding options',
                                        'Gastrostomy placement to prevent further pneumonias',
                                        'Laryngotracheal separation to stop secretion aspiration',
                                        'Further thickening of liquids to pudding consistency'],
                            'answer': 0,
                            'explanation': 'She aspirates her own saliva before any oral intake, '
                                           'so diet changes cannot stop it, and a feeding tube '
                                           'does not prevent aspiration of secretions or '
                                           'refluxate. In advanced dementia, gastrostomy has not '
                                           'been shown to prolong life or prevent pneumonia. The '
                                           'chief-level task is a multidisciplinary goals '
                                           'discussion covering prognosis, oral care, comfort '
                                           'feeding with accepted risk, and whether any '
                                           'intervention matches her values. Aspiration-prevention '
                                           'surgery is rarely appropriate in this setting.',
                            'why_wrong': ['Correct.',
                                          'Tube feeding does not stop aspiration of saliva or '
                                          'refluxate and has not prevented pneumonia in advanced '
                                          'dementia.',
                                          'Separation can stop secretion aspiration, but in '
                                          'advanced dementia and frailty the burden usually '
                                          'outweighs benefit.',
                                          'Thicker liquids cannot help when she aspirates her own '
                                          'secretions before any food is offered.'],
                            'board_pearl': 'Feeding tubes do not prevent aspiration of secretions; '
                                           'in advanced dementia, start with a goals discussion.',
                            'curveball': 'In a different patient with the same FEES findings, when '
                                         'might laryngotracheal separation become reasonable '
                                         'despite loss of normal voice?',
                            'curveball_answer': 'It becomes reasonable when severe aspiration of '
                                                'secretions is causing recurrent, life-threatening '
                                                'pneumonia, laryngeal function is not expected to '
                                                'recover, the patient has a meaningful prognosis, '
                                                'and the goals favor survival or fewer hospital '
                                                'stays over laryngeal voice. Neurologically '
                                                'devastated but stable patients are typical '
                                                'candidates. Some separations can be reversed if '
                                                'function returns.'},
 'v128_lar_01': {'stem': 'A 22-year-old female musical theater student has a year of hoarseness '
                         'and loss of soft high notes that worsen late in the week. Stroboscopy '
                         'shows small, symmetric, whitish swellings at the junction of the '
                         'anterior and middle thirds of both folds, an hourglass closure with gaps '
                         'in front and behind, and a mucosal wave that is mildly reduced but '
                         'present. What is the most likely diagnosis?',
                 'choices': ['Bilateral vocal fold cysts',
                             'Unilateral polyp with reaction',
                             'Vocal fold nodules',
                             'Bilateral sulcus vergeture'],
                 'answer': 2,
                 'explanation': 'Nodules form at the midpoint of the membranous fold, where '
                                'collision forces are greatest. They are bilateral, symmetric, and '
                                'superficial, so the wave is only mildly reduced, and they meet in '
                                'the middle to create the hourglass closure. They develop in heavy '
                                'voice users, especially young women and children, from repeated '
                                'phonotrauma. First-line treatment is voice therapy, and most '
                                'improve without surgery.',
                 'why_wrong': ['Cysts are usually unilateral subepithelial masses with a markedly '
                               'reduced wave, not symmetric superficial swellings.',
                               'A polyp with a contralateral reaction is asymmetric, with one '
                               'dominant lesion rather than two matched swellings.',
                               'Correct.',
                               'Sulcus vergeture causes a linear furrow and spindle gap, not '
                               'discrete bumps with an hourglass closure.'],
                 'board_pearl': 'Symmetric mid-membranous lesions with an hourglass gap are '
                                'nodules; treat with voice therapy.',
                 'curveball': 'How would stroboscopic mucosal-wave behavior differ for a cyst '
                              'versus a polyp?',
                 'curveball_answer': 'A cyst lies within the superficial lamina propria, so the '
                                     'wave is markedly reduced or absent over it and often stiff '
                                     "on the opposite side's contact point. A polyp is usually "
                                     'superficial and soft, so the wave is preserved or only '
                                     'mildly reduced, and pedunculated polyps may move with '
                                     'airflow. Asymmetric wave loss favors cyst.'},
 'v128_lar_02': {'stem': 'A 44-year-old male restaurant manager has 3 months of hoarseness that '
                         'began suddenly while he shouted orders during a busy shift. He takes '
                         'aspirin for coronary disease. Stroboscopy shows a unilateral, red, '
                         'pedunculated lesion on the free edge of the left mid-membranous fold '
                         'that flops into the glottis with each cycle; the opposite fold is '
                         'normal. Which diagnosis best fits?',
                 'choices': ['Vocal fold varix with recent bleed',
                             'Hemorrhagic vocal fold polyp',
                             'Intracordal epidermoid cyst',
                             'Contact granuloma of the vocal process'],
                 'answer': 1,
                 'explanation': 'Sudden hoarseness during forceful voice use, especially on '
                                'antiplatelet therapy, suggests a vessel rupture in the '
                                'superficial lamina propria. A unilateral, red, pedunculated '
                                'lesion that moves with airflow on the mid-membranous free edge is '
                                'a hemorrhagic polyp, a common phonotraumatic lesion that is '
                                'usually unilateral. Antithrombotic drugs raise the risk of '
                                'hemorrhage. Polyps can be sessile or pedunculated; hemorrhagic '
                                'and large pedunculated lesions are less likely to resolve with '
                                'therapy alone.',
                 'why_wrong': ['A varix is a dilated vessel on the fold surface, not a '
                               'pedunculated mass that flops into the glottis.',
                               'Correct.',
                               'An epidermoid cyst is a white subepithelial mass within the fold '
                               'rather than a red pedunculated lesion on the free edge.',
                               'Contact granulomas arise on the posterior vocal process, not on '
                               'the mid-membranous free edge.'],
                 'board_pearl': 'Unilateral red pedunculated mid-fold lesion after shouting, often '
                                'on antiplatelets: hemorrhagic polyp.',
                 'curveball': 'He wants the lesion gone before his busy season. What initial '
                              'management is appropriate before considering phonomicrosurgery?',
                 'curveball_answer': 'Start with a period of relative voice rest after the bleed, '
                                     'voice therapy to correct phonotraumatic technique, '
                                     'hydration, and review of antiplatelet therapy with his '
                                     'cardiologist without stopping it unilaterally. Recheck with '
                                     'stroboscopy after several weeks. Small sessile polyps may '
                                     'shrink, but large pedunculated or organized hemorrhagic '
                                     'polyps usually need cold-instrument excision.'},
 'v128_lar_03': {'stem': 'A 38-year-old female radio host has 9 months of hoarseness and voice '
                         'fatigue that did not improve after voice therapy. Stroboscopy shows a '
                         'smooth, rounded, yellowish bulge beneath intact epithelium in the right '
                         'mid-membranous fold with a markedly reduced mucosal wave directly over '
                         'it. The left fold has a small contact swelling, and closure is '
                         'incomplete. Which diagnosis is favored?',
                 'choices': ['Sessile phonotraumatic vocal polyp',
                             'Asymmetric vocal fold nodules',
                             'Localized Reinke space edema',
                             'Subepithelial vocal fold cyst'],
                 'answer': 3,
                 'explanation': 'A rounded yellowish bulge beneath intact epithelium with a '
                                'markedly reduced wave directly over it indicates a mass embedded '
                                'within the superficial lamina propria, the typical appearance of '
                                'a mucous retention or epidermoid cyst. The small contralateral '
                                'swelling is a reactive contact lesion. Failure of voice therapy '
                                'also fits, because cysts are structural and rarely regress. '
                                'Treatment is microflap excision of the intact cyst with '
                                'preservation of the overlying cover.',
                 'why_wrong': ['A sessile polyp is usually soft and superficial with a largely '
                               'preserved wave, not a yellow lesion with marked wave loss.',
                               'Nodules are bilateral and symmetric with only mild wave change and '
                               'often shrink with therapy, unlike this lesion.',
                               'Reinke edema is diffuse polypoid swelling along the whole fold, '
                               'typically in smokers, rather than a focal yellow mass.',
                               'Correct.'],
                 'board_pearl': 'Focal wave loss over a subepithelial yellow bulge suggests a '
                                'cyst; therapy rarely resolves it.',
                 'curveball': 'Why can aggressive excision worsen her voice even when the cyst is '
                              'completely removed?',
                 'curveball_answer': 'The superficial lamina propria is what lets the cover '
                                     'vibrate. Wide removal of epithelium or lamina propria around '
                                     'the cyst, deep dissection into the ligament, or thermal '
                                     'injury replaces pliable tissue with scar. The fold then '
                                     'becomes stiff with a poor wave, which is harder to treat '
                                     'than the original cyst. A microflap preserves the cover and '
                                     'limits that risk.'},
 'v254_lar_polycyst_fnd': {'stem': 'A 51-year-old male football coach has 4 months of persistent '
                                   'hoarseness after shouting at a championship game. He does not '
                                   'smoke. Stroboscopy shows a single translucent, pedunculated '
                                   'lesion on the right mid-membranous free edge with a normal '
                                   'mucosal wave in the surrounding fold. The left fold is normal, '
                                   'and the posterior glottis is clear. Which diagnosis is most '
                                   'likely?',
                           'choices': ['Vocal fold cyst',
                                       'Vocal process granuloma',
                                       'Vocal fold polyp',
                                       'Glottic papilloma'],
                           'answer': 2,
                           'explanation': 'Polyps are usually unilateral phonotraumatic lesions '
                                          'arising on the mid-membranous free edge after a '
                                          'shouting episode or chronic misuse. They sit '
                                          'superficially, so the surrounding wave is preserved, '
                                          'and pedunculated polyps move with airflow. A cyst is '
                                          'instead embedded within the cover and reduces the wave '
                                          'over it, and granulomas arise posteriorly. His single '
                                          'translucent lesion with normal surrounding vibration '
                                          'and a clear posterior glottis points to a polyp.',
                           'why_wrong': ['Cysts sit deeper in the superficial lamina propria and '
                                         'reduce the wave over them rather than hanging on a '
                                         'stalk.',
                                         'Granulomas arise on the posterior vocal process, not on '
                                         'the mid-membranous free edge.',
                                         'Correct.',
                                         'Papillomas are exophytic grapelike clusters, often '
                                         'multifocal, rather than a single translucent '
                                         'pedunculated lesion.'],
                           'board_pearl': 'Unilateral mid-membranous lesion after shouting with '
                                          'preserved surrounding wave: polyp.',
                           'curveball': 'What stroboscopic feature would make a deeper cyst more '
                                        'likely than a superficial polyp?',
                           'curveball_answer': 'A markedly reduced or absent mucosal wave directly '
                                               'over the lesion, with a rounded subepithelial '
                                               'bulge seen through intact epithelium, suggests a '
                                               'cyst within the superficial lamina propria. A '
                                               'polyp is typically superficial with preserved '
                                               'wave. A white or yellow color, persistence after '
                                               'therapy, and a reactive contralateral lesion also '
                                               'favor a cyst.'},
 'v254_lar_polycyst_app': {'stem': 'A 33-year-old female daycare worker has 3 months of moderate '
                                   'hoarseness. Stroboscopy shows a small, soft, sessile '
                                   'translucent polyp on the left mid-membranous edge with '
                                   'preserved wave and no leukoplakia. She shouts across a noisy '
                                   'room all day, drinks mainly coffee, and uses hard glottal '
                                   'attacks. She does not smoke and has no airway symptoms. What '
                                   'is the most reasonable initial management?',
                           'choices': ['Voice therapy, then surgery for persistent disease',
                                       'Microlaryngoscopy with cold excision at the first visit',
                                       'Pulsed-dye laser treatment of the polyp in the office',
                                       'Oral steroid course with high-dose PPI for 3 months'],
                           'answer': 0,
                           'explanation': 'Small sessile polyps, particularly when a patient has '
                                          'strong ongoing phonotraumatic behaviors, can shrink '
                                          'with voice therapy and hygiene. Therapy also treats the '
                                          'shouting and hard glottal attacks that would cause '
                                          'recurrence after surgery. If a structural lesion still '
                                          'limits her voice after an adequate trial, '
                                          'phonomicrosurgery is effective. The decision balances '
                                          'lesion size and type, voice demands, and response to '
                                          'therapy, and her preserved wave with no red flags '
                                          'favors a conservative start.',
                           'why_wrong': ['Correct.',
                                         'Immediate excision is reasonable for large or '
                                         'hemorrhagic polyps but ignores the behaviors that would '
                                         'cause recurrence here.',
                                         'Office laser can treat selected polyps, but it is not '
                                         'first-line before she has tried behavioral treatment.',
                                         'Steroids and acid suppression do not correct phonotrauma '
                                         'and are not indicated without inflammatory or reflux '
                                         'findings.'],
                           'board_pearl': 'Small sessile polyps may respond to therapy; reserve '
                                          'surgery for persistent function-limiting lesions.',
                           'curveball': 'Which lesion or patient features would make earlier '
                                        'operative treatment more reasonable?',
                           'curveball_answer': 'Earlier surgery is reasonable for large, '
                                               'pedunculated, fibrotic, or organized hemorrhagic '
                                               'polyps that rarely shrink, for a professional '
                                               'voice user with an imminent critical performance '
                                               'after a failed brief trial, or for any atypical '
                                               'feature such as leukoplakia or irregularity that '
                                               'calls for tissue diagnosis. Therapy before and '
                                               'after surgery still lowers recurrence.'},
 'v254_lar_polycyst_snr': {'stem': 'A 35-year-old male tenor has persistent hoarseness from a '
                                   'right intracordal cyst despite therapy. At microlaryngoscopy, '
                                   'a lateral microflap exposes a cyst whose wall is densely '
                                   'adherent to the overlying epithelium and to the surrounding '
                                   'superficial lamina propria, and the ligament lies just deep to '
                                   'it. Complete removal would require taking a broad strip of '
                                   'lamina propria. What principle should guide dissection?',
                           'choices': ['Remove the adjacent lamina propria to get the whole wall',
                                       'Excise the vocal ligament beneath the adherent cyst',
                                       'Cauterize the cyst bed to destroy any residual lining',
                                       'Accept a small wall remnant to preserve the cover'],
                           'answer': 3,
                           'explanation': 'A retained cyst wall can recur, but stripping the '
                                          'superficial lamina propria or entering the ligament to '
                                          'obtain a perfect specimen can produce permanent scar '
                                          'and stiffness, which is far worse for a tenor than a '
                                          'small recurrence. Senior judgment preserves the '
                                          'vibratory cover, accepts a small adherent remnant when '
                                          'necessary, and plans follow-up stroboscopy. A '
                                          'recurrence can be removed later, whereas lost lamina '
                                          'propria cannot be restored.',
                           'why_wrong': ['Removing broad lamina propria to clear the wall risks '
                                         'permanent stiffness that is worse than possible '
                                         'recurrence.',
                                         'The ligament is not involved by a benign cyst, and '
                                         'removing it would cause severe lasting dysphonia.',
                                         'Thermal injury spreads into the surrounding cover and '
                                         'creates scar; it is not a safe way to treat residual '
                                         'lining.',
                                         'Correct.'],
                           'board_pearl': 'In phonosurgery, preserve the superficial lamina '
                                          'propria even if a small benign remnant remains.',
                           'curveball': 'If postoperative stroboscopy shows persistent stiffness '
                                        'despite good closure, how would management differ from '
                                        'recurrent mass effect?',
                           'curveball_answer': 'Stiffness with good closure and no mass means scar '
                                               'in the lamina propria, so further excision would '
                                               'only worsen it. Treat with voice therapy aimed at '
                                               'flexibility, time for remodeling, and possibly '
                                               'steroid injection into the scar. A visible '
                                               'recurrent bulge with focal wave loss suggests '
                                               'residual cyst, which can be re-excised once '
                                               'healing is complete.'},
 'v128_lar_04': {'stem': 'A 59-year-old woman who has smoked a pack a day for 35 years says '
                         'friends tease her about sounding like a man. She is not breathless. '
                         'Laryngoscopy shows bilateral pale, floppy swelling along the whole '
                         'membranous length of both folds that billows with inspiration. '
                         'Stroboscopy shows large, slow, irregular mucosal waves without a focal '
                         'lesion. What is the most likely diagnosis?',
                 'choices': ['Bilateral vocal fold polyps',
                             'Reinke edema',
                             'Laryngeal hypothyroid myxedema',
                             'Bilateral vocal fold cysts'],
                 'answer': 1,
                 'explanation': 'Reinke edema is diffuse accumulation of gelatinous fluid in the '
                                'superficial lamina propria, Reinke space, along the full '
                                'membranous fold. Smoking is the dominant cause, with phonotrauma '
                                'and reflux contributing. The added mass lowers the fundamental '
                                'frequency, so women develop a deep, masculine voice. Floppy '
                                'swelling that billows with respiration and large, slow waves are '
                                'characteristic. Although she is not breathless, massive disease '
                                'can narrow the glottis and complicate airway management.',
                 'why_wrong': ['Polyps are discrete, usually unilateral lesions at the free edge '
                               'rather than diffuse swelling along both whole folds.',
                               'Correct.',
                               'Hypothyroidism can thicken the folds, but a heavy smoker with this '
                               'classic appearance most likely has Reinke edema.',
                               'Cysts are focal subepithelial masses with reduced wave, not '
                               'diffuse floppy swelling of both folds.'],
                 'board_pearl': 'Smoker with a deep voice and bilateral floppy full-length fold '
                                'swelling: Reinke edema.',
                 'curveball': 'She is scheduled for surgery and the swelling nearly fills the '
                              'glottis. What airway consideration matters?',
                 'curveball_answer': 'Massive edema can make mask ventilation and intubation '
                                     'harder and the folds can obstruct the view or tube passage. '
                                     'Plan with anesthesia beforehand: have smaller tubes ready, '
                                     'consider jet ventilation or awake techniques, and keep a '
                                     'surgical airway option available. Treating one side or '
                                     'staging debulking reduces the risk of postoperative web.'},
 'v141_lar_04': {'stem': 'A 56-year-old female bartender who smokes a pack a day has a very '
                         'low-pitched voice that has slowly deepened over years. Laryngoscopy '
                         'shows bilateral diffuse polypoid swelling of both membranous folds '
                         'without leukoplakia or a focal lesion, and she has no breathlessness or '
                         'stridor. She asks for surgery to restore her old voice and plans to keep '
                         'smoking. Which treatment principle is correct?',
                 'choices': ['Smoking cessation is the core treatment, with surgery later if '
                             'needed',
                             'Microflap reduction now, because smoking does not affect the final '
                             'outcome',
                             'Radiation therapy to shrink the edematous lamina propria',
                             'Oral antibiotics and steroids for the swelling, then reassess'],
                 'answer': 0,
                 'explanation': 'Reinke edema is driven mainly by smoking, so continued smoking '
                                'undermines any treatment and raises the recurrence risk after '
                                'surgery. Cessation, along with voice therapy and reflux control '
                                'when relevant, is the foundation. Phonomicrosurgery with '
                                'microflap reduction can improve pitch and quality, but it is '
                                'offered for persistent function-limiting disease or airway '
                                'compromise, ideally after she quits. Surgery also provides tissue '
                                'for histology if the mucosa looks atypical, given her risk of '
                                'malignancy.',
                 'why_wrong': ['Correct.',
                               'Smoking keeps injuring the lamina propria, so surgery while she '
                               'still smokes carries a high recurrence risk.',
                               'Radiation has no role in this benign condition and would scar the '
                               'folds and worsen voice.',
                               'Reinke edema is not infectious or steroid responsive; these drugs '
                               'do not reverse the gelatinous expansion.'],
                 'board_pearl': 'Reinke edema: smoking cessation first; surgery for persistent '
                                'function-limiting disease or airway concern.',
                 'curveball': 'Her edema is so bulky that she now has exertional stridor. How does '
                              'that change timing?',
                 'curveball_answer': 'Airway compromise moves surgery earlier: she needs debulking '
                                     'now rather than waiting for the effect of smoking cessation. '
                                     'Plan the airway with anesthesia and use conservative '
                                     'microflap reduction of the bulkiest areas while preserving '
                                     'epithelium, staging the opposite side if needed. Continue to '
                                     'press for cessation to prevent recurrence.'},
 'v252_lar_reinke_app': {'stem': 'A 52-year-old male construction foreman who smokes 30 cigarettes '
                                 'a day has a markedly deep, rough voice. Stroboscopy shows '
                                 'moderate bilateral Reinke edema with no leukoplakia, no focal '
                                 'mass, and a patent glottis. He has no stridor or exertional '
                                 'dyspnea and is willing to try quitting. Which initial management '
                                 'best addresses the disease rather than only the sound of his '
                                 'voice?',
                         'choices': ['Bilateral microflap reduction within the next 2 weeks',
                                     'Bilateral thyroarytenoid botulinum toxin injection',
                                     'Smoking cessation plus voice and reflux optimization',
                                     'Bilateral CO2 laser stripping of the vocal fold cover'],
                         'answer': 2,
                         'explanation': 'Reinke edema reflects chronic injury of the superficial '
                                        'lamina propria, mainly from smoking, with phonotrauma and '
                                        'reflux as contributors. Removing the cause through '
                                        'smoking cessation is the most important intervention and '
                                        'can stop progression, although established edema rarely '
                                        'resolves fully. Voice therapy and reflux treatment when '
                                        'indicated reduce further injury. Microflap reduction is '
                                        'reserved for persistent function-limiting voice or airway '
                                        'disease, ideally after he quits.',
                         'why_wrong': ['Early surgery while he smokes heavily treats the swelling '
                                       'but not its cause, so recurrence is likely.',
                                       'Toxin weakens the adductors and treats spasm, not '
                                       'gelatinous expansion of the superficial lamina propria.',
                                       'Correct.',
                                       'Stripping the whole cover removes the lamina propria and '
                                       'risks permanent scar, webs, and severe dysphonia.'],
                         'board_pearl': 'Treat the cause of Reinke edema, smoking, before '
                                        'operating on its effect.',
                         'curveball': 'What laryngoscopic finding would make you biopsy rather '
                                      'than assume all polypoid change is benign?',
                         'curveball_answer': 'Leukoplakia, erythroplakia, an irregular or granular '
                                             'surface, a focal firm area, ulceration, asymmetric '
                                             'stiffness on stroboscopy, or reduced fold mobility '
                                             'all raise concern for dysplasia or carcinoma in a '
                                             'heavy smoker. These findings call for '
                                             'microlaryngoscopy with biopsy, with the specimen '
                                             'from the suspicious area labeled separately.'},
 'v252_lar_reinke_snr': {'stem': 'A 64-year-old woman with massive bilateral Reinke edema has '
                                 'exertional stridor and is scheduled for suspension '
                                 'microlaryngoscopy. Flexible laryngoscopy shows the polypoid '
                                 'folds nearly filling the glottis, with only a small posterior '
                                 'chink visible on inspiration. She quit smoking 6 months ago. The '
                                 'anesthesiologist asks about the plan. What is the best operative '
                                 'principle?',
                         'choices': ['Excise both covers to the vocalis in one stage',
                                     'Plan the airway together and debulk conservatively',
                                     'Perform bilateral posterior cordotomy for airway',
                                     'Use routine induction and a standard 7.5 tube'],
                         'answer': 1,
                         'explanation': 'Massive edema can obstruct mask ventilation and the view '
                                        'of the glottis, so airway planning with anesthesia must '
                                        'happen before induction, with small tubes, jet '
                                        'ventilation, or awake options and a surgical airway plan. '
                                        'The operation must protect both airway and vibratory '
                                        'cover: microflap evacuation of gelatinous material with '
                                        'conservative trimming of redundant epithelium. Staging '
                                        'the sides, or avoiding the anterior commissure on one '
                                        'side, reduces web formation.',
                         'why_wrong': ['Stripping both covers to muscle removes the vibratory '
                                       'layer and risks webs, stiffness, and permanent dysphonia.',
                                       'Correct.',
                                       'Cordotomy widens the airway by sacrificing voice and is '
                                       'not needed when the obstruction is soft tissue that can be '
                                       'reduced.',
                                       'Routine induction ignores the risk that bulky edema '
                                       'obstructs the airway or the view during intubation.'],
                         'board_pearl': 'Massive Reinke edema: plan the airway with anesthesia, '
                                        'then perform conservative epithelium-preserving '
                                        'debulking.',
                         'curveball': 'One side has an irregular leukoplakic focus. How would that '
                                      'alter specimen handling and oncologic caution?',
                         'curveball_answer': 'Biopsy or excise the leukoplakic area separately and '
                                             'label it apart from the edematous tissue so '
                                             'pathology can grade dysplasia or carcinoma. Avoid '
                                             'aggressive resection of that side until pathology '
                                             'returns, and if invasive carcinoma is found, staging '
                                             'and oncologic treatment take precedence over the '
                                             'voice plan.'},
 'v128_lar_05': {'stem': 'A 78-year-old woman, a retired librarian, has 2 years of a soft, breathy '
                         'voice that tires during phone calls with her grandchildren. She has no '
                         'dysphagia, tremor, or neurologic history and no prior neck surgery. '
                         'Stroboscopy shows bilateral concave free edges, prominent vocal '
                         'processes, a spindle-shaped gap on closure, and full symmetric abduction '
                         'and adduction. What is the best diagnosis?',
                 'choices': ['Bilateral superior laryngeal nerve paresis',
                             'Hypokinetic dysphonia from Parkinson disease',
                             'Bilateral sulcus vergeture from old phonotrauma',
                             'Presbylaryngis with bilateral vocal fold atrophy'],
                 'answer': 3,
                 'explanation': 'With age, the thyroarytenoid muscle atrophies and the lamina '
                                'propria thins, so the free edges become concave and the vocal '
                                'processes stand out. The folds then meet only at their ends, '
                                'leaving a spindle-shaped gap that lets air escape, producing a '
                                'soft, breathy, easily fatigued voice. Full symmetric motion '
                                'argues against paralysis or paresis, and the absence of '
                                'neurologic signs argues against Parkinson disease. Presbylaryngis '
                                'remains a diagnosis of exclusion.',
                 'why_wrong': ['Superior laryngeal nerve paresis causes pitch problems and '
                               'asymmetric tilt of the glottis rather than symmetric bowing with '
                               'prominent processes.',
                               'Hypokinetic dysphonia comes with tremor, masked face, or small '
                               'handwriting, none of which she has.',
                               'Sulcus vergeture can bow the folds, but it typically starts '
                               'earlier in life and shows a linear furrow with stiffness.',
                               'Correct.'],
                 'board_pearl': 'Bilateral bowing, prominent vocal processes, and a spindle gap '
                                'with normal motion: presbylaryngis.',
                 'curveball': 'Voice therapy helped only partly and she is frustrated by phone '
                              'calls. When is injection augmentation reasonable for her '
                              'presbyphonia?',
                 'curveball_answer': 'Augmentation is reasonable when glottic insufficiency still '
                                     'limits communication after an adequate trial of therapy and '
                                     'the patient is motivated. Bilateral office injection with a '
                                     'hyaluronic acid or similar temporary filler closes the '
                                     'spindle gap and can be repeated or used as a trial before '
                                     'durable bilateral medialization. Continue voice therapy '
                                     'afterward, because breath support and efficient phonation '
                                     'remain important.'},
 'v145_lar_09': {'stem': 'An 80-year-old male retired lawyer who leads a weekly book club has a '
                         'weak, breathy voice that fades by the end of conversations. He has no '
                         'dysphagia, no weight loss, and no smoking history. Stroboscopy shows '
                         'bilateral bowing with a spindle-shaped gap, prominent vocal processes, '
                         'symmetric motion, and no mucosal lesion. He asks what treatment sequence '
                         'makes sense. Which management sequence is reasonable?',
                 'choices': ['Bilateral medialization thyroplasty as the initial therapy',
                             'Testosterone therapy to restore vocal fold muscle bulk',
                             'Voice therapy first, then augmentation if gap persists',
                             'Bilateral fat injection now, then voice therapy later'],
                 'answer': 2,
                 'explanation': 'Presbyphonia reflects age-related muscle atrophy and thinning of '
                                'the lamina propria. Voice therapy, particularly programs that '
                                'build respiratory support, efficient closure, and loudness such '
                                'as phonation resistance training, improves voice-related quality '
                                'of life in many patients and is the first-line treatment. When a '
                                'function-limiting gap persists after therapy, injection '
                                'augmentation and, for durable benefit, bilateral medialization '
                                'thyroplasty can improve closure. Therapy remains useful alongside '
                                'these procedures.',
                 'why_wrong': ['Thyroplasty is a durable option after therapy and often after a '
                               'successful injection trial, not the first treatment.',
                               'Hormone therapy has no established role for age-related vocal fold '
                               'atrophy and carries systemic risks in older men.',
                               'Correct.',
                               'Augmentation can be offered after an inadequate response to '
                               'therapy, but it is not the starting point.'],
                 'board_pearl': 'Presbyphonia: voice therapy first; augmentation or thyroplasty '
                                'for persistent function-limiting insufficiency.',
                 'curveball': 'Stroboscopy also shows that his left fold lags and moves less '
                              'briskly than the right. How does a coexisting unilateral paresis '
                              'change the plan?',
                 'curveball_answer': 'An asymmetric lag suggests unilateral paresis on top of '
                                     'atrophy, which is not explained by aging. Image the nerve '
                                     'course if the cause is unclear and consider laryngeal EMG. '
                                     'Treatment may need unilateral or asymmetric augmentation '
                                     'targeting the weaker fold, and the gap may respond less to '
                                     'therapy alone, so earlier augmentation is reasonable.'},
 'v252_lar_presby_app': {'stem': 'A 75-year-old woman who sings in her church choir and volunteers '
                                 'as a docent has a year of a weak, breathy voice and effortful '
                                 'projection. She has no dysphagia, cough, or neurologic symptoms. '
                                 'Stroboscopy shows bilateral bowing and a spindle gap with mild '
                                 'supraglottic squeezing, symmetric motion, and no lesion. Which '
                                 'first treatment strategy is best?',
                         'choices': ['Voice therapy for breath support and efficient closure',
                                     'Bilateral injection augmentation in the office',
                                     'Complete voice rest until fatigue resolves',
                                     'Bilateral type I medialization thyroplasty'],
                         'answer': 0,
                         'explanation': 'Presbyphonia is usually treated first with voice therapy. '
                                        'Breath-support training, resonant voice work, and '
                                        'exercises that build adduction and loudness reduce effort '
                                        'and improve closure, while helping her drop the '
                                        'compensatory supraglottic squeeze. Many patients improve '
                                        'enough to avoid procedures, and therapy also clarifies '
                                        'how much of the problem is structural gap versus '
                                        'inefficient technique. Augmentation is reasonable when '
                                        'glottic insufficiency stays function limiting despite '
                                        'therapy or when she needs more closure.',
                         'why_wrong': ['Correct.',
                                       'Injection augmentation is reasonable later if a meaningful '
                                       'gap persists, but it bypasses a first-line treatment that '
                                       'often succeeds.',
                                       'Voice rest does nothing for atrophy and may worsen '
                                       'conditioning of the laryngeal and respiratory muscles.',
                                       'Framework surgery is reserved for persistent '
                                       'function-limiting insufficiency, usually after therapy and '
                                       'an injection trial.'],
                         'board_pearl': 'Presbyphonia improves with targeted voice therapy; '
                                        'reserve procedures for persistent function-limiting gaps.',
                         'curveball': 'Which symptoms or asymmetric findings would make you reopen '
                                      'the diagnosis instead of attributing dysphonia to age?',
                         'curveball_answer': 'Reopen it for asymmetric mobility or fold height, a '
                                             'unilateral lag, a mucosal lesion or leukoplakia, '
                                             'rapid progression, dysphagia, tremor, slurred '
                                             'speech, limb weakness, or smoking with weight loss. '
                                             'These suggest paresis, cancer, Parkinson disease, '
                                             'ALS, or myasthenia, which need imaging, EMG, '
                                             'neurology referral, or biopsy rather than '
                                             'age-related therapy.'},
 'v252_lar_presby_snr': {'stem': 'An 82-year-old male retired professor who still lectures monthly '
                                 'has persistent breathy dysphonia from bilateral atrophy despite '
                                 '3 months of excellent participation in voice therapy. '
                                 'Stroboscopy shows a persistent spindle gap and symmetric motion '
                                 'without a lesion. He is unsure whether a permanent operation '
                                 'would help enough to justify it. What is the most useful next '
                                 'strategy?',
                         'choices': ['Bilateral medialization thyroplasty under local anesthesia',
                                     'Bilateral fat injection as a single permanent procedure',
                                     'Repeat the same voice therapy program for 6 more months',
                                     'Office injection trial, then reassess before surgery'],
                         'answer': 3,
                         'explanation': 'After an adequate therapy trial, temporary injection '
                                        'augmentation with hyaluronic acid or a similar filler '
                                        'tests how much of his disability comes from the spindle '
                                        'gap. If voice, effort, and patient-reported quality of '
                                        'life improve meaningfully, he can choose repeat '
                                        'injections or a durable bilateral medialization '
                                        'thyroplasty with realistic expectations. If benefit is '
                                        'small, he avoids an unnecessary operation. The trial '
                                        'respects his uncertainty and guides a decision based on '
                                        'his own response.',
                         'why_wrong': ['Thyroplasty is a reasonable durable option, but committing '
                                       'before a trial ignores his uncertainty about benefit.',
                                       'Fat injection has unpredictable resorption and requires an '
                                       'operating room harvest; it is not an ideal first trial.',
                                       'He already participated well in therapy, so repeating the '
                                       'same program is unlikely to close the remaining gap.',
                                       'Correct.'],
                         'board_pearl': 'When benefit from durable medialization is uncertain, use '
                                        'a temporary injection as a therapeutic trial.',
                         'curveball': 'He also coughs weakly and has had one aspiration pneumonia. '
                                      'How does that change the value you place on improved '
                                      'glottic closure?',
                         'curveball_answer': 'Better glottic closure strengthens cough and '
                                             'protects the airway, so augmentation now serves '
                                             'safety as well as voice. That makes treatment more '
                                             'urgent and the benefit greater. Pair it with an '
                                             'instrumental swallow study to define the aspiration '
                                             'mechanism, because atrophy alone rarely explains '
                                             'pneumonia and other contributors may need '
                                             'treatment.'},
 'v128_lar_06': {'stem': 'A 34-year-old female second-grade teacher has 5 months of a rough, '
                         'effortful voice that worsens through the school week and improves after '
                         'weekends. She has neck tension by afternoon. Stroboscopy shows lateral '
                         'compression of the false folds during phonation with normal fold '
                         'structure, symmetric mobility, complete closure under the squeeze, and a '
                         'normal mucosal wave. What is the best initial treatment?',
                 'choices': ['Two weeks of total voice rest',
                             'Voice therapy',
                             'Empiric twice-daily PPI therapy',
                             'Office injection augmentation'],
                 'answer': 1,
                 'explanation': 'Fluctuating effortful dysphonia that worsens with voice load, '
                                'neck tension, and supraglottic compression with normal structure, '
                                'motion, closure, and wave is primary muscle tension dysphonia. It '
                                'is a functional hyperfunction disorder treated first with '
                                'behavioral voice therapy: circumlaryngeal massage, resonant '
                                'voice, and semi-occluded vocal tract exercises reduce excess '
                                'laryngeal tension and restore efficient phonation. Most patients '
                                'improve over several sessions. The examination has excluded a '
                                'lesion or glottic gap that might be driving the compensatory '
                                'squeeze.',
                 'why_wrong': ['Brief rest may temporarily ease symptoms but does not retrain the '
                               'hyperfunctional pattern, which returns when she resumes teaching.',
                               'Correct.',
                               'Empiric acid suppression is not indicated without reflux symptoms '
                               'or findings, and it does not treat muscular hyperfunction.',
                               'Augmentation treats glottic insufficiency; her folds close fully '
                               'and adding bulk would not address the squeeze.'],
                 'board_pearl': 'Primary MTD: normal structure and motion with supraglottic '
                                'squeeze; voice therapy is first-line.',
                 'curveball': 'Stroboscopy later shows a subtle unilateral lag and a small gap '
                              'beneath the squeeze. How does that change your plan?',
                 'curveball_answer': 'A lag with a gap suggests paresis, with the squeeze '
                                     'compensating for glottic insufficiency. Investigate the '
                                     'cause with imaging when unexplained and laryngeal EMG when '
                                     'useful. Treatment shifts toward closing the gap, possibly '
                                     'with injection augmentation, while continuing therapy, '
                                     'because therapy alone rarely relieves compensatory squeeze '
                                     'over an underlying gap.'},
 'v145_lar_08': {'stem': 'A 29-year-old male actor has 3 months of vocal fatigue, throat ache, and '
                         'loss of projection during performances. Laryngoscopy shows '
                         'anterior-posterior compression of the supraglottis during speech, normal '
                         'fold mobility, and no lesion; stroboscopy with high-pitched phonation '
                         'shows complete closure and a normal mucosal wave. His larynx sits high '
                         'and is tender on palpation. What is the first-line treatment?',
                 'choices': ['Voice therapy to reduce laryngeal tension',
                             'Botulinum toxin into the false vocal folds',
                             'Microlaryngoscopy to exclude a hidden lesion',
                             'Oral corticosteroid taper before performances'],
                 'answer': 0,
                 'explanation': 'Anterior-posterior supraglottic compression, a high tender '
                                'larynx, and fatigue with normal structure, closure, and wave are '
                                'primary muscle tension dysphonia, a hyperkinetic functional voice '
                                'disorder. First-line treatment is voice therapy with '
                                'circumlaryngeal massage, laryngeal reposturing, resonant voice, '
                                'and breath-phonation coordination. High-pitched phonation opened '
                                'the supraglottis enough to view the folds, which excluded an '
                                'underlying lesion or gap driving compensatory tension. Most '
                                'patients regain efficient voice with targeted therapy.',
                 'why_wrong': ['Correct.',
                               'Toxin is reserved for rare refractory supraglottic hyperfunction '
                               'and is not first-line when therapy has not been tried.',
                               'Stroboscopy already showed the folds clearly, so operative '
                               'examination adds risk without new diagnostic information.',
                               'Steroids reduce inflammation, which he does not have, and repeated '
                               'courses carry systemic risk without fixing tension.'],
                 'board_pearl': 'MTD is a functional hyperkinetic disorder; therapy reduces '
                                'tension once an underlying driver is excluded.',
                 'curveball': 'What stroboscopic finding would suggest an underlying paresis '
                              'rather than primary MTD?',
                 'curveball_answer': 'A persistent glottic gap, asymmetric amplitude or phase, a '
                                     'fold that lags or sits at a different height, or bowing on '
                                     'one side suggests paresis. Reduced lateral excursion or '
                                     'rapid fatigue on repetitive tasks also points to neural '
                                     'weakness. The supraglottic squeeze then compensates for the '
                                     'gap rather than being the primary problem.'},
 'v252_lar_mtd_app': {'stem': 'A 53-year-old female choir teacher has 4 months of strained '
                              'hoarseness and fatigue. Flexible laryngoscopy shows marked false '
                              'fold compression during speech that hides the true folds. The '
                              'referring physician diagnosed primary muscle tension dysphonia and '
                              'wants to start therapy. She had cervical spine surgery 8 months '
                              'ago. What is the most important diagnostic step before accepting '
                              'that diagnosis?',
                      'choices': ['Begin voice therapy and reexamine if no improvement',
                                  'Laryngeal EMG of both thyroarytenoid muscles first',
                                  'Stroboscopy with maneuvers to view the true folds',
                                  'Barium swallow to look for postoperative esophageal injury'],
                      'answer': 2,
                      'explanation': 'Supraglottic compression is a behavior, not a complete '
                                     'diagnosis. It may be primary, but it frequently compensates '
                                     'for glottic insufficiency, subtle paresis, or a mucosal '
                                     'lesion, and her recent anterior cervical spine surgery '
                                     'raises the possibility of recurrent laryngeal nerve injury. '
                                     'Stroboscopy with maneuvers that open the supraglottis, such '
                                     'as high-pitched phonation, sniffing, and whispering, should '
                                     'show true fold structure, closure, symmetry, and wave before '
                                     'therapy begins.',
                      'why_wrong': ['Starting therapy without seeing the true folds risks missing '
                                    'a paresis or lesion, delaying correct treatment.',
                                    'EMG is useful when paresis is suspected, but the true folds '
                                    'must first be visualized to look for asymmetry or a gap.',
                                    'Correct.',
                                    'Her complaint is voice rather than swallowing, so a swallow '
                                    'study does not answer the question about fold function.'],
                      'board_pearl': 'Supraglottic squeeze can hide a lesion or paresis; view the '
                                     'true folds before diagnosing primary MTD.',
                      'curveball': 'What stroboscopic closure pattern would make you suspect '
                                   'subtle unilateral paresis beneath apparent muscle tension?',
                      'curveball_answer': 'Suspect paresis with a persistent posterior or spindle '
                                          'gap, asymmetric amplitude or phase with one fold '
                                          'lagging, a fold that is bowed or lower, or reduced '
                                          'abduction with rapid alternating tasks. Asymmetric '
                                          'squeezing, where the false fold on one side compresses '
                                          'more, also suggests compensation for a weaker side.'},
 'v252_lar_mtd_snr': {'stem': 'A 47-year-old male radio announcer has persistent supraglottic '
                              'hyperfunction despite 12 sessions of skilled voice therapy with '
                              'good adherence. Repeat stroboscopy now shows a small persistent '
                              'glottic gap, slightly bowed left fold, and asymmetric phase with '
                              'the left lagging. CT of the nerve course was normal. What is the '
                              'best next decision?',
                      'choices': ['Intensify therapy with daily sessions for 3 more months',
                                  'Treat the gap as the driver with an augmentation trial',
                                  'Rediagnose adductor dystonia and start toxin therapy',
                                  'Refer for psychotherapy as refractory functional dysphonia'],
                      'answer': 1,
                      'explanation': 'Failure of skilled therapy should trigger diagnostic '
                                     'reassessment. A persistent gap, bowing, and a lagging left '
                                     'fold suggest subtle left paresis, with the supraglottic '
                                     'squeeze compensating for inadequate glottic closure. '
                                     'Improving closure with temporary injection augmentation '
                                     'serves as both a diagnostic test and treatment: if the gap '
                                     'is the driver, the squeeze lessens and therapy becomes more '
                                     'effective. Laryngeal EMG can support the diagnosis of '
                                     'paresis and guide longer-term choices.',
                      'why_wrong': ['More of the same therapy is unlikely to help when an '
                                    'underlying gap keeps driving compensation.',
                                    'Correct.',
                                    'Dystonia causes task-specific spasmodic breaks, not a '
                                    'constant squeeze over a persistent gap with an asymmetric '
                                    'lag.',
                                    'His examination shows an organic gap and asymmetry, so '
                                    'labeling the problem as purely functional would miss the '
                                    'cause.'],
                      'board_pearl': 'MTD refractory to therapy: reexamine for glottic '
                                     'insufficiency or paresis driving secondary hyperfunction.',
                      'curveball': 'When would laryngeal EMG add useful information in his '
                                   'suspected subtle paresis?',
                      'curveball_answer': 'EMG is useful when stroboscopic findings are subtle or '
                                          'disputed, when deciding between temporary and durable '
                                          'augmentation, and when localizing recurrent versus '
                                          'superior laryngeal nerve involvement. Reduced '
                                          'recruitment or polyphasic potentials confirm paresis '
                                          'and suggest prognosis. A normal study supports looking '
                                          'for another cause, such as scar or atrophy.'},
 'v128_lar_08': {'stem': 'A 43-year-old woman has 8 months of progressive exertional dyspnea '
                         'treated as asthma without benefit. She has never been intubated, had a '
                         'tracheostomy, or had neck trauma. ANCA, ACE level, and inflammatory '
                         'markers are normal, and she has no sinus, ear, kidney, or joint '
                         'symptoms. A flow-volume loop shows flattening of both limbs. Endoscopy '
                         'shows a smooth circumferential scar just below the folds. Which '
                         'diagnosis is most likely?',
                 'choices': ['Granulomatosis with polyangiitis',
                             'Laryngotracheal sarcoidosis',
                             'Postintubation tracheal stenosis',
                             'Idiopathic subglottic stenosis'],
                 'answer': 3,
                 'explanation': 'Idiopathic subglottic stenosis is a fibroinflammatory narrowing '
                                'of the subglottis and upper trachea that occurs almost '
                                'exclusively in otherwise healthy adult women, often mistreated as '
                                'asthma for months. Biphasic flattening on the flow-volume loop '
                                'shows a fixed upper airway obstruction. The diagnosis is one of '
                                'exclusion: no intubation or trauma, normal ANCA and ACE, and no '
                                'systemic features of vasculitis or sarcoidosis. The smooth '
                                'circumferential scar just below normal folds is typical.',
                 'why_wrong': ['GPA usually has sinonasal, ear, pulmonary, or renal disease and is '
                               'often ANCA positive, all absent here.',
                               'Sarcoidosis more commonly involves the supraglottis and usually '
                               'has systemic features and an elevated ACE.',
                               'She has never been intubated or had a tracheostomy, so there is no '
                               'mechanism for postintubation stenosis.',
                               'Correct.'],
                 'board_pearl': 'Healthy woman with fixed upper airway obstruction and no '
                                'intubation history: idiopathic subglottic stenosis.',
                 'curveball': 'She later develops nasal crusting, epistaxis, and hematuria. Which '
                              'systemic disease must you consider, and how?',
                 'curveball_answer': 'Sinonasal disease with hematuria suggests granulomatosis '
                                     'with polyangiitis, which can cause subglottic stenosis '
                                     'indistinguishable from the idiopathic form. Repeat ANCA '
                                     'testing, especially PR3, check urinalysis and renal '
                                     'function, and consider chest CT and biopsy of nasal or '
                                     'airway tissue. Active GPA requires systemic '
                                     'immunosuppression with rheumatology alongside airway '
                                     'treatment.'},
 'v141_lar_02': {'stem': 'A 46-year-old woman with idiopathic subglottic stenosis has worsening '
                         'exertional dyspnea. Bronchoscopy shows a thin, web-like circumferential '
                         'scar 1.5 cm below the folds, under 1 cm long, with about 60% '
                         'obstruction, intact cartilage, and no malacia. She has never had airway '
                         'surgery and wants the least invasive effective option. What treatment is '
                         'most appropriate initially?',
                 'choices': ['Cricotracheal resection with primary anastomosis',
                             'Tracheostomy placed below the level of stenosis',
                             'Endoscopic radial incision and balloon dilation',
                             'Silicone stent placed across the subglottic scar'],
                 'answer': 2,
                 'explanation': 'Short, thin, web-like stenoses without cartilage collapse often '
                                'respond well to endoscopic treatment. Radial incisions with a CO2 '
                                'laser or cold knife followed by balloon dilation, often with '
                                'intralesional steroid injection, open the lumen with minimal '
                                'morbidity. Recurrence is common in idiopathic disease and serial '
                                'procedures may be needed, but many patients maintain good '
                                'function for long intervals. Open resection is reserved for '
                                'longer, mature, or rapidly recurring disease.',
                 'why_wrong': ['Resection is more durable but carries greater morbidity, so it is '
                               'usually reserved for recurrent or more extensive disease.',
                               'Tracheostomy bypasses the stenosis but is unnecessary when a short '
                               'web can be opened endoscopically.',
                               'Correct.',
                               'Stents in the subglottis cause granulation, migration, and further '
                               'scar and are rarely used for benign short webs.'],
                 'board_pearl': 'Short thin web-like subglottic stenosis: start with endoscopic '
                                'incision and dilation, plus steroid if desired.',
                 'curveball': 'Her stenosis recurs every 4 months despite dilation. Which features '
                              'make cricotracheal resection more appropriate?',
                 'curveball_answer': 'Rapid recurrence after repeated dilation, mature thick '
                                     'circumferential scar, length beyond a short web, cartilage '
                                     'involvement or malacia, and a patient willing to accept open '
                                     'surgery favor resection. Cricotracheal resection with '
                                     'primary anastomosis has high durable success but risks '
                                     'recurrent nerve injury, voice change, and anastomotic '
                                     'complications. It is best performed in experienced airway '
                                     'centers.'},
 'v249_lar_stenosis_fnd': {'stem': 'A 58-year-old man has progressive exertional dyspnea and noisy '
                                   'breathing in and out 4 months after a 3-week ICU stay for '
                                   'pancreatitis with 18 days of intubation. He was treated twice '
                                   'for presumed COPD flares without benefit. Flexible '
                                   'laryngoscopy shows normal folds that abduct fully, and a '
                                   'flow-volume loop shows flattening of both limbs. Which '
                                   'diagnosis should be strongly considered?',
                           'choices': ['Postintubation subglottic or tracheal stenosis',
                                       'Posterior glottic stenosis with joint fixation',
                                       'Bilateral vocal fold paralysis in paramedian position',
                                       'Tracheobronchomalacia from chronic airway disease'],
                           'answer': 0,
                           'explanation': 'Prolonged intubation injures the subglottis and trachea '
                                          'through cuff and tube pressure that causes ischemic '
                                          'ulceration, chondritis, and circumferential scar. Fixed '
                                          'obstruction below the glottis produces biphasic stridor '
                                          'and flattening of both limbs of the flow-volume loop, '
                                          'and patients are often misdiagnosed with asthma or '
                                          'COPD. Fully abducting folds exclude glottic causes, '
                                          'placing the narrowing lower. Bronchoscopy defines the '
                                          'site, length, and grade of the stenosis.',
                           'why_wrong': ['Correct.',
                                         'Posterior glottic stenosis limits abduction, but his '
                                         'folds abduct fully, so the obstruction must be lower.',
                                         'Bilateral paralysis is excluded by normal full abduction '
                                         'on laryngoscopy.',
                                         'Malacia causes dynamic collapse, typically flattening '
                                         'the expiratory limb, rather than a fixed biphasic '
                                         'pattern.'],
                           'board_pearl': 'Dyspnea and biphasic stridor after intubation with '
                                          'mobile folds: suspect subglottic or tracheal stenosis.',
                           'curveball': 'What history would raise concern for idiopathic '
                                        'subglottic stenosis, GPA, relapsing polychondritis, or '
                                        'another inflammatory cause?',
                           'curveball_answer': 'Idiopathic stenosis is suggested by a woman with '
                                               'no intubation or trauma. GPA is suggested by '
                                               'sinonasal crusting, epistaxis, otitis, hematuria, '
                                               'or lung nodules with positive ANCA. Relapsing '
                                               'polychondritis is suggested by recurrent ear or '
                                               'nasal cartilage inflammation. Sarcoidosis, '
                                               'amyloidosis, and Crohn disease are also causes. '
                                               'Lack of an intubation history should prompt a full '
                                               'inflammatory workup.'},
 'v249_lar_stenosis_app': {'stem': 'A 49-year-old woman has a known subglottic stenosis after a '
                                   '2-week intubation and is stable in clinic with exertional '
                                   'dyspnea but no stridor at rest. Flexible laryngoscopy shows '
                                   'mobile folds and a narrowed subglottis, but the scope cannot '
                                   'pass to see its lower extent. She asks whether endoscopic '
                                   'dilation will be enough. Which assessment best informs '
                                   'treatment planning?',
                           'choices': ['Pulmonary function testing with a flow-volume loop alone',
                                       'Repeat office flexible laryngoscopy in 3 months',
                                       'Empiric balloon dilation and judging the response',
                                       'Operative endoscopy with imaging to define length and '
                                       'cartilage'],
                           'answer': 3,
                           'explanation': 'Treatment depends on more than the percentage '
                                          'narrowing. Rigid and flexible endoscopy under '
                                          'anesthesia, with sizing by endotracheal tubes, defines '
                                          'grade, length, distance from the folds and cricoid, '
                                          'maturity, and cartilage integrity, while CT helps show '
                                          'length, wall thickness, and malacia. Short, thin, soft '
                                          'stenoses suit endoscopic treatment, whereas long, '
                                          'mature, cartilaginous, or cricoid-involving disease '
                                          'often needs open reconstruction. Flow-volume loops and '
                                          'symptom scores track function over time.',
                           'why_wrong': ['Flow-volume loops show fixed obstruction and help '
                                         'monitoring, but they cannot measure length or cartilage '
                                         'involvement.',
                                         'Waiting with repeat office examination does not provide '
                                         'the information needed and the scope still cannot pass '
                                         'the narrowing.',
                                         'Dilating without characterizing the stenosis risks '
                                         'choosing a treatment that cannot succeed for long or '
                                         'cartilaginous disease.',
                                         'Correct.'],
                           'board_pearl': 'Plan airway stenosis surgery from length, grade, '
                                          'location, maturity, and cartilage integrity, not '
                                          'percent narrowing alone.',
                           'curveball': 'The stenosis is severe enough that passing an '
                                        'endotracheal tube may be impossible. What airway plan '
                                        'would you make before endoscopy?',
                           'curveball_answer': 'Plan jointly with anesthesia: spontaneous '
                                               'ventilation or jet ventilation through a rigid '
                                               'bronchoscope, small tubes and dilators ready, and '
                                               'avoidance of paralysis until the airway is '
                                               'secured. Mark the neck and have a tracheostomy set '
                                               'and surgeon ready, recognizing the stenosis may '
                                               'sit at the usual tracheostomy site.'},
 'v249_lar_stenosis_snr': {'stem': 'A 54-year-old man has needed five endoscopic dilations in 18 '
                                   'months for a postintubation tracheal stenosis, each giving '
                                   'only 3 months of relief. Bronchoscopy shows a 2-cm mature '
                                   'circumferential scar beginning 3 cm below the cricoid with '
                                   'intact cartilage elsewhere, normal folds, and no active '
                                   'inflammation. He is healthy with normal neck mobility. What is '
                                   'the best next step?',
                           'choices': ['Continued scheduled dilations every 3 months indefinitely',
                                       'Tracheal resection with primary end-to-end anastomosis',
                                       'Long-term silicone stent across the stenotic segment',
                                       'Mitomycin application at the next dilation and then '
                                       'reassess'],
                           'answer': 1,
                           'explanation': 'Rapid recurrence after repeated dilation shows mature '
                                          'structural scar that endoscopic treatment cannot '
                                          'control. A short, focal tracheal stenosis well below '
                                          'the cricoid, with normal cartilage elsewhere, normal '
                                          'folds, no active inflammation, and good neck mobility, '
                                          'is ideal for segmental resection with primary '
                                          'end-to-end anastomosis. Durable success rates are high '
                                          'in experienced airway centers. Continuing the same '
                                          'procedure accumulates anesthetics, cost, and risk '
                                          'without a durable result.',
                           'why_wrong': ['Repeated dilation has already failed five times, showing '
                                         'diminishing returns for mature circumferential scar.',
                                         'Correct.',
                                         'Stents in benign stenosis cause granulation, mucus '
                                         'plugging, and migration and are reserved for poor '
                                         'surgical candidates.',
                                         'Topical mitomycin may lengthen intervals for some '
                                         'stenoses but is unlikely to give durable control of '
                                         'mature recurrent scar.'],
                           'board_pearl': 'Rapidly recurrent short mature tracheal stenosis in a '
                                          'fit patient: resect and reanastomose.',
                           'curveball': 'In a different patient referred for the same operation, '
                                        'which features would change the reconstructive choice '
                                        'away from simple segmental resection?',
                           'curveball_answer': 'Long-segment stenosis needing release maneuvers or '
                                               'slide tracheoplasty, cricoid involvement requiring '
                                               'cricotracheal resection, poor cartilage or '
                                               'malacia, active inflammatory disease such as GPA, '
                                               'prior radiation, diabetes or steroid use that '
                                               'raises anastomotic risk, or high anastomotic '
                                               'tension all change the plan. Some patients need '
                                               'staged laryngotracheal reconstruction or a '
                                               'long-term tracheostomy.'},
 'v128_lar_09': {'stem': 'A 41-year-old female church cantor has a lifelong rough, breathy voice '
                         'that has worsened with increased singing. Office laryngoscopy under '
                         'continuous light looked nearly normal. Stroboscopy shows a 5-mm segment '
                         'of the left mid-membranous fold with an absent mucosal wave and '
                         'tethering of the cover, plus a small spindle gap. She has no history of '
                         'surgery or intubation. What diagnosis should be considered?',
                 'choices': ['Vocal fold scar or sulcus vocalis',
                             'Primary muscle tension dysphonia',
                             'Superior laryngeal nerve paresis',
                             'Small subepithelial vocal fold cyst'],
                 'answer': 0,
                 'explanation': 'Scar and sulcus disrupt the superficial lamina propria, replacing '
                                'the gel-like layer with stiff collagen or tethering the '
                                'epithelium to the ligament. Under continuous light the edge can '
                                'look nearly normal, but stroboscopy reveals the defining finding: '
                                'a segment where the mucosal wave is absent and the cover is '
                                'tethered. A lifelong rough, breathy voice without surgery '
                                'suggests congenital sulcus, possibly from a ruptured epidermoid '
                                'cyst. A spindle gap often adds glottic insufficiency.',
                 'why_wrong': ['Correct.',
                               'Primary muscle tension dysphonia has a normal mucosal wave, so a '
                               'focal adynamic segment points to a structural cover lesion.',
                               'Superior laryngeal nerve paresis affects pitch control and glottic '
                               'tilt, not focal tethering of the mucosal cover.',
                               'A cyst usually shows a rounded bulge with focal wave reduction '
                               'rather than a flat tethered segment.'],
                 'board_pearl': 'Near-normal edge but a focal adynamic segment on stroboscopy: '
                                'think scar or sulcus.',
                 'curveball': 'Why are surgical outcomes for vocal fold scar less predictable than '
                              'for a simple polyp?',
                 'curveball_answer': 'A polyp is added tissue on top of a normal cover, so '
                                     'removing it restores normal vibration. Scar and sulcus are '
                                     'loss or replacement of the superficial lamina propria '
                                     'itself, and no technique reliably regenerates it. Surgery '
                                     'that elevates or grafts the cover can also create new scar, '
                                     'so outcomes vary and normal vibration is rarely restored.'},
 'v145_lar_14': {'stem': 'A 37-year-old male high school drama teacher has chronic breathy '
                         'dysphonia and vocal fatigue. Stroboscopy shows bilateral linear furrows '
                         'along the medial edges of both mid-membranous folds with a '
                         'spindle-shaped gap and a reduced mucosal wave. He completed voice '
                         'therapy with improved fatigue but no change in quality. He asks why his '
                         'problem is so hard to fix. What is the best explanation?',
                 'choices': ['The furrows reflect weak nerve input that an injection can restore '
                             'over time',
                             'The gap comes from atrophied muscle that strength training can '
                             'rebuild',
                             'The sulcus stiffens the vibratory cover, which closure alone cannot '
                             'restore',
                             'The sulcus is an active inflammatory process that needs steroids to '
                             'settle'],
                 'answer': 2,
                 'explanation': 'Sulcus vergeture is a loss of superficial lamina propria along '
                                'the fold, with epithelium adherent to the ligament. That causes '
                                'two problems: stiffness of the vibratory cover and a spindle gap '
                                'from bowed edges. Injection or medialization can close the gap '
                                'and reduce breathiness and effort, but the pliable cover that '
                                'produces a normal mucosal wave cannot be reliably restored. That '
                                'is why therapy and augmentation help effort but not quality.',
                 'why_wrong': ['His folds move normally; the problem is the structure of the '
                               'cover, not neural input to the muscles.',
                               'Muscle strength does not change the stiff lamina propria, which is '
                               'why therapy helped fatigue but not quality.',
                               'Correct.',
                               'Sulcus is a structural defect rather than active inflammation and '
                               'does not respond to steroids.'],
                 'board_pearl': 'Scar and sulcus combine a stiff cover with a gap; closure can be '
                                'improved, but vibration is hard to restore.',
                 'curveball': 'He sings in a band and asks what to expect before scar-directed '
                              'surgery. How would you counsel him?',
                 'curveball_answer': 'Explain that procedures such as sulcus excision, slicing, or '
                                     'lamina propria grafting can improve some features but '
                                     'outcomes vary, recovery is long, and voice may worsen. '
                                     'Augmentation improves loudness and effort more predictably. '
                                     'Set goals around projection and endurance rather than a '
                                     'normal singing voice, and continue therapy before and after '
                                     'any surgery.'},
 'v252_lar_sulcus_app': {'stem': 'A 44-year-old female pastor has a rough, breathy voice and '
                                 'fatigue from a right mid-membranous scar after prior polyp '
                                 'stripping elsewhere. Stroboscopy shows an adynamic segment with '
                                 'reduced wave and a persistent glottic gap. Twelve weeks of voice '
                                 'therapy improved technique but not her projection. She asks '
                                 'about an operation to remove the scar. What is most useful '
                                 'before considering scar-directed surgery?',
                         'choices': ['Excise the scarred cover down to the vocal ligament',
                                     'Trial injection augmentation to close the glottic gap',
                                     'Intralesional steroid injection followed by more therapy',
                                     'Medialization thyroplasty with a permanent implant'],
                         'answer': 1,
                         'explanation': 'Scar combines two problems: stiffness of the cover and '
                                        'glottic insufficiency. Temporary injection augmentation '
                                        'closes the gap and shows how much of her disability comes '
                                        'from incomplete closure, even though it does not restore '
                                        'the stiff superficial lamina propria. If projection and '
                                        'effort improve, repeated or durable medialization may be '
                                        'enough, sparing her a less predictable scar operation. If '
                                        'benefit is small, the stiffness itself is the main '
                                        'problem and further options can be discussed.',
                         'why_wrong': ['Excising the scar removes more lamina propria and often '
                                       'worsens stiffness rather than restoring pliability.',
                                       'Correct.',
                                       'Steroid injection may soften some early scar, but it does '
                                       'not address the persistent gap limiting her projection.',
                                       'A permanent implant may become appropriate later, but a '
                                       'temporary trial first tests whether closure helps her.'],
                         'board_pearl': 'For scar with a gap, a temporary injection tests how much '
                                        'closure alone will help.',
                         'curveball': 'If augmentation improves loudness but roughness persists, '
                                      'what does that teach you about her remaining vibratory '
                                      'limitation?',
                         'curveball_answer': 'It shows that her gap was causing breathiness and '
                                             'effort, while the remaining roughness comes from the '
                                             'stiff, irregularly vibrating cover. Closure-directed '
                                             'procedures have done what they can, and further '
                                             'gains would require scar-directed techniques with '
                                             'uncertain results. Counsel her that persistent '
                                             'roughness reflects the lamina propria injury rather '
                                             'than a failed injection.'},
 'v252_lar_sulcus_snr': {'stem': 'A 33-year-old female professional jazz singer has longstanding '
                                 'bilateral sulcus vocalis. Voice therapy and a trial injection '
                                 'augmentation improved her effort and projection but not the '
                                 'focal stiffness, and she still cannot sing softly in her upper '
                                 'range. She asks for an operation that will reliably restore a '
                                 'normal mucosal wave so she can return to full performance. What '
                                 'is the best counseling principle?',
                         'choices': ['Recommend sulcus excision, which reliably restores the '
                                     'mucosal wave',
                                     'Advise that no procedure can improve her voice and she '
                                     'should stop singing',
                                     'Offer bilateral medialization thyroplasty to restore her '
                                     'mucosal wave',
                                     'Explain variable results and individualize options without '
                                     'promising'],
                         'answer': 3,
                         'explanation': 'No operation reliably restores normal vibration in sulcus '
                                        'or scar. Scar-directed techniques such as sulcus '
                                        'excision, mucosal slicing, or fat and fascia grafting '
                                        'into the lamina propria can improve some patients, but '
                                        'manipulating the cover can also worsen stiffness. Her '
                                        'care should be individualized among continued '
                                        'rehabilitation, repeated or durable augmentation, and '
                                        'selected scar-directed surgery at an experienced center, '
                                        'with explicit discussion of goals, risk tolerance, and '
                                        'uncertain results for a professional singer.',
                         'why_wrong': ['Sulcus excision can help some patients, but results vary '
                                       'and it can worsen stiffness, so it is not reliable.',
                                       'Augmentation already helped her, and selected scar '
                                       'procedures may help further, so stating that nothing helps '
                                       'is inaccurate.',
                                       'Medialization improves closure but does not restore the '
                                       'stiff cover or produce a normal mucosal wave.',
                                       'Correct.'],
                         'board_pearl': 'Sulcus and scar surgery have variable outcomes; avoid '
                                        'promising normal vibration.',
                         'curveball': 'Her left fold is normal and closure is already excellent '
                                      'after augmentation. How does that change your willingness '
                                      'to operate on the right?',
                         'curveball_answer': 'With a normal contralateral fold and good closure, '
                                             'much of her function already comes from the healthy '
                                             'side. Operating on the scarred fold risks making it '
                                             'stiffer and creating asymmetry for a modest possible '
                                             'gain. That raises the bar for surgery; continued '
                                             'therapy and periodic augmentation may be the better '
                                             'choice unless she accepts the risk.'},
 'v128_lar_10': {'stem': 'A 17-year-old female rower has episodes of noisy inspiration and throat '
                         'tightness during races that peak at maximal effort and resolve within 5 '
                         'minutes of stopping. Albuterol before races has not helped, and resting '
                         'spirometry and methacholine challenge are normal. Laryngoscopy during a '
                         'rowing machine test shows the folds moving toward the midline on '
                         'inspiration. What is the best diagnosis?',
                 'choices': ['Exercise-induced bronchoconstriction',
                             'Bilateral abductor vocal fold paresis',
                             'Exercise-induced laryngeal obstruction',
                             'Supraglottic collapse from laryngomalacia'],
                 'answer': 2,
                 'explanation': 'Inducible laryngeal obstruction is inappropriate adduction of the '
                                'glottis or supraglottis during inspiration, triggered by '
                                'exercise, irritants, or stress. Symptoms peak at maximal effort, '
                                'cause inspiratory noise and throat tightness, and resolve quickly '
                                'after stopping, unlike asthma, which peaks after exercise and '
                                'responds to bronchodilators. Normal spirometry and methacholine '
                                'challenge and failure of albuterol support the diagnosis, but the '
                                'decisive clue is direct observation of inspiratory adduction '
                                'during a provoked episode.',
                 'why_wrong': ['Bronchoconstriction usually peaks after exercise, causes '
                               'expiratory wheeze, and responds to albuterol, none of which fit '
                               'her pattern.',
                               'Paresis causes persistent abduction limits at rest, not episodic '
                               'adduction only during exertion with normal motion between '
                               'episodes.',
                               'Correct.',
                               'Her laryngoscopy shows the true folds moving to midline rather '
                               'than supraglottic tissue prolapsing into the inlet.'],
                 'board_pearl': 'Inspiratory stridor at peak exertion that stops quickly, with no '
                                'response to albuterol: think exercise ILO.',
                 'curveball': 'What treatment is first-line, and when is continuous laryngoscopy '
                              'during exercise most useful?',
                 'curveball_answer': 'First-line treatment is education plus respiratory '
                                     'retraining with a speech-language pathologist, including '
                                     'relaxed-throat breathing, rescue-breathing techniques, and '
                                     'biofeedback. Continuous laryngoscopy during exercise is most '
                                     'useful when the diagnosis is uncertain, asthma and ILO may '
                                     'coexist, symptoms occur only at high exertion, or therapy '
                                     'fails and supraglottic collapse is suspected.'},
 'v135_lary_02': {'stem': 'A 20-year-old male college soccer player has throat tightness and loud '
                          'inspiratory noise during sprints for a year, with three emergency '
                          'visits where he was treated for asthma. Spirometry, methacholine '
                          'challenge, and chest radiograph are normal. Continuous laryngoscopy '
                          'during exercise shows inspiratory adduction of the true folds with a '
                          'posterior chink, and the supraglottis remains open. What is the '
                          'first-line management?',
                  'choices': ['Laryngeal control therapy with rescue breathing training',
                              'Inhaled corticosteroid and long-acting bronchodilator',
                              'Endoscopic supraglottoplasty of the aryepiglottic folds',
                              'Botulinum toxin to the thyroarytenoid muscles'],
                  'answer': 0,
                  'explanation': 'Exercise-induced inducible laryngeal obstruction at the glottic '
                                 'level is functional, trigger-associated closure. First-line '
                                 'treatment is education and laryngeal control therapy with a '
                                 'speech-language pathologist, teaching relaxed-throat and '
                                 'rescue-breathing techniques such as nasal inhalation, pursed-lip '
                                 'exhalation, and abdominal breathing that release the laryngeal '
                                 'squeeze. Treating comorbid contributors such as rhinitis or '
                                 'reflux helps when relevant. Most athletes improve, and '
                                 'confirming the diagnosis lets them stop unnecessary asthma '
                                 'medication.',
                  'why_wrong': ['Correct.',
                                'His testing excludes asthma, so escalating inhaled therapy adds '
                                'side effects without treating the laryngeal closure.',
                                'Supraglottoplasty is for refractory supraglottic collapse, while '
                                'his supraglottis stays open and the problem is glottic.',
                                'Toxin is reserved for rare refractory cases and is not '
                                'appropriate before laryngeal control therapy.'],
                  'board_pearl': 'ILO: education and respiratory retraining first; stop needless '
                                 'asthma escalation once confirmed.',
                  'curveball': 'Why can a normal office laryngoscopy fail to exclude '
                               'exercise-induced ILO?',
                  'curveball_answer': 'ILO is dynamic and occurs only when the trigger is present, '
                                      'so the larynx is normal at rest and during simple office '
                                      'tasks. Exercise-induced obstruction may appear only at '
                                      'near-maximal ventilation, which cannot be reproduced while '
                                      'sitting. Continuous laryngoscopy during exercise or a '
                                      'provocation test that reproduces symptoms is needed to '
                                      'observe the obstruction.'},
 'v252_lar_ilo_app': {'stem': 'A 21-year-old female collegiate middle-distance runner has '
                              'reproducible inspiratory stridor only during the final lap of '
                              'races. Her asthma therapy has been escalated twice to high-dose '
                              'inhaled steroid and a long-acting bronchodilator without benefit. '
                              'Baseline spirometry is normal, and resting laryngoscopy with sniff '
                              'and phonation shows normal fold motion. What is the best next '
                              'diagnostic strategy?',
                      'choices': ['Methacholine challenge to test airway hyperreactivity',
                                  'CT of the neck and chest with contrast to exclude masses',
                                  'Direct laryngoscopy and bronchoscopy under anesthesia',
                                  'Continuous laryngoscopy during treadmill exercise'],
                      'answer': 3,
                      'explanation': 'Inducible laryngeal obstruction is dynamic, so the larynx '
                                     'can look entirely normal at rest. Continuous laryngoscopy '
                                     'during exercise, with a scope secured in place while she '
                                     'runs on a treadmill to the point of symptoms, shows whether '
                                     'the obstruction is glottic, supraglottic, or both, and it '
                                     'can document coexisting asthma if she wheezes with an open '
                                     'larynx. Confirming ILO prevents further escalation of asthma '
                                     'therapy and directs her to laryngeal control therapy.',
                      'why_wrong': ['Methacholine testing evaluates asthma but cannot show the '
                                    'laryngeal obstruction that occurs only during peak exercise.',
                                    'Imaging is appropriate if a fixed lesion is suspected, but '
                                    'her normal resting examination and episodic pattern favor '
                                    'dynamic obstruction.',
                                    'Examination under anesthesia removes the trigger and the '
                                    'dynamic behavior needed to make the diagnosis.',
                                    'Correct.'],
                      'board_pearl': 'Larynx normal at rest with exertional stridor: perform '
                                     'continuous laryngoscopy during exercise.',
                      'curveball': 'How do glottic versus supraglottic exercise-induced '
                                   'obstruction patterns affect what you teach the patient?',
                      'curveball_answer': 'Glottic obstruction, with the true folds closing on '
                                          'inspiration, responds well to laryngeal control and '
                                          'rescue-breathing techniques that relax adduction. '
                                          'Supraglottic obstruction, with arytenoid and '
                                          'aryepiglottic tissue prolapsing inward, responds less '
                                          'to breathing techniques. It may need inspiratory muscle '
                                          'training, adjusted pacing, or, if refractory, '
                                          'supraglottoplasty, so teach her what type of '
                                          'obstruction she has.'},
 'v252_lar_ilo_snr': {'stem': 'A 26-year-old woman with laryngoscopy-confirmed inducible laryngeal '
                              'obstruction arrives in the emergency department with loud '
                              'inspiratory noise and throat tightness after exposure to cleaning '
                              'fumes. Saturation is 99% on room air, she can speak in short '
                              'sentences, her chest is clear, and there is no drooling or '
                              'swelling. Prior episodes resolved with coached breathing. What is '
                              'the best approach?',
                      'choices': ['Rapid sequence intubation to secure the airway',
                                  'Coached rescue breathing with close monitoring',
                                  'Nebulized racemic epinephrine and IV steroids',
                                  'Heliox mixture and an urgent ENT airway examination'],
                      'answer': 1,
                      'explanation': 'Most ILO episodes are frightening but self-limited when gas '
                                     'exchange and airway patency remain adequate. With normal '
                                     'saturation, the ability to speak, no swelling or drooling, '
                                     'and a confirmed diagnosis with prior response to coached '
                                     'breathing, the best approach is calm reassurance, removal '
                                     'from the trigger, and rescue-breathing coaching such as '
                                     'sniffing or nasal inhalation and pursed-lip exhalation. '
                                     'Clinicians should watch for signs that this episode is not '
                                     'ILO and avoid unnecessary intubation.',
                      'why_wrong': ['Intubation carries real risk and is unnecessary when '
                                    'oxygenation is normal and she can speak.',
                                    'Correct.',
                                    'Racemic epinephrine and steroids treat airway edema, which '
                                    'she does not have, and do not relax laryngeal closure.',
                                    'Heliox can reduce turbulent flow, but she is oxygenating '
                                    'normally and coached breathing usually ends the episode.'],
                      'board_pearl': 'Acute ILO with normal oxygenation: coach breathing, remove '
                                     'the trigger, and avoid reflexive intubation.',
                      'curveball': 'Which findings would force you to abandon the ILO assumption '
                                   'during this episode?',
                      'curveball_answer': 'Abandon it for falling saturation, rising carbon '
                                          'dioxide, inability to speak, progressive fatigue, '
                                          'stridor persisting during sleep or sedation, drooling '
                                          'or facial and tongue swelling suggesting anaphylaxis, '
                                          'fever with odynophagia suggesting supraglottitis, or a '
                                          'history suggesting foreign body. These require airway '
                                          'evaluation and treatment as true obstruction.'},
 'v138_lar_01': {'stem': 'A 31-year-old female opera singer has 5 days of hoarseness that began '
                         'with a cold. She has mild sore throat and nasal congestion, no fever, '
                         'stridor, dysphagia, or neck mass, and she does not smoke. Her concert is '
                         'in 3 weeks, and she asks for antibiotics and a steroid pack. Flexible '
                         'laryngoscopy shows mildly erythematous, edematous folds with normal '
                         'mobility and no lesion or hemorrhage. What is the best initial approach?',
                 'choices': ['Voice conservation, hydration, and symptomatic care',
                             'Amoxicillin-clavulanate for presumed bacterial laryngitis',
                             'Oral prednisone taper to speed recovery before her concert',
                             'Empiric twice-daily PPI for presumed reflux laryngitis'],
                 'answer': 0,
                 'explanation': 'Most acute laryngitis follows a viral upper respiratory infection '
                                'and resolves within 1 to 3 weeks. Supportive care with voice '
                                'conservation, hydration, humidification, and avoidance of '
                                'irritants is the treatment. The 2018 hoarseness guideline '
                                'recommends against routine antibiotics, steroids, and antireflux '
                                'therapy without a specific indication. Her examination shows no '
                                'hemorrhage or lesion, so there is no reason to cancel. A short '
                                'steroid course is sometimes used for performers at an imminent '
                                'event, but it is not routine.',
                 'why_wrong': ['Correct.',
                               'Viral laryngitis does not respond to antibiotics, and the '
                               'hoarseness guideline recommends against routine use without '
                               'bacterial infection.',
                               'Steroids are not recommended routinely; with weeks before her '
                               'concert, the risks outweigh a small benefit for self-limited '
                               'swelling.',
                               'Her symptoms began with a cold and she has no reflux symptoms, so '
                               'empiric acid suppression is not indicated.'],
                 'board_pearl': 'Acute viral laryngitis: supportive care; avoid routine '
                                'antibiotics, steroids, and antireflux therapy.',
                 'curveball': 'What duration or red-flag history should prompt earlier '
                              'laryngoscopy in a patient with hoarseness?',
                 'curveball_answer': 'The hoarseness guideline advises laryngoscopy when '
                                     'hoarseness fails to resolve or improve within 4 weeks, or '
                                     'sooner if serious disease is suspected. Red flags include '
                                     'smoking or alcohol use, hemoptysis, dysphagia or '
                                     'odynophagia, otalgia, stridor, a neck mass, recent neck '
                                     'surgery or intubation, weight loss, or professional voice '
                                     'needs that cannot wait.'},
 'v145_lar_01': {'stem': 'A 42-year-old male middle school teacher has 10 days of hoarseness '
                         'following a viral upper respiratory infection. His cough is improving, '
                         'and he has no stridor, dysphagia, hemoptysis, neck mass, or smoking '
                         'history. He is speaking all day at school. He asks whether he needs '
                         'antibiotics or a scope. Which management principle is best?',
                 'choices': ['Laryngoscopy today before any treatment is given',
                             'Course of azithromycin for possible bacterial superinfection',
                             'Supportive care, and scope if not improved by 4 weeks',
                             'CT of the neck with contrast to exclude a mass'],
                 'answer': 2,
                 'explanation': 'Hoarseness after a viral infection without red flags is usually '
                                'acute laryngitis that resolves within a few weeks. Supportive '
                                'care, hydration, and reduced voice load are appropriate. The '
                                'hoarseness guideline recommends laryngoscopy when hoarseness does '
                                'not resolve or improve within 4 weeks, or immediately when '
                                'serious disease is suspected, and recommends against routine '
                                'antibiotics and against imaging before visualizing the larynx. '
                                'Without red flags, examination can wait while he improves.',
                 'why_wrong': ['Immediate laryngoscopy is reasonable with red flags or urgent '
                               'voice needs, but it is not required for uncomplicated postviral '
                               'hoarseness at 10 days.',
                               'Antibiotics are not effective for viral laryngitis, and the '
                               'guideline recommends against routine use.',
                               'Correct.',
                               'The guideline recommends against imaging before laryngoscopy, and '
                               'nothing here suggests a mass.'],
                 'board_pearl': 'Hoarseness without red flags: scope if it persists beyond 4 '
                                'weeks; skip routine antibiotics and imaging.',
                 'curveball': 'He returns a week later still hoarse. Which red flags would make '
                              'you visualize his larynx sooner than 4 weeks?',
                 'curveball_answer': 'Visualize sooner if he develops stridor or breathing '
                                     'difficulty, hemoptysis, dysphagia, odynophagia, referred '
                                     'otalgia, weight loss, or a neck mass, or if he has a smoking '
                                     'history, recent neck surgery or intubation, or symptoms that '
                                     'worsen rather than improve. Immunosuppression also lowers '
                                     'the threshold, given the risk of fungal or atypical '
                                     'infection.'},
 'v148_lar_02': {'stem': 'A 49-year-old man with diabetes has 18 hours of rapidly worsening sore '
                         'throat and odynophagia. He is now drooling, has a muffled voice, is '
                         'sitting forward, and has soft inspiratory stridor with suprasternal '
                         'retractions. Temperature is 39.1 C, and saturation is 95% on room air. '
                         'Oropharyngeal examination is unremarkable apart from pooled saliva. What '
                         'is the priority?',
                 'choices': ['Lateral neck radiograph before any airway assessment',
                             'Controlled airway evaluation with ENT and anesthesia',
                             'Supine bedside flexible laryngoscopy in the ED bay',
                             'IV antibiotics and steroids, then laryngoscopy tomorrow'],
                 'answer': 1,
                 'explanation': 'Severe odynophagia, drooling, muffled voice, tripod positioning, '
                                'stridor, and fever with a normal oropharynx point to acute '
                                'supraglottitis, which can obstruct the airway suddenly. This is '
                                'not routine laryngitis. The priority is a controlled setting: '
                                'keep him upright and calm, involve ENT and anesthesia early, and '
                                'perform careful flexible laryngoscopy where awake fiberoptic '
                                'intubation or a surgical airway can proceed immediately. IV '
                                'antibiotics and steroids follow once the airway plan is in place.',
                 'why_wrong': ['Sending him for radiographs delays airway control and risks '
                               'obstruction outside a monitored setting.',
                               'Correct.',
                               'Laying him supine and scoping without airway backup can '
                               'precipitate complete obstruction.',
                               'Medical therapy is needed, but deferring airway assessment in a '
                               'patient with stridor and drooling risks sudden obstruction.'],
                 'board_pearl': 'Drooling, muffled voice, and stridor with a normal oropharynx: '
                                'supraglottitis; plan the airway first.',
                 'curveball': 'What bedside actions can worsen a critically narrowed supraglottic '
                              'airway in this patient?',
                 'curveball_answer': 'Forcing him supine, depressing the tongue aggressively, '
                                     'attempting blind oral examination or nasal instrumentation '
                                     'without airway backup, sedation, agitation from painful '
                                     'procedures, and leaving him unmonitored for imaging can all '
                                     'trigger laryngospasm or complete obstruction. Keep him '
                                     'upright, calm, and monitored, and give oxygen.'},
 'v256_lar_laryngitis_fnd': {'stem': 'A 27-year-old female graduate student has 4 days of '
                                     'hoarseness and mild sore throat after a cold, with a '
                                     'low-grade fever that has resolved. She has no stridor, '
                                     'drooling, dyspnea, dysphagia, or neck swelling, and she is '
                                     'not immunosuppressed. She asks her primary care clinician '
                                     'for an antibiotic because her roommate received one. What is '
                                     'the most appropriate initial management?',
                             'choices': ['Five-day course of amoxicillin for presumed bacterial '
                                         'laryngitis',
                                         'Oral fluconazole for possible candidal laryngitis',
                                         'Urgent laryngoscopy to exclude supraglottitis today',
                                         'Supportive care with reduced voice use and fluids'],
                             'answer': 3,
                             'explanation': 'Acute laryngitis in an immunocompetent adult after an '
                                            'upper respiratory infection is viral or irritative '
                                            'and self-limited, typically resolving within 1 to 3 '
                                            'weeks. Treatment is supportive: voice rest or reduced '
                                            'use, hydration, humidification, and analgesia. '
                                            'Antibiotics do not shorten viral laryngitis and add '
                                            'side effects and resistance. Specific treatment is '
                                            'reserved for signs of airway compromise, bacterial '
                                            'supraglottitis, fungal infection, or other defined '
                                            'causes, none of which she has.',
                             'why_wrong': ['Antibiotics do not help viral laryngitis, and her '
                                           'improving course without red flags does not suggest '
                                           'bacterial infection.',
                                           'Candidal laryngitis occurs with inhaled steroids, '
                                           'immunosuppression, or antibiotics and needs '
                                           'visualization; she has none of these.',
                                           'Supraglottitis causes severe odynophagia, drooling, '
                                           'and muffled voice, not mild hoarseness after a cold.',
                                           'Correct.'],
                             'board_pearl': 'Uncomplicated acute laryngitis is viral; treat '
                                            'supportively and avoid antibiotics.',
                             'curveball': 'Which airway symptoms would convert this from routine '
                                          'outpatient laryngitis into an urgent laryngeal '
                                          'evaluation?',
                             'curveball_answer': 'Stridor, increasing work of breathing, drooling '
                                                 'or inability to swallow saliva, a muffled voice, '
                                                 'severe odynophagia out of proportion to the '
                                                 'throat examination, tripod positioning, or high '
                                                 'fever with toxic appearance suggest '
                                                 'supraglottitis or a deep neck infection. These '
                                                 'require urgent airway assessment in a controlled '
                                                 'setting.'},
 'v256_lar_laryngitis_app': {'stem': 'A 61-year-old man who smokes a pack a day has 7 weeks of '
                                     'hoarseness. His primary care clinician diagnosed chronic '
                                     'laryngitis and prescribed two courses of antibiotics and '
                                     'then omeprazole, without improvement. No one has examined '
                                     'his larynx. He has no stridor or neck mass. He asks for a '
                                     'stronger antibiotic. What is the best next step?',
                             'choices': ['A month of high-dose twice-daily omeprazole',
                                         'Contrast CT of the neck before any laryngoscopy',
                                         'Laryngoscopy to visualize the larynx now',
                                         'Prednisone taper with reassessment in 2 weeks'],
                             'answer': 2,
                             'explanation': 'Hoarseness lasting more than 4 weeks requires '
                                            'laryngoscopy, and his heavy smoking makes '
                                            'visualization urgent rather than optional. The '
                                            'hoarseness guideline recommends against routine '
                                            'antibiotics, steroids, or antireflux therapy before '
                                            'the larynx is examined and against imaging before '
                                            'laryngoscopy. Persistent dysphonia in a smoker may be '
                                            'leukoplakia, dysplasia, or carcinoma, and each month '
                                            'of empiric treatment delays diagnosis. Stroboscopy or '
                                            'biopsy follows according to what laryngoscopy shows.',
                             'why_wrong': ['More reflux therapy without examination delays '
                                           'diagnosis of possible cancer in a smoker with '
                                           'persistent hoarseness.',
                                           'The guideline recommends against imaging before '
                                           'laryngoscopy; imaging is chosen after the larynx is '
                                           'seen.',
                                           'Correct.',
                                           'Steroids may mask disease and are not recommended '
                                           'without a diagnosis based on visualization.'],
                             'board_pearl': 'Hoarseness over 4 weeks, especially in a smoker: '
                                            'perform laryngoscopy before any empiric therapy.',
                             'curveball': 'What endoscopic features would lower your threshold for '
                                          'direct laryngoscopy and biopsy rather than another '
                                          'medical trial?',
                             'curveball_answer': 'Leukoplakia, erythroplakia, an exophytic or '
                                                 'ulcerated lesion, an irregular surface, reduced '
                                                 'fold mobility, stiffness or absent wave on '
                                                 'stroboscopy, or asymmetry in a smoker all '
                                                 'warrant microlaryngoscopy with biopsy. These '
                                                 'suggest dysplasia or carcinoma, which empiric '
                                                 'medical therapy will not treat.'},
 'v256_lar_laryngitis_snr': {'stem': 'A 66-year-old man has been treated for 4 months for presumed '
                                     'chronic laryngopharyngitis with PPIs and voice hygiene. He '
                                     'now reports right-sided throat pain radiating to the right '
                                     'ear, progressive odynophagia, blood-streaked sputum, and 6 '
                                     'kg weight loss. He smoked for 40 years. Flexible examination '
                                     'shows an irregular, friable lesion on the right '
                                     'aryepiglottic fold. What is the best next step?',
                             'choices': ['Neck imaging with operative biopsy and airway planning',
                                         'Double the PPI dose and reexamine in 8 weeks',
                                         'Course of antibiotics for presumed supraglottic abscess',
                                         'Office biopsy only, deferring imaging until pathology'],
                             'answer': 0,
                             'explanation': 'Unilateral throat pain with referred otalgia, '
                                            'progressive odynophagia, hemoptysis, weight loss, and '
                                            'an irregular friable supraglottic lesion in a '
                                            'long-term smoker indicate probable supraglottic '
                                            'carcinoma. The earlier inflammatory label must be '
                                            'dropped. Contrast CT or MRI of the neck, ideally '
                                            'before biopsy so swelling does not distort staging, '
                                            'followed by direct laryngoscopy with biopsy, defines '
                                            'the extent. Airway planning comes first if the lesion '
                                            'narrows the inlet, and chest imaging completes '
                                            'staging.',
                             'why_wrong': ['Correct.',
                                           'More acid suppression ignores red flags and an '
                                           'irregular lesion, delaying cancer diagnosis.',
                                           'An abscess would be fluctuant with fever rather than '
                                           'an irregular friable lesion with weight loss in a '
                                           'smoker.',
                                           'Office biopsy may be used, but imaging is best '
                                           'obtained before biopsy changes the tissue, and staging '
                                           'needs it anyway.'],
                             'board_pearl': 'When the phenotype changes to unilateral pain, '
                                            'otalgia, hemoptysis, and a lesion, abandon the '
                                            'laryngitis label.',
                             'curveball': 'He now has stridor at rest and saturation of 91%. How '
                                          'does impending airway compromise change the sequence?',
                             'curveball_answer': 'The airway now comes first. Secure it in the '
                                                 'operating room with anesthesia, using awake '
                                                 'tracheostomy under local anesthesia or awake '
                                                 'fiberoptic intubation if a tube will pass, and '
                                                 'obtain biopsies at the same procedure. Imaging '
                                                 'may follow once the airway is safe. Avoid '
                                                 'emergency transoral debulking without a backup '
                                                 'airway.'},
 'v138_lar_02': {'stem': 'A 55-year-old man has persistent breathy dysphonia and coughing with '
                         'liquids 18 months after left jugular foramen tumor resection. EMG shows '
                         'no reinnervation. Stroboscopy shows a lateralized left fold sitting '
                         'higher than the right with a wide posterior glottic gap. A prior '
                         'medialization thyroplasty narrowed only the anterior gap. Which adjunct '
                         'procedure best closes the posterior gap and corrects the height '
                         'mismatch?',
                 'choices': ['Revision thyroplasty with a larger implant',
                             'Injection augmentation of the vocal process',
                             'Ansa cervicalis to vagus nerve reinnervation',
                             'Arytenoid adduction'],
                 'answer': 3,
                 'explanation': 'High vagal injury paralyzes the cricothyroid and all intrinsic '
                                'adductors, so the arytenoid rotates laterally and the vocal '
                                'process sits high, leaving a wide posterior gap and a level '
                                'mismatch. Medialization thyroplasty pushes the membranous fold '
                                'medially but cannot rotate the arytenoid. Arytenoid adduction '
                                'places a suture through the muscular process and pulls it '
                                'anteriorly, mimicking the lateral cricoarytenoid, to rotate the '
                                'vocal process medially and down. It is often combined with '
                                'thyroplasty.',
                 'why_wrong': ['A larger implant pushes the membranous fold further but does not '
                               'rotate the arytenoid to close the posterior gap or level it.',
                               'Injection near the vocal process adds bulk anteriorly but cannot '
                               'correct arytenoid rotation and height in a wide posterior gap.',
                               'Reinnervation restores tone over months but does not correct the '
                               'rotated, elevated arytenoid that is causing the posterior gap.',
                               'Correct.'],
                 'board_pearl': 'Large posterior gap or height mismatch in paralysis: add '
                                'arytenoid adduction to medialization.',
                 'curveball': 'A 30-year-old with recent RLN injury but good bulk asks about '
                              'reinnervation. When is ansa-to-RLN reinnervation especially '
                              'attractive?',
                 'curveball_answer': 'Reinnervation suits younger patients with permanent '
                                     'recurrent nerve injury, a viable ansa donor, and a goal of '
                                     'durable tone and bulk rather than an implant. It works best '
                                     'within about 2 years of injury, before muscle and motor '
                                     'endplates degenerate. Results develop over months, so '
                                     'temporary injection bridges the gap.'},
 'v145_lar_02': {'stem': 'A 62-year-old woman has breathy dysphonia and choking on liquids 14 '
                         'months after left pneumonectomy with mediastinal dissection. EMG shows '
                         'denervation without recovery. Stroboscopy shows the left fold with good '
                         'bulk but a large posterior glottic gap, and the left vocal process sits '
                         'higher than the right. Which procedure specifically corrects this '
                         'glottic geometry?',
                 'choices': ['Bilateral injection augmentation',
                             'Arytenoid adduction',
                             'Type III thyroplasty to shorten the fold',
                             'Cricothyroid approximation'],
                 'answer': 1,
                 'explanation': 'With adequate bulk but a large posterior gap and vertical '
                                'mismatch, the problem is arytenoid position rather than fold '
                                'volume. Arytenoid adduction rotates the arytenoid on the cricoid '
                                'by a suture through the muscular process, moving the vocal '
                                'process medially and down to close the posterior glottis and '
                                'align the folds. It is usually combined with medialization '
                                'thyroplasty. Reinnervation may add long-term tone in selected '
                                'younger patients but does not correct this geometry.',
                 'why_wrong': ['Injecting both folds adds bulk but the problem is unilateral '
                               'arytenoid rotation, and the healthy fold does not need '
                               'augmentation.',
                               'Correct.',
                               'Type III thyroplasty shortens and relaxes the fold to lower pitch '
                               'and does not close a posterior gap.',
                               'Cricothyroid approximation, type IV, raises pitch by lengthening '
                               'the fold and does not rotate the arytenoid.'],
                 'board_pearl': 'Arytenoid adduction rotates the vocal process medially and down; '
                                'medialization alone cannot.',
                 'curveball': 'A 34-year-old with a recent stable RLN injury and good health asks '
                              'about reinnervation instead. When might it be favored?',
                 'curveball_answer': 'Reinnervation is favored in younger patients with a '
                                     'permanent but recent injury, usually within 2 years, a '
                                     'healthy ansa donor, and a wish to avoid implants. It '
                                     'restores tone and bulk and may improve vertical position, '
                                     'but it does not produce purposeful movement. Benefit appears '
                                     'over 3 to 6 months, so temporary injection is used '
                                     'meanwhile.'},
 'v255_lar_aa_reinn_fnd': {'stem': 'A 57-year-old man undergoes left medialization thyroplasty '
                                   'under local anesthesia for paralysis 2 years after vagal '
                                   'paraganglioma resection. With the implant in place, the '
                                   'anterior fold looks well medialized, but his voice remains '
                                   'breathy and flexible laryngoscopy shows a persistent posterior '
                                   'chink with the left vocal process higher than the right. Which '
                                   'additional step most directly addresses the remaining problem?',
                           'choices': ['Add arytenoid adduction through the same incision',
                                       'Replace the implant with a thicker one to push harder',
                                       'Inject fat into the posterior paraglottic space',
                                       'Place a second implant along the thyroid cartilage'],
                           'answer': 0,
                           'explanation': 'Real-time voice and endoscopic feedback under local '
                                          'anesthesia shows that medialization has closed the '
                                          'anterior gap, but a persistent posterior chink with an '
                                          'elevated vocal process means the arytenoid remains '
                                          'laterally rotated. Arytenoid adduction, using the same '
                                          'incision, places a suture through the muscular process '
                                          'and pulls it anteriorly to rotate the vocal process '
                                          'medially and down. That closes the posterior gap and '
                                          'corrects the height mismatch, which a thicker implant '
                                          'cannot do.',
                           'why_wrong': ['Correct.',
                                         'A thicker implant overmedializes the anterior fold and '
                                         'can narrow the airway while still not rotating the '
                                         'arytenoid.',
                                         'Posterior fat injection can add some posterior bulk but '
                                         'does not reliably rotate or level a high vocal process.',
                                         'A second implant along the same cartilage still '
                                         'medializes only the membranous fold, not the arytenoid.'],
                           'board_pearl': 'Persistent posterior chink and a high vocal process '
                                          'after thyroplasty call for arytenoid adduction.',
                           'curveball': 'What intraoperative finding would suggest that '
                                        'medialization alone has not corrected the relevant '
                                        'glottic geometry?',
                           'curveball_answer': 'A persistent posterior gap, a vocal process '
                                               'sitting above the other side, a voice that '
                                               'improves with manual rotation of the arytenoid or '
                                               'lateral pressure on the thyroid ala posteriorly '
                                               'but not with a larger implant, or short phonation '
                                               'time despite good anterior closure all indicate '
                                               'that arytenoid adduction is needed.'},
 'v255_lar_aa_reinn_app': {'stem': 'A 29-year-old female kindergarten teacher has permanent left '
                                   'recurrent laryngeal nerve paralysis 4 months after '
                                   'thyroidectomy, with the nerve divided and not repaired. She is '
                                   'healthy, has a moderate glottic gap with good fold position, '
                                   'and wants a durable solution without an implant. She asks what '
                                   'ansa cervicalis to RLN reinnervation will do. Which statement '
                                   'is most accurate?',
                           'choices': ['It restores coordinated abduction and adduction in weeks',
                                       'It enlarges the glottic airway for bilateral paralysis',
                                       'It restores tone over months but not purposeful motion',
                                       'It improves voice within days of the operation'],
                           'answer': 2,
                           'explanation': 'Ansa cervicalis to recurrent laryngeal nerve '
                                          'reinnervation supplies new motor input to the '
                                          'denervated laryngeal muscles. Over 3 to 6 months it '
                                          'restores thyroarytenoid tone and bulk and improves fold '
                                          'position, giving durable voice benefit that often '
                                          'improves with time, particularly in younger patients. '
                                          'It does not restore purposeful abduction or normal '
                                          'coordinated mobility because the ansa does not carry '
                                          'coordinated laryngeal motor signals. Temporary '
                                          'injection augmentation is often used to bridge the '
                                          'delay.',
                           'why_wrong': ['The ansa is not a laryngeal motor nerve, so coordinated '
                                         'movement does not return, and improvement takes months.',
                                         'Ansa reinnervation of a unilateral paralysis improves '
                                         'closure; it is not an airway-widening operation for '
                                         'bilateral disease.',
                                         'Correct.',
                                         'Benefit appears only after axons regrow over months, '
                                         'which is why a temporary injection is often added.'],
                           'board_pearl': 'Ansa-to-RLN reinnervation restores tone and bulk over '
                                          'months, not purposeful movement.',
                           'curveball': 'She also has thin-liquid aspiration. How would the need '
                                        'for immediate aspiration control influence whether you '
                                        'add temporary injection or framework surgery?',
                           'curveball_answer': 'Reinnervation alone leaves her aspirating for '
                                               'several months. Add a temporary injection '
                                               'augmentation at the same operation to close the '
                                               'gap now, which bridges until reinnervation takes '
                                               'effect without committing her to an implant. '
                                               'Framework surgery is unnecessary unless the gap or '
                                               'level mismatch is too large for injection, or '
                                               'reinnervation fails.'},
 'v255_lar_aa_reinn_snr': {'stem': 'A 32-year-old male chef has severe dysphonia and coughing with '
                                   'liquids 3 years after a high vagal injury from carotid body '
                                   'tumor surgery. EMG shows denervation without recovery. '
                                   'Stroboscopy shows a large posterior gap and the paralyzed fold '
                                   'sitting high. He needs a better voice before reopening his '
                                   'restaurant in 2 months but also values a durable result. What '
                                   'is the best planning principle?',
                           'choices': ['Ansa cervicalis reinnervation alone for the most lasting '
                                       'tone',
                                       'Combine framework procedures with arytenoid adduction',
                                       'Repeated hyaluronic acid injections every 4 months',
                                       'Defer treatment until voice therapy has run 6 months'],
                           'answer': 1,
                           'explanation': 'He has a large posterior gap and height mismatch from '
                                          'high vagal paralysis, and he needs prompt improvement. '
                                          'Medialization thyroplasty with arytenoid adduction '
                                          'corrects fold position, the posterior gap, and level '
                                          'immediately and durably. Reinnervation is less '
                                          'attractive 3 years after injury because muscle and '
                                          'motor endplates have degenerated, and it would not '
                                          'correct the arytenoid geometry or give early benefit. '
                                          'Procedure choice should match glottic geometry, timing, '
                                          'and goals.',
                           'why_wrong': ['Reinnervation acts over months and is less effective '
                                         'years after injury, and it does not correct his height '
                                         'mismatch.',
                                         'Correct.',
                                         'Injections add bulk temporarily but cannot correct a '
                                         'large posterior gap or level mismatch, and they need '
                                         'repeated treatment.',
                                         'Therapy cannot close a large posterior gap from '
                                         'permanent paralysis and would delay effective '
                                         'treatment.'],
                           'board_pearl': 'Match the procedure to the gap: arytenoid adduction for '
                                          'posterior gaps and level mismatch; reinnervation for '
                                          'early tone.',
                           'curveball': 'How would advanced age, poor donor nerve quality, or a '
                                        'small anterior gap change the value of reinnervation '
                                        'versus framework surgery?',
                           'curveball_answer': 'Advanced age reduces reinnervation results, and a '
                                               'poor or sacrificed ansa removes the donor, so '
                                               'framework surgery becomes the better choice. A '
                                               'small anterior gap with good position may need '
                                               'only injection or thyroplasty, and reinnervation '
                                               'adds little. Reinnervation is most valuable in '
                                               'younger patients within about 2 years of injury.'},
 'v138_lar_03': {'stem': 'A 46-year-old woman has been in a minimally conscious state for 2 years '
                         'after an anoxic brain injury. She has a tracheostomy and gastrostomy but '
                         'has had six aspiration pneumonias in a year from continuous salivary '
                         'aspiration despite suctioning, cuffed tubes, and anticholinergics. Her '
                         'neurologists do not expect laryngeal recovery. Her family asks what '
                         'surgery would accomplish. What is the goal of aspiration-prevention '
                         'surgery?',
                 'choices': ['Improve glottic closure so she can safely resume eating',
                             'Reduce saliva production so the airway can stay unchanged',
                             'Allow decannulation by restoring laryngeal protective reflexes',
                             'Separate the airway from the pharynx to protect the lungs'],
                 'answer': 3,
                 'explanation': 'When aspiration of secretions is intractable and laryngeal '
                                'function will not recover, operations such as laryngotracheal '
                                'separation, tracheoesophageal diversion, glottic closure, or '
                                'narrow-field laryngectomy separate the trachea from the pharynx '
                                'so saliva and refluxate cannot enter the lungs. The goal is '
                                'pulmonary protection and fewer pneumonias, not restored '
                                'swallowing. These procedures sacrifice or alter laryngeal voice, '
                                'which matters less here, and some separation procedures can be '
                                'reversed if function returns.',
                 'why_wrong': ['Medialization improves glottic closure for unilateral '
                               'insufficiency, but it cannot overcome global failure of airway '
                               'protection.',
                               'Salivary reduction with botulinum toxin or duct procedures can '
                               'help, but she already failed medical measures and the goal of '
                               'surgery is separation.',
                               'Separation procedures leave a permanent tracheostoma rather than '
                               'allowing decannulation through the larynx.',
                               'Correct.'],
                 'board_pearl': 'Aspiration-prevention surgery separates airway from pharynx; it '
                                'protects the lungs at the cost of laryngeal voice.',
                 'curveball': 'What communication counseling is required before an '
                              'airway-separating operation in a patient who can still speak?',
                 'curveball_answer': 'Explain that after separation the patient cannot phonate '
                                     'through the larynx, so normal voice is lost. Discuss '
                                     'alternatives such as writing, communication boards, '
                                     'electrolarynx, and augmentative devices, and in some '
                                     'separations or laryngectomies, tracheoesophageal puncture '
                                     'for voice. If reversal is possible, explain how voice could '
                                     'return, but do not promise recovery.'},
 'v145_lar_03': {'stem': 'A 67-year-old man with ALS has recurrent life-threatening aspiration '
                         'pneumonia from salivary and refluxed secretions despite gastrostomy '
                         'feeding, a cuffed tracheostomy, and salivary gland botulinum toxin. He '
                         'communicates with an eye-gaze device and no longer has useful laryngeal '
                         'voice. He still wishes to taste small amounts of food. What is the goal '
                         'of aspiration-prevention surgery for him?',
                 'choices': ['Restore safe swallowing so he can resume a full oral diet',
                             'Reduce reflux of gastric contents into the pharynx',
                             'Isolate the lungs from aspirated material at the cost of voice',
                             'Strengthen cough by medializing both vocal folds'],
                 'answer': 2,
                 'explanation': 'Laryngotracheal separation, glottic closure, or narrow-field '
                                'laryngectomy divides the airway from the digestive tract so '
                                'secretions and refluxate cannot reach the lungs, reducing '
                                'pneumonia and suctioning burden. He has already lost useful '
                                'laryngeal voice, so the voice trade-off matters less. Surgery '
                                'protects the lungs rather than restoring swallowing, but it can '
                                'allow taste-for-pleasure oral intake because aspiration is no '
                                'longer possible.',
                 'why_wrong': ['Separation removes the risk of aspiration but does not restore '
                               'swallowing strength in progressive ALS.',
                               'Antireflux measures do not address salivary aspiration and do not '
                               'protect the lungs from all aspirated material.',
                               'Correct.',
                               'Medializing both folds would compromise his airway and does not '
                               'solve global failure of airway protection in ALS.'],
                 'board_pearl': 'Separation surgery protects the lungs; it does not fix the '
                                'swallow but can permit pleasure feeding.',
                 'curveball': 'How does his preserved desire for oral intake influence counseling, '
                              'even if aspiration is eliminated?',
                 'curveball_answer': 'After separation he can take small amounts of food for '
                                     'pleasure because nothing can enter the lungs, which is often '
                                     'valued. But his pharyngeal weakness still limits bolus '
                                     'transit, so intake will be small and nutrition remains '
                                     'through the gastrostomy. Set expectations about taste, '
                                     'residue, and regurgitation, and involve speech pathology in '
                                     'planning.'},
 'v148_lar_03': {'stem': 'A 72-year-old man with severe aspiration after a brainstem stroke, '
                         'managed with a gastrostomy, is found by his nurse coughing and hypoxic '
                         'at 82% after vomiting tube feeds. He has diffuse crackles and tachypnea. '
                         'His family had been discussing aspiration-prevention surgery with the '
                         'ENT team last week. What is the immediate priority?',
                 'choices': ['Oxygenation, airway suctioning, and pulmonary assessment',
                             'Urgent laryngotracheal separation to prevent recurrence',
                             'Immediate broad-spectrum antibiotics before oxygen therapy',
                             'Restart tube feeds at a lower rate to maintain nutrition'],
                 'answer': 0,
                 'explanation': 'A large aspiration with hypoxemia is a respiratory emergency. '
                                'Support oxygenation and ventilation, suction the airway, stop the '
                                'tube feeds, position him upright, and assess for pneumonitis or '
                                'pneumonia with examination and imaging. Antibiotics are given for '
                                'clinical pneumonia or high-risk features rather than routinely '
                                'for chemical pneumonitis. Decisions about separation surgery wait '
                                'until he is stable and goals are clarified, because surgery in an '
                                'acutely hypoxic patient adds risk without immediate benefit.',
                 'why_wrong': ['Correct.',
                               'Surgery is a decision for after stabilization and goals '
                               'discussion, not an emergency response to an acute event.',
                               'Antibiotics may be needed, but oxygenation comes first and '
                               'aspiration pneumonitis does not always need antibiotics.',
                               'Restarting feeds during acute aspiration risks further vomiting '
                               'and aspiration before the cause is addressed.'],
                 'board_pearl': 'Acute aspiration with hypoxemia is a respiratory emergency; '
                                'stabilize first, then plan definitive prevention.',
                 'curveball': 'He recovers. What features would make long-term '
                              'aspiration-prevention surgery reasonable afterward?',
                 'curveball_answer': 'Surgery becomes reasonable if aspiration remains severe and '
                                     'recurrent despite maximal conservative care, laryngeal '
                                     'recovery is not expected, pneumonias are clearly aspiration '
                                     'driven, and he or his surrogates value fewer '
                                     'hospitalizations over laryngeal voice. Separation may not '
                                     'help if aspiration is mostly from gastric reflux below the '
                                     'larynx.'},
 'v253_lar_asp_fnd': {'stem': 'The ENT team is asked to see four inpatients about aspiration. '
                              'Patient 1 has trace penetration on one study and no pneumonia. '
                              'Patient 2 is getting a gastrostomy for nutrition after a stroke. '
                              'Patient 3, a 58-year-old man, has had four aspiration pneumonias in '
                              '8 months despite maximal therapy. Patient 4 has dysphonia with '
                              'normal swallowing. Which patient most warrants discussion of '
                              'aspiration-prevention surgery?',
                      'choices': ['Patient 2, because a gastrostomy is about to be placed',
                                  'Patient 1, to prevent progression from early laryngeal '
                                  'penetration',
                                  'Patient 4, to protect the airway before swallowing worsens',
                                  'Patient 3, with intractable aspiration despite maximal care'],
                      'answer': 3,
                      'explanation': 'Aspiration-prevention operations intentionally trade '
                                     'laryngeal voice or normal airway-pharynx continuity for '
                                     'pulmonary safety, so they are reserved for severe, '
                                     'persistent aspiration causing recurrent pulmonary morbidity '
                                     'despite rehabilitation, diet modification, and less '
                                     'destructive measures. Patient 3 has failed maximal therapy '
                                     'with repeated pneumonias, which is the indication. Trace '
                                     'penetration, a feeding tube, or dysphonia without aspiration '
                                     'do not justify such surgery. Reversibility and goals still '
                                     'need discussion.',
                      'why_wrong': ['A gastrostomy addresses nutrition, and a feeding tube alone '
                                    'is not an indication for airway separation.',
                                    'Trace penetration without pneumonia is mild and is managed '
                                    'with therapy and monitoring, not surgery.',
                                    'Dysphonia with normal swallowing involves no aspiration risk '
                                    'that would justify an irreversible airway operation.',
                                    'Correct.'],
                      'board_pearl': 'Aspiration-prevention surgery is for intractable aspiration '
                                     'with recurrent pulmonary harm despite maximal care.',
                      'curveball': "Patient 2's family believes the gastrostomy will stop "
                                   'aspiration pneumonia. Why can a feeding tube fail to do that?',
                      'curveball_answer': 'A feeding tube removes oral food but not the aspiration '
                                          'of saliva, which is produced continuously and contains '
                                          'oral bacteria. Tube feeds can also reflux into the '
                                          'pharynx and be aspirated, especially when supine. That '
                                          'is why pneumonia often continues after gastrostomy in '
                                          'patients with poor airway protection.'},
 'v253_lar_asp_app': {'stem': 'A 64-year-old man treated with chemoradiation for laryngeal '
                              'carcinoma 6 years ago now has a nonfunctional larynx with fixed '
                              'folds, chronic aspiration of secretions, three pneumonias this '
                              'year, and no useful voice. He has a tracheostomy and gastrostomy, '
                              'and there is no tumor recurrence. He is considering laryngotracheal '
                              'separation, glottic closure, or narrow-field laryngectomy. Which '
                              'counseling principle is essential?',
                      'choices': ['Expect normal laryngeal voice after any of these procedures',
                                  'Weigh radiated tissue, fistula risk, and voice options',
                                  'Select the procedure by his Penetration-Aspiration Scale score',
                                  'Treat prior radiation as irrelevant to his wound healing risk'],
                      'answer': 1,
                      'explanation': 'Aspiration-prevention procedures differ in reversibility, '
                                     'fistula and wound risk, reconstructive needs, and '
                                     'communication options. In a heavily radiated larynx, tissue '
                                     'healing is poor, so separation or closure procedures carry '
                                     'high fistula rates, and some surgeons prefer narrow-field '
                                     'laryngectomy, which removes the dysfunctional organ, with '
                                     'vascularized flap reinforcement. Laryngectomy also allows '
                                     'tracheoesophageal puncture for voice. Choice must reflect '
                                     'anatomy, radiation, reversibility, his goals, and '
                                     'reconstruction risk.',
                      'why_wrong': ['These operations prioritize the lungs and usually remove or '
                                    'bypass laryngeal voice, which he has already lost.',
                                    'Correct.',
                                    'The scale grades aspiration severity but does not choose a '
                                    'procedure, which depends on anatomy and goals.',
                                    'Prior radiation markedly increases fistula and wound '
                                    'complications and affects reconstruction planning.'],
                      'board_pearl': 'In a radiated, nonfunctional larynx, choose aspiration '
                                     'surgery around tissue quality, fistula risk, and '
                                     'communication.',
                      'curveball': 'How would heavily radiated tissue influence your '
                                   'reconstruction and fistula-prevention plan?',
                      'curveball_answer': 'Expect poor healing and a high fistula rate, so bring '
                                          'in nonradiated vascularized tissue such as a pectoralis '
                                          'major muscle flap or free flap to reinforce the '
                                          'closure. Optimize nutrition and thyroid function, plan '
                                          'a longer period without oral intake, and favor '
                                          'procedures with fewer suture lines in radiated tissue.'},
 'v253_lar_asp_snr': {'stem': 'A 39-year-old woman with severe cerebral palsy and intellectual '
                              'disability has had five pneumonias in 18 months despite gastrostomy '
                              'feeding, a cuffed tracheostomy, and salivary botulinum toxin. FEES '
                              'shows continuous salivary aspiration, and pH testing shows little '
                              'reflux. Her pulmonary reserve is worsening, and recovery of '
                              'laryngeal protection is not expected. She communicates with '
                              'gestures. What is the best next step?',
                      'choices': ['Confirm aspiration drives pneumonia, then discuss separation',
                                  'Increase the tube feeding rate to improve her nutrition',
                                  'Avoid surgery because neurologic disease is a contraindication',
                                  'Bilateral vocal fold medialization to improve glottic closure'],
                      'answer': 0,
                      'explanation': 'Tube feeding does not prevent salivary aspiration, and her '
                                     'FEES confirms continuous salivary aspiration with little '
                                     'reflux, so aspiration of secretions is the dominant driver. '
                                     'In carefully selected patients with irreversible severe '
                                     'aspiration, laryngotracheal separation substantially reduces '
                                     'pneumonia and suctioning burden. Before surgery, confirm the '
                                     'mechanism, define goals with her caregivers, discuss her '
                                     'limited communication, and weigh pulmonary benefit against '
                                     'irreversible loss of laryngeal function.',
                      'why_wrong': ['Correct.',
                                    'Increasing feeds does not reduce salivary aspiration and may '
                                    'worsen reflux and aspiration of feeds.',
                                    'Neurologic disease is a common indication rather than a '
                                    'contraindication when aspiration is severe and irreversible.',
                                    'Medialization does not fix global failure of airway '
                                    'protection and may narrow an already limited airway.'],
                      'board_pearl': 'Tube feeding does not stop salivary aspiration; separation '
                                     'helps when aspiration is the proven driver.',
                      'curveball': 'What evidence would suggest her pneumonias are not mainly '
                                   'aspiration driven and unlikely to improve after separation?',
                      'curveball_answer': 'Pneumonias that persist despite minimal secretion '
                                          'aspiration on FEES, prominent gastroesophageal reflux '
                                          'below the larynx, poor cough or atelectasis from '
                                          'restrictive lung disease or scoliosis, '
                                          'immunodeficiency, or bronchiectasis suggest other '
                                          'drivers. Separation does not stop aspiration of '
                                          'refluxed material reaching the trachea from below or '
                                          'fix poor pulmonary clearance.'},
 'v138_lar_04': {'stem': 'A 52-year-old female teacher has 14 months of dry cough triggered by '
                         'talking, laughing, cold air, and perfume, preceded by a throat tickle. '
                         'She does not smoke or take an ACE inhibitor. Chest CT, spirometry, '
                         'methacholine challenge, sinus evaluation, and an 8-week PPI trial were '
                         'unrevealing. Laryngoscopy shows no lesion and normal mobility. What '
                         'treatment is most reasonable?',
                 'choices': ['Twice-daily PPI with an alginate for 6 more months',
                             'Inhaled corticosteroid trial for cough-variant asthma',
                             'Behavioral cough suppression therapy with an SLP',
                             'Course of azithromycin for chronic bronchitis'],
                 'answer': 2,
                 'explanation': 'After common causes have been evaluated and treated, a cough '
                                'triggered by talking, temperature, and odors with a throat tickle '
                                'indicates laryngeal hypersensitivity, a neurogenic cough '
                                'syndrome. Behavioral cough suppression therapy with a '
                                'speech-language pathologist teaches recognition of the urge, '
                                'suppression techniques, laryngeal relaxation, and hydration, and '
                                'it has evidence of benefit. Selected patients with persistent '
                                'symptoms may add a neuromodulator such as gabapentin or low-dose '
                                'amitriptyline after discussion of side effects.',
                 'why_wrong': ['She already failed an adequate PPI trial, and more acid '
                               'suppression is unlikely to help a hypersensitivity cough.',
                               'Methacholine challenge was negative, making cough-variant asthma '
                               'unlikely and inhaled steroids unhelpful.',
                               'Correct.',
                               'She has no infection, and antibiotics do not treat a neurogenic '
                               'hypersensitivity cough.'],
                 'board_pearl': 'Refractory cough with triggers and a throat tickle: behavioral '
                                'cough suppression first, neuromodulators selectively.',
                 'curveball': 'What history would make an ACE inhibitor or eosinophilic airway '
                              'disease more likely as the cause?',
                 'curveball_answer': 'ACE inhibitor cough is suggested by a dry cough that began '
                                     'within weeks to months of starting the drug, although it can '
                                     'start later; it resolves within weeks of stopping. '
                                     'Eosinophilic bronchitis is suggested by productive cough, '
                                     'atopy, and sputum eosinophilia with normal spirometry and '
                                     'methacholine testing, and it responds to inhaled steroids.'},
 'v145_lar_04': {'stem': 'A 49-year-old man has a dry cough for 11 months that began after a viral '
                         'illness and is triggered by talking, cold air, and strong odors, with a '
                         'persistent tickle in his throat. He never smoked and takes no ACE '
                         'inhibitor. Chest radiograph, spirometry, sinus CT, and reflux treatment '
                         'were unrevealing, and laryngoscopy is normal. Which treatment concept is '
                         'most appropriate?',
                 'choices': ['Postnasal drip treated with a first-generation antihistamine',
                             'Laryngeal hypersensitivity treated with cough suppression therapy',
                             'Reflux cough treated with a laparoscopic fundoplication',
                             'Psychogenic cough treated with cognitive behavioral therapy'],
                 'answer': 1,
                 'explanation': 'A cough that persists after a viral illness, triggered by '
                                'non-tussive stimuli and accompanied by a throat tickle, despite '
                                'evaluation and treatment of common causes, fits laryngeal '
                                'hypersensitivity. The cough reflex has become sensitized, so mild '
                                'stimuli trigger it. Behavioral cough suppression therapy reduces '
                                'maladaptive coughing, and selected neuromodulators such as '
                                'gabapentin or amitriptyline help some patients. The diagnosis is '
                                'reached after appropriate evaluation, not before.',
                 'why_wrong': ['His sinus evaluation is unrevealing, and an antihistamine trial '
                               'does not address a sensitized cough reflex.',
                               'Correct.',
                               'Fundoplication is not indicated when reflux treatment has failed '
                               'and there is no objective reflux disease.',
                               'The sensory triggers and throat tickle suggest neural '
                               'hypersensitivity, not a primarily psychological cough.'],
                 'board_pearl': 'Post-viral cough triggered by talking, cold air, and odors '
                                'suggests laryngeal hypersensitivity.',
                 'curveball': 'What findings would make you return to a pulmonary or oncologic '
                              'differential instead?',
                 'curveball_answer': 'Return to the structural workup for hemoptysis, weight loss, '
                                     'smoking history, abnormal chest imaging, a new focal '
                                     'laryngeal lesion, progressive dysphagia or hoarseness, fever '
                                     'or night sweats, clubbing, or a change in cough character. '
                                     'These suggest malignancy, infection, interstitial lung '
                                     'disease, or bronchiectasis rather than hypersensitivity.'},
 'v255_lar_cough_fnd': {'stem': 'A 58-year-old female choir member has 2 years of dry cough '
                                'triggered by singing, talking, and cold air, with an '
                                'urge-to-cough sensation in her throat. Evaluation for asthma, '
                                'eosinophilic bronchitis, rhinosinusitis, reflux, and medications '
                                'was negative, and treatment trials failed. Chest CT is normal. '
                                'Laryngoscopy shows no lesion, normal mobility, and mild '
                                'paradoxical adduction during a cough fit. Which concept best '
                                'fits?',
                        'choices': ['Cough-variant asthma with negative challenge testing',
                                    'Habit cough as a primary behavioral disorder',
                                    'Inducible laryngeal obstruction from exercise',
                                    'Chronic refractory cough with laryngeal hypersensitivity'],
                        'answer': 3,
                        'explanation': 'Chronic refractory cough with laryngeal hypersensitivity '
                                       'is a sensory neuropathic phenotype featuring non-tussive '
                                       'triggers such as talking, singing, and temperature, an '
                                       'urge-to-cough sensation, and persistence after appropriate '
                                       'evaluation and treatment of common causes. It may coexist '
                                       'with paradoxical laryngeal motion, as in this patient. The '
                                       'diagnosis is made in context, after reasonable workup and '
                                       'in the absence of red flags. Treatment includes behavioral '
                                       'cough suppression and selected neuromodulators.',
                        'why_wrong': ['Negative methacholine challenge and failure of asthma '
                                      'treatment make cough-variant asthma unlikely.',
                                      'Habit cough lacks a sensory urge and usually stops during '
                                      'sleep and distraction, while she reports a throat urge with '
                                      'triggers.',
                                      'Exercise ILO causes inspiratory stridor at peak exertion, '
                                      'not a chronic cough triggered by talking.',
                                      'Correct.'],
                        'board_pearl': 'Non-tussive triggers and an urge to cough after a negative '
                                       'workup: laryngeal hypersensitivity.',
                        'curveball': 'She returns a year later with a change in symptoms. Which '
                                     'red flags would reopen the structural workup in her case?',
                        'curveball_answer': 'Hemoptysis, weight loss, a new or heavy smoking '
                                            'history, abnormal chest imaging, progressive '
                                            'dysphagia, new hoarseness, a focal laryngeal finding, '
                                            'fever or night sweats, or immunosuppression all '
                                            'reopen the evaluation. These raise concern for '
                                            'cancer, infection, aspiration, or lung disease that a '
                                            'hypersensitivity label would miss.'},
 'v255_lar_cough_app': {'stem': 'A 63-year-old woman has chronic refractory cough with a '
                                'convincing laryngeal hypersensitivity phenotype after a negative '
                                'workup. Six sessions of behavioral cough suppression therapy '
                                'reduced her cough by about a third. She has mild chronic kidney '
                                'disease, takes no sedating drugs, and lives alone. She asks about '
                                'adding medication. Which strategy is appropriate?',
                        'choices': ['Codeine-based cough syrup taken as needed',
                                    'High-dose PPI plus a prokinetic for presumed reflux',
                                    'Low-dose gabapentin titrated slowly, renally dosed',
                                    'Prolonged oral steroid course to calm inflammation'],
                        'answer': 2,
                        'explanation': 'Behavioral cough suppression therapy is the foundation, '
                                       'and neuromodulators such as gabapentin, pregabalin, or '
                                       'low-dose amitriptyline can add benefit when therapy helps '
                                       'only partly. Gabapentin has trial evidence in refractory '
                                       'cough but is renally cleared, so her kidney disease '
                                       'requires a low starting dose and slow titration. Because '
                                       'she lives alone, counsel her about dizziness, sedation, '
                                       'and fall risk, and reassess benefit at a defined point. '
                                       'Continuing therapy alongside medication is appropriate.',
                        'why_wrong': ['Opioids carry dependence and sedation risk and are not a '
                                      'preferred option for long-term refractory cough.',
                                      'Her workup and trials already excluded reflux as a driver, '
                                      'so more acid suppression is unlikely to help.',
                                      'Correct.',
                                      'Laryngeal hypersensitivity is not steroid-responsive '
                                      'inflammation, and prolonged steroids cause significant '
                                      'harm.'],
                        'board_pearl': 'Neuromodulators such as gabapentin help selected '
                                       'refractory cough; adjust for kidney function and fall '
                                       'risk.',
                        'curveball': 'How would sedation risk, fall risk, renal function, or '
                                     'concurrent neuropathic medications affect your choice?',
                        'curveball_answer': 'Reduced renal function lowers gabapentin and '
                                            'pregabalin dosing. High fall risk or sedation '
                                            'concerns favor the lowest effective dose or '
                                            'behavioral therapy alone. Amitriptyline is avoided in '
                                            'older adults with cardiac conduction disease, '
                                            'glaucoma, or urinary retention. Patients already '
                                            'taking a gabapentinoid or other neuropathic drug '
                                            'should not have another added without coordination.'},
 'v255_lar_cough_snr': {'stem': 'A 64-year-old man is referred for neurogenic cough after failing '
                                '3 months of PPI therapy, and he asks for a superior laryngeal '
                                'nerve block. On review he reports new blood-streaked sputum and a '
                                '35 pack-year smoking history, and the prior laryngeal examination '
                                'was a brief mirror view. No chest imaging was done. What is the '
                                'best next step?',
                        'choices': ['Chest CT and complete laryngoscopy first',
                                    'Superior laryngeal nerve block as he requested',
                                    'Start gabapentin and review response in 8 weeks',
                                    'Behavioral cough suppression therapy with an SLP'],
                        'answer': 0,
                        'explanation': 'Chronic refractory cough is diagnosed after appropriate '
                                       'assessment, not after failure of one empiric therapy. '
                                       'Hemoptysis and heavy tobacco exposure are red flags for '
                                       'lung or laryngeal cancer, and he has had neither chest '
                                       'imaging nor adequate laryngoscopy. Chest CT, flexible '
                                       'laryngoscopy with careful examination of the larynx and '
                                       'hypopharynx, and bronchoscopy when indicated must come '
                                       'first. Hypersensitivity-directed therapy is appropriate '
                                       'only once structural disease is excluded.',
                        'why_wrong': ['Correct.',
                                      'A nerve block treats hypersensitivity and is premature when '
                                      'red flags for cancer have not been evaluated.',
                                      'Neuromodulator therapy may mask symptoms while a possible '
                                      'malignancy remains undiagnosed.',
                                      'Behavioral therapy is appropriate for hypersensitivity only '
                                      'after structural disease has been excluded.'],
                        'board_pearl': 'Hemoptysis or heavy smoking history in chronic cough: '
                                       'complete the structural workup before hypersensitivity '
                                       'therapy.',
                        'curveball': 'If the renewed workup is reassuring, how would you sequence '
                                     'treatments while defining measurable response?',
                        'curveball_answer': 'Start with behavioral cough suppression therapy, then '
                                            'add a neuromodulator such as gabapentin or low-dose '
                                            'amitriptyline if benefit is partial. Consider '
                                            'superior laryngeal nerve block in specialist centers '
                                            'for persistent refractory cough. Measure response '
                                            'with a validated cough questionnaire or cough '
                                            'frequency at baseline and after each step, stopping '
                                            'treatments that fail.'}}
