"""v24.1 — Pediatric Otolaryngology deliberate ladder pass 1.

High-yield airway/swallow/neck topics selected from exact canonical registry labels.
Adds only missing structured foundation -> application -> senior-decision layers.
"""
DOMAIN="Pediatric Otolaryngology"

def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}

VIGNETTES_V241=[
_q("v241_ped_choanal_fnd","Choanal Atresia","foundation",
"A newborn has cyclical cyanosis that improves while crying, and a catheter cannot be passed through either nasal cavity. What diagnosis should be assumed until proven otherwise?",
["Bilateral choanal atresia","Laryngomalacia","Unilateral vocal-fold paralysis","Viral croup"],0,
"Bilateral choanal atresia classically causes neonatal nasal obstruction with cyanosis at rest that improves when the infant cries and opens the mouth.",
["Correct: this is the classic physiology of bilateral posterior nasal obstruction.","Laryngomalacia causes inspiratory stridor rather than failure to pass a nasal catheter.","Vocal-fold paralysis is a laryngeal disorder and does not explain bilateral nasal catheter obstruction.","Croup is acquired subglottic inflammation, not a congenital posterior nasal blockage."],
"Cyanosis relieved by crying is a nasal-airway clue in a neonate.","What immediate temporizing airway maneuvers can stabilize a neonate before definitive repair?"),
_q("v241_ped_choanal_app","Choanal Atresia","application",
"A term neonate with suspected bilateral choanal atresia has worsening obstruction and desaturation. What is the best immediate management while the diagnosis and associated anomalies are being defined?",
["Establish a reliable oral airway or intubate if needed, then confirm anatomy and evaluate associated anomalies before definitive transnasal repair","Repeated blind dilation of the posterior nose at bedside","Wait because crying reliably protects the airway","Perform emergent tracheostomy in every case"],0,
"The first priority is oxygenation and ventilation. An oral airway can bypass the obstructed nasal airway; intubation is appropriate if that is inadequate. Definitive repair follows stabilization and anatomic/syndromic assessment.",
["Correct: stabilize the airway first, then define anatomy and plan repair.","Blind instrumentation risks trauma and does not provide controlled definitive treatment.","Reliance on crying is unsafe in a neonate with significant obstruction.","Tracheostomy is not automatically required when the obstruction can be bypassed orally or with an endotracheal tube."],
"Bilateral choanal atresia is an airway emergency before it is a nasal operation.","Which CHARGE-associated findings should alter the preoperative evaluation?","overnight_call"),
_q("v241_ped_choanal_snr","Choanal Atresia","senior_decision",
"After endoscopic repair of bilateral choanal atresia, an infant develops progressive recurrent nasal obstruction. Endoscopy shows circumferential restenosis rather than removable crust alone. What is the best senior-level next step?",
["Reassess the restenosis endoscopically, optimize local wound care, and plan targeted revision when fixed restenosis is clinically significant rather than repeatedly traumatizing the repair with blind dilation","Perform repeated blind office dilation regardless of anatomy","Ignore recurrent respiratory symptoms until school age","Convert automatically to open craniofacial surgery"],0,
"Restenosis requires distinction from crusting or granulation. Significant fixed restenosis is managed with endoscopic reassessment and selective revision while minimizing mucosal trauma and optimizing postoperative care.",
["Correct: define the mechanism and revise deliberately when obstruction is fixed and important.","Blind repeated trauma can worsen scarring and is not anatomy-driven management.","Symptomatic recurrent obstruction in an infant requires timely reassessment.","Open surgery is not the default response to endoscopically manageable restenosis."],
"When a repaired neonatal airway worsens, identify crust, granulation, or fixed scar before choosing the intervention.","How would severe reflux, syndromic anatomy, or repeated restenosis change counseling?","senior_management"),

_q("v241_ped_asp_fnd","Pediatric Aspiration","foundation",
"An infant coughs, chokes, and intermittently desaturates during feeds and has recurrent pneumonias. What problem must be evaluated directly rather than assuming reflux alone?",
["Oropharyngeal aspiration during swallowing","Otitis externa","Isolated allergic rhinitis","Benign positional vertigo"],0,
"Feeding-associated cough, choking, desaturation, and recurrent lower-respiratory disease are classic clues to aspiration and warrant a structured feeding/swallow evaluation.",
["Correct: the timing with feeds and pulmonary consequences localize concern to swallowing safety.","Otitis externa does not cause feeding-associated pulmonary symptoms.","Allergic rhinitis does not explain recurrent pneumonias linked to swallowing.","BPPV does not cause aspiration during feeds."],
"Recurrent pneumonia plus symptoms during feeds is an aspiration history until evaluated.","Which children can aspirate silently without cough?"),
_q("v241_ped_asp_app","Pediatric Aspiration","application",
"A child with recurrent pneumonias has a modified barium swallow showing aspiration of thin liquids. What is the best next management principle?",
["Use the swallow findings to guide safe feeding strategies while identifying the cause, and pursue airway endoscopy when structural disease such as a laryngeal cleft is suspected","Place a feeding tube permanently without defining mechanism","Treat every case with proton-pump inhibitor monotherapy","Proceed directly to tracheostomy"],0,
"Management should reduce immediate aspiration risk while determining whether dysphagia is developmental, neurologic, sensory, or structural. Suspicion for a laryngeal cleft or other airway lesion warrants direct airway evaluation.",
["Correct: protect the lungs and define mechanism in parallel.","Enteral access may be needed in severe cases but should not substitute for etiologic evaluation.","Acid suppression does not correct oropharyngeal aspiration.","Tracheostomy neither automatically prevents aspiration nor represents first-line management for most children."],
"Treat the physiology shown on the swallow study, but keep asking why the child aspirates.","What endoscopic anatomy defines a type I versus deeper laryngeal cleft?","overnight_call"),
_q("v241_ped_asp_snr","Pediatric Aspiration","senior_decision",
"A medically complex child continues to aspirate across consistencies despite therapy and has repeated ICU admissions for aspiration pneumonia. Oral intake is unsafe and the family asks whether one more minor feeding adjustment is enough. What is the best senior-level approach?",
["Escalate to a multidisciplinary airway/swallow plan that prioritizes pulmonary protection, nutrition, etiology-directed treatment, and—when aspiration is truly intractable—discussion of definitive aspiration-prevention options","Continue unrestricted oral feeding because aspiration is common","Assume a tracheostomy cuff will reliably prevent aspiration","Perform adenotonsillectomy as aspiration-prevention surgery"],0,
"Recurrent severe aspiration despite optimized conservative care requires explicit escalation. Decisions may include nonoral nutrition, treatment of a structural lesion, neurologic/feeding optimization, and selected aspiration-prevention surgery when morbidity is otherwise unacceptable.",
["Correct: severity and failed conservative management justify multidisciplinary escalation.","Ongoing unrestricted intake can perpetuate preventable pulmonary injury.","A tracheostomy cuff is not a dependable barrier to aspirated material and can add morbidity.","Adenotonsillectomy does not separate the airway from alimentary flow."],
"The escalation threshold is recurrent pulmonary injury despite a well-executed conservative plan—not merely an abnormal swallow study.","Which goals-of-care and communication issues matter before irreversible aspiration-prevention surgery?","senior_management"),

_q("v241_ped_supra_fnd","Supraglottoplasty","foundation",
"Which infant with laryngomalacia is most likely to need supraglottoplasty rather than observation alone?",
["An infant with severe retractions, apnea/cyanotic events, feeding compromise, or failure to thrive attributable to laryngomalacia","An infant with mild stridor who feeds and grows normally","A child with isolated otitis media","A teenager with uncomplicated epistaxis"],0,
"Most laryngomalacia is self-limited, but severe obstruction, hypoxemia/apnea, feeding dysfunction, or growth failure are classic reasons to consider operative treatment.",
["Correct: severity is defined by physiologic consequence, not loudness of stridor alone.","Mild disease with normal feeding and growth is generally observed.","Otitis media is unrelated to supraglottic collapse.","Epistaxis is unrelated to laryngomalacia."],
"Operate for consequences of laryngomalacia, not for noise alone.","Which synchronous airway lesions or comorbidities increase the chance of persistent symptoms?"),
_q("v241_ped_supra_app","Supraglottoplasty","application",
"During endoscopic evaluation of severe laryngomalacia, which operative concept best describes a typical supraglottoplasty?",
["Release shortened aryepiglottic folds and selectively reduce redundant supraglottic tissue while preserving enough mucosa to avoid excessive scarring","Circumferentially strip all supraglottic mucosa","Divide both recurrent laryngeal nerves","Remove the entire epiglottis routinely"],0,
"Supraglottoplasty is tailored to the collapsing anatomy. Common maneuvers include division of tight aryepiglottic folds and conservative treatment of redundant arytenoid/supraglottic tissue while avoiding opposing raw surfaces and unnecessary injury.",
["Correct: the operation is anatomy-targeted and tissue-preserving.","Aggressive circumferential mucosal injury risks stenosis and dysphagia.","RLN injury would create major laryngeal dysfunction and is not therapeutic.","Routine total epiglottectomy is unnecessary and potentially harmful."],
"Know what is collapsing before cutting: supraglottoplasty is not one identical operation for every infant.","Which areas should be treated conservatively to reduce postoperative supraglottic stenosis?","OR_prep"),
_q("v241_ped_supra_snr","Supraglottoplasty","senior_decision",
"An infant remains oxygen-dependent with severe work of breathing after technically adequate supraglottoplasty. What is the best next step?",
["Reassess the entire airway and comorbid physiology for synchronous lesions, edema, aspiration, neurologic hypotonia, or another cause before reflexively repeating the same operation","Repeat supraglottoplasty immediately without airway reassessment","Assume all postoperative stridor is expected and discharge","Perform tonsillectomy"],0,
"Persistent severe symptoms after supraglottoplasty should trigger a new localization problem. Synchronous airway lesions, postoperative edema, aspiration, neurologic disease, pulmonary disease, and residual collapse can all change management.",
["Correct: failure of an anatomically appropriate operation should reopen the differential.","Blind repetition risks morbidity when the true driver may be elsewhere.","Ongoing oxygen need and severe work of breathing require evaluation, not routine discharge.","Tonsillectomy does not address infant supraglottic obstruction."],
"A failed airway operation is a reason to relocalize, not merely to repeat.","When would noninvasive support, revision surgery, or tracheostomy become reasonable?","senior_management"),

_q("v241_ped_ltr_fnd","Laryngotracheal Reconstruction","foundation",
"What is the primary objective of cartilage-graft laryngotracheal reconstruction for mature pediatric subglottic stenosis?",
["Expand the laryngotracheal framework to create a stable airway that can support breathing and, when appropriate, decannulation","Paralyze the vocal folds","Reduce tongue-base volume","Ablate the Eustachian tube"],0,
"LTR enlarges a stenotic laryngeal or tracheal framework with anterior and/or posterior expansion, often using cartilage grafts. The ultimate goal is a stable functional airway, not merely a larger measured lumen.",
["Correct: framework expansion is the defining reconstructive principle.","Vocal-fold paralysis worsens airway and voice function.","Tongue-base surgery addresses a different level of obstruction.","Eustachian-tube treatment has no role in subglottic stenosis reconstruction."],
"LTR treats a fixed framework problem by expanding the framework.","How does cricotracheal resection differ conceptually from expansion reconstruction?"),
_q("v241_ped_ltr_app","Laryngotracheal Reconstruction","application",
"A tracheostomy-dependent child is being considered for airway reconstruction. Which preoperative finding is most important to define before choosing single-stage versus double-stage LTR?",
["The complete airway lesion plus glottic function, pulmonary status, aspiration/swallowing safety, comorbidities, and ability to tolerate a period without the tracheostomy","Only the child's chronological age","Only the external tracheostomy tube brand","Only whether the family lives near the hospital"],0,
"Staging is a systems decision. Airway grade and length matter, but glottic competence, aspiration, pulmonary reserve, neurologic status, infection/inflammation, and postoperative support determine whether immediate decannulation/extubation is realistic and safe.",
["Correct: reconstruction planning integrates airway anatomy with the child's physiologic reserve.","Age alone does not determine reconstructive staging.","Tube brand does not define stenosis biology or airway readiness.","Geography can affect logistics but cannot replace the clinical staging assessment."],
"Do not choose single- versus double-stage LTR from stenosis grade alone.","How do vocal-fold mobility and aspiration risk change the reconstruction plan?","OR_prep"),
_q("v241_ped_ltr_snr","Laryngotracheal Reconstruction","senior_decision",
"A child has an adequately enlarged reconstructed subglottis but repeatedly fails decannulation because of aspiration, poor pulmonary reserve, and multilevel dynamic collapse. What is the best interpretation?",
["The reconstruction may be anatomically successful while the child is not yet functionally decannulation-ready; address the nonstenotic barriers rather than repeatedly enlarging an already adequate subglottis","The cartilage graft must always be replaced","Decannulation failure proves the original stenosis was misdiagnosed","A larger tracheostomy tube will cure aspiration"],0,
"Decannulation is an integrated endpoint. A patent reconstructed segment cannot compensate for severe aspiration, tracheobronchomalacia, glottic dysfunction, secretion burden, or inadequate pulmonary reserve.",
["Correct: separate anatomic airway success from functional decannulation readiness.","Replacing a sound graft does not treat downstream causes of failure.","Persistent nonstenotic barriers do not invalidate the original stenosis diagnosis.","Tube size does not correct swallowing dysfunction."],
"Before revising a patent reconstruction, identify why the whole child—not just the subglottis—cannot tolerate decannulation.","Which objective airway, swallow, sleep, and pulmonary data would you want before another decannulation attempt?","senior_management"),

_q("v241_ped_tgdc_fnd","Thyroglossal Duct Cyst","foundation",
"A child has a painless midline neck mass that elevates with swallowing and tongue protrusion. What is the most likely diagnosis?",
["Thyroglossal duct cyst","Second branchial cleft cyst","Ranula","Parotid abscess"],0,
"A thyroglossal duct remnant typically presents as a midline neck mass related to the hyoid that moves with swallowing or tongue protrusion because of its embryologic tract toward the tongue base.",
["Correct: midline location and movement with tongue protrusion are classic clues.","Second branchial lesions are typically lateral neck masses.","Ranulas arise from the sublingual gland/floor of mouth.","Parotid infection presents in the lateral face/parotid region."],
"A midline mobile neck mass in a child should make you think embryology before lymph node.","What imaging finding would make you verify the presence of orthotopic thyroid tissue before surgery?"),
_q("v241_ped_tgdc_app","Thyroglossal Duct Cyst","application",
"A child with a previously infected thyroglossal duct cyst is now clinically well after antibiotic treatment. What is the definitive operation?",
["Sistrunk procedure removing the cyst, central hyoid segment, and tract toward the tongue base","Simple cyst shell-out only","Total thyroidectomy in every child","Incision and drainage as definitive therapy"],0,
"The tract commonly courses through or around the hyoid. The Sistrunk procedure reduces recurrence by removing the central hyoid segment and the superior tract rather than excising only the visible cyst.",
["Correct: definitive treatment follows embryologic anatomy.","Simple cyst excision leaves tract and has a substantially higher recurrence risk.","Normal orthotopic thyroid should not be removed routinely.","Drainage treats an acute abscess but leaves the congenital tract in place."],
"Control acute infection first; definitive Sistrunk follows when inflammation has settled.","Where is the tract followed superiorly and what nearby anatomy matters during dissection?","OR_prep"),
_q("v241_ped_tgdc_snr","Thyroglossal Duct Cyst","senior_decision",
"A child develops another midline cyst after prior 'thyroglossal cyst excision.' The operative note shows the central hyoid was never removed. What is the best next management principle?",
["Confirm diagnosis and thyroid anatomy, then plan revision Sistrunk-style excision of residual tract/hyoid-related disease with attention to scarred planes","Repeat aspiration whenever it enlarges","Observe indefinitely despite recurrent infection","Perform bilateral neck dissection"],0,
"Recurrence after simple excision often reflects retained tract or hyoid-associated tissue. Revision requires careful confirmation of anatomy and deliberate removal of the residual embryologic pathway while accounting for scar.",
["Correct: the prior inadequate embryologic excision explains recurrence and guides revision.","Aspiration does not eradicate the epithelial tract.","Recurrent infection is a meaningful morbidity and warrants definitive reassessment.","Neck dissection is not treatment for a benign recurrent thyroglossal remnant."],
"When a TGDC recurs, ask what part of the Sistrunk anatomy was left behind.","How would suspected carcinoma within a thyroglossal duct remnant alter the workup and operation?","senior_management")]

def apply_learning_ladders_v241(challenges,item_id_fn):
    existing={q.get("id") for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V241:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v241 pediatric orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}