"""v20.30 learner-facing Esthesioneuroblastoma/Olfactory Neuroblastoma management repair.

This cohort repairs discoverability inside the already-deep Sinonasal Malignancy canonical concept.
It preserves the prior sinonasal-oncology framework while adding a coherent ONB pathway across the
Deep Curriculum, Concept Check, and Daily Curriculum data path without creating a 326th topic.
"""
from concept_check_board_repair_v177 import _find_module

QIDS = ("cc-v112-rec-rhinology-allergy-skull-base-sinonasal-malignancy",)
CID = "v6-rhinology-allergy-skull-base-sinonasal-malignancy"
TOPIC = "Sinonasal Malignancy"

ONB_SECTION = r'''

### Esthesioneuroblastoma (Olfactory Neuroblastoma; ONB) — management pathway

**Recognize the disease and establish risk before choosing treatment.** Esthesioneuroblastoma and olfactory neuroblastoma are the same entity; ONB arises from the superior nasal vault/olfactory neuroepithelium and should not be managed as generic sinonasal SCC. After endoscopic biopsy with expert head-and-neck pathology review, document **Hyams grade** and an anatomic stage such as modified **Kadish** and/or the Dulguerov/TNM framework. Map the superior nasal cavity, cribriform plate, dura/brain, orbit and skull base with MRI plus CT for bone; image the neck and complete systemic staging when appropriate. Hyams grade is a major prognostic variable, and high-grade (III-IV), advanced-stage, nodal or intracranial disease changes the intensity and sequencing of treatment.

**Resectable disease: surgery is the local-control backbone, usually with adjuvant radiation.** The operative goal is complete oncologic resection with negative margins and a reconstructable skull base, not preservation of an old-fashioned open approach. Appropriately selected tumors can be resected endoscopically; open or combined craniofacial approaches remain appropriate when lateral extension, extensive intracranial/brain involvement or margin geometry cannot be safely controlled endonasally. The current 2026 REFCOR expert guideline describes **surgical resection followed by adjuvant radiotherapy** as the standard-of-care framework. Modern evidence also supports individualized de-escalation discussions for unusually favorable early, low-grade, completely resected disease, but omission of RT is not a blanket rule and should be an expert-MDT decision rather than assumed from a small Kadish stage alone.

**High-grade, bulky or very morbid locally advanced disease: consider induction therapy selectively.** The 2025 ESMO–EURACAN guideline specifically includes **Hyams III-IV ONB** among high-grade tumors for which neoadjuvant chemotherapy should be considered. This is most useful when up-front local therapy would carry very high morbidity (for example major orbital or near-chiasmal involvement) or when response can help select the definitive strategy. Platinum/etoposide-containing regimens are commonly used in neuroendocrine practice, but evidence remains largely retrospective and rare-tumor based. A response does not erase the pretreatment disease map. REFCOR likewise limits chemotherapy to selected high-grade or unresectable forms; it is not routine adjuvant therapy for every resected low-grade ONB.

**The neck is a deliberate decision, not an SCC copy-and-paste.** A clinically node-positive neck requires therapeutic treatment with surgery and/or radiation according to extent and the definitive plan. For a cN0 neck, elective treatment remains controversial because ONB can relapse regionally late. Risk is higher with advanced Kadish stage, high Hyams grade and extensive primary disease. Meta-analysis shows elective neck irradiation lowers regional recurrence but has not demonstrated an overall-survival advantage in the available low-quality retrospective evidence. Therefore discuss elective neck irradiation (or another elective-neck strategy in selected programs) for higher-risk cN0 disease while observation with disciplined long-term surveillance remains reasonable for selected lower-risk patients.

**Recurrence and surveillance are part of the initial management plan.** ONB is notorious for late local, regional and distant relapse. REFCOR recommends **at least 20 years of follow-up**; other contemporary reviews similarly emphasize prolonged or lifelong surveillance. Follow the primary site with endoscopy plus MRI-based imaging tailored to initial extent, continue neck surveillance rather than stopping after the usual early HNSCC window, and investigate symptoms or nodes even many years later. Resectable isolated recurrence may be salvaged surgically, with radiation/reirradiation or systemic treatment selected according to prior therapy, anatomy and disease distribution.

**Senior-resident synthesis.** For ONB, write the plan as: **confirm expert pathology and Hyams grade -> map Kadish/TNM extent, skull base, orbit, neck and distant disease -> determine whether a negative-margin resection is safely achievable -> use endoscopic versus open/combined exposure according to margin control, not tradition -> add postoperative RT for the usual resected-risk framework -> consider induction chemotherapy for Hyams III-IV/high-morbidity locally advanced disease -> make an explicit cN0-neck decision rather than ignoring it -> commit to decades-long surveillance.** Do not substitute pediatric neuroblastoma drugs, generic HNSCC immunotherapy approvals or an SCC neck algorithm for ONB-specific multidisciplinary reasoning; as of this review there is no FDA indication that makes a systemic drug a routine ONB-specific standard.
'''

SOURCE_REFS_V230 = [
    {"type":"textbook","citation":"Cummings Otolaryngology–Head and Neck Surgery, 7th ed. (2021), connected Google Drive full-volume copy ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t. Cross-referenced for olfactory neuroblastoma/esthesioneuroblastoma terminology, sinonasal/skull-base anatomy, staging and durable operative principles."},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology–Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Cross-referenced for esthesioneuroblastoma/Kadish framework and surgery plus postoperative-radiation teaching."},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology, 12th ed. (2019), connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Cross-referenced for olfactory neuroblastoma, Hyams/Kadish risk concepts and craniofacial/endoscopic oncologic principles."},
    {"type":"guideline","citation":"Resteghini C, et al. Sinonasal malignancy: ESMO–EURACAN Clinical Practice Guideline. ESMO Open. 2025;10(2):104121. PMID 39986703. DOI 10.1016/j.esmoop.2024.104121. Includes ONB; supports histology-aware MDT care and neoadjuvant chemotherapy consideration for Hyams III-IV ONB/high-morbidity locally advanced disease."},
    {"type":"consensus","citation":"Gorzkowski V, et al. REFCOR guidelines on the management of olfactory neuroblastoma: a formalized expert consensus. Eur Ann Otorhinolaryngol Head Neck Dis. 2026;143(4):325-329. PMID 42442982. DOI 10.1016/j.anorl.2026.06.004. Surgery plus adjuvant RT standard framework; chemotherapy selected for high-grade/unresectable disease; at least 20 years follow-up."},
    {"type":"review","citation":"Ariizumi Y, Asakage T. Development of an evaluation and treatment strategy for olfactory neuroblastoma: review of large-scale studies, multicenter studies and meta-analyses. Jpn J Clin Oncol. 2024;54(8):847-862. PMID 38762332. DOI 10.1093/jjco/hyae062."},
    {"type":"systematic_review","citation":"De Virgilio A, et al. Elective neck irradiation in the management of esthesioneuroblastoma: systematic review and meta-analysis. Rhinology. 2021;59(5):433-440. PMID 34254061. DOI 10.4193/Rhin21.139. ENI reduced regional recurrence in cN0 patients without demonstrated OS or distant-metastasis benefit; evidence quality limited."},
    {"type":"regulatory_boundary","citation":"FDA approvals for pediatric/adult high-risk neuroblastoma are not esthesioneuroblastoma/olfactory-neuroblastoma indications. No ONB-specific FDA systemic-drug indication was identified in the current FDA approval search; do not transfer pediatric neuroblastoma or generic HNSCC labels into routine ONB treatment."},
]

# These are intentionally concise additions to the existing canonical card. They make the ONB
# pathway visible where a learner studies the topic and feed the adaptive Daily answers because
# get_adaptive_items_v120 is built from the live DEEP_MODULES_V6 fields.
DEEP_ONB_V230 = {
    "workup": "ONB/esthesioneuroblastoma focus: confirm expert pathology and Hyams grade; stage anatomic extent with Kadish/Dulguerov-TNM concepts; use CT for bone plus MRI for cribriform/dural/brain/orbital extent; assess the neck and distant disease when indicated.",
    "manage": "ONB/esthesioneuroblastoma focus: for resectable disease, margin-oriented surgery followed by adjuvant radiotherapy is the usual curative framework. Consider induction chemotherapy selectively for Hyams III-IV or very morbid locally advanced disease. Treat a node-positive neck therapeutically; for cN0 disease, discuss elective neck treatment versus disciplined observation according to risk because regional relapse can be late.",
    "operate": "ONB/esthesioneuroblastoma senior decision: choose endoscopic versus open/combined exposure by ability to obtain controlled negative margins and reconstruct the skull base, not by tradition. Extensive lateral/intracranial disease or unsafe margin geometry should trigger a combined/open strategy rather than forcing an endonasal resection. Preserve the pretreatment disease map even after induction response.",
    "teach": "Teach ONB as: expert pathology + Hyams -> map Kadish/TNM extent including skull base/orbit/neck -> decide safe negative-margin resectability -> endoscopic versus open/combined approach by margin control -> usual postoperative RT -> selective induction therapy for high-grade/high-morbidity disease -> explicit cN0-neck decision -> surveillance for at least 20 years because late recurrence is characteristic.",
}

LEARNER_SOURCE_BASIS_V230 = [
    "Cummings Otolaryngology–Head and Neck Surgery, 7e (2021) — connected Google Drive ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
    "Pasha & Golub, Otolaryngology–Head and Neck Surgery: Clinical Reference Guide, 6e (2022) — connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
    "K.J. Lee's Essential Otolaryngology, 12e (2019) — connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
    "ESMO–EURACAN Sinonasal Malignancy Clinical Practice Guideline (2025) — PMID 39986703",
    "REFCOR Olfactory Neuroblastoma guideline/consensus (2026) — PMID 42442982",
    "De Virgilio et al. elective neck irradiation systematic review/meta-analysis (2021) — PMID 34254061",
]

TRAPS_V230 = [
    "Treating esthesioneuroblastoma and olfactory neuroblastoma as different diseases rather than synonyms for ONB.",
    "Managing ONB as generic sinonasal SCC and ignoring Hyams grade and Kadish/Dulguerov staging.",
    "Calling open craniofacial resection mandatory when a negative-margin endoscopic resection is feasible in an experienced center.",
    "Conversely choosing endoscopy because the tumor is reachable when lateral/intracranial extent prevents controlled margins.",
    "Omitting postoperative radiation reflexively because an early-stage tumor was completely resected without discussing grade and expert-MDT risk.",
    "Giving induction chemotherapy to every ONB instead of selecting high-grade or very morbid locally advanced disease.",
    "Assuming an induction response erases the pretreatment skull-base/orbital disease map.",
    "Ignoring the cN0 neck even though delayed regional failure is a characteristic ONB problem.",
    "Claiming elective neck irradiation improves overall survival when current meta-analysis primarily demonstrates regional-control benefit.",
    "Stopping surveillance after five years despite documented very late ONB recurrence.",
    "Applying pediatric neuroblastoma drugs or biology to ONB because both contain the word neuroblastoma.",
    "Applying generic HNSCC immunotherapy approvals as an ONB-specific standard without disease-specific evidence or a valid tumor-agnostic indication.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "learner_experience_v230": {
        "discoverable_subtopic": "Esthesioneuroblastoma (Olfactory Neuroblastoma; ONB)",
        "search_aliases": ["esthesioneuroblastoma", "olfactory neuroblastoma", "ONB", "esthesioblastoma"],
        "required_path": "Sinonasal Malignancy -> explicit ONB management subsection -> ONB-focused Daily management/advanced prompts",
    },
    "depth_layers_v230": {
        "foundation": "ONB terminology, olfactory-skull-base origin, Hyams grade, Kadish/Dulguerov/TNM extent and staging workup.",
        "application": "Negative-margin surgery with approach selected by anatomy, adjuvant RT framework, selective induction therapy and explicit cN0-neck decision.",
        "senior_decision": "Balance resectability, skull-base/orbital morbidity, high-grade chemosensitivity, regional-risk uncertainty and decades-long surveillance.",
    },
    "common_traps_v230": TRAPS_V230,
    "deliberate_review_v230": {"priority":"high","review_after_days":[1,7,21,60],"reason":"rare skull-base malignancy with histology-specific treatment, neck and late-recurrence decisions that were previously not learner-discoverable"},
    "source_refs_v230": SOURCE_REFS_V230,
    "evidence_distinction_v230": "Durable textbook anatomy, staging and margin-oriented surgery are preserved. Current management is updated with 2025 ESMO–EURACAN and 2026 REFCOR guidance: surgery plus adjuvant RT remains the usual curative framework, Hyams III-IV/high-morbidity disease may justify induction chemotherapy, cN0 neck treatment is risk-stratified and controversial, and surveillance must extend for decades. Retrospective/meta-analytic neck and de-escalation evidence is labeled as limited rather than promoted to universal standard.",
    "task_alignment_v230": True,
}}


def _append_once(module, field, addition):
    current = str(module.get(field) or "").strip()
    marker = "ONB/esthesioneuroblastoma"
    if marker.lower() not in current.lower():
        module[field] = (current + ("\n\n" if current else "") + addition).strip()


def _apply_deep_learner_path_v230(module):
    if not module:
        return
    for field, addition in DEEP_ONB_V230.items():
        _append_once(module, field, addition)
    existing = [str(x) for x in (module.get("source_basis") or [])]
    seen = {x.lower() for x in existing}
    for source in LEARNER_SOURCE_BASIS_V230:
        if source.lower() not in seen:
            existing.append(source)
            seen.add(source.lower())
    module["source_basis"] = existing
    aliases = [str(x) for x in (module.get("search_aliases") or [])]
    alias_seen = {x.lower() for x in aliases}
    for alias in ("esthesioneuroblastoma", "olfactory neuroblastoma", "ONB", "esthesioblastoma"):
        if alias.lower() not in alias_seen:
            aliases.append(alias)
            alias_seen.add(alias.lower())
    module["search_aliases"] = aliases
    module["learner_experience_v230"] = {
        "daily_curriculum": True,
        "concept_check": True,
        "deep_curriculum": True,
        "source_basis_visible": True,
    }


def apply_concept_check_task_alignment_v230(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, patch in COHORT.items():
        q = by.get(qid)
        if q is None:
            missing.append(qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != patch["canonical_topic"] or cid != patch["concept_id"]:
            link_mismatch.append(qid)
            continue
        _apply_deep_learner_path_v230(module)
        answer = str(q.get("answer_text") or "")
        marker = "### Esthesioneuroblastoma (Olfactory Neuroblastoma; ONB) — management pathway"
        if marker not in answer:
            q["answer_text"] = answer.rstrip() + ONB_SECTION
        q["concept_id"] = CID
        q["learner_experience_v230"] = patch["learner_experience_v230"]
        q["search_aliases"] = sorted(set(list(q.get("search_aliases") or []) + patch["learner_experience_v230"]["search_aliases"]), key=str.lower)
        for field in ("depth_layers_v230", "common_traps_v230", "deliberate_review_v230", "source_refs_v230", "evidence_distinction_v230", "task_alignment_v230"):
            q[field] = patch[field]
        q["choices"] = []
        q["answer"] = None
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
