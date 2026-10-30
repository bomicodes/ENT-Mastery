"""v491 rewrites: Head & Neck Oncology part 1 (hn1)."""

REWRITES = {'v11_hn_01': {'stem': 'A 63-year-old man with a 45 pack-year smoking history has 4 months of '
                       'progressive hoarseness. Laryngoscopy shows an exophytic left true vocal '
                       'fold tumor extending into the ventricle and touching the anterior '
                       'commissure; the left fold does not move with phonation. CT shows a 1.8-cm '
                       'tumor with intact thyroid cartilage, no extralaryngeal spread, and no '
                       'adenopathy. Biopsy shows squamous cell carcinoma. Which finding assigns '
                       'this tumor its T category?',
               'choices': ['Immobility of the left true vocal fold on phonation',
                           'Extension of tumor into the left laryngeal ventricle',
                           'Contact with the anterior commissure at the midline',
                           'Overall tumor length approaching 2 cm on imaging'],
               'answer': 0,
               'explanation': 'For glottic cancer, the AJCC 8 T category is driven by extent and '
                              'mobility rather than size. T1 is confined to the folds with normal '
                              'mobility; T2 extends to the supraglottis or subglottis or impairs '
                              'mobility; T3 is a fixed fold, paraglottic space invasion, or '
                              'inner-cortex thyroid cartilage erosion. Fixation reflects deep '
                              'invasion of the thyroarytenoid muscle, paraglottic space, or '
                              'cricoarytenoid joint, so the immobile fold makes this T3 even '
                              'though the cartilage is intact and the tumor is small.',
               'why_wrong': ['Correct.',
                             'Ventricular or supraglottic extension upgrades a glottic tumor only '
                             'to T2, so it does not explain the higher category here.',
                             'Anterior commissure contact does not change the T category by '
                             'itself, although it raises concern for cartilage invasion and '
                             'complicates endoscopic resection.',
                             'Glottic T staging does not use tumor diameter; a small tumor with a '
                             'fixed fold is still T3.'],
               'board_pearl': 'Glottic staging: impaired mobility is T2, fixed fold or paraglottic '
                              'space or inner cortex is T3.',
               'curveball': 'Fine-cut CT now shows tumor through the outer cortex of the thyroid '
                            'cartilage into the strap muscles. How does that change staging and '
                            'the treatment discussion?',
               'curveball_answer': 'Invasion through the outer cortex of the thyroid cartilage or '
                                   'into extralaryngeal soft tissue such as the strap muscles is '
                                   'T4a. Cartilage-penetrating T4a disease responds poorly to '
                                   'organ preservation and was largely excluded from the major '
                                   'trials, so NCCN favors total laryngectomy with neck dissection '
                                   'and adjuvant therapy as indicated. Chemoradiation is reserved '
                                   'for selected patients who decline surgery.'},
 'v116-hno-02': {'stem': 'A 58-year-old woman who smokes has 3 months of hoarseness. Stroboscopy '
                         'shows a right true vocal fold lesion with absent mucosal wave and '
                         'sluggish but present abduction. Contrast CT shows enhancing tumor '
                         'extending lateral to the thyroarytenoid muscle into the fat deep to the '
                         'thyroid lamina, with intact cartilage and no nodes. Biopsy shows '
                         'squamous cell carcinoma. Which finding places this tumor beyond early '
                         'T1-T2 glottic disease?',
                 'choices': ['Paraglottic space invasion seen on the contrast CT',
                             'Absent mucosal wave over the lesion on stroboscopy',
                             'Reduced but preserved abduction of the right fold',
                             'Superficial spread of tumor to the vocal process'],
                 'answer': 0,
                 'explanation': 'The paraglottic space lies between the thyroarytenoid muscle and '
                                'the thyroid cartilage and connects the glottis with the '
                                'supraglottis. Tumor in this space defines T3 glottic disease in '
                                'AJCC 8 even when the fold still moves, because it signals deep '
                                'spread that is often underestimated on mucosal examination. That '
                                'deep extension reduces the success of radiation alone or limited '
                                'transoral resection, which are designed for early lesions. '
                                'Impaired mobility alone is T2; fixation or paraglottic invasion '
                                'is T3.',
                 'why_wrong': ['Correct.',
                               'Loss of mucosal wave shows the lesion is stiff and at least into '
                               'the vocal ligament, but it does not define T category.',
                               'Impaired mobility without fixation is a T2 feature, so this '
                               'finding alone keeps the tumor within early-stage disease.',
                               'Superficial extension along the fold to the vocal process stays '
                               'within T1 or T2 and does not indicate deep spread.'],
                 'board_pearl': 'Paraglottic space invasion makes glottic cancer T3 even if the '
                                'fold still moves.',
                 'curveball': 'The patient asks whether transoral laser surgery is still possible. '
                              'What features would make an experienced surgeon decline an '
                              'endoscopic approach for this T3 tumor?',
                 'curveball_answer': 'Selected T3 glottic tumors can be resected transorally by '
                                     'experienced surgeons, but poor exposure, deep paraglottic '
                                     'spread toward the thyroid cartilage, arytenoid fixation from '
                                     'cricoarytenoid joint involvement, subglottic extension, and '
                                     'anterior commissure involvement with cartilage contact make '
                                     'clear margins unlikely. In those settings, chemoradiation or '
                                     'open partial or total laryngectomy is preferred over a '
                                     'margin-positive endoscopic resection.',
                 'accuracy_note': 'The original implied that impaired vocal fold mobility by '
                                  'itself marks progression beyond early disease; impaired '
                                  'mobility alone is T2, and fixation or paraglottic invasion is '
                                  'T3.'},
 'v128_hn_04': {'stem': 'A 61-year-old man who smokes has a 2-cm squamous cell carcinoma on the '
                        'laryngeal surface of the suprahyoid epiglottis with normal vocal fold '
                        'mobility. CT shows enlarged level II nodes on both sides, 2.2 cm and 1.4 '
                        'cm, both FNA-positive. A junior resident asks why such a small tumor has '
                        'bilateral nodes, when his last patient with a T1 vocal fold cancer had '
                        'none. Which explanation is most accurate?',
                'choices': ['Tracheobronchial embryologic origin of the supraglottic larynx',
                            'Drainage of the epiglottis through the prelaryngeal Delphian node',
                            'Dense lymphatic network of the supraglottis that crosses midline',
                            'Higher rate of HPV association in supraglottic carcinoma'],
                'answer': 2,
                'explanation': 'The supraglottis develops from the buccopharyngeal primordium and '
                               'has a rich, bilaterally communicating lymphatic network that '
                               'drains through the thyrohyoid membrane to levels II and III. The '
                               'true vocal folds have very sparse lymphatics, so early glottic '
                               'cancers rarely metastasize, while even small supraglottic tumors '
                               'carry substantial occult and bilateral nodal risk. Midline '
                               'epiglottic tumors in particular drain to both necks, which is why '
                               'both sides are treated even in cN0 patients.',
                'why_wrong': ['The glottis and subglottis arise from the tracheobronchial '
                              'primordium; the supraglottis is buccopharyngeal in origin, so this '
                              'reverses the embryology.',
                              'The Delphian node mainly receives anterior glottic and subglottic '
                              'drainage; supraglottic lymphatics exit through the thyrohyoid '
                              'membrane to levels II-III.',
                              'Correct.',
                              'HPV is not a meaningful driver of laryngeal carcinoma, and viral '
                              'status does not explain the anatomic difference in nodal spread.'],
                'board_pearl': 'Supraglottis: rich bilateral lymphatics and early nodes. Glottis: '
                               'sparse lymphatics, rare nodes when early.',
                'curveball': "A different patient's glottic tumor extends 1.5 cm below the vocal "
                             'folds. Which nodal basins now need attention?',
                'curveball_answer': 'Subglottic extension brings drainage through the cricothyroid '
                                    'membrane to the prelaryngeal (Delphian) node and through the '
                                    'cricotracheal membrane to the paratracheal (level VI) and '
                                    'upper mediastinal nodes. Treatment should therefore include '
                                    'level VI on the involved side, often bilaterally, with '
                                    'ipsilateral hemithyroidectomy or total thyroidectomy '
                                    'considered when the tumor abuts the thyroid. Subglottic '
                                    'extension also raises stomal recurrence risk after '
                                    'laryngectomy.'},
 'v219_hn_larynx_app': {'stem': 'A 67-year-old man has 6 months of hoarseness and new mild '
                                'dysphagia. Laryngoscopy shows a transglottic left tumor with a '
                                'fixed left vocal fold. CT shows tumor filling the left '
                                'paraglottic space with erosion of the inner cortex of the thyroid '
                                'lamina, an intact outer cortex, and no extralaryngeal soft '
                                'tissue. Neck and chest imaging are negative. Which T category is '
                                'correct?',
                        'choices': ['T3, since cortical erosion is limited to the inner cortex',
                                    'T4a, because any thyroid cartilage erosion upstages the tumor',
                                    'T2, because transglottic spread without cartilage penetration',
                                    'T4b, because the tumor reaches the deep paraglottic fat '
                                    'plane'],
                        'answer': 0,
                        'explanation': 'In AJCC 8 laryngeal staging, vocal fold fixation, '
                                       'paraglottic space invasion, and erosion of the inner '
                                       'cortex of the thyroid cartilage are all T3 features. T4a '
                                       'requires tumor through the outer cortex or into tissues '
                                       'beyond the larynx, such as the trachea, strap muscles, '
                                       'thyroid, or esophagus. This distinction matters because T3 '
                                       'tumors remain candidates for larynx preservation, whereas '
                                       'cartilage-penetrating T4a disease generally favors total '
                                       'laryngectomy.',
                        'why_wrong': ['Correct.',
                                      'Inner-cortex erosion alone is T3; T4a requires penetration '
                                      'through the outer cortex or extralaryngeal spread.',
                                      'Transglottic spread with a fixed fold and paraglottic '
                                      'invasion exceeds T2, which allows only impaired mobility.',
                                      'T4b means prevertebral space invasion, mediastinal '
                                      'involvement, or carotid encasement, none of which is '
                                      'present.'],
                        'board_pearl': 'Inner cortex erosion is T3; through the outer cortex or '
                                       'out of the larynx is T4a.',
                        'curveball': 'Six weeks later, repeat imaging shows tumor extending '
                                     'through the cricothyroid membrane into the anterior neck '
                                     'soft tissue. How does that change T category and management?',
                        'curveball_answer': 'Spread through the cricothyroid membrane into the '
                                            'anterior neck soft tissue is extralaryngeal extension '
                                            'and makes the tumor T4a. This favors total '
                                            'laryngectomy with ipsilateral thyroid lobectomy, '
                                            'level VI dissection and neck dissection as indicated, '
                                            'followed by adjuvant radiation or chemoradiation '
                                            'based on pathology, rather than nonsurgical organ '
                                            'preservation.'},
 'v219_hn_larynx_snr': {'stem': 'A 66-year-old man with a newly biopsied bulky supraglottic '
                                'squamous cell carcinoma comes to the emergency department at 2 '
                                'a.m. with worsening stridor and suprasternal retractions. He is '
                                'sitting upright, speaking in short phrases, with oxygen '
                                'saturation 95% on room air. Flexible laryngoscopy shows friable '
                                'tumor obscuring most of the glottic inlet with a small residual '
                                'airway. What is the best next step?',
                        'choices': ['Rapid-sequence induction and video laryngoscopy in the '
                                    'department',
                                    'Dexamethasone and heliox with contrast CT of the neck in the '
                                    'morning',
                                    'Awake tracheostomy under local anesthesia in the operating '
                                    'room',
                                    'Inhalational induction in the operating room with oral '
                                    'intubation'],
                        'answer': 2,
                        'explanation': 'This is impending airway obstruction from a friable, '
                                       'obstructing tumor, and securing the airway comes before '
                                       'staging. Sedation or paralysis removes the muscle tone '
                                       'holding the airway open, and instrumentation can cause '
                                       'bleeding or complete obstruction when the glottis cannot '
                                       'be seen. Because he is still oxygenating, the safest '
                                       'course is a controlled awake tracheostomy below the tumor '
                                       'under local anesthesia in the operating room, with '
                                       'anesthesia present and the team ready for a surgical '
                                       'airway.',
                        'why_wrong': ['Paralysis in a patient with an obstructing tumor can cause '
                                      'a cannot-intubate, cannot-oxygenate emergency, and the '
                                      'glottis may not be visible.',
                                      'Steroids and heliox only buy time, and lying supine for CT '
                                      'could precipitate complete obstruction in this patient.',
                                      'Correct.',
                                      'Inhalational induction can still lose the airway when tone '
                                      'falls, and tumor can block or bleed into the field during '
                                      'intubation.'],
                        'board_pearl': 'Obstructing laryngeal tumor with stridor: secure the '
                                       'airway awake, usually by tracheostomy under local '
                                       'anesthesia.',
                        'curveball': 'The anesthesiologist suggests awake fiberoptic intubation '
                                     'instead. Which tumor features make that approach especially '
                                     'risky here?',
                        'curveball_answer': 'Awake fiberoptic intubation is reasonable when a '
                                            'scope can be passed through a visible glottic '
                                            'opening, but it is risky when bulky friable '
                                            'supraglottic tumor obscures the inlet. The scope or '
                                            'tube can cause bleeding, push tumor into the '
                                            'remaining lumen, or wedge in a small airway, causing '
                                            'complete obstruction. Awake tracheostomy below the '
                                            'tumor avoids passing through it. Tumor that extends '
                                            'into the subglottis requires a lower tracheotomy '
                                            'site.'},
 'v11_hn_02': {'stem': 'A 52-year-old man who has never smoked notices a painless left neck mass '
                       'that has slowly enlarged over 5 weeks. He had no preceding infection or '
                       'fever. Examination shows a 3.5-cm soft, mobile mass beneath the anterior '
                       'border of the sternocleidomastoid at level IIA. Ultrasound shows a cystic '
                       'mass with a thick, irregular wall. Flexible laryngoscopy and oral '
                       'examination are normal. Which diagnosis must be presumed until proven '
                       'otherwise?',
               'choices': ['Cystic nodal metastasis from HPV-associated oropharyngeal carcinoma',
                           'Second branchial cleft cyst presenting for the first time in adulthood',
                           'Tuberculous cervical lymphadenitis with central caseous necrosis',
                           'Suppurative lymphadenitis from an odontogenic infection source'],
               'answer': 0,
               'explanation': 'A new cystic lateral neck mass in an adult over 40 is metastatic '
                              'carcinoma until proven otherwise. HPV-associated oropharyngeal '
                              'carcinoma often arises in a small tonsillar or base-of-tongue '
                              'primary and spreads early to level II nodes that become cystic, so '
                              'it can mimic a branchial cleft cyst. The 2017 AAO-HNSF neck mass '
                              'guideline lists cystic masses as high risk and advises against '
                              'excising a presumed branchial cyst before FNA and a search for a '
                              'primary.',
               'why_wrong': ['Correct.',
                             'Branchial cleft cysts usually present earlier in life; assuming one '
                             'in a 52-year-old risks open excision of a metastasis.',
                             'Tuberculous adenitis usually produces matted nodes, constitutional '
                             'symptoms, or exposure history, none of which this patient has.',
                             'Suppurative adenitis follows an infection with tenderness and fever; '
                             'this mass is painless and arose without any infectious trigger.'],
               'board_pearl': 'Adult cystic lateral neck mass: think HPV oropharyngeal metastasis, '
                              'not branchial cyst.',
               'curveball': 'Ultrasound-guided FNA returns only acellular cyst fluid. What should '
                            'happen next?',
               'curveball_answer': 'A nondiagnostic aspirate does not exclude carcinoma, because '
                                   'cystic metastases often yield sparse cells. Repeat '
                                   'ultrasound-guided FNA targeting the solid wall, or core needle '
                                   'biopsy, with p16 immunohistochemistry and HPV testing on the '
                                   'cell block. Proceed with imaging and examination under '
                                   'anesthesia of the oropharynx. If still nondiagnostic, open '
                                   'excisional biopsy with frozen section should be done only when '
                                   'the team is ready to proceed with neck dissection.'},
 'v11_hn_04': {'stem': 'A 49-year-old man has a 3-cm firm right level IIA node present for 2 '
                       'months. FNA shows nonkeratinizing squamous cell carcinoma with strong p16 '
                       'staining. He has never used tobacco. Oral examination, palpation, and '
                       'flexible nasopharyngolaryngoscopy show no mucosal lesion. CT of the neck '
                       'shows the node but no primary. Where is the occult primary most likely to '
                       'be found?',
               'choices': ['Fossa of Rosenmuller in the lateral nasopharynx',
                           'Apex of the pyriform sinus or postcricoid mucosa',
                           'Crypt epithelium of the palatine or lingual tonsil',
                           'Laryngeal ventricle or saccule beneath the false fold'],
               'answer': 2,
               'explanation': 'p16-positive squamous cell carcinoma in a level II node is very '
                              'likely HPV-associated, and HPV-associated carcinoma arises in the '
                              'reticulated crypt epithelium of the palatine and lingual tonsils. '
                              'These primaries can be millimeters in size and buried deep in '
                              'crypts, so they are often invisible on examination and CT. The '
                              'workup therefore focuses on the palatine and lingual tonsils, often '
                              'with PET/CT before examination under anesthesia.',
               'why_wrong': ['Nasopharyngeal carcinoma is usually EBV-driven and EBER-positive; '
                             'p16 positivity points to the oropharyngeal tonsils, not the '
                             'nasopharynx.',
                             'Hypopharyngeal primaries are rarely HPV-driven and usually occur in '
                             'heavy smokers and drinkers, unlike this never-smoker.',
                             'Correct.',
                             'Supraglottic carcinoma is tobacco-related, not HPV-driven, and a '
                             'ventricular primary would rarely present as a p16-positive cystic '
                             'node.'],
               'board_pearl': 'p16-positive unknown primary: look in the palatine and lingual '
                              'tonsil crypts first.',
               'curveball': 'Directed biopsies of both tonsils and the base of tongue are '
                            'negative. What do palatine and lingual tonsillectomy add?',
               'curveball_answer': 'Biopsies miss small primaries buried deep in tonsillar crypts. '
                                   'Palatine tonsillectomy, often bilateral, together with '
                                   'transoral lingual tonsillectomy greatly increases detection '
                                   'over biopsies alone. Finding a small primary allows directed '
                                   'transoral resection or limits radiation to the involved side, '
                                   'sparing the contralateral pharynx, larynx, and nasopharynx and '
                                   'reducing late dysphagia and xerostomia.'},
 'v116-hno-01': {'stem': 'A 57-year-old man who has never smoked has a 4-cm cystic right level II '
                         'neck mass. Ultrasound-guided FNA shows squamous cell carcinoma, '
                         'p16-positive. Office examination and flexible laryngoscopy show no '
                         'mucosal lesion. Contrast CT of the neck shows the cystic node and no '
                         'obvious primary. He is scheduled to see you next week to plan the '
                         'operative evaluation. What is the most appropriate next step?',
                 'choices': ['Open excisional biopsy of the node to confirm the histology',
                             'Neck dissection now, with the mucosal search done afterward',
                             'PET/CT before examination under anesthesia and tonsil surgery',
                             'Chemoradiation to the neck and pharynx without further search'],
                 'answer': 2,
                 'explanation': 'FNA has already confirmed p16-positive squamous cell carcinoma, '
                                'so the priority is finding the oropharyngeal primary without '
                                'compromising the neck. PET/CT should be obtained before '
                                'examination under anesthesia because biopsy and tonsillectomy '
                                'cause postoperative inflammation and false-positive uptake. PET '
                                'can show a small tonsillar or base-of-tongue focus to target, '
                                'stage distant disease, and guide surgery. Open biopsy of the node '
                                'is unnecessary and violates the neck, and treating without '
                                'searching for the primary forfeits the chance to narrow the '
                                'treatment fields.',
                 'why_wrong': ['The diagnosis is already established by FNA; open biopsy adds no '
                               'information and violates tissue planes before definitive '
                               'treatment.',
                               'Neck dissection before identifying the primary may commit him to '
                               'surgery that an identified primary would have redirected.',
                               'Correct.',
                               'Treating without a primary search commits him to wide mucosal '
                               'fields and the late toxicity that a found primary might avoid.'],
                 'board_pearl': 'Unknown primary: get PET/CT before the operating room, because '
                                'biopsy causes false-positive uptake.',
                 'curveball': 'PET/CT shows faint uptake in both the right palatine tonsil and the '
                              'right base of tongue. How does that shape the operation?',
                 'curveball_answer': 'Faint PET uptake is common in normal lymphoid tissue, so it '
                                     'guides rather than proves the site. Plan examination under '
                                     'anesthesia with right palatine tonsillectomy and transoral '
                                     'right lingual tonsillectomy, with frozen sections and '
                                     'oriented specimens. Many surgeons also remove the left '
                                     'palatine tonsil because some primaries are contralateral. '
                                     'Finding the primary with clear margins may allow transoral '
                                     'surgery alone or directed radiation.'},
 'v128_hn_02': {'stem': 'A 60-year-old man has a 2.5-cm left level IIA node; FNA shows '
                        'p16-positive squamous cell carcinoma. Flexible laryngoscopy, oral '
                        'examination, CT of the neck, and PET/CT show no primary site. An outside '
                        'surgeon proposes examination under anesthesia with random mucosal '
                        'biopsies of the nasopharynx, base of tongue, and pyriform sinus. Which '
                        'operative strategy best increases the chance of finding the primary?',
                'choices': ['Random biopsies of the nasopharynx, tongue base, and pyriform',
                            'Palatine tonsillectomy plus transoral lingual tonsillectomy',
                            'Bilateral neck dissection with frozen section of the left node',
                            'Repeat PET/CT in 6 weeks before any operative evaluation'],
                'answer': 1,
                'explanation': 'HPV-associated primaries hide in tonsillar crypts and are often '
                               'too small to see or to hit with random biopsy. Removing the '
                               'palatine tonsils and the lingual tonsil, usually by transoral '
                               'robotic or laser surgery, examines the entire crypt epithelium and '
                               'finds the primary far more often than random biopsies. Finding it '
                               'allows targeted surgery or narrower radiation fields. Pyriform and '
                               'nasopharyngeal biopsies add little when the node is p16-positive.',
                'why_wrong': ['Random biopsies sample a tiny fraction of tonsillar crypt '
                              'epithelium and miss most small HPV primaries.',
                              'Correct.',
                              'Neck dissection treats the node but does not search the mucosa, so '
                              'the primary stays unknown and fields stay wide.',
                              'Delaying for repeat imaging rarely reveals a primary that PET has '
                              'already missed and only postpones treatment.'],
                'board_pearl': 'Palatine plus lingual tonsillectomy finds far more occult '
                               'primaries than random biopsies.',
                'curveball': 'Bilateral palatine tonsillectomy shows no carcinoma on permanent '
                             'sections. What does adding a lingual tonsillectomy offer?',
                'curveball_answer': 'Many occult HPV-associated primaries that are not in the '
                                    'palatine tonsils lie in the lingual tonsil. Transoral lingual '
                                    'tonsillectomy removes this crypt epithelium for full '
                                    'pathologic examination and finds a primary in many patients '
                                    'after negative palatine tonsillectomy and imaging. A found '
                                    'primary can allow transoral resection or radiation limited to '
                                    'the involved side, while morbidity of the lingual procedure '
                                    'is usually modest.'},
 'v135_hn_01': {'stem': 'A 52-year-old man who never smoked was treated by his primary physician '
                        'with two courses of amoxicillin-clavulanate for a painless right neck '
                        'lump that did not shrink. Examination shows a 3-cm fluctuant level II '
                        'mass and normal oral cavity and laryngoscopy. FNA shows squamous cell '
                        'carcinoma that is p16-positive. Neck CT confirms a cystic node without a '
                        'visible primary. What is the most appropriate next step?',
                'choices': ['PET/CT, then examination under anesthesia with tonsil surgery',
                            'Transcervical excision of the cyst with frozen-section analysis',
                            'A third course of antibiotics followed by repeat ultrasound',
                            'Thyroid ultrasound and thyroglobulin washout of the aspirate'],
                'answer': 0,
                'explanation': 'An adult cystic neck mass that fails antibiotics and shows '
                               'p16-positive squamous cell carcinoma is presumed HPV-associated '
                               'oropharyngeal metastasis. The 2017 AAO-HNSF neck mass guideline '
                               'warns against prolonged antibiotics without follow-up and against '
                               'excising a presumed cyst. The next step is a search for the '
                               'oropharyngeal primary with PET/CT and examination under '
                               'anesthesia, including palatine and lingual tonsil evaluation, '
                               'before definitive treatment.',
                'why_wrong': ['Correct.',
                              'Excising the mass violates the neck and confirms nothing that FNA '
                              'has not already shown; the primary would remain unknown.',
                              'More antibiotics delay cancer care; the guideline advises against '
                              'repeated antibiotics for an adult neck mass without clear '
                              'infection.',
                              'Papillary thyroid metastases can be cystic, but the cytology here '
                              'is squamous cell carcinoma with p16 positivity, not thyroid '
                              'carcinoma.'],
                'board_pearl': 'Adult neck mass that fails antibiotics: stop treating it as '
                               'infection and search for a primary.',
                'curveball': 'No primary is found despite palatine and lingual tonsillectomy. '
                             'Which factors help decide whether radiation fields can be safely '
                             'narrowed?',
                'curveball_answer': 'Narrowing is reasonable when the node is p16-positive, '
                                    'lateralized, and limited, and when bilateral palatine and '
                                    'lingual tonsillectomy are negative. Radiation can then focus '
                                    'on the ipsilateral neck and oropharynx, sparing the larynx, '
                                    'hypopharynx, nasopharynx, and often the contralateral neck. '
                                    'Bilateral or low-neck nodes, smoking history, and imaging ENE '
                                    'argue for wider fields. Protocols vary between centers.'},
 'v219_hn_unknown_snr': {'stem': 'A 54-year-old man has a 3-cm right level II node with '
                                 'p16-positive squamous cell carcinoma on FNA. Flexible endoscopy '
                                 'and PET/CT show no primary. Examination under anesthesia '
                                 'elsewhere with random biopsies of the tongue base and '
                                 'nasopharynx was negative; his tonsils were not removed. '
                                 'Radiation oncology proposes treating the entire pharyngeal axis '
                                 'and both necks. What should be done first?',
                         'choices': ['Proceed with pharyngeal-axis and bilateral neck radiation as '
                                     'planned',
                                     'Repeat the random mucosal biopsies under anesthesia, taking '
                                     'more and deeper cores',
                                     'Bilateral palatine tonsillectomy and transoral lingual '
                                     'tonsillectomy',
                                     'Ultrasound-guided core biopsy of the node for HPV in situ '
                                     'testing'],
                         'answer': 2,
                         'explanation': 'Random biopsies miss small HPV-associated primaries '
                                        'buried in tonsillar crypts. Removing the palatine tonsils '
                                        'and, transorally, the lingual tonsil allows full '
                                        'histologic examination and identifies the primary in many '
                                        'patients with negative imaging and biopsies. Finding a '
                                        'small lateralized primary can allow transoral resection '
                                        'or focused radiation and spare the uninvolved mucosa from '
                                        'full-dose treatment. That is worth doing before '
                                        'committing to wide-field radiation and its lifelong '
                                        'dysphagia risk.',
                         'why_wrong': ['Committing to wide-field radiation without tonsillectomy '
                                       'accepts avoidable toxicity when the primary is still '
                                       'likely findable.',
                                       'More random biopsies have the same low yield as before; '
                                       'removing the crypt-bearing tissue is what improves '
                                       'detection.',
                                       'Correct.',
                                       'The node is already p16-positive carcinoma, so more nodal '
                                       'tissue would not help locate the mucosal primary.'],
                         'board_pearl': 'Before wide-field radiation for unknown primary, remove '
                                        'the palatine and lingual tonsils.',
                         'curveball': 'A 6-mm primary is found in the right palatine tonsil with '
                                      'clear margins. How can this change radiation planning?',
                         'curveball_answer': 'With a known, completely excised right tonsil '
                                             'primary, radiation can target the right tonsillar '
                                             'bed and right neck instead of the full pharyngeal '
                                             'axis and both necks. Sparing the contralateral '
                                             'pharynx and larynx lowers dysphagia and xerostomia. '
                                             'In selected patients with limited nodal disease, '
                                             'transoral resection plus neck dissection may allow '
                                             'lower-dose adjuvant radiation or none, depending on '
                                             'pathology.'},
 'v11_hn_03': {'stem': 'A 59-year-old woman has a 1.5-cm ulcerated, indurated lesion of the left '
                       'lateral oral tongue present for 2 months. Incisional biopsy shows invasive '
                       'moderately differentiated squamous cell carcinoma. There are no palpable '
                       'nodes, and contrast CT of the neck is negative. The tumor board debates '
                       'whether to treat the clinically negative neck. Which feature of the '
                       'primary best predicts occult nodal metastasis?',
               'choices': ['Total tumor thickness including the exophytic component',
                           'Greatest surface diameter of the ulcer on examination',
                           'Degree of keratinization on the incisional biopsy specimen',
                           'Depth of invasion below the adjacent basement membrane'],
               'answer': 3,
               'explanation': 'Depth of invasion, measured from the basement membrane of adjacent '
                              'normal mucosa to the deepest point of tumor, is the strongest '
                              'primary-tumor predictor of occult nodal metastasis in oral cavity '
                              'carcinoma. It was added to AJCC 8 T staging for this reason. NCCN '
                              'recommends elective neck dissection when depth exceeds about 4 mm, '
                              'with clinical judgment between 2 and 4 mm. Depth reflects access to '
                              'deeper lymphatics, which surface diameter and thickness do not.',
               'why_wrong': ['Thickness includes exophytic tumor above the mucosal surface and '
                             'overestimates risk in bulky exophytic lesions.',
                             'Surface diameter defines the basic T category, but small tumors can '
                             'invade deeply, so size alone underestimates occult nodal risk.',
                             'Keratinization and grade are weak, inconsistent predictors of nodal '
                             'spread compared with depth of invasion.',
                             'Correct.'],
               'board_pearl': 'Oral cavity cN0 neck: depth of invasion, not thickness, drives '
                              'elective neck decisions.',
               'curveball': 'Final pathology after partial glossectomy shows 6 mm depth of '
                            'invasion, perineural invasion, and clear margins, but no neck was '
                            'dissected. What now?',
               'curveball_answer': 'A depth of 6 mm makes her pT2 and carries occult nodal risk '
                                   'well above the usual threshold for elective neck treatment, so '
                                   'offer ipsilateral selective neck dissection of levels I-III, '
                                   'often with IV for oral tongue. Perineural invasion is an '
                                   'intermediate-risk feature that supports adjuvant radiation, '
                                   'and final neck pathology will guide the radiation fields and '
                                   'whether chemotherapy is needed.'},
 'v140_hn_06': {'stem': 'A 55-year-old man has a 1.8-cm squamous cell carcinoma of the right '
                        'lateral oral tongue. MRI estimates a depth of invasion of 9 mm, and the '
                        'tumor is more than 1 cm from midline. Neck examination and contrast CT '
                        'show no adenopathy. He is fit for surgery and is scheduled for partial '
                        'glossectomy. What is the most appropriate management of his neck?',
                'choices': ['Ultrasound surveillance because the primary is under 2 cm',
                            'Elective radiation to the right neck after the glossectomy',
                            'Bilateral modified radical neck dissection of levels I to V',
                            'Right selective neck dissection of levels I through III'],
                'answer': 3,
                'explanation': 'At 1.8 cm with 9 mm depth of invasion, this is a T2 oral tongue '
                               'cancer, and occult nodal risk is well above the threshold for '
                               'elective treatment. Because the primary is treated surgically, '
                               'elective ipsilateral selective neck dissection, at least levels '
                               'I-III and often including level IV for oral tongue, is standard. '
                               'It also provides pathologic staging that guides adjuvant therapy. '
                               "The D'Cruz randomized trial showed better survival with elective "
                               'than with delayed therapeutic neck dissection.',
                'why_wrong': ['Small surface size does not offset a 9-mm depth of invasion, which '
                              'makes occult nodal disease too likely for observation.',
                              'Elective neck radiation is reasonable when the primary is '
                              'irradiated, but here it adds toxicity without pathologic staging.',
                              'A comprehensive bilateral dissection is excessive for a '
                              'well-lateralized cN0 tumor and adds shoulder and lymphedema '
                              'morbidity.',
                              'Correct.'],
                'board_pearl': 'Oral tongue with depth over about 4 mm and cN0 neck: elective '
                               'selective neck dissection.',
                'curveball': 'How close to midline must the primary be before the contralateral '
                             'neck needs elective treatment?',
                'curveball_answer': 'Contralateral risk rises when the tumor reaches or crosses '
                                    'midline, involves the floor of mouth or tongue base, or is '
                                    'deeply invasive near the midline septum. Many surgeons treat '
                                    'both necks when the tumor is within about 1 cm of midline or '
                                    'crosses it. A clearly lateralized tumor, like this one, '
                                    'usually needs only ipsilateral elective dissection, but '
                                    'practice varies.'},
 'v219_hn_tongue_fnd': {'stem': 'A 61-year-old man who smokes and drinks daily has a painful sore '
                                'on the right lateral oral tongue for 6 weeks, with right ear '
                                'pain. His dentist smoothed a sharp molar 3 weeks ago, but the '
                                'sore has not healed. Examination shows a 2-cm ulcer with raised, '
                                'firm edges and induration on palpation; otoscopy is normal and no '
                                'nodes are palpable. What is the most appropriate next step?',
                        'choices': ['Topical triamcinolone paste with recheck in another 4 weeks',
                                    'Brush cytology of the ulcer base for an office screening test',
                                    'Oral fluconazole for presumed chronic hyperplastic '
                                    'candidiasis',
                                    'Incisional biopsy taken from the indurated edge of the ulcer'],
                        'answer': 3,
                        'explanation': 'An oral ulcer persisting more than 2-3 weeks after '
                                       'removing the presumed irritant, especially with induration '
                                       'and referred otalgia in a smoker and drinker, is carcinoma '
                                       'until proven otherwise. Otalgia with a normal ear reflects '
                                       'referred pain through the lingual nerve (V3) and possibly '
                                       'the glossopharyngeal nerve. The next step is a scalpel or '
                                       'punch biopsy from the edge, including deep tissue, '
                                       'followed by staging that assesses size, depth, and neck '
                                       'nodes.',
                        'why_wrong': ['Topical steroids delay diagnosis of a likely carcinoma that '
                                      'has already failed removal of the presumed traumatic cause.',
                                      'Brush cytology can miss invasive carcinoma and cannot '
                                      'measure depth; an indurated lesion needs a tissue biopsy.',
                                      'Candidiasis does not cause an indurated ulcer with referred '
                                      'otalgia, and an antifungal trial would only delay '
                                      'diagnosis.',
                                      'Correct.'],
                        'board_pearl': 'Indurated oral ulcer persisting after removing the '
                                       'irritant: biopsy now.',
                        'curveball': 'Biopsy confirms squamous cell carcinoma. Which examination '
                                     'findings suggest deep extension that changes resection and '
                                     'reconstruction planning?',
                        'curveball_answer': 'Reduced tongue protrusion or deviation suggests '
                                            'extrinsic muscle or hypoglossal involvement. '
                                            'Induration extending to the floor of mouth, ventral '
                                            'tongue, or tongue base suggests deep spread, and '
                                            'fixation to the mandible suggests bone involvement. '
                                            'Trismus raises concern for masticator space spread. '
                                            'Lingual nerve numbness suggests perineural spread. '
                                            'These findings call for MRI and can convert a partial '
                                            'glossectomy into a composite resection needing '
                                            'free-flap reconstruction.'},
 'v219_hn_tongue_app': {'stem': 'A 48-year-old woman has a 1.8-cm squamous cell carcinoma of the '
                                'left lateral oral tongue with a depth of invasion of 7 mm on MRI. '
                                'Her neck is negative on examination and CT. She asks why she '
                                'needs a neck operation when no lymph node is enlarged. You cite '
                                "the randomized trial by D'Cruz and colleagues in early oral "
                                'cancer. What did that trial show?',
                        'choices': ['Watchful waiting with salvage surgery gave equal overall '
                                    'survival',
                                    'Elective dissection improved overall survival over delayed '
                                    'surgery',
                                    'Elective neck radiation outperformed elective neck dissection',
                                    'The survival benefit was limited to tumors larger than 4 cm'],
                        'answer': 1,
                        'explanation': "In the D'Cruz trial, patients with lateralized T1-T2 cN0 "
                                       'oral cavity squamous cell carcinoma had better overall and '
                                       'disease-free survival with elective neck dissection at the '
                                       'time of primary surgery than with watchful waiting and '
                                       'therapeutic dissection on nodal relapse. Patients who '
                                       'waited often relapsed with more advanced nodal disease. '
                                       'With a depth of 7 mm she is T2 with substantial occult '
                                       'nodal risk, so elective ipsilateral selective neck '
                                       'dissection should be recommended.',
                        'why_wrong': ['Watchful waiting led to worse survival, because nodal '
                                      'relapses often presented with extranodal extension and were '
                                      'harder to salvage.',
                                      'Correct.',
                                      'The trial compared elective neck dissection with '
                                      'observation and did not test elective radiation against '
                                      'surgery.',
                                      'The trial enrolled only early T1-T2 tumors, so there was no '
                                      'subgroup of tumors larger than 4 cm.'],
                        'board_pearl': "D'Cruz: elective neck dissection beats watchful waiting "
                                       'for early cN0 oral cancer.',
                        'curveball': 'She asks whether sentinel lymph node biopsy is an '
                                     'alternative. What do you tell her?',
                        'curveball_answer': 'For cT1-T2 cN0 oral cavity cancer, sentinel lymph '
                                            'node biopsy is an accepted alternative to elective '
                                            'neck dissection in centers with experience, with '
                                            'similar detection and less shoulder morbidity in '
                                            'trials. Positive sentinel nodes lead to completion '
                                            'neck dissection. It is less reliable for '
                                            'floor-of-mouth tumors near the injection site and '
                                            'needs nuclear medicine and pathology support.'},
 'v219_hn_tongue_snr': {'stem': 'A 52-year-old thin man has a T3 squamous cell carcinoma of the '
                                'right lateral oral tongue. Planned resection will remove about '
                                '40% of the mobile tongue with a small cuff of floor-of-mouth '
                                'mucosa, leaving the tongue base and the opposite half intact. He '
                                'has good dentition, no mandible involvement, and a normal Allen '
                                'test. Which reconstruction best serves his speech and swallowing?',
                        'choices': ['Bulky rectus abdominis myocutaneous free flap to maximize '
                                    'volume',
                                    'Primary closure of the remaining tongue edges to the floor of '
                                    'mouth',
                                    'Pedicled pectoralis major myocutaneous flap tunneled into the '
                                    'mouth',
                                    'Thin, pliable radial forearm free flap to the hemiglossectomy '
                                    'defect'],
                        'answer': 3,
                        'explanation': 'A hemiglossectomy defect with the opposite half and tongue '
                                       'base intact needs thin, pliable lining that lets the '
                                       'remaining tongue move freely. A radial forearm free flap '
                                       'restores surface area and modest volume without tethering, '
                                       'which best preserves articulation and bolus manipulation. '
                                       'Bulky flaps suit near-total or total glossectomy, where '
                                       'volume is needed for palatal contact and bolus propulsion. '
                                       'Primary closure of a large defect tethers the tongue to '
                                       'the floor of mouth.',
                        'why_wrong': ['A bulky flap fills the mouth and restricts the mobile '
                                      'remnant; bulk is needed mainly after total or subtotal '
                                      'glossectomy.',
                                      'Closing a 40% defect primarily tethers the residual tongue '
                                      'to the floor of mouth and worsens speech and swallowing.',
                                      'A pectoralis flap is bulky, gravity pulls it down, and it '
                                      'tethers the tongue; it is better reserved for salvage or '
                                      'neck coverage.',
                                      'Correct.'],
                        'board_pearl': 'Partial glossectomy: thin, pliable flap for mobility. '
                                       'Total glossectomy: bulky flap for volume.',
                        'curveball': 'If the resection instead became a total glossectomy with '
                                     'laryngeal preservation, how would the reconstruction goal '
                                     'change?',
                        'curveball_answer': 'After total glossectomy there is no mobile remnant to '
                                            'preserve, so the goal is enough convex bulk to '
                                            'contact the palate and propel the bolus. A bulky '
                                            'anterolateral thigh or rectus abdominis flap, '
                                            'designed to over-correct for later atrophy, is '
                                            'preferred. Laryngeal suspension and cricopharyngeal '
                                            'myotomy are often added, and aspiration risk is '
                                            'high.'},
 'v429-oral-cavity-doi-threshold-01': {'stem': 'A 64-year-old woman underwent transoral excision '
                                               'of a 1.4-cm left lateral oral tongue squamous cell '
                                               'carcinoma, done without neck surgery because the '
                                               'lesion looked superficial. Final pathology shows a '
                                               'depth of invasion of 5 mm, margins clear by 6 mm, '
                                               'and no perineural or lymphovascular invasion. Her '
                                               'neck remains negative on examination and contrast '
                                               'CT. What should be recommended next?',
                                       'choices': ['Observation only, because the primary was '
                                                   'small and fully removed',
                                                   'Radiation to the primary bed alone to treat '
                                                   'any occult nodes',
                                                   'Wider re-excision of the primary site instead '
                                                   'of neck treatment',
                                                   'Left selective neck dissection of the at-risk '
                                                   'nodal levels'],
                                       'answer': 3,
                                       'explanation': 'A 5-mm depth of invasion carries enough '
                                                      'risk of occult nodal metastasis to justify '
                                                      'elective neck treatment, even with a small, '
                                                      'completely excised primary. NCCN recommends '
                                                      'elective dissection for depth greater than '
                                                      '4 mm. A left selective neck dissection, '
                                                      'levels I-III and often IV for oral tongue, '
                                                      'both treats and stages the neck. Sentinel '
                                                      'node biopsy or close ultrasound '
                                                      'surveillance are alternatives in '
                                                      'experienced programs.',
                                       'why_wrong': ['Small size and clear margins do not address '
                                                     'the occult nodal risk created by a 5-mm '
                                                     'depth of invasion.',
                                                     'Radiating only the primary bed does not '
                                                     'cover the cervical nodes, and the primary '
                                                     'already has clear margins.',
                                                     'Margins are already clear by 6 mm, and '
                                                     're-excision cannot address the nodal risk.',
                                                     'Correct.'],
                                       'board_pearl': 'Depth of invasion on final pathology can '
                                                      'revive the neck question after a small '
                                                      'excision.',
                                       'curveball': 'The neck dissection shows one 2-cm level II '
                                                    'node with pathologic extranodal extension. '
                                                    'How does that change her stage and treatment?',
                                       'curveball_answer': 'A single ipsilateral node up to 3 cm '
                                                           'with extranodal extension is pN2a in '
                                                           'AJCC 8, which makes her stage IVA. '
                                                           'Extranodal extension is a high-risk '
                                                           'feature, so postoperative radiation '
                                                           'with concurrent cisplatin is '
                                                           'recommended if she is fit, starting '
                                                           'ideally within about 6 weeks of '
                                                           'surgery.'},
 'v429-oral-cavity-staging-pearl-01': {'stem': 'A 56-year-old man has a 1.2-cm squamous cell '
                                               'carcinoma of the right lateral oral tongue with a '
                                               'depth of invasion of 3 mm on biopsy and MRI. CT '
                                               'shows a single 2-cm right level IIA node without '
                                               'imaging signs of extranodal extension, and FNA '
                                               'confirms carcinoma. PET/CT shows no distant '
                                               'disease. What is the AJCC 8 overall stage group?',
                                       'choices': ['Stage II', 'Stage III', 'Stage IVA', 'Stage I'],
                                       'answer': 1,
                                       'explanation': 'A tumor of 2 cm or less with depth of '
                                                      'invasion of 5 mm or less is T1. A single '
                                                      'ipsilateral node of 3 cm or less without '
                                                      'extranodal extension is N1. In AJCC 8 oral '
                                                      'cavity staging, any N1 disease with T1-T3 '
                                                      'is stage III, and N2 disease or T4a is '
                                                      'required for stage IVA. Small primaries can '
                                                      'therefore be stage III once a node is '
                                                      'positive, which affects counseling and '
                                                      'trial eligibility.',
                                       'why_wrong': ['Stage II applies to T2N0 disease, and any '
                                                     'nodal involvement moves this patient beyond '
                                                     'stage II.',
                                                     'Correct.',
                                                     'Stage IVA requires T4a disease or N2 nodal '
                                                     'disease, such as a larger node, multiple '
                                                     'nodes, or extranodal extension.',
                                                     'Stage I is T1N0; the positive node excludes '
                                                     'stage I.'],
                                       'board_pearl': 'Oral cavity AJCC 8: T1-T3 with N1 is stage '
                                                      'III; N2 or T4a is IVA.',
                                       'curveball': 'If the neck dissection shows extranodal '
                                                    'extension in that same 2-cm node, how do the '
                                                    'nodal category and stage change?',
                                       'curveball_answer': 'Pathologic extranodal extension in a '
                                                           'single ipsilateral node of 3 cm or '
                                                           'less makes it pN2a, so the stage '
                                                           'becomes IVA. Clinical ENE on '
                                                           'examination or imaging is classified '
                                                           'differently, as cN3b, which is stage '
                                                           'IVB. ENE is also a high-risk feature '
                                                           'for adjuvant cisplatin-radiation.'},
 'v429-oral-cavity-bilateral-neck-01': {'stem': 'A 62-year-old man who smokes has a 2.5-cm '
                                                'squamous cell carcinoma of the anterior floor of '
                                                'mouth that reaches the lingual frenulum at '
                                                'midline. MRI estimates a depth of invasion of 6 '
                                                'mm without mandibular involvement. Both sides of '
                                                'the neck are negative on examination and contrast '
                                                'CT. Resection with free flap reconstruction is '
                                                'planned. What neck plan best addresses his '
                                                'drainage pattern?',
                                        'choices': ['Ipsilateral levels I-III dissection with '
                                                    'contralateral observation',
                                                    'Bilateral ultrasound surveillance with '
                                                    'dissection if nodes appear',
                                                    'Bilateral selective neck dissection of levels '
                                                    'I through III',
                                                    'Sentinel node biopsy from the side with the '
                                                    'greater tumor bulk'],
                                        'answer': 2,
                                        'explanation': 'Floor-of-mouth tumors that reach or cross '
                                                       'midline drain to both necks, and occult '
                                                       'contralateral metastasis is common, '
                                                       'especially in the submental and '
                                                       'submandibular nodes. With a 6-mm depth and '
                                                       'midline involvement, elective bilateral '
                                                       'selective neck dissection of levels I-III '
                                                       'is appropriate. It treats both at-risk '
                                                       'basins, stages the neck for adjuvant '
                                                       'therapy, and exposes recipient vessels for '
                                                       'the free flap.',
                                        'why_wrong': ['Observing the contralateral neck ignores '
                                                      'the bilateral drainage of a midline '
                                                      'floor-of-mouth primary.',
                                                      'Surveillance is inappropriate at this '
                                                      'depth; nodal relapse after observation is '
                                                      'often harder to salvage.',
                                                      'Correct.',
                                                      'Sentinel node mapping is less reliable in '
                                                      'the floor of mouth because injection near '
                                                      'the primary can obscure nearby nodes, and '
                                                      'one side is not enough here.'],
                                        'board_pearl': 'Midline floor-of-mouth cancer: treat both '
                                                       'necks electively.',
                                        'curveball': 'What changes if a 2-cm ipsilateral level IB '
                                                     'node is clinically positive?',
                                        'curveball_answer': 'That neck becomes therapeutic: '
                                                            'dissect levels I-IV or I-V on that '
                                                            'side as indicated, preserving '
                                                            'uninvolved structures, while the '
                                                            'contralateral neck still receives '
                                                            'elective levels I-III. The node also '
                                                            'raises the stage and may change '
                                                            'adjuvant therapy, which will depend '
                                                            'on final pathology, especially '
                                                            'extranodal extension and margins.'},
 'v11_hn_05': {'stem': 'A 78-year-old man had a 2-cm squamous cell carcinoma of the right frontal '
                       'scalp excised 14 months ago. He now has a 2.5-cm firm, painless mass in '
                       'the right preauricular parotid region, with normal facial nerve function '
                       'and no other palpable nodes. He has never smoked and has no oral or throat '
                       'symptoms. Ultrasound-guided FNA shows keratinizing squamous cell '
                       'carcinoma. What is the most likely source of this mass?',
               'choices': ['Primary squamous cell carcinoma arising in the parotid ductal tissue',
                           'High-grade mucoepidermoid carcinoma sampled from squamoid areas',
                           'Metastasis to an intraparotid lymph node from the scalp primary',
                           'Nodal metastasis from an occult HPV-associated tonsil carcinoma'],
               'answer': 2,
               'explanation': 'The parotid contains intraparotid and periparotid lymph nodes that '
                              'drain the scalp, forehead, temple, auricle, and lateral face. In '
                              'older fair-skinned patients, squamous cell carcinoma in the parotid '
                              'is far more often a nodal metastasis from cutaneous carcinoma than '
                              'a true salivary primary, and the prior frontal scalp cancer is the '
                              'deciding clue. Diagnosis of primary parotid squamous cell carcinoma '
                              'requires excluding a cutaneous or mucosal source first.',
               'why_wrong': ['True primary parotid squamous cell carcinoma is rare and is '
                             'diagnosed only after a cutaneous or mucosal source is excluded.',
                             'Mucoepidermoid carcinoma can look squamoid, but it contains mucous '
                             'cells, and the prior scalp primary makes metastasis more likely.',
                             'Correct.',
                             'HPV-associated nodes are usually level II and nonkeratinizing; '
                             'keratinizing tumor in the parotid after scalp cancer points to '
                             'skin.'],
               'board_pearl': 'SCC in the parotid of an older patient: assume metastatic cutaneous '
                              'SCC until proven otherwise.',
               'curveball': 'CT also shows two enlarged right level II nodes. How does that change '
                            'the extent of surgery?',
               'curveball_answer': 'Clinically positive neck nodes call for a therapeutic neck '
                                   'dissection, usually levels I or II through V depending on the '
                                   'primary site, together with parotidectomy, rather than an '
                                   'elective selective dissection. Superficial parotidectomy is '
                                   'extended to total if deep-lobe nodes are involved. The facial '
                                   'nerve is preserved unless directly invaded. Postoperative '
                                   'radiation is standard, with concurrent therapy considered for '
                                   'extranodal extension or positive margins.'},
 'v113-hn-04': {'stem': 'A 71-year-old man had a squamous cell carcinoma of the left cheek excised '
                        '18 months ago; pathology noted perineural invasion, and margins were '
                        'clear. He now has 3 months of progressive numbness of the left cheek, '
                        'side of the nose, and upper lip, with intermittent crawling sensations. '
                        'The scar is well healed with no visible recurrence, and facial movement '
                        'is normal. Which process should be suspected?',
                'choices': ['Postherpetic neuralgia affecting the maxillary division',
                            'Classic trigeminal neuralgia from vascular nerve compression',
                            'Scar-related injury to small sensory twigs at the site',
                            'Perineural spread of tumor along the infraorbital nerve'],
                'answer': 3,
                'explanation': 'Progressive numbness, paresthesia, or formication in a named nerve '
                               'distribution after a high-risk cutaneous squamous cell carcinoma, '
                               'especially one with known perineural invasion, indicates '
                               'perineural spread until proven otherwise. Tumor can travel along '
                               'the infraorbital nerve toward the pterygopalatine fossa and '
                               'foramen rotundum without a visible skin recurrence. The cheek, '
                               'lateral nose, and upper lip match the infraorbital branch of V2. '
                               'MRI with contrast and fat suppression is the key study.',
                'why_wrong': ['Postherpetic neuralgia follows a shingles eruption and causes pain; '
                              'it does not produce progressive numbness without a rash.',
                              'Trigeminal neuralgia causes brief electric pain with a normal '
                              'sensory exam, not progressive numbness.',
                              'Scar injury to small twigs causes stable local numbness at the '
                              'scar, not a progressive full infraorbital distribution.',
                              'Correct.'],
                'board_pearl': 'New numbness in a named nerve after high-risk cSCC means '
                               'perineural spread until proven otherwise.',
                'curveball': 'Which skull-base foramina would you scrutinize on MRI if the '
                             'symptoms were in the V2 or the V3 distribution?',
                'curveball_answer': 'For V2, follow the infraorbital nerve through the '
                                    'infraorbital canal to the pterygopalatine fossa, foramen '
                                    'rotundum, and cavernous sinus, looking for loss of fat in the '
                                    'pterygopalatine fossa. For V3, examine the inferior alveolar '
                                    'and auriculotemporal nerves, the masticator space, and '
                                    'foramen ovale; denervation atrophy of the muscles of '
                                    'mastication supports V3 spread. Also check Meckel cave.'},
 'v128_hn_06': {'stem': 'A 74-year-old immunocompetent man has a 1.6-cm squamous cell carcinoma '
                        'excised from the left cheek. Pathology shows a moderately differentiated '
                        'tumor 3 mm thick confined to the dermis, with surface ulceration, '
                        'adjacent actinic keratosis, and marked solar elastosis. Tumor cells '
                        'encircle a dermal nerve measuring 0.2 mm in diameter. Margins are clear. '
                        'Which pathologic finding most increases his risk of recurrence and nodal '
                        'metastasis?',
                'choices': ['Surface epidermal ulceration',
                            'Perineural invasion',
                            'Actinic keratosis',
                            'Solar elastosis'],
                'answer': 1,
                'explanation': 'Perineural invasion is one of the strongest adverse features in '
                               'cutaneous squamous cell carcinoma, associated with local '
                               'recurrence, nodal metastasis, and disease-specific death. '
                               "Involvement of a nerve 0.1 mm or larger is a Brigham and Women's "
                               'high-risk factor, and NCCN treats perineural involvement as a very '
                               'high-risk feature that should prompt discussion of adjuvant '
                               'radiation. The other findings reflect sun damage or surface change '
                               'rather than aggressive biology.',
                'why_wrong': ['Ulceration is common in cutaneous SCC and is not a staging or '
                              'high-risk criterion in AJCC 8 or the Brigham system.',
                              'Correct.',
                              'Adjacent actinic keratosis reflects field sun damage and does not '
                              'by itself change the risk of the excised tumor.',
                              'Solar elastosis is background photodamage and does not predict '
                              'recurrence or nodal spread.'],
                'board_pearl': 'Perineural invasion, especially of nerves 0.1 mm or larger, is a '
                               'major high-risk feature in cSCC.',
                'curveball': 'What imaging findings would suggest clinically significant '
                             'perineural spread rather than microscopic perineural invasion alone?',
                'curveball_answer': 'On contrast MRI with fat suppression, signs include nerve '
                                    'thickening and enhancement, widening or erosion of a '
                                    'skull-base foramen, loss of normal fat at the pterygopalatine '
                                    'fossa or stylomastoid foramen, and denervation changes in the '
                                    'muscles the nerve supplies. Microscopic invasion alone '
                                    'usually shows nothing on imaging. Radiographic spread changes '
                                    'T stage, surgical extent, and radiation fields.'},
 'v135_hn_03': {'stem': 'A 69-year-old man has a second recurrence of squamous cell carcinoma of '
                        'the left temple after Mohs surgery. He reports numbness over the left '
                        'cheek and upper lip. MRI with contrast shows thickening and enhancement '
                        'of the left infraorbital nerve through the infraorbital canal, stopping '
                        'short of the pterygopalatine fossa. There is no parotid or neck '
                        'adenopathy. How should this finding change his treatment plan?',
                'choices': ['Repeat Mohs excision at the temple with standard peripheral margins',
                            'Give adjuvant radiation limited to the temple scar and its margins',
                            'Follow the nerve with resection and radiate its path to the skull '
                            'base',
                            'Observe with repeat MRI in 3 months before changing the plan'],
                'answer': 2,
                'explanation': 'Radiographic named-nerve involvement turns a skin cancer into a '
                               'perineural problem that must be treated along the nerve. Surgery '
                               'should follow the infraorbital nerve proximally with frozen '
                               'sections, often including maxillectomy or orbital floor resection, '
                               'and radiation must cover the nerve path back to the skull base, '
                               'typically the pterygopalatine fossa and foramen rotundum. Treating '
                               'only the skin site leaves disease in the nerve and leads to '
                               'skull-base recurrence.',
                'why_wrong': ['Mohs examines skin margins but not the infraorbital nerve deep in '
                              'the canal, so tumor along the nerve would be left.',
                              'Radiating only the scar misses tumor tracking along the nerve '
                              'toward the skull base.',
                              'Correct.',
                              'Observing radiographic named-nerve spread allows progression into '
                              'the skull base, where cure becomes much harder.'],
                'board_pearl': 'Named-nerve perineural spread: treat the nerve path to the skull '
                               'base, not just the skin.',
                'curveball': 'Repeat MRI 6 weeks later shows enhancement extending through the '
                             'foramen rotundum. How does that affect operability and adjuvant '
                             'planning?',
                'curveball_answer': 'Tumor through the foramen rotundum is skull-base involvement, '
                                    'T4b in AJCC 8, and usually means the nerve cannot be cleared '
                                    'to a negative margin without major skull-base surgery. Many '
                                    'centers then treat with definitive radiation along V2 back to '
                                    'the gasserian ganglion. A PD-1 inhibitor such as cemiplimab '
                                    'is an option for unresectable disease, with surgery '
                                    'considered only in selected patients.'},
 'v223_hn_cscc_fnd': {'stem': 'A 70-year-old man has a 1.5-cm well-differentiated squamous cell '
                              'carcinoma of the right forehead that has been present for 6 months. '
                              'He now has difficulty raising his right eyebrow, and examination '
                              'confirms right frontal branch weakness with normal lower facial '
                              'movement. MRI shows enhancement along the frontal branch toward the '
                              'stylomastoid foramen. He is immunocompetent. Which feature most '
                              'increases his risk?',
                      'choices': ['Clinical perineural spread along a facial nerve branch',
                                  'Location of the primary on sun-exposed forehead skin',
                                  'Primary tumor diameter of 1.5 cm at presentation',
                                  'Well-differentiated histology on the shave biopsy'],
                      'answer': 0,
                      'explanation': 'Clinical or radiographic perineural spread along a named '
                                     'nerve is among the most adverse features in cutaneous '
                                     'squamous cell carcinoma, predicting local and skull-base '
                                     'recurrence and lower disease-specific survival. It upstages '
                                     'the tumor regardless of its surface size and calls for '
                                     'imaging of the full nerve path, surgery that follows the '
                                     'nerve, and radiation along the path to the skull base. A '
                                     'small, well-differentiated lesion can still behave '
                                     'aggressively once it tracks along a nerve.',
                      'why_wrong': ['Correct.',
                                    'Head and neck location adds some risk, but here site matters '
                                    'far less than clinical involvement of a named nerve.',
                                    'A diameter under 2 cm is low risk by size criteria, so size '
                                    'alone does not explain his high risk.',
                                    'Well-differentiated histology is favorable; poor '
                                    'differentiation, not good differentiation, is the adverse '
                                    'feature.'],
                      'board_pearl': 'Clinical named-nerve spread in cSCC outweighs size, site, '
                                     'and grade in predicting poor outcome.',
                      'curveball': 'Which named nerves most commonly require skull-base imaging '
                                   'when cutaneous SCC is suspected of perineural spread?',
                      'curveball_answer': 'The trigeminal branches and the facial nerve are most '
                                          'often involved. V1 travels through the supraorbital '
                                          'nerve to the superior orbital fissure, V2 through the '
                                          'infraorbital nerve to the foramen rotundum, and V3 '
                                          'through the auriculotemporal and inferior alveolar '
                                          'nerves to the foramen ovale. The facial nerve leads to '
                                          'the stylomastoid foramen and temporal bone. Spread can '
                                          'also cross between V3 and VII via the auriculotemporal '
                                          'nerve.'},
 'v223_hn_cscc_snr': {'stem': 'A 68-year-old man has a third recurrence of squamous cell carcinoma '
                              'of the left temple. He has left cheek numbness, and MRI shows '
                              'enhancement along V2 to the foramen rotundum without cavernous '
                              'sinus involvement. There is a 2.5-cm left intraparotid node and no '
                              'distant disease on PET/CT. He is fit and wants curative treatment. '
                              'What is the best plan?',
                      'choices': ['Wide local excision of the temple recurrence with radiation to '
                                  'it',
                                  'En bloc skin, parotid, and neck resection tracing V2, then '
                                  'radiation',
                                  'Superficial parotidectomy and neck dissection, leaving the '
                                  'nerve',
                                  'Radiation to the temple and parotid, omitting the trigeminal '
                                  'path'],
                      'answer': 1,
                      'explanation': 'Named-nerve spread to the skull base plus intraparotid '
                                     'metastasis makes this a regional and skull-base problem. '
                                     'Curative treatment needs one multidisciplinary plan: en bloc '
                                     'resection of the skin site, parotidectomy and neck '
                                     'dissection, and the V2 pathway traced proximally with frozen '
                                     'sections, often through a skull-base approach. Postoperative '
                                     'radiation must cover the primary bed, parotid, neck, and the '
                                     'nerve path to the gasserian ganglion. Adjuvant cemiplimab '
                                     'may be considered for high-risk disease after radiation, '
                                     'based on C-POST.',
                      'why_wrong': ['Excising the skin site alone ignores both the parotid '
                                    'metastasis and tumor along V2 toward the skull base.',
                                    'Correct.',
                                    'Treating the parotid and neck while leaving V2 leaves gross '
                                    'disease along the nerve to recur at the skull base.',
                                    'Leaving the nerve pathway out of the radiation field fails to '
                                    'treat the most likely site of recurrence.'],
                      'board_pearl': 'cSCC with named-nerve spread plus nodal disease: plan '
                                     'surgery and radiation as one regional skull-base unit.',
                      'curveball': 'If the enhancement extended into the cavernous sinus and was '
                                   'judged unresectable, how would the roles of radiation and '
                                   'immunotherapy change?',
                      'curveball_answer': 'With unresectable intracranial spread, surgery is no '
                                          'longer curative. A PD-1 inhibitor such as cemiplimab is '
                                          'a first-line systemic option for unresectable locally '
                                          'advanced cSCC, with high response rates. Definitive '
                                          'radiation along the trigeminal pathway to the ganglion '
                                          'and brainstem margin is another option, used alone or '
                                          'with systemic therapy, and the choice depends on '
                                          'symptoms, prior radiation, and goals.'},
 'v11_hn_06': {'stem': 'A 64-year-old man completed 66 Gy of radiation for a left floor-of-mouth '
                       'squamous cell carcinoma 2 years ago. Four months ago a left lower first '
                       'molar was extracted, and the socket has not healed. He has exposed '
                       'yellow-gray bone in the socket with mild pain and no fistula. He has never '
                       'received bisphosphonates or denosumab. Biopsy of the socket margin shows '
                       'no carcinoma. What is the most likely diagnosis?',
               'choices': ['Medication-related osteonecrosis of the jaw from antiresorptives',
                           'Alveolar osteitis from loss of the clot in the extraction socket',
                           'Recurrent carcinoma invading the mandible at the extraction site',
                           'Osteoradionecrosis of the mandible after dental extraction'],
               'answer': 3,
               'explanation': 'Osteoradionecrosis is irradiated bone that becomes exposed and '
                              'fails to heal over months in the absence of tumor. High-dose '
                              'mandibular radiation causes small-vessel injury, fibrosis, and loss '
                              'of bone cells, so trauma such as an extraction can start a wound '
                              'that does not heal. Post-radiation extraction in a high-dose field '
                              'is a classic trigger, and the posterior mandible is the most common '
                              'site. Negative biopsy and no antiresorptive exposure confirm the '
                              'diagnosis.',
               'why_wrong': ['MRONJ requires exposure to antiresorptive or antiangiogenic drugs, '
                             'which this patient has never received.',
                             'Dry socket presents a few days after extraction and resolves within '
                             'weeks; it does not persist for 4 months.',
                             'Recurrence must be excluded, but the socket biopsy shows no '
                             'carcinoma.',
                             'Correct.'],
               'board_pearl': 'Exposed, nonhealing bone in an irradiated field after excluding '
                              'tumor is osteoradionecrosis.',
               'curveball': 'Months later he develops a pathologic fracture and a draining skin '
                            'fistula. Which findings push you from conservative care toward '
                            'segmental resection?',
               'curveball_answer': 'Pathologic fracture, orocutaneous fistula, necrosis extending '
                                   'to the inferior border, and failure of conservative or medical '
                                   'therapy mark advanced osteoradionecrosis. These are structural '
                                   'failures that do not heal with local care, so the standard is '
                                   'segmental resection to bleeding bone with vascularized '
                                   'reconstruction, usually a fibula free flap. Recurrence should '
                                   'be excluded with imaging and biopsy first.'},
 'v116-hno-03': {'stem': 'A 59-year-old woman completed chemoradiation for a right tonsil squamous '
                         'cell carcinoma 3 years ago. She now has right jaw pain with intermittent '
                         'purulent drainage and 1 cm of exposed bone on the lingual right '
                         'mandible. CT shows mottled lucency, sclerosis, and cortical breakdown of '
                         'the right mandibular body without a soft-tissue mass; PET shows no nodal '
                         'uptake. She takes no antiresorptive drugs. Bone-edge biopsy is negative '
                         'for carcinoma. What is the most likely diagnosis?',
                 'choices': ['Chronic suppurative osteomyelitis from an odontogenic focus',
                             'Recurrent squamous cell carcinoma invading the mandible',
                             'Medication-related osteonecrosis of the mandibular body',
                             'Osteoradionecrosis with secondary bacterial colonization'],
                 'answer': 3,
                 'explanation': 'Exposed irradiated bone with pain, drainage, and mixed '
                                'lytic-sclerotic changes with cortical breakdown is classic '
                                'osteoradionecrosis. The primary problem is radiation injury that '
                                'leaves bone poorly vascularized and unable to heal; bacteria '
                                'colonize the exposed bone secondarily rather than causing the '
                                'disease. The tonsil and ipsilateral mandible were in the '
                                'high-dose field. Recurrence must be excluded, and here the '
                                'absence of a soft-tissue mass and negative biopsy support '
                                'osteoradionecrosis.',
                 'why_wrong': ['Bacteria are present, but the underlying cause is '
                               'radiation-damaged bone; antibiotics alone do not cure it as they '
                               'can in ordinary osteomyelitis.',
                               'Recurrence must be considered, but the absent soft-tissue mass, '
                               'negative PET, and negative biopsy argue against it.',
                               'Medication-related osteonecrosis requires antiresorptive or '
                               'antiangiogenic drug exposure, which she has not had.',
                               'Correct.'],
                 'board_pearl': 'Irradiated mandible with lytic-sclerotic change and no mass: '
                                'osteoradionecrosis, but always exclude recurrence.',
                 'curveball': 'Which features would move management from conservative care toward '
                              'segmental resection and vascularized reconstruction?',
                 'curveball_answer': 'Escalate when there is pathologic fracture, orocutaneous '
                                     'fistula, necrosis through the full bone height or to the '
                                     'inferior border, extensive involvement on CT, or persistent '
                                     'pain and infection despite debridement and medical therapy. '
                                     'These indicate advanced disease. Segmental mandibulectomy to '
                                     'bleeding bone with a vascularized bone free flap, usually '
                                     'fibula, is then the definitive treatment.'},
 'v128_hn_07': {'stem': 'A 67-year-old man completed radiation for a base-of-tongue squamous cell '
                        'carcinoma 18 months ago. He has a nonhealing 8-mm area of exposed bone on '
                        'the left posterior mandible with mild pain; cultures grow mixed oral '
                        'flora. Biopsy shows necrotic bone without carcinoma. A junior resident '
                        'proposes a 6-week course of antibiotics as definitive treatment. Which '
                        'mechanism best explains why this approach is unlikely to cure him?',
                'choices': ['The mixed oral flora are resistant to standard oral antibiotics',
                            'Residual microscopic tumor in the marrow prevents bone healing',
                            'Radiation-induced hypovascular, hypocellular fibrosis impairs healing',
                            'Osteoclast suppression from radiation blocks normal bone turnover'],
                'answer': 2,
                'explanation': 'Osteoradionecrosis results from radiation injury to bone and its '
                               'blood supply. Endarteritis, fibrosis, and loss of osteoblasts and '
                               'osteocytes leave hypoxic, hypocellular, hypovascular tissue that '
                               'cannot heal after minor trauma, the model described by Marx, with '
                               'newer radiation-induced fibroatrophic theories. Bacteria colonize '
                               'the exposed bone but are secondary, so antibiotics treat '
                               'superimposed infection without restoring healing. This is why '
                               'therapy targets tissue biology and removes necrotic bone.',
                'why_wrong': ['Mixed flora are expected contaminants of exposed bone; resistance '
                              'is not why antibiotics fail.',
                              'The biopsy is negative for carcinoma, and residual tumor is not the '
                              'mechanism of osteoradionecrosis.',
                              'Correct.',
                              'Osteoclast inhibition is the mechanism of antiresorptive '
                              'osteonecrosis; radiation injury is primarily vascular and '
                              'fibrotic.'],
                'board_pearl': 'ORN is radiation-damaged tissue that cannot heal; infection is '
                               'secondary, not the cause.',
                'curveball': 'Which medical therapy targets the fibroatrophic mechanism, and how '
                             'strong is the evidence?',
                'curveball_answer': 'Pentoxifylline combined with tocopherol, sometimes with '
                                    'clodronate, targets radiation-induced fibrosis and oxidative '
                                    'injury. Case series and small trials show healing or '
                                    'stabilization in many patients with early or moderate '
                                    'osteoradionecrosis, but randomized evidence is limited. '
                                    'Hyperbaric oxygen remains debated after mixed trial results. '
                                    'Both are used with local care rather than as replacements for '
                                    'resection of advanced disease.'},
 'v225_hn_orn_fnd': {'stem': 'A 62-year-old woman treated with 70 Gy for a left retromolar trigone '
                             'squamous cell carcinoma 2 years ago has 4 months of exposed bone '
                             'along the left mandibular alveolus with mild discomfort. She has '
                             'never taken antiresorptive drugs. Biopsy of the adjacent soft tissue '
                             'shows no carcinoma. The radiation oncologist asks you to document a '
                             'formal diagnosis. Which description best fits osteoradionecrosis of '
                             'the jaw?',
                     'choices': ['Any bone exposure in a field irradiated in the past, with or '
                                 'without tumor',
                                 'Jaw necrosis that requires prior exposure to antiresorptive '
                                 'medication',
                                 'Irradiated bone that is exposed and fails to heal, without tumor',
                                 'Pain in an irradiated jaw with a normal mucosal and radiographic '
                                 'exam'],
                     'answer': 2,
                     'explanation': 'Osteoradionecrosis of the jaw is irradiated bone that becomes '
                                    'devitalized and exposed, or necrotic on imaging, and fails to '
                                    'heal over a period of months, after residual or recurrent '
                                    'tumor has been excluded. Definitions differ in the required '
                                    'duration, often 3 months, and newer classifications include '
                                    'imaging-only disease. Excluding recurrence is central, '
                                    'because carcinoma can mimic osteoradionecrosis. '
                                    'Antiresorptive exposure points instead to medication-related '
                                    'osteonecrosis.',
                     'why_wrong': ['Exposed bone with active tumor is recurrence, not '
                                   'osteoradionecrosis; excluding carcinoma is part of the '
                                   'definition.',
                                   'Antiresorptive exposure defines medication-related '
                                   'osteonecrosis, a separate entity with a different mechanism.',
                                   'Correct.',
                                   'Pain without exposed or necrotic bone does not meet the '
                                   'definition, though it warrants close follow-up.'],
                     'board_pearl': 'ORN definition: irradiated, devitalized bone that fails to '
                                    'heal for months, with tumor excluded.',
                     'curveball': 'The resident is drafting a prevention handout for future '
                                  'patients. Which dental and radiation factors raise the risk of '
                                  'osteoradionecrosis?',
                     'curveball_answer': 'Risk rises with mandibular doses above about 60 Gy, '
                                         'larger volumes of high-dose bone, oral cavity and '
                                         'oropharyngeal primaries near the mandible, and the '
                                         'posterior mandible. Dental factors include poor '
                                         'dentition, periodontal disease, extractions after '
                                         'radiation, and ill-fitting dentures. Smoking, alcohol, '
                                         'mandibular surgery, and concurrent chemotherapy add '
                                         'risk. Prevention relies on pre-radiation dental '
                                         'extraction of nonrestorable teeth, fluoride, and careful '
                                         'oral hygiene.'},
 'v225_hn_orn_app': {'stem': 'A 61-year-old man completed chemoradiation for a left tonsil '
                             'squamous cell carcinoma 2 years ago. At a routine visit he has a '
                             '6-mm area of exposed bone on the lingual surface of the left '
                             'mandible near the mylohyoid ridge, with minimal discomfort. There is '
                             'no fistula, trismus, or swelling. CT shows no fracture or deep bone '
                             'destruction, and PET shows no recurrence. He still smokes. What is '
                             'the best initial management?',
                     'choices': ['Chlorhexidine rinses, smoking cessation, and close clinical '
                                 'follow-up',
                                 'Segmental mandibulectomy with fibula free flap reconstruction',
                                 'Hyperbaric oxygen therapy as the required first intervention',
                                 'Extraction of the adjacent teeth to remove a possible source'],
                     'answer': 0,
                     'explanation': 'Small, minimally symptomatic osteoradionecrosis without '
                                    'fracture, fistula, or extensive bone loss is treated '
                                    'conservatively first. Care includes antiseptic rinses, '
                                    'avoidance of trauma and denture pressure, antibiotics for '
                                    'infection, removal of loose sequestra, and smoking and '
                                    'alcohol cessation, with close follow-up for progression. Many '
                                    'small lesions stabilize or heal. Pentoxifylline-tocopherol '
                                    'may be added. Surgery is reserved for progressive, '
                                    'refractory, or structurally complicated disease.',
                     'why_wrong': ['Correct.',
                                   'Segmental resection is for advanced disease with fracture, '
                                   'fistula, or failure of conservative therapy, not a small '
                                   'stable lesion.',
                                   'Hyperbaric oxygen is debated after mixed trial results and is '
                                   'an optional adjunct rather than a required first step.',
                                   'Extracting teeth in a high-dose field is itself a major '
                                   'trigger and would likely worsen the necrosis.'],
                     'board_pearl': 'Early, limited ORN: start with conservative care and close '
                                    'watching, not resection.',
                     'curveball': 'He returns every 6 weeks for review. What findings on follow-up '
                                  'would indicate progression to advanced osteoradionecrosis?',
                     'curveball_answer': 'Progression is shown by enlarging exposed bone, new '
                                         'orocutaneous fistula, pathologic fracture, necrosis '
                                         'extending to the inferior border or through the full '
                                         'bone height on CT, persistent infection, or uncontrolled '
                                         'pain. Any new soft-tissue mass, nodes, or fast change '
                                         'should prompt biopsy to exclude recurrence. Advanced '
                                         'disease usually requires segmental resection with '
                                         'vascularized bone reconstruction.'},
 'v225_hn_orn_snr': {'stem': 'A 63-year-old man treated with radiation for oral cavity squamous '
                             'cell carcinoma 5 years ago has a pathologic fracture of the right '
                             'mandibular body, a draining submandibular skin fistula, and severe '
                             'pain. CT shows necrosis through the full height of the mandible over '
                             '4 cm. He has failed debridement, antibiotics, and '
                             'pentoxifylline-tocopherol. Biopsy shows no recurrence. What is the '
                             'best management?',
                     'choices': ['Reconstruction plate across the fracture after debridement',
                                 'Further hyperbaric oxygen followed by limited sequestrectomy',
                                 'Pedicled pectoralis major flap over the fractured mandible',
                                 'Segmental resection to bleeding bone and a fibula free flap'],
                     'answer': 3,
                     'explanation': 'Pathologic fracture, fistula, and full-height necrosis are '
                                    'signs of advanced osteoradionecrosis that will not heal with '
                                    'local care. Definitive treatment removes all nonviable bone '
                                    'back to bleeding margins and replaces it with '
                                    'well-vascularized tissue that can heal in an irradiated '
                                    'field. A fibula osteocutaneous free flap restores mandibular '
                                    'continuity, provides skin to close the fistula, and brings '
                                    'its own blood supply. Recurrence must be excluded first, as '
                                    'it was here.',
                     'why_wrong': ['A plate alone in irradiated, necrotic bone has a high rate of '
                                   'exposure, infection, and failure without vascularized '
                                   'coverage.',
                                   'Hyperbaric oxygen and limited debridement have already been '
                                   'outmatched by full-height necrosis with fracture and fistula.',
                                   'Soft-tissue coverage does not remove the necrotic bone or '
                                   'restore mandibular continuity, so the fracture would persist.',
                                   'Correct.'],
                     'board_pearl': 'Advanced ORN with fracture or fistula: resect to bleeding '
                                    'bone and reconstruct with vascularized bone.',
                     'curveball': 'He had a prior right neck dissection and radiation. How should '
                                  'recipient-vessel quality shape reconstructive planning?',
                     'curveball_answer': 'Irradiated, previously dissected necks may lack usable '
                                         'vessels. CT angiography helps plan. Options include the '
                                         'contralateral neck vessels, the transverse cervical '
                                         'artery and vein low in the neck, the superficial '
                                         'temporal vessels, and a transposed cephalic vein. Vein '
                                         'grafts may be needed to bridge gaps. Choosing a flap '
                                         'with a long pedicle also helps.'},
 'v113-hn-01': {'stem': 'A 47-year-old Vietnamese man has 3 months of left ear fullness, two '
                        'episodes of blood-streaked nasal mucus, and a painless left neck lump. '
                        'Otoscopy shows a left middle ear effusion with a type B tympanogram; the '
                        'right ear is normal. There is a 2.5-cm firm left level II node. Flexible '
                        'endoscopy shows a friable mass in the left lateral nasopharyngeal recess. '
                        'What is the most likely diagnosis?',
                'choices': ['Adenoid hypertrophy with reactive nodes',
                            'Extranodal NK/T-cell lymphoma, nasal type',
                            'Nasopharyngeal carcinoma',
                            'Juvenile nasopharyngeal angiofibroma'],
                'answer': 2,
                'explanation': 'Unilateral middle ear effusion in an adult demands nasopharyngeal '
                               'examination, because a mass in the fossa of Rosenmuller can block '
                               'the eustachian tube orifice. With a neck node, blood-streaked '
                               'mucus, and Southeast Asian ancestry, nasopharyngeal carcinoma is '
                               'the most likely diagnosis. These tumors are usually '
                               'nonkeratinizing and EBV-associated and spread early to the neck, '
                               'often bilaterally. Biopsy, MRI of the skull base, and staging '
                               'follow.',
                'why_wrong': ['Adenoid tissue usually regresses by adulthood and does not cause a '
                              'friable unilateral mass with a firm metastatic-looking node.',
                              'NK/T-cell lymphoma usually destroys the midline nasal cavity, '
                              'palate, and septum rather than arising as a lateral nasopharyngeal '
                              'mass.',
                              'Correct.',
                              'Angiofibroma occurs in adolescent males and arises near the '
                              'sphenopalatine foramen, not as a mass with neck nodes in an adult.'],
                'board_pearl': 'Adult unilateral middle ear effusion: examine the nasopharynx to '
                               'rule out carcinoma.',
                'curveball': 'He develops horizontal double vision on looking to the left. Which '
                             'cranial neuropathy pattern suggests skull-base extension, and why?',
                'curveball_answer': 'Abducens palsy is the most common cranial neuropathy in '
                                    'nasopharyngeal carcinoma. Tumor reaches the cavernous sinus '
                                    'and petrous apex through the foramen lacerum or by eroding '
                                    'the clivus, where CN VI is vulnerable. Involvement of CN III, '
                                    'IV, V1, and V2 indicates cavernous sinus spread, while IX-XII '
                                    'and Horner syndrome suggest parapharyngeal or jugular foramen '
                                    'spread. Any of these indicates T4 disease.'},
 'v128_hn_10': {'stem': 'A 44-year-old woman who emigrated from Guangzhou has bilateral painless '
                        'level II and V neck nodes and nasal congestion. Endoscopy shows a '
                        'nasopharyngeal mass. Biopsy shows sheets of undifferentiated tumor cells '
                        'with a dense lymphoid background; cytokeratin is positive. The '
                        'pathologist wants one additional test to confirm the diagnosis and its '
                        'etiology. Which test is most informative?',
                'choices': ['p16 immunohistochemistry with high-risk HPV testing',
                            'BRAF V600E immunostaining of the tumor cells',
                            'EBV-encoded RNA (EBER) in situ hybridization',
                            'Molecular testing for an NUT gene rearrangement'],
                'answer': 2,
                'explanation': 'Endemic nonkeratinizing nasopharyngeal carcinoma, particularly the '
                               'undifferentiated subtype, is almost always associated with '
                               'Epstein-Barr virus. EBER in situ hybridization detects EBV RNA in '
                               'nearly every tumor cell and confirms the diagnosis, and in a '
                               'metastatic node it localizes an unknown primary to the '
                               'nasopharynx. Endemic risk reflects southern Chinese ancestry, '
                               'genetic susceptibility, early EBV infection, and dietary factors '
                               'such as salted fish.',
                'why_wrong': ['HPV-associated nasopharyngeal tumors exist but are uncommon, and '
                              'p16 does not establish the classic endemic EBV-related subtype.',
                              'BRAF V600E is a marker of papillary thyroid and some other cancers, '
                              'not nasopharyngeal carcinoma.',
                              'Correct.',
                              'NUT carcinoma is a rare aggressive midline tumor; EBER is the test '
                              'that fits this endemic undifferentiated morphology.'],
                'board_pearl': 'Endemic nonkeratinizing NPC is EBV-associated; EBER in situ '
                               'hybridization confirms it.',
                'curveball': "What is the role of plasma EBV DNA in this patient's care?",
                'curveball_answer': 'Plasma EBV DNA is a validated circulating marker in endemic '
                                    'nasopharyngeal carcinoma. A high pretreatment level predicts '
                                    'worse outcome and is used in risk-adapted trials. Persistent '
                                    'or rising levels after treatment suggest residual disease or '
                                    'relapse and prompt imaging. It has also been used for '
                                    'screening in high-risk populations. Assays are not fully '
                                    'standardized, so use the same laboratory over time.'},
 'v221_hn_npc_app': {'stem': 'A 51-year-old woman has biopsy-proven nonkeratinizing nasopharyngeal '
                             'carcinoma. MRI shows a tumor in the right lateral nasopharyngeal '
                             'wall extending into the parapharyngeal space, with bulky bilateral '
                             'level II and right level V nodes up to 5 cm. PET/CT shows no distant '
                             'metastases. Renal function and hearing are normal, and performance '
                             'status is 0. What is the standard primary treatment framework?',
                     'choices': ['Endoscopic nasopharyngectomy followed by bilateral neck '
                                 'dissection',
                                 'Bilateral neck dissection followed by radiation to the primary '
                                 'site',
                                 'Gemcitabine and cisplatin alone, with radiation only at '
                                 'progression',
                                 'IMRT to the nasopharynx and both necks with concurrent '
                                 'cisplatin'],
                     'answer': 3,
                     'explanation': 'Nasopharyngeal carcinoma is very sensitive to radiation and '
                                    'chemotherapy, and its location next to the skull base makes '
                                    'primary surgery impractical. Locoregionally advanced disease '
                                    'is treated with intensity-modulated radiation to the '
                                    'nasopharynx and both necks with concurrent cisplatin. '
                                    'Induction gemcitabine-cisplatin before chemoradiation '
                                    'improves survival in locoregionally advanced disease and is '
                                    'now commonly added. Surgery is reserved for persistent or '
                                    'recurrent disease.',
                     'why_wrong': ['Primary nasopharyngectomy is used for selected small local '
                                   'recurrences, not as first treatment for bulky node-positive '
                                   'disease.',
                                   'Neck dissection first delays definitive radiation and adds '
                                   'morbidity, since radiation and chemotherapy control most nodal '
                                   'disease.',
                                   'Chemotherapy alone is for metastatic disease; curative '
                                   'treatment of nonmetastatic disease requires radiation.',
                                   'Correct.'],
                     'board_pearl': 'Locoregionally advanced NPC: radiation-based chemoradiation '
                                    'to both necks, often after induction chemotherapy.',
                     'curveball': 'How does plasma EBV DNA contribute to her pretreatment '
                                  'assessment and surveillance?',
                     'curveball_answer': 'A high pretreatment EBV DNA level adds prognostic '
                                         'information beyond TNM stage and may support intensified '
                                         'therapy such as induction chemotherapy. Clearance during '
                                         'or after treatment predicts good outcome, while '
                                         'detectable or rising levels after treatment signal '
                                         'residual or recurrent disease and prompt MRI and PET. It '
                                         'is a complement to imaging, not a replacement.'},
 'v221_hn_npc_snr': {'stem': 'A 46-year-old man completed concurrent chemoradiation for T2N2 '
                             'nasopharyngeal carcinoma 6 months ago. A 2-cm right level II node, '
                             'avid on 3-month PET, has not shrunk on repeat imaging. '
                             'Ultrasound-guided FNA shows viable carcinoma. Endoscopy and MRI show '
                             'no residual nasopharyngeal disease, and PET/CT shows no distant '
                             'spread. He is fit for surgery. What is the best next step?',
                     'choices': ['Re-irradiation of the right neck with concurrent weekly '
                                 'cisplatin',
                                 'Observation with plasma EBV DNA monitoring for 6 months',
                                 'Salvage neck dissection of the persistent regional disease',
                                 'Systemic gemcitabine-cisplatin as for metastatic disease'],
                     'answer': 2,
                     'explanation': 'Nasopharyngeal nodes can regress slowly after radiation, so '
                                    'persistent nodes are reassessed before acting. Here the node '
                                    'is persistent at 6 months and biopsy-proven, the primary is '
                                    'controlled, and there is no distant disease. Salvage neck '
                                    'dissection, comprehensive or selective based on extent, '
                                    'offers the best chance of regional control. Re-irradiation '
                                    'and systemic therapy are reserved for unresectable or distant '
                                    'disease. Prior radiation raises the risks of wound breakdown, '
                                    'nerve injury, and carotid exposure.',
                     'why_wrong': ['Re-irradiation of the neck carries high toxicity and is '
                                   'reserved for unresectable recurrence, not resectable nodal '
                                   'disease.',
                                   'Delay lets biopsy-proven viable disease progress when it is '
                                   'still resectable.',
                                   'Correct.',
                                   'Systemic therapy is for distant or unresectable disease; '
                                   'isolated nodal persistence is treated locally for cure.'],
                     'board_pearl': 'Biopsy-proven persistent neck node after NPC chemoradiation, '
                                    'primary controlled: salvage neck dissection.',
                     'curveball': 'How does the prior high-dose neck radiation change wound, '
                                  'cranial nerve, and carotid risk during salvage?',
                     'curveball_answer': 'Fibrosis obliterates tissue planes, so the vagus, '
                                         'hypoglossal, and accessory nerves are harder to identify '
                                         'and more easily injured, and wound healing is poor. Thin '
                                         'skin and devascularized tissue increase the risk of '
                                         'breakdown, and carotid exposure can lead to blowout. '
                                         'Plan incisions carefully, consider pectoralis or '
                                         'free-flap coverage of the carotid, and counsel on '
                                         'cranial nerve morbidity.'},
 'v113-hn-02': {'stem': 'A 59-year-old man with a 50 pack-year history has 2 months of solid-food '
                        'dysphagia and right ear pain with a normal otoscopic exam. Flexible '
                        'laryngoscopy shows an ulcerated tumor of the right lingual epiglottic '
                        'surface with normal true vocal fold mobility. Biopsy shows squamous cell '
                        'carcinoma. Contrast CT shows no enlarged nodes. How does his nodal risk '
                        'compare with that of an early glottic carcinoma?',
                'choices': ['Similar, since nodal risk rises only once a vocal fold is fixed',
                            'Higher, with frequent occult and bilateral spread to levels II-III',
                            'Lower, since supraglottic lymphatics are sparse and drain late',
                            'Different, with spread mainly to retropharyngeal nodes first'],
                'answer': 1,
                'explanation': 'The supraglottis has a rich lymphatic network that drains through '
                               'the thyrohyoid membrane to levels II and III, often to both sides. '
                               'Even small, clinically N0 supraglottic tumors carry substantial '
                               'occult nodal risk, so both necks are usually treated electively. '
                               'Early glottic tumors rarely metastasize because the true folds '
                               'have sparse lymphatics. Referred otalgia comes through the '
                               'internal branch of the superior laryngeal nerve and the vagal '
                               'Arnold nerve.',
                'why_wrong': ['Nodal risk in supraglottic cancer depends on lymphatic density and '
                              'subsite, not on vocal fold fixation.',
                              'Correct.',
                              'This reverses the anatomy: the supraglottis is lymphatically rich, '
                              'and the glottis is sparse.',
                              'Retropharyngeal nodes are typical first-echelon drainage for '
                              'nasopharyngeal and posterior pharyngeal wall tumors, not the '
                              'epiglottis.'],
                'board_pearl': 'Supraglottic SCC: high occult and bilateral nodal risk, so treat '
                               'both necks.',
                'curveball': 'The tumor crosses midline onto the left aryepiglottic fold. How does '
                             'that change neck management?',
                'curveball_answer': 'Midline or bilateral supraglottic tumors carry high bilateral '
                                    'occult nodal risk, so both necks should be treated electively '
                                    'at levels II-IV, by bilateral selective neck dissection with '
                                    'surgery or bilateral neck radiation with nonsurgical '
                                    'treatment. Even well-lateralized supraglottic tumors are '
                                    'often treated bilaterally, unlike most lateralized oral '
                                    'cavity tumors.'},
 'v140_hn_05': {'stem': 'A 64-year-old woman has a T2 squamous cell carcinoma centered on the '
                        'suprahyoid epiglottis, extending onto the left aryepiglottic fold, with '
                        'mobile vocal folds. Contrast CT and ultrasound show no enlarged or '
                        'suspicious nodes in either neck. She is scheduled for transoral laser '
                        'supraglottic laryngectomy with good exposure on preoperative '
                        'laryngoscopy. What is the most appropriate management of her neck?',
                'choices': ['Left selective neck dissection of levels II through IV only',
                            'Bilateral selective neck dissection of levels II through IV',
                            'Observation with surveillance imaging and examination of both sides',
                            'Bilateral comprehensive neck dissection of levels I through V'],
                'answer': 1,
                'explanation': 'Supraglottic carcinoma has rich, bilaterally communicating '
                               'lymphatics, and a midline epiglottic tumor drains to both necks. '
                               'Occult nodal rates in cN0 supraglottic cancer are high enough to '
                               'justify elective treatment of both sides. When the primary is '
                               'treated surgically, bilateral selective dissection of levels II-IV '
                               'covers the at-risk basins and provides staging for adjuvant '
                               'therapy. Level I and V are rarely involved in cN0 disease and can '
                               'be spared.',
                'why_wrong': ['A midline epiglottic primary drains bilaterally, so dissecting only '
                              'the left neck leaves the right neck at risk.',
                              'Correct.',
                              'Occult nodal risk for supraglottic carcinoma is too high to justify '
                              'observing a cN0 neck.',
                              'Levels I and V are rarely involved in cN0 supraglottic cancer, so '
                              'comprehensive dissection adds morbidity without benefit.'],
                'board_pearl': 'cN0 supraglottic SCC treated surgically: bilateral selective neck '
                               'dissection, levels II-IV.',
                'curveball': 'Which neck levels are at greatest risk for supraglottic squamous '
                             'cell carcinoma, and when would you extend the dissection?',
                'curveball_answer': 'Levels II and III carry the highest risk, followed by level '
                                    'IV. Level I and V involvement is uncommon without bulky '
                                    'disease elsewhere. Extend to levels IIb, V, or I when there '
                                    'are clinically positive nodes at multiple levels or in those '
                                    'regions, and add level VI when tumor extends into the '
                                    'subglottis or pyriform apex.'},
 'v220_hn_supra_fnd': {'stem': 'A 57-year-old man has a 1.5-cm T1 squamous cell carcinoma of the '
                               'free edge of the epiglottis, scheduled for transoral laser '
                               'excision. Both necks are negative on CT. In clinic, a medical '
                               'student notes that the man treated earlier that day, with a T1 '
                               'vocal fold cancer, needed no neck treatment, and asks why this '
                               'patient does. Which anatomic feature explains the difference?',
                       'choices': ['Conus elasticus channeling spread to paratracheal nodes',
                                   'Rich supraglottic lymphatics that cross the midline',
                                   'Absence of a pre-epiglottic space barrier to deep spread',
                                   'Shared lymphatic drainage of the vocal folds with the tongue'],
                       'answer': 1,
                       'explanation': 'The supraglottis has a dense lymphatic network with '
                                      'bilateral drainage through the thyrohyoid membrane to '
                                      'levels II-IV, so even small tumors have meaningful occult '
                                      'nodal risk. The true vocal folds have very few lymphatics, '
                                      'so T1 glottic cancers rarely metastasize and the neck can '
                                      'be observed. This difference is why elective neck '
                                      'treatment, often bilateral, is standard for supraglottic '
                                      'primaries but not for early glottic ones.',
                       'why_wrong': ['The conus elasticus is a barrier in the subglottis and does '
                                     'not explain supraglottic nodal spread.',
                                     'Correct.',
                                     'The pre-epiglottic space exists and is an important route of '
                                     'local spread, not a missing barrier that explains nodal '
                                     'risk.',
                                     'The vocal folds do not share lymphatics with the tongue; '
                                     'their sparse lymphatics explain low nodal risk.'],
                       'board_pearl': 'Small supraglottic tumors still need elective neck '
                                      'treatment; small glottic tumors usually do not.',
                       'curveball': 'Which neck levels are commonly at risk from a lateralized '
                                    'supraglottic primary, and should the opposite side still be '
                                    'treated?',
                       'curveball_answer': 'Levels II and III are at highest risk, followed by '
                                           'level IV. Even with a lateralized supraglottic '
                                           'primary, contralateral occult metastasis is common '
                                           'enough that many guidelines recommend treating both '
                                           'necks, especially for tumors involving the epiglottis '
                                           'or near midline. Some surgeons treat only the '
                                           'ipsilateral neck for strictly lateral aryepiglottic '
                                           'fold tumors, but practice varies.'},
 'v220_hn_supra_app': {'stem': 'A 68-year-old man has a T2 squamous cell carcinoma of the right '
                               'aryepiglottic fold and false vocal fold with normal vocal fold '
                               'mobility and good transoral exposure. He has severe COPD with home '
                               'oxygen, an FEV1 of 38% predicted, and two hospitalizations for '
                               'exacerbations this year. CT shows no nodes. He is being considered '
                               'for transoral supraglottic laryngectomy. Which factor most '
                               'threatens his candidacy?',
                       'choices': ['Voice Handicap Index score before treatment begins',
                                   'Possible contralateral level II node on surveillance CT',
                                   'Limited pulmonary reserve to tolerate early aspiration',
                                   'Absence of HPV association on p16 immunostaining'],
                       'answer': 2,
                       'explanation': 'Supraglottic laryngectomy removes the epiglottis and false '
                                      'folds, so patients aspirate at least temporarily while '
                                      'learning compensatory swallowing techniques. Candidates '
                                      'need enough pulmonary reserve to tolerate that aspiration, '
                                      'plus cognition and motivation for rehabilitation. Severe '
                                      'COPD with home oxygen and frequent exacerbations predicts '
                                      'aspiration pneumonia and failed swallowing recovery. '
                                      'Radiation-based treatment or, in selected cases, total '
                                      'laryngectomy may be safer options for him.',
                       'why_wrong': ['Voice outcomes are usually good after supraglottic '
                                     'laryngectomy because the true folds are preserved, so '
                                     'baseline voice scores are not decisive.',
                                     'Neck findings guide neck treatment but do not determine '
                                     'whether he can tolerate a supraglottic laryngectomy.',
                                     'Correct.',
                                     'HPV status has little relevance to laryngeal carcinoma '
                                     'management and does not determine candidacy for partial '
                                     'laryngectomy.'],
                       'board_pearl': 'Supraglottic laryngectomy requires adequate pulmonary '
                                      'reserve to survive the period of aspiration.',
                       'curveball': 'Which tumor extension or arytenoid dysfunction would make a '
                                    'conservation approach less attractive?',
                       'curveball_answer': 'Fixed vocal fold or arytenoid, cricoarytenoid joint or '
                                           'posterior commissure involvement, extension to the '
                                           'glottis or ventricle beyond what can be resected while '
                                           'preserving one functioning cricoarytenoid unit, '
                                           'thyroid cartilage invasion, deep pre-epiglottic space '
                                           'or tongue base spread, and pyriform apex involvement '
                                           'make conservation surgery less feasible. These usually '
                                           'favor chemoradiation or total laryngectomy.'},
 'v220_hn_supra_snr': {'stem': 'A 70-year-old man has T3N1 supraglottic squamous cell carcinoma '
                               'with pre-epiglottic space invasion and an intact thyroid '
                               'cartilage. Before any treatment, he aspirates thin liquids and his '
                               'own secretions on FEES, has had three aspiration pneumonias this '
                               'year, and depends on a gastrostomy tube. His FEV1 is 45% '
                               'predicted. The tumor is technically eligible for concurrent '
                               'chemoradiation. What is the best treatment recommendation?',
                       'choices': ['Concurrent cisplatin-radiation to preserve the larynx and '
                                   'native voice',
                                   'Total laryngectomy with bilateral neck dissection and adjuvant '
                                   'therapy',
                                   'Induction chemotherapy, then chemoradiation only for good '
                                   'responders',
                                   'Transoral laser supraglottic laryngectomy with bilateral neck '
                                   'dissection'],
                       'answer': 1,
                       'explanation': 'Organ preservation aims to keep a functioning larynx, not '
                                      'just an anatomically intact one. Severe aspiration, '
                                      'recurrent pneumonia, and tube dependence before treatment '
                                      'predict a nonfunctional larynx after chemoradiation, with '
                                      'high risk of fatal aspiration and later functional '
                                      'laryngectomy. ASCO and NCCN guidance support total '
                                      'laryngectomy for patients with poor baseline laryngeal '
                                      'function, which provides oncologic control and separates '
                                      'the airway from the food passage. Neck dissection and '
                                      'adjuvant therapy follow standard pathologic indications.',
                       'why_wrong': ['Chemoradiation would worsen an already failed swallow, '
                                     'likely leaving a larynx that aspirates and threatens his '
                                     'life.',
                                     'Correct.',
                                     'Induction selection still ends in chemoradiation for '
                                     'responders and does not solve his baseline aspiration '
                                     'problem.',
                                     'Supraglottic laryngectomy increases aspiration and needs '
                                     'good pulmonary reserve, which he lacks.'],
                       'board_pearl': 'Organ preservation is not function preservation: a larynx '
                                      'that aspirates before treatment favors laryngectomy.',
                       'curveball': 'How would pretreatment tracheostomy or feeding-tube '
                                    'dependence affect counseling about organ-preservation '
                                    'outcomes?',
                       'curveball_answer': 'Pretreatment tracheostomy and feeding-tube dependence '
                                           'predict poor function after chemoradiation, with a '
                                           'high chance of remaining tube- or '
                                           'tracheostomy-dependent and of later laryngectomy for '
                                           'aspiration. Counseling should explain that the larynx '
                                           'may be kept but not work, and that total laryngectomy '
                                           'may give a safer swallow, better pulmonary health, and '
                                           'good speech through tracheoesophageal voice.'},
 'v113-hn-03': {'stem': 'A 63-year-old man who worked 35 years as a furniture maker has 5 months '
                        'of right nasal obstruction, recurrent epistaxis, and decreased smell. '
                        'Endoscopy shows a friable mass high in the right nasal cavity. CT shows '
                        'an ethmoid-centered mass eroding the lamina papyracea and cribriform '
                        'plate. Biopsy shows adenocarcinoma with colonic-type glands, CDX2- and '
                        'CK20-positive. Which exposure most likely contributed?',
                'choices': ['Nickel refining', 'Formaldehyde', 'Chromium plating', 'Hardwood dust'],
                'answer': 3,
                'explanation': 'Intestinal-type sinonasal adenocarcinoma is classically associated '
                               'with occupational hardwood dust exposure, as in furniture making '
                               'and woodworking, and typically arises in the ethmoid sinuses and '
                               'superior nasal cavity. Long exposure can raise risk many times '
                               'over, and it is recognized as an occupational disease in several '
                               'countries. The colonic-type morphology and CDX2 and CK20 '
                               'positivity identify this subtype. Metastatic colorectal '
                               'adenocarcinoma should be excluded clinically.',
                'why_wrong': ['Nickel exposure is mainly linked to sinonasal squamous cell '
                              'carcinoma, not intestinal-type adenocarcinoma.',
                              'Formaldehyde has been studied mainly for nasopharyngeal carcinoma, '
                              'and its link to sinonasal adenocarcinoma is weak.',
                              'Chromium exposure causes septal perforation and is linked to '
                              'sinonasal squamous cell carcinoma rather than adenocarcinoma.',
                              'Correct.'],
                'board_pearl': 'Woodworker with an ethmoid adenocarcinoma: intestinal-type '
                               'adenocarcinoma from hardwood dust.',
                'curveball': 'Which imaging study best defines intracranial and perineural '
                             'extension for operative planning, and what does CT add?',
                'curveball_answer': 'MRI with gadolinium and fat suppression best distinguishes '
                                    'tumor from trapped secretions and shows dural enhancement, '
                                    'brain invasion, orbital involvement, and perineural spread '
                                    'along V2 or through the foramen rotundum. CT complements it '
                                    'by showing bony erosion of the cribriform plate, lamina '
                                    'papyracea, and skull base and serves for image guidance. '
                                    'PET/CT helps with nodal and distant staging.'},
 'v145_hn_17': {'stem': 'A 58-year-old woman has a biopsy-proven intestinal-type adenocarcinoma of '
                        'the left superior nasal cavity and ethmoid. CT shows thinning of the left '
                        'cribriform plate; MRI shows no dural enhancement, no orbital invasion, '
                        'and no brain involvement. Nodal and distant staging are negative. Her '
                        'surgeon proposes an endoscopic endonasal resection. Which question most '
                        'determines whether that approach is appropriate?',
                'choices': ['Whether her histology is adenocarcinoma rather than squamous',
                            'Whether she would prefer to avoid any facial incisions',
                            'Whether clear margins can be obtained at the skull base',
                            'Whether the nasoseptal flap pedicle will be preserved'],
                'answer': 2,
                'explanation': 'Endoscopic endonasal resection is acceptable for selected '
                               'sinonasal malignancies only if it achieves the same oncologic goal '
                               'as an open approach: complete resection with clear margins, '
                               'including at the skull base, orbit, and dura when needed. Outcomes '
                               'in experienced centers are comparable when patients are selected '
                               'on that basis. Histology, reconstruction, and patient preference '
                               'matter but are secondary. When endoscopic margins are not '
                               'achievable, a combined or open craniofacial approach is used.',
                'why_wrong': ['Endoscopic resection is used for many histologies; histology does '
                              'not determine whether margins can be cleared.',
                              'Patient preference matters, but it cannot justify an approach that '
                              'compromises oncologic margins.',
                              'Correct.',
                              'The nasoseptal flap helps reconstruction, but its availability does '
                              'not decide whether the tumor can be completely removed.'],
                'board_pearl': 'Endoscopic sinonasal cancer surgery is acceptable only when it '
                               'achieves the same margins as open surgery.',
                'curveball': 'A dural margin is required. What reconstructive principles reduce '
                             'the risk of postoperative CSF leak?',
                'curveball_answer': 'Use a multilayer repair with an inlay graft such as fascia '
                                    'lata or a dural substitute, an onlay layer, and a '
                                    'vascularized flap, ideally the nasoseptal flap if uninvolved '
                                    'by tumor, or a pericranial flap if not. Cover the whole '
                                    'defect with flap on bare bone, support it with packing, and '
                                    'avoid straining after surgery. Lumbar drains are debated and '
                                    'used selectively for large, high-flow defects.'},
 'v227_hn_sinonasal_fnd': {'stem': 'A 66-year-old man has 3 months of progressive left nasal '
                                   'obstruction, recurrent left epistaxis, and numbness of the '
                                   'left cheek and upper teeth. He has no history of sinusitis or '
                                   'allergy. Endoscopy shows a firm, friable, polypoid mass '
                                   'filling the left nasal cavity. The right side is normal. There '
                                   'is no neck adenopathy. What is the most appropriate next step?',
                           'choices': ['Office punch biopsy of the mass today before any imaging',
                                       'Oral prednisone and topical steroid with recheck in 4 '
                                       'weeks',
                                       'Endoscopic polypectomy in the OR to relieve the '
                                       'obstruction',
                                       'Contrast CT and MRI of the sinuses, then a planned biopsy'],
                           'answer': 3,
                           'explanation': 'Unilateral nasal mass with epistaxis and V2 numbness '
                                          'suggests malignancy with perineural or pterygopalatine '
                                          'spread. Imaging comes first: CT for bone and MRI for '
                                          'soft tissue, orbit, skull base, and nerves. It defines '
                                          'extent and excludes vascular tumors or encephalocele '
                                          'that would make an office biopsy dangerous. A '
                                          'controlled biopsy then follows. Nonsurgical treatment '
                                          'or piecemeal debulking before imaging can delay '
                                          'diagnosis or disrupt oncologic margins.',
                           'why_wrong': ['Biopsy before imaging risks heavy bleeding from a '
                                         'vascular tumor or CSF leak from an encephalocele.',
                                         'Steroids for presumed polyps delay diagnosis of a likely '
                                         'malignancy causing nerve deficits.',
                                         'Debulking before imaging and diagnosis can disrupt tumor '
                                         'margins and complicate later oncologic resection.',
                                         'Correct.'],
                           'board_pearl': 'Unilateral sinonasal mass with bleeding or numbness: '
                                          'image with CT and MRI before biopsy.',
                           'curveball': 'Which symptoms suggest orbital, skull-base, or '
                                        'named-nerve involvement in this patient?',
                           'curveball_answer': 'Diplopia, proptosis, epiphora, decreased vision, '
                                               'or globe displacement suggest orbital spread. '
                                               'Headache, CSF rhinorrhea, anosmia, or personality '
                                               'changes suggest anterior skull-base or '
                                               'intracranial extension. Cheek or upper teeth '
                                               'numbness signals V2 or infraorbital nerve spread, '
                                               'and trismus suggests pterygoid or masticator space '
                                               'invasion. Each finding raises the T stage and '
                                               'changes surgical and radiation planning.'},
 'v227_hn_sinonasal_app': {'stem': 'A 59-year-old man has a biopsy-proven squamous cell carcinoma '
                                   'of the left ethmoid and maxillary sinuses. CT shows erosion of '
                                   'the lamina papyracea and medial orbital floor with intact '
                                   'periorbita on MRI. The cribriform plate is thinned without '
                                   'dural enhancement. There are no nodes or distant metastases. '
                                   'He is fit for surgery. What is the most appropriate primary '
                                   'treatment?',
                           'choices': ['Resection with clear margins followed by postoperative '
                                       'radiation',
                                       'Definitive chemoradiation as for oropharyngeal squamous '
                                       'cell cancer',
                                       'Induction chemotherapy alone, then surveillance with '
                                       'serial MRI',
                                       'Endoscopic debulking of the nasal component and close '
                                       'surveillance'],
                           'answer': 0,
                           'explanation': 'For resectable sinonasal squamous cell carcinoma, '
                                          'standard treatment is surgery aiming for clear margins '
                                          'followed by postoperative radiation, with chemotherapy '
                                          'added for high-risk features such as positive margins. '
                                          'Planning depends on histology and the exact relation to '
                                          'the orbit, skull base, and nerves. Intact periorbita '
                                          'usually allows orbital preservation. Nonsurgical '
                                          'treatment is generally reserved for unresectable '
                                          'disease or some chemosensitive histologies, sometimes '
                                          'after induction chemotherapy.',
                           'why_wrong': ['Correct.',
                                         'Primary chemoradiation gives inferior local control for '
                                         'resectable sinonasal SCC and is used mainly for '
                                         'unresectable disease.',
                                         'Induction chemotherapy is not definitive treatment and '
                                         'is used only in selected settings before surgery or '
                                         'radiation.',
                                         'Debulking leaves gross disease and is not an oncologic '
                                         'resection, so it would compromise cure.'],
                           'board_pearl': 'Resectable sinonasal SCC: surgery with clear margins, '
                                          'then postoperative radiation.',
                           'curveball': 'What findings permit orbital preservation despite tumor '
                                        'near the orbit, and what findings mandate exenteration?',
                           'curveball_answer': 'Orbital preservation is possible when tumor erodes '
                                               'the bony wall or abuts the periorbita but does not '
                                               'invade orbital fat, because the periorbita can be '
                                               'resected and reconstructed. Exenteration is '
                                               'generally needed for invasion of orbital fat '
                                               'beyond focal areas, extraocular muscles, the '
                                               'orbital apex, the globe, or the bulbar conjunctiva '
                                               'or sclera. Decisions are made intraoperatively '
                                               'with frozen sections.'},
 'v227_hn_sinonasal_snr': {'stem': 'A 58-year-old woman has a squamous cell carcinoma of the right '
                                   'ethmoid sinus extending through the cribriform plate. MRI '
                                   'shows focal enhancement of the overlying dura without brain '
                                   'parenchymal edema, and the orbits, cavernous sinuses, and '
                                   'internal carotid arteries are free. There are no nodes or '
                                   'distant disease. She is fit and wants curative treatment. What '
                                   'is the best approach?',
                           'choices': ['Palliative radiation because dural involvement makes cure '
                                       'unlikely',
                                       'Endoscopic piecemeal debulking of the nasal part, then '
                                       'radiation',
                                       'Induction chemotherapy alone, reserving surgery for '
                                       'progression',
                                       'Craniofacial or endoscopic resection with dural margin, '
                                       'then radiation'],
                           'answer': 3,
                           'explanation': 'Focal dural involvement over the cribriform plate is '
                                          'resectable and does not make the disease incurable. '
                                          'Anterior craniofacial resection, or an endoscopic '
                                          'endonasal equivalent in experienced hands, removes the '
                                          'cribriform plate and involved dura with clear margins '
                                          'and allows multilayer skull-base repair. Postoperative '
                                          'radiation follows. Brain parenchymal invasion, '
                                          'cavernous sinus or carotid involvement, and optic '
                                          'chiasm involvement are the features that limit surgery.',
                           'why_wrong': ['Focal dural invasion is resectable with good outcomes in '
                                         'selected patients, so palliation abandons a chance of '
                                         'cure.',
                                         'Debulking the nasal part leaves tumor at the skull base '
                                         'and dura and is not an oncologic resection.',
                                         'Induction chemotherapy is used selectively, not as '
                                         'definitive therapy that delays surgery for resectable '
                                         'disease.',
                                         'Correct.'],
                           'board_pearl': 'Focal dural involvement in sinonasal cancer is '
                                          'resectable; cavernous sinus, carotid, or brain invasion '
                                          'limits surgery.',
                           'curveball': 'Which cavernous sinus, carotid, or brain findings most '
                                        'strongly limit surgical options?',
                           'curveball_answer': 'Cavernous sinus invasion, encasement of the '
                                               'internal carotid artery, optic chiasm or bilateral '
                                               'optic nerve involvement, extensive brain '
                                               'parenchymal invasion, and spread to the '
                                               'prevertebral space or nasopharynx are generally '
                                               'considered unresectable or associated with poor '
                                               'outcomes. These usually favor definitive '
                                               'radiation-based therapy, sometimes after induction '
                                               'chemotherapy, rather than craniofacial resection.'},
 'v113-hn-05': {'stem': 'A 62-year-old man completed concurrent cisplatin-radiation for T3N0 '
                        'glottic squamous cell carcinoma 4 months ago. He remains hoarse, the left '
                        'vocal fold is still fixed, and biopsy of a persistent exophytic lesion '
                        'shows squamous cell carcinoma. PET/CT shows no nodal or distant disease. '
                        'He has good pulmonary function and wants curative treatment. Which '
                        'treatment offers the best chance of cure?',
                'choices': ['Re-irradiation with cetuximab',
                            'Salvage total laryngectomy',
                            'Pembrolizumab as monotherapy',
                            'Transoral laser debulking'],
                'answer': 1,
                'explanation': 'Biopsy-proven persistent laryngeal carcinoma after chemoradiation '
                               'without distant disease is treated with salvage surgery when '
                               'resectable. With a still-fixed vocal fold, the operation is '
                               'usually total laryngectomy, since partial laryngectomy is reserved '
                               'for small, well-selected recurrences. Salvage laryngectomy gives '
                               'the best chance of durable control. Counseling should cover the '
                               'higher fistula and wound risk of an irradiated field and plans for '
                               'vascularized flap reinforcement and tracheoesophageal speech.',
                'why_wrong': ['Re-irradiation has substantial toxicity and lower control rates and '
                              'is reserved for patients who cannot undergo surgery.',
                              'Correct.',
                              'Immunotherapy is for recurrent or metastatic disease that cannot be '
                              'treated locally, not resectable persistent disease.',
                              'Debulking leaves residual tumor in a fixed, deeply invaded larynx '
                              'and cannot provide durable control.'],
                'board_pearl': 'Resectable persistent laryngeal cancer after chemoradiation: '
                               'salvage laryngectomy offers the best chance of cure.',
                'curveball': 'He agrees to surgery. How does his prior chemoradiation change your '
                             'reconstruction and pharyngocutaneous fistula planning?',
                'curveball_answer': 'After chemoradiation, fistula risk after salvage laryngectomy '
                                    'is much higher than in primary surgery. Many surgeons bring '
                                    'in nonirradiated vascularized tissue: a pectoralis major '
                                    'muscle onlay over the primary closure, or a free flap '
                                    'interposed when mucosa is insufficient for tension-free '
                                    'closure. Meta-analyses show lower fistula rates with flap '
                                    'reinforcement. Optimizing nutrition and thyroid function also '
                                    'helps.'},
 'v128_hn_08': {'stem': 'A 66-year-old man with recurrent supraglottic squamous cell carcinoma 2 '
                        'years after concurrent chemoradiation is scheduled for salvage total '
                        'laryngectomy with bilateral neck dissection. His albumin is 3.3 g/dL and '
                        'TSH is mildly elevated. You are leading the preoperative counseling. '
                        "Which complication's risk is most increased by his prior chemoradiation?",
                'choices': ['Postoperative chyle leak',
                            'Hypocalcemia after surgery',
                            'Pharyngocutaneous fistula',
                            'Late stomal stenosis'],
                'answer': 2,
                'explanation': 'Radiation causes fibrosis, small-vessel injury, and impaired '
                               'healing of the pharyngeal closure. After chemoradiation, fistula '
                               'rates after salvage laryngectomy are substantially higher than '
                               'after primary laryngectomy in most series. Hypoalbuminemia and '
                               'hypothyroidism further raise risk. Fistula prolongs '
                               'hospitalization, delays oral intake, and can expose the carotid. '
                               'Prevention includes nutrition and thyroid optimization and '
                               'vascularized flap reinforcement of the closure.',
                'why_wrong': ['Chyle leak follows thoracic duct injury during low neck dissection '
                              'and is not specifically increased by prior radiation.',
                              'Hypocalcemia relates to parathyroid handling during thyroid '
                              'surgery, not mainly to previous chemoradiation.',
                              'Correct.',
                              'Stomal stenosis occurs after laryngectomy, but prior radiation does '
                              'not raise its risk as much as it raises fistula risk.'],
                'board_pearl': 'Salvage laryngectomy after chemoradiation: counsel about high '
                               'pharyngocutaneous fistula risk.',
                'curveball': 'When would you add a pectoralis or free-tissue onlay to reduce '
                             'fistula risk, and what does the evidence show?',
                'curveball_answer': 'Many surgeons routinely add vascularized tissue after prior '
                                    'chemoradiation, especially with poor tissue quality, '
                                    'hypothyroidism, low albumin, or extended pharyngeal '
                                    'resection. A pectoralis major onlay or free-flap '
                                    'interposition brings healthy nonirradiated blood supply to '
                                    'the closure. Pooled studies show lower fistula rates, and '
                                    'fistulas that do occur are smaller and heal faster.'},
 'v135_hn_02': {'stem': 'A 59-year-old woman had concurrent chemoradiation for T2N0 supraglottic '
                        'squamous cell carcinoma. Eighteen months later she develops odynophagia, '
                        'and biopsy shows recurrent carcinoma involving the epiglottis and left '
                        'false fold with a now-fixed left vocal fold. CT shows resectable disease '
                        'and no nodes; PET shows no distant disease. She is fit and wants to be '
                        'cured. What is the best management?',
                'choices': ['Re-irradiation as the preferred curative approach for recurrence',
                            'Salvage laryngectomy, with counseling on irradiated-field wound risk',
                            'Pembrolizumab first, with surgery deferred unless she progresses',
                            'Observation and serial imaging until her airway is compromised'],
                'answer': 1,
                'explanation': 'Isolated resectable recurrence after radiation is best treated '
                               'with salvage surgery, which offers the highest chance of durable '
                               'control. With vocal fold fixation, total laryngectomy is usually '
                               'needed. Because the field is irradiated, she should be counseled '
                               'about higher risks of pharyngocutaneous fistula, wound '
                               'complications, and swallowing problems, and the operation should '
                               'include vascularized flap reinforcement. Re-irradiation and '
                               'systemic therapy are reserved for unresectable or distant disease.',
                'why_wrong': ['Re-irradiation has lower cure rates and more severe toxicity than '
                              'surgery for resectable recurrence.',
                              'Correct.',
                              'Immunotherapy is for recurrent disease that cannot be treated '
                              'locally, and delaying surgery risks losing resectability.',
                              'Waiting for airway compromise lets resectable disease progress and '
                              'turns curative surgery into an emergency.'],
                'board_pearl': 'Resectable recurrence after radiation: salvage surgery, with frank '
                               'counseling about irradiated-wound risks.',
                'curveball': 'The pharyngeal closure will be under tension in a heavily irradiated '
                             'field. What reconstructive principle lowers fistula risk?',
                'curveball_answer': 'Avoid a tight primary closure. Patch the pharyngeal defect '
                                    'with a nonirradiated vascularized free flap, such as a radial '
                                    'forearm or anterolateral thigh flap, or use a pectoralis '
                                    'major myocutaneous flap, so that the neopharynx is wide and '
                                    'closed without tension. This lowers fistula and stricture '
                                    'rates compared with a tight primary closure in irradiated '
                                    'tissue.'},
 'v134_hno_01': {'stem': 'A 61-year-old man had chemoradiation for a left base-of-tongue squamous '
                         'cell carcinoma 2 years ago. He now has a biopsy-proven 2.5-cm recurrence '
                         'in the left tongue base. CT shows tumor abutting the left internal '
                         'carotid artery over about 120 degrees. PET shows no distant disease. He '
                         'is gastrostomy-dependent with silent aspiration on a recent swallow '
                         'study. What is the most important step before offering salvage surgery?',
                 'choices': ['Book transoral robotic salvage resection within the week',
                             'Begin re-irradiation with SBRT to the tongue base recurrence',
                             'Start pembrolizumab monotherapy for the recurrent disease',
                             'Define carotid involvement, likely function, and his goals'],
                 'answer': 3,
                 'explanation': 'Salvage surgery is worthwhile only when complete resection is '
                                'realistic and the expected oncologic benefit justifies the '
                                'functional cost. Carotid proximity, prior radiation, and existing '
                                'tube dependence with aspiration mean that resection may require '
                                'carotid management and a large reconstruction and may leave him '
                                'unable to swallow, possibly needing laryngectomy. MRI or CT '
                                'angiography should define carotid and prevertebral involvement, '
                                'and a multidisciplinary team should discuss likely function, '
                                'reconstruction, and his priorities before choosing treatment.',
                 'why_wrong': ['Operating before defining carotid involvement and functional '
                               'consequences risks incomplete resection and a severely disabled '
                               'patient.',
                               'Re-irradiation near the carotid carries real risk of blowout and '
                               'is chosen only after defining surgical options and goals.',
                               'Immunotherapy may become appropriate, but choosing it before '
                               'defining resectability may forgo a curative option.',
                               'Correct.'],
                 'board_pearl': 'Before salvage surgery, define resectability, function, and the '
                                "patient's goals together.",
                 'curveball': 'Imaging now shows circumferential carotid encasement and fixation '
                              'to the prevertebral fascia. How does that alter the meaning of '
                              'resectable?',
                 'curveball_answer': 'Carotid encasement of more than 270 degrees and prevertebral '
                                     'fascia fixation generally indicate unresectable disease, '
                                     'since clear margins would require carotid resection with '
                                     'high stroke risk and are rarely achievable at the '
                                     'prevertebral fascia. Treatment then usually shifts to '
                                     'systemic therapy, such as pembrolizumab alone or with '
                                     'chemotherapy based on CPS, or carefully selected '
                                     're-irradiation, guided by his goals.'},
 'v134_hno_08': {'stem': 'A 52-year-old woman had radiation for a T2N0 right lateral oral tongue '
                         'squamous cell carcinoma 3 years ago. She now has a biopsy-proven 1.5-cm '
                         'recurrence at the original site. MRI shows no deep extension to the '
                         'floor of mouth or mandible, and PET/CT shows no nodal or distant '
                         'disease. Her swallowing is good, and a radial forearm free flap is '
                         'planned. Which feature most supports offering salvage surgery?',
                 'choices': ['A realistic chance of complete resection with good function '
                             'afterward',
                             'Prior radiation, which makes further radiation unsafe to give',
                             'Her younger age, since age alone decides surgical candidacy',
                             'Ability to debulk most of the tumor even if some gross remains'],
                 'answer': 0,
                 'explanation': 'Salvage surgery is most compelling when the recurrence can be '
                                'removed completely with clear margins and the patient can '
                                'tolerate the functional and reconstructive consequences. Here the '
                                'recurrence is small, confined, and late, with good baseline '
                                'swallowing and a feasible reconstruction, all of which predict '
                                'durable control. Prior radiation adds complexity but does not by '
                                'itself favor or exclude surgery. Incomplete resection gives '
                                'little benefit and adds morbidity.',
                 'why_wrong': ['Correct.',
                               'Prior radiation makes re-irradiation riskier, but by itself it is '
                               'not a reason to choose surgery.',
                               'Age informs fitness, but resectability and expected function '
                               'matter far more than age alone.',
                               'Leaving gross disease gives little survival benefit and adds '
                               'morbidity; salvage surgery aims for complete resection.'],
                 'board_pearl': 'Salvage surgery is justified by a realistic complete resection '
                                'with acceptable function.',
                 'curveball': 'What factors would make you favor systemic therapy or '
                              're-irradiation instead of salvage surgery?',
                 'curveball_answer': 'Favor nonsurgical options when clear margins are unlikely, '
                                     'such as with carotid encasement, prevertebral or skull-base '
                                     'involvement, or extensive soft-tissue spread. Also favor '
                                     'them with distant metastases, very early recurrence after '
                                     'treatment, poor performance status or frailty, expected '
                                     "severe functional loss, or the patient's preference after "
                                     'informed discussion.'},
 'v225_hn_salv_fnd': {'stem': 'A 63-year-old man is undergoing salvage total laryngectomy 14 '
                              'months after concurrent chemoradiation for laryngeal squamous cell '
                              'carcinoma. During the operation the resident notes woody, pale '
                              'tissue, obliterated planes around the carotid sheath, and slow '
                              'bleeding from the cut edges. Afterward she asks why salvage carries '
                              'more wound and fistula complications than primary surgery. Which '
                              'mechanism best explains this?',
                      'choices': ['Radiation-induced hypothyroidism acting as the only factor',
                                  'Obliterative endarteritis and fibrosis that impair perfusion',
                                  'Larger bacterial load carried in by the recurrent tumor',
                                  'Long-lasting neutropenia caused by the prior cisplatin'],
                      'answer': 1,
                      'explanation': 'Radiation causes small-vessel endarteritis, fibrosis, and '
                                     'loss of fibroblasts and stem cells, leaving tissue '
                                     'hypovascular, hypocellular, and hypoxic. Such tissue heals '
                                     'poorly, so pharyngeal closures break down, wounds dehisce, '
                                     'and vessels can become exposed. Fibrosis also obliterates '
                                     'surgical planes, making dissection harder and nerve or '
                                     'vessel injury more likely. Bringing in nonirradiated '
                                     'vascularized tissue addresses this directly.',
                      'why_wrong': ['Hypothyroidism adds fistula risk and should be corrected, but '
                                    'it is one contributor rather than the main mechanism.',
                                    'Correct.',
                                    'Recurrent tumor does not markedly raise wound bacterial load; '
                                    'poor healing of irradiated tissue is the key problem.',
                                    'Cisplatin-induced neutropenia resolves within weeks and is '
                                    'not present 14 months after treatment.'],
                      'board_pearl': 'Irradiated tissue is hypovascular, hypocellular, and '
                                     'hypoxic, so salvage wounds heal poorly.',
                      'curveball': 'She is drafting a risk checklist for the next salvage case. '
                                   'Which preoperative factors predict higher pharyngocutaneous '
                                   'fistula risk?',
                      'curveball_answer': 'Prior chemoradiation more than radiation alone, a '
                                          'shorter interval since radiation, hypothyroidism, low '
                                          'albumin and hemoglobin, diabetes, COPD, prior '
                                          'tracheostomy, positive margins, extended pharyngeal '
                                          'resection, and concurrent neck dissection all predict '
                                          'higher fistula risk. Correcting thyroid function and '
                                          'nutrition and planning flap reinforcement address the '
                                          'modifiable factors.'},
 'v225_hn_salv_snr': {'stem': 'A 79-year-old man has a biopsy-proven 2-cm recurrence in the left '
                              'pyriform sinus 10 months after chemoradiation. It is technically '
                              'resectable but would require total laryngopharyngectomy with '
                              'free-flap reconstruction. He uses home oxygen for COPD, has an '
                              'albumin of 2.8 g/dL, spends most of the day seated, and says '
                              'staying at home with his wife matters most. What should determine '
                              'whether salvage surgery is offered?',
                      'choices': ['Realistic cure odds weighed against operative risk and his '
                                  'wishes',
                                  'Technical resectability on imaging, since that alone means '
                                  'surgery',
                                  'Any recurrent tumor needing re-irradiation, which is less '
                                  'morbid',
                                  'A transoral partial resection to avoid free-flap '
                                  'reconstruction'],
                      'answer': 0,
                      'explanation': 'Technical resectability is necessary but not sufficient. '
                                     'Salvage laryngopharyngectomy in a frail patient with severe '
                                     'COPD, malnutrition, and poor performance status carries high '
                                     'perioperative mortality, long hospitalization, and difficult '
                                     'rehabilitation, while early recurrence lowers the chance of '
                                     'cure. The decision should weigh realistic cure against '
                                     'operative risk, expected function, and his stated '
                                     'priorities. Palliative systemic therapy or supportive care '
                                     'may better match his goals.',
                      'why_wrong': ['Correct.',
                                    'Resectability alone ignores frailty, operative risk, and '
                                    'expected function, which all shape the net benefit of '
                                    'surgery.',
                                    'Re-irradiation carries its own serious toxicity and is not '
                                    'automatically safer than surgery.',
                                    'A limited resection would likely leave tumor in an irradiated '
                                    'field without avoiding the main risks.'],
                      'board_pearl': 'Salvage surgery: weigh cure probability against operative '
                                     'risk, function, and patient goals.',
                      'curveball': 'When would nonsurgical palliation or systemic therapy be the '
                                   'better option despite resectability?',
                      'curveball_answer': 'When perioperative mortality is high, when early '
                                          'recurrence predicts a low chance of durable cure, when '
                                          'expected function after surgery is poor, or when the '
                                          'patient prioritizes time at home over aggressive '
                                          'treatment. Options include pembrolizumab alone or with '
                                          'chemotherapy based on CPS per KEYNOTE-048, palliative '
                                          'radiation, or best supportive care with hospice '
                                          'involvement.'},
 'v225_hn_salv_postcrt_app': {'stem': 'A 61-year-old man completed chemoradiation 13 weeks ago for '
                                      'p16-positive tonsil carcinoma with a 3.5-cm right level II '
                                      'node. Examination is reassuring. PET/CT shows complete '
                                      'metabolic response at the primary and in the neck, but CT '
                                      'shows a residual 1.2-cm right level II node without uptake. '
                                      'What is the best management of the neck?',
                              'choices': ['Clinical and imaging surveillance without neck '
                                          'dissection',
                                          'Planned neck dissection given the residual node on the '
                                          'CT',
                                          'Ultrasound-guided FNA of the residual node before any '
                                          'plan',
                                          'Repeat PET/CT in 4 weeks to confirm complete response'],
                              'answer': 0,
                              'explanation': 'After chemoradiation, neck management is guided by '
                                             'response on PET/CT at about 12 weeks, not by '
                                             'pretreatment nodal stage. The PET-NECK trial showed '
                                             'that PET-guided surveillance gave similar survival '
                                             'to planned neck dissection with far fewer '
                                             'operations. A complete metabolic response has a very '
                                             'high negative predictive value, even when a small '
                                             'node remains on CT, since residual nodes often '
                                             'contain only fibrosis. Equivocal or persistent '
                                             'uptake calls for further assessment.',
                              'why_wrong': ['Correct.',
                                            'A small residual node without PET uptake usually '
                                            'contains only fibrosis, so planned dissection would '
                                            'mostly be unnecessary surgery.',
                                            'FNA of a PET-negative residual node has low yield and '
                                            'is not needed when PET shows complete response.',
                                            'Very early repeat PET adds cost and delay without '
                                            'improving the high negative predictive value of the '
                                            'current scan.'],
                              'board_pearl': 'Complete metabolic response on 12-week PET/CT: '
                                             'observe the neck rather than dissect.',
                              'curveball': 'If the 12-week PET/CT were equivocal rather than '
                                           'clearly positive or negative, why is short-interval '
                                           'reassessment often preferable to reflex neck '
                                           'dissection?',
                              'curveball_answer': 'Post-radiation inflammation can cause low-grade '
                                                  'uptake that is not tumor, so equivocal scans '
                                                  'have a low positive predictive value. Repeat '
                                                  'PET/CT or ultrasound-guided FNA in several '
                                                  'weeks clarifies most cases, and many resolve '
                                                  'without surgery. Neck dissection is reserved '
                                                  'for persistent or rising uptake, enlarging '
                                                  'nodes, or biopsy-proven disease, which avoids '
                                                  'unnecessary surgery in an irradiated neck.'},
 'v128_hn_01': {'stem': 'A 58-year-old man who never smoked has a 3.2-cm squamous cell carcinoma '
                        'of the left palatine tonsil with strong, diffuse p16 staining and '
                        'positive high-risk HPV testing. CT shows two left level II nodes, 2.5 cm '
                        'and 1.8 cm, without imaging signs of extranodal extension. PET/CT shows '
                        'no distant disease. A rotating medical student stages him as stage IVA. '
                        'Which staging principle corrects this?',
                'choices': ['Two ipsilateral nodes are classified N1 in every oropharyngeal '
                            'staging system',
                            'HPV-associated tumors use a separate system with lower stage groups',
                            'p16 status changes prognosis but leaves AJCC stage group unchanged',
                            'Tonsil primaries are staged with the oral cavity criteria instead'],
                'answer': 1,
                'explanation': 'Since AJCC 8, HPV-associated oropharyngeal carcinoma has its own '
                               'staging system because its prognosis is much better than that of '
                               'HPV-negative disease. Ipsilateral nodes up to 6 cm without '
                               'extranodal extension are clinical N1 in that system, so this '
                               'patient falls into an early stage group, whereas the p16-negative '
                               'system would call him N2b, stage IVA. AJCC Version 9 keeps the '
                               'separate HPV-associated system and makes extranodal extension the '
                               'key nodal modifier.',
                'why_wrong': ['In the p16-negative system, multiple ipsilateral nodes are N2b; '
                              'only the HPV-associated system groups them as N1.',
                              'Correct.',
                              'p16 status determines which staging system is used, and that '
                              'changes both the N category and the stage group.',
                              'The tonsil is an oropharyngeal subsite and is never staged with '
                              'oral cavity criteria.'],
                'board_pearl': 'HPV-associated oropharyngeal cancer has its own staging system '
                               'with lower stage groups than p16-negative disease.',
                'curveball': 'How would the nodal classification differ if this tumor were '
                             'p16-negative?',
                'curveball_answer': 'In the p16-negative oropharynx system, a single ipsilateral '
                                    'node 3 cm or less is N1, a single node over 3 to 6 cm is N2a, '
                                    'multiple ipsilateral nodes up to 6 cm are N2b, and bilateral '
                                    'or contralateral nodes are N2c. Any node over 6 cm or with '
                                    'clinical extranodal extension is N3. His two ipsilateral '
                                    'nodes would therefore be N2b, making him stage IVA.'},
 'v143_hno_02': {'stem': 'A 54-year-old man who never smoked has a 1.8-cm p16-positive squamous '
                         'cell carcinoma of the right tonsil and a 3-cm cystic right level II '
                         'node. PET/CT shows no distant disease. He read that HPV-related cancers '
                         'have an excellent prognosis and asks whether he can have lighter '
                         'treatment, such as reduced-dose radiation or cetuximab instead of '
                         'cisplatin. Which recommendation is most appropriate?',
                 'choices': ['Reduced-dose radiation alone, since p16 positivity predicts cure',
                             'Standard surgery or radiation-based therapy, with de-escalation on '
                             'trials',
                             'Radiation with cetuximab to avoid the toxicity of cisplatin',
                             'Active surveillance, as HPV-associated cancers often regress'],
                 'answer': 1,
                 'explanation': 'HPV-associated oropharyngeal carcinoma has a better prognosis and '
                                'its own staging system, but treatment is still based on extent '
                                'and risk, using transoral surgery with neck dissection or '
                                'radiation with or without cisplatin. Trials of de-escalation have '
                                'produced cautionary results: RTOG 1016 and De-ESCALaTE showed '
                                'that replacing cisplatin with cetuximab led to worse outcomes. '
                                'Reduced-dose approaches remain investigational and should be '
                                'offered within clinical trials.',
                 'why_wrong': ['Reduced-dose radiation has not replaced standard dosing outside '
                               'trials, and p16 positivity does not guarantee cure.',
                               'Correct.',
                               'RTOG 1016 and De-ESCALaTE showed worse tumor control with '
                               'cetuximab than with cisplatin, without less toxicity.',
                               'HPV-associated carcinoma does not regress spontaneously; untreated '
                               'disease progresses.'],
                 'board_pearl': 'HPV-positive OPSCC: better prognosis, but standard treatment; '
                                'de-escalation belongs in trials.',
                 'curveball': 'If transoral surgery reveals extranodal extension or positive '
                              'margins, how does that alter adjuvant therapy?',
                 'curveball_answer': 'Positive margins and extranodal extension are high-risk '
                                     'features that support postoperative radiation with '
                                     'concurrent cisplatin in fit patients, even in HPV-associated '
                                     'disease. Intermediate features such as perineural or '
                                     'lymphovascular invasion or multiple nodes usually call for '
                                     'radiation alone. Trials such as ECOG 3311 and PATHOS are '
                                     'testing whether some HPV-positive patients can safely '
                                     'receive less adjuvant treatment.'},
 'v219_hn_hpv_snr': {'stem': 'A 52-year-old fit man has a 1.5-cm p16-positive squamous cell '
                             'carcinoma of the left tonsil, well lateralized and with good '
                             'transoral exposure. CT shows a 3.5-cm matted left level II nodal '
                             'mass with irregular margins invading the sternocleidomastoid muscle. '
                             'PET/CT shows no distant disease. He asks whether transoral robotic '
                             'surgery would let him avoid chemotherapy. What is the best treatment '
                             'recommendation?',
                     'choices': ['Definitive chemoradiation, as surgery would likely need adjuvant '
                                 'chemo',
                                 'TORS and neck dissection followed by adjuvant radiation alone',
                                 'TORS and neck dissection, expecting no further treatment after',
                                 'Induction chemotherapy followed by TORS only for good '
                                 'responders'],
                     'answer': 0,
                     'explanation': 'Surgery and definitive chemoradiation are both appropriate '
                                    'for many HPV-associated oropharyngeal cancers, but the '
                                    'expected pathology should guide the choice. Imaging signs of '
                                    'extranodal extension, such as a matted nodal mass invading '
                                    'muscle, predict pathologic extranodal extension, which '
                                    'mandates postoperative cisplatin-radiation. Surgery would '
                                    'then lead to trimodality therapy with more dysphagia and no '
                                    'survival gain. Definitive chemoradiation avoids that and is '
                                    'the better recommendation here.',
                     'why_wrong': ['Correct.',
                                   'Pathologic extranodal extension is very likely here, and it '
                                   'calls for concurrent cisplatin rather than radiation alone.',
                                   'With likely extranodal extension, adjuvant treatment will '
                                   'almost certainly be needed after surgery.',
                                   'Induction chemotherapy followed by surgery is not a standard '
                                   'approach and does not remove the need for adjuvant therapy.'],
                     'board_pearl': 'If surgery for HPV-positive OPSCC will likely need adjuvant '
                                    'chemoradiation, favor definitive chemoradiation instead.',
                     'curveball': 'Which postoperative pathologic findings most strongly escalate '
                                  'adjuvant therapy after transoral resection?',
                     'curveball_answer': 'Positive margins and extranodal extension call for '
                                         'postoperative radiation with concurrent cisplatin. Close '
                                         'margins, perineural invasion, lymphovascular invasion, '
                                         'multiple positive nodes, and pT3-T4 disease are '
                                         'intermediate features that usually prompt radiation '
                                         'alone. Trials such as ECOG 3311 and PATHOS are defining '
                                         'how far adjuvant treatment can be reduced in '
                                         'HPV-positive patients.'},
 'v128_hn_03': {'stem': 'A 55-year-old man with p16-positive tonsil carcinoma and a 2-cm left '
                        'level IIA node is undergoing transoral resection with left selective neck '
                        'dissection of levels II-IV, including level IIB. Three weeks after '
                        'surgery he has aching left shoulder pain and cannot fully abduct his arm, '
                        'with mild winging of the scapula on the left. Which operative step most '
                        'likely caused this deficit?',
                'choices': ['Clearing nodal tissue above and behind the accessory nerve',
                            'Dividing the omohyoid muscle where it crosses the jugular',
                            'Ligating the common facial vein at its junction with the IJV',
                            'Separating the specimen from the carotid sheath in level III'],
                'answer': 0,
                'explanation': 'Level IIB, the submuscular recess, lies above and behind the '
                               'spinal accessory nerve, bounded by the posterior belly of the '
                               'digastric and the sternocleidomastoid. Clearing it requires '
                               'lifting or skeletonizing the nerve, and traction or '
                               'devascularization of the nerve can weaken the trapezius, causing '
                               'shoulder pain, limited abduction, and scapular winging. Gentle '
                               'handling and early physical therapy reduce the deficit, and most '
                               'traction injuries recover over months.',
                'why_wrong': ['Correct.',
                              'The omohyoid crosses the IJV in levels III-IV, far below the course '
                              'of the accessory nerve in level II.',
                              'The common facial vein enters the IJV in level IIA anterior to the '
                              'nerve and is not near its course in level IIB.',
                              'The carotid sheath dissection in level III is anterior and medial '
                              'to the accessory nerve, which runs in level II and V.'],
                'board_pearl': 'Level IIB dissection puts the spinal accessory nerve at risk '
                               'through traction and skeletonization.',
                'curveball': 'Which primary sites most strongly influence whether level IIB must '
                             'be routinely included?',
                'curveball_answer': 'Oropharyngeal primaries, especially with a positive level IIA '
                                    'node, carry enough IIB risk to justify routine dissection, as '
                                    'do posterior scalp, parotid, and nasopharyngeal-type '
                                    'drainage. For cN0 oral cavity, larynx, and hypopharynx '
                                    'cancers, isolated IIB metastasis is uncommon, and many '
                                    'surgeons omit IIB to protect the accessory nerve, though '
                                    'practice varies.'},
 'v140_hn_03': {'stem': 'A 60-year-old man is undergoing left modified radical neck dissection for '
                        'metastatic laryngeal squamous cell carcinoma. While clearing level IV '
                        'near the junction of the internal jugular and subclavian veins, the '
                        'resident notes clear fluid that turns milky after the anesthesiologist '
                        'gives a Valsalva maneuver. A thin-walled structure is seen leaking behind '
                        'the jugular vein. What is the best intraoperative response?',
                'choices': ['Close over a suction drain and start a fat-free diet after surgery',
                            'Ligate or clip the duct, then retest with Valsalva before closing',
                            'Coagulate the leaking lymphatic channels with bipolar cautery',
                            'Pack the area with oxidized cellulose and close without a drain'],
                'answer': 1,
                'explanation': 'Milky fluid near the left venous angle that increases with '
                               'Valsalva indicates a thoracic duct injury. Recognizing it during '
                               'surgery is the best opportunity for repair. The duct and its '
                               'branches should be ligated or clipped with care, sometimes '
                               'reinforced with a local muscle flap or sealant, and a repeat '
                               'Valsalva should confirm that the leak has stopped before closure. '
                               'A drain is still placed so that a later leak can be detected.',
                'why_wrong': ['Leaving a known leak for conservative care risks a high-output '
                              'chyle leak, malnutrition, and wound problems.',
                              'Correct.',
                              'Cautery on the thin-walled duct often enlarges the tear rather than '
                              'sealing it.',
                              'Packing without control does not seal the duct, and closing without '
                              'a drain hides a later leak.'],
                'board_pearl': 'Thoracic duct injury seen at surgery: ligate it and confirm with '
                               'Valsalva before closing.',
                'curveball': 'A low-output chyle leak appears on postoperative day 2. What diet '
                             'and drain strategy would you use?',
                'curveball_answer': 'Confirm chyle with drain triglyceride above 100 mg/dL or '
                                    'chylomicrons. For low output, keep the drain, switch to a '
                                    'fat-free or medium-chain triglyceride diet or enteral '
                                    'formula, and apply pressure dressings. Octreotide may help. '
                                    'Persistent or high output, often above 500-1000 mL per day, '
                                    'prompts lymphangiography with thoracic duct embolization or '
                                    'surgical re-exploration.'},
 'v219_hn_neck_app': {'stem': 'A 58-year-old woman has a cT2 squamous cell carcinoma of the right '
                              'buccal mucosa with a depth of invasion of 6 mm, well away from '
                              'midline. Her neck is negative on examination and contrast CT. Wide '
                              'local excision with a radial forearm free flap is planned, and the '
                              'tumor board recommends elective treatment of the ipsilateral neck. '
                              'Which neck operation is most appropriate?',
                      'choices': ['Selective neck dissection of right levels II through IV',
                                  'Selective neck dissection of the right levels I through III',
                                  'Modified radical neck dissection of right levels I to V',
                                  'Excisional biopsy of the largest right level IB lymph node'],
                      'answer': 1,
                      'explanation': 'Elective selective neck dissection removes the nodal levels '
                                     'at greatest risk for the primary site while preserving the '
                                     'spinal accessory nerve, internal jugular vein, and '
                                     'sternocleidomastoid. For lateral oral cavity cancer, '
                                     'first-echelon drainage is to levels I, II, and III, so the '
                                     'supraomohyoid dissection of levels I-III is standard, with '
                                     'level IV added by some surgeons for oral tongue. It stages '
                                     'the neck and exposes recipient vessels for the free flap.',
                      'why_wrong': ['Levels II-IV is the pattern used for larynx and hypopharynx; '
                                    'it omits level I, which is the first echelon for buccal '
                                    'cancer.',
                                    'Correct.',
                                    'A comprehensive dissection of all five levels adds morbidity '
                                    'without benefit in a clinically negative neck.',
                                    'Excising a single node misses occult disease elsewhere and '
                                    'does not stage the neck reliably.'],
                      'board_pearl': 'cN0 lateral oral cavity cancer: elective selective neck '
                                     'dissection of levels I-III.',
                      'curveball': 'Which nodal levels are classically included in an elective '
                                   'dissection for oral tongue cancer, and why do some surgeons '
                                   'add level IV?',
                      'curveball_answer': 'The supraomohyoid dissection of levels I-III is classic '
                                          'for oral cavity cancer. For oral tongue, some surgeons '
                                          'add level IV because skip metastases to levels III or '
                                          'IV without level I or II involvement have been '
                                          'reported. Others reserve level IV for clinically '
                                          'positive necks. Practice varies, and evidence on '
                                          'routine level IV dissection is mixed.'},
 'v219_hn_neck_snr': {'stem': 'A 63-year-old man is undergoing left neck dissection for '
                              'supraglottic squamous cell carcinoma with a 4-cm level III node. In '
                              'the operating room, the node is densely adherent to and invading '
                              'the wall of the left internal jugular vein over 3 cm. It separates '
                              'cleanly from the spinal accessory nerve, sternocleidomastoid, and '
                              'carotid artery. The right internal jugular vein is intact. What is '
                              'the best oncologic step?',
                      'choices': ['Resect the involved jugular segment and spare the other '
                                  'structures',
                                  'Convert to radical neck dissection, removing nerve, muscle, and '
                                  'vein',
                                  'Shave the node off the vein and mark the area for radiation '
                                  'boost',
                                  'Abort the dissection and refer him for definitive '
                                  'chemoradiation'],
                      'answer': 0,
                      'explanation': 'Modern neck dissection is tailored to the disease. When a '
                                     'node directly invades the internal jugular vein, the '
                                     'involved vein is resected en bloc with the specimen to '
                                     'achieve clear margins, while uninvolved nonlymphatic '
                                     'structures such as the accessory nerve and '
                                     'sternocleidomastoid are preserved. This is a modified '
                                     'radical neck dissection with jugular sacrifice. Because the '
                                     'opposite jugular vein is intact, unilateral ligation is '
                                     'safe.',
                      'why_wrong': ['Correct.',
                                    'Removing an uninvolved accessory nerve and '
                                    'sternocleidomastoid adds shoulder and cosmetic morbidity '
                                    'without oncologic benefit.',
                                    'Shaving tumor off the vein leaves gross or microscopic '
                                    'disease and risks a positive margin.',
                                    'Invasion of the jugular vein does not make the neck '
                                    'unresectable, so stopping forfeits a complete resection.'],
                      'board_pearl': 'Sacrifice only the nonlymphatic structures that tumor '
                                     'invades; preserve the rest.',
                      'curveball': 'How would carotid encasement or skull-base fixation alter '
                                   'resectability and multidisciplinary planning?',
                      'curveball_answer': 'Carotid encasement of more than 270 degrees, fixation '
                                          'to the prevertebral fascia, or skull-base invasion are '
                                          'usually considered unresectable, because clear margins '
                                          'would need carotid resection with high stroke risk. '
                                          'Such patients are usually treated with definitive '
                                          'chemoradiation. Carotid resection with bypass is '
                                          'reserved for very selected cases after balloon '
                                          'occlusion testing.'},
 'v128_hn_05': {'stem': 'A 59-year-old man has T3N1 transglottic squamous cell carcinoma with a '
                        'fixed right vocal fold, no cartilage penetration, and good swallowing. He '
                        'is fit for any treatment and wants to keep his larynx. While reviewing '
                        'nonsurgical options, he asks what the RTOG 91-11 trial showed. Which '
                        'statement accurately summarizes its main result?',
                'choices': ['Induction chemotherapy then radiation best preserved the larynx',
                            'Concurrent chemoradiation improved overall survival over radiation',
                            'Radiation alone matched concurrent therapy for locoregional control',
                            'Concurrent cisplatin-radiation gave the best larynx preservation'],
                'answer': 3,
                'explanation': 'RTOG 91-11 randomized patients with stage III-IV glottic or '
                               'supraglottic cancer, excluding large T4 tumors, to induction '
                               'cisplatin-fluorouracil followed by radiation, concurrent '
                               'cisplatin-radiation, or radiation alone. Concurrent therapy gave '
                               'the highest larynx preservation and locoregional control, at the '
                               'cost of more acute toxicity. Overall survival did not differ '
                               'significantly, and the 10-year analysis showed more deaths not '
                               'attributed to cancer with concurrent therapy. Salvage laryngectomy '
                               'remained essential for failures.',
                'why_wrong': ['Induction followed by radiation preserved the larynx less often '
                              'than concurrent therapy, though laryngectomy-free survival was '
                              'similar long term.',
                              'Overall survival did not differ significantly between arms, and '
                              'late deaths unrelated to cancer were higher with concurrent '
                              'therapy.',
                              'Locoregional control was better with concurrent therapy than with '
                              'radiation alone.',
                              'Correct.'],
                'board_pearl': 'RTOG 91-11: concurrent cisplatin-radiation gives the best larynx '
                               'preservation, not better survival.',
                'curveball': 'Which patients are poor candidates for nonsurgical larynx '
                             'preservation despite technically resectable disease?',
                'curveball_answer': 'Poor candidates include those with T4a disease with cartilage '
                                    'destruction or extralaryngeal spread, pretreatment aspiration '
                                    'or tube dependence, tracheostomy for airway obstruction, a '
                                    'nonfunctional larynx, or poor pulmonary reserve. Patients '
                                    'unlikely to complete treatment or attend surveillance are '
                                    'also poor candidates. For them, total laryngectomy usually '
                                    'offers better cure and function.'},
 'v140_hn_04': {'stem': 'A 64-year-old man has laryngeal squamous cell carcinoma with a fixed left '
                        'vocal fold. CT shows tumor through the outer cortex of the left thyroid '
                        'lamina into the strap muscles, with a 2-cm left level III node. On FEES '
                        'he aspirates thin liquids, and he has lost 8 kg. PET shows no distant '
                        'disease. He is medically fit. What is the best primary treatment?',
                'choices': ['Concurrent cisplatin-radiation with salvage surgery if needed',
                            'Induction docetaxel-cisplatin-fluorouracil, then radiation',
                            'Total laryngectomy with neck dissection and adjuvant therapy',
                            'Transoral laser resection followed by adjuvant chemoradiation'],
                'answer': 2,
                'explanation': 'Tumor through the outer cortex of the thyroid cartilage into the '
                               'strap muscles is T4a. Cartilage-penetrating, bulky T4a tumors were '
                               'largely excluded from organ-preservation trials, respond poorly to '
                               'chemoradiation, and often leave a nonfunctional larynx. With '
                               'aspiration and weight loss already present, total laryngectomy '
                               'with neck dissection, followed by adjuvant radiation or '
                               'chemoradiation, offers better cure and function. NCCN prefers '
                               'surgery for this presentation.',
                'why_wrong': ['Chemoradiation for cartilage-penetrating T4a disease gives lower '
                              'control and risks a nonfunctioning aspirating larynx.',
                              'Induction chemotherapy still relies on radiation for responders and '
                              'does not suit T4a disease with existing aspiration.',
                              'Correct.',
                              'Transoral resection cannot clear tumor through the thyroid '
                              'cartilage into the strap muscles.'],
                'board_pearl': 'T4a larynx with cartilage penetration or poor function: primary '
                               'total laryngectomy is favored.',
                'curveball': 'How would a T3 tumor with good swallowing and no cartilage '
                             'penetration change the discussion?',
                'curveball_answer': 'A T3 tumor with good function is a strong candidate for organ '
                                    'preservation, usually concurrent cisplatin-radiation, or '
                                    'induction chemotherapy followed by radiation for responders. '
                                    'Survival is similar to primary total laryngectomy when '
                                    'salvage surgery is available. Selected patients may instead '
                                    'have partial laryngectomy. The choice rests on patient '
                                    'preference, comorbidity, and expected function.'},
 'v221_hn_pres_app': {'stem': 'A 66-year-old man has T3N2b glottic squamous cell carcinoma with '
                              'transglottic spread and no cartilage penetration. Two weeks ago he '
                              'needed an urgent tracheostomy for stridor. FEES shows aspiration of '
                              'his own secretions, he has had one pneumonia, and he takes only '
                              'small amounts by mouth. He is otherwise fit. Which factor most '
                              'weighs against nonsurgical larynx preservation?',
                      'choices': ['N2b nodal disease made up of several ipsilateral nodes under 6 '
                                  'cm',
                                  'Airway obstruction and aspiration showing poor baseline '
                                  'function',
                                  'His age of 66 years at the time of the treatment recommendation',
                                  'Transglottic spread of tumor without thyroid cartilage '
                                  'penetration'],
                      'answer': 1,
                      'explanation': 'The aim of larynx preservation is a larynx that breathes, '
                                     'protects the airway, and allows swallowing. Pretreatment '
                                     'tracheostomy for obstruction and aspiration of secretions '
                                     'mean the larynx is already failing. After chemoradiation, '
                                     'such patients often remain tracheostomy- and tube-dependent '
                                     'or need later laryngectomy for aspiration. ASCO guidance '
                                     'lists poor baseline function as a reason to favor total '
                                     'laryngectomy despite technical eligibility.',
                      'why_wrong': ['Nodal disease is managed with neck treatment in either '
                                    'approach and does not itself exclude larynx preservation.',
                                    'Correct.',
                                    'Age in a fit patient does not determine eligibility; '
                                    'laryngeal function and comorbidity matter more.',
                                    'Transglottic spread without cartilage penetration is still T3 '
                                    'and does not by itself exclude organ preservation.'],
                      'board_pearl': 'Pretreatment tracheostomy and aspiration predict a '
                                     'nonfunctional preserved larynx.',
                      'curveball': 'Which T4 features or cartilage and extralaryngeal patterns '
                                   'tend to shift the discussion toward total laryngectomy?',
                      'curveball_answer': 'Thyroid cartilage penetration through the outer cortex, '
                                          'extralaryngeal spread into the strap muscles, thyroid '
                                          'gland, or esophagus, extensive base-of-tongue '
                                          'involvement, and substantial subglottic extension to '
                                          'the cricoid all favor total laryngectomy. These tumors '
                                          'respond poorly to chemoradiation and leave a '
                                          'nonfunctional larynx more often.'},
 'v221_hn_pres_snr': {'stem': 'A 63-year-old woman has bulky laryngeal squamous cell carcinoma '
                              'with destruction of the thyroid cartilage and extension into the '
                              'anterior neck soft tissue. She has had progressive dysphagia with '
                              'aspiration of liquids for 2 months. She says she would rather die '
                              'than lose her voice and asks for chemoradiation. She is fit and has '
                              'no distant disease. What is the best counseling approach?',
                      'choices': ['Explain that laryngectomy likely offers better cure and '
                                  'function',
                                  'Agree to chemoradiation because her preference outweighs tumor '
                                  'extent',
                                  'Offer induction chemotherapy as a trial of tumor responsiveness',
                                  'Recommend partial laryngectomy as a compromise between options'],
                      'answer': 0,
                      'explanation': 'Shared decision-making requires honest information. '
                                     'Cartilage destruction with extralaryngeal spread is T4a '
                                     'disease, which responds poorly to chemoradiation, and her '
                                     'aspiration predicts a preserved larynx that may not work. '
                                     'Total laryngectomy offers better local control and safer '
                                     'swallowing, and modern tracheoesophageal voice restoration '
                                     'lets most patients speak well. Her wish to keep her voice '
                                     'should be explored and respected. Chemoradiation can be '
                                     'offered after informed refusal, with salvage surgery '
                                     'planned.',
                      'why_wrong': ['Correct.',
                                    'Respecting preference does not mean withholding the expected '
                                    'cure and functional outcomes of each option.',
                                    'Induction selection was studied mainly in tumors without '
                                    'extensive cartilage destruction and does not fix her baseline '
                                    'aspiration.',
                                    'Partial laryngectomy cannot clear tumor that has destroyed '
                                    'the thyroid cartilage and spread outside the larynx.'],
                      'board_pearl': 'Counsel T4a laryngeal cancer honestly: laryngectomy often '
                                     'gives better cure and function than chemoradiation.',
                      'curveball': 'Years later, a disease-free patient after chemoradiation '
                                   'aspirates chronically. How would that reopen the surgical '
                                   'discussion?',
                      'curveball_answer': 'A disease-free but chronically aspirating, tube- or '
                                          'tracheostomy-dependent larynx is a functional failure. '
                                          'After restaging excludes recurrence and rehabilitation '
                                          'is exhausted, functional total laryngectomy or another '
                                          'aspiration-prevention procedure can be offered to stop '
                                          'pneumonias, allow oral intake, and restore speech '
                                          'through a tracheoesophageal prosthesis.'},
 'v128_hn_09': {'stem': 'A 47-year-old woman has composite resection and right neck dissection for '
                        'a pT2 squamous cell carcinoma of the right floor of mouth. Pathology '
                        'shows a microscopically positive deep margin that cannot be revised and '
                        'two positive right level IB nodes, one with extranodal extension. Her '
                        'creatinine clearance is 95 mL/min, hearing is normal, and performance '
                        'status is 0. Which adjuvant approach is most strongly supported?',
                'choices': ['Radiation with concurrent cisplatin',
                            'Radiation alone to a dose of 60-66 Gy',
                            'Radiation with concurrent cetuximab',
                            'Observation with PET/CT at 3 months'],
                'answer': 0,
                'explanation': 'Positive margins and extranodal extension are the two high-risk '
                               'features for which postoperative radiation with concurrent '
                               'cisplatin improved locoregional control in RTOG 9501 and EORTC '
                               '22931, and survival in the EORTC trial. A pooled analysis found '
                               'the benefit concentrated in these two features. High-dose '
                               'cisplatin every 3 weeks is standard, and weekly cisplatin is an '
                               'accepted alternative based on JCOG1008. Treatment should start '
                               'within about 6 weeks of surgery.',
                'why_wrong': ['Correct.',
                              'Radiation alone undertreats high-risk disease; adding cisplatin '
                              'improves locoregional control when margins are positive or ENE is '
                              'present.',
                              'Cetuximab is not an established substitute for cisplatin and is '
                              'reserved, at most, for patients who cannot receive it.',
                              'Observing high-risk pathology invites early recurrence when proven '
                              'adjuvant therapy is available.'],
                'board_pearl': 'Positive margin or extranodal extension after surgery: '
                               'postoperative radiation with concurrent cisplatin.',
                'curveball': 'What other pathologic findings may justify adjuvant radiation '
                             'without necessarily requiring chemotherapy?',
                'curveball_answer': 'Intermediate-risk features include pT3 or pT4 primary, pN2 or '
                                    'pN3 nodal disease without extranodal extension, nodes in '
                                    'level IV or V, perineural invasion, lymphovascular invasion, '
                                    'and close margins. These generally support postoperative '
                                    'radiation alone. Chemotherapy is added mainly for positive '
                                    'margins or extranodal extension.'},
 'v140_hn_07': {'stem': 'A 60-year-old man undergoes partial glossectomy and left neck dissection '
                        'for pT3 oral tongue squamous cell carcinoma. All margins are negative at '
                        '6 mm. Pathology shows perineural and lymphovascular invasion and three '
                        'positive left nodes, one of which shows extranodal extension. He is fit, '
                        'with normal renal function and hearing. Which pathologic finding is the '
                        'main reason to add concurrent cisplatin?',
                'choices': ['Extranodal extension in one of the positive nodes',
                            'Perineural invasion identified at the primary site',
                            'Three positive lymph nodes in the left neck sample',
                            'Lymphovascular invasion seen within the primary'],
                'answer': 0,
                'explanation': 'In the pooled analysis of RTOG 9501 and EORTC 22931, adding '
                               'concurrent cisplatin to postoperative radiation benefited patients '
                               'with extranodal extension or positive margins. Other adverse '
                               'features, such as perineural invasion, lymphovascular invasion, '
                               'pT3-T4 disease, and multiple nodes, support postoperative '
                               'radiation but are not by themselves standard indications for '
                               'chemotherapy. Here his margins are clear, so extranodal extension '
                               'is the feature that drives the decision to add cisplatin.',
                'why_wrong': ['Correct.',
                              'Perineural invasion supports postoperative radiation, but it is not '
                              'by itself a standard indication for concurrent chemotherapy.',
                              'Multiple positive nodes support postoperative radiation, but '
                              'chemotherapy is driven by extranodal extension or positive margins.',
                              'Lymphovascular invasion is an intermediate-risk feature for '
                              'radiation, not a standard indication for cisplatin.'],
                'board_pearl': 'Only positive margins and extranodal extension are standard '
                               'indications for adding cisplatin after surgery.',
                'curveball': 'How do close but negative margins, perineural invasion, '
                             'lymphovascular invasion, and multiple nodes differ in adjuvant '
                             'implications?',
                'curveball_answer': 'Each of these is an intermediate-risk feature that generally '
                                    'supports postoperative radiation alone. Close margins may '
                                    'prompt re-resection if feasible. Chemotherapy is sometimes '
                                    'considered when several intermediate features occur together, '
                                    'but evidence is weaker than for positive margins or '
                                    'extranodal extension and the decision is individualized.'},
 'v222_hn_adv_fnd': {'stem': 'A 64-year-old man had a right partial maxillectomy and neck '
                             'dissection for squamous cell carcinoma of the hard palate and '
                             'alveolus. Pathology shows a positive microscopic posterior margin '
                             'that cannot be safely re-resected and extranodal extension in a '
                             'level II node. He is fit, with normal renal function. He asks '
                             'whether radiation alone would be enough. What is the most accurate '
                             'answer?',
                     'choices': ['Radiation alone is equivalent because the positive margin is '
                                 'microscopic',
                                 'Chemotherapy helps only when more than three nodes are involved',
                                 'Sequential chemotherapy after radiation gives the same benefit',
                                 'Concurrent cisplatin improves control, and survival in EORTC '
                                 '22931'],
                     'answer': 3,
                     'explanation': 'Positive margins and extranodal extension are the high-risk '
                                    'features for which postoperative concurrent '
                                    'cisplatin-radiation is standard. RTOG 9501 showed better '
                                    'locoregional control and EORTC 22931 showed better survival '
                                    'with concurrent cisplatin compared with radiation alone, and '
                                    'a pooled analysis confirmed that benefit was concentrated in '
                                    'these two features. Radiation alone would undertreat him. '
                                    'Treatment should begin within about 6 weeks of surgery when '
                                    'healing allows.',
                     'why_wrong': ['A microscopic positive margin is still a high-risk feature in '
                                   'which radiation alone gave worse locoregional control.',
                                   'The number of nodes was not the feature that predicted benefit '
                                   'from cisplatin in the pooled analysis.',
                                   'The benefit comes from concurrent radiosensitization; '
                                   'sequential chemotherapy has not been shown to match it.',
                                   'Correct.'],
                     'board_pearl': 'Positive margin or ENE: concurrent cisplatin-radiation, '
                                    'supported by RTOG 9501 and EORTC 22931.',
                     'curveball': 'Suppose his creatinine clearance were 30 mL/min instead. How '
                                  'would severe renal dysfunction alter the systemic therapy '
                                  'discussion?',
                     'curveball_answer': 'Cisplatin is generally contraindicated with a creatinine '
                                         'clearance below about 50 mL/min. Options include '
                                         'radiation alone, radiation with a non-cisplatin '
                                         'radiosensitizer such as weekly docetaxel based on more '
                                         'recent trial data, or enrollment in a clinical trial. '
                                         'Carboplatin or cetuximab are sometimes used, but '
                                         'evidence is weaker. The decision is made at the tumor '
                                         'board.'},
 'v222_hn_adv_app': {'stem': 'A 58-year-old man undergoes partial glossectomy and left neck '
                             'dissection for oral tongue squamous cell carcinoma. Final pathology '
                             'shows a 3.5-cm tumor with 8-mm depth of invasion, perineural '
                             'invasion, margins clear at 7 mm, and two positive left level II '
                             'nodes without extranodal extension. He is fit, with normal renal '
                             'function. What is the most appropriate adjuvant treatment?',
                     'choices': ['Postoperative radiation to the primary site and neck',
                                 'Postoperative radiation with concurrent cisplatin',
                                 'Observation, since all the margins are negative',
                                 'Adjuvant docetaxel-cisplatin without radiation'],
                     'answer': 0,
                     'explanation': 'This is pT2N2b disease with perineural invasion. Multiple '
                                    'positive nodes and perineural invasion are intermediate-risk '
                                    'features that support postoperative radiation to the primary '
                                    'bed and neck. Without a positive margin or extranodal '
                                    'extension, concurrent cisplatin is not routinely indicated, '
                                    'because the pooled RTOG 9501 and EORTC 22931 analysis did not '
                                    'show clear benefit in that setting. Negative margins do not '
                                    'remove the recurrence risk from his nodal disease and '
                                    'perineural invasion.',
                     'why_wrong': ['Correct.',
                                   'Concurrent cisplatin adds toxicity without established benefit '
                                   'when margins are clear and there is no extranodal extension.',
                                   'Negative margins do not offset the regional recurrence risk '
                                   'from multiple nodes and perineural invasion.',
                                   'Adjuvant chemotherapy alone has not been shown to replace '
                                   'postoperative radiation in head and neck cancer.'],
                     'board_pearl': 'Intermediate-risk features without ENE or positive margins: '
                                    'postoperative radiation alone.',
                     'curveball': 'Which nodal and primary-site features most strongly alter '
                                  'postoperative radiation volumes?',
                     'curveball_answer': 'Radiation covers the primary bed and dissected neck. '
                                         'Extranodal extension, multiple nodes, or low-neck levels '
                                         'increase dose to the involved regions and expand '
                                         'coverage. A primary near midline or bilateral nodes '
                                         'calls for treating the contralateral neck. Perineural '
                                         'invasion of a named nerve extends fields along that '
                                         'nerve toward the skull base.'},
 'v222_hn_adv_snr': {'stem': 'A 74-year-old man had resection and neck dissection for oral cavity '
                             'squamous cell carcinoma with extranodal extension in a level III '
                             'node and clear margins. He has chronic kidney disease with '
                             'creatinine clearance of 35 mL/min, bilateral sensorineural hearing '
                             'loss with hearing aids, diabetic neuropathy, and ECOG performance '
                             'status 2. The tumor board is discussing adjuvant treatment. What is '
                             'the best approach?',
                     'choices': ['High-dose cisplatin every 3 weeks with aggressive hydration '
                                 'support',
                                 'Postoperative radiation, with a non-cisplatin option chosen by '
                                 'the board',
                                 'No adjuvant therapy, since he cannot receive standard cisplatin',
                                 'Delay treatment and start therapy only if recurrence is '
                                 'detected'],
                     'answer': 1,
                     'explanation': 'Extranodal extension is a high-risk feature, so the case for '
                                    'intensified adjuvant treatment remains. Kidney disease, '
                                    'hearing loss, neuropathy, and reduced performance status each '
                                    'make cisplatin unsafe. The team should still deliver '
                                    'postoperative radiation and consider a non-cisplatin '
                                    'approach, such as radiation alone or with a radiosensitizer '
                                    'like docetaxel, or a clinical trial, guided by his '
                                    'priorities. Ineligibility for cisplatin changes the regimen, '
                                    'not the indication for adjuvant therapy.',
                     'why_wrong': ['Cisplatin with this renal function, hearing loss, and '
                                   'neuropathy risks severe kidney damage, deafness, and worse '
                                   'neuropathy.',
                                   'Correct.',
                                   'Ineligibility for cisplatin does not remove the need for '
                                   'postoperative radiation after a high-risk resection.',
                                   'Waiting for recurrence forgoes effective adjuvant treatment, '
                                   'and salvage after recurrence rarely cures.'],
                     'board_pearl': 'Cisplatin-ineligible high-risk patients still need adjuvant '
                                    'radiation; change the regimen, not the indication.',
                     'curveball': 'If the final margin had been truly positive, how would that '
                                  'change the discussion about re-resection before adjuvant '
                                  'therapy?',
                     'curveball_answer': 'If the positive margin can be located and safely '
                                         're-resected, re-resection to a clear margin is preferred '
                                         'before adjuvant therapy, since a re-resected margin '
                                         'carries less risk than leaving it positive. If '
                                         're-resection is not feasible, the positive margin adds a '
                                         'second high-risk feature and increases the importance of '
                                         'intensified adjuvant treatment.'},
 'v134_hno_03': {'stem': 'A 68-year-old man is 4 years disease-free after chemoradiation for T3 '
                         'glottic carcinoma. He has had four aspiration pneumonias in 18 months, '
                         'takes nothing by mouth through his gastrostomy, and on FEES silently '
                         'aspirates his own secretions. Six months of intensive swallowing therapy '
                         'have not helped. Laryngoscopy shows a fibrotic larynx, and PET/CT and '
                         'biopsy show no recurrence. Which management option should now be '
                         'discussed?',
                 'choices': ['A further 6-month block of the same intensive swallowing therapy',
                             'Cuffed tracheostomy tube left inflated to protect the lower airway',
                             'Injection medialization of the vocal folds to improve glottic '
                             'closure',
                             'Functional total laryngectomy to separate airway and food passage'],
                 'answer': 3,
                 'explanation': 'This larynx is anatomically preserved but functionally failed: '
                                'years after chemoradiation it cannot protect the airway, causing '
                                'recurrent pneumonia despite maximal rehabilitation. Without '
                                'recurrence, functional total laryngectomy separates the airway '
                                'from the food passage, which stops aspiration, often restores '
                                'oral intake, and allows tracheoesophageal speech. It is a '
                                'reasonable, sometimes lifesaving option for selected disease-free '
                                'patients who understand the trade-offs.',
                 'why_wrong': ['He has already had intensive therapy without benefit, and silent '
                               'aspiration of secretions is unlikely to respond to more of it.',
                               'A cuffed tube does not prevent aspiration, because secretions pool '
                               'above and leak past the cuff into the trachea.',
                               'Medialization helps glottic gaps but cannot fix the sensory loss, '
                               'fibrosis, and pharyngeal weakness behind this aspiration.',
                               'Correct.'],
                 'board_pearl': 'A disease-free larynx that aspirates despite rehabilitation can '
                                'justify functional laryngectomy.',
                 'curveball': 'What wound complication is especially important when performing '
                              'laryngectomy in this heavily irradiated field, and how can '
                              'reconstruction reduce it?',
                 'curveball_answer': 'Pharyngocutaneous fistula is the key risk, because '
                                     'irradiated pharyngeal tissue heals poorly. Reinforcing the '
                                     'closure with nonirradiated vascularized tissue, such as a '
                                     'pectoralis major muscle onlay or a free flap when mucosa is '
                                     'insufficient, lowers fistula rates. Optimizing nutrition and '
                                     'thyroid function beforehand also helps.'},
 'v138_hn_15': {'stem': 'A 72-year-old woman completed chemoradiation for hypopharyngeal squamous '
                        'cell carcinoma 6 years ago and remains disease-free on imaging. She has '
                        'been gastrostomy-dependent for 3 years and has been admitted three times '
                        'this year with aspiration pneumonia. Modified barium swallow shows '
                        'aspiration of all consistencies with a weak cough. She has completed two '
                        'rounds of swallowing therapy. What should guide the next discussion?',
                'choices': ['Continued oncologic surveillance alone, since the larynx remains '
                            'intact',
                            'Long-term prophylactic azithromycin to prevent further pneumonias',
                            'Her candidacy for functional laryngectomy now that rehab has failed',
                            'Botulinum toxin injection of the cricopharyngeus to ease bolus flow'],
                'answer': 2,
                'explanation': 'A chronically aspirating larynx can be life-threatening even '
                               'without cancer recurrence. When intensive rehabilitation has '
                               'failed and pneumonias continue, the discussion should turn to '
                               'functional options such as aspiration-prevention surgery or total '
                               'laryngectomy. Definitive separation of the airway and food passage '
                               'stops aspiration, reduces pneumonias, and may allow some oral '
                               'intake. Candidacy depends on pulmonary reserve, nutrition, tissue '
                               'quality, her goals, and communication plans.',
                'why_wrong': ['Surveillance addresses recurrence but ignores the aspiration that '
                              'is now her main threat to life.',
                              'Prophylactic antibiotics do not stop aspiration and select for '
                              'resistant organisms.',
                              'Correct.',
                              'Cricopharyngeal botulinum helps upper esophageal sphincter '
                              'dysfunction, but she aspirates all consistencies from failed airway '
                              'protection.'],
                'board_pearl': 'Recurrent aspiration pneumonia after failed rehab: discuss '
                               'functional laryngectomy or other airway-food separation.',
                'curveball': 'She asks what she would gain and what she would give up. What '
                             'quality-of-life trade-offs accompany functional laryngectomy?',
                'curveball_answer': 'She gains freedom from aspiration, fewer hospitalizations, '
                                    'and often some oral intake, but loses her natural voice and '
                                    'nasal breathing and smell, and will have a permanent stoma '
                                    'requiring care. Most patients achieve useful speech with a '
                                    'tracheoesophageal prosthesis or electrolarynx. Patients with '
                                    'chronic pneumonias often report better quality of life after '
                                    'surgery.'},
 'v140_hn_09': {'stem': 'A 65-year-old man completed radiation for T2 supraglottic carcinoma 5 '
                        'years ago and has no evidence of recurrence. He depends on a gastrostomy '
                        'tube and has had two ICU admissions for aspiration pneumonia despite a '
                        'year of swallowing therapy. His oncologist calls his treatment a success '
                        'because his larynx was preserved. When counseling him, which outcome best '
                        'defines successful larynx preservation?',
                'choices': ['Absence of recurrent tumor on surveillance PET/CT',
                            'Preserved natural voice quality after radiation therapy',
                            'An intact laryngeal framework visible on CT imaging',
                            'Safe swallowing and freedom from aspiration pneumonia'],
                'answer': 3,
                'explanation': 'Larynx preservation aims for a functional organ that breathes, '
                               'protects the airway, and permits swallowing and voice. A larynx '
                               'that is tumor-free and anatomically intact but causes repeated '
                               'aspiration pneumonia and tube dependence is a functional failure. '
                               'Measuring success this way reframes his situation and opens '
                               'discussion of aspiration-prevention surgery, which may improve '
                               'survival and quality of life at the cost of his native voice.',
                'why_wrong': ['Tumor control is necessary but not sufficient; a tumor-free larynx '
                              'that aspirates is not a successful preservation.',
                              'Voice is one function, but safe airway protection and swallowing '
                              'matter more for survival and quality of life.',
                              'An intact framework on imaging says nothing about whether the '
                              'larynx protects the airway.',
                              'Correct.'],
                'board_pearl': 'Measure larynx preservation by function, safe swallowing and '
                               'airway protection, not anatomy.',
                'curveball': 'He agrees to consider surgery. What preoperative counseling '
                             'distinguishes functional laryngectomy from laryngectomy done for '
                             'cancer?',
                'curveball_answer': 'The goal is to stop aspiration, not to remove cancer, so '
                                    'margins and neck dissection are not needed, and a '
                                    'narrow-field laryngectomy may preserve more pharyngeal '
                                    'mucosa. Counseling should cover the irradiated wound and '
                                    'fistula risk, loss of natural voice with tracheoesophageal '
                                    'speech options, the permanent stoma, and the realistic chance '
                                    'of resuming some oral intake.'},
 'v145_hn_11': {'stem': 'A 60-year-old man had chemoradiation for base-of-tongue carcinoma 7 years '
                        'ago and remains cancer-free. He now needs his gastrostomy for all '
                        'nutrition after a gradual decline over 2 years and has had three '
                        'pneumonias. He completed swallowing therapy twice. His pulmonologist asks '
                        'what to do next. His last instrumental swallow study was 2 years ago. '
                        'What is the most appropriate next step?',
                'choices': ['Repeat instrumental swallow study and multidisciplinary review',
                            'Proceed directly to total laryngectomy at the earliest opportunity',
                            'Start long-term azithromycin and continue nothing by mouth',
                            'Order restaging PET/CT as the only evaluation needed now'],
                'answer': 0,
                'explanation': 'Before considering aspiration-prevention surgery, the team needs a '
                               'current picture of why and how he aspirates. A repeat modified '
                               'barium swallow or FEES defines the mechanism, the severity, and '
                               'whether any rehabilitative target remains. Multidisciplinary '
                               'review with speech pathology, pulmonology, and surgery then weighs '
                               'his pulmonary risk, rehabilitation potential, nutrition, and '
                               'goals. If rehabilitation has truly reached its ceiling, '
                               'aspiration-prevention surgery or functional laryngectomy becomes '
                               'appropriate to discuss.',
                'why_wrong': ['Correct.',
                              'Laryngectomy may be the eventual answer, but deciding without '
                              'current swallow data and goals discussion skips essential steps.',
                              'Antibiotics treat infections but do not address aspiration, the '
                              'cause of his recurring pneumonia.',
                              'Excluding recurrence is part of the workup, but imaging alone does '
                              'not assess his swallowing function.'],
                'board_pearl': 'Before aspiration-prevention surgery, update the swallow '
                               'assessment and decide as a team.',
                'curveball': 'How would tracheoesophageal speech counseling differ for a '
                             'functional laryngectomy done for aspiration rather than active '
                             'cancer?',
                'curveball_answer': 'The discussion focuses on speech as a gain from a safer '
                                    'airway rather than loss from cancer surgery. Many patients '
                                    'have very poor voice before surgery. Primary or secondary '
                                    'puncture is chosen based on tissue quality, since irradiated '
                                    'tissue and fistula risk often favor secondary puncture. '
                                    'Prosthesis leakage can be a recurring problem in irradiated '
                                    'tissue.'},
 'v227_hn_nfl_fnd': {'stem': 'A 70-year-old woman completed chemoradiation for T3 glottic '
                             'carcinoma 8 years ago. Surveillance imaging and biopsies have been '
                             'negative. She now has a tracheostomy, depends on a feeding tube, and '
                             'aspirates thin and thick liquids on FEES, despite two years of '
                             'supervised swallowing therapy. Her family is told her larynx was '
                             'saved. Which description best characterizes her larynx?',
                     'choices': ['Successful organ preservation with an expected late side effect',
                                 'Recurrent tumor until proven otherwise despite negative biopsies',
                                 'Anatomically present but functionally failed after treatment',
                                 'A normal survivorship course that needs no further intervention'],
                     'answer': 2,
                     'explanation': 'Cancer control and organ preservation are not the same as '
                                    'preserved function. Late radiation effects such as fibrosis, '
                                    'sensory loss, and impaired laryngeal closure can leave a '
                                    'tumor-free larynx that cannot protect the airway or support '
                                    'swallowing. Tracheostomy and feeding-tube dependence with '
                                    'aspiration despite therapy mark a functionally failed larynx. '
                                    'Naming the problem this way opens discussion of '
                                    'aspiration-prevention surgery.',
                     'why_wrong': ['Calling this success ignores the aspiration and tube '
                                   'dependence, which are major functional failures.',
                                   'Recurrence must be excluded, but negative imaging and biopsies '
                                   'point to treatment-related dysfunction instead.',
                                   'Correct.',
                                   'Chronic aspiration with tracheostomy and tube dependence is a '
                                   'serious complication, not a normal survivorship course.'],
                     'board_pearl': 'A tumor-free larynx that cannot protect the airway is a '
                                    'functional failure.',
                     'curveball': 'What objective swallowing and pulmonary findings help determine '
                                  'whether rehabilitation has reached its ceiling?',
                     'curveball_answer': 'Persistent aspiration of secretions and all '
                                         'consistencies on instrumental studies, absent laryngeal '
                                         'sensation and cough, and penetration-aspiration scores '
                                         'that do not improve over serial studies suggest a '
                                         'ceiling. Repeated aspiration pneumonia, declining lung '
                                         'function, and inability to meet nutrition orally add '
                                         'support. When these persist after expert therapy, '
                                         'aspiration-prevention surgery is reasonable.'},
 'v227_hn_nfl_app': {'stem': 'A 63-year-old man completed chemoradiation for supraglottic '
                             'carcinoma 5 years ago and has no recurrence. He has had four '
                             'aspiration pneumonias in 2 years despite thickened liquids, '
                             'chin-tuck, and swallowing therapy. Modified barium swallow shows '
                             'poor laryngeal elevation and incomplete airway closure with '
                             'aspiration during the swallow; the upper esophageal sphincter opens '
                             'normally, and there is no stricture. What is the best next step?',
                     'choices': ['Serial dilation of the pharyngoesophageal segment to treat her '
                                 'dysphagia',
                                 'Discuss aspiration-prevention surgery after reviewing his goals',
                                 'Cricopharyngeal myotomy to improve passage of the bolus',
                                 'Continue thickened liquids and chin-tuck indefinitely as before'],
                     'answer': 1,
                     'explanation': 'His aspiration arises from failed airway closure and poor '
                                    'laryngeal elevation, not from an obstructed outflow. When '
                                    'rehabilitation, diet changes, and nutrition support have '
                                    'failed and pneumonias continue, the next step is to reassess '
                                    'goals and discuss aspiration-prevention surgery. Options '
                                    'include total laryngectomy or other separation procedures, '
                                    'chosen based on voice goals, anatomy, tissue quality, and '
                                    'prior radiation.',
                     'why_wrong': ['Dilation treats stricture, but his sphincter opens normally '
                                   'and there is no stricture to dilate.',
                                   'Correct.',
                                   'Myotomy helps a tight upper esophageal sphincter, which he '
                                   'does not have, and does not fix poor airway closure.',
                                   'Continuing measures that have already failed accepts further '
                                   'pneumonias without addressing the cause.'],
                     'board_pearl': 'Match treatment to the aspiration mechanism; failed airway '
                                    'protection needs aspiration-prevention surgery.',
                     'curveball': 'How do his voice goals alter the choice between total '
                                  'laryngectomy and other aspiration-prevention procedures?',
                     'curveball_answer': 'Total laryngectomy offers the most reliable separation '
                                         'and allows tracheoesophageal speech. Laryngotracheal '
                                         'separation or tracheoesophageal diversion is in theory '
                                         'reversible, but in an irradiated, fibrotic larynx '
                                         'reversal rarely restores useful voice or swallowing. '
                                         'Glottic closure procedures sacrifice voice. A patient '
                                         'who values voice may prefer total laryngectomy with '
                                         'tracheoesophageal speech.'},
 'v227_hn_nfl_snr': {'stem': 'A 78-year-old man is 5 years disease-free after high-dose '
                             'chemoradiation for oropharyngeal carcinoma and has chronic '
                             'aspiration. He asks for total laryngectomy to stop the pneumonias. '
                             'He uses home oxygen for COPD, weighs 52 kg with an albumin of 2.7 '
                             'g/dL, lives alone, and has had poor wound healing after a prior '
                             'gastrostomy. What is the best approach?',
                     'choices': ['Proceed promptly, as chronic aspiration alone mandates '
                                 'laryngectomy',
                                 'Weigh aspiration control against operative, wound, and rehab '
                                 'risks',
                                 'Decline surgery because laryngectomy is reserved for active '
                                 'cancer',
                                 'Offer laryngotracheal separation, as it carries no fistula risk'],
                     'answer': 1,
                     'explanation': 'Functional laryngectomy can help selected patients, but here '
                                    'frailty, severe lung disease, malnutrition, poor wound '
                                    'healing, and limited home support raise operative and wound '
                                    'risks and make rehabilitation and stoma care difficult. The '
                                    'decision should balance the expected benefit against '
                                    'perioperative risk, fistula and reconstructive needs, '
                                    'communication outcome, and realistic rehabilitation, together '
                                    'with his goals. Nutrition optimization and alternatives '
                                    'should be discussed.',
                     'why_wrong': ['Aspiration supports considering surgery, but frailty and wound '
                                   'risk must be weighed before recommending it.',
                                   'Correct.',
                                   'Laryngectomy is also a valid functional operation for '
                                   'life-threatening aspiration in disease-free patients.',
                                   'Separation procedures in irradiated tissue also carry fistula '
                                   'and wound risks.'],
                     'board_pearl': 'Functional laryngectomy in a frail patient needs a frank '
                                    'risk-benefit and goals discussion.',
                     'curveball': 'What role can vascularized tissue reinforcement play when the '
                                  'pharynx is heavily irradiated?',
                     'curveball_answer': 'Nonirradiated vascularized tissue, such as a pectoralis '
                                         'major muscle onlay or a free flap interposed in the '
                                         'pharyngeal closure, brings blood supply into the '
                                         'irradiated field, lowers fistula rates, and reduces '
                                         'fistula severity and carotid exposure when leaks occur. '
                                         'It is commonly used in irradiated functional and salvage '
                                         'laryngectomy.'},
 'v231_hn_nfl_fnd': {'stem': 'A 61-year-old man completed chemoradiation for tonsil carcinoma 7 '
                             'years ago. Over 3 years his swallowing has steadily worsened, and he '
                             'now has recurrent aspiration pneumonia and depends on a feeding '
                             'tube. Examination shows a woody neck and a fibrotic, poorly mobile '
                             'larynx with pooled secretions. PET/CT and biopsies show no '
                             'recurrence, and he has no neurologic symptoms elsewhere. What is the '
                             'most likely diagnosis?',
                     'choices': ['Late radiation-associated dysphagia with a failed larynx',
                                 'Recurrent carcinoma in the hypopharynx not yet visible',
                                 'Primary achalasia unrelated to his previous treatment',
                                 'Myasthenia gravis with progressive bulbar weakness'],
                     'answer': 0,
                     'explanation': 'Late radiation-associated dysphagia develops years after '
                                    'treatment as fibrosis, lymphedema, sensory loss, and nerve '
                                    'and muscle injury progress. It causes impaired pharyngeal '
                                    'contraction, poor laryngeal elevation and closure, and '
                                    'chronic aspiration. A woody neck and fibrotic larynx with '
                                    'negative restaging fit this picture. The result is a '
                                    'nonfunctional larynx and intractable aspiration even without '
                                    'recurrent cancer, which may justify aspiration-prevention '
                                    'surgery.',
                     'why_wrong': ['Correct.',
                                   'Recurrence must always be excluded, but negative PET/CT and '
                                   'biopsies point to treatment-related dysfunction instead.',
                                   'Achalasia causes esophageal outflow obstruction with '
                                   'regurgitation, not laryngeal fibrosis and pooled secretions.',
                                   'Myasthenia causes fluctuating fatigable weakness, usually with '
                                   'ocular signs, and does not cause a woody neck.'],
                     'board_pearl': 'Progressive dysphagia years after radiation with negative '
                                    'restaging: late radiation-associated dysphagia.',
                     'curveball': 'His wife asks why his swallowing got worse years after '
                                  'treatment ended. Which late radiation changes explain this '
                                  'progression?',
                     'curveball_answer': 'Progressive fibrosis of the pharyngeal constrictors and '
                                         'neck, lymphedema, sensory loss in the pharynx and '
                                         'larynx, lower cranial neuropathy affecting IX, X, and '
                                         'XII, upper esophageal sphincter stricture, and laryngeal '
                                         'chondronecrosis can all worsen with time. Muscle atrophy '
                                         'and trismus add to this. Each contributes to impaired '
                                         'bolus transport and airway protection.'},
 'v231_hn_nfl_app': {'stem': 'A 66-year-old woman is 6 years past radiation for supraglottic '
                             'carcinoma. Despite diet modification, swallowing therapy, and full '
                             'gastrostomy feeding, she has had three pneumonias this year. FEES '
                             'shows gross aspiration of secretions with absent laryngeal sensation '
                             'and no cough. She communicates by voice and wants to keep talking. '
                             'Her last surveillance scan was 14 months ago. What is the best next '
                             'step?',
                     'choices': ['Salivary botulinum toxin as definitive control of her aspiration',
                                 'Cuffed tracheostomy tube to protect the airway from secretions',
                                 'Restage to exclude recurrence, then discuss '
                                 'aspiration-prevention surgery',
                                 'Continue the current plan and treat each pneumonia as it occurs'],
                     'answer': 2,
                     'explanation': 'Severe aspiration of secretions with absent sensation and '
                                    'recurrent pneumonia despite maximal rehabilitation and tube '
                                    'feeding is life-threatening. Because surveillance is overdue, '
                                    'recurrence must be excluded first. Then she can be counseled '
                                    'on aspiration-prevention options, such as total laryngectomy '
                                    'with tracheoesophageal speech or separation procedures, with '
                                    'her wish to keep speaking guiding the choice. Pulmonary risk '
                                    'and tissue quality also shape the plan.',
                     'why_wrong': ['Salivary botulinum can reduce secretion volume as an adjunct '
                                   'but does not stop aspiration or prevent pneumonia on its own.',
                                   'A cuffed tube does not prevent aspiration of secretions, which '
                                   'leak around the cuff into the trachea.',
                                   'Correct.',
                                   'Treating each pneumonia accepts repeated life-threatening '
                                   'events without addressing the cause.'],
                     'board_pearl': 'Confirm no recurrence, then match aspiration-prevention '
                                    "surgery to the patient's communication goals.",
                     'curveball': 'How do total laryngectomy, laryngotracheal separation, and '
                                  'other aspiration-prevention procedures differ in voice and '
                                  'reconstructive implications?',
                     'curveball_answer': 'Total laryngectomy reliably separates airway and food '
                                         'passage and allows tracheoesophageal speech, but it is '
                                         'irreversible and needs careful closure in irradiated '
                                         'tissue. Laryngotracheal separation is in theory '
                                         'reversible but leaves no voice, and in irradiated tissue '
                                         'reversal rarely restores useful function. Glottic or '
                                         'epiglottic closure procedures sacrifice voice and often '
                                         'break down in irradiated tissue.'},
 'v231_hn_nfl_snr': {'stem': 'A 64-year-old man is disease-free 6 years after salvage partial '
                             'pharyngectomy and radiation for hypopharyngeal carcinoma, which was '
                             'complicated by a pharyngocutaneous fistula. His larynx is now '
                             'nonfunctional, with chronic aspiration and repeated pneumonias. He '
                             'requests total laryngectomy. His neck is woody and fibrotic, and his '
                             'albumin is 2.9 g/dL. What is the best planning principle?',
                     'choices': ['Close the pharynx primarily, since no tumor margin is needed',
                                 'Choose laryngotracheal separation, which avoids wound problems',
                                 'Postpone until a full course of hyperbaric oxygen is complete',
                                 'Optimize nutrition and plan vascularized flap reinforcement'],
                     'answer': 3,
                     'explanation': 'Total laryngectomy can be used for a nonfunctional larynx '
                                    'when aspiration is otherwise uncontrollable, but in a heavily '
                                    'irradiated field with prior fistula it carries the same wound '
                                    'risks as oncologic salvage. Planning should optimize '
                                    'nutrition and lung function, confirm the aspiration mechanism '
                                    'and his goals, and include nonirradiated vascularized tissue, '
                                    'such as a pectoralis onlay or free flap, to reinforce the '
                                    'closure. Alaryngeal communication should be planned too.',
                     'why_wrong': ['Lack of a tumor margin does not change the poor healing of '
                                   'irradiated tissue; primary closure alone invites another '
                                   'fistula.',
                                   'Laryngotracheal separation in fibrotic, previously fistulized '
                                   'tissue also carries significant wound and fistula risk.',
                                   'Hyperbaric oxygen has uncertain benefit here and would delay '
                                   'definitive surgery while pneumonias continue.',
                                   'Correct.'],
                     'board_pearl': 'Functional laryngectomy in irradiated tissue: plan nutrition '
                                    'and flap reinforcement as for salvage.',
                     'curveball': 'What findings would favor primary flap reinforcement rather '
                                  'than simple pharyngeal closure in this irradiated field?',
                     'curveball_answer': 'A prior fistula, low albumin, hypothyroidism, woody '
                                         'fibrotic tissue, high cumulative dose, prior surgery in '
                                         'the field, and insufficient mucosa for a tension-free '
                                         'closure all favor flap reinforcement. A pectoralis major '
                                         'onlay or a free-flap interposition brings in healthy '
                                         'blood supply and lowers fistula and stricture risk.'}}
