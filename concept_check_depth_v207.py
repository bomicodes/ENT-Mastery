"""v20.7 — deepen the exact live General ENT / Emergencies Esophageal Foreign Body Concept Checks.

Durable pediatric aerodigestive anatomy, radiographic localization, extraction mechanics and
perforation principles are cross-checked against Cummings 7e, Pasha 6e and K.J. Lee 12e in the
connected Drive corpus. Management is updated against the 2026 ESPGHAN pediatric foreign-body
position paper, current National Capital Poison Center button-battery guidance, and contemporary
food-impaction/EoE quality guidance.
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V207 = [
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed., Chapter 211 Pediatric Aerodigestive Foreign Bodies and related esophagoscopy sections (connected Drive 7e corpus re-verified 2026-09-04).","role":"foundation/operative: esophageal narrowing sites, symptoms, biplanar radiography, object-specific extraction mechanics, perforation risk and post-removal assessment"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed., pediatric laryngoesophagology/esophageal foreign-body sections (connected Drive copy re-verified 2026-09-04).","role":"foundation/operative: proximal esophageal foreign-body evaluation, rigid esophagoscopy, airway protection, instrumentation and complications"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed., pediatric otolaryngology and esophagus sections (connected Drive copy re-verified 2026-09-04).","role":"foundation/operative: cervical esophageal anatomy, presentation, radiographic localization, endoscopic retrieval and perforation complications"},
 {"type":"society","citation":"Ledder O, et al. Foreign body ingestions in children and adolescents: A position paper of the ESPGHAN endoscopy special interest group. J Pediatr Gastroenterol Nutr. 2026. PMID 42383497.","role":"current management: urgency based on object type, anatomic location, symptoms and elapsed time; emergent removal for symptomatic esophageal foreign bodies and sharp esophageal objects; airway protection during extraction"},
 {"type":"guideline","citation":"National Capital Poison Center. Button Battery Ingestion Triage and Treatment Guideline, current resource accessed 2026-09-04.","role":"current battery management: halo/step-off recognition, immediate esophageal battery removal, age/time-limited honey mitigation without delay, post-removal injury assessment and delayed vascular/TE-fistula surveillance"},
 {"type":"society","citation":"American Society for Gastrointestinal Endoscopy. Contemporary food-impaction quality guidance and 2025 Journal Scan on index-endoscopy biopsy for eosinophilic esophagitis, accessed 2026-09-04.","role":"current food-impaction boundary: disimpaction is not the endpoint; evaluate structural disease and obtain esophageal biopsies for EoE when medically safe"},
]

CID="v6-general-ent-emergencies-esophageal-foreign-body"
QID_REC="cc-v112-rec-general-ent-emergencies-esophageal-foreign-body"
QID_MGT="cc-v112-mgt-general-ent-emergencies-esophageal-foreign-body"

COMMON_TRAPS_V207 = [
 "Calling every round radiopaque esophageal object a coin. A button battery can mimic a coin; deliberately inspect the AP view for a double rim or halo and the lateral view for a step-off because delay can convert a simple retrieval into a caustic esophageal and vascular injury.",
 "Letting a child with drooling and inability to handle secretions wait because the object appears blunt. Complete or near-complete esophageal obstruction is an emergent airway/aspiration problem even when the object itself is not intrinsically caustic.",
 "Giving contrast to prove an obvious esophageal foreign body before removal. Contrast can delay definitive treatment, obscure the operative field and increase aspiration risk; use plain biplanar imaging first and reserve CT for selected radiolucent, delayed, perforation or vascular-risk scenarios.",
 "Treating honey as definitive button-battery therapy. Honey is only a mitigation bridge in an eligible child at least 12 months old within 12 hours who can swallow; it must never delay transport, imaging or immediate removal of an esophageal battery.",
 "Pushing a sharp object distally because retrieval looks difficult. A sharp esophageal object should be removed under controlled visualization with airway protection; blind advancement can convert mucosal penetration into perforation or vascular injury.",
 "Forcing a rigid scope or retrieval instrument when resistance is unexpected. Stop, re-establish orientation and reassess the object and wall; force against the cricopharyngeus or a fixed object can cause a cervical esophageal perforation and mediastinal contamination.",
 "Assuming a successful extraction ends a button-battery case. Tissue injury can progress after removal, with delayed perforation, recurrent-laryngeal-nerve injury, tracheoesophageal fistula or esophageal-vascular fistula; post-removal injury location and depth determine surveillance and multidisciplinary escalation.",
 "Removing an acute food bolus and omitting etiologic workup. Eosinophilic esophagitis and structural narrowing are common substrates; when safe, obtain appropriate biopsies at the index endoscopy and arrange follow-up rather than labeling the event idiopathic.",
]

BASE_ANSWER = """Foundation — first decide whether this is an airway problem, an esophageal obstruction problem, or both. A child with stridor, respiratory distress, aspiration, cyanosis, or inability to handle secretions needs immediate airway-focused stabilization while the retrieval team mobilizes. Esophageal foreign bodies commonly lodge at physiologic narrowings, especially the upper esophagus near the cricopharyngeus, but can also impact at the aortic-arch/left-mainstem level or distally. Symptoms such as drooling, dysphagia, odynophagia, gagging, food refusal, chest discomfort or vomiting may be prominent; a normal exam does not exclude an impacted object.

Localize before you instrument — when the object is radiopaque or its identity is uncertain, obtain biplanar imaging that includes the neck and chest and usually the abdomen. AP and lateral views help distinguish esophageal from airway location and identify object shape. For a presumed coin, actively look for the button-battery double-rim or halo sign on AP and a step-off on lateral. Do not let the label 'coin ingestion' substitute for looking at the film. Radiolucent objects may need endoscopy based on history and symptoms; CT is selectively useful for delayed presentation, suspected perforation, sharp objects, or concern for vascular involvement rather than as a routine delay before obvious urgent extraction.

Urgency is object + location + symptoms + time. The 2026 ESPGHAN framework makes those four variables explicit. Symptomatic esophageal foreign bodies and any esophageal object causing complete obstruction require emergent intervention. Sharp esophageal objects require emergent controlled removal. Multiple high-powered magnets, or a magnet plus another ferromagnetic object, can trap bowel or esophageal tissue and deserve aggressive specialty management. A simple asymptomatic blunt object such as a coin may occasionally be managed less urgently if the child is stable, but an esophageal object should not be allowed to sit indefinitely; the resident should distinguish a short observation window for a low-risk blunt object from dangerous delay in a high-risk object.

Button batteries are their own emergency phenotype. An esophageal battery can cause severe alkaline injury within hours. If a child is at least 12 months old, the suspected ingestion occurred within the preceding 12 hours, and the child can swallow, current Poison Center guidance supports honey while traveling for definitive care. Honey slows tissue injury; it does not neutralize the emergency and must not delay radiography, transfer, anesthesia or endoscopic removal. Once an esophageal battery is identified, remove it immediately. Document orientation when possible, inspect the mucosa after removal and assess for perforation and depth/location of injury. Proximal injury can threaten the recurrent laryngeal nerves and airway; mid-esophageal injury may be close to major vessels.

Operative planning — choose the extraction route according to level, object, patient size, local expertise and airway needs. Proximal/cervical esophageal objects near the cricopharyngeus commonly fall within the ENT rigid-esophagoscopy skill set. Flexible endoscopy may be appropriate for more distal objects in experienced hands. In children and in high-risk removals, airway protection with an endotracheal tube is usually appropriate because an object can be lost into the pharynx or airway during extraction. Select a retrieval tool that controls the object rather than merely touching it: optical forceps, graspers, baskets, snares or protected techniques depending on geometry. Keep sharp points oriented or shielded to minimize mucosal injury on withdrawal.

Stop-on-resistance — the senior resident must know when not to push. Unexpected resistance during scope advancement or extraction should trigger a stop, reorientation and reassessment rather than more force. The cervical esophagus is vulnerable to perforation, especially around a fixed object or difficult cricopharyngeal exposure. If perforation is suspected because of free air, neck/chest crepitus, severe pain, fever, tachycardia, mucosal disruption or a difficult traumatic extraction, stop further blind manipulation, keep the patient NPO, give broad-spectrum antibiotics when contamination is suspected, obtain appropriate contrast imaging/CT based on stability, and involve thoracic/pediatric surgery early. The exact repair versus drainage versus nonoperative strategy depends on location, size, contamination, timing and clinical stability.

Post-battery rescue is not routine post-esophagoscopy care. Delayed injury can evolve after a battery is gone. Significant mucosal injury warrants admission and tailored surveillance; injury near the aorta or other major vessels may require cross-sectional vascular assessment and early cardiothoracic input. Sentinel bleeding, new chest pain, hematemesis, respiratory deterioration or neurologic change after prior battery extraction must trigger concern for catastrophic esophageal-vascular fistula rather than reassurance from the prior successful procedure. Delayed TE fistula, perforation, RLN paresis and stricture also remain possible.

Food impaction is a diagnostic clue. After safe bolus extraction, inspect for rings, narrowing, mucosal changes or another structural lesion. Contemporary EoE practice differs from the older 'remove the bolus and arrange clinic follow-up' habit: when the mucosa and patient condition permit, obtain adequate esophageal biopsies during the index endoscopy because eosinophilic esophagitis is a leading cause of food impaction and diagnosis is otherwise frequently delayed.

Textbook-versus-current distinction — Cummings, Pasha and K.J. Lee remain the durable foundation for narrowing anatomy, radiographic localization, rigid-esophagoscopy technique, controlled extraction and perforation avoidance. Current guidance sharpens object-specific urgency: button batteries, sharp objects, high-risk magnets and symptomatic esophageal impaction move immediately to the front of the queue; honey is only a time-limited bridge for eligible battery ingestions; and food-impaction care increasingly includes index-endoscopy evaluation for EoE rather than ending at disimpaction.

Senior synthesis — think AIRWAY, IDENTIFY, LOCALIZE, RISK-CLASSIFY, CONTROL, STOP, INSPECT, FOLLOW. Protect the AIRWAY; IDENTIFY the object instead of assuming 'coin'; LOCALIZE it with appropriate imaging; RISK-CLASSIFY by type, site, symptoms and time; CONTROL it with the correct endoscopic route and tool; STOP rather than forcing unexpected resistance; INSPECT for mucosal injury/perforation after extraction; and FOLLOW high-risk battery or food-impaction patients for delayed complications and underlying disease."""

COHORT={
 QID_REC:{
  "concept_id":CID,"canonical_topic":"Esophageal Foreign Body",
  "prompt":"A 3-year-old presents after a witnessed ingestion of a round metallic object. She is drooling and refusing liquids but has no stridor. AP and lateral radiographs show a circular object at the thoracic inlet, and the ED calls it a coin. As the ENT resident, explain how you distinguish a coin from a button battery, how symptoms and object type change urgency, what imaging or mitigation should and should not delay removal, and how you plan a safe extraction and post-removal evaluation?",
  "answer_text":BASE_ANSWER,
  "explanation":"Esophageal foreign-body management is driven by airway status, object identity, location, symptoms and elapsed time. The high-stakes resident move is to recognize batteries, sharp objects, magnets and complete obstruction early, extract under controlled visualization with airway protection, stop when resistance suggests unsafe mechanics, and continue surveillance when injury can progress after removal.",
  "board_pearl":"Never accept 'coin' until you have looked for a battery halo/step-off. Esophageal button batteries, sharp objects and symptomatic obstruction are time-critical; honey may mitigate battery injury in eligible children but never delays removal.",
 },
 QID_MGT:{
  "concept_id":CID,"canonical_topic":"Esophageal Foreign Body",
  "prompt":"During urgent endoscopy for a child with an impacted esophageal foreign body, the object is difficult to control and the scope meets unexpected resistance near the cricopharyngeus. Walk through the senior resident's operative decision-making: airway protection, rigid versus flexible route selection, object-specific retrieval strategy, the stop-on-resistance rule, what findings should trigger a perforation bailout, and how button-battery injury or a food impaction changes post-procedure management?",
  "answer_text":BASE_ANSWER,
  "explanation":"The safest extraction is not the fastest instrument movement; it is the controlled plan that protects the airway, matches the route and retrieval tool to the object and level, stops before force creates a perforation, and treats post-extraction battery injury or food-impaction etiology as part of the same emergency.",
  "board_pearl":"Unexpected resistance during esophagoscopy is a stop signal. Reorient rather than force, and if perforation is suspected switch from retrieval momentum to contamination control, imaging and surgical backup.",
 }
}

for _qid,_p in COHORT.items():
 _p["depth_layers_v207"]={
  "foundation":"Know physiologic esophageal narrowing sites, symptoms of obstruction, AP/lateral localization, coin-versus-button-battery signs and object-specific injury mechanisms.",
  "application":"Triage airway/secretions, classify urgency by type-location-symptoms-time, choose rigid versus flexible retrieval with airway protection, and use controlled object-specific extraction rather than blind advancement.",
  "senior_decision":"Stop on unexpected resistance, recognize and bail out for perforation, plan delayed button-battery vascular/TE-fistula surveillance, and investigate food impaction for EoE or structural disease."
 }
 _p["common_traps_v207"]=COMMON_TRAPS_V207
 _p["deliberate_review_v207"]="Selected from the exact successful v20.6 live-canonical backlog because two Esophageal Foreign Body checks remained extremely shallow despite high resident/board/OR value. The concept was prioritized over lexical rank because missed battery recognition, complete obstruction, sharp-object mechanics, forced instrumentation or delayed post-battery injury can cause immediate morbidity or death."
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
