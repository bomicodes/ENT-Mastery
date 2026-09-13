#!/usr/bin/env python3
"""v31.6 — fail closed on Systemic Disease of the Nose / Sinuses learner continuity."""

import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Systemic Disease of the Nose / Sinuses"
CORE_SOURCE_IDS = (
    "18qgoaazhvh-keujxtwdwxn1ho86pry-t",
    "14e4iy4xcjgpsymt5n7uyurgtidnhi-52",
    "112c9y0fb1z_7olp4allag2z-r8weuxvr",
)
DEEP_ANCHORS = (
    "systemic-inflammatory/destructive phenotype",
    "granulomatosis with polyangiitis",
    "eosinophilic granulomatosis with polyangiitis",
    "sarcoidosis",
    "igg4-related disease",
    "serial ess is not a diagnostic",
)
ALIASES = (
    "granulomatosis with polyangiitis",
    "wegener granulomatosis",
    "egpa",
    "churg-strauss",
    "sarcoidosis",
    "igg4-related disease",
    "destructive sinonasal disease",
    "septal perforation",
    "saddle nose",
)


def text(value):
    return str(value or "").lower()


def main():
    data = production.runtime_entry.data
    app_mod = production.runtime_entry.app_mod
    modules = (data.DEEP_MODULES_V6 or {}).get(DOMAIN, []) or []
    checks = list(data.CONCEPT_CHECKS_V112 or [])
    adaptive = list(data.get_adaptive_items_v120())
    v6_item_id = data._v6_item_id
    failures = []

    canonical = [v6_item_id(domain, mod.get("topic")) for domain, rows in data.DEEP_MODULES_V6.items() for mod in rows]
    if len(canonical) != 325 or len(set(canonical)) != 325:
        failures.append(f"canonical_contract:{len(canonical)}:{len(set(canonical))}")
    if len(modules) != 42 or len({text(x.get('topic')) for x in modules}) != 42:
        failures.append(f"rhinology_inventory:{len(modules)}")

    matches = [mod for mod in modules if str(mod.get("topic") or "") == TOPIC]
    if len(matches) != 1:
        failures.append(f"canonical_target_count:{len(matches)}")
        mod = None
    else:
        mod = matches[0]

    cid = v6_item_id(DOMAIN, TOPIC)
    target_url = "/concept/id/" + cid
    search_rows = list(app_mod._canonical_search_index())
    client = production.app.test_client()

    if mod is not None:
        deep_blob = " ".join(str(mod.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        for anchor in DEEP_ANCHORS:
            if anchor not in deep_blob:
                failures.append("deep_path_missing:" + anchor)
        sources = " ".join(str(x) for x in (mod.get("source_basis") or [])).lower()
        for anchor in ("cummings", "pasha", "k.j. lee", "acr", "sarcoidosis", "igg4") + CORE_SOURCE_IDS:
            if anchor not in sources:
                failures.append("deep_source_missing:" + anchor)
        metadata = text(mod.get("source_metadata_v366"))
        for anchor in CORE_SOURCE_IDS:
            if anchor not in metadata:
                failures.append("structured_source_missing:" + anchor)

    hub_rows = [r for r in search_rows if r.get("type") == "Curriculum concept" and r.get("url") == target_url]
    if not hub_rows:
        failures.append("live_search_missing")
    else:
        searchable = " ".join(text(r.get("title")) + " " + text(r.get("text")) for r in hub_rows)
        for alias in ALIASES:
            if alias not in searchable:
                failures.append("alias_not_searchable:" + alias)

    related = [q for q in checks if str(q.get("concept_id") or "") == cid]
    if not related:
        failures.append("concept_check_missing")
    else:
        concept_blob = " ".join(text(q.get("prompt")) + " " + text(q.get("answer_text")) for q in related)
        for anchor in ("gpa", "egpa", "sarcoidosis", "igg4", "biopsy", "serial ess"):
            if anchor not in concept_blob:
                failures.append("concept_teaching_missing:" + anchor)
        refs = " ".join(text(ref.get("citation")) for q in related for ref in (q.get("source_refs_v230") or []) if isinstance(ref, dict))
        for anchor in ("cummings", "pasha", "k.j. lee", "acr", "ats"):
            if anchor not in refs:
                failures.append("concept_source_missing:" + anchor)
        for q in related:
            qid = str(q.get("id") or "")
            if not qid:
                continue
            page = client.get("/concept-check/" + qid)
            page_text = page.get_data(as_text=True).lower()
            if page.status_code != 200:
                failures.append(f"concept_check_http:{qid}:{page.status_code}")
            for anchor in ("cummings", "pasha", "k.j. lee"):
                if anchor not in page_text:
                    failures.append("concept_render_missing:" + qid + ":" + anchor)

    items = [x for x in adaptive if x.get("concept_id") == cid]
    levels = {int(x.get("level") or 0) for x in items}
    if levels != {1, 2, 3, 4, 5, 6}:
        failures.append("daily_levels_incomplete:" + repr(sorted(levels)))
    later = " ".join(text(x.get("question")) + " " + text(x.get("answer")) for x in items if int(x.get("level") or 0) >= 3)
    if not any(anchor in later for anchor in ("gpa", "vascul", "septal perfor", "systemic", "sarcoid", "biopsy", "anca")):
        failures.append("daily_not_systemic_specific")

    hub = client.get(target_url)
    hub_text = hub.get_data(as_text=True).lower()
    if hub.status_code != 200:
        failures.append(f"concept_hub_http:{hub.status_code}")
    for anchor in ("cummings", "pasha", "k.j. lee", "granulomatosis with polyangiitis"):
        if anchor not in hub_text:
            failures.append("hub_render_missing:" + anchor)

    if failures:
        print("FAIL v31.6 systemic sinonasal learner experience")
        for item in failures:
            print(" -", item)
        raise SystemExit(1)

    print("PASS v31.6 systemic sinonasal learner experience")
    print("canonical_id=", cid)
    print("related_concept_checks=", [q.get("id") for q in related])
    print("daily_levels=", sorted(levels))


if __name__ == "__main__":
    main()
