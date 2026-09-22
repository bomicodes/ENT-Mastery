"""v43.0: tensor veli palatini and middle-ear disease in cleft palate."""

import re


TVP_MARKER = "TENSOR VELI PALATINI MECHANISM"

RECOGNIZE_ADDITION = (
    " Children with cleft palate are prone to persistent otitis media with effusion (OME), "
    "conductive hearing loss, and sometimes recurrent acute otitis media (AOM). Distinguish "
    "the highly prevalent effusion from recurrent acute infection, which is not inevitable."
)
LOCALIZE_ADDITION = (
    " TENSOR VELI PALATINI MECHANISM: the tensor veli palatini (TVP) is the primary "
    "active dilator of the cartilaginous Eustachian tube. Its tendon passes around the "
    "pterygoid hamulus into the palatal aponeurosis; coordinated contraction during swallowing "
    "pulls the tubal wall open to ventilate the middle ear. Cleft-associated variation in TVP "
    "attachment and orientation, together with altered tubal cartilage and compliance, can "
    "impair opening and promote negative middle-ear pressure and effusion. The levator veli "
    "palatini chiefly raises the palate for velopharyngeal closure and speech, although its "
    "movement may assist the earlier phase of tubal opening. The mechanism is multifactorial "
    "rather than a proven single cleft-margin insertion defect in every patient."
)
TEACH_ADDITION = (
    " Board pearl: tensor veli palatini is the primary active Eustachian-tube dilator; "
    "levator veli palatini is central to the speech-related velopharyngeal sling. Palate repair "
    "does not reliably resolve middle-ear disease. Continue age-appropriate audiology and "
    "middle-ear surveillance after repair; consider tympanostomy tubes when persistent OME "
    "with hearing difficulty or recurrent AOM with effusion meets criteria, including when "
    "assessment at palate repair supports placement."
)


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


CLINICAL_CHALLENGES_NEW = [{
    "id": "v430-cleft-tvp-otitis-media-01",
    "domain": "Pediatric Otolaryngology",
    "topic": "Cleft / Craniofacial Otologic-Airway Care",
    "stem": (
        "An infant with cleft palate has persistent middle-ear effusion and conductive hearing "
        "loss. Which palatal muscle is the primary active dilator of the cartilaginous "
        "Eustachian tube during swallowing?"
    ),
    "choices": ["Levator veli palatini", "Tensor veli palatini", "Musculus uvulae", "Palatopharyngeus"],
    "answer": 1,
    "explanation": (
        "Tensor veli palatini is the primary active Eustachian-tube dilator. Its tendon passes "
        "around the pterygoid hamulus and acts on the tubal wall during swallowing. Cleft-related "
        "muscle and tubal structural differences impair ventilation and favor persistent effusion; "
        "the cause is not necessarily one abnormal insertion pattern in every child."
    ),
    "why_wrong": [
        "Levator veli palatini forms the velopharyngeal sling for speech and can contribute to "
        "tubal movements, but it is not the primary active dilator.",
        "Correct.",
        "Musculus uvulae contributes to palatal bulk and closure, not the main tubal dilation force.",
        "Palatopharyngeus helps pharyngeal and palatal movement, not primary active tubal dilation.",
    ],
    "board_pearl": "TVP primarily dilates the Eustachian tube; levator mainly supports velopharyngeal closure. OME is particularly common in cleft palate.",
    "curveball": "Does successful palatoplasty end the need for ear and hearing follow-up?",
    "curveball_answer": (
        "No. Ear disease can persist after repair. Follow middle-ear status and hearing longitudinally; "
        "consider tubes for persistent effusion with hearing difficulty or recurrent AOM with "
        "effusion according to the child's examination and guideline criteria."
    ),
    "tier": "Curated board-style", "mode": "Clinical discrimination",
}]


def apply_cleft_palate_tensor_veli_palatini_v430(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    row = next((c for c in modules.get("Pediatric Otolaryngology", [])
                if c.get("topic") == "Cleft / Craniofacial Otologic-Airway Care"), None)
    if row is None:
        raise RuntimeError("v43.0: cleft otologic-airway topic missing from curriculum")
    result = {"deepened": False, "challenges_added": []}
    if TVP_MARKER not in (row.get("localize") or ""):
        for field, addition in (("recognize", RECOGNIZE_ADDITION),
                                ("localize", LOCALIZE_ADDITION), ("teach", TEACH_ADDITION)):
            row[field] = (row.get(field) or "").rstrip() + addition
        for tag in ("tensor veli palatini", "Eustachian tube dysfunction", "otitis media with effusion"):
            if tag not in row.setdefault("tags", []):
                row["tags"].append(tag)
        for source in (
            "Heidsieck DSP et al. The role of the tensor veli palatini muscle in the development of cleft palate-associated middle ear problems. Clin Oral Investig. 2016;20:1389-1401. doi:10.1007/s00784-016-1828-x.",
            "Rosenfeld RM et al. Clinical Practice Guideline: Tympanostomy Tubes in Children (Update). Otolaryngol Head Neck Surg. 2022;166:S1-S55.",
        ):
            if source not in row.setdefault("source_basis", []):
                row["source_basis"].append(source)
        result["deepened"] = True
    challenges = data_module.CLINICAL_CHALLENGES_V119
    existing = {q.get("id") for q in challenges}
    for question in CLINICAL_CHALLENGES_NEW:
        if question["id"] not in existing:
            new_row = dict(question)
            new_row["concept_id"] = _v6_item_id("Pediatric Otolaryngology", question["topic"])
            challenges.append(new_row)
            existing.add(new_row["id"])
            result["challenges_added"].append(new_row["id"])
    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in challenges if q.get("id")}
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.CLINICAL_CHALLENGES_V119 = challenges
        app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119
    return result
