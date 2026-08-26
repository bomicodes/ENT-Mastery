"""v20.4 — proven Otology foundation gaps discovered by runtime reconciliation.

Only concepts that fail to supply a separate pre-existing foundation are added
here. Their strong second-pass application cases remain preserved and are staged
later by vignette_ladders_v204.
"""

DOMAIN = "Otology / Neurotology"

FOUNDATIONS_V204 = [
    {
        "id": "v204_oto_sscd_fnd",
        "domain": DOMAIN,
        "topic": "Superior Canal Dehiscence",
        "learning_stage": "foundation",
        "stem": (
            "A patient reports hearing their own voice and internal body sounds unusually loudly, "
            "with brief vertigo triggered by loud sound and straining. Audiometry shows a low-frequency "
            "air-bone gap, but otoscopy and tympanometry show normal middle-ear mechanics. Which diagnosis "
            "best explains this pattern?"
        ),
        "choices": [
            "Otosclerosis with stapes fixation",
            "Superior canal dehiscence producing a third-window syndrome",
            "Patulous Eustachian tube dysfunction",
            "Ménière disease",
        ],
        "answer": 1,
        "explanation": (
            "Autophony of internal sounds, sound- or pressure-induced vestibular symptoms, and a "
            "conductive-appearing low-frequency air-bone gap despite normal middle-ear mechanics are a "
            "classic third-window pattern. Superior canal dehiscence is a leading cause and should be "
            "confirmed with concordant physiologic testing and properly reformatted high-resolution CT."
        ),
        "why_wrong": [
            "Stapes fixation can create a conductive air-bone gap, but it does not explain sound- and pressure-induced vertigo with normal third-window-type middle-ear mechanics.",
            "Correct.",
            "Patulous Eustachian tube dysfunction can cause voice or breathing autophony, but respiratory tympanic-membrane movement and positional symptom change are more characteristic than Tullio or pressure-induced vertigo.",
            "Ménière disease causes episodic vertigo with fluctuating cochlear symptoms, not a persistent conductive-appearing gap with sound- and pressure-triggered third-window physiology.",
        ],
        "board_pearl": (
            "An air-bone gap with normal middle-ear mechanics plus autophony or Tullio/Hennebert symptoms "
            "should make you think third window before stapes surgery."
        ),
        "curveball": (
            "Which VEMP findings and CT reformats would provide physiologic and anatomic confirmation before any surgical discussion?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "focus": "boards",
        "ladder_reviewed": True,
    },
    {
        "id": "v204_oto_lab_fnd",
        "domain": DOMAIN,
        "topic": "Labyrinthitis / Infections of the Labyrinth",
        "learning_stage": "foundation",
        "stem": (
            "A patient develops acute continuous spinning vertigo, nausea, spontaneous horizontal-torsional "
            "nystagmus, new unilateral sensorineural hearing loss, and tinnitus during an acute middle-ear "
            "infection. Which diagnosis best fits the cochleovestibular syndrome?"
        ),
        "choices": [
            "Vestibular neuritis",
            "Posterior-canal BPPV",
            "Labyrinthitis with cochlear involvement",
            "Otosclerosis",
        ],
        "answer": 2,
        "explanation": (
            "Labyrinthitis involves both vestibular and cochlear structures, producing an acute vestibular "
            "syndrome together with sensorineural hearing loss and/or tinnitus. Vestibular neuritis can look "
            "similar from the balance standpoint but classically spares hearing, while an active otologic "
            "infection increases concern for an infectious labyrinthine process."
        ),
        "why_wrong": [
            "Vestibular neuritis causes prolonged peripheral vertigo but classically lacks new cochlear hearing loss or tinnitus from labyrinthine involvement.",
            "BPPV causes brief position-triggered attacks with canal-specific positional nystagmus rather than continuous vertigo with new sensorineural hearing loss.",
            "Correct.",
            "Otosclerosis is a chronic stapes-fixation disorder causing conductive or mixed hearing loss, not an acute infectious cochleovestibular syndrome.",
        ],
        "board_pearl": (
            "In an acute vestibular syndrome, new sensorineural hearing loss means the cochlea is involved and "
            "should move you away from a simple vestibular-neuritis label."
        ),
        "curveball": (
            "Which fever, neurologic, meningeal, or mastoid findings would convert this from an otologic diagnosis into an urgent intracranial/source-control problem?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "focus": "boards",
        "ladder_reviewed": True,
    },
]


def apply_otology_foundation_gap_v204(challenges, id_factory):
    existing_ids = {q.get("id") for q in challenges if q.get("id")}
    added = []
    skipped = []
    for source in FOUNDATIONS_V204:
        topic = source["topic"]
        expected_cid = id_factory(DOMAIN, topic)
        if source["id"] in existing_ids:
            skipped.append(topic)
            continue
        if any(
            q.get("concept_id") == expected_cid
            and q.get("learning_stage") == "foundation"
            for q in challenges
        ):
            skipped.append(topic)
            continue
        item = dict(source)
        item["concept_id"] = expected_cid
        challenges.append(item)
        existing_ids.add(item["id"])
        added.append(topic)
    return {"added": len(added), "topics": added, "skipped": skipped}
