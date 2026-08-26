"""v18.0 — exhaustive backend smoke audit for every user-facing navigation surface.

The older reliability gate intentionally tested only representative top-level routes.
This audit expands coverage to all sidebar destinations plus every live data-backed
child page reachable from those surfaces (labs, integrated cases, concept checks,
clinical challenges, and curriculum concept pages where discoverable).

It uses an isolated SQLite database and never mutates production state.
"""
import os
import tempfile

if not os.environ.get("DATABASE_URL"):
    os.environ["SQLITE_PATH"] = os.path.join(tempfile.gettempdir(), "ent_mastery_v180_routes.db")
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

import runtime_entry

app = runtime_entry.app
data = runtime_entry.data

client = app.test_client()
failures = []
seen = set()


def check(path, *, allowed=(200, 301, 302)):
    if not path or path in seen:
        return
    seen.add(path)
    try:
        r = client.get(path, follow_redirects=False)
        if r.status_code not in allowed:
            body = (r.get_data(as_text=True) or "")[:240].replace("\n", " ")
            failures.append(f"{path}|status={r.status_code}|{body}")
    except Exception as exc:
        failures.append(f"{path}|exception={type(exc).__name__}:{exc}")


# Every persistent left-sidebar / topbar destination.
for path in (
    "/",
    "/health",
    "/daily-adaptive?minutes=30",
    "/curriculum",
    "/curriculum/depth",
    "/clinical-challenges",
    "/concept-checks",
    "/integrated",
    "/case-tomorrow",
    "/case-tomorrow?q=thyroidectomy",
    "/lab",
    "/anatomy",
    "/progress",
    "/attending",
    "/mistakes",
    "/evidence",
    "/search?q=otosclerosis",
):
    check(path)

# Interpretation Atlas child links.
for slug in sorted((getattr(data, "INTERPRETATION_LABS", {}) or {}).keys()):
    check(f"/lab/{slug}")

# Every live Concept Check detail page.
for q in list(getattr(data, "CONCEPT_CHECKS_V112", []) or []):
    qid = q.get("id") if isinstance(q, dict) else None
    if qid:
        check(f"/concept-check/{qid}")

# Every live Clinical Challenge detail page.
for q in list(getattr(data, "CLINICAL_CHALLENGES_V119", []) or []):
    qid = q.get("id") if isinstance(q, dict) else None
    if qid:
        check(f"/clinical-challenge/{qid}")

# Every integrated-case detail page.
for case in list(getattr(data, "INTEGRATED_CASES", []) or []):
    cid = case.get("id") if isinstance(case, dict) else None
    if cid:
        check(f"/integrated/{cid}")

# Curriculum concept detail pages use live canonical IDs where a direct route exists.
# A 404 here means the app does not expose that route shape, so only probe when the
# URL rule is registered.
rules = {rule.rule for rule in app.url_map.iter_rules()}
concept_rule = next((r for r in rules if "<" in r and ("concept" in r or "curriculum" in r)), None)
if concept_rule:
    for domain, modules in (getattr(data, "DEEP_MODULES_V6", {}) or {}).items():
        for mod in modules or []:
            if not isinstance(mod, dict) or not mod.get("topic"):
                continue
            cid = data._v6_item_id(domain, mod["topic"])
            # Probe only route shapes we know how to populate safely.
            if concept_rule in ("/concept/<concept_id>", "/curriculum/<concept_id>"):
                check(concept_rule.replace("<concept_id>", cid))

print(f"V180_ROUTES_CHECKED|{len(seen)}")
print(f"V180_FAILURES|{len(failures)}")
for f in failures[:300]:
    print("FAIL|" + f)

if failures:
    raise SystemExit(1)
