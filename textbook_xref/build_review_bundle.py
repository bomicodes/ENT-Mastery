"""Build TEXTBOOK_REVIEW_BUNDLE.md: every v47 physiology section and v47.1 concept check,
numbered so a reviewer with the textbooks can return corrections by ID.
Run from the repo root: python textbook_xref/build_review_bundle.py"""
import importlib, pkgutil, os, sys
sys.path.insert(0, os.getcwd())
import pathophys_v470, cc_v471

DOMAIN = {"otology": "Otology / Neurotology", "rhinology": "Rhinology / Allergy / Skull Base",
          "head_neck": "Head & Neck Oncology", "thyroid": "Thyroid / Parathyroid / Salivary",
          "pediatric": "Pediatric Otolaryngology", "laryngology": "Laryngology / Voice / Swallowing",
          "facial_plastics": "Facial Plastics / Trauma", "sleep": "Sleep Surgery",
          "general_ent": "General ENT / Emergencies"}
ORDER = list(DOMAIN)

def dom(name):
    for k in ORDER:
        if name.startswith(k):
            return k
    raise KeyError(name)

topics = {k: {} for k in ORDER}
for info in sorted(pkgutil.iter_modules(pathophys_v470.__path__), key=lambda i: i.name):
    mod = importlib.import_module("pathophys_v470." + info.name)
    for t, e in mod.CONTENT.items():
        topics[dom(info.name)][t] = {"src": "pathophys_v470/%s.py" % info.name, **e, "checks": []}

orphans = []
for info in sorted(pkgutil.iter_modules(cc_v471.__path__), key=lambda i: i.name):
    mod = importlib.import_module("cc_v471." + info.name)
    d = dom(info.name)
    for i, row in enumerate(mod.CHECKS):
        rec = {"src": "cc_v471/%s.py" % info.name, "row": row}
        (topics[d][row[0]]["checks"] if row[0] in topics[d] else orphans).append((d, rec))

out = ["# ENT Mastery v47 textbook review bundle", "",
       "Reviewer instructions:",
       "- Check every factual statement below against Cummings 7e, Pasha & Golub 6e, K.J. Lee 12e, and (pediatric) Bluestone & Stool 5e.",
       "- Item IDs: `T-<domain>-<n>.<field>` for topic text (field = overview / physiology / pathophysiology) and `CC-<domain>-<n>.<k>` for concept checks.",
       "- Return results as `textbook_xref/corrections.csv` with columns:",
       "  `item_id, verdict (OK|CORRECT|UNSUPPORTED|CONFLICT), quoted_claim, book, edition_chapter, printed_page, book_text_excerpt (<=40 words), suggested_fix`",
       "- Only rows that need action are required; one OK row per topic with its best citation is enough to add the source.",
       "- `CONFLICT` = books disagree with each other; quote both. `UNSUPPORTED` = none of the four books covers it.",
       "- Do not edit the Python files; corrections.csv will be applied in the repo.", ""]
n_t = n_c = 0
for d in ORDER:
    out += ["", "---", "", "# %s" % DOMAIN[d], ""]
    for i, (t, e) in enumerate(sorted(topics[d].items()), 1):
        tid = "T-%s-%d" % (d, i)
        n_t += 1
        out += ["## %s — %s" % (tid, t), "_source: %s_" % e["src"], ""]
        for f in ("overview", "physiology", "pathophysiology"):
            out += ["**%s.%s**" % (tid, f), "", e.get(f, ""), ""]
        for k, (_, c) in enumerate(e["checks"], 1):
            n_c += 1
            topic, stem, correct, dis, expl, pearl = c["row"]
            cid = "CC-%s-%d.%d" % (d, i, k)
            out += ["### %s (concept check)" % cid, "", "Stem: " + stem, "",
                    "- **Correct:** " + correct]
            out += ["- Distractor: %s — _why wrong:_ %s" % (x, w) for x, w in dis]
            out += ["", "Explanation: " + expl, "", "Pearl: " + pearl, ""]
if orphans:
    out += ["", "---", "", "# Concept checks on legacy topic names", ""]
    for k, (d, c) in enumerate(orphans, 1):
        n_c += 1
        topic, stem, correct, dis, expl, pearl = c["row"]
        out += ["### CC-%s-legacy.%d — %s" % (d, k, topic), "", "Stem: " + stem, "", "- **Correct:** " + correct]
        out += ["- Distractor: %s — _why wrong:_ %s" % (x, w) for x, w in dis]
        out += ["", "Explanation: " + expl, "", "Pearl: " + pearl, ""]
out.insert(2, "Contents: %d topics, %d concept checks." % (n_t, n_c))
path = os.path.join("textbook_xref", "TEXTBOOK_REVIEW_BUNDLE.md")
open(path, "w").write("\n".join(out))
print(path, n_t, n_c, os.path.getsize(path))
