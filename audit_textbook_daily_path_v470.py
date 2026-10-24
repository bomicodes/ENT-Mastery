"""v47.0 release gate: textbook Deep Curriculum, curated links, rebuilt Daily Path.

Checks against the real production entrypoint (daily_path_entry_v403):
  * every canonical topic has overview / physiology / pathophysiology content
  * no leaked internal authoring tags ("v40.8 priority completion", "v44.1 ...:")
  * the curated topic -> OR map covers exactly the live topics, every slug exists,
    and every mapped OR title lands directly on its card in OR Tomorrow
  * every topic has Daily Path questions at Foundation, Application and Mastery
  * no auto-generated template concept checks reach the Daily Path
  * key routes render
"""
import os
import re
import sys

os.environ.setdefault("ENT_MASTERY_AUDIT_MODE", "1")
import daily_path_entry_v403 as entry

rt = entry.production.runtime_entry
data, app_mod = rt.data, rt.app_mod
failures = []


def fail(msg):
    failures.append(msg)


topics = [(d, m) for d, mods in data.DEEP_MODULES_V6.items() for m in mods]
for d, m in topics:
    for f in ("overview", "physiology", "pathophysiology"):
        if len((m.get(f) or "").strip()) < 120:
            fail("thin_or_missing_%s:%s" % (f, m["topic"]))
    for f in ("recognize", "localize", "workup", "manage", "operate", "teach"):
        if re.search(r"\bv\d{2}\.\d+\b", m.get(f) or ""):
            fail("leaked_version_tag:%s:%s" % (m["topic"], f))

live = {m["topic"] for _, m in topics}
mapped = set(data.TOPIC_OR_MAP_V470)
if live != mapped:
    fail("or_map_mismatch: missing=%s extra=%s" % (sorted(live - mapped)[:5], sorted(mapped - live)[:5]))
registry = app_mod.OR_PREP_REGISTRY
for slug in {s for v in data.TOPIC_OR_MAP_V470.values() for s in v}:
    op = registry.get(slug)
    if not op:
        fail("unknown_or_slug:" + slug)
        continue
    ranked = app_mod._or_rank(op["title"])
    if not ranked or ranked[0][2].get("title") != op["title"] or ranked[0][0] < 92:
        fail("or_title_not_direct:" + slug)

stats = data.LEARNING_PATH_V470
if stats["topics_with_all_phases"] != len(topics):
    fail("daily_path_phase_gap: %s/%s" % (stats["topics_with_all_phases"], len(topics)))

client = entry.app.test_client()
page = client.get("/daily-adaptive?minutes=60").data.decode()
if "curriculum framework" in page:
    fail("template_concept_check_in_daily_path")
for url in ("/daily-adaptive", "/daily-adaptive?topic=BPPV", "/curriculum/depth",
            "/curriculum/depth?domain=Otology%20/%20Neurotology&topic=BPPV",
            "/concept?domain=Head%20%26%20Neck%20Oncology&topic=Glottic%20Cancer"):
    r = client.get(url)
    if r.status_code != 200:
        fail("route_%s:%s" % (r.status_code, url))

if failures:
    print("FAIL", len(failures))
    for f in failures[:40]:
        print(" -", f)
    sys.exit(1)
print("PASS v47.0 textbook curriculum + Daily Path: %d topics, %d OR-mapped, %d questions indexed"
      % (len(topics), data.TEXTBOOK_CURRICULUM_V470["or_mapped_topics"], stats["questions_indexed"]))
