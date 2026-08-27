"""v24.2 — Pediatric Otolaryngology deliberate ladder pass 2.

Five exact canonical topics emphasizing boards, overnight-call decisions, airway
endoscopy, adenotonsillar risk stratification, and common pediatric ear disease.
"""
DOMAIN="Pediatric Otolaryngology"

def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}

VIGNETTES_V242=[
_q("v242_ped_osa_fnd","Pediatric OSA / Adenotonsillar Disease","foundation",
"A 6-year-old snores nightly, has witnessed apneas and daytime behavioral problems. Tonsils are 3+, but the family asks whether tonsil size alone proves obstructive sleep apnea. Which statement is most accurate?",
["OSA is a physiologic diagnosis; symptoms and anatomy raise suspicion, while polysomnography defines sleep-disordered breathing when objective severity is needed","Tonsil size alone establishes OSA severity","Any child who snores has severe OSA","A normal awake oxygen saturation excludes OSA"],0,
"Adenotonsillar hypertrophy is common in pediatric OSA, but awake anatomy does not reliably quantify sleep physiology. PSG is the gold-standard objective test when diagnosis or severity matters.",
["Correct. Tonsil size contributes to the phenotype but does not replace sleep physiology.","Large tonsils can coexist with mild disease or multilevel obstruction, so size alone does not grade severity.","Primary snoring and OSA are not equivalent, and severity cannot be inferred from snoring alone.","Children with clinically important OSA can have normal oxygen saturation while awake."],
"Snoring is a symptom; PSG measures physiology; anatomy explains where obstruction may occur.","Which comorbid children merit a lower threshold for preoperative PSG?"),
_q("v242_ped_osa_app","Pediatric OSA / Adenotonsillar Disease","application",
"A 2-year-old with severe PSG-confirmed OSA is scheduled for adenotonsillectomy. What perioperative decision is most important beyond choosing the tonsil technique?",
["Plan postoperative monitored admission because young age and severe OSA increase respiratory-complication risk","Discharge routinely from PACU if the tonsils were removed without bleeding","Avoid perioperative dexamethasone in every child","Prescribe codeine for breakthrough pain"],0,
"Postoperative disposition is a major safety decision. Young age, severe OSA and important comorbidities increase risk of obstruction, hypoxemia and opioid sensitivity after adenotonsillectomy.",
["Correct. Risk-stratified postoperative monitoring can be more important than the specific dissection tool.","An uncomplicated operation does not eliminate delayed respiratory risk in severe OSA.","A single perioperative dexamethasone dose is standard evidence-based care unless a patient-specific contraindication exists.","Codeine should not be used after pediatric tonsillectomy because variable CYP2D6 metabolism can cause life-threatening opioid toxicity."],
"The chief-level adenotonsillectomy question is often not 'how do I remove the tonsil?' but 'who is unsafe for routine discharge?'","How do obesity, Down syndrome, craniofacial disease, neuromuscular weakness, or hypoventilation change postoperative planning?","overnight_call"),
_q("v242_ped_osa_snr","Pediatric OSA / Adenotonsillar Disease","senior_decision",
"A child remains symptomatic six months after technically successful adenotonsillectomy, and repeat PSG confirms persistent OSA. What is the best senior-level approach?",
["Re-phenotype the residual obstruction and comorbid drivers, then choose targeted therapy such as weight management, CPAP, medical nasal therapy, DISE-directed surgery, or other site-specific treatment","Repeat tonsillectomy automatically without localization","Assume persistent symptoms are behavioral because adenotonsillectomy cures all pediatric OSA","Perform tracheostomy as the routine next step"],0,
"Persistent pediatric OSA is often multilevel or driven by obesity, craniofacial restriction, tongue-base/supraglottic collapse, nasal disease or neuromuscular factors. Reassessment should identify the residual mechanism before another operation.",
["Correct. Persistent OSA is a localization and phenotype problem, not an automatic repeat-surgery problem.","Repeat tonsil surgery is inappropriate when the tonsillar tissue is no longer the dominant obstruction.","Adenotonsillectomy is first-line for many children but does not cure every phenotype.","Tracheostomy is reserved for selected severe refractory circumstances, not routine residual OSA."],
"Residual OSA requires a new anatomic and physiologic hypothesis.","When is DISE most useful, and when would CPAP be preferable to another operation?","senior_management"),

_q("v242_ped_fb_fnd","Pediatric Airway Foreign Body","foundation",
"A toddler suddenly chokes while eating peanuts, then develops persistent unilateral wheeze. Chest radiographs are read as normal. What is the most important diagnostic principle?",
["A convincing choking history can justify airway endoscopy despite normal radiographs because many aspirated objects are radiolucent","Normal radiographs exclude an airway foreign body","Unilateral wheeze in a toddler is always asthma","Wait for fever before considering bronchoscopy"],0,
"Radiolucent foreign bodies may not be seen directly on plain films, and secondary findings such as air trapping can also be absent. History and persistent focal findings can outweigh normal imaging.",
["Correct. Normal imaging does not safely overrule a high-probability aspiration history.","Many organic foreign bodies are radiolucent and can be missed on plain films.","Abrupt onset after choking with focal wheeze is much more concerning for aspiration than new isolated asthma.","Retained foreign bodies can cause morbidity before infection develops."],
"Sudden choking + persistent focal respiratory findings = foreign body until convincingly excluded.","What inspiratory/expiratory or decubitus radiographic findings can indirectly suggest unilateral bronchial obstruction?"),
_q("v242_ped_fb_app","Pediatric Airway Foreign Body","application",
"A stable 3-year-old has high suspicion for a retained bronchial foreign body. What is the preferred definitive removal strategy?",
["Controlled rigid bronchoscopy with a shared surgeon-anesthesiologist ventilation and rescue plan","Blind finger sweep under sedation","Repeated outpatient albuterol trials before endoscopy","Flexible nasolaryngoscopy of the nose only"],0,
"Rigid bronchoscopy provides a ventilating working airway, optical control and extraction instruments and remains the definitive pediatric platform for most retained lower-airway foreign bodies.",
["Correct. Rigid bronchoscopy combines airway control and extraction capability.","Blind sweeps can push an object distally or traumatize the airway and are inappropriate for a retained bronchial object.","Bronchodilators do not remove the mechanical cause and delay can increase inflammation and granulation.","Nasal/laryngeal flexible examination cannot remove or adequately assess a suspected distal bronchial foreign body."],
"Before induction, explicitly discuss how you will ventilate, retrieve the object, and respond if partial obstruction becomes complete.","How do friable organic objects, sharp objects, or a proximal object near the glottis change extraction technique?","OR_prep"),
_q("v242_ped_fb_snr","Pediatric Airway Foreign Body","senior_decision",
"During rigid bronchoscopy, a friable nut is removed from the right mainstem bronchus. Oxygenation improves, but there was marked granulation around the object. What should the team do before concluding the case?",
["Reinspect the tracheobronchial tree when safe for residual fragments, a second object, mucosal injury and complications, then plan follow-up based on the degree of inflammation","End the procedure immediately after the first visible fragment is removed without reassessment","Perform prophylactic thoracotomy in every case","Assume persistent postoperative wheeze always means asthma"],0,
"Fragmentation and multiple objects are recognized risks, especially with organic material. A deliberate final inspection reduces missed retained material and identifies injury or distal disease that changes postoperative care.",
["Correct. Extraction is not complete until the airway has been reassessed for residual or additional pathology.","Stopping after one fragment risks leaving retained material behind.","Thoracotomy is not routine when endoscopic removal is successful and the airway is stable.","Persistent symptoms after removal can reflect residual foreign body, edema, granulation, atelectasis or pneumothorax and require reassessment before labeling asthma."],
"A successful foreign-body case ends with a second look, not merely with an object in the specimen cup.","What postoperative findings would trigger repeat bronchoscopy or chest imaging?","senior_management"),

_q("v242_ped_sgs_fnd","Pediatric Subglottic Stenosis","foundation",
"A former premature infant with a prolonged intubation history has recurrent biphasic stridor and repeated extubation failure. Which evaluation definitively characterizes suspected subglottic stenosis?",
["Direct microlaryngoscopy and bronchoscopy with airway sizing and assessment of length, scar character, glottis and distal airway","CT alone without endoscopy","A routine lateral neck radiograph alone","Tonsil examination alone"],0,
"Endoscopic evaluation directly defines lumen size, length, maturity, circumferential scar, vocal-fold/posterior-glottic status and associated tracheal disease. Imaging can complement but not replace operative airway characterization.",
["Correct. Surgical planning depends on direct sizing and full-airway characterization.","CT may show framework and length but cannot provide the same functional sizing and mucosal assessment.","Plain radiography is insufficient for definitive grading and operative planning.","Tonsil anatomy does not characterize the subglottis."],
"Myer-Cotton grade matters, but length, maturity, framework and multilevel disease choose the operation.","Why can two children with the same percentage obstruction require different operations?"),
_q("v242_ped_sgs_app","Pediatric Subglottic Stenosis","application",
"A child has a short, thin, immature subglottic scar with a stable cartilaginous framework and no major glottic disease. Which management strategy is most reasonable before open reconstruction?",
["Selected endoscopic scar incision/dilation with appropriate adjuncts and interval reassessment","Immediate total laryngectomy","Repeated circumferential thermal ablation of the entire subglottis","Observation indefinitely despite recurrent clinically important obstruction"],0,
"Favorable short, soft or immature stenosis can respond to endoscopic therapy. Long, thick, circumferential or framework-level disease is less likely to be durably managed this way and shifts the discussion toward open reconstruction.",
["Correct. Lesion morphology, not grade alone, determines whether an endoscopic trial is sensible.","Total laryngectomy is not an appropriate treatment for routine pediatric benign SGS.","Circumferential thermal injury can worsen fibrosis and stenosis.","Clinically important recurrent obstruction warrants treatment rather than indefinite observation."],
"Endoscopic therapy is best for favorable scar; repeated low-value dilations should not postpone definitive reconstruction indefinitely.","What pattern of recurrence would make you stop repeating endoscopic procedures and discuss LTR or CTR?","OR_prep"),
_q("v242_ped_sgs_snr","Pediatric Subglottic Stenosis","senior_decision",
"A tracheostomy-dependent child has severe mature high-grade subglottic stenosis. Endoscopy shows a stable glottis but a thick cricoid-level scar. How should the chief frame LTR versus cricotracheal resection and staging?",
["Use stenosis length and maturity, cartilage framework, distance from the vocal folds, comorbidities and ability to safely rely on the reconstructed airway to choose expansion versus resection and single- versus double-stage reconstruction","Choose solely from Myer-Cotton grade","Perform single-stage reconstruction in every child to shorten hospitalization","Leave the tracheostomy permanently without considering reconstructive candidacy"],0,
"LTR expands a stenotic framework; CTR removes a severe mature segment. The choice and staging depend on anatomy plus pulmonary, neurologic, swallowing and multilevel-airway factors that determine whether immediate airway dependence on the reconstruction is safe.",
["Correct. Reconstruction is an anatomic and physiologic decision, not a one-number algorithm.","Myer-Cotton grade alone ignores length, scar maturity, framework and glottic proximity.","Single-stage reconstruction is unsafe when comorbidity or airway complexity requires a protective tracheostomy/stent strategy.","Some children are poor reconstruction candidates, but permanent tracheostomy should follow deliberate assessment rather than default abandonment of airway rehabilitation."],
"Single versus double stage is fundamentally a question of whether the child can safely depend on the reconstructed airway immediately.","How do aspiration, pulmonary reserve, active infection, tracheomalacia, or vocal-fold dysfunction affect reconstruction timing and decannulation probability?","senior_management"),

_q("v242_ped_lm_fnd","Laryngomalacia","foundation",
"An infant has inspiratory stridor that worsens with feeding and supine positioning. Flexible laryngoscopy shows dynamic supraglottic collapse. Which finding most strongly changes the diagnosis from mild disease suitable for observation to severe disease requiring escalation?",
["Failure to thrive, apnea/cyanosis, significant retractions, hypoxemia or major feeding/aspiration morbidity","The stridor is loud","The epiglottis is omega-shaped but the infant feeds and grows normally","Symptoms improve when calm"],0,
"Laryngomalacia severity is defined by physiologic consequence, not acoustic intensity. Growth failure, hypoxemia, apnea/cyanosis and important feeding or cardiopulmonary consequences justify escalation.",
["Correct. Physiologic compromise defines severe laryngomalacia.","Loudness does not reliably correlate with dangerous obstruction.","An omega-shaped epiglottis can occur without severe physiology and does not by itself mandate surgery.","Improvement when calm is common and does not establish severe disease."],
"A noisy infant can be safe; a quieter infant with hypoxemia or growth failure may not be.","Which synchronous airway lesions should be sought when symptoms are atypical or unusually severe?"),
_q("v242_ped_lm_app","Laryngomalacia","application",
"An infant with laryngomalacia has poor weight gain, recurrent cyanotic spells and significant retractions. What is the best next treatment principle?",
["Proceed with airway evaluation and a tailored supraglottoplasty after defining collapse pattern and synchronous lesions","Use acid suppression alone as definitive treatment regardless of reflux evidence","Observe until age five despite physiologic compromise","Perform tonsillectomy"],0,
"Severe laryngomalacia with cardiopulmonary, growth or feeding consequences is an accepted indication for supraglottoplasty. Operative evaluation also helps identify synchronous disease that can alter outcome.",
["Correct. This infant has severe physiology that warrants operative escalation rather than observation alone.","Reflux may coexist, but acid suppression does not correct dynamic supraglottic collapse and should not be automatic therapy without indication.","Waiting despite cyanosis and growth failure risks ongoing morbidity.","Tonsillectomy does not treat infant supraglottic collapse."],
"Supraglottoplasty is tailored to the collapse pattern; over-resection can trade obstruction for aspiration or stenosis.","Which aryepiglottic, arytenoid and epiglottic components can be selectively addressed at surgery?","OR_prep"),
_q("v242_ped_lm_snr","Laryngomalacia","senior_decision",
"A syndromic infant remains obstructed and aspirates after an appropriately performed supraglottoplasty. What is the best senior-level response?",
["Reassess the entire airway and swallow for residual supraglottic disease, synchronous lesions, multilevel collapse and neurologic or pulmonary contributors before planning revision or another airway strategy","Repeat exactly the same supraglottoplasty without reevaluation","Assume surgery can never help because the first operation did not cure symptoms","Place a cuffed tracheostomy solely to stop aspiration"],0,
"Failure after supraglottoplasty should trigger mechanism-based reassessment. Syndromic, neurologic and multilevel-airway disease predict less straightforward outcomes and may require targeted revision, treatment of another level, feeding intervention or occasionally tracheostomy.",
["Correct. Persistent symptoms require a new localization and physiology assessment.","Blind repetition risks added injury if the residual mechanism is elsewhere.","A first-operation failure does not prove that all targeted airway treatment is futile.","A tracheostomy cuff does not reliably prevent aspiration and should not substitute for defining the swallowing problem."],
"After failed supraglottoplasty, ask what was missed or what is multilevel—not simply whether more supraglottic tissue can be removed.","When would PSG, repeat MLB, FEES/VFSS, or DISE each add useful information?","senior_management"),

_q("v242_ped_ear_fnd","AOM / OME / Tympanostomy Decisions","foundation",
"A child has middle-ear fluid on otoscopy but no fever, otalgia or acute inflammatory symptoms. Which diagnosis best fits?",
["Otitis media with effusion","Acute otitis media","Acute mastoiditis","Otitis externa"],0,
"OME is middle-ear effusion without the acute inflammatory syndrome of AOM. AOM requires acute symptoms plus objective middle-ear inflammation, classically a bulging tympanic membrane or new non-OE otorrhea.",
["Correct. Fluid without acute infection symptoms is OME.","AOM requires acute inflammatory findings rather than effusion alone.","Mastoiditis includes postauricular inflammatory findings and represents a complication, not uncomplicated asymptomatic effusion.","Otitis externa is an external-canal process, typically with canal inflammation and tragal/pinna tenderness."],
"Do not collapse AOM and OME into the same diagnosis: infection and sterile/persistent effusion have different treatment pathways.","What otoscopic finding is more specific for AOM than tympanic-membrane erythema alone?"),
_q("v242_ped_ear_app","AOM / OME / Tympanostomy Decisions","application",
"A 4-year-old has bilateral OME persisting for more than three months with documented conductive hearing difficulty. What management is most appropriate?",
["Discuss tympanostomy tubes after confirming chronicity, hearing impact and developmental context","Give repeated systemic antibiotics until the effusion clears","Obtain temporal-bone CT routinely","Ignore the hearing loss because OME is never clinically important"],0,
"Chronic bilateral OME with hearing difficulty is a standard situation in which tympanostomy tubes can improve middle-ear ventilation and short-term hearing while the family weighs natural history and procedural risks.",
["Correct. Persistent bilateral effusion with hearing impact is a meaningful tube indication.","OME without acute bacterial infection does not improve reliably with repeated antibiotic courses and unnecessary exposure adds harm.","CT is not routine evaluation for uncomplicated OME.","Persistent conductive loss can affect listening, speech/language access and school function, especially in at-risk children."],
"Tube candidacy is driven by duration, hearing/symptom burden and developmental risk—not merely the presence of fluid on one visit.","How does an at-risk developmental profile or structural tympanic-membrane change alter the threshold for intervention?","clinic_decision"),
_q("v242_ped_ear_snr","AOM / OME / Tympanostomy Decisions","senior_decision",
"A child is referred for 'recurrent AOM' after multiple treated episodes, but both ears are aerated with no middle-ear effusion at the surgical-consult visit. The family expects tubes based only on episode count. What is the best senior-level counseling?",
["Explain that recurrent-AOM tube benefit is strongest when middle-ear effusion is present at candidacy assessment; without effusion, observation and reassessment during future episodes is often preferable","Place tubes automatically based on any historical episode count","Perform adenoidectomy and tonsillectomy in every child with recurrent AOM","Start chronic prophylactic systemic antibiotics indefinitely"],0,
"Current middle-ear status matters. Recurrent AOM without effusion at assessment often reflects favorable Eustachian-tube function between episodes and does not carry the same evidence for immediate tube placement as recurrent AOM with persistent effusion.",
["Correct. The decision integrates episode history with objective effusion at the time of candidacy assessment.","Episode count alone can lead to unnecessary surgery when the middle ear is currently normal.","Adenotonsillectomy is not a universal treatment for recurrent AOM; adenoidectomy has selective age- and symptom-dependent roles.","Long-term systemic antibiotic prophylaxis creates adverse effects and resistance and is not routine modern management."],
"For recurrent AOM, ask what the middle ear looks like today—not only how many antibiotic prescriptions occurred last year.","When do age, adenoid symptoms, repeat tube need, speech/language risk or craniofacial disease change the plan?","senior_management")]

def apply_learning_ladders_v242(challenges,item_id_fn):
    existing={q.get("id") for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V242:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v242 orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
