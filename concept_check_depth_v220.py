"""v20.20 — deepen the exact-live Cranial Nerve Examination / Skull Base Localization Concept Check on validated v20.19 production."""
from concept_check_board_repair_v177 import _find_module

QIDS = (
    "cc-v112-rec-general-ent-emergencies-cranial-nerve-examination-skull-base-localization",
)
CID = "v6-general-ent-emergencies-cranial-nerve-examination-skull-base-localization"
TOPIC = "Cranial Nerve Examination / Skull Base Localization"

SOURCE_REFS_V220 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive corpus rechecked 2026-09-08; full/compressed copies and split Parts 1-6 remain available. Topic-level extraction from the oversized/split corpus was not reliably available, so no unsupported page-level claim is made.","role":"required core-text cross-check for durable cranial-nerve, skull-base foraminal, temporal-bone and operative anatomy; current management is separately updated below"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy rechecked 2026-09-08.","role":"resident/board cross-check for focused cranial-nerve examination, lower-cranial-nerve dysfunction, facial-nerve differential diagnosis and ENT localization"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy rechecked 2026-09-08; indexed text identifies Collet-Sicard syndrome as unilateral CN IX-XII palsy.","role":"durable localization cross-check for clustered lower cranial neuropathies and named skull-base syndromes"},
    {"type":"appropriateness_criteria","citation":"Rath TJ, Policeni B, et al. ACR Appropriateness Criteria Cranial Neuropathy: 2022 Update. J Am Coll Radiol. 2022;19(11S):S266-S303. PMID: 36436957. Current online criterion/references reverified 2026-09-08.","role":"current imaging layer: choose imaging by the involved nerve/pathway and suspected compartment; MRI, high-resolution CT and vascular imaging answer different questions"},
    {"type":"society_guidance","citation":"American Academy of Otolaryngology-Head and Neck Surgery. Bell's Palsy imaging quality-measure/clinical-guideline boundary, current material reviewed 2026-09-08.","role":"do not routinely image a classic uncomplicated new Bell palsy, but atypical features such as additional cranial neuropathies, recurrence, branch-limited weakness or other neurologic abnormalities invalidate that shortcut"},
    {"type":"systematic_review","citation":"Kumar LP, Upreti G, Paramasivam S, et al. Current Evidence in the Management of Central Skull Base Osteomyelitis: A Systematic Review. J Neurol Surg B Skull Base. 2025;86(3):360-369. PMID: 40351881. DOI: 10.1055/a-2297-9474.","role":"current disease-layer reminder that skull-base osteomyelitis commonly presents with headache and cranial neuropathy and requires diagnosis/treatment of the underlying skull-base infection"},
    {"type":"peer_reviewed_review","citation":"Supsupin EP Jr, Gonzales NS, Debnam JM. Anatomy and Pathology of the Skull Base: Malignant and Nonmalignant Lesions. Oral Maxillofac Surg Clin North Am. 2023;35(3):413-433. PMID: 37142448.","role":"modern skull-base imaging/anatomic review supporting foramina and named nerve pathways as routes of disease spread"},
]

PROMPT = """A 68-year-old patient with diabetes develops progressive deep otalgia and headache followed by dysphonia, aspiration symptoms, ipsilateral shoulder weakness, tongue weakness, and a new peripheral facial paresis. A routine emergency-department head CT is unrevealing. As the ENT resident, localize the deficits before naming a diagnosis, identify the functions requiring immediate protection, select imaging that covers the suspected skull-base pathways, and explain why an uncomplicated Bell-palsy label is unsafe. How does the plan change if vision is threatened, airway/swallow function deteriorates, or a skull-base/carotid-space lesion is pulsatile or vascular-appearing?"""

ANSWER = """Foundation — treat a cranial-nerve examination as an anatomic localization exercise, not twelve isolated checkboxes. Multiple ipsilateral deficits should be mapped to a shared corridor: III/IV/V1/V2/VI cluster around the cavernous sinus; optic dysfunction added to ophthalmoplegia pushes toward the orbital apex; VII/VIII point toward CPA/IAC/temporal-bone pathways; IX/X/XI traverse the jugular foramen; XII exits the hypoglossal canal. A unilateral IX-XII pattern is classically Collet-Sicard syndrome. Lower-cranial-nerve deficits plus sympathetic dysfunction suggest extension into the carotid/parapharyngeal space rather than a lesion confined to the foramina.

Repeat and document the examination yourself. Test pupils, visual function, ocular motility, V1/V2/V3 sensation, facial movement, hearing/vestibular symptoms, palate and secretion handling, voice/cough, tongue bulk/fasciculation/protrusion, and trapezius/SCM. Flexible laryngoscopy is appropriate when IX/X dysfunction or vocal-fold mobility is in question. Do not write 'CN intact' without testing the functions that establish the localization.

Application — imaging must follow the suspected nerve pathway. Contrast-enhanced MRI is usually the principal soft-tissue/nerve-pathway study for unexplained progressive or multiple cranial neuropathies, but the protocol and field of view must cover the relevant skull-base and extracranial course. Add high-resolution CT when the question is temporal-bone/skull-base osseous disease, foraminal erosion/remodeling, fracture or osteomyelitis. Add CTA/MRA and, when appropriate, venous imaging when aneurysm, dissection, carotid-space vascular pathology, cavernous-sinus thrombosis or another vascular process is plausible. A normal routine noncontrast head CT does not close a clinically compelling skull-base localization.

Cavernous-sinus/orbital-apex reasoning — painful ophthalmoplegia is a localization, not a diagnosis. Check pupils and vision. Cavernous-sinus disease may affect III, IV, V1, V2, VI and sympathetic fibers; orbital-apex disease adds optic-nerve dysfunction. New visual loss, an afferent pupillary defect, rapidly progressive ophthalmoplegia, severe orbital findings or systemic toxicity changes urgency because vision, intracranial spread or a vascular/infectious emergency may be threatened. Protect vision and obtain urgent targeted imaging/specialty help rather than waiting for an elective workup.

Lower-cranial-nerve reasoning — dysphonia, dysphagia, aspiration, palatal weakness, shoulder weakness and tongue weakness require functional triage before etiologic elegance. IX/X dysfunction can threaten airway protection and nutrition now. Document vocal-fold and pharyngeal function, obtain swallow evaluation when aspiration risk is clinically important, and support nutrition/pulmonary safety as needed. XI weakness deserves direct trapezius/SCM testing and early rehabilitation planning. XII weakness with atrophy/fasciculation supports a lower-motor-neuron lesion and can compound bolus-control and airway/swallow problems.

Skull-base osteomyelitis trap — in an older, diabetic, immunocompromised or otherwise at-risk patient with severe persistent otalgia/headache and new cranial neuropathies, do not stop at 'Bell palsy' or 'stroke ruled out.' Central skull-base osteomyelitis can produce multiple cranial neuropathies and substantial morbidity. Current systematic-review evidence reinforces early recognition and an underlying-disease approach: targeted imaging, microbiology/pathology when needed, antimicrobial planning, comorbidity optimization and multidisciplinary management rather than symptomatic labeling alone.

Facial-paralysis boundary — routine imaging is not needed for every classic new uncomplicated Bell palsy, but that rule does not apply when the phenotype is atypical. Additional cranial neuropathies, recurrent same-side paralysis, branch-selective weakness, progressive course, hearing/vestibular findings, parotid/temporal-bone abnormalities, cancer history or other neurologic signs should trigger investigation for a different process. VII weakness embedded in a skull-base syndrome is not uncomplicated Bell palsy.

Oncologic application — progressive unilateral multiple cranial neuropathies with deep pain, trismus, unilateral effusion, nasal symptoms, parotid/neck findings, weight loss or prior malignancy should raise concern for nasopharyngeal, parotid, skull-base, metastatic or perineural-spread disease. Image the full expected nerve course and suspected primary compartment. Named skull-base syndromes localize anatomy; they do not establish etiology.

Senior rescue — protect function in parallel with diagnosis. Exposure keratopathy from VII weakness requires eye protection. Vision-threatening orbital/apical disease requires urgent escalation. IX/X dysfunction with aspiration, secretion failure, bilateral vocal-fold impairment or progressive airway symptoms requires airway/swallow planning before routine outpatient investigation. Severe dysphagia may require temporary nutritional support. These measures should not wait for final pathology.

Operative/anatomic application — when a lesion reaches the skull base, the operative question is not simply whether it is technically accessible. First define which compartment, foramen, carotid segment, dura, venous sinus, cranial nerves and lower-neck neurovascular structures are involved, then decide whether the intended procedure is diagnostic, decompressive, source-control, oncologic or reconstructive. Preoperative imaging should be reviewed with that objective in mind. Loss of a clean tissue plane around the internal carotid artery, extension across multiple foramina, intracranial disease, or a deficit pattern implying extensive perineural spread may fundamentally change the safest approach and the value of an attempted resection. Senior judgment means recognizing when more anatomy must be defined before committing to a corridor.

Diagnostic sequencing matters as well. Infection, inflammatory disease and malignancy can mimic one another at the central skull base, so tissue is sometimes necessary, but the route and timing must be deliberate. Correlate endoscopy, otologic findings, inflammatory markers, cultures, imaging and cancer history; choose a biopsy target that is both diagnostically useful and anatomically safe; and avoid assuming that a negative superficial sample excludes deeper disease. If the patient is unstable because of airway compromise, aspiration, sepsis, threatened vision or a vascular process, stabilize that threat first and obtain tissue in a controlled setting rather than allowing diagnostic urgency to create a procedural catastrophe.

Vascular/procedural bailout — a pulsatile skull-base mass is not automatically a biopsy target. Pulsatility, flow voids, carotid-space location, lower-cranial-nerve deficits with sympathetic findings, brisk unexplained bleeding or imaging concern for paraganglioma/vascular pathology should trigger vascular characterization before instrumentation. Do not perform blind transnasal exploration for a possible carotid or cavernous-sinus complication. Stop, localize, obtain appropriate vascular imaging and involve skull-base/neurovascular teams according to the threat.

Senior synthesis — if the pattern does not fit one nerve, do not force it into a familiar diagnosis. Verify the deficits, localize the shared corridor, image the full pathway with the modality that answers the anatomic question, and rescue threatened vision, cornea, airway, swallow or nutrition immediately. The board-level answer is localization; the resident-level answer is a reproducible exam plus pathway-directed imaging; the senior-level answer is recognizing when a benign label is invalid, when a function needs rescue, and when a potentially vascular lesion must not be blindly biopsied."""

TRAPS = [
    "Documenting 'cranial nerves intact' without testing palate, voice/vocal-fold function, tongue, trapezius/SCM, hearing, pupils, facial sensation and ocular motility.",
    "Calling progressive facial weakness Bell palsy despite additional cranial neuropathies.",
    "Using a normal routine noncontrast head CT to close a compelling skull-base localization.",
    "Ordering generic brain imaging that does not cover the full extracranial skull-base/nerve pathway.",
    "Missing corneal protection while waiting for the cause of facial paralysis.",
    "Ignoring aspiration, secretion failure or vocal-fold dysfunction during a lower-cranial-nerve workup.",
    "Confusing jugular-foramen IX-XI deficits with the broader IX-XII Collet-Sicard pattern.",
    "Missing carotid/parapharyngeal extension when lower cranial neuropathies are accompanied by sympathetic dysfunction.",
    "Treating painful ophthalmoplegia as a diagnosis rather than checking vision/pupils and localizing cavernous sinus versus orbital apex.",
    "Missing skull-base osteomyelitis in an at-risk patient with severe otalgia/headache and progressive neuropathies.",
    "Failing to consider malignancy/perineural spread in progressive unilateral multiple cranial neuropathies.",
    "Biopsying a pulsatile or vascular-appearing skull-base/carotid-space lesion before vascular characterization.",
    "Waiting for final pathology before protecting airway, swallow, nutrition, vision or cornea.",
    "Assuming a named skull-base syndrome establishes etiology rather than localization.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "explanation": "Progressive or multiple cranial neuropathies are a localization problem before they are a diagnostic label: map the shared skull-base corridor, protect threatened function, image the entire relevant pathway, and never blindly biopsy a potentially vascular lesion.",
    "board_pearl": "A normal routine head CT does not clear the skull base. IX-XII is the classic Collet-Sicard cluster; any additional cranial neuropathy makes an uncomplicated Bell-palsy label unsafe.",
    "depth_layers_v220": {
        "foundation":"Focused CN examination and cavernous-sinus/orbital-apex, CPA/IAC/temporal-bone, jugular-foramen/hypoglossal-canal localization including Collet-Sicard.",
        "application":"Choose MRI versus high-resolution CT versus vascular imaging by pathway; distinguish typical Bell palsy from skull-base infection, neoplasm and perineural spread.",
        "senior_decision":"Protect cornea/vision/airway/swallow/nutrition, avoid blind biopsy of vascular-appearing lesions, and escalate when the pattern is progressive, multiple or function-threatening."
    },
    "common_traps_v220": TRAPS,
    "deliberate_review_v220": "Promoted from the exact live residual backlog despite lower lexical rank because the prior answer under-taught a high-yield resident/board/emergency localization skill with immediate vision, airway, aspiration and vascular-biopsy consequences.",
    "source_refs_v220": SOURCE_REFS_V220,
    "evidence_distinction_v220": "Durable foraminal anatomy and localization are grounded in Cummings 7e, Pasha 6e and K.J. Lee 12e. Current management is separated explicitly: ACR cranial-neuropathy guidance informs pathway-directed imaging; the Bell-palsy no-routine-imaging rule is preserved only for a typical uncomplicated phenotype; current skull-base-osteomyelitis literature reinforces infection as an important multiple-neuropathy cause. No FDA drug/device indication governs this examination/localization concept.",
    "audit_profile_v220": "cranial_nerve_skull_base_localization",
}}

def apply_concept_check_task_alignment_v220(checks, deep_modules, v6_item_id):
    by={str(q.get("id") or ""):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
    for qid,p in COHORT.items():
        q=by.get(qid)
        if q is None: missing.append(qid); continue
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        persisted=q.get("concept_id")
        if m is None or topic!=p["canonical_topic"] or cid!=p["concept_id"] or (persisted is not None and persisted!=cid): link_mismatch.append(qid); continue
        q["concept_id"]=cid; q["canonical_topic"]=topic
        for field in ("prompt","answer_text","explanation","board_pearl","depth_layers_v220","common_traps_v220","deliberate_review_v220","source_refs_v220","evidence_distinction_v220","audit_profile_v220"): q[field]=p[field]
        q["choices"]=[]; q["answer"]=None; q["task_alignment_v220"]=True; repaired.append(qid)
    return {"repaired":repaired,"missing":missing,"link_mismatch":link_mismatch}
