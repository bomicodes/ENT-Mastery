"""v17.1 — Deliberate learning-ladder curation, Otology pass 3.

Reviews the next five canonical Otology concepts. Strong existing foundations are
preserved and explicitly tagged; only missing application and senior/chief
reasoning layers are added.
"""


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus):
    return {
        "id": qid,
        "domain": "Otology / Neurotology",
        "topic": topic,
        "learning_stage": stage,
        "stem": stem,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
        "why_wrong": why_wrong,
        "board_pearl": pearl,
        "curveball": curveball,
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "focus": focus,
    }


REVIEWED_FOUNDATION_IDS_V171 = {
    "v124_oto_12",  # Autoimmune Inner Ear Disease
    "v124_oto_13",  # Tinnitus
    "v124_oto_14",  # Central Vestibular Disorders
    "v135_oto_01",  # Sudden Sensorineural Hearing Loss
    "v135_oto_03",  # Chronic Otitis Media / Cholesteatoma
}


VIGNETTES_V171 = [
    _q(
        "v171_oto_aied_app", "Autoimmune Inner Ear Disease", "application",
        "A 49-year-old develops bilateral asymmetric sensorineural hearing loss that fluctuates and progresses over 6 weeks. MRI of the internal auditory canals is unrevealing, and there is no conductive component. ESR, CRP, ANA, and rheumatoid factor are normal. What is the best next interpretation?",
        [
            "Normal systemic inflammatory markers exclude autoimmune inner-ear disease",
            "The clinical tempo remains compatible with autoimmune inner-ear disease, but important mimics must still be excluded and treatment response interpreted cautiously",
            "The patient has presbycusis because all laboratory tests are normal",
            "This is otosclerosis until proven otherwise",
        ], 1,
        "Autoimmune inner-ear disease is primarily a clinical syndrome of rapidly progressive or fluctuating sensorineural loss over weeks to months. There is no single blood test that confirms or excludes it. Normal systemic markers therefore do not end the evaluation; infectious, inflammatory, toxic, genetic, hydrops-spectrum, and retrocochlear mimics still need to be considered according to the presentation.",
        [
            "Systemic serologies can support a broader autoimmune diagnosis but lack sufficient sensitivity to rule out isolated immune-mediated cochlear disease.",
            "Correct. The tempo is concerning, but the label remains a diagnosis of exclusion supported by the total clinical picture rather than one laboratory panel.",
            "Presbycusis is usually gradual over years and relatively symmetric, not rapidly fluctuating over several weeks.",
            "Otosclerosis is primarily a conductive or mixed mechanical loss and does not fit this rapidly progressive bilateral SNHL pattern.",
        ],
        "In rapidly progressive SNHL, a negative autoimmune panel does not make the tempo benign.",
        "If hearing improves clearly with corticosteroids and then declines during taper, how would that influence diagnosis, treatment planning, and steroid-sparing discussions?",
        "boards",
    ),
    _q(
        "v171_oto_aied_snr", "Autoimmune Inner Ear Disease", "senior_decision",
        "A patient with suspected autoimmune inner-ear disease has meaningful steroid-responsive hearing improvement but relapses repeatedly during taper and is developing major steroid toxicity. What is the best senior-level management principle?",
        [
            "Continue repeated high-dose systemic steroid courses indefinitely without reassessing the diagnosis",
            "Reconfirm the working diagnosis and coordinate steroid-sparing immunomodulatory management with appropriate specialists while continuing serial audiometric monitoring",
            "Proceed directly to labyrinthectomy because hearing fluctuates",
            "Stop all hearing rehabilitation until the immune diagnosis is proven by biopsy",
        ], 1,
        "Repeated steroid responsiveness can support an immune-mediated mechanism, but chronic systemic steroid toxicity changes the risk-benefit balance. Senior management means reassessing mimics, documenting objective audiometric response, involving rheumatology or another appropriate specialist when systemic immunomodulation is considered, and planning hearing rehabilitation in parallel rather than treating steroids as the only endpoint.",
        [
            "Indefinite systemic steroids expose the patient to substantial morbidity and can reinforce an incorrect diagnosis if objective response is not tracked.",
            "Correct. The decision integrates diagnostic uncertainty, objective hearing trajectory, treatment toxicity, and longer-term rehabilitation.",
            "Labyrinthectomy sacrifices vestibular function and is not treatment for immune-mediated fluctuating hearing loss.",
            "Hearing rehabilitation should not be withheld while diagnostic work continues; function matters during the entire disease course.",
        ],
        "A steroid response is evidence, not proof; use objective audiograms and toxicity to decide when the strategy must change.",
        "What features would make you abandon the autoimmune label and redirect the workup toward another cause of rapidly progressive SNHL?",
        "OR_prep",
    ),

    _q(
        "v171_oto_tin_app", "Tinnitus", "application",
        "A 61-year-old has unilateral pulse-synchronous tinnitus with normal otoscopy. The sound diminishes when gentle pressure is applied over the ipsilateral internal jugular vein. Which next step is most appropriate?",
        [
            "Treat as routine bilateral nonpulsatile tinnitus with reassurance only",
            "Pursue directed vascular imaging with particular attention to venous causes of pulsatile tinnitus",
            "Diagnose vestibular migraine from the tinnitus alone",
            "Start chronic vestibular suppressants",
        ], 1,
        "Pulse-synchronous tinnitus requires evaluation for vascular and structural causes. Modulation with ipsilateral jugular compression suggests a venous source and should shape the imaging strategy toward lesions such as sigmoid sinus wall abnormalities, jugular bulb variants, venous sinus stenosis, or other venous pathology while still considering the full pulsatile-tinnitus differential.",
        [
            "Pulsatile unilateral tinnitus is not managed like common symmetric nonpulsatile tinnitus because potentially treatable vascular lesions may be present.",
            "Correct. The bedside modulation is a localization clue that should inform targeted imaging rather than provide a final diagnosis by itself.",
            "Migraine can coexist with tinnitus but pulse synchronicity and venous modulation require a vascular evaluation first.",
            "Vestibular suppressants do not investigate or treat a vascular tinnitus generator.",
        ],
        "In pulsatile tinnitus, ask whether the patient can change the sound with venous compression, head turning, or Valsalva; modulation can help localize the source.",
        "What otoscopic finding would push you toward a glomus tumor rather than a venous sinus-wall source?",
        "boards",
    ),
    _q(
        "v171_oto_tin_snr", "Tinnitus", "senior_decision",
        "A patient with disabling pulsatile tinnitus has sigmoid sinus dehiscence on CT, but MR venography also shows transverse-sinus stenosis and the patient has headaches and papilledema. What is the best senior-level decision?",
        [
            "Repair the sigmoid sinus wall immediately because any CT dehiscence proves it is the sole cause",
            "Evaluate and address possible intracranial-pressure/venous outflow pathology before assuming the local bony finding is the only mechanism",
            "Ignore the papilledema because tinnitus is an otologic symptom",
            "Perform stapedotomy",
        ], 1,
        "Pulsatile tinnitus can reflect interacting venous and intracranial-pressure mechanisms. Sigmoid wall abnormalities may be causal, contributory, or incidental. Papilledema and venous sinus stenosis demand evaluation for intracranial hypertension before committing to a local operation that may fail if the underlying pressure physiology remains untreated.",
        [
            "An imaging abnormality must match the physiology; dehiscence alone does not prove it is the sole symptomatic lesion.",
            "Correct. Chief-level management asks whether the apparent local target is actually downstream of a broader venous-pressure problem.",
            "Papilledema is a neurologic red flag and cannot be dismissed during tinnitus workup.",
            "Stapes surgery treats conductive mechanics and has no role in venous pulsatile tinnitus.",
        ],
        "Do not operate on an image in pulsatile tinnitus; operate on a mechanism that matches the history, exam, and vascular workup.",
        "If intracranial pressure is normalized but pulse-synchronous tinnitus persists and still localizes to the sigmoid wall, how does the surgical discussion change?",
        "OR_prep",
    ),

    _q(
        "v171_oto_central_app", "Central Vestibular Disorders", "application",
        "A 66-year-old has sudden continuous vertigo, vomiting, and gait instability. Examination shows a normal head impulse, direction-changing gaze-evoked nystagmus, and skew deviation. MRI obtained 5 hours after symptom onset is negative. What is the best next step?",
        [
            "Discharge because diffusion MRI excludes stroke",
            "Continue urgent posterior-circulation stroke evaluation and observation because the central bedside pattern outweighs an early negative scan",
            "Perform an Epley maneuver and discharge",
            "Diagnose vestibular neuritis because the patient has vertigo without hearing loss",
        ], 1,
        "In a true acute vestibular syndrome, a central bedside pattern can be more sensitive than very early MRI for small posterior-fossa ischemia. The correct response to discordant imaging is not diagnostic closure but continued stroke-level evaluation, serial examination, and repeat imaging when clinically appropriate.",
        [
            "Early diffusion imaging can miss posterior-circulation infarction, especially small lesions in the brainstem or cerebellum.",
            "Correct. The bedside localization remains central and should determine disposition despite the initial scan.",
            "BPPV produces brief position-triggered attacks, not a continuous central ocular-motor syndrome.",
            "Vestibular neuritis usually produces an abnormal head impulse toward the affected side and unidirectional nystagmus.",
        ],
        "A negative early MRI is not permission to overrule a strongly central acute vestibular examination.",
        "Which features of the presentation make HINTS appropriate here, and in what dizziness presentations would HINTS be misapplied?",
        "overnight_call",
    ),
    _q(
        "v171_oto_central_snr", "Central Vestibular Disorders", "senior_decision",
        "A patient with known multiple sclerosis presents with new vertigo. The team assumes the symptoms are another demyelinating relapse, but examination shows a new severe truncal ataxia and a vascular-pattern acute vestibular syndrome. What is the best senior-level principle?",
        [
            "Attribute all future vertigo to multiple sclerosis once that diagnosis exists",
            "Re-localize the current syndrome from first principles and urgently exclude stroke or another new central lesion rather than anchoring on the chronic diagnosis",
            "Treat only with vestibular suppressants",
            "Assume BPPV because vertigo is common",
        ], 1,
        "A pre-existing neurologic diagnosis increases, rather than decreases, the need for careful localization when the current syndrome changes. Senior reasoning separates disease history from present anatomy: a new acute vestibular syndrome with major gait or ocular-motor abnormalities deserves evaluation for vascular and other central causes even in a patient with known demyelinating disease.",
        [
            "Diagnostic anchoring can miss a second process with a different time course and management urgency.",
            "Correct. The present syndrome must earn its diagnosis independently of the problem list.",
            "Symptomatic suppression does not address a potentially time-sensitive central cause.",
            "BPPV is brief and position-triggered and does not explain severe continuous central dysfunction.",
        ],
        "A prior central diagnosis does not explain every future central symptom; always ask whether the current tempo and localization still fit.",
        "How would focal auditory symptoms change the posterior-circulation differential, particularly for AICA-territory disease?",
        "overnight_call",
    ),

    _q(
        "v171_oto_ssnhl_app", "Sudden Sensorineural Hearing Loss", "application",
        "A patient presents 18 days after sudden unilateral sensorineural hearing loss. He completed an oral steroid course but has had minimal recovery. MRI shows no retrocochlear lesion. What treatment should now be specifically discussed?",
        [
            "No further treatment because the initial 2-week window has closed",
            "Intratympanic steroid salvage within the accepted early salvage window, with follow-up audiometry",
            "Routine systemic antibiotics",
            "Immediate labyrinthectomy",
        ], 1,
        "Incomplete recovery after initial therapy does not end the treatment pathway. Intratympanic steroid salvage is typically offered during the first several weeks after onset, and hearing should be documented after treatment. The important resident-level decision is recognizing that the salvage window is distinct from the initial systemic-treatment window.",
        [
            "The end of the preferred initial systemic-steroid window does not mean that evidence-based salvage options have disappeared.",
            "Correct. This presentation remains within the usual intratympanic salvage period.",
            "Antibiotics do not treat typical idiopathic SSNHL without evidence of bacterial disease.",
            "Labyrinthectomy would destroy vestibular function and residual hearing and is unrelated to SSNHL salvage.",
        ],
        "For SSNHL, know both clocks: initial therapy is time-sensitive, and incomplete recovery has its own salvage window.",
        "Where does hyperbaric oxygen fit as initial or salvage therapy, and how would access and comorbidity affect the discussion?",
        "boards",
    ),
    _q(
        "v171_oto_ssnhl_snr", "Sudden Sensorineural Hearing Loss", "senior_decision",
        "A patient with unilateral SSNHL improves after treatment, then develops a second sudden episode in the opposite ear 3 months later with new inflammatory joint symptoms. What is the best next decision?",
        [
            "Label both episodes idiopathic and repeat the same treatment without broadening the differential",
            "Treat the acute hearing loss promptly while expanding the etiologic evaluation for systemic inflammatory, autoimmune, infectious, and other non-idiopathic causes",
            "Delay therapy until every laboratory test returns",
            "Proceed directly to cochlear implantation before reassessing the active disease process",
        ], 1,
        "Bilateral, recurrent, or systemically associated sudden SNHL breaks the usual idiopathic pattern. Treatment for the acute hearing emergency should not be delayed, but the diagnostic frame must widen at the same time to search for a secondary process that changes prognosis and longer-term management.",
        [
            "Recurrence in the opposite ear plus systemic symptoms is exactly the pattern that should reopen etiology rather than reinforce an idiopathic label.",
            "Correct. Senior management runs urgent treatment and targeted etiologic investigation in parallel.",
            "Waiting for complete laboratory certainty sacrifices the time-sensitive treatment window.",
            "Implant candidacy may become relevant later for persistent severe loss, but it does not replace evaluation and treatment of an active recurrent process.",
        ],
        "Idiopathic is the common endpoint for a typical single episode, not a permanent label that survives recurrent bilateral disease.",
        "Which history or laboratory clues would make syphilis, Lyme disease, vasculitis, or Cogan-spectrum disease more plausible in this setting?",
        "overnight_call",
    ),

    _q(
        "v171_oto_chol_app", "Chronic Otitis Media / Cholesteatoma", "application",
        "A patient with attic cholesteatoma has conductive hearing loss and CT evidence of incus erosion. The ear is chronically draining, but there is no labyrinthine fistula or facial weakness. Which operative priority is most appropriate?",
        [
            "Maximize hearing reconstruction first even if keratin remains in a hidden recess",
            "Eradicate cholesteatoma and create a safe, maintainable ear first; reconstruct hearing only when disease control and middle-ear conditions permit",
            "Treat indefinitely with topical drops because drainage has improved",
            "Observe until a cranial neuropathy develops",
        ], 1,
        "Cholesteatoma surgery follows a hierarchy: complete disease control and a safe dry maintainable ear come before hearing reconstruction. Ossiculoplasty can be simultaneous when clearance is confident and the middle-ear environment is favorable, but should be staged when residual-disease risk or inflammation makes reconstruction secondary.",
        [
            "Leaving matrix behind to preserve or rebuild hearing defeats the primary safety goal and increases residual disease risk.",
            "Correct. Hearing rehabilitation matters, but never at the expense of cholesteatoma clearance.",
            "Drops can control superinfection but cannot eradicate keratinizing epithelium from the middle ear or mastoid.",
            "Waiting for facial, labyrinthine, or intracranial complications is precisely what definitive surgery seeks to prevent.",
        ],
        "Cholesteatoma hierarchy: safe ear first, dry/maintainable ear second, hearing reconstruction third.",
        "What middle-ear and stapes findings make single-stage PORP reconstruction reasonable, and what findings would make you stage it?",
        "OR_prep",
    ),
    _q(
        "v171_oto_chol_snr", "Chronic Otitis Media / Cholesteatoma", "senior_decision",
        "A patient has extensive recurrent cholesteatoma involving the epitympanum, mastoid, sinus tympani, and posterior canal wall with poor mastoid aeration. The patient has repeatedly missed follow-up and cannot reliably return for serial MRI or planned second-look surgery. What is the best senior-level operative principle?",
        [
            "Choose canal-wall-up surgery because preserving anatomy is always more important than surveillance reliability",
            "Favor the approach that maximizes complete clearance and creates a durable maintainable ear, with canal-wall-down or reconstruction/obliteration strategies considered when disease extent and follow-up reliability make canal-wall-up surveillance unsafe",
            "Avoid surgery because recurrence proves cholesteatoma is incurable",
            "Perform ossiculoplasty only and leave mastoid disease for later",
        ], 1,
        "Canal-wall-up versus canal-wall-down is not a prestige choice. Extensive recurrent disease, hidden recess involvement, unfavorable anatomy, and unreliable surveillance can shift the balance toward a more exteriorized or reconstructed cavity strategy that improves disease control and maintainability. The exact technique remains individualized, but the operation must match both the anatomy and the patient's ability to complete surveillance.",
        [
            "Canal-wall-up preserves canal anatomy but carries a surveillance burden that may be unsafe when residual disease risk is high and follow-up is unreliable.",
            "Correct. Chief-level planning integrates disease extent, anatomy, hearing, recurrence history, and real-world follow-up reliability.",
            "Recurrent cholesteatoma remains surgically treatable; recurrence changes strategy rather than eliminating the goal of a safe ear.",
            "Hearing reconstruction without eradication of extensive mastoid disease reverses the correct operative priorities.",
        ],
        "CWU versus CWD is fundamentally a disease-control and surveillance decision, not simply a cosmetic/anatomic preference.",
        "How would an only-hearing ear alter counseling and your tolerance for a more aggressive disease-control strategy?",
        "OR_prep",
    ),
]


def apply_learning_ladders_v171(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed = 0
    for qid in REVIEWED_FOUNDATION_IDS_V171:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v17.1: reviewed foundation missing from live registry: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for q in VIGNETTES_V171:
        item = dict(q)
        if item["id"] in existing:
            continue
        item["concept_id"] = id_factory(item["domain"], item["topic"])
        item["ladder_reviewed"] = True
        challenges.append(item)
        existing.add(item["id"])
        added += 1

    return {
        "reviewed_foundations": reviewed,
        "added_questions": added,
        "topics": sorted({q["topic"] for q in VIGNETTES_V171}),
    }
