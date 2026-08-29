"""v27.9 — source-grounded salivary Concept Hub rebuild, benign lesions.

Rebuilds two remaining salivary canonical cards that were clinically useful but too
compressed: Ranula and Pleomorphic Adenoma / Warthin Tumor. Each ladder now adds a
new layer rather than restating the diagnosis: recognition -> anatomic/biologic
classification -> evaluation -> management -> operative judgment -> boards teaching.
"""

import re

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


RANULA_V279 = {
    "recognize": (
        "Recognize a ranula as a mucus-extravasation lesion arising overwhelmingly from the sublingual gland rather than as a generic 'floor-of-mouth cyst.' "
        "A simple ranula is usually a painless, fluctuant, translucent or blue lateral floor-of-mouth swelling that can elevate the tongue when large. A plunging ranula may present mainly as a soft upper-neck/submandibular swelling with little oral component. "
        "Pain, fever, fixation, a solid component, cranial neuropathy, or an atypical age/location should make you question the diagnosis rather than repeatedly aspirating a presumed ranula."
    ),
    "localize": (
        "Localize the lesion by its relationship to the mylohyoid and the sublingual space. A simple ranula remains in the floor of mouth above the mylohyoid; a plunging ranula tracks through a mylohyoid dehiscence or around the posterior free border into the submandibular/upper-neck spaces while retaining a sublingual source. "
        "This anatomy distinguishes it from a submandibular-gland process. The key operative neighborhood is the sublingual gland, Wharton duct, lingual nerve, and submandibular duct-ganglion complex: the lingual nerve courses lateral, inferior, then medial to Wharton duct as it travels anteriorly."
    ),
    "workup": (
        "Evaluate a classic small oral ranula primarily with history and examination, but image lesions that are plunging, recurrent, unusually large, primarily cervical, or diagnostically uncertain. Ultrasound can confirm a cystic lesion; contrast CT or MRI defines deep-space extent and the connection to the sublingual space. "
        "A tapering extension back toward the sublingual space ('tail sign') supports a plunging ranula, although absence of a conspicuous tail does not exclude one. The differential includes dermoid/epidermoid cyst, lymphatic malformation, thyroglossal or branchial anomaly depending on location, abscess, and cystic neoplasm. Aspiration may show thick mucin but is not a substitute for resolving discordant imaging or a suspicious mass."
    ),
    "manage": (
        "Manage the mucus source rather than treating only the collection. Observation can be reasonable for a small, minimally symptomatic lesion in selected patients, but repeated needle aspiration alone has a high recurrence problem because the leaking sublingual gland remains. For persistent, symptomatic, recurrent, or plunging disease, definitive treatment generally targets the ipsilateral sublingual gland, with decompression/evacuation of the ranula as needed. "
        "Marsupialization or micromarsupialization can be considered in selected simple oral lesions, especially when minimizing operative morbidity matters, but recurrence risk and the likelihood of needing subsequent gland-directed treatment should be part of counseling."
    ),
    "operate": (
        "For definitive surgery, transoral excision of the ipsilateral sublingual gland is the core source-control operation for many recurrent simple and plunging ranulas; a large cervical component often collapses without formal neck excision once the leak source is removed. Identify and protect Wharton duct and the lingual nerve, control sublingual-gland vessels carefully, and avoid injuring the contralateral duct papilla. "
        "Add a cervical approach selectively for unusual anatomy, inaccessible residual disease, infection/scarring, major diagnostic uncertainty, or a component that cannot be safely managed from the mouth. Counsel for recurrence, lingual-nerve sensory change, duct injury/stenosis, bleeding, infection, and postoperative floor-of-mouth swelling."
    ),
    "teach": (
        "Boards/chief framework: RANULA = SUBLINGUAL GLAND LEAK. SIMPLE stays above the mylohyoid; PLUNGING escapes into the neck but usually keeps the same sublingual source. A neck-dominant mass therefore does not automatically require a neck operation. "
        "The common management error is draining the reservoir without treating the faucet. The common anatomy error is forgetting the lingual nerve–Wharton duct relationship during transoral gland excision. If the lesion is solid, fixed, infected-appearing without a typical cystic pattern, or radiographically discordant, stop calling it a ranula and reopen the differential."
    ),
    "tags": ["ranula", "plunging ranula", "sublingual gland", "mylohyoid", "Wharton duct", "lingual nerve"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — ranula, sublingual-gland disease, and floor-of-mouth surgical anatomy",
        "K.J. Lee's Essential Otolaryngology, 12e — ranula and salivary-gland disorders",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — salivary lesions and floor-of-mouth differential",
    ],
}


BENIGN_PAROTID_V279 = {
    "recognize": (
        "Recognize pleomorphic adenoma (PA) and Warthin tumor as common benign parotid neoplasms, but do not treat 'benign parotid mass' as one disease. PA is classically a slow-growing, painless, firm/mobile mass and often occurs in younger or middle-aged adults; Warthin tumor commonly arises in the parotid tail in older adults, has a strong smoking association, and may be bilateral or multifocal. "
        "Rapid recent enlargement, pain, skin fixation, facial weakness, trismus, or pathologic nodes are red flags for malignancy or malignant transformation regardless of an earlier benign label."
    ),
    "localize": (
        "Localize the tumor to superficial versus deep parotid compartments and understand why the distinction changes exposure and facial-nerve strategy. PA has an incomplete/variable capsule with microscopic pseudopods and satellite nodules, so a grossly intact 'shell' is not a license for casual enucleation. Warthin tumor is usually well circumscribed, frequently near the lower pole/tail, and can be synchronous or metachronous on the opposite side. "
        "Deep-lobe lesions can displace the parapharyngeal fat and may require a different dissection trajectory even when histology is benign."
    ),
    "workup": (
        "Evaluate a persistent parotid mass with focused cranial-nerve/neck examination, ultrasound for accessible lesions, and tissue diagnosis—usually ultrasound-guided FNA or core biopsy according to local expertise and the question being asked. MRI is particularly useful for deep-lobe/parapharyngeal extent, facial-nerve/perineural concern, or complex soft-tissue anatomy; CT is useful when bone, calcification, or broader neck anatomy matters. "
        "Interpret cytology together with imaging and clinical behavior: a 'benign' needle result that conflicts with rapid growth, nerve dysfunction, infiltrative imaging, or nodes should not end the workup. For Warthin, concordant classic imaging/cytology in an asymptomatic patient can materially change the threshold for surgery."
    ),
    "manage": (
        "Management follows natural history and diagnostic certainty. A resectable PA is generally offered surgery because it tends to grow, can recur after inadequate removal, and carries a small but clinically meaningful long-term risk of carcinoma ex pleomorphic adenoma. A confidently diagnosed, asymptomatic Warthin tumor may be observed in selected patients, especially when comorbidity or operative morbidity outweighs benefit; growth, symptoms, cosmetic burden, diagnostic uncertainty, or patient preference favor excision. "
        "Smoking cessation should be encouraged in Warthin patients because of the strong association and broader health benefit."
    ),
    "operate": (
        "Tailor parotid surgery to tumor location while preserving an uninvolved facial nerve and avoiding tumor rupture. Depending on size, location, surgeon experience, and pathology confidence, selected superficial benign lesions may be treated with extracapsular dissection or partial/superficial parotidectomy; deep or large lesions require exposure that safely identifies/protects the nerve and achieves intact removal. "
        "For PA, do not intentionally enucleate or violate the capsule; rupture or spillage increases the difficulty of long-term recurrence control. Counsel about transient/permanent facial weakness, Frey syndrome, salivary fistula/sialocele, numbness, contour deformity, first-bite symptoms in relevant deep dissections, and the possibility of recurrent multifocal PA after prior rupture."
    ),
    "teach": (
        "Boards/chief discriminator: PA = PSEUDOPODS + RECURRENCE/MALIGNANT-TRANSFORMATION TIME HORIZON; WARTHIN = SMOKING + PAROTID TAIL + BILATERAL/MULTIFOCAL POTENTIAL. PA is benign but usually a surgical disease in a fit patient; Warthin can be an observation disease when diagnosis and behavior are convincingly benign. "
        "Facial paralysis is never a reassuring feature of a presumed benign parotid tumor. A long-standing PA that suddenly accelerates, becomes painful/fixed, or causes nerve dysfunction should raise concern for carcinoma ex pleomorphic adenoma and trigger a malignancy-level reassessment rather than routine benign-tumor planning."
    ),
    "tags": ["pleomorphic adenoma", "Warthin tumor", "parotid", "facial nerve", "parotidectomy", "carcinoma ex pleomorphic adenoma"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — benign salivary neoplasms and parotid surgery",
        "K.J. Lee's Essential Otolaryngology, 12e — salivary-gland neoplasms",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — parotid tumors and operative complications",
    ],
}


def apply_salivary_benign_rebuild_v279(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    targets = {
        "ranula": RANULA_V279,
        "pleomorphic adenoma warthin tumor": BENIGN_PAROTID_V279,
    }
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = targets.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v279"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
