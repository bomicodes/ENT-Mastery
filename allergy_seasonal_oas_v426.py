"""v42.6: seasonal aeroallergen timing + oral allergy syndrome (pollen-food cross-reactivity).

Requested 2026-09-21: make sure boards coverage includes (1) which aeroallergens
peak in which season -- trees in spring, grasses in late spring/summer, weeds
(ragweed) in fall, mold spores variable/damp-season -- and (2) the pollen-food
(oral allergy) cross-reactivity pattern boards love to test: birch-associated
fruits/vegetables, ragweed-melon family, grass-tomato/melon, and the
mugwort-celery-spice pattern, plus how this differs mechanistically (and in
food safety) from true, potentially anaphylactic food allergy.

Neither existed anywhere in the curriculum: the existing "Allergic Rhinitis"
topic covers diagnosis/management of AR generally but has no seasonal pollen
calendar and no oral allergy syndrome content at all.
"""

SEASONAL_MARKER = "SEASONAL AEROALLERGEN CALENDAR"
OAS_SPLIT_MARKER = "see Oral Allergy Syndrome (Pollen-Food Syndrome)."

ALLERGIC_RHINITIS_RECOGNIZE_ADDITION = (
    " SEASONAL AEROALLERGEN CALENDAR (boards pattern-recognition): TREE pollen peaks in SPRING (roughly "
    "February-May depending on region/climate) -- oak, birch, cedar/juniper, maple, elm. GRASS pollen peaks in "
    "LATE SPRING through SUMMER (roughly May-July) -- timothy, Bermuda, Kentucky bluegrass. WEED pollen, "
    "dominated by ragweed, peaks in FALL (roughly August-October, worsening until first frost). MOLD spores "
    "(Alternaria, Cladosporium) are more variable and often peak in warm, damp, or late-summer/fall conditions "
    "and can persist indoors year-round. A patient whose symptoms cluster tightly in one of these windows year "
    "after year is describing a specific pollen family before any testing is done -- use the seasonal history "
    "to predict which panel to test and to anticipate oral allergy syndrome triggers (below)."
)

ALLERGIC_RHINITIS_LOCALIZE_ADDITION = (
    " ORAL ALLERGY SYNDROME (pollen-food syndrome): pollen-specific IgE can cross-react with structurally "
    "similar, heat-labile plant proteins (commonly PR-10/Bet v1 homologs and profilins) in certain raw fruits, "
    "vegetables, and nuts. Contact with the oral mucosa triggers rapid-onset, LOCALIZED lip/mouth/throat "
    "itching or mild swelling that typically resolves within minutes and rarely progresses to systemic "
    "anaphylaxis, because the causative proteins are usually degraded by cooking, processing, and digestion -- "
    "this is the key discriminator from a true, potentially anaphylactic food allergy (classically to peanut, "
    "tree nut, shellfish, egg, or milk), which is stable to heat/digestion and can cause systemic reactions "
    "with cooked or processed forms of the food."
)

ALLERGIC_RHINITIS_WORKUP_ADDITION = (
    " BOARDS-STYLE POLLEN-FOOD CROSS-REACTIVITY PAIRINGS: BIRCH pollen -> apple, pear, peach/stone fruits, "
    "cherry, kiwi, carrot, celery, hazelnut, almond (Bet v1/PR-10 homology; classic high-yield pairing is "
    "birch-apple). RAGWEED pollen -> melons (cantaloupe, honeydew, watermelon), banana, cucumber, zucchini "
    "(profilin-mediated cross-reactivity; classic pairing is ragweed-melon/banana). GRASS pollen -> tomato, "
    "melon, orange, peach. MUGWORT pollen -> celery, carrot, fennel, and spices such as coriander/anise "
    "('mugwort-celery-spice syndrome', more prominent in some European populations). Latex-fruit syndrome is a "
    "related but distinct cross-reactivity pattern (latex allergy with banana, avocado, kiwi, chestnut) worth "
    "distinguishing from pollen-food syndrome on boards. Testing (skin prick with fresh fruit/'prick-to-prick' "
    "testing outperforms commercial extracts for labile proteins) is reserved for diagnostic uncertainty or "
    "before advising food reintroduction, not for routine confirmation of a classic, reproducible history."
)

ALLERGIC_RHINITIS_MANAGE_ADDITION = (
    " Manage oral allergy syndrome by counseling avoidance of the specific RAW trigger foods (cooking/peeling/"
    "canning usually denatures the causative protein and restores tolerance for most patients), reassuring "
    "that systemic reactions are uncommon but can rarely occur (so a first reaction with a new food, throat "
    "tightness, or systemic symptoms should prompt allergy referral and possible epinephrine auto-injector "
    "prescription), and treating the underlying seasonal allergic rhinitis, since better pollen control can "
    "reduce the threshold for oral symptoms."
)

ALLERGIC_RHINITIS_TEACH_ADDITION = (
    " Boards pearl: a seasonal timing history (tree = spring, grass = summer, weed/ragweed = fall) plus a "
    "reproducible 'raw fruit makes my mouth itch' history is oral allergy syndrome, not a true food allergy -- "
    "match the fruit family to the pollen (birch-apple, ragweed-melon/banana, mugwort-celery-spice) rather than "
    "reflexively ordering food-allergy panels or restricting cooked forms of the food."
)


def apply_allergy_seasonal_oas_v426(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    result = {"deepened": False, "challenges_added": []}

    rhinology = modules.get("Rhinology / Allergy / Skull Base", [])
    for row in rhinology:
        if row.get("topic") == "Allergic Rhinitis":
            recognize = row.get("recognize") or ""
            if SEASONAL_MARKER not in recognize and OAS_SPLIT_MARKER not in recognize:
                row["recognize"] = (row.get("recognize") or "").rstrip() + ALLERGIC_RHINITIS_RECOGNIZE_ADDITION
                row["localize"] = (row.get("localize") or "").rstrip() + ALLERGIC_RHINITIS_LOCALIZE_ADDITION
                row["workup"] = (row.get("workup") or "").rstrip() + ALLERGIC_RHINITIS_WORKUP_ADDITION
                row["manage"] = (row.get("manage") or "").rstrip() + ALLERGIC_RHINITIS_MANAGE_ADDITION
                row["teach"] = (row.get("teach") or "").rstrip() + ALLERGIC_RHINITIS_TEACH_ADDITION
                for tag in ("oral allergy syndrome", "pollen-food syndrome", "seasonal allergens", "birch-apple", "ragweed"):
                    if tag not in row.get("tags", []):
                        row.setdefault("tags", []).append(tag)
                sources = row.setdefault("source_basis", [])
                addition = (
                    "AAAAI/ACAAI allergen-immunology teaching on pollen-food (oral allergy) syndrome cross-"
                    "reactivity patterns and seasonal aeroallergen timing."
                )
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
            raise RuntimeError(f"v42.6: challenge topic missing from curriculum: {row['topic']}")
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
        "id": "v426-allergy-oas-birch-apple-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Allergic Rhinitis",
        "stem": (
            "A patient with spring-predominant sneezing and rhinorrhea reports that her lips and mouth itch "
            "within minutes whenever she eats a raw apple or pear, but she tolerates apple pie and canned pear "
            "without any symptoms. What is the most likely explanation?"
        ),
        "choices": [
            "True IgE-mediated food allergy to apple and pear requiring strict avoidance of all forms",
            "Oral allergy syndrome from birch pollen cross-reactivity with heat-labile proteins in raw apple/pear",
            "Hereditary angioedema triggered by fruit acidity",
            "Irritant contact stomatitis unrelated to her allergic rhinitis",
        ],
        "answer": 1,
        "explanation": (
            "Spring (tree pollen season) allergic rhinitis plus rapid-onset oral itching limited to RAW apple/"
            "pear that resolves with cooking is the classic birch-pollen oral allergy syndrome pattern: IgE "
            "against birch pollen cross-reacts with a heat-labile PR-10 (Bet v1 homolog) protein in these "
            "fruits, which is degraded by cooking/processing."
        ),
        "why_wrong": [
            "A true IgE-mediated food allergy is typically stable to heat and would also react to cooked/"
            "processed forms, unlike this history.",
            "Correct.",
            "Hereditary angioedema is not triggered by specific raw fruits and does not track with a pollen "
            "season or resolve with cooking.",
            "The tight correlation with raw-versus-cooked form and the seasonal pollen context point to a "
            "specific IgE cross-reactivity mechanism, not nonspecific irritation.",
        ],
        "board_pearl": "Birch pollen (spring) cross-reacts with raw apple, pear, peach, cherry, carrot, and "
        "hazelnut via a heat-labile PR-10 protein -- cooking/processing usually eliminates the reaction.",
        "curveball": "What would make you refer this patient to allergy rather than just reassure her?",
        "curveball_answer": (
            "A first reaction to a new cross-reactive food, any systemic symptoms (throat tightness, "
            "wheeze, hives beyond the mouth, hypotension), or reaction to a food that should be cooked/"
            "processed in this pattern should prompt allergy referral, skin/prick-to-prick testing with fresh "
            "fruit if needed, and consideration of an epinephrine auto-injector prescription, since a small "
            "minority of oral allergy syndrome patients can have more significant reactions."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v426-allergy-oas-ragweed-melon-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Allergic Rhinitis",
        "stem": (
            "A patient with fall-predominant nasal congestion and sneezing that worsens each August through "
            "October develops mouth itching after eating fresh cantaloupe and banana. Which pollen is most "
            "likely driving both his seasonal symptoms and his fruit reaction?"
        ),
        "choices": ["Birch", "Grass", "Ragweed", "Mugwort"],
        "answer": 2,
        "explanation": (
            "Ragweed is the dominant fall weed pollen (peaking roughly August-October until first frost) and "
            "is the classic pollen associated with profilin-mediated cross-reactivity to melons (cantaloupe, "
            "honeydew, watermelon), banana, cucumber, and zucchini."
        ),
        "why_wrong": [
            "Birch is a spring tree pollen classically linked to apple/pear/stone fruit/hazelnut, not this "
            "fall timing or these fruits.",
            "Grass pollen peaks in late spring/summer and is more associated with tomato, melon, and orange.",
            "Correct.",
            "Mugwort is a weed classically linked to celery, carrot, and spices (mugwort-celery-spice "
            "syndrome), and while it can overlap with ragweed season, ragweed is the higher-yield fall answer "
            "for this exact melon/banana pairing.",
        ],
        "board_pearl": "Ragweed (fall) cross-reacts with melons and banana via profilin; match the fruit "
        "family to the pollen season to identify the culprit aeroallergen.",
        "curveball": "Why does profilin cross-reactivity tend to produce a broader, less predictable food list than PR-10 cross-reactivity?",
        "curveball_answer": (
            "Profilins are highly conserved, ubiquitous plant proteins found across many unrelated plant "
            "families, so profilin-sensitized patients can react to a wider and less anatomically predictable "
            "range of fruits and vegetables than PR-10 (Bet v1)-driven reactions, which track more tightly "
            "with specific botanically related foods."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
]
