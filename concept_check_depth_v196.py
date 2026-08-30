"""v19.6 — clinically deepen the exact live PAP Troubleshooting Concept Check.

This cohort deliberately targets a high-yield sleep-surgery management gap rather
than following the lexical backlog rank. It teaches the resident to diagnose why
PAP is failing before escalating pressure or abandoning therapy, and to recognize
central/hypoventilation physiology that should redirect the pathway.
"""

from concept_check_board_repair_v177 import _find_module

COHORT = {
    "cc-v112-rec-sleep-surgery-pap-troubleshooting": {
        "concept_id": "v6-sleep-surgery-pap-troubleshooting",
        "canonical_topic": "PAP Troubleshooting",
        "prompt": (
            "An adult with obstructive sleep apnea returns to sleep-surgery clinic saying CPAP is 'not working.' "
            "The download shows inconsistent use, intermittent large leak, and a residual event index that rises "
            "on nights the device is worn. The patient also reports nasal congestion, dry mouth, pressure intolerance, "
            "and aerophagia. What is the best structured management approach now, and which findings should make you "
            "stop simply increasing pressure and instead reassess the physiology or treatment modality?"
        ),
        "answer_text": (
            "Treat PAP 'failure' as a diagnosis to be established, not as a synonym for disliking CPAP. Start with the "
            "download and separate four problems: whether the patient is actually using PAP for enough of the sleep period, "
            "whether leak is preventing effective therapy, whether pressure/interface symptoms are driving intolerance, and "
            "whether the residual events are truly obstructive. Review nightly use, residual event type/index, leak pattern, "
            "pressure behavior and the relationship between symptoms and device use. A high residual index on a poorly sealed "
            "mask is not proof that the prescribed pressure is inadequate.\n\n"
            "Correct the reversible interface and upper-airway barriers first. Refit or change the mask when leak, pressure "
            "injury, claustrophobia or mouth leak is present; add heated humidification when dryness is limiting use; and treat "
            "clinically important rhinitis or nasal obstruction with appropriate medical therapy. Structural nasal surgery can "
            "improve nasal breathing and PAP tolerance in selected patients, but it should not be presented as automatically "
            "curing OSA or as permission to stop PAP without objective reassessment. Education, desensitization and behavioral "
            "support matter when insomnia, anxiety or conditioning is the adherence barrier.\n\n"
            "Next individualize pressure delivery rather than reflexively turning the pressure up. If residual events are "
            "obstructive after leak and adherence are corrected, review whether pressure is inadequate, whether events cluster "
            "in REM or supine sleep, and whether formal retitration or an appropriate auto-adjusting range is needed. Ramp or "
            "expiratory-pressure relief can help selected patients with pressure intolerance, while bilevel therapy may be "
            "appropriate when clinically indicated for persistent intolerance or ventilatory needs. Aerophagia should trigger "
            "review of unnecessarily high pressures, sleep position and pressure mode rather than automatic escalation.\n\n"
            "The senior decision is to identify physiology that changes the pathway. If the device download or repeat study "
            "shows new or substantial central apneas, periodic breathing, sustained hypoxemia, or hypoventilation, do not keep "
            "raising pressure as though every event were upper-airway obstruction. Reassess for treatment-emergent central sleep "
            "apnea and contributors such as opioids, cardiopulmonary disease, neurologic disease or altitude, and involve sleep "
            "medicine for diagnostic clarification and modality selection. Similarly, severe oxygenation abnormalities out of "
            "proportion to obstructive events require evaluation for additional pulmonary, cardiac or hypoventilation disease.\n\n"
            "Only after a documented optimization attempt should you label PAP genuinely intolerable or ineffective and move "
            "to an alternative OSA strategy. Then match the alternative to anatomy and physiology: oral appliance therapy, "
            "weight-directed treatment, positional therapy, site-directed sleep surgery, or hypoglossal nerve stimulation in "
            "appropriately selected patients. PAP intolerance is not itself an anatomic diagnosis, and a surgical plan should "
            "not be chosen until you know what obstruction you are trying to correct."
        ),
        "explanation": (
            "The board-level distinction is optimization failure versus physiologic failure. Leak, nasal/interface symptoms, "
            "insufficient use and pressure intolerance are common remediable causes of apparent PAP failure. Persistent "
            "obstructive events may justify retitration; central events, periodic breathing or hypoventilation demand a different "
            "diagnostic pathway and can be worsened conceptually by treating every residual event as simple obstruction."
        ),
        "board_pearl": (
            "Before abandoning PAP, read the download and name the failure mode. Before increasing pressure, confirm the residual "
            "events are obstructive rather than leak artifact, treatment-emergent central events, or hypoventilation physiology."
        ),
        "depth_layers_v196": {
            "foundation": (
                "PAP efficacy depends on adequate use, a functioning interface with acceptable leak, tolerable pressure delivery, "
                "and a mode that matches the patient's respiratory physiology."
            ),
            "application": (
                "Use objective device data to distinguish nonadherence, mask/mouth leak, nasal obstruction, pressure intolerance, "
                "persistent obstructive events and treatment-emergent central events; fix the identified mechanism rather than "
                "using a generic 'CPAP failed' label."
            ),
            "senior_decision": (
                "Escalate to repeat titration or sleep-medicine reassessment when residual events remain unexplained, and redirect "
                "the pathway when central apnea, periodic breathing, sustained hypoxemia or hypoventilation suggests physiology "
                "that an upper-airway pressure increase or anatomic operation will not appropriately treat."
            ),
        },
        "common_traps_v196": [
            (
                "Increasing pressure whenever the residual event index is high without first checking large leak and event type. "
                "Leak can make therapy ineffective and device-estimated events less trustworthy, while treatment-emergent central "
                "events require reassessment rather than reflexively treating them as persistent pharyngeal obstruction."
            ),
            (
                "Calling nasal surgery definitive OSA therapy because it improves PAP tolerance. Septal or turbinate treatment can "
                "meaningfully reduce nasal resistance and make PAP easier to use, but the patient still needs objective reassessment "
                "before PAP is discontinued because the collapsible pharyngeal airway may remain untreated."
            ),
            (
                "Labeling PAP 'failed' after a brief poorly supported trial and jumping directly to an implant or multilevel surgery. "
                "First document interface optimization, adherence barriers and residual physiology; only then select an alternative "
                "therapy that matches OSA severity, collapse pattern, anatomy, comorbidity and patient goals."
            ),
        ],
        "deliberate_review_v196": (
            "High-yield Sleep Surgery management concept selected from the live v19.5 canonical backlog because the existing "
            "35-word response collapsed several clinically distinct PAP failure modes into one generic instruction."
        ),
    },
}


def apply_concept_check_task_alignment_v196(checks, deep_modules, v6_item_id):
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    repaired = []
    missing = []
    link_mismatch = []
    for qid, payload in COHORT.items():
        q = by_id.get(qid)
        if q is None:
            missing.append(qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        concept_id = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if (
            module is None
            or topic != payload["canonical_topic"]
            or concept_id != payload["concept_id"]
            or q.get("concept_id") != concept_id
        ):
            link_mismatch.append(qid)
            continue
        for field in (
            "prompt", "answer_text", "explanation", "board_pearl",
            "depth_layers_v196", "common_traps_v196", "deliberate_review_v196",
        ):
            q[field] = payload[field]
        q["task_alignment_v196"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
