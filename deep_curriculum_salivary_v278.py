"""v27.8 — source-grounded salivary malignancy Concept Hub rebuild.

Deepens the canonical Salivary Adenoid Cystic Carcinoma / Perineural Spread card
into six distinct resident-level layers. The ladder emphasizes the clinically
important behavior of ACC: neurotropism, long natural history, late distant
failure, and management that follows named-nerve anatomy rather than the visible
primary alone.
"""

import re

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


ACC_V278 = {
    "recognize": (
        "Recognize adenoid cystic carcinoma (ACC) as a salivary malignancy whose clinical behavior can look deceptively indolent. "
        "It may arise in major glands or minor salivary sites such as the palate and can present as a slowly enlarging firm mass, "
        "but pain, paresthesia, numbness, facial weakness, or another cranial neuropathy should immediately raise concern for neural involvement. "
        "The resident-level pearl is that a small-appearing primary is not necessarily biologically limited: ACC is strongly neurotropic, can recur locally, "
        "and may develop distant metastases years after apparently successful local treatment."
    ),
    "localize": (
        "Localize ACC along both the gland compartment and the involved nerve. Perineural invasion is microscopic tumor involving or surrounding nerves; "
        "perineural spread is clinically or radiographically evident extension along a named nerve. Symptoms help map the route: palatal or maxillary disease with V2 numbness "
        "should make you follow the infraorbital/maxillary pathway toward foramen rotundum; mandibular or floor-of-mouth sensory change can implicate V3 toward foramen ovale; "
        "parotid disease with facial weakness raises concern for CN VII involvement toward the stylomastoid foramen and facial canal. Do not stop localization at the palpable mass—"
        "the true oncologic extent may run proximally toward the skull base."
    ),
    "workup": (
        "Evaluate ACC with tissue diagnosis plus imaging that answers the neural-extent question. MRI with contrast and appropriate fat-suppressed sequences is especially useful when "
        "perineural spread is suspected; inspect the entire expected nerve pathway for enlargement, enhancement, loss of normal fat at neural foramina, denervation change, and skull-base extension. "
        "CT complements MRI for bone involvement and surgical anatomy. Stage the neck and chest according to site and risk because distant hematogenous failure, particularly pulmonary metastasis, "
        "is an important part of ACC biology. On pathology, document margins, perineural invasion, grade/solid component where reported, lymphovascular invasion, and nodal status because these features alter adjuvant planning."
    ),
    "manage": (
        "For resectable disease, management centers on complete oncologic excision when that can be achieved with acceptable morbidity, followed by multidisciplinary postoperative planning. "
        "Current ASCO guidance recommends postoperative radiation for all resected ACC; perineural invasion, positive margins, advanced T stage, nodal disease, and lymphovascular invasion further reinforce the indication. "
        "When a named nerve is involved, radiation planning may include the associated neural pathway proximally toward the skull base rather than treating only the surgical bed. "
        "Routine concurrent chemotherapy is not a default addition to postoperative radiation outside an appropriate clinical-trial setting."
    ),
    "operate": (
        "The advanced decision is how far to pursue a nerve or skull-base margin without creating morbidity disproportionate to achievable control. Map preoperative symptoms and MRI to the specific nerve, "
        "plan the resection around the full clinically involved pathway, and obtain proximal neural margins when surgically meaningful. Grossly involved expendable sensory nerve may require sacrifice; major motor-nerve decisions require explicit discussion of oncologic benefit, reconstructive options, "
        "and function. Clinical or radiographic skull-base perineural extension may make a conventional gland resection inadequate or unresectable and should trigger skull-base/radiation multidisciplinary planning rather than piecemeal chasing of tumor. "
        "Neck treatment is driven by primary site, T category, grade, and clinical nodal disease; ACC is not managed as though occult nodal spread is automatically the dominant problem."
    ),
    "teach": (
        "Boards/chief framework: ACC = FOLLOW THE NERVE and FOLLOW FOR YEARS. New pain or numbness is oncologic anatomy until proven otherwise. Distinguish microscopic perineural invasion from gross perineural spread, "
        "trace the named nerve centrally on MRI, and remember that a negative neck does not neutralize margin or neural risk. Resected ACC generally receives postoperative radiation, and an involved nerve may need coverage toward the skull base. "
        "Long surveillance matters because distant recurrence can occur late, often after good local control. The common mistake is to let a slow-growing primary or cN0 neck falsely reassure you about the disease's long-term behavior."
    ),
    "tags": ["adenoid cystic carcinoma", "salivary cancer", "perineural invasion", "perineural spread", "skull base", "MRI", "postoperative radiation"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — salivary gland malignancy, adenoid cystic carcinoma, and perineural spread",
        "K.J. Lee's Essential Otolaryngology, 12e — salivary gland neoplasms",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide — salivary malignancy",
        "ASCO Clinical Practice Guideline: Management of Salivary Gland Malignancy (Geiger et al., J Clin Oncol 2021)",
    ],
    "source_grounded_v278": True,
}


def apply_salivary_acc_rebuild_v278(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        topic = _norm(module.get("topic"))
        if topic != "salivary adenoid cystic carcinoma perineural spread":
            continue
        for field in FIELDS:
            module[field] = ACC_V278[field]
        module["tags"] = list(ACC_V278["tags"])
        module["source_basis"] = list(ACC_V278["source_basis"])
        module["source_grounded_v278"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
