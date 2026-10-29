"""v49.1 sweep: rewrites of the older practice-bank questions to the v49 board-vignette standard.

Rewrites live in ``rewrites_v491/<batch>.py`` as ``REWRITES = {question_id: {fields}}``. Each one replaces
the question's stem, choices, answer, explanation, why_wrong, board pearl and curveball in place, so the
question id (and every learner's history on it) is unchanged. Topic, concept, stage and focus are kept.
Must run before the Daily Path installer, which indexes questions at install time.
"""
import importlib
import pkgutil

FIELDS = ("stem", "choices", "answer", "explanation", "why_wrong", "board_pearl", "curveball", "curveball_answer")
SKIP_IDS = set()  # ids whose original wording an audit pins; leave untouched


def _valid(r):
    ch, a, ww = r.get("choices"), r.get("answer"), r.get("why_wrong")
    return (all(k in r for k in FIELDS) and isinstance(ch, list) and len(ch) == 4 and isinstance(a, int)
            and 0 <= a < 4 and isinstance(ww, list) and len(ww) == 4 and str(r.get("stem", "")).strip())


def _load():
    import rewrites_v491
    out = {}
    for info in sorted(pkgutil.iter_modules(rewrites_v491.__path__), key=lambda i: i.name):
        mod = importlib.import_module("rewrites_v491." + info.name)
        out.update(getattr(mod, "REWRITES", {}))
    return out


def install_clinical_challenge_rewrites_v491(data, app_mod=None):
    rewrites = _load()
    by_id = getattr(data, "CLINICAL_CHALLENGE_BY_ID_V119", None)
    targets = {}
    for q in data.CLINICAL_CHALLENGES_V119:
        targets.setdefault(q.get("id"), []).append(q)
    for d in (by_id, getattr(app_mod, "CLINICAL_CHALLENGE_BY_ID_V119", None) if app_mod else None):
        if isinstance(d, dict):
            for qid, q in d.items():
                if not any(q is t for t in targets.get(qid, [])):
                    targets.setdefault(qid, []).append(q)
    applied, rejected, missing = [], [], []
    for qid, r in rewrites.items():
        if qid in SKIP_IDS:
            continue
        if not _valid(r):
            rejected.append(qid)
            continue
        if qid not in targets:
            missing.append(qid)
            continue
        for q in targets[qid]:
            for k in FIELDS:
                q[k] = r[k]
            q["rewritten_v491"] = True
        applied.append(qid)
    result = {"applied": len(applied), "rejected": rejected, "missing": missing}
    data.CLINICAL_CHALLENGE_REWRITES_V491 = result
    return result
