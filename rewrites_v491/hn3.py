"""v491 rewrites: Head & Neck Oncology part 3 (hn3)."""

REWRITES = {'v138_hn_18': {'stem': 'A 49-year-old woman reports 6 months of muffled voice and new snoring. '
                        'She has no dysphagia, otalgia, or cranial neuropathy. The left soft '
                        'palate bulges medially under normal mucosa, and the neck is unremarkable. '
                        'MRI shows a 3.5-cm lobulated, T2-bright, enhancing mass anterior to the '
                        'styloid process that pushes the parapharyngeal fat medially and the '
                        'internal carotid artery posteriorly, without flow voids. Which diagnosis '
                        'is most likely?',
                'choices': ['Schwannoma of the vagus nerve',
                            'Pleomorphic adenoma',
                            'Glomus vagale paraganglioma',
                            'Retropharyngeal nodal metastasis'],
                'answer': 1,
                'explanation': 'The styloid process and tensor-vascular-styloid fascia divide the '
                               'parapharyngeal space. Prestyloid masses are mostly salivary in '
                               'origin, and pleomorphic adenoma of the deep parotid lobe or minor '
                               'salivary rests is the most common parapharyngeal tumor overall. '
                               'The deciding clues are the prestyloid location and posterior '
                               'displacement of the carotid; poststyloid lesions arise behind or '
                               'around the carotid sheath and push it anteriorly. A lobulated, '
                               'T2-bright mass without flow voids fits a benign salivary neoplasm.',
                'why_wrong': ['A vagal schwannoma sits in the poststyloid space and displaces the '
                              'internal carotid artery anteriorly while splaying it from the '
                              'jugular vein.',
                              'Correct.',
                              'A vagal paraganglioma is poststyloid, displaces the carotid '
                              'anteriorly, and typically shows flow voids with a salt-and-pepper '
                              'appearance on MRI.',
                              'Retropharyngeal nodes lie medial to the carotid behind the pharynx '
                              'and would usually accompany a known mucosal primary, not a '
                              'prestyloid mass.'],
                'board_pearl': 'Prestyloid mass pushing the carotid posteriorly is salivary until '
                               'proven otherwise; poststyloid pushes it anteriorly.',
                'curveball': "The same patient's MRI instead showed a poststyloid mass pushing the "
                             'internal carotid anteriorly with flow voids. How does the '
                             'differential and workup change?',
                'curveball_answer': 'A poststyloid mass is neurogenic or vascular: paraganglioma '
                                    '(flow voids, intense enhancement) or schwannoma. Workup '
                                    'shifts to vascular imaging and plasma free metanephrines '
                                    'before surgery, with no needle biopsy of a suspected '
                                    'paraganglioma. Genetic counseling for SDHx variants is '
                                    'reasonable, and counseling must cover lower cranial nerve and '
                                    'sympathetic deficits.'},
 'v143_hno_05': {'stem': 'A 57-year-old man has a parapharyngeal mass found on CT done for sinus '
                         'symptoms. He is asymptomatic, and facial nerve function is normal. MRI '
                         'shows a 4-cm prestyloid mass that is dumbbell-shaped, widens the '
                         'stylomandibular tunnel, and has no fat plane separating it from the '
                         'major salivary gland lateral to the tunnel. The internal carotid artery '
                         'is displaced posteriorly. What is the most likely site of origin?',
                 'choices': ['Deep lobe of the parotid gland',
                             'Vagus nerve within the carotid sheath',
                             'Minor salivary rest in the pharyngeal wall',
                             'Cervical sympathetic chain'],
                 'answer': 0,
                 'explanation': 'Prestyloid tumors are usually salivary, and the key preoperative '
                                'question is whether they arise from the deep parotid lobe or from '
                                'extraparotid minor salivary tissue. A dumbbell shape through a '
                                'widened stylomandibular tunnel with loss of the fat plane between '
                                'the mass and the gland means deep-lobe parotid origin. That '
                                'matters operatively: the facial nerve must be identified, usually '
                                'with a transcervical-transparotid approach. A preserved fat plane '
                                'around a round mass favors a minor salivary origin.',
                 'why_wrong': ['Correct.',
                               'A vagal schwannoma is poststyloid, separates the carotid from the '
                               'jugular vein, and pushes the carotid anteriorly rather than '
                               'posteriorly.',
                               'A minor salivary tumor is typically surrounded by a preserved fat '
                               'plane and does not extend through the stylomandibular tunnel to '
                               'join the gland.',
                               'A sympathetic chain schwannoma is poststyloid and displaces the '
                               'carotid sheath anteriorly rather than posteriorly.'],
                 'board_pearl': 'Dumbbell prestyloid tumor through the stylomandibular tunnel '
                                'equals deep-lobe parotid origin; plan facial nerve dissection.',
                 'curveball': 'Imaging instead shows the mass abutting the skull base and partly '
                              'surrounding the internal carotid artery. How does that change '
                              'planning and counseling?',
                 'curveball_answer': 'Skull-base extension or carotid contact calls for vascular '
                                     'imaging, and if carotid sacrifice is conceivable, balloon '
                                     'test occlusion. Exposure may require a '
                                     'transcervical-transparotid approach with mandibulotomy or a '
                                     'skull-base team. Counseling covers stroke, lower cranial '
                                     'nerve and facial nerve risk, and the possibility of subtotal '
                                     'removal, since pleomorphic adenoma rupture raises recurrence '
                                     'risk.'},
 'v221_hn_pps_snr': {'stem': 'A 58-year-old man has a 5-cm right poststyloid parapharyngeal mass '
                             'that extends to the jugular foramen and separates the internal '
                             'carotid artery from the internal jugular vein. He has mild '
                             'hoarseness, and flexible laryngoscopy shows a sluggish right vocal '
                             'fold with full contralateral function. Plasma metanephrines are '
                             'normal. Surgical resection is being considered. What is the most '
                             'appropriate next step before choosing an approach?',
                     'choices': ['Transoral core needle biopsy to confirm histology',
                                 'Transoral robotic excision to avoid a neck incision',
                                 'Upfront stereotactic radiosurgery to the whole mass',
                                 'CTA or MRA plus temporal bone CT to map vessels and skull base'],
                     'answer': 3,
                     'explanation': 'A poststyloid mass splaying the carotid and jugular vein is a '
                                    'vagal schwannoma or paraganglioma, and both sit among the '
                                    'carotid sheath and cranial nerves IX to XII. Before choosing '
                                    'transcervical, transparotid, or combined skull-base exposure, '
                                    'the surgeon needs vascular imaging and bone detail at the '
                                    'jugular foramen. The existing vagal weakness also changes '
                                    'counseling: resection will likely produce a complete '
                                    'paralysis, so swallowing rehabilitation and possible '
                                    'medialization should be planned, and observation or radiation '
                                    'may be weighed.',
                     'why_wrong': ['Needling a possibly hypervascular poststyloid lesion through '
                                   'the pharynx risks bleeding and rarely adds to characteristic '
                                   'imaging.',
                                   'Transoral access gives poor control of the carotid and jugular '
                                   'foramen for a large poststyloid tumor that reaches the skull '
                                   'base.',
                                   'Radiation may be an option later, but committing to treatment '
                                   'before defining the anatomy and lesion type skips essential '
                                   'characterization.',
                                   'Correct.'],
                     'board_pearl': 'Poststyloid tumor: map vessels and skull base, assess lower '
                                    'cranial nerves, and counsel on expected deficits before '
                                    'resection.',
                     'curveball': 'How would a vagal schwannoma differ from a sympathetic chain '
                                  'schwannoma in vessel displacement and in what you warn the '
                                  'patient about?',
                     'curveball_answer': 'A vagal schwannoma arises between the carotid and '
                                         'jugular vein and splays them apart; resection risks '
                                         'vocal fold paralysis and aspiration. A sympathetic chain '
                                         'schwannoma lies posteromedial and pushes the carotid and '
                                         'jugular anteriorly together without separating them; '
                                         'resection risks Horner syndrome and first bite '
                                         'syndrome.'},
 'v138_hn_19': {'stem': 'A 57-year-old man with a T3N2b supraglottic SCC chooses larynx '
                        'preservation. His renal function and hearing are normal. The radiation '
                        'oncologist recommends 70 Gy in 35 fractions with high-dose cisplatin on '
                        'days 1, 22, and 43. He asks why adding a drug that causes nausea and '
                        'kidney risk is worthwhile when radiation alone can treat the tumor. Which '
                        'mechanism best explains the benefit?',
                'choices': ['It sensitizes tumor cells to radiation DNA damage',
                            'It mainly clears distant micrometastatic disease',
                            'It shrinks the tumor so hypoxic cells reoxygenate first',
                            'It protects mucosa so a higher total dose can be given'],
                'answer': 0,
                'explanation': 'Concurrent cisplatin acts as a radiosensitizer: platinum adducts '
                               'impair repair of radiation-induced DNA damage and hit cells in '
                               'resistant phases. The meta-analysis of chemotherapy in head and '
                               'neck cancer showed that the survival gain from concurrent '
                               'chemotherapy comes mostly from better locoregional control, with '
                               'little effect on distant metastasis. The price is more mucositis, '
                               'nephrotoxicity, ototoxicity, and late dysphagia, which is why '
                               'patient fitness matters.',
                'why_wrong': ['Correct.',
                              'Concurrent chemotherapy has a small effect on distant failure; its '
                              'main benefit is locoregional control, not clearing micrometastases.',
                              'Debulking before radiation describes induction chemotherapy, not '
                              'cisplatin given concurrently during the radiation course.',
                              'Cisplatin increases mucositis rather than protecting mucosa, and '
                              'total dose stays at the standard 70 Gy.'],
                'board_pearl': 'Concurrent cisplatin is a radiosensitizer; its survival benefit '
                               'comes mainly from locoregional control.',
                'curveball': 'His creatinine clearance is 40 mL/min and he has hearing loss '
                             'needing aids. What are the reasonable alternatives to high-dose '
                             'cisplatin?',
                'curveball_answer': 'He is cisplatin-ineligible. Options include radiation with '
                                    'cetuximab, carboplatin-based regimens, or weekly docetaxel, '
                                    'which improved outcomes over radiation alone in a '
                                    'cisplatin-ineligible trial, or radiation alone if frail. '
                                    'Cetuximab is inferior to cisplatin in eligible patients, so '
                                    'these are used only when cisplatin is contraindicated.'},
 'v145_hn_15': {'stem': 'A 64-year-old woman undergoes partial glossectomy and ipsilateral neck '
                        'dissection for oral tongue SCC. Pathology shows a 3.2-cm tumor with 9-mm '
                        'depth of invasion, perineural invasion, and lymphovascular invasion. '
                        'Margins are clear at 6 mm. Two of 31 nodes are positive, and one shows '
                        'extranodal extension. She is fit with normal renal function. Which '
                        'pathologic finding most strongly supports adding concurrent cisplatin to '
                        'postoperative radiation?',
                'choices': ['Capsular spread in a positive node',
                            'Lymphovascular invasion within the tumor',
                            'Perineural invasion at the primary site',
                            'Two positive nodes on the dissected side'],
                'answer': 0,
                'explanation': 'The pooled analysis of the EORTC 22931 and RTOG 9501 trials showed '
                               'that the benefit of adding concurrent cisplatin to postoperative '
                               'radiation is concentrated in patients with extranodal extension or '
                               'a positive margin. Perineural invasion, lymphovascular invasion, '
                               'depth, and multiple positive nodes are intermediate-risk features '
                               'that justify postoperative radiation but do not by themselves '
                               "mandate chemotherapy. This patient's margins are clear, so the "
                               'capsular spread in one node is the deciding indication.',
                'why_wrong': ['Correct.',
                              'Lymphovascular invasion supports adjuvant radiation, yet trial data '
                              'do not show that it alone warrants adding chemotherapy.',
                              'Perineural invasion is an indication for postoperative radiation, '
                              'but by itself it does not establish a benefit from concurrent '
                              'cisplatin.',
                              'Multiple positive nodes without extranodal extension indicate '
                              'radiation, with chemotherapy considered case by case rather than '
                              'routinely.'],
                'board_pearl': 'Positive margin or extranodal extension: postoperative '
                               'chemoradiation; other adverse features: postoperative radiation '
                               'alone.',
                'curveball': 'How should the anticipated radiation shape her dental care and '
                             'reconstruction choices before treatment begins?',
                'curveball_answer': 'Dental evaluation should occur before radiation, ideally '
                                    'before or during surgery, with extraction of nonrestorable '
                                    'teeth in the field about 2 weeks before radiation and '
                                    'lifelong fluoride trays. Reconstruction should use '
                                    'well-vascularized tissue that tolerates radiation and '
                                    'anticipate flap shrinkage. Delays in wound healing should be '
                                    'avoided so radiation starts within about 6 weeks.'},
 'v228_hn_rt_fnd': {'stem': 'A 60-year-old man with a T2N1 base of tongue SCC is scheduled for 70 '
                            'Gy over 7 weeks in 35 daily fractions. He asks why he cannot receive '
                            'the same total dose in a single session or a few large treatments to '
                            'save travel. He has diabetes and works full time. Which radiobiologic '
                            'principle best explains dividing the dose into many small fractions?',
                    'choices': ['Small fractions keep tumor cells hypoxic and thus more sensitive',
                                'Normal tissues repair sublethal damage between fractions',
                                'Large single doses spare late-responding bone and nerve',
                                'Daily treatment prevents tumor repopulation over 7 weeks'],
                    'answer': 1,
                    'explanation': 'Fractionation exploits the 4 Rs. Between fractions, normal '
                                   'tissues, especially late-responding ones such as nerve, bone, '
                                   'and connective tissue, repair sublethal damage. Tumor cells '
                                   'redistribute into sensitive cell-cycle phases and hypoxic '
                                   'cores reoxygenate. Small daily doses therefore widen the '
                                   'therapeutic window and allow a curative cumulative dose. Large '
                                   'fractions mainly harm late-responding normal tissue, and '
                                   'repopulation is a cost of long treatment time that '
                                   'fractionation does not prevent.',
                    'why_wrong': ['Hypoxia makes tumor cells two to three times more resistant; '
                                  'fractionation helps because tumors reoxygenate between '
                                  'treatments.',
                                  'Correct.',
                                  'Late-responding tissues are the most sensitive to large '
                                  'fraction sizes, which is why hypofractionation raises the risk '
                                  'of late toxicity.',
                                  'Repopulation accelerates as treatment goes on; fractionation '
                                  'does not stop it, and long courses or gaps make it worse.'],
                    'board_pearl': 'Fractionation spares late-responding normal tissue through '
                                   'repair, while reoxygenation and redistribution sensitize the '
                                   'tumor.',
                    'curveball': 'Why might twice-daily hyperfractionated radiation allow a higher '
                                 'total dose, and has it beaten standard chemoradiation?',
                    'curveball_answer': 'Smaller fractions spare late-responding tissues, so a '
                                        'higher total dose can be given for the same late '
                                        'toxicity, and accelerated schedules shorten overall time '
                                        'to limit repopulation. Altered fractionation improved '
                                        'control over standard radiation alone, but RTOG 0129 '
                                        'showed no advantage over standard fractionation when both '
                                        'were given with concurrent cisplatin.'},
 'v228_hn_rt_app': {'stem': 'A 59-year-old man undergoes partial glossectomy, ipsilateral neck '
                            'dissection, and radial forearm flap reconstruction for a pT2N2b oral '
                            'tongue SCC. Margins are clear but close at 3 mm. Three level II and '
                            'III nodes are positive, and one level II node shows extranodal '
                            'extension. He is fit for cisplatin. Which description of the '
                            'postoperative radiation plan is most accurate?',
                    'choices': ['Highest dose to the node with capsular spread, with bed and neck '
                                'covered',
                                'Primary bed only, because the involved neck was fully dissected',
                                'Uniform 50 Gy elective dose to the primary bed and both necks',
                                'Dissected neck only, because the primary margins are negative'],
                    'answer': 0,
                    'explanation': 'Postoperative fields are built from pathology and surgical '
                                   'anatomy. The tumor bed, the flap interface, and the dissected '
                                   'neck are treated, usually to about 60 Gy, with escalation to '
                                   'about 66 Gy in regions of highest risk such as extranodal '
                                   'extension or a positive margin. At-risk undissected drainage '
                                   'receives elective dose. Neck dissection does not remove the '
                                   'need to irradiate an involved neck, and extranodal extension '
                                   'also supports concurrent cisplatin in a fit patient.',
                    'why_wrong': ['Correct.',
                                  'An involved neck with extranodal extension carries high '
                                  'regional recurrence risk despite dissection and must be '
                                  'included in the field.',
                                  'An elective 50 Gy dose underdoses a resected bed and a neck '
                                  'with extranodal extension, which need about 60 to 66 Gy.',
                                  'A close-margin primary bed with perineural and nodal risk still '
                                  'needs adjuvant dose; dropping the primary invites local '
                                  'recurrence.'],
                    'board_pearl': 'Postoperative radiation: about 60 Gy to bed and neck, about 66 '
                                   'Gy where there is extranodal extension or a positive margin.',
                    'curveball': "How can the surgeon's operative choices help or hinder the "
                                 'radiation oncologist in defining the postoperative target?',
                    'curveball_answer': 'Surgical clips at the resection margins, an operative '
                                        'note or diagram of the original tumor extent, and direct '
                                        'communication about close or positive areas help define '
                                        'the high-risk volume. Flaps move and distort the native '
                                        'anatomy, so the flap-tumor bed interface must be '
                                        'included. Wound complications that delay radiation beyond '
                                        'about 6 weeks also hinder treatment.'},
 'v228_hn_rt_snr': {'stem': 'A 62-year-old man completed 70 Gy with cisplatin for a right tonsil '
                            'SCC 20 months ago. He now has a biopsy-proven 2.5-cm recurrence in '
                            'the right parapharyngeal space that contacts the internal carotid '
                            'artery over about 120 degrees and lies near the cervical spinal cord. '
                            'PET-CT shows no distant disease. Salvage surgery is judged high risk. '
                            'What is the most important step before offering re-irradiation?',
                    'choices': ['Repeat a full 70 Gy course, since tissues recover after a year',
                                'Accept the clean PET-CT as proof that re-irradiation will be safe',
                                'Use stereotactic radiation, since steep dose falloff removes the '
                                'risk',
                                'Retrieve the prior plan and sum cumulative dose to cord and '
                                'carotid'],
                    'answer': 3,
                    'explanation': 'Re-irradiation can control selected recurrences, but it '
                                   'carries serious risks: carotid blowout, soft-tissue necrosis, '
                                   'osteoradionecrosis, myelopathy, and severe dysphagia. Safe '
                                   'planning starts with reconstructing the original dose '
                                   'distribution so cumulative dose to the cord, carotid, and '
                                   'mucosa can be estimated. That estimate is weighed with the '
                                   'interval since treatment, target size, carotid involvement, '
                                   'performance status, and alternatives such as salvage surgery '
                                   'or systemic therapy in multidisciplinary review.',
                    'why_wrong': ['Normal tissue recovers only partly, and a second full course '
                                  'without dose accounting risks myelopathy and carotid rupture.',
                                  'PET-CT addresses distant spread but says nothing about '
                                  'cumulative normal-tissue dose, which determines whether '
                                  're-irradiation is safe.',
                                  'Stereotactic radiation can reduce treated volume, but blowout '
                                  'risk remains substantial near an encased or contacted carotid.',
                                  'Correct.'],
                    'board_pearl': 'Before re-irradiation, obtain the prior dose plan and estimate '
                                   'cumulative dose to cord and carotid.',
                    'curveball': 'Which features of this recurrence or its treatment would most '
                                 'increase the risk of carotid blowout after re-irradiation?',
                    'curveball_answer': 'Risk rises with tumor surrounding the carotid by more '
                                        'than about 180 degrees, high cumulative carotid dose, '
                                        'ulceration or skin and mucosal breakdown over the vessel, '
                                        'prior neck dissection or flap loss leaving the carotid '
                                        'exposed, and stereotactic schedules given on consecutive '
                                        'days. Pharyngocutaneous fistula and infection further '
                                        'raise risk.'},
 'v138_hn_20': {'stem': 'A 56-year-old man has SCC of the right mandibular alveolar ridge invading '
                        'the marrow. Resection will remove an 8-cm segment of the body from the '
                        'canine to the angle, plus a 4 x 5-cm area of floor-of-mouth and gingival '
                        'mucosa. He has no prior radiation. Both feet have palpable pulses, and CT '
                        'angiography shows normal three-vessel runoff. Which reconstruction is '
                        'most appropriate?',
                'choices': ['Reconstruction plate with a pectoralis major myocutaneous flap',
                            'Anterolateral thigh free flap without a bony component',
                            'Radial forearm free flap over a bridging reconstruction plate',
                            'Fibula osteocutaneous free flap'],
                'answer': 3,
                'explanation': 'A segmental mandibular defect needs restored bony continuity, and '
                               'the mucosal loss needs thin lining. The fibula provides up to '
                               'about 25 cm of bicortical bone that tolerates osteotomies and '
                               'dental implants, and its septocutaneous skin paddle replaces the '
                               'floor-of-mouth mucosa. Normal leg runoff on CT angiography clears '
                               'the donor site. Soft-tissue flaps over plates are reserved for '
                               'poor candidates because plate exposure and fracture are common, '
                               'especially in anterior defects.',
                'why_wrong': ['A plate with a pectoralis flap is a fallback for medically unfit '
                              'patients and has high rates of plate exposure and fracture.',
                              'A thigh flap restores soft tissue but leaves a segmental gap, '
                              'causing mandibular drift, malocclusion, and poor cosmesis.',
                              'A radial forearm flap over a plate replaces lining but not bone, '
                              'and plate extrusion risk is high over an 8-cm span.',
                              'Correct.'],
                'board_pearl': 'Segmental mandibular defect with lining loss in a fit patient: '
                               'fibula osteocutaneous free flap.',
                'curveball': 'When would a scapular system flap be preferable to the fibula for '
                             'this defect?',
                'curveball_answer': 'A scapular or scapular tip flap from the subscapular system '
                                    'is preferred when the legs are unsuitable, such as '
                                    'peroneal-dominant runoff or severe peripheral arterial '
                                    'disease, in elderly patients needing early mobility, or when '
                                    'large independent soft-tissue paddles are needed. Its '
                                    'drawbacks are thinner bone for implants and the need for '
                                    'repositioning, which prevents two-team harvest.'},
 'v140_hn_10': {'stem': 'A 52-year-old man undergoes total glossectomy with laryngeal preservation '
                        'for a T4a oral tongue SCC. The mandible is intact, and the floor of mouth '
                        'resection leaves a large dead space beneath the palate. He has a body '
                        'mass index of 26 and normal leg vascular examination. The goals are to '
                        'fill the oral cavity, contact the palate, and help propel the bolus. '
                        'Which reconstruction best meets these goals?',
                'choices': ['Bulky anterolateral thigh free flap',
                            'Split-thickness skin graft to the floor of mouth',
                            'Radial forearm fasciocutaneous free flap',
                            'Fibula osteocutaneous free flap'],
                'answer': 0,
                'explanation': 'After total glossectomy the functional need is volume. A bulky '
                               'neotongue that contacts the palate restores oral containment, '
                               'helps drive the bolus, and protects the larynx from aspiration. '
                               'The anterolateral thigh flap, harvested with a cuff of vastus '
                               'lateralis when needed, supplies adjustable bulk and a large skin '
                               'paddle with low donor morbidity; a rectus abdominis flap is an '
                               'alternative. The flap should be overcorrected because denervated '
                               'muscle atrophies after surgery and radiation.',
                'why_wrong': ['Correct.',
                              'A skin graft provides no volume, leaving a dead space that cannot '
                              'contact the palate or propel food.',
                              'The radial forearm flap is thin and pliable, ideal for partial '
                              'glossectomy, but too small to fill a total glossectomy defect.',
                              'The mandible is intact, so vascularized bone is unnecessary and the '
                              'fibula skin paddle cannot supply adequate bulk.'],
                'board_pearl': 'Total glossectomy needs bulk: anterolateral thigh or rectus, '
                               'overcorrected to allow for atrophy.',
                'curveball': 'If he also needed a segmental mandibulectomy, how would donor '
                             'selection change?',
                'curveball_answer': 'He would need both vascularized bone and large-volume soft '
                                    'tissue. Options include a fibula for the mandible plus a '
                                    'second free flap such as an anterolateral thigh for the '
                                    'tongue, or a single subscapular system flap combining '
                                    'scapular bone with latissimus or parascapular soft tissue on '
                                    'one pedicle. Recipient vessel planning becomes critical.'},
 'v225_hn_recon_fnd': {'stem': 'A 61-year-old man undergoes resection of an anterior '
                               'floor-of-mouth SCC with marginal mandibulectomy that leaves an '
                               'intact inferior mandibular rim. The defect is a 4 x 5-cm area of '
                               'lining with exposed cancellous bone, and the tongue is spared. He '
                               'has no prior radiation, and the Allen test is normal. A junior '
                               'resident proposes a fibula flap because bone was removed. Which '
                               'reconstruction best matches this defect?',
                       'choices': ['Radial forearm fasciocutaneous free flap',
                                   'Pectoralis major myocutaneous flap',
                                   'Fibula osteocutaneous free flap',
                                   'Split-thickness skin graft with a bolster'],
                       'answer': 0,
                       'explanation': 'Reconstruction is defect-driven: identify what is missing, '
                                      'then choose the simplest option that restores it reliably. '
                                      'A marginal mandibulectomy preserves continuity, so the true '
                                      'defect is thin lining over bone in a mobile floor of mouth. '
                                      'The radial forearm flap supplies thin, pliable, potentially '
                                      'sensate tissue that covers bone, resists radiation, and '
                                      'does not tether the tongue. Choosing a favorite flap rather '
                                      'than analyzing the missing components leads to excess bulk '
                                      'or donor morbidity.',
                       'why_wrong': ['Correct.',
                                     'A pectoralis flap is bulky and tends to pull down and tether '
                                     'the anterior floor of mouth and tongue.',
                                     'Mandibular continuity is intact, so vascularized bone adds '
                                     'donor morbidity without restoring a missing component.',
                                     'A skin graft over exposed cancellous bone in a field likely '
                                     'to be irradiated has a high risk of failure and '
                                     'contracture.'],
                       'board_pearl': 'Analyze the defect first: marginal mandibulectomy needs '
                                      'lining, not bone; segmental needs vascularized bone.',
                       'curveball': 'Which mandibular and midface defects truly require '
                                    'vascularized bone rather than soft tissue alone?',
                       'curveball_answer': 'Anterior segmental defects crossing the symphysis need '
                                           'vascularized bone because soft tissue over a plate '
                                           'causes extrusion and the Andy Gump deformity. Lateral '
                                           'segmental defects in fit patients, especially those '
                                           'planned for radiation or implants, benefit as well. In '
                                           'the midface, large palatomaxillary or orbital floor '
                                           'defects may need fibula or scapular tip bone.'},
 'v225_hn_recon_app': {'stem': 'A 66-year-old woman has a retromolar trigone SCC invading the '
                               'mandible. Planned resection removes 7 cm of mandible from the '
                               'parasymphysis to the angle, plus a 5 x 4-cm area of buccal and '
                               'floor-of-mouth mucosa. She wants dental implants later. Leg CT '
                               'angiography is normal, and she has not been irradiated. The '
                               'surgical team debates how to restore both the bone and the lining. '
                               'Which reconstruction is most appropriate?',
                       'choices': ['Fibula osseous flap with primary closure of the mucosa',
                                   'Fibula flap with a septocutaneous skin paddle for lining',
                                   'Nonvascularized iliac crest graft with a tongue flap',
                                   'Radial forearm flap with a reconstruction plate bridge'],
                       'answer': 1,
                       'explanation': 'This composite defect has two missing components: '
                                      'mandibular continuity and intraoral lining. A fibula with a '
                                      'skin paddle based on septocutaneous perforators through the '
                                      'posterior crural septum restores both on one pedicle, and '
                                      'the bone accepts osteotomies and implants. A 5 x 4-cm '
                                      'lining defect cannot be closed primarily without tethering '
                                      'the tongue. Nonvascularized bone fails in a contaminated '
                                      'field likely to be irradiated, and soft tissue over a plate '
                                      'risks extrusion.',
                       'why_wrong': ['Closing a 5 x 4-cm mucosal defect primarily tethers the '
                                     'tongue and risks dehiscence over exposed bone and plates.',
                                     'Correct.',
                                     'Nonvascularized bone grafts become infected and resorb in a '
                                     'field contaminated by saliva and likely to be irradiated.',
                                     'Soft tissue over a 7-cm plate restores lining but not bone, '
                                     'with high plate exposure and no implant option.'],
                       'board_pearl': 'Composite mandible plus lining defect: vascularized bone '
                                      'with a skin paddle on one pedicle.',
                       'curveball': 'How do planned dental implants and the shape of the defect '
                                    'influence fibula design?',
                       'curveball_answer': 'Virtual surgical planning with cutting guides sets '
                                           'osteotomy number and segment length, keeping segments '
                                           'at least about 2 cm to protect periosteal blood '
                                           'supply. A double-barrel fibula or positioning the bone '
                                           'at the alveolar height improves implant prosthetics. '
                                           'Primary or delayed implants are considered, '
                                           'recognizing that radiation lowers implant survival.'},
 'v225_hn_recon_snr': {'stem': 'A 71-year-old man needs salvage total laryngectomy for recurrent '
                               'glottic SCC 2 years after chemoradiation. Enough pharyngeal mucosa '
                               'remains for primary closure. He has severe peripheral arterial '
                               'disease with superficial femoral occlusion, a prior left radial '
                               'forearm harvest, and an abnormal right Allen test. Albumin is 3.1 '
                               'g/dL. The team wants vascularized tissue to lower fistula risk. '
                               'Which reconstruction is most appropriate?',
                       'choices': ['Primary pharyngeal closure without added vascularized tissue',
                                   'Anterolateral thigh free flap as an onlay',
                                   'Radial forearm free flap from the right arm',
                                   'Pectoralis major myofascial onlay flap'],
                       'answer': 3,
                       'explanation': 'Salvage laryngectomy after chemoradiation carries a high '
                                      'pharyngocutaneous fistula rate, and vascularized onlay '
                                      'tissue over a primary closure reduces it. Flap choice must '
                                      'respect the donor constraints in this patient: diseased leg '
                                      'inflow, a used left forearm, and poor ulnar collateral flow '
                                      'on the right. A pedicled pectoralis major myofascial flap '
                                      'brings unirradiated tissue with no microvascular '
                                      'anastomosis and no need for leg or arm donors, which suits '
                                      'a frail, malnourished patient.',
                       'why_wrong': ['Primary closure alone after chemoradiation carries a '
                                     'substantially higher fistula rate than closure reinforced '
                                     'with vascularized tissue.',
                                     'Severe arterial disease of the leg raises concern for '
                                     'unreliable thigh perforators and donor-site wound problems.',
                                     'An abnormal Allen test means radial artery harvest risks '
                                     'hand ischemia, so the right forearm is not a safe donor.',
                                     'Correct.'],
                       'board_pearl': 'Salvage laryngectomy after chemoradiation: reinforce the '
                                      'closure with vascularized, unirradiated tissue chosen '
                                      'around donor constraints.',
                       'curveball': 'Intraoperatively the remaining pharyngeal mucosa is only a '
                                    'narrow strip that cannot be closed without tension. How does '
                                    'the plan change?',
                       'curveball_answer': 'A patch of skin is now needed to restore the '
                                           'pharyngeal lumen rather than an onlay. A pectoralis '
                                           'major myocutaneous flap or a supraclavicular artery '
                                           'island flap can supply that skin without microvascular '
                                           'surgery. If a free flap were feasible, a tubed or '
                                           'patch anterolateral thigh or radial forearm flap would '
                                           'be standard; circumferential defects may need '
                                           'jejunum.'},
 'v138_hn_21': {'stem': 'A 67-year-old man had chemoradiation for a p16-negative laryngeal SCC 2 '
                        'years ago. He now has an unresectable recurrence in the neck encasing the '
                        'carotid and two small lung metastases. ECOG performance status is 1, '
                        'renal function and hearing are normal, and he has had no immunotherapy. '
                        'PD-L1 combined positive score on the recurrence is 0. Which first-line '
                        'systemic therapy is most appropriate?',
                'choices': ['Pembrolizumab with platinum and 5-FU',
                            'Pembrolizumab as a single agent',
                            'Nivolumab as a single agent',
                            'Cetuximab as single-agent weekly therapy'],
                'answer': 0,
                'explanation': 'In KEYNOTE-048, pembrolizumab with platinum and 5-FU improved '
                               'overall survival over the EXTREME regimen, and this combination is '
                               'a preferred first-line option regardless of PD-L1 status. '
                               'Pembrolizumab alone is reserved for a combined positive score of 1 '
                               'or more, because its benefit is driven by PD-L1-expressing tumors. '
                               'With a score of 0, good performance status, and preserved organ '
                               'function, the decision pivots on the biomarker: he needs the '
                               'chemotherapy backbone. EXTREME remains a reasonable alternative in '
                               'this group.',
                'why_wrong': ['Correct.',
                              'Single-agent pembrolizumab is indicated only when the combined '
                              'positive score is at least 1, and its benefit in PD-L1-negative '
                              'tumors is not established.',
                              'Nivolumab monotherapy is a second-line option after platinum '
                              'progression, not first-line therapy for a platinum-naive patient.',
                              'Single-agent cetuximab has low response rates and no survival '
                              'advantage over immunotherapy-based first-line regimens in fit '
                              'patients.'],
                'board_pearl': 'Recurrent/metastatic HNSCC: CPS 1 or more allows pembrolizumab '
                               'alone; any CPS allows pembrolizumab with platinum and 5-FU.',
                'curveball': 'His imaging instead showed a controlled neck and a single new lung '
                             'nodule 18 months after treatment. How does oligometastatic disease '
                             'change the role of local therapy?',
                'curveball_answer': 'A solitary lung lesion should be biopsied to separate a new '
                                    'primary lung cancer from a metastasis. For true '
                                    'oligometastatic disease with a controlled primary and a long '
                                    'disease-free interval, metastasectomy or stereotactic '
                                    'radiation can be considered alongside systemic therapy, '
                                    'ideally in multidisciplinary review or a trial, since '
                                    'selected patients achieve durable control.'},
 'v145_hn_16': {'stem': 'A 58-year-old woman treated with surgery and postoperative radiation for '
                        'oral cavity SCC 14 months ago now has a rapidly enlarging, painful, '
                        'unresectable submandibular recurrence that is fungating through the skin, '
                        'plus new liver metastases. Over 3 weeks she has needed escalating opioids '
                        'and her intake is falling. ECOG performance status is 1 and renal '
                        'function is normal. PD-L1 combined positive score is 22. Which first-line '
                        'regimen is most appropriate?',
                'choices': ['Pembrolizumab as a single agent',
                            'Nivolumab as a single agent',
                            'Cetuximab as single-agent weekly therapy',
                            'Pembrolizumab with platinum and 5-FU'],
                'answer': 3,
                'explanation': 'With a combined positive score of 1 or more, both pembrolizumab '
                               'alone and pembrolizumab with platinum and 5-FU are first-line '
                               'options from KEYNOTE-048. The choice then turns on tempo and '
                               'symptoms. Single-agent checkpoint inhibition has a lower response '
                               'rate and can take weeks to work, and early progression is more '
                               'common. Rapidly growing, painful, fungating disease that threatens '
                               'nutrition favors the combination, which offers a higher and faster '
                               'objective response while retaining the survival benefit of '
                               'immunotherapy.',
                'why_wrong': ['Pembrolizumab alone is reasonable for indolent disease but has a '
                              'lower, slower response, risking further decline in rapidly '
                              'progressing symptomatic tumor.',
                              'Nivolumab monotherapy is approved after progression on platinum, '
                              'not as first-line therapy for a platinum-naive recurrence.',
                              'Cetuximab alone produces modest response rates and has no survival '
                              'advantage over immunotherapy-based first-line treatment.',
                              'Correct.'],
                'board_pearl': 'High CPS with bulky, symptomatic, fast-moving disease: add '
                               'platinum and 5-FU to pembrolizumab for faster response.',
                'curveball': 'Months later, on maintenance pembrolizumab, a single painful rib '
                             'metastasis grows while all other disease is controlled. What local '
                             'treatment may help?',
                'curveball_answer': 'Oligoprogression can be treated with local therapy while '
                                    'continuing the effective systemic agent. Palliative or '
                                    'stereotactic radiation to the rib gives good pain control and '
                                    'may extend disease control, avoiding a premature switch in '
                                    'systemic therapy. Bone-modifying agents and orthopedic review '
                                    'are added if there is fracture risk.'},
 'v223_hn_rm_fnd': {'stem': 'A 63-year-old man completed definitive radiation for a T2N0 glottic '
                            'SCC 16 months ago. He now has worsening hoarseness, and laryngoscopy '
                            'shows an exophytic lesion on the previously treated fold with normal '
                            'mobility. Biopsy confirms recurrent SCC. He is otherwise well, with '
                            'ECOG performance status 0, and has no neck mass on palpation. What is '
                            'the most appropriate next step?',
                    'choices': ['Restage with neck imaging and PET-CT to judge salvage candidacy',
                                'Re-irradiate the larynx to full dose, since a year has passed',
                                'Start pembrolizumab, since recurrence after radiation is '
                                'incurable',
                                'Schedule total laryngectomy based on the biopsy alone'],
                    'answer': 0,
                    'explanation': 'The first question in any recurrence is whether it is isolated '
                                   'and potentially curable with salvage local therapy or is '
                                   'unresectable or metastatic and better treated systemically. '
                                   'That requires restaging: contrast CT or MRI of the larynx and '
                                   'neck to map local extent and cartilage invasion, and PET-CT or '
                                   'chest CT for regional and distant disease. A small '
                                   'radiation-failure glottic recurrence in a fit patient is often '
                                   'salvageable, sometimes by partial laryngectomy, so the extent '
                                   'determines the operation.',
                    'why_wrong': ['Correct.',
                                  'Re-irradiation is reserved for selected unresectable '
                                  'recurrences; surgery is preferred for a resectable laryngeal '
                                  'recurrence after radiation.',
                                  'Many radiation failures of the larynx are curable by salvage '
                                  'surgery, so jumping to palliative immunotherapy forfeits a '
                                  'chance of cure.',
                                  'Without staging, distant disease could be missed or a smaller '
                                  'conservation operation such as partial laryngectomy could be '
                                  'overlooked.'],
                    'board_pearl': 'Recurrence: first decide salvageable versus not, by restaging '
                                   'extent, prior treatment, and fitness.',
                    'curveball': 'What imaging is most useful before committing to salvage '
                                 'laryngectomy, and how should a post-radiation PET be '
                                 'interpreted?',
                    'curveball_answer': 'Contrast CT or MRI defines local extent and cartilage '
                                        'invasion, and PET-CT screens for nodal and distant '
                                        'disease, especially lung. PET is most reliable at least '
                                        '12 weeks after radiation, and uptake from inflammation or '
                                        'chondronecrosis can mimic tumor, so a positive scan in '
                                        'the larynx needs biopsy correlation.'},
 'v223_hn_rm_app': {'stem': 'A 60-year-old woman with a history of chemoradiation for '
                            'hypopharyngeal SCC now has biopsy-proven bone and lung metastases. '
                            'She is ECOG 1 with normal renal function and wants to start treatment '
                            'soon. The archived primary tumor was p16-negative. The oncologist '
                            'orders additional testing on the new biopsy before choosing '
                            'first-line systemic therapy. Which test result most directly '
                            'determines her first-line regimen?',
                    'choices': ['EGFR expression on immunohistochemistry',
                                'HPV status by p16 immunostaining',
                                'Tumor mutational burden on sequencing',
                                'PD-L1 combined positive score'],
                    'answer': 3,
                    'explanation': 'First-line therapy for recurrent or metastatic HNSCC follows '
                                   'KEYNOTE-048. The PD-L1 combined positive score, which counts '
                                   'PD-L1-positive tumor cells, lymphocytes, and macrophages '
                                   'relative to tumor cells, decides whether pembrolizumab alone '
                                   'is an option (score 1 or more) or whether chemotherapy should '
                                   'be added. Tissue from the recurrence is preferred because '
                                   'expression can change after treatment. Performance status, '
                                   'tempo, and symptoms then refine the choice between monotherapy '
                                   'and combination therapy.',
                    'why_wrong': ['Nearly all HNSCC expresses EGFR, and cetuximab use does not '
                                  'depend on the level of expression.',
                                  'HPV status is prognostic and important in oropharyngeal cancer '
                                  'staging, but it does not select among first-line regimens.',
                                  'Tumor mutational burden can support a tissue-agnostic '
                                  'immunotherapy indication but is not the standard driver of '
                                  'first-line choice here.',
                                  'Correct.'],
                    'board_pearl': 'Order PD-L1 combined positive score on recurrent or metastatic '
                                   'tissue; it selects first-line pembrolizumab strategy.',
                    'curveball': 'Her score is 30, but she develops rapidly progressive, painful '
                                 'bone disease while awaiting treatment. How does that influence '
                                 'the choice between immunotherapy alone and combination therapy?',
                    'curveball_answer': 'A high score makes pembrolizumab alone an option, but '
                                        'rapidly progressive symptomatic disease favors '
                                        'pembrolizumab with platinum and 5-FU for a higher, faster '
                                        'response. Painful bone lesions also warrant palliative '
                                        'radiation and a bone-modifying agent, while the systemic '
                                        'therapy starts.'},
 'v223_hn_rm_snr': {'stem': 'A 69-year-old man with metastatic oral cavity SCC has progressed '
                            'through pembrolizumab with chemotherapy and then second-line '
                            'cetuximab. He has lost 14 kg, spends most of the day in bed with ECOG '
                            'performance status 3, and has had three admissions in 6 weeks for '
                            'pain and dehydration. He says he wants to be at home. What is the '
                            'most appropriate next step?',
                    'choices': ['Start a third-line cytotoxic doublet to try to regain control',
                                'Rechallenge immunotherapy with ipilimumab added to nivolumab',
                                'Refer for surgical debulking of the dominant metastatic site',
                                'Discuss goals of care and offer hospice with active symptom '
                                'control'],
                    'answer': 3,
                    'explanation': 'With ECOG 3, progression through two lines, cachexia, and '
                                   'repeated admissions, further anticancer therapy offers little '
                                   'realistic benefit and substantial toxicity. Patients this ill '
                                   'were excluded from the trials behind later-line regimens. The '
                                   "attending's job is an honest prognostic discussion, early "
                                   'palliative and hospice involvement, and continued active '
                                   'management of pain, nutrition, secretions, airway, and '
                                   'bleeding. That honors his wish to be home and is not '
                                   'abandonment.',
                    'why_wrong': ['Cytotoxic chemotherapy in a patient with ECOG 3 adds toxicity '
                                  'and admissions with little expected survival or symptom '
                                  'benefit.',
                                  'Adding ipilimumab to nivolumab did not improve survival in '
                                  'HNSCC trials and is poorly suited to a declining patient.',
                                  'Debulking surgery does not change outcome in disseminated '
                                  'disease and adds morbidity in a patient with poor reserve.',
                                  'Correct.'],
                    'board_pearl': 'Poor performance status after two lines: shift to goals of '
                                   'care and hospice while treating symptoms actively.',
                    'curveball': 'Which airway or bleeding events still warrant urgent ENT action '
                                 'in this comfort-focused plan, and how should the team prepare?',
                    'curveball_answer': 'A sentinel bleed from tumor near the carotid, or '
                                        'progressive stridor from airway compression, may still '
                                        'warrant intervention such as endovascular embolization or '
                                        'tracheostomy if consistent with his goals. Plans should '
                                        'be agreed in advance, with dark towels, suction, and '
                                        'crisis sedation orders at home for a terminal '
                                        'hemorrhage.'},
 'v138_hn_22': {'stem': 'A 55-year-old man has a T4aN2c hypopharyngeal SCC. The tumor board '
                        'recommends three cycles of docetaxel, cisplatin, and 5-FU, then '
                        'reassessment, then 70 Gy of radiation given with weekly carboplatin. He '
                        'has mild baseline hearing loss. A medical student asks how to classify '
                        'the weekly carboplatin and what it is meant to accomplish. Which '
                        'description is most accurate?',
                'choices': ['Concurrent therapy that sensitizes tumor cells to the radiation dose',
                            'Induction therapy that selects responders for organ preservation',
                            'Adjuvant therapy that eradicates residual microscopic disease',
                            'Maintenance therapy that lowers the rate of late distant failure'],
                'answer': 0,
                'explanation': 'Systemic therapy is named by its timing relative to local '
                               'treatment. Induction or neoadjuvant therapy, here the '
                               'docetaxel-based regimen, comes before local treatment to shrink '
                               'tumor, test chemosensitivity, and select patients for larynx '
                               'preservation. Concurrent therapy is given during radiation, where '
                               'agents such as carboplatin or cisplatin act mainly as '
                               'radiosensitizers that improve locoregional control. Adjuvant '
                               'therapy follows completed local treatment. Carboplatin was chosen '
                               'here because of his hearing loss.',
                'why_wrong': ['Correct.',
                              'The docetaxel, cisplatin, and 5-FU cycles are the induction '
                              'component; the carboplatin is given during radiation.',
                              'Adjuvant therapy follows completion of local treatment, whereas '
                              'this carboplatin is delivered alongside the radiation course.',
                              'No maintenance therapy has proven benefit after curative '
                              'chemoradiation, and this drug is given during radiation.'],
                'board_pearl': 'Name systemic therapy by timing: induction before, concurrent '
                               'during (radiosensitizing), adjuvant after local therapy.',
                'curveball': 'Why do renal function and hearing need to be checked before '
                             'cisplatin, and what does carboplatin trade off?',
                'curveball_answer': 'Cisplatin causes dose-related proximal tubular injury and '
                                    'irreversible high-frequency sensorineural hearing loss, so '
                                    'baseline creatinine clearance and audiometry identify '
                                    'patients at risk. Carboplatin is less nephrotoxic and less '
                                    'ototoxic but more myelosuppressive, particularly causing '
                                    'thrombocytopenia, and is considered somewhat less effective '
                                    'as a radiosensitizer.'},
 'v145_hn_18': {'stem': 'A 71-year-old man has a T3N1 p16-negative supraglottic SCC and chooses '
                        'chemoradiation. He has diabetic kidney disease with a creatinine '
                        'clearance of 38 mL/min, moderate bilateral sensorineural hearing loss '
                        'treated with hearing aids, and grade 2 peripheral neuropathy. ECOG '
                        'performance status is 1. Which concurrent regimen with radiation is most '
                        'appropriate?',
                'choices': ['Cetuximab given weekly throughout the radiation course',
                            'Weekly cisplatin at a reduced dose of 40 mg/m2',
                            'High-dose cisplatin every 3 weeks with extra hydration',
                            'Induction docetaxel, cisplatin, and 5-FU first'],
                'answer': 0,
                'explanation': 'Cisplatin is the standard radiosensitizer, but impaired renal '
                               'function, preexisting hearing loss, neuropathy, and frailty are '
                               'accepted contraindications. Weekly dosing still delivers '
                               'cumulative nephrotoxicity and ototoxicity, and creatinine '
                               'clearance below about 50 to 60 mL/min generally excludes '
                               'cisplatin. For cisplatin-ineligible HPV-negative disease, '
                               'radiation with cetuximab is a standard option; weekly docetaxel or '
                               'carboplatin-based regimens are alternatives. Cetuximab is inferior '
                               'to cisplatin in eligible patients, so it is used only when '
                               'cisplatin is unsafe.',
                'why_wrong': ['Correct.',
                              'Weekly cisplatin still causes cumulative kidney, ear, and nerve '
                              'injury, and his organ function falls below accepted thresholds.',
                              'Hydration does not make high-dose cisplatin safe with a clearance '
                              'of 38 mL/min, existing hearing loss, and neuropathy.',
                              'Induction with this regimen still uses cisplatin and adds toxicity '
                              'without addressing why he cannot receive platinum.'],
                'board_pearl': 'Cisplatin-ineligible: poor renal function, hearing loss, '
                               'neuropathy, or frailty; consider cetuximab, docetaxel, or '
                               'carboplatin.',
                'curveball': 'How does baseline audiometry help the otolaryngologist contribute to '
                             'systemic therapy planning?',
                'curveball_answer': 'Baseline audiometry, including high frequencies, documents '
                                    'preexisting loss that may make cisplatin inadvisable and '
                                    'provides a reference for monitoring during treatment. New '
                                    'threshold shifts during therapy can prompt dose modification '
                                    'or a switch to carboplatin. It also guides counseling and '
                                    'hearing aid planning before ototoxic treatment.'},
 'v228_hn_sys_fnd': {'stem': 'A 52-year-old man with a p16-positive left tonsil SCC with '
                             'ipsilateral nodes is starting 70 Gy of radiation with high-dose '
                             'cisplatin. His renal function and hearing are normal. At consent he '
                             'asks whether the cisplatin is mainly there to stop the cancer from '
                             'spreading to his lungs. Which outcome does concurrent cisplatin '
                             'chiefly improve?',
                     'choices': ['Rate of distant metastasis',
                                 'Locoregional control of the tumor',
                                 'Long-term swallowing function',
                                 'Incidence of second primary cancers'],
                     'answer': 1,
                     'explanation': 'Concurrent cisplatin acts as a radiosensitizing systemic '
                                    'agent. Platinum-DNA adducts impair repair of radiation damage '
                                    'and add direct cytotoxicity, so more tumor cells are killed '
                                    'in the irradiated volume. Meta-analysis data show the '
                                    'survival benefit of concurrent chemotherapy comes mainly from '
                                    'better locoregional control, with only a small effect on '
                                    'distant failure. The cost is added mucositis, nephrotoxicity, '
                                    'ototoxicity, neuropathy, and late dysphagia, which must be '
                                    'weighed in each patient.',
                     'why_wrong': ['Concurrent chemotherapy has only a small effect on distant '
                                   'metastasis; its main contribution is improved control within '
                                   'the radiation field.',
                                   'Correct.',
                                   'Cisplatin adds acute mucositis and increases late dysphagia '
                                   'rather than improving long-term swallowing.',
                                   'Cisplatin does not prevent second primary cancers, which '
                                   'depend on field cancerization and continued tobacco and '
                                   'alcohol exposure.'],
                     'board_pearl': 'Concurrent cisplatin mainly improves locoregional control, '
                                    'not distant metastasis.',
                     'curveball': 'Which baseline findings make standard high-dose cisplatin '
                                  'particularly hazardous for a patient like this?',
                     'curveball_answer': 'Creatinine clearance below about 50 to 60 mL/min, '
                                         'preexisting hearing loss or tinnitus, grade 2 or worse '
                                         'neuropathy, ECOG performance status of 2 or more, '
                                         'advanced age with frailty, and significant heart failure '
                                         'or uncontrolled comorbidity all raise risk. Such '
                                         'patients are usually considered cisplatin-ineligible and '
                                         'offered alternative radiosensitizers.'},
 'v228_hn_sys_app': {'stem': 'A 74-year-old woman had surgery and radiation for laryngeal SCC 3 '
                             'years ago. Surveillance now shows several slowly growing lung '
                             'metastases up to 1.5 cm, with no locoregional disease. She has no '
                             'symptoms, ECOG performance status is 1, and she prefers treatment '
                             'with few side effects. PD-L1 combined positive score is 40. Which '
                             'first-line systemic therapy is most appropriate?',
                     'choices': ['Cetuximab, platinum, and 5-FU (EXTREME)',
                                 'Nivolumab as a single agent',
                                 'Weekly single-agent methotrexate',
                                 'Pembrolizumab as a single agent'],
                     'answer': 3,
                     'explanation': 'First-line therapy for recurrent or metastatic HNSCC is '
                                    'selected by PD-L1, tempo, symptoms, and patient goals. With a '
                                    'combined positive score of 1 or more, pembrolizumab alone '
                                    'improved overall survival over EXTREME in KEYNOTE-048, with '
                                    'the greatest benefit at higher scores and fewer severe '
                                    'adverse events. Her disease is low-volume, slow, and '
                                    'asymptomatic, so there is no need for the faster response of '
                                    'added chemotherapy, and single-agent immunotherapy matches '
                                    'her wish to limit toxicity.',
                     'why_wrong': ['EXTREME was inferior to pembrolizumab for PD-L1-positive '
                                   'tumors in KEYNOTE-048 and is considerably more toxic.',
                                   'Nivolumab monotherapy is approved after progression on '
                                   'platinum-based therapy rather than for platinum-naive '
                                   'first-line treatment.',
                                   'Methotrexate has low response rates and no survival benefit; '
                                   'it is reserved for patients unfit for modern therapy.',
                                   'Correct.'],
                     'board_pearl': 'High CPS, low-volume, slow, asymptomatic metastatic HNSCC: '
                                    'pembrolizumab monotherapy.',
                     'curveball': 'Why might bulky symptomatic disease instead favor a regimen '
                                  'with faster expected cytoreduction?',
                     'curveball_answer': 'Pembrolizumab alone produces responses in only about one '
                                         'in five patients, and responses can take weeks, with '
                                         'more early progression than chemotherapy-containing '
                                         'regimens. When airway compromise, uncontrolled pain, or '
                                         'bleeding is imminent, adding platinum and 5-FU gives a '
                                         'higher and quicker objective response while preserving '
                                         'the survival benefit of immunotherapy.'},
 'v228_hn_sys_snr': {'stem': 'A 72-year-old woman with metastatic tonsil SCC is receiving '
                             'third-line paclitaxel and cetuximab. In 2 months she has had four '
                             'admissions for febrile neutropenia, dehydration, and falls. Her ECOG '
                             'performance status has declined from 1 to 3, albumin is 2.6 g/dL, '
                             'and restaging shows growth of liver metastases. She asks whether the '
                             'treatment is still worth it. What is the most appropriate next step?',
                     'choices': ['Dose-reduce paclitaxel and continue weekly treatment',
                                 'Add filgrastim support and continue the regimen',
                                 'Hold therapy and hold a goals-of-care discussion',
                                 'Switch to a phase 1 trial of an investigational agent'],
                     'answer': 2,
                     'explanation': 'Systemic therapy is continued only while expected benefit '
                                    "stays proportionate to toxicity and the patient's goals. Here "
                                    'every trigger for reassessment is present: progression '
                                    'despite third-line therapy, a fall to ECOG 3, malnutrition, '
                                    'and repeated severe toxicity. The right step is to pause '
                                    'treatment and have an honest conversation about prognosis and '
                                    'priorities with early palliative care, while continuing '
                                    'active symptom management. Modifying or supporting the same '
                                    'failing regimen addresses toxicity but ignores the absence of '
                                    'benefit.',
                     'why_wrong': ['Dose reduction may lessen toxicity, but the disease is '
                                   'progressing, so continued paclitaxel offers little benefit.',
                                   'Growth factor support prevents neutropenia but does not '
                                   'address tumor progression, falls, malnutrition, or her '
                                   'question about value.',
                                   'Correct.',
                                   'Phase 1 trials generally require good performance status, and '
                                   'she has not yet had a chance to state her goals.'],
                     'board_pearl': 'Progression, declining performance status, and repeated '
                                    'toxicity are triggers to pause therapy and revisit goals of '
                                    'care.',
                     'curveball': 'Which clinical changes during systemic therapy should trigger '
                                  'an urgent goals-of-care reassessment?',
                     'curveball_answer': 'Triggers include a fall in ECOG to 3 or 4, progression '
                                         'through two or more lines, repeated unplanned admissions '
                                         'or ICU care, cachexia with falling albumin, new organ '
                                         'failure, a sentinel bleed or impending airway '
                                         'compromise, and the patient voicing doubts. Each should '
                                         'prompt explicit discussion of prognosis, code status, '
                                         'and hospice.'},
 'v138_hn_23': {'stem': 'A 64-year-old man is 4 months past total laryngectomy and postoperative '
                        'radiation for laryngeal SCC. He communicates with a neck-type '
                        'electrolarynx but dislikes its mechanical sound and wants more natural, '
                        'fluent speech. He has good hand dexterity, a 2-cm stoma, and adequate '
                        'pulmonary function. An esophageal insufflation test produces fluent '
                        'voicing. Which rehabilitation is most appropriate?',
                'choices': ['Training in injected-air esophageal speech',
                            'Switching to an intraoral-tube electrolarynx',
                            'Secondary tracheoesophageal voice prosthesis',
                            'A pneumatic artificial larynx attached at the stoma'],
                'answer': 2,
                'explanation': 'Tracheoesophageal puncture with a one-way voice prosthesis is the '
                               'most effective voice restoration after laryngectomy and produces '
                               'the most natural and fluent speech. When the stoma is occluded, '
                               'pulmonary air passes through the prosthesis into the esophagus and '
                               'vibrates the pharyngoesophageal segment, giving longer phrases and '
                               'better loudness than esophageal speech. A fluent insufflation test '
                               'predicts a segment that will vibrate without spasm, and good '
                               'dexterity and lung function make him a strong candidate.',
                'why_wrong': ['Esophageal speech uses a small swallowed air bolus, gives short '
                              'phrases, and many patients never achieve functional fluency.',
                              'An intraoral electrolarynx still produces a mechanical, monotone '
                              'voice, which is the quality he wants to escape.',
                              'Correct.',
                              'Pneumatic devices are uncommon, awkward to use, and less fluent '
                              'than a prosthesis that uses pulmonary air directly.'],
                'board_pearl': 'Most fluent, natural alaryngeal voice: tracheoesophageal puncture '
                               'with a voice prosthesis.',
                'curveball': 'After placement, what distinguishes leakage through the prosthesis '
                             'from leakage around it?',
                'curveball_answer': 'Leakage through the center means valve failure, usually from '
                                    'Candida biofilm or wear, and is treated by replacing the '
                                    'prosthesis and controlling yeast. Leakage around it means the '
                                    'tract has enlarged or the device is the wrong length, and is '
                                    'treated by resizing, temporary removal to let the tract '
                                    'shrink, or tract revision.'},
 'v145_hn_19': {'stem': 'A 60-year-old woman with a T4a laryngeal SCC invading through the thyroid '
                        'cartilage is scheduled for primary total laryngectomy and bilateral neck '
                        'dissection, with postoperative chemoradiation expected. She is a teacher '
                        'who wants pulmonary-powered speech as soon as possible. Pharyngeal '
                        'closure is expected to be primary without a flap. She has good dexterity '
                        'and normal lung function. Which voice restoration plan is most '
                        'appropriate?',
                'choices': ['Delay any puncture until a year after radiation ends',
                            'Primary tracheoesophageal puncture at laryngectomy',
                            'Esophageal speech as the planned primary method',
                            'Electrolarynx alone, reassessing after radiation'],
                'answer': 1,
                'explanation': 'Tracheoesophageal speech uses pulmonary air through a one-way '
                               'prosthesis to vibrate the pharyngoesophageal segment and is the '
                               'most fluent alaryngeal option. In a primary laryngectomy with a '
                               'straightforward closure, puncture at the time of surgery is safe, '
                               'avoids a second procedure, and allows voicing within weeks, even '
                               'if postoperative radiation follows. Many surgeons add a pharyngeal '
                               'plexus neurectomy or myotomy to reduce spasm. An electrolarynx is '
                               'still taught early as a backup.',
                'why_wrong': ['Planned postoperative radiation does not require deferring '
                              'puncture; primary puncture is safe and avoids months without fluent '
                              'voice.',
                              'Correct.',
                              'Esophageal speech is hard to master and less fluent, which does not '
                              'meet her goal of pulmonary-powered voice.',
                              'An electrolarynx is a useful bridge but not the preferred '
                              'definitive option for a motivated, dexterous candidate.'],
                'board_pearl': 'Primary TEP at total laryngectomy is safe and standard when '
                               'closure is straightforward, even with adjuvant radiation planned.',
                'curveball': 'Months later her prosthesis begins leaking through its center when '
                             'she drinks. What is the likely mechanism and first response?',
                'curveball_answer': 'Central leakage means the one-way valve is failing, most '
                                    'often from Candida biofilm deforming the flap or from wear. '
                                    'The prosthesis is replaced, and recurrent early failure '
                                    'prompts antifungal treatment and probiotics or a device with '
                                    'an antifungal valve. A plug can stop leakage temporarily '
                                    'until replacement.'},
 'v222_hn_tep_fnd': {'stem': 'A 68-year-old man is 6 weeks after total laryngectomy with primary '
                             'tracheoesophageal puncture. At his first voicing session he occludes '
                             'the stoma with his thumb and produces speech. His wife asks how he '
                             'can talk without a larynx and whether his vocal folds were saved. '
                             'Videofluoroscopy during phonation shows vibration high in the '
                             'reconstructed pharynx. Which mechanism best explains his voice?',
                     'choices': ['Swallowed air is belched up to vibrate the neopharynx',
                                 'An external source drives vibration through neck tissue',
                                 'Lung air through a one-way valve vibrates the pharyngoesophageal '
                                 'segment',
                                 'Air through the prosthesis vibrates preserved false vocal folds'],
                     'answer': 2,
                     'explanation': 'Stoma occlusion diverts exhaled pulmonary air through the '
                                    'one-way tracheoesophageal prosthesis into the upper '
                                    'esophagus. The air then vibrates the pharyngoesophageal '
                                    'segment, formed largely by the cricopharyngeus and inferior '
                                    'constrictor, which becomes the new sound source, and the '
                                    'tongue, palate, and lips articulate it. The valve opens only '
                                    'toward the esophagus, preventing aspiration. No laryngeal '
                                    'structure is preserved or recreated, and the pulmonary air '
                                    'supply gives longer phrases than esophageal speech.',
                     'why_wrong': ['Injecting or swallowing air and releasing it describes '
                                   'esophageal speech, which does not use pulmonary air or a '
                                   'prosthesis.',
                                   'An external vibration source describes a neck-type '
                                   'electrolarynx, not tracheoesophageal speech.',
                                   'Correct.',
                                   'Total laryngectomy removes the false vocal folds along with '
                                   'the rest of the larynx, so they cannot generate sound.'],
                     'board_pearl': 'TEP voice: pulmonary air through a one-way valve vibrates the '
                                    'pharyngoesophageal segment.',
                     'curveball': 'How do esophageal speech and an electrolarynx differ from TEP '
                                  'speech in mechanism and practical use?',
                     'curveball_answer': 'Esophageal speech uses a small injected or swallowed air '
                                         'bolus without a prosthesis, so phrases are short and '
                                         'many patients never master it. An electrolarynx supplies '
                                         'an external vibration source, is easy to learn and '
                                         'useful early after surgery, but sounds mechanical. TEP '
                                         'uses pulmonary air and gives the most fluent speech but '
                                         'requires prosthesis care.'},
 'v222_hn_tep_app': {'stem': 'A 66-year-old woman has used a tracheoesophageal voice prosthesis '
                             'for 7 months. For a week she has coughed when drinking. In clinic, '
                             'while she swallows colored water, fluid drips from the lumen of the '
                             'prosthesis into the trachea, and none appears around its rim. The '
                             'device fits snugly, and her voice is unchanged. What is the most '
                             'appropriate management?',
                     'choices': ['Replace with a new prosthesis of the same size',
                                 'Downsize to a shorter prosthesis to tighten the tract',
                                 'Remove the device and allow the puncture to close',
                                 'Place a purse-string suture around the puncture'],
                     'answer': 0,
                     'explanation': 'Leakage through the lumen means the one-way valve no longer '
                                    'seals, usually from Candida biofilm, debris, or wear, and is '
                                    'the most common reason prostheses are changed. The tract fit '
                                    'is fine, so the solution is a new device of the same length; '
                                    'a temporary plug can stop leakage until then. Recurrent early '
                                    'failure should prompt evaluation for yeast and antifungal '
                                    'measures. Leakage around the rim is a different problem that '
                                    'points to tract enlargement or incorrect length.',
                     'why_wrong': ['Correct.',
                                   'A shorter device addresses a pistoning prosthesis or a '
                                   'thinning tract wall, not a valve that fails to close.',
                                   'Closing the puncture sacrifices her voice to treat a valve '
                                   'problem fixed by simple replacement.',
                                   'Purse-string suture treats an enlarged tract with '
                                   'periprosthetic leakage, which is not present here.'],
                     'board_pearl': 'Leak through the center: valve failure, replace the '
                                    'prosthesis. Leak around it: tract problem, resize or revise.',
                     'curveball': 'If fluid instead leaked around the rim of a loose prosthesis, '
                                  'what would that suggest about the tract and how would you '
                                  'respond?',
                     'curveball_answer': 'Periprosthetic leakage suggests tract dilation, a '
                                         'prosthesis that is too long and pistons, or poor tissue '
                                         'quality from radiation, reflux, or recurrence. Steps '
                                         'include remeasuring and fitting a correct length, a '
                                         'larger-flange prosthesis, temporary removal with a small '
                                         'catheter to let the tract shrink, injection augmentation '
                                         'or purse-string suture, and biopsy if tumor is '
                                         'suspected.'},
 'v222_hn_tep_snr': {'stem': 'A 65-year-old man needs salvage total laryngectomy after '
                             'chemoradiation. The pharyngeal remnant is fibrotic, and closure will '
                             'require a pectoralis major myocutaneous flap patch. His albumin is '
                             '2.9 g/dL, and he has diabetes. He is motivated and dexterous and '
                             'wants the most fluent voice possible. The team discusses when to '
                             'place the tracheoesophageal puncture. Which plan is most '
                             'appropriate?',
                     'choices': ['Primary puncture with immediate prosthesis through the patch '
                                 'closure',
                                 'Secondary puncture once the pharyngeal closure has fully healed',
                                 'Esophageal speech as the planned definitive method',
                                 'Electrolarynx only, ruling out puncture after radiation'],
                     'answer': 1,
                     'explanation': 'Primary puncture is often safe in salvage laryngectomy, but '
                                    'timing should be individualized. This patient has several '
                                    'fistula risk factors: prior chemoradiation, fibrotic tissue '
                                    'needing a flap patch, malnutrition, and diabetes. A puncture '
                                    'through a tenuous reconstruction adds a potential leak point '
                                    'at the most vulnerable time. Deferring to secondary puncture '
                                    'after healing keeps the goal of fluent voice while protecting '
                                    'the closure; an electrolarynx bridges communication in the '
                                    'meantime. Some centers still do primary puncture here, so '
                                    'judgment varies.',
                     'why_wrong': ['A primary puncture through a tenuous flap closure in a '
                                   'malnourished, irradiated patient adds fistula risk at the '
                                   'weakest point.',
                                   'Correct.',
                                   'Esophageal speech is difficult and often fails after flap '
                                   'reconstruction, so it should not be the planned definitive '
                                   'method.',
                                   'Prior radiation does not exclude tracheoesophageal puncture; '
                                   'many irradiated patients use prostheses successfully.'],
                     'board_pearl': 'Primary versus secondary TEP is individualized; high fistula '
                                    'risk favors deferring puncture until healing.',
                     'curveball': 'Arthritis later prevents him from occluding the stoma with a '
                                  'finger. How does that change device and rehabilitation '
                                  'planning?',
                     'curveball_answer': 'A hands-free tracheostoma valve can work if a heat and '
                                         'moisture exchanger housing seals reliably and he has '
                                         'adequate expiratory pressure. Stoma shape, adhesives, or '
                                         'a laryngectomy tube may be needed for the seal. If '
                                         'hands-free voicing fails, speech pathology can adapt '
                                         'occlusion aids or prioritize an electrolarynx.'},
 'v138_hn_24': {'stem': 'A 51-year-old man who never smoked has a 2.2-cm exophytic right tonsil '
                        'SCC that is p16-positive, confined to the tonsillar fossa, with a single '
                        'mobile 2-cm ipsilateral level II node and no radiographic extranodal '
                        'extension. CT shows a normal-caliber internal carotid artery well lateral '
                        'to the tumor, and PET-CT shows no distant disease. Mouth opening is '
                        'normal. Which treatment approach is most appropriate?',
                'choices': ['Transoral resection with neck dissection, or definitive radiation',
                            'Composite resection with mandibulotomy and free flap',
                            'Radiation to the primary site only, sparing both necks',
                            'Induction chemotherapy followed by chemoradiation'],
                'answer': 0,
                'explanation': 'HPV-associated oropharyngeal cancer is staged with its own system '
                               '(AJCC 9 for HPV-associated disease), and this cT2 cN1 tumor is '
                               'clinical stage I with an excellent prognosis. Single-modality '
                               'treatment is the goal: transoral surgery with ipsilateral neck '
                               'dissection, followed by pathology-directed adjuvant therapy, or '
                               'definitive radiation, which for a well-lateralized tonsil primary '
                               'can often be limited to the ipsilateral neck. Choice between them '
                               'weighs expected function and the chance that surgery will need '
                               'adjuvant treatment.',
                'why_wrong': ['Correct.',
                              'Open mandibulotomy is reserved for advanced tumors not reachable '
                              'transorally and adds morbidity unnecessary for a small '
                              'fossa-confined primary.',
                              'A node-positive neck must be treated; well-lateralized tonsil '
                              'cancers may spare the contralateral neck but not the involved side.',
                              'Induction chemotherapy has no proven benefit and adds toxicity for '
                              'low-volume, early-stage HPV-associated disease.'],
                'board_pearl': 'Early HPV-associated tonsil SCC: single-modality transoral surgery '
                               'with neck dissection, or definitive radiation.',
                'curveball': 'He chooses transoral surgery. Which findings on final pathology '
                             'would intensify his adjuvant therapy?',
                'curveball_answer': 'A positive margin or extranodal extension are the major '
                                    'triggers for postoperative chemoradiation in fit patients, '
                                    'though de-escalation for HPV-associated disease with minor '
                                    'extranodal extension is being studied. Multiple nodes, pT3 or '
                                    'pT4 disease, perineural invasion, and lymphovascular invasion '
                                    'support postoperative radiation alone. Under AJCC 9, '
                                    'extranodal extension also raises the pathologic N category.'},
 'v145_hn_20': {'stem': 'A 57-year-old woman has a p16-positive 2.5-cm left tonsil SCC confined to '
                        'the tonsillar fossa. Contrast CT shows three matted level II nodes up to '
                        '3.5 cm with irregular, spiculated margins and infiltration into the '
                        'sternocleidomastoid muscle. She is fit, and transoral exposure is '
                        'excellent on examination. Her surgeon and radiation oncologist both see '
                        'her. Which finding most favors definitive chemoradiation over transoral '
                        'surgery?',
                'choices': ['A primary tumor of 2.5 cm in the tonsillar fossa',
                            'Matted nodes infiltrating the adjacent muscle',
                            'Positive p16 staining of the primary tumor',
                            'Excellent transoral exposure on examination'],
                'answer': 1,
                'explanation': 'Transoral surgery for early oropharyngeal cancer is attractive '
                               'when it can be the main treatment, with adjuvant therapy reduced '
                               'or avoided. Matted nodes with irregular margins and muscle '
                               'infiltration indicate radiographic extranodal extension, which '
                               'predicts pathologic extranodal extension. That would require '
                               'postoperative chemoradiation, producing trimodality therapy with '
                               'the combined morbidity of surgery, radiation, and cisplatin '
                               'without an oncologic advantage. Definitive chemoradiation avoids '
                               'stacking treatments, so predicted nodal pathology drives the '
                               'choice.',
                'why_wrong': ['A small primary confined to the fossa is ideal for transoral '
                              'resection and does not by itself favor chemoradiation.',
                              'Correct.',
                              'HPV positivity improves prognosis with either modality and does not '
                              'decide between surgery and radiation.',
                              'Good exposure makes transoral resection feasible; it is a factor '
                              'favoring surgery rather than chemoradiation.'],
                'board_pearl': 'Choose transoral surgery when it can stand alone; predicted '
                               'extranodal extension means trimodality therapy, so favor '
                               'chemoradiation.',
                'curveball': 'After transoral surgery in a different patient, which pathologic '
                             'findings most strongly escalate adjuvant therapy?',
                'curveball_answer': 'A positive microscopic margin and pathologic extranodal '
                                    'extension are the classic findings that escalate '
                                    'postoperative treatment to concurrent chemoradiation in fit '
                                    'patients. Other adverse features, such as several positive '
                                    'nodes, perineural or lymphovascular invasion, and pT3 to pT4 '
                                    'disease, typically support radiation alone. Trials are '
                                    'testing whether HPV-associated disease with minimal '
                                    'extranodal extension can avoid chemotherapy.'},
 'v220_hn_tonsil_fnd': {'stem': 'A 52-year-old man who never smoked has a 6-week history of a '
                                'painless left neck mass. Examination shows an asymmetric, firm '
                                'left tonsil, and ultrasound shows a 3-cm cystic level II node. '
                                'Biopsy of the tonsil shows nonkeratinizing squamous cell '
                                'carcinoma. MRI shows no extension beyond the oropharynx, and '
                                'chest CT is clear. Which additional pathology test is essential '
                                'for staging?',
                        'choices': ['EBV-encoded RNA in situ hybridization',
                                    'PD-L1 combined positive score',
                                    'p16 immunohistochemistry',
                                    'EGFR expression by immunostaining'],
                        'answer': 2,
                        'explanation': 'The palatine tonsil is an oropharyngeal subsite, and '
                                       'HPV-associated oropharyngeal SCC is staged separately from '
                                       'HPV-negative disease. p16 immunohistochemistry is the '
                                       'accepted surrogate for HPV and determines whether the '
                                       'HPV-associated staging system (AJCC 9 as of 2026) or the '
                                       'HPV-negative system applies. Strong diffuse p16 staining '
                                       'predicts much better survival and response to therapy. The '
                                       'young never-smoker, cystic node, and nonkeratinizing '
                                       'histology all point toward HPV, but testing is still '
                                       'required.',
                        'why_wrong': ['EBV testing helps when a nasopharyngeal primary is '
                                      'suspected, but this tumor arises in the tonsil and needs '
                                      'HPV assessment.',
                                      'PD-L1 scoring guides systemic therapy in recurrent or '
                                      'metastatic disease but plays no role in staging.',
                                      'Correct.',
                                      'EGFR is expressed in most HNSCC and does not influence '
                                      'staging or the choice of cetuximab.'],
                        'board_pearl': 'Every oropharyngeal SCC needs p16 testing; it selects the '
                                       'HPV-associated staging system.',
                        'curveball': 'How does p16-negative tonsil SCC differ from p16-positive '
                                     'disease in prognosis and staging?',
                        'curveball_answer': 'p16-negative oropharyngeal SCC is typically '
                                            'tobacco-related and has substantially worse survival. '
                                            'It is staged with the AJCC 8 HPV-negative oropharynx '
                                            'system, which uses classic nodal criteria including '
                                            'extranodal extension. Patients are not candidates for '
                                            'de-escalation trials and are more likely to need '
                                            'intensified multimodality therapy.'},
 'v220_hn_tonsil_app': {'stem': 'A 60-year-old man has a p16-positive 2-cm right tonsil SCC '
                                'confined to the fossa with a single 2-cm level II node. He is '
                                'being considered for transoral robotic radical tonsillectomy with '
                                'neck dissection. Preoperative contrast CT shows that the right '
                                'internal carotid artery courses medially and lies immediately '
                                'deep to the tumor bed, with only a thin superior constrictor '
                                'between them. Which preoperative finding most directly threatens '
                                'the safety of transoral resection?',
                        'choices': ['A single 2-cm ipsilateral level II node without extranodal '
                                    'extension',
                                    'A medialized internal carotid lying just deep to the '
                                    'tonsillar fossa',
                                    'A primary tumor 2 cm in size that is confined to the '
                                    'tonsillar fossa',
                                    'A tortuous ipsilateral facial artery near the submandibular '
                                    'gland'],
                        'answer': 1,
                        'explanation': 'Radical tonsillectomy removes the constrictor and enters '
                                       'the parapharyngeal fat, so the deep margin lies near the '
                                       'internal carotid artery. A medialized or retropharyngeal '
                                       'carotid, seen on preoperative imaging, places the vessel '
                                       'at risk during dissection and may make a safe deep margin '
                                       'impossible transorally. Imaging review before transoral '
                                       'surgery should define carotid position, deep extension, '
                                       'and exposure. When the carotid is medialized, definitive '
                                       'radiation or an open approach is usually safer.',
                        'why_wrong': ['A small node without extranodal extension is managed by '
                                      'neck dissection and does not affect the safety of the '
                                      'transoral resection.',
                                      'Correct.',
                                      'A small tumor confined to the fossa is the ideal transoral '
                                      'case rather than a contraindication.',
                                      'The facial artery is addressed during neck dissection and '
                                      'can be ligated to reduce bleeding risk, not a '
                                      'contraindication.'],
                        'board_pearl': 'Before transoral tonsil surgery, check imaging for a '
                                       'medialized internal carotid artery.',
                        'curveball': 'What postoperative bleeding pattern after transoral surgery '
                                     'requires immediate airway and operative escalation?',
                        'curveball_answer': 'A sentinel bleed or brisk bleeding, especially if '
                                            'recurrent after initial control or causing airway '
                                            'compromise, demands securing the airway first, often '
                                            'by intubation or tracheostomy, then urgent operative '
                                            'control. External carotid branch ligation during neck '
                                            'dissection reduces severity. If the source is the '
                                            'carotid or is not controllable, interventional '
                                            'angiography is needed.'},
 'v220_hn_tonsil_snr': {'stem': 'A 56-year-old man undergoes transoral radical tonsillectomy and '
                                'ipsilateral neck dissection for a p16-positive right tonsil SCC. '
                                'Pathology shows a 2.8-cm tumor with clear margins of 4 mm, no '
                                'perineural invasion, and 2 of 24 positive nodes, one with 3 mm of '
                                'extranodal extension. He is fit with normal renal function and '
                                'hearing. Which adjuvant plan is most consistent with current '
                                'standard guidelines?',
                        'choices': ['Observation, given HPV status and clear margins',
                                    'Radiation alone to about 60 Gy',
                                    'De-escalated 30 Gy radiation alone',
                                    'Radiation with concurrent cisplatin'],
                        'answer': 3,
                        'explanation': 'Extranodal extension is one of the two classic high-risk '
                                       'postoperative features, with a positive margin, and NCCN '
                                       'guidance supports adding concurrent cisplatin to '
                                       'postoperative radiation in fit patients. Under AJCC 9 for '
                                       'HPV-associated disease, extranodal extension now upstages '
                                       'pathologic N, so two nodes with extranodal extension '
                                       'become pN2. Whether HPV-associated tumors with limited '
                                       'extranodal extension can safely omit chemotherapy is being '
                                       'tested in trials such as PATHOS, so de-escalation remains '
                                       'investigational.',
                        'why_wrong': ['Nodal disease with extranodal extension carries significant '
                                      'regional risk, so observation is inappropriate despite '
                                      'clear margins.',
                                      'Radiation alone is reasonable for intermediate-risk '
                                      'features, but extranodal extension is a standard indication '
                                      'to add cisplatin.',
                                      'Very low-dose regimens are investigational and are not '
                                      'standard for a patient with extranodal extension.',
                                      'Correct.'],
                        'board_pearl': 'After transoral surgery, a positive margin or extranodal '
                                       'extension calls for postoperative chemoradiation outside '
                                       'trials.',
                        'curveball': 'How does a positive surgical margin compare with extranodal '
                                     'extension as a trigger for adjuvant treatment?',
                        'curveball_answer': 'Both are major high-risk features supporting '
                                            'concurrent chemoradiation in a fit patient. A '
                                            'positive margin may first prompt re-resection if it '
                                            'can be achieved transorally, because clear margins '
                                            'may permit radiation alone. Close margins, perineural '
                                            'invasion, lymphovascular invasion, and multiple nodes '
                                            'are intermediate-risk features that support radiation '
                                            'without automatic chemotherapy.'},
 'v138_hn_25': {'stem': 'A 65-year-old man with a T4a glottic SCC eroding the thyroid cartilage is '
                        'scheduled for total laryngectomy. He has had a tracheostomy before for '
                        'pneumonia and assumes this will be similar. He asks what will change in '
                        'how he breathes and whether the neck opening can be closed later. Which '
                        'counseling point about the surgery is most accurate?',
                'choices': ['He will breathe through a neck stoma permanently',
                            'Food may still enter his lungs through the new pharynx',
                            'Nasal breathing returns once the stoma has matured',
                            'The stoma can be closed once he can swallow safely'],
                'answer': 0,
                'explanation': 'Total laryngectomy removes the larynx and sutures the trachea to '
                               'the skin as an end stoma, permanently separating the airway from '
                               'the pharynx. Unlike a tracheostomy, which leaves an intact upper '
                               'airway and can be decannulated, the stoma is the only route for '
                               'breathing, and it cannot be closed. Consequences include loss of '
                               'laryngeal voice, loss of nasal warming, humidification and smell, '
                               'and lifelong stoma care, but aspiration through a native larynx is '
                               'eliminated.',
                'why_wrong': ['Correct.',
                              'Because the airway and food passage are separated, aspiration '
                              'through the pharynx is eliminated after laryngectomy.',
                              'Nasal airflow is permanently lost because the trachea no longer '
                              'connects to the pharynx or nose.',
                              'Laryngectomy stomas cannot be closed because they are the only '
                              'airway; only tracheostomies can be decannulated.'],
                'board_pearl': 'Laryngectomy separates airway and food passage permanently; the '
                               'stoma is the only airway and never closes.',
                'curveball': 'After surgery, which clinical signs suggest that he has developed a '
                             'pharyngocutaneous fistula?',
                'curveball_answer': 'Fever, neck erythema, swelling, and tenderness, often between '
                                    'days 5 and 10 or when oral intake starts, together with '
                                    'saliva or cloudy drainage from the wound or drain, suggest a '
                                    'fistula. Suspicion prompts holding oral intake, opening the '
                                    'wound, and a contrast swallow or methylene blue test to '
                                    'confirm.'},
 'v140_hn_02': {'stem': 'A 67-year-old man is on postoperative day 5 after salvage total '
                        'laryngectomy following chemoradiation. He has a temperature of 38.3 C, '
                        'and the skin above the stoma is red and indurated. His neck drain output, '
                        'previously serosanguinous, has become cloudy and frothy, and it turns '
                        'blue within minutes after he swallows a small amount of methylene blue. '
                        'What is the most likely diagnosis?',
                'choices': ['Chyle leak from thoracic duct injury',
                            'Infected seroma without mucosal breakdown',
                            'Pharyngocutaneous fistula',
                            'Tracheal necrosis at the stoma'],
                'answer': 2,
                'explanation': 'Saliva entering the neck through a breakdown in the pharyngeal '
                               'closure creates a pharyngocutaneous fistula. It typically presents '
                               'around days 5 to 10 with fever, erythema, and induration, and '
                               'cloudy or frothy drainage; methylene blue appearing in the drain '
                               'after swallowing confirms communication with the pharynx. Salvage '
                               'surgery after chemoradiation is the strongest risk factor, along '
                               'with malnutrition, hypothyroidism, and closure tension. Management '
                               'depends on size, sepsis, and whether the carotid is exposed.',
                'why_wrong': ['A chyle leak produces milky drainage that rises with fatty feeds '
                              'and would not turn blue after swallowed dye.',
                              'A seroma with superinfection would not connect to the pharynx, so '
                              'swallowed dye would not appear in the drain.',
                              'Correct.',
                              'Stomal necrosis causes dark, crusted mucosa at the stoma rather '
                              'than swallowed dye appearing in the neck drain.'],
                'board_pearl': 'Fever, erythema, and saliva in the drain around day 5 to 10 after '
                               'laryngectomy: pharyngocutaneous fistula.',
                'curveball': 'When does a fistula need vascularized tissue coverage rather than '
                             'conservative wound care alone?',
                'curveball_answer': 'Vascularized coverage, usually a pectoralis major flap or '
                                    'free flap, is needed when the carotid is exposed or '
                                    'threatened, the fistula is large or high-output, there is '
                                    'necrosis or uncontrolled infection, or conservative care '
                                    'fails over several weeks. Irradiated fields heal poorly and '
                                    'lower the threshold for operative repair.'},
 'v148_hn_01': {'stem': 'A 72-year-old woman who had total laryngectomy 3 years ago arrives in the '
                        'emergency department with severe dyspnea after a week of a cold. Oxygen '
                        'saturation is 82 percent. A paramedic has placed a nonrebreather mask '
                        'over her mouth and nose without improvement. A thick plug of dried mucus '
                        'is visible occluding the stoma, and she is still awake. What is the most '
                        'appropriate immediate action?',
                'choices': ['Perform orotracheal intubation with video laryngoscopy',
                            'Give nebulized saline by face mask to loosen the plug',
                            'Extract the mucus plug and apply oxygen at the stoma',
                            'Add bag-mask ventilation over the mouth and nose'],
                'answer': 2,
                'explanation': 'After total laryngectomy the trachea ends at the neck stoma and '
                               'has no connection to the mouth or nose. Oxygen through a face '
                               'mask, bag-mask ventilation over the face, and oral intubation '
                               'cannot reach the lungs. The obstruction is at the stoma, so the '
                               'immediate step is to remove the plug with forceps and suction, '
                               'then deliver oxygen directly to the stoma. If she deteriorates, a '
                               'cuffed tube is placed through the stoma for ventilation. '
                               'Humidification prevents recurrence.',
                'why_wrong': ['Oral intubation cannot reach the trachea after laryngectomy because '
                              'the larynx has been removed and the airway ends at the stoma.',
                              'Face mask nebulization goes to the pharynx, not the lungs, and '
                              'delays clearing the obstructing plug.',
                              'Correct.',
                              'Bag-mask ventilation over the face inflates the pharynx and '
                              'stomach, not the lungs, in a patient without a larynx.'],
                'board_pearl': 'Laryngectomy airway emergency: look at the neck; clear the stoma '
                               'and oxygenate through it.',
                'curveball': 'How would this emergency differ in a patient with a tracheostomy and '
                             'an intact larynx?',
                'curveball_answer': 'A tracheostomy patient usually retains a connection between '
                                    'the upper airway and the lungs. The tracheostomy tube is '
                                    'checked and the inner cannula changed first, and the tube is '
                                    'replaced if obstructed. If the stoma cannot be cannulated, '
                                    'oxygen by face mask and even oral intubation may still work, '
                                    'which never applies after laryngectomy.'},
 'v148_hn_02': {'stem': 'A 62-year-old man undergoes primary total laryngectomy for a T4a '
                        'supraglottic SCC with no prior radiation. After the larynx is removed, '
                        'the remaining pharyngeal mucosa is healthy, well-perfused, and about 5 cm '
                        'wide, and his albumin is normal. The resident asks how to close the '
                        'neopharynx to minimize the risk of a pharyngocutaneous fistula. Which '
                        'closure plan is most appropriate?',
                'choices': ['Routine pectoralis onlay over every primary closure',
                            'Tension-free inverted closure checked for leaks',
                            'Single-layer everting closure to maximize lumen',
                            'Routine salivary bypass tube left for 3 weeks'],
                'answer': 1,
                'explanation': 'Fistula risk depends on tissue quality, tension, and technique. In '
                               'a nonirradiated patient with healthy, adequate mucosa, the key '
                               'principles are a tension-free, watertight, mucosa-inverting '
                               'closure, often in a T or vertical configuration with a second '
                               'layer of constrictor muscle, and testing the closure for leaks '
                               'before closing the neck. Vascularized onlay flaps are reserved for '
                               'higher-risk salvage settings. Correcting malnutrition and '
                               'hypothyroidism further reduces fistula risk.',
                'why_wrong': ['A pectoralis onlay is valuable in irradiated salvage fields but '
                              'adds unnecessary morbidity in a healthy, nonirradiated closure.',
                              'Correct.',
                              'Everting closures place mucosa into the wound and leak more often; '
                              'inverted mucosal closures are standard.',
                              'Salivary bypass tubes may help selected high-risk or reconstructed '
                              'cases but are not needed routinely after a healthy primary '
                              'closure.'],
                'board_pearl': 'Laryngectomy closure: tension-free, inverted, watertight, and '
                               'tested; add vascularized tissue only when risk is high.',
                'curveball': 'When would a pectoralis or free-tissue reinforcement flap be '
                             'particularly valuable at total laryngectomy?',
                'curveball_answer': 'Vascularized reinforcement is most valuable in salvage '
                                    'laryngectomy after radiation or chemoradiation, when mucosa '
                                    'is fibrotic or under tension, when a partial pharyngectomy '
                                    'leaves a narrow remnant, and when malnutrition, diabetes, or '
                                    'hypothyroidism impair healing. It reduces fistula rate and '
                                    'severity and covers the carotid if breakdown occurs.'},
 'v154_hn_fnd': {'stem': 'A 68-year-old man had total laryngectomy without radiation for a T4a '
                         'laryngeal SCC 6 months ago. He uses a tracheoesophageal prosthesis and '
                         'is eating normally. He complains that food tastes bland and he cannot '
                         'smell smoke or his coffee. Nasal endoscopy is normal, and he has no '
                         'history of sinus disease or head injury. Which explanation best accounts '
                         'for his symptom?',
                 'choices': ['Injury to olfactory fibers from the neck dissection',
                             'Atrophy of the olfactory epithelium from radiation',
                             'Chronic rhinosinusitis caused by the lost nasal airflow',
                             'Inspired air bypasses the nose and enters at the stoma'],
                 'answer': 3,
                 'explanation': 'Total laryngectomy permanently separates the trachea from the '
                                'pharynx, so all inspired air enters through the neck stoma. '
                                'Without nasal airflow, odorants do not reach the olfactory cleft, '
                                'causing hyposmia and reduced flavor perception even though the '
                                'olfactory epithelium and nerves are intact. Taste through the '
                                'tongue persists, but flavor depends heavily on smell. Speech '
                                'pathologists teach the nasal airflow-inducing maneuver, a polite '
                                'yawn with the lips closed, which draws air through the nose and '
                                'restores some smell.',
                 'why_wrong': ['The olfactory nerves lie in the anterior skull base and are not '
                               'exposed during laryngectomy or neck dissection.',
                               'He received no radiation, and the problem is lack of airflow to '
                               'the olfactory cleft rather than epithelial injury.',
                               'His nasal endoscopy is normal, and reduced nasal airflow does not '
                               'typically cause chronic rhinosinusitis.',
                               'Correct.'],
                 'board_pearl': 'After laryngectomy, all air enters through the stoma; loss of '
                                'nasal airflow causes hyposmia, helped by the polite yawn '
                                'maneuver.',
                 'curveball': 'Why does this airway anatomy matter when a code team is called for '
                              'this patient?',
                 'curveball_answer': 'The mouth and nose no longer connect to the lungs, so face '
                                     'mask oxygen, bag-mask ventilation over the face, and oral '
                                     'intubation will not oxygenate him. Oxygen and ventilation go '
                                     'to the stoma, with a pediatric mask or a cuffed tube placed '
                                     'through it after any obstruction is removed. Bedside signage '
                                     'helps prevent errors.'},
 'v154_hn_app': {'stem': 'A 70-year-old man who had total laryngectomy 2 years ago is found '
                         'unresponsive and apneic on the ward. The rapid response team has already '
                         'removed a crust from the stoma and confirmed that a suction catheter '
                         'passes freely into the trachea. He remains apneic with a pulse, and '
                         'oxygen saturation is 78 percent. Which method of ventilation is most '
                         'appropriate?',
                 'choices': ['Bag-mask ventilation sealed over the mouth and nose',
                             'Orotracheal intubation using video laryngoscopy',
                             'Needle cricothyrotomy with jet ventilation',
                             'Cuffed tube placed in the stoma and bagged'],
                 'answer': 3,
                 'explanation': 'After total laryngectomy the stoma is the only path to the lungs, '
                                'so ventilation must be delivered through it. With the obstruction '
                                'cleared, a cuffed endotracheal or tracheostomy tube placed a '
                                'short distance into the stoma allows effective positive-pressure '
                                'ventilation and protects against leak; a pediatric face mask over '
                                'the stoma is a temporary alternative. Mouth and nose routes '
                                'ventilate only the pharynx. There is no larynx or cricothyroid '
                                'membrane for a cricothyrotomy.',
                 'why_wrong': ['Bag-mask ventilation over the face inflates only the pharynx and '
                               'esophagus because the trachea is not connected to the mouth.',
                               'Oral intubation cannot reach the trachea after laryngectomy, since '
                               'the larynx has been removed and the trachea ends at the stoma.',
                               'The cricothyroid membrane was removed with the larynx, and the '
                               'stoma already provides direct tracheal access.',
                               'Correct.'],
                 'board_pearl': 'Ventilating a laryngectomee: cuffed tube or small mask at the '
                                'stoma, never the face.',
                 'curveball': 'How would management differ in an apneic tracheostomy patient with '
                              'an intact larynx?',
                 'curveball_answer': 'In a tracheostomy patient, ventilate through the '
                                     'tracheostomy tube first after checking patency and changing '
                                     'the inner cannula. If it is blocked or dislodged, the stoma '
                                     'can be covered and the patient ventilated by bag-mask or '
                                     'intubated orally, because the upper airway still connects to '
                                     'the lungs.'},
 'v154_hn_snr': {'stem': 'A 64-year-old man undergoes salvage total laryngectomy with partial '
                         'pharyngectomy for recurrent SCC 18 months after chemoradiation. After '
                         'resection, the remaining pharyngeal mucosa is fibrotic and only about 3 '
                         'cm wide. Approximating it would require visible tension and leave a '
                         'narrow lumen. A pectoralis major flap and anterolateral thigh donor '
                         'sites are both available. Which decision most directly addresses his '
                         'fistula and stricture risk?',
                 'choices': ['Close under tension and add a pectoralis onlay over it',
                             'Close primarily and place a salivary bypass tube',
                             'Close primarily and keep him without oral intake for 4 weeks',
                             'Patch the defect with vascularized skin for a wider lumen'],
                 'answer': 3,
                 'explanation': 'Fistula risk is highest when irradiated, fibrotic mucosa is '
                                'closed under tension, and a narrow remnant also risks stricture '
                                'and dysphagia. When primary closure cannot be achieved without '
                                'tension, the defect should be augmented with vascularized tissue '
                                'as a patch, such as an anterolateral thigh free flap or a '
                                'pectoralis myocutaneous flap, rather than forced closed. This '
                                'restores lumen width and brings unirradiated tissue to the suture '
                                'lines.',
                 'why_wrong': ['An onlay cannot compensate for a closure under tension, which '
                               'still risks dehiscence and a narrow, strictured neopharynx.',
                               'A bypass tube may reduce fistula consequences but does not relieve '
                               'closure tension or prevent stricture.',
                               'Prolonged fasting does not fix a closure under tension and delays '
                               'nutrition and rehabilitation.',
                               'Correct.'],
                 'board_pearl': 'Narrow irradiated pharyngeal remnant: patch with vascularized '
                                'skin rather than forcing a tight primary closure.',
                 'curveball': 'What patient and wound factors would push you toward prophylactic '
                              'flap reinforcement even when closure is tension-free?',
                 'curveball_answer': 'Prior radiation or chemoradiation, especially to high doses, '
                                     'fibrotic or poorly perfused mucosa, malnutrition with low '
                                     'albumin, hypothyroidism, diabetes, prior neck surgery, and '
                                     'an extended pharyngectomy all favor prophylactic '
                                     'vascularized onlay. Evidence suggests a pectoralis onlay or '
                                     'free flap lowers fistula rates in salvage laryngectomy.'},
 'v221_hn_tl_fnd': {'stem': 'A 66-year-old man is about to be discharged 2 weeks after total '
                            'laryngectomy. He enjoys swimming and fishing, and his wife asks what '
                            'safety precautions to take at home. He has a stoma without a tube, '
                            'uses a heat and moisture exchanger, and is learning electrolarynx '
                            'speech. Which counseling point follows most directly from his new '
                            'airway anatomy?',
                    'choices': ['Swimming is safe if he keeps his mouth closed',
                                'Shield the stoma from shower water entering the airway',
                                'Rescue breathing works by mouth-to-mouth as before',
                                'Cover the stoma with an occlusive dressing at night'],
                    'answer': 1,
                    'explanation': 'Total laryngectomy brings the trachea to the skin as an end '
                                   'stoma that is completely separated from the mouth and nose. '
                                   'Water entering the stoma goes directly into the lungs, so '
                                   'showering requires a stoma shield, and swimming is unsafe '
                                   'without specialized equipment. Rescue breathing must be '
                                   'mouth-to-stoma, and the stoma must never be occluded. Patients '
                                   'should carry identification and their family should learn '
                                   'stoma-based resuscitation.',
                    'why_wrong': ['The mouth no longer connects to the trachea, so closing it does '
                                  'nothing to stop water entering the open stoma.',
                                  'Correct.',
                                  'Mouth-to-mouth breaths reach only the pharynx and stomach; '
                                  'rescue breaths must be delivered to the stoma.',
                                  'An occlusive dressing would block his only airway; filters such '
                                  'as a heat and moisture exchanger must stay breathable.'],
                    'board_pearl': 'Laryngectomees breathe only through the stoma: protect it from '
                                   'water and resuscitate through it.',
                    'curveball': 'How does this differ from a patient with a tracheostomy whose '
                                 'larynx remains connected to the trachea?',
                    'curveball_answer': 'With a tracheostomy, the upper airway still communicates '
                                        'with the lungs, so the patient may breathe around a '
                                        'capped tube, can usually be ventilated or intubated '
                                        'orally in an emergency, and may eventually be '
                                        'decannulated. Water aspiration risk exists but the mouth '
                                        'and nose remain part of the airway.'},
 'v221_hn_tl_app': {'stem': 'A 63-year-old woman is on postoperative day 6 after salvage total '
                            'laryngectomy. She has a temperature of 38.1 C, neck erythema, and '
                            'saliva leaking from a 1-cm opening in the incision below the chin. '
                            'Contrast swallow shows a small leak from the pharyngeal closure '
                            'tracking anteriorly, away from the carotid. She is hemodynamically '
                            'stable, TSH is elevated, and albumin is 2.8 g/dL. What is the most '
                            'appropriate initial management?',
                    'choices': ['Return to the operating room for an immediate pectoralis flap',
                                'Continue her oral diet, since small fistulas close spontaneously',
                                'Hold oral intake, open and pack the wound, and treat infection',
                                'Start postoperative radiation early to promote wound sealing'],
                    'answer': 2,
                    'explanation': 'Most small, low-output pharyngocutaneous fistulas without '
                                   'carotid exposure heal with conservative care. That includes '
                                   'stopping oral intake and feeding by tube, opening and packing '
                                   'the wound to drain saliva away from the vessels, '
                                   'culture-directed antibiotics, and correcting healing barriers '
                                   'such as malnutrition and hypothyroidism, both present here. '
                                   'Radiation is a major risk factor for fistula, and '
                                   'postoperative hypothyroidism is common and should be treated. '
                                   'Operative repair is reserved for failed conservative care or '
                                   'threatened vessels.',
                    'why_wrong': ['Immediate flap repair is reserved for large fistulas, carotid '
                                  'exposure, or failed conservative care, none of which is '
                                  'present.',
                                  'Continued oral intake pushes saliva and food through the leak, '
                                  'perpetuating infection and delaying closure.',
                                  'Correct.',
                                  'Radiation impairs wound healing and is a major risk factor for '
                                  'fistula, so it does not promote sealing.'],
                    'board_pearl': 'Small fistula without carotid exposure: no oral intake, wound '
                                   'drainage and packing, antibiotics, and correct nutrition and '
                                   'thyroid.',
                    'curveball': 'Which findings make conservative fistula care unsafe and push '
                                 'toward operative debridement or vascularized coverage?',
                    'curveball_answer': 'Exposed or threatened carotid artery, a large or '
                                        'expanding high-output fistula, necrotic tissue or '
                                        'uncontrolled infection, a sentinel bleed, or failure to '
                                        'improve after several weeks of conservative care all call '
                                        'for operative debridement and vascularized coverage, '
                                        'usually a pectoralis major flap or free flap, to protect '
                                        'the vessels and close the tract.'},
 'v221_hn_tl_snr': {'stem': 'A 69-year-old man undergoes salvage total laryngectomy 2 years after '
                            'chemoradiation for glottic SCC. The remaining pharyngeal mucosa is '
                            'wide enough for a tension-free primary closure, but the tissues are '
                            'woody and bleed poorly. He has diabetes and an albumin of 3.0 g/dL. '
                            'The pectoralis major is available. Which reconstructive step should '
                            'be considered at the index operation?',
                    'choices': ['Primary closure plus 3 weeks with no oral intake',
                                'Primary closure, adding a flap only if a fistula develops',
                                'Pectoralis major myofascial onlay over the closure',
                                'Free jejunal interposition graft for the neopharynx'],
                    'answer': 2,
                    'explanation': 'Even when tension-free closure is possible, salvage '
                                   'laryngectomy after chemoradiation carries a high fistula rate '
                                   'because irradiated tissue heals poorly. Bringing unirradiated, '
                                   'vascularized tissue over the suture line, such as a pectoralis '
                                   'major myofascial onlay or a free flap, reduces the rate and '
                                   'severity of fistula and covers the carotid if breakdown '
                                   'occurs. His diabetes and low albumin add risk. Prolonged '
                                   'fasting alone does not change healing biology.',
                    'why_wrong': ['Prolonged fasting delays nutrition without improving the '
                                  'vascularity of irradiated tissue, which is the main risk '
                                  'factor.',
                                  'Waiting for a fistula forfeits prevention and means repairing '
                                  'an infected wound near the carotid in a poorly healing field.',
                                  'Correct.',
                                  'Jejunal interposition is used for circumferential defects; here '
                                  'enough mucosa remains for primary closure.'],
                    'board_pearl': 'Salvage laryngectomy after chemoradiation: consider '
                                   'prophylactic vascularized onlay even when closure is '
                                   'tension-free.',
                    'curveball': 'How do circumferential versus partial pharyngeal defects change '
                                 'flap selection and stricture risk?',
                    'curveball_answer': 'Partial defects can be patched with an anterolateral '
                                        'thigh, radial forearm, or pectoralis myocutaneous flap. '
                                        'Circumferential defects need a tubed fasciocutaneous '
                                        'flap, usually anterolateral thigh, or a free jejunum; '
                                        'gastric pull-up is reserved for defects extending into '
                                        'the thoracic esophagus. Circumferential reconstructions '
                                        'carry higher stricture rates, particularly at the distal '
                                        'anastomosis.'},
 'v138_hn_26': {'stem': 'A 47-year-old woman who never smoked has adenoid cystic carcinoma of the '
                        'upper trachea. CT shows a 3-cm intraluminal mass starting 2 cm below the '
                        'cricoid, with submucosal thickening extending about 1.5 cm beyond each '
                        'visible edge. There is no mediastinal invasion or distant disease. The '
                        'thoracic and head and neck surgeons plan segmental resection. Which '
                        'factor most limits the length of trachea that can be safely resected?',
                'choices': ['Microscopic perineural spread at the margins',
                            'Proximity of the recurrent laryngeal nerves',
                            'Preoperative FEV1 on spirometry',
                            'Tension on the end-to-end anastomosis'],
                'answer': 3,
                'explanation': 'Primary tracheal resection is limited by whether the ends can be '
                               'rejoined without excessive tension, which causes dehiscence, '
                               'stenosis, or fatal disruption. With neck flexion, pretracheal '
                               'mobilization, and release maneuvers, roughly half of the adult '
                               'trachea can be removed. Adenoid cystic carcinoma spreads '
                               'submucosally and perineurally beyond visible margins, so resection '
                               'length must be planned from imaging and endoscopy. When clear '
                               'margins would demand an unsafe length, surgeons accept microscopic '
                               'positive margins and give adjuvant radiation.',
                'why_wrong': ['Perineural spread commonly leaves microscopic positive margins, '
                              'which are accepted with adjuvant radiation rather than extending '
                              'resection beyond safe length.',
                              'The recurrent laryngeal nerves must be preserved during dissection '
                              'but do not set the maximum length of resection.',
                              'Pulmonary function influences fitness for surgery but does not '
                              'determine how much trachea can be removed and reconstructed.',
                              'Correct.'],
                'board_pearl': 'Tracheal resection length is limited by anastomotic tension; about '
                               'half the adult trachea with release maneuvers.',
                'curveball': 'After the anastomosis is completed, what postoperative measure '
                             'reduces tension on a cervical tracheal anastomosis?',
                'curveball_answer': 'A chin-to-chest guardian suture, placed from the submental '
                                    'skin to the presternal skin, keeps the neck flexed for about '
                                    'a week and prevents sudden extension that would pull the '
                                    'anastomosis apart. Early extubation, avoidance of a cuff at '
                                    'the anastomosis, and bronchoscopic checks before suture '
                                    'removal complete the protection.'},
 'v145_hn_21': {'stem': 'A 63-year-old man with a 50 pack-year history has 4 months of exertional '
                        'dyspnea and two episodes of hemoptysis. CT shows a 2.5-cm SCC of the mid '
                        'trachea involving 3 cm of length, with no extension into the esophagus or '
                        'mediastinal vessels and no nodal or distant disease. Bronchoscopy '
                        'confirms normal mucosa above and below. His cardiopulmonary function is '
                        'adequate. What is the most appropriate treatment?',
                'choices': ['Segmental resection with primary end-to-end anastomosis',
                            'Endoscopic core-out debulking followed by observation',
                            'Definitive radiation alone as the preferred initial therapy',
                            'Silicone stent placement followed by chemotherapy'],
                'answer': 0,
                'explanation': 'For a resectable primary tracheal malignancy, segmental resection '
                               'with primary anastomosis offers the best chance of cure. '
                               'Resectability depends on obtaining oncologic margins while '
                               'performing a tension-safe anastomosis, determined by length, '
                               'location, mediastinal invasion, and prior radiation. This 3-cm '
                               'lesion is well within the length that can be removed. '
                               'Postoperative radiation is commonly added for SCC, especially with '
                               'close margins or nodal disease. Radiation, debulking, and stents '
                               'are for unresectable disease.',
                'why_wrong': ['Correct.',
                              'Core-out relieves obstruction but leaves tumor in the wall, so it '
                              'is palliative rather than curative for resectable disease.',
                              'Radiation is reserved for unresectable tumors or as adjuvant '
                              'therapy; outcomes are inferior to resection when resection is '
                              'feasible.',
                              'Stenting with chemotherapy is a palliative approach for '
                              'unresectable or metastatic disease, not for a short resectable '
                              'lesion.'],
                'board_pearl': 'Resectable primary tracheal cancer: segmental resection with '
                               'primary anastomosis, often followed by radiation.',
                'curveball': 'Postoperatively, how is a high-risk tracheal anastomosis protected '
                             'from sudden neck extension?',
                'curveball_answer': 'A heavy chin-to-chest guardian suture holds the neck in '
                                    'flexion for about 7 days, combined with patient and nursing '
                                    'education. Early extubation avoids cuff pressure on the '
                                    'anastomosis, and bronchoscopy is done before the suture is '
                                    'removed to confirm healing.'},
 'v227_hn_trachca_fnd': {'stem': 'A 41-year-old woman who never smoked has been treated for asthma '
                                 'for 14 months with escalating inhalers and three courses of '
                                 'prednisone without benefit. She now has noisy breathing on '
                                 'exertion and blood-streaked sputum. Chest radiograph and peak '
                                 'flow variability are normal. Spirometry shows flattening of both '
                                 'inspiratory and expiratory limbs of the flow-volume loop. What '
                                 'is the most appropriate next step?',
                         'choices': ['Neck and chest CT focused on the central airway',
                                     'Methacholine challenge to confirm airway reactivity',
                                     'Add a long-acting bronchodilator to inhaled steroids',
                                     'Prolonged oral prednisone with a slow taper'],
                         'answer': 0,
                         'explanation': 'Fixed central airway obstruction, from a tracheal tumor '
                                        'or stenosis, mimics asthma but does not respond to '
                                        'bronchodilators or steroids. Symptoms appear only after '
                                        'the lumen is narrowed by roughly half or more. Flattening '
                                        'of both limbs of the flow-volume loop signals a fixed '
                                        'obstruction, and hemoptysis adds concern for tumor. The '
                                        'next step is anatomic evaluation with contrast CT, then '
                                        'bronchoscopy with a safe airway plan. Repeated empiric '
                                        'asthma treatment delays diagnosis.',
                         'why_wrong': ['Correct.',
                                       'Methacholine testing evaluates reactive airways, which '
                                       'does not explain hemoptysis and fixed flow-volume loop '
                                       'flattening.',
                                       'Escalating bronchodilator therapy repeats a strategy that '
                                       'has already failed and delays imaging of a fixed '
                                       'obstruction.',
                                       'Steroids have already failed and do not treat a structural '
                                       'tracheal lesion, while delaying diagnosis.'],
                         'board_pearl': 'Refractory asthma with a flat flow-volume loop or '
                                        'hemoptysis: image the central airway.',
                         'curveball': 'Imaging shows a tracheal mass. How does adenoid cystic '
                                      'carcinoma differ from SCC in spread and its implications '
                                      'for resection?',
                         'curveball_answer': 'Adenoid cystic carcinoma grows slowly with extensive '
                                             'submucosal and perineural spread beyond the visible '
                                             'edge, so margins are often microscopically positive; '
                                             'long survival is still possible and adjuvant '
                                             'radiation is added. SCC is smoking-related, tends to '
                                             'spread to nodes and distant sites, and usually has '
                                             'more defined margins.'},
 'v227_hn_trachca_app': {'stem': 'A 58-year-old man has stridor at rest and can speak only short '
                                 'sentences. CT shows a friable mass of the mid trachea narrowing '
                                 'the lumen by about 80 percent over 3 cm, with no mediastinal '
                                 'invasion. He is able to lie at 30 degrees, with oxygen '
                                 'saturation 93 percent. The team plans to confirm histology and '
                                 'then resect. What is the safest initial airway strategy?',
                         'choices': ['Rigid bronchoscopy with spontaneous ventilation and core-out',
                                     'Rapid-sequence induction and standard endotracheal '
                                     'intubation',
                                     'Awake flexible bronchoscopy with biopsy in the clinic',
                                     'Tracheostomy under local anesthesia through the tumor site'],
                         'answer': 0,
                         'explanation': 'A critically narrowed trachea is both an oncologic and an '
                                        'airway problem. Muscle relaxation can collapse a '
                                        'borderline airway, and a standard tube may not pass or '
                                        'may cause bleeding. In the operating room with surgery '
                                        'and anesthesia present, rigid bronchoscopy with '
                                        'spontaneous ventilation allows inspection, biopsy, and '
                                        'core-out to restore the lumen, with rescue options and '
                                        'sometimes extracorporeal support on standby. Once '
                                        'stabilized, he can be staged and planned for segmental '
                                        'resection with a tension-free anastomosis.',
                         'why_wrong': ['Correct.',
                                       'Paralysis can convert partial to complete obstruction, and '
                                       'a tube may not pass an 80 percent stenosis.',
                                       'Biopsy of a friable, critically obstructing lesion outside '
                                       'the operating room risks bleeding and complete obstruction '
                                       'without rescue options.',
                                       'A tracheostomy through tumor seeds the field and may not '
                                       'bypass a mid-tracheal lesion below the stoma.'],
                         'board_pearl': 'Never biopsy a critically obstructing tracheal tumor '
                                        'without a ventilation and rescue plan; rigid bronchoscopy '
                                        'in the OR.',
                         'curveball': 'How would a tumor arising within 1 cm of the cricoid change '
                                      'the resection and airway plan?',
                         'curveball_answer': 'Tumor near the cricoid requires laryngotracheal '
                                             'resection, such as partial cricoid resection with '
                                             'thyrotracheal anastomosis, which places the '
                                             'recurrent laryngeal nerves at higher risk. A '
                                             'tracheostomy cannot bypass the lesion, so jet '
                                             'ventilation or cross-field intubation of the distal '
                                             'trachea is planned. Glottic edema is common, and '
                                             'some patients need a temporary tracheostomy below '
                                             'the anastomosis.'},
 'v227_hn_trachca_snr': {'stem': 'A 72-year-old man has primary tracheal SCC extending 7 cm from '
                                 'the upper trachea toward the carina, with circumferential wall '
                                 'thickening. He had mediastinal radiation for lymphoma 20 years '
                                 'ago. Surgeons estimate that clear margins would require '
                                 'resecting about 70 percent of his trachea, beyond safe '
                                 'anastomotic limits even with release maneuvers. There is no '
                                 'distant disease. What is the most appropriate management?',
                         'choices': ['Resect with laryngeal and hilar release despite expected '
                                     'tension',
                                     'Resect and bridge the gap with a long silicone T-tube',
                                     'Resect leaving gross tumor at the margins to shorten the '
                                     'segment',
                                     'Definitive chemoradiation, with endoscopic airway palliation '
                                     'as needed'],
                         'answer': 3,
                         'explanation': 'Resectability includes the ability to rebuild the airway '
                                        'safely. A resection beyond about half of the trachea, '
                                        'especially in a previously irradiated field, carries a '
                                        'prohibitive risk of anastomotic dehiscence, which is '
                                        'often fatal. In that situation the team should not force '
                                        'reconstruction, and nonsurgical treatment becomes '
                                        'appropriate: definitive radiation, often with concurrent '
                                        'chemotherapy, with debulking or stenting if obstruction '
                                        'threatens. Tracheal replacement remains investigational.',
                         'why_wrong': ['Release maneuvers gain only limited length and cannot make '
                                       'a 70 percent resection safe, particularly in irradiated '
                                       'tissue.',
                                       'Prosthetic bridging of a long tracheal gap is not reliable '
                                       'and risks migration, infection, and erosion into vessels.',
                                       'Leaving gross tumor to shorten the resection sacrifices '
                                       'oncologic benefit while keeping the surgical risks.',
                                       'Correct.'],
                         'board_pearl': 'If safe reconstruction is impossible, the tumor is '
                                        'unresectable: choose chemoradiation and airway '
                                        'palliation.',
                         'curveball': 'In a patient who does undergo tracheal resection, which '
                                      'postoperative findings suggest early anastomotic '
                                      'compromise?',
                         'curveball_answer': 'New stridor, voice change, subcutaneous or '
                                             'mediastinal emphysema, wound collection or '
                                             'infection, hemoptysis, and fever in the first week '
                                             'suggest dehiscence or anastomotic ischemia. Prompt '
                                             'flexible bronchoscopy confirms the problem, and '
                                             'management ranges from observation for small defects '
                                             'to reintubation, a T-tube, or tracheostomy for '
                                             'larger ones.'},
 'v138_hn_27': {'stem': 'A 49-year-old man who still smokes has a T1a SCC confined to the mid '
                        'third of the right vocal fold, with normal mobility and no anterior '
                        'commissure involvement. Exposure under suspension laryngoscopy is '
                        'excellent. He lives 3 hours from the nearest radiation center and works '
                        'as a truck driver. He asks what advantages laser surgery would offer over '
                        'radiation. Which advantage of transoral laser microsurgery is most '
                        'relevant?',
                'choices': ['Better voice than radiation even after deep resection',
                            'Higher local control than radiation for T1a tumors',
                            'A single treatment, margin pathology, and radiation in reserve',
                            'Avoids general anesthesia and suspension laryngoscopy'],
                'answer': 2,
                'explanation': 'For early glottic cancer, transoral laser microsurgery and '
                               'radiation give similar local control. Laser resection is a single, '
                               'short procedure with histologic margin assessment, which matters '
                               'for a patient who would otherwise travel daily for 6 weeks. It '
                               'also keeps radiation available for a recurrence or a second '
                               'primary, a real concern in a continuing smoker. Voice outcomes are '
                               'comparable for superficial resections but worsen with deeper '
                               'cordectomies, so voice is not a universal advantage.',
                'why_wrong': ['Voice after laser surgery depends on resection depth; deep '
                              'cordectomies usually give worse voice than radiation.',
                              'Local control for T1a glottic cancer is similar with laser surgery '
                              'and radiation; neither is clearly superior.',
                              'Correct.',
                              'Transoral laser microsurgery requires general anesthesia and '
                              'suspension laryngoscopy, unlike radiation.'],
                'board_pearl': 'TLM for early glottic cancer: one procedure, margin pathology, and '
                               'radiation saved for later.',
                'curveball': 'How does anterior commissure involvement complicate margin '
                             'assessment and recurrence risk after laser resection?',
                'curveball_answer': 'The anterior commissure is hard to expose, and its tendon '
                                    'inserts on thyroid cartilage with little intervening '
                                    'perichondrium, giving tumor a short path to cartilage. '
                                    'Margins are often close and difficult to assess, and local '
                                    'control after laser resection is lower. Webbing is common if '
                                    'both folds are resected together.'},
 'v145_hn_22': {'stem': 'A 66-year-old woman has a 2.5-cm T2 SCC of the right false vocal fold and '
                        'aryepiglottic fold with normal mobility. Exposure is good. During '
                        'transoral laser resection, the resident hesitates to cut through the '
                        'tumor because the textbook he read emphasized en bloc removal. The '
                        'attending prefers to divide the tumor to judge its depth. Which approach '
                        'reflects sound oncologic principle for this operation?',
                'choices': ['Transect the tumor to see depth, then orient each piece for pathology',
                            'Vaporize the tumor to char the bed and minimize specimen handling',
                            'Remove only the visible exophytic tumor to maximize preserved tissue',
                            'Insist on en bloc removal, converting to open surgery if needed'],
                'answer': 0,
                'explanation': 'Transoral laser microsurgery is controlled oncologic resection '
                               'under magnification, not burning out a tumor. Cutting through the '
                               'tumor lets the surgeon see its depth of invasion directly and '
                               'tailor margins in three dimensions while preserving uninvolved '
                               'tissue. Piecemeal resection is oncologically sound when every '
                               'piece is oriented, mapped, and sent with clear labeling, so '
                               'pathology can assess each margin. Outcomes from this technique are '
                               'equivalent to open partial laryngectomy for selected tumors.',
                'why_wrong': ['Correct.',
                              'Vaporization destroys tissue that pathology needs for margin '
                              'assessment, so the completeness of resection cannot be confirmed.',
                              'Removing only the exophytic part ignores deep invasion and leaves '
                              'residual tumor, defeating the oncologic purpose.',
                              'En bloc removal is not required; converting to open surgery for '
                              'that reason adds morbidity without improving control.'],
                'board_pearl': 'TLM: cut through the tumor to read depth, then map and orient '
                               'every piece.',
                'curveball': 'Exposure is poor, and the anterior commissure cannot be adequately '
                             'visualized. What should you do rather than force the transoral '
                             'approach?',
                'curveball_answer': 'Stop rather than resect blindly. Options are trying a '
                                    'different laryngoscope or positioning, then choosing '
                                    'definitive radiation or an open partial laryngectomy if '
                                    'exposure remains inadequate. Incomplete transoral resection '
                                    'under poor visualization risks positive margins and '
                                    'compromises later salvage.'},
 'v228_hn_tlm_fnd': {'stem': 'A 68-year-old man has a T1b glottic SCC involving both anterior '
                             'vocal folds and the anterior commissure. He has severe retrognathia, '
                             'a cervical spine fusion from C3 to C6, and prominent upper incisors. '
                             'Under general anesthesia, several laryngoscopes are tried, but the '
                             'anterior commissure cannot be seen even with external laryngeal '
                             'pressure. Which finding most strongly argues against transoral laser '
                             'microsurgery?',
                     'choices': ['Tumor confined to the folds with normal mobility',
                                 'Anterior commissure that cannot be exposed',
                                 'A smoking history of 40 pack-years',
                                 'Expected need for piecemeal resection'],
                     'answer': 1,
                     'explanation': 'Transoral laser microsurgery depends on complete, safe '
                                    'endoscopic exposure of the whole tumor, so its extent can be '
                                    'seen and resected with margins. Retrognathia, prominent '
                                    'incisors, and limited neck extension predict difficult '
                                    'exposure, and here the anterior commissure, the site most '
                                    'associated with close margins and recurrence, cannot be '
                                    'visualized at all. Forcing a transoral resection risks '
                                    'incomplete removal. Definitive radiation or open partial '
                                    'laryngectomy is preferable.',
                     'why_wrong': ['Tumor confined to the folds with normal mobility makes the '
                                   'lesion suitable for transoral surgery, not a contraindication.',
                                   'Correct.',
                                   'Smoking history influences surveillance and second primary '
                                   'risk but does not determine transoral feasibility.',
                                   'Piecemeal resection is a standard, oncologically sound part of '
                                   'laser microsurgery when pieces are oriented.'],
                     'board_pearl': 'No exposure, no TLM: the entire tumor must be visualized to '
                                    'be resected with margins.',
                     'curveball': 'Which dental, mandibular, cervical, and tumor factors predict '
                                  'difficult transoral laryngeal exposure?',
                     'curveball_answer': 'Prominent or protruding upper incisors, retrognathia, '
                                         'limited mouth opening or trismus, a short thick neck, '
                                         'limited cervical extension from fusion or arthritis, '
                                         'prior neck radiation with fibrosis, a high body mass '
                                         'index, and tumors at the anterior commissure or '
                                         'infrahyoid epiglottis all predict difficult exposure.'},
 'v228_hn_tlm_app': {'stem': 'A 61-year-old woman undergoes transoral laser resection of a T2 '
                             'supraglottic SCC extending into the preepiglottic fat. As dissection '
                             'proceeds anteriorly, the deep margin approaches the thyroid '
                             'cartilage, and the surgeon cannot confidently distinguish tumor from '
                             'fibrotic tissue under the microscope. Frozen section is available. '
                             'Which action best reflects sound oncologic practice?',
                     'choices': ['Accept the margin, since laser char sterilizes the remaining bed',
                                 'Vaporize the base deeply and send no separate margin samples',
                                 'Proceed to total laryngectomy now without margin sampling',
                                 'Send oriented deep margins and change plan if clearance fails'],
                     'answer': 3,
                     'explanation': 'Laser resection still demands margin discipline. When the '
                                    'deep margin is uncertain, the surgeon should take oriented, '
                                    'labeled deep margin samples for frozen section, resect '
                                    'further where tumor is found, and change strategy, such as '
                                    'open partial laryngectomy, adjuvant radiation, or another '
                                    'modality, if a safe clear margin cannot be achieved. Thermal '
                                    'char does not sterilize tumor, and vaporization destroys the '
                                    'tissue pathology needs. Specimen mapping makes piecemeal '
                                    'resection meaningful.',
                     'why_wrong': ['Laser char does not reliably kill residual tumor, and '
                                   'accepting an unknown margin risks local recurrence.',
                                   'Vaporizing the base destroys the tissue needed to judge '
                                   'margins and leaves the completeness of resection unknown.',
                                   'Total laryngectomy may be unnecessary if margins clear with '
                                   'directed sampling or further transoral resection.',
                                   'Correct.'],
                     'board_pearl': 'Uncertain deep margin in TLM: send oriented margins and be '
                                    'willing to change strategy.',
                     'curveball': 'How can piecemeal transoral laser specimens still be oriented '
                                  'for meaningful pathology?',
                     'curveball_answer': 'Each piece is pinned on a labeled diagram or corkboard '
                                         'with sutures or ink marking superior, anterior, and deep '
                                         'surfaces, and the surgeon communicates directly with the '
                                         'pathologist. Separate margin biopsies from the wound bed '
                                         'are labeled by site. A drawing of the resection in the '
                                         'operative note guides later surveillance and '
                                         're-resection.'},
 'v228_hn_tlm_snr': {'stem': 'A 55-year-old professional singer has a T1a SCC of the left vocal '
                             'fold that infiltrates into the vocalis muscle on biopsy and '
                             'stroboscopy, with normal mobility. Exposure is excellent. She has '
                             'never smoked. Laser resection would require a transmuscular '
                             'cordectomy, while radiation would treat the whole larynx over about '
                             '5 to 6 weeks. Which factor most favors radiation over transoral '
                             'laser microsurgery for her?',
                     'choices': ['Need for a deep cordectomy in a singer',
                                 'Excellent exposure of the vocal fold on laryngoscopy',
                                 'Normal mobility of the involved vocal fold',
                                 'A desire to keep radiation for a second primary'],
                     'answer': 0,
                     'explanation': 'Laser microsurgery and radiation give similar control for '
                                    'early glottic cancer, so the choice is individualized by '
                                    'exposure, extent, expected function, salvage options, and the '
                                    "patient's priorities. Voice after laser surgery depends on "
                                    'depth: subepithelial or subligamental cordectomy preserves '
                                    'voice well, but transmuscular resection leaves a scarred, '
                                    'deficient fold. For a professional voice user needing a deep '
                                    'resection, radiation usually preserves a better voice. '
                                    'Excellent exposure and normal mobility favor laser surgery.',
                     'why_wrong': ['Correct.',
                                   'Excellent exposure makes laser resection feasible and is a '
                                   'factor in favor of surgery rather than radiation.',
                                   'Normal mobility indicates early disease amenable to either '
                                   'treatment and does not favor radiation.',
                                   'Preserving radiation for future cancers is an argument for '
                                   'laser surgery, not against it.'],
                     'board_pearl': 'Early glottic cancer: deep resection in a voice professional '
                                    'favors radiation; superficial disease or a smoker favors '
                                    'laser.',
                     'curveball': 'How would a history of prior neck radiation for another cancer '
                                  'alter this choice?',
                     'curveball_answer': 'Prior radiation to the larynx usually makes repeat '
                                         'radiation unsafe, so transoral laser resection becomes '
                                         'the preferred option if exposure and margins are '
                                         'achievable, with open partial laryngectomy as the '
                                         'alternative. Healing after laser surgery in irradiated '
                                         'tissue is slower, and chondronecrosis risk is higher.'},
 'v138_hn_28': {'stem': 'A 64-year-old man with metastatic oropharyngeal SCC to the lungs received '
                        'pembrolizumab for 2 years and had a complete response. Therapy was '
                        'stopped as planned 14 months ago, and imaging remains clear without any '
                        'further treatment. He asks his oncologist why the cancer has not returned '
                        'even though the drug is no longer in his body. Which mechanism best '
                        'explains his durable response?',
                'choices': ['Persistent drug-induced DNA damage in residual tumor cells',
                            'Reactivated tumor-specific T cells with immunologic memory',
                            'Ongoing antibody-dependent killing of EGFR-expressing cells',
                            'Antiangiogenic starvation of residual tumor deposits'],
                'answer': 1,
                'explanation': 'Tumors evade immunity by expressing PD-L1, which engages PD-1 on '
                               'activated T cells and switches them off. Pembrolizumab blocks PD-1 '
                               'and releases this brake, allowing tumor-specific cytotoxic T cells '
                               'to recognize and kill cancer cells. Because the response is '
                               'mediated by the adaptive immune system, it can generate memory T '
                               'cells that continue surveillance after the drug is stopped, '
                               'explaining durable responses in a minority of patients. '
                               'HPV-associated tumors, which carry viral antigens, are often more '
                               'inflamed.',
                'why_wrong': ['Pembrolizumab is not cytotoxic and causes no DNA damage; that '
                              'mechanism describes platinum agents and radiation.',
                              'Correct.',
                              'EGFR-directed antibody-dependent cytotoxicity is a mechanism of '
                              'cetuximab, not of an anti-PD-1 antibody.',
                              'Inhibiting blood vessel growth is the mechanism of antiangiogenic '
                              'agents, which are not standard in head and neck cancer.'],
                'board_pearl': 'Checkpoint blockade releases the PD-1 brake on T cells; immune '
                               'memory explains durable responses.',
                'curveball': 'Which clinical findings during checkpoint therapy should raise '
                             'suspicion for immune-mediated pneumonitis?',
                'curveball_answer': 'New or worsening cough, exertional dyspnea, or hypoxia, with '
                                    'new ground-glass or organizing opacities on CT, suggest '
                                    'pneumonitis. Infection and tumor progression must be '
                                    'excluded, often with bronchoscopy. Therapy is held, and grade '
                                    '2 or higher disease is treated with corticosteroids, with '
                                    'permanent discontinuation for severe cases.'},
 'v145_hn_23': {'stem': 'A 59-year-old woman is receiving pembrolizumab for recurrent oral cavity '
                        'SCC, and her latest scan shows a partial response. Over 5 days she has '
                        'had 8 watery stools a day above her baseline, with abdominal cramping and '
                        'nocturnal stools. She is afebrile and tolerating fluids. Stool studies '
                        'for Clostridioides difficile are pending, and CT shows diffuse colonic '
                        'wall thickening. What is the most appropriate management?',
                'choices': ['Continue pembrolizumab with loperamide as needed',
                            'Hold pembrolizumab and start systemic corticosteroids',
                            'Start empiric antibiotics alone for presumed infection',
                            'Reduce the pembrolizumab dose by half and continue'],
                'answer': 1,
                'explanation': 'Checkpoint inhibitors activate T cells that can attack normal '
                               'tissue in almost any organ. Seven or more stools a day above '
                               'baseline with colitis on CT is grade 3 immune-related colitis. '
                               'Management is to hold the drug, exclude infection, and start '
                               'systemic corticosteroids at about 1 to 2 mg/kg of prednisone or '
                               'equivalent, with gastroenterology involvement. Infliximab or '
                               'vedolizumab is added if symptoms do not improve within a few days. '
                               'Tumor response does not justify ignoring toxicity.',
                'why_wrong': ['Antidiarrheals alone can mask worsening colitis and delay steroids, '
                              'risking perforation in grade 3 immune-related disease.',
                              'Correct.',
                              'Infection should be excluded, but antibiotics alone do not treat '
                              'immune-mediated colitis, which needs corticosteroids.',
                              'Checkpoint inhibitors are not dose-reduced for toxicity; they are '
                              'held or stopped and the reaction is treated.'],
                'board_pearl': 'Grade 3 immune colitis: hold the checkpoint inhibitor, exclude '
                               'infection, start steroids; add infliximab if refractory.',
                'curveball': 'Which airway or swallowing symptoms during checkpoint therapy would '
                             'require urgent ENT evaluation in this patient?',
                'curveball_answer': 'New stridor, hoarseness, or dysphagia may reflect tumor flare '
                                    'or inflammation, immune-related laryngeal edema or '
                                    'vasculitis, or rarely myositis affecting swallowing. A '
                                    'rapidly enlarging neck mass with airway compromise also needs '
                                    'urgent assessment. Flexible laryngoscopy defines the airway, '
                                    'and securing it takes priority before tissue diagnosis.'},
 'v225_hn_imm_fnd': {'stem': 'A 61-year-old man completed high-dose cisplatin and radiation for a '
                             'p16-negative laryngeal SCC 2 months ago. PET-CT now shows new liver '
                             'and bone metastases, confirmed by biopsy. ECOG performance status is '
                             '1, and he has not received immunotherapy. His disease is considered '
                             'platinum-refractory. Which drug class has shown a survival benefit '
                             'in this setting?',
                     'choices': ['EGFR-blocking monoclonal antibody',
                                 'Taxane microtubule stabilizer',
                                 'Antifolate antimetabolite',
                                 'Anti-PD-1 monoclonal antibody'],
                     'answer': 3,
                     'explanation': 'PD-1 checkpoint inhibitors restore antitumor T-cell activity '
                                    'and have become central to recurrent and metastatic HNSCC. '
                                    'Disease that progresses within 6 months of platinum is '
                                    'considered platinum-refractory. In this setting, nivolumab in '
                                    'CheckMate 141 and pembrolizumab in KEYNOTE-040 improved '
                                    "overall survival over investigator's choice of methotrexate, "
                                    'docetaxel, or cetuximab. Responses are less frequent than '
                                    'with first-line regimens but can be durable, and toxicity is '
                                    'generally lower than with cytotoxic therapy.',
                     'why_wrong': ['Cetuximab was part of the comparator arm in the '
                                   'platinum-refractory trials and did not show the survival '
                                   'benefit of PD-1 inhibition.',
                                   'Docetaxel was a comparator in these trials and was inferior to '
                                   'anti-PD-1 therapy for overall survival.',
                                   'Methotrexate has modest activity and no survival advantage; it '
                                   'was a comparator in the immunotherapy trials.',
                                   'Correct.'],
                     'board_pearl': 'Platinum-refractory recurrent or metastatic HNSCC: nivolumab '
                                    'or pembrolizumab improves survival over chemotherapy or '
                                    'cetuximab.',
                     'curveball': 'Why can immune-related adverse events involve organs far '
                                  'outside the head and neck?',
                     'curveball_answer': 'PD-1 and PD-L1 maintain peripheral tolerance throughout '
                                         'the body, not just in the tumor. Blocking them can '
                                         'unleash T cells against self-antigens in any organ, '
                                         'causing thyroiditis, colitis, pneumonitis, hepatitis, '
                                         'hypophysitis, dermatitis, myocarditis, and others, '
                                         'sometimes months after starting or even after stopping '
                                         'treatment.'},
 'v225_hn_imm_app': {'stem': 'A 66-year-old man has been receiving pembrolizumab for metastatic '
                             'hypopharyngeal SCC for 10 weeks. Routine labs show AST 320 U/L and '
                             'ALT 410 U/L, about eight times the upper limit of normal, with '
                             'normal bilirubin. He has mild fatigue. Viral hepatitis serologies '
                             'are negative, he takes no new medications, and ultrasound shows no '
                             'liver metastases or biliary obstruction. What is the most '
                             'appropriate management?',
                     'choices': ['Continue pembrolizumab and recheck labs in 4 weeks',
                                 'Hold pembrolizumab and start prednisone at 1 to 2 mg/kg',
                                 'Start infliximab as first-line immunosuppression',
                                 'Halve the pembrolizumab dose and continue therapy'],
                     'answer': 1,
                     'explanation': 'Checkpoint inhibitors can cause immune-mediated hepatitis, '
                                    'usually within the first few months. Transaminases between 5 '
                                    'and 20 times the upper limit of normal define grade 3 '
                                    'toxicity once other causes are excluded, as here. Management '
                                    'is to hold the drug, start corticosteroids at about 1 to 2 '
                                    'mg/kg of prednisone or equivalent, monitor liver tests '
                                    'closely, and involve hepatology. If transaminases do not '
                                    'improve, mycophenolate is added; infliximab is avoided '
                                    'because it is itself hepatotoxic.',
                     'why_wrong': ['Grade 3 hepatitis requires holding therapy and starting '
                                   'steroids; waiting 4 weeks risks liver failure.',
                                   'Correct.',
                                   'Infliximab is avoided in immune hepatitis because of its own '
                                   'hepatotoxicity; mycophenolate is the second-line agent.',
                                   'Checkpoint inhibitors are not dose-reduced for toxicity; the '
                                   'drug is held or stopped and the reaction treated.'],
                     'board_pearl': 'Immune hepatitis grade 3: hold the drug and give steroids; '
                                    'use mycophenolate, not infliximab, if refractory.',
                     'curveball': 'Which endocrine immune-related toxicities may require lifelong '
                                  'hormone replacement even after immunotherapy is stopped?',
                     'curveball_answer': 'Hypothyroidism after thyroiditis, primary adrenal '
                                         'insufficiency, hypophysitis with secondary adrenal '
                                         'insufficiency or other pituitary deficits, and '
                                         'insulin-dependent diabetes from beta-cell destruction '
                                         'are usually permanent. They are treated with hormone '
                                         'replacement rather than prolonged steroids, and '
                                         'immunotherapy can often continue once replacement is '
                                         'stable.'},
 'v225_hn_imm_snr': {'stem': 'A 57-year-old woman with metastatic oropharyngeal SCC started '
                             'pembrolizumab 9 weeks ago. Restaging CT shows the lung nodules have '
                             'grown by about 15 percent and one new 8-mm mediastinal node has '
                             'appeared. Meanwhile her neck pain has resolved, she has regained '
                             'weight, and ECOG performance status improved from 2 to 1. There is '
                             'no airway or spinal cord compromise. What is the most appropriate '
                             'next step?',
                     'choices': ['Stop pembrolizumab and start platinum chemotherapy now',
                                 'Add ipilimumab to the current pembrolizumab regimen',
                                 'Continue pembrolizumab and repeat imaging in 4 to 8 weeks',
                                 'Transition to hospice given progression on immunotherapy'],
                     'answer': 2,
                     'explanation': 'Checkpoint inhibitors can produce atypical response kinetics. '
                                    'Immune infiltration can enlarge lesions or reveal new ones '
                                    'before shrinkage, called pseudoprogression, although true '
                                    'progression is far more common in HNSCC. When imaging shows '
                                    'modest growth but the patient is clinically improving and no '
                                    'critical organ is threatened, immune-modified response '
                                    'criteria support continuing therapy and confirming '
                                    'progression on repeat imaging. Rapid symptomatic progression '
                                    'or a threatened airway or spinal cord would warrant an early '
                                    'switch.',
                     'why_wrong': ['Switching immediately may abandon an effective therapy in a '
                                   'patient who is clinically improving and has low-volume growth.',
                                   'Adding ipilimumab to PD-1 blockade did not improve survival in '
                                   'HNSCC trials and adds substantial toxicity.',
                                   'Correct.',
                                   'Her symptoms and performance status are improving, so hospice '
                                   'is premature and inconsistent with her course.'],
                     'board_pearl': 'Modest growth with clinical improvement on immunotherapy: '
                                    'continue and confirm with repeat imaging.',
                     'curveball': 'Which sites of apparent progression would make waiting for '
                                  'confirmatory imaging unsafe?',
                     'curveball_answer': 'Growth threatening the airway, the spinal cord or '
                                         'vertebral stability, a major vessel such as the carotid '
                                         'with bleeding risk, the brain, or causing organ '
                                         'dysfunction such as biliary obstruction or symptomatic '
                                         'effusion cannot wait. Those require prompt local '
                                         'treatment and usually a change in systemic therapy.'},
 'v231_hn_cbs_fnd': {'stem': 'A 62-year-old man had chemoradiation for a hypopharyngeal SCC 2 '
                             'years ago and salvage neck dissection 4 weeks ago. The neck wound '
                             'has partly dehisced, with pale, dry tissue at its base near the '
                             'carotid pulse. On the ward he coughs up about 100 mL of bright red '
                             'blood that stops on its own within a minute. Vital signs are now '
                             'normal. What is the most likely explanation?',
                     'choices': ['Granulation tissue oozing in the open neck wound',
                                 'Posterior epistaxis from irradiated nasal mucosa',
                                 'Sentinel hemorrhage from a threatened carotid',
                                 'Capillary bleeding from radiation mucositis'],
                     'answer': 2,
                     'explanation': 'Carotid blowout syndrome ranges from a threatened, exposed '
                                    'artery to a sentinel bleed to active rupture. A brisk, '
                                    'self-limited bleed in a neck that has been irradiated and '
                                    'operated on, with wound breakdown near the carotid, should be '
                                    'treated as a sentinel hemorrhage until proven otherwise, '
                                    'because it often precedes fatal rupture. Management is '
                                    'urgent: monitored bed, large-bore access, type and '
                                    'crossmatch, airway readiness, and prompt CT angiography or '
                                    'catheter angiography with interventional radiology planning.',
                     'why_wrong': ['Granulation tissue oozes slowly and would not produce a 100 mL '
                                   'burst of bright red blood that stops abruptly.',
                                   'Epistaxis is possible after radiation, but dehiscence near the '
                                   'carotid makes a sentinel carotid bleed the dangerous and '
                                   'likelier diagnosis.',
                                   'Correct.',
                                   'Mucositis bleeding is low-volume and occurs during or soon '
                                   'after radiation, not 2 years later as a sudden brisk bleed.'],
                     'board_pearl': 'Brisk self-limited bleed after neck radiation and surgery is '
                                    'a sentinel carotid bleed until proven otherwise.',
                     'curveball': 'Which prior treatments and wound findings most increase this '
                                  "patient's risk of carotid blowout?",
                     'curveball_answer': 'Prior radiation, especially re-irradiation or high '
                                         'cumulative dose, radical neck dissection removing '
                                         'protective tissue, pharyngocutaneous fistula bathing the '
                                         'artery in saliva, wound dehiscence or infection exposing '
                                         'the carotid, flap loss, recurrent tumor encasing the '
                                         'vessel, and malnutrition all increase risk. Exposed '
                                         'carotid should be covered promptly with vascularized '
                                         'tissue.'},
 'v231_hn_cbs_app': {'stem': 'A 66-year-old man with recurrent oropharyngeal SCC after '
                             're-irradiation suddenly has massive bleeding from the mouth and his '
                             'tracheostomy, with blood pooling in his lap. Blood pressure is 78/40 '
                             'mm Hg and heart rate 132. He has a cuffless tracheostomy tube, and '
                             'an interventional radiology suite is available. He has previously '
                             'stated he wants full treatment. What is the immediate management '
                             'priority?',
                     'choices': ['Obtain CT angiography first to localize the source',
                                 'Give tranexamic acid and observe in intensive care',
                                 'Intubate orally and wait for the bleeding to slow',
                                 'Pack, place a cuffed tube, transfuse, then rapid IR'],
                     'answer': 3,
                     'explanation': 'Active carotid blowout is a simultaneous airway, '
                                    'resuscitation, and vascular control emergency. Steps happen '
                                    'in parallel: direct pressure or transoral packing, replacing '
                                    'the cuffless tube with a cuffed tube and inflating it to '
                                    'protect the lower airway, large-bore access, activation of '
                                    'massive transfusion, and immediate transfer to interventional '
                                    'radiology for embolization or a covered stent, or to the '
                                    'operating room for ligation. Diagnostic imaging must not '
                                    'delay control in an unstable patient.',
                     'why_wrong': ['CT angiography delays definitive control in an unstable '
                                   'patient; catheter angiography both diagnoses and treats the '
                                   'bleeding.',
                                   'Tranexamic acid alone cannot control arterial rupture, and '
                                   'observation risks exsanguination or aspiration.',
                                   'He already has a stoma, and oral intubation through blood is '
                                   'difficult; airway protection should use a cuffed tube via '
                                   'tracheostomy.',
                                   'Correct.'],
                     'board_pearl': 'Active carotid blowout: compress or pack, protect the airway '
                                    'with a cuffed tube, transfuse, and get emergent vascular '
                                    'control.',
                     'curveball': 'How does an endovascular covered stent differ from vessel '
                                  'sacrifice in rebleeding, stroke, infection, and antiplatelet '
                                  'considerations?',
                     'curveball_answer': 'Sacrifice by coil or balloon occlusion is durable and '
                                         'needs no antiplatelet therapy, but risks stroke if '
                                         'collateral flow is inadequate. A covered stent preserves '
                                         'flow and lowers immediate stroke risk but needs dual '
                                         'antiplatelet therapy, can thrombose or become infected '
                                         'in a contaminated field, and has higher rebleeding '
                                         'rates, so it is often a bridge.'},
 'v231_hn_cbs_snr': {'stem': 'A 59-year-old woman with a pharyngocutaneous fistula after salvage '
                             'laryngectomy had a sentinel bleed and is now stable. Angiography '
                             'shows a 6-mm pseudoaneurysm of the right internal carotid artery '
                             'adjacent to the infected, irradiated wound. Balloon test occlusion '
                             'causes left arm weakness within 5 minutes. The interventional team '
                             'asks the head and neck surgeon to help choose treatment. Which '
                             'approach is most appropriate?',
                     'choices': ['Coil occlusion of the internal carotid artery',
                                 'Covered stent, antibiotics, and flap coverage',
                                 'Surgical ligation of the common carotid artery',
                                 'Anticoagulation and observation in intensive care'],
                     'answer': 1,
                     'explanation': 'A failed balloon test occlusion predicts stroke if the '
                                    'carotid is sacrificed, whether by coils or ligation. '
                                    'Reconstructive endovascular treatment with a covered stent '
                                    'excludes the pseudoaneurysm while preserving flow. Because '
                                    'the field is infected and irradiated, the stent is vulnerable '
                                    'to infection, thrombosis, and rebleeding, so it should be '
                                    'paired with antibiotics, dual antiplatelet therapy, '
                                    'debridement, and vascularized tissue coverage of the wound, '
                                    'often a pectoralis flap. Multidisciplinary planning balances '
                                    'stroke and durability.',
                     'why_wrong': ['Permanent occlusion after a failed balloon test is likely to '
                                   'cause a stroke from inadequate collateral flow.',
                                   'Correct.',
                                   'Common carotid ligation carries the same high stroke risk as '
                                   'endovascular sacrifice and requires surgery in an infected '
                                   'field.',
                                   'Anticoagulation increases bleeding risk from a pseudoaneurysm '
                                   'and does nothing to exclude it.'],
                     'board_pearl': 'Failed balloon test occlusion: covered stent rather than '
                                    'sacrifice, plus infection control and vascularized coverage.',
                     'curveball': 'When is a technically successful covered stent still a poor '
                                  'long-term solution in this setting?',
                     'curveball_answer': 'A stent in a persistently infected or '
                                         'salivary-contaminated wound, or one eroded by recurrent '
                                         'tumor, has high rates of infection, thrombosis, and '
                                         'rebleeding. If the wound cannot be closed with '
                                         'vascularized tissue or tumor persists, the stent may '
                                         'only bridge to definitive management, such as delayed '
                                         'sacrifice after collateral recovery or bypass.'},
 'v425-skull-base-vernet-villaret-01': {'stem': 'A 55-year-old man has 2 months of hoarseness, '
                                                'choking on liquids, and difficulty lifting his '
                                                'right arm above his shoulder. Examination shows '
                                                'right vocal fold paralysis, an absent right gag, '
                                                'weak right trapezius, and tongue deviation to the '
                                                'right. He also has a 2-mm right ptosis and a '
                                                'smaller right pupil. MRI shows a 3-cm right '
                                                'poststyloid mass. What does the ptosis and miosis '
                                                'add to the localization?',
                                        'choices': ['Oculomotor involvement from cavernous sinus '
                                                    'extension',
                                                    'Facial nerve involvement at the stylomastoid '
                                                    'foramen',
                                                    'Sympathetic chain injury in the retroparotid '
                                                    'space',
                                                    'Descending sympathetic tract injury in the '
                                                    'medulla'],
                                        'answer': 2,
                                        'explanation': 'Deficits of cranial nerves IX, X, XI, and '
                                                       'XII together form Collet-Sicard syndrome. '
                                                       'The added Horner syndrome, ptosis and '
                                                       'miosis with anhidrosis, means the cervical '
                                                       'sympathetic chain is also involved. The '
                                                       'sympathetic chain runs with the carotid '
                                                       'sheath and lower cranial nerves just below '
                                                       'the skull base in the retroparotid, or '
                                                       'poststyloid parapharyngeal, space, so a '
                                                       'single mass there produces all the '
                                                       'deficits. The combination is Villaret '
                                                       'syndrome, which localizes the lesion '
                                                       'outside the skull base foramina.',
                                        'why_wrong': ['Oculomotor palsy causes a large, poorly '
                                                      'reactive pupil with major ptosis, not the '
                                                      'small pupil and mild ptosis of Horner '
                                                      'syndrome.',
                                                      'Facial nerve injury causes facial weakness, '
                                                      'not ptosis and miosis, and the stylomastoid '
                                                      'foramen is not part of this pattern.',
                                                      'Correct.',
                                                      'A lateral medullary lesion causes Horner '
                                                      'syndrome with crossed sensory loss and '
                                                      'ataxia, and spares cranial nerves XI and '
                                                      'XII.'],
                                        'board_pearl': 'Lower cranial nerves IX to XII plus '
                                                       'Horner: Villaret syndrome, localizing to '
                                                       'the retroparotid space.',
                                        'curveball': 'What must be done before any biopsy of this '
                                                     'poststyloid mass is attempted, and why?',
                                        'curveball_answer': 'Obtain vascular imaging, such as CTA '
                                                            'or MRA and sometimes catheter '
                                                            'angiography, and plasma metanephrines '
                                                            'if a paraganglioma is possible, '
                                                            'before any needle biopsy. A '
                                                            'poststyloid mass causing this pattern '
                                                            'may be a schwannoma or paraganglioma, '
                                                            'and needling a hypervascular lesion '
                                                            'risks significant hemorrhage while '
                                                            'adding little when imaging is already '
                                                            'characteristic.'},
 'v431-villaret-01': {'stem': 'A 61-year-old man treated with surgery for a right tonsil SCC 2 '
                              'years ago now has a firm, fixed mass behind the right angle of the '
                              'mandible. He has hoarseness, nasal regurgitation, a weak right '
                              'shoulder shrug, tongue deviation to the right, and right ptosis '
                              'with miosis and facial anhidrosis. Facial movement and hearing are '
                              'normal. Where is the lesion most likely located?',
                      'choices': ['Jugular foramen at the skull base',
                                  'Hypoglossal canal and occipital condyle',
                                  'Retroparotid poststyloid parapharyngeal space',
                                  'Cavernous sinus on the right side'],
                      'answer': 2,
                      'explanation': 'Combined deficits of cranial nerves IX, X, XI, and XII plus '
                                     'Horner syndrome define Villaret syndrome. The retroparotid '
                                     'space, the poststyloid parapharyngeal compartment just '
                                     'behind the parotid, contains the carotid sheath, the lower '
                                     'cranial nerves after they exit the skull, and the cervical '
                                     'sympathetic chain. A mass there, here likely a recurrent '
                                     'nodal metastasis, can injure all of them. Collet-Sicard '
                                     'syndrome has the same IX to XII pattern without Horner '
                                     'syndrome, localizing to the skull base.',
                      'why_wrong': ['A jugular foramen lesion causes Vernet syndrome, involving '
                                    'IX, X, and XI without the hypoglossal nerve or Horner '
                                    'syndrome.',
                                    'A lesion at the hypoglossal canal and condyle region produces '
                                    'Collet-Sicard syndrome, which lacks the sympathetic deficit '
                                    'seen here.',
                                    'Correct.',
                                    'Cavernous sinus disease affects cranial nerves III, IV, V1, '
                                    'V2, and VI rather than the lower cranial nerves.'],
                      'board_pearl': 'Villaret localizes below the skull base, where lower cranial '
                                     'nerves and sympathetic chain run together behind the '
                                     'parotid.',
                      'curveball': 'If a vascular lesion were suspected instead of a metastasis, '
                                   'what must be done before needle biopsy?',
                      'curveball_answer': 'Characterize vascularity with CTA or MRA, and test '
                                          'plasma metanephrines if paraganglioma is possible, '
                                          'before any needle biopsy, because schwannomas and '
                                          'paragangliomas are common here. If resection is '
                                          'planned, counsel proactively about permanent voice, '
                                          'swallowing, shoulder, and oculosympathetic deficits and '
                                          'plan rehabilitation.'},
 'v460_hn_vill_fnd': {'stem': 'A 38-year-old woman is evaluated 1 week after a motor vehicle '
                              'collision with a seat-belt injury to the left neck. She has '
                              'hoarseness, dysphagia with aspiration, left shoulder droop, and '
                              'tongue deviation to the left. Examination also shows left ptosis, a '
                              'smaller left pupil, and decreased sweating on the left forehead. CT '
                              'angiography shows a dissection of the left cervical internal '
                              'carotid artery below the skull base. Which syndrome does she have?',
                      'choices': ['Vernet syndrome',
                                  'Collet-Sicard syndrome',
                                  'Villaret syndrome',
                                  'Wallenberg syndrome'],
                      'answer': 2,
                      'explanation': 'Villaret syndrome is ipsilateral palsy of cranial nerves IX, '
                                     'X, XI, and XII plus Horner syndrome from a lesion in the '
                                     'retroparotid space. Here an extracranial internal carotid '
                                     'dissection, with an expanding wall hematoma, compresses the '
                                     'lower cranial nerves and the sympathetic fibers that travel '
                                     'with the carotid. Collet-Sicard syndrome has the same IX to '
                                     'XII deficits without Horner syndrome, and Vernet syndrome '
                                     'involves only IX to XI at the jugular foramen.',
                      'why_wrong': ['Vernet syndrome affects only nerves IX, X, and XI at the '
                                    'jugular foramen, sparing the hypoglossal nerve and '
                                    'sympathetic chain.',
                                    'Collet-Sicard syndrome involves IX through XII but lacks '
                                    'Horner syndrome, which is present in this patient.',
                                    'Correct.',
                                    'Wallenberg syndrome is a lateral medullary stroke with '
                                    'crossed sensory loss and ataxia, sparing nerves XI and XII.'],
                      'board_pearl': 'Vernet: IX to XI. Collet-Sicard: IX to XII. Villaret: IX to '
                                     'XII plus Horner.',
                      'curveball': 'Anatomically, what does the retroparotid space contain that '
                                   'lets a single lesion produce all of these deficits?',
                      'curveball_answer': 'The retroparotid, or poststyloid parapharyngeal, space '
                                          'contains the internal carotid artery, internal jugular '
                                          'vein, cranial nerves IX, X, XI, and XII just after they '
                                          'exit the skull base, and the cervical sympathetic '
                                          'chain, all packed together behind the parotid gland. A '
                                          'mass, dissection, or infection there can compress all '
                                          'of them at once.'},
 'v460_hn_vill_app': {'stem': 'A 64-year-old man with a poststyloid parapharyngeal mass initially '
                              'had hoarseness, dysphagia, a weak left shoulder shrug, and tongue '
                              'deviation to the left, which his neurologist called Collet-Sicard '
                              'syndrome. At follow-up 6 weeks later, the mass has grown on MRI, '
                              'and his examination has changed. Which new finding would most '
                              'change the localization and the name of his syndrome?',
                      'choices': ['Worsening deviation of the tongue toward the left',
                                  'Left ptosis, miosis, and facial anhidrosis',
                                  'Pooling of secretions in the left piriform sinus',
                                  'Further atrophy of the left trapezius muscle'],
                      'answer': 1,
                      'explanation': 'Collet-Sicard syndrome is palsy of cranial nerves IX through '
                                     'XII, which can arise at the skull base. The appearance of '
                                     'Horner syndrome, ptosis, miosis, and anhidrosis, shows that '
                                     'the cervical sympathetic chain is now involved. Because the '
                                     'sympathetic chain joins the lower cranial nerves only below '
                                     'the skull base in the retroparotid space, the lesion '
                                     'localizes there, and the syndrome becomes Villaret syndrome. '
                                     'Worsening of the existing nerve deficits does not change '
                                     'localization.',
                      'why_wrong': ['Worsening tongue deviation reflects progression of the '
                                    'hypoglossal palsy already present and does not change the '
                                    'localization.',
                                    'Correct.',
                                    'Piriform pooling reflects worsening vagal dysfunction already '
                                    'present in Collet-Sicard syndrome and adds no new localizing '
                                    'information.',
                                    'Trapezius atrophy reflects longstanding accessory nerve '
                                    'palsy, which is already part of his existing syndrome.'],
                      'board_pearl': 'Horner syndrome turns Collet-Sicard into Villaret and moves '
                                     'localization to the retroparotid space.',
                      'curveball': 'How does Vernet syndrome differ from both Collet-Sicard and '
                                   'Villaret syndromes?',
                      'curveball_answer': 'Vernet syndrome involves only cranial nerves IX, X, and '
                                          'XI, as they pass through the jugular foramen, without '
                                          'hypoglossal palsy or Horner syndrome. It is the most '
                                          'limited of the three. Adding XII suggests involvement '
                                          'below the foramen or of the hypoglossal canal, and '
                                          'adding Horner places the lesion in the retroparotid '
                                          'space.'},
 'v460_hn_vill_snr': {'stem': 'A 49-year-old woman has 5 months of hoarseness, dysphagia, left '
                              'shoulder weakness, tongue deviation to the left, and left ptosis '
                              'with miosis. MRI shows a 4-cm left poststyloid parapharyngeal mass '
                              'that enhances intensely and displaces the internal carotid artery '
                              'anteriorly. Plasma metanephrines are pending. The referring '
                              'physician has scheduled a transoral fine-needle aspiration through '
                              'the bulging pharyngeal wall. What is the most appropriate next '
                              'step?',
                      'choices': ['Proceed with transoral aspiration as scheduled',
                                  'Open incisional biopsy through a neck incision',
                                  'Vascular imaging such as CTA or MRA first',
                                  'Empiric radiation based on the MRI findings'],
                      'answer': 2,
                      'explanation': 'A poststyloid mass causing Villaret syndrome is most often a '
                                     'schwannoma, a paraganglioma, or a metastatic node. Intense '
                                     'enhancement raises concern for a paraganglioma, and needling '
                                     'a hypervascular lesion, especially transorally, risks major '
                                     'hemorrhage while adding little when imaging is '
                                     'characteristic. Vascularity should be defined with CTA or '
                                     'MRA, and sometimes catheter angiography, along with '
                                     'metanephrines, before any biopsy. Management then follows '
                                     'the same logic as other parapharyngeal tumors: observation, '
                                     'radiation, or resection.',
                      'why_wrong': ['Transoral needling of a possibly hypervascular poststyloid '
                                    'mass risks significant bleeding and is not the first step.',
                                    'Open biopsy of a possible paraganglioma risks hemorrhage and '
                                    'tumor spillage and is rarely needed if imaging is '
                                    'characteristic.',
                                    'Correct.',
                                    'Radiation may later be chosen for paraganglioma, but treating '
                                    'before characterizing the lesion risks mismanaging a '
                                    'different diagnosis.'],
                      'board_pearl': 'Characterize vascularity before needling any poststyloid '
                                     'mass that could be a paraganglioma.',
                      'curveball': 'If resection is chosen, what should be planned and counseled '
                                   'given her multiple nerve deficits?',
                      'curveball_answer': 'Resection may make existing deficits permanent and add '
                                          'new ones. Counseling covers voice, swallowing, shoulder '
                                          'function, and Horner syndrome, and planning includes '
                                          'swallow evaluation, early vocal fold medialization, '
                                          'temporary feeding access, and physical therapy for the '
                                          'shoulder. Because she already has deficits, '
                                          'compensation may already be under way, which lessens '
                                          'the functional impact.'},
 'v431-slnb-oral-cavity-01': {'stem': 'A 57-year-old man has a 1.8-cm SCC of the right lateral '
                                      'tongue with 5-mm depth of invasion on biopsy. Examination, '
                                      'CT, and neck ultrasound show no suspicious nodes. He works '
                                      'as a singer and prefers to avoid unnecessary neck surgery. '
                                      'The center has a validated lymphatic mapping program with '
                                      'SPECT-CT and step-sectioning pathology. Which neck staging '
                                      'approach is most appropriate along with resection of the '
                                      'primary?',
                              'choices': ['Sentinel lymph node biopsy',
                                          'Ultrasound surveillance of the neck alone',
                                          'Modified radical neck dissection',
                                          'PET-CT surveillance in place of neck surgery'],
                              'answer': 0,
                              'explanation': 'With depth of invasion over about 4 mm, occult nodal '
                                             'risk is high enough that the neck needs elective '
                                             'staging or treatment rather than observation. For a '
                                             'cT1 to cT2 clinically node-negative oral cavity SCC '
                                             'in a validated program, sentinel lymph node biopsy '
                                             'is an accepted alternative to elective neck '
                                             'dissection, with comparable survival in trials and '
                                             'less shoulder dysfunction and morbidity. It is a '
                                             'staging tool and is not used for a clinically '
                                             'node-positive neck.',
                              'why_wrong': ['Correct.',
                                            'Observation is inappropriate with 5-mm depth of '
                                            'invasion, where elective neck management improves '
                                            'survival.',
                                            'Comprehensive dissection is a therapeutic operation '
                                            'for node-positive necks and adds unnecessary '
                                            'morbidity for a node-negative neck.',
                                            'PET-CT cannot detect micrometastases and does not '
                                            'replace pathologic staging of the clinically negative '
                                            'neck.'],
                              'board_pearl': 'Sentinel node biopsy suits cT1 to cT2 N0 oral cavity '
                                             'SCC in experienced centers; not for node-positive '
                                             'necks.',
                              'curveball': 'What technical factor complicates sentinel node '
                                           'localization specifically for floor-of-mouth '
                                           'primaries?',
                              'curveball_answer': 'Shine-through: radiotracer injected around a '
                                                  'floor-of-mouth primary creates intense activity '
                                                  'close to the submental and submandibular nodes, '
                                                  'which can obscure true sentinel nodes in level '
                                                  'I. SPECT-CT, careful probe technique, and '
                                                  'removing the primary before probing level I '
                                                  'help, but sensitivity is lower than for lateral '
                                                  'tongue tumors.'},
 'v431-slnb-oral-cavity-02': {'stem': 'A 54-year-old woman underwent partial glossectomy and '
                                      'sentinel lymph node biopsy for a cT1N0 SCC of the left '
                                      'lateral tongue at a high-volume center. SPECT-CT identified '
                                      'two sentinel nodes in left level II, both removed with low '
                                      'residual counts in the bed. Step-sectioning with '
                                      'cytokeratin immunohistochemistry shows no tumor. Primary '
                                      'margins are clear. What is the most appropriate management '
                                      'of the neck?',
                              'choices': ['Completion selective neck dissection of levels I to IV',
                                          'Elective radiation to the ipsilateral neck',
                                          'Surveillance with examination and neck ultrasound',
                                          'Contralateral sentinel node biopsy'],
                              'answer': 2,
                              'explanation': 'A negative, technically adequate sentinel node '
                                             'biopsy, with good mapping, removal of all hot nodes, '
                                             'and step-sectioning with immunohistochemistry, has a '
                                             'high negative predictive value. It permits '
                                             'surveillance with regular examination and ultrasound '
                                             'rather than further neck treatment, sparing '
                                             'morbidity. Elective neck dissection remains a valid '
                                             'alternative when mapping expertise, pathology '
                                             'support, or reliable follow-up is unavailable, but '
                                             'once a negative biopsy is achieved, completion '
                                             'surgery or radiation adds morbidity without benefit.',
                              'why_wrong': ['Completion dissection after a negative sentinel '
                                            'biopsy adds morbidity and defeats the purpose of the '
                                            'staging procedure.',
                                            'Elective neck radiation is unnecessary after a '
                                            'negative adequate biopsy and carries lasting '
                                            'toxicity.',
                                            'Correct.',
                                            'Mapping showed ipsilateral drainage only, and a '
                                            'well-lateralized tongue tumor does not require '
                                            'contralateral staging.'],
                              'board_pearl': 'Negative, technically adequate sentinel node biopsy: '
                                             'observe the neck with close surveillance.',
                              'curveball': 'Had one of the sentinel nodes contained metastatic '
                                           'carcinoma, how would the neck usually be managed?',
                              'curveball_answer': 'A sentinel node containing metastasis, '
                                                  'including micrometastasis, is generally '
                                                  'followed by completion neck dissection of the '
                                                  'involved basin, or radiation in selected '
                                                  'patients, and the overall pathology then guides '
                                                  'adjuvant therapy. Management of isolated tumor '
                                                  'cells is debated, and some protocols observe '
                                                  'them.'},
 'v460_hn_slnb_fnd': {'stem': 'A 63-year-old man has a biopsy-proven 1.5-cm SCC of the left '
                              'lateral tongue with 4-mm depth of invasion. Examination and '
                              'ultrasound show no enlarged neck nodes. His surgeon recommends '
                              'partial glossectomy plus sentinel lymph node biopsy. The patient '
                              'asks whether the sentinel node procedure will remove his cancer. '
                              'What is the purpose of the sentinel node procedure in his '
                              'treatment?',
                      'choices': ['Treating the primary tongue tumor',
                                  'Staging the clinically negative neck',
                                  'Deciding whether the primary needs re-excision',
                                  'Clearing known nodal metastases'],
                      'answer': 1,
                      'explanation': 'Sentinel lymph node biopsy is a staging procedure. '
                                     'Peritumoral radiotracer identifies the first-echelon nodes '
                                     'draining the tumor, which are removed and examined '
                                     'intensively with step-sectioning and immunohistochemistry. '
                                     'Because metastases spread stepwise, a negative sentinel node '
                                     'predicts a negative neck, allowing observation, while a '
                                     'positive node leads to neck treatment. The primary tumor is '
                                     'treated separately by resection with clear margins, and the '
                                     'procedure is not used for a clinically positive neck.',
                      'why_wrong': ['The primary tumor is treated by partial glossectomy; the '
                                    'sentinel node procedure does not address it.',
                                    'Correct.',
                                    'Primary margin status is assessed on the resection specimen '
                                    'and frozen sections, not by sampling neck nodes.',
                                    'Known nodal metastases require therapeutic neck dissection; '
                                    'sentinel biopsy applies only to clinically node-negative '
                                    'necks.'],
                      'board_pearl': 'Sentinel node biopsy is staging, not treatment; it applies '
                                     'to the clinically node-negative neck.',
                      'curveball': 'Which technique localizes the first-echelon nodes '
                                   'intraoperatively, and what pitfall complicates floor-of-mouth '
                                   'primaries?',
                      'curveball_answer': 'Technetium-99m tracer is injected around the primary, '
                                          'lymphoscintigraphy with SPECT-CT maps drainage, and an '
                                          'intraoperative gamma probe guides excision of hot nodes '
                                          'until bed counts fall. In floor-of-mouth tumors, '
                                          'shine-through from the nearby injection site can hide '
                                          'level I sentinel nodes, lowering accuracy.'},
 'v460_hn_slnb_app': {'stem': 'A 60-year-old man with a cT2N0 SCC of the right lateral tongue '
                              'undergoes attempted sentinel node mapping at a community hospital. '
                              'Lymphoscintigraphy shows faint, delayed drainage, and the gamma '
                              'probe finds no node clearly above background in the neck. The '
                              'pathology department cannot perform step-sectioning or '
                              'immunohistochemistry on short notice. The primary has been resected '
                              'with clear frozen margins. What is the most appropriate next step '
                              'for the neck?',
                      'choices': ['Excise any nodes found and call the biopsy complete',
                                  'Observe the neck with ultrasound surveillance',
                                  'Repeat lymphoscintigraphy next week before deciding',
                                  'Perform elective selective neck dissection'],
                      'answer': 3,
                      'explanation': 'The safety of sentinel node biopsy depends on patient '
                                     'selection, mapping quality, pathology processing, and team '
                                     'experience. Here the mapping failed and pathology cannot '
                                     'reliably detect small deposits, so a negative result would '
                                     'not be trustworthy. A cT2 tongue tumor carries substantial '
                                     'occult nodal risk, so the neck still needs staging and '
                                     'treatment. Elective selective neck dissection is the '
                                     'established alternative and is preferred when mapping or '
                                     'pathology support is inadequate.',
                      'why_wrong': ['Removing random nodes without confirmed sentinel status and '
                                    'adequate pathology gives a falsely reassuring result.',
                                    'Observation leaves a cT2 tongue cancer with substantial '
                                    'occult nodal risk unstaged and untreated.',
                                    'Delaying to repeat mapping after the primary has been '
                                    'resected disrupts lymphatics and postpones definitive neck '
                                    'staging.',
                                    'Correct.'],
                      'board_pearl': 'Failed mapping or inadequate pathology support: do elective '
                                     'neck dissection rather than trust the sentinel node.',
                      'curveball': 'If elective neck dissection is chosen and final pathology '
                                   'shows nodal metastases, how are those findings acted on '
                                   'compared with a positive sentinel node?',
                      'curveball_answer': 'The logic is the same: nodal number, size, and '
                                          'extranodal extension guide adjuvant decisions. '
                                          'Postoperative radiation is indicated for multiple nodes '
                                          'or other adverse features, with concurrent cisplatin '
                                          'for extranodal extension. The difference is that a '
                                          'completed dissection is already therapeutic, while a '
                                          'positive sentinel node usually requires completion neck '
                                          'dissection first.'},
 'v460_hn_slnb_snr': {'stem': 'A 58-year-old woman undergoes resection of a cT1N0 SCC of the '
                              'lateral tongue with sentinel lymph node biopsy. Two sentinel nodes '
                              'are removed from right level II. On step-sectioning and '
                              'immunohistochemistry, one node contains a 0.8-mm focus of '
                              'metastatic carcinoma without extranodal extension. The primary '
                              'margins are clear. What is the most appropriate management of the '
                              'neck?',
                      'choices': ['Observation, because the deposit is under 2 mm',
                                  'Completion neck dissection on the right side',
                                  'Contralateral sentinel node biopsy before deciding',
                                  'Postoperative radiation to the primary site only'],
                      'answer': 1,
                      'explanation': 'A metastatic deposit larger than 0.2 mm but no more than 2 '
                                     'mm is a micrometastasis, and in the main sentinel node '
                                     'trials positive sentinel nodes, including micrometastases, '
                                     'were followed by completion neck dissection, which is the '
                                     'standard response. The completed dissection then defines the '
                                     'total nodal burden and guides adjuvant therapy. Whether '
                                     'isolated tumor cells, deposits of 0.2 mm or less, need '
                                     'further treatment is debated, and protocols differ on that '
                                     'narrower question.',
                      'why_wrong': ['Micrometastases predict additional nonsentinel disease in a '
                                    'meaningful share of patients, so observation is not standard.',
                                    'Correct.',
                                    'A lateralized tongue tumor with ipsilateral drainage does not '
                                    'need contralateral sampling before treating the positive '
                                    'side.',
                                    'Irradiating only the primary leaves the positive neck '
                                    'untreated, which is the site of proven metastatic disease.'],
                      'board_pearl': 'Positive sentinel node, including micrometastasis: '
                                     'completion neck dissection; isolated tumor cells are '
                                     'debated.',
                      'curveball': 'If step-sectioning had shown only isolated tumor cells of 0.1 '
                                   'mm, how would management be debated?',
                      'curveball_answer': 'Isolated tumor cells, deposits of 0.2 mm or less, are '
                                          'classified as pN0 with an itc modifier and carry a '
                                          'lower risk of further nodal disease. Some protocols '
                                          'observe them with close ultrasound surveillance, while '
                                          'others still recommend completion neck dissection. The '
                                          'decision is individualized in multidisciplinary review, '
                                          'and evidence is limited.',
                      'accuracy_note': "Replaced the original's vague 'no single uniform response' "
                                       'answer with completion neck dissection, the standard after '
                                       'a sentinel node micrometastasis; observation is debated '
                                       'only for isolated tumor cells.'},
 'v443-head-neck-oncology-lip-cancer-01': {'stem': 'A 71-year-old retired farmer has a 2-cm '
                                                   'ulcerated SCC of the left lower lip vermilion, '
                                                   'confirmed on biopsy. Over the past month he '
                                                   'has noticed numbness of the left lower lip and '
                                                   'chin. There are no palpable neck nodes, and '
                                                   'the mandible is not tender. Wedge excision '
                                                   'with 5-mm margins and primary closure had been '
                                                   'planned. What is the most appropriate next '
                                                   'step?',
                                           'choices': ['Proceed with wedge excision as originally '
                                                       'planned',
                                                       'PET-CT to exclude distant metastatic '
                                                       'disease',
                                                       'Contrast MRI along the mental and inferior '
                                                       'alveolar nerve',
                                                       'Neurology referral for trigeminal sensory '
                                                       'neuropathy'],
                                           'answer': 2,
                                           'explanation': 'New numbness of the lip and chin in a '
                                                          'patient with lower lip SCC means '
                                                          'perineural spread along the mental '
                                                          'nerve until proven otherwise. The tumor '
                                                          'can track through the mental foramen '
                                                          'into the inferior alveolar canal and '
                                                          'toward the skull base, far beyond the '
                                                          'visible lesion. Contrast MRI along the '
                                                          'nerve, with CT if bone involvement is '
                                                          'suspected, defines the extent. That '
                                                          'finding changes margin planning, may '
                                                          'require mandibular resection, and '
                                                          'usually leads to adjuvant radiation.',
                                           'why_wrong': ['A standard wedge excision would likely '
                                                         'leave tumor along the nerve and result '
                                                         'in a positive perineural margin.',
                                                         'PET-CT has limited sensitivity for '
                                                         'perineural spread and does not address '
                                                         'the local problem raised by the '
                                                         'numbness.',
                                                         'Correct.',
                                                         'In a patient with lip cancer, new '
                                                         'numbness in the mental nerve '
                                                         'distribution reflects tumor spread '
                                                         'rather than an unrelated neuropathy.'],
                                           'board_pearl': 'Lip SCC with chin numbness: perineural '
                                                          'spread along the mental nerve; image '
                                                          'with MRI before resection.',
                                           'curveball': 'The tumor instead involves the oral '
                                                        'commissure. How does that change '
                                                        'reconstructive planning?',
                                           'curveball_answer': 'The commissure has little '
                                                               'redundant tissue and is essential '
                                                               'for oral competence and speech. '
                                                               'Defects involving it are poorly '
                                                               'suited to simple wedge closure and '
                                                               'typically need an Estlander flap, '
                                                               'which rotates upper lip tissue '
                                                               'around the commissure, or a '
                                                               'Karapandzic flap for larger '
                                                               'defects. A secondary '
                                                               'commissuroplasty is often needed '
                                                               'to correct blunting.'},
 'v460_hn_lip_fnd': {'stem': 'A 68-year-old fair-skinned man who worked as a roofer for 40 years '
                             'has a sore on his lower lip that has not healed for 3 months. He '
                             'smokes a pipe. Examination shows a 1.2-cm crusted ulcer on the '
                             'central lower vermilion with a firm, indurated base. The surrounding '
                             'vermilion is dry and scaly. There are no vesicles and no palpable '
                             'neck nodes. What is the most likely diagnosis?',
                     'choices': ['Actinic cheilitis',
                                 'Basal cell carcinoma',
                                 'Squamous cell carcinoma',
                                 'Recurrent herpes labialis'],
                     'answer': 2,
                     'explanation': 'Lip SCC usually arises on the lower lip vermilion, which '
                                    'receives the most direct sunlight, in fair-skinned patients '
                                    'with chronic outdoor exposure, smoking, or immunosuppression. '
                                    'A nonhealing ulcer with induration is the key sign of '
                                    'invasion, and the surrounding dry, scaly vermilion is the '
                                    'precursor actinic cheilitis. Basal cell carcinoma favors the '
                                    'hair-bearing skin of the upper lip. Biopsy confirms the '
                                    'diagnosis and depth of invasion, which helps estimate nodal '
                                    'risk.',
                     'why_wrong': ['Actinic cheilitis is the scaly precursor surrounding this '
                                   'lesion, but an indurated, nonhealing ulcer indicates invasive '
                                   'carcinoma.',
                                   'Basal cell carcinoma arises on hair-bearing cutaneous lip, '
                                   'more often upper lip, and rarely on the lower vermilion.',
                                   'Correct.',
                                   'Herpes labialis presents with vesicles that crust and heal '
                                   'within 2 weeks, not a 3-month indurated ulcer.'],
                     'board_pearl': 'Nonhealing indurated lower vermilion ulcer with sun exposure: '
                                    'lip SCC; BCC favors upper lip skin.',
                     'curveball': 'Why do commissure lesions carry distinct reconstructive '
                                  'implications compared with lesions elsewhere on the lip?',
                     'curveball_answer': 'The commissure has little redundant tissue and anchors '
                                         'the orbicularis oris sphincter, so its loss threatens '
                                         'oral competence, speech, and appearance. Reconstruction '
                                         'must restore a functioning, sensate commissure, often '
                                         'with an Estlander flap or Karapandzic flap, and may need '
                                         'a later commissuroplasty for a rounded, blunted corner.'},
 'v460_hn_lip_app': {'stem': 'A 74-year-old woman has a 1.8-cm SCC of the right lower lip with '
                             '5-mm depth of invasion. She reports tingling and numbness of the '
                             'right chin. MRI shows thickening and enhancement of the right mental '
                             'nerve up to the mental foramen, without involvement of the inferior '
                             'alveolar canal. The neck is clinically and radiographically '
                             'negative. How should this finding change the operative plan?',
                     'choices': ['Standard wedge excision with 5-mm margins only',
                                 'Trace the mental nerve with frozen-section margins',
                                 'Add neck dissection without changing the primary plan',
                                 'Defer surgery and give radiation alone first'],
                     'answer': 1,
                     'explanation': 'Perineural spread along the mental nerve is a distinct risk '
                                    'in lip SCC and should change both imaging and margin '
                                    'planning. Because tumor tracks along the nerve beyond the '
                                    'visible lesion, the resection should follow the nerve toward '
                                    'the mental foramen with frozen-section nerve margins, '
                                    'extending to marginal or segmental mandibulectomy if tumor '
                                    'enters the canal. Named nerve involvement also supports '
                                    'postoperative radiation along the nerve pathway. Depth of '
                                    'invasion guides elective neck management separately.',
                     'why_wrong': ['A standard wedge ignores the documented nerve involvement and '
                                   'would likely leave a positive perineural margin.',
                                   'Correct.',
                                   'Neck dissection may be considered for depth, but it does not '
                                   'address tumor spreading along the mental nerve at the primary.',
                                   'Surgery remains the primary treatment for resectable lip SCC; '
                                   'radiation is usually adjuvant for perineural spread.'],
                     'board_pearl': 'Lip SCC with mental nerve spread: chase the nerve with frozen '
                                    'margins and plan adjuvant radiation.',
                     'curveball': 'Besides perineural spread, what biopsy-derived finding helps '
                                  'estimate her occult nodal risk, similar to oral cavity SCC?',
                     'curveball_answer': 'Depth of invasion, as in oral cavity SCC, predicts '
                                         'occult nodal metastasis. Deeper lesions, roughly beyond '
                                         '4 to 5 mm, along with poor differentiation, recurrence, '
                                         'and lymphovascular invasion, lower the threshold for '
                                         'elective neck dissection, usually of levels I to III, or '
                                         'sentinel node biopsy.'},
 'v460_hn_lip_snr': {'stem': 'A 76-year-old man with diabetes needs excision of a recurrent SCC of '
                             'the left lower lip that involves the oral commissure. After clear '
                             'margins, the defect will span about half of the lower lip, including '
                             'the left commissure, with the central lip and the right side intact. '
                             'He is a poor candidate for further surgery if reconstruction fails, '
                             'and oral competence and speech are his priorities. Which '
                             'reconstruction best fits this defect?',
                     'choices': ['Primary wedge closure of the defect',
                                 'Abbe flap from the central upper lip',
                                 'Estlander flap rotated around the commissure',
                                 'Radial forearm free flap with a palmaris sling'],
                     'answer': 2,
                     'explanation': 'Lip reconstruction depends on defect size and subunit. Up to '
                                    'about one third of the lip can be closed primarily; larger '
                                    'defects need flaps that restore sphincter function. An '
                                    'Estlander flap transfers a full-thickness triangle of upper '
                                    'lateral lip tissue on the labial artery and rotates it around '
                                    'the commissure, so it suits lateral defects that include the '
                                    'commissure, in a single stage. Larger near-total defects use '
                                    'a Karapandzic flap, and total defects may need free tissue.',
                     'why_wrong': ['Primary closure works for defects up to about one third of the '
                                   'lip; closing half the lip would cause severe microstomia.',
                                   'The Abbe flap suits central defects that spare the commissure '
                                   'and requires a second stage to divide the pedicle.',
                                   'Correct.',
                                   'Free tissue transfer is reserved for total or near-total lip '
                                   'defects and is adynamic and insensate, a poor fit here.'],
                     'board_pearl': 'Lateral lip defect involving the commissure: Estlander flap; '
                                    'central defect sparing it: Abbe flap.',
                     'curveball': 'How is lip cancer classified relative to oral cavity cancer for '
                                  'staging, and how does its prognosis compare?',
                     'curveball_answer': 'The lip is a distinct primary site in AJCC, defined as '
                                         'the vermilion surface, yet it is staged with the same T '
                                         'criteria as oral cavity cancer, including depth of '
                                         'invasion. Lip SCC has a more favorable prognosis than '
                                         'most oral cavity subsites, with lower nodal metastasis '
                                         'rates, except for recurrent or perineural tumors.'}}
