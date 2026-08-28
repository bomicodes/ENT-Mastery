"""v23.15 procedure-specific rhinology OR Tomorrow management review.

Adds end-to-end planning and postoperative rescue to five generic-only high-yield
rhinology procedures identified by the full live OR registry audit. Existing exact
operative sequences and reviewed anatomy remain unchanged.
"""

TARGETS = [
    {
        "slug": "endoscopic-sinus-surgery",
        "title_terms": ("endoscopic", "sinus", "surgery"),
        "setup": [
            "Before endoscopic sinus surgery, correlate symptoms and endoscopy with CT rather than operating on radiographic opacification alone. Review the scan in three planes for skull-base height/asymmetry, Keros/lateral-lamella vulnerability, lamina/orbit, anterior ethmoid artery course, Onodi cells, sphenoid carotid/optic relationships, frontal drainage anatomy and prior surgical distortion; define which sinuses actually require treatment and whether image guidance is indicated.",
            "Optimize reversible inflammatory disease before surgery when feasible and identify factors that alter bleeding, healing or recurrence risk: systemic/local steroid strategy, aspirin/anticoagulants, asthma/AERD, immunodeficiency, diabetes, smoking and prior surgery. The operative plan should preserve mucosa and landmarks while creating durable physiologic drainage rather than simply maximizing cavity size.",
        ],
        "postop": [
            "After FESS, acute visual loss or decline, afferent pupillary defect, severe orbital pain, proptosis, ophthalmoplegia or rapidly increasing orbital swelling is an orbital emergency; assess the eye immediately and activate decompression/ophthalmologic management without delaying vision-saving treatment for routine imaging when compartment syndrome is suspected.",
            "Persistent brisk epistaxis, clear unilateral rhinorrhea, severe headache, meningismus, focal neurologic change or altered mental status should trigger evaluation for vascular or skull-base complication rather than being attributed to expected postoperative congestion. Subsequent saline care, topical therapy and debridement should support mucosal healing while avoiding unnecessary trauma to exposed skull base or orbit.",
        ],
        "marker": "fess_management_v2315",
    },
    {
        "slug": "draf",
        "title_terms": ("frontal", "sinusotomy"),
        "setup": [
            "Before Draf II/III frontal sinusotomy, map the frontal drainage pathway in all planes and identify the agger nasi, frontal cells, frontal beak, intersinus septum, orbit, skull base and anterior ethmoid artery. Define why an extended frontal procedure is required—recalcitrant inflammatory disease, mucocele, tumor access or salvage after prior surgery—and confirm that simpler drainage would be inadequate rather than escalating extent by habit.",
            "Review prior operations, frontal recess scarring, lateral disease reach and expected neo-ostium dimensions, and plan postoperative topical access. In a Draf III, preservation of mucosa where possible and a strategy to limit restenosis are as important as achieving the initial drill-out.",
        ],
        "postop": [
            "After extended frontal sinus surgery, new severe frontal headache, clear rhinorrhea, meningismus, neurologic change, visual symptoms or major epistaxis warrants urgent assessment for skull-base, orbital or vascular complication. Routine crusting does not explain progressive neurologic or ocular findings.",
            "Long-term failure is often restenosis rather than an immediate technical catastrophe. Endoscopic surveillance should assess neo-ostium patency, scar/granulation and recurrent inflammatory disease; persistent narrowing should be addressed with optimized topical therapy and selective debridement before mature cicatricial closure makes revision more difficult.",
        ],
        "marker": "draf_management_v2315",
    },
    {
        "slug": "sphenoidotomy",
        "title_terms": ("sphenoidotomy",),
        "setup": [
            "Before sphenoidotomy, identify the natural ostium and review CT for sphenoid pneumatization, septations that insert on the carotid canal, optic-nerve prominence/dehiscence, Onodi cells and skull-base relationships. Prior surgery or distorted anatomy should lower the threshold for image guidance and for deliberately re-establishing reliable landmarks before enlarging the ostium.",
        ],
        "postop": [
            "After sphenoid surgery, sudden visual change, ophthalmoplegia, severe retro-orbital pain, brisk arterial bleeding, clear rhinorrhea or neurologic deterioration is not routine postoperative discomfort and requires urgent evaluation for optic, carotid, orbital or skull-base injury. Delayed headache with fever/meningismus likewise requires assessment for infectious or CSF complication.",
        ],
        "marker": "sphenoidotomy_management_v2315",
    },
    {
        "slug": "spa-ligation",
        "title_terms": ("sphenopalatine", "artery"),
        "setup": [
            "Before endoscopic sphenopalatine-artery control, stabilize the patient and confirm that persistent posterior epistaxis warrants operative arterial control after appropriate resuscitation and correction of reversible coagulopathy. Review prior nasal surgery and anticipate multiple SPA branches at the sphenopalatine foramen so the goal is complete branch control rather than clipping a single visible vessel and assuming the bleeding source is eliminated.",
        ],
        "postop": [
            "Recurrent brisk bleeding after SPA ligation should trigger reassessment of branch control and alternative sources, including anterior ethmoid or other arterial contributors, rather than repeated blind packing alone. Monitor hemodynamics and hemoglobin according to blood loss; new orbital findings or facial/palatal ischemic symptoms warrant evaluation for non-routine vascular injury.",
        ],
        "marker": "spa_management_v2315",
    },
    {
        "slug": "orbital-abscess",
        "title_terms": ("orbital", "abscess"),
        "setup": [
            "Before endoscopic drainage of a subperiosteal/orbital abscess, document vision, pupils, color vision when feasible, extraocular movements, proptosis, pain and cranial-nerve findings, and review contrast imaging for abscess location/size, sinus source, orbital-apex involvement, intracranial extension and anatomy that determines whether endoscopic, external or combined drainage is most appropriate. Coordinate ophthalmology and broad-spectrum IV antibiotics while recognizing that threatened vision, clinical deterioration or an appropriate drainable collection can require urgent surgery.",
        ],
        "postop": [
            "After orbital abscess drainage, repeat objective visual and motility examinations; worsening acuity, new RAPD, increasing proptosis, ophthalmoplegia, severe pain or declining mental status means treatment failure or progression until proven otherwise and requires immediate reassessment, not delayed routine rounds.",
            "Persistent fever, worsening orbital signs or absent clinical improvement should prompt review for residual/loculated abscess, inadequately treated sinus source, resistant organism, intracranial extension or another diagnosis. Continue antibiotic duration and repeat imaging based on clinical trajectory rather than a fixed postoperative timetable alone.",
        ],
        "marker": "orbital_abscess_management_v2315",
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in target["title_terms"]):
            return slug, op
    return None, None


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_rhinology_management_v2315(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
