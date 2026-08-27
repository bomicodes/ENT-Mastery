"""v22.7 — Head & Neck Oncology learning-ladder pass 7.

Reviews canonical topics 31-35 from the live inventory: nonfunctional larynx/
chronic aspiration after cancer therapy, surveillance/second primaries,
sinonasal malignancies, tracheal malignancy, and palliative/goals-of-care
head-and-neck oncology.
"""
DOMAIN = "Head & Neck Oncology"


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus="boards"):
    return {"id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
            "stem": stem, "choices": choices, "answer": answer, "explanation": explanation,
            "why_wrong": why_wrong, "board_pearl": pearl, "curveball": curveball,
            "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
            "ladder_reviewed": True}


VIGNETTES_V227 = [
    _q("v227_hn_nfl_fnd", "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy", "foundation",
       "Years after chemoradiation for laryngeal cancer, a disease-free patient has chronic aspiration, recurrent pneumonias, feeding-tube dependence, and a tracheostomy despite maximal rehabilitation. What is the best way to frame the problem?",
       ["The larynx is anatomically present but functionally failed", "This is recurrent cancer by definition", "Aspiration is expected and never requires intervention", "The feeding tube proves swallowing is safe"], 0,
       "Cancer control and organ preservation are not synonymous with preserved function. Severe chronic aspiration, pneumonia, tracheostomy dependence, and inability to maintain oral nutrition can represent a nonfunctional larynx even without recurrent tumor.",
       ["Correct. Functional failure can persist despite an anatomically preserved, disease-free larynx.", "Recurrence must be excluded, but dysfunction after treatment is not itself proof of cancer.", "Repeated pulmonary morbidity can become life-threatening and warrants active management.", "Tube feeding may reduce oral intake but does not necessarily eliminate salivary or reflux-related aspiration."],
       "An organ-preservation success can still become a functional failure.",
       "What objective swallowing and pulmonary findings help determine whether rehabilitation has reached its ceiling?"),
    _q("v227_hn_nfl_app", "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy", "application",
       "A disease-free irradiated patient has recurrent aspiration pneumonia despite diet modification, swallowing therapy, and enteral nutrition. Which next-step framework is most appropriate?",
       ["Continue identical conservative therapy indefinitely", "Reassess aspiration mechanism and goals, then discuss aspiration-prevention surgery when pulmonary morbidity remains unacceptable despite maximal rehabilitation", "Give chronic antibiotics as definitive treatment", "Assume a PEG prevents all aspiration"], 1,
       "When rehabilitation and nutrition strategies fail to control life-threatening aspiration, aspiration-prevention surgery can become appropriate. Options depend on residual speech goals, airway anatomy, tissue quality, prior radiation, and whether total laryngectomy or another separation/closure procedure best matches the patient.",
       ["Persistent recurrent pneumonia suggests the current strategy is inadequate.", "Correct. Escalation is based on pulmonary consequences, failed rehabilitation, anatomy, and patient goals.", "Antibiotics treat infections but not the aspiration mechanism.", "Patients can aspirate secretions or refluxate despite enteral feeding."],
       "The indication for aspiration-prevention surgery is functional harm, not merely an abnormal swallow study.",
       "How do voice goals alter the choice between total laryngectomy and other aspiration-prevention procedures?", "overnight_call"),
    _q("v227_hn_nfl_snr", "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy", "senior_decision",
       "A frail survivor requests total laryngectomy solely to stop aspiration. He has severe pulmonary disease, poor nutrition, prior high-dose radiation, and limited rehabilitation support. What is the best attending-level approach?",
       ["Proceed because aspiration alone makes laryngectomy mandatory", "Balance expected aspiration control against perioperative risk, wound/fistula burden, reconstructive needs, communication outcome, and realistic rehabilitation before recommending surgery", "Refuse surgery because the cancer is cured", "Recommend chronic intubation instead"], 1,
       "Functional laryngectomy can dramatically improve selected patients, but the operation carries substantial risk in irradiated, malnourished, medically frail patients. The decision should integrate pulmonary reserve, nutrition, wound biology, reconstructive strategy, communication rehabilitation, and the patient's priorities.",
       ["A strong indication does not erase operative risk.", "Correct. Senior judgment is proportional: expected functional benefit must outweigh the morbidity of salvage-field surgery.", "Cancer cure does not preclude treatment of severe treatment-related dysfunction.", "Chronic intubation is not a durable aspiration-management strategy."],
       "A functional laryngectomy is still a major salvage-field operation.",
       "What role can vascularized tissue reinforcement play when the pharynx is heavily irradiated?", "OR_prep"),

    _q("v227_hn_surv_fnd", "Head & Neck Cancer Surveillance / Second Primaries", "foundation",
       "After curative treatment for head-and-neck SCC, what are the two major purposes of long-term surveillance?",
       ["Detect recurrence and new primary malignancies while also monitoring treatment-related dysfunction", "Only repeat imaging forever", "Only monitor body weight", "Stop follow-up once the first post-treatment scan is negative"], 0,
       "Surveillance aims to detect recurrence or second primaries at a stage where intervention may matter and to identify survivorship problems such as dysphagia, hypothyroidism, dental disease, fibrosis, and tobacco/alcohol-related risk.",
       ["Correct. Surveillance is both oncologic and functional.", "Imaging is only one component and is not required indefinitely at the same intensity for every patient.", "Weight is useful but insufficient by itself.", "Risk does not disappear after one negative scan."],
       "Follow-up after HNSCC is not just recurrence hunting; it is survivorship care plus second-primary vigilance.",
       "Which smoking-related second primary sites deserve particular attention?"),
    _q("v227_hn_surv_app", "Head & Neck Cancer Surveillance / Second Primaries", "application",
       "A treated oral cavity SCC patient develops new unilateral otalgia, progressive dysphagia, and weight loss two years after therapy despite a previously reassuring surveillance visit. What is the best next step?",
       ["Wait for the next routine appointment", "Perform prompt symptom-directed examination and appropriate imaging/biopsy because new focal symptoms override the routine surveillance calendar", "Treat empirically with reflux medication for six months", "Assume late radiation toxicity without excluding recurrence"], 1,
       "Surveillance intervals do not supersede new concerning symptoms. Progressive pain, otalgia, dysphagia, bleeding, mass, cranial neuropathy, or weight loss should trigger expedited evaluation for recurrent or second primary disease.",
       ["Delay can sacrifice salvageability.", "Correct. New red flags reset the timeline and require targeted evaluation.", "Empiric treatment should not postpone cancer assessment when symptoms are concerning.", "Late toxicity is common but recurrence must be excluded first."],
       "Symptoms beat the schedule.",
       "When is PET/CT most useful after definitive chemoradiation, and when can early imaging be misleading?"),
    _q("v227_hn_surv_snr", "Head & Neck Cancer Surveillance / Second Primaries", "senior_decision",
       "A five-year disease-free survivor asks whether intensive cross-sectional imaging every three months should continue indefinitely. What is the best senior-level counseling principle?",
       ["Continue the same imaging frequency for life", "Tailor surveillance intensity to time from treatment, recurrence risk, symptoms, exam accessibility, smoking/second-primary risk, and whether detecting asymptomatic disease would change management", "Stop all clinical follow-up", "Replace examination with tumor markers alone"], 1,
       "Most recurrences occur earlier after treatment, while second-primary and late-toxicity risks can persist. Surveillance should become risk-adapted rather than mechanically maintaining the same scan frequency forever.",
       ["Indefinite high-frequency imaging can add radiation, incidental findings, cost, and anxiety without proven benefit in every survivor.", "Correct. Surveillance should remain clinically purposeful and risk-adapted.", "Long-term survivorship needs remain even after recurrence risk falls.", "No validated serum marker replaces examination and symptom-directed assessment for routine HNSCC surveillance."],
       "A surveillance test is useful only if its result can change care.",
       "How does ongoing tobacco use change counseling about second-primary prevention and screening?"),

    _q("v227_hn_sinonasal_fnd", "Sinonasal Malignancies", "foundation",
       "An adult has progressive unilateral epistaxis, nasal obstruction, facial numbness, and a unilateral sinonasal mass with bony destruction. What is the best oncologic interpretation?",
       ["Treat as routine inflammatory polyposis", "Assume malignancy is possible and obtain extent-defining imaging plus tissue diagnosis in a controlled fashion", "Begin allergy shots without imaging", "Perform blind office avulsion"], 1,
       "Unilateral destructive sinonasal disease with bleeding, cranial neuropathy, or facial numbness is concerning for malignancy. CT defines bone and MRI is important for orbit, skull base, dura, perineural spread, and intracranial relationships.",
       ["Inflammatory polyps are typically not associated with aggressive bony destruction or cranial neuropathy.", "Correct. Diagnosis and anatomic mapping must precede definitive treatment.", "Allergy treatment does not address a destructive mass.", "Blind removal can cause hemorrhage and compromise oncologic planning."],
       "Unilateral destructive sinonasal disease is a cancer workup until proved otherwise.",
       "Which symptoms suggest orbital, skull-base, or named-nerve involvement?"),
    _q("v227_hn_sinonasal_app", "Sinonasal Malignancies", "application",
       "Biopsy shows sinonasal SCC abutting the orbit and anterior skull base. What should guide treatment planning?",
       ["Primary-site histology and exact orbital/skull-base extent, resectability, margin feasibility, nodal risk, and the expected morbidity of surgery versus radiation-based therapy", "Tumor size alone", "Whether the patient prefers antibiotics", "Routine total laryngectomy"], 0,
       "Sinonasal malignancies are anatomically complex and histologically diverse. Treatment requires multidisciplinary integration of pathology, orbit/skull-base involvement, ability to obtain margins, neck risk, reconstruction, radiation, and systemic therapy when indicated.",
       ["Correct. Both biology and three-dimensional extent determine treatment.", "Size alone does not capture orbit, dura, carotid, cranial nerve, or histologic risk.", "Antibiotics do not treat sinonasal carcinoma.", "Laryngectomy does not address a sinonasal primary."],
       "For sinonasal cancer, the imaging map is part of the operation.",
       "What findings can permit orbital preservation despite tumor near the orbit, and what findings threaten it?", "OR_prep"),
    _q("v227_hn_sinonasal_snr", "Sinonasal Malignancies", "senior_decision",
       "A sinonasal carcinoma reaches the skull base with suspected dural involvement but no distant disease. What is the best attending-level principle?",
       ["Dural contact always makes disease incurable", "Determine whether an en bloc or endoscopic craniofacial oncologic resection can achieve safe margins with skull-base reconstruction, and compare that morbidity with nonsurgical options in a multidisciplinary skull-base setting", "Perform piecemeal debulking without margin planning", "Ignore intracranial anatomy"], 1,
       "Selected skull-base-involving sinonasal cancers remain potentially curable. Resectability depends on the structures involved, ability to achieve meaningful margins, carotid/cavernous sinus/brain involvement, histology, and reconstructive feasibility—not simply the presence of dural contact.",
       ["Some dural involvement is resectable with appropriate skull-base expertise.", "Correct. Curative planning requires coordinated oncologic resection and reconstruction.", "Unplanned debulking can compromise margin assessment and definitive therapy.", "Intracranial relationships are central to safety and resectability."],
       "Skull-base extension changes the team and the operation; it does not automatically eliminate curative intent.",
       "Which cavernous-sinus or carotid findings most strongly limit surgical options?", "OR_prep"),

    _q("v227_hn_trachca_fnd", "Tracheal Malignancy", "foundation",
       "A patient has progressive dyspnea and stridor for months and is repeatedly treated for asthma. CT finally shows a focal intraluminal tracheal mass. What is the key diagnostic lesson?",
       ["Fixed central-airway obstruction can mimic asthma and requires anatomic airway evaluation", "All stridor is asthma", "Tracheal tumors are always benign", "Spirometry eliminates the need for imaging"], 0,
       "Primary tracheal malignancies are uncommon but can present insidiously with wheeze, dyspnea, cough, hemoptysis, or stridor. Persistent fixed-airway symptoms should trigger bronchoscopy and cross-sectional imaging rather than repeated empiric asthma treatment.",
       ["Correct. The symptom pattern should prompt localization to the central airway.", "Stridor is an upper/central-airway warning sign rather than typical lower-airway wheeze.", "Tracheal tumors may be malignant, including SCC and adenoid cystic carcinoma.", "Flow-volume loops can suggest fixed obstruction but do not replace anatomic evaluation."],
       "When 'asthma' does not behave like asthma, localize the airway.",
       "How can adenoid cystic carcinoma differ from SCC in submucosal and longitudinal spread?"),
    _q("v227_hn_trachca_app", "Tracheal Malignancy", "application",
       "A resectable primary tracheal malignancy is limited to a short segment with no distant disease. What operative principle is most important?",
       ["Resect as much trachea as possible regardless of tension", "Aim for oncologic resection with a tension-free primary anastomosis, planning airway control and release maneuvers according to segment length and location", "Perform tracheostomy through the tumor before planning", "Ignore the recurrent laryngeal nerves"], 1,
       "Curative tracheal surgery requires both adequate oncologic margins and a viable low-tension anastomosis. Resectable length, cricoid/innominate relationships, prior treatment, airway strategy, and release maneuvers must be planned before incision.",
       ["Excessive tension is a major cause of anastomotic failure.", "Correct. Margin goals and anastomotic mechanics must be solved together.", "A tumor-violating tracheostomy may complicate definitive resection and should not be routine when another airway plan is feasible.", "Neural injury can profoundly affect postoperative airway and swallowing."],
       "Tracheal cancer surgery is an oncologic problem constrained by anastomotic mechanics.",
       "How does tumor proximity to the cricoid change resection and airway planning?", "OR_prep"),
    _q("v227_hn_trachca_snr", "Tracheal Malignancy", "senior_decision",
       "A long-segment tracheal tumor is technically removable only with an anastomosis under prohibitive tension. What is the best senior-level decision?",
       ["Proceed because negative margins are the only endpoint", "Do not force an unsafe reconstruction; reassess resectability and multidisciplinary nonsurgical or palliative options", "Create the anastomosis under tension and hope it heals", "Ignore prior radiation"], 1,
       "Catastrophic anastomotic dehiscence can be fatal. Technical resectability must include the ability to reconstruct the airway safely; when adequate margins require an unsafe length of resection, alternative oncologic strategies are appropriate.",
       ["Oncologic clearance without a survivable reconstruction is not a successful operation.", "Correct. Safe reconstructability is part of resectability.", "High-tension anastomosis risks dehiscence, mediastinitis, hemorrhage, and death.", "Prior radiation can worsen healing and materially affect candidacy."],
       "Resectability ends where safe reconstruction ends.",
       "What postoperative findings suggest early anastomotic compromise?", "postoperative_call"),

    _q("v227_hn_goc_fnd", "Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer", "foundation",
       "Which statement best describes palliative care in advanced head-and-neck cancer?",
       ["It can be integrated alongside cancer-directed therapy to address symptoms, communication, values, and decision-making", "It is only for the final hours of life", "It means all ENT procedures stop", "It is the same as hospice"], 0,
       "Palliative care focuses on symptom burden, quality of life, communication, and goal-concordant decisions and can be introduced at any stage of serious illness. Hospice is a specific end-of-life care model and is not synonymous with palliative care.",
       ["Correct. Palliative care can accompany active oncologic treatment.", "Late-only referral misses opportunities to improve symptoms and decision quality.", "Airway, bleeding, pain, nutrition, and other ENT interventions may remain appropriate when they support the patient's goals.", "Hospice is one form of end-of-life care, whereas palliative care is broader."],
       "Palliation is an active treatment goal, not absence of treatment.",
       "Which symptoms most commonly require urgent ENT involvement even when cure is not possible?"),
    _q("v227_hn_goc_app", "Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer", "application",
       "A patient with incurable recurrent HNSCC has episodic tumor bleeding, severe pain, dysphagia, and a threatened airway. What is the best management framework?",
       ["Discuss goals while actively treating reversible symptom crises with options such as airway planning, hemostatic intervention, palliative radiation, analgesia, and nutrition decisions that match the patient's priorities", "Avoid ENT involvement because the disease is incurable", "Perform the most extensive surgery possible regardless of goals", "Treat pain only after all oncologic options are exhausted"], 0,
       "Incurable disease can still generate urgent, treatable symptoms. Palliative head-and-neck care often requires coordinated ENT, radiation oncology, medical oncology, pain/palliative, nutrition, and hospice expertise to reduce suffering without imposing disproportionate morbidity.",
       ["Correct. Symptom-directed interventions remain active care.", "Airway or hemorrhage crises may require immediate ENT expertise despite noncurative intent.", "A morbid operation may be inappropriate when it does not support the patient's goals or expected benefit.", "Pain control should occur concurrently with oncologic care."],
       "Noncurative does not mean noninterventional; intervene when the intervention serves the patient's goal.",
       "How can palliative radiation help bleeding or painful tumor burden?", "overnight_call"),
    _q("v227_hn_goc_snr", "Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer", "senior_decision",
       "A patient with terminal recurrent oral cavity cancer has a sentinel bleed from an exposed carotid and has chosen comfort-focused care with no ICU or major invasive procedures. What is the best attending-level response?",
       ["Ignore the bleed because treatment is comfort-focused", "Honor the stated goals while making an explicit catastrophic-hemorrhage plan, controlling distress, preparing rapid comfort medications and family/staff guidance, and avoiding unwanted escalation", "Override the patient and mandate major surgery", "Wait to discuss the possibility of fatal bleeding until it occurs"], 1,
       "Goals-of-care planning is most valuable before predictable crises. When catastrophic hemorrhage is possible and invasive rescue is not desired, the team should prepare the patient, family, nursing staff, and medication plan so care remains rapid, calm, and goal-concordant.",
       ["Comfort-focused care still requires active anticipatory symptom management.", "Correct. Preparation prevents a foreseeable crisis from becoming chaotic and misaligned with the patient's wishes.", "Capacity and informed patient preferences should guide treatment limits.", "Delayed discussion deprives the patient and family of preparation and choice."],
       "A do-not-escalate decision requires more planning, not less.",
       "How would management differ if the same patient instead wanted every potentially life-prolonging intervention?", "overnight_call"),
]


def apply_learning_ladders_v227(challenges, item_id_fn):
    existing = {str(q.get("id")) for q in challenges if q.get("id")}
    added = 0
    for q in VIGNETTES_V227:
        row = dict(q)
        row["concept_id"] = item_id_fn(DOMAIN, row["topic"])
        if not row["concept_id"]:
            raise RuntimeError("v227 orphan: " + row["topic"])
        if row["id"] not in existing:
            challenges.append(row)
            existing.add(row["id"])
            added += 1
    return {"added": added, "reviewed_topics": 5}
