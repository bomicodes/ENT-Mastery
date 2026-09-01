#!/usr/bin/env python3
"""Fail closed on live post-esophagoscopy cervical esophageal perforation rescue."""

import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
app = runtime_entry_pasha.app
TARGETS = ("esophageal-fb", "transnasal-esophagoscopy")


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
    client = app.test_client()

    for target in TARGETS:
        op = reg.get(target)
        if not op:
            failures += fail(f"missing live OR target {target!r}")
            continue

        postop = " ".join(str(x) for x in (op.get("postop") or []))
        checks = {
            "recognition/initial stabilization": ("esophageal perforation", "stop oral intake", "airway", "IV access"),
            "prompt CT definition": ("CT of the neck/chest", "extraluminal", "contamination"),
            "NPO/antimicrobial pathway": ("NPO", "broad-spectrum antimicrobial", "nutritional"),
            "selective contained nonoperative path": ("small", "contained cervical perforation", "stable patient", "close inpatient observation"),
            "source-control failure criteria": ("free leak", "mediastinal", "uncontrolled sepsis", "source-control failure"),
            "closure/escalation": ("endoscopic closure", "failed", "surgical consultation", "definitive source-control"),
        }
        for label, tokens in checks.items():
            if not contains_all(postop, tokens):
                failures += fail(f"{target}: missing {label}: {tokens}")

        if not op.get("esophageal_perforation_rescue_v285"):
            failures += fail(f"{target}: v28.5 live marker missing")

        sources = " ".join(str(x) for x in (op.get("sources") or []))
        for token in ("Cummings", "K. J. Lee", "Pasha", "Paspatis", "ESGE"):
            if norm(token) not in norm(sources):
                failures += fail(f"{target}: missing provenance token {token!r}")

        r = client.get("/case-tomorrow", query_string={"q": op.get("title", target)}, follow_redirects=True)
        if r.status_code >= 500:
            failures += fail(f"{target}: /case-tomorrow HTTP {r.status_code}")
        rendered = r.get_data(as_text=True)
        for token in ("esophageal perforation", "CT of the neck/chest", "contained cervical perforation", "endoscopic closure"):
            if norm(token) not in norm(rendered):
                failures += fail(f"{target}: rendered route missing rescue token {token!r}")

    if failures:
        print(f"\nEsophageal perforation rescue gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: live esophagoscopy/foreign-body OR cases convert perforation recognition into NPO/resuscitation, CT-defined contamination, selective contained-leak management, closure selection, source-control escalation, route exposure, and traceable provenance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
