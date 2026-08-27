"""Hard gate for v22.7 procedure-specific surgical-tracheostomy OR Tomorrow anatomy."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_trach_v227_", suffix=".db")
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
    for s, candidate in reg.items():
        hay = (str(s) + " " + str((candidate or {}).get("title", ""))).lower()
        if "tracheostomy" in hay and not any(x in hay for x in ("laryngectomy", "tracheoesophageal puncture", "tep")):
            slug, op = s, candidate
            break
    if not op:
        failures.append("surgical tracheostomy: live OR module not found")
    else:
        if op.get("landmarks_v227") != "procedure-specific":
            failures.append(f"{slug}: landmarks_v227 procedure-specific marker missing")
        landmarks = " ".join(str(x) for x in (op.get("landmarks") or [])).lower()
        for term in ("cricoid", "strap", "thyroid isthmus", "tracheal rings", "recurrent laryngeal", "innominate"):
            if term not in landmarks:
                failures.append(f"{slug}: landmarks missing {term!r}")
        for term in ("carina", "eustachian", "facial nerve"):
            if term in landmarks:
                failures.append(f"{slug}: landmarks retain irrelevant family anatomy {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    if failures:
        print("TRACHEOSTOMY OR v22.7 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: surgical tracheostomy has reviewed v22.7 anatomy and renders successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
