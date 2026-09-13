#!/usr/bin/env python3
"""v31.5 — fail closed on Facial Pain / Headache vs Rhinogenic Disease continuity."""

import runtime_entry_pasha as production
from concept_check_board_repair_v177 import _find_module

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Facial Pain / Headache vs Rhinogenic Disease"
SOURCE_IDS = (
    "18qgoaazhvh-keujxtwdwxn1ho86pry-t",
    "14e4iy4xcjgpsymt5n7uyurgtidnhi-52",
    "112c9y0fb1z_7olp4allag2z-r8weuxvr",
)


def txt(v):
    return str(v or "").lower()


def main():
    data = production.runtime_entry.data
    app_mod = production.runtime_entry.app_mod
    failures = []
    rows = (data.DEEP_MODULES_V6 or {}).get(DOMAIN, []) or []
    canonical = [data._v6_item_id(d, r.get("topic")) for d, rs in data.DEEP_MODULES_V6.items() for r in rs]
    if len(canonical) != 325 or len(set(canonical)) != 325:
        failures.append(f"canonical_contract:{len(canonical)}:{len(set(canonical))}")
    if len(rows) != 42 or len({txt(r.get('topic')) for r in rows}) != 42:
        failures.append(f"rhinology_inventory:{len(rows)}")

    matches = [r for r in rows if str(r.get("topic") or "") == TOPIC]
    if len(matches) != 1:
        failures.append(f"canonical_target_count:{len(matches)}")
        row = None
    else:
        row = matches[0]

    cid = data._v6_item_id(DOMAIN, TOPIC)
    if row:
        blob = " ".join(txt(row.get(k)) for k in ("recognize", "localize", "workup", "manage", "operate", "teach"))
        for anchor in ("sinus headache", "objective", "migraine", "trigeminal", "dental", "contact-point", "fess is not a diagnostic trial", "when not"):
            if anchor not in blob:
                failures.append("deep_missing:" + anchor)
        sources = " ".join(txt(x) for x in (row.get("source_basis") or []))
        for anchor in ("cummings", "pasha", "k.j. lee", "ichd-3") + SOURCE_IDS:
            if anchor not in sources:
                failures.append("source_missing:" + anchor)
        meta = txt(row.get("source_metadata_v365"))
        for anchor in SOURCE_IDS:
            if anchor not in meta:
                failures.append("structured_source_missing:" + anchor)

    search_rows = list(app_mod._canonical_search_index())
    hub_url = "/concept/id/" + cid
    hub_rows = [r for r in search_rows if r.get("type") == "Curriculum concept" and r.get("url") == hub_url]
    search_blob = " ".join(txt(r.get("title")) + " " + txt(r.get("text")) for r in hub_rows)
    for alias in ("sinus headache", "rhinogenic headache", "facial pressure", "migraine"):
        if alias not in search_blob:
            failures.append("alias_not_searchable:" + alias)

    related = []
    for q in list(data.CONCEPT_CHECKS_V112 or []):
        found = _find_module(q, data.DEEP_MODULES_V6, data._v6_item_id)
        if found and str(found.get("topic") or "") == TOPIC and str(q.get("domain") or "") == DOMAIN:
            related.append(q)
    if not related:
        failures.append("concept_check_missing")
    else:
        cblob = " ".join(txt(q.get("prompt")) + " " + txt(q.get("answer_text")) + " " + " ".join(txt(x) for x in (q.get("choices") or [])) for q in related)
        for anchor in ("migraine", "objective", "sinus"):
            if anchor not in cblob:
                failures.append("concept_teaching_missing:" + anchor)

    items = [x for x in data.get_adaptive_items_v120() if x.get("concept_id") == cid]
    levels = {int(x.get("level") or 0) for x in items}
    if levels != {1, 2, 3, 4, 5, 6}:
        failures.append("daily_levels_incomplete:" + repr(sorted(levels)))
    later = " ".join(txt(x.get("question")) + " " + txt(x.get("answer")) for x in items if int(x.get("level") or 0) >= 3)
    if "migraine" not in later or not any(x in later for x in ("objective", "endoscopy", "ct", "surgery", "fess")):
        failures.append("daily_not_specific")

    client = production.app.test_client()
    page = client.get(hub_url)
    page_text = page.get_data(as_text=True).lower()
    if page.status_code != 200:
        failures.append(f"hub_http:{page.status_code}")
    for anchor in ("facial pain", "cummings", "pasha", "k.j. lee", "ichd-3"):
        if anchor not in page_text:
            failures.append("hub_render_missing:" + anchor)

    if failures:
        print("FAIL v31.5 facial pain learner experience")
        for item in failures:
            print(" -", item)
        raise SystemExit(1)
    print("PASS v31.5 facial pain learner experience")
    print("canonical_id=", cid)
    print("concept_checks=", [q.get("id") for q in related])
    print("daily_levels=", sorted(levels))


if __name__ == "__main__":
    main()
