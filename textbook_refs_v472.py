"""v47.2 textbook cross-reference: page-level citations for every Deep Curriculum topic.

The reviewer checked each topic's overview / physiology / pathophysiology and each v47.1
Concept Check against Cummings 7e, Pasha & Golub 6e, K.J. Lee 12e and Bluestone & Stool 5e
and returned textbook_xref/corrections/*.csv. Text corrections were applied directly to
pathophys_v470/ and cc_v471/; this module turns the confirmed citations into a per-topic
"Textbook references" list, plus literature sources for claims the books do not cover.
"""
import csv, glob, os, sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_XREF = os.path.join(_HERE, "textbook_xref")
SHORT = {"Cummings": "Cummings 7e", "Pasha": "Pasha & Golub 6e", "K.J.": "K.J. Lee 12e",
         "Bluestone": "Bluestone & Stool 5e"}


def _short(book):
    for k, v in SHORT.items():
        if book.startswith(k):
            return v
    return book.strip()


def _split(v):
    return [x.strip() for x in str(v or "").split("|")]


def build_refs():
    sys.path.insert(0, _XREF)
    try:
        from ids import topic_index
        from literature_refs import LITERATURE_REFS
    finally:
        sys.path.remove(_XREF)
    idx = topic_index()
    refs, checks, stats = {}, {}, {"rows": 0, "verdicts": {}}
    for path in sorted(glob.glob(os.path.join(_XREF, "corrections", "*.csv"))):
        with open(path, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                stats["rows"] += 1
                stats["verdicts"][r["verdict"]] = stats["verdicts"].get(r["verdict"], 0) + 1
                iid = r["item_id"].strip()
                key = iid if iid.startswith("CC-") else iid.split(".")[0]
                if key not in idx or r["verdict"] == "UNSUPPORTED":
                    continue
                topic = idx[key][1]
                books, chaps, pages = _split(r["book"]), _split(r["edition_chapter"]), _split(r["printed_page"])
                for i, page in enumerate(pages):
                    if not page:
                        continue
                    book = _short(books[min(i, len(books) - 1)])
                    chap = chaps[min(i, len(chaps) - 1)]
                    chap = chap.split(",", 1)[-1].strip() if "," in chap else chap
                    label = "%s, %s, p %s" % (book, chap, page)
                    lst = refs.setdefault(topic, [])
                    if label not in lst:
                        lst.append(label)
                    if iid.startswith("CC-"):
                        checks.setdefault(topic, set()).add(label)
    order = list(SHORT.values())
    for topic, lst in refs.items():
        lst.sort(key=lambda s: (next((i for i, b in enumerate(order) if s.startswith(b)), 9), s))
    return refs, LITERATURE_REFS, {t: sorted(v) for t, v in checks.items()}, stats


def install_textbook_refs_v472(data, app):
    refs, lit, check_refs, stats = build_refs()
    data.TEXTBOOK_REFS_V472 = refs
    data.LITERATURE_REFS_V472 = lit

    def textbook_refs_v472(topic):
        return {"books": refs.get(topic, []), "literature": lit.get(topic, [])}

    app.jinja_env.globals["textbook_refs_v472"] = textbook_refs_v472
    tagged = 0
    for q in getattr(data, "CONCEPT_CHECKS_V112", []):
        if q.get("authored_v471") and q.get("topic") in refs:
            q["textbook_refs_v472"] = refs[q["topic"]][:4]
            tagged += 1
    result = {"topics_cited": len(refs), "literature_topics": len(lit),
              "checks_tagged": tagged, **stats}
    data.TEXTBOOK_XREF_V472 = result
    return result
