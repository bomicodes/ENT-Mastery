"""v39.9 -- Merge the "Nonfunctional Larynx" duplicate topic flagged during
the v38.4 OR-prep-link work and deferred to this content-staleness pass.

The base curriculum (data.py) has always carried "Nonfunctional Larynx /
Chronic Aspiration After Cancer Therapy" under Head & Neck Oncology.
new_topics_v133.py separately added "Nonfunctional Larynx and Intractable
Aspiration" under the same domain as a supposedly new topic -- the same
_merge_depth_topics bug class that produced the duplicate "Carotid Blowout
Syndrome" node (see recognize_stage_v127.py), except the two exact topic
strings differ, so the existing global exact-string dedup in
_merge_depth_topics never caught this pair, and the duplicate went on to
grow its own full three-stage vignette ladder (vignette_ladders_v231.py)
plus a dedicated regression gate
(audit_cross_domain_aspiration_semantic_v308.py) protecting it, entirely
independent of the original topic's own ladder (vignette_ladders_v227.py).

This retires the newer duplicate into the original canonical topic,
following the same merge pattern as deep_curriculum_canonicalize_v166.py
(reusing its _merge_text/_union_list helpers): union any clinically
distinct sentences from the retiring module into the canonical module,
record the retiring name as an alias, remove the retiring module, and
repoint every CLINICAL_CHALLENGES_V119 vignette that pointed at the
retiring topic (5 vignettes: v134_hno_03, v145_hn_11, v231_hn_nfl_fnd,
v231_hn_nfl_app, v231_hn_nfl_snr) to the canonical topic/concept_id.

Must run after the full vignette-ladder chain (recognize_stage_v127 and
ladder_answer_balance_v211's chain, both already executed inside
runtime_entry by the time runtime_entry_pasha's own patches run), since it
repoints already-merged CLINICAL_CHALLENGES_V119 rows rather than the raw
vignette-batch source lists.

Companion change: audit_cross_domain_aspiration_semantic_v308.py's
HN_TOPIC constant is updated to the canonical name so that standalone
regression gate keeps passing against the post-merge concept_id/topic.
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
        # Already merged (idempotent reload, or a collaborator applied an
        # equivalent fix upstream) -- nothing left to do.
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
