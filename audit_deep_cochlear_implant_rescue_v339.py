"""v33.9 adversarial production gate for cochlear-implant gusher/misplacement rescue."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_ci_rescue_", suffix=".db"); os.close(fd)
os.environ.pop("DATABASE_URL", None); os.environ["SQLITE_PATH"] = db; os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)


def norm(v): return re.sub(r"[^a-z0-9]+", " ", str(v or "").lower()).strip()
def has_all(text, groups):
    t = norm(text)
    return all(any(norm(term) in t for term in group) for group in groups)

try:
    # Audit the same final production assembly Render imports. Later curriculum
    # layers are chained through runtime_entry_pasha, so inspecting bare
    # runtime_entry can falsely report a missing earlier mutation.
    import runtime_entry_pasha
    data = runtime_entry_pasha.runtime_entry.data
    target = None
    for _domain, modules in (getattr(data, "DEEP_MODULES_V6", {}) or {}).items():
        for module in modules or []:
            if norm(module.get("topic")) == "cochlear implant surgery":
                target = module
                break
        if target: break
    failures = []
    if not target:
        failures.append("live Cochlear Implant Surgery module missing")
    else:
        combined = "\n".join(str(target.get(k) or "") for k in ("recognize","localize","workup","manage","operate","teach"))
        sources = "\n".join(str(x) for x in (target.get("source_basis") or []))
        if not target.get("cochlear_implant_rescue_v339"):
            failures.append("v33.9 production marker absent")
        checks = [
            ("malformed-cochlea commitment", (("ip iii","ip 3"),("gusher",),("sealing material", "seal around the electrode"))),
            ("gusher bailout", (("do not enlarge",),("suction",),("persistent high flow",),("bailout", "stop"))),
            ("electrode-position stop rule", (("unexpected insertion resistance",),("pause", "stop"),("reconfirm the round window",),("position verification",))),
            ("IAC misplacement response", (("iac", "internal auditory canal"),("misplacement",),("stop further insertion",),("reposition", "revision"))),
            ("postop leak/performance rescue", (("clear otorrhea", "clear rhinorrhea"),("meningitic",),("poor early performance",),("facial stimulation",),("malposition",))),
        ]
        for label, groups in checks:
            if not has_all(combined, groups): failures.append("missing " + label)
        if not has_all(sources, (("k j lee", "lee's essential"),("pasha",),("johnson",),("2024",),("ip iii", "incomplete partition type iii"))):
            failures.append("source trail incomplete")
    if failures:
        print("CI v33.9 RESCUE FAILURES\n" + "\n".join(failures)); raise SystemExit(1)
    print("PASS: final Render assembly Cochlear Implant Surgery card protects malformed-cochlea gusher bailout, electrode stop/verify, misplacement rescue, postoperative recognition, and provenance")
finally:
    try: os.remove(db)
    except OSError: pass
