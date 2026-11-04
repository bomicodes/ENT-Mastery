"""v63.0: OR Tomorrow card for inferior turbinate reduction.

"Inferior Turbinate Hypertrophy" used to be cross-referenced to the septoplasty card, but
that card never covers turbinate surgery. This adds a dedicated card, written from the
Deep Curriculum topic, and moves the topic onto it (or_merge_v610 merges the topic into
this card). The septoplasty card links here for combined cases. Installed before or_merge_v610.
"""

SLUG = "inferior-turbinate-reduction"
TOPIC = "Inferior Turbinate Hypertrophy"

CARD_V630 = {
    "title": "Inferior Turbinate Reduction",
    "domain": "Rhinology",
    "linked_topic": TOPIC,
    "or_family_v190": "nasal",
    "indications": (
        "Nasal obstruction from inferior turbinate hypertrophy that persists despite an adequate medical trial "
        "(intranasal steroid with correct technique, treatment of allergic or other rhinitis, and stopping topical "
        "decongestant overuse), where exam confirms the turbinate is a meaningful contributor rather than the nasal "
        "valve or septum alone. Often combined with septoplasty when both contribute. Rhinitis symptoms such as "
        "rhinorrhea, sneezing and itching are not an indication for turbinate reduction by themselves. Document a NOSE score; CPAP intolerance from nasal obstruction is another reason to treat."
    ),
    "setup": [
        "Confirm the obstruction source on exam before and after topical decongestion: a turbinate that shrinks well is mucosal and suits submucosal techniques; one that stays bulky has a bony or fixed soft-tissue component. Check the internal and external nasal valve and the septum so the operation matches the problem.",
        "Look for rhinitis medicamentosa (topical decongestant overuse) and treat it first; surgery does not fix rebound congestion while the spray continues.",
        "Ask about prior turbinate surgery, crusting or dryness, and any sense of obstruction out of proportion to exam; a history of aggressive prior reduction is a reason for caution, not more resection.",
        "Choose the technique by tissue type: radiofrequency or coblation submucosal reduction for mucosal hypertrophy (often office-based), microdebrider-assisted submucosal reduction for larger soft-tissue bulk, and submucous resection of bone with lateral outfracture when the bone is enlarged or medialized.",
        "Review antithrombotics and bleeding history. The inferior turbinate artery (from the posterior lateral nasal branch of the sphenopalatine artery) enters near the posterior attachment, within about 1 cm of the tail, and runs forward along the lateral side of the bone; the tail is the usual source of delayed bleeding.",
        "Children: the cause is usually allergic rhinitis, so maximize medical therapy first; turbinate reduction is often combined with adenoidectomy when adenoids also contribute. Use mucosa- and bone-sparing submucosal techniques only, and avoid resection or turbinectomy.",
        "Topical vasoconstrictor pledgets and local anesthetic infiltration of the anterior head and along the turbinate, aspirating before injecting because the turbinate is very vascular, with time allowed for vasoconstriction. Tell anesthesia which vasoconstrictor is used: hypertension after topical phenylephrine or oxymetazoline should not be treated with beta-blockers (risk of acute heart failure). Do not inject particulate steroid into the turbinate (embolic vision loss has been reported).",
    ],
    "landmarks": [
        "anterior head of the inferior turbinate, part of the internal nasal valve with the septum, caudal upper lateral cartilage and nasal floor; bulk here matters most for airflow, and it is the entry point for submucosal instruments",
        "inferior turbinate bone and its lateral attachment to the maxillary and palatine bones",
        "inferior meatus and the Hasner valve (nasolacrimal duct opening), about 1 cm behind the anterior tip under the anterior third; keep bone work there medial and superior to the meatus",
        "posterior tail of the inferior turbinate near the choana and eustachian tube orifice",
        "posterior lateral wall, where branches of the sphenopalatine artery supply the turbinate",
    ],
    "steps": [
        "Decongest and inject, then examine endoscopically to confirm which part of the turbinate (head, body, tail) is obstructing.",
        "Submucosal reduction (radiofrequency or coblation): insert the probe at the anterior head into the submucosa, apply energy in several passes along the medial and inferior submucosa of the head and body. Make sure the whole active electrode, past the insulation, is submucosal before energizing, and do not deliver energy at the entry point or against bone.",
        "Microdebrider-assisted submucosal reduction: make a small incision on the anterior head, raise a submucosal pocket with an elevator, and resect submucosal stroma (and bone if needed) with the blade facing the bone and away from the mucosa.",
        "Submucous resection of bone when the bone is enlarged: incise the anterior head, elevate mucoperiosteum off the bone medially and laterally, and remove the enlarged bone while keeping the mucosal flap intact (the inferior turbinoplasty described by Mabry is a variant that also trims lateral mucosa and rolls the medial flap over the raw surface).",
        "Lateral outfracture: with a Boies elevator or similar, medialize then fracture the turbinate laterally toward the lateral wall to widen the airway. Outfracture alone tends to recoil, so it is most durable combined with a submucosal technique.",
        "Reserve partial resection (for example of a hypertrophic posterior tail) for tissue that will not respond to submucosal reduction, and remove only the obstructing portion with endoscopic control of the cut edge.",
        "Inspect for bleeding, especially posteriorly, and cauterize any bleeding point; decide on packing or splints (often none, or a light dissolvable dressing).",
    ],
    "danger": [
        "Over-resection of turbinate mucosa or bone: risks empty nose syndrome (paradoxical obstruction despite a wide airway), chronic crusting and dryness. Reduce bulk; do not remove the turbinate.",
        "Mucosal surface burns or stripping from radiofrequency or debrider use near the surface: causes crusting, synechiae and loss of function.",
        "Posterior bleeding from the inferior turbinate artery near the tail, which can be brisk and delayed.",
        "Injury to the nasolacrimal duct opening in the inferior meatus during aggressive anterior work.",
        "Synechiae between the turbinate and the septum, especially when septoplasty is done in the same case and both surfaces are raw.",
    ],
    "exit_check": [
        "Airway is improved on endoscopy without exposed bone or large raw surfaces.",
        "No active bleeding, including the posterior tail; nasopharynx clear of blood.",
        "If septoplasty was also done, septum is midline and splints or dressings are placed to separate raw septal and turbinate surfaces.",
    ],
    "postop": [
        "Saline sprays or irrigations and humidification during healing; expect congestion and crusting for 1 to 3 weeks before improvement, especially after radiofrequency, whose results mature over about 6 to 8 weeks.",
        "Avoid nose blowing, straining and heavy lifting for about a week; resume antithrombotics when the operating surgeon and prescriber agree. If non-absorbable packing is used, counsel on toxic shock signs (fever, rash, hypotension) and remove it on schedule.",
        "Bleeding precautions: anterior oozing usually settles with pressure and oxymetazoline; persistent or posterior bleeding needs evaluation and may need cautery, packing or return to the OR.",
        "Clinic endoscopy to debride crusts and break early synechiae, and continue treatment of the underlying rhinitis, since surgery does not cure it.",
    ],
    "complications": {
        "early": [
            "Bleeding, including delayed posterior bleeding from the inferior turbinate artery.",
            "Crusting and prolonged congestion during healing.",
            "Synechiae, especially with concurrent septoplasty.",
        ],
        "late": [
            "Recurrent hypertrophy; radiofrequency and coblation results may fade over years more than microdebrider or bony reduction, but repeat treatment is simple.",
            "Atrophic rhinitis, chronic dryness and crusting after aggressive resection.",
            "Empty nose syndrome after excessive tissue removal.",
            "Epiphora from nasolacrimal duct injury (rare).",
        ],
    },
    "attending_followup": [
        ["How do you decide whether the turbinate or the septum is causing the obstruction?",
         "Examine before and after topical decongestion: a turbinate that shrinks well is reversible mucosal swelling; a septal deflection or valve collapse does not change. Test the valve with a Cottle or modified Cottle maneuver, and remember turbinate hypertrophy is often compensatory on the side opposite a septal deviation. Many patients have both, which is why turbinate reduction is often paired with septoplasty."],
        ["Which technique would you use for this patient and why?",
         "Match it to the tissue: radiofrequency or coblation for mucosal hypertrophy, microdebrider submucosal reduction for larger soft-tissue bulk, and submucous bone resection with outfracture when the bone is enlarged. All preserve the overlying mucosa."],
        ["Why not just do a total turbinectomy?",
         "The turbinate warms and humidifies air and its mucosa senses airflow. Removing it risks atrophic rhinitis, crusting and empty nose syndrome, and more tissue removed does not reliably mean more relief."],
        ["What is empty nose syndrome?",
         "A sensation of obstruction or suffocation despite a widely patent airway after turbinate tissue loss, thought to come from losing mucosal airflow sensing. It is hard to treat, so prevention by conservative reduction is the key."],
        ["How would you work up suspected empty nose syndrome?",
         "Use the ENS6Q questionnaire and the cotton test (cotton placed where turbinate is missing should relieve symptoms), image the turbinate remnant, and screen for anxiety and depression, which are common in these patients."],
        ["Where does postoperative turbinate bleeding come from?",
         "Usually the inferior turbinate artery, a branch of the posterior lateral nasal artery (sphenopalatine system) that enters near the tail and runs forward along the bone, so persistent bleeding after turbinate surgery is often posterior."],
    ],
    "antibiotics": {
        "indicated": "Not routinely indicated",
        "regimen": "No routine perioperative antibiotic for turbinate reduction. If non-absorbable packing or splints are left in place, follow institutional protocol for coverage while they stay in.",
        "rationale": "Turbinate surgery is a clean-contaminated nasal procedure with a low infection rate, and the evidence does not support routine prophylaxis; any use is tied to a packing practice. Confirm against institutional protocol.",
    },
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — nasal obstruction, septoplasty and inferior turbinate surgery.",
        "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Rhinology: nasal obstruction and turbinate hypertrophy.",
        "K.J. Lee's Essential Otolaryngology, 12e — nasal obstruction and turbinate reduction.",
        "Seidman MD, Gurgel RK, Lin SY, et al. Clinical Practice Guideline: Allergic Rhinitis. Otolaryngol Head Neck Surg. 2015;152(1 Suppl):S1-S43 (Statement 12, option: inferior turbinate reduction may be offered for allergic rhinitis with nasal airway obstruction and enlarged inferior turbinates that fail medical management).",
        "Han JK, Stringer SP, Rosenfeld RM, et al. Clinical Consensus Statement: Septoplasty with or without Inferior Turbinate Reduction. Otolaryngol Head Neck Surg. 2015;153(5):708-720 (PMID 26527752).",
    ],
}

SEE_ALSO_SEPTOPLASTY = {"slug": SLUG, "label": "Doing turbinates too? → Inferior Turbinate Reduction card"}
SEE_ALSO_TURBINATE = {"slug": "septoplasty", "label": "Doing a septoplasty too? → Septoplasty card"}


def install_or_cards_v630(data, app_mod):
    import textbook_curriculum_v470
    registry = data.OR_PREP_REGISTRY
    if SLUG not in registry:
        c = {k: (list(v) if isinstance(v, list) else dict(v) if isinstance(v, dict) else v) for k, v in CARD_V630.items()}
        c["attending_followup"] = [list(p) for p in CARD_V630["attending_followup"]]
        c["complications"] = {k: list(v) for k, v in CARD_V630["complications"].items()}
        c.update({"slug": SLUG, "status": "authored-v63.0", "review_status_v190": "operative-depth reviewed",
                  "sequence_status_v200": "procedure-specific", "sources": list(CARD_V630["source_basis"]),
                  "see_also_v630": [dict(SEE_ALSO_TURBINATE)]})
        registry[SLUG] = c
    sep = registry.get("septoplasty")
    if sep is not None:
        sa = sep.setdefault("see_also_v630", [])
        if not any(x.get("slug") == SLUG for x in sa):
            sa.append(dict(SEE_ALSO_SEPTOPLASTY))
    # The turbinate topic now belongs to this card, not septoplasty.
    textbook_curriculum_v470.TOPIC_OR_MAP_V470[TOPIC] = [SLUG]
    if getattr(app_mod, "OR_PREP_REGISTRY", None) is not registry:
        app_mod.OR_PREP_REGISTRY = registry
    return {"added": [SLUG]}
