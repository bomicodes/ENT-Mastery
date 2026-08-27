"""Hard gate for v23.7 arytenoid-adduction OR Tomorrow anatomy and management."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_arytenoid_v237_", suffix=".db")
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
        if "arytenoid" in hay and "adduction" in hay:
            slug, op = candidate_slug, candidate
            break

    if not op:
        failures.append("arytenoid adduction: live OR module not found")
    else:
        if op.get("landmarks_v237") != "procedure-specific":
            failures.append(f"{slug}: landmarks_v237 marker missing")
        landmarks = " ".join(str(x) for x in (op.get("landmarks") or [])).lower()
        for term in ("posterior thyroid", "cricoarytenoid", "muscular process", "vocal process", "pyriform", "recurrent laryngeal"):
            if term not in landmarks:
                failures.append(f"{slug}: landmarks missing {term!r}")
        for term in ("eustachian", "thyrothymic", "carina"):
            if term in landmarks:
                failures.append(f"{slug}: landmarks retain irrelevant family anatomy {term!r}")

        if not op.get("arytenoid_adduction_management_v237"):
            failures.append(f"{slug}: arytenoid_adduction_management_v237 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in ("posterior gap", "vertical height mismatch", "type i medialization", "contralateral vocal-fold"):
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in ("stridor", "hematoma", "excessive medialization", "undercorrection", "overadduction"):
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")

        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("ARYTENOID ADDUCTION OR v23.7 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: arytenoid-adduction v23.7 anatomy/management are live and route renders")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
