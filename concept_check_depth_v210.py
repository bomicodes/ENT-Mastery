"""v20.10 — deepen the exact live Facial Plastics / Trauma Facial Soft-Tissue Lacerations / Burns Concept Check.

Durable facial soft-tissue trauma principles are cross-checked against the connected ENT
Boards Library copies of Cummings 7e, Pasha 6e, and K.J. Lee 12e. Burn disposition is
updated against the current American Burn Association referral guidance.
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V210 = [
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed., facial trauma/facial plastics soft-tissue injury and facial nerve sections (connected ENT Boards Library).","role":"foundation/operative: systematic facial wound assessment, conservative facial debridement, layered repair, facial nerve/parotid duct evaluation, tissue loss and staged reconstruction"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed., facial trauma and burns sections (connected ENT Boards Library).","role":"foundation/management: initial trauma priorities, facial laceration repair principles, special-structure injury and burn assessment"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed., facial trauma/reconstruction sections (connected ENT Boards Library).","role":"operative: facial nerve, parotid duct, eyelid/lacrimal, lip, nasal/auricular cartilage and reconstructive principles"},
 {"type":"guideline","citation":"American Burn Association. Guidelines for Burn Patient Referral, current online guidance accessed 2026-09-04.","role":"current management: burn-center consultation/transfer for deep partial or full-thickness facial burns and suspected inhalation injury, plus consultation for potentially deep burns"},
 {"type":"review","citation":"Braun TL, Maricevich RS. Management of Traumatic Soft Tissue Injuries of the Face. Semin Plast Surg. 2021;35(4):229-237. PMCID: PMC8604620.","role":"operative review: pre-anesthetic facial nerve examination, irrigation/hemostasis, conservative debridement, layered closure, facial nerve exploration/repair, parotid duct assessment and repair"},
]

QID="cc-v112-rec-facial-plastics-trauma-facial-soft-tissue-lacerations-burns"
CID="v6-facial-plastics-trauma-facial-soft-tissue-lacerations-burns"
TOPIC="Facial Soft-Tissue Lacerations / Burns"

PROMPT="""A patient arrives after a complex cheek-and-lip laceration with possible parotid-region injury, while another patient has a deep facial thermal burn with soot around the mouth. Before focusing on cosmetic closure, how should you evaluate the facial wound for functional injuries, decide what requires immediate repair versus staged reconstruction, and distinguish a routine facial laceration from a burn that needs airway escalation or burn-center involvement?"""

ANSWER="""Foundation — treat facial soft-tissue trauma as a function-first problem before it is a scar problem. Complete the trauma priorities, control hemorrhage, and identify injuries that cannot be safely hidden under a skin closure. Before injecting local anesthetic or creating additional neuropraxia, document facial nerve function by testing brow elevation, forceful eye closure, smile/oral commissure excursion and lower-lip depression. Examine vision and the globe when the periorbital region is involved; inspect eyelid margin and medial canthus for canalicular injury; assess nasal airway/septum, oral mucosa, teeth/occlusion when relevant, and auricular or nasal cartilage exposure. In a cheek wound, specifically look for parotid gland/duct and facial nerve injury rather than simply closing the skin.

Wound preparation — obtain adequate anesthesia after the neurologic examination, achieve hemostasis, irrigate thoroughly, remove gross contamination and foreign bodies, and inspect the full depth of the wound. Facial tissue is highly vascular, so debridement should be conservative when viability is uncertain; marginal or avulsed tissue that may survive should not be discarded reflexively. Crush and avulsion wounds may declare viability over time. The objective is to preserve tissue, restore anatomic landmarks and avoid burying contamination or an unrecognized deep injury.

Layered closure — repair from deep to superficial so muscle and soft-tissue layers restore function and take tension off the skin. Reapproximate mucosa when violated, restore orbicularis or other muscle continuity, eliminate meaningful dead space, align dermis precisely and use a low-tension skin closure. The first key stitch belongs at the landmark whose mismatch would be most visible or functionally consequential: for example, align the vermilion-cutaneous junction before completing a lip repair, the helical rim before closing an auricular laceration, and eyelid/nasal free margins with meticulous attention to notching or retraction. Do not close skin over an unrepaired facial nerve or parotid duct transection.

Facial nerve — a sharp traumatic facial nerve transection in a repairable branch should be recognized early and repaired primarily when feasible. Early exploration is valuable because the distal segment can still be stimulated before Wallerian degeneration eliminates that aid after roughly 72 hours. If immediate neurorrhaphy is impossible, identify and tag nerve ends for planned reconstruction rather than losing them in scar. Distal midfacial branch injuries may have redundancy, so not every tiny distal branch mandates exploration; the decision depends on the level of injury and observed functional deficit. The board error is failing to document function before anesthetic and then discovering postoperative weakness with no baseline.

Parotid duct/gland — suspect Stensen duct injury when a laceration crosses the parotid-masseter region along the course from the tragus toward the upper lip. The papilla lies opposite the maxillary second molar and can be cannulated to help assess duct continuity; massage of the gland may show saliva in the wound. A clear transection that can be repaired is generally repaired primarily over a stent. More proximal injuries or associated gland injuries require individualized management, but the resident should anticipate salivary fistula or sialocele if the injury is missed. A cheek wound with buccal facial weakness should heighten concern for a concomitant duct injury because the structures travel in close proximity.

Special structures — medial eyelid/canthal lacerations require deliberate evaluation of the canalicular system; full-thickness eyelid injuries require accurate tarsal and margin alignment. Exposed auricular cartilage needs viable soft-tissue/perichondrial coverage and careful contour restoration. Nasal wounds should restore lining, structural support and skin rather than accepting exposed cartilage or a distorted free margin. Through-and-through lip injuries require layered mucosa, muscle and skin repair. Tissue loss is not solved by pulling remaining tissue together under excessive tension; local flap, graft or staged reconstruction may be safer for a true defect.

Contamination and antibiotics — irrigation and removal of devitalized contamination are more important than routine antibiotics for every simple facial laceration. Antibiotic decisions should be selective: bites, gross contamination, oral cavity communication, open fractures/cartilage concerns, immunocompromise or established infection may justify prophylaxis or treatment depending on the scenario. Update tetanus prophylaxis as indicated. A delayed presentation is not automatically an instruction to leave every facial wound open; judge contamination, infection, tissue viability and whether safe debridement/repair can still be achieved.

Burn distinction — facial burns require a different first decision: airway and burn depth before reconstruction. Stop the burning process, assess total burn extent/depth and look specifically for inhalation injury. Facial flash burns, singed hairs, soot, voice change, stridor, respiratory distress, enclosed-space smoke exposure or progressive edema should raise concern for inhalation injury. A currently adequate airway can deteriorate as edema evolves, so escalating airway assessment early is safer than waiting for impossible late intubation in a high-risk patient. Do not intubate solely because the face is burned, but do not dismiss evolving airway signs because oxygen saturation is initially normal.

Burn-center threshold — current American Burn Association referral guidance recommends immediate consultation with consideration for transfer for deep partial-thickness or full-thickness burns involving the face and for suspected inhalation injury; potentially deep burns also warrant consultation. Facial burns matter disproportionately because eyelids, lips, nose and ears are functional/aesthetic units prone to contracture and because airway injury may coexist. Definitive wound strategy then depends on burn depth and evolution: superficial injuries may heal with local wound care, whereas deep burns may require excision/grafting and later contracture reconstruction.

Failure/rescue — after laceration repair, worsening pain, erythema, purulence, fluctuance, salivary swelling with meals, new facial weakness, wound dehiscence, exposed cartilage or free-margin distortion should trigger reassessment rather than cosmetic reassurance. A salivary collection suggests missed gland/duct injury; new weakness raises nerve injury/compression concerns; ectropion, lip notching or nasal/auricular deformity may reflect poor landmark alignment or tension. After burns, progressive hoarseness, stridor, respiratory effort, hypoxemia, circumferential neck swelling or worsening edema requires urgent airway reassessment.

Senior synthesis — use five checks: FUNCTION asks which nerve, eye/lacrimal, salivary, cartilage, mucosal or airway structures are threatened; CLEAN asks whether contamination and nonviable tissue have been addressed without over-debriding viable face; ALIGN asks which landmark must be restored first and which layers remove tension; REPAIR asks which deep structure requires immediate microsurgical or ductal repair before skin closure; BURN asks whether depth, facial location or inhalation risk changes disposition and airway planning. The dangerous errors are documenting facial nerve function only after anesthetic, closing a cheek wound over an unrecognized nerve/duct injury, aggressively discarding marginally viable facial tissue, using tension to close a true tissue defect, and treating a deep facial burn as merely a skin wound while inhalation edema evolves."""

COHORT={QID:{
 "concept_id":CID,
 "canonical_topic":TOPIC,
 "prompt":PROMPT,
 "answer_text":ANSWER,
 "explanation":"Facial soft-tissue trauma is a structured functional-anatomy problem. Examine nerve, eye/lacrimal, salivary, mucosal/cartilage and airway structures before anesthetic or closure; preserve viable tissue, restore landmarks with layered low-tension repair, repair deep injuries before skin, and treat deep facial burns or suspected inhalation injury as burn/airway problems rather than cosmetic wounds.",
 "board_pearl":"Before local anesthetic, document facial nerve function. Before closing a cheek wound, exclude facial nerve and Stensen duct injury. Before treating a facial burn as a wound, decide whether inhalation injury or burn depth changes the airway and disposition.",
 "depth_layers_v210":{"foundation":"Function-first facial examination, conservative debridement, irrigation and precise layered landmark repair.","application":"Recognize and manage facial nerve, parotid duct, eyelid/canalicular, lip, nasal and auricular injuries before superficial closure.","senior_decision":"Choose primary versus staged reconstruction, selectively use antibiotics, and escalate deep facial burns/suspected inhalation injury according to airway risk and burn-center referral criteria."},
 "common_traps_v210":[
  "Injecting local anesthetic before documenting facial nerve function and then being unable to determine whether postoperative weakness was traumatic or iatrogenic.",
  "Closing a cheek laceration without checking the course of Stensen duct and the adjacent buccal/zygomatic facial nerve branches.",
  "Aggressively debriding marginal facial tissue that could survive because the face's vascularity often supports conservative tissue preservation.",
  "Using skin sutures to pull a deep wound together instead of restoring muscle/dermal layers and eliminating tension/dead space.",
  "Missing the vermilion border, eyelid margin, helical rim or nasal free margin by a few millimeters and assuming the final scar will correct the distortion.",
  "Closing skin over a known nerve or duct transection before the deeper injury is repaired or deliberately staged.",
  "Giving antibiotics to every clean facial laceration while underemphasizing irrigation, foreign-body removal and selective prophylaxis for bites, oral communication or heavy contamination.",
  "Assuming every facial burn requires prophylactic intubation; airway intervention should be driven by inhalation-risk features and evolving edema rather than facial location alone.",
  "Making the opposite burn error: waiting for overt airway obstruction despite soot, hoarseness, enclosed-space exposure or progressive edema suggesting an airway that may become difficult to secure.",
  "Treating deep partial/full-thickness facial burns as routine outpatient wounds instead of obtaining burn-center consultation and planning for functional-unit contracture risk."
 ],
 "deliberate_review_v210":"Selected as the highest-ranked residual live Concept Check after v20.9. The prior 28-word reveal mentioned early repair and burns but omitted pre-anesthetic nerve examination, parotid duct injury, landmark/layered repair, special-structure injuries, selective antibiotics, inhalation-airway reasoning and current facial-burn referral thresholds.",
 "source_refs_v210":SOURCE_REFS_V210,
}}


def apply_concept_check_task_alignment_v210(checks, deep_modules, v6_item_id):
 by={str(q.get('id') or ''):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
 for qid,p in COHORT.items():
  q=by.get(qid)
  if q is None: missing.append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if m is None or topic!=p['canonical_topic'] or cid!=p['concept_id'] or q.get('concept_id')!=cid: link_mismatch.append(qid); continue
  for field in ('prompt','answer_text','explanation','board_pearl','depth_layers_v210','common_traps_v210','deliberate_review_v210','source_refs_v210'): q[field]=p[field]
  q['choices']=[]; q['answer']=None; q['task_alignment_v210']=True; repaired.append(qid)
 return {'repaired':repaired,'missing':missing,'link_mismatch':link_mismatch}
