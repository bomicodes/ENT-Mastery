"""v16.6/v16.7 — Deep Curriculum canonicalization + clinical hierarchy pass.

Removes high-confidence duplicate/over-fragmented curriculum nodes only after
all historical enrichment patches have run. Unique teaching from the retiring
node is merged into the canonical six-layer module sentence-by-sentence, then
linked content is repointed to the canonical concept_id.

This deliberately does NOT auto-merge every fuzzy-title pair. Closely related
but clinically distinct topics (e.g. ETD vs patulous ETD, acute diffuse otitis
externa vs necrotizing otitis externa, CRSsNP vs CRSwNP, oral tongue vs
base-of-tongue SCC) remain separate and are instead related by the v16.7
clinical hierarchy when appropriate.

v17.7 expands this cleanup in two ways:
1) adds a second set of manually reviewed over-fragmented nodes; and
2) collapses only a conservative whitelist of alias-label collisions when both
   the alias and its already-established canonical topic exist as curriculum
   nodes. This catches legacy synonym cards without merging clinically distinct
   parent/child concepts merely because their titles look similar.
"""

from difflib import SequenceMatcher
import re

from clinical_hierarchy_v167 import apply_clinical_hierarchy_v167


# domain -> canonical topic -> retiring duplicate/over-fragmented topics
# IMPORTANT: only true duplicates/naming variants belong here. Disease entities
# that are clinically differentiated on boards (for example uncomplicated AOE
# versus necrotizing OE) must remain separate nodes.
CANONICAL_MERGES_V166 = {
    "Otology / Neurotology": {
        "Otosclerosis / Stapes Fixation": ["Otosclerosis"],
    },
    "Head & Neck Oncology": {
        "Salvage Surgery After Radiation / Chemoradiation": [
            "Salvage Surgery After Chemoradiation",
        ],
        "Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer": [
            "Palliative Decision-Making in Head and Neck Cancer",
        ],
        "Free-Flap Monitoring / Compromise / Salvage": [
            "Free Flap Monitoring and Salvage",
        ],
        # Keep one dedicated rescue/complication node rather than a second
        # neck-dissection card that repeats the same complication material.
        "Complications of Neck Surgery": ["Neck Dissection Complications"],
    },
    "Thyroid / Parathyroid / Salivary": {
        # Active surveillance is a management branch of differentiated thyroid
        # cancer, not a second disease entity. Preserve its unique teaching in
        # the parent module rather than duplicating staging/workup content.
        "Differentiated Thyroid Cancer": [
            "Differentiated Thyroid Cancer: Active Surveillance",
        ],
    },
    "Pediatric Otolaryngology": {
        "Croup vs Epiglottitis": ["Epiglottitis"],
    },
    "Facial Plastics / Trauma": {
        "NOE Fracture": ["NOE Fracture Mechanics"],
        "Frontal Sinus Fracture": ["Frontal Sinus Fracture Decision Model"],
        "Facial Nerve Reanimation": [
            "Dynamic Facial Reanimation",
            "Static Facial Reanimation",
        ],
    },
    "Sleep Surgery": {
        "Palatal Surgery": ["Palatal Surgery Selection for OSA"],
    },
}

# Alias labels that are genuinely naming variants / same canonical concept.
# These are intentionally conservative; broader/subtype relationships such as
# Adult OSA -> Adult PSG Interpretation or perineural spread -> cutaneous SCC
# are excluded even though legacy vignette routing may map them together.
SAFE_ALIAS_COLLISIONS_V177 = {
    "Cholesteatoma": "Chronic Otitis Media / Cholesteatoma",
    "Facial Nerve Paralysis": "Facial Paralysis",
    "Labyrinthitis": "Labyrinthitis / Infections of the Labyrinth",
    "Perilymph Fistula": "Perilymph Fistula / Inner-Ear Window Leak",
    "SSNHL": "Sudden Sensorineural Hearing Loss",
    "Superior Semicircular Canal Dehiscence": "Superior Canal Dehiscence",
    "Acute Invasive Fungal Rhinosinusitis": "Invasive Fungal Rhinosinusitis",
    "Frontal Sinus Mucocele": "Mucocele",
    "Intracranial Complication of Sinusitis": "Intracranial Complications of Sinusitis",
    "Inverted Papilloma": "Sinonasal Inverted Papilloma",
    "Orbital Complication of Sinusitis": "Orbital Complications of Sinusitis",
    "Adjuvant Therapy After Head and Neck Cancer Surgery": "Adverse Pathology and Adjuvant Therapy",
    "HPV-Positive Oropharyngeal Squamous Cell Carcinoma": "HPV-Associated Oropharyngeal SCC",
    "Osteoradionecrosis": "Osteoradionecrosis of the Jaw",
    "Sinonasal Malignancy": "Sinonasal Malignancies",
    "Unknown Primary": "Unknown Primary with Cervical Metastasis",
    "Unknown Primary Head and Neck Cancer": "Unknown Primary with Cervical Metastasis",
    "Unknown Primary Squamous Cell Carcinoma": "Unknown Primary with Cervical Metastasis",
    "Hungry Bone Syndrome": "Hungry Bone / Post-Thyroid Calcium Management",
    "Medullary Thyroid Carcinoma": "Medullary Thyroid Cancer",
    "Airway Foreign Body": "Pediatric Airway Foreign Body",
    "Congenital Neck Mass": "Congenital Neck Masses",
    "Subglottic Stenosis": "Pediatric Subglottic Stenosis",
    "Bilateral Vocal Fold Paralysis": "Bilateral Vocal Fold Immobility",
    "Laryngeal Granuloma": "Vocal Process Granuloma",
    "Vocal Fold Scar / Sulcus Vocalis": "Vocal Fold Sulcus / Scar",
    "Central Sleep Apnea": "Central Sleep Apnea / Treatment-Emergent CSA",
    "Treatment-Emergent Central Sleep Apnea": "Central Sleep Apnea / Treatment-Emergent CSA",
    "Drug-Induced Sleep Endoscopy": "DISE",
    "Hypoventilation": "Sleep-Related Hypoventilation",
    "Mandibular Advancement Device": "Oral Appliance Therapy",
    "Pediatric Residual OSA": "Residual OSA After Surgery",
    "Esophageal Perforation": "Esophageal Perforation / Cervical Mediastinitis",
    "Post-thyroidectomy Neck Hematoma": "Postoperative Neck Hematoma",
    "Laryngeal Cancer": "Laryngeal SCC",
}

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _sentences(text):
    text = " ".join(str(text or "").split())
    if not text:
        return []
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", text) if x.strip()]


def _norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text or "").lower()).strip()


def _merge_text(primary, extra):
    """Union clinically distinct sentences without doubling near-identical prose."""
    kept = _sentences(primary)
    for sentence in _sentences(extra):
        ns = _norm(sentence)
        if not ns:
            continue
        duplicate = False
        for existing in kept:
            ne = _norm(existing)
            if not ne:
                continue
            if ns == ne or SequenceMatcher(None, ns, ne).ratio() >= 0.88:
                duplicate = True
                break
        if not duplicate:
            kept.append(sentence)
    return " ".join(kept)


def _union_list(a, b):
    out = []
    seen = set()
    for item in list(a or []) + list(b or []):
        key = _norm(item)
        if key and key not in seen:
            seen.add(key)
            out.append(item)
    return out


def _repoint_linked_records(data, id_map, topic_map):
    """Repoint known learning banks while preserving their display labels."""
    banks = []
    for name in (
        "CLINICAL_CHALLENGES_V119",
        "CONCEPT_CHECKS_V112",
        "ADAPTIVE_ITEMS_V6",
        "ADAPTIVE_ITEMS_V91",
        "CHIEF_PROMPTS_V120",
        "ATTENDING_PROMPTS_V120",
    ):
        value = getattr(data, name, None)
        if isinstance(value, list):
            banks.append(value)

    seen_lists = set()
    for bank in banks:
        if id(bank) in seen_lists:
            continue
        seen_lists.add(id(bank))
        for item in bank:
            if not isinstance(item, dict):
                continue
            cid = item.get("concept_id")
            if cid in id_map:
                item["concept_id"] = id_map[cid]
            key = (item.get("domain"), item.get("topic"))
            if key in topic_map:
                item["canonical_topic"] = topic_map[key]


def _expanded_merge_groups(data):
    """Return static reviewed merges plus safe synonym collisions found live."""
    groups = {
        domain: {canonical: list(retiring) for canonical, retiring in mapping.items()}
        for domain, mapping in CANONICAL_MERGES_V166.items()
    }
    for domain, modules in data.DEEP_MODULES_V6.items():
        topics = {m.get("topic") for m in modules}
        for alias, canonical in SAFE_ALIAS_COLLISIONS_V177.items():
            if alias == canonical or alias not in topics or canonical not in topics:
                continue
            retiring = groups.setdefault(domain, {}).setdefault(canonical, [])
            if alias not in retiring:
                retiring.append(alias)
    return groups


def apply_deep_curriculum_canonicalization_v166(data):
    applied = []
    missing = []
    id_map = {}
    topic_map = {}

    for domain, groups in _expanded_merge_groups(data).items():
        modules = data.DEEP_MODULES_V6.get(domain, [])
        for canonical_topic, retiring_topics in groups.items():
            canonical = next((m for m in modules if m.get("topic") == canonical_topic), None)
            if canonical is None:
                # Static mappings may target a module not present in a particular
                # historical registry; report rather than creating a new node.
                missing.append((domain, canonical_topic, "canonical_missing"))
                continue

            aliases = list(canonical.get("aliases") or [])
            for retiring_topic in retiring_topics:
                retiring = next((m for m in modules if m.get("topic") == retiring_topic), None)
                if retiring is None:
                    continue

                for field in FIELDS:
                    canonical[field] = _merge_text(canonical.get(field), retiring.get(field))
                canonical["tags"] = _union_list(canonical.get("tags"), retiring.get("tags"))
                canonical["source_basis"] = _union_list(
                    canonical.get("source_basis"), retiring.get("source_basis")
                )
                aliases.append(retiring_topic)

                old_id = data._v6_item_id(domain, retiring_topic)
                new_id = data._v6_item_id(domain, canonical_topic)
                id_map[old_id] = new_id
                topic_map[(domain, retiring_topic)] = canonical_topic
                modules.remove(retiring)
                applied.append((domain, retiring_topic, canonical_topic))

            canonical["aliases"] = _union_list(canonical.get("aliases"), aliases)

    _repoint_linked_records(data, id_map, topic_map)

    if hasattr(data, "CLINICAL_CHALLENGES_V119"):
        data.CLINICAL_CHALLENGE_BY_ID_V119 = {
            q["id"]: q for q in data.CLINICAL_CHALLENGES_V119 if q.get("id")
        }
    if hasattr(data, "CONCEPT_CHECKS_V112"):
        data.CONCEPT_CHECK_BY_ID_V112 = {
            q["id"]: q for q in data.CONCEPT_CHECKS_V112 if q.get("id")
        }

    hierarchy = apply_clinical_hierarchy_v167(data, id_map, topic_map)

    return {
        "applied": applied,
        "missing": missing,
        "id_map": id_map,
        "topic_map": topic_map,
        "hierarchy": hierarchy,
    }
