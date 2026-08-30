"""Hard gate for v23.12 thyroid OR Tomorrow planning, commitment, and postoperative rescue."""
import os
import re
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_thyroid_v2312_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("thyroid", "lobectomy"), ("unilateral extent", "baseline voice", "vocal-fold"), ("postoperative hematoma", "urgent decompression", "dysphonia")),
    (("total", "thyroidectomy"), ("graves", "substernal", "calcium/pth"), ("perioral", "low early pth", "bilateral vocal-fold")),
    (("reop", "thyroid"), ("prior operative", "preoperative vocal-fold mobility", "scar-displaced"), ("reoperative thyroid", "hypocalcemic", "postoperative vocal-fold")),
]


def _find(reg, terms):
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms):
            return slug, op
    return None, None


def _norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def _has_groups(text, groups):
    t = _norm(text)
    return all(any(_norm(term) in t for term in group) for group in groups)

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []

    for terms, setup_required, postop_required in CHECKS:
        slug, op = _find(reg, terms)
        label = "/".join(terms)
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if not op.get("thyroid_management_v2312"):
            failures.append(f"{slug}: thyroid_management_v2312 marker missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in setup_required:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in postop_required:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    slug, total = _find(reg, ("total", "thyroidectomy"))
    if total:
        setup = "\n".join(str(x) for x in (total.get("setup") or []))
        los_groups = (
            ("loss of signal", "nerve signal"),
            ("false loss", "technical event", "technical"),
            ("vagus", "rln stimulation", "repeat"),
            ("staging", "stage", "deferment", "defer"),
            ("bilateral vocal fold", "bilateral vocal-fold"),
            ("malignancy", "oncologic"),
            ("deliberate", "documented", "reassess"),
        )
        if not _has_groups(setup, los_groups):
            failures.append(f"{slug}: missing true first-side LOS troubleshooting/stage-versus-continue decision")
        invaded_rln_groups = (
            ("adherent", "invades", "invasion"),
            ("preoperative vocal fold", "preoperative vocal-fold", "vocal-fold mobility"),
            ("preserve", "shave", "partial layer", "partial-layer"),
            ("full thickness", "full-thickness", "gross invasion", "destructive"),
            ("en bloc", "resection", "sacrifice"),
            ("reconstruction", "reinnervation", "rehabilitation"),
        )
        if not _has_groups(setup, invaded_rln_groups):
            failures.append(f"{slug}: missing function- and invasion-aware RLN preservation-versus-resection strategy")
        last_nerve_groups = (
            ("preoperative unilateral vocal fold paralysis", "preoperative unilateral vocal-fold paralysis"),
            ("last functioning nerve", "last-functioning-nerve", "last functioning rln"),
            ("bilateral vocal fold paralysis", "bilateral vocal-fold paralysis"),
            ("respiratory distress", "tracheostomy", "airway"),
            ("preservation", "preserve"),
            ("oncologic",),
            ("reinnervation", "reconstruction"),
            ("immediate", "postoperative airway"),
        )
        if not _has_groups(setup, last_nerve_groups):
            failures.append(f"{slug}: missing last-functioning-RLN planning when the opposite cord is already paralyzed")
        parathyroid_groups = (
            ("preserve normal glands in situ", "preserve normal glands"),
            ("native blood supply", "pedicle"),
            ("inadvertently excised", "ischemic", "devascularized"),
            ("selective autotransplantation", "autotransplantation"),
            ("do not sacrifice", "do not routinely autotransplant", "normally perfused"),
            ("rescue", "compromised tissue"),
        )
        if not _has_groups(setup, parathyroid_groups):
            failures.append(f"{slug}: missing in-situ-first/selective parathyroid autotransplant commitment strategy")
        sources = "\n".join(str(x) for x in (total.get("sources") or []))
        source_groups = (
            ("cummings",),
            ("k j lee", "essential otolaryngology"),
            ("pasha", "clinical reference guide"),
            ("2025 american thyroid association", "2025 ata"),
            ("postoperative hypoparathyroidism",),
            ("kasmirski", "does parathyroid autotransplantation prevent"),
            ("jiang", "devascularized glands"),
            ("improving voice outcomes", "aao hnsf"),
            ("international neural monitoring study group", "inmsg"),
            ("invasive thyroid cancer",),
        )
        if not _has_groups(sources, source_groups):
            failures.append(f"{slug}: thyroid commitment source provenance incomplete")

    slug, lob = _find(reg, ("thyroid", "lobectomy"))
    if lob:
        setup = "\n".join(str(x) for x in (lob.get("setup") or []))
        if not _has_groups(setup, (("invading", "invades", "adherent"), ("functioning nerve", "nerve function"), ("shaved", "shave", "partial"), ("en bloc", "resection"), ("reinnervation", "rehabilitation"))):
            failures.append(f"{slug}: lobectomy case missing invasive-RLN commitment logic")
        if not _has_groups(setup, (("opposite vocal fold", "contralateral"), ("last functioning rln", "last functioning nerve"), ("airway", "bilateral paralysis"), ("reinnervation", "reconstruction"), ("immediate abduction", "immediate"))):
            failures.append(f"{slug}: lobectomy case missing opposite-paralysis/last-functioning-RLN strategy")

    slug, reop = _find(reg, ("reop", "thyroid"))
    if reop:
        setup = "\n".join(str(x) for x in (reop.get("setup") or []))
        if not _has_groups(setup, (("already paralyzed", "paralyzed"), ("last functioning rln", "last functioning nerve"), ("blind traction", "energy in scar"), ("oncologic", "recurrent cancer"), ("airway", "bilateral vocal fold paralysis"), ("reinnervation", "reconstruction"))):
            failures.append(f"{slug}: reoperative case missing last-functioning-RLN scar/airway commitment logic")
        sources = "\n".join(str(x) for x in (reop.get("sources") or []))
        if not _has_groups(sources, (("cummings",), ("k j lee", "essential otolaryngology"), ("pasha",), ("2025 american thyroid association",), ("international neural monitoring study group",))):
            failures.append(f"{slug}: reoperative thyroid source provenance incomplete")

    if failures:
        print("THYROID OR v23.12 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} thyroid procedures retain source-grounded LOS, invasive-RLN, last-functioning-RLN, and selective parathyroid-preservation/autotransplant commitment strategy")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
