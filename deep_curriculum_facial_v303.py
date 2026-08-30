"""v30.3 — source-grounded facial reanimation semantic-boundary rebuild.

Separates three clinically different jobs:
1) Facial Nerve Reanimation = reconstruction strategy/timing and option selection.
2) Dynamic Facial Reanimation = how movement is restored with viable native muscle,
   nerve transfer, regional muscle, or free functional muscle transfer.
3) Static Facial Reanimation = immediate support/protection when movement restoration is
   impossible, undesirable, delayed, or insufficient.
"""

import re

DOMAIN = "Facial Plastics / Trauma"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


REANIMATION_V303 = {
    "facial nerve reanimation": {
        "recognize": "Treat facial reanimation as a TIMING + MOTOR-UNIT + GOAL problem, not as a menu of procedures. First distinguish flaccid paralysis from post-paralytic synkinesis, determine whether meaningful spontaneous recovery remains possible, and identify the functions that matter now: corneal protection, oral competence, nasal valve support, resting symmetry, and smile. Acute repairable transection, recent denervation with viable native mimetic muscle, and long-standing paralysis with irreversible motor-endplate loss require different reconstructive pathways.",
        "localize": "Localize the lesion and inventory the reconstructive system: is a proximal facial nerve stump available, are distal facial branches intact, is native facial musculature still viable, and are donor motor nerves usable? Map eye closure, brow position, alar collapse, oral commissure vector, lower-lip depressor function, and smile excursion. Duration of denervation matters because a technically intact distal nerve is not useful after the native motor endplates have irreversibly atrophied; conversely, abandoning viable native muscle too early can commit the patient to unnecessarily complex muscle transfer.",
        "workup": "Reconstruct the timeline from onset/injury and the probability of recovery before operating. Document standardized facial function at rest and with movement, ocular surface risk, corneal sensation/Bell phenomenon, oral competence, and synkinesis. Review prior tumor or parotid/skull-base surgery, radiation, nerve sacrifice and pathology. Use electrodiagnostic testing selectively when it will clarify residual motor-unit viability or prognosis; imaging is driven by the cause of paralysis rather than routinely by the reanimation operation itself. The key preoperative question is whether the patient still has a reinnervatable native facial muscle target.",
        "manage": "Choose the least burdensome strategy that can meet the patient's functional goals. When a repairable facial nerve is available, primary tension-free neurorrhaphy or interposition grafting best preserves the native pathway. When the proximal facial nerve is unavailable but distal branches and native muscle remain viable, nerve transfer (commonly masseteric-to-facial, partial hypoglossal-to-facial, and/or cross-facial input) can reinnervate the face. With long-standing denervation and nonviable native muscle, restore movement with regional muscle transfer or free functional muscle transfer. Static support and ocular protection can be used at any stage as definitive treatment or as an adjunct while dynamic recovery matures.",
        "operate": "Plan the operation around what tissue can still generate motion. Acute nerve repair requires atraumatic, tension-free alignment; grafting bridges a gap when direct coaptation would place the repair under tension. Nerve transfer requires a healthy donor motor source and viable distal facial target. Long-standing flaccid paralysis shifts toward temporalis-based regional transfer or free functional muscle transfer, most commonly gracilis. Combine procedures by subunit when necessary: dynamic smile reconstruction does not automatically correct lagophthalmos, lower-lid ectropion, nasal valve collapse, or lower-lip asymmetry. Protect the eye independently of the smile plan.",
        "teach": "Chief framework: NERVE AVAILABLE? → MUSCLE VIABLE? → WHAT FUNCTION NEEDS RESTORATION? If proximal + distal facial nerve are available, repair/graft. If the proximal facial source is lost but native mimetic muscle is viable, provide a new motor source. If native muscle is no longer viable, bring or transpose muscle. Static procedures support tissue but do not create active movement. Synkinesis is a different physiology—misdirected reinnervation—and should not be taught as if it were chronic flaccid paralysis.",
        "tags": ["facial nerve reanimation", "facial paralysis", "timing", "motor endplate", "nerve repair", "nerve transfer", "free functional muscle transfer", "static support"],
    },
    "dynamic facial reanimation": {
        "recognize": "Dynamic facial reanimation specifically means restoring ACTIVE MOVEMENT. It should therefore begin after the broader reconstruction decision has established that motion is a realistic and worthwhile goal. Separate two situations: viable native mimetic muscle that can still be reinnervated versus chronic denervation in which a new contractile unit is required. The desired outcome is not merely elevation of the oral commissure at rest, but excursion, vector, timing, and—when possible—spontaneity of smile.",
        "localize": "For nerve-based reconstruction, identify usable distal facial branches and donor motor sources. The masseteric nerve provides a strong, nearby V3 motor source with relatively rapid reinnervation but initially produces a bite-activated smile; a cross-face nerve graft can provide contralateral facial input and the best pathway toward spontaneous emotional smile but requires sufficient axonal input and time. Partial hypoglossal strategies can add resting tone and movement while minimizing tongue morbidity. When native facial muscle is nonviable, define the desired smile vector and recipient vessels/nerves for regional or free muscle transfer.",
        "workup": "Document denervation duration, residual movement, synkinesis, donor cranial-nerve function, and muscle viability before selecting a dynamic method. Confirm that CN V motor function is intact before masseteric transfer and assess tongue function before hypoglossal-based reconstruction. For free functional muscle transfer, assess recipient facial vessels, prior radiation/neck dissection, donor-site considerations, and the intended neural source. In children and selected adults, a staged cross-face nerve graft followed by gracilis can prioritize spontaneity; a masseteric-powered gracilis prioritizes reliable axonal input and powerful excursion.",
        "manage": "Match technique to the biologic substrate. With viable native facial muscle and unavailable proximal VII, use nerve transfer rather than importing new muscle. Masseteric-to-facial transfer offers robust excursion and relatively fast recovery; cross-face input offers the possibility of spontaneous smile but weaker/longer axonal regeneration; dual innervation can combine advantages in selected patients. Once native motor endplates are no longer useful, choose regional temporalis transfer or free functional muscle transfer. Postoperative neuromuscular retraining is part of the treatment because the brain must learn and refine the new motor source.",
        "operate": "Dynamic operations are vector- and tension-sensitive. Nerve coaptations must be tension-free and atraumatic. In free gracilis transfer, orient the muscle along the desired zygomatic-to-oral-commissure smile vector, secure stable fixation, perform reliable microvascular anastomoses, and coapt the motor nerve to the chosen donor source. In temporalis transfer, preserve a functional muscle/tendon unit and recreate a favorable oral-commissure vector while avoiding excessive bulk. Do not judge a nerve-transfer result immediately: axonal regeneration and cortical adaptation require months.",
        "teach": "Boards distinction: MASSETERIC = strong/reliable/fast but initially volitional bite-smile; CROSS-FACE = contralateral VII input with spontaneity potential but longer regeneration and less axonal power; GRACILIS = new motor unit for long-standing paralysis when native mimetic muscle is no longer viable. A nerve transfer cannot animate a face whose target motor endplates have disappeared. Dynamic reconstruction restores motion; resting symmetry alone belongs to static reconstruction.",
        "tags": ["dynamic facial reanimation", "masseteric facial nerve transfer", "cross-face nerve graft", "hypoglossal facial transfer", "gracilis free flap", "temporalis transfer", "spontaneous smile"],
    },
    "static facial reanimation": {
        "recognize": "Static facial reanimation restores SUPPORT, PROTECTION, and RESTING SYMMETRY without attempting to create active contraction. It is particularly valuable when dynamic reinnervation is not feasible, when medical status or prognosis makes a long recovery unattractive, after failed dynamic reconstruction, or as an immediate adjunct while nerve/muscle reanimation matures. Static treatment is subunit-specific: cornea, brow/lid, nasal valve, oral commissure, and lower lip have different functional problems.",
        "localize": "Localize the gravitational and soft-tissue failure rather than re-localizing the facial nerve lesion. At the eye, identify lagophthalmos, brow ptosis, lower-lid ectropion/retraction, Bell phenomenon, corneal sensation, and exposure. At the midface, assess alar collapse and loss of nasolabial support. At the mouth, determine commissure descent, oral incompetence, drooling, speech/articulation impairment, and lower-lip asymmetry. The vector of suspension should reproduce the missing support rather than simply pulling tissue laterally.",
        "workup": "Prioritize ocular safety first. Document corneal exposure and sensation, then photograph/measure facial position at rest and during attempted movement. For alar obstruction, distinguish paralytic nasal-valve collapse from pre-existing septal or structural obstruction. For oral suspension, determine the desired commissure vector while the patient is upright. Assess wound-healing risk, prior radiation and expected longevity of implanted/alloplastic materials versus autologous fascia. Static procedures can be planned independently from whether a future dynamic operation will also be performed.",
        "manage": "Protect the cornea with lubrication and moisture strategies immediately, then use upper-lid loading and lower-lid tightening/repositioning when exposure persists. Brow procedures address superior visual-field and symmetry problems. Fascia lata or other suspension can elevate the oral commissure, support the nasolabial fold, and lateralize a collapsed nasal ala; lower-lip balancing procedures address oral incompetence and asymmetry. Static support is not an inferior fallback: it provides immediate function, can be definitive in selected patients, and commonly complements dynamic reanimation.",
        "operate": "For suspension, establish a strong fixed point—often temporal/deep fascial support—and set the graft along the functional vector to the oral commissure, nasolabial region, or ala without overcorrection that distorts the lip or airway. Autologous fascia lata provides durable biologic support but adds donor-site morbidity; alloplastic materials avoid harvest but carry infection/extrusion considerations. Eyelid loading should restore closure without unacceptable ptosis, and lower-lid tightening must restore globe apposition. Reassess the patient upright when possible because gravitational symmetry differs from the supine operative view.",
        "teach": "Chief distinction: STATIC = position/support now; DYNAMIC = contraction later. Static options include eyelid loading/lid tightening, brow repositioning, fascia-lata suspension of the oral commissure or nasal ala, and lower-lip balancing. They are appropriate for poor dynamic candidates, limited life expectancy, failed dynamic reconstruction, or as adjuncts. Do not promise a spontaneous smile from a sling, and do not postpone corneal protection while waiting for a nerve transfer to recover.",
        "tags": ["static facial reanimation", "facial suspension", "fascia lata sling", "eyelid weight", "lower lid tightening", "nasal valve support", "oral competence"],
    },
}

SOURCE_BASIS = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — facial paralysis and contemporary facial reanimation: timing, nerve repair/transfer, static support, regional and free functional muscle transfer",
    "K.J. Lee's Essential Otolaryngology, 12e — Facial Nerve Paralysis: static smile restoration, nerve transfer, temporalis transfer, cross-face grafting, and gracilis free muscle transfer",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — facial nerve injury evaluation and facial reanimation principles",
    "Operative Otolaryngology—Head and Neck Surgery, 3e — Facial Reanimation: duration-based selection, static suspension, nerve substitution, and free muscle transfer",
]


def apply_facial_reanimation_rebuild_v303(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = REANIMATION_V303.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(SOURCE_BASIS)
        module["source_grounded_v303"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
