"""v20.32 exact-live Cleft / Craniofacial Otologic-Airway Care depth cohort.

Rehomed from the superseded pre-v20.31 cleft draft after production v20.31 was assigned to
Rhinology AR/LAR. Durable anatomy/operative principles are cross-referenced to the user's
connected Cummings 7e, Pasha 6e and K.J. Lee 12e copies. Current management is separated from
those durable principles and anchored to 2024 ACPA Parameters, 2026 ACPA team standards,
AAO-HNSF tympanostomy-tube guidance and peer-reviewed evidence through 2026.
"""
from copy import deepcopy
from concept_check_board_repair_v177 import _find_module

QIDS = ["cc-v112-rec-pediatric-otolaryngology-cleft-craniofacial-otologic-airway-care"]
CID = "v6-pediatric-otolaryngology-cleft-craniofacial-otologic-airway-care"
TOPIC = "Cleft / Craniofacial Otologic-Airway Care"

PROMPT = (
    "A child with cleft palate or another craniofacial difference presents across infancy and childhood with middle-ear effusion, "
    "conductive hearing loss, sleep-disordered breathing, feeding concerns, or an upcoming airway/palatal procedure. How should an "
    "ENT resident connect palatal and craniofacial anatomy to Eustachian-tube dysfunction and airway risk; decide when audiology, "
    "tympanostomy tubes, sleep/airway evaluation, or operative intervention is appropriate; avoid velopharyngeal harm from adenoid "
    "surgery; and recognize the airway, hearing, developmental, and multidisciplinary problems that require senior escalation?"
)

ANSWER = r'''Cleft and craniofacial ENT care is a **longitudinal airway-hearing-speech problem**, not a one-operation diagnosis. Repeatedly ask: **Is the airway safe? Is hearing adequate for language development? Is the velopharyngeal mechanism being protected? Is care coordinated with the cleft/craniofacial team?**

**Foundation — anatomy explains the ear and changes the airway.** In cleft palate, abnormal levator veli palatini sling formation and abnormal tensor veli palatini orientation/function impair active Eustachian-tube opening. The consequence is persistent negative middle-ear pressure, OME, conductive loss, retraction, adhesive disease and cholesteatoma risk. Palatal repair improves anatomy but does **not** guarantee normalization of Eustachian-tube physiology, so otologic surveillance continues after repair. Craniofacial diagnoses can independently alter airway geometry: Robin-sequence micrognathia/glossoptosis, midface hypoplasia, choanal/nasal obstruction, adenotonsillar tissue, syndromic hypotonia and prior pharyngeal surgery may coexist. A cleft does not identify the level of obstruction; localize before operating.

**Application — treat hearing as a developmental vital sign.** Use age-appropriate audiology plus otoscopy/tympanometry instead of waiting for subjective hearing complaints. Cleft palate is an AAO-HNSF 'at-risk' context for developmental difficulty. Tympanostomy tubes may be offered when OME is present and likely to persist, but this is not a mandate for universal prophylactic tubes. Integrate persistence of effusion, hearing level, tympanic-membrane disease, speech/language vulnerability, prior tube history, anesthesia opportunities and reliable follow-up. The practical rule is **aggressive surveillance with a low threshold for indicated ventilation**, not 'every cleft equals automatic tubes' and not a rigid three-month wait regardless of developmental risk.

Repeated tubes have costs: otorrhea, tympanosclerosis, granulation, persistent perforation and additional procedures. A 2026 cohort of 278 children reported tube-related complications in about 21% and repeat tube insertion in about 42%; use those figures for counseling, not as universal center-independent rates. Persistent conductive loss after ventilation requires reassessment for retraction, perforation, ossicular disease or cholesteatoma rather than assuming recurrent fluid. Disproportionate chronic ear disease in apparently isolated cleft lip should also prompt consideration of occult/submucous cleft.

**Current evidence boundary — anatomy does not guarantee surgical physiology.** Tensor veli palatini is central to normal Eustachian-tube opening, but a 2026 randomized trial of 81 nonsyndromic children undergoing Furlow palatoplasty found that adding tensor veli palatini tenopexy did **not** improve longitudinal OME outcomes. Do not convert correct tensor anatomy into a claim that tensor manipulation reliably normalizes middle-ear disease. Likewise, a 2026 41-child retrospective comparison of routine versus selective ventilation tubes during palatoplasty found no significant difference in hearing, re-tympanostomy or complications; the authors favored routine placement, but the study does not establish a universal mandate.

**Application — airway triage starts in infancy.** A neonate with micrognathia/glossoptosis, increased work of breathing, desaturation, cyanotic spells, feeding failure or poor growth needs prompt airway assessment. Positioning or nasopharyngeal-airway support may be sufficient in selected Robin-sequence infants; persistent clinically important obstruction can require objective sleep/airway assessment and multidisciplinary escalation to tongue-lip adhesion, mandibular distraction or tracheostomy depending on obstruction level, severity, syndrome, feeding/aspiration status and institutional expertise. The senior decision is not 'small jaw = distraction.' Determine whether obstruction is tongue-base predominant, whether additional levels exist, whether nonoperative support works, and whether the infant can feed and grow safely.

**Sleep and adenoid decisions must protect the velopharynx.** In a craniofacial child, polysomnography is especially useful when symptoms and examination disagree, anatomy suggests multilevel disease, or the result will change perioperative planning. Before adenoid surgery, look for overt/submucous cleft, short palate, poor palatal motion, prior VPI, hypernasality or nasal regurgitation. Complete adenoidectomy can unmask or worsen VPI. If adenoid tissue materially contributes to obstruction and VPI risk is high, a deliberately limited/superior-partial approach may be considered in selected patients; it is a compromise, not a guarantee against postoperative VPI.

**Secondary VPI surgery creates an airway-speech tradeoff.** Hypernasality after cleft repair requires perceptual speech assessment plus structural/functional evaluation; nasopharyngoscopy and/or multiview videofluoroscopy can define closure pattern and gap. Pharyngeal flap, sphincter pharyngoplasty and palatal-lengthening procedures can improve speech in selected anatomy but may create or worsen OSA. Conversely, OSA after a VPI operation requires assessment of the reconstruction and other obstruction levels; do not dismantle a speech operation reflexively, but do not preserve resonance at the expense of clinically important airway compromise.

**Feeding and airway safety intersect.** Specialized feeding systems are often needed because infants with cleft palate cannot generate normal suction. Failure to thrive should not automatically be attributed to cleft mechanics when airway obstruction, aspiration, cardiac disease, neurologic disease or syndromic pathology may contribute. Coughing/choking, recurrent pneumonia, wet respirations, prolonged feeds, desaturation with feeding or poor growth should trigger targeted swallowing/airway evaluation.

**Senior perioperative decision.** Craniofacial syndromes can add difficult mask ventilation/intubation, choanal stenosis, midface deficiency, cervical-spine issues, cardiac disease and prior airway reconstruction. Review prior anesthetic records, current airway symptoms, sleep data and previous airway operations. If difficult ventilation or intubation is plausible, define a primary and rescue airway plan before induction rather than discovering the anatomy after loss of spontaneous ventilation.

**Synthesis:** identify the craniofacial diagnosis and palatal anatomy -> screen airway, feeding, sleep, hearing and speech -> obtain age-appropriate audiology and objective sleep/airway testing when it will change management -> ventilate the middle ear when OME/hearing/developmental risk warrants -> continue surveillance after palatal repair -> localize airway obstruction before choosing an operation -> protect velopharyngeal function during adenoid/pharyngeal surgery -> anticipate difficult-airway rescue -> coordinate longitudinally with the cleft/craniofacial team.'''

TRAPS = [
    "Stopping otologic surveillance because the palate has been repaired.",
    "Waiting for caregivers to notice hearing loss rather than scheduling age-appropriate audiology.",
    "Treating cleft palate as an automatic lifelong indication for prophylactic tympanostomy tubes.",
    "Applying a rigid three-month OME wait to a developmentally at-risk child without considering earlier intervention.",
    "Assuming conductive loss after tubes is still fluid without reassessing chronic tympanic-membrane or ossicular disease.",
    "Ignoring retraction pockets and cholesteatoma because middle-ear disease is expected in cleft palate.",
    "Missing occult/submucous cleft in isolated cleft lip with disproportionate chronic middle-ear disease.",
    "Assuming tensor veli palatini tenopexy normalizes Eustachian-tube function because the anatomy is mechanistically plausible.",
    "Equating micrognathia with an automatic indication for mandibular distraction without localizing obstruction.",
    "Assuming Robin-sequence obstruction is always single-level tongue-base collapse.",
    "Ignoring feeding failure and growth trajectory during neonatal craniofacial airway assessment.",
    "Treating syndromic snoring as benign when objective sleep assessment would change management.",
    "Performing complete adenoidectomy without screening for VPI risk or occult palatal dysfunction.",
    "Calling partial adenoidectomy risk-free for VPI rather than a selected compromise.",
    "Choosing VPI surgery by procedure name rather than closure pattern, gap, speech findings and airway risk.",
    "Ignoring new or worsened OSA after pharyngeal flap or sphincter surgery because speech improved.",
    "Dismantling a VPI reconstruction reflexively for OSA without evaluating other obstruction levels and speech consequences.",
    "Attributing failure to thrive entirely to cleft feeding mechanics while missing airway obstruction or aspiration.",
    "Using a textbook palatoplasty age as a rigid deadline rather than integrating growth, airway and team protocol.",
    "Inducing anesthesia in a syndromic craniofacial child without a shared difficult-airway rescue plan.",
]

SOURCE_REFS_V232 = [
    {"type":"textbook","citation":"Cummings Otolaryngology–Head and Neck Surgery, 7th ed. (2021). Connected Google Drive full-volume ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t. Rechecked 2026-09-13 for craniofacial/cleft airway, hearing and durable operative-anatomy foundations."},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology–Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022). Connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Rechecked 2026-09-13 for cleft classification/repair, Eustachian-tube dysfunction, chronic middle-ear disease, VPI risk and pediatric airway principles."},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology, 12th ed. (2019). Connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Rechecked 2026-09-13 for levator/tensor anatomy, cleft-associated Eustachian-tube dysfunction, OME surveillance and craniofacial-airway foundations."},
    {"type":"society","citation":"American Cleft Palate Craniofacial Association. Parameters of Care for Evaluation and Treatment of Individuals with Cleft Lip/Palate and/or Other Craniofacial Differences, revised 2024. Longitudinal sections include airway/breathing, ears/Eustachian tube/hearing, feeding/growth, sleep, speech and surgery."},
    {"type":"society","citation":"American Cleft Palate Craniofacial Association. Standards for Approval of Cleft Palate and Craniofacial Teams, revised 2026 and released May 4, 2026 to align with the 2024 Parameters; supports coordinated interdisciplinary team care."},
    {"type":"guideline","citation":"Rosenfeld RM et al. Clinical Practice Guideline: Tympanostomy Tubes in Children (Update). Otolaryngol Head Neck Surg. 2022;166(1_suppl):S1-S55. Cleft palate is an at-risk developmental context; tube decisions remain individualized to persistent OME/hearing-development risk."},
    {"type":"systematic_review","citation":"Stanton E et al. Tympanostomy Tubes: Are They Necessary? A Systematic Review on Implementation in Cleft Care. Cleft Palate Craniofac J. 2023;60(4):430-445. PMID 35044261. Supports uncertainty around universal prophylactic versus selective tube strategies."},
    {"type":"randomized_trial","citation":"Alper CM et al. Tensor Veli Palatini Muscle Tenopexy During Furlow Palatoplasty Fails to Improve Otologic Outcomes. Cleft Palate Craniofac J. 2026 Apr 3. PMID 41930721; DOI 10.1177/10556656261438891. Randomized 81 children; added tensor tenopexy did not improve longitudinal OME outcomes."},
    {"type":"peer_reviewed","citation":"Bachini S et al. Hearing and Otologic Outcomes After Routine Versus Selective Ventilation Tube Insertions in Children With Cleft Palate. Cleft Palate Craniofac J. 2026 May 29. PMID 42213516; DOI 10.1177/10556656261450120. Forty-one-child retrospective cohort; no significant differences in hearing, re-tympanostomy or complications; not a universal mandate."},
    {"type":"peer_reviewed","citation":"Complications of tympanostomy tubes in patients with cleft palate. 2026. PMID 42266256. Retrospective 278-child cohort; tube-related complications 21% and repeat tubes 42%, useful for counseling rather than universal rates."},
    {"type":"peer_reviewed","citation":"The presence of a submucous cleft palate in patients with isolated cleft lip and middle ear dysfunction. 2024. PMID 38604103. Disproportionate middle-ear disease can signal occult submucous cleft."},
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "depth_layers_v232": {
        "foundation": "Cleft-palate levator/tensor anatomy, Eustachian-tube dysfunction, craniofacial airway geometry, hearing/speech development and velopharyngeal competence.",
        "application": "Longitudinal audiology/OME surveillance, individualized tympanostomy tubes, airway/sleep localization, feeding assessment and VPI-aware adenoid/pharyngeal decisions.",
        "senior_decision": "Balance hearing-development benefit against repeated-tube morbidity, localize multilevel airway obstruction, protect speech/velopharyngeal function, anticipate difficult-airway rescue and coordinate multidisciplinary escalation.",
    },
    "common_traps_v232": TRAPS,
    "deliberate_review_v232": {"priority":"high","review_after_days":[1,7,21,60],"reason":"high-yield pediatric ENT integration of chronic ear disease, developmental hearing, neonatal/operative airway risk, sleep surgery and velopharyngeal complications"},
    "source_refs_v232": SOURCE_REFS_V232,
    "evidence_distinction_v232": "Durable textbook anatomy and operative foundations are retained. Current management is updated with 2024 ACPA Parameters, 2026 ACPA team standards and 2022 AAO-HNSF tympanostomy guidance. Universal prophylactic tube timing, exact palatoplasty timing, tensor-tenopexy otologic benefit and any one Robin-sequence airway operation are not taught as universal. The 2026 randomized tensor-tenopexy trial and routine-versus-selective tube cohort refine current decision-making without replacing guideline- and phenotype-based care.",
    "task_alignment_v232": True,
}}


def apply_concept_check_task_alignment_v232(checks, deep_modules, v6_item_id):
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
        q["concept_id"] = patch["concept_id"]
        q["prompt"] = patch["prompt"]
        q["question"] = patch["prompt"]
        q["answer_text"] = patch["answer_text"]
        q["choices"] = []
        q.pop("answer", None)
        for field in ("depth_layers_v232", "common_traps_v232", "deliberate_review_v232", "source_refs_v232", "evidence_distinction_v232", "task_alignment_v232"):
            q[field] = deepcopy(patch[field])
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
