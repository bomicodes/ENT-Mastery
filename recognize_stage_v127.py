"""
v12.7 — Recognize-stage blind reveal fix.

Problem: Daily Path level-1 "Recognize" cards showed the topic name as the
card's H2 title, then asked the resident to "Recognize the pattern." for a
diagnosis already printed above the question. That tests recall of a named
diagnosis, not recognition of an undifferentiated pattern.

Fix (data layer only — template must also honor `blind_reveal`, see
daily_adaptive.html): for every stage=="recognize" adaptive item, turn the
existing pattern-description text into an actual question stem instead of a
static instruction, and move the diagnosis name into the revealed answer.
Localize/Workup/Manage/Operate/Teach are unchanged — those stages legitimately
proceed from a known diagnosis, so showing the topic name there is fine.

v12.8 runtime integration: this module is already imported by wsgi.py before
Flask imports app.py, so it also performs the small idempotent V128 vignette
merge. This avoids replacing the generated multi-megabyte data.py while keeping
the live CLINICAL_CHALLENGES_V119 bank and direct-lookup index synchronized.

v13.3-v13.4 depth integration: adds decision-heavy thyroid/parathyroid/salivary
and head-and-neck oncology topics, then validates every new vignette against the
live canonical curriculum before merging. A future typo now fails loudly at
startup instead of silently creating an orphaned case.
"""

import data
from vignettes_v128 import VIGNETTES_V128
from topic_alias_v129 import apply_topic_alias_v129
from new_topics_v131 import NEW_TOPICS_V131
from vignettes_v132 import VIGNETTES_V132
from new_topics_v133 import NEW_TOPICS_V133
from vignettes_v134 import VIGNETTES_V134


def apply_recognize_blind_reveal_v127(items):
    """Mutates and returns the adaptive-items list in place."""
    for item in items:
        if item.get("stage") != "recognize":
            continue
        if item.get("blind_reveal"):
            continue  # already patched
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
    """Idempotently merge exact canonical topics, failing on a bad domain."""
    for domain, topics in patch.items():
        if domain not in data.DEEP_MODULES_V6:
            raise RuntimeError(
                f"{patch_name}: unknown curriculum domain {domain!r}; "
                "refusing to create detached topics"
            )
        existing_topics = {m["topic"] for m in data.DEEP_MODULES_V6[domain]}
        for topic in topics:
            if topic["topic"] not in existing_topics:
                data.DEEP_MODULES_V6[domain].append(topic)
                existing_topics.add(topic["topic"])


def _merge_validated_challenges(batch, patch_name):
    """Merge cases only when domain/topic resolves to the live curriculum."""
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
                f"{patch_name}: orphan vignette {source.get('id')!r} targets "
                f"non-canonical {key!r}; add/alias the curriculum topic first"
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

# Recurrent Respiratory Papillomatosis is tagged under Laryngology in its
# vignette but the canonical topic currently only lives under Pediatric
# Otolaryngology - cross-link rather than duplicate the topic.
for _q in data.CLINICAL_CHALLENGES_V119:
    if _q.get("topic") == "Recurrent Respiratory Papillomatosis" and _q.get("domain") == "Laryngology / Voice / Swallowing":
        _q["concept_id"] = data._v6_item_id("Pediatric Otolaryngology", "Recurrent Respiratory Papillomatosis")
        _q["canonical_topic"] = "Recurrent Respiratory Papillomatosis"

# Bug fix: _generated_chief_prompt_v120/_generated_attending_prompt_v120 in
# data.py reference an undefined name (_slugify_v94 - the real helper is
# _v91_slug). This was never triggered because all 312 original topics
# already had a curated chief/attending prompt, so the dynamic fallback path
# never actually ran until the 9 new_topics_v131 topics exercised it for the
# first time. Patch both generators in place with the correct helper.
def _fixed_generated_chief_prompt_v120(_domain, _m):
    _id = data._v6_item_id(_domain, _m["topic"])
    return {
        "id": "chief-v120-" + data._v91_slug(_domain) + "-" + data._v91_slug(_m["topic"]),
        "domain": _domain, "topic": _m["topic"], "concept_id": _id,
        "junior_question": f"I'm trying to understand {_m['topic']}. What is the framework I should use so I do not just memorize a list?",
        "must_mention": [x for x in [_m.get("recognize", ""), _m.get("localize", ""), _m.get("manage", "")] if x],
        "model_answer": _m.get("teach") or _m.get("manage", ""),
        "curveball": _m.get("operate") or _m.get("workup", ""),
        "source": "dynamic fallback from deep curriculum"
    }


def _fixed_generated_attending_prompt_v120(_domain, _m):
    _id = data._v6_item_id(_domain, _m["topic"])
    return {
        "id": "attending-v120-" + data._v91_slug(_domain) + "-" + data._v91_slug(_m["topic"]),
        "domain": _domain, "topic": _m["topic"], "concept_id": _id,
        "prompt": f"You say this is {_m['topic']}. Convince me: what finding changes your differential or management, and what would make you change course?",
        "required_points": [x for x in [_m.get("recognize", ""), _m.get("workup", ""), _m.get("manage", ""), _m.get("operate", "")] if x],
        "model_answer": _m.get("teach") or _m.get("manage", ""),
        "curveball": _m.get("operate") or _m.get("localize", ""),
        "source": "dynamic fallback from deep curriculum"
    }


data._generated_chief_prompt_v120 = _fixed_generated_chief_prompt_v120
data._generated_attending_prompt_v120 = _fixed_generated_attending_prompt_v120

_existing_ids_v132 = {q.get("id") for q in data.CLINICAL_CHALLENGES_V119}
for _q_src in VIGNETTES_V132:
    if _q_src.get("id") in _existing_ids_v132:
        continue
    _q = dict(_q_src)
    _q["concept_id"] = data._v6_item_id(_q["domain"], _q["topic"])
    data.CLINICAL_CHALLENGES_V119.append(_q)
    _existing_ids_v132.add(_q.get("id"))
data.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in data.CLINICAL_CHALLENGES_V119}

# v13.4 is the first case batch with strict canonical-link validation.
_merge_validated_challenges(VIGNETTES_V134, "v13.4")
