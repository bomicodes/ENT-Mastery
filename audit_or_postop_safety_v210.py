"""Hard gate for the v20.10 focused OR Tomorrow postoperative safety layer."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_postop_v210_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

TARGETS = {
    "tracheostomy": {
        "triggers": ("tracheostomy",),
        "exclude": ("laryngectomy", "tracheoesophageal puncture", "tep"),
        "terms": ("fresh surgical tracheostomy", "false passage", "tracheo-innominate fistula"),
    },
    "septoplasty": {
        "triggers": ("septoplasty",),
        "exclude": (),
        "terms": ("septal hematoma", "cartilage necrosis", "saddle-nose"),
    },
    "pharyngoesophageal-myotomy": {
        "triggers": ("zenker", "cricopharyngeal myotomy", "cricopharyngeal-myotomy"),
        "exclude": (),
        "terms": ("perforation", "mediastinal", "crepitus"),
    },
}

try:
    import runtime_entry as rt

    reg = rt.data.OR_PREP_REGISTRY
    failures = []
    matched_slugs = []

    for name, spec in TARGETS.items():
        matches = []
        for slug, op in reg.items():
            label = f"{slug} {op.get('title', '')}".lower()
            if not any(term in label for term in spec["triggers"]):
                continue
            if any(term in label for term in spec["exclude"]):
                continue
            matches.append((slug, op))

        if not matches:
            failures.append(f"{name}: no live OR module matched target")
            continue

        for slug, op in matches:
            matched_slugs.append(slug)
            postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
            if not op.get("postop_safety_v210"):
                failures.append(f"{slug}: v20.10 marker missing")
            for term in spec["terms"]:
                if term not in postop:
                    failures.append(f"{slug}: postop missing {term!r}")

    client = rt.app.test_client()
    for slug in sorted(set(matched_slugs)):
        op = reg[slug]
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
            continue
        text = r.get_data(as_text=True).lower()
        if "immediate post-op priorities" not in text:
            failures.append(f"{slug}: rendered page missing postoperative section")

    if failures:
        print("OR POSTOP SAFETY v20.10 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: v20.10 postoperative safety targets render correctly for {len(set(matched_slugs))} live OR modules")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
