"""v42.9: oral-cavity neck management and AJCC 8 stage grouping.

The 4 mm DOI threshold is a common decision aid, not a universal rule:
the D'Cruz trial established benefit for elective neck dissection in early
oral cancer and found a steep rise in occult-node risk between 3 and 4 mm.
ASCO separately recommends elective dissection for most cT1-4 cN0 oral SCC.
"""

import re


DOI_MARKER = "DOI DECISION POINT (4 MM)"

WORKUP_ADDITION = (
    " DOI DECISION POINT (4 MM): measure depth of invasion (DOI) from the adjacent normal "
    "mucosal basement membrane to the deepest invasive front, distinct from tumor thickness. "
    "In early cN0 oral cancer, DOI at or above approximately 4 mm strengthens the case for elective "
    "neck treatment even when the primary appears small. The D'Cruz randomized trial supports elective "
    "dissection in early oral cancer and observed a marked increase in occult nodal risk between 3 and "
    "4 mm; it did not randomize patients to a 4 mm treatment rule. ASCO recommends elective neck "
    "dissection for most surgically treated cT1-4 cN0 oral SCC, with close ultrasound surveillance "
    "reserved for selected, reliable cT1 patients. Sentinel-node biopsy is an alternative in an "
    "experienced program. Reassess the untreated neck when final pathology reveals unexpected depth."
)

MANAGE_ADDITION = (
    " NECK LEVELS AND LATERALITY: elective dissection in a cN0 oral cavity neck includes "
    "ipsilateral levels Ia, Ib, II and III. For a cN+ neck, ASCO describes therapeutic selective "
    "dissection of Ia, Ib, IIa, IIb, III and IV, extending to level V when disease distribution "
    "warrants it; clinically positive nodes do not automatically require a modified radical I-V "
    "dissection. Consider elective contralateral treatment for a primary crossing or closely "
    "approaching midline, especially a floor-of-mouth or tongue-tip primary with bilateral drainage. "
    "The exact distance is not a validated universal 1 cm rule: consider site, DOI, lateralization, "
    "stage and ipsilateral burden. A confirmed contralateral node makes that side therapeutic, with "
    "extent tailored to its disease. Pathologic extranodal extension (ENE) modifies the AJCC 8 "
    "N category and, like a positive margin, supports postoperative concurrent cisplatin-based "
    "chemoradiation in eligible patients."
)

TEACH_ADDITION = (
    " AJCC 8 ORAL CAVITY STAGE PEARL: for M0 disease, T1-3 N1 is Stage III; T4a or N2 "
    "raises the group to IVA, and T4b or N3 to IVB. Thus a small T1N1M0 oral tongue cancer "
    "is Stage III. Do not apply this rule to HPV-mediated oropharyngeal cancer, which has a "
    "different staging system. Clinical gross ENE is cN3b; pathologic ENE can raise pN1 "
    "to pN2. Pair group staging with the approximate 4 mm DOI risk threshold, the ASCO "
    "cN0 recommendation, and individual assessment of contralateral drainage."
)


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


CLINICAL_CHALLENGES_NEW = [
    {
        "id": "v429-oral-cavity-doi-threshold-01",
        "domain": "Head & Neck Oncology", "topic": "Oral Tongue SCC",
        "stem": "A small cN0 oral tongue SCC was excised without neck treatment. Final pathology shows 5 mm depth of invasion and clear margins. What should be discussed next?",
        "choices": [
            "Observe solely because the lesion was clinically small",
            "Reassess and offer elective treatment of the at-risk neck; the 5 mm DOI strengthens the indication despite a small primary",
            "Irradiate only the primary site to treat occult neck disease",
            "Re-excise the clear primary margins in place of neck treatment",
        ],
        "answer": 1,
        "explanation": "A 5 mm DOI increases the concern for occult metastasis. Elective treatment of the at-risk neck should be offered even for a small primary; discuss an appropriate elective dissection or an accepted alternative in an experienced program. The 4 mm value is a useful risk threshold, not an absolute rule that overrides the broader cN0 guideline.",
        "why_wrong": [
            "Small surface dimensions do not remove occult nodal risk associated with 5 mm invasion.",
            "Correct.",
            "Primary-only radiation does not address the neck.",
            "Clear margins do not create an indication for re-excision, and re-excision does not treat the neck.",
        ],
        "board_pearl": "DOI around 4 mm or greater strengthens the elective-neck indication; evaluate the cN0 neck even for a small oral primary.",
        "curveball": "What if a dissected node shows pathologic extranodal extension?",
        "curveball_answer": "Pathologic ENE raises the AJCC 8 nodal category and is a major indication for postoperative concurrent cisplatin-based chemoradiation when the patient is eligible.",
        "tier": "Curated board-style", "mode": "Clinical discrimination",
    },
    {
        "id": "v429-oral-cavity-staging-pearl-01",
        "domain": "Head & Neck Oncology", "topic": "Oral Tongue SCC",
        "stem": "A 1.2 cm oral tongue SCC with DOI 3 mm has one 2 cm ipsilateral node without extranodal extension and no distant disease (T1N1M0). What is its AJCC 8 overall stage group?",
        "choices": ["Stage I", "Stage II", "Stage III", "Stage IVA"],
        "answer": 2,
        "explanation": "T1N1M0 oral-cavity cancer is Stage III under AJCC 8. The single ipsilateral node makes this N1, provided there is no ENE.",
        "why_wrong": [
            "Stage I requires T1N0M0.",
            "Stage II requires T2N0M0.",
            "Correct.",
            "Stage IVA requires T4a or N2 here; this is T1N1M0.",
        ],
        "board_pearl": "For oral cavity SCC with M0, T1-3N1 is Stage III; HPV-mediated oropharyngeal staging differs.",
        "curveball": "If pathology shows extranodal extension in that same node, how do the nodal category and stage change?",
        "curveball_answer": "A single ipsilateral node no larger than 3 cm with pathologic ENE becomes pN2a; with T1 and M0 the overall group becomes Stage IVA. Gross clinical ENE instead is cN3b and Stage IVB.",
        "tier": "Curated board-style", "mode": "Reasoning",
    },
    {
        "id": "v429-oral-cavity-bilateral-neck-01",
        "domain": "Head & Neck Oncology", "topic": "Oral Tongue SCC",
        "stem": "A cT2 floor-of-mouth SCC reaches the midline; both necks are clinically negative. What neck plan best addresses its drainage pattern?",
        "choices": [
            "Ipsilateral elective treatment only, because neither neck has a palpable node",
            "Consider bilateral elective neck treatment because the primary reaches midline and floor-of-mouth drainage can be bilateral",
            "Observe both necks solely because imaging is negative",
            "Perform a contralateral comprehensive dissection only",
        ],
        "answer": 1,
        "explanation": "A floor-of-mouth primary reaching midline risks contralateral occult spread. Bilateral elective treatment should be considered, with laterality and extent chosen from the site, DOI, and overall nodal risk.",
        "why_wrong": [
            "An ipsilateral-only plan may miss contralateral occult disease in this midline primary.",
            "Correct.",
            "Negative clinical imaging does not exclude occult nodes in a cT2 midline primary.",
            "A negative contralateral neck calls for elective rather than therapeutic treatment, and the ipsilateral neck remains at risk.",
        ],
        "board_pearl": "Midline floor-of-mouth tumors warrant a deliberate contralateral-neck decision; elective levels Ia-III cover the typical cN0 oral cavity neck.",
        "curveball": "What changes if an ipsilateral 2 cm node is clinically positive?",
        "curveball_answer": "Treat the positive side therapeutically. ASCO describes selective dissection of levels Ia, Ib, IIa, IIb, III and IV for a cN+ oral cavity neck; include level V when disease distribution warrants it. Continue to assess the contralateral elective risk separately.",
        "tier": "Curated board-style", "mode": "Clinical discrimination",
    },
]


def apply_oral_cavity_neck_dissection_depth_v429(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    result = {"deepened": False, "challenges_added": []}
    oral = next((card for card in modules.get("Head & Neck Oncology", []) if card.get("topic") == "Oral Tongue SCC"), None)
    if oral is None:
        raise RuntimeError("v42.9: Oral Tongue SCC missing from curriculum")
    if DOI_MARKER not in (oral.get("workup") or ""):
        for key, addition in (("workup", WORKUP_ADDITION), ("manage", MANAGE_ADDITION), ("teach", TEACH_ADDITION)):
            oral[key] = (oral.get(key) or "").rstrip() + addition
        for tag in ("depth of invasion threshold", "contralateral neck treatment", "extranodal extension", "AJCC 8 staging"):
            if tag not in oral.setdefault("tags", []):
                oral["tags"].append(tag)
        for source in (
            "D'Cruz AK et al. Elective versus Therapeutic Neck Dissection in Node-Negative Oral Cancer. N Engl J Med. 2015;373:521-529 (trial and DOI subgroup).",
            "Koyfman SA et al. Management of the Neck in Squamous Cell Carcinoma of the Oral Cavity and Oropharynx: ASCO Clinical Practice Guideline. J Clin Oncol. 2019;37:1753-1774.",
            "AJCC Cancer Staging Manual, 8th ed., oral cavity stage grouping and ENE categories.",
        ):
            if source not in oral.setdefault("source_basis", []):
                oral["source_basis"].append(source)
        result["deepened"] = True
    challenges = data_module.CLINICAL_CHALLENGES_V119
    existing_ids = {q.get("id") for q in challenges}
    for question in CLINICAL_CHALLENGES_NEW:
        if question["id"] not in existing_ids:
            row = dict(question)
            row["concept_id"] = _v6_item_id("Head & Neck Oncology", "Oral Tongue SCC")
            challenges.append(row)
            existing_ids.add(row["id"])
            result["challenges_added"].append(row["id"])
    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in challenges if q.get("id")}
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.CLINICAL_CHALLENGES_V119 = challenges
        app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119
    return result
