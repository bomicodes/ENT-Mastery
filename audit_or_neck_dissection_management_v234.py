"""Hard gate for v23.4 neck-dissection OR Tomorrow planning/postoperative management."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_neck_dissection_v234_", suffix=".db")
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
        if "neck" in hay and "dissection" in hay and "central neck" not in hay:
            slug, op = candidate_slug, candidate
            break

    if not op:
        failures.append("neck-dissection: live OR module not found")
    else:
        if not op.get("neck_dissection_management_v234"):
            failures.append(f"{slug}: neck_dissection_management_v234 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in ("nodal levels", "baseline shoulder", "thoracic-duct", "bilateral ijv"):
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in ("chyle leak", "medium-chain", "shoulder", "carotid blowout"):
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("NECK DISSECTION OR v23.4 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: neck dissection has reviewed v23.4 planning/rescue content and renders successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
