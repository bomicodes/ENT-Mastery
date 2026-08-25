"""v16.6 — Deep Curriculum canonicalization pass.

Removes high-confidence duplicate/over-fragmented curriculum nodes only after
all historical enrichment patches have run. Unique teaching from the retiring
node is merged into the canonical six-layer module sentence-by-sentence, then
linked content is repointed to the canonical concept_id.

This deliberately does NOT auto-merge every fuzzy-title pair. Closely related
but clinically distinct topics (e.g. ETD vs patulous ETD, CRSsNP vs CRSwNP,
oral tongue vs base-of-tongue SCC) remain separate.
"""

from difflib import SequenceMatcher
import re


# domain -> canonical topic -> retiring duplicate/over-fragmented topics
CANONICAL_MERGES_V166 = {
    "Otology / Neurotology": {
        # NOE is already taught as the invasive escalation branch inside the
        # enriched Acute Otitis Externa module, including NOE vs SBO.
        "Acute Otitis Externa": ["Necrotizing Otitis Externa"],
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
    },
    "Pediatric Otolaryngology": {
        # Keep one emergency module that explicitly teaches the croup-vs-
        # epiglottitis discrimination rather than a second epiglottitis card.
        "Croup vs Epiglottitis": ["Epiglottitis"],
    },
    "Facial Plastics / Trauma": {
        "NOE Fracture": ["NOE Fracture Mechanics"],
        "Frontal Sinus Fracture": ["Frontal Sinus Fracture Decision Model"],
        # Static and dynamic are decision branches of one reanimation framework;
        # keeping three canonical cards was producing repeated anatomy/timing.
        "Facial Nerve Reanimation": [
            "Dynamic Facial Reanimation",
            "Static Facial Reanimation",
        ],
    },
    "Sleep Surgery": {
        "Palatal Surgery": ["Palatal Surgery Selection for OSA"],
    },
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
                # Keep the more specific legacy label for the question/card,
                # but make its canonical home explicit for coverage/search.
                item["canonical_topic"] = topic_map[key]


def apply_deep_curriculum_canonicalization_v166(data):
    applied = []
    missing = []
    id_map = {}
    topic_map = {}

    for domain, groups in CANONICAL_MERGES_V166.items():
        modules = data.DEEP_MODULES_V6.get(domain, [])
        for canonical_topic, retiring_topics in groups.items():
            canonical = next((m for m in modules if m.get("topic") == canonical_topic), None)
            if canonical is None:
                missing.append((domain, canonical_topic, "canonical_missing"))
                continue

            aliases = list(canonical.get("aliases") or [])
            for retiring_topic in retiring_topics:
                retiring = next((m for m in modules if m.get("topic") == retiring_topic), None)
                if retiring is None:
                    # Idempotent: already removed is fine.
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

    # Rebuild indexes that are known to depend directly on concept-linked banks.
    if hasattr(data, "CLINICAL_CHALLENGES_V119"):
        data.CLINICAL_CHALLENGE_BY_ID_V119 = {
            q["id"]: q for q in data.CLINICAL_CHALLENGES_V119 if q.get("id")
        }
    if hasattr(data, "CONCEPT_CHECKS_V112"):
        data.CONCEPT_CHECK_BY_ID_V112 = {
            q["id"]: q for q in data.CONCEPT_CHECKS_V112 if q.get("id")
        }

    return {
        "applied": applied,
        "missing": missing,
        "id_map": id_map,
        "topic_map": topic_map,
    }
