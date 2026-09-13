"""v20.33 — learner-facing Concept Check for Facial Pain / Headache vs Rhinogenic Disease.

The Deep Curriculum successor establishes the causal threshold and surgery-avoidance boundary.
This integrated case makes that reasoning explicit at the Concept Check layer without adding or
renaming a Deep Curriculum topic.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Facial Pain / Headache vs Rhinogenic Disease"
QID = "cc-v233-rhinology-facial-pain-rhinogenic-headache"

SOURCE_REFS = [
    {
        "type": "textbook",
        "citation": "Cummings Otolaryngology–Head and Neck Surgery, 7th ed. (2021), connected Google Drive full-volume copy ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t. Cross-referenced for facial-pain differential diagnosis, rhinogenic disease, migraine mimics, and durable operative decision principles.",
    },
    {
        "type": "textbook",
        "citation": "Pasha R, Golub JS. Otolaryngology–Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Cross-referenced for practical sinus-versus-headache differentiation and sinonasal workup.",
    },
    {
        "type": "textbook",
        "citation": "K.J. Lee's Essential Otolaryngology, 12th ed. (2019), connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Cross-referenced for facial pain, neuralgia, dental/TMJ mimics, and sinonasal surgical boundaries.",
    },
    {
        "type": "classification",
        "citation": "International Headache Society. International Classification of Headache Disorders, 3rd edition (ICHD-3), section 11.5.2 Headache attributed to chronic or recurring rhinosinusitis. Requires objective sinonasal inflammatory evidence plus evidence of causation; imaging/endoscopic abnormalities alone do not secure the diagnosis.",
    },
    {
        "type": "guideline",
        "citation": "AAO-HNSF Clinical Practice Guideline: Adult Sinusitis Update (2025). Used for current objective-confirmation and alternative-diagnosis principles in chronic rhinosinusitis rather than treating facial pressure alone as proof of sinus disease.",
    },
]

PROMPT = (
    "An adult patient has recurrent facial pressure and headache labeled as 'sinus headache.' CT "
    "shows limited mucosal thickening, but symptoms include episodic photophobia and nausea and do "
    "not reliably track with nasal inflammation. As the senior ENT resident, what objective evidence "
    "and causal relationship are required before calling the pain rhinogenic, which migraine, "
    "trigeminal/neuralgic, dental, and TMJ alternatives should remain visible, and when should FESS "
    "not be used as a diagnostic trial?"
)

ANSWER = """### Facial pain and 'sinus headache' — objective inflammation is necessary, but causation still has to be demonstrated

**Do not diagnose rhinogenic headache from the symptom label or a mildly abnormal CT alone.** ICHD-3 requires clinical/endoscopic/imaging evidence of sinonasal inflammatory disease plus evidence that the headache behaves causally with that disease and is not better explained by another headache disorder. Objective disease is therefore necessary for CRS attribution, but it is not sufficient by itself.

**Migraine is the common trap.** Migraine can produce facial pressure, congestion, tearing, rhinorrhea, photophobia, phonophobia and nausea. Episodic attacks that do not wax and wane with sinonasal inflammation should push the differential away from a reflex 'sinus headache' diagnosis. Also consider trigeminal neuralgia or neuropathic facial pain, TACs when autonomic symptoms and attack pattern fit, dental disease, and TMJ/masticatory disorders.

**Ask whether the anatomy and time course actually match.** A stronger rhinogenic attribution has concordant objective inflammation, temporal coupling between pain and sinus disease, and improvement/worsening that parallels the sinonasal process. A unilateral inflammatory process with ipsilateral pain can support causation. Conversely, isolated contact-point anatomy is not proof that a headache is caused by the nose.

**FESS is not a diagnostic trial for unexplained facial pain.** Operate when there is an established sinonasal disease indication and a reasonable expectation that surgery addresses that disease burden. Persistent pain despite adequate inflammatory control or technically successful sinus surgery should reopen migraine, neuralgia, dental, TMJ, or another non-rhinogenic diagnosis rather than trigger automatic revision surgery.

**Escalate red flags outside the routine headache pathway.** New neurologic deficit, visual loss/ophthalmoplegia, thunderclap or rapidly progressive headache, meningismus, cranial neuropathy, necrotic tissue, or destructive/skull-base findings require urgent evaluation for complication or alternative disease rather than routine 'sinus headache' management.
"""

CHECK = {
    "id": QID,
    "domain": DOMAIN,
    "topic": TOPIC,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "question": PROMPT,
    "choices": [],
    "answer": None,
    "answer_text": ANSWER,
    "explanation": ANSWER,
    "reviewed_all_domains_v178": True,
    "review_basis_v178": "Dedicated v20.33 facial-pain learner-path repair reviewed for objective sinonasal evidence, causal attribution, migraine/neuralgia/dental/TMJ alternatives, surgery avoidance, red flags, and exact canonical linkage.",
    "curated_v177": True,
    "converted_to_oral_board_v178": True,
    "search_aliases": ["sinus headache", "rhinogenic headache", "facial pressure", "facial pain", "migraine", "contact point headache"],
    "source_refs_v230": SOURCE_REFS,
    "learner_experience_v233": {
        "deep_curriculum": True,
        "concept_check": True,
        "daily_curriculum": True,
        "sources_visible": True,
    },
}


def apply_rhinology_facial_pain_concept_check_v233(checks, deep_modules, v6_item_id):
    module = next(
        (m for m in (deep_modules or {}).get(DOMAIN, []) or [] if str(m.get("topic") or "") == TOPIC),
        None,
    )
    if module is None:
        return {"added": [], "link_mismatch": [QID], "expected": [QID]}
    if any(str(q.get("id") or "") == QID for q in checks or []):
        return {"added": [], "link_mismatch": [], "expected": [QID]}
    q = dict(CHECK)
    q["concept_id"] = v6_item_id(DOMAIN, TOPIC)
    checks.append(q)
    return {"added": [QID], "link_mismatch": [], "expected": [QID]}
