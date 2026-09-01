"""v28.2 — post-thyroidectomy neck hematoma airway rescue.

Adds an executable resident/chief emergency sequence to the existing thyroid OR Tomorrow
cards without replacing the v23.12 planning, RLN, calcium, or parathyroid material.
Grounded in the DAS/BAETS/ENT-UK multidisciplinary post-thyroid hematoma guideline.
"""

TARGETS = (
    "thyroid-lobectomy",
    "total-thyroidectomy",
    "reop-thyroid",
)

RESCUE = [
    "POST-THYROID HEMATOMA COMMITMENT POINT: new neck swelling or tightness, dysphagia/discomfort, anxiety/agitation, tachypnea or difficulty breathing, oxygen desaturation, or stridor after thyroid surgery should trigger immediate concern for a compressive hematoma; stridor is a late sign. Give supplemental oxygen, sit the patient head-up when feasible, call senior surgical and anesthesia help immediately, bring difficult-airway/front-of-neck-airway capability to the bedside, and evaluate airway patency while the response is mobilizing. Do not let a functioning drain, an initially modest external swelling, or a plan for routine imaging falsely reassure you when the clinical trajectory suggests compression.",
    "AIRWAY-COMPROMISE BAILOUT — SCOOP: if suspected post-thyroid hematoma is causing airway compromise or rapidly progressive deterioration, do not wait for transport or imaging before decompressing the neck. Systematically open the wound at bedside through the constricting layers: Skin exposure -> Cut sutures/clips -> Open skin -> Open the superficial and deep muscle/strap layers -> Pack the opened wound while maintaining decompression and preparing definitive control. Opening only the skin is inadequate if the deeper closure remains constricting. This is emergency decompression, not definitive hemostasis; once stabilized, return urgently to the operating room to evacuate clot, identify and control the bleeding source, irrigate/check hemostasis, and reassess the airway before reclosure.",
    "RESCUE ESCALATION: if wound opening/hematoma evacuation does not promptly stabilize oxygenation or airway patency, proceed to tracheal intubation with senior anesthesia while recognizing that laryngeal edema and distorted anatomy can make intubation difficult; have emergency front-of-neck airway equipment immediately available. Treat dexamethasone or tranexamic acid, when used in a stable patient, as adjuncts rather than substitutes for decompression or airway control. After rescue, continue high-acuity observation for rebleeding, airway edema and the underlying bleeding cause rather than assuming bedside decompression ended the event.",
]

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — thyroid surgery anatomy and postoperative complication principles",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — thyroid surgery and postoperative airway/bleeding principles",
    "Pasha: Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — thyroidectomy complications and emergency management framework",
    "Iliff HA et al. Management of haematoma after thyroid surgery: systematic review and multidisciplinary consensus guidelines from the Difficult Airway Society, BAETS and ENT-UK. Anaesthesia. 2022;77:82-95. doi:10.1111/anae.15585",
]


def _find(registry, slug):
    if slug in (registry or {}):
        return slug, registry[slug]
    needle = slug.replace("-", " ")
    for key, op in (registry or {}).items():
        hay = (str(key) + " " + str((op or {}).get("title", ""))).lower().replace("-", " ")
        if all(token in hay for token in needle.split() if token not in {"reop"}):
            if slug == "reop-thyroid" and not any(t in hay for t in ("reop", "reoperative", "completion")):
                continue
            return key, op
    return None, None


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.append(text)
            changed = True
    return out, changed


def apply_or_thyroid_hematoma_rescue_v282(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _find(registry, target)
        if not op:
            missing.append(target)
            continue
        op["postop"], c1 = _append_unique(op.get("postop"), RESCUE)
        op["sources"], c2 = _append_unique(op.get("sources"), SOURCES)
        op["thyroid_hematoma_rescue_v282"] = True
        op["thyroid_hematoma_semantic_role_v282"] = "recognition -> immediate oxygen/help -> bedside SCOOP decompression for airway compromise -> airway escalation -> definitive OR hemostasis"
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "resolved": resolved, "missing": missing}
