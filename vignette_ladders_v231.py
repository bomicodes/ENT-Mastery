"""v23.1 — Head & Neck Oncology learning-ladder closure.

Closes the three remaining canonical H&N topics identified by the live v21.7
inventory: Complications of Neck Surgery, Carotid Blowout Syndrome, and
Nonfunctional Larynx and Intractable Aspiration.
"""
DOMAIN="Head & Neck Oncology"


def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,
            "stem":stem,"choices":choices,"answer":answer,"explanation":explanation,
            "why_wrong":why_wrong,"board_pearl":pearl,"curveball":curveball,
            "tier":"Curated learning ladder","mode":"Vignette","focus":focus,
            "ladder_reviewed":True}


VIGNETTES_V231=[
_q("v231_hn_neckcomp_fnd","Complications of Neck Surgery","foundation",
"After a left lateral neck dissection, a patient has a milky drain output that increases after enteral feeding. Which complication is most likely?",
["Chyle leak from thoracic-duct or lymphatic injury","Pharyngocutaneous fistula","Carotid blowout","Recurrent laryngeal nerve paralysis"],0,
"Milky cervical drainage that increases with dietary fat is classic for a postoperative chyle leak, particularly after lower left-neck dissection where the thoracic duct enters the venous system. The complication matters because persistent high-output loss can cause volume, protein, electrolyte, lymphocyte, and nutritional depletion.",
["Correct. Meal-related milky drainage after lower neck surgery strongly suggests chyle leakage.","A pharyngocutaneous fistula produces salivary contamination rather than characteristic lipid-rich milky drainage.","Carotid blowout presents with hemorrhage, not enteral-feed-responsive milky drainage.","Vocal-fold dysfunction does not cause this drain phenotype."],
"After neck surgery, the character of drain output can localize the injured system.",
"How would low-output versus persistent high-output chyle loss change dietary, interventional, and operative management?","postoperative_call"),

_q("v231_hn_neckcomp_app","Complications of Neck Surgery","application",
"On postoperative day 1 after neck dissection, a patient has shoulder droop, difficulty abducting the arm above shoulder level, and trapezius weakness despite an anatomically preserved spinal accessory nerve. What is the best interpretation and early management principle?",
["Expected mandibular nerve palsy requiring no follow-up","Accessory-nerve dysfunction from traction/devascularization; document function and begin shoulder-focused rehabilitation while monitoring recovery","Immediate carotid ligation","Thoracic-duct injury"],1,
"Spinal accessory dysfunction can occur even when the nerve is preserved, owing to traction, skeletonization, devascularization, or neuropraxia. Early recognition and physical therapy help limit chronic shoulder pain, scapular dyskinesis, and loss of range of motion; persistent severe deficits warrant further evaluation.",
["The mandibular division of CN V does not innervate trapezius.","Correct. Nerve preservation does not guarantee normal function, and early rehabilitation matters.","There is no hemorrhagic indication for carotid ligation.","Thoracic-duct injury causes chyle leakage rather than isolated trapezius weakness."],
"A preserved nerve can still be a dysfunctional nerve; postoperative examination belongs in the operation's outcome assessment.",
"Which additional deficits after level II-IV surgery should prompt evaluation of hypoglossal, vagal, phrenic, sympathetic-chain, or marginal-mandibular injury?","postoperative_call"),

_q("v231_hn_neckcomp_snr","Complications of Neck Surgery","senior_decision",
"Several days after salvage neck surgery in an irradiated field, the wound breaks down and the carotid sheath becomes exposed beneath infected salivary contamination. There is no major hemorrhage yet. What is the best attending-level principle?",
["Treat as a routine superficial wound and wait for spontaneous granulation","Recognize threatened major-vessel exposure, control infection and salivary contamination, obtain urgent vascular/interventional planning, and provide durable vascularized tissue coverage when feasible","Debride directly over the carotid at bedside","Restart oral intake to test the wound"],1,
"An exposed carotid in an infected or salivary-contaminated irradiated wound is a sentinel high-risk state for arterial rupture. Management must address the source of contamination, infection, vessel status, and tissue coverage rather than treating the skin defect alone. Vascularized tissue may be required to protect the artery and close the wound.",
["Observation alone can allow progression to catastrophic hemorrhage.","Correct. Vessel protection and source control are the priorities before blowout occurs.","Uncontrolled bedside manipulation of an exposed carotid can precipitate hemorrhage.","Oral intake can worsen salivary contamination when a pharyngeal leak is present."],
"In a radiated neck, carotid exposure is a vascular emergency in evolution even before active bleeding starts.",
"What imaging or endovascular options become important if pseudoaneurysm or vessel-wall irregularity is suspected?","overnight_call"),

_q("v231_hn_cbs_fnd","Carotid Blowout Syndrome","foundation",
"A previously irradiated head-and-neck cancer patient with wound breakdown has a brief episode of brisk oral bleeding that stops spontaneously. What is the most important interpretation?",
["Benign mucosal irritation","A possible sentinel bleed from threatened carotid blowout requiring urgent evaluation","Expected radiation dryness","Simple epistaxis until proven otherwise"],1,
"Carotid blowout syndrome ranges from threatened exposure to sentinel hemorrhage to active rupture. A self-limited high-volume bleed in a previously irradiated or surgically violated neck can precede catastrophic exsanguination and requires urgent airway, hemorrhage, and vascular evaluation.",
["The host and wound context make a benign explanation unsafe without evaluation.","Correct. Sentinel bleeding may be the only warning before complete arterial rupture.","Radiation xerostomia does not explain brisk hemorrhage.","Assuming routine epistaxis can delay life-saving vascular assessment."],
"A sentinel bleed is a warning shot, not reassurance because it stopped.",
"Which prior treatments and wound findings increase carotid blowout risk?","overnight_call"),

_q("v231_hn_cbs_app","Carotid Blowout Syndrome","application",
"A patient with recurrent irradiated oropharyngeal cancer develops active massive pharyngeal hemorrhage with hypotension. What is the immediate management priority?",
["Send the patient for routine outpatient CT","Activate massive-hemorrhage resuscitation, secure or protect the airway without delaying hemorrhage control, and obtain emergent endovascular/surgical vascular control","Pack the mouth and leave the patient unmonitored","Give oral antibiotics and observe"],1,
"Active carotid blowout is a simultaneous airway, resuscitation, and vascular-control emergency. Large-bore access, blood-product resuscitation, experienced airway management, direct pressure/packing as a bridge when appropriate, and immediate interventional or operative vascular control should occur in parallel.",
["An unstable hemorrhaging patient cannot enter a routine outpatient pathway.","Correct. Airway protection, balanced resuscitation, and definitive vascular control are simultaneous priorities.","Temporary packing without monitored definitive control can fail abruptly and does not address shock.","Antibiotics do not control major arterial hemorrhage."],
"In carotid blowout, do not sequence airway, blood, and vascular control leisurely—they are parallel emergencies.",
"How does an endovascular covered stent differ from vessel sacrifice in recurrent bleeding, stroke, infection, and antiplatelet considerations?","overnight_call"),

_q("v231_hn_cbs_snr","Carotid Blowout Syndrome","senior_decision",
"Angiography in a hemodynamically stabilized patient shows a focal carotid pseudoaneurysm adjacent to an infected irradiated wound. Balloon-occlusion testing suggests poor collateral tolerance of carotid sacrifice. What should drive the senior treatment decision?",
["Sacrifice the carotid regardless of cerebral perfusion","Balance cerebral ischemic risk, infection/contamination, lesion anatomy, durability, and rebleeding risk when choosing reconstructive endovascular treatment versus sacrifice or surgical options","Observe because the patient is temporarily stable","Start anticoagulation alone"],1,
"Management of threatened or contained carotid blowout is individualized. Vessel sacrifice may provide durable hemorrhage control but can cause stroke when collateral circulation is inadequate; covered stenting can preserve flow but introduces thrombosis, antiplatelet, infection, and rebleeding concerns in contaminated fields. Multidisciplinary vascular decision-making is essential.",
["Poor collateral tolerance makes unselected vessel sacrifice dangerous.","Correct. The safest hemorrhage-control strategy depends on both the artery and the brain it supplies.","Pseudoaneurysm in this context remains at risk for catastrophic rupture despite temporary stability.","Anticoagulation alone neither repairs the pseudoaneurysm nor controls impending hemorrhage."],
"Carotid blowout treatment is not only about stopping bleeding; it is also about preserving cerebral perfusion when possible.",
"When is a technically successful covered stent still a poor long-term solution because of infected tissue or persistent tumor erosion?","boards"),

_q("v231_hn_nfl_fnd","Nonfunctional Larynx and Intractable Aspiration","foundation",
"Years after chemoradiation, a disease-free patient has profound dysphagia, recurrent aspiration pneumonia, feeding-tube dependence, and a severely fibrotic larynx. What is the best conceptual diagnosis?",
["Successful organ preservation because the larynx remains anatomically present","A nonfunctional larynx with late treatment-related swallowing failure and intractable aspiration","Acute bacterial laryngitis","Normal survivorship"],1,
"An anatomically preserved larynx can become functionally useless or dangerous because of radiation fibrosis, sensory loss, impaired airway closure, stenosis, chondronecrosis, or neuromuscular dysfunction. Recurrent aspiration pneumonia and feeding dependence indicate major functional failure even in the absence of recurrent cancer.",
["Anatomical preservation without safe airway/swallow function is not a successful functional outcome.","Correct. Late laryngeal dysfunction can become a life-threatening survivorship problem.","The chronic fibrotic syndrome does not fit an acute infection.","Recurrent pneumonia and tube dependence are not normal survivorship findings."],
"Organ preservation is only meaningful when the preserved organ can function safely.",
"Which late radiation changes can progressively worsen swallowing years after treatment?","boards"),

_q("v231_hn_nfl_app","Nonfunctional Larynx and Intractable Aspiration","application",
"A disease-free head-and-neck cancer survivor has repeated aspiration pneumonias despite diet modification, swallowing therapy, and enteral nutrition. Instrumental swallowing evaluation shows gross aspiration of secretions and poor laryngeal sensation. What is the best next management framework?",
["Continue the same conservative plan indefinitely regardless of pulmonary complications","Discuss aspiration-prevention surgical options after confirming cancer status, pulmonary risk, residual communication goals, and failure of rehabilitative strategies","Perform elective neck dissection","Treat with repeated antibiotics alone"],1,
"When aspiration is severe, persistent, and life-threatening despite maximal rehabilitation, definitive aspiration-prevention surgery may be appropriate. Options include total laryngectomy in selected patients and other procedures that separate or close the airway depending on anatomy, prior treatment, voice goals, and reconstructive needs.",
["Repeated pneumonia despite maximal therapy means conservative management has failed its safety endpoint.","Correct. The goal shifts from preserving laryngeal anatomy to preventing life-threatening pulmonary contamination.","Neck dissection does not correct aspiration physiology.","Antibiotics treat infections but not the recurrent aspiration mechanism."],
"When aspiration becomes life-threatening, airway separation can be rehabilitative rather than oncologic surgery.",
"How do total laryngectomy, laryngotracheal separation, and other aspiration-prevention procedures differ in voice and reconstructive implications?","boards"),

_q("v231_hn_nfl_snr","Nonfunctional Larynx and Intractable Aspiration","senior_decision",
"A disease-free salvage patient requests total laryngectomy solely for chronic aspiration and a nonfunctional irradiated larynx. The neck is fibrotic, nutrition is poor, and prior fistula history raises wound risk. What is the best attending-level planning principle?",
["Decline surgery because laryngectomy is only an oncologic procedure","Treat this as functional salvage surgery: confirm the aspiration mechanism and goals, optimize nutrition/pulmonary status, anticipate irradiated wound risk, and plan vascularized reconstruction when needed","Promise normal swallowing after surgery","Ignore speech rehabilitation because cancer is absent"],1,
"Total laryngectomy can be used for a nonfunctional larynx when aspiration and pulmonary morbidity are otherwise uncontrollable. In a heavily irradiated field, the operation requires the same attention to fistula prevention, pharyngeal reconstruction, nutrition, pulmonary reserve, and alaryngeal communication as oncologic salvage surgery.",
["Laryngectomy can be indicated for irreversible functional failure even without active malignancy.","Correct. Functional salvage still demands rigorous reconstructive and rehabilitation planning.","Swallowing often improves by eliminating aspiration, but dysphagia can persist from pharyngeal fibrosis or stenosis.","Voice restoration and communication planning remain central to quality of life."],
"A functional laryngectomy removes a dangerous organ to restore pulmonary safety; it is not a lesser operation because there is no tumor.",
"What findings would favor primary flap reinforcement rather than simple pharyngeal closure in this irradiated field?","OR_prep"),
]


def apply_learning_ladders_v231(challenges,item_id_fn):
    existing={str(q.get("id")) for q in challenges if q.get("id")}
    added=0
    for q in VIGNETTES_V231:
        row=dict(q)
        row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]:
            raise RuntimeError("v231 orphan: "+row["topic"])
        if row["id"] not in existing:
            challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":3}
