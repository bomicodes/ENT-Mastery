"""v20.11 — deepen the exact live Facial Plastics / Trauma Facial Soft-Tissue Lacerations / Burns Concept Check.

This cohort rehomes preserved clinical work from the stale pre-PTA v20.10 branch onto the
validated v20.10 production lineage. Durable anatomy/operative principles are cross-checked
against connected Cummings 7e, Pasha 6e, and K.J. Lee 12e. Burn disposition is updated
against current American Burn Association referral guidance.
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V211 = [
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), Ch. 19, Facial Trauma: Soft Tissue Lacerations and Burns, pp. 269-285 (connected Drive split Part 1).","role":"foundation/operative: early functional examination, conservative tissue handling, eyelid/canalicular injury, facial nerve and parotid injury, layered landmark repair, facial burns"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), Ch. 10 Head and Neck Trauma, Soft Tissue Trauma and Burns of the Head and Neck, pp. 672-676 (connected Drive copy).","role":"foundation/management: local anesthesia caveats, wound management, special soft-tissue injuries, burn assessment"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), Part 7 Facial Plastic and Reconstructive Surgery, Chs. 54-58, especially craniomaxillofacial trauma and eyelid/lacrimal/auricular repair principles (connected Drive copy).","role":"operative cross-check: anatomic-unit repair, canalicular injury, auricular cartilage/perichondrium, facial trauma reconstruction"},
 {"type":"guideline","citation":"American Burn Association. Burn Patient Referral Guidelines, current online guidance verified 2026-09-04.","role":"current management: immediate consultation/consideration for transfer for deep partial/full-thickness facial burns and suspected inhalation injury; consultation for potentially deep burns"},
 {"type":"review","citation":"Braun TL, Maricevich RS. Management of Traumatic Soft Tissue Injuries of the Face. Semin Plast Surg. 2021;35(4):229-237. PMCID: PMC8604620.","role":"operative review: pre-anesthetic facial nerve examination, irrigation/hemostasis, conservative debridement, layered closure, facial nerve exploration/repair and parotid duct assessment"},
]

QID="cc-v112-rec-facial-plastics-trauma-facial-soft-tissue-lacerations-burns"
CID="v6-facial-plastics-trauma-facial-soft-tissue-lacerations-burns"
TOPIC="Facial Soft-Tissue Lacerations / Burns"

PROMPT="""A patient arrives after a complex cheek-and-lip laceration with possible parotid-region injury, while another patient has a deep facial thermal burn with soot around the mouth. Before focusing on cosmetic closure, how should you evaluate the wound for functional injuries, decide what requires immediate repair versus staged reconstruction, and distinguish a routine facial laceration from a burn that needs airway escalation or burn-center involvement?"""

ANSWER="""Foundation — treat facial soft-tissue trauma as a function-first problem before it is a scar problem. Complete trauma priorities and control hemorrhage, but do not let an apparently cosmetic wound hide an eye, lacrimal, facial nerve, parotid duct, mucosal, cartilage, dental/occlusal, or airway injury. Cummings specifically emphasizes documenting facial nerve function early and before wound exploration, anesthetic application, or repair because those interventions can obscure the original deficit. Test brow elevation, forceful eye closure, smile/oral commissure excursion, and lower-lip depression. Examine the globe and vision when the orbit is involved; inspect eyelid margins and the medial canthus for canalicular injury; examine nasal support/airway, oral mucosa, teeth and occlusion when relevant; and identify exposed auricular or nasal cartilage.

Wound preparation — after the neurologic and functional examination, obtain adequate anesthesia, achieve hemostasis, irrigate thoroughly, remove foreign material, and inspect the wound through its full depth. The face is highly vascular, so debridement should be conservative when viability is uncertain. Do not reflexively discard marginal or partially avulsed tissue that may survive. Crush and avulsion injuries may declare viability over time. The goal is to preserve tissue while avoiding closure over contamination, dead tissue, or an unrecognized deep injury.

Layered repair — rebuild anatomy from deep to superficial. Reapproximate mucosa when violated, restore muscle continuity, eliminate meaningful dead space, restore dermis, and use low-tension skin closure. The first key stitch belongs at the landmark whose mismatch would be most visible or functionally consequential: align the vermilion-cutaneous junction before completing a lip repair, precisely restore eyelid/free margins, and restore the helical rim or nasal margin without notching. Tissue loss is not solved by pulling the remaining face together under excessive tension; graft, local flap, regional flap, or staged reconstruction may be safer when a true defect exists.

Facial nerve — a sharp traumatic transection in a repairable facial nerve branch should be recognized early and repaired primarily when feasible. Early exploration is valuable because distal stimulation becomes unreliable after Wallerian degeneration. If immediate neurorrhaphy cannot be performed, identify/tag nerve ends and make the reconstruction plan rather than allowing them to disappear into scar. Distal midfacial branches have variable redundancy, so management depends on branch level and observed deficit rather than an automatic rule that every tiny distal branch requires exploration. The board and OR trap is documenting facial movement only after local anesthetic or wound manipulation and then being unable to distinguish traumatic from iatrogenic weakness.

Parotid duct/gland — suspect Stensen duct injury when a laceration crosses the parotid-masseter region. The duct papilla is opposite the maxillary second molar and can be cannulated to assess continuity; gland massage may reveal saliva in the wound. A clear repairable transection is generally repaired primarily over a stent. Buccal facial nerve weakness plus a cheek wound should increase suspicion because the nerve branches and duct travel close together. Missed injuries can present with salivary fistula or sialocele and require reassessment rather than repeated superficial drainage alone.

Special structures — medial eyelid/canthal lacerations require deliberate canalicular evaluation; full-thickness eyelid injury requires exact tarsal and margin alignment. Exposed auricular cartilage needs viable soft-tissue/perichondrial coverage and contour restoration. Nasal wounds should restore lining, support, and skin rather than accepting exposed cartilage or free-margin distortion. Through-and-through lip wounds require layered mucosa, orbicularis, and skin repair. These injuries deserve specialist escalation when the required structure cannot be confidently identified or repaired.

Contamination and antibiotics — irrigation, foreign-body removal, and appropriate debridement are more important than reflex antibiotics for every clean facial laceration. Antibiotic decisions should be selective and individualized for bites, gross contamination, oral cavity communication, open fracture/cartilage concerns, immunocompromise, or established infection. Update tetanus prophylaxis when indicated. A delayed presentation is not automatically a reason to leave every facial wound open; judge contamination, infection, tissue viability, and whether safe repair can still be achieved.

Burn distinction — facial burns require a different first decision: airway and burn depth before reconstruction. Stop the burning process, assess burn extent/depth, and look specifically for inhalation injury. Facial flash burns, singed hairs, soot, hoarseness, stridor, respiratory distress, enclosed-space smoke exposure, or progressive edema should raise concern. A currently adequate airway can deteriorate as edema evolves, so early airway escalation is safer than waiting for a difficult late intubation in a high-risk patient. Do not intubate solely because the face is burned, but do not dismiss evolving airway findings because the initial oxygen saturation is normal.

Current-guidance distinction — the textbooks provide durable wound, anatomy, nerve/duct, and reconstruction principles. Disposition should follow current ABA referral guidance rather than older blanket rules: deep partial-thickness or full-thickness burns involving the face warrant immediate burn-center consultation with consideration for transfer, as does suspected inhalation injury; potentially deep burns warrant consultation. Facial location matters because eyelid, lip, nose, and ear injuries are functional/aesthetic units prone to contracture, and airway injury may coexist.

Failure/rescue — worsening pain, erythema, purulence, salivary swelling with meals, new facial weakness, dehiscence, exposed cartilage, ectropion, free-margin notching, or contour distortion should trigger re-examination for a missed deep injury or failed reconstruction rather than cosmetic reassurance. After burns, progressive hoarseness, stridor, respiratory effort, hypoxemia, or rapidly worsening edema demands urgent airway reassessment.

Senior synthesis — use five checks: FUNCTION asks which nerve, eye/lacrimal, salivary, cartilage, mucosal, dental, or airway structures are threatened; CLEAN asks whether contamination and nonviable tissue were addressed without over-debriding viable face; ALIGN asks which landmark must be restored first and which layers remove tension; REPAIR asks which deep structure requires immediate repair or deliberate staged reconstruction before skin closure; BURN asks whether depth, facial location, or inhalation risk changes airway planning and disposition. The dangerous errors are examining facial nerve function only after anesthetic, closing a cheek wound over an unrecognized nerve/duct injury, aggressively discarding potentially viable facial tissue, forcing a true defect closed under tension, and treating a deep facial burn as merely a skin wound while airway edema evolves."""

COHORT={QID:{
 "concept_id":CID,
 "canonical_topic":TOPIC,
 "prompt":PROMPT,
 "answer_text":ANSWER,
 "explanation":"Facial soft-tissue trauma is a functional-anatomy problem before it is a scar problem: document nerve/eye/lacrimal/salivary/cartilage/airway status before anesthetic or closure, preserve viable tissue, restore landmarks with layered low-tension repair, repair deep injuries before skin, and apply current burn-airway/referral guidance.",
 "board_pearl":"Before local anesthetic, document facial nerve function. Before closing a cheek wound, exclude facial nerve and Stensen duct injury. Before treating a facial burn as a wound, decide whether inhalation injury or burn depth changes the airway and disposition.",
 "depth_layers_v211":{"foundation":"Function-first facial examination, conservative tissue preservation, irrigation and precise layered landmark repair.","application":"Recognize and manage facial nerve, parotid duct, eyelid/canalicular, lip, nasal and auricular injuries before superficial closure.","senior_decision":"Choose primary versus staged reconstruction, selectively use antibiotics, recognize failed repair, and escalate deep facial burns/suspected inhalation injury using current burn-center guidance."},
 "common_traps_v211":[
  "Injecting local anesthetic before documenting facial nerve function and losing the baseline neurologic examination.",
  "Closing a cheek laceration without checking the course and function of Stensen duct and nearby facial nerve branches.",
  "Aggressively debriding marginal facial tissue that might survive because of the face's robust vascularity.",
  "Using skin sutures to pull a deep wound together instead of restoring muscle/dermal layers and eliminating tension or dead space.",
  "Missing the vermilion border, eyelid margin, helical rim, or nasal free margin and assuming later scar maturation will correct the distortion.",
  "Closing skin over a recognized nerve, duct, or canalicular transection without repairing it or making an explicit staged plan.",
  "Giving antibiotics to every clean facial laceration while underemphasizing irrigation, foreign-body removal, and selective prophylaxis.",
  "Assuming every facial burn requires prophylactic intubation rather than integrating inhalation-risk findings and evolution.",
  "Waiting for overt airway obstruction despite soot, hoarseness, enclosed-space exposure, or progressive edema.",
  "Treating deep partial/full-thickness facial burns as routine outpatient wounds instead of using current burn-center referral thresholds."
 ],
 "deliberate_review_v211":"Preserved from the stale pre-PTA facial-trauma branch and rehomed onto exact-head-green v20.10 main. The prior live reveal was shallow and omitted pre-anesthetic facial nerve documentation, parotid duct/canalicular injury, landmark-first layered repair, conservative tissue preservation, failed-repair rescue, inhalation-airway reasoning, and current burn-center referral thresholds.",
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
