"""Hard gate for v23.8 pediatric adenotonsillar OR Tomorrow management."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_adenotonsillar_v238_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("tonsillectomy",), ("severe osa", "intracapsular", "extracapsular"), ("possible tonsillar hemorrhage", "npo", "dehydration"), ("adenoid", "lingual")),
    # Keep the adenoidectomy-only check from resolving to the combined T&A module.
    (("adenoidectomy",), ("submucous cleft", "velopharyngeal", "hypernasality"), ("velopharyngeal insufficiency", "neck pain", "bleeding"), ("tonsil",)),
    (("tonsillectomy", "adenoid"), ("polysomnographic", "postoperative disposition", "velopharyngeal"), ("post-tonsillectomy hemorrhage", "desaturation", "objective osa follow-up"), ()),
]


def _find(reg, terms, forbidden_terms=()):
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms) and not any(term in hay for term in forbidden_terms):
            return slug, op
    return None, None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    for terms, setup_required, postop_required, exclusions in CHECKS:
        slug, op = _find(reg, terms, exclusions)
        label = "/".join(terms)
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if not op.get("adenotonsillar_management_v238"):
            failures.append(f"{slug}: adenotonsillar_management_v238 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in setup_required:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in postop_required:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("ADENOTONSILLAR OR v23.8 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} adenotonsillar procedures have reviewed v23.8 management and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
