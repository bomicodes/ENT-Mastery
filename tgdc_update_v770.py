"""v77.0: Thyroglossal duct cyst content updated and made consistent.

A review of every TGDC item (curriculum topic, Sistrunk OR card, questions, concept checks,
flashcards) against current literature found conflicting numbers (recurrence quoted as 40-50%,
~50%, 3-6%, under 5%), wrong location figures, a self-contradictory dermoid sign, template text
copied onto the OR card, outdated revision advice and thin carcinoma coverage. Figures now used
everywhere: recurrence about 3-5% after Sistrunk vs about 45-55% after simple cystectomy
(Rohof 2015; Galluzzi 2013); about three-quarters at or below the hyoid; carcinoma about 1%,
mostly papillary; ectopic thyroid in about 1-2% of presumed TGDCs; recurrence after Sistrunk ->
wide central neck ("en bloc") dissection.
Applied at boot as exact text replacements and additions (a fix whose text is not found is
skipped and reported). The edit lists live in tgdc_update_v770.json.
"""
import json
import os

TOPIC = "Thyroglossal Duct Cyst"
_HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_HERE, "tgdc_update_v770.json"), encoding="utf-8") as _f:
    _EDITS = json.load(_f)
FIXES_V770 = _EDITS["fixes"]
ADDITIONS_V770 = _EDITS["additions"]


def _targets(data, app_mod):
    out = {}
    for dom, mods in data.DEEP_MODULES_V6.items():
        for m in mods:
            if m.get("topic") == TOPIC:
                out["curriculum_topic"] = m
    reg = getattr(app_mod, "OR_PREP_REGISTRY", None) or data.OR_PREP_REGISTRY
    out["or_card_thyroglossal"] = reg.get("thyroglossal")
    return out


def _find_q(data, kind, qid):
    bank = data.CLINICAL_CHALLENGES_V119 if kind == "question" else data.CONCEPT_CHECKS_V112
    for q in bank:
        if str(q.get("id")) == qid:
            return q
    by = getattr(data, "CLINICAL_CHALLENGE_BY_ID_V119", {}) if kind == "question" else {}
    return by.get(qid)


def _replace_in(obj, field, old, new):
    v = obj.get(field)
    if isinstance(v, str):
        if old in v:
            obj[field] = v.replace(old, new, 1)
            return True
        return False
    if isinstance(v, list):
        for i, item in enumerate(v):
            if isinstance(item, str) and old in item:
                v[i] = item.replace(old, new, 1)
                return True
            if isinstance(item, list):
                for j, sub in enumerate(item):
                    if isinstance(sub, str) and old in sub:
                        item[j] = sub.replace(old, new, 1)
                        return True
    if isinstance(v, dict):
        for items in v.values():
            if isinstance(items, list):
                for i, item in enumerate(items):
                    if isinstance(item, str) and old in item:
                        items[i] = item.replace(old, new, 1)
                        return True
    return False


def _resolve(where, data, app_mod, targets):
    import re
    head, field = where.split(".", 1)
    if ":" in head:
        kind, qid = head.split(":", 1)
        obj = _find_q(data, kind, qid)
    else:
        obj = targets.get(head)
    # "steps[0]" -> field steps; "antibiotics.regimen" / "complications.early[0]" -> nested dict
    parts = [re.sub(r"\[\d+\]", "", x) for x in field.split(".")]
    while obj is not None and len(parts) > 1 and isinstance(obj.get(parts[0]), dict):
        obj = obj.get(parts[0]); parts = parts[1:]
    return obj, parts[0]


def install_tgdc_update_v770(data, app_mod=None):
    targets = _targets(data, app_mod)
    applied, missing = 0, []
    for f in FIXES_V770:
        obj, field = _resolve(f["where"], data, app_mod, targets)
        if obj is not None and _replace_in(obj, field, f["current"], f["replacement"]):
            applied += 1
        else:
            missing.append(f["where"])
    added = 0
    for a in ADDITIONS_V770:
        obj, field = _resolve(a["where"], data, app_mod, targets)
        if obj is None:
            missing.append(a["where"])
            continue
        v = obj.get(field)
        if isinstance(v, list):
            if a["text"] not in v:
                v.append(a["text"])
        elif isinstance(v, str):
            if a["text"] not in v:
                obj[field] = (v.rstrip() + " " + a["text"]).strip()
        else:
            obj[field] = a["text"]
        added += 1
    return {"applied": applied, "added": added, "missing": missing}
