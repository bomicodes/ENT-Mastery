"""Hard gate for v23.3 total-laryngectomy OR Tomorrow planning and rescue."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_laryngectomy_v233_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    slug = None
    op = None
    for candidate_slug, candidate in reg.items():
        hay = (str(candidate_slug) + " " + str((candidate or {}).get("title", ""))).lower()
        if "total" in hay and "laryngectomy" in hay:
            slug, op = candidate_slug, candidate
            break

    if not op:
        failures.append("total laryngectomy: live OR module not found")
    else:
        if not op.get("laryngectomy_management_v233"):
            failures.append(f"{slug}: laryngectomy_management_v233 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in ("tumor extent", "nutrition", "prior radiation", "permanent neck breather", "tracheoesophageal"):
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in ("neck stoma", "oral endotracheal intubation", "pharyngocutaneous fistula", "great vessels", "carotid"):
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("TOTAL LARYNGECTOMY OR v23.3 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: total-laryngectomy v23.3 planning/rescue content is live and renders successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
