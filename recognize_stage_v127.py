"""
ENT Mastery runtime patch integration.

v12.7 recognize-stage blind reveal; v12.8+ vignette merges; v13.1+ canonical
topic additions and alias repair; v14.x second-pass board/call/OR depth.
All v13.4+ vignette batches are validated against the live canonical curriculum
before merge so a typo fails loudly instead of creating an orphaned case.
"""

import hashlib
import data
from quality_repair_v151 import apply_quality_repair_v151
from vignettes_v128 import VIGNETTES_V128
from topic_alias_v129 import apply_topic_alias_v129
from new_topics_v131 import NEW_TOPICS_V131
from vignettes_v132 import VIGNETTES_V132
from new_topics_v133 import NEW_TOPICS_V133
from vignettes_v134 import VIGNETTES_V134
from vignettes_v136 import VIGNETTES_V136
from vignettes_v137 import VIGNETTES_V137
from vignettes_v138 import VIGNETTES_V138
from vignettes_v139 import VIGNETTES_V139
from vignettes_v140 import VIGNETTES_V140
from vignettes_v141 import VIGNETTES_V141
from vignettes_v142 import VIGNETTES_V142
from vignettes_v143 import VIGNETTES_V143
from vignettes_v144 import VIGNETTES_V144
from vignettes_v145 import VIGNETTES_V145
from vignettes_v146 import VIGNETTES_V146
from vignettes_v147 import VIGNETTES_V147
from vignettes_v148 import VIGNETTES_V148


def apply_recognize_blind_reveal_v127(items):
    """Mutates and returns the adaptive-items list in place."""
    for item in items:
        if item.get("stage") != "recognize" or item.get("blind_reveal"):
            continue
        original_pattern = item.get("answer", "").strip()
        if not original_pattern:
            continue
        topic = item.get("topic", "this condition")
        item["prompt"] = (
            "A patient presents with the following, with no diagnosis given yet: "
            f"{original_pattern}\n\nWhat do you suspect?"
        )
        item["answer"] = f"This is {topic}. {original_pattern}"
        item["blind_reveal"] = True
        item["blind_display_domain"] = item.get("domain", "")
    return items


def _merge_v128_clinical_challenges():
    existing = {q.get("id") for q in data.CLINICAL_CHALLENGES_V119}
    for source in VIGNETTES_V128:
        if source.get("id") in existing:
            continue
        q = dict(source)
        q["concept_id"] = data._v6_item_id(q["domain"], q["topic"])
        data.CLINICAL_CHALLENGES_V119.append(q)
        existing.add(q["id"])
    data.CLINICAL_CHALLENGE_BY_ID_V119 = {
        q["id"]: q for q in data.CLINICAL_CHALLENGES_V119
    }


def _merge_depth_topics(patch, patch_name):
    """Idempotently add exact canonical topics; reject unknown domains."""
    for domain, topics in patch.items():
        if domain not in data.DEEP_MODULES_V6:
            raise RuntimeError(
                f"{patch_name}: unknown curriculum domain {domain!r}; "
                "refusing detached topics"
            )
        existing_topics = {m["topic"] for m in data.DEEP_MODULES_V6[domain]}
        for topic in topics:
            if topic["topic"] not in existing_topics:
                data.DEEP_MODULES_V6[domain].append(topic)
                existing_topics.add(topic["topic"])


def _merge_validated_challenges(batch, patch_name):
    """Merge only cases whose domain/topic resolves to the live curriculum."""
    canonical = {
        (domain, module.get("topic"))
        for domain, modules in data.DEEP_MODULES_V6.items()
        for module in modules
    }
    existing_ids = {q.get("id") for q in data.CLINICAL_CHALLENGES_V119}
    for source in batch:
        key = (source.get("domain"), source.get("topic"))
        if key not in canonical:
            raise RuntimeError(
                f"{patch_name}: orphan vignette {source.get('id')!r} "
                f"targets non-canonical {key!r}"
            )
        if source.get("id") in existing_ids:
            continue
        q = dict(source)
        q["concept_id"] = data._v6_item_id(q["domain"], q["topic"])
        data.CLINICAL_CHALLENGES_V119.append(q)
        existing_ids.add(q["id"])
    data.CLINICAL_CHALLENGE_BY_ID_V119 = {
        q["id"]: q for q in data.CLINICAL_CHALLENGES_V119
    }


_merge_depth_topics(NEW_TOPICS_V131, "v13.1")
_merge_depth_topics(NEW_TOPICS_V133, "v13.3")
_merge_v128_clinical_challenges()
apply_topic_alias_v129(data.CLINICAL_CHALLENGES_V119, data._v6_item_id)

# RRP's canonical curriculum home is Pediatric ENT even for the laryngology-tagged
# legacy vignette; bridge it without duplicating the curriculum topic.
for _q in data.CLINICAL_CHALLENGES_V119:
    if (
        _q.get("topic") == "Recurrent Respiratory Papillomatosis"
        and _q.get("domain") == "Laryngology / Voice / Swallowing"
    ):
        _q["concept_id"] = data._v6_item_id(
            "Pediatric Otolaryngology", "Recurrent Respiratory Papillomatosis"
        )
        _q["canonical_topic"] = "Recurrent Respiratory Papillomatosis"


# data.py's dynamic fallback historically referenced a stale slug helper.
def _fixed_generated_chief_prompt_v120(_domain, _m):
    _id = data._v6_item_id(_domain, _m["topic"])
    return {
        "id": "chief-v120-" + data._v91_slug(_domain) + "-" + data._v91_slug(_m["topic"]),
        "domain": _domain,
        "topic": _m["topic"],
        "concept_id": _id,
        "junior_question": (
            f"I'm trying to understand {_m['topic']}. What is the framework "
            "I should use so I do not just memorize a list?"
        ),
        "must_mention": [
            x for x in (
                _m.get("recognize", ""),
                _m.get("localize", ""),
                _m.get("manage", ""),
            ) if x
        ],
        "model_answer": _m.get("teach") or _m.get("manage", ""),
        "curveball": _m.get("operate") or _m.get("workup", ""),
        "source": "dynamic fallback from deep curriculum",
    }


def _fixed_generated_attending_prompt_v120(_domain, _m):
    _id = data._v6_item_id(_domain, _m["topic"])
    return {
        "id": "attending-v120-" + data._v91_slug(_domain) + "-" + data._v91_slug(_m["topic"]),
        "domain": _domain,
        "topic": _m["topic"],
        "concept_id": _id,
        "prompt": (
            f"You say this is {_m['topic']}. Convince me: what finding changes "
            "your differential or management, and what would make you change course?"
        ),
        "required_points": [
            x for x in (
                _m.get("recognize", ""),
                _m.get("workup", ""),
                _m.get("manage", ""),
                _m.get("operate", ""),
            ) if x
        ],
        "model_answer": _m.get("teach") or _m.get("manage", ""),
        "curveball": _m.get("operate") or _m.get("localize", ""),
        "source": "dynamic fallback from deep curriculum",
    }


data._generated_chief_prompt_v120 = _fixed_generated_chief_prompt_v120
data._generated_attending_prompt_v120 = _fixed_generated_attending_prompt_v120

# v13.2 predates strict validator; keep its idempotent merge unchanged.
_existing_ids_v132 = {q.get("id") for q in data.CLINICAL_CHALLENGES_V119}
for _q_src in VIGNETTES_V132:
    if _q_src.get("id") in _existing_ids_v132:
        continue
    _q = dict(_q_src)
    _q["concept_id"] = data._v6_item_id(_q["domain"], _q["topic"])
    data.CLINICAL_CHALLENGES_V119.append(_q)
    _existing_ids_v132.add(_q.get("id"))
data.CLINICAL_CHALLENGE_BY_ID_V119 = {
    q["id"]: q for q in data.CLINICAL_CHALLENGES_V119
}

for _batch, _name in (
    (VIGNETTES_V134, "v13.4"),
    (VIGNETTES_V136, "v13.6"),
    (VIGNETTES_V137, "v13.7"),
    (VIGNETTES_V138, "v13.8"),
    (VIGNETTES_V139, "v13.9"),
    (VIGNETTES_V140, "v14.0"),
    (VIGNETTES_V141, "v14.1"),
    (VIGNETTES_V142, "v14.2"),
    (VIGNETTES_V143, "v14.3"),
    (VIGNETTES_V144, "v14.4"),
    (VIGNETTES_V145, "v14.5"),
    (VIGNETTES_V146, "v14.6"),
    (VIGNETTES_V147, "v14.7"),
    (VIGNETTES_V148, "v14.8"),
):
    _merge_validated_challenges(_batch, _name)


def _rebalance_vignette_answer_positions_v150(challenges):
    """Deterministically distribute keyed answers while preserving alignment."""
    for q in challenges:
        choices = list(q.get("choices") or [])
        why_wrong = list(q.get("why_wrong") or [])
        if len(choices) < 2:
            continue
        try:
            answer = int(q.get("answer"))
        except (TypeError, ValueError):
            continue
        if answer < 0 or answer >= len(choices):
            continue
        digest = hashlib.sha256(str(q.get("id", "")).encode("utf-8")).digest()
        target = int.from_bytes(digest[:4], "big") % len(choices)
        if target == answer:
            continue
        correct_choice = choices.pop(answer)
        choices.insert(target, correct_choice)
        if len(why_wrong) == len(choices):
            correct_reason = why_wrong.pop(answer)
            why_wrong.insert(target, correct_reason)
            q["why_wrong"] = why_wrong
        q["choices"] = choices
        q["answer"] = target
    return challenges


# Repair legacy placeholder distractor teaching before the deterministic shuffle,
# so each explanation remains attached to its intended option after reordering.
QUALITY_REPAIR_V151 = apply_quality_repair_v151(data.CLINICAL_CHALLENGES_V119)
_rebalance_vignette_answer_positions_v150(data.CLINICAL_CHALLENGES_V119)
data.CLINICAL_CHALLENGE_BY_ID_V119 = {
    q["id"]: q for q in data.CLINICAL_CHALLENGES_V119
}
