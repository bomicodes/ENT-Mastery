"""v44.2: close the remaining "bucket 6" data-hygiene items from the 2026-09-23 deep
audit (the only bucket left after v43.8-v44.1 closed the content-creation buckets).

Fixes, each verified against the live `runtime_entry_pasha` view before writing:

1. Evidence-catalog citations sitting unused: the 2026 nasal-fracture Practice
   Management Guideline and the AAO-HNSF Bell's Palsy CPG (2013) were added to
   CURRENT_EVIDENCE_CATALOG_V98 but never actually cited in the topics they were meant
   to support. Adds them to "Nasal Fracture"'s and "Facial Nerve
   Reanimation"/"Facial Synkinesis / Static-Dynamic Rehabilitation"'s `source_basis`.

2. OR-prep domain-tag fragmentation: 9 thyroid/parotid/submandibular-salivary
   OR_PREP_REGISTRY entries used 5 different loose domain strings
   ("Thyroid / Endocrine Surgery", "Head & Neck / Salivary", "Salivary", "Endocrine")
   instead of the canonical "Thyroid / Parathyroid / Salivary" that "parathyroidectomy"
   already used (fixed by an earlier patch). Normalizes all 9 to the canonical string,
   and normalizes "pharyngocutaneous-fistula" (a laryngectomy complication, not a
   thyroid/salivary procedure) to canonical "Head & Neck Oncology" instead of the
   loose "Head & Neck".

3. Two genuinely missing OR-prep cards, confirmed absent by name-and-synonym search
   (cricotracheal resection and pediatric/cleft LTR already exist; adult
   laryngotracheal reconstruction and maxillomandibular advancement do not):
   "Adult Laryngotracheal Reconstruction" (linked to the existing "Subglottic /
   Tracheal Stenosis" Laryngology topic) and "Maxillomandibular Advancement" (linked
   to the existing "Maxillomandibular Advancement" Sleep Surgery topic).

4. Sialolithiasis question-bank mislabel: 2 Concept Checks and 2 Clinical Challenges
   were authored under the stale topic label "Submandibular Sialolithiasis" instead of
   the canonical "Sialolithiasis" topic, splitting what should be one concept into two
   concept_id buckets. Live check found this was a partial gap, not a total one (4
   Clinical Challenges and 2 Concept Checks already carried the correct label) --
   consolidates the 4 mislabeled entries onto the canonical topic/concept_id so
   mastery tracking and topic-filtered browsing see one concept, not two.

5. The "Croup vs Epiglottitis" comparison card carried `aliases: ['Epiglottitis']`,
   which is a real collision risk with the standalone "Epiglottitis" disease-management
   topic (confirmed these are legitimately distinct, complementary cards, not
   duplicates -- the comparison card's own `teach` text explicitly distinguishes them).
   Removes the incorrect self-aliasing.

6. "Severe Epistaxis" was a stray Clinical Challenge topic-tag variant with no matching
   canonical topic (canonical topics are "Epistaxis" and "Epistaxis Surgical Control").
   Renames the 1 affected Clinical Challenge to canonical "Epistaxis". (A broader scan
   found 78 non-exact Clinical Challenge topic labels, but most are intentional
   sub-case labels rather than bugs -- only this one and the Sialolithiasis case above
   were confirmed as actual mislabels worth fixing.)

7. "Carotid Blowout Syndrome" cited 'NCCN Head & Neck v2.2026' in `source_basis` while
   its own `teach` field explicitly states the classification "comes from
   vascular/interventional literature, not an NCCN head-and-neck staging algorithm" --
   a direct self-contradiction. Removes the mismatched NCCN citation (the topic
   retains its Cummings/Pasha/K.J. Lee core-textbook citations and its actual
   vascular-literature citation, so this does not create a missing-source regression).

The stale Rhinology/Allergy/Skull Base topic-count gate in
audit_rhinology_allergy_source_semantic_v349.py (hardcoded 42, live domain is 48; a
pre-existing issue unrelated to any v43.x/v44.x change, confirmed via `git stash` to
already fail before this patch) is fixed by a direct one-line edit to that file
alongside this module, following the same convention used for
EXPECTED_DOMAIN_COUNTS in audit_all_topic_source_saturation_v368.py.
"""

EVIDENCE_CITATION_ADDITIONS_V442 = {
    ("Facial Plastics / Trauma", "Nasal Fracture", "source_basis"): (
        "Acute Management of Nasal Bone Fractures",
        "Acute Management of Nasal Bone Fractures: A Systematic Review and Practice Management Guideline (2026).",
    ),
    ("Facial Plastics / Trauma", "Facial Nerve Reanimation", "source_basis"): (
        "AAO-HNSF Clinical Practice Guideline: Bell's Palsy",
        "AAO-HNSF Clinical Practice Guideline: Bell's Palsy (2013).",
    ),
    ("Facial Plastics / Trauma", "Facial Synkinesis / Static-Dynamic Rehabilitation", "source_basis"): (
        "AAO-HNSF Clinical Practice Guideline: Bell's Palsy",
        "AAO-HNSF Clinical Practice Guideline: Bell's Palsy (2013).",
    ),
}

OR_PREP_DOMAIN_NORMALIZATIONS_V442 = {
    "thyroid-lobectomy": "Thyroid / Parathyroid / Salivary",
    "total-thyroidectomy": "Thyroid / Parathyroid / Salivary",
    "parotidectomy": "Thyroid / Parathyroid / Salivary",
    "submandibular-gland": "Thyroid / Parathyroid / Salivary",
    "sialendoscopy": "Thyroid / Parathyroid / Salivary",
    "reop-thyroid": "Thyroid / Parathyroid / Salivary",
    "four-gland": "Thyroid / Parathyroid / Salivary",
    "reop-parathyroid": "Thyroid / Parathyroid / Salivary",
    "parotid-total": "Thyroid / Parathyroid / Salivary",
    "pharyngocutaneous-fistula": "Head & Neck Oncology",
}

NEW_OR_PREP_ENTRIES_V442 = {
    "adult-ltr": {
        "slug": "adult-ltr",
        "title": "Adult Laryngotracheal Reconstruction",
        "domain": "Laryngology / Voice / Swallowing",
        "indications": (
            "Adult subglottic or tracheal stenosis where expanding the airway "
            "framework with cartilage grafting is a better fit than segmental "
            "resection -- generally shorter-segment, lower-grade, or anatomically "
            "unfavorable-for-resection stenosis, or a patient who is not a "
            "cricotracheal resection candidate."
        ),
        "setup": [
            "Characterize the stenosis precisely with endoscopy and imaging before "
            "the OR: length, grade, location relative to the vocal folds, "
            "circumferential extent, and posterior glottic/cricoid plate involvement "
            "determine whether expansion (LTR) or resection (CTR) is the better fit, "
            "and which graft strategy (anterior only vs anterior and posterior) is "
            "needed.",
            "Confirm airway control planning (existing tracheostomy, anticipated "
            "staged vs single-stage approach, stenting strategy) and counsel on "
            "realistic decannulation/voice expectations before proceeding.",
        ],
        "landmarks": ["glottis/posterior commissure", "subglottis/cricoid", "recurrent laryngeal nerves", "tracheostomy tract if present", "costal cartilage donor site (if autologous graft planned)"],
        "steps": [
            "Expose the airway framework and define the full extent of the stenosis "
            "before committing to a graft plan.",
            "Incise the stenotic segment (anterior, or anterior and posterior for "
            "circumferential/posterior glottic disease) and harvest and shape a "
            "cartilage graft (commonly costal) to expand the lumen.",
            "Secure the graft, assess the resulting lumen endoscopically, and decide "
            "single-stage closure versus staged reconstruction with a stent based on "
            "the airway's stability and the extent of grafting performed.",
        ],
        "danger": ["Recurrent laryngeal nerve", "Posterior cricoid plate/esophagus", "Graft extrusion or displacement", "Restenosis/granulation"],
        "exit_check": [
            "Reassess the lumen endoscopically and document graft position, mucosal "
            "coverage, and stent placement (if used) before leaving the OR.",
            "Make the extubation, staged intubation, or tracheostomy plan explicit "
            "based on how much of the airway was reconstructed and how stable it "
            "appears.",
        ],
        "complications": {
            "early": [
                "Airway obstruction from edema, graft malposition, or bleeding.",
                "Graft extrusion, infection, or stent-related mucosal injury.",
            ],
            "late": [
                "Restenosis, granulation tissue, graft resorption/collapse, "
                "dysphonia, or failure to decannulate.",
            ],
        },
        "postop": [
            "New stridor, subcutaneous emphysema, voice change, or respiratory "
            "distress after LTR should raise concern for graft displacement, edema, "
            "or restenosis, and warrants prompt airway re-evaluation rather than "
            "reassurance.",
            "Avoid repeated traumatic instrumentation near the reconstruction and "
            "coordinate any re-intervention with the airway surgery team.",
        ],
        "attending_followup": [
            ["Why choose LTR over CTR here?", "LTR expands the existing framework with grafting rather than resecting and reanastomosing it, which fits shorter-segment or lower-grade stenosis, or anatomy less favorable for a tension-free anastomosis."],
            ["What determines single-stage versus staged reconstruction?", "The extent of grafting, airway stability, and mucosal coverage achieved -- more extensive circumferential or posterior grafting more often needs staged management with a stent."],
            ["What threatens the graft?", "Malposition, infection, mechanical stress from ongoing instrumentation, and inadequate mucosal coverage."],
        ],
        "linked_topic": "Subglottic / Tracheal Stenosis",
        "status": "v44.2 added",
        "or_family_v190": "adult_airway",
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — laryngotracheal reconstruction, adult airway stenosis management.",
            "Operative Otolaryngology—Head and Neck Surgery, 3rd ed. — LTR technique and graft selection.",
        ],
    },
    "mma": {
        "slug": "mma",
        "title": "Maxillomandibular Advancement",
        "domain": "Sleep Surgery",
        "indications": (
            "Moderate-to-severe OSA in a patient who has failed or cannot tolerate "
            "PAP therapy, particularly with a skeletal (retrognathic/hypoplastic) "
            "component to their airway obstruction, or as a component of "
            "multilevel/staged surgical planning."
        ),
        "setup": [
            "Confirm sleep-study severity and PAP failure/intolerance, and obtain "
            "cephalometric/3D imaging to characterize the maxillomandibular "
            "skeletal relationship before planning the advancement.",
            "Coordinate with oral/maxillofacial surgery for combined planning "
            "(osteotomy design, occlusal plan, fixation strategy) since this is "
            "typically performed as a joint procedure.",
        ],
        "landmarks": ["maxilla", "mandibular body/ramus", "occlusal plane", "genial tubercle", "inferior alveolar nerve"],
        "steps": [
            "Perform Le Fort I osteotomy of the maxilla and bilateral sagittal "
            "split osteotomy of the mandible.",
            "Advance both the maxilla and mandible (commonly 10 mm or more) to "
            "enlarge the retropalatal and retrolingual airway, and secure a "
            "planned occlusion.",
            "Achieve rigid fixation and confirm a stable, planned bite before "
            "closing.",
        ],
        "danger": ["Inferior alveolar nerve", "Tooth roots", "Malocclusion from imprecise fixation", "Airway compromise from postoperative edema/bleeding"],
        "exit_check": [
            "Confirm the planned occlusion and stable fixation before leaving the "
            "OR.",
            "Assess the airway for edema/bleeding risk and make an explicit "
            "extubation-timing decision given the combined maxillary and "
            "mandibular surgery.",
        ],
        "complications": {
            "early": [
                "Airway edema/bleeding, malocclusion, or hardware-related issues.",
            ],
            "late": [
                "Nonunion, relapse of advancement, chronic paresthesia (inferior "
                "alveolar nerve), or temporomandibular joint symptoms.",
            ],
        },
        "postop": [
            "Monitor the airway closely in the immediate postoperative period given "
            "combined jaw surgery and soft-tissue edema, and confirm occlusion "
            "stability at follow-up before assuming the advancement is durable.",
        ],
        "attending_followup": [
            ["Why does MMA work for OSA when it isn't a soft-tissue procedure?", "Advancing the skeletal framework pulls forward the soft-tissue attachments (palate, tongue base) that cause retropalatal and retrolingual collapse, enlarging the airway at both levels simultaneously."],
            ["Who is the best MMA candidate?", "Patients with PAP failure/intolerance and a retrognathic or otherwise favorable skeletal pattern, or those already planned for combined/staged sleep surgery."],
        ],
        "linked_topic": "Maxillomandibular Advancement",
        "status": "v44.2 added",
        "or_family_v190": "sleep_surgery",
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — maxillomandibular advancement for OSA.",
            "Pasha & Golub, 6e (2022), Sleep Surgery chapter.",
        ],
    },
}

SIALOLITHIASIS_TOPIC_FIX_V442 = {
    "old_topic": "Submandibular Sialolithiasis",
    "new_topic": "Sialolithiasis",
    "old_concept_id": "v6-thyroid-parathyroid-salivary-submandibular-sialolithiasis",
    "new_concept_id": "v6-thyroid-parathyroid-salivary-sialolithiasis",
}

CAROTID_BLOWOUT_STALE_CITATION_V442 = "NCCN Head & Neck v2.2026"


def apply_bucket6_data_hygiene_v442(data_module, app_module=None):
    result = {
        "evidence_citations_added": 0,
        "or_prep_domains_normalized": 0,
        "or_prep_entries_added": 0,
        "sialolithiasis_entries_fixed": 0,
        "aliases_fixed": 0,
        "clinical_challenge_tags_fixed": 0,
        "carotid_blowout_citation_fixed": 0,
    }

    deep = data_module.DEEP_MODULES_V6
    for (domain, topic, field), (marker, citation) in EVIDENCE_CITATION_ADDITIONS_V442.items():
        for row in deep.get(domain, []):
            if row.get("topic") == topic:
                sources = row.get(field) or []
                if not any(marker in str(s) for s in sources):
                    sources.append(citation)
                    row[field] = sources
                    result["evidence_citations_added"] += 1
                break

    or_prep = data_module.OR_PREP_REGISTRY
    for slug, new_domain in OR_PREP_DOMAIN_NORMALIZATIONS_V442.items():
        entry = or_prep.get(slug)
        if entry is not None and entry.get("domain") != new_domain:
            entry["domain"] = new_domain
            result["or_prep_domains_normalized"] += 1
    for slug, entry in NEW_OR_PREP_ENTRIES_V442.items():
        if slug not in or_prep:
            or_prep[slug] = dict(entry)
            result["or_prep_entries_added"] += 1
    data_module.OR_PREP_REGISTRY = or_prep
    if app_module is not None:
        app_module.OR_PREP_REGISTRY = or_prep

    fix = SIALOLITHIASIS_TOPIC_FIX_V442
    for q in data_module.CONCEPT_CHECKS_V112:
        if q.get("topic") == fix["old_topic"]:
            q["topic"] = fix["new_topic"]
            q["concept_id"] = fix["new_concept_id"]
            result["sialolithiasis_entries_fixed"] += 1
    data_module.CONCEPT_CHECK_BY_ID_V112 = {q["id"]: q for q in data_module.CONCEPT_CHECKS_V112 if q.get("id")}
    for c in data_module.CLINICAL_CHALLENGES_V119:
        if c.get("topic") == fix["old_topic"]:
            c["topic"] = fix["new_topic"]
            if c.get("concept_id") == fix["old_concept_id"]:
                c["concept_id"] = fix["new_concept_id"]
            result["sialolithiasis_entries_fixed"] += 1
        elif c.get("topic") == "Severe Epistaxis":
            c["topic"] = "Epistaxis"
            result["clinical_challenge_tags_fixed"] += 1
    if app_module is not None:
        app_module.CONCEPT_CHECKS_V112 = data_module.CONCEPT_CHECKS_V112
        app_module.CONCEPT_CHECK_BY_ID_V112 = data_module.CONCEPT_CHECK_BY_ID_V112
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119

    for row in deep.get("Pediatric Otolaryngology", []):
        if row.get("topic") == "Croup vs Epiglottitis" and row.get("aliases") == ["Epiglottitis"]:
            row["aliases"] = []
            result["aliases_fixed"] += 1

    for row in deep.get("General ENT / Emergencies", []):
        if row.get("topic") == "Carotid Blowout Syndrome":
            sources = row.get("source_basis") or []
            filtered = [s for s in sources if CAROTID_BLOWOUT_STALE_CITATION_V442 not in str(s)]
            if len(filtered) != len(sources):
                row["source_basis"] = filtered
                result["carotid_blowout_citation_fixed"] += 1
            break

    data_module.DEEP_MODULES_V6 = deep
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = deep

    return result
