"""v32.6 — goals-of-care framework versus H&N-specific palliative intervention decisions.

The duplicate audit identifies full title containment between:
- Palliative / Goals-of-Care Decision-Making in H&N Cancer
- Palliative Decision-Making in H&N Cancer

Preserve both. The parent card owns VALUES/PROGNOSIS/DECISION ARCHITECTURE. The companion
card owns translation of those goals into HEAD-AND-NECK-SPECIFIC symptom and procedural choices.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


PALLIATIVE_REBUILD_V326 = {
    "palliative goals of care decision making in h n cancer": {
        "recognize": (
            "Use this card for GOALS-OF-CARE AND TREATMENT-INTENT DECISIONS in advanced head and neck cancer. "
            "Palliative care is not synonymous with hospice, withdrawal, or 'no treatment': it can and should run concurrently "
            "with disease-directed therapy when symptom burden, prognosis, functional tradeoffs, or decision complexity justify it. "
            "Trigger an explicit goals conversation when disease is incurable or recurrent/metastatic, when curative treatment has a "
            "low probability of benefit or high functional cost, when symptoms/QOL are poorly controlled, or when repeated admissions, "
            "declining performance status, major weight loss, aspiration, airway dependence, or caregiver strain signal a changing trajectory."
        ),
        "localize": (
            "Localize the DECISION, not merely the tumor. Separate: (1) oncologic facts—resectability, metastatic burden, treatment options, "
            "expected response and prognosis; (2) functional consequences—speech/communication, swallowing/oral intake, airway independence, "
            "appearance, cognition and mobility; (3) patient priorities—longevity, symptom relief, time at home, preserving a specific function, "
            "avoiding hospitalization or major surgery; and (4) treatment burden—operations, tracheostomy, feeding access, radiation visits, "
            "systemic toxicity and recovery time. A technically feasible treatment is not automatically a goal-concordant treatment."
        ),
        "workup": (
            "Before recommending a pathway, confirm decision-making capacity, identify the legally appropriate surrogate when capacity is absent, "
            "review any advance directive/POLST-equivalent documentation, and assess what the patient understands about diagnosis and prognosis. "
            "Ask what outcome would be unacceptable and what function matters most. Clarify whether the proposed intervention is curative, "
            "life-prolonging, symptom-directed, or a time-limited trial. Reassess pain, dyspnea, dysphagia/aspiration, nutrition, communication, "
            "mood, spiritual distress and caregiver burden; these are treatment-relevant data, not side issues."
        ),
        "manage": (
            "Use a shared-decision sequence: state the medical situation in plain language -> elicit values and acceptable tradeoffs -> offer a "
            "clinician recommendation that links those values to realistic options -> document the chosen intent and contingencies. Early specialist "
            "palliative care should be integrated alongside oncology for advanced cancer rather than reserved for the final days. When benefit is "
            "uncertain, a TIME-LIMITED TRIAL may be appropriate only if the team defines the intervention, expected measurable benefit, review point, "
            "and what will happen if that benefit is not achieved. Revisit goals after progression, hospitalization, major functional loss, or a new "
            "airway/feeding/bleeding crisis."
        ),
        "operate": (
            "For the surgeon, the key operative question is not 'Can I do this?' but 'What outcome is this operation expected to achieve, at what "
            "burden, and does that outcome match the patient's priorities?' Before major palliative or noncurative surgery, explicitly discuss the "
            "probability of meaningful symptom relief, wound/reconstruction risk, hospitalization and rehabilitation, likelihood of tracheostomy or "
            "feeding dependence, alternatives, and the possibility that recovery consumes much of the patient's remaining time. The detailed choice "
            "among airway, hemorrhage, feeding, wound and local-control procedures belongs to the companion 'Palliative Decision-Making in H&N Cancer' card."
        ),
        "teach": (
            "Boards/chief discriminator: GOALS-OF-CARE = DEFINE INTENT BEFORE CHOOSING THE INTERVENTION. Palliative care may coexist with active cancer "
            "treatment; hospice is a distinct end-of-life care model. Capacity/surrogate status, prognosis understanding, patient values, function, "
            "treatment burden and contingency planning are part of the oncologic plan. Never infer a patient's goals from age, disability, stage, "
            "tracheostomy status, or clinician preference."
        ),
        "tags": ["palliative care", "goals of care", "shared decision-making", "treatment intent", "advanced head and neck cancer", "quality of life", "capacity", "surrogate", "time-limited trial", "hospice distinction"],
        "source_basis": [
            "ASCO 2024 Palliative Care for Patients With Cancer guideline update — early interdisciplinary palliative care alongside active cancer treatment for advanced malignancy and distress/QOL needs",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — palliative-care consultation, multidisciplinary planning, symptom management and end-of-life discussion in incurable H&N cancer",
            "K.J. Lee's Essential Otolaryngology, 12e — recurrent/metastatic HNSCC pathways and palliative care when disease is incurable",
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — head-and-neck oncology, supportive care, functional outcomes and palliative-versus-curative decision framework (textbook backbone; current palliative-care timing updated with ASCO 2024)",
        ],
    },
    "palliative decision making in h n cancer": {
        "recognize": (
            "Use this card for HEAD-AND-NECK-SPECIFIC PALLIATIVE INTERVENTION TRIAGE after the goals and treatment intent are known. "
            "The recurring problems are threatened airway, tumor bleeding/carotid blowout risk, dysphagia/aspiration, pain, secretions, "
            "fungating/malodorous wounds, infection, communication loss and burdensome local progression. A symptom-directed procedure can "
            "be appropriate even when cancer is incurable, but every intervention must have a defined symptom target and a plausible time-to-benefit."
        ),
        "localize": (
            "Localize the immediate threat and the anatomy that determines options. AIRWAY: supraglottic/laryngeal obstruction, bulky pharyngeal disease, "
            "tracheal involvement or secretions. BLEEDING: focal mucosal bleeding versus sentinel hemorrhage with exposed/encased carotid or irradiated "
            "wound. SWALLOW: mechanical obstruction versus neuromuscular aspiration, with attention to saliva aspiration that a feeding tube will not fix. "
            "WOUND: necrotic tumor, fistula, infected secretions, exposed vessels or hardware. Then ask whether local treatment can relieve that specific "
            "problem within the patient's expected trajectory."
        ),
        "workup": (
            "Do only the workup that can change a goal-concordant decision. Flexible endoscopy and targeted imaging may define airway level, bleeding source, "
            "resectability or a focal radiation/IR target; swallow assessment may clarify aspiration mechanism and safe comfort strategies. A sentinel bleed "
            "in an irradiated/recurrent neck warrants urgent carotid-blowout consideration if rescue is consistent with goals. Avoid burdensome staging, "
            "biopsy or imaging when the result will not alter treatment. For every proposed procedure, document target symptom, expected onset/duration of benefit, "
            "burden, alternative, and a backup plan if it fails."
        ),
        "manage": (
            "Match the least-burdensome effective treatment to the symptom target. AIRWAY: consider endoscopic debulking, tracheostomy, stenting in selected anatomy, "
            "palliative radiation/systemic therapy when time permits, or comfort-focused dyspnea treatment when invasive rescue is outside goals. BLEEDING: local "
            "hemostatic measures, radiation, IR/endovascular or operative control when appropriate; for anticipated catastrophic hemorrhage under comfort-focused care, "
            "prepare the team/family and prioritize rapid relief of distress and continuous bedside support. DYSPHAGIA: feeding access may support nutrition or bypass "
            "obstruction but does not reliably prevent aspiration of saliva/reflux; comfort feeding can be goal-concordant when informed risk is accepted. WOUNDS: control "
            "pain, odor, exudate and bleeding rather than pursuing closure at any cost."
        ),
        "operate": (
            "Procedure selection is symptom-specific. Do not perform a tracheostomy, feeding tube, major resection, flap, carotid intervention or other invasive rescue "
            "simply because it is technically possible. Ask whether it prevents an imminent event or relieves a dominant symptom, whether benefit will occur soon enough, "
            "and what new burdens it creates. Palliative radiation fractionation and surgical extent should be chosen with prognosis, travel/treatment burden and time-to-benefit "
            "in mind. If an invasive intervention no longer serves the stated goal, redirect to active symptom control rather than framing that choice as 'doing nothing.'"
        ),
        "teach": (
            "Boards/chief discriminator: PALLIATIVE H&N PROCEDURES = DEFINE THE SYMPTOM TARGET, THEN CHOOSE THE LOWEST-BURDEN INTERVENTION WITH A REALISTIC TIME-TO-BENEFIT. "
            "Tracheostomy may relieve obstruction but can add secretion/care burden; gastrostomy can provide nutrition but does not abolish aspiration; palliative RT can control "
            "pain/bleeding/mass effect but still imposes treatment burden; sentinel hemorrhage changes urgency. This card answers HOW TO TRANSLATE ESTABLISHED GOALS INTO H&N-SPECIFIC ACTIONS."
        ),
        "tags": ["palliative head and neck surgery", "airway obstruction", "carotid blowout", "sentinel hemorrhage", "dysphagia", "aspiration", "feeding tube", "fungating wound", "palliative radiation", "symptom-directed procedure"],
        "source_basis": [
            "ASCO 2024 Palliative Care for Patients With Cancer guideline update — symptom/QOL-centered interdisciplinary palliative care integrated with cancer treatment",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — H&N multidisciplinary palliation, IR for bleeding, feeding access, nutrition and symptom management",
            "K.J. Lee's Essential Otolaryngology, 12e — recurrent/metastatic HNSCC symptom progression, reirradiation limitations and palliation when cancer is incurable",
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — advanced/recurrent H&N cancer, airway/swallowing morbidity, local symptom control and supportive-care framework",
        ],
    },
}


def apply_palliative_rebuild_v326(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = PALLIATIVE_REBUILD_V326.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v326"] = True
            module["semantic_role_v326"] = (
                "values, prognosis, capacity, treatment intent, shared decision-making and contingency planning"
                if key == "palliative goals of care decision making in h n cancer"
                else "head-and-neck-specific airway, hemorrhage, swallowing, wound and symptom-directed intervention triage"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
