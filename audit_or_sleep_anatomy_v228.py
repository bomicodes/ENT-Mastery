"""Hard gate for v22.8 procedure-specific sleep-surgery OR Tomorrow anatomy."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_sleep_v228_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("hypoglossal",), ("digastric", "protrusor", "retrusor", "genioglossus", "intercostal", "pleura", "generator"), ("carina", "eustachian", "thyrothymic")),
    (("hyoid", "genioglossus"), ("genial tubercle", "tooth roots", "hyoid", "hypoglossal", "superior laryngeal", "thyroid cartilage"), ("carina", "eustachian", "facial nerve")),
]


def _find(reg, terms):
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms):
            return slug, op
    return None, None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    for terms, required, forbidden in CHECKS:
        slug, op = _find(reg, terms)
        label = "/".join(terms)
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if op.get("landmarks_v228") != "procedure-specific":
            failures.append(f"{slug}: landmarks_v228 procedure-specific marker missing")
        landmarks = " ".join(str(x) for x in (op.get("landmarks") or [])).lower()
        for term in required:
            if term not in landmarks:
                failures.append(f"{slug}: landmarks missing {term!r}")
        for term in forbidden:
            if term in landmarks:
                failures.append(f"{slug}: landmarks retain irrelevant family anatomy {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("SLEEP SURGERY OR v22.8 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} sleep-surgery procedures have reviewed v22.8 anatomy and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
