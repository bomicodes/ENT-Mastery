"""Hard gate for v23.12 thyroid OR Tomorrow planning and postoperative rescue."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_thyroid_v2312_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("thyroid", "lobectomy"), ("unilateral extent", "baseline voice", "vocal-fold"), ("postoperative hematoma", "urgent decompression", "dysphonia")),
    (("total", "thyroidectomy"), ("graves", "substernal", "calcium/pth"), ("perioral", "low early pth", "bilateral vocal-fold")),
    (("reop", "thyroid"), ("prior operative", "preoperative vocal-fold mobility", "scar-displaced"), ("reoperative thyroid", "hypocalcemic", "postoperative vocal-fold")),
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

    for terms, setup_required, postop_required in CHECKS:
        slug, op = _find(reg, terms)
        label = "/".join(terms)
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if not op.get("thyroid_management_v2312"):
            failures.append(f"{slug}: thyroid_management_v2312 marker missing")
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
        print("THYROID OR v23.12 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} thyroid procedures have reviewed v23.12 planning/postoperative management and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
