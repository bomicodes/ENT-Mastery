"""v32.9 — source-grounded Eustachian Tube Dysfunction vs Patulous ET Dysfunction rebuild.

The parent ETD card owns obstructive/dilatory and baro-challenge failure-to-open physiology,
objective middle-ear consequences, and treatment selection. The patulous card owns failure
to-stay-closed physiology, autophony/respiratory transmission, objective confirmation, and
avoidance of obstructive-ET procedures. The pair is intentionally reciprocal rather than
redundant.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


ETD_REBUILD_V329 = {
    "eustachian tube dysfunction": {
        "recognize": (
            "Use this card for DILATORY/OBSTRUCTIVE or BARO-CHALLENGE Eustachian tube dysfunction: the tube fails to open adequately to ventilate the middle ear. Symptoms include pressure/fullness, popping, muffled hearing and pain or inability to equalize with altitude/diving. Chronic dilatory ETD should not be diagnosed from symptoms alone: look for concordant evidence of negative middle-ear pressure such as tympanic-membrane retraction and/or a type C tympanogram, or a disease consequence such as effusion. Baro-challenge ETD can have a normal examination and tympanogram at baseline because failure appears only during pressure change."
        ),
        "localize": (
            "Separate MECHANICAL obstruction from FUNCTIONAL failure to open. Intrinsic mucosal inflammation can narrow the cartilaginous tube; extrinsic disease includes adenoid or nasopharyngeal mass effect; palatal/tensor veli palatini dysfunction can impair active opening. The downstream chain is failure to ventilate -> negative middle-ear pressure -> retraction/effusion ->, in selected chronic ears, atelectasis/retraction-pocket disease and cholesteatoma risk. Persistent unilateral adult effusion or unilateral obstructive findings require nasopharyngeal evaluation rather than reflexively labeling the problem idiopathic ETD."
        ),
        "workup": (
            "Start with otoscopy/otomicroscopy, pneumatic assessment when useful, audiogram and tympanometry. Nasal endoscopy evaluates the nasopharyngeal orifice, adenoids, tumor and inflammatory disease; dynamic swallowing can add functional information. Do not treat a questionnaire score as proof of obstruction. For chronic dilatory ETD, symptoms should be reconciled with objective middle-ear findings; for baro-challenge disease, the history itself may be the key evidence when resting tests normalize. Exclude important mimics including temporomandibular pain, inner-ear/third-window disease and PATULOUS ETD before an irreversible or device-based intervention."
        ),
        "manage": (
            "Treat the CAUSE and the clinically important CONSEQUENCE. Acute URI-associated dysfunction often resolves. Manage clearly active sinonasal/allergic inflammation when present, but do not promise that empiric nasal medication cures mechanically confirmed ETD in the absence of corresponding nasal disease. Ventilation tubes bypass the dysfunctional tube and can relieve pressure/effusion consequences without restoring native ET physiology. Chronic retraction, atelectasis, effusion or cholesteatoma is managed according to the middle-ear pathology as well as the underlying ventilation problem."
        ),
        "operate": (
            "Balloon dilation of the cartilaginous Eustachian tube is a SELECTED treatment for appropriately confirmed obstructive/dilatory ETD after evaluation of alternatives and treatable causes; contemporary algorithms also include selected baro-challenge disease and chronic middle-ear sequelae. PATULOUS ETD is a contraindication because opening an already over-patent tube attacks the wrong physiology and may worsen symptoms. Tympanostomy tube placement remains a consequence-directed option in selected patients. Preoperative anatomy and institutional/device protocols guide whether temporal-bone imaging is needed before dilation, particularly when skull-base/carotid anatomy is a concern."
        ),
        "teach": (
            "Chief/boards discriminator: OBSTRUCTIVE ETD = TOO CLOSED / WILL NOT OPEN. Think pressure disequilibrium, negative middle-ear pressure, retracted TM or type C tympanogram, baro-challenge symptoms, and selected ventilation/BDET strategies. Do not merge this with patulous disease. If the complaint is prominent self-voice/self-breathing transmission and the drum moves with respiration, switch to the patulous card before doing anything designed to open the tube further."
        ),
        "tags": ["eustachian tube dysfunction", "dilatory ETD", "obstructive ETD", "baro-challenge ETD", "type C tympanogram", "tympanic membrane retraction", "balloon dilation", "nasopharyngoscopy"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — Eustachian tube physiology, middle-ear ventilation and obstructive dysfunction framework",
            "K.J. Lee's Essential Otolaryngology, 12e — Eustachian tube/middle-ear disease evaluation and differential framework",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — obstructive ETD symptoms, type C tympanometry and management framework",
            "Schilder et al., Clin Otolaryngol 2015 — international consensus on ETD definition, dilatory/baro-challenge/patulous types and diagnostic criteria",
            "AAO-HNSF Clinical Consensus Statement, 2019 — balloon dilation of the Eustachian tube patient-selection framework",
            "Sandoval et al., Otolaryngol Clin North Am 2026 — diagnostic algorithm and indications/contraindications for BDET in obstructive ETD",
        ],
    },
    "patulous eustachian tube dysfunction": {
        "recognize": (
            "Use this card for FAILURE OF CLOSURE: the cartilaginous Eustachian tube remains abnormally patent at rest. The signature complaint is AUTOPHONY, especially transmission of the patient's own BREATHING as well as voice, often with aural fullness. Symptoms may fluctuate, worsen upright or with exertion/dehydration, and improve supine or with head-dependent positioning as peritubal venous tissue engorges. Important associations include substantial weight loss and other states that reduce peritubal soft-tissue bulk; symptoms can also follow interventions that alter tubal mechanics."
        ),
        "localize": (
            "The problem is the opposite of obstructive ETD: nasopharyngeal sound/pressure is transmitted too freely into the middle ear because the normally closed cartilaginous valve is open. Otoscopy during quiet/deep nasal breathing may show tympanic-membrane excursion synchronous with respiration. A normal-looking drum at one clinic visit does not exclude PET because patency can be intermittent. Distinguish PET from superior semicircular canal dehiscence and other third-window syndromes: voice autophony occurs in both, but audible breathing and respiration-linked TM motion strongly favor PET; sound/pressure-induced vertigo, low-frequency air-bone gaps with inner-ear features, or other third-window signs should redirect the workup."
        ),
        "workup": (
            "Diagnosis requires characteristic symptoms PLUS objective support when possible. Examine the tympanic membrane while the patient breathes through one nostril with the mouth closed; long time-base tympanometry or other ET function testing can document respiration-synchronous pressure changes. Nasal endoscopy can assess an unusually open pharyngeal orifice and exclude other pathology. Positional improvement supports the diagnosis. Because intermittent PET may disappear during a scheduled visit, symptom-triggered video/otoscopy can be useful; a 2026 prospective study showed patient-operated otoscopy increased objective confirmation by capturing episodic TM fluttering. Obtain third-window imaging/physiology only when the clinical pattern warrants it rather than as routine PET testing."
        ),
        "manage": (
            "Begin by reversing aggravating factors when feasible: restore hydration, avoid unnecessary drying/decongestant strategies, and address excessive or rapid weight loss or another reversible cause. Counseling matters because symptoms can fluctuate and no single medical therapy is reliably effective for all patients. Selected patients may benefit from maneuvers that reduce acoustic transmission or increase peritubal bulk, but evidence across topical and procedural therapies is heterogeneous. Do not casually prescribe obsolete or weakly supported treatments as universal standard therapy."
        ),
        "operate": (
            "Refractory, objectively supported PET belongs in a specialist decision pathway. Procedural options described in contemporary literature include targeted augmentation/bulking near the pharyngeal valve, implants/plugs or other methods that reduce excessive patency, and in selected ears tympanic-membrane mass loading/cartilage approaches when the drum itself amplifies symptoms. Choice depends on the demonstrated mechanism and local expertise; there is no single universally superior operation. Crucial safety rule: BALLOON DILATION FOR OBSTRUCTIVE ETD IS CONTRAINDICATED IN PET because further opening can worsen the underlying failure-to-close physiology."
        ),
        "teach": (
            "Chief/boards discriminator: PATULOUS ETD = TOO OPEN / WILL NOT STAY CLOSED. Think voice + BREATHING autophony, positional fluctuation, and respiration-synchronous TM motion. Obstructive ETD instead produces pressure disequilibrium/negative middle-ear pressure and may be treated by ventilation or selected balloon dilation. PET must also be separated from superior canal dehiscence before intervention. The safest mental model is OPENING FAILURE versus CLOSURE FAILURE; confusing the two can produce exactly the wrong procedure."
        ),
        "tags": ["patulous eustachian tube", "autophony", "breathing autophony", "tympanic membrane respiration", "superior canal dehiscence", "long time-base tympanometry", "weight loss", "BDET contraindication"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — Eustachian tube valve physiology and patulous dysfunction framework",
            "K.J. Lee's Essential Otolaryngology, 12e — patulous ET differential and otologic physiology framework",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — autophony, respiration-linked TM movement, causes and SCDS differential",
            "Schilder et al., Clin Otolaryngol 2015 — international consensus distinguishing patulous from dilatory and baro-challenge ETD",
            "Ikeda, Auris Nasus Larynx 2024 — contemporary review of diagnosis and treatment of patulous Eustachian tube",
            "Yun et al., Otol Neurotol 2026 — symptom-triggered patient-operated otoscopy for intermittent PET confirmation",
        ],
    },
}


def apply_etd_rebuild_v329(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules:
            payload = ETD_REBUILD_V329.get(_norm(module.get("topic")))
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v329"] = True
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
