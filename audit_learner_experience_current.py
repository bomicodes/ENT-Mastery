"""Persistent learner-experience audit for ENT Mastery.

Discoverability, source visibility, and teaching flow are release requirements. A concept can be
factually complete yet still fail if an ENT resident cannot find the diagnosis, management path,
or evidence where the actual Deep Curriculum -> Concept Check -> Daily Curriculum journey exposes it.
"""
from pathlib import Path

import runtime_entry
from concept_check_board_repair_v177 import _find_module

CONTRACTS = {
    "cc-v112-rec-rhinology-allergy-skull-base-sinonasal-malignancy": {
        "canonical_topic": "Sinonasal Malignancy",
        "concept_id": "v6-rhinology-allergy-skull-base-sinonasal-malignancy",
        "heading": "### Esthesioneuroblastoma (Olfactory Neuroblastoma; ONB) — management pathway",
        "aliases": ("esthesioneuroblastoma", "olfactory neuroblastoma", "onb", "esthesioblastoma"),
        "required_terms": (
            "hyams", "kadish", "surgical resection", "adjuvant radiotherapy",
            "induction chemotherapy", "node-positive", "cn0", "elective neck irradiation",
            "20 years", "surveillance",
        ),
        "minimum_subsection_words": 500,
    },
}

SOURCE_ANCHORS = (
    "cummings", "18qgoaazhvh-keujxtwdwxn1ho86pry-t",
    "pasha", "14e4iy4xcjgpsymt5n7uyurgtidnhi-52",
    "k.j. lee", "112c9y0fb1z_7olp4allyg2z-r8weuxvr",
    "esmo", "39986703", "refcor", "42442982", "34254061",
)


def _text(value):
    return str(value or "").lower()


def main():
    data = runtime_entry.data
    app_mod = runtime_entry.app_mod
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []

    # The canonical contract itself is part of learner-experience safety: this repair may deepen
    # one topic but must never create a duplicate/326th topic.
    canonical = [v6_item_id(domain, mod.get("topic")) for domain, mods in deep_modules.items() for mod in mods]
    if len(canonical) != 325 or len(set(canonical)) != 325:
        failures.append("learner_canonical_contract:" + str(len(canonical)) + ":" + str(len(set(canonical))))

    for qid, contract in CONTRACTS.items():
        q = by.get(qid)
        if q is None:
            failures.append("learner_missing_concept:" + qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != contract["canonical_topic"] or cid != contract["concept_id"]:
            failures.append("learner_wrong_canonical:" + qid)
            continue

        # Concept Check: the ONB pathway must be explicit learner-facing prose, not metadata.
        answer = str(q.get("answer_text") or "")
        heading = contract["heading"]
        if heading not in answer:
            failures.append("learner_not_discoverable:" + qid + ":missing_heading")
            section = ""
        else:
            section = answer.split(heading, 1)[1]
        low = section.lower()
        if len(section.split()) < contract["minimum_subsection_words"]:
            failures.append("learner_path_too_shallow:" + qid + ":" + str(len(section.split())))
        for term in contract["required_terms"]:
            if term not in low:
                failures.append("learner_path_missing_management:" + qid + ":" + term)
        for verb in ("resect", "radiotherapy", "consider", "surveillance"):
            if verb not in low:
                failures.append("learner_actionability:" + qid + ":" + verb)

        aliases = {str(x).strip().lower() for x in q.get("search_aliases") or []}
        for alias in contract["aliases"]:
            if alias not in aliases:
                failures.append("learner_alias_missing:" + qid + ":" + alias)

        # Deep Curriculum: ONB must be visible in the actual six-layer card, not only in the
        # Concept Check. Management/advanced/teaching layers are intentionally required.
        deep_blob = " ".join(str(module.get(k) or "") for k in ("recognize", "localize", "workup", "manage", "operate", "teach")).lower()
        for alias in contract["aliases"]:
            if alias not in deep_blob:
                failures.append("deep_alias_not_visible:" + qid + ":" + alias)
        for field, anchors in {
            "workup": ("hyams", "kadish", "ct", "mri", "neck"),
            "manage": ("surgery", "radiotherapy", "induction", "cn0", "neck"),
            "operate": ("endoscopic", "open", "margin", "skull base"),
            "teach": ("surveillance", "20 years"),
        }.items():
            blob = _text(module.get(field))
            for anchor in anchors:
                if anchor not in blob:
                    failures.append("deep_layer_missing:" + qid + ":" + field + ":" + anchor)

        # Sources must surface through the Concept Hub's learner-facing source_basis and through
        # the Concept Check answer UI; source_refs metadata alone is insufficient.
        source_basis = " ".join(str(x) for x in (module.get("source_basis") or [])).lower()
        source_refs = " ".join(str(x.get("citation") or "") for x in (q.get("source_refs_v230") or []) if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in source_basis:
                failures.append("deep_source_not_visible:" + qid + ":" + anchor)
            if anchor not in source_refs:
                failures.append("concept_source_missing:" + qid + ":" + anchor)

        # Searchability: every synonym must resolve the exact canonical curriculum row through
        # the live search index, rather than only existing in a hidden alias list.
        rows = list(app_mod._canonical_search_index())
        target_url = "/concept/id/" + contract["concept_id"]
        for alias in contract["aliases"]:
            matches = [r for r in rows if r.get("type") == "Curriculum concept" and r.get("url") == target_url and alias in _text(r.get("title")) + " " + _text(r.get("text"))]
            if not matches:
                failures.append("live_search_alias_missing:" + qid + ":" + alias)

        # Daily Curriculum data path: exact canonical ID, all six levels, and ONB-specific
        # teaching answers at evaluation -> teaching stages. This catches fragmentation where
        # the page asks ONB but the reveal still serves only a generic sinonasal-malignancy answer.
        items = [x for x in data.get_adaptive_items_v120() if x.get("concept_id") == contract["concept_id"]]
        levels = {int(x.get("level") or 0) for x in items}
        if levels != {1, 2, 3, 4, 5, 6}:
            failures.append("daily_levels_incomplete:" + qid + ":" + repr(sorted(levels)))
        for item in items:
            level = int(item.get("level") or 0)
            answer_low = _text(item.get("answer"))
            if level >= 3 and not ("onb" in answer_low or "esthesioneuroblastoma" in answer_low or "olfactory neuroblastoma" in answer_low):
                failures.append("daily_answer_not_onb_specific:" + qid + ":level" + str(level))

        # Learner-facing templates must explicitly expose ONB Daily prompts and render source
        # citations in the Concept Check. A metadata-only repair fails closed.
        daily_template = Path("templates/daily_adaptive.html").read_text(encoding="utf-8").lower()
        concept_template = Path("templates/concept_check.html").read_text(encoding="utf-8").lower()
        for anchor in (contract["concept_id"], "esthesioneuroblastoma", "hyams", "cn0", "negative-margin", "20 years"):
            if anchor not in daily_template:
                failures.append("daily_ui_path_missing:" + qid + ":" + anchor)
        for anchor in ("source_refs_v230", "sources for this repaired pathway", "learner-facing answer path"):
            if anchor not in concept_template:
                failures.append("concept_source_ui_missing:" + qid + ":" + anchor)

        # Render-level smoke checks ensure the source/management path survives the live Flask UI.
        client = runtime_entry.app.test_client()
        hub = client.get("/concept/id/" + contract["concept_id"])
        hub_text = hub.get_data(as_text=True).lower()
        if hub.status_code != 200:
            failures.append("concept_hub_http:" + qid + ":" + str(hub.status_code))
        for anchor in ("olfactory neuroblastoma", "cummings", "refcor", "39986703"):
            if anchor not in hub_text:
                failures.append("concept_hub_render_missing:" + qid + ":" + anchor)
        check_page = client.get("/concept-check/" + qid)
        check_text = check_page.get_data(as_text=True).lower()
        if check_page.status_code != 200:
            failures.append("concept_check_http:" + qid + ":" + str(check_page.status_code))
        for anchor in ("esthesioneuroblastoma", "sources for this repaired pathway", "cummings", "refcor"):
            if anchor not in check_text:
                failures.append("concept_check_render_missing:" + qid + ":" + anchor)

    print("LEARNER_EXPERIENCE_CONTRACTS|" + str(len(CONTRACTS)))
    print("LEARNER_EXPERIENCE_FAILURES|" + str(len(failures)))
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: Deep Curriculum -> Concept Check -> Daily Curriculum learner paths, aliases, management decisions, and learner-visible sources satisfy the fail-closed contracts")


if __name__ == "__main__":
    main()
