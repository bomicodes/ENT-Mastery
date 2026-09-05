"""v20.11 — rehome the exact live Facial Plastics / Trauma Facial Soft-Tissue Lacerations / Burns Concept Check.

This preserves the prior hand-curated function-first facial-trauma teaching while moving it
onto the validated v20.10 PTA lineage. Durable operative principles are cross-checked against
Cummings 7e, Pasha 6e, and K.J. Lee 12e; burn disposition follows current ABA guidance.
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V211 = [
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed., facial trauma/facial plastics soft-tissue injury and facial nerve sections (connected ENT Boards Library).","role":"foundation/operative: systematic wound assessment, conservative facial debridement, layered repair, facial nerve/parotid duct evaluation, tissue loss and staged reconstruction"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed., facial trauma and burns sections (connected ENT Boards Library).","role":"foundation/management: initial trauma priorities, laceration repair principles, special-structure injury and burn assessment"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed., facial trauma/reconstruction sections (connected ENT Boards Library).","role":"operative: facial nerve, parotid duct, eyelid/lacrimal, lip, nasal/auricular cartilage and reconstructive principles"},
 {"type":"guideline","citation":"American Burn Association. Guidelines for Burn Patient Referral, current online guidance accessed 2026-09-04.","role":"current management: burn-center consultation/transfer for deep partial or full-thickness facial burns and suspected inhalation injury"},
 {"type":"review","citation":"Braun TL, Maricevich RS. Management of Traumatic Soft Tissue Injuries of the Face. Semin Plast Surg. 2021;35(4):229-237. PMCID: PMC8604620.","role":"operative review: pre-anesthetic facial nerve examination, irrigation/hemostasis, conservative debridement, layered closure, facial nerve exploration/repair, parotid duct assessment and repair"},
]

QID="cc-v112-rec-facial-plastics-trauma-facial-soft-tissue-lacerations-burns"
CID="v6-facial-plastics-trauma-facial-soft-tissue-lacerations-burns"
TOPIC="Facial Soft-Tissue Lacerations / Burns"
PROMPT="""A patient arrives after a complex cheek-and-lip laceration with possible parotid-region injury, while another patient has a deep facial thermal burn with soot around the mouth. Before focusing on cosmetic closure, how should you evaluate the facial wound for functional injuries, decide what requires immediate repair versus staged reconstruction, and distinguish a routine facial laceration from a burn that needs airway escalation or burn-center involvement?"""
ANSWER="""Foundation — treat facial soft-tissue trauma as a function-first problem before it is a scar problem. Complete trauma priorities and control hemorrhage, then identify injuries that cannot be safely hidden beneath a skin closure. Before injecting local anesthetic or creating additional neuropraxia, document facial nerve function with brow elevation, forceful eye closure, smile/oral commissure excursion and lower-lip depression. When the periorbital region is involved, document vision and globe findings and inspect the eyelid margin and medial canthus for canalicular injury. Assess nasal airway/septum, oral mucosa, teeth and occlusion when relevant, and auricular or nasal cartilage exposure. A cheek wound specifically demands assessment of the parotid gland/duct and facial nerve.

Wound preparation — obtain adequate anesthesia after the neurologic examination, achieve hemostasis, irrigate thoroughly, remove gross contamination and foreign bodies, and inspect the full depth. Facial tissue is highly vascular, so debridement should be conservative when viability is uncertain; marginal or avulsed tissue that may survive should not be discarded reflexively. Crush and avulsion wounds may declare viability over time. Preserve tissue, restore anatomic landmarks and avoid burying contamination or an unrecognized deep injury.

Layered closure — repair from deep to superficial so muscle and soft-tissue layers restore function and remove tension from skin. Reapproximate mucosa when violated, restore orbicularis or other muscle continuity, eliminate meaningful dead space, align dermis precisely and use a low-tension skin closure. Place the first key stitch at the landmark whose mismatch would be most visible or functionally consequential: align the vermilion-cutaneous junction before completing a lip repair, the helical rim before completing an auricular repair, and eyelid/nasal free margins with meticulous attention to notching or retraction. Do not close skin over an unrepaired facial nerve or parotid duct transection.

Facial nerve — recognize a sharp traumatic facial nerve transection early and repair a repairable major branch primarily when feasible. Early exploration is especially useful because the distal segment can still be electrically stimulated before Wallerian degeneration removes that aid after roughly 72 hours. If immediate neurorrhaphy is impossible, identify and tag nerve ends for planned reconstruction rather than losing them in scar. Distal midfacial branch injuries can have redundancy, so not every tiny distal branch mandates exploration; the decision depends on injury level and functional deficit. A major board and medicolegal error is failing to document function before anesthetic and then discovering weakness without a baseline.

Parotid duct/gland — suspect Stensen duct injury when a laceration crosses the parotid-masseter region along the line from the tragus toward the upper lip. The papilla lies opposite the maxillary second molar and can be cannulated to assess continuity; gland massage may demonstrate saliva within the wound. A clear repairable transection is generally repaired primarily over a stent. More proximal injuries or associated gland injuries require individualized management, but a missed injury can present as salivary fistula or sialocele. Buccal facial weakness in a cheek wound should heighten concern for concomitant duct injury because the structures travel in close proximity.

Special structures — medial eyelid/canthal lacerations require deliberate canalicular evaluation; full-thickness eyelid injuries require accurate tarsal and margin alignment. Exposed auricular cartilage needs viable soft-tissue/perichondrial coverage and contour restoration. Nasal wounds should restore lining, structural support and skin rather than accepting exposed cartilage or a distorted free margin. Through-and-through lip injuries require layered mucosa, muscle and skin repair. True tissue loss is not solved by pulling remaining tissue together under excessive tension; local flap, graft or staged reconstruction may be safer.

Contamination and antibiotics — irrigation and removal of devitalized contamination matter more than routine antibiotics for every simple facial laceration. Use antibiotics selectively for scenarios such as bites, gross contamination, oral cavity communication, open fractures or meaningful cartilage concerns, immunocompromise, or established infection. Update tetanus prophylaxis when indicated. Delayed presentation does not automatically mean every facial wound must remain open; judge contamination, infection, tissue viability and whether safe debridement and repair remain possible.

Burn distinction — facial burns require a different first decision: airway and burn depth before reconstruction. Stop the burning process, estimate burn extent/depth and actively look for inhalation injury. Facial flash burns, singed hairs, soot, hoarseness or voice change, stridor, respiratory distress, enclosed-space smoke exposure, or progressive edema should increase concern. A currently adequate airway can deteriorate as edema evolves, so early airway escalation in a high-risk patient is safer than waiting for a difficult late intubation. Do not intubate solely because the face is burned, but do not dismiss evolving airway signs because the initial oxygen saturation is normal.

Burn-center threshold — current American Burn Association referral guidance recommends immediate consultation with consideration for transfer for deep partial-thickness or full-thickness burns involving the face and for suspected inhalation injury; potentially deep burns also merit consultation. Facial burns matter disproportionately because eyelids, lips, nose and ears are functional/aesthetic units prone to contracture and airway injury may coexist. Definitive wound strategy depends on depth and evolution: superficial injuries may heal with local care, whereas deep burns may require excision/grafting and later contracture reconstruction.

Failure/rescue — after repair, worsening pain, erythema, purulence, fluctuance, salivary swelling with meals, new facial weakness, wound dehiscence, exposed cartilage or free-margin distortion should trigger reassessment rather than cosmetic reassurance. A sialocele suggests a missed gland/duct injury; new weakness raises nerve injury or compression concerns; ectropion, lip notching or nasal/auricular deformity may reflect poor landmark alignment or tension. After burns, progressive hoarseness, stridor, respiratory effort, hypoxemia, circumferential neck swelling or worsening edema requires urgent airway reassessment.

Senior synthesis — use five checks. FUNCTION asks which nerve, eye/lacrimal, salivary, cartilage, mucosal or airway structures are threatened. CLEAN asks whether contamination and nonviable tissue have been addressed without over-debriding viable face. ALIGN asks which landmark must be restored first and which layers remove tension. REPAIR asks which deep structure requires immediate microsurgical or ductal repair before skin closure. BURN asks whether depth, facial location or inhalation risk changes disposition and airway planning. Dangerous errors are documenting facial nerve function only after anesthetic, closing a cheek wound over an unrecognized nerve or duct injury, aggressively discarding marginally viable facial tissue, using tension to close a true tissue defect, and treating a deep facial burn as merely a skin wound while inhalation edema evolves."""

COHORT={QID:{
 "concept_id":CID,"canonical_topic":TOPIC,"prompt":PROMPT,"answer_text":ANSWER,
 "explanation":"Facial soft-tissue trauma is a functional-anatomy problem before it is a scar problem: examine nerve, eye/lacrimal, salivary, mucosal/cartilage and airway structures before anesthetic or closure; preserve viable tissue, restore landmarks with layered low-tension repair, repair deep injuries before skin, and treat deep facial burns or suspected inhalation injury as burn/airway problems.",
 "board_pearl":"Before local anesthetic, document facial nerve function. Before closing a cheek wound, exclude facial nerve and Stensen duct injury. Before treating a facial burn as a wound, decide whether inhalation injury or burn depth changes airway and disposition.",
 "depth_layers_v211":{"foundation":"Function-first facial examination, conservative debridement, irrigation and precise layered landmark repair.","application":"Recognize and manage facial nerve, parotid duct, eyelid/canalicular, lip, nasal and auricular injuries before superficial closure.","senior_decision":"Choose primary versus staged reconstruction, selectively use antibiotics, and escalate deep facial burns/suspected inhalation injury according to airway risk and burn-center referral criteria."},
 "common_traps_v211":[
  "Injecting local anesthetic before documenting facial nerve function.",
  "Closing a cheek laceration without checking Stensen duct and adjacent facial nerve branches.",
  "Aggressively debriding marginal facial tissue that may survive.",
  "Using skin sutures to pull a deep wound together instead of restoring muscle and dermis.",
  "Missing the vermilion border, eyelid margin, helical rim or nasal free margin and expecting the scar to correct it.",
  "Closing skin over a known nerve or duct transection before repair or deliberate staging.",
  "Giving antibiotics to every clean laceration while underemphasizing irrigation and selective prophylaxis.",
  "Assuming every facial burn requires prophylactic intubation rather than using inhalation-risk features and evolving edema.",
  "Waiting for overt airway obstruction despite soot, hoarseness, enclosed-space exposure or progressive edema.",
  "Treating deep partial/full-thickness facial burns as routine outpatient wounds rather than obtaining burn-center consultation."
 ],
 "deliberate_review_v211":"Rehomed from the previously curated facial-trauma cohort after v20.10 became the validated Peritonsillar Abscess cohort. The original 28-word reveal omitted pre-anesthetic nerve examination, parotid duct injury, landmark/layered repair, special-structure injuries, selective antibiotics, inhalation-airway reasoning and current facial-burn referral thresholds.",
 "source_refs_v211":SOURCE_REFS_V211,
}}

def apply_concept_check_task_alignment_v211(checks, deep_modules, v6_item_id):
 by={str(q.get('id') or ''):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
 for qid,p in COHORT.items():
  q=by.get(qid)
  if q is None: missing.append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if m is None or topic!=p['canonical_topic'] or cid!=p['concept_id'] or q.get('concept_id')!=cid: link_mismatch.append(qid); continue
  for field in ('prompt','answer_text','explanation','board_pearl','depth_layers_v211','common_traps_v211','deliberate_review_v211','source_refs_v211'): q[field]=p[field]
  q['choices']=[]; q['answer']=None; q['task_alignment_v211']=True; repaired.append(qid)
 return {'repaired':repaired,'missing':missing,'link_mismatch':link_mismatch}
