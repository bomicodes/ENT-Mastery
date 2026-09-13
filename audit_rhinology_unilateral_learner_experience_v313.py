#!/usr/bin/env python3
"""v31.3 — fail closed on Unilateral Sinonasal Disease learner continuity.

The v35.6 clinical gate protects the disease-specific reasoning. This companion audit verifies
that the exact canonical row remains coherent across Deep Curriculum -> Concept Check ->
Daily Curriculum and that connected textbook provenance is visible through learner-facing
paths rather than surviving only as hidden metadata.
"""

import runtime_entry_pasha as production
from concept_check_board_repair_v177 import _find_module

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Unilateral Sinonasal Disease"
CORE_SOURCE_IDS = (
    "18qgoaazhvh-keujxtwdwxn1ho86pry-t",
    "14e4iy4xcjgpsymt5n7uyurgtidnhi-52",
    "112c9y0fb1z_7olp4allag2z-r8weuxvr",
)
DEEP_ANCHORS = (
    "unilateral disease is a diagnostic phenotype",
    "odontogenic",
    "fungal",
    "malignancy",
    "mri",
    "unsafe biopsy",
)
CONCEPT_ANCHORS = ("unilateral", "mass", "biopsy", "malign", "fungal", "odontogenic")


def text(value):
    return str(value or "").lower()


def fail(failures, message):
    failures.append(message)


def main():
    data = production.runtime_entry.data
    app_mod = production.runtime_entry.app_mod
    modules = (data.DEEP_MODULES_V6 or {}).get(DOMAIN, []) or []
    checks = list(data.CONCEPT_CHECKS_V112 or [])
    adaptive = list(data.get_adaptive_items_v120())
    v6_item_id = data._v6_item_id
    failures = []

    canonical = [
        v6_item_id(domain, mod.get("topic"))
        for domain, rows in data.DEEP_MODULES_V6.items()
        for mod in rows
    ]
    if len(canonical) != 325 or len(set(canonical)) != 325:
        fail(failures, f"canonical_contract:{len(canonical)}:{len(set(canonical))}")
    if len(modules) != 42 or len({text(x.get('topic')) for x in modules}) != 42:
        fail(failures, f"rhinology_inventory:{len(modules)}")

    matches = [mod for mod in modules if str(mod.get("topic") or "") == TOPIC]
    if len(matches) != 1:
        fail(failures, f"canonical_target_count:{len(matches)}")
        mod = None
    else:
        mod = matches[0]

    cid = v6_item_id(DOMAIN, TOPIC)
    target_url = "/concept/id/" + cid
    search_rows = list(app_mod._canonical_search_index())
    client = production.app.test_client()

    if mod is not None:
        deep_blob = " ".join(
            str(mod.get(k) or "")
            for k in ("recognize", "localize", "workup", "manage", "operate", "teach")
        ).lower()
        for anchor in DEEP_ANCHORS:
            if anchor not in deep_blob:
                fail(failures, "deep_path_missing:" + anchor)

        source_blob = " ".join(str(x) for x in (mod.get("source_basis") or [])).lower()
        for anchor in ("cummings", "pasha", "k.j. lee") + CORE_SOURCE_IDS:
            if anchor not in source_blob:
                fail(failures, "deep_source_missing:" + anchor)
        metadata = text(mod.get("source_metadata_v364"))
        for anchor in CORE_SOURCE_IDS:
            if anchor not in metadata:
                fail(failures, "structured_source_missing:" + anchor)

    hub_rows = [
        row for row in search_rows
        if row.get("type") == "Curriculum concept" and row.get("url") == target_url
    ]
    if not hub_rows:
        fail(failures, "live_search_missing")
    else:
        searchable = " ".join(text(r.get("title")) + " " + text(r.get("text")) for r in hub_rows)
        for anchor in ("unilateral sinonasal disease", "unilateral"):
            if anchor not in searchable:
                fail(failures, "curriculum_alias_not_searchable:" + anchor)

    related = []
    for q in checks:
        found = _find_module(q, data.DEEP_MODULES_V6, v6_item_id)
        if found and str(found.get("topic") or "") == TOPIC and str(q.get("domain") or "") == DOMAIN:
            related.append(q)
    if not related:
        fail(failures, "concept_check_missing")
    else:
        concept_blob = " ".join(
            text(q.get("prompt")) + " " + text(q.get("answer_text")) + " " +
            " ".join(text(c) for c in (q.get("choices") or []))
            for q in related
        )
        for anchor in CONCEPT_ANCHORS:
            if anchor not in concept_blob:
                fail(failures, "concept_teaching_missing:" + anchor)
        refs = " ".join(
            text(ref.get("citation"))
            for q in related
            for ref in (q.get("source_refs_v230") or [])
            if isinstance(ref, dict)
        )
        for anchor in ("cummings", "pasha", "k.j. lee"):
            if anchor not in refs:
                fail(failures, "concept_source_missing:" + anchor)
        for q in related:
            qid = str(q.get("id") or "")
            if not qid:
                continue
            rows = [r for r in search_rows if r.get("type") == "Concept Check" and r.get("url") == "/concept-check/" + qid]
            if not rows:
                fail(failures, "concept_search_missing:" + qid)
            page = client.get("/concept-check/" + qid)
            page_text = page.get_data(as_text=True).lower()
            if page.status_code != 200:
                fail(failures, f"concept_check_http:{qid}:{page.status_code}")
            for anchor in ("unilateral", "cummings", "pasha", "k.j. lee"):
                if anchor not in page_text:
                    fail(failures, "concept_render_missing:" + qid + ":" + anchor)

    items = [x for x in adaptive if x.get("concept_id") == cid]
    levels = {int(x.get("level") or 0) for x in items}
    if levels != {1, 2, 3, 4, 5, 6}:
        fail(failures, "daily_levels_incomplete:" + repr(sorted(levels)))
    later = " ".join(
        text(x.get("question")) + " " + text(x.get("answer"))
        for x in items if int(x.get("level") or 0) >= 3
    )
    if "unilateral" not in later or not any(x in later for x in ("biopsy", "malign", "fungal", "odontogenic", "mri")):
        fail(failures, "daily_not_disease_specific")

    hub = client.get(target_url)
    hub_text = hub.get_data(as_text=True).lower()
    if hub.status_code != 200:
        fail(failures, f"concept_hub_http:{hub.status_code}")
    for anchor in ("unilateral sinonasal disease", "cummings", "pasha", "k.j. lee"):
        if anchor not in hub_text:
            fail(failures, "hub_render_missing:" + anchor)

    if failures:
        print("FAIL v31.3 unilateral learner experience")
        for item in failures:
            print(" -", item)
        raise SystemExit(1)

    print("PASS v31.3 unilateral learner experience")
    print("canonical_id=", cid)
    print("related_concept_checks=", [q.get("id") for q in related])
    print("daily_levels=", sorted(levels))


if __name__ == "__main__":
    main()
