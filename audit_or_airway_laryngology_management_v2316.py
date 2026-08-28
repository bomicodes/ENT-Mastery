"""Hard gate for v23.16 airway/laryngology OR Tomorrow management review."""
import os, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_v2316_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

TARGETS = {
    "tracheal-resection": {
        "marker": "tracheal_resection_management_v2316",
        "setup_any": (("tension-free", "release"), ("cricoid",)),
        "postop_any": (("anastom",), ("subcutaneous", "air leak")),
    },
    "airway-dilation": {
        "marker": "airway_dilation_management_v2316",
        "setup_any": (("stenosis",), ("malacia", "inflammation")),
        "postop_any": (("pneumomediastinum", "pneumothorax", "perforation"),),
    },
    "cordotomy": {
        "marker": "cordotomy_management_v2316",
        "setup_any": (("bilateral",), ("cricoarytenoid", "posterior glottic")),
        "postop_any": (("aspiration",),),
    },
    "microflap": {
        "marker": "microflap_management_v2316",
        "setup_any": (("stroboscopy",), ("lamina propria",)),
        "postop_any": (("scar", "stiffness"),),
    },
    "rrp-debridement": {
        "marker": "rrp_management_v2316",
        "setup_any": (("papillomatosis",), ("laser", "fire")),
        "postop_any": (("stenosis", "web"),),
    },
    "laryngeal-fracture": {
        "marker": "laryngeal_fracture_management_v2316",
        "setup_any": (("airway",), ("ct",)),
        "postop_any": (("stenosis",),),
    },
    "transoral-laser-laryngeal-cancer": {
        "marker": "tlm_laryngeal_cancer_management_v2316",
        "setup_any": (("exposure",), ("margin",), ("laser",)),
        "postop_any": (("pathology", "margin"), ("aspiration", "bleeding", "hemorrhage")),
    },
}


def _has_any(text, terms):
    return any(term in text for term in terms)

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    failures = []
    client = rt.app.test_client()

    for slug, spec in TARGETS.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from live OR registry")
            continue
        if not op.get(spec["marker"]):
            failures.append(f"{slug}: missing {spec['marker']}")
        setup = " ".join(str(x).lower() for x in (op.get("setup") or []))
        postop = " ".join(str(x).lower() for x in (op.get("postop") or []))
        for terms in spec["setup_any"]:
            if not _has_any(setup, terms):
                failures.append(f"{slug}: setup missing one of {terms}")
        for terms in spec["postop_any"]:
            if not _has_any(postop, terms):
                failures.append(f"{slug}: postop missing one of {terms}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("OR v23.16 AIRWAY/LARYNGOLOGY FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(TARGETS)} airway/laryngology OR modules carry v23.16 planning/rescue review and render successfully")
finally:
    try: os.remove(db)
    except OSError: pass
