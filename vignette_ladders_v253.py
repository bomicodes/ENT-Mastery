"""v25.3 — Laryngology / Voice / Swallowing deliberate ladder pass 4.

Closes five swallowing-focused canonical concepts with explicit foundation ->
application -> senior-decision ladders. Zenker/cricopharyngeal management is
aligned with the established OR Tomorrow decision framework rather than
creating a competing procedure model.
"""
DOMAIN = "Laryngology / Voice / Swallowing"


def _q(qid, topic, stage, stem, choices, answer, explanation, reasons, pearl,
       curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": reasons,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True, "_coverage_reviewed_v211": True,
    }


VIGNETTES_V253 = [
    _q("v253_lar_fees_fnd", "FEES", "foundation",
       "A patient with dysphagia needs bedside assessment of secretion management, laryngeal sensation, pharyngeal residue, penetration, and aspiration across repeated trials without radiation. Which study best fits?",
       ["Flexible endoscopic evaluation of swallowing (FEES)", "Routine barium esophagram", "Noncontrast neck CT", "Esophageal manometry alone"], 0,
       "FEES directly visualizes the pharynx and larynx before and after the swallow, including secretions, residue, penetration/aspiration, and response to strategies; it can be repeated at bedside without ionizing radiation.",
       ["Correct. FEES is particularly strong for secretion burden, airway protection, residue, sensory observations, and repeated bedside testing.", "An esophagram is useful for structural/esophageal questions but does not provide the same direct laryngeal secretion and airway-protection assessment.", "Static CT does not test swallowing physiology.", "Manometry measures pressure physiology and cannot replace direct assessment of airway invasion and residue."],
       "FEES is not simply 'MBS without radiation'; its unique strengths are direct laryngeal visualization, secretions, repeatability, and bedside access.",
       "What key portion of the actual swallow is briefly obscured by white-out?"),
    _q("v253_lar_fees_app", "FEES", "application",
       "After stroke, FEES shows pooled secretions entering the laryngeal vestibule, reduced sensation, aspiration after the swallow from pyriform residue, and improvement with a head turn. What is the most useful interpretation?",
       ["The study has identified both a physiologic airway-protection problem and a compensatory strategy that should inform supervised diet/therapy planning", "The aspiration proves the patient must permanently remain NPO", "The head turn is irrelevant because FEES cannot assess treatment response", "Aspiration after the swallow proves a primary oral-phase disorder"], 0,
       "Instrumental swallowing assessment should localize why aspiration occurs and test whether a maneuver changes safety or efficiency. Post-swallow aspiration from residue points to pharyngeal clearance/airway-protection physiology rather than automatically mandating permanent NPO status.",
       ["Correct. FEES can connect mechanism, airway consequence, and immediate response to a compensatory maneuver.", "NPO decisions require the entire clinical context; one aspiration event does not by itself define a permanent feeding plan.", "Testing strategies during FEES is a major clinical strength.", "Post-swallow aspiration from pharyngeal residue does not localize primarily to the oral phase."],
       "Do not stop at PAS-style labeling; ask when aspiration occurs, from what residue, why, and whether a strategy changes it.",
       "How would severe silent secretion aspiration despite no oral intake change your assumptions about what a feeding tube can accomplish?", "senior_management"),
    _q("v253_lar_fees_snr", "FEES", "senior_decision",
       "A patient with persistent dysphagia has repeated bedside FEES showing good laryngeal closure but suspected impaired upper-esophageal-sphincter opening and retrograde flow. What is the best next step?",
       ["Obtain a fluoroscopic swallow/esophageal study appropriate to the question because FEES cannot directly visualize bolus transit through the UES during white-out", "Repeat FEES indefinitely because it visualizes the cervical esophagus better than fluoroscopy", "Schedule cricopharyngeal myotomy from FEES alone", "Assume the symptoms are functional because aspiration was not seen"], 0,
       "A senior interpretation recognizes test limitations. FEES is excellent for pharyngeal/laryngeal findings but does not directly show the bolus traversing the UES; suspected UES or esophageal pathology often needs complementary fluoroscopy and, selectively, esophageal testing.",
       ["Correct. Choose the next study to answer the unresolved physiologic question rather than repeating a test with the same blind spot.", "FEES does not directly visualize cervical-esophageal bolus transit through the UES.", "Permanent UES surgery requires stronger physiologic localization than this FEES finding alone.", "Absence of aspiration does not exclude clinically important dysphagia or UES dysfunction."],
       "FEES and MBS are complementary; the senior move is knowing which unresolved question belongs to which test.",
       "When might manometry add value after fluoroscopy still leaves the UES mechanism uncertain?", "senior_management"),

    _q("v253_lar_mbs_fnd", "Modified Barium Swallow", "foundation",
       "Which test best evaluates oral and pharyngeal bolus flow dynamically while showing timing of airway invasion and upper-esophageal-sphincter opening during different consistencies?",
       ["Modified barium swallow / videofluoroscopic swallow study", "FEES only", "Routine chest radiograph", "Laryngeal EMG"], 0,
       "MBS/VFSS dynamically evaluates oral and pharyngeal swallowing under fluoroscopy and can show bolus timing, penetration/aspiration, residue, hyolaryngeal excursion, and UES opening while testing compensations.",
       ["Correct. Fluoroscopy provides a dynamic lateral view of bolus transit from oral preparation through the pharynx and UES.", "FEES is complementary but does not directly visualize the bolus during the moment of pharyngeal white-out or through the UES.", "A chest radiograph cannot localize swallowing physiology.", "Laryngeal EMG evaluates neuromuscular function, not bolus transit."],
       "MBS answers a motion-and-timing question; an esophagram answers a different structural/esophageal question even though both use contrast.",
       "Why is a brief esophageal screen during MBS not equivalent to a complete diagnostic esophagram?"),
    _q("v253_lar_mbs_app", "Modified Barium Swallow", "application",
       "MBS shows reduced hyolaryngeal excursion, poor pharyngeal constriction, diffuse residue, and limited UES opening rather than an isolated focal cricopharyngeal bar. What is the best interpretation before considering myotomy?",
       ["The UES finding may be secondary to global pharyngeal weakness, so rehabilitation and broader physiologic assessment are more appropriate than assuming isolated cricopharyngeal obstruction", "Any limited UES opening proves isolated cricopharyngeal achalasia", "Cricopharyngeal myotomy will restore pharyngeal contraction", "The study is nondiagnostic because aspiration is not mentioned"], 0,
       "UES opening depends on cricopharyngeal relaxation plus hyolaryngeal traction and upstream driving pressure. Global weakness can produce poor opening; cutting the sphincter does not restore absent pharyngeal propulsion.",
       ["Correct. The intervention must match the dominant physiology rather than a single fluoroscopic shape.", "Limited opening is not synonymous with isolated sphincter hypertonicity.", "Myotomy reduces sphincter resistance but cannot recreate pharyngeal contraction.", "MBS provides useful physiology even without aspiration."],
       "A CP bar is an image finding; an operation requires evidence that the UES is actually the limiting physiology.",
       "What additional testing would you consider if symptoms suggest distal esophageal obstruction despite an abnormal pharyngeal study?", "boards"),
    _q("v253_lar_mbs_snr", "Modified Barium Swallow", "senior_decision",
       "A frail patient aspirates thin liquids before the swallow because of delayed pharyngeal trigger but is safe with a tested strategy and has good pulmonary reserve. Family asks whether the fluoroscopic aspiration automatically requires a gastrostomy. What is the best response?",
       ["No; integrate frequency/mechanism of aspiration, effectiveness of tested strategies, nutrition/hydration, cognition, pulmonary reserve, goals, and secretion burden before choosing an enteral plan", "Yes; any aspiration on fluoroscopy mandates permanent tube feeding", "A gastrostomy will eliminate aspiration of saliva and refluxed material", "Ignore the study because aspiration can occur only after the swallow"], 0,
       "Instrumental findings inform but do not independently dictate feeding decisions. Tube feeding may support nutrition but does not abolish aspiration of secretions or reflux and must be weighed against realistic function and goals.",
       ["Correct. Senior swallowing decisions integrate physiology with clinical consequence and patient goals.", "There is no universal rule that one aspiration event requires permanent enteral feeding.", "A feeding tube does not eliminate secretion aspiration and may not eliminate reflux-related aspiration.", "Aspiration can occur before, during, or after the swallow, each implying different physiology."],
       "Treat the patient, not the fluoroscopic frame; aspiration severity is mechanism + frequency + consequence + modifiability.",
       "What findings would make continued oral intake unsafe despite compensatory strategies?", "senior_management"),

    _q("v253_lar_zenker_fnd", "Zenker Diverticulum", "foundation",
       "An older adult has progressive dysphagia, regurgitation of undigested food, halitosis, cough, and aspiration. Barium study shows a posterior hypopharyngeal pouch above the cricopharyngeus. What is the diagnosis?",
       ["Zenker diverticulum", "Achalasia of the distal esophagus", "Laryngocele", "Epiphrenic diverticulum"], 0,
       "Zenker diverticulum is a pulsion diverticulum through Killian dehiscence above the cricopharyngeus and is strongly associated with dysfunctional UES mechanics.",
       ["Correct. The symptom complex and posterior cervical pouch above the CP are classic for Zenker diverticulum.", "Distal achalasia produces a different level and physiologic pattern.", "A laryngocele is an air-filled dilation related to the laryngeal ventricle, not a food-retaining hypopharyngeal pouch.", "Epiphrenic diverticula arise distally near the diaphragm."],
       "Zenker is not just a pouch problem; the cricopharyngeal/septal muscle is central to durable treatment.",
       "Which anatomic weak area forms the pouch, and why does that matter during myotomy?"),
    _q("v253_lar_zenker_app", "Zenker Diverticulum", "application",
       "A patient with symptomatic Zenker diverticulum has severe cervical kyphosis, limited neck extension, and poor transoral rigid exposure. Which planning principle is best?",
       ["Choose among flexible endoscopic, Z-POEM-type, or open approaches based on pouch anatomy, exposure, comorbidity, and expertise rather than forcing rigid stapling", "Rigid stapling is mandatory for every Zenker diverticulum", "Excise the pouch without addressing the cricopharyngeus", "Observe indefinitely despite recurrent aspiration pneumonia because exposure is difficult"], 0,
       "Rigid transoral techniques require favorable exposure. Flexible endoscopic, tunneling, and open options permit individualized treatment while preserving the essential goal of an adequate septal/cricopharyngeal myotomy.",
       ["Correct. Exposure is part of candidacy, and alternate approaches should be planned before induction when rigid access may fail.", "Rigid exposure can be impossible or unsafe in unfavorable anatomy.", "Pouch treatment without adequate myotomy fails to address the driving UES dysfunction.", "Recurrent aspiration pneumonia is a meaningful morbidity that can justify treatment through another appropriate approach."],
       "For Zenker, the best approach is the one that safely achieves an adequate myotomy in that patient's anatomy—not the surgeon's favorite platform.",
       "How do very small pouches or very large pouches alter the technical pros and cons of different approaches?", "OR_prep"),
    _q("v253_lar_zenker_snr", "Zenker Diverticulum", "senior_decision",
       "Hours after Zenker diverticulotomy, a patient develops tachycardia, fever, increasing neck/chest pain, and cervical crepitus. What is the best next action?",
       ["Treat as possible pharyngoesophageal perforation with urgent evaluation, NPO status, IV antibiotics, and source-control planning based on clinical/imaging findings", "Reassure that this is expected odynophagia", "Advance to a regular diet to test the repair", "Give only an antacid and discharge"], 0,
       "Perforation and cervical/mediastinal contamination are high-consequence complications after Zenker intervention. Systemic signs, escalating pain, or crepitus demand prompt leak evaluation and management rather than routine postoperative reassurance.",
       ["Correct. Early recognition, contamination control, antibiotics, and selective drainage/repair are the priority.", "Progressive pain plus systemic signs and crepitus are not routine postoperative findings.", "Oral challenge can worsen contamination when a leak is suspected.", "Acid suppression alone does not address perforation or mediastinal infection."],
       "After Zenker surgery, fever + tachycardia + neck/chest pain or crepitus is a perforation problem until proven otherwise.",
       "Which stable contained leaks may be managed nonoperatively, and which findings mandate drainage or operative source control?", "overnight_call"),

    _q("v253_lar_cp_fnd", "Cricopharyngeal Dysfunction", "foundation",
       "A swallow study shows impaired opening at the upper esophageal sphincter. Which physiologic statement is most important before labeling isolated cricopharyngeal dysfunction?",
       ["UES opening depends on CP relaxation plus hyolaryngeal traction and pharyngeal driving force, so impaired opening can be secondary to broader swallowing weakness", "The cricopharyngeus alone determines every UES opening abnormality", "A visible CP bar always causes symptoms", "UES dysfunction is diagnosed only by laryngoscopy"], 0,
       "The UES opens through coordinated sphincter relaxation, anterior-superior laryngeal movement, and bolus-driving pressure. Poor opening therefore requires physiologic localization before treatment.",
       ["Correct. This prevents mistaking a downstream appearance for an isolated muscle problem.", "UES opening is a coordinated event, not a single-muscle switch.", "CP bars can be incidental and should be correlated with symptoms and bolus obstruction.", "Laryngoscopy alone does not demonstrate UES opening physiology."],
       "Do not operate on a CP bar; operate on clinically important, localized UES dysfunction.",
       "How can generalized pharyngeal weakness make a myotomy less effective?"),
    _q("v253_lar_cp_app", "Cricopharyngeal Dysfunction", "application",
       "A patient has focal bolus hold-up at the UES with otherwise strong pharyngeal propulsion and no distal obstruction. Symptoms improve substantially after dilation. What does that response suggest?",
       ["The UES is likely a meaningful limiting site, supporting consideration of repeat dilation, selected botulinum toxin, or durable myotomy depending on diagnosis and goals", "The response proves the problem is distal achalasia", "Dilation response excludes cricopharyngeal dysfunction", "A permanent feeding tube is now mandatory"], 0,
       "When physiology is otherwise favorable, improvement after a reversible UES-directed intervention supports the hypothesis that sphincter resistance contributes materially to symptoms and can inform whether durable treatment is worthwhile.",
       ["Correct. A reversible intervention can function as both therapy and patient-specific decision information.", "Improvement at the cervical UES does not establish distal LES achalasia.", "The response supports rather than excludes a meaningful UES component.", "Improved swallowing after dilation argues against reflexive permanent tube feeding."],
       "Dilation or botulinum toxin can be more than treatment—they can test whether lowering UES resistance actually helps this patient.",
       "What features would make you hesitate before a durable myotomy despite temporary benefit?", "boards"),
    _q("v253_lar_cp_snr", "Cricopharyngeal Dysfunction", "senior_decision",
       "A patient with severe neurodegenerative pharyngeal weakness has diffuse residue, poor airway protection, and only modest UES restriction. The team requests cricopharyngeal myotomy to 'fix the swallow.' What is the best decision?",
       ["Do not promise myotomy; the dominant problem is global pharyngeal/airway-protection failure, and lowering UES resistance may not restore safe propulsion", "Perform myotomy because any UES narrowing guarantees benefit", "Myotomy will restore laryngeal sensation", "Perform arytenoidectomy to improve swallowing"], 0,
       "Myotomy is most useful when excessive UES resistance is a major limiting physiology and upstream propulsion is capable of benefiting. Advanced global weakness changes both expected benefit and aspiration risk.",
       ["Correct. Match the operation to the dominant mechanism and counsel realistically about irreversible progression.", "A radiographic narrowing alone is not enough to predict benefit.", "Myotomy does not restore sensory function.", "Arytenoidectomy enlarges the glottic airway and can worsen airway protection."],
       "The senior question is not 'can I cut the CP?' but 'is the CP the bottleneck that is preventing an otherwise useful swallow?'",
       "When could a limited dilation or botulinum trial still be reasonable for symptom palliation?", "senior_management"),

    _q("v253_lar_asp_fnd", "Aspiration-Prevention Surgery", "foundation",
       "Which patient is most appropriate to begin discussing aspiration-prevention surgery?",
       ["A patient with severe, intractable aspiration causing recurrent pulmonary morbidity despite maximal rehabilitation and appropriate less-destructive measures", "A patient with one trace penetration event and no pneumonia", "Any patient receiving a gastrostomy", "A patient with isolated dysphonia and normal swallowing"], 0,
       "Aspiration-prevention operations are reserved for severe persistent airway contamination when rehabilitation and reversible strategies cannot provide adequate pulmonary protection. They intentionally trade voice and/or normal airway-swallow continuity for safety.",
       ["Correct. Recurrent clinically consequential aspiration despite maximal conservative care is the core indication framework.", "Minor penetration without clinical consequence does not justify irreversible airway-separating surgery.", "Gastrostomy status alone does not define aspiration severity or surgical candidacy.", "Isolated dysphonia is not an indication for aspiration-prevention surgery."],
       "These are function-sacrificing operations; the indication is pulmonary protection from otherwise uncontrollable aspiration, not an abnormal swallow-study image alone.",
       "Why can a feeding tube fail to stop aspiration pneumonia?"),
    _q("v253_lar_asp_app", "Aspiration-Prevention Surgery", "application",
       "A patient with a devastated, nonfunctional larynx after cancer treatment has chronic secretion aspiration, recurrent pneumonias, and cannot safely communicate by laryngeal voice. Which counseling principle is essential when considering laryngotracheal separation, laryngeal closure, or functional total laryngectomy?",
       ["Explain that the operations prioritize pulmonary protection and usually sacrifice normal laryngeal voice, so procedure choice must incorporate reversibility, anatomy, prior radiation, communication goals, and reconstruction risk", "Promise normal voice after every aspiration-prevention operation", "Assume prior radiation has no effect on wound risk", "Choose the operation solely from the PAS score"], 0,
       "Aspiration-prevention procedures differ in reversibility, fistula/wound risk, reconstructive burden, and communication options. In a radiated nonfunctional larynx, the decision is a goals-and-anatomy problem as much as a swallowing problem.",
       ["Correct. The benefit is airway protection; the tradeoffs include voice loss, stoma/airway changes, wound risk, and rehabilitation needs.", "Normal laryngeal voice is commonly sacrificed; alternative communication must be planned.", "Radiation materially changes healing and fistula risk.", "A single instrumental score cannot select an irreversible operation."],
       "Name the function being sacrificed before you name the operation being offered.",
       "How would salvage-radiation tissue quality influence your reconstruction and fistula-prevention plan?", "OR_prep"),
    _q("v253_lar_asp_snr", "Aspiration-Prevention Surgery", "senior_decision",
       "A neurologically impaired patient has repeated aspiration pneumonias despite tube feeding because of continuous salivary aspiration. Pulmonary reserve is worsening and recovery of useful laryngeal protection is not expected. What is the best senior-level framework?",
       ["Confirm that aspiration is the dominant driver of pulmonary morbidity, define goals and communication priorities, then consider an airway-separating/closure procedure if the expected pulmonary benefit outweighs irreversible functional loss", "Escalate tube feeding because it should eventually stop salivary aspiration", "Avoid discussing surgery because aspiration-prevention procedures are never appropriate in neurologic disease", "Perform a vocal-fold medialization without evaluating the broader aspiration mechanism"], 0,
       "Tube feeding does not prevent aspiration of saliva and may not prevent refluxate aspiration. In carefully selected patients with irreversible severe aspiration, airway separation can substantially reduce pulmonary contamination, but only after mechanism, prognosis, goals, and tradeoffs are explicit.",
       ["Correct. This is a mechanism- and goals-based irreversible decision, not a reflex to one pneumonia or one swallow result.", "Enteral feeding does not eliminate secretion aspiration.", "Neurologic disease can be an appropriate context when aspiration is severe, persistent, and unlikely to recover.", "Medialization may help selected glottic insufficiency but is not a universal solution for global secretion aspiration."],
       "A PEG changes the route of nutrition; aspiration-prevention surgery changes the route of the airway. Those are not equivalent interventions.",
       "What evidence would make you conclude that recurrent pneumonias are not primarily aspiration-driven and therefore unlikely to improve after airway separation?", "senior_management"),
]


def apply_learning_ladders_v253(challenges, item_id_fn):
    canonical_topics = {"FEES", "Modified Barium Swallow", "Zenker Diverticulum", "Cricopharyngeal Dysfunction", "Aspiration-Prevention Surgery"}
    existing = {q.get("id") for q in challenges}
    added = []
    for src in VIGNETTES_V253:
        if src["id"] in existing:
            continue
        q = dict(src)
        q["concept_id"] = item_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added.append(q["id"])
    return {"added": added, "count": len(added), "topics": sorted(canonical_topics)}
