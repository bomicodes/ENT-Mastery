"""v26.8 OR Tomorrow danger-zone and rescue audit.

Checks high-consequence modules for actionable rescue logic rather than complication
recognition alone. Requirements are deliberately conservative and accept clinically
equivalent phrasing. Failures print the live setup/steps/postop snapshot for review.
"""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_rescue_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

# target = (preferred slug, title/slug aliases, checks). Every group in a check must
# be represented somewhere in setup + steps + postop. The specificity checks below
# intentionally distinguish recognition-only warnings from an executable rescue plan.
CHECKS = [
    ("total-thyroidectomy", ("total thyroidectomy",), [
        ("nerve-loss commitment rescue", (("loss of signal", "unexplained loss", "nerve signal"), ("staged", "opposite side", "contralateral"))),
    ]),
    ("parathyroidectomy", ("parathyroidectomy", "focused parathyroid"), [
        ("failed ioPTH rescue", (("pth",), ("fails to fall", "inadequate", "failed", "multigland"), ("reassess", "localization", "exploration", "ectopic"))),
    ]),
    ("tracheal-resection", ("tracheal resection", "cricotracheal resection"), [
        ("anastomosis protection", (("anastom",), ("flex", "anti extension", "neck"))),
        ("dehiscence airway rescue", (("dehisc", "disruption"), ("bronchoscop", "direct visualization"), ("distal", "beyond the anastomosis"), ("avoid repeated blind", "avoid blind", "traumatic instrumentation"))),
    ]),
    ("free-flap-takeback", ("free flap takeback", "flap takeback"), [
        ("mechanical rescue first", (("kink", "twist", "compression", "hematoma"), ("release", "correct", "reopen"))),
        ("thrombosis revision", (("thromb",), ("revise", "take down", "thrombectomy"))),
    ]),
    ("endoscopic-sinus-surgery", ("endoscopic sinus surgery", "fess"), [
        ("orbit danger recognition", (("orbit", "lamina"),)),
        ("skull-base danger recognition", (("skull base", "csf", "dura"),)),
        ("vision-threatening orbital rescue", (("visual decline", "visual loss", "vision is threatened"), ("compartment syndrome", "tense orbit"), ("canthotomy", "cantholysis", "orbital decompression"), ("rather than waiting", "without delaying", "must not substitute"))),
    ]),
    ("csf-nasoseptal", ("csf leak", "nasoseptal flap", "skull base repair"), [
        ("flow-based reconstruction decision", (("low flow", "high flow", "flow character"), ("multilayer",), ("vascularized", "pedicled flap", "nasoseptal flap"))),
        ("selective lumbar-drain logic", (("lumbar drain",), ("selective", "not automatic", "not routinely"), ("sound closure", "mechanically sound", "substitute"))),
        ("major-vessel bailout", (("arterial", "carotid", "major vessel"), ("vascular", "vascular injury"), ("blind",), ("cautery", "instrumentation"))),
    ]),
    ("tors", ("transoral robotic", "tors"), [
        ("hemorrhage rescue awareness", (("bleed", "hemorrhage", "hemostasis"), ("vessel", "airway", "control"))),
        ("catastrophic hemorrhage choreography", (("anesthesia", "airway"), ("operative", "re-exploration", "or"), ("suction", "pressure", "packing"), ("blind", "clamping"))),
    ]),
    ("tracheostomy", ("tracheostomy",), [
        ("fresh tract false-passage rescue", (("fresh", "immature"), ("false passage",), ("upper airway", "oral endotracheal", "bag-mask"), ("blind", "force"))),
        ("laryngectomy distinction", (("laryngectomy",), ("stoma",), ("mouth", "nose"))),
    ]),
    ("stapedotomy", ("stapedotomy", "stapedectomy"), [
        ("inner-ear rescue escalation", (("vertigo",), ("hearing", "sensorineural"), ("urgent", "reassess", "evaluation"))),
    ]),
    ("cholesteatoma", ("cholesteatoma", "mastoidectomy"), [
        ("major otologic complication escalation", (("facial", "vertigo", "csf", "sensorineural"), ("urgent", "reassess", "evaluation"))),
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
    failures=[]; snapshots={}
    for preferred, aliases, checks in CHECKS:
        slug, op = resolve(reg, preferred, aliases)
        if not op:
            failures.append(f"{preferred}: no live OR case resolved from aliases {aliases!r}")
            continue
        sections = []
        for key in ("setup", "steps", "postop"):
            sections.extend(str(x) for x in (op.get(key) or []))
        combined = "\n".join(sections)
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing actionable rescue concept {label!r}")
                snapshots[slug] = {k:list(op.get(k) or []) for k in ("setup","steps","postop")}
        r = client.get("/case-tomorrow", query_string={"q":op.get("title",slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    if failures:
        print("OR v26.8 RESCUE FAILURES")
        print("\n".join(failures))
        for slug,snap in snapshots.items():
            print(f"RESCUE_SNAPSHOT {slug}: {snap!r}")
        raise SystemExit(1)
    print(f"PASS: {len(CHECKS)} high-consequence OR modules preserve actionable danger-zone/rescue logic")
finally:
    try: os.remove(db)
    except OSError: pass
