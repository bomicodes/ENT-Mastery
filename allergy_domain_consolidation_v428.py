"""v42.8: consolidate allergy content -- move Anaphylaxis into the allergy domain,
split Oral Allergy Syndrome out of Allergic Rhinitis into its own topic.

Requested 2026-09-21, following up on the seasonal-allergy/OAS deep dive:

1. "Anaphylaxis" (added in v42.2) lived in General ENT / Emergencies. The user
   asked to move it in with the rest of allergy content, since it is most often
   triggered by an allergy-related exposure (SCIT/SLIT injections, food, insect
   sting) and is taught alongside allergy/immunology. Moves the topic to
   Rhinology / Allergy / Skull Base, where Allergic Rhinitis, Allergy Testing,
   SCIT/SLIT, Local Allergic Rhinitis, and Nonallergic Rhinitis already live.

2. Oral Allergy Syndrome (pollen-food syndrome) was added in v42.6 as an
   addendum inside "Allergic Rhinitis." Per user agreement, it is genuinely a
   distinct, self-contained board entity (its own mechanism, its own
   diagnostic reasoning, its own management logic) the same way Anaphylaxis
   was pulled out of SCIT/SLIT rather than left as an addendum -- so it is
   promoted to its own topic, "Oral Allergy Syndrome (Pollen-Food Syndrome)."
   The seasonal aeroallergen calendar moves with it (it is what predicts the
   culprit food), leaving Allergic Rhinitis focused on AR diagnosis/management
   with a brief cross-reference to OAS.

Also adds one more Clinical Challenge (latex-fruit syndrome discrimination) so
the newly dedicated OAS topic has broader coverage than the original two
birch/ragweed-only vignettes, and repoints all affected Clinical Challenges'
topic/concept_id fields so mastery tracking follows the content to its new home.

Net effect: total topics 348 -> 349 (one new OAS topic; the Anaphylaxis move is
domain-neutral for the total). Rhinology / Allergy / Skull Base 46 -> 48
(+1 Anaphylaxis moved in, +1 new OAS topic). General ENT / Emergencies 36 -> 35
(-1 Anaphylaxis moved out).
"""

import re


ANAPHYLAXIS_OLD_DOMAIN = "General ENT / Emergencies"
ANAPHYLAXIS_NEW_DOMAIN = "Rhinology / Allergy / Skull Base"
OAS_TOPIC = "Oral Allergy Syndrome (Pollen-Food Syndrome)"
AR_TOPIC = "Allergic Rhinitis"
AR_DOMAIN = "Rhinology / Allergy / Skull Base"

MOVE_MARKER = "canonical_domain"

# --- Exact text this module removes from Allergic Rhinitis (added by v42.6) ---

AR_RECOGNIZE_OAS_ADDITION = (
    " SEASONAL AEROALLERGEN CALENDAR (boards pattern-recognition): TREE pollen peaks in SPRING (roughly "
    "February-May depending on region/climate) -- oak, birch, cedar/juniper, maple, elm. GRASS pollen peaks in "
    "LATE SPRING through SUMMER (roughly May-July) -- timothy, Bermuda, Kentucky bluegrass. WEED pollen, "
    "dominated by ragweed, peaks in FALL (roughly August-October, worsening until first frost). MOLD spores "
    "(Alternaria, Cladosporium) are more variable and often peak in warm, damp, or late-summer/fall conditions "
    "and can persist indoors year-round. A patient whose symptoms cluster tightly in one of these windows year "
    "after year is describing a specific pollen family before any testing is done -- use the seasonal history "
    "to predict which panel to test and to anticipate oral allergy syndrome triggers (below)."
)
AR_RECOGNIZE_CROSSREF = (
    " Seasonal timing of symptoms (tree = spring, grass = summer, ragweed = fall) also predicts which pollen "
    "family is responsible and, in turn, which foods may trigger oral allergy syndrome -- see Oral Allergy "
    "Syndrome (Pollen-Food Syndrome)."
)

AR_LOCALIZE_OAS_ADDITION = (
    " ORAL ALLERGY SYNDROME (pollen-food syndrome): pollen-specific IgE can cross-react with structurally "
    "similar, heat-labile plant proteins (commonly PR-10/Bet v1 homologs and profilins) in certain raw fruits, "
    "vegetables, and nuts. Contact with the oral mucosa triggers rapid-onset, LOCALIZED lip/mouth/throat "
    "itching or mild swelling that typically resolves within minutes and rarely progresses to systemic "
    "anaphylaxis, because the causative proteins are usually degraded by cooking, processing, and digestion -- "
    "this is the key discriminator from a true, potentially anaphylactic food allergy (classically to peanut, "
    "tree nut, shellfish, egg, or milk), which is stable to heat/digestion and can cause systemic reactions "
    "with cooked or processed forms of the food."
)
AR_LOCALIZE_CROSSREF = (
    " A subset of allergic-rhinitis patients also report oral itching with specific raw fruits/vegetables; see "
    "Oral Allergy Syndrome (Pollen-Food Syndrome) for the mechanism and management."
)

AR_WORKUP_OAS_ADDITION = (
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

AR_MANAGE_OAS_ADDITION = (
    " Manage oral allergy syndrome by counseling avoidance of the specific RAW trigger foods (cooking/peeling/"
    "canning usually denatures the causative protein and restores tolerance for most patients), reassuring "
    "that systemic reactions are uncommon but can rarely occur (so a first reaction with a new food, throat "
    "tightness, or systemic symptoms should prompt allergy referral and possible epinephrine auto-injector "
    "prescription), and treating the underlying seasonal allergic rhinitis, since better pollen control can "
    "reduce the threshold for oral symptoms."
)

AR_TEACH_OAS_ADDITION = (
    " Boards pearl: a seasonal timing history (tree = spring, grass = summer, weed/ragweed = fall) plus a "
    "reproducible 'raw fruit makes my mouth itch' history is oral allergy syndrome, not a true food allergy -- "
    "match the fruit family to the pollen (birch-apple, ragweed-melon/banana, mugwort-celery-spice) rather than "
    "reflexively ordering food-allergy panels or restricting cooked forms of the food."
)
AR_TEACH_CROSSREF = (
    " If the story includes oral itching with specific raw produce, work it up as Oral Allergy Syndrome "
    "(Pollen-Food Syndrome) rather than a food allergy or a separate rhinitis phenotype."
)

AR_TAGS_TO_REMOVE = ["oral allergy syndrome", "pollen-food syndrome", "seasonal allergens", "birch-apple", "ragweed"]
AR_SOURCE_TO_REMOVE = (
    "AAAAI/ACAAI allergen-immunology teaching on pollen-food (oral allergy) syndrome cross-reactivity patterns "
    "and seasonal aeroallergen timing."
)

# --- New standalone Oral Allergy Syndrome topic ---

OAS_CARD = {
    "topic": OAS_TOPIC,
    "primary_domain": AR_DOMAIN,
    "recognize": (
        "Recognize oral allergy syndrome (OAS, also called pollen-food syndrome) from a reproducible history of "
        "rapid-onset, LOCALIZED lip/mouth/throat itching or mild swelling within minutes of eating a specific "
        "RAW fruit, vegetable, or nut, resolving within minutes and rarely progressing beyond the oropharynx. "
        "The trigger foods are predictable from the patient's pollen sensitization: TREE pollen peaks in "
        "SPRING (oak, birch, cedar/juniper, maple, elm), GRASS pollen in LATE SPRING-SUMMER (timothy, Bermuda, "
        "Kentucky bluegrass), WEED pollen (dominated by ragweed) in FALL (worsening until first frost), and "
        "MOLD spores more variably (often warm/damp conditions, persisting indoors year-round). A patient with "
        "seasonal allergic rhinitis who also reports itching with specific raw produce is describing OAS before "
        "any testing is done."
    ),
    "localize": (
        "Localize the mechanism as cross-reactivity, not a separate food-specific sensitization: pollen-specific "
        "IgE recognizes structurally similar, HEAT-LABILE plant proteins (commonly PR-10/Bet v1 homologs and "
        "profilins) present in certain raw foods. Because these proteins are degraded by cooking, processing, "
        "and digestion, reactions are essentially limited to raw forms and to the oral mucosa on first contact, "
        "which is the key mechanistic reason OAS rarely becomes systemic -- unlike a true, potentially "
        "anaphylactic food allergy (classically peanut, tree nut, shellfish, egg, or milk), which involves "
        "heat-stable proteins that remain allergenic when cooked and can trigger systemic reactions."
    ),
    "workup": (
        "Match the fruit/vegetable family to the pollen season to identify the likely culprit before testing: "
        "BIRCH -> apple, pear, peach/stone fruits, cherry, kiwi, carrot, celery, hazelnut, almond (Bet v1/PR-10 "
        "homology; classic high-yield pairing is birch-apple). RAGWEED -> melons (cantaloupe, honeydew, "
        "watermelon), banana, cucumber, zucchini (profilin-mediated; classic pairing is ragweed-melon/banana). "
        "GRASS -> tomato, melon, orange, peach. MUGWORT -> celery, carrot, fennel, and spices such as "
        "coriander/anise ('mugwort-celery-spice syndrome'). LATEX-FRUIT SYNDROME is a related but mechanistically "
        "and clinically DISTINCT cross-reactivity pattern (latex allergy with banana, avocado, kiwi, chestnut, "
        "driven by different shared proteins) and carries a higher rate of systemic reactions than classic "
        "pollen-food OAS -- do not conflate the two on boards. Testing is reserved for diagnostic uncertainty or "
        "before advising food reintroduction: skin prick testing with FRESH fruit ('prick-to-prick' testing) "
        "outperforms commercial extracts for these labile proteins, since commercial extracts often degrade the "
        "relevant epitopes during preparation."
    ),
    "manage": (
        "Counsel avoidance of the specific RAW trigger foods; cooking, peeling, canning, or baking usually "
        "denatures the causative protein and restores tolerance for most patients, so blanket food-allergy-style "
        "restriction of cooked/processed forms is unnecessary and overly restrictive. Reassure that systemic "
        "progression is uncommon but can rarely occur -- a first reaction to a new cross-reactive food, any "
        "systemic symptoms (throat tightness, wheeze, hives beyond the mouth, hypotension), or a reaction "
        "pattern resembling latex-fruit syndrome should prompt allergy referral, consideration of an epinephrine "
        "auto-injector prescription, and possibly formal testing rather than reassurance alone. Treating the "
        "patient's underlying seasonal allergic rhinitis can reduce the threshold for oral symptoms during peak "
        "pollen season."
    ),
    "operate": (
        "OAS has no surgical treatment. The ENT's operative role is limited to managing any coexisting airway "
        "concern in the rare systemic reaction (see Anaphylaxis) and to accurately distinguishing OAS from true "
        "food allergy or latex-fruit syndrome before referring for allergy/immunology follow-up, since that "
        "distinction changes counseling and risk stratification rather than any procedural decision."
    ),
    "teach": (
        "Boards pearl: a seasonal pollen history (tree = spring, grass = summer, ragweed = fall) plus a "
        "reproducible 'raw fruit makes my mouth itch' history is oral allergy syndrome, not a true food allergy "
        "-- match the fruit family to the pollen (birch-apple, ragweed-melon/banana, mugwort-celery-spice) "
        "rather than reflexively ordering food-allergy panels or restricting cooked forms of the food. Keep "
        "latex-fruit syndrome mentally separate from pollen-food OAS: different proteins, different pollen "
        "association (none), and a higher systemic-reaction rate."
    ),
    "tags": [
        "oral allergy syndrome", "pollen-food syndrome", "seasonal allergens", "birch-apple", "ragweed",
        "latex-fruit syndrome", "PR-10", "profilin", "cross-reactivity",
    ],
    "source_basis": [
        "AAAAI/ACAAI allergen-immunology teaching on pollen-food (oral allergy) syndrome cross-reactivity "
        "patterns, latex-fruit syndrome, and seasonal aeroallergen timing.",
        "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021), relevant domain chapter and index.",
        "Pasha & Golub, 6e (2022), Ch 1 Allergy and Rhinology, pp 1-74.",
        "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 3, Ch 26-34, pp 479-611.",
    ],
    "evidence_calibrated": "v42.8-review-2026",
    "source_metadata_v408": {
        "canonical_domain": AR_DOMAIN,
        "canonical_topic": OAS_TOPIC,
        "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
        "locator_level": "domain-foundational",
        "reviewed_after": "v42.8",
    },
}

REPOINT_TOPIC_MAP = {
    "v426-allergy-oas-birch-apple-01": OAS_TOPIC,
    "v426-allergy-oas-ragweed-melon-01": OAS_TOPIC,
}
RECOMPUTE_CONCEPT_ID_ONLY = ["v422-allergy-anaphylaxis-01", "v422-allergy-anaphylaxis-02"]


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


CLINICAL_CHALLENGES_NEW = [
    {
        "id": "v428-allergy-oas-latex-fruit-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": OAS_TOPIC,
        "stem": (
            "A healthcare worker with a known latex glove allergy develops lip swelling and hives after eating "
            "avocado, and on a separate occasion develops throat tightness and wheeze after eating banana. How "
            "does this pattern differ from classic pollen-food (birch/ragweed) oral allergy syndrome?"
        ),
        "choices": [
            "It is mechanistically identical to pollen-food OAS and should be managed the same way",
            "It is latex-fruit syndrome, a distinct cross-reactivity pattern (not pollen-driven) that carries a "
            "higher risk of systemic reactions than classic pollen-food OAS",
            "It indicates the patient has developed a new pollen sensitization, most likely to ragweed",
            "It confirms hereditary angioedema rather than any IgE-mediated process",
        ],
        "answer": 1,
        "explanation": (
            "Latex-fruit syndrome is a distinct cross-reactivity pattern between latex proteins and certain "
            "fruits (classically banana, avocado, kiwi, chestnut) that is NOT pollen-driven and carries a "
            "meaningfully higher rate of systemic reactions (throat tightness, wheeze, hypotension) than "
            "classic pollen-food oral allergy syndrome, which is why it should be kept mentally and clinically "
            "separate from birch/ragweed-type OAS."
        ),
        "why_wrong": [
            "The higher systemic-reaction rate and non-pollen mechanism make latex-fruit syndrome clinically "
            "distinct from classic pollen-food OAS, not identical in risk or management.",
            "Correct.",
            "This pattern is not predicted by a pollen season and is not evidence of new aeroallergen "
            "sensitization; it tracks with latex sensitization instead.",
            "Hereditary angioedema does not follow a reproducible specific-food and latex-sensitization "
            "pattern and does not present with hives/wheeze in this IgE-mediated fashion.",
        ],
        "board_pearl": "Latex-fruit syndrome (banana, avocado, kiwi, chestnut) is a separate, higher-systemic-"
        "risk cross-reactivity pattern from pollen-food OAS -- do not conflate the two on boards.",
        "curveball": "What should this patient be counseled to carry, given the systemic reaction to banana?",
        "curveball_answer": (
            "Given a systemic reaction (throat tightness, wheeze) to a cross-reactive food, this patient should "
            "be referred to allergy/immunology and prescribed an epinephrine auto-injector, since latex-fruit "
            "syndrome carries a real risk of more significant reactions than typical localized pollen-food OAS."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
]


def apply_allergy_domain_consolidation_v428(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    result = {"anaphylaxis_moved": False, "oas_split": False, "challenges_added": [], "challenges_repointed": []}

    # 1. Move Anaphylaxis into the allergy domain.
    old_bucket = modules.get(ANAPHYLAXIS_OLD_DOMAIN, [])
    anaphylaxis_row = next((r for r in old_bucket if r.get("topic") == "Anaphylaxis"), None)
    if anaphylaxis_row is not None:
        old_bucket[:] = [r for r in old_bucket if r.get("topic") != "Anaphylaxis"]
        modules[ANAPHYLAXIS_OLD_DOMAIN] = old_bucket
        anaphylaxis_row["primary_domain"] = ANAPHYLAXIS_NEW_DOMAIN
        metadata = anaphylaxis_row.get("source_metadata_v408")
        if isinstance(metadata, dict):
            metadata["canonical_domain"] = ANAPHYLAXIS_NEW_DOMAIN
            metadata["reviewed_after"] = "v42.8"
        new_bucket = modules.setdefault(ANAPHYLAXIS_NEW_DOMAIN, [])
        if not any(r.get("topic") == "Anaphylaxis" for r in new_bucket):
            new_bucket.append(anaphylaxis_row)
        result["anaphylaxis_moved"] = True

    # 2. Split Oral Allergy Syndrome out of Allergic Rhinitis.
    rhinology = modules.get(AR_DOMAIN, [])
    ar_row = next((r for r in rhinology if r.get("topic") == AR_TOPIC), None)
    if ar_row is not None and AR_RECOGNIZE_OAS_ADDITION in (ar_row.get("recognize") or ""):
        ar_row["recognize"] = (ar_row.get("recognize") or "").replace(AR_RECOGNIZE_OAS_ADDITION, AR_RECOGNIZE_CROSSREF)
        ar_row["localize"] = (ar_row.get("localize") or "").replace(AR_LOCALIZE_OAS_ADDITION, AR_LOCALIZE_CROSSREF)
        ar_row["workup"] = (ar_row.get("workup") or "").replace(AR_WORKUP_OAS_ADDITION, "")
        ar_row["manage"] = (ar_row.get("manage") or "").replace(AR_MANAGE_OAS_ADDITION, "")
        ar_row["teach"] = (ar_row.get("teach") or "").replace(AR_TEACH_OAS_ADDITION, AR_TEACH_CROSSREF)
        ar_row["tags"] = [t for t in (ar_row.get("tags") or []) if t not in AR_TAGS_TO_REMOVE]
        ar_row["source_basis"] = [s for s in (ar_row.get("source_basis") or []) if s != AR_SOURCE_TO_REMOVE]

        if not any(r.get("topic") == OAS_TOPIC for r in rhinology):
            rhinology.append(dict(OAS_CARD))
        modules[AR_DOMAIN] = rhinology
        result["oas_split"] = True

    # 3. Repoint / recompute Clinical Challenge concept ids so mastery tracking follows the content.
    topic_domains = {
        card.get("topic"): domain
        for domain, cards in modules.items()
        for card in cards
        if card.get("topic")
    }
    challenges = data_module.CLINICAL_CHALLENGES_V119
    for q in challenges:
        qid = q.get("id")
        if qid in REPOINT_TOPIC_MAP:
            new_topic = REPOINT_TOPIC_MAP[qid]
            if q.get("topic") != new_topic:
                q["topic"] = new_topic
                canonical_domain = topic_domains.get(new_topic)
                if canonical_domain is not None:
                    q["concept_id"] = _v6_item_id(canonical_domain, new_topic)
                result["challenges_repointed"].append(qid)
        elif qid in RECOMPUTE_CONCEPT_ID_ONLY:
            canonical_domain = topic_domains.get(q.get("topic"))
            if canonical_domain is not None:
                new_concept_id = _v6_item_id(canonical_domain, q.get("topic"))
                if q.get("concept_id") != new_concept_id:
                    q["concept_id"] = new_concept_id
                    result["challenges_repointed"].append(qid)

    existing_ids = {q.get("id") for q in challenges}
    for q in CLINICAL_CHALLENGES_NEW:
        if q["id"] in existing_ids:
            continue
        row = dict(q)
        canonical_domain = topic_domains.get(row["topic"])
        if canonical_domain is None:
            raise RuntimeError(f"v42.8: challenge topic missing from curriculum: {row['topic']}")
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
