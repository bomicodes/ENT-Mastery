#!/usr/bin/env python3
"""v34.2 — hard-gate facial-plastics graft semantic split and bailout choreography.

Checks the final Render production assembly rather than the patch source so future
rebuilds cannot silently collapse structural rhinoplasty grafting into skin-graft
coverage or remove the chief-resident rescue actions added in v34.2.
"""

import sys
import runtime_entry_pasha


data = runtime_entry_pasha.runtime_entry.data
DOMAIN = "Facial Plastics / Trauma"
RHINO = "Rhinoplasty Graft Selection"
SKIN = "Skin Graft Selection"


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def find_topic(topic):
    rows = (getattr(data, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [row for row in rows if str(row.get("topic", "")).strip().lower() == topic.lower()]
    if len(matches) != 1:
        return None, f"expected exactly one live {topic!r} record, found {len(matches)}"
    return matches[0], None


def text(row, *fields):
    return " ".join(str(row.get(field, "")) for field in fields).lower()


def require_any(blob, terms, label):
    if not any(term.lower() in blob for term in terms):
        return fail(f"lost {label}; expected one of {terms}")
    return 0


def main():
    failures = 0
    rhino, err = find_topic(RHINO)
    if err:
        failures += fail(err)
    skin, err = find_topic(SKIN)
    if err:
        failures += fail(err)
    if failures:
        return 1

    if rhino.get("semantic_role_v341") != "nasal structural biomechanics, graft geometry, and donor-material selection":
        failures += fail("rhinoplasty semantic role drifted from structural nasal biomechanics")
    if skin.get("semantic_role_v341") != "cutaneous wound-bed assessment, graft thickness selection, take physiology, and surface coverage":
        failures += fail("skin-graft semantic role drifted from wound-bed/coverage biology")
    if not rhino.get("facialplastics_graft_rescue_v342") or not skin.get("facialplastics_graft_rescue_v342"):
        failures += fail("v34.2 rescue marker missing from one or both live records")

    rhino_blob = text(rhino, "recognize", "localize", "workup", "manage", "operate", "teach")
    skin_blob = text(skin, "recognize", "localize", "workup", "manage", "operate", "teach")

    for terms, label in [
        (["spreader", "septal extension"], "structural graft-geometry anchors"),
        (["costal cartilage", "rib graft"], "costal-cartilage donor selection"),
        (["pleural", "pneumothorax"], "rib-harvest chest complication recognition"),
        (["alert anesthesia", "ventilation", "oxygenation"], "coordinated pleural-injury rescue"),
        (["decompression", "drainage"], "significant pneumothorax rescue endpoint"),
        (["abandon further rib harvest", "stop-assess-control-rescue"], "donor-safety bailout/commitment rule"),
    ]:
        failures += require_any(rhino_blob, terms, f"{RHINO}: {label}")

    for terms, label in [
        (["vascularized recipient bed", "vascular bed"], "recipient-bed requirement"),
        (["plasmatic imbibition"], "plasmatic-imbibition physiology"),
        (["inosculation"], "inosculation physiology"),
        (["hematoma", "seroma"], "subgraft fluid failure mechanism"),
        (["restore intimate graft-to-bed contact", "re-secure", "immobilize"], "early separation rescue"),
        (["reassess the recipient bed", "avascular bed"], "cause-based failure bailout"),
    ]:
        failures += require_any(skin_blob, terms, f"{SKIN}: {label}")

    # Exclude the explicit chief-level contrast sentence from the rhinoplasty negative
    # check. Mentioning FTSG/STSG only to say “this is not that decision” is desirable;
    # actual collapse would put take physiology/thickness-selection into the clinical
    # recognition/workup/management/operative pathway itself.
    rhino_clinical_path = text(rhino, "recognize", "localize", "workup", "manage", "operate")
    if any(term in rhino_clinical_path for term in ("plasmatic imbibition", "inosculation", "neovascularization", "full-thickness skin graft", "split-thickness skin graft")):
        failures += fail("rhinoplasty clinical pathway collapsed into cutaneous skin-graft take biology")
    if "spreader graft" in skin_blob or "septal extension" in skin_blob or "costal cartilage" in skin_blob:
        failures += fail("skin-graft teaching collapsed into structural nasal graft selection")

    sources_rhino = " ".join(str(x) for x in rhino.get("source_basis") or []).lower()
    sources_skin = " ".join(str(x) for x in skin.get("source_basis") or []).lower()
    for source in ("cummings", "k.j. lee", "pasha"):
        if source not in sources_rhino:
            failures += fail(f"{RHINO}: missing textbook provenance token {source!r}")
        if source not in sources_skin:
            failures += fail(f"{SKIN}: missing textbook provenance token {source!r}")
    if "varadharajan" not in sources_rhino or "updated meta-analysis" not in sources_rhino:
        failures += fail(f"{RHINO}: missing literature provenance for costal-cartilage donor-site rescue")

    if failures:
        print(f"\nFacial graft rescue semantic gate FAILED with {failures} issue(s).")
        return 1

    print("PASS: facial-plastics graft selection remains semantically distinct and rescue-ready in the final Render assembly.")
    print("  Rhinoplasty: framework/force -> graft geometry/material -> rib-harvest pleural bailout.")
    print("  Skin graft: vascular bed -> FTSG/STSG/take physiology -> hematoma/seroma/shear rescue.")
    print("  Cummings/K.J. Lee/Pasha provenance remains attached; costal donor-site literature is retained.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
