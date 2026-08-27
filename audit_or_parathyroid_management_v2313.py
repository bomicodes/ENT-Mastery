"""Hard gate for v23.13 parathyroid OR Tomorrow planning and postoperative rescue."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_parathyroid_v2313_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    {
        "slug": "parathyroidectomy",
        "terms": ("parathyroidectomy",),
        "exclude": ("reop", "reoperative", "four", "bilateral"),
        "setup": ("biochemical diagnosis", "localization", "ioPTH response"),
        "postop": ("hypocalcemia", "hungry-bone", "neck-hematoma", "dysphonia"),
        "renal": (">50%", "renal", "later sample"),
    },
    {
        "slug": "four-gland",
        "terms": ("four", "gland"),
        "exclude": (),
        "setup": ("multigland", "renal hyperparathyroidism", "intraoperative PTH"),
        "postop": ("calcium/PTH", "hungry-bone", "active-vitamin-D", "voice"),
        "renal": (">50%", "renal", "later sample"),
    },
    {
        "slug": "reop-parathyroid",
        "terms": ("reop", "parathyroid"),
        "exclude": (),
        "setup": ("persistent", "recurrent", "vocal-fold mobility", "least-scarred"),
        "postop": ("dysphonia", "stridor", "hypocalcemic", "calcium surveillance"),
        "renal": (">50%", "renal", "delayed sampling"),
    },
]


def _resolve(reg, check):
    if check["slug"] in reg:
        return check["slug"], reg[check["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if not all(term.lower() in hay for term in check["terms"]):
            continue
        if any(term.lower() in hay for term in check.get("exclude", ())):
            continue
        return slug, op
    return None, None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    for check in CHECKS:
        slug, op = _resolve(reg, check)
        label = check["slug"]
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if op.get("parathyroid_management_v2313") is not True:
            failures.append(f"{slug}: parathyroid_management_v2313 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in check["setup"]:
            if term.lower() not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in check["postop"]:
            if term.lower() not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        for term in check["renal"]:
            if term.lower() not in setup:
                failures.append(f"{slug}: renal/ioPTH planning nuance missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("PARATHYROID OR v23.13 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: focused, four-gland, and reoperative parathyroid modules retain renal/ioPTH nuance, v23.13 management, and route integrity")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
