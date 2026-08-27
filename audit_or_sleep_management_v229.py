"""Hard gate for v22.9 sleep-surgery OR Tomorrow planning and postoperative management."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_sleep_mgmt_v229_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("hypoglossal",), ("pap intolerance", "central-versus-obstructive", "drug-induced sleep endoscopy", "baseline tongue mobility"), ("tongue deviation", "pleural injury", "activation", "residual collapse phenotype")),
    (("hyoid", "genioglossus"), ("tongue-base", "mandibular dentition/root", "genial-tubercle", "fixation vector"), ("floor-of-mouth", "hypoglossal injury", "malocclusion", "objective sleep-study")),
]


def _find(reg, terms):
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms) and "reanimation" not in hay:
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
        if not op.get("sleep_management_v229"):
            failures.append(f"{slug}: sleep_management_v229 marker missing")
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
        print("SLEEP SURGERY OR v22.9 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} sleep-surgery procedures have reviewed v22.9 planning/postop management and render successfully")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
