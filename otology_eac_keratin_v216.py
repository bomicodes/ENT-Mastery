"""v21.6 — canonical external-auditory-canal keratinizing disease closure.

Adds two genuinely missing Otology concepts as separate canonical modules:
External Auditory Canal Cholesteatoma and Keratosis Obturans. They are not
aliases for middle-ear cholesteatoma or acute otitis externa. Each receives a
six-layer curriculum module and a deliberate foundation -> application ->
senior_decision question ladder.
"""

DOMAIN = "Otology / Neurotology"

NEW_MODULES_V216 = [
    {
        "topic": "External Auditory Canal Cholesteatoma",
        "recognize": (
            "External auditory canal cholesteatoma (EACC) is focal accumulation of keratinizing squamous epithelium in the bony EAC with underlying osteitis, focal bony erosion, and sometimes sequestration. Patients commonly have chronic otorrhea, dull otalgia, conductive hearing loss, or an incidentally seen focal keratin pocket. The tympanic membrane and middle ear may initially be normal. EACC may be spontaneous or secondary to canal trauma, surgery, radiation, stenosis, or chronic obstruction."
        ),
        "localize": (
            "The defining process is in the external auditory canal rather than the tympanic membrane retraction pocket or middle ear. Disease often begins along one wall of the bony canal and erodes focally; inferior and posterior canal walls are common locations. Advanced disease can extend into mastoid air cells, temporomandibular joint region, facial nerve canal, or middle ear depending on location and extent."
        ),
        "workup": (
            "Microscopic otoscopy after careful debridement should define whether there is a focal keratin pocket, exposed bone, granulation, or sequestrum and whether the tympanic membrane is intact. High-resolution temporal-bone CT is useful when the full extent cannot be seen, symptoms are substantial, recurrent debris is difficult to clear, or there is concern for focal bony erosion, mastoid/middle-ear extension, facial canal involvement, or an alternative destructive process. Biopsy is appropriate when irregular soft tissue, disproportionate pain, or atypical erosion raises concern for squamous cell carcinoma or another mimic."
        ),
        "manage": (
            "Small accessible EACC without deep extension can sometimes be managed with meticulous microscopic debridement, dry-ear care, treatment of secondary infection, and serial surveillance. Persistent focal disease, progressive erosion, pain/drainage despite office care, canal stenosis, or disease that cannot be safely cleaned favors operative eradication. Unlike keratosis obturans, the management problem is not merely removing a circumferential plug; it is controlling a focal erosive epithelial process and restoring a self-cleaning canal."
        ),
        "operate": (
            "Surgery is tailored to extent. Limited disease may require transcanal removal with canalplasty and coverage of exposed bone using local skin, fascia, or grafting as appropriate. More extensive posterior disease may require a postauricular approach and mastoidectomy if mastoid air cells or middle ear are involved. Preserve facial nerve, temporomandibular joint capsule, tympanic membrane, ossicles, and healthy canal skin whenever possible; reconstruct the canal to reduce recurrent trapping."
        ),
        "teach": (
            "EACC is focal and erosive: keratin plus localized bony erosion/sequestration in the canal. That separates it from keratosis obturans, which classically produces a dense circumferential keratin plug with generalized smooth canal widening rather than focal osteitic destruction. A destructive canal lesion also demands a malignancy/NOE differential when the host, pain, or soft tissue is atypical."
        ),
        "tags": ["EAC cholesteatoma", "canal cholesteatoma", "keratin", "canal erosion", "canalplasty", "otoscopy", "temporal bone CT"],
        "source_basis": ["Cummings Otolaryngology", "Pasha Otolaryngology", "KJ Lee Otolaryngology"],
    },
    {
        "topic": "Keratosis Obturans",
        "recognize": (
            "Keratosis obturans is accumulation of a dense laminated keratin plug within the external auditory canal, typically causing marked otalgia, aural fullness, and conductive hearing loss. Removal may reveal a widened or ballooned bony canal with inflamed epithelium. It can be unilateral or bilateral and has reported associations with chronic sinus/pulmonary disease such as bronchiectasis, but the diagnosis rests on the canal phenotype rather than an associated condition."
        ),
        "localize": (
            "The process involves abnormal epithelial migration and keratin accumulation throughout the canal rather than a single focal erosive pocket. The canal may become diffusely and smoothly widened from chronic pressure. The tympanic membrane can be obscured by the plug but is not the primary site of disease. Focal sequestration and localized bone destruction should shift concern toward EACC or another destructive canal process."
        ),
        "workup": (
            "Diagnosis is usually made by otomicroscopy during careful removal of the keratin plug. Audiometry can document conductive loss when hearing symptoms are significant. CT is not required for every straightforward case, but is useful when debridement is incomplete, anatomy is atypical, there is focal erosion or granulation, recurrent severe disease, or concern for EACC, canal stenosis, malignancy, or middle-ear extension."
        ),
        "manage": (
            "The mainstay is meticulous removal of accumulated keratin under microscopy, often staged when the canal is exquisitely painful or inflamed, followed by topical anti-inflammatory treatment when indicated and scheduled aural toilet because recurrence is common. Avoid traumatic blind removal that strips canal epithelium. Patients with recurrent disease need a long-term cleaning plan rather than repeated treatment as bacterial otitis externa."
        ),
        "operate": (
            "Most keratosis obturans is managed nonoperatively with serial debridement. Canalplasty or meatoplasty is reserved for unusual refractory cases in which anatomic narrowing, repeated severe accumulation, or inability to maintain a clean self-draining canal defeats conservative care. The presence of true focal bony necrosis/erosion should prompt reconsideration of the diagnosis before labeling the case refractory keratosis obturans."
        ),
        "teach": (
            "Keratosis obturans is plug-and-widening disease; EACC is focal erosion disease. Both contain keratin and can cause conductive loss, so the distinction comes from the canal wall after the debris is removed: diffuse smooth widening favors keratosis obturans, while localized osteitis, sequestration, or a focal crater favors EACC."
        ),
        "tags": ["keratosis obturans", "keratin plug", "external auditory canal", "conductive hearing loss", "aural toilet", "otoscopy"],
        "source_basis": ["Cummings Otolaryngology", "Pasha Otolaryngology", "KJ Lee Otolaryngology"],
    },
]


def _q(qid, topic, stage, stem, choices, answer, explanation, reasons, pearl, curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic,
        "learning_stage": stage, "stem": stem, "choices": choices,
        "answer": answer, "explanation": explanation, "why_wrong": reasons,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette",
        "focus": focus, "ladder_reviewed": True,
    }


VIGNETTES_V216 = [
    _q(
        "v216_oto_eacc_found", "External Auditory Canal Cholesteatoma", "foundation",
        "A patient has chronic unilateral otorrhea and dull otalgia. After microscopic debridement, a focal keratin-filled crater with exposed eroded bone is seen along the posterior bony external auditory canal; the tympanic membrane is intact. What diagnosis best fits?",
        ["External auditory canal cholesteatoma", "Keratosis obturans", "Diffuse acute otitis externa", "Middle-ear cholesteatoma"], 0,
        "A focal keratinizing lesion of the bony EAC with localized osteitis or erosion is classic for EACC. The intact tympanic membrane and focal canal-wall disease localize the process outside the middle ear.",
        ["Correct. Focal canal keratin plus localized bony erosion is the defining pattern.", "Keratosis obturans more often forms a dense circumferential plug with generalized smooth canal widening rather than a focal erosive crater.", "AOE produces diffuse inflamed canal skin and debris, not a chronic focal keratin pocket with bone erosion.", "Middle-ear cholesteatoma arises medial to the tympanic membrane/retraction pathway rather than as an isolated bony canal-wall crater."],
        "For canal keratin disease, look at the bone after the debris is removed: focal erosion points toward EACC.",
        "What CT pattern would support EACC and what findings would make you biopsy for canal carcinoma?"
    ),
    _q(
        "v216_oto_eacc_app", "External Auditory Canal Cholesteatoma", "application",
        "A patient thought to have recurrent otitis externa has repeated focal keratin accumulation in the inferior EAC. CT shows a localized bony defect with small sequestra but no mastoid or middle-ear extension. Which management best matches the mechanism?",
        ["Long-term oral antipseudomonal therapy as the definitive treatment", "Canal-wall-focused management with meticulous debridement and surveillance if fully accessible, escalating to limited canalplasty/eradication if recurrent or not safely maintainable", "Epley maneuver", "Routine canal-wall-down mastoidectomy for every case"], 1,
        "Localized EACC is an erosive epithelial disease. Accessible limited lesions may be controlled with repeated microscopic cleaning and dry-ear care, while persistent/recurrent disease or an inaccessible bony pocket may require canalplasty and removal of diseased epithelium/bone. Extent—not the word cholesteatoma alone—determines whether mastoid surgery is needed.",
        ["Systemic antipseudomonal therapy treats invasive infection such as NOE, not a localized keratinizing epithelial pocket without that phenotype.", "Correct. Treatment should eliminate trapped keratin and the focal diseased canal while preserving normal canal function.", "A vestibular repositioning maneuver has no role in external-canal disease.", "Mastoidectomy is unnecessary when imaging confirms disease is confined to a limited accessible EAC segment."],
        "EACC surgery is extent-driven: do not turn a focal canal lesion into a mastoid operation unless the disease actually extends there.",
        "Which posterior canal-wall extension would make a postauricular approach or mastoidectomy more appropriate?", "OR_prep"
    ),
    _q(
        "v216_oto_eacc_snr", "External Auditory Canal Cholesteatoma", "senior_decision",
        "An older patient with presumed EACC has worsening deep pain, friable granulation tissue, and progressive irregular canal erosion despite serial cleaning. The lesion now appears more like soft tissue than a simple keratin pocket. What is the best attending-level decision?",
        ["Continue debridement indefinitely because all focal canal erosion is benign EACC", "Start chronic topical steroid alone", "Obtain tissue diagnosis and re-stage the destructive canal process for squamous cell carcinoma and invasive infection rather than anchoring on EACC", "Perform stapedotomy"], 2,
        "EACC is an important benign erosive diagnosis, but progressive pain, friable mass-like tissue, or irregular destructive behavior should reopen the differential. EAC squamous cell carcinoma and necrotizing infection can mimic or coexist with keratinizing canal disease; biopsy and appropriate imaging are required when the phenotype changes.",
        ["Therapeutic inertia can delay recognition of a malignant or invasive mimic.", "Steroid monotherapy neither diagnoses nor controls a destructive mass-like canal lesion.", "Correct. Senior judgment means abandoning the benign label when the clinical behavior no longer fits it.", "Stapes surgery does not address an external-canal destructive lesion."],
        "A benign diagnosis must keep earning its benign behavior; progressive destructive soft tissue deserves biopsy.",
        "How do diabetes, cranial neuropathy, and skull-base marrow change the differential between EACC, NOE, and EAC carcinoma?", "overnight_call"
    ),
    _q(
        "v216_oto_ko_found", "Keratosis Obturans", "foundation",
        "A patient presents with severe ear pain, fullness, and conductive hearing loss. Microscopy reveals a dense circumferential laminated keratin plug. After careful removal, the bony canal is diffusely widened without a focal erosive crater. What diagnosis best fits?",
        ["External auditory canal cholesteatoma", "Keratosis obturans", "Otosclerosis", "Necrotizing otitis externa"], 1,
        "A dense circumferential keratin plug with generalized smooth canal widening is the classic keratosis-obturans phenotype. The lack of focal osteitic erosion distinguishes it from EACC.",
        ["EACC is more characteristically focal with localized bone erosion or sequestration.", "Correct. Plug formation plus diffuse canal widening is the key pattern.", "Otosclerosis causes conductive loss behind a normal canal and tympanic membrane, not a keratin plug.", "NOE is an invasive infection in a high-risk host with disproportionate pain, granulation, and potentially skull-base extension rather than a simple laminated keratin plug."],
        "Keratosis obturans fills and widens the canal; EACC focally erodes it.",
        "Why can the first debridement be difficult and how should you avoid iatrogenic canal injury?"
    ),
    _q(
        "v216_oto_ko_app", "Keratosis Obturans", "application",
        "A patient with confirmed keratosis obturans returns every few months with recurrent dense keratin accumulation but has no focal bone erosion, granulation mass, or middle-ear disease. What is the most appropriate long-term plan?",
        ["Schedule repeated microscopic aural toilet at an interval matched to recurrence, with topical treatment for canal inflammation when needed", "Treat each recurrence as bacterial otitis externa with systemic antibiotics", "Perform canal-wall-down mastoidectomy", "Observe without cleaning until complete canal obstruction recurs"], 0,
        "Keratosis obturans commonly requires longitudinal mechanical control because abnormal epithelial migration and recurrent keratin accumulation persist. Scheduled microscopic cleaning prevents painful complete obstruction and avoids unnecessary antibiotics or major ear surgery.",
        ["Correct. Maintenance debridement is the core management strategy for recurrent uncomplicated disease.", "Keratin recurrence without infectious findings is not evidence of repeated bacterial OE.", "There is no mastoid target in uncomplicated keratosis obturans.", "Waiting for complete re-obstruction recreates avoidable pain and conductive loss and makes debridement harder."],
        "For recurrent keratosis obturans, maintenance cleaning is treatment—not evidence that treatment failed.",
        "When would canalplasty become reasonable despite the usual nonoperative management?"
    ),
    _q(
        "v216_oto_ko_snr", "Keratosis Obturans", "senior_decision",
        "During follow-up for presumed keratosis obturans, the next debridement reveals a new localized posterior canal-wall crater with exposed necrotic bone rather than the prior smooth circumferential widening. What is the best senior-level interpretation?",
        ["This is an expected stage of keratosis obturans and requires no diagnostic change", "The finding proves middle-ear cholesteatoma", "Treat with vestibular suppressants", "Reconsider the diagnosis for EACC or another focal destructive canal process and obtain extent-defining evaluation as appropriate"], 3,
        "Keratosis obturans should not produce a new focal osteitic crater as its defining pattern. Localized bony erosion or sequestration should shift the diagnostic frame toward EACC, and irregular granulation or disproportionate pain should additionally raise concern for malignancy or invasive infection.",
        ["Diffuse smooth widening and recurrent plug formation are expected; a focal necrotic crater is a different morphologic process.", "The lesion remains in the external canal; middle-ear cholesteatoma is not established without tympanic/middle-ear disease.", "Vestibular suppressants do not address an external-canal bony lesion.", "Correct. The morphology has changed from plug disease to focal destructive disease, so the diagnosis and workup must change with it."],
        "The EACC-versus-KO distinction is dynamic: if the bone pattern changes, the diagnosis should change too.",
        "What temporal-bone CT findings separate smooth canal expansion from focal EACC erosion and mastoid extension?", "boards"
    ),
]


def apply_otology_eac_keratin_v216(data):
    modules = data.DEEP_MODULES_V6.setdefault(DOMAIN, [])
    existing_topics = {m.get("topic") for m in modules if m.get("topic")}
    added_topics = []
    for module in NEW_MODULES_V216:
        if module["topic"] not in existing_topics:
            modules.append(dict(module))
            existing_topics.add(module["topic"])
            added_topics.append(module["topic"])

    challenges = data.CLINICAL_CHALLENGES_V119
    existing_ids = {q.get("id") for q in challenges if q.get("id")}
    added_questions = []
    for question in VIGNETTES_V216:
        if question["id"] in existing_ids:
            continue
        item = dict(question)
        item["concept_id"] = data._v6_item_id(DOMAIN, item["topic"])
        challenges.append(item)
        existing_ids.add(item["id"])
        added_questions.append(item["id"])

    return {
        "added_topics": added_topics,
        "added_questions": added_questions,
        "otology_topic_count": len([m for m in modules if m.get("topic")]),
    }
