"""v491 sweep rewrites: General ENT / Emergencies (gen2)."""

REWRITES = {'v139_gen_06': {'stem': 'A 45-year-old man has 5 days of right throat pain after tonsillitis. Despite 48 hours of IV '
                         'ampicillin-sulbactam, he has a temperature of 39.4 C, heart rate 118, trismus with a 1.5 cm '
                         'opening, a muffled voice, and new inspiratory noise when supine. Contrast CT shows a 4.5 cm '
                         'rim-enhancing right prestyloid parapharyngeal collection narrowing the oropharyngeal airway. '
                         'What is the next step?',
                 'choices': ['Secure the airway awake, then drain the collection operatively with cultures',
                             'Broaden coverage to vancomycin plus meropenem and repeat contrast CT in 48 hours',
                             'Bedside ultrasound-guided needle aspiration and continued IV antibiotics',
                             'Add IV dexamethasone and continue ampicillin-sulbactam with ICU monitoring'],
                 'answer': 0,
                 'explanation': 'This is a mature, rim-enhancing abscess that has failed 48 hours of appropriate IV '
                                'therapy and is now producing sepsis and positional airway noise. Pus within a '
                                'walled-off cavity is poorly penetrated by antibiotics, so source control by drainage '
                                'is required, with cultures to direct therapy. Because trismus and pharyngeal '
                                'narrowing make induction dangerous, the airway is secured first, typically by awake '
                                'fiberoptic intubation with a surgical airway ready. The prestyloid location permits '
                                'transoral or transcervical drainage chosen by access and vessel relationships.',
                 'why_wrong': ['Correct.',
                               'Changing antibiotics does not drain a large organized collection, and waiting 48 hours '
                               'risks airway loss in a patient already failing therapy.',
                               'Needle aspiration may suit a small collection in a stable patient, but sepsis, airway '
                               'narrowing, and failed therapy call for formal drainage.',
                               'Steroids may reduce edema, but they do not treat an undrained abscess and could mask '
                               'progression in a septic patient with airway noise.'],
                 'board_pearl': 'Large organized deep neck abscess plus sepsis, airway symptoms, or failed IV '
                                'antibiotics: secure the airway, then drain and culture.',
                 'curveball': 'Postoperative CT shows fluid and gas extending below the thoracic inlet into the '
                              'anterior and posterior mediastinum. What does this indicate, and who must be involved?',
                 'curveball_answer': 'This is descending necrotizing mediastinitis, spread along cervical fascial '
                                     'planes such as the retropharyngeal and danger spaces into the chest. It carries '
                                     'high mortality and is not controlled by cervical drainage alone when it extends '
                                     'below the carina or into multiple compartments. Thoracic surgery should be '
                                     'involved immediately for mediastinal drainage by thoracoscopy or thoracotomy, '
                                     'with CT of the chest repeated to confirm source control.'},
 'v143_gen_02': {'stem': 'A 38-year-old woman with a left parapharyngeal abscess is going to the operating room for '
                         'drainage after failing IV antibiotics. She has trismus with a 1 cm interincisal opening, '
                         'drools, and sits upright to breathe comfortably. Flexible laryngoscopy shows medial bulging '
                         'of the left lateral pharyngeal wall with a narrowed but visible glottis. Oxygen saturation '
                         'is 96% on room air. Which airway plan is most appropriate before drainage?',
                 'choices': ['Rapid-sequence induction with videolaryngoscopy and a bougie available',
                             'Inhalational induction with spontaneous ventilation and direct laryngoscopy',
                             'Awake fiberoptic nasotracheal intubation with tracheostomy setup ready',
                             'Transoral needle decompression in clinic, followed by routine induction'],
                 'answer': 2,
                 'explanation': 'Airway strategy is part of the drainage operation. Severe trismus does not relax '
                                'reliably with neuromuscular blockade when it is caused by inflammation, and a '
                                'distorted pharynx can make mask ventilation and laryngoscopy fail after induction. '
                                'Awake fiberoptic intubation, usually nasal because the mouth will not open, preserves '
                                'spontaneous ventilation and airway tone until the tube is placed. The surgeon should '
                                'be scrubbed with tracheostomy instruments ready because manipulation or abscess '
                                'rupture can precipitate obstruction. Cultures and culture-directed antibiotics follow '
                                'drainage.',
                 'why_wrong': ['Paralysis removes airway tone, and trismus from inflammation may not resolve, risking '
                               'a cannot-intubate, cannot-oxygenate situation in a distorted pharynx.',
                               'Inhalational induction preserves breathing, but direct laryngoscopy still requires '
                               'mouth opening that this 1 cm interincisal gap will not allow.',
                               'Correct.',
                               'Blind clinic needle decompression near the parapharyngeal vessels is unsafe and does '
                               'not make a subsequent routine induction safe.'],
                 'board_pearl': 'Trismus from deep neck infection may not relax with paralysis; plan awake fiberoptic '
                                'intubation with tracheostomy backup.',
                 'curveball': 'The fiberoptic scope reaches the oropharynx, but pus suddenly fills the field after the '
                              'bulge ruptures and saturation falls to 85%. What should happen next?',
                 'curveball_answer': 'Suction the pharynx immediately and place her head down and turned to drain pus '
                                     'away from the larynx. If the glottis cannot be visualized quickly and '
                                     'oxygenation keeps falling, proceed to the planned surgical airway, '
                                     'cricothyrotomy or tracheostomy, rather than repeating scope attempts. Once '
                                     'secured, the cavity is drained and cultured and the airway is inspected for '
                                     'aspirated material.'},
 'v269_gen_deep_fnd': {'stem': 'A 59-year-old woman has 4 days of painful right submandibular swelling after a '
                               'toothache. She has mild trismus, a normal voice, and no stridor, and the floor of '
                               'mouth is soft. Contrast CT shows a 3 cm rim-enhancing right submandibular space '
                               'abscess contiguous with a periapical lucency of the right mandibular second molar. She '
                               'is started on IV ampicillin-sulbactam and admitted for airway observation. Which step '
                               'is also essential to definitive management?',
                       'choices': ['Repeat contrast CT every 48 hours until the collection resolves',
                                   'Transcervical drainage plus extraction of the infected molar',
                                   'Six weeks of IV antibiotics through a peripherally inserted catheter',
                                   'Hyperbaric oxygen therapy to improve antibiotic delivery to the cavity'],
                       'answer': 1,
                       'explanation': 'Deep neck infection management rests on three pillars: airway safety, source '
                                      'control, and appropriate antimicrobial therapy. This patient has a stable '
                                      'airway and is on suitable antibiotics, but a drainable abscess and an ongoing '
                                      'odontogenic source remain. Source control means draining the submandibular '
                                      'collection and removing the infected tooth, because leaving the source in place '
                                      'invites recurrence. Cultures from the drainage guide narrowing of therapy. '
                                      'Imaging is repeated only if improvement stalls.',
                       'why_wrong': ['Serial routine imaging adds radiation and delay but does not treat the abscess; '
                                     'repeat CT is reserved for clinical failure.',
                                     'Correct.',
                                     'Prolonged IV antibiotics are not a substitute for drainage and tooth removal and '
                                     'are typically used for osteomyelitis rather than a drained abscess.',
                                     'Hyperbaric oxygen is not a standard treatment for odontogenic deep neck abscess '
                                     'and does not replace drainage or source removal.'],
                       'board_pearl': 'Deep neck infection: airway safety, anatomic source control, and '
                                      'culture-directed antibiotics. Odontogenic abscess needs drainage plus treatment '
                                      'of the tooth.',
                       'curveball': 'Two days later she develops bilateral floor-of-mouth firmness, an elevated '
                                    'tongue, and a muffled voice. What has happened, and how does the airway plan '
                                    'change?',
                       'curveball_answer': 'She has progressed to Ludwig angina, a bilateral submandibular, '
                                           'sublingual, and submental cellulitis that elevates the tongue and can '
                                           'obstruct the airway rapidly. The airway becomes the first priority: keep '
                                           'her upright, avoid sedation, and secure it by awake fiberoptic intubation '
                                           'or awake tracheostomy under local anesthesia, followed by wide bilateral '
                                           'decompression and continued broad antibiotics.'},
 'v269_gen_deep_snr': {'stem': 'A 52-year-old man is on postoperative day 2 after transcervical drainage of left '
                               'parapharyngeal and retropharyngeal abscesses from a tonsillar source. His fever has '
                               'risen to 39.5 C, WBC has increased from 18,000 to 26,000, and he now has substernal '
                               'pleuritic chest pain and heart rate 124. The neck drain output is serous and the wound '
                               'looks clean. Which is the best next step?',
                       'choices': ['Transthoracic echocardiogram and serial blood cultures for endocarditis',
                                   'CT pulmonary angiogram to evaluate for postoperative embolism',
                                   'Add empiric antifungal therapy and observe for another 48 hours',
                                   'Contrast CT of the neck and chest with early thoracic surgery input'],
                       'answer': 3,
                       'explanation': 'Worsening sepsis after drainage means an undrained compartment or a '
                                      'complication until proven otherwise. Retropharyngeal infection can pass into '
                                      'the danger space between the alar and prevertebral fascia and descend freely to '
                                      'the posterior mediastinum. New substernal chest pain with rising WBC is the '
                                      'classic warning of descending necrotizing mediastinitis. Contrast CT covering '
                                      'both neck and chest localizes residual neck collections, mediastinal fluid or '
                                      'gas, and vascular complications such as jugular thrombosis, and early thoracic '
                                      'surgery involvement allows prompt mediastinal drainage.',
                       'why_wrong': ['Endocarditis can cause persistent fever, but substernal pain after '
                                     'retropharyngeal drainage points first to mediastinal spread, which needs urgent '
                                     'imaging.',
                                     'A pulmonary embolism protocol is the wrong study for this question and would not '
                                     'image the neck spaces that may still hold pus.',
                                     'Adding drugs without localizing the source repeats the error of treating a '
                                     'surgical problem medically and delays drainage of mediastinal infection.',
                                     'Correct.'],
                       'board_pearl': 'Retropharyngeal infection plus new chest pain or rising sepsis after drainage: '
                                      'CT neck and chest for descending mediastinitis.',
                       'curveball': 'CT shows no mediastinal fluid but a filling defect in the left internal jugular '
                                    'vein with scattered peripheral lung nodules. How does this change management?',
                       'curveball_answer': 'This is septic jugular thrombophlebitis with septic pulmonary emboli, the '
                                           'Lemierre pattern, classically caused by Fusobacterium necrophorum. '
                                           'Treatment is prolonged IV antibiotics with anaerobic coverage, such as '
                                           'ampicillin-sulbactam or a carbapenem, for several weeks, plus drainage of '
                                           'any residual collection. Anticoagulation is debated and individualized, '
                                           'and jugular ligation is reserved for persistent septic emboli despite '
                                           'appropriate therapy.'},
 'v139_gen_07': {'stem': 'A 64-year-old man with a T4 hypopharyngeal squamous cell carcinoma has lost 15% of his body '
                         'weight and taken almost nothing by mouth for 10 days. A gastrostomy tube is placed and feeds '
                         'are advanced to goal within 24 hours. On day 3 he has new ankle edema and generalized '
                         'weakness. Phosphate is 1.4 mg/dL, potassium 2.9 mmol/L, and magnesium 1.3 mg/dL. Which '
                         'diagnosis best explains these findings?',
                 'choices': ['Tumor lysis syndrome',
                             'Hungry bone syndrome',
                             'Syndrome of inappropriate ADH secretion',
                             'Refeeding syndrome'],
                 'answer': 3,
                 'explanation': 'Refeeding syndrome occurs when nutrition is restarted after prolonged starvation. '
                                'Carbohydrate stimulates insulin release, which drives phosphate, potassium, and '
                                'magnesium into cells and increases thiamine use, while insulin-related sodium and '
                                'water retention causes edema. His weight loss, 10 days of minimal intake, and rapid '
                                'advancement to goal feeds are classic risk features, and the triad of low phosphate, '
                                'potassium, and magnesium with edema on day 3 is the characteristic picture. Head and '
                                'neck cancer patients with dysphagia are a high-risk group.',
                 'why_wrong': ['Tumor lysis raises phosphate and potassium from cell breakdown, the opposite of this '
                               'pattern, and is uncommon with head and neck squamous carcinoma.',
                               'Hungry bone syndrome follows parathyroidectomy for hyperparathyroidism, with skeletal '
                               'uptake of calcium and phosphate; he has had no parathyroid surgery.',
                               'SIADH causes euvolemic hyponatremia with concentrated urine, not combined '
                               'hypophosphatemia, hypokalemia, and hypomagnesemia with edema.',
                               'Correct.'],
                 'board_pearl': 'Low phosphate, potassium, and magnesium with edema days after restarting feeds in a '
                                'starved patient means refeeding syndrome.',
                 'curveball': 'His team asks how they should have started his feeds given his risk profile. What '
                              'regimen would have reduced this risk?',
                 'curveball_answer': 'High-risk patients should receive thiamine before or with the first feed, have '
                                     'phosphate, potassium, and magnesium checked and corrected, and start at a low '
                                     'caloric rate, commonly about 10 kcal/kg/day, or 5 kcal/kg/day in extreme cases. '
                                     'Calories are advanced over several days toward goal while electrolytes are '
                                     'checked at least daily and replaced, along with fluid balance monitoring.'},
 'v147_gen_03': {'stem': 'A 71-year-old woman with recurrent oral cavity carcinoma and severe trismus has subsisted on '
                         'liquids for a month and has a BMI of 16. Nasogastric feeds are started at full goal rate. '
                         'Thirty-six hours later she is weak, has palpitations, and telemetry shows frequent premature '
                         'ventricular beats. Phosphate is 0.9 mg/dL, potassium 3.0 mmol/L, and magnesium 1.2 mg/dL. '
                         'Which mechanism best explains these findings?',
                 'choices': ['Renal wasting of phosphate and magnesium from nephrotoxic drugs',
                             'Insulin-driven intracellular shift of phosphate, potassium, and magnesium',
                             'Dilutional depletion from hypotonic free-water tube flushes',
                             'Gastrointestinal loss of electrolytes from feed-associated secretory diarrhea'],
                 'answer': 1,
                 'explanation': 'During starvation total-body phosphate, potassium, and magnesium are depleted even '
                                'when serum levels look normal. When carbohydrate arrives, insulin secretion drives '
                                'these ions into cells for glycogen synthesis and ATP production, unmasking the '
                                'deficit in serum. Severe hypophosphatemia limits ATP and 2,3-DPG, impairing cardiac '
                                'and respiratory muscle, while low potassium and magnesium promote arrhythmias. Her '
                                'BMI of 16, a month of poor intake, and full-rate feeds explain the timing within 2 to '
                                '3 days.',
                 'why_wrong': ['Nephrotoxic drug wasting needs an offending agent and would not produce this abrupt '
                               'fall timed to the start of feeds.',
                               'Correct.',
                               'Free-water excess lowers sodium predominantly; it does not selectively drop phosphate, '
                               'potassium, and magnesium within 36 hours.',
                               'Diarrhea can lower potassium and magnesium, but she has none reported, and stool '
                               'losses do not explain a profound fall in phosphate.'],
                 'board_pearl': 'Refeeding syndrome: insulin shifts phosphate, potassium, and magnesium into cells, '
                                'unmasking total-body depletion.',
                 'curveball': 'Her magnesium is replaced but potassium stays low despite large oral supplements. Why '
                              'might potassium be refractory, and what should be checked?',
                 'curveball_answer': 'Hypomagnesemia causes renal potassium wasting by releasing inhibition of ROMK '
                                     'channels in the distal nephron, so potassium will not correct until magnesium is '
                                     'fully replete. Recheck magnesium after replacement, since a single dose is often '
                                     'redistributed, and continue IV magnesium as needed. Also review ongoing losses '
                                     'and avoid rapid feed advancement until levels stabilize.'},
 'v152_gen_01': {'stem': 'A 66-year-old man with laryngeal cancer and 18% weight loss starts tube feeds at goal rate. '
                         'Twelve hours later his phosphate has fallen from 2.8 to 1.0 mg/dL, and he is weak with heart '
                         'rate 112 and ventricular ectopy. Potassium is 3.1 mmol/L and magnesium 1.4 mg/dL. He has not '
                         'received thiamine. Blood pressure and oxygen saturation are normal. What is the best '
                         'immediate response?',
                 'choices': ['Reduce feeds, replace electrolytes IV, give thiamine, and monitor rhythm',
                             'Continue feeds at goal and give oral phosphate through the tube',
                             'Stop enteral feeds and start parenteral nutrition at full calories',
                             'Give a 2 L normal saline bolus for tachycardia and recheck labs tomorrow'],
                 'answer': 0,
                 'explanation': 'This is symptomatic refeeding syndrome. Ventricular ectopy with severe '
                                'hypophosphatemia, hypokalemia, and hypomagnesemia requires IV replacement under '
                                'cardiac monitoring, not oral correction. Caloric delivery is reduced substantially, '
                                'commonly by about half or to a low starting rate, then advanced slowly once '
                                'electrolytes stabilize. Thiamine is given because carbohydrate load increases demand '
                                'and deficiency can precipitate Wernicke encephalopathy or cardiac failure. Nutrition '
                                'is slowed rather than abandoned, because the underlying malnutrition still needs '
                                'treatment.',
                 'why_wrong': ['Correct.',
                               'Oral phosphate is too slow for symptomatic severe hypophosphatemia with ectopy, and '
                               'continuing full calories keeps driving the intracellular shift.',
                               'Parenteral nutrition at full calories carries the same insulin-driven shift and adds '
                               'line risks without addressing the cause.',
                               'Volume loading does not correct the electrolyte shift, may worsen sodium-related '
                               'edema, and delaying labs is unsafe with arrhythmia.'],
                 'board_pearl': 'Symptomatic refeeding: slow the calories, replace phosphate, potassium, and magnesium '
                                'IV, give thiamine, and monitor rhythm.',
                 'curveball': 'Two days later he is confused with nystagmus and an unsteady gait, although his '
                              'electrolytes have normalized. What is the likely cause and treatment?',
                 'curveball_answer': 'This suggests Wernicke encephalopathy from thiamine deficiency unmasked by '
                                     'carbohydrate refeeding. Normal electrolytes do not exclude it. Give high-dose IV '
                                     'thiamine immediately, before further dextrose-containing fluids, and continue it '
                                     'for several days, then oral supplementation. Magnesium should also be replete '
                                     'because it is a cofactor for thiamine-dependent enzymes. Delay can lead to '
                                     'permanent Korsakoff memory deficits.'},
 'v154_gen_fnd': {'stem': 'A 57-year-old man is intubated in the ICU after a pharyngocutaneous fistula and sepsis '
                          'following salvage laryngectomy. He had lost 20% of his weight before surgery. Feeds were '
                          'started 3 days ago and advanced quickly. Sepsis has resolved, but he repeatedly fails '
                          'spontaneous breathing trials with rapid shallow breathing and generalized weakness. Chest '
                          'radiograph is clear. Which laboratory abnormality most likely explains his failure to wean?',
                  'choices': ['Hypercalcemia', 'Hypernatremia', 'Hypophosphatemia', 'Hypermagnesemia'],
                  'answer': 2,
                  'explanation': 'Hypophosphatemia is the hallmark and most dangerous electrolyte abnormality of '
                                 'refeeding syndrome. Phosphate is needed for ATP and red cell 2,3-DPG, so severe '
                                 'depletion weakens the diaphragm and other respiratory muscles, impairs myocardial '
                                 'contractility, and can cause rhabdomyolysis and confusion. Failure to wean in a '
                                 'malnourished patient days after rapid feed advancement, with a clear chest film and '
                                 'resolved sepsis, should prompt measurement and IV correction of phosphate along with '
                                 'potassium and magnesium.',
                  'why_wrong': ['Hypercalcemia causes weakness and confusion but is not a feature of refeeding, which '
                                'tends to lower rather than raise mineral levels.',
                                'Hypernatremia from free-water deficit can occur in tube-fed patients but does not '
                                'typically cause respiratory muscle failure during weaning.',
                                'Correct.',
                                'Refeeding lowers magnesium rather than raising it; high magnesium usually follows '
                                'excess replacement or renal failure.'],
                  'board_pearl': 'Hypophosphatemia is the signature lab of refeeding syndrome and can cause '
                                 'respiratory muscle failure and failure to wean.',
                  'curveball': 'His phosphate is 0.8 mg/dL and creatinine is normal. How should it be replaced, and '
                               'what must be watched during replacement?',
                  'curveball_answer': 'Severe hypophosphatemia below about 1 mg/dL, especially with symptoms, is '
                                      'treated with IV sodium or potassium phosphate infused over several hours, with '
                                      'levels rechecked after each dose. Monitor calcium, because rapid phosphate '
                                      'infusion can precipitate calcium phosphate and cause hypocalcemia, and watch '
                                      'potassium if potassium phosphate is used. Reduce caloric delivery until '
                                      'phosphate stabilizes.'},
 'v154_gen_app': {'stem': 'A 68-year-old woman with T4 oral tongue carcinoma has eaten little for 2 weeks because of '
                          'pain and has lost 12% of her weight in 3 months. She drinks alcohol daily. A nasogastric '
                          'tube is placed the day before planned surgery. Baseline phosphate is 2.4 mg/dL, potassium '
                          '3.4 mmol/L, and magnesium 1.6 mg/dL. Which feeding plan is most appropriate?',
                  'choices': ['Start feeds at full goal rate and check electrolytes after 1 week',
                              'Hold all nutrition until surgery is complete and albumin improves',
                              'Give thiamine, correct electrolytes, and start feeds near 10 kcal/kg/day',
                              'Begin parenteral nutrition at goal to bypass the gut and its insulin response'],
                  'answer': 2,
                  'explanation': 'She meets high-risk refeeding criteria: weight loss over 10% in 3 to 6 months, '
                                 'little intake for more than 5 days, alcohol use, and low baseline electrolytes. '
                                 'Prevention involves thiamine before feeding, correction of phosphate, potassium, and '
                                 'magnesium, and starting at a low caloric rate, commonly about 10 kcal/kg/day, then '
                                 'advancing slowly over several days while checking electrolytes daily. Enteral '
                                 'feeding is preferred when the gut works. Withholding nutrition would worsen '
                                 'malnutrition and wound healing.',
                  'why_wrong': ['Full calories in a high-risk patient provoke the insulin-driven shift, and weekly '
                                'labs would miss the fall that typically appears within 72 hours.',
                                'Albumin reflects inflammation more than nutrition, and withholding feeds deepens '
                                'malnutrition and impairs postoperative healing.',
                                'Correct.',
                                'Parenteral dextrose also triggers insulin release, so refeeding risk persists, and '
                                'the gut remains the preferred route when it is usable.'],
                  'board_pearl': 'High refeeding risk: thiamine first, correct electrolytes, start low, about 10 '
                                 'kcal/kg/day, and advance slowly with daily labs.',
                  'curveball': 'Her BMI is 14 and she has had almost no intake for 3 weeks. Does this change the '
                               'starting regimen?',
                  'curveball_answer': 'Yes. Extreme risk, such as a BMI below 14 or negligible intake for more than 15 '
                                      'days, warrants an even lower start, about 5 kcal/kg/day per NICE guidance, with '
                                      'cardiac monitoring and electrolytes checked at least daily. Thiamine and a '
                                      'multivitamin continue for the first days, and calories are increased gradually '
                                      'only as phosphate, potassium, and magnesium remain stable.'},
 'v154_gen_snr': {'stem': 'A 62-year-old man with oropharyngeal cancer, weight loss of 16%, and 2 weeks of minimal '
                          'intake starts gastrostomy feeds. Twelve hours later he reports weakness and shortness of '
                          'breath. Heart rate is 110 with runs of ventricular ectopy, phosphate is 0.8 mg/dL, '
                          'potassium 2.8 mmol/L, magnesium 1.2 mg/dL, and corrected calcium is normal. Creatinine is '
                          'normal. Which management is most appropriate now?',
                  'choices': ['IV phosphate, potassium, and magnesium on telemetry with feeds reduced',
                              'Oral phosphate and potassium via the gastrostomy, with feeds left at goal',
                              'IV calcium gluconate and amiodarone with feeds continued at goal',
                              'Sodium bicarbonate infusion to shift potassium and phosphate back out'],
                  'answer': 0,
                  'explanation': 'Severe hypophosphatemia below 1 mg/dL with dyspnea and ventricular ectopy is '
                                 'life-threatening refeeding syndrome. Replacement must be IV and monitored on '
                                 'telemetry or in a step-down or ICU setting, because both respiratory muscle failure '
                                 'and arrhythmia can follow. Magnesium is replaced alongside potassium so that '
                                 'potassium correction holds. Caloric delivery is reduced while thiamine is given, '
                                 'then advanced gradually once electrolytes stabilize. The arrhythmia is treated at '
                                 'its cause, the electrolyte deficit.',
                  'why_wrong': ['Correct.',
                                'Oral replacement is too slow and unreliable for symptomatic severe depletion, and '
                                'continuing goal feeds sustains the shift.',
                                'Calcium does not correct hypophosphatemia, and an antiarrhythmic treats the rhythm '
                                'while ignoring its electrolyte cause.',
                                'Bicarbonate drives potassium further into cells, worsening hypokalemia, and has no '
                                'role in treating refeeding syndrome.'],
                  'board_pearl': 'Phosphate below 1 mg/dL with symptoms: monitored IV replacement of phosphate, '
                                 'potassium, and magnesium while slowing calories.',
                  'curveball': 'During repletion his oxygen saturation falls and he needs more oxygen, with rising '
                               'respiratory rate. What features would prompt ICU transfer?',
                  'curveball_answer': 'Rising work of breathing, hypercapnia on blood gas, falling vital capacity, '
                                      'inability to clear secretions, or progressive weakness suggest respiratory '
                                      'muscle failure from hypophosphatemia and warrant ICU care with possible '
                                      'ventilatory support. Sustained ventricular arrhythmia, heart failure from '
                                      'edema, or new confusion also justify ICU transfer. Electrolytes should be '
                                      'rechecked every few hours during IV replacement.'},
 'v273_gen_fen_fnd': {'stem': 'A 60-year-old woman with a large maxillary sinus carcinoma has had little oral intake '
                              'for a week because of pain and trismus and has lost 11% of her weight. Feeds are being '
                              'started through a new nasogastric tube, and the team writes a monitoring plan for the '
                              'first 72 hours. Thiamine has been given and baseline electrolytes are normal. Which '
                              'laboratory value is the most important early warning to trend?',
                      'choices': ['Serum albumin', 'Serum prealbumin', 'Serum sodium', 'Serum phosphate'],
                      'answer': 3,
                      'explanation': 'Phosphate is the earliest and most characteristic abnormality in refeeding '
                                     'syndrome, because insulin drives it into cells for ATP and glycogen formation '
                                     'once carbohydrate is delivered. Levels typically fall within 2 to 3 days of '
                                     'starting feeds, often with potassium and magnesium. Normal baseline levels do '
                                     'not exclude risk because total-body stores are depleted. Monitoring should '
                                     'include phosphate, potassium, and magnesium at least daily for the first several '
                                     'days, with replacement and slower advancement if levels drop.',
                      'why_wrong': ['Albumin is a negative acute-phase reactant with a long half-life and does not '
                                    'change quickly enough to warn of refeeding.',
                                    'Prealbumin falls with inflammation and responds over days to weeks, so it cannot '
                                    'signal an acute refeeding shift.',
                                    'Sodium may change with fluid shifts but is not the characteristic early marker of '
                                    'refeeding syndrome.',
                                    'Correct.'],
                      'board_pearl': 'Trend phosphate, with potassium and magnesium, daily for the first 72 hours of '
                                     'refeeding in at-risk patients.',
                      'curveball': 'On day 2 her phosphate is 1.8 mg/dL but she has no symptoms. Should feeds be '
                                   'stopped?',
                      'curveball_answer': 'Not necessarily. Moderate asymptomatic hypophosphatemia is managed by '
                                          'replacing phosphate, oral or IV depending on severity and absorption, and '
                                          'holding or slowing advancement of calories rather than stopping nutrition. '
                                          'Recheck levels within 12 to 24 hours. Feeds are reduced more substantially '
                                          'if phosphate falls further or symptoms appear, and stopping feeds entirely '
                                          'is rarely needed.'},
 'v273_gen_fen_app': {'stem': 'A 73-year-old man is on day 2 after free-flap reconstruction of the floor of mouth. He '
                              'had lost 14% of his weight preoperatively, and feeds were advanced to goal on day 1. He '
                              'now has new bilateral leg edema, weakness, and heart rate 108. Phosphate is 1.1 mg/dL, '
                              'magnesium 1.3 mg/dL, and potassium 3.0 mmol/L. Echocardiogram last month was normal. '
                              'What is the best next step?',
                      'choices': ['IV furosemide for the edema and continue feeds at the goal rate',
                                  'Reduce feeds, replace electrolytes, give thiamine, and limit sodium load',
                                  'Stop all nutrition and give only free water until edema resolves',
                                  'Switch to a high-protein, low-carbohydrate formula at the same goal rate'],
                      'answer': 1,
                      'explanation': 'Edema, tachycardia, and low phosphate, magnesium, and potassium after rapid '
                                     'feeding in a malnourished patient indicate refeeding syndrome. Insulin causes '
                                     'renal sodium and water retention while the ion shift depletes serum '
                                     'electrolytes, so fluid overload and heart failure can follow. Management is to '
                                     'reduce caloric delivery, replace phosphate, magnesium, and potassium, give '
                                     'thiamine, and limit sodium and fluid, with close monitoring of fluid balance and '
                                     'rhythm. Nutrition is then advanced cautiously, which matters for flap and wound '
                                     'healing.',
                      'why_wrong': ['A diuretic treats the edema but worsens potassium and magnesium loss, and '
                                    'continuing goal feeds sustains the underlying shift.',
                                    'Correct.',
                                    'Stopping nutrition worsens malnutrition and flap healing, and free water alone '
                                    'risks hyponatremia without correcting the deficits.',
                                    'Changing macronutrient mix without lowering total calories and replacing '
                                    'electrolytes does not address the established syndrome.'],
                      'board_pearl': 'Refeeding causes sodium and water retention as well as electrolyte shifts; edema '
                                     'and heart failure can follow rapid feeding.',
                      'curveball': 'Despite these measures his oxygen requirement climbs, he develops crackles, and '
                                   'BNP is elevated. What is the next consideration?',
                      'curveball_answer': 'He may have refeeding-associated heart failure from volume and sodium '
                                          'retention combined with myocardial dysfunction from hypophosphatemia and '
                                          'possibly thiamine deficiency. Transfer to monitored care, give cautious '
                                          'diuresis with aggressive potassium and magnesium replacement, ensure '
                                          'full-dose thiamine, and minimize sodium-containing fluids. Repeat '
                                          'echocardiography if function does not improve after electrolyte '
                                          'correction.'},
 'v273_gen_fen_snr': {'stem': 'A 61-year-old man is 8 hours out from oral cavity resection with an anterolateral thigh '
                              'free flap. Blood pressure is 84/48 after 4 L of crystalloid. The flap is warm, with '
                              'brisk capillary refill and a strong Doppler signal. Hemoglobin is stable at 10.8 g/dL, '
                              'urine output is 0.4 mL/kg/h, and new bibasilar crackles are present. What is the best '
                              'management?',
                      'choices': ['Give another 2 L crystalloid bolus to reach a urine output of 1 mL/kg/h',
                                  'Transfuse 2 units of red cells to improve flap oxygen delivery',
                                  'Withhold vasopressors because they cause pedicle vasospasm',
                                  'Assess fluid responsiveness and cause, then start a vasopressor'],
                      'answer': 3,
                      'explanation': 'Postoperative hypotension after adequate resuscitation is not simply fluid '
                                     'depletion. With stable hemoglobin, a healthy flap, and crackles after 4 L, more '
                                     'crystalloid will mainly add pulmonary and flap edema. The senior step is to '
                                     'identify the physiology, such as vasodilation from anesthetics, bleeding, '
                                     'sepsis, or cardiac dysfunction, using bedside assessment of volume '
                                     'responsiveness, and treat it directly. Retrospective series show that judicious '
                                     'vasopressor use does not increase free-flap failure, so a vasopressor is '
                                     'reasonable once the patient is euvolemic.',
                      'why_wrong': ['Further boluses in a patient with crackles and no evidence of volume '
                                    'responsiveness worsen pulmonary and flap edema without improving perfusion.',
                                    'His hemoglobin is stable at 10.8 g/dL, so transfusion does not target the cause '
                                    'of hypotension and adds transfusion risks.',
                                    'Available evidence shows judicious vasopressor use does not increase flap '
                                    'failure, and untreated hypotension itself threatens flap perfusion.',
                                    'Correct.'],
                      'board_pearl': 'After adequate resuscitation, treat free-flap patient hypotension by cause; '
                                     'judicious vasopressors are not contraindicated.',
                      'curveball': 'An hour later the neck drain fills with 200 mL of bright blood and the flap '
                                   'Doppler becomes faint. How do priorities change?',
                      'curveball_answer': 'This is active hemorrhage with probable compression of the pedicle by '
                                          'hematoma, so he needs urgent return to the operating room. Protect the '
                                          'airway, give blood products through large-bore access, correct '
                                          'coagulopathy, and open the neck to evacuate clot, control bleeding, and '
                                          'inspect the anastomosis. Flap salvage depends on rapid decompression, and '
                                          'fluids and vasopressors only bridge to surgery.'},
 'v139_gen_08': {'stem': 'A 19-year-old woman had exudative pharyngitis 1 week ago. She now has fever of 39.2 C, '
                         'rigors, and tender swelling along the left anterior border of the sternocleidomastoid, with '
                         'mild trismus. Chest radiograph shows several small peripheral nodules. She is '
                         'hemodynamically stable with normal renal function and no contrast allergy. Which imaging '
                         'study is most useful initially?',
                 'choices': ['Contrast-enhanced CT of the neck',
                             'Lateral soft-tissue radiograph of the neck',
                             'MRI of the neck without gadolinium',
                             'Duplex ultrasound of the jugular veins alone'],
                 'answer': 0,
                 'explanation': 'Recent pharyngitis followed by rigors, lateral neck swelling, and septic-appearing '
                                'lung nodules suggests a deep neck infection with internal jugular septic '
                                'thrombophlebitis, the Lemierre pattern. Contrast-enhanced CT is the initial study '
                                'because it is fast and widely available and maps parapharyngeal and other space '
                                'collections, rim enhancement, and airway effect, while showing filling defects in the '
                                'jugular vein. It can be extended to the chest to characterize emboli. MRI adds detail '
                                'in selected cases but is slower.',
                 'why_wrong': ['Correct.',
                               'A lateral radiograph can suggest retropharyngeal widening but cannot localize '
                               'parapharyngeal collections or show jugular thrombosis.',
                               'Noncontrast MRI is slower, less available urgently, and without gadolinium it is '
                               'weaker at showing rim enhancement and venous thrombus.',
                               'Duplex can show jugular thrombus but misses deep collections behind the mandible and '
                               'does not map the involved spaces.'],
                 'board_pearl': 'Suspected deep neck infection or jugular septic thrombophlebitis: contrast-enhanced '
                                'CT of the neck is the initial study.',
                 'curveball': 'CT shows left jugular thrombus but no abscess. Her course is complicated by new facial '
                              'numbness and diplopia. When is MRI preferred?',
                 'curveball_answer': 'New cranial neuropathy raises concern for skull base extension, cavernous sinus '
                                     'thrombosis, or intracranial complications. MRI with gadolinium, plus MR '
                                     'venography, is preferred because it shows marrow and dural enhancement, '
                                     'cavernous sinus filling defects, perineural spread, and early intracranial '
                                     'abscess far better than CT. CT remains better for cortical bone erosion, so both '
                                     'are often complementary.'},
 'v147_gen_04': {'stem': 'A 44-year-old man has 3 days of right lower jaw pain after a dental abscess. He now has '
                         'fever, firm right submandibular swelling, and trismus with a 2 cm opening, but a normal '
                         'voice and no stridor. His dentist obtained a panoramic radiograph showing a periapical '
                         'lucency at the right mandibular second molar. Creatinine is normal. Which imaging study best '
                         'defines a drainable collection and its vascular relationships?',
                 'choices': ['Cone-beam CT of the mandible',
                             'Contrast-enhanced CT of the neck',
                             'Gadolinium MRI of the face and neck',
                             'Ultrasound of the submandibular region'],
                 'answer': 1,
                 'explanation': 'The panoramic film identifies the dental source but cannot assess soft-tissue spread. '
                                'Contrast-enhanced CT of the neck shows which spaces are involved, whether there is a '
                                'rim-enhancing drainable abscess or only phlegmon, gas, airway displacement, extension '
                                'toward the parapharyngeal or retropharyngeal spaces, and the relationship of a '
                                'collection to the carotid and jugular vessels, which guides the drainage approach. It '
                                'is fast and available emergently. MRI adds soft-tissue detail in selected cases but '
                                'takes longer and is harder for a patient with trismus.',
                 'why_wrong': ['Cone-beam CT shows dental and bony anatomy well but has poor soft-tissue contrast and '
                               'cannot map deep space collections.',
                               'Correct.',
                               'MRI offers excellent soft-tissue contrast but is slower, less available urgently, and '
                               'difficult for a patient with an airway concern.',
                               'Ultrasound can find superficial submandibular collections but misses deeper '
                               'parapharyngeal extension and vascular relationships.'],
                 'board_pearl': 'Odontogenic deep neck infection: contrast CT defines abscess versus phlegmon, spaces '
                                'involved, and vessel relationships.',
                 'curveball': 'Months later he has persistent jaw pain and a draining sinus despite tooth extraction. '
                              'Which imaging best evaluates for osteomyelitis?',
                 'curveball_answer': 'CT shows cortical erosion, sequestra, and periosteal reaction, which is useful '
                                     'for surgical planning, but MRI is more sensitive early, showing marrow edema on '
                                     'fat-suppressed T2 and enhancement after gadolinium before bone destruction is '
                                     'visible. Using both is common. Bone biopsy with culture confirms the diagnosis '
                                     'and directs prolonged antibiotics.'},
 'v273_gen_img_fnd': {'stem': 'A 63-year-old man has 3 months of right nasal obstruction and epistaxis. Noncontrast CT '
                              'shows a mass filling the right nasal cavity and ethmoid sinuses with erosion of the '
                              'cribriform plate and lamina papyracea, and complete opacification of the right '
                              'maxillary and frontal sinuses. Biopsy confirms squamous cell carcinoma. MRI with '
                              'gadolinium is ordered. Which information is MRI most likely to add?',
                      'choices': ['Finer detail of thin bony erosion along the cribriform plate and lamina',
                                  'Whether the tumor contains calcified matrix',
                                  'Separation of tumor from retained secretions and dural spread',
                                  'Faster staging in a patient who cannot lie still'],
                      'answer': 2,
                      'explanation': 'CT and MRI answer different questions. Thin-section CT is strongest for cortical '
                                     'bone, calcification, and air, so it already shows cribriform and lamina erosion. '
                                     'MRI has superior soft-tissue contrast: tumor typically has intermediate T2 '
                                     'signal and enhances, while obstructed secretions are usually bright on T2 and '
                                     'enhance only peripherally. MRI also shows dural enhancement, brain invasion, '
                                     'orbital periosteal breach, marrow involvement, and perineural spread, all of '
                                     'which change staging and resectability. Many skull base tumors therefore need '
                                     'both studies.',
                      'why_wrong': ['CT is superior to MRI for depicting fine cortical bone and thin plates such as '
                                    'the cribriform plate and lamina papyracea.',
                                    'Calcification is best seen on CT; MRI depicts calcium poorly and inconsistently.',
                                    'Correct.',
                                    'MRI takes longer and is more sensitive to motion than CT, so it is not the faster '
                                    'study.'],
                      'board_pearl': 'CT for bone, calcification, and air; MRI for soft tissue, marrow, dura, orbit, '
                                     'and perineural spread. Skull base tumors often need both.',
                      'curveball': 'Why might you deliberately obtain both CT and MRI for a lateral skull base lesion '
                                   'such as a jugular foramen mass?',
                      'curveball_answer': 'CT defines bony margins, which differ by tumor: permeative destruction of '
                                          'the jugular foramen suggests paraganglioma, while smooth enlargement '
                                          'suggests schwannoma. It also shows the jugular bulb, carotid canal, and '
                                          'ossicles. MRI shows tumor extent, salt-and-pepper flow voids, intracranial '
                                          'and dural extension, and venous sinus patency. Together they guide '
                                          'diagnosis and surgical approach.'},
 'v273_gen_img_app': {'stem': 'A 50-year-old man with diabetes has 4 days of sore throat, then neck swelling and '
                              'severe pain. He has fever of 39.6 C, heart rate 122, trismus, and new retrosternal pain '
                              'when swallowing, but oxygen saturation is normal and he is speaking comfortably '
                              'upright. Creatinine is normal. He is stable enough to travel to the scanner. Which '
                              'initial imaging study is most appropriate?',
                      'choices': ['Contrast-enhanced CT of the neck and chest',
                                  'Contrast-enhanced CT of the neck alone',
                                  'Noncontrast CT of the neck and chest',
                                  'MRI of the neck and chest with and without gadolinium'],
                      'answer': 0,
                      'explanation': 'Contrast-enhanced CT is the workhorse for deep neck infection because it is fast '
                                     'and maps fascial spaces, rim-enhancing collections, gas, airway displacement, '
                                     'and vascular complications. Coverage should match the clinical question. His '
                                     'retrosternal pain with toxicity raises concern for descending infection through '
                                     'the retropharyngeal or danger space into the mediastinum, so the scan should '
                                     'extend through the chest. Missing mediastinal involvement leads to inadequate '
                                     'drainage and high mortality.',
                      'why_wrong': ['Correct.',
                                    'Neck-only coverage will not show mediastinal fluid or gas, which his retrosternal '
                                    'pain specifically raises as a concern.',
                                    'Without contrast, rim enhancement and vascular complications are hard to '
                                    'identify, and IV contrast does not obscure abscesses.',
                                    'MRI is slower and less available in a toxic patient, and chest MRI is limited by '
                                    'motion and poorly suited to emergency mediastinal evaluation.'],
                      'board_pearl': 'Deep neck infection with chest pain or sepsis: extend contrast CT through the '
                                     'chest to detect mediastinal spread.',
                      'curveball': 'The scan shows gas tracking along the fascia of the neck without a discrete fluid '
                                   'collection. What does this suggest and what is the next step?',
                      'curveball_answer': 'Gas dissecting along fascial planes without a discrete abscess in a toxic '
                                          'patient suggests necrotizing fasciitis rather than a simple abscess. It is '
                                          'a clinical and surgical emergency: secure the airway, resuscitate, give '
                                          'broad-spectrum antibiotics including anaerobic and toxin-suppressing '
                                          'coverage, and proceed to immediate wide operative debridement, with '
                                          'thoracic surgery involved if the mediastinum is affected.'},
 'v273_gen_img_snr': {'stem': 'A 27-year-old man was stabbed in the left neck between the cricoid and the angle of the '
                              'mandible 1 hour ago. Paramedics reported a rapidly enlarging hematoma and brief oral '
                              'bleeding. He now has blood pressure 128/80, a soft nonexpanding hematoma, no active '
                              'bleeding, a normal voice, and no neurologic deficit. Which imaging study is most '
                              'appropriate?',
                      'choices': ['Contrast-enhanced CT of the neck in the venous phase',
                                  'MR angiography of the neck',
                                  'Duplex ultrasound of the carotid arteries',
                                  'CT angiography of the neck'],
                      'answer': 3,
                      'explanation': 'He has soft signs of vascular injury, a history of expanding hematoma and oral '
                                     'bleeding, without current hard signs, and he is stable. The imaging protocol '
                                     'must answer the vascular question, so CT angiography is the study of choice: it '
                                     'is fast, shows intimal flaps, pseudoaneurysm, extravasation, and occlusion, and '
                                     'maps the wound trajectory toward the aerodigestive tract. Results direct '
                                     'observation, endovascular repair, or surgery. The airway and hemorrhage rescue '
                                     'plan remains in place throughout.',
                      'why_wrong': ['A venous-phase neck CT is timed for soft tissue and abscesses and can miss '
                                    'intimal injury or small pseudoaneurysms.',
                                    'MRA is slower, less available, difficult with monitoring equipment, and less '
                                    'suitable in acute trauma.',
                                    'Duplex is operator dependent and limited near the skull base, under hematoma, and '
                                    'in the upper neck, so it is not the first choice.',
                                    'Correct.'],
                      'board_pearl': 'Stable penetrating neck trauma with soft vascular signs: CT angiography is the '
                                     'imaging study of choice.',
                      'curveball': 'During the wait for CT, the hematoma begins expanding again and his blood pressure '
                                   'falls to 90/60. Should he still go to the scanner?',
                      'curveball_answer': 'No. An expanding hematoma with hypotension is now a hard sign, and he needs '
                                          'immediate operative or endovascular hemorrhage control without imaging '
                                          'delay. Secure the airway early because the hematoma can distort it, apply '
                                          'direct pressure, resuscitate with blood products, and proceed to the '
                                          'operating room or a hybrid suite for proximal and distal vascular control.'},
 'v139_gen_09': {'stem': 'A 67-year-old man with a bulky supraglottic squamous cell carcinoma is scheduled for direct '
                         'laryngoscopy and biopsy. He has inspiratory stridor when lying flat but breathes quietly '
                         'sitting upright, with oxygen saturation of 95%. Flexible laryngoscopy shows an exophytic '
                         'epiglottic mass obscuring most of the laryngeal inlet, with a narrow posterior glottic '
                         'chink. Which airway plan is safest?',
                 'choices': ['Rapid-sequence induction with a small tube and a videolaryngoscope',
                             'Secure the airway awake while he keeps breathing spontaneously',
                             'Supine contrast CT of the neck before any airway decision is made',
                             'IV dexamethasone and heliox, then biopsy under deep propofol sedation'],
                 'answer': 1,
                 'explanation': 'Positional stridor means he is maintaining a marginal airway through upright posture, '
                                'muscle tone, and spontaneous effort. Induction or paralysis can remove those '
                                'compensations and turn partial obstruction into complete obstruction, with mask '
                                'ventilation and laryngoscopy both likely to fail. The safe approach is a shared ENT '
                                'and anesthesia plan that secures the airway awake, by fiberoptic intubation or '
                                'tracheostomy under local anesthesia, with a surgical airway ready, before any '
                                'sedation that could abolish his own breathing.',
                 'why_wrong': ['Paralysis removes the tone holding his airway open, and a bulky epiglottic mass may '
                               'block the view even with videolaryngoscopy.',
                               'Correct.',
                               'Lying him supine and unmonitored in the scanner risks obstruction, and imaging should '
                               'not precede a secure airway plan.',
                               'Steroids and heliox may buy time, but deep sedation can abolish the tone and drive he '
                               'relies on to keep the airway patent.'],
                 'board_pearl': 'Positional stridor from a laryngeal tumor: keep spontaneous ventilation and secure '
                                'the airway awake before sedation or induction.',
                 'curveball': 'What anatomy would make awake tracheostomy preferable to awake fiberoptic intubation in '
                              'this patient?',
                 'curveball_answer': 'Awake tracheostomy is favored when the scope or tube would have to pass through '
                                     'or beside friable obstructing tumor, risking bleeding or complete occlusion, '
                                     'when the glottic opening cannot be seen, or when transoral access is limited by '
                                     'trismus. Favorable neck anatomy, a palpable trachea without tumor extension or '
                                     'prior radiation, makes the tracheostomy itself safer under local anesthesia.'},
 'v140_gen_09': {'stem': 'A 59-year-old man with a large base-of-tongue carcinoma and severe trismus, with a 1.5 cm '
                         'interincisal opening, needs an airway for panendoscopy. He sleeps sitting up, cannot '
                         'tolerate lying flat, and has a muffled voice. Flexible nasal endoscopy shows the tumor '
                         'filling the vallecula and pushing the epiglottis posteriorly. Which plan carries the '
                         'greatest risk?',
                 'choices': ['Awake fiberoptic nasotracheal intubation with ENT scrubbed for a surgical airway',
                             'Awake tracheostomy under local anesthesia with minimal sedation',
                             'IV induction and neuromuscular blockade before confirming ventilation',
                             'High-flow nasal oxygen during topicalization for awake intubation'],
                 'answer': 2,
                 'explanation': 'This patient has a predicted difficult mask ventilation and intubation: trismus '
                                'limits mouth opening and laryngoscope insertion, and a base-of-tongue mass displaces '
                                'the epiglottis and fills the oropharynx. Induction and paralysis remove the tone and '
                                'respiratory drive that hold his airway open and commit the team before they know they '
                                'can ventilate, risking a cannot-intubate, cannot-oxygenate emergency. Awake '
                                'techniques preserve spontaneous ventilation, and high-flow oxygen extends safe apnea '
                                'time during topicalization.',
                 'why_wrong': ['Awake fiberoptic intubation keeps spontaneous ventilation and is a standard approach '
                               'for predicted difficult airways with surgical backup available.',
                               'Awake tracheostomy under local anesthesia is a safe primary choice when transoral or '
                               'transnasal passage is unlikely to succeed.',
                               'Correct.',
                               'High-flow nasal oxygen during topicalization improves oxygen reserve and reduces '
                               'desaturation; it adds safety rather than risk.'],
                 'board_pearl': 'Predicted difficult airway with obstruction: do not induce and paralyze before '
                                'ventilation and intubation are assured.',
                 'curveball': 'What topicalization and sedation principles help an awake fiberoptic intubation succeed '
                              'without losing ventilation?',
                 'curveball_answer': 'Use thorough topical lidocaine to the nose, pharynx, and larynx, with nebulized '
                                     'or spray-as-you-go application and a nasal vasoconstrictor, staying within '
                                     'maximum dosing. Sedation should be minimal and titratable, such as low-dose '
                                     'dexmedetomidine or remifentanil, so the patient keeps breathing and can '
                                     'cooperate. Avoid long-acting benzodiazepines, and keep the surgeon ready for an '
                                     'awake surgical airway.'},
 'v270_gen_airway_fnd': {'stem': 'A 60-year-old woman with a large exophytic glottic tumor is awaiting laryngoscopy. '
                                 'Awake, she breathes quietly with mild stridor on exertion. While dozing in the '
                                 'preoperative area after a small dose of IV midazolam, she develops loud snoring, '
                                 'paradoxical chest movement, and oxygen saturation falling to 84%, which recover when '
                                 'she is roused. Which mechanism best explains why induction could produce complete '
                                 'obstruction?',
                         'choices': ['Tumor edema provoked by the intravenous induction agents',
                                     'Lower airway bronchospasm triggered by laryngeal stimulation',
                                     'Aspiration of gastric contents through an incompetent larynx',
                                     'Loss of pharyngeal and laryngeal tone and inspiratory drive'],
                         'answer': 3,
                         'explanation': 'Awake patients with a narrowed upper airway compensate with pharyngeal and '
                                        'laryngeal dilator muscle tone, active inspiratory effort, and posture. '
                                        'Sedation, induction, and paralysis abolish these compensations: the pharynx '
                                        'collapses around the lesion, the tongue falls back, and reduced drive limits '
                                        'the effort that keeps flow going. Her desaturation with a small dose of '
                                        'midazolam demonstrates that loss of tone alone can convert a marginal airway '
                                        'into near-complete obstruction, which is why an awake or spontaneously '
                                        'breathing plan is chosen.',
                         'why_wrong': ['Induction agents do not cause acute tumor swelling; the obstruction worsens '
                                       'because supporting muscle tone is lost.',
                                       'Bronchospasm can complicate airway surgery, but her snoring and paradoxical '
                                       'breathing reflect upper airway collapse, not lower airway narrowing.',
                                       'Aspiration is a separate risk; her rapid recovery on arousal points to loss of '
                                       'airway tone, not soiling of the lungs.',
                                       'Correct.'],
                         'board_pearl': 'Upper airway obstruction is held open by tone, drive, and posture; sedation '
                                        'or induction can remove all three at once.',
                         'curveball': 'Anesthesia proposes inhalational induction to preserve spontaneous ventilation. '
                                      'Why may this still fail in critical obstruction?',
                         'curveball_answer': 'Inhalational induction preserves breathing in principle, but a narrow '
                                             'airway slows uptake, so induction is prolonged, and as depth increases '
                                             'pharyngeal tone is lost and obstruction can still become complete. '
                                             'Coughing or laryngospasm in the excitement phase can worsen it. For '
                                             'critical laryngeal obstruction, awake tracheostomy under local '
                                             'anesthesia or a carefully prepared awake technique is often safer.'},
 'v270_gen_airway_snr': {'stem': 'A 71-year-old man with a near-obstructing supraglottic carcinoma has worsening '
                                 'stridor and cannot lie flat. Flexible laryngoscopy shows a friable mass that bleeds '
                                 'on contact and fills the laryngeal inlet, and the glottis cannot be seen. He has a '
                                 'thin neck with a palpable cricoid and trachea, no prior radiation, and no tumor in '
                                 'the anterior neck. Which airway plan is best?',
                         'choices': ['Awake fiberoptic intubation guided through the obstructing tumor',
                                     'Awake tracheostomy under local anesthesia with anesthesia standing by',
                                     'Inhalational induction followed by rigid bronchoscopy to core out the tumor',
                                     'Repeated deep sedation until oral instrumentation is tolerated'],
                         'answer': 1,
                         'explanation': 'The route should have the highest chance of securing the airway without '
                                        'crossing or destabilizing the obstructing lesion. Here the glottis is not '
                                        'visible and the tumor bleeds on contact, so a fiberoptic scope or tube would '
                                        'have to pass blindly through friable tissue, risking hemorrhage, a lost view, '
                                        'or complete occlusion. His neck anatomy is favorable, with palpable landmarks '
                                        'and no radiation or tumor, which makes awake tracheostomy under local '
                                        'anesthesia the safest primary plan, with anesthesia and ENT sharing one '
                                        'rescue strategy.',
                         'why_wrong': ['With no glottic view and a bleeding, friable mass, passing a scope through the '
                                       'tumor risks hemorrhage and conversion to complete obstruction.',
                                       'Correct.',
                                       'Inhalational induction in critical obstruction can still cause complete '
                                       'closure, and rigid bronchoscopy needs a skilled team as a rescue, not the '
                                       'first plan.',
                                       'Deep sedation abolishes the tone and drive he depends on and can precipitate '
                                       'complete obstruction before an airway is established.'],
                         'board_pearl': 'Choose the airway route that avoids traversing the obstructing lesion; '
                                        'favorable neck plus no glottic view favors awake tracheostomy.',
                         'curveball': 'How would prior radiation and a low, bulky neck mass change the surgical airway '
                                      'backup?',
                         'curveball_answer': 'Radiation fibrosis and a bulky mass obscure landmarks, deepen the '
                                             'trachea, and make tracheostomy slow and bloody, so it becomes a poor '
                                             'emergency bailout. The team may then favor awake fiberoptic intubation '
                                             'with a small tube by an expert, prepare rigid bronchoscopy and jet '
                                             'ventilation as rescues, and consider ECMO standby for truly critical '
                                             'obstruction. The incision site and backup should be marked before '
                                             'starting.'},
 'v139_gen_10': {'stem': 'A 36-year-old man has been unable to swallow since a piece of steak stuck behind his sternum '
                         '4 hours ago. He is spitting saliva into a cup and drooling, but breathing comfortably with '
                         'oxygen saturation of 99% and clear lungs. He has had two milder episodes in the past year '
                         'that passed on their own. Chest radiograph shows no free air. Which is the best next step?',
                 'choices': ['Flexible endoscopy within hours to clear the impacted bolus',
                             'IV glucagon and observation for spontaneous passage over 24 hours',
                             'Carbonated beverage to soften and advance the food bolus',
                             'Barium esophagram to define the level of the food bolus'],
                 'answer': 0,
                 'explanation': 'Inability to handle secretions signals complete esophageal obstruction, which risks '
                                'aspiration and progressive pressure injury to the wall, so endoscopy is performed '
                                'emergently, generally within about 6 hours, rather than electively. Flexible '
                                'endoscopy allows the bolus to be gently pushed into the stomach or retrieved '
                                'piecemeal, along with inspection for an underlying cause. Glucagon has little proven '
                                'benefit, and nothing should delay endoscopy in complete obstruction. His prior '
                                'episodes raise concern for eosinophilic esophagitis or a ring.',
                 'why_wrong': ['Correct.',
                               'Glucagon rarely clears impactions, and waiting 24 hours with complete obstruction '
                               'increases the risk of aspiration and mucosal necrosis.',
                               'Carbonated drinks have weak evidence, cannot be swallowed safely when secretions are '
                               'not passing, and increase aspiration risk.',
                               'Barium coats the mucosa, impairs endoscopic view, and risks aspiration in a patient '
                               'who cannot clear his secretions.'],
                 'board_pearl': 'Food impaction with inability to swallow secretions is complete obstruction and needs '
                                'emergent endoscopy.',
                 'curveball': 'After the bolus is cleared, what underlying disease should be investigated and how?',
                 'curveball_answer': 'Recurrent food impaction in a young man suggests eosinophilic esophagitis, which '
                                     'is found in a large share of adult impactions. Biopsies should be taken at the '
                                     'index endoscopy when safe, at least six from the proximal and distal esophagus, '
                                     'even if the mucosa looks normal. A Schatzki ring, peptic stricture, or motility '
                                     'disorder remain alternatives and may need esophagram or manometry.'},
 'v140_gen_07': {'stem': 'A 3-year-old girl was seen putting a coin-sized button battery in her mouth 90 minutes ago. '
                         'She is drooling slightly but breathing comfortably, and has no hematemesis. AP and lateral '
                         'radiographs show a round radiopaque disc with a double-ring halo at the thoracic inlet, in '
                         'the upper esophagus. She weighs 14 kg. What is the most appropriate management?',
                 'choices': ['Honey every 10 minutes and admission for observation overnight',
                             'Endoscopic removal within 24 hours if she remains asymptomatic',
                             'Emergent endoscopic removal as soon as the team can assemble',
                             'Repeat radiographs in 4 hours to see whether it has passed'],
                 'answer': 2,
                 'explanation': 'An esophageal button battery is a true emergency. The battery generates hydroxide at '
                                'the negative pole through current flow in the moist mucosa, causing liquefactive '
                                'necrosis that can begin within 2 hours and progress to perforation, tracheoesophageal '
                                'fistula, or aortoesophageal fistula. The double-ring halo distinguishes it from a '
                                'coin. Removal is emergent regardless of symptoms. Honey or sucralfate may be given '
                                'while awaiting endoscopy in children over 1 year within 12 hours of ingestion, but '
                                'they do not replace removal.',
                 'why_wrong': ['Honey can reduce injury while awaiting removal, but it is a bridge, not a substitute, '
                               'and overnight observation allows necrosis to progress.',
                               'Being asymptomatic does not protect her; deep injury occurs within hours, so a 24-hour '
                               'window is too slow for an esophageal battery.',
                               'Correct.',
                               'Waiting for passage is acceptable only for selected gastric batteries; an esophageal '
                               'battery must not be left in place.'],
                 'board_pearl': 'Esophageal button battery is an emergency: remove it immediately; honey or sucralfate '
                                'only bridges the wait.',
                 'curveball': 'After removal there is a deep posterior wall burn at the level of the aortic arch. What '
                              'follow-up is needed?',
                 'curveball_answer': 'Deep or circumferential injury, especially posterior or near the aorta, raises '
                                     'the risk of delayed aortoesophageal fistula, tracheoesophageal fistula, '
                                     'perforation, and stricture, sometimes days to weeks later. She should remain '
                                     'admitted, often NPO with nasogastric feeding, with contrast CT or MRA to assess '
                                     'the aorta before discharge and repeat imaging or endoscopy as recommended. '
                                     'Sentinel bleeding should prompt immediate vascular evaluation.'},
 'v270_gen_eso_fnd': {'stem': 'A 48-year-old woman swallowed her partial denture, which has two sharp metal clasps, '
                              'while sleeping. She now has pain on swallowing at the level of the sternal notch but '
                              'can swallow her saliva and breathes comfortably. Vital signs are normal. Lateral neck '
                              'and chest radiographs show the radiopaque appliance in the cervical esophagus, with no '
                              'subcutaneous or mediastinal air. Which management is most appropriate?',
                      'choices': ['Elective endoscopy in 24 hours because she is swallowing saliva',
                                  'Serial radiographs to follow the denture into the stomach',
                                  'Barium swallow to outline the clasps before any endoscopy',
                                  'Emergent endoscopic removal with overtube or hood protection'],
                      'answer': 3,
                      'explanation': 'Sharp-pointed esophageal foreign bodies, along with button batteries and '
                                     'complete obstruction, are treated emergently because they can perforate the '
                                     'esophageal wall within hours, leading to mediastinitis. Her ability to swallow '
                                     'saliva and a normal respiratory exam do not make this elective. Removal uses '
                                     'flexible or rigid esophagoscopy under direct vision, with an overtube, protector '
                                     'hood, or rigid scope sheath to shield the mucosa from the clasps during '
                                     'withdrawal. The mucosa is inspected for injury afterward.',
                      'why_wrong': ['Swallowing saliva excludes complete obstruction, but a sharp object still '
                                    'mandates emergent removal because of perforation risk.',
                                    'Sharp objects should not be left to pass from the esophagus, where perforation '
                                    'risk is high; observation applies to small blunt gastric objects.',
                                    'Barium delays definitive treatment, impairs endoscopic view, and adds nothing '
                                    'when plain films already localize a radiopaque object.',
                                    'Correct.'],
                      'board_pearl': 'Emergent esophageal foreign bodies: complete obstruction, button battery, and '
                                     'sharp-pointed objects, even if breathing is comfortable.',
                      'curveball': 'Why does an esophageal button battery demand an even faster pathway than this '
                                   'denture or a coin?',
                      'curveball_answer': 'A button battery causes active electrochemical injury: current through '
                                          'moist mucosa produces hydroxide at the negative pole, causing liquefactive '
                                          'necrosis that starts within 2 hours and continues even after removal. A '
                                          'coin causes only pressure injury, and a sharp object injures mainly at '
                                          'impaction or extraction. That time-dependent chemical burn is why batteries '
                                          'are removed immediately.'},
 'v270_gen_eso_snr': {'stem': 'A 29-year-old man with asthma and seasonal allergies presents with his third food '
                              'impaction in 2 years. Endoscopy clears a chicken bolus from the distal esophagus. The '
                              'mucosa shows concentric rings, linear furrows, and scattered white exudates, without '
                              'stricture or perforation. He takes no acid-suppressing medication. Which step is best '
                              'at this endoscopy?',
                      'choices': ['Biopsy proximal and distal esophagus for eosinophilic esophagitis',
                                  'Dilate the rings now and discharge without further testing',
                                  'Start a PPI and repeat endoscopy only if impaction recurs',
                                  'Arrange esophageal manometry for a motility disorder before any biopsy'],
                      'answer': 0,
                      'explanation': 'Recurrent food impaction in a young atopic man with rings, furrows, and white '
                                     'exudates is the classic picture of eosinophilic esophagitis. Extraction ends the '
                                     'emergency, but preventing recurrence requires diagnosis. Current consensus '
                                     'recommends at least six biopsies from at least two levels of the esophagus, '
                                     'since disease is patchy and diagnosis requires 15 or more eosinophils per '
                                     'high-power field. Confirming the diagnosis directs treatment with PPI, swallowed '
                                     'topical steroids, dietary elimination, or dupilumab, and dilation is used for '
                                     'fibrostenotic narrowing.',
                      'why_wrong': ['Correct.',
                                    'Dilation treats fixed narrowing, but skipping biopsy leaves the inflammatory '
                                    'cause untreated and the recurrence risk unchanged.',
                                    'A PPI is a first-line therapy for eosinophilic esophagitis, but starting it '
                                    'without biopsy forfeits the diagnosis and may mask histology.',
                                    'Manometry is reserved for suspected motility disorders; his endoscopic findings '
                                    'point to an inflammatory cause that biopsy can confirm.'],
                      'board_pearl': 'Recurrent food impaction with rings and furrows: take at least six biopsies from '
                                     'two levels to diagnose eosinophilic esophagitis.',
                      'curveball': 'During extraction the bolus is difficult, and afterward he has chest pain and '
                                   'crepitus at the neck. How does suspected perforation change management?',
                      'curveball_answer': 'Suspected perforation calls for urgent CT of the neck and chest with oral '
                                          'water-soluble contrast, keeping him NPO, starting broad-spectrum IV '
                                          'antibiotics, and involving thoracic surgery. Biopsy and dilation are '
                                          'deferred. Small contained perforations may be managed nonoperatively or '
                                          'with endoscopic clips or stents, while uncontained leaks with mediastinal '
                                          'contamination need surgical drainage and repair.'},
 'v139_gen_11': {'stem': 'A 67-year-old man with resected oral cavity cancer asks whether he should receive an '
                         'adjuvant drug. A national database study found that patients given the drug had better '
                         '3-year survival than those not given it. In that study, treated patients were younger, had '
                         'better performance status, and had fewer comorbidities. Which problem most limits the '
                         'conclusion that the drug improves survival?',
                 'choices': ['Lead-time bias from earlier detection',
                             'Recall bias in exposure reporting',
                             'Confounding by indication',
                             'Type II error from low power'],
                 'answer': 2,
                 'explanation': 'In observational studies, clinicians choose treatment based on prognosis. Here '
                                'healthier, younger patients were more likely to receive the drug, and those same '
                                'features independently improve survival, so the comparison mixes the drug effect with '
                                'baseline differences. This is confounding by indication, a form of selection bias. '
                                'Multivariable adjustment and propensity methods reduce imbalance in measured factors, '
                                'but unmeasured confounders such as frailty or social support remain, so only '
                                'randomization can balance them reliably.',
                 'why_wrong': ['Lead-time bias arises when earlier diagnosis lengthens apparent survival, as in '
                               'screening studies, not when healthier patients receive treatment.',
                               'Recall bias affects self-reported exposures in case-control studies, whereas treatment '
                               'here was recorded in a database.',
                               'Correct.',
                               'A type II error is failing to find a true effect; this study found a difference, and '
                               'the concern is that it is biased.'],
                 'board_pearl': 'When prognosis influences who gets treated, observational benefit may reflect '
                                'confounding by indication, not the treatment.',
                 'curveball': 'What does a confidence interval add beyond the p value when reading this study?',
                 'curveball_answer': 'The p value only indicates whether data are surprising under no effect, while '
                                     'the confidence interval gives the range of effect sizes compatible with the data '
                                     'and shows precision. A hazard ratio of 0.80 with 95% CI 0.65 to 0.98 suggests '
                                     'anything from a substantial to a trivial benefit. Neither, however, corrects '
                                     'bias: a precise estimate can still be precisely confounded.'},
 'v147_gen_05': {'stem': 'A 62-year-old woman with T2N1 HPV-associated oropharyngeal cancer asks about transoral '
                         'robotic surgery. She reads a retrospective institutional series reporting better swallowing '
                         'scores after surgery than after primary chemoradiation. In that series, surgeons offered '
                         'robotic surgery mainly to patients with small, well-exposed tumors, good dentition, and few '
                         'comorbidities. Which bias most threatens the conclusion?',
                 'choices': ['Lead-time bias from earlier detection',
                             'Confounding by indication',
                             'Publication bias favoring positive series',
                             'Attrition bias from loss to follow-up'],
                 'answer': 1,
                 'explanation': 'Treatment choice in this series was driven by features that also predict good '
                                'swallowing outcomes: small tumors, good exposure, and fewer comorbidities. The '
                                'surgical group therefore started with a better prognosis, so better scores may '
                                'reflect patient selection rather than the operation. This is confounding by '
                                'indication. Matching, regression, and propensity scores can balance measured factors '
                                'but not unmeasured ones. In the randomized ORATOR trial, 1-year swallowing quality of '
                                'life slightly favored radiotherapy, by less than the clinically meaningful margin.',
                 'why_wrong': ['Lead-time bias inflates survival when disease is found earlier; it does not explain '
                               'better swallowing after one chosen treatment.',
                               'Correct.',
                               'Publication bias concerns which studies get published across the literature, not '
                               'imbalance within this series.',
                               'Attrition bias requires differential loss to follow-up, which is not described; the '
                               'problem lies in how patients were assigned.'],
                 'board_pearl': 'Surgical case series select favorable patients; better outcomes may reflect selection '
                                'rather than technique.',
                 'curveball': 'What problem does propensity-score matching address in such a study, and what can it '
                              'not fix?',
                 'curveball_answer': "Propensity scores estimate each patient's probability of receiving surgery from "
                                     'measured covariates, and matching on them balances those covariates between '
                                     'groups, mimicking randomization for observed factors. They cannot balance '
                                     'unmeasured confounders such as surgeon judgment of exposure or frailty, and '
                                     'matching may discard patients and reduce generalizability. Balance should be '
                                     'checked with standardized mean differences.'},
 'v274_gen_evidence_fnd': {'stem': 'A 30-year-old man asks whether adding perioperative gabapentin will reduce his '
                                   'opioid use after tonsillectomy. A randomized trial reported a mean reduction of 12 '
                                   'morphine milligram equivalents over the first week, with a 95% confidence interval '
                                   'of 1 to 23. The investigators considered a reduction of 15 or more to be '
                                   'clinically meaningful. Which interpretation of the confidence interval is best?',
                           'choices': ['95% of patients will reduce their opioid use by 1 to 23 units',
                                       'There is a 95% probability that the study was free of bias',
                                       'The result is not statistically significant because the interval is wide',
                                       'The data fit effects ranging from trivial to clinically meaningful'],
                           'answer': 3,
                           'explanation': 'A 95% confidence interval gives the range of effect sizes compatible with '
                                          'the data under the study model, conveying precision. Here it excludes zero, '
                                          'so the result is statistically significant, but it spans a trivial 1-unit '
                                          'reduction to a meaningful 23-unit reduction, and the point estimate falls '
                                          'below the 15-unit threshold. The honest conclusion is that a benefit is '
                                          'likely but its clinical importance is uncertain. The interval describes the '
                                          'average effect, not individual responses, and says nothing about bias.',
                           'why_wrong': ['The interval describes uncertainty in the average treatment effect, not the '
                                         'spread of individual patient responses.',
                                         'Confidence intervals reflect random error only; they do not measure or '
                                         'exclude bias in study design or conduct.',
                                         'An interval that excludes zero is statistically significant; width reflects '
                                         'precision, not significance.',
                                         'Correct.'],
                           'board_pearl': 'A confidence interval shows the range of plausible average effects; compare '
                                          'both ends with the clinically important difference.',
                           'curveball': 'How would a narrow interval around a clinically trivial effect change your '
                                        'conclusion?',
                           'curveball_answer': 'A narrow interval, such as a 2-unit reduction with 95% CI 1 to 3, '
                                               'shows a precise estimate that is statistically significant but '
                                               'entirely below the 15-unit meaningful threshold. That excludes an '
                                               'important benefit, so the drug would not be worth its sedation and '
                                               'dizziness risks for this purpose. Precision and clinical relevance are '
                                               'separate questions.'},
 'v274_gen_evidence_app': {'stem': 'A 55-year-old man scheduled for thyroid lobectomy asks which vessel-sealing '
                                   'technique his surgeon will use. A retrospective review of 900 patients reports '
                                   'fewer complications with technique A. The authors note that surgeons chose '
                                   'technique A for younger patients without diabetes or anticoagulant use and chose '
                                   'technique B for higher-risk patients. Which conclusion is best supported by this '
                                   'study?',
                           'choices': ['Technique A causes fewer complications and should be adopted',
                                       'Technique B is harmful and should be abandoned for all patients',
                                       'Baseline risk differences may explain the gap between techniques',
                                       'The study shows no difference because it was not a randomized trial'],
                           'answer': 2,
                           'explanation': 'When treatment assignment depends on baseline risk, outcomes may differ '
                                          'simply because the groups differed at the start. Healthier patients without '
                                          'diabetes or anticoagulation have fewer complications regardless of '
                                          'technique, so the observed association cannot be read as causal. This is '
                                          'confounding by indication. Adjustment or propensity methods can reduce '
                                          'imbalance in measured factors but not unmeasured ones. The study generates '
                                          'a hypothesis that a randomized or well-adjusted comparison would need to '
                                          'test.',
                           'why_wrong': ['Inferring causation ignores that healthier patients were selected for '
                                         'technique A, so the benefit may reflect selection rather than the technique.',
                                         'Higher complications with technique B are expected in the higher-risk '
                                         'patients assigned to it and do not prove harm.',
                                         'Correct.',
                                         'Lack of randomization limits causal inference, but it does not show absence '
                                         'of a difference; it leaves the question unresolved.'],
                           'board_pearl': 'Observational association with risk-based treatment choice generates '
                                          'hypotheses but does not prove a technique is better.',
                           'curveball': 'If the authors performed propensity matching, which balance diagnostics would '
                                        'you inspect?',
                           'curveball_answer': 'Check standardized mean differences for each covariate after matching, '
                                               'generally aiming for values below 0.1, and compare distributions of '
                                               'the propensity score to confirm adequate overlap. Note how many '
                                               'patients went unmatched, because discarding high-risk patients changes '
                                               'who the result applies to. Balance on measured factors still leaves '
                                               'unmeasured confounders unaddressed.'},
 'v274_gen_evidence_snr': {'stem': 'A 52-year-old woman with chronic rhinosinusitis asks about a new sinus surgery '
                                   'technique she read about. A randomized trial of 600 patients reported a 1-point '
                                   'greater improvement on a 100-point symptom scale than standard surgery, p = 0.03, '
                                   'with no difference in complications. The minimal clinically important difference '
                                   'for this scale is 8 points. As the chief resident, how should you interpret this '
                                   'result?',
                           'choices': ['Adopt the technique because p below 0.05 establishes superiority',
                                       'Statistically significant but too small to matter clinically',
                                       'Disregard the result because symptom scales are unreliable',
                                       'Likely a false-negative result requiring a larger trial'],
                           'answer': 1,
                           'explanation': 'Large trials can detect statistically significant differences that are too '
                                          'small to matter to patients. A 1-point difference on a 100-point scale is '
                                          'well below the 8-point minimal clinically important difference, so although '
                                          'chance is an unlikely explanation, the benefit is unlikely to be '
                                          'noticeable. Before changing practice, a chief should also weigh the '
                                          'confidence interval, risk of bias, durability of follow-up, cost, learning '
                                          'curve, and whether the trial population resembles their own patients.',
                           'why_wrong': ['A p value addresses chance, not magnitude; a 1-point gain far below the '
                                         'meaningful threshold does not justify changing practice.',
                                         'Correct.',
                                         'Validated patient-reported outcomes are standard endpoints in rhinology; the '
                                         'issue is the size of the effect, not the instrument.',
                                         'The trial found a statistically significant difference, so a false-negative '
                                         'error does not apply here.'],
                           'board_pearl': 'Statistical significance is not clinical importance; compare the effect and '
                                          'its interval with the minimal clinically important difference.',
                           'curveball': 'How would a noninferiority design change the questions you ask about this '
                                        'trial?',
                           'curveball_answer': 'In a noninferiority trial, ask whether the margin was prespecified and '
                                               'clinically justified, whether the upper bound of the confidence '
                                               'interval for worse outcomes stays within it, and whether the '
                                               'comparator was given at its proven effective standard. Review both '
                                               'per-protocol and intention-to-treat analyses, because poor adherence '
                                               'biases noninferiority results toward showing no difference.'},
 'v139_gen_12': {'stem': 'An 84-year-old woman has a technically resectable T3N0 squamous cell carcinoma of the '
                         'lateral tongue. She has advanced dementia, needs help with bathing, dressing, and toileting, '
                         'has fallen three times this year, and has lost 8% of her weight. Her daughter, the health '
                         'care proxy, says her mother valued staying at home. The tumor board asks how to plan '
                         'treatment. What should guide the recommendation?',
                 'choices': ['Geriatric assessment of reserve, cognition, and goals with the proxy',
                             'Proceed with glossectomy and free flap because the tumor is resectable',
                             'Recommend no treatment because of her chronological age',
                             'Offer concurrent chemoradiation as a less invasive standard option'],
                 'answer': 0,
                 'explanation': 'Chronological age alone neither mandates nor excludes treatment. Her dementia, '
                                'dependence in activities of daily living, falls, and weight loss indicate severe '
                                'frailty, which predicts complications, delirium, institutionalization, and death '
                                'after major surgery far better than age. Geriatric assessment clarifies reserve and '
                                'competing mortality, and a goals-of-care discussion with her proxy aligns options '
                                'with what she valued. Choices may range from resection to palliative radiation or '
                                'symptom-focused care, chosen deliberately rather than by resectability or age.',
                 'why_wrong': ['Correct.',
                               'Technical resectability ignores frailty, cognition, and goals, and major '
                               'reconstruction may cost her function and independence without benefit.',
                               'Excluding treatment by age alone is inappropriate; her frailty and goals, not her '
                               'birth date, should drive the decision.',
                               'Concurrent chemoradiation is highly toxic in a frail patient with dementia and weight '
                               'loss and is not automatically gentler than surgery.'],
                 'board_pearl': 'Treatment for older patients follows frailty, function, cognition, and goals, not '
                                'chronological age or resectability alone.',
                 'curveball': 'If she were less frail and surgery were chosen, which prehabilitation strategies might '
                              'reduce perioperative risk?',
                 'curveball_answer': 'Useful strategies include nutritional supplementation or early tube feeding for '
                                     'weight loss, supervised exercise and strength training, inspiratory muscle '
                                     'training, smoking and alcohol cessation, medication review to remove '
                                     'deliriogenic or redundant drugs, and anemia correction. Preoperative swallow '
                                     'therapy and caregiver preparation help, and delirium prevention plans should be '
                                     'set before admission.'},
 'v147_gen_06': {'stem': 'A 79-year-old man is being evaluated for total laryngectomy with neck dissection for a T4a '
                         'glottic cancer. He uses a walker, has lost 10 lb in 6 months, reports exhaustion, and has a '
                         'slow gait and weak grip. He has hypertension and well-controlled diabetes, and his ASA class '
                         'is 3. His family asks what best predicts his risk of complications and of not returning '
                         'home. Which factor is most predictive?',
                 'choices': ['His chronological age',
                             'His ASA physical status class',
                             'His frailty on a validated index',
                             'His clinical tumor stage'],
                 'answer': 2,
                 'explanation': 'Frailty is a state of reduced physiologic reserve across multiple systems. Validated '
                                'measures, such as the modified frailty index or the Fried phenotype of weight loss, '
                                'exhaustion, weakness, slow gait, and low activity, predict complications, delirium, '
                                'prolonged stay, nonhome discharge, and mortality after head and neck surgery better '
                                'than age or ASA class. This patient shows most of the Fried criteria. Identifying '
                                'frailty supports prehabilitation, realistic counseling, and consideration of less '
                                'burdensome treatment.',
                 'why_wrong': ['Age correlates with risk, but older patients differ widely in reserve, and age alone '
                               'predicts outcomes less well than frailty.',
                               'ASA class captures comorbidity grossly and is subjective; frailty indices add '
                               'independent prediction of complications and discharge.',
                               'Correct.',
                               'Stage guides the oncologic plan, but his perioperative risk and recovery depend more '
                               'on physiologic reserve.'],
                 'board_pearl': 'Frailty predicts complications, nonhome discharge, and mortality after head and neck '
                                'surgery better than age.',
                 'curveball': 'What prehabilitation domains could be optimized in the weeks before his laryngectomy?',
                 'curveball_answer': 'Nutrition, with supplements or prophylactic gastrostomy; physical conditioning '
                                     'with walking and resistance exercise; medication review and deprescribing; '
                                     'glycemic control; anemia correction; and cognitive and mood screening with '
                                     'delirium prevention planning. Speech pathology preparation for alaryngeal '
                                     'communication and early caregiver training also improve recovery and support '
                                     'discharge home.'},
 'v274_gen_frail_fnd': {'stem': 'Two patients are scheduled for the same parotidectomy. An 81-year-old man lives '
                                'alone, walks 3 miles daily, and manages his own finances. A 68-year-old woman has '
                                'lost 12 lb unintentionally, tires after one flight of stairs, walks slowly, and has a '
                                'weak grip. Both have similar comorbidities and ASA class. Which statement best '
                                'explains why the younger patient may face higher surgical risk?',
                        'choices': ['Her younger age makes anesthetic drug clearance slower',
                                    'Her ASA class predicts higher risk than his for this surgery',
                                    'Women have higher parotidectomy complication rates than men',
                                    'She has frailty, reflecting reduced physiologic reserve'],
                        'answer': 3,
                        'explanation': 'Frailty is reduced physiologic reserve and increased vulnerability to '
                                       'stressors, independent of chronological age. The younger woman meets several '
                                       'Fried phenotype criteria: unintentional weight loss, exhaustion, slow gait, '
                                       'and weakness. These predict postoperative complications, delirium, prolonged '
                                       'recovery, and loss of independence. The older man is robust despite his age. '
                                       'This is why preoperative assessment should measure function and reserve rather '
                                       'than infer risk from age or comorbidity count alone.',
                        'why_wrong': ['Drug clearance generally declines with age, so younger age does not explain '
                                      'higher risk; her reduced reserve does.',
                                      'The stem states their ASA classes are similar, so ASA cannot distinguish their '
                                      'risks.',
                                      'Sex is not a recognized major predictor of parotidectomy complications and does '
                                      'not account for her functional decline.',
                                      'Correct.'],
                        'board_pearl': 'Frailty is diminished physiologic reserve; it can affect younger patients and '
                                       'spare robust older ones.',
                        'curveball': 'If both patients proceed with surgery, which bedside frailty features would most '
                                     'change the discharge planning for the younger woman?',
                        'curveball_answer': 'Slow gait or a prolonged timed up-and-go test, recent falls, cognitive '
                                            'impairment, dependence in daily activities, and weight loss predict '
                                            'nonhome discharge and readmission. Living alone or lacking a caregiver '
                                            'compounds risk. Identifying these early allows physical therapy, home '
                                            'services, or rehabilitation placement to be arranged before surgery.'},
 'v274_gen_frail_app': {'stem': 'An 82-year-old woman with a resectable T2N1 oral cavity carcinoma lives '
                                'independently. She has lost 7% of her weight, walks slowly, takes 11 medications '
                                'including a benzodiazepine for sleep, and scores 23 of 30 on a cognitive screen. '
                                'Surgery is planned in 3 weeks. Her son asks how the team will prepare. What is the '
                                'best preoperative approach?',
                        'choices': ['Geriatric assessment, deprescribing, nutrition, and delirium planning',
                                    'Use the standard pathway because she currently lives fully independently',
                                    'Recommend palliative care only because she is over 80',
                                    'Defer surgery 3 months for prehabilitation despite the nodal disease'],
                        'answer': 0,
                        'explanation': 'Age alone should not exclude curative surgery, but her weight loss, slow gait, '
                                       'polypharmacy, and mild cognitive impairment mark her as frail and at high risk '
                                       'for delirium, complications, and nonhome discharge. A geriatric assessment '
                                       'identifies modifiable factors: tapering the benzodiazepine, reducing other '
                                       'deliriogenic drugs, nutrition support, and exercise. Delirium prevention, '
                                       'early mobility, family presence, and discharge needs are planned in advance, '
                                       'and these risks are incorporated into shared decision-making within the '
                                       'oncologic time frame.',
                        'why_wrong': ['Correct.',
                                      'Living independently does not offset her frailty markers, and a standard '
                                      'pathway misses delirium, nutrition, and medication risks.',
                                      'Age over 80 is not a reason to forgo curative treatment in a patient who can be '
                                      'optimized and wants treatment.',
                                      'Prehabilitation should fit the oncologic window; a 3-month delay with nodal '
                                      'disease risks progression beyond curability.'],
                        'board_pearl': 'Frail older surgical patients need geriatric assessment, deprescribing, '
                                       'nutrition, and delirium planning, not age-based exclusion.',
                        'curveball': 'What findings during workup would shift the discussion toward less morbid '
                                     'oncologic options?',
                        'curveball_answer': 'Severe frailty or dependence in daily activities, moderate to severe '
                                            'dementia that limits participation in rehabilitation, poor '
                                            'cardiopulmonary reserve, limited life expectancy from competing illness, '
                                            'or a patient who prioritizes avoiding major functional loss would favor '
                                            'less extensive surgery, primary radiation, or palliative approaches. '
                                            'Shared decision-making should present expected function as well as '
                                            'survival.'},
 'v274_gen_frail_snr': {'stem': 'An 80-year-old man is on postoperative day 3 after composite resection and free flap. '
                                'He has become quiet and sleepy, stares at the wall, and answers slowly with '
                                'inattention on testing. He is eating little, has not walked since surgery, and has a '
                                'urinary catheter. He is receiving scheduled IV opioids. Oxygen saturation is 95% on '
                                'room air. What is the best management?',
                        'choices': ['Observe on bed rest, as this reflects his age and the surgery',
                                    'Treat reversible causes and use nonpharmacologic delirium care',
                                    'Lorazepam at night to restore his sleep and alertness',
                                    'Head CT for an acute stroke before any other evaluation or changes'],
                        'answer': 1,
                        'explanation': 'Quiet inattention with sleepiness is hypoactive delirium, which is common, '
                                       'often missed, and associated with longer stay, functional decline, and '
                                       'mortality. It is usually multifactorial, so the priority is to search for and '
                                       'correct triggers: infection, hypoxia or hypercapnia, urinary retention, '
                                       'constipation, dehydration, electrolyte disturbance, pain, and deliriogenic '
                                       'drugs, here scheduled opioids. Nonpharmacologic care, including early '
                                       'mobilization, sleep protection, orientation, glasses and hearing aids, family '
                                       'presence, and catheter removal, is first-line.',
                        'why_wrong': ['Hypoactive delirium is not normal aging, and bed rest promotes deconditioning, '
                                      'pneumonia, and prolonged delirium.',
                                      'Correct.',
                                      'Benzodiazepines worsen delirium in older adults and should be avoided except '
                                      'for alcohol or benzodiazepine withdrawal.',
                                      'Imaging is reserved for focal deficits, head trauma, or unexplained '
                                      'persistence; most postoperative delirium has systemic causes.'],
                        'board_pearl': 'Postoperative hypoactive delirium: search for reversible triggers, reduce '
                                       'deliriogenic drugs, and mobilize early.',
                        'curveball': 'His delirium persists for 5 days despite correcting his medications and '
                                     'catheter. When does persistent delirium require neuroimaging or specialty '
                                     'consultation?',
                        'curveball_answer': 'Obtain brain imaging for new focal neurologic deficits, a fall or head '
                                            'injury especially on anticoagulation, or delirium that persists without a '
                                            'systemic explanation after triggers are corrected. Seizure concerns '
                                            'warrant EEG. Geriatrics or psychiatry consultation helps when delirium is '
                                            'prolonged, severe agitation threatens the flap or airway, or medication '
                                            'management becomes complex.'},
 'v139_gen_13': {'stem': 'A 63-year-old man had anterior segmental mandibulectomy for squamous cell carcinoma, '
                         'reconstructed with a titanium plate and soft-tissue flap, followed by 66 Gy of radiation. '
                         'Two years later the plate is exposed through the chin skin with purulent drainage. CT shows '
                         'lucency around three loose screws and no recurrent tumor. Two courses of oral antibiotics '
                         'have failed. What is the best management?',
                 'choices': ['Long-term suppressive oral antibiotics with local wound care at home only',
                             'Debride the skin edges and close primarily over the existing plate',
                             'Hyperbaric oxygen alone to promote healing over the exposed plate',
                             'Remove the plate, debride, and restore vascularized bone and coverage'],
                 'answer': 3,
                 'explanation': 'Implants depend on a healthy host bed and durable coverage. Irradiated tissue is '
                                'hypovascular, hypocellular, and fibrotic, and once a plate is exposed, infected, and '
                                'loose, it is colonized by biofilm that antibiotics cannot sterilize. Salvage requires '
                                'removal of the compromised hardware, debridement of infected and nonviable bone and '
                                'soft tissue, and import of well-vascularized nonirradiated tissue, typically a free '
                                'fibula or other osteocutaneous flap, to restore the mandible and skin coverage.',
                 'why_wrong': ['Antibiotics cannot sterilize biofilm on a loose, exposed plate, and suppression only '
                               'delays definitive treatment while infection progresses.',
                               'Closing irradiated skin under tension over an infected plate fails predictably because '
                               'the bed cannot heal and the source remains.',
                               'Hyperbaric oxygen may be an adjunct in irradiated wounds, but it cannot treat a loose, '
                               'infected, exposed plate on its own.',
                               'Correct.'],
                 'board_pearl': 'Exposed, infected, loose hardware in an irradiated field: remove it, debride, and '
                                'bring in vascularized tissue.',
                 'curveball': 'When is autologous tissue preferable to alloplastic material in head and neck '
                              'reconstruction?',
                 'curveball_answer': 'Autologous tissue is preferred in irradiated, contaminated, or poorly '
                                     'vascularized beds, where implants face higher infection and extrusion rates, and '
                                     'when coverage is thin or under tension. Autologous cartilage, bone, and '
                                     'vascularized flaps integrate and resist infection better and can be revised. '
                                     'Alloplasts suit clean, well-covered, low-tension sites where donor morbidity '
                                     'matters.'},
 'v147_gen_07': {'stem': 'A 66-year-old man had maxillectomy with titanium mesh orbital floor and zygoma '
                         'reconstruction, followed by radiation. Eighteen months later a 1 cm area of mesh is exposed '
                         'through thin cheek skin. There is no purulence, erythema, or fluid collection, the mesh is '
                         'fixed and stable on palpation, and CT shows no recurrence. He asks whether the mesh can be '
                         'saved. Which factor best predicts salvage success?',
                 'choices': ['Starting long-term oral antibiotics at the time of exposure',
                             'No infection, a stable implant, and vascularized tissue to cover it',
                             'The interval since radiation was completed before the exposure occurred',
                             'Advancing the adjacent irradiated cheek skin to close the defect'],
                 'answer': 1,
                 'explanation': 'Implant salvage depends on the host bed. A stable, uninfected implant that can be '
                                'covered with durable, well-vascularized tissue, such as a regional or free flap '
                                'brought into the irradiated field, has a reasonable chance of salvage. Infection with '
                                'biofilm, implant motion, persistent tension, and inability to provide vascularized '
                                'coverage predict failure, in which case removal is usually needed. Local irradiated '
                                'skin is poor coverage because it is hypovascular and already failed once.',
                 'why_wrong': ['Antibiotics do not create coverage and cannot sterilize biofilm; without healthy '
                               'tissue over the mesh, exposure persists.',
                               'Correct.',
                               'Radiation injury to vessels is progressive and does not reliably improve with time, so '
                               'the interval since treatment is a weak predictor.',
                               'The surrounding skin is irradiated and has already broken down, so advancing it under '
                               'tension is likely to fail again.'],
                 'board_pearl': 'Exposed implant salvage needs no infection, a stable implant, and durable '
                                'vascularized coverage; otherwise remove it.',
                 'curveball': 'How does autologous cartilage differ from synthetic material in its behavior when '
                              'infected or exposed?',
                 'curveball_answer': 'Autologous cartilage is living tissue without a foreign surface for biofilm, so '
                                     'a small exposure or infection can often be managed with debridement, '
                                     'antibiotics, and coverage while the graft is kept. Synthetic implants harbor '
                                     'biofilm on their surface, so infection or exposure usually requires removal. '
                                     'Cartilage can resorb or warp, whereas alloplasts keep shape but carry lifelong '
                                     'extrusion risk.'},
 'v274_gen_graft_fnd': {'stem': 'A 64-year-old man undergoes lateral temporal bone resection for recurrent cutaneous '
                                'squamous cell carcinoma in a previously irradiated field. To save time, a '
                                'split-thickness skin graft is placed directly over the exposed bare cortical mastoid '
                                'and squamous temporal bone, which has no periosteum. One week later the graft is '
                                'pale, nonadherent, and necrotic over the bone. Which principle best explains this '
                                'outcome?',
                        'choices': ['Split-thickness grafts lack enough dermis to survive on any recipient bed',
                                    'The graft failed from rejection because it was harvested too thin',
                                    'A graft relies on its recipient bed, while a flap carries its own supply',
                                    'Radiation increases bed vascularity but causes graft contraction'],
                        'answer': 2,
                        'explanation': 'A free graft has no blood supply of its own. For the first days it survives by '
                                       'plasmatic imbibition, absorbing nutrients from the bed, and then by '
                                       'inosculation and ingrowth of new vessels from the recipient bed. Bare '
                                       'irradiated cortical bone without periosteum cannot provide this, so the graft '
                                       'dies. A flap is transferred with an intrinsic pedicle or microvascular inflow '
                                       'and outflow and can therefore cover avascular bone, which is why a regional or '
                                       'free flap is used for such defects.',
                        'why_wrong': ['Split-thickness grafts survive well on vascular beds such as muscle, fascia, '
                                      'periosteum, and granulation tissue; the bed was the problem.',
                                      'An autograft is not rejected immunologically, and thinner grafts actually take '
                                      'more easily because they need less nutrition.',
                                      'Correct.',
                                      'Radiation reduces rather than increases vascularity, making the bed even less '
                                      'able to support a graft.'],
                        'board_pearl': 'Grafts survive by imbibition and inosculation from the bed; flaps bring their '
                                       'own blood supply.',
                        'curveball': 'If the defect had been only a small area of bare bone in a nonirradiated field, '
                                     'could a graft still be used?',
                        'curveball_answer': 'Yes, with preparation. Burring the outer cortex to bleeding diploe or '
                                            'allowing granulation tissue to form, sometimes over weeks with dermal '
                                            'regeneration templates, creates a vascular bed that will accept a '
                                            'split-thickness graft. Small areas of avascular bed may also be bridged '
                                            'by graft from surrounding vascular tissue. Irradiated bone usually '
                                            'responds poorly, which favors a flap.'},
 'v274_gen_graft_app': {'stem': 'A 45-year-old man developed a septal abscess after nasal trauma 1 year ago, with loss '
                                'of septal cartilage and now a saddle-nose deformity with poor tip support. The dorsal '
                                'skin is thin, and there is little remaining septal cartilage. He does not use cocaine '
                                'and has no autoimmune disease. He asks which material will be used to rebuild his '
                                'dorsum. Which choice is most appropriate?',
                        'choices': ['Autologous costal cartilage graft for dorsal and septal support',
                                    'Silicone dorsal implant placed beneath the thin skin envelope',
                                    'Porous polyethylene dorsal implant carved to fill the dorsal defect',
                                    'Hyaluronic acid filler injected along the dorsum in stages'],
                        'answer': 0,
                        'explanation': 'Material choice must match mechanical demand, infection risk, and soft-tissue '
                                       'coverage. A saddle nose after septal abscess needs strong structural support '
                                       'of the septum and dorsum. With a previously infected field, thin skin, and '
                                       'little septal cartilage, autologous costal cartilage is preferred: it provides '
                                       'enough volume and strength, integrates as living tissue, and resists infection '
                                       'and extrusion better than alloplasts. Warping is reduced by carving balanced '
                                       'cross-sections or by using diced cartilage techniques.',
                        'why_wrong': ['Correct.',
                                      'Silicone under thin dorsal skin has a substantial risk of extrusion, '
                                      'visibility, and infection, especially after a prior septal infection.',
                                      'Porous polyethylene allows tissue ingrowth but is hard to remove if infected '
                                      'and risks exposure beneath thin, previously infected skin.',
                                      'Filler may camouflage a minor dorsal dip, but it provides no structural septal '
                                      'or tip support and is not a reconstruction.'],
                        'board_pearl': 'Structural nasal reconstruction in a previously infected or thinly covered '
                                       'field favors autologous cartilage over alloplasts.',
                        'curveball': 'When might vascularized tissue be needed before any structural graft is placed?',
                        'curveball_answer': 'When the lining or skin envelope is inadequate, as after radiation, '
                                            'extensive necrosis, or full-thickness nasal loss, a structural graft has '
                                            'no healthy bed and will become exposed or infected. Lining is restored '
                                            'first with local mucosal, septal, or turbinate flaps or a free flap, and '
                                            'skin with a forehead flap, then cartilage or bone is placed in a later '
                                            'stage.'},
 'v274_gen_graft_snr': {'stem': 'A 52-year-old woman had a porous polyethylene chin implant placed 3 years ago. She '
                                'now has her third episode of submental cellulitis in 6 months with a small draining '
                                'sinus below the chin. Each episode improved with antibiotics and incision and '
                                'drainage, then recurred. CT shows fluid surrounding the implant without '
                                'osteomyelitis. Cultures grew coagulase-negative staphylococcus. What is the best '
                                'management?',
                        'choices': ['Remove the implant, debride and culture, and delay reconstruction',
                                    'Six weeks of IV antibiotics through a PICC with the implant left in',
                                    'Irrigate the pocket with antibiotic solution and close over a drain',
                                    'Exchange it for a new implant in the same pocket at one operation'],
                        'answer': 0,
                        'explanation': 'Recurrent infection around a permanent implant despite antibiotics and '
                                       'drainage indicates a biofilm infection. Bacteria such as coagulase-negative '
                                       "staphylococci adhere within the implant's surface and porous matrix, protected "
                                       'from antibiotics and host defenses, so infection relapses when antibiotics '
                                       'stop. Definitive source control requires removal of the implant with '
                                       'debridement of the capsule and sinus tract and cultures. Reconstruction is '
                                       'usually staged after the infection has fully resolved.',
                        'why_wrong': ['Correct.',
                                      'Prolonged antibiotics rarely clear biofilm on a porous implant, and relapse '
                                      'after stopping is expected.',
                                      'Irrigation does not remove biofilm within the porous implant, and closing the '
                                      'pocket over infected material invites recurrence.',
                                      'Placing a new implant into an infected pocket risks immediate recolonization; '
                                      'reconstruction should wait until infection resolves.'],
                        'board_pearl': 'Recurrent implant infection despite antibiotics suggests biofilm; remove the '
                                       'implant and reconstruct later.',
                        'curveball': 'After the implant is removed, she wants her chin contour restored as soon as '
                                     'possible. What factors would justify immediate rather than staged '
                                     'reconstruction?',
                        'curveball_answer': 'Immediate reconstruction may be reasonable when contamination is limited, '
                                            'all infected and devitalized tissue can be excised, the bed is well '
                                            'vascularized, and autologous tissue such as bone or a vascularized flap '
                                            'is used. Staged reconstruction is preferred with active purulence, '
                                            'osteomyelitis, irradiated tissue, or when another alloplast is planned, '
                                            'because these increase reinfection risk.'},
 'v139_gen_14': {'stem': 'A 74-year-old man on apixaban for atrial fibrillation had a right neck dissection yesterday, '
                         'and his apixaban was mistakenly restarted this morning. He now has rapidly enlarging right '
                         'neck swelling, a hoarse voice, and inspiratory stridor, with oxygen saturation of 89%. The '
                         'drain is clotted. Blood pressure is 158/90. What is the priority?',
                 'choices': ['Give 4-factor PCC and wait for an anti-Xa level before operating',
                             'CT angiography of the neck to localize the bleeding vessel first',
                             'Fresh frozen plasma and IV vitamin K, then reassess the neck swelling hourly',
                             'Open the wound to decompress, securing the airway with PCC in parallel'],
                 'answer': 3,
                 'explanation': 'An expanding neck hematoma with stridor and hypoxia is an airway emergency caused by '
                                'venous and lymphatic congestion of the larynx under pressure. Decompression by '
                                'opening the incision and deep layers at the bedside relieves the compression, while '
                                'the team calls anesthesia, prepares to secure the airway, and moves to the operating '
                                'room for definitive hemostasis. Reversal is given in parallel, not first: for '
                                'apixaban, 4-factor prothrombin complex concentrate is used now that andexanet alfa is '
                                'no longer marketed in the US.',
                 'why_wrong': ['Reversal takes time and does not decompress the airway; waiting for labs while stridor '
                               'worsens risks complete obstruction.',
                               'Transport to CT with stridor and hypoxia is dangerous, and imaging is unnecessary when '
                               'the source is clearly the operative bed.',
                               'Vitamin K and plasma do not reverse factor Xa inhibitors, and delaying decompression '
                               'for them risks losing the airway.',
                               'Correct.'],
                 'board_pearl': 'Expanding neck hematoma with airway compromise: decompress and secure the airway '
                                'first; give reversal in parallel.',
                 'curveball': 'How would management differ for minor anterior epistaxis in a high-stroke-risk patient '
                              'on apixaban?',
                 'curveball_answer': 'Minor bleeding is managed with local measures first: pressure, topical '
                                     'vasoconstrictor, cautery of a visible vessel, or absorbable packing. The '
                                     'anticoagulant is usually continued, or at most briefly held after discussion '
                                     'with the prescriber, because stopping it in a patient at high stroke risk '
                                     'exposes them to thromboembolism. Reversal is reserved for life-threatening or '
                                     'uncontrolled bleeding.'},
 'v140_gen_10': {'stem': 'A 56-year-old woman with a mechanical mitral valve had total thyroidectomy 4 hours ago and '
                         'received her first postoperative dose of therapeutic enoxaparin. She now reports neck '
                         'pressure and difficulty swallowing. The neck is tense and swelling is visibly expanding '
                         'above the incision, she has early inspiratory stridor, and oxygen saturation is 93% on 4 '
                         'L/min. What should happen first?',
                 'choices': ['Bedside ultrasound to confirm a hematoma before intervention',
                             'Protamine and coagulation studies before anyone touches the wound',
                             'Open the skin and strap layers at the bedside to evacuate clot',
                             'Rapid-sequence intubation on the ward before any decompression'],
                 'answer': 2,
                 'explanation': 'A compressive hematoma after thyroidectomy causes airway obstruction mainly through '
                                'venous congestion and laryngeal edema, not simply tracheal compression. When stridor '
                                'and expanding swelling appear, the incision, including the platysma and the strap '
                                'muscle closure, must be opened at the bedside to evacuate clot, while help is called '
                                'and the patient is prepared for return to the operating room. Decompression often '
                                'improves the airway enough for safer intubation. Imaging and reversal must not delay '
                                'it.',
                 'why_wrong': ['The diagnosis is clinical; ultrasound wastes time while the airway worsens and does '
                               'not treat the compression.',
                               'Partial protamine reversal can be given in parallel, but waiting for it or for labs '
                               'delays the decompression the airway needs now.',
                               'Correct.',
                               'Laryngoscopy through an edematous, compressed airway is likely to fail; decompression '
                               'first improves the chance of safe intubation.'],
                 'board_pearl': 'Post-thyroidectomy hematoma with stridor: open the skin and strap layers at the '
                                'bedside immediately, then go to the OR.',
                 'curveball': 'What specific bedside wound-opening sequence should the on-call resident know?',
                 'curveball_answer': 'Call for help and give oxygen. Remove skin staples or sutures, open the '
                                     'subcuticular layer, then spread the strap muscle closure in the midline with a '
                                     'clamp or fingers to release deep clot, which is where compression arises. '
                                     'Evacuate clot gently, apply moist gauze, and sit the patient up. Then secure the '
                                     'airway with anesthesia and return to the OR for hemostasis and closure.'},
 'v270_gen_hemo_fnd': {'stem': 'A 68-year-old man takes apixaban 5 mg twice daily for nonvalvular atrial fibrillation '
                               'with a CHA2DS2-VASc score of 2 and no prior stroke. Creatinine clearance is 75 mL/min. '
                               'He is scheduled for elective superficial parotidectomy, where a hematoma could '
                               'threaten the facial nerve and wound. His cardiologist asks for the perioperative plan. '
                               'Which approach is most appropriate?',
                       'choices': ['Continue apixaban through surgery because it has a short half-life',
                                   'Stop 2 days before surgery without bridging; resume after hemostasis',
                                   'Hold for 5 days and bridge with therapeutic enoxaparin until surgery',
                                   'Hold apixaban and check INR the morning of surgery to confirm clearance'],
                       'answer': 1,
                       'explanation': 'Perioperative antithrombotic decisions balance the bleeding consequences of the '
                                      'procedure against the thrombotic risk of the indication. Parotidectomy carries '
                                      'meaningful bleeding risk, while atrial fibrillation with a score of 2 carries '
                                      'low short-term stroke risk. For apixaban with normal renal function, the PAUSE '
                                      'study supports stopping 2 days before a high-bleeding-risk procedure without '
                                      'heparin bridging and resuming 48 to 72 hours after surgery once hemostasis is '
                                      'secure. Clearance depends on drug and renal function.',
                       'why_wrong': ['Continuing a therapeutic anticoagulant through parotidectomy raises hematoma '
                                     'risk in a patient whose stroke risk does not justify it.',
                                     'Correct.',
                                     'Bridging DOACs is unnecessary because they wear off and restart predictably; '
                                     'heparin bridging increases bleeding without reducing stroke.',
                                     'INR does not measure apixaban effect reliably; timing based on drug half-life '
                                     'and renal function is used instead.'],
                       'board_pearl': 'DOAC interruption: timing follows drug, renal function, and procedural bleeding '
                                      'risk; bridging is not needed.',
                       'curveball': 'Why is a coronary stent placed 6 weeks ago a different conversation from a remote '
                                    'provoked DVT?',
                       'curveball_answer': 'A recent drug-eluting stent carries a high risk of stent thrombosis, often '
                                           'fatal myocardial infarction, if dual antiplatelet therapy is stopped, so '
                                           'elective surgery is usually delayed until at least 6 months, and aspirin '
                                           'is continued when possible. A remote provoked DVT treated for 3 months '
                                           'carries low recurrence risk, so anticoagulation is usually complete or can '
                                           'be interrupted safely.'},
 'v270_gen_hemo_snr': {'stem': 'A 69-year-old woman on rivaroxaban for recurrent pulmonary emboli resumed her '
                               'medication on day 1 after hemithyroidectomy. On day 2 she develops tense, expanding '
                               'neck swelling, voice change, and inspiratory stridor. The junior resident has paged '
                               'anesthesia and proposes giving 4-factor PCC and waiting 30 minutes for it to take '
                               'effect before opening the wound. What is the best response?',
                       'choices': ['Decompress now and plan the OR, with PCC and blood products in parallel',
                                   'Agree, since opening the wound before reversal risks uncontrollable bleeding',
                                   'Give tranexamic acid alone and reassess the swelling in 30 minutes',
                                   'Obtain CT angiography first to locate the bleeding vessel before acting'],
                       'answer': 0,
                       'explanation': 'Life-threatening neck hemorrhage requires simultaneous physiologic support and '
                                      'source control. Reversal improves clotting but does not mechanically decompress '
                                      'the airway or ligate the bleeding vessel, so it runs in parallel rather than '
                                      'first. The senior plan is immediate bedside decompression, airway management '
                                      'with anesthesia, transfer to the operating room for surgical hemostasis, '
                                      '4-factor PCC for the factor Xa inhibitor, labs, and blood products as needed. '
                                      'Her thrombotic indication will later shape when anticoagulation resumes.',
                       'why_wrong': ['Correct.',
                                     'Waiting 30 minutes with stridor risks complete obstruction; bleeding is '
                                     'controlled surgically once the wound is opened.',
                                     'Tranexamic acid is a reasonable adjunct but neither reverses rivaroxaban nor '
                                     'decompresses the airway.',
                                     'Transport to CT with stridor is dangerous, and the bleeding source is the '
                                     'operative bed, which surgery will expose directly.'],
                       'board_pearl': 'Reversal supports hemostasis but does not decompress the airway; run '
                                      'decompression, OR, and reversal in parallel.',
                       'curveball': 'How would stable, low-volume oozing in a patient with very high thrombotic risk '
                                    'change the threshold to reverse anticoagulation?',
                       'curveball_answer': 'If bleeding is modest, controllable with local measures, and not '
                                           'threatening the airway, reversal is usually avoided because it exposes a '
                                           'patient with recurrent emboli to a high risk of new thrombosis. Local '
                                           'hemostasis, pressure, and close observation come first, with temporary '
                                           'holding of a dose if needed after discussing with hematology, and earlier '
                                           'restart planned once hemostasis is secure.'},
 'v139_gen_15': {'stem': 'A 54-year-old man with acute myeloid leukemia on induction chemotherapy has an absolute '
                         'neutrophil count of 100 cells per microliter. He has 2 days of fever, severe right facial '
                         'pain, and now diplopia with limited abduction of the right eye. Nasal endoscopy shows black, '
                         'insensate necrotic mucosa on the right middle turbinate and septum. What is the most '
                         'appropriate management?',
                 'choices': ['Voriconazole alone, with endoscopy repeated after neutrophil recovery',
                             'Broad antibacterials and saline irrigation, reassessing in 48 hours',
                             'MRI of the orbits and sinuses, then biopsy at an outpatient visit',
                             'Urgent biopsy and debridement with liposomal amphotericin B'],
                 'answer': 3,
                 'explanation': 'Neutropenia, facial pain, black necrotic insensate mucosa, and a new cranial '
                                'neuropathy indicate acute invasive fungal rhinosinusitis with orbital or cavernous '
                                'sinus extension. It progresses over hours through angioinvasion. Management is urgent '
                                'tissue diagnosis with frozen section, aggressive surgical debridement to bleeding '
                                'tissue, immediate empiric liposomal amphotericin B, which covers both Mucorales and '
                                'Aspergillus, and reversal of immunosuppression where possible, such as granulocyte '
                                'colony-stimulating factor. Imaging can be obtained urgently but must not delay '
                                'surgery.',
                 'why_wrong': ['Voriconazole does not cover Mucorales, and waiting for count recovery allows rapid '
                               'angioinvasive progression into the orbit and brain.',
                               'Antibacterial therapy does not treat invasive fungal disease, and 48 hours of delay '
                               'can be fatal with orbital involvement.',
                               'MRI helps define extent, but this is an emergency, and outpatient biopsy would delay '
                               'diagnosis and debridement by days.',
                               'Correct.'],
                 'board_pearl': 'Neutropenia plus necrotic nasal mucosa: urgent biopsy, debridement, liposomal '
                                'amphotericin, and immune reconstitution.',
                 'curveball': 'The fellow asks what other ENT infections behave atypically in profoundly '
                              'immunosuppressed patients like this one. What should you tell them?',
                 'curveball_answer': 'Necrotizing otitis externa can occur in neutropenic and transplant patients '
                                     'without diabetes, and may be fungal. Herpes simplex and cytomegalovirus cause '
                                     'deep, chronic oral or laryngeal ulcers. Bacterial deep neck infections may lack '
                                     'fluctuance or leukocytosis. Mycobacterial, Nocardia, and endemic fungal '
                                     'infections cause nodal or mucosal disease, and post-transplant '
                                     'lymphoproliferative disorder can mimic infection.'},
 'v147_gen_08': {'stem': 'A 41-year-old woman is 10 days after allogeneic stem cell transplant and remains '
                         'neutropenic. She has a fever of 38.9 C and severe left cheek pain for 1 day. Sinus CT shows '
                         'only mild unilateral mucosal thickening of the left maxillary sinus. Nasal endoscopy shows a '
                         'dusky, mildly crusted area on the left middle turbinate without black eschar, and sensation '
                         'there is reduced. What is the safest approach?',
                 'choices': ['Repeat endoscopy in 48 hours to see whether black eschar develops',
                             'Biopsy the dusky mucosa now for frozen section and start antifungals',
                             'Amoxicillin-clavulanate for presumed acute bacterial sinusitis',
                             'MRI first, with biopsy only if bone erosion or orbital spread is shown'],
                 'answer': 1,
                 'explanation': 'In neutropenic patients, inflammatory signs are muted, and black eschar is a late '
                                'finding. Severe focal facial pain, fever, and dusky, crusted, or insensate mucosa '
                                'should be treated as possible acute invasive fungal rhinosinusitis. CT findings are '
                                'often minimal early. Biopsy of abnormal mucosa for frozen section, showing hyphae '
                                'invading tissue or vessels, allows same-day debridement, with empiric antifungal '
                                'therapy begun when suspicion is high. Immunosuppression is reduced where feasible in '
                                'coordination with the transplant team.',
                 'why_wrong': ['Waiting for eschar allows angioinvasion to progress; eschar is a late sign, and early '
                               'biopsy is what changes outcome.',
                               'Correct.',
                               'Bacterial sinusitis is possible, but antibacterials alone delay diagnosis of a rapidly '
                               'fatal fungal infection in a neutropenic host.',
                               'Bone erosion is late and often absent early, so waiting for it delays diagnosis; MRI '
                               'can be done urgently alongside biopsy.'],
                 'board_pearl': 'Do not wait for black eschar; neutropenic facial pain with dusky or insensate mucosa '
                                'needs biopsy now.',
                 'curveball': 'What frozen-section finding establishes tissue invasion and how does it change '
                              'management?',
                 'curveball_answer': 'Fungal hyphae within submucosal tissue, especially invading blood vessel walls '
                                     'with thrombosis and necrosis, establishes invasive disease, while hyphae '
                                     'confined to surface debris do not. Broad, pauci-septate, ribbon-like hyphae '
                                     'suggest Mucorales, and narrow septate hyphae with acute-angle branching suggest '
                                     'Aspergillus. Positive frozen section prompts immediate debridement to bleeding '
                                     'tissue and continued amphotericin.'},
 'v272_gen_immuno_fnd': {'stem': 'A 62-year-old man receiving chemotherapy for diffuse large B-cell lymphoma has an '
                                 'absolute neutrophil count of 200 cells per microliter. He has fever and severe right '
                                 'facial pain. CT shows only mild right ethmoid mucosal thickening. On nasal '
                                 'endoscopy, the right middle turbinate is pale, does not bleed when touched, and is '
                                 'insensate to probing, while the left side is normal. How should this finding be '
                                 'interpreted?',
                         'choices': ['Normal mucosal blanching after topical decongestant spray',
                                     'A sign of allergic fungal sinusitis warranting systemic steroids',
                                     'An early sign of invasive fungal disease needing urgent biopsy',
                                     'A nonspecific change, so endoscopy should be repeated in 2 days'],
                         'answer': 2,
                         'explanation': 'Pale, insensate, nonbleeding mucosa reflects ischemia from fungal '
                                        'angioinvasion and thrombosis, and it often precedes black necrosis. In a '
                                        'neutropenic patient with fever and focal facial pain, this finding should be '
                                        'treated as acute invasive fungal rhinosinusitis until excluded by urgent '
                                        'biopsy with frozen section. CT is often unremarkable early. Prompt tissue '
                                        'diagnosis allows debridement and antifungal therapy before orbital or '
                                        'intracranial spread, so ENT evaluation should be immediate and coordinated '
                                        'with oncology and infectious disease.',
                         'why_wrong': ['Decongestant blanching affects both sides and preserves sensation and '
                                       'bleeding; unilateral insensate mucosa signals ischemia.',
                                       'Allergic fungal sinusitis occurs in immunocompetent atopic patients, and '
                                       'steroids would worsen invasive infection in this host.',
                                       'Correct.',
                                       'Waiting allows angioinvasion to progress; mucosal ischemia in this setting '
                                       'demands same-day tissue diagnosis.'],
                         'board_pearl': 'Pale, insensate, nonbleeding nasal mucosa in a neutropenic patient may be the '
                                        'earliest sign of invasive fungal sinusitis.',
                         'curveball': 'Which bedside cranial nerve and orbital findings should be documented before '
                                      'the patient leaves for imaging or the OR?',
                         'curveball_answer': 'Document visual acuity, pupillary responses including an afferent '
                                             'defect, color vision if possible, extraocular movements, proptosis, and '
                                             'chemosis, plus facial sensation in V1 and V2, palate sensation and '
                                             'color, and facial nerve function. These establish a baseline for '
                                             'detecting orbital apex or cavernous sinus progression and guide the '
                                             'extent of debridement and need for orbital surgery.'},
 'v272_gen_immuno_app': {'stem': 'A 47-year-old man with a kidney transplant on tacrolimus, mycophenolate, and '
                                 'prednisone has 3 days of fever, odynophagia, and neck pain. Temperature is 39.1 C, '
                                 'blood pressure 96/58, and lactate 3.2 mmol/L. He speaks clearly without stridor. CT '
                                 'shows retropharyngeal edema and phlegmon without a rim-enhancing collection. What is '
                                 'the best approach?',
                         'choices': ['Discharge on oral amoxicillin-clavulanate because there is no abscess',
                                     'Immediate transcervical exploration and drainage of the phlegmon',
                                     'Hold antibiotics until tissue cultures are taken in the operating room',
                                     'Admit for cultures, broad IV antibiotics, and serial airway checks'],
                         'answer': 3,
                         'explanation': 'Transplant immunosuppression changes both the tempo and the microbiology of '
                                        'infection. Absence of a mature abscess does not offset sepsis with '
                                        'hypotension and elevated lactate. He needs admission to a monitored setting, '
                                        'blood cultures, prompt broad empiric IV antibiotics chosen with his immune '
                                        'defect and resistance patterns in mind, serial airway examinations, and early '
                                        'repeat imaging if he fails to improve. Immunosuppression adjustments, '
                                        'including stress-dose steroids, are coordinated with the transplant team.',
                         'why_wrong': ['Sepsis in an immunosuppressed host is not outpatient disease, even without an '
                                       'abscess on the first scan.',
                                       'Phlegmon without a drainable collection usually responds to antibiotics; '
                                       'surgery is reserved for a collection or clinical failure.',
                                       'Delaying antibiotics in sepsis increases mortality; cultures should be drawn '
                                       'quickly but must not postpone treatment.',
                                       'Correct.'],
                         'board_pearl': 'Immunocompromised host with sepsis and phlegmon: admit, culture, treat '
                                        'broadly, and reassess early, even without an abscess.',
                         'curveball': 'How should recent neutropenia, transplant immunosuppression, HIV status, or '
                                      'chronic steroids change your pathogen differential?',
                         'curveball_answer': 'Neutropenia raises concern for Pseudomonas, gram-negative rods, and '
                                             'invasive molds. Transplant immunosuppression adds resistant bacteria, '
                                             'Nocardia, cytomegalovirus, herpes viruses, and post-transplant '
                                             'lymphoproliferative disorder. Advanced HIV with low CD4 adds '
                                             'mycobacteria, endemic fungi, and Kaposi sarcoma. Chronic steroids blunt '
                                             'fever and inflammation and increase fungal and staphylococcal risk.'},
 'v272_gen_immuno_snr': {'stem': 'A 50-year-old man who had an allogeneic stem cell transplant 8 months ago is on '
                                 'prednisone for graft-versus-host disease. Five days ago a left submandibular abscess '
                                 'was drained, but bacterial cultures showed no growth. Despite vancomycin and '
                                 'piperacillin-tazobactam, fever persists and the swelling is enlarging. Repeat '
                                 'examination shows firm, indurated tissue extending into the floor of mouth. What is '
                                 'the best next step?',
                         'choices': ['Add micafungin and ganciclovir empirically without any further sampling',
                                     'Repeat imaging and obtain tissue for fungal, AFB, and pathology study',
                                     'Continue the current regimen, since a slow response is expected',
                                     'Stop all immunosuppression immediately to restore host defenses'],
                         'answer': 1,
                         'explanation': 'Failure of broad therapy after drainage with sterile bacterial cultures '
                                        'should prompt re-phenotyping of the problem rather than adding drugs. '
                                        'Possibilities include a residual or new collection, invasive fungal '
                                        'infection, mycobacteria, Nocardia, viral ulceration, post-transplant '
                                        'lymphoproliferative disorder or other malignancy, and drug fever. Repeat '
                                        'contrast imaging localizes disease, and tissue sent for bacterial, fungal, '
                                        'and mycobacterial culture, special stains, histopathology, and flow cytometry '
                                        'guides targeted therapy. Immune changes are made with the transplant team.',
                         'why_wrong': ['Empiric escalation without tissue may miss malignancy or mycobacteria, adds '
                                       'toxicity, and makes later cultures less informative.',
                                       'Correct.',
                                       'Progressive induration despite drainage and broad therapy is failure, not slow '
                                       'response, and waiting risks spread and airway compromise.',
                                       'Abruptly stopping immunosuppression can provoke severe graft-versus-host '
                                       'disease and must be coordinated with the transplant team.'],
                         'board_pearl': 'When infection in an immunocompromised host fails broad therapy, re-image and '
                                        'get tissue rather than add antimicrobials blindly.',
                         'curveball': 'When should reduction of immunosuppression be discussed, and which service must '
                                      'be involved before changing it?',
                         'curveball_answer': 'Reduction is discussed for invasive fungal infection, uncontrolled or '
                                             'opportunistic infection, and post-transplant lymphoproliferative '
                                             'disorder, where restoring immune function is part of therapy. Changes '
                                             'must be made by or with the transplant team, hematology for stem cell '
                                             'recipients or the organ transplant service, because of the risk of '
                                             'rejection or graft-versus-host disease.'},
 'v139_gen_16': {'stem': 'A 46-year-old woman is undergoing CO2 laser excision of a vocal fold lesion during '
                         'suspension microlaryngoscopy with a laser-resistant endotracheal tube. She is healthy, with '
                         'oxygen saturation of 99% on 50% oxygen in air at the start of the case. The anesthesiologist '
                         'asks what gas settings the surgeon prefers before the laser is activated. Which practice '
                         'most reduces airway fire risk?',
                 'choices': ['Switch to 50% nitrous oxide in oxygen to lower the oxygen percentage',
                             'Keep 50% oxygen because the laser-resistant tube prevents ignition',
                             'Lower oxygen to 30% or less in air and avoid nitrous oxide',
                             'Increase oxygen to 100% so that apnea is tolerated if needed'],
                 'answer': 2,
                 'explanation': 'Airway fire requires an oxidizer, a fuel, and an ignition source, and laser cases '
                                'should control all three. The oxidizer is reduced by lowering inspired oxygen to the '
                                'minimum that maintains saturation, generally 30% or less, delivered with air or '
                                'helium rather than nitrous oxide, which also supports combustion. A laser-resistant '
                                'tube with a saline-filled cuff reduces fuel but is not fireproof, and the cuff and '
                                'shaft can still ignite. The surgeon announces activation so anesthesia can confirm '
                                'the oxygen level.',
                 'why_wrong': ['Nitrous oxide is an oxidizer that supports combustion as well as oxygen does, so it '
                               'does not reduce fire risk.',
                               'Laser-resistant tubes reduce but do not eliminate ignition risk, especially at the '
                               'cuff, so oxygen still needs to be minimized.',
                               'Correct.',
                               'High oxygen concentration dramatically increases flammability and is the opposite of '
                               'fire prevention.'],
                 'board_pearl': 'Airway laser fire prevention: oxygen at 30% or lower, no nitrous oxide, laser-safe '
                                'tube with saline cuff, and announced activation.',
                 'curveball': 'Despite these precautions, a flame appears at the cuff of the endotracheal tube. What '
                              'are the immediate steps?',
                 'curveball_answer': 'Remove the tube immediately and stop all airway gas flow at the same time, then '
                                     'remove any burning pledgets and pour saline into the airway. Once the fire is '
                                     'out, ventilate by mask with air rather than oxygen if possible, then reintubate '
                                     'and perform bronchoscopy to assess thermal injury and retrieve debris, with '
                                     'observation for airway edema.'},
 'v147_gen_09': {'stem': 'A 61-year-old man is undergoing transoral CO2 laser resection of a supraglottic carcinoma '
                         'through a laser-resistant tube. Inspired oxygen is 28% in air. As the surgeon works near the '
                         'posterior commissure, the cuff of the tube lies just below the glottis within the laser '
                         'path. Which additional step most directly reduces the risk of airway fire?',
                 'choices': ['Fill the cuff with saline and place moist cottonoids over it',
                             'Fill the cuff with air so a puncture can be detected by leak',
                             'Place dry cottonoids over the cuff to shield it from the beam',
                             'Wrap the cuff and the distal tube in reflective aluminum tape'],
                 'answer': 0,
                 'explanation': 'Fire prevention controls oxidizer, ignition, and fuel. With oxygen already low, the '
                                'remaining risk is the cuff, which is the most vulnerable part of a laser-resistant '
                                'tube. Filling it with saline, often tinted with methylene blue, absorbs heat and '
                                'signals puncture by blue fluid and loss of seal, and moist cottonoids placed above '
                                'the cuff shield it from the beam and act as a heat sink. Cottonoids must be kept wet '
                                'and counted, because dry ones are themselves fuel.',
                 'why_wrong': ['Correct.',
                               'An air-filled cuff can ignite or rupture and release oxygen-rich gas, while saline '
                               'would absorb heat and reveal puncture.',
                               'Dry cottonoids are flammable fuel in the laser path; only saline-soaked pledgets '
                               'protect the cuff.',
                               'Metal foil wrapping of standard tubes is an outdated technique that can reflect the '
                               'beam, and tape cannot cover an inflated cuff.'],
                 'board_pearl': 'Protect the laser tube cuff with saline, often with methylene blue, and keep '
                                'cottonoids wet; dry pledgets are fuel.',
                 'curveball': 'Despite these steps, a cuff puncture is seen with blue fluid in the field and a leak. '
                              'What should happen next?',
                 'curveball_answer': 'Stop the laser and inform anesthesia. The tube no longer has a protected, sealed '
                                     'cuff, so oxygen-rich gas may leak into the field. Most teams pack the larynx '
                                     'with wet cottonoids to control the leak or exchange the tube before continuing. '
                                     'Ensure oxygen stays at the minimum, inspect the tube for damage, and resume only '
                                     'once a sealed, protected airway is restored.'},
 'v274_gen_laser_fnd': {'stem': 'A 57-year-old man with COPD is undergoing CO2 laser excision of a laryngeal lesion '
                                'through a laser-resistant tube at 30% oxygen. His saturation falls to 89%, and the '
                                'anesthesiologist increases oxygen to 100% for 2 minutes until saturation recovers to '
                                '97%. The surgeon is ready to resume lasing near the tube. Which action most directly '
                                'reduces fire risk?',
                        'choices': ['Resume immediately at a lower power setting with shorter pulse duration',
                                    'Pause until oxygen is back to 30% or less and anesthesia confirms',
                                    'Add nitrous oxide to the gas mix to keep saturation stable',
                                    'Resume lasing, since a laser-resistant tube removes fire risk'],
                        'answer': 1,
                        'explanation': 'Fire risk depends on the oxidizer concentration at the moment of activation, '
                                       'so after a period of high oxygen the airway and pharynx remain oxygen-enriched '
                                       'for some time. The surgeon should pause, anesthesia should reduce oxygen to '
                                       'the lowest level that maintains saturation, generally 30% or less, and wait '
                                       'for the airway to wash out, and the team should confirm verbally before the '
                                       'laser fires. This explicit communication about oxidizer, ignition, and fuel is '
                                       'central to airway laser safety.',
                        'why_wrong': ['Lower power reduces but does not eliminate ignition risk, and firing in an '
                                      'oxygen-enriched airway remains dangerous.',
                                      'Correct.',
                                      'Nitrous oxide supports combustion and is itself an oxidizer, so it increases '
                                      'rather than reduces fire risk.',
                                      'Laser-resistant tubes are not fireproof, particularly the cuff, and high oxygen '
                                      'makes ignition far more likely.'],
                        'board_pearl': 'Before each laser activation, confirm with anesthesia that oxygen is at the '
                                       'lowest safe level, generally 30% or less.',
                        'curveball': 'If he cannot maintain saturation at 30% oxygen, which airway strategies could '
                                     'reduce oxidizer and tube exposure?',
                        'curveball_answer': 'Options include intermittent apneic technique, where the tube is removed '
                                            'or ventilation paused while lasing in short windows, subglottic or '
                                            'supraglottic jet ventilation with air to avoid a combustible tube, or '
                                            'switching to cold instruments or a microdebrider near the tube. Each has '
                                            'trade-offs, such as barotrauma with jet ventilation, and the plan should '
                                            'be agreed with anesthesia beforehand.'},
 'v274_gen_laser_app': {'stem': 'A 39-year-old woman is undergoing CO2 laser microlaryngoscopy for a vocal fold lesion '
                                'through a laser-resistant endotracheal tube. Midway through the case, a flash appears '
                                'and flame is seen at the tube cuff below the glottis. Oxygen is flowing at 30% in '
                                'air. The anesthesiologist asks what to do. What should happen first?',
                        'choices': ['Stop the laser and keep ventilating through the tube to maintain oxygenation',
                                    'Deflate the cuff and partially withdraw the tube above the vocal folds',
                                    'Remove the tube and stop gas flow at once, then pour saline into the airway',
                                    'Leave the tube in place and flood it with saline to cool the burning cuff'],
                        'answer': 2,
                        'explanation': 'An airway fire is managed by removing all three elements at once. The tube, '
                                       'which is the burning fuel, is removed immediately while all airway gas flow is '
                                       'stopped to cut off the oxidizer. Any burning pledgets are removed, and saline '
                                       'is poured into the airway to extinguish residual embers. Ventilation is then '
                                       'resumed by mask, preferably with air, and the airway is re-established. '
                                       'Bronchoscopy follows to assess thermal injury and retrieve debris before '
                                       'reintubation and observation.',
                        'why_wrong': ['Continued ventilation through a burning tube forces flame and hot gas into the '
                                      'lower airway, causing a blowtorch injury.',
                                      'Partial withdrawal leaves burning material in the airway and delays the most '
                                      'important step of removing the fuel.',
                                      'Correct.',
                                      'Leaving the tube in place keeps the fuel in the airway; saline helps only after '
                                      'the burning tube is removed.'],
                        'board_pearl': 'Airway fire: remove the tube and stop gases simultaneously, pour saline, then '
                                       'mask ventilate and bronchoscope.',
                        'curveball': 'When would bronchoscopy and ICU observation be indicated after apparently rapid '
                                     'extinguishment?',
                        'curveball_answer': 'Essentially always. After any airway fire, bronchoscopy should assess the '
                                            'trachea and bronchi for thermal injury and retained tube or cottonoid '
                                            'fragments, even when the fire seemed brief. Observation, often in the '
                                            'ICU, is warranted for airway edema, inhalation injury, and pneumonitis. '
                                            'Significant mucosal burns may need reintubation, steroids, and serial '
                                            'bronchoscopy.'},
 'v274_gen_laser_snr': {'stem': 'A 70-year-old man with severe COPD needs excision of a small exophytic lesion at the '
                                'anterior vocal fold. In the operating room he cannot maintain oxygen saturation above '
                                '90% unless inspired oxygen is at least 60%. The only available laser-resistant tube '
                                'is too large for his narrow glottis, so a standard PVC tube is in place, its cuff '
                                'close to the lesion. What is the best decision?',
                        'choices': ['Proceed with the CO2 laser at low power in short bursts',
                                    'Lower oxygen to room air for laser use despite desaturation',
                                    'Cover the PVC tube with dry gauze sponges and proceed with the laser',
                                    'Abandon the laser and use cold microinstruments for this lesion'],
                        'answer': 3,
                        'explanation': 'Senior judgment includes refusing an unsafe fire triangle. With a combustible '
                                       'PVC tube near the target and an oxygen requirement of 60%, any laser '
                                       'activation carries a high risk of airway fire. When oxidizer and fuel cannot '
                                       'be controlled, the energy plan must change. Cold steel microlaryngeal '
                                       'instruments remove a small lesion precisely without ignition risk. '
                                       'Alternatively, the case can be staged once a suitable laser-safe tube or a '
                                       'different ventilation strategy is available.',
                        'why_wrong': ['Low power and short pulses reduce but do not prevent ignition of a PVC tube in '
                                      '60% oxygen.',
                                      'Accepting severe hypoxemia for a laser is unsafe in a patient with COPD when a '
                                      'nonlaser technique is available.',
                                      'Dry gauze is additional fuel, not protection, and adds to the fire risk in the '
                                      'laser field.',
                                      'Correct.'],
                        'board_pearl': 'If oxygen cannot be lowered and the tube cannot be protected, change the '
                                       'energy plan or abort laser use.',
                        'curveball': 'Which airway strategies can reduce oxidizer and tube exposure in selected laser '
                                     'cases?',
                        'curveball_answer': 'Options include an appropriately sized laser-resistant tube with '
                                            'saline-filled cuff, tubeless techniques using intermittent apnea or '
                                            'spontaneous ventilation, and subglottic or supraglottic jet ventilation '
                                            'with air or low oxygen. High-flow nasal oxygen has been used for brief '
                                            'apneic cases but adds oxidizer, so it is generally avoided during '
                                            'lasing.'},
 'v139_gen_17': {'stem': 'A 28-year-old man of Turkish descent has had painful oral ulcers more than five times a year '
                         'for 3 years, each healing within 2 weeks. He has also had painful scrotal ulcers that left '
                         'scars, and was treated last month for anterior uveitis. A sterile pustule formed 48 hours '
                         'after a blood draw. Exam shows three round ulcers with yellow bases and red halos on the '
                         'buccal mucosa. Which diagnosis is most likely?',
                 'choices': ['Behcet disease',
                             'Recurrent herpes simplex infection',
                             'Reactive arthritis',
                             'Crohn disease with oral involvement'],
                 'answer': 0,
                 'explanation': 'Behcet disease is a variable-vessel vasculitis most common along the historic Silk '
                                'Road. Recurrent oral aphthous ulcers, at least three episodes a year, are present in '
                                'nearly all patients and are often the first sign. Scarring genital ulcers, anterior '
                                'or posterior uveitis, skin lesions, and a positive pathergy test complete the '
                                'diagnostic picture. Recognizing the pattern matters because eye, vascular, and '
                                'neurologic involvement can cause blindness or death, so ophthalmology and '
                                'rheumatology care is needed.',
                 'why_wrong': ['Correct.',
                               'Herpes simplex causes clustered vesicles that ulcerate, usually on keratinized mucosa '
                               'or lips, and does not cause uveitis or pathergy.',
                               'Reactive arthritis causes conjunctivitis, urethritis, arthritis, and painless oral '
                               'lesions, not painful scarring genital ulcers with pathergy.',
                               'Crohn disease can cause oral ulcers and uveitis, but scarring genital ulcers and '
                               'positive pathergy point to Behcet disease.'],
                 'board_pearl': 'Recurrent oral aphthae plus genital ulcers, uveitis, or pathergy suggest Behcet '
                                'disease; refer for eye and systemic care.',
                 'curveball': 'His blood count is pending. What oral findings would instead have suggested a '
                              'hematologic malignancy or severe neutropenia?',
                 'curveball_answer': 'Gingival enlargement with bleeding, especially boggy purple hypertrophy, '
                                     'suggests acute myeloid leukemia, particularly monocytic subtypes. Spontaneous '
                                     'gingival bleeding, petechiae, and mucosal pallor suggest thrombocytopenia or '
                                     'anemia. Neutropenia causes deep, painful ulcers with little surrounding '
                                     'inflammation and necrotizing gingivitis. These findings warrant an urgent '
                                     'complete blood count with differential.'},
 'v147_gen_10': {'stem': 'A 34-year-old woman has recurrent painful oral ulcers that her dentist has treated as simple '
                         'canker sores for 2 years. She now reports vulvar ulcers, tender red nodules on her shins, '
                         'and blurred vision in the left eye. Exam shows several shallow, round, painful ulcers on the '
                         'tongue and labial mucosa. Ophthalmology finds retinal vasculitis. Which diagnosis best '
                         'unifies these findings?',
                 'choices': ['Simple recurrent aphthous stomatitis',
                             'Behcet disease',
                             'Mucous membrane pemphigoid',
                             'Erythema multiforme major'],
                 'answer': 1,
                 'explanation': 'Recurrent oral aphthae occur in many healthy people, but when combined with genital '
                                'ulcers, erythema nodosum-like skin lesions, and ocular inflammation, they suggest '
                                'Behcet disease. Retinal vasculitis is a sight-threatening manifestation that requires '
                                'urgent systemic immunosuppression, often with azathioprine or anti-TNF therapy. Oral '
                                'findings can be the presenting sign of systemic disease, so multisystem clues should '
                                'prompt coordinated evaluation rather than repeated local treatment of each ulcer.',
                 'why_wrong': ['Simple aphthous stomatitis is confined to the mouth and does not explain genital '
                               'ulcers, skin nodules, or retinal vasculitis.',
                               'Correct.',
                               'Mucous membrane pemphigoid causes desquamative gingivitis and scarring conjunctivitis, '
                               'not retinal vasculitis or erythema nodosum.',
                               'Erythema multiforme causes acute targetoid skin lesions and hemorrhagic lip crusting, '
                               'typically after herpes infection, not recurring aphthae.'],
                 'board_pearl': 'Oral aphthae with genital, skin, and eye findings is systemic until proven otherwise; '
                                'think Behcet disease.',
                 'curveball': 'Her ulcers recur every 3 weeks with fevers. What oral findings suggest neutropenia or '
                              'another hematologic disorder instead?',
                 'curveball_answer': 'Neutropenic ulcers are deep, painful, and lack an inflammatory halo, sometimes '
                                     'with necrotizing gingivitis, and cyclic neutropenia causes ulcers that recur '
                                     'about every 3 weeks with fevers. Leukemic gingival enlargement and bleeding, '
                                     'petechiae from thrombocytopenia, and pallor from anemia also point toward blood '
                                     'disorders. A complete blood count with differential, repeated during episodes if '
                                     'cyclic, is the first test.'},
 'v274_gen_oral_fnd': {'stem': 'A 66-year-old woman has 4 months of a burning, sore tongue, fatigue, and tingling in '
                               'both feet. She had a partial gastrectomy 10 years ago. Exam shows a smooth, beefy-red '
                               'tongue with loss of filiform papillae and cracks at the corners of the mouth. '
                               'Hemoglobin is 10.1 g/dL with mean corpuscular volume of 112 fL. Which diagnosis best '
                               'explains her oral findings?',
                       'choices': ['Vitamin B12 deficiency',
                                   'Oral lichen planus',
                                   'Benign migratory glossitis',
                                   'Erythematous candidiasis'],
                       'answer': 0,
                       'explanation': 'A smooth, red, painful tongue with loss of papillae is atrophic glossitis, a '
                                      'classic clue to deficiency of vitamin B12, folate, or iron. Her prior partial '
                                      'gastrectomy reduces intrinsic factor and B12 absorption, and macrocytic anemia '
                                      'with peripheral neuropathy points specifically to B12 deficiency. Angular '
                                      'cheilitis often accompanies it. Oral findings are not specific on their own, so '
                                      'serum B12, methylmalonic acid, folate, and iron studies confirm the cause, and '
                                      'replacement improves the tongue and can halt neuropathy.',
                       'why_wrong': ['Correct.',
                                     'Lichen planus shows lacy white striae or erosions, often bilateral on the buccal '
                                     'mucosa, and does not cause macrocytic anemia or neuropathy.',
                                     'Geographic tongue shows migrating red patches with white borders that change '
                                     'location over days, not diffuse persistent atrophy.',
                                     'Erythematous candidiasis can cause a red tongue, but macrocytic anemia, '
                                     'neuropathy, and gastrectomy point to a nutritional cause.'],
                       'board_pearl': 'Atrophic glossitis is a classic clue to B12, folate, or iron deficiency; check '
                                      'blood counts and levels.',
                       'curveball': 'Which laboratory pattern would distinguish iron deficiency from B12 deficiency in '
                                    'a patient with glossitis?',
                       'curveball_answer': 'Iron deficiency produces microcytic anemia with low ferritin, low serum '
                                           'iron, and high total iron-binding capacity. B12 deficiency produces '
                                           'macrocytic anemia with hypersegmented neutrophils, low B12, and elevated '
                                           'methylmalonic acid and homocysteine. Folate deficiency is also macrocytic '
                                           'but has normal methylmalonic acid. Mixed deficiency can produce normal MCV '
                                           'with a wide red cell distribution width.'},
 'v274_gen_oral_app': {'stem': 'A 31-year-old man has had recurrent painful oral ulcers for 18 months that have not '
                               'responded to topical steroids. He now has a painful red left eye with blurred vision '
                               'for 3 days and two healing scrotal ulcers. Exam shows four shallow round ulcers with '
                               'erythematous halos on the soft palate and tongue. He is otherwise well, and HIV and '
                               'syphilis tests are negative. What is the best next step?',
                       'choices': ['Silver nitrate cautery of each ulcer and a stronger topical steroid',
                                   'Empiric oral fluconazole for presumed candidal ulceration',
                                   'Urgent ophthalmology and rheumatology evaluation for systemic disease',
                                   'Excisional biopsy of the largest ulcer under general anesthesia'],
                       'answer': 2,
                       'explanation': 'Recurrent oral ulcers combined with genital ulcers and a red, painful eye with '
                                      'blurred vision suggest Behcet disease with active uveitis, which can rapidly '
                                      'threaten vision. The priority is recognizing the systemic pattern and arranging '
                                      'same-day ophthalmology assessment and rheumatology evaluation for systemic '
                                      'immunosuppression, rather than treating each oral lesion in isolation. '
                                      'Infectious mimics such as HIV and syphilis have already been excluded, and '
                                      'biopsy is reserved for atypical or nonhealing lesions.',
                       'why_wrong': ['Local cautery treats symptoms of individual ulcers but ignores the '
                                     'sight-threatening eye disease that defines the urgency.',
                                     'Nothing suggests candidiasis, and antifungals would not treat a systemic '
                                     'vasculitis with ocular involvement.',
                                     'Correct.',
                                     'Biopsy is nonspecific in Behcet disease and is reserved for atypical lesions; it '
                                     'would delay treatment of the eye.'],
                       'board_pearl': 'Oral ulcers plus a red, painful eye with blurred vision needs urgent '
                                      'ophthalmology and systemic evaluation.',
                       'curveball': 'If he were a 64-year-old smoker with a single nonhealing ulcer, which ulcer '
                                    'features would instead demand an urgent malignancy workup?',
                       'curveball_answer': 'A solitary ulcer persisting more than 2 to 3 weeks without healing, '
                                           'especially with induration, rolled or raised margins, fixation, or an '
                                           'exophytic component, needs biopsy for squamous cell carcinoma. Risk rises '
                                           'with tobacco and alcohol use, older age, and lateral tongue or floor of '
                                           'mouth location. Associated neck nodes, otalgia, or numbness add urgency.'},
 'v274_gen_oral_snr': {'stem': 'A 58-year-old man with a kidney transplant on tacrolimus, mycophenolate, and '
                               'prednisone has a 3-week history of a painful ulcer on the hard palate. It has enlarged '
                               'despite topical clobetasol and now has a black necrotic base with exposed bone at its '
                               'center. He has mild left nasal congestion and low-grade fever. His glucose is 280 '
                               'mg/dL. What is the best approach?',
                       'choices': ['Continue topical clobetasol for 4 more weeks and recheck in clinic',
                                   'Empiric valacyclovir and review the ulcer again in 2 weeks',
                                   'Wide palatal resection with obturator before any tissue diagnosis',
                                   'Urgent biopsy with fungal stains and culture, plus CT and MRI'],
                       'answer': 3,
                       'explanation': 'A progressive necrotic palatal ulcer in an immunosuppressed, hyperglycemic '
                                      'patient may represent invasive fungal infection such as mucormycosis spreading '
                                      'from the sinuses, and malignancy, viral ulceration, and vasculitis are '
                                      'alternatives. Delay can be fatal. Urgent biopsy with frozen section, fungal '
                                      'stains, cultures, and histopathology establishes the diagnosis, while CT and '
                                      'MRI define bone, sinus, orbital, and skull base extent. Debridement follows '
                                      'once tissue and extent are defined, along with antifungal therapy and glucose '
                                      'control.',
                       'why_wrong': ['Topical steroids have already failed and can worsen infection; continuing them '
                                     'delays diagnosis of a possibly lethal process.',
                                     'Herpes viruses can cause chronic ulcers in transplant patients, but necrotic '
                                     'bone and hyperglycemia demand tissue diagnosis now.',
                                     'Major resection before diagnosis and extent are known risks both inadequate and '
                                     'unnecessary surgery.',
                                     'Correct.'],
                       'board_pearl': 'Necrotic oral or palatal ulcer in an immunosuppressed host needs urgent biopsy '
                                      'and imaging, not more topical therapy.',
                       'curveball': 'What endoscopic or imaging findings would suggest invasive fungal spread toward '
                                    'the orbit or skull base?',
                       'curveball_answer': 'Endoscopic pale or black insensate mucosa extending to the middle '
                                           'turbinate, septum, or nasopharynx suggests spread. On imaging, look for '
                                           'soft tissue infiltration of the premaxillary or retroantral fat, '
                                           'pterygopalatine fossa, or orbital apex, loss of mucosal enhancement, the '
                                           'black turbinate sign on MRI, cavernous sinus filling defects, and bony '
                                           'erosion, although bone may appear intact early.'},
 'v139_gen_18': {'stem': 'A 49-year-old woman is on postoperative day 1 after mandible reconstruction with a free '
                         'fibula flap. Her morphine PCA dose has been increased twice for severe pain in the donor '
                         'leg, and she is now drowsy with a respiratory rate of 10. The calf is tense, and passive '
                         'extension of the toes worsens her pain. Creatinine is normal. Which is the best next step?',
                 'choices': ['Increase the PCA dose and add a continuous basal morphine infusion',
                             'Give naloxone 2 mg IV and resume the PCA at the same settings',
                             'Hold opioids, assess compartment pressures, and add nonopioids',
                             'Add IV ketamine and continue the current opioid escalation'],
                 'answer': 2,
                 'explanation': 'Pain out of proportion that keeps escalating despite opioids is a warning that '
                                'something is wrong surgically. A tense calf with pain on passive stretch after fibula '
                                'harvest suggests compartment syndrome, which needs urgent compartment pressure '
                                'measurement and fasciotomy if confirmed. Meanwhile her drowsiness and slow breathing '
                                'show opioid toxicity, so further opioid is held and nonopioid analgesia such as '
                                'acetaminophen is added. Multimodal analgesia improves pain control while limiting '
                                'opioid adverse effects.',
                 'why_wrong': ['Adding a basal infusion increases respiratory depression risk in a drowsy patient and '
                               'ignores a possible compartment syndrome.',
                               'Full-dose naloxone causes abrupt severe pain and withdrawal; titrated small doses '
                               'suffice, and the cause of pain still needs evaluation.',
                               'Correct.',
                               'Ketamine is a useful adjunct, but continuing opioid escalation while drowsy is unsafe '
                               'and the leg needs urgent assessment.'],
                 'board_pearl': 'Escalating pain despite opioids may signal a surgical complication; examine the '
                                'patient before giving more opioid.',
                 'curveball': 'Which nonopioid analgesics require caution with bleeding risk, renal disease, or liver '
                              'disease?',
                 'curveball_answer': 'NSAIDs impair platelet function and renal perfusion, so they need caution with '
                                     'bleeding concern, kidney disease, heart failure, and peptic ulcer, although '
                                     'ibuprofen is considered safe after tonsillectomy. Acetaminophen is limited in '
                                     'liver disease and heavy alcohol use, often to 2 g daily. Gabapentinoids are '
                                     'renally cleared and sedating. Ketamine can raise blood pressure and cause '
                                     'dissociation.'},
 'v147_gen_11': {'stem': 'A 52-year-old man with severe obstructive sleep apnea, AHI 45 on CPAP, and BMI 38 is '
                         'opioid-naive. He is recovering from tonsillectomy and uvulopalatopharyngoplasty and reports '
                         'pain of 8 out of 10 on swallowing. Kidney function is normal, and he has no ulcer or '
                         'bleeding history. The team writes his analgesic orders for the ward and discharge. Which '
                         'plan is most appropriate?',
                 'choices': ['Morphine PCA with a basal infusion and supplemental oxygen overnight',
                             'Scheduled acetaminophen and ibuprofen, with low-dose opioid for breakthrough',
                             'Scheduled oxycodone every 4 hours plus gabapentin at bedtime',
                             'Opioids alone, avoiding NSAIDs because of bleeding after tonsillectomy'],
                 'answer': 1,
                 'explanation': 'Multimodal analgesia reduces opioid exposure and its respiratory risks, which matter '
                                'greatly in severe obstructive sleep apnea. Scheduled acetaminophen and an NSAID form '
                                'the base; ibuprofen does not meaningfully increase post-tonsillectomy hemorrhage and '
                                'is recommended in the AAO-HNSF tonsillectomy guideline. Opioids are reserved for '
                                'breakthrough pain at the lowest effective dose, with CPAP used during sleep and '
                                'continuous monitoring such as pulse oximetry or capnography. Sedative combinations '
                                'are avoided.',
                 'why_wrong': ['Basal opioid infusions raise the risk of respiratory depression in sleep apnea, and '
                               'oxygen can mask hypoventilation.',
                               'Correct.',
                               'Combining scheduled opioids with gabapentin compounds sedation and respiratory '
                               'depression risk in severe sleep apnea.',
                               'Ibuprofen is safe after tonsillectomy per guideline evidence, and avoiding nonopioids '
                               'increases opioid exposure.'],
                 'board_pearl': 'In obstructive sleep apnea, build analgesia on acetaminophen and NSAIDs, limit '
                                'opioids, and monitor with CPAP use.',
                 'curveball': 'How does NSAID use change after a procedure with high bleeding concern, such as a '
                              'thyroidectomy in a patient on antiplatelet therapy?',
                 'curveball_answer': 'When even a small hematoma is dangerous or the patient has another bleeding '
                                     'risk, many surgeons avoid nonselective NSAIDs for the first 24 to 48 hours and '
                                     'rely on acetaminophen, local anesthetic, and adjuncts, or use a COX-2 selective '
                                     'agent, which has minimal platelet effect. The choice is individualized, since '
                                     'evidence for NSAID-related hematoma after thyroidectomy is mixed.'},
 'v273_gen_pain_fnd': {'stem': 'A 45-year-old woman with normal kidney and liver function is scheduled for total '
                               'thyroidectomy. She asks how her pain will be managed and says she wants to avoid '
                               'feeling drugged. She has no bleeding disorder, ulcer history, or sleep apnea. The '
                               'resident drafts a perioperative analgesia plan consistent with current guidance. Which '
                               'plan best reflects modern practice?',
                       'choices': ['Scheduled oxycodone every 4 hours as the foundation of her regimen',
                                   'Avoid acetaminophen because it impairs platelets and raises hematoma risk',
                                   'Codeine at discharge because it is weaker and safer than other opioids',
                                   'Acetaminophen, an NSAID, local anesthetic, and opioid only as rescue'],
                       'answer': 3,
                       'explanation': 'Modern perioperative analgesia is multimodal: scheduled acetaminophen, an NSAID '
                                      'when bleeding and renal risks allow, wound infiltration or regional block with '
                                      'local anesthetic, and selected adjuncts, with opioids reserved for breakthrough '
                                      'pain. Many thyroidectomy patients need few or no opioid tablets. The AAO-HNSF '
                                      'opioid guideline recommends counseling, limiting quantity, and favoring '
                                      'nonopioid first-line therapy. Regimens must be individualized to renal and '
                                      'hepatic function, bleeding risk, sleep apnea, and procedure.',
                       'why_wrong': ['Scheduled opioids as the foundation increase nausea, constipation, sedation, and '
                                     'persistent use without better pain control.',
                                     'Acetaminophen does not impair platelet function and is the safest base of '
                                     'multimodal analgesia.',
                                     'Codeine depends on CYP2D6 conversion to morphine, so effect is unpredictable, '
                                     'with toxicity in ultrarapid metabolizers.',
                                     'Correct.'],
                       'board_pearl': 'Multimodal analgesia: acetaminophen, NSAID when safe, local anesthetic, and '
                                      'opioids only for breakthrough pain.',
                       'curveball': 'Which patient factors would make you reduce opioid dosing or increase '
                                    'postoperative respiratory monitoring?',
                       'curveball_answer': 'Obstructive sleep apnea, obesity, older age, frailty, chronic lung '
                                           'disease, renal or hepatic impairment that slows clearance, concurrent '
                                           'benzodiazepines or gabapentinoids, opioid naivety receiving high doses, '
                                           'and airway surgery or edema all raise respiratory risk. These warrant '
                                           'lower doses, avoiding basal infusions, CPAP use, and continuous pulse '
                                           'oximetry or capnography.'},
 'v273_gen_pain_app': {'stem': 'A 55-year-old man with severe obstructive sleep apnea is 6 hours out from transoral '
                               'robotic tongue base reduction. After three doses of IV hydromorphone over 2 hours, he '
                               'is difficult to arouse, with respiratory rate of 6, loud snoring with pauses, and '
                               'oxygen saturation of 94% on 4 L/min nasal cannula. There is no neck swelling or '
                               'bleeding. What is the best immediate response?',
                       'choices': ['Stimulate, support ventilation, stop opioids, and titrate naloxone',
                                   'Increase oxygen to 10 L/min by face mask and recheck him in an hour',
                                   'Give flumazenil and continue the hydromorphone schedule as written',
                                   'Allow him to sleep, since his saturation is normal on oxygen'],
                       'answer': 0,
                       'explanation': 'A slow respiratory rate with depressed consciousness after repeated opioids is '
                                      'opioid-induced ventilatory impairment, made worse by sleep apnea and airway '
                                      'surgery. Supplemental oxygen keeps saturation normal while carbon dioxide '
                                      'rises, so oximetry is falsely reassuring. He needs immediate stimulation, '
                                      'airway maneuvers and bag-mask support if needed, cessation of opioids and '
                                      'sedatives, small titrated doses of naloxone, and escalation to monitored care. '
                                      'The airway should also be examined for edema, bleeding, or hematoma.',
                       'why_wrong': ['Correct.',
                                     'More oxygen further masks hypoventilation and does nothing for the slow '
                                     'respiratory rate and rising carbon dioxide.',
                                     'Flumazenil reverses benzodiazepines, not opioids, and continuing hydromorphone '
                                     'would worsen his respiratory depression.',
                                     'Normal saturation on oxygen does not exclude hypoventilation, and unmonitored '
                                     'sleep risks respiratory arrest.'],
                       'board_pearl': 'Supplemental oxygen can hide opioid hypoventilation; respiratory rate and '
                                      'arousal matter more than saturation.',
                       'curveball': 'How would neck swelling, stridor, or bloody oral output change your differential '
                                    'and threshold for return to the OR?',
                       'curveball_answer': 'Swelling, stridor, or bleeding points to a mechanical cause such as '
                                           'hematoma, tongue base edema, or hemorrhage rather than opioid effect '
                                           'alone. Naloxone will not fix it. The threshold for securing the airway, '
                                           'often by awake fiberoptic intubation, and returning to the OR for '
                                           'hemostasis falls sharply, with tracheostomy ready. Steroids may help edema '
                                           'but cannot replace airway control.'},
 'v273_gen_pain_snr': {'stem': 'A 61-year-old man with recurrent oral cavity cancer takes extended-release oxycodone '
                               '60 mg twice daily plus immediate-release doses for tumor pain. After composite '
                               'resection and free flap, his orders are morphine 2 mg IV every 4 hours as needed. On '
                               'day 1 he reports pain of 9 out of 10 and is sweating, yawning, and has rhinorrhea and '
                               'piloerection. He has a nasogastric tube. What is the best plan?',
                       'choices': ['Replace his baseline opioid dose, add nonopioids, and dose breakthrough higher',
                                   'Hold all opioids for a day to reassess his true baseline pain level',
                                   'Add lorazepam for anxiety and keep the low-dose as-needed morphine',
                                   'Stop opioids and rely on scheduled IV ketorolac for pain control'],
                       'answer': 0,
                       'explanation': 'He is opioid tolerant and now in withdrawal, with sweating, yawning, '
                                      'rhinorrhea, and piloerection, because his baseline requirement was not '
                                      'replaced. Management is to continue his baseline opioid as an equivalent dose '
                                      'through the feeding tube or IV, add multimodal analgesia, and give breakthrough '
                                      'doses scaled to his tolerance, commonly 10 to 20% of the daily total, with '
                                      'respiratory monitoring. Pain or palliative care consultation helps. '
                                      'Undertreatment impairs coughing, mobilization, and swallowing rehabilitation.',
                       'why_wrong': ['Correct.',
                                     'Stopping opioids worsens withdrawal and pain and gives no meaningful information '
                                     'about baseline pain.',
                                     'Benzodiazepines do not treat withdrawal or pain here and add respiratory '
                                     'depression risk.',
                                     'Ketorolac alone cannot replace a large daily opioid requirement and adds '
                                     'bleeding risk after free-flap surgery.'],
                       'board_pearl': 'Opioid-tolerant patients need their baseline opioid continued after surgery '
                                      'plus tolerance-adjusted breakthrough dosing.',
                       'curveball': 'If he had instead been on methadone or buprenorphine maintenance for opioid use '
                                    'disorder, how would the perioperative medication plan change?',
                       'curveball_answer': 'Current guidance favors continuing buprenorphine through surgery, '
                                           'sometimes in divided doses, adding multimodal analgesia and full agonists '
                                           'at higher doses for breakthrough as needed. Methadone is continued at the '
                                           'verified daily dose, with QTc monitoring. The prescriber or addiction '
                                           'medicine should be contacted to confirm doses, and the discharge plan '
                                           'arranged with them.'},
 'v139_gen_19': {'stem': 'A 44-year-old man has 6 months of bloody nasal crusting, nasal obstruction, and progressive '
                         'exertional stridor. Endoscopy shows friable, crusted mucosa with an anterior septal '
                         'perforation, and laryngoscopy shows circumferential subglottic narrowing. Urinalysis shows '
                         'red cell casts and creatinine is 2.1 mg/dL, up from normal a year ago. Chest CT shows two '
                         'cavitating nodules. Which diagnosis is most likely?',
                 'choices': ['Sarcoidosis',
                             'Granulomatosis with polyangiitis',
                             'Relapsing polychondritis',
                             'Eosinophilic granulomatosis with polyangiitis'],
                 'answer': 1,
                 'explanation': 'Granulomatosis with polyangiitis is a necrotizing granulomatous small-vessel '
                                'vasculitis that classically involves the upper airway, lungs, and kidneys. '
                                'Destructive sinonasal disease with crusting and septal perforation, subglottic '
                                'stenosis, cavitating lung nodules, and glomerulonephritis with red cell casts form '
                                'the classic pattern. ENT findings often precede the systemic diagnosis. PR3-ANCA is '
                                'positive in most patients with generalized disease, and biopsy shows necrotizing '
                                'granulomatous inflammation with vasculitis.',
                 'why_wrong': ['Sarcoidosis causes nasal crusting and hilar adenopathy but rarely cavitating nodules '
                               'with glomerulonephritis and red cell casts.',
                               'Correct.',
                               'Relapsing polychondritis affects auricular and laryngotracheal cartilage, but it does '
                               'not cause cavitating nodules or necrotizing glomerulonephritis.',
                               'EGPA features adult-onset asthma, nasal polyps, and eosinophilia rather than '
                               'destructive septal perforation with cavitating nodules.'],
                 'board_pearl': 'Crusting with septal perforation, subglottic stenosis, lung nodules, and nephritis: '
                                'granulomatosis with polyangiitis.',
                 'curveball': 'What laboratory and tissue findings support GPA, recognizing that ANCA can be negative?',
                 'curveball_answer': 'PR3-ANCA with a cytoplasmic pattern is the most specific serology, though '
                                     'MPO-ANCA occurs in some patients and limited sinonasal disease is ANCA-negative '
                                     'in a substantial minority. Biopsy shows necrotizing granulomas, vasculitis, and '
                                     'geographic necrosis, although nasal biopsies are often nonspecific. Elevated ESR '
                                     'and CRP, hematuria, and red cell casts support systemic disease.'},
 'v147_gen_12': {'stem': 'A 52-year-old woman has 8 months of nasal crusting with bloody discharge, chronic otitis '
                         'media with effusion, and new exertional stridor. Laryngoscopy shows smooth subglottic '
                         'narrowing. Chest CT shows multiple nodules, two of them cavitating, and urinalysis shows '
                         'dysmorphic red cells. She has no asthma, eosinophilia, or hilar adenopathy. Which serologic '
                         'test most specifically supports the unifying diagnosis?',
                 'choices': ['MPO-ANCA with perinuclear staining',
                             'Serum angiotensin-converting enzyme',
                             'PR3-ANCA with cytoplasmic staining',
                             'Anti-double-stranded DNA antibody'],
                 'answer': 2,
                 'explanation': 'Sinonasal crusting, otitis media with effusion from eustachian tube involvement, '
                                'subglottic stenosis, cavitating lung nodules, and glomerular hematuria point to '
                                'granulomatosis with polyangiitis. PR3-ANCA with a cytoplasmic pattern is the most '
                                'specific serologic marker and is positive in most patients with generalized disease. '
                                'Because limited disease may be ANCA-negative, tissue biopsy remains important. '
                                'Controlling inflammation with rituximab or cyclophosphamide plus steroids precedes '
                                'purely structural airway surgery.',
                 'why_wrong': ['MPO-ANCA is typical of microscopic polyangiitis and EGPA and is less specific for this '
                               'classic granulomatous pattern.',
                               'ACE is elevated in some sarcoidosis, but its sensitivity and specificity are poor, and '
                               'she lacks hilar adenopathy.',
                               'Correct.',
                               'Anti-dsDNA supports systemic lupus erythematosus, which does not cause destructive '
                               'sinonasal disease or cavitating nodules.'],
                 'board_pearl': 'PR3-ANCA with cytoplasmic staining is the most specific serology for granulomatosis '
                                'with polyangiitis.',
                 'curveball': 'Her stridor progresses over the next year. How should active GPA affect the timing of '
                              'subglottic airway reconstruction?',
                 'curveball_answer': 'Open reconstruction such as laryngotracheal resection is deferred until disease '
                                     'is in remission, because active inflammation causes restenosis and poor healing. '
                                     'During active disease, airway symptoms are managed endoscopically with dilation, '
                                     'radial incisions, and intralesional steroid injection, alongside systemic '
                                     'therapy. Tracheostomy is reserved for critical obstruction that cannot be '
                                     'managed endoscopically.'},
 'v274_gen_sys_fnd': {'stem': 'A 38-year-old man has 6 months of nasal obstruction and crusting that have not improved '
                              'with saline irrigations, nasal steroids, and two antibiotic courses. He also reports '
                              'joint aches and fatigue, and his ESR is elevated. His primary physician refers him for '
                              'presumed chronic rhinosinusitis. On examination, which finding would most raise concern '
                              'for granulomatosis with polyangiitis rather than routine sinus disease?',
                      'choices': ['Bilateral polyps with thick eosinophilic mucin in both ethmoid cavities',
                                  'Purulent drainage from the middle meatus with maxillary sinus tenderness',
                                  'Bilateral inferior turbinate hypertrophy that decongests with oxymetazoline',
                                  'Septal perforation, friable crusted mucosa, and subglottic narrowing'],
                      'answer': 3,
                      'explanation': 'Destructive features distinguish granulomatosis with polyangiitis from ordinary '
                                     'chronic rhinosinusitis. Friable, crusted, bleeding mucosa, septal perforation or '
                                     'saddle deformity, and subglottic stenosis in a patient with constitutional '
                                     'symptoms and raised inflammatory markers suggest systemic vasculitis. Diagnosis '
                                     'integrates the clinical pattern, PR3-ANCA, urinalysis and creatinine, chest '
                                     'imaging, and biopsy of the most active site. Early recognition matters because '
                                     'renal and pulmonary involvement can be life-threatening.',
                      'why_wrong': ['Polyps with eosinophilic mucin suggest chronic rhinosinusitis with polyps or '
                                    'allergic fungal sinusitis rather than a destructive vasculitis.',
                                    'Purulent meatal drainage with tenderness fits bacterial rhinosinusitis, which '
                                    'explains his antibiotic courses but not systemic features.',
                                    'Turbinate hypertrophy that decongests reflects mucosal swelling from rhinitis, '
                                    'not tissue destruction or granulomatous disease.',
                                    'Correct.'],
                      'board_pearl': 'Septal perforation, friable crusting, and subglottic stenosis signal '
                                     'granulomatous vasculitis, not routine sinusitis.',
                      'curveball': 'Rheumatology wants to start high-dose steroids today. What findings make tissue '
                                   'diagnosis urgent before immunosuppression is started?',
                      'curveball_answer': 'Biopsy is needed promptly when the differential includes infection, such as '
                                          'invasive fungal sinusitis or mycobacteria, or malignancy such as extranodal '
                                          'NK/T-cell lymphoma, which causes midline destruction and would worsen with '
                                          'steroids. Necrotic, progressive, or unilateral destructive lesions and '
                                          'ANCA-negative disease raise these concerns. Biopsy should not delay '
                                          'treatment of rapidly progressive renal or pulmonary involvement.'},
 'v274_gen_sys_app': {'stem': 'A 46-year-old woman has 5 months of refractory nasal crusting and now a new saddle-nose '
                              'deformity. She has had intermittent hemoptysis and her urine dipstick shows 3+ blood. '
                              'Chest radiograph shows two nodules, and creatinine has risen from 0.9 to 1.6 mg/dL over '
                              '2 months. She asks whether her nose can be fixed. What is the best next approach?',
                      'choices': ['Septorhinoplasty with costal cartilage to restore dorsal support',
                                  'Revision endoscopic sinus surgery for refractory chronic sinusitis',
                                  'Urgent ANCA, renal and chest workup, and rheumatology input',
                                  'Prolonged itraconazole for presumed chronic fungal sinusitis'],
                      'answer': 2,
                      'explanation': 'Destructive sinonasal disease with saddle nose, hemoptysis, lung nodules, '
                                     'hematuria, and rising creatinine suggests systemic vasculitis, most likely '
                                     'granulomatosis with polyangiitis with lung and kidney involvement. '
                                     'Life-threatening organ involvement and diagnostic confirmation take priority: '
                                     'ANCA serology, urinalysis with microscopy, creatinine trend, chest CT, and '
                                     'rheumatology and nephrology input, with biopsy of an accessible active site. '
                                     'Cosmetic or structural nasal reconstruction is delayed until the disease has '
                                     'been in remission for a sustained period.',
                      'why_wrong': ['Reconstruction during active vasculitis risks graft resorption and failure, and '
                                    'it ignores rapidly progressive kidney injury.',
                                    'More sinus surgery treats the local symptom while missing a systemic vasculitis '
                                    'threatening her kidneys and lungs.',
                                    'Correct.',
                                    'Nothing supports fungal disease, and antifungals would delay treatment of active '
                                    'vasculitis with renal involvement.'],
                      'board_pearl': 'Destructive nasal disease plus lung or kidney findings is systemic vasculitis '
                                     'until proven otherwise; organ threat comes first.',
                      'curveball': 'How would suspected invasive fungal disease alter the urgency and biopsy strategy?',
                      'curveball_answer': 'If she were immunocompromised or had necrotic, insensate mucosa, invasive '
                                          'fungal sinusitis would become the leading concern. Same-day endoscopic '
                                          'biopsy with frozen section and fungal stains would be needed, and steroids '
                                          'would be withheld until infection was excluded, because immunosuppression '
                                          'could accelerate a fatal infection. Debridement and antifungal therapy '
                                          'would follow positive findings.'},
 'v274_gen_sys_snr': {'stem': 'A 39-year-old woman with known granulomatosis with polyangiitis has a systemic flare '
                              'with rising creatinine and new arthralgias, and she was started on rituximab and '
                              'high-dose steroids 4 days ago. Over 2 weeks her exertional stridor has worsened, and '
                              'she now has stridor at rest. Laryngoscopy shows firm, circumferential subglottic '
                              'stenosis narrowing the lumen by about 70%. Oxygen saturation is 96%. What is the best '
                              'management?',
                      'choices': ['Endoscopic dilation with intralesional steroid alongside systemic therapy',
                                  'Rely on rituximab and steroids and recheck the airway in 6 weeks',
                                  'Open laryngotracheal resection now to definitively remove the stenosis',
                                  'Inhaled budesonide and racemic epinephrine with outpatient follow-up'],
                      'answer': 0,
                      'explanation': 'GPA subglottic stenosis often combines active inflammation with fixed scar and '
                                     'may not respond to systemic therapy alone. Stridor at rest with 70% narrowing '
                                     'threatens the airway and needs prompt local intervention, typically endoscopic '
                                     'dilation with radial incisions and intralesional steroid injection, while '
                                     'rheumatology continues systemic immunosuppression. Open reconstruction is '
                                     'deferred until remission because active disease causes restenosis and poor '
                                     'healing, and tracheostomy is reserved for failure of endoscopic management.',
                      'why_wrong': ['Correct.',
                                    'Systemic therapy treats active inflammation, but a firm fixed stenosis causing '
                                    'stridor at rest needs airway intervention now.',
                                    'Open resection during an uncontrolled flare carries high restenosis and '
                                    'anastomotic failure rates and should wait for remission.',
                                    'Inhaled steroids and racemic epinephrine do not relieve fixed subglottic scar and '
                                    'are unsafe with stridor at rest.'],
                      'board_pearl': 'GPA subglottic stenosis with stridor: endoscopic dilation and steroid injection '
                                     'plus systemic therapy; defer open repair to remission.',
                      'curveball': 'At laryngoscopy, which features of the subglottic lesion suggest inflammatory '
                                   'edema rather than mature cicatricial stenosis?',
                      'curveball_answer': 'Inflammatory disease appears as red, friable, edematous mucosa that may '
                                          'bleed, often with active systemic disease and raised inflammatory markers, '
                                          'and may improve with immunosuppression. Mature scar appears pale, firm, '
                                          'smooth, and circumferential, persists during remission, and responds only '
                                          'to dilation or surgery. Many patients have both, which is why dilation with '
                                          'steroid injection is combined with systemic therapy.'},
 'v139_gen_20': {'stem': 'A 66-year-old man completed 70 Gy of radiation to the neck 3 years ago for laryngeal cancer '
                         'and later had a neck dissection with plate fixation for a mandibular fracture. He now has a '
                         'chronic draining neck wound with exposed hardware. The surrounding skin is woody, hairless, '
                         'and pale with telangiectasias. Cultures show mixed skin flora. Which mechanism best explains '
                         'his impaired healing?',
                 'choices': ['Persistent hyperemia from radiation that causes chronic tissue edema',
                             'Obliterative endarteritis causing hypovascular, hypocellular, hypoxic tissue',
                             'Radiation-induced immune suppression that allows bacterial overgrowth',
                             'Overactive matrix metalloproteinases dissolving all newly formed collagen'],
                 'answer': 1,
                 'explanation': 'Radiation damages small blood vessels, causing obliterative endarteritis and '
                                'progressive loss of microvasculature, and injures fibroblasts and stem cells, leaving '
                                'tissue that is hypovascular, hypocellular, and hypoxic, the classic description by '
                                'Marx. Fibrosis replaces normal tissue and worsens over time. Wound healing depends on '
                                'perfusion, oxygenation, nutrition, infection control, and mechanical stability, and '
                                'radiation impairs several of these at once, which is why vascularized nonirradiated '
                                'tissue is often needed for coverage.',
                 'why_wrong': ['Acute radiation causes transient inflammation, but late irradiated tissue is pale and '
                               'poorly perfused, not hyperemic.',
                               'Correct.',
                               'Local radiation does not cause systemic immunosuppression, and the colonizing flora '
                               'reflects the poor bed rather than causing it.',
                               'Proteases matter in chronic wounds, but the dominant late radiation injury is vascular '
                               'and cellular loss with fibrosis.'],
                 'board_pearl': 'Irradiated tissue is hypovascular, hypocellular, and hypoxic from obliterative '
                                'endarteritis; it heals poorly and worsens over time.',
                 'curveball': 'When should vascularized flap coverage be favored over repeated local closure in an '
                              'irradiated wound?',
                 'curveball_answer': 'Favor a regional or free flap when local closure has already failed, when '
                                     'hardware, bone, or great vessels are exposed, when the defect cannot be closed '
                                     'without tension, or when skin edges are fibrotic and poorly perfused. Bringing '
                                     'in nonirradiated, well-vascularized tissue, such as a pectoralis major or free '
                                     'flap, supplies blood flow and cells the bed cannot provide.'},
 'v147_gen_13': {'stem': 'A 63-year-old woman had salvage total laryngectomy for recurrent glottic cancer 14 months '
                         'after chemoradiation. On postoperative day 9 the neck incision separates along a 3 cm '
                         'segment, with pale, poorly bleeding edges and no saliva leak. Albumin is 3.7 g/dL, glucose '
                         'and thyroid function are normal, and she does not smoke. The intern asks why her wound is '
                         'failing. Which explanation is most accurate?',
                 'choices': ['Fibroblasts that overproduce collagen and form a hypertrophic scar',
                             'Increased angiogenesis creating fragile, leaky wound vessels',
                             'Loss of skin innervation that prevents normal wound contraction',
                             'Microvascular and fibroblast injury reducing perfusion and repair'],
                 'answer': 3,
                 'explanation': 'Radiation damages endothelial cells and small vessels and injures fibroblasts and '
                                'progenitor cells, so irradiated tissue has fewer vessels, less oxygen, fewer '
                                'functional repair cells, and more fibrosis. Pale, poorly bleeding edges show this '
                                'reduced perfusion. With nutrition, glucose, thyroid function, and smoking already '
                                'addressed, the residual problem is the irradiated bed. This is why salvage surgery '
                                'has higher wound and fistula rates and why vascularized nonirradiated tissue is often '
                                'used.',
                 'why_wrong': ['Hypertrophic scarring is an excessive healing response; irradiated wounds instead show '
                               'deficient repair and poor collagen deposition.',
                               'Radiation reduces angiogenesis and microvascular density rather than increasing it.',
                               'Denervation is not the main mechanism; impaired perfusion and loss of repair cells '
                               'drive radiation wound failure.',
                               'Correct.'],
                 'board_pearl': 'Radiation causes microvascular and fibroblast injury, so salvage surgery wounds heal '
                                'poorly and often need vascularized tissue.',
                 'curveball': 'Her surgeon is planning the next salvage laryngectomy. What role can vascularized flap '
                              'tissue play in the pharyngeal closure?',
                 'curveball_answer': 'An onlay pectoralis major flap or a free flap interposed in the pharyngeal '
                                     'closure brings nonirradiated vascularized tissue to the repair. Meta-analyses '
                                     'show this reduces pharyngocutaneous fistula rates and shortens fistula duration '
                                     'compared with primary closure after chemoradiation. Many surgeons use it '
                                     'routinely in salvage cases.'},
 'v274_gen_wound_fnd': {'stem': 'A 40-year-old man had a 5 cm laceration of the cheek that was cleaned and left partly '
                                'open because of contamination. At a wound check 7 days later, the base is filled with '
                                'beefy red, granular, moist tissue that bleeds easily, and the edges are beginning to '
                                'pull inward with new pink epithelium at the margins. Which process predominates '
                                'during this phase of healing?',
                        'choices': ['Platelet plug formation with fibrin clot and neutrophil influx',
                                    'Cross-linking and replacement of type III by type I collagen',
                                    'Neutrophil-dominated clearance of debris and bacteria from the wound',
                                    'Fibroblast proliferation, angiogenesis, and type III collagen deposition'],
                        'answer': 3,
                        'explanation': 'Beefy red granulation tissue at about 1 week marks the proliferative phase, '
                                       'which follows hemostasis and inflammation and lasts from roughly day 4 to week '
                                       '3. Fibroblasts proliferate and deposit type III collagen and extracellular '
                                       'matrix, new capillaries form through angiogenesis, myofibroblasts begin wound '
                                       'contraction, and keratinocytes migrate across the surface. The later '
                                       'remodeling phase, lasting months, replaces type III with type I collagen and '
                                       'increases tensile strength.',
                        'why_wrong': ['Platelet plug and fibrin clot formation occur in the first minutes to hours '
                                      'during hemostasis, not at 1 week.',
                                      'Collagen cross-linking and conversion to type I occur during remodeling, which '
                                      'begins weeks later and lasts months.',
                                      'Neutrophil clearance dominates the first 1 to 3 days; by day 7 macrophages and '
                                      'fibroblasts drive the wound.',
                                      'Correct.'],
                        'board_pearl': 'Proliferative phase: fibroblasts, angiogenesis, granulation tissue, type III '
                                       'collagen, and epithelial migration.',
                        'curveball': 'If he were a smoker with diabetes, prior radiation, and malnutrition, how would '
                                     'each of these alter the phases of healing?',
                        'curveball_answer': 'Radiation reduces vascularity and fibroblast function, impairing '
                                            'proliferation. Diabetes impairs neutrophil function and angiogenesis and '
                                            'promotes infection. Nicotine causes vasoconstriction and reduces oxygen '
                                            'delivery. Protein, vitamin C, and zinc deficiencies impair collagen '
                                            'synthesis and cross-linking, and corticosteroids blunt inflammation, an '
                                            'effect partly reversed by vitamin A.'},
 'v274_gen_wound_app': {'stem': 'A 62-year-old man had a salvage neck dissection for recurrent nodal disease 2 years '
                                'after chemoradiation. On postoperative day 10 the irradiated skin flap edges become '
                                'necrotic and separate, exposing a 2 cm segment of the common carotid artery covered '
                                'only by adventitia, with surrounding purulent exudate. He is afebrile and '
                                'hemodynamically stable. Albumin is 2.9 g/dL. What is the best management?',
                        'choices': ['Wet-to-dry dressings until granulation tissue covers the artery',
                                    'Debride, optimize nutrition, and cover the artery with a vascularized flap',
                                    'Negative-pressure dressing placed directly over the exposed artery',
                                    'Re-suture the necrotic skin edges at the bedside over a drain'],
                        'answer': 1,
                        'explanation': 'An exposed carotid in an infected, irradiated wound is at high risk of drying, '
                                       'infection, and blowout. Radiation impairs vascularity and repair, so waiting '
                                       'for granulation or closing compromised edges again will fail. The principle is '
                                       'source control and durable vascularized coverage: debride necrotic and '
                                       'infected tissue, address systemic factors such as nutrition, and cover the '
                                       'artery promptly with well-vascularized nonirradiated tissue, typically a '
                                       'pectoralis major or free flap, while planning for possible carotid bleeding.',
                        'why_wrong': ['Granulation over irradiated carotid adventitia is slow and unreliable, and '
                                      'dressing changes risk desiccation and blowout.',
                                      'Correct.',
                                      'Negative-pressure therapy directly on exposed major vessels is contraindicated '
                                      'because it can precipitate hemorrhage.',
                                      'Necrotic irradiated edges cannot heal when re-sutured, and closing over '
                                      'infection leaves the artery at risk.'],
                        'board_pearl': 'Irradiated wound breakdown over vital structures: debride, optimize, and '
                                       'import vascularized tissue rather than re-close.',
                        'curveball': 'A small sentinel bleed occurs from the wound before surgery. How does this '
                                     'change management?',
                        'curveball_answer': 'A sentinel bleed from an exposed carotid warns of impending blowout. '
                                            'Apply pressure, secure large-bore access and the airway, type and cross '
                                            'blood, and obtain urgent CT angiography or go directly to angiography for '
                                            'endovascular stenting or occlusion after balloon test occlusion when '
                                            'possible. Definitive debridement and flap coverage follow once the vessel '
                                            'is controlled.'},
 'v274_gen_wound_snr': {'stem': 'A 34-year-old woman had a total thyroidectomy 3 months ago. Her horizontal neck scar '
                                'is red, raised, firm, and itchy, and has widened to 6 mm, but it stays within the '
                                'borders of the original incision. She has no personal or family history of keloids. '
                                'She is distressed by its appearance and asks for immediate surgical excision. What is '
                                'the best approach?',
                        'choices': ['Excise and re-close the scar now with a careful layered closure',
                                    'Low-dose radiation to the scar now to prevent further hypertrophy',
                                    'Silicone, massage, and steroid injection, then revise once mature',
                                    'Reassure her that nothing can be done for at least 2 years'],
                        'answer': 2,
                        'explanation': 'A raised, red, itchy scar confined to the incision at 3 months is a '
                                       'hypertrophic scar, which tends to regress as it matures over 12 to 18 months. '
                                       'Early treatment is conservative: silicone gel or sheeting, pressure or '
                                       'massage, sun protection, and intralesional triamcinolone for persistent raised '
                                       'areas, with pulsed dye laser as an option for redness. Revision is reserved '
                                       'for a stable mature scar, and should address tension vectors such as neck '
                                       'extension, unless function is affected.',
                        'why_wrong': ['Excising an immature hypertrophic scar often recreates the same scar, because '
                                      'the tension and active remodeling that caused it persist.',
                                      'Radiation is reserved mainly for adjuvant treatment after keloid excision, not '
                                      'for an immature hypertrophic scar in a young patient.',
                                      'Correct.',
                                      'Effective early treatments exist, including silicone and steroid injection, so '
                                      'telling her to wait 2 years with no therapy is wrong.'],
                        'board_pearl': 'Immature hypertrophic scar: silicone, massage, and steroid injection while it '
                                       'matures; revise only after maturity and tension correction.',
                        'curveball': 'When would a contracture threatening eyelid closure, airway, or neck motion '
                                     'justify earlier surgery?',
                        'curveball_answer': 'Functional compromise overrides the wait for maturation. An ectropion '
                                            'with corneal exposure, a contracture limiting neck extension or mouth '
                                            'opening, or a scar band affecting the airway or stoma warrants early '
                                            'release with Z-plasty, grafts, or flaps to lengthen the scar and redirect '
                                            'tension, followed by scar therapy afterward.'},
 'v431-cervical-necrotizing-fasciitis-02': {'stem': 'A 57-year-old woman developed rapidly spreading right neck '
                                                    'swelling 3 days after a peritonsillar abscess was drained. She is '
                                                    'febrile and tachycardic, with dusky skin and crepitus. At '
                                                    'surgery, thin gray foul-smelling fluid is found, the deep '
                                                    'cervical fascia is necrotic and separates from muscle with blunt '
                                                    'finger dissection, and the tissue does not bleed. Which process '
                                                    'best explains these operative findings?',
                                            'choices': ['Polymicrobial spread along fascial planes with small-vessel '
                                                        'thrombosis',
                                                        'A walled-off abscess caused by a single organism in one neck '
                                                        'space',
                                                        'Toxin-driven myonecrosis from Clostridium with primary muscle '
                                                        'death',
                                                        'An immune-complex vasculitis set off by the recent pharyngeal '
                                                        'infection'],
                                            'answer': 0,
                                            'explanation': 'Cervical necrotizing fasciitis is usually a polymicrobial '
                                                           'synergistic infection, with streptococci, staphylococci, '
                                                           'gram-negative rods, and anaerobes from an odontogenic or '
                                                           'pharyngeal source. Bacterial enzymes and toxins spread '
                                                           'infection rapidly along fascial planes, and thrombosis of '
                                                           'small perforating vessels causes ischemic necrosis of '
                                                           'fascia and overlying skin, which explains the dishwater '
                                                           'fluid, easy finger dissection, and lack of bleeding. '
                                                           'Spread through the retropharyngeal and danger spaces can '
                                                           'produce descending necrotizing mediastinitis, so thoracic '
                                                           'extension must be anticipated.',
                                            'why_wrong': ['Correct.',
                                                          'An abscess is a contained collection of pus with a wall; '
                                                          'this infection is spreading along planes without '
                                                          'containment.',
                                                          'Clostridial myonecrosis primarily destroys muscle, whereas '
                                                          'here the fascia is necrotic and separates easily from '
                                                          'viable muscle.',
                                                          'Immune-complex vasculitis does not produce foul dishwater '
                                                          'fluid, crepitus, or rapidly spreading fascial necrosis.'],
                                            'board_pearl': 'Necrotizing fasciitis: polymicrobial fascial spread with '
                                                           'small-vessel thrombosis; watch for danger-space extension '
                                                           'to the mediastinum.',
                                            'curveball': 'She returns from the first debridement intubated and on '
                                                         'vasopressors. What supportive therapies should accompany '
                                                         'surgical debridement?',
                                            'curveball_answer': 'She needs ICU resuscitation with fluids and '
                                                                'vasopressors as required, a secure airway, and '
                                                                'broad-spectrum IV antibiotics covering aerobes and '
                                                                'anaerobes, such as a carbapenem or '
                                                                'piperacillin-tazobactam with vancomycin, plus '
                                                                'clindamycin for toxin suppression. Nutrition support, '
                                                                'glucose control, and planned serial re-exploration '
                                                                'follow. Hyperbaric oxygen is unproven and must not '
                                                                'delay surgery.'},
 'v431-cervical-necrotizing-fasciitis-01': {'stem': 'A 47-year-old man with alcohol use disorder has a 2-day history '
                                                    'of rapidly progressive left neck pain and swelling after a lower '
                                                    'molar infection. He has fever of 39.8 C, heart rate 128, and '
                                                    'blood pressure 94/60. The pain is severe but the skin shows only '
                                                    'mild duskiness and edema, without crepitus. Contrast CT shows '
                                                    'diffuse fascial thickening and fluid along the left neck without '
                                                    'gas or a discrete collection. What is the most appropriate next '
                                                    'step?',
                                            'choices': ['Continue IV antibiotics and repeat contrast CT in 24 hours',
                                                        'Ultrasound-guided aspiration of the edematous soft tissue',
                                                        'MRI of the neck to confirm fascial involvement before surgery',
                                                        'Secure the airway, resuscitate, and debride widely in the OR'],
                                            'answer': 3,
                                            'explanation': 'Cervical necrotizing fasciitis is a clinical diagnosis. '
                                                           'Rapid progression, systemic toxicity, pain out of '
                                                           'proportion to skin findings, and early duskiness after an '
                                                           'odontogenic infection are enough to act on, and gas may be '
                                                           'absent on CT. Fascial thickening and fluid without a '
                                                           'collection is consistent with the diagnosis. The airway is '
                                                           'secured, resuscitation and broad aerobic and anaerobic '
                                                           'coverage begin, and he goes immediately for wide '
                                                           'debridement to viable bleeding tissue. Delay to source '
                                                           'control increases mortality.',
                                            'why_wrong': ['Waiting 24 hours for gas or a collection allows necrosis to '
                                                          'spread, and antibiotics cannot penetrate thrombosed tissue.',
                                                          'There is no discrete collection to aspirate, and aspiration '
                                                          'does not remove necrotic fascia or establish source '
                                                          'control.',
                                                          'MRI is slow, difficult in a septic patient, and delays the '
                                                          'operation that both confirms and treats the disease.',
                                                          'Correct.'],
                                            'board_pearl': 'Necrotizing fasciitis is a clinical diagnosis; absent gas '
                                                           'on CT does not exclude it or justify delaying debridement.',
                                            'curveball': 'At surgery the fascia is gray and nonbleeding. What '
                                                         'operative principle governs the extent and follow-through of '
                                                         'his debridement?',
                                            'curveball_answer': 'Debride all necrotic fascia, fat, muscle, and skin '
                                                                'back to viable bleeding tissue, open and drain every '
                                                                'involved space, and leave the wounds open and packed. '
                                                                'Return to the operating room every 24 to 48 hours, or '
                                                                'sooner if he worsens, until no further necrosis is '
                                                                'found. Thoracic surgery drains the mediastinum if '
                                                                'infection has spread there.'},
 'v466_gent_necfasc_fnd': {'stem': 'A 61-year-old man with type 2 diabetes had a mandibular molar treated 4 days ago. '
                                   'He now has rapidly spreading swelling of the right submandibular area and upper '
                                   'neck over 12 hours, severe pain much worse than the mild skin redness suggests, a '
                                   'temperature of 39.5 C, heart rate 124, and a patch of dusky gray skin below the '
                                   'jaw. He is drinking water without difficulty. Which diagnosis should be excluded '
                                   'first?',
                           'choices': ['Odontogenic facial cellulitis',
                                       'Acute suppurative submandibular sialadenitis',
                                       'Cervical necrotizing fasciitis',
                                       'Angioedema from his ACE inhibitor'],
                           'answer': 2,
                           'explanation': 'Rapidly progressive neck swelling, pain out of proportion to the exam, '
                                          'systemic toxicity, and dusky skin after an odontogenic infection are the '
                                          'warning signs of cervical necrotizing fasciitis. Diabetes is a common risk '
                                          'factor. These findings call for immediate surgical evaluation, airway '
                                          'assessment, resuscitation, and broad-spectrum antibiotics, because '
                                          'mortality rises with each hour of delay. Crepitus, bullae, and gas on '
                                          'imaging support the diagnosis but are often absent early, so their absence '
                                          'does not reassure.',
                           'why_wrong': ['Simple cellulitis rarely causes pain out of proportion, toxicity, and dusky '
                                         'skin over hours, and treating it as cellulitis delays surgery.',
                                         'Sialadenitis causes a tender, swollen gland with purulent duct discharge, '
                                         'not rapidly spreading dusky skin and septic physiology.',
                                         'Correct.',
                                         'Angioedema causes painless, nonpitting swelling of lips and tongue without '
                                         'fever or skin necrosis.'],
                           'board_pearl': 'Pain out of proportion, rapid spread, toxicity, and dusky skin after dental '
                                          'infection: think necrotizing fasciitis first.',
                           'curveball': 'If crepitus is absent on exam, does that make necrotizing fasciitis less '
                                        'likely?',
                           'curveball_answer': 'Not meaningfully. Crepitus reflects gas from anaerobic organisms and '
                                               'is a late, insensitive sign, present in only a minority at '
                                               'presentation. The diagnosis rests on the clinical picture of rapid '
                                               'progression, toxicity, and pain out of proportion, and confirmation '
                                               'comes at surgery. Absent crepitus or gas should not delay operative '
                                               'exploration.'},
 'v466_gent_necfasc_app': {'stem': 'A 44-year-old woman has rapidly progressive right neck swelling, fever of 39.4 C, '
                                   'heart rate 120, and pain out of proportion after a dental abscess. She is stable '
                                   'enough for imaging, and contrast CT of the neck and chest shows fascial thickening '
                                   'without gas, a discrete abscess, or mediastinal fluid. Her calculated LRINEC score '
                                   'is 4. The emergency physician asks how to interpret these results. What is the '
                                   'best interpretation?',
                           'choices': ['The diagnosis remains clinical, so operative exploration is warranted',
                                       'The negative CT excludes necrotizing fasciitis, so treat as cellulitis',
                                       'A low LRINEC score confirms low risk, so observation on antibiotics is safe',
                                       'The scan should be repeated in 48 hours to look for gas before deciding'],
                           'answer': 0,
                           'explanation': 'Cervical necrotizing fasciitis is a clinical diagnosis. CT in a stable '
                                          'patient maps extent and identifies mediastinal involvement, but gas and '
                                          'discrete collections are often absent early, so a negative scan cannot '
                                          'exclude disease. Scoring tools such as LRINEC have poor sensitivity and '
                                          'should not override clinical suspicion. With rapid progression, toxicity, '
                                          'and pain out of proportion, the next step is surgical exploration, where '
                                          'gray, nonbleeding fascia that separates easily confirms the diagnosis and '
                                          'debridement follows.',
                           'why_wrong': ['Correct.',
                                         'CT has limited sensitivity early; fascial thickening without gas is '
                                         'compatible with necrotizing fasciitis and does not support cellulitis.',
                                         'LRINEC has poor sensitivity, and a low score does not exclude necrotizing '
                                         'fasciitis in a patient with this clinical picture.',
                                         'Waiting 48 hours for gas lets necrosis spread along fascial planes and '
                                         'raises mortality; surgery should not be delayed.'],
                           'board_pearl': 'A gas-negative CT or low LRINEC score does not exclude necrotizing '
                                          'fasciitis; clinical suspicion drives surgical exploration.',
                           'curveball': 'How does the workup differ for a well-localized fluctuant neck abscess '
                                        'without systemic toxicity or rapid progression?',
                           'curveball_answer': 'A contained abscess in a stable patient is mapped with contrast CT and '
                                               'treated with drainage of that collection, transoral or transcervical '
                                               'depending on location, plus culture-directed antibiotics, with serial '
                                               'exams. Small collections may even be treated with antibiotics alone. '
                                               'Necrotizing fasciitis instead needs wide debridement of all involved '
                                               'fascia and planned re-exploration.'},
 'v466_gent_necfasc_snr': {'stem': 'A 52-year-old man with poorly controlled diabetes has cervical necrotizing '
                                   'fasciitis from an odontogenic source, with dusky skin and crepitus spreading from '
                                   'the submandibular region to the anterior neck. He is intubated and on '
                                   'norepinephrine, and broad-spectrum antibiotics are running. The CT scanner will '
                                   'not be available for 2 hours because of a trauma backlog. What is the best '
                                   'decision?',
                           'choices': ['Wait for CT to map involved spaces before making any incision',
                                       'Proceed now to wide debridement and drainage of every involved space',
                                       'Take an incisional biopsy for frozen section before committing to debridement',
                                       'Continue antibiotics in the ICU, operating only if shock worsens'],
                           'answer': 1,
                           'explanation': 'Antibiotics cannot penetrate thrombosed, necrotic tissue, so surgical '
                                          'source control is the key determinant of survival, and delay increases '
                                          'mortality. With a clear clinical diagnosis and septic shock, he should go '
                                          'to the operating room now for wide debridement to viable bleeding tissue, '
                                          'opening and draining all involved spaces, with the wounds left open and a '
                                          'plan for serial re-exploration. Imaging can follow after the first '
                                          'operation, including CT of the chest to assess mediastinal spread.',
                           'why_wrong': ['Imaging helps map extent but must not delay surgery in a patient with an '
                                         'established clinical diagnosis and septic shock.',
                                         'Correct.',
                                         'Frozen section is unnecessary when the diagnosis is clinically clear and '
                                         'delays definitive debridement in a patient in shock.',
                                         'Medical therapy alone fails in necrotizing fasciitis; waiting for worsening '
                                         'shock allows necrosis to spread.'],
                           'board_pearl': 'Antibiotics do not replace debridement; with a clinical diagnosis, operate '
                                          'immediately and plan re-exploration.',
                           'curveball': 'If intraoperative or CT findings suggest danger-space extension toward the '
                                        'mediastinum, how should the operative plan change?',
                           'curveball_answer': 'Mediastinal extension, descending necrotizing mediastinitis, needs '
                                               'thoracic surgery involvement and mediastinal drainage in addition to '
                                               'cervical debridement. Infection limited above the carina may sometimes '
                                               'be drained through the neck, but spread below the carina or into '
                                               'multiple compartments usually requires thoracoscopic or open drainage. '
                                               'CT of the chest after the first operation guides this.'},
 'v431-penetrating-blunt-neck-trauma-01': {'stem': 'A 24-year-old man was stabbed in the left neck, midway between the '
                                                   'cricoid cartilage and the angle of the mandible. He has blood '
                                                   'pressure 132/78, a normal voice, no stridor, and no hemoptysis. '
                                                   'Examination shows a 2 cm wound that clearly penetrates the '
                                                   'platysma, with a small nonexpanding hematoma, no bruit, and no '
                                                   'subcutaneous emphysema. What is the most appropriate evaluation?',
                                           'choices': ['CT angiography of the neck with serial clinical examinations',
                                                       'Mandatory operative exploration because the platysma is '
                                                       'violated',
                                                       'Local wound exploration with probing to determine wound depth',
                                                       'Wound closure and discharge given his normal vital signs'],
                                           'answer': 0,
                                           'explanation': 'Classic zones describe exposure, with zone II lying between '
                                                          'the cricoid and the angle of the mandible, but stable '
                                                          'penetrating neck injuries without hard signs are now '
                                                          'evaluated selectively, often called a no-zone approach. '
                                                          'Platysma violation with a nonexpanding hematoma is a '
                                                          'soft-sign presentation, so CT angiography is obtained to '
                                                          'assess vessels and trajectory toward the aerodigestive '
                                                          'tract, combined with serial examinations. Findings on CTA '
                                                          'then direct observation, endoscopy, endovascular treatment, '
                                                          'or surgery.',
                                           'why_wrong': ['Correct.',
                                                         'Mandatory exploration of zone II wounds has been replaced by '
                                                         'selective CTA-based management in stable patients, avoiding '
                                                         'many negative explorations.',
                                                         'Probing can dislodge clot and provoke hemorrhage and cannot '
                                                         'reliably define injury to deep vessels or the aerodigestive '
                                                         'tract.',
                                                         'Platysma penetration with a hematoma requires evaluation for '
                                                         'vascular and aerodigestive injury before discharge.'],
                                           'board_pearl': 'Stable penetrating neck trauma without hard signs: '
                                                          'selective CTA and serial exams rather than mandatory zone '
                                                          'II exploration.',
                                           'curveball': 'His CTA is normal, but he reports pain on swallowing the next '
                                                        'morning. Does a negative CTA definitively exclude an '
                                                        'esophageal injury?',
                                           'curveball_answer': 'No. CTA can miss small pharyngoesophageal injuries. '
                                                               'When the trajectory approaches the esophagus, or there '
                                                               'is dysphagia, odynophagia, hematemesis, subcutaneous '
                                                               'or prevertebral air, or other CT changes, add '
                                                               'esophagoscopy, a contrast esophagram, or both, because '
                                                               'missed esophageal injuries cause mediastinitis and '
                                                               'deep neck infection.'},
 'v431-penetrating-blunt-neck-trauma-02': {'stem': 'A 31-year-old man arrives after a gunshot wound to the anterior '
                                                   'neck. He is speaking and has blood pressure 118/74. The trauma '
                                                   'attending asks the resident which single examination finding, if '
                                                   'found on the secondary survey, would mandate immediate operative '
                                                   'or endovascular management without first obtaining CT angiography. '
                                                   'Which finding would mandate this?',
                                           'choices': ['A small, stable hematoma at the wound',
                                                       'Mild dysphonia without stridor',
                                                       'Air bubbling from the wound with breathing',
                                                       'Subcutaneous emphysema near the wound'],
                                           'answer': 2,
                                           'explanation': 'Hard signs of neck injury mandate immediate operative or '
                                                          'endovascular management without routine imaging delay. They '
                                                          'include active arterial bleeding, expanding or pulsatile '
                                                          'hematoma, shock attributable to the neck injury, bruit or '
                                                          'thrill, major airway compromise, air bubbling from the '
                                                          'wound, and evolving focal neurologic deficit. Air bubbling '
                                                          'indicates a major airway injury. Soft signs, such as a '
                                                          'nonexpanding hematoma, dysphonia, dysphagia, minor '
                                                          'hemoptysis, or subcutaneous emphysema, instead prompt '
                                                          'selective CTA-based workup in stable patients.',
                                           'why_wrong': ['A small stable hematoma is a soft sign that prompts CT '
                                                         'angiography in a stable patient, not immediate exploration.',
                                                         'Dysphonia without stridor is a soft sign of laryngeal injury '
                                                         'and is evaluated with laryngoscopy and imaging.',
                                                         'Correct.',
                                                         'Subcutaneous emphysema is a soft sign of aerodigestive '
                                                         'injury that prompts CT and endoscopic evaluation.'],
                                           'board_pearl': 'Hard signs: active bleeding, expanding hematoma, shock, '
                                                          'bruit or thrill, airway compromise, bubbling wound, and '
                                                          'focal deficit.',
                                           'curveball': 'In blunt neck trauma, what injury must be screened for based '
                                                        'on mechanism and risk factors?',
                                           'curveball_answer': 'Blunt cerebrovascular injury, meaning carotid or '
                                                               'vertebral artery dissection, which can present hours '
                                                               'to days later with stroke. Screening CTA is indicated '
                                                               'for high-risk mechanisms or findings such as seatbelt '
                                                               'sign with neck injury, cervical spine fractures, '
                                                               'basilar skull fracture involving the carotid canal, Le '
                                                               'Fort II or III fractures, Horner syndrome, or '
                                                               'unexplained neurologic deficit.'},
 'v466_gent_necktrauma_fnd': {'stem': 'A 22-year-old man arrives 15 minutes after a stab wound to the right lateral '
                                      'neck. Bright red blood is pulsing from the wound, the surrounding hematoma is '
                                      'visibly enlarging, and blood pressure is 84/50 with heart rate 132. He is '
                                      'awake, follows commands, and has no stridor. Two large-bore IV lines are in '
                                      'place, and the trauma team is calling for blood. What is the most appropriate '
                                      'immediate step?',
                              'choices': ['CT angiography of the neck before any operative decision',
                                          'Direct pressure, airway control, and immediate operative control',
                                          'Bedside wound exploration to identify the bleeding vessel',
                                          'Blind clamping of the bleeding point deep within the wound'],
                              'answer': 1,
                              'explanation': 'Active arterial bleeding, an expanding hematoma, and shock are hard '
                                             'signs that mandate immediate operative or endovascular control without '
                                             'routine imaging. Direct digital pressure, or balloon tamponade, '
                                             'temporizes while blood products are given. The airway is secured early, '
                                             'before the hematoma distorts it, ideally in the operating room. Exposure '
                                             'is chosen by trajectory to obtain proximal and distal vascular control. '
                                             'The wound must not be probed or blindly clamped at the bedside.',
                              'why_wrong': ['Transporting an unstable, actively bleeding patient to the scanner delays '
                                            'hemorrhage control and risks arrest.',
                                            'Correct.',
                                            'Bedside exploration can dislodge clot, worsen bleeding, and does not '
                                            'achieve proximal and distal control.',
                                            'Blind clamping risks injury to the vagus, hypoglossal nerve, and adjacent '
                                            'vessels without achieving controlled repair.'],
                              'board_pearl': 'Hard signs of neck vascular injury: pressure, airway, and straight to '
                                             'the OR or hybrid suite without imaging delay.',
                              'curveball': 'The same patient instead has only a nonexpanding hematoma and mild '
                                           'dysphonia with stable vital signs. How does the initial step change?',
                              'curveball_answer': 'These are soft signs. In a stable patient, he would undergo CT '
                                                  'angiography of the neck to assess vascular injury and trajectory, '
                                                  'plus flexible laryngoscopy for the dysphonia and esophageal '
                                                  'evaluation if the tract approaches the pharynx or esophagus, with '
                                                  'serial examinations rather than mandatory operative exploration.'},
 'v466_gent_necktrauma_app': {'stem': 'A 28-year-old woman sustained a stab wound that crosses the midline neck '
                                      'between the cricoid and the angle of the mandible. She remains stable without '
                                      'hard signs, but she has coughed up streaks of blood and has palpable '
                                      'subcutaneous emphysema. CT angiography shows no vascular injury, with some air '
                                      'tracking along the tract toward the pharynx. What is the most appropriate next '
                                      'step?',
                              'choices': ['Discharge after 6 hours of observation because the CTA is negative',
                                          'Mandatory neck exploration based on the injury location alone',
                                          'Repeat CT angiography in 24 hours to look for delayed injury',
                                          'Endoscopic evaluation of the airway and esophagus for injury'],
                              'answer': 3,
                              'explanation': 'A negative CTA excludes significant vascular injury but not '
                                             'aerodigestive injury. Hemoptysis and subcutaneous emphysema are soft '
                                             'signs of laryngotracheal or pharyngoesophageal injury, and air tracking '
                                             'toward the pharynx on a transcervical trajectory increases concern. She '
                                             'needs laryngoscopy and bronchoscopy for the airway and esophagoscopy, '
                                             'with or without a contrast esophagram, for the esophagus, because missed '
                                             'esophageal injuries lead to deep neck infection and mediastinitis. '
                                             'Positive findings direct repair and drainage.',
                              'why_wrong': ['A negative CTA does not exclude esophageal or airway injury, and her soft '
                                            'signs and trajectory demand further evaluation.',
                                            'Location alone no longer mandates exploration in stable patients; '
                                            'targeted endoscopic evaluation identifies who needs surgery.',
                                            'Repeat CTA addresses vessels, which were already normal, and does not '
                                            'evaluate the aerodigestive tract.',
                                            'Correct.'],
                              'board_pearl': 'Negative CTA plus suspicious trajectory or aerodigestive soft signs: add '
                                             'esophagoscopy or esophagram and airway endoscopy.',
                              'curveball': 'What historical approach to zone II penetrating injuries has this '
                                           'selective strategy largely replaced?',
                              'curveball_answer': 'Mandatory operative exploration of every zone II wound that '
                                                  'penetrated the platysma, regardless of signs. It produced high '
                                                  'rates of negative explorations. Modern practice operates on hard '
                                                  'signs or unstable patients and uses CTA, endoscopy, and serial '
                                                  'examination to select stable patients for surgery.'},
 'v466_gent_necktrauma_snr': {'stem': 'A 35-year-old man struck his anterior neck on the steering wheel in a '
                                      'collision. He has worsening hoarseness, inspiratory stridor, hemoptysis, and '
                                      'palpable crepitus over a flattened thyroid cartilage, with oxygen saturation of '
                                      '93% sitting upright. Suspicion for laryngotracheal separation is high. The '
                                      'emergency physician wants to perform rapid-sequence intubation in the trauma '
                                      'bay. What is the safest airway plan?',
                              'choices': ['Awake tracheostomy under local anesthesia below the injury',
                                          'Rapid-sequence intubation in the trauma bay with videolaryngoscopy',
                                          'Delay all airway intervention until CT of the neck is completed',
                                          'Cricothyrotomy through the injured cricothyroid region as first step'],
                              'answer': 0,
                              'explanation': 'With suspected laryngotracheal separation, blind or rapid-sequence '
                                             'intubation can pass the tube into a false passage, complete a partial '
                                             'separation, or lose the distal trachea into the chest. The safest '
                                             'approach is a controlled airway in the operating room with expert '
                                             'surgical backup, typically awake tracheostomy under local anesthesia '
                                             'below the level of injury, while the patient keeps breathing '
                                             'spontaneously. Fiberoptic intubation by an expert is an alternative in '
                                             'selected patients. Laryngeal repair follows once the airway is secure.',
                              'why_wrong': ['Correct.',
                                            'Rapid-sequence intubation across a suspected separation risks a false '
                                            'passage, complete transection, and loss of the airway.',
                                            'With stridor and falling saturation, imaging must not delay securing the '
                                            'airway, which is the immediate threat.',
                                            'Cricothyrotomy places the airway through the injured larynx and can '
                                            'worsen the injury; access below it is safer.'],
                              'board_pearl': 'Suspected laryngotracheal separation: avoid reflexive intubation; secure '
                                             'the airway awake below the injury.',
                              'curveball': 'If this patient instead had a vascular injury with ongoing hemorrhage, how '
                                           'should operative exposure be chosen?',
                              'curveball_answer': 'Exposure is chosen by trajectory and injury location to obtain '
                                                  'proximal and distal vascular control, rather than simply enlarging '
                                                  'the contaminated wound. An incision along the anterior border of '
                                                  'the sternocleidomastoid exposes the carotid sheath, with sternotomy '
                                                  'or clavicular extension for low injuries and endovascular options '
                                                  'for high injuries near the skull base. Associated injuries are '
                                                  'repaired at the same time.'},
 'v431-ear-nasal-foreign-body-01': {'stem': 'A 2-year-old boy was found with a silver disc-shaped button battery in '
                                            'his right nostril about 1 hour ago. He has mild right nasal discharge and '
                                            'is crying and resisting examination. Anterior rhinoscopy shows the '
                                            'battery wedged against the septum in the anterior nasal cavity, with '
                                            'surrounding mucosal edema. He is breathing comfortably. What is the most '
                                            'appropriate management?',
                                    'choices': ['Saline irrigation of the nose to flush the battery toward the '
                                                'nasopharynx',
                                                'CT of the sinuses to localize the battery before any removal attempt',
                                                'Removal at the next available elective operating room slot',
                                                'Immediate removal without irrigation, under sedation if necessary'],
                                    'answer': 3,
                                    'explanation': 'A button battery in the nose is a tissue-destructive emergency. '
                                                   'Current through moist mucosa generates hydroxide, causing '
                                                   'liquefactive necrosis that can perforate the septum within hours, '
                                                   'and pressure adds injury. It must be removed immediately, with '
                                                   'irrigation avoided because fluid can increase current flow and '
                                                   'spread caustic material. Because he is uncooperative, controlled '
                                                   'endoscopic removal under sedation or general anesthesia is '
                                                   'appropriate. After removal, the mucosa is inspected and followed '
                                                   'for septal necrosis.',
                                    'why_wrong': ['Irrigation is avoided for batteries because fluid can enhance '
                                                  'electrical injury and risks aspiration of the battery or caustic '
                                                  'fluid.',
                                                  'The battery is visible on rhinoscopy, so imaging adds delay without '
                                                  'changing the need for immediate removal.',
                                                  'Elective scheduling allows necrosis and septal perforation to '
                                                  'develop within hours; removal must be immediate.',
                                                  'Correct.'],
                                    'board_pearl': 'Nasal or aural button battery: remove immediately, avoid '
                                                   'irrigation, and use sedation or anesthesia if needed.',
                                    'curveball': 'How does the approach differ for a live insect in the ear canal?',
                                    'curveball_answer': 'A live insect is first killed or immobilized with mineral oil '
                                                        'or lidocaine instilled into the canal, provided the tympanic '
                                                        'membrane is believed intact, to stop movement and pain and '
                                                        'prevent canal or eardrum injury. It is then removed with '
                                                        'forceps or suction under the microscope. A battery, in '
                                                        'contrast, is removed immediately without instilling any '
                                                        'fluid.'},
 'v431-ear-nasal-foreign-body-02': {'stem': 'A 5-year-old girl pushed a smooth, round plastic bead into her right ear '
                                            'canal yesterday. She has a tympanostomy tube in that ear placed 6 months '
                                            'ago. She is cooperative and sits still for the microscope. The bead is '
                                            'lodged in the lateral bony canal, filling most of the lumen, and the '
                                            'tympanic membrane cannot be seen behind it. Which removal technique is '
                                            'most appropriate?',
                                    'choices': ['Grasp the bead with alligator forceps under the microscope',
                                                'Pass a right-angle hook behind the bead and roll it outward',
                                                'Roll the bead out with a cotton-tipped applicator',
                                                'Irrigate the canal with body-temperature water'],
                                    'answer': 1,
                                    'explanation': "The tool should match the object's shape and material. Smooth, "
                                                   'round objects cannot be grasped securely, so forceps tend to push '
                                                   'them deeper toward the tympanic membrane. A right-angle hook or '
                                                   'curette is passed beyond the object under the microscope and '
                                                   'rotated behind it to roll it outward; suction can also work for '
                                                   'some smooth objects. Irrigation is avoided here because she has a '
                                                   'tympanostomy tube, and the membrane cannot be confirmed intact. '
                                                   'The safest first attempt is the best attempt.',
                                    'why_wrong': ['Forceps slip off smooth, round objects and push them medially '
                                                  'toward the eardrum and ossicles.',
                                                  'Correct.',
                                                  'A cotton-tipped applicator acts like a plunger and pushes the bead '
                                                  'deeper toward the tympanic membrane.',
                                                  'Irrigation is contraindicated with a tympanostomy tube in place '
                                                  'because water would enter the middle ear.'],
                                    'board_pearl': 'Choose the tool by shape: forceps for graspable objects, hook or '
                                                   'curette behind smooth round ones.',
                                    'curveball': 'The bead comes out intact on the first pass. What should be done '
                                                 'before she leaves the clinic?',
                                    'curveball_answer': 'Re-examine the canal and tympanic membrane under the '
                                                        'microscope for abrasions, bleeding, retained fragments, tube '
                                                        'displacement, or perforation, since removal attempts can '
                                                        'cause trauma. Canal abrasions may be treated with '
                                                        'antibiotic-steroid drops. Any perforation or hearing concern '
                                                        'prompts audiometry and follow-up.'},
 'v466_gent_fb_fnd': {'stem': 'A 4-year-old boy has had 2 weeks of foul-smelling discharge from the left nostril only. '
                              'His mother suspects he put something in his nose. Anterior rhinoscopy after topical '
                              'decongestion shows a crumpled wad of paper with irregular edges in the anterior left '
                              "nasal cavity, surrounded by purulent secretions. He is calm in his mother's lap and "
                              'allows examination. What is the best first removal attempt?',
                      'choices': ['Saline irrigation to flush the wad toward the nasopharynx',
                                  'Blind sweeping with a cotton-tipped applicator',
                                  'Alligator forceps grasp under direct vision with a headlight',
                                  'CT of the sinuses before any attempt at removal'],
                      'answer': 2,
                      'explanation': 'Unilateral foul rhinorrhea in a child suggests a retained nasal foreign body. '
                                     'The safest first attempt is the best attempt: with good lighting, decongestion, '
                                     "a cooperative child, and positioning, the instrument is chosen by the object's "
                                     'geometry. A soft, irregular paper wad is easily grasped, so alligator or bayonet '
                                     'forceps under direct vision is ideal. Hooks or curettes suit smooth round '
                                     'objects, and positive pressure techniques suit selected anterior objects. '
                                     'Repeated failed attempts reduce cooperation and push objects deeper.',
                      'why_wrong': ['Irrigation causes organic or absorbent material like paper to swell and risks '
                                    'pushing it posteriorly with aspiration.',
                                    'Blind sweeping pushes material deeper and traumatizes mucosa without direct '
                                    'control of the object.',
                                    'Correct.',
                                    'Imaging is unnecessary when the object is visible on rhinoscopy and would only '
                                    'delay a straightforward removal.'],
                      'board_pearl': 'The safest first attempt is the best attempt: good light, decongestion, and a '
                                     "tool chosen for the object's shape.",
                      'curveball': 'What single feature of the object, if present, would change this from a routine '
                                   'removal into an emergency?',
                      'curveball_answer': 'A button battery, or paired magnets clamped across the septum, makes it an '
                                          'emergency. Batteries cause electrochemical liquefactive necrosis within '
                                          'hours and magnets cause pressure necrosis, both risking septal perforation. '
                                          'They must be removed immediately rather than in an unhurried routine '
                                          'visit.'},
 'v466_gent_fb_app': {'stem': 'A 3-year-old girl is seen in clinic with 1 day of right nasal discharge. Anterior '
                              'rhinoscopy shows a small silver disc in the right nasal vestibule against the septum, '
                              'which her parents confirm is a button battery from a toy. She is otherwise well and '
                              'breathing normally. The parents ask whether removal can be scheduled for later this '
                              'week, since she is not bothered. What is the correct response?',
                      'choices': ['Schedule elective removal later this week since she has no symptoms',
                                  'Observe with nasal saline sprays, since many nasal objects pass alone',
                                  'Remove it today without delay, because tissue injury progresses in hours',
                                  'Topical antibiotic ointment now, with a recheck visit in 48 hours'],
                      'answer': 2,
                      'explanation': 'A button battery in the nasal cavity is a tissue-destructive emergency '
                                     'regardless of symptoms. The battery generates hydroxide through current flow in '
                                     'moist mucosa, causing liquefactive necrosis that can begin within hours and lead '
                                     'to septal perforation, synechiae, and saddle deformity. After a day in place, '
                                     'injury is likely already under way. It must be removed immediately, under '
                                     'sedation if needed, without irrigation, followed by inspection and follow-up of '
                                     'the septum.',
                      'why_wrong': ['Absence of symptoms does not reflect tissue injury, which progresses within hours '
                                    'to septal necrosis and perforation.',
                                    'Nasal batteries rarely pass on their own, and saline sprays add fluid that can '
                                    'worsen electrical injury.',
                                    'Correct.',
                                    'Ointment does not stop electrochemical injury, and a 48-hour delay allows septal '
                                    'necrosis to progress.'],
                      'board_pearl': 'A nasal button battery is removed immediately regardless of symptoms; irrigation '
                                     'and delay are avoided.',
                      'curveball': 'If the object were a dried bean rather than a battery, would irrigation be an '
                                   'appropriate technique?',
                      'curveball_answer': 'No. Organic material such as beans and seeds absorbs water and swells, '
                                          'making it more impacted and harder to remove, so irrigation is avoided. '
                                          'Irrigation is also avoided with suspected tympanic membrane perforation in '
                                          'ear cases. A bean is usually removed with a hook or curette behind it, '
                                          'suction, or positive pressure.'},
 'v466_gent_fb_snr': {'stem': 'A 3-year-old boy has a small pebble deep in the right ear canal, abutting the tympanic '
                              'membrane. Two bedside attempts with forceps at an urgent care center failed, the canal '
                              'is abraded and bleeding, and he now screams and fights any examination. The pebble is '
                              'not a battery or magnet. He has no vertigo or facial weakness. What is the most '
                              'appropriate next step?',
                      'choices': ['A third bedside attempt with a papoose restraint and forceps',
                                  'Cerumenolytic drops overnight, then retry with canal irrigation',
                                  'Ciprofloxacin drops and recheck in clinic in 2 weeks',
                                  'Microscopic removal under general anesthesia at the next opportunity'],
                      'answer': 3,
                      'explanation': 'Deep or impacted objects, poor cooperation, proximity to the tympanic membrane, '
                                     'and failed prior attempts each call for controlled microscopic removal under '
                                     'sedation or general anesthesia. Further bedside attempts on a struggling child '
                                     'risk tympanic membrane perforation, ossicular injury, and more canal trauma. '
                                     'Under anesthesia the object can be removed with appropriate instruments, and the '
                                     'canal and eardrum inspected. Because it is inert, this can be done at the next '
                                     'available opportunity rather than emergently.',
                      'why_wrong': ['Restraint and repeated forceps attempts in a fighting child risk eardrum '
                                    'perforation and ossicular injury next to the membrane.',
                                    'Irrigation is unsafe when the eardrum may be injured after traumatic attempts, '
                                    'and it may drive the pebble medially.',
                                    'Delaying removal does not make it easier and leaves an impacted object against '
                                    'the eardrum in an abraded canal.',
                                    'Correct.'],
                      'board_pearl': 'Deep, impacted, or failed-attempt aural foreign bodies in uncooperative '
                                     'children: remove under the microscope with anesthesia.',
                      'curveball': 'After removal under anesthesia, what should be done before considering the case '
                                   'complete?',
                      'curveball_answer': 'Inspect the entire canal and tympanic membrane under the microscope for '
                                          'perforation, ossicular exposure, retained fragments, or a second object, '
                                          'and clean blood and debris. Treat canal abrasions with topical drops. Any '
                                          'perforation or concern for middle ear injury warrants audiometry and '
                                          'follow-up to confirm healing.'}}
