"""v30.0 production wrapper — preserves the NOE rebuild and chains v30.1 frontal sinus rebuild."""

from deep_curriculum_facial_v300_base import apply_facial_noe_rebuild_v300 as _apply_noe_v300
from deep_curriculum_facial_v301 import apply_facial_frontal_sinus_rebuild_v301


def apply_facial_noe_rebuild_v300(data_module, app_module=None):
    noe_result = _apply_noe_v300(data_module, app_module)
    frontal_result = apply_facial_frontal_sinus_rebuild_v301(data_module, app_module)
    return {
        "patched": noe_result.get("patched", []),
        "count": noe_result.get("count", 0),
        "v301_frontal_sinus": frontal_result,
    }
