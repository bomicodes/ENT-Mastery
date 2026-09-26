"""ENT Mastery v46.0 -- Learning-ladder gapfill: Head & Neck Oncology.

Adds foundation/application/senior_decision Clinical Challenge vignettes for
the 3 Head & Neck Oncology topics flagged by audit_domain_ladder_inventory_v217.py
as having no deliberately-reviewed ladder row (recently-added topics that never
got this pass). Grounded in each topic's existing Deep Curriculum content --
no new clinical facts, numbers, or staging systems introduced beyond what that
content already states.
"""
from copy import deepcopy

DOMAIN = "Head & Neck Oncology"

NEW_QUESTIONS = [
    # ---------------------------------------------------------------
    # Sentinel Lymph Node Biopsy in Oral Cavity Cancer
    # concept_id: v6-head-neck-oncology-sentinel-lymph-node-biopsy-in-oral-cavity-cancer
    # ---------------------------------------------------------------
    {
        "id": "v460_hn_slnb_fnd",
        "domain": DOMAIN,
        "topic": "Sentinel Lymph Node Biopsy in Oral Cavity Cancer",
        "stem": (
            "A patient has a biopsy-proven cT1 squamous cell carcinoma of the lateral "
            "tongue. Examination and imaging show no palpable or radiographic evidence "
            "of cervical adenopathy. The multidisciplinary team has an established "
            "lymphatic mapping program. What is sentinel lymph node biopsy being used "
            "for in this patient?"
        ),
        "choices": [
            "Definitive treatment of the primary tumor",
            "A staging procedure to sample first-echelon nodes in a clinically node-negative neck",
            "A screening test to decide whether the primary tumor requires re-excision",
            "A procedure reserved for patients with a clinically node-positive neck",
        ],
        "answer": 1,
        "explanation": (
            "SLNB is a staging option for selected early (cT1-2), clinically node-negative "
            "(cN0) oral-cavity SCC, performed within a validated multidisciplinary program. "
            "It identifies first-echelon lymphatic drainage for intensive pathologic "
            "examination; it does not treat the primary tumor and is not indicated for an "
            "overtly node-positive neck."
        ),
        "why_wrong": [
            "SLNB samples nodes for staging; it is not treatment of the primary tumor, which is addressed separately.",
            "Correct.",
            "SLNB evaluates regional nodal status, not margin adequacy at the primary site.",
            "SLNB is specifically for the cN0 neck; an overtly node-positive neck is managed with pathology- and protocol-directed neck treatment rather than sentinel mapping.",
        ],
        "board_pearl": (
            "SLNB is staging, not primary-tumor treatment -- reserved for early cT1-2, "
            "cN0 oral-cavity SCC in a program with real mapping and pathology support."
        ),
        "curveball": (
            "What technique is used intraoperatively to identify the first-echelon "
            "nodes, and what anatomic pitfall can complicate localization for floor-of-mouth "
            "primaries?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-sentinel-lymph-node-biopsy-in-oral-cavity-cancer",
        "learning_stage": "foundation",
        "curveball_answer": (
            "Peritumoral tracer (lymphoscintigraphy/SPECT-CT protocol) identifies first-echelon "
            "lymphatic drainage, and an intraoperative probe is used to localize and excise the "
            "mapped sentinel nodes, with step-sectioning and immunohistochemistry improving "
            "detection of small deposits. Floor-of-mouth primaries are a recognized pitfall "
            "because injection-site 'shine-through' near the primary can obscure or complicate "
            "identification of the true first-echelon node."
        ),
        "ladder_reviewed": True,
        "focus": "boards",
    },
    {
        "id": "v460_hn_slnb_app",
        "domain": DOMAIN,
        "topic": "Sentinel Lymph Node Biopsy in Oral Cavity Cancer",
        "stem": (
            "A cT2N0 oral tongue SCC patient undergoes attempted sentinel lymph node "
            "mapping. Lymphoscintigraphy shows poor tracer uptake and the surgical team "
            "is not confident that all first-echelon nodes have been reliably identified "
            "intraoperatively. Pathology support for step-sectioning is also limited at "
            "this center. What is the most appropriate next step?"
        ),
        "choices": [
            "Proceed with excision of whatever nodes were found and call the SLNB complete",
            "Abandon nodal staging altogether and observe the neck",
            "Convert to elective neck dissection given the technically inadequate mapping and limited pathology support",
            "Repeat the tracer injection intraoperatively using a different radiotracer dose without changing the plan",
        ],
        "answer": 2,
        "explanation": (
            "SLNB's safety depends on selection, mapping quality, pathology processing, and "
            "an experienced team. Elective neck dissection remains a valid alternative and is "
            "preferred specifically when mapping expertise, pathology support, or reliable "
            "follow-up is unavailable -- exactly the scenario of poor uptake and limited "
            "step-sectioning capability described here."
        ),
        "why_wrong": [
            "A technically inadequate mapping procedure should not be treated as an equivalent, reliable staging result.",
            "A cT2N0 oral cavity primary still requires nodal staging; abandoning staging is not appropriate.",
            "Correct.",
            "The issue described is inadequate mapping and pathology support, not simply an insufficient tracer dose; the appropriate response is to fall back to a proven alternative rather than repeat an unreliable technique.",
        ],
        "board_pearl": (
            "When mapping quality, pathology support, or follow-up cannot be assured, elective "
            "neck dissection -- not a marginal SLNB -- is the safer staging choice."
        ),
        "curveball": (
            "If elective neck dissection is chosen instead, what is different about how nodal "
            "positivity discovered on final pathology from a neck dissection is acted upon "
            "compared with a positive sentinel node?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-sentinel-lymph-node-biopsy-in-oral-cavity-cancer",
        "learning_stage": "application",
        "curveball_answer": (
            "In both pathways, positive findings trigger pathology- and protocol-directed neck "
            "treatment and adjuvant decision-making rather than one automatic response for every "
            "deposit -- the underlying management logic (further neck treatment and adjuvant "
            "therapy decisions driven by the extent and character of nodal disease) is the same "
            "regardless of whether the positive node was identified via sentinel mapping or "
            "within a completed neck dissection specimen."
        ),
        "ladder_reviewed": True,
        "focus": "OR_prep",
    },
    {
        "id": "v460_hn_slnb_snr",
        "domain": DOMAIN,
        "topic": "Sentinel Lymph Node Biopsy in Oral Cavity Cancer",
        "stem": (
            "A patient with a cT1N0 floor-of-mouth SCC undergoes SLNB. The excised "
            "sentinel node, after step-sectioning and immunohistochemistry, shows a small "
            "focus of metastatic carcinoma. The surgeon is deciding how to proceed. What "
            "is the most appropriate senior-level management framework?"
        ),
        "choices": [
            "Treat every positive sentinel node identically with completion neck dissection regardless of the pathologic details",
            "Ignore the finding since the primary tumor was small and low stage",
            "Base further neck treatment and adjuvant decisions on the specific pathologic and protocol-directed findings rather than applying one uniform response",
            "Repeat the SLNB on the contralateral neck before making any decision",
        ],
        "answer": 2,
        "explanation": (
            "Positive SLNB findings trigger pathology- and protocol-directed neck treatment and "
            "adjuvant decision-making rather than one automatic response for every deposit. A "
            "senior decision-maker weighs the specific pathologic findings (e.g., extent of "
            "involvement) within the established protocol rather than reflexively applying a "
            "single fixed pathway to every positive result."
        ),
        "why_wrong": [
            "The framework explicitly rejects a single automatic response for every positive deposit; the specific pathologic findings and protocol matter.",
            "A negative technically adequate SLNB can permit surveillance, but this SLNB was positive -- a positive result cannot be disregarded regardless of primary tumor size.",
            "Correct.",
            "There is no basis in a unilateral floor-of-mouth primary's staging pathway for repeating sentinel mapping on the uninvolved contralateral neck as the next step.",
        ],
        "board_pearl": (
            "A positive sentinel node is not a single-branch decision tree -- pathology- and "
            "protocol-directed nuance (not one default reflex) governs what happens next."
        ),
        "curveball": (
            "What would a negative, technically adequate SLNB have permitted instead?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-sentinel-lymph-node-biopsy-in-oral-cavity-cancer",
        "learning_stage": "senior_decision",
        "curveball_answer": (
            "A negative, technically adequate SLNB can permit surveillance rather than committing "
            "the patient to elective neck dissection or further neck treatment."
        ),
        "ladder_reviewed": True,
        "focus": "postoperative_call",
    },
    # ---------------------------------------------------------------
    # Villaret Syndrome (Retroparotid Space Syndrome)
    # concept_id: v6-head-neck-oncology-villaret-syndrome-retroparotid-space-syndrome
    # ---------------------------------------------------------------
    {
        "id": "v460_hn_vill_fnd",
        "domain": DOMAIN,
        "topic": "Villaret Syndrome (Retroparotid Space Syndrome)",
        "stem": (
            "A patient presents with ipsilateral hoarseness, dysphagia, shoulder droop, "
            "and tongue deviation, consistent with combined CN IX, X, XI, and XII palsy. "
            "On the same side, the examiner also notes ptosis, miosis, and facial "
            "anhidrosis. Which syndrome does this combination of findings describe?"
        ),
        "choices": [
            "Vernet syndrome",
            "Collet-Sicard syndrome",
            "Villaret syndrome",
            "Isolated CN XII palsy",
        ],
        "answer": 2,
        "explanation": (
            "Ipsilateral CN IX, X, XI, and XII palsy plus Horner syndrome (ptosis, miosis, "
            "anhidrosis) is Villaret syndrome -- Collet-Sicard syndrome (IX-XII) with the "
            "added finding of sympathetic-chain injury, which localizes the lesion to the "
            "retroparotid space rather than the jugular foramen or skull base alone."
        ),
        "why_wrong": [
            "Vernet syndrome involves the jugular foramen only (CN IX, X, XI), without CN XII involvement and without Horner syndrome.",
            "Collet-Sicard syndrome is CN IX-XII palsy at the skull base, but without Horner syndrome -- the Horner findings here are what distinguish this case.",
            "Correct.",
            "The findings describe combined CN IX-XII palsy plus Horner syndrome, not an isolated single nerve deficit.",
        ],
        "board_pearl": (
            "Horner syndrome is the key discriminator that elevates a lower-cranial-nerve "
            "syndrome from Collet-Sicard to Villaret, because it means the sympathetic chain "
            "in the retroparotid space is also involved."
        ),
        "curveball": (
            "Anatomically, what structures does the retroparotid space contain that explains "
            "why a single lesion there can produce all of these deficits together?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-villaret-syndrome-retroparotid-space-syndrome",
        "learning_stage": "foundation",
        "curveball_answer": (
            "The retroparotid (retrostyloid/poststyloid parapharyngeal) space contains the "
            "carotid sheath (ICA, IJV), cranial nerves IX-XII as they course extracranially, "
            "and the cervical sympathetic chain, all in close proximity immediately behind "
            "the parotid gland -- so a mass there can compress all of these structures at once."
        ),
        "ladder_reviewed": True,
        "focus": "boards",
    },
    {
        "id": "v460_hn_vill_app",
        "domain": DOMAIN,
        "topic": "Villaret Syndrome (Retroparotid Space Syndrome)",
        "stem": (
            "Two patients each present with ipsilateral CN IX, X, XI, and XII deficits. "
            "Patient A has no other cranial nerve or autonomic findings. Patient B has the "
            "same lower cranial nerve deficits plus ipsilateral ptosis, miosis, and facial "
            "anhidrosis. What single additional finding in Patient B changes the localization "
            "of the lesion compared with Patient A?"
        ),
        "choices": [
            "Tongue deviation, which is common to both patients",
            "Horner syndrome, indicating sympathetic-chain involvement and localizing to the retroparotid space rather than the skull base alone",
            "Hoarseness, which is also common to both patients",
            "Shoulder droop, which is also common to both patients",
        ],
        "answer": 1,
        "explanation": (
            "Patient A's presentation (isolated CN IX-XII palsy) is Collet-Sicard syndrome, "
            "localizing to the skull base. Patient B's added Horner syndrome (ptosis, miosis, "
            "anhidrosis) indicates the cervical sympathetic chain is also involved, which "
            "localizes the lesion to the retroparotid space -- this is what distinguishes "
            "Villaret from Collet-Sicard."
        ),
        "why_wrong": [
            "Tongue deviation (CN XII) is shared by both patients' lower cranial nerve findings and does not discriminate between the two syndromes.",
            "Correct.",
            "Hoarseness (CN X) is shared by both patients and does not discriminate between the two syndromes.",
            "Shoulder droop (CN XI) is shared by both patients and does not discriminate between the two syndromes.",
        ],
        "board_pearl": (
            "Collet-Sicard = IX-XII at the skull base, no Horner. Villaret = the same nerves "
            "plus Horner, because the lesion has extended into the retroparotid space where "
            "the sympathetic chain runs alongside the carotid sheath and CN IX-XII."
        ),
        "curveball": (
            "How does Vernet syndrome differ from both of these presentations?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-villaret-syndrome-retroparotid-space-syndrome",
        "learning_stage": "application",
        "curveball_answer": (
            "Vernet syndrome involves only the jugular foramen (CN IX, X, XI), without CN XII "
            "and without Horner syndrome -- it is the most limited of the three in both nerve "
            "involvement and anatomic extent."
        ),
        "ladder_reviewed": True,
    },
    {
        "id": "v460_hn_vill_snr",
        "domain": DOMAIN,
        "topic": "Villaret Syndrome (Retroparotid Space Syndrome)",
        "stem": (
            "A patient with Villaret syndrome from a retroparotid space mass is being "
            "evaluated for possible biopsy. Cross-sectional imaging of the poststyloid "
            "parapharyngeal compartment raises concern that the mass may be vascular in "
            "origin (e.g., a vagal or sympathetic-chain schwannoma or paraganglioma). What "
            "is the most appropriate next step before any biopsy is attempted?"
        ),
        "choices": [
            "Proceed directly to needle biopsy to establish histology as quickly as possible",
            "Characterize vascularity with appropriate vascular imaging before any needle biopsy of a suspected vascular lesion",
            "Skip further workup and proceed straight to resection without imaging characterization",
            "Defer all workup indefinitely since Horner syndrome makes biopsy unnecessary",
        ],
        "answer": 1,
        "explanation": (
            "Management of a retroparotid space mass follows the same logic as other "
            "parapharyngeal space tumors: characterize vascularity with vascular imaging "
            "before any needle biopsy of a suspected vascular lesion, then decide among "
            "observation, irradiation, or resection based on diagnosis, growth, and symptoms."
        ),
        "why_wrong": [
            "Proceeding directly to needle biopsy of a suspected vascular lesion without first characterizing vascularity risks hemorrhage and is not the recommended sequence.",
            "Correct.",
            "Resection without diagnostic and vascular imaging characterization skips a necessary step in appropriately planning the operation and counseling the patient.",
            "The presence of Horner syndrome localizes the lesion but does not itself establish a diagnosis or eliminate the need for imaging and vascular characterization.",
        ],
        "board_pearl": (
            "Any suspected vascular lesion in the retroparotid/parapharyngeal space needs "
            "vascular imaging characterization before needle biopsy is even considered."
        ),
        "curveball": (
            "If resection is ultimately chosen, what should be proactively planned for and "
            "counseled given the multi-nerve involvement typical of Villaret syndrome?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-villaret-syndrome-retroparotid-space-syndrome",
        "learning_stage": "senior_decision",
        "curveball_answer": (
            "Resection is tailored to the compartment and diagnosis; the surgeon should expect "
            "and counsel for potential permanent multi-nerve deficits (voice, swallow, shoulder "
            "function, and oculosympathetic findings) and plan functional rehabilitation "
            "proactively rather than reactively."
        ),
        "ladder_reviewed": True,
        "focus": "OR_prep",
    },
    # ---------------------------------------------------------------
    # Lip Cancer
    # concept_id: v6-head-neck-oncology-lip-cancer
    # ---------------------------------------------------------------
    {
        "id": "v460_hn_lip_fnd",
        "domain": DOMAIN,
        "topic": "Lip Cancer",
        "stem": (
            "A fair-skinned patient with a long history of outdoor work and chronic sun "
            "exposure presents with a non-healing, crusted, indurated lesion on the "
            "vermilion of the lower lip. What diagnosis should be at the top of the "
            "differential?"
        ),
        "choices": [
            "Squamous cell carcinoma of the lip",
            "A simple herpetic cold sore",
            "An aphthous ulcer",
            "A mucocele",
        ],
        "answer": 0,
        "explanation": (
            "A non-healing ulcer, crusted lesion, or induration of the vermilion -- far more "
            "often the lower lip than the upper lip -- in a patient with chronic UV exposure, "
            "smoking, fair skin, or immunosuppression should raise concern for lip squamous "
            "cell carcinoma."
        ),
        "why_wrong": [
            "Correct.",
            "A herpetic lesion is typically vesicular, self-limited, and recurrent rather than a chronic non-healing, indurated lesion in a patient with chronic UV risk factors.",
            "An aphthous ulcer classically occurs on non-keratinized intraoral mucosa and heals over days to weeks, unlike a chronic non-healing vermilion lesion.",
            "A mucocele is a soft, fluctuant, mucus-retention lesion, not an indurated, crusted, non-healing ulcer in a high-risk patient.",
        ],
        "board_pearl": (
            "Lower lip vermilion is the classic site for SCC in a chronically sun-exposed "
            "patient -- a non-healing, indurated lesion there is cancer until proven otherwise."
        ),
        "curveball": (
            "Why do commissure lesions carry distinct reconstructive implications compared "
            "with lesions elsewhere on the lip?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-lip-cancer",
        "learning_stage": "foundation",
        "curveball_answer": (
            "Commissure lesions are reconstructively challenging because there is less "
            "redundant tissue there and the commissure is functionally critical for oral "
            "competence and speech, so reconstruction has to preserve function as well as "
            "close the defect."
        ),
        "ladder_reviewed": True,
        "focus": "boards",
    },
    {
        "id": "v460_hn_lip_app",
        "domain": DOMAIN,
        "topic": "Lip Cancer",
        "stem": (
            "A patient with a biopsy-proven lower lip SCC reports new numbness of the chin "
            "and lower lip on the same side. There is no palpable neck mass. What does this "
            "finding suggest, and how should it change the workup?"
        ),
        "choices": [
            "It is an unrelated, incidental finding and requires no change to the standard workup",
            "It suggests perineural spread along the mental/inferior alveolar nerve, which should prompt imaging and adjust margin planning",
            "It confirms nodal metastasis and mandates immediate neck dissection without further imaging",
            "It indicates the tumor is upper lip in origin rather than lower lip",
        ],
        "answer": 1,
        "explanation": (
            "Perineural spread along the mental/inferior alveolar nerve can present as chin/lip "
            "numbness; this is a distinct risk that should change both imaging and margin "
            "planning when suspected, rather than being dismissed as incidental."
        ),
        "why_wrong": [
            "Chin/lip numbness in this setting is a recognized sign of perineural spread and should not be dismissed as incidental.",
            "Correct.",
            "Sensory numbness reflects perineural nerve involvement, not nodal disease, and does not by itself establish nodal metastasis or mandate neck dissection.",
            "Numbness reflects perineural spread patterns rather than indicating which lip subsite the primary tumor arose from.",
        ],
        "board_pearl": (
            "Chin or lip numbness in a lip cancer patient is a key trap for perineural spread "
            "along the mental/inferior alveolar nerve -- it should trigger targeted imaging and "
            "influence margin planning, not be written off as incidental."
        ),
        "curveball": (
            "Besides perineural spread, what other biopsy-derived finding helps estimate this "
            "patient's occult nodal risk, similar to oral cavity SCC?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-lip-cancer",
        "learning_stage": "application",
        "curveball_answer": (
            "Biopsy establishes histology and depth of invasion, which -- as in oral cavity "
            "SCC -- helps estimate occult nodal risk; deeper lesions carry higher occult nodal "
            "risk and a lower threshold for elective neck dissection."
        ),
        "ladder_reviewed": True,
    },
    {
        "id": "v460_hn_lip_snr",
        "domain": DOMAIN,
        "topic": "Lip Cancer",
        "stem": (
            "A patient requires resection of an advanced lower lip SCC involving the oral "
            "commissure, leaving a large defect after adequate-margin excision. The patient "
            "is a poor candidate for further surgery if reconstruction fails, and oral "
            "competence and speech are top priorities. Which reconstructive approach best "
            "fits this scenario?"
        ),
        "choices": [
            "Primary closure regardless of defect size",
            "A wedge excision closure technique alone",
            "A flap technique such as Abbe, Estlander, or Karapandzic, selected because the defect is large and involves the commissure",
            "No reconstruction, allowing the defect to heal by secondary intention",
        ],
        "answer": 2,
        "explanation": (
            "Reconstruction depends on defect size and lip subunit, ranging from primary "
            "closure and wedge excision for small defects to Abbe, Estlander, or Karapandzic "
            "flaps for larger defects, particularly when the commissure is involved -- exactly "
            "the situation described, where a large defect and commissure involvement demand a "
            "flap-based approach to preserve function."
        ),
        "why_wrong": [
            "Primary closure is appropriate for small defects, not the large commissure-involving defect described here.",
            "Wedge excision closure alone is suited to small defects, not a large defect involving the commissure.",
            "Correct.",
            "Leaving a large functional defect to heal by secondary intention would compromise oral competence and speech, which are explicitly priorities here.",
        ],
        "board_pearl": (
            "Reconstructive choice in lip cancer scales with defect size and lip subunit -- "
            "large or commissure-involving defects call for Abbe, Estlander, or Karapandzic "
            "flaps rather than primary closure or wedge excision."
        ),
        "curveball": (
            "How is lip cancer classified relative to oral cavity cancer for staging purposes, "
            "and how does its typical prognosis compare with other oral cavity subsites?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-head-neck-oncology-lip-cancer",
        "learning_stage": "senior_decision",
        "curveball_answer": (
            "Lip is its own AJCC primary site distinct from oral cavity, even though it is "
            "staged with similar T-category principles and managed with overlapping surgical "
            "logic. Lip SCC generally carries a more favorable prognosis than most other oral "
            "cavity subsites."
        ),
        "ladder_reviewed": True,
        "focus": "OR_prep",
    },
]


def apply_deep_curriculum_ladder_hn_v460(data_module, app_module=None):
    existing = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(existing, list):
        raise RuntimeError("v46.0: CLINICAL_CHALLENGES_V119 unavailable")
    existing_ids = {q.get("id") for q in existing}
    added = 0
    cases = list(existing)
    for q in NEW_QUESTIONS:
        if q["id"] in existing_ids:
            raise RuntimeError(f"v46.0: duplicate id {q['id']!r}")
        cases.append(q)
        added += 1
    data_module.CLINICAL_CHALLENGES_V119 = cases
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {"questions_added": added}
