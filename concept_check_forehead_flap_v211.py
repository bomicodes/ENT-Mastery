"""v20.11i focused depth patch for Forehead Flap / Nasal Reconstruction."""
from concept_check_board_repair_v177 import _find_module

QID="cc-v112-rec-facial-plastics-trauma-forehead-flap-nasal-reconstruction"
CID="v6-facial-plastics-trauma-forehead-flap-nasal-reconstruction"
TOPIC="Forehead Flap / Nasal Reconstruction"

SOURCE_REFS_V211_FOREHEAD=[
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected ENT Boards Library; facial plastic/reconstructive surgery sections on nasal reconstruction and forehead flaps.","role":"foundation/operative: nasal subunits, lining-support-cover analysis, flap design, staging and complications"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected ENT Boards Library; Chapter 8, Head and Neck Reconstructive Flaps and Facial Reconstruction Techniques.","role":"board framework: reconstructive ladder, flap vascularity, nasal reconstruction and donor-site planning"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected ENT Boards Library; facial plastic and reconstructive surgery sections.","role":"board/operative cross-check: nasal anatomy, reconstructive principles and flap complications"},
 {"type":"review","citation":"Correa BJ et al. Nasal Reconstruction: An Overview and Nuances. Semin Plast Surg. 2010;24:322-332.","role":"nasal subunit and three-layer lining/support/cover reconstruction principles"},
 {"type":"review","citation":"Two or Three? Approaches to Staging of the Paramedian Forehead Flap for Nasal Reconstruction. Plast Reconstr Surg Glob Open. 2021.","role":"contemporary staging framework: two- versus three-stage reconstruction according to defect complexity, vascular risk and need for intermediate thinning/framework refinement"},
]

PROMPT="""A patient has a large distal nasal defect after margin-controlled skin-cancer resection involving most of the ala and part of the tip. The defect includes external skin loss, missing alar cartilage support, and a focal full-thickness lining defect. A paramedian forehead flap is being considered. Explain how you decide whether the forehead flap is appropriate, how lining, support, and cover should be reconstructed and sequenced, the key supratrochlear/pedicle considerations, how two- versus three-stage reconstruction differs, what must be checked before pedicle division, and how you respond to early vascular compromise."""

ANSWER="""A paramedian forehead flap is not simply a large local skin flap; it is a staged interpolated axial flap used primarily to provide robust external nasal cover when the defect is too large, deep, multi-subunit, or structurally complex for primary closure, a skin graft, or a smaller local flap. Start with the true defect rather than the flap name. Map the nasal subunits involved, determine how much of each subunit is missing, and analyze the defect in three independent layers: internal LINING, STRUCTURAL SUPPORT, and external COVER. The forehead flap replaces cover. It does not independently recreate missing vestibular lining or alar/tip framework, so those components must be planned separately.

For the described ala-tip defect, first decide how lining will be restored, because an unsupported or poorly vascularized internal surface can contract and compromise the airway or reconstructed framework. Small lining defects may be managed with local mucosal options depending on location and available tissue; larger or complex lining deficits may require vascularized lining flaps or other reconstructive strategies. Next restore structural support where needed, commonly with cartilage to maintain alar contour, external-valve patency, tip shape, or dorsal framework. Only after the foundation is sound should external cover be transferred. Covering a deficient lining/support construct with a beautiful forehead flap does not make the reconstruction functionally complete.

The paramedian forehead flap is based on the supratrochlear vascular system and is designed as a vertically oriented interpolated flap with a pedicle near the medial brow. Template the actual nasal defect, confirm forehead height, hairline and scars, and design adequate length without unnecessary width or a hair-bearing distal segment when avoidable. During elevation, preserve the vascular pedicle and transition to the appropriate deeper plane near the brow/orbital rim rather than blindly thinning the pedicle. At transfer, the pedicle must lie without kink, torsion, compression, hematoma, or excessive inset tension. Early aggressive distal thinning can endanger perfusion; contour refinement can be staged when necessary.

Two-stage and three-stage reconstructions are both legitimate frameworks. A classic two-stage plan transfers the flap at stage 1 and divides/insets the pedicle after sufficient neovascularization and healing. A three-stage approach adds an intermediate operation before division, allowing safer thinning, contour refinement, and framework adjustment while the pedicle is still intact; this can be useful for thick flaps, complex three-dimensional defects, substantial framework work, or higher-risk vascular situations. The choice should follow defect complexity, tissue thickness, vascular risk and reconstructive goals rather than a rule that every forehead flap must use the same number of stages.

Before pedicle division, assess more than the calendar. The flap should be well healed and adequately vascularized from the recipient bed, with no unresolved distal ischemia, infection, dehiscence, or major wound-healing concern. Pedicle division is a perfusion/healing decision, not simply a scheduled event. At division, trim and inset the nasal and brow ends deliberately, preserve contour and brow position, and reassess airway, alar support, free-margin position and external contour.

Vascular compromise requires immediate pattern recognition and correction. A pale, cool flap with poor capillary refill or little bleeding suggests inadequate arterial inflow; a dusky, swollen/turgid flap with brisk dark bleeding suggests venous congestion. First eliminate reversible mechanical causes: release constricting sutures or dressings, correct pedicle twist/kink or compression, relieve excessive tension, and evacuate a compressive hematoma while preserving the pedicle. Reassess immediately. Persistent compromise with a plausible surgically correctable cause warrants early operative reassessment rather than passive observation. Selective venous-decongestion adjuncts can be considered when inflow is intact and no correctable obstruction remains, but they do not substitute for fixing torsion, compression, hematoma or tension.

Subunit principles help camouflage scars and restore contour, but they are guides rather than a command to excise viable normal nasal tissue automatically. Consider complete subunit replacement when loss is extensive and the expected aesthetic benefit outweighs sacrificing healthy tissue. Likewise, defect size alone does not determine the flap: depth, lining/support loss, adjacent tissue availability, scars/radiation, vascular risk and the patient's ability to undergo multiple stages all matter.

Senior synthesis — make seven decisions: DEFECT: which nasal subunits and layers are missing? INDICATION: does this need staged axial forehead skin rather than a smaller option? LINING: how will the internal surface be restored? SUPPORT: what cartilage/framework is required to resist contraction and preserve the valve? COVER: how will the supratrochlear flap be designed and transferred without pedicle distortion? STAGING: is two-stage reconstruction sufficient or is an intermediate thinning/refinement stage safer? DIVISION/RESCUE: is the flap truly healed and independently perfused, and if it becomes threatened have all reversible mechanical causes been corrected immediately? The dangerous alternatives are treating the forehead flap as a one-layer skin solution, placing cover over absent lining/support, over-thinning at the first transfer, accepting pedicle kink or tight inset, dividing because a date arrived despite questionable healing, and watching progressive congestion without correcting the cause."""

COHORT_FOREHEAD_V211={QID:{
 "concept_id":CID,"canonical_topic":TOPIC,"prompt":PROMPT,"answer_text":ANSWER,
 "explanation":"Paramedian forehead-flap reconstruction is a staged three-layer nasal problem: separately restore lining and support, use supratrochlear axial tissue for cover, choose staging deliberately, protect the pedicle, and treat vascular compromise as an immediate mechanical-rescue problem.",
 "board_pearl":"The forehead flap provides COVER. Large full-thickness nasal defects still require an independent plan for LINING and STRUCTURAL SUPPORT; pedicle division depends on healing/perfusion, not the calendar alone.",
 "curveball":"The flap is dusky and swollen after stage 1 and only looks acceptable when the inset sutures are loosened. Do not retighten the sutures or simply observe: remove compression/tension, check for pedicle kink/torsion and hematoma, restore a nonconstricting inset, and escalate early if perfusion remains abnormal.",
 "depth_layers_v211":["forehead-flap indication and nasal subunit analysis","lining-support-cover decomposition and sequence","supratrochlear axial pedicle anatomy","two- versus three-stage decision","initial transfer and conservative thinning","pedicle-division readiness","arterial versus venous compromise recognition and rescue","functional/aesthetic bailout decisions"],
 "common_traps_v211":[
  "Treating a forehead flap as a larger generic local flap",
  "Using forehead skin to cover a defect without separately reconstructing missing lining",
  "Ignoring alar/tip cartilage support and later valve collapse or contraction",
  "Choosing the flap from defect diameter alone instead of depth, subunits and missing layers",
  "Automatically excising healthy residual subunit tissue to satisfy the subunit principle",
  "Aggressively thinning the distal flap during the first transfer when perfusion is most vulnerable",
  "Allowing the supratrochlear pedicle to kink, twist, compress or sit under a tight dressing",
  "Teaching every forehead flap as obligatorily two-stage or obligatorily three-stage",
  "Dividing the pedicle because the scheduled date arrived despite questionable healing/perfusion",
  "Observing progressive venous congestion without correcting tension, compression, hematoma or pedicle distortion",
  "Calling a well-covered nose successful despite inadequate lining, alar support or nasal-valve function"
 ],
 "deliberate_review_v211":"Focused Concept Check repair aligned to the already-strong v34.4/v34.5 forehead-flap Concept Hub. Preserves the semantic split from general local-flap teaching and tests three-layer reconstruction, supratrochlear vascular anatomy, staging, division readiness and rescue.",
 "source_refs_v211":SOURCE_REFS_V211_FOREHEAD,
}}

def apply_forehead_flap_v211(checks,deep_modules,v6_item_id):
 result={"repaired":[],"missing":[],"link_mismatch":[]}; by={str(q.get("id") or ""):q for q in checks or []}
 for qid,p in COHORT_FOREHEAD_V211.items():
  q=by.get(qid)
  if not q: result["missing"].append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id)
  if not m or str(m.get("topic") or "")!=p["canonical_topic"]:
   result["link_mismatch"].append(qid); continue
  cid=v6_item_id(q.get("domain"),m.get("topic")) if q.get("domain") else None
  if cid!=p["concept_id"] or q.get("concept_id")!=cid:
   result["link_mismatch"].append(qid); continue
  q.update(p); q["task_alignment_v211"]=True; q["depth_patch_v211_forehead_flap"]=True
  q.pop("choices",None); q.pop("answer",None); q.pop("why_wrong",None)
  result["repaired"].append(qid)
 return result