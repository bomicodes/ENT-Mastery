"""v29.5 — add the missing frontal-sinus outflow-tract management layer.

The existing canonical Frontal Sinus Fracture ladder is strong and is preserved:
- foundation: analyzes anterior table, posterior table/dura, and frontal sinus
  outflow tract as independent management axes;
- application: observes a minimally displaced isolated anterior-table fracture
  when the outflow tract is intact and there is no CSF leak;
- senior decision: escalates a severe posterior-table/CSF-leak/intracranial pattern
  to cranialization.

What was missing was a direct management decision for the third axis taught by the
foundation question: a threatened/obstructed frontal sinus outflow tract without a
separate indication for reflex cranialization. This pass adds only that layer.
"""

DOMAIN = "Facial Plastics / Trauma"
TOPIC = "Frontal Sinus Fracture"
QUESTION_ID = "v295_fpt_frontal_outflow_mgt"


def apply_facial_frontal_sinus_management_v295(challenges, id_fn):
    concept_id = id_fn(DOMAIN, TOPIC)
    by_id = {str(q.get("id") or ""): q for q in challenges}
    if QUESTION_ID in by_id:
        q = by_id[QUESTION_ID]
        if q.get("concept_id") != concept_id:
            raise RuntimeError(
                f"v29.5: {QUESTION_ID} canonical link drift: "
                f"{q.get('concept_id')!r} != {concept_id!r}"
            )
        return {"concept_id": concept_id, "added": [], "preserved": [QUESTION_ID]}

    q = {
        "id": QUESTION_ID,
        "domain": DOMAIN,
        "topic": TOPIC,
        "concept_id": concept_id,
        "learning_stage": "application",
        "ladder_reviewed": True,
        "management_layer_v295": True,
        "deliberate_review_v295": (
            "Added only the previously untested frontal-sinus outflow-tract management axis; "
            "preserved the existing observation and cranialization cases."
        ),
        "stem": (
            "A patient has a frontal sinus fracture with acceptable forehead contour, no neurologic "
            "instability, no active CSF leak, and no posterior-table injury requiring intracranial "
            "exposure. Thin-cut CT shows fracture through the frontal recess with convincing frontal "
            "sinus outflow-tract obstruction. Which management principle best addresses the major "
            "long-term risk without overtreating the posterior table?"
        ),
        "choices": [
            (
                "Treat the outflow tract as an independent management axis: define the frontal recess "
                "injury carefully and, when the sinus can be safely preserved, establish durable drainage "
                "with an appropriate frontal-sinus procedure and long-term surveillance; use obliteration "
                "or cranialization when a safe functional sinus cannot be maintained or separate posterior-"
                "table/dural indications require it"
            ),
            (
                "Observe without further frontal-sinus planning because acceptable anterior-table contour "
                "and absence of a CSF leak make the outflow tract clinically irrelevant"
            ),
            (
                "Perform cranialization for every suspected frontal sinus outflow-tract injury even when "
                "the posterior table and dura are otherwise stable"
            ),
            (
                "Repair only the anterior-table contour because restoring the external bony shape reliably "
                "re-establishes frontal sinus ventilation"
            ),
        ],
        "answer": 0,
        "why_wrong": [
            (
                "Correct. Outflow obstruction is its own decision axis because retained mucosa behind a "
                "nonfunctional drainage pathway can produce chronic infection or delayed mucocele. The goal "
                "is a safe sinus with durable drainage when preservation is feasible, while obliteration or "
                "cranialization is reserved for patterns in which that goal cannot be achieved or other "
                "posterior-table/dural injuries independently justify escalation."
            ),
            (
                "An intact posterior table and acceptable contour do not neutralize an obstructed frontal "
                "recess. Observation is appropriate for selected fractures with a patent outflow tract, but "
                "known obstruction creates a distinct late sinus-complication pathway that must be addressed."
            ),
            (
                "Cranialization is not the automatic treatment for isolated outflow-tract injury. It is a "
                "major escalation driven chiefly by severe posterior-table/dural/intracranial patterns or by "
                "situations in which a safe functional sinus cannot otherwise be maintained."
            ),
            (
                "Anterior-table fixation restores contour, not necessarily drainage. A well-reduced forehead "
                "can still develop retained secretions, chronic frontal sinusitis, or a mucocele if the frontal "
                "recess remains obstructed."
            ),
        ],
        "explanation": (
            "Frontal sinus fracture management is not a one-axis displacement algorithm. Analyze anterior-table "
            "contour, posterior-table/dural/CSF injury, and the frontal sinus outflow tract independently. "
            "Outflow obstruction matters even when the posterior table is stable: when feasible, preserve a "
            "functional sinus by creating or maintaining durable drainage, often with endoscopic frontal-sinus "
            "techniques in experienced hands. If reliable drainage cannot be achieved, an exclusion procedure "
            "such as obliteration may be needed; cranialization belongs to more destructive posterior-table/"
            "dural/intracranial patterns rather than being a reflex response to every outflow injury."
        ),
        "board_pearl": (
            "For frontal sinus fractures, say the three axes out loud: anterior table/contour, posterior "
            "table-dura-CSF, and frontal sinus outflow. A normal-looking forehead does not make an obstructed "
            "frontal recess safe."
        ),
        "curveball": (
            "A late frontal mucocele can present years after the original trauma or reconstruction. Patients "
            "with significant outflow-tract injury need durable follow-up and reassessment for new frontal pain, "
            "swelling, recurrent sinus symptoms, orbital findings, or imaging evidence of an expansile lesion."
        ),
        "source_basis_v295": (
            "Frontal-sinus trauma principles synthesized from contemporary frontal sinus fracture reviews and "
            "AO CMF Surgery Reference: management depends on anterior/posterior table injury, CSF/dural status, "
            "and frontal sinus outflow patency; outflow obstruction may require drainage restoration or sinus "
            "exclusion rather than automatic cranialization."
        ),
    }
    challenges.append(q)
    return {"concept_id": concept_id, "added": [QUESTION_ID], "preserved": []}
