"""ENT Mastery v41.6 — Interpretation Labs depth and AJCC 8 accuracy repair.

Replaces generic learner-facing explanations in 28 interpretation cases, repairs
the incomplete papillary-thyroid-carcinoma answer, and adds exact AJCC 8 staging
criteria to four head-and-neck imaging cases.  AJCC 8 remains the operative
clinical/board system in this curriculum; AJCC 9 remains separately labelled
reference material.
"""

from copy import deepcopy


GENERIC = "Interpret the finding through anatomy/physiology, then state the clinical or operative consequence."


# case id -> (case-specific WHY THIS MATTERS, case-specific follow-up answer)
SPECIFIC = {
    # Pathology
    "p8": (
        "Depth of invasion (DOI) is a major predictor of occult nodal risk in oral cavity SCC and, together with greatest tumor dimension, directly determines AJCC 8 T category; invasion pattern, DOI, PNI/LVI and margins therefore change neck and adjuvant decisions.",
        "Report greatest dimension, DOI in millimeters, invasive-front pattern, PNI/LVI and margin distance; each can change staging, elective neck management or adjuvant planning.",
    ),
    "p9": (
        "Block-positive p16 is a validated surrogate for HPV-mediated biology in the oropharynx, not a universal head-and-neck HPV marker; applying HPV-mediated staging to an oral cavity, laryngeal or hypopharyngeal primary would misclassify it.",
        "Confirm the primary is oropharyngeal and that p16 meets the required block-positive pattern before using the separate AJCC 8 HPV-mediated oropharyngeal staging system.",
    ),
    "p10": (
        "Papillary thyroid carcinoma is fundamentally a nuclear-features diagnosis; papillary architecture can be sparse or absent, so the characteristic nuclear changes establish the diagnosis before variant and postoperative risk features are considered.",
        "After establishing PTC, report variant, size, gross extrathyroidal extension, margins, vascular invasion and nodal disease because these shape postoperative risk and treatment.",
    ),
    "p11": (
        "Medullary thyroid carcinoma arises from parafollicular C cells, so its calcitonin-producing neuroendocrine biology requires RET/MEN2 evaluation rather than a differentiated-thyroid-cancer pathway.",
        "Check calcitonin and CEA, obtain germline RET testing, and exclude MEN2-associated pheochromocytoma before thyroid surgery; assess hyperparathyroidism as appropriate.",
    ),
    "p12": (
        "Adenoid cystic carcinoma has a marked tendency for perineural spread that can extend beyond the visible primary, so named-nerve involvement may change both resection and skull-base radiation fields.",
        "Request explicit reporting of PNI and correlate symptoms or named-nerve disease with contrast-enhanced fat-suppressed MRI tracing the nerve toward its skull-base foramen.",
    ),
    "p13": (
        "Mucoepidermoid carcinoma is anchored by a mixture of mucous, epidermoid and intermediate cells; cystic versus solid growth, mitoses, necrosis and neural invasion contribute to grade and therefore expected behavior.",
        "Confirm the grading system and reported grade, then integrate site, extent, nodal risk, margins and PNI when planning resection, neck management and possible radiation.",
    ),
    "p14": (
        "Pleomorphic adenoma may have an incomplete capsule and microscopic pseudopods, so capsular violation or enucleation can seed or leave tumor and increase recurrence.",
        "Plan complete excision without tumor spillage—using extracapsular, partial or superficial-parotid techniques according to tumor anatomy and nerve relationships—rather than simple enucleation; document facial-nerve function.",
    ),
    "p15": (
        "Pathologic extranodal extension (ENE) is an AJCC 8 nodal-stage modifier in most non-HPV-mediated head-and-neck sites and is a validated high-risk postoperative feature supporting concurrent chemoradiation when the patient can tolerate it; imaging suspicion of ENE is important but is not interchangeable with pathologic ENE for adjuvant selection.",
        "State whether ENE is radiographic/clinical or pathologically confirmed, quantify it when the applicable pathology protocol requires, and apply the correct site-specific AJCC system before translating it into adjuvant treatment.",
    ),
    "p16": (
        "Clinically significant perineural invasion in cutaneous SCC can extend along named nerves toward skull-base foramina and can enlarge both surgical and radiation fields beyond the skin specimen.",
        "Separate incidental microscopic small-nerve PNI from symptomatic, named-nerve or larger-caliber disease and obtain nerve-pathway imaging when the latter is suspected.",
    ),
    "p17": (
        "Inverted papilloma grows endophytically into stroma, but that pattern alone is not carcinoma; recurrence is driven mainly by residual disease at the attachment site, while synchronous or metachronous SCC must be excluded.",
        "Identify and completely treat the attachment site, orient tissue for pathology, and sample suspicious or heterogeneous areas for associated dysplasia or SCC.",
    ),
    # Vestibular
    "v8": (
        "Calorics test horizontal-canal VOR at very low frequency whereas vHIT tests high-frequency, high-acceleration function; disease and compensation can affect these frequency ranges differently, so discordance is physiologic information rather than automatic test error.",
        "Interpret calorics and vHIT as complementary and integrate timing, symptoms, VEMPs and hearing rather than declaring one result invalid when they disagree.",
    ),
    "v9": (
        "Reduced canal-specific VOR gain with overt or covert corrective saccades demonstrates inadequate high-frequency reflex function; the involved canal pattern helps map superior versus inferior vestibular-nerve pathways.",
        "Map affected canals, confirm technical quality, and correlate with calorics, VEMPs and the clinical syndrome before assigning a specific lesion or diagnosis.",
    ),
    "v10": (
        "cVEMP primarily reflects the saccule and inferior vestibular nerve through the sacculocollic reflex, so an absent response—after accounting for age and sternocleidomastoid activation—does not automatically imply superior-division dysfunction.",
        "Pair cVEMP with oVEMP, vHIT and calorics and first exclude poor muscle activation or age-related response loss before localizing.",
    ),
    "v11": (
        "Enhanced, low-threshold VEMP responses can reflect third-window physiology because the additional mobile window alters inner-ear impedance; physiology must still match symptoms and correctly reformatted high-resolution CT.",
        "Correlate VEMPs with autophony and sound/pressure-induced symptoms and require appropriately acquired/reformatted temporal-bone CT before diagnosing superior canal dehiscence syndrome.",
    ),
    "v12": (
        "Typical BPPV produces canal-plane, latency-onset, transient positional nystagmus; persistent or otherwise atypical direction-changing nystagmus that does not fit one canal should raise concern for central positional nystagmus.",
        "Look for other central ocular-motor or neurologic findings and pursue neurologic evaluation/imaging when the pattern is atypical instead of repeating repositioning maneuvers indefinitely.",
    ),
    "v13": (
        "In an acute vestibular syndrome with ongoing spontaneous nystagmus, a normal head impulse, direction-changing gaze-evoked nystagmus or skew is a central HINTS pattern; HINTS is reliable only in the correct syndrome and when performed by a trained clinician.",
        "Treat a central HINTS/HINTS-plus pattern as a posterior-circulation warning requiring urgent stroke evaluation, while remembering that HINTS is not validated for brief episodic or purely positional dizziness.",
    ),
    # Audiology
    "a8": (
        "Present otoacoustic emissions indicate preserved outer-hair-cell function while an abnormal/absent ABR suggests impaired neural synchrony; that combination supports auditory neuropathy spectrum disorder rather than routine cochlear loss.",
        "Base rehabilitation on behavioral thresholds, speech perception and demonstrated aided benefit: hearing aids may help some patients, while persistently poor speech understanding can support cochlear-implant evaluation.",
    ),
    "a9": (
        "Cochlear-implant candidacy is based on functional benefit from appropriately fitted hearing aids and standardized aided speech recognition, because equal pure-tone thresholds can produce very different real-world understanding.",
        "Document ear-specific and best-aided speech scores under defined conditions and apply current device/payer criteria rather than deciding from thresholds alone.",
    ),
    "a10": (
        "CROS and bone-conduction rerouting systems both send information from the deaf side to the better cochlea and therefore reduce head-shadow but do not restore true binaural localization or squelch.",
        "Compare non-surgical CROS with bone-conduction options using the better ear's hearing, ear-canal/middle-ear status, anatomy, patient preference and a real-world trial; a conductive component in the better ear is not by itself a universal device-selection rule.",
    ),
    "a11": (
        "Ear-canal volume separates common causes of a flat type-B tympanogram: normal volume supports an intact drum with effusion, whereas a large volume suggests a perforation or patent tube.",
        "Confirm the volume-based inference with otoscopy rather than diagnosing effusion, perforation or tube patency from the tracing alone.",
    ),
    "a12": (
        "A flat tracing with normal ear-canal volume indicates poor tympanic-membrane mobility behind an intact drum; effusion is common, but the tympanogram cannot directly visualize the membrane or fluid.",
        "Confirm with pneumatic otoscopy and integrate hearing level, symptoms and duration before choosing observation or tympanostomy tubes.",
    ),
    "a13": (
        "Ototoxicity monitoring is a change-from-baseline problem: ASHA significant-shift criteria include at least 20 dB at one frequency, at least 10 dB at two adjacent frequencies, or loss of response at three consecutive previously responsive frequencies, confirmed on repeat testing when feasible.",
        "Obtain a pretreatment baseline whenever feasible and report serial threshold change promptly so the treating team can weigh oncologic/infectious benefit against auditory injury.",
    ),
    # Laryngeal endoscopy
    "e8": (
        "Leukoplakia is a visual descriptor rather than histology; focal stiffness, reduced/absent mucosal wave, ulceration or submucosal fullness raises concern for deeper dysplasia or carcinoma and lowers the threshold for biopsy.",
        "Describe surface morphology and vascular pattern, then look specifically for focal stiffness or loss of wave and integrate patient risk before choosing surveillance versus operative biopsy.",
    ),
    "e9": (
        "Posterior glottic stenosis and bilateral neurogenic immobility can both produce a narrow airway, but one is mechanical joint fixation/scar and the other is neuromuscular; the operations and prognosis differ.",
        "Review intubation and neurologic history, inspect the posterior commissure, and palpate arytenoid mobility under anesthesia when needed before committing to a paralysis- or scar-directed procedure.",
    ),
    "e10": (
        "Reinke edema expands the superficial lamina propria, classically from smoking/irritant exposure; the diffusely pliable cover often retains or exaggerates wave even while added mass lowers pitch and can narrow the airway.",
        "Prioritize smoking/irritant cessation, assess airway effect, and use conservative microflap reduction when surgery is needed to avoid scarring the vibratory cover.",
    ),
    "e11": (
        "Vocal-fold paresis may create glottic insufficiency and secondary supraglottic squeeze that resembles primary muscle-tension dysphonia; fold position, bowing, phase asymmetry and closure must be assessed beneath the compensatory behavior.",
        "Compare motion across tasks, examine stroboscopic phase/closure, and use laryngeal EMG selectively when paresis remains uncertain and the result would change management.",
    ),
    "e12": (
        "Recurrent respiratory papillomatosis is multifocal HPV-driven disease; aggressive treatment of normal mucosa increases scar without eliminating the biologic tendency to recur, so airway and voice preservation are central endpoints.",
        "Map disease, preserve normal mucosa, document recurrence burden and consider selected adjuvant therapy—most commonly bevacizumab-based strategies in contemporary practice—when disease is frequent, aggressive or difficult to control.",
    ),
    "e13": (
        "Voice tremor is usually rhythmic and can involve palate, pharynx and larynx across multiple tasks, whereas spasmodic dysphonia produces task-specific irregular voice breaks; task testing reveals the distribution and behavior.",
        "Compare sustained vowels, connected speech, singing and non-speech tasks and inspect palate/pharynx as well as the larynx before choosing tremor- versus dystonia-directed treatment.",
    ),
}


P10_OLD = "Diagnosis plus variant, size, extrathyroidal extension, margins, vascular invasion and nodal disease shape postoperative strategy."
P10_NEW = (
    "Papillary thyroid carcinoma is identified by characteristic nuclear enlargement and overlap, irregular/angulated contours, longitudinal grooves, intranuclear cytoplasmic pseudoinclusions and optically clear chromatin ('Orphan Annie eye' nuclei). Variant, size, gross extrathyroidal extension, margins, vascular invasion and nodal disease then shape postoperative risk and treatment."
)


AJCC8 = {
    "hn2": (
        "cystic nodal metastasis can be a presenting feature of HPV-associated oropharyngeal cancer.",
        " AJCC 8 uses a separate clinical nodal system for p16-positive oropharyngeal SCC: cN1 is one or more ipsilateral nodes, none larger than 6 cm; cN2 is contralateral or bilateral nodes, none larger than 6 cm; and cN3 is any node larger than 6 cm. Do not import the HPV-negative ENE-based clinical N categories.",
    ),
    "hn3": (
        "affect resection and staging decisions.",
        " AJCC 8 oral-cavity T category uses both greatest dimension and DOI: T1 is 2 cm or smaller with DOI 5 mm or less; T2 is 2 cm or smaller with DOI greater than 5 through 10 mm, or larger than 2 through 4 cm with DOI 10 mm or less; T3 is larger than 4 cm or any tumor with DOI greater than 10 mm.",
    ),
    "hn4": (
        "upstage disease and change partial-larynx versus organ-preservation/laryngectomy options.",
        " In AJCC 8 glottic/supraglottic staging, paraglottic-space invasion and/or minor inner-cortex thyroid-cartilage erosion qualifies as T3 even without vocal-fold fixation. Tumor penetrating the outer thyroid-cartilage cortex and/or extending beyond the larynx is T4a; imaging should distinguish sclerosis from convincing invasion.",
    ),
    "hn11": (
        "retrosternal extent, nodal levels and any likely RLN-course involvement.",
        " AJCC 8 differentiated-thyroid staging assigns gross invasion limited to strap muscles as T3b; gross invasion of subcutaneous soft tissue, larynx, trachea, esophagus or recurrent laryngeal nerve as T4a; and prevertebral-fascia invasion or carotid/mediastinal-vessel encasement as T4b.",
    ),
}


TEXTBOOKS = (
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021), interpretation/staging chapters.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022).",
    "K.J. Lee's Essential Otolaryngology, 12e (2019).",
)
AJCC_SOURCE = "AJCC Cancer Staging Manual, 8th edition — site-specific head-and-neck and differentiated-thyroid TNM criteria."


def _case_index(labs):
    return {
        (lab_key, case.get("id")): case
        for lab_key, lab in labs.items()
        if isinstance(lab, dict)
        for case in lab.get("cases", [])
        if isinstance(case, dict)
    }


def apply_interpretation_labs_depth_fix_v416(data_module, app_module=None):
    source = getattr(data_module, "INTERPRETATION_LABS", None)
    if not isinstance(source, dict):
        raise RuntimeError("interpretation v41.6: INTERPRETATION_LABS unavailable")
    labs = deepcopy(source)
    index = _case_index(labs)
    prefixes = {"p": "pathology", "v": "vestibular", "a": "audiology", "e": "laryngeal-endoscopy"}

    fixed, preserved = [], []
    for case_id, (why, follow_answer) in SPECIFIC.items():
        key = (prefixes[case_id[0]], case_id)
        case = index.get(key)
        if case is None:
            raise RuntimeError(f"interpretation v41.6: missing case {key!r}")
        if case.get("why") == GENERIC:
            case["why"] = why
            case["follow_answer"] = follow_answer
            fixed.append(case_id)
        elif case.get("why") == why and case.get("follow_answer") == follow_answer:
            preserved.append(case_id)
        else:
            raise RuntimeError(f"interpretation v41.6: independently changed case requires review: {case_id}")
        case["review_sources_v416"] = list(TEXTBOOKS)

    p10 = index.get(("pathology", "p10"))
    if p10 is None:
        raise RuntimeError("interpretation v41.6: missing pathology:p10")
    p10_fixed = False
    if p10.get("answer") == P10_OLD:
        p10["answer"] = P10_NEW
        p10_fixed = True
    elif p10.get("answer") != P10_NEW:
        raise RuntimeError("interpretation v41.6: unexpected p10 answer")

    staging_added = []
    for case_id, (marker, addition) in AJCC8.items():
        case = index.get(("head-neck-imaging", case_id))
        if case is None:
            raise RuntimeError(f"interpretation v41.6: missing head-neck-imaging:{case_id}")
        answer = str(case.get("answer") or "")
        if addition.strip() not in answer:
            if not answer.rstrip().endswith(marker):
                raise RuntimeError(f"interpretation v41.6: unexpected staging answer: {case_id}")
            case["answer"] = answer + addition
            staging_added.append(case_id)
        case["review_sources_v416"] = list(TEXTBOOKS) + [AJCC_SOURCE]
        case["staging_edition"] = "AJCC 8 (operative curriculum standard); AJCC 9 reference-only"

    data_module.INTERPRETATION_LABS.clear()
    data_module.INTERPRETATION_LABS.update(labs)
    if app_module is not None:
        app_module.INTERPRETATION_LABS = data_module.INTERPRETATION_LABS
    return {
        "why_follow_answer_fixed": fixed,
        "why_follow_answer_already_current": preserved,
        "p10_nuclear_features_fixed": p10_fixed,
        "ajcc8_staging_additions": staging_added,
        "accuracy_corrections": ["DOI-plus-size", "pathologic-ENE", "larynx-T3", "thyroid-T4a-vs-T4b", "ANSD-rehabilitation", "CROS-vs-bone-conduction"],
    }
