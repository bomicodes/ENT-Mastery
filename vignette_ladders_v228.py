"""v22.8 — Head & Neck Oncology learning-ladder pass 8.

Reviews canonical topics 36-40: radiation principles, systemic-therapy foundations,
free-flap monitoring/salvage, open partial laryngectomy, and transoral laser
microsurgery for laryngeal cancer.
"""
DOMAIN="Head & Neck Oncology"

def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":why_wrong,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder","mode":"Vignette",
            "focus":focus,"ladder_reviewed":True}

VIGNETTES_V228=[
_q("v228_hn_rt_fnd","Radiation Therapy Principles for Head & Neck Surgeons","foundation",
"A surgeon is counseling a patient with head-and-neck SCC about definitive radiation. Which concept best explains why dose is divided into daily fractions rather than delivered all at once?",
["Fractionation exploits differences in repair and repopulation between tumor and normal tissues while allowing a curative cumulative dose","Fractionation eliminates all late toxicity","Radiation affects only malignant cells","Fractionation makes anatomy irrelevant"],0,
"Fractionation balances tumor control against normal-tissue tolerance by exploiting radiobiologic differences in repair, reassortment, repopulation, and reoxygenation. Dose, fraction size, overall treatment time, and tissue volume all matter.",
["Correct. Fractionation is a therapeutic-ratio strategy.","Late toxicity remains possible and is strongly influenced by dose and tissue volume.","Normal tissues are also irradiated and can develop acute and late injury.","Target definition and organs-at-risk anatomy are central to planning."],
"Radiation is a dose-to-volume treatment: anatomy and biology both matter.","Why can unplanned treatment breaks compromise tumor control?"),
_q("v228_hn_rt_app","Radiation Therapy Principles for Head & Neck Surgeons","application",
"A postoperative oral cavity SCC patient has a positive margin and extranodal extension. What should the surgeon understand about the adjuvant radiation plan?",
["Only the visible surgical bed matters","Risk-adapted postoperative fields must cover the primary bed and appropriate nodal pathways, with dose escalation to highest-risk regions and concurrent systemic therapy when indicated","The neck is never irradiated after dissection","Radiation should be delayed until recurrence"],1,
"Postoperative radiation is designed around pathologic risk and surgical anatomy. High-risk beds, involved nodal levels, and at-risk drainage pathways receive tailored dose; positive margins and extranodal extension often justify concurrent systemic intensification in fit patients.",
["Microscopic-risk regions extend beyond visible scar or cavity.","Correct. Surgeons should understand how pathology drives target volumes, dose, and systemic intensification.","Dissection does not eliminate all microscopic nodal risk.","Adjuvant therapy is intended to reduce recurrence before it becomes clinically evident."],
"The pathology report is part of the radiation treatment plan.","Which operative clips, flap geometry, or altered anatomy can help or hinder postoperative target definition?"),
_q("v228_hn_rt_snr","Radiation Therapy Principles for Head & Neck Surgeons","senior_decision",
"A previously irradiated patient develops an isolated recurrence near the carotid and spinal cord. Re-irradiation is being considered. What is the best senior-level principle?",
["Prior radiation dose is irrelevant","Reconstruct the prior dose distribution and weigh cumulative organ-at-risk tolerance, recurrence geometry, interval, expected control, and catastrophic toxicity against surgery or systemic options","Give the original full course again without reviewing records","Re-irradiation is never possible"],1,
"Re-irradiation can be useful in selected patients but carries major risks such as soft-tissue necrosis, dysphagia, neurologic injury, and carotid blowout. Prior dose maps, interval, target size, adjacent critical structures, and alternative curative options are essential.",
["Cumulative dose strongly determines normal-tissue risk.","Correct. Re-irradiation is a highly selected therapeutic-ratio decision.","Ignoring prior dose can expose critical structures to unsafe cumulative treatment.","Selected patients can benefit from modern re-irradiation approaches."],
"Re-irradiation is not 'more radiation'; it is cumulative-dose risk engineering.","Which clinical features increase carotid blowout risk after re-irradiation?"),

_q("v228_hn_sys_fnd","Systemic Therapy Foundations in Head & Neck Cancer","foundation",
"What is the major role of concurrent cisplatin during definitive radiation for appropriately selected locally advanced HNSCC?",
["It replaces radiation","It acts as a radiosensitizing systemic agent that improves locoregional treatment effectiveness in appropriate patients","It prevents every distant metastasis","It is used only for pain control"],1,
"Concurrent cisplatin is a standard radiosensitizing systemic therapy in many definitive and postoperative high-risk HNSCC settings. Its benefit must be balanced against renal, auditory, neurologic, marrow, and performance-status toxicity.",
["Radiation remains the local-treatment backbone.","Correct. Cisplatin intensifies radiation rather than substituting for it.","Distant failure can still occur.","Its role is oncologic treatment, not merely analgesia."],
"Before recommending cisplatin, know both the indication and the patient's ability to tolerate it.","Which baseline findings make standard cisplatin particularly hazardous?"),
_q("v228_hn_sys_app","Systemic Therapy Foundations in Head & Neck Cancer","application",
"A patient with recurrent/metastatic HNSCC is not a candidate for curative local therapy. What should guide first-line systemic treatment selection?",
["Use the same regimen for everyone","Disease burden/tempo, symptoms, performance status, prior therapy, PD-L1-related biomarkers where applicable, comorbidities, and whether rapid cytoreduction is needed","Tumor side alone","Whether the primary was surgically exposed"],1,
"Modern recurrent/metastatic therapy may include checkpoint inhibition alone or combined with chemotherapy depending on biomarker context, symptoms, disease tempo, prior treatment, and need for rapid response. Treatment must be individualized rather than algorithmically detached from the patient.",
["Different disease and patient profiles favor different regimens.","Correct. Biomarkers and clinical urgency both matter.","Laterality does not determine systemic regimen.","Surgical exposure is irrelevant to systemic-treatment selection."],
"Systemic therapy choices are driven by biology plus urgency.","Why might bulky symptomatic disease favor a regimen with faster expected cytoreduction?"),
_q("v228_hn_sys_snr","Systemic Therapy Foundations in Head & Neck Cancer","senior_decision",
"A patient with incurable metastatic HNSCC has declining performance status and repeated hospitalizations from treatment toxicity. What is the best attending-level principle?",
["Escalate chemotherapy because more treatment is always better","Reassess whether further systemic therapy offers meaningful benefit relative to toxicity and integrate symptom-focused and goals-of-care planning","Ignore functional decline","Continue the same regimen until death regardless of response"],1,
"Systemic treatment should be continued only while expected oncologic benefit remains proportionate to toxicity and the patient's goals. Performance decline, organ dysfunction, refractory progression, or repeated severe toxicity should trigger reconsideration of treatment intensity.",
["Treatment burden can exceed likely benefit.","Correct. Oncology decisions must remain proportional and goal-concordant.","Functional decline is a major prognostic and treatment-tolerance signal.","Automatic continuation can worsen suffering without meaningful benefit."],
"Knowing when not to intensify treatment is part of systemic-therapy competence.","Which clinical changes should trigger an urgent goals-of-care reassessment?"),

_q("v228_hn_flap_fnd","Free-Flap Monitoring / Compromise / Salvage","foundation",
"In the first postoperative day after head-and-neck free-flap reconstruction, why is frequent flap monitoring important?",
["Microvascular thrombosis can evolve rapidly, and salvage probability falls as ischemia time increases","Flaps never fail after the first hour","Monitoring is only cosmetic","Venous and arterial compromise present identically in every flap"],0,
"Early recognition of vascular compromise is essential because timely operative take-back can salvage many threatened flaps. Clinical appearance, Doppler signals, capillary refill, turgor, temperature, bleeding characteristics, and implantable monitoring are interpreted together.",
["Correct. Time to recognition and re-exploration is a key determinant of salvage.","Compromise can occur hours or days after transfer.","Monitoring protects reconstructive viability and downstream airway, swallowing, wound, and vessel coverage.","Venous congestion and arterial insufficiency often have different clinical patterns."],
"A threatened free flap is a time-sensitive vascular emergency.","How do venous congestion and arterial insufficiency differ on examination?"),
_q("v228_hn_flap_app","Free-Flap Monitoring / Compromise / Salvage","application",
"Six hours after oral-cavity free-flap reconstruction, the flap becomes dusky and swollen with brisk dark bleeding on pinprick while the venous Doppler signal is lost. What is the best next step?",
["Observe until morning","Treat as probable venous compromise and proceed urgently toward exploration after rapid bedside/system troubleshooting","Apply topical steroid only","Remove the flap at bedside"],1,
"Dusky congestion, swelling, dark brisk bleeding, and loss of venous signal strongly suggest venous outflow failure. After rapid confirmation that monitoring equipment is functioning and reversible external compression is excluded, urgent take-back is generally indicated.",
["Delay allows progressive thrombosis and ischemic injury.","Correct. Suspected vascular compromise should trigger rapid salvage workflow.","Steroids do not correct a thrombosed or kinked venous pedicle.","Definitive evaluation and revision require controlled operative exploration."],
"Do not 'watch' a convincing threatened flap while the salvage window closes.","What bedside findings can suggest a compressive hematoma rather than intrinsic anastomotic thrombosis?","postoperative_call"),
_q("v228_hn_flap_snr","Free-Flap Monitoring / Compromise / Salvage","senior_decision",
"At take-back, a free flap has venous thrombosis with a technically correctable pedicle problem but several hours of congestion. What should guide the salvage attempt?",
["Abandon every thrombosed flap immediately","Correct the mechanical/anastomotic cause, restore flow, assess tissue viability, and use thrombectomy/revision or other salvage maneuvers as appropriate while minimizing further ischemia","Ignore the pedicle and revise the skin closure","Wait for spontaneous recanalization"],1,
"Successful salvage requires finding and correcting the cause—kink, compression, twist, anastomotic thrombosis, recipient-vessel problem—then rapidly restoring perfusion and judging whether tissue remains viable. The exact technique depends on the intraoperative problem.",
["Many early compromised flaps are salvageable if treated promptly.","Correct. Salvage is cause-directed and time-sensitive.","Skin closure does not fix microvascular outflow failure.","Spontaneous recovery is not a safe strategy for proven thrombosis."],
"At take-back, diagnose the mechanism before declaring the reconstruction lost.","When does the ischemia/congestion burden make a second flap or alternate reconstruction more appropriate?","OR_prep"),

_q("v228_hn_cons_fnd","Open Partial / Conservation Laryngectomy","foundation",
"What is the central oncologic requirement for an open partial/conservation laryngectomy?",
["The tumor must be resectable with adequate margins while preserving enough functional laryngeal framework—particularly a usable cricoarytenoid unit—for airway and swallowing rehabilitation","Any laryngeal tumor can be treated this way","Voice preservation overrides aspiration risk","Fixed extensive extralaryngeal disease is ideal"],0,
"Conservation laryngeal surgery is appropriate only when oncologic clearance and functional preservation are both realistic. Tumor extent, cartilage/subglottic spread, arytenoid/cricoarytenoid involvement, pulmonary reserve, and rehabilitation potential are central.",
["Correct. Cure and a functional residual larynx are both required.","Advanced extent can make conservation unsafe or nonfunctional.","Severe chronic aspiration is not a successful preservation outcome.","Extensive extralaryngeal spread usually pushes treatment away from partial laryngeal surgery."],
"Conservation surgery preserves a functional unit, not merely a piece of larynx.","Which cricoarytenoid findings are most important for candidacy?"),
_q("v228_hn_cons_app","Open Partial / Conservation Laryngectomy","application",
"A patient has a localized laryngeal SCC technically amenable to conservation surgery but severe COPD, weak cough, and baseline aspiration. What is the best treatment principle?",
["Proceed because tumor anatomy is the only criterion","Recognize that pulmonary reserve and swallowing function may make partial laryngectomy a poor functional choice despite oncologic resectability","Ignore aspiration because it always resolves","Perform bilateral neck dissection instead of treating the primary"],1,
"Open partial laryngectomy requires intensive swallowing and airway rehabilitation. Poor pulmonary reserve, weak cough, and baseline aspiration can convert an anatomically feasible operation into an unsafe functional outcome.",
["Functional candidacy matters alongside tumor extent.","Correct. A preserved larynx must be safe enough to use.","Aspiration may persist and can be dangerous in a patient with limited pulmonary reserve.","Neck surgery does not solve the primary-site functional problem."],
"Partial laryngectomy candidacy is a tumor-plus-patient decision.","How would prolonged postoperative aspiration change rehabilitation and rescue planning?"),
_q("v228_hn_cons_snr","Open Partial / Conservation Laryngectomy","senior_decision",
"During planned conservation laryngectomy, the true tumor extent would require sacrificing the only functional cricoarytenoid unit to obtain a clear margin. What is the best attending-level decision?",
["Accept a positive margin to preserve anatomy","Abandon the conservation goal and convert to an oncologically appropriate alternative rather than leave a nonfunctional or margin-positive larynx","Leave gross disease and close","Remove less tumor than planned"],1,
"Conservation is conditional on adequate margins and preservation of the functional structures required for rehabilitation. If either premise fails intraoperatively, forcing the original plan defeats both oncologic and functional goals.",
["Positive margins compromise disease control.","Correct. The operation should change when the fundamental candidacy assumptions change.","Gross residual disease is not acceptable curative surgery.","Undertreatment sacrifices oncologic control."],
"The right intraoperative pivot is part of conservation surgery.","What preoperative imaging/endoscopic findings help anticipate this conversion risk?","OR_prep"),

_q("v228_hn_tlm_fnd","Transoral Laser Microsurgery for Laryngeal Cancer","foundation",
"What is the most important prerequisite for transoral laser microsurgery of a laryngeal cancer?",
["Complete safe endoscopic exposure of the tumor sufficient to define and resect its oncologic extent","A mandatory external neck incision","Routine tracheostomy for every lesion","Ignoring anterior commissure involvement"],0,
"TLM depends on adequate transoral exposure. If the tumor cannot be safely visualized and accessed with appropriate deep and peripheral margin control, another treatment approach is preferable.",
["Correct. Exposure is an oncologic requirement, not merely a technical convenience.","TLM is specifically a transoral approach.","Tracheostomy is not universally required.","Anterior commissure and cartilage relationships can materially affect margin planning."],
"If you cannot expose it, you cannot responsibly laser-resect it.","Which dental, mandibular, cervical, and tumor factors predict difficult exposure?"),
_q("v228_hn_tlm_app","Transoral Laser Microsurgery for Laryngeal Cancer","application",
"During TLM, the surgeon reaches a deep margin near cartilage and cannot confidently distinguish tumor from normal tissue. What is the best principle?",
["Continue blindly to preserve the transoral plan","Maintain oncologic orientation, obtain directed margin assessment as appropriate, and change the operative strategy if a safe clear deep margin cannot be achieved","Ignore deep margins because laser sterilizes tumor","Stop documenting specimen orientation"],1,
"Laser resection does not eliminate the need for oncologic margin discipline. Specimen orientation, depth assessment, and willingness to convert or choose another modality are important when exposure or deep extension prevents reliable clearance.",
["Blind extension risks inadequate or unsafe resection.","Correct. TLM remains an oncologic resection, not simply a debulking technique.","Laser energy does not make an involved margin acceptable.","Orientation is essential for pathology and subsequent decisions."],
"The laser changes the instrument, not the cancer principles.","How can piecemeal TLM specimens still be oriented for meaningful pathology?","OR_prep"),
_q("v228_hn_tlm_snr","Transoral Laser Microsurgery for Laryngeal Cancer","senior_decision",
"A patient with an early glottic cancer could receive either TLM or radiation with high expected control. What should guide modality selection?",
["Use TLM automatically","Integrate exposure, tumor extent, expected voice/swallow outcome, prior treatment, anesthesia/surgical risk, surveillance/re-treatment options, patient preference, and local expertise","Use radiation automatically","Choose whichever can be scheduled first"],1,
"For appropriately selected early laryngeal cancer, both TLM and radiation can provide excellent control. The optimal choice is individualized by anatomy, function, logistics, salvage implications, and informed patient values rather than a universal hierarchy.",
["TLM is not superior for every patient or lesion.","Correct. Equivalent oncologic options should be compared on functional and patient-specific tradeoffs.","Radiation is not universally superior either.","Scheduling convenience should not dominate a durable cancer decision."],
"When two modalities cure well, the decision becomes anatomy, function, salvage, and preference.","How does prior neck radiation alter this choice?"),
]

def apply_learning_ladders_v228(challenges,item_id_fn):
    existing={str(q.get("id")) for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V228:
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v228 orphan: "+row["topic"])
        if row["id"] not in existing:
            challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
