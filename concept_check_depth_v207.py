"""v20.7 — deepen exact live General ENT / Emergencies Esophageal Foreign Body Concept Checks.

Durable anatomy, endoscopic exposure, foreign-body localization, and perforation principles are
cross-checked against Cummings 7e chapter 211 (Pediatric Aerodigestive Foreign Bodies), Pasha 6e,
and K.J. Lee 12e in the connected Drive corpus. Contemporary object-specific timing is updated
against the 2026 ESPGHAN position paper and current National Capital Poison Center button-battery guidance.
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V207 = [
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed., Ch. 211 Pediatric Aerodigestive Foreign Bodies, pp. ~3124-3126 in connected Drive split corpus; re-verified 2026-09-04.","role":"foundation/operative: symptoms and localization, AP/lateral radiography, coin-versus-button-battery signs, endoscopic retrieval principles, mucosal injury and delayed complications"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), pediatric laryngoesophagology/esophageal and swallowing sections; connected Drive copy re-verified 2026-09-04.","role":"foundation/operative: cervical esophageal anatomy, rigid endoscopy, foreign-body and food-impaction management"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), chapters on oral cavity/pharynx/esophagus and pediatric otolaryngology; connected Drive copy re-verified 2026-09-04.","role":"foundation/operative: esophageal anatomy, aerodigestive foreign-body presentation, endoscopic rescue and perforation awareness"},
 {"type":"position_statement","citation":"Ledder O, et al. Foreign body ingestions in children and adolescents: A position paper of the ESPGHAN endoscopy special interest group. J Pediatr Gastroenterol Nutr. 2026; doi:10.1002/jpn3.70485.","role":"current management: object type, anatomic location, symptoms and time since ingestion drive intervention urgency and endoscopic strategy"},
 {"type":"toxicology_guideline","citation":"National Capital Poison Center. Button Battery Ingestion Triage and Treatment Guideline. Current online guideline accessed 2026-09-04.","role":"current button-battery rescue: immediate esophageal removal, honey/sucralfate mitigation without delaying removal, post-removal injury assessment and delayed fistula/vascular surveillance"},
 {"type":"society_guideline","citation":"ASGE. Management of ingested foreign bodies and food impactions.","role":"general endoscopic timing: emergent removal for complete esophageal obstruction and esophageal disk battery; ENT consultation for objects at/above the cricopharyngeus; timely removal of esophageal coins and sharp objects"},
 {"type":"quality_guidance","citation":"ASGE Eosinophilic Esophagitis quality indicators and contemporary food-impaction guidance, reviewed 2023-2026.","role":"food impaction: when medically safe, obtain esophageal biopsies at index endoscopy to evaluate EoE rather than treating disimpaction as the endpoint"},
]

CONCEPT_ID="v6-general-ent-emergencies-esophageal-foreign-body"
TOPIC="Esophageal Foreign Body"
Q_REC="cc-v112-rec-general-ent-emergencies-esophageal-foreign-body"
Q_MGT="cc-v112-mgt-general-ent-emergencies-esophageal-foreign-body"

FOUNDATION_ANSWER="""Foundation — first decide whether this is an airway problem, an esophageal obstruction, or both. Drooling, inability to handle secretions, dysphagia, odynophagia, vomiting, food refusal and chest/neck pain point toward esophageal impaction; stridor, severe respiratory distress or inability to protect the airway changes the first priority to airway stabilization. The classic cervical narrowing is the cricopharyngeus/upper esophageal sphincter, with additional physiologic narrowings distally. Objects at or above the cricopharyngeus sit squarely in ENT territory because rigid endoscopic exposure and airway control may be needed.

Imaging — for a suspected radiopaque object obtain AP and lateral films that include the neck, chest and abdomen when object location is uncertain. Do not call a circular density a coin until a button battery has been excluded. A button battery may show a double-ring/halo sign on AP view and a step-off on lateral view. Orientation also helps distinguish airway from esophageal location: an esophageal coin commonly lies in the coronal plane, while airway foreign bodies more often align sagittally, but location must be confirmed rather than inferred from one sign. Avoid delaying definitive removal in a symptomatic child or a known high-risk object for elaborate imaging.

Object-specific urgency — complete esophageal obstruction with inability to manage secretions is emergent regardless of object type. An esophageal button battery is an immediate-removal emergency because severe alkali injury can develop rapidly. Sharp objects and multiple magnets carry perforation, fistula and pressure-necrosis risks and demand urgent specialist removal. A blunt coin in an asymptomatic child may sometimes be observed briefly for spontaneous passage depending on location and timing, but persistent esophageal coins should not simply remain for days.

Button battery nuance — if a child at least 12 months old swallowed a possible lithium coin cell within the prior 12 hours and can swallow, current Poison Center guidance supports honey during transport; after radiographic confirmation, sucralfate may also be used before endoscopy. Neither treatment substitutes for removal and neither should delay transport, anesthesia or endoscopy. After removal, inspect the injury and think beyond the mucosa: delayed tracheoesophageal fistula, recurrent laryngeal nerve injury, perforation, mediastinitis and catastrophic vascular fistula can occur after the battery is gone. Injury location relative to the aorta or other major vessels determines surveillance intensity.

Operative principles — secure an airway appropriate to the patient's physiology and object location, then expose the hypopharynx/cervical esophagus under direct vision. Choose rigid versus flexible endoscopy according to location, operator expertise, object shape and need for airway control; proximal/cervical objects are often well suited to rigid esophagoscopy by ENT. Use a retrieval instrument that controls the object rather than allowing it to tumble. Protect sharp points during withdrawal when possible. Stop if resistance suggests the object is embedded or the wall is being injured; forcing extraction can convert a contained impaction into a perforation.

Perforation concern — severe neck/chest pain, crepitus, fever, tachycardia, subcutaneous emphysema, pneumomediastinum or a difficult traumatic extraction should trigger evaluation for esophageal injury. Keep the patient NPO, involve surgery/ENT/GI early, use cross-sectional imaging with contrast strategy appropriate to the scenario, and treat contamination/source control rather than reflexively performing repeated instrumentation. The repository's separate esophageal-perforation rescue pathway remains the detailed postoperative bailout.

Food impaction is not the endpoint — after successful disimpaction, ask why the food stuck. In children and young adults, eosinophilic esophagitis is a major underlying diagnosis; structural narrowing and motility disease also matter. When medically safe, contemporary quality guidance supports obtaining adequate esophageal biopsies during the index endoscopy rather than discharging the patient with no etiologic workup.

Textbook-versus-current distinction — Cummings, Pasha and K.J. Lee provide the durable anatomy, radiographic localization, rigid endoscopy, object-control and perforation principles. The 2026 ESPGHAN position paper updates the decision frame around four variables—object type, location, symptoms and elapsed time—while current button-battery guidance is more aggressive and specific about mitigation, immediate removal and delayed vascular/TE-fistula surveillance than older textbook algorithms.

Senior synthesis — ask AIRWAY, OBJECT, LOCATION, SYMPTOMS, TIME, then REMOVE without creating a second injury. The dangerous misses are calling a battery a coin, sending a drooling child for nonessential imaging, pulling a sharp embedded object against resistance, forgetting delayed battery vascular injury, and treating food disimpaction as a complete diagnosis."""

MANAGEMENT_ANSWER="""Application — a child with an esophageal foreign body is managed by urgency, not by the fact that the x-ray looks tidy. First stabilize airway/breathing and determine whether secretions can be handled. Inability to swallow saliva, respiratory compromise, severe pain or toxicity means the patient is not an observation candidate. Keep NPO, call ENT/GI/anesthesia early, and identify the object and its exact level.

For a round radiopaque object, obtain AP and lateral imaging and actively distinguish a coin from a button battery. The double-rim/halo and lateral step-off favor a battery. If an esophageal battery is present, move directly toward emergent endoscopic removal. In a child at least 12 months old with ingestion within 12 hours who can swallow, honey can be given while coming to the hospital; after battery location is confirmed, sucralfate may be considered while the OR/endoscopy team mobilizes. These are injury-mitigation measures only and must never delay removal.

A complete obstruction is emergent even if the object is otherwise benign. Sharp objects and magnets deserve urgent removal because the complication is not just persistent dysphagia—it is perforation, fistula, bleeding or injury to adjacent structures. A stable asymptomatic coin may have a short observation window depending on location and time since ingestion, but persistent esophageal location requires timely removal rather than outpatient neglect.

Procedure choice — a proximal object at or above the cricopharyngeus is a classic ENT problem. Rigid esophagoscopy offers excellent cervical exposure, airway control and use of robust graspers; flexible endoscopy may be preferred for more distal objects depending on local expertise and object characteristics. The senior resident plans the extraction path before grasping: which end should lead, where is the sharp point, can the object rotate, and what structure will be injured if it slips? If the object is embedded or significant resistance is encountered, stop and re-visualize rather than using force.

After removal, inspect the mucosa and decide whether the case is over. A superficial pressure mark is different from deep circumferential battery necrosis, perforation or an extraction-related tear. Battery injuries may continue to evolve after removal. Deep injury near major vessels merits multidisciplinary surveillance and cross-sectional vascular imaging according to location and severity; sentinel hematemesis or other bleeding after battery injury is an emergency warning for vascular fistulization.

Food bolus cases require a second diagnosis. If the patient has recurrent solid-food dysphagia, atopy, rings/furrows or an otherwise unexplained impaction, think eosinophilic esophagitis. When safe, obtain adequate biopsies at the index endoscopy and arrange longitudinal treatment rather than simply documenting 'foreign body removed.'

Senior bailout — suspected perforation, rapidly worsening pain, crepitus, mediastinal air, fever/sepsis, uncontrolled bleeding or inability to retrieve the object safely should move the team from routine extraction to complication control. Stop traumatic attempts, keep NPO, start appropriate broad-spectrum therapy when perforation/contamination is suspected, obtain targeted imaging, and involve the surgeons needed for drainage, repair or vascular rescue. The operative goal is not 'get the object out at any cost'; it is remove the object while preserving an intact aerodigestive tract."""

COHORT={
 Q_REC:{"concept_id":CONCEPT_ID,"canonical_topic":TOPIC,"prompt":"A 3-year-old is brought to the ED after suddenly refusing food and drooling while playing with coins and a remote control. AP imaging shows a round upper-esophageal density, but the lateral film has not yet been reviewed. How should the otolaryngology resident distinguish coin from button battery, determine urgency, choose the removal strategy, and recognize the post-removal injuries that require continued surveillance?","answer_text":FOUNDATION_ANSWER,
 "explanation":"Esophageal foreign bodies are triaged by airway status, ability to handle secretions, object type, location and time since ingestion. Button batteries, complete obstruction, sharp objects and magnets are high-risk phenotypes; safe endoscopy requires planned object control and post-removal injury assessment.",
 "board_pearl":"Never label a round esophageal object a coin before excluding a button battery; complete obstruction and an esophageal battery are emergent, and battery injury can progress after removal.",
 "depth_layers_v207":{"foundation":"Cricopharyngeal/cervical esophageal anatomy, symptom pattern, AP/lateral localization, coin-versus-battery radiographic signs and object-specific injury mechanisms.","application":"Use airway status, secretion handling, object type, location and elapsed time to select observation versus urgent/emergent endoscopy and rigid versus flexible retrieval.","senior_decision":"Stop on unsafe resistance, recognize perforation and delayed button-battery vascular/TE-fistula injury, and investigate EoE/structural disease after food impaction."}},
 Q_MGT:{"concept_id":CONCEPT_ID,"canonical_topic":TOPIC,"prompt":"A child has a proximal esophageal foreign body with drooling but stable oxygenation, and the OR is being prepared. Walk through the management decisions from imaging and object-specific timing through rigid versus flexible endoscopy, safe extraction, perforation bailout, and what additional workup is needed if the event is a food bolus impaction?","answer_text":MANAGEMENT_ANSWER,
 "explanation":"The management task is to remove the object on the correct timeline without converting impaction into perforation, while identifying high-risk battery/sharp/magnet phenotypes and the underlying disease behind food impaction.",
 "board_pearl":"Urgency follows physiology and object risk: inability to handle secretions, button battery, sharp object or magnet beats a comfortable-looking x-ray; force against an embedded object is a perforation trap.",
 "depth_layers_v207":{"foundation":"Symptoms, location and object identity define risk.","application":"Select imaging, timing, airway plan, endoscope and retrieval method according to object and level.","senior_decision":"Escalate suspected perforation/vascular injury, avoid force, and complete etiologic evaluation after food impaction."}},
}

TRAPS=[
 "Calling every round radiopaque esophageal object a coin and missing the double-ring/step-off of a button battery.",
 "Sending a drooling child who cannot handle secretions for optional imaging before mobilizing definitive airway/endoscopic management.",
 "Assuming honey or sucralfate makes an esophageal battery less urgent; mitigation never substitutes for immediate removal.",
 "Forcing a sharp or embedded object through resistance instead of re-visualizing and changing the extraction plan.",
 "Treating removal of a button battery as the endpoint despite delayed tracheoesophageal, recurrent-laryngeal-nerve or vascular fistula risk.",
 "Using only object type and ignoring location, symptoms and elapsed time when deciding whether observation is safe.",
 "Ignoring perforation warning signs after a difficult esophagoscopy because the foreign body was technically retrieved.",
 "Discharging recurrent food-impaction patients without evaluating for eosinophilic esophagitis or structural narrowing."
]
for _p in COHORT.values():
 _p["common_traps_v207"]=list(TRAPS)
 _p["deliberate_review_v207"]="Selected from the exact successful v20.6 live-canonical backlog because both Esophageal Foreign Body Concept Checks were approximately 12 words despite high board and OR consequence. Priority was based on button-battery, complete-obstruction, sharp-object, perforation and operative-extraction risk rather than lexical rank alone."
 _p["source_refs_v207"]=SOURCE_REFS_V207

def apply_concept_check_task_alignment_v207(checks, deep_modules, v6_item_id):
 by={str(q.get('id') or ''):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
 for qid,p in COHORT.items():
  q=by.get(qid)
  if q is None: missing.append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if m is None or topic!=p['canonical_topic'] or cid!=p['concept_id'] or q.get('concept_id')!=cid: link_mismatch.append(qid); continue
  for field in ('prompt','answer_text','explanation','board_pearl','depth_layers_v207','common_traps_v207','deliberate_review_v207','source_refs_v207'): q[field]=p[field]
  q['task_alignment_v207']=True; repaired.append(qid)
 return {'repaired':repaired,'missing':missing,'link_mismatch':link_mismatch}
