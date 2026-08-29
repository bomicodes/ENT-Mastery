"""v26.7 adversarial OR Tomorrow operative-choreography audit.

Checks high-consequence operations for clinically meaningful ordering, points of no
return, and rescue-aware end states. Each checkpoint is an AND of semantic groups;
terms within a group are acceptable alternatives. Failures print the live sequence.
"""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_choreo_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = {
    "total-thyroidectomy": [
        ("superior-pole control", (("superior pole", "superior thyroid"),)),
        ("RLN identification", (("recurrent laryngeal", "rln"),)),
        ("Berry release", (("berry",),)),
        ("contralateral commitment check", (("opposite side", "contralateral", "staged completion", "loss of signal"),)),
        ("final hemostasis", (("hemostasis", "valsalva"),)),
    ],
    "parathyroidectomy": [
        ("nerve-safe localization", (("recurrent", "rln", "nerve-safe"),)),
        ("gland dissection", (("gland", "parathyroid"),)),
        ("pedicle/excision", (("pedicle", "remove", "excision"),)),
        ("ioPTH assessment", (("pth",),)),
        ("failed-drop reassessment", (("fails to fall", "inadequate", "multigland", "broader exploration"),)),
    ],
    "tracheal-resection": [
        ("mobilization/tension strategy", (("mobil", "release maneuver"), ("tension", "low tension"))),
        ("resect diseased segment", (("resect",), ("diseased", "stenotic"))),
        ("posterior-before-anterior anastomosis", (("posterior",), ("anterior",), ("first", "then"), ("suture", "anastom"))),
        ("leak check", (("saline", "positive pressure", "leak"),)),
        ("neck-position protection", (("flex", "guardian", "chin", "neck position", "anti extension"),)),
    ],
    "free-flap-takeback": [
        ("prompt exposure", (("prompt", "time critical", "reopen", "expose the pedicle"),)),
        ("release mechanical causes", (("hematoma", "kink", "twist", "compression"),)),
        ("localize arterial/venous failure", (("arterial",), ("venous",))),
        ("revise thrombosed anastomosis", (("thromb", "take down", "revise"), ("anastom", "vessel"))),
        ("confirm sustained reperfusion", (("reperf", "sustained", "confirm"),)),
    ],
    "endoscopic-sinus-surgery": [
        ("orient before dissection", (("middle turbinate", "uncinate", "orientation", "landmark"),)),
        ("open drainage pathway", (("uncinate", "maxillary", "ethmoid"),)),
        ("posterior/superior progression", (("basal lamella", "posterior ethmoid", "skull base"),)),
        ("danger-boundary control", (("lamina", "orbit", "skull base"),)),
        ("final hemostasis/patency", (("hemostasis", "patent", "patency"),)),
    ],
    "tors": [
        ("exposure/localization", (("exposure", "mouth gag", "robot", "tumor"),)),
        ("define margins", (("margin",),)),
        ("controlled deep dissection", (("constrictor", "deep", "lingual", "carotid", "pharyngeal"),)),
        ("specimen/margin assessment", (("specimen",), ("margin", "frozen"))),
        ("hemostasis before exit", (("hemostasis", "bleeding", "vessel"),)),
    ],
    "laryngotracheal-cleft-repair": [
        ("define full cleft", (("cleft",), ("extent", "entire posterior"))),
        ("separate tissue planes", (("separate",), ("esophageal",), ("laryngotracheal",))),
        ("esophageal closure", (("esophageal layer",),)),
        ("airway closure", (("laryngotracheal", "airway surface"),)),
        ("inspect airway before exit", (("inspect",), ("airway", "lumen"))),
    ],
    "free-flap-basics": [
        ("prepare recipient bed", (("recipient",), ("vessel",))),
        ("pedicle division after readiness", (("divide",), ("recipient bed", "recipient", "ready"))),
        ("microvascular anastomosis", (("anastom",),)),
        ("reperfusion assessment", (("release clamps", "inflow", "outflow", "doppler"),)),
        ("inset protects pedicle", (("inset",), ("pedicle",), ("compression", "kink", "twist"))),
    ],
}


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def checkpoint_match(step, groups):
    txt = norm(step)
    return all(any(norm(term) in txt for term in group) for group in groups)


def find_after(steps, groups, start):
    for i in range(start, len(steps)):
        if checkpoint_match(steps[i], groups):
            return i
    return None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures=[]; snapshots={}
    for slug, checkpoints in CHECKS.items():
        op=reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from live OR registry")
            continue
        steps=[str(x) for x in (op.get("steps") or [])]
        cursor=0
        for label, groups in checkpoints:
            idx=find_after(steps, groups, cursor)
            if idx is None:
                failures.append(f"{slug}: missing/out-of-order checkpoint {label!r} after step {cursor}")
                snapshots[slug]=steps
                break
            cursor=idx+1
        r=client.get("/case-tomorrow",query_string={"q":op.get("title",slug)},follow_redirects=True)
        if r.status_code>=500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    if failures:
        print("OR v26.7 CHOREOGRAPHY FAILURES")
        print("\n".join(failures))
        for slug,steps in snapshots.items():
            print(f"STEP_SNAPSHOT {slug}:")
            for i,s in enumerate(steps,1): print(f"  {i}. {s}")
        raise SystemExit(1)
    print(f"PASS: {len(CHECKS)} high-consequence OR modules preserve clinically coherent operative checkpoint ordering")
finally:
    try: os.remove(db)
    except OSError: pass
