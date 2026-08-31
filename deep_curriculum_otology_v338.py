"""v33.8 — source-grounded cochlear implant candidacy vs operative execution separation.

The duplicate audit flags Cochlear Implant Candidacy vs Cochlear Implant Surgery because both
can collapse into generic CI indications/steps. This bounded patch gives candidacy the
referral/testing/ear-selection/expectations job and surgery the anatomy/access/electrode/
complication-prevention job. It preserves later revision/failure content as a separate pathway.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


COCHLEAR_IMPLANT_REBUILD_V338 = {
    "cochlear implant candidacy": {
        "recognize": (
            "Use this card to decide WHO should be referred/evaluated for cochlear implantation, not to rehearse mastoidectomy steps. "
            "CI is not a last-resort treatment reserved only for bilateral profound deafness. Refer patients with sensorineural hearing loss who derive limited functional benefit from appropriately fit hearing aids, including patients with substantial residual low-frequency hearing, asymmetric hearing loss, or single-sided deafness when the clinical scenario fits contemporary indications. In adults, a practical referral screen is the REVISED 60/60 rule applied EAR-SPECIFICALLY: PTA about >=60 dB HL with unaided monosyllabic word recognition <=60% in the worse ear should trigger formal CI evaluation, while patients outside that screen may still qualify."
        ),
        "localize": (
            "Treat EACH EAR as a separate auditory organ. Characterize laterality, duration and etiology of hearing loss, residual acoustic hearing, speech-recognition performance, prior hearing-aid use, and the contralateral ear's function. The poorer ear is often implanted when anatomy and history are otherwise symmetric, but do not reflexively sacrifice the worse ear if that side has cochlear ossification, an absent/nonfunctional cochlear nerve, chronic infection, unfavorable malformation, or another surgical limitation. Residual low-frequency hearing can support hearing-preservation/electric-acoustic stimulation rather than exclude implantation."
        ),
        "workup": (
            "Formal candidacy requires optimized amplification and EAR-SPECIFIC aided speech testing, not an unaided audiogram alone. Verify hearing aids to prescriptive targets, obtain aided CNC monosyllabic word scores and sentence testing such as AzBio as appropriate, and assess real-world communication/QOL goals. Adult ACI Alliance recommendations support CI candidacy when CNC performance in the ear to be implanted is <=50% despite optimized amplification, with sentence testing used in part for payer qualification. Remember CANDIDACY is not synonymous with COVERAGE: CMS currently defines limited benefit for covered bilateral moderate-to-profound SNHL as <=60% correct on recorded open-set sentence recognition in the best-aided condition, while evidence-based practice may support patients outside a payer label. Obtain temporal-bone imaging to assess cochlear patency/anatomy and the cochlear nerve as clinically appropriate; MRI is particularly important when nerve deficiency, retrocochlear disease, or inner-ear malformation is a concern."
        ),
        "manage": (
            "Counsel around EXPECTED BENEFIT, not simply eligibility. Important outcome modifiers include duration of auditory deprivation, age at onset, etiology, cognition/communication needs, language exposure, hearing-aid history, rehabilitation engagement and family/support structure; none should be converted into a simplistic age cutoff. Pediatric candidacy must consider month-for-month auditory/language progress and functional benefit with well-fit amplification rather than waiting for a child to 'fail long enough.' Review pneumococcal vaccination status because CI recipients have increased pneumococcal meningitis risk; CDC recommends indicated pneumococcal vaccination for candidates/recipients and, when feasible, completion of recommended doses at least 2 weeks before surgery."
        ),
        "operate": (
            "The operative decision on this card is WHICH EAR / WHICH STRATEGY, not the drilling sequence. Integrate ear-specific speech performance, residual hearing, anatomy, chronic ear disease, vestibular status, patient preference, hearing-aid use in the opposite ear and the possibility of bimodal or bilateral hearing. Discuss hearing-preservation intent/electric-acoustic stimulation when useful low-frequency hearing remains. Flag cases needing a modified surgical plan before the day of surgery: cochlear ossification after meningitis, congenital malformation, prior mastoid surgery, active/chronic ear disease, otosclerosis, abnormal facial-nerve course, or cochlear nerve deficiency."
        ),
        "teach": (
            "Chief/boards discriminator: CANDIDACY asks WHO benefits, WHETHER each ear qualifies, and WHICH ear/strategy best serves the patient. Use optimized aids and ear-specific speech testing; do not use residual hearing, advanced age, or the old 'bilateral profound only' model as automatic exclusions. Know the revised 60/60 REFERRAL rule, understand that payer coverage can be narrower than clinical candidacy, and separate candidacy from the operative mechanics taught on the Cochlear Implant Surgery card."
        ),
        "tags": [
            "cochlear implant candidacy", "revised 60/60", "CNC", "AzBio", "ear-specific testing",
            "single-sided deafness", "asymmetric hearing loss", "electric acoustic stimulation", "hearing preservation",
            "CMS NCD 50.3", "pneumococcal vaccination"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cochlear implantation, candidacy, imaging, ear selection and hearing-preservation principles",
            "K.J. Lee's Essential Otolaryngology, 12e — cochlear implantation indications, temporal-bone anatomy and operative principles",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — cochlear implant evaluation and otologic surgical framework",
            "American Cochlear Implant Alliance Task Force, Laryngoscope 2024 — adult candidacy, revised 60/60 referral rule, optimized hearing aids and ear-specific CNC/AzBio testing",
            "American Cochlear Implant Alliance Task Force, Ear & Hearing 2022 — pediatric candidacy based on audiology, functional progress and benefit with amplification",
            "AAO-HNS Position Statement: Cochlear Implants, reviewed August 2025 — CI appropriate in children and adults with moderate-to-profound hearing loss with inadequate benefit from appropriately fit hearing aids",
            "CMS NCD 50.3, effective September 26 2022 — <=60% recorded open-set sentence recognition in best-aided condition for covered bilateral moderate-to-profound SNHL",
            "CDC Cochlear Implants and Vaccine Recommendations, February 25 2026 — pneumococcal vaccination and timing before surgery",
        ],
    },
    "cochlear implant surgery": {
        "recognize": (
            "Use this card once candidacy and ear selection are established. The surgical objective is safe placement of the receiver-stimulator and electrode array with atraumatic access to the cochlea, correct scala-tympani insertion when achievable, secure device positioning, and prevention/recognition of facial-nerve, CSF, wound, vestibular and electrode-position complications. This is NOT the card for deciding whether a patient meets audiologic candidacy."
        ),
        "localize": (
            "Know the operative corridor: cortical mastoidectomy -> mastoid antrum -> facial recess bounded by facial nerve medially/posteriorly, chorda tympani laterally/anteriorly and incus buttress superiorly -> round-window niche/promontory -> basal turn/scala tympani. Confirm the facial nerve course before opening the facial recess. In malformed ears, anatomy may be displaced and the risk of CSF gusher, facial-nerve anomaly or electrode misdirection into the IAC is higher. Preoperative CT/MRI findings should change the plan rather than merely document anatomy."
        ),
        "workup": (
            "Before incision, verify side/device, imaging, vaccination status, hearing-preservation intent and any anatomy that predicts difficult access or insertion. Identify cochlear ossification, otosclerosis, congenital malformation, prior mastoid cavity, chronic infection and abnormal facial-nerve course. For suspected cochlear nerve deficiency, ensure the nerve has been appropriately assessed because a technically perfect electrode cannot compensate for an absent functional neural target. Plan array type and insertion strategy around anatomy and residual hearing rather than choosing an electrode in isolation from the audiologic plan."
        ),
        "manage": (
            "Standard modern implantation usually uses a transmastoid facial-recess approach with round-window or extended-round-window entry when the window is accessible; a separate cochleostomy is used when anatomy requires it. Favor an atraumatic insertion strategy: minimal intracochlear trauma, controlled insertion without force, avoidance of suction directly at the cochleostomy/round window, and preservation of viable residual hearing when that is an explicit goal. Intraoperative impedance/neural-response telemetry can confirm device integrity and neural response but does not by itself prove ideal scalar position. Postoperative activation, mapping and auditory rehabilitation are required parts of treatment, not afterthoughts."
        ),
        "operate": (
            "OPERATIVE SEQUENCE: position/prep -> postauricular exposure and receiver-stimulator bed/pocket -> cortical mastoidectomy with identification of tegmen, sigmoid and lateral semicircular canal -> open facial recess while protecting facial nerve/chorda -> expose round-window niche and confirm middle-ear landmarks -> open the round window/extended round window or perform a deliberate cochleostomy when required -> insert the array slowly into the cochlea without force -> secure the lead/device -> perform impedance and neural-response testing and obtain intraoperative/postoperative position confirmation according to local practice -> close without device migration or flap compromise. Stop and reassess if resistance is unexpected; forcing an array risks tip fold-over, extracochlear placement, translocation or insertion into an abnormal pathway. In IP-III and selected severe malformations, anticipate brisk CSF flow and risk of electrode entry toward the IAC; meticulous preoperative imaging and controlled sealing are essential."
        ),
        "teach": (
            "Chief/boards discriminator: SURGERY asks whether you can identify the facial-recess/round-window corridor, insert into the intended cochlear compartment without trauma, and manage anatomic danger. Round-window access is generally favored when identifiable because it provides direct scala-tympani entry, but anatomy controls the route. Know the complications: facial-nerve injury/stimulation, chorda injury, CSF leak/gusher, meningitis, vertigo, wound/device infection or extrusion, electrode tip fold-over/migration/misplacement, loss of residual hearing and device failure. Do not mix these operative decisions with the separate audiologic candidacy algorithm."
        ),
        "tags": [
            "cochlear implant surgery", "facial recess", "round window", "scala tympani", "receiver stimulator",
            "electrode array", "hearing preservation", "CSF gusher", "cochlear malformation", "facial nerve",
            "tip fold-over", "neural response telemetry"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cochlear implant surgical anatomy, facial recess, round-window/cochleostomy techniques, malformed cochlea and complications",
            "K.J. Lee's Essential Otolaryngology, 12e — temporal-bone anatomy and cochlear implantation operative principles",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — cochlear implantation operative approach and complication framework",
            "American Cochlear Implant Alliance adult candidacy recommendations, Laryngoscope 2024 — preoperative imaging/medical evaluation, residual-hearing and ear-selection considerations",
            "CDC Cochlear Implants and Vaccine Recommendations, February 25 2026 — pneumococcal meningitis prevention",
            "Contemporary cochlear-implant surgical literature — round-window/scalal-position emphasis, electrode malposition, CSF gusher and malformed-ear risk",
        ],
    },
}


def apply_cochlear_implant_rebuild_v338(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = COCHLEAR_IMPLANT_REBUILD_V338.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v338"] = True
            module["semantic_role_v338"] = (
                "CI candidacy/referral/ear-selection" if key == "cochlear implant candidacy" else
                "CI operative anatomy/electrode insertion/complication prevention"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
