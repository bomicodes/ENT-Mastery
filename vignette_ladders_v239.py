"""v23.9 — final Thyroid / Parathyroid / Salivary ladder closure.

Reviews the final two canonical topics: familial hyperparathyroidism /
parathyromatosis and salivary adenoid cystic carcinoma / perineural spread.
"""
DOMAIN="Thyroid / Parathyroid / Salivary"

def _q(qid,topic,stage,stem,choices,answer,explanation,reasons,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":reasons,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V239=[
_q("v239_tps_famhpt_fnd","Familial Hyperparathyroidism / Parathyromatosis","foundation",
"A young patient has multigland primary hyperparathyroidism and several relatives with hypercalcemia or endocrine tumors. What is the most important additional principle?",
["Evaluate for a hereditary hyperparathyroidism syndrome because genetics can change the operation, surveillance, and family counseling","Assume every case is a solitary sporadic adenoma","Perform thyroid ablation with radioactive iodine","Ignore the family history"],0,
"Young age, multigland disease, recurrent disease, atypical pathology, or a strong family history should raise concern for syndromes such as MEN1, MEN2A, CDC73-related disease, or familial isolated hyperparathyroidism. The syndrome can alter how much parathyroid tissue is treated and what other tumors require surveillance.",
["Correct. Hereditary context changes both the index operation and lifelong management.","A solitary sporadic model can lead to inadequate surgery in true multigland hereditary disease.","RAI does not treat parathyroid hyperfunction.","Family history is a major diagnostic clue and has implications for relatives."],
"Multigland hyperparathyroidism in a young patient is a genetics question before it is merely a localization question.","Which associated tumors should be sought when MEN1 is suspected?"),
_q("v239_tps_famhpt_app","Familial Hyperparathyroidism / Parathyromatosis","application",
"A patient with known MEN1 has primary hyperparathyroidism. Why is a focused excision of one enlarged gland often inadequate?",
["MEN1 usually represents multigland hyperplasia, so the operative strategy must address the expected multigland biology while balancing durable control against permanent hypoparathyroidism","MEN1 affects only one parathyroid gland","Parathyroid surgery is contraindicated in MEN1","The calcium level is unrelated to parathyroid tissue"],0,
"MEN1-associated hyperparathyroidism is usually multigland disease. Operations are therefore designed around multigland treatment—such as subtotal parathyroidectomy or total parathyroidectomy with autotransplantation in selected settings—rather than simply chasing the largest localized gland.",
["Correct. The syndrome predicts the biology better than a single localization study.","MEN1 is characteristically multigland, not a one-gland disorder.","Surgery is commonly required when standard indications are met.","Hypercalcemia is produced by excess parathyroid hormone activity and is central to the disease."],
"In hereditary HPT, localization helps you find glands; genetics tells you how many glands you should expect to be diseased.","How does a prior subtotal operation change planning for recurrent MEN1 hyperparathyroidism?","OR_prep"),
_q("v239_tps_famhpt_snr","Familial Hyperparathyroidism / Parathyromatosis","senior_decision",
"A patient has recurrent hyperparathyroidism after several neck operations. Imaging shows multiple tiny enhancing nodules scattered in the prior operative bed, and the original surgery involved capsular disruption. What diagnosis and planning issue should be considered?",
["Parathyromatosis from implanted hyperfunctioning parathyroid tissue, requiring careful reoperative mapping and counseling that cure may be difficult without unacceptable morbidity","Simple dehydration","Frey syndrome","A ranula"],0,
"Parathyromatosis can arise from seeding of parathyroid tissue after capsular rupture or prior surgery and can cause difficult recurrent hyperparathyroidism. Multiple small implants may be hard to eradicate completely in a scarred neck, so reoperation requires detailed localization, RLN awareness, biochemical confirmation, and realistic expectations.",
["Correct. Multifocal implants in a previously operated field are a classic reoperative challenge.","Dehydration does not create multiple enhancing parathyroid implants.","Frey syndrome is gustatory sweating after parotid-region injury.","A ranula is a sublingual mucus collection and does not produce hyperparathyroidism."],
"Avoiding parathyroid capsular rupture is not cosmetic technique—it can prevent a lifelong reoperative problem.","How would recurrent laryngeal nerve function and the distribution of implants affect the threshold for another operation?","OR_prep"),

_q("v239_tps_acc_fnd","Salivary Adenoid Cystic Carcinoma / Perineural Spread","foundation",
"Which biologic feature is especially characteristic of salivary adenoid cystic carcinoma?",
["A strong tendency for perineural invasion and late distant recurrence despite sometimes indolent local growth","Almost universal early lymph-node metastasis with no neural invasion","Spontaneous cure without treatment","Exclusive origin in the thyroid"],0,
"Adenoid cystic carcinoma is notable for neurotropism, perineural invasion, local recurrence, and the possibility of late hematogenous metastasis, particularly to the lungs. Nodal spread is generally less dominant than in many squamous carcinomas.",
["Correct. Neural spread and long natural history are central to ACC behavior.","Routine biology is not dominated by early nodal metastasis, and neural invasion is common.","ACC is a malignant salivary neoplasm requiring definitive management.","ACC arises in major or minor salivary glands, not exclusively in thyroid tissue."],
"ACC is a 'follow the nerve and follow for years' cancer.","Which cranial neuropathies can reveal occult proximal perineural spread from minor salivary primaries?"),
_q("v239_tps_acc_app","Salivary Adenoid Cystic Carcinoma / Perineural Spread","application",
"A hard-palate adenoid cystic carcinoma causes new V2 numbness, and MRI shows enhancement tracking toward foramen rotundum. What is the best management principle?",
["Map the full named-nerve pathway to its proximal extent and incorporate that disease into surgical and radiation planning rather than treating only the visible mucosal primary","Ignore the numbness because ACC never spreads along nerves","Perform elective thyroidectomy","Treat with antibiotics alone"],0,
"Clinical and radiographic perineural spread changes the true oncologic extent. Imaging should follow the involved nerve centrally, and resection/adjuvant radiation fields should be designed around the involved pathway when curative treatment remains feasible.",
["Correct. The nerve can be a route of gross tumor extension beyond the visible primary.","ACC is highly neurotropic, making new sensory loss a major staging clue.","Thyroid surgery does not address a palatal salivary malignancy.","Antibiotics do not treat malignant perineural spread."],
"In ACC, new numbness is tumor anatomy until proven otherwise.","How does skull-base extension affect surgical margins and adjuvant radiation design?","OR_prep"),
_q("v239_tps_acc_snr","Salivary Adenoid Cystic Carcinoma / Perineural Spread","senior_decision",
"A patient has resected major-salivary adenoid cystic carcinoma with close margins and extensive named-nerve perineural invasion but no nodal disease. What should dominate postoperative planning?",
["Discuss adjuvant radiation to the operative bed and involved neural pathways based on the high local/perineural recurrence risk, while planning long-term surveillance for late distant disease","Observe only because the neck nodes are negative","Perform routine bilateral radical neck dissection","Stop surveillance after two years"],0,
"ACC risk is not captured by nodal status alone. Close/positive margins, advanced T category, and perineural invasion strongly influence local control strategy, and distant recurrence can emerge many years later, supporting prolonged surveillance.",
["Correct. Postoperative management follows the tumor's local and neural-risk biology.","A node-negative neck does not erase perineural or margin-related recurrence risk.","Routine radical bilateral neck dissection is not justified solely by ACC histology without appropriate nodal indications.","ACC can relapse late, so short surveillance is inadequate."],
"Negative nodes do not make ACC low risk when the nerve and margin are involved.","How would unresectable skull-base perineural extension change the balance among radiation, systemic therapy, and symptom-directed care?")]

def apply_learning_ladders_v239(challenges,item_id_fn):
    existing={q.get("id") for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V239:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v239 orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":2}
