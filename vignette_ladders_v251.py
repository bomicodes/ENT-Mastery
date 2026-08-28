"""v25.1 — Laryngology / Voice / Swallowing deliberate ladder pass 2.

Adds five exact canonical topics emphasizing diagnostic interpretation, phonomicrosurgery,
glottic-insufficiency procedure selection, and mechanical posterior-glottic fixation.
Each receives foundation -> application -> senior-decision coverage.
"""
DOMAIN="Laryngology / Voice / Swallowing"


def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}


VIGNETTES_V251=[
_q("v251_lar_strobe_fnd","Stroboscopy Interpretation","foundation",
"What is the principal advantage of videostroboscopy over routine continuous-light laryngoscopy when evaluating dysphonia?",
["It samples successive phases of periodic phonation to estimate mucosal-wave and vibratory behavior","It directly measures recurrent-laryngeal-nerve conduction velocity","It continuously images the cervical esophagus during swallowing","It proves whether a white vocal-fold lesion is malignant"],0,
"Stroboscopy uses synchronized flashes to create an apparent slow-motion representation of sufficiently periodic vocal-fold vibration, allowing assessment of mucosal wave, amplitude, symmetry, periodicity, closure pattern and nonvibrating segments.",
["Correct. The test adds vibratory physiology that ordinary continuous-light examination may not reveal.","Neural conduction is not measured by stroboscopy.","Dynamic esophageal bolus transit is evaluated with swallowing/esophageal studies, not stroboscopy.","Stroboscopy can identify suspicious vibratory abnormalities but cannot replace tissue diagnosis when biopsy is indicated."],
"Stroboscopy is a vibration test, not a pathology specimen.","Why can highly aperiodic phonation make the apparent slow-motion image unreliable?"),
_q("v251_lar_strobe_app","Stroboscopy Interpretation","application",
"A singer has persistent focal dysphonia. Stroboscopy shows a small subepithelial lesion with a reproducibly reduced mucosal wave over that segment. Which interpretation is most useful?",
["A focal lesion tethering the cover, such as a cyst or scar, is more likely than a purely superficial lesion with preserved pliability","Normal mucosal wave excludes structural disease","The finding proves invasive carcinoma","The abnormality localizes to the recurrent laryngeal nerve rather than the vocal-fold cover"],0,
"A focal reduction or absence of mucosal wave suggests impaired pliability of the epithelium/superficial lamina propria and helps distinguish deeper or tethering pathology from lesions that ride on an otherwise preserved wave.",
["Correct. Localized wave restriction is a clue to depth and stiffness, not a diagnosis by itself.","Structural lesions may exist despite portions of preserved wave.","Wave restriction is nonspecific and does not by itself establish invasive cancer.","The finding describes cover vibration rather than proving a neural lesion."],
"Use the wave to reason about pliability and depth; do not turn it into a histology test.","How would an hourglass closure pattern plus bilateral symmetric mid-membranous lesions change your differential?","senior_management"),
_q("v251_lar_strobe_snr","Stroboscopy Interpretation","senior_decision",
"A patient with severe irregular dysphonia has such aperiodic phonation that the strobe repeatedly fails to synchronize. What is the best senior interpretation?",
["Do not overread an unstable stroboscopic image; use standard endoscopy and, when the vibratory question remains important, another method such as high-speed imaging if available","Call every apparent nonvibrating frame scar","Increase strobe brightness until synchronization becomes valid","Conclude that no structural lesion can be present"],0,
"Stroboscopy depends on sufficiently periodic vibration. In markedly aperiodic voices, synchronization artifacts can mimic or obscure pathology, so the examiner should recognize the technical limitation and use complementary visualization rather than manufacture certainty.",
["Correct. A technically invalid physiologic test should not drive irreversible treatment.","Apparent frame-to-frame abnormalities during failed synchronization are not reliable evidence of scar.","Brightness does not correct the sampling problem created by aperiodicity.","A limited strobe does not exclude structural disease."],
"Know when the test is lying to you.","Which disorders commonly produce enough aperiodicity that routine strobe interpretation becomes difficult?","senior_management"),

_q("v251_lar_micro_fnd","Microlaryngoscopy","foundation",
"During suspension microlaryngoscopy for a benign phonatory lesion, what operative principle best protects long-term voice?",
["Preserve normal epithelium and superficial lamina propria while limiting unnecessary thermal or deep tissue injury","Remove a wide margin of normal vocal-fold muscle around every benign lesion","Cauterize the entire free edge to prevent recurrence","Intentionally violate the vocal ligament so postoperative scar is more stable"],0,
"Phonomicrosurgery aims to remove or treat pathology while preserving the layered vibratory cover. Excessive epithelial loss, deep dissection and thermal injury increase stiffness and scar.",
["Correct. Tissue preservation is central because the operation succeeds only if the remaining vocal fold still vibrates well.","Wide muscle resection is inappropriate for routine benign phonatory lesions and worsens functional morbidity.","Diffuse cautery injures the vibratory edge.","Vocal-ligament injury increases rather than prevents disabling scar."],
"In voice surgery, millimeters of unnecessary injury matter.","Which layer is Reinke space, and why is it functionally important?","OR_prep"),
_q("v251_lar_micro_app","Microlaryngoscopy","application",
"A professional voice user has a persistent vocal-fold cyst after optimized voice therapy and elects surgery. Which operative strategy best matches phonomicrosurgical principles?",
["Use precise exposure and a limited microflap/dissection that preserves as much overlying cover as possible while removing the cyst wall without unnecessary ligament injury","Strip the entire vocal fold epithelium","Perform bilateral cordectomy even though the opposite fold is normal","Use blind transcutaneous curettage without visualizing the lesion"],0,
"A true intracordal cyst may require careful microflap excision, but the objective is complete enough lesion treatment with maximal preservation of epithelium, superficial lamina propria and ligament integrity.",
["Correct. Precise dissection balances recurrence risk against the even more important risk of postoperative stiffness/scar.","Stripping sacrifices normal vibratory cover.","The normal contralateral fold should not be resected prophylactically.","Blind removal cannot provide the precision required for layered vocal-fold surgery."],
"The lesion is not the only thing you are operating on; you are preserving a vibration system.","When might you stage treatment of bilateral lesions rather than aggressively address both free edges at once?","OR_prep"),
_q("v251_lar_micro_snr","Microlaryngoscopy","senior_decision",
"During planned microlaryngoscopy for an anterior vocal-fold lesion, suspension exposure is poor despite appropriate repositioning and scopes, and safe visualization of the target cannot be achieved. What is the best senior decision?",
["Avoid blind or traumatic instrumentation; change the exposure strategy or abort and plan an alternative approach if the target cannot be treated safely","Continue deeper suspension pressure until the target appears regardless of dental or soft-tissue injury","Resect the unseen lesion by feel","Convert automatically to an open partial laryngectomy for any benign lesion"],0,
"Exposure is part of the operation. When visualization is inadequate, forcing suspension or operating blindly can injure teeth, tongue, mucosa or normal vocal fold and may still fail to treat the lesion accurately.",
["Correct. Safe inability to proceed is better than creating avoidable injury for a nonemergent voice procedure.","Escalating suspension trauma is not an acceptable substitute for visualization.","Phonomicrosurgery requires visual precision.","Open laryngeal resection is not the routine rescue for an inadequately exposed benign lesion."],
"A chief knows when exposure has made the planned operation unsafe.","What preoperative dental, cervical-spine, mandibular, and prior-radiation features should make difficult suspension more likely?","senior_management"),

_q("v251_lar_inj_fnd","Injection Laryngoplasty","foundation",
"What problem does injection laryngoplasty primarily treat?",
["Glottic insufficiency by adding bulk and medializing an underclosed vocal fold","Bilateral fixed midline vocal folds by widening the posterior glottis","Cricopharyngeal hypertonicity by cutting the sphincter","Subglottic stenosis by expanding the cricoid framework"],0,
"Injection augmentation improves glottic closure in conditions such as unilateral paresis/paralysis or selected atrophy by adding volume lateral to the vibratory edge.",
["Correct. The goal is improved glottic competence for voice, cough and sometimes swallowing.","Posterior airway widening is the opposite mechanical goal.","Cricopharyngeal dysfunction is an upper-esophageal-sphincter problem.","Subglottic stenosis is not treated by vocal-fold augmentation."],
"Injection closes an insufficient glottis; it does not open an obstructed one.","How does injection material duration influence a case with uncertain neural recovery?"),
_q("v251_lar_inj_app","Injection Laryngoplasty","application",
"Six weeks after recurrent-laryngeal-nerve injury, a patient has severe breathy dysphonia, ineffective cough and aspiration, but recovery remains possible. What is the best procedural logic?",
["Offer a temporary injection augmentation now rather than forcing prolonged functional impairment while waiting for recovery","Perform permanent destructive cordectomy","Delay all treatment because injection prevents nerve recovery","Perform bilateral posterior cordotomy"],0,
"Early temporary augmentation can restore glottic competence while preserving the observation window and later options. This principle is already reinforced in the site's UVFP and OR-management material.",
["Correct. Temporary augmentation treats current functional morbidity without committing the patient to permanent framework surgery.","Cordectomy worsens unilateral glottic insufficiency.","Injection does not stop neural recovery.","Posterior cordotomy enlarges an airway and is used for selected bilateral immobility, not unilateral insufficiency."],
"Treat the disability during the recovery window without pretending the prognosis is already known.","Which aspiration or pulmonary features would push you toward earlier rather than delayed augmentation?","senior_management"),
_q("v251_lar_inj_snr","Injection Laryngoplasty","senior_decision",
"A patient with chronic unilateral paralysis has a large posterior glottic gap and marked vertical height mismatch. Repeated injections improve the anterior gap but leave substantial insufficiency. What is the best senior next step?",
["Reassess framework and arytenoid-position options because injection alone may not correct posterior gap or vertical mismatch","Keep increasing injection volume indefinitely regardless of airway narrowing","Perform posterior cordotomy to enlarge the gap further","Conclude that all medialization procedures are contraindicated"],0,
"Large posterior gaps and vertical level differences often require framework correction and sometimes arytenoid adduction rather than simply adding more injectable bulk.",
["Correct. Procedure selection should match the geometry of the insufficiency.","Overaugmentation can create poor voice, airway compromise, dysphagia or misplaced material without solving arytenoid position.","Cordotomy enlarges the glottis and worsens insufficiency.","Failure of injection to solve a geometry problem does not invalidate other medialization strategies."],
"When augmentation fails, ask whether the problem is volume or position.","What new stridor or dyspnea after injection should trigger urgent laryngoscopic airway assessment?","senior_management"),

_q("v251_lar_thyro_fnd","Medialization Thyroplasty","foundation",
"Type I medialization thyroplasty improves unilateral glottic insufficiency by which mechanism?",
["Placing a framework implant through a thyroid-cartilage window to medialize the affected vocal fold","Removing the posterior vocal fold to enlarge the airway","Dividing the cricopharyngeus","Resecting the recurrent laryngeal nerve"],0,
"Type I thyroplasty is a framework operation that repositions the paralyzed or paretic fold toward midline to improve closure while preserving its tissue layers.",
["Correct. The implant changes vocal-fold position through the laryngeal framework.","Posterior cordotomy is an airway-widening procedure.","Cricopharyngeal myotomy treats selected UES dysfunction.","RLN resection would not improve glottic competence."],
"Thyroplasty changes position without cutting the vibratory edge.","Why can awake phonation or endoscopic feedback be useful during implant sizing?","OR_prep"),
_q("v251_lar_thyro_app","Medialization Thyroplasty","application",
"A patient has stable long-standing unilateral vocal-fold paralysis with no meaningful recovery expected and persistent breathy dysphonia despite therapy. The gap is primarily membranous without major posterior height mismatch. Which durable option best fits?",
["Type I medialization thyroplasty","Temporary short-duration injection as the only lifetime plan","Bilateral posterior cordotomy","Tracheal resection"],0,
"For established glottic insufficiency when recovery is not expected, framework medialization is a durable option. Temporary injection is especially useful earlier when recovery remains uncertain or when a reversible trial is desired.",
["Correct. Durable stable unilateral insufficiency is a classic setting for framework medialization.","Repeated temporary injection can be appropriate in selected patients but is not the only durable strategy for a stable deficit.","Cordotomy treats airway obstruction from bilateral immobility and worsens closure.","Tracheal resection does not address a glottic gap."],
"Temporary versus permanent is a prognosis-and-goals decision, not a preference for one device.","How would high vagal injury with sensory loss change your swallowing counseling?","senior_management"),
_q("v251_lar_thyro_snr","Medialization Thyroplasty","senior_decision",
"After an otherwise uncomplicated medialization thyroplasty, a patient develops rapidly increasing neck swelling, stridor and work of breathing. What is the correct chief response?",
["Treat this as an airway-threatening postoperative complication and urgently assess/manage possible hematoma or edema rather than waiting for routine voice follow-up","Assume expected implant settling and discharge","Add more implant material to improve the voice","Delay airway evaluation until a formal stroboscopy appointment"],0,
"A medialized larynx has limited reserve. Expanding hematoma or edema can rapidly threaten the airway and requires immediate bedside/operative assessment and airway planning.",
["Correct. Airway deterioration after framework surgery is an emergency, not a routine voice issue.","Stridor and expanding swelling are not expected settling.","Further medialization could worsen airway compromise.","Definitive voice testing is secondary to immediate airway safety."],
"Post-thyroplasty stridor plus swelling is an airway problem until proved otherwise.","If voice remains poor after healing but the implant is well positioned, what posterior-gap or arytenoid-level problem should you reassess?","overnight_call"),

_q("v251_lar_pgs_fnd","Posterior Glottic Stenosis / Arytenoid Fixation","foundation",
"A patient develops bilateral vocal-fold immobility after prolonged intubation. Why should posterior glottic stenosis be considered before labeling this bilateral nerve paralysis?",
["Interarytenoid/posterior-commissure scar can mechanically fix the cricoarytenoid joints and mimic neurogenic paralysis","Intubation cannot injure the posterior glottis","Posterior scar always causes unilateral rather than bilateral findings","Flexible laryngoscopy can always distinguish joint fixation from denervation by appearance alone"],0,
"Posterior pressure injury can produce interarytenoid scar and cricoarytenoid fixation, creating bilateral immobility that resembles recurrent-laryngeal-nerve paralysis.",
["Correct. Bilateral immobility is a finding; the mechanism may be neural or mechanical.","Prolonged intubation is a classic risk for posterior glottic injury.","Posterior scar can restrict both arytenoids.","Office visualization often cannot determine passive joint mobility or neural integrity."],
"When both folds do not move, ask nerve versus joint/scar.","What posterior laryngeal pressure points are most vulnerable during prolonged intubation?"),
_q("v251_lar_pgs_app","Posterior Glottic Stenosis / Arytenoid Fixation","application",
"A tracheostomy-dependent patient has bilateral immobility after prolonged intubation, and office laryngoscopy cannot distinguish paralysis from fixation. What evaluation most directly resolves the mechanism?",
["Direct laryngoscopy with arytenoid palpation and scar assessment, with laryngeal EMG when it adds useful neural information","Assume recurrent-laryngeal-nerve paralysis and perform irreversible cordotomy","Order a sinus CT only","Judge cricoarytenoid mobility from voice quality alone"],0,
"Operative palpation directly tests passive cricoarytenoid mobility and identifies posterior scar; EMG can complement the examination when neurogenic dysfunction remains in the differential.",
["Correct. Mechanical versus neurogenic immobility changes the reconstructive strategy.","Irreversible airway-widening surgery before localization risks treating the wrong mechanism.","Sinus imaging does not determine arytenoid fixation.","Voice quality cannot reliably separate joint fixation from denervation."],
"Palpate before you permanently widen.","How would dense interarytenoid scar with mobile joints differ from ankylosed cricoarytenoid joints in operative planning?","OR_prep"),
_q("v251_lar_pgs_snr","Posterior Glottic Stenosis / Arytenoid Fixation","senior_decision",
"A patient with mature posterior glottic scar is tracheostomy dependent but wants decannulation and values voice. What is the best senior operative framework?",
["Match the operation to scar pattern and joint mobility, considering scar release/reconstruction versus selective airway-widening while explicitly balancing airway, voice and swallowing","Perform maximal bilateral arytenoidectomy in every patient","Treat all posterior glottic stenosis as recurrent-laryngeal-nerve paralysis","Promise decannulation without any voice or swallowing tradeoff"],0,
"Posterior glottic stenosis is heterogeneous. Scar lysis with mucosal flap/grafting or other reconstruction may be appropriate in selected patterns, whereas fixed mature disease may require posterior airway-widening procedures; tracheostomy status and functional priorities matter.",
["Correct. The operation should reflect anatomy and patient goals rather than a one-size-fits-all widening maneuver.","Aggressive bilateral tissue removal can create unnecessary voice and swallowing morbidity.","Mechanical scar requires different reasoning from pure denervation.","Any procedure that enlarges or reconstructs the posterior glottis carries functional tradeoffs and cannot guarantee decannulation."],
"For posterior glottic stenosis, decannulation is a goal—not permission to ignore phonation and swallowing.","When would a reconstructive scar-release approach be preferable to destructive posterior widening?","senior_management"),
]


def apply_learning_ladders_v251(challenges, concept_id_fn):
    existing={q.get("id") for q in challenges}
    added=[]
    for src in VIGNETTES_V251:
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
