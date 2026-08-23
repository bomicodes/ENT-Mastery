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
"""


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
