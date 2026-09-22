"""v42.2: allergy/anaphylaxis deep dive requested 2026-09-21.

Adds a dedicated Anaphylaxis topic (recognition, weight-based epinephrine
dosing/timing, vasovagal-syncope differential, biphasic-reaction observation
windows -- none of which existed anywhere in the curriculum; the only prior
mentions of anaphylaxis were safety-preparedness asides inside the SCIT/SLIT
and Angioedema topics), deepens the existing Allergen Immunotherapy -- SCIT /
SLIT topic with the Treg/IL-10/IgG4-blocking-antibody immune-tolerance
mechanism and a structured SCIT-vs-SLIT pros/cons comparison, and adds new
Clinical Challenge vignettes so these four specific areas are actually
quizzed: epinephrine dosing/timing, vasovagal syncope vs anaphylaxis,
IL-10/Treg immunology of immunotherapy, and SCIT vs SLIT tradeoffs.

Epinephrine dosing figures are grounded in the AAAAI/ACAAI 2023 anaphylaxis
practice parameter update and are given as standard teaching ranges rather
than over-precise absolutes (e.g. "commonly repeated every 5-15 minutes")
where the literature itself gives a range rather than one fixed number.
"""
from copy import deepcopy
import re


ANAPHYLAXIS_TOPIC = {
    "topic": "Anaphylaxis",
    "primary_domain": "General ENT / Emergencies",
    "recognize": (
        "Suspect anaphylaxis with acute onset (minutes to a couple of hours) of illness involving skin/mucosa "
        "(urticaria, flushing, angioedema) PLUS respiratory compromise (dyspnea, wheeze, stridor, hypoxia) and/or "
        "hypotension/end-organ dysfunction, or hypotension alone after exposure to a likely allergen (a known "
        "allergen just before a skin test, the build-up/maintenance phase of SCIT, a new medication, food, or "
        "insect sting), or two or more organ systems (skin/mucosa, respiratory, cardiovascular, persistent GI "
        "symptoms) involved after any allergen exposure. Skin/mucosal findings are present in the large majority "
        "of cases but are absent often enough that their absence must never be used to rule anaphylaxis out, "
        "especially when hypotension or airway symptoms follow a clear allergen trigger."
    ),
    "localize": (
        "This is a systemic type I (IgE-mediated) or, less commonly, non-IgE mast-cell/basophil degranulation "
        "process: preformed and newly synthesized mediators (histamine, tryptase, leukotrienes, prostaglandins, "
        "platelet-activating factor) cause vasodilation and increased vascular permeability (hypotension, "
        "flushing, angioedema), bronchoconstriction (wheeze, dyspnea), and increased mucus/GI smooth-muscle "
        "activity (cramping, vomiting, diarrhea) essentially simultaneously across organ systems -- distinct "
        "from a single-organ allergic reaction (isolated urticaria, isolated bronchospasm) and distinct from a "
        "vasovagal (neurocardiogenic) reflex, which is a transient, self-limited autonomic response to pain, "
        "fear, or the sight of a needle rather than mediator release."
    ),
    "workup": (
        "Anaphylaxis is a clinical diagnosis made in real time from the history and exam; do not delay "
        "epinephrine to obtain a tryptase level or wait for laboratory confirmation. A serum tryptase drawn "
        "acutely (roughly 15 minutes to 3 hours after symptom onset) and compared with a baseline level can "
        "support the diagnosis retrospectively, particularly when the presentation was atypical or hypotension "
        "was the dominant feature, but a normal tryptase does not exclude anaphylaxis (especially food-triggered "
        "reactions). The key bedside discriminator from vasovagal syncope is vital signs and associated findings: "
        "anaphylaxis typically produces tachycardia, urticaria/flushing/angioedema, bronchospasm, or persistent "
        "hypotension that does NOT resolve simply by lying the patient flat, while vasovagal syncope classically "
        "produces bradycardia, pallor, diaphoresis, and transient hypotension that resolves promptly with "
        "recumbency/leg elevation and has no urticaria, angioedema, wheeze, or persistent cardiovascular "
        "compromise."
    ),
    "manage": (
        "Epinephrine is first-line and should be given immediately, intramuscularly in the anterolateral thigh "
        "(vastus lateralis), at a standard weight-based dose of 0.01 mg/kg of 1:1000 (1 mg/mL) concentration, to "
        "a maximum single dose of 0.3 mg in children and 0.5 mg in adults; auto-injectors deliver fixed doses "
        "(commonly 0.1 mg, 0.15 mg, or 0.3 mg tiers by weight). If symptoms do not improve, epinephrine is "
        "commonly repeated every 5-15 minutes as needed, and a patient who does not respond after two doses, or "
        "who has refractory hypotension/bronchospasm, needs emergency-level care (IV fluids, oxygen, positioning "
        "supine with legs elevated if tolerated, and consideration of an epinephrine infusion) rather than "
        "escalating doses of second-line agents. Antihistamines and corticosteroids are adjuncts for "
        "cutaneous/itch symptoms and (unproven) theoretical biphasic-reaction prevention respectively -- they do "
        "NOT treat the airway/hemodynamic emergency and must never be substituted for or given before "
        "epinephrine. After stabilization, observe the patient (commonly on the order of several hours, longer "
        "for severe reactions, reactions requiring more than one epinephrine dose, or patients with asthma or "
        "poor access to care) because a biphasic reaction -- recurrence of symptoms without re-exposure, "
        "typically within 8-10 hours but reported up to about 72 hours later -- occurs in a meaningful minority "
        "of cases. Every patient treated for anaphylaxis should be prescribed and taught to use an epinephrine "
        "auto-injector and referred for allergy evaluation before discharge."
    ),
    "operate": (
        "There is no operative treatment for anaphylaxis itself; the otolaryngologist's operative-adjacent role "
        "is airway management when laryngeal edema/angioedema threatens obstruction -- have a low threshold for "
        "early, controlled airway intervention (including surgical airway readiness) if stridor, voice change, "
        "or rapidly progressive oropharyngeal/laryngeal swelling is present, since airway anatomy can become "
        "unsalvageable by direct laryngoscopy or intubation if intervention is delayed. Anyone who performs "
        "allergy skin testing or administers SCIT (a required otolaryngology-office competency) must have "
        "epinephrine, appropriate resuscitation equipment, and a rehearsed anaphylaxis protocol immediately "
        "available, and must observe patients through the standard post-injection window precisely because "
        "office-based immunotherapy is a recognized cause of anaphylaxis."
    ),
    "teach": (
        "BOARD PEARL: epinephrine is never contraindicated in true anaphylaxis, and the most common preventable "
        "error is delaying it while reaching for diphenhydramine or waiting to \"see if it gets worse.\" Learn the "
        "vasovagal-versus-anaphylaxis discriminator cold: bradycardia + pallor + diaphoresis + rapid resolution "
        "with recumbency = vasovagal; tachycardia + urticaria/angioedema/wheeze + persistent hypotension despite "
        "positioning = anaphylaxis, treat with epinephrine. Know the dose by heart: 0.01 mg/kg of 1:1000 IM in "
        "the anterolateral thigh, max 0.3 mg (child) / 0.5 mg (adult), repeat roughly every 5-15 minutes as "
        "needed -- and remember that a reaction can recur hours later (biphasic reaction), which is why "
        "observation and auto-injector prescription at discharge are part of the standard of care, not optional "
        "extras."
    ),
    "tags": ["anaphylaxis", "epinephrine", "vasovagal syncope", "allergy", "emergency", "SCIT safety"],
    "source_basis": [
        "AAAAI/ACAAI/JCAAI Joint Task Force: Anaphylaxis -- A 2023 Practice Parameter Update. Ann Allergy Asthma Immunol. 2023 -- weight-based epinephrine dosing (0.01 mg/kg of 1:1000, max 0.3 mg child/0.5 mg adult), anterolateral-thigh IM route, individualized observation duration, and biphasic-reaction risk/timing.",
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — anaphylaxis recognition and management in the context of allergy testing and immunotherapy safety.",
        "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021), connected Google Drive full-text ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; foundational General ENT / Emergencies section and index (domain-level locator, not a claim-level citation).",
        "Pasha & Golub, 6e (2022), Ch 5 General Otolaryngology, pp 183-248, and Ch 10 Trauma, pp 629-670; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
        "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 1, Ch 1-12, pp 1-233, with relevant Part 4 sections; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    ],
    "evidence_calibrated": "v42.2-review-2026",
    "source_metadata_v408": {
        "canonical_domain": "General ENT / Emergencies",
        "canonical_topic": "Anaphylaxis",
        "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
        "locator_level": "domain-foundational",
        "reviewed_after": "v42.2",
    },
}


SCIT_SLIT_IL10_MARKER = "IL-10"

SCIT_SLIT_LOCALIZE_ADDITION = (
    " IMMUNOLOGIC MECHANISM: successful immunotherapy shifts the response toward tolerance by inducing "
    "allergen-specific regulatory T cells (Treg) that secrete IL-10 and TGF-beta. IL-10 suppresses Th2 cytokine "
    "production, reduces mast cell/basophil and eosinophil activity, and -- critically -- drives a class switch "
    "of allergen-specific B cells away from IgE and toward IgG4 (\"blocking antibody\"), which competes with IgE "
    "for allergen binding and for FcR engagement on effector cells. The clinically relevant takeaway is that "
    "AIT's benefit is a slow, multi-year immunologic remodeling (Treg/IL-10 induction and blocking-antibody "
    "generation) rather than a pharmacologic effect, which is why an adequate course takes years and why "
    "efficacy is judged clinically rather than by serial IgE/skin-test normalization."
)

SCIT_SLIT_MANAGE_ADDITION = (
    " SCIT VERSUS SLIT, side by side: SCIT (subcutaneous) offers the broadest range of available allergens and "
    "the ability to treat polysensitized patients with a mixed extract, and has the longest track record of "
    "efficacy data, but requires monthly in-office injection visits during maintenance, mandatory in-office "
    "post-injection observation, and carries the higher risk of systemic reaction/anaphylaxis of the two routes. "
    "SLIT (sublingual) is self-administered at home after an observed first dose, generally has a more favorable "
    "systemic-reaction safety profile with anaphylaxis being rare, and suits patients who cannot commit to "
    "frequent office visits or who are needle-averse, but in the U.S. only single-allergen FDA-approved tablets "
    "exist (compounded multi-allergen SLIT drops are not FDA-approved for allergic rhinitis), which limits it to "
    "monosensitized or a few dominant allergens, and adherence can be harder to verify with a take-home therapy. "
    "Choose the route with the patient after reviewing efficacy, allergen coverage, visit burden, and safety "
    "profile together -- neither route is universally superior."
)


CLINICAL_CHALLENGES_NEW = [
    {
        "id": "v422-allergy-anaphylaxis-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Anaphylaxis",
        "stem": (
            "A 34-year-old develops diffuse urticaria, lip swelling, wheeze, and a blood pressure of 78/44 mm Hg "
            "twelve minutes after her build-up-phase SCIT injection. She weighs 70 kg. What is the correct "
            "immediate dose and route of epinephrine?"
        ),
        "choices": [
            "0.5 mg IM 1:1000 epinephrine in the anterolateral thigh",
            "0.5 mg IV 1:10,000 epinephrine push",
            "0.3 mg subcutaneous 1:1000 epinephrine in the deltoid",
            "Diphenhydramine 50 mg IM, reserving epinephrine for cardiac arrest",
        ],
        "answer": 0,
        "explanation": (
            "Weight-based dosing is 0.01 mg/kg of 1:1000 (1 mg/mL) epinephrine, capped at 0.5 mg in adults; the "
            "route is intramuscular in the anterolateral thigh, which achieves faster, more reliable peak "
            "plasma concentration than subcutaneous or deltoid IM injection."
        ),
        "why_wrong": [
            "Correct.",
            "IV push epinephrine at resuscitation concentration is reserved for cardiac arrest/refractory shock with hemodynamic monitoring, not first-line anaphylaxis management -- it risks dangerous arrhythmia and hypertension.",
            "Subcutaneous injection and the deltoid site both give slower, less reliable absorption than IM anterolateral thigh dosing.",
            "Antihistamines are an adjunct for itch/urticaria only; they do not treat the airway or hemodynamic emergency and must never be given instead of or before epinephrine.",
        ],
        "board_pearl": "Epinephrine 0.01 mg/kg of 1:1000 IM in the anterolateral thigh (max 0.3 mg child / 0.5 mg adult) is first-line and should never be delayed for antihistamines or steroids.",
        "curveball": "If she does not improve after the first dose, what do you do next and when?",
        "curveball_answer": (
            "Repeat the IM epinephrine dose, commonly at 5-15 minute intervals as needed, while escalating "
            "supportive care (supine positioning with legs elevated if tolerated, supplemental oxygen, IV "
            "fluids for hypotension, and continuous monitoring). A patient who fails to respond after two doses "
            "or has refractory bronchospasm/hypotension needs emergency-level escalation (e.g., an epinephrine "
            "infusion), not simply waiting or substituting a second-line agent for further epinephrine."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v422-allergy-anaphylaxis-02",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Anaphylaxis",
        "stem": (
            "Immediately after a scratch allergy skin test, a needle-phobic 19-year-old becomes pale, diaphoretic, "
            "and briefly loses consciousness. His heart rate is 48 bpm and blood pressure is 82/50 mm Hg; there is "
            "no urticaria, angioedema, or wheeze. He returns to baseline within two minutes of being placed supine "
            "with his legs elevated. What is the most likely diagnosis?"
        ),
        "choices": [
            "Anaphylaxis requiring immediate epinephrine",
            "Vasovagal (neurocardiogenic) syncope",
            "Biphasic anaphylactic reaction",
            "Angioedema from ACE-inhibitor use",
        ],
        "answer": 1,
        "explanation": (
            "Bradycardia, pallor, and diaphoresis that resolve promptly with recumbency/leg elevation, without "
            "any skin/mucosal, respiratory, or persistent cardiovascular findings, is the classic pattern of a "
            "vasovagal reflex triggered by needle/injection anxiety -- not anaphylaxis."
        ),
        "why_wrong": [
            "Anaphylaxis classically produces tachycardia (a compensatory/mediator-driven response) and skin/respiratory findings, and does not resolve simply by lying the patient flat.",
            "Correct.",
            "A biphasic reaction is a recurrence of a prior anaphylactic episode hours later; there is no initial anaphylaxis here to recur.",
            "Angioedema causes localized swelling, not this global vital-sign/autonomic picture, and there is no swelling described.",
        ],
        "board_pearl": "Bradycardia + pallor + diaphoresis + rapid resolution with recumbency = vasovagal syncope; tachycardia + urticaria/angioedema/wheeze + persistent hypotension = anaphylaxis, treat with epinephrine.",
        "curveball": "Why is misdiagnosing vasovagal syncope as anaphylaxis (or vice versa) clinically dangerous in both directions?",
        "curveball_answer": (
            "Treating vasovagal syncope as anaphylaxis exposes the patient to unnecessary epinephrine, which can "
            "cause tachyarrhythmia, hypertension, or anxiety in a patient who did not need it. Conversely, "
            "misreading true anaphylaxis as a simple faint and withholding epinephrine allows airway edema, "
            "bronchospasm, or refractory hypotension to progress unchecked, which is the more dangerous error -- "
            "when the presentation is genuinely ambiguous, the safer default is to treat as anaphylaxis given "
            "epinephrine's wide margin of safety at appropriate doses."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v422-allergy-scit-slit-il10-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Allergen Immunotherapy — SCIT / SLIT",
        "stem": (
            "A patient asks how allergy immunotherapy actually works at the immune level, beyond \"getting used to\" "
            "the allergen. Which mechanism best explains the durable tolerance induced by several years of SCIT "
            "or SLIT?"
        ),
        "choices": [
            "Depletion of all allergen-specific IgE-producing plasma cells by direct cytotoxicity",
            "Induction of allergen-specific regulatory T cells producing IL-10, driving a class switch toward blocking IgG4 antibody",
            "Permanent downregulation of the high-affinity IgE receptor (FcεRI) on mast cells",
            "Competitive saturation of mast cell IgE receptors by the injected allergen itself",
        ],
        "answer": 1,
        "explanation": (
            "Effective immunotherapy induces allergen-specific Treg cells that secrete IL-10 and TGF-beta; IL-10 "
            "suppresses the Th2 response and drives allergen-specific B cells to class-switch from IgE toward "
            "IgG4, a \"blocking antibody\" that competes with IgE for allergen and effector-cell binding."
        ),
        "why_wrong": [
            "Immunotherapy does not work by cytotoxic depletion of plasma cells; it works by shifting the regulatory balance of the immune response.",
            "Correct.",
            "There is no permanent structural downregulation of FcεRI as the primary mechanism described for AIT tolerance.",
            "The allergen itself does not persist to competitively occupy receptors long-term; the durable effect is immunologic (Treg/IL-10/IgG4), not a transient occupancy effect.",
        ],
        "board_pearl": "IL-10 from induced Treg cells is the immunologic hinge of AIT tolerance: it dampens Th2 signaling and switches B cells toward blocking IgG4 rather than IgE.",
        "curveball": "Why does this mechanism explain why AIT efficacy should be judged clinically rather than by repeat allergy testing?",
        "curveball_answer": (
            "Because the therapeutic effect is a slow, multi-year immune remodeling process (Treg induction, "
            "IL-10 production, IgG4 class-switching) rather than elimination of sensitization, a patient can have "
            "clear clinical improvement in symptoms while still showing a positive skin test or detectable "
            "specific IgE; conversely, test results do not reliably track with symptom control. Guidelines "
            "therefore recommend judging AIT success by symptom/medication burden over time, not by serial "
            "retesting."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v422-allergy-scit-vs-slit-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Allergen Immunotherapy — SCIT / SLIT",
        "stem": (
            "A polysensitized adult with severe allergic rhinitis wants disease-modifying therapy but cannot commit "
            "to monthly office visits during a maintenance-injection schedule, and is significantly needle-averse. "
            "Which statement about matching SCIT versus SLIT to this patient is most accurate?"
        ),
        "choices": [
            "SLIT is preferred here, but in the U.S. it is limited to single-allergen FDA-approved tablets, which may not cover this patient's full sensitization profile",
            "SCIT is mandatory in polysensitized patients because SLIT has no evidence of efficacy in this population",
            "SLIT and SCIT are interchangeable and equally cover multi-allergen sensitization with the same FDA approval pathway",
            "SLIT should be avoided entirely in needle-averse patients because it also requires monthly injections",
        ],
        "answer": 0,
        "explanation": (
            "SLIT better fits this patient's visit-burden and needle-aversion constraints, but its major practical "
            "limitation in the U.S. is that only single-allergen FDA-approved tablets exist -- compounded "
            "multi-allergen SLIT drops are not FDA-approved for allergic rhinitis -- so a broadly polysensitized "
            "patient may not be fully covered by an approved SLIT product, whereas SCIT can use a mixed extract "
            "tailored to multiple relevant allergens."
        ),
        "why_wrong": [
            "Correct.",
            "SLIT has demonstrated efficacy for its approved single-allergen indications; the issue for a polysensitized patient is allergen coverage, not a lack of any evidence.",
            "SLIT and SCIT are not interchangeable: SCIT can combine multiple allergens in one extract, while U.S.-approved SLIT tablets are single-allergen products with their own individual FDA indications.",
            "SLIT is self-administered sublingually at home after an observed first dose -- it does not require monthly injections, which is precisely why it suits a needle-averse patient.",
        ],
        "board_pearl": "SCIT covers more allergens and has the longest efficacy track record but demands frequent injection visits and carries the higher systemic-reaction risk; SLIT is home-administered and generally safer systemically but, in the U.S., is limited to single-allergen approved tablets.",
        "curveball": "Which route carries the higher risk of anaphylaxis, and what safety infrastructure does that require regardless of which route is chosen?",
        "curveball_answer": (
            "SCIT carries the higher risk of systemic reaction/anaphylaxis of the two routes, which is why "
            "in-office post-injection observation is mandatory; SLIT's systemic-reaction risk is lower but not "
            "zero. Whichever route is used, the prescribing office must be able to recognize and treat "
            "anaphylaxis immediately -- epinephrine and a rehearsed protocol are a required competency for "
            "anyone administering immunotherapy or performing allergy skin testing, not an optional safeguard."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
]


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


def apply_allergy_anaphylaxis_deep_dive_v422(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    result = {"topic_added": False, "scit_slit_deepened": False, "challenges_added": []}

    bucket = modules.setdefault(ANAPHYLAXIS_TOPIC["primary_domain"], [])
    if not any(x.get("topic") == ANAPHYLAXIS_TOPIC["topic"] for x in bucket):
        bucket.append(deepcopy(ANAPHYLAXIS_TOPIC))
        result["topic_added"] = True

    rhinology = modules.get("Rhinology / Allergy / Skull Base", [])
    for card in rhinology:
        if card.get("topic") == "Allergen Immunotherapy — SCIT / SLIT":
            if SCIT_SLIT_IL10_MARKER not in (card.get("localize") or ""):
                card["localize"] = (card.get("localize") or "").rstrip() + SCIT_SLIT_LOCALIZE_ADDITION
                card["manage"] = (card.get("manage") or "").rstrip() + SCIT_SLIT_MANAGE_ADDITION
                if "IL-10" not in card.get("tags", []):
                    card.setdefault("tags", []).append("IL-10")
                if "Treg" not in card.get("tags", []):
                    card.setdefault("tags", []).append("Treg")
                result["scit_slit_deepened"] = True
            break

    challenges = data_module.CLINICAL_CHALLENGES_V119
    existing_ids = {q.get("id") for q in challenges}
    topic_domains = {
        card.get("topic"): domain
        for domain, cards in modules.items()
        for card in cards
        if card.get("topic")
    }
    for q in CLINICAL_CHALLENGES_NEW:
        if q["id"] in existing_ids:
            continue
        row = dict(q)
        canonical_domain = topic_domains.get(row["topic"])
        if canonical_domain is None:
            raise RuntimeError(f"v42.2: challenge topic missing from curriculum: {row['topic']}")
        row["concept_id"] = _v6_item_id(canonical_domain, row["topic"])
        challenges.append(row)
        existing_ids.add(row["id"])
        result["challenges_added"].append(row["id"])

    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {
        q["id"]: q for q in challenges if q.get("id")
    }
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.CLINICAL_CHALLENGES_V119 = challenges
        app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119
    return result
