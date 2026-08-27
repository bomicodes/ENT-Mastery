"""Hard gate for v23.5 oral-composite and conservation-laryngectomy OR management."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_major_onc_v235_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("oral", "composite"),
     ("three dimensions", "mandibular management", "reconstruction", "baseline speech", "tracheostomy"),
     ("airway obstruction", "salivary leak", "fistula", "occlusion", "swallowing safety")),
    (("conservation", "laryngectomy"),
     ("functional laryngeal unit", "cricoarytenoid", "pulmonary reserve", "temporary airway", "decannulation"),
     ("airway edema", "aspiration", "pneumonia", "swallowing rehabilitation", "pharyngeal leak")),
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
        if not op.get("major_oncologic_resection_management_v235"):
            failures.append(f"{slug}: major_oncologic_resection_management_v235 marker missing")
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
        print("MAJOR ONCOLOGIC RESECTION OR v23.5 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} major oncologic-resection modules have reviewed v23.5 planning/rescue and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
