"""v15.9 — Deep Curriculum content audit.

Audits the six-layer curriculum itself (not vignette counts). The goal is to
surface the same kind of issues found manually in SSNHL/cholesteatoma:
missing etiologic/pathogenesis framing, Teach/Boards prompts that ask rather
than teach, thin operative decision logic, missing subtype/variant coverage,
and duplicated text across layers.

Informational only: this prints a review list for human/clinical curation and
always exits 0. It deliberately excludes Otology / Neurotology because v15.8
is already addressing that domain in a dedicated pass.
"""

from difflib import SequenceMatcher
import re
import runtime_entry


data = runtime_entry.data

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")
DOMAINS = [d for d in data.DEEP_MODULES_V6 if d != "Otology / Neurotology"]

# Commands/questions in Teach/Boards are a smell: this layer should contain the
# answer/pearl, not tell the learner what they ought to explain.
TEACH_PROMPT_RE = re.compile(
    r"(?:^|[.;]\s+)(?:explain|discuss|describe|know|be able to|teach|compare|contrast|why|how|what)\b|\?",
    re.I,
)

ETIOLOGY_TERMS = (
    "cause", "etiolog", "pathogenesis", "mechanism", "risk factor", "acquired",
    "congenital", "infect", "inflamm", "autoimmune", "viral", "vascular",
    "trauma", "iatrogen", "genetic", "idiopathic", "exposure",
)
DECISION_TERMS = (
    "indication", "contraindication", "choose", "versus", "vs", "when", "if ",
    "reserve", "select", "stage", "extent", "approach", "threshold", "failure",
    "recurrent", "salvage", "observation", "surveillance",
)

# High-yield topic families where the six-layer module should carry specific
# resident-level discriminators. Matching is intentionally broad and the audit
# only reports missing themes; it does not mutate content.
EXPECTATIONS = {
    "Rhinology / Allergy / Skull Base": [
        (("chronic rhinosinusitis", "crs"), {
            "phenotype/endotype": ("polyp", "eosinoph", "type 2", "asthma", "aerd"),
            "medical-to-surgical threshold": ("maximal", "medical", "endoscopic sinus", "ess", "surgery"),
            "biologic selection": ("biologic", "dupil", "omaliz", "mepol"),
        }),
        (("epistaxis",), {
            "arterial localization": ("sphenopalatine", "anterior ethmoid", "posterior", "internal maxillary"),
            "escalation options": ("cauter", "packing", "ligation", "embol"),
        }),
        (("csf", "cerebrospinal"), {
            "confirmation": ("beta-2", "beta 2", "transferrin"),
            "localization/repair": ("ct", "mri", "intrathecal", "endoscopic", "repair"),
            "spontaneous leak/IIH": ("intracranial pressure", "iih", "obesity"),
        }),
        (("invasive fungal",), {
            "host/risk": ("neutrop", "diabet", "immun"),
            "serial debridement": ("repeat", "serial", "debrid"),
            "orbital/cranial extension": ("orbit", "cranial", "cavernous"),
        }),
    ],
    "Head & Neck Oncology": [
        (("orophary", "hpv"), {
            "HPV-specific staging": ("p16", "hpv", "8th", "stage"),
            "treatment selection": ("radiation", "chemoradi", "surgery", "transoral"),
        }),
        (("unknown primary",), {
            "workup sequence": ("pet", "tonsil", "base of tongue", "p16", "ebv"),
            "neck management": ("neck dissection", "radiation", "mucosal"),
        }),
        (("laryngeal", "glottic", "supraglottic"), {
            "subsite lymphatics": ("lymph", "nodal", "level"),
            "organ preservation/salvage": ("preservation", "chemoradi", "salvage", "laryngectomy"),
        }),
        (("neck dissection",), {
            "levels/anatomic risk": ("level", "spinal accessory", "xi", "jugular", "carotid"),
            "selective vs comprehensive": ("selective", "modified radical", "radical"),
        }),
    ],
    "Thyroid / Parathyroid / Salivary": [
        (("thyroid nodule",), {
            "risk stratification": ("tirads", "ultrasound", "bethesda"),
            "molecular testing": ("molecular", "indeterminate", "bethesda iii", "bethesda iv"),
        }),
        (("differentiated thyroid", "papillary", "follicular"), {
            "extent of surgery": ("lobectomy", "total thyroid", "completion"),
            "nodal strategy": ("central", "lateral", "neck dissection"),
            "RAI/surveillance": ("radioactive iodine", "rai", "thyroglobulin", "surveillance"),
        }),
        (("medullary",), {
            "MEN2/RET": ("ret", "men2", "pheochrom"),
            "calcitonin/CEA": ("calcitonin", "cea"),
        }),
        (("hyperparathy", "parathyroid"), {
            "localization is not diagnosis": ("localization", "ultrasound", "sestamibi", "4d"),
            "operative strategy": ("focused", "bilateral", "exploration", "intraoperative pth", "iopth"),
        }),
        (("salivary", "parotid"), {
            "facial nerve implication": ("facial nerve", "nerve sacrifice", "reanimation"),
            "neck/adjuvant decisions": ("neck dissection", "radiation", "adjuvant"),
        }),
    ],
    "Pediatric Otolaryngology": [
        (("tonsil", "osa"), {
            "severity/risk stratification": ("ahi", "severe", "age", "obesity", "down syndrome"),
            "intracapsular vs total": ("intracapsular", "extracapsular", "total tonsil"),
            "postop disposition": ("admit", "observe", "overnight", "monitor"),
        }),
        (("airway foreign body", "foreign body"), {
            "rigid bronchoscopy": ("rigid", "bronchoscopy"),
            "airway/anesthesia plan": ("ventilat", "spontaneous", "airway"),
        }),
        (("laryngomalacia",), {
            "severity spectrum": ("feeding", "failure to thrive", "cyan", "apnea"),
            "supraglottoplasty indication": ("supraglottoplasty", "severe"),
        }),
        (("subglottic stenosis",), {
            "grade/measurement": ("cotton", "myer", "grade", "sizing"),
            "endoscopic vs open": ("endoscopic", "ltr", "ctr", "resection", "reconstruction"),
        }),
    ],
    "Laryngology / Voice / Swallowing": [
        (("unilateral vocal", "vocal fold paralysis", "paresis"), {
            "etiologic workup": ("vagus", "recurrent", "ct", "skull base", "mediast"),
            "temporary vs permanent rehabilitation": ("injection", "thyroplasty", "reinnervation"),
        }),
        (("bilateral vocal",), {
            "airway-first logic": ("airway", "stridor", "trache"),
            "motion restoration vs airway widening": ("cordotomy", "arytenoid", "reinnervation", "pacing"),
        }),
        (("subglottic", "tracheal stenosis"), {
            "etiology": ("idiopathic", "intubat", "autoimmune", "granulomatosis"),
            "endoscopic vs open": ("dilat", "laser", "steroid", "resection", "open"),
        }),
        (("dysphagia", "aspiration"), {
            "instrumental testing": ("fees", "vfss", "mbs"),
            "compensation vs rehabilitation": ("compens", "rehab", "diet", "therapy"),
        }),
    ],
    "Facial Plastics / Trauma": [
        (("mandib",), {
            "occlusion/biomechanics": ("occlusion", "tension", "compression", "load-bearing", "load sharing"),
            "closed vs ORIF": ("closed", "orif", "open reduction", "fixation"),
        }),
        (("noe", "naso-orbito", "nasoorbito"), {
            "medial canthal tendon": ("medial canthal", "canthal tendon", "telecanthus"),
            "classification/fixation": ("type i", "type ii", "type iii", "markowitz", "fixation"),
        }),
        (("orbital", "zmc"), {
            "vision emergency": ("vision", "afferent", "compartment", "canthotomy"),
            "repair indications/timing": ("diplopia", "enophthal", "repair", "timing"),
        }),
        (("facial nerve", "reanimation"), {
            "timing-dependent strategy": ("immediate", "delayed", "months", "muscle", "atrophy"),
            "static vs dynamic": ("static", "dynamic", "nerve transfer", "free muscle"),
        }),
    ],
    "Sleep Surgery": [
        (("adult psg", "adult osa", "obstructive sleep apnea"), {
            "severity/phenotype": ("ahi", "positional", "rem", "hypox"),
            "non-surgical first-line": ("cpap", "pap", "weight", "oral appliance"),
        }),
        (("dise",), {
            "collapse pattern": ("velum", "lateral", "tongue", "epiglott"),
            "procedure selection": ("concentric", "hypoglossal", "palatal", "tongue base"),
        }),
        (("hypoglossal",), {
            "candidacy": ("bmi", "ahi", "concentric", "dise", "cpap"),
            "implant anatomy/programming": ("inclusion", "exclusion", "cuff", "branch", "program"),
        }),
        (("mma", "maxillomandibular"), {
            "mechanism/selection": ("skeletal", "advance", "multilevel", "severe"),
            "tradeoffs": ("malocclusion", "numb", "paresthesia", "cosmetic"),
        }),
    ],
    "General ENT / Emergencies": [
        (("tracheostomy emergency",), {
            "fresh vs mature tract": ("fresh", "immature", "mature", "false passage"),
            "laryngectomy distinction": ("laryngectomy", "stoma", "upper airway"),
        }),
        (("postoperative neck hematoma",), {
            "bedside decompression": ("open", "bedside", "release", "sutures", "clips"),
            "airway after decompression": ("edema", "intubat", "airway"),
        }),
        (("post-tonsillectomy hemorrhage",), {
            "primary vs secondary": ("primary", "secondary", "day 5", "day 10"),
            "resuscitation/OR": ("iv", "resusc", "npo", "operating", "or "),
            "full stomach": ("full stomach", "aspiration", "rapid sequence"),
        }),
        (("deep neck",), {
            "space anatomy": ("parapharyngeal", "retropharyngeal", "danger space", "carotid space"),
            "airway/source control": ("airway", "drain", "source control"),
            "mediastinal spread": ("mediast", "descending"),
        }),
        (("carotid blowout",), {
            "threatened/impending/acute": ("threatened", "impending", "sentinel", "acute"),
            "endovascular/surgical control": ("endovascular", "stent", "embol", "ligation"),
        }),
    ],
}


def norm(s):
    return " ".join(str(s or "").lower().split())


def combined(m):
    return " ".join(norm(m.get(k)) for k in FIELDS)


def matches_topic(topic, needles):
    t = norm(topic)
    return any(n in t for n in needles)


def main():
    print("DEEP_CURRICULUM_AUDIT|v15.9|informational")
    total = 0
    flagged = 0
    for domain in DOMAINS:
        mods = data.DEEP_MODULES_V6.get(domain, [])
        print(f"DOMAIN|{domain}|topics={len(mods)}")
        for m in mods:
            total += 1
            topic = m.get("topic", "")
            issues = []
            for k in FIELDS:
                txt = norm(m.get(k))
                if not txt:
                    issues.append(f"missing_{k}")
                elif len(txt) < 95:
                    issues.append(f"thin_{k}:{len(txt)}")
            teach = norm(m.get("teach"))
            if teach and TEACH_PROMPT_RE.search(teach):
                issues.append("teach_reads_like_prompt")
            eti_text = norm(m.get("recognize")) + " " + norm(m.get("localize"))
            if len(eti_text) > 140 and not any(x in eti_text for x in ETIOLOGY_TERMS):
                issues.append("no_explicit_etiology_or_pathogenesis_signal")
            operate = norm(m.get("operate"))
            if len(operate) > 100 and not any(x in operate for x in DECISION_TERMS):
                issues.append("operate_lacks_decision_threshold_signal")
            # Similarity catches layers that are nominally six stages but teach
            # essentially the same sentence twice.
            pairs = (("recognize", "teach"), ("manage", "operate"), ("localize", "workup"))
            for a, b in pairs:
                aa, bb = norm(m.get(a)), norm(m.get(b))
                if len(aa) > 80 and len(bb) > 80:
                    ratio = SequenceMatcher(None, aa, bb).ratio()
                    if ratio >= .72:
                        issues.append(f"layer_overlap_{a}_{b}:{ratio:.2f}")
            # Topic-specific resident-level expectations.
            text = combined(m)
            for needles, expected in EXPECTATIONS.get(domain, []):
                if not matches_topic(topic, needles):
                    continue
                for label, terms in expected.items():
                    if not any(term in text for term in terms):
                        issues.append("missing_theme:" + label)
            if issues:
                flagged += 1
                print(f"FLAG|{domain}|{topic}|" + ",".join(issues))
                # Print enough actual text for a human reviewer to judge whether
                # the flag is real rather than trusting the heuristic blindly.
                print("  RECOGNIZE|" + str(m.get("recognize", ""))[:700].replace("\n", " "))
                print("  MANAGE|" + str(m.get("manage", ""))[:700].replace("\n", " "))
                print("  OPERATE|" + str(m.get("operate", ""))[:900].replace("\n", " "))
                print("  TEACH|" + str(m.get("teach", ""))[:900].replace("\n", " "))
        print("DOMAIN_END|" + domain)
    print(f"SUMMARY|topics_reviewed={total}|flagged={flagged}")
    print("NOTE|Flags are review candidates; no content is changed by this audit.")


if __name__ == "__main__":
    main()
