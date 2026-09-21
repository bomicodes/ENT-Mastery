"""v41.8: add ECoG and VEMP workflow fundamentals to Audiology."""
from copy import deepcopy


_CASES = [
    {
        "id": "audfund9",
        "level": 4,
        "variant_type": "interpret",
        "concept_id": "audiology:fundamentals-ecog",
        "prompt": (
            "Electrocochleography (ECoG) records cochlear and distal auditory-nerve "
            "potentials after an acoustic stimulus. What are its principal components, "
            "and how is ECoG used clinically?"
        ),
        "answer": (
            "The cochlear microphonic (CM) is an alternating receptor potential that "
            "follows the stimulus waveform and chiefly reflects hair-cell activity; the "
            "summating potential (SP) is a sustained direct-current hair-cell response; "
            "and the compound action potential (AP) reflects synchronized distal auditory-"
            "nerve firing and corresponds closely to ABR wave I. An elevated SP/AP ratio "
            "may support endolymphatic hydrops/Ménière disease, but technique- and lab-"
            "specific norms are required. ECoG can also monitor cochlear responses during "
            "cochlear implantation and selected otologic procedures."
        ),
        "why": (
            "ECoG samples receptor and distal neural responses close to their source, but "
            "no single waveform or SP/AP cutoff establishes Ménière disease. Its value is "
            "as an adjunct to the clinical history and serial audiometry, or as real-time "
            "physiologic monitoring during surgery."
        ),
        "follow": "Why is ECoG supportive rather than diagnostic for Ménière disease?",
        "follow_answer": (
            "Sensitivity and specificity are imperfect, SP/AP measurement and cutoffs vary "
            "with transtympanic versus extratympanic technique and between laboratories, "
            "and a normal study does not exclude disease. Definite Ménière disease remains "
            "a clinical diagnosis using Bárány Society/AAO-HNS criteria."
        ),
    },
    {
        "id": "audfund10",
        "level": 3,
        "variant_type": "interpret",
        "concept_id": "audiology:fundamentals-vemp-in-audiology",
        "prompt": (
            "VEMPs are vestibular tests commonly performed in an audiology evoked-potential "
            "workflow. How are cVEMP and oVEMP recorded, and what does each chiefly assess?"
        ),
        "answer": (
            "For cVEMP, surface electrodes record an inhibitory response from an activated "
            "sternocleidomastoid; it chiefly assesses the saccule and inferior vestibular "
            "nerve. For oVEMP, electrodes below the eyes record an excitatory, usually "
            "contralateral extraocular response; it chiefly assesses the utricle and superior "
            "vestibular nerve. Loud air-conducted clicks or tone bursts are common stimuli; "
            "bone-conducted vibration can be used when conductive attenuation would make an "
            "air-conducted response unreliable. Amplitude, latency, threshold, symmetry, age, "
            "muscle activation, stimulus, and laboratory norms all affect interpretation."
        ),
        "why": (
            "The audiologist uses surface electrodes, amplification, artifact rejection, and "
            "signal averaging familiar from other evoked-potential studies, but VEMPs answer "
            "a vestibular end-organ question. They are selected for indications such as "
            "suspected otolith/nerve-division dysfunction or third-window physiology, not "
            "automatically added to every asymmetric or sudden hearing-loss evaluation."
        ),
        "follow": "Why does conductive hearing loss matter before air-conducted VEMP testing?",
        "follow_answer": (
            "Conductive pathology attenuates the stimulus reaching the inner ear and can "
            "falsely reduce or abolish an air-conducted VEMP. Bone-conducted stimulation, "
            "correction of the conductive problem, and technique-specific norms help avoid "
            "a false-negative interpretation."
        ),
    },
]


def apply_interpretation_labs_audiology_ecog_vemp_v418(data_module, app_module=None):
    labs = getattr(data_module, "INTERPRETATION_LABS", None)
    if not isinstance(labs, dict):
        raise RuntimeError("v41.8: INTERPRETATION_LABS unavailable")
    audiology = labs.get("audiology")
    if not isinstance(audiology, dict):
        raise RuntimeError("v41.8: missing audiology lab")

    existing = {case.get("id") for case in audiology.get("cases", [])}
    added = []
    for case in _CASES:
        if case["id"] not in existing:
            audiology["cases"].append(deepcopy(case))
            existing.add(case["id"])
            added.append(case["id"])

    if app_module is not None:
        app_module.INTERPRETATION_LABS = data_module.INTERPRETATION_LABS
    return {"audiology_ecog_vemp_added": added}
