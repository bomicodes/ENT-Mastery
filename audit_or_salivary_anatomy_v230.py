"""Hard gate for v23.0 procedure-specific salivary OR Tomorrow anatomy."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_salivary_v230_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("superficial", "parotid"), ("facial nerve", "tragal pointer", "retromandibular", "stensen", "greater auricular"), ("lingual nerve", "wharton")),
    (("total", "parotid"), ("facial nerve", "deep lobe", "retromandibular", "external carotid", "parapharyngeal"), ("wharton", "hypoglossal nerve deep/inferior")),
    (("submandibular", "gland"), ("marginal mandibular", "facial artery", "mylohyoid", "lingual nerve", "wharton", "hypoglossal"), ("tragal pointer", "retromandibular")),
    (("sialendosc",), ("papilla", "wharton", "stensen", "branch points", "lingual nerve"), ("facial nerve main trunk", "retromandibular vein")),
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
        if op.get("landmarks_v230") != "procedure-specific":
            failures.append(f"{slug}: landmarks_v230 procedure-specific marker missing")
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
        print("SALIVARY OR v23.0 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} salivary procedures have reviewed v23.0 anatomy and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
