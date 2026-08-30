"""v31.3 — source-grounded free-flap monitoring vs compromise/salvage rebuild.

The duplicate audit identifies two nearly contained free-flap cards. This bounded repair
assigns different clinical jobs: bedside monitoring owns early recognition and escalation;
compromise/salvage owns urgent operative diagnosis, pedicle rescue, and the contingency
plan when the index flap cannot be recovered.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


FREE_FLAP_REBUILD_V313 = {
    "free flap monitoring and salvage": {
        "recognize": (
            "This card owns POSTOPERATIVE MONITORING and early recognition. Establish a documented baseline immediately after transfer from the OR, then trend the same skin-paddle or mucosal-paddle findings serially. Clinical monitoring remains fundamental: color, temperature, turgor, capillary refill, bleeding after a standardized pinprick when appropriate, and an external or implantable Doppler signal. A healthy flap is warm and appropriately colored with brisk-but-not-instant refill. Venous congestion classically becomes dusky/blue, swollen and tense with very brisk refill and dark rapid bleeding; arterial insufficiency is more often pale/cool with delayed or absent refill, weak/absent bleeding and loss of arterial signal. A single sign is not perfect—the important event is a meaningful change from the established baseline."
        ),
        "localize": (
            "Localize an abnormal finding to INFLOW, OUTFLOW, or EXTRINSIC COMPRESSION before calling the flap simply 'bad.' Venous problems are more common than arterial causes of early compromise. A preserved arterial Doppler does not exclude venous thrombosis, and a Doppler signal heard near the pedicle can persist despite distal flap malperfusion. Conversely, loss of a signal can reflect probe displacement or technical artifact. Buried flaps require a deliberately planned monitoring strategy—such as an implantable Doppler, flow coupler, externalized monitor segment, or other validated adjunct—because visual examination is unavailable."
        ),
        "workup": (
            "The workup for a suspected failing free flap is deliberately SHORT. Repeat and verify the bedside examination, compare with prior documented checks, inspect the neck for hematoma/tension, assess the Doppler/monitoring device, and immediately contact the reconstructive team. Do not send a clearly threatened flap through a prolonged CT, angiographic, laboratory, or observation pathway merely to obtain diagnostic certainty. Adjunct technologies can improve surveillance in selected settings, but none should delay operative exploration when the clinical trajectory indicates vascular compromise. The highest-yield 'test' is rapid expert reassessment of a changing flap."
        ),
        "manage": (
            "Organize monitoring so deterioration is detected and acted on rapidly, especially during the first 24-48 hours when most salvageable vascular events declare themselves. Use a written institutional schedule and a clear escalation pathway rather than an arbitrary universal frequency. Optimize systemic physiology—oxygenation, temperature, volume status and hemodynamics—without reflexively treating every Doppler change with fluids, transfusion or anticoagulation. Avoid external compression or a tight tracheostomy tie/dressing over the pedicle. If repeated examination remains concerning, management is urgent takeback, not prolonged bedside tinkering."
        ),
        "operate": (
            "This monitoring card stops at the threshold for exploration: a convincing new perfusion abnormality that cannot be immediately explained and corrected at the bedside should trigger prompt operative assessment. The purpose of monitoring is not to name the exact thrombus from the ward—it is to shorten ischemic/congestive time. When exploration is required, transition to the separate FREE-FLAP COMPROMISE / SALVAGE framework, where the pedicle, anastomoses, hematoma, kinking and recipient vessels are systematically evaluated and repaired."
        ),
        "teach": (
            "Chief/boards framework: MONITORING asks, 'Is this flap changing, is the pattern more consistent with venous congestion or arterial insufficiency, and does it need immediate escalation?' Trend COLOR + TURGOR + CAPILLARY REFILL + TEMPERATURE + BLEEDING + DOPPLER against a baseline. Venous = blue/swollen/brisk refill/dark rapid blood; arterial = pale/cool/slow refill/little blood. Clinical concern overrides a reassuring gadget. The value of monitoring is TIME TO RECOGNITION, because salvage probability falls as vascular compromise persists. Do not duplicate the operative salvage algorithm here."
        ),
        "tags": ["free flap monitoring", "skin paddle", "capillary refill", "pinprick", "Doppler", "implantable Doppler", "venous congestion", "arterial insufficiency", "buried flap", "takeback threshold"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — microvascular head-and-neck reconstruction and postoperative flap assessment",
            "K.J. Lee's Essential Otolaryngology, 12e — head-and-neck reconstruction and postoperative free-flap principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — reconstructive monitoring and postoperative complication pearls",
            "Abdel-Galil & Mitchell, Br J Oral Maxillofac Surg 2009 — systematic reviews of noninvasive and invasive free-tissue-transfer monitoring techniques",
            "Kwee et al., J Reconstr Microsurg 2021 — systematic review of free-flap monitoring, salvage and failure timing; close monitoring is most valuable in the first 48 hours"
        ],
    },
    "free flap monitoring compromise salvage": {
        "recognize": (
            "This card owns CONFIRMED OR STRONGLY SUSPECTED COMPROMISE and operative salvage—not routine ward surveillance. Treat an evolving vascular problem as a reconstructive emergency. Early failure mechanisms include venous thrombosis/congestion, arterial thrombosis or inflow failure, hematoma/extrinsic compression, pedicle kink or torsion, vasospasm, and technical anastomotic problems. Later deterioration broadens the differential to infection, fistula/wound breakdown, vessel exposure or thrombosis after a previously stable period. The question is not 'which monitor is best?' but 'what is preventing perfusion and can it be reversed now?'"
        ),
        "localize": (
            "At takeback, localize the failure systematically from flap to pedicle to recipient vessels. Release constricting sutures/dressings and evacuate hematoma when present; inspect the pedicle course for tension, twist, compression and geometry; then assess venous outflow and arterial inflow across the anastomoses. Venous thrombosis is the most frequent early vascular mechanism in pooled series, but apparent venous congestion can be caused by mechanical compression rather than intraluminal clot. Repeated thrombosis after technically adequate revision should prompt a search for pedicle geometry, recipient-vessel quality, a distal problem, or an unrecognized systemic contributor rather than repeated blind thrombectomy alone."
        ),
        "workup": (
            "Do not delay exploration for extensive imaging when the flap is acutely threatened. In the OR, the diagnostic sequence is direct inspection plus assessment of inflow/outflow after relieving mechanical causes. Determine whether thrombus is present, whether the anastomosis is technically sound, whether recipient artery and vein remain usable, and whether the flap demonstrates recoverable perfusion after correction. If the flap cannot be salvaged, define the reconstructive defect and available recipient vessels before committing to a second free flap, pedicled flap, or temporizing strategy."
        ),
        "manage": (
            "Management priority is RAPID RE-EXPLORATION. Correct reversible systemic and mechanical factors while mobilizing the OR, but do not allow observation to substitute for takeback in a convincingly compromised flap. After successful salvage, intensify monitoring because recurrent thrombosis can occur. If the index flap is nonviable, debride nonviable tissue and reconstruct according to defect needs, infection/contamination, recipient-vessel availability and patient physiology. Evidence synthesis supports a second free flap as a highly successful option in appropriately selected head-and-neck patients after flap loss; a pedicled regional flap remains important when recipient vessels, contamination, operative tolerance or urgency make another free transfer less attractive."
        ),
        "operate": (
            "Operative salvage is cause-directed: evacuate compressive hematoma; correct kink/torsion or excessive pedicle tension; revise a faulty anastomosis; remove thrombus and re-establish reliable inflow/outflow when thrombosis is present; and move to an alternate recipient vessel or interposition strategy when the original vessel cannot provide dependable perfusion. Reassess the entire flap after flow is restored rather than accepting a Doppler signal alone as proof of viability. Pharmacologic thrombolysis or other adjuncts are selective tools—not substitutes for correcting the mechanical/anastomotic cause and not universal protocol. If tissue remains nonviable despite restored flow, abandon futile repeated revisions and move to a planned secondary reconstruction."
        ),
        "teach": (
            "Chief/boards framework: SALVAGE asks, 'Why did flow fail, how quickly can I restore it, and what is plan B if the flap is dead?' TAKE BACK EARLY -> RELEASE COMPRESSION / CHECK GEOMETRY -> INSPECT ANASTOMOSES -> RESTORE VENOUS OUTFLOW AND ARTERIAL INFLOW -> REASSESS VIABILITY -> CHOOSE SECONDARY RECONSTRUCTION IF UNSALVAGEABLE. Time matters: a large systematic review found salvage was highest for explorations in the first postoperative day and dropped sharply with later recognition. A successful revision requires correction of the CAUSE, not merely removal of clot. This is deliberately distinct from the monitoring card, whose job ends when it recognizes the need for takeback."
        ),
        "tags": ["free flap compromise", "free flap salvage", "takeback", "venous thrombosis", "arterial thrombosis", "hematoma", "pedicle kink", "anastomotic revision", "recipient vessel", "secondary free flap"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — microvascular reconstruction, vascular compromise and flap salvage",
            "K.J. Lee's Essential Otolaryngology, 12e — reconstructive complications and management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — head-and-neck free-flap complication management",
            "Kwee et al., J Reconstr Microsurg 2021 — systematic review of 44,031 free flaps: venous causes predominate and salvage is strongly time-dependent",
            "Walia et al., Otolaryngol Head Neck Surg 2021 — systematic review/meta-analysis of management after head-and-neck free-flap failure; secondary free-flap reconstruction had high success"
        ],
    },
}


def apply_free_flap_rebuild_v313(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = FREE_FLAP_REBUILD_V313.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v313"] = True
        module["semantic_role_v313"] = (
            "bedside monitoring and early recognition" if key == "free flap monitoring and salvage"
            else "operative diagnosis, urgent vascular salvage, and secondary reconstruction contingency"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
