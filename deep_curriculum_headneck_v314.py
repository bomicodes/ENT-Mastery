"""v31.4 — source-grounded H&N goals-of-care vs palliative intervention rebuild.

Keeps two highly overlapping Concept Hub cards clinically distinct:
1) goals-of-care = communication, prognosis, decision capacity/surrogacy and treatment alignment;
2) palliative decision-making = symptom-directed ENT/oncologic interventions when cure is not the goal.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


PALLIATIVE_HN_REBUILD_V314 = {
    "palliative goals of care decision making in head neck cancer": {
        "recognize": (
            "This card owns GOAL-CONCORDANT DECISION MAKING, not a list of salvage procedures. Palliative care can and should occur concurrently with disease-directed treatment; it is not synonymous with hospice or imminent death. Trigger structured goals-of-care work when disease is incurable or recurrent, treatment burden is rising, symptoms are uncontrolled, function/communication are threatened, or the patient faces a preference-sensitive choice such as morbid salvage surgery versus nonoperative care. Start by identifying what the patient understands, what outcomes matter most, and which tradeoffs are unacceptable."
        ),
        "localize": (
            "Localize the DECISION before recommending an intervention: Is the immediate problem prognosis/values, uncontrolled symptoms, a threatened airway, bleeding, nutrition, communication, or a potentially curable recurrence? Head-and-neck choices are unusually preference-sensitive because survival may trade against speech, swallowing, appearance, independence, and caregiver burden. Separate 'Can we technically do it?' from 'Would the expected outcome meet this patient's goals?' Capacity is decision-specific; if capacity is absent, identify the legally appropriate surrogate and use substituted judgment when possible, then best-interest reasoning when preferences are unknown."
        ),
        "workup": (
            "Use a reproducible conversation framework: assess illness understanding -> give a clear prognosis in ranges/conditional terms -> elicit values and functional priorities -> define the decision and realistic options -> make a recommendation that explicitly links the option to those values -> document the plan and revisit it as disease changes. Screen physical, psychological, social and spiritual distress and caregiver needs. Clarify code status only after the broader goals discussion; a DNR order is not a complete care plan and does not automatically prohibit surgery, transfusion, antibiotics, radiation, tracheostomy, or other goal-concordant treatments."
        ),
        "manage": (
            "Integrate specialist palliative care EARLY for advanced cancer and unresolved symptom/QOL concerns while oncology treatment continues. Establish a shared plan for anticipated crises—airway compromise, hemorrhage, aspiration, dehydration, pain—and identify who will make decisions if the patient loses capacity. Hospice is appropriate when the care goal and eligibility align with comfort-focused end-of-life care, but referral to palliative care should not wait for hospice eligibility. Reassess goals after major restaging, hospitalization, functional decline, treatment toxicity, or a new salvage option because preferences and acceptable burdens can change."
        ),
        "operate": (
            "The operative question here is WHETHER an operation serves the patient's goals. Before a high-morbidity salvage laryngectomy, composite resection, free flap, feeding access, or tracheostomy, state the best-case, worst-case and most likely outcomes in functional as well as oncologic terms. Discuss likelihood of prolonged hospitalization, nonoral feeding, permanent airway/voice change, wound complications and discharge destination when relevant. A procedure can be appropriate despite noncurative disease if it meaningfully advances the patient's stated priorities; conversely, technical resectability alone does not create an obligation to operate."
        ),
        "teach": (
            "Chief/boards frame: GOALS-OF-CARE asks, 'What outcome is this patient trying to achieve, what burdens are acceptable, and which medically reasonable option best matches those values?' Palliative care is concurrent care; hospice is a later eligibility/goal construct. Capacity is decision-specific. DNR is not 'do not treat.' In head and neck cancer, explicitly discuss speech, swallow, airway, appearance, independence and caregiver burden—not survival alone. Once the goal is established, move to the separate PALLIATIVE DECISION-MAKING card for symptom-directed interventions."
        ),
        "tags": ["goals of care", "shared decision making", "advanced head neck cancer", "capacity", "surrogate", "prognosis", "palliative care", "hospice", "DNR", "functional outcomes"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — advanced/recurrent head and neck cancer, treatment morbidity and supportive care",
            "K.J. Lee's Essential Otolaryngology, 12e — head and neck oncology treatment selection, morbidity and advanced disease",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — head and neck oncology management and treatment complications",
            "Sanders et al., ASCO Guideline Update: Palliative Care for Patients With Cancer, J Clin Oncol 2024"
        ],
    },
    "palliative decision making in head and neck cancer": {
        "recognize": (
            "This card owns SYMPTOM-DIRECTED H&N INTERVENTION after the therapeutic goal has been defined. Common high-stakes palliative problems are pain, dysphagia/aspiration, inability to maintain nutrition or hydration, dyspnea/airway obstruction, bleeding, malodor/fungating tumor, secretion burden, communication loss and distress. 'Palliative' describes intent, not therapeutic passivity: radiation, systemic therapy, embolization, tracheostomy, gastrostomy, debridement or occasionally resection may be appropriate when expected symptom benefit outweighs burden."
        ),
        "localize": (
            "Localize the dominant symptom to a reversible target. Airway compromise may arise from tumor bulk, edema, bilateral vocal-fold dysfunction or secretions; dysphagia may reflect obstruction, neuromuscular dysfunction, pain or treatment fibrosis; bleeding may be mucosal oozing, tumor-vessel erosion or sentinel hemorrhage from a threatened carotid. Distinguish chronic symptom palliation from emergencies: stridor/impending obstruction and sentinel or major hemorrhage require immediate airway/bleeding planning before a routine outpatient palliative algorithm."
        ),
        "workup": (
            "Define the symptom, trajectory, performance status, prognosis, prior surgery/radiation/systemic therapy, anatomy on current imaging, wound status and the patient's stated priorities. For bleeding, identify whether there is a focal endovascular/surgical target and consider carotid blowout risk; for airway symptoms, use flexible laryngoscopy when safe and determine whether intubation or tracheostomy would actually achieve the agreed goal; for dysphagia/nutrition, distinguish temporary treatment support from long-term tube dependence and evaluate aspiration when it will change management. Avoid burdensome testing that cannot alter a goal-concordant plan."
        ),
        "manage": (
            "Match intervention intensity to expected benefit and time-to-benefit. Use multimodal analgesia and specialist symptom management; consider palliative radiation for painful, bleeding or obstructive locoregional disease when feasible; systemic therapy can palliate disease burden in selected patients but carries toxicity and delayed benefit. Use enteral access when it supports the patient's goals rather than as an automatic response to weight loss. Treat infection, odor and wound exudate pragmatically. For catastrophic hemorrhage risk, create an anticipatory plan with patient/family and the multidisciplinary team, including emergency versus comfort-focused responses consistent with goals."
        ),
        "operate": (
            "Palliative procedures should solve a SPECIFIC problem with acceptable burden. Tracheostomy can relieve upper-airway obstruction but may worsen secretion/care burden and does not treat the cancer; gastrostomy can support nutrition but does not prevent all aspiration; embolization or vascular intervention can control selected bleeding; limited debridement/resection may improve odor, bleeding or wound care in carefully chosen cases. Do not offer a major operation merely because disease is anatomically resectable when recovery time and morbidity exceed the likely symptom-control window. Coordinate with radiation oncology, medical oncology, interventional radiology and palliative care before high-burden procedures whenever the clinical tempo permits."
        ),
        "teach": (
            "Chief/boards frame: PALLIATIVE INTERVENTION asks, 'What symptom am I trying to improve, how quickly must it improve, how likely is this intervention to work, and what burden does it impose?' Airway, hemorrhage, nutrition and pain each need their own mechanism-based plan. Tracheostomy is not automatically beneficial; a feeding tube is not a complete aspiration strategy; palliative RT/systemic therapy still require time-to-benefit and toxicity reasoning. The GOALS-OF-CARE card establishes the destination; this card chooses the least-burdensome ENT/oncologic tool that can realistically get there."
        ),
        "tags": ["palliative head neck cancer", "airway palliation", "tumor bleeding", "carotid blowout", "dysphagia", "nutrition", "palliative radiation", "tracheostomy", "gastrostomy", "symptom control"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent/advanced head and neck cancer, airway, dysphagia and treatment complications",
            "K.J. Lee's Essential Otolaryngology, 12e — advanced head and neck cancer and complication management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — advanced head and neck oncology, airway and complication management",
            "Sanders et al., ASCO Guideline Update: Palliative Care for Patients With Cancer, J Clin Oncol 2024"
        ],
    },
}


def apply_palliative_hn_rebuild_v314(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = PALLIATIVE_HN_REBUILD_V314.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v314"] = True
        module["semantic_role_v314"] = {
            "palliative goals of care decision making in head neck cancer": "prognosis, values, capacity/surrogacy and goal-concordant treatment selection",
            "palliative decision making in head and neck cancer": "mechanism-based symptom palliation using the least-burdensome effective ENT/oncologic intervention",
        }[key]
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
