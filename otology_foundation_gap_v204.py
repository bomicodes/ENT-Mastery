"""v20.4 — one proven Otology foundation gap.

The runtime reconciliation established that Superior Canal Dehiscence has a
strong second-pass application case but no separate live canonical foundation
question. Add exactly that missing layer before the final Otology reconciler;
do not manufacture foundations for concepts that already have them.
"""

DOMAIN = "Otology / Neurotology"
TOPIC = "Superior Canal Dehiscence"

SSCD_FOUNDATION_V204 = {
    "id": "v204_oto_sscd_fnd",
    "domain": DOMAIN,
    "topic": TOPIC,
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
}


def apply_otology_foundation_gap_v204(challenges, id_factory):
    expected_cid = id_factory(DOMAIN, TOPIC)
    existing = {q.get("id") for q in challenges if q.get("id")}
    if SSCD_FOUNDATION_V204["id"] in existing:
        return {"added": 0, "topic": TOPIC}

    # Do not create a second explicit foundation if another runtime patch has
    # already supplied one for the same canonical concept.
    for q in challenges:
        if q.get("concept_id") == expected_cid and q.get("learning_stage") == "foundation":
            return {"added": 0, "topic": TOPIC}

    item = dict(SSCD_FOUNDATION_V204)
    item["concept_id"] = expected_cid
    challenges.append(item)
    return {"added": 1, "topic": TOPIC}
