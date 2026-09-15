#!/usr/bin/env python3
"""v36.7 — fail closed on Cleft / Craniofacial Otologic-Airway Care learner continuity."""

import re
import runtime_entry_pasha as production
from concept_check_board_repair_v177 import _find_module

DOMAIN = "Pediatric Otolaryngology"
TOPIC = "Cleft / Craniofacial Otologic-Airway Care"
SOURCE_IDS = (
    "18qgoaazhvh-keujxtwdwxn1ho86pry-t",
    "14e4iy4xcjgpsymt5n7uyurgtidnhi-52",
    "112c9y0fb1z_7olp4allag2z-r8weuxvr",
)


def txt(value):
    return str(value or "").lower()


def semantic(value):
    """Normalize punctuation without weakening the required clinical phrase."""
    return re.sub(r"[^a-z0-9]+", " ", txt(value)).strip()


def main():
    data = production.runtime_entry.data
    app_mod = production.runtime_entry.app_mod
    failures = []

    canonical = [data._v6_item_id(domain, row.get("topic")) for domain, rows in data.DEEP_MODULES_V6.items() for row in rows]
    if len(canonical) != 325 or len(set(canonical)) != 325:
        failures.append(f"canonical_contract:{len(canonical)}:{len(set(canonical))}")
    rows = (data.DEEP_MODULES_V6 or {}).get(DOMAIN, []) or []
    if len(rows) != 40 or len({txt(row.get('topic')) for row in rows}) != 40:
        failures.append(f"pediatric_inventory:{len(rows)}")

    matches = [row for row in rows if str(row.get("topic") or "") == TOPIC]
    if len(matches) != 1:
        failures.append(f"canonical_target_count:{len(matches)}")
        row = None
    else:
        row = matches[0]

    cid = data._v6_item_id(DOMAIN, TOPIC)
    if row:
        deep_blob = " ".join(txt(row.get(field)) for field in ("recognize", "localize", "workup", "manage", "operate", "teach"))
        for anchor in ("longitudinal airway-hearing-speech", "eustachian", "developmental vital sign", "robin", "velopharyngeal", "universal prophylactic tubes", "rescue airway plan"):
            if anchor not in deep_blob:
                failures.append("deep_missing:" + anchor)

        tags = " ".join(txt(x) for x in (row.get("tags") or []))
        for alias in ("cleft palate", "robin sequence", "eustachian tube dysfunction", "velopharyngeal insufficiency"):
            if semantic(alias) not in semantic(tags + " " + deep_blob):
                failures.append("deep_alias_missing:" + alias)

        sources = " ".join(txt(x) for x in (row.get("source_basis") or []))
        source_requirements = {
            "cummings": ("cummings",),
            "pasha": ("pasha",),
            "k.j. lee": ("k.j. lee",),
            "acpa": ("american cleft palate craniofacial association", "acpa"),
            "aao-hnsf": ("aao-hnsf", "clinical practice guideline: tympanostomy tubes in children"),
        }
        for label, alternatives in source_requirements.items():
            if not any(anchor in sources for anchor in alternatives):
                failures.append("source_missing:" + label)
        for anchor in SOURCE_IDS:
            if anchor not in sources:
                failures.append("source_missing:" + anchor)
        meta = txt(row.get("source_metadata_v367"))
        for anchor in SOURCE_IDS:
            if anchor not in meta:
                failures.append("structured_source_missing:" + anchor)
        if "universal prophylactic" not in meta or "tensor tenopexy" not in meta:
            failures.append("evidence_distinction_missing")

    search_rows = list(app_mod._canonical_search_index())
    hub_url = "/concept/id/" + cid
    hub_rows = [item for item in search_rows if item.get("type") == "Curriculum concept" and item.get("url") == hub_url]
    search_blob = " ".join(txt(item.get("title")) + " " + txt(item.get("text")) for item in hub_rows)
    for alias in ("cleft palate", "robin sequence", "eustachian tube dysfunction", "velopharyngeal insufficiency"):
        if semantic(alias) not in semantic(search_blob):
            failures.append("alias_not_searchable:" + alias)

    related = []
    for question in list(data.CONCEPT_CHECKS_V112 or []):
        found = _find_module(question, data.DEEP_MODULES_V6, data._v6_item_id)
        if found and str(found.get("topic") or "") == TOPIC and str(question.get("domain") or "") == DOMAIN:
            related.append(question)
    if not related:
        failures.append("concept_check_missing")
    else:
        concept_blob = " ".join(txt(question.get("prompt")) + " " + txt(question.get("answer_text")) + " " + " ".join(txt(x) for x in (question.get("choices") or [])) for question in related)
        for anchor in ("hearing", "airway", "eustachian", "velopharyngeal", "robin"):
            if anchor not in concept_blob:
                failures.append("concept_teaching_missing:" + anchor)

    items = [item for item in data.get_adaptive_items_v120() if item.get("concept_id") == cid]
    levels = {int(item.get("level") or 0) for item in items}
    if levels != {1, 2, 3, 4, 5, 6}:
        failures.append("daily_levels_incomplete:" + repr(sorted(levels)))
    later = " ".join(txt(item.get("question")) + " " + txt(item.get("answer")) for item in items if int(item.get("level") or 0) >= 3)
    if not any(anchor in later for anchor in ("hearing", "audiolog", "effusion", "tube")):
        failures.append("daily_hearing_management_missing")
    if not any(anchor in later for anchor in ("airway", "sleep", "obstruction", "intubat")):
        failures.append("daily_airway_management_missing")
    if not any(anchor in later for anchor in ("velopharyngeal", "vpi", "adenoid", "speech")):
        failures.append("daily_speech_vpi_management_missing")

    client = production.app.test_client()
    page = client.get(hub_url)
    page_text = page.get_data(as_text=True).lower()
    if page.status_code != 200:
        failures.append(f"hub_http:{page.status_code}")
    for anchor in ("cleft", "cummings", "pasha", "k.j. lee", "eustachian", "robin"):
        if anchor not in page_text:
            failures.append("hub_render_missing:" + anchor)

    if failures:
        print("FAIL v36.7 pediatric cleft learner experience")
        for item in failures:
            print(" -", item)
        raise SystemExit(1)

    print("PASS v36.7 pediatric cleft learner experience")
    print("canonical_id=", cid)
    print("concept_checks=", [question.get("id") for question in related])
    print("daily_levels=", sorted(levels))


if __name__ == "__main__":
    main()
