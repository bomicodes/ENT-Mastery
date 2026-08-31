"""v27.4 adversarial production gate for neck-dissection carotid danger-zone strategy."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_neck_carotid_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def has_groups(text, groups):
    t = norm(text)
    return all(any(norm(term) in t for term in group) for group in groups)


def resolve(reg):
    if "neck-dissection" in reg:
        return "neck-dissection", reg["neck-dissection"]
    for slug, op in reg.items():
        hay = norm(str(slug) + " " + str((op or {}).get("title", "")))
        if "neck dissection" in hay and "complication" not in hay:
            return slug, op
    return None, None


try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    slug, op = resolve(reg)
    failures = []
    if not op:
        failures.append("neck-dissection: no live OR Tomorrow case resolved")
    else:
        combined = "\n".join(str(x) for key in ("setup", "steps", "postop") for x in (op.get(key) or []))
        sources = "\n".join(str(x) for x in (op.get("sources") or []))
        if not op.get("neck_dissection_carotid_danger_v274"):
            failures.append(f"{slug}: v27.4 production marker absent")
        checks = [
            ("pre-incision carotid commitment", (("carotid involvement", "fixation"), ("pre incision", "commitment"), ("vascular", "endovascular"), ("resection", "preservation"))),
            ("loss-of-safe-plane stop rule", (("loss of a safe arterial plane", "safe arterial plane"), ("stop",), ("proximal",), ("distal",), ("blind", "circumferential stripping"))),
            ("injury control choreography", (("carotid is injured", "carotid injury"), ("proximal",), ("distal",), ("resuscitate", "resuscitation"), ("blind deep clamping", "blind clamping"))),
            ("sentinel bleed recognition", (("sentinel",), ("irradiated", "operated"), ("wound breakdown", "fistula", "infection", "exposed carotid"), ("do not dismiss", "warning"))),
            ("major hemorrhage rescue", (("massive",), ("airway",), ("pressure", "packing"), ("endovascular",), ("ligation", "bypass", "repair"), ("stroke", "neurologic"))),
        ]
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing carotid-danger concept {label!r}")
        source_groups = (("cummings",), ("k j lee", "lee's essential"), ("pasha",), ("sun k",), ("pace gm",), ("zhu wy",), ("slijepcevic",))
        if not has_groups(sources, source_groups):
            failures.append(f"{slug}: textbook/carotid-danger source trail incomplete")
        client = rt.app.test_client()
        response = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if response.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {response.status_code}")
        body = norm(response.get_data(as_text=True))
        route_groups = (("carotid",), ("sentinel",), ("endovascular",), ("blind",), ("proximal",), ("distal",))
        if not has_groups(body, route_groups):
            failures.append(f"{slug}: rendered OR Tomorrow route does not expose v27.4 carotid danger rescue")
    if failures:
        print("OR v27.4 NECK-DISSECTION CAROTID-DANGER FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: live neck-dissection OR Tomorrow preserves carotid commitment, safe-plane stop rules, sentinel-bleed rescue, source provenance, and route coverage")
finally:
    try: os.remove(db)
    except OSError: pass
