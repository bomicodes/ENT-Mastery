#!/usr/bin/env python3
"""v31.2 — fail closed on learner-facing Allergic Rhinitis/LAR continuity.

The v34.9 production gate already protects AR/LAR clinical/source semantics. This companion
audit verifies that those strong concepts remain discoverable and coherent across the actual
Deep Curriculum -> Concept Check -> Daily Curriculum learner journey, with sources rendered
through learner-facing paths rather than surviving only as hidden metadata.
"""
import sys

import runtime_entry
from concept_check_board_repair_v177 import _find_module

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPICS = {
    "Allergic Rhinitis": {
        "deep": ("specific ige", "intranasal", "immunotherapy", "structural"),
        "concept": ("allergic rhinitis", "testing", "intranasal", "immunotherapy"),
        "daily": ("allergic rhinitis", "ige", "allergen", "immunotherapy"),
        "sources": ("cummings", "pasha", "k.j. lee", "allergic rhinitis", "2015", "immunotherapy for inhalant allergy", "2024"),
    },
    "Local Allergic Rhinitis": {
        "deep": ("negative", "nasal allergen", "specific ige", "nares", "immunotherapy"),
        "concept": ("local allergic rhinitis", "negative", "nasal allergen"),
        "daily": ("local allergic rhinitis", "nasal allergen", "negative", "allergy"),
        "sources": ("cummings", "pasha", "k.j. lee", "local allergic rhinitis", "immunotherapy for inhalant allergy", "2024"),
    },
}
CORE_SOURCE_IDS = (
    "18qgoaazhvh-keujxtwdwxn1ho86pry-t",
    "14e4iy4xcjgpsymt5n7uyurgtidnhi-52",
    "112c9y0fb1z_7olp4allag2z-r8weuxvr",
)


def text(value):
    return str(value or "").lower()


def fail(failures, message):
    failures.append(message)


def main():
    data = runtime_entry.data
    app_mod = runtime_entry.app_mod
    modules = (data.DEEP_MODULES_V6 or {}).get(DOMAIN, []) or []
    checks = list(data.CONCEPT_CHECKS_V112 or [])
    adaptive = list(data.get_adaptive_items_v120())
    v6_item_id = data._v6_item_id
    failures = []

    canonical = [v6_item_id(domain, mod.get("topic")) for domain, rows in data.DEEP_MODULES_V6.items() for mod in rows]
    if len(canonical) != 325 or len(set(canonical)) != 325:
        fail(failures, f"canonical_contract:{len(canonical)}:{len(set(canonical))}")
    if len(modules) != 42:
        fail(failures, f"rhinology_inventory:{len(modules)}")

    by_topic = {str(mod.get("topic") or ""): mod for mod in modules}
    search_rows = list(app_mod._canonical_search_index())
    client = runtime_entry.app.test_client()

    for topic, contract in TOPICS.items():
        mod = by_topic.get(topic)
        if mod is None:
            fail(failures, "missing_canonical:" + topic)
            continue
        cid = v6_item_id(DOMAIN, topic)
        target_url = "/concept/id/" + cid

        deep_blob = " ".join(str(mod.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        if topic.lower() not in deep_blob:
            fail(failures, "deep_topic_not_visible:" + topic)
        for anchor in contract["deep"]:
            if anchor not in deep_blob:
                fail(failures, "deep_path_missing:" + topic + ":" + anchor)

        source_basis = " ".join(str(x) for x in (mod.get("source_basis") or [])).lower()
        for anchor in contract["sources"] + CORE_SOURCE_IDS:
            if anchor not in source_basis:
                fail(failures, "deep_source_missing:" + topic + ":" + anchor)

        search_hits = [r for r in search_rows if r.get("type") == "Curriculum concept" and r.get("url") == target_url and topic.lower() in (text(r.get("title")) + " " + text(r.get("text")))]
        if not search_hits:
            fail(failures, "live_search_missing:" + topic)

        related = []
        for q in checks:
            found = _find_module(q, data.DEEP_MODULES_V6, v6_item_id)
            if found and str(found.get("topic") or "") == topic and str(q.get("domain") or "") == DOMAIN:
                related.append(q)
        if not related:
            fail(failures, "concept_check_missing:" + topic)
        else:
            answers = " ".join(str(q.get("answer_text") or "") for q in related).lower()
            for anchor in contract["concept"]:
                if anchor not in answers:
                    fail(failures, "concept_teaching_missing:" + topic + ":" + anchor)
            refs = " ".join(str(ref.get("citation") or "") for q in related for ref in (q.get("source_refs_v230") or []) if isinstance(ref, dict)).lower()
            for anchor in ("cummings", "pasha", "k.j. lee"):
                if anchor not in refs:
                    fail(failures, "concept_source_missing:" + topic + ":" + anchor)

        items = [x for x in adaptive if x.get("concept_id") == cid]
        levels = {int(x.get("level") or 0) for x in items}
        if levels != {1, 2, 3, 4, 5, 6}:
            fail(failures, "daily_levels_incomplete:" + topic + ":" + repr(sorted(levels)))
        later = " ".join(str(x.get("answer") or "") for x in items if int(x.get("level") or 0) >= 3).lower()
        if not any(anchor in later for anchor in contract["daily"]):
            fail(failures, "daily_not_specific:" + topic)

        hub = client.get(target_url)
        hub_text = hub.get_data(as_text=True).lower()
        if hub.status_code != 200:
            fail(failures, "concept_hub_http:" + topic + ":" + str(hub.status_code))
        for anchor in (topic.lower(), "cummings", "pasha", "k.j. lee"):
            if anchor not in hub_text:
                fail(failures, "concept_hub_render_missing:" + topic + ":" + anchor)

        if related:
            qid = str(related[0].get("id") or "")
            page = client.get("/concept-check/" + qid)
            page_text = page.get_data(as_text=True).lower()
            if page.status_code != 200:
                fail(failures, "concept_check_http:" + topic + ":" + str(page.status_code))
            if topic.lower() not in page_text:
                fail(failures, "concept_check_render_missing:" + topic)
            for anchor in ("cummings", "pasha", "k.j. lee"):
                if anchor not in page_text:
                    fail(failures, "concept_source_render_missing:" + topic + ":" + anchor)

    print("RHINOLOGY_ALLERGY_LEARNER_CONTRACTS|" + str(len(TOPICS)))
    print("RHINOLOGY_ALLERGY_LEARNER_FAILURES|" + str(len(failures)))
    for item in failures:
        print("FAIL|" + item)
    if failures:
        return 1
    print("PASS: AR/LAR remain coherent and source-visible across Deep Curriculum -> Concept Check -> Daily Curriculum")
    return 0


if __name__ == "__main__":
    sys.exit(main())
