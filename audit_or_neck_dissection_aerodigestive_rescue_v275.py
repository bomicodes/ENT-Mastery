"""v27.5 adversarial production gate for neck-dissection aerodigestive injury rescue."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_neck_aerodigestive_", suffix=".db")
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
        if not op.get("neck_dissection_aerodigestive_rescue_v275"):
            failures.append(f"{slug}: v27.5 production marker absent")
        checks = [
            ("injury recognition/source control", (("pharyngeal", "esophageal"), ("contamination", "source control"), ("extent",), ("debride", "nonviable"))),
            ("selective durable repair", (("tension free",), ("primary repair",), ("vascularized",), ("selectively", "not mandatory"), ("drain",))),
            ("loss-of-plane stop rule", (("stop rule", "stop"), ("blind",), ("improve exposure", "define the defect"), ("diversion", "reconstruction", "drainage"))),
            ("postoperative contamination rescue", (("antimicrobial", "antibiotic"), ("oral intake", "npo"), ("nutrition",), ("deep neck",), ("mediastinal",))),
            ("persistent leak/vessel protection", (("source control",), ("persistent", "uncontained"), ("great vessel", "carotid"), ("viable tissue",), ("sentinel",))),
        ]
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing aerodigestive-rescue concept {label!r}")
        source_groups = (("cummings",), ("k j lee", "lee's essential"), ("pasha",), ("chen s",), ("chirica", "wses"), ("american association for thoracic surgery", "aats"), ("emergency general surgery algorithms",))
        if not has_groups(sources, source_groups):
            failures.append(f"{slug}: textbook/aerodigestive source trail incomplete")
        client = rt.app.test_client()
        response = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if response.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {response.status_code}")
        body = norm(response.get_data(as_text=True))
        route_groups = (("pharyngeal", "esophageal"), ("contamination",), ("tension free",), ("nutrition",), ("mediastinal",), ("sentinel",))
        if not has_groups(body, route_groups):
            failures.append(f"{slug}: rendered OR Tomorrow route does not expose v27.5 aerodigestive rescue")
    if failures:
        print("OR v27.5 NECK-DISSECTION AERODIGESTIVE-RESCUE FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: live neck-dissection OR Tomorrow preserves aerodigestive injury recognition, safe-plane stop rules, source control, durable repair, leak rescue, provenance, and route coverage")
finally:
    try: os.remove(db)
    except OSError: pass
