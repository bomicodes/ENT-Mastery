"""v24.6 — Pediatric Otolaryngology deliberate ladder pass 6.

Five exact remaining canonical topics selected for boards, overnight-call and OR value:
tympanostomy-tube indications, velopharyngeal insufficiency, cleft/craniofacial
otologic-airway care, croup-versus-epiglottitis discrimination, and epiglottitis.
The two epiglottitis nodes are intentionally nonredundant: one teaches syndrome
recognition/triage and the other teaches confirmed supraglottitis airway management.
"""
DOMAIN="Pediatric Otolaryngology"


def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}


VIGNETTES_V246=[
_q("v246_ped_tubes_fnd","Tympanostomy Tube Indications","foundation",
"A healthy 3-year-old has bilateral otitis media with effusion documented for 4 months and an age-appropriate audiogram shows persistent conductive hearing loss. What is the best management principle?",
["Offer bilateral tympanostomy tubes after counseling because chronic bilateral OME with hearing difficulty is a standard indication","Continue observation indefinitely because effusion is never an operative indication","Prescribe repeated systemic antibiotics until the effusion clears","Perform adenoidectomy alone as the obligatory first procedure in every 3-year-old"],0,
"Persistent bilateral OME for at least 3 months with documented hearing difficulty is a classic tube indication after shared decision-making. The decision is based on chronicity plus functional consequence, not simply the presence of fluid on one visit.",
["Correct. Chronic bilateral OME plus hearing difficulty supports tympanostomy tubes.","Observation remains reasonable for many short-lived effusions, but prolonged hearing-relevant bilateral disease has crossed a standard intervention threshold.","Antibiotics do not provide durable clearance of sterile chronic middle-ear effusion.","Adenoidectomy is not an obligatory first-line substitute for tubes in every young child with chronic OME."],
"Tube questions are duration + symptoms/risk + whether effusion is actually present.","How would baseline speech-language delay or another developmental risk factor lower your threshold for intervention?"),
_q("v246_ped_tubes_app","Tympanostomy Tube Indications","application",
"A 2-year-old has had four well-documented episodes of acute otitis media in 6 months. At today's surgical evaluation both ears are aerated with no middle-ear effusion. The family requests tubes to prevent another infection. What is the best response?",
["Do not place tubes solely for recurrent AOM when no middle-ear effusion is present at candidacy assessment; continue follow-up and reassess if disease persists","Place tubes because episode count alone mandates surgery","Perform mastoidectomy because recurrent AOM implies occult mastoid disease","Start indefinite prophylactic oral antibiotics instead of reassessing"],0,
"For recurrent AOM, the presence of middle-ear effusion at the time of tube candidacy assessment materially changes the recommendation. Episode count without current effusion does not by itself justify routine tympanostomy tube placement.",
["Correct. Recurrent AOM without effusion at assessment is managed without routine tubes, with follow-up if infections continue.","Frequency criteria alone are not the whole candidacy decision when the ears are currently aerated.","Uncomplicated recurrent AOM is not an indication for mastoidectomy.","Chronic prophylactic systemic antibiotics create adverse effects and resistance without replacing appropriate reassessment."],
"For recurrent AOM, always ask: is there effusion today?","How would the recommendation change if unilateral or bilateral effusion were present at the candidacy visit?","senior_management"),
_q("v246_ped_tubes_snr","Tympanostomy Tube Indications","senior_decision",
"A 4-year-old with Down syndrome has persistent bilateral OME, fluctuating conductive loss, and limited expressive language. Thresholds on one office audiogram are only mildly elevated. What is the best senior-level recommendation?",
["Treat the child as at risk for speech/language consequences and use the full developmental and hearing trajectory—not a single mild audiogram—to decide on tubes and close audiologic follow-up","Dismiss the effusion because the latest threshold shift is mild","Wait for permanent language regression before intervening","Place long-term T-tubes automatically without considering anatomy, duration, or complication risk"],0,
"Children at increased developmental risk deserve a lower threshold for active management of persistent OME because fluctuating conductive loss can compound baseline communication vulnerability. Tube type and timing still require individualized risk-benefit assessment.",
["Correct. Developmental vulnerability, chronic effusion and longitudinal hearing access matter more than one isolated threshold value.","A single mildly abnormal test can understate the functional burden of fluctuating loss.","Waiting for irreversible developmental harm defeats the purpose of identifying an at-risk child.","Long-term tubes carry greater perforation and otorrhea risk and are not automatic for every at-risk child."],
"The chief-level tube decision is not a decibel cutoff; it is the child's hearing access over time and the consequence of losing it.","When would concurrent adenoidectomy become reasonable in a child undergoing repeat tube surgery?","senior_management"),

_q("v246_ped_vpi_fnd","Velopharyngeal Insufficiency","foundation",
"A child has persistent hypernasal speech with audible nasal air emission after repaired cleft palate. Which mechanism best defines velopharyngeal insufficiency?",
["A structural inability of the soft palate and pharyngeal walls to achieve adequate closure during pressure consonants","Isolated articulation mislearning with normal velopharyngeal closure","Conductive hearing loss from middle-ear effusion","Laryngeal weakness causing incomplete glottic closure"],0,
"Velopharyngeal insufficiency is a structural/anatomic failure of the velopharyngeal valve. It must be distinguished from velopharyngeal incompetence due to neuromotor dysfunction and from articulation errors that can mimic nasal emission despite adequate closure.",
["Correct. VPI is fundamentally a structural closure problem.","Learned articulation errors can cause nasal emission but do not equal structural VPI.","OME can affect speech development but does not create the velopharyngeal gap itself.","Glottic insufficiency changes voice and airway protection rather than creating the classic palatal-pharyngeal closure defect."],
"Hypernasality is a symptom; the board-level task is to decide whether the problem is structural, motor, or learned.","Why can a child have both compensatory articulation errors and true structural VPI at the same time?"),
_q("v246_ped_vpi_app","Velopharyngeal Insufficiency","application",
"A 6-year-old has hypernasality after cleft repair. Perceptual speech evaluation confirms resonance abnormality, but the team needs to choose an operation. What is the most useful next step?",
["Perform dynamic velopharyngeal assessment with nasoendoscopy and/or multiview videofluoroscopy to define closure pattern and gap before selecting surgery","Choose a pharyngeal flap from the sound of the voice alone","Order a routine neck CT as the primary dynamic speech study","Treat all hypernasality with speech therapy before evaluating structure"],0,
"Surgical planning for VPI depends on dynamic closure pattern, gap size and lateral pharyngeal-wall motion. Perceptual speech assessment establishes the functional problem; endoscopy or videofluoroscopy then localizes the mechanism for procedure selection.",
["Correct. Dynamic visualization connects the speech phenotype to the anatomy that must be corrected.","A pharyngeal flap is not selected safely from resonance alone because closure pattern and airway risk matter.","Static CT does not substitute for dynamic assessment during speech.","Speech therapy can correct compensatory articulation but cannot close a fixed structural gap."],
"VPI surgery should be pattern-driven, not procedure-driven.","How would poor lateral wall motion versus a small central gap influence the choice among flap, sphincter, or palatal-lengthening strategies?","OR_prep"),
_q("v246_ped_vpi_snr","Velopharyngeal Insufficiency","senior_decision",
"A child with repaired cleft palate has a large VPI gap and significant hypernasality, but also severe obstructive sleep apnea and multilevel airway obstruction. What is the best senior-level strategy?",
["Balance speech and airway goals explicitly; optimize/localize the airway and choose or stage VPI treatment to avoid creating dangerous additional obstruction","Proceed directly to the most obstructive pharyngeal flap because speech always takes priority","Avoid treating VPI permanently because any OSA is an absolute contraindication","Treat the OSA only after VPI surgery because resonance determines urgency"],0,
"Pharyngeal VPI procedures can narrow the upper airway. Severe baseline OSA changes operative planning and may require airway optimization, a less obstructive reconstruction, staging, or postoperative monitoring rather than reflex use of a standard flap.",
["Correct. The senior decision integrates speech benefit with the child's pre-existing airway reserve.","Maximizing obturation without considering airway physiology can worsen OSA substantially.","OSA does not make speech surgery impossible, but it demands tailored planning.","Severe airway disease may represent the more immediate physiologic risk and should not be ignored until after a potentially obstructive procedure."],
"In VPI, a technically excellent speech result is not excellent if the child cannot breathe safely during sleep.","What postoperative symptoms should trigger urgent evaluation for new or worsened sleep-disordered breathing?","senior_management"),

_q("v246_ped_cranio_fnd","Cleft / Craniofacial Otologic-Airway Care","foundation",
"Why are children with cleft palate particularly prone to chronic otitis media with effusion?",
["Abnormal palatal muscle anatomy impairs effective Eustachian-tube opening and middle-ear ventilation","The cochlea fails to form in most cleft-palate patients","The external auditory canal is routinely congenitally absent","Adenoid tissue mechanically blocks both Eustachian tubes in every infant with cleft palate"],0,
"Cleft palate disrupts the normal function and orientation of muscles involved in Eustachian-tube opening, especially the tensor veli palatini mechanism, producing chronic ventilation dysfunction and a high burden of OME.",
["Correct. Palatal anatomy creates a functional Eustachian-tube problem.","Most cleft-associated hearing disease is conductive from middle-ear dysfunction, not universal cochlear agenesis.","Canal atresia belongs to other craniofacial phenotypes and is not inherent to cleft palate.","Adenoid size is not the universal mechanism in infants with cleft palate."],
"Cleft palate links speech, swallowing and middle-ear ventilation through the same muscular anatomy.","Why does this physiology make longitudinal audiology important even after an initially successful set of tubes?"),
_q("v246_ped_cranio_app","Cleft / Craniofacial Otologic-Airway Care","application",
"An infant with Pierre Robin sequence has micrognathia, glossoptosis, intermittent desaturation and feeding difficulty. Which evaluation principle is most appropriate before choosing mandibular distraction or tongue-lip adhesion?",
["Define the level and severity of obstruction and look for multilevel disease, often including endoscopic airway assessment and sleep/oxygenation data when feasible","Assume all obstruction is isolated tongue-base collapse and operate without airway localization","Treat the middle-ear effusion first because it is the cause of desaturation","Delay airway assessment until after palate repair"],0,
"Robin-sequence airway management depends on physiology and obstruction level. Some infants improve with positioning or nasopharyngeal support, whereas severe tongue-base obstruction may require surgery; multilevel or non-glossoptotic disease predicts failure of a one-size-fits-all operation.",
["Correct. Airway localization and severity assessment should precede definitive skeletal or soft-tissue intervention when the child is stable enough for evaluation.","Not every infant has isolated tongue-base obstruction, and missed multilevel disease can cause operative failure.","OME affects hearing rather than causing the obstructive desaturation pattern.","Airway compromise is assessed and treated before elective palate repair."],
"Craniofacial airway surgery should follow localization; micrognathia on the face does not prove a single obstruction site.","Which findings would make tracheostomy more appropriate than a single-level reconstructive procedure?","senior_management"),
_q("v246_ped_cranio_snr","Cleft / Craniofacial Otologic-Airway Care","senior_decision",
"A child with repaired cleft palate, chronic Eustachian-tube dysfunction, prior tubes and new VPI is being considered for adenoid surgery because of nasal obstruction. What is the best senior-level framework?",
["Coordinate airway, speech and ear goals: preserve velopharyngeal function when possible, consider partial/targeted adenoid treatment if surgery is necessary, and continue hearing surveillance","Perform complete adenoidectomy routinely because prior palate repair eliminates VPI risk","Avoid all nasal-airway treatment forever in any child with a cleft history","Use repeated tympanostomy tubes as treatment for the child's nasal obstruction and VPI"],0,
"The adenoid pad may contribute to velopharyngeal closure in susceptible cleft/craniofacial patients. Adenoid surgery therefore requires speech-risk assessment and, when indicated, a tailored technique that treats obstruction without unnecessarily unmasking or worsening VPI.",
["Correct. Craniofacial ENT care requires one integrated plan for airway, resonance and hearing.","Palate repair does not eliminate reliance on adenoid tissue for closure in every child.","A cleft history changes risk but does not prohibit treatment of meaningful nasal obstruction.","Tubes manage middle-ear ventilation; they do not correct nasal obstruction or structural VPI."],
"In cleft care, an operation in one compartment can change function in another—especially adenoids, palate and middle ear.","What preoperative speech findings would make you especially cautious about complete adenoidectomy?","OR_prep"),

_q("v246_ped_croup_epi_fnd","Croup vs Epiglottitis","foundation",
"A 2-year-old has a barking cough, hoarseness and inspiratory stridor after two days of viral upper-respiratory symptoms. He is comfortable enough to drink and has no drooling. Which diagnosis is most likely?",
["Viral croup","Epiglottitis","Retropharyngeal abscess","Bacterial tracheitis with impending respiratory failure"],0,
"Barking cough, hoarseness and inspiratory stridor after a viral prodrome are classic for croup. Epiglottitis more often produces toxic appearance, severe odynophagia/dysphagia, drooling and reluctance to lie down, often without a barking cough.",
["Correct. The symptom cluster localizes inflammation to the subglottic/laryngotracheal airway typical of croup.","Epiglottitis usually presents with prominent swallowing pain, drooling and toxicity rather than a classic bark.","Retropharyngeal infection more often produces fever, neck stiffness/torticollis and dysphagia.","Bacterial tracheitis can follow a viral illness but typically causes a much sicker child with progressive airway toxicity and poor response to standard croup therapy."],
"Croup barks; epiglottitis drools. The deeper skill is recognizing which child is safe to examine and which airway you must not agitate.","Which bedside sign tells you croup severity has progressed beyond a mild outpatient phenotype?"),
_q("v246_ped_croup_epi_app","Croup vs Epiglottitis","application",
"An unimmunized 4-year-old has high fever, severe sore throat, drooling, muffled voice and tripod positioning with inspiratory stridor. He becomes more distressed when staff approach with a tongue depressor. What is the best immediate action?",
["Keep the child calm and upright, summon anesthesia/ENT for controlled airway management, and avoid provocative pharyngeal examination or unnecessary imaging","Force an oropharyngeal examination to visualize the epiglottis before calling the airway team","Send the child alone for lateral neck radiography before treatment","Give oral dexamethasone and discharge if stridor transiently improves"],0,
"This is a high-risk epiglottitis/supraglottitis phenotype. Agitation or forced examination can precipitate complete obstruction; airway planning takes precedence over diagnostic proof in an unstable child.",
["Correct. Controlled airway management with minimal agitation is the priority.","Provocative examination outside a controlled airway environment can trigger catastrophic obstruction.","Imaging should not delay or destabilize a child whose clinical picture already signals a threatened airway.","Standard croup therapy is not adequate management for suspected epiglottitis with drooling, tripod posture and toxicity."],
"When epiglottitis is clinically threatening the airway, diagnosis is an airway-management problem—not an imaging contest.","How would your approach differ in a stable older child or adult with supraglottitis and no respiratory distress?","overnight_call"),
_q("v246_ped_croup_epi_snr","Croup vs Epiglottitis","senior_decision",
"A child treated for presumed severe croup has persistent high fever, toxic appearance, thick secretions and worsening stridor despite dexamethasone and repeated nebulized epinephrine. What is the best escalation?",
["Reconsider bacterial tracheitis or another dangerous airway diagnosis and move toward controlled endoscopic airway evaluation/intubation with cultures and IV antibiotics as indicated","Continue endless nebulized epinephrine because all stridor in this age group is viral croup","Discharge once the heart rate normalizes","Order outpatient allergy testing before changing the diagnosis"],0,
"Failure of appropriate croup therapy plus toxicity and copious secretions should trigger diagnostic reassessment. Bacterial tracheitis can cause rapid obstruction from inflamed mucosa and purulent debris and may require intubation, bronchoscopic toilet/culture and antibiotics.",
["Correct. A senior clinician must recognize when the initial syndrome no longer explains the trajectory.","Repeated rescue medication without reassessment can delay definitive airway control in bacterial disease.","Physiologic normalization of one vital sign does not resolve progressive upper-airway obstruction.","Allergy testing has no role in the acute toxic airway."],
"The dangerous croup question is often not 'what is croup?' but 'when is this no longer croup?'","What endoscopic finding distinguishes bacterial tracheitis from isolated supraglottitis?","senior_management"),

_q("v246_ped_epi_fnd","Epiglottitis","foundation",
"A child with suspected epiglottitis has drooling, severe odynophagia and a preference to sit upright. Why is minimizing agitation so important?",
["A critically narrowed inflamed supraglottic airway can obstruct abruptly with distress or instrumentation","Agitation permanently worsens middle-ear pressure","Crying converts viral infection into bacterial infection","Supine positioning causes aspiration in every child regardless of airway disease"],0,
"Inflamed supraglottic tissues can leave very little airway reserve. Crying, forced supine positioning or instrumentation can increase dynamic obstruction, so the child should remain in the position of comfort while a controlled airway plan is assembled.",
["Correct. The concern is sudden loss of a marginal supraglottic airway.","Middle-ear pressure is unrelated to the immediate risk.","Agitation does not change the microbiology of the infection.","Aspiration is not inevitable in all children; the key danger here is abrupt upper-airway obstruction."],
"With suspected pediatric epiglottitis, the first therapeutic intervention may be simply not making the airway worse.","Why did widespread Hib vaccination change, but not eliminate, the differential diagnosis of supraglottitis?"),
_q("v246_ped_epi_app","Epiglottitis","application",
"A child with clear clinical epiglottitis is taken to the operating room because of progressive respiratory distress. What is the safest airway principle?",
["Secure the airway in a controlled setting with experienced anesthesia and ENT support, maintaining spontaneous ventilation when appropriate until the airway is obtained and having a surgical-airway rescue plan","Paralyze immediately in an unprepared ward room before confirming that ventilation is possible","Perform repeated bedside laryngoscopy attempts by inexperienced staff","Delay airway control until antibiotics have had several hours to work"],0,
"A threatened epiglottic airway should be managed by the most experienced available team in a setting with advanced airway and surgical rescue capability. The exact anesthetic technique is individualized, but loss of spontaneous ventilation before a secure plan can be hazardous in critical obstruction.",
["Correct. Preparation, expertise and rescue capability are central to safe airway control.","Unplanned paralysis can convert partial obstruction into a cannot-ventilate/cannot-intubate emergency.","Repeated traumatic attempts worsen edema and waste limited airway reserve.","Antibiotics are essential but do not act quickly enough to replace airway control in progressive distress."],
"In epiglottitis, airway technique is less about a single magic device than about preserving options until the airway is secure.","What equipment and personnel should be immediately available if oral intubation fails?","OR_prep"),
_q("v246_ped_epi_snr","Epiglottitis","senior_decision",
"After intubation for epiglottitis, a child is hemodynamically stable and cultures are pending. Which ongoing plan is most appropriate?",
["Give IV antibiotics active against likely respiratory pathogens, monitor in intensive care, and extubate only after clinical improvement and evidence that supraglottic edema has sufficiently resolved","Extubate immediately because placement of the tube proves the airway is now safe","Stop antibiotics if the first culture is negative","Keep the child intubated for a fixed 7 days regardless of airway examination or clinical trajectory"],0,
"Definitive treatment combines airway protection with antimicrobial therapy and reassessment of edema. Extubation is a physiologic decision based on improving infection and airway caliber, not a preset clock or the fact that intubation was initially successful.",
["Correct. Airway protection, appropriate antibiotics and objective clinical improvement guide safe liberation from the tube.","The inflammatory airway can remain critically narrowed after initial stabilization.","Cultures can be negative after prior antibiotics or because sampling is limited; management follows the clinical syndrome as well as microbiology.","A rigid duration ignores both rapid improvement and persistent edema; extubation timing should be individualized."],
"The senior endpoint is not 'infection treated'; it is 'the child can safely maintain the airway without the tube.'","What signs of persistent edema or difficult reintubation risk would make you postpone extubation?","senior_management"),
]


def apply_learning_ladders_v246(challenges, concept_id_fn):
    existing={q.get("id") for q in challenges}
    added=[]
    for src in VIGNETTES_V246:
        if src["id"] in existing:
            continue
        q=dict(src)
        q["concept_id"]=concept_id_fn(q["domain"],q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added.append(q["id"])
    return {"added":len(added),"ids":added}
