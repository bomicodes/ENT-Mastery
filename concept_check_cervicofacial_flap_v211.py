"""v20.11h focused depth patch for Cervicofacial Flap."""
from concept_check_board_repair_v177 import _find_module

QID="cc-v112-rec-facial-plastics-trauma-cervicofacial-flap"
CID="v6-facial-plastics-trauma-cervicofacial-flap"
TOPIC="Cervicofacial Flap"

SOURCE_REFS_V211_CERVICOFACIAL=[
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected ENT Boards Library; facial plastic/reconstructive surgery sections on cheek reconstruction and local-regional tissue transfer.","role":"foundation/operative: defect analysis, cheek reconstruction, vascularity, tension and complication management"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected ENT Boards Library; Chapter 8, Head and Neck Reconstructive Flaps and Facial Reconstruction Techniques.","role":"board framework: local-regional flap selection, vascular design, donor-site planning and facial reconstruction"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected ENT Boards Library; facial plastic and reconstructive surgery sections.","role":"board/operative cross-check: cheek reconstruction, facial nerve anatomy, flap complications"},
 {"type":"systematic_review","citation":"Alam DS et al. An outcome comparison of superficial versus deep plane dissection of cervicofacial flaps: a systematic review and meta-analysis. J Plast Reconstr Aesthet Surg. 2021. PMID 33386263.","role":"contemporary evidence: superficial and deep-plane dissections both have low reported complication rates; no evidence supports teaching one plane as universally mandatory"},
 {"type":"review","citation":"Sakellariou A, Salama A. The use of cervicofacial flap in maxillofacial reconstruction. Oral Maxillofac Surg Clin North Am. 2014;26:389-400. PMID 24980990.","role":"indications/anatomy: cervicofacial flap for cheek, temple and orbital defects, alone or combined with regional/free tissue according to defect extent"},
]

PROMPT="""After margin-controlled resection of a large lateral cheek skin cancer, the defect approaches the lower eyelid and extends toward the preauricular cheek. Primary closure would create a strong inferior vector on the lid, while adjacent cheek and cervical skin remain mobile. When is a cervicofacial rotation-advancement flap a good choice, how should it be designed and elevated, what structures and perfusion problems matter, how do you prevent ectropion, and when should you abandon the plan for a different regional or free-tissue reconstruction?"""

ANSWER="""A cervicofacial flap is a large rotation-advancement concept, not simply a bigger generic local flap. It is most useful when a moderate-to-large cheek, lateral face, temple, or selected periorbital cutaneous defect needs a broad sheet of adjacent skin with excellent color, thickness, and texture match and when the neck/preauricular tissues provide enough laxity to recruit that skin without sacrificing a critical free margin. Start by confirming the defect is actually a surface-tissue problem that this flap can solve: define its cheek zone, depth, exposed parotid/facial nerve/cartilage/bone, lower-eyelid involvement, prior scars or radiation, and whether lining, major bulk, structural support, or vascularized tissue for a hostile bed is also missing. A very deep composite defect, major dead space, exposed critical structures in a compromised field, or insufficient regional laxity may be better served by another regional flap or free tissue rather than forcing a cervicofacial flap beyond its capabilities.

Design around recruitment and tension. The flap generally recruits preauricular, lateral facial, and cervical skin through a broad rotation-advancement arc; incisions can be hidden along natural preauricular and cervical creases when oncologically and mechanically appropriate. The key question is not how long the incision is but whether the arc and undermining create enough mobility that the leading edge reaches without tight inset. Preserve a broad vascularized base and avoid unnecessary distal narrowing. Plan the secondary standing cone/donor closure before cutting, because the neck donor closure can create a new vector back toward the cheek and eyelid.

Lower-eyelid protection is a defining decision. A defect near the lid-cheek junction is vulnerable to postoperative ectropion from gravity, scar contraction, and especially inferior or vertical tension transmitted to the lid. Redirect closure forces laterally/superolaterally rather than hanging the flap from the lower eyelid. When the defect or flap geometry places meaningful load on the lid, use deep fixation to stable periosteal/fascial support and add canthal support when clinically indicated rather than relying on skin sutures to hold the lid position. Recheck lid position after inset with the patient-level geometry in mind. A well-perfused flap that causes ectropion is still a reconstructive failure.

Elevation plane requires judgment rather than dogma. Traditional superficial/subcutaneous and deeper sub-SMAS/platysmal approaches are both described. Deeper elevation can recruit thicker tissue and release retaining structures, but it brings the dissection into closer relationship with facial nerve branches and other deeper anatomy. Contemporary systematic-review data have not shown a clear complication advantage for one plane over the other, and the evidence quality is limited. Therefore choose the plane according to defect, required mobility/thickness, prior surgery, surgeon familiarity, and regional anatomy; do not teach that every cervicofacial flap must be deep-plane or that superficial elevation is automatically safer. Whichever plane is chosen, know where facial nerve branches become vulnerable, respect the parotid region, and avoid blind deep cautery or traction.

Perfusion remains a whole-flap problem. Preserve an adequately broad base, avoid pedicle kinking or torsion, avoid aggressive distal thinning, maintain meticulous hemostasis, and do not close under excess tension. Smoking, radiation, prior scars, previous surgery, and long distal reach can reduce reliability. At inset, examine color, temperature, capillary refill, turgor, and bleeding. Pale/cool/sluggish tissue suggests inflow compromise; dusky swollen tissue with brisk dark bleeding suggests venous congestion. First correct mechanical causes: release tight sutures or dressings, remove compression, evacuate hematoma, eliminate a kink/twist, and revise inset tension. Do not simply observe a progressively compromised distal flap.

Complication prevention is geometry plus surveillance. Hematoma can compress the flap and must be treated promptly. Distal epidermolysis or necrosis is more likely where reach and tension are greatest; avoid sacrificing more normal tissue merely to obtain a textbook shape. Facial weakness after deeper dissection demands distinction between neuropraxia and a recognized nerve injury. Lower-lid malposition should be addressed according to mechanism and severity; early support and tension correction are different problems from late cicatricial ectropion that may require scar release, lid tightening/support, grafting, or revision reconstruction.

Bailout thinking belongs in the original plan. If adequate reach requires excessive traction, the distal flap becomes poorly perfused, closure will pull the lower eyelid despite support, or the defect requires missing bulk/lining/support that this skin flap cannot replace, stop escalating the same design. Consider another local option, a regional flap, or free tissue based on the missing components and recipient bed. The cervicofacial flap can also be combined with other reconstruction when it is the best skin-cover component but not a complete solution.

Senior synthesis — make six decisions: INDICATION: is this primarily a cheek/lateral-face skin defect with useful adjacent cervicocervical laxity? VECTOR: can I recruit tissue without pulling the lower lid or another free margin? PLANE: what elevation plane gives the required mobility/thickness while respecting facial nerve and parotid anatomy? SUPPORT: does the lid-cheek junction need deep fixation or canthal support? PERFUSION: is the distal flap reaching without tension, compression, hematoma, or pedicle distortion? BAILOUT: if the defect is composite, irradiated, poorly vascularized, or beyond safe reach, what regional/free-tissue option better restores the missing components? The dangerous alternatives are memorizing a single dissection plane, using skin sutures to fight an inferior lid vector, accepting a tight distal inset, ignoring donor-site forces, assuming a broad flap cannot become congested, and forcing cervicofacial skin to solve a defect that actually needs vascularized bulk or structural reconstruction."""

COHORT_CERVICOFACIAL_V211={QID:{
 "concept_id":CID,"canonical_topic":TOPIC,"prompt":PROMPT,"answer_text":ANSWER,
 "explanation":"Cervicofacial reconstruction is a large cheek rotation-advancement problem: select the right defect, recruit cheek/neck skin with a safe vector, choose the dissection plane deliberately, protect the facial nerve and lower eyelid, preserve distal perfusion, and bail out when the defect needs more than skin cover.",
 "board_pearl":"Near the lid-cheek junction, flap viability is not enough: eliminate inferior lid tension and add stable deep/canthal support when needed. Do not teach superficial or deep-plane elevation as universally mandatory.",
 "curveball":"The flap reaches only when the lower eyelid is pulled inferiorly and the distal edge becomes dusky. Do not tighten the skin sutures and hope it settles: release the inset, correct compression/kinking or hematoma, restore a safer vector and mobility, and change the reconstruction if adequate reach and lid position cannot coexist.",
 "depth_layers_v211":["indications and defect-component analysis","cervicofacial recruitment and donor-site planning","lower-eyelid tension and ectropion prevention","superficial versus deep-plane decision","facial nerve/parotid danger anatomy","distal perfusion recognition and rescue","regional/free-tissue bailout"],
 "common_traps_v211":[
  "Choosing a cervicofacial flap for a composite defect that also needs major bulk, lining, or structural support",
  "Treating the cervicofacial flap as interchangeable with a small generic local flap",
  "Teaching deep-plane elevation as mandatory despite limited comparative evidence",
  "Assuming superficial elevation eliminates facial nerve risk",
  "Allowing the flap or donor closure to place an inferior vector on the lower eyelid",
  "Using tight skin sutures instead of deep support or redesign to control lid position",
  "Ignoring the donor neck closure and its contribution to tension",
  "Aggressively thinning or narrowing the distal flap for easier inset",
  "Observing progressive venous congestion without correcting compression, hematoma, kink, or inset tension",
  "Calling a viable flap successful despite new ectropion",
  "Forcing the same flap when safe reach and perfusion cannot be achieved"
 ],
 "deliberate_review_v211":"Focused cervicofacial-flap teaching kept distinct from the general Local Flap Reconstruction cohort. Emphasizes cheek/neck recruitment, lid vector/support, plane-selection nuance, facial nerve danger anatomy, distal perfusion and reconstruction bailout.",
 "source_refs_v211":SOURCE_REFS_V211_CERVICOFACIAL,
}}

def apply_cervicofacial_flap_v211(checks,deep_modules,v6_item_id):
 result={"repaired":[],"missing":[],"link_mismatch":[]}; by={str(q.get("id") or ""):q for q in checks or []}
 for qid,p in COHORT_CERVICOFACIAL_V211.items():
  q=by.get(qid)
  if not q: result["missing"].append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id)
  if not m or str(m.get("topic") or "")!=p["canonical_topic"]:
   result["link_mismatch"].append(qid); continue
  cid=v6_item_id(q.get("domain"),m.get("topic")) if q.get("domain") else None
  if cid!=p["concept_id"] or q.get("concept_id")!=cid:
   result["link_mismatch"].append(qid); continue
  q.update(p); q["task_alignment_v211"]=True; q["depth_patch_v211_cervicofacial"]=True
  q.pop("choices",None); q.pop("answer",None); q.pop("why_wrong",None)
  result["repaired"].append(qid)
 return result