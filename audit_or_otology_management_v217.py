"""Hard gate for v21.7 otology OR Tomorrow planning and postoperative management."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_otology_v217_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("staped",),
     ("air-bone gap", "bone-conduction reserve", "contralateral ear", "sensorineural hearing loss/deafness"),
     ("severe or worsening vertigo", "sudden hearing deterioration", "forceful valsalva")),
    (("tympanoplast",),
     ("preoperative audiometry", "middle-ear status", "cholesteatoma", "staged reconstruction"),
     ("protect the graft", "new facial weakness", "sudden hearing decline")),
    (("ossiculoplast",),
     ("stapes superstructure", "partial versus total reconstruction", "staged reconstruction"),
     ("progressive vertigo", "prosthesis-related complication", "displacement")),
    (("cholesteat",),
     ("current audiogram", "facial-nerve function", "labyrinthine fistula", "canal-wall-up", "canal-wall-down", "diffusion-weighted mri"),
     ("new facial weakness", "sudden sensorineural hearing loss", "csf-like drainage", "planned surveillance")),
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
        if not op.get("otology_management_v217"):
            failures.append(f"{slug}: v21.7 otology-management marker missing")
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
        print("OR OTOLOGY MANAGEMENT v21.7 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} otology OR modules have procedure-specific planning/postoperative priorities and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
