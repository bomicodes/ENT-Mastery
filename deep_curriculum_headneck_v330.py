"""v33.0 — source-grounded salvage surgery distinction rebuild.

The broader salvage card owns oncologic candidacy after prior RT/CRT: prove recurrence,
restage, decide whether an R0 resection is realistically achievable, and balance cure against
functional/morbidity cost. The chemoradiation-specific card owns execution in the hostile
previously irradiated field: tissue quality, exposure, vessels, closure/reconstruction, fistula
and wound-risk mitigation, and postoperative surveillance for complications.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


SALVAGE_REBUILD_V330 = {
    "salvage surgery after radiation chemoradiation": {
        "recognize": (
            "Use this card for the ONCOLOGIC SALVAGE DECISION after definitive radiation or chemoradiation. First distinguish persistent/residual disease, true recurrence after a disease-free interval, and a second primary; then ask whether disease is confined enough that complete macroscopic and microscopic resection is realistically achievable. Salvage is not simply 'operate because radiation failed.' It is a second curative-intent selection problem in a patient whose anatomy, function, and treatment reserve have already been altered by prior therapy. New progressive pain, ulceration/mass, cranial neuropathy, worsening dysphagia, new fixation or nodal disease after treatment should trigger recurrence evaluation rather than reflex attribution to fibrosis or radionecrosis."
        ),
        "localize": (
            "Map RECURRENCE GEOMETRY before discussing an operation: primary-site extent, deep-space/skull-base/prevertebral involvement, carotid relationship, laryngeal or mandibular invasion, nodal recurrence, dermal/soft-tissue extension, and distant metastasis. Previously treated tissue can obscure planes, so compare current cross-sectional imaging with pretreatment studies and the prior radiation field. Resectability is an anatomic AND biologic concept: a technically removable tumor may still be a poor salvage target when disease is multifocal, rapidly progressive, metastatic, or would require morbidity grossly disproportionate to the chance of durable control."
        ),
        "workup": (
            "Confirm suspected recurrence histologically when feasible and safe; do not commit to ablative salvage from PET avidity alone. Restage the entire patient with site-appropriate contrast imaging and distant-disease assessment, often including PET/CT when it will change management. Review the ORIGINAL pathology, operative notes, radiation dose/fields, systemic therapy, interval since treatment, prior complications and reconstruction. At multidisciplinary review explicitly assess probability of an R0 margin, carotid/skull-base involvement, nutritional status, pulmonary reserve, swallowing/airway function, performance status, wound-healing risk, reconstructive options, and the patient's priorities. A short disease-free interval, advanced recurrent burden, nodal/locoregional recurrence and inability to obtain clear margins are adverse prognostic signals; none should be converted into a simplistic single-number contraindication."
        ),
        "manage": (
            "For a fit patient with RESECTABLE locoregional recurrence and no competing disseminated disease, salvage surgery often provides the best available chance of cure and should be discussed in a multidisciplinary setting. If an R0 resection is not realistic or expected functional/morbidity cost is unacceptable, shift deliberately to another pathway: reirradiation in carefully selected patients, systemic/immunotherapy according to recurrent/metastatic HNSCC biomarkers and prior therapy, a clinical trial, or symptom-focused/palliative treatment. Do not let the availability of a large operation substitute for an oncologic benefit assessment."
        ),
        "operate": (
            "The operative plan begins BEFORE incision: define the oncologic resection required for negative margins, then design the airway, neck exposure, recipient-vessel strategy and reconstruction around that defect. Anticipate that fibrosis can make tumor boundaries, nerves, carotid dissection and mucosal closure less forgiving. Plan vascularized tissue when defect size, pharyngeal closure, exposed great vessels, irradiated soft tissue or dead space make primary closure unreliable; reconstruction is part of the salvage oncologic plan, not an afterthought. Frozen sections can answer focused margin questions but cannot rescue a fundamentally unresectable geometry. After pathology, reconsider additional therapy only through multidisciplinary risk/benefit review because prior RT/CRT constrains both reirradiation and systemic options."
        ),
        "teach": (
            "Chief/boards model: SALVAGE SELECTION = PROVE IT -> RESTAGE IT -> CAN YOU CLEAR IT? -> WHAT WILL THE CURE COST? -> CAN YOU RECONSTRUCT THE DEFECT? The most important preoperative endpoint is not 'technically operable'; it is a plausible R0 resection with a functional/reconstructive plan and a benefit that matches the patient's goals. Keep this card separate from the chemoradiation-specific execution card, which focuses on surviving the hostile irradiated field once the decision to operate has already been made."
        ),
        "tags": ["salvage surgery", "recurrent HNSCC", "persistent disease", "resectability", "R0 margin", "prior radiation", "chemoradiation", "multidisciplinary selection"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent/persistent HNSCC, salvage treatment and reconstructive planning framework",
            "K.J. Lee's Essential Otolaryngology, 12e — recurrence recognition, biopsy confirmation, post-treatment imaging and salvage laryngeal/H&N principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — residual/recurrent H&N cancer pathways and salvage surgery after failed RT/CRT",
            "Williamson et al., J Natl Cancer Inst 2025 — multidisciplinary evidence-based consensus statements for salvage surgery in recurrent head and neck cancer",
            "Williamson et al., Otolaryngol Clin North Am 2026 — contemporary surgery framework for recurrent head and neck cancer",
            "NCCN Head and Neck Cancers, Version 2.2025 — multidisciplinary recurrent/metastatic treatment framework",
        ],
    },
    "salvage surgery after chemoradiation": {
        "recognize": (
            "Use this card AFTER the patient has already been selected for salvage surgery to manage the PREVIOUSLY CHEMORADIATED FIELD. Radiation/CRT changes the operation: fibrosis obscures planes, microvascular and mucosal healing are impaired, soft tissue may be thin or noncompliant, edema can complicate airway assessment, and prior infection/chondroradionecrosis can coexist with recurrent tumor. The practical question is no longer 'should this recurrence be salvaged?' but 'how do I obtain oncologic clearance and a durable closure without carotid exposure, fistula, wound breakdown or reconstructive failure?'"
        ),
        "localize": (
            "Inventory the HOSTILE FIELD, not just the tumor. Mark irradiated skin and mucosa, prior neck-dissection planes, tracheostomy/stoma, pharyngeal or oral communication, exposed or threatened carotid, plate/bone problems, prior flap pedicles, and usable recipient vessels outside or at the edge of the radiation field. For salvage laryngectomy/laryngopharyngectomy, define how much pharyngeal mucosa will remain and whether primary closure would be tight; circumferential or near-circumferential defects require planned conduit reconstruction. Distinguish tumor-related cartilage destruction from radionecrosis when possible, but never delay definitive evaluation of a suspicious progressive lesion merely because treatment injury is plausible."
        ),
        "workup": (
            "Build an OPERATIVE RESCUE PLAN before surgery: review prior radiation dose map if available, prior neck operations and flap/vessel history; assess nutrition, anemia, thyroid function and modifiable wound risks; obtain speech/swallow evaluation when functional outcomes or TEP decisions matter. Coordinate reconstructive surgery early for large mucosal defects, circumferential pharynx, vessel coverage, poor local tissue or anticipated dead space. In a vessel-depleted neck, identify alternative recipient-vessel options before flap harvest rather than discovering the problem after ablation. Counsel specifically about pharyngocutaneous fistula, wound infection/dehiscence, bleeding/carotid catastrophe, dysphagia/stricture, flap compromise, prolonged feeding access and the possibility of additional reconstruction."
        ),
        "manage": (
            "Treat perioperative optimization as part of salvage care, not generic pre-op housekeeping. Correct meaningful malnutrition/dehydration and other reversible physiologic deficits, plan airway and feeding strategy, and involve SLP/nutrition/reconstruction teams early. After surgery, maintain a low threshold to investigate salivary leak, deep infection, progressive neck erythema, sentinel bleeding or exposed great vessels. A fistula is not merely a skin problem in an irradiated neck: it can contaminate the carotid and threaten catastrophic hemorrhage. Conversely, not every small controlled leak requires immediate major reoperation; management depends on defect, vascular exposure, sepsis, tissue viability and reconstructive stability."
        ),
        "operate": (
            "Execute salvage with WIDE AWARENESS OF TISSUE QUALITY: preserve viable skin/mucosa when oncologically safe, avoid devascularizing already marginal flaps, obtain hemostasis without unnecessary tissue injury, and achieve a tension-free, well-vascularized separation between aerodigestive contents and critical vessels. Use regional or free vascularized tissue when the defect or field demands it; the goal is replacement/reinforcement with healthy blood supply, dead-space obliteration and vessel protection, not simply 'put in a flap because this is salvage.' In salvage total laryngectomy, prophylactic vascularized reinforcement may reduce fistula risk in selected high-risk patients, but technique and indication are defect- and patient-specific rather than a universal one-flap rule. If recipient vessels are compromised, move deliberately to healthy vessels, vein grafts or alternate configurations according to reconstructive expertise."
        ),
        "teach": (
            "Chief/boards model: CHEMORADIATED-FIELD SALVAGE = ONCOLOGIC RESECTION + VASCULARIZED HEALING STRATEGY. Expect distorted planes, fistula and wound risk, vessel problems and functional morbidity. The parent salvage card decides WHETHER an R0 salvage operation is worth doing; this card decides HOW to perform and reconstruct that operation safely in tissue that has already paid the biologic price of chemoradiation."
        ),
        "tags": ["salvage after chemoradiation", "irradiated neck", "pharyngocutaneous fistula", "salvage laryngectomy", "vascularized tissue", "vessel-depleted neck", "carotid protection", "reconstruction"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — salvage laryngopharyngeal surgery, irradiated-field healing and reconstructive principles",
            "K.J. Lee's Essential Otolaryngology, 12e — increased fistula/wound risk after prior radiation and vascularized reconstruction concepts",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — salvage laryngectomy after organ-preservation failure and H&N reconstruction framework",
            "Williamson et al., J Natl Cancer Inst 2025 — multidisciplinary perioperative consensus for recurrent H&N salvage surgery",
            "Williamson et al., Otolaryngol Clin North Am 2026 — contemporary technical considerations in recurrent H&N cancer surgery",
            "Salvage surgery after RT/CRT meta-analytic literature — high fistula/wound burden and importance of complete resection/reconstructive planning",
        ],
    },
}


def apply_salvage_rebuild_v330(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules:
            payload = SALVAGE_REBUILD_V330.get(_norm(module.get("topic")))
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v330"] = True
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
