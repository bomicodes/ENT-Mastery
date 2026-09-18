"""v37.2 - Sudden Sensorineural Hearing Loss: bedside tuning-fork localization
when audiometry is not immediately available.

Gap found on manual curriculum-depth review: both live SNHL canonical concepts
("Sensorineural Hearing Loss" foundation card, v35.8; "Sudden Sensorineural
Hearing Loss" / "Sudden SNHL" applied card, v15.8) discuss tuning forks only
as a generic step ("otoscopy, bedside tuning forks, and prompt audiometry")
without ever stating which fork to use, what a normal SNHL pattern looks like
on Weber/Rinne, or how to use that pattern when audiometry cannot be obtained
same-day (weekend/ER presentation, rural transfer, etc). The 512-Hz fork
detail exists elsewhere in the codebase only under Otosclerosis/Stapedectomy
workup (deep_curriculum_otology_v361.py), not under SNHL. This patch adds the
missing bedside-exam teaching point to the Sudden SNHL applied card without
disturbing any other field.

Idempotent: re-running just re-appends the same block if it is ever missing,
and is a no-op if the block is already present.
"""

import re

DOMAIN = "Otology / Neurotology"

SUDDEN_SNHL_TOPIC_CANDIDATES_V372 = (
    "Sudden Sensorineural Hearing Loss",
    "Sudden SNHL",
)

TUNING_FORK_ADDENDUM_V372 = (
    " BEDSIDE TUNING-FORK LOCALIZATION WHEN AUDIOMETRY IS NOT YET AVAILABLE: use a 512-Hz "
    "fork (not 256/128 Hz, which over-relies on tactile vibration, and not 1024/2048 Hz, "
    "which decays too quickly to time reliably). Weber (fork on midline forehead/vertex) "
    "lateralizes AWAY from the affected ear in true SNHL, i.e. to the better-hearing side; "
    "Rinne stays 'positive' (air conduction louder than bone conduction) on the affected "
    "side, the same pattern as a normal ear. This is the opposite of conductive loss, where "
    "Weber lateralizes TO the affected ear and Rinne becomes 'negative' there. A patient "
    "whose Weber lateralizes to the worse ear should prompt a second look for a conductive "
    "component (canal debris, middle-ear effusion, hemotympanum after trauma) rather than an "
    "assumption of SNHL. Tuning forks confirm the conductive-versus-sensorineural pattern and "
    "support same-day urgency; they cannot grade severity, cannot substitute for formal "
    "audiometry, and do not remove the requirement to obtain audiometry as soon as possible "
    "(within 14 days) to confirm the diagnosis and document a treatment-eligible baseline."
)


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _find_sudden_snhl(rows):
    for row in rows:
        if row.get("topic") in SUDDEN_SNHL_TOPIC_CANDIDATES_V372:
            return row
    return None


def apply_snhl_bedside_exam_v372(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    rows = deep_modules.get(DOMAIN, []) or []
    module = _find_sudden_snhl(rows)
    if module is None:
        raise RuntimeError(
            "v37.2: could not find the canonical Sudden Sensorineural Hearing Loss topic"
        )

    for field in ("recognize", "workup"):
        current = module.get(field, "") or ""
        if "512-Hz" not in current and "512 Hz" not in current:
            module[field] = current.rstrip() + TUNING_FORK_ADDENDUM_V372

    tags = module.setdefault("tags", [])
    for tag in ("tuning fork", "512 Hz", "Weber test", "Rinne test", "bedside hearing exam"):
        if tag not in tags:
            tags.append(tag)

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6

    return {"patched_topic": module.get("topic")}
