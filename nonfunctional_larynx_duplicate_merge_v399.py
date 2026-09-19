"""v39.9 -- Merge the duplicate nonfunctional-larynx topic into the existing
canonical Head & Neck Oncology module, retaining unique teaching and repointing
live vignette links. Apply after all vignette ladders have been assembled.
"""

from deep_curriculum_canonicalize_v166 import _merge_text, _union_list

DOMAIN = "Head & Neck Oncology"
CANONICAL_TOPIC = "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy"
RETIRING_TOPIC = "Nonfunctional Larynx and Intractable Aspiration"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def apply_nonfunctional_larynx_duplicate_merge_v399(data_module):
    modules = data_module.DEEP_MODULES_V6.get(DOMAIN, [])
    canonical = next((m for m in modules if m.get("topic") == CANONICAL_TOPIC), None)
    if canonical is None:
        raise RuntimeError(f"v39.9: expected canonical topic {CANONICAL_TOPIC!r} not found under {DOMAIN!r}")

    retiring = next((m for m in modules if m.get("topic") == RETIRING_TOPIC), None)
    if retiring is None:
        return {"already_merged": True}

    for field in FIELDS:
        canonical[field] = _merge_text(canonical.get(field), retiring.get(field))
    canonical["tags"] = _union_list(canonical.get("tags"), retiring.get("tags"))
    canonical["source_basis"] = _union_list(canonical.get("source_basis"), retiring.get("source_basis"))
    canonical["aliases"] = _union_list(canonical.get("aliases"), [RETIRING_TOPIC])
    modules.remove(retiring)

    canonical_id = data_module._v6_item_id(DOMAIN, CANONICAL_TOPIC)
    retiring_id = data_module._v6_item_id(DOMAIN, RETIRING_TOPIC)

    repointed = []
    for q in data_module.CLINICAL_CHALLENGES_V119:
        if q.get("domain") == DOMAIN and q.get("topic") == RETIRING_TOPIC:
            q["topic"] = CANONICAL_TOPIC
            q["concept_id"] = canonical_id
            repointed.append(q.get("id"))
    if hasattr(data_module, "CLINICAL_CHALLENGE_BY_ID_V119"):
        data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {
            q["id"]: q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")
        }

    return {
        "merged": True,
        "retired_topic": RETIRING_TOPIC,
        "canonical_topic": CANONICAL_TOPIC,
        "id_map": {retiring_id: canonical_id},
        "repointed_vignettes": repointed,
    }
