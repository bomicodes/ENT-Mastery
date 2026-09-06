"""v35.0 — source-grounded CRS phenotype, AERD, CRSsNP/CRSwNP, and AFRS depth.

Durable anatomy/pathophysiology and operative principles are grounded in Cummings 7e,
K.J. Lee 12e, and Pasha 6e. Management is deliberately updated to current AAO-HNSF
2025 CRS guidance and 2025-26 biologic evidence/indications where those postdate the texts.
"""

import re

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


CORE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — CRS inflammatory phenotypes, CRSwNP/CRSsNP, AERD/AFRS associations, topical-delivery and ESS principles",
    "K.J. Lee's Essential Otolaryngology, 12e — CRS diagnosis/differential, polyposis, AERD and allergic fungal rhinosinusitis clinical framework",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — CRS workup, medical therapy, surgery indications, AERD/AFRS resident-level management",
    "AAO-HNSF Clinical Practice Guideline: Adult Sinusitis Update, 2025 — objective CRS confirmation, modifying factors including AERD, topical therapy and contemporary biologic recommendations",
    "AAO-HNSF Clinical Practice Guideline: Surgical Management of Chronic Rhinosinusitis, 2025 — adult ESS candidacy, shared decision-making, surgical extent and postoperative care",
]


def _sources(*extra):
    return list(CORE_SOURCES) + list(extra)


PATCHES = {
    "crs phenotyping": {
        "recognize": "Recognize CHRONIC RHINOSINUSITIS as persistent sinonasal inflammation, not a synonym for recurrent 'sinus infections.' Symptoms must fit a chronic CRS syndrome and be paired with OBJECTIVE inflammatory evidence on nasal endoscopy and/or CT. Then phenotype the disease rather than stopping at the label: CRSsNP, CRSwNP, AFRS and clinically important modifiers such as asthma, AERD, immune dysfunction, ciliary disease or odontogenic disease behave differently and change counseling, recurrence risk and treatment choices.",
        "localize": "Localize CRS to the sinonasal mucosa and drainage pathways while separating PHENOTYPE from ENDOTYPE. Phenotype is the clinically observable pattern such as polyps versus no polyps or AFRS; endotype refers to the dominant inflammatory biology, commonly type-2 inflammation in many Western CRSwNP patients but not universally. Do not equate a single biomarker with a complete endotype or assume all polyps share identical biology. Structural narrowing can worsen ventilation/topical access, but CRS is fundamentally an inflammatory disease rather than simply blocked plumbing.",
        "workup": "Confirm objective disease before committing a patient to long-term CRS treatment or surgery. Use nasal endoscopy to document edema, purulence, polyps and postoperative anatomy; obtain CT when it will confirm extent/anatomy or guide surgery rather than as a symptom-only screening test. Ask specifically about asthma, NSAID reactions/AERD, prior surgery, smell loss, allergy, immune deficiency clues, dental source and unilateral red flags. Allergy or immune testing is selective. Interpret eosinophils, total IgE and other biomarkers as context rather than stand-alone diagnostic labels.",
        "manage": "Treat the phenotype and patient goals. SALINE IRRIGATION plus TOPICAL INTRANASAL CORTICOSTEROID therapy are durable baseline treatments; systemic antibiotics are not reflexive chronic anti-inflammatory therapy merely because the CT is abnormal. Short systemic steroid courses may be useful selectively, especially for severe polyp inflammation, after weighing risk. For recalcitrant CRSwNP, integrate asthma/AERD status, prior ESS, systemic-steroid burden, smell loss and quality of life when discussing revision surgery versus a biologic; contemporary guidance does NOT support biologics for routine CRS without nasal polyps.",
        "operate": "Offer ESS when symptoms, objective disease, phenotype and prior appropriate therapy support a reasonable expectation of benefit—not after an arbitrary one-size-fits-all antibiotic checklist. The operative goal is disease-appropriate clearance and creation of durable access for ventilation, surveillance and TOPICAL THERAPY while preserving critical boundaries: orbit, skull base, carotid and optic nerve. Extent should match disease burden and anatomy; recalcitrant inflammatory phenotypes may require broader access than limited focal disease. Surgery modifies anatomy and inflammatory burden but does not erase the underlying inflammatory tendency.",
        "teach": "Senior model: diagnose CRS with SYMPTOMS + OBJECTIVE INFLAMMATION, then ask 'which phenotype, which modifiers, which prior treatment, and what outcome matters?' Phenotype guides prognosis and treatment; endotype may refine biologic thinking but is not a magic single-test answer. The trap is treating every CT opacity as infection, every polyp patient as identical, or every refractory patient as either 'needs surgery' or 'needs a biologic' without integrating disease type, asthma/AERD, prior ESS, steroid burden and patient preference.",
        "tags": ["CRS", "phenotype", "endotype", "CRSsNP", "CRSwNP", "objective inflammation", "biologics", "ESS"],
        "source_basis": _sources("Current biologic labeling/evidence through 2026 — phenotype-specific add-on biologic use is updated separately from durable textbook anatomy and ESS principles"),
    },
    "aerd": {
        "recognize": "Recognize ASPIRIN-EXACERBATED RESPIRATORY DISEASE (AERD/NSAID-exacerbated respiratory disease) as the clinical combination of asthma, typically severe/recurrent CRSwNP, and reproducible upper/lower respiratory reactions to COX-1–inhibiting NSAIDs. It is not simply a vague 'aspirin allergy.' Ask what drug caused the reaction, timing, respiratory features, alcohol sensitivity, asthma control, smell loss, prior polyp surgery and how rapidly polyps recur.",
        "localize": "Localize AERD as dysregulated arachidonic-acid/eicosanoid biology with excess cysteinyl-leukotriene signaling in a type-2 inflammatory airway phenotype. The clinically important concept is the UNITED AIRWAY: the nose/sinuses and asthma must be managed together. Cross-reactivity is driven largely by COX-1 inhibition, so do not teach that every NSAID has identical risk; medication counseling should distinguish strong COX-1 inhibitors from appropriately selected alternatives and specialist-supervised challenge when needed.",
        "workup": "A convincing history of asthma + CRSwNP + stereotyped respiratory reactions to COX-1 NSAIDs can establish the syndrome clinically. If the history is uncertain and the answer will change management, refer for a CONTROLLED ASPIRIN/NSAID CHALLENGE in an appropriate setting rather than advising an unsupervised trial. Assess asthma control before challenge/desensitization and document sinonasal burden objectively. Do not diagnose AERD from nasal polyps plus an unrelated rash or GI intolerance to aspirin.",
        "manage": "Build treatment across both airways: topical sinonasal corticosteroid therapy and saline, guideline-based asthma treatment, and often a leukotriene-pathway agent. For persistent disease, discuss ASPIRIN DESENSITIZATION followed by aspirin therapy (ATAD) versus a BIOLOGIC based on asthma/polyp severity, bleeding/GI risk, pregnancy plans, adherence, cost/access and patient goals. Current evidence supports both strategies in selected patients, but there is no universal rule that every AERD patient must receive ATAD or that a biologic always replaces it.",
        "operate": "ESS is often important when polyp burden and sinus disease remain substantial because it clears inflammatory load and creates access for postoperative topical therapy; in patients pursuing ATAD, surgery is commonly optimized before desensitization when clinically appropriate. Do not present surgery as curative: AERD carries a high recurrence tendency and requires longitudinal anti-inflammatory management. Escalate perioperative planning when asthma is poorly controlled or the history suggests severe NSAID reactions.",
        "teach": "Boards/chief discriminator: AERD = ASTHMA + CRSwNP + COX-1 NSAID respiratory reaction. The senior decision is not merely 'avoid aspirin.' Decide whether the patient needs disease-control optimization, ESS, ATAD, biologic therapy, or a combination, and know why. Trap: calling any aspirin adverse effect AERD, challenging an unstable asthmatic, or forgetting that recurrent sinonasal disease and asthma are one inflammatory airway problem.",
        "tags": ["AERD", "NSAID-exacerbated respiratory disease", "CRSwNP", "asthma", "aspirin desensitization", "ATAD", "biologics"],
        "source_basis": _sources("AAAAI Work Group Report on aspirin desensitization and aspirin therapy after desensitization in AERD — candidate selection, contraindications, optimization and maintenance therapy", "Peer-reviewed AERD biologic literature through 2026 — biologics and ATAD are individualized options; no single universal sequence is established"),
    },
    "crssnp": {
        "recognize": "Recognize CRSsNP as chronic rhinosinusitis with the required chronic symptom pattern and OBJECTIVE inflammation but without endoscopically visible nasal polyps. Do not infer CRSsNP from facial pressure alone, a remote history of antibiotics, or incidental CT mucosal thickening. Reconsider migraine, neuralgia, dental disease and other mimics when objective inflammatory evidence does not match the symptom story.",
        "localize": "Localize CRSsNP to inflamed sinonasal mucosa and involved drainage pathways while recognizing biologic heterogeneity. Absence of polyps does not mean the disease is simply bacterial obstruction, and it does not guarantee a non–type-2 endotype. Anatomy matters for drainage and surgical access, but the disease remains an inflammatory mucosal disorder.",
        "workup": "Document objective disease by endoscopy and/or CT and evaluate pattern, laterality and likely drivers. Unilateral purulence or maxillary-predominant disease should trigger consideration of odontogenic disease, foreign body, fungal process or neoplasm rather than automatic 'routine CRS.' Culture is selective for refractory purulence or unusual hosts, not a universal diagnostic requirement. Consider immune evaluation when the infection history or disease behavior supports it.",
        "manage": "Use saline irrigation and intranasal corticosteroid therapy as durable baseline management. Avoid serial empiric antibiotic courses for stable chronic symptoms without evidence of an acute bacterial exacerbation. Tailor additional therapy to comorbidity and phenotype. Current AAO-HNSF guidance specifically argues against routine biologic therapy for CRS WITHOUT nasal polyps; a biologic indication should not be extrapolated from CRSwNP merely because symptoms are severe.",
        "operate": "Consider ESS when objective disease and quality-of-life burden persist despite appropriate medical management and the expected benefit justifies surgery. Plan extent from CT/endoscopy, prior surgery and disease distribution rather than a fixed template. Preserve skull base/orbit safety and create durable access for postoperative topical therapy. A technically patent sinus with persistent symptoms should trigger reassessment of inflammatory control and non-CRS symptom generators rather than reflex revision.",
        "teach": "Senior trap: CRSsNP is not 'chronic bacterial sinusitis without polyps.' Confirm objective inflammation, look for focal etiologies and mimics, use topical anti-inflammatory therapy, and reserve antibiotics for an appropriate bacterial context. Biologics belong to a different current evidence/indication framework than routine CRSsNP.",
        "tags": ["CRSsNP", "objective CRS", "endoscopy", "CT", "topical corticosteroid", "ESS", "no routine biologic"],
        "source_basis": _sources(),
    },
    "crswnp": {
        "recognize": "Recognize CRSwNP as chronic rhinosinusitis with bilateral inflammatory nasal polyps in the usual presentation, commonly accompanied by obstruction and prominent smell loss. A unilateral 'polyp,' bleeding mass, severe focal pain or atypical appearance requires a different differential and often tissue diagnosis rather than being assumed to be routine inflammatory polyposis. Ask about asthma, AERD, prior ESS/systemic steroids and recurrence rate because these strongly affect disease severity and management.",
        "localize": "Localize CRSwNP as a diffuse inflammatory mucosal phenotype, frequently type-2–predominant in contemporary U.S. practice, rather than a mechanical overgrowth alone. Polyps commonly arise from ethmoid/middle-meatal inflammatory disease. Asthma and AERD mark important united-airway modifiers and often more recalcitrant disease; AFRS is a distinct polyp-associated phenotype with allergic mucin/fungal hypersensitivity features.",
        "workup": "Confirm polyps endoscopically and define sinus extent with CT when it will guide management or surgery. Assess smell, asthma/AERD, prior systemic steroid exposure, previous operations and quality-of-life burden. Do not use serum eosinophils or total IgE alone to diagnose CRSwNP, but biomarkers and comorbid asthma can inform biologic selection in context. Atypical unilateral disease deserves evaluation for inverted papilloma, malignancy, encephalocele or other focal pathology.",
        "manage": "Use saline irrigation and topical intranasal corticosteroid therapy as baseline treatment, often with high-volume postoperative topical delivery when anatomy permits. Short systemic steroid courses may be considered selectively, but repeated systemic-steroid dependence should trigger a safer long-term strategy. For severe/refractory CRSwNP, discuss ESS and/or an FDA-approved add-on biologic according to disease burden, asthma/AERD, prior surgery, steroid exposure, smell loss, contraindications, access and patient preference. Biologic options and age/phenotype indications have changed since the core textbooks and must be kept current rather than memorized from an older list.",
        "operate": "ESS removes obstructing inflammatory tissue, opens diseased sinuses and—critically—creates access for postoperative topical therapy and surveillance. Extent should match inflammatory burden, prior surgery and anatomy; recalcitrant diffuse polyposis often needs more complete surgery than a limited focal process. Protect orbit and skull base. Surgery is not immunologic cure, so pair technically successful surgery with longitudinal anti-inflammatory control and reassess recurrence phenotype rather than repeatedly operating without a medical strategy.",
        "teach": "Senior decision: in refractory CRSwNP, frame surgery and biologics as tools within longitudinal inflammatory control, not competing dogmas. The key variables are objective burden, asthma/AERD, prior ESS, systemic-steroid toxicity, smell/QOL, recurrence tempo and patient preference. Current 2025-26 guidance supports biologics for appropriately selected CRSwNP—not for routine CRSsNP—and the FDA-approved option set has expanded since older textbooks.",
        "tags": ["CRSwNP", "nasal polyps", "type 2 inflammation", "asthma", "AERD", "biologics", "ESS", "smell loss"],
        "source_basis": _sources("AAO-HNS Bulletin, Spring 2026 biologics update — tezepelumab FDA approval for add-on maintenance treatment of CRSwNP in October 2025 and evolving age/phenotype indications"),
    },
    "afrs": {
        "recognize": "Recognize ALLERGIC FUNGAL RHINOSINUSITIS (AFRS) as a distinct, usually highly inflammatory polypoid CRS phenotype characterized by atopy/type-2 inflammation, eosinophilic 'allergic' mucin containing fungal elements and often striking heterogeneous/hyperattenuating sinus material with expansion or bony remodeling. It is NOT invasive fungal sinusitis: the defining process is allergic/inflammatory rather than tissue-invasive fungal necrosis.",
        "localize": "Localize AFRS to sinuses packed with tenacious eosinophilic mucin and fungal debris, often with polyposis and anatomic distortion. Expansion, thinning or erosion can occur from chronic pressure/inflammation and does not by itself prove invasive fungal disease. Tissue invasion, vascular invasion, necrosis, cranial neuropathy or an immunocompromised host should immediately reopen the differential toward invasive fungal rhinosinusitis.",
        "workup": "Integrate endoscopy, CT pattern, atopic history and operative/pathologic findings rather than relying on a fungal culture alone, because fungi can colonize sinonasal cavities without causing AFRS. Pathology should assess eosinophilic mucin/fungal elements and, critically, absence of tissue invasion when AFRS is the diagnosis. Define orbital/skull-base distortion on CT before surgery. Consider MRI when extension or the relationship to orbit/skull base cannot be adequately characterized on CT.",
        "manage": "Long-term control requires anti-inflammatory therapy and surveillance after clearance of the obstructing mucin burden. Use topical corticosteroid therapy, often facilitated by postoperative sinus access; systemic corticosteroids may be used selectively for severe inflammatory flares while minimizing cumulative toxicity. Do not teach routine systemic antifungal therapy as a universal cornerstone. Biologic therapy has evolved beyond the core textbooks: DUPILUMAB received a specific U.S. FDA AFRS indication in February 2026, so contemporary counseling should distinguish that new option from older evidence and still individualize treatment by severity, age, prior surgery, steroid burden and comorbidity.",
        "operate": "ESS is central when substantial AFRS burden is present: remove allergic mucin and polyps, ventilate involved sinuses and create durable access for topical therapy and postoperative debridement/surveillance. Expect distorted anatomy and protect orbit/skull base; extensive expansion or erosion may make landmarks unreliable, so senior-level planning emphasizes image review, navigation when appropriate and stopping/reorienting rather than following diseased anatomy blindly. Surgery reduces burden but does not eliminate the underlying inflammatory tendency.",
        "teach": "Board/chief discriminator: AFRS = ALLERGIC/INFLAMMATORY fungal-associated CRS with eosinophilic mucin, typically polyps and characteristic imaging; invasive fungal sinusitis = TISSUE INVASION/NECROSIS and a very different emergency. Senior trap: calling bone erosion 'invasion,' treating a positive fungal culture as diagnostic by itself, or prescribing antifungals while neglecting surgical clearance and long-term anti-inflammatory control. Management updates matter: a specific dupilumab AFRS indication arrived in 2026, after the core textbooks.",
        "tags": ["AFRS", "allergic fungal rhinosinusitis", "eosinophilic mucin", "fungal elements", "noninvasive", "ESS", "dupilumab"],
        "source_basis": _sources("Cummings 7e — AFRS is treated with ESS plus medical anti-inflammatory management; distorted CRSwNP-type anatomy requires experienced surgery and durable topical access", "AAO-HNS Bulletin, Spring 2026 biologics update — dupilumab received a specific U.S. FDA indication for AFRS in February 2026; this postdates the core textbooks"),
    },
}


def apply_rhinology_crs_inflammatory_depth_v350(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = PATCHES.get(_norm(module.get("topic")))
        if payload is None:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v350"] = True
        module["deliberate_review_v350"] = {
            "foundation": "disease definition, inflammatory biology, phenotype/endotype and high-value differential",
            "application": "objective workup plus phenotype-specific medical treatment using current guidance",
            "senior_decision": "ESS/biologic/ATAD selection, recurrence strategy, danger-zone differential and bailout thinking",
        }
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}