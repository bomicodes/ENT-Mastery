"""v30.0 production wrapper — preserves NOE + frontal-sinus + facial reanimation rebuilds and chains v30.4 complicated sinusitis."""

from deep_curriculum_facial_v300_base import apply_facial_noe_rebuild_v300 as _apply_noe_v300
from deep_curriculum_facial_v301 import apply_facial_frontal_sinus_rebuild_v301
from deep_curriculum_facial_v303 import apply_facial_reanimation_rebuild_v303
from deep_curriculum_rhinology_v304 import apply_rhinology_complications_rebuild_v304


def apply_facial_noe_rebuild_v300(data_module, app_module=None):
    noe_result = _apply_noe_v300(data_module, app_module)
    frontal_result = apply_facial_frontal_sinus_rebuild_v301(data_module, app_module)
    reanimation_result = apply_facial_reanimation_rebuild_v303(data_module, app_module)
    sinus_complications_result = apply_rhinology_complications_rebuild_v304(data_module, app_module)
    return {
        "patched": noe_result.get("patched", []),
        "count": noe_result.get("count", 0),
        "v301_frontal_sinus": frontal_result,
        "v303_facial_reanimation": reanimation_result,
        "v304_rhinology_complications": sinus_complications_result,
    }
