"""v28.9 — keep pediatric otitis disease decisions distinct from tube candidacy.

The canonical registry intentionally contains both:
- AOM / OME / Tympanostomy Decisions
- Tympanostomy Tube Indications

The original v24.2 application and senior cases duplicated the later v24.6 tube
candidacy ladder. Preserve the useful v24.2 AOM-vs-OME foundation case, but
retarget the two duplicated layers to acute treatment and complication escalation.
"""

DOMAIN = "Pediatric Otolaryngology"
TOPIC = "AOM / OME / Tympanostomy Decisions"

REPAIRS = {
    "v242_ped_ear_app": {
        "learning_stage": "application",
        "stem": "A 30-month-old has unilateral acute otitis media with a newly bulging tympanic membrane, mild otalgia for less than 24 hours, temperature 38.0 C, no otorrhea, and reliable follow-up. What is the best management approach?",
        "choices": [
            "Use shared decision-making: observation for 48-72 hours with a reliable rescue-antibiotic plan is reasonable, while immediate antibiotics are also acceptable",
            "Place tympanostomy tubes immediately because one episode of AOM is an operative indication",
            "Order temporal-bone CT before treating uncomplicated AOM",
            "Treat with topical ear drops alone despite an intact tympanic membrane",
        ],
        "answer": 0,
        "explanation": "In a child at least 24 months old with nonsevere unilateral AOM and reliable follow-up, either immediate antibiotics or initial observation with a defined rescue plan is reasonable. Severity, age, laterality, otorrhea and follow-up reliability determine whether observation is safe; this is a disease-treatment decision rather than a tube-candidacy question.",
        "why_wrong": [
            "Correct. This child has nonsevere unilateral AOM, is older than 24 months, and has reliable follow-up, so a 48-72 hour observation option with rescue therapy is evidence-based.",
            "A single uncomplicated AOM episode is not an indication for tympanostomy tubes and surgery does not replace appropriate acute treatment.",
            "Routine CT adds radiation without benefit in uncomplicated AOM; imaging is reserved for suspected intratemporal or intracranial complication.",
            "With an intact tympanic membrane, topical drops do not reliably reach the infected middle ear and are not stand-alone treatment for routine AOM.",
        ],
        "board_pearl": "For uncomplicated AOM, treatment is driven by age, severity, laterality, otorrhea and follow-up reliability—not by reflex antibiotics or reflex tubes.",
        "curveball": "How would bilateral disease in a 12-month-old, otorrhea, severe otalgia, temperature at least 39 C, or unreliable follow-up change the plan?",
        "focus": "clinic_decision",
    },
    "v242_ped_ear_snr": {
        "learning_stage": "senior_decision",
        "stem": "A 5-year-old treated for acute otitis media returns with fever, worsening otalgia, postauricular erythema and tenderness, auricular protrusion, and loss of the postauricular sulcus. What is the best senior-level next step?",
        "choices": [
            "Treat this as acute mastoiditis: admit, start appropriate IV antibiotics, obtain urgent ENT assessment, and use imaging and drainage/mastoid surgery according to abscess, neurologic findings, complications, and clinical response",
            "Reassure the family that postauricular swelling is expected during uncomplicated AOM and continue routine outpatient observation",
            "Place an elective tympanostomy tube weeks later without addressing the current infection",
            "Manage only with topical otic drops because all post-AOM infections are confined to the ear canal",
        ],
        "answer": 0,
        "explanation": "Postauricular inflammation with auricular displacement after AOM is a mastoiditis phenotype, not routine persistent otitis. The chief-level task is to recognize complication, stabilize and admit the child, start parenteral therapy, involve ENT early, and identify subperiosteal, intracranial or other complicated disease that changes the need for imaging and source control.",
        "why_wrong": [
            "Correct. These are classic mastoid inflammatory findings and require inpatient treatment plus early surgical assessment rather than routine AOM follow-up.",
            "Auricular protrusion, postauricular tenderness and sulcus loss are red flags for mastoid involvement and should not be normalized as uncomplicated AOM.",
            "Deferring treatment to a later elective tube does not control a current potentially invasive mastoid infection or its complications.",
            "Topical drops alone do not treat mastoid infection and would dangerously under-treat possible deep or intracranial extension.",
        ],
        "board_pearl": "AOM becomes an escalation problem when postauricular inflammation, auricular displacement, cranial neuropathy, meningismus, severe headache, vertigo, or systemic toxicity appears.",
        "curveball": "Which findings would make you obtain urgent contrast imaging and proceed more quickly to drainage or mastoidectomy rather than relying on IV antibiotics alone?",
        "focus": "overnight_call",
    },
}


def apply_pediatric_ear_semantic_alignment_v289(challenges, id_fn):
    expected_cid = id_fn(DOMAIN, TOPIC)
    by_id = {str(q.get("id") or ""): q for q in challenges}
    repaired = []
    for qid, patch in REPAIRS.items():
        q = by_id.get(qid)
        if not q:
            raise RuntimeError(f"v28.9: expected pediatric ear ladder case missing: {qid}")
        if q.get("concept_id") != expected_cid:
            raise RuntimeError(f"v28.9: {qid} canonical link drift: {q.get('concept_id')!r} != {expected_cid!r}")
        if not q.get("ladder_reviewed"):
            raise RuntimeError(f"v28.9: {qid} lost ladder_reviewed metadata")
        q.update(patch)
        q["semantic_alignment_v289"] = True
        q["deliberate_review_v289"] = "Removed duplicated tube-candidacy decision and restored a distinct otitis disease-management layer."
        repaired.append(qid)
    return {"repaired": repaired, "concept_id": expected_cid}
