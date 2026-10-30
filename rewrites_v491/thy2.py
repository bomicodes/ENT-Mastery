# v491 rewrites: Thyroid / Parathyroid / Salivary (batch thy2)
REWRITES = {'v137_tps_01': {'stem': 'A 78-year-old woman is on postoperative day 3 after a sigmoid colectomy. She has been NPO '
                         'with poor fluid intake and is receiving scheduled oral glycopyrrolate. She develops fever '
                         'and a tender, swollen, erythematous right parotid. Massage expresses pus from Stensen duct. '
                         'Ultrasound shows a diffusely enlarged, hypoechoic gland without a drainable collection or '
                         'calculus. Facial function is normal. What is the best initial management?',
                 'choices': ['Urgent sialendoscopy with ductal irrigation and saline dilation of Stensen duct',
                             'IV fluids, gland massage, sialogogues, and IV antistaphylococcal antibiotics',
                             'Incision and drainage through a preauricular parotid skin flap',
                             'Oral corticosteroids, warm compresses, and oral fluids without antibiotics'],
                 'answer': 1,
                 'explanation': 'Acute suppurative parotitis results from salivary stasis: dehydration, NPO status, '
                                'and anticholinergic drugs reduce flow, allowing retrograde ascent of Staphylococcus '
                                'aureus and oral flora up Stensen duct. The serous parotid secretion is less '
                                'bacteriostatic than mucinous saliva, which is why the parotid is favored. Initial '
                                'care restores flow and treats infection: IV hydration, massage, sialogogues, oral '
                                'hygiene, stopping xerogenic drugs where possible, and IV antistaphylococcal '
                                'antibiotics. Drainage is added only when imaging shows an abscess or the patient '
                                'fails to improve.',
                 'why_wrong': ['Instrumenting an acutely infected duct risks perforation and spread; sialendoscopy is '
                               'reserved for recurrent or obstructive disease after the acute infection settles.',
                               'Correct.',
                               'Ultrasound shows no drainable collection, so open drainage adds facial nerve risk '
                               'without a target.',
                               'Purulence from the duct indicates bacterial infection, and steroids without '
                               'antibiotics leave it untreated.'],
                 'board_pearl': 'Postoperative suppurative parotitis: rehydrate, massage, sialogogues, '
                                'antistaphylococcal antibiotics; drain only a proven abscess.',
                 'curveball': 'She improves, but months later she returns with chronic bilateral dry mouth, gritty '
                              'eyes, arthralgias, and recurrent painless parotid swelling. What workup is now '
                              'relevant?',
                 'curveball_answer': 'This pattern suggests Sjogren disease rather than recurrent bacterial infection. '
                                     'Review xerogenic medications, then check anti-SSA/Ro (with ANA, RF, and '
                                     'complement levels), objective ocular testing such as Schirmer and ocular '
                                     'staining, and unstimulated salivary flow. A labial minor salivary gland biopsy '
                                     'showing focal lymphocytic sialadenitis is weighted heavily in the 2016 ACR/EULAR '
                                     'criteria when serology is negative or the diagnosis is uncertain.'},
 'v146_tps_01': {'stem': 'You are called overnight about an 84-year-old man admitted from a nursing home with '
                         'pneumonia and dehydration. His nares screen is positive for MRSA. On day 2 he develops a '
                         'painful, swollen left parotid with fever. Bimanual massage expresses purulent saliva from '
                         'Stensen duct. Bedside ultrasound shows an inflamed gland without abscess or stone, and he is '
                         'hemodynamically stable. What is the most appropriate initial regimen?',
                 'choices': ['IV ampicillin-sulbactam with hydration, massage, and sialogogues',
                             'Hydration and sialogogues alone, holding antibiotics for culture results',
                             'CT-guided needle drainage of the gland followed by IV antibiotics',
                             'IV vancomycin with hydration, gland massage, and sialogogues'],
                 'answer': 3,
                 'explanation': 'Acute suppurative parotitis is treated by restoring salivary flow and covering the '
                                'likely organisms. Staphylococcus aureus is the dominant pathogen, and nursing-home '
                                'residents, recently hospitalized patients, and MRSA-colonized patients need empiric '
                                'MRSA coverage. Hydration, massage, warm compresses, sialogogues, and oral care '
                                'reverse stasis. Culture the expressed pus to tailor therapy, add anaerobic or '
                                'gram-negative coverage according to the clinical setting, and reimage if fever or '
                                'swelling persists beyond 48 to 72 hours, looking for an abscess that needs drainage.',
                 'why_wrong': ['Ampicillin-sulbactam covers oral flora and methicillin-sensitive staphylococci but '
                               'misses MRSA, which this colonized nursing-home patient likely carries.',
                               'Frank purulence with fever warrants empiric antibiotics now; culture guides narrowing '
                               'later rather than delaying treatment.',
                               'Ultrasound shows no collection, so needle drainage has no target and is premature.',
                               'Correct.'],
                 'board_pearl': 'Suppurative parotitis is mostly S. aureus; cover MRSA in nursing-home, hospitalized, '
                                'or colonized patients.',
                 'curveball': 'Forty-eight hours later he remains febrile and the gland has become fluctuant over the '
                              'angle of the mandible. What changes?',
                 'curveball_answer': 'Persistent fever with new fluctuance suggests abscess formation. Obtain contrast '
                                     'CT or ultrasound to define the collection and look for parapharyngeal or '
                                     'deep-neck extension. A drainable abscess is managed with ultrasound-guided '
                                     'aspiration or open drainage through a parotid-type incision with radial or blunt '
                                     'spreading parallel to facial nerve branches. Continue culture-directed '
                                     'antibiotics and check for airway compromise.'},
 'v237_tps_sialad_fnd': {'stem': 'A 69-year-old man with Parkinson disease recently started trihexyphenidyl and has '
                                 'had poor oral intake during a viral gastroenteritis. Over 36 hours he develops '
                                 'fever, trismus, and a tense, exquisitely tender right parotid swelling. Massage of '
                                 'the gland produces thick yellow fluid from the Stensen papilla. Labs show '
                                 'leukocytosis. Ultrasound shows diffuse glandular enlargement without calculi or '
                                 'ductal dilation. What is the most likely diagnosis?',
                         'choices': ['Acute bacterial suppurative parotitis',
                                     'Viral parotitis from paramyxovirus',
                                     'Obstructive sialadenitis from a parotid stone',
                                     'Infected first branchial cleft cyst'],
                         'answer': 0,
                         'explanation': 'Acute suppurative parotitis is a stasis disease: anticholinergic medication '
                                        'and dehydration reduce salivary flow, letting oral bacteria, chiefly '
                                        'Staphylococcus aureus, ascend Stensen duct. The deciding clues are a single '
                                        'tender gland, systemic inflammation, and pus expressed from the duct, with '
                                        'ultrasound showing no stone or duct dilation to suggest a primary obstructive '
                                        'cause. The tough parotid fascia limits expansion, so the gland is tense and '
                                        'very painful. Treatment is hydration, sialogogues, massage, and '
                                        'antistaphylococcal antibiotics, with imaging for abscess if it fails to '
                                        'settle.',
                         'why_wrong': ['Correct.',
                                       'Mumps is usually bilateral, occurs mainly in unvaccinated children or young '
                                       'adults, and produces clear rather than purulent ductal saliva.',
                                       'No calculus or ductal dilation is seen, and the presentation lacks the '
                                       'recurrent meal-related swelling typical of obstruction.',
                                       'A first cleft cyst presents as a recurrent cyst near the ear canal or angle of '
                                       'mandible, not diffuse gland swelling with ductal pus.'],
                         'board_pearl': 'Tender unilateral parotid plus ductal pus in a dehydrated patient on '
                                        'anticholinergics: acute suppurative parotitis.',
                         'curveball': 'What findings would suggest abscess formation or deep-neck extension requiring '
                                      'imaging and drainage?',
                         'curveball_answer': 'Suspect abscess when fever or swelling persists after 48 to 72 hours of '
                                             'appropriate antibiotics, the gland becomes fluctuant, or pus stops '
                                             'draining from the duct while swelling grows. Trismus beyond baseline, '
                                             'dysphagia, medial pharyngeal wall bulging, or neck swelling below the '
                                             'mandible suggests parapharyngeal extension. Obtain contrast CT, drain '
                                             'the collection, and protect the airway if needed.'},
 'v237_tps_sialad_app': {'stem': 'A 72-year-old woman takes oxybutynin, amitriptyline, and hydrochlorothiazide. She '
                                 'presents to clinic with 2 days of a tender, warm left parotid and low-grade fever. '
                                 'Pus is expressed from Stensen duct and sent for culture. She is eating and drinking, '
                                 'vital signs are stable, and ultrasound shows no abscess or calculus. Facial nerve '
                                 'function is normal. Which outpatient plan is most appropriate?',
                         'choices': ['Oral antistaphylococcal antibiotic alone, avoiding sialogogues and massage until '
                                     'the swelling fully settles',
                                     'Admission for IV antibiotics and CT-guided aspiration of the inflamed parotid '
                                     'gland',
                                     'Oral antistaphylococcal antibiotic with fluids, massage, sialogogues, and '
                                     'xerogenic drug review',
                                     'Oral prednisone taper with sialogogues and massage, deferring antibiotics to '
                                     'culture'],
                         'answer': 2,
                         'explanation': 'Uncomplicated acute suppurative parotitis in a stable patient who is drinking '
                                        'can be managed as an outpatient. Treatment must reverse stasis and treat '
                                        'infection at the same time: hydration, warm compresses, massage, sialogogues '
                                        'such as sour lozenges, oral hygiene, and an oral antibiotic covering '
                                        'Staphylococcus aureus and oral flora. Her anticholinergic and diuretic burden '
                                        'is the modifiable cause and should be reviewed with her prescribers. Close '
                                        'follow-up is needed, with imaging and drainage if she worsens or does not '
                                        'improve within 48 to 72 hours.',
                         'why_wrong': ['Sialogogues and massage restore flow and flush the duct; withholding them '
                                       'prolongs the stasis that drives the infection.',
                                       'She is stable, tolerating oral intake, and has no abscess, so admission and '
                                       'aspiration are unnecessary.',
                                       'Correct.',
                                       'Ductal pus means bacterial infection is already present, and steroids without '
                                       'antibiotics risk progression to abscess.'],
                         'board_pearl': 'Treat sialadenitis by fixing flow and infection together, and remove '
                                        'xerogenic drugs that caused the stasis.',
                         'curveball': 'A 6-mm stone is palpable at the Stensen papilla when she returns. How does that '
                                      'change source-control planning?',
                         'curveball_answer': 'A distal stone is a correctable cause of obstruction. Once the acute '
                                             'infection settles, plan transoral removal through a papillotomy or '
                                             'sialendoscopic basket retrieval, preserving the gland. Avoid '
                                             'instrumenting the duct during florid infection unless the stone is right '
                                             'at the papilla and easily delivered. Persistent stasis behind a retained '
                                             'stone predicts recurrent infection.'},
 'v237_tps_sjog_snr': {'stem': 'A 52-year-old woman has primary Sjogren disease, anti-SSA/Ro positive, for 9 years, '
                               'with intermittent symmetric parotid swelling that resolves within weeks. For 4 months '
                               'the left parotid has stayed firm and enlarged and is not tender. No pus is expressed '
                               'from either duct. She has two firm 1.5-cm left level II nodes and night sweats. What '
                               'is the most appropriate next step?',
                       'choices': ['Two weeks of amoxicillin-clavulanate and reassessment in clinic',
                                   'Increase hydroxychloroquine and add pilocarpine to improve salivary flow',
                                   'Ultrasound with core needle biopsy of the dominant parotid lesion',
                                   'Labial minor salivary gland biopsy to grade Sjogren activity'],
                       'answer': 2,
                       'explanation': 'Sjogren disease carries a markedly increased risk of B-cell non-Hodgkin '
                                      'lymphoma, most often extranodal marginal zone (MALT) lymphoma of the parotid, '
                                      'driven by chronic B-cell stimulation. The deciding clue is change in pattern: '
                                      'persistent unilateral firm enlargement, adenopathy, and B symptoms instead of '
                                      'the usual fluctuating bilateral swelling. This is not another flare. Ultrasound '
                                      'characterizes the gland and nodes, and core needle biopsy provides architecture '
                                      'for lymphoma diagnosis and flow cytometry. Other risk markers include low C4, '
                                      'cryoglobulinemia, and palpable purpura.',
                       'why_wrong': ['There is no pus, tenderness, or fever, so empiric antibiotics only delay '
                                     'diagnosis of a possible lymphoma.',
                                     'Escalating Sjogren therapy treats a presumed flare while ignoring red flags for '
                                     'a lymphoproliferative process.',
                                     'Correct.',
                                     'Her Sjogren diagnosis is established; a labial biopsy grades focal sialadenitis '
                                     'but does not sample the parotid mass.'],
                       'board_pearl': 'Persistent asymmetric gland enlargement in Sjogren is lymphoma until proven '
                                      'otherwise; get tissue with architecture.',
                       'curveball': 'Core biopsy shows a dense lymphoid infiltrate but is nondiagnostic for lymphoma '
                                    'subtype. Which biopsy strategy best preserves tissue architecture?',
                       'curveball_answer': 'Proceed to an excisional biopsy: excise an abnormal node intact, or '
                                           'perform superficial parotidectomy with facial nerve preservation if the '
                                           'disease is confined to the gland. Send fresh, unfixed tissue for flow '
                                           'cytometry, cytogenetics, and gene rearrangement studies. FNA alone cannot '
                                           'reliably subtype lymphoma, and incisional wedges of the parotid risk nerve '
                                           'injury and fistula.'},
 'v137_tps_02': {'stem': 'A 74-year-old woman has a left thyroid mass that has roughly doubled in 3 weeks, with '
                         'hoarseness and dysphagia to solids. She has mild exertional dyspnea but no stridor. Flexible '
                         'laryngoscopy shows left vocal fold paralysis with an adequate glottic airway. CT shows a '
                         '6-cm mass with extrathyroidal extension, tracheal deviation, and partial compression. '
                         'Outside FNA reports a poorly differentiated malignancy. What is the next step?',
                 'choices': ['Core biopsy for histology with expedited BRAF and NGS testing',
                             'Total thyroidectomy with radioactive iodine planned soon afterward',
                             'Repeat FNA with thyroglobulin washout in about 4 to 6 weeks',
                             'Awake tracheostomy before obtaining any further tissue'],
                 'answer': 0,
                 'explanation': 'Explosive growth, vocal fold paralysis, and invasive imaging in an older adult '
                                'indicate anaplastic thyroid carcinoma until proven otherwise. ATA 2021 guidance '
                                'treats this as an oncologic emergency: confirm the diagnosis with core or open '
                                'biopsy, because FNA can be nondiagnostic or confused with lymphoma or poorly '
                                'differentiated carcinoma, and obtain rapid molecular testing. BRAF V600E '
                                'immunohistochemistry can return within days and identifies candidates for '
                                'dabrafenib-trametinib. Staging, airway planning, and goals-of-care discussions '
                                'proceed at the same time.',
                 'why_wrong': ['Correct.',
                               'Resectability is undefined and ATC does not concentrate iodine, so upfront surgery '
                               'with RAI is the wrong plan.',
                               'Waiting weeks wastes critical time in a tumor that can obstruct the airway within '
                               'days.',
                               'Her glottic airway is adequate without stridor, so a tracheostomy through bulky tumor '
                               'is not yet indicated.'],
                 'board_pearl': 'Suspected ATC: core biopsy, rapid BRAF testing, staging, and airway planning happen '
                                'in parallel, not sequentially.',
                 'curveball': 'BRAF V600E is positive and the tumor is unresectable. How does that change systemic '
                              'treatment options?',
                 'curveball_answer': 'Dabrafenib plus trametinib is FDA-approved for BRAF V600E-mutant ATC and '
                                     'produces rapid, often dramatic responses. Many teams start it within days, '
                                     'sometimes before definitive staging is complete. A good response can convert an '
                                     'unresectable tumor into one suitable for neoadjuvant-then-surgery, followed by '
                                     'radiation. Immunotherapy may be added in selected patients through trials or '
                                     'expert centers.'},
 'v142_tps_01': {'stem': 'A 69-year-old man has a rapidly enlarging, fixed anterior neck mass with stridor at rest, '
                         'drooling, and inability to lie flat. Flexible laryngoscopy shows bilateral vocal fold '
                         'immobility with a narrow glottic chink. CT shows a 7-cm thyroid mass invading the tracheal '
                         'wall and encircling the esophagus. Core biopsy this morning is suspicious for anaplastic '
                         'carcinoma. Oxygen saturation is 93%. What is the immediate priority?',
                 'choices': ['Emergency debulking thyroidectomy to relieve the extrinsic tracheal compression',
                             'Start dabrafenib-trametinib empirically and monitor in the ICU',
                             'High-dose dexamethasone and heliox while awaiting outpatient staging',
                             'Secure the airway in the OR with awake intubation and surgical backup'],
                 'answer': 3,
                 'explanation': 'Stridor at rest, orthopnea, and bilateral vocal fold immobility mean the airway is '
                                'failing. The airway takes priority over staging. The safest plan is controlled airway '
                                'management in the operating room: awake fiberoptic intubation or awake tracheostomy '
                                'with the surgical team scrubbed, avoiding sedation that can convert partial to '
                                'complete obstruction. Tracheostomy through bulky invasive tumor can be very '
                                'hazardous, so the approach is chosen with anesthesia. ATA 2021 guidance discourages '
                                'heroic debulking; once the airway is secure, rapid molecular testing and '
                                'multidisciplinary planning resume.',
                 'why_wrong': ['An incomplete resection of invasive tumor adds major morbidity, often fails to relieve '
                               'the airway, and does not improve survival.',
                               'BRAF status is unknown and targeted therapy takes days to shrink tumor, which is too '
                               'slow for impending obstruction.',
                               'Steroids and heliox only temporize, and outpatient staging ignores an airway that is '
                               'failing now.',
                               'Correct.'],
                 'board_pearl': 'ATC with stridor: secure the airway in a controlled setting first; debulking does not '
                                'rescue the airway.',
                 'curveball': 'Why can tracheostomy be technically difficult or harmful in a bulky invasive anterior '
                              'neck tumor, and when is it nevertheless required?',
                 'curveball_answer': 'Tumor overlies and invades the trachea, distorting landmarks, bleeding heavily, '
                                     'and sometimes requiring a low or transtumoral approach; the stoma may be overrun '
                                     'by tumor and the tube can erode vessels. It is still required when obstruction '
                                     'is at or below the glottis and intubation is impossible or unsafe, such as '
                                     'bilateral vocal fold paralysis with stridor.'},
 'v234_tps_atc_fnd': {'stem': 'A 71-year-old man has had a small left thyroid nodule for 10 years that was never '
                              'biopsied. Over 5 weeks it has grown into a hard, fixed 6-cm mass with hoarseness, '
                              'dysphagia, and bulky ipsilateral adenopathy. He has no history of thyroiditis, and TPO '
                              'antibodies are negative. CT shows a heterogeneous, necrotic mass with coarse '
                              'calcifications invading the tracheal wall. What is the most likely diagnosis?',
                      'choices': ['Primary thyroid lymphoma',
                                  'Anaplastic thyroid carcinoma',
                                  'Medullary thyroid carcinoma (sporadic)',
                                  'Riedel thyroiditis'],
                      'answer': 1,
                      'explanation': 'Anaplastic thyroid carcinoma typically arises in older adults, often from a '
                                     'long-standing differentiated tumor that dedifferentiates as TP53 and TERT '
                                     'promoter mutations accumulate on a BRAF or RAS background. The deciding clues '
                                     'are weeks of explosive growth, a hard fixed mass, recurrent laryngeal nerve '
                                     'dysfunction, and a necrotic invasive tumor on CT. The absence of Hashimoto '
                                     'thyroiditis and the necrotic, calcified appearance argue against lymphoma. Every '
                                     'ATC is stage IV. Rapid core biopsy, molecular testing, and airway assessment '
                                     'should begin immediately.',
                      'why_wrong': ['Thyroid lymphoma usually arises in Hashimoto glands and appears homogeneous, with '
                                    'little necrosis or calcification.',
                                    'Correct.',
                                    'Medullary carcinoma usually grows slowly over years; weeks of explosive growth '
                                    'with necrosis point to anaplastic transformation.',
                                    'Riedel thyroiditis causes woody fibrosis that evolves over months to years, '
                                    'without a necrotic invasive mass.'],
                      'board_pearl': 'Older patient, long-standing nodule, weeks of explosive growth, necrotic '
                                     'invasive mass: anaplastic carcinoma until proven otherwise.',
                      'curveball': 'Which other diagnosis, especially thyroid lymphoma, must remain in the '
                                   'rapid-growth differential?',
                      'curveball_answer': 'Primary thyroid lymphoma, usually diffuse large B-cell or MALT type in a '
                                          'Hashimoto gland, also grows rapidly but is homogeneous and responds to '
                                          'chemotherapy and radiation rather than surgery. Core biopsy with flow '
                                          'cytometry separates the two. Also consider poorly differentiated carcinoma, '
                                          'squamous carcinoma, metastases, and hemorrhage into a benign nodule.'},
 'v234_tps_atc_app': {'stem': 'A 66-year-old woman has core biopsy-proven anaplastic thyroid carcinoma in a 5-cm right '
                              'thyroid mass. She has mild dysphagia but no stridor, and laryngoscopy shows mobile '
                              'vocal folds. CT shows extension into the strap muscles and abutment of the tracheal '
                              'wall. A multidisciplinary thyroid tumor board meets in 48 hours. Which study should be '
                              'expedited now because it most directly changes first-line therapy?',
                      'choices': ['Serum thyroglobulin and anti-thyroglobulin antibody levels',
                                  'Diagnostic whole-body radioiodine scan after rhTSH',
                                  'Serum calcitonin and carcinoembryonic antigen levels',
                                  'BRAF V600E immunohistochemistry and tumor NGS panel'],
                      'answer': 3,
                      'explanation': 'Modern ATC care depends on molecular results. BRAF V600E is present in a '
                                     'substantial subset of tumors, and immunohistochemistry can return within days '
                                     'while a broader NGS panel looks for other actionable alterations such as NTRK, '
                                     'RET, or ALK fusions and gives tumor mutational burden. ATA 2021 guidance '
                                     'recommends rapid molecular profiling because dabrafenib-trametinib can shrink '
                                     'BRAF-mutant tumors quickly and sometimes allow later resection. Staging with '
                                     'PET/CT or cross-sectional imaging and airway planning proceed at the same time.',
                      'why_wrong': ['Thyroglobulin reflects differentiated thyroid tissue and does not guide treatment '
                                    'of undifferentiated anaplastic carcinoma.',
                                    'Anaplastic carcinoma has lost the sodium-iodide symporter, so radioiodine imaging '
                                    'and therapy have no role.',
                                    'Calcitonin can help exclude medullary carcinoma, but the diagnosis is already '
                                    'confirmed on histology and these markers do not select therapy.',
                                    'Correct.'],
                      'board_pearl': 'In ATC, order BRAF V600E IHC immediately; a positive result opens '
                                     'dabrafenib-trametinib and neoadjuvant pathways.',
                      'curveball': 'BRAF V600E is positive and the tumor is borderline resectable. How can '
                                   'BRAF-directed therapy change management?',
                      'curveball_answer': 'Neoadjuvant dabrafenib-trametinib can shrink tumor away from the trachea '
                                          'and vessels within weeks, converting borderline or unresectable disease to '
                                          'resection with gross margins clear, followed by adjuvant radiation or '
                                          'chemoradiation. Series from expert centers report improved survival with '
                                          'this neoadjuvant-then-surgery approach. Response is reassessed with imaging '
                                          'every few weeks.'},
 'v234_tps_atc_snr': {'stem': 'An 80-year-old man has unresectable BRAF-wild-type anaplastic thyroid carcinoma with '
                              'lung metastases. He speaks comfortably, lies flat, and has no stridor. Laryngoscopy '
                              'shows one mobile vocal fold, and CT shows 40% tracheal narrowing from external '
                              'compression. Palliative radiation is planned. His daughter asks for a tracheostomy now '
                              "'before things get worse.' What is the best approach?",
                      'choices': ['Elective tracheostomy now while he can still lie flat for general anesthesia',
                                  'Defer tracheostomy and document an emergency airway plan with goals of care',
                                  'Place a prophylactic tracheal stent before radiation therapy begins',
                                  'Palliative debulking thyroidectomy to protect the airway in advance'],
                      'answer': 1,
                      'explanation': 'ATA 2021 guidance advises against routine prophylactic tracheostomy in '
                                     'anaplastic carcinoma. The procedure can be technically dangerous through '
                                     'invasive tumor, may need a low or transtumoral approach, and does not improve '
                                     'survival when obstruction is not imminent. It can also burden the time the '
                                     'patient has left. The right approach is individualized: continue tumor-directed '
                                     'therapy, discuss prognosis and goals of care openly, and document a clear plan '
                                     'for who secures the airway, where, and how if obstruction develops.',
                      'why_wrong': ['Tracheostomy through bulky invasive tumor is hazardous and has not been shown to '
                                    'prolong survival when the airway is not threatened.',
                                    'Correct.',
                                    'Stents in external compression can migrate, obstruct with secretions or tumor, '
                                    'and erode, so they are not placed preemptively.',
                                    'Incomplete resection of unresectable tumor carries major morbidity and does not '
                                    'provide durable airway protection.'],
                      'board_pearl': 'ATC without airway compromise: no prophylactic tracheostomy; make a contingency '
                                     'airway plan and discuss goals of care.',
                      'curveball': 'Which symptoms or endoscopic and imaging findings would convert observation into '
                                   'urgent airway intervention?',
                      'curveball_answer': 'Stridor at rest, orthopnea, inability to clear secretions, rising oxygen '
                                          'need, new bilateral vocal fold paralysis, or rapid progression of tracheal '
                                          'narrowing on imaging all signal impending obstruction. At that point, '
                                          'secure the airway in the operating room with awake intubation or awake '
                                          'tracheostomy, with anesthesia and surgeons ready, if consistent with his '
                                          'goals of care.'},
 'v137_tps_03': {'stem': 'A 44-year-old woman has a 2.8-cm papillary thyroid carcinoma in the right lobe. Ultrasound '
                         'shows a 1.2-cm round, hyperechoic right paratracheal node with microcalcifications; FNA with '
                         'thyroglobulin washout confirms metastatic papillary carcinoma. Lateral neck ultrasound is '
                         'normal, and laryngoscopy shows mobile vocal folds. Which operation is most appropriate?',
                 'choices': ['Total thyroidectomy with excision of the biopsied paratracheal node',
                             'Right lobectomy alone with radioiodine to treat the nodal disease',
                             'Total thyroidectomy with therapeutic right central neck dissection',
                             'Total thyroidectomy with right modified radical neck dissection'],
                 'answer': 2,
                 'explanation': 'Clinically involved central nodes from papillary carcinoma are treated with a '
                                'therapeutic, compartment-oriented dissection that removes prelaryngeal, pretracheal, '
                                'and paratracheal fibrofatty tissue en bloc while preserving the recurrent laryngeal '
                                'nerve and parathyroid blood supply. Removing only the visible node leaves the '
                                'remaining nodal tissue behind and makes later reoperation in a scarred field more '
                                'dangerous. With biopsy-proven N1a disease, total thyroidectomy is standard so that '
                                'radioiodine and thyroglobulin surveillance can be used. The lateral neck is treated '
                                'only when it is clinically involved.',
                 'why_wrong': ['Node plucking leaves adjacent microscopic disease and scars the compartment, raising '
                               'risk of central recurrence and reoperative injury.',
                               'Clinically evident nodal disease calls for total thyroidectomy and nodal clearance; '
                               'radioiodine does not reliably treat gross nodes.',
                               'Correct.',
                               'The lateral neck is clinically negative, so a lateral dissection adds morbidity '
                               'without oncologic benefit.'],
                 'board_pearl': 'Biopsy-proven level VI disease: therapeutic compartment dissection, not node '
                                'plucking; treat lateral neck only if involved.',
                 'curveball': 'How does the decision differ for a cN0 low-risk papillary cancer?',
                 'curveball_answer': 'For small (T1 or T2), noninvasive, clinically node-negative papillary carcinoma, '
                                     'prophylactic central dissection is generally not recommended. It increases '
                                     'hypoparathyroidism and nerve injury risk, and its benefit in central recurrence '
                                     'is uncertain. It is considered for T3 or T4 tumors, gross extrathyroidal '
                                     'extension, or clinically involved lateral nodes, and when nodal staging would '
                                     'change adjuvant therapy.'},
 'v142_tps_02': {'stem': 'A 37-year-old woman with papillary thyroid carcinoma and ultrasound-proven bilateral '
                         'paratracheal metastases is scheduled for total thyroidectomy with bilateral central neck '
                         'dissection. Preoperative CT shows no mediastinal or lateral neck disease. Before the case, '
                         'the attending asks the junior resident to define the anatomic limits of the dissection. '
                         'Which set of boundaries is correct?',
                 'choices': ['Hyoid to innominate artery, bounded laterally by the common carotid arteries',
                             'Hyoid to clavicle, bounded by the carotid sheath and posterior border of SCM',
                             'Cricoid to sternal notch, bounded by the tracheoesophageal grooves',
                             'Mandible to hyoid, bounded laterally by the anterior bellies of the digastric'],
                 'answer': 0,
                 'explanation': 'The central compartment, level VI, extends from the hyoid superiorly to the '
                                'innominate artery on the right and its corresponding level on the left inferiorly, '
                                'between the common carotid arteries, with the prevertebral fascia as the deep limit. '
                                'It contains prelaryngeal (Delphian), pretracheal, and paratracheal nodes. The 2009 '
                                'ATA consensus defines a bilateral dissection as removal of both paratracheal basins '
                                'plus the prelaryngeal and pretracheal nodes. Structures at risk include both '
                                'recurrent laryngeal nerves, the inferior parathyroids supplied by the inferior '
                                'thyroid artery, and the thymus.',
                 'why_wrong': ['Correct.',
                               'These limits describe the lateral neck levels II through IV, which lie lateral to the '
                               'carotid, not the central compartment.',
                               'This is too narrow; it omits the prelaryngeal nodes above the cricoid and lateral '
                               'paratracheal tissue out to the carotid.',
                               'These boundaries define the submental triangle, level IA, which drains the lip, chin, '
                               'and anterior floor of mouth.'],
                 'board_pearl': 'Level VI: hyoid to innominate artery, carotid to carotid, prevertebral fascia deep; '
                                'protect both RLNs and parathyroids.',
                 'curveball': 'How does a therapeutic dissection on the right differ anatomically near the recurrent '
                              'laryngeal nerve and innominate artery?',
                 'curveball_answer': 'The right RLN loops around the subclavian artery and runs a more oblique, '
                                     'lateral-to-medial course, so paratracheal tissue lies both anterior and '
                                     'posterior to the nerve and must be cleared from both sides. The left nerve, '
                                     'after looping the aortic arch, sits deeper and more vertically in the '
                                     'tracheoesophageal groove. Inferiorly, the innominate artery marks the floor of '
                                     'right level VI.'},
 'v234_tps_cnd_fnd': {'stem': 'A 41-year-old man has a 3.2-cm papillary thyroid carcinoma of the right lobe. '
                              'Ultrasound shows several enlarged, cystic nodes beside the trachea and one on the '
                              'cricothyroid membrane, while the jugular chain lateral to the carotid looks normal. FNA '
                              'of a paratracheal node confirms metastasis. He is scheduled for total thyroidectomy '
                              'with therapeutic central neck dissection. Which nodal groups does that dissection '
                              'remove?',
                      'choices': ['Prelaryngeal, pretracheal, and paratracheal nodes',
                                  'Upper, middle, and lower internal jugular nodes',
                                  'Retropharyngeal, parapharyngeal, and retrostyloid nodes',
                                  'Submental, submandibular, and perifacial nodes'],
                      'answer': 0,
                      'explanation': 'Central neck dissection clears level VI, the first-echelon drainage basin of '
                                     'papillary and medullary thyroid carcinoma. The compartment contains the '
                                     'prelaryngeal (Delphian) nodes on the cricothyroid membrane, the pretracheal '
                                     'nodes, and the right and left paratracheal nodes along the recurrent laryngeal '
                                     'nerves. Its limits are the hyoid above, the carotid arteries laterally, the '
                                     'prevertebral fascia deep, and the innominate artery or suprasternal region '
                                     'below, with superior mediastinal level VII included when involved. The lateral '
                                     'jugular chain is a separate compartment treated only when clinically involved.',
                      'why_wrong': ['Correct.',
                                    'The jugular chain forms levels II through IV, lateral to the carotid, and is '
                                    'addressed only by a lateral neck dissection.',
                                    'Retropharyngeal nodes lie behind the pharynx above the central compartment and '
                                    'are not part of a level VI dissection.',
                                    'These are level I nodes that drain the oral cavity and face, not first-echelon '
                                    'thyroid drainage.'],
                      'board_pearl': 'Central dissection removes prelaryngeal, pretracheal, and paratracheal nodes; '
                                     'jugular chain nodes belong to the lateral neck.',
                      'curveball': 'CT also shows a node just above the innominate artery, below the suprasternal '
                                   'notch. How is that node classified, and can it be reached through the neck?',
                      'curveball_answer': 'In AJCC nomenclature that node is level VII, superior mediastinal, because '
                                          'level VI ends at the suprasternal notch; the 2009 thyroid consensus extends '
                                          'level VI down to the innominate artery, so state the definition used. '
                                          'Either way, nodes above the innominate artery can usually be cleared '
                                          'transcervically by following the paratracheal tissue inferiorly, without '
                                          'sternotomy.'},
 'v234_tps_cnd_app': {'stem': 'A 49-year-old woman undergoes planned right lobectomy for a 1.8-cm Bethesda VI '
                              'papillary carcinoma; preoperative ultrasound showed no suspicious nodes. During the '
                              'operation, the surgeon palpates a firm 1-cm node in the right tracheoesophageal groove, '
                              'and frozen section confirms metastatic papillary carcinoma. Both recurrent laryngeal '
                              'nerves have normal signal on monitoring. What is the best intraoperative decision?',
                      'choices': ['Excision of that single node alone, then completion of the planned right lobectomy',
                                  'Completion of the lobectomy as planned, with radioiodine for residual nodes',
                                  'Completion of total thyroidectomy with therapeutic right central neck dissection',
                                  'Addition of a right lateral neck dissection of levels II through V'],
                      'answer': 2,
                      'explanation': 'An intraoperatively discovered, frozen-section-proven central node converts the '
                                     'case to clinically node-positive disease. The principle is compartment-oriented '
                                     'therapeutic dissection of the involved central basin rather than removal of the '
                                     'single node, because adjacent nodes are often involved and reentering a scarred '
                                     'central neck sharply raises nerve and parathyroid risk. With normal nerve '
                                     'signals on both sides, completing the total thyroidectomy is reasonable so '
                                     'radioiodine and thyroglobulin surveillance can be used. Parathyroids should be '
                                     'identified and preserved or autotransplanted if devascularized.',
                      'why_wrong': ['Plucking the positive node leaves adjacent disease in the compartment and '
                                    'guarantees a scarred reoperative field if more appears.',
                                    'Clinically apparent nodal metastasis justifies total thyroidectomy and nodal '
                                    'clearance now, rather than relying on radioiodine for gross disease.',
                                    'Correct.',
                                    'There is no evidence of lateral neck disease, so lateral dissection adds '
                                    'morbidity without oncologic benefit.'],
                      'board_pearl': 'Unexpected positive central node at lobectomy: do a compartment dissection and '
                                     'usually complete the thyroidectomy now.',
                      'curveball': 'How do preoperative vocal fold status and parathyroid-autotransplant planning '
                                   'affect the operation?',
                      'curveball_answer': 'Documented bilateral vocal fold mobility allows contralateral surgery; a '
                                          'preexisting paralysis would favor stopping after the ipsilateral side and '
                                          'staging any contralateral work. During central dissection, identify '
                                          'inferior parathyroids early, preserve their inferior thyroid artery supply, '
                                          'and inspect the specimen; autotransplant a devascularized or inadvertently '
                                          'removed gland into the SCM after frozen confirmation.'},
 'v234_tps_cnd_snr': {'stem': 'A 36-year-old woman has a 1.4-cm papillary thyroid carcinoma confined to the left lobe, '
                              'with no extrathyroidal extension on ultrasound and normal-appearing central and lateral '
                              'nodes. Laryngoscopy is normal. She has chosen lobectomy. A friend told her that '
                              "surgeons should 'clean out the lymph nodes just in case,' and she asks whether that "
                              'should be added. What is the best counseling?',
                      'choices': ['Lobectomy with ipsilateral prophylactic central dissection',
                                  'Lobectomy alone, without prophylactic central neck dissection',
                                  'Total thyroidectomy with bilateral prophylactic central dissection',
                                  'Lobectomy with lateral neck sentinel lymph node biopsy'],
                      'answer': 1,
                      'explanation': 'Microscopic central node metastases are common in papillary carcinoma but are '
                                     'usually clinically insignificant. For small (T1 or T2), noninvasive, clinically '
                                     'node-negative tumors, ATA guidance does not recommend routine prophylactic '
                                     'central dissection, because it increases transient and permanent '
                                     'hypoparathyroidism and recurrent laryngeal nerve injury without clear survival '
                                     'or recurrence benefit. Prophylactic dissection is considered for T3 or T4 '
                                     'tumors, gross extrathyroidal extension, or clinically involved lateral nodes, or '
                                     'when nodal staging will change adjuvant therapy. She can be counseled that '
                                     'lobectomy alone is appropriate.',
                      'why_wrong': ['For a small intrathyroidal cN0 tumor, prophylactic dissection adds parathyroid '
                                    'and nerve risk without a proven reduction in recurrence or death.',
                                    'Correct.',
                                    'Bilateral prophylactic dissection carries the highest hypoparathyroidism risk and '
                                    'is not recommended for a low-risk T1 tumor.',
                                    'Sentinel node biopsy is not standard in papillary thyroid carcinoma and would not '
                                    'change management of this low-risk tumor.'],
                      'board_pearl': 'Small intrathyroidal cN0 papillary carcinoma: no routine prophylactic central '
                                     'dissection, given parathyroid and RLN morbidity.',
                      'curveball': 'Which primary-tumor or nodal features would make prophylactic central treatment '
                                   'more reasonable in a patient like her?',
                      'curveball_answer': 'Prophylactic central dissection becomes reasonable with a tumor larger than '
                                          '4 cm, gross extrathyroidal extension into strap muscles or beyond, or '
                                          'clinically involved lateral neck nodes even when the central neck appears '
                                          'negative. It is also considered when the result would change radioiodine '
                                          'dosing or surgical extent, and some surgeons add it for aggressive '
                                          'histologic subtypes.'},
 'v137_tps_05': {'stem': 'A 62-year-old woman has calcium 11.4 mg/dL, intact PTH 98 pg/mL, a calcium-to-creatinine '
                         'clearance ratio of 0.03, a recent kidney stone, and a femoral neck T-score of -2.8. Neck '
                         'ultrasound, sestamibi SPECT/CT, and 4D-CT do not localize an abnormal gland. She has no '
                         'prior neck surgery and wants definitive treatment. What is the most appropriate management?',
                 'choices': ['Observation with repeat localization imaging every year until a target appears',
                             'Focused right inferior exploration, where single adenomas are most often found',
                             'Selective venous PTH sampling before any initial neck exploration is offered',
                             'Bilateral four-gland exploration by an experienced parathyroid surgeon'],
                 'answer': 3,
                 'explanation': 'Primary hyperparathyroidism is a biochemical diagnosis; imaging only plans the '
                                'operation. The normal calcium-to-creatinine clearance ratio excludes familial '
                                'hypocalciuric hypercalcemia, and stones plus osteoporosis meet guideline criteria for '
                                'surgery. Negative imaging is more common with small adenomas or multigland disease, '
                                'which a focused approach handles poorly. Bilateral exploration by an experienced '
                                'surgeon, systematically identifying all four glands using their embryologic '
                                'positions, cures most of these patients. Intraoperative PTH monitoring can be added '
                                'to confirm biochemical cure.',
                 'why_wrong': ['She meets surgical criteria with stones and osteoporosis; negative imaging does not '
                               'argue against the diagnosis or against surgery.',
                               'Without localization, a focused unilateral approach misses contralateral adenomas and '
                               'multigland disease that a bilateral exploration would find.',
                               'Invasive venous sampling is reserved mainly for reoperative cases after noninvasive '
                               'studies fail, not for an unoperated neck.',
                               'Correct.'],
                 'board_pearl': 'Negative localization does not cancel parathyroidectomy; it calls for bilateral '
                                'four-gland exploration by an experienced surgeon.',
                 'curveball': 'How does suspected multigland disease change the value of a focused approach?',
                 'curveball_answer': 'Multigland disease, from double adenomas or four-gland hyperplasia, is more '
                                     'likely with negative or discordant imaging, lithium use, hereditary syndromes, '
                                     'and modest calcium elevations. A focused approach that removes one enlarged '
                                     'gland can leave the patient with persistent disease, and intraoperative PTH can '
                                     'occasionally fall falsely. Bilateral exploration directly assesses every gland '
                                     'and is preferred when multigland disease is suspected.'},
 'v146_tps_04': {'stem': 'A 58-year-old man has primary hyperparathyroidism with calcium 11.1 mg/dL, elevated PTH, and '
                         'nephrolithiasis. Ultrasound shows a 9-mm hypoechoic nodule behind the lower pole of the '
                         'right thyroid lobe, but sestamibi SPECT/CT shows faint uptake behind the upper left lobe. He '
                         'has never had neck surgery. Which operative strategy is most appropriate?',
                 'choices': ['Focused right exploration based on the ultrasound finding',
                             'Bilateral exploration with intraoperative PTH monitoring',
                             'Focused left exploration based on the sestamibi finding',
                             'Defer surgery and repeat both studies in 12 months'],
                 'answer': 1,
                 'explanation': 'Concordant ultrasound and sestamibi strongly predict a single adenoma and allow a '
                                'focused approach. Discordant localization predicts more multigland disease and more '
                                'failures with focused surgery. The correct strategy is bilateral exploration using '
                                'embryology: superior glands lie posterior to the recurrent laryngeal nerve near the '
                                'cricothyroid junction, and inferior glands lie anterior to it near the lower pole or '
                                'thyrothymic ligament. Both candidate sites can be checked, all four glands assessed, '
                                'and intraoperative PTH used to confirm cure after excision.',
                 'why_wrong': ['Discordant studies lower confidence in any single target and raise the chance of '
                               'multigland disease, so a unilateral right approach may miss disease.',
                               'Correct.',
                               'Faint sestamibi uptake without ultrasound concordance is unreliable, and a unilateral '
                               'left approach may miss a right adenoma.',
                               'He has stones and meets criteria for surgery; discordant imaging is a reason to '
                               'explore bilaterally, not to delay.'],
                 'board_pearl': 'Discordant localization means higher multigland risk: plan bilateral exploration '
                                'rather than chasing one scan.',
                 'curveball': 'At bilateral exploration only three normal glands are found. What do you do next?',
                 'curveball_answer': 'Think about where the missing gland should be. A missing inferior gland is '
                                     'sought in the thyrothymic ligament and cervical thymus, which can be removed '
                                     'transcervically, then within the thyroid or carotid sheath. A missing superior '
                                     'gland is sought in the tracheoesophageal groove, retroesophageal space, '
                                     'posterior mediastinum, and undescended near the carotid bifurcation. Consider '
                                     'intraoperative ultrasound and ipsilateral thyroid lobectomy only after these '
                                     'sites are cleared.'},
 'v234_tps_4g_fnd': {'stem': 'A 55-year-old woman undergoes bilateral neck exploration for nonlocalized primary '
                             'hyperparathyroidism. On the left, after the recurrent laryngeal nerve and inferior '
                             'thyroid artery are identified, a 6-mm caramel-colored gland is found dorsal to the '
                             'nerve, about 1 cm above where the artery crosses it, near the cricothyroid junction. The '
                             'resident is asked to name the gland and its embryologic origin. Which is correct?',
                     'choices': ['Inferior parathyroid, from the third pharyngeal pouch',
                                 'Superior parathyroid, from the third pharyngeal pouch',
                                 'Inferior parathyroid, from the ultimobranchial body',
                                 'Superior parathyroid, from the fourth pharyngeal pouch'],
                     'answer': 3,
                     'explanation': 'A four-gland exploration depends on knowing where each gland should be. The '
                                    'superior parathyroids arise from the fourth pharyngeal pouch, migrate a short '
                                    'distance, and have a consistent position dorsal to the recurrent laryngeal nerve, '
                                    'cephalad to the inferior thyroid artery, near the cricothyroid junction. The '
                                    'inferior glands arise from the third pouch with the thymus, travel farther, and '
                                    'lie ventral to the nerve near the lower pole or in the thyrothymic ligament, with '
                                    'more variable ectopic positions. Systematic identification lets the surgeon judge '
                                    'single versus multigland disease.',
                     'why_wrong': ['Inferior glands usually lie anterior or ventral to the nerve near the lower '
                                   'thyroid pole, not dorsal near the cricothyroid junction.',
                                   'The third pouch gives rise to the inferior glands with the thymus; the superior '
                                   'glands arise from the fourth pouch.',
                                   'The ultimobranchial body gives rise to the parafollicular C cells; inferior glands '
                                   'arise from the third pouch and lie ventral to the nerve.',
                                   'Correct.'],
                     'board_pearl': 'Superior glands: fourth pouch, dorsal to the RLN near the cricothyroid junction; '
                                    'inferior glands: third pouch, ventral.',
                     'curveball': 'Where are the most important ectopic locations for superior versus inferior glands?',
                     'curveball_answer': 'Ectopic superior glands are found in the tracheoesophageal groove, '
                                         'retroesophageal or retropharyngeal spaces, and the posterior mediastinum, '
                                         'and occasionally within the thyroid. Ectopic inferior glands follow the '
                                         'thymic descent: thyrothymic ligament, cervical thymus, anterior mediastinum, '
                                         'or undescended high near the carotid bifurcation within the carotid sheath.'},
 'v234_tps_4g_app': {'stem': 'A 64-year-old woman with nonlocalized primary hyperparathyroidism undergoes bilateral '
                             'exploration. Baseline intraoperative PTH is 182 pg/mL. A 1.1-cm right inferior gland is '
                             'removed and frozen section confirms parathyroid tissue. The other three glands appear '
                             'normal in size and color. The 10-minute PTH is 151 pg/mL, and a repeat draw at 20 '
                             'minutes is 148 pg/mL. What is the best next step?',
                     'choices': ['Continue exploring for a second abnormal or ectopic gland',
                                 'Close, since an enlarged gland was found and removed',
                                 'Ipsilateral thyroid lobectomy to look for an intrathyroidal gland',
                                 'Excision of all three remaining normal-appearing glands'],
                     'answer': 0,
                     'explanation': 'Intraoperative PTH predicts cure when the level falls by more than 50% from the '
                                    'highest pre-excision value by 10 minutes, the Miami criterion. Here a repeat draw '
                                    'has already ruled out a timing or assay delay, so hyperfunctioning tissue '
                                    'remains. Possibilities include a second adenoma, hyperplasia of glands that look '
                                    'normal, or a supernumerary or ectopic gland. The surgeon should reassess the '
                                    'glands seen, biopsy or remove a clearly enlarged one, and then search ectopic '
                                    'sites systematically, including the thymus, before more extensive maneuvers.',
                     'why_wrong': ['Correct.',
                                   'A PTH drop of under 20% after removing the gland means hyperfunctioning tissue '
                                   'remains, so closing now risks persistent disease.',
                                   'Thyroid lobectomy is a late maneuver after the usual eutopic and ectopic sites, '
                                   'such as the thymus and carotid sheath, have been checked.',
                                   'Removing every remaining gland risks permanent hypoparathyroidism when the source '
                                   'may be a supernumerary or ectopic gland.'],
                     'board_pearl': 'IOPTH failing to fall by more than 50% after excision means more hyperfunctioning '
                                    'tissue; keep exploring.',
                     'curveball': 'Which ectopic sites should be revisited before escalating to a more extensive '
                                  'mediastinal exploration?',
                     'curveball_answer': 'Revisit the thyrothymic ligament and cervical thymus with a transcervical '
                                         'thymectomy, the tracheoesophageal groove and retroesophageal space down to '
                                         'the posterior mediastinum, the carotid sheath up to the bifurcation for an '
                                         'undescended gland, and the thyroid itself with intraoperative ultrasound. '
                                         'Sternotomy or thoracoscopy is reserved for a later, image-guided operation.'},
 'v234_tps_4g_snr': {'stem': 'A 28-year-old man with MEN1 from a known menin mutation and a treated prolactinoma has '
                             'calcium 11.2 mg/dL, elevated PTH, and a kidney stone. Sestamibi shows uptake only at the '
                             'right inferior gland, and ultrasound shows a 1-cm nodule there. He has had no neck '
                             'surgery and asks for the most durable operation. What is the most appropriate procedure?',
                     'choices': ['Focused excision of the localized right inferior gland with intraoperative PTH only',
                                 'Total parathyroidectomy with no autotransplantation and calcitriol lifelong',
                                 'Bilateral exploration, subtotal parathyroidectomy, and transcervical thymectomy',
                                 'Bilateral exploration with excision of only grossly enlarged glands seen'],
                     'answer': 2,
                     'explanation': 'MEN1 hyperparathyroidism is almost always multigland hyperplasia, often '
                                    'asymmetric and asynchronous, and imaging that shows one gland is misleading. The '
                                    'standard initial operation is bilateral exploration with subtotal (3.5-gland) '
                                    'parathyroidectomy, leaving a well-vascularized remnant marked with a clip, plus '
                                    'transcervical thymectomy because supernumerary and thymic glands are common. '
                                    'Total parathyroidectomy with forearm autotransplantation is an alternative. The '
                                    'goal balances recurrence, which is likely over his lifetime, against permanent '
                                    'hypoparathyroidism, and the remnant location must be documented for future '
                                    'surgery.',
                     'why_wrong': ['MEN1 hyperparathyroidism is multigland and asynchronous, so excising the imaged '
                                   'gland alone leads to early persistence or recurrence.',
                                   'Removing every gland without autotransplant guarantees permanent '
                                   'hypoparathyroidism in a young man and is not standard.',
                                   'Correct.',
                                   'Removing only visibly enlarged glands leaves asymmetrically hyperplastic tissue '
                                   'and carries a high recurrence rate.'],
                     'board_pearl': 'MEN1 hyperparathyroidism: subtotal parathyroidectomy plus transcervical '
                                    'thymectomy, regardless of single-gland imaging.',
                     'curveball': 'How does preservation or cryopreservation planning change when the patient is young '
                                  'and recurrence is likely?',
                     'curveball_answer': 'Choose and clip the most normal-appearing gland for the remnant, ideally '
                                         'away from the recurrent nerve, so reoperation is predictable. Cryopreserve '
                                         'resected parathyroid tissue when available, because delayed autograft can '
                                         'treat later permanent hypoparathyroidism. Forearm autotransplantation is an '
                                         'alternative that allows recurrence to be treated under local anesthesia '
                                         'instead of reentering the neck.'},
 'v137_tps_06': {'stem': 'A 47-year-old woman has a 2.0-cm solid, isoechoic, smooth-margined right thyroid nodule '
                         '(TI-RADS 3) with normal TSH. Two FNAs 3 months apart are both Bethesda III, atypia of '
                         'undetermined significance. She has no radiation exposure or family history. She is anxious, '
                         'prefers a definitive tissue answer, and her insurer does not cover molecular testing. Which '
                         'management is most appropriate?',
                 'choices': ['Total thyroidectomy with central neck dissection',
                             'Radioiodine uptake scan to judge malignancy risk',
                             'Diagnostic right thyroid lobectomy',
                             'Levothyroxine suppression and repeat ultrasound'],
                 'answer': 2,
                 'explanation': 'Bethesda III cytology carries an intermediate malignancy risk, so management is a '
                                'risk-and-preference decision. ATA guidance supports repeat FNA or molecular testing, '
                                'followed by surveillance or diagnostic surgery, chosen with the patient. Her repeated '
                                'AUS result, a nodule of 2 cm, unavailable molecular testing, and a preference for a '
                                'definitive answer make diagnostic lobectomy the best fit. Lobectomy gives a '
                                'histologic diagnosis with lower risk than total thyroidectomy, and current ATA '
                                'guidance accepts lobectomy as definitive surgery for many low-risk cancers if one is '
                                'found.',
                 'why_wrong': ['Indeterminate cytology is not a cancer diagnosis; total thyroidectomy with nodal '
                               'dissection overtreats a nodule most likely to be benign.',
                               'With a normal TSH, uptake scanning does not stratify malignancy, and most cold nodules '
                               'are benign.',
                               'Correct.',
                               'TSH suppression does not reliably shrink nodules or clarify cytology and carries '
                               'cardiac and bone risks.'],
                 'board_pearl': 'Indeterminate cytology warrants diagnostic lobectomy, not total thyroidectomy, when '
                                'surgery is chosen.',
                 'curveball': 'How would a highly suspicious ultrasound phenotype change the pretest probability of '
                              'cancer in this nodule?',
                 'curveball_answer': 'A TI-RADS 5 pattern, such as a solid hypoechoic nodule that is taller than wide '
                                     'with irregular margins or microcalcifications, raises the pretest malignancy '
                                     'risk well above the Bethesda III average. Molecular results then have lower '
                                     'negative predictive value, and many surgeons proceed to diagnostic or definitive '
                                     'surgery rather than rely on a benign molecular call.'},
 'v143_tps_02': {'stem': 'A 55-year-old man has a 2.2-cm solid, isoechoic thyroid nodule with smooth margins and no '
                         'calcifications. Two FNAs both show atypia of undetermined significance (Bethesda III). He '
                         'wants to avoid surgery if it is safe. A validated gene-expression classifier performed on '
                         'the aspirate returns benign. TSH is normal and no suspicious nodes are seen. What is the '
                         'most appropriate next step?',
                 'choices': ['Surveillance neck ultrasound in about 12 to 24 months',
                             'Diagnostic lobectomy, since molecular results cannot exclude cancer',
                             'Repeat FNA with a second molecular platform in 3 months',
                             'Levothyroxine suppression therapy to shrink the nodule over time'],
                 'answer': 0,
                 'explanation': 'Molecular testing is most useful when its result will change management. A validated '
                                'classifier with high negative predictive value, applied to a nodule with '
                                'low-suspicion ultrasound features, can lower malignancy risk to about the level of '
                                'benign cytology. ATA guidance supports active surveillance in that setting, as for a '
                                'benign nodule, with repeat ultrasound in about 12 to 24 months. Performance depends '
                                'on the assay and local cancer prevalence. Growth, new suspicious features, or patient '
                                'preference can still lead to repeat FNA or surgery.',
                 'why_wrong': ['Correct.',
                               'A benign classifier result in a low-suspicion nodule lowers cancer risk to roughly '
                               'that of benign cytology, so surgery is no longer needed.',
                               'Sending a second platform after a valid benign result adds cost and confusion without '
                               'changing management.',
                               'TSH suppression is not recommended for benign nodules because benefit is small and '
                               'cardiac and bone risks are real.'],
                 'board_pearl': 'Benign validated molecular result plus low-suspicion ultrasound: surveil like a '
                                'benign nodule.',
                 'curveball': 'How does a high-risk driver mutation differ from a benign-pattern classifier result in '
                              'counseling about the extent and timing of surgery?',
                 'curveball_answer': 'A high-risk alteration such as BRAF V600E, or TERT combined with another driver, '
                                     'carries a very high likelihood of cancer and may justify surgery promptly, with '
                                     'extent based on tumor size, nodes, and ATA risk. RAS-like alterations carry '
                                     'intermediate risk and often prove to be NIFTP, adenoma, or low-risk carcinoma, '
                                     'usually favoring diagnostic lobectomy. A benign classifier result supports '
                                     'surveillance.'},
 'v235_tps_indet_fnd': {'stem': 'A 38-year-old woman has a 1.8-cm solid, isoechoic, well-circumscribed left thyroid '
                                'nodule. FNA is reported as Bethesda IV, follicular neoplasm, with a cellular '
                                'microfollicular pattern and no nuclear features of papillary carcinoma. She asks why '
                                'the pathologist cannot simply say whether this is cancer. Which explanation is '
                                'correct?',
                        'choices': ['The sample lacked enough follicular cells, so the aspirate must be repeated first',
                                    'The nodule is malignant, but its histologic subtype cannot be determined on '
                                    'cytology',
                                    'The cells show nuclear features diagnostic of papillary carcinoma but lack '
                                    'colloid',
                                    'Follicular carcinoma is defined by capsular or vascular invasion, seen only on '
                                    'histology'],
                        'answer': 3,
                        'explanation': 'Indeterminate means cytology alone cannot reliably classify the nodule as '
                                       'benign or malignant. For Bethesda IV, the reason is biologic: follicular '
                                       'adenoma and follicular carcinoma have similar cells, and carcinoma is defined '
                                       'by invasion through the capsule or into vessels, which can be judged only on '
                                       'the resected nodule. The 2023 Bethesda system assigns an intermediate risk of '
                                       'malignancy to this category. Management integrates ultrasound pattern, size, '
                                       'molecular testing, and patient preference to choose surveillance or diagnostic '
                                       'lobectomy.',
                        'why_wrong': ['That describes a nondiagnostic Bethesda I specimen; a follicular neoplasm '
                                      'diagnosis requires an adequate, cellular aspirate.',
                                      'Bethesda IV is indeterminate, and most of these nodules prove benign; a '
                                      'malignant call corresponds to Bethesda VI.',
                                      'Nuclear features of papillary carcinoma would lead to a Bethesda V or VI call, '
                                      'and the report notes none.',
                                      'Correct.'],
                        'board_pearl': 'Follicular adenoma versus carcinoma depends on capsular or vascular invasion, '
                                       'which cytology cannot show.',
                        'curveball': 'Why does local malignancy prevalence change the positive and negative predictive '
                                     'value of a molecular test?',
                        'curveball_answer': 'Predictive values depend on pretest probability as well as sensitivity '
                                            'and specificity. Where cancer is common in indeterminate nodules, '
                                            'positive predictive value rises and negative predictive value falls, so a '
                                            'benign result is less reassuring. Where cancer is uncommon, the reverse '
                                            'holds. Published values come from validation cohorts and may not match a '
                                            "given institution's prevalence."},
 'v235_tps_indet_snr': {'stem': 'An 81-year-old man with ischemic cardiomyopathy (ejection fraction 25%) and '
                                'oxygen-dependent COPD has a 1.6-cm solid, isoechoic, smooth thyroid nodule found on '
                                'chest CT. FNA is Bethesda IV, and molecular testing detects an isolated NRAS '
                                'mutation, reported as intermediate-to-high risk. He has no compressive symptoms, and '
                                'nodes are normal. Which recommendation is most appropriate?',
                        'choices': ['Total thyroidectomy, because a positive molecular result confirms cancer',
                                    'Ultrasound surveillance after discussing his competing health risks',
                                    'Lobectomy within 4 weeks, because RAS-mutant nodules behave aggressively',
                                    'Radiofrequency ablation of the nodule as definitive treatment of the neoplasm'],
                        'answer': 1,
                        'explanation': 'Molecular results should update, not replace, the overall risk estimate. An '
                                       'isolated RAS mutation in a Bethesda IV nodule raises the probability of a '
                                       'follicular-pattern neoplasm, but many such lesions are adenomas, NIFTP, or '
                                       'minimally invasive, low-risk carcinomas that grow slowly. A 1.6-cm nodule with '
                                       'a low-suspicion ultrasound pattern in a man with severe heart and lung disease '
                                       'is unlikely to shorten his life, while surgery carries real risk. Shared '
                                       'decision-making favors ultrasound surveillance, with intervention reserved for '
                                       'growth or new suspicious features.',
                        'why_wrong': ['A RAS mutation raises the probability of a neoplasm but does not confirm '
                                      'cancer, and his operative risk is high.',
                                      'Correct.',
                                      'Isolated RAS alterations usually mark follicular adenoma, NIFTP, or low-risk '
                                      'carcinoma, which are indolent rather than aggressive.',
                                      'Ablation is not standard treatment for an indeterminate follicular neoplasm '
                                      'because it gives no histologic diagnosis and leaves possible carcinoma.'],
                        'board_pearl': 'A positive molecular result updates risk but does not mandate surgery; weigh '
                                       'competing comorbidity and tumor biology.',
                        'curveball': 'How would a convincingly benign molecular result change management when '
                                     'ultrasound remains highly suspicious?',
                        'curveball_answer': 'A highly suspicious ultrasound pattern raises pretest risk enough that a '
                                            'benign molecular call has lower negative predictive value. Discordance '
                                            'should not be resolved by trusting the test alone. Repeat FNA, review the '
                                            'cytology, or offer diagnostic lobectomy in a patient fit for surgery; in '
                                            'a frail patient, close surveillance with a low threshold to biopsy again '
                                            'is reasonable.'},
 'v235_tps_indet_app': {'stem': 'A 29-year-old woman has a 2.4-cm solid, mildly hypoechoic right thyroid nodule with '
                                'smooth margins (TI-RADS 4) and normal TSH. Repeat FNA again shows atypia of '
                                'undetermined significance. She is planning pregnancy next year and says she would '
                                'choose surveillance if her cancer risk were low, but surgery if it were not. Her '
                                'insurer covers testing. What is the best next step?',
                        'choices': ['Total thyroidectomy without any further testing, given her young age',
                                    'Core needle biopsy to definitively classify the nodule as benign',
                                    'Technetium thyroid scintigraphy to identify an autonomous nodule',
                                    'Validated molecular testing on the existing or a repeat aspirate'],
                        'answer': 3,
                        'explanation': 'Molecular testing helps most when the result will change what the patient '
                                       'does. She has a repeated Bethesda III result, an intermediate-suspicion '
                                       'ultrasound pattern, and has said that a low-risk result would lead her to '
                                       'choose surveillance. A validated assay, gene-expression classifier or mutation '
                                       'panel, can lower risk enough to justify surveillance or raise it enough to '
                                       'favor diagnostic lobectomy before pregnancy. The result should be interpreted '
                                       "together with the ultrasound and cytology, and with the assay's known "
                                       'predictive values.',
                        'why_wrong': ['Her nodule is indeterminate and most likely benign; total thyroidectomy without '
                                      'further risk stratification overtreats her.',
                                      'Core biopsy can help in some cases but cannot reliably exclude follicular '
                                      'carcinoma, which requires histology of the capsule.',
                                      'Scintigraphy helps only when TSH is low; with normal TSH it does not stratify '
                                      'malignancy risk.',
                                      'Correct.'],
                        'board_pearl': 'Order molecular testing for indeterminate cytology when the result will '
                                       'actually change the management decision.',
                        'curveball': 'How would a strongly suspicious ultrasound phenotype change your confidence in a '
                                     'reassuring molecular result?',
                        'curveball_answer': 'A TI-RADS 5 nodule with irregular margins, taller-than-wide shape, or '
                                            'microcalcifications has a high pretest risk, which lowers the negative '
                                            'predictive value of a benign molecular result. Many surgeons would then '
                                            'recommend diagnostic lobectomy despite the reassuring test, or at least '
                                            'repeat FNA, because the imaging is discordant with the molecular call.'},
 'v137_tps_07': {'stem': 'A 36-year-old woman has a 1.8-cm left thyroid nodule. FNA shows medullary thyroid carcinoma, '
                         'and serum calcitonin and CEA are elevated. Germline testing finds a RET C634R pathogenic '
                         'variant. She is normotensive and denies headaches or palpitations. Neck ultrasound shows '
                         'suspicious left central nodes. Total thyroidectomy is being scheduled. Which preoperative '
                         'evaluation is most critical to complete before thyroidectomy?',
                 'choices': ['Serum calcium and intact parathyroid hormone',
                             'Plasma free or urinary fractionated metanephrines',
                             'Serum gastrin, prolactin, and fasting glucose',
                             'Twenty-four-hour urine 5-hydroxyindoleacetic acid level'],
                 'answer': 1,
                 'explanation': 'RET C634 variants cause MEN2A, with high penetrance of medullary carcinoma, '
                                'pheochromocytoma, and primary hyperparathyroidism. An unrecognized pheochromocytoma '
                                'can cause a hypertensive crisis, arrhythmia, or death during induction and surgery, '
                                'and many are asymptomatic or normotensive. Biochemical screening with plasma free or '
                                'urinary fractionated metanephrines must precede thyroidectomy in any patient with MTC '
                                'until hereditary disease is excluded. If positive, the adrenal tumor is resected '
                                'first after alpha blockade. Calcium and PTH are also measured so that parathyroid '
                                'disease can be addressed at the neck operation.',
                 'why_wrong': ['Calcium and PTH are checked so hyperparathyroidism can be treated at the same '
                               'operation, but missing it is not an anesthetic emergency.',
                               'Correct.',
                               'Gastrin, prolactin, and glucose screen for MEN1 tumors, which RET variants do not '
                               'cause.',
                               'Urine 5-HIAA screens for carcinoid tumors and is not part of MEN2 evaluation.'],
                 'board_pearl': 'MEN2 or any new MTC: exclude pheochromocytoma with metanephrines before '
                                'thyroidectomy, even if normotensive.',
                 'curveball': 'How does RET genotype influence the timing of prophylactic thyroidectomy in her '
                              'affected children?',
                 'curveball_answer': 'ATA 2015 groups RET variants by risk. Highest risk, M918T or MEN2B, warrants '
                                     'thyroidectomy in the first year of life. High risk, codon 634 or A883F as here, '
                                     'warrants thyroidectomy at or before age 5, guided by calcitonin. Moderate-risk '
                                     'variants are followed with calcitonin and ultrasound from about age 5, with '
                                     'surgery when calcitonin rises.'},
 'v143_tps_03': {'stem': 'A 41-year-old man with MEN2A has a 2.5-cm medullary thyroid carcinoma with elevated '
                         'calcitonin. Preoperative plasma free normetanephrine is 6 times the upper limit, and CT '
                         'shows a 3.5-cm left adrenal mass. Blood pressure is 158/96 mm Hg. There is no distant '
                         'metastasis. Thyroidectomy with central neck dissection was planned for next week. What is '
                         'the most appropriate sequence of treatment?',
                 'choices': ['Thyroidectomy first, then adrenalectomy in 6 weeks',
                             'Same-day thyroidectomy and adrenalectomy, no blockade',
                             'Alpha blockade, then adrenalectomy, then thyroidectomy',
                             'Beta blockade alone, then proceed with thyroidectomy'],
                 'answer': 2,
                 'explanation': 'In MEN2, a biochemically confirmed pheochromocytoma is treated before thyroid '
                                'surgery. Preparation begins with alpha-adrenergic blockade, such as phenoxybenzamine '
                                'or doxazosin, for about 1 to 2 weeks with liberal salt and fluid to restore volume; '
                                'beta blockade is added only after alpha blockade for tachycardia. Laparoscopic '
                                'adrenalectomy, cortical-sparing in selected bilateral cases, then removes the '
                                'catecholamine source. Thyroidectomy and central neck dissection follow once he has '
                                'recovered. Medullary carcinoma rarely progresses meaningfully in that short interval.',
                 'why_wrong': ['Operating on the neck with an untreated pheochromocytoma exposes him to a '
                               'catecholamine crisis under anesthesia.',
                               'Any operation without preoperative alpha blockade risks severe intraoperative '
                               'hypertension and arrhythmia.',
                               'Correct.',
                               'Beta blockade without alpha blockade leaves alpha stimulation unopposed and can '
                               'precipitate hypertensive crisis.'],
                 'board_pearl': 'MEN2 with pheochromocytoma: alpha blockade, adrenalectomy first, then thyroidectomy; '
                                'never beta blockade alone.',
                 'curveball': 'How do RET genotype and age influence the timing of prophylactic thyroidectomy in an '
                              'asymptomatic carrier?',
                 'curveball_answer': 'Timing follows the ATA risk category. M918T carriers have thyroidectomy in the '
                                     'first year of life. Codon 634 and A883F carriers have thyroidectomy at or before '
                                     'age 5, earlier if calcitonin rises. Moderate-risk carriers start calcitonin and '
                                     'ultrasound screening around age 5 and have surgery when calcitonin rises, or in '
                                     'childhood if families prefer not to undergo prolonged surveillance.'},
 'v236_tps_men2_fnd': {'stem': 'A 45-year-old man had total thyroidectomy and central neck dissection for medullary '
                               'thyroid carcinoma. Postoperative germline testing reveals a RET C618S pathogenic '
                               'variant. He has no symptoms, and his father died suddenly during elective hernia '
                               'surgery at age 50. The patient asks which other tumors he needs to be screened for. '
                               'Which pair is most important?',
                       'choices': ['Pheochromocytoma and primary hyperparathyroidism',
                                   'Pancreatic neuroendocrine tumor and pituitary adenoma',
                                   'Renal cell carcinoma and CNS hemangioblastoma',
                                   'Paraganglioma and gastrointestinal stromal tumor'],
                       'answer': 0,
                       'explanation': 'Germline RET gain-of-function variants cause MEN2. MEN2A includes medullary '
                                      'carcinoma, pheochromocytoma, and primary hyperparathyroidism, and MEN2B adds '
                                      'mucosal neuromas and a marfanoid habitus but rarely hyperparathyroidism. His '
                                      "father's sudden death during surgery is a classic clue to an undiagnosed "
                                      'pheochromocytoma. Codon 618 is a moderate-risk variant in the ATA scheme, so '
                                      'annual screening with metanephrines and calcium begins by age 16. First-degree '
                                      'relatives should be offered cascade genetic testing.',
                       'why_wrong': ['Correct.',
                                     'Pancreatic islet and pituitary tumors define MEN1, caused by menin mutations, '
                                     'not RET.',
                                     'Renal cell carcinoma and hemangioblastomas are features of von Hippel-Lindau '
                                     'disease, caused by VHL mutations.',
                                     'Paraganglioma with GIST suggests succinate dehydrogenase deficiency, as in '
                                     'Carney-Stratakis syndrome, not RET.'],
                       'board_pearl': 'RET equals MEN2: screen for pheochromocytoma and, in MEN2A, '
                                      'hyperparathyroidism; offer cascade testing to relatives.',
                       'curveball': 'Why must pheochromocytoma be excluded before any elective thyroid surgery in a '
                                    'patient with MEN2?',
                       'curveball_answer': 'Anesthetic induction, intubation, and surgical manipulation can trigger '
                                           'massive catecholamine release from an unrecognized pheochromocytoma, '
                                           'causing hypertensive crisis, arrhythmia, stroke, or death. Many tumors are '
                                           'small, normotensive, or asymptomatic, so symptoms cannot be relied on. '
                                           'Metanephrine screening identifies the tumor so it can be resected first '
                                           'after alpha blockade.'},
 'v236_tps_men2_app': {'stem': 'A 33-year-old woman with known MEN2A is admitted the evening before total '
                               'thyroidectomy for a 1.5-cm medullary carcinoma. At the preoperative check she reports '
                               '2 months of episodic pounding headaches, palpitations, and drenching sweats. Blood '
                               'pressure is 172/104 mm Hg. Her chart has no metanephrine results, and the outside '
                               "surgeon's note says 'proceed.' What is the best next step?",
                       'choices': ['Postpone surgery and obtain plasma free metanephrines',
                                   'Proceed with thyroidectomy using arterial line monitoring',
                                   'Start propranolol tonight and proceed with surgery tomorrow',
                                   'Proceed with thyroidectomy and obtain adrenal CT afterward'],
                       'answer': 0,
                       'explanation': 'Paroxysmal headache, palpitations, sweating, and hypertension in a patient with '
                                      'MEN2A strongly suggest pheochromocytoma. Elective thyroidectomy is not urgent '
                                      'compared with the risk of a catecholamine crisis under anesthesia. Surgery '
                                      'should be postponed and plasma free or urinary fractionated metanephrines '
                                      'obtained, followed by adrenal imaging if positive. A confirmed tumor is treated '
                                      'with alpha blockade, volume expansion, and adrenalectomy before thyroidectomy. '
                                      'Medullary carcinoma of this size will not be harmed by a delay of several '
                                      'weeks.',
                       'why_wrong': ['Correct.',
                                     'Monitoring does not prevent a catecholamine surge; an undiagnosed '
                                     'pheochromocytoma should be removed before elective thyroid surgery.',
                                     'Beta blockade without alpha blockade leaves alpha stimulation unopposed and can '
                                     'provoke severe hypertension.',
                                     'Imaging after the neck operation is too late; the dangerous event is the '
                                     'anesthetic itself.'],
                       'board_pearl': 'Spells and hypertension in MEN2 before thyroidectomy: cancel, check '
                                      'metanephrines, treat pheochromocytoma first.',
                       'curveball': 'How does a RET genotype influence screening age and prophylactic thyroidectomy '
                                    'timing in an unaffected carrier?',
                       'curveball_answer': 'Highest-risk M918T carriers have thyroidectomy within the first year of '
                                           'life and begin pheochromocytoma screening at age 11. High-risk codon 634 '
                                           'or A883F carriers have thyroidectomy at or before age 5 and also screen '
                                           'from age 11. Moderate-risk carriers start calcitonin screening around age '
                                           '5, operate when calcitonin rises, and begin pheochromocytoma screening at '
                                           'age 16.'},
 'v236_tps_men2_snr': {'stem': 'A 3-year-old girl is found on cascade testing to carry the RET C634Y variant that '
                               'caused MEN2A in her mother. She is well. Serum calcitonin is normal for age, and neck '
                               'ultrasound shows a normal thyroid with no enlarged nodes. Her parents ask when thyroid '
                               'surgery should be done. Which plan is most appropriate?',
                       'choices': ['Total thyroidectomy now, as soon as it can be scheduled',
                                   'Defer surgery until calcitonin rises, most likely in adolescence',
                                   'Total thyroidectomy at or before age 5, timed by calcitonin',
                                   'Defer surgery until adulthood with yearly neck ultrasound'],
                       'answer': 2,
                       'explanation': 'ATA 2015 guidance stratifies RET variants. Codon 634 and A883F are high risk, '
                                      'with medullary carcinoma often developing in early childhood, so total '
                                      'thyroidectomy is recommended at or before age 5, with timing guided by '
                                      'calcitonin. With normal calcitonin and a normal ultrasound, central neck '
                                      'dissection is not needed; it is added if calcitonin exceeds about 40 pg/mL or '
                                      'nodes are suspicious. Experienced pediatric thyroid surgeons should operate to '
                                      'minimize hypoparathyroidism and nerve injury.',
                       'why_wrong': ['Immediate surgery as early as possible is the plan for highest-risk M918T '
                                     'carriers with MEN2B, not codon 634.',
                                     'Waiting for calcitonin to rise into adolescence is the moderate-risk approach '
                                     'and risks nodal metastasis in a high-risk carrier.',
                                     'Correct.',
                                     'Delaying until adulthood would allow medullary carcinoma and nodal spread in '
                                     'most codon 634 carriers.'],
                       'board_pearl': 'RET codon 634: total thyroidectomy at or before age 5; M918T in infancy; '
                                      'moderate-risk by calcitonin.',
                       'curveball': 'How would an elevated calcitonin or suspicious cervical nodes change the '
                                    'operation from prophylactic to therapeutic?',
                       'curveball_answer': 'An elevated calcitonin, particularly above about 40 pg/mL, or '
                                           'ultrasound-suspicious nodes indicates likely established carcinoma. The '
                                           'operation becomes therapeutic: total thyroidectomy with central neck '
                                           'dissection, and lateral dissection for clinically involved lateral nodes. '
                                           'Staging imaging is considered at higher calcitonin levels, and surgery '
                                           'should not be deferred further.'},
 'v137_tps_08': {'stem': 'A 52-year-old man has fatigue, polyuria, bone pain, and nephrolithiasis. Calcium is 14.8 '
                         'mg/dL and intact PTH is 12 times the upper limit. A firm, fixed 3.8-cm mass is palpable low '
                         'in the right neck. Laryngoscopy shows right vocal fold paralysis. Ultrasound shows a '
                         'lobulated hypoechoic mass behind the right thyroid lobe with loss of the tissue plane '
                         'between them. Which operation should be planned?',
                 'choices': ['Excision of the mass along its capsule, preserving the thyroid lobe',
                             'En bloc resection of the mass with the ipsilateral thyroid lobe',
                             'Focused parathyroidectomy with frozen section',
                             'Subtotal parathyroidectomy with thymectomy for presumed hyperplasia'],
                 'answer': 1,
                 'explanation': 'Very high calcium, PTH more than 10 times normal, a palpable firm mass, recurrent '
                                'laryngeal nerve paralysis, and loss of the tissue plane with the thyroid strongly '
                                'suggest parathyroid carcinoma. The best chance of cure is the first operation: en '
                                'bloc resection of the tumor with the ipsilateral thyroid lobe and any adherent strap '
                                'muscle, central nodal tissue, or involved structures, without breaching the capsule. '
                                'Local recurrence after capsular rupture or piecemeal removal is common and hard to '
                                'salvage. Preoperative calcium should be controlled with hydration, bisphosphonates or '
                                'denosumab, and cinacalcet.',
                 'why_wrong': ['Dissecting along the capsule of an invasive tumor risks rupture and leaves microscopic '
                               'disease, the main driver of local recurrence.',
                               'Correct.',
                               'Frozen section cannot reliably distinguish carcinoma from adenoma, and a focused '
                               'excision ignores the invasion seen on imaging.',
                               'A single invasive mass with marked hypercalcemia indicates carcinoma, not multigland '
                               'hyperplasia.'],
                 'board_pearl': 'Suspected parathyroid carcinoma: plan en bloc resection with the ipsilateral thyroid '
                                'lobe at the first operation.',
                 'curveball': 'What biochemical problem often dominates the care of recurrent or metastatic '
                              'parathyroid carcinoma?',
                 'curveball_answer': 'Refractory PTH-driven hypercalcemia, rather than tumor bulk, causes most of the '
                                     'morbidity and deaths. It is managed with hydration, IV bisphosphonates or '
                                     'denosumab, and cinacalcet, with resection or ablation of metastases whenever '
                                     'feasible to reduce the PTH-secreting mass. Chemotherapy and radiation have '
                                     'limited effect.'},
 'v143_tps_04': {'stem': 'A 58-year-old woman has calcium 15.2 mg/dL, PTH 14 times normal, and a hard 3.5-cm mass in '
                         'the left tracheoesophageal groove. She has been hoarse for 3 months, and laryngoscopy shows '
                         'left vocal fold paralysis with good compensation by the right fold. CT shows the mass '
                         "encasing the left recurrent laryngeal nerve's expected course. The right vocal fold moves "
                         'normally. How should the left nerve be managed at en bloc resection?',
                 'choices': ['Dissect the nerve free and shave the tumor off its surface',
                             'Leave tumor on the nerve and plan adjuvant neck radiation',
                             'Debulk the tumor around the nerve and control calcium medically',
                             'Resect the encased, already paralyzed nerve with the specimen'],
                 'answer': 3,
                 'explanation': 'Preoperative vocal fold paralysis in a patient with suspected parathyroid carcinoma '
                                'implies nerve invasion and strengthens the diagnosis. Because the nerve is already '
                                'nonfunctional and the contralateral fold moves normally, resecting the encased nerve '
                                'with the specimen achieves an en bloc margin without losing function. Complete '
                                'initial resection is the main determinant of local control, and recurrence after '
                                'capsule violation is hard to treat. Immediate reinnervation, such as ansa cervicalis '
                                'to recurrent laryngeal nerve, or later medialization can improve voice.',
                 'why_wrong': ['Shaving tumor off a nerve that is already paralyzed risks capsular rupture and '
                               'positive margins without any functional benefit.',
                               'Deliberately leaving gross tumor sacrifices the best chance of cure, and radiation '
                               'does not reliably control residual disease.',
                               'Debulking violates the tumor and leaves residual disease that will drive recurrent '
                               'hypercalcemia.',
                               'Correct.'],
                 'board_pearl': 'Parathyroid carcinoma encasing an already paralyzed RLN: take the nerve en bloc; '
                                'consider reinnervation for voice.',
                 'curveball': 'How would normal preoperative vocal fold function change the decision about a nerve '
                              'that is adherent to the tumor?',
                 'curveball_answer': 'A functioning nerve is preserved whenever it can be separated from the tumor '
                                     'without leaving gross disease, because sacrifice causes new paralysis and '
                                     'aspiration risk. If gross tumor truly invades a functioning nerve, sacrifice for '
                                     'complete resection may still be justified after counseling, but only if the '
                                     'contralateral fold works. Immediate reinnervation should then be planned.'},
 'v236_tps_ptca_fnd': {'stem': 'A 47-year-old woman has 6 months of bone pain, fatigue, and recurrent kidney stones. '
                               'Calcium is 14.2 mg/dL and intact PTH is 680 pg/mL (normal 15 to 65). A firm 3.4-cm '
                               'mass is palpable low in the left neck, and her voice has become breathy. Laryngoscopy '
                               'shows left vocal fold paralysis. Radiographs show subperiosteal resorption of the '
                               'phalanges. What is the most likely diagnosis?',
                       'choices': ['Giant parathyroid adenoma',
                                   'Parathyroid carcinoma',
                                   'Multigland parathyroid hyperplasia',
                                   'Medullary thyroid carcinoma'],
                       'answer': 1,
                       'explanation': 'Parathyroid carcinoma is rare, but its presentation is distinctive. Calcium '
                                      'above about 14 mg/dL, PTH more than several-fold elevated, concurrent bone and '
                                      'kidney disease, a palpable neck mass, and recurrent laryngeal nerve paralysis '
                                      'from local invasion all point toward carcinoma. Benign adenomas usually produce '
                                      'milder hypercalcemia, are rarely palpable, and do not invade nerves. '
                                      'Recognizing the pattern before surgery matters because the first operation '
                                      'should be an en bloc resection rather than a simple gland excision.',
                       'why_wrong': ['Large adenomas can cause high calcium but rarely cause a palpable hard mass with '
                                     'recurrent laryngeal nerve invasion.',
                                     'Correct.',
                                     'Hyperplasia produces milder hypercalcemia with several small glands, not a '
                                     'single invasive palpable mass.',
                                     'Medullary carcinoma secretes calcitonin, not PTH, and does not cause '
                                     'PTH-dependent hypercalcemia with bone resorption.'],
                       'board_pearl': 'Calcium above 14, PTH markedly elevated, palpable mass, RLN palsy: think '
                                      'parathyroid carcinoma.',
                       'curveball': 'Why should suspected parathyroid carcinoma like hers generally not undergo '
                                    'routine preoperative needle biopsy?',
                       'curveball_answer': 'FNA cannot distinguish parathyroid carcinoma from adenoma, because the '
                                           'diagnosis depends on invasion rather than cytologic features. Needle '
                                           'passage can also seed tumor along the tract and cause local recurrence. '
                                           'The diagnosis is made by the clinical picture and confirmed on the en bloc '
                                           'resection specimen.'},
 'v236_tps_ptca_app': {'stem': 'A 61-year-old man with calcium 12.9 mg/dL and a sestamibi-concordant right inferior '
                               'gland undergoes planned focused parathyroidectomy. At operation the gland is 3 cm, '
                               'gray-white, and hard, and it is densely adherent to the lower pole of the right '
                               'thyroid lobe and the overlying sternothyroid muscle. The recurrent laryngeal nerve is '
                               'separate and stimulates normally. What is the best intraoperative decision?',
                       'choices': ['Proceed with excision of the gland after carefully opening the capsule plane',
                                   'Close and obtain ultrasound-guided FNA to confirm malignancy before resection',
                                   'Remove the gland piecemeal to protect the nearby recurrent laryngeal nerve',
                                   'Convert to en bloc resection with the right thyroid lobe and adherent strap'],
                       'answer': 3,
                       'explanation': 'Hard consistency, gray-white color, large size, and adherence to adjacent '
                                      'thyroid and strap muscle are intraoperative signs of parathyroid carcinoma, '
                                      'even when the preoperative picture looked like an adenoma. The best chance of '
                                      'durable control is an en bloc resection at this first operation, taking the '
                                      'ipsilateral thyroid lobe, adherent strap muscle, and adjacent central tissue '
                                      'without breaching the tumor. Because the recurrent nerve is uninvolved and '
                                      'functioning, it is preserved. Final diagnosis rests on histologic invasion.',
                       'why_wrong': ['Entering the capsule plane of a possible carcinoma risks rupture and '
                                     'implantation, the main cause of local recurrence.',
                                     'Delay adds a second operation in scarred tissue, and FNA cannot diagnose '
                                     'carcinoma and risks tract seeding.',
                                     'Piecemeal removal spills tumor cells; the nerve is uninvolved and can be '
                                     'preserved during an en bloc resection.',
                                     'Correct.'],
                       'board_pearl': 'Unexpected hard, adherent parathyroid tumor at surgery: convert to en bloc '
                                      'resection; do not shell it out.',
                       'curveball': 'How should gross recurrent laryngeal nerve invasion be balanced against '
                                    'preoperative vocal fold function and oncologic control?',
                       'curveball_answer': 'If the nerve already does not work, it is resected with the specimen. If '
                                           'it works and the tumor can be peeled off without leaving gross disease, '
                                           'preserve it. If gross tumor invades a functioning nerve, sacrifice may be '
                                           'justified for complete resection only when the contralateral fold is '
                                           'normal, with immediate reinnervation and full preoperative counseling.'},
 'v236_tps_ptca_snr': {'stem': 'A 56-year-old woman had en bloc resection of parathyroid carcinoma 4 years ago with '
                               'normal calcium afterward. She now has calcium 13.2 mg/dL with elevated PTH. Ultrasound '
                               'and 4D-CT show a 1.8-cm nodule in the left paratracheal region of the old operative '
                               'bed, and PET/CT shows no distant disease. She is otherwise well and has normal vocal '
                               'folds. What is the best management?',
                       'choices': ['Medical control of calcium, then reoperative resection of the recurrence',
                                   'Long-term cinacalcet alone, avoiding reoperation in the scarred neck',
                                   'External beam radiation to the neck as the primary local therapy',
                                   'Cytotoxic chemotherapy, given the high risk of later metastasis'],
                       'answer': 0,
                       'explanation': 'Recurrent parathyroid carcinoma usually harms patients through PTH-driven '
                                      'hypercalcemia. Management has two parallel goals: control calcium with '
                                      'hydration, bisphosphonates or denosumab, and cinacalcet, and remove the '
                                      'PTH-secreting tissue when it can be resected. A localized recurrence without '
                                      'distant disease should be resected, ideally en bloc, by an experienced surgeon '
                                      'after concordant localization. Repeat resections can provide prolonged '
                                      'biochemical control even when cure is unlikely. Laryngoscopy, careful operative '
                                      'planning, and postoperative calcium monitoring for hungry bone are needed.',
                       'why_wrong': ['Correct.',
                                     'Medical therapy controls calcium only temporarily and does nothing for a '
                                     'resectable recurrence that can be removed.',
                                     'Radiation has limited effectiveness for parathyroid carcinoma and is not a '
                                     'substitute for resecting localized disease.',
                                     'Chemotherapy has poor response rates in parathyroid carcinoma and is not '
                                     'first-line for resectable recurrence.'],
                       'board_pearl': 'Resectable recurrent parathyroid carcinoma: control calcium, then resect; '
                                      'surgery gives the best biochemical control.',
                       'curveball': 'Which medical therapies can bridge severe hypercalcemia while definitive disease '
                                    'control is planned?',
                       'curveball_answer': 'Start aggressive IV saline to correct volume depletion, then give an IV '
                                           'bisphosphonate such as zoledronic acid or, with renal impairment, '
                                           'subcutaneous denosumab. Add cinacalcet to lower PTH secretion through the '
                                           'calcium-sensing receptor. Calcitonin gives a rapid but short-lived effect, '
                                           'and dialysis is a last resort for life-threatening hypercalcemia.'},
 'v137_tps_09': {'stem': 'A 34-year-old woman has a 2-cm painless, mobile mass in the superficial lobe of the left '
                         'parotid that has grown slowly over 2 years. Facial nerve function is normal. FNA shows bland '
                         'epithelial and myoepithelial cells in a chondromyxoid stroma. A general surgeon offers to '
                         'shell out the mass through a small incision. What is the main reason enucleation is avoided?',
                 'choices': ['Malignant transformation is common within a year of a shelled-out excision',
                             'Enucleation requires sacrifice of the facial nerve branches over the tumor',
                             'Its incomplete capsule and pseudopodia leave residual tumor cells behind',
                             'Handling the capsule seeds the intraparotid nodes with metastatic tumor'],
                 'answer': 2,
                 'explanation': 'Pleomorphic adenoma has an incomplete, variably thick capsule with microscopic '
                                'finger-like pseudopodia and satellite nodules extending into the surrounding gland. '
                                'Enucleation along the capsule leaves these extensions behind and often ruptures the '
                                'tumor, producing multinodular recurrence that is much harder to cure and that places '
                                'the facial nerve at greater risk at revision. Resection with a cuff of normal '
                                'parotid, by superficial or partial parotidectomy with facial nerve dissection or by '
                                'careful extracapsular dissection for small mobile tumors, keeps recurrence low.',
                 'why_wrong': ['Malignant transformation to carcinoma ex pleomorphic adenoma occurs over many years '
                               'and is not the reason enucleation fails.',
                               'Enucleation does not require nerve sacrifice; the concern is that it leaves tumor '
                               'behind, not that it injures the nerve.',
                               'Correct.',
                               'Pleomorphic adenoma is benign and does not metastasize to nodes; spillage causes local '
                               'multinodular recurrence instead.'],
                 'board_pearl': 'Pleomorphic adenoma has pseudopodia; remove it with a cuff of normal gland, never by '
                                'enucleation.',
                 'curveball': 'How does a deep-lobe tumor alter the surgical approach and nerve dissection?',
                 'curveball_answer': 'A deep-lobe tumor lies medial to the facial nerve plane, so the nerve is '
                                     'identified at the main trunk, its branches are dissected and gently mobilized, '
                                     'and the tumor is delivered beneath or between them. Large tumors extending into '
                                     'the parapharyngeal space may need a transcervical-transparotid approach, '
                                     'sometimes with mandibulotomy, while keeping the capsule intact.'},
 'v146_tps_05': {'stem': 'A 45-year-old man undergoes superficial parotidectomy with facial nerve dissection for a '
                         '3-cm pleomorphic adenoma. While freeing the tumor from the buccal branch, the thin capsule '
                         'tears, and a small amount of gelatinous tumor spills into the wound. The nerve is intact and '
                         'stimulates normally. Which intraoperative management is most appropriate?',
                 'choices': ['Convert to total parotidectomy with sacrifice of the buccal and zygomatic branches',
                             'Stop the resection and refer him for primary radiation therapy to the parotid bed',
                             'Remove all visible spilled tumor, irrigate copiously, and complete the resection',
                             'Complete the resection without irrigation, since the tumor is benign and inert'],
                 'answer': 2,
                 'explanation': 'Capsular rupture and tumor spillage are the main avoidable causes of pleomorphic '
                                'adenoma recurrence, because spilled cells implant and grow into many small nodules. '
                                'When rupture occurs, the surgeon removes all visible tumor fragments, irrigates the '
                                'field thoroughly, completes the resection with a margin of normal gland, and '
                                'preserves the functioning nerve. The event is recorded in the operative note, and the '
                                'patient is counseled and followed long term, often with MRI. Adjuvant radiation after '
                                'a single limited spill is debated and not routine.',
                 'why_wrong': ['Spillage does not justify sacrificing a functioning facial nerve; removing the '
                               'remaining tumor and irrigating treat the spill.',
                               'Stopping leaves a known benign tumor in place; surgery remains the primary treatment, '
                               'and radiation is not first-line.',
                               'Correct.',
                               'Spilled pleomorphic adenoma cells implant and grow, so leaving them causes '
                               'multinodular recurrence.'],
                 'board_pearl': 'Pleomorphic adenoma spill: remove fragments, irrigate, finish the resection, preserve '
                                'the nerve, document, and follow long term.',
                 'curveball': 'How does Warthin tumor differ from pleomorphic adenoma in multiplicity and in the '
                              'option of observation?',
                 'curveball_answer': 'Warthin tumor is often multifocal or bilateral, is strongly linked to smoking, '
                                     'and almost never becomes malignant. A secure diagnosis allows observation in '
                                     'older or high-risk patients. Pleomorphic adenoma is usually solitary but keeps '
                                     'growing, recurs after spillage, and carries a small, rising risk of carcinoma ex '
                                     'pleomorphic adenoma, so removal is usually recommended.'},
 'v236_tps_benignsal_fnd': {'stem': 'A 31-year-old woman has a painless, firm, mobile 2.5-cm mass in the tail of the '
                                    'right parotid that has slowly enlarged over 3 years. Facial nerve function is '
                                    'normal, and there is no adenopathy. She has never smoked. MRI shows a '
                                    'well-circumscribed, lobulated, markedly T2-hyperintense mass. FNA shows bland '
                                    'spindle and plasmacytoid cells in a fibrillary chondromyxoid stroma. What is the '
                                    'most likely diagnosis?',
                            'choices': ['Pleomorphic adenoma',
                                        'Warthin tumor',
                                        'Adenoid cystic carcinoma',
                                        'Low-grade mucoepidermoid carcinoma'],
                            'answer': 0,
                            'explanation': 'Pleomorphic adenoma is the most common salivary gland tumor and typically '
                                           'affects middle-aged women in the superficial parotid. It is a mixed tumor: '
                                           'epithelial and myoepithelial cells, the latter often spindle or '
                                           'plasmacytoid, within a chondromyxoid stroma, which gives a very bright T2 '
                                           'signal and lobulated margins on MRI. It grows slowly but continues to '
                                           'enlarge, recurs after capsular violation because of pseudopodia, and '
                                           'carries a small risk of carcinoma ex pleomorphic adenoma with long '
                                           'duration. Warthin tumor differs in age, smoking history, and cytology.',
                            'why_wrong': ['Correct.',
                                          'Warthin tumor occurs mostly in older smokers and shows oncocytic cells with '
                                          'a lymphoid background, not chondromyxoid stroma.',
                                          'Adenoid cystic carcinoma shows basaloid cells around hyaline globules and '
                                          'often causes pain or nerve symptoms.',
                                          'Mucoepidermoid carcinoma shows mucous, intermediate, and epidermoid cells, '
                                          'and its MRI signal is often heterogeneous.'],
                            'board_pearl': 'Lobulated, bright-T2 parotid mass with chondromyxoid stroma in a young '
                                           'woman: pleomorphic adenoma.',
                            'curveball': 'What clinical change in a long-standing pleomorphic adenoma should raise '
                                         'concern for malignant transformation?',
                            'curveball_answer': 'Sudden rapid growth after years of stability, new pain, facial nerve '
                                                'weakness, skin fixation, or new cervical adenopathy suggest carcinoma '
                                                'ex pleomorphic adenoma. The risk rises with how long the tumor has '
                                                'been present and with recurrence. Evaluate with MRI and FNA or core '
                                                'biopsy, and treat as a malignancy with parotidectomy and neck '
                                                'management as indicated.'},
 'v236_tps_benignsal_app': {'stem': 'A 26-year-old man has a 2.8-cm, firm, mobile mass in the superficial lobe of the '
                                    'right parotid, anterior to the earlobe. FNA confirms pleomorphic adenoma. Facial '
                                    'nerve function is normal, and MRI shows the tumor lateral to the retromandibular '
                                    'vein without deep-lobe extension. He asks whether he can avoid surgery because '
                                    'the tumor is benign. Which recommendation is most appropriate?',
                            'choices': ['Observation with yearly MRI, since the tumor is histologically benign',
                                        'Enucleation of the tumor through a small preauricular skin incision',
                                        'Total parotidectomy including the deep lobe',
                                        'Superficial or partial parotidectomy with facial nerve dissection'],
                            'answer': 3,
                            'explanation': 'A young, healthy patient with pleomorphic adenoma faces decades of tumor '
                                           'growth and a cumulative risk of carcinoma ex pleomorphic adenoma, so '
                                           'excision is recommended. The goal is complete removal with a cuff of '
                                           'normal parotid while preserving the facial nerve. For a superficial-lobe '
                                           'tumor, superficial or partial superficial parotidectomy with '
                                           'identification of the main trunk and dissection of the relevant branches '
                                           'achieves this. Extracapsular dissection is an alternative in experienced '
                                           'hands for small, mobile, superficial tumors. Enucleation and unnecessary '
                                           'deep-lobe resection are avoided.',
                            'why_wrong': ['Pleomorphic adenomas keep growing and carry a small, cumulative risk of '
                                          'malignant change, so observation is not favored in a young patient.',
                                          'Enucleation leaves pseudopodia behind and often ruptures the capsule, '
                                          'causing multinodular recurrence.',
                                          'The deep lobe is uninvolved, so removing it adds facial nerve risk and '
                                          'contour defect without benefit.',
                                          'Correct.'],
                            'board_pearl': 'Superficial-lobe pleomorphic adenoma: superficial or partial parotidectomy '
                                           'with nerve dissection, keeping a normal-tissue cuff.',
                            'curveball': 'How does a deep-lobe location change exposure and facial nerve planning?',
                            'curveball_answer': 'The tumor lies medial to the nerve, so the main trunk and all '
                                                'branches over the tumor must be identified and mobilized before the '
                                                'mass is delivered between or beneath them, increasing the risk of '
                                                'temporary weakness. Tumors extending through the stylomandibular '
                                                'tunnel into the parapharyngeal space may need a transcervical '
                                                'approach to keep the capsule intact.'},
 'v236_tps_benignsal_snr': {'stem': 'A 76-year-old man with a 50-pack-year smoking history, heart failure, and atrial '
                                    'fibrillation on apixaban has a soft, painless 2.2-cm mass in the right parotid '
                                    'tail. It has been unchanged on ultrasound for 2 years. FNA shows oncocytic '
                                    'epithelial cells in a lymphoid background. Facial nerve function is normal, and '
                                    'imaging shows no adenopathy. He would prefer to avoid surgery. What is the best '
                                    'management?',
                            'choices': ['Superficial parotidectomy now, since malignant change is common',
                                        'Observation with periodic clinical examination and ultrasound',
                                        'Total parotidectomy to remove synchronous occult tumors in the gland',
                                        'Repeat FNA every 6 months to watch for transformation to carcinoma'],
                            'answer': 1,
                            'explanation': 'Warthin tumor is a benign, often multifocal or bilateral parotid tail '
                                           'tumor strongly associated with smoking, and it almost never becomes '
                                           'malignant. When cytology, imaging, and clinical behavior are concordant, '
                                           'observation is reasonable, especially in older patients with significant '
                                           'comorbidity or anticoagulation. Surgery is offered for growth, symptoms '
                                           'such as pain or infection, diagnostic uncertainty, or patient preference. '
                                           'This differs from pleomorphic adenoma, which keeps growing and carries a '
                                           'cumulative malignant risk. Smoking cessation should also be advised.',
                            'why_wrong': ['Malignant transformation of Warthin tumor is exceedingly rare, so surgery '
                                          'is not required to prevent it in this high-risk patient.',
                                          'Correct.',
                                          'Removing the entire gland for possible additional Warthin foci adds facial '
                                          'nerve risk without meaningful benefit.',
                                          'Serial FNAs add discomfort without benefit; clinical and imaging follow-up '
                                          'detect growth or worrisome change.'],
                            'board_pearl': 'Concordant Warthin tumor in an older, high-risk patient: observation is '
                                           'reasonable; operate for growth, symptoms, or doubt.',
                            'curveball': 'What discordant imaging, cytology, or growth pattern would make observation '
                                         'of this tumor unsafe?',
                            'curveball_answer': 'Rapid growth, pain, facial weakness, fixation, firm consistency, or '
                                                'new adenopathy argue against Warthin tumor. So do ill-defined or '
                                                'infiltrative margins on imaging, or cytology with atypia, scant '
                                                'lymphoid tissue, or squamous metaplasia that could mimic '
                                                'mucoepidermoid or squamous carcinoma. Any of these warrants core '
                                                'biopsy or parotidectomy rather than continued observation.'},
 'v137_tps_10': {'stem': 'A 22-year-old woman has a painless swelling under the left jaw for 5 months and a smaller '
                         'bluish swelling in the left floor of mouth. Ultrasound-guided aspiration twice yielded '
                         'thick, clear, viscous fluid, and the neck swelling recurred within weeks each time. MRI '
                         'shows a thin-walled cystic lesion extending from the left sublingual space through a '
                         'mylohyoid gap into the submandibular space. What management best minimizes recurrence?',
                 'choices': ['Transcervical excision of the cervical pseudocyst alone, leaving the glands',
                             'Ipsilateral submandibular gland excision through a transcervical incision',
                             'Further ultrasound-guided aspirations of the neck collection as needed',
                             'Excision of the ipsilateral sublingual gland with evacuation of the ranula'],
                 'answer': 3,
                 'explanation': 'A ranula is a mucus extravasation pseudocyst, usually from the sublingual gland, '
                                'which secretes continuously even between meals. A plunging ranula reaches the '
                                'submandibular space through a mylohyoid dehiscence or around its posterior edge. '
                                'Because the sublingual gland keeps leaking, aspiration, marsupialization, or excision '
                                'of the cervical collection alone has a high recurrence rate. Excising the ipsilateral '
                                'sublingual gland, usually transorally, with evacuation of the pseudocyst removes the '
                                'source and gives the lowest recurrence. The pseudocyst wall does not need to be '
                                'removed.',
                 'why_wrong': ['Removing only the cervical collection leaves the leaking sublingual gland, so mucus '
                               'reaccumulates and the ranula recurs.',
                               'The submandibular gland is not the source; removing it leaves the sublingual gland '
                               'leaking and adds marginal mandibular nerve risk.',
                               'Aspiration removes mucus but not its source, as her two rapid recurrences show.',
                               'Correct.'],
                 'board_pearl': 'Ranula recurs unless the sublingual gland is removed; the pseudocyst wall itself does '
                                'not need excision.',
                 'curveball': 'Which lingual nerve and submandibular duct relationships matter during sublingual gland '
                              'excision?',
                 'curveball_answer': 'Wharton duct runs along the medial surface of the sublingual gland, and the '
                                     'lingual nerve crosses beneath the duct from lateral to medial in the posterior '
                                     "floor of mouth. Identify and protect both before dividing the gland's deep "
                                     'attachments. Cannulating the duct helps protect it, and the duct may need '
                                     'rerouting if injured.'},
 'v146_tps_08': {'stem': 'A 9-year-old boy had transcervical excision of a submandibular-space cyst 8 months ago; '
                         'pathology showed mucin and histiocytes surrounded by granulation tissue without an '
                         'epithelial lining. The submandibular and sublingual glands were left in place. The neck '
                         'swelling has returned, and a small bluish bulge is now visible in the right floor of mouth. '
                         'What best explains the recurrence?',
                 'choices': ['The submandibular gland was left in place',
                             'The leaking sublingual gland was left in place',
                             "Part of the cyst's epithelial lining was retained",
                             'A branchial cleft tract was not identified at surgery'],
                 'answer': 1,
                 'explanation': 'Ranula is a mucus extravasation pseudocyst: mucin leaks from a disrupted sublingual '
                                'gland and is walled off by granulation and fibrous tissue, without a true epithelial '
                                'lining. The sublingual gland secretes continuously, so any operation that removes the '
                                'collection but leaves the gland lets mucus reaccumulate. That is why excision of a '
                                "plunging ranula's cervical component alone has a high recurrence rate. Definitive "
                                'management is excision of the ipsilateral sublingual gland, usually transorally, with '
                                'evacuation of the mucus, in children as in adults.',
                 'why_wrong': ['Ranulas arise mainly from the sublingual gland; the submandibular gland is rarely the '
                               'source.',
                               'Correct.',
                               'The pathology describes a pseudocyst with no epithelial lining, so there is no lining '
                               'to leave behind.',
                               'The mucin-filled pseudocyst and floor-of-mouth component indicate a ranula, not a '
                               'branchial cleft anomaly.'],
                 'board_pearl': 'Ranula has no epithelial lining; recurrence means the sublingual gland source '
                                'remains.',
                 'curveball': 'What nerves and ducts are at risk during transoral sublingual gland excision in this '
                              'child?',
                 'curveball_answer': 'The lingual nerve, which crosses beneath Wharton duct in the posterior floor of '
                                     'mouth, and Wharton duct itself, which lies along the medial gland surface, are '
                                     'most at risk. Injury causes tongue numbness and taste change or submandibular '
                                     'obstruction. The hypoglossal nerve lies deeper on the hyoglossus and is less '
                                     'often exposed.'},
 'v237_tps_ranula_fnd': {'stem': 'A 19-year-old man notices a painless swelling under the left side of his tongue that '
                                 'has slowly enlarged over 6 weeks. Exam shows a 2.5-cm soft, fluctuant, translucent '
                                 'bluish swelling in the lateral floor of mouth, lateral to the lingual frenulum and '
                                 'above the mylohyoid. The neck is normal on palpation, and saliva flows clearly from '
                                 'both Wharton ducts. What is the most likely diagnosis?',
                         'choices': ['Midline dermoid cyst',
                                     'Lymphatic malformation',
                                     'Simple (oral) ranula',
                                     'Sublingual gland carcinoma'],
                         'answer': 2,
                         'explanation': 'A simple ranula is a mucus extravasation pseudocyst arising from the '
                                        'sublingual gland that stays above the mylohyoid in the floor of mouth. Its '
                                        'thin wall and mucin content give it a translucent bluish appearance, and it '
                                        'lies lateral to the midline, over the sublingual gland. Normal Wharton duct '
                                        'flow argues against submandibular obstruction. When the mucus passes through '
                                        'or behind the mylohyoid into the submandibular space, it becomes a plunging '
                                        'ranula. Treatment of recurrent or bothersome ranulas centers on the '
                                        'sublingual gland.',
                         'why_wrong': ['Dermoid cysts are midline, doughy, and yellowish, and they often present in '
                                       'childhood rather than as a lateral bluish swelling.',
                                       'Lymphatic malformations are usually present from early childhood, are often '
                                       'multispatial, and can enlarge with infections.',
                                       'Correct.',
                                       'Sublingual gland tumors are uncommon, are usually firm rather than fluctuant, '
                                       'and are often malignant, such as adenoid cystic carcinoma.'],
                         'board_pearl': 'Lateral, translucent bluish floor-of-mouth swelling above the mylohyoid: '
                                        'simple ranula from the sublingual gland.',
                         'curveball': 'What imaging sign can show continuity between a plunging ranula and the '
                                      'sublingual space?',
                         'curveball_answer': 'The tail sign: on CT or MRI, a thin tail of the collapsed cyst extends '
                                             'from the submandibular space collection back into the sublingual space, '
                                             'often through or around the mylohyoid. It points to the sublingual gland '
                                             'as the source, and that gland should be targeted at surgery.'},
 'v237_tps_ranula_app': {'stem': 'A 28-year-old woman has a 2-cm bluish, fluctuant swelling in the right floor of '
                                 'mouth. It was aspirated in clinic 4 months ago and again 6 weeks ago, and each time '
                                 'it returned within weeks. She has no neck swelling, and MRI shows the collection '
                                 'confined above the mylohyoid adjacent to the right sublingual gland. She wants a '
                                 'definitive treatment. Which procedure best addresses the source?',
                         'choices': ['Transoral excision of the right sublingual gland',
                                     'Repeat aspiration with intralesional steroid injection',
                                     'Marsupialization of the ranula roof with packing',
                                     'Transcervical excision of the right submandibular gland'],
                         'answer': 0,
                         'explanation': 'Recurrence after aspiration is expected because the sublingual gland keeps '
                                        'secreting into the extravasation pseudocyst. Removing the ipsilateral '
                                        'sublingual gland through the mouth, with evacuation of the mucus, has the '
                                        'lowest recurrence rate. During the procedure, Wharton duct and the lingual '
                                        'nerve, which crosses beneath the duct, are identified and preserved. '
                                        'Marsupialization, with or without packing, is an option for small first-time '
                                        'ranulas but recurs more often. The submandibular gland is not involved.',
                         'why_wrong': ['Correct.',
                                       'Steroids do not stop the sublingual gland from leaking, and further aspiration '
                                       'has already failed twice.',
                                       'Marsupialization leaves the leaking gland and has a higher recurrence rate '
                                       'than gland excision.',
                                       'The submandibular gland is not the source, and a neck incision adds marginal '
                                       'mandibular nerve risk without benefit.'],
                         'board_pearl': 'Recurrent ranula: transoral sublingual gland excision gives the lowest '
                                        'recurrence; protect Wharton duct and lingual nerve.',
                         'curveball': 'Which nerve and Wharton duct relationships matter during transoral sublingual '
                                      'gland excision?',
                         'curveball_answer': 'Wharton duct runs along the medial surface of the sublingual gland, and '
                                             'the lingual nerve hooks beneath the duct from lateral to medial in the '
                                             'posterior floor of mouth. Cannulate the duct to protect it, find the '
                                             'nerve before dividing deep tissue, and expect possible postoperative '
                                             'duct stenosis or transient tongue numbness.'},
 'v237_tps_ranula_snr': {'stem': 'A 34-year-old man has a 6-cm soft, painless left submandibular neck swelling and a '
                                 'small left floor-of-mouth bulge. MRI shows a unilocular collection in the '
                                 'submandibular space with a narrow tail running into the left sublingual space. He '
                                 'has no airway symptoms, infection, or solid component. The general surgeon proposes '
                                 'a transcervical cyst excision. What is the best surgical approach?',
                         'choices': ['Transoral sublingual gland excision with drainage of the neck component',
                                     'Combined transcervical and transoral excision of the entire pseudocyst',
                                     'Transcervical excision of the collection and the submandibular gland',
                                     'Serial ultrasound-guided aspiration until the collection stops refilling'],
                         'answer': 0,
                         'explanation': 'Even when most of the collection lies in the neck, a plunging ranula is '
                                        'driven by the sublingual gland, as the tail sign here shows. Transoral '
                                        'sublingual gland excision with evacuation of the mucus controls most plunging '
                                        'ranulas, and the cervical component usually resolves without a neck incision. '
                                        'Excising the pseudocyst wall is unnecessary because it has no epithelium. '
                                        'This approach avoids the scar and the marginal mandibular and hypoglossal '
                                        'nerve risks of transcervical surgery. Wharton duct and the lingual nerve are '
                                        'protected during the dissection.',
                         'why_wrong': ['Correct.',
                                       'The pseudocyst has no epithelial lining, so removing it through the neck adds '
                                       'a scar and nerve risk without lowering recurrence.',
                                       'The submandibular gland is not the source, and leaving the sublingual gland in '
                                       'place leads to recurrence.',
                                       'Aspiration leaves the leaking gland in place and usually fails for plunging '
                                       'ranulas.'],
                         'board_pearl': 'Plunging ranula: remove the sublingual gland transorally; the neck component '
                                        'usually resolves without cervical surgery.',
                         'curveball': 'When would a neck approach become reasonable despite a clear sublingual origin?',
                         'curveball_answer': 'A transcervical approach is reasonable when the collection is very large '
                                             'or loculated and fails to resolve after sublingual gland excision, when '
                                             'it is infected and needs drainage, when imaging shows no clear '
                                             'sublingual connection or a solid component that raises concern for '
                                             'another diagnosis, or when recurrence persists after adequate transoral '
                                             'surgery.'},
 'v137_tps_11': {'stem': 'A 59-year-old woman had a right-sided parathyroid exploration at another hospital 5 months '
                         'ago without intraoperative PTH. Calcium never normalized; it is now 11.2 mg/dL with PTH 118 '
                         'pg/mL, normal 25-hydroxyvitamin D, and a calcium-to-creatinine clearance ratio of 0.028. The '
                         'outside pathology report describes a lymph node with no parathyroid tissue. She has '
                         'osteoporosis. What is the most appropriate next step?',
                 'choices': ['Immediate bilateral re-exploration guided by the original operative findings',
                             'Selective venous PTH sampling as the first localization study after surgery',
                             'New noninvasive localization with ultrasound and 4D-CT before reoperation',
                             'Cinacalcet alone, since reoperative risks outweigh any benefit of cure'],
                 'answer': 2,
                 'explanation': 'Persistent hyperparathyroidism after failed surgery requires a diagnostic reset '
                                'before reentry. Here biochemistry is already confirmed: PTH-dependent hypercalcemia, '
                                'normal vitamin D, and a clearance ratio that excludes familial hypocalciuric '
                                'hypercalcemia. The pathology shows the abnormal gland was never removed. The next '
                                'step is high-quality noninvasive localization, typically surgeon-performed ultrasound '
                                'plus 4D-CT or sestamibi SPECT/CT, ideally at an experienced center. Reoperation '
                                'carries higher recurrent nerve and hypoparathyroidism risk, so a concordant target '
                                'supports a focused, planned approach.',
                 'why_wrong': ['Exploring a scarred neck without a fresh target raises nerve and parathyroid risk and '
                               'repeats the original failure.',
                               'Venous sampling is invasive and is reserved for cases where noninvasive studies are '
                               'negative or discordant.',
                               'Correct.',
                               'She has osteoporosis and persistent disease; cure by reoperation is usually achievable '
                               'and preferred over lifelong medication.'],
                 'board_pearl': 'Failed parathyroidectomy: confirm biochemistry, review records, then relocalize '
                                'before reentering a scarred neck.',
                 'curveball': 'What ectopic locations should be specifically reconsidered after a failed exploration '
                              'like hers?',
                 'curveball_answer': 'Missed glands are most often in normal positions or in predictable ectopic '
                                     'sites: the tracheoesophageal groove and retroesophageal space for superior '
                                     'glands, and the thymus, thyrothymic ligament, anterior mediastinum, and '
                                     'undescended carotid-sheath positions for inferior glands. Intrathyroidal glands '
                                     'and supernumerary glands are also considered.'},
 'v142_tps_04': {'stem': 'A 63-year-old man has persistent primary hyperparathyroidism after a bilateral exploration '
                         'elsewhere 2 years ago, at which two normal glands were biopsied. Calcium is 11.3 mg/dL with '
                         'elevated PTH, and familial hypocalciuric hypercalcemia has been excluded. Ultrasound and '
                         '4D-CT both show a 1.4-cm enhancing nodule in the left retroesophageal space at the level of '
                         'the cricoid. Laryngoscopy is normal. What is the best operative plan?',
                 'choices': ['Repeat full bilateral exploration of the scarred neck to inspect all four of the glands',
                             'Focused left reoperation targeting the concordant lesion, with intraoperative PTH',
                             'Median sternotomy to explore the mediastinum for an ectopic inferior gland',
                             'Selective venous PTH sampling before any reoperative surgery is planned'],
                 'answer': 1,
                 'explanation': 'Reoperative parathyroid surgery is safest and most successful when two concordant '
                                'studies identify one target. A retroesophageal gland at the cricoid level is a '
                                'classic missed superior gland that descended posteriorly. A focused approach, often '
                                'through a lateral or back-door plane between the strap muscles and the carotid to '
                                'avoid central scar, with nerve monitoring and intraoperative PTH, limits dissection '
                                'and confirms cure. Reviewing the old operative note matters too: the biopsied glands '
                                'may have been devascularized, raising the risk of hypoparathyroidism.',
                 'why_wrong': ['A full bilateral reexploration exposes both recurrent nerves and remaining '
                               'parathyroids to scar-related injury when a target is already known.',
                               'Correct.',
                               'Concordant imaging places the gland in the neck behind the esophagus, so a sternotomy '
                               'is unnecessary.',
                               'Venous sampling is reserved for negative or discordant noninvasive imaging, which is '
                               'not the case here.'],
                 'board_pearl': 'Concordant reoperative localization allows a focused, lateral-approach reoperation '
                                'with intraoperative PTH.',
                 'curveball': 'When localization remains negative despite unequivocal disease, how do expert-center '
                              'referral and alternative imaging fit the plan?',
                 'curveball_answer': 'Refer to a high-volume parathyroid center for repeat surgeon-performed '
                                     'ultrasound, expert review of prior images, and additional studies such as '
                                     'fluorocholine PET/CT or 4D-MRI. If those fail, selective venous PTH sampling can '
                                     'lateralize the gland. Asymptomatic patients without a target may be observed or '
                                     'treated with cinacalcet rather than explored blindly.'},
 'v236_tps_reophpt_fnd': {'stem': 'A 44-year-old man had a bilateral neck exploration 8 months ago for presumed '
                                  'primary hyperparathyroidism; four normal-sized glands were seen and one was '
                                  'removed. Calcium remains 10.9 mg/dL with PTH 72 pg/mL. A 24-hour urine calcium is '
                                  '40 mg, and the calcium-to-creatinine clearance ratio is 0.004. His mother and '
                                  "sister have 'mildly high calcium' that was never treated. What is the most "
                                  'appropriate next step?',
                          'choices': ['4D-CT and sestamibi SPECT/CT to localize a missed adenoma',
                                      'Median sternotomy to explore the mediastinum for a fifth gland',
                                      'Subtotal parathyroidectomy of the three remaining glands',
                                      'Germline CASR gene testing for familial hypocalciuric hypercalcemia'],
                          'answer': 3,
                          'explanation': 'Before any reoperation, the diagnosis must be reconfirmed. A '
                                         'calcium-to-creatinine clearance ratio below 0.01, low urine calcium, mild '
                                         'hypercalcemia with modestly elevated PTH, four normal glands at exploration, '
                                         'and affected relatives strongly suggest familial hypocalciuric '
                                         'hypercalcemia. This is an inactivating CASR mutation that raises the calcium '
                                         'set point, and it is benign and not cured by parathyroidectomy. Germline '
                                         'CASR testing confirms the diagnosis. Thiazides, lithium, and vitamin D '
                                         'deficiency should also be excluded, and the original operative and pathology '
                                         'records reviewed.',
                          'why_wrong': ['Localization assumes a surgical disease; with this urine profile and family '
                                        'history, the diagnosis itself must be reconsidered first.',
                                        'A mediastinal search for a missed gland is premature and unjustified when the '
                                        'diagnosis is likely not primary hyperparathyroidism.',
                                        'Removing more glands in FHH does not correct calcium and risks permanent '
                                        'hypoparathyroidism.',
                                        'Correct.'],
                          'board_pearl': 'Failed parathyroidectomy with low urine calcium and affected relatives: test '
                                         'for FHH before relocalizing.',
                          'curveball': 'If FHH is excluded, what defines persistent versus recurrent primary '
                                       'hyperparathyroidism after surgery?',
                          'curveball_answer': 'Persistent hyperparathyroidism is failure to achieve normocalcemia '
                                              'within 6 months of surgery, usually from a missed gland or unrecognized '
                                              'multigland disease. Recurrent hyperparathyroidism is return of '
                                              'hypercalcemia after at least 6 months of normal calcium, suggesting new '
                                              'gland disease, hereditary multigland disease, parathyromatosis, or '
                                              'carcinoma.'},
 'v236_tps_reophpt_app': {'stem': 'A 67-year-old woman has biochemically confirmed persistent primary '
                                  'hyperparathyroidism after a bilateral exploration 3 years ago. Calcium is 11.5 '
                                  'mg/dL, and she has recurrent kidney stones. Ultrasound and sestamibi SPECT/CT are '
                                  'negative. Her eGFR is 28 mL/min, and she had anaphylaxis to iodinated contrast '
                                  'during a prior cardiac catheterization. Which next localization study is most '
                                  'appropriate?',
                          'choices': ['4D-CT after steroid and antihistamine premedication for contrast',
                                      'Fluorocholine PET/CT or 4D-MRI, which avoid iodinated contrast',
                                      'Bilateral re-exploration without more imaging',
                                      'Selective venous PTH sampling with iodinated contrast venography'],
                          'answer': 1,
                          'explanation': 'Reoperative localization uses complementary studies chosen for the patient. '
                                         'After negative ultrasound and sestamibi, 4D-CT is usually next, but this '
                                         "patient's contrast anaphylaxis and reduced kidney function make it a poor "
                                         'choice. Fluorocholine PET/CT has high sensitivity for hyperfunctioning '
                                         'parathyroid tissue and needs no iodinated contrast, and 4D-MRI is an '
                                         'alternative where available. A coherent target should be found before '
                                         'reentering a scarred neck, because negative reexploration carries high '
                                         'nerve, parathyroid, and failure risk.',
                          'why_wrong': ['Premedication does not reliably prevent recurrent anaphylaxis, and iodinated '
                                        'contrast adds kidney risk at this eGFR.',
                                        'Correct.',
                                        'A blind reexploration in a scarred neck has a lower cure rate and higher '
                                        'nerve and parathyroid risk.',
                                        'Venous sampling is invasive, needs contrast, and is reserved for when other '
                                        'noninvasive studies have failed.'],
                          'board_pearl': 'Tailor reoperative localization to the patient: fluorocholine PET or 4D-MRI '
                                         'when contrast or kidney function precludes 4D-CT.',
                          'curveball': 'When is selective venous PTH sampling useful after the noninvasive studies '
                                       'disagree or stay negative?',
                          'curveball_answer': 'Selective venous sampling is reserved for reoperative patients with '
                                              'unequivocal disease when noninvasive imaging is negative or discordant. '
                                              'A step-up in PTH in a specific thyroid, thymic, or vertebral vein '
                                              'lateralizes the gland and can guide a focused approach. It is invasive, '
                                              'operator-dependent, and needs an experienced interventional '
                                              'radiologist.'},
 'v236_tps_reophpt_snr': {'stem': 'A 68-year-old woman has persistent mild primary hyperparathyroidism after two prior '
                                  'explorations; the second caused permanent right vocal fold paralysis. Calcium is '
                                  '10.8 mg/dL, bone density is normal, and she has no stones and normal kidney '
                                  'function. 4D-CT shows a 7-mm target in the scarred left tracheoesophageal groove, '
                                  'beside her only functioning recurrent laryngeal nerve. What is the best '
                                  'recommendation?',
                          'choices': ['Left reoperation with continuous nerve monitoring and intraoperative PTH',
                                      'Elective tracheostomy, then left reoperation to remove the target gland',
                                      'Bilateral re-exploration to identify and remove all remaining glands',
                                      'Surveillance of calcium, bone, and kidneys, with cinacalcet if needed'],
                          'answer': 3,
                          'explanation': 'The threshold for reoperative parathyroidectomy is higher than for primary '
                                         'surgery, and the expected benefit must justify the specific risks. She has '
                                         'mild, asymptomatic disease that meets no surgical criterion: calcium within '
                                         '1 mg/dL of normal, normal bone density, no stones, and normal kidney '
                                         'function. The target sits beside her only functioning recurrent laryngeal '
                                         'nerve, so injury would cause bilateral vocal fold paralysis and possibly '
                                         'tracheostomy. Surveillance of calcium, bone density, and kidney function, '
                                         'with cinacalcet for symptomatic or rising calcium, is the safer course.',
                          'why_wrong': ['Injury to her only functioning nerve would cause bilateral paralysis and '
                                        'airway compromise, a risk out of proportion to mild asymptomatic disease.',
                                        'Accepting a tracheostomy to remove a gland causing mild, asymptomatic disease '
                                        'reverses the risk-benefit balance.',
                                        'Bilateral reexploration magnifies the risk to the only working nerve and to '
                                        'any remaining parathyroid tissue.',
                                        'Correct.'],
                          'board_pearl': 'Reoperation must justify its risk; mild asymptomatic disease beside the only '
                                         'working RLN favors surveillance.',
                          'curveball': 'Two years later her calcium has risen to 12.1 mg/dL and she passes a kidney '
                                       'stone. How does that change the plan?',
                          'curveball_answer': 'New end-organ disease shifts the balance toward treatment. Options '
                                              'include reoperation at an expert center with continuous nerve '
                                              'monitoring and explicit consent for airway risk, or a nonsurgical '
                                              'alternative such as ultrasound-guided ethanol or thermal ablation, '
                                              'which also threatens the nearby nerve. Cinacalcet remains reasonable if '
                                              'she declines intervention.'},
 'v137_tps_12': {'stem': 'A 50-year-old woman had total thyroidectomy, central neck dissection, and radioiodine for '
                         'papillary carcinoma 6 years ago. Stimulated thyroglobulin has risen to 8 ng/mL. Ultrasound '
                         'shows a 1.3-cm hypoechoic right paratracheal node, and FNA with thyroglobulin washout is '
                         'positive. Her voice sounds normal and she has no dysphagia. Reoperative central neck surgery '
                         'is planned. Which preoperative assessment is essential?',
                 'choices': ['Laryngoscopy and ultrasound mapping of the central and lateral neck',
                             'Voice assessment by history alone, since her voice sounds normal',
                             'Diagnostic radioiodine scan to choose between surgery and more RAI',
                             'FDG PET/CT as the sole imaging study, in place of neck ultrasound'],
                 'answer': 0,
                 'explanation': 'Reoperative central neck surgery carries higher recurrent nerve and parathyroid risk '
                                'because scar obscures planes and landmarks. Two assessments are essential. '
                                'Laryngoscopy documents vocal fold mobility, since a compensated unilateral paralysis '
                                'may be silent and would change the risk of operating near the other nerve. '
                                'Comprehensive ultrasound of the central and lateral compartments maps every target so '
                                'that all disease is removed in one operation; cross-sectional imaging is added for '
                                'bulky or deep disease. The prior operative and pathology reports should also be '
                                'reviewed.',
                 'why_wrong': ['Correct.',
                               'A normal-sounding voice does not exclude a compensated unilateral paralysis, which '
                               'changes the risk of further nerve injury.',
                               'Biopsy-proven structural nodal disease of this size is treated surgically, and '
                               'recurrent disease is often iodine-refractory.',
                               'PET is insensitive for small nodal recurrences and cannot map neck disease as '
                               'precisely as surgeon-directed ultrasound.'],
                 'board_pearl': 'Before reoperative thyroid surgery: laryngoscopy regardless of voice, and complete '
                                'ultrasound mapping of all neck compartments.',
                 'curveball': 'If one recurrent laryngeal nerve is already paralyzed, how does that alter the risk '
                              'discussion for contralateral surgery?',
                 'curveball_answer': 'Injury to the only functioning nerve would cause bilateral vocal fold paralysis '
                                     'with stridor and likely tracheostomy. The surgeon should use continuous or '
                                     'careful intermittent nerve monitoring, consider limiting dissection near that '
                                     'nerve or accepting minimal residual disease, consider staging procedures, and '
                                     'discuss tracheostomy risk explicitly during consent.'},
 'v146_tps_09': {'stem': 'A 47-year-old man needs reoperation for a biopsy-proven 1.5-cm recurrent papillary carcinoma '
                         'node in the right paratracheal region, 5 years after total thyroidectomy. The prior '
                         'operative note states both inferior parathyroids were removed and autotransplanted into the '
                         'left SCM, and the left superior gland was not seen. The right superior gland was preserved '
                         'on its pedicle. Laryngoscopy is normal. What intraoperative priority does this record '
                         'create?',
                 'choices': ['Disregard the old record, since parathyroids regenerate after surgery',
                             'Routinely autotransplant the right superior gland before dissecting',
                             'Identify and protect the right superior parathyroid as a key source',
                             'Plan a bilateral central dissection to remove any remaining glands'],
                 'answer': 2,
                 'explanation': 'Reoperative fields hide what the first surgeon removed, saw, or left. This note shows '
                                'that the right superior gland, which sits right next to the planned dissection, may '
                                'be one of her few remaining in situ glands, along with whatever function the SCM '
                                'autografts provide. The surgeon should find it early, dorsal to the recurrent nerve '
                                'near the cricothyroid junction, preserve its blood supply, and autotransplant it if '
                                'it is devascularized. Baseline calcium and PTH show how much function the grafts '
                                'provide.',
                 'why_wrong': ['Parathyroid tissue does not regenerate, and the old record is the only map of what '
                               'remains.',
                               'A gland left in situ on its own pedicle functions more reliably than a graft; '
                               'autotransplant only if it becomes devascularized.',
                               'Correct.',
                               'The recurrence is right-sided; bilateral dissection adds risk to both nerves and the '
                               'remaining parathyroid tissue without benefit.'],
                 'board_pearl': 'Read the prior operative note before reoperation: it tells you which parathyroids and '
                                'nerves remain at risk.',
                 'curveball': 'How does a preexisting unilateral paralysis change the threshold for contralateral '
                              'dissection?',
                 'curveball_answer': 'It raises the threshold sharply, because injury to the remaining functioning '
                                     'nerve would cause bilateral paralysis and airway compromise. Contralateral '
                                     'dissection is limited to clear, clinically important disease, done with nerve '
                                     'monitoring and by an experienced surgeon, and the patient is counseled about '
                                     'possible tracheostomy. Staged surgery or surveillance of small disease is often '
                                     'preferable.'},
 'v234_tps_reopthy_fnd': {'stem': 'A 55-year-old woman had a left lobectomy for a benign nodule 12 years ago. A new '
                                  'right-lobe nodule is now Bethesda VI, and completion of thyroid surgery is planned. '
                                  'During consent she asks why the surgeon quoted higher risks of voice change and low '
                                  'calcium than for her first operation, even though the right side was never operated '
                                  'on. Which explanation is most accurate?',
                          'choices': ['The recurrent laryngeal nerve regenerates after surgery into a new course',
                                      'Prior radioiodine treatment has weakened the tissue planes around the gland',
                                      'Scar and distorted planes obscure the nerve and parathyroid blood supply',
                                      'Thyroid tissue regrows into the old operative bed and encases the nerve'],
                          'answer': 2,
                          'explanation': 'Reoperative thyroid surgery is riskier because fibrosis from the first '
                                         'operation fuses tissue planes, distorts landmarks, tethers the recurrent '
                                         'laryngeal nerve, and obscures parathyroid glands and their blood supply. '
                                         'Even an unoperated side can be scarred by midline and strap muscle '
                                         'dissection. Her left parathyroids may have been removed or devascularized '
                                         'during the lobectomy, so the right glands may be her only functioning '
                                         'tissue. Preoperative laryngoscopy, the prior operative report, nerve '
                                         'monitoring, and a lateral approach to avoid midline scar help reduce risk.',
                          'why_wrong': ['Nerves do not regenerate into new anatomic courses after thyroid surgery; '
                                        'scar distorts their surroundings instead.',
                                        'She has not received radioiodine; the added risk comes from postoperative '
                                        'scarring, not from radiation.',
                                        'Correct.',
                                        'Thyroid remnants can regrow, but the main hazard is fibrosis distorting '
                                        'planes, not regrowth that encases the nerve.'],
                          'board_pearl': 'Reoperative thyroid risk comes from scar, distorted planes, and possibly '
                                         'fewer remaining parathyroids; review records and scope first.',
                          'curveball': 'Which details from the original operative and pathology reports are most '
                                       'useful before re-entry?',
                          'curveball_answer': 'Useful details include whether each recurrent nerve was identified and '
                                              'how it stimulated, which parathyroids were seen, preserved, biopsied, '
                                              'removed, or autotransplanted and where, the extent of nodal dissection, '
                                              'any complications, and whether the pathology contains parathyroid '
                                              'tissue. Together these show which structures remain at risk.'},
 'v234_tps_reopthy_app': {'stem': 'A 52-year-old man had a right thyroid lobectomy at another hospital 9 years ago. A '
                                  '2.5-cm left-lobe nodule is now Bethesda V, and completion thyroidectomy is '
                                  'scheduled. His voice sounds normal to him and to the surgeon, and he sings in a '
                                  'church choir. He asks whether a scope exam is necessary, since his voice is fine. '
                                  'Which preoperative step is most appropriate?',
                          'choices': ['Flexible laryngoscopy before surgery, despite the normal voice',
                                      'Postoperative laryngoscopy only if hoarseness develops afterward',
                                      'Voice Handicap Index questionnaire as the preoperative screen',
                                      'Intraoperative nerve monitoring in place of preoperative laryngoscopy'],
                          'answer': 0,
                          'explanation': 'Laryngoscopy before reoperative thyroid surgery is recommended for every '
                                         'patient, regardless of voice, because unilateral vocal fold paralysis can be '
                                         'well compensated and silent. If his right recurrent nerve was injured at the '
                                         'first operation, the left nerve is his only functioning one, and injuring it '
                                         'would cause bilateral paralysis with airway obstruction. That knowledge '
                                         'changes consent, nerve monitoring strategy, extent of surgery, and whether '
                                         'staging or limiting the operation is safer. AAO-HNSF voice-outcome guidance '
                                         'for thyroid surgery and ATA guidance both support preoperative laryngeal '
                                         'examination.',
                          'why_wrong': ['Correct.',
                                        'Learning after surgery that the right nerve was already paralyzed means the '
                                        'left nerve was risked without that knowledge.',
                                        'Voice questionnaires are not sensitive enough to detect a compensated '
                                        'unilateral paralysis.',
                                        'Monitoring helps during surgery but does not reveal baseline paralysis of the '
                                        'previously operated right side.'],
                          'board_pearl': 'Scope every reoperative thyroid patient preoperatively; a normal voice does '
                                         'not exclude a compensated paralysis.',
                          'curveball': 'How would preexisting contralateral vocal fold paralysis change the threshold '
                                       'for surgery or nerve sacrifice?',
                          'curveball_answer': 'If the right fold is paralyzed, the left nerve must be preserved '
                                              'whenever possible. Surgeons use continuous monitoring, stop if signal '
                                              'is lost, and do not sacrifice a functioning nerve for oncologic margin '
                                              'when the tumor can be shaved off, accepting minimal residual disease. '
                                              'For a Bethesda V nodule, discussing the airway risk and possible '
                                              'tracheostomy is mandatory.'},
 'v234_tps_reopthy_snr': {'stem': 'A 61-year-old woman undergoes reoperation for recurrent papillary carcinoma in the '
                                  'left paratracheal region. Her right vocal fold has been paralyzed since her '
                                  'original thyroidectomy. The tumor is tightly adherent to the left recurrent '
                                  'laryngeal nerve but does not encase or enter it, and the nerve stimulates normally. '
                                  'Frozen section shows no poorly differentiated features. How should the nerve be '
                                  'managed?',
                          'choices': ['Resect the nerve with the tumor to achieve a clear margin, then reinnervate it',
                                      'Abort the resection and refer her for external beam radiation of the neck',
                                      'Resect the nerve and the tumor en bloc, with a tracheostomy planned afterward',
                                      'Sharply dissect the tumor off the nerve and preserve it, accepting minimal '
                                      'residual'],
                          'answer': 3,
                          'explanation': 'Nerve management in reoperative thyroid cancer weighs oncologic gain against '
                                         'function. A functioning nerve that is adherent to, but not grossly invaded '
                                         'by, well-differentiated carcinoma should be preserved by sharp dissection, '
                                         'accepting possible microscopic residual disease that can be treated with '
                                         'radioiodine and surveillance. Here the left nerve is her only functioning '
                                         'nerve, which makes preservation even more important. Sacrifice is considered '
                                         'only for true gross invasion of a nerve that is already paralyzed, or in '
                                         'selected cases with a normal contralateral nerve and aggressive histology.',
                          'why_wrong': ['Resecting her only functioning nerve would cause bilateral paralysis, and '
                                        'reinnervation does not restore abduction for the airway.',
                                        'Well-differentiated tumor adherent to but separable from the nerve should be '
                                        'removed; radiation is not first-line.',
                                        'Accepting a tracheostomy to clear microscopic margins of differentiated '
                                        'cancer trades a manageable risk for permanent harm.',
                                        'Correct.'],
                          'board_pearl': 'Preserve a functioning RLN that can be dissected off differentiated cancer, '
                                         'especially if it is the only working nerve.',
                          'curveball': 'When might intentional gross residual disease be reasonable because nerve '
                                       'sacrifice would create disproportionate harm?',
                          'curveball_answer': 'When the only functioning recurrent nerve is grossly invaded by '
                                              'well-differentiated, slowly growing carcinoma, leaving a small amount '
                                              'of tumor on the nerve may be better than bilateral paralysis and '
                                              'tracheostomy. Residual disease is then treated with radioiodine or '
                                              'external beam radiation, or watched, and the decision is documented and '
                                              'discussed with the patient in advance.'},
 'v137_tps_13': {'stem': 'A 47-year-old man on hemodialysis for 7 years has bone pain, two vertebral fractures, and '
                         'pruritus. Intact PTH is 1,850 pg/mL, calcium 10.4 mg/dL, phosphate 6.8 mg/dL, and alkaline '
                         'phosphatase elevated, despite cinacalcet, phosphate binders, and calcitriol limited by '
                         'hypercalcemia. Ultrasound shows four enlarged glands. He is not a transplant candidate in '
                         'the near term. Which operation is most appropriate?',
                 'choices': ['Focused excision of the largest gland with intraoperative PTH monitoring',
                             'Subtotal parathyroidectomy, or total with forearm autotransplant',
                             'Removal of the two largest glands only',
                             'Ultrasound-guided ethanol ablation of the most enlarged gland identified'],
                 'answer': 1,
                 'explanation': 'Secondary hyperparathyroidism of kidney disease produces diffuse and then nodular '
                                'hyperplasia of all glands. When severe disease persists despite optimal medical '
                                'therapy, with fractures, bone pain, pruritus, or vascular calcification, '
                                'parathyroidectomy is indicated. The operation must address every gland: subtotal '
                                'parathyroidectomy leaving a well-vascularized remnant of about 50 mg, or total '
                                'parathyroidectomy with forearm autotransplantation. Transcervical thymectomy is often '
                                'added because supernumerary glands are common. Total parathyroidectomy without '
                                'autotransplant is avoided in transplant candidates because of permanent '
                                'hypoparathyroidism.',
                 'why_wrong': ['Renal hyperparathyroidism is multigland hyperplasia, so removing one gland leaves most '
                               'of the hyperfunctioning tissue in place.',
                               'Correct.',
                               'Leaving two hyperplastic glands intact usually results in persistent or early '
                               'recurrent disease.',
                               'Ablating one gland does not address four-gland hyperplasia and makes later surgery '
                               'harder by scarring the field.'],
                 'board_pearl': 'Refractory renal hyperparathyroidism: subtotal or total-plus-autotransplant '
                                'parathyroidectomy, often with thymectomy; never focused excision.',
                 'curveball': 'After his parathyroidectomy, what postoperative electrolyte complication requires '
                              'aggressive monitoring, and who is at highest risk?',
                 'curveball_answer': 'Hungry bone syndrome: abrupt PTH withdrawal causes rapid skeletal uptake of '
                                     'calcium, phosphate, and magnesium, leading to severe, prolonged hypocalcemia. '
                                     'Preoperative high alkaline phosphatase and severe bone disease predict it. Check '
                                     'calcium every 4 to 6 hours, start high-dose calcitriol and oral calcium early, '
                                     'use IV calcium infusion as needed, and adjust the dialysate calcium.'},
 'v146_tps_11': {'stem': 'A 52-year-old woman on hemodialysis has painful, nonhealing calciphylaxis ulcers on both '
                         'thighs. Intact PTH is 1,400 pg/mL despite maximal cinacalcet, and calcium-phosphate product '
                         'is high. Sestamibi SPECT/CT shows intense uptake in a 2-cm left inferior gland and faint '
                         'uptake elsewhere. A colleague suggests a quick focused excision of the dominant gland to '
                         'limit anesthesia time. What is the most appropriate operation?',
                 'choices': ['Focused excision of the sestamibi-positive gland with intraoperative PTH',
                             'Increase cinacalcet and defer any surgery until the thigh ulcers heal',
                             'Ultrasound-guided ethanol ablation of the dominant left inferior gland',
                             'Bilateral exploration with subtotal parathyroidectomy and thymectomy'],
                 'answer': 3,
                 'explanation': 'Renal hyperparathyroidism is multigland disease even when imaging highlights one '
                                'dominant nodular gland. Localization in this setting finds ectopic or supernumerary '
                                'glands; it does not justify a focused operation. With very high PTH and calciphylaxis '
                                'refractory to medical therapy, parathyroidectomy is reasonable as part of '
                                'comprehensive calciphylaxis care, alongside wound care, sodium thiosulfate, and '
                                'dialysis optimization. The operation is bilateral exploration with subtotal '
                                'parathyroidectomy, or total with autotransplant, plus transcervical thymectomy, '
                                'followed by close monitoring for hungry bone.',
                 'why_wrong': ['Sestamibi often highlights the largest nodular gland, but the other hyperplastic '
                               'glands remain and disease persists.',
                               'She is already on maximal cinacalcet with worsening ulcers; delaying treatment of PTH '
                               'excess risks progression and sepsis.',
                               'Ablating one gland leaves the others hyperfunctioning and scars the field for later '
                               'surgery.',
                               'Correct.'],
                 'board_pearl': 'In renal hyperparathyroidism, single-gland imaging does not permit focused surgery; '
                                'plan a multigland operation.',
                 'curveball': 'Why is postoperative calcium management especially challenging in this dialysis patient '
                              'with calciphylaxis?',
                 'curveball_answer': 'Severe, long-standing high-turnover bone disease predicts hungry bone syndrome, '
                                     'with profound hypocalcemia lasting days to weeks. Dialysis patients also lack '
                                     'renal calcitriol production. Management needs early high-dose calcitriol, oral '
                                     'calcium, frequent calcium checks, IV calcium infusion, magnesium and phosphate '
                                     'monitoring, and coordination of dialysate calcium with nephrology.'},
 'v234_tps_secpar_fnd': {'stem': 'A 61-year-old woman with stage 5 chronic kidney disease on hemodialysis has intact '
                                 'PTH 620 pg/mL, calcium 8.6 mg/dL, phosphate 6.4 mg/dL, and low 1,25-dihydroxyvitamin '
                                 'D. Ultrasound shows four symmetrically enlarged parathyroid glands. A medical '
                                 'student asks how her disease differs from tertiary hyperparathyroidism. Which '
                                 'mechanism best explains her current PTH elevation?',
                         'choices': ['Autonomous PTH secretion persisting after the stimulus is corrected',
                                     'Compensatory hyperplasia from phosphate retention and low calcitriol',
                                     'A single autonomous adenoma with suppression of the other glands',
                                     'Ectopic PTH-related peptide secretion by an occult malignancy'],
                         'answer': 1,
                         'explanation': 'Secondary hyperparathyroidism is an appropriate response to the mineral '
                                        'derangements of kidney failure. Phosphate retention, reduced renal production '
                                        'of calcitriol, hypocalcemia, raised FGF23, and skeletal resistance to PTH all '
                                        'stimulate the glands, which first become diffusely and then nodularly '
                                        'hyperplastic. Calcium is low or normal. Tertiary hyperparathyroidism develops '
                                        'when long-standing stimulation produces autonomous glands that keep secreting '
                                        'PTH, usually with hypercalcemia, even after the stimulus is corrected, '
                                        'classically after kidney transplantation. Both are multigland diseases.',
                         'why_wrong': ['That describes tertiary hyperparathyroidism, which usually presents with '
                                       'hypercalcemia, often after transplant; her calcium is low-normal.',
                                       'Correct.',
                                       'Four symmetrically enlarged glands and low calcium argue against a single '
                                       'adenoma causing primary disease.',
                                       'PTH-related peptide suppresses intact PTH and causes hypercalcemia, the '
                                       'opposite of this picture.'],
                         'board_pearl': 'Secondary HPT: compensatory hyperplasia with low or normal calcium; tertiary '
                                        'HPT: autonomous secretion with hypercalcemia.',
                         'curveball': 'If she receives a kidney, how does successful renal transplantation change the '
                                      'expected calcium-PTH physiology?',
                         'curveball_answer': 'A working graft restores phosphate excretion and calcitriol production, '
                                             'so PTH usually falls over 6 to 12 months as hyperplastic glands slowly '
                                             'involute. Nodular glands may not involute and continue secreting PTH, '
                                             'causing hypercalcemia, hypophosphatemia, and graft or bone injury. '
                                             'Persistent hypercalcemia beyond about a year after transplant defines '
                                             'tertiary hyperparathyroidism.'},
 'v234_tps_secpar_app': {'stem': 'A 39-year-old man on hemodialysis for 5 years has intact PTH 1,600 pg/mL, calcium '
                                 '10.6 mg/dL, and phosphate 7.2 mg/dL despite maximal cinacalcet, sevelamer, and '
                                 'low-dose calcitriol limited by hypercalcemia. He has bone pain and painful calcific '
                                 'masses around both shoulders. Ultrasound shows four enlarged glands. He is listed '
                                 'for a kidney transplant with an expected wait of 4 years. What is the best next '
                                 'step?',
                         'choices': ['Increase the calcitriol dose to further suppress PTH secretion',
                                     'Await kidney transplant, which reliably reverses his gland disease',
                                     'Referral for parathyroidectomy after nephrology optimization',
                                     'Add etelcalcetide to cinacalcet and recheck PTH again in a year'],
                         'answer': 2,
                         'explanation': 'Most secondary hyperparathyroidism is managed medically, but KDIGO guidance '
                                        'supports parathyroidectomy for severe disease that fails medical therapy. '
                                        'This patient has very high PTH despite maximal calcimimetic, binder, and '
                                        'vitamin D therapy, plus hypercalcemia, hyperphosphatemia, bone pain, and '
                                        'tumoral calcinosis. Large nodular glands respond poorly to drugs and often '
                                        'persist after transplant. With years until transplant, parathyroidectomy is '
                                        'appropriate after optimizing dialysis and electrolytes. The operation '
                                        'addresses all glands, and the team prepares for hungry bone syndrome.',
                         'why_wrong': ['Higher-dose calcitriol is already limited by hypercalcemia and would worsen '
                                       'calcium, phosphate, and soft tissue calcification.',
                                       'Large nodular glands often keep secreting after transplant, and waiting years '
                                       'leaves him with progressive bone and calcific disease.',
                                       'Correct.',
                                       'Calcimimetics are not combined, and another year of uncontrolled PTH allows '
                                       'his calcific disease to progress.'],
                         'board_pearl': 'Refractory secondary HPT with hypercalcemia, calcification, or bone disease '
                                        'despite maximal therapy: refer for parathyroidectomy.',
                         'curveball': 'What preoperative calcium, phosphate, alkaline phosphatase, and vitamin D '
                                      'findings predict difficult postoperative calcium management?',
                         'curveball_answer': 'High alkaline phosphatase, very high PTH, radiographic bone disease, '
                                             'younger age, and low preoperative calcium predict hungry bone syndrome. '
                                             'Vitamin D deficiency worsens it. Begin calcitriol before or immediately '
                                             'after surgery, monitor calcium every few hours early, and plan IV '
                                             'calcium infusion and dialysate adjustments.'},
 'v234_tps_secpar_snr': {'stem': 'A 46-year-old man received a deceased-donor kidney transplant 14 months ago and has '
                                 'stable graft function with creatinine 1.2 mg/dL. Calcium remains 11.6 mg/dL, '
                                 'phosphate 2.2 mg/dL, and intact PTH 420 pg/mL. He has had a kidney stone since '
                                 'transplant, and DEXA shows new osteoporosis. Ultrasound shows enlargement of at '
                                 'least three glands. What is the best management?',
                         'choices': ['Subtotal parathyroidectomy via bilateral neck exploration',
                                     'Focused excision of the largest gland seen on ultrasound',
                                     'Continued observation, since PTH will normalize with time',
                                     'Lifelong cinacalcet as the definitive long-term medical treatment'],
                         'answer': 0,
                         'explanation': 'Persistent hypercalcemia more than a year after successful transplant, with a '
                                        'high PTH, low phosphate, kidney stones, and bone loss, indicates tertiary '
                                        'hyperparathyroidism. The glands have become autonomous and nodular. '
                                        'Parathyroidectomy is indicated for symptomatic or persistent disease because '
                                        'it normalizes calcium more reliably than cinacalcet and protects the graft '
                                        'and skeleton. Because the disease is multigland, bilateral exploration with '
                                        'subtotal parathyroidectomy is standard, with less extensive resection only '
                                        'for selected asymmetric disease. The transplant team helps monitor graft '
                                        'function closely.',
                         'why_wrong': ['Correct.',
                                       'Tertiary hyperparathyroidism is multigland disease, so a focused excision of '
                                       'one gland usually leaves persistent hypercalcemia.',
                                       'Hypercalcemia persisting beyond a year after a working transplant is unlikely '
                                       'to resolve and is already causing stones and bone loss.',
                                       'Cinacalcet is used off-label after transplant and normalizes calcium less '
                                       'often than surgery, with no proven bone benefit.'],
                         'board_pearl': 'Tertiary HPT after transplant: bilateral exploration with subtotal '
                                        'parathyroidectomy beats cinacalcet for durable normocalcemia.',
                         'curveball': 'How do subtotal parathyroidectomy and total parathyroidectomy with '
                                      'autotransplantation differ in recurrence and hypoparathyroidism tradeoffs?',
                         'curveball_answer': 'Subtotal parathyroidectomy leaves a vascularized cervical remnant with '
                                             'reliable function, but recurrence requires reoperation in the neck. '
                                             'Total parathyroidectomy with forearm autotransplantation allows graft '
                                             'recurrence to be treated under local anesthesia, but the graft may fail '
                                             'and cause hypoparathyroidism. After transplant, subtotal is favored to '
                                             'avoid permanent hypocalcemia.'},
 'v137_tps_14': {'stem': 'A 38-year-old woman has 8 months of recurrent painful right submandibular swelling that '
                         'begins while eating and subsides over 2 hours. Between episodes the gland is soft and '
                         'nontender. Ultrasound shows a 4-mm mobile echogenic stone in the proximal Wharton duct with '
                         'mild ductal dilation and normal gland parenchyma. The stone is not palpable transorally. '
                         'Which treatment is most appropriate?',
                 'choices': ['Sialendoscopy with basket retrieval of the stone',
                             'Transcervical submandibular gland excision',
                             'Extracorporeal shock wave lithotripsy sessions',
                             'Long-term sialogogues and antibiotics alone'],
                 'answer': 0,
                 'explanation': 'Small, mobile, intraductal stones are ideal for interventional sialendoscopy. The '
                                'papilla is dilated, a small-caliber endoscope is passed under saline irrigation, and '
                                'the stone is captured in a wire basket and delivered, preserving a gland whose '
                                'parenchyma is still normal. Submandibular stones are common because the saliva is '
                                'more alkaline and mucinous and the duct runs uphill. Stones up to about 4 to 5 mm in '
                                'the submandibular duct can usually be retrieved endoscopically. Larger, fixed, or '
                                'hilar stones need fragmentation or a combined transoral approach.',
                 'why_wrong': ['Correct.',
                               'Excision sacrifices a healthy gland and adds marginal mandibular, lingual, and '
                               'hypoglossal nerve risk when a gland-preserving option exists.',
                               'Shock wave lithotripsy is not FDA-cleared for salivary stones in the US and needs '
                               'repeated sessions with fragments that may remain.',
                               'Conservative care does not remove the stone, and ongoing obstruction leads to '
                               'recurrent infection and gland damage.'],
                 'board_pearl': 'Small mobile ductal stone: sialendoscopic basket retrieval preserves the gland and '
                                'avoids neck surgery.',
                 'curveball': 'When is a combined transoral approach more useful than endoscopic retrieval alone?',
                 'curveball_answer': 'A combined approach helps when the stone is larger than about 5 mm in the '
                                     'submandibular duct or 4 mm in the parotid duct, is fixed or impacted, or lies at '
                                     'the hilum and is palpable. The endoscope localizes the stone, a transoral '
                                     'ductotomy over it delivers it, and the duct is repaired or marsupialized while '
                                     'the lingual nerve is protected.'},
 'v143_tps_05': {'stem': 'A 46-year-old man has recurrent meal-related left submandibular swelling with two episodes '
                         'of infection treated with antibiotics. A firm 8-mm stone is palpable bimanually in the mid '
                         'Wharton duct, opposite the first molar. CT shows the single stone without gland atrophy, and '
                         'the gland empties well on massage once the swelling settles. He wants to keep the gland. '
                         'What is the best gland-preserving strategy?',
                 'choices': ['Basket retrieval of the intact stone through the papilla',
                             'Transcervical excision of the left submandibular gland',
                             'Endoscope-assisted transoral ductotomy to remove the stone',
                             'Long-term antibiotics with massage and sialogogues'],
                 'answer': 2,
                 'explanation': 'Small accessible stones are basketed, but a stone this large in the submandibular '
                                'duct exceeds the diameter of the distal duct. Because it is palpable in the mid duct, '
                                'the best gland-preserving option is transoral removal: the endoscope confirms '
                                'position and clears debris, an incision is made directly over the stone along the '
                                'duct, and the stone is delivered, with the lingual nerve, which crosses beneath the '
                                'posterior duct, protected. Gland function is preserved and recurrence is low. '
                                'Intracorporeal laser lithotripsy is an alternative for nonpalpable large stones.',
                 'why_wrong': ['An 8-mm stone is too large to pull intact through the narrow distal duct and papilla, '
                               'risking duct avulsion or impaction.',
                               'Gland excision is reserved for intraparenchymal, irretrievable, or refractory disease, '
                               'not an accessible ductal stone in a functioning gland.',
                               'Correct.',
                               'Antibiotics treat infections but leave the obstructing stone, so episodes recur and '
                               'the gland is progressively damaged.'],
                 'board_pearl': 'Large palpable submandibular duct stone: combined endoscope-assisted transoral '
                                'removal preserves the gland.',
                 'curveball': 'What stone size or location may require lithotripsy rather than basket extraction or '
                              'ductotomy?',
                 'curveball_answer': 'Large stones that are not palpable transorally, especially those in the parotid '
                                     'duct or deep in the submandibular hilum where a ductotomy is impractical, can be '
                                     'fragmented with intracorporeal holmium laser or pneumatic lithotripsy under '
                                     'endoscopic vision. The fragments are then basketed or flushed out. Combined '
                                     'approaches help when fragments remain.'},
 'v235_tps_sialendo_fnd': {'stem': 'A 52-year-old man has 1 year of recurrent left parotid swelling that starts within '
                                   'minutes of eating and resolves over several hours, without fever or pus. He has '
                                   'not received radioiodine and has no dry eyes or mouth. Ultrasound shows a dilated '
                                   'Stensen duct with no visible stone and normal parenchyma. MR sialography suggests '
                                   'a filling defect in the proximal duct. What is the most appropriate next step?',
                           'choices': ['Superficial parotidectomy with nerve dissection',
                                       'Diagnostic and interventional sialendoscopy',
                                       'Botulinum toxin injection into the parotid gland',
                                       'CT-guided core biopsy of the parotid parenchyma'],
                           'answer': 1,
                           'explanation': 'Meal-related swelling with a dilated duct indicates obstruction, and the '
                                          'filling defect could be a small stone, mucus plug, or stenosis that '
                                          'ultrasound cannot resolve. Sialendoscopy lets the surgeon see the ductal '
                                          'system directly and treat what is found in the same procedure: irrigation '
                                          'of mucus plugs, basket retrieval of small stones, and balloon or dilator '
                                          'treatment of stenoses, often with intraductal steroid irrigation and a '
                                          'temporary stent. It preserves the gland and avoids facial nerve risk, '
                                          'making it first-line for obstructive parotid disease.',
                           'why_wrong': ['Parotidectomy removes a functioning gland and risks facial nerve injury for '
                                         'an obstruction that can usually be treated through the duct.',
                                         'Correct.',
                                         'Botulinum toxin reduces salivary output and is reserved for refractory '
                                         'cases, sialoceles, or fistulas, not untreated obstruction.',
                                         'There is no mass; a biopsy of normal parenchyma cannot diagnose or relieve a '
                                         'ductal obstruction.'],
                           'board_pearl': 'Obstructive salivary symptoms with unclear cause: sialendoscopy diagnoses '
                                          'and treats stones, plugs, and stenoses while preserving the gland.',
                           'curveball': 'What anatomy makes submandibular duct endoscopy technically different from '
                                        'parotid duct endoscopy?',
                           'curveball_answer': 'Wharton duct is wider and runs a long, fairly straight course, but its '
                                               'papilla is small and hard to cannulate and the lingual nerve crosses '
                                               'beneath it posteriorly. Stensen duct has a narrower lumen and a sharp '
                                               'bend where it turns around the anterior border of the masseter, the '
                                               'usual site of resistance, before piercing the buccinator.'},
 'v235_tps_sialendo_app': {'stem': 'A 44-year-old woman undergoes left submandibular sialendoscopy under general '
                                   'anesthesia for a 3-mm stone seen on ultrasound in the proximal Wharton duct. After '
                                   'papillary dilation, the scope advances 2 cm, then meets increasing resistance at a '
                                   'bend. The duct wall ahead blanches white, a small mucosal flap appears, and '
                                   'irrigation fluid begins pooling in the floor of mouth. What is the safest next '
                                   'action?',
                           'choices': ['Push the scope through with firmer pressure to pass the narrow bend',
                                       'Increase irrigation pressure to distend and dilate the duct ahead',
                                       'Fire the laser fiber forward to open a passage through the bend',
                                       'Stop advancing, withdraw slightly, and reassess the lumen under vision'],
                           'answer': 3,
                           'explanation': 'Blanching, a mucosal flap, and fluid pooling outside the duct are early '
                                          'signs of mucosal injury or perforation. Sialendoscopy depends on gentle, '
                                          'controlled advancement with the lumen in view at all times. The surgeon '
                                          'should stop, withdraw slightly, lower irrigation pressure, and look for the '
                                          'true lumen. Options include gentle guide-wire dilation if the lumen is '
                                          'clear, or ending the endoscopic attempt and converting to a transoral '
                                          'approach or staging the procedure. Forcing the scope creates a false '
                                          'passage, extravasation, and later stenosis.',
                           'why_wrong': ['Forcing the scope against blanching tissue creates a false passage or full '
                                         'perforation and can end the procedure.',
                                         'Higher pressure drives more fluid through the tear into the floor of mouth, '
                                         'increasing swelling and airway risk.',
                                         'Laser energy without a visible lumen can perforate the duct and injure the '
                                         'lingual nerve nearby.',
                                         'Correct.'],
                           'board_pearl': 'During sialendoscopy, never push against resistance or blanching; stop, '
                                          'back off, and find the true lumen.',
                           'curveball': 'When should a combined transoral approach replace repeated attempts at purely '
                                        'endoscopic extraction?',
                           'curveball_answer': 'Convert to a combined approach when the stone is palpable but cannot '
                                               'be reached or captured endoscopically, when the duct is too narrow or '
                                               'kinked to pass safely, after a false passage, or when repeated basket '
                                               'attempts fail. Endoscopic transillumination guides a transoral '
                                               'incision directly over the stone, avoiding further instrumentation '
                                               'trauma.'},
 'v235_tps_sialendo_snr': {'stem': 'A 49-year-old woman has 2 years of recurrent left submandibular swelling with '
                                   'meals. Ultrasound shows a dilated proximal duct without stones and normal gland '
                                   'parenchyma. Sialendoscopy shows a single tight, white, 1-cm fibrotic stenosis of '
                                   'the proximal Wharton duct with normal ducts beyond it and no stones or mucus '
                                   'plugs. She has no sicca symptoms and negative SSA antibodies. Which treatment is '
                                   'most appropriate?',
                           'choices': ['Transcervical submandibular gland excision as the definitive therapy',
                                       'Endoscopic dilation with intraductal steroid and a temporary stent',
                                       'Long-term antibiotics with sialogogues, without addressing the stenosis',
                                       'Botulinum toxin to the gland as first-line therapy for the stenosis'],
                           'answer': 1,
                           'explanation': "Sialendoscopy defines the obstruction's phenotype: a single, short, focal "
                                          'stenosis with normal ducts beyond it has a good prognosis with '
                                          'duct-preserving therapy. Balloon or graded dilator dilation, intraductal '
                                          'steroid irrigation, and a temporary stent for several weeks to keep the '
                                          'lumen open relieve symptoms in most patients. Diffuse, multiple, or '
                                          'long-segment stenoses, systemic disease such as Sjogren, or prior radiation '
                                          'predict poorer durability. Gland excision is reserved for failure of these '
                                          'measures.',
                           'why_wrong': ['A focal stenosis in a functioning gland is often treatable through the duct; '
                                         'excision is reserved for refractory or diffuse disease.',
                                         'Correct.',
                                         'Antibiotics do not relieve a fixed stenosis, so obstructive symptoms and '
                                         'gland damage continue.',
                                         'Botulinum toxin reduces secretion but leaves the stenosis untreated and is '
                                         'reserved for refractory cases.'],
                           'board_pearl': 'Focal salivary duct stenosis in a functioning gland: endoscopic dilation, '
                                          'intraductal steroid, and stenting before excision.',
                           'curveball': 'If she later develops sicca symptoms and positive SSA, how would Sjogren '
                                        'disease change expectations for durable symptom control?',
                           'curveball_answer': 'Sjogren causes diffuse ductal inflammation and multiple stenoses, so '
                                               'sialendoscopic dilation and steroid irrigation often relieve symptoms '
                                               'only temporarily and may need repeating. Patients should be counseled '
                                               'about partial, sometimes short-lived benefit. Persistent asymmetric '
                                               'enlargement should still prompt evaluation for lymphoma.'},
 'v425-sialolithiasis-lithotripsy-indication-01': {'stem': 'A 41-year-old man has recurrent right submandibular '
                                                           'swelling with meals. Ultrasound shows a 6-mm stone in the '
                                                           'proximal Wharton duct near the hilum, not palpable '
                                                           'transorally. At sialendoscopy the stone is seen clearly '
                                                           'but is impacted in a dilated segment, and the basket '
                                                           'cannot be opened around it despite several gentle '
                                                           'attempts. The duct wall is intact. What is the most '
                                                           'appropriate next step?',
                                                   'choices': ['Firmer basket traction until the stone dislodges',
                                                               'Abandon endoscopy and proceed to gland excision in the '
                                                               'same sitting',
                                                               'Leave the basket engaged as a stent and retry '
                                                               'endoscopy next week',
                                                               'Intracorporeal holmium laser lithotripsy under '
                                                               'endoscopic vision'],
                                                   'answer': 3,
                                                   'explanation': 'A stone too large or impacted for basket capture is '
                                                                  'the classic indication for intracorporeal '
                                                                  'lithotripsy. A holmium laser fiber, or pneumatic '
                                                                  'device, is passed through the working channel and '
                                                                  'fires directly on the stone under vision, '
                                                                  'fragmenting it into pieces small enough to basket '
                                                                  'or irrigate out in the same session. This preserves '
                                                                  'the gland and avoids a transcervical incision. '
                                                                  'Continuous irrigation, keeping the fiber on the '
                                                                  'stone and off the duct wall, and a temporary stent '
                                                                  'afterward reduce perforation and stenosis risk.',
                                                   'why_wrong': ['Forceful traction on an impacted stone risks duct '
                                                                 'avulsion, perforation, or a trapped basket.',
                                                                 'Excision is premature when a gland-preserving '
                                                                 'fragmentation option is available and the duct is '
                                                                 'intact.',
                                                                 'A basket left in place does not function as a stent '
                                                                 'and can migrate or cause infection and injury.',
                                                                 'Correct.'],
                                                   'board_pearl': 'Impacted or too-large ductal stone at '
                                                                  'sialendoscopy: intracorporeal laser lithotripsy, '
                                                                  'then retrieve the fragments.',
                                                   'curveball': 'What historically limited extracorporeal shock wave '
                                                                "lithotripsy's role compared with intracorporeal "
                                                                'lithotripsy for salivary stones?',
                                                   'curveball_answer': 'ESWL is not FDA-cleared for salivary stones in '
                                                                       'the US, so availability is limited. It usually '
                                                                       'needs several sessions, cannot confirm '
                                                                       'complete clearance, and leaves fragments that '
                                                                       'must pass on their own, with lower success for '
                                                                       'submandibular stones. Intracorporeal '
                                                                       'lithotripsy fragments the stone under direct '
                                                                       'vision and allows immediate retrieval.'},
 'v137_tps_15': {'stem': 'A 55-year-old man with three years of recurrent right submandibular sialadenitis from an '
                         'intraparenchymal stone is scheduled for transcervical gland excision after sialendoscopy '
                         'failed. Facial, tongue, and lip function are normal. During consent he asks which nerves '
                         'could be injured and what each would affect. Which group of nerves is most at risk during '
                         'this operation?',
                 'choices': ['Marginal mandibular, lingual, and hypoglossal nerves',
                             'Marginal mandibular, glossopharyngeal, and accessory nerves',
                             'Great auricular, cervical, and lingual nerves',
                             'Buccal branch, inferior alveolar, and hypoglossal nerves'],
                 'answer': 0,
                 'explanation': 'Three nerves define the risk of submandibular gland excision. The marginal mandibular '
                                "branch of the facial nerve runs superficial to the gland's fascia, beneath the "
                                'platysma, and is protected by a low incision and ligating the facial vein low and '
                                'reflecting it upward. The lingual nerve lies superior and deep, attached to the gland '
                                'by the submandibular ganglion and looping beneath Wharton duct. The hypoglossal nerve '
                                'runs deep and inferior on the hyoglossus, beneath the digastric tendon. Injury causes '
                                'lower-lip weakness, tongue numbness and taste change, or tongue weakness, '
                                'respectively.',
                 'why_wrong': ['Correct.',
                               'The glossopharyngeal and spinal accessory nerves lie deep in the parapharyngeal space '
                               'and posterior triangle, away from this dissection.',
                               'The great auricular nerve is at risk in parotid surgery, not in submandibular '
                               'dissection near the mandible.',
                               'The buccal branch runs above the mandible in the cheek, and the inferior alveolar '
                               'nerve lies within the mandibular canal.'],
                 'board_pearl': 'Submandibular excision risks the marginal mandibular, lingual, and hypoglossal '
                                "nerves; know each one's plane.",
                 'curveball': 'How does chronic inflammation from long-standing stones change the dissection risk?',
                 'curveball_answer': 'Repeated infection causes periglandular fibrosis that fuses the gland to the '
                                     'mylohyoid, the lingual nerve, and the facial vessels, obscuring tissue planes. '
                                     'The lingual nerve may be tethered close to the gland and is easier to injure '
                                     'when the ganglion is divided. Careful identification of each nerve before '
                                     'dividing tissue, and bipolar cautery near nerves, reduce risk.'},
 'v146_tps_12': {'stem': 'A 49-year-old woman is undergoing left submandibular gland excision for chronic '
                         'sialadenitis. The gland is retracted inferiorly and the mylohyoid is retracted anteriorly, '
                         'exposing the deep surface. A broad, flat nerve is seen descending toward the gland, attached '
                         'to it by small branches through a ganglion, and then curving beneath Wharton duct toward the '
                         'tongue. Which nerve is this?',
                 'choices': ['Hypoglossal nerve', 'Nerve to mylohyoid', 'Lingual nerve', 'Glossopharyngeal nerve'],
                 'answer': 2,
                 'explanation': 'With the mylohyoid retracted anteriorly and the gland pulled down, the lingual nerve '
                                'appears as a broad, flat band descending toward the gland. It is tethered by the '
                                'submandibular ganglion, which carries parasympathetic fibers to the gland, and then '
                                'passes beneath Wharton duct from lateral to medial on its way to the tongue. Dividing '
                                'the ganglion between ligatures close to the gland lets the nerve spring upward and '
                                'away. Only then is the duct ligated and divided, avoiding tongue numbness and taste '
                                'loss.',
                 'why_wrong': ['The hypoglossal nerve lies lower on the hyoglossus, below the duct, and runs with the '
                               'ranine veins rather than to a ganglion.',
                               'The nerve to mylohyoid runs on the superficial surface of the mylohyoid muscle and '
                               'does not loop beneath the duct.',
                               'Correct.',
                               'The glossopharyngeal nerve stays deep to the hyoglossus near the tonsil bed and is not '
                               'seen in this dissection.'],
                 'board_pearl': 'Lingual nerve: tethered to the gland by the submandibular ganglion and looping '
                                'beneath Wharton duct; divide the ganglion first.',
                 'curveball': 'How do you protect the marginal mandibular nerve during the cervical approach?',
                 'curveball_answer': 'Place the incision about two fingerbreadths below the mandible in a skin crease, '
                                     'then incise the fascia over the gland low. Ligate the facial vein low on the '
                                     'gland and reflect it superiorly with the fascia (the Hayes Martin maneuver), '
                                     'which lifts the nerve away. Avoid aggressive traction and cautery near the '
                                     'mandibular border.'},
 'v235_tps_smgex_fnd': {'stem': 'A 61-year-old man had right submandibular gland excision 1 day ago for a chronically '
                                'infected gland. Tongue protrusion is midline, and tongue sensation and taste are '
                                'normal. When he smiles and bares his teeth, the right lower lip fails to depress, '
                                'giving an asymmetric smile, while forehead movement and eye closure are normal. Which '
                                'nerve was most likely injured?',
                        'choices': ['Cervical branch of the facial nerve',
                                    'Lingual nerve near the submandibular ganglion',
                                    'Marginal mandibular branch of the facial nerve',
                                    'Hypoglossal nerve on the hyoglossus muscle'],
                        'answer': 2,
                        'explanation': 'The marginal mandibular branch of the facial nerve supplies the depressor '
                                       'labii inferioris and depressor anguli oris. It runs beneath the platysma, '
                                       'superficial to the submandibular fascia, sometimes dipping below the '
                                       'mandibular border, and is the most frequently injured nerve in submandibular '
                                       'gland excision. Weakness produces an asymmetric smile because the lower lip '
                                       'cannot be depressed on that side. Most injuries are neurapraxia from traction '
                                       'or cautery and recover over weeks to months. A low incision and the Hayes '
                                       'Martin maneuver reduce risk.',
                        'why_wrong': ['Cervical branch injury weakens the platysma and can mimic lip asymmetry, but '
                                      'depressor labii inferioris function is typically preserved.',
                                      'Lingual nerve injury causes tongue numbness and loss of taste on the anterior '
                                      'two-thirds, which he does not have.',
                                      'Correct.',
                                      'Hypoglossal injury causes tongue deviation toward the side of surgery on '
                                      'protrusion, which is midline here.'],
                        'board_pearl': 'Asymmetric lower lip after submandibular surgery: marginal mandibular nerve, '
                                       'usually traction neurapraxia that recovers.',
                        'curveball': 'How does the facial artery relate to the gland and marginal mandibular nerve?',
                        'curveball_answer': 'The facial artery runs deep to the posterior gland, grooves its superior '
                                            'surface, and hooks over the mandible at the anterior border of the '
                                            'masseter, where the marginal mandibular nerve crosses superficial to it '
                                            'with the facial vein. Ligate the artery proximally near the posterior '
                                            "belly of the digastric and distally at the gland's superior border, "
                                            'keeping the nerve above and away from the ties.'},
 'v235_tps_smgex_app': {'stem': 'A 43-year-old woman had left submandibular gland excision 2 weeks ago for recurrent '
                                'sialadenitis. The operative note states that dense fibrosis tethered the gland deeply '
                                'and that the duct and ganglion were divided together with a single tie. She now '
                                'reports numbness of the left anterior tongue and altered taste on that side. Tongue '
                                'protrusion is midline and her smile is symmetric. Which structure was most likely '
                                'injured?',
                        'choices': ['Lingual nerve',
                                    'Hypoglossal nerve',
                                    'Chorda tympani in the middle ear',
                                    'Glossopharyngeal nerve'],
                        'answer': 0,
                        'explanation': 'The lingual nerve carries general sensation from the anterior two-thirds of '
                                       'the tongue and, through chorda tympani fibers that have joined it, taste. It '
                                       'is attached to the deep gland by the submandibular ganglion and loops beneath '
                                       'Wharton duct. Dividing the duct and ganglion together in a fibrotic field '
                                       'risks including the nerve in the tie. The safe sequence is to divide the '
                                       'ganglion close to the gland first, let the nerve retract upward, identify it '
                                       'clearly, and then ligate the duct separately.',
                        'why_wrong': ['Correct.',
                                      'Hypoglossal injury causes tongue weakness and deviation on protrusion, without '
                                      'sensory or taste loss.',
                                      'The chorda tympani carries taste but runs in the middle ear; it joins the '
                                      'lingual nerve far above the neck and was not exposed.',
                                      'Glossopharyngeal injury affects posterior-third tongue sensation and taste and '
                                      'pharyngeal sensation, not the anterior tongue.'],
                        'board_pearl': 'Anterior tongue numbness and taste loss after submandibular surgery: lingual '
                                       'nerve; divide the ganglion before the duct.',
                        'curveball': 'On examination, what deficit would indicate postoperative hypoglossal rather '
                                     'than lingual nerve injury in this patient?',
                        'curveball_answer': 'Hypoglossal injury causes ipsilateral tongue weakness: the tongue '
                                            'deviates toward the injured side on protrusion, and speech can be slurred '
                                            'with difficulty moving food, while sensation and taste are normal. '
                                            'Atrophy and fasciculations develop over weeks. Lingual injury causes '
                                            'numbness and taste loss without motor weakness.'},
 'v235_tps_smgex_snr': {'stem': 'A 58-year-old man has a firm, slightly fixed 3-cm right submandibular mass that has '
                                'grown over 4 months. Tongue movement and sensation are normal. Ultrasound-guided FNA '
                                'shows high-grade carcinoma, and MRI shows the mass confined to the gland with a '
                                '1.6-cm round, necrotic level IB node. There are no distant metastases on PET/CT. What '
                                'is the most appropriate surgical plan?',
                        'choices': ['Simple submandibular gland excision, as for chronic sialadenitis',
                                    'Primary chemoradiation, reserving surgery for residual disease',
                                    'Open incisional biopsy of the mass before deciding on treatment',
                                    'En bloc gland excision with neck dissection of levels I through III'],
                        'answer': 3,
                        'explanation': 'A suspected submandibular malignancy requires an oncologic operation rather '
                                       'than the routine excision used for sialadenitis. With high-grade carcinoma and '
                                       'a clinically positive level IB node, the plan is en bloc resection of the '
                                       'gland with surrounding tissue and a neck dissection of at least levels I '
                                       'through III, extended to IV and V if nodal burden warrants. The lingual and '
                                       'hypoglossal nerves, floor of mouth, and mandibular periosteum are assessed and '
                                       'resected if involved. Postoperative radiation is likely given the high grade '
                                       'and nodal disease.',
                        'why_wrong': ['A routine intracapsular gland excision without nodal dissection undertreats a '
                                      'high-grade carcinoma with a clinically positive node.',
                                      'Salivary carcinomas are treated primarily with surgery; chemoradiation is '
                                      'reserved for unresectable disease or adjuvant use.',
                                      'FNA has already shown carcinoma, and open incisional biopsy risks tumor spill '
                                      'and complicates the definitive resection.',
                                      'Correct.'],
                        'board_pearl': 'Submandibular carcinoma: en bloc gland resection with neck dissection, not a '
                                       'routine sialadenitis excision.',
                        'curveball': 'How would gross hypoglossal or lingual nerve invasion affect counseling and '
                                     'resection?',
                        'curveball_answer': 'A grossly invaded nerve is resected with the tumor, and frozen sections '
                                            'of proximal nerve margins are taken because of perineural spread, '
                                            'especially in adenoid cystic carcinoma. Counsel about permanent tongue '
                                            'weakness or numbness and taste loss. Nerve invasion also supports '
                                            'adjuvant radiation that covers the nerve pathway toward the skull base.'},
 'v137_tps_16': {'stem': 'A 58-year-old man with Graves disease has 3 months of worsening bilateral proptosis, eyelid '
                         'swelling, and diplopia on upgaze. Exam shows Hertel readings of 24 mm, upper lid retraction '
                         'with mild lagophthalmos, and restricted elevation of the right eye. Right visual acuity has '
                         'fallen to 20/50, he identifies 6 of 14 color plates, and there is a right relative afferent '
                         'pupillary defect. Which finding makes this an ophthalmic emergency?',
                 'choices': ['Upper eyelid retraction with mild lagophthalmos on closure',
                             'Reduced color vision with a relative afferent pupillary defect',
                             'Restrictive diplopia from a tight inferior rectus on upgaze',
                             'Proptosis of 24 mm measured on Hertel exophthalmometry'],
                 'answer': 1,
                 'explanation': 'Dysthyroid optic neuropathy is compression of the optic nerve at the orbital apex by '
                                'enlarged extraocular muscles. Its signs are color desaturation, decreased acuity, a '
                                'relative afferent pupillary defect, visual field loss, and optic disc swelling, '
                                'sometimes with only moderate proptosis. It threatens permanent vision loss and '
                                'requires same-day ophthalmology evaluation. First-line treatment is high-dose IV '
                                'methylprednisolone, with urgent orbital decompression of the medial wall and floor if '
                                'vision does not improve within about 1 to 2 weeks. Corneal breakdown from severe '
                                'exposure is the other sight-threatening emergency.',
                 'why_wrong': ['Lid retraction with mild lagophthalmos causes exposure symptoms treated with '
                               'lubrication, but does not by itself threaten vision.',
                               'Correct.',
                               'Restrictive diplopia is disabling but not sight-threatening; strabismus is managed '
                               'after the disease becomes inactive.',
                               'The degree of proptosis does not predict optic nerve compression, which can occur with '
                               'only modest proptosis.'],
                 'board_pearl': 'TED with color desaturation, RAPD, or acuity loss is compressive optic neuropathy, a '
                                'sight-threatening emergency.',
                 'curveball': 'He still smokes a pack a day. Why is smoking cessation especially important in thyroid '
                              'eye disease?',
                 'curveball_answer': 'Smoking is the strongest modifiable risk factor. It increases the risk of '
                                     'developing TED, its severity, and its progression after radioiodine, and it '
                                     'reduces response to steroids and orbital radiation. Cessation lowers these '
                                     'risks, so it should be advised and supported at every visit for patients with '
                                     'Graves disease.'},
 'v146_tps_13': {'stem': 'A 63-year-old woman with Graves disease, on methimazole and euthyroid, has 6 weeks of '
                         'painful proptosis, chemosis, and eyelid edema. Over 3 days her left acuity has fallen from '
                         '20/25 to 20/80 with marked color desaturation and a left relative afferent pupillary defect. '
                         'CT shows enlarged rectus muscles crowding the left orbital apex. Her glucose is controlled '
                         'on metformin. What is the most appropriate initial treatment?',
                 'choices': ['Total thyroidectomy now to remove the autoimmune antigen source from the patient',
                             'Orbital radiotherapy as the sole initial therapy, given her diabetes and age',
                             'Selenium supplementation, lubricants, and prisms with follow-up in 6 weeks',
                             'IV methylprednisolone pulses, with urgent decompression if vision fails to improve'],
                 'answer': 3,
                 'explanation': 'Painful proptosis, chemosis, and new vision loss with color desaturation and an '
                                'afferent pupillary defect indicate active thyroid eye disease with compressive optic '
                                'neuropathy. This requires urgent coordinated care with ophthalmology and '
                                'endocrinology. European guidance recommends high-dose IV methylprednisolone pulses as '
                                'first-line therapy, with close monitoring of vision and glucose. If optic nerve '
                                'function does not improve within about 1 to 2 weeks, or worsens, urgent orbital '
                                'decompression of the medial wall and floor relieves apical crowding. Thyroid function '
                                'should be kept stable.',
                 'why_wrong': ['Thyroidectomy controls hyperthyroidism but does not decompress the optic nerve or '
                               'treat orbital inflammation in time.',
                               'Radiotherapy works slowly over weeks and is an adjunct; it cannot reverse acute optic '
                               'nerve compression alone.',
                               'Selenium helps only mild disease; supportive care with delayed follow-up risks '
                               'permanent vision loss here.',
                               'Correct.'],
                 'board_pearl': 'Dysthyroid optic neuropathy: IV methylprednisolone first; urgent orbital '
                                'decompression if vision does not respond quickly.',
                 'curveball': 'How does active inflammatory disease affect the timing of orbital decompression versus '
                              'rehabilitative surgery?',
                 'curveball_answer': 'During active disease, decompression is reserved for emergencies such as optic '
                                     'neuropathy or severe corneal exposure. Elective rehabilitative decompression, '
                                     'strabismus surgery, and eyelid surgery wait until the disease has been inactive '
                                     'and stable for about 6 months, because ongoing inflammation makes outcomes '
                                     'unpredictable.'},
 'v237_tps_ted_fnd': {'stem': 'A 40-year-old woman with newly diagnosed Graves hyperthyroidism and strongly positive '
                              'TSH-receptor antibodies has gritty eyes, bilateral proptosis, and stare. Orbital CT '
                              'shows enlarged extraocular muscle bellies and increased orbital fat. A resident asks '
                              'how the autoimmune thyroid disease produces these orbital changes. Which mechanism best '
                              'explains them?',
                      'choices': ['Excess free thyroxine directly stimulating extraocular muscle growth',
                                  'Antibody activation of orbital fibroblasts via TSH and IGF-1 receptors',
                                  'Venous congestion from a carotid-cavernous fistula raising pressure',
                                  'Lymphocytic infiltration confined to the lacrimal gland bilaterally'],
                      'answer': 1,
                      'explanation': 'Thyroid eye disease is an autoimmune orbital disorder. TSH-receptor antibodies '
                                     'and IGF-1 receptor signaling activate orbital fibroblasts, which produce '
                                     'hydrophilic glycosaminoglycans such as hyaluronan and differentiate into '
                                     'adipocytes. Water-binding glycosaminoglycans swell the extraocular muscle '
                                     'bellies, typically sparing the tendons, and expand orbital fat. Within the bony '
                                     'orbit this causes proptosis, restrictive diplopia, exposure, and, at the apex, '
                                     'optic nerve compression. Lid retraction also reflects sympathetic overactivity '
                                     'and levator fibrosis. This explains why IGF-1 receptor blockade with '
                                     'teprotumumab reduces proptosis.',
                      'why_wrong': ['Eye disease can occur in euthyroid or hypothyroid patients and does not track '
                                    'thyroid hormone levels, so hormone excess is not the cause.',
                                    'Correct.',
                                    'A carotid-cavernous fistula causes pulsatile proptosis, a bruit, and dilated '
                                    'superior ophthalmic veins, not symmetric muscle enlargement.',
                                    'Isolated lacrimal infiltration suggests sarcoid or IgG4 disease and would not '
                                    'enlarge the extraocular muscles.'],
                      'board_pearl': 'TED: TSH-receptor and IGF-1R activation of orbital fibroblasts expands muscles '
                                     'and fat in a fixed bony orbit.',
                      'curveball': 'Which symptoms should she be told suggest sight-threatening disease requiring '
                                   'urgent ophthalmologic evaluation?',
                      'curveball_answer': 'Urgent evaluation is needed for blurred or decreased vision, colors '
                                          'appearing washed out, a new visual field defect, or an afferent pupillary '
                                          'defect, all suggesting optic neuropathy. Severe eye pain, inability to '
                                          'close the eyes, or a white corneal opacity suggests exposure keratopathy or '
                                          'ulceration. Sudden globe subluxation is also an emergency.'},
 'v237_tps_ted_app': {'stem': 'A 66-year-old man with diabetes, a 40-pack-year smoking history, and Graves disease has '
                              'had 2 months of blurred vision in the right eye. Hertel readings are only 18 mm '
                              'bilaterally, and there is no lagophthalmos. Right acuity is 20/60 with color '
                              'desaturation and a right relative afferent pupillary defect. The cornea is clear and '
                              'the retina shows no edema. CT shows enlarged muscles crowding the orbital apex. What is '
                              'the most likely cause of his vision loss?',
                      'choices': ['Exposure keratopathy from eyelid retraction',
                                  'Diabetic macular edema in the affected eye',
                                  'Compressive optic neuropathy at the orbital apex',
                                  'Nonarteritic anterior ischemic optic neuropathy'],
                      'answer': 2,
                      'explanation': 'Dysthyroid optic neuropathy does not require marked proptosis. Patients with a '
                                     'tight orbital septum or limited forward displacement of the globe, often older '
                                     'men, smokers, and diabetics, can compress the optic nerve at the apex with only '
                                     'modest proptosis because the orbit cannot decompress itself forward. Color '
                                     'desaturation, reduced acuity, an afferent pupillary defect, and apical crowding '
                                     'on CT make this a sight-threatening emergency. Treatment is urgent IV '
                                     'methylprednisolone with orbital decompression if vision does not respond '
                                     'quickly.',
                      'why_wrong': ['His cornea is clear and there is no lagophthalmos, so exposure does not explain '
                                    'the acuity loss and afferent defect.',
                                    'Macular edema would be seen on retinal exam and does not cause an afferent '
                                    'pupillary defect at this level.',
                                    'Correct.',
                                    'Ischemic optic neuropathy is sudden and painless with disc edema, and it would '
                                    'not explain apical crowding on CT.'],
                      'board_pearl': 'Optic neuropathy can occur with minimal proptosis; apical crowding, color loss, '
                                     'and RAPD drive urgent treatment.',
                      'curveball': 'Besides optic nerve compression, how does corneal breakdown create a second '
                                   'sight-threatening pathway in thyroid eye disease?',
                      'curveball_answer': 'Severe proptosis and lid retraction prevent complete closure, causing '
                                          'exposure keratopathy that can progress to corneal ulceration, infection, '
                                          'and perforation. Treatment escalates from frequent lubricants and nighttime '
                                          'moisture chambers to tarsorrhaphy and, if needed, urgent orbital '
                                          'decompression to reduce proptosis and allow lid closure.'},
 'v237_tps_ted_snr': {'stem': 'A 48-year-old woman with Graves disease has disfiguring proptosis, constant diplopia in '
                              'primary gaze, and upper lid retraction. Her clinical activity score is 4 of 7 with '
                              'painful eye movements and chemosis, and her measurements changed over the past 2 '
                              'months. Vision and color are normal. She asks to have all of her eye operations done '
                              'together now. What is the best plan?',
                      'choices': ['Control activity, then staged decompression, strabismus, then eyelids',
                                  'Eyelid surgery first, then strabismus surgery, then orbital decompression',
                                  'Strabismus surgery now, then decompression after stability',
                                  'Combined decompression, strabismus, and eyelid surgery at one sitting now'],
                      'answer': 0,
                      'explanation': 'Rehabilitative surgery is most predictable after the inflammatory phase has '
                                     'settled and measurements have been stable, usually for about 6 months. Her '
                                     'active disease, with a clinical activity score of 4, should first be treated '
                                     'medically, for example with IV methylprednisolone or teprotumumab, plus smoking '
                                     'cessation and stable thyroid function. Surgery is then staged because each step '
                                     'affects the next: orbital decompression changes globe position and can induce '
                                     'diplopia, strabismus surgery then aligns the eyes, and eyelid surgery comes last '
                                     'to fine-tune lid height and retraction.',
                      'why_wrong': ['Correct.',
                                    'Decompression changes globe position and muscle balance, so lid and strabismus '
                                    'results achieved first would be undone.',
                                    'Strabismus surgery during active disease gives unpredictable results, and '
                                    'decompression afterward can create new diplopia.',
                                    'Operating during active, changing disease gives unpredictable results and does '
                                    'not allow each stage to inform the next.'],
                      'board_pearl': 'TED rehabilitation: quiet the disease, then decompression, then strabismus, then '
                                     'eyelid surgery.',
                      'curveball': 'When is urgent orbital decompression appropriate even while her disease is still '
                                   'active?',
                      'curveball_answer': 'Urgent decompression is appropriate during active disease for compressive '
                                          'optic neuropathy that does not respond to IV steroids within about 1 to 2 '
                                          'weeks, for severe exposure keratopathy or corneal ulceration not controlled '
                                          'by medical measures and tarsorrhaphy, and for globe subluxation. These '
                                          'sight-threatening indications override the usual wait for inactivity.'},
 'v431-subacute-thyroiditis-01': {'stem': 'A 45-year-old woman has 2 weeks of anterior neck pain radiating to the jaw, '
                                          'low-grade fever, palpitations, and tremor, beginning 3 weeks after an upper '
                                          'respiratory infection. The thyroid is firm and exquisitely tender without '
                                          'fluctuance. Free T4 is elevated, TSH suppressed, ESR 82 mm/h, and 24-hour '
                                          'radioiodine uptake is 2%. Heart rate is 108. What is the best initial '
                                          'management?',
                                  'choices': ['Propranolol plus an NSAID such as naproxen',
                                              'Methimazole with propranolol until euthyroid',
                                              'Radioactive iodine ablation',
                                              'IV antibiotics and ultrasound-guided drainage'],
                                  'answer': 0,
                                  'explanation': 'A painful tender gland after a viral illness, high ESR, '
                                                 'thyrotoxicosis, and very low radioiodine uptake are the classic '
                                                 'pattern of subacute granulomatous (de Quervain) thyroiditis. '
                                                 'Inflammation destroys follicles and releases stored hormone; '
                                                 'synthesis is actually suppressed. Treatment is symptomatic: a beta '
                                                 'blocker for adrenergic symptoms and an NSAID for pain. Prednisone, '
                                                 'typically about 40 mg daily tapered over several weeks, is used for '
                                                 'severe pain or failure of NSAIDs. Antithyroid drugs and radioiodine '
                                                 'have no role.',
                                  'why_wrong': ['Correct.',
                                                'Methimazole blocks new hormone synthesis, but this thyrotoxicosis '
                                                'comes from release of stored hormone, so it does not help.',
                                                'With near-zero uptake, the gland cannot take up radioiodine, and the '
                                                'thyrotoxicosis is self-limited anyway.',
                                                'There is no fluctuance or abscess, and the low uptake and high ESR '
                                                'fit granulomatous thyroiditis rather than bacterial infection.'],
                                  'board_pearl': 'De Quervain thyroiditis: beta blocker plus NSAID; prednisone if '
                                                 'severe; antithyroid drugs and radioiodine do not help.',
                                  'curveball': 'When should surgery be reconsidered in a patient with presumed '
                                               'subacute thyroiditis?',
                                  'curveball_answer': 'Surgery has no routine role, but reconsider the diagnosis if a '
                                                      'fluctuant collection suggests acute suppurative thyroiditis '
                                                      'needing drainage, if a persistent focal nodule remains after '
                                                      'the inflammation resolves and needs FNA, or if compressive '
                                                      'symptoms progress. Rarely, recurrent painful episodes '
                                                      'refractory to medical therapy have been treated with '
                                                      'thyroidectomy.'},
 'v431-subacute-thyroiditis-02': {'stem': 'A 39-year-old woman was diagnosed with subacute thyroiditis 9 weeks ago, '
                                          'when she had a painful gland and thyrotoxicosis; she was treated with '
                                          'naproxen and propranolol and her pain resolved. She now has fatigue, cold '
                                          'intolerance, and constipation. The thyroid is nontender. TSH is 14 mU/L and '
                                          'free T4 is low. What is the most accurate interpretation and plan?',
                                  'choices': ['Permanent autoimmune hypothyroidism needing lifelong levothyroxine',
                                              'Relapsing thyroiditis with recurrent thyrotoxicosis needing steroids',
                                              'Expected transient hypothyroid phase; treat symptoms and recheck',
                                              'Central hypothyroidism from pituitary damage, needing MRI of the sella'],
                                  'answer': 2,
                                  'explanation': 'Subacute thyroiditis follows a predictable course. Inflammatory '
                                                 'follicular destruction first releases stored hormone, causing 4 to 8 '
                                                 'weeks of thyrotoxicosis. Once stores are depleted and the gland is '
                                                 'still recovering, a transient hypothyroid phase follows, often '
                                                 'lasting weeks to a few months. Most patients then return to normal '
                                                 'function; only a minority develop permanent hypothyroidism. '
                                                 'Symptomatic patients like her can take levothyroxine for several '
                                                 'months, then taper while TSH is rechecked to see whether the gland '
                                                 'has recovered.',
                                  'why_wrong': ['Most patients recover normal function within months; permanent '
                                                'hypothyroidism develops in only a minority.',
                                                'Her TSH is high and free T4 low, which is hypothyroidism, not '
                                                'thyrotoxicosis, and the gland is no longer painful.',
                                                'Correct.',
                                                'A high TSH with low free T4 indicates a primary thyroid cause; '
                                                'central hypothyroidism would have a low or normal TSH.'],
                                  'board_pearl': 'Subacute thyroiditis course: thyrotoxic, then transient hypothyroid, '
                                                 'then usually full recovery.',
                                  'curveball': 'Had her pain not settled on naproxen, what would determine whether '
                                               'corticosteroids should be used instead of NSAIDs?',
                                  'curveball_answer': 'Corticosteroids are used for severe pain, high fever, marked '
                                                      'systemic symptoms, or failure of an adequate NSAID trial after '
                                                      'several days. Prednisone, about 40 mg daily, gives dramatic '
                                                      'relief within 1 to 2 days and is tapered over 4 to 8 weeks. '
                                                      'Recurrence during the taper is common, and steroids do not '
                                                      'prevent the later hypothyroid phase.'},
 'v461_tps_dequervain_fnd': {'stem': 'A 34-year-old woman has a 10-day history of painful swelling in the front of her '
                                     'neck, worse with swallowing, beginning two weeks after an upper respiratory '
                                     'illness. She has a temperature of 37.9 C, palpitations, and mild heat '
                                     'intolerance. The thyroid is diffusely firm and very tender without fluctuance or '
                                     'skin erythema. ESR is 74 mm/h, and she has no prior thyroid history. What is the '
                                     'most likely diagnosis?',
                             'choices': ['Graves disease',
                                         'Subacute granulomatous thyroiditis',
                                         'Acute suppurative thyroiditis',
                                         'Painless (silent) thyroiditis'],
                             'answer': 1,
                             'explanation': 'A painful, tender gland after a viral illness, with fever, thyrotoxic '
                                            'symptoms, and a markedly elevated ESR, is the classic presentation of '
                                            'subacute granulomatous (de Quervain) thyroiditis. Inflammation disrupts '
                                            'follicles and releases stored hormone, so thyrotoxicosis is destructive '
                                            'rather than from excess synthesis, and radioiodine uptake is low. '
                                            'Histology shows granulomatous inflammation with multinucleated giant '
                                            'cells. The course is self-limited: thyrotoxicosis, a transient '
                                            'hypothyroid phase, then recovery in most patients. Pain and inflammatory '
                                            'markers distinguish it from painless thyroiditis and Graves disease.',
                             'why_wrong': ['Graves disease causes a painless diffuse goiter, often with eye signs, and '
                                           'does not raise the ESR this much.',
                                           'Correct.',
                                           'Suppurative thyroiditis is usually unilateral and fluctuant with red skin '
                                           'and toxicity, often from a left pyriform sinus fistula.',
                                           'Painless thyroiditis, often postpartum, causes thyrotoxicosis without '
                                           'gland tenderness or a high ESR.'],
                             'board_pearl': 'Tender thyroid, post-viral, high ESR, thyrotoxic: subacute granulomatous '
                                            'thyroiditis, with low radioiodine uptake.',
                             'curveball': 'What basic labs and inflammatory markers should be checked first in this '
                                          'patient?',
                             'curveball_answer': 'Check TSH, free T4, and total or free T3 to define thyroid status, '
                                                 'plus ESR or CRP, which are typically markedly elevated. A CBC may '
                                                 'show mild leukocytosis. Radioiodine uptake, low in thyroiditis, or '
                                                 'Doppler ultrasound showing reduced flow can confirm the diagnosis if '
                                                 'Graves disease is still in question.'},
 'v461_tps_dequervain_app': {'stem': 'A 37-year-old woman has 3 weeks of palpitations, weight loss, and mild anterior '
                                     'neck discomfort. The thyroid is diffusely enlarged and only mildly tender. She '
                                     'has no eye signs. Free T4 is elevated, TSH suppressed, ESR 38 mm/h, and anti-TPO '
                                     'antibodies are positive. TSH-receptor antibody results will take a week. Her '
                                     'physician must decide between Graves disease and subacute thyroiditis before '
                                     'treating. Which test best discriminates now?',
                             'choices': ['Anti-thyroid peroxidase antibody titer',
                                         'Serum thyroglobulin concentration',
                                         'Fine-needle aspiration of the gland',
                                         'Radioactive iodine uptake measurement'],
                             'answer': 3,
                             'explanation': 'Radioiodine uptake separates thyrotoxicosis from increased synthesis from '
                                            'thyrotoxicosis from hormone leakage. In Graves disease, TSH-receptor '
                                            'stimulation drives uptake high and diffuse. In subacute thyroiditis, '
                                            'damaged follicles leak stored hormone and the suppressed gland takes up '
                                            'very little iodine. The distinction changes management directly: '
                                            'antithyroid drugs or radioiodine treat Graves disease, while thyroiditis '
                                            'needs only beta blockade and anti-inflammatory therapy. Doppler '
                                            'ultrasound showing increased or reduced flow is an alternative when '
                                            'uptake testing is unavailable or contraindicated, such as in pregnancy.',
                             'why_wrong': ['TPO antibodies are common in Graves disease and can be transiently '
                                           'positive in subacute thyroiditis, so a titer does not separate them.',
                                           'Thyroglobulin is elevated in both conditions; a low level mainly helps '
                                           'identify factitious thyrotoxicosis.',
                                           'Diffuse thyroid disease does not need cytology, and FNA does not reliably '
                                           'distinguish these two diagnoses.',
                                           'Correct.'],
                             'board_pearl': 'Thyrotoxicosis with high radioiodine uptake suggests Graves disease; low '
                                            'uptake suggests destructive thyroiditis.',
                             'curveball': 'The uptake study confirms de Quervain thyroiditis. She has significant '
                                          'adrenergic symptoms and gland pain. How should these be managed?',
                             'curveball_answer': 'Treat adrenergic symptoms with a beta blocker such as propranolol, '
                                                 'titrated to heart rate and tremor. Treat pain with an NSAID first. '
                                                 'If pain is severe or does not respond within several days, use '
                                                 'prednisone, about 40 mg daily, tapered over 4 to 8 weeks. Monitor '
                                                 'for the later hypothyroid phase.'},
 'v461_tps_dequervain_snr': {'stem': 'A 48-year-old woman had typical de Quervain thyroiditis 3 months ago with '
                                     'diffuse tenderness, high ESR, and low uptake, treated with naproxen. Her pain, '
                                     'ESR, and thyroid function have all normalized. Follow-up ultrasound shows the '
                                     'diffuse changes have resolved, but a 1.8-cm solid, hypoechoic, '
                                     'irregular-margined nodule persists in the right lobe. The nodule is nontender. '
                                     'What is the most appropriate next step?',
                             'choices': ['Restart prednisone for presumed smoldering thyroiditis',
                                         'Ultrasound-guided FNA of the persistent focal nodule',
                                         'Reassurance and repeat ultrasound in two years',
                                         'Total thyroidectomy for a presumed thyroid malignancy'],
                             'answer': 1,
                             'explanation': 'Subacute thyroiditis can produce ill-defined hypoechoic areas that mimic '
                                            'cancer, but these should resolve with the inflammation. When the clinical '
                                            'course, ESR, and thyroid function have normalized and a focal lesion '
                                            'persists, the diagnosis must be reopened. A solid, hypoechoic, '
                                            'irregular-margined nodule of this size meets FNA criteria regardless of '
                                            'the earlier thyroiditis. Cytology can identify papillary carcinoma or '
                                            'other pathology that was masked by the inflammatory episode. The '
                                            'thyroiditis itself has no surgical role.',
                             'why_wrong': ['Her inflammation has resolved clinically and biochemically, so a '
                                           'persistent focal lesion should not be treated as ongoing thyroiditis.',
                                           'Correct.',
                                           'A solid hypoechoic irregular nodule is high suspicion by ultrasound '
                                           'criteria and should not wait two years.',
                                           'Surgery without tissue diagnosis is premature; FNA can establish whether '
                                           'this is malignant before choosing extent of surgery.'],
                             'board_pearl': 'Thyroiditis changes should resolve; a persistent suspicious focal nodule '
                                            'afterward needs FNA on its own merits.',
                             'curveball': 'What specific findings, beyond a persistent focal lesion, should make a '
                                          'clinician reconsider the diagnosis during follow-up of presumed subacute '
                                          'thyroiditis?',
                             'curveball_answer': 'Reconsider the diagnosis if pain is strictly unilateral with '
                                                 'fluctuance, skin erythema, or high fever, which suggests suppurative '
                                                 'thyroiditis, especially with a left pyriform sinus fistula. Also '
                                                 'reconsider with rapid growth or compressive symptoms, which raise '
                                                 'concern for lymphoma or anaplastic carcinoma, failure to improve '
                                                 'with steroids, recurrent episodes, or high uptake on scanning.'},
 'v431-hashimoto-thyroiditis-01': {'stem': 'A 68-year-old woman with Hashimoto thyroiditis on stable levothyroxine has '
                                           '5 weeks of rapid, painless enlargement of the right side of her neck with '
                                           'mild dysphagia and voice change. Exam shows a firm 5-cm right thyroid '
                                           'mass. Ultrasound shows a markedly hypoechoic, pseudocystic-appearing mass '
                                           'with posterior acoustic enhancement within a heterogeneous gland. There is '
                                           'no stridor. What is the most appropriate next step?',
                                   'choices': ['Increase levothyroxine and repeat the neck ultrasound in 3 months',
                                               'Routine FNA cytology alone, with surgery only if malignant',
                                               'Total thyroidectomy as combined diagnosis and treatment',
                                               'Core needle biopsy with flow cytometry for possible lymphoma'],
                                   'answer': 3,
                                   'explanation': 'Primary thyroid lymphoma arises almost always in glands with '
                                                  'chronic lymphocytic thyroiditis, typically in older women, and '
                                                  'presents as rapid, painless enlargement. Ultrasound often shows a '
                                                  'markedly hypoechoic mass with posterior enhancement that can look '
                                                  'cystic. A focal, rapidly growing mass must be evaluated on its own '
                                                  'merits, not attributed to Hashimoto disease. Core needle biopsy '
                                                  'preserves architecture, and flow cytometry, immunohistochemistry, '
                                                  'and gene rearrangement studies distinguish diffuse large B-cell '
                                                  'from MALT lymphoma, which determines treatment. Anaplastic '
                                                  'carcinoma is the other key differential.',
                                   'why_wrong': ['Rapid growth of a focal mass is not explained by Hashimoto disease, '
                                                 'and waiting delays treatment of a possible lymphoma.',
                                                 'FNA cytology alone often cannot subtype lymphoma or distinguish it '
                                                 'from florid lymphocytic thyroiditis.',
                                                 'Lymphoma is treated without surgery; thyroidectomy adds morbidity '
                                                 'before the diagnosis is known.',
                                                 'Correct.'],
                                   'board_pearl': 'Rapidly enlarging mass in a Hashimoto gland: suspect lymphoma; get '
                                                  'core biopsy with flow cytometry.',
                                   'curveball': 'Before the mass appeared, what labs and imaging would have supported '
                                                'her baseline diagnosis of Hashimoto thyroiditis?',
                                   'curveball_answer': 'TSH and free T4 define thyroid function, and anti-TPO '
                                                       'antibodies, positive in most patients, support autoimmune '
                                                       'thyroiditis, with anti-thyroglobulin antibodies adding a '
                                                       'little. Ultrasound shows a diffusely enlarged or atrophic '
                                                       'gland with heterogeneous, hypoechoic echotexture, fibrous '
                                                       'septa, and sometimes pseudonodules. Biopsy is not needed for '
                                                       'diffuse disease.'},
 'v431-hashimoto-thyroiditis-02': {'stem': 'A 35-year-old woman has 6 months of fatigue, weight gain, and dry skin. '
                                           'Exam shows a painless, firm, symmetric, finely bosselated goiter without '
                                           'dominant nodules. TSH is 9.8 mU/L with a low-normal free T4. Her mother '
                                           'has type 1 diabetes and her sister has vitiligo. Ultrasound shows a '
                                           'diffusely heterogeneous, hypoechoic gland. Which test best supports the '
                                           'underlying diagnosis?',
                                   'choices': ['Anti-thyroid peroxidase antibodies',
                                               'TSH-receptor stimulating antibodies',
                                               'Twenty-four-hour radioiodine uptake',
                                               'Serum calcitonin and CEA levels'],
                                   'answer': 0,
                                   'explanation': 'Hashimoto thyroiditis is chronic autoimmune lymphocytic '
                                                  'thyroiditis. T-cell and antibody-mediated injury, with '
                                                  'lymphoplasmacytic infiltration, germinal centers, and Hurthle cell '
                                                  'change, progressively destroys follicles, producing a firm goiter '
                                                  'or, later, an atrophic gland. TSH and free T4 define function, here '
                                                  'subclinical hypothyroidism. Anti-TPO antibodies are positive in '
                                                  'most patients and confirm the autoimmune cause and the higher risk '
                                                  'of progression to overt hypothyroidism. Ultrasound shows diffuse '
                                                  'heterogeneity. A family history of autoimmune disease is common.',
                                   'why_wrong': ['Correct.',
                                                 'TSH-receptor stimulating antibodies indicate Graves disease and '
                                                 'would not explain a rising TSH with hypothyroid symptoms.',
                                                 'Uptake testing is used to evaluate thyrotoxicosis, not '
                                                 'hypothyroidism, and does not confirm autoimmune thyroiditis.',
                                                 'Calcitonin and CEA evaluate medullary carcinoma, which does not '
                                                 'cause a diffuse hypothyroid goiter.'],
                                   'board_pearl': 'Hashimoto: TSH and free T4 define function; anti-TPO antibodies '
                                                  'confirm the autoimmune cause.',
                                   'curveball': 'She asks whether she will ever need her thyroid removed. When is '
                                                'surgery indicated in Hashimoto thyroiditis?',
                                   'curveball_answer': 'Surgery is not used to treat the thyroiditis itself. It is '
                                                       'indicated for a compressive goiter causing dysphagia, dyspnea, '
                                                       'or tracheal narrowing, for a nodule with suspicious or '
                                                       'malignant cytology, and occasionally for persistent pain or '
                                                       'cosmesis. Suspected lymphoma is diagnosed by core biopsy and '
                                                       'treated without thyroidectomy.'},
 'v461_tps_hashimoto_fnd': {'stem': 'A 45-year-old woman is found on a routine visit to have a painless, firm, '
                                    'rubbery, diffusely enlarged thyroid without discrete nodules. She reports a year '
                                    'of fatigue, cold intolerance, constipation, and heavier periods. TSH is 24 mU/L '
                                    'and free T4 is low. She has no neck pain, fever, or recent pregnancy. What is the '
                                    'most likely diagnosis?',
                            'choices': ['Subacute (de Quervain) granulomatous thyroiditis',
                                        'Graves disease in its early hypothyroid phase',
                                        'Hashimoto (chronic lymphocytic) thyroiditis',
                                        'Riedel (invasive fibrous) thyroiditis'],
                            'answer': 2,
                            'explanation': 'Hashimoto thyroiditis is the most common cause of hypothyroidism in '
                                           'iodine-sufficient regions. It typically presents in middle-aged women with '
                                           'a painless, firm, rubbery, diffuse goiter and gradual hypothyroid '
                                           'symptoms, or with incidental lab findings. Chronic autoimmune lymphocytic '
                                           'injury progressively destroys follicles, and the gland may be goitrous or '
                                           'eventually atrophic. A high TSH with low free T4 indicates overt primary '
                                           'hypothyroidism. Anti-TPO antibodies confirm the cause, and ultrasound '
                                           'typically shows heterogeneous, hypoechoic echotexture.',
                            'why_wrong': ['De Quervain thyroiditis causes a painful, tender gland with fever and a '
                                          'high ESR, which she does not have.',
                                          'Graves disease causes hyperthyroidism from TSH-receptor stimulation, not a '
                                          'high TSH with low free T4.',
                                          'Correct.',
                                          'Riedel thyroiditis causes a rock-hard, fixed gland with compressive '
                                          'symptoms, and is rare.'],
                            'board_pearl': 'Painless firm rubbery goiter with high TSH and low free T4 in a '
                                           'middle-aged woman: Hashimoto thyroiditis.',
                            'curveball': "What is the recommended treatment for this patient's overt hypothyroidism, "
                                         'and how is the dose monitored?',
                            'curveball_answer': 'Levothyroxine replacement, starting near the full weight-based dose '
                                                'of about 1.6 mcg/kg/day in a healthy younger adult, or lower in older '
                                                'or cardiac patients. Take it on an empty stomach, apart from calcium '
                                                'and iron, and recheck TSH in 6 to 8 weeks, titrating to a normal '
                                                'TSH.'},
 'v461_tps_hashimoto_app': {'stem': 'A 52-year-old woman with long-standing Hashimoto thyroiditis on a stable '
                                    'levothyroxine dose has a routine ultrasound for neck fullness. Within her '
                                    'diffusely heterogeneous gland is a new, discrete 1.6-cm solid, markedly '
                                    'hypoechoic nodule with irregular margins and punctate echogenic foci. It has not '
                                    'grown rapidly, and she has no compressive symptoms. TSH is normal. What is the '
                                    'most appropriate next step?',
                            'choices': ['Increase levothyroxine to shrink the nodule',
                                        'Repeat ultrasound in two years as a pseudonodule',
                                        'Ultrasound-guided FNA of the dominant nodule',
                                        'Core needle biopsy with flow cytometry for lymphoma'],
                            'answer': 2,
                            'explanation': 'Diffuse heterogeneity from Hashimoto disease is not an indication for '
                                           'biopsy, but a discrete nodule must be risk-stratified on its own merits. '
                                           'This nodule is solid, markedly hypoechoic, irregular, and contains '
                                           'punctate echogenic foci, making it highly suspicious by ACR TI-RADS, and '
                                           'at 1.6 cm it meets FNA size thresholds. Chronic lymphocytic thyroiditis '
                                           'does not protect against papillary carcinoma, which is commonly found in '
                                           'Hashimoto glands. Cytology may show a lymphocytic background, which the '
                                           'pathologist should be told about.',
                            'why_wrong': ['TSH suppression does not reliably shrink nodules and would not answer '
                                          'whether this nodule is malignant.',
                                          'Hashimoto pseudonodules are ill-defined and blend into the background; this '
                                          'discrete, suspicious nodule needs evaluation.',
                                          'Correct.',
                                          'Without rapid growth or a lymphoma-type appearance, the concern is '
                                          'papillary carcinoma, which FNA diagnoses well.'],
                            'board_pearl': 'A discrete suspicious nodule in a Hashimoto gland is evaluated by TI-RADS '
                                           'and FNA, not dismissed as thyroiditis.',
                            'curveball': 'Ultrasound a year later shows the dominant area markedly enlarged compared '
                                         'with prior imaging. What diagnosis should be urgently considered, and how is '
                                         'it worked up?',
                            'curveball_answer': 'Rapid enlargement in a Hashimoto gland raises concern for primary '
                                                'thyroid lymphoma, usually diffuse large B-cell or MALT type, as well '
                                                'as anaplastic carcinoma. Obtain urgent core needle biopsy with flow '
                                                'cytometry and immunohistochemistry, assess the airway, and stage with '
                                                'PET/CT if lymphoma is confirmed.'},
 'v461_tps_hashimoto_snr': {'stem': 'A 70-year-old woman with Hashimoto thyroiditis has a large goiter with '
                                    'progressive dysphagia and neck pressure but no stridor; CT shows the trachea '
                                    'mildly narrowed. Core biopsy of a dominant right-lobe mass with flow cytometry '
                                    'shows diffuse large B-cell lymphoma, and PET/CT shows disease confined to the '
                                    'thyroid. The endocrinologist asks whether thyroidectomy should be the primary '
                                    'treatment. What is the best recommendation?',
                            'choices': ['Rituximab-based chemotherapy with or without radiation, without surgery',
                                        'Total thyroidectomy as the primary treatment, followed by observation',
                                        'Levothyroxine dose escalation to shrink both the goiter and the lymphoma',
                                        'Defer any treatment until the patient develops overt airway obstruction'],
                            'answer': 0,
                            'explanation': 'Thyroid lymphoma is treated nonsurgically once core biopsy with flow '
                                           'cytometry establishes the subtype. Localized diffuse large B-cell lymphoma '
                                           'is treated with R-CHOP chemotherapy, often with involved-site radiation, '
                                           'and usually shrinks rapidly, relieving compressive symptoms. Localized '
                                           'MALT lymphoma is often treated with radiation alone. Surgery in Hashimoto '
                                           'disease is reserved for compressive goiter that does not respond or '
                                           'independently suspicious disease, and for airway emergencies. The airway '
                                           'should be monitored during early treatment, and steroids can give rapid '
                                           'relief.',
                            'why_wrong': ['Correct.',
                                          'Thyroidectomy adds nerve and parathyroid risk without improving survival '
                                          'over chemotherapy and radiation for diffuse large B-cell lymphoma.',
                                          'TSH suppression does not treat lymphoma, and the compressive symptoms come '
                                          'largely from the tumor.',
                                          'Diffuse large B-cell lymphoma is aggressive and responds quickly to '
                                          'treatment; waiting risks airway compromise.'],
                            'board_pearl': 'Thyroid lymphoma: diagnose by core biopsy with flow; treat with '
                                           'chemotherapy and/or radiation, not thyroidectomy.',
                            'curveball': 'Why is core biopsy with flow cytometry preferred over standard FNA when '
                                         'lymphoma is suspected in a Hashimoto gland?',
                            'curveball_answer': 'Hashimoto glands are already full of reactive lymphocytes, so FNA '
                                                'cytology often cannot separate low-grade lymphoma from florid '
                                                'thyroiditis or classify the lymphoma subtype. A core biopsy preserves '
                                                'architecture and gives enough tissue for flow cytometry, '
                                                'immunohistochemistry, and clonality studies, which determine the '
                                                'subtype and treatment.'},
 'v431-ebsln-injury-01': {'stem': 'A 38-year-old woman who teaches music and sings in a choir has total thyroidectomy '
                                  'for a multinodular goiter with a large left superior pole. Three weeks later she '
                                  'cannot reach her upper register, tires quickly when singing, and her voice lacks '
                                  'projection. Flexible laryngoscopy shows full abduction and adduction of both folds. '
                                  'Stroboscopy shows the posterior glottis rotated toward the left during phonation. '
                                  'What is the most specific confirmatory test?',
                          'choices': ['Repeat videostroboscopy in three months',
                                      'CT of the neck and upper mediastinum',
                                      'Empiric proton pump inhibitor trial',
                                      'Laryngeal EMG of the cricothyroid muscles'],
                          'answer': 3,
                          'explanation': 'Loss of upper register, vocal fatigue, and reduced projection with normal '
                                         'gross vocal fold motion after thyroidectomy suggest injury to the external '
                                         'branch of the superior laryngeal nerve, especially after dissecting a large '
                                         'superior pole. The EBSLN supplies the cricothyroid, which tilts the thyroid '
                                         'cartilage to lengthen and tense the folds. Unilateral weakness can rotate '
                                         'the posterior glottis toward the weak side, though stroboscopic signs are '
                                         'inconsistent. Laryngeal EMG of the cricothyroid, showing reduced recruitment '
                                         'or denervation, is the most specific confirmation when it will change '
                                         'counseling.',
                          'why_wrong': ['Stroboscopy suggests the diagnosis, but its findings are subtle and '
                                        'nonspecific, and waiting does not confirm the lesion.',
                                        'Imaging cannot show the function of a small motor nerve and adds radiation '
                                        'without diagnostic benefit.',
                                        'Reflux does not explain the loss of pitch range after superior pole surgery '
                                        'with posterior glottic rotation.',
                                        'Correct.'],
                          'board_pearl': 'Normal fold motion but lost high pitch and projection after thyroidectomy: '
                                         'suspect EBSLN injury; confirm with cricothyroid EMG.',
                          'curveball': 'Looking back at her operation, how can EBSLN injury be prevented during '
                                       'thyroidectomy for a large superior pole?',
                          'curveball_answer': 'Dissect in the avascular cricothyroid space between the superior pole '
                                              'and the cricothyroid muscle, identifying the nerve visually or with '
                                              'nerve stimulation and monitoring. Ligate the superior pedicle vessels '
                                              'individually and close to the thyroid capsule rather than with mass '
                                              'ligation high on the pedicle. Look for the cricothyroid twitch before '
                                              'dividing tissue.'},
 'v431-ebsln-injury-02': {'stem': 'A 52-year-old woman who is a high school teacher has reduced pitch range and vocal '
                                  'fatigue after a right lobectomy 3 months ago. Laryngoscopy shows normal vocal fold '
                                  'mobility, and laryngeal EMG confirms isolated right cricothyroid denervation with '
                                  'some voluntary motor units preserved. Her glottic closure is complete on '
                                  'stroboscopy, and she is not aspirating. She asks what treatment is available. What '
                                  'is the most appropriate management?',
                          'choices': ['Revision neck exploration with primary nerve repair',
                                      'Voice therapy and observation for spontaneous recovery',
                                      'Injection laryngoplasty of the right vocal fold',
                                      'Ansa cervicalis to superior laryngeal nerve graft'],
                          'answer': 1,
                          'explanation': 'No standard restorative operation exists for isolated external branch of the '
                                         'superior laryngeal nerve injury. Management is observation for spontaneous '
                                         'recovery, which is likely when EMG shows preserved motor units, plus voice '
                                         'therapy. Therapy teaches compensation, efficient resonance and projection, '
                                         'and safe vocal loading, which matter greatly for teachers and singers. '
                                         'Recovery and functional impact vary widely, and many patients adapt well '
                                         'over 6 to 12 months. Repeat EMG can help with prognosis if symptoms persist.',
                          'why_wrong': ['The nerve is small and hard to find in a scarred field, and there is no '
                                        'standard reconstructive operation for it.',
                                        'Correct.',
                                        'Injection medialization treats glottic insufficiency, but her closure is '
                                        'complete and injection does not restore pitch range.',
                                        'Reinnervation of the superior laryngeal nerve is not a standard procedure and '
                                        'has no proven benefit for isolated EBSLN injury.'],
                          'board_pearl': 'Isolated EBSLN injury: voice therapy and observation; there is no standard '
                                         'restorative surgery.',
                          'curveball': 'What symptoms should specifically be asked about in a professional voice user '
                                       'after neck surgery?',
                          'curveball_answer': 'Ask about loss of upper range or difficulty with high notes, reduced '
                                              'loudness and projection, vocal fatigue with prolonged use, breathiness, '
                                              'pitch breaks, and voice change that worsens over the day. Also ask '
                                              'about swallowing and aspiration. Subtle EBSLN symptoms may be missed if '
                                              'only hoarseness is asked about.'},
 'v461_tps_ebsln_fnd': {'stem': 'A 41-year-old woman who sings professionally has an uncomplicated total '
                                'thyroidectomy. Two weeks later she cannot reach her high notes, her voice is weaker '
                                'and tires quickly, and she cannot sing a pitch glide upward. Speaking voice sounds '
                                'near normal. Flexible laryngoscopy shows normal abduction and adduction of both '
                                'folds. Weakness of which muscle best explains her symptoms?',
                        'choices': ['Posterior cricoarytenoid',
                                    'Thyroarytenoid',
                                    'Lateral cricoarytenoid',
                                    'Cricothyroid'],
                        'answer': 3,
                        'explanation': 'The cricothyroid is the only intrinsic laryngeal muscle supplied by the '
                                       'external branch of the superior laryngeal nerve; all others receive recurrent '
                                       'laryngeal nerve fibers. Contraction tilts the thyroid cartilage forward on the '
                                       'cricoid, lengthening and tensing the vocal folds to raise pitch. Injury '
                                       'therefore reduces pitch range, projection, and endurance while gross abduction '
                                       'and adduction stay normal. The deficit is most obvious in singers and '
                                       'professional voice users. The nerve is at risk during superior pole '
                                       'dissection, where it runs close to the superior thyroid vessels.',
                        'why_wrong': ['The posterior cricoarytenoid is the only abductor; its weakness impairs '
                                      'abduction, which is normal here, and causes airway problems.',
                                      'The thyroarytenoid is supplied by the recurrent nerve, and its paralysis '
                                      'typically causes reduced fold motion and breathiness.',
                                      'The lateral cricoarytenoid is an adductor supplied by the recurrent nerve; its '
                                      'weakness would show impaired adduction.',
                                      'Correct.'],
                        'board_pearl': 'The EBSLN supplies only the cricothyroid, the pitch-raising tensor; injury '
                                       'spares fold abduction and adduction.',
                        'curveball': 'What test is the most specific confirmatory study for EBSLN injury when the '
                                     'result will change counseling or treatment?',
                        'curveball_answer': 'Laryngeal EMG of the cricothyroid muscle is the most specific test, '
                                            'showing reduced recruitment, fibrillations, or absent motor units on the '
                                            'affected side. It also provides prognostic information. Stroboscopy may '
                                            'show posterior glottic rotation toward the weak side or vertical fold '
                                            'height mismatch, but these signs are inconsistent.'},
 'v461_tps_ebsln_app': {'stem': 'A 58-year-old woman undergoes total thyroidectomy for a large multinodular goiter '
                                'that extends high toward the thyroid cartilage. While dissecting the right superior '
                                'pole, the surgeon sees the external branch of the superior laryngeal nerve crossing '
                                'the superior thyroid artery and vein below the upper border of the superior pole, '
                                'within the planned ligation field. How is this nerve course classified?',
                        'choices': ['Cernea type 1, crossing more than 1 cm above',
                                    'Cernea type 2b, the highest-risk course',
                                    'Cernea type 2a, crossing less than 1 cm above',
                                    'Friedman type 3, protected beneath the constrictor'],
                        'answer': 1,
                        'explanation': 'The Cernea classification describes where the EBSLN crosses the superior '
                                       'thyroid vessels relative to the upper edge of the superior pole. Type 1 '
                                       'crosses more than 1 cm above, type 2a crosses within 1 cm above, and type 2b '
                                       'crosses below the upper border of the pole. Type 2b nerves lie within the '
                                       'field of superior pedicle ligation and carry the highest injury risk. They are '
                                       'more common with large goiters and short necks, because the enlarged pole '
                                       'rises toward the nerve.',
                        'why_wrong': ['Type 1 nerves cross the vessels more than 1 cm above the upper pole, well away '
                                      'from the ligation field, and have the lowest risk.',
                                      'Correct.',
                                      'Type 2a nerves cross within 1 cm above the upper pole, which is closer but '
                                      'still above the gland.',
                                      "The Friedman scheme describes the nerve's relation to the inferior constrictor; "
                                      'a type 3 nerve runs deep and is protected, unlike this one.'],
                        'board_pearl': 'Cernea 2b: EBSLN crosses below the upper pole border; highest risk, common '
                                       'with large goiters.',
                        'curveball': 'What operative technique should the surgeon use to reduce EBSLN injury risk when '
                                     'handling the superior pedicle in this setting?',
                        'curveball_answer': 'Open the avascular cricothyroid space by retracting the pole laterally '
                                            'and inferiorly, find the nerve on the cricothyroid or inferior '
                                            'constrictor with a nerve stimulator or monitor, and confirm the '
                                            'cricothyroid twitch. Then ligate the superior pole branches individually '
                                            'on the thyroid capsule, below the nerve, rather than mass-ligating the '
                                            'pedicle.'},
 'v461_tps_ebsln_snr': {'stem': 'A 35-year-old professional soprano had thyroidectomy 7 months ago. She still has lost '
                                'upper range and projection despite 6 months of voice therapy. Repeat laryngeal EMG '
                                'shows fibrillation potentials and no voluntary motor units in the left cricothyroid. '
                                'Vocal fold mobility and glottic closure are normal. She asks about a definitive '
                                'operation to restore her prior voice. What is the most appropriate counseling?',
                        'choices': ['Laryngeal reinnervation of the left superior laryngeal nerve as the standard '
                                    'repair',
                                    'Exploration and repair of the left recurrent laryngeal nerve to restore pitch',
                                    'No standard restorative operation exists; continue voice therapy and adaptation',
                                    'Injection laryngoplasty of the left fold to restore her lost upper range'],
                        'answer': 2,
                        'explanation': 'Isolated external branch of the superior laryngeal nerve injury has no '
                                       'standard restorative operation, unlike recurrent laryngeal nerve paralysis, '
                                       'for which medialization and reinnervation are established. Fibrillations '
                                       'without voluntary motor units at 7 months suggest a poor chance of spontaneous '
                                       'recovery. Honest counseling should cover the likely permanence, continued '
                                       'voice therapy with a singing specialist to build compensation and safe vocal '
                                       'loading, and possible repertoire adjustment. Selected pitch-altering '
                                       'procedures have been described, but they are not standard care and are not '
                                       'expected to restore a professional soprano range.',
                        'why_wrong': ['Superior laryngeal reinnervation is not an established standard procedure and '
                                      'has no proven ability to restore singing range.',
                                      'Her recurrent nerve function is normal; the injured nerve supplies the '
                                      'cricothyroid, so recurrent nerve repair would not help.',
                                      'Correct.',
                                      'Injection medialization treats incomplete glottic closure, which she does not '
                                      'have, and does not restore pitch range.'],
                        'board_pearl': 'Persistent EBSLN injury: counsel that no standard restorative surgery exists; '
                                       'focus on skilled voice therapy and adaptation.',
                        'curveball': 'How would you counsel this patient differently before her original surgery if '
                                     'her EBSLN course had been identified as Cernea type 2b intraoperatively?',
                        'curveball_answer': 'Before surgery, a professional singer should be told that EBSLN injury '
                                            'can change pitch range even with normal recurrent nerve function, and '
                                            'that large superior poles raise the risk. If a type 2b course is found, '
                                            'document it, use nerve monitoring and capsular ligation, and tell her '
                                            'afterward so early voice evaluation and therapy can begin.'}}
