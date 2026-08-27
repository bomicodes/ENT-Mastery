"""v24.9 — Laryngology / Voice / Swallowing deliberate ladder pass 1.

Begins canonical Laryngology closure with five high-yield resident/chief topics:
unilateral vocal-fold paralysis, dysphagia/aspiration, bilateral vocal-fold
immobility, subglottic/tracheal stenosis, and laryngeal anatomy. Each exact
canonical topic receives a foundation -> application -> senior-decision ladder.
"""
DOMAIN="Laryngology / Voice / Swallowing"


def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}


VIGNETTES_V249=[
_q("v249_lar_uvfp_fnd","Unilateral Vocal Fold Paralysis","foundation",
"A patient develops a breathy weak voice and cough with thin liquids after thyroid surgery. Flexible laryngoscopy shows one vocal fold immobile in a paramedian position. Which diagnosis best fits?",
["Unilateral vocal fold paralysis","Spasmodic dysphonia","Bilateral vocal fold paralysis","Muscle tension dysphonia"],0,
"New unilateral immobility after surgery along the recurrent-laryngeal-nerve course, with glottic insufficiency symptoms, is classic for unilateral vocal fold paralysis. The immediate clinical questions are airway safety, aspiration risk, cause, and likelihood of recovery.",
["Correct. Unilateral immobility with breathy dysphonia and liquid dysphagia after thyroid surgery is a classic UVFP presentation.","Spasmodic dysphonia causes task-specific involuntary voice breaks rather than a persistently immobile fold.","Bilateral paralysis more often threatens the airway and requires bilateral motion loss.","Muscle tension dysphonia can mimic dysphonia but does not explain true unilateral immobility."],
"UVFP is more than a voice diagnosis: assess swallowing and aspiration as well as glottic closure.","What operative history or cranial-neuropathy findings would make you suspect a more proximal vagal lesion?"),
_q("v249_lar_uvfp_app","Unilateral Vocal Fold Paralysis","application",
"A patient has new unexplained left vocal-fold paralysis with no recent neck surgery and no obvious laryngeal mass. What is the best next diagnostic principle?",
["Image the vagus and recurrent-laryngeal-nerve course from skull base through the mediastinum/aortic arch as appropriate rather than labeling it idiopathic","Observe indefinitely without etiologic evaluation","Image only the larynx because the recurrent laryngeal nerve never leaves the neck","Proceed directly to permanent framework surgery before defining cause or recovery potential"],0,
"Unexplained UVFP requires evaluation along the entire relevant vagal/RLN course. Left-sided paralysis especially warrants attention to the aorticopulmonary window and mediastinum because the left RLN loops under the aortic arch.",
["Correct. The lesion can occur anywhere from skull base to mediastinum, so unexplained paralysis deserves pathway-directed imaging.","Idiopathic is a diagnosis reached after an appropriate evaluation, not before it.","The recurrent laryngeal nerve has major thoracic relationships, particularly on the left.","Permanent intervention may eventually be appropriate, but first define etiology, functional burden, and recovery potential."],
"Unexplained UVFP is a localization problem: image the nerve, not just the vocal fold.","How does right-sided RLN anatomy change the inferior extent of imaging compared with the left?","senior_management"),
_q("v249_lar_uvfp_snr","Unilateral Vocal Fold Paralysis","senior_decision",
"Six weeks after a likely iatrogenic recurrent-laryngeal-nerve injury, a patient has severe breathy dysphonia and aspiration but meaningful spontaneous recovery is still possible. What is the best senior-level intervention strategy?",
["Offer temporary injection augmentation to restore glottic competence while recovery is observed, with later framework surgery or reinnervation if persistent deficits warrant it","Perform destructive cordectomy to enlarge the airway","Wait many months without treating aspiration because any intervention prevents nerve recovery","Perform permanent medialization thyroplasty immediately in every recent postoperative paralysis"],0,
"Temporary injection laryngoplasty can improve voice, cough, and swallowing during the recovery window without committing the patient to a permanent framework procedure. Long-term choices depend on time course, glottic configuration, age, nerve prognosis, and goals.",
["Correct. Temporary augmentation treats clinically important glottic insufficiency while preserving options during uncertain neural recovery.","Cordectomy enlarges the airway and would worsen glottic insufficiency in unilateral paralysis.","Clinically important aspiration and ineffective cough deserve treatment; augmentation does not block neural recovery.","Permanent thyroplasty is useful for established deficits but is not automatically the first choice during an early recovery window."],
"Treat the function now while preserving the recovery window; temporary injection is often the bridge.","When would posterior glottic gap, vertical level mismatch, or high vagal injury make you consider arytenoid adduction or additional strategies?","senior_management"),

_q("v249_lar_dysphagia_fnd","Dysphagia / Aspiration","foundation",
"During swallowing, which event is most important for protecting the airway from aspiration?",
["Coordinated laryngeal closure with hyolaryngeal elevation and timely pharyngeal propulsion","Opening of the external auditory canal","Contraction of the temporalis muscle alone","Nasal valve widening"],0,
"Airway protection is coordinated, not a single-flap event: true and false vocal-fold closure, epiglottic inversion, hyolaryngeal elevation, pharyngeal driving pressure, and upper-esophageal-sphincter opening must occur in sequence.",
["Correct. Safe swallowing depends on coordinated closure, elevation, propulsion, and bolus clearance.","The external auditory canal has no role in swallowing protection.","Mastication helps oral preparation but does not by itself protect the laryngeal inlet during the pharyngeal swallow.","Nasal valve mechanics are unrelated to aspiration prevention."],
"Aspiration is usually a timing/closure/clearance problem, not simply an 'epiglottis problem.'",
"How does impaired laryngeal sensation increase risk even when gross motor closure looks reasonable?"),
_q("v249_lar_dysphagia_app","Dysphagia / Aspiration","application",
"A patient coughs with liquids after a lateral medullary stroke. You need to determine whether material enters the airway, when it occurs relative to the swallow, and which compensatory strategies improve safety. What is the best test?",
["An instrumental swallowing study such as modified barium swallow/VFSS or FEES selected to answer the clinical question","A routine chest radiograph alone","A noncontrast sinus CT","Pure-tone audiometry"],0,
"Instrumental swallowing assessment is required when bedside evaluation cannot define physiology or aspiration risk. VFSS visualizes bolus flow across oral, pharyngeal, and cervical-esophageal phases; FEES provides direct repeated assessment of pharyngeal/laryngeal secretion and airway-protection findings without radiation.",
["Correct. Instrumental assessment defines aspiration physiology and can test compensatory maneuvers or diet modifications.","Chest radiography may show pulmonary consequences but cannot characterize swallow timing or mechanism.","Sinus CT does not evaluate swallowing physiology.","Audiometry does not assess airway protection or bolus transit."],
"Choose FEES versus VFSS by the question, not by habit; both are physiologic tests with different strengths.","What features would make FEES especially useful, and what phase of swallowing is VFSS better able to display continuously?","overnight_call"),
_q("v249_lar_dysphagia_snr","Dysphagia / Aspiration","senior_decision",
"A frail patient has recurrent aspiration pneumonia despite therapy. FEES shows severe secretion aspiration and poor laryngeal sensation; oral intake is unsafe even before food is given. What is the best chief-level principle?",
["Treat this as a global airway-protection problem: define reversibility and goals, optimize pulmonary/oral/nutritional care, and consider nonoral feeding or aspiration-prevention surgery only after multidisciplinary assessment","Assume a feeding tube alone will prevent all aspiration pneumonia","Recommend thickened liquids as the only intervention despite aspiration of secretions","Proceed directly to total laryngectomy without clarifying goals, prognosis, or reversible contributors"],0,
"Aspiration can arise from secretions, refluxed material, and oral intake. Feeding tubes do not eliminate secretion aspiration. Senior management integrates prognosis, cognition, pulmonary reserve, rehabilitation potential, nutrition, patient goals, and whether separation procedures are justified for intractable life-threatening aspiration.",
["Correct. Severe aspiration requires a mechanism- and goals-based plan rather than a single dietary or procedural reflex.","Enteral feeding bypasses oral boluses but does not prevent aspiration of saliva or refluxate.","Thickening cannot address aspiration that occurs from secretions at baseline.","Aspiration-prevention operations can be transformative but carry major functional consequences and should follow a deliberate multidisciplinary decision."],
"A PEG changes the route of nutrition; it does not close the larynx.","When might laryngotracheal separation or other aspiration-prevention surgery become reasonable despite loss of normal voice?","senior_management"),

_q("v249_lar_bvfi_fnd","Bilateral Vocal Fold Immobility","foundation",
"A patient develops inspiratory stridor after total thyroidectomy. Both vocal folds are immobile near the paramedian position, but the voice is relatively strong. What is the immediate concern?",
["Bilateral vocal-fold immobility causing a critically narrowed glottic airway","Isolated unilateral vocal-fold paralysis","Benign vocal-fold nodules","Presbyphonia"],0,
"Bilateral folds fixed near the midline can preserve phonation while severely restricting inspiration. The first priority is airway adequacy, while the eventual differential includes bilateral neurogenic paralysis, posterior glottic stenosis, and cricoarytenoid fixation.",
["Correct. A good voice does not reassure you when both folds are near midline and the airway is narrow.","Unilateral paralysis does not explain bilateral immobility and severe inspiratory restriction.","Nodules affect vibration and voice rather than causing bilateral fixation.","Presbyphonia causes age-related glottic insufficiency, not acute stridor with fixed folds."],
"Bilateral immobility can sound better than it breathes.","Which examination distinguishes true neurogenic paralysis from posterior glottic scar or joint fixation?","overnight_call"),
_q("v249_lar_bvfi_app","Bilateral Vocal Fold Immobility","application",
"A patient with a history of prolonged intubation has bilateral vocal-fold immobility. Flexible laryngoscopy cannot determine whether the problem is neural or mechanical. What is the best next diagnostic step?",
["Direct laryngoscopy with arytenoid palpation, supplemented by laryngeal EMG when useful, to distinguish fixation/posterior glottic stenosis from denervation","Assume bilateral recurrent-laryngeal-nerve injury because all immobility is neurogenic","Order only a chest radiograph and make no further laryngeal assessment","Perform bilateral permanent cordotomy before defining the mechanism"],0,
"Posterior glottic stenosis can mimic bilateral paralysis after prolonged intubation. Operative palpation of the cricoarytenoid joints and scar, plus EMG when indicated, helps separate mechanical fixation from neurogenic loss.",
["Correct. Mechanism matters because treatment for posterior glottic scar differs from treatment for bilateral denervation.","Bilateral immobility is a physical finding, not a diagnosis; mechanical fixation is an important alternative.","A chest radiograph cannot establish arytenoid mobility or neural integrity.","Permanent airway-widening surgery before localization risks inappropriate irreversible treatment."],
"When both folds do not move, ask 'nerve or joint/scar?' before choosing the operation.","How would interarytenoid scar and reduced passive arytenoid mobility alter your operative plan?","OR_prep"),
_q("v249_lar_bvfi_snr","Bilateral Vocal Fold Immobility","senior_decision",
"A patient has stable chronic bilateral neurogenic vocal-fold paralysis with tracheostomy dependence and useful voice. Recovery is no longer expected. The patient wants decannulation. What is the best senior-level framework?",
["Discuss airway-widening options such as posterior cordotomy/arytenoidectomy while explicitly balancing decannulation against voice and aspiration, and tailor laterality/extent to the patient's priorities","Promise that widening the glottis will improve airway without changing voice or swallowing","Perform bilateral aggressive resection at the first operation regardless of airway need","Leave the tracheostomy permanently because no endoscopic airway-widening option exists"],0,
"Definitive BVFP surgery trades glottic resistance for phonatory and sometimes swallowing function. Posterior cordotomy and selected arytenoid procedures can permit decannulation, but the extent should be individualized and staged when appropriate.",
["Correct. The chief-level decision is a three-way balance among airway, voice, and swallowing rather than maximizing only glottic size.","Any irreversible widening can affect voice and may alter aspiration risk.","Overaggressive bilateral surgery increases functional morbidity and may be unnecessary.","Endoscopic posterior glottic-widening procedures are established options for selected chronic bilateral paralysis."],
"In bilateral paralysis, every millimeter of airway is purchased with some potential voice/swallow tradeoff.","When would reinnervation or pacing concepts be considered instead of static tissue removal?","senior_management"),

_q("v249_lar_stenosis_fnd","Subglottic / Tracheal Stenosis","foundation",
"An adult develops progressive exertional dyspnea and biphasic stridor months after prolonged intubation. Flexible laryngoscopy shows mobile vocal folds. Which diagnosis should be strongly considered?",
["Postintubation subglottic or tracheal stenosis","Unilateral vocal-fold paralysis","Allergic rhinitis","Benign positional vertigo"],0,
"Fixed central-airway narrowing below mobile vocal folds commonly presents with progressive dyspnea, reduced exercise tolerance, and biphasic stridor. Prior intubation or tracheostomy is a major clue.",
["Correct. The history and biphasic noise with preserved vocal-fold motion point below the glottis.","Unilateral paralysis usually causes dysphonia/glottic insufficiency rather than fixed subglottic narrowing.","Rhinitis does not cause biphasic central-airway stridor.","BPPV causes positional vertigo and is unrelated to airway obstruction."],
"Biphasic stridor plus mobile folds should move your localization below the glottis.","What history raises concern for idiopathic subglottic stenosis, GPA, relapsing polychondritis, or another inflammatory cause?"),
_q("v249_lar_stenosis_app","Subglottic / Tracheal Stenosis","application",
"A patient with suspected subglottic stenosis is stable in clinic. Which assessment best informs treatment planning?",
["Define stenosis length, diameter/grade, location, inflammatory activity and cartilage integrity using endoscopy plus appropriate cross-sectional/airway evaluation","Choose dilation based only on the patient's age","Use spirometry alone and never visualize the airway","Assume every stenosis is a short soft web suitable for endoscopic treatment"],0,
"Management depends on more than percent narrowing. Endoscopic characterization of length, maturity, circumference, cartilage involvement and distance from the vocal folds/tracheostomy, combined with imaging and flow testing when useful, determines whether endoscopic or open reconstruction is reasonable.",
["Correct. Morphology and framework integrity drive the procedure choice.","Age alone does not define whether a stenosis is amenable to dilation or resection.","Flow-volume loops can support fixed obstruction but cannot replace anatomic characterization.","Long, mature, circumferential or cartilaginous stenoses often behave differently from short compliant lesions."],
"Grade tells you how narrow; length and cartilage tell you what operation is likely to work.","What airway plan would you make before endoscopy if the stenosis is severe enough that passing an endotracheal tube may be impossible?","OR_prep"),
_q("v249_lar_stenosis_snr","Subglottic / Tracheal Stenosis","senior_decision",
"A patient has recurrent high-grade short-segment tracheal stenosis after multiple dilations, with mature circumferential scar and otherwise favorable resection anatomy. What is the best chief-level principle?",
["Recognize diminishing returns from repeated endoscopic procedures and consider definitive segmental resection/reconstruction in an experienced airway center","Continue identical dilations indefinitely because repeated recurrence proves open surgery is contraindicated","Perform total laryngectomy because any recurrent tracheal stenosis requires removal of the larynx","Place a permanent tracheostomy without discussing reconstructive options"],0,
"Repeated dilation can be appropriate for selected disease, but rapid recurrence from mature structural scar should trigger reassessment of the strategy. Short resectable tracheal stenosis may be best treated with tracheal resection and primary anastomosis when patient and anatomy are suitable.",
["Correct. Senior management recognizes when endoscopic palliation has stopped being durable and escalates to a definitive reconstruction when appropriate.","Repeated procedures are not automatically safer or better if the same fixed lesion predictably recurs.","The larynx need not be sacrificed for a resectable tracheal segment.","Tracheostomy can secure an airway but is not the only long-term option for favorable reconstructive anatomy."],
"Recurrent stenosis should make you reconsider the strategy, not simply repeat the last procedure faster.","Which features—long segment, cricoid involvement, poor cartilage, active inflammation, or high anastomotic tension—would change the reconstructive choice?","senior_management"),

_q("v249_lar_anatomy_fnd","Laryngeal Anatomy","foundation",
"Which intrinsic laryngeal muscle is the only abductor of the true vocal fold?",
["Posterior cricoarytenoid","Lateral cricoarytenoid","Thyroarytenoid","Interarytenoid"],0,
"The posterior cricoarytenoid abducts the vocal fold by rotating the arytenoid laterally. The lateral cricoarytenoid and interarytenoid are adductors, while the thyroarytenoid contributes to adduction, shortening, and body stiffness.",
["Correct. Posterior cricoarytenoid is the sole vocal-fold abductor and is therefore critical for airway opening.","Lateral cricoarytenoid adducts the membranous vocal fold.","Thyroarytenoid primarily shortens/adducts and adjusts vocal-fold tension rather than abducting.","Interarytenoid closes the posterior glottis by adducting the arytenoids."],
"PCA = the one true abductor; bilateral loss explains why recurrent-laryngeal-nerve injury can threaten the airway.","Which nerve supplies the posterior cricoarytenoid, and what happens if both sides lose function?"),
_q("v249_lar_anatomy_app","Laryngeal Anatomy","application",
"During external laryngeal framework surgery, which nerve is most at risk near the superior thyroid pedicle and cricothyroid muscle, and what deficit follows injury?",
["External branch of the superior laryngeal nerve; impaired cricothyroid function with difficulty raising pitch","Internal branch of the superior laryngeal nerve; isolated loss of tongue protrusion","Hypoglossal nerve; loss of vocal-fold abduction","Glossopharyngeal nerve; bilateral recurrent-laryngeal paralysis"],0,
"The external branch of the superior laryngeal nerve innervates the cricothyroid and is vulnerable near the superior thyroid vessels. Injury reduces the ability to lengthen/tension the vocal fold, often most noticeable to professional voice users as loss of upper range or projection.",
["Correct. EBSLN injury is a cricothyroid/pitch-control problem.","The internal SLN carries supraglottic sensation; tongue protrusion is hypoglossal motor function.","Hypoglossal nerve supplies the tongue, not the posterior cricoarytenoid.","Glossopharyngeal injury does not produce bilateral RLN paralysis."],
"RLN is not the only laryngeal nerve that matters; EBSLN injury can be devastating to a singer with a seemingly mobile larynx.","How does internal superior-laryngeal sensory loss alter aspiration risk?","OR_prep"),
_q("v249_lar_anatomy_snr","Laryngeal Anatomy","senior_decision",
"A patient has a deep laryngeal cancer crossing tissue planes. Which anatomic framework best explains why the paraglottic and pre-epiglottic spaces matter for staging and surgical planning?",
["They are potential fat-containing pathways that permit submucosal tumor spread and connect key supraglottic/glottic compartments","They are intravascular spaces that contain no soft tissue","They are external neck spaces unrelated to laryngeal tumor spread","They are synonymous with the Reinke space of the free vocal-fold edge"],0,
"The paraglottic and pre-epiglottic spaces are clinically important pathways of deep laryngeal spread. Invasion can be underestimated by mucosal appearance alone and can change T classification, feasibility of partial laryngeal surgery, and required margins.",
["Correct. Deep-space extension is a staging and resectability problem because tumor can travel beyond what surface endoscopy shows.","These are soft-tissue compartments rather than intravascular channels.","Both spaces are integral to internal laryngeal anatomy and tumor spread.","Reinke space is the superficial lamina propria of the true vocal fold and is anatomically distinct."],
"Surface disease can look small while deep-space disease makes the operation large.","How do the conus elasticus and quadrangular membrane help explain barriers and routes of spread between subglottic, glottic, and supraglottic regions?","senior_management"),
]


def apply_learning_ladders_v249(challenges, concept_id_fn):
    existing={q.get("id") for q in challenges}
    added=[]
    for src in VIGNETTES_V249:
        if src.get("id") in existing:
            continue
        q=dict(src)
        q["choices"]=list(src.get("choices") or [])
        q["why_wrong"]=list(src.get("why_wrong") or [])
        q["concept_id"]=concept_id_fn(q["domain"],q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added.append(q["id"])
    return added
