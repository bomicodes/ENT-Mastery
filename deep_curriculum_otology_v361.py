"""v36.1 — source-grounded Otosclerosis / Stapes Fixation depth and provenance."""

DOMAIN = "Otology / Neurotology"
TOPIC = "Otosclerosis / Stapes Fixation"

SOURCE_BASIS_V361 = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — otosclerosis pathophysiology, audiologic diagnosis, stapes surgery anatomy, technique, complications and rehabilitation. Connected Google Drive source: CUMMINGS OTOLARYNGOLOGY–HEAD AND NECK 7th Ed 2021_compressed.pdf, file id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; split-volume copies also present.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022), Otology/Neurotology chapter — otosclerosis/stapes fixation diagnosis and operative framework. Connected Google Drive file id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — otosclerosis, conductive hearing-loss differential, stapedotomy/stapedectomy principles and complications. Connected Google Drive file id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "AAO-HNSF Clinical Indicators: Stapedectomy/Stapedotomy (published 2014; current Academy resource rechecked 2026-09-12) — history/exam/audiometric checklist including intact TM, air-bone gap, speech testing, 512-Hz tuning-fork findings and absent acoustic reflex support. The Academy explicitly labels these indicators suggestions rather than a standard of care.",
    "Outcomes and predictive factors of success in stapes surgery: a multicentric retrospective analysis. J Laryngol Otol. 2026;140(2):214-220. doi:10.1017/S0022215125103903 — contemporary 615-patient evidence showing high hearing-success rates across diode laser, microdrill and combined techniques; technique choice remains anatomy- and surgeon-dependent rather than a single universally superior method.",
    "Current-evidence distinction (rechecked 2026-09-12): durable middle-ear/oval-window anatomy and operative principles come from core texts; candidacy and counseling require the actual audiogram, speech discrimination, contralateral hearing, patient goals and discussion of hearing-aid versus surgical rehabilitation rather than treating a Carhart notch or CT appearance alone as an operative indication."
]

DEPTH_APPEND_V361 = {
    "recognize": " FOUNDATION REFINEMENT — suspect otosclerosis when progressive conductive or mixed hearing loss occurs behind an intact, otherwise normal tympanic membrane, especially with family history and supportive tuning-fork/audiometric findings. A 2-kHz Carhart notch is supportive but not pathognomonic; do not collapse every normal-drum conductive loss into otosclerosis.",
    "localize": " APPLICATION REFINEMENT — localize the mechanical problem to stapes/oval-window fixation only after considering ossicular discontinuity, congenital fixation, superior-canal dehiscence/other third-window physiology and other middle-ear causes. Absent acoustic reflexes and a conductive pattern can support fixation, but discordant vestibular symptoms, unusually large low-frequency gaps, or atypical anatomy should reopen the differential.",
    "workup": " SENIOR DIAGNOSTIC REFINEMENT — obtain complete audiometry including air/bone thresholds and speech measures; interpret the air-bone gap in context rather than using a single threshold as a binary surgical trigger. Tympanometry/reflexes and 512-Hz tuning forks are supportive. High-resolution temporal-bone CT is selective rather than mandatory for every classic case; use it when diagnosis/anatomy is uncertain, congenital or revision anatomy is possible, third-window disease is a concern, or imaging will change operative planning.",
    "manage": " SENIOR MANAGEMENT REFINEMENT — observation, conventional amplification and stapes surgery are legitimate pathways. Offer surgery when the diagnosis is convincing, hearing disability and conductive component make meaningful benefit plausible, cochlear reserve/speech understanding are appropriate, the ear is otherwise suitable, and the patient accepts risks. Counsel explicitly about sensorineural loss, vertigo, dysgeusia/chorda symptoms, tympanic-membrane injury, prosthesis problems, persistent/recurrent conductive loss and need for revision; individualize decisions in an only-hearing ear or other unusually high-consequence setting.",
    "operate": " OR DECISION REFINEMENT — confirm fixation and anatomy before irreversible steps. Maintain orientation to the facial nerve, oval window, incus long process, promontory and round-window region; preserve chorda when feasible. Small-fenestra stapedotomy with a properly sized piston is the common modern strategy, but laser versus microdrill is a technique choice rather than dogma. Avoid uncontrolled footplate manipulation: if the footplate becomes floating, anatomy is obscured, the facial nerve is markedly overhanging, bleeding prevents safe visualization, or unexpected perilymphatic flow raises concern for a gusher, stop the planned sequence, control the immediate problem, re-localize and modify or abort rather than forcing completion. Measure prosthesis length deliberately and verify a stable incus attachment without overcrimping or excessive vestibular penetration.",
    "teach": " CHIEF FRAMEWORK — 1) prove that normal-drum conductive/mixed loss is truly stapes fixation; 2) distinguish third-window and ossicular alternatives; 3) compare amplification with surgery using the patient's actual disability and cochlear reserve; 4) enter the oval window only with landmarks and bailout plans clear; 5) treat floating footplate, facial-nerve obstruction or unexpected gusher as strategy-changing events; 6) judge success by hearing function and complications, not air-bone-gap closure alone."
}


def apply_otosclerosis_source_depth_v361(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [row for row in rows if row.get("topic") == TOPIC]
    if len(matches) != 1:
        raise RuntimeError(f"v36.1 requires exactly one exact live {DOMAIN} / {TOPIC!r}; found {len(matches)}")
    row = matches[0]
    for field, addition in DEPTH_APPEND_V361.items():
        current = str(row.get(field) or "").strip()
        if addition not in current:
            row[field] = (current + " " + addition).strip()
    row["source_basis"] = list(SOURCE_BASIS_V361)
    row["source_grounded_v361"] = True
    row["source_metadata_v361"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TOPIC},
        "identity_rule": "exact live canonical domain/topic equality",
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "management_currency": "Durable anatomy/operative principles retained from core texts; Academy clinical indicators and contemporary 2026 stapes-surgery outcomes rechecked 2026-09-12.",
    }
    row["deliberate_review_v361"] = {
        "foundation": "recognize the normal-drum conductive/mixed phenotype while treating Carhart notch as supportive rather than diagnostic",
        "application": "separate true stapes fixation from ossicular and third-window mimics, then choose testing/imaging only when it changes confidence or planning",
        "senior_decision": "individualize amplification versus surgery and execute stapedotomy with explicit facial-nerve, footplate, prosthesis and gusher bailout decisions",
        "traps": [
            "calling every normal-drum conductive hearing loss otosclerosis",
            "treating a Carhart notch as pathognomonic",
            "ignoring third-window physiology before stapes surgery",
            "ordering CT reflexively instead of for diagnostic or operative uncertainty",
            "using an air-bone-gap number without considering speech, cochlear reserve and patient disability",
            "forcing fenestration or prosthesis placement when the footplate is floating or visualization is unsafe",
            "failing to recognize unexpected high-flow perilymph as a strategy-changing gusher risk",
            "overlooking prosthesis sizing, incus attachment and excessive vestibular penetration as causes of failure/complication",
        ],
    }
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TOPIC], "count": 1, "canonical_topic": TOPIC}
