#!/usr/bin/env python3
"""Fail closed on live post-neck-dissection cervical chyle-leak rescue."""

import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
app = runtime_entry_pasha.app


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def contains_all(blob, tokens):
    hay = norm(blob)
    return all(norm(token) in hay for token in tokens)


def main():
    failures = 0
    reg = data.OR_PREP_REGISTRY or {}
    targets = [(slug, op) for slug, op in reg.items() if "neck dissection" in norm(f"{slug} {(op or {}).get('title', '')}")]
    if not targets:
        return fail("no live neck-dissection OR target resolved")

    client = app.test_client()
    for slug, op in targets:
        postop = " ".join(str(x) for x in (op.get("postop") or []))
        checks = {
            "recognition/confirmation": ("milky", "fasting", "drain triglycerides", "chylomicrons"),
            "loss replacement/monitoring": ("fluid balance", "electrolytes", "protein", "wound/flap healing"),
            "nutrition-directed flow reduction": ("low-fat", "medium-chain-triglyceride", "nutrition"),
            "adjunct nuance": ("octreotide", "adjunct", "Compression dressings", "airway"),
            "non-dogmatic escalation": ("single universal milliliter cutoff", "substantial", "downward trajectory", "source control"),
            "definitive options": ("re-exploration", "lymphangiography", "embolization", "thoracoscopic thoracic-duct ligation"),
        }
        for label, tokens in checks.items():
            if not contains_all(postop, tokens):
                failures += fail(f"{slug}: missing {label}: {tokens}")

        if not op.get("neck_chyle_leak_rescue_v286"):
            failures += fail(f"{slug}: v28.6 live marker missing")

        sources = " ".join(str(x) for x in (op.get("sources") or []))
        for token in ("Cummings", "K. J. Lee", "Pasha", "Smith", "Picton"):
            if norm(token) not in norm(sources):
                failures += fail(f"{slug}: missing provenance token {token!r}")

        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures += fail(f"{slug}: /case-tomorrow HTTP {r.status_code}")
        rendered = r.get_data(as_text=True)
        for token in ("CHYLE-LEAK RECOGNITION", "medium-chain-triglyceride", "octreotide", "thoracic-duct/tributary embolization"):
            if norm(token) not in norm(rendered):
                failures += fail(f"{slug}: rendered route missing rescue token {token!r}")

    if failures:
        print(f"\nNeck chyle-leak rescue gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: live neck-dissection OR cards connect low-neck thoracic-duct danger anatomy to diagnostic confirmation, physiologic/nutritional rescue, non-dogmatic escalation and definitive cervical/IR/thoracic source control with traceable provenance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
