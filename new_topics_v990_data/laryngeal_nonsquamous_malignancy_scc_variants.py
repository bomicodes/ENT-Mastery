T = "Nonsquamous Laryngeal Malignancies and SCC Variants"


def _v(stem, choices, answer, explanation, why_wrong, pearl, cb, cba, stage, focus):
    return {"topic": T, "stem": stem, "choices": choices, "answer": answer,
            "explanation": explanation, "why_wrong": why_wrong, "board_pearl": pearl,
            "curveball": cb, "curveball_answer": cba, "learning_stage": stage, "focus": focus}


TOPIC = {
    "domain": "Head & Neck Oncology",
    "topic": T,
    "overview": "\n".join([
        "**Scope**: about 95% of laryngeal cancers are conventional SCC. The remaining minority, SCC variants plus neuroendocrine, cartilaginous, salivary-type, hematolymphoid and melanocytic tumors, behave so differently that histology rather than T stage drives treatment (Cummings 7e, Ch 105)",
        "**SCC variants**: verrucous carcinoma (indolent, glottic), basaloid SCC (aggressive, supraglottic/piriform), spindle cell (sarcomatoid) carcinoma (polypoid glottic mass) (Pasha 6e, Ch 6)",
        "**Neuroendocrine tumors**: the second most common laryngeal malignancy group after SCC. Atypical carcinoid is the most common NET, followed by small cell NEC. Typical carcinoid is rare (Cummings 7e, Ch 105)",
        "**Chondrosarcoma**: the most common nonepithelial laryngeal malignancy, usually from the posterior cricoid lamina in men (about 3:1), mostly low grade (Cummings 7e, Ch 105)",
        "**Salivary-type carcinomas**: adenoid cystic (subglottis about 60%), mucoepidermoid (supraglottis) and adenocarcinoma (about 1%) arise from submucosal seromucinous glands (Cummings 7e, Ch 105)",
        "**Others**: extramedullary plasmacytoma, primary lymphoma, mucosal melanoma, paraganglioma (benign) and metastases (kidney, prostate, breast, lung, melanoma) (Pasha 6e, Ch 6)",
    ]),
    "physiology": "\n".join([
        "**Gland distribution**: seromucinous glands are densest in the supraglottis (saccule, false cords, epiglottic pits) and subglottis and sparse on the true cord, which explains where salivary-type tumors arise (Cummings 7e, Ch 105)",
        "**Cartilage ossification**: hyaline cartilages (cricoid, thyroid, most of arytenoid) ossify with age, and chondrosarcoma arises in hyaline cartilage, most often the posterior cricoid plate (Cummings 7e, Ch 105)",
        "**Paraganglia**: paired superior (near the superior laryngeal artery, false cord/aryepiglottic fold) and inferior (near the cricoid/RLN) laryngeal paraganglia give rise to laryngeal paragangliomas (Cummings 7e, Ch 105)",
        "**Lymphoid tissue**: MALT in the supraglottis/ventricle is the substrate for primary laryngeal lymphoma and plasmacytoma, both submucosal lesions (Cummings 7e, Ch 105)",
        "**Basement membrane**: the boundary separating verrucous carcinoma (pushing, intact) from invasive SCC. Its integrity determines metastatic potential (Pasha 6e, Ch 6)",
    ]),
    "pathophysiology": "\n".join([
        "**Verrucous carcinoma (Ackerman)**: very well-differentiated, hyperkeratotic church-spire papillae with broad pushing borders and no true destructive invasion. Nodal metastasis is rare. Hybrid tumors with foci of conventional SCC behave like SCC (Pasha 6e, Ch 6)",
        "**Basaloid SCC**: high-grade nests of basaloid cells with comedonecrosis, strongly tobacco/alcohol related, with early nodal and distant spread and worse stage-for-stage behavior (Pasha 6e, Ch 6)",
        "**Spindle cell carcinoma**: biphasic carcinoma whose malignant spindle stroma can be keratin-weak, mimicking sarcoma or a reactive polyp. Prognosis tracks depth of invasion more than polypoid size (Pasha 6e, Ch 6)",
        "**Atypical carcinoid**: supraglottic, male smokers, about 50% nodal and 40-45% distant spread (skin, liver, bone, lung) with about 50% 5-year disease-specific survival. Calcitonin may be elevated and can mimic medullary thyroid cancer (Cummings 7e, Ch 105)",
        "**Small cell NEC**: behaves like lung small cell, with roughly 50% nodal and 60% distant disease at presentation and paraneoplastic syndromes possible (Cummings 7e, Ch 105)",
        "**Adenoid cystic carcinoma**: perineural and hematogenous spread with late lung metastasis, so long survival with disease is common and 5-year figures overstate cure (Cummings 7e, Ch 105)",
        "**Plasmacytoma**: monoclonal plasma cell neoplasm, amyloid in up to 40%, and 16-32% later progress to multiple myeloma (Cummings 7e, Ch 105)",
    ]),
    "recognize": "\n".join([
        "**Verrucous**: older male smoker with hoarseness and a bulky warty gray-white glottic mass. Repeated small biopsies read as 'hyperplasia' or 'papillomatosis' (Pasha 6e, Ch 6)",
        "**Spindle cell**: pedunculated polypoid glottic mass that looks like a benign polyp but recurs or grows quickly (Pasha 6e, Ch 6)",
        "**Submucosal mass with intact mucosa**: think chondrosarcoma (hard, posterior subglottic, slow dyspnea), salivary-type tumor, lymphoma, plasmacytoma or paraganglioma (Cummings 7e, Ch 105)",
        "**Paraganglioma**: woman (about 3:1) with a red-blue submucosal aryepiglottic fold or false cord mass, hoarseness or dysphagia (Cummings 7e, Ch 105)",
        "**Mucosal melanoma**: pigmented or amelanotic supraglottic mass. Always exclude a cutaneous primary metastatic to the larynx (Cummings 7e, Ch 105)",
        "**Neck or distant disease out of proportion**: a small supraglottic primary with bulky nodes, skin nodules or liver lesions suggests atypical carcinoid, small cell or basaloid SCC (Cummings 7e, Ch 105)",
    ]),
    "localize": "\n".join([
        "**Glottis**: verrucous carcinoma and spindle cell carcinoma (Pasha 6e, Ch 6)",
        "**Supraglottis/aryepiglottic fold**: atypical carcinoid, small cell NEC, basaloid SCC, paraganglioma, mucoepidermoid, plasmacytoma, lymphoma, melanoma (Cummings 7e, Ch 105)",
        "**Subglottis**: adenoid cystic carcinoma (about 60%), and chondrosarcoma presenting as a posterior subglottic bulge (Cummings 7e, Ch 105)",
        "**Cricoid lamina**: chondrosarcoma site of origin in the majority, then thyroid cartilage and arytenoid (Cummings 7e, Ch 105)",
        "**Nodal basins**: supraglottic NETs drain bilaterally to levels II-IV, subglottic tumors to level VI, paratracheal and mediastinal nodes (Cummings 7e, Ch 105)",
    ]),
    "workup": "\n".join([
        "**Biopsy technique**: verrucous carcinoma needs a large, deep biopsy including the base to see the pushing border. Lymphoma needs a deep fresh specimen sent for flow cytometry (Pasha 6e, Ch 6)",
        "**Do not biopsy a suspected paraganglioma in clinic**: risk of brisk bleeding. Use contrast MRI (flow voids, avid enhancement) and somatostatin-receptor imaging (Ga-68 DOTATATE now preferred over octreotide scan) (Cummings 7e, Ch 105)",
        "**Chondrosarcoma imaging**: CT shows an expansile cartilage-centered mass with stippled or 'popcorn' calcification. Biopsy is often nondiagnostic because low-grade tumor resembles chondroma (Cummings 7e, Ch 105)",
        "**Neuroendocrine staging**: chromogranin/synaptophysin/INSM1 IHC, Ki-67, serum calcitonin, CT chest/abdomen or PET, and DOTATATE PET for well-differentiated tumors. Small cell needs brain imaging (Cummings 7e, Ch 105)",
        "**Plasmacytoma**: SPEP/UPEP with free light chains, bone marrow biopsy and skeletal survey or whole-body low-dose CT/PET to exclude multiple myeloma (Cummings 7e, Ch 105)",
        "**Melanoma**: full skin and ocular exam, S-100/SOX10/HMB-45/Melan-A IHC, and PET-CT (Cummings 7e, Ch 105)",
    ]),
    "manage": "\n".join([
        "**Verrucous**: surgery (transoral laser excision or partial laryngectomy) is preferred. RT also controls disease, and the old fear of anaplastic transformation after RT is now considered overstated, but surgery remains first choice. No elective neck (Pasha 6e, Ch 6)",
        "**Basaloid and spindle cell**: treat like conventional SCC of equal stage, with low threshold to treat the neck for basaloid. Spindle cell polyps often do well with excision when invasion is shallow (Pasha 6e, Ch 6)",
        "**Atypical carcinoid**: surgery (partial or total laryngectomy) plus bilateral neck dissection even when N0. RT and chemotherapy are of limited benefit (Cummings 7e, Ch 105)",
        "**Typical carcinoid and paraganglioma**: conservative complete excision with no elective neck. Paraganglioma via lateral pharyngotomy or thyrotomy, sometimes after embolization (Cummings 7e, Ch 105)",
        "**Small cell NEC**: systemic platinum-etoposide chemotherapy with RT, like lung small cell. Surgery has no primary role (Cummings 7e, Ch 105)",
        "**Chondrosarcoma**: function-preserving resection (partial cricoid resection with reconstruction) for low grade, total laryngectomy for high grade or unreconstructable disease. RT/chemo largely ineffective and about 90% 5-year survival (Cummings 7e, Ch 105)",
        "**Salivary-type, plasmacytoma, lymphoma**: adenoid cystic gets surgery plus PORT (neck dissection only if N+). Plasmacytoma gets RT including first-echelon nodes. Lymphoma gets RT and/or R-CHOP-based chemotherapy (Cummings 7e, Ch 105)",
        "**Mucosal melanoma**: wide surgical excision with adjuvant RT for local control. Systemic immunotherapy for advanced disease, with poor survival (<20% at 5 years) (Cummings 7e, Ch 105)",
    ]),
    "operate": "\n".join([
        "**Biopsy depth**: for any submucosal or 'benign-looking' glottic lesion, take a deep cold-cup or laser wedge to the base rather than surface shavings (Pasha 6e, Ch 6)",
        "**Cricoid chondrosarcoma**: preserve at least part of the cricoid ring when possible. Partial cricoid resection can be reconstructed with rib cartilage, a stent or a flap, and tracheostomy is often temporary (Cummings 7e, Ch 105)",
        "**Paraganglioma**: open external approach (lateral pharyngotomy or laryngofissure) gives vascular control. Endoscopic biopsy or piecemeal removal invites hemorrhage (Cummings 7e, Ch 105)",
        "**Atypical carcinoid**: include bilateral levels II-IV (and VI for subglottic extension) in the neck dissection regardless of clinical N stage (Cummings 7e, Ch 105)",
        "**Adenoid cystic**: send nerve and subglottic/tracheal margins on frozen section and expect submucosal extension beyond the visible tumor (Cummings 7e, Ch 105)",
    ]),
    "teach": "\n".join([
        "**'Histology beats T stage'**: two T2 supraglottic tumors can need opposite treatment (bilateral neck dissection for atypical carcinoid, chemoradiation for small cell) (Cummings 7e, Ch 105)",
        "**Three that radiation does not fix**: chondrosarcoma, typical carcinoid and atypical carcinoid are surgical diseases",
        "**Three that radiation does fix**: plasmacytoma, lymphoma and small cell NEC (with chemo) are nonsurgical",
        "**'Pushing, not invading'**: verrucous carcinoma has a pushing border, an intact basement membrane and rarely metastasizes, so no elective neck",
        "**'Red submucosal supraglottic mass in a woman: put the biopsy forceps down'**: think paraganglioma",
    ]),
    "tags": ["larynx", "neuroendocrine", "carcinoid", "chondrosarcoma", "verrucous carcinoma", "basaloid SCC", "spindle cell carcinoma", "adenoid cystic carcinoma", "plasmacytoma", "paraganglioma", "mucosal melanoma"],
    "source_basis": ["Cummings 7e Ch 105", "Pasha 6e Ch 6"],
    "textbook_refs": [
        "Cummings Otolaryngology 7e, Ch 105 Malignant Tumors of the Larynx (pp 1591-1595)",
        "Pasha Otolaryngology-Head and Neck Surgery Clinical Reference Guide 6e, Ch 6 (pp 280, 293, 295-296, 315)",
    ],
    "literature_refs": [
        "Ferlito A, Silver CE, Bradford CR, Rinaldo A. Head Neck 2009;31:1634-1646 (neuroendocrine neoplasms of the larynx: atypical carcinoid most common NET, surgery plus neck dissection, small cell treated systemically)",
        "Thompson LDR, Gannon FH. Am J Surg Pathol 2002;26:836-851 (111 laryngeal chondrosarcomas: cricoid predominance, mostly low grade, excellent survival with conservative surgery)",
    ],
    "case_label": "Small supraglottic submucosal mass with bilateral neck nodes and elevated serum calcitonin in a 60-year-old smoker",
    "or_slugs": [],
  "concept_check": {
    "topic": "Nonsquamous Laryngeal Malignancies and SCC Variants",
    "stem": "A 64-year-old man who has smoked for 45 years presents with 6 months of progressive hoarseness. Laryngoscopy shows a bulky, warty, gray-white exophytic mass of the left true vocal fold with normal fold mobility. Two superficial cup-forceps biopsies in clinic show only hyperkeratosis and squamous hyperplasia without dysplasia. The neck is clinically N0. Which is the most appropriate next step?",
    "choices": [
      "Repeat office brush biopsy and reexamine in 3 months",
      "Deep biopsy to the lesion base under general anesthesia",
      "Definitive radiation for presumed squamous cell carcinoma",
      "PET-CT and elective bilateral neck dissection"
    ],
    "answer": 1,
    "explanation": "A bulky warty glottic mass with repeatedly 'benign' superficial biopsies is verrucous carcinoma until proven otherwise. Its diagnostic feature is the broad, pushing border of well-differentiated epithelium at the tumor-stroma interface with an intact basement membrane, which superficial samples never reach. A large, deep biopsy including the base, usually at microlaryngoscopy, is required before treatment. Once confirmed, surgery such as endoscopic excision is preferred, and the neck is not treated electively.",
    "why_wrong": [
      "Another superficial sample will repeat the same nondiagnostic result and delay treatment.",
      "Correct.",
      "Treatment should not start without tissue diagnosis, and surgery is preferred first treatment for verrucous carcinoma.",
      "Verrucous carcinoma rarely metastasizes, so elective neck dissection is not indicated and staging is premature."
    ],
    "board_pearl": "Verrucous carcinoma: warty glottic mass, pushing borders, intact basement membrane, near-zero nodal risk, surgery first.",
    "curveball": "Final pathology of the excision shows verrucous carcinoma with a separate focus of conventional invasive SCC. Does this change management?",
    "curveball_answer": "Yes. A hybrid verrucous tumor containing conventional invasive SCC behaves like conventional SCC, with real nodal and recurrence risk. It should be staged and treated as SCC of the same site and stage, including margin assessment and consideration of elective neck treatment or adjuvant therapy as for conventional disease.",
    "learning_stage": "foundation",
    "focus": "diagnosis"
  },
  "ladder": [
    {
      "topic": "Nonsquamous Laryngeal Malignancies and SCC Variants",
      "stem": "A 58-year-old man presents with progressive exertional dyspnea and mild hoarseness over 2 years. He is a nonsmoker. Laryngoscopy shows a smooth submucosal bulge of the posterior subglottis with normal overlying mucosa and mobile vocal folds. CT shows an expansile, well-circumscribed mass arising from the posterior cricoid lamina with stippled internal calcifications. What is the most likely diagnosis?",
      "choices": [
        "Squamous cell carcinoma",
        "Adenoid cystic carcinoma",
        "Laryngeal paraganglioma",
        "Chondrosarcoma"
      ],
      "answer": 3,
      "explanation": "A slow-growing, cartilage-centered expansile mass of the posterior cricoid plate with stippled or 'popcorn' chondroid calcification and intact mucosa in a middle-aged man is chondrosarcoma, the most common nonepithelial laryngeal malignancy. Most are low grade, grow slowly and rarely metastasize, with about 90% 5-year survival. Treatment is conservative function-preserving resection where possible, as radiation is relatively ineffective. Mucosal SCC destroys rather than expands cartilage.",
      "why_wrong": [
        "SCC is mucosal and ulcerative and destroys cartilage rather than expanding it with calcified matrix.",
        "Adenoid cystic carcinoma is subglottic and submucosal but is not cartilage-centered or calcified.",
        "Paraganglioma is a supraglottic, avidly enhancing mass that is more common in women.",
        "Correct."
      ],
      "board_pearl": "Laryngeal chondrosarcoma: men, posterior cricoid lamina, stippled calcification on CT, low grade, about 90% 5-year survival.",
      "curveball": "The endoscopic biopsy is read as 'chondroma.' Should the patient be reassured that the lesion is benign?",
      "curveball_answer": "No. Laryngeal chondroma and low-grade chondrosarcoma are very difficult to separate on small biopsies because they differ mainly in cellularity and invasion pattern. A large expansile cricoid lesion with this imaging should be managed as low-grade chondrosarcoma, with function-preserving resection and long-term surveillance for recurrence.",
      "learning_stage": "foundation",
      "focus": "imaging"
    },
    {
      "topic": "Nonsquamous Laryngeal Malignancies and SCC Variants",
      "stem": "A 62-year-old male smoker presents with a right neck mass. Exam shows a 1.5-cm submucosal mass of the right aryepiglottic fold and a 3-cm level III node. Biopsy shows a moderately differentiated neuroendocrine carcinoma, chromogranin and synaptophysin positive, with 4 mitoses per 10 HPF and focal necrosis. Serum calcitonin is elevated, and thyroid ultrasound is normal. Which is the most appropriate treatment?",
      "choices": [
        "Supraglottic laryngectomy with bilateral neck dissection",
        "Concurrent cisplatin-etoposide chemoradiation",
        "Primary radiation alone to the larynx and neck",
        "Transoral excision of the primary with neck observation"
      ],
      "answer": 0,
      "explanation": "A moderately differentiated neuroendocrine carcinoma with necrosis and a few mitoses is atypical carcinoid, the most common laryngeal neuroendocrine tumor. It favors the supraglottis of male smokers and spreads to nodes in about 50% and to distant sites in 40-45%. It responds poorly to radiation and chemotherapy, so treatment is surgical: conservation or total laryngectomy with bilateral neck dissection. The raised calcitonin is a known feature and does not indicate medullary thyroid cancer once the thyroid is normal.",
      "why_wrong": [
        "Correct.",
        "Platinum-etoposide chemoradiation is the treatment for small cell neuroendocrine carcinoma, not atypical carcinoid.",
        "Atypical carcinoid responds poorly to radiation alone, which gives inferior control.",
        "Observing the neck ignores a proven node and the high bilateral nodal risk."
      ],
      "board_pearl": "Atypical carcinoid: supraglottic, male smokers, can raise calcitonin and mimic medullary thyroid cancer. Treat with surgery including the neck.",
      "curveball": "If the biopsy instead showed small cell neuroendocrine carcinoma with nuclear molding and a high Ki-67, how would management change?",
      "curveball_answer": "Small cell NEC is treated like its lung counterpart with platinum-etoposide chemotherapy and radiation rather than primary surgery, because most patients develop distant disease. Systemic staging should include brain imaging, because about 60% have distant disease at presentation, and paraneoplastic syndromes should be sought.",
      "learning_stage": "application",
      "focus": "management"
    },
    {
      "topic": "Nonsquamous Laryngeal Malignancies and SCC Variants",
      "stem": "A 55-year-old woman presents with 1 year of mild hoarseness and a globus sensation. Laryngoscopy shows a smooth, red-blue submucosal mass of the left false vocal fold. Contrast MRI shows an avidly enhancing lesion with flow voids. A junior resident proposes an office cup-forceps biopsy to 'get tissue before the tumor board.' Which is the most appropriate plan?",
      "choices": [
        "Office cup-forceps biopsy to establish histology",
        "Endoscopic piecemeal laser debulking",
        "Somatostatin-receptor imaging, then open excision without biopsy",
        "Total laryngectomy with bilateral neck dissection"
      ],
      "answer": 2,
      "explanation": "A red-blue, avidly enhancing supraglottic submucosal mass with flow voids in a woman is a laryngeal paraganglioma. Biopsy risks brisk, airway-threatening hemorrhage, so diagnosis rests on imaging, including somatostatin-receptor imaging such as DOTATATE PET, which also screens for multicentric disease. Treatment is complete excision through an external approach, typically lateral pharyngotomy, with vascular control. It is benign, so laryngectomy and neck dissection are not needed.",
      "why_wrong": [
        "Office biopsy of a vascular paraganglioma can cause airway-threatening hemorrhage.",
        "Piecemeal endoscopic removal gives poor vascular control and higher recurrence.",
        "Correct.",
        "This benign tumor does not require laryngectomy or neck dissection."
      ],
      "board_pearl": "Laryngeal paraganglioma: women about 3:1, supraglottic, do not biopsy, image with somatostatin-receptor scan, excise via lateral pharyngotomy.",
      "curveball": "Her imaging confirms a solitary paraganglioma. What genetic evaluation should be offered, and why?",
      "curveball_answer": "She should be offered germline testing for succinate dehydrogenase genes (SDHB, SDHC, SDHD and related) and other paraganglioma syndrome genes, as for all head and neck paragangliomas. A pathogenic variant changes surveillance for multifocal and malignant disease and prompts cascade testing of relatives.",
      "learning_stage": "senior_decision",
      "focus": "surgery"
    }
  ],
  "vignettes": [
    {
      "topic": "Nonsquamous Laryngeal Malignancies and SCC Variants",
      "stem": "A 70-year-old man presents with muffled voice and mild dysphagia. Laryngoscopy shows a 2-cm smooth subepithelial mass of the laryngeal surface of the epiglottis. Biopsy shows sheets of monoclonal kappa-restricted plasma cells with amyloid deposits. Bone marrow biopsy, serum and urine protein electrophoresis, free light chains and whole-body imaging are normal. Which is the most appropriate treatment?",
      "choices": [
        "Open supraglottic laryngectomy",
        "Radiation to the primary and first-echelon nodes",
        "Bortezomib-based systemic chemotherapy",
        "Observation with yearly protein electrophoresis"
      ],
      "answer": 1,
      "explanation": "A monoclonal plasma cell tumor of the larynx with a normal marrow, electrophoresis and skeletal survey is a solitary extramedullary plasmacytoma. It is highly radiosensitive, and radiation of about 40-50 Gy to the primary and first-echelon nodes gives local control in most patients while preserving laryngeal function. Surgery is reserved for small, easily excised lesions or radiation failure. Lifelong surveillance is required because about 16-32% progress to multiple myeloma.",
      "why_wrong": [
        "Surgery is reserved for small easily excised lesions or radiation failure and is not standard.",
        "Correct.",
        "Systemic myeloma therapy is for multiple myeloma, which has been excluded by the workup.",
        "An untreated plasmacytoma progresses locally, so surveillance belongs after definitive treatment."
      ],
      "board_pearl": "Extramedullary plasmacytoma: exclude myeloma first, treat with radiation, and follow lifelong for conversion.",
      "curveball": "Why does the amyloid seen on this biopsy matter for his evaluation and follow-up?",
      "curveball_answer": "Amyloid is present in up to 40% of laryngeal plasmacytomas and reflects light-chain production by the clonal plasma cells. It should prompt careful exclusion of systemic AL amyloidosis and myeloma, including free light chains and attention to cardiac and renal symptoms, and continued monitoring for conversion.",
      "learning_stage": "application",
      "focus": "management"
    },
    {
      "topic": "Nonsquamous Laryngeal Malignancies and SCC Variants",
      "stem": "A 60-year-old woman presents with 8 months of progressive dyspnea on exertion and recent hoarseness. Laryngoscopy shows a smooth submucosal subglottic mass narrowing the airway by about 40%. Biopsy shows a cribriform tumor with perineural invasion, consistent with adenoid cystic carcinoma. CT of the neck and chest shows no nodal or distant disease. Which is the most appropriate treatment?",
      "choices": [
        "Elective bilateral modified radical neck dissection",
        "Primary concurrent chemoradiation",
        "Negative-margin resection plus postoperative radiation",
        "Endoscopic debulking and observation"
      ],
      "answer": 2,
      "explanation": "Laryngeal adenoid cystic carcinoma usually arises in the subglottis and spreads submucosally, perineurally and hematogenously rather than to lymph nodes. Treatment is wide resection with negative margins, often total laryngectomy for subglottic disease, followed by postoperative radiation because perineural spread makes clear margins difficult. The neck is dissected only if clinically positive. Chemotherapy has little activity, and follow-up must extend beyond 10 years because lung metastases appear late.",
      "why_wrong": [
        "Nodal metastasis is uncommon in adenoid cystic carcinoma, so elective neck dissection is not standard.",
        "Chemotherapy has little activity in adenoid cystic carcinoma and is not definitive therapy.",
        "Correct.",
        "Debulking leaves gross disease in a tumor known for submucosal and perineural extension."
      ],
      "board_pearl": "Laryngeal adenoid cystic carcinoma: subglottic, perineural, rarely nodal, late lung metastases. Follow for 10 or more years.",
      "curveball": "Seven years later a slowly growing 1-cm lung nodule appears. Is she incurable and in need of immediate chemotherapy?",
      "curveball_answer": "Not necessarily. Pulmonary metastases from adenoid cystic carcinoma often grow slowly, and patients can live many years with them. Observation with serial imaging or metastasectomy for limited disease is reasonable, and systemic therapy is reserved for rapidly progressive or symptomatic disease, ideally within a clinical trial.",
      "learning_stage": "application",
      "focus": "management"
    },
    {
      "topic": "Nonsquamous Laryngeal Malignancies and SCC Variants",
      "stem": "A 68-year-old man who smokes presents with 3 months of hoarseness and intermittent choking. Laryngoscopy shows a 2-cm pedunculated polypoid mass arising from the anterior glottis. Excisional biopsy shows a surface focus of squamous dysplasia overlying a cellular, pleomorphic spindle cell stroma that is only focally positive for cytokeratin. What is the most likely diagnosis?",
      "choices": [
        "Spindle cell (sarcomatoid) carcinoma",
        "Reactive pseudosarcomatous polyp",
        "Laryngeal leiomyosarcoma",
        "Contact granuloma"
      ],
      "answer": 0,
      "explanation": "A polypoid glottic mass in an older smoker with a biphasic pattern, surface squamous dysplasia or carcinoma over a malignant pleomorphic spindle cell stroma, is spindle cell (sarcomatoid) carcinoma, a variant of SCC. The spindle cells are of epithelial origin but often lose keratin expression, so a broad keratin panel and p63 or p40 help. True laryngeal sarcomas are rare. Treatment follows the principles for conventional SCC of the same site and stage.",
      "why_wrong": [
        "Correct.",
        "A reactive polyp lacks malignant pleomorphic spindle cells and an overlying carcinoma component.",
        "True laryngeal sarcomas are rare, and the squamous component plus keratin favor spindle cell carcinoma.",
        "Contact granulomas arise on the posterior vocal process and are not pleomorphic."
      ],
      "board_pearl": "Weak keratin does not exclude spindle cell carcinoma. Use multiple keratins and p63/p40, and treat it as SCC.",
      "curveball": "After excision the margins are negative and the stalk is superficial. What factors determine prognosis in polypoid spindle cell carcinoma?",
      "curveball_answer": "Prognosis depends mainly on depth of invasion and stage rather than the spindle cell histology itself. Superficial, pedunculated glottic tumors have a favorable outlook similar to conventional early glottic SCC, while deeply invasive or sessile tumors and non-glottic sites do worse. Pathologic depth should therefore guide adjuvant decisions.",
      "learning_stage": "foundation",
      "focus": "diagnosis"
    },
    {
      "topic": "Nonsquamous Laryngeal Malignancies and SCC Variants",
      "stem": "A 66-year-old man presents with dysphagia and a right neck mass. Exam shows a 2-cm tumor of the right aryepiglottic fold and a 4-cm ipsilateral level II node, and CT shows a 3-cm liver lesion. Biopsy shows high-grade basaloid cells in lobules with central comedonecrosis, overlying squamous dysplasia, p16 negative and p40 positive. Which statement about this tumor is most accurate?",
      "choices": [
        "It is an indolent SCC variant with low nodal risk",
        "It is a small cell NEC best treated with etoposide",
        "It is a benign adnexal tumor requiring local excision",
        "It is an aggressive SCC variant with early nodal and distant spread"
      ],
      "answer": 3,
      "explanation": "Lobules of high-grade basaloid cells with comedonecrosis, an overlying squamous component and p40 positivity define basaloid squamous cell carcinoma. It favors the supraglottis and piriform sinus and presents at advanced stage, with early regional and distant metastasis. The main histologic pitfall is small cell neuroendocrine carcinoma, separated by p63/p40 positivity and absent neuroendocrine markers. Here the liver lesion should be biopsied because confirming distant disease changes treatment intent.",
      "why_wrong": [
        "Low nodal risk describes verrucous carcinoma, the opposite end of the SCC spectrum.",
        "Small cell NEC lacks a squamous component and p40 positivity and expresses neuroendocrine markers instead.",
        "Benign basaloid adnexal tumors do not produce nodal and hepatic metastases.",
        "Correct."
      ],
      "board_pearl": "Basaloid SCC vs small cell NEC: basaloid is p63/p40 positive with a squamous component; small cell is neuroendocrine positive with nuclear molding.",
      "curveball": "If the liver lesion proves benign, how should treatment of basaloid SCC compare with conventional SCC of the same stage?",
      "curveball_answer": "Stage for stage, basaloid SCC is treated on the same principles as conventional SCC, with surgery or chemoradiation chosen by site and stage. Because of its propensity for early spread, there should be a lower threshold to treat both sides of the neck and thorough systemic staging such as PET-CT before and after treatment.",
      "learning_stage": "senior_decision",
      "focus": "diagnosis"
    }
  ],
}
