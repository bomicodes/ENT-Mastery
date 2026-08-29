"""v28.8 — reconcile v28.7 salvage content with the live canonical inventory.

The production H&N inventory has one canonical salvage card:
"Salvage Surgery After Radiation / Chemoradiation". v28.7 authored an excellent
post-definitive-CRT response sublayer under a second payload name, but there is no
second live canonical module for that payload to patch. This compatibility pass
preserves the broad salvage Hub and folds only the missing post-CRT response,
management, operative, teaching, tags, and source material into the live card.
"""

import re
from deep_curriculum_headneck_v287 import SALVAGE_REBUILD_V287

DOMAIN = "Head & Neck Oncology"
BROAD_KEY = "salvage surgery after radiation chemoradiation"
POST_CRT_KEY = "salvage surgery after chemoradiation"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _append_unique(existing, addition, heading):
    existing = str(existing or "").strip()
    addition = str(addition or "").strip()
    if not addition or addition in existing:
        return existing
    return existing + f"\n\n{heading}: " + addition


def apply_headneck_salvage_runtime_alignment_v288(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    broad = next((m for m in modules if _norm(m.get("topic")) == BROAD_KEY), None)
    if broad is None:
        raise RuntimeError("v28.8 live broad salvage canonical module missing")

    post = SALVAGE_REBUILD_V287[POST_CRT_KEY]
    broad["workup"] = _append_unique(
        broad.get("workup"), post["workup"], "POST-CRT RESPONSE ASSESSMENT"
    )
    broad["manage"] = _append_unique(
        broad.get("manage"), post["manage"], "POST-CRT RESPONSE-DIRECTED MANAGEMENT"
    )
    broad["operate"] = _append_unique(
        broad.get("operate"), post["operate"], "POST-CRT SALVAGE OPERATIVE BRANCH"
    )
    broad["teach"] = _append_unique(
        broad.get("teach"), post["teach"], "POST-CRT BOARD DECISION TREE"
    )

    tags = list(broad.get("tags") or [])
    for tag in post.get("tags") or []:
        if tag not in tags:
            tags.append(tag)
    broad["tags"] = tags

    sources = list(broad.get("source_basis") or [])
    for source in post.get("source_basis") or []:
        if source not in sources:
            sources.append(source)
    broad["source_basis"] = sources
    broad["source_grounded_v288"] = True
    broad["post_crt_response_sublayer_v288"] = True

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [broad.get("topic")], "count": 1, "post_crt_folded_into_live_salvage": True}
