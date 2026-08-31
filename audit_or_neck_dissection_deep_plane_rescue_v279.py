"""v27.9 adversarial production gate for neck-dissection deep-plane nerve rescue."""
import os, re, tempfile
fd, db = tempfile.mkstemp(prefix="ent_or_neck_deep_plane_", suffix=".db"); os.close(fd)
os.environ.pop("DATABASE_URL", None); os.environ["SQLITE_PATH"] = db; os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

def norm(v): return re.sub(r"[^a-z0-9]+", " ", str(v or "").lower()).strip()
def has_groups(text, groups):
    t=norm(text); return all(any(norm(term) in t for term in group) for group in groups)
def resolve(reg):
    if "neck-dissection" in reg: return "neck-dissection", reg["neck-dissection"]
    for slug, op in reg.items():
        if "neck dissection" in norm(str(slug)+" "+str((op or {}).get("title",""))) and "complication" not in norm(str(slug)):
            return slug, op
    return None, None
try:
    import runtime_entry as rt
    slug, op = resolve(rt.data.OR_PREP_REGISTRY); failures=[]
    if not op: failures.append("neck-dissection: no live OR Tomorrow case resolved")
    else:
        combined="\n".join(str(x) for key in ("setup","steps","postop") for x in (op.get(key) or [])); sources="\n".join(str(x) for x in (op.get("sources") or []))
        if not op.get("neck_dissection_deep_plane_rescue_v279"): failures.append(f"{slug}: v27.9 production marker absent")
        checks=[
            ("posterior safety boundary", (("prevertebral fascia",),("posterior safety boundary",),("brachial plexus",),("scalene",))),
            ("sympathetic protection", (("sympathetic",),("retropharyngeal",),("widen exposure",),("monopolar",))),
            ("plexus bailout", (("brachial plexus",),("stop further traction",),("define the injury",),("peripheral nerve",))),
            ("Horner recognition", (("ptosis",),("miosis",),("horner",),("hematoma","neuropraxia"))),
            ("plexopathy differentiation", (("arm pain", "arm"),("weakness",),("cn xi", "trapezius"),("radiculopathy",),("electrodiagnostic",))),
        ]
        for label, groups in checks:
            if not has_groups(combined, groups): failures.append(f"{slug}: missing deep-plane concept {label!r}")
        if not has_groups(sources, (("cummings",),("k j lee","lee's essential"),("pasha",),("horner",),("brachial plexus",))): failures.append(f"{slug}: deep-plane source trail incomplete")
        response=rt.app.test_client().get("/case-tomorrow", query_string={"q":op.get("title",slug)}, follow_redirects=True)
        if response.status_code >= 500: failures.append(f"{slug}: /case-tomorrow HTTP {response.status_code}")
        if not has_groups(response.get_data(as_text=True), (("prevertebral fascia",),("sympathetic",),("brachial plexus",),("horner",))): failures.append(f"{slug}: rendered route does not expose v27.9 rescue")
    if failures:
        print("OR v27.9 DEEP-PLANE FAILURES\n"+"\n".join(failures)); raise SystemExit(1)
    print("PASS: live neck-dissection OR Tomorrow protects deep-plane sympathetic/brachial-plexus anatomy, rescue, provenance, and route coverage")
finally:
    try: os.remove(db)
    except OSError: pass
