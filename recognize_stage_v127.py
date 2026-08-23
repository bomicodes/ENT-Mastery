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
"""

import data
from vignettes_v128 import VIGNETTES_V128


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


_merge_v128_clinical_challenges()
