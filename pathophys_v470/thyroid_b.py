"""Thyroid / Parathyroid / Salivary (part B): mechanism-level teaching content."""

CONTENT = {
"Reoperative Hyperparathyroidism": dict(
overview=(
"Reoperative parathyroid surgery treats persistent (within 6 months) or recurrent (after 6 months) hyperparathyroidism after a failed first operation. "
"Success depends on confirming the diagnosis, precise localization, and knowing where missed glands hide."),
physiology=(
"**Embryologic migration**: inferior glands descend with the thymus from the third pouch and can stop anywhere from the angle of the mandible to the mediastinum; superior glands from the fourth pouch are more constant but can slide into the tracheoesophageal groove or retroesophageal space. "
"**Gland number**: most people have four glands, but a minority have supernumerary glands, often in the thymus. "
"**Feedback**: normal glands are suppressed by hypercalcemia, so in persistent disease the remaining hyperfunctioning tissue is the source of PTH. "
"**PTH kinetics**: intact PTH has a half-life of a few minutes, allowing intraoperative confirmation."),
pathophysiology=(
"**Why first operations fail**: a missed ectopic adenoma, unrecognized multigland disease, a supernumerary gland, or parathyromatosis from capsular rupture. "
"**Confirm the diagnosis first**: exclude familial hypocalciuric hypercalcemia and secondary causes such as vitamin D deficiency before reoperating. "
"**Precise localization**: ideally concordant studies (sestamibi SPECT-CT, 4D-CT, ultrasound, or venous sampling) are obtained because scar defeats blind exploration. "
"**Scar risk**: reoperation raises the risk of RLN injury and permanent hypoparathyroidism, so cryopreservation of removed tissue is considered."),
),

"Hungry Bone / Post-Thyroid Calcium Management": dict(
overview=(
"Post-thyroidectomy hypocalcemia usually reflects transient parathyroid dysfunction, whereas hungry bone syndrome is severe, prolonged hypocalcemia after parathyroidectomy as demineralized bone avidly takes up calcium. "
"Anticipating, monitoring, and treating hypocalcemia prevents tetany and arrhythmia."),
physiology=(
"**PTH maintains calcium**: by stimulating bone resorption, renal calcium reabsorption, and calcitriol synthesis. "
"**Bone as a reservoir**: bone holds 99 percent of body calcium and exchanges it with blood under PTH control. "
"**Parathyroid blood supply**: delicate branches mainly from the inferior thyroid artery, easily injured during thyroidectomy. "
"**Neuromuscular excitability**: low ionized calcium lowers the threshold for nerve and muscle depolarization."),
pathophysiology=(
"**Post-thyroidectomy hypocalcemia**: devascularization, bruising, or removal of parathyroid glands causes a sudden PTH drop; a low postoperative PTH predicts symptomatic hypocalcemia. "
"**Hungry bone syndrome**: after removing a long-standing PTH source, osteoblastic activity outpaces resorption, so bone deposits calcium, phosphate, and magnesium rapidly. "
"**Risk factors**: large adenomas, high preoperative PTH and alkaline phosphatase, and severe bone disease. "
"**Symptoms**: perioral tingling, paresthesias, Chvostek and Trousseau signs, tetany, laryngospasm, seizures, and QT prolongation. "
"**Magnesium matters**: hypomagnesemia impairs PTH secretion and action, so it must be corrected. "
"**Treatment logic**: calcium replaces the deficit and calcitriol bypasses the missing PTH-driven renal activation."),
),

"Pleomorphic Adenoma / Warthin Tumor": dict(
overview=(
"Pleomorphic adenoma is the most common salivary tumor, usually in the parotid tail; Warthin tumor is the second most common, often bilateral or multifocal in older smokers. "
"Both are benign and treated by parotidectomy with facial nerve preservation, but pleomorphic adenoma recurs if enucleated and can become malignant."),
physiology=(
"**Parotid structure**: a serous gland divided by the facial nerve into superficial and deep lobes, enclosed in the parotid fascia. "
"**Intraparotid lymph nodes**: the parotid develops late and encapsulates lymph nodes, unlike other salivary glands. "
"**Cell lineages**: ductal epithelium and myoepithelial cells interact to form glandular structures."),
pathophysiology=(
"**Pleomorphic adenoma**: a mixed tumor of epithelial and myoepithelial cells in chondromyxoid stroma, driven by PLAG1 or HMGA2 rearrangements. "
"**Pseudopods and incomplete capsule**: tumor projections extend through a thin capsule, which is why enucleation leaves tumor behind and recurrence is multinodular. "
"**Malignant transformation**: risk rises with duration (carcinoma ex pleomorphic adenoma). "
"**Warthin tumor**: oncocytic epithelium with lymphoid stroma arising from salivary tissue trapped in intraparotid nodes; strongly associated with smoking; hot on technetium scans because oncocytes concentrate pertechnetate. "
"**Surgery**: superficial or partial parotidectomy with a cuff of normal tissue and facial nerve dissection."),
),

"Acute Sialadenitis / Sjögren": dict(
overview=(
"Acute suppurative sialadenitis is bacterial infection of a salivary gland, typically the parotid in dehydrated or postoperative patients. "
"Sjögren syndrome is autoimmune exocrinopathy causing dry eyes and mouth, gland swelling, and a higher risk of MALT lymphoma."),
physiology=(
"**Salivary flow is protective**: continuous flow flushes ducts and contains antimicrobial proteins (lysozyme, lactoferrin, IgA). "
"**Parotid saliva**: serous and less bacteriostatic than mucinous saliva, making the parotid more prone to suppurative infection. "
"**Glandular immune tolerance**: salivary epithelium normally avoids autoimmune attack."),
pathophysiology=(
"**Acute suppurative parotitis**: dehydration, anticholinergics, and poor oral hygiene reduce flow, allowing retrograde ascent of S. aureus and oral flora through Stensen duct. "
"**Pus at the duct**: massage expresses purulent saliva from the papilla. "
"**Abscess**: the fibrous parotid fascia limits expansion, making it painful; abscesses may need drainage. "
"**Sjögren mechanism**: lymphocytic infiltration (focal sialadenitis) and autoantibodies (anti-Ro/SSA, anti-La/SSB) destroy acinar function. "
"**Lymphoma risk**: chronic B-cell stimulation raises MALT lymphoma risk, so persistent or asymmetric gland enlargement warrants biopsy."),
),

"Ranula": dict(
overview=(
"A ranula is a mucus extravasation pseudocyst from the sublingual gland, presenting as a floor-of-mouth swelling (simple) or neck mass (plunging). "
"Definitive treatment is excision of the sublingual gland."),
physiology=(
"**Sublingual gland**: lies in the floor of mouth above the mylohyoid, secreting continuously through multiple small ducts of Rivinus or a common Bartholin duct. "
"**Continuous mucous secretion**: unlike the submandibular gland, it secretes even without stimulation. "
"**Mylohyoid muscle**: forms the floor of mouth diaphragm, sometimes with natural dehiscences."),
pathophysiology=(
"**Extravasation**: duct injury lets mucus leak into surrounding tissue, forming a pseudocyst without an epithelial lining. "
"**Plunging ranula**: mucus passes through or around the mylohyoid into the submandibular space, presenting as a soft neck mass. "
"**Why marsupialization fails**: the gland keeps secreting, so recurrence is common unless the sublingual gland is removed. "
"**Submandibular gland innocent**: the source is almost always the sublingual gland."),
),

"Thyroid Eye Disease / Graves Ophthalmopathy": dict(
overview=(
"Thyroid eye disease is autoimmune orbital inflammation, usually with Graves disease, causing proptosis, lid retraction, diplopia, and in severe cases optic neuropathy. "
"It has an active inflammatory phase then a stable fibrotic phase, and teprotumumab, steroids, radiation, and decompression surgery are matched to phase and severity."),
physiology=(
"**Orbital compartments**: the bony orbit contains extraocular muscles, fat, the optic nerve, and vessels in a fixed volume open only anteriorly. "
"**Orbital fibroblasts**: express TSH receptor and IGF-1 receptor. "
"**Glycosaminoglycans**: hydrophilic molecules that retain water when produced in excess."),
pathophysiology=(
"**Shared antigen**: TSH receptor antibodies activate orbital fibroblasts through TSH receptor and IGF-1 receptor signaling. "
"**Tissue expansion**: fibroblasts produce glycosaminoglycans, causing edema, muscle enlargement (inferior and medial rectus first), and adipogenesis. "
"**Proptosis**: fixed bony walls force expanded tissue forward. "
"**Optic neuropathy**: apical crowding compresses the optic nerve, causing vision loss, an emergency. "
"**Smoking**: worsens disease and treatment response; RAI can worsen it unless covered with steroids. "
"**Teprotumumab**: IGF-1 receptor antibody that reduces proptosis and inflammation in active disease. "
"**Decompression**: removes orbital walls to expand space, relieving optic nerve compression."),
),

"First-Bite Syndrome": dict(
overview=(
"First-bite syndrome is severe parotid-region pain with the first bites of each meal after surgery involving the parapharyngeal space or deep parotid. "
"It reflects loss of sympathetic innervation to the parotid."),
physiology=(
"**Dual autonomic control**: parasympathetic fibers (via otic ganglion and auriculotemporal nerve) drive watery secretion; sympathetic fibers (from the superior cervical ganglion along the external carotid) modulate secretion and myoepithelial contraction. "
"**Myoepithelial cells**: contract to squeeze saliva from acini. "
"**Sympathetic chain**: lies in the poststyloid parapharyngeal space."),
pathophysiology=(
"**Sympathetic denervation**: surgery damages sympathetic fibers. "
"**Denervation hypersensitivity**: myoepithelial cells upregulate receptors and respond excessively to parasympathetic neurotransmitters. "
"**Pain with first bites**: intense myoepithelial contraction at the start of a meal, improving with continued eating. "
"**Treatment**: botulinum toxin to the parotid reduces contraction."),
),

"Frey Syndrome": dict(
overview=(
"Frey syndrome (gustatory sweating) is sweating and flushing of the cheek skin with eating after parotidectomy. "
"It results from aberrant regeneration of parasympathetic fibers to sweat glands."),
physiology=(
"**Parasympathetic secretomotor fibers**: from CN IX via the otic ganglion and auriculotemporal nerve to the parotid. "
"**Sympathetic cholinergic fibers**: supply facial sweat glands, which use acetylcholine. "
"**Shared transmitter**: both systems use acetylcholine at the target."),
pathophysiology=(
"**Aberrant regeneration**: severed parasympathetic fibers regrow into skin sweat glands and vessels deprived of their sympathetic supply. "
"**Gustatory sweating**: meals activate parasympathetic fibers, causing sweating and flushing. "
"**Minor starch-iodine test**: confirms it. "
"**Prevention**: interposing a barrier (SMAS flap, fat, or acellular dermis) blocks regrowth. "
"**Treatment**: botulinum toxin injection."),
),

"Recurrent Laryngeal Nerve Injury During Thyroidectomy": dict(
overview=(
"RLN injury during thyroidectomy causes unilateral vocal fold paralysis (hoarseness, aspiration) or bilateral paralysis (stridor, airway emergency). "
"Visual identification, knowledge of variants, and neuromonitoring reduce injury."),
physiology=(
"**Course**: the right RLN loops around the subclavian artery and ascends obliquely; the left loops around the aortic arch and ascends in the tracheoesophageal groove. "
"**Entry**: both enter the larynx under the inferior constrictor near the cricothyroid joint, close to Berry ligament. "
"**Function**: supplies all intrinsic laryngeal muscles except the cricothyroid, plus sensation below the vocal folds. "
"**Variants**: a nonrecurrent right laryngeal nerve occurs with an aberrant right subclavian artery; extralaryngeal branching is common."),
pathophysiology=(
"**Mechanisms**: traction (a leading mechanism), thermal injury from energy devices, compression, clamping, ligature, and transection. "
"**Unilateral paralysis**: breathy voice and aspiration risk from glottic incompetence. "
"**Bilateral paralysis**: both folds rest near midline, causing stridor and airway obstruction, often requiring reintubation or tracheostomy. "
"**Loss of signal**: during neuromonitoring, loss of signal on the first side should prompt consideration of staging the contralateral side. "
"**Recovery**: neurapraxia recovers over weeks to months; transection needs repair (reinnervation)."),
),

"Completion Thyroidectomy": dict(
overview=(
"Completion thyroidectomy removes the remaining lobe after a lobectomy shows cancer that warrants total thyroidectomy or RAI. "
"Timing (early or after healing) balances scar against urgency."),
physiology=(
"**Thyroid remnant function**: a single lobe produces enough hormone for most patients, so lobectomy often avoids lifelong replacement. "
"**Iodine-avid tissue**: any remaining normal thyroid concentrates radioactive iodine far more than cancer cells, so a large remnant absorbs the dose meant for metastases. "
"**Thyroglobulin**: produced by both normal and malignant follicular cells; it is only a sensitive cancer marker once all normal thyroid is gone. "
"**Wound healing**: the operative bed passes through inflammation in the first days to weeks and fibrosis over the following months."),
pathophysiology=(
"**Indications**: high-risk pathology (extrathyroidal extension, vascular invasion, nodal disease, aggressive variants) that benefits from RAI or thyroglobulin surveillance. "
"**RAI requirement**: RAI needs complete thyroid removal to target residual cancer. "
"**Timing**: within days or after several months avoids peak inflammation and scarring. "
"**Contralateral RLN and parathyroids**: the remaining side's nerve and glands are at risk; preop laryngoscopy confirms ipsilateral nerve function."),
),

"Radioactive Iodine and TSH Suppression in DTC": dict(
overview=(
"Radioactive iodine (I-131) ablates remnant thyroid tissue and treats iodine-avid metastases in differentiated thyroid cancer, and TSH suppression reduces stimulation of residual cancer. "
"Both are used selectively by recurrence risk."),
physiology=(
"**Iodide uptake**: the sodium-iodide symporter concentrates iodine in follicular cells under TSH stimulation. "
"**I-131 emission**: beta particles destroy cells over a few millimeters; gamma emission allows imaging. "
"**TSH stimulation**: increases iodide uptake and thyroid cell growth."),
pathophysiology=(
"**Ablation and adjuvant therapy**: destroys remnant tissue, making thyroglobulin a better marker, and treats microscopic disease. "
"**Preparation**: elevated TSH (withdrawal or recombinant TSH) and low-iodine diet maximize uptake. "
"**TSH suppression**: levothyroxine to suppress TSH limits growth of residual cancer; the degree depends on risk. "
"**Side effects**: sialadenitis, xerostomia, nasolacrimal duct obstruction, and second malignancies. "
"**Risk-adapted use**: low-risk patients often do not need RAI."),
),

"Radioiodine-Refractory Differentiated Thyroid Cancer": dict(
overview=(
"RAI-refractory DTC no longer concentrates iodine or progresses despite it. "
"Treatment shifts to surveillance, local therapies, and kinase inhibitors for progressive disease."),
physiology=(
"**Sodium-iodide symporter (NIS)**: the basolateral transporter that concentrates iodide 20- to 40-fold in follicular cells; its expression requires TSH signaling and differentiation transcription factors (PAX8, TTF-1). "
"**Thyroid differentiation program**: the same pathway controls thyroglobulin, TPO, and the TSH receptor. "
"**MAPK pathway**: normally modulates growth; when overactive, it represses differentiation genes. "
"**Glucose metabolism**: differentiated cells rely on oxidative metabolism, whereas dedifferentiated cancer cells increase glucose uptake."),
pathophysiology=(
"**Dedifferentiation**: BRAF and TERT mutations and MAPK activation suppress NIS, causing loss of iodine uptake. "
"**FDG-avidity**: PET-avid tumors are more aggressive (flip-flop phenomenon). "
"**Kinase inhibitors**: lenvatinib and sorafenib prolong progression-free survival. "
"**Redifferentiation**: MEK or BRAF inhibitors can restore iodine uptake in some tumors. "
"**Targeted therapy**: RET, NTRK, and BRAF inhibitors for actionable alterations."),
),

"Primary Thyroid Lymphoma": dict(
overview=(
"Primary thyroid lymphoma usually arises in Hashimoto thyroiditis, presenting as a rapidly enlarging neck mass in older women. "
"MALT lymphoma may be treated with radiation alone, while diffuse large B-cell lymphoma needs chemoimmunotherapy; surgery is mainly for diagnosis."),
physiology=(
"**Normal thyroid**: contains no organized lymphoid tissue, so lymphoma there almost always reflects acquired lymphoid infiltration. "
"**Hashimoto thyroiditis**: introduces lymphocytes and germinal centers into the gland as part of chronic autoimmunity. "
"**Germinal center biology**: B cells mutate their immunoglobulin genes and proliferate rapidly, a process prone to errors such as translocations. "
"**Mucosa-associated lymphoid tissue (MALT)**: acquired lymphoid tissue in epithelial organs can give rise to marginal zone lymphomas."),
pathophysiology=(
"**Chronic antigenic stimulation**: Hashimoto inflammation drives B-cell proliferation, eventually producing clonal lymphoma. "
"**MALT vs DLBCL**: MALT lymphoma is indolent and localized; DLBCL is aggressive and may arise from MALT. "
"**Rapid enlargement**: compressive symptoms (dysphagia, dyspnea) mimic anaplastic carcinoma. "
"**Diagnosis**: core biopsy with flow cytometry. "
"**Treatment**: R-CHOP for DLBCL; radiation for localized MALT."),
),

"Familial Hyperparathyroidism and Parathyromatosis": dict(
overview=(
"Familial hyperparathyroidism (MEN1, MEN2A, HPT-JT, familial isolated hyperparathyroidism) causes multigland disease and recurrence. "
"Parathyromatosis is seeding of parathyroid tissue in the neck, usually after capsular rupture."),
physiology=(
"**Tumor suppressors and oncogenes**: menin (MEN1), RET (MEN2A), and parafibromin (CDC73) regulate parathyroid growth. "
"**Parathyroid tissue viability**: parathyroid cells survive and grow when implanted, which is the basis of autotransplantation."),
pathophysiology=(
"**Multigland disease**: germline mutations affect all glands, causing asynchronous hyperplasia. "
"**Recurrence**: remaining glands grow, so subtotal parathyroidectomy or total with autotransplant is used. "
"**MEN1**: parathyroid, pituitary, and pancreatic tumors. "
"**HPT-JT**: higher carcinoma risk. "
"**Parathyromatosis**: spilled parathyroid cells implant and grow in soft tissue, causing persistent disease."),
),

"Salivary Adenoid Cystic Carcinoma and Perineural Spread": dict(
overview=(
"Adenoid cystic carcinoma is a slow-growing, persistent salivary cancer known for perineural spread and late distant metastasis. "
"Complete resection and adjuvant radiation along nerve paths are key, and patients need long-term follow-up."),
physiology=(
"**Salivary duct units**: luminal ductal cells surrounded by myoepithelial and basal cells form the functional secretory unit. "
"**Nerve sheaths**: the perineurium and epineurium create continuous low-resistance channels running from the gland to the skull base. "
"**Key nerves**: the facial nerve traverses the parotid; V2 (palate, sinus) and V3 (submandibular, oral) carry minor and major salivary territories back to foramen rotundum and ovale. "
"**Neurotrophic signaling**: nerves release growth factors that tumor cells can exploit."),
pathophysiology=(
"**MYB-NFIB fusion**: a translocation that drives constitutive MYB transcription factor activity and proliferation. "
"**Growth patterns**: cribriform (Swiss cheese), tubular, and solid patterns; the solid pattern is more aggressive. "
"**Perineural spread**: tumor cells track along nerves, causing pain, numbness, or facial weakness, often far beyond visible margins. "
"**Skip lesions**: discontinuous nerve involvement makes negative margins unreliable, which is why adjuvant radiation covers nerve paths to the skull base. "
"**Late distant metastasis**: lung metastases can appear after 10 years and progress slowly, so follow-up is lifelong. "
"**Outcome logic**: survival is long but cure rates fall over time, reflecting persistent, indolent disease."),
),

"Subacute (de Quervain) Thyroiditis": dict(
overview=(
"Subacute granulomatous thyroiditis is a painful, likely post-viral inflammation causing transient thyrotoxicosis followed by hypothyroidism and recovery. "
"It is treated with NSAIDs, steroids, and beta-blockers, not antithyroid drugs."),
physiology=(
"**Colloid storage**: follicles store weeks of preformed thyroid hormone bound to thyroglobulin. "
"**Controlled release**: TSH stimulates endocytosis of colloid and proteolysis to release T4 and T3 at a regulated rate. "
"**Iodine uptake**: functioning follicles take up iodine under TSH stimulation, the basis of the radioactive iodine uptake scan. "
"**Capsular innervation**: the thyroid capsule is innervated, so inflammation causes neck pain radiating to the jaw and ear."),
pathophysiology=(
"**Post-viral inflammation**: a granulomatous reaction, often weeks after an upper respiratory infection, destroys follicles. "
"**Unregulated release**: ruptured follicles dump preformed hormone, causing thyrotoxicosis with suppressed TSH. "
"**Low uptake**: damaged follicles cannot trap iodine, so the RAI uptake is very low, the key difference from Graves disease. "
"**Inflammatory markers**: ESR and CRP are high and the gland is tender. "
"**Hypothyroid phase**: once stores are depleted and follicles recover, transient hypothyroidism follows before most return to normal. "
"**Treatment logic**: NSAIDs or steroids treat inflammation and beta-blockers control symptoms; antithyroid drugs are useless because no new hormone synthesis is driving the thyrotoxicosis."),
),

"Hashimoto Thyroiditis": dict(
overview=(
"Hashimoto thyroiditis is chronic autoimmune thyroiditis, the most common cause of hypothyroidism in iodine-sufficient areas. "
"It can cause goiter, and it raises the risk of thyroid lymphoma."),
physiology=(
"**Central and peripheral tolerance**: thymic deletion and regulatory T cells normally prevent immune attack on thyroid antigens such as TPO and thyroglobulin. "
"**Hormone synthesis**: TPO iodinates thyroglobulin and couples iodotyrosines to form T4 and T3. "
"**HPT axis**: falling thyroid hormone raises TSH, which stimulates thyroid growth and function. "
"**Iodine supply**: adequate iodine is required, but excess iodine can promote thyroid autoimmunity in susceptible people."),
pathophysiology=(
"**Loss of tolerance**: genetic (e.g., HLA-DR3) and environmental factors allow autoreactive T cells and B cells to target the thyroid. "
"**Autoantibodies**: anti-TPO and anti-thyroglobulin antibodies mark the disease and correlate with lymphocytic infiltration. "
"**Tissue destruction**: cytotoxic T cells and apoptosis destroy follicles, which are replaced by lymphoid follicles with germinal centers and oncocytic (H\u00fcrthle) cells. "
"**Progressive hypothyroidism**: shrinking functional mass leads first to subclinical (high TSH, normal T4) then overt hypothyroidism. "
"**Goiter**: TSH stimulation and lymphocytic infiltration enlarge the gland, often firm and lobulated. "
"**Lymphoma risk**: chronic B-cell stimulation raises the risk of primary thyroid lymphoma."),
),

"External Branch of the Superior Laryngeal Nerve Injury": dict(
overview=(
"EBSLN injury during thyroidectomy weakens the cricothyroid muscle, reducing pitch range and vocal projection. "
"It is subtle but career-changing for professional voice users."),
physiology=(
"**Course**: runs with the superior thyroid artery toward the cricothyroid muscle. "
"**Cricothyroid function**: tilts the thyroid cartilage forward, lengthening and tensing the vocal folds to raise pitch. "
"**Cernea classification**: type 1 crosses the vessels more than 1 cm above the superior pole; type 2a within 1 cm; type 2b below the superior pole."),
pathophysiology=(
"**Mechanism**: ligation or traction near the superior pole, especially Cernea type 2b. "
"**Voice effects**: reduced pitch range, vocal fatigue, and weak projection; posterior glottic rotation toward the paralyzed side is taught (Pasha) but is inconsistent, since unilateral cricothyroid action does not reliably rotate the glottis (Cummings). "
"**Prevention**: dissecting close to the thyroid capsule and ligating superior pole vessels individually. "
"**Neuromonitoring**: stimulating the EBSLN produces cricothyroid twitch."),
),
}
