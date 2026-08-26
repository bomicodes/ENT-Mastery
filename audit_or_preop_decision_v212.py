"""Hard gate for v21.2-v21.3 OR Tomorrow procedure-specific preoperative decisions."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_preop_decision_v213_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("superficial parotid",), ("baseline facial", "deep-lobe/parapharyngeal", "nodal disease"), "preop_decision_v212"),
    (("total parotid",), ("baseline facial-nerve", "nerve sacrifice/reconstruction", "deep lobe/parapharyngeal"), "preop_decision_v212"),
    (("submandibular gland",), ("inflammatory/stone disease versus neoplasm", "tongue mobility/sensation", "oncologic neck"), "preop_decision_v212"),
    (("sialendosc",), ("stone size", "combined approach", "lingual-nerve risk"), "preop_decision_v212"),
    (("jugular foramen",), ("cn ix-xii", "aspiration status", "vascular imaging"), "preop_decision_v212"),
    (("translabyrinthine",), ("hearing-sacrificing", "preoperative hearing status", "csf-leak closure"), "preop_decision_v212"),
    (("retrosigmoid",), ("serviceable hearing", "lower-cranial-nerve status", "hearing-preservation intent"), "preop_decision_v212"),
    (("middle fossa",), ("hearing-preservation", "geniculate/facial-nerve", "petrous-carotid"), "preop_decision_v212"),
    (("conservation", "laryng"), ("cricoarytenoid unit", "pulmonary reserve", "swallowing/aspiration", "appropriate margins"), "preop_decision_v213"),
    (("transoral", "laser", "laryngeal"), ("completely exposed transorally", "anterior-commissure", "unsafe deep/cartilage margins"), "preop_decision_v213"),
    (("supraglottoplasty",), ("feeding/aspiration history", "synchronous lesions", "postoperative level of care"), "preop_decision_v213"),
    (("laryngotracheal", "cleft"), ("cleft type/length", "aspiration physiology", "open-versus-endoscopic"), "preop_decision_v213"),
    (("direct laryngoscopy", "bronch"), ("spontaneous versus controlled ventilation", "rescue strategy", "critical stenosis"), "preop_decision_v213"),
    (("tracheal", "resection"), ("tension-free resection", "innominate", "release maneuvers", "backup airway"), "preop_decision_v213"),
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
    failures = []
    client = rt.app.test_client()

    for title_terms, required, marker in CHECKS:
        slug, op = _find(reg, title_terms)
        label = "/".join(title_terms)
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if not op.get(marker):
            failures.append(f"{slug}: {marker} missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        for term in required:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("OR PREOP DECISION v21.2-v21.3 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} procedure-specific preoperative decision modules are live and render")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
