"""ENT Mastery v41.6 — practical CSF-rhinorrhea on-call disposition pathway.

Adds the missing bridge between diagnosis and repair: what can proceed through an
expedited outpatient skull-base pathway, what needs same-day postoperative/trauma
assessment, and what requires emergency evaluation/admission.  The disposition
language is deliberately framed as safety triage rather than a universal admission
rule because institutional resources and the clinical context still matter.
"""

from copy import deepcopy


DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "CSF Rhinorrhea"
QUESTION_ID = "v416_rhi_csf_oncall_disposition"

WORKUP = (
    "ON-CALL SPECIMEN / IMAGING — If a stable patient has intermittent unilateral "
    "watery drainage and fluid is available, collect passive drainage in the clean "
    "screw-cap container specified by the receiving laboratory for beta-2 transferrin "
    "(or beta-trace protein where available); verify local minimum-volume, storage, and "
    "transport requirements. Do not use nasal glucose, and do not delay emergency "
    "evaluation or indicated imaging merely to obtain a specimen. Thin-cut high-resolution "
    "CT maps bone; add high-resolution fluid-sensitive MRI when encephalocele, soft-tissue "
    "pathology, multiple candidate defects, or uncertain localization is present."
)

MANAGE = (
    "ON-CALL DISPOSITION — This is a safety-triage framework, not a universal admission "
    "rule. EMERGENCY evaluation with ENT/neurosurgical coordination and admission as "
    "clinically indicated: fever or meningismus, photophobia with severe headache, altered "
    "mental status, focal neurologic deficit, seizure, acute visual change, significant "
    "pneumocephalus, acute skull-base trauma, or concern for intracranial infection/complication. "
    "A suspected active leak after recent sinonasal or skull-base surgery warrants immediate "
    "contact with the operating team and same-day assessment; high-volume continuous drainage, "
    "neurologic/infectious features, or inability to obtain prompt specialty evaluation lowers "
    "the threshold for ED evaluation/admission. EXPEDITED OUTPATIENT pathway: a reliable, "
    "clinically stable patient with chronic/intermittent suspected spontaneous leakage, no "
    "recent trauma or surgery, and no infectious, neurologic, or intracranial red flags may "
    "undergo prompt beta-2-transferrin testing, skull-base imaging, and rhinology/skull-base "
    "follow-up; do not dismiss or route this as routine rhinitis. Persistent confirmed leakage "
    "still requires a definitive closure plan."
)

PRECAUTIONS = (
    "WHILE AWAITING DEFINITIVE EVALUATION — Avoid nose blowing, forceful sniffing, Valsalva/"
    "straining, heavy lifting, deep bending, and unnecessary nasal instrumentation; sneeze "
    "with the mouth open and use measures to avoid constipation when appropriate. Follow the "
    "operating skull-base team's specific instructions after surgery, including guidance about "
    "nasal positive-pressure devices. Give explicit meningitis return precautions: fever, neck "
    "stiffness, photophobia, severe or rapidly worsening headache, vomiting with systemic illness, "
    "confusion, seizure, or new neurologic deficit requires emergency evaluation. Routine "
    "prophylactic antibiotics do not close an uncomplicated cranial leak and are not routinely "
    "recommended solely to prevent meningitis; treat suspected infection promptly. Review "
    "pneumococcal vaccination status and follow the current CDC/ACIP risk-based schedule for a "
    "patient with a CSF leak rather than hard-coding an outdated vaccine regimen."
)

TEACH = (
    "CALL PEARL — First separate danger from diagnosis. Red flags or an acute postoperative/"
    "traumatic context determine immediate disposition; beta-2 transferrin answers whether the "
    "fluid is CSF, and CT/MRI answer where the defect is. A stable outpatient pathway means "
    "expedited testing and skull-base follow-up with documented precautions—not watchful waiting "
    "without a plan."
)

CONSENSUS = (
    "Georgalas C et al. International Consensus Statement: Spontaneous Cerebrospinal Fluid "
    "Rhinorrhea. Int Forum Allergy Rhinol. 2021;11:794-803. PMID 33099888; "
    "doi:10.1002/alr.22704 — biochemical confirmation, CT/MRI localization, prompt definitive "
    "management, and evaluation of intracranial-pressure biology."
)
ANTIBIOTIC_SOURCE = (
    "Ratilal BO et al. Antibiotic prophylaxis for preventing meningitis in patients with basilar "
    "skull fractures. Cochrane Database Syst Rev. 2015;2015(4):CD004884. PMID 25918919 — available "
    "randomized evidence does not support routine prophylactic antibiotics, including in patients "
    "with CSF leakage; suspected infection requires treatment."
)
CDC_SOURCE = (
    "CDC/ACIP. Adult Immunization Schedule by Medical Condition and Other Indication, current "
    "online schedule: https://www.cdc.gov/vaccines/hcp/imz-schedules/adult-medical-condition.html "
    "— CSF leak is a pneumococcal risk condition; use the current age-, history-, and "
    "product-specific schedule at the time of care."
)
OUTCOMES_SOURCE = (
    "Mughal Z et al. Outcomes of Endoscopic Management of Spontaneous Cerebrospinal Fluid "
    "Rhinorrhea: A Meta-Analysis. Laryngoscope. 2026;136(1):36-49. Epub 2025 Jul 12. "
    "PMID 40650638; doi:10.1002/lary.32428."
)

QUESTION = {
    "id": QUESTION_ID,
    "domain": DOMAIN,
    "topic": TOPIC,
    "learning_stage": "senior_decision",
    "stem": (
        "At 2 AM, a reliable adult reports several weeks of intermittent unilateral clear "
        "positional rhinorrhea. There was no trauma or recent sinonasal/skull-base surgery. The "
        "patient is afebrile and has no severe headache, meningismus, visual symptoms, confusion, "
        "or neurologic deficit. What is the best on-call disposition?"
    ),
    "choices": [
        "Reassure the patient that clear drainage is allergic rhinitis and arrange routine follow-up in several months",
        "Send every suspected cranial CSF leak to the ICU before confirmation",
        "Use an expedited outpatient skull-base pathway: provide pressure and meningitis precautions, collect fluid for beta-2 transferrin when feasible, arrange high-resolution CT with MRI as indicated, and ensure prompt specialty follow-up",
        "Start prophylactic antibiotics and defer localization unless meningitis develops",
    ],
    "answer": 2,
    "explanation": (
        "A stable, reliable patient with a chronic/intermittent suspected spontaneous leak and no "
        "postoperative, traumatic, infectious, neurologic, or intracranial danger features does not "
        "automatically require overnight admission. The safe alternative is expedited—not routine—"
        "outpatient confirmation, localization, skull-base follow-up, and explicit precautions. "
        "Fever/meningismus, severe or rapidly worsening headache, altered mental status, focal deficit, "
        "seizure, acute visual change, pneumocephalus, acute trauma, or an active recent postoperative "
        "leak changes the disposition toward immediate same-day/emergency assessment and admission as indicated."
    ),
    "why_wrong": [
        "Persistent unilateral positional drainage can represent a cranial communication and should not be routed as routine rhinitis without a plan.",
        "Disposition is driven by acuity and danger features; stable chronic suspected leakage does not universally require ICU admission.",
        "Correct. Confirmation, localization, precautions, and prompt skull-base follow-up form the stable outpatient pathway.",
        "Routine prophylactic antibiotics neither localize nor close the defect and are not a substitute for definitive evaluation.",
    ],
    "board_pearl": (
        "On call, disposition comes first: danger/postoperative/traumatic context determines urgency; "
        "beta-2 transferrin confirms fluid and CT/MRI localize the defect."
    ),
    "curveball": (
        "If the caller instead has fever, neck stiffness, severe headache, confusion, a new neurologic "
        "deficit, acute trauma, significant pneumocephalus, or active drainage soon after skull-base "
        "surgery, direct immediate ED/same-day surgical evaluation rather than outpatient testing."
    ),
    "curveball_answer": (
        "Those features remove the patient from the stable outpatient branch. Direct emergency or "
        "same-day operative-team assessment, evaluate for meningitis and intracranial complication, "
        "obtain urgent imaging as clinically indicated, and admit when the findings or required "
        "monitoring/treatment warrant it; do not wait for an outpatient beta-2-transferrin result."
    ),
    "tier": "Curated learning ladder",
    "mode": "Vignette",
    "focus": "overnight_call",
    "ladder_reviewed": True,
    "source_refs": [CONSENSUS, ANTIBIOTIC_SOURCE, CDC_SOURCE],
}


def _append(row, field, text, marker):
    current = row.get(field) or ""
    if not isinstance(current, str):
        raise RuntimeError(f"v41.6: malformed {field} on {TOPIC}")
    if marker.lower() not in current.lower():
        row[field] = current.rstrip() + ("\n\n" if current.strip() else "") + text


def _replace_outcomes_source(sources):
    cleaned = []
    for source in sources:
        text = str(source)
        if "PMID 40650638" in text:
            if OUTCOMES_SOURCE not in cleaned:
                cleaned.append(OUTCOMES_SOURCE)
        elif text not in cleaned:
            cleaned.append(text)
    if OUTCOMES_SOURCE not in cleaned:
        cleaned.append(OUTCOMES_SOURCE)
    return cleaned


def apply_csf_rhinorrhea_oncall_v416(data_module, app_module=None):
    deep_source = getattr(data_module, "DEEP_MODULES_V6", None)
    challenges_source = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(deep_source, dict) or not isinstance(challenges_source, list):
        raise RuntimeError("v41.6: production curriculum registries unavailable")

    deep = deepcopy(deep_source)
    challenges = deepcopy(challenges_source)
    matches = [row for row in deep.get(DOMAIN, []) if row.get("topic") == TOPIC]
    if len(matches) != 1:
        raise RuntimeError(f"v41.6: expected one {TOPIC} topic; found {len(matches)}")
    row = matches[0]

    _append(row, "workup", WORKUP, "on-call specimen / imaging")
    _append(row, "manage", MANAGE, "on-call disposition")
    _append(row, "manage", PRECAUTIONS, "while awaiting definitive evaluation")
    _append(row, "teach", TEACH, "call pearl")

    sources = row.get("source_basis") or []
    if isinstance(sources, str):
        sources = [sources]
    if not isinstance(sources, list):
        raise RuntimeError(f"v41.6: malformed source_basis on {TOPIC}")
    sources = _replace_outcomes_source(sources)
    row["source_basis"] = list(dict.fromkeys(sources + [CONSENSUS, ANTIBIOTIC_SOURCE, CDC_SOURCE]))
    row["oncall_disposition_v416"] = {
        "stable_outpatient": "expedited confirmation, localization, precautions, and skull-base follow-up",
        "same_day": "suspected active recent postoperative leak or clinically concerning traumatic context",
        "emergency": "infectious, neurologic, visual, pneumocephalus, or other intracranial danger features",
        "scope": "safety triage; local admission and perioperative protocols still apply",
    }

    for related in deep.get(DOMAIN, []):
        if related.get("topic") == "Endoscopic CSF Leak Repair / Nasoseptal Flap":
            related_sources = related.get("source_basis") or []
            if isinstance(related_sources, str):
                related_sources = [related_sources]
            related["source_basis"] = _replace_outcomes_source(related_sources)

    ids = [str(item.get("id") or "") for item in challenges]
    if ids.count(QUESTION_ID) > 1:
        raise RuntimeError(f"v41.6: duplicate challenge id: {QUESTION_ID}")
    question_added = QUESTION_ID not in ids
    if question_added:
        question = deepcopy(QUESTION)
        question["concept_id"] = data_module._v6_item_id(DOMAIN, TOPIC)
        challenges.append(question)

    data_module.DEEP_MODULES_V6.clear()
    data_module.DEEP_MODULES_V6.update(deep)
    data_module.CLINICAL_CHALLENGES_V119[:] = challenges
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {
        "topic": TOPIC,
        "oncall_disposition_added": True,
        "question_added": question_added,
        "question_id": QUESTION_ID,
        "outcomes_citation_reconciled": True,
    }
