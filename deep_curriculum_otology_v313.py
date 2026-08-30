"""v31.3 — source-grounded cochlear implant candidacy / surgery / failure-revision rebuild.

Separates three commonly collapsed Concept Hub jobs:
1) candidacy = who should be referred/selected and how to evaluate benefit,
2) surgery = temporal-bone anatomy, insertion strategy, perioperative risk and activation,
3) failure/revision = structured troubleshooting, hard vs soft failure and reimplantation.
"""

import re

DOMAIN = "Otology / Neurotology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


COCHLEAR_IMPLANT_REBUILD_V313 = {
    "cochlear implant candidacy": {
        "recognize": (
            "This card owns REFERRAL AND SELECTION, not the mastoidectomy. Refer patients whose sensorineural hearing loss is not adequately managed by optimized hearing aids rather than waiting for 'profound deafness.' In adults, evaluate each ear independently; the American Cochlear Implant Alliance revised 60/60 benchmark (PTA >=60 dB HL and unaided monosyllabic word recognition <=60% in the ear being considered) is a referral screen, not an exclusion rule. Residual acoustic hearing, asymmetric hearing loss and single-sided deafness can coexist with modern CI candidacy. Duration/etiology of deafness, cognition, communication goals, prior amplification and rehabilitation support affect counseling and prognosis but are rarely single absolute contraindications."
        ),
        "localize": (
            "Localize the hearing problem across the AUDITORY PATHWAY before promising benefit. Confirm a cochlear/sensorineural deficit that is poorly served by acoustic amplification and determine whether the cochlear nerve and central pathway are capable of meaningful stimulation. Ear-specific performance matters: a strong contralateral ear should not hide a poorly performing implant ear. In children, distinguish audibility from functional progress—appropriately fitted hearing aids with inadequate month-for-month auditory, speech and language development should trigger CI evaluation even when a child does not fit an outdated pure-tone stereotype. Cochlear nerve deficiency, severe inner-ear malformation, long auditory deprivation and developmental comorbidity modify expected outcome rather than being reduced to a yes/no audiogram rule."
        ),
        "workup": (
            "Use a multidisciplinary CI evaluation. Verify appropriately fitted hearing aids and obtain ear-specific aided speech testing using a standardized battery; contemporary adult recommendations begin with CNC words in the ear being considered and use AzBio sentence testing for additional characterization/coverage qualification. Keep CLINICAL CANDIDACY separate from PAYER COVERAGE: FDA labels and CMS rules are not identical to evidence-based referral practice. Review otologic history, prior meningitis, chronic ear disease, prior temporal-bone surgery, vestibular symptoms and communication goals. CT temporal bone is useful for bony anatomy, ossification and surgical planning; MRI is especially important when cochlear-nerve integrity, retrocochlear pathology or soft-tissue labyrinthine obstruction is a concern. Complete age/risk-appropriate pneumococcal vaccination; CDC recommends indicated pneumococcal doses at least 2 weeks before implantation when possible."
        ),
        "manage": (
            "Counsel toward the best HEARING STRATEGY rather than toward a device. Optimize conventional amplification when it still provides useful speech access; discuss bimodal hearing, bilateral implantation, electric-acoustic stimulation, or ear-specific implantation when appropriate. Explain that CI restores access to sound but does not reproduce normal hearing, and outcome depends on auditory deprivation, neural anatomy, rehabilitation, consistent device use and patient-specific factors. For children, family engagement, educational/communication environment and early auditory-language intervention are part of treatment, not administrative extras. For adults, do not withhold referral simply because a patient falls outside a payer criterion; document evidence-based candidacy and separately address coverage."
        ),
        "operate": (
            "The operative decision in this card is WHICH EAR / WHETHER TO IMPLANT, not how to perform the facial recess. Choose the ear by integrating aided performance, residual hearing, anatomic feasibility, duration of deprivation, vestibular considerations, prior surgery and the plan for bilateral/bimodal hearing. Address active middle-ear infection or unsafe chronic ear disease before or as part of a staged implant strategy. Patients with cochlear ossification, inner-ear malformation or cochlear-nerve abnormality need individualized counseling because anatomy may alter electrode choice, insertion depth, CSF-leak risk and expected performance. Once the patient is selected and the side chosen, transition to the separate COCHLEAR IMPLANT SURGERY framework."
        ),
        "teach": (
            "Chief/boards framework: CANDIDACY asks, 'Would electrical hearing outperform optimized acoustic hearing for this EAR, and can the auditory pathway/use environment support benefit?' Think EAR-SPECIFIC AIDED PERFORMANCE + ANATOMY/NERve + GOALS/REHAB. Revised 60/60 is a referral trigger, not the final indication. Residual hearing is not a contraindication. Pediatric candidacy is developmental: inadequate auditory-language progress despite appropriate amplification matters. Coverage criteria are not synonymous with candidacy. Preop vaccination and anatomy belong in the evaluation; mastoidectomy steps and device-failure troubleshooting belong to separate cards."
        ),
        "tags": ["cochlear implant candidacy", "revised 60/60", "CNC", "AzBio", "ear-specific testing", "pediatric cochlear implant", "single-sided deafness", "cochlear nerve", "pneumococcal vaccine", "aural rehabilitation"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cochlear implantation, candidacy, imaging, outcomes and rehabilitation",
            "K.J. Lee's Essential Otolaryngology, 12e, Chapter 20 Cochlear Implants — candidacy, evaluation, operative anatomy and complications",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — cochlear implantation candidacy and operative pearls",
            "American Cochlear Implant Alliance Task Force Recommendations for Determining Cochlear Implant Candidacy in Adults, Laryngoscope 2024",
            "American Cochlear Implant Alliance Task Force Guidelines for Determining Cochlear Implant Candidacy in Children, Ear Hear 2022",
            "CDC Pneumococcal Vaccine Recommendations for People with Cochlear Implants, updated 2026"
        ],
    },
    "cochlear implant surgery": {
        "recognize": (
            "This card owns the OPERATION. Standard implantation places the receiver-stimulator securely and introduces an electrode array into the scala tympani through a round-window, extended-round-window or selected cochleostomy approach. The classic route is cortical mastoidectomy plus posterior tympanotomy/facial recess between the facial nerve and chorda tympani. The surgeon must understand facial-nerve course, chorda, incus buttress, round-window niche, promontory, hypotympanum and tegmen before drilling. Anatomic variants, prior mastoid surgery, ossification and congenital malformations may require a modified approach; they are not reasons to memorize one rigid tunnel."
        ),
        "localize": (
            "Localize the surgical hazards before opening the cochlea. The facial recess is bounded by the facial nerve posteromedially, chorda tympani anterolaterally and fossa incudis superiorly; over-aggressive drilling risks facial weakness or taste disturbance. Identify the round-window membrane and planned basal-turn trajectory rather than blindly drilling an anteroinferior cochleostomy. In malformed ears anticipate aberrant facial-nerve anatomy and CSF/perilymph gusher; after meningitis or labyrinthitis anticipate partial/complete cochlear ossification. Preoperative CT defines bony surgical anatomy while MRI complements it for the cochlear nerve and intracochlear soft tissue."
        ),
        "workup": (
            "Before incision, confirm the selected ear, device/electrode plan, current imaging, vaccination status and absence of uncontrolled infection. Review residual hearing because hearing-preservation goals influence electrode and insertion strategy. Intraoperatively confirm array position/behavior with manufacturer-appropriate impedance and neural-response telemetry when available; unexpected resistance, abnormal insertion trajectory or nonphysiologic measurements should trigger reassessment rather than forceful advancement. Postoperative imaging is selective by center/device/anatomic complexity but is appropriate when electrode position, tip fold-over, migration or misplacement is suspected."
        ),
        "manage": (
            "Preserve tissue and residual function when feasible: meticulous soft-tissue handling, avoidance of unnecessary cochlear trauma, controlled insertion and secure receiver/electrode fixation reduce later problems. Counsel about facial-nerve injury/stimulation, dysgeusia, vertigo/imbalance, tinnitus change, wound or device infection/extrusion, hematoma, CSF leak/gusher, meningitis, electrode migration/misplacement and device failure. Activation is not performed as an immediate proof of surgical success; after wound healing, audiology activates/maps the device and begins longitudinal programming and rehabilitation. Persistent poor performance after activation should move into a structured diagnostic pathway rather than being labeled 'bad surgery.'"
        ),
        "operate": (
            "Boards sequence: expose a safe receiver-stimulator bed/pocket -> cortical mastoidectomy -> identify incus/facial nerve/chorda -> open the facial recess -> visualize the round window -> create the planned cochlear opening -> insert the electrode atraumatically to the intended depth -> secure lead/device -> confirm impedance/neural responses -> close without pressure over the implant. Do not force an array against resistance: stop and reassess for ossification, false passage, fold-over or altered anatomy. In a gusher, obtain electrode placement and seal the cochleostomy/round-window region with appropriate soft tissue rather than abandoning implantation reflexively."
        ),
        "teach": (
            "Chief/boards framework: SURGERY asks, 'Can I reach the round window safely, place the electrode in the intended scala with minimal trauma, and prevent device/wound complications?' Know FACIAL RECESS anatomy, round-window orientation, aberrant facial nerve and gusher risk, and post-meningitic ossification. Atraumatic insertion matters when residual hearing is valuable. Telemetry supports—but does not replace—anatomic judgment. The operation ends with a secured system and viable wound; candidacy testing occurred before surgery, while declining performance months/years later belongs to the FAILURE/REVISION card."
        ),
        "tags": ["cochlear implant surgery", "facial recess", "posterior tympanotomy", "round window", "scala tympani", "electrode insertion", "cochlear ossification", "CSF gusher", "neural response telemetry", "hearing preservation"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cochlear implant surgical anatomy, electrode insertion, complications and special anatomy",
            "K.J. Lee's Essential Otolaryngology, 12e, Chapter 20 Cochlear Implants — operative technique and complications",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — cochlear implant operative steps and complications",
            "CDC Pneumococcal Vaccine Recommendations for People with Cochlear Implants, updated 2026 — meningitis-risk counseling and preoperative vaccination"
        ],
    },
    "cochlear implant failure revision": {
        "recognize": (
            "This card owns TROUBLESHOOTING AND REIMPLANTATION after a previously implanted system. Do not collapse every decline into 'device failure.' HARD failure means demonstrable loss of device function/integrity; SOFT failure is a clinical syndrome of declining performance, intermittent function, aversive auditory or nonauditory symptoms despite no definitive integrity-test abnormality and is therefore a diagnosis of exclusion. Also consider programming/processor problems, electrode migration or tip fold-over, receiver migration, infection/extrusion, trauma, facial-nerve stimulation, cochlear ossification, neural/cognitive change and unrealistic mapping/rehabilitation expectations."
        ),
        "localize": (
            "Localize failure to EXTERNAL HARDWARE/PROGRAMMING, INTERNAL DEVICE, ELECTRODE POSITION, SURGICAL SITE, or PATIENT/AUDITORY PATHWAY. A sudden complete loss of communication with abnormal integrity testing favors hard failure. Gradual or intermittent performance decline with normal manufacturer testing may still represent soft failure, but first exclude mapping problems, cable/processor issues, middle-ear disease, cognitive/neurologic change and electrode problems. Pain, erythema, drainage, skin breakdown or exposed hardware points toward a wound/infectious problem; new facial stimulation may reflect programming, current spread or electrode migration."
        ),
        "workup": (
            "Use a staged failure workup: detailed symptom/performance timeline -> physical/wound and otoscopic examination -> audiology with aided speech comparison to prior best performance -> remapping and external-component exchange -> electrode impedances/telemetry -> manufacturer integrity testing -> targeted imaging when migration, fold-over, extrusion, trauma or intracochlear position is in question. Compare against the patient's own historical baseline rather than a population average. A NORMAL INTEGRITY TEST DOES NOT EXCLUDE SOFT FAILURE. When infection is present, define whether it is superficial and salvageable or involves the receiver/electrode system such that explantation is safer."
        ),
        "manage": (
            "Correct reversible nonoperative causes first when the implant is stable: replace faulty external hardware, optimize mapping, treat middle-ear/wound disease and restore rehabilitation. Revision is appropriate for confirmed hard failure, significant electrode/device migration, extrusion/infection not safely salvageable, or convincing soft failure after a multidisciplinary exclusion workup when symptoms/performance materially impair use. Counsel that reimplantation usually restores or maintains speech performance, but outcome is not guaranteed; long implant duration, fibrosis/ossification, infection, altered anatomy and neural factors can make explantation/reinsertion more difficult."
        ),
        "operate": (
            "Plan revision from the FAILURE MECHANISM. Review the original operative report, device model/electrode, imaging and recipient anatomy. Re-enter with facial-nerve and wound-scar risk in mind; preserve a usable cochlear lumen during explantation and avoid unnecessary traction on an intracochlear array. Replace or reposition the device/electrode when indicated and choose an alternate receiver bed or surgical strategy if migration, infection or soft-tissue compromise caused the failure. Fibrosis/neo-ossification can prevent full reinsertion, so have an electrode/approach contingency. After reimplantation confirm objective function and return the patient to audiologic activation/remapping and performance follow-up."
        ),
        "teach": (
            "Chief/boards framework: FAILURE/REVISION asks, 'Is the problem hardware, electrode position, wound, programming, or the patient—and is revision likely to fix it?' HARD failure = objective device malfunction. SOFT failure = meaningful symptoms/performance decline despite nondiagnostic integrity testing after alternatives are excluded. Work from outside-in before committing to surgery, but do not let a normal integrity test falsely reassure you when the clinical pattern is convincing. Revision is mechanism-directed; after reimplantation most series show recovery toward prior auditory performance, while infection/ossification/anatomic constraints require more guarded counseling."
        ),
        "tags": ["cochlear implant failure", "cochlear implant revision", "hard failure", "soft failure", "integrity testing", "electrode migration", "device extrusion", "reimplantation", "mapping", "cochlear fibrosis"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cochlear implant complications, device failure and revision",
            "K.J. Lee's Essential Otolaryngology, 12e, Chapter 20 Cochlear Implants — implant complications and reimplantation",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — cochlear implant failure/revision pearls",
            "Lane et al., Otol Neurotol 2021 — adult CI failure/revision systematic review",
            "European consensus-derived hard/soft/device/medical failure taxonomy used in contemporary CI failure literature"
        ],
    },
}


def apply_cochlear_implant_rebuild_v313(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = COCHLEAR_IMPLANT_REBUILD_V313.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v313"] = True
        module["semantic_role_v313"] = {
            "cochlear implant candidacy": "ear-specific referral, selection, prognostic evaluation and rehabilitation planning",
            "cochlear implant surgery": "temporal-bone operative anatomy, electrode insertion and perioperative complication avoidance",
            "cochlear implant failure revision": "postimplant troubleshooting, hard/soft failure classification and mechanism-directed reimplantation",
        }[key]
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
