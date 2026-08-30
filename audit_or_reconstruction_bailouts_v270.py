"""v27.0 adversarial gate for free-flap recipient-vessel and salvage bailouts."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_recon_bailout_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    ("free-flap-basics", ("free flap",), [
        ("hostile recipient changes plan", (("recipient vessel",), ("poor flow", "intimal", "radiation", "fibrotic"), ("kink", "twist", "tension", "compression"), ("alternate", "cross the neck", "better ipsilateral"))),
        ("vein graft is selective", (("vein graft", "interposition"), ("selective", "when", "cannot"), ("alternate recipient", "different reconstructive", "pedicle routing"))),
    ]),
    ("free-flap-takeback", ("free flap takeback", "flap takeback"), [
        ("recurrent thrombosis is cause directed", (("recurrent thrombosis", "thrombosis recurs"), ("kink", "twist", "tension", "compression"), ("healthy", "change recipient"), ("cause", "mechanical"))),
        ("unsalvageable flap changes reconstruction", (("unsalvageable",), ("ischemia",), ("second free flap", "regional", "pedicled"), ("repeated", "serial", "further revision"))),
    ]),
]


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def has_groups(text, groups):
    t = norm(text)
    return all(any(norm(term) in t for term in group) for group in groups)


def resolve(reg, preferred, aliases):
    if preferred in reg:
        return preferred, reg[preferred]
    for slug, op in reg.items():
        hay = norm(str(slug) + " " + str((op or {}).get("title", "")))
        if any(norm(alias) in hay for alias in aliases):
            return slug, op
    return None, None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []
    for preferred, aliases, checks in CHECKS:
        slug, op = resolve(reg, preferred, aliases)
        if not op:
            failures.append(f"{preferred}: no live case resolved")
            continue
        combined = "\n".join(str(x) for key in ("setup", "steps", "postop") for x in (op.get(key) or []))
        if not op.get("reconstruction_bailouts_v270"):
            failures.append(f"{slug}: v27.0 production marker absent")
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing reconstructive bailout concept {label!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    if failures:
        print("OR v27.0 RECONSTRUCTION BAILOUT FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: {len(CHECKS)} free-flap modules preserve recipient-vessel and salvage bailout logic")
finally:
    try: os.remove(db)
    except OSError: pass
