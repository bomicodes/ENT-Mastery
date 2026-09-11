"""v35.8 — source-grounded Sensorineural Hearing Loss foundation/application/senior-decision rebuild.

This bounded patch targets the exact live canonical Sensorineural Hearing Loss concept. It
separates durable cochlear/auditory-pathway principles from time-sensitive management:
chronic SNHL rehabilitation, asymmetric/retrocochlear workup, the sudden-SNHL emergency
pathway, cochlear-implant referral, and the narrow 2026 OTOF gene-therapy indication.
"""

import re

DOMAIN = "Otology / Neurotology"
TARGET = "sensorineural hearing loss"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


SNHL_REBUILD_V358 = {
    "recognize": (
        "FOUNDATION — SENSORINEURAL HEARING LOSS means impaired cochlear transduction and/or neural transmission rather than a mechanical external/middle-ear block. On a reliable audiogram, air- and bone-conduction thresholds are both elevated without a clinically meaningful air-bone gap. Common phenotypes include congenital/genetic loss, age-related loss, noise injury, ototoxicity, sudden SNHL, infectious/immune inner-ear disease, Ménière-spectrum loss, and retrocochlear disease. Do not use the old phrase 'nerve deafness' as if every SNHL is a CN VIII lesion: most acquired SNHL is cochlear. The first time-critical discriminator is tempo. A new unilateral or asymmetric loss over hours to <=72 hours is a SUDDEN-SNHL problem until proven otherwise, whereas slowly progressive bilateral loss follows a different diagnostic and rehabilitation pathway."
    ),
    "localize": (
        "APPLICATION — localize the deficit before choosing a test or treatment. Normal otoscopy and tympanometry can coexist with substantial SNHL because the pathology is medial to the middle ear. Cochlear disease often shows reduced thresholds with frequency-specific patterns and may show recruitment; disproportionate speech-recognition difficulty, marked asymmetry, unilateral tinnitus, or associated neurologic findings should reopen the retrocochlear/IAC-CPA differential. OAEs assess outer-hair-cell function and ABR assesses synchronized auditory-neural pathway responses, but neither replaces an ear-specific behavioral audiogram when that is obtainable. In children, distinguish peripheral cochlear loss from auditory neuropathy spectrum and verify cochlear-nerve anatomy when implantation is being considered."
    ),
    "workup": (
        "SENIOR DIAGNOSTIC DECISION — start with history (onset/tempo, laterality, fluctuation, tinnitus/vertigo, noise and medication exposure, infection/meningitis, trauma, family history), otoscopy, and complete audiometry including speech testing; add immittance/OAEs/ABR when the clinical question requires them. Significant asymmetric SNHL, unexpectedly poor word recognition, unilateral tinnitus with hearing asymmetry, or other retrocochlear concern generally warrants IAC/CPA evaluation, usually MRI when feasible rather than a reflexive broad laboratory panel. For idiopathic sudden SNHL, obtain audiometric confirmation promptly and evaluate for retrocochlear pathology with MRI or ABR; AAO-HNSF specifically recommends against routine head CT and routine laboratory testing in the uncomplicated idiopathic pathway. For congenital/early childhood SNHL, coordinate etiologic evaluation (including genetics and congenital-CMV timing/history when applicable) with developmental hearing intervention rather than delaying habilitation while every cause is pursued."
    ),
    "manage": (
        "MANAGEMENT SPLIT — chronic SNHL is primarily a communication/rehabilitation problem plus cause-specific prevention; sudden SNHL is a treatment-window problem. For chronic adult loss, counsel on communication strategies and appropriately fit amplification, then reassess functional benefit; persistent hearing difficulty with poor speech understanding despite optimized amplification should trigger cochlear-implant evaluation rather than years of progressively stronger hearing aids. For idiopathic sudden SNHL, current AAO-HNSF guidance allows corticosteroids as initial therapy within 2 weeks of onset and recommends intratympanic steroid salvage for incomplete recovery 2–6 weeks after onset; hyperbaric oxygen may be offered only in combination with steroids within the guideline windows. Do not routinely prescribe antivirals, thrombolytics, vasodilators, or vasoactive drugs for idiopathic SSNHL. Counsel that recovery is variable and obtain follow-up audiometry after treatment and again within 6 months."
    ),
    "operate": (
        "ADVANCED / OPERATE — surgery does not 'repair' generic SNHL; choose a device or operation only after defining the hearing phenotype and expected acoustic benefit. Cochlear implantation bypasses damaged sensory transduction and electrically stimulates the auditory nerve; candidacy is ear-specific and depends on aided speech performance, anatomy, goals, and current device/coverage criteria, not a single unaided pure-tone threshold. Contemporary practice includes selected asymmetric and single-sided-deafness indications, but FDA indications are DEVICE-SPECIFIC and should not be generalized from one manufacturer's label. A new 2026 FDA gene-therapy option is also deliberately narrow: OTARMENI (lunsotogene parvec-cwha) is indicated for pediatric and adult patients with severe-to-profound/profound SNHL associated with molecularly confirmed biallelic OTOF variants, preserved outer-hair-cell function, and no prior cochlear implant in the same ear. It is not a treatment for undifferentiated SNHL."
    ),
    "teach": (
        "BOARDS / CHIEF FRAMEWORK — 1) prove sensorineural rather than conductive loss; 2) use TEMPO + LATERALITY to choose the pathway; 3) sudden unilateral SNHL is time-sensitive—confirm promptly, evaluate retrocochlear disease, and discuss steroids within the evidence window; 4) chronic bilateral loss needs cause/risk review plus rehabilitation; 5) asymmetric loss or disproportionate speech performance deserves retrocochlear thinking; 6) inadequate aided speech understanding should trigger CI referral; 7) never turn a device-specific FDA label or an OTOF-specific gene therapy into a universal SNHL indication. Durable physiology comes from the textbooks; treatment windows, device labeling, and gene-therapy indications must track current guidance."
    ),
    "tags": [
        "sensorineural hearing loss", "SNHL", "sudden sensorineural hearing loss", "SSNHL",
        "asymmetric hearing loss", "speech recognition", "retrocochlear", "MRI IAC",
        "hearing aids", "cochlear implant referral", "OTOF", "OTARMENI"
    ],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — cochlear/auditory physiology, approach to sensorineural and sudden hearing loss, retrocochlear evaluation, hearing rehabilitation and cochlear implantation. Connected Google Drive source: CUMMINGS OTOLARYNGOLOGY–HEAD AND NECK 7th Ed 2021_compressed.pdf, file id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; split-volume copies also present.",
        "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022) — Approach to Hearing Loss and Tinnitus and hearing-rehabilitation framework. Connected Google Drive file id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
        "K.J. Lee's Essential Otolaryngology, 12e — congenital hearing loss, auditory evaluation, hearing rehabilitation and cochlear-implant principles. Connected Google Drive file id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
        "AAO-HNSF Clinical Practice Guideline: Sudden Hearing Loss (Update), Otolaryngol Head Neck Surg. 2019;161(1_suppl):S1-S45. doi:10.1177/0194599819859885 — prompt audiometry, retrocochlear evaluation, steroid/HBOT windows, intratympanic salvage, and therapies not routinely recommended.",
        "AAO-HNSF Clinical Practice Guideline: Age-Related Hearing Loss, Otolaryngol Head Neck Surg. 2024;170(Suppl 2):S1-S54. doi:10.1002/ohn.750 — audiometric evaluation, asymmetric/poor-word-recognition referral, amplification, communication counseling, and CI referral when optimized amplification leaves poor speech understanding.",
        "American Cochlear Implant Alliance Task Force, Laryngoscope. 2024;134(Suppl 3):S1-S14. doi:10.1002/lary.30879 — evidence-based adult CI referral/candidacy evaluation and ear-specific testing.",
        "U.S. FDA, OTARMENI (lunsotogene parvec-cwha), approved April 2026 — molecularly confirmed biallelic OTOF severe-to-profound/profound SNHL with preserved outer-hair-cell function and no prior CI in the same ear.",
        "U.S. FDA cochlear-implant approvals/labeling — current cochlear-implant indications are device-specific; single-sided-deafness labeling must be checked against the selected system rather than generalized."
    ],
}


def apply_snhl_source_rebuild_v358(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [row for row in rows if _norm(row.get("topic")) == TARGET]
    if len(matches) != 1:
        raise RuntimeError(
            f"v35.8 requires exactly one live canonical '{TARGET}' concept; found "
            f"{len(matches)}: {[row.get('topic') for row in matches]}"
        )

    module = matches[0]
    for field in FIELDS:
        module[field] = SNHL_REBUILD_V358[field]
    module["tags"] = list(SNHL_REBUILD_V358["tags"])
    module["source_basis"] = list(SNHL_REBUILD_V358["source_basis"])
    module["source_grounded_v358"] = True
    module["source_metadata_v358"] = {
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "management_currency": "Guideline/device/FDA claims rechecked 2026-09-11; textbook physiology/anatomy retained as durable foundation.",
        "canonical_link": {"domain": DOMAIN, "topic": module.get("topic")},
    }
    module["deliberate_review_v358"] = {
        "foundation": "differentiate cochlear/neural SNHL from conductive loss and avoid equating SNHL with CN VIII disease",
        "application": "use tempo, laterality, speech performance and objective testing to select the diagnostic pathway",
        "senior_decision": "separate sudden-treatment windows, retrocochlear escalation, chronic rehabilitation, CI referral and narrow molecular therapy indications",
        "traps": [
            "calling every SNHL 'nerve deafness'",
            "missing sudden SNHL because the otoscopic exam is normal",
            "ordering routine head CT or shotgun laboratory testing for uncomplicated idiopathic SSNHL",
            "delaying salvage intratympanic steroids beyond the evidence window without counseling",
            "ignoring asymmetric speech recognition because pure-tone thresholds look only mildly asymmetric",
            "leaving a poorly aided patient in hearing aids indefinitely without CI referral",
            "generalizing one cochlear-implant manufacturer's FDA label to every device",
            "generalizing OTOF-specific gene therapy to nonsyndromic or ungenotyped SNHL",
        ],
    }

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [module.get("topic")], "count": 1}
