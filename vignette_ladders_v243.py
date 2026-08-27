"""v24.3 — Pediatric Otolaryngology deliberate ladder pass 3.

Five exact canonical airway topics: laryngotracheal cleft, pediatric tracheostomy/
decannulation, pediatric vocal-fold immobility, subglottic hemangioma, and
tracheomalacia/bronchomalacia.
"""
DOMAIN="Pediatric Otolaryngology"

def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}

VIGNETTES_V243=[
_q("v243_ped_cleft_fnd","Laryngotracheal Cleft","foundation",
"An infant has coughing, choking, cyanotic spells with feeds and recurrent pneumonias despite treatment for reflux. Which structural airway lesion should remain high on the differential?",
["Laryngotracheal cleft","Choanal atresia","Adenoid hypertrophy","Otitis media"],0,
"A posterior interarytenoid/laryngotracheal cleft permits swallowed material to enter the airway and can present with feeding-associated respiratory symptoms and recurrent pulmonary disease.",
["Correct. Feeding-triggered airway symptoms and recurrent pneumonia are classic clues to a cleft.","Choanal atresia causes nasal obstruction rather than aspiration during swallowing.","Adenoid hypertrophy does not create a direct larynx-esophagus communication.","Otitis media does not explain recurrent aspiration pneumonia."],
"Persistent feeding-associated aspiration deserves a structural-airway differential, not reflux labeling alone.","Why can a shallow type I cleft be missed on flexible examination?"),
_q("v243_ped_cleft_app","Laryngotracheal Cleft","application",
"A child with aspiration has a swallow study suggesting posterior laryngeal penetration, but office flexible laryngoscopy is nondiagnostic. What is the definitive anatomic evaluation when a laryngeal cleft is suspected?",
["Direct laryngoscopy and bronchoscopy with careful palpation of the interarytenoid region","CT chest alone","Empiric tonsillectomy","Observation until a severe pneumonia occurs"],0,
"Direct endoscopic examination with palpation is required because shallow clefts can be subtle and may not be reliably diagnosed by flexible visualization alone.",
["Correct. Palpation during direct laryngoscopy defines the posterior laryngeal defect.","Chest imaging may show consequences of aspiration but does not define a small laryngeal cleft.","Tonsil surgery does not diagnose the posterior larynx.","Delaying diagnosis risks repeated pulmonary injury."],
"A type I cleft is a palpation diagnosis as much as a visual diagnosis.","How do type II-IV defects extend relative to the cricoid and cervical trachea?","OR_prep"),
_q("v243_ped_cleft_snr","Laryngotracheal Cleft","senior_decision",
"A child with a type I cleft continues to aspirate and develop pneumonias despite optimized feeding therapy and appropriate thickening. What is the best escalation principle?",
["Discuss endoscopic cleft repair after confirming the cleft is a meaningful driver of aspiration and accounting for neurologic, pulmonary and swallowing comorbidity","Repeat feeding changes indefinitely despite recurrent lung injury","Perform tracheostomy solely because a cleft exists","Assume repair will cure all aspiration regardless of neurologic dysphagia"],0,
"Failure of well-executed conservative therapy with ongoing pulmonary morbidity supports repair in a symptomatic type I cleft, but outcomes depend on whether the cleft is the dominant aspiration mechanism.",
["Correct. Escalate when morbidity persists, while counseling that comorbid dysphagia may limit cure.","Repeated ineffective conservative care can permit preventable pulmonary injury.","Tracheostomy is not the routine treatment for an isolated type I cleft.","Neurologic or sensory dysphagia can persist after technically successful repair."],
"Repair the cleft when it matters clinically, but do not promise that closing anatomy cures every swallowing disorder.","What findings would make an open approach more likely than endoscopic repair?","senior_management"),

_q("v243_ped_trach_fnd","Pediatric Tracheostomy / Decannulation","foundation",
"Which statement best describes pediatric tracheostomy decannulation readiness?",
["It requires resolution or adequate control of the original indication plus a patent upper airway, manageable secretions, adequate respiratory reserve and safe sleep/ventilation physiology","It is determined by age alone","A normal chest radiograph alone is sufficient","Every child should be decannulated once daytime capping is tolerated for ten minutes"],0,
"Decannulation is a whole-airway and whole-child decision. Upper-airway patency, pulmonary reserve, secretion burden, swallowing/aspiration, ventilatory needs and sleep physiology all matter.",
["Correct. Decannulation readiness is multidimensional.","Chronologic age does not establish airway or pulmonary readiness.","Chest imaging cannot replace airway and physiologic assessment.","Brief daytime capping does not prove sustained sleep or respiratory safety."],
"A patent trachea is necessary but not sufficient for decannulation.","Which children warrant formal capped sleep assessment before decannulation?"),
_q("v243_ped_trach_app","Pediatric Tracheostomy / Decannulation","application",
"A tracheostomy-dependent child is being considered for decannulation after airway reconstruction. What is the most appropriate pre-decannulation strategy?",
["Confirm airway patency endoscopically and use a structured capping/physiologic assessment appropriate to the child, including sleep evaluation when indicated","Remove the tube without examining the airway","Upsize the tracheostomy immediately before removal","Ignore secretion burden and aspiration because they do not affect decannulation"],0,
"Direct airway assessment identifies residual stenosis, suprastomal collapse or granulation, while capping and selected sleep testing assess whether the child can maintain ventilation through the natural airway.",
["Correct. Anatomy and physiology should both support decannulation.","Unrecognized residual obstruction can make unplanned decannulation dangerous.","Upsizing does not prove readiness for natural-airway breathing.","Secretions and aspiration can cause decannulation failure despite adequate lumen size."],
"Before removing a pediatric trach, prove both the airway and the child can handle the work.","What suprastomal lesion commonly prevents successful capping despite an adequate distal airway?","OR_prep"),
_q("v243_ped_trach_snr","Pediatric Tracheostomy / Decannulation","senior_decision",
"A child has a widely patent reconstructed airway and tolerates daytime capping but repeatedly obstructs and hypercapnic-desaturates during sleep. What is the best senior-level interpretation?",
["Do not decannulate yet; identify and treat the sleep-related or multilevel obstruction/ventilatory problem rather than relying on daytime capping alone","Proceed because daytime capping overrides sleep physiology","Enlarge the already patent subglottis repeatedly","Assume the sleep study is irrelevant once endoscopy is normal"],0,
"Sleep can expose dynamic collapse, adenotonsillar obstruction, hypoventilation or reduced reserve that is not apparent while awake. Decannulation should wait until clinically important nocturnal failure is addressed.",
["Correct. Sleep physiology can reveal a real decannulation barrier despite good daytime performance.","Daytime tolerance does not guarantee safe sleep ventilation.","Further subglottic enlargement does not treat a different obstructive or ventilatory mechanism.","Normal static airway anatomy cannot exclude sleep-related physiologic failure."],
"Decannulation failure is often a localization problem: do not revise the segment that is already adequate.","When would DISE, adenotonsillar treatment, noninvasive ventilation or continued tracheostomy each be reasonable?","senior_management"),

_q("v243_ped_vfi_fnd","Pediatric Vocal Fold Immobility","foundation",
"A neonate has weak cry, stridor and feeding difficulty. Flexible laryngoscopy shows one vocal fold immobile in a paramedian position. What diagnosis best fits?",
["Unilateral vocal-fold immobility","Bilateral choanal atresia","Acute epiglottitis","Adenoid hypertrophy"],0,
"Unilateral vocal-fold immobility can cause weak cry, dysphonia and aspiration; bilateral immobility more often creates significant airway obstruction with a relatively preserved cry.",
["Correct. The laryngoscopic finding localizes the disorder to one vocal fold.","Choanal atresia is a nasal obstruction diagnosis.","Epiglottitis is an acute inflammatory syndrome, not isolated chronic fold immobility.","Adenoid disease does not immobilize a vocal fold."],
"Unilateral immobility is often a voice/swallow problem; bilateral immobility is often an airway problem.","Which birth, cardiac and neurologic histories are important causes?"),
_q("v243_ped_vfi_app","Pediatric Vocal Fold Immobility","application",
"A newborn has bilateral vocal-fold immobility with significant stridor and repeated desaturations. What is the immediate management priority?",
["Secure and stabilize the airway while evaluating central neurologic, iatrogenic and congenital causes and defining whether recovery is plausible","Observe indefinitely because bilateral immobility is harmless","Perform injection laryngoplasty as the universal emergency procedure","Treat with antibiotics alone"],0,
"Bilateral immobility can critically narrow the glottic airway. Stabilization precedes etiologic workup; some children recover, so irreversible glottic-widening procedures require careful timing.",
["Correct. Airway safety comes first, followed by cause and prognosis.","Bilateral glottic obstruction can be life-threatening.","Injection augmentation narrows rather than widens the glottic airway and is not the routine treatment for bilateral obstruction.","Antibiotics do not restore vocal-fold motion."],
"In bilateral immobility, first decide whether the child can breathe safely; then decide how much permanence you can accept in the airway solution.","When is brain/brainstem imaging particularly important?","overnight_call"),
_q("v243_ped_vfi_snr","Pediatric Vocal Fold Immobility","senior_decision",
"A child with persistent bilateral vocal-fold immobility remains tracheostomy-dependent after an adequate observation period and has no meaningful recovery. What should drive the next operation?",
["Balance decannulation benefit against voice and aspiration cost when considering posterior cordotomy, arytenoid-level procedures, reinnervation strategies or continued tracheostomy","Choose the widest possible glottic procedure regardless of function","Perform tonsillectomy as definitive treatment","Assume every child must remain tracheostomy-dependent forever"],0,
"Definitive intervention is a tradeoff: increasing posterior glottic airway may improve decannulation probability while worsening voice or swallowing. Age, etiology, recovery potential, aspiration and family goals matter.",
["Correct. The best airway is not simply the largest airway; function matters.","Over-widening can create avoidable dysphonia and aspiration.","Tonsillectomy does not restore glottic motion.","Selected children can be decannulated after appropriately chosen interventions."],
"The chief-level bilateral-VFI decision is airway versus voice/swallow—not procedure name alone.","How would severe baseline aspiration change the appetite for irreversible glottic widening?","senior_management"),

_q("v243_ped_sgh_fnd","Subglottic Hemangioma","foundation",
"An infant develops progressive biphasic stridor during the first months of life and has a segmental beard-distribution cutaneous hemangioma. Which airway lesion should be suspected?",
["Subglottic hemangioma","Adenoid hypertrophy","Peritonsillar abscess","Foreign body in the ear"],0,
"Subglottic hemangioma classically presents in infancy with progressive airway symptoms and is associated with segmental cervicofacial/beard-distribution hemangiomas.",
["Correct. Age, progressive biphasic stridor and hemangioma phenotype are classic.","Adenoids do not cause infant biphasic stridor.","Peritonsillar abscess is an acquired oropharyngeal infection.","An ear foreign body does not obstruct the subglottis."],
"Infant progressive biphasic stridor plus a beard hemangioma is a subglottic clue.","Which syndromic vascular-anomaly evaluation may be relevant in large segmental facial hemangiomas?"),
_q("v243_ped_sgh_app","Subglottic Hemangioma","application",
"Endoscopy confirms a symptomatic subglottic hemangioma causing significant but noncritical airway narrowing. What is the preferred modern first-line disease-directed therapy for most infants?",
["Systemic propranolol with appropriate cardiovascular/metabolic screening and monitoring","Routine open cricoid resection","Long-term antibiotics","Repeated blind dilation"],0,
"Beta-blocker therapy with propranolol has transformed management and is first-line for most clinically important infantile subglottic hemangiomas, with airway intervention reserved for instability or inadequate response.",
["Correct. Propranolol is the principal modern medical therapy for infantile hemangioma.","Open airway resection is not first-line for a typical responsive lesion.","Antibiotics do not involute a vascular tumor.","Dilation does not treat the vascular biology and can injure the airway."],
"Treat the hemangioma biology, not just the diameter of the airway.","What heart-rate, blood-pressure, feeding and hypoglycemia precautions matter with propranolol?","boards"),
_q("v243_ped_sgh_snr","Subglottic Hemangioma","senior_decision",
"An infant with a known subglottic hemangioma develops worsening retractions and repeated desaturations despite medical therapy. What is the best escalation principle?",
["Reassess airway severity urgently and secure the airway if needed while determining whether adjunctive endoscopic treatment, alternative medical therapy or tracheostomy is required","Continue the same outpatient plan regardless of respiratory compromise","Perform repeated traumatic dilation","Wait for spontaneous involution despite hypoxemia"],0,
"Progressive physiologic compromise overrides routine outpatient management. Airway stabilization and updated endoscopic assessment guide rescue therapy while ongoing hemangioma treatment is optimized.",
["Correct. Respiratory physiology determines urgency.","Desaturation and worsening work of breathing require escalation.","Traumatic dilation can worsen bleeding and scarring without treating the lesion.","Natural involution is not a safe strategy during clinically important obstruction."],
"A hemangioma can be medically responsive and still become an airway emergency.","Which findings would make tracheostomy or operative debulking reasonable despite propranolol?","overnight_call"),

_q("v243_ped_tm_fnd","Tracheomalacia / Bronchomalacia","foundation",
"A child has recurrent expiratory wheeze, barking cough and episodes of airway collapse that worsen with agitation and infection. Bronchoscopy shows dynamic expiratory narrowing of the trachea. What is the diagnosis?",
["Tracheomalacia","Fixed subglottic stenosis","Choanal atresia","Otitis externa"],0,
"Tracheomalacia is excessive dynamic collapse of the tracheal lumen, often most apparent during expiration or cough; bronchomalacia involves the bronchi.",
["Correct. Dynamic expiratory collapse defines the mechanism.","Fixed SGS does not characteristically vary with expiration.","Choanal atresia is nasal obstruction.","Otitis externa is unrelated to intrathoracic airway collapse."],
"Stridor/wheeze is not always fixed stenosis: dynamic disease changes with the respiratory cycle.","Why can a static bronchoscopy under deep anesthesia underestimate or alter malacia?"),
_q("v243_ped_tm_app","Tracheomalacia / Bronchomalacia","application",
"A child with moderate tracheomalacia has recurrent symptoms but no life-threatening events and is growing adequately. What is the best management principle?",
["Treat contributing pulmonary/reflux/secretory issues, use airway-clearance and positive-pressure support when indicated, and reserve surgery for severe persistent physiologic compromise","Perform aortopexy in every child with any collapse","Use repeated airway dilation","Treat as bacterial croup indefinitely"],0,
"Many children improve with growth and supportive management. Positive pressure can pneumatic-stent the airway; surgery is selected for severe disease with recurrent life-threatening or ventilation-limiting collapse.",
["Correct. Treatment intensity should match physiologic severity.","Not every degree of malacia requires surgery.","Dilation is not a durable treatment for dynamic wall collapse.","Chronic antibiotics do not correct airway mechanics."],
"Manage the physiology first; reserve structural surgery for structural failure that remains clinically important.","When can CPAP or PEEP function as a pneumatic stent?","boards"),
_q("v243_ped_tm_snr","Tracheomalacia / Bronchomalacia","senior_decision",
"A child has recurrent life-threatening airway-collapse events despite optimized medical and positive-pressure support. Imaging and dynamic bronchoscopy show severe anterior vascular compression with posterior membranous intrusion. What should guide operative planning?",
["Match the operation to the mechanism—such as aortopexy for anterior compression and posterior tracheopexy when posterior membrane intrusion is dominant—using multidisciplinary airway/cardiothoracic evaluation","Perform identical surgery for every malacia phenotype","Repeatedly dilate the trachea","Assume tracheostomy always cures distal malacia"],0,
"Severe malacia surgery is mechanism-specific. Dynamic bronchoscopy and vascular imaging identify whether anterior compression, posterior membrane intrusion or multilevel bronchial collapse dominates and therefore which intervention is rational.",
["Correct. Operative choice follows the dynamic mechanism.","Different collapse patterns require different strategies.","Dilation does not correct unsupported dynamic airway walls.","A tracheostomy may bypass proximal disease or provide ventilation but does not necessarily eliminate distal tracheobronchial collapse."],
"For severe malacia, do not operate on the word 'malacia'; operate on the observed collapse mechanism.","How would distal bronchomalacia or complex congenital heart disease change the expected benefit of tracheopexy?","OR_prep")]

def apply_learning_ladders_v243(challenges,item_id_fn):
    existing={q.get("id") for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V243:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v243 orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
