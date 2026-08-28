"""Hard gate for v23.14 high-risk OR Tomorrow management review."""
import os, tempfile

_fd, _db = tempfile.mkstemp(prefix="ent_or_v2314_", suffix=".db")
os.close(_fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = _db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

EXPECT = {
    "tors": {
        "marker": "tors_management_v2314",
        "setup": ("exposure", "hemorrhage"),
        "postop": ("bleeding", "aspiration"),
    },
    "tracheostomy": {
        "marker": "tracheostomy_management_v2314",
        "setup": ("fresh tract", "rescue"),
        "postop": ("false passage", "tracheo-innominate"),
    },
    "csf-nasoseptal": {
        "marker": "csf_nasoseptal_management_v2314",
        "setup": ("intracranial-pressure", "reconstruction"),
        "postop": ("mening", "clear rhinorrhea"),
    },
    "vestibular-schwannoma": {
        "marker": "vestibular_schwannoma_management_v2314",
        "setup": ("hearing", "corridor"),
        "postop": ("facial", "hydrocephalus"),
    },
}

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    failures = []
    client = rt.app.test_client()

    for slug, spec in EXPECT.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from live registry")
            continue
        if not op.get(spec["marker"]):
            failures.append(f"{slug}: missing {spec['marker']}")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in spec["setup"]:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in spec["postop"]:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: route HTTP {r.status_code}")
        text = r.get_data(as_text=True).lower()
        for term in (spec["setup"][0], spec["postop"][0]):
            if term not in text:
                failures.append(f"{slug}: rendered route missing {term!r}")

    if failures:
        print("OR v23.14 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: v23.14 high-risk management review is live for", ", ".join(EXPECT))
finally:
    try:
        os.remove(_db)
    except OSError:
        pass
