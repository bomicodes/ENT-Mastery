"""Hard gate for v21.2 OR Tomorrow procedure-specific preoperative decision points."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_preop_decision_v212_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("superficial parotid",), ("baseline facial", "deep-lobe/parapharyngeal", "nodal disease")),
    (("total parotid",), ("baseline facial-nerve", "nerve sacrifice/reconstruction", "deep lobe/parapharyngeal")),
    (("submandibular gland",), ("inflammatory/stone disease versus neoplasm", "tongue mobility/sensation", "oncologic neck")),
    (("sialendosc",), ("stone size", "combined approach", "lingual-nerve risk")),
    (("jugular foramen",), ("cn ix-xii", "aspiration status", "vascular imaging")),
    (("translabyrinthine",), ("hearing-sacrificing", "preoperative hearing status", "csf-leak closure")),
    (("retrosigmoid",), ("serviceable hearing", "lower-cranial-nerve status", "hearing-preservation intent")),
    (("middle fossa",), ("hearing-preservation", "geniculate/facial-nerve", "petrous-carotid")),
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

    for title_terms, required in CHECKS:
        slug, op = _find(reg, title_terms)
        label = "/".join(title_terms)
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if not op.get("preop_decision_v212"):
            failures.append(f"{slug}: v21.2 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        for term in required:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("OR PREOP DECISION v21.2 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} procedure-specific preoperative decision modules are live and render")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
