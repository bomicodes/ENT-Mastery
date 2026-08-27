"""Hard gate for v23.6 skull-base OR Tomorrow planning/postoperative rescue."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_skull_base_v236_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("jugular", "foramen"), ("cn ix-xii", "aspiration", "vascular-control"), ("csf leak", "intracranial", "lower-cranial-nerve")),
    (("translabyrinthine",), ("hearing-sacrificing", "facial", "csf-leak closure"), ("pseudomeningocele", "meningitic", "neurologic")),
    (("retrosigmoid",), ("hearing preservation", "brainstem", "lower-cranial-nerve"), ("hydrocephalus", "pseudomeningocele", "aspiration")),
    (("middle", "fossa"), ("hearing-preservation", "temporal-lobe", "cochlear monitoring"), ("seizure", "csf leak", "intracranial")),
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
        if not op.get("skull_base_management_v236"):
            failures.append(f"{slug}: skull_base_management_v236 marker missing")
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
        print("SKULL BASE OR v23.6 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} skull-base procedures have reviewed v23.6 management and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
