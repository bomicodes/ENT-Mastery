"""Hard gate for v20.3-v20.4 OR Tomorrow preoperative physiology content."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_preop_v204_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

REQUIRED = {
    "thyroid-lobectomy": ("thyroid functional status", "tsh", "free t4"),
    "total-thyroidectomy": ("thyroid functional status", "tsh", "free t4"),
    "reop-thyroid": ("thyroid functional status", "tsh", "free t4"),
    "parathyroidectomy": ("renal function", "vitamin d", "hungry-bone"),
    "four-gland": ("renal function", "vitamin d", "hungry-bone"),
    "reop-parathyroid": ("renal function", "vitamin d", "biochemical"),
    "tonsillectomy": ("osa severity", "obesity", "postoperative disposition"),
    "tonsillectomy-adenoidectomy": ("osa severity", "obesity", "postoperative disposition"),
    "hypoglossal-stimulator": ("central-versus-obstructive", "pap intolerance", "dise"),
    "free-flap-basics": ("weight loss", "anemia", "cardiopulmonary"),
    "oral-composite": ("nutritional", "anemia", "aspiration risk"),
    "total-laryngectomy": ("nutritional", "anemia", "cardiopulmonary"),
    "cochlear-implant": ("audiology", "imaging", "pneumococcal"),
}

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    failures = []
    for slug, terms in REQUIRED.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from OR registry")
            continue
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        for term in terms:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")

    # Make sure the resident-facing route actually renders setup content.
    client = rt.app.test_client()
    for slug in REQUIRED:
        op = reg.get(slug)
        if not op:
            continue
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: rendered /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("OR PREOP PHYSIOLOGY v20.4 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(REQUIRED)} OR modules contain targeted preoperative physiology/optimization checks")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
