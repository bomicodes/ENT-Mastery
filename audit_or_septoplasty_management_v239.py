"""Hard gate for v23.9 septoplasty OR Tomorrow planning and postoperative rescue."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_septoplasty_v239_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

REQUIRED_SETUP = (
    "functional deformity",
    "nasal-valve",
    "l-strut",
    "keystone",
)
REQUIRED_POSTOP = (
    "septal hematoma",
    "mucoperichondrium",
    "saddle-nose",
    "clear unilateral rhinorrhea",
    "visual symptoms",
    "valve collapse",
)

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    slug = None
    op = None
    for candidate_slug, candidate in reg.items():
        hay = (str(candidate_slug) + " " + str((candidate or {}).get("title", ""))).lower()
        if "septoplasty" in hay:
            slug, op = candidate_slug, candidate
            break

    if not op:
        failures.append("septoplasty: live OR module not found")
    else:
        if not op.get("septoplasty_management_v239"):
            failures.append(f"{slug}: septoplasty_management_v239 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in REQUIRED_SETUP:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in REQUIRED_POSTOP:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("SEPTOPLASTY OR v23.9 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: septoplasty has reviewed v23.9 planning/postoperative management and renders successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
