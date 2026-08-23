from pathlib import Path

p = Path("data.py")
text = p.read_text(encoding="utf-8")
marker = "# v12.5 — source-level final registry normalization"
if marker not in text:
    text += r'''

# v12.5 — source-level final registry normalization
# Keep the canonical data module correct even when imported directly (outside
# the Render WSGI entrypoint). This prevents late content from becoming orphaned.
from curveballs_v123 import ORIGINAL_V11_CURVEBALLS_V123
from vignettes_v124 import VIGNETTES_V124

# Static VFSS/MBS/FEES frames are intentionally not an Interpretation Atlas lab.
# Swallowing curriculum, clinical reasoning, and integrated cases remain intact.
INTERPRETATION_LABS.pop("swallowing-imaging", None)
for _mapping_name in (
    "LAB_PARENT_TOPIC_V98",
    "LAB_PARENT_CONCEPT_V98",
    "_GENERIC_FOLLOW_BY_LAB_V91",
    "INTERPRETATION_V118_COLLAPSED",
):
    _mapping = globals().get(_mapping_name)
    if isinstance(_mapping, dict):
        _mapping.pop("swallowing-imaging", None)

# Backfill the original curated challenge set's missing attending-style follow-up.
# Apply across cumulative aliases because older lists may contain shared or copied
# dict records depending on build generation.
for _bank_name in (
    "CLINICAL_CHALLENGES_V11",
    "CLINICAL_CHALLENGES_V112",
    "CLINICAL_CHALLENGES_V115",
    "CLINICAL_CHALLENGES_V116",
    "CLINICAL_CHALLENGES_V119",
):
    _bank = globals().get(_bank_name)
    if not isinstance(_bank, list):
        continue
    for _q in _bank:
        _qid = _q.get("id")
        if _qid in ORIGINAL_V11_CURVEBALLS_V123 and not (_q.get("curveball") or "").strip():
            _q["curveball"] = ORIGINAL_V11_CURVEBALLS_V123[_qid]

# Wire the weighted Otology/Pediatric expansion into the canonical live bank.
_topic_to_concept_v125 = {
    (_domain, _m.get("topic")): _v6_item_id(_domain, _m.get("topic"))
    for _domain, _mods in DEEP_MODULES_V6.items()
    for _m in _mods
    if _m.get("topic")
}
_existing_ids_v125 = {q.get("id") for q in CLINICAL_CHALLENGES_V119}
for _q_src in VIGNETTES_V124:
    if _q_src.get("id") in _existing_ids_v125:
        continue
    _q = dict(_q_src)
    _q["concept_id"] = _topic_to_concept_v125.get((_q.get("domain"), _q.get("topic")))
    CLINICAL_CHALLENGES_V119.append(_q)
    _existing_ids_v125.add(_q.get("id"))
CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in CLINICAL_CHALLENGES_V119}
'''
    p.write_text(text, encoding="utf-8")
