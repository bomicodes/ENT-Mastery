"""Hard gate for v20.3-v21.1 OR Tomorrow physiology and safety content."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_preop_v211_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

SETUP_REQUIRED = {
    "thyroid-lobectomy": ("thyroid functional status", "tsh", "free t4"),
    "total-thyroidectomy": ("thyroid functional status", "tsh", "free t4"),
    "reop-thyroid": ("thyroid functional status", "tsh", "free t4"),
    "parathyroidectomy": ("renal function", "vitamin d", "hungry-bone", ">50% fall", "20 minutes", "multigland"),
    "four-gland": ("renal function", "vitamin d", "hungry-bone", ">50% fall", "20 minutes", "renal disease alone"),
    "reop-parathyroid": ("renal function", "vitamin d", "biochemical", ">50% decline", "delayed sampling", "multigland"),
    "tonsillectomy": ("osa severity", "obesity", "postoperative disposition"),
    "tonsillectomy-adenoidectomy": ("osa severity", "obesity", "postoperative disposition"),
    "hypoglossal-stimulator": ("central-versus-obstructive", "pap intolerance", "dise"),
    "free-flap-basics": ("weight loss", "anemia", "cardiopulmonary", "donor-site perfusion"),
    "oral-composite": ("nutritional", "anemia", "aspiration risk"),
    "total-laryngectomy": ("nutritional", "anemia", "cardiopulmonary"),
    "cochlear-implant": ("audiology", "imaging", "pneumococcal"),
    "tracheal-resection": ("pulmonary reserve", "active respiratory infection", "anastomotic healing"),
    "peds-ltr": ("pulmonary status", "aspiration/swallow", "reflux control"),
}

POSTOP_REQUIRED = {
    "tracheal-resection": ("neck-flexion", "subcutaneous emphysema", "anastomotic failure"),
    "peds-ltr": ("tube/stent", "extubation timing", "urgent endoscopy"),
    "total-laryngectomy": ("permanent neck breather", "tracheal stoma", "oral or nasal intubation cannot ventilate"),
    "neck-dissection": ("chyle leak", "left", "cn xi"),
    "free-flap-basics": ("doppler", "venous congestion", "operative exploration"),
    "cochlear-implant": ("facial-nerve", "vertigo", "meningitic"),
    "tonsillectomy": ("post-tonsillectomy hemorrhage", "hematemesis", "urgent ent"),
    "tonsillectomy-adenoidectomy": ("post-tonsillectomy/adenoid hemorrhage", "hematemesis", "urgent ent"),
    "button-battery": ("sentinel bleeding", "tracheoesophageal fistula", "aorto-esophageal fistula"),
    "esophageal-fb": ("chest pain", "crepitus", "esophageal perforation"),
    "pharyngocutaneous-fistula": ("sentinel hemorrhage", "carotid-blowout", "blind bedside probing"),
    "translabyrinthine-skull-base": ("pseudomeningocele", "meningitic", "csf leak"),
    "retrosigmoid-skull-base": ("declining mental status", "aspiration", "pseudomeningocele"),
    "middle-fossa-skull-base": ("seizure", "focal neurologic deficit", "csf-like"),
}

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    failures = []

    for slug, terms in SETUP_REQUIRED.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from OR registry")
            continue
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        for term in terms:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")

    for slug, terms in POSTOP_REQUIRED.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from OR registry")
            continue
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        for term in terms:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")

    client = rt.app.test_client()
    for slug in sorted(set(SETUP_REQUIRED) | set(POSTOP_REQUIRED)):
        op = reg.get(slug)
        if not op:
            continue
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: rendered /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("OR PHYSIOLOGY/SAFETY v21.1 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(
        f"PASS: {len(SETUP_REQUIRED)} modules contain targeted preop physiology and "
        f"{len(POSTOP_REQUIRED)} contain procedure-specific postoperative safety priorities"
    )
finally:
    try:
        os.remove(db)
    except OSError:
        pass
