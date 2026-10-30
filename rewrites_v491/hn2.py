# v491 rewrites: Head & Neck Oncology part 2
REWRITES = {
    'v134_hno_04': {'stem': 'A 61-year-old man is 6 hours out from segmental mandibulectomy with an anterolateral thigh free flap. The nurse reports the skin paddle has become swollen and violaceous over the last '
             'hour. Pinprick yields brisk dark blood, and the external Doppler signal is present but weaker than the baseline marked at the end of surgery. His blood pressure is 128/76. What is the most '
             'appropriate next step?',
     'choices': ['Loosen any constricting ties or dressings and notify the surgeon for urgent takeback',
                 'Begin a therapeutic heparin infusion and repeat the flap check in 4 hours',
                 'Apply medicinal leeches to the paddle and continue hourly flap checks',
                 'Obtain CT angiography of the neck to confirm pedicle thrombosis first'],
     'answer': 0,
     'explanation': 'A swollen, purple flap with brisk dark pinprick bleeding is the classic picture of venous outflow obstruction, the most common mode of early free-flap failure. Salvage is '
                    'time-dependent because congestion progresses to arterial thrombosis and no-reflow. Correct reversible external compression at the bedside while mobilizing the reconstructive surgeon '
                    'and the OR; do not trade the ischemic window for anticoagulation trials or imaging. A still-audible arterial signal does not exclude venous thrombosis.',
     'why_wrong': ['Correct.',
                   'Systemic heparin does not open a mechanically kinked or thrombosed vein, and a 4-hour delay erodes salvage odds.',
                   'Leeches are a temporizer when outflow cannot be surgically restored, not first-line care for a likely correctable pedicle problem.',
                   'CTA consumes ischemic time and adds little; a congested flap with this exam warrants exploration, not imaging.'],
     'board_pearl': 'Purple, swollen, brisk dark bleeding means venous compromise: relieve compression and go back to the OR now.',
     'curveball': 'The charge nurse points out that the external arterial Doppler signal is still audible. Does that argue against venous thrombosis?',
     'curveball_answer': 'No. Arterial inflow can persist for hours while the venous side is occluded, so the artery keeps transmitting a signal even as the flap congests. An arterial Doppler is not '
                         'proof of viability. The clinical exam of congestion drives the decision; eventually rising venous pressure halts inflow and the arterial signal disappears, by which point '
                         'salvage odds are worse.'},
    'v134_hno_09': {'stem': 'A 57-year-old woman underwent radial forearm free flap reconstruction of a hemiglossectomy defect. At midnight the paddle was pink and warm with 2-second capillary refill and a strong '
             'arterial Doppler signal. At 2 AM it is pale and cool, refill is absent, pinprick yields only a faint bead of serum, and the arterial signal cannot be found. She is normotensive on no '
             'vasopressors. What is the best interpretation?',
     'choices': ['Arterial inflow failure at the pedicle or anastomosis',
                 'Early venous outflow obstruction before swelling has developed',
                 'Expected flap vasospasm that resolves with rewarming',
                 'Benign postoperative dehydration with reduced dermal perfusion'],
     'answer': 0,
     'explanation': 'A pale, cool flap with absent refill, no fresh pinprick bleeding, and loss of the arterial signal after a documented normal baseline indicates arterial inflow failure: anastomotic '
                    'thrombosis, pedicle kink or twist, or extrinsic compression. Arterial compromise is less visually dramatic than venous congestion and easy to dismiss, but the abrupt change from '
                    'baseline in a normotensive patient makes this a surgical emergency requiring urgent exploration.',
     'why_wrong': ['Correct.',
                   'Venous obstruction produces a swollen, dusky flap with brisk dark bleeding, the opposite of this pale, nonbleeding paddle.',
                   'Vasospasm is a diagnosis of exclusion at exploration; attributing abrupt signal loss to spasm delays rescue of a thrombosed artery.',
                   'She is normotensive, and dehydration does not abolish an arterial Doppler signal from a previously healthy flap.'],
     'board_pearl': 'Pale, cool, no refill, no pinprick bleeding, lost arterial signal: arterial inflow failure needing urgent exploration.',
     'curveball': "At exploration the arterial anastomosis is patent, but a tense hematoma is compressing the pedicle. What does this teach about the 'thrombosed' flap?",
     'curveball_answer': 'Extrinsic compression mimics intrinsic thrombosis, so the differential must include hematoma, tight closure or dressings, tracheostomy ties, edema, and pedicle kink or twist '
                         'from head position. Evacuating the hematoma and repositioning the pedicle may restore flow without anastomotic revision, but only if found quickly. Prolonged compression still '
                         'causes secondary thrombosis, so the same urgency applies.'},
    'v138_hn_07': {'stem': 'A 70-year-old man is 10 hours out from a fibula free flap for osteoradionecrosis of the mandible. On rounds the skin paddle is tense and blue with rapid dark bleeding on pinprick and '
             '1-second capillary refill. The intern suggests this is arterial thrombosis because the flap is blue. The neck is soft without hematoma. Which is the most accurate assessment and plan?',
     'choices': ['Venous congestion, warranting prompt return to the OR for pedicle exploration',
                 'Arterial thrombosis, best managed with a thrombolytic infusion given at the bedside',
                 'Normal early flap edema, best managed with head elevation and observation',
                 'Venous congestion, best managed with leeches as the definitive treatment'],
     'answer': 0,
     'explanation': 'Blue color with tense swelling, brisk refill, and rapid dark bleeding indicates venous outflow obstruction, not arterial failure. Arterial compromise produces a pale, cool flap with '
                    'sluggish or absent refill and little bleeding. Venous thrombosis is the more common cause of early failure, and congestion progresses to arterial stasis, so the standard is urgent '
                    'exploration of the venous anastomosis and pedicle geometry rather than bedside temporizing.',
     'why_wrong': ['Correct.',
                   'Arterial failure makes a flap pale and nonbleeding; thrombolytics also require surgical access to the pedicle, not bedside infusion.',
                   'Physiologic edema does not produce a tense blue paddle with brisk dark bleeding; observation wastes the salvage window.',
                   'Leeches are a temporizing adjunct when surgical outflow cannot be re-established, not a substitute for exploring a correctable pedicle.'],
     'board_pearl': 'Blue does not mean arterial: congestion, brisk dark bleeding and fast refill signal venous outflow failure.',
     'curveball': 'The intern asks how this same paddle would look if the artery, rather than the vein, had thrombosed. What would you teach?',
     'curveball_answer': 'Arterial insufficiency produces a pale or mottled, cool, flat or soft paddle with delayed or absent capillary refill and little or no bleeding on pinprick, often with loss of '
                         'the arterial Doppler signal. It is less visually striking than congestion, so it is easily missed. Mixed pictures occur, and late venous failure can end with arterial stasis.'},
    'v140_hn_01': {'stem': 'A 64-year-old woman with a buccal SCC had a radial forearm free flap 4 hours ago. Her systolic pressure has stayed above 120 mm Hg. The paddle is now white and cool, capillary refill is '
             'absent, there is no bleeding after a 25-gauge needle stick, and the handheld Doppler finds no pedicle signal. Neck drain output is 30 mL serosanguinous. What vascular problem is most '
             'likely?',
     'choices': ['Arterial insufficiency from inflow compromise',
                 'Low-flow state from relative systemic hypotension',
                 'Venous anastomotic thrombosis with outflow obstruction',
                 'Microvascular no-reflow from prolonged primary ischemia'],
     'answer': 0,
     'explanation': 'White, cool skin with absent refill and no pinprick bleeding, together with loss of the pedicle signal, defines arterial insufficiency. Common causes are anastomotic thrombosis, '
                    'intimal flap, vessel kinking, or compression. Her blood pressure is stable and drain output is modest, removing systemic hypotension and large hematoma as the explanation. Because '
                    'salvage falls quickly with ischemia time, this requires urgent exploration of the pedicle.',
     'why_wrong': ['Correct.',
                   'Her systolic pressure has stayed above 120 mm Hg, so systemic hypotension does not explain abrupt loss of the pedicle signal.',
                   'Venous thrombosis causes a swollen, dusky flap with brisk dark bleeding rather than a white, nonbleeding paddle.',
                   'No-reflow describes failed perfusion despite a patent revised anastomosis after prolonged ischemia, not a new postoperative change at 4 hours.'],
     'board_pearl': 'White, cool, no refill or pinprick bleeding with absent signal equals arterial insufficiency until the pedicle is explored.',
     'curveball': 'You return her to the OR. In what order should you inspect and correct the problem once the neck is open?',
     'curveball_answer': 'First evacuate any hematoma and check pedicle geometry for kink, twist, tension, or compression. Then assess inflow from the recipient artery and inspect each anastomosis. If '
                         'thrombus is present, take down the anastomosis, remove clot with thrombectomy and heparinized saline irrigation, consider intra-arterial thrombolytic with venous effluent '
                         'drained out, and redo the anastomosis, changing recipient vessels if needed.'},
    'v148_hn_03': {'stem': 'A 59-year-old man had a total glossectomy reconstructed with an anterolateral thigh free flap. Six hours later the flap is cool and pale, capillary refill is sluggish beyond 4 seconds, and '
             'the arterial Doppler signal that was strong at 2 hours is gone. He is normotensive, his drain output is low, and there is no neck swelling. What is the most appropriate management?',
     'choices': ['Obtain urgent CT angiography of the neck to localize the occlusion',
                 'Give an intravenous heparin bolus and recheck the flap in 1 hour',
                 'Warm the room and flap, then repeat the Doppler examination in 2 hours',
                 'Return to the operating room promptly to explore the pedicle'],
     'answer': 3,
     'explanation': 'Loss of a previously strong arterial signal with a cool, pale flap and sluggish refill indicates arterial inflow compromise. The deciding features are the documented change from '
                    'baseline and the absence of a systemic explanation such as hypotension. Salvage rates fall steeply with ischemia time, and a no-reflow state develops with prolonged ischemia, so the '
                    'patient needs immediate operative exploration rather than further diagnostic or pharmacologic trials.',
     'why_wrong': ['CTA delays surgery without changing the plan; clinical findings already justify exploration of the pedicle.',
                   'Heparin does not correct a kink or occlusive thrombus, and an hour of observation lengthens ischemia time.',
                   'Cooling does not abolish an established arterial signal, and waiting 2 hours risks irreversible no-reflow.',
                   'Correct.'],
     'board_pearl': 'Monitoring exists to trigger rescue: a lost arterial signal with a pale, cool flap means the OR, not imaging.',
     'curveball': 'Exploration shows a patent arterial anastomosis, but the flap still has no venous outflow and is now slowly congesting. What is the next consideration?',
     'curveball_answer': 'Arterial failure that appears to resolve or is not explained may hide a venous problem, and late venous thrombosis can mimic or follow arterial stasis. Examine the vein for '
                         'thrombus, kink, or compression, and revise the venous anastomosis or add a second venous outflow, using a different recipient vein if needed. Venous congestion typically '
                         'produces brisk dark bleeding and swelling.'},
    'v152_hn_01': {'stem': 'A 66-year-old woman is 8 hours out from fibula free flap reconstruction of the mandible. At 2 AM the night nurse calls you, the covering junior resident: the skin paddle is swollen and '
             'violaceous, pinprick produces brisk dark bleeding, and the venous Doppler signal is fading. You notice the tracheostomy ties are tight across the neck. What should you do first?',
     'choices': ['Document the findings and plan to reassess on morning rounds',
                 'Place a compressive dressing over the paddle to reduce swelling',
                 'Start intravenous furosemide and recheck the paddle color in 2 hours',
                 'Loosen the ties and call the reconstructive surgeon to plan takeback'],
     'answer': 3,
     'explanation': 'Congestion with brisk dark bleeding and a fading venous signal means impaired venous outflow. Tight tracheostomy ties are a classic reversible cause of jugular and pedicle '
                    'compression, so loosen them immediately. Bedside correction must run in parallel with, not instead of, immediate senior notification and preparation for exploration, because venous '
                    'thrombosis is time-sensitive and salvage odds fall with every hour of congestion.',
     'why_wrong': ['Waiting until rounds spends the salvage window; venous compromise must be escalated as soon as it is recognized.',
                   'External pressure worsens venous outflow obstruction and can compress the pedicle, accelerating flap loss.',
                   'Diuresis does not treat outflow obstruction, and a 2-hour wait allows congestion to progress to thrombosis.',
                   'Correct.'],
     'board_pearl': 'Fix external compression at the bedside, but call the surgeon and prepare the OR at the same time.',
     'curveball': 'After loosening the ties, the implantable venous Doppler is still audible, but the paddle keeps darkening over 20 minutes. What should drive the decision?',
     'curveball_answer': 'The clinical exam. Doppler and tissue-oxygen monitors are adjuncts that speed detection, especially for buried flaps, but they should not overrule a clearly worsening '
                         'accessible flap. Partial thrombus, a malpositioned probe, or flow in a different vein can keep a signal present. A progressively congesting paddle warrants takeback even when '
                         'the device is reassuring.'},
    'v228_hn_flap_fnd': {'stem': 'A 55-year-old man is admitted to the step-down unit after resection of a floor-of-mouth SCC and radial forearm free flap reconstruction. Orders call for flap checks every hour for the '
             'first 24 hours, then every 2 to 4 hours through postoperative day 3. A new nurse asks why checks are so frequent early and then tapered. Which statement best explains this schedule?',
     'choices': ['Most failures occur within 72 hours, and salvage odds fall as ischemia time lengthens',
                 'Most failures occur after day 5, so early checks mainly establish a reliable baseline signal',
                 'Early checks chiefly detect wound infection, which is the leading cause of flap loss',
                 'Frequent checks are needed because Doppler alone cannot be used after the first day'],
     'answer': 0,
     'explanation': 'The fresh anastomosis is most thrombogenic until endothelium covers the suture line, so most thromboses and flap failures occur within the first 48 to 72 hours, with venous '
                    'thrombosis more common than arterial. Salvage depends on detecting compromise within hours, before no-reflow develops. Intensive early monitoring, tapered as risk falls, maximizes '
                    'the chance that a threatened flap reaches the OR in time.',
     'why_wrong': ['Correct.',
                   'Late failure is uncommon and usually relates to infection or fistula; the thrombotic risk peaks in the first 72 hours.',
                   'Infection is a later and less common cause of loss; early monitoring targets vascular thrombosis and compression.',
                   'Doppler remains a useful adjunct throughout; the issue is timing of thrombotic risk, not the limits of any device.'],
     'board_pearl': 'Free-flap thrombosis clusters in the first 72 hours, venous more than arterial; early detection drives salvage.',
     'curveball': 'The nurse then asks how she will tell a venous problem from an arterial one at the bedside. What do you teach?',
     'curveball_answer': 'Venous compromise makes the flap swollen, tense, and dusky or purple, with brisk capillary refill and rapid dark blood on pinprick. Arterial compromise makes it pale, cool, and '
                         'flat, with slow or absent refill and little or no bleeding. Compare every check against the marked baseline, and call immediately for any change rather than waiting for the '
                         'next scheduled check.'},
    'v228_hn_flap_app': {'stem': 'A 68-year-old man had a buried jejunal free flap after total laryngopharyngectomy, monitored with an exteriorized segment and an implantable venous coupler probe. Six hours postoperatively '
             'the monitor segment is dusky and swollen, its mucosa oozes dark blood when pricked, and the venous probe signal has been lost. The probe cable is connected and the console is working. What '
             'is the best next step?',
     'choices': ['Apply leeches to the monitor segment and continue hourly observation',
                 'Obtain CT angiography to confirm venous thrombosis before reexploring',
                 'Start a heparin infusion and reassess the monitor segment at 6 hours',
                 'Release any external compression and proceed to urgent exploration'],
     'answer': 3,
     'explanation': 'A dusky, swollen monitor segment with dark bleeding and loss of the venous coupler signal strongly suggests venous outflow failure. Once equipment malfunction is excluded and '
                    'reversible external compression addressed, urgent takeback is indicated. The threshold is especially low for buried flaps, because surface examination is limited and the monitor '
                    'segment and implantable probe are the only windows on the pedicle.',
     'why_wrong': ['Leeches do not decompress a thrombosed visceral flap and only temporize when surgical outflow cannot be restored.',
                   'Imaging delays exploration and rarely changes the decision when clinical and probe findings already agree.',
                   'Anticoagulation alone does not clear an occlusive venous thrombus, and 6 hours of congestion invites no-reflow.',
                   'Correct.'],
     'board_pearl': 'Buried flaps get a lower takeback threshold: trust monitor segments and implantable probes once equipment is verified.',
     'curveball': 'In a similar patient with a skin-paddle flap, which bedside clues point to a compressive hematoma rather than intrinsic anastomotic thrombosis?',
     'curveball_answer': 'Hematoma is suggested by a tense, expanding neck swelling, rising or bloody drain output, ecchymosis, a clotted or nonfunctioning drain, and airway compromise, often with '
                         'congestion developing alongside the neck swelling. Anticoagulant use and hypertension add risk. It still requires urgent return to the OR, where evacuation may restore flow '
                         'without anastomotic revision.'},
    'v228_hn_flap_snr': {'stem': 'A 62-year-old woman is returned to the OR 5 hours after the first signs of congestion in an anterolateral thigh free flap for a parotidectomy defect. Exploration shows a twisted vein with '
             'occlusive thrombus at the venous anastomosis; the artery is patent. The paddle is dark but still bleeds after release. Which approach should guide this salvage attempt?',
     'choices': ['Untwist the pedicle, clear thrombus, and redo the venous anastomosis',
                 'Discard the flap and close with a pedicled pectoralis flap immediately',
                 'Infuse thrombolytic through the flap artery and close without revision',
                 'Apply leeches to the paddle and close the neck to limit operative time'],
     'answer': 0,
     'explanation': 'Salvage begins with correcting the mechanical cause, here the twisted vein, then removing thrombus and revising the anastomosis to restore outflow, and judging tissue viability by '
                    'bleeding and color. Thrombolytic infusion, extra venous outflow, and postoperative leeches are adjuncts when microvascular clot persists. With a correctable problem and a '
                    'still-bleeding paddle, salvage is reasonable and often succeeds despite several hours of congestion.',
     'why_wrong': ['Correct.',
                   'Abandoning a flap with a correctable cause and bleeding tissue forfeits a reasonable chance of successful salvage.',
                   'Thrombolytics clear microvascular clot but leave the twist that caused the thrombosis, so rethrombosis is likely.',
                   'Leeches temporize when outflow cannot be surgically restored; here the venous problem is directly correctable.'],
     'board_pearl': 'Salvage means fixing the mechanical cause, clearing thrombus, revising the anastomosis, then confirming the tissue bleeds.',
     'curveball': 'After venous revision and thrombolysis, the paddle still does not bleed and the skin stays mottled. When is a second flap or alternative reconstruction preferable?',
     'curveball_answer': 'When perfusion fails despite a technically patent anastomosis, suggesting no-reflow, when tissue is clearly nonviable, when recipient vessels or donor options are exhausted, or '
                         'when the patient cannot tolerate more anesthesia. In those cases, debride the flap and use a second free flap or pedicled flap, either immediately or after the wound is '
                         'controlled.'},
    'v134_hno_05': {'stem': 'A 63-year-old man is 3 days out from a left modified radical neck dissection including level IV for metastatic laryngeal SCC. Drain output was clear and serosanguinous until enteral feeds '
             'were advanced; it is now milky white and 700 mL over 24 hours. There is fullness above the left clavicle without skin changes. Which structure was most likely injured?',
     'choices': ['Thoracic duct near the left jugulosubclavian junction',
                 'Right lymphatic duct as it enters the right venous angle',
                 'Cisterna chyli injured through the thoracic inlet',
                 'Submandibular duct with saliva tracking inferiorly'],
     'answer': 0,
     'explanation': 'Milky drainage that appears or rises once enteral fat is given is chyle, and on the left it comes from the thoracic duct, which arches up behind the carotid sheath and enters the '
                    'venous system at the junction of the internal jugular and subclavian veins in low level IV. Left-sided leaks are far more common than right-sided ones. Drain triglycerides above 100 '
                    'mg/dL or chylomicrons confirm the diagnosis.',
     'why_wrong': ['Correct.',
                   'The right lymphatic duct drains on the right; this leak is on the left, where the thoracic duct terminates.',
                   'The cisterna chyli lies in the upper abdomen and is not exposed during a cervical neck dissection.',
                   'Saliva is clear, not milky, and does not increase with enteral fat; it also arises far from level IV.'],
     'board_pearl': 'Milky left low-neck drainage after feeds is a thoracic duct leak; drain triglyceride above 100 mg/dL confirms it.',
     'curveball': 'Despite a medium-chain triglyceride diet, output remains near 1 liter daily after 5 days. Which features push you toward intervention?',
     'curveball_answer': 'Escalate for persistently high output (commonly cited near 1 liter per day), failure to decline after roughly a week of conservative care, skin flap compromise, chylous '
                         'collection threatening the wound, or electrolyte, protein, or lymphocyte depletion. Options include NPO with parenteral nutrition, octreotide, percutaneous thoracic duct '
                         'embolization, and neck re-exploration with duct ligation, sometimes with a muscle flap.'},
    'v134_hno_06': {'stem': 'A 54-year-old woman returns 3 weeks after a right selective neck dissection of levels II to IV for oral tongue SCC. She has an aching right shoulder, cannot raise her arm above horizontal '
             'to reach a shelf, and the shoulder sits lower than the left. With arm abduction the scapula flares laterally, and shrug strength is reduced. Serratus anterior strength is normal. Which '
             'nerve is most likely injured?',
     'choices': ['Long thoracic nerve', 'Upper trunk of the brachial plexus', 'Dorsal scapular nerve', 'Spinal accessory nerve'],
     'answer': 3,
     'explanation': 'The spinal accessory nerve crosses level IIA and IIB and supplies the trapezius, which elevates and upwardly rotates the scapula. Injury produces shoulder droop, weak shrug, lateral '
                    'scapular flaring on abduction, inability to abduct above about 90 degrees, and pain from adhesive capsulitis. Normal serratus strength excludes the long thoracic nerve, and the '
                    'absence of deltoid or biceps weakness argues against the brachial plexus.',
     'why_wrong': ['Long thoracic injury causes medial winging with wall push from serratus weakness, but her serratus strength is normal.',
                   'Upper trunk injury would weaken deltoid, biceps, and shoulder external rotation, not mainly shrug and scapular position.',
                   'Dorsal scapular palsy weakens the rhomboids with subtle medial winging and does not reduce shrug or cause marked shoulder droop.',
                   'Correct.'],
     'board_pearl': 'Shoulder droop, weak shrug, lateral scapular flaring and no overhead abduction localize to CN XI and the trapezius.',
     'curveball': 'Her operative note says the nerve was identified and preserved throughout. How can she still have this deficit, and what should start now?',
     'curveball_answer': 'Traction, skeletonization over long segments, devascularization, and cautery heat can cause neuropraxia even when the nerve is intact; division of cervical plexus contributions '
                         'adds to it. Begin shoulder-focused physical therapy early to keep range of motion and prevent adhesive capsulitis, document function, and reassess. Persistent deficits at '
                         'several months may warrant EMG.'},
    'v138_hn_04': {'stem': 'A 71-year-old man had a posterolateral neck dissection including level V for a scalp cutaneous SCC with parotid and neck metastases. At 6 weeks he cannot lift his arm overhead to comb his '
             'hair, the shoulder droops, and the scapula wings laterally on abduction. Sensation over the ear and lateral neck is reduced. Which structure injury best explains his weakness?',
     'choices': ['Cervical plexus sensory branches at Erb point', 'C5 root in the interscalene groove', 'Long thoracic nerve on the serratus anterior', 'Accessory nerve in the posterior triangle'],
     'answer': 3,
     'explanation': 'In level V the spinal accessory nerve runs superficially across the posterior triangle on the levator scapulae, emerging near Erb point before entering the trapezius, which makes it '
                    'easy to injure. Trapezius denervation explains the droop, lateral winging, and failed overhead abduction. Numbness over the ear and lateral neck comes from expected sacrifice of '
                    'great auricular and transverse cervical branches, which causes sensory loss but no shoulder weakness.',
     'why_wrong': ['Cervical plexus sensory branches explain his numbness but carry no motor fibers to the trapezius.',
                   'A C5 root injury would weaken the deltoid and biceps and reduce reflexes rather than produce trapezius-pattern droop.',
                   'Long thoracic injury produces medial winging from serratus palsy, not shoulder droop with lateral winging.',
                   'Correct.'],
     'board_pearl': 'Level V puts CN XI at greatest risk because it lies superficially in the posterior triangle.',
     'curveball': 'A different patient after a submandibular-level dissection cannot depress the lower lip on one side when smiling. Which nerve is injured, and how do you confirm it?',
     'curveball_answer': 'The marginal mandibular branch of the facial nerve, which runs deep to platysma along the lower border of the mandible and supplies depressor labii inferioris. Have the patient '
                         'show the lower teeth: the lip fails to depress on that side. If the lip still everts normally on pouting, mentalis is spared, distinguishing true marginal nerve injury from '
                         'cervical branch platysma weakness, a pseudoparalysis.'},
    'v145_hn_04': {'stem': 'A 48-year-old man has persistent right shoulder pain and weakness 4 months after a right modified radical neck dissection for oropharyngeal SCC. Exam shows shoulder droop and inability to '
             'abduct above 90 degrees. EMG shows active denervation of the right trapezius with normal deltoid, supraspinatus, and serratus anterior. Which structure was most likely injured?',
     'choices': ['Spinal accessory nerve', 'Suprascapular nerve', 'Axillary nerve', 'Long thoracic nerve'],
     'answer': 0,
     'explanation': 'Isolated trapezius denervation on EMG with normal deltoid, supraspinatus, and serratus localizes the lesion to the spinal accessory nerve, which is dissected in levels II and V '
                    'during modified radical neck dissection. Trapezius loss causes shoulder droop, lateral scapular instability, and limited abduction, often with chronic pain. EMG separates CN XI '
                    'injury from other causes of postoperative shoulder dysfunction and gives a baseline for recovery.',
     'why_wrong': ['Correct.',
                   "Suprascapular palsy weakens supraspinatus and infraspinatus, but supraspinatus is normal on this patient's EMG.",
                   'Axillary nerve injury denervates the deltoid, which is normal here, and the nerve is not exposed in a neck dissection.',
                   'Long thoracic injury denervates serratus anterior, which shows normal findings on this EMG.'],
     'board_pearl': 'Isolated trapezius denervation after neck dissection localizes to CN XI; EMG documents injury and recovery.',
     'curveball': 'His contralateral neck dissection was complicated by milky high-output drainage from the left lower neck. What is likely, and what is the first-line approach?',
     'curveball_answer': 'A chyle leak from the thoracic duct. Confirm with drain triglycerides above 100 mg/dL or chylomicrons. First-line management for low or moderate output is closed suction '
                         'drainage, a fat-free or medium-chain triglyceride diet, and sometimes octreotide or pressure dressings. High or refractory output escalates to NPO with parenteral nutrition, '
                         'thoracic duct embolization, or re-exploration.'},
    'v148_hn_04': {'stem': 'A 67-year-old woman is 4 hours out from a bilateral neck dissection and partial laryngectomy, with no tracheostomy. She develops rapidly expanding swelling under the incision, a muffled '
             'voice, inspiratory stridor, and oxygen saturation falling to 88%. The drains contain clot. The anesthesia team is on the way. What is the most appropriate immediate action?',
     'choices': ['Open the incision at the bedside to decompress the hematoma',
                 'Give racemic epinephrine and dexamethasone, then reassess airway',
                 'Obtain a CT of the neck to define the size of the collection',
                 'Aspirate the collection with a large-bore needle through the skin'],
     'answer': 0,
     'explanation': 'An expanding neck hematoma with stridor and desaturation is an airway emergency. The hematoma obstructs venous and lymphatic outflow, causing laryngeal and pharyngeal edema beyond '
                    'simple compression. Opening the skin and platysma at the bedside evacuates clot and relieves pressure immediately, buying time for a controlled airway and return to the OR for '
                    'hemostasis. Imaging and medical temporizing waste minutes that may be fatal.',
     'why_wrong': ['Correct.',
                   'Epinephrine and steroids do not treat compression or venous congestion from an expanding hematoma and delay definitive relief.',
                   'Sending an unstable stridulous patient to CT delays decompression and risks complete obstruction outside a controlled setting.',
                   'Clotted blood cannot be aspirated effectively through a needle, and the attempt delays definitive bedside decompression.'],
     'board_pearl': 'Expanding neck hematoma with stridor: open the wound at the bedside, then secure the airway and control bleeding.',
     'curveball': 'In another patient the collection is small, soft, and not enlarging, and the airway is normal. How does management change?',
     'curveball_answer': 'A stable, nonexpanding hematoma without airway symptoms can be observed closely with drain checks, blood pressure control, and correction of coagulopathy or anticoagulant '
                         'effect. Larger collections that compromise flaps, threaten a free-flap pedicle, or persist may need elective evacuation in the OR. Any expansion or airway change converts it to '
                         'an emergency.'},
    'v231_hn_neckcomp_fnd': {'stem': 'A 58-year-old man is 2 days out from a left selective neck dissection of levels II to IV for papillary thyroid carcinoma. After he resumed a regular diet, his drain output turned cloudy '
             'white and rose to 350 mL per day. He is afebrile without wound erythema. Drain fluid triglyceride is 480 mg/dL. Which complication is most likely?',
     'choices': ['Pharyngocutaneous fistula from an unrecognized pharyngeal mucosal tear',
                 'Chyle leak from injury to the thoracic duct or its tributaries',
                 'Seroma with serous fluid collecting in the dissection bed',
                 'Infected collection with purulent drainage from the wound'],
     'answer': 1,
     'explanation': 'Cloudy white drainage that rises after a regular diet, with drain triglyceride far above 100 mg/dL, establishes a chyle leak. The thoracic duct and its variable tributaries enter '
                    'the left venous angle and are at risk during level IV dissection. Persistent loss matters because chyle carries fat, protein, fluid, electrolytes, and lymphocytes, so prolonged '
                    'leaks cause malnutrition, immunosuppression, and wound breakdown.',
     'why_wrong': ['No pharyngeal mucosa is entered in a thyroid-related neck dissection, and saliva has low triglyceride content.',
                   'Correct.',
                   'Seroma fluid is clear and straw colored with low triglycerides, unlike this fat-laden drainage.',
                   'He is afebrile without wound erythema, and purulence would not produce a triglyceride level this high.'],
     'board_pearl': 'Chyle leak: milky drainage rising with dietary fat, triglyceride above 100 mg/dL; left level IV is the classic site.',
     'curveball': 'How would management differ if output were 150 mL per day versus over 1 liter per day persisting after a week?',
     'curveball_answer': 'Low output usually closes with drainage, a fat-free or medium-chain triglyceride diet, pressure dressing, and possibly octreotide. Persistent high output after about a week of '
                         'conservative care, or metabolic depletion, warrants NPO with parenteral nutrition and early intervention: lymphangiography with thoracic duct embolization or neck exploration '
                         'with duct ligation, sometimes reinforced with a muscle flap or sealant.'},
    'v231_hn_neckcomp_app': {'stem': 'A 50-year-old woman is on postoperative day 1 after a left selective neck dissection of levels II to IV. The operative note documents a dissected but preserved spinal accessory nerve. She '
             'has a drooping left shoulder, weak shrug, and cannot abduct above shoulder height. The incision is dry, and deltoid and biceps strength are normal. What is the best interpretation and '
             'plan?',
     'choices': ['Rotator cuff tear from positioning; obtain a shoulder MRI',
                 'Nerve transection missed at surgery; explore and graft now',
                 'Brachial plexus stretch; immobilize the arm in a sling',
                 'CN XI neuropraxia; start early shoulder physical therapy'],
     'answer': 3,
     'explanation': 'A preserved but dissected spinal accessory nerve commonly suffers neuropraxia from traction, skeletonization, or devascularization, producing trapezius weakness that usually '
                    'recovers over months. The right response is to document function and begin early shoulder-focused rehabilitation to prevent adhesive capsulitis, chronic pain, and scapular '
                    'dyskinesis. The operative note of nerve continuity argues against immediate exploration, and normal deltoid and biceps exclude a plexus injury.',
     'why_wrong': ['The pattern of droop and weak shrug matches trapezius denervation, not a cuff tear, so MRI misdirects care.',
                   'The nerve was documented intact, so early exploration risks further injury; persistent deficit can be evaluated later with EMG.',
                   'Normal deltoid and biceps argue against plexus injury, and immobilization promotes frozen shoulder after CN XI dysfunction.',
                   'Correct.'],
     'board_pearl': 'A preserved CN XI can still fail from traction or devascularization; start shoulder therapy early.',
     'curveball': 'Which other new deficits after a level II to IV dissection should prompt evaluation of a different injured nerve?',
     'curveball_answer': 'Tongue deviation toward the operated side suggests hypoglossal injury; hoarseness or aspiration suggests vagal or recurrent laryngeal injury needing laryngoscopy; ptosis and '
                         'miosis suggest sympathetic chain injury; an elevated hemidiaphragm suggests phrenic injury; lower-lip weakness suggests marginal mandibular injury; and arm weakness suggests '
                         'brachial plexus injury.'},
    'v231_hn_neckcomp_snr': {'stem': 'A 64-year-old man is 9 days out from salvage neck dissection in a previously irradiated field. The wound has broken down, and saliva from a small pharyngeal leak bathes a pale, exposed '
             'segment of the common carotid artery. There has been no bleeding. He is afebrile on antibiotics, and his hemoglobin is stable. What is the most appropriate management?',
     'choices': ['Place negative-pressure wound therapy directly over the artery',
                 'Divert saliva, debride, and cover the artery with vascularized muscle',
                 'Begin wet-to-dry dressings and await secondary granulation',
                 'Resume oral feeding and pack the wound with iodoform gauze'],
     'answer': 1,
     'explanation': 'An exposed carotid in an irradiated, salivary-contaminated wound is a sentinel state for carotid blowout, which carries high mortality. Management addresses every driver: control '
                    'salivary contamination and infection, debride devitalized tissue, image the vessel wall for pseudoaneurysm, involve interventional radiology, and bring well-vascularized tissue such '
                    'as a pectoralis major flap to cover the artery. Irradiated skin cannot be expected to heal over the vessel.',
     'why_wrong': ['Negative-pressure therapy over an exposed major vessel risks erosion and rupture and does not address salivary contamination.',
                   'Correct.',
                   'Secondary healing over an irradiated, contaminated carotid is slow and unreliable, leaving the vessel at risk of blowout.',
                   'Oral intake increases salivary and food contamination of the wound and does nothing to protect the exposed artery.'],
     'board_pearl': 'Exposed carotid plus saliva in an irradiated field threatens blowout: divert, debride, image, and cover with vascularized tissue.',
     'curveball': 'CT angiography shows a small pseudoaneurysm and vessel-wall irregularity at the exposed segment. Which interventional options become relevant?',
     'curveball_answer': 'Interventional radiology can place a covered stent to exclude the pseudoaneurysm while preserving flow, accepting infection risk in a contaminated field, or perform permanent '
                         'carotid occlusion, ideally after a balloon test occlusion confirms adequate collateral flow. Either is followed by definitive vascularized flap coverage, with prepared blood '
                         'products and a plan for sentinel bleeding.'},
    'v134_hno_07': {'stem': 'A 72-year-old man with recurrent oral cavity SCC after surgery and chemoradiation has lung and bone metastases. A painful fungating right neck mass oozes intermittently but has never bled '
             'heavily; his airway is patent. He spends most of the day in bed (ECOG 3). He tells you his priority is staying home with his wife and avoiding further hospital stays. Which plan best fits '
             'his situation?',
     'choices': ['Composite neck resection with pectoralis flap coverage for local control',
                 'Elective tracheostomy now to prevent a future airway emergency at home',
                 'Inpatient admission for third-line systemic therapy and daily dressing changes',
                 'Home-based analgesia and wound care, offering a short palliative RT course'],
     'answer': 3,
     'explanation': 'With metastatic disease, poor performance status, and a clear priority of staying home, the best plan is goal-concordant symptom care: scheduled analgesia with neuropathic agents as '
                    'needed, wound care with absorbent and hemostatic dressings, and an offer of hypofractionated palliative radiation if he accepts the visits for pain and oozing. Every intervention '
                    'should be tied to a realistic symptom target and to what he values, not to technical feasibility.',
     'why_wrong': ['Technical resectability does not create an obligation to operate; this morbid surgery conflicts with his goals and prognosis.',
                   'He has no airway compromise, and a tracheostomy adds care burden and hospitalization he has said he wants to avoid.',
                   'Admission contradicts his stated priority, and further systemic therapy at ECOG 3 offers little benefit with substantial toxicity.',
                   'Correct.'],
     'board_pearl': "Palliative ENT care is active care: match each intervention to a symptom target and the patient's stated priorities.",
     'curveball': 'Two weeks later the oozing becomes a brisk bleed from the neck, and imaging shows tumor abutting the carotid. How does the plan change if goals stay comfort-focused?',
     'curveball_answer': 'Revisit goals immediately and build an explicit hemorrhage plan: whether he wants transfer or endovascular treatment, dark towels and pressure at home, a crisis sedative such '
                         'as midazolam with opioid available to family or hospice, and preparation of family for a possible terminal bleed. Hemostatic dressings or palliative radiation may reduce minor '
                         'bleeding.'},
    'v138_hn_17': {'stem': 'A 78-year-old woman with recurrent laryngeal SCC after chemoradiation declined salvage laryngectomy. She has intermittent tumor bleeding, odynophagia, and 8% weight loss. Her oncologist '
             'plans palliative radiation for the bleeding and offers pembrolizumab. She asks whether seeing the palliative care team means stopping cancer treatment. What is the best response?',
     'choices': ['Palliative care can start now, alongside radiation and immunotherapy',
                 'Palliative care requires hospice enrollment, which ends radiation',
                 'Palliative care begins after cancer treatment ends, so defer referral',
                 'Palliative care begins once a do-not-resuscitate order is signed'],
     'answer': 0,
     'explanation': 'Specialist palliative care is concurrent care. ASCO guidance supports early referral for patients with advanced cancer and significant symptom burden while disease-directed '
                    'treatment continues, because it improves symptom control, quality of life, and goal-concordant decisions. Her bleeding, odynophagia, and weight loss are exactly the needs palliative '
                    'care addresses. Hospice is a separate end-of-life model with its own eligibility and goals.',
     'why_wrong': ['Correct.',
                   'Palliative care and hospice are different; she can receive palliative care without enrolling in hospice or stopping radiation.',
                   'Waiting until treatment ends withholds symptom and decision support during the period of highest burden and is contrary to guidance.',
                   'Code status is clarified after the broader goals discussion, and a DNR order is not a prerequisite for palliative care.'],
     'board_pearl': 'Palliative care is concurrent with cancer treatment; hospice is a separate eligibility and goals construct.',
     'curveball': 'During radiation she has a small sentinel bleed from the tumor bed near the carotid. How should urgent planning change?',
     'curveball_answer': 'Treat a sentinel bleed as a warning of carotid blowout. Admit for monitoring with large-bore access and crossmatched blood, protect the airway, and obtain urgent CT angiography '
                         'with interventional radiology consultation for possible stent or embolization if consistent with her goals. In parallel, revisit goals and document a plan for a massive bleed, '
                         'including comfort measures if she declines escalation.'},
    'v145_hn_13': {'stem': 'A 69-year-old man with incurable recurrent oropharyngeal SCC has severe throat pain, progressive dysphagia to liquids, and poor performance status (ECOG 3); he is no longer a candidate for '
             'further systemic therapy. His daughter asks that a gastrostomy tube be placed before discharge because he is not eating. He says he wants to be comfortable and at home. What is the best '
             'next step?',
     'choices': ['Place the gastrostomy tube before discharge, as his daughter has requested',
                 'Discuss goals, the expected benefit of a gastrostomy, and pain control',
                 'Begin parenteral nutrition through a PICC line before he goes home',
                 'Decline any feeding access because the disease cannot be cured'],
     'answer': 1,
     'explanation': "Feeding access should follow the patient's goals and a realistic estimate of benefit rather than serving as a default. With capacity intact, his priorities guide the decision. A "
                    'goals conversation explains what a gastrostomy can and cannot achieve at this stage, offers comfort feeding as an option, and pairs the decision with aggressive control of his pain, '
                    "which may itself be limiting intake. The family's concerns are acknowledged, not ignored.",
     'why_wrong': ['He has decision-making capacity, so a family request alone does not determine the plan without his informed preference.',
                   'Correct.',
                   'Parenteral nutrition adds line risk and burden with little benefit at ECOG 3 and does not match his comfort goals.',
                   'Feeding access may still be goal-concordant for some incurable patients; refusing to discuss it on that basis is wrong.'],
     'board_pearl': 'Tracheostomy and feeding tubes should match patient goals, not be placed by default in incurable disease.',
     'curveball': 'He decides against a gastrostomy and goes home. A week later he has a small episode of oral bleeding. What anticipatory planning should happen now?',
     'curveball_answer': 'Prepare for possible larger bleeding: confirm whether he wants hospital transfer, explain warning signs, supply dark towels, and arrange hospice with a crisis medication kit, '
                         'typically a rapid-acting benzodiazepine and opioid. Review code status, a portable medical order such as POLST, and caregiver instructions, and make sure the hospice team knows '
                         'the bleeding risk.'},
    'v145_hn_14': {'stem': 'A 74-year-old woman with terminal recurrent supraglottic SCC has increasing noisy breathing and dyspnea over 2 weeks. Laryngoscopy shows the airway narrowed to about 5 mm by tumor. She is '
             'lucid, has prognosis measured in weeks, and states firmly that she does not want a tracheostomy, intubation, or ICU care. Her son insists that everything be done. What should determine the '
             'airway plan?',
     'choices': ["Her son's wishes, because a tracheostomy could extend her life",
                 'Her informed refusal, with a dyspnea plan for the likely course',
                 'The degree of narrowing, which mandates an awake tracheostomy',
                 'A trial of elective intubation in the ICU until symptoms improve'],
     'answer': 1,
     'explanation': "A capacitated patient may refuse any intervention, including a lifesaving airway. The surgeon's role is to explain the likely trajectory, the option of tracheostomy and its burdens, "
                    "and what will happen without it, then build a goal-concordant plan for dyspnea and crisis. Tracheostomy is not automatically indicated because obstruction exists. The son's distress "
                    'is addressed through communication, not by overriding the patient.',
     'why_wrong': ["A family member cannot override a capacitated patient's informed refusal; surrogates decide only when capacity is absent.",
                   'Correct.',
                   'Airway narrowing defines risk but does not create an obligation to operate on a patient who has refused.',
                   'Intubation and ICU care are exactly what she declined, and an unplanned trial may be impossible to withdraw cleanly.'],
     'board_pearl': "Capacity is decision-specific; a capacitated patient's informed refusal of tracheostomy must be respected.",
     'curveball': 'She continues to decline an airway procedure. Which medications and bedside measures reduce distress as obstruction progresses?',
     'curveball_answer': 'Use low-dose opioids for dyspnea, a benzodiazepine for anxiety, and dexamethasone to reduce peritumoral edema; add humidified air or oxygen, upright positioning, and '
                         'glycopyrrolate for secretions. Prepare a crisis plan with rapid-acting sedation such as midazolam for terminal obstruction, and teach the family and nursing staff what to '
                         'expect.'},
    'v227_hn_goc_fnd': {'stem': 'A 58-year-old man with newly diagnosed stage IVA oral cavity SCC is scheduled for composite resection, free flap reconstruction, and adjuvant chemoradiation with curative intent. He has '
             'severe pain and depressed mood, and his surgeon requests a palliative care consult. He becomes upset and asks whether this means he is dying. Which statement is most accurate?',
     'choices': ['Palliative care is limited to patients with under 6 months to live',
                 'Palliative care is offered once curative treatment has failed',
                 'Palliative care is the same service as hospice under a new name',
                 'Palliative care can be given alongside treatment meant to cure'],
     'answer': 3,
     'explanation': 'Palliative care is specialized care for symptoms, distress, communication, and decision-making in serious illness, offered at any stage and alongside curative-intent therapy. His '
                    'severe pain and depression are appropriate reasons for referral during treatment planning. Hospice is a distinct model for comfort-focused end-of-life care with eligibility usually '
                    'tied to a limited prognosis. Explaining this difference helps patients accept early referral.',
     'why_wrong': ['A 6-month prognosis is a hospice eligibility concept, not a requirement for palliative care.',
                   'Palliative care does not wait for treatment failure; early integration improves symptoms and quality of life.',
                   'Hospice is a specific end-of-life model; palliative care is broader and can coexist with curative treatment.',
                   'Correct.'],
     'board_pearl': 'Palliative care is appropriate at any stage, including alongside curative-intent treatment; it is not hospice.',
     'curveball': 'Even when cure is no longer possible, which symptoms most often bring the otolaryngologist back to treat a palliative patient urgently?',
     'curveball_answer': 'Airway obstruction, tumor or vascular bleeding including sentinel carotid bleeds, uncontrolled pain, dysphagia with aspiration or dehydration, fungating wounds with odor or '
                         "infection, and loss of communication. Each can need an ENT procedure, such as tracheostomy, hemostasis, debulking, or feeding access, chosen according to the patient's goals."},
    'v227_hn_goc_app': {'stem': 'A 61-year-old woman with incurable recurrent hypopharyngeal SCC has episodic tumor bleeding, severe pain, and worsening stridor, with the airway narrowed to a slit on endoscopy. She '
             "declines further systemic therapy but wants to live long enough to attend her daughter's wedding in 2 months and accepts procedures that help her get there. Which plan best fits her goals?",
     'choices': ['Decline procedures because her disease cannot be cured',
                 'Advise salvage laryngopharyngectomy with free flap repair',
                 'Offer awake tracheostomy and palliative radiation for bleeding',
                 'Enroll in hospice now with opioids alone for her symptoms'],
     'answer': 2,
     'explanation': "A procedure can be appropriate in noncurative disease when it advances the patient's stated priorities. Tracheostomy addresses a threatened airway that could kill her before the "
                    'wedding, and short-course palliative radiation can reduce bleeding and pain, together with optimized analgesia. This is goal-concordant care: the interventions are chosen because '
                    'they meet her specific goal, with explicit discussion of burdens such as tracheostomy care and voice change.',
     'why_wrong': ['Incurability does not preclude procedures that relieve symptoms and help her achieve a defined, near-term goal.',
                   'Salvage laryngopharyngectomy is not curative in her recurrent disease and carries recovery time that conflicts with her goal.',
                   'Correct.',
                   'Comfort-only care leaves a reversible airway threat untreated despite her explicit wish to accept procedures to reach her goal.'],
     'board_pearl': "Noncurative disease does not preclude procedures; choose those that advance the patient's stated priorities.",
     'curveball': 'How does palliative radiation help her bleeding and pain, and what regimen is typical?',
     'curveball_answer': 'Radiation shrinks tumor and induces vascular thrombosis and fibrosis, which reduces oozing, mass effect, and nerve infiltration pain within days to weeks. Hypofractionated '
                         'courses are usual, such as a few large fractions over one to two weeks or the QUAD SHOT regimen. Prior radiation fields and total dose limit options, so reirradiation decisions '
                         'involve radiation oncology carefully.'},
    'v227_hn_goc_snr': {'stem': 'A 70-year-old man with terminal recurrent oral cavity SCC has an exposed carotid artery in a necrotic neck wound. This morning he had a 50 mL sentinel bleed that stopped with pressure. '
             'Last month he chose comfort-focused care, declining ICU admission, transfusion, and invasive procedures, and he reaffirms this today with intact capacity. What is the best response?',
     'choices': ['Arrange endovascular carotid occlusion to prevent a fatal hemorrhage',
                 'Transfer to the ICU for monitoring with blood products on standby',
                 'Avoid discussing a terminal bleed so the family is not frightened',
                 'Make a hemorrhage plan with crisis sedation and family preparation'],
     'answer': 3,
     'explanation': 'Goals-of-care planning is most valuable before predictable crises. He has capacity and has declined escalation, so the team honors that while preparing for a possible terminal '
                    'hemorrhage: dark towels and suction at the bedside, a rapid-acting sedative such as midazolam with an opioid ordered for immediate use, nursing guidance, and family preparation. '
                    'This keeps care calm and consistent with his goals.',
     'why_wrong': ['Endovascular occlusion is an invasive procedure he explicitly declined, despite its potential to prevent blowout.',
                   'ICU transfer and blood products directly conflict with his stated, capacitated refusal of escalation.',
                   'Failing to prepare the family leaves them unready for a frightening event that can be anticipated and planned for.',
                   'Correct.'],
     'board_pearl': 'Sentinel bleed in comfort care: plan for terminal hemorrhage with towels, crisis sedation, and prepared family.',
     'curveball': 'How would management differ if the same patient instead wanted every potentially life-prolonging intervention?',
     'curveball_answer': 'Treat it as an impending carotid blowout: admit with monitoring, large-bore access, and crossmatched blood, secure the airway if threatened, and obtain urgent CT angiography '
                         'with interventional radiology for covered stent or embolization, ideally after balloon test occlusion. Plan vascularized flap coverage of the wound if he can tolerate surgery.'},
    'v138_hn_01': {'stem': 'A 62-year-old woman has a 7-mm lesion on the left nasal ala that has bled intermittently for a year. It is a pearly papule with telangiectasias, but its edges blend into surrounding '
             'sun-damaged skin and are hard to define. Shave biopsy shows nodular basal cell carcinoma. She is healthy and wants the best chance of cure with the smallest possible defect. Which '
             'treatment is most appropriate?',
     'choices': ['Mohs micrographic surgery', 'Excision with 4-mm margins', 'Topical imiquimod cream', 'Primary radiation therapy'],
     'answer': 0,
     'explanation': 'The nasal ala is in the central-face H-zone, where BCC tracks along embryonic fusion planes and subclinical extension is common, and her ill-defined borders add risk. Mohs surgery '
                    'examines the entire peripheral and deep margin, giving the highest cure rate while removing the least normal tissue, which matters on the ala because of the nasal valve and cosmetic '
                    'subunit. Margin-controlled surgery is preferred for high-risk facial BCC.',
     'why_wrong': ['Correct.',
                   'Standard 4-mm margins suit low-risk well-defined BCC; at this H-zone site with ill-defined borders, conventional sampling misses subclinical extension.',
                   'Imiquimod is for selected superficial BCC on low-risk sites and has lower cure rates than surgery for nodular disease.',
                   'Radiation is reserved for patients who are poor surgical candidates and offers lower cure without margin assessment in a healthy patient.'],
     'board_pearl': 'H-zone, ill-defined, recurrent or aggressive-histology BCC: Mohs gives the highest cure with maximal tissue sparing.',
     'curveball': 'At follow-up she reports new formication and numbness of the upper lip and cheek. How does this change staging and imaging?',
     'curveball_answer': 'Paresthesia in the infraorbital distribution suggests perineural invasion along V2, making this high-risk disease. Obtain MRI with gadolinium and fat suppression of the named '
                         'nerve to the skull base to map extent. Clinical perineural spread requires resection to clear margins where feasible and usually adjuvant radiation covering the nerve pathway, '
                         'through multidisciplinary planning.'},
    'v145_hn_01': {'stem': 'A 67-year-old man has a 1.8-cm ulcerated plaque on the right nasal ala with poorly defined margins. Biopsy shows infiltrative basal cell carcinoma. There is no numbness, the nasal lining '
             'looks intact on anterior rhinoscopy, and the neck is clinically negative. He asks whether the cancer can be removed and the nose rebuilt in the same sitting. Which plan is most '
             'appropriate?',
     'choices': ['Wide excision with 4-mm margins and an immediate forehead flap',
                 'Excision with frozen-section spot checks and immediate full-thickness skin grafting',
                 'Margin-controlled excision first, then reconstruction of the final cleared defect',
                 'Vismodegib to shrink the tumor before excision with nasolabial flap closure'],
     'answer': 2,
     'explanation': 'Infiltrative histology on the ala grows in thin strands well beyond visible margins. Margin-controlled excision, such as Mohs or staged complete-margin assessment, clears the tumor '
                    'first; reconstruction is then planned for the true final defect. Immediate flap reconstruction after conventional excision risks burying positive margins under tissue that must '
                    'later be taken down. Nodal staging is not needed, because metastasis from BCC is rare.',
     'why_wrong': ['Conventional 4-mm margins are often inadequate for infiltrative BCC, and an immediate flap hides any residual tumor.',
                   'Spot frozen sections sample only a small fraction of the margin and miss the strands typical of infiltrative growth.',
                   'Correct.',
                   'Hedgehog inhibitors are for locally advanced or unresectable BCC, not a resectable alar lesion amenable to surgery.'],
     'board_pearl': 'For high-risk facial BCC, clear the margins first, then reconstruct the final defect.',
     'curveball': 'After clearance, the defect crosses the alar rim and includes vestibular lining. Which reconstructive layers must be restored?',
     'curveball_answer': 'All three: internal lining, for example with a septal mucoperichondrial or turnover flap, or the lining of a folded forehead flap; structural support, typically an alar batten '
                         'or rim graft of conchal or septal cartilage to resist valve collapse and notching; and external skin coverage, such as a paramedian forehead flap or nasolabial flap that '
                         'respects the alar subunit.'},
    'v223_hn_bcc_fnd': {'stem': 'A 74-year-old retired farmer has a 1.5-cm nodular basal cell carcinoma of the left cheek confirmed on biopsy. Last year he had a cutaneous SCC of the scalp treated with excision and '
             'parotid ultrasound surveillance. He asks whether he now needs a neck CT and sentinel node biopsy as he had discussed before. There are no palpable nodes. Which statement best guides your '
             'answer?',
     'choices': ['BCC metastasizes to parotid nodes as often as cutaneous SCC does',
                 'BCC is locally destructive, but nodal or distant spread is rare',
                 'BCC needs sentinel node biopsy when the lesion exceeds 1 cm',
                 'BCC staging requires a neck CT before any facial excision'],
     'answer': 1,
     'explanation': 'BCC arises from basal keratinocytes that depend on their specific stroma, which helps explain its very low metastatic rate. Its morbidity comes from relentless local invasion, '
                    'recurrence, and destruction of critical facial structures rather than regional or distant spread. Routine BCC needs no nodal imaging or sentinel biopsy, unlike high-risk cutaneous '
                    'SCC, where parotid and neck metastasis is a real concern. Imaging is reserved for suspected deep or perineural extension.',
     'why_wrong': ['Cutaneous SCC metastasizes to parotid and neck nodes far more often than BCC, which rarely spreads.',
                   'Correct.',
                   'Sentinel node biopsy is used in melanoma, Merkel cell carcinoma, and selected cSCC, not routine BCC regardless of size.',
                   'Routine BCC needs no systemic staging; CT or MRI is reserved for suspected bone, orbit, or named-nerve involvement.'],
     'board_pearl': 'BCC threatens by local destruction, not metastasis; routine nodal staging is not indicated.',
     'curveball': 'Which histologic subtypes or clinical settings make recurrence of his cheek BCC more likely?',
     'curveball_answer': 'Infiltrative, morpheaform (sclerosing), micronodular, and basosquamous histology, perineural invasion, poorly defined borders, prior recurrence, H-zone location, larger size, '
                         'prior radiation at the site, and immunosuppression. These features favor margin-controlled surgery such as Mohs and, for perineural or residual disease, consideration of '
                         'adjuvant radiation.'},
    'v223_hn_bcc_app': {'stem': 'A 69-year-old woman underwent Mohs surgery for a third recurrence of infiltrative basal cell carcinoma of the left nasal ala. Margins are now clear in three stages. The defect is 1.6 cm, '
             'involves the whole alar subunit, includes most of the lateral crus, and exposes a 1-cm defect in the vestibular lining. She smokes 5 cigarettes a day. Which reconstruction is most '
             'appropriate?',
     'choices': ['Full-thickness skin graft from the preauricular region',
                 'Healing by secondary intention with nasal packing',
                 'Split-thickness skin graft over the cartilage and lining',
                 'Lining flap, cartilage graft, and staged forehead flap'],
     'answer': 3,
     'explanation': 'Once oncologic clearance is confirmed, the reconstruction must replace each missing layer. This full-thickness alar defect lacks lining, structural support, and skin. Lining can '
                    'come from local mucosal or turnover flaps, support from a conchal or septal cartilage graft to prevent valve collapse and notching, and skin cover from a paramedian forehead flap '
                    'for a full alar subunit. Smoking increases flap risk and should be stopped.',
     'why_wrong': ['A skin graft alone cannot survive over a lining defect and provides no support against alar collapse.',
                   'Secondary healing of a full-thickness alar defect causes severe retraction, notching, and nasal valve collapse.',
                   'A split-thickness graft provides neither lining nor support and contracts heavily on the mobile ala.',
                   'Correct.'],
     'board_pearl': 'Full-thickness nasal defects need all three layers rebuilt: lining, cartilage support, and skin coverage.',
     'curveball': 'In a different patient, the cleared alar defect is only 8 mm, superficial, and spares cartilage and lining. Would you still need a forehead flap or cartilage graft?',
     'curveball_answer': 'Usually not. A small superficial alar defect can be closed with a full-thickness skin graft or a local flap such as a bilobed or nasolabial flap. A forehead flap becomes '
                         'necessary for large or subunit-sized defects, and a cartilage graft is needed when the defect removes support or when closure risks alar retraction or valve collapse, even '
                         'without cartilage removal.'},
    'v223_hn_bcc_snr': {'stem': 'A 76-year-old man has a fourth recurrence of basal cell carcinoma at the right medial canthus after three excisions. He now has epiphora, mild proptosis, and diplopia on lateral gaze. '
             'Visual acuity is 20/30. The plastic surgeon offers another excision under local anesthesia. CT shows soft tissue thickening extending into the medial orbit. What is the most appropriate '
             'next step?',
     'choices': ['Repeat excision under local anesthesia with Mohs margin checks',
                 'Start a Hedgehog inhibitor before any further imaging or review',
                 'Gadolinium MRI and multidisciplinary review of all treatment options',
                 'Definitive radiation to the medial canthus as the sole treatment'],
     'answer': 2,
     'explanation': 'Proptosis and diplopia indicate likely orbital invasion by multiply recurrent BCC. Before choosing treatment, define the true extent with contrast MRI, which shows orbital fat, '
                    'muscle, lacrimal, and perineural involvement better than CT. A multidisciplinary team, including oculoplastic and skull base surgery, radiation oncology, and medical oncology, then '
                    'weighs orbital exenteration, radiation, and Hedgehog-pathway inhibitors against vision and patient goals.',
     'why_wrong': ['Office excision cannot clear orbital disease, and repeated shaving of a positive deep margin drives further recurrence.',
                   'Hedgehog inhibitors are an option, but committing to one before defining extent and resectability is premature.',
                   'Correct.',
                   'Radiation may be part of treatment, but choosing it before mapping orbital extent and reviewing surgery is premature.'],
     'board_pearl': 'Locally advanced periocular BCC: define extent with MRI, then decide surgery, radiation or Hedgehog inhibitor in tumor board.',
     'curveball': 'Which clinical or imaging findings would bring orbital exenteration into the surgical discussion for him?',
     'curveball_answer': 'Invasion of orbital fat beyond the periorbita, extraocular muscle, the globe, or the lacrimal sac and duct with deep extension, especially with fixed proptosis, restricted '
                         'motility, or vision loss, when clear margins cannot be obtained with eye-sparing resection. Exenteration is weighed against eye-sparing options such as Hedgehog inhibitors or '
                         "radiation, the status of the other eye, and the patient's goals."},
    'v138_hn_02': {'stem': 'A 49-year-old man who never smoked has a 3-month history of a painless, enlarging right neck mass. Exam shows a 3.5-cm cystic level IIA node, and flexible laryngoscopy shows a 2-cm '
             'exophytic lesion of the right base of tongue. Biopsy confirms nonkeratinizing squamous cell carcinoma. Before staging is assigned, which tumor characteristic must be determined?',
     'choices': ['Depth of invasion measured on the biopsy', 'Serum squamous cell carcinoma antigen', 'p16 immunohistochemistry on the tumor', 'EBV-encoded RNA in situ hybridization'],
     'answer': 2,
     'explanation': 'Oropharyngeal SCC is staged by separate AJCC systems for HPV-associated and HPV-negative disease, and p16 immunohistochemistry is the standard surrogate for HPV-mediated tumors. A '
                    'nonsmoker with a cystic node and nonkeratinizing histology is the classic HPV phenotype, which carries much better survival and a different nodal classification. Version 9 now '
                    'governs HPV-associated oropharynx staging. HPV-specific testing may be added when p16 is equivocal.',
     'why_wrong': ['Depth of invasion modifies T stage for oral cavity cancer, not for base-of-tongue cancer, which is oropharyngeal.',
                   'Serum SCC antigen is not part of staging and has no role in classifying oropharyngeal cancer.',
                   'Correct.',
                   'EBER testing identifies EBV-associated nasopharyngeal carcinoma; it is used for unknown primaries, not to stage a known oropharyngeal primary.'],
     'board_pearl': 'Every oropharyngeal SCC needs p16 status because HPV-associated disease has its own staging and better prognosis.',
     'curveball': 'He is p16-positive, T2N1. Which features would make transoral robotic surgery versus definitive chemoradiation reasonable choices?',
     'curveball_answer': 'TORS with neck dissection is reasonable when there is good transoral exposure, a resection that spares enough tongue base for swallowing, and a low likelihood of ENE or '
                         'positive margins that would mandate adjuvant chemoradiation. Definitive radiation-based treatment is favored when adjuvant therapy is very likely, exposure is poor, or '
                         'resection would compromise swallowing. Survival is similar, so expected function guides choice.'},
    'v145_hn_02': {'stem': 'A 55-year-old man has p16-positive SCC of the left base of tongue measuring 1.5 cm, easily exposed transorally. CT shows three left level II and III nodes, the largest 4 cm, with irregular '
             'margins and infiltration of adjacent fat suggesting extranodal extension. He wants the option with the best swallowing outcome. Which consideration should most influence the choice between '
             'TORS and definitive chemoradiation?',
     'choices': ['The small primary size, which favors TORS whatever the neck findings',
                 'The easy transoral exposure, which makes TORS the default strategy',
                 'The p16 status, which allows a de-escalated radiation dose by protocol',
                 'The likelihood that surgery would still require adjuvant chemoradiation'],
     'answer': 3,
     'explanation': 'Treatment selection integrates HPV status, stage, functional outcome, and expected adjuvant burden. Although his primary is small and accessible, multiple nodes with radiographic '
                    'extranodal extension make adjuvant chemoradiation after TORS very likely. Surgery would then add morbidity to full-dose chemoradiation, a trimodality outcome with worse swallowing. '
                    'Definitive chemoradiation is often favored in that situation, while TORS fits patients likely to avoid or reduce adjuvant therapy.',
     'why_wrong': ['Primary size is only one factor; his nodal burden drives the likelihood of adjuvant chemoradiation regardless of T stage.',
                   'Technical access does not establish candidacy when the overall treatment package would be more morbid.',
                   'De-escalation for p16-positive disease remains investigational and should not drive standard treatment selection outside a trial.',
                   'Correct.'],
     'board_pearl': 'Avoid trimodality by accident: if TORS will likely need adjuvant chemoradiation, consider definitive chemoradiation.',
     'curveball': 'He chooses TORS, and final pathology confirms extranodal extension in one node with clear primary margins. How does that alter adjuvant therapy?',
     'curveball_answer': 'Extranodal extension is a high-risk pathologic feature, along with positive margins, so postoperative radiation with concurrent high-dose cisplatin is recommended rather than '
                         'radiation alone. The benefit of adding chemotherapy is greatest for ENE and positive margins. De-escalated adjuvant regimens for HPV-positive disease remain trial-based.'},
    'v220_hn_bot_snr': {'stem': 'A 60-year-old woman has p16-positive SCC of the base of tongue crossing midline, with bilateral level II and III nodes, one showing matted nodes. Endoscopy suggests transoral access would '
             'be adequate, but clearing margins would remove more than half the tongue base. She has mild baseline dysphagia, is a former smoker, and values eating by mouth. Which treatment is most '
             'appropriate?',
     'choices': ['TORS with bilateral neck dissection, then adjuvant chemoradiation',
                 'Total glossectomy with laryngeal preservation and flap reconstruction',
                 'TORS with bilateral neck dissection and no planned adjuvant therapy',
                 'Definitive chemoradiation with prophylactic swallowing therapy'],
     'answer': 3,
     'explanation': 'Transoral access is only one part of surgical candidacy. Resecting more than half the tongue base would cripple bolus propulsion, and bilateral matted nodes make adjuvant '
                    'chemoradiation nearly certain, so surgery would add morbidity without removing the need for chemoradiation. Survival outcomes are similar between approaches in oropharyngeal cancer, '
                    'so definitive chemoradiation with swallowing rehabilitation offers the better functional value for a patient prioritizing oral intake.',
     'why_wrong': ['This creates trimodality treatment with extensive tongue-base loss plus full chemoradiation, maximizing dysphagia without survival gain.',
                   'Total glossectomy is far more morbid than needed and is not a standard first-line option for this tumor.',
                   'Bilateral matted nodes predict ENE and other adverse features, so omitting adjuvant therapy is not realistic.',
                   'Correct.'],
     'board_pearl': 'The base-of-tongue question is not whether you can remove it, but whether surgery spares or merely adds to chemoradiation.',
     'curveball': 'Which pretreatment swallowing and nutrition factors should enter her shared decision-making?',
     'curveball_answer': 'Baseline instrumental swallowing evaluation such as FEES or modified barium swallow, aspiration and pulmonary reserve, weight loss and nutritional status, dentition needing '
                         'extraction before radiation, expected feeding-tube need, ability to engage in prophylactic swallowing exercises, and social support. Baseline dysphagia and aspiration predict '
                         'long-term tube dependence after either surgery or chemoradiation.'},
    'v138_hn_03': {'stem': 'A 44-year-old woman has a painless left upper neck mass slowly enlarging over 2 years. It is pulsatile and moves side to side but not vertically. Cranial nerve exam is normal. Contrast CT '
             'shows a 3.2-cm avidly enhancing mass at the carotid bifurcation splaying the internal and external carotid arteries. A colleague suggests a core biopsy. What is the most appropriate next '
             'step?',
     'choices': ['Plasma metanephrines, nerve assessment and angiographic mapping',
                 'Ultrasound-guided core needle biopsy to confirm the diagnosis',
                 'Open incisional biopsy in the operating room under anesthesia',
                 'Excision through a neck dissection approach without further testing'],
     'answer': 0,
     'explanation': 'Splaying of the carotid bifurcation by an avidly enhancing mass is diagnostic of carotid body paraganglioma, and biopsy adds hemorrhage risk without changing management. The next '
                    'step is a treatment-planning workup: biochemical screening for catecholamine secretion, documentation of vagal, hypoglossal, and sympathetic function including laryngoscopy, and CTA '
                    'or MRA to grade the Shamblin relationship. Genetic counseling should also be offered. Management then ranges from observation to radiation or surgery.',
     'why_wrong': ['Correct.',
                   'Needle biopsy of a hypervascular paraganglioma risks bleeding and rarely changes management in a radiographically classic case.',
                   'Open biopsy carries major hemorrhage risk and is unnecessary when imaging is characteristic.',
                   'Proceeding without biochemical screening risks an unprepared catecholamine crisis, and Shamblin grading is needed to plan vascular control.'],
     'board_pearl': 'Classic carotid body tumor on imaging: no biopsy; screen metanephrines, document cranial nerves, and grade Shamblin class.',
     'curveball': 'Which family or personal history should prompt genetic evaluation in this patient?',
     'curveball_answer': 'Any relative with paraganglioma or pheochromocytoma, bilateral or multifocal tumors, age under about 40 to 50, a secreting tumor, prior pheochromocytoma, renal cell carcinoma, '
                         'or GIST. Many experts now offer germline testing to all paraganglioma patients because SDHx mutations are common; SDHD and SDHAF2 show paternal transmission, so a negative '
                         'maternal history does not exclude risk.'},
    'v145_hn_03': {'stem': 'An 81-year-old man with heart failure (ejection fraction 25%) and COPD on home oxygen was found to have a 2.1-cm right carotid body paraganglioma on CT done for chest pain 3 years ago. MRI '
             'today shows the tumor unchanged in size. He is asymptomatic, has normal cranial nerve function, and plasma metanephrines are normal. What is the most appropriate management?',
     'choices': ['Surgical excision after preoperative embolization',
                 'Stereotactic radiation therapy as soon as it can be scheduled',
                 'Ultrasound-guided core biopsy to exclude malignancy',
                 'Observation with periodic MRI and nerve examination'],
     'answer': 3,
     'explanation': 'Carotid body paragangliomas usually grow slowly, are rarely malignant, and are managed individually according to age, growth, symptoms, genetics, Shamblin anatomy, and comorbidity. '
                    'An elderly, high-risk patient with a small, stable, nonsecreting, asymptomatic tumor is best served by observation with serial imaging. Surgery carries risks of cranial nerve injury '
                    'and stroke that outweigh benefit here, and radiation is reserved for growth or symptoms.',
     'why_wrong': ['Surgery risks lower cranial nerve injury and stroke in a frail patient whose small tumor has been stable for 3 years.',
                   'Radiation is an option if the tumor grows or causes symptoms, but a stable asymptomatic tumor does not need treatment now.',
                   'Imaging is diagnostic, and biopsy of this hypervascular tumor adds bleeding risk without changing management.',
                   'Correct.'],
     'board_pearl': 'Small, stable, asymptomatic carotid body tumor in an older high-risk patient: observe with serial imaging.',
     'curveball': 'In a healthy 45-year-old, the tumor is a 5-cm Shamblin III lesion encasing the internal carotid. Which preoperative issue becomes more important?',
     'curveball_answer': 'Planning for possible carotid resection or reconstruction. Involve vascular surgery, assess collateral cerebral circulation, and consider balloon test occlusion of the internal '
                         'carotid. Counsel about stroke risk and the high likelihood of vagal, hypoglossal, and sympathetic injury, and arrange for an interposition graft. Preoperative embolization may '
                         'be considered to reduce blood loss.'},
    'v222_hn_cbp_fnd': {'stem': 'A 52-year-old woman has a painless right neck mass noticed 2 years ago. It sits deep to the anterior border of the sternocleidomastoid at the level of the hyoid and moves laterally but not '
             'vertically; a bruit is present. Cranial nerves are intact. CTA shows a 3-cm intensely enhancing mass widening the angle between the internal and external carotid arteries. What is the most '
             'likely diagnosis?',
     'choices': ['Vagal schwannoma of the poststyloid parapharyngeal space',
                 'Carotid body paraganglioma at the bifurcation',
                 'Second branchial cleft cyst near the carotid',
                 'Metastatic papillary thyroid carcinoma node'],
     'answer': 1,
     'explanation': 'A pulsatile, laterally mobile but vertically fixed mass with a bruit, intense enhancement, and splaying of the internal and external carotid arteries, the lyre sign, is '
                    'characteristic of carotid body paraganglioma arising in the adventitia of the bifurcation. The carotid body is among the most highly perfused tissues in the body, explaining the '
                    'avid enhancement and flow voids on MRI.',
     'why_wrong': ['Vagal tumors arise above the bifurcation and push the internal carotid anteromedially without splaying the internal and external arteries.',
                   'Correct.',
                   'Branchial cleft cysts are nonenhancing cystic masses that displace, rather than splay, the carotid vessels.',
                   'Nodal metastases lie lateral to the carotid sheath and do not enhance intensely or widen the carotid bifurcation.'],
     'board_pearl': 'Splaying of internal and external carotids with avid enhancement equals carotid body paraganglioma.',
     'curveball': 'Which additional history would raise concern for a hereditary paraganglioma syndrome in this patient?',
     'curveball_answer': 'A family history of paraganglioma or pheochromocytoma, bilateral or multifocal tumors, young age at onset, prior pheochromocytoma, catecholamine secretion, or associated tumors '
                         'such as renal cell carcinoma or GIST. Paternal family history is especially relevant for SDHD. Positive findings warrant genetic testing and whole-body imaging.'},
    'v222_hn_cbp_app': {'stem': "A 34-year-old man has bilateral carotid body tumors on MRI, 2.5 cm on the left and 1.8 cm on the right. His father had a 'neck tumor' removed and his paternal aunt had a pheochromocytoma. "
             'Cranial nerves are intact bilaterally. He asks whether both tumors can be removed in one operation. What is the most appropriate next step before treatment planning?',
     'choices': ['Simultaneous bilateral excision under one anesthetic',
                 'Staged excision beginning with the larger left tumor',
                 'Germline testing, metanephrines, and whole-body imaging',
                 'Bilateral fractionated radiation to both carotid body tumors'],
     'answer': 2,
     'explanation': 'Young age, bilateral tumors, and a paternal family history of paraganglioma and pheochromocytoma strongly suggest a hereditary syndrome, most likely SDHD with paternal transmission. '
                    'Before committing to intervention, obtain germline testing, biochemical screening, and whole-body functional imaging such as DOTATATE PET to detect other paragangliomas or a '
                    'pheochromocytoma. This changes sequencing, surveillance, and the decision about which tumor, if any, to treat.',
     'why_wrong': ['Bilateral simultaneous resection risks bilateral vagal and hypoglossal palsy and baroreflex failure, and bypasses evaluation for other tumors.',
                   'Staged surgery may eventually be part of care, but treatment should not begin before syndromic evaluation and a full tumor survey.',
                   'Correct.',
                   'Radiation may be used for one side, but treating both before syndromic workup and staging is premature.'],
     'board_pearl': 'Bilateral or familial paraganglioma: germline testing, biochemistry and whole-body imaging before planning treatment.',
     'curveball': 'After resection of the left tumor he develops a left vocal fold paralysis. How does that change treatment of the right tumor?',
     'curveball_answer': 'Now the right tumor should be observed or treated with radiation rather than resected, because surgery that injures the right vagus would cause bilateral vocal fold paralysis '
                         'with airway compromise and severe aspiration. Bilateral carotid body resection also risks baroreflex failure with labile blood pressure. Surgery is reconsidered only if the '
                         'tumor grows despite radiation.'},
    'v222_hn_cbp_snr': {'stem': 'A 58-year-old woman has a 5.5-cm left carotid body paraganglioma that encases the internal carotid and extends to the skull base; it grew 6 mm over the past year. She had a right vagal '
             'schwannoma resected years ago and has a paralyzed right vocal fold with mild aspiration of thin liquids. Metanephrines are normal. Which management is most appropriate?',
     'choices': ['Resection with planned internal carotid reconstruction',
                 'Open biopsy to confirm the diagnosis before deciding',
                 'Radiation therapy to the tumor for long-term control',
                 'Resection after preoperative tumor embolization'],
     'answer': 2,
     'explanation': 'This tumor is growing, so treatment is reasonable, but resection of a large skull-base-extending Shamblin III lesion carries a high chance of left vagal injury. With a paralyzed '
                    'right vocal fold, that would produce bilateral paralysis, airway compromise, and severe aspiration. Radiation offers high long-term control with far less cranial nerve morbidity. A '
                    'technically resectable tumor is not automatically the right one to remove when the functional cost is catastrophic.',
     'why_wrong': ['Resection with carotid reconstruction is technically feasible but carries high left vagal risk, producing bilateral paralysis.',
                   'Imaging is diagnostic for paraganglioma, and biopsy adds bleeding risk without changing management.',
                   'Correct.',
                   'Embolization lowers blood loss but does not reduce the risk of vagal injury that makes surgery so hazardous here.'],
     'board_pearl': 'When surgery risks bilateral vagal palsy, radiation or observation is preferred for carotid body tumors.',
     'curveball': 'If she were a surgical candidate, when might preoperative embolization be considered and what risks must be discussed?',
     'curveball_answer': 'Embolization is considered for large Shamblin II or III tumors to reduce blood loss, usually 24 to 72 hours before surgery. Risks include stroke from reflux of particles into '
                         'the internal carotid or its branches, cranial nerve ischemia, and inflammation that can make subadventitial dissection planes harder. Many surgeons use it selectively rather '
                         'than routinely.'},
    'v138_hn_05': {'stem': 'A 45-year-old man has an irregular 7-mm pigmented papule on the scalp excised with narrow margins. Pathology reports superficial spreading melanoma, measured tumor depth 0.9 mm, Clark '
             'level IV, no ulceration, mitotic rate 3 per mm2, and focal regression, with clear margins. No nodes are palpable. Which reported feature most directly drives his T category and the '
             'sentinel node discussion?',
     'choices': ['Breslow thickness', 'Clark level of invasion', 'Mitotic rate per mm2', 'Focal tumor regression'],
     'answer': 0,
     'explanation': 'In AJCC 8th edition, T category is defined by Breslow thickness and ulceration. A 0.9-mm tumor is T1b even without ulceration, because T1a is limited to tumors under 0.8 mm without '
                    'ulceration. Sentinel node biopsy is discussed for clinically node-negative melanoma at least 0.8 mm thick or with other high-risk features. Clark level and mitotic rate were removed '
                    'from T staging, although they still inform prognosis.',
     'why_wrong': ['Correct.',
                   'Clark level was dropped from AJCC T classification because Breslow thickness is more reproducible and prognostic.',
                   'Mitotic rate was removed from T1 subcategorization in AJCC 8th edition, although it remains a prognostic factor.',
                   'Regression is reported but does not define T category or the threshold for sentinel node biopsy.'],
     'board_pearl': 'Melanoma T stage is Breslow plus ulceration; at 0.8 mm or more, discuss sentinel node biopsy.',
     'curveball': 'He has sentinel node biopsy, and one node shows a 0.3-mm deposit. How does this change regional management?',
     'curveball_answer': 'It upstages him to stage III but does not mandate completion lymph node dissection. MSLT-II and DeCOG-SLT showed no melanoma-specific survival benefit, so nodal-basin '
                         'ultrasound surveillance is standard after multidisciplinary review. Adjuvant anti-PD-1 therapy is discussed for resected stage III disease, and BRAF testing adds a BRAF/MEK '
                         'option when V600-mutant.'},
    'v143_hno_04': {'stem': 'A 58-year-old woman has a 1.6-mm nonulcerated melanoma of the left temple, diagnosed on excisional biopsy with clear narrow margins. She has no palpable parotid or neck nodes, and '
             'ultrasound of the parotid and neck is normal. She asks whether the surgeon will simply remove her parotid and neck nodes at the time of wide excision. What is the most appropriate regional '
             'management?',
     'choices': ['Elective superficial parotidectomy with neck dissection',
                 'Wide excision alone with clinical surveillance of the neck',
                 'Elective neck dissection of levels II to V at wide excision',
                 'Lymphoscintigraphy-guided sentinel node biopsy at wide excision'],
     'answer': 3,
     'explanation': 'A clinically node-negative melanoma thicker than 0.8 mm meets the threshold for sentinel node biopsy, which provides accurate pathologic staging and guides adjuvant therapy. Head '
                    'and neck lymphatic drainage is unpredictable, can involve parotid, preauricular, postauricular, occipital, or contralateral basins, and often differs from clinical prediction, so '
                    'preoperative lymphoscintigraphy with SPECT/CT maps the true sentinel nodes. Elective dissection adds morbidity without survival benefit.',
     'why_wrong': ['Elective parotidectomy and neck dissection risk facial nerve injury and add morbidity without a survival benefit over sentinel biopsy.',
                   'At 1.6 mm, omitting nodal staging forgoes prognostic information needed for adjuvant therapy decisions.',
                   'Elective dissection may miss aberrant drainage to parotid or contralateral basins and adds morbidity without proven benefit.',
                   'Correct.'],
     'board_pearl': 'Head and neck melanoma drainage is unpredictable: map with lymphoscintigraphy before sentinel node biopsy.',
     'curveball': 'The mapped sentinel node lies within the parotid and is positive. How does that change multidisciplinary regional management?',
     'curveball_answer': 'It establishes stage III disease and triggers adjuvant systemic therapy discussion, typically anti-PD-1 or BRAF/MEK inhibition if V600-mutant. Completion parotidectomy and neck '
                         'dissection is not mandatory; ultrasound surveillance of the parotid and neck is an accepted alternative after multidisciplinary review. Any later clinically evident node is '
                         'treated with therapeutic dissection and facial nerve preservation.'},
    'v223_hn_mel_fnd': {'stem': 'A 63-year-old man has a changing 9-mm pigmented papule on the right cheek. His primary care physician performed a superficial shave biopsy. Pathology shows invasive melanoma with no '
             'ulceration, but tumor cells extend to the deep margin of the specimen, measuring at least 0.6 mm. No nodes are palpable. Which staging variable is compromised and must be clarified before '
             'definitive planning?',
     'choices': ['Ulceration status of the primary melanoma', 'Breslow thickness of the primary tumor', 'Clark level of invasion of the primary', 'Mitotic rate per square millimeter'],
     'answer': 1,
     'explanation': 'Breslow thickness is the central variable in melanoma T staging, excision margins, and the decision to offer sentinel node biopsy. A transected deep margin means the true thickness '
                    'is unknown and may exceed 0.8 or 1 mm, the thresholds for sentinel biopsy and wider margins. The residual lesion should be sampled deeply to establish true thickness. The first '
                    'biopsy should be deep enough to measure Breslow depth accurately.',
     'why_wrong': ['Ulceration is assessed at the epidermal surface and is not lost when the deep margin is transected.',
                   'Correct.',
                   'Clark level is no longer used for AJCC T staging and is not the variable that drives management here.',
                   'Mitotic rate is prognostic but not used for T staging, and it does not determine margins or sentinel biopsy thresholds.'],
     'board_pearl': 'Biopsy suspected melanoma deeply enough to measure Breslow thickness; a transected base leaves stage unknown.',
     'curveball': 'Deeper sampling shows a 0.7-mm melanoma with ulceration. How does ulceration modify his stage and management?',
     'curveball_answer': 'Ulceration upgrades a melanoma under 0.8 mm from T1a to T1b, worsens prognosis at every thickness, and lowers the threshold for sentinel node biopsy, which should now be '
                         'discussed. In thicker tumors, ulceration moves the T subcategory from a to b, and T3b or T4b disease without nodes is stage IIB or IIC, where adjuvant anti-PD-1 is an option.'},
    'v223_hn_mel_snr': {'stem': 'A 60-year-old man had a 2.4-mm ulcerated scalp melanoma excised with 2-cm margins. Lymphoscintigraphy mapped a single sentinel node in the right parotid, removed through a limited approach '
             'with facial nerve monitoring; it contains a 1.2-mm deposit without extranodal extension. Neck ultrasound is normal. The resident proposes a completion parotidectomy and neck dissection. '
             'What is the most appropriate plan?',
     'choices': ['Completion parotidectomy and neck dissection in every such case',
                 'Parotid bed radiation with observation of the neck',
                 'Nodal ultrasound surveillance with adjuvant anti-PD-1 therapy',
                 'Observation alone, because parotid deposits are not staged'],
     'answer': 2,
     'explanation': 'A positive sentinel node establishes stage III disease, prompting systemic staging and multidisciplinary discussion. Randomized trials showed that immediate completion dissection '
                    'does not improve melanoma-specific survival, so nodal-basin ultrasound surveillance is an accepted alternative and avoids facial nerve risk. Adjuvant anti-PD-1 therapy is standard '
                    'for resected stage III disease, with BRAF/MEK inhibition an option for V600 mutations. Completion surgery remains reasonable in selected patients who cannot comply with '
                    'surveillance.',
     'why_wrong': ['Completion dissection improves regional control but not survival and adds facial nerve risk, so it is no longer mandatory.',
                   'Adjuvant radiation to the parotid bed is reserved for selected high-risk nodal disease and does not replace systemic therapy.',
                   'Correct.',
                   'Intraparotid nodes are regional nodes; a positive one defines stage III and warrants adjuvant therapy discussion.'],
     'board_pearl': 'Positive sentinel node in melanoma: stage III, surveillance ultrasound instead of mandatory completion dissection, consider adjuvant anti-PD-1.',
     'curveball': 'Once regional nodal disease is identified, what additional imaging or systemic staging is appropriate?',
     'curveball_answer': 'Baseline cross-sectional staging is reasonable for stage III disease, typically CT of chest, abdomen, and pelvis or whole-body PET/CT, with brain MRI to exclude occult '
                         'metastases before adjuvant therapy. Send the tumor for BRAF V600 mutation testing. Serum LDH is obtained because it carries prognostic value in stage IV disease.'},
    'v138_hn_06': {'stem': 'A 57-year-old dentate man has a 2-cm SCC of the left anterolateral floor of mouth whose edge lies 4 mm from the lingual gingiva. Bimanual exam shows the lesion is mobile over the mandible '
             'without fixation, and lower-lip sensation is normal. CT shows no cortical erosion, and the neck is clinically negative. Which approach to the mandible is most appropriate?',
     'choices': ['Mandible-sparing excision, adding rim resection only if periosteum is involved',
                 'Segmental mandibulectomy, because tumor within 1 cm of bone predicts bone invasion',
                 'Marginal mandibulectomy in every case, regardless of the operative findings',
                 'Definitive radiation, so that any surgery on the mandible is avoided entirely'],
     'answer': 0,
     'explanation': 'Mandible proximity is not mandibular invasion. A mobile lesion without fixation, normal mental nerve function, and no cortical erosion has not invaded bone, so the mandible can be '
                    'preserved, using the periosteum or a marginal rim of alveolus as the deep margin only if the tumor proves adherent at surgery. Segmental resection is reserved for true medullary '
                    'invasion or when inadequate bone height prevents a safe marginal resection.',
     'why_wrong': ['Correct.',
                   'Proximity without fixation or cortical erosion does not imply bone invasion; segmental resection adds major morbidity without oncologic benefit.',
                   'Routine rim resection removes bone that may be unnecessary when the tumor separates cleanly from the periosteum.',
                   'Surgery is the primary treatment for oral cavity SCC, and radiation to the mandible adds osteoradionecrosis risk.'],
     'board_pearl': 'Proximity is not invasion: match mandibular resection to true bone involvement, not closeness.',
     'curveball': 'The same patient instead has a 2.5-cm left level IB node with suspected extranodal extension. How does this change neck management?',
     'curveball_answer': 'The neck now needs therapeutic rather than elective treatment: an ipsilateral neck dissection including levels I to III or broader, with contralateral dissection considered for '
                         'an anterior or midline primary. Radiographic ENE predicts adjuvant chemoradiation if confirmed on pathology, so plan reconstruction and dental evaluation with that in mind.'},
    'v145_hn_05': {'stem': 'A 62-year-old woman has a biopsy-proven SCC of the right floor of mouth. On inspection it measures 1.8 cm, but palpation shows submucosal induration extending posteriorly toward the '
             'tongue, and MRI shows tumor depth of 9 mm with extension toward the genioglossus. The neck is clinically negative and the mandible is mobile and radiographically intact. Which factor '
             'should most change the primary surgical plan?',
     'choices': ['The surface diameter seen on inspection', 'The three-dimensional extent of invasion', 'The histologic grade of the biopsy tissue', 'The p16 status of the biopsy specimen'],
     'answer': 1,
     'explanation': 'Oral cavity surgery is planned on three-dimensional extent, not surface size. Her deep extension toward the extrinsic tongue muscles means the resection must include part of the '
                    'tongue to achieve a clear deep margin, which is often the limiting margin in floor-of-mouth cancer. Depth also upgrades T category and drives the reconstruction choice, often a free '
                    'flap to preserve tongue mobility, and supports elective neck dissection.',
     'why_wrong': ['Surface size underestimates this tumor; the 9-mm depth and tongue extension determine the resection.',
                   'Correct.',
                   'Grade has limited influence on resection extent compared with depth, bone status, and margin requirements.',
                   'p16 has prognostic meaning in oropharyngeal cancer but does not change surgical planning for oral cavity SCC.'],
     'board_pearl': 'The deep margin is usually limiting in floor-of-mouth cancer; plan resection on depth, not surface size.',
     'curveball': 'How does depth of invasion affect elective neck management in an otherwise N0 oral cavity cancer?',
     'curveball_answer': 'Depth of invasion predicts occult nodal metastasis. Guidelines recommend elective neck dissection when depth exceeds about 3 mm, and observation may be considered only for very '
                         'thin tumors with reliable follow-up. Because floor-of-mouth tumors are near midline with bilateral drainage, consider bilateral levels I to III when the lesion approaches or '
                         'crosses midline.'},
    'v220_hn_fom_fnd': {'stem': 'A 59-year-old man with a 40 pack-year smoking history and daily alcohol use has a painful sore under his tongue for 7 weeks that did not heal after his dentist smoothed a sharp tooth. Exam '
             'shows a 1.5-cm ulcer with rolled edges in the anterior floor of mouth, with firm induration surrounding the left Wharton duct opening. Which diagnosis must be excluded with prompt biopsy?',
     'choices': ['Sialolith with obstructive submandibular sialadenitis',
                 'Traumatic ulcer from the sharp edge of a tooth',
                 'Squamous cell carcinoma of the floor of mouth',
                 'Simple ranula from a ruptured sublingual gland duct'],
     'answer': 2,
     'explanation': 'A floor-of-mouth ulcer persisting more than 3 weeks after removal of an irritant, with rolled edges and induration, in a heavy smoker and drinker is SCC until proven otherwise. '
                    'Prompt biopsy is required, followed by assessment of depth, mandible, Wharton duct, lingual nerve, and the neck. Duct involvement can obstruct the submandibular gland and mimic '
                    'nodal disease, so imaging should distinguish gland swelling from nodes.',
     'why_wrong': ['Sialoliths cause meal-related swelling and may be palpable but do not produce a persistent ulcer with rolled edges.',
                   'Traumatic ulcers heal within 2 to 3 weeks after removal of the cause; persistence despite smoothing the tooth demands biopsy.',
                   'Correct.',
                   'Ranulas are soft, bluish cystic swellings in the floor of mouth, not indurated ulcers with rolled edges.'],
     'board_pearl': 'An oral ulcer persisting beyond 3 weeks after removal of irritants needs biopsy, especially in smokers.',
     'curveball': 'Which examination findings would raise particular concern for mandibular or deep tongue involvement?',
     'curveball_answer': 'Fixation of the tumor to the mandible, loss of a mobile plane on bimanual exam, numbness of the lower lip and chin from inferior alveolar nerve involvement, and loose teeth '
                         'suggest bone invasion. Deep induration, reduced tongue mobility, deviation on protrusion, or lingual numbness suggest extension into the extrinsic muscles, lingual nerve, or '
                         'hypoglossal nerve.'},
    'v220_hn_fom_snr': {'stem': 'A 66-year-old dentate woman has a 3-cm SCC of the right lateral floor of mouth that is fixed to the lingual surface of the mandible. CT and MRI show the tumor abutting the lingual cortex '
             'without cortical erosion or marrow signal change, and panoramic radiograph shows good vertical bone height. The surgeon expects the periosteum and adjacent cortex can be cleared with '
             'margin. What is the best mandibular strategy?',
     'choices': ['Segmental mandibulectomy with fibula free flap reconstruction',
                 'Soft-tissue resection leaving the lingual periosteum in place',
                 'Marginal mandibulectomy preserving mandibular continuity',
                 'Definitive chemoradiation to avoid any mandibular resection'],
     'answer': 2,
     'explanation': 'Fixation to the lingual plate without cortical erosion or marrow involvement indicates periosteal contact, not medullary invasion. Marginal mandibulectomy removes the involved '
                    'periosteum and a rim of lingual cortex to achieve an adequate margin while preserving mandibular continuity, provided enough height remains, as here. Segmental resection is reserved '
                    'for medullary invasion, extensive cortical involvement, or an atrophic mandible that would fracture after marginal resection.',
     'why_wrong': ['Segmental resection adds major functional and reconstructive morbidity when imaging shows no medullary invasion.',
                   'A fixed tumor abutting the cortex makes the periosteum part of the tumor margin, so leaving it risks a positive deep margin.',
                   'Correct.',
                   'Oral cavity SCC is treated primarily with surgery; chemoradiation offers inferior control and adds osteoradionecrosis risk.'],
     'board_pearl': 'Periosteal involvement without marrow invasion: marginal mandibulectomy; medullary invasion: segmental resection.',
     'curveball': 'Intraoperatively the tumor is found to invade the medullary bone. How does a segmental defect change reconstruction and dental rehabilitation?',
     'curveball_answer': 'A segmental defect needs vascularized bone, typically a fibula free flap, to restore mandibular continuity, contour, and occlusion; plates alone or soft-tissue flaps risk plate '
                         'exposure and poor function. Fibula bone stock accepts osseointegrated implants, which can be placed at the time of reconstruction or later. Virtual surgical planning helps '
                         'restore occlusion and implant position.'},
    'v138_hn_08': {'stem': 'A 64-year-old man with a 30 pack-year history has 3 months of hoarseness. Microlaryngoscopy and biopsy show SCC confined to the middle third of the left true vocal fold, sparing the '
             'anterior commissure. Both folds are fully mobile, the neck is clinically negative, and exposure was excellent. He wants the treatment that best preserves his larynx. Which pair of options '
             'is oncologically appropriate?',
     'choices': ['Concurrent chemoradiation, or total laryngectomy',
                 'Transoral laser cordectomy, or definitive radiation',
                 'Radiation with elective neck irradiation, or neck dissection',
                 'Induction chemotherapy, or open partial laryngectomy with neck dissection'],
     'answer': 1,
     'explanation': 'This is T1a glottic SCC: one fold, normal mobility. Early glottic cancer is cured at very high rates with a single local modality, either transoral laser microsurgery or definitive '
                    'radiation, chosen by exposure, voice priorities, lesion location, logistics, and patient preference. Because the true vocal folds have sparse lymphatics, elective neck treatment is '
                    'not needed. Adding chemotherapy or radical surgery only increases morbidity.',
     'why_wrong': ['Chemoradiation and total laryngectomy are for advanced disease and are excessive for a T1a mobile-fold tumor.',
                   'Correct.',
                   'Occult nodal risk in early glottic cancer is low, so elective neck treatment adds morbidity without benefit.',
                   'Induction chemotherapy is used in advanced larynx preservation trials, and neck dissection is unnecessary in T1a disease.'],
     'board_pearl': 'T1 glottic cancer: single modality, laser or radiation, with no elective neck treatment.',
     'curveball': 'If stroboscopy instead showed impaired, but not absent, left vocal fold mobility, how would T category and treatment considerations change?',
     'curveball_answer': 'Impaired mobility makes it T2, implying deeper extension into the thyroarytenoid muscle. Local control with radiation alone is lower than for T1, so altered or hypofractionated '
                         'radiation is often used, and transoral resection requires deeper cordectomy with worse voice. Complete fixation would make it T3, with paraglottic involvement, prompting '
                         'chemoradiation or conservation or total laryngectomy discussion.'},
    'v143_hno_01': {'stem': 'A 71-year-old woman with a remote smoking history has SCC of the right true vocal fold, limited to the membranous fold with normal mobility. The anterior commissure is uninvolved, CT shows '
             'no cartilage abnormality, and there are no neck nodes on exam or imaging. She is scheduled for transoral laser cordectomy. A junior resident proposes adding a right selective neck '
             'dissection. What is the most appropriate plan?',
     'choices': ['Laser cordectomy with an ipsilateral selective neck dissection',
                 'Laser cordectomy with postoperative radiation to both necks',
                 'Laser cordectomy alone, without elective neck treatment',
                 'Laser cordectomy with bilateral selective neck dissections'],
     'answer': 2,
     'explanation': 'Early glottic cancer is a single-modality disease. The true vocal folds have sparse lymphatics, so occult nodal metastasis from a T1 cN0 tumor is rare and elective neck treatment is '
                    'not indicated. Transoral laser cordectomy alone, with clear margins, offers excellent local control and voice. Neck management becomes relevant with supraglottic or subglottic '
                    'extension, impaired mobility, or advanced T stage.',
     'why_wrong': ['Elective neck dissection adds morbidity without benefit in T1 cN0 glottic disease, unlike supraglottic cancer.',
                   'Adjuvant radiation converts single-modality cure into dual therapy, adding toxicity and removing radiation as a salvage option.',
                   'Correct.',
                   'Bilateral neck dissection treats a risk that is very low for early glottic cancer and adds unnecessary morbidity.'],
     'board_pearl': 'Early glottic cancer has low nodal risk; do not add elective neck treatment as you would for supraglottic disease.',
     'curveball': 'Which finding on preoperative exam would upstage her for impaired or fixed mobility and substantially change planning?',
     'curveball_answer': 'Reduced vocal fold motion on laryngoscopy makes it T2, and complete fixation of the fold or arytenoid, implying paraglottic space or thyroarytenoid invasion, makes it T3. '
                         'Fixation signals deep spread, warrants CT or MRI for paraglottic and cartilage involvement, and shifts treatment toward chemoradiation, conservation laryngectomy, or total '
                         'laryngectomy, with neck treatment.'},
    'v220_hn_glottic_snr': {'stem': 'A 52-year-old professional singer has T1a SCC of the middle third of the right vocal fold with superficial involvement, normal mobility, and excellent laryngeal exposure. Both transoral '
             'laser microsurgery and radiation are oncologically suitable. She asks which gives the better voice and whether radiation would limit future options. She lives 3 hours from the radiation '
             'center. What is the best recommendation approach?',
     'choices': ['Recommend radiation, because voice outcomes are better for all lesions',
                 'Recommend total laryngectomy to maximize the chance of local control',
                 'Recommend observation with stroboscopy until the fold loses mobility',
                 'Weigh exposure, depth, voice goals, travel and salvage in a shared decision'],
     'answer': 3,
     'explanation': 'Both modalities cure properly selected T1a glottic cancer at similar rates. Voice outcomes depend on lesion depth, location, and resection extent: a superficial cordectomy can give '
                    'near-normal voice, while radiation spares tissue but causes fibrosis and mucositis over weeks. Laser treatment is completed in one session and keeps radiation available for salvage '
                    'or second primaries. Counseling should be individualized through shared decision-making.',
     'why_wrong': ['Voice outcomes are broadly similar for superficial lesions, and claiming universal superiority misrepresents the evidence.',
                   'Total laryngectomy is grossly excessive for T1a disease, which single-modality larynx-sparing treatment cures at high rates.',
                   'Observation allows a curable cancer to progress to T2 or beyond, reducing cure rates and voice preservation.',
                   'Correct.'],
     'board_pearl': 'For T1a glottic cancer, laser and radiation are equivalent oncologically; choose by depth, exposure, voice goals and logistics.',
     'curveball': 'The lesion instead involves the anterior commissure. How does that affect exposure, resection, and recurrence counseling?',
     'curveball_answer': 'Anterior commissure involvement makes transoral exposure harder, puts tumor next to Broyles ligament with a route into thyroid cartilage, and is associated with higher local '
                         'recurrence after both laser and radiation in many series. Resection risks anterior web formation and poorer voice. Careful imaging for cartilage invasion and experienced '
                         'surgical judgment, or radiation, are often favored.'},
    'v138_hn_09': {'stem': 'A 63-year-old man is 2 years past composite resection and adjuvant radiation for a T3N1 SCC of the retromolar trigone. His last exam and neck CT were clear. He still smokes half a pack '
             'daily and drinks most evenings. He feels well apart from dry mouth and asks whether he can stop coming to the head and neck clinic. What is the most appropriate counsel?',
     'choices': ['Continue scheduled exams while treating tobacco use and late effects',
                 'Discharge to primary care since recurrence after 2 years is very rare',
                 'Continue follow-up with PET/CT every 3 months for the next 5 years',
                 'Replace clinic exams with an annual chest radiograph and blood tests'],
     'answer': 0,
     'explanation': 'Most recurrences occur within 2 to 3 years, but risk does not end then, and second primaries in the lung, esophagus, and upper aerodigestive mucosa continue at a few percent per '
                    'year, highest in those who keep smoking. NCCN-based surveillance continues with history and examination, less often after year 2, plus tobacco and alcohol cessation, dental, '
                    'thyroid, swallowing, and psychosocial care. Survivorship is active care.',
     'why_wrong': ['Correct.',
                   'Recurrence risk falls after 2 years but persists, and second primary risk is ongoing, especially with continued smoking.',
                   'Routine frequent PET in asymptomatic patients beyond the post-treatment baseline is not recommended and generates false positives.',
                   'Chest radiographs are insensitive for lung cancer, and blood tests cannot replace examination of the treated field.'],
     'board_pearl': 'Survivorship surveillance continues beyond 2 years and includes cessation support and late-effect care.',
     'curveball': 'At his next visit he reports 6 weeks of cough with blood-streaked sputum. How should this be evaluated?',
     'curveball_answer': 'New hemoptysis or persistent cough in a smoking head and neck survivor raises concern for second primary lung cancer or pulmonary metastasis. Obtain CT of the chest with '
                         'contrast promptly, followed by pulmonology referral for bronchoscopy or biopsy of any lesion. He should also be offered annual low-dose CT lung screening if he meets criteria.'},
    'v145_hn_06': {'stem': 'A 66-year-old woman with a 50 pack-year history is 3 years past total laryngectomy for T4aN0 glottic SCC and still smokes. She is asymptomatic, and the stoma and neck are clear on exam. A '
             'low-dose screening chest CT shows a new 1.6-cm solitary spiculated nodule in the right upper lobe; there are no other lesions or adenopathy. What is the most likely nature of this nodule?',
     'choices': ['Hematogenous metastasis from laryngeal cancer',
                 'Second primary non-small cell lung cancer',
                 'Postobstructive inflammation near the stoma',
                 'Radiation-induced fibrosis of the lung apex'],
     'answer': 1,
     'explanation': 'Field cancerization from tobacco exposes the entire aerodigestive tract, including the bronchial mucosa, to carcinogens, so survivors of laryngeal SCC face a persistent risk of '
                    'second primaries, with the lung the most common site. A solitary spiculated nodule appearing years after an N0 primary is more likely a new lung cancer than a metastasis, which '
                    'tends to be multiple, round, and earlier. It requires tissue diagnosis, because a second primary may be curable.',
     'why_wrong': ['Metastases from N0 laryngeal SCC are less likely, tend to appear earlier, and are usually multiple, smooth nodules.',
                   'Correct.',
                   'Postobstructive changes are not expected after laryngectomy and would not produce a solitary spiculated peripheral nodule.',
                   'She was treated with surgery alone, and radiation fibrosis has a linear, field-shaped pattern, not a spiculated nodule.'],
     'board_pearl': 'Lung is the most common second primary after tobacco-related head and neck SCC; a solitary spiculated nodule needs biopsy.',
     'curveball': 'Over the coming years, which new symptom should prompt expedited esophageal evaluation in this patient?',
     'curveball_answer': 'Progressive dysphagia to solids, odynophagia, regurgitation, or weight loss, which in a laryngectomee may also reflect pharyngeal recurrence or stricture. Obtain a barium study '
                         'and upper endoscopy with biopsy promptly, because esophageal squamous cell carcinoma is a smoking- and alcohol-related second primary in this population.'},
    'v227_hn_surv_fnd': {'stem': 'A 54-year-old man completed surgery and adjuvant chemoradiation for a pT2N2b oral tongue SCC 8 months ago. At his surveillance visit he asks what these appointments are for, because his '
             '3-month PET/CT was negative and he feels cured. He has xerostomia and mild dysphagia and has resumed light smoking. Which statement best describes the purposes of his long-term follow-up?',
     'choices': ['To detect recurrence at the original tumor site only',
                 'To repeat PET/CT until five years show no disease',
                 'To find recurrence or new primaries and manage effects',
                 'To screen for distant spread using serial serum tumor markers'],
     'answer': 2,
     'explanation': 'Surveillance has two major purposes: detecting recurrence or new primary cancers early enough that salvage may succeed, and identifying and managing treatment-related dysfunction '
                    'such as dysphagia, xerostomia, dental disease, hypothyroidism, fibrosis, and psychosocial distress. His resumed smoking makes cessation support a key part of each visit, because it '
                    'reduces second primary risk. A negative early PET does not end the need for follow-up.',
     'why_wrong': ['Recurrence can be regional or distant, and second primaries arise at other mucosal sites, so the whole field must be checked.',
                   'Routine repeated PET in asymptomatic patients is not recommended after a negative post-treatment baseline study.',
                   'Correct.',
                   'No serum tumor marker is validated for detecting recurrence of oral cavity SCC.'],
     'board_pearl': 'Surveillance means detecting recurrence and second primaries plus managing late toxicity and tobacco use.',
     'curveball': 'Which smoking-related second primary sites deserve particular attention in his follow-up?',
     'curveball_answer': 'The lung, which is the most common second primary site and warrants annual low-dose CT screening if he meets criteria; the esophagus, assessed by dysphagia history and '
                         'endoscopy when symptomatic; and the remaining oral cavity, pharynx, and larynx mucosa, examined with flexible laryngoscopy at each visit. Persistent alcohol and tobacco use '
                         'raise all of these risks.'},
    'v227_hn_surv_app': {'stem': 'A 60-year-old woman is 2 years past composite resection and radiation for an oral cavity SCC. Six weeks after a reassuring routine visit, she reports new deep left ear pain, progressive '
             'solid-food dysphagia, and 5 kg weight loss. Otoscopy is normal. Her next scheduled appointment is in 2 months. What is the best next step?',
     'choices': ['Reassure her and reassess at the routine visit in 2 months',
                 'Start an 8-week trial of a proton pump inhibitor for reflux',
                 'Refer to swallowing therapy for presumed late radiation fibrosis',
                 'Expedited endoscopy, contrast imaging, and biopsy of any lesion'],
     'answer': 3,
     'explanation': 'New referred otalgia with a normal ear, progressive dysphagia, and weight loss are red flags for recurrence or a second primary in the pharynx or larynx. New focal symptoms override '
                    'the routine surveillance calendar and require prompt examination including flexible laryngoscopy, contrast CT or MRI, often PET/CT, and biopsy of any suspicious area. Late radiation '
                    'effects are a diagnosis of exclusion once recurrence has been sought.',
     'why_wrong': ['Delaying 2 months allows a possible recurrence to progress and may convert a salvageable lesion to an unresectable one.',
                   'Reflux does not explain referred otalgia with weight loss, and an empirical trial delays the diagnosis.',
                   'Late fibrosis is possible, but new progressive symptoms must be evaluated for recurrence before attributing them to toxicity.',
                   'Correct.'],
     'board_pearl': 'New otalgia, dysphagia or weight loss after treatment is recurrence until proven otherwise.',
     'curveball': 'When is PET/CT most useful after definitive chemoradiation, and when can early imaging be misleading?',
     'curveball_answer': 'A PET/CT about 12 weeks after chemoradiation best assesses response; PET-NECK showed that a negative scan allows observation of the neck instead of planned dissection. Imaging '
                         'earlier than about 8 to 12 weeks is confounded by radiation-induced inflammation, which causes false-positive uptake and can prompt unnecessary biopsies of healing tissue.'},
    'v227_hn_surv_snr': {'stem': 'A 67-year-old woman is 5 years past chemoradiation for a T2N1 p16-negative supraglottic SCC, with no evidence of disease. She quit smoking at diagnosis. Her prior surgeon ordered neck CT '
             'every 3 months, and she asks whether this should continue for life. She has hypothyroidism on levothyroxine and moderate dysphagia. Which surveillance plan is most appropriate now?',
     'choices': ['Continue contrast neck CT every 3 months for the rest of her life',
                 'Discharge from all follow-up because she has passed 5 years',
                 'Annual exam, symptom-driven imaging, and late-effect care',
                 'Replace examinations with circulating tumor DNA testing alone'],
     'answer': 2,
     'explanation': 'Most recurrences occur within the first 2 to 3 years, so surveillance intensity should taper as time passes, while second primary and late-toxicity risks persist. After 5 years, '
                    'NCCN-based follow-up is usually annual history and examination with imaging driven by symptoms or exam findings, plus thyroid testing, swallowing and dental care, and lung cancer '
                    'screening if eligible. Imaging should be ordered only when the result would change management.',
     'why_wrong': ['Frequent routine imaging this late rarely detects salvageable disease and adds cost, radiation, and false positives.',
                   'Second primary and late toxicity risks persist, so she still needs annual examination and survivorship care.',
                   'Correct.',
                   'Circulating tumor DNA assays are not validated for p16-negative surveillance and cannot replace examination.'],
     'board_pearl': 'Surveillance should taper with time, but annual exam and survivorship care continue after 5 years.',
     'curveball': 'If she had resumed smoking, how would that change counseling about second primary prevention and screening?',
     'curveball_answer': 'Continued smoking increases second primary risk in the lung, esophagus, and head and neck mucosa, and worsens late toxicities. Counseling should include pharmacotherapy such as '
                         'varenicline with behavioral support at every visit, annual low-dose CT lung screening if she meets criteria, and attention to esophageal symptoms. Quitting reduces second '
                         'primary risk over time.'},
    'v138_hn_10': {'stem': 'A 65-year-old woman is 6 years past chemoradiation for a T2N2 tonsil SCC. She reports gradually worsening dysphagia to solids, persistent dry mouth, a tight woody neck, fatigue, and cold '
             'intolerance. Flexible laryngoscopy and contrast neck CT show post-treatment changes without mass. TSH is 14 mIU/L with low free T4. What is the best interpretation and plan?',
     'choices': ['Recurrent tumor; schedule PET/CT and panendoscopy with directed biopsies',
                 'Late radiation effects; start levothyroxine and swallow therapy',
                 'Autoimmune thyroiditis unrelated to her radiation treatment',
                 'Expected aging changes that do not need specific treatment'],
     'answer': 1,
     'explanation': 'With recurrence excluded by examination and imaging, her symptoms fit late radiation toxicity: xerostomia from acinar cell loss, fibrosis-driven dysphagia and neck stiffness, and '
                    'primary hypothyroidism from incidental thyroid irradiation. These effects evolve over years and need their own surveillance and treatment: thyroid replacement and periodic TSH, '
                    'instrumental swallowing evaluation and therapy, dental prevention, lymphedema and fibrosis therapy, and nutrition support.',
     'why_wrong': ['Gradual multisystem symptoms with negative endoscopy and CT fit late toxicity; invasive biopsy needs a specific diagnostic question.',
                   'Correct.',
                   'Radiation is the most likely cause of hypothyroidism here, and the label does not address her dysphagia and fibrosis.',
                   'These are treatable radiation effects, not aging, and ignoring them worsens dysphagia, nutrition, and quality of life.'],
     'board_pearl': 'Radiation-induced hypothyroidism is common; check TSH periodically after neck radiation.',
     'curveball': 'She now needs a mandibular molar extraction in the high-dose field. Which dental precautions matter?',
     'curveball_answer': 'Extraction in irradiated bone risks osteoradionecrosis. Coordinate with an oral surgeon familiar with irradiated patients, review the dose to that region, use atraumatic '
                         'technique with primary closure, and consider perioperative antibiotics and chlorhexidine. The 2024 ISOO-MASCC-ASCO guideline does not support routine prophylactic hyperbaric '
                         'oxygen. Daily fluoride trays and close follow-up continue afterward.'},
    'v145_hn_07': {'stem': 'A 58-year-old man is 4 years past radiation for nasopharyngeal carcinoma. He has worsening dysphagia with occasional cough on liquids, severe xerostomia, rampant cervical caries in several '
             'teeth, 6 kg weight loss, and a TSH of 9 mIU/L. He has not seen a dentist since treatment and stopped using fluoride trays. Endoscopy and MRI show no recurrence. Which plan best addresses '
             'his problems?',
     'choices': ['Levothyroxine alone, with recheck of thyroid function in 6 weeks',
                 'Dental extraction of all remaining teeth and immediate dentures',
                 'Gastrostomy tube placement with no oral intake from now onward',
                 'Dental care with fluoride, swallow study, nutrition and thyroid care'],
     'answer': 3,
     'explanation': 'Late radiation toxicity is multisystem and needs coordinated survivorship care rather than single-problem treatment. He needs urgent dental care with daily fluoride and restoration '
                    'to protect teeth and prevent osteoradionecrosis, instrumental swallowing evaluation with speech pathology rehabilitation given his cough, dietitian support for weight loss, thyroid '
                    'replacement, and salivary measures such as sialogogues. Waiting for crises leads to aspiration, tooth loss, and ORN.',
     'why_wrong': ['Thyroid replacement is needed but ignores his dental decay, aspiration risk, and weight loss.',
                   'Mass extraction in irradiated bone risks osteoradionecrosis, and many carious teeth can be restored with fluoride and dental care.',
                   'Making him NPO before an instrumental swallow study is premature and may accelerate disuse atrophy of swallowing muscles.',
                   'Correct.'],
     'board_pearl': 'Late radiation toxicity is multisystem; coordinate dental, swallow, nutrition and thyroid care rather than treating one issue.',
     'curveball': 'He is admitted with a second aspiration pneumonia in 3 months. What tests and functional decisions become urgent?',
     'curveball_answer': 'Obtain an instrumental swallowing study, FEES or modified barium swallow, to define aspiration and test compensatory strategies, plus chest imaging. Decide on nutrition route, '
                         'such as temporary or long-term gastrostomy, while continuing swallowing exercises where safe. Evaluate for vocal fold paralysis from lower cranial neuropathy, and discuss goals '
                         'if aspiration is intractable.'},
    'v222_hn_rts_fnd': {'stem': 'A 52-year-old woman finished IMRT for an oropharyngeal SCC 13 months ago and is disease-free. Her mucositis and skin changes have healed, and she asks if her treatment side effects are now '
             'behind her. She has persistent mild xerostomia and slightly reduced neck mobility. Which statement about radiation late effects is most accurate?',
     'choices': ['They resolve by one year once mucositis and dermatitis heal',
                 'They can arise or progress for years and need lifelong follow-up',
                 'They follow the recurrence curve and stop after two to three years',
                 'They are age-related changes not caused by radiation therapy itself'],
     'answer': 1,
     'explanation': 'Acute effects such as mucositis and dermatitis occur in rapidly dividing tissue and heal within months. Late effects arise in slowly dividing connective tissue and vessels through '
                    'fibrosis and endarteritis, and can appear or worsen for years: xerostomia, dental decay, dysphagia and aspiration, trismus, neck fibrosis, lymphedema, hypothyroidism, '
                    'osteoradionecrosis, and carotid atherosclerosis. Each needs its own lifelong surveillance and prevention plan.',
     'why_wrong': ['Healing of acute toxicity does not end late toxicity, which develops in slowly dividing tissues over years.',
                   'Correct.',
                   'Recurrence risk wanes over 2 to 3 years, but fibrosis, ORN, hypothyroidism, and carotid disease can appear much later.',
                   'These changes follow the radiation field and dose and are well-documented treatment effects, not normal aging.'],
     'board_pearl': 'Radiation late effects evolve over years; build lifelong surveillance for dental, swallow, thyroid and carotid problems.',
     'curveball': 'Which preventive dental strategy is especially important before and after high-dose mandibular radiation?',
     'curveball_answer': 'Before radiation, a dental evaluation with extraction of nonrestorable or doubtful teeth, ideally about 2 weeks before treatment to allow healing, and custom fluoride trays. '
                         'After radiation, lifelong daily topical fluoride, meticulous hygiene, regular dental visits, and avoidance of extractions in irradiated bone when possible, because extraction '
                         'is the most common trigger of osteoradionecrosis.'},
    'v222_hn_rts_app': {'stem': 'A 70-year-old man is 5 years past chemoradiation for laryngeal SCC and has no evidence of disease. Over 6 months he has had three pneumonias, 7 kg weight loss, and coughing during meals, '
             'and he avoids eating with family. Flexible laryngoscopy shows no recurrence but pooled secretions and reduced laryngeal sensation. Chest CT shows right lower lobe infiltrates. What is the '
             'best next step?',
     'choices': ['Reassurance and a high-calorie oral supplement',
                 'Prophylactic long-term antibiotics with no other changes',
                 'PET/CT and panendoscopy with random biopsies',
                 'Instrumental swallow study with SLP-led rehabilitation'],
     'answer': 3,
     'explanation': 'Late radiation-associated dysphagia results from progressive fibrosis and lower cranial neuropathy and can cause silent aspiration years after treatment. Recurrent dependent-lobe '
                    'pneumonia, weight loss, pooled secretions, and reduced sensation point to aspiration. An instrumental study, modified barium swallow or FEES, defines the physiology and tests '
                    'compensatory strategies, guiding speech pathology rehabilitation and decisions about diet and gastrostomy.',
     'why_wrong': ['Supplements without addressing aspiration add calories while continuing the risk of recurrent pneumonia.',
                   'Prophylactic antibiotics do not stop aspiration and promote resistance while the underlying swallow problem progresses.',
                   'Laryngoscopy shows no tumor, and his symptoms fit aspiration; random biopsies in irradiated tissue risk chondronecrosis.',
                   'Correct.'],
     'board_pearl': 'Late radiation dysphagia can cause silent aspiration years later; recurrent pneumonia warrants an instrumental swallow study.',
     'curveball': 'Despite rehabilitation and gastrostomy feeding, he continues to aspirate saliva with recurrent pneumonia. When does aspiration-prevention surgery enter the discussion?',
     'curveball_answer': 'When aspiration is intractable and life-threatening despite maximal rehabilitation, nonoral feeding, and secretion management, and the larynx is functionally useless. Options '
                         'include laryngotracheal separation, which is potentially reversible, or narrow-field total laryngectomy, both sacrificing voice. Discuss goals, alaryngeal speech options, and '
                         'prognosis before proceeding.'},
    'v222_hn_rts_snr': {'stem': 'A 64-year-old man treated with 70 Gy for a tonsil SCC 7 years ago had a mandibular molar extracted 3 months ago. He now has 1.5 cm of exposed bone at the socket with pain, foul taste, and '
             'no fistula or lip numbness. Panoramic radiograph shows a small area of lucency limited to the alveolus, with no pathologic fracture. What is the most appropriate initial management?',
     'choices': ['Segmental mandibulectomy with fibula free flap reconstruction',
                 'Rule out tumor and begin conservative care with medical therapy',
                 'Hyperbaric oxygen alone as definitive therapy without debridement',
                 'Repeat radiation to the mandible to treat possible occult tumor'],
     'answer': 1,
     'explanation': 'Exposed bone in a high-dose field after extraction is osteoradionecrosis until proven otherwise, but recurrence should be excluded with biopsy of suspicious soft tissue or imaging. '
                    'Early, limited ORN is managed conservatively with oral hygiene, chlorhexidine rinses, antibiotics for infection, removal of loose sequestra, and medical therapy such as '
                    'pentoxifylline with tocopherol. Advanced disease with fracture, fistula, or progression despite treatment escalates to resection with vascularized bone reconstruction.',
     'why_wrong': ['Segmental resection is reserved for advanced ORN with fracture, fistula, or failure of conservative care, not limited alveolar disease.',
                   'Correct.',
                   'HBO may be considered selectively, but guidelines do not support it as a default stand-alone therapy for ORN.',
                   'Re-irradiation worsens osteoradionecrosis and has no role without biopsy-proven recurrent tumor.'],
     'board_pearl': 'Early ORN: exclude recurrence and treat conservatively; fracture, fistula or progression calls for vascularized bone reconstruction.',
     'curveball': 'Which clinical or radiographic findings suggest impending pathologic fracture or the need for segmental reconstruction?',
     'curveball_answer': 'Lucency extending to the inferior border of the mandible, orocutaneous fistula, a pathologic fracture, involvement of the inferior alveolar canal with lip numbness, extensive '
                         'necrosis on CT, and pain or infection progressing despite medical therapy. These define advanced ORN that needs segmental resection to bleeding bone and reconstruction with a '
                         'vascularized free flap such as the fibula.'},
    'v138_hn_11': {'stem': 'A 61-year-old man who drinks heavily and smokes has 6 weeks of dysphagia to solids and right ear pain, with 9 kg weight loss. Exam shows a hard 5-cm right level III node. Laryngoscopy '
             'shows pooled secretions and an ulcerated mass filling the right pyriform sinus; both vocal folds move. A colleague is surprised the patient had no earlier symptoms. Which statement about '
             'this cancer is most accurate?',
     'choices': ['It often presents late, with nodal metastasis at diagnosis',
                 'It rarely spreads to nodes because its lymphatics are sparse',
                 'It is staged by p16 status, as oropharyngeal cancer is',
                 'It is usually cured by transoral local excision alone'],
     'answer': 0,
     'explanation': 'The hypopharynx is a distensible tube with loose submucosa, so tumors grow large and spread submucosally before causing dysphagia, and referred otalgia through the vagus is common. '
                    'Its rich lymphatics drain to levels II to IV, retropharyngeal, and paratracheal nodes, so most patients present with nodal disease and many with distant spread. Treatment must '
                    'address both oncologic control and swallowing, nutrition, and airway function.',
     'why_wrong': ['Correct.',
                   'Sparse lymphatics describe the true vocal folds; the hypopharynx has rich lymphatics and high nodal metastasis rates.',
                   'p16-based staging applies only to oropharyngeal cancer; hypopharyngeal SCC uses the standard AJCC 8 system.',
                   'Most hypopharyngeal cancers are advanced at diagnosis and need multimodality therapy, not local excision alone.'],
     'board_pearl': 'Hypopharyngeal SCC presents late, with nodal disease common, and carries the worst prognosis of laryngopharyngeal cancers.',
     'curveball': 'Which findings would favor primary laryngopharyngectomy over organ-preservation therapy for him?',
     'curveball_answer': 'A nonfunctional larynx with fixation and major aspiration, thyroid or cricoid cartilage destruction or extralaryngeal spread (T4a), bulky disease unlikely to respond, '
                         'tube-dependent dysphagia, poor pulmonary reserve that makes chronic aspiration dangerous, or inability to tolerate chemoradiation. These favor laryngopharyngectomy with '
                         'reconstruction and adjuvant therapy.'},
    'v145_hn_08': {'stem': 'A 57-year-old woman has SCC of the left pyriform sinus extending to the aryepiglottic fold, with a fixed left hemilarynx and bulky left level II to IV nodes. She has lost 8% of her body '
             'weight, coughs occasionally with liquids, and asks to keep her voice box if possible. CT reports equivocal thyroid cartilage sclerosis. What should happen before choosing a treatment '
             'modality?',
     'choices': ['Begin induction chemotherapy this week to test tumor response',
                 'Perform transoral laser resection of the primary tumor first',
                 'Define extent and laryngeal function, and correct nutrition',
                 'Schedule total laryngopharyngectomy without further testing'],
     'answer': 2,
     'explanation': 'Organ preservation is only meaningful if the larynx will remain oncologically controlled and functional. Before choosing chemoradiation, induction chemotherapy, or '
                    'laryngopharyngectomy, define true extent with endoscopy under anesthesia and cartilage imaging such as MRI, screen for synchronous primaries and distant disease, objectively assess '
                    'swallowing and aspiration, and address nutrition, often with a feeding tube. Multidisciplinary review then matches modality to tumor, function, and goals.',
     'why_wrong': ['Induction chemotherapy is one organ-preservation option, but starting it before defining cartilage invasion and function is premature.',
                   'Transoral resection is unsuitable for a fixed hemilarynx with bulky nodes and would not avoid adjuvant therapy.',
                   'Correct.',
                   'Laryngopharyngectomy may be right, but choosing it before defining cartilage invasion and function ignores her goals.'],
     'board_pearl': 'Larynx preservation is worthwhile only when the preserved larynx will be oncologically controlled and functional.',
     'curveball': 'Which findings would make total laryngopharyngectomy more compelling than organ-preservation treatment?',
     'curveball_answer': 'Confirmed cartilage destruction or extralaryngeal extension, a nonfunctional aspirating larynx, tube-dependent dysphagia, circumferential or bulky T4 disease, poor response to '
                         'induction chemotherapy, or inability to complete chemoradiation. Poor pulmonary reserve also tips the balance, because chronic aspiration after preservation is dangerous.'},
    'v221_hn_hypo_snr': {'stem': 'A 68-year-old man has T4a SCC of the right pyriform sinus with a fixed larynx and bilateral level III nodes. He has been gastrostomy-dependent for 2 months, has had two aspiration '
             'pneumonias, and his FEV1 is 55% predicted. Radiation oncology notes he could technically receive definitive chemoradiation. He wants the treatment most likely to let him live without '
             'pneumonia. What is the most appropriate treatment?',
     'choices': ['Definitive chemoradiation with larynx preservation and swallowing therapy',
                 'Induction chemotherapy, then radiation if there is a good tumor response',
                 'Total laryngopharyngectomy with reconstruction and adjuvant therapy',
                 'Palliative radiation alone, because his pulmonary reserve is limited'],
     'answer': 2,
     'explanation': 'Baseline function must enter modality selection. His larynx is already nonfunctional, with tube dependence and recurrent aspiration, and T4a disease predicts poor '
                    'larynx-preservation outcomes. Preserving an organ that already fails to protect the airway risks chronic aspiration, which is especially dangerous with limited pulmonary reserve. '
                    'Laryngopharyngectomy with flap reconstruction separates airway from food passage, removes the tumor, and is followed by adjuvant therapy based on pathology.',
     'why_wrong': ['Chemoradiation would preserve a larynx that already aspirates, and radiation fibrosis worsens dysphagia and pneumonia risk.',
                   'EORTC-style induction selects responders but cannot restore function to an already aspirating, fixed larynx with T4a disease.',
                   'Correct.',
                   'He has curable locoregional disease and a goal of avoiding pneumonia, which palliative radiation does not achieve.'],
     'board_pearl': 'A nonfunctional, aspirating larynx favors laryngopharyngectomy over organ preservation, even when chemoradiation is technically possible.',
     'curveball': 'Which reconstructive options restore pharyngeal continuity after circumferential versus partial pharyngeal defects?',
     'curveball_answer': 'Partial defects with a mucosal strip can be patched with a radial forearm or anterolateral thigh free flap, or a pectoralis major flap. Circumferential defects need a tubed '
                         'fasciocutaneous free flap such as ALT or radial forearm, or a jejunal free flap. Defects extending below the thoracic inlet usually need gastric pull-up. Pectoralis onlay over '
                         'a primary closure lowers fistula risk in irradiated patients.'},
    'v138_hn_12': {'stem': 'A 78-year-old man taking methotrexate for rheumatoid arthritis has a 1.4-cm painless violaceous nodule on the right cheek that appeared over 2 months. Biopsy shows Merkel cell carcinoma '
             'with CK20 perinuclear dot staining. He has no palpable parotid or neck nodes, and baseline PET/CT shows no regional or distant disease. Which plan is most appropriate?',
     'choices': ['Mohs excision of the primary with clinical follow-up of the neck',
                 'Wide excision with sentinel node biopsy and radiation planning',
                 'Excisional biopsy only, with observation if margins are clear',
                 'Elective superficial parotidectomy and radical neck dissection'],
     'answer': 1,
     'explanation': 'Merkel cell carcinoma is an aggressive neuroendocrine skin cancer whose small primary size belies a high rate of occult nodal disease, worse with immunosuppression. Standard care '
                    'for clinically node-negative disease is wide excision with sentinel node biopsy, done before or at the same time as excision so lymphatic channels are intact, plus multidisciplinary '
                    'consideration of adjuvant radiation because MCC is radiosensitive and recurrence-prone. Immunosuppression should be reduced where possible.',
     'why_wrong': ['Mohs can clear the primary, but omitting nodal staging misses frequent occult nodal disease that changes treatment.',
                   'Correct.',
                   'MCC recurs frequently and spreads early; observation after biopsy undertreats both the primary and regional nodes.',
                   'Elective radical surgery adds facial nerve and shoulder morbidity when sentinel biopsy can stage the clinically negative basin.'],
     'board_pearl': 'Merkel cell carcinoma: wide excision, sentinel node biopsy, and consider radiation; small size does not mean low risk.',
     'curveball': 'If he instead had a palpable 2-cm right parotid node confirmed by FNA, how would management change?',
     'curveball_answer': 'Clinically node-positive disease requires full staging with PET/CT and definitive regional treatment: therapeutic parotidectomy and neck dissection followed by radiation, or '
                         'definitive radiation to the primary and nodal basins in poor surgical candidates. Neoadjuvant or adjuvant immunotherapy may be considered within trials or multidisciplinary '
                         'review.'},
    'v145_hn_09': {'stem': 'A 69-year-old man who received a kidney transplant 9 years ago, on tacrolimus and mycophenolate, has a 2.2-cm rapidly growing red-violet nodule on the scalp vertex. Biopsy confirms Merkel '
             'cell carcinoma. There are no palpable nodes. He asks why his surgeon wants more than a simple excision. Which plan is most appropriate?',
     'choices': ['Excision with 5-mm margins, followed by routine dermatology follow-up',
                 'Carboplatin and etoposide chemotherapy before any surgical treatment',
                 'Imaging, wide excision with sentinel biopsy, and immunosuppression review',
                 'PD-1 inhibitor therapy before excision, continuing full immunosuppression'],
     'answer': 2,
     'explanation': 'MCC carries high nodal and distant metastatic risk, and solid-organ transplant recipients have more aggressive disease and worse survival. He needs baseline staging imaging, wide '
                    'excision with sentinel node biopsy, multidisciplinary planning for adjuvant radiation, and coordination with his transplant team to reduce immunosuppression or switch to an mTOR '
                    'inhibitor where possible. Checkpoint inhibitors are used cautiously in transplant patients because of graft rejection risk.',
     'why_wrong': ['Narrow excision without nodal staging or adjuvant planning undertreats a cancer with high recurrence and nodal spread.',
                   'Chemotherapy responses in MCC are brief, and systemic therapy is not first-line for localized resectable disease.',
                   'Correct.',
                   'Checkpoint inhibitors risk graft rejection in transplant recipients and are not standard neoadjuvant therapy for localized MCC.'],
     'board_pearl': 'Immunosuppression worsens MCC prognosis; stage carefully and review immunosuppression with the transplant team.',
     'curveball': 'His sentinel node is positive for micrometastasis. How does that change regional management?',
     'curveball_answer': 'Positive sentinel nodes require definitive regional treatment of that basin: radiation to the nodal basin, completion lymphadenectomy, or both, decided in tumor board. Surgery '
                         'may be preferred when radiation fields are complex, and radiation is preferred in frail patients. Adjuvant immunotherapy is not established as standard and is considered within '
                         'trials.'},
    'v223_hn_merkel_fnd': {'stem': 'An 82-year-old woman with chronic lymphocytic leukemia has a 1.2-cm painless, firm, red nodule on the left malar cheek that grew over 5 weeks. Biopsy shows small round blue cells with CK20 '
             'perinuclear dot positivity and negative TTF-1; Merkel cell polyomavirus is detected. Her family asks whether this is a minor skin cancer. Which description best fits this tumor?',
     'choices': ['An indolent adnexal tumor that only rarely spreads beyond the skin',
                 'A neuroendocrine carcinoma with early nodal and distant spread',
                 'A metastasis from small cell lung carcinoma to the facial skin',
                 'A locally destructive tumor that rarely metastasizes, like BCC'],
     'answer': 1,
     'explanation': 'This is Merkel cell carcinoma: an aggressive primary cutaneous neuroendocrine carcinoma of older, sun-exposed, or immunosuppressed patients. CK20 perinuclear dots with negative '
                    'TTF-1 confirm cutaneous origin and exclude metastatic small cell lung cancer. Most cases are driven by integrated Merkel cell polyomavirus. Occult nodal disease is common even with '
                    'small primaries, and recurrence and distant spread are frequent, so it is not a minor skin cancer.',
     'why_wrong': ['MCC is not indolent; its neuroendocrine biology produces early nodal metastasis and high mortality.',
                   'Correct.',
                   'Small cell lung carcinoma is TTF-1 positive and CK20 negative, the opposite of this staining pattern.',
                   'Basal cell carcinoma rarely metastasizes, whereas MCC has a high risk of nodal and distant spread.'],
     'board_pearl': 'Merkel cell carcinoma: CK20 perinuclear dot, TTF-1 negative, aggressive with early nodal spread.',
     'curveball': 'Which patient factors increase her risk of MCC, and how does immunosuppression affect prognosis?',
     'curveball_answer': 'Older age, fair skin with heavy UV exposure, and immunosuppression from CLL, HIV, or solid-organ transplant raise risk because cellular immunity normally controls polyomavirus '
                         'and UV-mutated cells. Immunosuppressed patients present with more advanced disease and have significantly worse disease-specific survival, and reducing immunosuppression when '
                         'possible is part of treatment.'},
    'v223_hn_merkel_app': {'stem': 'A 73-year-old man has a 1.1-cm Merkel cell carcinoma of the left preauricular skin diagnosed on punch biopsy. Exam and ultrasound of the parotid and neck are negative, and PET/CT shows no '
             'disease beyond the primary. The plastic surgery team plans wide excision with a rotation flap next week, and asks whether nodal staging can be done later if needed. What is the most '
             'appropriate regional staging plan?',
     'choices': ['Sentinel node biopsy at or before wide excision of the primary',
                 'Sentinel node biopsy after the rotation flap has fully healed',
                 'Elective superficial parotidectomy with selective neck dissection',
                 'Observation of the neck with ultrasound every 3 months instead'],
     'answer': 0,
     'explanation': 'Occult nodal metastasis is common in clinically node-negative MCC, and sentinel node status is a major prognostic factor that determines regional radiation or surgery. '
                    'Lymphoscintigraphy and sentinel biopsy should be performed before or at the same operation as wide excision, because excision and local flap rotation disrupt lymphatic channels and '
                    'make later mapping unreliable. Preauricular primaries often drain to the parotid, so facial nerve monitoring is useful.',
     'why_wrong': ['Correct.',
                   'After wide excision and flap rotation, lymphatic drainage is disrupted, making delayed sentinel mapping unreliable.',
                   'Elective dissection adds facial nerve risk without the targeted staging accuracy of sentinel biopsy in a clinically negative basin.',
                   'Ultrasound misses microscopic nodal disease, which is common in MCC and changes regional treatment.'],
     'board_pearl': 'Do sentinel node biopsy for MCC before or with wide excision, before flaps disrupt lymphatics.',
     'curveball': 'His sentinel node is positive. How does that alter regional radiation or surgery discussions?',
     'curveball_answer': 'A positive sentinel node is stage III disease and requires treatment of the involved basin with radiation, completion parotidectomy and neck dissection, or both. Radiation to '
                         'the primary site and nodal basin is commonly favored because MCC is highly radiosensitive. Adjuvant immunotherapy has mixed trial results and is not standard outside a trial.'},
    'v223_hn_merkel_snr': {'stem': 'An 86-year-old woman with Merkel cell carcinoma of the forehead, treated with excision and radiation 2 years ago, now has a painful unresectable recurrence over the frontal bone, bulky '
             'parotid nodes, and liver metastases on PET/CT. She lives independently, ECOG 1, and wants treatment if it is tolerable. Which approach is most appropriate?',
     'choices': ['Carboplatin and etoposide as first-line therapy for metastatic disease',
                 'Radical resection of the forehead recurrence with free flap repair',
                 'Immune checkpoint inhibitor with palliative radiation for symptoms',
                 'Hospice referral now without discussing systemic treatment options'],
     'answer': 2,
     'explanation': 'For advanced or metastatic MCC, PD-1 or PD-L1 blockade such as avelumab or pembrolizumab is first-line because responses are frequent and often durable, unlike the brief responses '
                    'to platinum-etoposide chemotherapy. With good performance status and a wish for tolerable treatment, she is a good candidate. Radiation can palliate the painful forehead lesion. '
                    'Goals-of-care discussion continues alongside treatment, and local surgery is not curative with distant disease.',
     'why_wrong': ['Chemotherapy responses in MCC are short-lived and more toxic, so it is reserved for checkpoint inhibitor failure or ineligibility.',
                   'Morbid local surgery does not change survival with liver metastases and delays effective systemic therapy.',
                   'Correct.',
                   'She is fit and wants tolerable treatment, so foregoing immunotherapy without discussion is not goal-concordant.'],
     'board_pearl': 'Advanced Merkel cell carcinoma: checkpoint inhibitors first-line, with radiation for local symptom control.',
     'curveball': 'When can radiation provide useful palliation even when cure is not realistic?',
     'curveball_answer': 'MCC is highly radiosensitive, so short courses, even a single 8 Gy fraction, can shrink painful, bleeding, ulcerated, or obstructing lesions and nodal masses in most patients '
                         'with little toxicity. Palliative radiation suits frail patients, sites causing pain or nerve compression, and lesions progressing during immunotherapy.'},
    'v138_hn_13': {'stem': 'A 77-year-old woman with severe aortic stenosis has 4 weeks of rapidly enlarging bilateral neck nodes, fevers, drenching night sweats, and 6 kg weight loss. Exam shows matted rubbery nodes '
             'in levels II to IV bilaterally, the largest 4 cm, with no mucosal lesion on endoscopy. Anesthesia advises against general anesthesia. Her airway is patent. Which tissue strategy is most '
             'appropriate?',
     'choices': ['Fine-needle aspiration cytology as the definitive diagnostic test',
                 'Ultrasound-guided multiple core biopsies with flow cytometry studies',
                 'Bilateral selective neck dissection to diagnose and treat the disease',
                 'Empiric involved-field radiation to the neck before obtaining tissue'],
     'answer': 1,
     'explanation': 'Rapidly enlarging bilateral nodes with B symptoms and no mucosal primary suggest lymphoma, which needs tissue architecture plus immunophenotyping and flow cytometry for '
                    'classification. Excisional biopsy is preferred when feasible, but when anesthesia risk is high, ultrasound-guided core biopsy with multiple cores, coordinated with hematopathology '
                    'and sending fresh tissue for flow, establishes many lymphoma diagnoses under local anesthesia. Surgery here is diagnostic, not therapeutic.',
     'why_wrong': ['FNA can suggest lymphoma but lacks the architecture needed for initial classification and subtyping.',
                   'Correct.',
                   'Lymphoma is treated systemically; neck dissection adds morbidity and is not therapy for this disease.',
                   'Treating without tissue risks the wrong diagnosis and destroys the material needed to classify the lymphoma.'],
     'board_pearl': 'Suspected lymphoma needs architecture and flow cytometry: excisional or multiple core biopsy, not FNA alone.',
     'curveball': 'Her nodes grow further and she develops inspiratory stridor while waiting for biopsy. How does airway compromise change urgency?',
     'curveball_answer': 'It becomes an airway emergency. Keep her upright with monitoring and oxygen, call anesthesia and the surgical team, avoid sedation that could convert partial to complete '
                         'obstruction, and secure the airway in a controlled setting with awake techniques and surgical backup. Obtain tissue as soon as safely possible, as steroids may be needed for '
                         'the airway even though they can compromise diagnosis.'},
    'v145_hn_10': {'stem': 'A 31-year-old man has a 3-month history of painless progressive enlargement of nodes in the left posterior triangle, with night sweats and pruritus. He does not smoke. Exam shows a 3-cm '
             'rubbery mobile node in level VB and smaller nodes nearby; endoscopy is normal. Ultrasound-guided FNA showed scattered atypical cells, nondiagnostic. What is the best next tissue strategy?',
     'choices': ['Repeat FNA with cell block and flow cytometry, then await results',
                 'Excisional biopsy of the accessible node, sent fresh',
                 'Modified radical neck dissection of the left neck',
                 'PET/CT now and repeat ultrasound in 6 to 8 weeks'],
     'answer': 1,
     'explanation': 'Persistent rubbery nodes with night sweats and pruritus in a young nonsmoker suggest Hodgkin lymphoma, where Reed-Sternberg cells are sparse in an inflammatory background and FNA is '
                    'frequently nondiagnostic. Excisional biopsy of an accessible representative node, delivered fresh to pathology for morphology, immunohistochemistry, and flow cytometry, is the '
                    'preferred diagnostic strategy. Care is taken to protect the spinal accessory nerve in level V.',
     'why_wrong': ['Repeated cytology rarely provides the architecture needed for Hodgkin diagnosis and delays treatment.',
                   'Correct.',
                   'Lymphoma is treated systemically, so a radical dissection adds morbidity, including CN XI injury, without therapeutic benefit.',
                   'PET stages known lymphoma but does not replace tissue, and repeat imaging delays a needed diagnosis.'],
     'board_pearl': 'Nondiagnostic FNA with suspected lymphoma: get excisional biopsy of an accessible node with fresh tissue.',
     'curveball': 'The only abnormal node is deep, posterior to the carotid sheath. How do you balance biopsy adequacy with operative morbidity?',
     'curveball_answer': 'Discuss with hematopathology first. Image-guided core biopsy with multiple cores can often establish the diagnosis while avoiding open dissection near the carotid and vagus. If '
                         'a more accessible node or extranodal site such as the tonsil appears on PET, biopsy that instead. Reserve open excision for nondiagnostic cores, planned with careful exposure '
                         'of the vessels and nerves.'},
    'v222_hn_lym_fnd': {'stem': 'A 38-year-old woman who never smoked has 2 months of painless enlarging nodes in the right neck with night sweats and 5 kg weight loss. CT shows multiple 1.5- to 3-cm nonnecrotic nodes in '
             'right levels II to V and enlarged mediastinal nodes; there is no mucosal abnormality on endoscopy. A colleague proposes panendoscopy with neck dissection for presumed metastatic SCC of '
             'unknown primary. What is the most appropriate approach?',
     'choices': ['Panendoscopy with right neck dissection for an unknown primary SCC',
                 'Two weeks of antibiotics before deciding whether to obtain tissue',
                 'FNA cytology alone as the definitive diagnostic test for her nodes',
                 'Biopsy planned with pathology to preserve architecture and send fresh'],
     'answer': 3,
     'explanation': 'Multiple nonnecrotic nodes across several levels, mediastinal disease, B symptoms, and no tobacco history point toward lymphoma rather than metastatic SCC. That suspicion should '
                    'change how tissue is obtained: coordinate with pathology, take an excisional or adequate core biopsy that preserves architecture, and send fresh tissue for flow cytometry and '
                    'molecular studies. Treating the neck as a metastatic SCC operation adds morbidity and may still miss the diagnosis.',
     'why_wrong': ['Neck dissection for presumed SCC adds morbidity for a disease treated systemically and misreads the clinical pattern.',
                   'Antibiotics delay diagnosis in a patient with B symptoms and multistation adenopathy that is unlikely to be infectious.',
                   'FNA cannot reliably classify lymphoma because it lacks the architecture and adequate material for full subtyping.',
                   'Correct.'],
     'board_pearl': 'Clinical suspicion of lymphoma should change how the node is biopsied, not just the differential.',
     'curveball': 'When can image-guided core biopsy provide an adequate diagnosis, and when is excisional biopsy preferable?',
     'curveball_answer': 'Multiple-core needle biopsy is often adequate for diffuse large B-cell lymphoma and when excision is unsafe or the node is deep. Excisional biopsy is preferred for suspected '
                         'Hodgkin, follicular, or other lymphomas where architecture and scattered diagnostic cells matter, for small or nondiagnostic cores, and whenever transformation must be '
                         'assessed.'},
    'v222_hn_lym_app': {'stem': 'A 45-year-old man has suspected lymphoma with several enlarged right cervical nodes: a 3-cm level III node beneath the sternocleidomastoid, a 1-cm superficial level IB node, and matted '
             'level IV nodes near the internal jugular vein. Hematopathology has requested tissue for flow cytometry and cytogenetics. You are performing an excisional biopsy. Which operative approach '
             'is best?',
     'choices': ['Remove all enlarged nodes through a selective neck dissection',
                 'Excise the 1-cm level IB node because it is quickest and safest to remove',
                 'Remove a representative node intact and send it fresh promptly',
                 'Remove the matted level IV nodes piecemeal and fix in formalin'],
     'answer': 2,
     'explanation': 'The goal is diagnosis with minimal morbidity. Choose a representative, abnormal, accessible node, here the 3-cm level III node, remove it intact with minimal crush and cautery '
                    'artifact, and deliver it fresh to pathology so flow cytometry and cytogenetics can be performed. Small nodes may be reactive and nondiagnostic, and formalin fixation prevents flow '
                    'studies. Removing every node adds morbidity without benefit.',
     'why_wrong': ['A dissection adds morbidity for a disease treated systemically, and the diagnosis needs only one representative node.',
                   'Small superficial nodes are often reactive and may miss the lymphoma, leading to a repeat procedure.',
                   'Correct.',
                   'Piecemeal removal destroys architecture, and formalin prevents the requested flow cytometry and cytogenetics.'],
     'board_pearl': 'Lymphoma biopsy: representative node, intact, minimal crush, sent fresh after talking with pathology.',
     'curveball': 'If the only abnormal node were deep and adjacent to the carotid and vagus, how would you choose between core and excisional biopsy?',
     'curveball_answer': 'Favor ultrasound- or CT-guided core biopsy with multiple cores after discussing adequacy with hematopathology, because open excision near the carotid and vagus adds vascular '
                         'and nerve risk. Look on PET for a safer alternative site. Proceed to open excision only if cores are nondiagnostic or the suspected subtype needs whole-node architecture.'},
    'v222_hn_lym_snr': {'stem': 'A 26-year-old woman has a bulky anterior mediastinal mass and a 2.5-cm left supraclavicular node. She has orthopnea, cannot lie flat, and has facial plethora. CT shows 60% tracheal '
             'narrowing above the carina and a small pericardial effusion. Thoracic surgery requests mediastinoscopy under general anesthesia for diagnosis. What should the otolaryngologist recommend?',
     'choices': ['Mediastinoscopy under general anesthesia with neuromuscular paralysis',
                 'Supraclavicular node excision under local anesthesia, sitting upright',
                 'High-dose steroids now and general anesthesia biopsy after improvement',
                 'Supraclavicular node excision under general anesthesia, lying supine'],
     'answer': 1,
     'explanation': 'A large anterior mediastinal mass with orthopnea, significant tracheal compression, and pericardial effusion carries a high risk of catastrophic airway or cardiovascular collapse '
                    'with supine positioning, induction, and loss of spontaneous ventilation. The safest diagnostic strategy is biopsy of an accessible peripheral node under local anesthesia with the '
                    'patient upright, coordinated with anesthesia, oncology, and pathology. General anesthesia is avoided or done with extracorporeal support on standby.',
     'why_wrong': ['General anesthesia with paralysis can cause complete airway or cardiovascular collapse when a compressive mediastinal mass loses muscle tone support.',
                   'Correct.',
                   'Steroids can rapidly shrink lymphoma but may make tissue nondiagnostic; reserve them for when no safe biopsy exists.',
                   'Supine positioning under general anesthesia carries the same collapse risk as the planned mediastinoscopy.'],
     'board_pearl': 'Mediastinal mass with orthopnea: biopsy a peripheral node under local anesthesia upright; avoid general anesthesia.',
     'curveball': 'Which preoperative symptoms and imaging features make general anesthesia particularly hazardous in these patients?',
     'curveball_answer': 'Orthopnea or inability to lie flat, stridor, syncope, superior vena cava syndrome, and upper body swelling; on imaging, tracheal or bronchial compression greater than about '
                         '50%, pericardial effusion, compression of the heart or great vessels, and a large anterior mediastinal mass. These patients may lose the airway or circulation on induction.'},
    'v138_hn_14': {'stem': 'A 47-year-old woman has a 1.9-cm SCC of the right lateral oral tongue with depth of invasion 6 mm on MRI. Palpation, ultrasound, and contrast CT of the neck are negative. She asks why her '
             'surgeon recommends a neck operation when the scans show no spread. Which concept best justifies elective neck treatment here?',
     'choices': ['Occult nodal metastasis risk exceeds the 15 to 20% threshold',
                 'Elective dissection removes the need for any adjuvant radiation',
                 'Lateral tongue tumors usually drain to both sides of the neck',
                 'Sentinel node biopsy cannot be performed in oral cavity cancer'],
     'answer': 0,
     'explanation': 'A clinically negative neck is not a pathologically negative neck. Oral tongue SCC with depth of invasion beyond a few millimeters carries an occult nodal metastasis rate well above '
                    "the 15 to 20% threshold at which elective treatment is justified. The D'Cruz randomized trial showed that elective neck dissection improves overall survival compared with watchful "
                    'waiting for early oral cancer. Elective treatment can be surgical or radiation-based.',
     'why_wrong': ['Correct.',
                   'Adjuvant radiation depends on final pathology, such as nodal disease, ENE, or margins; elective dissection does not eliminate it.',
                   'Lateralized tongue tumors drain mainly ipsilaterally; bilateral risk rises when the primary approaches or crosses midline.',
                   'Sentinel node biopsy is a validated alternative in selected early oral cancers at experienced centers.'],
     'board_pearl': 'Treat the N0 neck electively when occult metastasis risk exceeds about 15 to 20%, as in deeper oral tongue SCC.',
     'curveball': 'How does depth of invasion influence the elective neck decision in oral tongue SCC?',
     'curveball_answer': 'Depth of invasion is the strongest primary-tumor predictor of occult nodal disease and is incorporated into AJCC 8 T staging. Guidelines recommend elective neck dissection when '
                         'depth exceeds about 3 mm and allow observation with close follow-up for very thin tumors of 2 mm or less, with the intermediate range decided individually or by sentinel '
                         'biopsy.'},
    'v143_hno_03': {'stem': 'A 56-year-old man has a 2.6-cm SCC of the left lateral oral tongue with depth of invasion 8 mm. It is 2 cm from midline, and the floor of mouth is free. Exam and contrast CT show no '
             'suspicious nodes. He will undergo partial glossectomy with radial forearm free flap reconstruction. Which elective neck treatment is most appropriate?',
     'choices': ['Ipsilateral selective neck dissection of levels II to IV only',
                 'Bilateral radical neck dissection to clear all nodal basins',
                 'Ipsilateral selective neck dissection of levels I to III or IV',
                 'PET/CT surveillance of the neck, with dissection if it turns positive'],
     'answer': 2,
     'explanation': 'With an 8-mm depth of invasion, occult nodal risk is high, so the clinically negative neck should be treated electively rather than waiting for palpable disease. Oral cavity drains '
                    'first to levels I to III, and oral tongue cancers can skip to levels III and IV, so an ipsilateral supraomohyoid dissection of levels I to III, often extended to level IV for tongue '
                    'primaries, is standard. A lateralized tumor 2 cm from midline does not need contralateral treatment.',
     'why_wrong': ['Levels II to IV suit oropharyngeal and laryngeal primaries; omitting level I misses the first echelon for oral cavity cancer.',
                   'Radical dissection adds major morbidity without benefit in a clinically negative neck from a lateralized primary.',
                   'Correct.',
                   'PET misses micrometastases, and waiting for detectable disease forfeits the survival benefit of elective dissection.'],
     'board_pearl': 'N0 oral tongue: ipsilateral levels I to III, adding IV for tongue because of skip metastases.',
     'curveball': 'If the primary instead crossed midline into the contralateral tongue, how would contralateral neck treatment change?',
     'curveball_answer': 'A tumor reaching or crossing midline has bilateral lymphatic drainage, so the contralateral neck should also be treated electively, usually with a contralateral selective '
                         'dissection of levels I to III, or bilateral radiation if adjuvant therapy is planned. Floor-of-mouth involvement and thicker tumors increase contralateral risk further.'},
    'v225_hn_neck_fnd': {'stem': 'Two patients with clinically negative necks are presented at tumor board. A 64-year-old man has a 1.5-cm T1a SCC of the mid right vocal fold with normal mobility. A 52-year-old woman has a '
             '1.5-cm SCC of the right lateral oral tongue with depth of invasion 6 mm. The board recommends elective neck treatment for only the second patient. What best explains the difference?',
     'choices': ['Glottic cancer drains first to level I, which is treated with the primary',
                 'Oral tongue cancer spreads through blood vessels, not lymphatic channels',
                 'Each primary site differs in lymphatic density and occult nodal risk',
                 'Neck treatment for glottic cancer is withheld because of patient age'],
     'answer': 2,
     'explanation': "Occult nodal risk is determined by the primary site's lymphatic anatomy plus tumor features. The true vocal folds have sparse lymphatics, so T1 glottic cancer has very low nodal "
                    'risk and needs no elective neck treatment. The oral tongue has rich lymphatics draining to levels I to IV, and with deeper invasion its occult metastasis rate exceeds the threshold '
                    'for elective treatment, even at the same surface size.',
     'why_wrong': ['Glottic cancer drains to levels II to IV and VI, not level I, and early disease rarely spreads at all.',
                   'Oral tongue SCC spreads mainly through lymphatics, which is why elective neck dissection is valuable.',
                   'Correct.',
                   'Age does not determine elective neck treatment; site-specific lymphatic risk and tumor features do.'],
     'board_pearl': 'Same size, different neck: sparse glottic lymphatics versus rich oral tongue lymphatics change occult nodal risk.',
     'curveball': 'How would a depth of invasion of 1.5 mm instead of 6 mm alter neck management for the oral tongue patient?',
     'curveball_answer': 'A very thin tongue cancer with depth of invasion of 2 mm or less has low occult nodal risk, so observation with close clinical and ultrasound surveillance, or sentinel node '
                         'biopsy, are reasonable alternatives to elective dissection. Above about 3 mm, elective neck dissection is recommended.'},
    'v225_hn_neck_snr': {'stem': 'A 59-year-old man has a 3.8-cm SCC of the right lateral oral tongue whose medial edge lies 5 mm from midline, with depth of invasion 11 mm. He has two right level II nodes, one 3.5 cm. The '
             'left neck is clinically and radiographically negative. The fellow asks whether to dissect the left neck too. What should determine whether the contralateral neck is treated?',
     'choices': ['Midline proximity, depth, T stage, and ipsilateral nodal burden',
                 'Patient age and performance status, independent of tumor features',
                 'Contralateral dissection in every oral cavity cancer with nodes',
                 'Only a palpable or radiographically suspicious contralateral node'],
     'answer': 0,
     'explanation': 'Contralateral nodal risk is not binary. A primary approaching within millimeters of midline, deep invasion, advanced T category, and substantial ipsilateral nodal disease all '
                    'increase the probability of contralateral occult metastasis, and floor-of-mouth or tongue-base extension raises it further. With these features, many surgeons would treat the left '
                    'neck electively, by dissection or by including it in adjuvant radiation fields, after multidisciplinary review.',
     'why_wrong': ['Correct.',
                   'Age and fitness affect treatment tolerance but do not define contralateral nodal risk.',
                   'Many lateralized tumors with ipsilateral nodes have low contralateral risk, so a blanket rule overtreats.',
                   'Waiting for detectable contralateral disease ignores high occult risk created by near-midline, deep tumors.'],
     'board_pearl': 'Contralateral neck risk rises with midline proximity, depth, T stage and ipsilateral nodal burden.',
     'curveball': 'Which oral cavity or oropharyngeal subsites most often require bilateral neck consideration?',
     'curveball_answer': 'Floor of mouth, ventral or midline tongue, and tumors crossing midline in the oral cavity; in the oropharynx, base of tongue, soft palate, and posterior pharyngeal wall. '
                         'Lateralized tonsil cancers without significant tongue-base or palate extension can often be treated ipsilaterally. Supraglottic and nasopharyngeal primaries also need bilateral '
                         'treatment.'},
    'v138_hn_16': {'stem': 'A 66-year-old man has a T2N0 SCC of the epiglottis and right false vocal fold, with mobile true folds, a free anterior commissure, and no cartilage invasion on CT. The surgeon is '
             'considering open horizontal supraglottic laryngectomy. He smoked for 45 years and gets winded climbing one flight of stairs. Which patient factor must be confirmed before offering this '
             'operation?',
     'choices': ['Adequate pulmonary reserve with an effective cough',
                 'Age younger than 65 years at the time of surgery',
                 'No prior surgery anywhere on the neck or larynx',
                 'Normal voice quality on the preoperative exam'],
     'answer': 0,
     'explanation': 'Conservation laryngectomy requires both a suitable tumor and suitable physiology. Supraglottic laryngectomy removes the upper sphincters, so every patient aspirates during the weeks '
                    'of swallowing relearning. Only patients with adequate pulmonary reserve and a strong cough can clear that aspiration safely. Pulmonary function testing and stair climbing assessment '
                    'are part of candidacy; poor reserve converts a voice-sparing operation into chronic aspiration or an unplanned total laryngectomy.',
     'why_wrong': ['Correct.',
                   'Physiologic reserve matters more than age; fit older patients can undergo conservation surgery successfully.',
                   'Prior neck surgery may complicate the procedure, but it does not define candidacy the way pulmonary reserve does.',
                   'Voice quality is not a selection criterion, and many candidates are hoarse from their tumor.'],
     'board_pearl': 'Partial laryngectomy guarantees temporary aspiration; pulmonary reserve and cough are hard gates for candidacy.',
     'curveball': 'If his tumor were glottic instead, why would arytenoid function matter so much after supracricoid partial laryngectomy?',
     'curveball_answer': 'After supracricoid laryngectomy, the true and false folds and thyroid cartilage are removed, and the remaining mobile arytenoid moves against the base of tongue or epiglottis '
                         'to create a neoglottis. That arytenoid provides airway protection during swallowing, voice production, and opening for breathing. At least one functional cricoarytenoid unit is '
                         'required for decannulation and safe swallowing.'},
    'v145_hn_12': {'stem': 'A 60-year-old woman with good pulmonary function has glottic SCC involving the anterior two-thirds of both vocal folds and the anterior commissure, with impaired right fold mobility. She '
             'wants to avoid radiation and a permanent stoma, and is being evaluated for supracricoid partial laryngectomy. Which finding best supports her candidacy?',
     'choices': ['Both arytenoids are fixed, with tumor at the posterior commissure',
                 'Tumor extends 15 mm below the anterior commissure into subglottis',
                 'Tumor breaches the outer cortex of the thyroid cartilage on CT',
                 'The left arytenoid is mobile and free of tumor, with intact cricoid'],
     'answer': 3,
     'explanation': 'Supracricoid partial laryngectomy removes the true and false folds, paraglottic spaces, and thyroid cartilage, then rebuilds a neoglottis with cricohyoidopexy or '
                    'cricohyoidoepiglottopexy. Function depends on preserving at least one mobile, tumor-free cricoarytenoid unit and an intact cricoid ring. Impaired, but not fixed, mobility on the '
                    'tumor side is acceptable. Bilateral arytenoid fixation, significant subglottic extension, or extralaryngeal spread defeat the operation.',
     'why_wrong': ['Bilateral arytenoid fixation and posterior commissure involvement leave no functional cricoarytenoid unit for the neoglottis.',
                   'Subglottic extension of this degree approaches the cricoid, which must be preserved and tumor free for supracricoid surgery.',
                   'Outer cortex breach is T4a extralaryngeal disease, an indication for total laryngectomy rather than partial surgery.',
                   'Correct.'],
     'board_pearl': 'Supracricoid partial laryngectomy needs at least one mobile, tumor-free cricoarytenoid unit and an intact cricoid.',
     'curveball': 'Which tumor extension would generally defeat the premise of a supracricoid partial laryngectomy?',
     'curveball_answer': 'Fixation of both arytenoids or cricoarytenoid joint invasion, involvement of the posterior commissure or interarytenoid area, subglottic extension reaching the cricoid, cricoid '
                         'invasion, thyroid cartilage outer cortex penetration or extralaryngeal spread, and massive pre-epiglottic or hyoid involvement. Poor pulmonary reserve is also a '
                         'contraindication.'},
    'v228_hn_cons_fnd': {'stem': 'A 63-year-old man had radiation for a T1a left glottic SCC 2 years ago. He now has a biopsy-proven recurrence involving the left vocal fold and anterior commissure with impaired left fold '
             'mobility; the right fold and both arytenoids are free and mobile. CT shows no cartilage invasion. He asks about an alternative to total laryngectomy. Which requirement defines whether open '
             'conservation surgery is appropriate?',
     'choices': ['Tumor smaller than 2 cm, regardless of its precise anatomic site',
                 'Clear margins possible while a functional cricoarytenoid unit remains',
                 'Patient preference to avoid a stoma, regardless of tumor extent',
                 'Response to induction chemotherapy before the planned operation'],
     'answer': 1,
     'explanation': 'Open partial laryngectomy, including selected salvage cases after radiation, is appropriate only when the tumor can be removed with adequate margins while preserving enough '
                    'laryngeal framework, particularly a mobile cricoarytenoid unit, to restore airway, swallowing, and voice without a permanent stoma. Recurrence mapping by endoscopy and imaging, '
                    'cartilage status, subglottic extent, and pulmonary reserve all determine whether that is realistic. Irradiated tissue also heals less reliably.',
     'why_wrong': ['Size alone is insufficient; location relative to the arytenoids, cricoid, and cartilage determines feasibility.',
                   'Correct.',
                   'Patient preference matters, but conservation surgery that cannot clear tumor sacrifices oncologic control.',
                   'Induction chemotherapy response selects patients for radiation-based preservation, not for conservation surgery.'],
     'board_pearl': 'Conservation laryngectomy requires clear margins plus at least one preserved functional cricoarytenoid unit.',
     'curveball': 'On his endoscopy and imaging, which cricoarytenoid findings are most important for his candidacy?',
     'curveball_answer': 'Whether at least one arytenoid is mobile and free of tumor, whether the cricoarytenoid joint is fixed or invaded, whether tumor reaches the posterior commissure or '
                         'interarytenoid mucosa, and whether the cricoid itself is involved. Fixation suggests joint or posterior paraglottic invasion. Mapping these by endoscopy, stroboscopy, and '
                         'imaging decides between partial and total laryngectomy.'},
    'v228_hn_cons_app': {'stem': 'A 71-year-old man has a T2N0 SCC of the supraglottis with mobile true folds, anatomically suitable for open supraglottic laryngectomy. He has severe COPD with FEV1 at 38% predicted, a weak '
             'cough, two hospitalizations for pneumonia last year, and penetration of thin liquids on a baseline swallow study. He hopes to keep his voice. What is the best treatment recommendation?',
     'choices': ['Open supraglottic laryngectomy, because the tumor anatomy is suitable',
                 'Radiation-based therapy, or total laryngectomy, given his poor reserve',
                 'Supraglottic laryngectomy with a long-term tracheostomy for pulmonary toilet',
                 'Bilateral neck dissection alone, then observation of the primary site'],
     'answer': 1,
     'explanation': 'Pulmonary reserve is a hard gate for conservation surgery. Supraglottic laryngectomy produces expected aspiration during swallowing relearning, and with an FEV1 of 38%, a weak '
                    'cough, prior pneumonias, and baseline penetration, he cannot clear it safely. Definitive radiation-based therapy preserves the larynx without removing the sphincter, while total '
                    'laryngectomy separates airway from food path if needed. Anatomic resectability alone does not make partial laryngectomy the right operation.',
     'why_wrong': ['Anatomic suitability is not enough; his pulmonary status makes postoperative aspiration likely to be life-threatening.',
                   'Correct.',
                   'A tracheostomy does not prevent aspiration and would leave him with chronic pneumonia risk and no real functional gain.',
                   'The primary tumor must be treated; neck dissection alone leaves the supraglottic cancer untreated.'],
     'board_pearl': 'Severe COPD or weak cough contraindicates partial laryngectomy even when the tumor is anatomically suitable.',
     'curveball': 'In a different patient after supraglottic laryngectomy, aspiration persists at 3 months with recurrent pneumonia. How does rehabilitation and rescue planning change?',
     'curveball_answer': 'Continue intensive speech pathology with supraglottic and super-supraglottic swallow maneuvers, use instrumental studies to tailor diet, keep the tracheostomy and use '
                         'gastrostomy feeding for nutrition, and treat pneumonias. If aspiration remains intractable despite rehabilitation, completion total laryngectomy or laryngotracheal separation '
                         'may be required to protect the lungs.'},
    'v228_hn_cons_snr': {'stem': 'A 58-year-old man consented for supracricoid partial laryngectomy with possible total laryngectomy for a glottic SCC with a fixed right arytenoid. Intraoperatively, frozen sections show '
             'tumor extending across the posterior commissure into the left arytenoid mucosa, his only mobile arytenoid. Clearing the margin would require removing it. What is the best decision?',
     'choices': ['Accept the close posterior margin and plan postoperative chemoradiation',
                 'Remove both arytenoids and reconstruct a supracricoid neoglottis',
                 'Convert to total laryngectomy as covered by the preoperative consent',
                 'Leave residual disease in place for postoperative chemoradiation'],
     'answer': 2,
     'explanation': 'Conservation surgery is conditional on two premises: clear margins and a preserved functional cricoarytenoid unit. Here the only mobile arytenoid is involved, so either margins or '
                    'function must be sacrificed. Removing both arytenoids produces a larynx that cannot protect the airway, and leaving tumor compromises cure. The correct decision is conversion to '
                    'total laryngectomy, which is why consent for possible conversion is obtained beforehand.',
     'why_wrong': ['A knowingly positive margin in laryngeal cancer sharply increases recurrence, and radiation does not reliably sterilize residual disease.',
                   'A neoglottis without any mobile arytenoid cannot protect the airway, leading to aspiration and permanent tracheostomy.',
                   'Correct.',
                   'Leaving gross residual tumor sacrifices oncologic control and does not preserve a functional larynx.'],
     'board_pearl': 'If margins require the last functional cricoarytenoid unit, convert to total laryngectomy rather than force a partial.',
     'curveball': 'Looking back, which preoperative endoscopic or imaging findings help anticipate this conversion risk?',
     'curveball_answer': 'Arytenoid fixation, tumor at or across the posterior commissure or interarytenoid mucosa, subglottic extension toward the cricoid, paraglottic spread on MRI or CT, and '
                         'cartilage sclerosis or erosion. Careful microlaryngoscopy with angled telescopes and high-resolution imaging help, and these findings should be discussed during consent.'},
}
