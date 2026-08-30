"""v31.1 — source-grounded Acute Otitis Externa vs Necrotizing Otitis Externa rebuild.

Diffuse AOE owns the superficial EAC infection pathway: diagnosis, topical therapy,
drug delivery, TM-safety, and early reassessment. NOE owns invasive infection of the
EAC/lateral skull base: risk recognition, biopsy/culture, multimodal imaging, systemic
culture-directed therapy, cranial-neuropathy surveillance, and response assessment.
"""

import re

DOMAIN = "Otology / Neurotology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


OTITIS_EXTERNA_REBUILD_V311 = {
    "acute otitis externa": {
        "recognize": (
            "Recognize DIFFUSE acute otitis externa (AOE) as rapid-onset inflammation of the external auditory canal, usually with severe otalgia, pruritus/fullness and sometimes conductive hearing loss or otorrhea. The classic examination discriminator is pain with tragal or pinna manipulation plus diffuse canal edema/erythema and debris. Water exposure, canal trauma/cotton swabs, hearing aids/earbuds, eczema and loss of protective cerumen are common predisposing factors. Keep the taxonomy straight: a focal tender pustule/furuncle is localized follicular infection; fluffy fungal debris with prominent pruritus suggests otomycosis; neither should be collapsed into the diffuse bacterial AOE algorithm."
        ),
        "localize": (
            "Localize uncomplicated AOE to the SKIN/SOFT TISSUE of the EAC. Decide whether inflammation is diffuse, focal furunculosis, fungal, dermatitic/contact-related, or secondary to middle-ear drainage. Examine the pinna/periauricular skin for cellulitic extension and determine whether the tympanic membrane is intact; a tympanostomy tube, known perforation, or uncertain TM integrity changes drop selection. Diabetes, immunocompromise, prior radiation, severe pain out of proportion, granulation tissue, cranial neuropathy, or failure of appropriate topical therapy should trigger a separate invasive-disease question—NECROTIZING otitis externa—not simply 'bad swimmer's ear.'"
        ),
        "workup": (
            "Uncomplicated diffuse AOE is a CLINICAL diagnosis and usually needs no laboratory testing or imaging. Carefully clear enough debris to evaluate the canal/TM and ensure medication can reach infected skin. Routine culture is unnecessary in a straightforward first episode, but obtain culture when disease is recurrent, unusually severe, immunocompromised, treatment-refractory, or microbiology is otherwise uncertain. CT/MRI are not part of routine AOE workup. Reassess a patient who fails to improve within 48–72 hours: confirm the diagnosis, drop adherence and delivery, canal patency, fungal/contact dermatitis or middle-ear source, and reconsider NOE when the risk phenotype or pain trajectory is concerning."
        ),
        "manage": (
            "Treat uncomplicated diffuse AOE with adequate ANALGESIA plus TOPICAL therapy; systemic antibiotics should not be initial treatment unless infection extends beyond the canal or specific host factors require systemic management. Effective topical classes include antibiotic, antiseptic and antibiotic-steroid preparations; practical selection depends on TM status, allergy, cost, local practice and suspected organism. If the TM is perforated or a tympanostomy tube is present—or cannot be confidently excluded—use a NON-OTOTOXIC preparation rather than an aminoglycoside-containing drop. Keep the ear dry during active infection and stop canal trauma."
        ),
        "operate": (
            "The procedural skill in AOE is DRUG DELIVERY, not surgery. Perform atraumatic aural toilet when obstructing debris prevents examination or topical contact. When marked edema closes the canal, place an ear wick to carry drops to the medial canal and remove/reassess as swelling improves. Drain a true focal furuncle only when clinically appropriate rather than treating it as diffuse AOE. Persistent stenosis, abscess, periauricular extension, exposed bone/granulation, or cranial-nerve findings are escalation signals and should prompt reassessment for another diagnosis, particularly NOE, rather than repeated blind wick placement or oral antibiotics."
        ),
        "teach": (
            "Chief/boards framework: DIFFUSE AOE = TRAGAL/PINNA TENDERNESS + EAC EDEMA/ERYTHEMA -> analgesia + TOPICAL drops -> restore delivery with toilet/wick -> choose NON-OTOTOXIC drops if TM is nonintact -> reassess at 48–72 h if not improving. Do not reflexively prescribe oral antibiotics for canal-limited disease. Do not call every painful EAC process AOE: furunculosis is focal, otomycosis has a fungal/pruritic phenotype, and NECROTIZING OE is invasive skull-base disease requiring systemic evaluation and treatment."
        ),
        "tags": [
            "acute otitis externa", "diffuse otitis externa", "swimmer's ear", "tragal tenderness",
            "ear wick", "aural toilet", "topical antibiotic", "non-ototoxic drops", "tympanic membrane perforation"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — external auditory canal infections and differential diagnosis",
            "K.J. Lee's Essential Otolaryngology, 12e — disorders/infections of the external ear and canal",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — external ear disease and otitis externa management",
            "AAO-HNSF Clinical Practice Guideline: Acute Otitis Externa (Update), Otolaryngol Head Neck Surg 2014 — topical first-line therapy, systemic-antibiotic stewardship, drug delivery, non-ototoxic drops, and 48–72 h reassessment"
        ],
    },
    "necrotizing otitis externa": {
        "recognize": (
            "Recognize necrotizing otitis externa (NOE; historically 'malignant' OE) as an INVASIVE infection beginning in the EAC and extending into adjacent soft tissue and lateral skull base, potentially producing skull-base osteomyelitis and cranial neuropathies. The classic patient is older with diabetes or another impaired immune state and has deep, severe—often nocturnal—otalgia and persistent otorrhea despite appropriate local therapy. Canal edema and granulation tissue, classically near the bony-cartilaginous junction, increase concern but are not individually diagnostic. Facial weakness or lower cranial neuropathy signals advanced disease; absence of a neuropathy does not exclude NOE."
        ),
        "localize": (
            "Localize spread beyond superficial canal skin. Infection can track through fissures of Santorini and the tympanomastoid region into the lateral skull base, then toward the stylomastoid foramen, jugular foramen, petrous apex/clivus and central skull base. Perform and document a COMPLETE cranial-nerve examination, not only CN VII. Pseudomonas aeruginosa remains the most commonly isolated organism, but modern series include other gram-negative/gram-positive bacteria, fungi and culture-negative cases; therefore 'diabetic + Pseudomonas' is a useful prototype, not a sufficient case definition. EAC or skull-base malignancy can mimic NOE and must remain in the differential."
        ),
        "workup": (
            "NOE requires MULTIMODAL confirmation. Obtain EAC cultures before systemic antibiotics when feasible, but a negative culture does not exclude disease. Biopsy suspicious granulation/abnormal canal tissue when necessary to exclude squamous cell carcinoma or another malignancy and to obtain tissue microbiology. Check inflammatory markers such as ESR/CRP as useful longitudinal adjuncts and assess glucose/diabetes control and immune risk. CT best defines cortical bone erosion and temporal-bone anatomy; contrast MRI better maps marrow, soft-tissue, skull-base, intracranial and cranial-nerve involvement. The 2024 COSNOE Delphi consensus includes compatible canal findings/pain, microbiology, histology excluding malignancy, CT/MRI evidence, persistence despite treatment, immune-risk context and advanced-disease indicators as a standardized diagnostic framework—no single test should be treated as sufficient."
        ),
        "manage": (
            "Treat NOE as a serious skull-base infection with ENT plus infectious-disease collaboration when available, aggressive control of diabetes/immunologic contributors, meticulous local canal care, and PROLONGED SYSTEMIC culture-directed antimicrobial therapy with antipseudomonal coverage when empiric treatment is required. Route can be IV, oral high-bioavailability therapy, or sequential therapy depending on organism, severity, resistance, absorption and host factors; do not teach ciprofloxacin as an automatic one-drug answer in an era of resistance and non-Pseudomonas disease. Treatment commonly spans many weeks, but contemporary systematic review data do not support a universal fixed duration. Base cessation on the combined clinical course, inflammatory-marker trend and appropriate imaging/MDT assessment rather than an arbitrary calendar date."
        ),
        "operate": (
            "Surgery is SELECTIVE in NOE. Its major roles are obtaining diagnostic tissue/cultures, excluding malignancy, draining a focal collection, removing clearly sequestrated/devitalized tissue in selected refractory disease, and addressing complications. Routine radical temporal-bone debridement is not the default treatment for a disease primarily managed with systemic antimicrobials and host optimization. Follow worsening pain, granulation, cranial-nerve function, inflammatory markers and imaging carefully; radiographic bone abnormalities can lag behind clinical improvement, so an unchanged CT alone should not automatically trigger more surgery. New cranial neuropathy, intracranial extension, vascular complication or sepsis demands urgent escalation."
        ),
        "teach": (
            "Chief/boards framework: NOE = HIGH-RISK HOST + PERSISTENT/NOCTURNAL DEEP OTALGIA/OTORRHEA + GRANULATION OR OTHER EAC INFLAMMATION + EVIDENCE OF INVASIVE DISEASE -> culture/biopsy as indicated -> CT for bone + MRI for soft tissue/skull base -> prolonged SYSTEMIC culture-directed therapy + glucose/host optimization + serial CN/clinical response assessment. The key contrast with routine AOE is not merely 'more pain': AOE is superficial and topical-treatment driven; NOE is invasive and demands skull-base/malignancy evaluation. Pseudomonas is common but not obligatory, and cranial neuropathy is advanced disease rather than a required entry criterion."
        ),
        "tags": [
            "necrotizing otitis externa", "malignant otitis externa", "skull base osteomyelitis",
            "Pseudomonas", "diabetes", "granulation tissue", "cranial neuropathy", "CT temporal bone",
            "MRI skull base", "culture directed antibiotics", "COSNOE"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — necrotizing external otitis/skull-base infection, temporal-bone spread, cranial neuropathy, imaging and treatment",
            "K.J. Lee's Essential Otolaryngology, 12e — invasive external-ear infection and skull-base complications",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — malignant/necrotizing otitis externa diagnostic and treatment pearls",
            "COSNOE Delphi consensus study, J Laryngol Otol 2024 — consensus diagnostic criteria and advanced-disease reporting for necrotising otitis externa",
            "Takata et al., Clinical Otolaryngology 2023 — systematic review of NOE diagnosis/management, microbiology, treatment duration uncertainty and outcomes",
            "Ahmed et al., World J Otorhinolaryngol Head Neck Surg 2024 — contemporary multimodal diagnostic/imaging review"
        ],
    },
}


def apply_otitis_externa_rebuild_v311(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = OTITIS_EXTERNA_REBUILD_V311.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v311"] = True
        module["semantic_role_v311"] = (
            "superficial diffuse EAC infection with topical-treatment and drug-delivery decisions"
            if key == "acute otitis externa"
            else "invasive EAC/lateral-skull-base infection requiring systemic therapy and skull-base evaluation"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
