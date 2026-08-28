"""v23.18 facial-trauma OR Tomorrow management review.

Adds procedure-selection logic and postoperative rescue to six facial-trauma modules
that remained generic-only. Existing fracture anatomy and operative choreography are
left intact. The v23.19 facial-plastics review is chained through this tail.
"""

from or_facial_plastics_management_v2319 import apply_or_facial_plastics_management_v2319

TARGETS = [
    {
        "slug": "closed-nasal-reduction",
        "title_terms": ("closed", "nasal", "reduction"),
        "setup": [
            "Before closed nasal fracture reduction, document preinjury appearance and nasal airway when possible and distinguish reducible bony displacement from septal fracture, septal hematoma, NOE injury or other midface fracture that requires a different plan. Reduction is usually timed after enough edema subsides for accurate assessment but before fracture consolidation; an urgent septal hematoma should be drained rather than waiting for the elective reduction window.",
        ],
        "postop": [
            "After nasal fracture reduction, worsening obstruction with boggy septal swelling, fever or increasing pain should prompt evaluation for septal hematoma/abscess because cartilage necrosis can produce perforation or saddle deformity. Persistent cosmetic deviation or obstruction after swelling resolves should be reassessed for residual bony displacement, septal injury or nasal-valve dysfunction rather than judged from the immediate postoperative appearance alone.",
        ],
        "marker": "closed_nasal_reduction_management_v2318",
    },
    {
        "slug": "frontal-sinus-trauma",
        "title_terms": ("frontal", "sinus", "fracture"),
        "setup": [
            "Before frontal-sinus fracture surgery, classify the injury by anterior-table displacement, posterior-table injury, nasofrontal outflow-tract involvement, dural/CSF injury and associated intracranial or orbital trauma. Those features—not the diagnosis of frontal fracture alone—drive observation versus anterior-table repair, sinus-preserving intervention, obliteration or cranialization; review thin-cut CT and coordinate neurosurgery when posterior-table/dural injury materially changes the operation.",
        ],
        "postop": [
            "After frontal-sinus trauma repair, persistent clear rhinorrhea, meningismus, severe or progressive headache, neurologic change, fever or wound infection requires evaluation for CSF leak or intracranial complication. Long-term surveillance matters because outflow obstruction or retained mucosa can present years later as frontal mucocele/mucopyocele, pain, swelling or orbital symptoms rather than an immediate postoperative failure.",
        ],
        "marker": "frontal_sinus_trauma_management_v2318",
    },
    {
        "slug": "mandible-orif",
        "title_terms": ("mandible", "orif"),
        "setup": [
            "Before mandible ORIF, define fracture pattern and displacement, dentition, baseline occlusion, open-fracture status, inferior-alveolar/mental nerve function and associated condylar or midface injuries. Establish the target occlusion before rigid fixation and identify teeth in the line of fracture, comminution, bone loss and infection that may alter fixation strategy; airway planning must account for trismus, swelling and the need to reproduce occlusion intraoperatively.",
        ],
        "postop": [
            "After mandible fixation, new malocclusion is a technical warning sign and should not be attributed automatically to swelling. Progressive floor-of-mouth/neck swelling, respiratory difficulty, fever, purulent drainage, plate exposure, increasing mobility or worsening pain should prompt evaluation for airway compromise, infection, nonunion/malunion or hardware failure; document inferior-alveolar/mental nerve function separately from occlusal success.",
        ],
        "marker": "mandible_orif_management_v2318",
    },
    {
        "slug": "noe-orif",
        "title_terms": ("noe", "orif"),
        "setup": [
            "Before NOE fracture repair, determine medial canthal tendon attachment/stability, degree of central fragment comminution, intercanthal distance, nasal projection/support, lacrimal injury and associated orbital, frontal-sinus or skull-base/CSF injury. Restoration of canthal position and central midface projection must be planned from stable reference points before dissection because late telecanthus is difficult to correct after scar maturation.",
        ],
        "postop": [
            "After NOE repair, document medial canthal symmetry/stability, globe findings and nasal projection. Increasing intercanthal distance, new diplopia/visual change, persistent epiphora, clear rhinorrhea, infection or progressive nasal collapse should trigger targeted reassessment for fixation failure, lacrimal injury or occult skull-base complication rather than waiting for routine fracture follow-up.",
        ],
        "marker": "noe_orif_management_v2318",
    },
    {
        "slug": "orbital-floor",
        "title_terms": ("orbital", "floor"),
        "setup": [
            "Before orbital-floor repair, document visual acuity, pupils, extraocular movements/diplopia, globe position, facial sensation and CT-defined defect/entrapment. Differentiate true muscle/soft-tissue entrapment from edema-related motility restriction; pediatric trapdoor entrapment or an oculocardiac reflex can require urgent release, whereas many non-entrapped fractures can be observed until swelling permits a reliable functional/cosmetic assessment.",
        ],
        "postop": [
            "After orbital-floor repair, acute visual decline, new RAPD, severe orbital pain, proptosis or rapidly progressive ophthalmoplegia is an orbital-compartment/optic emergency and requires immediate assessment and decompression when indicated. Persistent diplopia, new restriction, enophthalmos or globe malposition should prompt evaluation for implant position, residual entrapment, edema or scarring rather than assuming all postoperative diplopia is transient.",
        ],
        "marker": "orbital_floor_management_v2318",
    },
    {
        "slug": "zmc-orif",
        "title_terms": ("zmc", "orif"),
        "setup": [
            "Before ZMC ORIF, assess malar projection/width, infraorbital nerve sensation, trismus and occlusion and perform a complete ocular examination when the orbit is involved. Review CT at the zygomaticofrontal, zygomaticomaxillary, arch and sphenozygomatic interfaces plus the orbital floor so reduction restores three-dimensional position rather than simply aligning one accessible buttress.",
        ],
        "postop": [
            "After ZMC fixation, new visual change, proptosis, severe orbital pain or worsening motility is an urgent orbital concern. Once swelling decreases, reassess malar symmetry, globe position/diplopia, mouth opening, occlusion and V2 sensation; persistent flattening, trismus or orbital asymmetry can indicate malreduction even when individual plates appear intact.",
        ],
        "marker": "zmc_orif_management_v2318",
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in target["title_terms"]):
            return slug, op
    return None, None


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_facial_trauma_management_v2318(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v2319 = apply_or_facial_plastics_management_v2319(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v2319": v2319}
