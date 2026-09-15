"""Regression gate for the exact-live Daily Curriculum and curveball UI data."""

import runtime_entry_pasha as production


BANNED = (
    "how do you localize",
    "what localization changes the differential",
    "localize the problem.",
    "evaluate it efficiently.",
    "build the management sequence.",
    "make the advanced decision.",
    "teach the mental model.",
    "what dangerous alternative must you not miss",
)

EXPECTED_KINDS = {
    "Acute Otitis Externa": "condition",
    "Chronic Otitis Media / Cholesteatoma": "condition",
    "Sudden Sensorineural Hearing Loss": "condition",
    "Eustachian Tube Dysfunction": "condition",
    "Allergic Rhinitis": "condition",
    "Acute Bacterial Rhinosinusitis": "condition",
    "Laryngomalacia": "condition",
    "Dysphagia / Aspiration": "condition",
    "FEES": "test",
    "Modified Barium Swallow": "test",
    "Total Laryngectomy": "procedure",
    "Submandibular Gland Excision": "procedure",
    "Periocular Reconstruction": "procedure",
    "PAP Troubleshooting": "therapy",
    "Frontal Recess / Frontal Sinus": "framework",
    "CRS Phenotyping": "framework",
    "Olfactory Dysfunction": "framework",
    "Lateral Skull-Base Tumor Framework": "framework",
    "Pediatric Hearing Loss Workup": "framework",
    "Structured Facial Trauma Examination": "framework",
    "Aesthetic Facial Analysis": "framework",
    "ENT Perioperative Anesthesia / Difficult Airway Planning": "framework",
    "Antimicrobial Stewardship in Otolaryngology": "framework",
    "Cranial Nerve Examination / Skull Base Localization": "framework",
    "Common ENT Consult Triage / Disposition": "framework",
    "Cochlear Implant Candidacy": "framework",
    "Petrous Apex Lesions": "framework",
    "Central Vestibular Disorders": "framework",
    "Facial Paralysis": "framework",
    "Ototoxic / Noise-Induced Hearing Loss": "framework",
    "Hyperacusis / Decreased Sound Tolerance": "framework",
    "Benign Sinonasal Tumor Framework": "framework",
    "Facial Pain / Headache vs Rhinogenic Disease": "framework",
    "Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer": "framework",
    "Tympanostomy Tube Indications": "framework",
    "Congenital Neck Masses": "framework",
    "Pediatric Aspiration": "framework",
    "Croup vs Epiglottitis": "framework",
    "Pediatric Reflux / Eosinophilic Esophagitis": "framework",
    "Benign Vocal Fold Lesions": "framework",
    "Professional Voice": "framework",
    "Dysphagia / Aspiration": "framework",
    "Acute / Chronic Laryngopharyngitis": "framework",
    "Functional Nasal Obstruction": "framework",
    "Systemic / Granulomatous Disease Manifestations in ENT": "framework",
    "Geriatric Otolaryngology / Frailty": "framework",
    "Immunocompromised Host in Otolaryngology": "framework",
    "Central Events / Hypoventilation": "framework",
    "Epistaxis": "framework",
    "AOM / OME / Tympanostomy Decisions": "framework",
    "Cleft / Craniofacial Otologic-Airway Care": "framework",
    "Ankyloglossia / Maxillary Frenulum": "framework",
    "Facial Soft-Tissue Lacerations / Burns": "framework",
    "ENT Fluids / Electrolytes / Nutrition": "framework",
    "Oral Manifestations of Systemic Disease": "framework",
    "Facial Nerve Reanimation": "procedure",
    "Hypoglossal Nerve Stimulation": "procedure",
    "HNS Activation / Programming": "therapy",
    "Cleft Lip / Palate — ENT Surgical Fundamentals": "foundation",
    "Pleomorphic Adenoma / Warthin Tumor": "condition",
    "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy": "condition",
    "Unknown Primary with Cervical Metastasis": "oncology",
}

EXPECTED_CASE_LABELS = {
    "Vestibular Neuritis": "Acute vestibular syndrome",
    "Post-Tonsillectomy Hemorrhage": "Postoperative oral bleeding",
    "Posterior Glottic Stenosis / Arytenoid Fixation": "Bilateral vocal-fold immobility",
    "Tracheomalacia / Bronchomalacia": "Dynamic pediatric airway symptoms",
    "Carotid Blowout Syndrome": "Sentinel or major neck bleeding",
    "Septal Hematoma": "Post-traumatic nasal obstruction",
}

EXPECTED_CASE_LABELS = {
    "Vestibular Neuritis": "Acute vestibular syndrome",
    "Post-Tonsillectomy Hemorrhage": "Postoperative oral bleeding",
    "Posterior Glottic Stenosis / Arytenoid Fixation": "Bilateral vocal-fold immobility",
    "Tracheomalacia / Bronchomalacia": "Dynamic pediatric airway symptoms",
    "Carotid Blowout Syndrome": "Sentinel or major neck bleeding",
    "Septal Hematoma": "Post-traumatic nasal obstruction",
}

CURVEBALL_ANSWER_ANCHORS = {
    "v252_lar_mtd_snr": ("laryngeal emg", "recruitment", "timing"),
    "v220_hn_fom_fnd": ("fixation", "mandible", "tongue mobility"),
    "v262_fpt_otoplasty_fnd": ("mustarde", "furnas", "conchal"),
    "v254_lar_polycyst_fnd": ("mucosal wave", "cyst", "polyp"),
    "v254_lar_polycyst_snr": ("stiffness", "scar", "recurrent mass"),
    "v11_fprs_05": ("modified cottle", "dynamic lateral-wall", "septal"),
    "v254_lar_nodule_fnd": ("soft", "fibrotic", "therapy"),
    "v254_lar_nodule_app": ("voice breaks", "amplification", "workload"),
    "v143_rhi_03": ("nasolacrimal duct", "anterior", "injury"),
    "v207_rhi_frontal_snr": ("saline", "debridement", "topical"),
    "v137_tps_05": ("multigland", "bilateral", "intraoperative pth"),
    "v220_hn_tonsil_snr": ("positive microscopic margin", "extranodal extension", "chemoradiation"),
    "v243_ped_sgh_snr": ("propranolol", "debulking", "tracheostomy"),
    "v267_sleep_ds_snr": ("central", "hypoventilation", "co2"),
    "v235_tps_indet_fnd": ("pretest", "positive predictive value", "prevalence"),
    "v147_fp_14": ("beyond", "wound margins", "hypertrophic"),
    "v222_hn_tep_snr": ("hands-free", "peristomal seal", "speech-language"),
    "v246_ped_cranio_fnd": ("eustachian-tube", "recur", "audiology"),
    "v269_gen_afb_app": ("both lungs", "fragments", "migrate"),
    "v113-oto-02": ("pöschl", "stenv", "vemp"),
    "v128_lar_03": ("superficial lamina propria", "scar"),
    "v136_oto_13": ("free-run", "stimulated"),
    "v136_rhi_04": ("situs inversus",),
    "v136_rhi_17": ("sphenopalatine artery",),
    "v139_gen_10": ("eosinophilic esophagitis", "biops"),
    "v140_gen_10": ("opening", "platysma", "do not wait"),
    "v141_slp_06": ("ejection fraction", "45"),
    "v144_oto_22": ("do not biopsy",),
    "v154_hn_fnd": ("neck stoma", "oral intubation"),
    "v124_ped_06": ("second branchial", "internal and external carotid"),
    "v128_lar_01": ("mucosal wave", "cyst", "polyp"),
    "v137_tps_08": ("hypercalcemia",),
    "v137_fpt_10": ("perichondrium", "vascularized"),
    "v138_hn_24": ("positive margins", "extranodal extension"),
    "v140_ped_06": ("neurolog", "aspiration"),
    "v143_lar_04": ("recovery", "fixation"),
    "v145_lar_16": ("horizontal", "vertical"),
    "v152_ped_01": ("aortopexy", "anterior tracheopexy"),
    "v154_hn_app": ("laryngectomy", "tracheostomy", "upper airway"),
    "v206_rhi_max_app": ("haller", "uncinate", "natural maxillary ostium"),
    "v222_hn_tep_fnd": ("esophageal speech", "electrolarynx", "tep"),
    "v236_tps_ptca_fnd": ("seed", "capsule"),
    "v243_ped_tm_fnd": ("positive-pressure", "stent"),
    "v245_ped_hl_app": ("oae", "abr", "speech"),
}


def main():
    data = production.runtime_entry.data
    app_mod = production.runtime_entry.app_mod
    items = data.get_adaptive_items_v120()
    expected = sum(len(modules) for modules in data.DEEP_MODULES_V6.values()) * 6
    failures = []

    if len(items) != expected:
        failures.append(f"item_count:{len(items)}!={expected}")

    by_concept = {}
    for item in items:
        by_concept.setdefault(item.get("concept_id"), []).append(item)
        prompt = str(app_mod._adaptive_question(item) or "").strip()
        low = prompt.lower()
        if not prompt or not prompt.endswith("?"):
            failures.append("not_a_question:" + str(item.get("id")))
        for phrase in BANNED:
            if phrase in low:
                failures.append("legacy_template:" + str(item.get("id")) + ":" + phrase)
        if item.get("stage") == "recognize" and item.get("blind_reveal"):
            label = str(item.get("blind_case_label") or "").strip()
            if not label:
                failures.append("missing_case_label:" + str(item.get("id")))
            if str(item.get("topic") or "").lower() in label.lower():
                failures.append("label_reveals_diagnosis:" + str(item.get("id")))
            if str(item.get("topic") or "").lower() in low:
                failures.append("prompt_reveals_diagnosis:" + str(item.get("id")))

    for cid, concept_items in by_concept.items():
        stages = {item.get("stage") for item in concept_items}
        if stages != {"recognize", "localize", "workup", "manage", "operate", "teach"}:
            failures.append("stage_set:" + str(cid))

    recognize_by_topic = {
        item.get("topic"): item for item in items if item.get("stage") == "recognize"
    }
    for topic, expected_kind in EXPECTED_KINDS.items():
        actual = (recognize_by_topic.get(topic) or {}).get("daily_topic_kind")
        if actual != expected_kind:
            failures.append(f"topic_kind:{topic}:{actual}!={expected_kind}")

    for topic, expected_label in EXPECTED_CASE_LABELS.items():
        actual = (recognize_by_topic.get(topic) or {}).get("blind_case_label")
        if actual != expected_label:
            failures.append(f"case_label:{topic}:{actual}!={expected_label}")

    for topic, expected_label in EXPECTED_CASE_LABELS.items():
        actual = (recognize_by_topic.get(topic) or {}).get("blind_case_label")
        if actual != expected_label:
            failures.append(f"case_label:{topic}:{actual}!={expected_label}")

    for item in items:
        if item.get("daily_topic_kind") != "framework":
            continue
        prompt = str(app_mod._adaptive_question(item) or "").lower()
        if item.get("blind_reveal"):
            failures.append("framework_blinded_as_diagnosis:" + str(item.get("id")))
        if "most likely diagnosis" in prompt or "once " in prompt and " is established" in prompt:
            failures.append("framework_disease_grammar:" + str(item.get("id")))

    malformed_pairs = (
        ("Sudden Sensorineural Hearing Loss", "before starting sudden sensorineural hearing loss"),
        ("Acute Otitis Externa", "time-critical response to acute otitis externa"),
        ("Eustachian Tube Dysfunction", "components of eustachian tube dysfunction"),
    )
    all_prompts = {
        item.get("topic"): " ".join(
            str(app_mod._adaptive_question(x) or "").lower()
            for x in items if x.get("topic") == item.get("topic")
        )
        for item in items
    }
    for topic, phrase in malformed_pairs:
        if phrase in all_prompts.get(topic, ""):
            failures.append(f"semantic_prompt_mismatch:{topic}:{phrase}")

    curveballs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("curveball")]
    for q in curveballs:
        if not str(q.get("curveball_answer") or "").strip():
            failures.append("missing_curveball_answer:" + str(q.get("id")))

    curveballs_by_id = {q.get("id"): q for q in curveballs}
    for qid, anchors in CURVEBALL_ANSWER_ANCHORS.items():
        answer = str((curveballs_by_id.get(qid) or {}).get("curveball_answer") or "").lower()
        for anchor in anchors:
            if anchor not in answer:
                failures.append(f"weak_curveball_answer:{qid}:{anchor}")

    thyroid = next(
        (q for q in curveballs if "stridor while awaiting biopsy" in str(q.get("curveball") or "").lower()),
        None,
    )
    if thyroid is None:
        failures.append("missing_thyroid_lymphoma_curveball")
    else:
        answer = str(thyroid.get("curveball_answer") or "").lower()
        for anchor in ("threatened airway", "anesthesia", "surgical-airway", "diagnostic tissue"):
            if anchor not in answer:
                failures.append("thyroid_curveball_answer:" + anchor)

    print(f"V368_ITEMS|{len(items)}")
    print(f"V368_CONCEPTS|{len(by_concept)}")
    print(f"V368_BLINDED_LABELED|{sum(bool(x.get('blind_reveal') and x.get('blind_case_label')) for x in items)}")
    print(f"V368_CURVEBALLS_WITH_ANSWERS|{sum(bool(q.get('curveball_answer')) for q in curveballs)}/{len(curveballs)}")
    print(f"V368_FAILURES|{len(failures)}")
    for failure in failures[:100]:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: every live Daily Curriculum item uses a coherent question, every blinded case is labeled, and every curveball has a revealable answer")


if __name__ == "__main__":
    main()
