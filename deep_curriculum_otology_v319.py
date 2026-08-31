"""v31.9 — source-grounded obstructive vs patulous Eustachian tube dysfunction separation.

The generic ETD card owns failure of middle-ear pressure equalization from obstructive/
dilatory or baro-challenge dysfunction. The patulous card owns pathologic resting patency,
autophony, respiratory tympanic-membrane motion, and therapies that restore closure rather
than enlarge the tube. This prevents the clinically dangerous error of treating a tube that
is already too open with balloon dilation or indiscriminate decongestion.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


ETD_REBUILD_V319 = {
    "eustachian tube dysfunction": {
        "recognize": (
            "Use this card for OBSTRUCTIVE/DILATORY OR BARO-CHALLENGE ETD: the cartilaginous Eustachian tube does not open adequately to equalize middle-ear pressure. Typical symptoms are aural pressure/fullness, popping, muffled or fluctuating conductive hearing, and pain or inability to equalize with altitude/diving. Chronic dilatory dysfunction can produce negative middle-ear pressure, effusion, tympanic-membrane retraction/atelectasis, ossicular damage, and cholesteatoma. Do not diagnose obstructive ETD from fullness alone, and do not use this pathway for a patient whose dominant complaint is hearing their own breathing/voice from a tube that is abnormally OPEN."
        ),
        "localize": (
            "Localize the failure along the middle-ear/Eustachian-tube/nasopharyngeal system. Otoscopy or microscopy may show retraction, reduced mobility, effusion, or atelectasis; tympanometry can show negative pressure (type C) or an effusion pattern (type B). Nasal endoscopy evaluates the nasopharyngeal orifice for inflammation, adenoid tissue, scarring, or a mass and also tests dynamic opening with swallowing. In an adult with persistent unilateral middle-ear effusion, examine the nasopharynx rather than labeling the finding 'ETD' and stopping. Baro-challenge ETD is different: otoscopy and tympanometry may be normal at baseline because dysfunction is exposed only by pressure change."
        ),
        "workup": (
            "Require a coherent phenotype before intervention: symptom history and duration, otoscopy/microscopy, tympanometry, and audiometry when hearing is affected; add nasal endoscopy when chronic obstructive disease, unilateral effusion, or balloon dilation is being considered. The 2015 international consensus separates dilatory, baro-challenge, and patulous ETD; the 2019 AAO-HNS balloon-dilation consensus targets adults with obstructive ETD lasting >=3 months that meaningfully affects quality of life/function. ETDQ-7 can quantify symptoms but is not a stand-alone physiologic diagnosis. Exclude mimics such as TMJ disorder, superior canal dehiscence, inner-ear disease, and PATULOUS ETD before procedural treatment."
        ),
        "manage": (
            "Treat the cause and the middle-ear consequence, not the word 'ETD.' Acute URI-associated dysfunction often resolves. Treat documented allergic/inflammatory sinonasal disease when present, but do not promise that nasal steroids or decongestants cure chronic obstructive ETD in the absence of a treatable nasal disorder. Tympanostomy ventilation can bypass poor pressure equalization when persistent effusion/retraction or recurrent barotrauma justifies it. For appropriately selected chronic obstructive ETD after diagnostic confirmation, balloon dilation is an option; PATULOUS ETD is a contraindication because further opening can worsen the patient's problem. In children, AAO-HNS (2025) supports balloon dilation only in selected obstructive disease refractory to standard interventions such as tubes/adenoid management, not as automatic first-line therapy."
        ),
        "operate": (
            "PROCEDURAL PRINCIPLE: first prove that the tube is too closed. For balloon dilation, enter the cartilaginous Eustachian tube transnasally under visualization and avoid force against resistance or false passage; preoperative imaging is selective rather than a substitute for endoscopic/anatomic judgment, with special attention to skull-base/carotid abnormalities when relevant. Tympanostomy tubes ventilate the middle ear but do not repair tubal opening mechanics. When chronic retraction or cholesteatoma is already present, the operation must address that disease rather than assuming balloon dilation alone reverses established structural damage. Never perform balloon dilation for a patulous phenotype."
        ),
        "teach": (
            "Chief/boards discriminator: OBSTRUCTIVE ETD = TOO CLOSED / WILL NOT OPEN. Look for pressure-change symptoms plus objective middle-ear consequences when chronic; remember that baro-challenge disease may test normally between exposures. Confirm the phenotype before BDET. If the patient hears their own BREATHING, improves supine/head-down, or has TM motion synchronous with respiration, stop and switch to the patulous ETD card."
        ),
        "tags": ["obstructive Eustachian tube dysfunction", "dilatory ETD", "baro-challenge ETD", "type C tympanogram", "middle ear negative pressure", "balloon dilation Eustachian tube", "BDET", "tympanostomy tube"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — Eustachian-tube physiology, middle-ear ventilation, otitis media/retraction disease, and Eustachian-tube procedures",
            "K.J. Lee's Essential Otolaryngology, 12e — middle-ear/Eustachian-tube physiology and otologic differential diagnosis",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — obstructive ETD symptoms, tympanometry, nasopharyngeal evaluation, and middle-ear sequelae",
            "Schilder et al. Eustachian tube dysfunction: consensus statement on definition, types, clinical presentation and diagnosis. Clin Otolaryngol. 2015;40:407-411 — dilatory, baro-challenge, and patulous phenotypes",
            "Tucci et al. Clinical Consensus Statement: Balloon Dilation of the Eustachian Tube. Otolaryngol Head Neck Surg. 2019;161:6-17 — adult obstructive-ETD patient selection and perioperative framework",
            "AAO-HNS. Eustachian Tube Balloon Dilation in the Pediatric Population. Position Statement. 2025 — selected refractory pediatric OETD",
            "Sandoval. Diagnostic Algorithm for Eustachian Tube Dysfunction and Indications for Balloon Dilation of the Eustachian Tube. Otolaryngol Clin North Am. 2026 — exclude patulous ETD/TMJ/SSCD and phenotype-select BDET",
        ],
    },
    "patulous eustachian tube dysfunction": {
        "recognize": (
            "Use this card for a Eustachian tube that is ABNORMALLY OPEN AT REST. The high-yield symptom is autophony—especially hearing one's own BREATHING in the affected ear—often accompanied by voice autophony, aural fullness, or a hollow/barrel sensation. Symptoms commonly improve supine, head-down, or with venous engorgement and may worsen upright, with exercise, dehydration, or after substantial weight loss. Voice autophony alone is not specific because superior semicircular canal dehiscence can mimic it; breathing autophony plus objective respiratory coupling is much more persuasive."
        ),
        "localize": (
            "The lesion is failure of closure of the cartilaginous Eustachian-tube valve, creating abnormal acoustic/pressure communication between nasopharynx and middle ear. Examine the patient while SYMPTOMATIC and preferably upright: otoscopy may show the tympanic membrane moving medially/laterally with nasal respiration, and long time-base tympanometry can demonstrate impedance oscillations synchronous with breathing. Nasal endoscopy may show an unusually open lumen but can be normal when disease is intermittent. A low BMI or recent weight loss supports but does not establish the diagnosis."
        ),
        "workup": (
            "Build the diagnosis from characteristic symptoms plus objective evidence whenever possible. Ask specifically about breathing autophony, positional improvement, weight change, pregnancy/postpartum or other physiologic changes, prior head/neck radiation or surgery, neuromuscular disease, and prior Eustachian-tube procedures. Try to reproduce TM excursion with ipsilateral nasal breathing; long time-base tympanometry, sonotubometry, or tubo-tympano-aerodynamic testing can help in specialty practice. A 2025 large JOS-criteria series found breathing autophony strongly predictive and TM flutter the strongest objective discriminator; a 2026 prospective study highlights why intermittent PET can be missed when patients are asymptomatic in clinic. Exclude superior canal dehiscence when sound/pressure-induced vestibular symptoms or third-window features are present."
        ),
        "manage": (
            "Management aims to RESTORE CLOSURE or reduce abnormal sound transmission. Start with education, hydration and reversal of a reversible precipitant when appropriate; address excessive/rapid weight loss when medically safe and avoid therapies that intentionally decongest or further open the tube if they aggravate symptoms. Evidence for specific medications is limited, so do not teach topical estrogen or other irritants as a universal evidence-based cure. Some patients benefit from saline-based measures or a tympanostomy tube, while persistent disabling disease can be considered for specialist procedures that add bulk/impedance or reduce patency (for example targeted filler/shim/plug-type approaches); outcomes vary and there is no single universally superior operation. Habitual sniffing may temporarily relieve autophony but can create chronic negative middle-ear pressure/retraction, so recognize that mixed patulous-plus-retraction phenotypes occur."
        ),
        "operate": (
            "PROCEDURAL PRINCIPLE: a patulous tube needs MORE resistance/closure, not dilation. Confirm the phenotype before any intervention. Options used in refractory disease include tympanostomy, augmentation around the cartilaginous valve, shims/plugs, or other techniques that narrow/disable pathologic patency; choice is anatomy- and experience-dependent and should be discussed with realistic expectations because durable symptom relief is variable. BALLOON EUSTACHIAN TUBE DILATION IS NOT A TREATMENT FOR PET and can create or worsen patulous symptoms."
        ),
        "teach": (
            "Chief/boards discriminator: PATULOUS ETD = TOO OPEN. Think BREATHING autophony + better supine/head-down + TM movement synchronous with respiration. Do not confuse generic fullness or voice autophony with proof of PET, and remember SSCD as a key mimic. Most important treatment trap: do NOT send a patulous patient down the obstructive-ETD balloon-dilation/decongestion pathway."
        ),
        "tags": ["patulous Eustachian tube", "PET", "autophony", "breathing autophony", "tympanic membrane respiratory movement", "long time-base tympanometry", "weight loss", "superior canal dehiscence differential"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — Eustachian-tube physiology and patulous/obstructive dysfunction framework",
            "K.J. Lee's Essential Otolaryngology, 12e — otologic physiology and autophony/third-window differential framework",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — PET as abnormal resting patency with autophony, respiratory TM motion, weight-loss/iatrogenic associations, and SSCD differential",
            "Schilder et al. Clin Otolaryngol. 2015;40:407-411 — consensus definition separating patulous from dilatory/baro-challenge ETD",
            "Poe. Diagnosis and management of the patulous eustachian tube. Otol Neurotol. 2007;28:668-677 — classic diagnostic/mechanistic framework and caution that voice autophony can overlap SSCD",
            "Kawamura et al. Clinical characteristics and diagnostic value of symptoms and objective findings in patulous eustachian tube: JOS criteria study. 2025 — breathing/voice autophony and objective TM flutter discrimination",
            "Yun et al. Application of Patient-operated Otoscope in Diagnosing Patulous Eustachian Tube Dysfunction. Otol Neurotol. 2026;47:599-603 — intermittent PET and confirmation of respiratory TM fluctuation",
        ],
    },
}


def apply_etd_rebuild_v319(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = ETD_REBUILD_V319.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v319"] = True
            module["semantic_role_v319"] = (
                "obstructive/dilatory and baro-challenge ETD diagnosis, middle-ear consequences, and pressure-restoring treatment"
                if key == "eustachian tube dysfunction"
                else "pathologic resting Eustachian-tube patency, autophony confirmation, mimic exclusion, and closure-restoring treatment"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
