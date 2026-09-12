"""v36.2 — source-grounded Vestibular Schwannoma depth and provenance."""

DOMAIN = "Otology / Neurotology"
TOPIC = "Vestibular Schwannoma"

SOURCE_BASIS_V362 = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — vestibular schwannoma/CPA tumor presentation, IAC and CPA anatomy, diagnostic evaluation, microsurgical approaches, cranial-nerve preservation and complications. Connected Google Drive source: CUMMINGS OTOLARYNGOLOGY–HEAD AND NECK 7th Ed 2021_compressed.pdf, file id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; split-volume copies also present.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022), Neurotology chapter — vestibular schwannoma/CPA localization, audiologic workup and retrosigmoid, middle-fossa and translabyrinthine management framework. Connected Google Drive file id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — vestibular schwannoma as a common IAC/CPA tumor, asymmetric auditory presentation, speech-discrimination clues and skull-base management principles. Connected Google Drive file id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Congress of Neurological Surgeons Systematic Review and Evidence-Based Guideline on Surgical Resection for Vestibular Schwannoma: Update. Neurosurgery. 2026;98(2):272-277. doi:10.1227/neu.0000000000003473 — hearing-preservation surgery through middle fossa or retrosigmoid may be considered in appropriately selected patients with good preoperative hearing; approach and intervention remain lesion- and patient-specific.",
    "Congress of Neurological Surgeons Systematic Review and Evidence-Based Guideline on Hearing Preservation Outcomes in Sporadic Vestibular Schwannoma: Update. Neurosurgery. 2026;98(2):298-302. doi:10.1227/neu.0000000000003551 — current counseling framework for hearing-preservation probabilities after observation, radiosurgery and microsurgery.",
    "Congress of Neurological Surgeons Systematic Review and Evidence-Based Guidelines Update for the Role of Imaging in Vestibular Schwannoma. Neurosurgery. 2026;98(2):283-287. doi:10.1227/neu.0000000000003419 — MRI-based diagnosis/surveillance and imaging follow-up principles.",
    "Congress of Neurological Surgeons Systematic Review and Evidence-Based Guideline on Radiosurgery/Radiation Therapy for Vestibular Schwannoma: Update. Neurosurgery. 2026;98(2):293-297. doi:10.1227/neu.0000000000003416 — contemporary SRS/radiation evidence and counseling.",
    "Tuleasca C, et al. Large vestibular schwannoma treated using a cranial nerve sparing approach with planned subtotal microsurgical resection and stereotactic radiosurgery: meta-analysis and ISRS practice guidelines. J Neurooncol. 2025;173(2):245-262. doi:10.1007/s11060-025-04990-6 — planned nerve-sparing subtotal resection plus SRS is a legitimate selected-patient strategy rather than gross-total removal at all costs.",
    "Marinelli JP, et al. Long-term tumor control after Gamma Knife radiosurgery for sporadic vestibular schwannoma. J Neurosurg. 2026;144(4):965-971. doi:10.3171/2025.8.JNS25829 — long-term SRS control remains high, but late failure and pseudoprogression require longitudinal interpretation rather than declaring early enlargement immediate treatment failure.",
    "Current-evidence distinction (rechecked 2026-09-12): durable IAC/CPA anatomy and operative approach principles come from core ENT texts; observation, SRS, hearing-preservation counseling, intentional residual strategy and imaging surveillance are updated to current CNS/ISRS evidence. No vestibular-schwannoma-specific FDA drug indication is asserted by this curriculum; pharmacologic therapy is not substituted for the standard observation/SRS/microsurgical decision framework for sporadic disease."
]

DEPTH_APPEND_V362 = {
    "recognize": " FOUNDATION REFINEMENT — suspect a retrocochlear process when unilateral or asymmetric sensorineural hearing loss, unilateral tinnitus, unexpectedly poor speech discrimination, disequilibrium or progressive cranial-neuropathy symptoms do not fit a simple cochlear explanation. These findings are clues, not a diagnosis: most asymmetric hearing loss is not vestibular schwannoma, and normal bedside vestibular findings do not exclude a small intracanalicular lesion.",
    "localize": " FOUNDATION/ANATOMY REFINEMENT — localize the lesion along the vestibular nerve within the internal auditory canal and cerebellopontine angle while tracking relationships to the facial nerve, cochlear nerve, brainstem, cerebellum and nearby AICA vascular loops. With increasing CPA size, distinguish isolated CN VIII symptoms from CN V/VII dysfunction, cerebellar signs, brainstem compression and hydrocephalus because these change urgency and management rather than merely increasing a size label.",
    "workup": " APPLICATION REFINEMENT — obtain complete audiometry with speech measures and contrast-enhanced MRI of the IAC/CPA when retrocochlear disease is suspected; MRI, not an isolated audiogram pattern or ABR, is the diagnostic imaging foundation. Characterize intracanalicular versus CPA extension, maximal/volumetric size, cystic features, brainstem effect and serial growth. During observation, compare standardized serial MRI and hearing trajectories rather than treating a single millimeter change or one audiogram as definitive progression.",
    "manage": " SENIOR DECISION REFINEMENT — observation, stereotactic radiosurgery and microsurgery are all valid in selected patients. Integrate tumor size and growth, serviceable hearing, symptoms, age/comorbidity, brainstem or CSF-pathway effect, prior treatment, anatomy and patient goals. Counsel separately for tumor control, facial-nerve function and hearing preservation because success in one domain does not guarantee the others. After SRS, distinguish expected treatment-related enlargement/pseudoprogression from durable serial growth before labeling failure when the clinical situation permits surveillance.",
    "operate": " OR DECISION REFINEMENT — choose the operative corridor for the actual objective and anatomy: middle fossa or retrosigmoid may support hearing-preservation attempts in selected small tumors with useful hearing, whereas translabyrinthine exposure accepts hearing sacrifice when hearing preservation is not a realistic objective and provides direct IAC access. Use facial-nerve monitoring and, when hearing preservation is attempted, cochlear/auditory monitoring appropriate to the case. Preserve arachnoid planes and avoid traction or thermal injury to CN VII/VIII and brainstem/AICA structures. If the capsule is densely inseparable from the facial nerve, cochlear nerve, brainstem or critical vasculature, stop escalating dissection: leave an intentional residual and plan MRI surveillance with selective adjuvant SRS rather than pursuing unsafe gross-total resection at the cost of function.",
    "teach": " CHIEF FRAMEWORK — 1) recognize asymmetric auditory findings as a retrocochlear prompt, not a tumor diagnosis; 2) map IAC/CPA anatomy and neurologic consequences before choosing treatment; 3) use MRI growth, hearing, symptoms and patient goals to choose observation, SRS or surgery; 4) choose middle fossa, retrosigmoid or translabyrinthine exposure by hearing objective and anatomy rather than habit; 5) counsel tumor control, facial function and hearing as separate outcomes; 6) recognize SRS pseudoprogression; 7) prefer planned functional preservation and an intentional residual over destructive dissection when the facial nerve, brainstem or critical vessels become the limiting plane."
}


def apply_vestibular_schwannoma_source_depth_v362(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [row for row in rows if row.get("topic") == TOPIC]
    if len(matches) != 1:
        raise RuntimeError(f"v36.2 requires exactly one exact live {DOMAIN} / {TOPIC!r}; found {len(matches)}")
    row = matches[0]
    for field, addition in DEPTH_APPEND_V362.items():
        current = str(row.get(field) or "").strip()
        if addition not in current:
            row[field] = (current + " " + addition).strip()
    row["source_basis"] = list(SOURCE_BASIS_V362)
    row["source_grounded_v362"] = True
    row["source_metadata_v362"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TOPIC},
        "identity_rule": "exact live canonical domain/topic equality",
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "management_currency": "Durable IAC/CPA anatomy and operative approach principles retained from core ENT texts; 2026 CNS guideline updates, 2025 ISRS planned-STR/SRS guidance and 2026 long-term SRS behavior evidence rechecked 2026-09-12.",
        "fda_scope": "No vestibular-schwannoma-specific FDA drug indication is asserted; sporadic VS management remains observation/SRS/microsurgical decision-making rather than ungrounded pharmacologic substitution.",
    }
    row["deliberate_review_v362"] = {
        "foundation": "localize asymmetric auditory symptoms to a possible retrocochlear IAC/CPA process without treating asymmetry or poor speech discrimination as pathognomonic",
        "application": "integrate contrast MRI anatomy/growth and hearing trajectory to distinguish observation, SRS and microsurgical pathways",
        "senior_decision": "choose the surgical corridor around the hearing objective and accept an intentional residual when cranial-nerve, brainstem or vascular preservation becomes the limiting plane",
        "traps": [
            "equating every asymmetric sensorineural hearing loss with vestibular schwannoma",
            "reassuring from a normal bedside vestibular examination despite a retrocochlear auditory pattern",
            "using ABR or speech discrimination as a substitute for indicated IAC/CPA MRI",
            "calling a single small MRI measurement change true biologic growth without standardized serial context",
            "choosing treatment by tumor size alone while ignoring hearing, symptoms, comorbidity and patient goals",
            "promising hearing preservation because tumor control is likely",
            "calling early post-SRS enlargement treatment failure without considering pseudoprogression and longitudinal behavior",
            "choosing middle fossa, retrosigmoid or translabyrinthine exposure by habit rather than anatomy and hearing objective",
            "pursuing gross-total resection through an unsafe facial-nerve, brainstem or vascular plane instead of accepting a planned residual",
            "treating postoperative or post-SRS surveillance as optional after apparently successful initial treatment",
        ],
    }
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TOPIC], "count": 1, "canonical_topic": TOPIC}
