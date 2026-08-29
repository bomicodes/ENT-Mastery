"""v28.9 — source-grounded free-flap Concept Hub rebuild.

The duplicate audit flags two near-identical Head & Neck Oncology cards. This patch gives
those cards different clinical jobs instead of letting both become generic flap-failure
summaries:

1) Free-Flap Monitoring / Compromise / Salvage = postoperative surveillance and early
   recognition/localization of compromise from bedside findings through the take-back call.
2) Free Flap Monitoring and Salvage = chief-level operative rescue: re-exploration,
   anastomotic/thrombotic troubleshooting, revision, vein graft/alternate recipient strategy,
   and what to do when the flap cannot be salvaged.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


FREE_FLAP_REBUILD_V289 = {
    "free flap monitoring compromise salvage": {
        "recognize": (
            "Recognize FREE-FLAP COMPROMISE as a TIME-CRITICAL postoperative diagnosis. The resident should know the flap's baseline immediately after inset and again at handoff: color, temperature, capillary refill, turgor, pinprick character when used, and the expected arterial/venous Doppler signal. A healthy skin paddle is typically warm and appropriately colored with brisk but not instantaneous refill. Venous congestion tends toward a swollen, dark or violaceous flap with brisk dark bleeding; arterial insufficiency tends toward a pale, cool, poorly perfused flap with delayed or absent bleeding. Do not wait for complete flap necrosis or loss of every signal before escalating a meaningful change from baseline."
        ),
        "localize": (
            "Localize the problem as ARTERIAL INFLOW, VENOUS OUTFLOW, PEDICLE MECHANICS, HEMATOMA/COMPRESSION, or a NONVASCULAR mimic. Arterial inflow problems produce pallor, coolness, slow refill, absent/weak arterial signal, and little pinprick bleeding. Venous outflow obstruction produces congestion, swelling, rapid refill, dark brisk blood, and a venous signal that may disappear or become abnormal. Pedicle kinking, torsion, neck position, tight closure, external compression, or hematoma can compromise either side. Systemic hypotension, hypothermia, vasoconstriction, anemia, or monitoring-device artifact can mimic compromise, so assess the patient and the flap together—but a plausible systemic explanation must not become an excuse to delay exploration of a deteriorating flap."
        ),
        "workup": (
            "Evaluate suspected compromise at the BEDSIDE first because unnecessary imaging can waste the salvage window. Compare directly with prior documented exams; inspect the paddle, palpate turgor/temperature, check capillary refill and Doppler signals, and perform pinprick testing when the reconstructive team uses it. Inspect the neck for expanding hematoma or excessive tension and review blood pressure, oxygenation, temperature, hemoglobin, and recent neck positioning. An implantable Doppler, near-infrared spectroscopy, or other adjunct may help depending on the flap and institution, but no device replaces a concerning clinical examination. If findings remain suspicious after immediately correcting obvious reversible external factors, call the reconstructive attending and mobilize the OR rather than ordering CT to prove vascular compromise."
        ),
        "manage": (
            "Manage the first minutes with PARALLEL RESCUE: notify the microvascular team, stop external compression, place the head/neck in a neutral non-kinking position, correct significant hypotension/hypoxia/hypothermia, and prepare for urgent re-exploration. Do not repeatedly massage, needle, or observe a progressively abnormal flap while waiting for a better Doppler. A small superficial hematoma without flap effect is different from a tense neck or hematoma altering pedicle geometry; the latter requires rapid decompression and operative control. Monitoring intensity is greatest early after surgery because vascular complications cluster in the early postoperative period, and every handoff should state the flap's current exam and the specific trigger for escalation."
        ),
        "operate": (
            "The operative threshold is CLINICAL SUSPICION OF A CORRECTABLE VASCULAR PROBLEM, not proof of irreversible failure. Return urgently for a deteriorating flap with convincing arterial/venous signs, persistent loss of a previously reliable signal, an expanding hematoma threatening the pedicle, or worsening congestion despite correction of external causes. In the OR, the reconstructive surgeon inspects the entire pedicle and inset for compression, twist, tension, thrombosis, or anastomotic failure before deciding on revision. This card stops at the decision to re-explore; detailed thrombectomy, anastomotic revision, alternate recipient vessels, vein grafting, and replacement-flap strategy belong in the companion operative-salvage card."
        ),
        "teach": (
            "Boards/chief surveillance framework: KNOW BASELINE → RECOGNIZE CHANGE → LOCALIZE INFLOW VS OUTFLOW VS MECHANICAL → CORRECT EXTERNAL FACTORS WHILE CALLING → TAKE BACK EARLY WHEN CONCERN PERSISTS. Clinical examination remains the foundation of monitoring even when technology is added. Venous congestion is not 'watch and wait,' an isolated device alarm must be checked against the flap, and a normal-looking external paddle does not completely exclude compromise of a buried component. The resident's highest-value action is shortening the time from a credible abnormal exam to definitive assessment by the reconstructive team."
        ),
        "tags": [
            "free flap monitoring", "flap compromise", "venous congestion", "arterial insufficiency",
            "microvascular free flap", "Doppler", "pinprick", "hematoma", "takeback", "flap surveillance"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — head-and-neck free-tissue transfer, postoperative flap monitoring, vascular compromise, and salvage principles",
            "K.J. Lee's Essential Otolaryngology, 12e — microvascular reconstruction, flap assessment, and postoperative complications",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — practical free-flap monitoring and early compromise recognition",
            "ERAS Society consensus recommendations for major head-and-neck cancer surgery with free-flap reconstruction — structured postoperative care and flap surveillance within an enhanced-recovery pathway",
            "Contemporary head-and-neck microvascular monitoring literature — clinical examination as the core surveillance method with Doppler/implantable monitoring as adjuncts and improved salvage with prompt recognition/re-exploration",
        ],
    },
    "free flap monitoring and salvage": {
        "recognize": (
            "Recognize OPERATIVE FLAP SALVAGE as a different problem from routine monitoring: once compromise is sufficiently likely to justify takeback, the chief-level task becomes identifying the correctable cause quickly and restoring durable perfusion. The clock matters because prolonged ischemia or venous congestion progressively injures the flap even if flow is later restored. Salvage is most plausible when deterioration is recognized early and the cause is mechanical or thrombotic and technically reversible. A flap that is globally nonviable after prolonged compromise requires a replacement/reconstruction plan rather than endless revision attempts."
        ),
        "localize": (
            "Localize failure systematically in the OR from RECIPIENT VESSEL → ANASTOMOSIS → PEDICLE → FLAP. Look for arterial thrombosis/spasm or poor inflow, venous thrombosis/outflow obstruction, anastomotic narrowing or leak, pedicle kink/twist/tension, compression beneath the inset or tunnel, hematoma, or a recipient-vessel problem in a previously treated neck. Determine whether the problem is proximal to the anastomosis, at the anastomosis, within the pedicle, or intrinsic to the flap. This sequence prevents the common error of revising the visible anastomosis while missing a twisted pedicle or distal outflow problem."
        ),
        "workup": (
            "Before and during takeback, reconstruct the operative map: flap type, arterial and venous recipient vessels, coupler/anastomosis configuration, ischemia time, prior neck dissection/radiation, anticoagulation issues, and exactly when the examination changed. Intraoperatively assess recipient-vessel pulsatility/inflow, venous drainage, pedicle geometry, and the anastomoses directly. Use magnification and targeted thrombectomy/revision rather than broad traumatic exploration. If recurrent thrombosis occurs after technically satisfactory revision, reconsider vessel quality, pedicle orientation, hypercoagulable/systemic contributors, and whether an alternate recipient vessel or interposition graft is safer than repeating the same failing configuration."
        ),
        "manage": (
            "Choose the rescue maneuver from the mechanism. Release a kink, twist, tight tunnel, or compressive inset; evacuate hematoma and control its source; revise a narrowed or thrombosed arterial/venous anastomosis; perform thrombectomy and irrigate according to the reconstructive team's protocol; and change recipient vessel or venous outflow when the original vessel is unreliable. Pharmacologic antithrombotic or thrombolytic adjuncts are institution- and case-dependent and do not substitute for correcting the mechanical/anastomotic cause. After flow is restored, reassess the entire flap—not just the Doppler—and revise the inset so the rescued pedicle is not returned to the geometry that caused failure."
        ),
        "operate": (
            "Operate with an ESCALATION PLAN. If direct anastomotic revision restores strong inflow/outflow, confirm flap reperfusion and a tension-free pedicle before closure. If recipient vessels are poor or repeatedly thrombose, move to a better vessel, consider a vein graft or alternate recipient strategy when necessary, and account for the vessel-depleted neck created by prior dissection/radiation. If the flap is unsalvageable, debride nonviable tissue and choose the safest secondary reconstruction for the defect—another free flap, regional pedicled flap, delayed reconstruction, or temporary wound strategy depending on exposed carotid, pharyngeal communication, infection, patient stability, and oncologic needs. The endpoint is a viable reconstruction that safely separates critical structures, not preservation of the original flap at any cost."
        ),
        "teach": (
            "Chief/boards operative framework: OPEN EARLY → TRACE THE WHOLE PEDICLE → FIX THE CAUSE → CONFIRM GLOBAL REPERFUSION → CHANGE THE GEOMETRY THAT FAILED → HAVE A PLAN B. Arterial and venous thrombosis are consequences as well as diagnoses: always ask why the vessel thrombosed. A technically perfect redo anastomosis will fail again if the pedicle remains kinked or the recipient vein is inadequate. When salvage fails, protect airway, pharynx, carotid, and dead space with the most reliable alternative reconstruction rather than persisting with futile microvascular revision. This card owns operative rescue; the companion monitoring card owns bedside recognition and the decision to take back."
        ),
        "tags": [
            "free flap salvage", "microvascular takeback", "thrombectomy", "anastomotic revision",
            "venous thrombosis", "arterial thrombosis", "recipient vessel", "vein graft",
            "vessel depleted neck", "second free flap", "regional flap"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — microvascular thrombosis, re-exploration, anastomotic revision, recipient-vessel selection, and failed-flap reconstruction",
            "K.J. Lee's Essential Otolaryngology, 12e — free-tissue transfer complications and operative salvage concepts",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — practical microvascular complication and salvage pearls",
            "Contemporary systematic reviews/large head-and-neck free-flap series — early re-exploration as the major modifiable determinant of salvage and venous/arterial thrombosis as common technical failure modes",
            "Vessel-depleted-neck reconstructive literature — alternate recipient vessels, interposition grafts, regional flaps, and second free-flap strategies when conventional cervical recipient vessels are unavailable",
        ],
    },
}


def apply_headneck_free_flap_rebuild_v289(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = FREE_FLAP_REBUILD_V289.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v289"] = True
        module["semantic_role_v289"] = (
            "postoperative surveillance and takeback threshold"
            if _norm(module.get("topic")) == "free flap monitoring compromise salvage"
            else "operative microvascular rescue and replacement strategy"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
