"""v33.5 — source-grounded free-flap monitoring versus operative salvage role separation.

The parent card owns bedside physiology, recognition, monitoring, and the decision that a flap is
threatened. The companion card starts at that decision and owns urgent takeback, pedicle/anastomosis
rescue, and fallback reconstruction. Keeping the cards adjacent but cognitively distinct prevents
six stages of duplicated 'check the Doppler and return to OR' content.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


FREE_FLAP_REBUILD_V335 = {
    "free flap monitoring compromise salvage": {
        "recognize": (
            "Use this as the MONITORING / DIAGNOSIS card. A newly reconstructed head-and-neck defect is a time-sensitive vascular exam, not a binary Doppler check. Establish the flap's immediate postoperative baseline and trend color, temperature, turgor, capillary refill, dermal bleeding/pinprick when applicable, and arterial/venous Doppler signals. Venous compromise classically becomes swollen, tense/dusky and may bleed rapidly with dark blood; arterial insufficiency is more often pale/cool with delayed or absent refill and little/no fresh bleeding. Real flaps can be mixed, buried, or partially monitored, so physiology and trend outrank one isolated sign."
        ),
        "localize": (
            "Localize the failure along the entire circuit: arterial inflow -> anastomosis/pedicle -> flap microcirculation -> venous anastomosis/outflow. Also look for EXTRINSIC causes before assuming intraluminal thrombosis: tight neck closure, hematoma, edema, dependent positioning, pedicle kinking/torsion, compression by a tracheostomy tie/dressing, or geometry altered by head position. A reassuring arterial signal does NOT exclude venous outflow obstruction; the artery may continue to transmit a strong signal while the flap congests."
        ),
        "workup": (
            "Clinical examination is the core monitoring test for an accessible flap; handheld Doppler, implantable Doppler, tissue oximetry or other adjuncts should accelerate recognition, not overrule a deteriorating clinical exam. Compare with the marked pedicle/perforator signal and with the patient's own baseline. If compromise is plausible, immediately call the reconstructive surgeon and mobilize the OR while correcting obvious reversible external compression. Do not spend the flap's ischemic window obtaining CT/CTA or serial observations merely to make the diagnosis look more certain."
        ),
        "manage": (
            "Treat suspected vascular compromise as a CLOCK problem. Most pedicle thromboses occur early after transfer and salvage probability falls as recognition-to-reexploration time lengthens. At bedside remove constrictive dressings or external pressure, normalize head/neck position, correct major hypotension/hypovolemia and inspect for expanding hematoma—but perform those steps in parallel with takeback preparation, not as a prolonged therapeutic trial. Leeches can temporize selected venous-congested tissue when surgical venous outflow cannot be established; they are not first-line treatment for a correctable thrombosed free-flap pedicle."
        ),
        "operate": (
            "The endpoint of this card is the DECISION TO EXPLORE, not the microsurgical rescue sequence. Escalate immediately for a new concerning clinical change, loss/change of the expected Doppler signal, progressive congestion/pallor, rapidly expanding neck hematoma, or discordant monitoring data that cannot promptly be explained. A buried flap deserves an especially low threshold because surface examination is limited. The separate 'Free Flap Monitoring and Salvage' card owns what to do once the neck is reopened."
        ),
        "teach": (
            "Chief/boards frame: identify whether the problem is INFLOW, OUTFLOW, or EXTRINSIC COMPRESSION, and remember that TIME TO TAKEBACK is a modifiable determinant of salvage. Venous congestion is often easier to see than arterial insufficiency; an arterial Doppler signal is not a certificate of flap viability. Monitoring exists to trigger timely rescue—not to delay rescue until every test agrees."
        ),
        "tags": ["free flap monitoring", "flap compromise", "venous congestion", "arterial insufficiency", "Doppler", "microvascular thrombosis", "hematoma", "urgent takeback"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — microvascular head-and-neck reconstruction, postoperative flap assessment, vascular compromise and salvage framework",
            "K.J. Lee's Essential Otolaryngology, 12e — head-and-neck reconstruction and postoperative complication framework",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — reconstructive options and postoperative head-and-neck surgical complication framework",
            "Salgado et al. Postoperative Care and Monitoring of the Reconstructed Head and Neck Patient — early intensive monitoring, venous-predominant compromise and inverse relationship between delay and salvage",
            "Wax/Spiegel-era and subsequent systematic free-flap monitoring literature — clinical assessment remains the core method; adjunct monitoring is useful particularly for buried flaps",
            "2025 free-flap salvage literature — urgent surgical revision remains primary therapy for established pedicle thrombosis; thrombolytics are selective adjuncts rather than substitutes for mechanical correction",
        ],
    },
    "free flap monitoring and salvage": {
        "recognize": (
            "Use this as the OPERATIVE RESCUE card. Start after the monitoring card has concluded that a free flap is threatened enough to explore. The question is no longer 'is the flap abnormal?' but 'what specifically has failed, can perfusion be restored quickly, and is the tissue still salvageable?' Obtain the index operative details while the room is being mobilized: donor flap, artery/vein(s), recipient vessels, coupler/suture technique, pedicle geometry, vein grafts, intraoperative problems and postoperative signal baseline."
        ),
        "localize": (
            "At takeback, reopen enough of the reconstruction to SEE THE ENTIRE PEDICLE and remove external causes first: evacuate hematoma, release constricting closure, untwist/kink the pedicle and correct geometry. Then interrogate arterial inflow, venous outflow and the anastomoses directly. Dark swollen tissue with good inflow directs attention to venous obstruction; a pale flap with absent inflow directs attention to artery/anastomosis. Do not revise a visible anastomosis blindly while leaving an occult downstream kink, recipient-vessel problem or compressive hematoma untouched."
        ),
        "workup": (
            "The operative 'workup' is sequential and mechanical: confirm proximal recipient-vessel flow -> inspect the arterial anastomosis -> inspect flap/pedicle -> inspect each venous pathway -> identify thrombus versus technical obstruction -> assess tissue reperfusion after correction. If thrombosis is present, open the affected anastomosis as needed, remove clot, assess back-bleeding/inflow, irrigate according to microsurgical practice and determine whether revision to healthier vessel ends or a different recipient vessel is required. Persistent poor outflow after a technically patent repair should trigger a search for propagation or microcirculatory failure rather than repeated cosmetic revisions."
        ),
        "manage": (
            "Match rescue to cause. External compression/kink -> release and re-site the pedicle. Anastomotic thrombosis/technical failure -> thrombectomy plus revision, often cutting back to healthy intima. Inadequate recipient vessel -> choose another recipient; bridge with a vein graft only when geometry demands it because added anastomoses increase complexity. Selective thrombolysis can be considered when extensive flap-side thrombosis persists despite mechanical thrombectomy and revision, but evidence does not support delaying definitive revision to give a drug. Systemic anticoagulation/antiplatelet decisions are individualized around thrombosis mechanism and bleeding risk."
        ),
        "operate": (
            "Before re-closing, prove a durable rescue: warm/color/turgor and bleeding recover appropriately, Doppler signals are stable, artery and vein lie without tension/kink through the intended head position, the neck has hemostasis without pedicle compression, and the monitoring target is clearly marked. If the flap remains nonviable or rapidly rethromboses despite correction, stop serial futile revisions: debride nonviable tissue, protect exposed carotid/hardware/aerodigestive tract, and choose a second free flap or regional/pedicled reconstruction according to defect, recipient-vessel availability, physiology and oncologic urgency."
        ),
        "teach": (
            "Salvage algorithm: OPEN EARLY -> RELIEVE EXTRINSIC CAUSES -> TRACE THE WHOLE PEDICLE -> RESTORE INFLOW/OUTFLOW -> REVISE THROMBOSED/FAULTY ANASTOMOSIS -> PROVE STABLE REPERFUSION -> choose backup reconstruction if viability cannot be restored. The important resident distinction is that 'takeback' is not an operation by itself: successful rescue requires identifying WHY the circuit failed and correcting that mechanism."
        ),
        "tags": ["free flap salvage", "microvascular takeback", "thrombectomy", "anastomotic revision", "recipient vessel", "vein graft", "thrombolysis", "second free flap", "pedicle kink"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — operative microvascular reconstruction, recipient vessels, postoperative vascular compromise and salvage principles",
            "K.J. Lee's Essential Otolaryngology, 12e — reconstructive surgery and postoperative complication framework",
            "Pasha 6e — head-and-neck reconstruction and surgical complication framework",
            "Salgado et al. Postoperative Care and Monitoring of the Reconstructed Head and Neck Patient — urgent exploration and time-dependent microvascular salvage",
            "Chemoprophylaxis and Management of Venous Thromboembolism in Microvascular Surgery (2023) — venous thrombosis, takeback timing and salvage determinants",
            "Free Flap Salvage Using Extracorporeal Tissue Plasminogen Activator Administration (2025) — surgical revision as foundation and selective tPA as an adjunct without demonstrated superiority",
        ],
    },
}


def apply_free_flap_role_separation_v335(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = FREE_FLAP_REBUILD_V335.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v335"] = True
            module["semantic_role_v335"] = {
                "free flap monitoring compromise salvage": "bedside physiology, recognition, localization of threatened-flap mechanism, and urgent takeback decision",
                "free flap monitoring and salvage": "operative takeback, pedicle/anastomotic rescue, proof of reperfusion, and backup reconstruction",
            }[key]
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
