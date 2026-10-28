"""Thyroid / Parathyroid / Salivary (part A): mechanism-level teaching content."""

CONTENT = {
"Thyroid Nodule": dict(
overview=(
"Thyroid nodules are found by palpation in about 5 percent of adults and by ultrasound in up to two-thirds, but only about 5-10 percent are malignant. "
"The workup (TSH, ultrasound risk stratification, selective FNA with Bethesda reporting) is designed to find the cancers without operating on the benign majority."),
physiology=(
"**Follicular architecture**: the thyroid is built of follicles, spheres of follicular cells surrounding colloid rich in thyroglobulin. "
"**Hormone synthesis**: follicular cells trap iodide via the sodium-iodide symporter, oxidize and organify it with thyroid peroxidase onto thyroglobulin, and release T4 and T3. "
"**TSH drive**: pituitary TSH stimulates follicular cell growth and hormone synthesis through the TSH receptor; T4 and T3 feed back negatively. "
"**C cells**: parafollicular cells scattered in the upper and middle lobes secrete calcitonin. "
"**Ultrasound anatomy**: normal thyroid is homogeneous and slightly hyperechoic relative to strap muscles."),
pathophysiology=(
"**Benign nodules**: focal follicular hyperplasia, colloid accumulation, and cyst formation from heterogeneous growth responses to TSH and growth factors. "
"**Autonomous (hot) nodules**: activating TSH receptor or Gs-alpha mutations make follicles produce hormone independent of TSH; a low TSH prompts scintigraphy, and hot nodules are rarely malignant. "
"**Malignant transformation**: BRAF V600E and RET/PTC rearrangements (papillary) or RAS mutations (follicular-patterned lesions) drive cancer. "
"**Ultrasound features of malignancy**: hypoechogenicity, irregular margins, taller-than-wide shape, microcalcifications (psammoma bodies), and extrathyroidal extension reflect the cellular and stromal biology of papillary carcinoma. "
"**Why cysts are reassuring**: purely cystic nodules contain colloid or degenerated fluid without solid neoplastic tissue. "
"**FNA logic**: cytology reveals nuclear features of papillary carcinoma but cannot see capsular or vascular invasion, which is why follicular lesions are indeterminate."),
),

"Differentiated Thyroid Cancer": dict(
overview=(
"Differentiated thyroid cancer (papillary and follicular, including oncocytic) is the most common endocrine cancer and usually has an excellent prognosis. "
"Treatment is risk-adapted under the 2025 ATA guideline: lobectomy for intrathyroidal cancers up to 2 cm, lobectomy or total thyroidectomy for 2-4 cm, total thyroidectomy for larger, extrathyroidal, or node-positive disease, with RAI and TSH suppression matched to a new four-tier recurrence risk (low, low-intermediate, intermediate-high, high)."),
physiology=(
"**Differentiated function**: cancer cells retain follicular functions (iodide uptake, thyroglobulin production, TSH responsiveness), which is why RAI and thyroglobulin monitoring work. "
"**Lymphatic drainage**: central compartment (level VI) first, then lateral levels III-IV and II, and superior mediastinum. "
"**Vascular spread**: follicular carcinoma reaches lung and bone through the blood rather than lymphatics."),
pathophysiology=(
"**Papillary carcinoma**: driven by MAPK activation (BRAF V600E, RET/PTC, RAS); characteristic nuclear features (grooves, pseudoinclusions, Orphan Annie nuclei) and psammoma bodies; spreads by lymphatics, so nodal metastases are common but rarely lethal. "
"**Follicular carcinoma**: RAS or PAX8-PPARG driven; diagnosis requires capsular or vascular invasion, so it cannot be diagnosed by FNA; spreads hematogenously. "
"**Oncocytic (Hürthle) carcinoma**: mitochondria-rich cells that take up iodine less avidly. "
"**Risk factors**: radiation exposure in childhood is the strongest environmental risk. "
"**Prognostic features**: age, tumor size, extrathyroidal extension, aggressive variants (tall cell, hobnail, columnar), vascular invasion, and BRAF/TERT co-mutation. "
"**TSH dependence**: TSH stimulates growth of residual cancer, which is the rationale for suppression in higher-risk disease."),
),

"Primary Hyperparathyroidism": dict(
overview=(
"Primary hyperparathyroidism is autonomous PTH overproduction, usually from a single adenoma, causing hypercalcemia with inappropriately normal or high PTH. "
"It causes bones, stones, abdominal groans, and psychiatric moans, and parathyroidectomy is curative."),
physiology=(
"**Calcium sensing**: the calcium-sensing receptor (CaSR) on chief cells detects ionized calcium and suppresses PTH release when calcium rises. "
"**PTH actions**: increases bone resorption, increases renal calcium reabsorption and phosphate excretion, and stimulates renal 1-alpha-hydroxylase to make calcitriol, which increases intestinal calcium absorption. "
"**Glands**: usually four parathyroids; superior glands (fourth pouch) lie posterior and deep to the RLN near the cricothyroid junction; inferior glands (third pouch, with thymus) are more variable and anterior to the RLN. "
"**Normal feedback**: hypercalcemia from any non-parathyroid cause suppresses PTH."),
pathophysiology=(
"**Single adenoma (about 85 percent)**: clonal expansion (cyclin D1/PRAD1 or MEN1 mutations) shifts the calcium set point so PTH is secreted despite high calcium. "
"**Multigland hyperplasia (about 10-15 percent)**: more common in MEN syndromes and lithium therapy. "
"**Carcinoma (under 1 percent)**: very high calcium and PTH, palpable mass, CDC73 mutations. "
"**Biochemical signature**: high calcium with nonsuppressed PTH; low phosphate; high urinary calcium (unlike familial hypocalciuric hypercalcemia, where a CaSR mutation raises the set point and urine calcium is low). "
"**End-organ effects**: bone loss (cortical, distal radius), nephrolithiasis and nephrocalcinosis, neuropsychiatric symptoms, and fatigue. "
"**Surgical cure**: removing the autonomous gland restores normal feedback; intraoperative PTH (half-life about 3-5 minutes) confirms removal."),
),

"Salivary Gland Malignancy": dict(
overview=(
"Salivary gland malignancies are a diverse group (mucoepidermoid, adenoid cystic, acinic cell, salivary duct carcinoma, carcinoma ex pleomorphic adenoma, and others). "
"The smaller the gland, the higher the chance a tumor is malignant, and grade drives treatment and prognosis."),
physiology=(
"**Salivary unit**: acini (serous, mucous, or mixed) drain through intercalated, striated, and excretory ducts. "
"**Cell types**: acinar, ductal, myoepithelial, and basal cells, each giving rise to distinct tumors. "
"**Glands**: parotid (serous), submandibular (mixed), sublingual and minor glands (mucous). "
"**Facial nerve**: divides the parotid into superficial and deep lobes. "
"**Saliva production**: parasympathetic stimulation (CN IX via otic ganglion for parotid; CN VII via chorda tympani and submandibular ganglion for submandibular and sublingual) drives secretion."),
pathophysiology=(
"**Gland size rule**: about 15-25 percent of parotid tumors, about 40-50 percent of submandibular, about half or more of minor salivary, and most sublingual tumors are malignant (series vary). "
"**Mucoepidermoid carcinoma**: most common malignancy; mucous, epidermoid, and intermediate cells; MAML2 fusions; grade determines behavior. "
"**Adenoid cystic carcinoma**: MYB-NFIB fusion; perineural spread and late lung metastasis. "
"**Carcinoma ex pleomorphic adenoma**: malignant transformation of a long-standing benign tumor. "
"**Salivary duct carcinoma**: aggressive, androgen receptor and HER2 positive, offering targeted therapy. "
"**Signs of malignancy**: rapid growth, pain, facial nerve weakness, skin fixation, and nodal disease. "
"**Staging (AJCC Version 9)**: now covers minor salivary glands, counts involved nodes instead of laterality (N1 1-3 nodes, N2 more than 3 or any ENE; N3 eliminated), and reserves stage IV for distant metastasis; histologic grade still guides treatment intensity."),
),

"Medullary Thyroid Cancer": dict(
overview=(
"Medullary thyroid cancer arises from calcitonin-secreting C cells; about 25 percent is hereditary through RET mutations (MEN2). "
"It does not take up iodine, so surgery is the primary curative treatment, and calcitonin and CEA are tumor markers."),
physiology=(
"**C cells**: neural crest-derived parafollicular cells concentrated in the upper two-thirds of the lobes. "
"**Calcitonin**: lowers blood calcium by inhibiting osteoclasts, though its role in adult calcium homeostasis is minor. "
"**RET proto-oncogene**: a receptor tyrosine kinase guiding neural crest development."),
pathophysiology=(
"**RET activation**: germline (MEN2A, MEN2B) or somatic RET mutations constitutively activate the kinase, driving C-cell hyperplasia then carcinoma. "
"**Genotype-phenotype**: specific codons predict aggressiveness and age of onset, guiding prophylactic thyroidectomy timing (ATA risk levels; M918T is highest risk). "
"**No iodine uptake**: C cells lack the sodium-iodide symporter, so RAI and TSH suppression are ineffective. "
"**Lymphatic spread**: early central and lateral nodal metastasis, guided by calcitonin levels. "
"**Markers**: calcitonin and CEA track disease burden; doubling time predicts prognosis. "
"**Pheochromocytoma**: must be excluded before surgery in MEN2. "
"**Targeted therapy**: selective RET inhibitors (selpercatinib, pralsetinib) treat advanced disease."),
),

"Anaplastic Thyroid Cancer": dict(
overview=(
"Anaplastic thyroid cancer is a rapidly growing, undifferentiated cancer of older adults and one of the most lethal human malignancies. "
"All are stage IV, and BRAF-targeted therapy has changed outcomes for BRAF-mutant tumors."),
physiology=(
"**Differentiation**: normal thyroid follicular cells express thyroglobulin, TPO, and the iodide symporter. "
"**Tumor progression**: differentiated cancers can dedifferentiate with accumulating mutations. "
"**Airway neighbors**: the trachea, esophagus, recurrent laryngeal nerves, and great vessels surround the gland."),
pathophysiology=(
"**Dedifferentiation**: TP53 and TERT promoter mutations on top of BRAF or RAS drive loss of follicular features. "
"**Loss of iodine uptake**: RAI is useless. "
"**Rapid local invasion**: compresses or invades the trachea, esophagus, and RLN, causing stridor, dysphagia, and hoarseness within weeks. "
"**BRAF V600E**: present in a substantial subset; dabrafenib-trametinib produces dramatic responses and can make tumors resectable. "
"**Airway management**: tracheostomy through tumor is difficult and may not prolong survival; goals of care are essential."),
),

"Central Neck Dissection": dict(
overview=(
"Central neck dissection removes level VI (and often VII) nodes between the carotids, from the hyoid to the innominate artery. "
"It is therapeutic for clinically involved nodes and prophylactic in selected thyroid cancers, at the cost of RLN and parathyroid risk."),
physiology=(
"**Boundaries**: hyoid superiorly, innominate artery inferiorly, carotids laterally, prevertebral fascia posteriorly. "
"**Contents**: prelaryngeal (Delphian), pretracheal, and paratracheal nodes. "
"**Structures at risk**: RLN (with right-left differences in course), inferior parathyroids and their blood supply (inferior thyroid artery), and the thymus."),
pathophysiology=(
"**First-echelon drainage**: papillary and medullary thyroid cancers metastasize to the central compartment first. "
"**Prophylactic dissection**: reduces central recurrence but increases hypoparathyroidism and RLN injury, so it is selective. "
"**Hypoparathyroidism mechanism**: devascularization of the inferior glands, which share blood supply and fat with central nodes. "
"**Reoperation risk**: scar after previous central surgery greatly increases complications."),
),

"Reoperative Thyroid Surgery": dict(
overview=(
"Reoperative thyroid surgery addresses recurrent or persistent disease, completion thyroidectomy, or recurrent goiter in a previously operated neck. "
"Scar distorts planes and raises RLN and parathyroid risk, so planning and alternative approaches matter."),
physiology=(
"**Virgin-neck planes**: strap muscles, thyroid capsule, and carotid sheath are separated by loose areolar tissue that dissects easily. "
"**Nerve identification**: the RLN is usually found in the tracheoesophageal groove or at its laryngeal entry near the cricothyroid joint. "
"**Parathyroid blood supply**: delicate end-arteries mostly from the inferior thyroid artery. "
"**Healing after surgery**: fibroblasts lay down collagen that obliterates planes over months, gluing structures together."),
pathophysiology=(
"**Scar**: obliterates planes and fixes structures, increasing RLN and parathyroid injury. "
"**Lateral (back-door) approach**: entering between strap muscles and SCM reaches the thyroid bed through less scarred tissue. "
"**Preoperative laryngoscopy**: identifies existing vocal fold paralysis. "
"**Nerve monitoring**: helps identify a scarred RLN."),
),

"Secondary / Tertiary Hyperparathyroidism": dict(
overview=(
"Secondary hyperparathyroidism is appropriate PTH elevation in response to low calcium or high phosphate, usually from chronic kidney disease or vitamin D deficiency. "
"Tertiary hyperparathyroidism is autonomous PTH secretion persisting after the stimulus is corrected (often after kidney transplant)."),
physiology=(
"**Kidney role**: kidneys activate vitamin D (1-alpha-hydroxylation) and excrete phosphate. "
"**FGF23**: bone-derived hormone that increases phosphate excretion and lowers calcitriol. "
"**Parathyroid response**: low calcium, high phosphate, and low calcitriol stimulate PTH secretion and gland growth."),
pathophysiology=(
"**CKD sequence**: phosphate retention and FGF23 rise reduce calcitriol, causing hypocalcemia and parathyroid stimulation. "
"**Gland hyperplasia**: chronic stimulation causes polyclonal then monoclonal (nodular) hyperplasia of all four glands, with reduced CaSR and vitamin D receptor expression. "
"**Tertiary disease**: autonomous nodules continue secreting after transplant, causing hypercalcemia. "
"**Renal osteodystrophy and calciphylaxis**: bone disease and vascular calcification result from mineral imbalance. "
"**Treatment**: phosphate binders, vitamin D analogs, and calcimimetics (cinacalcet) reduce PTH; surgery (subtotal or total with autotransplant) for refractory disease."),
),

"Four-Gland Parathyroid Exploration": dict(
overview=(
"Bilateral four-gland exploration identifies all parathyroid glands and removes abnormal ones. "
"It is required for multigland disease, MEN syndromes, discordant or negative localization, and inadequate intraoperative PTH drop."),
physiology=(
"**Embryology**: superior glands from the fourth pouch (consistent location); inferior glands from the third pouch with thymus (variable, can descend into the mediastinum). "
"**Normal glands**: about 3-5 mm, tan, 30-50 mg. "
"**Blood supply**: mostly the inferior thyroid artery."),
pathophysiology=(
"**Multigland disease**: hyperplasia or double adenomas missed by focused surgery cause persistent disease. "
"**Ectopic locations**: inferior glands in the thymus, mediastinum, or undescended near the carotid; superior glands tracheoesophageal groove or retroesophageal. "
"**Supernumerary glands**: present in a minority. "
"**Intraoperative PTH**: a drop of more than 50 percent predicts cure."),
),

"Sialolithiasis": dict(
overview=(
"Sialolithiasis is stone formation in salivary ducts, most often the submandibular (Wharton) duct, causing meal-related swelling and pain. "
"Treatment ranges from conservative care to sialendoscopy and gland excision."),
physiology=(
"**Saliva composition**: water, electrolytes, mucins, enzymes, and calcium phosphate near saturation. "
"**Submandibular saliva**: more alkaline, more mucinous, and higher in calcium than parotid saliva. "
"**Wharton duct**: long, runs upward against gravity, with an angle around the mylohyoid. "
"**Stimulated flow**: eating triggers a large increase in saliva production."),
pathophysiology=(
"**Stone formation**: stasis and alkaline, calcium-rich saliva promote precipitation of calcium phosphate around a nidus of mucus or debris. "
"**Submandibular predominance (about 80-90 percent)**: long uphill duct, viscous and calcium-rich saliva. "
"**Meal-related swelling**: obstructed saliva builds up when stimulated. "
"**Infection**: stasis allows retrograde bacteria (S. aureus). "
"**Chronic sialadenitis**: repeated obstruction causes fibrosis and gland dysfunction."),
),

"Sialendoscopy": dict(
overview=(
"Sialendoscopy is endoscopic examination and treatment of salivary ducts for stones, strictures, and inflammation, preserving the gland. "
"It has reduced the need for gland excision."),
physiology=(
"**Duct anatomy**: Stensen duct (parotid) is about 5 cm long, piercing the buccinator opposite the upper second molar; Wharton duct (submandibular) is about 5 cm, running from the hilum around the mylohyoid to the sublingual papilla. "
"**Narrowing points**: the papilla, the buccinator bend (Stensen), and the hilum are natural sites where stones and strictures occur. "
"**Ductal epithelium**: can heal after dilation or minor injury if the gland keeps flowing. "
"**Gland reserve**: an obstructed gland often retains secretory capacity, so restoring drainage restores function."),
pathophysiology=(
"**Stones**: small mobile stones are removed with baskets; larger stones require fragmentation or combined approaches. "
"**Strictures**: dilation treats stenoses. "
"**Inflammation**: irrigation with steroids treats juvenile recurrent parotitis and radioiodine sialadenitis. "
"**Gland recovery**: removing obstruction restores function."),
),

"Submandibular Gland Excision": dict(
overview=(
"Submandibular gland excision treats chronic sialadenitis, stones not amenable to sialendoscopy, and tumors. "
"It requires protecting the marginal mandibular, lingual, and hypoglossal nerves."),
physiology=(
"**Location**: in the submandibular triangle, wrapping around the posterior mylohyoid. "
"**Nerves**: marginal mandibular (superficial, under platysma), lingual (superior, connected to the submandibular ganglion), hypoglossal (deep, inferior). "
"**Vessels**: facial artery and vein."),
pathophysiology=(
"**Chronic sialadenitis**: repeated obstruction and infection replace acini with fibrosis and lymphocytes, making the gland firm and nonfunctional; removal is indicated when sialendoscopy cannot restore drainage. "
"**Tumors**: about half of submandibular tumors are malignant, so firmness, fixation, or nerve symptoms change the operation to an oncologic resection with neck dissection. "
"**Marginal mandibular injury**: lower-lip weakness, avoided by elevating the fascia over the gland deep to the nerve (Hayes Martin maneuver) or ligating the facial vein low. "
"**Lingual nerve injury**: tongue numbness from traction on the submandibular ganglion attachment. "
"**Hypoglossal injury**: tongue weakness from dissection deep and inferior to the gland. "
"**Inflamed planes**: fibrosis from chronic infection increases bleeding and nerve risk."),
),

"Graves Disease / Toxic Goiter": dict(
overview=(
"Graves disease is autoimmune hyperthyroidism caused by TSH receptor-stimulating antibodies; toxic multinodular goiter and toxic adenoma are autonomous nodular causes. "
"Treatment options are antithyroid drugs, radioactive iodine, or thyroidectomy."),
physiology=(
"**TSH receptor**: G-protein coupled receptor driving thyroid hormone synthesis and growth. "
"**Thyroid hormone effects**: increase metabolic rate, beta-adrenergic sensitivity, and heat production. "
"**Hormone synthesis steps**: iodide trapping, organification by TPO, coupling, and release."),
pathophysiology=(
"**Stimulating antibodies**: TSI mimic TSH, causing diffuse hyperplasia and hyperthyroidism independent of pituitary control. "
"**Extrathyroidal effects**: orbital fibroblasts express TSH receptor and IGF-1 receptor, explaining thyroid eye disease; pretibial myxedema results from similar mechanisms. "
"**Toxic nodules**: autonomous function from TSH receptor mutations. "
"**Thyroid storm**: decompensated thyrotoxicosis triggered by surgery, infection, or iodine load. "
"**Medication logic**: methimazole and PTU block TPO; PTU also blocks peripheral T4-to-T3 conversion; beta-blockers control symptoms. "
"**Preoperative iodine**: SSKI reduces gland vascularity and hormone release (Wolff-Chaikoff effect)."),
),

"Indeterminate Thyroid Cytology / Molecular Testing": dict(
overview=(
"Indeterminate thyroid cytology (Bethesda III and IV) carries an intermediate risk of malignancy. "
"Molecular testing refines risk and can spare surgery in benign-appearing molecular profiles."),
physiology=(
"**What FNA samples**: a fine needle aspirates individual follicular cells and colloid; it captures nuclear and cellular features but destroys tissue architecture. "
"**Bethesda categories**: I nondiagnostic, II benign, III atypia of undetermined significance, IV follicular neoplasm, V suspicious for malignancy, VI malignant, each with its own malignancy risk. "
"**Follicular growth patterns**: normal thyroid and many benign nodules contain follicles of varying size; a microfollicular, crowded pattern raises concern for a follicular neoplasm. "
"**Nuclear features of papillary carcinoma**: enlarged, overlapping nuclei with grooves, pseudoinclusions, and chromatin clearing are visible on cytology."),
pathophysiology=(
"**The architecture problem**: follicular carcinoma is defined by capsular or vascular invasion, which only histology of the whole capsule can show, so a cellular follicular aspirate cannot be called benign or malignant. "
"**Atypia (Bethesda III)**: partial or focal nuclear or architectural atypia that falls short of a diagnosis. "
"**Driver mutations**: BRAF V600E, RET/PTC, and NTRK fusions carry very high cancer risk; RAS mutations are common in follicular adenoma, follicular carcinoma, and NIFTP alike, so they predict a neoplasm rather than cancer. "
"**NIFTP**: a noninvasive follicular-patterned tumor with papillary-like nuclei, reclassified as a neoplasm with very low malignant potential, treated by lobectomy alone. "
"**Molecular test logic**: rule-out tests (high negative predictive value gene expression classifiers) allow surveillance; rule-in panels with high-risk mutations support surgery and inform extent."),
),

"MEN2 / RET": dict(
overview=(
"MEN2 is an autosomal dominant syndrome from germline RET mutations: MEN2A (medullary thyroid cancer, pheochromocytoma, primary hyperparathyroidism) and MEN2B (MTC, pheochromocytoma, mucosal neuromas, marfanoid habitus). "
"Genetic testing drives prophylactic thyroidectomy timing."),
physiology=(
"**RET receptor**: a transmembrane tyrosine kinase activated by GDNF-family ligands with a co-receptor, essential for neural crest cell migration and survival. "
"**Neural crest derivatives**: thyroid C cells, adrenal medullary chromaffin cells, and enteric neurons all depend on RET signaling during development. "
"**Parathyroid involvement**: the mechanism for parathyroid hyperplasia in MEN2A is less clear but tracks with specific codons. "
"**Inheritance**: autosomal dominant, so each child of a carrier has a 50 percent risk."),
pathophysiology=(
"**Activating mutations**: germline gain-of-function mutations cause constitutive kinase activity. "
"**Codon-specific risk**: M918T (MEN2B) causes very early aggressive MTC, prompting thyroidectomy in the first year; other codons allow later surgery. "
"**Pheochromocytoma**: must be excluded and treated first. "
"**Hyperparathyroidism**: MEN2A only, often milder. "
"**Hirschsprung association**: loss-of-function RET mutations; some MEN2A mutations also cause Hirschsprung disease."),
),

"Parathyroid Carcinoma": dict(
overview=(
"Parathyroid carcinoma is a rare cause of primary hyperparathyroidism with very high calcium and PTH, a palpable firm mass, and invasion of adjacent structures. "
"En bloc resection at first surgery offers the best chance of cure."),
physiology=(
"**Chief cells**: parathyroid chief cells secrete PTH and sense calcium through the calcium-sensing receptor. "
"**Growth control**: tumor suppressors including parafibromin (CDC73) and menin restrain parathyroid proliferation. "
"**Gland capsule**: normal glands and adenomas are encapsulated and separate cleanly from surrounding tissue. "
"**Set point**: in benign adenomas the calcium set point shifts modestly, so hypercalcemia is usually mild."),
pathophysiology=(
"**CDC73 inactivation**: loss of parafibromin (somatic or germline in hyperparathyroidism-jaw tumor syndrome) is the dominant driver, and loss of parafibromin staining supports the diagnosis. "
"**Profound hypercalcemia**: autonomous, high-volume PTH secretion produces very high calcium and PTH levels, with severe bone and kidney disease at presentation. "
"**Local invasion**: a firm, gray-white mass adherent to the thyroid, RLN, and strap muscles, unlike the soft, tan, easily separated adenoma. "
"**Histologic criteria**: vascular, perineural, or adjacent-tissue invasion suggests malignancy, but histology is often inconclusive; only metastasis or local recurrence is definitive. "
"**Why en bloc resection**: capsular rupture seeds tumor cells that implant and recur, so the gland is removed with the adjacent thyroid lobe and any adherent tissue. "
"**Natural history**: morbidity and death usually come from uncontrolled hypercalcemia rather than tumor bulk, so calcimimetics are central in advanced disease."),
),
}
