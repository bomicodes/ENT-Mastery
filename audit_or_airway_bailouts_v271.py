"""v27.1 adversarial gate for shared-airway exposure and ventilation bailouts."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_airway_bailout_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    ("airway-dilation", ("airway dilation",), [
        ("ventilation loss stops dilation", (("oxygenation", "ventilation"), ("stop", "withdraw", "re-establish"), ("blind", "poorly visualized"), ("change", "surgical airway", "open reconstruction"))),
        ("resistance does not justify force", (("will not accept", "cannot be traversed", "dense mature scar"), ("reassess",), ("smaller", "staged", "open reconstruction", "surgical airway"))),
    ]),
    ("microflap", ("microflap",), [
        ("poor exposure changes elective plan", (("adequate view", "exposure"), ("stop", "deferring", "alternate approach"), ("dental", "tongue", "pharyngeal", "laryngeal injury"))),
        ("physiology outranks lesion removal", (("oxygenation", "ventilation", "airway fire"), ("stop", "cease"), ("re-establish", "controlled airway"))),
    ]),
    ("rrp-debridement", ("rrp", "papilloma"), [
        ("staged debulking preserves airway", (("ventilation corridor", "ventilation worsens"), ("staged",), ("oxygenation", "airway control"), ("circumferential", "stenosis", "lost airway"))),
        ("fire-safety loss is a stop point", (("fire",), ("stop", "cease"), ("resume",), ("controlled", "precautions"))),
    ]),
    ("tracheal-resection", ("tracheal resection",), [
        ("cross-field failure pauses resection", (("cross-field", "distal airway"), ("pause", "stop"), ("re-establish", "oxygenation", "ventilation"))),
        ("anastomotic tension changes resection", (("tension",), ("well-perfused", "devascularized"), ("change", "limit resection", "release"), ("anastomosis",))),
    ]),
    ("airway-fb", ("airway foreign body", "foreign body"), [
        ("hypoxemia interrupts extraction", (("oxygenation", "saturation", "ventilation"), ("stop traction", "re-establish ventilation", "restore"), ("direct", "endoscopic control"))),
        ("central obstruction has a controlled rescue", (("trachea", "carina", "central"), ("mainstem", "opposite lung"), ("direct visualization", "direct endoscopic"), ("temporizing", "rescue"))),
        ("upper-airway impaction changes extraction route", (("glottis", "subglottis"), ("do not repeatedly", "repeated traumatic"), ("orientation", "retrieval instrument", "controlled"), ("tracheotomy", "open extraction"))),
        ("fragmentation mandates second look", (("fragment", "friable"), ("reinspect", "second look", "second-look"), ("both main bronchi", "trachea"), ("retained",))),
    ]),
    ("direct-laryngoscopy-bronchoscopy", ("direct laryngoscopy bronchoscopy", "laryngoscopy bronchoscopy"), [
        ("diagnostic exam stops for physiology", (("oxygenation", "ventilation"), ("stop point", "withdraw"), ("re-establish",), ("smaller instrument", "secured airway", "controlled ventilation"))),
        ("stenosis sizing is atraumatic", (("stenosis",), ("do not", "forcing", "force"), ("atraumatic",), ("cannot be crossed", "inability to traverse"))),
    ]),
]

PEDIATRIC_SOURCE_TARGETS = {"airway-fb", "direct-laryngoscopy-bronchoscopy"}
SOURCE_GROUPS = (("cummings",), ("k j lee", "lee's essential"), ("pasha",), ("ers statement", "pediatric airway endoscopy"))


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
    resolved_count = 0
    for preferred, aliases, checks in CHECKS:
        slug, op = resolve(reg, preferred, aliases)
        if not op:
            failures.append(f"{preferred}: no live case resolved")
            continue
        resolved_count += 1
        combined = "\n".join(str(x) for key in ("setup", "steps", "postop") for x in (op.get(key) or []))
        if not op.get("airway_bailouts_v271"):
            failures.append(f"{slug}: v27.1 production marker absent")
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing airway bailout concept {label!r}")
        if preferred in PEDIATRIC_SOURCE_TARGETS:
            source_text = "\n".join(str(x) for x in (op.get("sources") or []))
            if not has_groups(source_text, SOURCE_GROUPS):
                failures.append(f"{slug}: pediatric airway source provenance incomplete")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    if resolved_count != len(CHECKS):
        failures.append(f"resolved {resolved_count}/{len(CHECKS)} live airway-bailout targets")
    if failures:
        print("OR v27.1 AIRWAY BAILOUT FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: {len(CHECKS)} shared-airway modules preserve explicit exposure, ventilation, fire-safety, pediatric extraction, and source-grounded bailout logic")
finally:
    try: os.remove(db)
    except OSError: pass
