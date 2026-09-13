"""v20.31 exact-live Cleft / Craniofacial Otologic-Airway Care depth cohort.

Durable cleft-palate, velopharyngeal, Eustachian-tube and craniofacial-airway principles are
cross-referenced to Cummings 7e, Pasha 6e and K.J. Lee 12e in the user's connected Google Drive.
Current management is anchored to the 2024 ACPA Parameters of Care, 2026 ACPA team standards,
AAO-HNSF tympanostomy-tube guidance, and contemporary peer-reviewed cleft otology evidence.
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

ANSWER = r'''Cleft and craniofacial ENT care is a **longitudinal airway-hearing-speech problem**, not a one-operation diagnosis. The resident should repeatedly ask four questions: **Is the airway safe? Is hearing adequate for language development? Is the velopharyngeal mechanism being protected? Is care coordinated with the cleft/craniofacial team?** The answers change with growth, palatal repair, craniofacial anatomy, sleep symptoms, speech development and prior operations.

**1. Start with anatomy because it explains both the ear and the airway.** In cleft palate, the levator veli palatini does not form a normal transverse sling and tensor veli palatini orientation/function may be abnormal. This impairs active Eustachian-tube opening, promoting negative middle-ear pressure, chronic otitis media with effusion (OME), conductive hearing loss, tympanic-membrane retraction and, over years, adhesive disease or cholesteatoma. Palatal repair reconstructs anatomy but does **not** guarantee immediate normalization of Eustachian-tube function; otologic surveillance must continue after repair.

Craniofacial diagnoses also alter airway geometry. Micrognathia/glossoptosis in Robin sequence, midface hypoplasia, choanal/nasal obstruction, adenotonsillar tissue, obesity, syndromic hypotonia, prior pharyngeal surgery and craniosynostosis-related anatomy can contribute separately or together. A cleft does not itself tell you the level of obstruction. Localize the problem before recommending surgery.

**2. Treat hearing as a developmental vital sign.** Nearly every child with cleft palate will experience substantial Eustachian-tube dysfunction/OME risk. Perform age-appropriate audiologic surveillance and otoscopy/tympanometry rather than waiting for a parent to report hearing loss. Speech-language delay can reflect conductive loss, velopharyngeal dysfunction, articulation disorder, developmental disease, or several of these simultaneously.

The current AAO-HNSF tympanostomy-tube framework allows tube placement in children who are **at risk for developmental difficulty** when OME is present and unlikely to resolve quickly; cleft palate and craniofacial disorders are specifically recognized risk contexts. This does not mean every child receives automatic prophylactic tubes forever. Integrate persistence of effusion, hearing status, tympanic-membrane disease, speech/language vulnerability, prior tube history, anesthesia opportunities and family-centered follow-up.

Many cleft programs place tubes at the time of palatoplasty when OME/hearing risk supports intervention, while others use selective strategies. The literature remains heterogeneous, and the 2023 systematic review of cleft-care tube implementation did not justify converting local practice variation into a universal rule. Current teaching should therefore be **aggressive surveillance with a low threshold for indicated ventilation**, not 'every cleft equals mandatory tubes' and not 'wait three months regardless of developmental risk.'

**3. Know what repeated tubes can cost.** Recurrent OME and repeat tube placement are common. Counsel about otorrhea, tympanosclerosis, granulation, persistent perforation and the possibility of repeated procedures. A 2026 cohort of 278 children with cleft palate reported tube-related complications in about one fifth and repeat tube insertion in roughly two fifths; that is useful for counseling but does not establish a universal complication rate for every center or tube strategy. Chronic retraction, perforation, ossicular disease or cholesteatoma changes the problem from simple ventilation to otologic disease management.

Do not assume persistent conductive loss is always fluid. Re-examine the tympanic membrane, obtain audiology and consider ossicular/structural disease when hearing does not improve as expected after ventilation. Likewise, isolated cleft lip plus unexplained chronic middle-ear disease should raise suspicion for an occult/submucous cleft or another palatal abnormality rather than reflexively labeling the child 'just otitis-prone.'

**4. Airway triage begins in infancy.** A neonate with micrognathia/glossoptosis, increased work of breathing, desaturation, cyanotic spells, feeding failure or poor growth needs prompt airway assessment. Positioning and nasopharyngeal airway support may be sufficient in selected Robin-sequence infants, while persistent clinically important obstruction may require objective sleep/airway assessment and multidisciplinary escalation to options such as tongue-lip adhesion, mandibular distraction osteogenesis, or tracheostomy depending on anatomy, severity, associated syndromes, feeding/aspiration issues and institutional expertise. No single operation is appropriate for every Robin-sequence infant.

The senior decision is not simply 'small jaw = distraction.' Determine whether obstruction is tongue-base predominant, whether additional levels of obstruction exist, whether nonoperative support is effective, whether the infant can feed and grow safely, and whether the syndrome predicts a more complex airway. Flexible endoscopy, sleep evaluation and/or direct airway assessment should be chosen according to the clinical question and severity.

**5. Sleep-disordered breathing later in childhood requires the same localization discipline.** Snoring in a craniofacial child deserves attention, especially with witnessed apneas, gasping, daytime neurobehavioral symptoms, growth problems, pulmonary hypertension risk, prior pharyngeal surgery or syndromic disease. Polysomnography is particularly useful when symptoms and examination disagree, when craniofacial anatomy makes the obstruction multilevel/complex, or when the result will change perioperative planning.

Adenotonsillar hypertrophy may contribute, but surgery must respect velopharyngeal anatomy. **Adenoidectomy can unmask or worsen velopharyngeal insufficiency (VPI)** in a patient with overt or submucous cleft, short palate, poor palatal motion, prior VPI, hypernasality or nasal regurgitation. Before adenoid surgery, examine the palate, speech/resonance history and prior cleft/VPI operations. When adenoid tissue is materially contributing to obstruction and VPI risk is high, a deliberately limited/superior-partial approach may be considered in selected patients rather than routine complete adenoidectomy. This is a mechanism-specific compromise, not a guarantee against postoperative VPI.

**6. Protect the velopharynx when solving airway problems.** A child with hypernasal speech after cleft repair needs perceptual speech assessment and a structural/functional evaluation rather than automatic adenoidectomy, tonsillectomy or pharyngeal surgery. Nasopharyngoscopy and/or multiview videofluoroscopy can define closure pattern and gap when secondary VPI surgery is being considered. Pharyngeal flap, sphincter pharyngoplasty and palatal-lengthening procedures can improve speech in selected anatomy but may narrow the airway and create or worsen OSA. Preoperative sleep symptoms and postoperative airway surveillance matter.

Conversely, treating OSA in a patient who already has a pharyngeal flap or other VPI operation requires awareness that the prior reconstruction may be contributing to obstruction. Do not dismantle a speech operation casually, but do not ignore clinically important airway compromise to preserve resonance at all costs. The decision belongs in a cleft/craniofacial team with speech, sleep/airway and surgical expertise.

**7. Feeding and airway safety intersect.** Infants with cleft palate often need specialized feeding systems because they cannot generate normal suction. Failure to thrive should not be attributed automatically to the cleft if there are signs of airway obstruction, aspiration, cardiac disease, neurologic disease or a syndromic diagnosis. Coughing/choking, recurrent pneumonia, wet respirations, prolonged feeds, oxygen desaturation with feeding or poor weight gain should prompt a targeted swallowing/airway evaluation.

Palatal repair timing is coordinated around speech development, growth, airway safety and the cleft team's protocol rather than a rigid board-exam age. Textbooks commonly describe repair in later infancy (roughly around the first year of life), but current ACPA care emphasizes individualized, interdisciplinary planning. Durable anatomy and developmental goals remain valid; exact timing is program- and patient-specific.

**8. Craniofacial syndromes change the perioperative airway plan.** Treacher Collins, Apert/Crouzon-spectrum craniosynostosis, 22q11-related palatal disease, Stickler-associated Robin sequence and other syndromes can add difficult mask ventilation/intubation, cervical-spine issues, choanal stenosis, midface deficiency, cardiac disease, hearing loss and developmental considerations. Review prior anesthetic records, current airway symptoms, sleep data and prior airway operations. If difficult ventilation or intubation is plausible, establish a shared primary and rescue airway plan before induction rather than discovering the anatomy after loss of spontaneous ventilation.

**9. Senior-resident synthesis.** The useful longitudinal algorithm is: **identify the craniofacial diagnosis and palatal anatomy -> screen airway, feeding, sleep, hearing and speech -> obtain age-appropriate audiology and objective sleep/airway testing when it will change management -> ventilate the middle ear when OME/hearing/developmental risk warrants it -> continue surveillance after palatal repair -> localize airway obstruction before choosing an operation -> protect velopharyngeal function when considering adenoid/pharyngeal surgery -> anticipate difficult-airway rescue -> keep the cleft/craniofacial team responsible for longitudinal coordination.**

The quality endpoint is not 'the palate is repaired' or 'the tubes are in.' It is safe breathing and feeding, developmentally adequate hearing, intelligible speech with competent velopharyngeal function, prevention of chronic ear disease, and a perioperative airway plan that remains safe as the child grows.'''

TRAPS = [
    "Assuming palatal repair permanently normalizes Eustachian-tube function and stopping otologic surveillance.",
    "Waiting for a parent to notice hearing loss instead of using scheduled age-appropriate audiology in a high-risk child.",
    "Treating every cleft child with automatic prophylactic tubes regardless of current ear/hearing findings or prior complications.",
    "Applying a rigid three-month OME waiting rule to a developmentally at-risk cleft/craniofacial child without considering earlier intervention.",
    "Assuming persistent conductive loss after tubes is still fluid without reassessing the tympanic membrane and ossicular/structural disease.",
    "Ignoring retraction pockets or cholesteatoma risk because repeated effusions are expected in cleft palate.",
    "Missing an occult/submucous cleft in a child with apparently isolated cleft lip and disproportionate chronic middle-ear disease.",
    "Equating micrognathia with an automatic indication for mandibular distraction without localizing obstruction or assessing severity.",
    "Assuming Robin-sequence obstruction is always single-level tongue-base collapse.",
    "Ignoring feeding failure and growth trajectory when assessing neonatal craniofacial airway obstruction.",
    "Treating snoring in a syndromic craniofacial child as benign without considering objective sleep assessment when management is uncertain.",
    "Performing routine complete adenoidectomy without screening for overt/submucous cleft, hypernasality, nasal regurgitation or prior VPI.",
    "Calling partial adenoidectomy risk-free for VPI rather than a selected compromise that still needs counseling and follow-up.",
    "Choosing VPI surgery by procedure name rather than closure pattern, gap, speech assessment and airway risk.",
    "Ignoring new or worsened OSA after pharyngeal flap or sphincter surgery because speech improved.",
    "Dismantling a VPI reconstruction reflexively for OSA without multidisciplinary evaluation of other obstruction levels and speech consequences.",
    "Attributing failure to thrive entirely to cleft feeding mechanics while missing airway obstruction or aspiration.",
    "Using a textbook palatoplasty age as a rigid deadline rather than integrating growth, airway, speech-development goals and team protocol.",
    "Entering anesthesia in a syndromic craniofacial child without reviewing prior difficult-airway history and defining rescue options.",
    "Treating cleft care as isolated ENT procedures instead of longitudinal interdisciplinary airway-hearing-speech care.",
]

SOURCE_REFS_V231 = [
    {"type":"textbook","citation":"Cummings Otolaryngology–Head and Neck Surgery, 7th ed. (2021). Connected Google Drive full-volume ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t and split Part 5 ID 1Ew2jXOrWG9ISeuZ9WrAI2d5IuXFUzTXm. Cross-referenced for craniofacial syndromes, hearing/otologic risk and Robin-sequence foundations; durable anatomy/operative principles retained while current management is updated from contemporary guidance."},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology—Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022). Connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52. Pediatric chapter and otology sections cross-referenced for cleft classification/repair, Eustachian-tube dysfunction, chronic middle-ear disease, VPI risk with adenoidectomy and pediatric airway principles."},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology, 12th ed. (2019). Connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR. Chapters 52-53 and pediatric otology material cross-referenced for levator/tensor anatomy, cleft-associated Eustachian-tube dysfunction, chronic OME surveillance and craniofacial airway foundations."},
    {"type":"society","citation":"American Cleft Palate Craniofacial Association. Parameters of Care for Evaluation and Treatment of Individuals with Cleft Lip/Palate and/or Other Craniofacial Differences, revised 2024. Problem-based interdisciplinary framework includes neonatal airway, sleep, feeding/growth, hearing, speech and longitudinal evaluation."},
    {"type":"society","citation":"American Cleft Palate Craniofacial Association. Standards for Approval of Cleft Palate and Craniofacial Teams, revised/approved 2026 to align with the 2024 Parameters of Care; reinforces coordinated interdisciplinary cleft/craniofacial team care."},
    {"type":"guideline","citation":"Rosenfeld RM et al. Clinical Practice Guideline: Tympanostomy Tubes in Children (Update). Otolaryngol Head Neck Surg. 2022;166(1_suppl):S1-S55. AAO-HNSF. Cleft palate/craniofacial disorders are at-risk contexts; tubes may be offered when OME is present and likely to persist in children at risk for developmental difficulty."},
    {"type":"systematic_review","citation":"Stanton E et al. Tympanostomy Tubes: Are They Necessary? A Systematic Review on Implementation in Cleft Care. Cleft Palate Craniofac J. 2023;60(4):430-445. PMID 35044261. Used to preserve uncertainty around universal prophylactic versus selective tube strategies."},
    {"type":"peer_reviewed","citation":"Complications of tympanostomy tubes in patients with cleft palate. 2026. PMID 42266256. Retrospective cohort of 278 children; tube-related complications 21% and repeat tubes 42%, useful for counseling but not a universal rate."},
    {"type":"peer_reviewed","citation":"The presence of a submucous cleft palate in patients with isolated cleft lip and middle ear dysfunction. 2024. PMID 38604103. Chronic middle-ear disease in apparently isolated cleft lip can signal occult submucous cleft."},
    {"type":"evidence_update","citation":"Chandrasekharan DP et al. Interventions for Obstructive Eustachian Tube Dysfunction: An Evidence-Based Umbrella Review of Efficacy and Safety. Otolaryngol Clin North Am. 2026. PMID 42203563. Current ETD evidence remains heterogeneous; pediatric OME treatment should follow established age/risk-specific strategies rather than extrapolating adult BDET enthusiasm."},
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "depth_layers_v231": {
        "foundation": "Cleft-palate levator/tensor anatomy, Eustachian-tube dysfunction, craniofacial airway geometry, hearing/speech development and velopharyngeal competence.",
        "application": "Longitudinal audiology/OME surveillance, selective tympanostomy tubes, airway/sleep localization, feeding assessment and VPI-aware adenoid/pharyngeal decision-making.",
        "senior_decision": "Balance hearing-development benefit against repeated-tube morbidity, localize multilevel airway obstruction, protect speech/velopharyngeal function, anticipate difficult-airway rescue and coordinate multidisciplinary escalation.",
    },
    "common_traps_v231": TRAPS,
    "deliberate_review_v231": {"priority":"high","review_after_days":[1,7,21,60],"reason":"high-yield pediatric ENT problem linking chronic ear disease, developmental hearing, neonatal/operative airway risk, sleep surgery and velopharyngeal complications"},
    "source_refs_v231": SOURCE_REFS_V231,
    "evidence_distinction_v231": "Durable textbook anatomy and operative foundations are preserved. Current management is updated with the 2024 ACPA Parameters/2026 team standards and 2022 AAO-HNSF tube guideline: interdisciplinary longitudinal care and developmentally aware OME treatment are current standards, while universal prophylactic tube timing, exact palatoplasty timing and any one Robin-sequence airway operation remain individualized rather than universal. New 2026 tube-complication and ETD data refine counseling but do not replace guideline-based decision-making.",
    "task_alignment_v231": True,
}}


def apply_concept_check_task_alignment_v231(checks, deep_modules, v6_item_id):
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
        for field in ("depth_layers_v231", "common_traps_v231", "deliberate_review_v231", "source_refs_v231", "evidence_distinction_v231", "task_alignment_v231"):
            q[field] = deepcopy(patch[field])
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
