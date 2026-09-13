"""v20.32 — learner-facing Concept Check for exact Unilateral Sinonasal Disease canonical topic.

The Deep Curriculum already contains the broad unilateral differential and unsafe-biopsy bailout.
This cohort adds one integrated resident-level decision check so that the management pathway is not
fragmented between Deep prose and Daily prompts. It creates no new Deep Curriculum topic.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Unilateral Sinonasal Disease"
QID = "cc-v232-rhinology-unilateral-sinonasal-disease"

SOURCE_REFS = [
    {
        "type": "textbook",
        "citation": "Cummings Otolaryngology–Head and Neck Surgery, 7th ed. (2021), connected Google Drive full-volume copy ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t. Cross-referenced for unilateral sinonasal evaluation, neoplasm/skull-base differential, imaging selection, and biopsy safety principles.",
    },
    {
        "type": "textbook",
        "citation": "Pasha R, Golub JS. Otolaryngology–Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Cross-referenced for practical unilateral obstruction/mass differential, endoscopy, CT/MRI workup, odontogenic disease, and tumor red flags.",
    },
    {
        "type": "textbook",
        "citation": "K.J. Lee's Essential Otolaryngology, 12th ed. (2019), connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Cross-referenced for durable sinonasal tumor, fungal, dental, vascular, and skull-base diagnostic principles.",
    },
]

PROMPT = (
    "An adult patient presents with progressive unilateral nasal obstruction, intermittent epistaxis, "
    "and foul unilateral drainage. Endoscopy shows a unilateral middle-meatal mass with purulence. "
    "As the senior resident, how do you organize the differential, choose CT versus MRI, decide when "
    "biopsy is appropriate or unsafe, and keep odontogenic disease, fungal disease, and malignancy "
    "from being missed?"
)

ANSWER = """### Unilateral sinonasal disease — treat the asymmetry as a diagnostic phenotype, not as routine CRS

**Start broad before naming the lesion.** Important unilateral causes include odontogenic sinusitis, fungal ball or invasive fungal disease, inverted papilloma and other benign tumors, sinonasal malignancy, foreign body, mucocele/obstructive disease, CSF/skull-base lesions, and vascular pathology. Purulence does not exclude a tumor; a mass does not exclude superimposed infection.

**Endoscopy and CT define the first anatomic map.** CT is useful for unilateral sinus opacification, dental disease, calcification/hyperdensity, bony remodeling versus destructive change, and operative anatomy. Add contrast-enhanced MRI when there is a discrete mass, skull-base/orbital concern, possible perineural spread, intracranial continuity, or when retained secretions must be distinguished from tumor.

**Biopsy only after imaging has made biopsy safe.** A unilateral mass often requires tissue, but do not casually biopsy a lesion with possible vascular origin or intracranial/meningoencephalocele continuity. Image first when the history, endoscopy, pulsatility, location, skull-base defect, or bleeding pattern raises that possibility. This is a safety decision, not diagnostic delay.

**Use the pattern to keep common misses visible.** Odontogenic disease should trigger dental-source review and maxillary pattern recognition; fungal ball is suggested by characteristic unilateral material/calcification and is treated surgically rather than with routine prolonged antibiotics; invasive fungal disease requires urgent tissue diagnosis/debridement plus systemic therapy in the appropriate host; malignancy or papilloma requires oncologic imaging/pathology and attachment/extent-based treatment rather than routine FESS.

**Senior synthesis:** unilateral disease is a diagnostic phenotype. Localize with endoscopy and CT, escalate to MRI for mass/skull-base/orbital/perineural questions, establish whether biopsy is safe, obtain tissue when indicated, and treat the actual cause rather than labeling every unilateral process as chronic sinusitis.
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
    "review_basis_v178": "Dedicated v20.32 unilateral-sinonasal learner-path repair reviewed against the live canonical topic, biopsy safety, resident differential, imaging escalation, and learner-visible source requirements.",
    "curated_v177": True,
    "converted_to_oral_board_v178": True,
    "search_aliases": [
        "unilateral sinonasal disease",
        "unilateral sinus disease",
        "unilateral nasal mass",
        "unilateral nasal obstruction",
        "unilateral sinus opacification",
    ],
    "source_refs_v230": SOURCE_REFS,
    "learner_experience_v232": {
        "deep_curriculum": True,
        "concept_check": True,
        "daily_curriculum": True,
        "sources_visible": True,
    },
}


def apply_rhinology_unilateral_concept_check_v232(checks, deep_modules, v6_item_id):
    """Append one exact-canonical unilateral check, deriving its ID from the live inventory."""
    module = next(
        (
            m
            for m in (deep_modules or {}).get(DOMAIN, []) or []
            if str(m.get("topic") or "") == TOPIC
        ),
        None,
    )
    if module is None:
        return {"added": [], "link_mismatch": [QID], "expected": [QID]}
    existing = {str(q.get("id") or "") for q in checks or []}
    if QID in existing:
        return {"added": [], "link_mismatch": [], "expected": [QID]}
    q = dict(CHECK)
    q["concept_id"] = v6_item_id(DOMAIN, TOPIC)
    checks.append(q)
    return {"added": [QID], "link_mismatch": [], "expected": [QID]}
