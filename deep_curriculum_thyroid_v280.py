"""v28.0 — source-grounded thyroid Concept Hub rebuild.

Separates the broad Differentiated Thyroid Cancer card from its Active Surveillance
subconcept. The parent card teaches diagnosis/risk/initial treatment; the surveillance
card teaches patient + tumor selection, ultrasound anatomy, monitoring, and triggers
for delayed intervention. This prevents the two cards from becoming near-duplicates.
"""

import re

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


DTC_V280 = {
    "recognize": (
        "Recognize differentiated thyroid cancer (DTC) as papillary, follicular, and oncocytic/Hürthle-cell carcinoma arising from follicular cells—not as one biologically uniform tumor. Most patients present with an asymptomatic thyroid nodule, but rapid growth, fixation, dysphonia, dysphagia, hemoptysis, bulky adenopathy, or vocal-fold paresis raise concern for invasive disease. Papillary thyroid carcinoma most often spreads to cervical lymph nodes; follicular carcinoma is defined by capsular and/or vascular invasion and more characteristically spreads hematogenously; oncocytic carcinoma can behave more aggressively and may be less iodine-avid."
    ),
    "localize": (
        "Localize disease before choosing an operation: define which lobe contains the primary, whether there is multifocal/bilateral disease, the relationship to the thyroid capsule, trachea, esophagus, and recurrent laryngeal nerve, and whether central (VI/VII) or lateral neck nodes are clinically involved. Separate AJCC stage—which estimates disease-specific mortality—from recurrence-risk features that drive extent of adjuvant therapy and surveillance. Extrathyroidal extension, clinically apparent nodal disease, distant metastasis, aggressive histology, and unfavorable molecular/biologic features move the patient away from a de-escalated pathway."
    ),
    "workup": (
        "Evaluate a suspected DTC with high-quality thyroid and cervical lymph-node ultrasound plus ultrasound-guided FNA of the thyroid lesion and suspicious nodes when it will change management. Cytology is interpreted through the Bethesda framework; molecular testing is most useful when it resolves an indeterminate-cytology decision rather than as a blanket test for every nodule. Obtain laryngeal examination when there is dysphonia, prior neck surgery, invasive/posterior disease, or another reason to suspect vocal-fold dysfunction. Contrast CT/MRI is appropriate when bulky nodal disease, substernal extension, or invasion of aerodigestive/RLN structures cannot be mapped adequately by ultrasound. Serum thyroglobulin is a surveillance tumor marker after treatment; it is not a screening test that establishes the initial diagnosis of thyroid cancer."
    ),
    "manage": (
        "Manage DTC with risk-adapted rather than automatically maximal therapy. Under the 2025 ATA framework, appropriately selected intrathyroidal, node-negative cancers confined to one lobe can often be treated with lobectomy, with lobectomy favored for tumors ≤2 cm and either lobectomy or total thyroidectomy reasonable for many >2 to ≤4 cm tumors depending on tumor features, contralateral disease, follow-up strategy, and patient preference. Total thyroidectomy is generally favored when disease burden or biology makes bilateral treatment, radioactive iodine, or thyroglobulin-based follow-up important—for example larger primary tumors, gross extrathyroidal extension, clinically significant nodal disease, or distant metastasis. Therapeutic compartment-oriented nodal dissection is performed for clinically involved nodal disease; routine prophylactic lateral neck dissection has no role. Radioactive iodine and TSH targets are then selected according to recurrence risk and response rather than given identically to every DTC patient."
    ),
    "operate": (
        "The operation is an oncologic resection performed around structures whose function matters for decades. Preoperatively map nodal disease and anticipate whether the recurrent laryngeal nerve, trachea, esophagus, strap muscles, or major vessels may be involved. Intraoperatively identify/preserve an uninvolved RLN and viable parathyroids with their blood supply, remove gross disease without tumor violation, and perform nodal surgery by anatomic compartment rather than node-picking. If cancer is discovered after lobectomy, completion thyroidectomy is no longer automatic: the 2025 ATA approach allows it to be considered when needed for persistent disease, radioactive iodine strategy, or a follow-up plan that materially benefits from total thyroidectomy. Balance oncologic benefit against bilateral RLN and hypoparathyroidism risk."
    ),
    "teach": (
        "Chief/boards framework: DTC management is a sequence—MAP the primary + nodes → define tumor BIOLOGY/RISK → choose the LEAST operation that still meets oncologic goals → add RAI/TSH suppression only when risk justifies it → reassess response over time. Do not confuse nodal recurrence risk with mortality staging, and do not equate a thyroid-cancer diagnosis with mandatory total thyroidectomy. Papillary cancer is lymphotropic; follicular cancer requires capsular/vascular invasion for diagnosis and is more hematogenous; thyroglobulin is most valuable after treatment. A clinically positive lateral node calls for therapeutic compartment dissection, not isolated node removal."
    ),
    "tags": ["differentiated thyroid cancer", "papillary thyroid carcinoma", "follicular thyroid carcinoma", "oncocytic thyroid carcinoma", "thyroidectomy", "radioactive iodine", "thyroglobulin"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — differentiated thyroid carcinoma, thyroidectomy, and cervical nodal disease",
        "K.J. Lee's Essential Otolaryngology, 12e — thyroid malignancy and operative management",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid cancer evaluation, surgery, and postoperative management",
        "American Thyroid Association — 2025 Management Guidelines for Adult Patients with Differentiated Thyroid Cancer (Ringel et al., Thyroid 2025;35:841-985)",
    ],
}


ACTIVE_SURVEILLANCE_V280 = {
    "recognize": (
        "Recognize active surveillance (AS) as an intentional treatment strategy for carefully selected low-risk papillary thyroid cancer—not passive delay and not the same as following an indeterminate nodule. The best-established candidates have a small, intrathyroidal papillary carcinoma (classically papillary microcarcinoma), no clinical nodal or distant metastasis, no gross extrathyroidal invasion, no aggressive histology, and no symptoms or imaging features suggesting threat to the recurrent laryngeal nerve or aerodigestive tract. Patient preference, age/comorbidity, anxiety, access to expert ultrasound, and ability to maintain long-term follow-up are part of candidacy."
    ),
    "localize": (
        "Localize the tumor in three dimensions before calling it 'low risk.' Ultrasound should define its relationship to the anterior and posterior capsule, trachea, tracheoesophageal groove/RLN course, and surrounding thyroid tissue, while surveying central and lateral cervical nodes. A tiny tumor in a dangerous posteromedial position can be a worse surveillance candidate than a slightly larger lesion surrounded by normal thyroid. Apparent extrathyroidal extension, suspicious nodes, invasive anatomy, or a location in which a few millimeters of growth could compromise the RLN/trachea should move the decision toward intervention."
    ),
    "workup": (
        "Establish that the lesion truly fits an AS pathway: correlate diagnostic cytology with high-resolution ultrasound, perform a deliberate cervical nodal survey, and review the pathology/imaging for aggressive features or discordance. Baseline documentation should make future comparison reproducible—record maximal dimensions, exact location, capsule/trachea relationship, nodal status, and thyroid function. Additional cross-sectional imaging is selective rather than routine, used when ultrasound cannot confidently exclude invasive anatomy or nodal disease. The resident should be able to explain why 'subcentimeter' alone is not an eligibility criterion."
    ),
    "manage": (
        "Manage AS with a defined surveillance program and shared decision-making. Use serial expert neck ultrasound and clinical review, with closer observation early and longer intervals after stability according to the treating program and current guideline framework. Track change in tumor dimensions/volume, new extrathyroidal extension, and especially new suspicious lymph nodes rather than reacting to trivial measurement noise. Revisit the choice over time: patients may appropriately cross over to surgery because of meaningful structural progression, new nodal disease, changing anatomy, inability to continue reliable surveillance, or patient preference/anxiety even without oncologic progression."
    ),
    "operate": (
        "Delayed surgery is not 'failure' of surveillance; it is the planned rescue pathway when surveillance triggers are met. When intervention becomes appropriate, choose the operation from the disease present at that time rather than automatically escalating to total thyroidectomy: many patients still remain lobectomy candidates if disease is confined to one lobe and nodes remain negative. New proven nodal disease requires the appropriate therapeutic compartment operation. Conversely, stable low-risk disease should not be converted to surgery merely because a cancer label feels uncomfortable if the informed patient prefers surveillance and follow-up remains reliable."
    ),
    "teach": (
        "Chief/boards framework: AS requires the right TUMOR, the right ANATOMY, and the right PATIENT/SYSTEM. TUMOR: low-risk papillary biology without nodal/distant disease. ANATOMY: no invasion and no precarious relationship to the RLN/trachea. PATIENT/SYSTEM: understands the tradeoff and can return for high-quality longitudinal ultrasound. 'Observe' therefore means measure, map, compare, and act on predefined change—not ignore. The key distinction from the parent DTC concept is that this card teaches selection and monitoring; it should not re-teach the entire thyroid-cancer treatment algorithm."
    ),
    "tags": ["active surveillance", "papillary thyroid microcarcinoma", "low-risk papillary thyroid cancer", "ultrasound", "shared decision making"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — papillary thyroid cancer and risk-adapted management",
        "K.J. Lee's Essential Otolaryngology, 12e — thyroid malignancy",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid cancer evaluation and management",
        "American Thyroid Association — 2025 Management Guidelines for Adult Patients with Differentiated Thyroid Cancer (Ringel et al., Thyroid 2025;35:841-985)",
    ],
}


def apply_thyroid_dtc_rebuild_v280(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    targets = {
        "differentiated thyroid cancer": DTC_V280,
        "differentiated thyroid cancer active surveillance": ACTIVE_SURVEILLANCE_V280,
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
        module["source_grounded_v280"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
