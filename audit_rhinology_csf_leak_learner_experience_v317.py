#!/usr/bin/env python3
"""v31.7 — fail closed on paired CSF leak diagnostic -> operative learner continuity."""

import runtime_entry_pasha as production

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPICS = ("CSF Rhinorrhea", "Endoscopic CSF Leak Repair / Nasoseptal Flap")
CORE_IDS = ("18qgoaazhvh-keujxtwdwxn1ho86pry-t", "14e4iy4xcjgpsymt5n7uyurgtidnhi-52", "112c9y0fb1z_7olp4allag2z-r8weuxvr")
ALIASES = {
    "CSF Rhinorrhea": ("csf leak", "cerebrospinal fluid rhinorrhea", "spontaneous csf leak", "skull-base leak", "meningoencephalocele"),
    "Endoscopic CSF Leak Repair / Nasoseptal Flap": ("endoscopic csf leak repair", "nasoseptal flap", "hadad-bassagasteguy", "vascularized septal flap", "rescue-flap"),
}
DEEP = {
    "CSF Rhinorrhea": ("beta-2 transferrin", "thin-slice", "idiopathic intracranial hypertension", "persistent confirmed cranial csf rhinorrhea"),
    "Endoscopic CSF Leak Repair / Nasoseptal Flap": ("high-flow", "nasoseptal", "lumbar drain is selective", "stop and re-localize"),
}


def text(v): return str(v or "").lower()


def main():
    data = production.runtime_entry.data
    app = production.runtime_entry.app_mod
    rows = (data.DEEP_MODULES_V6 or {}).get(DOMAIN, []) or []
    checks = list(data.CONCEPT_CHECKS_V112 or [])
    adaptive = list(data.get_adaptive_items_v120())
    v6id = data._v6_item_id
    failures = []
    canonical = [v6id(d, m.get("topic")) for d, mods in data.DEEP_MODULES_V6.items() for m in mods]
    if len(canonical) != 325 or len(set(canonical)) != 325: failures.append(f"canonical_contract:{len(canonical)}:{len(set(canonical))}")
    if len(rows) != 42 or len({text(x.get('topic')) for x in rows}) != 42: failures.append(f"rhinology_inventory:{len(rows)}")
    by_topic = {str(x.get("topic") or ""): x for x in rows}
    search = list(app._canonical_search_index())
    client = production.app.test_client()

    for topic in TOPICS:
        mod = by_topic.get(topic)
        if not mod:
            failures.append("canonical_missing:" + topic); continue
        cid = v6id(DOMAIN, topic)
        blob = " ".join(text(mod.get(k)) for k in ("recognize","localize","workup","manage","operate","teach"))
        for anchor in DEEP[topic]:
            if anchor not in blob: failures.append(f"deep_missing:{topic}:{anchor}")
        src = " ".join(text(x) for x in (mod.get("source_basis") or []))
        for anchor in ("cummings","pasha","k.j. lee","33099888","40650638") + CORE_IDS:
            if anchor not in src: failures.append(f"source_missing:{topic}:{anchor}")
        visible = " ".join(text(r.get("title"))+" "+text(r.get("text")) for r in search if r.get("type") == "Curriculum concept" and r.get("url") == "/concept/id/"+cid)
        if not visible: failures.append("search_missing:" + topic)
        for alias in ALIASES[topic]:
            if alias not in visible: failures.append(f"alias_not_searchable:{topic}:{alias}")
        related = [q for q in checks if str(q.get("concept_id") or "") == cid]
        if not related: failures.append("concept_missing:" + topic)
        refs = " ".join(text(ref.get("citation")) for q in related for ref in (q.get("source_refs_v230") or []) if isinstance(ref, dict))
        for anchor in ("cummings","pasha","k.j. lee"):
            if anchor not in refs: failures.append(f"concept_source_missing:{topic}:{anchor}")
        for q in related:
            qid = str(q.get("id") or "")
            if not qid: continue
            page = client.get("/concept-check/" + qid); rendered = page.get_data(as_text=True).lower()
            if page.status_code != 200: failures.append(f"concept_http:{qid}:{page.status_code}")
            for anchor in ("cummings","pasha","k.j. lee"):
                if anchor not in rendered: failures.append(f"concept_render_missing:{qid}:{anchor}")
        items = [x for x in adaptive if x.get("concept_id") == cid]
        levels = {int(x.get("level") or 0) for x in items}
        if levels != {1,2,3,4,5,6}: failures.append(f"daily_levels:{topic}:{sorted(levels)}")
        later = " ".join(text(x.get("question"))+" "+text(x.get("answer")) for x in items if int(x.get("level") or 0) >= 3)
        if topic == "CSF Rhinorrhea" and not any(a in later for a in ("csf","transferrin","skull base","encephalo")): failures.append("daily_not_csf_specific")
        if topic == "Endoscopic CSF Leak Repair / Nasoseptal Flap" and not any(a in later for a in ("flap","repair","skull base","leak")): failures.append("daily_not_repair_specific")
        hub = client.get("/concept/id/" + cid); hub_text = hub.get_data(as_text=True).lower()
        if hub.status_code != 200: failures.append(f"hub_http:{topic}:{hub.status_code}")
        for anchor in ("cummings","pasha","k.j. lee"):
            if anchor not in hub_text: failures.append(f"hub_source_missing:{topic}:{anchor}")

    if failures:
        print("FAIL v31.7 CSF leak learner experience")
        for f in failures: print(" -", f)
        raise SystemExit(1)
    print("PASS v31.7 CSF leak learner experience")
    print("topics=", TOPICS)

if __name__ == "__main__": main()
