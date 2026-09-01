#!/usr/bin/env python3
"""Fail closed on tracheostomy hemorrhage / TIF rescue in final Render assembly."""

import re
import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
app = runtime_entry_pasha.app
TARGET = "tracheostomy"


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def contains_all(blob, tokens):
    hay = norm(blob)
    return all(norm(token) in hay for token in tokens)


def main():
    failures = 0
    op = (data.OR_PREP_REGISTRY or {}).get(TARGET)
    if not op:
        return fail("missing live OR Tomorrow tracheostomy target")

    postop = " ".join(str(x) for x in (op.get("postop") or []))
    all_text = " ".join(
        str(x)
        for key in ("landmarks", "setup", "steps", "postop")
        for x in (op.get(key) or [])
    )
    checks = {
        "sentinel-bleed commitment point": ("sentinel bleed", "catastrophic", "tracheo-innominate"),
        "senior hemorrhage activation": ("senior ENT", "anesthesia", "resuscitation", "vascular"),
        "cuff tamponade": ("hyperinflate the cuff", "temporizing tamponade"),
        "do-not-remove tamponading tube": ("avoid casually removing", "only tamponade"),
        "digital innominate compression": ("digital compression", "pretracheal", "posterior manubrium", "Utley"),
        "simultaneous airway contamination control": ("airway contamination", "suction aggressively", "large-bore"),
        "fresh-tract protection": ("avoid blind repeated tube exchanges", "fresh tract"),
        "no unstable imaging delay": ("do not delay", "CT/bronchoscopy", "unstable"),
        "definitive vascular control": ("definitive open vascular control", "endovascular", "bridges, not endpoints"),
        "post-sentinel high-acuity follow-up": ("high-acuity observation", "spontaneous cessation"),
    }
    for label, tokens in checks.items():
        if not contains_all(postop, tokens):
            failures += fail(f"{TARGET}: missing {label}: {tokens}")

    # Preserve the pre-existing anatomy and false-passage/laryngectomy safety layers.
    # Normalize punctuation so clinically equivalent 'false-passage', 'false passage',
    # and 'mouth/nose' versus 'mouth or nose' wording do not create a false failure.
    protected_groups = {
        "innominate danger anatomy": (("innominate artery",),),
        "usual tracheal window": (("second through fourth tracheal rings",),),
        "fresh-tract false passage": (("false passage",),),
        "laryngectomy distinction": (("laryngectomy",), ("stoma",), ("mouth",), ("nose",)),
    }
    normalized_all = norm(all_text)
    for label, groups in protected_groups.items():
        if not all(any(norm(token) in normalized_all for token in group) for group in groups):
            failures += fail(f"{TARGET}: prior protected tracheostomy safety concept missing {label!r}")

    if not op.get("tracheostomy_hemorrhage_rescue_v283"):
        failures += fail("v28.3 live marker missing")

    sources = " ".join(str(x) for x in (op.get("sources") or []))
    for token in ("Cummings", "K. J. Lee", "Pasha", "National Tracheostomy Safety Project", "Joshi", "Heller"):
        if norm(token) not in norm(sources):
            failures += fail(f"missing provenance token {token!r}")

    client = app.test_client()
    r = client.get("/case-tomorrow", query_string={"q": op.get("title", TARGET)}, follow_redirects=True)
    if r.status_code >= 500:
        failures += fail(f"/case-tomorrow HTTP {r.status_code}")
    rendered = r.get_data(as_text=True)
    for token in ("sentinel bleed", "hyperinflate the cuff", "Utley maneuver", "tracheo-innominate"):
        if norm(token) not in norm(rendered):
            failures += fail(f"rendered tracheostomy route missing rescue token {token!r}")

    if failures:
        print(f"\nTracheostomy hemorrhage/TIF rescue gate FAILED with {failures} issue(s).")
        return 1
    print("PASS: live tracheostomy OR case preserves prior anatomy/false-passage safety and adds sentinel-bleed recognition, cuff/digital tamponade, simultaneous airway-resuscitation, definitive vascular escalation, route exposure, and source provenance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
