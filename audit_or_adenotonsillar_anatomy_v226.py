"""Hard gate for v22.6 pediatric adenotonsillar OR Tomorrow anatomy."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_adenotonsillar_v226_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

REQUIRED_CHECKS = [
    (("tonsillectomy",), ("tonsil capsule", "constrictor", "palatogloss", "lower-pole", "glossopharyngeal", "carotid"), ("eustachian", "facial nerve")),
    (("adenoidectomy",), ("adenoid pad", "choana", "vomer", "torus tubarius", "eustachian", "soft palate", "prevertebral"), ("facial nerve", "tonsillar capsule")),
]


def _find(reg, terms, excludes=()):
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms) and not any(term in hay for term in excludes):
            return slug, op
    return None, None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    # Require distinct tonsillectomy and adenoidectomy modules if they are present in the
    # live registry. Exclusions prevent the combined T&A case from satisfying both checks.
    required_specs = [
        (("tonsillectomy",), ("adenoid", "lingual"), REQUIRED_CHECKS[0][1], REQUIRED_CHECKS[0][2]),
        (("adenoidectomy",), ("tonsil",), REQUIRED_CHECKS[1][1], REQUIRED_CHECKS[1][2]),
    ]
    found_any = False
    for terms, excludes, required, forbidden in required_specs:
        slug, op = _find(reg, terms, excludes)
        if not op:
            continue
        found_any = True
        if op.get("landmarks_v226") != "procedure-specific":
            failures.append(f"{slug}: landmarks_v226 procedure-specific marker missing")
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

    # If a combined T&A module exists, it must also receive combined oropharyngeal and
    # nasopharyngeal anatomy, but its absence does not create a false registry requirement.
    slug, op = _find(reg, ("tonsil", "adenoid"))
    if op:
        found_any = True
        if op.get("landmarks_v226") != "procedure-specific":
            failures.append(f"{slug}: combined T&A landmarks_v226 marker missing")
        landmarks = " ".join(str(x) for x in (op.get("landmarks") or [])).lower()
        for term in ("tonsil capsule", "constrictor", "choana", "torus tubarius", "velopharyngeal", "prevertebral"):
            if term not in landmarks:
                failures.append(f"{slug}: combined T&A landmarks missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: combined T&A /case-tomorrow HTTP {r.status_code}")

    if not found_any:
        failures.append("No live tonsillectomy/adenoidectomy OR module found for v22.6 audit")

    if failures:
        print("ADENOTONSILLAR OR v22.6 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: live pediatric adenotonsillar OR modules have reviewed v22.6 anatomy and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
