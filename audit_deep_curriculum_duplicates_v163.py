"""v16.3 — Deep Curriculum duplicate-architecture audit.

Reports exact/normalized duplicate topic names, high-similarity topic-name
pairs, and modules whose six-layer teaching content is nearly identical.
Informational only: the repair pass uses this output for explicit canonical
merges rather than deleting anything heuristically.
"""

from collections import defaultdict
from difflib import SequenceMatcher
import re

import runtime_entry


data = runtime_entry.data
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def norm_title(s):
    s = (s or "").lower()
    s = s.replace("&", " and ")
    s = re.sub(r"\b(the|of|and|with|after|during|for|in|to)\b", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def norm_text(s):
    s = re.sub(r"[^a-z0-9]+", " ", (s or "").lower())
    return " ".join(s.split())


def module_text(m):
    return " ".join(norm_text(m.get(k)) for k in FIELDS)


def main():
    exact = []
    fuzzy = []
    content = []
    total = 0

    for domain, mods in data.DEEP_MODULES_V6.items():
        total += len(mods)
        by_norm = defaultdict(list)
        for m in mods:
            by_norm[norm_title(m.get("topic"))].append(m.get("topic"))
        for key, topics in by_norm.items():
            if key and len(topics) > 1:
                exact.append((domain, topics))

        for i in range(len(mods)):
            a = mods[i]
            at = a.get("topic", "")
            an = norm_title(at)
            aw = set(an.split())
            atext = module_text(a)
            for j in range(i + 1, len(mods)):
                b = mods[j]
                bt = b.get("topic", "")
                bn = norm_title(bt)
                bw = set(bn.split())
                if not an or not bn:
                    continue
                ratio = SequenceMatcher(None, an, bn).ratio()
                containment = 0.0
                if aw and bw:
                    containment = len(aw & bw) / min(len(aw), len(bw))
                if ratio >= 0.72 or (containment >= 0.80 and min(len(aw), len(bw)) >= 2):
                    fuzzy.append((domain, at, bt, ratio, containment))

                btext = module_text(b)
                if len(atext) >= 250 and len(btext) >= 250:
                    tr = SequenceMatcher(None, atext, btext).ratio()
                    if tr >= 0.68:
                        content.append((domain, at, bt, tr))

    print(f"DEEP_DUP_AUDIT|topics={total}")
    print(f"EXACT_NORMALIZED_DUP_GROUPS|{len(exact)}")
    for domain, topics in exact:
        print("EXACT_NORMALIZED_DUP|" + domain + "|" + " <> ".join(topics))

    print(f"FUZZY_TITLE_PAIRS|{len(fuzzy)}")
    for domain, a, b, ratio, containment in sorted(fuzzy, key=lambda x: max(x[3], x[4]), reverse=True):
        print(f"FUZZY_TITLE|{domain}|{a}|{b}|ratio={ratio:.2f}|containment={containment:.2f}")

    print(f"NEAR_IDENTICAL_CONTENT_PAIRS|{len(content)}")
    for domain, a, b, ratio in sorted(content, key=lambda x: x[3], reverse=True):
        print(f"NEAR_IDENTICAL_CONTENT|{domain}|{a}|{b}|ratio={ratio:.2f}")

    print("DEEP_DUP_AUDIT_MODE|informational")


if __name__ == "__main__":
    main()
