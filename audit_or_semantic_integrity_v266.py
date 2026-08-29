"""v26.6 adversarial OR Tomorrow semantic-integrity audit.

Coverage can be structurally complete while still teaching the wrong operation if a
family-level anatomy patch leaks across neighboring procedures. This gate targets the
highest-risk collision pairs and requires procedure-defining anatomy while rejecting
obvious cross-procedure landmarks. It intentionally inspects landmarks rather than
setup prose so legitimate counseling such as "do not import lateral-neck anatomy" does
not create false positives.
"""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_semantic_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

# Each required group is OR-within-group; every group must have at least one match.
CHECKS = {
    "central-neck": {
        "required": [("recurrent laryngeal", "rln"), ("parathyroid",), ("tracheoesophageal", "paratracheal", "pretracheal")],
        "forbidden": ("spinal accessory", "brachial plexus", "thoracic duct"),
    },
    "neck-dissection": {
        "required": [("spinal accessory", "cn xi"), ("carotid",), ("hypoglossal", "cn xii")],
        "forbidden": ("berry ligament", "thyrothymic", "parathyroid adenoma"),
    },
    "parotidectomy": {
        "required": [("facial nerve",), ("tragal", "tympanomastoid"), ("digastric",)],
        "forbidden": ("wharton", "submandibular duct", "genial tubercle"),
    },
    "submandibular-gland": {
        "required": [("lingual nerve",), ("hypoglossal", "cn xii"), ("wharton", "submandibular duct")],
        "forbidden": ("tragal pointer", "tympanomastoid suture", "facial recess"),
    },
    "tonsillectomy": {
        "required": [("capsule", "peritonsillar"), ("constrictor",), ("glossopharyngeal", "cn ix")],
        "forbidden": ("torus tubarius", "eustachian tube orifice", "choana"),
    },
    "adenoidectomy": {
        "required": [("torus", "eustachian"), ("choana", "vomer"), ("velophary", "soft palate")],
        "forbidden": ("tonsillar capsule", "glossopharyngeal nerve", "superior constrictor"),
    },
    "stapedotomy": {
        "required": [("stapes", "footplate"), ("oval window",), ("incus",)],
        # The promontory/round-window niche can be a legitimate inferior orientation
        # reference in stapes surgery; facial-recess/basal-turn anatomy is the true CI leak.
        "forbidden": ("basal turn", "facial recess"),
    },
    "cochlear-implant": {
        "required": [("round window",), ("facial recess",), ("basal turn", "cochlea")],
        "forbidden": ("stapes footplate", "pyramidal eminence", "stapedius tendon"),
    },
    "septoplasty": {
        "required": [("l strut",), ("keystone",), ("quadrangular cartilage",)],
        "forbidden": ("natural maxillary ostium", "uncinate process", "lamina papyracea"),
    },
    "maxillary-antrostomy": {
        "required": [("natural ostium",), ("uncinate",), ("nasolacrimal", "nld")],
        "forbidden": ("l strut", "keystone area", "anterior nasal spine"),
    },
    "total-laryngectomy": {
        "required": [("trache", "stoma"), ("hypopharyn", "pharyngeal"), ("laryng",)],
        "forbidden": ("round window", "facial recess", "tragal pointer"),
    },
    "oral-composite": {
        "required": [("lingual nerve",), ("hypoglossal", "cn xii"), ("lingual artery",)],
        "forbidden": ("oval window", "facial recess", "keystone area"),
    },
}


def _normalize(text):
    return str(text).lower().replace("-", " ").replace("/", " ")


try:
    import runtime_entry as rt

    reg = rt.data.OR_PREP_REGISTRY
    failures = []
    snapshots = {}
    client = rt.app.test_client()

    for slug, spec in CHECKS.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from live OR registry")
            continue
        landmark_items = [str(x) for x in (op.get("landmarks") or [])]
        landmarks = " ".join(_normalize(x) for x in landmark_items)
        start_failure_count = len(failures)
        for group in spec["required"]:
            if not any(_normalize(term) in landmarks for term in group):
                failures.append(f"{slug}: missing defining landmark group {group!r}")
        for term in spec["forbidden"]:
            if _normalize(term) in landmarks:
                failures.append(f"{slug}: cross-procedure landmark contamination {term!r}")
        if len(failures) > start_failure_count:
            snapshots[slug] = landmark_items
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("OR v26.6 SEMANTIC-INTEGRITY FAILURES")
        print("\n".join(failures))
        for slug, items in snapshots.items():
            print(f"LANDMARK_SNAPSHOT {slug}: {items!r}")
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} collision-prone OR modules preserve procedure-defining anatomy without cross-family landmark leakage")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
