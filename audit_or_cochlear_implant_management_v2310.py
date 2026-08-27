"""Hard gate for v23.10 cochlear-implant OR Tomorrow planning and postoperative rescue."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_ci_v2310_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

REQUIRED_SETUP = (
    "aided performance",
    "speech-recognition",
    "temporal-bone imaging",
    "cochlear patency",
    "vaccination",
    "auditory rehabilitation",
)
REQUIRED_POSTOP = (
    "facial weakness",
    "csf leak",
    "meningitic",
    "device exposure",
    "implant-site infection",
    "device integrity",
)


def _find(reg):
    if "cochlear-implant" in reg:
        return "cochlear-implant", reg["cochlear-implant"]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if "cochlear" in hay and "implant" in hay:
            return slug, op
    return None, None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    slug, op = _find(reg)
    if not op:
        failures.append("cochlear implant: live OR module not found")
    else:
        if not op.get("cochlear_implant_management_v2310"):
            failures.append(f"{slug}: cochlear_implant_management_v2310 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in REQUIRED_SETUP:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in REQUIRED_POSTOP:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
        body = r.get_data(as_text=True).lower()
        if "cochlear" not in body or "implant" not in body:
            failures.append(f"{slug}: rendered page does not identify cochlear implantation")

    if failures:
        print("COCHLEAR IMPLANT OR v23.10 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: cochlear-implant planning/postoperative management is live and renders successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
