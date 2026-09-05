"""v20.11g focused depth patch for Local Flap Reconstruction."""
from concept_check_board_repair_v177 import _find_module

QID="cc-v112-rec-facial-plastics-trauma-local-flap-reconstruction"
CID="v6-facial-plastics-trauma-local-flap-reconstruction"
TOPIC="Local Flap Reconstruction"

SOURCE_REFS_V211_LOCAL_FLAP=[
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected ENT Boards Library; facial plastic/reconstructive surgery sections on local tissue transfer, defect analysis, flap design, vascularity, and complication management.","role":"foundation/operative: reconstructive ladder, local tissue mechanics, vascularity, aesthetic-unit and tension-vector planning"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected ENT Boards Library; Chapter 8, Head and Neck Reconstructive Flaps and Facial Reconstruction Techniques.","role":"board framework: advancement/rotation/transposition concepts, random versus axial blood supply, flap selection and donor-site planning"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected ENT Boards Library; facial plastic and reconstructive surgery sections.","role":"board/operative cross-check: local flap geometry, vascular preservation, facial subunits and reconstructive complications"},
]

PROMPT="""A patient has a full-thickness cutaneous defect of the lateral cheek after margin-controlled skin-cancer excision. Primary closure would pull the lower eyelid and oral commissure, but several adjacent areas have usable laxity. Before choosing an advancement, rotation, or transposition flap, how should the ENT surgeon analyze the defect, choose and design the local flap, protect blood supply and nearby free margins, close the donor defect, and recognize or rescue a flap that is becoming ischemic or distorted?"""

ANSWER="""Start with the defect, not the flap name. Local reconstruction succeeds when nearby tissue is recruited because its thickness, color, texture, hair-bearing quality, and contour match the missing tissue better than distant tissue—not because a particular named flap is routinely used in that region. First define the defect after oncologic clearance or definitive debridement: exact location, surface dimensions, depth, exposed cartilage/bone/nerve, missing lining or structural support, relationship to facial aesthetic units, and proximity to free margins such as the eyelid, nasal ala, lip, brow, and oral commissure. Then assess where adjacent skin actually moves. Pinch and move the surrounding tissue in several vectors rather than assuming the most obvious donor site has adequate laxity.

Reconstructive choice — ask whether secondary healing, primary closure, a skin graft, a local flap, a regional flap, or free tissue is the simplest option that restores both function and appearance. Do not climb the reconstructive ladder automatically. A small concave defect may heal well secondarily; a superficial defect with a suitable bed may accept a graft; a local flap becomes attractive when tissue match, contour, structural coverage, or free-margin protection makes simple closure or grafting inferior. Conversely, a very large, composite, irradiated, or poorly vascularized defect may exceed the safe reach of a local flap.

Tension-vector planning is a functional decision. Before making an incision, predict where closure forces will go. The final scar is less important than avoiding a vector that everts an eyelid, retracts an ala, distorts the vermilion, elevates a brow, or pulls an oral commissure. Place incisions along relaxed skin-tension lines, borders of aesthetic subunits, or existing creases when that is compatible with safe flap geometry. Excising extra normal tissue simply to force a textbook geometric design is not automatically justified; modify the design to the actual defect and available laxity.

Advancement, rotation, and transposition solve different mechanical problems. An advancement flap moves tissue primarily in a straight-line direction and works when laxity lies directly adjacent to the defect; Burrow triangles or standing-cone management may be needed, but their placement should not sacrifice a free margin or critical landmark. A rotation flap recruits tissue through an arc around a pivot point and converts surrounding laxity into movement toward the defect; an adequately long curvilinear incision and appropriate undermining reduce excessive tension at the leading edge. A transposition flap moves tissue over an intervening segment into the defect, changing the direction from which laxity is recruited; bilobed, rhombic, and nasolabial-type designs are examples of the principle, but each creates a secondary donor defect and potential pivot-point tension. Choose geometry based on where tissue can safely move, not on memorizing one flap per facial subunit.

Blood supply — distinguish the concept of a random-pattern flap from an axial-pattern flap. Random-pattern local flaps depend on the dermal/subdermal vascular plexus and therefore require a design, base, thickness, and length that preserve perfusion; do not make the pedicle unnecessarily narrow or thin the flap aggressively at its base. Axial-pattern flaps incorporate a known named vascular supply and can permit greater reliable reach, but the pedicle still must be protected from division, compression, torsion, or thermal injury. There is no single universal length-to-width ratio that safely applies to every facial flap: vascular territory, tissue thickness, prior scars, smoking, radiation, prior surgery, and the specific flap design all modify reliability. Treat a memorized ratio as a rough historical teaching aid, not as permission to ignore perfusion.

Undermining and elevation — elevate in the plane appropriate for that region and flap while preserving the vascular network needed by the design. Adequate undermining can redistribute tension, but excessive or overly superficial undermining can injure blood supply, motor branches, sensory nerves, ducts, or vessels. On the cheek, know the relationship of the facial nerve branches and parotid duct; near the nose, eyelid, lip, or ear, preserve the structural elements that maintain free-margin shape. Use meticulous hemostasis because a hematoma can both separate the flap from its bed and compress inflow/outflow.

Inset — the flap should reach the defect without relying on tight sutures to overcome a poor design. If the leading edge only reaches under substantial traction, stop and gain mobility by additional safe undermining, back-cut or design modification when appropriate, or choose another reconstruction. Do not strangulate the pedicle with deep sutures. Use layered closure to remove dead space and shift tension away from the epidermis while avoiding injury to the vascular base. Align high-salience landmarks first. Trim tissue conservatively after the flap has been transferred; premature aggressive thinning or trimming can convert a viable flap into an ischemic one.

Donor-site planning matters as much as defect closure. Ask where the secondary defect will lie, whether it closes primarily, what direction its tension will take, and whether the resulting scar or standing cone crosses an aesthetic boundary. A technically viable flap that creates lower-lid ectropion, alar notching, oral incompetence, or a conspicuous misplaced donor scar is not a successful reconstruction. Whenever possible, distribute scars at subunit borders or natural creases and preserve the option for revision.

Early perfusion assessment — after inset, evaluate color, capillary refill, temperature, turgor, and bleeding characteristics rather than documenting only that the flap 'looks good.' Pale, cool tissue with sluggish refill suggests arterial insufficiency; a dusky, congested, swollen flap with brisk dark bleeding suggests venous outflow impairment. First look for correctable mechanical causes: excessive inset tension, a kinked/twisted pedicle, constricting sutures, tight dressings, or hematoma. Release constricting sutures or dressings, remove the offending compression, and evacuate a hematoma promptly when indicated. Progressive ischemia is not treated by simply waiting because 'local flaps usually survive.' If perfusion does not normalize, reopen or revise the inset/pedicle and escalate reconstruction based on the threatened tissue and cause.

Late failure and distortion — distal epidermolysis, partial necrosis, infection, dehiscence, trapdoor/pincushion deformity, standing cones, hypertrophic scar, sensory change, and free-margin retraction require different responses. Small superficial eschar may be allowed to declare itself before conservative wound care or later revision, whereas full-thickness necrosis, exposed cartilage/hardware, infection, or functional distortion can require debridement and new coverage. Trapdoor deformity may improve with time, massage, steroid treatment, scar release, thinning, or revision depending on mechanism and persistence. Ectropion, alar retraction, or oral-commissure distortion should trigger analysis of the original tension vector rather than cosmetic camouflage alone.

Senior synthesis — make six decisions in order. DEFECT: what tissue layers and landmarks are missing? LAXITY: from which direction can similar tissue move without distorting a free margin? GEOMETRY: does advancement, rotation, or transposition best redirect that laxity? PERFUSION: what vascular plexus or named pedicle must remain intact, and are prior scars/radiation/smoking changing reliability? DONOR: what secondary defect and tension vector am I creating? RESCUE: if the flap becomes pale, congested, tense, or distorted, is there a mechanical problem I can immediately reverse? The dangerous alternatives are choosing a named flap before analyzing the defect, forcing primary closure across an eyelid/ala/lip, using a universal length-to-width rule as dogma, narrowing or thinning the pedicle for convenience, underestimating the donor defect, relying on tight sutures to obtain reach, accepting venous congestion as normal postoperative color, or waiting on a correctable hematoma/torsion until tissue is lost."""

COHORT_LOCAL_FLAP_V211={QID:{
 "concept_id":CID,"canonical_topic":TOPIC,"prompt":PROMPT,"answer_text":ANSWER,
 "explanation":"Local flap reconstruction is defect-first planning: map tissue layers and free margins, locate laxity, choose advancement/rotation/transposition geometry, preserve perfusion, control donor-site tension, and recognize reversible flap compromise early.",
 "board_pearl":"Choose the flap from the defect and tension vector, not from a memorized facial-region recipe. A flap that closes the hole but distorts the eyelid, ala, lip, or commissure is a reconstructive failure.",
 "curveball":"The flap is dusky and swollen immediately after inset. Before accepting this as expected postoperative change, release constricting sutures/dressings, inspect for pedicle kinking or torsion, and exclude a hematoma causing venous outflow obstruction.",
 "depth_layers_v211":["defect and reconstructive-ladder analysis","facial aesthetic units and free-margin protection","advancement versus rotation versus transposition mechanics","random versus axial vascularity","undermining/inset and donor-site planning","ischemia/congestion recognition and rescue"],
 "common_traps_v211":[
  "Choosing a named flap before analyzing defect depth, landmarks, and available laxity",
  "Forcing primary closure when its vector will retract the eyelid, ala, lip, brow, or commissure",
  "Teaching one local flap as mandatory for a particular facial subunit",
  "Using a universal random-flap length-to-width ratio as a guarantee of viability",
  "Narrowing or aggressively thinning the pedicle to improve apparent mobility",
  "Assuming an axial flap cannot fail because it contains a named vessel",
  "Using tight inset sutures to compensate for inadequate flap reach",
  "Ignoring the location and tension vector of the secondary donor defect",
  "Calling a dusky congested flap normal without checking torsion, compression, or hematoma",
  "Waiting on progressive ischemia instead of correcting a reversible mechanical cause",
  "Treating closure of the skin defect as success despite new ectropion, alar retraction, or oral distortion",
 ],
 "deliberate_review_v211":"Rehomed onto current post-Draf/post-Four-Gland main after the prior Local Flap branch became stale. Preserves the hand-curated defect-first reconstruction teaching while extending current exact-canonical gates without overwriting newer cohorts.","source_refs_v211":SOURCE_REFS_V211_LOCAL_FLAP,
}}

def apply_local_flap_reconstruction_v211(checks,deep_modules,v6_item_id):
 result={"repaired":[],"missing":[],"link_mismatch":[]}; by={str(q.get("id") or ""):q for q in checks or []}
 for qid,p in COHORT_LOCAL_FLAP_V211.items():
  q=by.get(qid)
  if not q: result["missing"].append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id)
  if not m or str(m.get("topic") or "")!=p["canonical_topic"]:
   result["link_mismatch"].append(qid); continue
  cid=v6_item_id(q.get("domain"),m.get("topic")) if q.get("domain") else None
  if cid!=p["concept_id"] or q.get("concept_id")!=cid:
   result["link_mismatch"].append(qid); continue
  q.update(p); q["task_alignment_v211"]=True; q["depth_patch_v211_local_flap"]=True
  q.pop("choices",None); q.pop("answer",None); q.pop("why_wrong",None)
  result["repaired"].append(qid)
 return result
