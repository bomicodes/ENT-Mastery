"""v39.3 -- Thyroid / Parathyroid / Salivary depth repair (content-staleness sweep, batch 4/9).

Same two defects as v39.0-v39.2. See thyroglossal_duct_cyst_depth_v389 for
the pattern and rationale.
"""

DOMAIN = "Thyroid / Parathyroid / Salivary"

DEPTH_V393 = {
    "Reoperative Thyroid Surgery": {
        "recognize": (
            "Reoperative need is recognized when recurrent/persistent thyroid disease, a completion "
            "thyroidectomy for cancer found after lobectomy, or recurrent hyperparathyroidism requires "
            "reentry into a previously dissected central or lateral neck, where normal fascial planes "
            "no longer exist and scar tissue obscures the recurrent laryngeal nerve (RLN) and "
            "parathyroid glands."
        ),
        "localize": (
            "Scarring most affects the same planes the first operation traversed -- the RLN course "
            "medial to the thyroid bed and near the ligament of Berry, and the parathyroid glands, "
            "which may have been displaced, devascularized, or auto-transplanted at the index "
            "operation -- so the operative target (which lobe, which specific gland, or the entire "
            "field for recurrent cancer) must be defined precisely before reentry rather than "
            "planned as a general re-exploration."
        ),
        "operate": (
            "Indication: recurrent/persistent thyroid cancer, contralateral nodule requiring "
            "completion thyroidectomy, or recurrent/persistent hyperparathyroidism after a prior "
            "neck operation, where the expected oncologic or biochemical benefit justifies materially "
            "higher morbidity than a first-time operation. Setup: obtain the prior operative note, "
            "review preoperative imaging (ultrasound, 4D-CT, or sestamibi as indicated) and, when "
            "available, laryngoscopy to document baseline vocal fold function before reoperating. Key "
            "steps: consider approaching the RLN from an unscarred plane (e.g., a lateral or "
            "posterior approach entering fresh tissue rather than dissecting directly through the "
            "prior bed) when feasible, use nerve monitoring, and identify the nerve at a reliable "
            "extralaryngeal landmark before working toward the area of concern. Danger structures: "
            "the RLN, external branch of the superior laryngeal nerve, and remaining parathyroid "
            "tissue are all at higher risk than in a virgin neck because scar has destroyed the "
            "normal tissue planes that protect them. Failure mode: relying on intraoperative "
            "exploration to 'find' the target rather than having precise preoperative localization -- "
            "reoperative surgery rewards imaging and planning far more than it rewards confident "
            "intraoperative searching. Postoperative plan: postoperative laryngoscopy if voice change "
            "is present, calcium monitoring given the added risk to remaining parathyroid tissue, and "
            "close follow-up given the higher complication rate of reoperative neck surgery."
        ),
    },
    "Four-Gland Parathyroid Exploration": {
        "recognize": (
            "Bilateral four-gland exploration is used when multigland parathyroid disease is "
            "suspected (hereditary syndromes, lithium-associated disease, or discordant/negative "
            "localization studies in primary hyperparathyroidism) or when a focused approach fails "
            "intraoperatively; it is a systematic search based on embryologic gland position, not an "
            "open-ended hunt."
        ),
        "localize": (
            "Superior parathyroid glands (fourth pharyngeal pouch origin) are typically found "
            "posterior to the recurrent laryngeal nerve, near the cricothyroid junction; inferior "
            "glands (third pharyngeal pouch, migrating with the thymus) are more variable, usually "
            "near the lower pole or within the thyrothymic tract, but can descend into the "
            "mediastinum with the thymus or, less often, fail to descend and sit near the carotid "
            "bifurcation; a 'missing' gland is sought along its embryologic migration path, not at "
            "random."
        ),
        "operate": (
            "Indication: multigland disease (or suspicion of it) where a single-gland focused "
            "approach is inappropriate or has already failed. Setup: know prior localization imaging "
            "but do not let it substitute for systematic bilateral exploration once multigland "
            "disease is confirmed intraoperatively or suspected preoperatively. Key steps: identify "
            "all four glands (or account for a missing one via its known embryologic pathway) before "
            "deciding on resection strategy, assess each gland's size/appearance for hyperfunction, "
            "and choose subtotal parathyroidectomy (leaving a well-vascularized remnant, often "
            "marked with a clip) or total parathyroidectomy with autotransplantation depending on the "
            "underlying disease, surgeon preference, and the risk of graft-dependent persistent "
            "disease; MEN1 may be managed by subtotal parathyroidectomy or total removal with "
            "autotransplantation rather than one universal preferred approach. Danger structures: the RLN, which must be identified early and protected "
            "throughout a bilateral dissection, and the vascular pedicle of each gland, since rough "
            "handling devascularizes glands you intend to preserve. Failure mode: stopping after "
            "finding an abnormal-appearing gland without confirming the status of the remaining three, "
            "or failing to search the thymus/retroesophageal space for a missing inferior or superior "
            "gland respectively. Postoperative plan: intraoperative or early postoperative PTH "
            "trending to confirm adequate resection, and calcium monitoring/supplementation given the "
            "higher hypoparathyroidism risk with more extensive gland removal."
        ),
    },
    "Submandibular Gland Excision": {
        "recognize": (
            "Indicated for a submandibular gland or duct tumor (benign or malignant), or for "
            "chronic/recurrent obstructive sialadenitis (sialolithiasis) or inflammatory disease "
            "refractory to conservative and duct-preserving (sialendoscopic) management."
        ),
        "localize": (
            "The gland sits within the submandibular triangle, wrapped around the posterior free "
            "border of the mylohyoid muscle, with three nerve relationships that must be planned "
            "before incision: the marginal mandibular branch of the facial nerve crossing superficial "
            "to the gland (at risk from a low-placed incision or retraction), the lingual nerve "
            "looping under the submandibular duct deep to the gland, and the hypoglossal nerve "
            "running deep and inferior to the digastric tendon."
        ),
        "operate": (
            "Indication: tumor of the gland/duct or refractory obstructive/inflammatory disease not "
            "resolved by sialendoscopy or duct surgery. Setup: preoperative imaging to define tumor "
            "extent or stone burden and counsel the patient specifically on marginal mandibular, "
            "lingual, and hypoglossal nerve risk. Key steps: incision placed at least 2 fingerbreadths "
            "below the mandibular border (or in a natural skin crease) to protect the marginal "
            "mandibular nerve, identify and preserve the facial artery and vein, retract the "
            "mylohyoid to expose the lingual and hypoglossal nerves, doubly ligate the submandibular "
            "duct while protecting the lingual nerve looping beneath it, and remove the gland from "
            "its bed. Danger structures: the three nerves above plus the facial artery, which crosses "
            "the gland twice (posteriorly and again as it emerges over the mandible). Failure mode: "
            "not mentally rehearsing all three nerve relationships before incision, leading to "
            "inadvertent marginal mandibular nerve injury (asymmetric lower lip weakness) from "
            "retraction alone, without ever transecting the nerve. Postoperative plan: monitor for "
            "hematoma (can compromise the airway in the floor of mouth/neck), assess lip and tongue "
            "function, and manage a drain if placed."
        ),
    },
    "Indeterminate Thyroid Cytology / Molecular Testing": {
        "recognize": (
            "Bethesda III (AUS/FLUS) and IV (follicular/Hurthle cell neoplasm) categories express a "
            "risk of malignancy (2023 Bethesda adult estimates: III mean 22%, range 13-30%; IV "
            "mean 30%, range 23-34%; local prevalence and NIFTP classification affect risk), "
            "not a diagnosis of cancer or benignity -- an indeterminate result means cytology alone "
            "cannot resolve the nodule and additional risk stratification is needed before deciding "
            "on surgery."
        ),
        "localize": (
            "Risk is reassessed by integrating multiple inputs at the nodule level: sonographic "
            "pattern (e.g., ACR TI-RADS features), nodule size, repeat cytology when appropriate, "
            "patient-level clinical risk factors (radiation history, family history), and, when used, "
            "a molecular test's own performance characteristics (sensitivity/NPV for ruling out "
            "cancer, or specificity/PPV for ruling it in) rather than treating the molecular result "
            "as a stand-alone answer."
        ),
        "operate": (
            "Indication: indeterminate cytology prompts shared risk assessment, not automatic molecular testing "
            "or surgery; options include repeat FNA (particularly Bethesda III), molecular testing when "
            "its result would change care, ultrasound surveillance in selected low-risk nodules, "
            "or diagnostic lobectomy. The choice of an upfront "
            "definitive (near-total/total) thyroidectomy depends on how the combined risk picture, "
            "including any molecular result, would change management. Setup/key steps: before "
            "ordering a molecular test, define explicitly what each possible result will change -- a "
            "high-NPV 'benign-favoring' result may support surveillance, while a mutation-positive "
            "result suggesting malignancy (or a specific alteration associated with more aggressive "
            "behavior) may justify total rather than partial thyroidectomy as the index operation, "
            "avoiding a second surgery. Failure mode: ordering a molecular panel reflexively without "
            "a predetermined action for each result, which adds cost and delay without changing "
            "management, or over-relying on a single test's result in isolation from the sonographic "
            "and clinical risk picture. Postoperative plan (when surgery is chosen): final pathology "
            "determines whether a completion thyroidectomy is needed after diagnostic lobectomy, and "
            "surveillance patients need a defined ultrasound follow-up interval rather than indefinite "
            "observation without a plan."
        ),
    },
    "MEN2 / RET": {
        "recognize": (
            "Multiple endocrine neoplasia type 2 (MEN2A and MEN2B) is caused by germline RET "
            "proto-oncogene mutations and links medullary thyroid carcinoma (MTC, essentially "
            "penetrant in all subtypes) with pheochromocytoma and, in MEN2A, primary "
            "hyperparathyroidism; the specific RET codon mutated predicts both disease aggressiveness "
            "and the age by which prophylactic thyroidectomy should occur."
        ),
        "localize": (
            "Genotype-phenotype correlation localizes risk: highest-risk mutations (e.g., codon M918T, "
            "classically MEN2B) drive very early, aggressive MTC and warrant thyroidectomy in infancy; "
            "high- and moderate-risk mutations allow thyroidectomy in early-to-mid childhood or when "
            "calcitonin/imaging suggests disease, respectively; pheochromocytoma, when present, "
            "arises from the adrenal medulla and must be localized and addressed before any thyroid "
            "or unrelated surgery is undertaken."
        ),
        "operate": (
            "Indication: confirmed pathogenic RET mutation drives prophylactic (or therapeutic, if "
            "calcitonin/imaging already shows MTC) thyroidectomy, timed by mutation-specific risk "
            "category rather than a fixed age for all patients. Setup: before any thyroid "
            "intervention, biochemically screen for and rule out pheochromocytoma (plasma or urine "
            "metanephrines); an unrecognized pheochromocytoma can precipitate a hypertensive crisis "
            "under anesthesia for an unrelated procedure. Key steps: total thyroidectomy (given the "
            "field-defect, multifocal nature of hereditary MTC); tailor central compartment surgery "
            "to calcitonin, ultrasound, age, RET risk and whether this is prophylactic versus "
            "clinically established MTC, avoiding a blanket dissection rule; screen for "
            "hyperparathyroidism in MEN2A. Danger structures: the RLN and parathyroid glands, as in "
            "any thyroidectomy, with added complexity in very young children. Failure mode: proceeding "
            "with thyroid (or any) surgery before excluding pheochromocytoma -- an unaddressed "
            "catecholamine-secreting tumor is an anesthetic emergency waiting to happen, which is why "
            "'pheochromocytoma before thyroid surgery' is the standing rule. Postoperative plan: "
            "lifelong calcitonin and CEA surveillance for recurrent MTC, calcium monitoring, and "
            "coordinated genetic counseling/cascade testing for at-risk family members."
        ),
    },
    "Parathyroid Carcinoma": {
        "recognize": (
            "Suspect parathyroid carcinoma with markedly elevated calcium and PTH (often several-fold "
            "above typical primary hyperparathyroidism), a palpable neck mass, vocal fold palsy, or a "
            "firm gland found densely adherent to surrounding tissue at surgery; it is rare and often "
            "not diagnosed with certainty until the resected specimen shows capsular or vascular "
            "invasion."
        ),
        "localize": (
            "Local invasion, when present, typically involves the ipsilateral thyroid lobe, strap "
            "muscles, recurrent laryngeal nerve, or trachea/esophagus; because capsule violation risks "
            "tumor seeding along the dissection plane, minimizing intraoperative capsule disruption "
            "(rather than more extensive dissection after suspicion is raised) is the key localization "
            "principle -- avoid, don't chase."
        ),
        "operate": (
            "Indication: biochemical and clinical findings suspicious for parathyroid carcinoma "
            "warrant en-bloc resection at the index operation rather than a standard focused "
            "parathyroidectomy; fine-needle aspiration of a suspected parathyroid carcinoma should be "
            "avoided given seeding risk and its limited diagnostic yield. Setup: confirm the "
            "biochemical picture and obtain localization/staging imaging preoperatively; approach the "
            "case as a potential cancer operation from the outset if intraoperative findings (dense "
            "adherence, invasion) or preoperative suspicion are high. Key steps: en-bloc resection of "
            "the gland with the ipsilateral thyroid lobe and any grossly involved structures, avoiding "
            "capsule rupture or piecemeal removal, plus resection of clinically involved lymph nodes; "
            "the extent of resection is guided by what is invaded, not a fixed template. Danger "
            "structures: the RLN, which may need to be sacrificed if truly invaded (rather than "
            "preserved at the cost of incomplete resection), and the trachea/esophagus if adherent. "
            "Failure mode: performing a standard, capsule-violating parathyroidectomy when carcinoma "
            "is suspected -- the first operation is the best and often only chance for complete "
            "oncologic resection, since local recurrence after an incomplete first operation is "
            "difficult to salvage. Postoperative plan: calcium monitoring, and for recurrent or "
            "metastatic disease, multidisciplinary management focused on controlling both tumor "
            "burden and severe hypercalcemia, which is often the more immediately life-threatening "
            "problem."
        ),
    },
}


def apply_depth_content_thyroid_parathyroid_v393(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in DEPTH_V393 if t not in modules]
    if missing:
        raise RuntimeError(f"v39.3: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in DEPTH_V393.items():
        modules[topic].update(fields)
    return {"enriched": list(DEPTH_V393.keys())}
