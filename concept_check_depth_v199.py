"""v19.9 — deepen the exact live Epistaxis Surgical Control Concept Check.

This cohort targets a high-yield rhinology/emergency/OR decision gap from the
validated v19.8 canonical state. It teaches stabilization and localization,
first-line control, posterior/refractory escalation, antithrombotic boundaries,
and definitive ligation-versus-embolization reasoning with hemorrhage rescue.
"""

from concept_check_board_repair_v177 import _find_module

COHORT = {
    "cc-v112-rec-rhinology-allergy-skull-base-epistaxis-surgical-control": {
        "concept_id": "v6-rhinology-allergy-skull-base-epistaxis-surgical-control",
        "canonical_topic": "Epistaxis Surgical Control",
        "prompt": (
            "A 68-year-old patient on apixaban presents with brisk recurrent epistaxis. Direct pressure and topical vasoconstrictor "
            "slow the bleeding only briefly, blood continues into the oropharynx, and no single anterior septal source is visible after "
            "suction and nasal endoscopy. How should a resident stabilize and localize this bleed, decide when cautery or packing is "
            "appropriate, recognize failure that requires definitive arterial control, and choose between endoscopic surgical control "
            "and embolization while protecting the airway during recurrent major hemorrhage?"
        ),
        "answer_text": (
            "Foundation: manage severe epistaxis as a hemorrhage problem before treating it as a nasal-procedure problem. Assess airway, "
            "breathing, circulation, hemodynamics, estimated blood loss, IV access, and need for resuscitation while clearing clot with suction "
            "so the nasal cavity can actually be examined. Initial control usually includes firm continuous compression of the soft nasal "
            "third and a topical vasoconstrictor when appropriate. Once the field is visible, identify a discrete bleeding point rather than "
            "cauterizing blindly. A clearly visualized anterior source can often be treated with targeted chemical or electrical cautery; avoid "
            "indiscriminate or opposing bilateral septal cautery because excessive septal injury increases ulceration and perforation risk. "
            "When a source cannot be directly controlled, packing is a temporizing hemostatic tool, not proof that the definitive problem has "
            "been solved.\n\n"
            "Application: persistent brisk blood in the nasopharynx/oropharynx, difficulty identifying an anterior source, recurrent bleeding "
            "despite appropriate anterior measures, or a bleed that rapidly saturates anterior packing should raise concern for a posterior or "
            "otherwise refractory source. Re-examine with suction and endoscopy when the patient is stable enough; blood seen anteriorly does "
            "not establish that the source is anterior. Choose packing based on source, anatomy, bleeding severity, and patient factors, and "
            "recognize that posterior packing can compromise the airway and produces substantial discomfort and cardiopulmonary stress. A patient "
            "with significant posterior packing, ongoing blood loss, major comorbidity, or recurrent hemorrhage generally needs monitored care "
            "and a clear escalation plan rather than repeated bedside repacking without a stop rule.\n\n"
            "Medication history changes risk but does not replace local hemorrhage control. In a patient taking an anticoagulant or antiplatelet "
            "agent who is not experiencing life-threatening bleeding, initiate first-line epistaxis treatment before reflexively transfusing, "
            "reversing anticoagulation, or withdrawing antithrombotic therapy. If bleeding is life-threatening or cannot be controlled, reversal "
            "and resuscitation decisions should be individualized to hemorrhage severity, the specific agent and timing, renal function when "
            "relevant, and the patient's thromboembolic indication, ideally with the appropriate emergency/hematology/cardiology team. The trap "
            "is treating an INR or medication list instead of the actively bleeding patient.\n\n"
            "Definitive escalation: persistent or recurrent bleeding not controlled by appropriate packing or nasal cauterization should prompt "
            "evaluation for surgical arterial control or endovascular embolization. For many operable refractory posterior bleeds, endoscopic "
            "sphenopalatine artery control is a durable definitive option because it permits endoscopic localization and treatment near the terminal "
            "arterial supply; identify and control the relevant branches rather than assuming one clip on one visible vessel guarantees success. "
            "The operative survey should also consider another source—such as anterior/posterior ethmoid territory, tumor, trauma, pseudoaneurysm, "
            "or an anatomic lesion—when the bleeding pattern does not fit routine posterior epistaxis or persists after technically adequate SPA "
            "control. Recurrent unilateral bleeding, a mass, cranial neuropathy, severe facial trauma, or an unusual arterial pattern should lower "
            "the threshold for imaging and cause-directed evaluation rather than endless empiric packing.\n\n"
            "Senior decision: ligation and embolization are parallel definitive pathways, not a mandatory sequence. Endoscopic SPA ligation or "
            "cauterization is often favored when the patient can tolerate anesthesia and the likely source is surgically accessible; embolization "
            "is especially valuable when surgery has failed, the suspected source is better approached endovascularly, anatomy limits surgical "
            "access, or the patient/team context favors interventional radiology. Embolization carries uncommon but potentially devastating "
            "neurologic or ophthalmic ischemic complications, so dangerous extracranial-intracranial or ophthalmic anastomoses matter. Conversely, "
            "surgery also fails when the wrong vessel, incomplete branching pattern, or non-SPA source is treated. The senior question is therefore "
            "which pathway most directly controls the suspected arterial source with the safest rescue options in this patient—not which modality "
            "comes first on a memorized ladder.\n\n"
            "Hemorrhage rescue: if brisk bleeding threatens oxygenation, visualization, or hemodynamics, stop repeated blind nasal manipulation. "
            "Call for help, suction aggressively, resuscitate, position and protect the airway, and move to a controlled setting for definitive "
            "hemostasis. An actively hemorrhaging patient who cannot protect the airway may require early definitive airway control by the most "
            "experienced available team while blood products, operative control, and/or interventional radiology are mobilized. Never let pursuit "
            "of the bleeding point delay oxygenation and circulation. The governing sequence is airway and resuscitation first, localization and "
            "temporary control second, and timely definitive arterial control when first-line measures have failed."
        ),
        "explanation": (
            "Epistaxis questions become senior-level when the learner stops equating blood location with source location and stops treating packing "
            "as an endpoint. The resident must stabilize, obtain a visible field, use targeted first-line therapy, recognize refractory/posterior "
            "bleeding, and escalate to the definitive pathway that best matches the source and patient while preserving an airway rescue plan."
        ),
        "board_pearl": (
            "Persistent bleeding after appropriate cautery/packing is a failure signal, not an invitation to repack indefinitely. For refractory "
            "posterior epistaxis, think definitive arterial control—often endoscopic SPA control or embolization—and protect the airway before chasing the source."
        ),
        "depth_layers_v199": {
            "foundation": (
                "Stabilize major hemorrhage, clear clot, obtain visualization, use firm compression/topical vasoconstriction, and cauterize only a "
                "discrete visible source rather than performing blind bilateral septal treatment."
            ),
            "application": (
                "Recognize posterior/refractory patterns, use packing as temporary control with monitoring and a stop rule, and manage antithrombotic "
                "therapy according to bleeding severity rather than reflex withdrawal or reversal in every patient."
            ),
            "senior_decision": (
                "After failed appropriate first-line control, choose endoscopic arterial control versus embolization from suspected source, anatomy, "
                "patient fitness, prior failures, and complication/rescue profile while prioritizing airway and resuscitation during major rebleeding."
            ),
        },
        "common_traps_v199": [
            (
                "Calling a bleed anterior simply because blood is visible at the naris. Posterior blood can track forward and backward; suction, "
                "endoscopic localization, response to treatment, and the overall bleeding pattern are more reliable than where pooled blood is first seen."
            ),
            (
                "Repeatedly cauterizing an unseen source or treating broad opposing septal surfaces. Cautery works best when a discrete bleeding point "
                "is visible; blind or excessive treatment adds tissue injury without reliably controlling a posterior or unidentified arterial source."
            ),
            (
                "Treating packing as definitive success after each temporary pause in hemorrhage. Rapid rebleeding, posterior flow, transfusion need, "
                "or failure of properly placed packing should trigger a stop rule and evaluation for surgical arterial control or embolization."
            ),
            (
                "Automatically stopping or reversing every anticoagulant before attempting local control. In non-life-threatening bleeding, first-line "
                "epistaxis measures come first; life-threatening hemorrhage requires individualized reversal that also respects the patient's thrombotic indication."
            ),
            (
                "Memorizing that SPA ligation must always precede embolization, or that embolization is automatically superior after packing fails. "
                "They are parallel definitive options whose choice depends on likely vessel, accessibility, anesthesia fitness, prior treatment, and local expertise."
            ),
            (
                "Continuing nasal instrumentation while the patient is aspirating blood or becoming unstable. Once oxygenation, airway protection, or "
                "circulation is threatened, resuscitation and controlled airway management outrank another attempt to find the bleeding point at bedside."
            ),
        ],
        "deliberate_review_v199": (
            "High-yield exact Rhinology canonical concept selected from the validated v19.8 state because epistaxis is a common resident emergency and "
            "the key board/OR distinction is not terminology but the transition from first-line localization/control to monitored packing, definitive "
            "arterial treatment, and airway-resuscitation bailout when hemorrhage becomes dangerous."
        ),
    },
}


def apply_concept_check_task_alignment_v199(checks, deep_modules, v6_item_id):
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, payload in COHORT.items():
        q = by_id.get(qid)
        if q is None:
            missing.append(qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        concept_id = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if module is None or topic != payload["canonical_topic"] or concept_id != payload["concept_id"] or q.get("concept_id") != concept_id:
            link_mismatch.append(qid)
            continue
        for field in ("prompt", "answer_text", "explanation", "board_pearl", "depth_layers_v199", "common_traps_v199", "deliberate_review_v199"):
            q[field] = payload[field]
        q["task_alignment_v199"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
