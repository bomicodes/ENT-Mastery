"""v35.3 — source-grounded fungal rhinosinusitis boundary depth.

AFRS already has dedicated v35.0 depth; this pass deliberately reuses that strong material
and strengthens only the exact canonical Fungal Ball and Invasive Fungal Rhinosinusitis
concepts where the management/urgency boundary is high consequence. Durable principles are
grounded in Cummings 7e, K.J. Lee 12e, and Pasha 6e and cross-checked against ICAR-RS 2021
and the ECMM/MSG-ERC global mucormycosis guideline.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")
CORE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — noninvasive versus invasive fungal rhinosinusitis, pathology, imaging and operative principles",
    "K.J. Lee's Essential Otolaryngology, 12e — fungal ball, AFRS and invasive fungal rhinosinusitis clinical distinctions",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — resident-level fungal sinusitis diagnosis, debridement and complication framework",
    "International Consensus Statement on Allergy and Rhinology: Rhinosinusitis (ICAR-RS 2021) — fungal/AFRS classification and evidence-based rhinosinusitis framework",
]

def _sources(*extra): return list(CORE_SOURCES) + list(extra)

PATCHES = {
    "Fungal Ball": {
        "recognize": "Recognize a FUNGAL BALL (mycetoma) as a NONINVASIVE dense collection of fungal hyphae/debris within a sinus, classically unilateral and often maxillary or sphenoid. The key discriminator is fungus within luminal debris WITHOUT mucosal or vascular tissue invasion. It is not AFRS simply because fungus is present, and it is not invasive fungal rhinosinusitis merely because CT shows hyperdensity or adjacent bony change.",
        "localize": "Localize disease to the involved sinus lumen and ask why that sinus is affected: obstruction, prior dental work/odontogenic material, altered anatomy or prior surgery can matter. Chronic pressure/inflammation may produce sclerosis or remodeling; the senior distinction is that bone change alone does not equal angioinvasion. Sphenoid disease deserves special respect because optic nerve, cavernous sinus and carotid complications can become clinically important even when the process began noninvasively.",
        "workup": "Use endoscopy and CT to define laterality, involved sinus, hyperattenuating/concreted material, anatomy and any destructive or extrasinus features. Unilateral disease requires a broad differential including odontogenic disease and neoplasm. At surgery send representative debris and abnormal mucosa for pathology; fungal elements within debris support fungal ball, while TISSUE or VASCULAR INVASION changes the diagnosis and urgency. Immunocompromise, necrotic mucosa, cranial neuropathy, orbital findings, severe acute pain or rapid progression should trigger an invasive-fungal pathway rather than routine elective management.",
        "manage": "For a confirmed uncomplicated fungal ball, definitive management is mechanical/surgical clearance with restoration of drainage and ventilation when symptomatic or clinically indicated; routine prolonged systemic antifungal therapy is not a standard requirement for a noninvasive fungal ball. Address contributory odontogenic disease when present. If pathology shows invasion or the clinical course suggests invasive disease, stop treating the case as fungal ball and escalate urgently.",
        "operate": "Open the involved sinus adequately to remove concreted fungal debris completely, irrigate/clear retained material, preserve safe boundaries and obtain tissue when the appearance is atypical. For maxillary disease, inspect recesses and address dental source when relevant; for sphenoid disease, respect optic nerve/carotid anatomy. Do not overcall simple bony remodeling as invasion, but do not undercall devitalized mucosa or suspicious extrasinus extension—biopsy those areas and escalate if invasion is found.",
        "teach": "Senior boundary: FUNGAL BALL = luminal fungal burden, usually unilateral, with NO tissue invasion. AFRS = eosinophilic allergic mucin/type-2 inflammatory polyposis without invasion. INVASIVE fungal rhinosinusitis = fungal tissue/vascular invasion and a time-critical threat. The management consequence of confusing them is large: fungal ball usually needs clearance, not empiric prolonged systemic antifungals, whereas invasive disease requires urgent multidisciplinary treatment.",
        "tags": ["fungal ball","mycetoma","noninvasive fungal rhinosinusitis","unilateral sinus disease","sphenoid","pathology"],
        "source_basis": _sources(),
    },
    "Invasive Fungal Rhinosinusitis": {
        "recognize": "Recognize INVASIVE FUNGAL RHINOSINUSITIS as fungal invasion of sinonasal tissue, often with angioinvasion, thrombosis and ischemic necrosis. Acute invasive disease is a TIME-CRITICAL emergency, classically in neutropenia/hematologic malignancy, transplant/immunosuppression, poorly controlled diabetes or ketoacidosis, although host context varies. Early symptoms and CT can be deceptively subtle; severe focal pain, necrotic/discolored mucosa, facial numbness, cranial neuropathy, orbital signs, vision change or rapid progression demand escalation.",
        "localize": "Localize beyond the sinus lumen because angioinvasion permits spread across expected anatomic boundaries into orbit, pterygopalatine/infratemporal fossae, skull base, cavernous sinus and intracranial compartments. A normal-looking turbinate or absence of dramatic bone erosion does not exclude early invasive disease. Distinguish acute fulminant invasion from more indolent chronic/granulomatous invasive forms, but never let subtype labeling delay urgent action when the presentation is acute and high risk.",
        "workup": "In a high-risk patient with suspicious symptoms/endoscopy, obtain urgent nasal endoscopy and targeted biopsy of abnormal or suspicious mucosa for frozen/permanent histopathology; diagnosis hinges on demonstrating TISSUE INVASION, not a positive fungal culture alone. CT rapidly defines sinonasal anatomy and extrasinus soft-tissue changes; MRI is especially useful when orbital apex, cavernous sinus, perineural, skull-base or intracranial extension is suspected. Send tissue for histopathology and fungal studies without delaying treatment in a compelling case, and simultaneously evaluate/correct reversible host factors such as neutropenia or ketoacidosis with the appropriate teams.",
        "manage": "Treat suspected/confirmed acute invasive fungal rhinosinusitis as an emergency with coordinated ENT, infectious-disease, pathology, radiology and host-disease teams. Management combines prompt surgical source control/debridement of nonviable infected tissue, immediate appropriate SYSTEMIC ANTIFUNGAL therapy tailored to likely/identified organism and host, and reversal of modifiable immunometabolic risk when possible. Mucormycosis guidance strongly supports urgent surgical plus medical treatment; do not wait for slow cultures when histology/clinical evidence is compelling.",
        "operate": "Debride devitalized/invaded tissue to viable bleeding margins when safely achievable, obtain mapping specimens when extent is uncertain, and plan serial endoscopic reassessment/re-debridement according to residual disease and host response. Escalate immediately for orbital apex/vision, cavernous sinus, skull-base, carotid or intracranial involvement; multidisciplinary decisions about orbital or skull-base procedures must reflect disease extent, visual prognosis, systemic status and goals—not a simplistic automatic exenteration rule. Preserve critical structures when oncologically/infectiously safe, but source control cannot be cosmetic.",
        "teach": "Senior decision model: HOST RISK + rapid clinical trajectory + endoscopy/imaging raise suspicion, but HISTOPATHOLOGIC TISSUE INVASION defines invasive disease. Do not require black eschar, dramatic bone erosion or a positive culture before acting. Separate this from fungal ball and AFRS because the treatment clock is different: acute invasive disease requires urgent biopsy, systemic antifungal therapy, aggressive source control and host-factor correction, with repeated reassessment until disease control is secure.",
        "tags": ["invasive fungal rhinosinusitis","AIFRS","angioinvasion","mucormycosis","frozen section","debridement","orbital apex"],
        "source_basis": _sources("ECMM/MSG-ERC Global Guideline for the Diagnosis and Management of Mucormycosis (Lancet Infectious Diseases, 2019) — rapid diagnosis, urgent surgical intervention plus systemic antifungal therapy and reversal of underlying risk", "Kim et al., International Forum of Allergy & Rhinology 2021 systematic review/meta-analysis — intraoperative frozen section has high specificity and useful diagnostic performance in acute invasive fungal rhinosinusitis"),
    },
}

def apply_rhinology_fungal_boundary_depth_v353(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        topic = str(module.get("topic") or "")
        payload = PATCHES.get(topic)
        if payload is None: continue
        for field in FIELDS: module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v353"] = True
        module["deliberate_review_v353"] = {"foundation":"noninvasive versus tissue-invasive fungal disease and host/pathology distinctions","application":"unilateral fungal-ball workup versus urgent biopsy/imaging pathway for suspected invasion","senior_decision":"clearance versus emergency source control/systemic antifungal therapy, extension mapping and re-debridement decisions"}
        patched.append(topic)
    expected, actual = set(PATCHES), set(patched)
    if actual != expected: raise RuntimeError(f"v35.3 canonical patch-target mismatch: missing={sorted(expected-actual) or 'none'} unexpected={sorted(actual-expected) or 'none'}")
    if app_module is not None: app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
