"""Hard gate for v23.11 procedure-specific salivary OR Tomorrow management."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_salivary_v2311_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    ("parotidectomy", ("parotidectomy",), ("branch territory", "cornea", "sialocele", "frey")),
    ("parotid-total", ("total", "parotid"), ("deep-lobe", "nerve sacrifice", "eye closure", "salivary")),
    ("submandibular-gland", ("submandibular", "gland"), ("tongue protrusion", "hypoglossal", "lingual-nerve", "floor-of-mouth")),
    ("sialendoscopy", ("sialendosc",), ("combined", "duct perforation", "lingual-nerve", "restenosis")),
]


def _find(reg, slug_hint, terms):
    if slug_hint in reg:
        return slug_hint, reg[slug_hint]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms):
            if slug_hint == "parotidectomy" and "total" in hay:
                continue
            return slug, op
    return None, None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    for slug_hint, terms, required in CHECKS:
        slug, op = _find(reg, slug_hint, terms)
        if not op:
            failures.append(f"{slug_hint}: live OR module not found")
            continue
        if not op.get("salivary_management_v2311"):
            failures.append(f"{slug}: salivary_management_v2311 marker missing")
        combined = " ".join(str(x) for x in ((op.get("setup") or []) + (op.get("postop") or []))).lower()
        for term in required:
            if term not in combined:
                failures.append(f"{slug}: management missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("SALIVARY OR v23.11 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} salivary procedures have reviewed v23.11 management and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
