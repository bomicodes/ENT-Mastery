import re
import data
from curveballs_v123 import ORIGINAL_V11_CURVEBALLS_V123

# ENT Mastery v12.3 production runtime integration.
# Build adaptive items from the final topic registry while preserving the schema
# expected by Daily Path.
_original_get_adaptive_items_v120 = data.get_adaptive_items_v120

def _get_adaptive_items_v123():
    items = _original_get_adaptive_items_v120()
    stage_level = {"recognize": 1, "localize": 2, "workup": 3, "manage": 4, "operate": 5, "teach": 6}
    for item in items:
        item.setdefault("level", stage_level.get(item.get("stage"), 1))
        item.setdefault("tags", sorted(set(re.findall(r"[a-z0-9]+", ((item.get("domain") or "") + " " + (item.get("topic") or "")).lower()))))
    return items

data.get_adaptive_items_v120 = _get_adaptive_items_v123

# Static swallow-study frames are intentionally removed from the Interpretation
# Atlas. VFSS/MBS and FEES are dynamic studies and cannot be meaningfully trained
# with the site's 2-D still-frame schematics. Swallowing concepts/cases remain.
data.INTERPRETATION_LABS.pop("swallowing-imaging", None)
for _name in ("LAB_PARENT_TOPIC_V98", "LAB_PARENT_CONCEPT_V98", "_GENERIC_FOLLOW_BY_LAB_V91", "INTERPRETATION_V118_COLLAPSED"):
    _mapping = getattr(data, _name, None)
    if isinstance(_mapping, dict):
        _mapping.pop("swallowing-imaging", None)

# Complete the original flagship vignette set with a true attending-style
# escalation step. The one already-authored curveball is preserved.
for _bank_name in ("CLINICAL_CHALLENGES_V11", "CLINICAL_CHALLENGES_V112", "CLINICAL_CHALLENGES_V115", "CLINICAL_CHALLENGES_V116", "CLINICAL_CHALLENGES_V119"):
    _bank = getattr(data, _bank_name, None)
    if not isinstance(_bank, list):
        continue
    for _q in _bank:
        _qid = _q.get("id")
        if _qid in ORIGINAL_V11_CURVEBALLS_V123 and not (_q.get("curveball") or "").strip():
            _q["curveball"] = ORIGINAL_V11_CURVEBALLS_V123[_qid]

# Do not expose leftover historical atlas links on cards that explicitly require
# a modern surgical-anatomy source. Keep intentional Open Anatomy links.
for _entry in data.ANATOMY_ATLAS_V97:
    if _entry.get("anatomy_visual_status") == "modern_source_needed":
        _src = (_entry.get("image_source") or "").lower()
        if "openanatomy.org" not in _src:
            _entry["image_source"] = None
            _entry["image_credit"] = "Modern topic-specific source not yet curated"

# Import Flask only after the registries above are corrected so all routes see
# the final production state.
import app as _app_module

# Correct two stale aliases still referenced by app.py without rewriting the
# large application file in this hotfix.
_app_module.CLINICAL_CHALLENGES_V111 = data.CLINICAL_CHALLENGES_V119
_app_module.CURRICULUM_V5 = data.get_curriculum_v120()

app = _app_module.app
