"""v28.0 adversarial production gate for parotid facial-nerve commitment and rescue."""
import os, re, tempfile
fd, db = tempfile.mkstemp(prefix="ent_or_parotid_fn_", suffix=".db"); os.close(fd)
os.environ.pop("DATABASE_URL", None); os.environ["SQLITE_PATH"] = db; os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

def norm(v): return re.sub(r"[^a-z0-9]+", " ", str(v or "").lower()).strip()
def has_groups(text, groups):
    t=norm(text); return all(any(norm(term) in t for term in group) for group in groups)

def resolve(registry, terms):
    for slug, op in (registry or {}).items():
        hay=(str(slug)+" "+str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms):
            return slug, op
    return None, None

try:
    import runtime_entry as rt
    failures=[]
    targets=(("superficial-parotidectomy", ("superficial","parotid")), ("total-parotidectomy", ("total","parotid")))
    for expected, terms in targets:
        slug, op=resolve(rt.data.OR_PREP_REGISTRY, terms)
        label=slug or expected
        if not op:
            failures.append(f"{expected}: no live OR Tomorrow case")
            continue
        combined="\n".join(str(x) for key in ("setup","steps","postop") for x in (op.get(key) or []))
        sources="\n".join(str(x) for x in (op.get("sources") or []))
        if not op.get("parotid_facial_nerve_rescue_v280"): failures.append(f"{label}: v28.0 production marker absent")
        checks=[
            ("preserve versus resect commitment", (("intact preoperative facial function", "baseline movement"),("preserve",),("dissection plane",),("grossly encased", "grossly involved"),("indeterminate",))),
            ("planned reconstruction before sacrifice", (("plan the reconstruction before cutting",),("proximal stump",),("distal targets",),("graft", "nerve transfer"))),
            ("unexpected transection bailout", (("unexpectedly transected",),("stop further traction",),("proximal and distal ends",),("tension free primary neurorrhaphy",),("interposition",))),
            ("functional postop exam", (("forehead",),("eye closure",),("oral competence",))),
            ("ocular rescue", (("incomplete eye closure",),("lubrication",),("moisture", "nighttime closure"),("ophthalmology",))),
        ]
        for check_label, groups in checks:
            if not has_groups(combined, groups): failures.append(f"{label}: missing {check_label}")
        if not has_groups(sources, (("cummings",),("k j lee", "lee's essential"),("pasha",),("asco",),("2026",))): failures.append(f"{label}: source trail incomplete")
        response=rt.app.test_client().get("/case-tomorrow", query_string={"q":op.get("title",slug)}, follow_redirects=True)
        if response.status_code >= 500: failures.append(f"{label}: /case-tomorrow HTTP {response.status_code}")
        rendered=response.get_data(as_text=True)
        if not has_groups(rendered, (("facial nerve",),("dissection plane",),("neurorrhaphy", "interposition"),("eye closure",),("lubrication",))): failures.append(f"{label}: rendered route does not expose v28.0 commitments/rescue")
    if failures:
        print("OR v28.0 PAROTID FACIAL-NERVE FAILURES\n"+"\n".join(failures)); raise SystemExit(1)
    print("PASS: live parotid OR Tomorrow cases protect facial-nerve commitment, transection reconstruction, ocular rescue, provenance, and route coverage")
finally:
    try: os.remove(db)
    except OSError: pass
