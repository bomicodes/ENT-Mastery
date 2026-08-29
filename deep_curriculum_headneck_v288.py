"""v28.8 — source-grounded palliative head & neck oncology Concept Hub rebuild.

Separates two clinically overlapping canonical cards into distinct jobs:
1) Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer = communication,
   prognosis, values, treatment intent, advance care planning, and longitudinal care goals.
2) Palliative Decision-Making in Head and Neck Cancer = symptom-directed ENT decisions
   for airway, bleeding, dysphagia/nutrition, pain, secretions, wounds, and procedure burden.

If only one of the two canonical cards is live, the missing companion content is folded into
that live card under explicit subheadings so resident-critical symptom rescue is not lost.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _append_unique(existing, addition, heading):
    existing = str(existing or "").strip()
    addition = str(addition or "").strip()
    if not addition or addition in existing:
        return existing
    return existing + f"\n\n{heading}: " + addition


PALLIATIVE_REBUILD_V288 = {
    "palliative goals of care decision making in head neck cancer": {
        "recognize": (
            "Recognize GOALS-OF-CARE work as a core oncologic skill, not a synonym for 'stopping treatment.' In advanced or recurrent head-and-neck cancer, palliative care can and should run CONCURRENTLY with disease-directed therapy. Trigger a goals conversation when prognosis, function, symptom burden, or treatment options change: unresectable or metastatic progression, major recurrence after prior therapy, repeated hospitalization, declining performance status, escalating airway/swallowing problems, severe pain, treatment toxicity, or a proposed operation whose functional burden may exceed its realistic oncologic benefit. The resident's first task is to identify what decision is actually being made and whether the patient understands the intent—curative, life-prolonging, symptom-directed, or comfort-focused—of each option."
        ),
        "localize": (
            "Localize the DECISION across four domains: DISEASE (what is controllable and with what probability), FUNCTION (speech, swallowing, airway, appearance, cognition, independence), VALUES (what outcomes the patient considers acceptable), and TIME (expected benefit versus near-term burden). Then identify the decision-maker: assess capacity for the specific decision, involve the legally appropriate surrogate when capacity is absent, and incorporate the patient's previously expressed preferences. Head-and-neck decisions are uniquely preference-sensitive because interventions can trade survival or local control against voice, swallowing, airway dependence, facial form, communication, and caregiver burden. A technically feasible procedure is not automatically a value-concordant procedure."
        ),
        "workup": (
            "Prepare for a goals conversation with the same rigor used for an operation. Clarify cancer status, realistic treatment options, expected response/control, major toxicities, likely functional trajectory, and the consequences of no disease-directed treatment. Assess performance status, frailty, nutrition, symptom burden, communication barriers, cognition/capacity, psychosocial distress, caregiver support, spiritual concerns, and existing advance directives or code-status documentation. Ask what the patient understands, how much prognostic detail they want, what abilities make life worth living, and which burdens they would accept for a meaningful chance of benefit. When uncertainty is high, offer a TIME-LIMITED TRIAL with explicit goals and stopping rules rather than presenting an open-ended treatment plan."
        ),
        "manage": (
            "Use shared decision-making to match treatment INTENSITY to patient goals. Explain best-case, worst-case, and most-likely outcomes in plain language; separate what an intervention can do from what it cannot do. Integrate specialist palliative care early for advanced cancer and especially for uncontrolled physical, psychosocial, or spiritual distress, while continuing appropriate oncology treatment. Revisit goals longitudinally because priorities may change with progression, treatment toxicity, loss of swallowing/voice, caregiver strain, or new symptom crises. Document the patient's values and the reasoning behind decisions—not merely 'DNR' or 'comfort care'—so future teams understand which outcomes matter and which interventions would be nonbeneficial or unacceptable."
        ),
        "operate": (
            "For the surgeon, the advanced decision is WHEN NOT TO OPERATE and when to redefine the operative goal. Before a high-morbidity palliative or salvage procedure, ask whether surgery is likely to deliver the outcome the patient values within the patient's expected time horizon. A tracheostomy, feeding access procedure, tumor debulking, drainage, or hemostatic operation may be appropriate when it predictably relieves a dominant symptom; the same procedure may be burdensome when it creates prolonged hospitalization, dependence, or complications without meaningful symptom or survival benefit. Obtain procedure-specific informed consent that includes the option of NO PROCEDURE and a plan for what happens if the hoped-for benefit is not achieved."
        ),
        "teach": (
            "Chief/boards framework: GOALS OF CARE = INTENT + VALUES + TRADE-OFFS + REASSESSMENT. Palliative care is compatible with active cancer treatment and should not be delayed until the final days of life. Ask 'What are we trying to accomplish for this patient?' before asking 'What can we technically do?' Capacity is decision-specific; when absent, use the appropriate surrogate and the patient's known values. Time-limited trials are useful when benefit is uncertain. Keep airway/bleeding/nutrition rescue algorithms in the companion PALLIATIVE DECISION-MAKING card—this card owns communication, prognosis, and value-concordant treatment selection."
        ),
        "tags": [
            "goals of care", "palliative care", "shared decision making", "advanced head and neck cancer",
            "treatment intent", "decision making capacity", "advance care planning", "time limited trial",
            "quality of life", "caregiver burden"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent/advanced head-and-neck cancer, functional consequences of treatment, and multidisciplinary decision-making",
            "K.J. Lee's Essential Otolaryngology, 12e — advanced head-and-neck cancer treatment principles and functional trade-offs",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — practical advanced-cancer and symptom-management considerations",
            "ASCO Clinical Practice Guideline Update: Palliative Care for Patients With Cancer, J Clin Oncol 2024 — early concurrent interdisciplinary palliative care for advanced cancer and patients with significant physical, psychosocial, or spiritual distress",
            "NCCN Clinical Practice Guidelines in Oncology: Head and Neck Cancers — recurrent/metastatic disease treatment intent, supportive care, and multidisciplinary management",
        ],
    },
    "palliative decision making in head and neck cancer": {
        "recognize": (
            "Recognize the SYMPTOM-DIRECTED palliative ENT problem: an advanced head-and-neck cancer patient may need an immediate decision about AIRWAY, BLEEDING, SWALLOWING/NUTRITION, PAIN, SECRETIONS, WOUND/ODOR, or infection even when the cancer is not curable. Triage first for threats that can kill or cause major suffering now—stridor/airway obstruction, sentinel or major hemorrhage, aspiration with respiratory compromise, uncontrolled pain, dehydration, sepsis, or catastrophic wound breakdown. Palliative does not mean passive: urgent symptom control can be highly active, but every intervention should have a defined symptom target and a burden proportionate to expected benefit."
        ),
        "localize": (
            "Localize the dominant symptom to the mechanism before choosing a procedure. Airway: intraluminal tumor, edema, bilateral vocal-fold immobility, secretions, or external compression. Bleeding: friable mucosal tumor, exposed vessel, pseudoaneurysm, carotid encasement/blowout risk, or treatment-related necrosis. Dysphagia: obstructing tumor, aspiration from neuromuscular dysfunction, pain/odynophagia, xerostomia, or stricture. Pain: nociceptive tumor pain, perineural disease, mucositis, osteoradionecrosis, infection, or neuropathic pain. Wound problems: fungation, necrosis, infection, salivary fistula, malodor, or exposed great vessel. The same symptom can require radically different treatment depending on its mechanism."
        ),
        "workup": (
            "Use focused testing only when it will change symptom-directed care. Flexible laryngoscopy can define airway obstruction, secretion burden, vocal-fold function, and mucosal bleeding. Contrast CT/CTA is useful for deep tumor extent, abscess, necrosis, vascular encasement, pseudoaneurysm, or suspected carotid blowout when the patient is stable enough for imaging. Swallow evaluation helps when aspiration risk and feeding route are uncertain. Check hemoglobin/coagulation for significant bleeding, hydration/electrolytes for poor intake, and infection markers/cultures selectively. Before any procedure, clarify the patient's goals and ceiling of care—especially whether they would accept tracheostomy, feeding-tube dependence, ICU care, embolization, or major operation if complications occur."
        ),
        "manage": (
            "Treat the dominant symptom with the LEAST BURDENSOME effective strategy. Pain: multimodal analgesia with opioid therapy when indicated, plus neuropathic agents and specialist palliative/pain input. Dysphagia/nutrition: texture modification, swallow strategies, analgesia, supplements, and feeding access only when it is likely to meet the patient's nutritional or comfort goals. Secretions: hydration adjustment, suction, oral care, positioning, and anticholinergic therapy when appropriate. Fungating wounds: gentle local wound care, absorbent dressings, odor control, and treatment of true infection rather than reflex antibiotics for colonization. Tumor bleeding may respond to topical/local measures, palliative radiation, endovascular therapy, or surgery depending on source and goals. Palliative radiation can provide meaningful relief of pain, bleeding, and mass-effect symptoms without implying curative intent."
        ),
        "operate": (
            "Perform a procedure only when its symptom benefit is concrete. AIRWAY: tracheostomy may relieve fixed upper-airway obstruction but can create secretion, wound, communication, and caregiving burdens; discuss awake technique when anatomy makes induction dangerous. BLEEDING: a sentinel bleed in a previously irradiated or tumor-encased carotid territory is a warning for carotid blowout—stabilize airway/hemodynamics, use CTA when stable, involve interventional radiology/vascular teams early, and consider endovascular occlusion or covered stenting according to anatomy/collateral flow/goals. NUTRITION: feeding access can support patients receiving meaningful therapy or relieve exhausting oral intake, but it does not automatically prevent aspiration and may not improve quality of life in the final phase of illness. DEBULKING or drainage is justified when it predictably relieves obstruction, infection, odor, pain, or bleeding—not simply because tumor is present."
        ),
        "teach": (
            "Chief/boards symptom framework: AIRWAY → BLEEDING → SWALLOW/NUTRITION → PAIN → SECRETIONS/WOUND, then ask whether the intervention actually serves the patient's stated goal. Sentinel hemorrhage + irradiated/tumor-encased carotid = CAROTID BLOWOUT RISK until proven otherwise. A feeding tube does not eliminate aspiration; a tracheostomy does not treat every cause of dyspnea; antibiotics do not fix a colonized fungating tumor; and a technically possible operation may worsen quality of life if its burden exceeds the expected symptom benefit. This card owns symptom rescue and proportional procedures; the companion GOALS-OF-CARE card owns communication and value-concordant treatment selection."
        ),
        "tags": [
            "palliative head and neck cancer", "airway obstruction", "carotid blowout", "tumor bleeding",
            "dysphagia", "feeding tube", "cancer pain", "fungating wound", "secretions",
            "palliative radiation", "tracheostomy"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — airway, dysphagia, hemorrhage, recurrent cancer, and treatment-related complications",
            "K.J. Lee's Essential Otolaryngology, 12e — airway emergencies, advanced head-and-neck cancer, and symptom-directed management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — practical airway, bleeding, swallowing, and wound management",
            "ASCO Clinical Practice Guideline Update: Palliative Care for Patients With Cancer, J Clin Oncol 2024 — symptom/distress management integrated with active oncology care",
            "NCCN Clinical Practice Guidelines in Oncology: Head and Neck Cancers — supportive/palliative treatment options for recurrent or metastatic disease",
            "Contemporary carotid blowout syndrome literature — recognition of sentinel bleeding, CTA/endovascular evaluation, and multidisciplinary hemorrhage control in irradiated/recurrent head-and-neck cancer",
        ],
    },
}


def apply_headneck_palliative_rebuild_v288(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    broad = None
    symptom = None
    for module in modules:
        key = _norm(module.get("topic"))
        payload = PALLIATIVE_REBUILD_V288.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v288"] = True
        patched.append(module.get("topic"))
        if key == "palliative goals of care decision making in head neck cancer":
            broad = module
        elif key == "palliative decision making in head and neck cancer":
            symptom = module

    folded = False
    if broad is not None and symptom is None:
        post = PALLIATIVE_REBUILD_V288["palliative decision making in head and neck cancer"]
        broad["workup"] = _append_unique(broad.get("workup"), post["workup"], "SYMPTOM-DIRECTED ASSESSMENT")
        broad["manage"] = _append_unique(broad.get("manage"), post["manage"], "SYMPTOM-DIRECTED MANAGEMENT")
        broad["operate"] = _append_unique(broad.get("operate"), post["operate"], "PALLIATIVE ENT PROCEDURES")
        broad["teach"] = _append_unique(broad.get("teach"), post["teach"], "SYMPTOM-RESCUE BOARD FRAMEWORK")
        for tag in post["tags"]:
            if tag not in broad["tags"]:
                broad["tags"].append(tag)
        for source in post["source_basis"]:
            if source not in broad["source_basis"]:
                broad["source_basis"].append(source)
        broad["symptom_sublayer_v288"] = True
        folded = True
    elif symptom is not None and broad is None:
        post = PALLIATIVE_REBUILD_V288["palliative goals of care decision making in head neck cancer"]
        symptom["recognize"] = _append_unique(symptom.get("recognize"), post["recognize"], "GOALS-OF-CARE CONTEXT")
        symptom["manage"] = _append_unique(symptom.get("manage"), post["manage"], "VALUE-CONCORDANT CARE")
        symptom["teach"] = _append_unique(symptom.get("teach"), post["teach"], "GOALS-OF-CARE FRAMEWORK")
        for source in post["source_basis"]:
            if source not in symptom["source_basis"]:
                symptom["source_basis"].append(source)
        symptom["goals_sublayer_v288"] = True
        folded = True

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched), "companion_folded_if_missing": folded}
