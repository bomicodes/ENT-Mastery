"""v491 rewrites: Pediatric Otolaryngology (ped1)."""

REWRITES = {'v11_ped_01': {'stem': 'A 2-year-old boy in full-time daycare has had three episodes of acute otitis media in the '
                        'past 6 months, each treated with amoxicillin, the most recent 5 weeks ago. He is meeting '
                        'language milestones and is well today. Pneumatic otoscopy shows translucent, mobile tympanic '
                        'membranes bilaterally, and tympanometry is type A in both ears. His parents ask about ear '
                        'tubes. What is the most appropriate recommendation?',
                'choices': ['Bilateral tympanostomy tubes now, given three episodes in 6 months',
                            'Adenoidectomy alone to remove the nasopharyngeal bacterial reservoir',
                            'No tubes for now; reduce risk factors and reassess with future episodes',
                            'Daily low-dose amoxicillin prophylaxis through the respiratory season'],
                'answer': 2,
                'explanation': 'He meets the frequency definition of recurrent AOM (3 episodes in 6 months or 4 in 12 '
                               'months with 1 in the last 6), but the 2022 AAO-HNSF tympanostomy tube guideline '
                               'recommends against tubes for recurrent AOM when no middle-ear effusion is present at '
                               'the candidacy assessment. Clear, mobile drums between infections indicate adequate '
                               'tube function, so tubes add surgical and otorrhea risk with little benefit. Counsel on '
                               'daycare, smoke and pacifier exposure, confirm pneumococcal and influenza vaccination, '
                               'and reassess if effusion is documented.',
                'why_wrong': ['Tubes for recurrent AOM are recommended only when effusion is present at assessment; '
                              'his type A tympanograms argue against surgery today.',
                              'Adenoidectomy is not recommended as a stand-alone procedure for recurrent AOM in a '
                              'child younger than 4 without a separate nasal indication.',
                              'Correct.',
                              'The AAP guideline advises against antibiotic prophylaxis for recurrent AOM because '
                              'benefit is modest and resistant pneumococcal carriage increases.'],
                'board_pearl': 'Recurrent AOM gets tubes only when effusion is present at the candidacy visit; clear '
                               'ears mean no tubes.',
                'curveball': 'He returns 2 months later after a fourth episode and now has bilateral effusions with '
                             'flat tympanograms at the candidacy visit. How does that change the plan?',
                'curveball_answer': 'Recurrent AOM with effusion present at assessment is a guideline indication to '
                                    'offer bilateral tympanostomy tubes, which reduce AOM frequency and let future '
                                    'infections be treated with topical drops instead of systemic antibiotics. Obtain '
                                    'a hearing test first. Adjunct adenoidectomy is not routine at age 2 unless there '
                                    'is nasal obstruction or chronic adenoiditis.'},
 'v124_ped_01': {'stem': 'A 26-month-old girl has had bilateral middle-ear effusions on every visit for the past 4 '
                         'months after an episode of AOM. She is afebrile and has no otalgia. Her vocabulary is about '
                         '20 words, and a speech-language pathologist reports expressive delay. Tympanometry is type B '
                         'bilaterally, and soundfield audiometry shows a 30 dB hearing level with normal '
                         'bone-conduction screening. What is the most appropriate management?',
                 'choices': ['Further watchful waiting with repeat audiometry in 3 months',
                             'Bilateral tympanostomy tubes with postoperative hearing retest',
                             'Oral prednisolone and amoxicillin for 2 weeks, then recheck',
                             'Adenoidectomy with bilateral myringotomy but without tubes'],
                 'answer': 1,
                 'explanation': 'Bilateral OME persisting 3 months or longer with documented hearing difficulty is the '
                                'setting in which the 2022 AAO-HNSF guideline recommends offering bilateral '
                                'tympanostomy tubes. The 30 dB conductive deficit during a sensitive period for '
                                'language, plus an established expressive delay, tips the balance away from more '
                                'observation. Tubes ventilate the middle ear and restore hearing while the Eustachian '
                                'tube matures. Steroids, antibiotics and decongestants do not produce durable '
                                'resolution and are not recommended for OME.',
                 'why_wrong': ['She has already completed more than 3 months of observation and now has hearing loss '
                               'with speech delay, so further waiting adds harm.',
                               'Correct.',
                               'Systemic steroids and antibiotics give only short-term clearance and are recommended '
                               'against for OME because of side effects and resistance.',
                               'Myringotomy alone closes within days, and adenoidectomy is not advised under age 4 '
                               'without a separate indication such as nasal obstruction.'],
                 'board_pearl': 'Bilateral OME for 3 months or more plus documented hearing difficulty: offer '
                                'bilateral tympanostomy tubes.',
                 'curveball': 'Her younger brother has Down syndrome and a 2-month unilateral effusion with normal '
                              'hearing on the other side. Does the 3-month rule apply to him the same way?',
                 'curveball_answer': 'Not exactly. Down syndrome makes him an at-risk child, so the guideline asks '
                                     'clinicians to evaluate for OME, test hearing and consider tubes earlier when the '
                                     'effusion is unlikely to resolve quickly, because baseline developmental '
                                     'vulnerability magnifies the cost of hearing loss. His narrow ear canals may also '
                                     'need otomicroscopy for accurate diagnosis and tube surveillance.'},
 'v135_ped_03': {'stem': 'A 4-year-old boy has had bilateral middle-ear effusions for 5 months. His preschool teacher '
                         'reports inattention, and audiometry shows a bilateral 35 dB conductive loss with type B '
                         'tympanograms. He has no nasal obstruction or snoring. His parents would prefer a medication '
                         'if one would work and ask about a nasal steroid spray. What is the most appropriate '
                         'recommendation?',
                 'choices': ['Daily intranasal corticosteroid spray for 3 months, then recheck',
                             'Oral antihistamine-decongestant combination for 4 to 6 weeks',
                             'Tympanostomy tubes, with adenoidectomy as an option at his age',
                             'Watchful waiting until he starts kindergarten in 8 months'],
                 'answer': 2,
                 'explanation': 'Chronic bilateral OME with a 35 dB conductive loss and school-related symptoms meets '
                                'criteria for surgery. The 2016 OME guideline recommends against intranasal or '
                                'systemic steroids, antihistamines and decongestants because they do not hasten '
                                'durable resolution. For a surgical candidate, tubes are first line, and from about '
                                'age 4 adenoidectomy may be added because removing the adenoid reservoir lowers the '
                                'chance of repeat surgery. The deciding clues are effusion duration beyond 3 months, '
                                'measured hearing loss and functional impact.',
                 'why_wrong': ['Intranasal steroids are recommended against for OME in the 2016 guideline because they '
                               'do not produce lasting resolution of effusion.',
                               'Antihistamines and decongestants have no proven benefit for OME and carry side '
                               'effects, so the guideline recommends against them.',
                               'Correct.',
                               'He already has 5 months of effusion with a measured 35 dB loss and functional impact, '
                               'so prolonged waiting is not appropriate.'],
                 'board_pearl': 'Medications do not cure OME; at age 4 or older, adenoidectomy may accompany tubes to '
                                'reduce reoperation.',
                 'curveball': 'Eighteen months later his tubes have extruded and the effusion has returned bilaterally '
                              'for 4 months. What procedure does the guideline favor now?',
                 'curveball_answer': 'For recurrent OME after tube extrusion in a child 4 or older, the guidelines '
                                     'support adding adenoidectomy to repeat tubes if not already done, because '
                                     'adenoidectomy reduces further recurrence and repeat surgery in this age group. '
                                     'Adenoidectomy alone, with or without myringotomy, is also an option at this age, '
                                     'but the hearing loss argues for restoring ventilation with tubes.'},
 'v242_ped_ear_fnd': {'stem': 'A 3-year-old girl is seen 6 weeks after an episode of acute otitis media treated with '
                              'amoxicillin. She has no fever, ear pain or irritability and is eating well. Pneumatic '
                              'otoscopy of the right ear shows a mildly retracted, amber, poorly mobile tympanic '
                              'membrane with an air-fluid level and no bulging or erythema. Tympanometry is type B '
                              'with normal canal volume. Which diagnosis best fits?',
                      'choices': ['Acute otitis media that failed first-line therapy',
                                  'Retraction pocket with early acquired cholesteatoma',
                                  'Chronic suppurative otitis media behind an intact drum',
                                  'Otitis media with effusion from post-acute fluid'],
                      'answer': 3,
                      'explanation': 'OME is middle-ear fluid without signs or symptoms of acute infection. After AOM, '
                                     'effusion persists in many children for weeks to months, and an asymptomatic '
                                     'child with an amber, poorly mobile drum, an air-fluid level and a type B '
                                     'tympanogram has OME, not treatment failure. AOM requires acute symptoms plus '
                                     'inflammatory drum findings, classically moderate to severe bulging or new '
                                     'otorrhea. Correct labeling prevents unnecessary repeat antibiotics; OME is '
                                     'managed with 3 months of watchful waiting and hearing assessment if it persists.',
                      'why_wrong': ['Treatment failure requires persistent fever or otalgia with ongoing inflammatory '
                                    'findings, and she is asymptomatic without bulging or erythema.',
                                    'A mild retraction with an air-fluid level does not show the keratin debris or '
                                    'pocket erosion that define cholesteatoma.',
                                    'Chronic suppurative otitis media requires persistent otorrhea through a '
                                    'perforation, which is absent with an intact, nondraining drum.',
                                    'Correct.'],
                      'board_pearl': 'Asymptomatic fluid after AOM is OME, not treatment failure; do not retreat with '
                                     'antibiotics.',
                      'curveball': 'Her brother has a red tympanic membrane with fever and crying but no bulging. What '
                                   'otoscopic finding would be more specific for AOM than erythema alone?',
                      'curveball_answer': 'Moderate to severe bulging of the tympanic membrane, or new otorrhea not '
                                          'caused by otitis externa, is the key AAP diagnostic finding. Mild bulging '
                                          'with ear pain for less than 48 hours or intense erythema also qualifies. '
                                          'Erythema alone is nonspecific because crying and fever flush the drum, so a '
                                          'red but nonbulging membrane does not establish AOM.'},
 'v242_ped_ear_app': {'stem': 'A 30-month-old boy has had left ear pain for 18 hours that settles with ibuprofen. His '
                              'temperature is 38.2 C. The left tympanic membrane is bulging and opaque; the right is '
                              'normal, and there is no otorrhea. He has not received antibiotics in the past month and '
                              'has no penicillin allergy. His parents have a phone and can return within a day. What '
                              'is the most appropriate management?',
                      'choices': ['Observation for 48-72 hours with a rescue antibiotic plan',
                                  'High-dose amoxicillin-clavulanate for 10 days as required therapy',
                                  'Single intramuscular dose of ceftriaxone given in clinic today',
                                  'Ofloxacin otic drops twice daily for 7 days to the left ear'],
                      'answer': 0,
                      'explanation': 'The AAP 2013 guideline allows initial observation with shared decision-making '
                                     'for children 24 months or older with nonsevere AOM, defined as mild otalgia for '
                                     'less than 48 hours and temperature below 39 C, provided follow-up is assured. '
                                     'His unilateral disease, mild pain, low-grade fever and reliable family make '
                                     'observation reasonable, with antibiotics started if he worsens or fails to '
                                     'improve within 48-72 hours. Immediate high-dose amoxicillin is also acceptable, '
                                     'but it is not mandatory here.',
                      'why_wrong': ['Correct.',
                                    'Amoxicillin-clavulanate is reserved for recent amoxicillin use, concurrent '
                                    'conjunctivitis or treatment failure, and antibiotics are not mandatory in '
                                    'nonsevere disease.',
                                    'Ceftriaxone is reserved for children who cannot tolerate oral medication or who '
                                    'fail oral therapy, which does not describe this child.',
                                    'Topical drops cannot reach the middle ear through an intact tympanic membrane and '
                                    'are used for tube otorrhea or otitis externa.'],
                      'board_pearl': 'Nonsevere AOM at age 2 or older with reliable follow-up: observation with a '
                                     'rescue plan is acceptable.',
                      'curveball': 'How would bilateral AOM in a 12-month-old, otorrhea, severe otalgia, temperature '
                                   'of 39 C or higher, or unreliable follow-up change the plan?',
                      'curveball_answer': 'Each of these calls for immediate antibiotics. AAP criteria require '
                                          'treatment for any child with otorrhea or severe symptoms (moderate to '
                                          'severe otalgia, otalgia for 48 hours or more, or temperature of 39 C or '
                                          'higher) and for bilateral AOM in children 6-23 months. Use high-dose '
                                          'amoxicillin 80-90 mg/kg/day, typically for 10 days under age 2.'},
 'v242_ped_ear_snr': {'stem': 'A 5-year-old girl started amoxicillin for right AOM 3 days ago. She now has a '
                              'temperature of 39.4 C, worsening ear pain, postauricular erythema and tenderness, an '
                              'outwardly displaced auricle and loss of the postauricular crease. There is no '
                              'fluctuance, headache, neck stiffness, facial weakness or vertigo. The right drum is '
                              'bulging. What is the best next step?',
                      'choices': ['Switch to oral amoxicillin-clavulanate and recheck in 48 hours',
                                  'Admission, IV antibiotics and myringotomy with culture of fluid',
                                  'Cortical mastoidectomy tonight before antibiotic response is known',
                                  'MRI brain with venography before giving any IV antibiotic doses'],
                      'answer': 1,
                      'explanation': 'Postauricular erythema, tenderness and auricular protrusion after AOM define '
                                     'acute mastoiditis. Without fluctuance or neurologic signs, initial management is '
                                     'admission, broad IV antibiotics and myringotomy, often with tube placement, to '
                                     'drain the middle ear and obtain culture. Contrast-enhanced CT is obtained when a '
                                     'subperiosteal abscess, intracranial complication or coalescence is suspected, or '
                                     'when she fails to improve within 24-48 hours. Mastoidectomy is reserved for '
                                     'coalescent disease, complications or treatment failure.',
                      'why_wrong': ['Oral therapy is inadequate once infection has spread to the mastoid periosteum; '
                                    'she needs inpatient parenteral treatment and middle-ear drainage.',
                                    'Correct.',
                                    'Uncomplicated acute mastoiditis without abscess, coalescence or neurologic signs '
                                    'often resolves with IV antibiotics and myringotomy alone.',
                                    'Imaging is selected for suspected complications and should never delay '
                                    'antibiotics in a febrile child with mastoiditis.'],
                      'board_pearl': 'Acute mastoiditis: admit, IV antibiotics and myringotomy; image and operate for '
                                     'abscess, complication or failure.',
                      'curveball': 'Which findings would make you obtain urgent contrast imaging and proceed more '
                                   'quickly to drainage or mastoidectomy rather than relying on IV antibiotics?',
                      'curveball_answer': 'Postauricular fluctuance suggesting subperiosteal abscess, headache, '
                                          'lethargy, meningismus, abducens palsy (Gradenigo syndrome), facial palsy, '
                                          'vertigo, or signs of sigmoid sinus thrombosis such as papilledema all need '
                                          'urgent contrast CT, with MRI and MRV if intracranial disease is suspected. '
                                          'Subperiosteal abscess needs drainage with or without mastoidectomy, and '
                                          'coalescence or intracranial extension favors mastoidectomy.'},
 'v11_ped_02': {'stem': 'A 5-year-old boy with normal weight and no other medical problems has loud nightly snoring, '
                        'witnessed pauses and daytime irritability. Tonsils are 4+ and kissing. Polysomnography shows '
                        'an obstructive apnea-hypopnea index of 28 events per hour with an oxygen saturation nadir of '
                        '76%. He is scheduled for adenotonsillectomy as the first case of the day. Which perioperative '
                        'plan is most appropriate?',
                'choices': ['Same-day discharge after 4 hours of normal saturations in recovery',
                            'Planned ICU admission with elective overnight postoperative intubation',
                            'Overnight stay only if airway difficulty occurs during the anesthetic',
                            'Overnight inpatient admission with continuous pulse oximetry'],
                'answer': 3,
                'explanation': 'The 2019 AAO-HNSF tonsillectomy guideline recommends overnight inpatient monitoring '
                               'after adenotonsillectomy for children with severe OSA, defined as an AHI of 10 or '
                               'more, an oxygen nadir below 80%, or both, and for all children younger than 3. His AHI '
                               'of 28 and nadir of 76% predict postoperative obstruction and desaturation, which peak '
                               'the first night as anesthetic, opioid and edema effects combine. Chronic intermittent '
                               'hypoxemia also up-regulates opioid sensitivity, so analgesia should be opioid-sparing.',
                'why_wrong': ['Normal saturations in recovery do not predict first-night events; severe OSA by AHI and '
                              'nadir criteria warrants overnight monitoring.',
                              'Routine ICU care with elective intubation is reserved for selected children with major '
                              'cardiopulmonary or craniofacial comorbidity, not otherwise healthy severe OSA.',
                              'Admission is decided by preoperative PSG severity and age, not by whether the '
                              'intraoperative course happens to be smooth.',
                              'Correct.'],
                'board_pearl': 'Admit overnight after adenotonsillectomy if age under 3, AHI of 10 or more, or nadir '
                               'below 80%.',
                'curveball': 'He is obese with severe OSA, and symptoms persist 3 months after adenotonsillectomy. '
                             'What should the next evaluation focus on before choosing additional therapy?',
                'curveball_answer': 'Obtain repeat polysomnography to quantify residual OSA, because obesity is a '
                                    'leading predictor of persistent disease. If significant OSA remains, define the '
                                    'sites of collapse with drug-induced sleep endoscopy or cine MRI, looking for '
                                    'lingual tonsils, adenoid regrowth or multilevel collapse, and pair any targeted '
                                    'therapy with weight management. CPAP is a strong option for obesity-driven '
                                    'residual OSA.'},
 'v113-ped-05': {'stem': 'An 8-year-old girl with Down syndrome had adenotonsillectomy 9 months ago for severe OSA. '
                         'Her parents report that she still snores most nights, sleeps with her neck hyperextended and '
                         'is more irritable at school. Her BMI is at the 90th percentile. Exam shows healed tonsillar '
                         'fossae, macroglossia and midface hypoplasia. Flexible nasopharyngoscopy shows no adenoid '
                         'regrowth. What is the best next step?',
                 'choices': ['Reassure the family that residual snoring resolves with growth',
                             'Repeat polysomnography to quantify residual obstructive apnea',
                             'Lingual tonsillectomy based on the history and examination',
                             'Montelukast and nasal steroid trial without further testing'],
                 'answer': 1,
                 'explanation': 'Children with Down syndrome have high rates of persistent OSA after '
                                'adenotonsillectomy because of macroglossia, midface hypoplasia, hypotonia, lingual '
                                'tonsil hypertrophy and obesity. Symptoms and exam do not reliably predict residual '
                                'severity, so guideline-endorsed care is repeat polysomnography when symptoms persist. '
                                'Objective results determine whether she needs further treatment and set the stage for '
                                'DISE or cine MRI to localize multilevel collapse before choosing CPAP, site-directed '
                                'surgery or, in adolescents, hypoglossal nerve stimulation.',
                 'why_wrong': ['Residual OSA in Down syndrome is common and harmful; persistent symptoms need '
                               'objective testing rather than reassurance.',
                               'Correct.',
                               'Lingual tonsillectomy without documenting residual OSA and localizing collapse risks '
                               'an operation that does not address the actual obstruction.',
                               'Anti-inflammatory therapy is reasonable for mild disease, but severity must be '
                               'measured first in a high-risk child with persistent symptoms.'],
                 'board_pearl': 'Persistent symptoms after adenotonsillectomy in Down syndrome: repeat PSG before '
                                'choosing more therapy.',
                 'curveball': 'At 14, she still has moderate OSA, cannot tolerate CPAP and her BMI is stable. Which '
                              'DISE finding would argue against hypoglossal nerve stimulation?',
                 'curveball_answer': 'Complete concentric collapse at the velum on DISE argues against hypoglossal '
                                     'nerve stimulation, because tongue protrusion does not relieve circumferential '
                                     'palatal collapse. Stimulation is FDA-approved for adolescents 13 and older with '
                                     'Down syndrome and moderate to severe OSA who cannot use CPAP, and works best '
                                     'when obstruction is mainly anteroposterior at the tongue base and palate.'},
 'v124_ped_02': {'stem': 'An 8-year-old boy has loud nightly snoring, witnessed apneas, restless sleep and behavioral '
                         'problems at school. His BMI is at the 98th percentile. Tonsils are 3+ and ear examination is '
                         'normal. He had one episode of streptococcal pharyngitis last year. His pediatrician has '
                         'referred him for adenotonsillectomy. Which feature most supports obtaining polysomnography '
                         'before surgery?',
                 'choices': ['His obesity, which raises severity and perioperative risk',
                             'His 3+ tonsils, which predict OSA severity on testing',
                             'His school behavior problems, which confirm severe disease',
                             'His witnessed apneas, which document obstructive events'],
                 'answer': 0,
                 'explanation': 'The AAO-HNSF polysomnography guideline recommends PSG before tonsillectomy in '
                                'children with obesity, Down syndrome, craniofacial abnormalities, neuromuscular '
                                'disorders, sickle cell disease or mucopolysaccharidoses. Obesity increases the '
                                'likelihood of severe OSA, postoperative respiratory complications and residual '
                                'disease, so objective severity guides disposition and counseling. In an otherwise '
                                'healthy child, symptoms with large tonsils can justify surgery without PSG; tonsil '
                                'size, behavior and parental reports correlate poorly with measured severity.',
                 'why_wrong': ['Correct.',
                               'Tonsil size correlates poorly with AHI, so large tonsils do not establish severity or '
                               'by themselves mandate PSG.',
                               'Behavioral symptoms support a clinical diagnosis of sleep-disordered breathing but do '
                               'not grade severity or make PSG necessary in healthy children.',
                               'Parent-reported apneas are common in sleep-disordered breathing and do not distinguish '
                               'primary snoring from moderate or severe OSA.'],
                 'board_pearl': 'Obtain PSG before tonsillectomy for obesity, Down syndrome, craniofacial, '
                                'neuromuscular or sickle cell disease.',
                 'curveball': 'After adenotonsillectomy his symptoms persist, and PSG still shows severe OSA. What '
                              'should the next evaluation focus on rather than repeating the same operation?',
                 'curveball_answer': 'Focus on the residual sites and drivers of obstruction. DISE or cine MRI can '
                                     'show lingual tonsil hypertrophy, adenoid regrowth, tongue-base or epiglottic '
                                     'collapse, and nasal obstruction, while weight trajectory and hypoventilation on '
                                     'PSG show the obesity contribution. CPAP is usually the first-line treatment for '
                                     'obesity-related residual OSA, with targeted surgery and weight management chosen '
                                     'by the findings.'},
 'v140_ped_07': {'stem': 'A 7-year-old boy with trisomy 21 and a BMI above the 97th percentile is scheduled for '
                         'adenotonsillectomy. Preoperative polysomnography shows an obstructive AHI of 22 events per '
                         'hour, a saturation nadir of 79% and end-tidal CO2 above 50 mm Hg for 30% of total sleep '
                         'time. Screening for atlantoaxial instability was unremarkable. Which postoperative '
                         'disposition is most appropriate?',
                 'choices': ['Discharge home if he tolerates fluids within 6 hours of surgery',
                             'Overnight observation on the ward with intermittent spot checks',
                             'Monitored inpatient bed with continuous oximetry and capnography',
                             'Planned postoperative intubation with ICU care for 48 hours'],
                 'answer': 2,
                 'explanation': 'Severe OSA, obesity, Down syndrome and hypoventilation each raise the risk of '
                                'postoperative obstruction, desaturation and opioid sensitivity, and together they '
                                'mandate overnight admission with continuous monitoring. Hypotonia, macroglossia and '
                                'midface hypoplasia keep the airway collapsible after the tonsils are removed, and '
                                'hypercapnia signals reduced respiratory drive under sedatives. A monitored bed with '
                                'continuous oximetry, ideally capnography, allows early recognition and treatment with '
                                'positioning, airway adjuncts or CPAP. Escalation to ICU depends on observed events '
                                'and comorbidities.',
                 'why_wrong': ['Early oral intake does not offset the first-night respiratory risk created by severe '
                               'OSA, hypoventilation, obesity and trisomy 21.',
                               'Intermittent checks miss the clustered desaturation and hypoventilation that occur '
                               'during the first night in high-risk children.',
                               'Correct.',
                               'Elective postoperative intubation is not routine; most high-risk children are safely '
                               'managed with continuous monitoring and noninvasive support.'],
                 'board_pearl': 'Severe OSA plus syndromic hypotonia, obesity or hypoventilation demands continuous '
                                'postoperative monitoring.',
                 'curveball': 'How should opioid-sparing analgesia be approached in this child after surgery?',
                 'curveball_answer': 'Schedule acetaminophen and ibuprofen as the analgesic base, since the 2019 '
                                     'guideline supports ibuprofen without increased bleeding risk, and add '
                                     'intraoperative dexamethasone. Codeine and tramadol are contraindicated in '
                                     'children after tonsillectomy because of ultrarapid metabolism deaths. If an '
                                     'opioid is needed, use reduced, titrated doses under monitoring, because '
                                     'intermittent hypoxemia increases opioid sensitivity.'},
 'v242_ped_osa_fnd': {'stem': 'A 6-year-old girl, otherwise healthy with normal weight, has nightly snoring, witnessed '
                              'pauses, mouth breathing and declining school performance. Her tonsils are 1+ and her '
                              'adenoids are small on flexible nasopharyngoscopy. Her parents ask whether her tonsils '
                              'should be removed. Home overnight oximetry arranged by her pediatrician was read as '
                              'normal. What is the most appropriate next step?',
                      'choices': ['Adenotonsillectomy based on the history of witnessed pauses',
                                  'Reassurance, because small tonsils exclude significant OSA',
                                  'Overnight polysomnography before deciding on any surgery',
                                  'No further testing, because normal oximetry excludes OSA'],
                      'answer': 2,
                      'explanation': 'OSA is a physiologic diagnosis made during sleep, and history and awake anatomy '
                                     'only raise suspicion. The polysomnography guideline recommends PSG when the need '
                                     'for surgery is uncertain or when tonsil size does not match the reported '
                                     'severity of sleep-disordered breathing. Her small tonsils and adenoid make '
                                     'adenotonsillectomy less likely to help, yet her symptoms are significant. Normal '
                                     'overnight oximetry has a poor negative predictive value because events with '
                                     'arousal but no desaturation are missed, so it cannot exclude OSA.',
                      'why_wrong': ['With 1+ tonsils and a small adenoid, the benefit of surgery is uncertain and '
                                    'objective severity should be defined first.',
                                    'Small tonsils do not exclude OSA; nasal, lingual, craniofacial or neuromuscular '
                                    'factors can cause significant obstruction.',
                                    'Correct.',
                                    'Oximetry misses hypopneas scored by arousal and events without desaturation, so a '
                                    'normal study does not rule out OSA.'],
                      'board_pearl': 'Tonsil size does not measure OSA; order PSG when anatomy and symptoms disagree.',
                      'curveball': 'Which comorbid children merit a lower threshold for preoperative polysomnography '
                                   'even when tonsils are large?',
                      'curveball_answer': 'Children with obesity, Down syndrome, craniofacial anomalies, neuromuscular '
                                          'disorders, sickle cell disease or mucopolysaccharidoses should have PSG '
                                          'before tonsillectomy. They have higher rates of severe OSA, postoperative '
                                          'respiratory complications and residual disease after surgery, so objective '
                                          'baseline severity guides disposition, anesthetic planning and postoperative '
                                          'reassessment.'},
 'v242_ped_osa_app': {'stem': 'A 26-month-old boy born at term, with normal growth and no other medical conditions, '
                              'has nightly snoring with witnessed pauses. Polysomnography shows an obstructive AHI of '
                              '6 events per hour with a saturation nadir of 86%. Tonsils are 3+. The family lives 20 '
                              'minutes from the hospital and asks whether he can go home the same day after '
                              'adenotonsillectomy. What disposition is most appropriate?',
                      'choices': ['Same-day discharge, because his OSA is only moderate',
                                  'Same-day discharge if he drinks and voids before leaving',
                                  'Overnight admission only if bleeding occurs during surgery',
                                  'Planned overnight inpatient admission with pulse oximetry'],
                      'answer': 3,
                      'explanation': 'The 2019 AAO-HNSF tonsillectomy guideline recommends overnight inpatient '
                                     'monitoring for children with OSA who are younger than 3, regardless of AHI, as '
                                     'well as for children with severe OSA. Young children have smaller airways, less '
                                     'respiratory reserve and higher rates of postoperative respiratory compromise, '
                                     'dehydration and poor oral intake. His moderate AHI would allow outpatient '
                                     'surgery at an older age, but his age of 26 months is the deciding factor. '
                                     'Proximity to the hospital does not offset this risk.',
                      'why_wrong': ['Age younger than 3 is an independent indication for admission, so moderate '
                                    'severity does not permit same-day discharge in this child.',
                                    'Early oral intake is necessary but does not address the higher first-night '
                                    'respiratory risk in children younger than 3.',
                                    'Admission is planned from age and PSG severity, not from intraoperative bleeding, '
                                    'which is uncommon and managed separately.',
                                    'Correct.'],
                      'board_pearl': 'Children with OSA under 3 years old stay overnight after adenotonsillectomy even '
                                     'when OSA is moderate.',
                      'curveball': 'How do obesity, Down syndrome, craniofacial disease, neuromuscular weakness or '
                                   'hypoventilation change postoperative planning?',
                      'curveball_answer': 'Each lowers the threshold for overnight continuous monitoring and may '
                                          'justify a high-dependency or ICU bed, especially when combined with severe '
                                          'OSA. These children need preoperative PSG, anesthesia planning for '
                                          'difficult airway or hypotonia, opioid-sparing analgesia and early access to '
                                          'CPAP or airway adjuncts, and they need postoperative PSG because residual '
                                          'OSA is common.'},
 'v242_ped_osa_snr': {'stem': 'A 7-year-old girl with normal weight and no syndromic features had adenotonsillectomy '
                              'for moderate OSA 6 months ago. She still snores and has daytime fatigue. Repeat '
                              'polysomnography shows an obstructive AHI of 9 events per hour. Examination shows healed '
                              'tonsillar fossae, a normal palate and turbinates without significant hypertrophy, and '
                              'flexible nasopharyngoscopy shows no adenoid regrowth. What is the best next step?',
                      'choices': ['Sleep endoscopy or cine MRI to localize collapse, discussing CPAP',
                                  'Hypoglossal nerve stimulator implantation after a CPAP trial',
                                  'Empiric lingual tonsillectomy with supraglottoplasty at one sitting',
                                  'Repeat polysomnography in 12 months without interim treatment'],
                      'answer': 0,
                      'explanation': 'Persistent moderate OSA after adenotonsillectomy is often due to lingual tonsil '
                                     'hypertrophy, tongue-base or epiglottic collapse, or other airway levels not '
                                     'addressed at the first operation. Because her exam explains no obvious residual '
                                     'obstruction, the next step is to localize collapse with drug-induced sleep '
                                     'endoscopy or cine MRI, which allows site-directed surgery only where obstruction '
                                     'is shown. CPAP is an effective alternative and should be discussed alongside any '
                                     'surgical plan. Moderate residual OSA should not be left untreated.',
                      'why_wrong': ['Correct.',
                                    'Hypoglossal stimulation is approved only for adolescents with Down syndrome in '
                                    'the pediatric population, so a nonsyndromic 7-year-old is not a candidate.',
                                    'Operating on the lingual tonsils and supraglottis without first documenting '
                                    'collapse at those levels risks morbidity without benefit.',
                                    'An AHI of 9 with symptoms is moderate disease that carries neurocognitive and '
                                    'behavioral harm and needs treatment, not a year of observation.'],
                      'board_pearl': 'Residual OSA after adenotonsillectomy: localize collapse with DISE or cine MRI '
                                     'before more surgery; CPAP is an alternative.',
                      'curveball': 'When is DISE most useful, and when would CPAP be preferable to another operation?',
                      'curveball_answer': 'DISE is most useful when residual OSA is significant and the cause is not '
                                          'evident awake, especially to show lingual tonsil, tongue-base, epiglottic '
                                          'or multilevel collapse that a single procedure could fix. CPAP is '
                                          'preferable when obstruction is diffuse or multilevel, when obesity or '
                                          'hypotonia drives collapse, or when surgical risks outweigh expected gain.'},
 'v11_ped_03': {'stem': 'A 3-year-old boy suddenly coughed and gagged while eating peanuts at a party 4 hours ago. He '
                        'now has an intermittent cough, a respiratory rate of 30 and an oxygen saturation of 96% on '
                        'room air. Auscultation reveals expiratory wheeze and decreased breath sounds over the right '
                        'lung. Frontal and lateral chest radiographs are read as normal. What is the best next step?',
                'choices': ['Albuterol trial with discharge if the wheeze clears',
                            'Rigid bronchoscopy under general anesthesia today',
                            'Low-dose chest CT to confirm before any endoscopy',
                            'Chest physiotherapy with postural drainage first'],
                'answer': 1,
                'explanation': 'A witnessed choking episode followed by unilateral wheeze and decreased breath sounds '
                               'carries a high probability of airway foreign body, and the history is the most '
                               'sensitive single clue. Peanuts are radiolucent, and plain films are normal in a '
                               'substantial share of confirmed cases, so a normal radiograph does not lower suspicion '
                               'enough to avoid endoscopy. Rigid bronchoscopy is both diagnostic and therapeutic, and '
                               'delay increases the risk of pneumonia, granulation and difficult extraction. CT is '
                               'reserved for cases where suspicion is low or equivocal.',
                'why_wrong': ['Bronchodilator response does not exclude a foreign body, and discharge risks migration, '
                              'complete obstruction or postobstructive pneumonia.',
                              'Correct.',
                              'With a convincing history and focal findings, CT adds radiation and delay without '
                              'changing the need for bronchoscopy.',
                              'Postural drainage can dislodge a bronchial foreign body into the trachea or glottis and '
                              'cause complete obstruction.'],
                'board_pearl': 'Convincing choking history plus focal chest findings means bronchoscopy, even with '
                               'normal radiographs.',
                'curveball': 'Bronchoscopy shows a peanut tightly wedged in the right mainstem with mucosal edema. '
                             'What extraction and postoperative airway considerations matter?',
                'curveball_answer': 'Grasp the peanut gently with optical forceps to avoid fragmentation, and withdraw '
                                    'the forceps, object and bronchoscope together as a unit if the object is larger '
                                    'than the scope lumen. Then reinspect both bronchial trees for fragments. Edema '
                                    'may justify a short course of systemic steroids, and the child should be observed '
                                    'for postextraction stridor, pneumonia and retained fragments.'},
 'v116-ped-03': {'stem': 'A 2-year-old girl choked on raw carrot pieces 2 days ago, coughed hard for several minutes, '
                         'then seemed fine. She now has a low-grade fever, persistent cough and decreased breath '
                         'sounds at the right base. A chest radiograph shows a subtle right lower lobe opacity. Her '
                         'pediatrician started amoxicillin for pneumonia, and her parents ask whether finishing the '
                         'course is enough. What is the best next step?',
                 'choices': ['Complete 10 days of amoxicillin and repeat radiographs in 4 weeks',
                             'Admit for IV antibiotics and scope if no improvement in 72 hours',
                             'Sweat chloride test to evaluate for underlying cystic fibrosis',
                             'Rigid bronchoscopy to look for and remove an aspirated fragment'],
                 'answer': 3,
                 'explanation': 'Choking followed by a symptom-free interval and then focal pneumonia is a classic '
                                'delayed presentation of aspirated food. The initial cough subsides as receptors '
                                'adapt, and obstruction later causes distal atelectasis and infection. The witnessed '
                                'choking event is the deciding clue: it makes the pneumonia postobstructive until '
                                'proven otherwise. Antibiotics may improve fever temporarily but cannot clear the '
                                'obstruction, and vegetable matter swells and incites granulation over time. Rigid '
                                'bronchoscopy is diagnostic and therapeutic and should not wait for antibiotic '
                                'failure.',
                 'why_wrong': ['Treating presumed pneumonia while a fragment remains allows recurrent infection, '
                               'granulation and possible bronchiectasis distal to the obstruction.',
                               'Waiting for antibiotic failure delays extraction of an organic object that swells and '
                               'inflames the bronchus over time.',
                               'Cystic fibrosis is not suggested by a single focal pneumonia after a witnessed choking '
                               'episode in an otherwise healthy toddler.',
                               'Correct.'],
                 'board_pearl': 'Recurrent or persistent focal pneumonia after a choking episode is a foreign body '
                                'until bronchoscopy proves otherwise.',
                 'curveball': 'What changes if the object is suspected in the larynx or proximal trachea rather than a '
                              'mainstem bronchus?',
                 'curveball_answer': 'A laryngeal or tracheal object threatens complete obstruction, so the child '
                                     'should stay calm and upright with minimal manipulation, go straight to the OR, '
                                     'and receive an inhalational induction with spontaneous ventilation. Have rigid '
                                     'bronchoscopes and a surgical airway ready. If total obstruction occurs and the '
                                     'object cannot be retrieved, pushing it into a mainstem bronchus can restore '
                                     'ventilation to one lung.'},
 'v135_ped_01': {'stem': 'A 9-year-old boy was chewing a plastic pen cap in class when he inhaled sharply and began '
                         'coughing. Thirty minutes later in the emergency department he speaks in full sentences with '
                         'a saturation of 97% but has persistent cough and a localized wheeze over the left chest. '
                         'Inspiratory chest radiograph is normal. He insists the cap went down the wrong way. What is '
                         'the best next step?',
                 'choices': ['Rigid bronchoscopy to examine and clear the bronchial tree',
                             'Back blows and abdominal thrusts while he remains awake',
                             'Discharge with return precautions, since he speaks in sentences',
                             'Expiratory and decubitus films, discharging him if they are normal'],
                 'answer': 0,
                 'explanation': 'Pen caps are radiolucent plastic, so a normal inspiratory film is expected. In an '
                                'older child who can describe the event, a credible aspiration history with persistent '
                                'cough and focal wheeze is enough to proceed to rigid bronchoscopy. Ancillary films '
                                'may show air trapping, but normal results do not exclude a foreign body and should '
                                'not override the history. Bronchoscopy under general anesthesia with a ventilating '
                                'scope allows controlled retrieval.',
                 'why_wrong': ['Correct.',
                               'Choking maneuvers are for complete obstruction with inability to speak or cough; in a '
                               'child who is ventilating they can convert partial obstruction into complete '
                               'obstruction.',
                               'Speaking normally means the object is below the larynx; it does not mean the airway is '
                               'clear, and the bronchial object can migrate.',
                               'Expiratory or decubitus films have limited sensitivity, so a normal result cannot '
                               'justify discharge after a credible aspiration history.'],
                 'board_pearl': 'Plastic is radiolucent: a credible aspiration history beats a normal film.',
                 'curveball': 'The child becomes completely obstructed during induction. What is the immediate airway '
                              'strategy?',
                 'curveball_answer': 'Pass the rigid ventilating bronchoscope immediately, since a dislodged object '
                                     'most likely lodged in the trachea or subglottis. If the object cannot be grasped '
                                     'and removed at once, advance it with the scope into a mainstem bronchus to '
                                     'ventilate the other lung, then retrieve it. A surgical airway is rarely helpful '
                                     'because the obstruction is usually below the tracheostomy site.'},
 'v140_ped_03': {'stem': 'A 3-year-old boy was diagnosed with new-onset asthma 3 weeks ago after the abrupt start of '
                         'cough and wheeze. Despite inhaled corticosteroids and albuterol he still coughs daily, and '
                         'every examiner has documented wheeze only over the left chest. His grandmother recalls that '
                         'he choked on mixed nuts at a family party the day before symptoms began. Chest radiographs '
                         'are normal. What is the best next step?',
                 'choices': ['Add montelukast and step up the inhaled corticosteroid dose',
                             'Spirometry and allergy testing to refine the asthma diagnosis',
                             'Rigid bronchoscopy to evaluate a retained airway object',
                             'Repeat chest radiograph only if fever or hypoxemia develops'],
                 'answer': 2,
                 'explanation': 'Delayed diagnosis of airway foreign body often follows misattribution to asthma or '
                                'bronchitis. The deciding clues are an abrupt onset after a choking episode, a '
                                'strictly unilateral fixed wheeze, which asthma does not produce, and poor response to '
                                'asthma therapy. Nuts are radiolucent and often produce normal films. Rigid '
                                'bronchoscopy should be performed promptly, because nuts absorb water, fragment and '
                                'provoke granulation that makes later extraction harder and increases the risk of '
                                'bronchiectasis.',
                 'why_wrong': ['Escalating asthma therapy ignores a strictly unilateral wheeze and a choking history '
                               'that point to a mechanical obstruction.',
                               'Spirometry is unreliable at age 3, and allergy testing does not address the likely '
                               'retained foreign body.',
                               'Correct.',
                               'Waiting for fever accepts postobstructive pneumonia and granulation that make '
                               'extraction harder and outcomes worse.'],
                 'board_pearl': 'Unilateral wheeze that fails asthma therapy: ask about choking and bronchoscope.',
                 'curveball': 'What radiographic expiratory or decubitus findings may reveal air trapping before '
                              'bronchoscopy?',
                 'curveball_answer': 'Expiratory films, or lateral decubitus films in children too young to cooperate, '
                                     'may show the obstructed lung staying hyperlucent and inflated while the normal '
                                     'side deflates. On decubitus views the dependent obstructed lung fails to lose '
                                     'volume, and the mediastinum shifts away from the obstructed side on expiration. '
                                     'These signs support the diagnosis, but a normal study does not exclude it.'},
 'v242_ped_fb_fnd': {'stem': 'A 20-month-old girl coughed, gagged and turned red while eating sunflower seeds 6 hours '
                             'ago. She now has persistent cough and a faint wheeze over the right lung. Frontal and '
                             'lateral chest radiographs are normal, without air trapping or atelectasis. A medical '
                             'student asks why the team is booking the operating room when the films are normal. Which '
                             'principle best explains the decision?',
                     'choices': ['Most aspirated foods are radiolucent and may not yet trap air',
                                 'Plain films become falsely negative only once 24 hours have passed',
                                 'Normal films exclude a proximal object but not a distal bronchial one',
                                 'Bronchoscopy is required whenever any toddler has new focal wheeze'],
                     'answer': 0,
                     'explanation': 'Most pediatric airway foreign bodies are organic, such as nuts and seeds, and are '
                                    'radiolucent. Indirect signs such as hyperinflation, atelectasis or mediastinal '
                                    'shift depend on the degree of obstruction and time, so films are often normal in '
                                    'the first hours. History is the most sensitive element of the evaluation, and a '
                                    'witnessed choking or penetration event with focal findings justifies bronchoscopy '
                                    'despite normal imaging. Missing a foreign body has far greater morbidity than a '
                                    'negative bronchoscopy.',
                     'why_wrong': ['Correct.',
                                   'Plain films can be normal at any time, and radiographic signs of obstruction often '
                                   'take hours to days to appear rather than disappearing after a day.',
                                   'A radiolucent object anywhere in the airway, including the trachea, can produce '
                                   'normal radiographs.',
                                   'Focal wheeze without a choking history usually reflects infection or asthma; the '
                                   'history is what makes bronchoscopy necessary here.'],
                     'board_pearl': 'Most aspirated objects are organic and radiolucent; history drives bronchoscopy.',
                     'curveball': 'What inspiratory-expiratory or decubitus radiographic findings can indirectly '
                                  'suggest unilateral bronchial obstruction?',
                     'curveball_answer': 'A check-valve obstruction lets air in but not out, so the obstructed lung '
                                         'stays hyperinflated and hyperlucent on expiration while the mediastinum '
                                         'shifts toward the normal side. On a lateral decubitus film the dependent '
                                         'obstructed lung fails to deflate. Complete obstruction causes atelectasis '
                                         'instead. Fluoroscopy can show the same dynamic shift.'},
 'v242_ped_fb_app': {'stem': 'A 3-year-old girl aspirated a small plastic toy bead 5 hours ago. She is stable with a '
                             'saturation of 97% on room air, intermittent cough and decreased breath sounds on the '
                             'left. Expiratory films show left-sided air trapping. Anesthesia and otolaryngology are '
                             'planning removal, and a pulmonology fellow offers bedside flexible bronchoscopy under '
                             'sedation. Which removal strategy is most appropriate?',
                     'choices': ['Flexible bronchoscopy with a basket under moderate sedation',
                                 'Bronchoscopy after 48 hours of steroids to shrink the edema',
                                 'Thoracotomy with bronchotomy to remove the bead under vision',
                                 'Rigid ventilating bronchoscopy with optical forceps under anesthesia'],
                     'answer': 3,
                     'explanation': 'Rigid ventilating bronchoscopy remains the standard for pediatric airway foreign '
                                    'body removal. It secures the airway, allows ventilation through the scope during '
                                    'extraction, provides optical forceps with excellent visualization, and permits '
                                    'the object, forceps and scope to be withdrawn together. Surgeon and '
                                    'anesthesiologist should agree beforehand on spontaneous versus controlled '
                                    'ventilation and on a rescue plan if the object is dislodged. Flexible '
                                    'bronchoscopy is useful for diagnosis or distal objects but offers less airway '
                                    'control.',
                     'why_wrong': ['Flexible scopes do not secure the airway; losing a smooth bead at the glottis '
                                   'under sedation could cause complete obstruction.',
                                   'Delay allows migration, edema and infection, and preoperative steroids do not '
                                   "replace prompt removal of a stable child's foreign body.",
                                   'Open bronchotomy is reserved for objects that cannot be removed endoscopically, '
                                   'such as distal impactions after failed bronchoscopy.',
                                   'Correct.'],
                     'board_pearl': 'Rigid ventilating bronchoscopy with optical forceps is the standard for pediatric '
                                    'airway foreign bodies.',
                     'curveball': 'How do friable organic objects, sharp objects, or a proximal object near the '
                                  'glottis change extraction technique?',
                     'curveball_answer': 'Friable nuts need gentle grasping and often piecemeal removal with suction '
                                         'and repeat inspection for fragments. Sharp objects such as pins should be '
                                         'sheathed in the scope or turned so the point trails during withdrawal. '
                                         'Objects near the glottis call for spontaneous ventilation, minimal '
                                         'manipulation and readiness to push the object distally if obstruction '
                                         'occurs.'},
 'v242_ped_fb_snr': {'stem': 'A 2-year-old boy undergoes rigid bronchoscopy for an almond aspirated 5 days ago. The '
                             'almond fragments as it is grasped, and two large pieces are removed from the right '
                             'mainstem bronchus. Saturations improve, but the bronchial mucosa is edematous with '
                             'granulation tissue where the nut sat. The fellow suggests ending the case. What should '
                             'the team do before concluding the procedure?',
                     'choices': ['Reinspect both bronchial trees to clear fragments and assess injury',
                                 'Extubate and obtain a chest radiograph in recovery to find fragments',
                                 'Give systemic steroids and end the case without further endoscopy',
                                 'Book second-look bronchoscopy in 1 week but end the case now'],
                     'answer': 0,
                     'explanation': 'Nuts fragment easily, and retained pieces or a second object are well-recognized '
                                    'causes of persistent symptoms after bronchoscopy. Before the case ends, the '
                                    'surgeon should systematically reinspect the trachea and both bronchial trees, '
                                    'including segmental orifices, suction secretions and assess mucosal injury. '
                                    'Granulation from delayed removal can hide fragments distally. Postoperative care '
                                    'is guided by what is found, with steroids considered for edema and repeat '
                                    'bronchoscopy for persistent findings rather than as routine.',
                     'why_wrong': ['Correct.',
                                   'Plain films cannot show radiolucent nut fragments, so a normal radiograph does not '
                                   'exclude retained pieces.',
                                   'Steroids may help edema, but they do not replace a final inspection to exclude '
                                   'retained fragments.',
                                   'Routine second-look bronchoscopy is not needed when a careful final inspection is '
                                   'clear; it is reserved for persistent findings.'],
                     'board_pearl': 'Organic foreign bodies fragment: always reinspect the whole tracheobronchial tree '
                                    'before ending.',
                     'curveball': 'Two days later he still has fever and right-sided wheeze. Which postoperative '
                                  'findings would trigger repeat bronchoscopy or chest imaging?',
                     'curveball_answer': 'Persistent or new unilateral wheeze, decreased breath sounds, ongoing fever, '
                                         'recurrent pneumonia in the same lobe, persistent air trapping or atelectasis '
                                         'on radiographs, or unexplained hypoxemia suggest a retained fragment or '
                                         'complication. These findings call for repeat bronchoscopy, while chest '
                                         'imaging or CT is used to look for pneumothorax, abscess or bronchiectasis '
                                         'after delayed removal.'},
 'v11_ped_04': {'stem': 'A 2-month-old girl born at term has had inspiratory stridor since 2 weeks of age that is '
                        'louder with feeding, crying and lying supine. She has a strong cry, occasional mild spit-up, '
                        'no cyanotic or apneic episodes, and her weight has tracked along the 50th percentile. Awake '
                        'flexible laryngoscopy shows an omega-shaped epiglottis, short aryepiglottic folds and '
                        'inspiratory prolapse of arytenoid mucosa. What is the best management?',
                'choices': ['Supraglottoplasty now to prevent later feeding problems',
                            'Polysomnography before deciding whether to observe her',
                            'Observation with feeding guidance and scheduled follow-up',
                            'Microlaryngoscopy and bronchoscopy to exclude other lesions'],
                'answer': 2,
                'explanation': 'Laryngomalacia is the most common cause of infant stridor and is graded by its '
                               'physiologic consequences. This infant has typical inspiratory stridor worse with '
                               'feeding and supine positioning, confirmed by awake laryngoscopy, with normal growth '
                               'and no apnea, cyanosis or significant retractions. That is mild disease, which usually '
                               'peaks around 6 months and resolves by 12-18 months. Management is observation with '
                               'feeding strategies, reflux management only if symptomatic, and regular weight and '
                               'symptom checks.',
                'why_wrong': ['Surgery is reserved for severe disease with failure to thrive, apnea, cyanosis or '
                              'significant feeding morbidity, none of which she has.',
                              'PSG is useful when obstructive sleep apnea or hypoxemia is suspected, but it is not '
                              'needed for mild laryngomalacia with normal growth.',
                              'Correct.',
                              'Operative airway endoscopy is reserved for atypical, severe or progressive cases; '
                              'synchronous lesions are uncommon in mild typical disease.'],
                'board_pearl': 'Mild laryngomalacia with normal growth and no apnea or cyanosis: observe and follow '
                               'weight.',
                'curveball': 'At 3 months she begins losing weight and has two cyanotic spells during feeds. What '
                             'findings now make supraglottoplasty appropriate?',
                'curveball_answer': 'Failure to thrive, cyanotic or apneic episodes, hypoxemia, significant '
                                    'retractions, feeding-related aspiration or cor pulmonale define severe '
                                    'laryngomalacia and justify supraglottoplasty. Before surgery, perform '
                                    'microlaryngoscopy and bronchoscopy to look for synchronous lesions, and assess '
                                    'swallowing, because aspiration and neurologic comorbidity change the operative '
                                    'plan and prognosis.'},
 'v142_ped_01': {'stem': 'A 3-month-old boy with laryngomalacia diagnosed at 3 weeks has worsening inspiratory stridor '
                         'with suprasternal and subcostal retractions. His weight has fallen from the 50th to below '
                         'the 5th percentile despite thickened feeds and acid suppression, and he has had three '
                         'cyanotic spells during feeding. Overnight oximetry shows recurrent desaturation below 85%. '
                         'Flexible laryngoscopy shows short aryepiglottic folds and severe arytenoid prolapse. What is '
                         'the best management?',
                 'choices': ['Supraglottoplasty with operative airway endoscopy',
                             'Tracheostomy as the first surgical airway procedure',
                             'Nasogastric feeding and recheck the airway in 3 months',
                             'Higher-dose acid suppression for 8 more weeks, then reassess'],
                 'answer': 0,
                 'explanation': 'Severe laryngomalacia is defined by physiologic consequences: failure to thrive, '
                                'cyanotic episodes, hypoxemia, significant retractions or cardiopulmonary strain. This '
                                'infant has all of these despite maximal feeding and reflux measures. '
                                'Supraglottoplasty, dividing short aryepiglottic folds and trimming redundant '
                                'arytenoid mucosa, relieves inspiratory collapse in most infants with isolated '
                                'disease. It is performed with microlaryngoscopy and bronchoscopy because synchronous '
                                'airway lesions are found in a meaningful minority of severe cases and change the '
                                'plan.',
                 'why_wrong': ['Correct.',
                               'Tracheostomy is reserved for infants who fail supraglottoplasty or have severe '
                               'neurologic or multilevel disease, not as first-line surgery.',
                               'Bypassing oral feeding does not treat the airway collapse that is causing his '
                               'hypoxemia, retractions and growth failure.',
                               'He has already failed acid suppression, and reflux therapy alone cannot correct the '
                               'anatomic collapse driving severe disease.'],
                 'board_pearl': 'Laryngomalacia with failure to thrive, cyanosis or hypoxemia: supraglottoplasty with '
                                'airway endoscopy.',
                 'curveball': 'Which synchronous airway lesions or neurologic comorbidities increase the chance of '
                              'persistent symptoms after supraglottoplasty?',
                 'curveball_answer': 'Synchronous subglottic stenosis, tracheomalacia, bronchomalacia or vocal fold '
                                     'paralysis can keep the child obstructed after a technically good '
                                     'supraglottoplasty. Neurologic disease, hypotonia, genetic syndromes, cardiac '
                                     'disease and craniofacial anomalies predict lower success and more need for '
                                     'revision, feeding tubes or tracheostomy. These children need counseling and '
                                     'closer postoperative surveillance.'},
 'v242_ped_lm_fnd': {'stem': 'A 7-week-old boy has inspiratory stridor that is loud enough for his parents to hear '
                             'from the next room and that worsens supine and during feeds. Awake laryngoscopy shows an '
                             'omega-shaped epiglottis with inspiratory supraglottic collapse. His oxygen saturation is '
                             '97% awake. His weight has fallen from the 40th to the 8th percentile over 4 weeks '
                             'despite adequate offered volumes. Which feature most determines that he needs escalation '
                             'of care?',
                     'choices': ['The loudness of the stridor, which is heard across the house',
                                 'The omega-shaped epiglottis seen on awake laryngoscopy',
                                 'The worsening of stridor when supine and during feeds',
                                 'The decline in weight percentile over the past 4 weeks'],
                     'answer': 3,
                     'explanation': 'Laryngomalacia severity is defined by consequences, not by how loud the stridor '
                                    'is or how the larynx looks. The increased work of breathing during feeds raises '
                                    'caloric expenditure and impairs suck-swallow-breathe coordination, which produces '
                                    'poor weight gain. Failure to thrive, apnea or cyanosis, hypoxemia, significant '
                                    'retractions and aspiration mark severe disease that warrants operative airway '
                                    'evaluation and usually supraglottoplasty. Loud stridor, positional worsening and '
                                    'an omega epiglottis are typical of mild disease.',
                     'why_wrong': ['Stridor loudness reflects turbulent airflow and does not correlate with severity; '
                                   'many mild cases are very loud.',
                                   'An omega-shaped epiglottis is a common finding in mild laryngomalacia and in '
                                   'normal infants and does not define severity.',
                                   'Worsening with feeding and supine positioning is the typical pattern of all '
                                   'laryngomalacia, including mild disease.',
                                   'Correct.'],
                     'board_pearl': 'Grade laryngomalacia by growth, apnea, cyanosis and hypoxemia, never by stridor '
                                    'loudness.',
                     'curveball': 'Which synchronous airway lesions should be sought when symptoms are atypical or '
                                  'unusually severe?',
                     'curveball_answer': 'Look for subglottic stenosis, subglottic hemangioma, tracheomalacia or '
                                         'bronchomalacia, vascular compression of the trachea, vocal fold paralysis '
                                         'and laryngeal cleft. Biphasic or expiratory stridor, a weak or abnormal cry, '
                                         'aspiration out of proportion to supraglottic collapse, or poor response to '
                                         'supraglottoplasty should prompt full microlaryngoscopy and bronchoscopy.'},
 'v242_ped_lm_app': {'stem': 'A 10-week-old girl with laryngomalacia confirmed on awake laryngoscopy has been on '
                             'thickened feeds and a proton pump inhibitor for 4 weeks. She still has retractions, a '
                             'pectus excavatum, two witnessed cyanotic spells, and poor weight gain. Her stridor is '
                             'now heard during both inspiration and expiration while she is calm. The family is ready '
                             'for surgery. What is the best next step?',
                     'choices': ['Higher-dose acid suppression with a prokinetic for 6 more weeks',
                                 'Endoscopy of the full airway with supraglottoplasty under one anesthetic',
                                 'Gastrostomy tube placement with continued airway observation',
                                 'Tracheostomy as the definitive airway for severe laryngomalacia'],
                     'answer': 1,
                     'explanation': 'She has severe laryngomalacia that has failed medical therapy, with cyanosis, '
                                    'retractions, chest wall deformity and growth failure. Supraglottoplasty is '
                                    'indicated. The deciding clue for full evaluation is the biphasic stridor, which '
                                    'laryngomalacia alone does not produce and which suggests a second lesion such as '
                                    'subglottic stenosis or tracheomalacia. Microlaryngoscopy and bronchoscopy at the '
                                    'same anesthetic define the collapse pattern, guide a tailored supraglottoplasty '
                                    'and detect synchronous disease that can limit surgical success.',
                     'why_wrong': ['She has already failed acid suppression, and medical therapy cannot correct the '
                                   'anatomic collapse causing her cyanosis and growth failure.',
                                   'Correct.',
                                   'A gastrostomy treats the nutritional consequence but leaves the airway obstruction '
                                   'that causes cyanosis and increased work of breathing.',
                                   'Tracheostomy is reserved for failure of supraglottoplasty or complex multilevel '
                                   'disease, not as first-line surgery for laryngomalacia.'],
                     'board_pearl': 'Biphasic stridor in laryngomalacia suggests a second lesion; evaluate the whole '
                                    'airway at supraglottoplasty.',
                     'curveball': 'Which aryepiglottic, arytenoid and epiglottic components can be selectively '
                                  'addressed at surgery?',
                     'curveball_answer': 'Short aryepiglottic folds are divided to release the tethered epiglottis. '
                                         'Redundant mucosa over the arytenoids and cuneiform cartilages is trimmed, '
                                         'while preserving the interarytenoid mucosa to avoid supraglottic stenosis. A '
                                         'retroflexed or posteriorly collapsing epiglottis can be treated with '
                                         'epiglottopexy. Tailoring to the observed collapse pattern limits aspiration '
                                         'and scarring.'},
 'v242_ped_lm_snr': {'stem': 'A 9-month-old boy with a 22q11 deletion syndrome and hypotonia had supraglottoplasty 3 '
                             'months ago for severe laryngomalacia. He still has noisy breathing, frequent overnight '
                             'desaturations, coughing with thin liquids and slow weight gain. Awake laryngoscopy shows '
                             'a well-healed supraglottis with only mild residual prolapse. His parents ask whether a '
                             'second operation will fix him. What is the best next step?',
                     'choices': ['Revision supraglottoplasty with an epiglottopexy added',
                                 'Tracheostomy now because supraglottoplasty has failed',
                                 'Fundoplication to stop reflux-driven supraglottic edema',
                                 'Repeat airway endoscopy, swallow study and PSG first'],
                     'answer': 3,
                     'explanation': 'Persistent obstruction and aspiration after an appropriate supraglottoplasty in a '
                                    'syndromic, hypotonic infant should prompt mechanism-based reassessment. The '
                                    'healed supraglottis with mild residual prolapse argues against inadequate '
                                    'surgery. Synchronous airway lesions, tracheobronchomalacia, multilevel or '
                                    'pharyngeal collapse, central apnea and neurologic dysphagia are common in '
                                    'syndromic infants. Microlaryngoscopy and bronchoscopy, an instrumental swallow '
                                    'study and PSG define the cause and direct targeted revision, feeding changes, '
                                    'positive airway pressure or tracheostomy.',
                     'why_wrong': ['Revision without new evidence of supraglottic collapse risks supraglottic stenosis '
                                   'and more aspiration while missing other causes.',
                                   'Tracheostomy may become necessary, but deciding before defining the residual '
                                   'mechanism risks an avoidable airway with major morbidity.',
                                   'Reflux surgery does not address hypotonia, multilevel collapse or neurologic '
                                   'dysphagia, the likely drivers in this child.',
                                   'Correct.'],
                     'board_pearl': 'Failed supraglottoplasty in a syndromic infant: reassess airway, swallow and '
                                    'sleep before reoperating.',
                     'curveball': 'When would PSG, repeat microlaryngoscopy and bronchoscopy, an instrumental swallow '
                                  'study, or DISE each add useful information?',
                     'curveball_answer': 'PSG separates obstructive from central events and shows hypoventilation. '
                                         'Microlaryngoscopy and bronchoscopy detect residual supraglottic disease, '
                                         'subglottic stenosis and tracheobronchomalacia. FEES or VFSS shows aspiration '
                                         'and which consistencies are safe. DISE shows multilevel pharyngeal or '
                                         'tongue-base collapse during sleep that awake endoscopy misses.'},
 'v11_ped_05': {'stem': 'A 6-year-old boy has a painless 2-cm mass in the anterior neck that his parents first noticed '
                        'during a cold 3 months ago. It lies in the midline just below the hyoid bone, is smooth and '
                        'cystic, and rises when he swallows and when he protrudes his tongue. There are no skin pits. '
                        'Ultrasound shows a thin-walled cyst embedded near the hyoid and a normal thyroid gland. Which '
                        'diagnosis is most likely?',
                'choices': ['Thyroglossal duct cyst',
                            'Midline dermoid cyst',
                            'Delphian lymph node',
                            'Plunging ranula cyst'],
                'answer': 0,
                'explanation': 'The thyroid descends from the foramen cecum through or anterior to the developing '
                               'hyoid to the lower neck, and a persistent tract can form a cyst anywhere along that '
                               'path, most often near the hyoid. Because the tract is attached to the hyoid and tongue '
                               'base, the cyst rises with swallowing and tongue protrusion, the classic deciding clue. '
                               'Enlargement with upper respiratory infection is common. Treatment is the Sistrunk '
                               'procedure, removing the cyst, central hyoid and tract to the tongue base.',
                'why_wrong': ['Correct.',
                              'Dermoid cysts are midline but attach to skin rather than the hyoid, so they do not rise '
                              'with tongue protrusion.',
                              'A Delphian node sits on the cricothyroid membrane, is solid on ultrasound and does not '
                              'move with tongue protrusion.',
                              'A plunging ranula extends from the sublingual gland through the mylohyoid into the '
                              'submandibular space and is usually lateral.'],
                'board_pearl': 'Midline cyst that rises with tongue protrusion: thyroglossal duct cyst; treat with '
                               'Sistrunk.',
                'curveball': 'Ultrasound shows no normal thyroid tissue in the neck. What must you establish before '
                             'excising the presumed thyroglossal duct cyst?',
                'curveball_answer': "Establish whether the mass is ectopic thyroid and the patient's only functioning "
                                    'thyroid tissue. Check TSH and free T4, and obtain a thyroid scintigraphy scan to '
                                    'map functioning tissue. If the lesion is the only thyroid, excision causes '
                                    'lifelong hypothyroidism, so the decision to observe, excise with replacement or '
                                    'relocate involves endocrinology and the family.'},
 'v124_ped_03': {'stem': 'A 5-year-old girl has a 2-cm midline cystic mass at the level of the hyoid that rises with '
                         'tongue protrusion and has been infected once, resolving with oral antibiotics 2 months ago. '
                         'She is clinically euthyroid. A Sistrunk procedure is being scheduled. Her preoperative '
                         'workup so far consists only of the physical exam. Which preoperative step is most important?',
                 'choices': ['Fine-needle aspiration of the cyst to exclude papillary carcinoma',
                             'Neck ultrasound to document a normal thyroid gland in the low neck',
                             'Contrast CT of the neck to map the tract to the foramen cecum',
                             'Technetium thyroid scan, which is required before every Sistrunk'],
                 'answer': 1,
                 'explanation': 'In a small but important minority of patients, an apparent thyroglossal duct cyst is '
                                "ectopic thyroid that may be the patient's only functioning thyroid tissue. Excising "
                                'it would cause permanent hypothyroidism. Ultrasound documenting a normal orthotopic '
                                'gland is the standard, radiation-free preoperative step, and it also confirms the '
                                'cystic nature of the lesion and its hyoid relationship. If no normal thyroid is seen, '
                                'thyroid function tests and scintigraphy follow before deciding whether to operate.',
                 'why_wrong': ['Carcinoma in a thyroglossal duct cyst is rare in children, and FNA is reserved for '
                               'solid or suspicious components on imaging.',
                               'Correct.',
                               'CT adds radiation and is not needed to plan a Sistrunk, because the operation removes '
                               'the central hyoid and tract regardless of imaging.',
                               'Scintigraphy is used selectively when ultrasound fails to show a normal thyroid, not '
                               'routinely before every Sistrunk.'],
                 'board_pearl': 'Before Sistrunk, confirm a normal thyroid by ultrasound; the cyst may be the only '
                                'thyroid tissue.',
                 'curveball': 'Ultrasound shows no orthotopic thyroid, and scintigraphy shows that the mass contains '
                              'the only functioning thyroid tissue. How does this change the surgical plan?',
                 'curveball_answer': 'Excision is no longer routine. If the mass is asymptomatic, observation with '
                                     'thyroid function monitoring is reasonable. If excision is needed for infection, '
                                     'obstruction or suspicion of malignancy, the family must accept lifelong '
                                     'levothyroxine, and some surgeons consider autotransplantation. Endocrinology '
                                     'should be involved, because many children with ectopic thyroid are hypothyroid '
                                     'and need replacement anyway.'},
 'v245_ped_neck_fnd': {'stem': 'A 7-year-old girl has 2 days of a tender, red, warm midline swelling just below the '
                               'hyoid that appeared during a viral illness. Her mother says a painless lump in the '
                               'same spot had been coming and going for a year and seemed to move when she swallowed. '
                               'She is afebrile with a normal airway. Ultrasound shows a thick-walled cyst with '
                               'internal debris adjacent to the hyoid. Which diagnosis should be presumed?',
                       'choices': ['Suppurative midline lymph node abscess',
                                   'Infected midline dermoid cyst',
                                   'Acute suppurative thyroiditis',
                                   'Infected thyroglossal duct cyst'],
                       'answer': 3,
                       'explanation': 'A previously painless midline lump that moved with swallowing and is now '
                                      'inflamed during an upper respiratory infection is an infected thyroglossal duct '
                                      'cyst until proven otherwise. The tract communicates with the foramen cecum, so '
                                      'oral flora can seed the cyst. Initial management is antibiotics, with needle '
                                      'aspiration if needed, avoiding incision and drainage when possible because it '
                                      'scars the field and increases recurrence. A Sistrunk procedure is performed '
                                      'after inflammation resolves.',
                       'why_wrong': ['Lymph nodes are rarely truly midline at the hyoid, and a node does not explain a '
                                     'year of a lump that moved with swallowing.',
                                     'Dermoid cysts attach to skin rather than the hyoid, rarely move with swallowing '
                                     'and rarely become infected after viral illnesses.',
                                     'Suppurative thyroiditis involves the thyroid lobe, usually on the left from a '
                                     'piriform sinus tract, not a cyst at the hyoid.',
                                     'Correct.'],
                       'board_pearl': 'Treat infected thyroglossal duct cysts with antibiotics or aspiration, then '
                                      'Sistrunk; avoid incision and drainage.',
                       'curveball': 'The infection resolves. Why does the Sistrunk procedure include removing the '
                                    'central hyoid rather than simple cyst excision?',
                       'curveball_answer': 'The thyroglossal tract passes through or closely around the central hyoid '
                                           'on its way to the foramen cecum. Simple cyst excision leaves this tract '
                                           'and carries a recurrence risk of roughly half, while removing the central '
                                           'hyoid and a core of tongue-base tissue toward the foramen cecum lowers '
                                           'recurrence to a small percentage. Prior infection raises recurrence risk.'},
 'v245_ped_neck_app': {'stem': 'An 8-year-old boy has a 3-day history of fever and a tender, enlarging left lateral '
                               'neck mass anterior to the upper sternocleidomastoid after a sore throat. His mother '
                               'says a soft painless lump has been there for a year. He is breathing comfortably and '
                               'swallowing liquids. Contrast CT shows a 3-cm rim-enhancing cystic lesion at the '
                               'carotid bifurcation displacing the jugular vein posteriorly. What is the best '
                               'management sequence?',
                       'choices': ['Immediate complete excision of the cyst and tract during infection',
                                   'Incision and drainage with observation and no later excision',
                                   'Antibiotics with aspiration if needed, then excision after recovery',
                                   'Percutaneous sclerotherapy of the cyst with doxycycline now'],
                       'answer': 2,
                       'explanation': 'A long-standing lateral neck cyst at the anterior border of the '
                                      'sternocleidomastoid that became infected after pharyngitis is an infected '
                                      'second branchial cleft cyst. Excision during active infection is difficult and '
                                      'increases the risk of incomplete removal, recurrence and injury to the '
                                      'hypoglossal, vagus and spinal accessory nerves. Treat with antibiotics, '
                                      'aspirating if a drainable collection needs source control, then perform '
                                      'complete excision of the cyst and any tract after inflammation has resolved, '
                                      'typically several weeks later.',
                       'why_wrong': ['Operating through inflamed tissue blurs planes around the carotid and cranial '
                                     'nerves and raises recurrence and nerve-injury risk.',
                                     'Drainage alone leaves the epithelial lining, so the cyst recurs and reinfects; '
                                     'interval excision is still required.',
                                     'Correct.',
                                     'Sclerotherapy is used for lymphatic malformations, not epithelial-lined '
                                     'branchial cysts, which recur unless excised.'],
                       'board_pearl': 'Infected branchial cyst: cool it down with antibiotics or aspiration, then '
                                      'excise electively.',
                       'curveball': 'How would a recurrent left low-neck infection with a piriform sinus opening '
                                    'change the embryologic diagnosis and operative plan?',
                       'curveball_answer': 'That points to a third or fourth pouch sinus arising from the piriform '
                                           'sinus, not a second cleft cyst. Direct laryngoscopy confirms the internal '
                                           'opening, which is treated by endoscopic cauterization or '
                                           'chemocauterization, with open excision and often hemithyroidectomy for '
                                           'failures. The recurrent laryngeal and superior laryngeal nerves are at '
                                           'risk during open surgery.'},
 'v245_ped_neck_snr': {'stem': 'A 3-year-old girl has a soft, compressible, nontender left neck mass that has been '
                               'present since infancy and swells during viral illnesses, then partly regresses. MRI '
                               'shows a multiloculated, transspatial lesion with large T2-bright cysts and fluid-fluid '
                               'levels that insinuates around the carotid sheath and extends into the submandibular '
                               'space. There is no airway compromise. What is the best initial treatment?',
                       'choices': ['Image-guided sclerotherapy of the macrocystic components',
                                   'Complete excision including any encased nerve branches',
                                   'Incision and drainage with a prolonged antibiotic course',
                                   'Oral propranolol until the lesion stops enlarging'],
                       'answer': 0,
                       'explanation': 'A compressible, transspatial lesion with large cysts and fluid-fluid levels '
                                      'that swells with infection is a macrocystic lymphatic malformation. Lymphatic '
                                      'malformations surround rather than displace structures, so complete excision '
                                      'often risks cranial nerve injury. Macrocystic disease responds well to '
                                      'sclerotherapy with agents such as doxycycline, bleomycin or OK-432, which '
                                      'ablate the endothelial lining. Surgery is chosen for accessible residual or '
                                      'symptomatic disease, and sirolimus is used for extensive microcystic or complex '
                                      'disease.',
                       'why_wrong': ['Correct.',
                                     'Radical excision of a transspatial lesion that encases neurovascular structures '
                                     'carries high cranial nerve morbidity when sclerotherapy works well.',
                                     'Swelling during viral illness reflects lymphatic engorgement or intralesional '
                                     'bleeding, not abscess, and drainage causes persistent leakage and infection.',
                                     'Propranolol treats infantile hemangioma, a proliferating vascular tumor, not a '
                                     'slow-flow lymphatic malformation.'],
                       'board_pearl': 'Macrocystic lymphatic malformation: sclerotherapy first; microcystic disease '
                                      'may need sirolimus or surgery.',
                       'curveball': 'What airway strategy would you need if rapid intralesional hemorrhage or '
                                    'infection suddenly caused tongue-base or pharyngeal compression?',
                       'curveball_answer': 'Treat it as an anticipated difficult airway. Keep the child upright and '
                                           'calm, and secure the airway in the operating room with anesthesia and '
                                           'otolaryngology present, using inhalational induction with spontaneous '
                                           'ventilation, video or fiberoptic intubation, and rigid scopes and a '
                                           'surgeon ready for tracheostomy. Once the airway is secure, aspiration, '
                                           'antibiotics, steroids or sclerotherapy can decompress the lesion.'},
 'v11_ped_06': {'stem': 'A 14-month-old boy born at 27 weeks was intubated for 6 weeks in the NICU and needed two '
                        'reintubations. Since discharge he has had biphasic stridor with exertion and three croup-like '
                        'illnesses requiring emergency visits. Microlaryngoscopy shows a firm, circumferential '
                        'subglottic narrowing with mature-appearing scar, a normal-shaped cricoid framework and mobile '
                        'vocal folds. Which mechanism best explains his stenosis?',
                'choices': ['Elliptical cricoid cartilage present from birth',
                            'Failed recanalization of the embryonic laryngeal lumen',
                            'Recurrent viral laryngotracheitis causing fibrosis',
                            'Endotracheal tube pressure injury to subglottic mucosa'],
                'answer': 3,
                'explanation': 'Prolonged and repeated intubation is the classic cause of acquired pediatric '
                               'subglottic stenosis, and most pediatric cases today are acquired. The cricoid is a '
                               'complete ring, so tube pressure on the mucosa causes ischemia, ulceration, '
                               'perichondritis and healing by fibrosis. His history of 6 weeks of intubation with '
                               'reintubations and the endoscopic appearance of soft-tissue scar in a normal '
                               'cartilaginous framework point to an acquired mechanism. Congenital stenosis, by '
                               'contrast, typically shows a small or elliptical cricoid without a scar history.',
                'why_wrong': ['An elliptical or small cricoid is a congenital cartilaginous stenosis, whereas his '
                              'endoscopy shows scar within a normal-shaped framework.',
                              'Failed recanalization produces congenital webs or atresia, and his history of prolonged '
                              'intubation explains the acquired scar better.',
                              'Viral croup causes transient subglottic edema; recurrent croup-like illnesses here are '
                              'a symptom of the fixed narrowing, not its cause.',
                              'Correct.'],
                'board_pearl': 'Most pediatric subglottic stenosis is acquired after intubation; congenital disease '
                               'reflects a small or elliptical cricoid.',
                'curveball': 'The stenosis is high-grade, and the child becomes tracheostomy-dependent. What factors '
                             'determine endoscopic treatment versus laryngotracheal reconstruction?',
                'curveball_answer': 'Endoscopic incision and balloon dilation suit thin, short, soft, low-grade '
                                    'stenoses with an intact cartilage framework. Open reconstruction is favored for '
                                    'thick, long, mature or circumferential scar, grade III or IV disease, loss of '
                                    'cartilage support or repeated endoscopic failure. Glottic involvement, pulmonary '
                                    'reserve, reflux, eosinophilic esophagitis and aspiration also shape the choice '
                                    'and timing.'},
 'v140_ped_04': {'stem': 'A 3-year-old girl born at 25 weeks has had a tracheostomy since 5 months of age for acquired '
                         'subglottic stenosis, recorded as Myer-Cotton grade III on an endoscopy report from an '
                         'outside hospital 2 years ago. She now uses room air, has no oxygen need, and eats by mouth. '
                         'Her family wants decannulation. Which preoperative evaluation is most essential before '
                         'choosing a reconstruction?',
                 'choices': ['Microlaryngoscopy and bronchoscopy defining glottis, scar length and distal airway',
                             'Neck CT with three-dimensional airway reconstruction to measure the stenosis',
                             'Myer-Cotton grade from the outside endoscopy report to select the graft type',
                             'Dual-probe pH-impedance study alone to decide whether surgery is safe now'],
                 'answer': 0,
                 'explanation': 'Reconstruction succeeds only when the whole airway is understood. Current '
                                'microlaryngoscopy and bronchoscopy with sizing defines the grade, the length and '
                                'maturity of the scar, its distance from the vocal folds, vocal fold mobility and '
                                'posterior glottic involvement, and distal tracheal problems such as suprastomal '
                                'collapse or tracheomalacia. Assessment of swallowing, reflux and eosinophilic '
                                'esophagitis, pulmonary reserve and neurologic status completes candidacy, because '
                                'each affects graft choice, staging and decannulation success.',
                 'why_wrong': ['Correct.',
                               'CT can estimate lumen size but cannot assess vocal fold motion, scar maturity or '
                               'dynamic collapse, so it complements rather than replaces endoscopy.',
                               'A 2-year-old outside grade does not reflect the current airway and omits length, '
                               'glottic involvement and distal disease that determine the operation.',
                               'Reflux evaluation is part of candidacy but cannot define the stenosis anatomy needed '
                               'to choose between expansion and resection.'],
                 'board_pearl': 'Before airway reconstruction, endoscopically define grade, length, glottis, vocal '
                                'fold mobility and distal airway.',
                 'curveball': 'Endoscopy shows interarytenoid scar with limited arytenoid abduction in addition to the '
                              'subglottic scar. How does posterior glottic stenosis alter the LTR plan?',
                 'curveball_answer': 'Posterior glottic scar fixes the arytenoids, so an anterior graft alone will not '
                                     'provide an adequate airway. The plan needs a posterior cricoid split with a '
                                     'posterior costal cartilage graft to widen the posterior glottis and subglottis, '
                                     'often with an anterior graft, and usually a staged approach with stenting. Voice '
                                     'and aspiration risk should be discussed.'},
 'v242_ped_sgs_fnd': {'stem': 'A 7-week-old boy born at 28 weeks has failed extubation three times because of stridor '
                              'and increased work of breathing within hours of each attempt. He was intubated for 5 '
                              'weeks with several tube changes. His lungs are otherwise healthy on minimal ventilator '
                              'settings. The neonatology team asks how best to diagnose and grade a suspected '
                              'subglottic stenosis. Which evaluation is most appropriate?',
                      'choices': ['Awake flexible laryngoscopy at the bedside in the NICU',
                                  'Microlaryngoscopy and bronchoscopy with endotracheal tube sizing',
                                  'Contrast-enhanced neck CT with virtual airway endoscopy',
                                  'Airway fluoroscopy to show dynamic subglottic narrowing'],
                      'answer': 1,
                      'explanation': 'Microlaryngoscopy and bronchoscopy under anesthesia is the definitive evaluation '
                                     'for suspected subglottic stenosis. Sizing with the largest endotracheal tube '
                                     'that allows an air leak at an acceptable pressure, compared with the '
                                     'age-appropriate size, assigns the Myer-Cotton grade (I up to 50%, II 51-70%, III '
                                     '71-99%, IV no lumen). Endoscopy also defines scar length and maturity, distance '
                                     'from the vocal folds, glottic and posterior glottic status and distal tracheal '
                                     'disease. These features, plus pulmonary status, determine whether an anterior '
                                     'cricoid split or other procedure is appropriate.',
                      'why_wrong': ['Flexible laryngoscopy assesses the supraglottis and vocal fold motion but cannot '
                                    'reliably see or size the subglottis in an infant.',
                                    'Correct.',
                                    'CT exposes an infant to radiation and cannot assess scar maturity, posterior '
                                    'glottic involvement or dynamic lesions with endoscopic accuracy.',
                                    'Fluoroscopy can show dynamic tracheal collapse but cannot grade a fixed '
                                    'subglottic stenosis or define its length and character.'],
                      'board_pearl': 'Grade subglottic stenosis endoscopically by endotracheal tube sizing using the '
                                     'Myer-Cotton scale.',
                      'curveball': 'Why can two children with the same percentage obstruction require different '
                                   'operations?',
                      'curveball_answer': 'Myer-Cotton grade measures only lumen reduction. Stenosis length, scar '
                                          'maturity and thickness, cartilage framework integrity, distance from the '
                                          'vocal folds, glottic or posterior glottic involvement, and comorbidities '
                                          'such as pulmonary disease, aspiration and reflux all change the choice. A '
                                          'thin web may respond to endoscopic incision, while a long mature scar of '
                                          'the same grade may need LTR or CTR.'},
 'v242_ped_sgs_app': {'stem': 'A 2-year-old girl who was intubated for 9 days after cardiac surgery has had exertional '
                              'biphasic stridor for 3 months. She has no tracheostomy. Microlaryngoscopy shows a thin, '
                              '3-mm, crescentic, immature-appearing subglottic scar narrowing the lumen by about 60%, '
                              'a normal cricoid framework, mobile vocal folds and a normal trachea. Which management '
                              'is most appropriate?',
                      'choices': ['Single-stage laryngotracheal reconstruction with an anterior costal graft',
                                  'Anterior cricoid split with postoperative intubation for 7 to 10 days',
                                  'Endoscopic radial incision of the scar with balloon dilation',
                                  'Cricotracheal resection with primary thyrotracheal anastomosis'],
                      'answer': 2,
                      'explanation': 'Endoscopic therapy works best for thin, short, soft or immature scar with an '
                                     'intact cartilaginous framework and lower grades. Her grade II, 3-mm crescentic '
                                     'scar with normal cricoid, glottis and trachea is ideal for radial incision with '
                                     'a cold knife or laser followed by balloon dilation, with interval endoscopy to '
                                     'assess durability. Adjuncts such as topical mitomycin or steroid injection are '
                                     'used selectively. Open reconstruction is reserved for thick, long, mature or '
                                     'circumferential disease and for repeated endoscopic failure.',
                      'why_wrong': ['Open reconstruction is unnecessary as first-line treatment for a thin, short '
                                    'grade II scar that responds well to endoscopic therapy.',
                                    'Anterior cricoid split is a neonatal procedure for infants who fail extubation, '
                                    'not for a 2-year-old with a thin acquired scar.',
                                    'Correct.',
                                    'Resection is reserved for severe grade III or IV mature stenosis and would be '
                                    'excessive for a thin grade II scar.'],
                      'board_pearl': 'Thin, short, immature, low-grade subglottic scar: endoscopic incision and '
                                     'balloon dilation first.',
                      'curveball': 'What pattern of recurrence would make you stop repeating endoscopic procedures and '
                                   'discuss LTR or CTR?',
                      'curveball_answer': 'Rapid restenosis after each dilation, needing procedures every few months, '
                                          'progression to a thicker, longer or circumferential scar, loss of cartilage '
                                          'support, or failure to maintain an adequate lumen after several '
                                          'well-performed sessions should shift care to open reconstruction. '
                                          'Uncontrolled reflux or eosinophilic esophagitis should also be evaluated, '
                                          'because they drive restenosis.'},
 'v242_ped_sgs_snr': {'stem': 'A 4-year-old boy has been tracheostomy-dependent since infancy for acquired subglottic '
                              'stenosis. Endoscopy shows a mature, thick, circumferential Myer-Cotton grade IV '
                              'stenosis that begins well below normally mobile vocal folds, with a normal posterior '
                              'glottis and trachea. He has no oxygen requirement, swallows safely, and his reflux and '
                              'eosinophilic esophagitis evaluation is negative. Which operation is most appropriate?',
                      'choices': ['Serial balloon dilation with topical mitomycin application',
                                  'Cricotracheal resection, given the isolated subglottic segment',
                                  'Single-stage laryngotracheoplasty with an anterior graft only',
                                  'Anterior cricoid split with short-term intubation as a stent'],
                      'answer': 1,
                      'explanation': 'LTR expands a stenotic framework with cartilage grafts, while CTR removes the '
                                     'stenotic subglottic segment and anastomoses healthy trachea to the thyroid '
                                     'cartilage. For severe grade III and IV mature stenosis with a margin of normal '
                                     'airway below the vocal folds and no glottic involvement, CTR is generally '
                                     'preferred because decannulation rates are higher than with LTR. His good '
                                     'pulmonary reserve, safe swallow and quiescent reflux and eosinophilic disease '
                                     'make him a favorable candidate. Staging depends on airway security and '
                                     'comorbidity.',
                      'why_wrong': ['Endoscopic dilation rarely succeeds in mature, thick, circumferential grade IV '
                                    'stenosis, which has no lumen to dilate durably.',
                                    'Correct.',
                                    'An anterior graft alone cannot expand a complete grade IV circumferential '
                                    'stenosis, which needs resection or anterior and posterior grafting.',
                                    'Anterior cricoid split is a neonatal procedure for extubation failure and is not '
                                    'effective for mature grade IV stenosis.'],
                      'board_pearl': 'Severe grade III-IV stenosis clear of the vocal folds: cricotracheal resection '
                                     'usually beats LTR for decannulation.',
                      'curveball': 'How do aspiration, pulmonary reserve, active infection, tracheomalacia or vocal '
                                   'fold dysfunction affect reconstruction timing and decannulation probability?',
                      'curveball_answer': 'Each lowers the chance of success and favors delay or a double-stage '
                                          'procedure with the tracheostomy kept. Aspiration and poor pulmonary reserve '
                                          'mean the child cannot tolerate airway edema or a narrow repaired lumen. '
                                          'Active infection impairs graft healing. Tracheomalacia and vocal fold '
                                          'immobility can keep the child obstructed despite a good subglottic result, '
                                          'so they must be addressed or accepted first.'},
 'v113-ped-01': {'stem': 'A 4-year-old boy who recently immigrated and has never been vaccinated develops a '
                         'temperature of 40.1 C and severe sore throat over 6 hours. He sits leaning forward with his '
                         'neck extended, drools, speaks in a muffled voice and has soft inspiratory stridor but almost '
                         'no cough. He appears toxic and anxious. Which diagnosis is most likely?',
                 'choices': ['Acute bacterial epiglottitis',
                             'Viral laryngotracheobronchitis',
                             'Bacterial tracheitis',
                             'Retropharyngeal abscess'],
                 'answer': 0,
                 'explanation': 'Rapid onset of high fever, toxicity, drooling, muffled voice and tripod or sniffing '
                                'posture without a barky cough is the classic picture of epiglottitis. Supraglottic '
                                'swelling obstructs the airway above the glottis, so the voice is muffled rather than '
                                'hoarse and swallowing is too painful to manage secretions. Lack of Hib vaccination is '
                                'the deciding risk clue, since Haemophilus influenzae type b remains the main cause in '
                                'unimmunized children, while streptococci and S. aureus predominate in vaccinated '
                                'children.',
                 'why_wrong': ['Correct.',
                               'Croup causes a barky cough and hoarseness after a viral prodrome, usually without '
                               'drooling, toxicity or a 6-hour onset of high fever.',
                               'Bacterial tracheitis usually follows a croup-like illness and produces a brassy cough '
                               'with thick secretions, not drooling and muffled voice.',
                               'Retropharyngeal abscess typically develops over days with neck stiffness and '
                               'torticollis rather than abrupt toxicity within hours.'],
                 'board_pearl': 'High fever, drooling, muffled voice, tripod posture and no barky cough: epiglottitis.',
                 'curveball': 'How would you coordinate airway examination and control without provoking complete '
                              'obstruction?',
                 'curveball_answer': "Leave him upright on a parent's lap, avoid tongue depressors, IV starts and "
                                     'supine positioning, and give blow-by oxygen. Call anesthesia and otolaryngology, '
                                     'move him with an airway-capable physician to the operating room, and use '
                                     'inhalational induction with spontaneous ventilation. Have rigid bronchoscopes '
                                     'and a tracheostomy tray ready, intubate with a smaller tube, then obtain '
                                     'cultures and start IV antibiotics.'},
 'v116-ped-01': {'stem': 'An unimmunized 3-year-old girl has a temperature of 39.8 C, inspiratory stridor, drooling '
                         'and a muffled voice that developed over the afternoon. She is sitting upright on her '
                         "mother's lap with her chin forward and refuses to lie down. Her saturation is 94% on blow-by "
                         'oxygen. The emergency physician asks what to do first. What is the safest immediate '
                         'approach?',
                 'choices': ['Tongue-depressor exam to confirm swelling before calling consultants',
                             'Lateral neck radiograph in radiology with a nurse escort first',
                             "Keep her calm on the parent's lap and assemble anesthesia and ENT",
                             'Rapid-sequence intubation in the ED by the first available provider'],
                 'answer': 2,
                 'explanation': 'This is a threatened supraglottic airway. Crying and agitation increase negative '
                                'inspiratory pressure and can collapse the swollen epiglottis onto the glottis, while '
                                'supine positioning lets it fall back. The priority is to keep her calm and upright '
                                'with her parent, avoid painful or frightening procedures, and assemble the most '
                                'experienced team to secure the airway in the operating room by inhalational induction '
                                'with surgical airway backup. Diagnosis can be confirmed under anesthesia, and IV '
                                'antibiotics follow airway control.',
                 'why_wrong': ['Pharyngeal manipulation in a child with suspected epiglottitis can provoke '
                               'laryngospasm or complete obstruction before anyone can secure the airway.',
                               'Sending a child with a threatened airway away from airway expertise risks sudden '
                               'obstruction in radiology, and imaging does not change management.',
                               'Correct.',
                               'Paralysis without a skilled team and surgical backup can turn partial obstruction into '
                               'a cannot-intubate, cannot-oxygenate situation.'],
                 'board_pearl': 'Suspected epiglottitis: keep calm and upright, call the team, and secure the airway '
                                'in the OR.',
                 'curveball': 'Which clinical features help distinguish epiglottitis from croup, bacterial tracheitis '
                              'and retropharyngeal abscess?',
                 'curveball_answer': 'Epiglottitis: abrupt high fever, toxicity, drooling, muffled voice, tripod '
                                     'posture and little cough. Croup: viral prodrome, barky cough, hoarseness, and a '
                                     'nontoxic child. Bacterial tracheitis: croup-like start, then high fever, '
                                     'toxicity and thick secretions with poor response to epinephrine. Retropharyngeal '
                                     'abscess: younger child with neck stiffness, torticollis, dysphagia and posterior '
                                     'pharyngeal bulge over days.'},
 'v140_ped_01': {'stem': 'A fully vaccinated 7-year-old boy has a temperature of 39.5 C, severe odynophagia, drooling, '
                         'a muffled voice and soft inspiratory stridor. He becomes more distressed and his stridor '
                         'worsens when a nurse approaches to place an IV. The emergency physician wants IV access and '
                         'blood cultures before transport so antibiotics are not delayed. What should happen next?',
                 'choices': ['Place an IV and draw blood cultures before moving him',
                             'Defer IV access and move to the OR with ENT and anesthesia',
                             'Give IM dexamethasone and nebulized epinephrine, then reassess',
                             'Obtain a portable CT of the neck with the child lying supine'],
                 'answer': 1,
                 'explanation': 'Vaccination lowers but does not eliminate epiglottitis risk, because streptococci, S. '
                                'aureus and nontypeable Haemophilus also cause supraglottitis. His stridor worsening '
                                'with agitation shows how little reserve he has. Painful procedures such as IV '
                                'placement and blood draws should wait until the airway is secured in the operating '
                                'room, where IV access, cultures and antibiotics follow induction. A short delay in '
                                'antibiotics is far less dangerous than precipitating complete obstruction in the ED.',
                 'why_wrong': ['Venipuncture provokes crying and inspiratory effort that can collapse the swollen '
                               'supraglottis; access and cultures can wait until after induction.',
                               'Correct.',
                               'Steroids and epinephrine treat croup and do not address supraglottic bacterial '
                               'infection or protect a threatened airway.',
                               'Lying supine for CT can precipitate obstruction, and leaving the airway team for '
                               'imaging adds risk without changing management.'],
                 'board_pearl': 'In suspected epiglottitis, IV starts and blood draws wait until the airway is '
                                'secured.',
                 'curveball': 'Which equipment and personnel should be in the operating room for this boy before '
                              'induction begins?',
                 'curveball_answer': 'An experienced pediatric anesthesiologist and otolaryngologist should be '
                                     'present, with endotracheal tubes one-half to one size smaller than usual, '
                                     'stylets, video laryngoscope, rigid ventilating bronchoscopes of several sizes, '
                                     'and an open tracheostomy and cricothyrotomy tray. Suction, IV access equipment '
                                     'and culture swabs should be ready, and the surgeon should be scrubbed for an '
                                     'emergency surgical airway.'},
 'v146_ped_05': {'stem': 'A 5-year-old girl with suspected epiglottitis is brought to the operating room sitting on '
                         "her father's lap. She is drooling, has a muffled voice and inspiratory stridor, and her "
                         'saturation is 93% on blow-by oxygen. The otolaryngologist is scrubbed with rigid '
                         'bronchoscopes and a tracheostomy tray open. The anesthesia resident proposes the induction '
                         'technique. Which approach is most appropriate?',
                 'choices': ['Rapid-sequence induction with a neuromuscular blocker',
                             'Awake flexible nasotracheal intubation after topical lidocaine',
                             'Propofol bolus with a laryngeal mask airway placed for rescue',
                             'Inhalational induction with spontaneous ventilation preserved'],
                 'answer': 3,
                 'explanation': 'In a child with a threatened supraglottic airway, inhalational induction with '
                                'sevoflurane while she sits upright preserves spontaneous ventilation and muscle tone '
                                'that keep the airway open. IV access is placed once she is anesthetized, and '
                                'laryngoscopy is performed in a deep plane, intubating with a smaller tube. If '
                                'intubation fails, the rigid bronchoscope or a surgical airway is immediately '
                                "available. Paralysis removes the child's own airway protection before the team knows "
                                'ventilation is possible.',
                 'why_wrong': ['Paralysis abolishes spontaneous breathing and airway tone; if mask ventilation fails '
                               'over the swollen epiglottis, the child cannot be oxygenated.',
                               'Awake flexible intubation requires a cooperative patient and can provoke laryngospasm '
                               'in a frightened young child with supraglottic edema.',
                               'A propofol bolus can cause apnea and loss of tone, and a laryngeal mask sits on the '
                               'inflamed supraglottis and is unreliable here.',
                               'Correct.'],
                 'board_pearl': 'Epiglottitis in the OR: inhalational induction, spontaneous ventilation, surgeon '
                                'scrubbed for bronchoscopy or tracheostomy.',
                 'curveball': 'How does classic viral croup differ in exam and first-line therapy?',
                 'curveball_answer': 'Croup produces a barky cough, hoarse voice and inspiratory stridor in a nontoxic '
                                     'child who handles secretions, after a viral prodrome, usually parainfluenza. '
                                     'Examination is safe and imaging is rarely needed. First-line therapy is a single '
                                     'dose of oral dexamethasone for all severities, with nebulized epinephrine added '
                                     'for stridor at rest and observation for rebound.'},
 'v154_ped_fnd': {'stem': 'An 18-month-old girl had 2 days of rhinorrhea and low-grade fever, then woke at night with '
                          'a barking cough, a hoarse cry and inspiratory stridor that is heard only when she is upset. '
                          'She is drinking, not drooling, and appears nontoxic. Her temperature is 38.3 C. A parent '
                          'asks which part of the airway is affected. Which site of inflammation best explains her '
                          'findings?',
                  'choices': ['Supraglottic larynx including the epiglottis',
                              'Glottic larynx at the true vocal folds alone',
                              'Subglottic larynx within the cricoid ring',
                              'Retropharyngeal space behind the pharynx'],
                  'answer': 2,
                  'explanation': 'Viral croup, most often parainfluenza, inflames the larynx and trachea, and the '
                                 'clinically important narrowing occurs in the subglottis. The cricoid is a complete '
                                 'ring, so mucosal edema can only narrow the lumen, and in a toddler a small amount of '
                                 'swelling greatly increases resistance. That produces inspiratory stridor and a '
                                 'barking cough, with hoarseness from vocal fold involvement. A frontal neck film, if '
                                 'obtained, shows the steeple sign of subglottic narrowing.',
                  'why_wrong': ['Supraglottic swelling causes epiglottitis, with drooling, muffled voice and toxicity '
                                'rather than a barking cough in a nontoxic child.',
                                'Vocal fold inflammation explains hoarseness, but the stridor and barky cough arise '
                                'from narrowing within the rigid cricoid ring below the folds.',
                                'Correct.',
                                'Retropharyngeal infection causes neck stiffness, torticollis and dysphagia, not a '
                                'barking cough with hoarseness after a viral prodrome.'],
                  'board_pearl': 'Croup narrows the subglottis inside the complete cricoid ring: steeple sign, barky '
                                 'cough, stridor.',
                  'curveball': 'What treatment is given to essentially all children with clinically significant croup?',
                  'curveball_answer': 'A single dose of dexamethasone, usually given orally at 0.15 to 0.6 mg/kg, is '
                                      'recommended for croup of every severity, including mild cases. It reduces '
                                      'return visits, admissions and the duration of symptoms. Nebulized epinephrine '
                                      'is added for stridor at rest or moderate to severe distress, while humidified '
                                      'air has no proven benefit.'},
 'v154_ped_app': {'stem': 'A 2-year-old boy with 1 day of rhinorrhea develops a barky cough with inspiratory stridor '
                          'that is audible at rest. He has suprasternal and intercostal retractions, but he is alert, '
                          'interactive and swallowing his saliva, with a saturation of 95% on room air and a '
                          'temperature of 38.0 C. There is no drooling. What is the most appropriate treatment?',
                  'choices': ['Oral dexamethasone and nebulized epinephrine, then observe',
                              'Oral dexamethasone and discharge home if he looks comfortable',
                              'Nebulized epinephrine and discharge once the stridor resolves',
                              'Heliox with IV ceftriaxone for possible bacterial superinfection'],
                  'answer': 0,
                  'explanation': 'Stridor at rest with retractions is moderate croup. Dexamethasone reduces subglottic '
                                 'inflammation but takes a few hours to work, so nebulized epinephrine is added for '
                                 'rapid mucosal vasoconstriction and relief. Epinephrine wears off within about 2 '
                                 'hours, so the child must be observed in the department, commonly for 2 to 4 hours, '
                                 'to make sure stridor at rest does not return before discharge. Repeated epinephrine '
                                 'needs or hypoxemia warrant admission.',
                  'why_wrong': ['Correct.',
                                'Dexamethasone alone is appropriate for mild croup, but stridor at rest with '
                                'retractions needs epinephrine and observation before discharge.',
                                'Discharge right after epinephrine risks return of stridor when its effect fades, '
                                'before steroids have taken effect.',
                                'Croup is viral and antibiotics do not help; heliox is a temporizing option only for '
                                'severe croup that is not improving.'],
                  'board_pearl': 'Croup with stridor at rest: dexamethasone plus nebulized epinephrine, then observe '
                                 'for rebound.',
                  'curveball': 'How long should you observe after nebulized epinephrine before assuming the rebound '
                               'window has passed?',
                  'curveball_answer': 'Observe for at least 2 hours, and commonly 3 to 4 hours, after the last '
                                      'epinephrine dose, because its effect lasts only about 1 to 2 hours. A child who '
                                      'has no stridor at rest, normal saturation and good oral intake after that '
                                      'period, has received dexamethasone and has reliable follow-up can be '
                                      'discharged. Two or more doses usually mean admission.'},
 'v154_ped_snr': {'stem': 'A 3-year-old boy is in the emergency department with fever and stridor that began this '
                          'morning. Over the last 20 minutes he has become quiet, stopped talking, leans forward, '
                          'drools and refuses to lie back. His voice is muffled. A pediatric resident pages '
                          'otolaryngology asking for a bedside flexible laryngoscopy to look at the epiglottis before '
                          'calling anesthesia. What is the safest response?',
                  'choices': ['Bedside flexible nasolaryngoscopy to confirm epiglottic swelling',
                              'Examination and intubation in the OR with anesthesia present',
                              'Lateral neck radiograph in the radiology suite, then decide',
                              'Nebulized epinephrine trial to see whether the stridor improves'],
                  'answer': 1,
                  'explanation': 'A febrile child who becomes quiet, drools, leans forward and has a muffled voice has '
                                 'a threatened supraglottic airway, and the quietness may signal fatigue, not '
                                 'improvement. Passing a scope through the nose of a frightened 3-year-old can cause '
                                 'crying, laryngospasm or complete obstruction. The safe response is to decline the '
                                 'bedside exam, keep him calm and upright, and move to the operating room, where '
                                 'examination and airway control occur with anesthesia and otolaryngology ready for '
                                 'bronchoscopy or tracheostomy.',
                  'why_wrong': ['Flexible laryngoscopy can be reasonable in a calm adult, but in a distressed young '
                                'child it can precipitate obstruction outside a controlled setting.',
                                'Correct.',
                                'Leaving the department for imaging separates a threatened airway from airway '
                                'expertise, and a radiograph does not change the need for controlled intubation.',
                                'Nebulized epinephrine treats croup and does not treat bacterial supraglottitis; any '
                                'brief improvement could falsely reassure the team.'],
                  'board_pearl': 'Drooling child with muffled voice: no bedside scope; examine and intubate in the '
                                 'operating room.',
                  'curveball': 'How would your approach differ in a stable older child or adult with supraglottitis '
                               'and no respiratory distress?',
                  'curveball_answer': 'A cooperative adolescent or adult without distress or stridor can safely '
                                      'undergo flexible laryngoscopy to confirm supraglottitis. Many are managed with '
                                      'IV antibiotics, steroids and close airway monitoring in an ICU without '
                                      'intubation. Airway intervention is reserved for stridor, drooling, rapid '
                                      'progression or significant airway compromise, with awake fiberoptic intubation '
                                      'or tracheostomy under local anesthesia as options.'},
 'v246_ped_croup_epi_fnd': {'stem': 'A 2-year-old boy had 2 days of runny nose and cough, then developed a barking '
                                    'cough, a hoarse voice and inspiratory stridor when agitated. His temperature is '
                                    '38.4 C. He is drinking, playful between coughing spells and has no drooling. This '
                                    'is his first such illness, and there is no history of allergies or similar '
                                    'nighttime episodes. Which diagnosis is most likely?',
                            'choices': ['Spasmodic (recurrent nocturnal) croup',
                                        'Acute epiglottitis',
                                        'Bacterial tracheitis',
                                        'Viral laryngotracheitis (croup)'],
                            'answer': 3,
                            'explanation': 'A viral prodrome followed by barking cough, hoarseness and inspiratory '
                                           'stridor in a nontoxic toddler is classic viral laryngotracheitis, most '
                                           'often parainfluenza. Subglottic edema produces the stridor and barky '
                                           'cough. The deciding clues are the viral prodrome with fever, a nontoxic '
                                           'appearance and handling of secretions. Epiglottitis more often causes '
                                           'toxicity, drooling and reluctance to lie down without a barking cough, and '
                                           'spasmodic croup recurs abruptly at night without a febrile prodrome.',
                            'why_wrong': ['Spasmodic croup starts abruptly at night without fever or a prodrome and '
                                          'recurs, often in atopic children, unlike this first febrile illness.',
                                          'Epiglottitis causes abrupt toxicity, drooling and muffled voice, usually '
                                          'without the barking cough this playful child has.',
                                          'Bacterial tracheitis causes toxicity, high fever and thick secretions with '
                                          'poor response to croup treatment, which this child does not show.',
                                          'Correct.'],
                            'board_pearl': 'Viral prodrome, barking cough, hoarseness, stridor and a nontoxic child: '
                                           'viral croup.',
                            'curveball': 'Which bedside sign tells you croup severity has progressed beyond a mild '
                                         'outpatient phenotype?',
                            'curveball_answer': 'Stridor at rest is the key sign that croup is at least moderate. '
                                                'Retractions at rest, agitation, decreasing level of consciousness, '
                                                'cyanosis or falling saturation, and decreased air entry mark severe '
                                                'or impending respiratory failure. A quiet child with less stridor but '
                                                'poor air movement is ominous, not improving.'},
 'v246_ped_croup_epi_app': {'stem': 'An unimmunized 4-year-old boy has a high fever, severe sore throat, drooling, '
                                    'muffled voice and soft stridor. He is sitting upright, leaning forward, on his '
                                    "mother's lap in the emergency department. Anesthesia and otolaryngology have been "
                                    'called and the operating room is being prepared. A transport attendant arrives '
                                    'with a stretcher to move him supine to the OR. What is the best way to move him?',
                            'choices': ['Supine on the stretcher with oxygen by face mask',
                                        'Supine with a nasal airway inserted before transport',
                                        'Upright with his parent, a physician carrying airway gear',
                                        'After sedation with intranasal midazolam to calm him'],
                            'answer': 2,
                            'explanation': 'Children with epiglottitis adopt an upright, forward-leaning posture to '
                                           'keep the swollen supraglottis off the airway. Lying them flat lets the '
                                           'epiglottis fall back and can cause complete obstruction, while separation '
                                           'from a parent provokes crying. He should travel to the operating room '
                                           'upright, ideally held by his parent, accompanied by a physician who can '
                                           'manage the airway, with a bag-mask, oxygen and intubation equipment. '
                                           'Sedation and airway adjuncts belong in the operating room, not the '
                                           'corridor.',
                            'why_wrong': ['Lying supine allows the swollen epiglottis to fall posteriorly and can '
                                          'convert partial obstruction into complete obstruction during transport.',
                                          'Inserting a nasal airway is a painful stimulus that can provoke '
                                          'laryngospasm, and it does not bypass supraglottic swelling.',
                                          'Correct.',
                                          'Sedation reduces airway tone and respiratory drive and can cause sudden '
                                          'obstruction outside the operating room.'],
                            'board_pearl': 'Transport suspected epiglottitis upright with a parent and an '
                                           'airway-capable physician; never supine or sedated.',
                            'curveball': 'Once the airway is secured, what antibiotic and intubation-duration plan is '
                                         'typical?',
                            'curveball_answer': 'After cultures from blood and the epiglottic surface, start a '
                                                'third-generation cephalosporin such as ceftriaxone, adding vancomycin '
                                                'or clindamycin if MRSA is a concern. Most children stay intubated for '
                                                'about 1 to 3 days. Extubation is done when there is an air leak '
                                                'around the tube or when repeat laryngoscopy shows that swelling has '
                                                'resolved, and if Hib grows, household contacts need rifampin when an '
                                                'incompletely vaccinated young child lives there.'},
 'v246_ped_croup_epi_snr': {'stem': 'A 3-year-old girl admitted with presumed severe croup has received dexamethasone '
                                    'and four doses of nebulized epinephrine over 12 hours. Her temperature has risen '
                                    'to 39.9 C, she appears toxic, has a brassy cough with thick purulent sputum, and '
                                    'her stridor is worsening. She is not drooling and can lie flat. Lateral neck '
                                    'radiograph shows a normal epiglottis with irregular tracheal air column. What is '
                                    'the best next step?',
                            'choices': ['Fifth dose of nebulized epinephrine with heliox in the ward',
                                        'Bronchoscopy with secretion removal, intubation and IV antibiotics',
                                        'Oral amoxicillin-clavulanate for presumed secondary pneumonia',
                                        'Repeat dexamethasone at a higher dose and reassess in 6 hours'],
                            'answer': 1,
                            'explanation': 'Failure of croup therapy with rising fever, toxicity, thick purulent '
                                           'secretions and a ragged tracheal air column is bacterial tracheitis, most '
                                           'often caused by S. aureus superinfecting viral laryngotracheitis. Adherent '
                                           'pseudomembranes and pus narrow the subglottis and trachea and can suddenly '
                                           'obstruct the airway. She needs urgent rigid or flexible bronchoscopy in '
                                           'the operating room to remove membranes and obtain cultures, usually with '
                                           'intubation, plus IV antibiotics covering S. aureus including MRSA.',
                            'why_wrong': ['More epinephrine and heliox temporize viral edema but cannot clear purulent '
                                          'tracheal membranes, and the delay risks sudden obstruction.',
                                          'Correct.',
                                          'Oral therapy is inadequate for a toxic child with an obstructing tracheal '
                                          'infection that requires airway control and debridement.',
                                          'Steroid escalation does not address bacterial infection or obstructing '
                                          'secretions, and waiting 6 hours risks respiratory arrest.'],
                            'board_pearl': 'Croup that fails therapy with toxicity and thick secretions: think '
                                           'bacterial tracheitis and bronchoscope.',
                            'curveball': 'At bronchoscopy, which endoscopic finding distinguishes bacterial tracheitis '
                                         'from isolated supraglottitis in a child like her?',
                            'curveball_answer': 'In bacterial tracheitis the epiglottis and supraglottis appear normal '
                                                'or only mildly inflamed, while the subglottis and trachea show thick '
                                                'purulent secretions, ulcerated, friable mucosa and adherent '
                                                'pseudomembranes. Supraglottitis shows a cherry-red swollen epiglottis '
                                                'and aryepiglottic folds with a relatively normal trachea. Tracheitis '
                                                'membranes often need repeated bronchoscopic removal.'},
 'v113-ped-02': {'stem': 'A 3-year-old boy has 4 days of fever after a cold, with refusal to eat, drooling and pain '
                         'when turning his head. He holds his neck tilted to the left and cries when it is extended. '
                         'There is no meningismus on flexion, and he is alert. Oral exam shows a fullness of the right '
                         'posterior pharyngeal wall displacing the uvula. Lateral neck radiograph shows widened '
                         'prevertebral soft tissue. Which diagnosis is most likely?',
                 'choices': ['Peritonsillar abscess',
                             'Bacterial meningitis',
                             'Retropharyngeal abscess',
                             'Atlantoaxial rotatory subluxation'],
                 'answer': 2,
                 'explanation': 'Retropharyngeal lymph nodes are prominent in young children and involute by about age '
                                '5, so suppurative adenitis after an upper respiratory infection is a disease of '
                                'toddlers. Infection in front of the prevertebral muscles causes painful, limited neck '
                                'extension, torticollis, dysphagia and drooling. The deciding clues are a unilateral '
                                'posterior pharyngeal bulge and widened prevertebral soft tissue on a lateral film. '
                                'Contrast CT then defines abscess versus phlegmon and the airway.',
                 'why_wrong': ['Peritonsillar abscess is typically seen in adolescents, with trismus, a bulging soft '
                               'palate above the tonsil and deviation of the uvula from that side.',
                               'Meningitis limits neck flexion, while retropharyngeal infection limits extension and '
                               'produces a posterior pharyngeal bulge and widened prevertebral tissue.',
                               'Correct.',
                               'Grisel syndrome can follow pharyngeal infection, but it causes fixed torticollis '
                               'without a posterior pharyngeal bulge or widened prevertebral tissue.'],
                 'board_pearl': 'Toddler with fever, torticollis, painful neck extension and posterior pharyngeal '
                                'bulge: retropharyngeal abscess.',
                 'curveball': 'Which imaging and airway features determine whether antibiotics alone are reasonable '
                              'versus drainage for this child?',
                 'curveball_answer': 'IV antibiotics alone are reasonable for a stable child without airway symptoms '
                                     'when CT shows a small or poorly defined collection or phlegmon. Drainage is '
                                     'favored for airway compromise, stridor or respiratory distress, toxicity, a '
                                     'large well-defined rim-enhancing collection, extension toward the mediastinum or '
                                     'carotid sheath, or failure to improve after 24 to 48 hours of IV antibiotics.'},
 'v116-ped-02': {'stem': 'A 3-year-old girl has 5 days of fever, torticollis, decreased oral intake and a muffled '
                         'voice. Today she has mild inspiratory stridor and sits forward to breathe, with a saturation '
                         'of 95%. Contrast CT shows a 3.5-cm rim-enhancing, low-density retropharyngeal collection '
                         'that narrows the oropharyngeal airway, without mediastinal extension. She has received one '
                         'dose of IV ampicillin-sulbactam. What is the best management?',
                 'choices': ['Continue IV antibiotics and repeat CT in 48 hours if not improved',
                             'Transoral drainage in the OR after a controlled intubation',
                             'Needle aspiration through the pharyngeal wall at the ED bedside',
                             'External transcervical drainage under local anesthesia, awake'],
                 'answer': 1,
                 'explanation': 'Antibiotics alone suit small collections in stable children, but this child has '
                                'airway narrowing with stridor and a large, mature rim-enhancing abscess, both '
                                'indications for drainage. The priority is a planned, controlled intubation in the '
                                'operating room with anesthesia and otolaryngology ready for a difficult airway, '
                                'because the bulging posterior pharyngeal wall can rupture or obstruct. Most medial '
                                'retropharyngeal abscesses are then drained transorally, with cultures guiding '
                                'continued IV antibiotics.',
                 'why_wrong': ['Stridor and a large mature collection make waiting unsafe; delay risks complete '
                               'obstruction, spontaneous rupture with aspiration or descending infection.',
                               'Correct.',
                               'Bedside aspiration in an awake child with a narrowed airway risks aspiration of pus '
                               'and loss of the airway without control.',
                               'External drainage is used for lateral extension near the great vessels, and an awake '
                               'approach in a toddler with stridor is unsafe.'],
                 'board_pearl': 'Retropharyngeal abscess with airway compromise: secure the airway in the OR, then '
                                'drain, usually transorally.',
                 'curveball': 'What complication should you consider if the infection tracks inferiorly, and which '
                              'imaging field should not be forgotten?',
                 'curveball_answer': 'Descending mediastinitis can follow spread through the retropharyngeal space or '
                                     'the danger space, which extends to the diaphragm. Any child with chest pain, '
                                     'dyspnea, worsening sepsis or inferior extension on neck CT should have contrast '
                                     'CT of the chest. Mediastinal collections need thoracic surgery input and often '
                                     'transthoracic or cervical mediastinal drainage.'},
 'v124_ped_07': {'stem': 'A 4-year-old boy is being treated with IV clindamycin for a retropharyngeal abscess. On day '
                         '2 he develops new pleuritic chest pain, tachypnea and rising fever. Contrast CT of the neck '
                         'shows the rim-enhancing collection extending caudally below the thoracic inlet, and a chest '
                         'CT shows fluid tracking along the posterior mediastinum. His airway remains patent. What is '
                         'the best next step?',
                 'choices': ['Broaden IV antibiotics and repeat neck CT in 48 hours before drainage',
                             'Transoral drainage of the neck component alone, without chest imaging',
                             'Image-guided needle aspiration of the neck collection for culture',
                             'Urgent drainage of neck and mediastinum with thoracic surgery'],
                 'answer': 3,
                 'explanation': 'Inferior extension into the posterior mediastinum converts a pediatric deep neck '
                                'infection into descending necrotizing mediastinitis, which carries high mortality '
                                'without aggressive source control. Retropharyngeal and danger-space infection can '
                                'reach the mediastinum along fascial planes. Management is airway protection, broad IV '
                                'antibiotics, and urgent combined drainage of the cervical and mediastinal components, '
                                'with thoracic surgery involved early and cervical or transthoracic approaches chosen '
                                'by the extent of disease. Repeat imaging guides further debridement.',
                 'why_wrong': ['Antibiotics alone fail in established mediastinal collections, and a 48-hour delay '
                               'allows sepsis and spread along mediastinal planes.',
                               'Draining only the neck leaves the mediastinal collection, which is the main source of '
                               'mortality in descending mediastinitis.',
                               'Aspiration gives cultures but provides no meaningful source control for a collection '
                               'already tracking into the mediastinum.',
                               'Correct.'],
                 'board_pearl': 'Deep neck infection tracking below the thoracic inlet: image the chest and drain with '
                                'thoracic surgery.',
                 'curveball': 'Cultures grow MRSA. How should antibiotic therapy and duration be planned after '
                              'drainage?',
                 'curveball_answer': 'Use IV vancomycin, or linezolid if vancomycin cannot be used, with anaerobic '
                                     'coverage until cultures exclude polymicrobial infection, guided by infectious '
                                     'disease input. Mediastinal involvement usually needs several weeks of therapy, '
                                     'with the IV-to-oral switch and total duration based on clinical response, '
                                     'normalizing inflammatory markers and follow-up imaging showing resolution of '
                                     'collections.'},
 'v135_ped_02': {'stem': 'A 4-year-old girl was admitted 48 hours ago with fever, torticollis and limited neck '
                         'extension. CT showed a 1.5-cm retropharyngeal hypodensity with ill-defined margins and '
                         'minimal rim enhancement. Her admission CRP was 80 mg/L. Despite IV ampicillin-sulbactam, she '
                         'still has a temperature of 39.5 C, now has mild inspiratory stridor and drools. Which '
                         'finding most strongly favors operative drainage?',
                 'choices': ['New stridor and persistent fever after 48 hours of IV antibiotics',
                             'Her age younger than 5 years, when retropharyngeal nodes suppurate',
                             'An admission CRP of 80 mg/L, indicating a severe bacterial infection',
                             'Ill-defined hypodensity on CT, consistent with a forming phlegmon'],
                 'answer': 0,
                 'explanation': 'Drainage decisions for pediatric retropharyngeal infection hinge on airway status, '
                                'toxicity, the size and maturity of the collection, and response to treatment. New '
                                'stridor with drooling is a sign of airway compromise, and persistent high fever after '
                                '48 hours of appropriate IV antibiotics indicates medical failure. Together they '
                                'warrant controlled airway management and drainage. Age, a single inflammatory marker '
                                'and an ill-defined hypodensity describe the disease but do not by themselves mandate '
                                'surgery.',
                 'why_wrong': ['Correct.',
                               'Young age explains why retropharyngeal adenitis occurs but does not indicate drainage, '
                               'and many young children respond to antibiotics alone.',
                               'An elevated CRP supports bacterial infection but is not a drainage criterion; airway '
                               'status and clinical response matter more.',
                               'Ill-defined hypodensity without a well-formed rim often reflects phlegmon, which '
                               'favors medical management rather than drainage.'],
                 'board_pearl': 'Drain pediatric deep neck infections for airway compromise, toxicity, a large mature '
                                'abscess or antibiotic failure.',
                 'curveball': 'Her drooling and stridor worsen while you are booking the OR. Where should the airway '
                              'be secured, and who should be present?',
                 'curveball_answer': 'Secure the airway in the operating room, not the ward or ED, with an experienced '
                                     'pediatric anesthesiologist and otolaryngologist present. Use inhalational '
                                     'induction with spontaneous ventilation or video laryngoscopy, gentle technique '
                                     'to avoid rupturing the abscess, suction ready to handle aspirated pus, and a '
                                     'rigid bronchoscope and tracheostomy tray immediately available.'},
 'v140_ped_09': {'stem': 'A 3-year-old boy has 3 days of fever, sore throat and neck pain with mild torticollis. He is '
                         'drinking fluids, handles his secretions, has no stridor or respiratory distress and can move '
                         'his neck with discomfort. Contrast CT shows a 1-cm ill-defined retropharyngeal '
                         'low-attenuation area without a rim-enhancing wall and no airway narrowing. What is the most '
                         'appropriate initial plan?',
                 'choices': ['Transoral incision and drainage in the operating room tonight',
                             'Discharge on oral clindamycin with a clinic visit in 2 days',
                             'Admit for IV antibiotics with serial airway and neck exams',
                             'Repeat contrast CT in 6 hours before starting antibiotics'],
                 'answer': 2,
                 'explanation': 'A small, ill-defined collection without a rim in a stable child usually represents '
                                'phlegmon or early suppurative adenitis, which often resolves with IV antibiotics '
                                'alone. He has no airway symptoms, toxicity or mediastinal extension, so drainage is '
                                'not indicated now. Admission allows IV coverage of streptococci, S. aureus and oral '
                                'anaerobes, such as ampicillin-sulbactam or clindamycin, along with close monitoring. '
                                'Drainage is reserved for airway compromise, clinical worsening or failure to improve '
                                'within about 48 hours.',
                 'why_wrong': ['Surgery for a phlegmon without a drainable abscess exposes him to anesthetic and '
                               'airway risk without benefit over IV antibiotics.',
                               'Outpatient oral therapy is inappropriate for a deep neck infection in a toddler who '
                               'can deteriorate quickly and needs airway monitoring.',
                               'Correct.',
                               'Repeat imaging before treatment delays antibiotics and adds radiation; repeat CT is '
                               'reserved for failure to improve or worsening.'],
                 'board_pearl': 'Small retropharyngeal phlegmon in a stable child: admit for IV antibiotics and watch '
                                'the airway.',
                 'curveball': 'During his admission, which clinical changes would mandate repeat imaging or operative '
                              'drainage?',
                 'curveball_answer': 'Persistent fever or no clinical improvement after 48 to 72 hours of IV '
                                     'antibiotics, new stridor, drooling or respiratory distress, worsening neck '
                                     'swelling or trismus, chest pain or signs of sepsis should trigger repeat '
                                     'contrast CT, and drainage if a mature abscess has formed or the airway is '
                                     'threatened. Chest pain should also prompt chest imaging for mediastinal '
                                     'extension.'},
 'v244_ped_dni_fnd': {'stem': 'A 2-year-old girl has 3 days of fever to 39.3 C, decreased oral intake, drooling and '
                              'refusal to move her neck. She resists extension more than flexion and has no rash or '
                              'altered mental status. Oral exam is limited but suggests posterior pharyngeal fullness. '
                              'A lateral neck radiograph shows prevertebral soft tissue measuring 12 mm at C2. Which '
                              'study should be obtained next?',
                      'choices': ['Lumbar puncture to exclude bacterial meningitis first',
                                  'Contrast-enhanced CT of the neck',
                                  'MRI of the cervical spine without contrast',
                                  'Repeat lateral film with the neck fully extended'],
                      'answer': 1,
                      'explanation': 'Fever, drooling and refusal of neck extension with prevertebral thickening on '
                                     'the lateral film strongly suggest retropharyngeal infection. Contrast-enhanced '
                                     'CT of the neck is the standard next study, because it distinguishes cellulitis, '
                                     'phlegmon and rim-enhancing abscess, shows airway narrowing and extension toward '
                                     'the mediastinum or carotid sheath, and guides the decision between IV '
                                     'antibiotics and drainage. The child should be monitored during imaging because '
                                     'airway compromise can progress.',
                      'why_wrong': ['Painful extension with a normal mental status and prevertebral widening points to '
                                    'a deep neck infection; LP does not image it and delays care.',
                                    'Correct.',
                                    'MRI requires prolonged sedation in a toddler with a possibly threatened airway '
                                    'and offers no advantage for initial deep neck abscess evaluation.',
                                    'Forcing the neck into extension is painful and adds no information beyond '
                                    'defining whether a drainable collection is present.'],
                      'board_pearl': 'Suspected retropharyngeal infection: contrast CT neck distinguishes phlegmon '
                                     'from abscess and guides drainage.',
                      'curveball': 'If her infection spread inferiorly, which fascial-space continuity would permit it '
                                   'to descend into the mediastinum?',
                      'curveball_answer': 'The retropharyngeal space, between the buccopharyngeal and alar fascia, '
                                          'ends at about the upper thoracic level, while the danger space, between the '
                                          'alar and prevertebral fascia, runs from the skull base to the diaphragm. '
                                          'Infection that ruptures through the alar fascia into the danger space can '
                                          'descend freely into the posterior mediastinum.'},
 'v244_ped_dni_app': {'stem': 'A 4-year-old girl was admitted 48 hours ago with a 1.5-cm retropharyngeal collection on '
                              'CT and started on IV ampicillin-sulbactam. Today she is afebrile for 24 hours, eating '
                              'soft foods, moving her neck more freely and has no stridor. Her CRP has fallen by half. '
                              'Her parents ask whether she needs drainage or another scan before going home. What is '
                              'the most appropriate plan?',
                      'choices': ['Repeat contrast CT to confirm resolution before switching to oral',
                                  'Transoral drainage because the rim-enhancing collection persists',
                                  'Stop antibiotics now because the clinical infection has resolved',
                                  'Switch to oral antibiotics without repeat imaging if she stays well'],
                      'answer': 3,
                      'explanation': 'Selected stable children with small retropharyngeal collections improve with IV '
                                     'antibiotics alone, and clinical response, not imaging, guides further care. '
                                     'Defervescence, improved oral intake and neck motion, absence of airway symptoms '
                                     'and falling inflammatory markers show success. She can complete a total course '
                                     'of roughly 2 weeks with an oral agent such as amoxicillin-clavulanate or '
                                     'clindamycin. Repeat CT and drainage are reserved for persistent fever, worsening '
                                     'symptoms or airway compromise.',
                      'why_wrong': ['Imaging lags behind clinical recovery and adds radiation; repeat CT is reserved '
                                    'for children who fail to improve or worsen.',
                                    'Drainage is not needed in a child who is improving clinically on antibiotics, '
                                    'even if a collection was present on admission.',
                                    'Stopping after 2 days risks relapse; deep neck infections need a full course, '
                                    'completed orally once the child is improving.',
                                    'Correct.'],
                      'board_pearl': 'Small pediatric retropharyngeal abscess improving on IV antibiotics: no repeat '
                                     'CT; finish an oral course.',
                      'curveball': 'If she had worsened overnight instead, which exam changes should trigger immediate '
                                   'airway or operative escalation?',
                      'curveball_answer': 'New or worsening stridor, drooling, muffled voice, increased work of '
                                          'breathing or desaturation, worsening torticollis or neck swelling, trismus, '
                                          'chest pain, persistent high fever with toxicity, or neurologic signs should '
                                          'trigger escalation. These call for urgent airway assessment in a controlled '
                                          'setting, repeat contrast CT if the airway allows, and operative drainage.'},
 'v244_ped_dni_snr': {'stem': 'A 6-year-old girl is on day 2 of IV clindamycin for a left parapharyngeal abscess. '
                              'Overnight she develops drooling, a muffled voice, trismus, inspiratory stridor and '
                              'increasing left neck swelling, with a saturation of 93% on room air. The resident '
                              'suggests repeating the CT before deciding on surgery. Anesthesia and otolaryngology are '
                              'available. What is the best next step?',
                      'choices': ['Controlled airway in the OR with surgical backup, then drainage',
                                  'Repeat contrast CT of the neck before deciding on drainage',
                                  'IV dexamethasone and 24 more hours of IV antibiotics',
                                  'Needle aspiration under sedation in the emergency department'],
                      'answer': 0,
                      'explanation': 'Progressive airway symptoms and failure of medical therapy turn a parapharyngeal '
                                     'abscess into an urgent airway and source-control problem. Trismus and pharyngeal '
                                     'swelling make laryngoscopy difficult, so induction must be planned around '
                                     'distorted anatomy, with awake or spontaneous-ventilation techniques, video or '
                                     'fiberoptic intubation, and an otolaryngologist ready for a surgical airway. '
                                     'Drainage, transoral or transcervical depending on the abscess relation to the '
                                     'great vessels, then follows. Waiting for another scan wastes time she may not '
                                     'have.',
                      'why_wrong': ['Correct.',
                                    'Leaving the airway team for imaging in a child with stridor and drooling risks '
                                    'obstruction in the scanner; the clinical change already decides management.',
                                    'Steroids may reduce edema but do not drain the abscess, and another day of failed '
                                    'medical therapy risks airway loss.',
                                    'Sedating a child with trismus and stridor outside a controlled setting can '
                                    'precipitate complete obstruction without airway control.'],
                      'board_pearl': 'Deep neck abscess with progressive airway signs on antibiotics: secure the '
                                     'airway in the OR and drain.',
                      'curveball': 'After drainage she improves, but her family asks about the chest. When would '
                                   'thoracic surgery involvement be necessary?',
                      'curveball_answer': 'Thoracic surgery should be involved when imaging shows extension below the '
                                          'thoracic inlet into the mediastinum, or when the child develops chest pain, '
                                          'dyspnea, pleural effusion or worsening sepsis that suggests mediastinitis. '
                                          'Combined cervical and mediastinal drainage, by cervical or transthoracic '
                                          'approaches, is often needed, and an empyema may need a chest tube or VATS.'},
 'v113-ped-03': {'stem': 'A 2-year-old boy is brought in 90 minutes after his sister saw him put something shiny from '
                         'the television remote drawer in his mouth. He is drooling and refusing his bottle but '
                         'breathing comfortably. Frontal chest radiograph shows a 20-mm round radiopaque object at the '
                         'thoracic inlet with a double-ring halo at its edge. His last meal was 2 hours ago. What is '
                         'the best next step?',
                 'choices': ['Observation for up to 24 hours to allow spontaneous passage',
                             'Emergent endoscopic removal without waiting for fasting',
                             'Chest CT to assess esophageal injury before any endoscopy',
                             'Repeat radiograph in 4 hours to see whether it has moved'],
                 'answer': 1,
                 'explanation': 'A double-ring or halo sign on the frontal film identifies a button battery, and a '
                                "20-mm lithium cell lodged in a toddler's esophagus is the highest-risk scenario. "
                                'Current through the moist mucosa generates hydroxide at the negative pole, causing '
                                'liquefactive necrosis that can become deep within about 2 hours. Removal is emergent '
                                'and should not wait for fasting, imaging or transfer delays that can be avoided. '
                                'Honey or sucralfate can be given while the team mobilizes, but only if they do not '
                                'delay endoscopy.',
                 'why_wrong': ['A 24-hour observation window applies to asymptomatic esophageal coins, not to '
                               'batteries that cause deep injury within hours.',
                               'Correct.',
                               'CT delays removal of the battery, which is causing ongoing injury; injury assessment '
                               'follows extraction.',
                               'Waiting for the battery to move allows hours of continued current flow and progressive '
                               'necrosis of the esophageal wall.'],
                 'board_pearl': 'Double-ring sign in the esophagus is a button battery: remove emergently, regardless '
                                'of fasting status.',
                 'curveball': 'After removal, which delayed vascular complication must remain on your radar if the '
                              'battery was near the aortic arch?',
                 'curveball_answer': 'Aortoesophageal fistula can develop days to weeks after removal as necrosis '
                                     'extends through the esophageal wall into the aorta. It often announces itself '
                                     'with a sentinel bleed, such as hematemesis or melena, before catastrophic '
                                     'hemorrhage. Injury near the aorta warrants vascular imaging such as CTA or MRI, '
                                     'prolonged monitoring and a plan for emergency cardiothoracic intervention.'},
 'v140_ped_02': {'stem': 'A 3-year-old girl underwent endoscopic removal of a 20-mm button battery from the '
                         'mid-esophagus after an estimated 8 hours of impaction. Endoscopy showed deep circumferential '
                         'necrosis with black eschar at the impaction site. She is now awake, hemodynamically stable '
                         'and asking for food. Her parents hope to take her home tonight. What is the most appropriate '
                         'plan?',
                 'choices': ['Discharge home on a soft diet and acid suppression after recovery',
                             'Covered esophageal stent placement now to prevent a later stricture',
                             'Admit, keep NPO and image the esophagus and its relation to the aorta',
                             'Elective esophageal dilation in 1 week to prevent stricture formation'],
                 'answer': 2,
                 'explanation': 'Battery injury progresses after removal as liquefactive necrosis continues into the '
                                'wall, so deep circumferential necrosis after a long impaction puts her at risk of '
                                'perforation, tracheoesophageal or aortoesophageal fistula, mediastinitis, stricture '
                                'and recurrent laryngeal nerve injury. She should be admitted, kept NPO with nutrition '
                                'support, and imaged with CT or MRI to define wall injury and proximity to the aorta '
                                'and trachea. A contrast study before feeding and serial reassessment then guide diet '
                                'advancement and the timing of discharge.',
                 'why_wrong': ['Early discharge and feeding ignore the days-to-weeks window in which deep injury can '
                               'perforate or erode into the aorta or trachea.',
                               'Stenting freshly necrotic tissue is not standard and can worsen the injury; stricture '
                               'is managed later if it develops.',
                               'Correct.',
                               'Strictures form over weeks and are treated when symptomatic; early dilation of '
                               'necrotic tissue risks perforation.'],
                 'board_pearl': 'Removing the battery does not end the injury: admit deep burns and image for fistula '
                                'risk.',
                 'curveball': 'Which location and injury severity should prompt vascular imaging and prolonged '
                              'monitoring?',
                 'curveball_answer': 'Mid-esophageal impaction, near the aortic arch, with deep, circumferential or '
                                     'full-thickness injury, especially after a long impaction or with the negative '
                                     'pole facing the aorta, should prompt CTA or MRI. If inflammation reaches the '
                                     'aorta without a safe fat plane, the child should stay hospitalized with serial '
                                     'imaging until the margin is safe, because fistula can present weeks later.'},
 'v245_ped_batt_fnd': {'stem': 'A 4-year-old boy is brought in after his father found an opened packet of spare '
                               'key-fob coin cells next to him about an hour ago. He is asymptomatic and eating '
                               'crackers. Frontal radiograph shows a 16-mm round radiopaque object in the upper '
                               'esophagus with a faint double contour at its rim, and the lateral view shows a '
                               'step-off at its edge. Which interpretation and plan are correct?',
                       'choices': ['Button battery; emergent removal despite the lack of symptoms',
                                   'Coin; observe up to 24 hours for passage since he is asymptomatic',
                                   'Coin; arrange elective removal tomorrow on the next endoscopy list',
                                   'Food bolus; give glucagon and recheck the radiograph in 2 hours'],
                       'answer': 0,
                       'explanation': 'On the frontal radiograph, a button battery shows a double-ring or halo contour '
                                      'from its two stacked electrodes, and the lateral film shows a step-off between '
                                      'the positive and negative sides, while a coin has a uniform density and a '
                                      'smooth, straight edge on the lateral view. Symptoms do not predict injury; many '
                                      'children with significant battery burns are asymptomatic early. An esophageal '
                                      'battery needs emergent endoscopic removal, with honey or sucralfate as a bridge '
                                      'in eligible children.',
                       'why_wrong': ['Correct.',
                                     'A coin has no double contour or lateral step-off, and observing a battery would '
                                     'allow ongoing hydroxide injury for hours.',
                                     'Elective scheduling is appropriate for some coins, but battery injury begins '
                                     'within 2 hours and cannot wait until tomorrow.',
                                     'Food boluses are radiolucent and do not form a sharply outlined round radiopaque '
                                     'disc with a double contour.'],
                       'board_pearl': 'Halo on AP and step-off on lateral distinguish a button battery from a coin.',
                       'curveball': 'Which side of the battery causes the most severe injury, and how can the lateral '
                                    'film help predict where damage will be worst?',
                       'curveball_answer': 'The negative pole, the narrower side on the lateral film, causes the most '
                                           'severe injury, because hydroxide forms there. If the negative side faces '
                                           'anteriorly, the trachea is at greatest risk for tracheoesophageal fistula; '
                                           'if it faces posteriorly or to the left in the mid-esophagus, the aorta and '
                                           'recurrent laryngeal nerve are more vulnerable.'},
 'v245_ped_batt_app': {'stem': 'A 2-year-old girl swallowed a 20-mm lithium button battery about 1 hour ago. She is at '
                               'a community hospital 90 minutes from the nearest pediatric endoscopy team, and '
                               'transfer is being arranged. A radiograph confirms the battery in the proximal '
                               'esophagus. She is alert, swallowing her saliva, with no drooling, hematemesis or '
                               'respiratory distress, and has no honey allergy. What is the best immediate plan?',
                       'choices': ['Keep her strictly NPO with no oral intake until endoscopy',
                                   'Give honey and observe for passage into the stomach overnight',
                                   'Delay the transfer until a 6-hour fasting interval has passed',
                                   'Give 10 mL of honey every 10 minutes during the transfer'],
                       'answer': 3,
                       'explanation': 'In children older than 12 months who are within 12 hours of ingestion and can '
                                      'swallow, honey coats the battery and buffers the hydroxide that forms at the '
                                      'negative pole, reducing the depth of esophageal injury. Current guidance is 10 '
                                      'mL of honey every 10 minutes for up to 6 doses on the way to definitive care, '
                                      'with sucralfate used in the hospital. Honey is a bridge, not a treatment: '
                                      'emergent endoscopic removal must not be delayed, and fasting status should not '
                                      'postpone extraction.',
                       'why_wrong': ['Strict NPO withholds a simple measure shown to reduce alkaline injury while she '
                                     'travels, and small honey volumes do not meaningfully raise anesthetic risk.',
                                     'Honey reduces injury only as a bridge; an esophageal battery must still be '
                                     'removed emergently and will not reliably pass.',
                                     'Waiting for a fasting interval allows hours of ongoing current flow and deep '
                                     'necrosis; removal should not be delayed for NPO status.',
                                     'Correct.'],
                       'board_pearl': 'Honey 10 mL every 10 minutes for up to 6 doses bridges to emergent removal in '
                                      'children over 1.',
                       'curveball': 'Which circumstances make honey inappropriate, including age and inability to '
                                    'swallow safely?',
                       'curveball_answer': 'Avoid honey in infants younger than 12 months because of the risk of '
                                           'infant botulism, in children with suspected perforation, mediastinitis or '
                                           'sepsis, in those who cannot swallow or protect the airway, in those with '
                                           'known honey allergy, and when ingestion was more than 12 hours ago. None '
                                           'of these should delay emergent endoscopic removal.'},
 'v245_ped_batt_snr': {'stem': 'A 2-year-old boy had a 20-mm button battery removed from the mid-esophagus 4 days ago '
                               'after prolonged impaction. Endoscopy showed deep circumferential injury. He is stable '
                               'without bleeding, and his parents want to go home. MRI shows transmural esophageal '
                               'inflammation abutting the aortic arch with no preserved fat plane between them. What '
                               'is the best next step?',
                       'choices': ['Discharge with outpatient endoscopy in 4 weeks to assess for stricture',
                                   'Elective aortic stent graft placement now to prevent a later fistula',
                                   'Continue inpatient monitoring and serial imaging until a margin returns',
                                   'Discharge on a proton pump inhibitor and sucralfate with diet advancement'],
                       'answer': 2,
                       'explanation': 'Injury from a button battery can continue after extraction, and transmural '
                                      'inflammation abutting the aorta without a preserved fat plane signals high risk '
                                      'of delayed aortoesophageal fistula, which can occur weeks later and is often '
                                      'fatal. He should remain hospitalized under a multidisciplinary team that '
                                      'includes cardiothoracic surgery, with serial MRI until a safe margin between '
                                      'the injury and the aorta is restored. Families and staff should know that any '
                                      'sentinel bleed means an immediate vascular emergency.',
                       'why_wrong': ['Outpatient follow-up leaves him far from emergency vascular care during the '
                                     'period in which fistula and catastrophic bleeding occur.',
                                     'Prophylactic aortic stenting is not standard care for an intact aorta and '
                                     'carries its own risks; surveillance guides intervention.',
                                     'Correct.',
                                     'Acid suppression and sucralfate do not prevent fistula from deep alkaline '
                                     'injury, and discharge removes protective monitoring.'],
                       'board_pearl': 'Battery injury abutting the aorta: stay inpatient with serial imaging until a '
                                      'safe margin returns.',
                       'curveball': 'What sentinel bleeding history would require immediate vascular-emergency '
                                    'escalation rather than routine endoscopic follow-up?',
                       'curveball_answer': 'Any hematemesis, bloody secretions, melena, a sudden drop in hemoglobin or '
                                           'unexplained hypotension after a mid-esophageal battery injury should be '
                                           'treated as a herald bleed from an aortoesophageal fistula. Call '
                                           'cardiothoracic and vascular surgery at once, obtain emergent CTA if the '
                                           'patient is stable, prepare blood products and avoid diagnostic endoscopy, '
                                           'which can trigger massive hemorrhage.'},
 'v113-ped-04': {'stem': 'A 3-week-old boy with hypoplastic aortic arch underwent arch reconstruction at 8 days of '
                         'age. Since extubation he has had a weak, breathy cry, mild stridor when agitated and '
                         'coughing with bottle feeds. His saturations are normal at rest. Flexible laryngoscopy shows '
                         'an immobile left vocal fold in the paramedian position with normal right fold motion and a '
                         'small posterior glottic gap. Which mechanism best explains his findings?',
                 'choices': ['Brainstem compression of the vagal nuclei by a Chiari malformation',
                             'Cricoarytenoid joint dislocation from traumatic endotracheal intubation',
                             'Superior laryngeal nerve injury from a traction injury during surgery',
                             'Left recurrent laryngeal nerve injury where it loops at the aortic arch'],
                 'answer': 3,
                 'explanation': 'The left recurrent laryngeal nerve hooks around the aortic arch at the ligamentum '
                                'arteriosum, so arch reconstruction, PDA ligation and other cardiothoracic procedures '
                                'commonly injure it. Iatrogenic injury is a leading cause of unilateral vocal fold '
                                'immobility in infants. A paramedian fold causes a weak, breathy cry and aspiration '
                                'risk from glottic insufficiency, with only mild stridor. Bilateral immobility, by '
                                'contrast, suggests a central cause such as Chiari malformation.',
                 'why_wrong': ['Chiari compression typically causes bilateral immobility with severe stridor rather '
                               'than an isolated left fold after arch surgery.',
                               'Arytenoid dislocation is uncommon and usually shows a displaced arytenoid; the timing '
                               'after arch surgery points to nerve injury.',
                               'Superior laryngeal nerve injury affects cricothyroid tension and supraglottic '
                               'sensation but does not immobilize the vocal fold.',
                               'Correct.'],
                 'board_pearl': 'Left vocal fold paralysis after cardiac surgery: recurrent laryngeal nerve injury at '
                                'the aortic arch.',
                 'curveball': 'At 4 months he still aspirates thin liquids. What findings would push you from '
                              'observation and feeding therapy toward injection, reinnervation or airway intervention?',
                 'curveball_answer': 'Persistent aspiration or pneumonia despite thickened feeds, failure to thrive, '
                                     'or a large glottic gap would favor temporary injection medialization, which can '
                                     'improve swallow and voice while recovery is awaited. Reinnervation, such as ansa '
                                     'cervicalis to recurrent laryngeal nerve, is considered for persistent paralysis '
                                     'in older children. Airway intervention is rarely needed for unilateral paralysis '
                                     'unless other lesions coexist.'},
 'v146_ped_16': {'stem': 'A 3-week-old girl born at term after an uncomplicated delivery has had high-pitched biphasic '
                         'stridor since birth with a normal-sounding cry. She feeds well, and her saturation is 96% on '
                         'room air with mild suprasternal retractions. There is no cardiac or surgical history, and '
                         'head circumference is normal. Flexible laryngoscopy shows both vocal folds immobile in a '
                         'paramedian position. Which evaluation is most important next?',
                 'choices': ['MRI of the brain and brainstem to look for a Chiari malformation',
                             'Laryngeal electromyography to predict whether function will recover',
                             'Modified barium swallow to assess the risk of silent aspiration',
                             'Echocardiogram to look for a vascular ring compressing both nerves'],
                 'answer': 0,
                 'explanation': 'Bilateral vocal fold immobility in a neonate is frequently neurologic or idiopathic, '
                                'and Arnold-Chiari malformation with or without hydrocephalus is the classic treatable '
                                'central cause. Brainstem compression stretches the vagus nerves, and early '
                                'decompression or shunting can restore function. Because she is stable, the next '
                                'priority is MRI of the brain and brainstem, while airway status is monitored closely. '
                                'A good cry with stridor is typical of bilateral paramedian folds, whereas unilateral '
                                'paralysis causes a weak cry.',
                 'why_wrong': ['Correct.',
                               'Laryngeal EMG can inform prognosis later but does not identify a treatable central '
                               'cause and is not the first priority.',
                               'Swallow assessment matters, but she is feeding well and missing a Chiari malformation '
                               'has far greater consequences.',
                               'Vascular rings compress the trachea and esophagus, causing tracheal symptoms, and '
                               'rarely produce bilateral vocal fold paralysis.'],
                 'board_pearl': 'Bilateral neonatal vocal fold paralysis: image the brain and brainstem for Chiari '
                                'malformation.',
                 'curveball': 'How does unilateral vocal fold immobility usually present differently in an infant '
                              'compared with this child?',
                 'curveball_answer': 'Unilateral immobility usually presents with a weak or breathy cry, feeding '
                                     'difficulty and aspiration, with mild or no stridor, because one mobile fold '
                                     'maintains the airway. Bilateral immobility with paramedian folds causes '
                                     'significant inspiratory or biphasic stridor and respiratory distress with a '
                                     'relatively normal cry. Unilateral palsy is more often iatrogenic, and bilateral '
                                     'palsy more often central or idiopathic.'},
 'v243_ped_vfi_fnd': {'stem': 'A 5-week-old girl was born at term by a difficult forceps delivery complicated by '
                              'shoulder dystocia. Since birth she has had a hoarse, weak cry and occasional sputtering '
                              'with breastfeeding, with mild stridor only when crying, normal saturations and steady '
                              'weight gain. Flexible laryngoscopy shows an immobile right vocal fold in a paramedian '
                              'position, with the left fold crossing the midline. Her parents ask whether she will '
                              'need a breathing tube in her neck. Which counseling is most accurate?',
                      'choices': ['Tracheostomy is usually needed until the fold recovers',
                                  'Early injection laryngoplasty is the standard first step',
                                  'Airway surgery is rarely needed; safe feeding guides care',
                                  'Immediate reinnervation offers the best chance of recovery'],
                      'answer': 2,
                      'explanation': 'Unilateral vocal fold immobility, here likely from vagal stretch at birth, '
                                     'usually leaves an adequate airway because the opposite fold abducts normally, so '
                                     'tracheostomy is rarely needed. The main problems are a weak cry and aspiration '
                                     'from glottic insufficiency. Management is an instrumental swallow study, feeding '
                                     'modification such as thickened feeds or pacing, and serial laryngoscopy, because '
                                     'some injuries recover and many infants compensate. Injection or reinnervation is '
                                     'considered later for persistent aspiration or dysphonia.',
                      'why_wrong': ['With one normally mobile fold and normal saturations, she has a stable airway, '
                                    'and tracheostomy is rarely needed for unilateral paralysis.',
                                    'Injection is reserved for persistent aspiration or poor feeding despite therapy, '
                                    'not as routine first-line treatment.',
                                    'Correct.',
                                    'Reinnervation is a later option for persistent paralysis; spontaneous recovery '
                                    'and compensation should be awaited first.'],
                      'board_pearl': 'Unilateral infant vocal fold paralysis threatens feeding and voice more than the '
                                     'airway.',
                      'curveball': 'Which birth, cardiac and neurologic histories are important causes of vocal fold '
                                   'immobility to ask about in an infant like her?',
                      'curveball_answer': 'Ask about cardiothoracic or neck surgery, such as PDA ligation, arch repair '
                                          'or tracheoesophageal fistula repair; birth trauma from a difficult forceps '
                                          'or shoulder dystocia delivery; prolonged intubation that may cause '
                                          'posterior glottic scar; and neurologic disease such as Chiari malformation, '
                                          'hydrocephalus or hypoxic injury. A congenital mediastinal or neck mass can '
                                          'also compress the nerve.'},
 'v243_ped_vfi_app': {'stem': 'A 2-day-old boy born at term develops loud biphasic stridor with marked retractions and '
                              'repeated desaturations to the low 80s despite high-flow nasal oxygen. His cry is '
                              'relatively strong. Flexible laryngoscopy shows both vocal folds immobile in the '
                              'paramedian position with a narrow glottic chink. Head ultrasound is pending. The '
                              'parents ask what will happen next. What is the most appropriate immediate management?',
                      'choices': ['Endoscopic posterior cordotomy now to widen the posterior glottis',
                                  'Intubation to secure the airway, then a full etiologic workup',
                                  'Bilateral injection laryngoplasty to improve glottic closure',
                                  'Continued high-flow oxygen and observation for 6 months'],
                      'answer': 1,
                      'explanation': 'Bilateral paramedian vocal fold immobility can critically narrow the glottis, '
                                     'and this infant is failing noninvasive support. The immediate priority is to '
                                     'secure the airway, usually by intubation, then perform MRI of the brain and '
                                     'brainstem, airway endoscopy and swallow assessment. Many infants with idiopathic '
                                     'or central bilateral paralysis recover within the first 1 to 2 years, so '
                                     'irreversible glottic-widening procedures are generally deferred, and '
                                     'tracheostomy is used if prolonged airway support is needed.',
                      'why_wrong': ['Cordotomy is irreversible and is deferred in infants because spontaneous recovery '
                                    'is common, especially before the cause is known.',
                                    'Correct.',
                                    'Injection medializes the folds and narrows the glottis further, which would '
                                    'worsen obstruction in bilateral paramedian paralysis.',
                                    'He already has repeated desaturations on high-flow oxygen, so observation without '
                                    'airway protection risks hypoxic injury or arrest.'],
                      'board_pearl': 'Bilateral neonatal vocal fold paralysis with distress: secure the airway first '
                                     'and defer irreversible surgery.',
                      'curveball': 'His MRI shows a Chiari II malformation with hydrocephalus. How does this change '
                                   'management and prognosis?',
                      'curveball_answer': 'A central cause becomes potentially reversible. Neurosurgery should treat '
                                          'the hydrocephalus with shunting and consider posterior fossa decompression, '
                                          'which can restore vocal fold motion when done early. Monitor the airway '
                                          'closely, because vocal fold function may recover over weeks to months, and '
                                          'watch for shunt malfunction, which can cause recurrent paralysis.'},
 'v243_ped_vfi_snr': {'stem': 'A 5-year-old boy has had a tracheostomy since 1 month of age for idiopathic bilateral '
                              'vocal fold paralysis. Serial laryngoscopy has shown no meaningful motion for 4 years, '
                              'and both folds rest near the midline. He has no aspiration on swallow study, a good '
                              'voice with speaking valve, normal lungs and an otherwise normal airway. His family '
                              'strongly wants decannulation. What is the most appropriate next step?',
                      'choices': ['Bilateral total arytenoidectomy to create the widest possible airway',
                                  'Bilateral injection laryngoplasty to bulk the folds toward midline',
                                  'Indefinite tracheostomy, since glottic surgery is not done in children',
                                  'Unilateral glottic widening, counseling about voice and aspiration risk'],
                      'answer': 3,
                      'explanation': 'After an adequate observation period without recovery, glottic-widening '
                                     'procedures can allow decannulation, but every millimeter of posterior airway is '
                                     'traded against voice quality and aspiration risk. Options include unilateral '
                                     'posterior cordotomy or partial arytenoidectomy, posterior cricoid split with '
                                     'cartilage grafting, and lateralization; selective reinnervation is an emerging '
                                     'option. A staged, unilateral approach preserves voice and swallow while '
                                     'improving airflow. His safe swallow, good pulmonary status and normal remaining '
                                     'airway make him a reasonable candidate.',
                      'why_wrong': ['Bilateral total arytenoidectomy creates a large airway at the cost of severe '
                                    'dysphonia and aspiration, so a staged unilateral approach is preferred.',
                                    'Injection medializes the folds and further narrows an airway that is already '
                                    'obstructed by paramedian folds.',
                                    'Glottic widening and posterior grafting are established in children, and his '
                                    'candidacy factors are favorable for decannulation.',
                                    'Correct.'],
                      'board_pearl': 'Persistent bilateral vocal fold paralysis: widen the glottis stepwise, trading '
                                     'airway against voice and aspiration.',
                      'curveball': 'How would severe baseline aspiration change the appetite for irreversible glottic '
                                   'widening?',
                      'curveball_answer': 'Severe aspiration argues against widening, because enlarging the posterior '
                                          'glottis further reduces airway protection and can cause recurrent '
                                          'pneumonia. Such a child may be better served by keeping the tracheostomy, '
                                          'optimizing feeding with thickened liquids or gastrostomy, and reconsidering '
                                          'decannulation only if swallow function improves, or by choosing a limited, '
                                          'reversible procedure.'},
 'v124_ped_04': {'stem': 'A 7-week-old boy born at term failed newborn hearing screening in both ears. Diagnostic ABR '
                         'today shows bilateral moderate sensorineural hearing loss with present wave V at 50-55 dB '
                         'nHL, normal tympanometry and absent otoacoustic emissions. His parents feel he startles to '
                         'loud noises and would rather wait to see whether his speech develops normally. Which '
                         'management is most appropriate?',
                 'choices': ['Repeat ABR at 6 months to confirm stability before fitting amplification',
                             'Hearing aids now, with the etiologic workup proceeding in parallel',
                             'Defer amplification until genetic testing identifies the cause',
                             'Cochlear implant candidacy evaluation now instead of hearing aids'],
                 'answer': 1,
                 'explanation': 'Confirmed bilateral SNHL in infancy is time-sensitive because the first months and '
                                'years are a critical period for auditory pathway and language development. JCIH '
                                'benchmarks call for diagnosis by 3 months and early intervention by 6 months. He '
                                'should be fitted with hearing aids promptly and enrolled in early intervention, while '
                                'etiologic evaluation, including CMV testing, genetic testing and selective imaging, '
                                'proceeds in parallel. Startle to loud sounds is expected with a moderate loss and '
                                'does not mean hearing is adequate for speech.',
                 'why_wrong': ['Delaying amplification for months wastes auditory input during a critical period; '
                               'thresholds are monitored after fitting rather than before.',
                               'Correct.',
                               'Etiologic testing informs prognosis and associated risks but should never delay '
                               'amplification and early intervention.',
                               'A moderate loss usually benefits from hearing aids; implant candidacy is considered '
                               'when aided access is inadequate.'],
                 'board_pearl': 'JCIH 1-3-6: screen by 1 month, diagnose by 3, intervene by 6; amplify while the '
                                'workup runs.',
                 'curveball': 'He also had prolonged neonatal jaundice and now has abnormal tone. Which broader '
                              'etiologic categories should move higher on the list?',
                 'curveball_answer': 'Hyperbilirubinemia raises concern for auditory neuropathy spectrum disorder and '
                                     'kernicterus-related injury to the brainstem auditory pathways, so ABR and OAE '
                                     'patterns need careful review. Congenital CMV, hypoxic-ischemic injury and '
                                     'syndromic or metabolic causes with neurologic involvement also move higher. '
                                     'Brain MRI, neurology and genetics referrals become more important.'},
 'v146_ped_12': {'stem': 'A 3-year-old boy has about 20 spoken words and often does not respond when called from '
                         'another room, but his parents say he turns to music. He passed newborn hearing screening and '
                         "has no ear infections. Otoscopy is normal, and he turned toward the pediatrician's voice "
                         'during a whisper test in the office. His pediatrician has referred him to speech therapy. '
                         'What is the most important next step?',
                 'choices': ['Speech therapy alone, since his newborn screening was passed',
                             'MRI of the brain to evaluate a central cause of language delay',
                             'Reassurance and a repeat office whisper test in 6 months',
                             'Formal audiology with play audiometry and tympanometry'],
                 'answer': 3,
                 'explanation': 'Every child with speech or language delay needs formal audiologic evaluation, because '
                                'office voice tests are unreliable and a passed newborn screen does not exclude '
                                'later-onset, progressive or mild loss. At age 3, conditioned play audiometry with '
                                'ear-specific thresholds, tympanometry and OAEs is appropriate, with ABR if behavioral '
                                'results are unreliable. Responding to music or loud sounds is consistent with a '
                                'high-frequency or partial loss. Hearing status must be established before speech '
                                'therapy alone is relied on.',
                 'why_wrong': ['A passed newborn screen misses later-onset and progressive loss, and therapy without '
                               'knowing hearing status can miss the cause of the delay.',
                               'Brain imaging is not first-line for language delay; hearing assessment is cheaper, '
                               'safer and essential before considering central causes.',
                               'Office whisper and voice tests are unreliable and cannot exclude mild or '
                               'frequency-specific loss; waiting 6 months loses critical time.',
                               'Correct.'],
                 'board_pearl': 'Every child with speech delay gets formal audiology, regardless of the newborn screen '
                                'result.',
                 'curveball': 'He cannot cooperate with play audiometry despite two attempts. What testing should '
                              'establish his hearing thresholds?',
                 'curveball_answer': 'Obtain sedated or natural-sleep ABR with click and frequency-specific tone-burst '
                                     'stimuli to estimate ear-specific thresholds, along with OAEs and tympanometry. '
                                     'If ABR is abnormal with present OAEs or cochlear microphonic, consider auditory '
                                     'neuropathy. Results guide amplification and the need for etiologic workup.'},
 'v245_ped_hl_fnd': {'stem': 'A 16-day-old girl born at term failed newborn hearing screening in both ears, and a '
                             'diagnostic ABR today confirms bilateral moderately severe sensorineural hearing loss. '
                             'She is otherwise well, with a normal examination and growth. No CMV testing has been '
                             'done. Her parents ask what should happen next and whether testing can wait until the '
                             'follow-up visit in a month. Which next step is most important?',
                     'choices': ['Temporal bone CT before any other testing or intervention',
                                 'GJB2 testing first, sending CMV testing only if it is negative',
                                 'Saliva or urine CMV PCR now, with referral for amplification',
                                 'Repeat diagnostic ABR in 3 months before starting any workup'],
                     'answer': 2,
                     'explanation': 'Etiologic evaluation and habilitation should run in parallel after confirmed '
                                    'congenital SNHL. The deciding clue is her age: congenital CMV can only be '
                                    'confirmed by PCR of saliva or urine collected within the first 21 days of life, '
                                    'after which postnatal infection cannot be excluded. Testing her now also '
                                    'identifies infants who may be candidates for antiviral therapy, which must start '
                                    'within the first month. Hearing aid fitting and early intervention should begin '
                                    'without waiting for results.',
                     'why_wrong': ['CT adds radiation and rarely changes early management; imaging is selected later '
                                   'according to severity and implant planning.',
                                   'Genetic testing has high yield, but delaying CMV testing past day 21 loses the '
                                   'diagnostic window for congenital infection.',
                                   'Correct.',
                                   'Waiting 3 months delays amplification during a critical period and makes '
                                   'congenital CMV impossible to diagnose by standard testing.'],
                     'board_pearl': 'Failed screen plus confirmed SNHL before 3 weeks: send CMV PCR immediately and '
                                    'start amplification.',
                     'curveball': 'What early-intervention timing benchmarks are commonly used after newborn hearing '
                                  'screening?',
                     'curveball_answer': 'The JCIH 1-3-6 benchmarks call for screening by 1 month, diagnostic '
                                         'audiology by 3 months and enrollment in early intervention by 6 months. JCIH '
                                         '2019 encourages programs that already meet these to aim for 1-2-3: screening '
                                         'by 1 month, diagnosis by 2 months and intervention by 3 months.'},
 'v245_ped_hl_app': {'stem': 'A 2-year-old girl has bilateral severe-to-profound congenital sensorineural hearing loss '
                             'and wears hearing aids. She sat at 10 months and walked at 22 months, and her gait is '
                             'unsteady in the dark. She has no dysmorphic features, preauricular pits, branchial '
                             'sinuses or goiter. CMV testing was never done in the newborn period. Genetic results are '
                             'pending. Which additional evaluation is most important?',
                     'choices': ['Dilated eye exam with electroretinography',
                                 'Renal ultrasound for branchio-oto-renal syndrome',
                                 'Urine CMV PCR to diagnose congenital infection now',
                                 'Thyroid function testing and a perchlorate test'],
                     'answer': 0,
                     'explanation': 'Congenital severe-to-profound SNHL with delayed motor milestones and unsteadiness '
                                    'in the dark suggests bilateral vestibular areflexia, the hallmark of Usher '
                                    'syndrome type 1. Retinitis pigmentosa develops in childhood, often before night '
                                    'blindness is noticed, so ophthalmology with electroretinography can make the '
                                    'diagnosis before visual symptoms. Diagnosis matters for communication planning, '
                                    'since visual sign language may become harder to use, and for early cochlear '
                                    'implantation. A structured etiologic workup directs testing to the phenotype.',
                     'why_wrong': ['Correct.',
                                   'Branchio-oto-renal syndrome is suggested by pits, branchial sinuses and ear '
                                   'anomalies, which she does not have.',
                                   'A positive CMV test at age 2 cannot distinguish congenital from postnatal '
                                   'infection; a stored newborn blood spot would be needed.',
                                   'Pendred syndrome causes enlarged vestibular aqueducts and later goiter, but does '
                                   'not explain vestibular areflexia with delayed walking.'],
                     'board_pearl': 'Congenital profound SNHL plus late walking: think Usher type 1 and get an ERG.',
                     'curveball': 'How would auditory neuropathy physiology change counseling about behavioral '
                                  'thresholds and cochlear implantation?',
                     'curveball_answer': 'In auditory neuropathy, OAEs or cochlear microphonics are present but ABR is '
                                         'absent or abnormal, so thresholds can fluctuate and speech understanding is '
                                         'worse than the audiogram predicts. Behavioral thresholds must guide '
                                         'amplification, and families should know hearing aids may give limited '
                                         'benefit. Cochlear implantation often helps, but cochlear nerve deficiency on '
                                         'MRI predicts poorer outcomes.'},
 'v245_ped_hl_snr': {'stem': 'An 11-month-old boy has bilateral severe-to-profound SNHL. He has worn well-fit hearing '
                             'aids for 5 months with intensive auditory-verbal therapy, but aided testing shows poor '
                             'speech detection and he is not babbling. MRI shows normal cochleae and cochlear nerves. '
                             'His parents prefer to wait for whole-exome sequencing results, expected in 4 months, '
                             'before considering surgery. What is the best recommendation?',
                     'choices': ['Wait for the exome results before any cochlear implant referral',
                                 'Cochlear implant evaluation now, while sequencing continues',
                                 'Higher-power hearing aids for 6 more months, then reassess',
                                 'Defer implantation until age 2, when testing is more reliable'],
                     'answer': 1,
                     'explanation': 'Cochlear implantation timing is driven by inadequate aided access and '
                                    'developmental need, not by completing every etiologic test. He has a demonstrated '
                                    'hearing aid trial with poor aided speech detection and absent babbling, and MRI '
                                    'confirms implantable anatomy. Implantation before about 12 months, and earlier in '
                                    'general, is associated with better spoken language outcomes, and implants are '
                                    'approved from 9 months of age. Genetic results can refine prognosis and '
                                    'counseling but should not cause months of avoidable auditory deprivation.',
                     'why_wrong': ['Exome results rarely change candidacy when imaging shows normal anatomy, and a '
                                   '4-month wait lengthens auditory deprivation.',
                                   'Correct.',
                                   'He already shows inadequate aided benefit after an appropriate trial, so more '
                                   'amplification time delays effective access.',
                                   'Implants are approved from 9 months, and waiting until 2 years worsens language '
                                   'outcomes compared with earlier implantation.'],
                     'board_pearl': 'Poor aided benefit in severe-to-profound SNHL: refer for cochlear implant '
                                    'evaluation without waiting on genetics.',
                     'curveball': 'What findings such as cochlear nerve deficiency or severe inner-ear malformation '
                                  'would materially change implant counseling?',
                     'curveball_answer': 'An absent or hypoplastic cochlear nerve on MRI predicts limited or no '
                                         'implant benefit and may lead to considering an auditory brainstem implant. '
                                         'Severe malformations such as labyrinthine aplasia or cochlear aplasia '
                                         'preclude cochlear implantation, while incomplete partition or common cavity '
                                         'anomalies raise risks of CSF gusher, electrode misplacement and variable '
                                         'outcomes.'},
 'v124_ped_05': {'stem': 'A 12-day-old boy born at term failed his newborn hearing screen in the right ear, and '
                         'diagnostic ABR today shows moderate right sensorineural hearing loss with normal left '
                         'hearing. He has normal growth, no rash and a normal neurologic exam. His mother had a mild '
                         'flu-like illness in the first trimester. The family asks whether CMV testing can wait until '
                         'the next visit in 3 weeks. Which plan is most appropriate?',
                 'choices': ['Saliva CMV PCR today, confirming a positive with urine PCR',
                             'Maternal CMV IgG and IgM serology to establish infection',
                             'Infant CMV IgM serology at the next visit in 3 weeks',
                             'Postpone testing until a repeat ABR confirms the loss at 3 months'],
                 'answer': 0,
                 'explanation': 'Congenital CMV is the most common nongenetic cause of congenital SNHL and can cause '
                                'unilateral loss. The diagnosis requires virus detection by PCR of saliva or urine '
                                'collected within the first 21 days of life, because infection acquired from birth '
                                'canal secretions or breast milk afterward cannot be distinguished from congenital '
                                'infection. A positive saliva result should be confirmed with urine, since breast milk '
                                'can contaminate saliva. Testing now also identifies whether antiviral therapy can be '
                                'discussed within the first month.',
                 'why_wrong': ['Correct.',
                               'Maternal serology shows past or recent maternal infection but cannot establish whether '
                               'the infant was infected in utero.',
                               'Infant IgM is insensitive and nonspecific, and testing at 5 weeks falls outside the '
                               'window for diagnosing congenital infection.',
                               'Waiting until 3 months makes congenital CMV impossible to confirm by standard testing '
                               'and delays any treatment discussion.'],
                 'board_pearl': 'Congenital CMV is diagnosed only by saliva or urine PCR collected within 21 days of '
                                'birth.',
                 'curveball': 'Another infant has confirmed congenital CMV but passes the newborn hearing screen. What '
                              'surveillance principle should you explain to that family?',
                 'curveball_answer': 'CMV-related hearing loss can be delayed in onset, progressive or fluctuating, so '
                                     'a passed screen does not mean hearing will stay normal. The child needs serial '
                                     'diagnostic audiology, commonly every 3 to 6 months in the first years and then '
                                     'annually through early childhood, with parents told to seek testing for any '
                                     'concern about hearing or speech.'},
 'v143_ped_02': {'stem': 'A 3-week-old girl born at term was found to have congenital CMV on a universal newborn '
                         'saliva screen, confirmed by urine PCR on day 10. She has a normal examination, platelet '
                         'count, liver tests and head ultrasound, and she passed newborn hearing screening in both '
                         'ears. Her parents ask whether she needs any further hearing follow-up or medicine. What is '
                         'the most appropriate counseling?',
                 'choices': ['No further hearing testing is needed after a bilateral screen pass',
                             'Start valganciclovir for 6 months to prevent later hearing loss',
                             'One diagnostic ABR at 12 months, then discharge if it is normal',
                             'Serial audiology through early childhood without antiviral therapy'],
                 'answer': 3,
                 'explanation': 'A minority of infants with asymptomatic congenital CMV develop SNHL, and much of it '
                                'appears after the newborn period or progresses over time. Normal newborn hearing '
                                'therefore does not end follow-up, and serial age-appropriate audiology is '
                                'recommended, typically every 3 to 6 months in the first years and then annually '
                                'through about age 5 or 6. Antiviral therapy is not routinely recommended for infants '
                                'with asymptomatic cCMV and normal hearing because benefit has not been shown and '
                                'valganciclovir causes neutropenia.',
                 'why_wrong': ['Congenital CMV hearing loss is often delayed or progressive, so a newborn screen pass '
                               'does not exclude later loss.',
                               'Valganciclovir is not routinely given to asymptomatic infants with normal hearing, '
                               'because benefit is unproven and neutropenia is a real risk.',
                               'A single test at 12 months misses loss that develops later in early childhood, so '
                               'surveillance must be repeated over years.',
                               'Correct.'],
                 'board_pearl': 'Congenital CMV with a passed screen still needs serial audiology through early '
                                'childhood.',
                 'curveball': 'At 14 months, testing shows new severe right SNHL with normal left hearing. How does '
                              'this change early-intervention and amplification or implant counseling?',
                 'curveball_answer': 'New unilateral severe loss still warrants early intervention referral, a hearing '
                                     'aid trial or remote microphone support, and closer monitoring of both ears, '
                                     'because CMV loss can progress and affect the other ear. If aided benefit is '
                                     'poor, cochlear implantation for single-sided deafness is an option, and earlier '
                                     'implantation supports better binaural outcomes. Antiviral therapy at this age is '
                                     'not supported.'},
 'v245_ped_cmv_fnd': {'stem': 'A 4-month-old girl was referred after failing newborn screening, but follow-up was '
                              'delayed. Diagnostic ABR now confirms bilateral moderate SNHL. A urine CMV PCR sent by '
                              'her pediatrician last week is positive. She is breastfed and attends daycare. Her '
                              'parents ask whether this proves CMV caused her hearing loss. Which interpretation and '
                              'next step are most accurate?',
                      'choices': ['It confirms congenital CMV; start valganciclovir for 6 months now',
                                  'It cannot prove congenital infection; test her newborn blood spot',
                                  'It proves postnatal infection, so CMV is unrelated to her loss',
                                  'It confirms congenital CMV, so no further etiologic workup is needed'],
                      'answer': 1,
                      'explanation': 'After 21 days of life, a positive PCR cannot separate congenital infection from '
                                     'postnatal acquisition through breast milk, daycare exposure or other contacts. '
                                     'The stored newborn dried blood spot, if available, can be tested by PCR to '
                                     'establish congenital infection retrospectively. A positive spot supports cCMV, '
                                     'but a negative spot does not fully exclude it because sensitivity is limited. '
                                     'Whatever the result, genetic testing and audiologic management should continue '
                                     'in parallel, and amplification should not wait.',
                      'why_wrong': ['A positive test at 4 months does not establish congenital infection, and '
                                    'valganciclovir started after 1 month did not improve hearing in a randomized '
                                    'trial.',
                                    'Correct.',
                                    'A positive result after 21 days is indeterminate, not proof of postnatal '
                                    'infection; congenital CMV may still be the cause.',
                                    'Even confirmed CMV does not exclude coexisting genetic causes, and the '
                                    'indeterminate result here leaves the etiology unresolved.'],
                      'board_pearl': 'CMV positive after 3 weeks of age is indeterminate; test the newborn dried blood '
                                     'spot.',
                      'curveball': 'Why can a stored newborn dried-blood-spot result help only partially when the '
                                   'early testing window was missed?',
                      'curveball_answer': 'Dried blood spot PCR is specific, so a positive result confirms congenital '
                                          'infection, but viral load in blood is often low and sensitivity varies by '
                                          'assay and storage, so a negative result does not exclude cCMV. Availability '
                                          'also depends on state retention policies. Clinicians weigh the result with '
                                          'the phenotype, including imaging findings such as calcifications.'},
 'v245_ped_cmv_app': {'stem': 'A 26-month-old boy with congenital CMV confirmed by urine PCR at 1 week had normal '
                              'hearing on diagnostic testing at 6 and 12 months. His family missed his 18-month '
                              'audiology visit. His speech has plateaued at about 15 words, and his daycare teacher '
                              'says he often ignores instructions. His parents believe his hearing is fine because he '
                              'passed earlier tests. What is the most important next step?',
                      'choices': ['Speech therapy referral alone, given his normal hearing at 12 months',
                                  'Evaluation for autism spectrum disorder before any hearing tests',
                                  'Diagnostic audiology now with ear-specific behavioral thresholds',
                                  'MRI brain to look for new periventricular white-matter injury'],
                      'answer': 2,
                      'explanation': 'Congenital CMV can cause hearing loss that begins or progresses after normal '
                                     'early results, and delayed-onset loss can appear throughout early childhood. A '
                                     'plateau in language with inattention to speech in a child with cCMV should be '
                                     'treated as possible new hearing loss until proven otherwise. He needs prompt '
                                     'diagnostic audiology with visual reinforcement or play audiometry and '
                                     'tympanometry, and ABR if needed. Missed surveillance visits are a common reason '
                                     'delayed CMV hearing loss is found late.',
                      'why_wrong': ['Normal hearing at 12 months does not exclude later loss in cCMV, so hearing must '
                                    'be retested before attributing delay to other causes.',
                                    'Developmental evaluation may be needed, but unrecognized hearing loss can mimic '
                                    'social-communication delay and must be excluded first.',
                                    'Correct.',
                                    'Brain imaging does not measure hearing and is not the next step; audiology is '
                                    'noninvasive and directly answers the question.'],
                      'board_pearl': 'In congenital CMV, new speech or attention concerns mean repeat audiology now, '
                                     'whatever earlier tests showed.',
                      'curveball': 'Which developmental or vestibular concerns should broaden his follow-up beyond '
                                   'pure-tone thresholds?',
                      'curveball_answer': 'Congenital CMV can cause vestibular hypofunction, which shows up as delayed '
                                          'sitting or walking, clumsiness and poor balance, so vestibular testing and '
                                          'physical therapy may help. Neurodevelopmental problems, including motor '
                                          'delay, cognitive impairment, seizures and visual issues such as '
                                          'chorioretinitis, also warrant developmental, neurology and ophthalmology '
                                          'follow-up.'},
 'v245_ped_cmv_snr': {'stem': 'A 20-month-old girl with congenital CMV has worn hearing aids since 7 months for '
                              'moderate bilateral SNHL. Over the past 6 months, her thresholds have fallen to '
                              'severe-to-profound in both ears, and aided testing now shows poor speech detection. She '
                              'had mild periventricular calcifications on neonatal imaging but is meeting motor '
                              'milestones. Her parents ask whether to wait until her hearing stops changing. What is '
                              'the best recommendation?',
                      'choices': ['Expedited cochlear implant evaluation without waiting for stability',
                                  'Wait 6 to 12 months until thresholds stabilize on serial audiograms',
                                  'Restart valganciclovir now in an effort to recover lost hearing',
                                  'Avoid implantation, since CMV-related brain injury predicts failure'],
                      'answer': 0,
                      'explanation': 'Progressive CMV-related SNHL can quickly narrow the window in which hearing aids '
                                     'provide useful speech access. Implant candidacy should be driven by poor aided '
                                     'performance and developmental need, not by waiting for thresholds to stabilize, '
                                     'since further decline is expected rather than reassuring. Most children with '
                                     'cCMV benefit substantially from cochlear implants, although outcomes vary with '
                                     'neurodevelopmental involvement. Counseling should note that hearing in the '
                                     'better ear may continue to decline.',
                      'why_wrong': ['Correct.',
                                    'Waiting for stability extends auditory deprivation while thresholds continue to '
                                    'fall, and progression is typical rather than temporary in cCMV.',
                                    'Valganciclovir started after the first month did not improve hearing outcomes in '
                                    'a randomized trial and carries hematologic toxicity.',
                                    'Mild calcifications with normal motor development do not preclude benefit, and '
                                    'most children with cCMV gain useful hearing from implants.'],
                      'board_pearl': 'Progressive CMV hearing loss with poor aided benefit: refer early for cochlear '
                                     'implant evaluation.',
                      'curveball': 'How would significant neurodevelopmental comorbidity change outcome counseling '
                                   'without automatically excluding implantation?',
                      'curveball_answer': 'Cognitive impairment, cerebral palsy or extensive white-matter injury '
                                          'lowers expected spoken language gains and can slow progress, so families '
                                          'should hear realistic goals such as sound awareness, safety and improved '
                                          'communication rather than full spoken language. Implantation is not '
                                          'excluded, and many such children still benefit; multidisciplinary '
                                          'assessment helps set expectations.'},
 'v124_ped_06': {'stem': 'A 14-year-old girl has had a pinpoint skin opening on the right side of her lower neck since '
                         'early childhood. It intermittently drains clear mucoid fluid, and it has become red and '
                         'tender three times, each treated with antibiotics. The opening lies at the anterior border '
                         'of the lower third of the sternocleidomastoid. She has no midline mass, and the thyroid is '
                         'normal. Which diagnosis is most likely?',
                 'choices': ['Infected epidermal inclusion cyst with a skin punctum',
                             'Thyroglossal duct sinus from a previously drained cyst',
                             'Second branchial cleft sinus or fistula tract',
                             'Cervical thymic cyst with a cutaneous opening'],
                 'answer': 2,
                 'explanation': 'A congenital pinpoint opening along the anterior border of the lower '
                                'sternocleidomastoid that drains mucoid fluid and becomes infected is the classic '
                                'external opening of a second branchial cleft sinus or fistula, the most common '
                                'branchial anomaly. Second cleft remnants are lined by epithelium that secretes mucus. '
                                'Definitive treatment is complete excision of the tract after infection has settled, '
                                'often through stepladder incisions, following it upward toward the tonsillar fossa to '
                                'prevent recurrence.',
                 'why_wrong': ['Epidermal inclusion cysts are not present from early childhood at a fixed anterior SCM '
                               'location and do not drain clear mucoid fluid.',
                               'Thyroglossal duct remnants are midline near the hyoid; a sinus forms only after '
                               'drainage of an infected midline cyst.',
                               'Correct.',
                               'Cervical thymic cysts are rare, usually present as a left-sided mass along the thymic '
                               'descent path and rarely drain through skin.'],
                 'board_pearl': 'Congenital mucoid-draining pit at the anterior lower SCM: second branchial cleft '
                                'sinus or fistula.',
                 'curveball': 'At surgery, the tract appears to pass between the internal and external carotid '
                              'arteries. Which branchial anomaly does that course suggest, and why does it matter '
                              'surgically?',
                 'curveball_answer': 'That course defines a second branchial cleft tract, which runs between the '
                                     'internal and external carotid arteries, superficial to the glossopharyngeal and '
                                     'hypoglossal nerves, toward the tonsillar fossa. Dissection must protect the '
                                     'carotid bifurcation, the hypoglossal nerve and the vagus, and the tract should '
                                     'be ligated at the pharynx to prevent recurrence.'},
 'v143_ped_01': {'stem': 'A 9-year-old boy is undergoing excision of a congenital draining pit at the anterior border '
                         'of the lower left sternocleidomastoid. A lacrimal probe passed into the opening travels '
                         'upward along the carotid sheath. Through a second stepladder incision, the tract is seen '
                         'passing between the internal and external carotid arteries, superficial to the hypoglossal '
                         'nerve. Where will the internal opening most likely be found?',
                 'choices': ['Apex of the ipsilateral piriform sinus',
                             'Ipsilateral tonsillar fossa',
                             'Cartilaginous external auditory canal',
                             'Foramen cecum of the tongue base'],
                 'answer': 1,
                 'explanation': 'Second branchial cleft tracts arise from the second cleft and pouch. They run from '
                                'the lower anterior sternocleidomastoid, along the carotid sheath, between the '
                                'internal and external carotid arteries, superficial to the glossopharyngeal and '
                                'hypoglossal nerves and deep to second arch structures such as the posterior belly of '
                                'the digastric, to end in the tonsillar fossa, the remnant of the second pouch. '
                                'Knowing this course allows complete excision and protection of neighboring nerves and '
                                'vessels.',
                 'why_wrong': ['The piriform sinus is the internal opening of third and fourth pouch tracts, which '
                               'pass posterior to the internal carotid artery or lower in the neck.',
                               'Correct.',
                               'The external auditory canal is linked to first branchial cleft anomalies, which arise '
                               'near the parotid and angle of the mandible.',
                               'The foramen cecum is the origin of the thyroglossal duct, a midline remnant unrelated '
                               'to the carotid bifurcation.'],
                 'board_pearl': 'Second cleft tract: between the ICA and ECA, over CN XII and IX, ending in the '
                                'tonsillar fossa.',
                 'curveball': 'How does a first branchial cleft anomaly change concern for the facial nerve during '
                              'surgery?',
                 'curveball_answer': 'First cleft tracts run from the angle of the mandible or periauricular skin '
                                     'toward the external auditory canal through the parotid region, and they may pass '
                                     'lateral to, medial to or between branches of the facial nerve. Surgery requires '
                                     'formal facial nerve identification, usually through a parotidectomy approach '
                                     'with nerve monitoring, and excision of any canal attachment.'},
 'v244_ped_bca_fnd': {'stem': 'An 11-year-old girl has a painless, soft, 3-cm right neck mass that appeared during a '
                              'cold 2 months ago and has not resolved. It lies just below the angle of the mandible '
                              'along the anterior border of the sternocleidomastoid, with no skin opening. Ultrasound '
                              'shows a thin-walled, mildly echogenic cyst posterior to the submandibular gland and '
                              'lateral to the carotid sheath, without internal flow. Which diagnosis is most likely?',
                      'choices': ['Macrocystic lymphatic malformation of the neck',
                                  'Cystic necrotic lymph node from metastatic disease',
                                  'Thyroglossal duct cyst in a lateral location',
                                  'Second branchial cleft cyst'],
                      'answer': 3,
                      'explanation': 'Second branchial cleft cysts are the most common branchial anomaly and '
                                     'classically present in older children or young adults as a soft lateral mass at '
                                     'the anterior border of the upper sternocleidomastoid that enlarges after an '
                                     'upper respiratory infection. The typical location posterior to the submandibular '
                                     'gland, lateral to the carotid sheath and anterior to the sternocleidomastoid is '
                                     'the deciding clue. Treatment is complete surgical excision once any infection '
                                     'has resolved.',
                      'why_wrong': ['Lymphatic malformations are usually present from infancy, are multiloculated and '
                                    'transspatial, and insinuate around structures rather than forming one thin-walled '
                                    'cyst.',
                                    'A cystic metastatic node is mainly an adult concern, and a thin-walled, '
                                    'unilocular cyst in a healthy 11-year-old is far more likely congenital.',
                                    'Thyroglossal duct cysts lie in or near the midline and move with tongue '
                                    'protrusion; lateral thyroglossal cysts are uncommon.',
                                    'Correct.'],
                      'board_pearl': 'Lateral cyst at the anterior upper SCM after a URI: second branchial cleft cyst; '
                                     'excise when quiet.',
                      'curveball': 'Which carotid and cranial nerve relationships help distinguish second from third '
                                   'or fourth cleft tracts?',
                      'curveball_answer': 'Second cleft tracts pass between the internal and external carotid arteries '
                                          'and over the hypoglossal nerve to the tonsillar fossa. Third pouch tracts '
                                          'pass posterior to the internal carotid and pierce the thyrohyoid membrane '
                                          'above the internal branch of the superior laryngeal nerve to reach the '
                                          'piriform sinus, while fourth pouch tracts run below the superior laryngeal '
                                          'nerve near the recurrent laryngeal nerve.'},
 'v244_ped_bca_app': {'stem': 'A 5-year-old boy has 4 days of fever and a tender, warm swelling in the left lower '
                              'anterior neck after a sore throat. TSH and free T4 are normal. Contrast CT shows a '
                              'rim-enhancing abscess involving the upper pole of the left thyroid lobe, with a thin '
                              'track of air extending superiorly toward the left piriform sinus. He had a smaller left '
                              'neck infection treated with antibiotics last year. Which underlying lesion is most '
                              'likely?',
                      'choices': ['Piriform sinus fistula from a third or fourth pouch remnant',
                                  'Infected thyroglossal duct cyst within the left thyroid lobe',
                                  'Suppurative lymphadenitis from Staphylococcus aureus alone',
                                  'Infected second branchial cleft cyst displaced inferiorly'],
                      'answer': 0,
                      'explanation': 'Recurrent left-sided lower neck infection or acute suppurative thyroiditis in a '
                                     'child points to a piriform sinus fistula from a third or fourth pharyngeal pouch '
                                     'remnant. The thyroid is normally resistant to infection, so thyroid abscess '
                                     'implies a route of entry, here a tract carrying pharyngeal flora from the '
                                     'piriform sinus apex. The left predominance reflects asymmetric embryologic '
                                     'development. After the acute infection is drained and treated, direct '
                                     'laryngoscopy identifies the opening for endoscopic cauterization or open '
                                     'excision.',
                      'why_wrong': ['Correct.',
                                    'Thyroglossal duct remnants are midline near the hyoid and do not explain a '
                                    'lateral thyroid abscess with a tract toward the piriform sinus.',
                                    'Simple lymphadenitis does not involve the thyroid lobe or produce an air track '
                                    'toward the piriform sinus, and recurrence suggests a congenital tract.',
                                    'Second cleft cysts lie at the upper anterior SCM and drain to the tonsillar '
                                    'fossa, not into the thyroid lobe or piriform sinus.'],
                      'board_pearl': 'Left-sided suppurative thyroiditis in a child: suspect a third or fourth pouch '
                                     'piriform sinus fistula.',
                      'curveball': 'Why can the piriform tract be difficult to identify while his acute inflammation '
                                   'is still active?',
                      'curveball_answer': 'Edema of the piriform mucosa can close or hide the internal opening, and '
                                          'inflammation obscures tissue planes on imaging and at surgery, so barium '
                                          'swallow and laryngoscopy may miss the tract while infection is active. Both '
                                          'are more reliable 6 or more weeks after the infection settles, when '
                                          'definitive endoscopic cauterization or open excision is safer and more '
                                          'accurate.'},
 'v244_ped_bca_snr': {'stem': 'A 3-year-old girl has a fluctuant, red, tender 3-cm mass just below the right earlobe '
                              'near the angle of the mandible, her third infection at this site. She has a small pit '
                              'in the floor of the right external auditory canal with intermittent otorrhea. Facial '
                              'nerve function is normal, and she is breathing and swallowing comfortably. Ultrasound '
                              'shows an abscess within the superficial parotid. What is the best management?',
                      'choices': ['Superficial parotidectomy with tract excision during infection',
                                  'Antibiotics with needle aspiration, then excision once quiet',
                                  'Wide incision and drainage with curettage of the whole tract',
                                  'Serial incision and drainage as the definitive treatment'],
                      'answer': 1,
                      'explanation': 'Recurrent infection below the earlobe with an opening in the external auditory '
                                     'canal is a first branchial cleft anomaly, Work type II, which runs through the '
                                     'parotid region and may pass lateral or medial to the facial nerve. During active '
                                     'infection, distorted planes make facial nerve injury and incomplete excision '
                                     'more likely. She should receive antibiotics with needle aspiration, avoiding '
                                     'incision through the infected field where possible. Definitive excision with '
                                     'facial nerve identification and monitoring follows after the inflammation '
                                     'settles.',
                      'why_wrong': ['Parotid dissection through inflamed, edematous tissue raises the risk of facial '
                                    'nerve injury and incomplete excision of the tract.',
                                    'Correct.',
                                    'Curettage near the facial nerve in an infected field risks nerve injury, and the '
                                    'epithelial tract left behind will recur.',
                                    'Repeated drainage leaves the epithelial tract and scars the field, making later '
                                    'facial nerve dissection harder and less safe.'],
                      'board_pearl': 'First cleft anomaly: control infection first, then excise with facial nerve '
                                     'identification and monitoring.',
                      'curveball': 'Which nerves are at risk during surgery for first, second, third and fourth cleft '
                                   'tracts?',
                      'curveball_answer': 'First cleft surgery endangers the facial nerve. Second cleft tracts risk '
                                          'the hypoglossal, glossopharyngeal, vagus and spinal accessory nerves and '
                                          'the marginal mandibular branch. Third and fourth pouch surgery risks the '
                                          'superior and recurrent laryngeal nerves, and fourth pouch excision with '
                                          'hemithyroidectomy puts the recurrent laryngeal nerve and parathyroids at '
                                          'particular risk.'}}
