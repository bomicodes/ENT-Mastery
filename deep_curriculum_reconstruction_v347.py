"""v34.7 — readability hardening for free-flap monitoring and operative salvage.

Preserves the source-grounded v33.5 clinical content but changes the six Concept Hub stages
from dense prose into rapid-scan clinical blocks. The monitoring card reads as
PATTERN -> MEANING -> ACTION; the salvage card reads as CAUSE -> FIX -> ENDPOINT.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


FREE_FLAP_READABILITY_V347 = {
    "free flap monitoring compromise salvage": {
        "recognize": (
            "PATTERN • Venous compromise: swollen/tense/dusky flap, brisk dark bleeding. "
            "Arterial compromise: pale/cool flap, delayed or absent refill, little fresh bleeding. "
            "MEANING • Treat the flap as a vascular circuit, not a binary Doppler result; mixed patterns and buried flaps occur. "
            "ACTION • Establish the immediate postoperative baseline and trend color, temperature, turgor, capillary refill, dermal bleeding/pinprick when appropriate, and arterial/venous Doppler signals."
        ),
        "localize": (
            "CIRCUIT • Arterial inflow -> arterial anastomosis/pedicle -> flap microcirculation -> venous anastomosis/outflow. "
            "EXTRINSIC CHECK • Hematoma, tight closure/dressing, edema, dependent positioning, pedicle kink/twist, tracheostomy tie, or head-position change. "
            "PEARL • A strong arterial Doppler does NOT exclude venous obstruction; the artery may still transmit while the flap congests."
        ),
        "workup": (
            "CORE TEST • Serial clinical examination remains primary for an accessible flap. "
            "ADJUNCTS • Handheld/implantable Doppler and tissue-oxygen technologies should accelerate recognition, especially for buried flaps, not overrule a deteriorating exam. "
            "ESCALATION • Compare with the marked baseline signal, call the reconstructive surgeon, and mobilize the OR as soon as compromise is plausible. Do not spend the ischemic window on CT/CTA or prolonged serial observation merely to increase diagnostic certainty."
        ),
        "manage": (
            "NOW • Remove constrictive dressings/external pressure, normalize head and neck position, correct major hypotension/hypovolemia, and assess for expanding hematoma. "
            "IN PARALLEL • Prepare urgent takeback; bedside maneuvers are not a prolonged therapeutic trial. "
            "LIMIT • Leeches are a selected temporizing option when surgically correctable venous outflow cannot be established; they are not first-line treatment for a thrombosed free-flap pedicle."
        ),
        "operate": (
            "TAKEBACK TRIGGERS • New progressive congestion/pallor, loss or meaningful change of the expected Doppler signal, rapidly expanding neck hematoma, or concerning discordant monitoring data without a prompt benign explanation. "
            "THRESHOLD • Keep it especially low for buried flaps because surface examination is limited. "
            "HANDOFF • This monitoring card ends at the decision to explore; the separate salvage card owns pedicle/anastomotic rescue once the neck is reopened."
        ),
        "teach": (
            "CHIEF FRAME • 1) Is this INFLOW, OUTFLOW, or EXTRINSIC COMPRESSION? 2) Is the trend worsening? 3) What is delaying takeback? "
            "BOARD PEARLS • Venous congestion is often more visually obvious than arterial insufficiency. An arterial Doppler signal is not proof of flap viability. Monitoring exists to trigger timely rescue—not to make every test agree before acting."
        ),
    },
    "free flap monitoring and salvage": {
        "recognize": (
            "STARTING POINT • Exploration has already been triggered. The question is no longer whether the flap is abnormal. "
            "RESCUE QUESTIONS • What failed? Can durable inflow/outflow be restored quickly? Is the tissue still viable? "
            "BEFORE INCISION • Retrieve donor flap, artery/vein(s), recipient vessels, coupler/suture technique, vein-graft history, pedicle geometry, intraoperative problems, and the postoperative signal baseline."
        ),
        "localize": (
            "OPEN • Reopen enough to visualize the entire pedicle. "
            "FIRST FIX EXTRINSIC CAUSES • Evacuate hematoma, release constriction, untwist/kink the pedicle, and correct geometry. "
            "THEN TRACE THE CIRCUIT • Recipient arterial inflow -> arterial anastomosis -> pedicle/flap -> each venous pathway/anastomosis. Do not revise a visible anastomosis while leaving an occult kink, recipient-vessel problem, or compressive hematoma untouched."
        ),
        "workup": (
            "OPERATIVE SEQUENCE • 1) Confirm proximal recipient-vessel flow. 2) Inspect arterial anastomosis. 3) Inspect pedicle/flap. 4) Inspect each venous pathway. 5) Identify thrombus versus mechanical obstruction. 6) Reassess tissue perfusion after correction. "
            "IF THROMBOSED • Open as needed, remove clot, assess inflow/back-bleeding, irrigate per microsurgical practice, and cut back/revise to healthy vessel ends when necessary. Persistent poor outflow after a patent repair should trigger a search for propagated clot or microcirculatory failure."
        ),
        "manage": (
            "CAUSE -> FIX • Compression/kink -> release and re-site. Anastomotic thrombosis/technical failure -> thrombectomy plus revision, often to healthy intima. Poor recipient vessel -> select another recipient. Geometry requiring a bridge -> vein graft only when necessary. "
            "ADJUNCTS • Selective thrombolysis may be considered for persistent extensive flap-side thrombosis after mechanical correction; do not delay definitive revision to give a drug. Anticoagulation/antiplatelet decisions remain individualized to mechanism and bleeding risk."
        ),
        "operate": (
            "PROVE THE RESCUE • Appropriate warmth/color/turgor and bleeding return; Doppler signals are stable; artery and vein lie without tension/kink through intended head positions; hemostasis is secure without pedicle compression; the postoperative monitoring target is clearly marked. "
            "FAILURE PLAN • If the flap remains nonviable or rapidly rethromboses despite correctable problems being addressed, stop serial futile revisions. Debride nonviable tissue, protect carotid/hardware/aerodigestive tract, and choose a second free flap or regional/pedicled reconstruction based on defect, recipient vessels, physiology, and oncologic urgency."
        ),
        "teach": (
            "TAKEBACK ALGORITHM • OPEN EARLY -> RELIEVE EXTRINSIC CAUSES -> TRACE THE WHOLE PEDICLE -> RESTORE INFLOW/OUTFLOW -> REVISE THE THROMBOSED/FAULTY SEGMENT -> PROVE STABLE REPERFUSION -> BACKUP RECONSTRUCTION if viability cannot be restored. "
            "CHIEF PEARL • 'Takeback' is not the diagnosis or the operation; successful salvage requires finding WHY the circuit failed and correcting that mechanism."
        ),
    },
}


def apply_free_flap_readability_v347(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = FREE_FLAP_READABILITY_V347.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["free_flap_readability_v347"] = True
            module["layout_role_v347"] = (
                "rapid-scan Pattern/Meaning/Action monitoring layout"
                if key == "free flap monitoring compromise salvage"
                else "rapid-scan Cause/Fix/Endpoint operative salvage layout"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
