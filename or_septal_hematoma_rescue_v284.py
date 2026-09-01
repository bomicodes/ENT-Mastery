"""v28.4 — post-septoplasty septal hematoma / abscess rescue.

Extends the existing recognition-only postoperative warning into an executable
resident/chief response. Textbooks remain foundational for septal anatomy and operative
principles; contemporary systematic reviews anchor the drainage/recurrence evidence.
"""

TARGET = "septoplasty"

RESCUE = [
    "SEPTAL COLLECTION COMMITMENT POINT: after septoplasty, disproportionate or increasing nasal pain/pressure, progressive bilateral obstruction, fever, purulent drainage, or a smooth boggy/fluctuant septal swelling should trigger urgent intranasal examination for septal hematoma or abscess. Do not dismiss a tense bilateral septal collection as routine postoperative edema or packing discomfort. Separation of mucoperichondrium from septal cartilage compromises its diffusion-dependent blood supply; delay can progress to infection, cartilage necrosis, septal perforation, and saddle-nose deformity.",
    "DRAINAGE BAILOUT: a true septal hematoma/abscess requires prompt evacuation rather than observation alone. Open the collection through an intranasal mucosal incision in a location that permits dependent drainage while avoiding unnecessary opposing mucosal injury, evacuate clot and/or pus completely, gently break clinically relevant loculations, irrigate, and inspect both sides of the septum because collections may communicate or be bilateral. Send purulent material for culture when abscess is suspected; culture should refine therapy but must not delay drainage of a clinically significant collection.",
    "PREVENT RE-ACCUMULATION: after evacuation, re-oppose the mucoperichondrial flaps and maintain drainage/obliteration of the dead space with an appropriate drain, quilting/transseptal sutures, nasal packing, or a procedure-specific combination. The endpoint is not simply 'blood came out'; it is a decompressed septum with restored flap-to-cartilage apposition and a plan that prevents re-collection. Re-examine early after drainage and again after removal of packing/drain as clinically appropriate because recurrence requires repeat evacuation/source control.",
    "INFECTION / RECONSTRUCTION FRAME: if abscess, systemic infection, immunocompromise, or contaminated postoperative findings are present, give systemic antimicrobial therapy directed initially at expected nasal flora and then tailored to cultures/local resistance and patient factors. Escalating fever, facial/orbital symptoms, neurologic symptoms, or systemic toxicity should trigger evaluation for extension rather than repeated office aspiration alone. Once acute infection/collection is controlled, document septal support and follow for perforation or developing saddle deformity; delayed reconstructive planning may be required after tissue viability and infection declare themselves.",
]

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — nasal septal anatomy, septoplasty, and complication principles",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — septal hematoma/abscess and septal surgery principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — septoplasty complications and nasal septal hematoma framework",
    "Jackson R, Jia W, Edafe O. Evaluation of the management of nasal septal haematoma and abscess: a systematic review. J Laryngol Otol. 2025;139(3):153-159. doi:10.1017/S0022215124001610",
    "Nanu DP et al. Unmasking Nasal Septal Hematoma/Abscess: A Systematic Review and Meta-analysis. OTO Open. 2024. doi:10.1002/oto2.174",
]


def _resolve(registry):
    reg = registry or {}
    if TARGET in reg:
        return TARGET, reg[TARGET]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if "septoplasty" in hay and "septorhinoplasty" not in hay:
            return slug, op
    return None, None


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        marker = text[:88].lower()
        if not any(marker in str(x).lower() for x in out):
            out.append(text)
            changed = True
    return out, changed


def apply_or_septal_hematoma_rescue_v284(registry):
    slug, op = _resolve(registry)
    if not op:
        return {"changed": [], "count": 0, "resolved": [], "missing": [TARGET]}
    op["postop"], c1 = _append_unique(op.get("postop"), RESCUE)
    op["sources"], c2 = _append_unique(op.get("sources"), SOURCES)
    op["septal_hematoma_rescue_v284"] = True
    op["septal_hematoma_semantic_role_v284"] = (
        "recognize septal collection -> urgent complete drainage -> culture abscess when present -> "
        "re-oppose mucoperichondrium/prevent re-collection -> antibiotics when infected -> early recheck"
    )
    return {"changed": [slug] if (c1 or c2) else [], "count": int(bool(c1 or c2)), "resolved": [slug], "missing": []}
