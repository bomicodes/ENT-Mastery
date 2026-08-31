"""v32.3 — source-grounded free-flap monitoring versus operative salvage separation.

The duplicate audit contains two full-containment free-flap cards. This patch preserves both
but assigns different resident/chief jobs: the first is postoperative SURVEILLANCE +
RECOGNITION of vascular compromise; the second is URGENT TAKE-BACK + SALVAGE strategy.
The overlap is intentional only at the escalation boundary: credible compromise triggers
immediate reconstructive-team assessment and should not be delayed by nonessential imaging.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


FREE_FLAP_REBUILD_V323 = {
    "free flap monitoring compromise salvage": {
        "recognize": (
            "Use this card for POSTOPERATIVE FLAP SURVEILLANCE AND RECOGNITION—not for the technical take-back operation. Establish a documented baseline immediately after inset and follow serial clinical change. A healthy accessible skin/mucosal paddle is warm and appropriately colored/turgid with prompt capillary refill, reproducible Doppler signal, and bright-red dermal bleeding when pinprick is used. VENOUS CONGESTION tends toward dusky/blue-purple color, swelling/turgor, brisk refill and brisk dark bleeding. ARTERIAL INSUFFICIENCY tends toward pallor/coolness, poor or absent refill, weak/absent arterial signal and little or no bright-red pinprick bleeding. Trend matters more than one isolated finding."
        ),
        "localize": (
            "Translate the bedside phenotype into a vascular problem. Venous compromise = outflow obstruction from venous thrombosis, pedicle kink/twist, compression, tight inset/closure, hematoma, or recipient-vein problem. Arterial compromise = inflow failure from arterial thrombosis, spasm, kink, compression, anastomotic problem, or systemic low-flow state. A flap can have an audible arterial signal despite clinically important venous obstruction, so Doppler is an adjunct rather than a substitute for examination. For buried flaps, know what is actually being monitored: an externalized/sentinel paddle when present, implantable Doppler, tissue oximetry or other institutional adjuncts; a reassuring device should not overrule a deteriorating patient/flap."
        ),
        "workup": (
            "Monitoring is a serial clinical diagnostic process, not a CT workup. Record color, temperature, turgor, capillary refill, dermal/mucosal bleeding and Doppler findings at protocolized intervals, with the most intensive surveillance early after reconstruction because most salvageable vascular events occur in the early postoperative period. Recheck neck position, dressings, tracheostomy ties, external pressure, swelling/hematoma and systemic perfusion. If findings remain equivocal, the reconstructive surgeon may use directed adjunct monitoring, but obvious or strongly suspected vascular compromise should NOT wait for routine imaging or prolonged bedside observation before operative decision-making."
        ),
        "manage": (
            "The management goal of the monitoring card is ESCALATION. Correct immediately reversible external contributors while the reconstructive team is mobilized: remove compressive dressings or positioning, optimize oxygenation/perfusion and identify an expanding hematoma or obvious pedicle compression. Do not repeatedly needle, warm, anticoagulate, leech, or simply 'watch' a flap with credible anastomotic compromise instead of arranging urgent exploration. Medicinal leeches can provide temporary outflow for selected superficial venous congestion when surgical venous correction is not possible or appropriate; they are not a replacement for take-back of a threatened microvascular anastomosis and require institution-specific infection prophylaxis/monitoring."
        ),
        "operate": (
            "MONITORING PRINCIPLE: design the reconstruction so it can be assessed. Mark a reliable Doppler site before leaving the OR; avoid pedicle compression/kinking with inset and closure; choose a clinically visible or sentinel paddle for otherwise buried reconstructions when appropriate; document the immediate postoperative exam so later change is meaningful. If the exam indicates vascular compromise, the operative details belong to the companion 'Free Flap Monitoring and Salvage' card—the key action here is rapid recognition and activation of the take-back pathway."
        ),
        "teach": (
            "Chief/boards discriminator: FREE-FLAP MONITORING = WHAT DOES THE FLAP LOOK/FEEL/SOUND LIKE, IS THE PROBLEM ARTERIAL OR VENOUS, AND DOES IT NEED IMMEDIATE ESCALATION? Purple + swollen + brisk dark blood -> venous congestion. Pale/cool + poor refill + absent bright bleeding -> arterial insufficiency. Clinical examination remains foundational; monitoring devices are adjuncts. The highest-yield error to avoid is delaying exploration of a convincingly compromised flap for nonessential testing."
        ),
        "tags": ["free flap monitoring", "flap compromise", "venous congestion", "arterial insufficiency", "pinprick", "capillary refill", "implantable doppler", "tissue oximetry", "buried flap"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — free-flap physiology, postoperative monitoring, vascular compromise, and reconstructive rescue framework",
            "K.J. Lee's Essential Otolaryngology, 12e — microvascular head-and-neck reconstruction and flap-monitoring principles",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — color/turgor/capillary-refill/pinprick/Doppler monitoring and arterial-versus-venous failure patterns",
            "Dort et al., JAMA Otolaryngol Head Neck Surg 2017 — ERAS Society consensus for major head-and-neck cancer surgery with free-flap reconstruction, including frequent postoperative flap monitoring",
            "Shen et al., J Reconstr Microsurg 2021 — systematic review of monitoring, salvage, and failure timing; close monitoring is most valuable in the first 48 postoperative hours",
        ],
    },
    "free flap monitoring and salvage": {
        "recognize": (
            "Use this card AFTER a flap is judged threatened: it is the OPERATIVE SALVAGE card. A credible loss of inflow/outflow, progressive venous congestion, new absent/changed signal with corroborating examination, expanding hematoma compressing the pedicle, or rapidly deteriorating paddle should be treated as a time-sensitive reconstructive emergency. Earlier recognition and re-exploration are associated with better salvage; venous compromise is often more salvageable than arterial insufficiency, but neither should be observed while viability deteriorates."
        ),
        "localize": (
            "At take-back, localize the failure systematically from outside to inside: external compression/tight closure or hematoma -> pedicle geometry (kink, twist, tension, positional compression) -> recipient artery and vein -> anastomoses -> intraluminal thrombus -> distal flap perfusion. Distinguish venous thrombosis from arterial thrombosis and mechanical obstruction because the correction differs. Also identify systemic contributors such as severe hypotension/hypovolemia, hypothermia or hypercoagulability, but do not attribute a focal failing flap to systemic physiology until the pedicle/anastomoses have been directly assessed."
        ),
        "workup": (
            "A threatened flap usually needs OPERATIVE EXPLORATION rather than additional diagnostic imaging. Review the monitoring trajectory, operative note, recipient vessels, prior neck treatment, pedicle course, anticoagulation/bleeding context and whether there was difficult inset or prior anastomotic revision; these guide what to expect at take-back. If compromise is not clinically convincing, adjunct monitoring can clarify selected cases, but the evidentiary threshold for re-exploration should remain low when serial findings point to vascular failure because salvage probability declines with delay."
        ),
        "manage": (
            "SALVAGE SEQUENCE: urgently re-explore; evacuate hematoma/release compression; untwist or unkink the pedicle; assess arterial inflow and venous outflow; reopen the abnormal anastomosis when indicated; remove thrombus with appropriate thrombectomy/irrigation; revise the anastomosis to healthy vessel; and use a new recipient segment or interposition vein graft when tension, vessel injury or an unusable segment prevents a reliable revision. Correct systemic perfusion and temperature concurrently. Selected intra-flap or catheter-directed fibrinolytic therapy may be considered for otherwise unsalvageable microvascular thrombosis by experienced teams, but current evidence is heterogeneous and lacks prospective randomized trials—do not teach thrombolysis as routine first-line salvage."
        ),
        "operate": (
            "If perfusion returns, verify the entire flap rather than accepting a Doppler signal alone: observe color/capillary refill/bleeding, confirm durable inflow and outflow, ensure the revised pedicle lies without tension or compression, obtain hemostasis without recreating a constricting closure, and re-establish a clear monitoring target. If the flap is irreversibly nonviable despite correction, debride nonviable tissue and choose a SECOND RECONSTRUCTION based on defect urgency, contamination, recipient-vessel availability, prior radiation, donor options and patient physiology—a second free flap can be appropriate, while a regional pedicled flap may be preferable when microsurgical re-reconstruction is unsafe or vessels are depleted."
        ),
        "teach": (
            "Chief/boards discriminator: FREE-FLAP SALVAGE = GET TO THE OR, FIND THE MECHANICAL/THROMBOTIC FAILURE, RESTORE FLOW, THEN PROVE THE REVISION IS DURABLE. Do not let CT, a single reassuring Doppler signal, empiric leeches, or systemic anticoagulation substitute for exploration of convincing anastomotic compromise. Thrombectomy/anastomotic revision are core salvage maneuvers; thrombolytics are selective adjuncts with limited heterogeneous evidence. If salvage fails, have a deliberate second-reconstruction plan rather than treating flap loss as the end of reconstruction."
        ),
        "tags": ["free flap salvage", "takeback", "microvascular thrombosis", "venous thrombosis", "arterial thrombosis", "thrombectomy", "anastomotic revision", "vein graft", "fibrinolysis", "second free flap"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — microvascular compromise, pedicle/anastomotic failure, take-back, and reconstructive salvage principles",
            "K.J. Lee's Essential Otolaryngology, 12e — microvascular reconstruction complications and revision concepts",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — early free-flap failure, arterial/venous compromise and urgent revision framework",
            "Olinde, Farber & Kain, Curr Opin Otolaryngol Head Neck Surg 2021 (PMID 34459800) — prompt identification/intervention and surgical microvascular revision in head-and-neck free-flap salvage",
            "Multi-institutional Head Neck study (PMID 32844522) — better salvage with early compromise, venous versus arterial compromise, and thrombectomy",
            "Mandal et al., Journal of Personalized Medicine 2024 (PMID 39201992) — systematic review showing fibrinolytic salvage evidence remains heterogeneous with no prospective randomized trials",
        ],
    },
}


def apply_free_flap_rebuild_v323(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = FREE_FLAP_REBUILD_V323.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v323"] = True
            module["semantic_role_v323"] = (
                "postoperative surveillance, arterial-versus-venous recognition, and escalation"
                if key == "free flap monitoring compromise salvage"
                else "urgent operative take-back, microvascular revision, and second-reconstruction salvage"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
