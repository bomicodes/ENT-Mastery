"""v29.6 — source-grounded palatal OSA Concept Hub rebuild.

Separates PALATAL SURGERY (what the reconstructive operations do, how they differ, and
how to perform them safely) from PALATAL SURGERY SELECTION FOR OSA (who should receive
a palate-directed operation and how anatomy/physiology drive procedure choice).
"""

import re

DOMAIN = "Sleep Surgery"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


SLEEP_PALATE_REBUILD_V296 = {
    "palatal surgery": {
        "recognize": (
            "Recognize PALATAL SURGERY as a family of reconstructive operations for retropalatal and lateral-pharyngeal-wall obstruction, not as a synonym for classic tissue-ablative UPPP. The operative problem is dynamic collapse of the velum and/or lateral walls during sleep. Contemporary procedures may remove selected obstructing tissue, reposition or tension the palatopharyngeus/superior constrictor complex, stabilize the lateral walls, enlarge the retropalatal airway, or combine these goals while trying to preserve normal speech and swallowing."
        ),
        "localize": (
            "Localize WHAT PART OF THE PALATE/PHARYNX the operation is designed to change. Classic UPPP enlarges the retropalatal port through tonsillar/oropharyngeal and soft-palate modification. Expansion sphincter pharyngoplasty recruits the palatopharyngeus to widen and stiffen the lateral retropalatal airway; lateral/relocation-type pharyngoplasties likewise target lateral-wall collapse; palatal advancement moves the soft-palate attachment/anterior framework forward. A patient with dominant tongue-base, epiglottic, or skeletal collapse has a different anatomic problem even if snoring seems to come from the palate."
        ),
        "workup": (
            "Before operating, know the anatomy that determines technique and complications: tonsil size, soft-palate length and redundancy, uvular morphology, palatal webbing, posterior pillar/palatopharyngeus anatomy, lateral-wall collapse, dentition, tongue position, prior tonsil/palate surgery, scar, and baseline speech/swallow function. Review the sleep study and the site-selection evaluation, but this card's operative workup is specifically about translating the chosen PALATAL target into a safe reconstructive plan. If prior surgery has distorted the palate, explicitly assess velopharyngeal competence and stenosis risk before further tissue removal."
        ),
        "manage": (
            "Match the reconstruction to the deforming force rather than defaulting to maximal resection. Large tonsils can be an important component of a palate-level operation; lateral-wall collapse favors a reconstructive pharyngoplasty strategy; excessive palatal tissue may require selective modification. Counsel that palate surgery usually IMPROVES rather than guarantees normalization of OSA and that residual multilevel obstruction may still require PAP, oral appliance therapy, weight management, or additional site-directed treatment. Discuss bleeding, severe postoperative pain, dehydration, transient dysphagia, globus/taste or voice change, velopharyngeal insufficiency, nasopharyngeal/oropharyngeal stenosis, and persistent OSA."
        ),
        "operate": (
            "Operate with FUNCTION-PRESERVING reconstruction as the endpoint. Protect palatal mucosa and avoid unnecessary circumferential denudation; preserve enough soft-palate length and neuromuscular function for velopharyngeal closure; control tonsillar-fossa bleeding meticulously; place suspension/repositioning sutures to widen the intended vector without creating excessive tension or asymmetric distortion. In expansion/lateral-wall techniques, understand the palatopharyngeus and superior-constrictor relationship and make the intended lateralizing vector reproducible. The endpoint is a stable, enlarged retropalatal airway without trading OSA for dysphagia, VPI, or scar stenosis."
        ),
        "teach": (
            "Chief/boards distinction: PALATAL SURGERY = PROCEDURE MECHANICS. Know what UPPP removes/repositions, what expansion or lateral pharyngoplasty is trying to stabilize, and which complications arise from excessive resection or scar. Do not teach every palate operation as 'cutting off the uvula.' Contemporary palate surgery is often reconstructive. Also do not claim that a technically successful palate operation cures multilevel OSA; postoperative objective reassessment remains important when symptoms or disease severity warrant it."
        ),
        "tags": [
            "palatal surgery", "UPPP", "uvulopalatopharyngoplasty", "expansion sphincter pharyngoplasty",
            "lateral pharyngoplasty", "relocation pharyngoplasty", "palatal advancement", "lateral pharyngeal wall",
            "velopharyngeal insufficiency", "pharyngeal stenosis"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — adult OSA surgery, palatal obstruction, UPPP, reconstructive pharyngoplasty, and complications",
            "K.J. Lee's Essential Otolaryngology, 12e — obstructive sleep apnea surgery and palate-level procedures",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — sleep surgery anatomy, UPPP/pharyngoplasty, and operative pearls",
            "AAO-HNS Position Statement: Uvulopalatopharyngoplasty (revised 2019) — UPPP and reconstructive palatal variants as accepted treatments in appropriately selected OSA patients",
            "AAO-HNS Position Statement: Surgical Management of Obstructive Sleep Apnea — palate surgery as one component of comprehensive site-directed OSA surgery",
        ],
    },
    "palatal surgery selection for osa": {
        "recognize": (
            "Recognize PALATAL SURGERY SELECTION as a CANDIDACY + PHENOTYPING problem. The question is not 'does this patient have OSA?' but whether clinically important OSA persists despite or in place of acceptable nonoperative therapy AND whether the palate/lateral pharyngeal wall is a meaningful obstructive site that a palate-directed procedure can improve. Separate a patient seeking surgery because PAP is intolerable from one who has never received an adequate treatment discussion, and separate obvious tonsillopalatal crowding from multilevel or predominantly hypopharyngeal collapse."
        ),
        "localize": (
            "Phenotype the obstruction using awake examination plus sleep-state information when it will change management. Record tonsil size, modified Mallampati/tongue position, palate position/length, BMI and craniofacial pattern; Friedman-style staging helps frame expected response to isolated palate surgery but is not a substitute for individualized anatomy. Drug-induced sleep endoscopy can refine the collapse pattern—velum versus oropharyngeal lateral wall versus tongue base versus epiglottis, and anteroposterior versus concentric behavior—especially when the awake examination does not explain disease or multilevel surgery is being considered."
        ),
        "workup": (
            "Confirm OSA objectively and understand severity, oxygen burden, symptoms, prior therapy, and goals before selecting surgery. Review PAP efficacy and why it failed or is unacceptable, oral-appliance candidacy/use when relevant, weight trajectory, cardiopulmonary comorbidity, sedative/alcohol contributors, nasal obstruction, dentition and skeletal anatomy. Then ask a site-specific question: is there enough PALATAL/lateral-wall obstruction to justify palate surgery, and is disease likely to remain elsewhere if the palate is corrected? Do not select UPPP from AHI alone."
        ),
        "manage": (
            "Choose among continued PAP optimization, oral appliance, weight-directed therapy, palate surgery, other site-directed surgery, or a multilevel strategy according to patient goals and anatomy. Favor palate-directed surgery when the palate/tonsillar-lateral-wall compartment is a major obstructive site and the patient is an appropriate surgical candidate; avoid presenting isolated palate surgery as the definitive answer when dominant tongue-base, epiglottic, or major skeletal obstruction remains. Large tonsils and favorable palatal anatomy generally improve the logic for tonsillopalatal surgery; obesity and multilevel collapse reduce confidence in an isolated-palate cure and should shape counseling rather than function as simplistic binary exclusions."
        ),
        "operate": (
            "Translate the phenotype into the least-burdensome operation that addresses the demonstrated collapse. Tonsillar hypertrophy plus retropalatal narrowing may support tonsillectomy with palate reconstruction; prominent lateral-wall collapse may favor an expansion/lateralizing pharyngoplasty rather than purely central tissue resection; multilevel collapse may require staged or combined treatment. DISE findings should inform—not mechanically dictate—the operation, because collapse patterns, awake anatomy, comorbidities, prior surgery, surgeon expertise, and patient priorities all matter. Plan postoperative monitoring according to OSA severity, comorbidity, opioid sensitivity, airway risk, and procedure extent."
        ),
        "teach": (
            "Chief/boards distinction: PALATAL SURGERY SELECTION = WHO + WHY + WHICH SITE. Confirm disease, understand failure/preferences for nonoperative therapy, phenotype the airway, predict whether the palate is a meaningful bottleneck, and counsel expected residual disease. Friedman staging and DISE are selection tools, not magic success scores. A favorable palate does not erase tongue-base disease, and an unfavorable global phenotype does not mean palate surgery can never provide meaningful benefit. The correct endpoint is a goal-concordant, anatomy-directed OSA plan—not merely a lower AHI after an indiscriminate UPPP."
        ),
        "tags": [
            "OSA surgical selection", "palatal surgery selection", "Friedman staging", "DISE", "drug-induced sleep endoscopy",
            "tonsil size", "lateral wall collapse", "multilevel OSA", "PAP intolerance", "site-directed sleep surgery"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — adult OSA evaluation, surgical phenotyping, palate-level obstruction, and multilevel surgery",
            "K.J. Lee's Essential Otolaryngology, 12e — OSA examination, surgical candidacy, and palate surgery selection",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — OSA workup, Friedman staging, DISE, and surgical selection pearls",
            "American Academy of Sleep Medicine clinical practice guideline on referral of adults with OSA for surgical consultation (J Clin Sleep Med 2021) — shared decision-making around surgical referral when PAP is not acceptable or adequately usable",
            "AAO-HNS Position Statement: Uvulopalatopharyngoplasty (revised 2019) — UPPP/palatal variants in appropriately selected patients and expectation of improvement rather than universal AHI normalization",
            "AAO-HNS Position Statement: Treatment of Obstructive Sleep Apnea (2021) — individualized use of medical, device, and surgical therapies",
        ],
    },
}


def apply_sleep_palate_rebuild_v296(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = SLEEP_PALATE_REBUILD_V296.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v296"] = True
        module["semantic_role_v296"] = (
            "palatal reconstructive procedure mechanics and complication avoidance"
            if key == "palatal surgery"
            else "OSA candidacy, airway phenotyping, and selection of palate-directed surgery"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
