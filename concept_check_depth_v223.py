"""v20.23 — deepen exact-live Forehead Flap / Nasal Reconstruction.

Durable nasal reconstruction, supratrochlear pedicle and flap-rescue principles are
cross-referenced against connected Cummings 7e, Pasha 6e and K.J. Lee 12e texts.
Traditional staging is explicitly distinguished from newer selected early-division data.
"""
from concept_check_board_repair_v177 import _find_module

QIDS = ("cc-v112-rec-facial-plastics-trauma-forehead-flap-nasal-reconstruction",)
CID = "v6-facial-plastics-trauma-forehead-flap-nasal-reconstruction"
TOPIC = "Forehead Flap / Nasal Reconstruction"

SOURCE_REFS_V223 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive split corpus; Part 3, Skin Flap Physiology and Wound Healing, including pedicled-flap monitoring/salvage and ICG-assisted paramedian forehead-flap take-down discussion; cross-referenced 2026-09-10.","role":"durable physiology/rescue: flap perfusion, early recognition of compromise, mechanical pedicle rescue, traditional 3-4 week division framework and selected perfusion-guided earlier take-down"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy Drive id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52; Ch 8 Reconstructive and Facial Plastic Surgery, paramedian forehead flap/facial reconstruction sections around p 472; cross-referenced 2026-09-10.","role":"resident/board framework: supratrochlear basis, extensive nasal-defect indication, traditional staged division and two- versus three-stage thinning"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy Drive id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR; Ch 55 Reconstructive Head and Neck Surgery, paramedian forehead flap p 1061; cross-referenced 2026-09-10.","role":"operative cross-check: supratrochlear artery basis and use for nasal defects including extension toward upper lip/medial cheek"},
    {"type":"review","citation":"McAllister L, Thornton J. Complex Nasal Reconstruction: A Methodical Approach to the Three-Stage Paramedian Forehead Flap. Semin Plast Surg. 2024;38(4):297-303. PMID: 39697410.","role":"contemporary complex reconstruction: three-layer lining/support/cover planning, lining replacement and cartilage framework in complex multi-subunit/full-thickness defects"},
    {"type":"systematic_review","citation":"Ma CC, et al. Early Division of the Paramedian Forehead Flap: A Systematic Review and Retrospective Analysis. Laryngoscope. 2025;135(7):2233-2240. PMID: 39871421.","role":"current timing boundary: division at 16 days or earlier can be successful in carefully selected patients, especially partial-thickness defects; evidence does not support blanket early division for all complex defects"},
    {"type":"comparative_study","citation":"Palmer WJ, et al. Outcomes and Complications of 2-Stage Versus 3-Stage Paramedian Forehead Flaps. Otolaryngol Head Neck Surg. 2025;172(6):1888-1896. PMID: 40062609.","role":"current staging boundary: both two- and three-stage pathways are effective; three-stage use tracks greater framework complexity and selected accelerated take-down was not associated with worse outcomes"},
    {"type":"review","citation":"Howard BE, Patel S, Shockley WW, Clark JM. Total Nasal Reconstruction: Advances in Free Tissue Transfer for Internal Lining and Structural Support. Facial Plast Surg Clin North Am. 2024;32(2):247-259. PMID: 38575283.","role":"three-layer reconstruction boundary: internal lining and structural support remain separate reconstructive problems from external forehead-flap cover"},
]

PROMPT = """A 68-year-old patient has a large distal nasal defect after margin-controlled cutaneous cancer resection involving most of the ala and part of the tip. There is external skin loss, a focal full-thickness lining defect and loss of alar structural support. A paramedian forehead flap is being considered. As the senior resident, how do you decide whether the flap is appropriate, reconstruct lining/support/cover, design and protect the supratrochlear pedicle, choose two versus three stages and timing of division, preserve nasal-valve function, and rescue early arterial or venous compromise? Explain what current evidence changes about traditional pedicle-division timing and what it does not change?"""

ANSWER = """Foundation — start with the defect, not the flap name. Nasal reconstruction is a three-layer problem: internal LINING, STRUCTURAL SUPPORT, and external COVER. A paramedian forehead flap is principally a robust axial option for external cover when a defect is large, deep, multi-subunit, distal, poorly suited to grafting, or too complex for a smaller local flap. It does not by itself solve missing vestibular lining or recreate an absent alar/tip framework. The first senior decision is therefore whether the patient has a cover-only defect or a composite defect whose lining and support must be rebuilt independently.

Map the involved aesthetic subunits and functional boundaries. Measure the true defect after oncologic clearance, inspect the alar rim and soft triangle, assess remaining cartilage, internal lining, vestibular scar risk and external nasal valve, and note prior scars, radiation, smoking/vascular risk and forehead height/hairline. Subunit principles can improve contour and scar camouflage, but they are a guide rather than a command to discard healthy tissue simply to complete a subunit. The reconstructive plan must protect airway and structure as well as appearance.

LINING — a full-thickness defect needs a vascularized internal surface or another reliable lining strategy appropriate to its size and location. Small focal lining deficits may be managed with local mucosal/turn-in options when tissue quality permits; larger or more complex defects may require folded forehead-flap designs, regional lining, or free tissue in extreme subtotal/total defects. Lining must be stable enough to support subsequent framework and resist contraction. A beautiful external flap over inadequate lining can contract, distort the ala and obstruct the valve.

SUPPORT — replace structural support when loss or expected scar contraction threatens contour or airway. Cartilage is commonly used to recreate alar stiffness, tip projection or other framework. The key is functional indication rather than a reflex rule that every defect receives the same graft. Modern reports describe selected folded/two-stage techniques in which some full-thickness distal defects can succeed without separate cartilage, but those small, technique-specific series do not erase the durable principle: ask whether this particular defect needs support to prevent collapse or distortion. Complex multi-subunit and subtotal reconstructions commonly require framework.

COVER — the paramedian forehead flap is based on the supratrochlear vascular system. Design from an accurate template, preserving adequate length and avoiding unnecessary pedicle width or hair-bearing distal skin when feasible. During elevation, respect the pedicle and the change in dissection plane toward the brow/orbital rim. Do not aggressively thin the vascularly vulnerable distal flap or blindly skeletonize the pedicle simply to obtain ideal contour at stage one. A thicker safe flap can be refined later; a necrotic thin flap cannot.

At transfer, inspect the entire pedicle path. The bridge must not be kinked, twisted, compressed by dressings, strangulated by inset sutures or placed under excessive tension. A hematoma under the flap or pedicle can convert a technically sound reconstruction into an ischemic one. Establish lining and structural support in a sequence that leaves them vascularized and mechanically stable, then inset cover without compressing the pedicle. Reassess the alar rim and external valve before leaving the operating room.

STAGING — two-stage and three-stage reconstructions are both legitimate. In a classic two-stage pathway, the flap is transferred at stage one and later divided/inset after neovascularization. A three-stage pathway adds an intermediate operation while the pedicle remains intact, allowing additional thinning, contour refinement and framework adjustment with retained axial inflow. Three-stage reconstruction is particularly useful when the defect is thick, complex, multi-layered, heavily framework-dependent or when safer delayed thinning is valuable. Current comparative data do not establish that every patient has superior outcomes with three stages; the stage count should follow defect complexity and reconstructive goals.

TRADITIONAL VERSUS CURRENT DIVISION TIMING — traditional teaching commonly places pedicle division around 3 to 4 weeks after inset/healing. That remains a durable, conservative framework and is reflected in core texts. Current evidence refines rather than abolishes it. A 2025 systematic review found successful division at 16 days or earlier in selected patients, but several included studies excluded full-thickness defects and the institutional cohort consisted of partial-thickness defects without cartilage grafting. Some studies used indocyanine-green perfusion assessment. A 2025 comparative series also found selected accelerated takedown at 21 days or earlier without increased failures. The senior lesson is therefore not 'divide at 10 days.' It is that division timing is a healing, perfusion and complexity decision rather than a fixed calendar rule, and lower-complexity, well-perfused cases may be candidates for accelerated division when the surgeon has a reliable assessment strategy.

Before division, evaluate the flap clinically: color, temperature, capillary refill, bleeding when appropriately tested, inset healing, infection, dehiscence and distal viability. Confirm that recipient-bed neovascularization is sufficient for the planned interruption of the pedicle. Perfusion adjuncts such as ICG can be helpful in selected accelerated protocols but do not replace judgment. Full-thickness defects, major lining work, substantial framework, questionable perfusion, irradiated tissue, infection or wound-healing concern should lower enthusiasm for accelerated division. Never divide simply because a date arrived.

VASCULAR RESCUE — recognize the pattern early. A pale, cool flap with delayed or absent capillary refill suggests inadequate arterial inflow. A dusky, swollen, congested flap with brisk dark bleeding suggests impaired venous outflow. The first response is mechanical: release constriction by removing tight dressings or sutures, correct pedicle kink/torsion, relieve tension and evacuate a compressive hematoma. Reassess immediately. If there is persistent compromise with a plausible surgically correctable cause, early operative reassessment is preferable to passive observation. Adjunctive venous-decongestion strategies may have a role after intact inflow and absence of a correctable obstruction are established, but they do not substitute for fixing a twisted or compressed pedicle.

Do not let generalized free-flap salvage algorithms obscure the physiology of an interpolated pedicled flap. There is no microvascular anastomosis to revise, but the macrocirculatory conduit can still be mechanically compromised. Conversely, not every color change is pedicle thrombosis: assess systemic hypotension, temperature, excessive vasoconstriction, hematoma, infection and local pressure. The clinical trajectory matters, and progressive compromise demands action.

NASAL FUNCTION — reconstruct alar support and lining with the external valve in mind. An ala that looks symmetric at rest can still collapse during inspiration if lateral-wall support is inadequate. Avoid an overly bulky internal lining that narrows the vestibule, excessive rim tension that notches the ala, or aggressive thinning that sacrifices vascularity. Secondary refinement is acceptable when the safer first-stage priority is perfusion and structural integrity.

ONCOLOGIC/OPERATIVE BOUNDARY — margin control precedes elaborate reconstruction. Do not design a complex flap around an uncertain tumor margin when additional resection is reasonably expected. Likewise, reconstructive elegance should not drive unsafe sacrifice of functional nasal tissue. If intraoperative perfusion, lining viability or framework stability is worse than expected, stage the problem rather than forcing definitive contour. A temporary imperfect contour is safer than a threatened flap or unsupported airway.

EVIDENCE BOUNDARY — there is no FDA indication or major society guideline that dictates two versus three PMFF stages or a universal day for pedicle division. Durable anatomic and operative principles come from reconstructive textbooks and longstanding surgical experience. Current 2024-2025 peer-reviewed literature updates patient selection, confirms that both two- and three-stage strategies can work, and supports selected earlier division. Those data are mostly retrospective/observational and heterogeneous; they should refine individualized decisions, not become a new absolute rule.

Senior synthesis — make eight decisions: DEFECT: which subunits and layers are missing? INDICATION: does the defect truly need staged forehead tissue? LINING: what vascularized internal surface will resist contraction? SUPPORT: what framework is required for contour and valve function? COVER: how will the supratrochlear flap reach without tension, torsion or over-thinning? STAGING: is two-stage adequate or does complexity favor an intermediate stage? DIVISION: is the flap independently healed and perfused, with accelerated timing only in a selected appropriate case? RESCUE: if the flap becomes pale or congested, have compression, kink, torsion, tension and hematoma been corrected immediately? The dangerous alternatives are treating forehead skin as a one-layer solution, sacrificing support or lining, over-thinning early, accepting a distorted pedicle, using a rigid calendar for division, or watching progressive compromise without correcting its mechanical cause."""

TRAPS = [
    "Treating the forehead flap as a one-layer skin solution and failing to plan lining and structural support independently.",
    "Choosing a flap from defect diameter alone while ignoring subunit involvement, depth, valve function, scars, radiation and forehead geometry.",
    "Covering a full-thickness defect before establishing a reliable lining plan, then accepting contraction and vestibular stenosis.",
    "Assuming every full-thickness defect must receive the identical cartilage graft rather than asking whether support is functionally required in that reconstruction.",
    "Misreading selected no-cartilage folded-flap series as proof that alar/tip framework is generally unnecessary.",
    "Aggressively thinning the distal flap at first transfer and trading contour for vascular compromise.",
    "Allowing a supratrochlear pedicle to kink, twist, compress under a dressing, or sit under a tight inset.",
    "Ignoring a small hematoma beneath the pedicle or flap even though local pressure can threaten perfusion.",
    "Teaching three-stage reconstruction as universally superior rather than selecting staging by defect and framework complexity.",
    "Teaching two-stage reconstruction as universally simpler when an intermediate thinning/framework stage may reduce risk in a complex defect.",
    "Using 3 to 4 weeks as an inflexible pedicle-division rule rather than a traditional reference point modified by healing and perfusion.",
    "Overgeneralizing 2025 early-division data from selected, frequently partial-thickness defects to every full-thickness or high-risk reconstruction.",
    "Dividing early without accounting for lining work, framework, radiation, infection, wound problems or questionable neovascularization.",
    "Mistaking a pale ischemic flap for venous congestion or a dusky swollen flap for simple bruising and delaying correction.",
    "Trying pharmacologic or leech-based adjuncts before releasing constriction, correcting torsion/kink or evacuating a compressive hematoma.",
    "Calling a reconstruction successful based on skin survival while ignoring alar collapse, nasal-valve obstruction, rim notching or vestibular stenosis.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "explanation": "Forehead-flap nasal reconstruction is a three-layer functional problem. Restore lining and support as indicated, use supratrochlear tissue for cover, select staging and division by complexity/perfusion, and treat early vascular compromise as an immediate mechanical-rescue problem.",
    "board_pearl": "The forehead flap supplies COVER, not automatically LINING or SUPPORT. Traditional division is roughly 3-4 weeks, but current evidence allows selected earlier division; the decision is based on healing, perfusion and defect complexity rather than the calendar alone.",
    "depth_layers_v223": {
        "foundation":"Nasal subunits; lining-support-cover analysis; supratrochlear axial pedicle; external-valve and alar-support principles.",
        "application":"Defect mapping, lining/framework selection, safe elevation/inset, two- versus three-stage planning and perfusion-based division readiness.",
        "senior_decision":"Recognize arterial versus venous compromise, correct mechanical causes immediately, stage/bail out when perfusion or framework is unsafe, and apply accelerated-division evidence only to appropriately selected cases.",
    },
    "common_traps_v223": TRAPS,
    "deliberate_review_v223": {
        "why_review":"High-yield facial plastics/OR concept where aesthetic success depends on layered reconstruction, airway function and immediate flap rescue.",
        "retrieval_prompts":["Name the three independent layers in complex nasal reconstruction.","What vessel supplies the PMFF and what mechanical problems threaten it?","When does current evidence justify considering earlier pedicle division?","How do arterial insufficiency and venous congestion look different?","What must be corrected before using adjunctive salvage?"],
        "spacing":"Revisit after nasal reconstruction cases and before facial-plastics oral boards; repeat if stage-count or early-division rules are recalled as absolutes.",
    },
    "source_refs_v223": SOURCE_REFS_V223,
    "evidence_distinction_v223": "Durable textbook principles are three-layer lining/support/cover analysis, supratrochlear pedicle anatomy, staged reconstruction, valve-support preservation and prompt mechanical rescue of vascular compromise. Traditional texts commonly teach division around 3-4 weeks. Current 2024-2025 evidence does not negate those principles: it shows that two- and three-stage pathways are both effective and that selected well-perfused, often lower-complexity/partial-thickness defects may tolerate accelerated division. There is no FDA indication or major society guideline prescribing PMFF stage count or a universal take-down day; newer observational evidence should individualize timing rather than create a new absolute rule.",
    "choices": [],
    "answer": None,
}}

def apply_concept_check_task_alignment_v223(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, spec in COHORT.items():
        q = by.get(qid)
        if q is None:
            missing.append(qid); continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != spec["canonical_topic"] or cid != spec["concept_id"]:
            link_mismatch.append(qid); continue
        q.update(spec)
        q["task_alignment_v223"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
