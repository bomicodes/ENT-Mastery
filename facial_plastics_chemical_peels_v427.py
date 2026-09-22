"""v42.7: chemical peel classification and formulations for facial plastics boards.

Requested 2026-09-21: full boards-level coverage of chemical peel agents and
depths -- superficial vs. medium vs. deep, the specific formulations in each
category (glycolic acid, Jessner solution, TCA, phenol-croton oil/Baker-Gordon),
and the practical differences between them (histologic depth, indications,
endpoints, and safety requirements).

The existing "Aging Face / Injectables / Resurfacing" topic covers the general
framework for matching aging changes to treatment modality and includes a
detailed facelift-hematoma rescue algorithm, but has no actual chemical peel
content -- no agent list, no depth classification, and no formulation
comparison. This adds that content as a dedicated section within the same
topic's six fields, since peels are one modality within its existing scope
("...Resurfacing").

Content grounded via 2026-09-21 literature check (chemical peel classification
by depth/agent, phenol-croton oil cardiotoxicity monitoring, TCA frosting
endpoints, Fitzpatrick-based PIH risk, and isotretinoin-timing guidance) against
The Plastics Fella chemical peel reference and the ASDS Guidelines Task Force
consensus on procedures during/after isotretinoin (Dermatol Surg 2017), in
addition to the standard Pasha/Cummings facial plastics chapters.
"""

PEELS_MARKER = "CHEMICAL PEEL DEPTH CLASSIFICATION"

RECOGNIZE_ADDITION = (
    " CHEMICAL PEEL DEPTH CLASSIFICATION (high-yield boards framework): peels are classified by the histologic "
    "depth of injury they produce, not just by agent name -- SUPERFICIAL (epidermis only, from stratum corneum "
    "to the basal layer), MEDIUM-DEPTH (full epidermis into the papillary dermis, occasionally upper reticular "
    "dermis), and DEEP (mid-reticular dermis). Depth determines both efficacy for a given problem (fine "
    "rhytids/dyschromia vs. deeper rhytids/actinic damage vs. severe photoaging) and the complication profile "
    "(downtime, scarring risk, and systemic toxicity for deep peels)."
)

LOCALIZE_ADDITION = (
    " SUPERFICIAL AGENTS: glycolic acid (~20-70%, an alpha-hydroxy acid), salicylic acid (~20-30%, a "
    "beta-hydroxy acid, useful in acne-prone/oilier skin since it is lipophilic), Jessner solution (resorcinol, "
    "salicylic acid, and lactic acid in ethanol -- itself superficial in 1-2 coats but becomes a MEDIUM-depth "
    "combination when layered with TCA), and lower-concentration TCA (<=20-30%). MEDIUM-DEPTH AGENTS: TCA "
    "30-35% alone, or -- because higher-concentration TCA alone above ~35% has an unacceptably high scarring "
    "risk -- TCA 35% COMBINED with a priming agent such as Jessner solution (Monheit combination peel) or "
    "70% glycolic acid (Coleman combination peel), which reach medium depth more safely by disrupting the "
    "epidermal barrier first. DEEP AGENTS: phenol-croton oil formulations, classically the Baker-Gordon "
    "formula (USP phenol, croton oil, septisol/soap, and distilled water); croton oil concentration is now "
    "recognized as the primary driver of depth (lower croton oil = shallower, more controllable peels), which "
    "is why modified/diluted phenol-croton formulas have largely replaced the original fixed-ratio Baker-"
    "Gordon recipe in modern practice."
)

WORKUP_ADDITION = (
    " Match peel depth to the problem and to Fitzpatrick skin type before selecting an agent: fine rhytids, "
    "mild dyschromia, and actinic keratoses respond to superficial-to-medium peels; deeper rhytids and more "
    "severe photodamage may need medium or deep peels. Higher Fitzpatrick phototypes (IV-VI) carry a higher "
    "risk of post-inflammatory hyperpigmentation with medium and deep peels, which favors more conservative "
    "depth selection, pretreatment skin priming (e.g., topical retinoid and/or hydroquinone to reduce "
    "post-peel dyschromia), and closer follow-up in this population. Herpes simplex prophylaxis is standard "
    "before medium and deep peels given the risk of reactivation with dermal injury. ISOTRETINOIN: the "
    "classic, still-tested teaching is to avoid medium and deep chemical peels (and other resurfacing/"
    "dermabrasion procedures) for roughly 6-12 months after isotretinoin use because of concern for abnormal "
    "wound healing and atypical scarring; note that a 2017 ASDS consensus found limited evidence to support "
    "this restriction for purely superficial procedures, but the traditional waiting period remains the "
    "expected board answer, especially for medium/deep peels."
)

MANAGE_ADDITION = (
    " ENDPOINTS BY DEPTH (how you tell how deep you are, in real time): SUPERFICIAL peels show a patchy, "
    "stringy white 'pseudofrost' that can be wiped away, or simple erythema. MEDIUM-DEPTH peels show a "
    "uniform, solid WHITE FROST WITH ERYTHEMA VISIBLE THROUGH IT (frosting from coagulated epidermal/papillary "
    "dermal protein while the dermal vasculature still shows through) -- the 'accordion sign' (skin sliding "
    "freely when stretched) confirms adequate but not excessive depth. DEEP (phenol-croton oil) peels progress "
    "to a SOLID, OPAQUE WHITE FROST WITHOUT VISIBLE ERYTHEMA, reflecting full-thickness epidermal and papillary/"
    "upper-reticular dermal coagulation. Titrate agent, concentration, and number of coats to the desired "
    "endpoint rather than to a fixed time."
)

OPERATE_ADDITION = (
    " DEEP PEEL SAFETY REQUIREMENT: phenol is directly cardiotoxic (arrhythmogenic, most often "
    "ventricular ectopy/arrhythmia) and hepato/nephrotoxic with rapid mucocutaneous absorption, so full "
    "phenol-croton oil (Baker-Gordon-type) peels require continuous cardiac monitoring, IV access and "
    "hydration, and staged application (typically treating cosmetic subunits over a defined interval, e.g., "
    "roughly every 10-15 minutes) to limit the systemic phenol load absorbed at any one time -- this "
    "monitoring requirement is unique to deep/phenol peels and is not needed for superficial or "
    "TCA-based medium peels, which are not systemically absorbed to a clinically significant degree."
)

TEACH_ADDITION = (
    " Boards/chief framework: depth of injury, not agent brand name, is what to reason from. SUPERFICIAL "
    "(epidermis: glycolic, salicylic, light TCA, Jessner alone) -> minimal downtime, treats fine texture/mild "
    "dyschromia. MEDIUM (papillary dermis: TCA 35% alone or combined with Jessner/glycolic priming) -> uniform "
    "white frost with erythema showing through, treats moderate rhytids/actinic damage/lentigines. DEEP "
    "(reticular dermis: phenol-croton oil) -> solid opaque frost, treats severe photoaging/deep rhytids but "
    "requires cardiac monitoring for phenol toxicity and carries the highest scarring/pigment-change risk, "
    "especially in darker Fitzpatrick types. A combination peel (Jessner+TCA or glycolic+TCA) exists precisely "
    "because high-concentration TCA alone is a poor way to reach medium depth safely."
)


def apply_facial_plastics_chemical_peels_v427(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    result = {"deepened": False, "challenges_added": []}

    facial = modules.get("Facial Plastics / Trauma", [])
    for row in facial:
        if row.get("topic") == "Aging Face / Injectables / Resurfacing":
            if PEELS_MARKER not in (row.get("recognize") or ""):
                row["recognize"] = (row.get("recognize") or "").rstrip() + RECOGNIZE_ADDITION
                row["localize"] = (row.get("localize") or "").rstrip() + LOCALIZE_ADDITION
                row["workup"] = (row.get("workup") or "").rstrip() + WORKUP_ADDITION
                row["manage"] = (row.get("manage") or "").rstrip() + MANAGE_ADDITION
                row["operate"] = (row.get("operate") or "").rstrip() + OPERATE_ADDITION
                row["teach"] = (row.get("teach") or "").rstrip() + TEACH_ADDITION
                for tag in ("chemical peel", "TCA", "phenol-croton oil", "Baker-Gordon", "Jessner solution", "glycolic acid"):
                    if tag not in row.get("tags", []):
                        row.setdefault("tags", []).append(tag)
                sources = row.setdefault("source_basis", [])
                for addition in (
                    "The Plastics Fella — Chemical Peels: Classification, Indications, & Complications "
                    "(reviewed 2026-09-21) — depth classification, agent/concentration lists, frosting "
                    "endpoints, phenol cardiac-monitoring requirement.",
                    "ASDS Guidelines Task Force: Consensus Recommendations Regarding the Safety of Lasers, "
                    "Dermabrasion, Chemical Peels, Energy Devices, and Skin Surgery During and After "
                    "Isotretinoin Use. Dermatol Surg. 2017 — isotretinoin timing guidance and its evolving "
                    "evidence base.",
                ):
                    if addition not in sources:
                        sources.append(addition)
                result["deepened"] = True
            break

    topic_domains = {
        card.get("topic"): domain
        for domain, cards in modules.items()
        for card in cards
        if card.get("topic")
    }

    challenges = data_module.CLINICAL_CHALLENGES_V119
    existing_ids = {q.get("id") for q in challenges}
    for q in CLINICAL_CHALLENGES_NEW:
        if q["id"] in existing_ids:
            continue
        row = dict(q)
        canonical_domain = topic_domains.get(row["topic"])
        if canonical_domain is None:
            raise RuntimeError(f"v42.7: challenge topic missing from curriculum: {row['topic']}")
        row["concept_id"] = _v6_item_id(canonical_domain, row["topic"])
        challenges.append(row)
        existing_ids.add(row["id"])
        result["challenges_added"].append(row["id"])

    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in challenges if q.get("id")}

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.CLINICAL_CHALLENGES_V119 = challenges
        app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119
    return result


import re


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


CLINICAL_CHALLENGES_NEW = [
    {
        "id": "v427-peels-depth-classification-01",
        "domain": "Facial Plastics / Trauma",
        "topic": "Aging Face / Injectables / Resurfacing",
        "stem": (
            "During a medium-depth TCA/Jessner combination peel, the treated skin develops a uniform white "
            "frost with erythema still visible through it, and the skin slides freely when stretched. What "
            "histologic depth does this endpoint correspond to?"
        ),
        "choices": [
            "Stratum corneum only",
            "Papillary dermis",
            "Mid-reticular dermis",
            "Subcutaneous fat",
        ],
        "answer": 1,
        "explanation": (
            "A uniform white frost with erythema showing through it, together with the 'accordion sign' "
            "(free skin sliding), is the classic medium-depth peel endpoint, corresponding to injury through "
            "the full epidermis into the papillary dermis."
        ),
        "why_wrong": [
            "Stratum-corneum-only injury is a superficial peel and shows only patchy, wipeable 'pseudofrost,' "
            "not a uniform frost with erythema showing through.",
            "Correct.",
            "Mid-reticular dermis injury is the deep-peel endpoint (solid, opaque white frost WITHOUT visible "
            "erythema), reached with phenol-croton oil, not TCA/Jessner.",
            "No standard chemical peel is intentionally taken to the subcutaneous fat; that depth is well "
            "beyond even deep peels and would represent a severe complication.",
        ],
        "board_pearl": "Superficial = patchy wipeable pseudofrost (epidermis). Medium = uniform frost WITH "
        "erythema showing through (papillary dermis). Deep = solid opaque frost WITHOUT erythema showing "
        "through (mid-reticular dermis, phenol-croton oil).",
        "curveball": "Why is TCA 35% typically combined with Jessner solution or glycolic acid rather than used alone at medium depth?",
        "curveball_answer": (
            "TCA concentrations much above 35% used alone carry an unacceptably high risk of scarring and "
            "uneven penetration; priming the epidermal barrier first with Jessner solution (Monheit peel) or "
            "70% glycolic acid (Coleman peel) allows a lower, safer TCA concentration to reach medium depth "
            "more predictably and with a more controllable endpoint."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v427-peels-phenol-cardiac-monitoring-01",
        "domain": "Facial Plastics / Trauma",
        "topic": "Aging Face / Injectables / Resurfacing",
        "stem": (
            "A patient is undergoing a full-face phenol-croton oil (Baker-Gordon-type) deep chemical peel. "
            "What safety measure is specifically required for this peel that is not routinely needed for a "
            "TCA-based medium-depth peel?"
        ),
        "choices": [
            "Herpes simplex antiviral prophylaxis",
            "Continuous cardiac monitoring with IV access and staged application to limit systemic phenol absorption",
            "Pretreatment with a topical retinoid",
            "Fitzpatrick skin typing before treatment",
        ],
        "answer": 1,
        "explanation": (
            "Phenol is directly cardiotoxic (arrhythmogenic) and hepato/nephrotoxic with rapid systemic "
            "absorption through the skin, so full phenol-croton oil deep peels require continuous cardiac "
            "monitoring, IV hydration/access, and staged application by cosmetic subunit to limit the "
            "systemic phenol load at any one time -- a requirement unique to deep/phenol peels."
        ),
        "why_wrong": [
            "Herpes prophylaxis is appropriate before medium AND deep peels given dermal injury, so it does "
            "not uniquely distinguish deep peels from medium peels.",
            "Correct.",
            "Retinoid priming is a general pretreatment strategy used across peel depths to improve outcomes "
            "and reduce dyschromia, not a deep-peel-specific safety requirement.",
            "Fitzpatrick typing is relevant to pigmentary risk assessment for any peel depth, not a "
            "deep-peel-specific safety measure.",
        ],
        "board_pearl": "Phenol-croton oil deep peels need cardiac monitoring because of phenol's "
        "cardiotoxicity; this is not required for superficial or TCA-based medium peels.",
        "curveball": "What peel-related teaching about isotretinoin should you counsel this patient on preoperatively?",
        "curveball_answer": (
            "The classic teaching is to avoid medium and deep chemical peels (and other resurfacing "
            "procedures) for roughly 6-12 months after isotretinoin use due to concern for abnormal wound "
            "healing and atypical scarring; a 2017 ASDS consensus found limited evidence for this restriction "
            "specifically for superficial procedures, but the traditional waiting period is still the expected "
            "answer for medium/deep peels like this one."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
]
