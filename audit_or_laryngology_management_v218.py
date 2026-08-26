"""Hard gate for v21.8 laryngology/swallowing OR Tomorrow management."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_laryngology_v218_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("medialization", "thyroplasty"),
     ("glottic-gap pattern", "posterior gap", "vertical height mismatch", "arytenoid adduction", "airway reserve"),
     ("new stridor", "expanding neck swelling", "implant extrusion/migration", "persistent posterior insufficiency")),
    (("injection", "laryngoplast"),
     ("recovery potential", "temporary/shorter-duration", "aspiration/cough", "office/awake", "early temporary augmentation"),
     ("dyspnea", "stridor", "urgent airway/laryngoscopic assessment", "aspiration")),
    (("zenker",),
     ("barium esophagram", "aspiration/pneumonia", "rigid endoscopic", "flexible endoscopic", "open treatment", "limited neck extension"),
     ("cervical crepitus", "perforation", "mediastinal", "diet advancement", "recurrent dysphagia")),
    (("cricopharyngeal", "myotomy"),
     ("upper-esophageal-sphincter dysfunction", "modified barium swallow/fees", "generalized pharyngeal weakness", "distal esophageal pathology", "baseline vocal-fold function"),
     ("occult mucosal perforation/leak", "new dysphonia", "recurrent-laryngeal-nerve dysfunction", "diet advancement")),
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
        if not op.get("laryngology_management_v218"):
            failures.append(f"{slug}: v21.8 laryngology-management marker missing")
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
        print("OR LARYNGOLOGY MANAGEMENT v21.8 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} laryngology/swallowing OR modules have procedure-specific planning/postoperative priorities and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
