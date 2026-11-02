"""v58.0 fact flashcards: one short Q/A card per curated board-style question.

Each batch module defines FACTS = [{"qid", "front", "back"}]. Written from each
question's keyed answer, board pearl and explanation, then reviewed against the
source question. load() returns {qid: {"front", "back"}}.
"""
import glob
import importlib.util
import os


def load():
    out = {}
    here = os.path.dirname(os.path.abspath(__file__))
    for path in sorted(glob.glob(os.path.join(here, "batch_*.py"))):
        spec = importlib.util.spec_from_file_location("facts_v580_" + os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for f in getattr(mod, "FACTS", []) or []:
            q, fr, bk = f.get("qid"), (f.get("front") or "").strip(), (f.get("back") or "").strip()
            if q and fr and bk:
                out[q] = {"front": fr, "back": bk}
    return out
