"""v19.8 — deepen the exact live Pediatric Airway Foreign Body Concept Check.

This cohort targets a high-yield pediatric airway/OR decision gap from the validated
v19.7 canonical backlog. It teaches suspicion despite normal imaging, stable versus
unstable pathways, rigid-bronchoscopy planning, extraction hazards, and rescue when
ventilation is lost or the object migrates.
"""

from concept_check_board_repair_v177 import _find_module

COHORT = {
    "cc-v112-rec-pediatric-otolaryngology-pediatric-airway-foreign-body": {
        "concept_id": "v6-pediatric-otolaryngology-pediatric-airway-foreign-body",
        "canonical_topic": "Pediatric Airway Foreign Body",
        "prompt": (
            "A previously healthy 2-year-old has a witnessed choking episode while eating peanuts. The severe coughing settles, "
            "but unilateral wheeze and decreased breath sounds persist; chest radiography is read as normal. How should a resident "
            "decide whether further imaging or bronchoscopy is needed, what features make this an immediate airway-rescue problem, "
            "how should rigid bronchoscopy be planned with anesthesia, and what should the team do if ventilation suddenly worsens "
            "or the foreign body migrates during extraction?"
        ),
        "answer_text": (
            "Foundation: treat the aspiration history as major diagnostic evidence. A witnessed choking event followed by persistent "
            "unilateral wheeze, asymmetric breath sounds, focal recurrent pneumonia, unexplained cough, or stridor can represent an "
            "airway foreign body even when the child later appears comfortable. Many aspirated objects are radiolucent, so a normal "
            "chest radiograph does not exclude aspiration. Inspiratory/expiratory films or bilateral decubitus views may show unilateral "
            "air trapping, atelectasis, mediastinal shift, or a radiopaque object, but imaging should answer an uncertainty question—not "
            "erase a convincing clinical event. CT can be useful in selected stable equivocal cases when it is likely to avoid an "
            "unnecessary bronchoscopy, but it should not delay endoscopic evaluation when suspicion remains high.\n\n"
            "Application: first separate the stable child from the child with impending or complete obstruction. Severe stridor, rapidly "
            "increasing work of breathing, cyanosis, inability to ventilate, altered mental status, or a clearly mobile/proximal object is "
            "an airway emergency. In a stable child with a convincing aspiration history, rigid bronchoscopy is both the diagnostic and "
            "definitive removal platform in most pediatric cases because the rigid scope provides a ventilating airway and permits secure "
            "instrumentation. Flexible bronchoscopy may have a diagnostic or adjunctive role in selected settings, but it should not become "
            "a reason to delay definitive rigid removal when clinical suspicion is high.\n\n"
            "Before entering the OR, the surgeon and anesthesiologist should agree on the suspected location and object, bronchoscope sizes, "
            "optical forceps and backup retrieval instruments, whether spontaneous or controlled ventilation best fits the case and local "
            "expertise, how ventilation will be maintained through the bronchoscope, and what the rescue sequence will be if the airway is "
            "lost. There is no single ventilation technique that is correct for every foreign body; the senior principle is shared planning "
            "that minimizes coughing, air trapping, migration, hypoxemia, and repeated traumatic attempts while preserving the surgeon's "
            "ability to see and control the object.\n\n"
            "During extraction, expose the object completely enough to understand its axis and surrounding edema before grasping it. Avoid "
            "blind instrumentation that can push a partially obstructing object distally or convert it into a complete obstruction. Select a "
            "grasp that controls the object rather than merely pinching a fragment; friable organic material may break apart and require "
            "multiple pieces to be removed. As the object passes the glottis, keep the bronchoscope, forceps, and object coordinated so the "
            "foreign body is not lost at the cords. After removal, re-inspect both bronchial trees for a second object, retained fragments, "
            "mucosal injury, bleeding, purulence, or edema before declaring the procedure finished.\n\n"
            "Senior decision/rescue: if oxygenation or ventilation deteriorates, stop repetitive extraction attempts and restore a ventilating "
            "airway first. Withdraw obstructing instruments, re-establish ventilation through the rigid bronchoscope, suction blood/secretions, "
            "and reassess object position. If a proximal object has migrated into a complete tracheal obstruction and cannot be immediately "
            "removed, an experienced bronchoscopist may need to displace it into one mainstem bronchus to permit contralateral-lung ventilation "
            "as a rescue maneuver while definitive removal is reorganized; this is a bailout, not a routine technique. The team must also be "
            "prepared for pneumothorax, airway edema, laryngospasm/bronchospasm, bleeding, or an unexpectedly sharp object. If endoscopic control "
            "cannot be maintained, escalate early to the institution's pediatric difficult-airway and surgical rescue plan rather than persisting "
            "with repeated blind attempts. The governing principle is oxygenation first, controlled extraction second."
        ),
        "explanation": (
            "Pediatric airway foreign-body questions test whether the learner respects the aspiration history, understands that normal imaging "
            "does not exclude a radiolucent object, and can move from diagnosis to a shared rigid-bronchoscopy/anesthesia plan. Senior-level "
            "reasoning includes recognizing when extraction itself is causing loss of ventilation and stopping to restore oxygenation before "
            "another attempt."
        ),
        "board_pearl": (
            "A classic choking history outranks a normal chest x-ray. In the OR, rigid bronchoscopy is not just a retrieval tool—it is the "
            "ventilating airway. If extraction worsens ventilation, stop, oxygenate, regain control, and then resume removal."
        ),
        "depth_layers_v198": {
            "foundation": (
                "Foreign-body aspiration is a clinical diagnosis supported, not excluded, by imaging; radiolucent objects commonly produce only "
                "secondary signs such as unilateral air trapping or atelectasis."
            ),
            "application": (
                "Distinguish stable high-suspicion patients who need definitive bronchoscopy from children with impending obstruction who need an "
                "immediate shared airway-rescue pathway, then plan scope size, retrieval instruments, ventilation, and post-removal reinspection."
            ),
            "senior_decision": (
                "Recognize migration or extraction-induced complete obstruction, stop repeated traumatic attempts, re-establish ventilation first, "
                "and use a deliberate bailout—including mainstem displacement only when required to restore contralateral ventilation—before "
                "returning to definitive removal."
            ),
        },
        "common_traps_v198": [
            (
                "Reassuring yourself with a normal chest radiograph after a witnessed choking event. Most food foreign bodies are radiolucent, "
                "and the dangerous miss is allowing negative imaging to overrule persistent unilateral findings or a highly convincing history."
            ),
            (
                "Sending a high-suspicion child through serial imaging because the patient currently looks comfortable. CT can help a truly stable "
                "equivocal case, but additional testing should not delay rigid bronchoscopy when the pretest probability is already high."
            ),
            (
                "Treating ventilation strategy as a memorized rule such as 'always spontaneous' or 'always controlled.' The correct senior move is "
                "a surgeon-anesthesiologist plan tailored to object location, degree of obstruction, age, air trapping, equipment, and rescue capability."
            ),
            (
                "Continuing to pull repeatedly when the object slips proximally and ventilation collapses. Extraction is no longer the immediate goal; "
                "restore a ventilating airway, reassess position, and only then make the next controlled retrieval attempt."
            ),
            (
                "Stopping after the first object is removed. Reinspect both bronchial trees because retained fragments, a second foreign body, bleeding, "
                "edema, purulence, or mucosal injury can explain persistent postoperative symptoms and may require additional treatment."
            ),
        ],
        "deliberate_review_v198": (
            "High-yield Pediatric Otolaryngology concept selected from the live v19.7 canonical backlog. Its prior 74-word answer correctly named "
            "rigid bronchoscopy but did not teach stable-versus-unstable triage, shared ventilation planning, extraction migration, oxygenation-first "
            "bailout reasoning, bilateral post-removal reinspection, or individualized OR traps."
        ),
    },
}


def apply_concept_check_task_alignment_v198(checks, deep_modules, v6_item_id):
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
        for field in ("prompt", "answer_text", "explanation", "board_pearl", "depth_layers_v198", "common_traps_v198", "deliberate_review_v198"):
            q[field] = payload[field]
        q["task_alignment_v198"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
