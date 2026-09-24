"""v44.3: close the 7-topic zero-Clinical-Challenge gap created by v44.1's new topics.

Fixing `audit_coverage_v135.py`'s stale `import runtime_entry` (v44.2 -- see
bucket6_data_hygiene_v442.py's docstring for the broader stale-count context) let that
audit correctly see the live 356-topic curriculum for the first time, which immediately
surfaced a real gap its own "coverage milestone 1" checks for: every canonical
DEEP_MODULES_V6 concept should have at least one linked Clinical Challenge vignette by
concept_id. The 7 topics added in v44.1 (missing_topics_gradingscales_v441.py) got
Concept Checks but never a Clinical Challenge vignette, so they showed as MISSING under
`audit_coverage_v135.py --strict`.

Adds one board-style MCQ vignette per topic, matching the existing house style (stem,
4 choices, why_wrong per choice, board_pearl, curveball, curveball_answer), grounded in
the same researched/verified facts used to author each topic in v44.1 -- no new clinical
claims invented here.
"""

NEW_CLINICAL_CHALLENGES_V443 = [
    {
        "id": "v443-otology-glomus-tumor-paraganglioma-01",
        "domain": "Otology / Neurotology",
        "topic": "Glomus Tumor / Paraganglioma",
        "stem": (
            "A 54-year-old reports pulsatile tinnitus. Otoscopy shows a reddish mass "
            "behind an intact tympanic membrane that blanches with pneumatic pressure. "
            "What is the most appropriate next step?"
        ),
        "choices": [
            "Transcanal biopsy of the mass in clinic to establish histology before imaging.",
            "CT temporal bone and MRI to characterize the lesion, with consideration of preoperative embolization if a vascular tumor is confirmed.",
            "Reassurance and repeat otoscopy in 6 months, since a blanching mass is benign by definition.",
            "Immediate oral antibiotics for presumed otitis media with effusion.",
        ],
        "answer": 1,
        "explanation": (
            "A pulsatile, blanching (Brown sign-positive) middle-ear mass is classic for "
            "a jugulotympanic paraganglioma. Imaging (CT temporal bone plus MRI) defines "
            "extent before any intervention, and vascular tumors are often embolized "
            "preoperatively to reduce blood loss -- clinic biopsy of a suspected vascular "
            "tumor risks serious hemorrhage."
        ),
        "why_wrong": [
            "Biopsying a suspected vascular paraganglioma in clinic risks serious hemorrhage and should never precede imaging.",
            "Correct.",
            "A blanching vascular mass is not benign by definition and needs full workup, not observation alone.",
            "There is no indication this is infectious; antibiotics do not address a vascular skull-base tumor.",
        ],
        "board_pearl": "Pulsatile tinnitus plus a reddish, blanching middle-ear mass (positive Brown sign) is a paraganglioma until proven otherwise; do not biopsy it in clinic.",
        "curveball": "Genetic testing later reveals an SDHB mutation. How does this change surveillance?",
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
        "concept_id": "v6-otology-neurotology-glomus-tumor-paraganglioma",
        "canonical_topic": "Glomus Tumor / Paraganglioma",
        "curveball_answer": (
            "SDHB mutations carry higher malignant/metastatic potential than other "
            "hereditary paraganglioma syndromes, so confirmed SDHB lowers the threshold "
            "for broader staging (looking for synchronous or metastatic disease) and "
            "warrants closer long-term surveillance and genetic counseling for at-risk "
            "family members."
        ),
    },
    {
        "id": "v443-laryngology-laryngeal-emg-01",
        "domain": "Laryngology / Voice / Swallowing",
        "topic": "Laryngeal Electromyography (LEMG)",
        "stem": (
            "Two days after thyroidectomy, a patient has a hypomobile left vocal fold. "
            "The surgeon wants to know whether this is recurrent laryngeal nerve injury "
            "or mechanical fixation, and orders laryngeal EMG. What is the best timing "
            "consideration for this test?"
        ),
        "choices": [
            "Perform LEMG immediately, since timing does not affect its accuracy.",
            "Defer LEMG for several weeks when possible, since fibrillation potentials take time to develop and an early study can be falsely reassuring.",
            "LEMG is contraindicated within 6 months of any neck surgery.",
            "LEMG should only be performed if the patient is already scheduled for reinnervation surgery.",
        ],
        "answer": 1,
        "explanation": (
            "Fibrillation potentials indicating denervation take time to appear after "
            "nerve injury. Reduced recruitment can be apparent early, but the absence "
            "of fibrillation potentials in the first days does not rule out denervation. "
            "Waiting several weeks when clinically feasible gives a more reliable "
            "read on denervation and prognosis."
        ),
        "why_wrong": [
            "Timing meaningfully affects accuracy; an early study can be falsely reassuring.",
            "Correct.",
            "There is no such blanket contraindication; timing relative to injury, not surgery type, is what matters.",
            "LEMG is useful for diagnosis and prognosis broadly, not only when reinnervation surgery is already planned.",
        ],
        "board_pearl": "A motionless fold is not automatically a paralyzed fold -- LEMG separates neurogenic immobility from mechanical fixation (e.g., cricoarytenoid joint fixation).",
        "curveball": "The delayed LEMG shows polyphasic, synkinetic reinnervation potentials. What does this suggest about prognosis?",
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "canonical_topic": "Laryngeal Electromyography (LEMG)",
        "curveball_answer": (
            "Polyphasic synkinetic reinnervation potentials indicate ongoing but "
            "disorganized reinnervation -- a pattern associated with a worse chance of "
            "normal, purposeful vocal fold motion returning, even though it may still "
            "eventually stabilize the airway through adductor synkinesis."
        ),
    },
    {
        "id": "v443-laryngology-laryngocele-01",
        "domain": "Laryngology / Voice / Swallowing",
        "topic": "Laryngocele",
        "stem": (
            "A trumpet player presents with a neck mass that enlarges when he plays and "
            "mild hoarseness. Imaging confirms a laryngocele. What must be done before "
            "treating this as a straightforward benign finding?"
        ),
        "choices": [
            "Proceed directly to endoscopic marsupialization without further workup.",
            "Confirm with CT and direct laryngoscopy that there is no obstructing glottic or supraglottic tumor at the saccule outlet.",
            "Reassure the patient and recommend he stop playing the instrument, with no further evaluation.",
            "Start a trial of oral corticosteroids to shrink the lesion before reimaging.",
        ],
        "answer": 1,
        "explanation": (
            "Laryngoceles coexist with an obstructing glottic or supraglottic squamous "
            "cell carcinoma at the saccule outlet in a clinically meaningful minority of "
            "cases. Imaging and laryngoscopy must actively exclude malignancy before the "
            "laryngocele itself is treated as benign."
        ),
        "why_wrong": [
            "Marsupialization should not proceed until malignancy has been excluded.",
            "Correct.",
            "Reassurance without excluding a coexisting tumor skips a mandatory safety step.",
            "There is no role for empiric corticosteroids in the workup of a laryngocele.",
        ],
        "board_pearl": "Never work up a laryngocele in isolation from the cancer question -- it can be the presenting sign of an obstructing glottic/supraglottic tumor.",
        "curveball": "The laryngocele has both an internal supraglottic and a neck component. How does this change management?",
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
        "concept_id": "v6-laryngology-voice-swallowing-laryngocele",
        "canonical_topic": "Laryngocele",
        "curveball_answer": (
            "A combined (mixed) laryngocele has both an internal supraglottic component "
            "within the thyrohyoid membrane and an external component that has herniated "
            "through it into the neck; unlike a purely internal laryngocele, combined "
            "disease generally requires open excision through the thyrohyoid membrane "
            "rather than endoscopic marsupialization alone."
        ),
    },
    {
        "id": "v443-head-neck-oncology-lip-cancer-01",
        "domain": "Head & Neck Oncology",
        "topic": "Lip Cancer",
        "stem": (
            "A patient with a biopsy-confirmed lower lip squamous cell carcinoma has new "
            "numbness of the chin. What does this finding most specifically suggest?"
        ),
        "choices": [
            "Unrelated trigeminal neuralgia, not requiring further evaluation.",
            "Perineural spread along the mental/inferior alveolar nerve, which should prompt targeted imaging and may change margin planning.",
            "A normal postoperative finding requiring no action.",
            "Distant metastasis to the brain requiring immediate palliative referral.",
        ],
        "answer": 1,
        "explanation": (
            "New sensory change in the distribution of the mental/inferior alveolar "
            "nerve in a patient with known lip SCC should raise concern for perineural "
            "spread, which changes imaging and margin planning."
        ),
        "why_wrong": [
            "In a patient with known lip SCC, new numbness in the nerve's distribution should not be dismissed as unrelated without evaluation.",
            "Correct.",
            "This finding is relevant preoperatively in a patient not yet treated and should prompt workup, not be ignored.",
            "Chin numbness reflects local perineural spread along a named nerve, not a typical presentation of distant brain metastasis.",
        ],
        "board_pearl": "Lip is its own AJCC primary site distinct from oral cavity, though staged with similar T-category principles.",
        "curveball": "The tumor involves the oral commissure. How does this change reconstructive planning?",
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
        "concept_id": "v6-head-neck-oncology-lip-cancer",
        "canonical_topic": "Lip Cancer",
        "curveball_answer": (
            "Commissure involvement is reconstructively challenging because there is "
            "less redundant tissue and the commissure is functionally critical for oral "
            "competence and speech; larger defects involving the commissure typically "
            "need an Abbe, Estlander, or Karapandzic flap rather than simple primary "
            "closure."
        ),
    },
    {
        "id": "v443-sleep-surgery-nasal-surgery-cpap-adjunct-01",
        "domain": "Sleep Surgery",
        "topic": "Nasal Surgery as a CPAP-Adherence Adjunct",
        "stem": (
            "A patient with OSA and septal deviation cannot tolerate his prescribed CPAP "
            "pressure due to significant mouth leak. After septoplasty and turbinate "
            "reduction, his AHI on a later unrelated study is essentially unchanged. Was "
            "the nasal surgery a failure?"
        ),
        "choices": [
            "Yes, since nasal surgery is expected to normalize the AHI on its own.",
            "Not necessarily -- the relevant outcome measures are CPAP tolerance, required pressure, and nightly usage hours, which AHI alone does not capture.",
            "Yes, and the patient should be referred directly for tracheostomy.",
            "The result is uninterpretable and no further outcome measures should be tracked.",
        ],
        "answer": 1,
        "explanation": (
            "Nasal surgery is a CPAP-adherence adjunct, not a stand-alone AHI-normalizing "
            "procedure. Success should be judged by CPAP tolerance, required therapeutic "
            "pressure, and adherence, not by AHI reduction from the nasal surgery alone."
        ),
        "why_wrong": [
            "Conflating nasal surgery with a stand-alone AHI-normalizing treatment is the classic teaching error for this topic.",
            "Correct.",
            "An unchanged AHI after nasal surgery alone does not itself justify escalating straight to tracheostomy.",
            "The correct outcome measures (CPAP pressure, leak, adherence) remain fully interpretable even when AHI alone is unchanged.",
        ],
        "board_pearl": "Measure success in CPAP usage hours and tolerated pressure, not AHI reduction from the nasal surgery alone.",
        "curveball": "His CPAP tolerance still has not improved despite the nasal surgery. What should be reassessed?",
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
        "concept_id": "v6-sleep-surgery-nasal-surgery-as-a-cpap-adherence-adjunct",
        "canonical_topic": "Nasal Surgery as a CPAP-Adherence Adjunct",
        "curveball_answer": (
            "Re-examine for an undertreated site of nasal obstruction -- particularly "
            "nasal valve collapse on a Cottle maneuver -- since valve collapse can "
            "persist and limit tolerance even after septoplasty and turbinate reduction."
        ),
    },
    {
        "id": "v443-sleep-surgery-adult-epiglottic-collapse-01",
        "domain": "Sleep Surgery",
        "topic": "Adult Epiglottic Collapse / Epiglottopexy",
        "stem": (
            "A patient's OSA persists after a technically successful palatal surgery. "
            "What is the most appropriate next diagnostic step before assuming the "
            "palate operation simply failed?"
        ),
        "choices": [
            "Repeat the same palatal procedure with more aggressive tissue resection.",
            "Perform drug-induced sleep endoscopy (DISE) to look for other or additional obstruction sites, including epiglottic collapse.",
            "Proceed directly to tracheostomy without further evaluation.",
            "Conclude the original diagnosis of OSA must have been incorrect.",
        ],
        "answer": 1,
        "explanation": (
            "Persistent OSA after palatal surgery should prompt DISE to look for "
            "additional or alternative obstruction sites, including epiglottic collapse "
            "-- a distinct, correctable obstruction pattern that is easy to miss on awake "
            "exam."
        ),
        "why_wrong": [
            "Repeating the same procedure without re-evaluating the collapse pattern risks operating on the wrong site again.",
            "Correct.",
            "Tracheostomy is a last resort reserved for severe, refractory disease after appropriate site-directed evaluation, not a default next step.",
            "Persistent OSA after treatment does not mean the original diagnosis was wrong; it means the obstruction pattern needs re-evaluation.",
        ],
        "board_pearl": "Do not assume palate or tongue-base collapse explains every surgical or CPAP failure -- DISE-confirmed epiglottic collapse is a distinct, correctable pattern.",
        "curveball": "DISE confirms significant epiglottic collapse as the dominant finding. What surgical options exist?",
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
        "concept_id": "v6-sleep-surgery-adult-epiglottic-collapse-epiglottopexy",
        "canonical_topic": "Adult Epiglottic Collapse / Epiglottopexy",
        "curveball_answer": (
            "Epiglottopexy (suturing the epiglottis anteriorly to the tongue base/"
            "vallecula to prevent posterior prolapse) or partial epiglottectomy are the "
            "established surgical options, generally paired with treatment of any other "
            "DISE-identified obstruction sites."
        ),
    },
    {
        "id": "v443-sleep-surgery-tracheostomy-definitive-osa-01",
        "domain": "Sleep Surgery",
        "topic": "Tracheostomy as Definitive OSA Therapy",
        "stem": (
            "A patient has severe OSA complicated by cor pulmonale and has failed or "
            "cannot tolerate CPAP, BiPAP, and other surgical options. Tracheostomy is "
            "being considered. What makes tracheostomy mechanistically different from "
            "every other OSA surgery?"
        ),
        "choices": [
            "It targets the palate more precisely than other procedures.",
            "It bypasses the entire upper airway obstruction below the level of collapse, rather than correcting one anatomic site.",
            "It works only by reducing tongue-base volume.",
            "It is effective solely because it improves nasal airflow.",
        ],
        "answer": 1,
        "explanation": (
            "Tracheostomy differs from every site-specific OSA operation because it "
            "bypasses the entire upper airway obstruction -- nasal, palatal, tongue-base, "
            "and laryngeal -- below the level of collapse, rather than correcting one "
            "anatomic site."
        ),
        "why_wrong": [
            "Tracheostomy does not target the palate; it bypasses the airway entirely.",
            "Correct.",
            "Its effectiveness is not limited to tongue-base volume; it bypasses obstruction regardless of site.",
            "It does not work through the nasal airway; it creates an airway below all sites of obstruction.",
        ],
        "board_pearl": "Tracheostomy bypasses the entire upper airway obstruction below the level of collapse, unlike any site-specific OSA surgery.",
        "curveball": "The patient wants to preserve some daytime speech and swallowing function. What strategy addresses this?",
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
        "concept_id": "v6-sleep-surgery-tracheostomy-as-definitive-osa-therapy",
        "canonical_topic": "Tracheostomy as Definitive OSA Therapy",
        "curveball_answer": (
            "A fenestrated or capped tube used during the day with nocturnal deflation/"
            "opening is a standard strategy that preserves daytime speech and swallowing "
            "function while still resolving nocturnal obstruction."
        ),
    },
]


def apply_clinical_challenge_gapfill_v443(data_module, app_module=None):
    challenges = data_module.CLINICAL_CHALLENGES_V119
    existing_ids = {c.get("id") for c in challenges}
    added = []
    for index, entry in enumerate(NEW_CLINICAL_CHALLENGES_V443):
        if entry["id"] not in existing_ids:
            challenge = dict(entry)
            target = (0, 2, 3, 1, 0, 2, 3)[index]
            shift = (target - challenge["answer"]) % len(challenge["choices"])
            challenge["choices"] = challenge["choices"][-shift:] + challenge["choices"][:-shift] if shift else list(challenge["choices"])
            challenge["why_wrong"] = challenge["why_wrong"][-shift:] + challenge["why_wrong"][:-shift] if shift else list(challenge["why_wrong"])
            challenge["answer"] = target
            challenges.append(challenge)
            existing_ids.add(entry["id"])
            added.append(entry["id"])
    data_module.CLINICAL_CHALLENGES_V119 = challenges
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = challenges
    return {"added_count": len(added)}
