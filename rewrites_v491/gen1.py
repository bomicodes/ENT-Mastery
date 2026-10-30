# v491 rewrites: General ENT / Emergencies part 1
REWRITES = {
    'v11_gen_01': {'stem': 'A 42-year-old man with a 4-day toothache from a carious left mandibular molar presents with fever of 38.9 C, firm bilateral submandibular and submental swelling, an elevated tongue, a '
             'muffled voice, and drooling. He prefers to sit upright. Oxygen saturation is 96% on room air, there is no fluctuance, and the white count is 19,000. What is the first management priority?',
     'choices': ['Airway assessment and a controlled airway plan with IV antibiotics started in parallel',
                 'Contrast CT of the neck to identify a drainable collection before any airway decision',
                 'Bilateral transcervical incision and drainage of the submandibular spaces under local anesthesia',
                 'Extraction of the offending molar in the dental chair to remove the infectious source'],
     'answer': 0,
     'explanation': 'Bilateral submandibular and sublingual involvement with tongue elevation, drooling, and a muffled voice defines Ludwig angina, a rapidly spreading odontogenic cellulitis that pushes '
                    'the tongue up and back. Airway loss can occur without any abscess, so the first priority is an experienced airway assessment and a controlled plan, often awake fiberoptic intubation '
                    'or awake tracheostomy, while IV antibiotics covering streptococci and oral anaerobes start immediately. Imaging, drainage of any collection, and dental source control follow once '
                    'the airway is safe.',
     'why_wrong': ['Correct.',
                   'Lying a drooling patient with tongue elevation supine in the scanner risks sudden obstruction; the airway plan comes before nonessential imaging.',
                   'There is no fluctuance, and drainage is not the first step while the airway is threatened; cellulitis alone does not mandate bilateral incision.',
                   'Source control matters but follows airway security; an office extraction with a threatened airway and limited mouth opening is unsafe.'],
     'board_pearl': 'Ludwig angina is an airway emergency first; obstruction can occur before any abscess forms.',
     'curveball': 'The floor of mouth is worsening and he cannot lie flat. Anesthesia proposes rapid-sequence induction with direct laryngoscopy. What approach is safer?',
     'curveball_answer': 'Avoid induction and paralysis, which remove the muscle tone holding the airway open and can turn partial obstruction into complete obstruction with failed mask ventilation. '
                         'Secure the airway awake with spontaneous ventilation, typically awake fiberoptic nasotracheal intubation in the OR with the neck prepped and a surgeon ready. If trismus and '
                         'floor-of-mouth swelling make intubation unsafe, perform awake tracheostomy under local anesthesia.'},
    'v116-gen-02': {'stem': 'A 35-year-old woman had a lower right molar extracted 5 days ago for a dental abscess. She now has fever, rapidly progressive firm swelling under both sides of the jaw, a raised woody '
             'floor of mouth, drooling, and a muffled voice. There is no fluctuance and no eye or chest symptoms. Oxygen saturation is 97% on room air. What is the most immediate concern?',
     'choices': ['Descending mediastinitis through the retropharyngeal and danger spaces into the chest',
                 'Upper airway obstruction from upward and posterior displacement of the tongue',
                 'Septic thrombophlebitis of the internal jugular vein with pulmonary emboli',
                 'Cavernous sinus thrombosis through the valveless facial venous system'],
     'answer': 1,
     'explanation': 'Firm bilateral submandibular swelling with a woody, raised floor of mouth after a mandibular dental infection is Ludwig angina. Infection spreads through the sublingual and '
                    'submandibular spaces around the posterior border of the mylohyoid, and the swollen sublingual tissue pushes the tongue upward and backward against the palate and pharyngeal wall. '
                    'Drooling and a muffled voice show the oral airway is already narrowing, so impending obstruction is the immediate threat even without fluctuance or hypoxemia.',
     'why_wrong': ['Mediastinal extension is a serious later risk, but nothing suggests chest involvement, while the floor-of-mouth findings threaten the airway now.',
                   'Correct.',
                   'Jugular thrombophlebitis follows pharyngeal or lateral neck infection and presents with neck tenderness and septic emboli, not tongue elevation.',
                   'Cavernous sinus thrombosis follows midface or maxillary infection and causes eye findings, which this mandibular infection lacks.'],
     'board_pearl': 'In Ludwig angina, the elevated, posteriorly displaced tongue is what obstructs the airway.',
     'curveball': 'Why is direct laryngoscopy after induction especially hazardous in this patient, and what airway options should be ready?',
     'curveball_answer': 'The woody floor of mouth is noncompliant, so the laryngoscope blade cannot displace the tongue into the submandibular space and the glottis may not be seen. After paralysis, '
                         'mask ventilation may also fail. Plan awake fiberoptic nasotracheal intubation with spontaneous ventilation, a surgeon at the bedside, and the neck prepped, with awake '
                         'tracheostomy or cricothyrotomy ready as the rescue.'},
    'v271_gen_lud_fnd': {'stem': 'A 50-year-old man with poor dentition and diabetes has 3 days of fever and neck swelling. Examination shows tender, firm, nonfluctuant swelling across both submandibular regions and the '
             'submental area, a raised floor of mouth, and a tongue pushed against the palate. The tonsils are symmetric and the uvula is midline. His voice is thick. Which diagnosis best explains these '
             'findings?',
     'choices': ['Peritonsillar abscess with spread into the adjacent lateral parapharyngeal space',
                 'Acute suppurative submandibular sialadenitis from an obstructing calculus',
                 'Ludwig angina involving the sublingual and submandibular spaces bilaterally',
                 'Retropharyngeal abscess from suppurative retropharyngeal lymph nodes'],
     'answer': 2,
     'explanation': 'Ludwig angina is a bilateral cellulitis of the submandibular space, including its sublingual and submaxillary compartments, usually from a lower molar whose roots lie below the '
                    'mylohyoid line. The defining exam is firm, brawny, nonfluctuant bilateral swelling with a raised floor of mouth and an elevated, posteriorly displaced tongue. Symmetric tonsils and '
                    'a midline uvula argue against peritonsillar disease. Recognizing the pattern matters because the main danger is rapid airway obstruction, which can occur before any abscess forms.',
     'why_wrong': ['Peritonsillar abscess causes unilateral palatal bulging and uvular deviation, and this patient has symmetric tonsils with a midline uvula.',
                   'Sialadenitis usually causes unilateral gland swelling with pus at Wharton duct, not bilateral woody swelling with tongue elevation.',
                   'Correct.',
                   'Retropharyngeal abscess bulges the posterior pharyngeal wall and stiffens the neck, and it is more typical in young children.'],
     'board_pearl': 'Second and third mandibular molar roots lie below the mylohyoid line and seed the submandibular space.',
     'curveball': 'Which bedside findings should make you secure his airway before sending him for CT?',
     'curveball_answer': 'Stridor, drooling or inability to handle secretions, upright or tripod positioning with intolerance of lying flat, rapidly progressive tongue elevation, voice change, rising '
                         'work of breathing, and agitation or hypoxemia all signal a precarious airway. Any of these means the airway should be secured in a controlled setting first, because lying '
                         'supine in the scanner can precipitate complete obstruction.'},
    'v271_gen_lud_app': {'stem': 'A 46-year-old woman with Ludwig angina from an infected lower molar has worsened over 6 hours despite IV ampicillin-sulbactam. She is sitting bolt upright, drooling, with a muffled voice '
             'and increased work of breathing. Mouth opening is 2.5 cm. Oxygen saturation is 95% while upright. CT has not yet been done. What is the best next step?',
     'choices': ['Contrast CT of the neck and chest first to plan drainage of all spaces',
                 'Rapid-sequence induction with video laryngoscopy in the emergency department',
                 'IV dexamethasone and heliox with close observation in the intensive care unit',
                 'Awake fiberoptic intubation in the OR with surgical airway backup ready'],
     'answer': 3,
     'explanation': 'Drooling, positional intolerance, and rising work of breathing despite antibiotics show that this airway is deteriorating; normal saturation is a late sign and offers little '
                    'reassurance. The safest approach preserves spontaneous ventilation: awake fiberoptic intubation, usually nasal, in the OR by an experienced team with the neck prepped and a surgeon '
                    'ready for awake tracheostomy or cricothyrotomy. Sedation, induction, and supine transport are avoided until the airway is controlled. Antibiotics continue, and imaging and source '
                    'control follow.',
     'why_wrong': ['Lying supine for CT with this degree of obstruction risks complete airway loss; imaging can follow once the airway is secured.',
                   'Induction and paralysis can abolish the tone holding the airway open, and video laryngoscopy may still fail with a rigid floor of mouth.',
                   'Steroids and heliox may temporize mild cases but do not address progressive obstruction in a patient already drooling and working to breathe.',
                   'Correct.'],
     'board_pearl': 'In Ludwig angina, saturation falls late; drooling and positional intolerance mean secure the airway now.',
     'curveball': 'What anatomy would push you toward awake tracheostomy rather than awake fiberoptic intubation in this patient?',
     'curveball_answer': 'Severe trismus, a massively elevated tongue filling the oral cavity, marked supraglottic or laryngeal edema on nasal endoscopy, pus or bleeding in the airway, or a failed '
                         'fiberoptic attempt favor awake tracheostomy under local anesthesia. Anterior neck swelling makes tracheostomy harder, so the decision is best made early and jointly by the '
                         'airway and surgical teams.'},
    'v271_gen_lud_snr': {'stem': 'A 55-year-old man with Ludwig angina was intubated awake fiberoptically 12 hours ago and is on IV ampicillin-sulbactam. Contrast CT now shows a 3 cm rim-enhancing collection in the right '
             'submandibular space, cellulitis without a collection in the left sublingual space, and periapical lucency around the right mandibular second molar. His fever persists. What is the best '
             'definitive management?',
     'choices': ['Incision and drainage of the collection with extraction of the infected molar',
                 'Continue IV antibiotics alone and repeat CT in 72 hours if fever persists',
                 'Bilateral transcervical exploration of all deep neck spaces plus tracheostomy',
                 'Ultrasound-guided needle aspiration of the collection without dental treatment'],
     'answer': 0,
     'explanation': 'Securing the airway buys time but does not treat the infection. Definitive care has two parts: drain any organized collection, here the rim-enhancing right submandibular abscess, '
                    'and remove the odontogenic source, the infected molar. Pus is sent for culture so the empiric regimen covering streptococci and oral anaerobes can be adjusted. Cellulitic spaces '
                    'without a collection, such as the left sublingual space, can be followed clinically. An undrained collection or retained tooth predicts ongoing sepsis and spread.',
     'why_wrong': ['Correct.',
                   'An organized rim-enhancing collection with persistent fever is an indication for drainage; antibiotics alone rarely clear it.',
                   'The left side is cellulitis without a collection, so routine exploration of every space adds morbidity without clear benefit.',
                   'Aspiration can help some small collections, but leaving the infected tooth allows persistent seeding and recurrence.'],
     'board_pearl': 'Ludwig angina definitive care: airway, IV antibiotics, drainage of collections, and extraction of the causative tooth.',
     'curveball': 'How would CT extension into the parapharyngeal space or the mediastinum change operative planning?',
     'curveball_answer': 'Parapharyngeal extension calls for transcervical drainage of that space with attention to the carotid sheath, often with a planned tracheostomy. Superior mediastinal '
                         'collections above the carina can sometimes be drained through the neck, but extension below the carina signals descending necrotizing mediastinitis and needs thoracic surgery '
                         'for mediastinal drainage, followed by repeat imaging to confirm control.'},
    'v11_gen_02': {'stem': 'A 24-year-old man has 5 days of worsening left-sided sore throat, now with left otalgia, mouth opening limited to 2 cm, a muffled voice, and drooling. Temperature is 38.6 C. Examination '
             'shows bulging of the left soft palate above the tonsil with the uvula deviated to the right. The neck is supple, with tender left jugulodigastric nodes. What is the most likely diagnosis?',
     'choices': ['Left peritonsillar cellulitis', 'Left peritonsillar abscess', 'Left parapharyngeal abscess', 'Mononucleosis tonsillitis'],
     'answer': 1,
     'explanation': 'Peritonsillar abscess forms between the tonsillar capsule and the superior constrictor, usually at the superior pole. Spread of inflammation to the medial pterygoid causes trismus, '
                    'and the mass pushes the soft palate forward and the uvula to the opposite side, producing the hot-potato voice. Unilateral pain, referred otalgia, trismus, and contralateral uvular '
                    'deviation in a young adult make this a clinical diagnosis. Needle aspiration confirms pus and is also therapeutic; CT is reserved for atypical findings or concern for deeper spread.',
     'why_wrong': ['Cellulitis can cause similar pain, but marked trismus, uvular deviation, and focal palatal bulging favor a collection; aspiration distinguishes them.',
                   'Correct.',
                   'Parapharyngeal abscess displaces the lateral pharyngeal wall medially and causes swelling below the mandibular angle, which are absent here.',
                   'Mononucleosis causes bilateral exudative tonsillar enlargement with diffuse adenopathy, not unilateral palatal bulging with uvular deviation.'],
     'board_pearl': 'Trismus plus contralateral uvular deviation separates peritonsillar abscess from cellulitis or simple tonsillitis.',
     'curveball': 'He becomes toxic with swelling extending below the angle of the mandible. What alternative diagnosis must you consider, and when is CT needed?',
     'curveball_answer': 'External swelling below the mandibular angle, toxicity, or neck stiffness suggests spread to the parapharyngeal or retropharyngeal space. Obtain contrast-enhanced neck CT once '
                         'the airway is judged stable, and also for failed aspiration, trismus preventing adequate examination, or an uncooperative child. Deeper collections usually need transcervical '
                         'or operative drainage rather than office aspiration.'},
    'v143_gen_04': {'stem': 'A 29-year-old woman has 4 days of right throat pain, trismus, and a muffled voice. She is handling secretions, has no stridor, and is otherwise healthy with no drug allergies. The right '
             'superior tonsillar pole is fluctuant, and the uvula is deviated to the left. This is her first episode, and she has had only one sore throat in the past year. What is the best management?',
     'choices': ['Contrast CT of the neck before deciding whether to drain the collection',
                 'Quinsy tonsillectomy under general anesthesia during this admission',
                 'Needle aspiration or incision with oral flora antibiotics and analgesia',
                 'IV antibiotics and steroids for 48 hours, draining only if no response'],
     'answer': 2,
     'explanation': 'A stable patient with classic peritonsillar abscess is managed with drainage, by needle aspiration or incision and drainage, which have similar success, plus antibiotics covering '
                    'streptococci and oral anaerobes, such as amoxicillin-clavulanate or clindamycin, with analgesia and hydration. Most patients who tolerate oral intake can be managed as outpatients. '
                    'Imaging is for atypical cases or suspected deep spread, and tonsillectomy is reserved for recurrent abscess or a history that meets criteria for recurrent tonsillitis.',
     'why_wrong': ['A classic, uncomplicated presentation is a clinical diagnosis; CT adds radiation and delay unless anatomy or deeper spread is uncertain.',
                   'Immediate tonsillectomy is reserved for selected patients, such as those with prior abscess or recurrent tonsillitis, and she has neither.',
                   'Correct.',
                   'A fluctuant collection needs drainage now; antibiotics alone suit peritonsillar cellulitis, not an established abscess.'],
     'board_pearl': 'Uncomplicated PTA: drain, cover oral flora, and reserve tonsillectomy for recurrence or recurrent tonsillitis.',
     'curveball': 'What history would make acute or interval tonsillectomy more reasonable for her?',
     'curveball_answer': 'A prior peritonsillar abscess, a history meeting recurrent tonsillitis criteria (7 episodes in 1 year, 5 per year for 2 years, or 3 per year for 3 years), failure of drainage, '
                         'or obstructive tonsillar hypertrophy all favor tonsillectomy. Quinsy tonsillectomy is also useful in a child who would need general anesthesia for drainage anyway.'},
    'v269_gen_pta_fnd': {'stem': 'A 21-year-old college student has 3 days of sore throat and fever to 38.5 C. Both tonsils are enlarged and erythematous with exudate, and she has tender anterior cervical nodes and painful '
             'swallowing. The resident is deciding between exudative tonsillitis and an evolving peritonsillar abscess. Which additional finding would most strongly support peritonsillar abscess?',
     'choices': ['Bilateral posterior cervical adenopathy with palpable splenomegaly',
                 'Tonsillar exudate with fever and absence of cough on presentation',
                 'Severe odynophagia with dehydration and inability to take solids',
                 'Trismus with asymmetric soft palate fullness and uvular deviation'],
     'answer': 3,
     'explanation': 'Peritonsillar abscess is a unilateral process. The collection pushes the superior tonsil and soft palate medially and forward, deviating the uvula away from the affected side, and '
                    'inflammation of the adjacent medial pterygoid produces trismus. A muffled voice and ipsilateral otalgia commonly accompany it. Bilateral findings, systemic features of '
                    'mononucleosis, or Centor criteria describe tonsillitis. When asymmetry and trismus appear, aspiration of the superior pole confirms the diagnosis and treats it.',
     'why_wrong': ['Posterior cervical nodes and splenomegaly point to infectious mononucleosis, a bilateral process, rather than a unilateral collection.',
                   'Exudate, fever, and no cough are Centor criteria that support streptococcal tonsillitis but do not indicate an abscess.',
                   'Severe odynophagia and dehydration occur with both tonsillitis and abscess, so they do not discriminate between the two.',
                   'Correct.'],
     'board_pearl': 'Unilateral palatal bulge, uvular deviation, and trismus signal peritonsillar abscess rather than tonsillitis.',
     'curveball': 'Which exam features should make you worry about parapharyngeal spread or airway compromise in this patient?',
     'curveball_answer': 'Swelling or tenderness below the mandibular angle, neck stiffness or torticollis, medial bulging of the lateral pharyngeal wall behind the tonsil, trismus out of proportion to '
                         'the tonsillar findings, stridor, drooling, and a toxic appearance suggest deeper spread or airway threat. These findings call for airway assessment with flexible laryngoscopy '
                         'and contrast CT once she is stable.'},
    'v269_gen_pta_snr': {'stem': 'A 33-year-old man referred for a presumed peritonsillar abscess has 6 days of right throat pain, fever to 39.4 C, and severe trismus. He appears toxic, holds his neck stiffly, and has '
             'tender induration below the right mandibular angle. The right lateral pharyngeal wall bulges medially, but the superior tonsillar pole is not fluctuant. He is breathing comfortably. What '
             'is the best next step?',
     'choices': ['Contrast CT of the neck after airway assessment with flexible laryngoscopy',
                 'Repeated needle aspiration at the superior, middle, and inferior tonsil poles',
                 'Incision and drainage of the superior pole followed by oral antibiotics',
                 'Discharge on oral clindamycin with reexamination in clinic in 24 hours'],
     'answer': 0,
     'explanation': 'Toxicity, neck stiffness, induration below the mandibular angle, and medial bulging of the lateral pharyngeal wall are not features of routine peritonsillar abscess. They suggest '
                    'parapharyngeal or retropharyngeal extension, which can threaten the airway, the carotid sheath, and the mediastinum. The airway is assessed first, often with flexible laryngoscopy, '
                    'and if it is stable, contrast CT defines the involved spaces and their relation to the great vessels. Treatment then includes IV antibiotics and drainage planned to the anatomy, '
                    'often transcervical.',
     'why_wrong': ['Correct.',
                   'Repeated blind passes risk carotid injury when the collection may lie lateral to the constrictor in the parapharyngeal space.',
                   'Superior-pole incision treats a peritonsillar collection, but the neck induration and lateral wall bulge point to a deeper space.',
                   'A toxic patient with neck induration and possible deep-space spread needs admission, IV antibiotics, and imaging, not outpatient therapy.'],
     'board_pearl': 'Neck swelling below the mandibular angle in a presumed PTA means deep-space spread until CT shows otherwise.',
     'curveball': 'What CT finding would push you toward transcervical rather than transoral drainage?',
     'curveball_answer': 'A collection lateral to the great vessels or in the poststyloid parapharyngeal space, carotid sheath involvement, multiloculated or multispace abscesses, inferior extension '
                         'toward the hyoid or mediastinum, or a collection not safely reachable through the pharyngeal wall favors transcervical drainage. Small prestyloid collections lying medial to '
                         'the great vessels may be drained transorally.'},
    'v11_gen_03': {'stem': 'A 58-year-old woman is 5 hours out from total thyroidectomy for multinodular goiter. The nurse notes rapidly increasing neck swelling under the dressing. The patient is anxious, says her '
             'neck feels tight, and has new inspiratory stridor. Oxygen saturation is 93% on face mask. The drain contains only 20 mL. What is the most appropriate immediate management?',
     'choices': ['Bedside neck ultrasound to confirm a hematoma before reopening the neck wound',
                 'Open the incision at the bedside to evacuate clot, then return to the OR',
                 'Nebulized racemic epinephrine and IV dexamethasone for laryngeal edema',
                 'Rapid-sequence intubation on the ward with standard direct laryngoscopy'],
     'answer': 1,
     'explanation': 'Rapid swelling, tightness, and stridor after thyroidectomy indicate a compressive hematoma, and low drain output does not exclude it because drains clot. The hematoma compresses '
                    'thin-walled veins and lymphatics, causing laryngeal and pharyngeal edema that narrows the airway faster than tracheal compression alone. Immediate bedside opening of the skin, '
                    'platysma, and strap closure evacuates clot and relieves pressure. The patient then returns to the OR for washout, hemostasis, and airway control as needed.',
     'why_wrong': ['This is a clinical diagnosis, and waiting for imaging allows progressive venous and lymphatic congestion of the larynx.',
                   'Correct.',
                   'The airway edema results from venous compression by the hematoma; medical therapy does not relieve the mechanical cause.',
                   'Laryngeal edema and tracheal deviation make intubation difficult; decompression first often restores the airway and improves the view.'],
     'board_pearl': 'A low drain output does not exclude a compressive hematoma; drains clot.',
     'curveball': 'She becomes more stridulous while the OR is being prepared. What bedside action should not be delayed while a definitive airway is organized?',
     'curveball_answer': 'Open the wound immediately at the bedside: cut the skin sutures or glue, open the platysma, and separate the strap muscles in the midline to release clot from the pretracheal '
                         'space. The SCOOP sequence (skin exposure, cut sutures, open skin, open muscles, pack) often relieves stridor within minutes. Pack the wound loosely with moist gauze and '
                         'transfer to the OR.'},
    'v135_gen_01': {'stem': 'A 44-year-old man is 2 hours out from right thyroid lobectomy. He reports neck pressure and difficulty swallowing his saliva, his voice is muffled, and inspiratory noise is increasing. The '
             'incision is tense and bulging. The anesthesiologist on call is 10 minutes away, and the OR is being prepared. What should the resident at the bedside do now?',
     'choices': ['Wait for the anesthesiologist so that intubation precedes any wound manipulation',
                 'Send him for urgent contrast CT of the neck to define the extent of the collection',
                 'Release the incision and strap muscles at the bedside to decompress the neck',
                 'Apply a firm compressive dressing over the incision to tamponade the bleeding'],
     'answer': 2,
     'explanation': 'An expanding, tense incision with secretion intolerance, voice change, and stridor after thyroid surgery means a hematoma is compressing the airway. Because venous and lymphatic '
                    'obstruction causes progressive laryngeal edema, decompression is time-critical and should be done by whoever is at the bedside, without waiting for imaging or the full team. Opening '
                    'the skin, platysma, and midline strap closure lets clot escape and usually improves breathing. Calling for help, the airway team, and return to the OR proceed in parallel.',
     'why_wrong': ['Every minute of compression worsens laryngeal edema; decompression should not wait for the full team when airway compromise is evolving.',
                   'Imaging delays treatment, requires lying supine, and is unnecessary for a clinical diagnosis with evolving airway symptoms.',
                   'Correct.',
                   'Compressing a closed neck space raises pressure on the airway and veins, worsening obstruction rather than stopping it.'],
     'board_pearl': 'Decompression of a compressive neck hematoma should not wait for imaging, transport, or a full team.',
     'curveball': 'After the incision is opened and clot evacuated, stridor persists. What additional airway problem may coexist, and how should it be evaluated?',
     'curveball_answer': 'Persistent stridor suggests established laryngeal and pharyngeal edema from venous congestion, or bilateral vocal fold immobility from recurrent laryngeal nerve injury. '
                         'Flexible laryngoscopy, if tolerated, distinguishes them. Edema often requires intubation by an experienced operator with a smaller tube and surgical backup, while bilateral '
                         'immobility may need intubation and later tracheostomy or a glottic airway procedure.'},
    'v153_tps_01': {'stem': 'A 39-year-old woman is 3 hours out from total thyroidectomy for Graves disease. She reports perioral tingling and neck tightness. Examination shows a tense, expanding swelling beneath the '
             'incision with ecchymosis, difficulty swallowing, and new stridor. Her ionized calcium was normal 1 hour ago. Help has been called. What should happen immediately?',
     'choices': ['Give IV calcium gluconate for presumed hypocalcemic laryngospasm and reassess',
                 'Perform flexible laryngoscopy to check vocal fold motion before intervening',
                 'Needle-aspirate the swelling through the incision to reduce its volume',
                 'Open the wound and evacuate the hematoma at the bedside while help arrives'],
     'answer': 3,
     'explanation': 'A tense, expanding swelling with ecchymosis, dysphagia, and stridor in the first hours after thyroidectomy is a compressive hematoma, the leading cause of airway compromise in this '
                    'window. Graves disease raises the bleeding risk. Symptomatic hypocalcemia typically appears 24 to 72 hours after surgery, and her ionized calcium was normal, so perioral tingling '
                    'does not explain the findings. The wound is opened through skin, platysma, and strap layers to release clot, while airway, surgical, and OR resources are mobilized for definitive '
                    'hemostasis.',
     'why_wrong': ['Hypocalcemia is unlikely at 3 hours with a normal ionized calcium, and it does not explain a tense, expanding neck swelling.',
                   'Laryngoscopy delays decompression and does not treat compression; it can follow once the hematoma is released.',
                   'Clotted blood does not aspirate through a needle, and partial decompression wastes time while laryngeal edema progresses.',
                   'Correct.'],
     'board_pearl': 'Early stridor with a tense neck after thyroidectomy is hematoma, not hypocalcemia; decompress first.',
     'curveball': 'Why can intubation remain difficult even after the hematoma itself is released?',
     'curveball_answer': 'Venous and lymphatic obstruction causes edema of the supraglottis, arytenoids, and pharynx that does not resolve immediately when the clot is removed. Combined with tracheal '
                         'deviation and blood in the airway, the glottic view may be poor. Plan for an experienced operator, video laryngoscopy or an awake fiberoptic technique, a smaller tube, and '
                         'front-of-neck access ready.'},
    'v269_gen_hemat_fnd': {'stem': 'A 62-year-old man is 4 hours out from a focused left inferior parathyroidectomy and is being considered for same-day discharge. His pain is controlled with oral analgesics, and the '
             'dressing is clean and dry. The nurse asks which change in his condition should prompt immediate bedside evaluation for a compressive neck hematoma. Which finding is most concerning?',
     'choices': ['New neck pressure with voice change, difficulty swallowing, and restlessness',
                 'Mild ecchymosis around the incision that has not enlarged over 2 hours',
                 'Nausea with one episode of emesis after his first oral analgesic dose',
                 'Incisional soreness that worsens with neck extension and head turning'],
     'answer': 0,
     'explanation': 'A cervical hematoma can compress the airway from deep to the strap muscles before the skin looks dramatically swollen. Early warning signs are subjective neck pressure or tightness, '
                    'voice change, dysphagia, and anxiety or restlessness, followed by stridor and respiratory distress. Most significant bleeds occur within the first 24 hours, many within 6 hours, '
                    'which is why same-day discharge pathways require an observation period and a patient and caregiver who can recognize these symptoms. Stable bruising and incisional pain are '
                    'expected.',
     'why_wrong': ['Correct.',
                   'Stable, nonexpanding bruising without pressure symptoms is common after neck surgery and does not indicate compression.',
                   'Postoperative nausea is common; retching raises venous pressure and bleeding risk, but alone it is not a sign of hematoma.',
                   'Positional incisional pain is expected and does not indicate deep compression without swelling, voice, or breathing changes.'],
     'board_pearl': 'Neck tightness, voice change, dysphagia, and restlessness can precede visible swelling in a compressive hematoma.',
     'curveball': 'Why does intubation become progressively harder the longer a compressive neck hematoma is left in place?',
     'curveball_answer': 'The hematoma compresses the jugular veins and cervical lymphatics, so the supraglottis, arytenoids, tongue base, and pharyngeal walls become progressively edematous, obscuring '
                         'the glottis and narrowing the airway. Because the edema worsens with time, the window for a straightforward intubation shrinks. Early decompression reverses the venous '
                         'obstruction, and any delayed intubation should be planned as a difficult airway.'},
    'v269_gen_hemat_snr': {'stem': 'A 66-year-old woman develops worsening stridor 90 minutes after total thyroidectomy at a community hospital at night. Her neck is visibly expanding, oxygen saturation has fallen to 86% on '
             'a nonrebreather mask, and she is becoming confused. The OR team is 30 minutes away. A senior resident is at the bedside with a suture removal kit. What is the best action?',
     'choices': ['Attempt awake fiberoptic nasal intubation under light sedation at the bedside',
                 'Cut the sutures and open skin, platysma, and straps to release the clot now',
                 'Place a needle cricothyrotomy and jet ventilate until the OR team arrives',
                 'Begin bag-mask ventilation and support oxygenation until the team arrives'],
     'answer': 1,
     'explanation': 'Falling saturation and confusion mean this hematoma is causing imminent airway loss. Bedside wound decompression is the lifesaving step: remove the skin closure, open the platysma, '
                    'and separate the strap muscles to release clot from the pretracheal space. This reduces pressure on the airway and veins and often improves ventilation at once. Definitive '
                    'hemostasis and airway management follow once pressure is relieved, but they should not delay decompression when the OR is not immediately available.',
     'why_wrong': ['Edema from venous congestion obscures the glottis, and sedation in a hypoxemic patient may precipitate complete obstruction before decompression.',
                   'Correct.',
                   'Needle cricothyrotomy through a hematoma-filled neck is difficult and does not relieve compression; it is a rescue if decompression fails.',
                   'Bag-mask ventilation may fail against external compression, and a 30-minute delay lets edema and hypoxemia worsen.'],
     'board_pearl': 'Hypoxemia from a post-thyroidectomy hematoma: decompress at the bedside first; hemostasis follows in the OR.',
     'curveball': 'Decompression is complete but ventilation does not improve. What parallel airway plan should already be underway?',
     'curveball_answer': 'Oxygenation continues by face mask or supraglottic device while the most experienced operator attempts intubation with video laryngoscopy and a smaller tube. If intubation '
                         'fails and oxygenation cannot be maintained, proceed to front-of-neck access, which is easier now that the trachea is exposed in the open wound; cricothyrotomy or direct '
                         'tracheal entry through the wound are both acceptable.'},
    'v11_gen_04': {'stem': 'A 67-year-old Black woman taking lisinopril for 3 years woke with lip swelling that has spread over 4 hours to the tongue and floor of mouth. She has no urticaria, itching, or wheezing. '
             'Her voice is thick, and she is spitting saliva. Blood pressure is 154/88 and oxygen saturation is 97% on room air. Which concern should drive the initial management?',
     'choices': ['Distributive shock from systemic mast cell mediator release',
                 'Bronchospasm from histamine-mediated lower airway inflammation',
                 'Progressive upper airway obstruction from tongue and laryngeal edema',
                 'Odontogenic floor-of-mouth cellulitis spreading to the deep neck spaces'],
     'answer': 2,
     'explanation': 'ACE inhibitors block breakdown of bradykinin, which increases vascular permeability and causes nonpitting submucosal edema of the lips, tongue, floor of mouth, and larynx. It can '
                    'occur after years of uneventful use and is more common in Black patients. Without urticaria or hypotension, mast cells are not the driver, so the dominant risk is mechanical upper '
                    'airway obstruction. Tongue and floor-of-mouth involvement, voice change, and drooling call for early flexible laryngoscopy and a controlled airway plan.',
     'why_wrong': ['Normal blood pressure and absent hives argue against anaphylaxis; ACE-inhibitor angioedema is bradykinin mediated and rarely causes shock.',
                   'She has no wheeze, and bradykinin-mediated angioedema affects the upper aerodigestive tract rather than the bronchi.',
                   'Correct.',
                   'Painless swelling of the lips and tongue over hours without fever or a dental source fits angioedema, not infection.'],
     'board_pearl': 'ACE-inhibitor angioedema can begin after years of therapy; tongue involvement and drooling predict airway risk.',
     'curveball': 'Why might epinephrine, antihistamines, and steroids be insufficient here, and what remains the overriding priority?',
     'curveball_answer': 'These drugs act on histamine and mast cell pathways, whereas ACE-inhibitor angioedema is driven by bradykinin, so response is unreliable. They are reasonable when the mechanism '
                         'is uncertain, but the priority is serial airway assessment with flexible laryngoscopy, ICU monitoring, permanent discontinuation of the ACE inhibitor, and early controlled '
                         'intubation if the larynx is involved or symptoms progress.'},
    'v140_gen_03': {'stem': 'A 59-year-old man taking enalapril has 3 hours of progressive tongue and floor-of-mouth swelling with a muffled voice, without hives or itching. He received IM epinephrine, IV '
             'diphenhydramine, and methylprednisolone 40 minutes ago without improvement. He is sitting upright, speaking in short phrases, with saturation of 96% on room air. What is the best next '
             'step?',
     'choices': ['Repeat IM epinephrine every 5 minutes and escalate only if stridor develops',
                 'Admit to a monitored floor bed with a plan to discontinue the enalapril',
                 'Obtain soft-tissue neck radiographs to grade the extent of laryngeal edema',
                 'Flexible laryngoscopy and early controlled airway planning with anesthesia'],
     'answer': 3,
     'explanation': 'Failure to respond to epinephrine, antihistamine, and steroid supports bradykinin-mediated ACE-inhibitor angioedema. The decision that matters is airway trajectory. Flexible '
                    'laryngoscopy shows whether the supraglottis, arytenoids, or larynx are involved, which predicts the need for intubation better than oxygen saturation. With progressive tongue '
                    'swelling and a muffled voice, the airway should be planned and, if needed, secured early under controlled conditions, usually by awake fiberoptic nasal intubation with a surgical '
                    'airway ready.',
     'why_wrong': ['Repeated epinephrine has limited effect on bradykinin-mediated swelling, and waiting for stridor lets the airway become harder to secure.',
                   'Stopping the drug is necessary but does not reverse current swelling; a progressing airway needs ICU-level monitoring and a plan.',
                   'Plain films do not reliably grade laryngeal edema; direct endoscopic assessment guides airway decisions.',
                   'Correct.'],
     'board_pearl': 'Angioedema not responding to epinephrine on an ACE inhibitor: scope the larynx and plan the airway early.',
     'curveball': 'Which anatomic sites on flexible laryngoscopy most strongly predict the need for airway intervention?',
     'curveball_answer': 'Laryngeal edema, especially of the arytenoids, aryepiglottic folds, epiglottis, and false folds, predicts the need for intubation, as does tongue base and floor-of-mouth '
                         'involvement with voice change. Isolated lip or facial swelling rarely needs intervention. The Ishoo staging captures this gradient: face and lip, soft palate, tongue, then '
                         'larynx, with the last two carrying the highest airway risk.'},
    'v272_gen_angio_fnd': {'stem': 'A 71-year-old woman who started ramipril 6 weeks ago has had 2 hours of asymmetric upper lip and tongue swelling. She has no urticaria, pruritus, or wheezing, and the swelling is '
             'nonpitting and painless. Her voice is clear, and flexible laryngoscopy shows a normal larynx. A tryptase level is pending. Which mechanism and management principle are most appropriate?',
     'choices': ['Bradykinin excess; stop the ACE inhibitor and monitor the airway closely',
                 'Mast cell degranulation; give antihistamines and switch her to an ARB now',
                 'C1 esterase inhibitor deficiency; begin danazol prophylaxis at discharge',
                 'IgE-mediated drug allergy; prescribe an epinephrine autoinjector and discharge'],
     'answer': 0,
     'explanation': 'ACE inhibition reduces breakdown of bradykinin, which acts on B2 receptors to increase vascular permeability, producing nonpitting edema without hives or itch. Because histamine is '
                    'not the mediator, antihistamines, steroids, and epinephrine are often ineffective, though they may be given when the mechanism is uncertain. Management is to stop the ACE inhibitor '
                    'permanently, avoid the class, and observe with serial airway checks; swelling usually resolves over 24 to 72 hours. Icatibant and C1 inhibitor concentrate have shown inconsistent '
                    'benefit in trials.',
     'why_wrong': ['Correct.',
                   'Absence of urticaria and pruritus argues against mast cell activation, and antihistamines do not reliably reverse bradykinin-mediated swelling.',
                   'Hereditary or acquired C1 inhibitor deficiency is possible, but a new ACE inhibitor is the likely cause, and long-term androgens are not a first step.',
                   'ACE-inhibitor angioedema is not IgE mediated, and discharge without observation is unsafe because swelling can progress to the larynx.'],
     'board_pearl': 'Angioedema without hives or itch on an ACE inhibitor is bradykinin mediated; stop the drug class permanently.',
     'curveball': 'Her cardiologist asks whether she can be switched to an angiotensin receptor blocker. How would you counsel?',
     'curveball_answer': 'ARBs do not directly block bradykinin breakdown, and recurrent angioedema on an ARB is uncommon, so most experts consider an ARB acceptable with counseling about a small '
                         'residual risk. Sacubitril-valsartan should be avoided because neprilysin inhibition also raises bradykinin. Swelling can recur for weeks after stopping the ACE inhibitor, which '
                         'does not by itself mean the ARB is responsible.'},
    'v272_gen_angio_app': {'stem': 'A 63-year-old man with ACE-inhibitor angioedema has had worsening tongue swelling over 5 hours. He now has a muffled voice, drooling, and increased work of breathing. Flexible laryngoscopy '
             'shows edematous arytenoids and aryepiglottic folds with a narrowed but visible glottis. Oxygen saturation is 98% on room air. What is the best next step?',
     'choices': ['ICU admission with hourly airway checks, intubating if saturation begins to fall',
                 'Awake fiberoptic nasal intubation in a controlled setting with surgical backup',
                 'Rapid-sequence induction with direct laryngoscopy in the emergency department',
                 'Nebulized racemic epinephrine with repeat flexible laryngoscopy in 2 hours'],
     'answer': 1,
     'explanation': 'Laryngeal involvement with drooling, voice change, and increasing work of breathing predicts the need for intubation, and normal saturation does not reassure. Securing the airway '
                    'while the patient is still oxygenating and cooperative allows a controlled awake technique, typically fiberoptic nasotracheal intubation with topical anesthesia and minimal '
                    'sedation, performed in the OR or ICU by an experienced operator with a surgeon ready for awake tracheostomy or cricothyrotomy. Waiting risks progression to complete obstruction.',
     'why_wrong': ['Saturation is a late marker in upper airway obstruction; waiting for desaturation turns a controlled intubation into a crash airway.',
                   'Correct.',
                   'Paralysis removes the tone keeping the swollen airway open, and a large tongue makes laryngoscopy and mask ventilation likely to fail.',
                   'Nebulized epinephrine has little effect on bradykinin-mediated edema, and a 2-hour delay risks losing the window for a controlled airway.'],
     'board_pearl': 'Symptomatic laryngeal edema in angioedema: intubate awake and early, before saturation falls.',
     'curveball': 'How would a known diagnosis of hereditary angioedema change disease-specific therapy while airway management proceeds?',
     'curveball_answer': 'Hereditary angioedema from C1 inhibitor deficiency responds to targeted on-demand therapy: plasma-derived or recombinant C1 inhibitor concentrate, icatibant (a bradykinin B2 '
                         'receptor antagonist), or ecallantide (a kallikrein inhibitor), with fresh frozen plasma as a fallback. These can halt progression within hours, but the airway is still secured '
                         'if laryngeal edema is already advanced.'},
    'v272_gen_angio_snr': {'stem': 'A 52-year-old woman with angioedema has worsening supraglottic edema despite 3 hours of medical therapy. Mouth opening is 1.5 cm, the tongue fills the oral cavity, and she is anxious but '
             'cooperative with saturation of 95%. The anesthesiologist suggests induction with paralysis to improve the view. You are asked for the airway plan. What is the best strategy?',
     'choices': ['Rapid-sequence induction with video laryngoscopy and a bougie as backup',
                 'Inhalational induction with sevoflurane, followed by direct laryngoscopy',
                 'Awake nasal fiberoptic intubation with the neck prepped for tracheostomy',
                 'Supraglottic airway after induction, then fiberoptic exchange for a tube'],
     'answer': 2,
     'explanation': 'The key decision is avoiding conversion of a spontaneously breathing patient into a cannot-intubate, cannot-oxygenate emergency. Limited mouth opening and a tongue filling the mouth '
                    'make oral approaches and rescue devices unreliable, so the nasal route with topical anesthesia and minimal sedation keeps her breathing while the airway is secured. The neck is '
                    'prepped and a surgeon is scrubbed so that tracheostomy or cricothyrotomy can follow immediately if the fiberoptic attempt fails.',
     'why_wrong': ['Paralysis abolishes spontaneous ventilation; if the tongue and supraglottis block the view, she may become impossible to ventilate.',
                   'Inhalational induction in a severely narrowed airway can cause obstruction and apnea, and limited mouth opening still prevents laryngoscopy.',
                   'Correct.',
                   'A supraglottic device needs adequate mouth opening and seals poorly over edematous tissue, so it is an unreliable rescue here.'],
     'board_pearl': 'In a swollen airway, keep the patient breathing: awake technique with front-of-neck access ready.',
     'curveball': 'When would an awake tracheostomy under local anesthesia be preferable to fiberoptic intubation for her?',
     'curveball_answer': 'Awake tracheostomy is preferred when massive supraglottic edema prevents visualization of the glottis, when nasal access is blocked or bleeding, when fiberoptic attempts have '
                         'failed, or when the team judges that any instrumentation risks complete obstruction. It is performed with the patient sitting up and breathing spontaneously under local '
                         'anesthesia, accepting added difficulty from neck swelling.'},
    'v11_gen_05': {'stem': 'A 28-year-old man intentionally swallowed several mouthfuls of liquid sodium hydroxide drain cleaner 3 hours ago. He has odynophagia and is drooling, but his voice is normal and there is '
             'no stridor. The oral cavity and oropharynx show only mild erythema without ulceration. Vital signs are normal, and the chest radiograph shows no free air. What is the best interpretation?',
     'choices': ['A normal water-soluble contrast swallow today would exclude significant injury',
                 'The mild oral findings make deep esophageal injury very unlikely in this patient',
                 'Drooling reflects oral pain alone and does not predict deeper esophageal injury',
                 'Significant esophageal injury remains likely despite the minimal oral findings'],
     'answer': 3,
     'explanation': 'Liquid alkali is swallowed rapidly, so contact time in the mouth is brief while the esophagus and stomach receive the bulk of the injury through liquefactive necrosis. Oral findings '
                    'therefore correlate poorly with deeper injury, and serious esophageal burns occur in patients with a normal-looking mouth. Symptoms such as drooling, odynophagia, dysphagia, and '
                    'vomiting, along with intentional large-volume ingestion, predict significant injury. He needs airway assessment and early upper endoscopy, usually within 12 to 24 hours, to grade '
                    'the injury.',
     'why_wrong': ['Contrast studies detect perforation but miss mucosal burns and ulceration, so a normal study does not grade injury depth.',
                   'Oral findings correlate poorly with esophageal and gastric injury; liquid alkali passes quickly and burns deeply downstream.',
                   'Drooling and odynophagia are symptoms that predict significant esophageal injury and warrant endoscopic evaluation.',
                   'Correct.'],
     'board_pearl': 'A normal mouth does not clear the esophagus after caustic ingestion; symptoms and intent drive endoscopy.',
     'curveball': 'His oropharynx looks nearly normal. What determines the timing of endoscopy, and when should it be avoided?',
     'curveball_answer': 'Endoscopy is best performed early, within about 12 to 24 hours and generally no later than 48 hours, before tissue softening in the healing phase raises perforation risk, which '
                         'is greatest roughly days 5 to 15. It is avoided with suspected perforation, hemodynamic instability, or an unsecured compromised airway; CT is used in those patients and '
                         'increasingly to detect transmural necrosis.'},
    'v143_gen_01': {'stem': 'A 36-year-old woman is brought in 1 hour after drinking an alkaline oven cleaner in a suicide attempt. She has drooling, odynophagia, and retrosternal chest pain, with a hoarse voice but '
             'no stridor. Heart rate is 112, blood pressure is normal, and the abdomen is soft. Her husband brought the bottle. The emergency physician asks for initial recommendations. What is the best '
             'initial plan?',
     'choices': ['Airway assessment, IV fluids, NPO, and endoscopy or CT within 24 hours',
                 'Oral milk or water dilution followed by induced emesis to clear the agent',
                 'Weak acid neutralization through a nasogastric tube, then early endoscopy',
                 'Nasogastric lavage with activated charcoal to bind the residual alkali'],
     'answer': 0,
     'explanation': 'Initial caustic management follows the ABCs. Hoarseness suggests laryngeal involvement, so the airway is examined with flexible laryngoscopy and secured early if edema progresses. '
                    'She is resuscitated, kept NPO, and given analgesia and acid suppression. Emesis, neutralization, charcoal, and blind nasogastric tubes are avoided because they re-expose or '
                    'perforate injured tissue. Because symptoms and intent predict significant injury, esophageal and gastric injury is graded by endoscopy within about 24 hours, or by CT when '
                    'perforation or transmural necrosis is suspected.',
     'why_wrong': ['Correct.',
                   'Induced emesis re-exposes the esophagus and larynx to the caustic and risks aspiration, and late dilution adds little.',
                   'Neutralization produces an exothermic reaction that can worsen burns, and blind tube passage risks perforating the injured esophagus.',
                   'Charcoal does not adsorb caustics, obscures endoscopic views, and blind lavage can perforate the injured esophagus.'],
     'board_pearl': 'Caustic ingestion: no emesis, neutralization, charcoal, or blind NG tube; secure the airway and grade the injury.',
     'curveball': 'Which findings suggest perforation or transmural necrosis and move management toward emergency surgery rather than routine endoscopy?',
     'curveball_answer': 'Peritonitis, severe chest or back pain, subcutaneous emphysema, free or mediastinal air, persistent shock or metabolic acidosis, rising lactate, and CT signs of absent wall '
                         'enhancement with periesophageal or perigastric fluid suggest transmural necrosis. These patients need resuscitation, broad-spectrum antibiotics, and urgent surgical '
                         'exploration, often with esophagectomy or gastrectomy, rather than diagnostic endoscopy.'},
    'v269_gen_caust_fnd': {'stem': 'A 4-year-old boy is brought in 2 hours after his mother found him with an open bottle of liquid lye. He vomited once and has refused to drink since, but he is not drooling and is breathing '
             'comfortably. The lips, oral cavity, and oropharynx show no burns. He is calm, with normal vital signs and a normal chest radiograph. What is the most appropriate interpretation and plan?',
     'choices': ['No oral burns excludes significant injury; discharge after a fluid challenge',
                 'Esophageal burns can occur without oral burns; admit and plan endoscopy',
                 'Obtain contrast CT of the chest and abdomen to grade any esophageal injury',
                 'Order a barium swallow now and perform endoscopy only if it is abnormal'],
     'answer': 1,
     'explanation': 'In children, the presence or absence of oral burns does not reliably predict esophageal injury. What predicts significant injury is the agent, here a strong alkali, and symptoms '
                    'such as vomiting, drooling, dysphagia, food refusal, stridor, or chest pain. Multiple symptoms carry the highest risk, but any symptom after a strong caustic warrants admission, NPO '
                    'status, and upper endoscopy within about 24 hours to grade injury. Truly asymptomatic accidental ingestions may be observed in selected cases.',
     'why_wrong': ['Oral burns correlate poorly with esophageal injury, and vomiting and food refusal are symptoms that warrant evaluation.',
                   'Correct.',
                   'CT is used mainly when perforation or transmural necrosis is suspected; endoscopy is the standard for grading injury in a stable child.',
                   'Barium obscures later endoscopy and can cause mediastinitis if a perforation is present, and it misses superficial burns.'],
     'board_pearl': 'In children, symptoms rather than oral burns predict esophageal injury after caustic ingestion.',
     'curveball': 'Which symptoms would make laryngeal injury and airway intervention the more urgent priority in this child?',
     'curveball_answer': 'Stridor, hoarseness or voice change, drooling with inability to handle secretions, dyspnea, or retractions indicate supraglottic or laryngeal burns with evolving edema. These '
                         'children need prompt airway evaluation in a controlled setting and early intubation by an experienced team, because edema can progress over hours. Blind nasotracheal intubation '
                         'is avoided.'},
    'v269_gen_caust_snr': {'stem': 'A 45-year-old man ingested concentrated hydrochloric acid 20 hours ago. He now has severe retrosternal pain, fever, a heart rate of 128, and epigastric guarding. CT shows absent gastric '
             'wall enhancement, pneumomediastinum, and free intraperitoneal air. He has received IV fluids, and his airway is protected. What is the best next step?',
     'choices': ['Upper endoscopy now to grade the injury before any surgical decision',
                 'Esophageal stent placement to seal the perforation and allow feeding',
                 'Broad-spectrum antibiotics and emergency laparotomy for source control',
                 'Nasogastric decompression, a PPI, and serial abdominal examinations'],
     'answer': 2,
     'explanation': 'Acids cause coagulation necrosis and characteristically injure the stomach more than the esophagus. Peritonism, fever, pneumomediastinum, free intraperitoneal air, and loss of wall '
                    'enhancement on CT mean transmural necrosis with perforation. At that point the question is no longer grading the injury but source control: resuscitation, broad-spectrum '
                    'antibiotics, and emergency surgery to resect necrotic viscera, often gastrectomy with or without esophagectomy and diversion, by a multidisciplinary team. Delay is associated with '
                    'high mortality.',
     'why_wrong': ['Endoscopy adds risk and little information once CT shows perforation and necrosis; it would only delay source control.',
                   'Stents do not treat necrotic, perforated stomach with peritoneal contamination and can worsen full-thickness injury.',
                   'Correct.',
                   'Free air, peritonism, and a nonenhancing gastric wall indicate transmural necrosis, which conservative care cannot control.'],
     'board_pearl': 'Caustic perforation or transmural necrosis needs emergency resection, not further diagnostic endoscopy.',
     'curveball': 'If he survives, how should later stricture risk and long-term surveillance be managed?',
     'curveball_answer': 'Survivors of deep injury, Zargar grade 2b or 3, have high stricture risk, usually within about 2 months. Strictures are managed with serial endoscopic dilation, with resection '
                         'and reconstruction such as colon interposition for refractory cases. Long-term endoscopic surveillance is also advised because caustic injury raises esophageal squamous cell '
                         'carcinoma risk decades later.'},
    'v11_gen_06': {'stem': 'A 68-year-old man taking aspirin and clopidogrel after a recent coronary stent has had heavy epistaxis for 2 hours. He is pale and diaphoretic, repeatedly swallowing and spitting blood, '
             'with heart rate 124 and blood pressure 84/50. Bleeding continues despite pinching the nose, and blood is pooling in the oropharynx. What is the immediate priority?',
     'choices': ['Endoscopic localization of the bleeding site with targeted suction cautery',
                 'Platelet transfusion and immediate discontinuation of both antiplatelet agents',
                 'CT angiography to identify the bleeding vessel for selective embolization',
                 'Resuscitate with large-bore IV access and blood while placing nasal packing'],
     'answer': 3,
     'explanation': 'Hypotension, tachycardia, and pallor indicate hemorrhagic shock, so this is first a resuscitation problem. He is positioned upright and leaning forward with suction to protect the '
                    'airway, two large-bore IV lines are placed, blood is crossmatched, and transfusion begins while the nose is packed, anterior and posterior if needed, to tamponade bleeding. '
                    'Intubation is considered if he cannot clear blood. Antithrombotic decisions involve cardiology because stopping dual antiplatelet therapy after a recent stent risks thrombosis.',
     'why_wrong': ['Endoscopic localization is valuable once he is stable, but it cannot come before resuscitation in a hypotensive patient.',
                   'Stopping dual antiplatelet therapy risks stent thrombosis, and platelet transfusion is not first-line; local control and resuscitation come first.',
                   'Sending an unstable patient with ongoing bleeding to CT delays resuscitation and hemorrhage control.',
                   'Correct.'],
     'board_pearl': 'Severe epistaxis with shock is an ABC problem: resuscitate and tamponade at the same time.',
     'curveball': 'Packing slows the bleeding, but he remains hypotensive and needs ongoing transfusion. When should you escalate to arterial control or embolization?',
     'curveball_answer': 'Persistent bleeding or ongoing transfusion need despite properly placed packing is failure of conservative care and warrants definitive treatment: endoscopic sphenopalatine '
                         'artery ligation, adding anterior ethmoid ligation if bleeding is superior, or angiographic embolization of internal maxillary branches when surgery is high risk. The AAO-HNSF '
                         'guideline supports these options for persistent or recurrent bleeding despite packing or cautery.'},
    'v116-gen-03': {'stem': 'A 72-year-old woman on warfarin for atrial fibrillation has brisk right-sided epistaxis with blood running down her throat despite 20 minutes of anterior pressure and oxymetazoline. Her '
             'INR is 2.8. After clot is suctioned, anterior rhinoscopy shows no bleeding from the anterior septum, and blood keeps appearing behind the soft palate. What is the most likely source?',
     'choices': ['Sphenopalatine artery branches in the posterior nasal cavity',
                 'Kiesselbach plexus on the anterior inferior nasal septum',
                 'Anterior ethmoid artery in the superior nasal vault',
                 'Greater palatine artery at the incisive canal of the anterior septum'],
     'answer': 0,
     'explanation': 'Bleeding that persists despite pressure and vasoconstrictor, runs into the pharynx, and has no visible anterior source suggests a posterior origin, most often sphenopalatine artery '
                    'branches from the internal maxillary system. Posterior epistaxis is more common in older patients and those on anticoagulants or with hypertension. It usually needs escalation '
                    'beyond anterior measures: endoscopic localization and cautery, posterior packing, endoscopic sphenopalatine artery ligation, or embolization. Anticoagulation decisions are '
                    'individualized to bleeding severity and thrombotic risk.',
     'why_wrong': ['Correct.',
                   'Kiesselbach plexus bleeding is visible on anterior rhinoscopy and usually controlled with pressure, which failed here.',
                   'Anterior ethmoid bleeding arises high above the middle turbinate and usually drains anteriorly; consider it after trauma or sinus surgery.',
                   'The greater palatine artery reaches the septum through the incisive canal and feeds Kiesselbach plexus, an anterior site.'],
     'board_pearl': 'No visible anterior source with blood behind the palate in an older patient suggests a sphenopalatine source.',
     'curveball': 'When would you favor endoscopic sphenopalatine artery ligation over prolonged posterior packing or embolization?',
     'curveball_answer': 'Endoscopic ligation is favored when bleeding persists or recurs despite packing, when prolonged packing is poorly tolerated because of pain, hypoxemia, or sleep apnea, and when '
                         'an experienced surgeon is available; it has high success and low morbidity. Embolization is favored for poor surgical candidates or after failed ligation, accepting a small '
                         'risk of stroke and facial necrosis.'},
    'v135_gen_03': {'stem': 'A 77-year-old man with a mechanical mitral valve on warfarin has had right epistaxis for 90 minutes. He is anxious, with heart rate 108 and blood pressure 104/66. His INR is 4.1 and '
             'hemoglobin 11.8 g/dL. Bleeding slows but continues with pressure. The resident wants to find the vessel endoscopically right away. What should happen first?',
     'choices': ['Vitamin K and four-factor PCC to fully reverse the INR before local treatment',
                 'IV access and fluids, nasal packing, and INR management with cardiology input',
                 'Rigid endoscopy with suction cautery before IV access to stop the bleeding',
                 'Noncontrast CT of the sinuses to exclude a tumor before choosing treatment'],
     'answer': 1,
     'explanation': 'Severe epistaxis is first an ABC and resuscitation problem. Tachycardia shows meaningful blood loss, so IV access, labs, type and screen, and fluids come with prompt local control, '
                    'here nasal packing because pressure failed. The AAO-HNSF epistaxis guideline advises starting first-line local treatment before transfusion, reversal, or withdrawal of '
                    'anticoagulation unless bleeding is life-threatening, and decisions about warfarin with a mechanical valve are made with the prescribing clinician. Endoscopic localization and '
                    'cautery follow once he is stable.',
     'why_wrong': ['Full reversal with a mechanical valve risks thrombosis; reversal is reserved for life-threatening bleeding that local measures cannot control.',
                   'Correct.',
                   'Localization matters, but a tachycardic patient needs IV access and stabilization first, and packing can control bleeding meanwhile.',
                   'Imaging does not help acute control and is reserved for suspected tumor, trauma, or recurrent unexplained unilateral bleeding.'],
     'board_pearl': 'Without life-threatening bleeding, start local treatment before reversing or stopping anticoagulation.',
     'curveball': 'He continues to bleed around a well-positioned posterior pack. What escalation options should be considered?',
     'curveball_answer': 'Persistent bleeding around a properly placed posterior pack calls for definitive arterial control: endoscopic sphenopalatine artery ligation or cautery in the OR, adding '
                         'anterior ethmoid ligation for superior bleeding, or angiographic embolization of internal maxillary branches. With a supratherapeutic INR and ongoing hemorrhage, targeted '
                         'reversal becomes reasonable after weighing valve thrombosis risk with cardiology.'},
    'v271_gen_epi_fnd': {'stem': 'A 34-year-old woman has had left nasal bleeding for 15 minutes after blowing her nose during a dry winter. She is calm, with normal vital signs, and takes no medications. She has been '
             'tilting her head back and pinching the bony bridge of her nose. Anterior rhinoscopy is obscured by clot. What is the best initial management sequence?',
     'choices': ['Tilt the head back, ice the nasal bridge, and pinch intermittently for 5 minutes',
                 'Place bilateral nonresorbable anterior packs and arrange removal in 3 days',
                 'Lean forward, compress the soft nose for 10 minutes, vasoconstrict, then cauterize',
                 'Silver nitrate cautery to both sides of the septum before clot is evacuated'],
     'answer': 2,
     'explanation': 'Most epistaxis arises anteriorly from Kiesselbach plexus. First-line care is sitting upright and leaning forward, then firm, sustained compression of the soft lower third of the '
                    'nose for at least 5 minutes, often 10 to 15, without releasing to check. Clot is evacuated, and a topical vasoconstrictor with anesthetic improves the view. A visible bleeding point '
                    'is treated with targeted cautery, usually silver nitrate, limited to that site. Packing is used only if bleeding persists, and imaging is not needed.',
     'why_wrong': ['Tilting back sends blood into the pharynx, and intermittent pressure on the bony bridge does not compress the anterior septum.',
                   'Packing is for bleeding that persists after pressure, vasoconstriction, and cautery, and bilateral packs add discomfort without localization.',
                   'Correct.',
                   'Cautery needs a visualized source after clot removal, and simultaneous bilateral septal cautery risks septal perforation.'],
     'board_pearl': 'Anterior epistaxis: lean forward, compress the soft nose without peeking, vasoconstrict, then cauterize a visible point.',
     'curveball': 'How would anticoagulation, hypertension, or a posterior bleeding pattern change her disposition if present?',
     'curveball_answer': 'Anticoagulant use does not mandate admission if local measures control bleeding. Posterior bleeding, posterior packing, need for transfusion, hemodynamic instability, or major '
                         'comorbidity warrants admission and monitoring. Elevated blood pressure is monitored and treated if severe, though acute lowering has not been shown to stop bleeding. Patients '
                         'discharged with packing need clear instructions and follow-up for removal.'},
    'v271_gen_epi_app': {'stem': 'An 81-year-old woman on rivaroxaban has a well-placed right anterior nasal tampon but continues to spit fresh blood. Blood trickles down the posterior pharyngeal wall, her heart rate is '
             '102, and blood pressure is normal. Hemoglobin is 10.9 g/dL. She has obstructive sleep apnea and uses CPAP at home. What is the best next step?',
     'choices': ['Remove the tampon and repeat silver nitrate cautery along the anterior septum',
                 'Add a second, larger anterior tampon on the right side and discharge her home',
                 'Andexanet alfa to reverse rivaroxaban, then continue observation of the tampon',
                 'Endoscopic localization and cautery or posterior packing, with monitored admission'],
     'answer': 3,
     'explanation': 'Ongoing bleeding into the pharynx despite a properly placed anterior pack points to a posterior source or uncontrolled arterial bleeding. Rigid endoscopy can often localize the '
                    'vessel for targeted cautery; when it cannot, a posterior pack or balloon is placed. Posterior packing can cause hypoxemia and hypoventilation, especially with sleep apnea, so she '
                    'needs monitored admission. Antithrombotic decisions are individualized to bleeding severity and stroke risk, and failure of these measures leads to sphenopalatine ligation or '
                    'embolization.',
     'why_wrong': ['Blood down the posterior pharynx despite an anterior tampon suggests a posterior source that anterior cautery will not reach.',
                   'More anterior packing does not tamponade a posterior source, and discharge is unsafe with ongoing bleeding.',
                   'Andexanet is no longer marketed in the US, and reversal is reserved for life-threatening bleeding; PCC would be used if needed.',
                   'Correct.'],
     'board_pearl': 'Bleeding down the pharynx despite an anterior pack implies a posterior source; posterior packing needs monitored admission.',
     'curveball': 'Which patients with posterior nasal packing require monitored admission, and why is it needed?',
     'curveball_answer': 'Essentially all patients with posterior packs are admitted with monitoring and supplemental oxygen. Packing obstructs nasal breathing and can cause hypoxemia and '
                         'hypoventilation, particularly in elderly patients and those with sleep apnea, lung disease, or heart disease. It also causes pain, vagal responses, aspiration, pressure '
                         'necrosis of the alar rim or palate, and sinusitis, so sedation is used cautiously.'},
    'v271_gen_epi_snr': {'stem': 'A 62-year-old man with hypertension has had three episodes of posterior epistaxis over 4 days despite a posterior balloon pack and has required 2 units of blood. He takes no '
             'antithrombotics. Endoscopy after pack removal shows bleeding from behind the posterior end of the right middle turbinate. He is now stable and fit for anesthesia. What is the best next '
             'step?',
     'choices': ['Endoscopic sphenopalatine artery ligation with posterior nasal artery cautery',
                 'Replace the posterior balloon pack and continue tamponade for 5 more days on the ward',
                 'Ligation of the external carotid artery through a cervical incision',
                 'Anterior ethmoid artery ligation through an external Lynch incision'],
     'answer': 0,
     'explanation': 'Recurrent posterior bleeding despite packing and transfusion is failure of conservative care and calls for definitive arterial control. Bleeding behind the posterior middle '
                    'turbinate localizes to the sphenopalatine artery, which exits the sphenopalatine foramen just behind the crista ethmoidalis. Endoscopic ligation or cautery of the sphenopalatine and '
                    'posterior nasal branches is highly effective with low morbidity. Embolization of internal maxillary branches is a comparable alternative for patients unfit for surgery or after '
                    'failed ligation, with a small risk of stroke and facial necrosis.',
     'why_wrong': ['Correct.',
                   'Repeated packing has already failed; longer packing adds pain, infection, and pressure necrosis without a definitive fix.',
                   'External carotid ligation is too proximal, allows collateral refilling, and has been replaced by endoscopic ligation and embolization.',
                   'The source is behind the middle turbinate, in sphenopalatine territory; ethmoid ligation treats superior vault bleeding.'],
     'board_pearl': 'The crista ethmoidalis is the landmark just anterior to the sphenopalatine foramen during endoscopic ligation.',
     'curveball': 'What vascular history or angiographic finding would make embolization particularly hazardous for him?',
     'curveball_answer': 'Dangerous anastomoses between external carotid branches and the internal carotid or ophthalmic circulation, for example through middle meningeal or ethmoidal collaterals, raise '
                         'the risk of stroke or blindness. Severe atherosclerosis, tortuous vessels, prior carotid disease, contrast allergy, and renal failure add risk. Anterior ethmoid bleeding cannot '
                         'be embolized safely because it arises from the ophthalmic artery.'},
    'v113-gen-01': {'stem': 'A 61-year-old man completed chemoradiation for tonsil cancer 14 months ago. Yesterday he had a brief episode of bright-red oral bleeding, about 20 mL, that stopped on its own. Tonight he '
             'presents after a second, larger episode. Examination shows an exposed, necrotic area in the right tonsillar fossa. He is hemodynamically stable. What does the first episode most likely '
             'represent?',
     'choices': ['Mucosal bleeding from radiation-induced telangiectasia',
                 'A sentinel bleed from a threatened carotid artery branch',
                 'Posterior epistaxis draining into the oropharynx',
                 'Gingival bleeding from radiation-related periodontal disease'],
     'answer': 1,
     'explanation': 'Carotid blowout ranges from threatened exposure through sentinel bleeding to acute rupture. A brief, self-limited arterial bleed in an irradiated field with necrotic tissue near the '
                    'carotid system is a sentinel bleed until proven otherwise, and it often precedes catastrophic hemorrhage within hours to days. Recognizing it allows urgent action while the patient '
                    'is stable: airway planning, IV access and crossmatch, CT angiography, and prompt endovascular evaluation, which is far safer than treating an active rupture.',
     'why_wrong': ['Telangiectatic oozing is low volume and venous, not bright-red episodes near an exposed, necrotic fossa after radiation.',
                   'Correct.',
                   'Posterior epistaxis is possible, but the exposed, necrotic tonsillar fossa is a far more dangerous and likely source.',
                   'Periodontal bleeding is minor oozing and does not explain repeated arterial bleeding from the tonsillar fossa.'],
     'board_pearl': 'A self-limited bleed in an irradiated, necrotic field is a sentinel carotid bleed until proven otherwise.',
     'curveball': 'What immediate airway and endovascular or surgical contingencies should be activated tonight?',
     'curveball_answer': 'Admit to a monitored bed with two large-bore IV lines, crossmatched blood, and a massive transfusion plan. Keep suction, packing, and airway equipment at the bedside, and '
                         'consider early controlled intubation or tracheostomy with a cuffed tube. Obtain urgent CT angiography and involve interventional radiology for angiography with possible stent '
                         'or embolization, with vascular surgery as backup.'},
    'v134_hno_02': {'stem': 'A 66-year-old man with recurrent hypopharyngeal cancer after laryngopharyngectomy and radiation has a draining right neck pharyngocutaneous fistula. He had 30 mL of bright-red bleeding '
             'from the wound that stopped with gauze pressure. He is alert, with normal vital signs and a hemoglobin of 11.6 g/dL. What is the most appropriate disposition?',
     'choices': ['Wound packing with hemostatic gauze and discharge with clinic follow-up in 2 days',
                 'Overnight floor observation with a repeat hemoglobin check in the morning',
                 'Admission with crossmatch, CT angiography, and urgent interventional review',
                 'Bedside exploration of the fistula tract to identify the bleeding vessel'],
     'answer': 2,
     'explanation': 'Bleeding from a pharyngocutaneous fistula in an irradiated neck is a sentinel bleed from threatened carotid blowout until proven otherwise. Salivary contamination and radiation '
                    'damage the adventitia and vasa vasorum, and rupture can follow within hours or days. The safe disposition is monitored admission with large-bore access, crossmatched blood, airway '
                    'readiness, urgent CT angiography, and early interventional radiology or vascular involvement while he is stable. Normal vital signs and hemoglobin offer false reassurance.',
     'why_wrong': ['A fistula bleed in an irradiated neck can herald rupture within hours; discharge leaves him without access to rapid control.',
                   'A stable hemoglobin does not exclude a threatened carotid, and routine observation delays the imaging and intervention he needs.',
                   'Correct.',
                   'Probing an infected, irradiated fistula near the carotid at the bedside can precipitate massive hemorrhage without any means of control.'],
     'board_pearl': 'Radiation plus a pharyngocutaneous fistula plus any bleed equals threatened carotid until proven otherwise.',
     'curveball': 'He suddenly rebleeds massively into the pharynx and cannot protect his airway. What happens before any imaging?',
     'curveball_answer': 'Apply direct pressure and pack the fistula and pharynx, call for massive transfusion, and place a cuffed tube through his stoma below the bleeding to protect the lungs from '
                         'aspiration. Once temporarily controlled, he goes directly to the angiography suite or OR for endovascular occlusion or stenting, or surgical ligation if endovascular control is '
                         'unavailable.'},
    'v140_gen_05': {'stem': 'A 58-year-old woman with recurrent neck squamous cell carcinoma after prior neck dissection and reirradiation had a self-limited episode of pulsatile oral bleeding 6 hours ago. CT '
             'angiography shows recurrent tumor encasing more than 270 degrees of the right internal carotid artery, with wall irregularity and a small contrast outpouching. Which interpretation should '
             'guide management?',
     'choices': ['Friable tumor surface bleeding best managed with palliative radiation or cautery',
                 'Incidental arterial irregularity from prior surgery unrelated to the oral bleeding',
                 'Bleeding from a lingual artery branch that can be treated by transoral ligation',
                 'Impending carotid blowout with a sentinel bleed needing urgent endovascular care'],
     'answer': 3,
     'explanation': 'CT angiographic signs of threatened carotid blowout include wall irregularity, pseudoaneurysm, contrast extravasation, and tumor encasement, particularly beyond 180 degrees, in a '
                    'previously irradiated field. Combined with a pulsatile self-limited bleed, this is a sentinel event from impending rupture, and reirradiation further raises the risk. Management is '
                    'urgent: airway readiness, crossmatched blood, and prompt angiography with endovascular treatment, either covered stent or vessel occlusion after assessment of collateral flow.',
     'why_wrong': ['Tumor oozing is possible, but pulsatile bleeding with carotid wall irregularity and outpouching implies the carotid itself is failing.',
                   'Wall irregularity with a pseudoaneurysm in a reirradiated, tumor-encased segment is a high-risk finding, not an incidental one.',
                   'The CTA localizes the problem to the internal carotid, and ligating a small branch transorally would not address it.',
                   'Correct.'],
     'board_pearl': 'CTA red flags for blowout: wall irregularity, pseudoaneurysm, extravasation, and tumor encasement beyond 180 degrees.',
     'curveball': 'If she begins exsanguinating through the mouth before angiography, what bedside temporizing maneuvers can buy time?',
     'curveball_answer': 'Sit her up or turn her to the side to drain blood, suction, and secure the airway with a cuffed tube by intubation or tracheostomy to prevent aspiration. Pack the oropharynx '
                         'firmly with gauze around the airway, and apply direct manual compression to the neck if accessible. Activate massive transfusion and move directly to angiography or the OR for '
                         'definitive control.'},
    'v140_hn_08': {'stem': 'A 57-year-old man undergoes salvage resection of recurrent neck disease 2 years after chemoradiation. After removal of the infected, necrotic tumor bed, the right common and internal '
             'carotid arteries are skeletonized and exposed, and a small pharyngotomy is present. The surrounding skin is fibrotic and poorly vascularized. Which closure strategy best reduces the risk '
             'of later carotid blowout?',
     'choices': ['Close the pharynx and cover the carotid with a pectoralis or free flap',
                 'Close the pharynx primarily and redrape the irradiated skin flaps over it',
                 'Cover the exposed carotid with a split-thickness skin graft and a bolster',
                 'Leave the wound open with wet-to-dry packing until granulation forms'],
     'answer': 0,
     'explanation': 'The carotid depends on its adventitia and vasa vasorum, which radiation, infection, and stripping during dissection compromise. Exposure to saliva, desiccation, or infection then '
                    'leads to wall necrosis and blowout. The key prevention is watertight pharyngeal closure and coverage of the vessel with healthy, well-vascularized tissue from outside the radiation '
                    'field, such as a pectoralis major flap or a free flap. The flap also fills dead space and reinforces the pharyngeal repair against fistula.',
     'why_wrong': ['Correct.',
                   'Irradiated, fibrotic skin flaps are prone to necrosis and fistula, which re-expose the carotid to saliva and infection.',
                   'A skin graft cannot take on an irradiated vessel wall and gives no vascularized barrier against desiccation or saliva.',
                   'Open packing against an exposed, irradiated carotid allows desiccation and infection and directly raises the risk of rupture.'],
     'board_pearl': 'Exposed irradiated carotid: watertight pharyngeal closure plus nonirradiated vascularized flap coverage.',
     'curveball': 'Which flap choices provide robust vessel coverage when the local tissue is irradiated?',
     'curveball_answer': 'The pectoralis major myocutaneous or muscle-only flap is the workhorse for carotid coverage and pharyngeal reinforcement because it lies outside the radiation field and '
                         'reliably reaches the neck. Free flaps such as the anterolateral thigh or radial forearm can resurface larger defects. Supraclavicular or deltopectoral flaps are alternatives, '
                         'though prior neck irradiation may compromise the supraclavicular pedicle.'},
    'v153_hn_01': {'stem': 'A 69-year-old woman returns to clinic 4 months after salvage total laryngectomy with a chronic pharyngocutaneous fistula in an irradiated neck. She mentions that last night the fistula '
             'bled briskly for a few minutes, soaking a towel, then stopped. Today she is comfortable with normal vital signs, and there is no active bleeding. What is the most appropriate action?',
     'choices': ['Outpatient CT angiography later this week with reinforced daily wound care at home',
                 'Direct transfer to the hospital for admission, crossmatch, and CT angiography',
                 'Debride the fistula tract in clinic and apply a silver nitrate dressing',
                 'Begin a 10-day course of oral amoxicillin-clavulanate and recheck in 1 week'],
     'answer': 1,
     'explanation': 'A brief, brisk bleed from a fistula in an irradiated neck after laryngectomy is a sentinel hemorrhage until proven otherwise, even though it has stopped. Saliva, infection, and '
                    'radiation have weakened the carotid wall, and a larger bleed may follow within hours or days. She should go directly to the hospital, by ambulance if needed, for monitored '
                    'admission, large-bore access and crossmatch, airway readiness at her stoma, CT angiography, and early interventional radiology involvement while she is stable.',
     'why_wrong': ['Rupture after a sentinel bleed can occur within hours to days; outpatient imaging leaves her without rapid hemorrhage control.',
                   'Correct.',
                   'Manipulating the fistula next to a threatened carotid can trigger massive hemorrhage in a setting with no way to control it.',
                   'Antibiotics may help wound infection but do not protect the vessel, and a week of delay risks fatal rupture.'],
     'board_pearl': 'A sentinel bleed reported after the fact still mandates same-day admission and vascular imaging.',
     'curveball': 'If she begins exsanguinating during transport, what are the simultaneous airway and hemorrhage priorities?',
     'curveball_answer': 'Place a cuffed tracheostomy or endotracheal tube through her stoma and inflate the cuff to protect the lungs from blood; after laryngectomy, the mouth and trachea are '
                         'separated, which simplifies this. Apply firm direct pressure or packing into the fistula over the bleeding site, call for massive transfusion, and go straight to angiography or '
                         'the OR for definitive control.'},
    'v156_gen_cbs_fnd': {'stem': 'A 64-year-old man is 6 weeks out from salvage neck dissection for recurrent oropharyngeal cancer after chemoradiation. He has diabetes, controlled hypertension, an albumin of 2.9 g/dL, and '
             'a smoking history. The skin flap has broken down, and a salivary fistula now leaves the carotid visible at the base of the wound. Which factor most directly places him at risk of carotid '
             'blowout?',
     'choices': ['Long-standing hypertension raising shear stress on the carotid arterial wall',
                 'Diabetes impairing neutrophil function and wound healing in the neck',
                 'Exposure of the irradiated carotid to saliva through the broken-down flap',
                 'Hypoalbuminemia reflecting protein-calorie malnutrition after treatment'],
     'answer': 2,
     'explanation': "Carotid blowout results from loss of the vessel's protective coverage and blood supply. Radiation damages the vasa vasorum and causes adventitial fibrosis, and surgery may strip the "
                    'adventitia. When a flap breaks down or a fistula exposes the irradiated carotid to saliva, bacteria, and desiccation, the wall necroses and ruptures. Diabetes, malnutrition, and '
                    'hypertension contribute by impairing healing, but the exposed, irradiated vessel bathed in saliva is the dominant risk and warrants urgent coverage.',
     'why_wrong': ['Hypertension is a minor contributor; blowout reflects local wall necrosis rather than systemic pressure on a healthy vessel.',
                   'Diabetes impairs healing and adds risk, but it acts through wound breakdown rather than by directly damaging the vessel.',
                   'Correct.',
                   'Malnutrition worsens healing and is a modifiable cofactor, but it is not the direct cause of carotid wall failure.'],
     'board_pearl': 'Classic blowout setup: prior radiation, wound breakdown or fistula, and an exposed or infected carotid.',
     'curveball': 'He has had no bleeding at all. What surveillance or preventive steps are reasonable given his risk profile?',
     'curveball_answer': 'An exposed carotid is a threatened blowout even without bleeding. Reasonable steps include admission, CT angiography to look for wall irregularity or pseudoaneurysm, salivary '
                         'diversion and fistula control, and early coverage of the vessel with a vascularized flap such as pectoralis major. Nutrition is optimized, the team prepares a bleeding plan, '
                         'and some centers consider preemptive endovascular treatment.'},
    'v272_gen_cbs_fnd': {'stem': 'A 55-year-old woman had transoral robotic resection of a tonsil cancer followed by adjuvant radiation 8 months ago. This morning she spat about two tablespoons of bright-red blood, which '
             'stopped without treatment. Examination shows necrotic, exposed tissue deep in the left tonsillar bed with no active bleeding. She is hemodynamically stable. What is the best next step?',
     'choices': ['Transoral cautery and debridement of the tonsillar bed in the operating room',
                 'Topical tranexamic acid gargles with clinic follow-up in 1 week',
                 'Hyperbaric oxygen therapy to treat the soft-tissue radionecrosis',
                 'Admit for CT angiography and urgent evaluation for endovascular treatment'],
     'answer': 3,
     'explanation': 'A self-limited bright-red bleed from a necrotic, irradiated tonsillar bed may come from external carotid branches, such as the lingual or facial arteries, or from the internal '
                    'carotid, which lies close behind the lateral pharyngeal wall. Either way, it is a sentinel bleed until proven otherwise. The next step is monitored admission with crossmatch and '
                    'airway readiness, CT angiography to look for pseudoaneurysm or wall irregularity, and angiography with embolization or stenting as needed, before any operative manipulation.',
     'why_wrong': ['Debriding necrotic tissue over a possibly exposed artery can provoke massive bleeding before the vessel has been imaged.',
                   'Topical antifibrinolytics do not protect a necrotic artery, and a week of delay risks rupture after this herald bleed.',
                   'Hyperbaric oxygen may help radionecrosis over weeks but does nothing for an imminent arterial rupture.',
                   'Correct.'],
     'board_pearl': 'After radiation, a necrotic tonsillar bed that bleeds needs vascular imaging before any debridement.',
     'curveball': 'Which history and wound findings should make you suspect a threatened carotid even before any hemorrhage occurs?',
     'curveball_answer': 'Prior radiation, especially reirradiation, radical neck dissection, recurrent or fungating tumor at the vessel, pharyngocutaneous fistula, flap or skin necrosis, wound '
                         'infection, and a visible or pulsating vessel in the wound base all signal threatened blowout. CTA showing encasement, wall irregularity, or pseudoaneurysm confirms the risk and '
                         'prompts preemptive coverage or endovascular planning.'},
    'v272_gen_cbs_app': {'stem': 'A 62-year-old man with recurrent oropharyngeal cancer and a tracheostomy suddenly develops brisk pulsatile bleeding from the mouth on the oncology ward. Blood is pooling around the '
             'tracheostomy tube, his heart rate is 132, and blood pressure is 86/52. Interventional radiology is available in 30 minutes. What is the best immediate management?',
     'choices': ['Inflate the cuff, pack the oropharynx, start massive transfusion, then angiography',
                 'Obtain CT angiography first to localize the bleeding before any intervention',
                 'Explore the neck at the bedside to clamp the common carotid artery directly',
                 'Give IV tranexamic acid and crystalloid, then reassess once bleeding slows'],
     'answer': 0,
     'explanation': 'Active carotid blowout is simultaneously an airway, exsanguination, and source-control emergency. Inflating or replacing a cuffed tracheostomy tube protects the lungs from blood. '
                    'Firm oropharyngeal packing and direct pressure temporize while two large-bore lines and a massive transfusion protocol replace losses with balanced blood products. He then goes '
                    'straight to angiography for endovascular occlusion or covered stent, or to the OR for ligation if endovascular care is unavailable. An early hemoglobin underestimates acute loss.',
     'why_wrong': ['Correct.',
                   'An unstable, actively bleeding patient should go directly to angiography or the OR; diagnostic CT costs time he does not have.',
                   'Blind bedside exploration of an irradiated, tumor-bearing neck rarely succeeds and risks uncontrolled hemorrhage.',
                   'Crystalloid dilutes clotting factors, and tranexamic acid does not stop arterial rupture; blood products and mechanical control are needed.'],
     'board_pearl': 'Active blowout: protect the airway with a cuffed tube, pack, transfuse, and go straight to angiography.',
     'curveball': 'How would an open pharyngocutaneous fistula change where and how you can tamponade the bleeding?',
     'curveball_answer': 'A fistula gives direct access to the bleeding region, so gauze can be packed firmly into the tract and held with manual pressure while transoral packing seals the pharyngeal '
                         'side. Pressure must not compress the airway, which is why a cuffed tube below the bleeding comes first. Packing through the fistula is temporary, and endovascular or surgical '
                         'control is still required.'},
    'v272_gen_cbs_snr': {'stem': 'A 60-year-old man with an infected pharyngocutaneous fistula in an irradiated neck has a sentinel bleed. Angiography shows a pseudoaneurysm of the right internal carotid artery. A complete '
             'circle of Willis is present, and he tolerates a 20-minute balloon test occlusion without neurologic change. He is currently stable. What is the most durable treatment?',
     'choices': ['Covered stent across the pseudoaneurysm to preserve carotid flow',
                 'Permanent endovascular occlusion of the internal carotid artery',
                 'Open resection of the pseudoaneurysm with saphenous vein interposition',
                 'Coil embolization of the aneurysm sac with the parent artery preserved'],
     'answer': 1,
     'explanation': 'Endovascular treatment is first-line for carotid blowout, and the choice between preserving and sacrificing the artery depends on cerebral collateral tolerance, contamination, and '
                    'urgency. With a complete circle of Willis and a tolerated balloon test occlusion, permanent occlusion is more durable because the diseased segment is excluded. Covered stents are '
                    'valuable when occlusion is not tolerated or testing is impossible in an emergency, but in contaminated fields they carry higher risks of infection, thrombosis, and rebleeding. '
                    'Vascularized wound coverage should follow.',
     'why_wrong': ['Covered stents preserve flow but, in an infected field, carry high rates of stent infection, thrombosis, and rebleeding.',
                   'Correct.',
                   'An open graft in an irradiated, infected, fistulized field is prone to infection and anastomotic blowout.',
                   'Sac coiling leaves the diseased, exposed wall in place and is less durable than parent artery occlusion in this setting.'],
     'board_pearl': 'Tolerated balloon test occlusion favors permanent carotid occlusion over a covered stent in a contaminated field.',
     'curveball': 'What neurologic and rebleeding surveillance is required after endovascular control of his carotid?',
     'curveball_answer': 'After occlusion, he needs frequent neurologic checks for delayed ischemia and avoidance of hypotension, because delayed strokes can occur despite a passed test occlusion. After '
                         'a stent, antiplatelet therapy is needed, with vigilance for stent infection, thrombosis, and rebleeding. In both cases the fistula and wound need definitive vascularized '
                         'coverage to prevent recurrence.'},
    'v113-gen-02': {'stem': 'A 70-year-old man with a cuffed tracheostomy placed 3 weeks ago for prolonged ventilation is on a ward with humidified oxygen. He suddenly becomes agitated and desaturates to 82%. There is '
             'little chest rise, and a suction catheter will not pass more than a few centimeters into the tube. Breath sounds are faint bilaterally. What is the most likely problem?',
     'choices': ['Bilateral tension pneumothorax from positive pressure ventilation',
                 'Acute bronchospasm from aspiration of oropharyngeal secretions',
                 'Tube obstruction by mucus or displacement out of the trachea',
                 'Massive pulmonary embolism after prolonged immobilization'],
     'answer': 2,
     'explanation': 'Failure to pass a suction catheter is the key bedside test in a tracheostomy emergency: it means the lumen is blocked, usually by inspissated mucus or clot, or the tip is no longer '
                    'in the trachea because of displacement into a false passage or the pretracheal tissues. Either problem prevents ventilation through the tube. The response is immediate: call for '
                    'help, apply oxygen to face and stoma, remove the inner cannula, and if that fails, deflate the cuff and remove or replace the tube.',
     'why_wrong': ['Pneumothorax reduces breath sounds but would not stop a suction catheter from passing through a patent tube.',
                   'Bronchospasm causes wheeze and high airway pressures, but the suction catheter would still pass freely into the trachea.',
                   'Correct.',
                   'Pulmonary embolism causes hypoxemia with preserved chest movement and does not block a suction catheter.'],
     'board_pearl': 'If a suction catheter will not pass, the tracheostomy is blocked or displaced until proven otherwise.',
     'curveball': 'How does your rescue algorithm differ for a fresh tracheostomy compared with a mature tract?',
     'curveball_answer': 'A mature tract, usually after about 7 days, can generally be recannulated through the stoma with a new or smaller tube. In a fresh tracheostomy the tract can collapse and blind '
                         'reinsertion easily creates a false passage, so oxygenation from above and oral intubation are the primary rescue, with stay sutures, if present, used to lift the trachea for '
                         'controlled reinsertion by an experienced operator.'},
    'v140_gen_02': {'stem': 'A 56-year-old woman underwent open tracheostomy 2 days ago for anticipated prolonged ventilation after a head injury. During repositioning, the tube comes out completely and she '
             'desaturates to 85%. Her upper airway is unobstructed, and she was intubated orally without difficulty before surgery. No stay sutures were placed. What is the safest initial approach?',
     'choices': ['Reinsert the same tube through the stoma, pushing firmly past any resistance',
                 'Insert a smaller tube blindly through the stoma and begin bagging at once',
                 'Pass a suction catheter through the stoma as a guide and railroad the tube',
                 'Call for help, cover the stoma, and oxygenate from above or intubate orally'],
     'answer': 3,
     'explanation': 'A tracheostomy tract takes about a week to mature. Before then, the tissue planes can close or shift once the tube is out, and blind reinsertion easily enters a false passage '
                    'anterior to the trachea. Because her upper airway is patent and she was easy to intubate, the safest route is from above: call for help, occlude the stoma, oxygenate by bag-mask, '
                    'and intubate orally with the tube advanced past the stoma. Controlled recannulation can then be done with good lighting and a fiberoptic scope.',
     'why_wrong': ['Forcing a tube through a fresh tract easily creates a false passage into the pretracheal tissues and worsens hypoxemia.',
                   'A smaller tube can still enter a false passage, and bagging into the mediastinum causes emphysema without oxygenation.',
                   'Exchange over a guide suits an experienced operator with visualization, but blind passage into a 2-day tract risks a false passage.',
                   'Correct.'],
     'board_pearl': 'Dislodged fresh tracheostomy with a patent upper airway: oxygenate and intubate from above.',
     'curveball': 'How would management differ for a patient with a mature total laryngectomy stoma?',
     'curveball_answer': 'After total laryngectomy there is no connection between the mouth and trachea, so oral intubation and bag-mask ventilation by mouth are impossible. Oxygen and ventilation go '
                         'only through the stoma, using a pediatric face mask or laryngeal mask applied over it, and the stoma can be intubated directly with a cuffed tracheostomy tube or small '
                         'endotracheal tube.'},
    'v153_lar_01': {'stem': 'A 63-year-old man is 5 days out from an open tracheostomy performed before staging of a bulky, obstructing supraglottic tumor. He suddenly desaturates. A suction catheter will not pass, '
             'bag ventilation through the tube is ineffective, and subcutaneous emphysema is spreading across his neck and upper chest. What is the key next step?',
     'choices': ['Deflate the cuff and remove the tube, then oxygenate through the stoma',
                 'Keep bagging through the tube with higher pressures to recruit the lungs',
                 'Attempt oral intubation with a video laryngoscope while the tube stays in',
                 'Obtain a portable chest radiograph to confirm tube position before acting'],
     'answer': 0,
     'explanation': 'A catheter that will not pass, failed bag ventilation, and spreading emphysema mean the tube is obstructed or has migrated into a false passage, and ventilating through it pumps air '
                    'into the neck and mediastinum. The pivot is to stop, call for help, deflate the cuff, and remove the tube. Because the obstructing tumor makes the upper airway unreliable, the stoma '
                    'is the best route: oxygenate over it and recannulate under direct vision with a fiberoptic scope or tracheal hook, by the most experienced operator.',
     'why_wrong': ['Correct.',
                   'Forcing ventilation through a malpositioned tube drives air into the tissues and mediastinum without oxygenating the lungs.',
                   'A bulky supraglottic tumor makes the upper airway unreliable, and oral attempts delay restoring the stoma route.',
                   'Imaging wastes minutes in a hypoxemic patient; the bedside findings already show obstruction or displacement.'],
     'board_pearl': 'Emphysema with failed ventilation through a tracheostomy means false passage: stop bagging and remove the tube.',
     'curveball': 'How does rescue differ in a mature tracheostomy compared with a total-laryngectomy stoma?',
     'curveball_answer': 'With a tracheostomy, the upper airway may still connect to the lungs, so oxygen is given to both face and stoma, and oral intubation is a backup if stoma recannulation fails. '
                         'After total laryngectomy, the mouth no longer connects to the trachea, so all oxygenation and intubation must go through the stoma, and face-mask ventilation is futile.'},
    'v271_gen_trach_fnd': {'stem': 'A 48-year-old woman with a cuffed tracheostomy placed 3 weeks ago is ventilated in the step-down unit. She becomes distressed, the ventilator alarms for high peak pressures, and saturation '
             'falls to 88%. The respiratory therapist is at the bedside. Her upper airway is known to be patent. What is the best first troubleshooting sequence?',
     'choices': ['Exchange the tube right away for a larger cuffed tube over a bougie at bedside',
                 'Call for help, oxygen to face and stoma, remove the inner cannula, pass suction',
                 'Raise the ventilator pressure limit and FiO2, then obtain a chest radiograph',
                 'Give a bronchodilator nebulizer through the circuit and sedate for dyssynchrony'],
     'answer': 1,
     'explanation': 'High pressures and distress in a tracheostomy patient mean tube obstruction or displacement until proven otherwise. The initial sequence, as in the National Tracheostomy Safety '
                    'Project algorithm, is to call for help, apply high-flow oxygen to both face and stoma, remove the speaking valve, cap, or attachments, and remove the inner cannula, which often '
                    'clears a mucus plug. A suction catheter then tests patency: if it passes, the tube is in the trachea; if not, deflate the cuff and, without improvement, remove the tube.',
     'why_wrong': ['Tube exchange may become necessary, but simple reversible checks come first, and urgent exchange carries its own displacement risk.',
                   'Correct.',
                   'Raising pressure limits treats the alarm rather than the cause and delays identifying an obstructed or displaced tube.',
                   'Bronchospasm and dyssynchrony are possible, but sedating before excluding tube obstruction can be fatal.'],
     'board_pearl': 'Tracheostomy emergency: oxygen to face and stoma, remove the inner cannula, then test with a suction catheter.',
     'curveball': 'Why is knowing whether this is a tracheostomy or a total-laryngectomy stoma lifesaving?',
     'curveball_answer': 'A tracheostomy patient may still be oxygenated and intubated from above, whereas a laryngectomy patient cannot, because the trachea is sutured to the skin and disconnected from '
                         'the pharynx. Applying a face mask or attempting oral intubation after laryngectomy wastes critical time. Bedhead signs, green for tracheostomy and red for laryngectomy, '
                         'communicate this to every responder.'},
    'v271_gen_trach_app': {'stem': 'A 52-year-old man with obesity is on postoperative day 2 after percutaneous tracheostomy. During a bed transfer the tube partly backs out. A suction catheter cannot be advanced into the '
             'trachea, ventilation through the tube is poor, and saturation is 84%. He has a patent upper airway and a grade 1 laryngoscopy view recorded at his original intubation. What is the safest '
             'next step?',
     'choices': ['Push the partly displaced tube back into the stoma and resume ventilation',
                 'Leave the tube in place and ventilate through it with larger tidal volumes',
                 'Remove the tube and oxygenate by bag-mask from above while help arrives',
                 'Pass a bougie blindly through the tube to search for the tracheal lumen'],
     'answer': 2,
     'explanation': 'A partly displaced tube that will not admit a suction catheter is outside the trachea. A fresh percutaneous tract is a tight dilated channel without stay sutures, and the soft '
                    'tissues collapse once the tube moves, so blind reinsertion often makes a false passage, particularly in obese necks. Because his upper airway is patent and he was easy to intubate, '
                    'the safest path is to remove the tube, cover the stoma, oxygenate from above, and intubate orally if needed, before controlled fiberoptic recannulation by an experienced team.',
     'why_wrong': ['Pushing a displaced tube through a 2-day percutaneous tract is likely to enter the pretracheal space and create a false passage.',
                   'Ventilating through a tube whose tip lies outside the trachea delivers gas into the tissues, not the lungs.',
                   'Correct.',
                   'Blind probing of a fresh percutaneous tract can tear tissue and create a false passage while he desaturates.'],
     'board_pearl': 'A fresh percutaneous tract collapses quickly; when the tube displaces, go from above rather than probe the stoma.',
     'curveball': 'How would the plan differ if he had a total laryngectomy and no connection between the mouth and the lungs?',
     'curveball_answer': 'Oxygenation from above would be impossible, so every effort goes through the stoma. Apply oxygen with a small face mask or laryngeal mask over the stoma, and recannulate '
                         'directly with a cuffed tracheostomy tube or small endotracheal tube, using a fiberoptic scope or bougie under direct vision. A laryngectomy stoma is usually wide and sutured to '
                         'skin, so recannulation is typically easier.'},
    'v271_gen_trach_snr': {'stem': 'A 71-year-old man has had a tracheostomy for 6 months because of bilateral vocal fold paralysis with a fixed glottic stenosis. He becomes apneic at home and arrives cyanotic. Paramedics '
             'removed his tube because suction would not pass. Bag-mask ventilation by mouth produces no chest rise. The stoma is mature and open. What is the best next step?',
     'choices': ['Attempt oral intubation with a video laryngoscope and a small endotracheal tube',
                 'Perform an emergency cricothyrotomy above the stoma to gain tracheal access',
                 'Use two-person face-mask ventilation over the mouth and nose with an oral airway',
                 'Insert a cuffed tube or small endotracheal tube into the stoma and ventilate'],
     'answer': 3,
     'explanation': 'When the upper airway is obstructed, the stoma is the only route to the lungs. A mature tract, here 6 months old, can be recannulated directly with a new tracheostomy tube or a '
                    'small cuffed endotracheal tube, guided by a bougie or fiberoptic scope if needed, and ventilation delivered through it. If recannulation fails, a pediatric face mask or laryngeal '
                    'mask over the stoma can oxygenate. A distal mucus plug, the likely cause, is cleared by suction or bronchoscopy once access is restored.',
     'why_wrong': ['A fixed glottic stenosis blocks the upper airway, so oral intubation is likely to fail and delays access through the stoma.',
                   'Cricothyrotomy is unnecessary when a mature stoma already gives direct tracheal access below the obstruction.',
                   'Mask ventilation has already failed because the glottis is obstructed; more operators will not overcome a fixed stenosis.',
                   'Correct.'],
     'board_pearl': 'With a known obstructed upper airway, the tracheostomy stoma is the only route; recannulate and ventilate there.',
     'curveball': 'What clues distinguish a distal mucus plug from a false passage or a cuff-related obstruction?',
     'curveball_answer': 'A mucus plug follows thick secretions or poor humidification; the catheter meets resistance at or beyond the tube tip, and the removed inner cannula may show crusting. A false '
                         'passage follows a recent tube change and causes emphysema and absent end-tidal CO2. Cuff herniation over the tip produces high pressures that resolve when the cuff is deflated.'},
    'v113-gen-03': {'stem': 'A 64-year-old woman underwent rigid esophagoscopy 8 hours ago to remove an impacted chicken bone at the cricopharyngeus. She now has severe neck pain worse with swallowing, a temperature '
             'of 38.7 C, heart rate 118, and crepitus over the left lower neck. Her voice is normal, and there is no stridor. Which complication is most likely?',
     'choices': ['Cervical esophageal perforation with periesophageal contamination',
                 'Retained bone fragment causing a persistent hypopharyngeal mucosal laceration',
                 'Aspiration pneumonitis from regurgitation during anesthesia',
                 'Subcutaneous emphysema from barotrauma during ventilation'],
     'answer': 0,
     'explanation': 'Pain out of proportion, fever, tachycardia, and subcutaneous emphysema after esophageal instrumentation are the classic signs of perforation. The cervical esophagus near the '
                    'cricopharyngeus and Killian dehiscence is the most common site of instrumental injury because the wall is thin and the lumen narrowest. Saliva and bacteria leak into the '
                    'retropharyngeal and danger spaces and can descend into the mediastinum. Prompt recognition matters because outcomes worsen sharply when diagnosis and treatment are delayed beyond 24 '
                    'hours.',
     'why_wrong': ['Correct.',
                   'A retained fragment or abrasion causes pain but not fever, tachycardia, and crepitus within hours of the procedure.',
                   'Aspiration causes cough, hypoxemia, and lung findings, not neck crepitus and pain on swallowing.',
                   'Ventilation barotrauma is uncommon and does not explain fever and focal neck pain after esophageal instrumentation.'],
     'board_pearl': 'Pain, fever, tachycardia, and crepitus after esophagoscopy indicate perforation until imaging excludes it.',
     'curveball': 'Which imaging study and patient factors guide whether she is managed operatively or nonoperatively?',
     'curveball_answer': 'CT of the neck and chest with water-soluble oral contrast, or a water-soluble esophagram, defines the leak, any collection, and mediastinal extension. Nonoperative care suits a '
                         'stable patient diagnosed early with a small contained leak that drains back into the esophagus and no sepsis. Free extravasation, abscess, mediastinitis, sepsis, or delayed '
                         'presentation favor drainage with or without repair.'},
    'v135_gen_02': {'stem': 'A 50-year-old man had flexible endoscopic removal of an impacted steak bolus 6 hours ago. He now reports neck and chest pain, with a temperature of 38.4 C, heart rate 112, and crepitus at '
             'the sternal notch. He asks for something to drink. His blood pressure is normal, and he is breathing comfortably. What is the best next step?',
     'choices': ['Clear liquid trial with a proton pump inhibitor, discharging if fluids are tolerated',
                 'NPO, IV broad-spectrum antibiotics, contrast CT, and surgical consultation',
                 'Barium esophagram as the first study, starting antibiotics only if it shows a leak',
                 'Repeat flexible endoscopy now to look for a mucosal tear and close it with clips'],
     'answer': 1,
     'explanation': 'Fever, tachycardia, chest pain, and crepitus after food bolus removal mean esophageal perforation until proven otherwise. It is a time-sensitive source-control problem, because '
                    'saliva and bacteria spread along fascial planes into the deep neck and mediastinum. Immediate steps are NPO status, IV fluids, broad-spectrum antibiotics covering oral flora and '
                    'anaerobes, with antifungal coverage in sicker patients, and CT of the neck and chest with water-soluble oral contrast to define the injury. Surgical consultation is obtained early.',
     'why_wrong': ['Oral intake feeds contamination into the tissues, and discharge with fever and crepitus misses a time-sensitive perforation.',
                   'Correct.',
                   'Water-soluble contrast or CT is used first because barium in the mediastinum causes mediastinitis, and antibiotics should not wait.',
                   'Insufflation can extend a perforation, and endoscopic therapy follows imaging and multidisciplinary planning.'],
     'board_pearl': 'Suspected perforation: NPO, broad antibiotics, water-soluble contrast CT, and early surgical input.',
     'curveball': 'What features favor nonoperative management of a confirmed perforation over drainage or repair?',
     'curveball_answer': 'Nonoperative care with NPO status, antibiotics, and tube or parenteral nutrition suits a stable patient diagnosed early with a small contained leak that drains back into the '
                         'lumen, minimal contamination, no abscess or sepsis, and no underlying malignancy or obstruction. It requires close monitoring and repeat imaging, and any deterioration prompts '
                         'drainage.'},
    'v272_gen_eso_perf_fnd': {'stem': 'A 70-year-old man has new neck pain and odynophagia 4 hours after rigid esophagoscopy and biopsy of a cervical esophageal lesion. He is afebrile with a heart rate of 104, and there is '
             'faint crepitus above the left clavicle. The team suspects a perforation and wants to define the leak and its extent. Which initial study is most appropriate?',
     'choices': ['Barium esophagram with upright, oblique, and lateral views',
                 'Lateral soft-tissue neck radiograph to look for prevertebral air',
                 'CT of the neck and chest with water-soluble oral contrast',
                 'Repeat rigid esophagoscopy under general anesthesia today'],
     'answer': 2,
     'explanation': 'After instrumentation, neck pain, tachycardia, and crepitus are early signs of cervical perforation even without fever. CT of the neck and chest with water-soluble oral contrast is '
                    'the preferred first study: it shows extraluminal air and contrast, fluid collections, and extension into the retropharyngeal space and mediastinum, which together decide management. '
                    'A water-soluble contrast esophagram is an alternative, followed by dilute barium if negative and suspicion remains. Meanwhile he is kept NPO on IV antibiotics, and surgery is '
                    'consulted.',
     'why_wrong': ['Barium gives fine mucosal detail but causes mediastinal inflammation if it leaks; water-soluble contrast is used first.',
                   'A lateral film may show prevertebral air but cannot define the leak, any collection, or mediastinal extension.',
                   'Correct.',
                   'Repeat esophagoscopy may miss or extend a small perforation and does not show extraluminal spread.'],
     'board_pearl': 'Suspected cervical perforation: CT with water-soluble oral contrast first; barium only if that is negative.',
     'curveball': 'Which imaging findings suggest a contained cervical leak rather than free mediastinal contamination?',
     'curveball_answer': 'A contained leak shows a small amount of extraluminal air or contrast near the defect, confined to the neck, that drains back into the lumen, without fluid collections. Free '
                         'contamination shows contrast spreading into the mediastinum, mediastinal air and fluid, pleural effusions, or a rim-enhancing abscess, and usually needs operative or '
                         'percutaneous drainage.'},
    'v272_gen_eso_perf_app': {'stem': 'A 59-year-old woman with a cervical esophageal perforation after stricture dilation was managed nonoperatively with NPO status and IV piperacillin-tazobactam. On day 3 she has a '
             'temperature of 39.2 C, heart rate 124, and a rising white count. Repeat CT shows an enlarging paraesophageal collection extending into the superior mediastinum and a new right pleural '
             'effusion. What is the best next step?',
     'choices': ['Broaden antibiotics to meropenem plus vancomycin and repeat CT in 48 hours',
                 'Begin oral clear liquids to stimulate motility and esophageal healing',
                 'Endoscopic clip closure of the defect without draining the collections',
                 'Operative or drain-based source control of neck, mediastinum, and pleura'],
     'answer': 3,
     'explanation': 'Nonoperative management suits only stable patients with small, contained leaks under close surveillance. Sepsis, an enlarging collection, mediastinal extension, and a new effusion '
                    'mean that approach has failed. The response is source control: transcervical drainage of the neck, drainage of the mediastinum and pleural space by thoracic surgery as indicated, '
                    'and repair, stenting, or diversion of the perforation chosen by its size and tissue quality. Broad antibiotics continue, and nutrition is given by a route that bypasses the leak.',
     'why_wrong': ['Broader antibiotics cannot sterilize an enlarging undrained collection; sepsis here signals failure of source control.',
                   'Oral intake feeds ongoing contamination through the defect and worsens the mediastinal infection.',
                   'Closing the defect without draining established collections leaves the septic source in place.',
                   'Correct.'],
     'board_pearl': 'Sepsis or an enlarging collection after perforation means nonoperative management has failed: drain it.',
     'curveball': 'When is primary repair reasonable, and when might diversion, stenting, or drainage without primary closure be favored?',
     'curveball_answer': 'Primary repair, often buttressed with muscle, is reasonable for early-recognized perforations with healthy tissue and limited contamination. Drainage alone is common for '
                         'cervical perforations, which often heal once drained. Stents suit selected contained thoracic leaks. Diversion or esophagectomy is reserved for extensive necrosis, delayed '
                         'presentation with friable tissue, or perforation through malignancy or obstruction.'},
    'v272_gen_eso_perf_snr': {'stem': 'A 67-year-old man presents 4 days after a fish bone injury with septic shock requiring norepinephrine. CT shows a cervical esophageal defect, necrotic retropharyngeal tissue, and gas and '
             'fluid tracking below the carina into the posterior mediastinum, with bilateral effusions. He is intubated. The team must choose an operative strategy. What is the best approach?',
     'choices': ['Cervical and thoracic debridement and drainage with planned re-look surgery',
                 'Primary two-layer closure of the esophageal defect through a neck incision',
                 'Transcervical drainage alone, relying on antibiotics for the mediastinum',
                 'Comfort-focused care because a delayed perforation makes surgery futile'],
     'answer': 0,
     'explanation': 'Delayed perforation with necrosis, septic shock, and spread below the carina is descending necrotizing mediastinitis, fundamentally a source-control problem. Friable infected tissue '
                    'will not hold a primary closure, and drainage limited to the neck usually fails when infection extends below the carina. The strategy combines cervical debridement and drainage with '
                    'thoracic drainage by thoracoscopy or thoracotomy, feeding access, control of contamination by drainage, stent, or diversion as tissue allows, and planned re-imaging or '
                    're-exploration, with critical care support.',
     'why_wrong': ['Correct.',
                   'Friable, necrotic tissue 4 days after injury will not hold a primary closure, and the mediastinal infection would remain undrained.',
                   'Infection below the carina usually needs thoracic drainage; cervical drainage alone often fails in descending mediastinitis.',
                   'Delayed presentation raises mortality, but aggressive source control still saves many patients and is the standard.'],
     'board_pearl': 'Descending mediastinitis below the carina needs thoracic as well as cervical drainage, often repeatedly.',
     'curveball': 'What findings would make you plan serial washouts rather than expecting one operation to achieve durable control?',
     'curveball_answer': 'Extensive necrosis, multiple involved compartments, spread below the carina or into both pleural spaces, persistent septic physiology, residual or new collections on follow-up '
                         'CT, and diabetes or immunocompromise predict that one operation will not suffice. Planned re-exploration or scheduled CT every 48 to 72 hours with a low threshold for further '
                         'drainage is standard.'},
    'v113-gen-04': {'stem': 'An 18-year-old male college student is admitted with fever, hypoxemia, and bilateral pleuritic pain. Ten days ago he had exudative tonsillitis treated with rest only. He now has a swollen, '
             'tender left neck below the angle of the jaw and a hot, swollen right knee. Chest CT shows multiple bilateral cavitating peripheral nodules, and blood cultures grow anaerobic gram-negative '
             'bacilli. Which diagnosis is most likely?',
     'choices': ['Right-sided endocarditis from Staphylococcus aureus',
                 'Lemierre syndrome from Fusobacterium necrophorum',
                 'Necrotizing pneumonia from Streptococcus pyogenes',
                 'Disseminated infection from Epstein-Barr virus'],
     'answer': 1,
     'explanation': 'Lemierre syndrome is septic thrombophlebitis of the internal jugular vein after oropharyngeal infection, usually in healthy adolescents and young adults. Fusobacterium necrophorum, '
                    'an anaerobic gram-negative bacillus, spreads from the tonsillar region through the parapharyngeal space to the jugular vein, and infected thrombus sheds septic emboli, most often to '
                    'the lungs as peripheral cavitating nodules and sometimes to joints. The classic clue is a pharyngitis that seems to improve, followed days later by rigors, lateral neck tenderness, '
                    'and pulmonary findings.',
     'why_wrong': ['Endocarditis causes septic emboli but is usually tied to injection drug use or lines, and cultures would show gram-positive cocci.',
                   'Correct.',
                   'Group A streptococcal pneumonia can follow pharyngitis, but cultures would show gram-positive cocci and it would not explain the neck.',
                   'EBV causes tonsillitis and adenopathy but not cavitating septic emboli, septic arthritis, or anaerobic bacteremia.'],
     'board_pearl': 'Pharyngitis, then rigors, lateral neck tenderness, and cavitating lung nodules: think Fusobacterium and Lemierre syndrome.',
     'curveball': 'Which imaging and antimicrobial coverage should be prioritized, and when does source control matter?',
     'curveball_answer': 'Contrast CT of the neck confirms internal jugular thrombosis and shows any peritonsillar or parapharyngeal abscess, and chest CT maps emboli and empyema. Start IV antibiotics '
                         'with reliable anaerobic coverage, such as ampicillin-sulbactam, piperacillin-tazobactam, a carbapenem, or metronidazole with ceftriaxone, usually for 3 to 6 weeks in total. '
                         'Drain any abscess, empyema, or septic joint.'},
    'v143_gen_03': {'stem': 'A 20-year-old man has internal jugular vein thrombosis on contrast neck CT 1 week after pharyngitis, with no neck abscess. Chest CT shows multiple peripheral cavitary nodules, and blood '
             'cultures grow Fusobacterium necrophorum. He is febrile but hemodynamically stable, with no neurologic findings and no thrombus extension beyond the jugular vein. What is the best '
             'treatment?',
     'choices': ['IV vancomycin and cefepime for 7 days, followed by oral amoxicillin for 7 more days',
                 'Therapeutic heparin as the primary treatment, combined with a short antibiotic course',
                 'Several weeks of anaerobic-covering antibiotics, with anticoagulation decided case by case',
                 'Internal jugular vein ligation followed by 2 weeks of IV penicillin G as sole therapy'],
     'answer': 2,
     'explanation': 'Treatment centers on prolonged antibiotics with strong anaerobic activity, such as a beta-lactam with a beta-lactamase inhibitor, a carbapenem, or metronidazole plus a streptococcal '
                    'agent, given IV initially for a total of 3 to 6 weeks because septic thrombus and cavitating emboli clear slowly. Abscesses and empyemas are drained. Anticoagulation is '
                    'individualized because randomized evidence is lacking; it is often considered for thrombus propagation, cavernous sinus or intracranial extension, or persistent sepsis despite '
                    'antibiotics.',
     'why_wrong': ['Vancomycin and cefepime lack reliable anaerobic coverage, and 2 weeks is usually too short for septic thrombophlebitis with emboli.',
                   'Lemierre syndrome is primarily an infection; anticoagulation is an adjunct with limited evidence, not the primary therapy.',
                   'Correct.',
                   'Ligation is reserved for uncontrolled sepsis or emboli despite treatment, and some Fusobacterium strains produce beta-lactamase.'],
     'board_pearl': 'Lemierre syndrome: weeks of anaerobic antibiotics and drainage of collections; anticoagulation is selective.',
     'curveball': 'What progression pattern would make anticoagulation more compelling despite limited randomized evidence?',
     'curveball_answer': 'Propagation of thrombus toward the sigmoid or cavernous sinus, intracranial extension, new septic emboli or persistent bacteremia and fever despite adequate antibiotics and '
                         'drainage, or extensive involvement of the subclavian or contralateral veins make anticoagulation more compelling. Bleeding risk, such as from an undrained abscess or recent '
                         'surgery, must be weighed, and many centers use it selectively.'},
    'v272_gen_lemierre_fnd': {'stem': 'A 22-year-old woman is admitted with presumed community-acquired pneumonia. She had severe pharyngitis 6 days ago that improved, then developed fever and pleuritic chest pain. On review, '
             'she has tender, cord-like swelling along the right sternocleidomastoid. Platelets are 68,000, and chest CT shows multiple peripheral, partly cavitating nodules rather than lobar '
             'consolidation. Which diagnosis should be suspected?',
     'choices': ['Community-acquired pneumonia with reactive cervical lymphadenitis',
                 'Granulomatosis with polyangiitis with multiple cavitating pulmonary nodules',
                 'Pulmonary tuberculosis with tuberculous cervical lymphadenitis',
                 'Septic internal jugular thrombophlebitis with septic pulmonary emboli'],
     'answer': 3,
     'explanation': 'Lemierre syndrome typically follows a pharyngitis that seems to improve, then days later causes fever, rigors, and lateral neck tenderness from septic internal jugular '
                    'thrombophlebitis. Infected clot embolizes to the lungs, producing multiple peripheral, often cavitating nodules, pleuritic pain, and effusions, so it is often mislabeled as '
                    'pneumonia. Thrombocytopenia and liver enzyme elevation are common. Fusobacterium necrophorum is the classic organism, although infection can be polymicrobial. Recognizing the neck '
                    'source changes imaging, antibiotic choice, and duration.',
     'why_wrong': ['Lobar pneumonia does not cause multiple peripheral cavitating nodules, and reactive nodes do not form a tender jugular cord.',
                   'Polyangiitis can cause cavitating nodules, but not after acute pharyngitis with a tender jugular cord and a rapid septic course.',
                   'Tuberculosis evolves over weeks to months and does not follow acute pharyngitis with a thrombosed jugular vein.',
                   'Correct.'],
     'board_pearl': 'Peripheral cavitating nodules after pharyngitis are septic emboli until a jugular source is excluded.',
     'curveball': 'Which imaging study best evaluates both the neck source and the internal jugular thrombosis?',
     'curveball_answer': 'Contrast-enhanced CT of the neck is preferred: it shows a filling defect with an enhancing wall and surrounding inflammation in the internal jugular vein and identifies '
                         'peritonsillar, parapharyngeal, or retropharyngeal collections that need drainage. Ultrasound can show thrombus but misses deep collections and clot behind the mandible or '
                         'clavicle. MRI helps when intracranial extension is suspected.'},
    'v272_gen_lemierre_app': {'stem': 'A 17-year-old boy is in the ICU with fever, tachycardia, and hypotension responding to fluids. Contrast CT shows right internal jugular vein thrombosis next to a 2 cm parapharyngeal '
             'abscess, and chest CT shows cavitating septic emboli with a loculated right pleural empyema. Blood cultures are pending. What is the core management plan?',
     'choices': ['Anaerobic-covering IV antibiotics plus drainage of the abscess and empyema',
                 'Therapeutic anticoagulation alone, since the thrombus is the embolic source',
                 'IV azithromycin for 5 days followed by oral clindamycin to finish at home',
                 'Internal jugular vein ligation as the first step, before starting antibiotics'],
     'answer': 0,
     'explanation': 'Lemierre syndrome is an invasive anaerobic infection first. The core plan is prompt IV antibiotics with reliable anaerobic coverage, blood and source cultures, sepsis resuscitation, '
                    'and drainage of purulent collections, here the parapharyngeal abscess and the loculated empyema, because antibiotics alone rarely clear undrained pus. Therapy continues for several '
                    'weeks. Anticoagulation is decided individually, weighing propagation, intracranial extension, or persistent emboli against bleeding risk around fresh drainage sites.',
     'why_wrong': ['Correct.',
                   'Anticoagulation does not treat infection or drain pus; antibiotics and source control are the foundation of care.',
                   'Macrolides have poor activity against Fusobacterium necrophorum, and a short course is inadequate for invasive disease.',
                   'Ligation is a rescue for refractory septic emboli, and antibiotics must not be delayed in a hypotensive patient.'],
     'board_pearl': 'Lemierre syndrome with collections: anaerobic antibiotics plus drainage of every accessible abscess and empyema.',
     'curveball': 'What clinical pattern would make you search for cavernous sinus or other intracranial extension?',
     'curveball_answer': 'Severe headache, altered mental status, meningismus, palsies of cranial nerves III, IV, V1, or VI, proptosis, chemosis, or periorbital swelling suggest cavernous sinus '
                         'thrombosis or intracranial spread. Thrombus reaching the sigmoid sinus on CT also raises concern. Contrast MRI with MR venography defines the extension, which strengthens the '
                         'case for anticoagulation.'},
    'v272_gen_lemierre_snr': {'stem': 'A 21-year-old woman with Lemierre syndrome has received IV ampicillin-sulbactam for 5 days after drainage of a peritonsillar abscess. She remains febrile with persistently positive blood '
             'cultures for Fusobacterium, and repeat chest CT shows new septic emboli. Her neck tenderness now extends down to the clavicle. What is the best next step?',
     'choices': ['Continue the same regimen unchanged, since fever often persists for weeks',
                 'Repeat neck and chest imaging for undrained pus or thrombus propagation',
                 'Stop antibiotics and send serologies for a presumed drug-induced fever',
                 'Bilateral neck exploration to remove any residual infected neck tissue'],
     'answer': 1,
     'explanation': 'Failure to improve on appropriate therapy is a localization problem. Persistent bacteremia, new septic emboli, and spreading neck tenderness suggest an undrained collection, '
                    'thrombus propagation toward the subclavian vein or sigmoid sinus, an empyema, or another metastatic focus. Repeat contrast CT of the neck and chest guides drainage, while '
                    'microbiology confirms the organism and susceptibilities. Anticoagulation becomes more compelling with propagation, and jugular ligation is reserved for emboli that continue despite '
                    'all other measures.',
     'why_wrong': ['Some fever is expected, but persistent bacteremia and new emboli signal an uncontrolled source that must be found.',
                   'Correct.',
                   'Positive blood cultures and new emboli prove ongoing infection, so stopping antibiotics would be dangerous.',
                   'Exploration without localization adds morbidity; imaging should first identify where the uncontrolled source lies.'],
     'board_pearl': 'Persistent bacteremia in Lemierre syndrome means find the uncontrolled source before changing drugs.',
     'curveball': 'When would internal jugular vein ligation or excision enter the discussion in modern practice?',
     'curveball_answer': 'Ligation or excision is now rare. It is considered when septic emboli or bacteremia continue despite appropriate antibiotics, drainage of all collections, and anticoagulation, '
                         'or when infected thrombus sits within an abscess cavity that cannot otherwise be controlled. It is often done during neck exploration for drainage, accepting a risk of venous '
                         'congestion.'},
    'v113-gen-05': {'stem': 'A 10-year-old girl is brought to the ED 7 days after tonsillectomy because she has been swallowing repeatedly for an hour and then vomited dark, blood-tinged fluid. She is pale, with heart '
             'rate 118 and normal blood pressure. The tonsillar fossae show white eschar without active bleeding. Her mother asks to take her home. What is the safest interpretation?',
     'choices': ['Normal eschar sloughing with reflux of old blood, safe for discharge',
                 'Viral gastroenteritis unrelated to the surgery, needing oral fluids',
                 'A secondary hemorrhage with swallowed blood that needs admission',
                 'A primary hemorrhage requiring immediate return to the operating room'],
     'answer': 2,
     'explanation': 'Secondary post-tonsillectomy hemorrhage occurs after 24 hours, most often on days 5 to 10 when the eschar separates. Children swallow blood, so repeated swallowing and hematemesis '
                    'may be the only signs, and a dry fossa on arrival does not exclude significant bleeding. Her pallor and tachycardia suggest real volume loss, since children maintain blood pressure '
                    'until late. She needs IV access, blood count and type and screen, NPO status, monitored admission, and ENT evaluation with a low threshold for operative control.',
     'why_wrong': ['Repeated swallowing, bloody emesis, pallor, and tachycardia indicate meaningful blood loss, not benign sloughing.',
                   'Blood-tinged emesis on postoperative day 7 is swallowed blood until proven otherwise, not gastroenteritis.',
                   'Correct.',
                   'Primary hemorrhage occurs within 24 hours; this is secondary, and the need for the OR depends on her course.'],
     'board_pearl': 'In children, tachycardia and repeated swallowing may be the only signs of significant post-tonsillectomy bleeding.',
     'curveball': 'What factors determine observation versus return to the operating room for control?',
     'curveball_answer': 'Active bleeding, a fresh clot in the fossa, hemodynamic changes such as tachycardia, a falling hemoglobin, recurrent episodes, or a child who cannot be examined adequately '
                         'favor operative exploration and cautery. A single minor blood-streaked episode with a clean fossa, normal vital signs, and a reliable family may be observed in hospital, with '
                         'lower thresholds for young children.'},
    'v140_gen_01': {'stem': 'A 19-year-old man presents 7 days after tonsillectomy after spitting about a cup of bright-red blood at home. Bleeding has stopped on arrival. He is anxious, with heart rate 96 and blood '
             'pressure 128/74. Examination shows an adherent fresh clot in the left inferior tonsillar fossa. Hemoglobin is 13.4 g/dL. What is the best next step?',
     'choices': ['Discharge with instructions to return if any further bleeding occurs',
                 'Suction the clot off at the bedside to look for the bleeding vessel',
                 'Ice-water gargles and observation for 2 hours in the emergency room',
                 'IV access, NPO, type and screen, and OR exploration with clot removal'],
     'answer': 3,
     'explanation': 'A large secondary bleed with a fresh clot in the fossa is a significant sentinel event; the clot is only temporary hemostasis and frequently dislodges. Normal vital signs and '
                    'hemoglobin offer limited reassurance in a young adult early after hemorrhage. He needs IV access, labs including type and screen, NPO status, and anesthesia involvement for '
                    'operative exploration, clot removal, and cautery. Some cooperative adults with minimal clot are managed at the bedside, but a large bleed favors the OR.',
     'why_wrong': ['A large-volume bleed with a fresh clot carries a high rebleeding risk and is not safe for discharge.',
                   'Removing the clot can restart brisk bleeding; bedside control is possible in some cooperative adults, but a large bleed favors the OR.',
                   'Gargles and brief observation underestimate a significant sentinel bleed with a clot, which commonly rebleeds.',
                   'Correct.'],
     'board_pearl': 'A fresh clot in the tonsillar fossa after a significant bleed predicts rebleeding; plan operative control.',
     'curveball': 'He suddenly vomits blood and becomes hypotensive. How does induction and airway planning change?',
     'curveball_answer': 'Assume a full stomach of swallowed blood and an obscured airway. Resuscitate with blood products, have two working suctions, and use rapid-sequence induction with a cuffed tube '
                         'and an experienced laryngoscopist, with video laryngoscopy available. After intubation, pass an orogastric tube to empty the stomach, and control the bleeding promptly.'},
    'v153_ped_01': {'stem': 'A 4-year-old boy arrives 7 days after tonsillectomy, pale and tachycardic at 150 beats per minute, after vomiting bright-red blood twice. Blood pressure is 98/60 and capillary refill is 3 '
             'seconds. He is crying and will not open his mouth fully, but no active oral bleeding is seen on a brief look. What is the safest management?',
     'choices': ['IV access with fluid resuscitation, labs, NPO, and urgent ENT evaluation',
                 'Oral fluid trial, with discharge if he keeps it down without more bleeding',
                 'Restrain him for a thorough oral examination and clot removal at bedside',
                 'CT angiography of the neck to look for an aberrant vascular injury first'],
     'answer': 0,
     'explanation': 'Children can swallow large volumes of blood and maintain blood pressure until late, so tachycardia, pallor, and delayed capillary refill after bloody emesis indicate significant '
                    'hemorrhage even with a dry first look. Management is resuscitation with IV access, a fluid bolus, blood count, coagulation tests, and crossmatch, NPO status, and urgent ENT and '
                    'anesthesia involvement. Examination is completed in a controlled setting, usually the OR, where the fossa can be explored and cauterized.',
     'why_wrong': ['Correct.',
                   'Oral intake is unsafe before possible anesthesia, and discharge ignores clear signs of significant blood loss.',
                   'Forced examination of a frightened child can dislodge a clot and precipitate brisk bleeding outside a controlled setting.',
                   'Angiography is reserved for recurrent unexplained hemorrhage; this child first needs resuscitation and operative evaluation.'],
     'board_pearl': 'Children compensate until late; tachycardia after bloody emesis following tonsillectomy is a significant bleed.',
     'curveball': 'What anesthesia concern arises from assuming this child has a stomach full of swallowed blood?',
     'curveball_answer': 'Swallowed blood makes him a full-stomach patient at high aspiration risk, and vomiting during induction can flood an airway already obscured by bleeding. Anesthesia uses '
                         'rapid-sequence induction with a cuffed tube, two suctions, an experienced laryngoscopist, and adequate resuscitation first. After intubation, an orogastric tube empties the '
                         'stomach before emergence to reduce aspiration at extubation.'},
    'v156_gen_pth_fnd': {'stem': 'A 6-year-old girl begins spitting bright-red blood 6 hours after tonsillectomy for sleep-disordered breathing, while still in the day-surgery unit. She is tachycardic, and a small '
             'pulsatile vessel is seen in the right tonsillar fossa. The resident is asked to classify the bleed and explain its likely cause to the family. Which classification and mechanism are '
             'correct?',
     'choices': ['Secondary hemorrhage, usually from separation of the eschar',
                 'Primary hemorrhage, usually from incomplete surgical hemostasis',
                 'Primary hemorrhage, usually from an undiagnosed coagulopathy',
                 'Secondary hemorrhage, usually from infection of the fossa'],
     'answer': 1,
     'explanation': 'Post-tonsillectomy hemorrhage is classified by timing. Primary hemorrhage occurs within the first 24 hours and usually reflects incomplete hemostasis of a vessel in the tonsillar '
                    'bed, often declaring as anesthesia wears off and blood pressure rises. Secondary hemorrhage occurs after 24 hours, most often between days 5 and 10, when the fibrinous eschar '
                    'separates. The distinction guides counseling and suspicion, but both can be life-threatening, and a visible pulsatile vessel with tachycardia needs return to the OR.',
     'why_wrong': ['Secondary hemorrhage occurs after 24 hours, typically days 5 to 10 when the eschar separates; this bleed occurred at 6 hours.',
                   'Correct.',
                   'Coagulopathy should be considered with recurrent or unusual bleeding, but most early bleeds are technical in origin.',
                   'Infection has been proposed as a contributor to late bleeding, but this bleed is within 24 hours and a vessel is visible.'],
     'board_pearl': 'Primary bleed: within 24 hours, technical. Secondary: after 24 hours, peaking days 5 to 10 with eschar separation.',
     'curveball': 'A child on postoperative day 7 has one episode of blood-tinged saliva that resolves before arrival. Does a benign exam on arrival rule out a significant secondary bleed?',
     'curveball_answer': 'No. Secondary bleeds are often intermittent, and clot can hide in the fossa while blood is swallowed. A single blood-streaked episode with a clean fossa, normal vital signs and '
                         'hemoglobin, and a reliable family may be observed, but any larger bleed, clot, tachycardia, or repeated episodes warrants admission and a low threshold for operative '
                         'exploration.',
     'accuracy_note': 'Corrected the definition of secondary hemorrhage to any bleed after 24 hours, peaking on days 5 to 10, rather than only bleeding after days 5 to 10.'},
    'v271_gen_pth_fnd': {'stem': 'An 8-year-old boy is brought in on postoperative day 6 after tonsillectomy because he coughed up a mouthful of bright-red blood at home 1 hour ago. He now looks well, with heart rate 92, '
             'normal blood pressure, and no active bleeding. Both fossae have eschar without visible clot. Hemoglobin is 12.6 g/dL. What is the most appropriate disposition?',
     'choices': ['Discharge home now, since the examination and hemoglobin are reassuring',
                 'Immediate return to the operating room for cautery of both tonsillar fossae',
                 'Hospital observation with IV access and NPO status pending ENT review',
                 'Discharge with tranexamic acid mouthwash and a clinic review in 3 days'],
     'answer': 2,
     'explanation': 'Secondary bleeding often stops before arrival, and a single episode can herald a larger rebleed within hours. A credible report of bright-red blood therefore needs monitored '
                    'assessment even when the child looks well: IV access, blood count and type and screen, NPO status in case anesthesia is needed, and ENT examination. With normal vital signs, no '
                    'clot, and no active bleeding, in-hospital observation is appropriate, and any rebleeding, clot, or hemodynamic change leads to operative control.',
     'why_wrong': ['A credible bright-red bleed can recur briskly; a dry fossa and normal labs on arrival do not exclude a significant event.',
                   'With normal vital signs, no clot, and no active bleeding, observation is reasonable, reserving the OR for rebleeding or clot.',
                   'Correct.',
                   'Topical tranexamic acid has limited evidence, and discharge without observation is premature after a credible bleed.'],
     'board_pearl': 'A credible secondary bleed with a dry fossa still warrants IV access and in-hospital observation.',
     'curveball': 'What findings during observation would move you from monitored evaluation to urgent operative control?',
     'curveball_answer': 'Any active bleeding, a new clot in the fossa, repeated hematemesis or swallowing, rising heart rate or other signs of hypovolemia, a falling hemoglobin, or inability to examine '
                         'the fossa adequately while concern persists all favor taking him to the OR for exploration and cautery under general anesthesia.'},
    'v271_gen_pth_app': {'stem': 'A 9-year-old girl on postoperative day 8 after tonsillectomy is in the ED with active bright-red bleeding from the left tonsillar fossa, repeated swallowing, and a heart rate of 140. Blood '
             'pressure is 100/64. She is frightened but cooperative. The emergency physician asks what to do while the OR is being prepared. What is the best immediate management?',
     'choices': ['Apply topical epinephrine on gauze and wait for the hemoglobin before escalating',
                 'Attempt bedside silver nitrate cautery of the fossa before obtaining IV access',
                 'Lay her flat with the head turned to one side while transfer is being arranged',
                 'Sit her up, suction, start IV fluids and labs, crossmatch, and call anesthesia'],
     'answer': 3,
     'explanation': 'Active post-tonsillectomy hemorrhage is a shared airway and blood-loss emergency. While the OR is prepared, she sits upright and leans forward with large-bore suction to clear '
                    'blood, and IV access is placed for fluids and blood, with blood count, coagulation tests, and crossmatch. She is kept NPO, and anesthesia is called early. Gauze pressure with a '
                    'vasoconstrictor can temporize. An early hemoglobin does not reflect acute loss, and definitive control follows in the OR.',
     'why_wrong': ['Topical pressure may help briefly, but waiting for a hemoglobin underestimates acute loss and delays resuscitation.',
                   'Bedside cautery in a bleeding child is rarely effective and should not take priority over IV access and resuscitation.',
                   'Supine positioning lets blood run into the airway; sitting up and leaning forward helps her clear blood.',
                   'Correct.'],
     'board_pearl': 'Active tonsil bleed: upright, suction, IV access, crossmatch, NPO, early anesthesia, then the OR.',
     'curveball': 'How do swallowed blood, induction of anesthesia, and a full stomach change aspiration planning?',
     'curveball_answer': 'She is a full-stomach patient whose stomach may hold a large volume of swallowed blood, so vomiting at induction can flood the airway. Plan rapid-sequence induction after '
                         'volume resuscitation, with two suctions, a cuffed tube, and an experienced laryngoscopist. Once she is intubated, an orogastric tube empties the stomach before emergence, and '
                         'she is extubated awake.'},
    'v271_gen_pth_snr': {'stem': 'A 5-year-old boy with a second post-tonsillectomy bleed on day 9 becomes pale and lethargic in the ED, with heart rate 170 and blood pressure 70/40. Brisk bleeding fills the oropharynx '
             'faster than it can be suctioned. Coagulation results are pending, and the OR is ready. What is the best decision?',
     'choices': ['Immediate transfer to the OR for intubation and hemostasis with blood running',
                 'Await coagulation results and correct any abnormality before going to the OR',
                 'Obtain CT angiography to look for an aberrant carotid artery or pseudoaneurysm',
                 'Pack the tonsillar fossa at the bedside and observe the response for 30 minutes'],
     'answer': 0,
     'explanation': 'Hypotension, tachycardia, and lethargy with ongoing brisk bleeding are decompensated hemorrhagic shock in a child, combined with a blood-filled difficult airway. The senior task is '
                    'coordination: emergency-release blood and a massive transfusion plan, an experienced anesthesia and ENT team, two suctions, and rapid-sequence induction with a cuffed tube, followed '
                    'by immediate fossa exploration and cautery or suture ligation. Laboratory correction and investigation of the cause proceed in parallel and must not delay operative control.',
     'why_wrong': ['Correct.',
                   'Waiting for labs in hemorrhagic shock delays the only effective treatment; coagulopathy can be corrected in the OR.',
                   'Imaging is for recurrent bleeding without a surgical source; an unstable child needs immediate operative control.',
                   'Bedside packing in a shocked, bleeding child is unreliable and delays airway protection and definitive hemostasis.'],
     'board_pearl': 'Shock from a tonsil bleed: go straight to the OR with blood running; investigate the cause later.',
     'curveball': 'If bleeding persists despite local operative control, what vascular escalation options should be considered?',
     'curveball_answer': 'Persistent or recurrent bleeding despite fossa cautery or suture ligation suggests an arterial source such as a lingual, facial, or ascending pharyngeal branch, or rarely a '
                         'pseudoaneurysm. Angiography with selective embolization is the preferred next step, with external carotid ligation if embolization is unavailable and the patient is unstable. A '
                         'coagulopathy workup, including von Willebrand disease, is also needed.'},
    'v116-gen-01': {'stem': 'A 48-year-old man with type 2 diabetes has 5 days of fever, odynophagia, trismus, and left neck swelling. He is handling secretions and has no stridor. Flexible laryngoscopy shows medial '
             'bulging of the left lateral pharyngeal wall with a patent glottis. Contrast CT shows a 4 cm multiloculated poststyloid parapharyngeal abscess displacing the carotid sheath. What is the '
             'management priority?',
     'choices': ['IV antibiotics alone for 72 hours, operating only if there is no response',
                 'IV antibiotics and prompt transcervical drainage with an airway plan',
                 'Transoral needle aspiration through the lateral pharyngeal wall at bedside',
                 'Tracheostomy under local anesthesia, deferring drainage for 48 hours'],
     'answer': 1,
     'explanation': 'Deep neck abscesses can threaten the airway and spread along the carotid sheath to the mediastinum, or cause jugular thrombosis and carotid erosion. Diabetes raises the risk of '
                    'Klebsiella infection and complications. Management combines airway assessment and a controlled airway plan, which with trismus often means awake fiberoptic intubation, IV '
                    'broad-spectrum antibiotics, and prompt drainage. A large multiloculated poststyloid collection beside the great vessels is best drained transcervically, which gives control of the '
                    'carotid sheath. Cultures guide later narrowing.',
     'why_wrong': ['A trial of antibiotics suits small unilocular collections, not a large multiloculated poststyloid abscess in a diabetic patient.',
                   'Correct.',
                   'A collection around the carotid sheath is unsafe to aspirate transorally, and multiloculated pus drains poorly through a needle.',
                   'Tracheostomy may be part of the airway plan, but deferring drainage of a large abscess allows spread to the mediastinum or vessels.'],
     'board_pearl': 'Large, multiloculated, or poststyloid parapharyngeal abscesses need transcervical drainage rather than a prolonged antibiotic trial.',
     'curveball': 'Which signs make awake airway control or an alternative airway strategy safer than routine induction in this patient?',
     'curveball_answer': 'Trismus limiting mouth opening, stridor, drooling, voice change, inability to lie flat, medial pharyngeal wall or supraglottic swelling on laryngoscopy, and airway deviation on '
                         'CT all predict difficult laryngoscopy or obstruction after induction. These favor awake fiberoptic intubation or awake tracheostomy with a surgeon ready, rather than induction '
                         'with paralysis.'},
    'v140_gen_04': {'stem': 'A 39-year-old woman has 2 days of fever and painful swelling under her jaw after a tooth infection. She has tongue elevation, drooling, and a firm, woody floor of mouth on both sides. '
             'Oxygen saturation is 97%. Contrast CT in the ED shows diffuse submandibular and sublingual edema with no drainable collection. The emergency physician asks whether she can go home on oral '
             'antibiotics. What is the best next step?',
     'choices': ['Discharge on oral amoxicillin-clavulanate with a recheck in 24 hours',
                 'Bedside needle aspiration of the floor of mouth to obtain cultures',
                 'Admit to a monitored setting with IV antibiotics and an airway plan',
                 'Await fluctuance before any treatment beyond analgesia and fluids'],
     'answer': 2,
     'explanation': 'Bilateral submandibular and sublingual swelling with tongue elevation and drooling is Ludwig angina, a spreading cellulitis that threatens the airway through tongue displacement and '
                    'edema, often without a discrete abscess. A CT showing no collection only means there is nothing to drain yet. She needs admission to an ICU or other monitored setting, IV '
                    'antibiotics covering oral streptococci and anaerobes, dental source control, and an airway assessment and plan with a low threshold for awake intubation or tracheostomy.',
     'why_wrong': ['Absence of an abscess does not remove airway risk; Ludwig angina can obstruct the airway without any collection.',
                   'There is no collection to aspirate, and needling an edematous floor of mouth adds bleeding and swelling risk.',
                   'Correct.',
                   'Ludwig angina may never become fluctuant, and waiting withholds antibiotics while the airway narrows.'],
     'board_pearl': 'No abscess on CT does not mean no airway risk in Ludwig angina.',
     'curveball': 'What features would push you toward awake intubation versus awake tracheostomy for her?',
     'curveball_answer': 'Awake fiberoptic nasal intubation suits patients with adequate nasal access and a visible glottis on endoscopy. Awake tracheostomy is favored with severe trismus, massive '
                         'tongue and floor-of-mouth swelling, supraglottic edema obscuring the glottis, pus or blood in the airway, or a failed fiberoptic attempt. Anterior neck edema makes tracheostomy '
                         'harder, so the decision is made early.'},
    'v153_gen_01': {'stem': 'A 57-year-old man with a right parapharyngeal abscess seen on CT 6 hours ago is receiving IV ampicillin-sulbactam while awaiting the OR. He now has increasing neck swelling, a muffled '
             'voice, drooling, and new inspiratory stridor. He is sitting forward with saturation of 92%. The resident asks whether to repeat the CT because the earlier scan may be outdated. What is the '
             'immediate priority?',
     'choices': ['Repeat contrast CT of the neck to reassess the extent of the abscess',
                 'Add IV dexamethasone and heliox and continue observation on the ward',
                 'Bedside incision through the neck swelling to decompress the abscess',
                 'Secure the airway awake in the OR with a surgeon ready for tracheostomy'],
     'answer': 3,
     'explanation': 'New stridor, drooling, and a muffled voice despite antibiotics mean the airway is actively threatened. The priority is a definitive airway in a controlled setting, usually awake '
                    'fiberoptic intubation or awake tracheostomy under local anesthesia in the OR, with an experienced team and front-of-neck access ready. Repeat imaging or ward observation risks '
                    'obstruction during transport or supine positioning. Once the airway is secure, the abscess can be drained in the same anesthetic, guided by the earlier CT.',
     'why_wrong': ['Lying supine for CT with new stridor risks complete obstruction, and the scan would not change the immediate need for an airway.',
                   'Steroids and heliox may temporize, but new stridor with drooling demands definitive airway control, not observation.',
                   'Blind bedside incision near the carotid sheath risks major bleeding and does not secure the airway.',
                   'Correct.'],
     'board_pearl': 'New stridor in a deep neck infection: secure the airway first; repeat imaging can wait.',
     'curveball': 'What CT or clinical findings would make mediastinal extension part of your immediate source-control planning?',
     'curveball_answer': 'Chest pain, dyspnea, pleural effusions, a widened mediastinum, or CT showing fluid or gas tracking through the retropharyngeal or danger space or along the carotid sheath into '
                         'the chest indicate descending mediastinitis. Imaging should include the chest, and thoracic surgery should join the plan, because cervical drainage alone often fails when '
                         'infection extends below the carina.'},
    'v271_gen_dnsi_fnd': {'stem': 'A 34-year-old woman has 4 days of fever, trismus, a muffled voice, and progressive right lateral neck swelling after a sore throat. She is sitting comfortably and handling secretions, with '
             'no stridor and saturation of 99%. Flexible laryngoscopy shows a patent airway with mild right pharyngeal wall fullness. IV antibiotics have been started. Which evaluation is most '
             'appropriate next?',
     'choices': ['Contrast-enhanced CT of the neck to map spaces and collections',
                 'Noncontrast CT of the neck to avoid any contrast-related kidney injury',
                 'Lateral soft-tissue neck radiograph as the definitive imaging study',
                 'MRI of the neck with gadolinium before deciding on any further therapy'],
     'answer': 0,
     'explanation': 'In a suspected deep neck infection, the airway is assessed first; here she is stable with a patent airway on laryngoscopy. Contrast-enhanced CT is then the standard rapid map: it '
                    'identifies the involved spaces, distinguishes a rim-enhancing collection from cellulitis or phlegmon, and shows the relation to the carotid sheath, jugular thrombosis, and '
                    'mediastinal extension. Antibiotics start promptly without waiting for imaging. If the airway were unstable, securing it would come before transport to the scanner.',
     'why_wrong': ['Correct.',
                   'Without contrast, CT cannot reliably distinguish abscess from cellulitis or show vascular complications such as jugular thrombosis.',
                   'A lateral radiograph screens for retropharyngeal swelling but cannot map parapharyngeal or multispace infection.',
                   'MRI gives soft-tissue detail but is slow, needs prolonged supine positioning, and is not the first study in acute deep neck infection.'],
     'board_pearl': 'Deep neck infection: airway first, then contrast CT to map spaces, collections, and vessels.',
     'curveball': 'Which symptoms in this patient would suggest retropharyngeal or danger-space extension toward the mediastinum?',
     'curveball_answer': 'Neck stiffness or pain on extension, odynophagia out of proportion, posterior pharyngeal wall bulging, chest or back pain, dyspnea, and widening of the prevertebral soft '
                         'tissues suggest retropharyngeal or danger-space spread. The danger space runs from the skull base to the diaphragm behind the alar fascia, so CT should extend into the chest '
                         'when these features appear.'},
    'v271_gen_dnsi_app': {'stem': 'A 41-year-old man has a 3.5 cm rim-enhancing collection in the left prestyloid parapharyngeal space on contrast CT, lying medial to the great vessels and bulging the lateral pharyngeal '
             'wall. Despite 48 hours of IV clindamycin, his trismus, fever, and dysphagia are worsening. The airway is patent on laryngoscopy, and the carotid sheath is uninvolved. What is the best next '
             'step?',
     'choices': ['Continue IV clindamycin for 72 more hours, then repeat contrast CT imaging',
                 'Transoral incision and drainage of the collection under general anesthesia',
                 'Bedside needle aspiration through the lateral pharyngeal wall under topical',
                 'Transcervical exploration of every deep neck space with planned tracheostomy'],
     'answer': 1,
     'explanation': 'A rim-enhancing parapharyngeal collection that worsens despite 48 hours of appropriate IV antibiotics needs drainage, with cultures, while antibiotics continue. The approach follows '
                    'the anatomy. A collection confined to the prestyloid compartment, medial to the great vessels and bulging into the pharynx, can be drained transorally through the lateral pharyngeal '
                    'wall under general anesthesia once a safe airway is secured. Collections lateral to or involving the carotid sheath, poststyloid collections, and multispace infections need '
                    'transcervical drainage.',
     'why_wrong': ['Worsening symptoms with an organized collection after 48 hours of antibiotics indicate a need for drainage now.',
                   'Correct.',
                   'Bedside aspiration in a trismic patient gives poor exposure near the great vessels and often fails to evacuate a large collection.',
                   'This prestyloid collection lies medial to the vessels and is reachable transorally, so extensive exploration adds morbidity.'],
     'board_pearl': 'Medial prestyloid parapharyngeal abscesses can be drained transorally; poststyloid or lateral collections go transcervical.',
     'curveball': 'When would a transcervical route be safer than a transoral route for a parapharyngeal abscess?',
     'curveball_answer': 'Transcervical drainage is safer when the collection extends lateral to or around the great vessels, into the poststyloid compartment, into multiple spaces such as the '
                         'submandibular or retropharyngeal, or inferiorly toward the mediastinum, or when jugular thrombosis or pseudoaneurysm is suspected. It gives proximal vascular control and '
                         'dependent drainage.'},
    'v271_gen_dnsi_snr': {'stem': 'A 60-year-old woman underwent transcervical drainage of a retropharyngeal abscess 2 days ago. Despite IV meropenem, she has persistent fever of 39 C, a rising lactate, new pleuritic chest '
             'pain, and dyspnea. Chest radiograph shows bilateral pleural effusions and a widened mediastinum. The neck wound is draining scant fluid. What is the best next step?',
     'choices': ['Add vancomycin and an antifungal agent and reassess in 48 hours',
                 'Remove the neck drains, since output is low and the wound looks clean',
                 'Urgent CT of the neck and chest with thoracic surgery involvement',
                 'Bedside thoracentesis alone, attributing the effusions to fluid overload'],
     'answer': 2,
     'explanation': 'Persistent sepsis after drainage is a localization problem until proven otherwise. A retropharyngeal infection can descend through the retropharyngeal and danger spaces into the '
                    'posterior mediastinum, producing descending necrotizing mediastinitis with pleural empyema. Chest pain, dyspnea, effusions, and a widened mediastinum require urgent contrast CT of '
                    'the neck and chest. Collections below the carina or in the pleura usually need thoracic surgical drainage by thoracoscopy or thoracotomy, with repeat imaging to confirm control.',
     'why_wrong': ['Broadening antibiotics without finding the source delays drainage of a likely mediastinal or pleural collection.',
                   'Low drain output does not mean control; persistent sepsis suggests infection has spread beyond the drained space.',
                   'Correct.',
                   'Attributing new effusions with sepsis to fluid overload risks missing empyema and mediastinitis, which need surgical drainage.'],
     'board_pearl': 'Persistent sepsis after neck drainage: image the chest for descending necrotizing mediastinitis.',
     'curveball': 'How would internal jugular thrombosis with septic pulmonary emboli change the differential and workup?',
     'curveball_answer': 'It suggests septic thrombophlebitis, a Lemierre-type process, as an alternative or additional source of sepsis and lung findings. Contrast neck CT shows the jugular filling '
                         'defect, and chest CT shows peripheral cavitating nodules. Blood cultures should include anaerobic culture for Fusobacterium, antibiotics need strong anaerobic coverage, and '
                         'anticoagulation is considered selectively.'},
    'v139_gen_01': {'stem': 'A 20-month-old boy started coughing and choking while eating peanuts at a party 6 hours ago. He now has a persistent cough, decreased breath sounds with expiratory wheeze over the right '
             'chest, and saturation of 95% on room air. An expiratory chest radiograph shows hyperinflation of the right lung with mediastinal shift to the left. What is the best next step?',
     'choices': ['Nebulized albuterol and a short course of oral steroids for reactive airway',
                 'CT of the chest to confirm a foreign body before any airway intervention',
                 'Chest physiotherapy with postural drainage to help dislodge the object',
                 'Rigid bronchoscopy under general anesthesia with foreign-body forceps'],
     'answer': 3,
     'explanation': 'A witnessed choking episode while eating nuts, followed by unilateral wheeze and decreased breath sounds, is a bronchial foreign body until proven otherwise. Expiratory '
                    'hyperinflation with a contralateral mediastinal shift reflects ball-valve air trapping behind a partially obstructing object, usually in a mainstem bronchus. Peanuts are '
                    'radiolucent, so the object itself is rarely seen. Definitive management is prompt rigid bronchoscopy under general anesthesia, with a ventilating bronchoscope, optical forceps, and '
                    'a team prepared for removal.',
     'why_wrong': ['Unilateral wheeze after witnessed choking is a foreign body, not asthma, and bronchodilators only delay removal.',
                   'With a classic history and air trapping, CT adds radiation and delay; it helps when history and findings are equivocal.',
                   'Postural drainage can dislodge the object into the trachea or glottis and cause complete obstruction.',
                   'Correct.'],
     'board_pearl': 'Witnessed choking plus unilateral wheeze or air trapping warrants rigid bronchoscopy, even for radiolucent objects.',
     'curveball': 'How would a completely obstructing proximal object, at the glottis or in the trachea, change the airway strategy?',
     'curveball_answer': 'Complete proximal obstruction is an immediate threat. A child who cannot cough, cry, or breathe gets back blows and chest thrusts if under 1 year, or abdominal thrusts if '
                         'older, then direct laryngoscopy with Magill forceps if the object is visible. In the OR, restoring ventilation comes first, sometimes by pushing a tracheal object into one '
                         'mainstem bronchus to ventilate the other lung.'},
    'v140_gen_06': {'stem': 'A 3-year-old girl is undergoing rigid bronchoscopy for an almond fragment in the right mainstem bronchus. While the fragment is being withdrawn with optical forceps, it slips free and '
             'lodges in the subglottis. Ventilation through the bronchoscope suddenly fails, and saturation falls rapidly to 75%. What is the immediate priority?',
     'choices': ['Push the fragment back into a mainstem bronchus to restore ventilation',
                 'Remove the bronchoscope and attempt bag-mask ventilation from above the glottis',
                 'Perform an emergency tracheostomy below the obstruction at once',
                 'Pause the procedure and increase the FiO2 and ventilating pressures'],
     'answer': 0,
     'explanation': 'Extraction can convert a partial distal obstruction into a complete central one if the object is dropped at a narrow point such as the subglottis, the narrowest part of the '
                    'pediatric airway. The priority is ventilation, not retrieval. Pushing the object back into a mainstem bronchus with the bronchoscope reopens the trachea and allows ventilation of '
                    'the other lung while the child reoxygenates. Retrieval is then reattempted, often after fragmenting the object or changing graspers, with constant communication with anesthesia.',
     'why_wrong': ['Correct.',
                   'Removing the scope loses visualization and access, and mask ventilation cannot pass a subglottic obstruction.',
                   'Tracheostomy takes too long in a desaturating child when the object can be displaced distally in seconds.',
                   'Higher pressures cannot ventilate past a complete subglottic obstruction, and pausing allows hypoxic arrest.'],
     'board_pearl': 'If a foreign body lodges centrally during extraction, push it distally to ventilate one lung, then retrieve it.',
     'curveball': 'What ventilation strategies can be used during rigid bronchoscopy for a foreign body?',
     'curveball_answer': 'A ventilating rigid bronchoscope allows positive pressure ventilation through its side port, with the eyepiece sealing the system; telescopes narrow the lumen and raise '
                         'resistance. Spontaneous ventilation under inhalational or intravenous anesthesia avoids pushing the object distally and is preferred by many for foreign bodies. Jet ventilation '
                         'is another option. The strategy is agreed between surgeon and anesthesiologist before starting.'},
    'v269_gen_afb_fnd': {'stem': 'A 3-year-old boy has had a cough and intermittent wheeze for 3 weeks, beginning the evening he choked on mixed nuts at dinner. Albuterol and an oral steroid course have not helped. He is '
             'afebrile with saturation of 97%, and there is a localized wheeze over the left lower chest. Chest radiography is normal. What is the best interpretation?',
     'choices': ['Normal radiographs exclude a foreign body, so asthma therapy should be continued',
                 'Foreign body is still likely, and bronchoscopy is warranted despite normal films',
                 'Persistent cough after choking is usually postviral, so reassess in 4 to 6 weeks',
                 'A barium swallow is the best test to show the location of an aspirated object'],
     'answer': 1,
     'explanation': 'A witnessed or reported choking episode is the most sensitive clue to an aspirated foreign body and should not be dismissed when imaging is normal. Nuts and other organic objects '
                    'are radiolucent, and indirect signs such as air trapping or atelectasis are often absent, especially early. Persistent focal wheeze unresponsive to asthma treatment adds weight. '
                    'Delayed diagnosis leads to pneumonia, bronchiectasis, and granulation that make extraction harder. Bronchoscopy is indicated; CT can help when the history is uncertain.',
     'why_wrong': ['Most aspirated nuts are radiolucent, and radiographs are normal in many children with airway foreign bodies.',
                   'Correct.',
                   'Choking at the onset of persistent focal wheeze is a foreign body until proven otherwise; delay invites pneumonia and granulation.',
                   'A barium swallow evaluates the esophagus and does not image an object in the bronchial tree.'],
     'board_pearl': 'A positive choking history outweighs a normal chest radiograph in suspected airway foreign body.',
     'curveball': 'What inspiratory-expiratory or decubitus radiograph findings can support ball-valve obstruction in a toddler?',
     'curveball_answer': 'In ball-valve obstruction, air enters around the object on inspiration but is trapped on expiration, so an expiratory film shows persistent hyperinflation of the affected lung '
                         'with mediastinal shift toward the normal side. In young children who cannot cooperate, lateral decubitus films substitute: the dependent lung should deflate, so failure of the '
                         'affected lung to deflate when down suggests air trapping.'},
    'v269_gen_afb_app': {'stem': 'A 5-year-old boy aspirated a small plastic toy piece 1 day ago, witnessed by his sister. He is comfortable on room air with mildly decreased breath sounds at the right base. CT of the '
             'chest shows a 6 mm object in the bronchus intermedius. His parents ask how it will be removed. What is the best definitive approach?',
     'choices': ['Awake flexible bronchoscopy with a retrieval basket in the clinic',
                 'Postural drainage with chest physiotherapy to cough the object out',
                 'Rigid bronchoscopy under general anesthesia with optical forceps',
                 'Observation with oral antibiotics, as small objects often pass'],
     'answer': 2,
     'explanation': 'Rigid bronchoscopy under general anesthesia is the standard for removing pediatric airway foreign bodies. The rigid scope secures and ventilates the airway, accommodates optical '
                    'forceps and telescopes, and lets the team withdraw the object, scope, and forceps together. Before starting, surgeon and anesthesiologist agree on spontaneous or controlled '
                    'ventilation and on a rescue plan if the object dislodges. After removal, the entire tracheobronchial tree is reinspected for residual fragments or a second object.',
     'why_wrong': ['Flexible scopes can retrieve some objects, but awake in a child they give no airway control or ventilation if the object dislodges.',
                   'Physiotherapy rarely clears a lodged object and risks moving it into the trachea, causing complete obstruction.',
                   'Correct.',
                   'Retained objects do not pass reliably and lead to pneumonia, granulation tissue, and bronchiectasis.'],
     'board_pearl': 'Pediatric airway foreign body: rigid bronchoscopy with a shared ventilation and rescue plan.',
     'curveball': 'Why should both lungs and the distal bronchi be inspected after the object is removed?',
     'curveball_answer': 'Objects may fragment during aspiration or extraction, and pieces can lodge in the opposite lung or more distal segments; multiple foreign bodies also occur in a small fraction '
                         'of cases. Reinspection identifies granulation tissue, mucosal injury, or retained secretions that need suction. Missing a second fragment leads to persistent symptoms and a '
                         'repeat anesthetic.'},
    'v269_gen_afb_snr': {'stem': 'A 6-year-old boy undergoes rigid bronchoscopy for a smooth 9 mm plastic bead in the left mainstem bronchus. During withdrawal, the bead is pulled off the forceps at the glottis, and '
             'ventilation abruptly fails. On direct laryngoscopy the bead is visible wedged between the vocal folds, with its upper half above them. Saturation is 80% and falling. What is the best next '
             'step?',
     'choices': ['Reinsert the bronchoscope and ventilate past the bead with high inflation pressure',
                 'Pause and allow the bead to clear with the next spontaneous breath or cough',
                 'Proceed directly to emergency tracheostomy below the obstructed glottis',
                 'Grasp it under direct laryngoscopy with forceps and remove it through the mouth'],
     'answer': 3,
     'explanation': 'Extraction can convert a distal partial obstruction into a complete central one, and the team must restore ventilation within seconds. When the object is visible at the glottis, the '
                    'fastest fix is controlled removal under direct laryngoscopy with Magill or optical forceps. If it cannot be grasped, it can be pushed back into the trachea and a mainstem bronchus '
                    'to ventilate one lung. Anesthesia and surgery communicate continuously, and a surgical airway is prepared in case neither maneuver works.',
     'why_wrong': ['Gas cannot pass a bead wedged in the glottis, and forcing the scope may impact it further or push it out of reach.',
                   'A wedged object will not clear on its own under anesthesia, and waiting allows hypoxic cardiac arrest.',
                   'Front-of-neck access is the backup if removal fails, but a visible object can be grasped faster than a tracheostomy can be done.',
                   'Correct.'],
     'board_pearl': 'Object lost at the glottis: grasp it if visible, push it distally if not, and have a surgical airway ready.',
     'curveball': 'How does a sharp foreign body, such as an open safety pin, change extraction orientation and mucosal-injury planning?',
     'curveball_answer': 'A sharp object is withdrawn with its point trailing, or with the point sheathed inside the bronchoscope, to avoid lacerating the airway. An open safety pin may be rotated so '
                         'the point faces distally, or closed, before removal. Afterward, the mucosa is inspected for lacerations or perforation, and chest imaging checks for pneumothorax or '
                         'pneumomediastinum.'},
    'v139_gen_02': {'stem': 'A 31-year-old teacher has 4 days of nasal congestion, clear rhinorrhea, sore throat, mild cough, and a low-grade fever that peaked at 37.9 C on day 1. She feels slightly better today. '
             'Examination shows erythematous nasal mucosa with clear secretions, normal tympanic membranes, and no tonsillar exudate. She asks for an antibiotic because of an important work trip. What '
             'is the best management?',
     'choices': ['Symptomatic care with saline, analgesics, and clear return precautions',
                 'Amoxicillin-clavulanate for 5 days to prevent bacterial sinusitis',
                 'Azithromycin for 3 days because of her upcoming travel schedule',
                 'Delayed amoxicillin prescription to fill if she is not better in 3 days'],
     'answer': 0,
     'explanation': 'Four days of congestion, clear rhinorrhea, sore throat, and cough that is already improving is a viral upper respiratory infection. Antibiotics do not shorten it or prevent '
                    'bacterial complications, and they cause adverse effects, C. difficile infection, and resistance. Bacterial sinusitis is suspected only with symptoms persisting 10 days or more '
                    'without improvement, or worsening after initial improvement. Stewardship here means explaining the expected course, symptomatic options, and when to return.',
     'why_wrong': ['Correct.',
                   'Antibiotics do not prevent bacterial sinusitis after a viral infection and add side effects and resistance.',
                   'A macrolide offers no benefit for a viral infection, and travel plans do not change the diagnosis.',
                   'Watchful waiting applies to possible bacterial sinusitis after 10 days of symptoms, not to an improving 4-day viral illness.'],
     'board_pearl': 'Viral URI: no antibiotics; suspect bacterial sinusitis only at 10 days without improvement or with double worsening.',
     'curveball': 'What sinusitis time course would support bacterial rather than viral disease, and what is first-line management then?',
     'curveball_answer': 'Under the AAO-HNSF adult sinusitis guideline, acute bacterial rhinosinusitis is diagnosed when purulent drainage with obstruction or facial pain persists 10 days or more '
                         'without improvement, or when symptoms worsen within 10 days after initial improvement. Even then, watchful waiting is first-line for uncomplicated disease, with amoxicillin '
                         'with or without clavulanate for 5 to 7 days if she fails to improve.'},
    'v147_gen_01': {'stem': 'A 54-year-old man is on postoperative day 4 after parotidectomy. He has 1 cm of mild erythema along the incision without spreading warmth, fluctuance, or drainage, and he has no fever. His '
             'white count is normal, and he feels well. The intern wants to start IV vancomycin and piperacillin-tazobactam to be safe. What is the best approach?',
     'choices': ['Start IV vancomycin and piperacillin-tazobactam for 7 days',
                 'Observe the wound closely without antibiotics and reassess daily',
                 'Start oral clindamycin for 10 days to prevent a wound infection',
                 'Open the incision at the bedside to look for a hidden collection'],
     'answer': 1,
     'explanation': 'Mild erythema confined to the incision, without spreading cellulitis, purulence, fever, or leukocytosis, is usually normal postoperative inflammation. Stewardship means '
                    'distinguishing inflammation from infection before treating, so he can be observed with daily wound checks. If infection develops, therapy is chosen for likely skin and salivary '
                    'flora, narrowed by culture when a collection is drained, and kept as short as the response allows. An abscess needs drainage rather than more antibiotics.',
     'why_wrong': ['Broad dual IV therapy for localized inflammation without infection adds toxicity, C. difficile risk, and resistance.',
                   'Correct.',
                   'Prophylactic oral antibiotics for incisional redness without infection are not supported and carry a high C. difficile risk.',
                   'There is no fluctuance or drainage to suggest a collection, so opening a healing incision causes unnecessary morbidity.'],
     'board_pearl': 'Treat surgical-site infection when signs support it; incisional redness alone is usually inflammation.',
     'curveball': 'How should culture data, source control, host risk, and early clinical response be used to narrow or stop empiric antibiotics?',
     'curveball_answer': 'Obtain cultures from drained pus rather than superficial swabs, then narrow to the organisms recovered once the patient improves. Adequate drainage often allows courses of 5 to '
                         '7 days. Immunocompromise, prosthetic material, or bacteremia may justify longer or broader therapy. Lack of improvement at 48 to 72 hours should prompt a search for an '
                         'undrained collection rather than reflexive broadening.'},
    'v273_gen_abx_fnd': {'stem': 'A 65-year-old woman undergoes total laryngectomy with primary pharyngeal closure and bilateral neck dissections. She received cefazolin and metronidazole before incision, with '
             'intraoperative redosing. On postoperative day 2 she is afebrile with clean wounds, and both neck drains remain in place. The team asks how long to continue prophylactic antibiotics. What '
             'is the best plan?',
     'choices': ['Continue IV antibiotics until all of the neck drains have been removed',
                 'Continue IV antibiotics for 7 days because the pharynx was opened',
                 'Stop prophylaxis within 24 hours of surgery despite drains remaining',
                 'Switch to oral ciprofloxacin until the pharyngeal leak study is done'],
     'answer': 2,
     'explanation': 'For clean-contaminated head and neck surgery, prophylaxis covering oral flora and anaerobes, such as cefazolin with metronidazole or ampicillin-sulbactam, is given within 60 minutes '
                    'before incision, redosed for long cases, and stopped within 24 hours. Studies show no benefit to longer courses, while extended therapy raises the risk of C. difficile, resistant '
                    'organisms, and drug toxicity. Drains, a tracheostomy, or a pending swallow study are not indications. New fever, wound changes, or a fistula would prompt reassessment and treatment.',
     'why_wrong': ['Drains do not justify continued antibiotics, and longer prophylaxis increases C. difficile and resistance without lowering infection rates.',
                   'Clean-contaminated head and neck cases gain no benefit from prophylaxis beyond 24 hours in the absence of infection.',
                   'Correct.',
                   'A fluoroquinolone adds toxicity without benefit, and a pending swallow study is not an indication for antibiotics.'],
     'board_pearl': 'Clean-contaminated head and neck prophylaxis: start before incision, stop within 24 hours, drains or not.',
     'curveball': 'Which contamination, infection, hardware, or host factors would convert prophylaxis into treatment and change its duration?',
     'curveball_answer': 'Active infection at surgery, such as an abscess, an existing fistula, or infected necrotic tumor, and a postoperative wound infection or pharyngocutaneous fistula convert '
                         'prophylaxis into treatment guided by cultures and source control. Infected hardware or osteomyelitis requires longer courses. A long operation changes redosing, and '
                         'immunosuppression may change agent choice, but neither alone extends prophylaxis.'},
    'v273_gen_abx_app': {'stem': 'A 38-year-old man had transcervical drainage of an odontogenic submandibular abscess and extraction of the infected molar 3 days ago and was started on IV vancomycin, cefepime, and '
             'metronidazole. He is now afebrile and eating, and the swelling is resolving. Cultures grow penicillin-susceptible viridans streptococci with mixed oral anaerobes, and blood cultures are '
             'negative. What is the best antibiotic plan?',
     'choices': ['Continue all three IV agents for 14 days to ensure complete eradication',
                 'Stop vancomycin but continue cefepime and metronidazole for 3 more weeks',
                 'Add IV fluconazole, since mixed oral flora can include Candida species',
                 'Narrow to oral amoxicillin-clavulanate to complete a short total course'],
     'answer': 3,
     'explanation': 'Broad empiric coverage is appropriate for a severe, undifferentiated deep neck infection, but once the abscess is drained, the tooth removed, and cultures show susceptible '
                    'streptococci and oral anaerobes, therapy should be narrowed. Amoxicillin-clavulanate covers both groups and allows oral step-down in a patient who is eating and improving. Duration '
                    'is guided by source control and response, often about 7 to 14 days in total. De-escalation lowers the risks of nephrotoxicity, C. difficile infection, and resistance.',
     'why_wrong': ['With source control and documented susceptible flora, continuing broad triple therapy adds toxicity and resistance without benefit.',
                   'Antipseudomonal cefepime is unnecessary here, and a multiweek course is not needed after drainage and clinical improvement.',
                   'Candida is not a pathogen in this culture or clinical picture, and empiric antifungals add toxicity and cost.',
                   'Correct.'],
     'board_pearl': 'After source control and cultures, de-escalate to the narrowest agent that covers the documented flora.',
     'curveball': 'What clinical deterioration would make you re-image or return for drainage instead of simply broadening antibiotics?',
     'curveball_answer': 'Recurrent fever, a rising white count, increasing swelling, new trismus or dysphagia, airway symptoms, chest pain, or persistent purulent drainage suggest an undrained or new '
                         'collection, spread to another space, or mediastinal extension. These prompt repeat contrast CT of the neck and chest and further drainage, because antibiotics cannot compensate '
                         'for undrained pus.'},
    'v273_gen_abx_snr': {'stem': 'A 46-year-old woman with acute myeloid leukemia and an absolute neutrophil count of 100 has had 4 days of fever and right facial pain despite IV cefepime and vancomycin. A colleague '
             'proposes adding meropenem and linezolid. Nasal endoscopy has not been performed since admission. Sinus CT shows right maxillary opacification with stranding of the pre-antral fat. What is '
             'the best next step?',
     'choices': ['Urgent nasal endoscopy with biopsy for histopathology and fungal culture',
                 'Switch to meropenem and linezolid and reassess the response in 72 hours',
                 'Start empiric voriconazole and avoid biopsy because of her neutropenia',
                 'Send a serum galactomannan and wait for the result before any procedure'],
     'answer': 0,
     'explanation': 'Clinical failure on broad antibacterials in a neutropenic host is information, not a reason to add more drugs. Fever, facial pain, and pre-antral fat stranding raise concern for '
                    'acute invasive fungal sinusitis. Urgent endoscopy looks for pale, insensate, or necrotic mucosa, and biopsy with frozen section, histopathology, and fungal culture distinguishes '
                    'Aspergillus from Mucorales. Treatment then combines surgical debridement, empiric amphotericin B until Mucorales is excluded, and reversal of immunosuppression where possible.',
     'why_wrong': ['Correct.',
                   'Stacking antibacterials ignores a likely fungal process and delays the diagnosis that determines treatment.',
                   'Voriconazole lacks activity against Mucorales, and avoiding biopsy delays debridement that can be lifesaving in invasive fungal disease.',
                   'Galactomannan is supportive but imperfect and does not detect mucormycosis; tissue diagnosis should not wait.'],
     'board_pearl': 'Fever on broad antibacterials in a neutropenic patient with sinus findings: scope and biopsy for invasive fungal disease.',
     'curveball': 'How should renal function, QT-prolonging drugs, marrow suppression, and drug interactions shape her definitive antimicrobial plan?',
     'curveball_answer': 'Liposomal amphotericin B is preferred over the conventional form to limit nephrotoxicity, with close electrolyte monitoring. Azoles such as voriconazole, posaconazole, and '
                         'isavuconazole inhibit CYP3A4, raising levels of chemotherapy agents and immunosuppressants, and most prolong the QT interval, although isavuconazole shortens it. Linezolid '
                         'causes marrow suppression. Pharmacy review and therapeutic drug monitoring balance efficacy and toxicity.'},
    'v139_gen_03': {'stem': 'A 61-year-old man is on postoperative day 1 after left modified radical neck dissection. Since nasogastric feeds started, his drain output has turned milky white and increased to 700 mL '
             'over 24 hours. The skin flaps are flat, and he is afebrile. The drain fluid triglyceride is 640 mg/dL. Which management is best now?',
     'choices': ['Remove the drain and apply a pressure dressing so the leak can seal on its own',
                 'MCT or fat-free feeds, closed drainage, octreotide, and early escalation if persistent',
                 'Continue the standard feeds and repeat triglyceride testing in 3 days to confirm',
                 'Thoracoscopic thoracic duct ligation today, before any conservative treatment'],
     'answer': 1,
     'explanation': 'Milky drainage that appears with enteral feeding after left neck dissection, with triglyceride above 100 mg/dL, confirms a chyle leak from the thoracic duct near the left venous '
                    'angle. Initial care reduces chyle flow and protects the patient: switch to fat-free or medium-chain triglyceride feeds, which bypass the lymphatics, maintain closed suction '
                    'drainage, consider pressure dressing and octreotide, and monitor volume, electrolytes, albumin, and lymphocytes. High output, often cited as over 500 to 1000 mL per day, or failure '
                    'to decline prompts early re-exploration or lymphatic intervention.',
     'why_wrong': ['Removing the drain allows chyle to collect under the flaps, causing seroma, infection, and flap compromise.',
                   'Correct.',
                   'Triglyceride above 100 mg/dL already confirms chyle, and continued long-chain fat feeding drives high flow.',
                   'Thoracoscopic duct ligation is a rescue for refractory leaks, not a day-1 step before conservative care.'],
     'board_pearl': 'Chyle leak: triglyceride above 100 mg/dL confirms it; output volume and trajectory drive escalation.',
     'curveball': 'His output stays above 1 L per day after a week of conservative care. What operative or interventional options exist?',
     'curveball_answer': 'Neck re-exploration with suture ligation or clipping of the leaking duct, often aided by preoperative enteral cream to make chyle visible, reinforced with fibrin sealant or a '
                         'local muscle flap such as the sternocleidomastoid or pectoralis major. Alternatives are interventional radiology thoracic duct embolization or disruption and, rarely, '
                         'thoracoscopic ligation of the duct above the diaphragm.'},
    'v140_gen_08': {'stem': 'A 58-year-old woman is on postoperative day 9 after left neck dissection. Despite a fat-free diet, a pressure dressing, and 5 days of octreotide, her chylous drain output remains about '
             '1,200 mL per day. Her sodium is 131 mmol/L, albumin has fallen to 2.6 g/dL, and her lymphocyte count is low. What is the best next step?',
     'choices': ['Raise octreotide to the maximum dose and add a firmer compression wrap',
                 'Remove the drain and rely on the pressure dressing to seal the leak',
                 'Neck re-exploration with duct ligation or thoracic duct embolization',
                 'Switch to TPN with nothing by mouth and reassess output in 2 weeks'],
     'answer': 2,
     'explanation': 'A chyle leak of more than about 1 L per day that persists despite an adequate conservative trial is unlikely to close on its own. Ongoing losses cause hyponatremia, hypoalbuminemia, '
                    'and lymphopenia with immunosuppression, as this patient shows. Definitive control is indicated: re-exploration of the left venous angle with ligation or clipping of the duct and '
                    "reinforcement with sealant or a muscle flap, or interventional radiology thoracic duct embolization, chosen by local expertise and the patient's fitness.",
     'why_wrong': ['Escalating medical therapy after 5 days of failure at this output rarely closes the leak and prolongs metabolic losses.',
                   'Removing the drain lets chyle collect under the flaps and risks wound breakdown, fistula, or chylothorax.',
                   'Correct.',
                   'TPN reduces flow, but 2 more weeks at this output risks malnutrition and immunosuppression when definitive options exist.'],
     'board_pearl': 'High-output chyle leak failing conservative care: proceed to re-exploration or thoracic duct embolization.',
     'curveball': 'Where is the thoracic duct typically encountered during left low-neck re-exploration?',
     'curveball_answer': 'The duct arches up from the thorax at about the level of C7, behind the carotid sheath and in front of the anterior scalene, phrenic nerve, vertebral vessels, and thyrocervical '
                         'trunk, then curves forward to enter the venous angle where the left internal jugular and subclavian veins meet. It often divides into several channels near its termination, so '
                         'more than one may need ligation.'},
    'v270_gen_chyle_fnd': {'stem': 'A 66-year-old man is on postoperative day 2 after left neck dissection of levels II to V. Drain output was 60 mL of serosanguineous fluid on day 1. After enteral feeds began this morning, '
             'the fluid turned opaque and milky and output rose to 280 mL over 12 hours. He is afebrile, and the flaps are flat. What is the most likely diagnosis?',
     'choices': ['Pharyngocutaneous salivary fistula', 'Early wound infection with purulent drainage', 'Lymphatic seroma from level II nodes', 'Thoracic duct injury with a chyle leak'],
     'answer': 3,
     'explanation': 'The thoracic duct carries chylomicron-rich lymph from the gut and empties into the left venous angle, so it is at risk during dissection of low levels IV and V on the left. Chyle '
                    'looks milky because of chylomicrons, and output rises sharply after enteral fat intake. Drainage that changes from serosanguineous to milky once feeds start, with rising volume, is '
                    'classic. Confirmation is a drain triglyceride above 100 mg/dL or higher than the serum level, or the presence of chylomicrons.',
     'why_wrong': ['A salivary fistula follows mucosal entry and drains cloudy saliva, often with fever and erythema, and does not rise with fat intake.',
                   'Purulent drainage comes with fever, erythema, and wound tenderness, and it typically appears later than day 2.',
                   'Seroma fluid is clear to straw-colored and does not turn milky with feeding; level II lymphatics do not carry chyle.',
                   'Correct.'],
     'board_pearl': 'Drain output that turns milky and rises once feeding starts after left neck dissection is chyle.',
     'curveball': 'Why is a right-sided cervical chyle leak still possible despite the usual left-sided teaching?',
     'curveball_answer': 'The right lymphatic duct drains the right head, neck, arm, and chest into the right venous angle, and in some patients the thoracic duct terminates bilaterally or on the right. '
                         'Right-sided chyle leaks are less common but well documented, so milky drainage after right level IV dissection should be evaluated and managed the same way.'},
    'v270_gen_chyle_snr': {'stem': 'A 72-year-old man with prior neck radiation underwent salvage left neck dissection and, on day 8, has 1,100 mL per day of chylous drainage despite medium-chain triglyceride feeds, '
             'octreotide, and a pressure dressing. Albumin is 2.4 g/dL, and lymphocytes are falling. He has severe COPD, and the irradiated neck is densely scarred. What is the best senior decision?',
     'choices': ['Lymphangiography with percutaneous thoracic duct embolization',
                 'Continue conservative care for 3 more weeks before any procedure',
                 'Open neck re-exploration through the irradiated, scarred field',
                 'Remove the drain and apply a compressive dressing to seal the leak'],
     'answer': 0,
     'explanation': 'Persistent high-output chyle loss despite an adequate conservative trial causes volume, protein, and lymphocyte depletion, so the senior priority is a short path to definitive '
                    'control. The method follows anatomy and risk. In a densely scarred, irradiated neck and a patient with severe lung disease, lymphangiography with percutaneous thoracic duct '
                    'embolization avoids reoperation and general anesthesia and has good success where available. Open re-exploration remains the alternative if embolization fails or is unavailable.',
     'why_wrong': ['Correct.',
                   'Persistent high output with falling albumin and lymphocytes is failure of conservative care; weeks more risk malnutrition and infection.',
                   'Re-exploration is an option, but dense irradiated scar raises risk to the phrenic nerve, vessels, and plexus, and the duct is hard to find.',
                   'Removing the drain allows chyle to collect under irradiated flaps, risking breakdown, fistula, and carotid exposure.'],
     'board_pearl': 'Refractory chyle leak in a hostile neck or poor surgical candidate: consider thoracic duct embolization.',
     'curveball': 'How would bilateral neck surgery or prior thoracic procedures alter localization and rescue planning?',
     'curveball_answer': 'Bilateral surgery raises the chance that the right lymphatic duct is involved or that leaks are bilateral, so lymphangiography or bilateral exploration helps localize the '
                         'source. Prior thoracic surgery or duct ligation can alter anatomy, block percutaneous access to the cisterna chyli, or divert flow through collaterals, making embolization '
                         'harder and favoring targeted neck exploration.'},
    'v139_gen_04': {'stem': 'At 2 AM, the on-call resident receives four pages at once: a 30-year-old with a peritonsillar abscess who is drinking fluids, a 7-year-old on day 6 after tonsillectomy whose blood-streaked '
             'saliva has stopped with normal vital signs, a 45-year-old with 2 days of sudden hearing loss, and a 61-year-old 6 hours after neck dissection with rapidly expanding swelling and new '
             'stridor. Who should be seen first?',
     'choices': ['The 7-year-old after tonsillectomy', 'The 61-year-old after neck dissection', 'The 30-year-old with a peritonsillar abscess', 'The 45-year-old with sudden hearing loss'],
     'answer': 1,
     'explanation': 'ENT triage ranks patients by how fast they can deteriorate and how irreversible the harm would be. An expanding neck hematoma with stridor after neck surgery can progress to '
                    'complete airway obstruction within minutes, and bedside decompression may be needed. The post-tonsillectomy child with a resolved sentinel bleed is next, because rebleeding can be '
                    'sudden, and should be placed in a monitored bed with IV access while waiting. The peritonsillar abscess and sudden hearing loss are urgent but stable.',
     'why_wrong': ['A resolved sentinel bleed with normal vital signs needs urgent monitored assessment, but it is not threatening the airway right now.',
                   'Correct.',
                   'A peritonsillar abscess in a patient drinking fluids is not an airway emergency and can be drained after the unstable patient.',
                   'Sudden hearing loss needs prompt steroids and audiometry within days, not minutes, and it is not life-threatening.'],
     'board_pearl': 'Triage by speed and irreversibility of harm: airway first, then hemorrhage risk, then urgent but stable problems.',
     'curveball': 'How would you protect the post-tonsillectomy child while you manage the neck hematoma?',
     'curveball_answer': 'Ask the ED to keep the child NPO in a monitored bed with IV access, blood count, and type and screen, sitting upright with suction available, and to page immediately if '
                         'bleeding recurs or heart rate rises. Alert anesthesia and the OR that a second case may follow, and see the child as soon as the hematoma is decompressed and the airway is '
                         'secure.'},
    'v143_gen_05': {'stem': 'A floor nurse calls at midnight about a 51-year-old woman 4 hours after total thyroidectomy. She is anxious, says her neck feels tight, and her voice sounds different, but saturation is '
             '97% and the dressing looks dry. The nurse asks for a lorazepam order so the patient can sleep. You are finishing a consult for a stable nasal fracture. What is the best response?',
     'choices': ['Order lorazepam and ask the nurse to call back if stridor develops',
                 'Order a serum calcium level and call back with the result to decide',
                 'Go to the bedside now and examine the neck with the dressing removed',
                 'Finish the nasal fracture consult first, then examine her within the hour'],
     'answer': 2,
     'explanation': 'Anxiety, neck tightness, and voice change in the first hours after thyroidectomy are early signs of a compressive hematoma, which can expand deep to the strap muscles before the '
                    'dressing shows anything. Normal saturation is falsely reassuring because hypoxemia is a late sign. This call requires immediate bedside evaluation with the dressing removed, ready '
                    'to open the wound if the neck is tense, and it outranks stable consults. Sedating the patient could blunt her airway reflexes and delay recognition.',
     'why_wrong': ['Sedation can mask and worsen airway compromise, and waiting for stridor means waiting for a late sign.',
                   'Hypocalcemia is unlikely at 4 hours and does not explain neck tightness and voice change, which suggest a hematoma.',
                   'Correct.',
                   'A stable nasal fracture can wait; neck tightness after thyroidectomy can progress to obstruction within minutes.'],
     'board_pearl': 'Anxiety and neck tightness after thyroidectomy are hematoma symptoms; examine the neck before sedating.',
     'curveball': 'If she deteriorates before transport to the OR, what immediate wound-decompression maneuver may be lifesaving?',
     'curveball_answer': 'Open the wound at the bedside: remove the dressing, cut the skin sutures or glue, open the platysma, and separate the strap muscles in the midline to release clot from around '
                         'the trachea. This relieves venous and lymphatic compression of the larynx and often restores breathing within minutes. Pack the wound loosely and take her to the OR for '
                         'hemostasis.'},
    'v270_gen_triage_fnd': {'stem': 'A junior resident on call has four pending consults, listed by page time: a stable ear canal foreign body, chronic dizziness, a routine tracheostomy tube change, and, paged last, a '
             '38-year-old woman with sinusitis-related orbital cellulitis who now has reduced visual acuity and an afferent pupillary defect. He plans to see them in order. Which principle should guide '
             'reordering?',
     'choices': ['Order of page arrival, so each consulting team is treated equally and fairly',
                 'Quickest consults first, so the list shrinks before the complex evaluation',
                 'Imaging availability, so whichever patient has a completed CT is seen first',
                 'Speed and irreversibility of harm, so the vision-threatened patient goes first'],
     'answer': 3,
     'explanation': 'ENT call triage is based on the consequence and speed of deterioration. Airway compromise, uncontrolled hemorrhage, threatened vision or neurologic function, rapidly progressive '
                    'deep infection, and time-sensitive foreign bodies such as button batteries can become irreversible before a full diagnosis is reached. Reduced acuity with an afferent pupillary '
                    'defect in orbital cellulitis signals optic nerve compromise, often from a subperiosteal or orbital abscess, and needs immediate evaluation, IV antibiotics, CT, and often urgent '
                    'drainage. The stable consults can wait.',
     'why_wrong': ['Arrival order ignores physiology; an earlier stable patient can safely wait while vision is lost within hours.',
                   'Clearing easy consults first delays care for the one patient whose harm is time-critical and irreversible.',
                   'Imaging logistics matter, but the deciding factor is the clinical threat, here optic nerve compromise.',
                   'Correct.'],
     'board_pearl': 'Triage ENT call by physiology: airway, bleeding, vision, neurologic function, invasive infection, and time-critical foreign bodies.',
     'curveball': 'A patient with a resolved post-tonsillectomy sentinel bleed is now stable. Why is that still higher priority than routine consults?',
     'curveball_answer': 'A sentinel bleed often precedes a larger hemorrhage within hours, and children compensate until they suddenly decompensate. The patient needs a monitored bed, IV access, labs '
                         'including type and screen, NPO status, and prompt ENT evaluation, ahead of stable problems such as cerumen, chronic dizziness, or a routine tube change, even though the '
                         'oropharynx is dry now.'},
    'v270_gen_triage_snr': {'stem': 'Three pages arrive together: a 64-year-old with bleeding granulation tissue around a mature tracheostomy that has now stopped, a 6-year-old with a post-tonsillectomy bleed now hemostatic '
             'with normal vital signs, and a 43-year-old with rapidly progressive floor-of-mouth swelling, drooling, and a muffled voice. You are the only resident in house. What is the best disposition '
             'strategy?',
     'choices': ['See the floor-of-mouth patient now and have the child monitored with IV access',
                 'See the child first, because pediatric bleeding outranks an adult airway problem',
                 "Send the floor-of-mouth patient to CT first while you examine the child's throat",
                 'Handle the tracheostomy first, since it is quick, then see the other two patients'],
     'answer': 0,
     'explanation': 'Senior triage weighs immediate threat and latent risk together. Progressive floor-of-mouth swelling with drooling and a muffled voice is a Ludwig-pattern infection with an evolving '
                    'airway threat, so it needs immediate airway-capable evaluation and early mobilization of anesthesia and the OR. The child with a resolved sentinel bleed carries hidden rebleeding '
                    'risk and should be placed in a monitored setting with IV access, labs, and NPO status, then seen next. The stopped tracheostomy granulation bleed can be deferred.',
     'why_wrong': ['Correct.',
                   "The child's bleed has stopped with normal vital signs, while the adult's airway is actively narrowing and can obstruct within minutes.",
                   'Sending a drooling patient with a muffled voice to lie supine in CT before airway assessment risks complete obstruction.',
                   'Quick tasks first delays the patient whose airway is deteriorating; stopped granulation bleeding around a mature stoma can wait.'],
     'board_pearl': 'Manage the active airway threat first while making sure the latent hemorrhage risk is monitored.',
     'curveball': 'What staffing or location change would you make if the floor-of-mouth patient cannot tolerate lying supine?',
     'curveball_answer': 'Keep the patient sitting upright with oxygen, avoid sedation, and move them to a resuscitation bay, ICU, or directly to the OR rather than the ward or CT. Call the attending '
                         'surgeon and an experienced anesthesiologist immediately, and have awake fiberoptic equipment and a tracheostomy tray at the bedside, with the neck marked for front-of-neck '
                         'access.'},
    'v139_gen_05': {'stem': 'A 49-year-old woman wakes after resection of a left glomus jugulare tumor with a breathy voice and coughing when she drinks water. Examination shows the palate elevating toward the right, '
             'left vocal fold paralysis, weak left shoulder shrug, and tongue deviation to the left on protrusion. Facial movement and hearing are unchanged from before surgery. Where do these deficits '
             'localize?',
     'choices': ['Cerebellopontine angle, cranial nerves VII and VIII with brainstem compression',
                 'Jugular foramen and adjacent hypoglossal canal, cranial nerves IX through XII',
                 'Cavernous sinus, cranial nerves III, IV, V1, V2, and VI beside the carotid',
                 'Superior orbital fissure, cranial nerves III, IV, V1, and VI to the orbit'],
     'answer': 1,
     'explanation': 'The deficits map to four nerves: the palate pulling to the healthy side and vocal fold paralysis reflect the vagus, dysphagia with aspiration reflects IX and X, a weak shrug '
                    'reflects the spinal accessory nerve, and tongue deviation toward the lesion reflects the hypoglossal nerve. CN IX, X, and XI exit through the jugular foramen, and XII exits nearby '
                    'through the hypoglossal canal, so combined deficits after jugular foramen surgery, Collet-Sicard syndrome, localize there. Patterns localize better than isolated deficits.',
     'why_wrong': ['A cerebellopontine angle lesion would affect facial movement and hearing, which are unchanged.',
                   'Correct.',
                   'Cavernous sinus lesions cause ophthalmoplegia and facial numbness, not palatal, laryngeal, shoulder, and tongue weakness.',
                   'Superior orbital fissure syndrome causes ophthalmoplegia and forehead numbness, without lower cranial nerve findings.'],
     'board_pearl': 'IX through XII together localize to the jugular foramen and hypoglossal canal: Collet-Sicard syndrome.',
     'curveball': 'What sympathetic finding would suggest a more extensive parapharyngeal or skull base lesion?',
     'curveball_answer': 'Ipsilateral Horner syndrome, with ptosis, miosis, and sometimes anhidrosis, indicates involvement of the cervical sympathetic chain, which lies in the poststyloid '
                         'parapharyngeal space beside the carotid. IX to XII palsies plus Horner syndrome, Villaret syndrome, point to a retrostyloid parapharyngeal lesion below the skull base rather '
                         'than a process confined to the jugular foramen.'},
    'v147_gen_02': {'stem': 'A 57-year-old man has 6 months of right pulsatile tinnitus and 2 months of hoarseness, choking on liquids, and difficulty lifting his right arm overhead. Examination shows a reddish mass '
             'behind the right tympanic membrane, right vocal fold paralysis, weak right trapezius, and right tongue atrophy. Facial sensation, limb strength, and coordination are normal. Where is the '
             'lesion?',
     'choices': ['Right lateral medulla in the vertebral artery territory',
                 'Right internal auditory canal and adjacent cerebellopontine angle',
                 'Right jugular foramen extending to the hypoglossal canal',
                 'Right carotid bifurcation in the neck at the hyoid level'],
     'answer': 2,
     'explanation': 'Pulsatile tinnitus with a red retrotympanic mass suggests a paraganglioma arising at the jugular bulb, a glomus jugulare. Its growth involves the nerves sharing the jugular foramen, '
                    'IX, X, and XI, producing dysphagia, hoarseness, and trapezius weakness, and medial extension to the hypoglossal canal adds tongue atrophy. Normal sensation, strength, and '
                    'coordination argue against a brainstem lesion. This cluster localizes to the jugular foramen region and calls for contrast MRI and CT of the skull base.',
     'why_wrong': ['Lateral medullary infarction is abrupt and causes crossed sensory loss, ataxia, and Horner syndrome, without tongue atrophy or trapezius weakness.',
                   'An internal auditory canal lesion would cause sensorineural hearing loss and facial weakness, not lower cranial nerve palsies.',
                   'Correct.',
                   'A carotid body tumor at the bifurcation can affect X and XII but does not produce a middle ear mass or pulsatile tinnitus.'],
     'board_pearl': 'Pulsatile tinnitus, a red retrotympanic mass, and IX to XII palsies point to glomus jugulare.',
     'curveball': 'What additional finding would indicate sympathetic chain involvement, and what would it imply about tumor extent?',
     'curveball_answer': 'Ipsilateral ptosis and miosis, with or without facial anhidrosis, indicate Horner syndrome from involvement of the sympathetic plexus on the internal carotid or the cervical '
                         'sympathetic chain. In a jugular foramen tumor, it implies extension into the poststyloid parapharyngeal space or the carotid canal, which changes the surgical approach and '
                         'raises the risk of carotid involvement.'},
    'v273_gen_cn_fnd': {'stem': 'A 44-year-old woman with a known left jugular foramen schwannoma has developed hoarseness and nasal regurgitation over 3 months. Examination shows reduced left gag sensation, the uvula '
             'pulled to the right on phonation, left vocal fold paralysis, and weak left shoulder elevation. Tongue protrusion is midline with normal bulk. Which localization best unifies these '
             'findings?',
     'choices': ['Hypoglossal canal, involving cranial nerve XII alone',
                 'Recurrent laryngeal nerve in the tracheoesophageal groove',
                 'Foramen ovale, involving the mandibular division of V',
                 'Jugular foramen, involving cranial nerves IX, X, and XI'],
     'answer': 3,
     'explanation': 'The jugular foramen transmits CN IX, X, and XI with the internal jugular vein. Reduced gag sensation reflects IX, the palate pulling to the healthy side and vocal fold paralysis '
                    'reflect X, and weak shoulder elevation reflects XI, together forming Vernet syndrome. A normal tongue shows that the hypoglossal nerve, which exits separately through the '
                    'hypoglossal canal, is spared, keeping the lesion within the foramen. Isolated vocal fold paralysis without palatal findings would instead point to a lower vagal or recurrent '
                    'laryngeal lesion.',
     'why_wrong': ['Hypoglossal canal involvement would cause tongue deviation and atrophy, and her tongue is normal.',
                   'A recurrent laryngeal lesion paralyzes the vocal fold but spares the palate, gag sensation, and trapezius.',
                   'Foramen ovale lesions cause jaw numbness and masticator weakness, not palatal, laryngeal, or shoulder deficits.',
                   'Correct.'],
     'board_pearl': 'IX, X, and XI palsies with a normal tongue is Vernet syndrome, localizing to the jugular foramen.',
     'curveball': 'What additional deficit would suggest extension from the jugular foramen into the hypoglossal canal?',
     'curveball_answer': 'Ipsilateral tongue weakness with deviation toward the lesion on protrusion, followed by fasciculations and atrophy, indicates hypoglossal nerve involvement. Because the '
                         'hypoglossal canal lies just anteromedial to the jugular foramen, this means medial extension and produces Collet-Sicard syndrome, IX to XII, which worsens swallowing and '
                         'changes the surgical and rehabilitation plan.'},
    'v273_gen_cn_app': {'stem': 'An overnight consult asks you to see a 68-year-old man for hoarseness before discharge. He has a breathy voice, coughs with thin liquids, and has a new right shoulder droop. Flexible '
             'laryngoscopy shows right vocal fold paralysis with pooled secretions, and the palate elevates poorly on the right. The primary team plans outpatient voice therapy. What is the best next '
             'step?',
     'choices': ['Full cranial nerve and swallow assessment with contrast MRI of the skull base',
                 'Outpatient voice therapy with repeat laryngoscopy in 3 months if unchanged',
                 'Contrast CT of the chest to trace the recurrent laryngeal nerve course only',
                 'Bedside injection laryngoplasty to improve glottic closure before discharge'],
     'answer': 0,
     'explanation': 'Vocal fold paralysis with palatal weakness and an accessory nerve deficit is not a recurrent laryngeal nerve problem. Palatal involvement places the vagal lesion above the '
                    'pharyngeal branch, near the skull base, and the shoulder droop adds CN XI, pointing to the jugular foramen or upper parapharyngeal space. The next steps are a complete cranial nerve '
                    'examination, including IX, XII, and sympathetic signs, an assessment of aspiration risk, and contrast MRI of the skull base and neck, with CT for bone detail.',
     'why_wrong': ['Correct.',
                   'Palatal weakness and shoulder droop show this is not isolated vocal fold paralysis, and delay could miss a skull base lesion.',
                   'Imaging only the chest suits isolated left-sided paralysis; palatal and accessory findings place this lesion high, near the skull base.',
                   'Injection may later help glottic closure, but it should not precede defining the cause and the broader aspiration risk.'],
     'board_pearl': 'Vocal fold paralysis plus palatal weakness means a high vagal lesion; image the skull base, not just the chest.',
     'curveball': 'Which examination findings would push the localization into the carotid space or sympathetic chain rather than the jugular foramen alone?',
     'curveball_answer': 'Ipsilateral Horner syndrome with ptosis and miosis, a pulsatile or palpable mass near the angle of the jaw, medial displacement of the lateral pharyngeal wall, or vagal and '
                         'hypoglossal weakness without accessory involvement suggest a lesion in the poststyloid parapharyngeal or carotid space below the skull base, such as a vagal paraganglioma or '
                         'schwannoma.'},
    'v273_gen_cn_snr': {'stem': 'A 66-year-old man treated with chemoradiation for nasopharyngeal carcinoma 4 years ago has 6 weeks of worsening dysphagia, a recent aspiration pneumonia, and right shoulder weakness. '
             'Examination shows right palatal weakness, right vocal fold paralysis, and right tongue atrophy with fasciculations. The junior resident orders a swallow study and an EMG of the shoulder. '
             'What is the best approach?',
     'choices': ['Attribute the deficits to late radiation neuropathy and arrange swallow therapy',
                 'Address aspiration risk and obtain contrast MRI of the skull base and neck',
                 'Order EMG of each affected muscle group before deciding on any imaging study',
                 'Inject the paralyzed vocal fold now and repeat the swallow study afterward'],
     'answer': 1,
     'explanation': 'Progressive palatal, vocal fold, accessory, and hypoglossal deficits over weeks form a single IX to XII pattern localizing to the jugular foramen, hypoglossal canal, or upper '
                    'parapharyngeal space, a structural red flag. After nasopharyngeal carcinoma, recurrence with skull base or perineural spread is the leading concern, and radiation neuropathy is a '
                    'diagnosis of exclusion. The senior approach first secures swallowing and airway safety with diet modification or NPO status, then obtains contrast MRI covering the skull base and '
                    "the nerves' extracranial course, with biopsy as indicated.",
     'why_wrong': ['Late radiation-induced cranial neuropathy occurs, but recurrence or skull base osteoradionecrosis must be excluded first by imaging.',
                   'Correct.',
                   'Fragmenting the workup by symptom delays a diagnosis that a single targeted imaging study can provide.',
                   'Medialization may help later, but it does not address the cause or the broader IX to XII aspiration risk.'],
     'board_pearl': 'Progressive IX to XII palsies are structural until imaging proves otherwise, even after radiation.',
     'curveball': 'How would abrupt onset over minutes, rather than progression over weeks, change the vascular urgency and imaging strategy?',
     'curveball_answer': 'Sudden lower cranial nerve palsies suggest a vascular cause, such as internal carotid or vertebral artery dissection compressing or devascularizing the nerves, or a brainstem '
                         'stroke. That calls for emergent CTA or MRA of the head and neck with diffusion-weighted brain MRI, stroke team involvement, and antithrombotic decisions, rather than routine '
                         'outpatient imaging.'},
}
