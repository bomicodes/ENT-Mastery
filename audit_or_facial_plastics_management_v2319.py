"""Hard gate for v23.19 facial-plastics OR Tomorrow management review."""
import os, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_v2319_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

TARGETS = {
    "bilobed-flap": ("bilobed_flap_management_v2319", ("alar", "pivot"), ("capillary", "trapdoor")),
    "cervicofacial-flap": ("cervicofacial_flap_management_v2319", ("facial-nerve", "lower-eyelid"), ("necrosis", "ectropion")),
    "forehead-flap": ("forehead_flap_management_v2319", ("lining", "supratrochlear"), ("pedicle", "congestion")),
    "melolabial-flap": ("melolabial_flap_management_v2319", ("alar", "support"), ("congestion", "retraction")),
    "otoplasty": ("otoplasty_management_v2319", ("antihelical", "conchal"), ("hematoma", "perichondritis")),
    "septorhino": ("septorhinoplasty_management_v2319", ("valve", "septal"), ("hematoma", "warping")),
    "skin-graft-face": ("facial_skin_graft_management_v2319", ("recipient bed", "full-"), ("hematoma", "contract")),
}

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []
    for slug, (marker, setup_terms, postop_terms) in TARGETS.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from live OR registry")
            continue
        if not op.get(marker): failures.append(f"{slug}: missing {marker}")
        setup = " ".join(str(x).lower() for x in (op.get("setup") or []))
        postop = " ".join(str(x).lower() for x in (op.get("postop") or []))
        for term in setup_terms:
            if term not in setup: failures.append(f"{slug}: setup missing {term!r}")
        for term in postop_terms:
            if term not in postop: failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500: failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    if failures:
        print("OR v23.19 FACIAL PLASTICS FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: {len(TARGETS)} facial-plastics OR modules carry v23.19 planning/rescue review and render successfully")
finally:
    try: os.remove(db)
    except OSError: pass
