"""v96: choosing the vestibular schwannoma approach by hearing, size and location."""

VS = "v6-otology-neurotology-vestibular-schwannoma"

VIGNETTES = [
    {
        "topic": "Vestibular Schwannoma",
        "concept_id": VS,
        "stem": "A healthy 38-year-old has an 8-mm intracanalicular vestibular schwannoma that fills the lateral internal auditory canal to the fundus, with no CSF between tumor and fundus and no extension into the cerebellopontine angle. Pure-tone average is 20 dB and word recognition 96%. After counseling she chooses surgery over observation or radiosurgery. Which approach gives the best chance of preserving hearing?",
        "choices": [
            "Translabyrinthine",
            "Retrosigmoid",
            "Middle cranial fossa",
            "Transcochlear",
        ],
        "answer": 2,
        "explanation": "The middle fossa approach exposes the entire internal auditory canal from above, including the fundus, without entering the labyrinth, so it is the hearing-preservation route of choice for small intracanalicular tumors that reach the fundus in younger patients with good hearing. A retrosigmoid approach reaches the canal from behind and cannot clear the lateral third without drilling toward the posterior semicircular canal and vestibule, which risks the hearing it aims to save. The tradeoff of the middle fossa route is the highest facial nerve risk, because the nerve lies above the tumor in the surgical path.",
        "why_wrong": [
            "Translabyrinthine surgery sacrifices hearing, so it is not chosen when hearing is excellent and preservation is the goal.",
            "Retrosigmoid suits tumors centered medially with CSF at the fundus; clearing a filled fundus from behind threatens the labyrinth.",
            "Correct.",
            "Transcochlear surgery sacrifices hearing and is reserved for extensive petrous or anterior lesions.",
        ],
        "board_pearl": "Small intracanalicular tumor reaching the fundus, good hearing, younger patient: middle cranial fossa.",
        "curveball": "Why is the middle fossa approach used more cautiously in patients over about 65?",
        "curveball_answer": "Older patients have thinner, more adherent temporal dura that tears more easily, and they tolerate temporal lobe retraction less well. Observation or radiosurgery is often preferred for small tumors in this group.",
        "learning_stage": "application",
        "focus": "surgery",
    },
    {
        "topic": "Vestibular Schwannoma",
        "concept_id": VS,
        "stem": "A 50-year-old has a vestibular schwannoma with a 15-mm cerebellopontine angle component and a short intracanalicular part that stops well short of the fundus, leaving a bright CSF cap laterally on T2 MRI. Pure-tone average is 30 dB and word recognition 88%. He wants to try to keep his hearing. Which approach is most appropriate?",
        "choices": [
            "Middle cranial fossa",
            "Retrosigmoid",
            "Translabyrinthine",
            "Observation is the only option once the tumor enters the CPA",
        ],
        "answer": 1,
        "explanation": "With serviceable hearing, a tumor centered in the cerebellopontine angle and a CSF cap at the fundus, the retrosigmoid approach offers the best exposure of the CPA with a chance of hearing preservation: the lateral canal does not need to be cleared, so the labyrinth can be left intact. The middle fossa approach handles the canal well but is limited for a CPA component beyond about 1 cm. Translabyrinthine surgery would give excellent exposure but sacrifices hearing.",
        "why_wrong": [
            "The middle fossa approach gives limited access to a CPA component of this size.",
            "Correct.",
            "It would sacrifice hearing that is still serviceable and the patient wants to preserve.",
            "Observation and radiosurgery remain options at this size, but surgery is not excluded once the tumor reaches the CPA.",
        ],
        "board_pearl": "Serviceable hearing, tumor centered in the CPA with CSF at the fundus, up to about 1.5 to 2 cm: retrosigmoid.",
        "curveball": "What preoperative findings predict a better chance of hearing preservation?",
        "curveball_answer": "A small tumor, excellent word recognition, a CSF cap at the fundus, preserved ABR waveforms, and origin from the superior rather than the inferior vestibular nerve.",
        "learning_stage": "application",
        "focus": "surgery",
    },
    {
        "topic": "Vestibular Schwannoma",
        "concept_id": VS,
        "stem": "A 57-year-old has a 22-mm vestibular schwannoma that touches the brainstem without hydrocephalus. The affected ear has a pure-tone average of 70 dB and word recognition of 20%. The other ear is normal. He chooses surgery. Which approach is generally preferred?",
        "choices": [
            "Middle cranial fossa",
            "Retrosigmoid with a hearing-preservation attempt",
            "Translabyrinthine",
            "Extended middle fossa",
        ],
        "answer": 2,
        "explanation": "When hearing is not serviceable, the translabyrinthine approach is the most direct route to the internal auditory canal and cerebellopontine angle. It identifies the facial nerve reliably at the fundus, needs little cerebellar retraction, and has a low rate of chronic headache. Because the hearing is already lost, sacrificing the labyrinth costs nothing functionally. A retrosigmoid approach is still reasonable, especially for large tumors with wide posterior fossa extension, but there is no hearing worth preserving here.",
        "why_wrong": [
            "The middle fossa approach is for small intracanalicular tumors with good hearing and cannot handle a 22-mm CPA tumor.",
            "There is no serviceable hearing to preserve at a word recognition of 20%.",
            "Correct.",
            "Extended middle fossa exposure suits small CPA extensions, not a 22-mm tumor contacting the brainstem.",
        ],
        "board_pearl": "Nonserviceable hearing at almost any tumor size: translabyrinthine is the default; retrosigmoid is the main alternative for large tumors.",
        "curveball": "During dissection the capsule is densely adherent to the facial nerve. What do you do?",
        "curveball_answer": "Leave a thin, planned remnant on the nerve (near-total resection) rather than risk permanent facial paralysis, then follow it with MRI and treat with radiosurgery if it grows. Facial nerve function outweighs gross-total removal.",
        "learning_stage": "application",
        "focus": "surgery",
    },
]
