"""v28.4 — source-grounded Eustachian tube dysfunction Concept Hub rebuild.

Separates obstructive/dilatory ETD from patulous ETD so the two canonical cards teach
opposite physiology, distinct objective findings, different procedural options, and the
critical contraindication to treating patulous disease with balloon dilation.
"""

import re

DOMAIN = "Otology / Neurotology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


ETD_REBUILD_V284 = {
    "eustachian tube dysfunction": {
        "recognize": (
            "Recognize OBSTRUCTIVE/DILATORY Eustachian tube dysfunction as failure of middle-ear pressure equalization, not as a synonym for any sensation of ear fullness. Typical symptoms are pressure/fullness, popping, muffled hearing, otalgia or difficulty clearing the ear; chronic disease may produce tympanic-membrane retraction or effusion. Baro-challenge ETD can be symptomatic only during descent/ascent, with a normal ear between exposures. Before labeling OETD, actively separate it from patulous ETD, temporomandibular pain, superior canal dehiscence, hydrops/Meniere phenotype and other causes of aural fullness."
        ),
        "localize": (
            "Localize the dysfunction to the cartilaginous ET functional valve and classify the phenotype: acute inflammatory dilatory dysfunction, chronic obstructive/dilatory dysfunction, or baro-challenge dysfunction. Obstructive physiology means the tube does not open effectively enough to equilibrate nasopharyngeal and middle-ear pressure. Nasal/nasopharyngeal inflammation, adenoid tissue, scarring or a mass may contribute, but unilateral adult middle-ear disease deserves nasopharyngeal examination rather than an automatic assumption of benign ETD. The key physiologic contrast is that OETD is TOO CLOSED; patulous ETD is TOO OPEN."
        ),
        "workup": (
            "Pair symptoms with objective evidence whenever possible. Perform pneumatic otoscopy/otomicroscopy, tympanometry and audiometry; chronic dilatory ETD is supported by tympanic-membrane retraction and/or negative middle-ear pressure, while effusion may create a flat tympanogram. Nasal endoscopy assesses the ET orifice and excludes inflammatory, scar-related or mass lesions. ETDQ-7 can quantify symptom burden but is not sufficiently specific to diagnose OETD by itself. A normal office tympanogram does not exclude baro-challenge ETD when the history is classic. Routine CT is not required unless alternate pathology or specific procedural/anatomic concern is suspected."
        ),
        "manage": (
            "Treat a demonstrated contributor rather than prescribing indefinite empiric therapy for every full ear. Manage active rhinitis/sinus or nasopharyngeal inflammation when present and observe transient post-URI dysfunction when clinically appropriate. Tympanostomy can ventilate the middle ear when persistent negative pressure/effusion or pressure-sensitive symptoms justify it, but failure of an open tube/myringotomy to relieve the complaint should force reconsideration of the diagnosis. For adults with chronic, clinically significant OETD and appropriate objective evaluation, balloon dilation of the cartilaginous ET is a treatment option; it is not a treatment for nonspecific fullness and is contraindicated when the true physiology is patulous."
        ),
        "operate": (
            "For balloon dilation, confirm the obstructive phenotype before entering the ET. Endoscopically guide an FDA-cleared balloon catheter into the CARTILAGINOUS portion of the tube and do not force instrumentation toward the bony ET/carotid canal. Counsel regarding bleeding, mucosal trauma/scarring, infection, emphysema, need for additional procedures and the possibility of inducing patulous symptoms. Tympanostomy tube placement is not a mandatory prerequisite to BDET. The operative mistake with the largest conceptual consequence is dilating a patient whose main problem is an abnormally open tube."
        ),
        "teach": (
            "Chief/boards framework: OETD = TOO CLOSED. Require a compatible pressure-dysregulation history plus appropriate ear findings when the phenotype should be objectively visible; remember that baro-challenge disease may look normal at baseline. Retraction/negative pressure supports dilatory dysfunction; breathing-synchronous TM movement argues for patulous disease instead. ETDQ-7 measures symptoms but does not establish the diagnosis. Balloon dilation is for selected chronic obstructive ETD after a multifaceted evaluation—not for isolated aural fullness, not for a diagnostic fishing expedition, and never for confirmed patulous ETD."
        ),
        "tags": [
            "eustachian tube dysfunction", "obstructive ETD", "dilatory ETD", "baro-challenge ETD",
            "tympanometry", "ETDQ-7", "balloon dilation", "BDET", "tympanic membrane retraction"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — Eustachian tube physiology, obstructive dysfunction, middle-ear consequences, and treatment",
            "K.J. Lee's Essential Otolaryngology, 12e — Eustachian tube dysfunction, tympanometry, and differential diagnosis",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — ETD evaluation and procedural pearls",
            "Schilder et al., Clinical Otolaryngology 2015 — international consensus definition, subtypes, presentation, and diagnostic signs of ETD",
            "AAO-HNSF Clinical Consensus Statement: Balloon Dilation of the Eustachian Tube, 2019 — adult OETD selection, evaluation, contraindications, and perioperative principles",
        ],
    },
    "patulous eustachian tube dysfunction": {
        "recognize": (
            "Recognize PATULOUS Eustachian tube dysfunction by AUTOPHONY—especially hearing one's own breathing and voice abnormally loudly—often with aural fullness. Symptoms commonly fluctuate, may worsen with exercise or dehydration, and may improve when supine or during an upper-respiratory infection as mucosal congestion narrows the lumen. Weight loss and habitual sniffing are useful clues but are not required. Do not mistake generic echoing/fullness for PET: superior semicircular canal dehiscence and other third-window disorders, occlusion phenomena, hydrops and OETD can mimic parts of the history."
        ),
        "localize": (
            "Localize PET to failure of the cartilaginous ET valve to remain closed at rest, creating an abnormal open acoustic and pressure conduit between nasopharynx and middle ear. This is the physiologic inverse of obstructive ETD. Transmission of respiratory pressure and sound explains breathing autophony and respiratory movement of the tympanic membrane. Habitual sniffing may transiently create negative middle-ear pressure and can produce retraction that falsely looks 'obstructive,' so the history must be interpreted with dynamic testing rather than static otoscopy alone."
        ),
        "workup": (
            "Try to reproduce and objectively confirm the open-tube physiology while the patient is symptomatic. Examine the tympanic membrane for breathing-synchronous excursion during nasal respiration; long time-base tympanometry can demonstrate respiratory pressure fluctuations, while sonotubometry or tubo-tympano-aerodynamic testing can support abnormal patency where available. Note whether symptoms improve with supine positioning or temporary obstruction of the pharyngeal ET orifice. The Japan Otological Society framework requires characteristic symptoms plus symptom improvement with tubal obstruction maneuvers and/or objective evidence of patency for definite disease. If autophony is dominated by internal body sounds or vestibular sound/pressure phenomena, evaluate for a third-window lesion rather than forcing a PET diagnosis."
        ),
        "manage": (
            "Start conservatively because PET fluctuates and invasive closure can trade autophony for obstructive middle-ear disease. Correct reversible precipitants such as excessive weight loss/dehydration when appropriate, avoid habitual decongestant use that worsens mucosal dryness, and counsel against repetitive sniffing when it perpetuates pressure problems. Hydration and selected topical/mucosal-bulking strategies are used in practice, although evidence quality varies. Escalate only when symptoms are persistent, objectively supported and functionally significant. Balloon dilation has the WRONG physiologic direction and should not be used for PET."
        ),
        "operate": (
            "For severe refractory objectively confirmed PET, procedural strategies aim to NARROW or OCCLUDE the pathologic lumen rather than enlarge it. Options described by subspecialty centers include ET plugging/occlusion, augmentation around the cartilaginous valve, or other targeted techniques; patient selection is crucial because overcorrection can cause chronic obstructive ETD, effusion or conductive hearing problems. The Kobayashi silicone plug has prospective multicenter evidence for severe PET but is not a routine first-line intervention. Any irreversible procedure should follow dynamic confirmation that the patient's disabling symptoms truly track an abnormally patent tube."
        ),
        "teach": (
            "Chief/boards framework: PET = TOO OPEN. The discriminator that should stop you from reflexively calling this 'ETD' is BREATHING AUTOPHONY with dynamic evidence such as respiratory TM movement, especially when symptoms improve supine. OETD tends toward negative pressure/retraction and difficulty equalizing; PET transmits nasopharyngeal sound/pressure continuously. A retracted drum does not exclude PET if habitual sniffing created the negative pressure. Never balloon-dilate confirmed PET: treatment, when needed, moves toward narrowing/occlusion, exactly opposite the obstructive card."
        ),
        "tags": [
            "patulous eustachian tube", "PET", "autophony", "breathing autophony", "respiratory tympanic membrane movement",
            "sonotubometry", "long time-base tympanometry", "habitual sniffing", "Kobayashi plug"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — patulous Eustachian tube physiology, differential diagnosis, and management",
            "K.J. Lee's Essential Otolaryngology, 12e — patulous ETD clinical presentation and otologic differential",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — PET recognition and management pearls",
            "Kobayashi et al., Auris Nasus Larynx 2018 — Japan Otological Society diagnostic criteria for patulous Eustachian tube",
            "Oshima et al., Auris Nasus Larynx 2025 and Yoshida et al., Auris Nasus Larynx 2026 — contemporary validation/characterization of JOS PET criteria",
            "Ikeda et al., Laryngoscope 2020 — prospective multicenter silicone-plug series for severe refractory PET",
        ],
    },
}


def apply_otology_etd_rebuild_v284(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = ETD_REBUILD_V284.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v284"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
