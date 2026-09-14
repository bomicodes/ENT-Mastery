"""v20.35 — paired Concept Checks for CSF Rhinorrhea and endoscopic repair."""

DOMAIN = "Rhinology / Allergy / Skull Base"
DIAG_TOPIC = "CSF Rhinorrhea"
OP_TOPIC = "Endoscopic CSF Leak Repair / Nasoseptal Flap"

SOURCE_REFS = [
    {"type":"textbook","citation":"Cummings Otolaryngology–Head and Neck Surgery, 7th ed. (2021), connected Google Drive ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t — CSF rhinorrhea diagnosis/localization, spontaneous-leak/IIH framework and endoscopic reconstruction."},
    {"type":"textbook","citation":"Pasha & Golub, Otolaryngology–Head & Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52 — CSF leak evaluation and skull-base repair principles."},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology, 12th ed., connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR — CSF rhinorrhea, encephalocele and endoscopic skull-base repair."},
    {"type":"consensus","citation":"Georgalas C, et al. International Consensus Statement: Spontaneous Cerebrospinal Fluid Rhinorrhea. Int Forum Allergy Rhinol. 2021;11:794-803. PMID 33099888; doi:10.1002/alr.22704."},
    {"type":"systematic_review","citation":"Outcomes of Endoscopic Management of Spontaneous Cerebrospinal Fluid Rhinorrhea: A Meta-Analysis. 2025. PMID 40650638 — endoscopic outcomes, reconstruction and lumbar-drain evidence."},
]

DIAG_PROMPT = (
    "An adult has months of unilateral clear watery rhinorrhea that increases with bending forward, intermittent headache and pulsatile tinnitus, "
    "and no convincing allergic symptoms. As the senior resident, how do you confirm a suspected cranial CSF leak, localize the defect, distinguish "
    "spontaneous from traumatic/iatrogenic disease, and address possible idiopathic intracranial hypertension rather than treating this as rhinitis?"
)
DIAG_ANSWER = """### CSF rhinorrhea — confirm, localize, identify the driver

**Confirm the fluid.** Persistent unilateral positional clear drainage should trigger a CSF-leak pathway. Collect fluid for a CSF-specific marker such as beta-2 transferrin when feasible; appearance, taste, or glucose testing alone is not adequate confirmation.

**Localize safely.** Thin-slice high-resolution CT maps bony skull-base defects. Add MRI with high-resolution fluid-sensitive sequences when a meningoencephalocele, soft-tissue lesion, multiple candidate defects, or uncertain localization remains. Recurrent meningitis, pneumocephalus, neurologic change or visual symptoms accelerate evaluation.

**Name the etiology.** Separate traumatic/iatrogenic leaks from spontaneous leaks. In spontaneous CSF rhinorrhea, actively look for idiopathic intracranial hypertension biology—headache, pulsatile tinnitus, visual symptoms, supportive imaging findings and neuro-ophthalmic abnormalities when indicated.

**Management bridge.** A persistent confirmed cranial communication generally needs definitive closure. ICP-directed therapy may be important for recurrence prevention but is not a reflex substitute for repair of an established persistent leak.
"""

OP_PROMPT = (
    "During endoscopic repair of a confirmed anterior skull-base CSF leak, how should defect size/flow, encephalocele, tissue quality, prior surgery and suspected elevated ICP change your reconstruction, "
    "when is a vascularized nasoseptal (Hadad-Bassagasteguy) flap appropriate, what is the role of a lumbar drain, and when should you stop and re-localize rather than force dissection?"
)
OP_ANSWER = """### Endoscopic CSF leak repair — match reconstruction to the defect

**Characterize before reconstructing.** Defect location, size, high- versus low-flow leak, encephalocele, surrounding bone/dura quality, prior surgery/radiation, multiple defects and pressure biology determine the repair.

**Use the least reconstruction that is reliably sufficient.** Small low-flow defects may be managed with supported free-graft/multilayer techniques. Larger, high-flow, revision, irradiated or expanded skull-base defects more often justify vascularized tissue such as a pedicled nasoseptal/Hadad-Bassagasteguy flap. Preserve the posterior septal artery pedicle and rescue-flap option when a vascularized reconstruction may become necessary.

**Lumbar drain is selective.** It is not mandatory for every repair; use should reflect defect/leak/pressure circumstances rather than ritual, and contemporary pooled outcomes do not show a routine success advantage.

**Bail out when anatomy stops making sense.** If the apparent defect conflicts with imaging or the skull-base boundary is uncertain near orbit, optic nerve or carotid, stop and re-localize with imaging/navigation/anatomic landmarks rather than widening blindly. The endpoint is watertight supported closure plus a plan for the underlying cause, including IIH when relevant.
"""


def _check(qid, topic, prompt, answer, aliases):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "canonical_topic": topic,
        "prompt": prompt, "question": prompt, "choices": [], "answer": None,
        "answer_text": answer, "explanation": answer,
        "reviewed_all_domains_v178": True,
        "review_basis_v178": "Dedicated v20.35 paired CSF-leak learner-path repair with exact canonical linkage, senior decision-making and learner-visible sources.",
        "curated_v177": True, "converted_to_oral_board_v178": True,
        "search_aliases": aliases, "source_refs_v230": [dict(x) for x in SOURCE_REFS],
        "learner_experience_v235": {"deep_curriculum": True, "concept_check": True, "daily_curriculum": True, "sources_visible": True},
    }

CHECKS = [
    _check("cc-v235-rhinology-csf-rhinorrhea", DIAG_TOPIC, DIAG_PROMPT, DIAG_ANSWER,
           ["CSF leak", "cerebrospinal fluid rhinorrhea", "spontaneous CSF leak", "skull base leak", "meningoencephalocele", "IIH"]),
    _check("cc-v235-rhinology-endoscopic-csf-repair", OP_TOPIC, OP_PROMPT, OP_ANSWER,
           ["endoscopic CSF leak repair", "nasoseptal flap", "Hadad-Bassagasteguy flap", "vascularized septal flap", "rescue flap", "lumbar drain"]),
]


def apply_rhinology_csf_leak_concept_checks_v235(checks, deep_modules, v6_item_id):
    rows = (deep_modules or {}).get(DOMAIN, []) or []
    by_topic = {str(m.get("topic") or ""): m for m in rows}
    missing = [topic for topic in (DIAG_TOPIC, OP_TOPIC) if topic not in by_topic]
    if missing:
        return {"added": [], "enriched": [], "link_mismatch": missing, "expected": [q["id"] for q in CHECKS]}
    existing = {str(q.get("id") or "") for q in checks or []}
    added = []
    for template in CHECKS:
        if template["id"] in existing:
            continue
        q = dict(template)
        q["source_refs_v230"] = [dict(x) for x in SOURCE_REFS]
        q["concept_id"] = v6_item_id(DOMAIN, template["topic"])
        checks.append(q)
        added.append(q["id"])
    enriched = []
    for q in checks or []:
        if str(q.get("concept_id") or "") not in {v6_item_id(DOMAIN, DIAG_TOPIC), v6_item_id(DOMAIN, OP_TOPIC)}:
            continue
        refs = list(q.get("source_refs_v230") or [])
        blob = " ".join(str(x.get("citation") or "").lower() for x in refs if isinstance(x, dict))
        for source in SOURCE_REFS[:3]:
            citation = str(source["citation"])
            marker = "cummings" if "cummings" in citation.lower() else "pasha" if "pasha" in citation.lower() else "k.j. lee"
            if marker not in blob:
                refs.append(dict(source)); blob += " " + citation.lower()
        q["source_refs_v230"] = refs
        enriched.append(str(q.get("id") or ""))
    return {"added": added, "enriched": enriched, "link_mismatch": [], "expected": [q["id"] for q in CHECKS]}
