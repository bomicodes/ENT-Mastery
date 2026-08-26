"""v20.4 — complete deliberate Otology / Neurotology ladder reconciliation.

The prior v16.9-v17.6 passes deliberately reviewed 38 of the 45 canonical
Otology topics (including the already complete Audiogram Interpretation ladder).
This patch closes the final seven by preserving an existing foundation case,
staging the strongest existing second-pass case as application, and adding only
one missing senior/chief decision layer per concept.

It also performs the answer-position shuffle *after* all deliberate ladder
mutation. Earlier global rebalancing occurs in recognize_stage_v127 before the
runtime ladder modules are appended, so without this final pass the curated
questions can retain author-position bias.
"""

import hashlib

DOMAIN = "Otology / Neurotology"

# These are the strongest existing application/management cases already in the
# live bank. They are upgraded in place rather than duplicated.
APPLICATION_IDS_V204 = {
    "BPPV": "v141_oto_01",
    "Ménière Disease": "v141_oto_02",
    "Vestibular Schwannoma": "v141_oto_03",
    "Necrotizing Otitis Externa": "v142_oto_01",
    "Superior Canal Dehiscence": "v143_oto_04",
    "Labyrinthitis / Infections of the Labyrinth": "v144_oto_12",
    "Ossicular Discontinuity": "v144_oto_15",
}


def _q(qid, topic, stem, choices, answer, explanation, why_wrong,
       pearl, curveball, focus):
    return {
        "id": qid,
        "domain": DOMAIN,
        "topic": topic,
        "learning_stage": "senior_decision",
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
        "ladder_reviewed": True,
    }


VIGNETTES_V204 = [
    _q(
        "v204_oto_bppv_snr", "BPPV",
        "A patient referred for 'refractory BPPV' has positional vertigo, but repeated Dix-Hallpike testing produces immediate persistent downbeating nystagmus without latency or fatigability. Multiple Epley maneuvers have not helped. What is the best senior-level decision?",
        [
            "Continue repeating Epley maneuvers because any positional vertigo is BPPV",
            "Begin chronic meclizine and stop positional testing",
            "Treat the atypical positional nystagmus as a central red flag and pursue neurologic evaluation/imaging rather than forcing a BPPV diagnosis",
            "Schedule labyrinthectomy",
        ], 2,
        "Classic posterior-canal BPPV has a canal-specific nystagmus pattern with characteristic latency, direction, and fatigability. Persistent immediate downbeat positional nystagmus that resists appropriate maneuvers should reopen localization and raise concern for a central positional syndrome rather than trigger endless canalith treatment.",
        [
            "Repeated maneuvers are inappropriate when the observed nystagmus no longer matches a peripheral canalithiasis pattern.",
            "Vestibular suppressants can mask examination findings and do not address a possible central lesion.",
            "Correct. Failure of the phenotype—not simply failure of the maneuver—is what should change the diagnostic pathway.",
            "A destructive inner-ear operation has no role before the atypical central pattern is explained.",
        ],
        "When 'BPPV' stops behaving like BPPV, re-localize before repeating the same maneuver.",
        "What positional nystagmus patterns support horizontal-canal cupulolithiasis, and how do you distinguish them from central positional nystagmus?",
        "boards",
    ),
    _q(
        "v204_oto_meniere_snr", "Ménière Disease",
        "A patient with unilateral definite Ménière disease continues frequent disabling vertigo despite appropriate nondestructive therapy. Hearing in the affected ear is now nonserviceable, vestibular testing confirms unilateral disease, and the contralateral ear is stable. Which escalation best fits the current goals?",
        [
            "Discuss definitive ablative vertigo control such as labyrinthectomy, with counseling about permanent ipsilateral hearing loss and postoperative vestibular rehabilitation",
            "Repeat hearing-preservation therapy indefinitely even though hearing is already nonserviceable and vertigo remains disabling",
            "Perform bilateral vestibular ablation to prevent future attacks",
            "Cochlear implantation alone will reliably eliminate the vertigo mechanism",
        ], 0,
        "Escalation in Ménière disease is driven by vertigo disability and the value of residual hearing. Once hearing is nonserviceable in a clearly unilateral refractory ear, labyrinthectomy becomes a reasonable high-control option because preservation of that ear's acoustic hearing is no longer the dominant constraint.",
        [
            "Correct. The treatment hierarchy changes when the ear no longer has useful hearing to preserve.",
            "Persisting with the same lower-intensity strategy despite disabling refractory attacks does not address the patient's current disease burden.",
            "Bilateral vestibular loss causes major chronic disability and is never the goal in unilateral disease.",
            "A cochlear implant can rehabilitate hearing in selected patients but is not, by itself, a dependable ablative treatment for active vertigo.",
        ],
        "Ménière escalation is a two-axis decision: vertigo burden and how much hearing remains worth preserving.",
        "How would useful hearing, bilateral disease, or poor contralateral vestibular reserve change the choice among intratympanic gentamicin, vestibular nerve section, and labyrinthectomy?",
        "OR_prep",
    ),
    _q(
        "v204_oto_vs_snr", "Vestibular Schwannoma",
        "During microsurgical resection of a vestibular schwannoma, a thin densely adherent tumor remnant remains on an anatomically intact facial nerve. Further dissection produces progressively worse stimulation responses. What is the best attending-level principle?",
        [
            "Continue until gross-total resection is achieved regardless of facial-nerve physiology",
            "Sacrifice the facial nerve preemptively because any residual tumor will inevitably recur",
            "Convert automatically to a translabyrinthine approach after the nerve is exposed",
            "Prioritize facial-nerve preservation; when the risk of permanent nerve injury exceeds the benefit of microscopic clearance, leave a deliberate small remnant and use surveillance with radiosurgical treatment if needed",
        ], 3,
        "Vestibular schwannoma surgery balances durable tumor control against facial and cochlear nerve function. A deliberate near-total or subtotal resection can be the safer oncologic-functional decision when the final adherent capsule cannot be separated without unacceptable facial-nerve risk; residual growth can be followed and treated selectively.",
        [
            "Gross-total resection is not a worthy endpoint if the final millimeter converts a functional facial nerve into a permanent paralysis.",
            "Facial-nerve sacrifice is not justified merely because a small adherent remnant remains.",
            "Changing the bony approach does not solve a tumor-capsule adherence problem once the nerve is already at risk.",
            "Correct. Senior skull-base judgment includes knowing when functional preservation outweighs microscopic completeness.",
        ],
        "In vestibular schwannoma surgery, 'complete' should describe the treatment plan, not necessarily the microscopic resection percentage.",
        "How do patient age, residual size, tumor growth kinetics, NF2-related disease, and preoperative hearing influence the surveillance-versus-adjuvant-radiosurgery plan?",
        "OR_prep",
    ),
    _q(
        "v204_oto_noe_snr", "Necrotizing Otitis Externa",
        "A diabetic patient being treated for presumed necrotizing otitis externa has persistent severe pain and granulation tissue despite appropriate systemic antipseudomonal therapy. Cultures are repeatedly negative after prior drops, and the canal lesion is becoming more mass-like. What is the best next decision?",
        [
            "Continue the same antibiotics for several more months without revisiting the diagnosis",
            "Obtain adequate tissue/deep cultures and biopsy to evaluate resistant infection, fungal disease, and malignancy while reassessing imaging and antimicrobial coverage",
            "Perform routine radical temporal-bone resection for all treatment failures",
            "Stop systemic therapy because negative surface cultures exclude infection",
        ], 1,
        "Failure to improve should trigger diagnostic reassessment rather than automatic prolongation of the same regimen. Necrotizing infection can be culture-negative after treatment, fungal pathogens may occur in selected hosts, and external-canal carcinoma can mimic skull-base infection; deep sampling and biopsy may be necessary when the phenotype changes or response is poor.",
        [
            "Therapeutic inertia can delay recognition of resistant organisms, fungal disease, or a malignant mimic.",
            "Correct. Refractory disease is a reason to improve the diagnosis, not simply extend an unproven treatment indefinitely.",
            "Extensive ablative surgery is not routine first-line salvage for skull-base osteomyelitis and carries major morbidity.",
            "Negative superficial cultures after prior topical/systemic therapy do not exclude invasive infection.",
        ],
        "A treatment-resistant skull-base infection deserves a better specimen and a reopened differential.",
        "Which clinical, inflammatory-marker, and imaging trends are most useful for judging response when radiographic marrow abnormalities lag behind improvement?",
        "overnight_call",
    ),
    _q(
        "v204_oto_sscd_snr", "Superior Canal Dehiscence",
        "A patient has disabling autophony, sound- and pressure-induced vertigo, a physiologic third-window pattern on VEMP testing, and high-resolution CT confirming superior canal dehiscence in the symptomatic ear. Symptoms persist despite conservative counseling. What is the best senior-level management principle?",
        [
            "Perform stapedotomy because the air-bone gap proves ossicular fixation",
            "Operate on the contralateral radiographic dehiscence first because it is larger on CT",
            "Discuss surgical occlusion/repair of the symptomatic superior canal using an anatomy-appropriate approach, with counseling about hearing, vestibular, and recurrence risks",
            "Avoid surgery in all patients because CT can overcall thin bone",
        ], 2,
        "Surgery is reserved for a clinically significant, concordant third-window syndrome—not a CT finding alone. When symptoms are disabling and physiology plus imaging agree, canal plugging/repair through an appropriate middle-fossa or transmastoid corridor can be considered after counseling about postoperative disequilibrium and auditory risk.",
        [
            "Third-window conductive-appearing loss is not stapes fixation; stapes surgery can worsen symptoms and fails to treat the mechanism.",
            "Radiographic size alone does not override symptom laterality and physiologic concordance.",
            "Correct. The operative target is the symptomatic physiologic third window, and approach choice follows anatomy and surgeon expertise.",
            "CT false positives are why physiologic and symptom concordance are required; they do not make surgery inappropriate for every confirmed disabling syndrome.",
        ],
        "Do not operate on dehiscent bone; operate on a concordant disabling third-window syndrome.",
        "What factors favor a transmastoid versus middle-fossa approach, and how would bilateral dehiscence change counseling about staged intervention?",
        "OR_prep",
    ),
    _q(
        "v204_oto_lab_snr", "Labyrinthitis / Infections of the Labyrinth",
        "A patient with acute otitis media develops abrupt severe vertigo, new sensorineural hearing loss, fever, and worsening headache with neck stiffness. What is the safest next decision?",
        [
            "Treat this as complicated otogenic infection with possible suppurative labyrinthitis/meningitis: admit, begin urgent IV antimicrobial therapy, evaluate intracranial extension, and obtain ENT source-control and neurologic/infectious-disease input",
            "Diagnose vestibular neuritis and discharge with meclizine because vertigo is the dominant symptom",
            "Delay antimicrobial therapy until every culture and lumbar-puncture result is finalized",
            "Perform an Epley maneuver and reassess in one week",
        ], 0,
        "Cochlear involvement already separates labyrinthitis from isolated vestibular neuritis; fever, meningismus, and progressive headache add intracranial red flags. Antimicrobial therapy and source-control planning must proceed urgently while imaging and further diagnostic testing define meningitis, mastoid, or intracranial extension.",
        [
            "Correct. This has crossed from an isolated vestibular syndrome into a potentially life-threatening otogenic infection.",
            "Vestibular neuritis classically spares hearing and does not explain fever or meningismus.",
            "Time-critical bacterial infection should not wait for complete diagnostic certainty before appropriate empiric therapy begins.",
            "Canalith repositioning treats BPPV, not an acute cochleovestibular infectious syndrome with systemic red flags.",
        ],
        "Acute vertigo plus new SNHL changes localization; add fever or meningismus and it becomes an infection/source-control emergency.",
        "What middle-ear or mastoid findings would lower your threshold for tympanostomy, mastoidectomy, or other operative source control?",
        "overnight_call",
    ),
    _q(
        "v204_oto_oss_snr", "Ossicular Discontinuity",
        "During exploratory tympanoplasty for persistent conductive hearing loss after trauma, the long process of the incus is absent. The malleus is stable, the stapes superstructure is intact and mobile, and the middle-ear mucosa is healthy. What reconstruction principle is most appropriate?",
        [
            "Abort reconstruction because any ossicular defect requires a cochlear implant",
            "Remove the mobile stapes and perform stapedotomy",
            "Pack the middle ear tightly with fascia without reconnecting the chain",
            "Re-establish a stable sound-conduction linkage to the intact mobile stapes, commonly with a partial ossicular reconstruction strategy when geometry and middle-ear conditions are favorable",
        ], 3,
        "Ossiculoplasty is chosen from the remaining mechanical chain. When a mobile stapes superstructure is present, a partial reconstruction can couple the tympanic membrane/malleus side to the stapes; total prosthetic reconstruction is generally reserved for loss of the superstructure. Middle-ear aeration, mucosal health, stability, and prosthesis geometry strongly affect outcome.",
        [
            "A conductive mechanical defect with good cochlear reserve is precisely the situation in which ossicular reconstruction can be useful.",
            "A mobile stapes is not the problem; stapes surgery would create unnecessary inner-ear risk.",
            "Fascia can support tympanic-membrane repair but does not by itself restore an interrupted ossicular linkage.",
            "Correct. Reconstruction should use the best remaining stable native structures rather than applying one prosthesis to every defect.",
        ],
        "PORP versus TORP is an anatomy question: is there a usable stapes superstructure to couple to?","
        "How would absent stapes superstructure, poor Eustachian-tube function, active infection, or a lateralized tympanic membrane change reconstruction choice or staging?",
        "OR_prep",
    ),
]


def _validate_reason_alignment(q):
    choices = list(q.get("choices") or [])
    reasons = list(q.get("why_wrong") or [])
    if len(choices) < 4 or len(reasons) != len(choices):
        raise RuntimeError(f"v20.4: malformed reviewed question {q.get('id')}: choices/reasons")
    try:
        answer = int(q.get("answer"))
    except (TypeError, ValueError):
        raise RuntimeError(f"v20.4: malformed answer for {q.get('id')}")
    if not 0 <= answer < len(choices):
        raise RuntimeError(f"v20.4: answer out of range for {q.get('id')}")


def _rebalance_reviewed_answers(challenges):
    """Deterministically rebalance all deliberately reviewed ladder questions."""
    changed = 0
    for q in challenges:
        if not q.get("ladder_reviewed"):
            continue
        _validate_reason_alignment(q)
        choices = list(q["choices"])
        reasons = list(q["why_wrong"])
        answer = int(q["answer"])
        target = int.from_bytes(
            hashlib.sha256(str(q.get("id", "")).encode("utf-8")).digest()[:4],
            "big",
        ) % len(choices)
        if target == answer:
            continue
        correct_choice = choices.pop(answer)
        correct_reason = reasons.pop(answer)
        choices.insert(target, correct_choice)
        reasons.insert(target, correct_reason)
        q["choices"] = choices
        q["why_wrong"] = reasons
        q["answer"] = target
        changed += 1
    return changed


def apply_learning_ladders_v204(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    by_topic = {}
    for q in challenges:
        if q.get("domain") == DOMAIN:
            by_topic.setdefault(q.get("topic"), []).append(q)

    staged_foundations = 0
    staged_applications = 0
    for topic, app_id in APPLICATION_IDS_V204.items():
        app = by_id.get(app_id)
        if app is None:
            raise RuntimeError(f"v20.4: expected application case missing: {app_id}")
        if app.get("domain") != DOMAIN or app.get("topic") != topic:
            raise RuntimeError(f"v20.4: application mapping mismatch: {app_id}")
        app["learning_stage"] = "application"
        app["ladder_reviewed"] = True
        staged_applications += 1

        # The selected v14.1-v14.4 cases were authored as second-pass depth cases.
        # Preserve the pre-existing first linked case as the foundation rather than
        # generating a duplicate recall question merely to satisfy the ladder.
        candidates = [
            q for q in by_topic.get(topic, [])
            if q.get("id") != app_id and q.get("learning_stage") not in {"application", "senior_decision"}
        ]
        if not candidates:
            raise RuntimeError(f"v20.4: no existing foundation candidate for {topic}")
        foundation = candidates[0]
        foundation["learning_stage"] = "foundation"
        foundation["ladder_reviewed"] = True
        staged_foundations += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for source in VIGNETTES_V204:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = id_factory(q["domain"], q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1

    rebalanced = _rebalance_reviewed_answers(challenges)
    return {
        "staged_foundations": staged_foundations,
        "staged_applications": staged_applications,
        "added_questions": added,
        "rebalanced_reviewed_questions": rebalanced,
        "topics": sorted(APPLICATION_IDS_V204),
    }
