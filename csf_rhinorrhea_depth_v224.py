"""v22.4 — CSF rhinorrhea depth expansion.

Keeps the existing canonical CSF Rhinorrhea concept and three-stage ladder, but
makes spontaneous versus traumatic/iatrogenic pathways explicit in the deep
curriculum and adds two high-value iatrogenic management cases.
"""
DOMAIN="Rhinology / Allergy / Skull Base"
TOPIC="CSF Rhinorrhea"

DEPTH_APPEND={
"recognize": "\n\nEtiologic split: CSF rhinorrhea should be classified as spontaneous, traumatic, or iatrogenic because recurrence risk and management differ. Spontaneous anterior skull-base leaks commonly occur with meningoencephalocele and a phenotype of chronically elevated intracranial pressure; imaging clues can include an empty or partially empty sella, skull-base thinning, meningoceles, and multiple defects. Iatrogenic leaks may occur during endoscopic sinus or skull-base surgery, especially near the lateral lamella/cribriform plate, ethmoid roof, posterior ethmoid, or sphenoid skull base. Sudden clear fluid, visualization of a skull-base defect, herniating intracranial tissue, or an unexpected deep superior opening during ESS should trigger immediate concern rather than continued powered dissection.",
"localize": "\n\nFor iatrogenic injury, operative localization is anatomy-driven. The anterior ethmoid artery marks an important skull-base/orbital relationship; the lateral lamella is thin and vulnerable, and asymmetry in Keros depth or a low fovea increases risk. Posteriorly, the sphenoid roof, planum, optic nerve, carotid protuberance, and Onodi-cell anatomy must be understood before instrumentation. The exact site and flow characteristics determine whether a small low-flow mucosal/bony defect or a larger high-flow dural defect is present.",
"workup": "\n\nIn a known intraoperative iatrogenic leak, biochemical confirmation is usually unnecessary because the defect is directly observed; the priority is anatomic definition and secure repair. For delayed postoperative clear rhinorrhea, confirm CSF with beta-2 transferrin or beta-trace protein and obtain high-resolution CT with MRI when encephalocele, multiple defects, or soft-tissue characterization is needed. Fever, meningismus, severe headache, neurologic change, or pneumocephalus changes urgency and may require emergency evaluation rather than routine outpatient localization.",
"manage": "\n\nSpontaneous leaks require definitive defect management plus assessment for an underlying intracranial-pressure disorder when appropriate. Traumatic leaks may occasionally close with observation depending on site, timing, and clinical context, but persistent anterior skull-base leakage or meningitis risk requires a definitive plan. Iatrogenic leaks recognized during surgery should be repaired at the same setting when feasible. Routine prophylactic antibiotics solely to prevent meningitis are not a substitute for closure of a persistent leak. Lumbar drainage is not mandatory for every endoscopic repair; it is reserved selectively for situations such as high-flow defects, difficult reconstruction, selected elevated-pressure states, or other specific operative concerns.",
"operate": "\n\nIf CSF is encountered during ESS: stop powered instrumentation and avoid blind suction, cautery, or traction at the defect; maintain orientation; define the bony/dural margins; preserve viable mucosa and reconstructive options; and repair according to size, location, and flow. Small defects may be closed with appropriately supported free grafts, while larger/high-flow defects often require multilayer reconstruction and/or a vascularized flap such as a nasoseptal flap when anatomy and prior surgery permit. Do not enlarge an uncertain superior defect simply to 'see better' until intracranial and orbital boundaries are understood. Postoperatively, counsel on leak precautions, monitor for recurrent rhinorrhea, meningitis, and pneumocephalus, and coordinate management of elevated intracranial pressure in spontaneous disease.",
"teach": "\n\nBoard/chief distinction: spontaneous CSF rhinorrhea is often a leak-plus-pressure problem; iatrogenic CSF rhinorrhea is an anatomy-and-repair problem. In the OR, the correct first response to an unexpected skull-base violation is to stop, localize, and protect—not to keep debriding. A lumbar drain is a selective adjunct, not a universal requirement. A successful spontaneous leak repair is incomplete management if the pressure driver is ignored."
}

def _q(qid,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus):
    return {"id":qid,"domain":DOMAIN,"topic":TOPIC,"learning_stage":stage,
            "stem":stem,"choices":choices,"answer":answer,"explanation":explanation,
            "why_wrong":reasons,"board_pearl":pearl,"curveball":curveball,
            "tier":"Curated learning ladder","mode":"Vignette","focus":focus,
            "ladder_reviewed":True}

VIGNETTES_V224=[
_q("v224_rhi_csf_iat_app","application",
"During anterior ethmoidectomy, the microdebrider suddenly enters a superior defect and clear fluid appears. What is the best immediate response?",
["Continue powered dissection to widen the opening and improve visualization","Stop powered instrumentation, avoid blind suction/traction, re-establish skull-base orientation, define the defect, and prepare an appropriate repair","Pack the nose and ignore the site if bleeding is minimal","Cauterize any tissue protruding through the defect without identifying it"],1,
"An unexpected CSF leak during ESS is an intraoperative skull-base injury until proven otherwise. Continuing powered dissection or blindly manipulating tissue risks enlarging the dural defect, injuring brain or vessels, and converting a repairable problem into a major complication. The surgeon should stop, regain anatomic orientation, characterize the defect and flow, and perform a secure repair.",
["Powered dissection can rapidly enlarge the skull-base injury.","Correct. Stop, localize, protect intracranial structures, then repair according to defect size and flow.","Packing without understanding or repairing the injury leaves persistent CSF leakage and its complications.","Protruding tissue may be dura or brain; blind cautery can cause intracranial injury."],
"Unexpected CSF in ESS is a stop signal, not a cue to keep dissecting.","Which skull-base locations are especially vulnerable when the lateral lamella is deep or asymmetric?","OR_prep"),
_q("v224_rhi_csf_iat_snr","senior_decision",
"A patient has persistent clear rhinorrhea one week after FESS. Beta-2 transferrin is positive and CT shows a small ethmoid-roof defect. There is no meningitis or tension pneumocephalus. What is the best attending-level management principle?",
["Treat indefinitely with antihistamines","Localize the iatrogenic defect and plan definitive endoscopic repair while assessing for complications; use lumbar drainage only selectively rather than routinely","Observe indefinitely because all postoperative leaks close spontaneously","Give long-term antibiotics as definitive therapy"],1,
"A persistent postoperative iatrogenic CSF leak requires a definitive closure strategy because of meningitis and pneumocephalus risk. Endoscopic repair is usually appropriate for an accessible anterior skull-base defect. Lumbar drainage can be helpful in selected circumstances but is not required for every routine repair.",
["Antihistamines do not close a dural defect.","Correct. Persistent iatrogenic leakage is a repair problem, with adjuncts chosen according to flow, pressure, defect, and reconstruction.","Indefinite observation exposes the patient to preventable infectious and intracranial complications.","Antibiotics do not repair the skull-base defect and are not definitive treatment."],
"Persistent postoperative CSF rhinorrhea is not 'post-op drainage'—prove it, map it, and close it.","What findings would make this an emergency rather than a planned repair?","overnight_call")]

def apply_csf_rhinorrhea_depth_v224(data):
    modules=data.DEEP_MODULES_V6.get(DOMAIN,[])
    target=next((m for m in modules if m.get("topic")==TOPIC),None)
    if target is None: raise RuntimeError("v224: canonical CSF Rhinorrhea module not found")
    for key,extra in DEPTH_APPEND.items():
        current=str(target.get(key) or "")
        if extra.strip() not in current: target[key]=current+extra
    cid=data._v6_item_id(DOMAIN,TOPIC)
    existing={q.get("id") for q in data.CLINICAL_CHALLENGES_V119 if q.get("id")}
    added=0
    for q in VIGNETTES_V224:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=cid
        data.CLINICAL_CHALLENGES_V119.append(row); existing.add(row["id"]); added+=1
    return {"module_enriched":True,"added_questions":added,"topic":TOPIC}
