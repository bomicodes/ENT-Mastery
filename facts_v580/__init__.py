"""Fact flashcards: short Q/A cards built from the curated board-style questions.

v58.0  batch_*.py   FACTS = [{"qid", "front", "back"}]  one card per question.
v59.0  fixes_*.py   FIXES = {qid: {"mode": split|hook|trim, "cards": [{front, back, hook?}]}}
                    replaces a question's card when its answer was a hard-to-memorize list.
       dups.py      DUPS = [{"mode": "merge", "keep", "aliases", "front"} | {"mode": "distinct", "qids", "fronts"}]
                    merges cards that tested the same fact (aliases point at the kept card).

load() -> (cards, by_qid)
  cards:  {card_key: {"qid", "front", "back", "hook"}}   card_key is the qid for the first card
          and "qid~2", "qid~3"... for extra cards from a split, so existing progress is kept.
  by_qid: {qid: [card_key, ...]}  every board question maps to the card(s) that teach its fact,
          including aliased questions, so a missed question schedules the right card.
"""
import glob
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _mod(path):
    spec = importlib.util.spec_from_file_location("facts_v580_" + os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load():
    base = {}
    for path in sorted(glob.glob(os.path.join(HERE, "batch_*.py"))):
        for f in getattr(_mod(path), "FACTS", []) or []:
            q, fr, bk = f.get("qid"), (f.get("front") or "").strip(), (f.get("back") or "").strip()
            if q and fr and bk:
                base[q] = [{"front": fr, "back": bk, "hook": ""}]
    for path in sorted(glob.glob(os.path.join(HERE, "fixes_*.py"))):
        for q, fix in (getattr(_mod(path), "FIXES", {}) or {}).items():
            cs = [{"front": (c.get("front") or "").strip(), "back": (c.get("back") or "").strip(),
                   "hook": (c.get("hook") or "").strip()} for c in fix.get("cards") or []]
            cs = [c for c in cs if c["front"] and c["back"]]
            if q in base and cs:
                base[q] = cs
    alias = {}
    dpath = os.path.join(HERE, "dups.py")
    if os.path.exists(dpath):
        for d in getattr(_mod(dpath), "DUPS", []) or []:
            if d.get("mode") == "merge" and d.get("keep") in base:
                if d.get("front"):
                    base[d["keep"]][0]["front"] = d["front"].strip()
                for a in d.get("aliases") or []:
                    if a in base:
                        alias[a] = d["keep"]
            elif d.get("mode") == "distinct":
                for q, fr in (d.get("fronts") or {}).items():
                    if fr and q in base:
                        base[q][0]["front"] = fr.strip()
    cards, by_qid = {}, {}
    for q, cs in base.items():
        if q in alias:
            continue
        keys = []
        for i, c in enumerate(cs):
            k = q if i == 0 else f"{q}~{i + 1}"
            cards[k] = {"qid": q, **c}
            keys.append(k)
        by_qid[q] = keys
    for a, keep in alias.items():
        by_qid[a] = by_qid.get(keep, [])
    return cards, by_qid
