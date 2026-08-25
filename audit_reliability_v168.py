"""Read-only-ish release gate for v16.8 runtime integrity.

Uses Flask's test client and an isolated SQLite database when run in CI.
"""
import os
import tempfile

if not os.environ.get("DATABASE_URL"):
    os.environ["SQLITE_PATH"] = os.path.join(tempfile.gettempdir(), "ent_mastery_v168_audit.db")
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

import runtime_entry
import db

app = runtime_entry.app
data = runtime_entry.data
app_mod = runtime_entry.app_mod

errors = []


def check(ok, message):
    if not ok:
        errors.append(message)


check(getattr(data, "RELIABILITY_V168", {}).get("concept_fuzzy_threshold") == 0.78,
      "v16.8 reliability layer not active")

aliases = dict(getattr(data, "RETIRED_CONCEPT_ALIASES_V167", {}) or {})
profiles = db.unified_mastery_profiles()
adaptive = db.adaptive_mastery_map()
for old, new in aliases.items():
    check(old not in profiles, f"retired profile ID still visible: {old}")
    check(old not in adaptive, f"retired adaptive ID still visible: {old}")

# Domain-first lookup must resolve a known relationship child in its canonical domain.
for topic, rel in list(getattr(data, "CURRICULUM_RELATIONSHIPS_V167", {}).items())[:8]:
    found = None
    for domain, mods in data.DEEP_MODULES_V6.items():
        if any(m.get("topic") == topic for m in mods):
            found = domain
            break
    if found:
        dname, mod = app_mod._find_deep_module_v94(found, topic)
        check(bool(mod and mod.get("topic") == topic and dname == found), f"domain-safe concept lookup failed: {topic}")

client = app.test_client()
smoke = ["/", "/health", "/daily-adaptive?minutes=30", "/curriculum", "/curriculum/depth",
         "/search?q=otosclerosis", "/clinical-challenges", "/concept-checks", "/integrated",
         "/lab", "/anatomy", "/progress", "/case-tomorrow", "/attending", "/mistakes", "/evidence"]
for path in smoke:
    r = client.get(path, follow_redirects=False)
    check(r.status_code in (200, 301, 302), f"route failed {path}: {r.status_code}")

# Bad adaptive payload should be rejected without exposing an exception.
r = client.post("/daily-adaptive/answer", json={"rating": "bad", "level": "bad"})
check(r.status_code == 400, f"invalid Daily Path payload returned {r.status_code}")

# Legacy case deep links should preserve a known target.
if data.INTEGRATED_CASES:
    cid = data.INTEGRATED_CASES[0].get("id")
    if cid:
        r = client.get(f"/case/{cid}", follow_redirects=False)
        check(r.status_code == 301 and f"/integrated/{cid}" in r.headers.get("Location", ""),
              "legacy case deep link did not preserve target")

if errors:
    print("V16.8 RELIABILITY AUDIT FAILED")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

print("V16.8 RELIABILITY AUDIT PASSED")
print(f"aliases={len(aliases)} profiles={len(profiles)} routes={len(smoke)}")
