"""v27.1 — General ENT / Emergencies deliberate ladder pass 3.

Five exact canonical overnight-call emergency concepts. Existing near-neighbor
material was reviewed first; none provided a strong exact-canonical application
case without relabeling, so each concept receives a purpose-built foundation ->
application -> senior_decision ladder. Rationales are choice-aligned so the
deterministic answer balancer can safely move answer positions.
"""
DOMAIN="General ENT / Emergencies"

def _q(qid,topic,stage,stem,choices,answer,exp,reasons,pearl,curveball,focus="boards"):
 return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,"choices":choices,"answer":answer,"explanation":exp,"why_wrong":reasons,"board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder","mode":"Vignette","focus":focus,"ladder_reviewed":True,"_coverage_reviewed_v211":True}

VIGNETTES_V271=[
_q("v271_gen_pth_fnd","Post-Tonsillectomy Hemorrhage","foundation",
   "A child presents on postoperative day 7 after tonsillectomy after coughing up bright-red blood at home. No active bleeding is visible now. What is the safest interpretation?",
   ["Treat the reported bleed as a potentially significant secondary post-tonsillectomy hemorrhage requiring urgent monitored assessment, IV access and ENT evaluation","Discharge because the oropharynx is currently dry","Assume swallowed blood cannot recur","Give food immediately to test swallowing"],0,
   "Secondary post-tonsillectomy hemorrhage commonly occurs when the eschar separates. Bleeding may stop before examination, but a credible sentinel bleed predicts rebleeding risk and deserves urgent assessment rather than reassurance from a temporarily dry field.",
   ["Correct. A credible postoperative tonsil bleed remains high risk even when bleeding has temporarily stopped.","A dry examination does not erase a witnessed or reported hemorrhage and may represent temporary clotting.","Blood is often swallowed, and intermittent bleeding can recur abruptly.","Patients at risk for operative control should remain NPO rather than receive a provocative oral challenge."],
   "A post-tonsillectomy bleed is a hemorrhage history first and an oropharyngeal snapshot second.",
   "What findings would make you move from monitored evaluation to urgent operative control?","overnight_call"),
_q("v271_gen_pth_app","Post-Tonsillectomy Hemorrhage","application",
   "A 9-year-old has active bright-red tonsillar-fossa bleeding, tachycardia and repeated swallowing. What is the best immediate management framework?",
   ["Activate ENT/anesthesia, position for suction and airway protection, obtain IV access with resuscitation/labs/type-and-screen, keep NPO, and proceed toward definitive hemorrhage control","Send the child unmonitored for CT angiography before resuscitation","Perform repeated blind bedside cautery in an uncooperative child","Wait for hemoglobin to fall before escalating"],0,
   "Active post-tonsillectomy hemorrhage is a shared airway and blood-loss emergency. Airway readiness, suction, vascular access, resuscitation and definitive source control occur in parallel; a normal early hemoglobin does not exclude major acute blood loss.",
   ["Correct. Stabilization and definitive source control must proceed together in active bleeding.","Routine CT delays treatment of an obvious surgical-site hemorrhage and may be unsafe during active airway contamination.","Blind manipulation in a bleeding, uncooperative child can worsen hemorrhage and jeopardize the airway.","Hemoglobin can lag behind acute blood loss; physiology and ongoing bleeding determine urgency."],
   "Do not wait for the CBC to prove the hemorrhage you can already see.",
   "How do swallowed blood, induction of anesthesia and a full stomach change aspiration planning?","overnight_call"),
_q("v271_gen_pth_snr","Post-Tonsillectomy Hemorrhage","senior_decision",
   "A child with recurrent post-tonsillectomy bleeding becomes pale and hypotensive while brisk bleeding obscures the oropharynx. What is the best senior decision?",
   ["Treat this as hemorrhagic shock with a contaminated difficult airway: mobilize blood products and an experienced anesthesia/ENT team for immediate operative airway and source control rather than delaying for diagnostic refinement","Observe after topical vasoconstrictor because most bleeds stop spontaneously","Delay intervention until coagulation studies return","Attempt prolonged bedside visualization despite worsening shock"],0,
   "Shock plus ongoing tonsillar hemorrhage mandates immediate resuscitation and operative control. The senior task is coordinating a potentially difficult induction with suction, blood availability, aspiration risk and rapid surgical hemostasis, not perfecting the diagnosis.",
   ["Correct. Hemorrhagic shock and ongoing airway contamination require immediate coordinated resuscitation and operative control.","Transient hemostasis is not an acceptable endpoint in a patient already in shock.","Laboratory clarification should not delay lifesaving airway, transfusion and source control.","Persistent bedside attempts waste time and may worsen aspiration or decompensation."],
   "In severe tonsil hemorrhage, the airway plan and massive-bleeding plan are the same conversation.",
   "If bleeding persists despite local operative control, what vascular escalation options should be considered?","senior_decision"),

_q("v271_gen_dnsi_fnd","Deep Neck Space Infection","foundation",
   "An adult has fever, trismus, muffled voice and progressive lateral neck swelling. Which principle should guide initial evaluation for a deep neck space infection?",
   ["Assess airway trajectory first; if stable enough, obtain contrast-enhanced CT to define involved spaces, drainable collection and vascular or mediastinal extension","Obtain noncontrast radiographs only and discharge","Assume every deep neck infection is a peritonsillar abscess","Delay antibiotics until every culture is finalized"],0,
   "Deep neck infections can cross fascial planes and threaten the airway. Contrast CT is the usual rapid anatomic map in a stable patient, while airway instability takes precedence over transport or imaging.",
   ["Correct. Airway trajectory determines whether imaging is safe, and contrast CT defines extent and complications when the patient is stable.","Plain radiographs do not reliably map complex deep neck spaces or abscess extent.","Parapharyngeal, retropharyngeal, submandibular and other spaces require different drainage and complication planning.","Empiric antimicrobial therapy should not be withheld in a clinically significant infection while awaiting final cultures."],
   "The scan is a map; the airway determines whether the patient is safe enough to get the map.",
   "Which symptoms suggest retropharyngeal or danger-space extension toward the mediastinum?","boards"),
_q("v271_gen_dnsi_app","Deep Neck Space Infection","application",
   "CT shows a 4-cm rim-enhancing parapharyngeal collection with carotid displacement in a septic patient whose trismus and dysphagia are worsening despite IV antibiotics. What is the best next step?",
   ["Reassess and secure the airway as needed, then obtain timely anatomically planned drainage with cultures while continuing broad IV antimicrobial therapy and addressing the source","Continue antibiotics alone indefinitely because surgery is never needed","Perform blind bedside aspiration toward the carotid sheath","Discharge once analgesia improves"],0,
   "A large organized collection with sepsis, progression and airway symptoms has strong indications for source control. Drainage approach must respect the involved compartment and adjacent carotid sheath/cranial nerve anatomy.",
   ["Correct. Progressive organized deep-space infection requires airway planning, source control, cultures and antibiotics.","Failure of medical therapy plus a large collection and sepsis argues against indefinite medical management alone.","Blind instrumentation near displaced great vessels is unsafe.","Clinical improvement in pain alone does not neutralize sepsis or an enlarging deep-space collection."],
   "Deep-neck drainage is an anatomy operation, not simply 'draining pus.'",
   "When might a transcervical route be safer than a transoral route?","OR_prep"),
_q("v271_gen_dnsi_snr","Deep Neck Space Infection","senior_decision",
   "After drainage of a deep neck infection, the patient develops persistent sepsis, chest pain and new pleural effusions. What is the best senior response?",
   ["Suspect missed-space infection or descending necrotizing mediastinitis, urgently image the neck/chest if physiology permits and involve thoracic/critical-care teams for additional source control","Call this expected postoperative inflammation and wait several days","Remove all drains immediately","Narrow to oral antibiotics without reassessment"],0,
   "Failure after drainage is a localization problem until proven otherwise. Deep cervical infection can descend through fascial planes into the mediastinum and requires rapid multidisciplinary source control rather than simple antibiotic substitution.",
   ["Correct. Persistent sepsis plus chest findings after deep-neck infection demands urgent evaluation for descending spread or incomplete source control.","Chest pain and pleural changes with ongoing sepsis are not routine postoperative findings.","Removing drainage before reassessing persistent infection can worsen source control.","De-escalating therapy without identifying an uncontrolled source is unsafe."],
   "When the patient worsens after drainage, ask which space, vessel or mediastinal compartment you missed.",
   "How would internal-jugular thrombosis with septic pulmonary emboli change the differential and workup?","senior_decision"),

_q("v271_gen_trach_fnd","Tracheostomy Emergency","foundation",
   "A tracheostomy patient suddenly becomes distressed and the ventilator shows high pressures. What is the first bedside troubleshooting sequence?",
   ["Call for help, give oxygen to both face and stoma when appropriate, remove attachments/inner cannula, pass suction to test patency and rapidly distinguish obstruction from displacement","Immediately force a larger tube into the stoma","Assume the ventilator is malfunctioning and leave the bedside","Occlude the stoma before assessing upper-airway patency"],0,
   "The initial tracheostomy emergency approach is rapid oxygenation plus simple reversible checks. Inability to pass a suction catheter strongly suggests obstruction or displacement and should trigger immediate airway escalation.",
   ["Correct. Oxygenation, removing simple obstructions and testing tube patency quickly identify the common reversible causes.","Blind forceful replacement can create a false passage, especially in an immature tract.","A distressed tracheostomy patient requires immediate airway assessment, not abandonment for equipment troubleshooting.","Whether the upper airway can be used depends on the indication and anatomy; premature occlusion can worsen obstruction."],
   "If a suction catheter will not pass, treat the trach as blocked or displaced until proven otherwise.",
   "Why is knowing whether this is a tracheostomy versus a total-laryngectomy stoma lifesaving?","overnight_call"),
_q("v271_gen_trach_app","Tracheostomy Emergency","application",
   "On postoperative day 2 after a new tracheostomy, the tube is accidentally displaced and a suction catheter cannot enter the trachea. The patient is desaturating but has a potentially patent upper airway. What is the safest next principle?",
   ["Do not blindly probe the immature tract; oxygenate and ventilate from above if possible while activating experienced airway help and preparing controlled recannulation or surgical airway rescue","Repeatedly force the same tube through resistance","Wait for the tract to mature","Pack the stoma tightly closed before oxygenation"],0,
   "A fresh tracheostomy tract can collapse and false passage is easy to create. Early displacement is therefore an airway emergency requiring oxygenation from the best available route and controlled recannulation by an experienced team.",
   ["Correct. An immature tract should not be blindly instrumented; oxygenation and controlled airway rescue come first.","Forceful blind replacement risks pretracheal false passage and complete loss of the airway.","A hypoxemic patient cannot wait days for tract maturation.","Packing the stoma does not solve loss of airway access and may impair rescue."],
   "Fresh trach displacement is not the same procedure as changing a mature trach.",
   "How would the plan differ if the patient had a total laryngectomy and no connection between mouth and lungs?","overnight_call"),
_q("v271_gen_trach_snr","Tracheostomy Emergency","senior_decision",
   "A mature tracheostomy patient cannot be ventilated through the tube; suction will not pass, removing the tube does not restore breathing, and the patient has no usable upper airway because of complete obstruction above. What is the best senior action?",
   ["Ventilate through the stoma with appropriate equipment while urgently re-establishing a patent tracheal airway under direct/controlled conditions and preparing surgical revision if needed","Focus exclusively on oral intubation despite known complete upper-airway obstruction","Replace the blocked tube repeatedly without visualization","Wait for chest radiography before attempting oxygenation"],0,
   "When the upper airway cannot be used, the stoma is the only route to the lungs. Senior management prioritizes stoma oxygenation/ventilation and controlled restoration of tracheal access, with bronchoscopy or surgical exposure as required.",
   ["Correct. With no usable upper airway, oxygenation and definitive airway restoration must occur through the neck route.","Oral intubation cannot bypass a known complete obstruction above the tracheostomy.","Repeated blind exchanges risk trauma and false passage without fixing the underlying problem.","Imaging cannot precede restoration of oxygenation in a failing airway."],
   "Always know whether the patient can be ventilated from above before a tracheostomy emergency occurs.",
   "What clues suggest a distal mucus plug versus a false passage versus cuff-related obstruction?","senior_decision"),

_q("v271_gen_epi_fnd","Epistaxis","foundation",
   "A stable adult has brisk anterior epistaxis from the septum. What is the best initial treatment sequence?",
   ["Sit the patient forward, apply firm continuous compression to the soft nose, use topical vasoconstrictor/anesthetic when appropriate, suction/localize and then cauterize or pack if needed","Tilt the head backward and repeatedly release pressure to check","Immediately obtain CT angiography for every nosebleed","Pack both posterior nasal cavities before attempting localization"],0,
   "Most epistaxis begins with positioning, sustained compression and topical therapy, followed by localization and focused treatment. Airway/hemodynamic instability changes the priority, but routine anterior bleeding does not require immediate advanced imaging.",
   ["Correct. Proper positioning, uninterrupted compression and targeted local therapy are first-line for a stable anterior source.","Head-back positioning promotes swallowing/aspiration of blood, and repeatedly releasing pressure prevents tamponade.","Routine uncomplicated anterior epistaxis is a clinical problem and does not require CTA.","Posterior packing has substantial morbidity and should not precede simpler targeted measures for an anterior source."],
   "Pressure means continuous pressure on the soft cartilaginous nose—not pinching the nasal bones for 30 seconds.",
   "How do anticoagulation, hypertension and a posterior bleeding pattern change disposition?","boards"),
_q("v271_gen_epi_app","Epistaxis","application",
   "An older anticoagulated patient has ongoing heavy epistaxis with blood in the oropharynx despite topical therapy and appropriate anterior packing. What is the best next framework?",
   ["Resuscitate and protect the airway as needed, suspect posterior bleeding, use effective posterior/endoscopic control and coordinate antithrombotic management based on bleeding severity and thrombotic risk","Continue adding traumatic anterior packs indefinitely","Stop all anticoagulation permanently without assessing indication","Discharge because the anterior nasal cavity looks dry"],0,
   "Persistent high-volume bleeding into the pharynx despite anterior measures suggests a posterior source or uncontrolled arterial bleeding. Management combines physiology, airway protection, source control and individualized reversal/holding decisions.",
   ["Correct. Severe suspected posterior bleeding requires escalation beyond repeated anterior measures while resuscitation and medication decisions occur in parallel.","Repeated packing without localization increases trauma and may not control a posterior artery.","Antithrombotic decisions require balancing hemorrhage severity against the indication and thrombosis risk.","A dry anterior cavity does not exclude blood flowing posteriorly into the pharynx."],
   "Posterior epistaxis is defined clinically by the behavior of the bleed, not merely by failing to see an anterior point.",
   "Which patients with posterior packing require monitored admission and why?","overnight_call"),
_q("v271_gen_epi_snr","Epistaxis","senior_decision",
   "A patient continues to require transfusion for posterior epistaxis despite packing. Endoscopy suggests a sphenopalatine arterial source and the patient is stable for the OR. What is the best senior decision?",
   ["Proceed to definitive endoscopic arterial control such as sphenopalatine artery ligation/cautery, with embolization reserved or selected based on anatomy, operative risk and failure pattern","Repeat the same packing indefinitely","Perform external carotid ligation as the routine first-line procedure","Delay definitive control until shock develops"],0,
   "Refractory posterior epistaxis is better managed with definitive arterial source control than cycles of packing. Endoscopic sphenopalatine control is commonly favored when feasible; embolization is an important alternative or rescue strategy with its own neurologic/vascular risks.",
   ["Correct. Ongoing transfusion-requiring posterior hemorrhage warrants definitive arterial control rather than repeated temporizing packs.","Repeated packing prolongs morbidity and does not address a persistently bleeding arterial source.","More proximal external ligation is generally not the routine first definitive approach when endoscopic distal control is feasible.","Waiting for shock exposes the patient to avoidable blood loss and airway risk."],
   "Know when packing has become a bridge rather than a treatment.",
   "What vascular history or imaging finding would make embolization particularly hazardous?","senior_decision"),

_q("v271_gen_lud_fnd","Ludwig Angina","foundation",
   "A patient with a mandibular molar infection has bilateral woody submandibular swelling, floor-of-mouth elevation and a posteriorly displaced tongue. What diagnosis and immediate concern are most important?",
   ["Ludwig angina with impending upper-airway compromise","Simple viral pharyngitis with no airway risk","Isolated parotitis","Peritonsillar abscess limited to one tonsillar fossa"],0,
   "Ludwig angina is rapidly progressive cellulitis of the submandibular/sublingual spaces, usually odontogenic. Floor-of-mouth edema and tongue displacement can make both ventilation and intubation progressively difficult.",
   ["Correct. Bilateral floor-of-mouth/submandibular cellulitis with tongue elevation is classic Ludwig angina and the airway is the immediate threat.","The described brawny bilateral floor-of-mouth process is not typical viral pharyngitis.","Parotitis localizes to the parotid region rather than elevating the floor of mouth and tongue.","A unilateral peritonsillar process does not explain bilateral submandibular induration and floor-of-mouth elevation."],
   "In Ludwig angina, the patient can lose the airway before a discrete abscess ever forms.",
   "Which bedside signs should make you secure the airway before attempting CT?","boards"),
_q("v271_gen_lud_app","Ludwig Angina","application",
   "A patient with Ludwig angina is drooling, cannot tolerate supine positioning and has increasing work of breathing but is still maintaining oxygen saturation while sitting upright. What is the best next step?",
   ["Secure the airway early with an experienced multidisciplinary plan that preserves spontaneous ventilation when appropriate, with surgical-airway backup, while starting IV antibiotics and source-control planning","Give sedatives and paralyze before an airway strategy is agreed","Send the patient supine to CT before airway intervention","Observe until oxygen saturation falls"],0,
   "Progressive symptoms, drooling and positional intolerance signal a precarious airway. Loss of tone after sedation or induction can convert partial obstruction to complete obstruction, so airway control should precede nonessential imaging.",
   ["Correct. A controlled airway strategy before decompensation is safer than waiting for complete obstruction.","Unplanned sedation/paralysis can abolish the remaining airway in severe floor-of-mouth obstruction.","Supine transport can worsen obstruction and delays control of the immediate threat.","Normal saturation can persist until late and should not be used as the threshold for securing a deteriorating airway."],
   "The dangerous Ludwig airway may still have a normal pulse oximeter until it suddenly does not.",
   "What anatomy would push you toward awake tracheostomy rather than awake transoral intubation?","overnight_call"),
_q("v271_gen_lud_snr","Ludwig Angina","senior_decision",
   "After airway control and broad IV antibiotics for Ludwig angina, CT shows a drainable submandibular collection and an infected mandibular molar. What is the best definitive management principle?",
   ["Drain the involved spaces and obtain odontogenic source control while continuing culture-directed antimicrobial therapy; airway stabilization alone is not definitive treatment","Remove the airway and observe without treating the dental source","Continue antibiotics indefinitely without drainage despite an organized collection","Perform tonsillectomy as the primary source-control operation"],0,
   "Once the airway is secure, definitive treatment addresses both any organized infected collection and the odontogenic source. Failure to control the tooth or involved fascial spaces predisposes to persistence and recurrent sepsis.",
   ["Correct. Durable treatment requires source control of the infected spaces and dental origin in addition to antimicrobial therapy.","Airway control buys time but does not eradicate the infection or diseased tooth.","An organized drainable collection generally requires source control rather than indefinite antibiotics alone.","The primary source in classic Ludwig angina is commonly odontogenic, not the tonsil."],
   "Airway control is step one; source control is what cures the disease.",
   "How would extension into the parapharyngeal or mediastinal spaces alter operative planning?","senior_decision"),
]

def apply_learning_ladders_v271(challenges,item_id_fn):
 existing={str(q.get("id")) for q in challenges if q.get("id")}; added=0
 for q in VIGNETTES_V271:
  if q["id"] in existing: continue
  row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
  if not row["concept_id"]: raise RuntimeError(f"v271 orphan topic {row['topic']}")
  challenges.append(row); existing.add(row["id"]); added+=1
 return {"added":added,"topics":sorted({q["topic"] for q in VIGNETTES_V271})}
