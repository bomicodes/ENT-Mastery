"""v24.4 — Pediatric Otolaryngology deliberate ladder pass 4.

Five high-yield exact canonical topics emphasizing airway recurrence, deep neck
infection, tonsil decision-making, and congenital cervical lesions.
"""
DOMAIN="Pediatric Otolaryngology"

def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}

VIGNETTES_V244=[
_q("v244_ped_rrp_fnd","Recurrent Respiratory Papillomatosis","foundation",
"A child develops progressive hoarseness and intermittent stridor. Endoscopy shows multiple exophytic papillomatous lesions on the true vocal folds. What diagnosis is most likely?",
["Recurrent respiratory papillomatosis","Vocal fold nodules","Subglottic hemangioma","Croup"],0,
"Juvenile-onset recurrent respiratory papillomatosis is an HPV-associated epithelial disease that commonly presents with progressive dysphonia and can produce airway obstruction when burden is extensive.",
["Correct. Multifocal papillomatous laryngeal lesions with progressive hoarseness are classic for RRP.","Nodules are smooth benign phonotraumatic lesions rather than multifocal papillomas.","Subglottic hemangioma is a vascular infantile lesion, not exophytic true-fold papillomatosis.","Croup is an acute inflammatory illness rather than chronic recurrent epithelial lesions."],
"Progressive pediatric hoarseness deserves visualization; RRP can be a voice disease before it becomes an airway disease.","Which HPV types are classically associated with juvenile RRP?"),
_q("v244_ped_rrp_app","Recurrent Respiratory Papillomatosis","application",
"A child with RRP has worsening voice and increasing laryngeal papilloma burden but a stable airway. What operative principle is most appropriate?",
["Debulk disease sufficiently to restore airway/voice goals while preserving normal laryngeal mucosa and avoiding aggressive injury that creates scar","Attempt complete deep excision into vocalis muscle at every operation","Perform total laryngectomy as first-line therapy","Use systemic antibiotics as definitive treatment"],0,
"RRP is recurrent biology, so surgery aims for functional disease control rather than destructive eradication at the cost of vocal-fold scar, webs or stenosis. Microdebrider or laser techniques should preserve uninvolved tissue.",
["Correct. Functional control with tissue preservation is the operative goal.","Deep aggressive excision can create irreversible dysphonia and stenosis without preventing viral recurrence.","Laryngectomy is extraordinarily disproportionate for routine pediatric RRP.","Antibiotics do not treat HPV-driven papillomatosis."],
"Do not trade recurrent papilloma for permanent laryngeal scar.","Why should opposing anterior-commissure raw surfaces be avoided?","OR_prep"),
_q("v244_ped_rrp_snr","Recurrent Respiratory Papillomatosis","senior_decision",
"A child requires very frequent RRP debulking despite careful surgery, with repeated rapid regrowth and increasing treatment burden. What is the best senior-level approach?",
["Reassess disease extent and discuss appropriate adjuvant therapy in a specialized multidisciplinary pathway while continuing tissue-preserving surgery","Simply make each surgery more aggressive until all mucosa is removed","Ignore distal airway disease because RRP is always confined to the glottis","Perform routine tracheostomy solely to reduce procedure frequency"],0,
"Frequent recurrence or aggressive disease can justify adjuvant strategies such as systemic or intralesional therapies depending on current evidence, age and disease phenotype. Distal spread should be considered when clinically suggested.",
["Correct. High-burden RRP is a disease-management problem, not a reason for progressively destructive surgery.","More mucosal injury increases scar without curing HPV persistence.","RRP can involve subglottis, trachea and rarely distal lung.","Tracheostomy is not a routine disease-control strategy and may complicate airway disease distribution."],
"When surgery becomes too frequent, change the disease-control strategy rather than just increasing surgical injury.","What features should raise concern for pulmonary spread or malignant transformation?","senior_management"),

_q("v244_ped_dni_fnd","Pediatric Deep Neck Infection","foundation",
"A febrile child has severe sore throat, neck stiffness, torticollis and refusal to extend the neck. Which diagnosis requires urgent consideration?",
["Retropharyngeal/deep neck infection","Otitis externa","Allergic rhinitis","Benign positional vertigo"],0,
"Retropharyngeal and parapharyngeal infections can present with fever, neck pain/stiffness, torticollis, dysphagia and respiratory symptoms and can progress to airway or mediastinal complications.",
["Correct. The symptom cluster localizes to a deep neck process.","External-canal inflammation does not cause torticollis and deep neck stiffness.","Allergic rhinitis does not explain fever and painful restricted neck motion.","BPPV is a vestibular disorder and does not cause febrile neck symptoms."],
"A febrile child with torticollis is not automatically musculoskeletal—think deep neck infection.","Which fascial-space continuity permits infection to descend into the mediastinum?"),
_q("v244_ped_dni_app","Pediatric Deep Neck Infection","application",
"CT shows a small retropharyngeal collection in a stable child with no airway compromise, no neurologic deficit and no sepsis. What is a reasonable initial management strategy?",
["Admit for IV antibiotics and close airway/clinical reassessment, reserving drainage for progression, failure to improve or a clearly drainable/high-risk abscess","Immediate bilateral neck exploration in every case","Outpatient antihistamines only","No monitoring because children cannot deteriorate quickly"],0,
"Selected stable children with small collections can improve with IV antibiotics and observation, but the threshold for drainage falls with airway symptoms, toxicity, large/organized collections or failure of medical therapy.",
["Correct. Management integrates physiology, collection characteristics and response rather than CT size alone.","Universal open drainage over-treats selected stable children.","Antihistamines do not treat deep bacterial infection.","Deep neck infection can progress rapidly and requires active reassessment."],
"The drainage decision is clinical plus radiographic—not a single millimeter cutoff.","What exam changes overnight should trigger immediate airway or operative escalation?","overnight_call"),
_q("v244_ped_dni_snr","Pediatric Deep Neck Infection","senior_decision",
"A child with a parapharyngeal abscess develops increasing work of breathing, drooling, muffled voice and worsening neck swelling despite IV antibiotics. What is the best next step?",
["Escalate airway planning and surgical source control urgently with anesthesia and appropriate surgical teams rather than waiting for another routine CT interval","Continue observation because antibiotics always work eventually","Sedate the child deeply for bedside drainage without an airway plan","Discharge on oral antibiotics"],0,
"Progressive airway symptoms and failure of medical therapy convert a potentially observable infection into an urgent airway/source-control problem. Induction and drainage should be planned around distorted anatomy and loss of airway tone.",
["Correct. Airway deterioration and treatment failure mandate urgent escalation.","Waiting can allow complete obstruction, sepsis or mediastinal spread.","Deep sedation without a rescue airway strategy can precipitate obstruction.","This child is clinically worsening and is not safe for outpatient care."],
"In deep neck infection, the operation may be drainage—but the dangerous decision is often how to secure the airway first.","When would thoracic surgery involvement be necessary?","senior_management"),

_q("v244_ped_tons_fnd","Recurrent Tonsillitis Decision-Making","foundation",
"Which principle is most important when considering tonsillectomy for recurrent throat infection?",
["Use well-documented episode frequency/severity and modifying factors rather than the mere statement that a child gets sick often","Operate after any two sore throats","Tonsil size alone determines recurrent-infection indication","Antibiotic allergy automatically mandates tonsillectomy"],0,
"Recurrent-infection tonsillectomy decisions depend on documented clinically meaningful episodes over time and modifying circumstances; many children below accepted thresholds improve with observation.",
["Correct. Documentation and disease burden matter more than a vague history.","A very small number of uncomplicated episodes does not usually justify surgery.","Tonsil size relates more directly to obstruction than infection frequency.","Medication allergy may modify management but is not by itself a universal operative indication."],
"For infection indications, count real episodes—not antibiotic prescriptions alone.","What documentation elements make an episode count as clinically meaningful?"),
_q("v244_ped_tons_app","Recurrent Tonsillitis Decision-Making","application",
"A child has recurrent severe febrile tonsillitis meeting accepted frequency thresholds with consistent documentation and major school absence. What is the best counseling framework?",
["Discuss tonsillectomy as a reasonable option while explaining natural improvement, postoperative pain/dehydration and hemorrhage risk","Promise surgery eliminates every future sore throat","Recommend indefinite prophylactic antibiotics","State that postoperative bleeding never occurs in children"],0,
"When recurrent infections are frequent, severe and well documented, tonsillectomy can reduce future throat-infection burden, but benefit must be weighed against perioperative morbidity and natural history.",
["Correct. This is preference-sensitive evidence-based counseling.","Children can still develop viral/pharyngeal infections after tonsil removal.","Chronic antibiotic prophylaxis is not routine management for recurrent tonsillitis.","Primary and secondary post-tonsillectomy hemorrhage are important known complications."],
"A valid indication does not eliminate the need to discuss natural history and surgical morbidity.","How do PFAPA, multiple antibiotic intolerance or prior peritonsillar abscess modify the decision?","clinic_decision"),
_q("v244_ped_tons_snr","Recurrent Tonsillitis Decision-Making","senior_decision",
"A child referred for tonsillectomy has many reported 'strep episodes,' but chart review shows repeated negative testing, minimal fever and symptoms dominated by chronic throat clearing and cough. What is the best senior-level decision?",
["Reassess the diagnosis and avoid surgery based on an unreliable infection count; evaluate alternative causes of chronic throat symptoms","Accept every antibiotic prescription as proof of tonsillitis","Operate because the family has already scheduled time off","Perform adenotonsillectomy regardless of indication"],0,
"A surgical threshold is only meaningful if the episodes actually represent the disease being counted. Diagnostic misclassification can turn a guideline into inappropriate surgery.",
["Correct. Validate the phenotype before applying an episode-count threshold.","Antibiotic treatment does not prove bacterial tonsillitis.","Scheduling convenience does not establish medical necessity.","Adenoid removal should also have a specific indication rather than being automatic."],
"Before counting episodes, make sure you are counting tonsillitis.","Which symptoms would redirect evaluation toward reflux, allergy, habit cough or another diagnosis?","senior_management"),

_q("v244_ped_lm_fnd","Lymphatic Malformation","foundation",
"A young child has a soft, compressible, transilluminating lateral neck mass that enlarges during viral illnesses. Imaging shows a multiloculated cystic lesion crossing tissue planes. What is the most likely diagnosis?",
["Lymphatic malformation","Thyroglossal duct cyst","Carotid body tumor","Acute mastoiditis"],0,
"Lymphatic malformations are low-flow congenital vascular anomalies that can be macrocytic, microcystic or mixed and often enlarge with infection, hemorrhage or inflammation.",
["Correct. Multiloculated trans-spatial cystic disease is characteristic.","Thyroglossal duct cyst is usually a discrete midline tract-related lesion.","Carotid body tumors are solid hypervascular bifurcation masses.","Mastoiditis is an acute postauricular infectious process."],
"A lymphatic malformation ignores fascial boundaries; that trans-spatial behavior is a diagnostic clue.","How do macrocytic and microcystic phenotypes differ in treatment response?"),
_q("v244_ped_lm_app","Lymphatic Malformation","application",
"A child has a symptomatic predominantly macrocystic cervical lymphatic malformation without airway compromise. What is a common first-line treatment strategy?",
["Image-guided sclerotherapy when anatomy is suitable, with surgery or combined therapy individualized to residual disease and functional goals","Radical neck dissection for every lesion","Antibiotics as definitive therapy despite no infection","Radiation therapy routinely"],0,
"Macrocystic lesions often respond well to sclerotherapy. Surgery is selected when disease is resectable and symptomatic, threatens function, or persists after other therapy; mixed lesions frequently require multimodal care.",
["Correct. Lesion architecture and functional morbidity guide modality choice.","Radical neck dissection is unnecessary and risks nerves/vessels for a benign malformation.","Antibiotics treat superinfection, not the congenital anomaly.","Radiation is not routine therapy for lymphatic malformation."],
"Treat the malformation phenotype, not just the fact that a neck mass exists.","Which agents are commonly used for sclerotherapy and what inflammatory swelling should be anticipated?","boards"),
_q("v244_ped_lm_snr","Lymphatic Malformation","senior_decision",
"A child with a large floor-of-mouth and cervical lymphatic malformation acutely enlarges after intralesional hemorrhage and develops tongue elevation and stridor. What should dominate management?",
["Airway stabilization and multidisciplinary control of the acute expansion before definitive lesion therapy","Elective cosmetic planning first","Needle aspiration at bedside without imaging or airway backup","Observation at home because lymphatic malformations are benign"],0,
"Benign histology does not make acute airway compromise benign. Floor-of-mouth/tongue-base expansion can rapidly obstruct the airway, and intervention must account for anticipated post-procedure edema as well.",
["Correct. Airway physiology outranks definitive lesion eradication during acute compromise.","Cosmetic concerns are secondary during respiratory deterioration.","Unplanned aspiration can bleed, infect or fail and may worsen an already tenuous airway.","Stridor and tongue elevation require monitored urgent care."],
"A benign vascular anomaly can still be an airway emergency.","How would anticipated post-sclerotherapy swelling alter the airway plan?","overnight_call"),

_q("v244_ped_bca_fnd","Branchial Cleft Anomalies","foundation",
"A child has a recurrent lateral neck cyst near the anterior border of the sternocleidomastoid without acute infection. Which congenital category is most likely?",
["Branchial cleft anomaly","Thyroglossal duct cyst","Ranula","Dermoid of the midline floor of mouth"],0,
"Branchial cleft anomalies classically present as lateral cervical cysts, sinuses or fistulae, with location and tract relationships reflecting embryologic origin.",
["Correct. A recurrent congenital lateral neck lesion fits a branchial anomaly.","Thyroglossal remnants are usually midline and hyoid-related.","Ranulas arise from the sublingual space.","Dermoids are typically midline developmental lesions."],
"Lateral congenital neck masses are an embryology map, not just a cyst differential.","Which carotid and cranial-nerve relationships help distinguish second- from third/fourth-cleft tracts?"),
_q("v244_ped_bca_app","Branchial Cleft Anomalies","application",
"A child has recurrent left suppurative thyroid-region infections beginning in early childhood, and imaging suggests a tract toward the piriform sinus apex. Which congenital lesion should be considered?",
["Third- or fourth-branchial pouch sinus/piriform sinus tract","Second branchial cyst only","Thyroglossal duct cyst","Parotid sialolithiasis"],0,
"Recurrent left-sided lower-neck or suppurative thyroid-region infection is a classic clue to a piriform sinus tract from third/fourth pouch anomaly, with fourth-pouch lesions especially associated with the left side.",
["Correct. Recurrent lower-neck infection with piriform sinus communication is the key pattern.","A typical second-cleft lesion occupies a different tract and does not communicate with the piriform apex.","Thyroglossal lesions are midline rather than piriform-sinus tracts.","Parotid stones cause meal-related parotid symptoms, not recurrent suppurative thyroiditis."],
"Recurrent left suppurative thyroiditis in a child should trigger a piriform-sinus tract search.","Why can the tract be difficult to identify during acute inflammation?","boards"),
_q("v244_ped_bca_snr","Branchial Cleft Anomalies","senior_decision",
"A child with a known branchial tract presents during acute infection with cellulitis and a poorly defined inflamed tract. What is the best definitive-management principle?",
["Control the acute infection first, then perform anatomy-directed tract treatment when inflammation has settled unless airway/sepsis requires urgent drainage","Attempt extensive tract dissection through uncontrolled infection in every case","Ignore recurrent infection indefinitely","Perform total thyroidectomy for every branchial anomaly"],0,
"Acute infection distorts tissue planes and raises nerve/vessel injury risk. Source control may be urgent for abscess or airway compromise, but definitive tract excision or endoscopic treatment is usually safer after inflammation improves.",
["Correct. Separate acute source control from elective definitive tract eradication when clinically possible.","Inflamed planes make complete safe tract dissection harder and recurrence more likely.","Untreated tracts can produce recurrent infection.","Thyroidectomy is not routine treatment for branchial anomalies."],
"Drain what is dangerous now; eradicate the congenital tract when the anatomy is safer to define.","Which nerves are at risk during first-, second-, third- and fourth-cleft tract surgery?","OR_prep")]

def apply_learning_ladders_v244(challenges,item_id_fn):
    existing={q.get("id") for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V244:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v244 orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
