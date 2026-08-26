"""Hard gate for v22.0-v22.1 pediatric-airway OR Tomorrow management/anatomy."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_peds_airway_v220_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

MANAGEMENT_CHECKS = [
    (("supraglottoplasty",), ("postoperative disposition", "severe osa", "aspiration/feeding"), ("progressive obstruction", "desaturation", "feeding safety")),
    (("laryngotracheal reconstruction",), ("single-stage versus double-stage", "ett or stent", "rescue plan"), ("tube/stent displacement", "blind tube manipulation", "direct visualization")),
    (("laryngotracheal", "cleft"), ("postoperative airway and feeding plan", "enteral access", "swallow/endoscopic reassessment"), ("aerodigestive leak", "feeding intolerance", "swallow assessment")),
]

LANDMARK_CHECKS = [
    (("supraglottoplasty",), ("aryepiglottic", "cuneiform/corniculate", "true vocal folds", "cricoarytenoid"), ("tracheostomy tract", "carina")),
    (("laryngotracheal reconstruction",), ("posterior cricoid plate", "recurrent laryngeal", "esophageal mucosa", "graft beds"), ("carina", "eustachian")),
    (("laryngotracheal", "cleft"), ("interarytenoid", "posterior cricoid", "anterior esophageal wall", "recurrent laryngeal"), ("carina", "eustachian")),
    (("direct laryngoscopy", "bronch"), ("true vocal folds", "subglottis", "cricoid", "carina", "mainstem"), ("thyrothymic", "wharton")),
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

    for terms, setup_required, postop_required in MANAGEMENT_CHECKS:
        slug, op = _find(reg, terms)
        label = "/".join(terms)
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if not op.get("pediatric_airway_management_v220"):
            failures.append(f"{slug}: pediatric_airway_management_v220 marker missing")
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

    for terms, required, forbidden in LANDMARK_CHECKS:
        slug, op = _find(reg, terms)
        label = "/".join(terms)
        if not op:
            failures.append(f"{label}: live landmark module not found")
            continue
        if op.get("landmarks_v221") != "procedure-specific":
            failures.append(f"{slug}: landmarks_v221 procedure-specific marker missing")
        landmarks = " ".join(str(x) for x in (op.get("landmarks") or [])).lower()
        for term in required:
            if term not in landmarks:
                failures.append(f"{slug}: landmarks missing {term!r}")
        for term in forbidden:
            if term in landmarks:
                failures.append(f"{slug}: landmarks retain irrelevant family anatomy {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: landmark /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("PEDIATRIC AIRWAY OR v22.0-v22.1 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(MANAGEMENT_CHECKS)} pediatric-airway management modules and {len(LANDMARK_CHECKS)} anatomy modules are live")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
