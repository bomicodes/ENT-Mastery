import os
import re
from pathlib import Path

import data

# ENT Mastery v12.2 direct-production hotfix.
# 1) Preserve the dynamic topic registry while restoring the legacy adaptive
#    schema expected by Daily Path.
_original_get_adaptive_items_v120 = data.get_adaptive_items_v120


def _get_adaptive_items_v122():
    items = _original_get_adaptive_items_v120()
    stage_level = {"recognize": 1, "localize": 2, "workup": 3, "manage": 4, "operate": 5, "teach": 6}
    for item in items:
        item.setdefault("level", stage_level.get(item.get("stage"), 1))
        item.setdefault(
            "tags",
            sorted(
                set(
                    re.findall(
                        r"[a-z0-9]+",
                        ((item.get("domain") or "") + " " + (item.get("topic") or "")).lower(),
                    )
                )
            ),
        )
    return items


data.get_adaptive_items_v120 = _get_adaptive_items_v122

# 2) Remove the static swallowing interpretation lab. FEES and MBS are dynamic
#    studies; still-frame schematics do not reproduce the temporal information
#    required for meaningful interpretation. Core dysphagia/swallowing learning
#    content remains in the curriculum and cases.
data.INTERPRETATION_LABS.pop("swallowing-imaging", None)
for mapping_name in (
    "LAB_PARENT_TOPIC_V98",
    "LAB_PARENT_CONCEPT_V98",
    "_GENERIC_FOLLOW_BY_LAB_V91",
    "INTERPRETATION_V118_COLLAPSED",
):
    mapping = getattr(data, mapping_name, None)
    if isinstance(mapping, dict):
        mapping.pop("swallowing-imaging", None)

# 3) Do not expose leftover historical atlas links on cards explicitly marked
#    as requiring a modern surgical-anatomy source. Keep the deliberate Open
#    Anatomy links used by the Sleep Surgery modules.
for entry in data.ANATOMY_ATLAS_V97:
    if entry.get("anatomy_visual_status") == "modern_source_needed":
        src = (entry.get("image_source") or "").lower()
        if "openanatomy.org" not in src:
            entry["image_source"] = None
            entry["image_credit"] = "Modern topic-specific source not yet curated"

# 4) Repair the XML ampersand in the 12 head-and-neck teaching SVGs on startup.
#    This keeps production rendering safe even on a fresh Render deploy.
svg_dir = Path(__file__).resolve().parent / "static" / "interpretation_v118"
for svg_path in svg_dir.glob("hn*.svg"):
    try:
        content = svg_path.read_text(encoding="utf-8")
        fixed = content.replace("Head & neck imaging case", "Head &amp; neck imaging case")
        if fixed != content:
            svg_path.write_text(fixed, encoding="utf-8")
    except OSError:
        pass

# Import the Flask application only after patching data so all routes see the
# corrected registries.
import app as _app_module

# The current app still references these legacy names in a few statistics/rank
# paths. Point them at the live registries without rewriting the large app.py.
_app_module.CLINICAL_CHALLENGES_V111 = data.CLINICAL_CHALLENGES_V119
_app_module.CURRICULUM_V5 = data.get_curriculum_v120()

app = _app_module.app
