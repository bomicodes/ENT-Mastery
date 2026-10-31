"""v491 rewrites: Thyroid / Parathyroid / Salivary (thy1)."""

REWRITES = {'v11_end_01': {'stem': 'A 38-year-old woman notices a fullness in her lower neck while buttoning a shirt. '
                        'She has no hoarseness, dysphagia, or radiation history. Exam shows a 2-cm firm, '
                        'mobile right thyroid nodule without adenopathy. TSH is 1.9 mIU/L. Ultrasound shows '
                        'a 1.8-cm solid hypoechoic nodule with irregular margins and punctate echogenic '
                        'foci, and the lateral neck nodes look normal. What is the best next diagnostic '
                        'step?',
                'choices': ["Iodine-123 scintigraphy to classify the nodule's function",
                            'Repeat neck ultrasound in 6 months to assess for growth',
                            'Diagnostic right lobectomy with intraoperative frozen section',
                            'Ultrasound-guided fine-needle aspiration of the right nodule'],
                'answer': 3,
                'explanation': 'The workup of a nodule starts with TSH and ultrasound. Her TSH is normal, so '
                               'functional imaging has no role, and the sonographic pattern then decides '
                               'biopsy. Solid hypoechoic composition, irregular margins, and punctate '
                               'echogenic foci (microcalcifications reflecting psammoma bodies) define a '
                               'high-suspicion ATA pattern, or ACR TI-RADS TR5, for which FNA is recommended '
                               'at 1 cm or larger. Bethesda-reported cytology then guides observation, '
                               'molecular testing, or surgery and its extent.',
                'why_wrong': ['Scintigraphy is reserved for a low or suppressed TSH; with a normal TSH it '
                              'adds nothing to malignancy risk assessment.',
                              'Interval ultrasound is appropriate for low-suspicion or subcentimeter '
                              'nodules, not a 1.8-cm nodule with a high-suspicion pattern.',
                              'Surgery before cytology skips the step that defines risk and extent, and '
                              'frozen section is unreliable for follicular-patterned lesions.',
                              'Correct.'],
                'board_pearl': 'Normal TSH plus a high-suspicion nodule of 1 cm or more means '
                               'ultrasound-guided FNA, not scintigraphy or surveillance.',
                'curveball': 'FNA returns Bethesda III (atypia of undetermined significance). Which options '
                             'are reasonable for this nodule?',
                'curveball_answer': 'Bethesda III carries an intermediate malignancy risk, so management is '
                                    'individualized. Reasonable options are repeat FNA, molecular testing on '
                                    'the aspirate, diagnostic lobectomy, or surveillance in selected '
                                    'low-risk patients. Her high-suspicion sonographic pattern raises the '
                                    'pretest risk, so a suspicious molecular result or a persistently '
                                    'atypical repeat FNA would favor diagnostic lobectomy rather than '
                                    'surveillance.'},
 'v116-end-01': {'stem': 'A 44-year-old woman has a 1.6-cm solid isoechoic left thyroid nodule with smooth '
                         'margins found on carotid imaging. TSH is normal, she has no radiation exposure or '
                         'family history of thyroid cancer, and the neck nodes are normal. FNA is reported '
                         'as Bethesda III, atypia of undetermined significance. She is anxious but strongly '
                         'prefers to avoid an operation if that is reasonably safe. What is the most '
                         'appropriate next step?',
                 'choices': ['Total thyroidectomy because the cytology is indeterminate',
                             'Repeat FNA or molecular testing of the aspirate to refine risk',
                             'Levothyroxine at a dose that suppresses TSH to shrink the nodule',
                             'Radiofrequency ablation of the nodule under local anesthesia'],
                 'answer': 1,
                 'explanation': 'Bethesda III is truly indeterminate: most such nodules are benign, but the '
                                'risk of malignancy is high enough that dismissal is unwise. With low '
                                'clinical risk features and a strong preference to avoid surgery, the '
                                'guideline-supported next step is repeat FNA or molecular testing on the '
                                'aspirate. A benign-appearing molecular result supports surveillance, while '
                                'a suspicious result or a mutation such as BRAF V600E shifts her toward '
                                'diagnostic lobectomy. The intensity of the next step should match the '
                                'measured risk.',
                 'why_wrong': ['Total thyroidectomy overtreats an indeterminate lesion that is most often '
                               'benign and ignores her stated wish to avoid surgery.',
                               'Correct.',
                               'TSH suppression for benign or indeterminate nodules has minimal effect on '
                               'size and carries cardiac and skeletal risks.',
                               'Thermal ablation is reserved for nodules with benign cytology; ablating an '
                               'indeterminate nodule destroys tissue that may harbor cancer.'],
                 'board_pearl': 'Bethesda III: refine risk with repeat FNA or molecular testing before '
                                'choosing surveillance or diagnostic lobectomy.',
                 'curveball': 'Molecular testing on the repeat aspirate detects a BRAF V600E mutation. How '
                              'does that change her recommendation?',
                 'curveball_answer': 'BRAF V600E is highly specific for papillary carcinoma, so the nodule '
                                     'should be treated as a cancer rather than an indeterminate lesion. '
                                     'Surgery is now recommended. For a 1.6-cm unilateral tumor with normal '
                                     'nodes, lobectomy remains an acceptable low-risk operation under ATA '
                                     '2025, with total thyroidectomy considered if other high-risk features '
                                     'emerge on imaging or pathology.'},
 'v233_tps_nodule_fnd': {'stem': 'A 50-year-old man is seen in clinic after his primary care physician '
                                 'palpated a left neck lump during a routine physical. He has no voice '
                                 'change, dysphagia, palpitations, or weight loss. He had no childhood '
                                 'radiation and no family history of thyroid disease. Exam shows a smooth '
                                 '2-cm left thyroid nodule that moves with swallowing, with no cervical '
                                 'adenopathy. No testing has been done. What is the best initial evaluation?',
                         'choices': ['Serum TSH and dedicated ultrasound of the thyroid and neck',
                                     "Palpation-guided FNA of the nodule during today's visit",
                                     'Serum calcitonin and thyroglobulin as tumor marker screening',
                                     'Contrast-enhanced CT of the neck to define nodule extent'],
                         'answer': 0,
                         'explanation': 'Every newly found thyroid nodule is evaluated first with serum TSH '
                                        'and a dedicated ultrasound of the thyroid and cervical nodes. TSH '
                                        'splits the pathway: a low TSH points to a possible autonomous '
                                        'nodule and scintigraphy, while a normal or high TSH leads to '
                                        'sonographic risk stratification. Ultrasound pattern and size '
                                        'together, using ATA patterns or ACR TI-RADS, then decide whether '
                                        'FNA is indicated, and ultrasound also screens the lateral and '
                                        'central neck for suspicious nodes.',
                         'why_wrong': ['Correct.',
                                       'Palpation-guided FNA before ultrasound misses the risk pattern that '
                                       'sets biopsy thresholds and has a higher nondiagnostic rate.',
                                       'Thyroglobulin does not discriminate benign from malignant nodules, '
                                       'and routine calcitonin screening is not a standard first step.',
                                       'CT does not characterize nodule risk features and its iodinated '
                                       'contrast can delay later radioiodine therapy if cancer is found.'],
                         'board_pearl': 'First step for any thyroid nodule: TSH and a dedicated thyroid and '
                                        'neck ultrasound.',
                         'curveball': 'His TSH returns at 0.08 mIU/L. How does that change the next '
                                      'diagnostic step?',
                         'curveball_answer': 'A low TSH raises the possibility of an autonomously '
                                             'functioning nodule, so radionuclide scintigraphy with '
                                             'iodine-123 or technetium is obtained next. A hot nodule is '
                                             'rarely malignant and usually does not need FNA; management '
                                             'then focuses on hyperthyroidism. If the nodule is cold or '
                                             'isofunctional, he returns to the ultrasound-based FNA '
                                             'pathway.'},
 'v233_tps_nodule_app': {'stem': 'A 33-year-old man has a right thyroid nodule found on a CT angiogram after '
                                 'a motor vehicle collision. He is asymptomatic with normal TSH. Dedicated '
                                 'ultrasound shows a 1.2-cm solid markedly hypoechoic nodule that is taller '
                                 'than wide, with irregular margins and punctate echogenic foci. No abnormal '
                                 'nodes are seen. He asks whether he can simply wait until it reaches 1.5 '
                                 'cm. What is the best next step?',
                         'choices': ['Repeat ultrasound in 12 months',
                                     'FNA only if it reaches 1.5 cm on follow-up',
                                     'Ultrasound-guided FNA now',
                                     'Thyroid lobectomy without prior cytology'],
                         'answer': 2,
                         'explanation': 'Biopsy thresholds scale with sonographic risk. A solid markedly '
                                        'hypoechoic nodule with irregular margins, a taller-than-wide shape, '
                                        'and microcalcifications is high suspicion by ATA criteria and TR5 '
                                        'by ACR TI-RADS, and both systems recommend FNA at 1 cm or larger. '
                                        'At 1.2 cm, this nodule meets the threshold now. The 1.5-cm cutoff '
                                        'he heard about applies to intermediate-suspicion nodules. Cytology '
                                        'establishes risk before surveillance, molecular testing, or surgery '
                                        'is chosen.',
                         'why_wrong': ['A year of surveillance is appropriate for a high-suspicion nodule '
                                       'under 1 cm, but this nodule already exceeds the biopsy threshold.',
                                       'The 1.5-cm threshold applies to intermediate-suspicion (TR4) '
                                       'nodules; high-suspicion nodules are sampled at 1 cm.',
                                       'Correct.',
                                       'Lobectomy without cytology commits him to surgery without knowing '
                                       'whether the nodule is benign or how extensive treatment should be.'],
                         'board_pearl': 'High-suspicion pattern (ATA high or TI-RADS TR5): FNA at 1 cm or '
                                        'larger; intermediate patterns use higher thresholds.',
                         'curveball': 'Ultrasound also shows a 9-mm right level III node with '
                                      'microcalcifications and loss of the fatty hilum. How should it be '
                                      'handled?',
                         'curveball_answer': 'A node with microcalcifications, cystic change, peripheral '
                                             'vascularity, or loss of the fatty hilum should be sampled '
                                             'separately with ultrasound-guided FNA and a thyroglobulin '
                                             'washout of the needle rinse. Confirmed lateral nodal '
                                             'metastasis upgrades staging, mandates total thyroidectomy with '
                                             'therapeutic lateral neck dissection, and changes radioiodine '
                                             'planning, so it must be proven before surgery.'},
 'v233_tps_nodule_snr': {'stem': 'A 72-year-old man with oxygen-dependent COPD and an ejection fraction of '
                                 '25% has a thyroid nodule found on chest CT. He has no neck symptoms, his '
                                 'voice is normal, and TSH is normal. Ultrasound shows a 9-mm solid '
                                 'hypoechoic nodule with irregular margins, well away from the trachea and '
                                 'nerve course, and no abnormal nodes. His cardiologist estimates limited '
                                 'life expectancy. What is the most appropriate management?',
                         'choices': ['Ultrasound-guided FNA so that a diagnosis is established',
                                     'Ultrasound surveillance of the nodule without biopsy for now',
                                     'Lobectomy once he has received cardiology clearance',
                                     'Radiofrequency ablation of the nodule under local anesthesia now'],
                         'answer': 1,
                         'explanation': 'A 9-mm high-suspicion nodule falls below the 1-cm FNA threshold of '
                                        'both ATA and ACR TI-RADS, and even if it were a papillary '
                                        'microcarcinoma, its natural history is usually indolent. His severe '
                                        'cardiopulmonary disease and limited life expectancy mean that '
                                        'biopsy or surgery is unlikely to benefit him. The principle is to '
                                        'sample only when the result would change management. Ultrasound '
                                        'surveillance tracks growth, nodal disease, or invasive features '
                                        'that would alter the plan.',
                         'why_wrong': ['Sampling a subcentimeter nodule rarely changes management when '
                                       'surgery is unlikely to be offered, so the diagnosis has little value '
                                       'here.',
                                       'Correct.',
                                       'Lobectomy exposes a frail patient to anesthetic and cardiopulmonary '
                                       'risk for a lesion unlikely to affect his survival.',
                                       'Ablation without a benign cytologic diagnosis is not standard, and '
                                       'it treats a lesion that does not threaten him.'],
                         'board_pearl': 'Biopsy only when the answer will change management; frailty and '
                                        'life expectancy legitimately lower the intensity of nodule workup.',
                         'curveball': 'Twelve months later the nodule measures 1.4 cm and a new suspicious '
                                      'level IV node has appeared. Does surveillance still make sense?',
                         'curveball_answer': 'New suspicious nodal disease and growth past 1 cm change the '
                                             'risk calculation, so FNA of the node with thyroglobulin '
                                             'washout is reasonable if he remains well enough that a result '
                                             'would alter care. If his condition still precludes surgery, '
                                             'results could guide less invasive options such as targeted '
                                             'radiation or continued observation with comfort-focused goals. '
                                             'The decision should be shared with him and his cardiologist.'},
 'v11_end_02': {'stem': 'A 55-year-old woman has fatigue and constipation. Calcium is 11.1 mg/dL on two '
                        'occasions with normal albumin, and intact PTH is 48 pg/mL (laboratory range 15-65). '
                        'Creatinine and 25-hydroxyvitamin D are normal, and she takes no thiazides or '
                        'lithium. Her 24-hour urine calcium is 290 mg with a calcium-to-creatinine clearance '
                        'ratio of 0.024. Her resident says the PTH is normal. Which interpretation is most '
                        'accurate?',
                'choices': ['A PTH within the reference range excludes a parathyroid source of her '
                            'hypercalcemia',
                            'The normal PTH points toward PTHrP-mediated hypercalcemia of malignancy',
                            'The pattern fits familial hypocalciuric hypercalcemia from a CASR variant',
                            'The PTH is inappropriately unsuppressed, supporting primary '
                            'hyperparathyroidism'],
                'answer': 3,
                'explanation': 'Calcium-sensing receptors on chief cells normally suppress PTH when calcium '
                               'rises, so any measurable mid-range PTH during hypercalcemia is inappropriate '
                               'and indicates PTH-dependent hypercalcemia. With normal renal function, '
                               'replete vitamin D, no confounding drugs, and a clearance ratio above 0.02, '
                               'the most likely diagnosis is primary hyperparathyroidism. Non-PTH causes, '
                               'including malignancy, granulomatous disease, and vitamin D excess, suppress '
                               'PTH. Clinicians must interpret PTH against simultaneous calcium rather than '
                               'against the isolated reference range.',
                'why_wrong': ['Hypercalcemia should drive PTH to low or undetectable levels, so a mid-range '
                              'value is physiologically abnormal rather than reassuring.',
                              'PTHrP-mediated hypercalcemia suppresses intact PTH to low levels; a PTH of 48 '
                              'pg/mL is inconsistent with that mechanism.',
                              'Her calcium-to-creatinine clearance ratio of 0.024 is well above the FHH '
                              'range, which is usually below 0.01.',
                              'Correct.'],
                'board_pearl': "During hypercalcemia, a 'normal' PTH is inappropriately unsuppressed and "
                               'supports primary hyperparathyroidism.',
                'curveball': 'Her urine calcium-to-creatinine clearance ratio had instead been 0.006 and her '
                             'brother has the same labs. What must be excluded before surgery?',
                'curveball_answer': 'Familial hypocalciuric hypercalcemia, usually from an inactivating CASR '
                                    'variant, must be excluded because parathyroidectomy does not cure it. A '
                                    'clearance ratio below 0.01, mild stable hypercalcemia, and affected '
                                    'relatives are typical. Germline CASR testing confirms the diagnosis, '
                                    'and confirmed FHH is generally observed rather than operated on.'},
 'v113-end-05': {'stem': 'A 64-year-old woman has calcium 11.3 mg/dL and intact PTH 104 pg/mL on repeated '
                         'testing, with normal vitamin D and a urine calcium clearance ratio of 0.03. DXA '
                         'shows a lumbar T-score of -2.8. Neck ultrasound and sestamibi SPECT/CT do not '
                         'identify an abnormal gland. Her primary physician wonders whether the diagnosis is '
                         'wrong and asks for guidance. Which interpretation is most accurate?',
                 'choices': ['Negative imaging makes primary hyperparathyroidism unlikely and the labs '
                             'should be repeated',
                             'The negative scans indicate secondary hyperparathyroidism rather than a '
                             'primary disorder',
                             'Surgery should be deferred until a repeat sestamibi scan localizes a gland '
                             'next year',
                             'The diagnosis stands, and she should still be referred to a surgeon for '
                             'parathyroidectomy'],
                 'answer': 3,
                 'explanation': 'Primary hyperparathyroidism is a biochemical diagnosis: reproducible '
                                'hypercalcemia with an elevated or inappropriately unsuppressed PTH after '
                                'mimics such as FHH and vitamin D deficiency are excluded. Localization '
                                'studies are operative road maps. Negative imaging often reflects small '
                                'glands, multigland hyperplasia, or ectopic position, but it does not remove '
                                'the indication. Her osteoporosis meets surgical criteria under the Fifth '
                                'International Workshop guidance, so she should be referred to an '
                                'experienced parathyroid surgeon.',
                 'why_wrong': ['Primary hyperparathyroidism is confirmed by biochemistry; imaging is used '
                               'only to plan the operation, not to establish the diagnosis.',
                               'Secondary hyperparathyroidism is defined by normal or low calcium, whereas '
                               'she has persistent hypercalcemia with high PTH.',
                               'Delaying surgery for imaging leaves her osteoporosis untreated, and an '
                               'experienced surgeon can explore without a localizing study.',
                               'Correct.'],
                 'board_pearl': 'Imaging localizes; biochemistry diagnoses. Negative scans never revoke a '
                                'confirmed diagnosis of primary hyperparathyroidism.',
                 'curveball': 'Which features of her history would push the surgeon toward a planned '
                              'bilateral exploration rather than further imaging first?',
                 'curveball_answer': 'Nonlocalizing imaging, a family history of hypercalcemia or MEN '
                                     'syndromes, young age, lithium use, and a modest PTH elevation '
                                     'suggesting multigland hyperplasia all favor planned four-gland '
                                     'exploration. Many surgeons first obtain 4D CT to look for an ectopic '
                                     'gland, but an experienced surgeon can explore bilaterally without '
                                     'localization and achieves high cure rates in first-time operations.'},
 'v116-end-02': {'stem': 'A 63-year-old man has repeated calcium values near 11.0 mg/dL, intact PTH 92 '
                         'pg/mL, a calcium clearance ratio of 0.028, and a femoral neck T-score of -2.6. '
                         'Ultrasound, sestamibi SPECT/CT, and 4D CT are all nonlocalizing. He has never had '
                         'neck surgery and has no family history of hypercalcemia. He is fit for anesthesia '
                         'and wants a definitive treatment. What is the most appropriate operative plan?',
                 'choices': ['Bilateral four-gland exploration by an experienced parathyroid surgeon',
                             'Focused exploration on the side where his thyroid appears larger',
                             'Selective venous sampling for PTH before any neck exploration',
                             'Cinacalcet indefinitely because the operation cannot be targeted'],
                 'answer': 0,
                 'explanation': 'He has confirmed primary hyperparathyroidism with osteoporosis, a clear '
                                'surgical indication, and imaging that does not localize. Negative imaging '
                                'raises the probability of multigland hyperplasia or a small or ectopic '
                                'adenoma, which is exactly why a focused approach is inappropriate. '
                                'Bilateral exploration with identification of all four glands by an '
                                'experienced surgeon cures most first-time patients, often with '
                                'intraoperative PTH as an adjunct. Invasive localization such as venous '
                                'sampling is held for reoperation.',
                 'why_wrong': ['Correct.',
                               'Thyroid asymmetry does not predict the location of an abnormal parathyroid, '
                               'and a blind unilateral approach risks missed disease.',
                               'Venous sampling is invasive and is generally reserved for reoperative cases '
                               'after failed exploration, not first-time surgery.',
                               'Cinacalcet lowers calcium but does not improve bone density or cure the '
                               'disease, so it is inferior to surgery in a fit patient.'],
                 'board_pearl': 'Nonlocalizing imaging in first-time PHPT with a surgical indication: '
                                'bilateral four-gland exploration, not abandoning surgery.',
                 'curveball': 'During exploration, all four glands appear normal in size. Where should the '
                              'surgeon look for a missing adenoma?',
                 'curveball_answer': 'Common ectopic sites follow embryology. Inferior glands derive from '
                                     'the third pouch and can lie in the thymus, thyrothymic ligament, or '
                                     'high in the carotid sheath. Superior glands derive from the fourth '
                                     'pouch and can sit in the tracheoesophageal groove or retroesophageal '
                                     'space. The surgeon also checks for intrathyroidal glands, often with '
                                     'transcervical thymectomy, before closing and re-imaging if PTH stays '
                                     'high.'},
 'v233_tps_php_fnd': {'stem': 'A 47-year-old man presents with an obstructing left ureteral stone. Calcium '
                              'is 11.0 mg/dL on three occasions, phosphate is 2.3 mg/dL, and intact PTH is '
                              '95 pg/mL. Creatinine is normal, 25-hydroxyvitamin D is 34 ng/mL, and 24-hour '
                              'urine calcium is 340 mg with a clearance ratio of 0.03. He takes no '
                              'medications and has no family history of hypercalcemia. What is the most '
                              'likely diagnosis?',
                      'choices': ['Familial hypocalciuric hypercalcemia',
                                  'Secondary hyperparathyroidism from vitamin D deficiency',
                                  'Primary hyperparathyroidism',
                                  'Humoral hypercalcemia of malignancy'],
                      'answer': 2,
                      'explanation': 'Reproducible hypercalcemia with an elevated PTH, low phosphate, and '
                                     'hypercalciuria is the classic picture of primary hyperparathyroidism. '
                                     'PTH increases distal tubular calcium reabsorption, but the filtered '
                                     'calcium load is so high that urine calcium rises, which promotes '
                                     'stones; PTH also reduces proximal phosphate reabsorption. The workup '
                                     'confirms the phenotype and excludes mimics: replete vitamin D, normal '
                                     'renal function, no thiazide or lithium exposure, and a clearance ratio '
                                     'above 0.02 that argues against FHH.',
                      'why_wrong': ['FHH causes low urinary calcium with a clearance ratio usually below '
                                    '0.01, whereas his urine calcium is elevated.',
                                    'His vitamin D is replete, and secondary hyperparathyroidism produces '
                                    'normal or low calcium rather than hypercalcemia.',
                                    'Correct.',
                                    'Humoral hypercalcemia is mediated by PTHrP and suppresses intact PTH, '
                                    'which is elevated in this patient.'],
                      'board_pearl': 'High calcium plus high or unsuppressed PTH, after excluding FHH and '
                                     'drug causes, equals primary hyperparathyroidism.',
                      'curveball': 'How does urinary calcium help distinguish primary hyperparathyroidism '
                                   'from familial hypocalciuric hypercalcemia?',
                      'curveball_answer': 'In FHH an inactivating CASR variant makes the kidney treat high '
                                          'calcium as normal, so tubular calcium reabsorption stays high and '
                                          'urine calcium is low. A calcium-to-creatinine clearance ratio '
                                          'below 0.01 strongly suggests FHH, above 0.02 favors primary '
                                          'hyperparathyroidism, and intermediate values warrant genetic '
                                          'testing. Vitamin D deficiency and thiazides can lower urine '
                                          'calcium and confuse the ratio.'},
 'v233_tps_php_app': {'stem': 'A 59-year-old woman with biochemically confirmed primary hyperparathyroidism '
                              'has passed two kidney stones in 3 years. Calcium is 11.2 mg/dL, eGFR is 74 '
                              'mL/min, and DXA shows a distal radius T-score of -2.9. Ultrasound and '
                              'sestamibi concordantly show a right inferior adenoma. She is otherwise '
                              'healthy and asks whether she could simply take medication instead of having '
                              'an operation. What is the best management?',
                      'choices': ['Parathyroidectomy',
                                  'Cinacalcet titrated to normalize serum calcium',
                                  'Oral bisphosphonate with annual calcium and DXA monitoring',
                                  'Observation with hydration and a low-calcium diet'],
                      'answer': 0,
                      'explanation': 'She has end-organ disease from primary hyperparathyroidism: recurrent '
                                     'nephrolithiasis and osteoporosis at the distal radius, a cortical site '
                                     'preferentially affected by PTH. Either feature meets surgical criteria '
                                     'under the Fifth International Workshop guidance. Parathyroidectomy is '
                                     'the only curative therapy, reduces stone recurrence, and improves bone '
                                     'density. Concordant imaging allows a focused approach with '
                                     'intraoperative PTH. Medical therapy is reserved for patients who '
                                     'cannot or will not undergo surgery.',
                      'why_wrong': ['Correct.',
                                    'Cinacalcet lowers calcium but does not improve bone density or reliably '
                                    'prevent stones, so it is reserved for patients unfit for surgery.',
                                    'Bisphosphonates help bone density but leave hypercalcemia and the stone '
                                    'risk untreated, and they do not cure the disease.',
                                    'Calcium restriction can raise PTH further and worsen bone loss, and '
                                    'observation is inappropriate once end-organ disease is present.'],
                      'board_pearl': 'Stones, osteoporosis, eGFR below 60, or calcium more than 1 mg/dL '
                                     'above normal each justify parathyroidectomy.',
                      'curveball': 'Why is the distal one-third radius site often the most abnormal on DXA '
                                   'in primary hyperparathyroidism?',
                      'curveball_answer': 'PTH excess preferentially resorbs cortical bone, while relatively '
                                          'sparing cancellous bone, so the distal one-third radius, which is '
                                          'mostly cortical, often shows the lowest T-score. The lumbar '
                                          'spine, which is mainly trabecular, may look relatively preserved. '
                                          'DXA should therefore include the forearm, and a low radius score '
                                          'alone meets the osteoporosis criterion for surgery.'},
 'v233_tps_php_snr': {'stem': 'A 52-year-old man has biochemically confirmed primary hyperparathyroidism '
                              'with calcium 11.5 mg/dL and a kidney stone. Ultrasound shows a hypoechoic '
                              'nodule posterior to the right lower thyroid pole, while sestamibi SPECT/CT '
                              'shows focal uptake behind the left upper pole. 4D CT is equivocal. He has no '
                              'family history and no prior neck surgery. What is the most appropriate '
                              'operative strategy?',
                      'choices': ['Focused right inferior exploration based on the ultrasound alone',
                                  'Postpone surgery until repeat imaging becomes concordant',
                                  'Bilateral exploration guided by intraoperative PTH monitoring',
                                  'Selective venous sampling before a first-time operation'],
                      'answer': 2,
                      'explanation': 'Concordant ultrasound and sestamibi justify a focused approach because '
                                     'they predict a single adenoma. Discordant studies lower that '
                                     'confidence and raise the chance of double adenoma or multigland '
                                     'disease. The diagnosis is already biochemical and the surgical '
                                     'indication is clear, so the right response is a strategy that '
                                     'tolerates uncertainty: bilateral exploration in which both candidate '
                                     'sites are examined, with intraoperative PTH used to confirm cure. Some '
                                     'surgeons begin on one side but should plan to convert.',
                      'why_wrong': ['Focusing on one study when the other points elsewhere risks missing a '
                                    'second adenoma or the true lesion, so a single-gland approach is '
                                    'unreliable.',
                                    'Waiting for concordance delays surgery for a patient who already has '
                                    'nephrolithiasis, and repeat imaging may remain discordant.',
                                    'Correct.',
                                    'Venous sampling is invasive and generally reserved for reoperative '
                                    'cases after failed or nonlocalizing first explorations.'],
                      'board_pearl': 'Discordant localization reduces confidence in a single adenoma; plan '
                                     'bilateral exploration with intraoperative PTH rather than a focused '
                                     'operation.',
                      'curveball': 'Which history features should raise concern for multigland or hereditary '
                                   'disease in this man?',
                      'curveball_answer': 'Onset before age 30 to 40, relatives with hypercalcemia, '
                                          'pituitary or pancreatic tumors suggesting MEN1, medullary '
                                          'carcinoma or pheochromocytoma suggesting MEN2A, jaw tumors '
                                          'suggesting CDC73 disease, lithium therapy, and prior failed '
                                          'exploration all raise concern. Any of these should prompt genetic '
                                          'evaluation and a planned four-gland operation rather than a '
                                          'focused one.'},
 'v11_end_03': {'stem': 'A 34-year-old woman has a 2-cm left thyroid nodule. FNA shows spindle and '
                        'plasmacytoid cells with salt-and-pepper chromatin, and serum calcitonin is 640 '
                        'pg/mL. Germline testing returns a RET codon 634 variant. She reports occasional '
                        'pounding headaches and palpitations, and her blood pressure is 152/96 mm Hg. Neck '
                        'ultrasound shows no suspicious nodes. Thyroidectomy is being scheduled. What '
                        'evaluation must be completed first?',
                'choices': ['Plasma free metanephrine levels',
                            'Serum thyroglobulin level',
                            'Iodine-123 whole-body scan',
                            '24-hour urine 5-hydroxyindoleacetic acid'],
                'answer': 0,
                'explanation': 'Codon 634 RET variants cause MEN2A, which carries a high risk of '
                               'pheochromocytoma and primary hyperparathyroidism. Her headaches, '
                               'palpitations, and hypertension heighten concern. An unrecognized '
                               'pheochromocytoma can cause a fatal hypertensive crisis during anesthesia '
                               'induction or thyroid manipulation, so revised ATA medullary carcinoma '
                               'guidance requires plasma free or urinary fractionated metanephrines before '
                               'thyroidectomy. Serum calcium and PTH are checked at the same time to detect '
                               'parathyroid disease that can be addressed during the neck operation.',
                'why_wrong': ['Correct.',
                              'Thyroglobulin is a marker of follicular-cell tissue and has no role in '
                              'diagnosing or following medullary carcinoma.',
                              'Medullary carcinoma arises from C cells that do not concentrate iodine, so '
                              'radioiodine imaging has no staging or treatment role.',
                              'Urine 5-HIAA screens for carcinoid syndrome; her symptoms in the setting of '
                              'MEN2A point to a catecholamine-secreting tumor instead.'],
                'board_pearl': 'Before thyroidectomy for MEN2 medullary carcinoma, exclude pheochromocytoma '
                               'with metanephrines; if present, the adrenal comes first.',
                'curveball': 'Her plasma metanephrines are markedly elevated and MRI shows a 3-cm left '
                             'adrenal mass. What is the sequence of treatment?',
                'curveball_answer': 'The pheochromocytoma is treated first. She needs alpha blockade, such '
                                    'as phenoxybenzamine or doxazosin, for 1 to 2 weeks with liberal salt '
                                    'and fluids, adding a beta blocker only after alpha blockade is '
                                    'established, followed by laparoscopic adrenalectomy. Thyroidectomy with '
                                    'central neck dissection follows once she has recovered, because '
                                    'operating on the neck first risks an intraoperative catecholamine '
                                    'crisis.'},
 'v141_tps_03': {'stem': 'A 58-year-old man has a 2.6-cm right thyroid nodule with FNA showing medullary '
                         'carcinoma and calcitonin of 410 pg/mL. He has no family history of thyroid cancer, '
                         'endocrine tumors, or early deaths, and he is normotensive. He asks whether genetic '
                         'testing is worthwhile, since nobody in his family has had this cancer. Which '
                         'evaluation is required before thyroidectomy?',
                 'choices': ['Somatic RET sequencing of the FNA material alone',
                             'Germline RET testing and plasma free metanephrines',
                             'Germline RET testing deferred until final pathology',
                             'Serum thyroglobulin and an iodine-123 uptake scan'],
                 'answer': 1,
                 'explanation': 'Roughly one in four medullary carcinomas is hereditary, and a meaningful '
                                'proportion of apparently sporadic cases carry de novo or unrecognized '
                                'germline RET variants. A negative family history is therefore not '
                                'reassuring, and every patient with medullary carcinoma should be offered '
                                'germline RET testing. Because hereditary disease is possible until testing '
                                'returns, pheochromocytoma is excluded biochemically before surgery. '
                                'Calcitonin and CEA establish the baseline tumor burden and guide the extent '
                                'of imaging.',
                 'why_wrong': ['Somatic sequencing identifies tumor mutations useful for systemic therapy '
                               'but cannot tell whether he carries a heritable variant.',
                               'Correct.',
                               'Waiting until after surgery risks operating on an unrecognized '
                               'pheochromocytoma and delays cascade testing of his relatives.',
                               'Thyroglobulin and radioiodine imaging reflect follicular-cell biology and '
                               'are irrelevant to C-cell-derived medullary carcinoma.'],
                 'board_pearl': 'Every medullary thyroid carcinoma gets germline RET testing, regardless of '
                                'family history, and metanephrines before surgery.',
                 'curveball': 'How does his calcitonin level of 410 pg/mL influence nodal and distant '
                              'staging before surgery?',
                 'curveball_answer': 'Basal calcitonin correlates with tumor burden. Ultrasound of the '
                                     'central and lateral neck is mandatory for all patients. Revised ATA '
                                     'guidance recommends cross-sectional imaging for distant disease, such '
                                     'as CT of the neck and chest and liver MRI or multiphase CT, when '
                                     'calcitonin exceeds about 500 pg/mL or there is extensive nodal '
                                     'disease. At 410 pg/mL, careful neck imaging is the priority.'},
 'v233_tps_mtc_fnd': {'stem': 'A 47-year-old woman underwent total thyroidectomy with central neck '
                              'dissection for sporadic medullary carcinoma 3 months ago. Pathology showed a '
                              '2.2-cm tumor and one of 14 central nodes involved. She feels well, her voice '
                              'and calcium are normal, and she is on levothyroxine. The fellow drafting her '
                              'surveillance plan asks which blood tests should be trended over time. Which '
                              'serum markers are most appropriate?',
                      'choices': ['Thyroglobulin and anti-thyroglobulin antibodies',
                                  'Stimulated thyroglobulin after recombinant TSH',
                                  'Alpha-fetoprotein and beta-hCG',
                                  'Calcitonin and CEA'],
                      'answer': 3,
                      'explanation': 'Medullary carcinoma arises from parafollicular C cells, derived from '
                                     'neural crest via the ultimobranchial body, which secrete calcitonin '
                                     'and frequently CEA. These markers are measured about 3 months after '
                                     'surgery and then serially. An undetectable calcitonin suggests '
                                     'biochemical cure, while rising values prompt imaging. Calcitonin and '
                                     'CEA doubling times are among the strongest predictors of progression '
                                     'and survival. Thyroglobulin and radioiodine, central to follow-up of '
                                     'differentiated cancer, play no role.',
                      'why_wrong': ['Thyroglobulin is made by follicular cells, so it tracks differentiated '
                                    'thyroid cancer rather than C-cell tumors.',
                                    'TSH stimulation increases thyroglobulin output from follicular tissue '
                                    'and has no effect on medullary tumor marker secretion.',
                                    'Alpha-fetoprotein and beta-hCG are germ cell and hepatocellular tumor '
                                    'markers with no role in medullary carcinoma.',
                                    'Correct.'],
                      'board_pearl': 'Medullary carcinoma is followed with calcitonin and CEA doubling '
                                     'times; thyroglobulin and radioiodine play no role.',
                      'curveball': 'Why does medullary carcinoma not respond to radioactive iodine the way '
                                   'papillary carcinoma can?',
                      'curveball_answer': 'Radioiodine works because follicular-derived cells express the '
                                          'sodium-iodide symporter and organify iodine under TSH control. C '
                                          'cells lack this iodine-handling machinery and are not TSH-driven, '
                                          'so medullary tumors do not concentrate iodine. Neither '
                                          'radioiodine nor TSH suppression helps. Persistent disease is '
                                          'managed with surgery, external radiation for selected sites, or '
                                          'RET-selective and multikinase inhibitors.'},
 'v233_tps_mtc_app': {'stem': 'A 39-year-old woman has just undergone total thyroidectomy for medullary '
                              'carcinoma, and germline testing shows a pathogenic RET variant in codon 634. '
                              'Her metanephrines and calcium were normal. She has two children, aged 3 and '
                              '7, and a younger sister, none of whom have been tested. She asks what this '
                              'result means for her family. What is the most appropriate recommendation?',
                      'choices': ['Annual calcitonin screening of her children starting at puberty, without '
                                  'genetic testing',
                                  'Genetic testing of relatives only if one of them develops a thyroid '
                                  'nodule on exam',
                                  'Targeted RET testing of her children and sister, with prophylactic '
                                  'thyroidectomy timed by risk',
                                  'Neck ultrasound for her relatives every year, with thyroidectomy if a '
                                  'nodule appears'],
                      'answer': 2,
                      'explanation': 'Hereditary medullary carcinoma is autosomal dominant with '
                                     'near-complete penetrance, so each child has a 50% risk. Revised ATA '
                                     'guidance recommends targeted testing of first-degree relatives, '
                                     'ideally early in childhood for high-risk variants. Codon 634 is high '
                                     'risk, and carriers should have thyroidectomy at or before age 5, timed '
                                     'by calcitonin levels. The highest-risk M918T variant of MEN2B warrants '
                                     'surgery in the first year of life. Carriers also need lifelong '
                                     'pheochromocytoma and hyperparathyroidism screening.',
                      'why_wrong': ['Calcitonin screening without genotyping misses the window for '
                                    'prevention, and codon 634 carriers can develop cancer in early '
                                    'childhood.',
                                    'Waiting for a palpable nodule means waiting for established cancer, '
                                    'which defeats the purpose of identifying carriers early.',
                                    'Correct.',
                                    'Ultrasound detects established tumors, whereas prophylactic surgery in '
                                    'carriers is intended to remove the thyroid before cancer develops.'],
                      'board_pearl': 'Germline RET result: cascade-test relatives and time prophylactic '
                                     'thyroidectomy by codon risk level and calcitonin.',
                      'curveball': 'What endocrine condition must be excluded in a RET carrier before '
                                   'prophylactic thyroidectomy, and from what age?',
                      'curveball_answer': 'Pheochromocytoma must be excluded with plasma free or urinary '
                                          'fractionated metanephrines before any thyroid surgery. For '
                                          'high-risk variants such as codon 634 and M918T, screening starts '
                                          'by age 11; for moderate-risk variants it starts by age 16. If a '
                                          'pheochromocytoma is found, alpha blockade and adrenalectomy '
                                          'precede thyroidectomy.'},
 'v233_tps_mtc_snr': {'stem': 'A 46-year-old man has a 3.4-cm right thyroid mass with FNA showing medullary '
                              'carcinoma. Calcitonin is 780 pg/mL and CEA is mildly elevated. Germline RET '
                              'testing and metanephrines are negative. Ultrasound with FNA confirms '
                              'metastases in right levels III and IV, and the left neck appears normal. CT '
                              'of the chest and liver MRI show no distant disease. What is the most '
                              'appropriate operation?',
                      'choices': ['Total thyroidectomy with central and right lateral neck dissections',
                                  'Total thyroidectomy with excision of the enlarged right nodes only',
                                  'Total thyroidectomy and central neck dissection followed by radioiodine',
                                  'Right lobectomy with right central and right lateral neck dissection'],
                      'answer': 0,
                      'explanation': 'Surgery is the only curative treatment for medullary carcinoma, which '
                                     'often spreads early to central and lateral nodes and does not respond '
                                     'to radioiodine. With distant disease excluded, the operation is total '
                                     'thyroidectomy with central (level VI) dissection and a '
                                     'compartment-oriented lateral neck dissection of levels II through V on '
                                     'the involved side. Extensive staging was done first because calcitonin '
                                     'exceeded 500 pg/mL. Contralateral lateral dissection in a clinically '
                                     'negative neck remains debated.',
                      'why_wrong': ['Correct.',
                                    'Node-picking leaves microscopic disease in the compartment and raises '
                                    'recurrence and reoperation risk in a disease that relies on surgery.',
                                    'Radioiodine is ineffective because C cells do not concentrate iodine, '
                                    'so leaving the lateral neck to adjuvant therapy fails him.',
                                    'Lobectomy leaves contralateral C cells and possible multifocal disease, '
                                    'and medullary carcinoma requires total thyroidectomy.'],
                      'board_pearl': 'Medullary carcinoma with lateral nodes: total thyroidectomy plus '
                                     'central and compartment-oriented lateral dissection, never '
                                     'node-picking.',
                      'curveball': 'If CT had shown multiple liver and lung metastases, how would the neck '
                                   'operation change?',
                      'curveball_answer': 'With distant metastases, the goal shifts from cure to local '
                                          'control with minimal morbidity. Less aggressive neck surgery that '
                                          'preserves voice, swallowing, and parathyroid function is favored, '
                                          'aimed at preventing airway or nerve compromise. Systemic therapy '
                                          'with a RET-selective inhibitor if a somatic RET variant is '
                                          'present, or a multikinase inhibitor, is reserved for progressive '
                                          'or symptomatic disease.'},
 'v11_end_04': {'stem': 'A 45-year-old man has recurrent painful swelling under the left mandible that '
                        'starts within minutes of eating and settles over an hour. Bimanual palpation '
                        'reveals a hard mobile mass in the anterior floor of mouth just behind the left '
                        'papilla, and the gland is soft between episodes. CT shows a 5-mm stone in the '
                        'distal Wharton duct and no abscess. What is the most appropriate initial procedure?',
                'choices': ['Transcervical submandibular gland excision under general anesthesia',
                            'Extracorporeal shock wave lithotripsy as a series of sessions',
                            'Transoral sialodochotomy over the stone with duct marsupialization',
                            'Long-term sialogogues and gland massage with antibiotics as needed'],
                'answer': 2,
                'explanation': 'Most salivary stones arise in the submandibular gland because its saliva is '
                               'alkaline and mucin-rich and Wharton duct runs a long uphill course. A '
                               'palpable stone in the distal duct is anterior to where the lingual nerve '
                               'crosses the duct and can be removed safely through a transoral incision over '
                               'the stone, with the duct marsupialized to prevent stricture. This approach '
                               'preserves the gland, which usually recovers function once obstruction is '
                               'relieved. Gland excision is held for failure.',
                'why_wrong': ['Gland excision sacrifices a functioning gland and adds marginal mandibular, '
                              'lingual, and hypoglossal nerve risk for an easily reached stone.',
                              'Lithotripsy is not widely available in the United States and is less '
                              'efficient than direct removal for a palpable distal stone.',
                              'Correct.',
                              'Conservative measures rarely clear an impacted 5-mm stone, and repeated '
                              'obstruction can lead to recurrent infection and gland damage.'],
                'board_pearl': 'Palpable distal Wharton duct stone: transoral sialodochotomy preserves the '
                               'gland and avoids the cervical approach.',
                'curveball': 'The stone is instead 12 mm and sits at the hilum. How does location change the '
                             'approach?',
                'curveball_answer': 'Large hilar stones are beyond the reach of simple distal sialodochotomy '
                                    'and too big for basket retrieval alone. They are typically treated with '
                                    'a combined approach: sialendoscopy localizes the stone and a transoral '
                                    'posterior floor-of-mouth incision removes it, with the lingual nerve '
                                    'identified and protected. Laser or pneumatic intracorporeal lithotripsy '
                                    'can fragment it, and gland excision remains a fallback.'},
 'v116-end-03': {'stem': 'A 38-year-old woman has 6 months of left submandibular swelling with meals. The '
                         'floor of mouth is normal to bimanual palpation, the gland is soft and nontender, '
                         'and clear saliva flows from the left papilla. Ultrasound shows a 4-mm mobile '
                         'echogenic focus with acoustic shadowing in the mid portion of Wharton duct and '
                         'mild proximal ductal dilation. What is the most gland-preserving management?',
                 'choices': ['Submandibular gland excision through a cervical incision',
                             'Sialendoscopy with wire-basket retrieval of the stone',
                             'Transoral incision over the expected stone position by palpation',
                             'Continued sialogogues, massage, and hydration alone'],
                 'answer': 1,
                 'explanation': 'Small mobile stones of about 4 to 5 mm or less within the submandibular '
                                'duct are ideal for interventional sialendoscopy. The endoscope enters '
                                'through the papilla, visualizes the stone directly, and retrieves it with a '
                                'wire basket or microforceps. When stones are not palpable, endoscopy avoids '
                                'a blind incision. Success rates are high for small mobile stones, and gland '
                                'function generally recovers, which is why sialendoscopy has largely '
                                'replaced excision for such disease.',
                 'why_wrong': ['Excision removes a gland that still functions and is reserved for stones '
                               'that cannot be cleared by duct-preserving methods.',
                               'Correct.',
                               'A nonpalpable mid-duct stone cannot be located reliably by a blind incision, '
                               'which also risks the lingual nerve and duct stricture.',
                               'Six months of recurrent obstruction shows conservative care has failed, and '
                               'a stone of this size is unlikely to pass spontaneously.'],
                 'board_pearl': 'Small mobile ductal stones are best handled by sialendoscopic basket '
                                'retrieval, which spares the gland.',
                 'curveball': 'How would the plan change for a large hilar or intraparenchymal stone?',
                 'curveball_answer': 'Stones over about 5 to 6 mm at the hilum are usually too large for '
                                     'basket extraction and need a combined endoscopic and transoral '
                                     'approach or intracorporeal lithotripsy. Truly intraparenchymal stones '
                                     'beyond the hilum, or a gland destroyed by chronic infection, generally '
                                     'require transcervical submandibular gland excision.'},
 'v235_tps_smstone_fnd': {'stem': 'A 29-year-old man has had five episodes in 4 months of painful swelling '
                                  'below the right jaw that begins as he starts eating and resolves over 2 '
                                  'hours. He has no fever, weight loss, or dry mouth. Between episodes, '
                                  'bimanual palpation finds a hard, gritty, mobile focus along the right '
                                  'floor of mouth, and the submandibular gland is mildly firm. Milking the '
                                  'gland produces scant saliva. What is the most likely diagnosis?',
                          'choices': ['Plunging ranula',
                                      'Submandibular sialolithiasis',
                                      'Pleomorphic adenoma of the submandibular gland',
                                      'Submandibular space abscess'],
                          'answer': 1,
                          'explanation': 'Mealtime swelling and pain that subsides over hours is the '
                                         'hallmark of salivary duct obstruction: secretion stimulated by '
                                         'eating meets a blocked duct and the gland distends. A hard, gritty '
                                         'mobile focus along Wharton duct on bimanual palpation confirms a '
                                         'calculus. The submandibular gland accounts for most salivary '
                                         'stones because its saliva is alkaline, viscous, and calcium-rich '
                                         'and its duct is long and runs upward against gravity. Ultrasound '
                                         "confirms the stone's size and position.",
                          'why_wrong': ['A plunging ranula is a painless soft cystic swelling from the '
                                        'sublingual gland that does not fluctuate with meals or contain a '
                                        'hard focus.',
                                        'Correct.',
                                        'Pleomorphic adenoma causes a slowly enlarging painless mass that '
                                        'does not swell and recede with eating.',
                                        'An abscess causes constant pain, fever, and induration, not brief '
                                        'meal-provoked swelling with complete resolution between episodes.'],
                          'board_pearl': 'Meal-provoked swelling that resolves over hours equals obstructive '
                                         'sialadenitis; feel along Wharton duct for the stone.',
                          'curveball': 'Which stone locations are most accessible to transoral removal '
                                       'versus endoscopic or combined approaches?',
                          'curveball_answer': 'Palpable stones in the distal duct near the papilla are '
                                              'removed transorally through a simple incision. Small mobile '
                                              'stones anywhere in the duct suit sialendoscopic basket '
                                              'retrieval. Larger stones at the hilum generally need a '
                                              'combined endoscopic and transoral approach with lingual nerve '
                                              'protection, and intraglandular stones beyond the hilum '
                                              'usually require gland excision.'},
 'v235_tps_smstone_app': {'stem': 'A 36-year-old woman was admitted 3 weeks ago with acute suppurative left '
                                  'submandibular sialadenitis, treated with intravenous antibiotics and '
                                  'hydration. She is now pain-free with no fever, and the gland is soft. '
                                  'Ultrasound shows a 4-mm stone in the proximal Wharton duct with mild '
                                  'ductal dilation, preserved glandular echotexture, and no abscess. She is '
                                  'told by a friend that the gland must come out after an infection. What is '
                                  'the most appropriate next step?',
                          'choices': ['Submandibular gland excision because the gland has been infected',
                                      'Elective sialendoscopic stone removal now that inflammation has '
                                      'settled',
                                      'Repeat antibiotic courses with each new episode of swelling',
                                      'Sialendoscopy at the next acute infection to drain pus from the duct'],
                          'answer': 1,
                          'explanation': 'The submandibular gland usually recovers secretory function after '
                                         'an obstructing stone is removed, even after an episode of '
                                         'suppurative sialadenitis. Ultrasound showing preserved parenchyma '
                                         'supports gland preservation. Interventional sialendoscopy is best '
                                         'performed electively once acute inflammation has resolved, when '
                                         'the duct is less friable and visualization is better. A small '
                                         'mobile stone like this is well suited to basket retrieval. Gland '
                                         'excision is reserved for failure of gland-preserving techniques or '
                                         'an atrophic gland.',
                          'why_wrong': ['A single infection does not mean the gland is destroyed; preserved '
                                        'echotexture predicts recovery once the stone is removed.',
                                        'Correct.',
                                        'Antibiotics treat episodes but leave the obstructing stone in '
                                        'place, so infections and gland damage will keep recurring.',
                                        'Endoscopy during acute infection is technically harder and risks '
                                        'duct perforation and spread, so it is performed once the gland is '
                                        'quiet.'],
                          'board_pearl': 'Treat the acute infection first, then remove the stone electively '
                                         'with gland-preserving sialendoscopy.',
                          'curveball': 'At sialendoscopy the stone is fixed to the duct wall and will not '
                                       'engage the basket. What are the options?',
                          'curveball_answer': 'A fixed or impacted stone can be fragmented with holmium '
                                              'laser or pneumatic intracorporeal lithotripsy and the '
                                              'fragments removed, or the stone can be localized '
                                              'endoscopically and removed through a small transoral incision '
                                              'in a combined approach. A stent placed afterward reduces '
                                              'stricture. Gland excision is considered only if these '
                                              'techniques fail.'},
 'v235_tps_smstone_snr': {'stem': 'A 50-year-old man has had three infections of the right submandibular '
                                  'gland in a year. CT shows a 10-mm stone impacted at the duct hilum. '
                                  'Ultrasound shows preserved glandular parenchyma, and saliva flows after '
                                  'the stone is pushed. Sialendoscopy confirms the stone but it is too large '
                                  'for basket retrieval. He works as a singer and wants to keep the gland if '
                                  'reasonable. What is the best approach?',
                          'choices': ['Combined sialendoscopic and transoral hilar stone extraction',
                                      'Submandibular gland excision as the first definitive procedure',
                                      'Repeated attempts to crush the stone blindly with forceps',
                                      'Extracorporeal shock wave lithotripsy followed by observation'],
                          'answer': 0,
                          'explanation': 'Large impacted hilar stones combine endoscopic localization with '
                                         'transoral access. Transillumination guides an incision in the '
                                         'posterior floor of mouth, the stone is delivered, and the duct is '
                                         'repaired or stented. Gland preservation is reasonable because '
                                         'function often recovers after stone clearance, as suggested by his '
                                         'preserved parenchyma and salivary flow. He should be counseled '
                                         'that submandibular excision remains necessary if the stone cannot '
                                         'be cleared safely or symptoms persist.',
                          'why_wrong': ['Correct.',
                                        'Excision is a reasonable fallback but discards a gland with '
                                        'preserved parenchyma that can recover after the stone is cleared.',
                                        'Blind crushing without endoscopic visualization risks duct '
                                        'perforation and lingual nerve injury and often leaves fragments '
                                        'behind.',
                                        'Lithotripsy alone is less effective for large impacted hilar stones '
                                        'and is not widely available in the United States.'],
                          'board_pearl': 'Large hilar submandibular stone: combined endoscopic-transoral '
                                         'removal first, gland excision as fallback.',
                          'curveball': 'Where is the lingual nerve relative to Wharton duct during a '
                                       'transoral hilar approach?',
                          'curveball_answer': 'The lingual nerve lies lateral and superior to the duct '
                                              'posteriorly, then loops beneath it from lateral to medial '
                                              'near the second molar, ending medial to the duct anteriorly. '
                                              'The posterior floor of mouth, where hilar stones sit, is '
                                              'therefore its zone of greatest risk. The surgeon identifies '
                                              'and retracts the nerve before incising the duct, usually '
                                              'dissecting medial to the sublingual gland.'},
 'v425-sialolithiasis-parotid-open-01': {'stem': 'A 45-year-old woman has recurrent swelling of the right '
                                                 'cheek during meals. CT shows a 3-mm stone in the mid '
                                                 'portion of Stensen duct over the masseter muscle. '
                                                 'Sialendoscopy is attempted, but a tight bend and a '
                                                 'stricture prevent the scope from reaching the stone. The '
                                                 'surgeon briefly considers an external transfacial incision '
                                                 'directly over the stone. Which structure is chiefly at '
                                                 'risk with that external approach?',
                                         'choices': ['Lingual nerve at the floor of mouth',
                                                     'Marginal mandibular branch of the facial nerve',
                                                     'Buccal branches of the seventh cranial nerve',
                                                     'Great auricular nerve near the earlobe'],
                                         'answer': 2,
                                         'explanation': 'Stensen duct crosses the masseter about a '
                                                        'fingerbreadth below the zygomatic arch, along a '
                                                        'line from the tragus to the midpoint of the upper '
                                                        'lip, and the buccal branches of the facial nerve '
                                                        'run alongside it. An external incision over the '
                                                        'duct therefore risks buccal branch injury and '
                                                        'visible scarring. This is why failed endoscopic '
                                                        'access to a small parotid stone is usually '
                                                        'escalated to repeat sialendoscopy after dilation, '
                                                        'intracorporeal lithotripsy, or a monitored combined '
                                                        'approach rather than an open incision.',
                                         'why_wrong': ['The lingual nerve is at risk with transoral '
                                                       'submandibular hilar surgery, not with an external '
                                                       'approach to the parotid duct over the masseter.',
                                                       'The marginal mandibular branch runs along the lower '
                                                       'border of the mandible, below the course of Stensen '
                                                       'duct.',
                                                       'Correct.',
                                                       'The great auricular nerve is encountered in the '
                                                       'incision for parotidectomy behind the angle, not '
                                                       'over the masseter where the duct runs.'],
                                         'board_pearl': 'Stensen duct and the buccal branches travel '
                                                        'together over the masseter; open duct surgery risks '
                                                        'facial nerve injury.',
                                         'curveball': 'If the stone were instead 6 mm and impacted at the '
                                                      'parotid hilum, how would management change?',
                                         'curveball_answer': 'A 6-mm impacted hilar parotid stone is '
                                                             'unlikely to be retrieved by basket alone. '
                                                             'Options include intracorporeal laser or '
                                                             'pneumatic lithotripsy, or a combined '
                                                             'sialendoscopy-assisted transfacial approach '
                                                             'using a parotidectomy-type flap with facial '
                                                             'nerve monitoring. Parotidectomy is a last '
                                                             'resort because of its facial nerve risk.'},
 'v11_end_05': {'stem': 'A 66-year-old man has a right preauricular mass that has grown noticeably over 3 '
                        'months. For the past 3 weeks he has been unable to close his right eye fully and '
                        'his smile droops on that side. Exam shows a 3-cm firm mass in the right parotid '
                        'with House-Brackmann grade IV weakness of all branches. There is no history of skin '
                        'cancer, and the scalp and ear are clear. What is the most likely diagnosis?',
                'choices': ['Pleomorphic adenoma of the parotid',
                            'Warthin tumor of the parotid tail',
                            'Bell palsy with an incidental parotid lymph node',
                            'Primary parotid carcinoma'],
                'answer': 3,
                'explanation': 'Most parotid tumors are benign, but facial nerve dysfunction alongside a '
                               'parotid mass strongly indicates malignancy, because benign tumors displace '
                               'the nerve rather than infiltrate it. Rapid growth over months, firmness, '
                               'pain, fixation, skin involvement, and cervical adenopathy add to the '
                               'concern. In older patients, metastatic cutaneous squamous cell carcinoma to '
                               'intraparotid nodes is an important alternative, which is why the scalp and '
                               'ear are examined. A progressive palsy with a mass is never attributed to '
                               'Bell palsy.',
                'why_wrong': ['Pleomorphic adenomas grow slowly over years and almost never cause facial '
                              'weakness, even when large.',
                              'Warthin tumors are slow-growing, often bilateral or cystic, and do not invade '
                              'the facial nerve.',
                              'Bell palsy is acute and idiopathic; a progressive palsy with a growing '
                              'parotid mass must be presumed neoplastic.',
                              'Correct.'],
                'board_pearl': 'A parotid mass with facial weakness is malignant until proven otherwise; '
                               'benign tumors displace the nerve rather than invade it.',
                'curveball': 'He has complete facial paralysis preoperatively and MRI shows enhancement of '
                             'the nerve into the mastoid segment. How does that affect planning?',
                'curveball_answer': 'Preoperative paralysis with radiographic nerve involvement means the '
                                    'nerve will be sacrificed. The surgeon follows it proximally with frozen '
                                    'sections, which may require mastoidectomy, until margins are clear. '
                                    'Immediate reconstruction is planned with an interposition cable graft, '
                                    'such as great auricular or sural nerve, plus static procedures for eye '
                                    'closure and facial support such as a gold weight and fascia sling.'},
 'v141_tps_04': {'stem': 'A 61-year-old woman has a 4-month history of a firm, fixed left parotid mass with '
                         'intermittent aching pain. Exam shows weakness of the left marginal mandibular and '
                         'buccal branches and a 1.5-cm firm left level II node. The overlying skin is not '
                         'involved and she has no history of skin cancer. She has not had any imaging or '
                         'tissue sampling. What is the most appropriate next step?',
                 'choices': ['Contrast MRI of the parotid and neck with ultrasound-guided FNA',
                             'Superficial parotidectomy for diagnosis before any imaging',
                             'Open incisional biopsy of the parotid mass through the skin',
                             'Two weeks of antibiotics and reassessment of the mass'],
                 'answer': 0,
                 'explanation': 'Facial weakness, pain, fixation, and a suspicious node signal a probable '
                                'malignancy. Before surgery, contrast MRI defines deep-lobe and '
                                'parapharyngeal extension and perineural spread along the facial or '
                                'trigeminal nerves, while ultrasound-guided FNA, or core biopsy if needed, '
                                'provides a tissue diagnosis from the mass and node. Histology, grade, and '
                                'extent determine the resection, the facial nerve plan, neck dissection, and '
                                'adjuvant radiation. Open incisional biopsy and diagnostic parotidectomy '
                                'without imaging are avoided.',
                 'why_wrong': ['Correct.',
                               'Operating without imaging leaves deep-lobe, perineural, and nodal extent '
                               'unknown, so the extent of resection and nerve plan cannot be set.',
                               'Open incisional biopsy risks tumor seeding and facial nerve injury, while '
                               'needle sampling provides tissue with less morbidity.',
                               'Pain, fixation, and nerve weakness indicate a neoplasm, and delaying with '
                               'antibiotics postpones diagnosis and staging.'],
                 'board_pearl': 'Suspected parotid malignancy: MRI for extent and perineural spread plus '
                                'needle sampling, then plan the nerve and neck.',
                 'curveball': 'When can an involved facial nerve be sacrificed, and what reconstruction '
                              'should be planned simultaneously?',
                 'curveball_answer': 'The nerve is sacrificed when it is grossly infiltrated or functionally '
                                     'lost from tumor, not because of a cancer diagnosis alone; a '
                                     'functioning nerve that peels off tumor is preserved. When sacrificed, '
                                     'proximal and distal margins are confirmed by frozen section, and '
                                     'immediate cable grafting from the great auricular or sural nerve is '
                                     'preferred, with static eye and smile support added.'},
 'v233_tps_sgmal_fnd': {'stem': 'A 52-year-old man has a 2.5-cm painless mass in the left parotid tail that '
                                'he first noticed 5 months ago. Facial nerve function is normal, the skin is '
                                'mobile over the mass, and the neck is otherwise unremarkable. He smokes a '
                                'pack a day. He asks which features would make the surgeon worry that the '
                                'mass is cancer. Which additional finding would most strongly suggest '
                                'malignancy?',
                        'choices': ['A second similar mass in the opposite parotid tail',
                                    'Weakness of a facial nerve branch on the same side',
                                    'Soft consistency with a cystic appearance on ultrasound',
                                    'Hot uptake on technetium-99m pertechnetate scanning'],
                        'answer': 1,
                        'explanation': 'Facial nerve weakness is the most specific clinical sign of parotid '
                                       'malignancy because benign tumors displace rather than infiltrate the '
                                       'nerve. Pain, rapid growth, fixation, skin involvement, and cervical '
                                       'adenopathy also raise concern. In a smoker with a tail mass, Warthin '
                                       'tumor is common, and its typical features (bilaterality, cystic '
                                       'change, pertechnetate avidity) are reassuring. Preoperative '
                                       'evaluation defines histology, facial nerve status, and the neck, '
                                       'because each changes the operation and counseling.',
                        'why_wrong': ['Bilateral parotid tail masses in a smoker suggest Warthin tumor, '
                                      'which is benign and the most common bilateral salivary neoplasm.',
                                      'Correct.',
                                      'A soft, partly cystic tail mass is typical of Warthin tumor or a '
                                      'benign cyst rather than an infiltrating carcinoma.',
                                      'Pertechnetate uptake is characteristic of Warthin and oncocytic '
                                      'tumors, which concentrate the tracer, and indicates a benign lesion.'],
                        'board_pearl': 'Facial weakness, pain, fixation, skin involvement, and nodes are '
                                       'malignant red flags; bilateral cystic tail masses suggest Warthin '
                                       'tumor.',
                        'curveball': 'Which imaging and tissue-sampling strategy best evaluates suspected '
                                     'deep-lobe or skull-base extension?',
                        'curveball_answer': 'Contrast MRI with fat suppression best shows deep-lobe and '
                                            'parapharyngeal extension, perineural spread along the facial '
                                            'and auriculotemporal nerves, and skull-base invasion, while CT '
                                            'adds bone detail. Ultrasound-guided FNA or core biopsy samples '
                                            'superficial disease. Deep-lobe masses may need CT-guided or '
                                            'transoral-approach sampling, and open biopsy is avoided.'},
 'v233_tps_sgmal_app': {'stem': 'A 68-year-old man has a 3.5-cm right parotid mass with normal facial nerve '
                                'function. FNA shows high-grade carcinoma, favoring salivary duct carcinoma. '
                                'MRI shows the mass in the superficial lobe, separate from the main nerve '
                                'trunk, with two enlarged right level II and III nodes. FNA of a level II '
                                'node is positive. PET-CT shows no distant disease. What is the most '
                                'appropriate operative plan?',
                        'choices': ['Total parotidectomy with elective sacrifice of the facial nerve and a '
                                    'neck dissection',
                                    'Superficial parotidectomy followed by radiation to the neck in place of '
                                    'dissection',
                                    'Neoadjuvant chemotherapy first, then parotidectomy if the nodes respond',
                                    'Total parotidectomy preserving the uninvolved nerve with therapeutic '
                                    'neck dissection'],
                        'answer': 3,
                        'explanation': 'Surgery for salivary carcinoma is planned around histology, nerve '
                                       'involvement, and neck status. A functioning facial nerve that can be '
                                       'separated from tumor is preserved, with gross residual on the nerve '
                                       'addressed by adjuvant radiation. Pathologically confirmed nodes '
                                       'require therapeutic neck dissection, typically levels I or II '
                                       'through V. High-grade histology, T3 size, and nodal disease all '
                                       'indicate postoperative radiation. Salivary duct carcinoma should '
                                       'also be tested for androgen receptor and HER2 expression.',
                        'why_wrong': ['A functioning nerve that is not grossly invaded is preserved; '
                                      'sacrifice improves neither survival nor control and causes permanent '
                                      'paralysis.',
                                      'Clinically positive nodes are treated surgically with a comprehensive '
                                      'dissection, and radiation alone is inferior for bulky nodal disease.',
                                      'Neoadjuvant chemotherapy is not standard for resectable salivary '
                                      'carcinoma and delays the surgery that offers cure.',
                                      'Correct.'],
                        'board_pearl': 'Preserve a functioning, separable facial nerve; treat clinically '
                                       'positive nodes with therapeutic neck dissection.',
                        'curveball': 'How would preoperative complete facial paralysis change counseling '
                                     'about nerve resection and reconstruction?',
                        'curveball_answer': 'Complete paralysis signals gross invasion, so the involved '
                                            'nerve segment is resected to negative frozen-section margins '
                                            'rather than preserved. Patients are counseled before surgery '
                                            'that facial function will not recover without reconstruction. '
                                            'Immediate cable grafting is preferred when proximal and distal '
                                            'stumps are available, combined with static eye and oral '
                                            'commissure procedures, and radiation does not preclude graft '
                                            'recovery.'},
 'v233_tps_sgmal_snr': {'stem': 'A 57-year-old woman has a high-grade mucoepidermoid carcinoma of the left '
                                'parotid. She reports burning preauricular and temporal pain and new '
                                'numbness of the left lower lip and chin. Facial nerve function is normal. '
                                'MRI shows thickening and enhancement of the auriculotemporal nerve that '
                                'continues along the mandibular division through an enlarged foramen ovale. '
                                'What should define the treatment plan?',
                        'choices': ['Total parotidectomy with radiation limited to the parotid bed and upper '
                                    'neck',
                                    'Superficial parotidectomy alone, since microscopic perineural invasion '
                                    'is common',
                                    'Palliative systemic therapy alone, as perineural spread means incurable '
                                    'disease',
                                    'Resection and radiation planned to the proximal extent of the involved '
                                    'trigeminal pathway'],
                        'answer': 3,
                        'explanation': 'The auriculotemporal nerve connects the parotid to the mandibular '
                                       'division of the trigeminal nerve and is a classic route of '
                                       'perineural spread from parotid cancers. Clinical symptoms and MRI '
                                       'findings indicate gross spread that extends the true tumor margin '
                                       'far beyond the gland. Treatment must follow the nerve to its '
                                       'proximal endpoint: resection to the foramen with skull-base or '
                                       'infratemporal fossa approaches when feasible, and radiation fields '
                                       'covering the entire pathway toward the Gasserian ganglion.',
                        'why_wrong': ['Treating only the parotid bed leaves the involved nerve segment '
                                      'untreated and is a common cause of skull-base recurrence.',
                                      'This is gross, radiographic perineural spread rather than incidental '
                                      'microscopic invasion, and limited surgery would leave disease behind.',
                                      'Spread to the foramen ovale may still be curable with skull-base '
                                      'surgery and radiation, so palliation alone is premature.',
                                      'Correct.'],
                        'board_pearl': 'Radiographic perineural spread redefines tumor extent; map and treat '
                                       'the nerve to its central endpoint.',
                        'curveball': 'When does proximal skull-base extension make definitive radiation '
                                     'preferable to an attempt at resection?',
                        'curveball_answer': 'When spread reaches the cavernous sinus, Meckel cave, or the '
                                            'brainstem, or when clear margins would require unacceptable '
                                            'morbidity, an incomplete resection adds harm without improving '
                                            'control. Definitive radiation, often with protons or carbon '
                                            'ions where available, to the full neural pathway is then '
                                            'preferred, with surgery limited to the resectable primary if it '
                                            'does not compromise the plan.'},
 'v11_end_06': {'stem': 'A 44-year-old woman is undergoing right thyroid lobectomy for a 3-cm Bethesda IV '
                        'nodule. While the lobe is being rotated medially, brisk bleeding starts from a '
                        'small vessel within the ligament of Berry. The recurrent laryngeal nerve was seen '
                        'inferiorly but has not been followed to its laryngeal entry, and nerve monitoring '
                        'is in use. What is the safest way to control the bleeding?',
                'choices': ['Monopolar cautery to the bleeding point within the ligament',
                            'Blind placement of a hemostatic clamp across the ligament tissue',
                            'Bipolar cautery after one stimulation confirms a normal signal',
                            'Tamponade, then trace the nerve upward before precise vessel control'],
                'answer': 3,
                'explanation': 'The recurrent laryngeal nerve is most vulnerable at the ligament of Berry, '
                               'where it runs immediately deep to the posterior suspensory ligament and '
                               'branches before entering the larynx under the inferior constrictor. Bleeding '
                               'here tempts blind clamping or cautery. The safe sequence is pressure to '
                               'control the field, followed by identification of the nerve along its course '
                               'to the larynx and precise ligation or low-energy bipolar control well away '
                               'from it. Neuromonitoring is an adjunct to visual identification.',
                'why_wrong': ['Monopolar cautery spreads heat several millimeters, and the nerve lies within '
                              'millimeters of the ligament of Berry.',
                              'Blind clamping in the ligament is the classic mechanism of nerve crush or '
                              'transection at the laryngeal entry point.',
                              'A normal signal before cautery does not protect the nerve from thermal '
                              'spread, and monitoring cannot replace visual identification.',
                              'Correct.'],
                'board_pearl': 'At the ligament of Berry, control bleeding with pressure and visualize the '
                               'nerve before any clamp or energy device.',
                'curveball': 'The nerve looks intact but the signal is lost after traction near the '
                             'ligament. What immediate steps distinguish equipment failure from true injury?',
                'curveball_answer': 'Check that the stimulator works on muscle, that ground and recording '
                                    'electrodes are connected, and that the endotracheal tube has not '
                                    'rotated or migrated. Then stimulate the vagus and palpate for a '
                                    'laryngeal twitch behind the cricoid. A twitch with no signal points to '
                                    'equipment or tube problems; no twitch means a true loss of signal.'},
 'v135_tps_01': {'stem': 'A 39-year-old woman is undergoing total thyroidectomy for Graves disease. After a '
                         'difficult left-sided dissection, stimulating the left vagus and recurrent nerve '
                         'produces no electromyographic response. The left nerve looks anatomically intact. '
                         'The anesthesiologist confirms that no paralytic agent was given after induction '
                         'and the monitor shows no electrode alarms. What should the surgeon do next?',
                 'choices': ['Stimulate the vagus while palpating for a posterior cricoid twitch',
                             'Proceed to the right lobe because the nerve is visibly intact',
                             'Raise the stimulator to its maximum current and repeat the stimulation',
                             'Give intravenous dexamethasone and complete the right side'],
                 'answer': 0,
                 'explanation': 'Loss of signal can come from true nerve injury or from equipment problems, '
                                'most often endotracheal tube malposition with the electrodes no longer '
                                'contacting the vocal folds. After confirming paralytics and connections, '
                                'the next step in the International Neural Monitoring Study Group algorithm '
                                'is the laryngeal twitch test: stimulate the vagus or nerve while palpating '
                                'behind the posterior cricoid. A twitch means the nerve works and the '
                                'recording system is at fault, whereas no twitch confirms true loss of '
                                'signal.',
                 'why_wrong': ['Correct.',
                               'Visual continuity does not prove function, and proceeding before confirming '
                               'the event risks bilateral vocal fold paralysis.',
                               'Increasing current without checking the system can produce misleading '
                               'volume-conducted responses and does not test the recording pathway.',
                               'Steroids have unproven benefit for neuropraxia and do not answer whether the '
                               'loss of signal is real before the second side.'],
                 'board_pearl': 'Loss of signal: check paralytics, connections, and tube position, then use '
                                'the laryngeal twitch test to confirm.',
                 'curveball': 'No twitch is felt and the contralateral vagus still gives a normal signal. '
                              'What does that mean for the rest of the operation?',
                 'curveball_answer': 'A preserved contralateral vagal signal confirms that the recording '
                                     'system works, so the left-sided loss is a true neural event. Because a '
                                     'second injury would cause bilateral vocal fold paralysis, most '
                                     'guidance recommends stopping and staging the right lobectomy after '
                                     'laryngoscopy shows recovery. In Graves disease, interim control with '
                                     'antithyroid drugs is usually feasible.'},
 'v152_tps_01': {'stem': 'A 57-year-old man is undergoing total thyroidectomy for a large symptomatic benign '
                         'multinodular goiter. After removal of the right lobe, the right vagus no longer '
                         'produces a signal despite tube repositioning, circuit checks, and an absent '
                         'laryngeal twitch. The right nerve is in continuity. The left vagus gives a normal '
                         'response. The left lobe is moderately enlarged but not urgent. What is the safest '
                         'operative strategy?',
                 'choices': ['Complete the left lobectomy now because the right nerve looks intact',
                             'Stop and stage the left lobectomy after vocal fold reassessment',
                             'Complete both sides and perform a tracheostomy at the same sitting',
                             'Explore the right nerve by opening its sheath to look for injury'],
                 'answer': 1,
                 'explanation': 'A confirmed loss of signal on the first side predicts postoperative vocal '
                                'fold paresis, even when the nerve looks intact, because traction or '
                                'compression can cause a conduction block without visible damage. Completing '
                                'the contralateral side risks bilateral vocal fold paralysis and a surgical '
                                'airway. When the remaining disease is benign and not urgent, staging is the '
                                'safest choice: the second side is completed after laryngoscopy confirms '
                                'recovery, which usually occurs within weeks to months.',
                 'why_wrong': ['An intact-appearing nerve can still have a conduction block, and a second '
                               'injury on the left would cause bilateral paralysis.',
                               'Correct.',
                               'Accepting a tracheostomy for a benign, nonurgent goiter trades a preventable '
                               'airway complication for convenience.',
                               'Opening the epineurium adds trauma to a nerve that may recover spontaneously '
                               'and does not change the immediate decision.'],
                 'board_pearl': 'True first-side loss of signal in a nonurgent case: stage the contralateral '
                                'lobectomy.',
                 'curveball': 'Before stopping, the attending asks which troubleshooting steps should have '
                              'preceded declaring the right signal truly lost. What are they?',
                 'curveball_answer': 'Confirm no neuromuscular blockade, check ground and recording '
                                     'electrode connections and impedances, verify stimulator function on '
                                     'muscle, and reposition the endotracheal tube under laryngoscopy. Then '
                                     'stimulate the ipsilateral vagus and palpate for a posterior cricoid '
                                     'twitch, and test the contralateral vagus. Only a reproducible absent '
                                     'response with an intact system is a true loss of signal.'},
 'v154_tps_fnd': {'stem': 'A 48-year-old woman is having a left thyroid lobectomy for a 3-cm follicular '
                          'lesion. The attending asks the resident to identify the site where nerve injury '
                          'most commonly occurs, pointing to where the posterior lobe is tethered to the '
                          'cricoid cartilage and upper tracheal rings. Nerve monitoring is in use. At which '
                          'site is the recurrent laryngeal nerve most vulnerable during lobectomy?',
                  'choices': ['At the crossing with the inferior thyroid artery',
                              'Near the ligament of Berry at its laryngeal entry',
                              'At the superior pole alongside the thyroid vessels',
                              'In the tracheoesophageal groove at the thoracic inlet'],
                  'answer': 1,
                  'explanation': 'Near the ligament of Berry, the recurrent laryngeal nerve passes directly '
                                 'deep to or through the dense posterior suspensory ligament that fixes the '
                                 'thyroid to the cricoid and upper trachea. Here it is closest to the gland, '
                                 'often branches extralaryngeally with the motor fibers usually in the '
                                 'anterior branch, and enters the larynx beneath the inferior constrictor. '
                                 'Medial traction tents the nerve, and bleeding invites blind clamping or '
                                 'cautery, making this the most common injury site.',
                  'why_wrong': ['The inferior thyroid artery is a useful landmark, but its relationship to '
                                'the nerve is variable and it is not the most frequent injury site.',
                                'Correct.',
                                'The superior pole is where the external branch of the superior laryngeal '
                                'nerve is at risk, not the recurrent laryngeal nerve.',
                                'Low in the groove the nerve is relatively deep and away from the gland, so '
                                'injury is less frequent than near its laryngeal entry.'],
                  'board_pearl': 'Most recurrent laryngeal nerve injuries occur at the ligament of Berry, '
                                 'where the nerve is tethered closest to the gland.',
                  'curveball': 'Why is the inferior thyroid artery an imperfect single landmark for the '
                               'recurrent laryngeal nerve?',
                  'curveball_answer': 'The nerve may pass deep to, superficial to, or between branches of '
                                      'the inferior thyroid artery, and the pattern differs between sides '
                                      'and patients. The artery can also be absent, and on the right the '
                                      'nerve may be nonrecurrent. Surgeons therefore identify the nerve low '
                                      'in the tracheoesophageal groove and follow it, rather than relying on '
                                      'the artery alone.'},
 'v154_tps_app': {'stem': 'A 50-year-old woman had a total thyroidectomy for multinodular goiter 2 days ago. '
                          'Her voice is now weak and breathy, she tires when speaking, and she coughs when '
                          'drinking water but manages thicker foods. She has no stridor and her oxygen '
                          'saturation is normal. Calcium is normal. The intraoperative monitoring signal was '
                          'reported as normal at the end of the case. What is the most appropriate first '
                          'diagnostic test?',
                  'choices': ['Flexible laryngoscopy to assess vocal fold motion',
                              'Modified barium swallow to define the aspiration',
                              'CT of the neck and chest to image the vagal course',
                              'Referral for voice therapy before any examination'],
                  'answer': 0,
                  'explanation': 'New breathy dysphonia and thin-liquid aspiration after thyroidectomy '
                                 'indicate glottic insufficiency until proven otherwise, and the key first '
                                 'test is flexible laryngoscopy to assess vocal fold mobility. A normal '
                                 'final signal predicts normal function but not perfectly. Laryngoscopy '
                                 'distinguishes recurrent nerve paresis from superior laryngeal nerve '
                                 'injury, edema, or arytenoid problems and guides early management, such as '
                                 'injection laryngoplasty for aspiration. The Hoarseness guideline also '
                                 'supports laryngeal examination when voice change follows neck surgery.',
                  'why_wrong': ['Correct.',
                                'A swallow study characterizes aspiration but does not diagnose its cause, '
                                'and laryngoscopy should come first to look for vocal fold immobility.',
                                'Imaging the vagus is reserved for unexplained paralysis; here the operation '
                                'is the likely cause and the larynx must be examined first.',
                                'Therapy without examination may miss vocal fold paralysis that needs '
                                'injection medialization to protect against aspiration.'],
                  'board_pearl': 'New voice change after thyroidectomy: examine the larynx first with '
                                 'flexible laryngoscopy.',
                  'curveball': 'How does management differ for unilateral versus bilateral vocal fold '
                               'immobility after thyroidectomy?',
                  'curveball_answer': 'Unilateral immobility usually causes a breathy voice and aspiration '
                                      'with a safe airway, and early injection laryngoplasty can be offered '
                                      'while recovery is awaited. Bilateral immobility typically causes '
                                      'stridor and airway compromise with a relatively good voice, and it '
                                      'may require reintubation, steroids, and tracheostomy or a '
                                      'glottic-widening procedure if recovery fails.'},
 'v154_tps_snr': {'stem': 'A 42-year-old man is undergoing planned total thyroidectomy for a 1.5-cm right '
                          'papillary carcinoma with a normal left lobe and no suspicious nodes. After the '
                          'right lobe is removed, a true loss of signal is confirmed on the right despite '
                          'full troubleshooting, and the nerve looks intact. The left vagus responds '
                          'normally. What is the most appropriate way to proceed?',
                  'choices': ['End surgery and decide on left lobectomy after vocal fold recovery',
                              'Complete the left lobectomy because cancer surgery should not be staged',
                              'Complete the left side with planned tracheostomy for airway protection',
                              'Resect and graft the right nerve segment to restore its conduction'],
                  'answer': 0,
                  'explanation': 'A confirmed first-side loss of signal predicts temporary paresis in many '
                                 'patients even with an intact nerve. Proceeding risks bilateral paralysis. '
                                 'The contralateral lobe here is normal and the tumor is low risk, so '
                                 'staging is safe. Under ATA 2025, lobectomy alone is acceptable for a '
                                 'low-risk unifocal tumor up to 2 cm, so completion may never be needed. '
                                 'Final pathology and laryngoscopy determine whether the left lobe is '
                                 'removed later.',
                  'why_wrong': ['Correct.',
                                'A 1.5-cm low-risk carcinoma does not require urgent contralateral surgery, '
                                'and a bilateral injury would be far more harmful than a short delay.',
                                'Tracheostomy addresses a complication that staging avoids and is not '
                                'justified for a low-risk cancer that can wait.',
                                'Resecting a nerve in continuity with likely neuropraxia destroys a nerve '
                                'that is expected to recover on its own.'],
                  'board_pearl': 'Loss of signal on the first side changes the plan; in low-risk cancer, '
                                 'lobectomy alone may become definitive.',
                  'curveball': 'Final pathology shows gross extrathyroidal extension and multiple nodal '
                               'metastases. How does that change timing?',
                  'curveball_answer': 'Higher-risk disease makes completion thyroidectomy and radioiodine '
                                      'appropriate, but the timing still depends on nerve recovery. '
                                      'Laryngoscopy is repeated, and completion is usually performed once '
                                      'right vocal fold motion recovers, often within weeks. If paralysis '
                                      'persists, the oncologic benefit is weighed against the bilateral '
                                      'paralysis risk, with meticulous left nerve monitoring.'},
 'v238_tps_rln_fnd': {'stem': 'A 59-year-old woman had a total thyroidectomy after a difficult intubation '
                              'that needed several attempts with a bougie. The surgeon documented intact '
                              'nerve signals bilaterally at the end of the case. Since extubation she has '
                              'had a breathy voice and pain with swallowing. Flexible laryngoscopy shows an '
                              'immobile left vocal fold with an anteriorly displaced, edematous left '
                              'arytenoid. Which test best distinguishes nerve paralysis from mechanical '
                              'fixation?',
                      'choices': ['CT with contrast from the skull base down to the aortic arch',
                                  'Modified barium swallow study to assess aspiration',
                                  'Repeat flexible laryngoscopy in 6 months',
                                  'Laryngeal electromyography of the thyroarytenoid muscle'],
                      'answer': 3,
                      'explanation': 'Unilateral immobility after thyroidectomy is usually recurrent nerve '
                                     'injury, but intubation trauma can cause arytenoid dislocation or '
                                     'cricoarytenoid joint hemarthrosis and fixation. Her traumatic '
                                     'intubation, normal final signal, and displaced arytenoid raise that '
                                     'concern. Laryngeal EMG shows normal recruitment in a mechanically '
                                     'fixed fold but fibrillations or reduced recruitment in a denervated '
                                     'one. Palpation of the arytenoid under anesthesia can also confirm '
                                     'fixation. Early diagnosis matters because closed reduction works best '
                                     'within the first weeks.',
                      'why_wrong': ['Imaging the vagal course seeks a lesion along the nerve, but it cannot '
                                    'show whether the laryngeal muscles are innervated.',
                                    'A swallow study measures aspiration risk but cannot separate neural '
                                    'paralysis from cricoarytenoid joint problems.',
                                    'Waiting 6 months loses the window for closed reduction of an arytenoid '
                                    'dislocation, which is most successful when done early.',
                                    'Correct.'],
                      'board_pearl': 'Immobile fold after intubation and thyroidectomy: laryngeal EMG '
                                     'separates denervation from arytenoid dislocation or fixation.',
                      'curveball': 'How does immediate versus delayed onset of dysphonia affect the '
                                   'suspected mechanism?',
                      'curveball_answer': 'Dysphonia present at extubation suggests direct injury: '
                                          'transection, clamp or ligature entrapment, thermal injury, '
                                          'traction, or arytenoid dislocation. Onset a day or more later '
                                          'suggests evolving edema, hematoma, or delayed neuropraxia from '
                                          'inflammation, which more often recovers. Timing therefore guides '
                                          'urgency of re-exploration in suspected ligature entrapment versus '
                                          'observation.'},
 'v238_tps_rln_app': {'stem': 'A 34-year-old woman with a large compressive benign goiter had a staged '
                              'operation: after right lobectomy, a confirmed right loss of signal led the '
                              'surgeon to stop. Postoperative laryngoscopy showed right vocal fold '
                              'immobility. She is now 5 weeks out, her voice is improving, and she asks to '
                              'have the left lobe removed before her wedding in 3 weeks. What is required '
                              'before the left lobectomy?',
                      'choices': ['A normal voice on perceptual rating by a speech pathologist',
                                  'Six full months since the first operation, irrespective of function',
                                  'Laryngeal EMG showing reinnervation potentials alone',
                                  'Laryngoscopy documenting recovered right vocal fold motion'],
                      'answer': 3,
                      'explanation': 'The purpose of staging after a confirmed loss of signal is to avoid '
                                     'bilateral vocal fold paralysis. Before operating on the second side, '
                                     'the surgeon must confirm that the first nerve has recovered, which '
                                     'means laryngoscopy showing restored motion of the affected fold. Voice '
                                     'can improve from compensation while the fold remains immobile. If '
                                     'motion has returned, the left lobectomy proceeds with nerve '
                                     'monitoring; if not, surgery waits or the indication for the second '
                                     'side is reconsidered.',
                      'why_wrong': ['Voice can improve through compensation by the opposite fold while the '
                                    'right fold stays immobile, so voice quality alone is unreliable.',
                                    'A fixed waiting period is arbitrary; many nerves recover within weeks, '
                                    'and the decision depends on documented motion.',
                                    'EMG reinnervation does not guarantee useful abduction, and the '
                                    'operative risk rests on actual fold movement seen at laryngoscopy.',
                                    'Correct.'],
                      'board_pearl': 'After a staged loss of signal, document recovered vocal fold motion by '
                                     'laryngoscopy before operating on the other side.',
                      'curveball': 'What technical checks distinguish equipment failure from a true neural '
                                   'event during the second operation?',
                      'curveball_answer': 'Before dissection, confirm a baseline vagal signal and correct '
                                          'tube position, since a missing baseline suggests an equipment or '
                                          'tube issue. If signal is lost, check paralytics, electrode '
                                          'connections and impedance, stimulator function, and tube '
                                          'position, then test the laryngeal twitch. A preserved twitch '
                                          'implies equipment failure; no twitch with a working system means '
                                          'true loss.'},
 'v238_tps_rln_snr': {'stem': 'A 64-year-old woman has had a breathy, weak voice and coughing with thin '
                              'liquids since a total thyroidectomy 10 months ago. Laryngoscopy shows a left '
                              'vocal fold paralyzed in the paramedian position with a glottic gap and no '
                              'recovery. A temporary gel injection at 2 months helped briefly. Laryngeal EMG '
                              'at 6 months showed poor prognosis. Her airway is adequate. What is the most '
                              'appropriate definitive treatment?',
                      'choices': ['Repeated temporary gel injections every few months',
                                  'Type I medialization thyroplasty with an implant',
                                  'Posterior cordotomy to widen the glottic airway',
                                  'Observation for another year awaiting recovery'],
                      'answer': 1,
                      'explanation': 'Unilateral paralysis that persists beyond about 9 to 12 months with an '
                                     'unfavorable EMG is unlikely to recover, so treatment shifts from '
                                     'temporary injection to durable medialization. Type I thyroplasty '
                                     'places an implant through a window in the thyroid cartilage to push '
                                     'the paralyzed fold medially, closing the glottic gap, improving voice, '
                                     'and reducing aspiration. Ansa cervicalis to recurrent nerve '
                                     'reinnervation is an alternative, though results are often less '
                                     'favorable in older patients.',
                      'why_wrong': ['Temporary injectables resorb within months; with no expected recovery, '
                                    'a durable medialization is more appropriate.',
                                    'Correct.',
                                    'Cordotomy enlarges the airway and would worsen her breathiness and '
                                    'aspiration; it is used for bilateral paralysis with obstruction.',
                                    'Recovery is unlikely after 10 months with a poor EMG prognosis, and '
                                    'continued glottic insufficiency risks aspiration.'],
                      'board_pearl': 'Persistent unilateral paralysis without expected recovery: durable '
                                     'medialization or reinnervation, chosen by age and goals.',
                      'curveball': 'Had her nerve been found transected at the original thyroidectomy, when '
                                   'would immediate intraoperative repair or reinnervation be considered?',
                      'curveball_answer': 'When the nerve is transected or a segment is resected during '
                                          'thyroidectomy, immediate repair is recommended. A tension-free '
                                          'end-to-end neurorrhaphy, an interposition graft, or an ansa '
                                          'cervicalis to recurrent nerve anastomosis restores tone and bulk, '
                                          'though not coordinated motion. This improves long-term voice '
                                          'compared with leaving the nerve unrepaired.'},
 'v113-end-01': {'stem': 'A 78-year-old woman with a long-standing multinodular goiter presents with 2 days '
                         'of worsening noisy breathing. She now has inspiratory stridor at rest, cannot lie '
                         'flat, and speaks in short phrases with oxygen saturation of 93%. CT shows a large '
                         'substernal goiter narrowing the trachea to 4 mm at the thoracic inlet. She is '
                         'euthyroid. Anesthesia and thoracic surgery are available. What is the most '
                         'appropriate immediate airway plan?',
                 'choices': ['Rapid-sequence induction and direct laryngoscopy in the emergency department '
                             'with a smaller tube',
                             'Awake fiberoptic intubation in the operating room with rigid bronchoscopy and '
                             'surgical backup',
                             'Emergency awake tracheostomy under local anesthesia through the goiter in the '
                             'emergency department',
                             'Ultrasound-guided FNA of the dominant nodule before deciding on the definitive '
                             'airway approach'],
                 'answer': 1,
                 'explanation': 'Critical tracheal compression from a goiter makes airway control the first '
                                'priority, ahead of any diagnostic step. Spontaneous ventilation is '
                                'preserved with an awake fiberoptic intubation in the operating room, '
                                'passing an appropriately sized reinforced tube beyond the narrowing, with '
                                'rigid bronchoscopy and a surgeon ready. In very severe cases extracorporeal '
                                'support can be placed on standby. Once the airway is secured, '
                                'thyroidectomy, sometimes with sternotomy for deep mediastinal extension, '
                                'relieves the compression definitively.',
                 'why_wrong': ['Induction and paralysis can collapse an extrinsically compressed airway, '
                               'leaving a cannot-intubate, cannot-oxygenate emergency.',
                               'Correct.',
                               'Tracheostomy through a large goiter is bloody and hazardous, and the '
                               'stenosis may extend below where the tracheostomy would sit.',
                               'Tissue diagnosis does not change the immediate need to secure a critically '
                               'narrowed airway and only delays definitive care.'],
                 'board_pearl': 'Goiter with critical tracheal narrowing: keep spontaneous ventilation, '
                                'secure the airway awake in the OR, then perform thyroidectomy.',
                 'curveball': 'What features would make awake airway control especially risky and bring '
                              'extracorporeal backup into the discussion?',
                 'curveball_answer': 'A tracheal lumen of only a few millimeters, narrowing that extends to '
                                     'the carina, orthopnea with hypoxemia, inability to pass a fiberoptic '
                                     'scope, and tracheomalacia or intraluminal invasion suggesting '
                                     'malignancy all raise the risk of losing the airway. In those patients, '
                                     'femoral access for ECMO or cardiopulmonary bypass is prepared before '
                                     'any sedation or airway manipulation.'},
 'v141_tps_01': {'stem': 'A 29-year-old woman with Graves disease stopped methimazole 2 months ago and is '
                         'admitted for an emergency appendectomy. Postoperatively she develops a temperature '
                         'of 40.1 C, heart rate 164 in atrial fibrillation, agitation, vomiting, and '
                         'bibasilar crackles. Free T4 is markedly elevated and TSH is undetectable. Her '
                         'Burch-Wartofsky score is well above 45. Which treatment sequence is most '
                         'appropriate?',
                 'choices': ['Potassium iodide first, then methimazole after 24 hours, plus aspirin',
                             'Emergency total thyroidectomy once fever and agitation are controlled',
                             'Propranolol, PTU, then potassium iodide an hour later, plus hydrocortisone',
                             'Radioactive iodine with propranolol and acetaminophen for fever'],
                 'answer': 2,
                 'explanation': 'Thyroid storm is a clinical diagnosis of decompensated thyrotoxicosis, here '
                                'precipitated by stopping methimazole and surgery. Treatment attacks every '
                                'step: beta blockade with propranolol controls adrenergic effects; PTU '
                                'blocks synthesis and peripheral T4-to-T3 conversion; iodine given at least '
                                'an hour after the thionamide blocks hormone release; and hydrocortisone '
                                'reduces conversion and treats relative adrenal insufficiency. Supportive '
                                'care includes cooling, fluids, acetaminophen, and management of heart '
                                'failure.',
                 'why_wrong': ['Iodine given before a thionamide supplies substrate for new hormone '
                               'synthesis, and aspirin displaces thyroid hormone from binding proteins.',
                               'Thyroidectomy is reserved for patients who fail or cannot tolerate medical '
                               'therapy, and operating during storm carries prohibitive risk.',
                               'Correct.',
                               'Radioiodine acts over weeks, can release stored hormone, and is not an '
                               'emergency treatment for thyroid storm.'],
                 'board_pearl': 'Thyroid storm: beta blocker, thionamide (PTU preferred), iodine at least an '
                                'hour after the thionamide, and steroids.',
                 'curveball': 'How is preoperative preparation different for elective thyroidectomy in a '
                              'patient with controlled Graves disease?',
                 'curveball_answer': 'Elective surgery is scheduled only after she is euthyroid on '
                                     'methimazole, with a beta blocker for symptoms. Potassium iodide, as '
                                     'SSKI or Lugol solution, is given for about 7 to 10 days before surgery '
                                     'to reduce gland vascularity and blood loss. Calcium and vitamin D '
                                     'status are optimized, and she is counseled about hypocalcemia from '
                                     'rapid bone remineralization.'},
 'v235_tps_graves_fnd': {'stem': 'A 41-year-old woman with Graves disease has a diffuse goiter weighing an '
                                 'estimated 120 g that causes dysphagia and pressure when she lies supine. '
                                 'Over 2 years, she has had hard-to-control thyrotoxicosis on methimazole, '
                                 'and a trial off medication failed. She has no eye disease and does not '
                                 'plan pregnancy soon. CT shows mild tracheal deviation. What is the most '
                                 'appropriate definitive treatment?',
                         'choices': ['Radioactive iodine at a standard ablative activity',
                                     'Continued long-term methimazole at a higher dose',
                                     'Total thyroidectomy after euthyroid preparation',
                                     'Subtotal thyroidectomy leaving bilateral remnants'],
                         'answer': 2,
                         'explanation': 'Graves disease can be treated with antithyroid drugs, radioactive '
                                        'iodine, or surgery. Thyroidectomy is favored when the goiter is '
                                        'large or compressive, rapid definitive control is wanted, nodules '
                                        'are suspicious, or eye disease is active. Her large compressive '
                                        'goiter and failed medical therapy make total thyroidectomy the best '
                                        'choice: it relieves compression immediately and eliminates '
                                        'recurrence. She should be euthyroid on methimazole with potassium '
                                        'iodide for 7 to 10 days preoperatively.',
                         'why_wrong': ['Large goiters respond less reliably to radioiodine, which also '
                                       'shrinks the gland slowly and may not relieve compressive symptoms.',
                                       'Two years of difficult control and a failed trial off medication '
                                       'make long-term thionamide a poor choice for her.',
                                       'Correct.',
                                       'Subtotal resection leaves tissue that can cause recurrent '
                                       'hyperthyroidism and makes reoperation riskier, so total '
                                       'thyroidectomy is preferred.'],
                         'board_pearl': 'Large or compressive Graves goiter, or failed drug therapy: total '
                                        'thyroidectomy after euthyroid and iodine preparation.',
                         'curveball': 'How can active thyroid eye disease influence the choice between '
                                      'radioactive iodine and other definitive treatments?',
                         'curveball_answer': 'Radioiodine can worsen active orbitopathy, especially in '
                                             'smokers and patients with high TSH receptor antibodies. With '
                                             'mild active disease, a course of oral steroids can cover '
                                             'radioiodine. Moderate-to-severe or sight-threatening active '
                                             'disease is a contraindication to radioiodine, favoring '
                                             'thyroidectomy or continued antithyroid drugs until the eye '
                                             'disease is inactive.'},
 'v235_tps_graves_app': {'stem': 'A 33-year-old woman with Graves disease and a moderate goiter is scheduled '
                                 'for elective total thyroidectomy tomorrow. At preoperative check-in her '
                                 'heart rate is 128 with tremor and diaphoresis. Free T4 is three times the '
                                 'upper limit. She admits she stopped methimazole a month ago because of '
                                 'nausea, and she has not taken potassium iodide. What is the most '
                                 'appropriate management?',
                         'choices': ['Postpone surgery and restore euthyroidism with a thionamide and beta '
                                     'blocker',
                                     'Proceed tomorrow after a dose of propranolol to control the heart rate',
                                     'Give potassium iodide alone for 10 days and then proceed with surgery',
                                     'Proceed tomorrow with stress-dose hydrocortisone and an esmolol '
                                     'infusion'],
                         'answer': 0,
                         'explanation': 'Elective thyroidectomy in Graves disease should be performed when '
                                        'the patient is euthyroid, because operating in a thyrotoxic state '
                                        'risks precipitating thyroid storm. Surgery is postponed and '
                                        'methimazole restarted, or PTU if she cannot tolerate methimazole, '
                                        'along with a beta blocker for symptoms. Once she is biochemically '
                                        'controlled, potassium iodide is added for 7 to 10 days to reduce '
                                        'vascularity. When thionamides cannot be used, rapid preparation can '
                                        'combine beta blockers, iodine, steroids, and cholestyramine.',
                         'why_wrong': ['Correct.',
                                       'Beta blockade masks adrenergic symptoms but leaves hormone levels '
                                       'high, so the risk of intraoperative or postoperative storm remains.',
                                       'Iodine alone produces only transient inhibition and can escape, '
                                       'worsening thyrotoxicosis if a thionamide is not also given.',
                                       'Rushing an elective case with markedly elevated hormone levels '
                                       'courts thyroid storm, which careful preparation can prevent.'],
                         'board_pearl': 'Elective Graves thyroidectomy waits for euthyroidism; operating '
                                        'while thyrotoxic risks precipitating storm.',
                         'curveball': 'In a patient like her, what circumstances would make urgent '
                                      'thyroidectomy necessary despite incomplete biochemical optimization?',
                         'curveball_answer': 'Agranulocytosis or severe hepatotoxicity from thionamides, '
                                             'airway compression from a large goiter, uncontrolled storm '
                                             'despite maximal medical therapy, or a need for rapid control '
                                             'such as cardiac decompensation can force surgery. Rapid '
                                             'preparation then uses high-dose beta blockade, potassium '
                                             'iodide, glucocorticoids, and cholestyramine over several days, '
                                             'with anesthesia aware of storm risk.'},
 'v235_tps_graves_snr': {'stem': 'A 46-year-old woman who smokes has Graves disease with a large goiter that '
                                 'causes dysphagia. She has painful proptosis, eyelid swelling, diplopia, '
                                 'and a clinical activity score of 5 of 7, with moderate-to-severe active '
                                 'orbitopathy confirmed by ophthalmology. TSH receptor antibodies are very '
                                 'high. She is euthyroid on methimazole but wants definitive treatment. '
                                 'Which definitive option is most appropriate?',
                         'choices': ['Radioactive iodine with a 3-month course of oral prednisone for '
                                     'prophylaxis',
                                     'Radioactive iodine alone at a higher activity to ensure prompt '
                                     'ablation',
                                     'Total thyroidectomy after euthyroid preparation, coordinated with '
                                     'ophthalmology',
                                     'Hemithyroidectomy of the dominant lobe to relieve compressive '
                                     'symptoms'],
                         'answer': 2,
                         'explanation': 'Definitive treatment of Graves disease must account for '
                                        'orbitopathy. Radioiodine can worsen active eye disease, '
                                        'particularly in smokers and patients with high receptor antibodies, '
                                        'and is contraindicated in moderate-to-severe or sight-threatening '
                                        'active disease. Total thyroidectomy gives rapid control without '
                                        'that risk and also relieves her compressive goiter. Coordination '
                                        'with ophthalmology may add intravenous glucocorticoids or '
                                        'teprotumumab, and smoking cessation is strongly advised. Continuing '
                                        'methimazole until the eye disease quiets is an alternative.',
                         'why_wrong': ['Steroid cover suits mild active orbitopathy; moderate-to-severe '
                                       'active disease is a contraindication to radioiodine.',
                                       'Higher-activity radioiodine still causes antigen release and can '
                                       'worsen active eye disease, particularly in smokers.',
                                       'Correct.',
                                       'Hemithyroidectomy leaves enough tissue for persistent '
                                       'hyperthyroidism and does not treat her Graves disease definitively.'],
                         'board_pearl': 'Moderate-to-severe active Graves orbitopathy: avoid radioiodine; '
                                        'thyroidectomy or continued thionamide are preferred.',
                         'curveball': 'Which preoperative laryngeal and calcium-related issues deserve '
                                      'special planning in a large vascular Graves goiter?',
                         'curveball_answer': 'Baseline laryngoscopy documents vocal fold function, since a '
                                             'large goiter can stretch the nerves. Potassium iodide reduces '
                                             'vascularity and blood loss. Vitamin D deficiency should be '
                                             'corrected because Graves patients have high bone turnover and '
                                             'are prone to postoperative hypocalcemia. A postoperative PTH '
                                             'level guides early calcium and calcitriol.'},
 'v113-end-02': {'stem': 'A 61-year-old woman with 8 years of untreated primary hyperparathyroidism, calcium '
                         '13.1 mg/dL, and alkaline phosphatase three times normal undergoes excision of a '
                         '3-cm adenoma. Intraoperative PTH falls appropriately. On postoperative day 3 she '
                         'has perioral numbness and carpopedal spasm. Calcium is 7.2 mg/dL, phosphate 1.8 '
                         'mg/dL, magnesium 1.4 mg/dL, and intact PTH 52 pg/mL. What is the most likely '
                         'explanation?',
                 'choices': ['Postoperative hypoparathyroidism',
                             'Persistent primary hyperparathyroidism',
                             'Hungry bone syndrome',
                             'Vitamin D deficiency osteomalacia alone'],
                 'answer': 2,
                 'explanation': 'Hungry bone syndrome follows removal of long-standing PTH excess. With '
                                'resorption suddenly halted, chronically demineralized bone avidly takes up '
                                'calcium, phosphate, and magnesium, so all three fall while PTH is normal or '
                                'even high as the remaining glands respond. Her long disease duration, '
                                'severe hypercalcemia, large adenoma, and high alkaline phosphatase all '
                                'predict it. In contrast, postoperative hypoparathyroidism causes low PTH '
                                'with high phosphate. Hungry bone may require weeks of high-dose calcium and '
                                'calcitriol.',
                 'why_wrong': ['Hypoparathyroidism causes low PTH and high phosphate, whereas her PTH is '
                               'normal and phosphate is low.',
                               'Persistent disease would keep calcium elevated, and her intraoperative PTH '
                               'fall and hypocalcemia argue against it.',
                               'Correct.',
                               'Osteomalacia can contribute, but it does not explain the abrupt '
                               'postoperative fall in calcium, phosphate, and magnesium.'],
                 'board_pearl': 'Hungry bone: low calcium, phosphate, and magnesium with normal or high PTH '
                                'after parathyroidectomy for severe disease.',
                 'curveball': 'Which preoperative features would make you anticipate aggressive calcium and '
                              'vitamin D replacement?',
                 'curveball_answer': 'High alkaline phosphatase, radiographic bone disease such as osteitis '
                                     'fibrosa cystica or brown tumors, a large adenoma, very high PTH and '
                                     'calcium, older age, and renal hyperparathyroidism predict hungry bone. '
                                     'In such patients, vitamin D is repleted before surgery, and calcium '
                                     'with calcitriol is started early postoperatively with close '
                                     'electrolyte monitoring.'},
 'v141_tps_02': {'stem': 'A 54-year-old man with severe primary hyperparathyroidism and brown tumors of the '
                         'tibia underwent parathyroidectomy 4 days ago. He has tingling and a positive '
                         'Trousseau sign. Calcium is 7.0 mg/dL despite calcium carbonate 1 g three times '
                         'daily, phosphate is 1.6 mg/dL, magnesium is 1.3 mg/dL, and intact PTH is 70 pg/mL. '
                         'ECG shows a prolonged QT interval. What is the most appropriate management?',
                 'choices': ['Continue the current calcium dose and stop once his tingling resolves',
                             'IV calcium and magnesium, then high-dose oral calcium with calcitriol',
                             'Withhold calcium so that his suppressed parathyroid glands can recover',
                             'Oral phosphate supplementation to correct the low serum phosphate first'],
                 'answer': 1,
                 'explanation': 'Brown tumors, prolonged hypocalcemia with low phosphate and magnesium, and '
                                'a preserved PTH define hungry bone syndrome, and his skeleton will absorb '
                                'large amounts of calcium for weeks. Symptomatic hypocalcemia with QT '
                                'prolongation calls for intravenous calcium gluconate, followed by high-dose '
                                'oral elemental calcium with calcitriol, since active vitamin D enhances '
                                'intestinal absorption. Magnesium must be repleted because hypomagnesemia '
                                'impairs PTH secretion and action. Phosphate is generally not supplemented '
                                'until calcium recovers.',
                 'why_wrong': ['His dose is far too low for hungry bone physiology, and symptoms with a '
                               'prolonged QT require escalation rather than tapering.',
                               'Correct.',
                               'His PTH is not suppressed, and withholding calcium in symptomatic hungry '
                               'bone risks tetany, seizures, and arrhythmia.',
                               'Phosphate binds calcium and deposits it in tissues, which worsens '
                               'hypocalcemia; phosphate is not replaced until calcium is safe.'],
                 'board_pearl': 'Hungry bone needs aggressive calcium, calcitriol, and magnesium; avoid '
                                'phosphate replacement until calcium is safe.',
                 'curveball': 'Which preoperative features predict higher risk and justify anticipatory '
                              'replacement in a patient like this?',
                 'curveball_answer': 'Brown tumors or osteitis fibrosa cystica, alkaline phosphatase well '
                                     'above normal, very high preoperative PTH and calcium, large gland '
                                     'weight, older age, and renal hyperparathyroidism predict hungry bone. '
                                     'Such patients benefit from vitamin D repletion before surgery and from '
                                     'scheduled calcium and calcitriol beginning immediately after surgery, '
                                     'with daily monitoring.'},
 'v236_tps_hungry_fnd': {'stem': 'A 67-year-old woman with primary hyperparathyroidism, osteoporosis, and an '
                                 'alkaline phosphatase of 380 U/L had a 4-gram adenoma removed. Two days '
                                 'later she has perioral tingling. Calcium is 7.4 mg/dL, phosphate 2.0 '
                                 'mg/dL, magnesium 1.5 mg/dL, and intact PTH 61 pg/mL. Her resident asks why '
                                 'her calcium is low when her remaining glands are working. Which mechanism '
                                 'best explains her hypocalcemia?',
                         'choices': ['Prolonged suppression of the remaining normal parathyroid glands',
                                     'Hypomagnesemia causing end-organ resistance to circulating PTH',
                                     'Rapid skeletal mineral uptake after PTH-driven resorption stops',
                                     'Increased renal calcium loss once the high PTH level has fallen'],
                         'answer': 2,
                         'explanation': 'Chronic PTH excess keeps osteoclastic resorption running, leaving a '
                                        'skeleton with large unmineralized surfaces. Once PTH falls '
                                        'abruptly, resorption stops while osteoblastic formation continues, '
                                        'and the skeleton rapidly draws calcium, phosphate, and magnesium '
                                        'from the blood. The remaining glands respond appropriately, so PTH '
                                        'is normal or high, distinguishing this from hypoparathyroidism, '
                                        'which has low PTH and high phosphate. High alkaline phosphatase, '
                                        'reflecting osteoblastic activity, is a key predictor.',
                         'why_wrong': ['Suppressed glands would produce low PTH with high phosphate, whereas '
                                       'her PTH is normal and phosphate is low.',
                                       'Her magnesium is only mildly low and does not explain the '
                                       'simultaneous fall in phosphate and the normal PTH level.',
                                       'Correct.',
                                       'Urinary calcium loss is a minor contributor and does not account for '
                                       'the drop in phosphate and magnesium together.'],
                         'board_pearl': 'Hungry bone means skeletal mineral uptake after PTH withdrawal; PTH '
                                        'is normal or high, phosphate low.',
                         'curveball': 'How does hungry bone differ biochemically from hypocalcemia caused by '
                                      'permanent hypoparathyroidism?',
                         'curveball_answer': 'In hungry bone, PTH is normal or elevated, phosphate and '
                                             'magnesium are low, and urine calcium is low because the '
                                             'skeleton absorbs mineral. In hypoparathyroidism, PTH is low or '
                                             'undetectable, phosphate is high because PTH no longer drives '
                                             'phosphaturia, and urine calcium can be relatively high on '
                                             'replacement. Phosphate and PTH together distinguish them.'},
 'v236_tps_hungry_app': {'stem': 'A 45-year-old woman had a total thyroidectomy with bilateral central neck '
                                 'dissection for papillary carcinoma 18 hours ago. She now has perioral '
                                 'numbness, carpal spasm, and a positive Chvostek sign. Calcium is 6.8 '
                                 'mg/dL, intact PTH is undetectable, and ECG shows a QTc of 510 ms. She is '
                                 'alert and her airway is normal. What is the most appropriate immediate '
                                 'management?',
                         'choices': ['Oral calcium carbonate alone and recheck calcium tomorrow',
                                     'Rapid IV push of calcium chloride through a hand vein',
                                     'Oral cholecalciferol with calcium citrate and discharge',
                                     'IV calcium gluconate, then oral calcium with calcitriol'],
                         'answer': 3,
                         'explanation': 'Symptomatic hypocalcemia with tetany signs and QT prolongation '
                                        'needs prompt intravenous calcium gluconate, given as a slow bolus '
                                        'and then an infusion with cardiac monitoring. Her undetectable PTH '
                                        'indicates postoperative hypoparathyroidism, so oral calcium must be '
                                        'paired with calcitriol, which bypasses the PTH-dependent renal '
                                        '1-alpha-hydroxylation that cholecalciferol requires. Magnesium is '
                                        'checked and repleted. Calcium is followed every few hours until '
                                        'stable on oral therapy before discharge.',
                         'why_wrong': ['Oral calcium alone is too slow and too weak for symptomatic '
                                       'hypocalcemia with QT prolongation and absent PTH.',
                                       'Calcium chloride through a small peripheral vein risks severe tissue '
                                       'necrosis if extravasated, and rapid pushes can cause arrhythmia.',
                                       'Without PTH, cholecalciferol cannot be activated efficiently, and '
                                       'discharge is unsafe until symptoms and the QT interval resolve.',
                                       'Correct.'],
                         'board_pearl': 'Symptomatic post-thyroidectomy hypocalcemia: IV calcium gluconate '
                                        'first, then oral calcium plus calcitriol.',
                         'curveball': 'How can an early postoperative PTH help stratify calcium replacement '
                                      'and discharge planning?',
                         'curveball_answer': 'A PTH drawn within hours of thyroidectomy predicts '
                                             'hypocalcemia. A very low or undetectable value, roughly below '
                                             '10 to 15 pg/mL depending on assay, identifies patients who '
                                             'benefit from immediate calcium and calcitriol and closer '
                                             'monitoring, while a normal value supports early discharge with '
                                             'minimal or no supplementation. Protocols differ in cutoffs.'},
 'v236_tps_hungry_snr': {'stem': 'A 48-year-old man on hemodialysis for 9 years has severe secondary '
                                 'hyperparathyroidism with PTH over 2,000 pg/mL, alkaline phosphatase five '
                                 'times normal, bone pain, and radiographic subperiosteal resorption. He is '
                                 'scheduled for subtotal parathyroidectomy. His nephrologist asks the '
                                 'surgeon what to plan for after surgery. What is the most appropriate '
                                 'postoperative plan?',
                         'choices': ['Begin calcitriol preoperatively and monitor calcium closely with '
                                     'nephrology',
                                     'Routine discharge on postoperative day 1 with standard oral calcium',
                                     'Withhold calcium until he develops symptoms, to avoid hypercalcemia',
                                     'Stop phosphate binders and add oral phosphate after surgery'],
                         'answer': 0,
                         'explanation': 'Renal hyperparathyroidism with very high PTH, marked alkaline '
                                        'phosphatase elevation, and radiographic bone disease carries the '
                                        'highest risk of severe and prolonged hungry bone syndrome. Planning '
                                        'begins before surgery: calcitriol or another active vitamin D '
                                        'analog is often started preoperatively. Afterward, calcium is '
                                        'checked every few hours, with intravenous calcium as needed, '
                                        'high-dose oral calcium, active vitamin D, and dialysate calcium '
                                        'adjusted in coordination with nephrology. Requirements can remain '
                                        'high for weeks.',
                         'why_wrong': ['Correct.',
                                       'He is at very high risk for hungry bone and may need intravenous '
                                       'calcium for days, so early routine discharge is unsafe.',
                                       'Waiting for symptoms risks seizures and arrhythmia in a patient '
                                       'expected to have a profound and rapid calcium fall.',
                                       'Adding phosphate binds calcium and worsens hypocalcemia, and '
                                       'dialysis patients already have phosphate retention.'],
                         'board_pearl': 'Dialysis patients with high alkaline phosphatase are highest risk '
                                        'for hungry bone; plan intensive calcium and active vitamin D.',
                         'curveball': 'How do poor renal clearance and delayed PTH kinetics complicate '
                                      'interpretation of intraoperative PTH in this patient?',
                         'curveball_answer': 'In renal failure, PTH fragments are cleared slowly, so '
                                             'intraoperative PTH declines more gradually and may not fall by '
                                             '50% within 10 minutes despite adequate resection. Surgeons '
                                             'often use a larger or later drop, such as 70 to 80% at 15 to '
                                             '20 minutes, and rely on gross findings of all glands rather '
                                             'than the standard Miami criterion alone.'},
 'v113-end-03': {'stem': 'A 52-year-old man had a left superficial parotidectomy for a pleomorphic adenoma '
                         '14 months ago. He now reports that the skin in front of his left ear becomes red '
                         'and damp whenever he eats, especially sour foods, and he carries a napkin to wipe '
                         'it. There is no pain, swelling, or drainage from the incision. Facial nerve '
                         'function is normal. What is the most likely diagnosis?',
                 'choices': ['First-bite syndrome',
                             'Salivary cutaneous fistula',
                             'Facial nerve synkinesis',
                             'Frey syndrome'],
                 'answer': 3,
                 'explanation': 'Frey syndrome, or gustatory sweating, typically appears months after '
                                'parotidectomy. During healing, transected postganglionic parasympathetic '
                                'fibers in the auriculotemporal nerve, which previously stimulated parotid '
                                'secretion, regenerate into the overlying skin and connect with sweat glands '
                                'and vessels that use acetylcholine. Eating then triggers sweating and '
                                'flushing over the preauricular area. Many patients have subclinical '
                                'findings on starch-iodine testing, but only a minority are bothered enough '
                                'to seek treatment.',
                 'why_wrong': ['First-bite syndrome causes cramping pain with the first bites of a meal, not '
                               'sweating and flushing of the skin.',
                               'A salivary fistula leaks saliva from an opening in the incision, whereas his '
                               'skin is intact and simply flushes and sweats.',
                               'Synkinesis causes involuntary movements after facial nerve injury, and his '
                               'facial function is normal.',
                               'Correct.'],
                 'board_pearl': 'Gustatory sweating and flushing months after parotidectomy is Frey '
                                'syndrome; pain with the first bite is first-bite syndrome.',
                 'curveball': 'He asks what could have prevented this and what can now be done. Which '
                              'options reduce symptomatic gustatory sweating?',
                 'curveball_answer': 'Prevention uses a thick skin flap and an interposition barrier such as '
                                     'an SMAS flap, sternocleidomastoid flap, temporoparietal fascia, or '
                                     'acellular dermis between the parotid bed and skin. Treatment of '
                                     'symptoms begins with topical antiperspirants or anticholinergics, and '
                                     'intradermal botulinum toxin to the mapped skin is the most effective, '
                                     'typically lasting about a year and repeatable.'},
 'v135_tps_03': {'stem': 'A 46-year-old woman had a right superficial parotidectomy 11 months ago. She now '
                         'notices flushing and beads of sweat over the right preauricular cheek whenever she '
                         'eats. There is no pain or swelling, and facial movement is normal. A starch-iodine '
                         'test outlines a 4-by-5-cm area that turns dark blue when she chews a lemon drop. '
                         'Her resident asks what has happened at the tissue level. Which mechanism best '
                         'explains her symptoms?',
                 'choices': ['Loss of sympathetic input to parotid myoepithelial cells',
                             'Regenerated parasympathetic fibers innervating cutaneous sweat glands',
                             'Saliva leaking through a tract between the gland and the skin',
                             'Facial nerve branches regenerating into the wrong muscle groups'],
                 'answer': 1,
                 'explanation': 'Frey syndrome results from aberrant regeneration. Postganglionic '
                                'parasympathetic fibers that travel from the otic ganglion through the '
                                'auriculotemporal nerve to the parotid are cut during parotidectomy. As they '
                                'regrow, some enter the overlying skin and reach sweat glands and dermal '
                                'vessels. Sweat glands are sympathetically innervated but use acetylcholine '
                                'at their receptors, so the misrouted parasympathetic fibers can drive them, '
                                'and every meal triggers sweating and flushing. The starch-iodine (Minor) '
                                'test maps the area.',
                 'why_wrong': ['Loss of sympathetic input to the gland produces first-bite syndrome, which '
                               'causes pain rather than skin sweating.',
                               'Correct.',
                               'A salivary leak drains fluid from an opening, whereas the starch-iodine test '
                               'here shows sweat across intact skin.',
                               'Misdirected facial nerve regeneration causes synkinesis, which produces '
                               'abnormal movement rather than sweating.'],
                 'board_pearl': 'Frey syndrome is cholinergic parasympathetic fibers misdirected to '
                                'cholinergic sweat glands in the parotidectomy skin flap.',
                 'curveball': 'Her sister now needs a parotidectomy. What intraoperative reconstructive '
                              'maneuver can reduce the incidence of this problem?',
                 'curveball_answer': 'Placing a barrier between the parotid bed and the skin flap reduces '
                                     'gustatory sweating. Options include an SMAS plication or flap, a '
                                     'superiorly based sternocleidomastoid flap, temporoparietal fascia, or '
                                     'acellular dermal matrix. A thicker flap elevated deep to the '
                                     'subcutaneous fat and a partial rather than complete superficial '
                                     'parotidectomy also lower the risk.'},
 'v237_tps_frey_fnd': {'stem': 'A 33-year-old man had open reduction and internal fixation of a left '
                               'mandibular condylar fracture through a preauricular approach 10 months ago. '
                               'He now reports that the skin over his left temple and in front of his ear '
                               'sweats and turns red within a minute of starting a meal. There is no pain, '
                               'jaw clicking, or swelling, and his facial movements are symmetric. What is '
                               'the most likely diagnosis?',
                       'choices': ['First-bite syndrome from sympathetic denervation',
                                   'Gustatory sweating from auriculotemporal nerve injury',
                                   'Auriculotemporal neuralgia with referred flushing',
                                   'Salivary sialocele related to the parotid capsule'],
                       'answer': 1,
                       'explanation': 'Frey syndrome is gustatory sweating and flushing caused by aberrant '
                                      'regeneration of injured auriculotemporal nerve fibers. Although it is '
                                      'best known after parotidectomy, any surgery or trauma near the '
                                      'auriculotemporal nerve can cause it, including preauricular '
                                      'approaches to the condyle and temporomandibular joint, facelift '
                                      'dissection, and parotid lacerations. Parasympathetic fibers bound for '
                                      'the parotid regrow into the skin and stimulate sweat glands with '
                                      'meals. The distribution follows the auriculotemporal territory over '
                                      'the temple and preauricular skin.',
                       'why_wrong': ['First-bite syndrome causes cramping parotid-region pain at the start '
                                     'of meals rather than sweating and flushing.',
                                     'Correct.',
                                     'Neuralgia causes paroxysmal burning or stabbing pain in the temple, '
                                     'and he has no pain at all.',
                                     'A sialocele is a fluctuant collection of saliva under the skin, not '
                                     'sweating and flushing of intact skin.'],
                       'board_pearl': 'Frey syndrome can follow any injury to the auriculotemporal nerve, '
                                      'including condylar and TMJ approaches.',
                       'curveball': 'What bedside test can objectively map the area of his gustatory '
                                    'sweating?',
                       'curveball_answer': 'The Minor starch-iodine test maps it. Iodine solution is painted '
                                           'on the dry skin, starch powder is dusted over it once dry, and '
                                           'he chews a sialogogue such as a lemon drop. Sweat dissolves the '
                                           'iodine into the starch, which turns dark blue-black over the '
                                           'affected skin. The outlined area guides botulinum toxin '
                                           'injection.'},
 'v237_tps_frey_app': {'stem': 'A 60-year-old woman has had embarrassing sweating over her right cheek with '
                               'every meal since a parotidectomy 2 years ago. She soaks a handkerchief at '
                               'business dinners. Two months of topical aluminum chloride antiperspirant '
                               'gave little benefit. Starch-iodine testing maps a 5-by-6-cm area of '
                               'preauricular and cheek skin. Facial nerve function is normal. What is the '
                               'most effective next treatment?',
                       'choices': ['Intraparotid botulinum toxin injected into the residual parotid gland',
                                   'Tympanic neurectomy to interrupt Jacobson nerve fibers',
                                   'Revision surgery to place an SMAS flap beneath the skin',
                                   'Intradermal botulinum toxin A injected across the mapped skin'],
                       'answer': 3,
                       'explanation': 'Botulinum toxin A blocks acetylcholine release at the nerve terminals '
                                      'that drive sweat glands. Injected intradermally in a grid across the '
                                      'area mapped by the starch-iodine test, it eliminates or markedly '
                                      'reduces gustatory sweating in most patients within days. Benefit '
                                      'usually lasts many months to more than a year as nerve sprouting '
                                      'gradually restores function, and injections can be repeated safely. '
                                      'Injections near the oral commissure are kept superficial to avoid '
                                      'weakening lip depressors.',
                       'why_wrong': ['Intraparotid injection targets salivary myoepithelial contraction in '
                                     'first-bite syndrome and does not reach the cutaneous sweat glands.',
                                     'Tympanic neurectomy has inconsistent, often temporary benefit and is '
                                     'far more invasive than a proven injection therapy.',
                                     'Revision flap surgery is invasive and less reliable than botulinum '
                                     'toxin, which is the first-line treatment for established symptoms.',
                                     'Correct.'],
                       'board_pearl': 'Intradermal botulinum toxin to the starch-iodine-mapped skin is '
                                      'first-line treatment for bothersome Frey syndrome.',
                       'curveball': 'Part of her mapped area extends to within 1 cm of the oral commissure. '
                                    'How does that change injection planning?',
                       'curveball_answer': 'Toxin diffusing into the depressor anguli oris, zygomaticus, or '
                                           'orbicularis oris can cause temporary lip asymmetry or drooling. '
                                           'Near the commissure, injections are kept strictly intradermal, '
                                           'use lower doses, and are spaced farther from the mouth. Patients '
                                           'are warned that any weakness resolves as the toxin wears off.'},
 'v237_tps_frey_snr': {'stem': 'A 39-year-old woman is planned for a right superficial parotidectomy for a '
                               '2.5-cm pleomorphic adenoma in the superficial lobe. She has no prior surgery '
                               'or radiation, and facial nerve function is normal. She is a teacher who is '
                               'worried about gustatory sweating after reading online forums. The tumor '
                               'margins are well defined on MRI. Which intraoperative step would most reduce '
                               'her risk of clinically significant Frey syndrome?',
                       'choices': ['Raising a thin skin flap in the immediate subdermal plane',
                                   'Ligating Stensen duct to reduce remaining salivary flow',
                                   'Placing an SMAS flap or acellular dermis over the parotid bed',
                                   'Applying a pressure dressing for 5 days after surgery'],
                       'answer': 2,
                       'explanation': 'Frey syndrome occurs when regenerating parasympathetic fibers cross '
                                      'from the exposed parotid bed into the skin flap. A physical barrier '
                                      'between the two reduces clinically significant gustatory sweating. '
                                      'Options include an SMAS flap or plication, a superiorly based '
                                      'sternocleidomastoid flap, temporoparietal fascia, and acellular '
                                      'dermal matrix, which also improves contour. The choice is balanced '
                                      'against oncologic exposure, donor morbidity, and cost. Thicker flaps '
                                      'and partial superficial parotidectomy add further protection.',
                       'why_wrong': ['Thin flaps bring regenerating parasympathetic fibers closer to the '
                                     'dermal sweat glands and increase the risk of Frey syndrome.',
                                     'Duct ligation does not stop nerve regeneration into the skin and can '
                                     'cause painful obstructive swelling of the residual gland.',
                                     'Correct.',
                                     'Pressure dressings reduce seroma and sialocele but do not create a '
                                     'barrier to aberrant nerve regeneration.'],
                       'board_pearl': 'An interposed barrier, such as an SMAS flap, sternocleidomastoid '
                                      'flap, or acellular dermis, reduces Frey syndrome after parotidectomy.',
                       'curveball': 'How does uncertainty about the oncologic margin affect the choice to '
                                    'place interposition tissue?',
                       'curveball_answer': 'When margins are uncertain or a malignancy is suspected, the bed '
                                           'must remain accessible for surveillance, re-excision, and '
                                           'radiation planning. Bulky flaps can obscure recurrence on exam '
                                           'and imaging. Surgeons therefore favor thin local tissue, such as '
                                           'an SMAS plication, or defer elaborate reconstruction until final '
                                           'pathology confirms a benign tumor or clear margins.'},
 'v113-end-04': {'stem': 'A 53-year-old woman had transcervical resection of a 5-cm prestyloid '
                         'parapharyngeal space pleomorphic adenoma 6 weeks ago. She now has a sharp, '
                         'cramping pain in the left parotid region with the first bite of every meal. The '
                         'pain is worst with sour foods, lasts about 20 seconds, and fades with continued '
                         'chewing. Facial nerve function is normal and there is no swelling or sweating. '
                         'What is the most likely diagnosis?',
                 'choices': ['Frey syndrome',
                             'Temporomandibular joint dislocation',
                             'Glossopharyngeal neuralgia',
                             'First-bite syndrome'],
                 'answer': 3,
                 'explanation': 'First-bite syndrome is intense pain in the parotid region with the first '
                                'bites of a meal that diminishes as eating continues. It follows surgery '
                                'that disrupts the sympathetic supply to the parotid, such as parapharyngeal '
                                'space, deep-lobe parotid, and skull-base resections or external carotid '
                                'ligation. Loss of sympathetic input is thought to cause denervation '
                                'hypersensitivity of myoepithelial cells, which contract excessively with '
                                'the first parasympathetic salivary stimulus. Sour foods provoke the '
                                'strongest response.',
                 'why_wrong': ['Frey syndrome causes painless sweating and flushing of the skin during meals '
                               'rather than cramping pain at the first bite.',
                               'Joint dislocation causes an open-lock jaw and pain with every movement, not '
                               'brief pain that fades with continued chewing.',
                               'Glossopharyngeal neuralgia causes stabbing throat and ear pain triggered by '
                               'swallowing, not parotid pain easing as a meal continues.',
                               'Correct.'],
                 'board_pearl': 'Severe parotid pain at the first bite that fades with chewing, after '
                                'parapharyngeal surgery, is first-bite syndrome.',
                 'curveball': 'She asks why this happens and whether an injection could help. Which '
                              'autonomic pathway is implicated, and why might botulinum toxin help?',
                 'curveball_answer': 'The sympathetic supply to the parotid, from the superior cervical '
                                     'ganglion along the external carotid artery, is disrupted, leaving '
                                     'myoepithelial cells hypersensitive to parasympathetic stimulation from '
                                     'the otic ganglion. Intraparotid botulinum toxin blocks acetylcholine '
                                     'release from those parasympathetic fibers, reducing the exaggerated '
                                     'contraction and pain at the start of meals.'},
 'v135_tps_02': {'stem': 'A 44-year-old man underwent resection of a 4-cm poststyloid parapharyngeal space '
                         'schwannoma arising from the cervical sympathetic trunk 3 months ago. Since then, '
                         'the first mouthful of each meal causes a stabbing pain beneath his right ear that '
                         'lasts seconds and eases as he keeps eating. He has mild right ptosis and miosis. '
                         'The parotid is soft without masses, and the oral exam is normal. What is the most '
                         'likely diagnosis?',
                 'choices': ['Obstructive parotid sialolithiasis with sialadenitis',
                             'Auriculotemporal gustatory sweating syndrome',
                             'Masseteric myofascial pain from surgical positioning',
                             'First-bite syndrome after sympathetic injury'],
                 'answer': 3,
                 'explanation': 'Resection of a sympathetic chain schwannoma removes sympathetic input to '
                                'the head, causing Horner syndrome and, by denervating the parotid, '
                                'first-bite syndrome. The hallmark is severe pain with the first bite of '
                                'each meal that subsides with continued chewing, explained by denervation '
                                'hypersensitivity of parotid myoepithelial cells to parasympathetic '
                                'stimulation. His ipsilateral ptosis and miosis confirm sympathetic injury. '
                                'Symptoms often improve over months, and initial management is reassurance '
                                'with dietary strategies.',
                 'why_wrong': ['Sialolithiasis causes swelling that builds during and after meals and lasts '
                               'hours, not seconds of pain that fades with chewing.',
                               'Auriculotemporal (Frey) syndrome produces painless sweating and flushing '
                               'over the cheek rather than pain at the first bite.',
                               'Myofascial pain worsens with prolonged chewing and has trigger points, '
                               'whereas his pain is greatest at the first bite and then fades.',
                               'Correct.'],
                 'board_pearl': 'Horner syndrome plus first-bite pain after parapharyngeal surgery points to '
                                'sympathetic chain injury.',
                 'curveball': 'Six months later his first-bite pain is still disabling despite reassurance. '
                              'What nonoperative treatments can be considered?',
                 'curveball_answer': 'Many patients improve over months, so initial care is reassurance and '
                                     'eating strategies such as starting meals with bland, non-sour foods '
                                     'and gentle massage. If pain stays disabling, neuropathic agents such '
                                     'as gabapentin or carbamazepine can be tried, and intraparotid '
                                     'botulinum toxin injection, often under ultrasound guidance, provides '
                                     'the most consistent relief.'},
 'v237_tps_firstbite_fnd': {'stem': 'A 58-year-old woman had a total parotidectomy with facial nerve '
                                    'preservation for a deep-lobe oncocytoma that required ligation of the '
                                    'external carotid artery behind the mandible. Two months later, she '
                                    'reports a severe cramp near the angle of her jaw each time she starts a '
                                    'meal, which subsides after several bites. She has no flushing, '
                                    'sweating, or swelling, and the facial nerve functions normally. What is '
                                    'the most likely cause of her pain?',
                            'choices': ['Loss of sympathetic input to remaining parotid tissue',
                                        'Aberrant parasympathetic regrowth into the skin',
                                        'Neuroma of the great auricular nerve at its stump',
                                        'Retained duct stone obstructing the parotid remnant'],
                            'answer': 0,
                            'explanation': 'Deep-lobe parotid surgery and external carotid ligation disrupt '
                                           'the sympathetic fibers that travel to the parotid along the '
                                           'external carotid artery. Residual parotid tissue then has '
                                           'unopposed parasympathetic innervation, and denervation '
                                           'hypersensitivity of the myoepithelial cells produces intense '
                                           'contraction and pain at the first salivary stimulus of a meal. '
                                           'The pain fades as the meal continues. Facial nerve function and '
                                           'skin findings are normal, distinguishing it from Frey syndrome '
                                           'and nerve injury.',
                            'why_wrong': ['Correct.',
                                          'Parasympathetic regrowth into the skin causes painless gustatory '
                                          'sweating and flushing, which she does not have.',
                                          'A great auricular neuroma causes localized tenderness and '
                                          'tingling of the earlobe that is not tied to the first bite of a '
                                          'meal.',
                                          'Obstruction produces swelling that builds through the meal and '
                                          'lasts hours, rather than brief pain that fades with eating.'],
                            'board_pearl': 'First-bite syndrome follows deep-lobe parotid, parapharyngeal, '
                                           'or external carotid surgery that disrupts parotid sympathetic '
                                           'supply.',
                            'curveball': 'Her colleague asks which other head and neck operations are most '
                                         'associated with first-bite syndrome. What are they?',
                            'curveball_answer': 'Parapharyngeal space resections, especially poststyloid '
                                                'tumors such as sympathetic chain schwannomas and '
                                                'paragangliomas, deep-lobe parotidectomy, infratemporal '
                                                'fossa and skull-base surgery, and procedures requiring '
                                                'external carotid ligation are most often implicated. '
                                                'Removal of the superior cervical ganglion carries the '
                                                'highest risk, and the syndrome can occur even when the '
                                                'parotid is left intact.'},
 'v237_tps_firstbite_app': {'stem': 'A 62-year-old man developed first-bite syndrome after resection of a '
                                    'vagal paraganglioma 9 months ago. Despite reassurance, starting meals '
                                    'with bland foods, and a 3-month trial of gabapentin, he still has '
                                    'severe pain with every first bite and has lost 5 kg because he avoids '
                                    'meals. Exam shows a soft parotid gland and normal facial movement. What '
                                    'is the most appropriate next treatment?',
                            'choices': ['Ultrasound-guided intraparotid botulinum toxin injection',
                                        'Intradermal botulinum toxin over the preauricular skin',
                                        'Completion parotidectomy to remove the denervated gland',
                                        'Microvascular decompression of the glossopharyngeal nerve'],
                            'answer': 0,
                            'explanation': 'First-bite syndrome often improves over months, but persistent '
                                           'severe symptoms that limit eating warrant treatment. After '
                                           'failed conservative measures and neuropathic medication, '
                                           'intraparotid botulinum toxin is the most consistently effective '
                                           'option. It blocks acetylcholine release from parasympathetic '
                                           'terminals and reduces the exaggerated myoepithelial contraction '
                                           'at the first salivary stimulus. Injection, often '
                                           'ultrasound-guided, is distributed across the gland and repeated '
                                           'as needed. Weight loss here makes treatment pressing.',
                            'why_wrong': ['Correct.',
                                          'Intradermal injection targets sweat glands for Frey syndrome and '
                                          'does not reach the parotid myoepithelial cells driving his pain.',
                                          'Parotidectomy adds facial nerve risk and has not been shown to be '
                                          'a reliable cure, so less invasive therapy comes first.',
                                          'Microvascular decompression treats glossopharyngeal neuralgia '
                                          'from vascular compression, which is not the mechanism here.'],
                            'board_pearl': 'Refractory first-bite syndrome: intraparotid botulinum toxin; '
                                           'Frey syndrome: intradermal botulinum toxin.',
                            'curveball': 'Why might xerostomia risk influence the dose and distribution of '
                                         'his injections?',
                            'curveball_answer': 'Botulinum toxin also reduces salivary secretion from the '
                                                'injected parotid, and after head and neck treatment some '
                                                'patients already have reduced saliva. Using the lowest '
                                                'effective dose, distributing it across the gland under '
                                                'ultrasound guidance, and avoiding the submandibular gland '
                                                'limit dry mouth and dental risk while still controlling '
                                                'pain.'},
 'v237_tps_firstbite_snr': {'stem': 'A 50-year-old woman is being counseled before transcervical resection '
                                    'of a 6-cm poststyloid parapharyngeal space schwannoma of the '
                                    'sympathetic chain. She has normal pupils and no Horner syndrome today. '
                                    'Her parotid gland will not be removed. She has read about postoperative '
                                    'jaw pain with eating and asks how likely it is and what it would mean. '
                                    'Which counseling statement is most accurate?',
                            'choices': ['It can occur with the parotid intact, and severity often lessens '
                                        'over months',
                                        'It occurs only after the parotid gland itself has been removed '
                                        'during surgery',
                                        'It reflects facial nerve injury and appears together with facial '
                                        'weakness',
                                        'Once present, it is permanent and steadily worsens over subsequent '
                                        'years'],
                            'answer': 0,
                            'explanation': 'Resection of a sympathetic chain schwannoma carries a high risk '
                                           'of first-bite syndrome because the superior cervical ganglion or '
                                           'its postganglionic fibers supply the parotid. The syndrome '
                                           'reflects autonomic imbalance with unopposed parasympathetic '
                                           'stimulation of parotid myoepithelial cells, so it occurs even '
                                           'when the gland is untouched. Patients should hear that pain at '
                                           'the first bites of meals is common after such surgery, that '
                                           'severity varies, and that it often improves, with botulinum '
                                           'toxin available for refractory cases.',
                            'why_wrong': ['Correct.',
                                          "The syndrome results from loss of the parotid's sympathetic "
                                          'supply, which can happen with the gland fully preserved.',
                                          'First-bite syndrome is an autonomic disorder, and facial nerve '
                                          'function is typically normal.',
                                          'Symptoms are often worst early and tend to improve over months, '
                                          'though some patients have persistent pain.'],
                            'board_pearl': 'Sympathetic chain surgery carries a high risk of first-bite '
                                           'syndrome even without parotid removal; counsel before surgery.',
                            'curveball': 'How does preexisting sympathetic dysfunction, such as a '
                                         'preoperative Horner syndrome, affect the expected risk?',
                            'curveball_answer': 'A preoperative Horner syndrome suggests the sympathetic '
                                                'chain is already nonfunctional, so surgery removes less '
                                                'remaining input and first-bite syndrome appears less '
                                                'likely. In practice, the risk is highest when an intact, '
                                                'functioning sympathetic chain is sacrificed. This can be '
                                                'framed as a counseling point, though data remain limited.'},
 'v134_tps_01': {'stem': 'A healthy 46-year-old woman has a 7-mm left thyroid nodule with FNA showing '
                         'papillary carcinoma, Bethesda VI. Ultrasound shows an intrathyroidal tumor '
                         'surrounded by normal thyroid, with no extrathyroidal extension, no contact with '
                         'the trachea or nerve course, and no suspicious central or lateral nodes. She is '
                         'reliable and strongly prefers to avoid surgery. What is the most appropriate '
                         'management?',
                 'choices': ['Total thyroidectomy followed by adjuvant radioactive iodine remnant ablation',
                             'Active surveillance with ultrasound at 6 to 12 months and set triggers',
                             'Lobectomy with prophylactic ipsilateral central neck dissection',
                             'Radioactive iodine alone, without surgery, to treat the primary tumor'],
                 'answer': 1,
                 'explanation': 'Low-risk papillary microcarcinomas, 1 cm or smaller, without extrathyroidal '
                                'extension, nodes, aggressive cytology, or proximity to the trachea or '
                                'recurrent nerve, rarely progress, and the Japanese and later cohorts showed '
                                'safe delayed surgery for those that do. ATA guidance accepts active '
                                'surveillance as an alternative to immediate surgery in suitable, reliable '
                                'patients. Surveillance is structured: ultrasound every 6 to 12 months '
                                'initially, with intervention for growth of 3 mm or more, new nodal disease, '
                                'or patient preference.',
                 'why_wrong': ['Total thyroidectomy with radioiodine overtreats a very low-risk '
                               'microcarcinoma and exposes her to unnecessary nerve and parathyroid risk.',
                               'Correct.',
                               'Prophylactic central dissection adds parathyroid and nerve morbidity without '
                               'a proven survival benefit in clinically node-negative microcarcinoma.',
                               'Radioiodine needs prior thyroid removal and does not treat an intact primary '
                               'tumor, so it has no role here.'],
                 'board_pearl': 'Low-risk papillary microcarcinoma away from trachea and nerve: active '
                                'surveillance is a legitimate alternative to surgery.',
                 'curveball': 'Her 7-mm tumor instead abuts the tracheoesophageal groove where future growth '
                              'could threaten the recurrent nerve. How does that change your recommendation?',
                 'curveball_answer': 'Location near the recurrent laryngeal nerve or trachea is an exclusion '
                                     'for active surveillance, because even small growth can invade critical '
                                     'structures and make later surgery more morbid. Immediate lobectomy is '
                                     'recommended for such tumors despite their size. Subcapsular dorsal '
                                     'tumors adjacent to the nerve course and tumors abutting the trachea at '
                                     'an obtuse angle carry the highest risk.'},
 'v137_tps_04': {'stem': 'A 41-year-old woman has a 1.4-cm right thyroid nodule with FNA showing classic '
                         'papillary carcinoma. Ultrasound shows the tumor confined to the right lobe, a '
                         'normal left lobe, and no suspicious central or lateral nodes. She has no radiation '
                         'history or family history. She does not want surveillance and prefers surgery that '
                         'preserves her own thyroid function if possible. Which operation is most '
                         'appropriate?',
                 'choices': ['Total thyroidectomy with planned radioiodine',
                             'Total thyroidectomy with bilateral central neck dissection',
                             'Right thyroid lobectomy',
                             'Right lobectomy with prophylactic right central neck dissection'],
                 'answer': 2,
                 'explanation': 'Contemporary risk-adapted management treats low-risk unifocal '
                                'intrathyroidal differentiated thyroid cancer with the least extensive '
                                'adequate operation. Under ATA 2025, lobectomy is an appropriate definitive '
                                'operation for low-risk tumors up to 2 cm without extrathyroidal extension, '
                                'nodal disease, or contralateral nodules. It avoids bilateral nerve and '
                                'parathyroid risk and often allows her to remain off levothyroxine. Outcomes '
                                'for low-risk disease are equivalent to total thyroidectomy, and radioiodine '
                                'is generally not needed.',
                 'why_wrong': ['Routine total thyroidectomy with radioiodine offers no survival benefit for '
                               'low-risk unifocal disease and increases complications.',
                               'Bilateral central dissection in a node-negative patient raises the risk of '
                               'permanent hypoparathyroidism without proven benefit.',
                               'Correct.',
                               'Prophylactic central dissection is not routinely recommended for small '
                               'node-negative papillary carcinoma and adds parathyroid risk.'],
                 'board_pearl': 'Low-risk unifocal papillary carcinoma up to 2 cm, cN0: lobectomy is an '
                                'appropriate definitive operation.',
                 'curveball': 'If she has a lobectomy, what final pathologic findings would make a later '
                              'completion thyroidectomy more reasonable?',
                 'curveball_answer': 'Gross extrathyroidal extension, positive margins, aggressive subtypes '
                                     'such as tall cell or hobnail, extensive vascular invasion, clinically '
                                     'significant nodal metastases (more than five, or any over 2 mm), and '
                                     'contralateral cancer favor completion thyroidectomy, especially if '
                                     'radioiodine is planned. Minor microscopic extension or a few '
                                     'micrometastases alone usually do not.'},
 'v143_tps_01': {'stem': 'A 38-year-old man has a 1.5-cm left thyroid nodule with FNA showing papillary '
                         "carcinoma. The referring physician's limited ultrasound measured only the nodule. "
                         'He has no voice change, the right lobe was not described, and he has no radiation '
                         'history. He is scheduled to discuss lobectomy next week. Before the extent of '
                         'surgery is finalized, which evaluation is most important?',
                 'choices': ['Contrast-enhanced CT of the chest to screen for pulmonary metastases',
                             'Serum thyroglobulin to estimate the tumor burden before surgery',
                             'Comprehensive ultrasound of the thyroid and central and lateral neck nodes',
                             'Whole-body iodine-123 scan to detect distant iodine-avid disease'],
                 'answer': 2,
                 'explanation': 'Lobectomy is appropriate only when the cancer is truly low risk, so '
                                'preoperative ultrasound must evaluate the contralateral lobe and both '
                                'central and lateral neck nodes. Finding contralateral nodules, suspicious '
                                'nodes, or extrathyroidal extension changes the operation to total '
                                'thyroidectomy, with therapeutic neck dissection for proven nodes. '
                                'Suspicious nodes are sampled with FNA and thyroglobulin washout. '
                                'Cross-sectional imaging is reserved for bulky or invasive disease, and '
                                'laryngoscopy is added for voice change or posterior extension.',
                 'why_wrong': ['Chest CT is not routine for low-risk papillary carcinoma and is reserved for '
                               'extensive nodal disease or suspected distant spread.',
                               'Preoperative thyroglobulin is not useful while the thyroid is in place and '
                               'does not alter the extent of surgery.',
                               'Correct.',
                               'Iodine scanning before thyroidectomy is not informative because the intact '
                               'thyroid takes up the tracer.'],
                 'board_pearl': 'Before choosing lobectomy for thyroid cancer, a complete neck ultrasound '
                                'must confirm unilateral, node-negative disease.',
                 'curveball': 'What adverse preoperative or intraoperative finding would make total '
                              'thyroidectomy or nodal surgery more compelling?',
                 'curveball_answer': 'Biopsy-proven lateral or central nodes require total thyroidectomy '
                                     'with therapeutic compartment dissection. Gross extrathyroidal '
                                     'extension, contralateral malignant or suspicious nodules, a tumor over '
                                     '4 cm, distant metastases, and a history of head and neck radiation '
                                     'also favor total thyroidectomy. Intraoperative gross invasion or '
                                     'abnormal nodes found at surgery should prompt conversion or frozen '
                                     'section.'},
 'v146_tps_02': {'stem': 'A 52-year-old woman has been on active surveillance for 3 years for an 8-mm '
                         'papillary microcarcinoma of the right lobe, which has remained stable in size. Her '
                         'latest ultrasound shows a new 1.1-cm right level IV node that is round, with loss '
                         'of the fatty hilum and cystic change. She feels well and her voice is normal. What '
                         'is the most appropriate next step?',
                 'choices': ['Continue surveillance and repeat ultrasound in 6 months',
                             'Ultrasound-guided FNA of the node with thyroglobulin washout',
                             'Total thyroidectomy with bilateral lateral neck dissection',
                             'Radioactive iodine without further surgery or sampling'],
                 'answer': 1,
                 'explanation': 'Active surveillance has explicit exit criteria: tumor growth of 3 mm or '
                                'more, new nodal metastasis, extrathyroidal extension, or patient '
                                'preference. A round node with loss of the fatty hilum and cystic change is '
                                'highly suspicious for papillary carcinoma metastasis. It should be '
                                'confirmed with ultrasound-guided FNA, adding thyroglobulin measurement in '
                                'the needle washout to increase sensitivity, especially in cystic nodes. '
                                'Confirmation leads to total thyroidectomy with right lateral neck '
                                'dissection, typically levels II through IV.',
                 'why_wrong': ['New suspicious nodal disease is a predefined trigger to leave surveillance, '
                               'so waiting is no longer appropriate even with a stable primary.',
                               'Correct.',
                               'Surgery should follow cytologic confirmation, and a contralateral lateral '
                               'dissection is not indicated without evidence of left-sided disease.',
                               'Radioiodine cannot be given with the thyroid in place and does not '
                               'substitute for surgical clearance of nodal disease.'],
                 'board_pearl': 'New suspicious node during active surveillance: confirm with FNA and '
                                'thyroglobulin washout, then convert to surgery.',
                 'curveball': 'How does proximity to the recurrent laryngeal nerve or trachea alter '
                              'surveillance candidacy, even without growth?',
                 'curveball_answer': 'Tumors abutting the trachea, especially at an obtuse angle, or lying '
                                     "along the dorsal capsule in the nerve's course are excluded from "
                                     'surveillance even if stable, because small increases could invade '
                                     'those structures and make later surgery more morbid. Such patients are '
                                     'offered surgery at diagnosis.'},
 'v233_tps_dtc_fnd': {'stem': 'A 44-year-old man has a 1.9-cm left thyroid nodule. FNA shows papillary '
                              'carcinoma, and comprehensive neck ultrasound shows a normal right lobe, no '
                              'extrathyroidal extension, and no suspicious central or lateral nodes. He has '
                              'no radiation exposure and no family history. His voice is normal. He asks '
                              'which operation the current ATA framework supports. What is the most '
                              'appropriate operation?',
                      'choices': ['Total thyroidectomy with routine radioiodine',
                                  'Left thyroid lobectomy alone',
                                  'Total thyroidectomy and prophylactic central neck dissection',
                                  'Near-total thyroidectomy leaving a small posterior remnant'],
                      'answer': 1,
                      'explanation': 'Under ATA 2025, low-risk differentiated thyroid cancer is treated with '
                                     'the least extensive adequate operation, and lobectomy is an '
                                     'appropriate definitive operation for unifocal intrathyroidal tumors up '
                                     'to 2 cm without nodal disease or extrathyroidal extension. His 1.9-cm '
                                     'tumor fits this category. Lobectomy avoids bilateral nerve and '
                                     'parathyroid risk, often spares lifelong levothyroxine, and gives '
                                     'survival equivalent to total thyroidectomy for low-risk disease. Total '
                                     'thyroidectomy is reserved for higher-risk features.',
                      'why_wrong': ['Routine radioiodine after total thyroidectomy for low-risk disease adds '
                                    'toxicity without improving survival or recurrence.',
                                    'Correct.',
                                    'Prophylactic central dissection in clinically node-negative disease '
                                    'increases hypoparathyroidism risk without improving survival.',
                                    'Near-total thyroidectomy still exposes both nerves and parathyroid sets '
                                    'while leaving tissue that complicates surveillance.'],
                      'board_pearl': 'ATA 2025: lobectomy is appropriate for low-risk unifocal '
                                     'differentiated thyroid cancer up to 2 cm without nodes or extension.',
                      'curveball': 'Which preoperative findings would shift the recommendation toward total '
                                   'thyroidectomy or therapeutic nodal surgery?',
                      'curveball_answer': 'Biopsy-proven nodal metastases, gross extrathyroidal extension, '
                                          'distant metastases, contralateral suspicious or malignant '
                                          'nodules, prior head and neck radiation, a strong family history, '
                                          'and tumors larger than 4 cm favor total thyroidectomy. Proven '
                                          'nodal disease additionally requires therapeutic dissection of the '
                                          'involved central or lateral compartments.'},
 'v233_tps_dtc_app': {'stem': 'A 49-year-old woman has a 3.2-cm right papillary carcinoma on FNA. Ultrasound '
                              'shows no extrathyroidal extension, no suspicious nodes, and a normal left '
                              'lobe. She has no radiation history. She values avoiding lifelong '
                              'levothyroxine but worries about needing a second operation. Her '
                              'endocrinologist asks the surgeon how to counsel her under current ATA '
                              'guidance. Which statement is most accurate?',
                      'choices': ['Total thyroidectomy is required because the tumor is larger than 2 cm',
                                  'Lobectomy or total thyroidectomy are both reasonable, chosen with her '
                                  'preferences',
                                  'Total thyroidectomy with prophylactic bilateral central dissection is '
                                  'required',
                                  'Active surveillance with ultrasound every 6 months is a reasonable '
                                  'alternative'],
                      'answer': 1,
                      'explanation': 'For intrathyroidal differentiated cancer larger than 2 cm and up to 4 '
                                     'cm, without nodal disease or gross extension, current ATA guidance '
                                     'allows either lobectomy or total thyroidectomy. The choice is '
                                     'individualized by tumor features, contralateral nodules, the '
                                     'likelihood that final pathology will prompt completion surgery or '
                                     'radioiodine, surveillance preferences, and patient values. She should '
                                     'hear that lobectomy may avoid levothyroxine but carries a chance of '
                                     'completion if adverse pathology is found.',
                      'why_wrong': ['Size over 2 cm alone does not mandate total thyroidectomy for an '
                                    'intrathyroidal, node-negative tumor up to 4 cm.',
                                    'Correct.',
                                    'Prophylactic bilateral central dissection is not required in clinically '
                                    'node-negative disease and raises hypoparathyroidism risk.',
                                    'Active surveillance is reserved for low-risk microcarcinomas about 1 cm '
                                    'or smaller, not 3-cm tumors.'],
                      'board_pearl': 'Intrathyroidal node-negative differentiated cancer over 2 cm up to 4 '
                                     'cm: lobectomy or total thyroidectomy by shared decision.',
                      'curveball': 'How would a suspicious contralateral nodule or a plan to give '
                                   'radioiodine alter the choice?',
                      'curveball_answer': 'A suspicious or malignant contralateral nodule means bilateral '
                                          'disease, so total thyroidectomy addresses both sides in one '
                                          'operation. If radioiodine is likely, for example because of '
                                          'high-risk features, total thyroidectomy is needed because a '
                                          'remaining lobe absorbs the iodine. Either finding tips the shared '
                                          'decision toward total thyroidectomy.'},
 'v233_tps_dtc_snr': {'stem': 'A 37-year-old woman underwent right lobectomy for a 1.6-cm Bethesda V nodule. '
                              'Final pathology shows classic papillary carcinoma, intrathyroidal, unifocal, '
                              'with negative margins, no vascular invasion, and two benign perithyroidal '
                              'nodes. Postoperative ultrasound shows a normal left lobe. Her TSH is normal '
                              'without levothyroxine. She asks whether she now needs her remaining thyroid '
                              'removed. What is the best response?',
                      'choices': ['Yes; completion is required so that radioiodine ablation can be given',
                                  'No; lobectomy is definitive, with ultrasound surveillance of the neck',
                                  'Yes; completion is needed because thyroglobulin cannot be interpreted',
                                  'No; and no further follow-up is needed after a benign lymph node result'],
                      'answer': 1,
                      'explanation': 'Final pathology confirms low-risk disease: an intrathyroidal unifocal '
                                     'papillary carcinoma under 2 cm with negative margins and no vascular '
                                     'invasion or nodal metastases. Under current ATA guidance, lobectomy is '
                                     'definitive treatment for this risk group. Completion thyroidectomy is '
                                     'selective and is reserved for features that create real benefit, such '
                                     'as aggressive histology, gross extension, significant nodal disease, '
                                     'or contralateral cancer. She can be followed with periodic neck '
                                     'ultrasound and TSH monitoring.',
                      'why_wrong': ['Radioiodine is not recommended for low-risk intrathyroidal papillary '
                                    'carcinoma, so it does not justify completion surgery.',
                                    'Correct.',
                                    'Thyroglobulin is less useful with a lobe in place, but neck ultrasound '
                                    'provides effective surveillance without reoperation.',
                                    'She still needs periodic neck ultrasound because recurrences, though '
                                    'uncommon, are treatable when detected early.'],
                      'board_pearl': 'After lobectomy with favorable final pathology, completion '
                                     'thyroidectomy is selective, not automatic.',
                      'curveball': 'Had her final pathology been less favorable, which adverse findings '
                                   'would have made completion thyroidectomy more compelling?',
                      'curveball_answer': 'Gross extrathyroidal extension, positive margins, aggressive '
                                          'subtypes such as tall cell, hobnail, or columnar, widespread '
                                          'vascular invasion, more than five involved nodes or any nodal '
                                          'metastasis over 2 mm, and a contralateral cancer would favor '
                                          'completion thyroidectomy, particularly when radioiodine therapy '
                                          'is planned.'},
 'v134_tps_02': {'stem': 'A 50-year-old woman underwent left lobectomy for a 2.3-cm Bethesda IV nodule. '
                         'Final pathology shows a minimally invasive follicular carcinoma with capsular '
                         'invasion only, no vascular invasion, negative margins, and no aggressive features. '
                         'Preoperative ultrasound showed a normal right lobe and normal nodes. She feels '
                         'well and asks what comes next. What is the most appropriate next step?',
                 'choices': ['Completion thyroidectomy followed by radioiodine remnant ablation',
                             'Completion thyroidectomy with bilateral central neck dissection',
                             'Neck ultrasound surveillance without completion thyroidectomy',
                             'Radioiodine ablation of the remaining right lobe without surgery'],
                 'answer': 2,
                 'explanation': 'Completion thyroidectomy is now selective. Minimally invasive follicular '
                                'carcinoma with capsular invasion only and no vascular invasion behaves as '
                                'low-risk disease, and lobectomy is adequate treatment. Removing the '
                                'remaining lobe adds bilateral nerve and parathyroid risk with little '
                                'oncologic gain. The decision should be driven by adverse pathology, such as '
                                'vascular invasion, gross extension, or aggressive histology, the need for '
                                'radioiodine, contralateral disease, and patient preference rather than a '
                                'cancer diagnosis alone.',
                 'why_wrong': ['Low-risk minimally invasive follicular carcinoma without vascular invasion '
                               'does not benefit from routine completion and radioiodine.',
                               'Central neck dissection is not indicated for a node-negative follicular '
                               'carcinoma, which spreads hematogenously rather than to nodes.',
                               'Correct.',
                               'Ablating an intact lobe requires high activities, causes radiation '
                               'thyroiditis, and is not a standard substitute for surgery.'],
                 'board_pearl': 'Low-risk differentiated cancer after lobectomy does not automatically need '
                                'completion; weigh benefit against reoperative risk.',
                 'curveball': 'Final pathology instead shows gross extrathyroidal extension and multiple '
                              'clinically significant nodal metastases. What reasons now favor completion?',
                 'curveball_answer': 'Gross extension and significant nodal disease place her in a '
                                     'higher-risk tier in which radioiodine is often recommended, and '
                                     'radioiodine requires total thyroid removal to work. Completion also '
                                     'removes possible contralateral disease, allows thyroglobulin to be '
                                     'used as a sensitive tumor marker, and permits TSH suppression '
                                     'strategies tailored to the higher risk of recurrence.'},
 'v141_tps_06': {'stem': 'A 47-year-old man underwent right lobectomy for an indeterminate nodule, and final '
                         'pathology shows a 1.5-cm intrathyroidal papillary carcinoma with negative margins '
                         'and no adverse features. His left lobe is normal on ultrasound. A colleague '
                         'suggests completion thyroidectomy to be safe, and the patient asks the surgeon why '
                         'that might be avoided. What is the main reason completion thyroidectomy is not '
                         'recommended for him?',
                 'choices': ['Small added oncologic benefit is outweighed by reoperative nerve and '
                             'parathyroid risk',
                             'Reoperation must wait 12 months, which delays treatment past the point of '
                             'benefit',
                             'Radioiodine given to the remaining lobe can substitute for surgical completion',
                             'Completion would commit him to lifelong TSH suppression to undetectable '
                             'levels'],
                 'answer': 0,
                 'explanation': 'For a low-risk intrathyroidal papillary carcinoma under 2 cm with negative '
                                'margins, lobectomy is definitive. Completion thyroidectomy would expose the '
                                'remaining recurrent nerve and the contralateral parathyroids to injury, '
                                'raising the risk of permanent hypoparathyroidism and, if the first nerve '
                                'were affected, bilateral paralysis, while adding little to survival or '
                                'recurrence. It would also commit him to levothyroxine. Completion is '
                                'reserved for findings that make total thyroid management meaningfully '
                                'beneficial.',
                 'why_wrong': ['Correct.',
                               'Completion can be done early, within days, or after several months when the '
                               'field has settled; timing is not the barrier.',
                               'Radioiodine is ineffective and impractical in an intact lobe and would not '
                               'be indicated for his low-risk disease anyway.',
                               'TSH targets after total thyroidectomy are risk-adapted, and low-risk '
                               'patients are not kept at undetectable TSH levels.'],
                 'board_pearl': 'Completion thyroidectomy should provide a defined benefit; for low-risk '
                                'disease, the reoperative risk outweighs it.',
                 'curveball': 'How would gross extrathyroidal extension or significant nodal disease change '
                              'the balance?',
                 'curveball_answer': 'Gross extension or clinically significant nodal metastases move him '
                                     'into a higher risk category in which radioiodine is often recommended. '
                                     'Because radioiodine requires removal of the remaining lobe, the '
                                     'benefit of completion now outweighs its reoperative risk. Completion '
                                     'also clears possible contralateral disease and allows thyroglobulin to '
                                     'serve as a sensitive marker of recurrence.'},
 'v238_tps_completion_fnd': {'stem': 'A 39-year-old woman had a right lobectomy for a 2.8-cm Bethesda V '
                                     'nodule. Final pathology shows papillary carcinoma with a '
                                     'microscopically positive posterior margin and six metastatic central '
                                     'nodes, two larger than 5 mm. The tumor board recommends completion '
                                     'thyroidectomy before radioiodine. She asks what that operation '
                                     'actually involves. Which description of completion thyroidectomy is '
                                     'most accurate?',
                             'choices': ['Re-excision of the right lobectomy bed to clear the margin only',
                                         'Dissection of the right central compartment lymph nodes only',
                                         'Removal of the remaining left lobe and any isthmus remnant',
                                         'Radioiodine ablation of the left lobe in place of surgery'],
                             'answer': 2,
                             'explanation': 'Completion thyroidectomy removes the residual thyroid after a '
                                            'prior unilateral operation, converting lobectomy to total '
                                            'thyroidectomy. Its indications come from final pathology and '
                                            'risk assessment, such as positive margins, significant nodal '
                                            'disease, aggressive histology, gross extension, or the need for '
                                            'radioiodine. Here, multiple nodal metastases larger than a few '
                                            'millimeters and a positive margin raise her risk tier, making '
                                            'radioiodine likely, so the left lobe must be removed. It is '
                                            'usually performed early (within about a week) or delayed '
                                            '(about 3 months).',
                             'why_wrong': ['Completion addresses the remaining thyroid; bed re-excision for '
                                           'a microscopic margin is not what the term describes.',
                                           'Central neck dissection treats nodes and may accompany '
                                           'completion, but it does not remove the remaining thyroid.',
                                           'Correct.',
                                           'Radioiodine is not a substitute for surgical completion and is '
                                           'ineffective in an intact lobe.'],
                             'board_pearl': 'Completion thyroidectomy removes the remaining lobe, usually to '
                                            'enable radioiodine or treat higher-risk disease.',
                             'curveball': 'Which postoperative pathology findings most often reopen the '
                                          'extent-of-thyroidectomy decision?',
                             'curveball_answer': 'Aggressive subtypes such as tall cell, hobnail, or '
                                                 'columnar, widely invasive follicular carcinoma or '
                                                 'extensive vascular invasion, gross extrathyroidal '
                                                 'extension, positive margins, significant nodal metastases '
                                                 '(more than five, or larger than 2 mm), and contralateral '
                                                 'or multifocal disease are the findings that most often '
                                                 'lead to completion thyroidectomy.'},
 'v238_tps_completion_app': {'stem': 'A 56-year-old woman had a left lobectomy for a 4.5-cm benign '
                                     'follicular nodule causing dysphagia. Final pathology shows the benign '
                                     'nodule plus an incidental separate 6-mm classic papillary carcinoma, '
                                     'intrathyroidal, with clear margins and no vascular invasion. Her right '
                                     'lobe is normal on ultrasound and she has no radiation history. What is '
                                     'the most appropriate management?',
                             'choices': ['No completion; periodic ultrasound and routine follow-up',
                                         'Completion thyroidectomy so that radioiodine can be given',
                                         'Completion thyroidectomy with prophylactic central dissection',
                                         'Radioiodine ablation of the right lobe without completion surgery'],
                             'answer': 0,
                             'explanation': 'Incidental papillary microcarcinomas found in lobectomy '
                                            'specimens are very low risk when intrathyroidal, unifocal, '
                                            'margin-negative, and without vascular invasion or nodal '
                                            'disease. Under current ATA guidance, lobectomy is definitive '
                                            'for such tumors, and completion surgery or radioiodine adds '
                                            'risk without benefit. She needs periodic neck ultrasound and '
                                            'TSH monitoring, often without levothyroxine if her remaining '
                                            'lobe maintains normal function. Completion is reserved for '
                                            'adverse features that make total thyroid management useful.',
                             'why_wrong': ['Correct.',
                                           'An incidental intrathyroidal microcarcinoma is very low risk, '
                                           'and radioiodine has no benefit for it.',
                                           'Central dissection in a clinically node-negative patient raises '
                                           'hypoparathyroidism risk without improving her excellent '
                                           'prognosis.',
                                           'Radioiodine to an intact lobe is not standard and is unnecessary '
                                           'for a very low-risk tumor.'],
                             'board_pearl': 'Incidental intrathyroidal papillary microcarcinoma after '
                                            'lobectomy: no completion thyroidectomy is needed.',
                             'curveball': 'How would gross extrathyroidal extension or significant nodal '
                                          'disease change the discussion?',
                             'curveball_answer': 'Either finding would move her into a higher-risk tier in '
                                                 'which radioiodine is often recommended, so completion '
                                                 'thyroidectomy becomes appropriate. A therapeutic neck '
                                                 'dissection would be added if nodal disease were clinically '
                                                 'evident. These features, rather than the cancer diagnosis '
                                                 'itself, are what make completion worthwhile.'},
 'v238_tps_completion_snr': {'stem': 'A 55-year-old man had a right lobectomy 4 months ago and has had '
                                     'persistent right vocal fold paralysis since. Pathology shows a 2.4-cm '
                                     'intrathyroidal papillary carcinoma with negative margins and two '
                                     'central nodal micrometastases under 2 mm. Ultrasound of the left lobe '
                                     'and neck is normal. A colleague suggests completion thyroidectomy for '
                                     'radioiodine. What is the most appropriate recommendation?',
                             'choices': ['Completion thyroidectomy with continuous nerve monitoring and '
                                         'radioiodine',
                                         'Ultrasound surveillance, avoiding reoperation on the only working '
                                         'nerve',
                                         'Completion thyroidectomy with a planned tracheostomy for airway '
                                         'safety',
                                         'Radioiodine ablation of the intact left lobe to avoid any '
                                         'reoperation'],
                             'answer': 1,
                             'explanation': 'An intrathyroidal tumor with only a few nodal micrometastases '
                                            'under 2 mm keeps him in a low-risk category, in which '
                                            'radioiodine and completion offer little benefit. His persistent '
                                            'right vocal fold paralysis means the left nerve is his only '
                                            'functioning nerve; injury would cause bilateral paralysis and '
                                            'likely tracheostomy. Reoperative surgery also has altered '
                                            'planes. The strength of any completion indication must justify '
                                            'that risk. Here surveillance with ultrasound, and thyroglobulin '
                                            'trends, is appropriate.',
                             'why_wrong': ['Even with monitoring, injury to the left nerve would cause '
                                           'bilateral paralysis, and his low-risk disease does not justify '
                                           'that risk.',
                                           'Correct.',
                                           'Planning a tracheostomy accepts a severe complication for a '
                                           'modest, uncertain benefit in low-risk disease.',
                                           'Radioiodine to an intact lobe is ineffective and not standard, '
                                           'and his risk category does not call for radioiodine.'],
                             'board_pearl': 'Before completion surgery, document vocal fold function; with a '
                                            'paralyzed side, only strong indications justify risking the '
                                            'last nerve.',
                             'curveball': 'When might a multidisciplinary nonoperative strategy be favored '
                                          'despite a theoretical completion indication?',
                             'curveball_answer': 'When the only functioning nerve is at risk, reoperation is '
                                                 'hazardous, or comorbidity limits surgery, the team may '
                                                 'choose surveillance with ultrasound and thyroglobulin, '
                                                 'active treatment only for structural recurrence, or '
                                                 'targeted local therapy. Radioiodine-based strategies '
                                                 'require completion, so the benefit of radioiodine must be '
                                                 'weighed against the risk to the airway and voice.'},
 'v134_tps_03': {'stem': 'A 68-year-old man had total thyroidectomy for a 1.8-cm low-risk papillary '
                         'carcinoma 6 years ago. Serial neck ultrasounds are normal and suppressed '
                         'thyroglobulin is undetectable with negative antibodies, an excellent response. He '
                         'developed paroxysmal atrial fibrillation last year, and DXA shows osteopenia. On '
                         'levothyroxine 175 mcg, his TSH is 0.03 mIU/L. What is the most appropriate change '
                         'to his thyroid hormone therapy?',
                 'choices': ['Continue the current dose to keep his TSH fully suppressed long term',
                             'Stop levothyroxine and monitor for recurrent disease',
                             'Switch to liothyronine to shorten the hormone half-life',
                             'Reduce levothyroxine to bring TSH into the low-normal range'],
                 'answer': 3,
                 'explanation': 'TSH suppression is risk-adapted and dynamic. TSH stimulates growth of '
                                'follicular-derived cancer cells, so suppression helps in higher-risk or '
                                'persistent disease. After an excellent response in low-risk disease, the '
                                'risk of recurrence is very low and suppression adds no benefit. Subclinical '
                                'hyperthyroidism increases atrial fibrillation and accelerates bone loss, '
                                'especially in older adults. ATA guidance supports a TSH target of roughly '
                                '0.5 to 2 mIU/L for excellent responders, and his levothyroxine should be '
                                'reduced accordingly.',
                 'why_wrong': ['Persistent suppression offers no meaningful benefit after an excellent '
                               'response and worsens atrial fibrillation and bone loss.',
                               'After total thyroidectomy he needs replacement to avoid hypothyroidism; the '
                               'goal is normal TSH, not no hormone.',
                               'Liothyronine produces fluctuating T3 peaks that can worsen arrhythmia and is '
                               'not a strategy for relaxing suppression.',
                               'Correct.'],
                 'board_pearl': 'Excellent response in low-risk DTC: target low-normal TSH; suppression '
                                'harms the heart and bones without benefit.',
                 'curveball': 'He instead has structurally persistent lung metastases despite therapy. How '
                              'would that shift the risk-benefit balance?',
                 'curveball_answer': 'With structural persistent disease, ATA guidance favors TSH '
                                     'suppression below 0.1 mIU/L in the absence of contraindications, '
                                     'because TSH drives tumor growth. His atrial fibrillation and '
                                     'osteopenia argue for moderating that target, perhaps to 0.1 to 0.5, '
                                     'with rate control, anticoagulation, and bone protection. The target '
                                     'balances tumor control against cardiac and skeletal harm.'},
 'v146_tps_06': {'stem': 'A 74-year-old woman had total thyroidectomy and radioiodine for intermediate-risk '
                         'papillary carcinoma 11 years ago. She has had an excellent response for 9 years, '
                         'with undetectable thyroglobulin and normal ultrasounds. She now has a painful '
                         'vertebral compression fracture and a lumbar T-score of -3.1. Her TSH on '
                         'levothyroxine is 0.05 mIU/L. What is the most appropriate thyroid management?',
                 'choices': ['Keep the current dose and add a bisphosphonate for her fracture',
                             'Keep the current dose and add a beta blocker to protect her heart',
                             'Repeat radioiodine imaging before deciding on any dose change',
                             'Lower the levothyroxine dose to bring TSH into the normal range'],
                 'answer': 3,
                 'explanation': 'Her recurrence risk has fallen substantially after 9 years of excellent '
                                'response, so ongoing suppression offers little benefit, while subclinical '
                                'hyperthyroidism accelerates bone loss and fracture risk in postmenopausal '
                                'women. ATA response-to-therapy reclassification supports relaxing her TSH '
                                'target to the low-normal or mid-normal range. Lowering the levothyroxine '
                                'dose removes a modifiable cause of osteoporosis, and she should also '
                                'receive appropriate osteoporosis treatment. TSH targets evolve with '
                                'response, age, and comorbidity.',
                 'why_wrong': ['A bisphosphonate treats osteoporosis but leaves the iatrogenic '
                               'hyperthyroidism contributing to bone loss in place.',
                               'A beta blocker addresses cardiac effects only and does not reduce the '
                               'skeletal harm of continued suppression.',
                               'Nine years of excellent response make diagnostic radioiodine imaging '
                               'unnecessary, and it does not change the dose decision.',
                               'Correct.'],
                 'board_pearl': 'TSH targets evolve with response; after durable excellent response, relax '
                                'suppression, especially with osteoporosis or arrhythmia.',
                 'curveball': 'Suppose she instead had persistent structural lung metastases. How would that '
                              'change the balance for this patient with a recent fracture?',
                 'curveball_answer': 'With structural persistent disease, TSH suppression below 0.1 is '
                                     'generally favored to slow tumor growth. Her severe osteoporosis and '
                                     'fracture would argue for a moderated target, about 0.1 to 0.5, while '
                                     'she receives antiresorptive therapy, so that tumor control is balanced '
                                     'against the high risk of further fractures.'},
 'v238_tps_rai_fnd': {'stem': 'A 41-year-old woman had total thyroidectomy and central neck dissection for a '
                              '3.5-cm papillary carcinoma with four central nodal metastases. Her '
                              'endocrinologist recommends adjuvant radioactive iodine, and a medical student '
                              'on the team asks why the treatment is selective for thyroid tissue and does '
                              'not affect her other organs equally. Which mechanism best explains '
                              'radioiodine selectivity?',
                      'choices': ['Binding to calcitonin receptors on parafollicular C cells',
                                  'Incorporation into hydroxyapatite at sites of bone turnover',
                                  'Uptake by any rapidly dividing malignant cell population',
                                  'Sodium-iodide symporter uptake by follicular-derived cells'],
                      'answer': 3,
                      'explanation': 'Follicular-derived thyroid cells express the sodium-iodide symporter '
                                     'on their basolateral membrane, which concentrates iodide, and thyroid '
                                     'peroxidase then organifies it. Differentiated papillary and follicular '
                                     'cancers often retain this machinery, so iodine-131 is concentrated in '
                                     'residual normal tissue and tumor, delivering beta radiation locally. '
                                     'TSH upregulates symporter expression, which is why TSH is raised '
                                     'before treatment. Salivary glands, stomach, and breast also express '
                                     'the symporter, explaining sialadenitis and other side effects.',
                      'why_wrong': ['C cells give rise to medullary carcinoma, which does not concentrate '
                                    'iodine, and radioiodine does not bind calcitonin receptors.',
                                    'Bone-seeking radiopharmaceuticals such as radium or strontium follow '
                                    'hydroxyapatite turnover; radioiodine does not.',
                                    'Iodine uptake depends on a specific transporter, not on proliferation, '
                                    'so many aggressive cancers do not take it up.',
                                    'Correct.'],
                      'board_pearl': 'Radioiodine works through the sodium-iodide symporter of '
                                     'follicular-derived cells; TSH stimulation increases uptake.',
                      'curveball': 'She is told she must stop levothyroxine or receive injections first. Why '
                                   'is elevated TSH needed before radioiodine treatment?',
                      'curveball_answer': 'TSH upregulates sodium-iodide symporter expression and iodine '
                                          'trapping in residual thyroid and cancer cells, increasing '
                                          'radioiodine uptake. A TSH above about 30 mIU/L is the '
                                          'conventional target, achieved by stopping levothyroxine for 3 to '
                                          '4 weeks or by recombinant human TSH injections, which avoid '
                                          'symptomatic hypothyroidism. A low-iodine diet also improves '
                                          'uptake.'},
 'v238_tps_rai_app': {'stem': 'A 34-year-old woman had total thyroidectomy for a 2.2-cm low-risk papillary '
                              'carcinoma 18 months ago, without radioiodine. Her nonstimulated thyroglobulin '
                              'is undetectable with negative antibodies, and neck ultrasound is normal, an '
                              'excellent response. She has no cardiac or bone disease. She is on '
                              'levothyroxine with a TSH of 0.08 mIU/L, and she reports palpitations and '
                              'insomnia. What is the most appropriate TSH target?',
                      'choices': ['About 0.5 to 2 mIU/L',
                                  'Below 0.1 mIU/L',
                                  'Between 0.1 and 0.5 mIU/L',
                                  'Above 4 mIU/L with low-dose levothyroxine'],
                      'answer': 0,
                      'explanation': 'TSH targets after differentiated thyroid cancer depend on initial risk '
                                     'and response to therapy. With low-risk disease and an excellent '
                                     'response, undetectable thyroglobulin, negative antibodies, and a '
                                     'normal ultrasound, recurrence risk is very low. ATA guidance supports '
                                     'a TSH in the low-normal range, about 0.5 to 2 mIU/L. Her current '
                                     'suppression causes symptoms of iatrogenic hyperthyroidism without '
                                     'oncologic benefit, so the dose should be reduced. Targets are '
                                     'reassessed as response evolves.',
                      'why_wrong': ['Correct.',
                                    'Suppression below 0.1 is reserved for structural persistent disease or '
                                    'high-risk patients and offers her no benefit.',
                                    'Mild suppression to 0.1 to 0.5 is used for biochemical incomplete or '
                                    'indeterminate responses, not for an excellent response.',
                                    'A TSH above the normal range leaves her hypothyroid and can stimulate '
                                    'growth of residual follicular tissue.'],
                      'board_pearl': 'Low-risk DTC with excellent response: target TSH about 0.5 to 2 mIU/L; '
                                     'avoid unneeded suppression.',
                      'curveball': 'How would atrial fibrillation or osteoporosis alter the target in a '
                                   'patient like her?',
                      'curveball_answer': 'With atrial fibrillation or osteoporosis, even a target near the '
                                          'lower end of normal can be relaxed toward the mid-normal range, '
                                          'because subclinical hyperthyroidism worsens both conditions. In '
                                          'patients who still need suppression for persistent disease, these '
                                          'comorbidities justify a moderated target with cardiac and bone '
                                          'protection.'},
 'v238_tps_rai_snr': {'stem': 'A 58-year-old man has lung metastases from papillary carcinoma. He has '
                              'received three radioiodine treatments over 4 years, totaling about 500 mCi. '
                              'Each post-therapy scan showed uptake in the lung nodules, but CT shows the '
                              'nodules grew after each of the last two treatments, and thyroglobulin is '
                              'rising. He has mild dry mouth and normal blood counts. What is the most '
                              'appropriate interpretation?',
                      'choices': ['A higher empiric radioiodine activity should be given next',
                                  'Repeat radioiodine at the same activity in 6 months',
                                  'The disease is radioiodine-refractory despite ongoing uptake',
                                  'Lithium should be added to enhance the next treatment'],
                      'answer': 2,
                      'explanation': 'Iodine avidity alone does not guarantee useful tumor response. Disease '
                                     'is considered radioiodine-refractory when tumors lose avidity, when '
                                     'some lesions are avid and others are not, or when lesions progress '
                                     'despite uptake after appropriate treatment, as here. Higher cumulative '
                                     'activities, roughly above 600 mCi, also make further benefit unlikely '
                                     'while raising risks of marrow suppression, salivary damage, pulmonary '
                                     'fibrosis, and secondary malignancy. Management shifts to surveillance, '
                                     'local therapy, or systemic targeted therapy.',
                      'why_wrong': ['Escalating activity adds cumulative marrow, salivary, and lung toxicity '
                                    'without evidence of benefit in disease progressing despite uptake.',
                                    'Repeating the same treatment that has twice failed to stop progression '
                                    'is unlikely to produce a different result.',
                                    'Correct.',
                                    'Lithium can prolong iodine retention, but it does not overcome '
                                    'biological resistance in tumors that progress despite uptake.'],
                      'board_pearl': 'Progression despite iodine uptake after appropriate treatment defines '
                                     'radioiodine-refractory disease; stop repeating radioiodine.',
                      'curveball': 'Looking back over his course, which findings suggest that differentiated '
                                   'thyroid cancer is becoming radioiodine-refractory?',
                      'curveball_answer': 'Lesions that lose or never show uptake on post-therapy scans, a '
                                          'mix of avid and non-avid lesions, progression within about a year '
                                          'of treatment despite uptake, high FDG avidity on PET, and '
                                          'persistent disease after high cumulative activities all suggest '
                                          'refractoriness. BRAF V600E and TERT promoter mutations, and '
                                          'aggressive histology, are associated with this behavior.'},
 'v134_tps_04': {'stem': 'A 66-year-old man with papillary carcinoma treated by total thyroidectomy and two '
                         'radioiodine courses has multiple lung metastases that showed no uptake on the last '
                         'post-therapy scan. CT shows the largest nodules growing from 8 to 13 mm over 12 '
                         'months. He has a mild cough but no dyspnea, and no lesions threaten the airway or '
                         'spine. What is the most appropriate next step?',
                 'choices': ['Molecular profiling of tumor tissue to guide the choice of therapy',
                             'A further empiric high-activity course of radioactive iodine',
                             'Bilateral pulmonary metastasectomy of all visible lung nodules',
                             'Supportive care only, waiting for life-threatening symptoms'],
                 'answer': 0,
                 'explanation': 'Radioiodine-refractory disease is managed by tempo, symptoms, and biology, '
                                'not by reflexive further radioiodine. His disease is progressing measurably '
                                'but is not yet causing major symptoms or threatening critical structures. '
                                'The next step is molecular profiling, which identifies actionable '
                                'alterations such as BRAF V600E, RET or NTRK fusions, and informs the choice '
                                'between multikinase inhibitors such as lenvatinib or sorafenib and '
                                'selective inhibitors. Profiling also supports trial eligibility. TSH '
                                'suppression continues.',
                 'why_wrong': ['Correct.',
                               'Non-avid metastases will not concentrate iodine, so another course adds '
                               'toxicity without benefit.',
                               'Multiple bilateral metastases are not suited to complete resection, and '
                               'surgery does not address microscopic disease.',
                               'Clear progression warrants planning before symptoms arise, since targeted '
                               'therapies can control disease and preserve function.'],
                 'board_pearl': 'Radioiodine-refractory disease: assess tempo and symptoms, profile the '
                                'tumor, and then choose observation, local, or systemic therapy.',
                 'curveball': 'One lesion is rapidly enlarging next to the spinal cord while the rest of his '
                              'disease is stable. Why might local therapy be preferable before changing '
                              'systemic therapy?',
                 'curveball_answer': 'A single threatening lesion can be controlled with stereotactic '
                                     'radiation or surgery without exposing him to the toxicity of systemic '
                                     'therapy, or without abandoning a systemic agent that is otherwise '
                                     'working. Local treatment prevents cord compression, a far greater risk '
                                     'to function than the stable remaining disease.'},
 'v146_tps_07': {'stem': 'A 61-year-old woman with radioiodine-refractory papillary carcinoma has been on '
                         'lenvatinib for 14 months with stable lung metastases. A new restaging MRI shows '
                         'one T10 vertebral metastasis that has enlarged and now extends into the epidural '
                         'space without cord compression. She has mild back pain and normal strength. All '
                         'other sites are stable. What is the most appropriate management?',
                 'choices': ['Switching from lenvatinib to a different multikinase inhibitor right away',
                             'A course of high-activity radioactive iodine for the spinal lesion',
                             'Increasing the lenvatinib dose and repeating the MRI in 3 months',
                             'Stereotactic radiation or surgery to T10 while continuing lenvatinib'],
                 'answer': 3,
                 'explanation': 'Oligoprogression, in which one site grows while the rest remains '
                                'controlled, is managed with local therapy to the threatening site while '
                                'continuing the effective systemic agent. Stereotactic body radiation, with '
                                'or without surgical decompression and stabilization, can control a '
                                'vertebral metastasis that threatens the cord. Bone metastases from thyroid '
                                'cancer can cause fractures and cord compression, and antiresorptive therapy '
                                'is often added. Switching systemic therapy is reserved for widespread '
                                'progression.',
                 'why_wrong': ['Changing therapy abandons an agent that controls all other disease, when '
                               'only one site is progressing.',
                               'The disease is radioiodine-refractory, so radioiodine will not treat the '
                               'spinal lesion and delays effective therapy.',
                               'Dose escalation adds toxicity and delays treatment of a lesion that already '
                               'threatens the spinal cord.',
                               'Correct.'],
                 'board_pearl': 'Oligoprogression of radioiodine-refractory disease: local therapy to the '
                                'threatening site, keep the working systemic agent.',
                 'curveball': 'What findings would trigger systemic kinase-inhibitor therapy in a patient '
                              'not yet on treatment?',
                 'curveball_answer': 'Systemic therapy is started for radioiodine-refractory disease that is '
                                     'clinically significant: progression by RECIST over about 12 to 14 '
                                     'months, symptomatic disease, bulky tumor burden, or metastases '
                                     'threatening vital structures that cannot be controlled locally. '
                                     'Low-volume, slowly progressive, asymptomatic disease is usually '
                                     'observed because kinase inhibitors carry real toxicity.'},
 'v238_tps_rrdtc_fnd': {'stem': 'A 59-year-old woman had total thyroidectomy and radioiodine for papillary '
                                'carcinoma with lateral nodal metastases. A year later, thyroglobulin is '
                                'rising. Her diagnostic and post-therapy whole-body scans show no uptake '
                                'outside the neck, but CT shows several enlarging 1-cm mediastinal nodes '
                                'that are intensely avid on FDG-PET. Ultrasound of the neck is unremarkable. '
                                'Which classification best fits her disease?',
                        'choices': ['Radioiodine-refractory structural disease',
                                    'Excellent response to initial therapy',
                                    'Biochemical incomplete response to therapy',
                                    'Indeterminate response to initial therapy'],
                        'answer': 0,
                        'explanation': 'She has structural disease that does not concentrate iodine but is '
                                       'FDG-avid and growing. This is radioiodine-refractory disease: '
                                       'lesions that lose or never show iodine uptake, show mixed uptake, or '
                                       'progress despite uptake. FDG avidity reflects dedifferentiation and '
                                       'higher glycolytic activity, and it often accompanies loss of the '
                                       'sodium-iodide symporter. This flip-flop pattern predicts more '
                                       'aggressive behavior. Further radioiodine is not useful, and '
                                       'management turns to local therapy, surveillance, or systemic '
                                       'targeted treatment.',
                        'why_wrong': ['Correct.',
                                      'An excellent response requires undetectable thyroglobulin and no '
                                      'structural disease, whereas she has rising markers and enlarging '
                                      'nodes.',
                                      'A biochemical incomplete response means elevated thyroglobulin '
                                      'without structural disease, but she has identified enlarging lesions.',
                                      'Indeterminate response describes nonspecific findings, whereas she '
                                      'has growing FDG-avid nodes with rising thyroglobulin.'],
                        'board_pearl': 'Iodine-negative, FDG-positive growing lesions signal '
                                       'dedifferentiated, radioiodine-refractory disease.',
                        'curveball': 'How can FDG avidity and lesion-to-lesion heterogeneity support the '
                                     'assessment of refractoriness?',
                        'curveball_answer': 'Lesions that are FDG-avid and iodine-negative are '
                                            'dedifferentiated and unlikely to respond to radioiodine, and a '
                                            'high FDG uptake value predicts worse survival. When some '
                                            'lesions take up iodine and others are FDG-avid without iodine '
                                            'uptake, the non-avid lesions will progress regardless of '
                                            'radioiodine, so the disease is managed as refractory.'},
 'v238_tps_rrdtc_app': {'stem': 'A 72-year-old man with radioiodine-refractory papillary carcinoma has six '
                                'lung nodules, the largest 9 mm. Over 18 months they have grown by less than '
                                '20% in total diameter. He has no cough, dyspnea, or bone pain, and no '
                                'lesions threaten the airway, vessels, or spinal cord. He has hypertension '
                                'and mild chronic kidney disease. What is the most appropriate management?',
                        'choices': ['Active surveillance with imaging every 3 to 6 months on TSH suppression',
                                    'Starting lenvatinib now because measurable metastatic disease exists',
                                    'A further empiric radioiodine course at a higher administered activity '
                                    'level',
                                    'Bilateral pulmonary metastasectomy to remove all detectable disease'],
                        'answer': 0,
                        'explanation': 'Systemic therapy for radioiodine-refractory thyroid cancer improves '
                                       'progression-free survival but carries substantial toxicity, '
                                       'including hypertension, proteinuria, fatigue, and diarrhea. For '
                                       'low-volume, slowly progressive, asymptomatic disease, ATA guidance '
                                       'favors active surveillance with periodic imaging and TSH '
                                       'suppression. Systemic treatment is reserved for clinically '
                                       'significant progression, symptoms, or threat to vital structures. '
                                       'His hypertension and renal disease would also increase VEGF '
                                       'inhibitor toxicity. Local therapy is used for focal threats.',
                        'why_wrong': ['Correct.',
                                      'Starting a kinase inhibitor for low-volume, slow, asymptomatic '
                                      'disease exposes him to hypertension, proteinuria, and renal toxicity '
                                      'without clear benefit.',
                                      'Radioiodine-refractory disease will not respond to more iodine, and '
                                      'further treatment adds cumulative toxicity.',
                                      'Multiple small bilateral nodules are not amenable to complete '
                                      'resection, and surgery offers no benefit over observation here.'],
                        'board_pearl': 'Slow, low-volume, asymptomatic radioiodine-refractory disease: '
                                       'surveillance; start kinase inhibitors for meaningful progression or '
                                       'symptoms.',
                        'curveball': 'Which disease sites make delay unsafe even when total tumor volume is '
                                     'modest?',
                        'curveball_answer': 'Metastases threatening the spinal cord, weight-bearing bones at '
                                            'risk of fracture, the brain, the trachea or major bronchi, the '
                                            'esophagus, or major vessels can cause catastrophic events even '
                                            'when total burden is small. These sites warrant local therapy '
                                            'such as stereotactic radiation or surgery, or earlier systemic '
                                            'treatment, rather than observation.'},
 'v238_tps_rrdtc_snr': {'stem': 'A 48-year-old woman has radioiodine-refractory papillary carcinoma with '
                                'growing, symptomatic lung and bone metastases. Next-generation sequencing '
                                'of her tumor shows a CCDC6-RET gene fusion, with no BRAF, RAS, or NTRK '
                                'alterations. She has not received systemic therapy and has good performance '
                                'status. Her oncologist asks the thyroid tumor board which systemic therapy '
                                'best matches her tumor biology. What is the most appropriate choice?',
                        'choices': ['Larotrectinib',
                                    'Dabrafenib plus trametinib',
                                    'Selpercatinib',
                                    'Cabozantinib'],
                        'answer': 2,
                        'explanation': 'Molecular profiling is standard for progressive '
                                       'radioiodine-refractory disease because actionable alterations change '
                                       'therapy. RET fusions occur in a minority of papillary carcinomas and '
                                       'drive tumor growth through constitutive RET kinase signaling. '
                                       'Selpercatinib is a highly selective RET inhibitor approved for RET '
                                       'fusion-positive thyroid cancer that needs systemic therapy and is '
                                       'radioiodine-refractory. It produces high response rates with less '
                                       'off-target VEGF toxicity than multikinase inhibitors. Lenvatinib '
                                       'remains an option when no target is found.',
                        'why_wrong': ['Larotrectinib targets NTRK gene fusions, which her tumor sequencing '
                                      'did not detect.',
                                      'Dabrafenib plus trametinib targets BRAF V600E-mutant tumors and is '
                                      'not effective against RET fusion-driven disease.',
                                      'Correct.',
                                      'Cabozantinib is approved after progression on prior VEGFR-targeted '
                                      'therapy and is less selective than a RET inhibitor for this tumor.'],
                        'board_pearl': 'Profile progressive radioiodine-refractory DTC: RET fusion to '
                                       'selpercatinib, NTRK to larotrectinib or entrectinib, BRAF V600E to '
                                       'dabrafenib-trametinib.',
                        'curveball': 'When can neoadjuvant targeted therapy change surgical resectability in '
                                     'locally advanced thyroid cancer?',
                        'curveball_answer': 'When a locally advanced tumor invades the trachea, larynx, or '
                                            'esophagus and resection would be highly morbid, selective '
                                            'inhibitors such as dabrafenib with trametinib for BRAF V600E or '
                                            'selpercatinib for RET can shrink the tumor. This has allowed '
                                            'less extensive resections in selected patients, though the '
                                            'approach is still under study and best done at experienced '
                                            'centers.'},
 'v134_tps_05': {'stem': 'A 72-year-old woman with Hashimoto thyroiditis on levothyroxine for 20 years has '
                         'noticed rapid enlargement of her thyroid over 5 weeks, with dysphagia to solids '
                         'and bulky bilateral cervical adenopathy. She has no stridor, and CT shows mild '
                         'tracheal deviation with a patent airway. FNA of the thyroid shows a monotonous '
                         'population of atypical lymphoid cells. What is the most appropriate next '
                         'diagnostic step?',
                 'choices': ['Total thyroidectomy for diagnosis and definitive treatment',
                             'Iodine-123 uptake scan to assess thyroid function',
                             'Repeat FNA in 3 months after levothyroxine adjustment',
                             'Core needle biopsy for histology with flow cytometry'],
                 'answer': 3,
                 'explanation': 'Rapid thyroid enlargement in an older woman with Hashimoto thyroiditis is '
                                'primary thyroid lymphoma until proven otherwise, most commonly diffuse '
                                'large B-cell or MALT lymphoma. FNA can suggest lymphoma but often cannot '
                                'classify it because architecture is lost. Core biopsy provides architecture '
                                'and tissue for immunohistochemistry, and flow cytometry adds '
                                'immunophenotype and clonality. Accurate classification matters because '
                                'treatment is chemoimmunotherapy and radiation, not thyroidectomy. Airway '
                                'stability is assessed at the same time.',
                 'why_wrong': ['Thyroidectomy is not the treatment for lymphoma, which is managed with '
                               'chemoimmunotherapy and radiation, and it adds nerve and parathyroid risk.',
                               'Uptake scanning does not provide a tissue diagnosis and does not distinguish '
                               'lymphoma from other causes of enlargement.',
                               'Waiting delays diagnosis of a rapidly growing tumor that may compromise the '
                               'airway.',
                               'Correct.'],
                 'board_pearl': 'Suspected thyroid lymphoma: core biopsy with flow cytometry for '
                                'classification; thyroidectomy is not the treatment.',
                 'curveball': 'She develops stridor while awaiting biopsy of the mass. What priorities now supersede the ideal diagnostic sequence?',
                 'curveball_answer': 'A threatened airway now comes first: involve anesthesia early, plan an awake fiberoptic or other airway-preserving technique, and have a surgical-airway team ready because a bulky gland can make tracheostomy difficult. Obtain diagnostic tissue as soon as it is safe, ideally before steroids, which can obscure lymphoma histology; if the airway is deteriorating, give steroids after a rapid core biopsy rather than delaying them.'},
 'v141_tps_05': {'stem': 'A 70-year-old woman has core-biopsy-proven diffuse large B-cell lymphoma of the '
                         'thyroid. Over 3 days, she has developed dyspnea when lying flat and mild '
                         'inspiratory noise, though her oxygen saturation is 96% on room air. CT shows the '
                         'tracheal lumen narrowed by about 50%. PET-CT shows disease limited to the thyroid '
                         'and neck nodes. What is the most appropriate management?',
                 'choices': ['Urgent chemoimmunotherapy with steroids, with airway backup planned',
                             'Total thyroidectomy to relieve compression and debulk the tumor',
                             'Elective tracheostomy under general anesthesia before starting chemotherapy',
                             'External-beam radiation to the neck alone as definitive therapy'],
                 'answer': 0,
                 'explanation': 'Diffuse large B-cell lymphoma of the thyroid is highly responsive to '
                                'steroids and chemoimmunotherapy, typically R-CHOP with or without '
                                'involved-site radiation. With tissue already obtained, urgent treatment '
                                'usually shrinks the tumor within days and relieves compression. She is '
                                'still oxygenating, so the safest plan is to start therapy promptly while '
                                'anesthesia and surgery stand ready to secure the airway if she '
                                'deteriorates. Thyroidectomy and routine tracheostomy add morbidity without '
                                'oncologic benefit.',
                 'why_wrong': ['Correct.',
                               'Thyroidectomy does not improve lymphoma outcomes and adds morbidity in a '
                               'tumor that shrinks rapidly with systemic therapy.',
                               'Tracheostomy through a large infiltrated thyroid is hazardous and is '
                               'unnecessary when she is oxygenating and treatment will work quickly.',
                               'Radiation alone has higher relapse rates for large B-cell lymphoma than '
                               'combined chemoimmunotherapy with radiation.'],
                 'board_pearl': 'Thyroid lymphoma with airway compression: diagnose, then treat urgently; '
                                'the tumor shrinks fast, so avoid surgery.',
                 'curveball': 'What biopsy method is preferred when FNA is nondiagnostic for suspected '
                              'thyroid lymphoma?',
                 'curveball_answer': 'Ultrasound-guided core needle biopsy is preferred because it preserves '
                                     'architecture and provides tissue for immunohistochemistry and flow '
                                     'cytometry. If cores are nondiagnostic or insufficient for subtyping, '
                                     'an open incisional biopsy of the thyroid or an accessible node is '
                                     'performed. Thyroidectomy is not used for diagnosis alone.'},
 'v238_tps_lymph_fnd': {'stem': 'A 69-year-old woman with long-standing hypothyroidism from Hashimoto '
                                'thyroiditis notices that her neck has swelled over 6 weeks, with a feeling '
                                'of pressure when swallowing. The swelling is painless. Exam shows a firm, '
                                'diffusely enlarged thyroid that is larger on the right, with mobile '
                                'cervical nodes. Ultrasound shows a markedly hypoechoic, pseudocystic mass '
                                'with posterior acoustic enhancement. Which diagnosis should be highest on '
                                'the differential?',
                        'choices': ['Benign colloid nodular goiter',
                                    'Primary thyroid lymphoma',
                                    'Riedel fibrosing thyroiditis',
                                    'Subacute granulomatous thyroiditis'],
                        'answer': 1,
                        'explanation': 'Primary thyroid lymphoma typically presents in older women with '
                                       'Hashimoto thyroiditis as rapid painless enlargement over weeks, '
                                       'often with compressive symptoms. Chronic autoimmune lymphoid '
                                       'stimulation predisposes to clonal B-cell expansion, so the risk is '
                                       'substantially higher than in the general population. Ultrasound '
                                       'often shows a markedly hypoechoic, pseudocystic mass with posterior '
                                       'enhancement. The key competing diagnosis is anaplastic carcinoma, '
                                       'which is usually hard, fixed, and often painful. Tissue diagnosis '
                                       'with core biopsy and flow cytometry is next.',
                        'why_wrong': ['Colloid nodules grow slowly over years and are not associated with '
                                      'rapid painless enlargement over weeks.',
                                      'Correct.',
                                      'Riedel thyroiditis causes a woody, fixed, hypovascular gland that '
                                      'grows slowly, not a rapidly expanding pseudocystic mass.',
                                      'Subacute thyroiditis is painful and tender after a viral illness, '
                                      'with transient thyrotoxicosis rather than painless growth.'],
                        'board_pearl': 'Rapid painless thyroid enlargement in an older woman with Hashimoto '
                                       'thyroiditis suggests thyroid lymphoma.',
                        'curveball': 'Which competing diagnosis is especially urgent when the mass is '
                                     'painful, fixed, and rapidly progressive?',
                        'curveball_answer': 'Anaplastic thyroid carcinoma is the critical alternative. It '
                                            'causes a hard, fixed, often painful mass, frequently with '
                                            'hoarseness or airway compromise, and can double in size over '
                                            'days to weeks. Urgent core biopsy with BRAF V600E testing is '
                                            'needed because BRAF-directed therapy has changed management, '
                                            'and airway planning must begin immediately.'},
 'v238_tps_lymph_app': {'stem': 'A 75-year-old woman with Hashimoto thyroiditis has a rapidly enlarging '
                                'thyroid mass with mild dysphagia and a stable airway. Two ultrasound-guided '
                                'core biopsies, taken 10 days apart, show only chronic lymphocytic '
                                'thyroiditis with fibrosis and crushed lymphoid cells, and flow cytometry is '
                                'inconclusive. Hematology says the samples are insufficient to exclude '
                                'lymphoma. What is the most appropriate next step?',
                        'choices': ['Total thyroidectomy for both diagnosis and definitive treatment',
                                    'Empiric R-CHOP chemotherapy without a confirmed tissue diagnosis',
                                    'Radioactive iodine to shrink the gland while the diagnosis is unclear',
                                    'Open incisional biopsy of the thyroid mass for full classification'],
                        'answer': 3,
                        'explanation': 'Lymphoma treatment depends on accurate classification. FNA and even '
                                       'core biopsies can be inconclusive when fibrosis, crush artifact, or '
                                       'a background of Hashimoto thyroiditis obscures architecture. After '
                                       'repeated nondiagnostic needle sampling, an open incisional biopsy '
                                       'provides enough fresh tissue for histology, immunohistochemistry, '
                                       'flow cytometry, and molecular studies. Total thyroidectomy is not '
                                       'needed for diagnosis and does not improve lymphoma outcomes. Tissue '
                                       'is sent fresh to pathology.',
                        'why_wrong': ['Total thyroidectomy adds nerve and parathyroid risk and is not the '
                                      'treatment for lymphoma, which an incisional biopsy can diagnose.',
                                      'Chemotherapy without a diagnosis risks treating the wrong disease and '
                                      'cannot be tailored to the lymphoma subtype.',
                                      'Radioiodine does not shrink lymphoma or establish a diagnosis, and it '
                                      'is not part of lymphoma management.',
                                      'Correct.'],
                        'board_pearl': 'Repeated nondiagnostic needle biopsies for suspected thyroid '
                                       'lymphoma: open incisional biopsy, not thyroidectomy.',
                        'curveball': 'Her family asks why a third needle biopsy is not being tried. When '
                                     'does open biopsy become preferable to repeated needle sampling?',
                        'curveball_answer': 'Open biopsy is preferred when two adequate core biopsies are '
                                            'nondiagnostic, when subtype classification requires more '
                                            'architecture or fresh tissue than needle cores provide, or when '
                                            'an accessible node can be excised more safely. It is planned '
                                            'with the airway in mind and avoided when the airway is '
                                            'critically narrowed.'},
 'v238_tps_lymph_snr': {'stem': 'A 67-year-old man has a rapidly enlarging thyroid mass over 4 weeks. He now '
                                'sleeps upright in a chair, speaks in short sentences, and has soft '
                                'inspiratory stridor. CT shows the trachea narrowed to 5 mm over a 3-cm '
                                'segment by a thyroid mass with bulky neck nodes. Lymphoma is strongly '
                                'suspected. A diagnosis is needed. What is the safest diagnostic approach?',
                        'choices': ['Excisional node biopsy under general anesthesia with inhalational '
                                    'induction',
                                    'Tracheostomy under general anesthesia, then thyroid biopsy',
                                    'Core biopsy under local anesthesia with him sitting upright',
                                    'Total thyroidectomy to both relieve compression and diagnose'],
                        'answer': 2,
                        'explanation': 'Critical tracheal narrowing with orthopnea and stridor makes general '
                                       'anesthesia hazardous: loss of muscle tone and the supine position '
                                       'can collapse an extrinsically compressed airway. Tissue is still '
                                       'needed, so the safest approach is ultrasound-guided core biopsy of '
                                       'the thyroid or an accessible node under local anesthesia with the '
                                       'patient upright. Anesthesia and surgery should be present with '
                                       'airway equipment and, in extreme cases, extracorporeal support '
                                       'ready. Treatment can then start promptly.',
                        'why_wrong': ['Induction of general anesthesia in the supine position can cause '
                                      'complete airway collapse in critical extrinsic compression.',
                                      'Tracheostomy through a large mass is technically difficult, and '
                                      'general anesthesia carries the same induction risks.',
                                      'Correct.',
                                      'Thyroidectomy is unnecessary for lymphoma, risky in this setting, and '
                                      'not required to obtain tissue.'],
                        'board_pearl': 'Critical airway with suspected lymphoma: obtain tissue under local '
                                       'anesthesia upright; avoid supine induction.',
                        'curveball': 'What symptoms or imaging findings should make routine supine induction '
                                     'particularly hazardous?',
                        'curveball_answer': 'Orthopnea, stridor, inability to lie flat, and syncope or '
                                            'cyanosis with position change suggest critical compression. On '
                                            'imaging, tracheal narrowing of more than half, compression '
                                            'extending into the mainstem bronchi, superior vena cava '
                                            'obstruction, and pericardial effusion indicate high risk. These '
                                            'findings call for awake or local techniques and extracorporeal '
                                            'standby.'},
 'v134_tps_06': {'stem': 'A 29-year-old woman has recurrent primary hyperparathyroidism 3 years after a '
                         'focused excision of a single enlarged gland. Calcium is 11.2 mg/dL with high PTH, '
                         'and urine calcium is elevated. Her father had a prolactinoma and her aunt had a '
                         'pancreatic neuroendocrine tumor. Sestamibi now shows uptake on the opposite side. '
                         'Before reoperative surgery is planned, which step is most important?',
                 'choices': ['Focused exploration of the sestamibi-positive side alone',
                             'Long-term cinacalcet to avoid any further neck surgery',
                             'Selective venous sampling as the primary next study',
                             'Germline MEN1 testing and evaluation for multigland disease'],
                 'answer': 3,
                 'explanation': 'Young age, recurrence after removal of a single gland, and relatives with '
                                'pituitary and pancreatic neuroendocrine tumors strongly suggest MEN1. In '
                                'MEN1, all four glands are usually abnormal, often asymmetrically, so '
                                'focused excision of the largest gland leads to persistent or recurrent '
                                'disease. Germline testing confirms the diagnosis, guides reoperation toward '
                                'subtotal or total parathyroidectomy with thymectomy, and triggers screening '
                                'for pituitary and pancreatic tumors and cascade testing of relatives.',
                 'why_wrong': ['A focused approach repeats the original error, since MEN1 is multigland '
                               'disease and chasing one gland risks further recurrence.',
                               'Cinacalcet controls calcium but does not address the cause in a young woman '
                               'who needs a durable treatment plan.',
                               'Venous sampling can help localize disease, but genetic evaluation must first '
                               'redefine the strategy and screening.',
                               'Correct.'],
                 'board_pearl': 'Young, recurrent hyperparathyroidism with pituitary or pancreatic tumors in '
                                'relatives: test for MEN1 before reoperation.',
                 'curveball': 'The prior pathology report notes capsular rupture with fragments of '
                              'parathyroid tissue left in the field. What additional cause of recurrence '
                              'should enter your differential?',
                 'curveball_answer': 'Parathyromatosis, the implantation of hyperfunctioning parathyroid '
                                     'tissue in the operative bed after capsular rupture, can cause '
                                     'recurrence as multiple small nodules scattered in the soft tissue. 4D '
                                     'CT or ultrasound may show several enhancing foci rather than one '
                                     'gland, and complete eradication can be difficult.'},
 'v146_tps_03': {'stem': 'A 26-year-old man with genetically confirmed MEN1 has primary hyperparathyroidism '
                         'with calcium 11.4 mg/dL and a kidney stone. Ultrasound shows enlargement of the '
                         'right inferior and left superior glands, and the other two are not seen. He has '
                         'had no neck surgery. The surgeon explains why the operation must address more than '
                         'the visible glands. Which operation is most appropriate?',
                 'choices': ['Subtotal parathyroidectomy after four-gland exploration',
                             'Focused excision of the largest gland with intraoperative PTH',
                             'Excision of only the two enlarged glands seen on ultrasound',
                             'Total parathyroidectomy without autotransplantation'],
                 'answer': 0,
                 'explanation': 'MEN1 hyperparathyroidism is multigland, often asymmetric hyperplasia. '
                                'Imaging frequently shows only the largest glands. Four-gland exploration '
                                'with subtotal parathyroidectomy, removing three and a half glands and '
                                'leaving a well-vascularized remnant, balances durable control against '
                                'permanent hypoparathyroidism. Transcervical thymectomy is added because '
                                'supernumerary glands and thymic carcinoids occur. Total parathyroidectomy '
                                'with forearm autotransplantation is an alternative. Lifelong surveillance '
                                'is required because recurrence is common over years.',
                 'why_wrong': ['Correct.',
                               'Intraoperative PTH can fall after removing one hyperplastic gland, falsely '
                               'suggesting cure in multigland MEN1 disease.',
                               'Glands that appear normal on imaging are usually hyperplastic in MEN1, and '
                               'leaving them causes early recurrence.',
                               'Total parathyroidectomy without autotransplantation guarantees permanent '
                               'hypoparathyroidism, which is worse than managed recurrence.'],
                 'board_pearl': 'MEN1 hyperparathyroidism: four-gland exploration with subtotal '
                                'parathyroidectomy and thymectomy, not focused surgery.',
                 'curveball': 'What is parathyromatosis, and why is avoiding capsular violation important in '
                              'surgery like his?',
                 'curveball_answer': 'Parathyromatosis is the implantation of hyperfunctioning parathyroid '
                                     'tissue in the neck or mediastinum, usually after capsular rupture or '
                                     'fragmentation during surgery. Because hyperplastic MEN1 glands are '
                                     'especially prone to seeding, surgeons remove glands intact and handle '
                                     'the remnant carefully, since implants cause recurrent disease that is '
                                     'very difficult to cure.'},
 'v239_tps_famhpt_fnd': {'stem': 'A 27-year-old woman has primary hyperparathyroidism with calcium 11.3 '
                                 'mg/dL, elevated PTH, and a urine calcium clearance ratio of 0.03. Her '
                                 'brother had a parathyroidectomy at 31 for multigland disease, and a cousin '
                                 'has hypercalcemia. She has no headaches, galactorrhea, or hypertension. '
                                 'Ultrasound shows two enlarged parathyroid glands. Before surgery is '
                                 'planned, what is the most important additional step?',
                         'choices': ['Focused excision of the larger of the two glands with intraoperative '
                                     'PTH monitoring',
                                     'DXA and observation until age 50 to see whether symptoms develop',
                                     'Genetic counseling and germline testing for hereditary '
                                     'hyperparathyroidism',
                                     'Total thyroidectomy combined with a four-gland parathyroid '
                                     'exploration'],
                         'answer': 2,
                         'explanation': 'Primary hyperparathyroidism before age 30, multigland disease, and '
                                        'affected relatives strongly suggest a hereditary syndrome, such as '
                                        'MEN1, MEN2A, CDC73-related hyperparathyroidism-jaw tumor syndrome, '
                                        'or familial isolated hyperparathyroidism. Her high urine calcium '
                                        'argues against FHH. Germline testing changes management: it '
                                        'determines the extent of parathyroid surgery, whether thymectomy is '
                                        'needed, screening for associated tumors, the possibility of '
                                        'parathyroid carcinoma, and testing of relatives. Pheochromocytoma '
                                        'must be excluded if a RET variant is found.',
                         'why_wrong': ['Focused surgery for likely multigland familial disease risks '
                                       'persistence and recurrence and ignores the syndrome.',
                                       'She meets surgical criteria by age alone, and observation does not '
                                       'address the hereditary question.',
                                       'Correct.',
                                       'Thyroidectomy is not indicated without thyroid pathology or a RET '
                                       'variant; the extent of neck surgery depends on genetic results.'],
                         'board_pearl': 'Young age, multigland disease, or affected relatives: genetic '
                                        'testing before parathyroid surgery shapes the operation.',
                         'curveball': 'Her germline testing confirms a pathogenic MEN1 variant. Which '
                                      'associated tumors should now be sought?',
                         'curveball_answer': 'MEN1 carriers need surveillance for pituitary adenomas, '
                                             'especially prolactinomas, pancreatic and duodenal '
                                             'neuroendocrine tumors such as gastrinomas and insulinomas, '
                                             'foregut carcinoids of the thymus, bronchus, and stomach, and '
                                             'adrenal cortical tumors. Surveillance uses periodic '
                                             'biochemical testing with prolactin, IGF-1, gastrin, and '
                                             'glucose, and MRI of the pituitary and pancreas.'},
 'v239_tps_famhpt_app': {'stem': 'A 34-year-old man with MEN1 has primary hyperparathyroidism and a kidney '
                                 'stone. Sestamibi shows intense uptake in a 2-cm right inferior gland, and '
                                 'the other glands are not visualized. He asks why the surgeon will not '
                                 'simply remove the one gland that lights up, as his coworker had done for a '
                                 'single adenoma. Which explanation is most accurate?',
                         'choices': ['Sestamibi is often falsely positive in MEN1, so the bright gland is '
                                     'likely normal',
                                     'MEN1 glands are all abnormal even when small, so multigland surgery is '
                                     'needed',
                                     'The bright gland is probably a carcinoma requiring en bloc thyroid '
                                     'resection',
                                     'Focused surgery would prevent a later thymectomy if one is ever '
                                     'required'],
                         'answer': 1,
                         'explanation': 'MEN1 hyperparathyroidism is multigland hyperplasia, usually '
                                        'asymmetric, so imaging often shows only the largest gland. Removing '
                                        'that gland may lower PTH briefly, but the remaining hyperplastic '
                                        'glands soon cause persistent or recurrent disease. Operations are '
                                        'designed around the expected biology: subtotal parathyroidectomy or '
                                        'total parathyroidectomy with autotransplantation, plus '
                                        'transcervical thymectomy, balancing durable control against '
                                        'permanent hypoparathyroidism. Lifelong surveillance is still needed '
                                        'because recurrence is common.',
                         'why_wrong': ['The bright gland is usually truly enlarged; the issue is that the '
                                       'nonvisualized glands are also hyperplastic.',
                                       'Correct.',
                                       'Parathyroid carcinoma is rare in MEN1 and is more characteristic of '
                                       'CDC73-related syndromes.',
                                       'Thymectomy can be performed later, and focused surgery is inadequate '
                                       'because of multigland biology, not because of thymectomy timing.'],
                         'board_pearl': 'In MEN1, the visible gland is only the largest of four abnormal '
                                        'glands; plan multigland surgery.',
                         'curveball': 'How does a prior subtotal parathyroidectomy change planning for '
                                      'recurrent MEN1 hyperparathyroidism?',
                         'curveball_answer': 'Recurrence usually arises from the remnant, a missed or '
                                             'supernumerary gland, or thymic tissue. Prior operative notes '
                                             "should identify the remnant's site, which ideally was marked "
                                             'with a clip or suture. Localization with 4D CT or ultrasound '
                                             'is essential. Reoperation targets the remnant or missed '
                                             'tissue, and laryngoscopy documents nerve function first. '
                                             'Cryopreservation of tissue helps if hypoparathyroidism '
                                             'results.'},
 'v239_tps_famhpt_snr': {'stem': 'A 63-year-old woman has recurrent hypercalcemia 8 years after a '
                                 'parathyroidectomy for a benign adenoma whose capsule tore during removal, '
                                 'and after a negative re-exploration 3 years ago. Calcium is 11.0 mg/dL '
                                 'with elevated PTH. 4D CT shows six small enhancing nodules, each under 8 '
                                 'mm, scattered in the soft tissue of the prior operative bed and strap '
                                 'muscles. What is the most likely diagnosis?',
                         'choices': ['Local recurrence of a parathyroid carcinoma',
                                     'Parathyromatosis from implanted parathyroid tissue',
                                     'A missed supernumerary parathyroid gland',
                                     'Reactive lymph nodes after prior neck surgery'],
                         'answer': 1,
                         'explanation': 'Parathyromatosis is the implantation and growth of hyperfunctioning '
                                        'parathyroid tissue in the neck or mediastinum, usually after '
                                        'capsular rupture or fragmentation during prior surgery. It causes '
                                        'recurrent hyperparathyroidism with multiple small nodules scattered '
                                        'in the soft tissue of the operative bed. Reoperation in a scarred '
                                        'neck requires detailed mapping, recurrent nerve assessment, and '
                                        'wide excision of involved tissue, and complete cure is difficult. '
                                        'Cinacalcet is often used for residual disease.',
                         'why_wrong': ['Carcinoma is unlikely after benign pathology and causes higher '
                                       'calcium with an invasive mass rather than tiny scattered implants.',
                                       'Correct.',
                                       'A supernumerary gland produces a single focus, often in the thymus, '
                                       'rather than multiple nodules in the operative bed.',
                                       'Reactive nodes do not secrete PTH and would not explain recurrent '
                                       'PTH-dependent hypercalcemia.'],
                         'board_pearl': 'Multiple small enhancing nodules in a prior parathyroid bed after '
                                        'capsular rupture suggest parathyromatosis.',
                         'curveball': 'How would recurrent laryngeal nerve function and the distribution of '
                                      'implants affect the threshold for another operation?',
                         'curveball_answer': 'Preoperative laryngoscopy is mandatory. If one nerve is '
                                             'already paralyzed, operating near the other risks bilateral '
                                             'paralysis, so surgery is limited or avoided in favor of '
                                             'cinacalcet. Implants confined to one accessible region favor '
                                             'resection, while widespread implants on both sides or in the '
                                             'mediastinum make cure unlikely and favor medical control.'},
 'v134_tps_07': {'stem': 'A 57-year-old woman has a 2.5-cm submucosal mass of the right hard palate, and '
                         'biopsy shows adenoid cystic carcinoma. She reports 4 months of progressive '
                         'numbness of the right upper lip and cheek. MRI shows thickening and enhancement of '
                         'the right maxillary nerve through the pterygopalatine fossa to an enlarged foramen '
                         'rotundum, with no cavernous sinus involvement. What is the key implication for '
                         'treatment?',
                 'choices': ['Only the palatal primary needs resection, with a 1-cm mucosal margin',
                             'Elective bilateral neck dissection is the priority for regional control',
                             'Treatment must cover the involved maxillary nerve to the skull base',
                             'The disease is incurable, and palliative chemotherapy should be offered'],
                 'answer': 2,
                 'explanation': 'Adenoid cystic carcinoma is strongly neurotropic. Numbness in the maxillary '
                                'distribution plus MRI enhancement and foraminal enlargement indicate gross, '
                                'named-nerve perineural spread. The true tumor extent therefore runs from '
                                'the palate through the greater palatine canal and pterygopalatine fossa to '
                                'foramen rotundum. Curative treatment requires resection that follows the '
                                'nerve, often with an infratemporal or skull-base approach, and '
                                'postoperative radiation that covers the entire nerve pathway to its '
                                'intracranial entry.',
                 'why_wrong': ['Gross perineural spread extends far beyond the visible primary, and treating '
                               'only the palate leaves disease along the nerve.',
                               'Adenoid cystic carcinoma spreads primarily along nerves rather than to '
                               'nodes, so neck dissection does not address the main route.',
                               'Correct.',
                               'Spread to foramen rotundum without cavernous sinus involvement may still be '
                               'treated with curative intent.'],
                 'board_pearl': 'Named-nerve perineural spread defines the true extent of adenoid cystic '
                                'carcinoma; treat the whole nerve pathway.',
                 'curveball': 'Had she no numbness but pathology showed microscopic PNI, how would that '
                              'differ from gross radiographic spread in planning?',
                 'curveball_answer': 'Microscopic PNI involves small unnamed nerves near the tumor and is '
                                     'managed with adjuvant radiation to the primary bed. Gross perineural '
                                     'spread involves a named nerve on imaging or clinically and requires '
                                     'the surgical and radiation fields to follow that nerve to the skull '
                                     'base. Gross spread is also associated with higher T category and worse '
                                     'prognosis.'},
 'v146_tps_10': {'stem': 'A 52-year-old man has biopsy-proven adenoid cystic carcinoma of a 2-cm left '
                         'palatal mass and reports new numbness over the left cheek and upper teeth. CT of '
                         'the neck with contrast was done at an outside hospital and showed only the palatal '
                         'mass. He has no cervical adenopathy. The tumor board is planning treatment. Which '
                         'imaging study is most important next?',
                 'choices': ['PET-CT to screen for nodal and distant metastatic disease',
                             'Repeat contrast CT of the neck with thinner axial sections',
                             'Gadolinium MRI with fat suppression along the maxillary nerve',
                             'Bone scintigraphy to evaluate the maxilla and skull base'],
                 'answer': 2,
                 'explanation': 'New numbness in the maxillary distribution in a patient with adenoid cystic '
                                'carcinoma signals perineural spread along V2. Contrast MRI with fat '
                                'suppression and thin sections is the most sensitive study: it shows nerve '
                                'thickening and enhancement, obliteration of fat in the pterygopalatine '
                                'fossa, foraminal enlargement, and denervation changes. Imaging must follow '
                                'the nerve from the palate through the greater palatine canal and '
                                'pterygopalatine fossa to foramen rotundum and the cavernous sinus.',
                 'why_wrong': ['PET-CT is relatively insensitive for perineural spread and for indolent '
                               'adenoid cystic carcinoma, so it cannot map nerve involvement.',
                               'CT shows foraminal widening but is less sensitive than MRI for early '
                               'perineural enhancement and nerve thickening.',
                               'Correct.',
                               'Bone scintigraphy is nonspecific and does not show the nerve pathway or soft '
                               'tissue extent.'],
                 'board_pearl': 'Cranial neuropathy with adenoid cystic carcinoma: contrast MRI following '
                                'the nerve from primary to skull base.',
                 'curveball': 'The MRI shows enhancement reaching foramen rotundum. What does that extension '
                              'do to surgical planning?',
                 'curveball_answer': 'Extension to foramen rotundum means the resection must reach the skull '
                                     'base. That typically requires an infratemporal fossa or endoscopic '
                                     'transpterygoid approach to follow V2 until frozen sections are '
                                     'negative, and radiation fields must cover the nerve to the cavernous '
                                     'sinus. Cavernous sinus or Meckel cave involvement often shifts '
                                     'treatment toward definitive radiation.'},
 'v239_tps_acc_fnd': {'stem': 'A 48-year-old woman had a submandibular gland excision for a painful mass, '
                              'and pathology shows adenoid cystic carcinoma with cribriform pattern and '
                              'perineural invasion. Her neck nodes are negative on imaging. She asks how '
                              'this cancer typically behaves and what she should expect in follow-up. Which '
                              'biologic feature is most characteristic of this tumor?',
                      'choices': ['Perineural spread with late distant metastases, often to lung',
                                  'Early regional nodal spread and rapid local recurrence',
                                  'Rapid early growth with frequent transformation to lymphoma',
                                  'Hormone-dependent growth driven by androgen receptor signaling'],
                      'answer': 0,
                      'explanation': 'Adenoid cystic carcinoma typically grows slowly but relentlessly. It '
                                     'invades nerves, causing pain and numbness, and recurs locally along '
                                     'neural pathways. Hematogenous metastases, most often to the lungs, may '
                                     'appear many years after treatment, even when the primary site is '
                                     'controlled. Regional nodal spread is less common than in many other '
                                     'head and neck cancers, though solid-pattern tumors spread more '
                                     'readily. Long-term follow-up with chest imaging is needed because '
                                     'recurrences may appear after 10 years.',
                      'why_wrong': ['Correct.',
                                    'Nodal metastasis is relatively uncommon in adenoid cystic carcinoma '
                                    'compared with squamous or salivary duct carcinoma.',
                                    'Adenoid cystic carcinoma usually grows slowly and does not transform '
                                    'into lymphoma.',
                                    'Androgen receptor signaling is characteristic of salivary duct '
                                    'carcinoma, not adenoid cystic carcinoma.'],
                      'board_pearl': 'Adenoid cystic carcinoma: neurotropic, slow but relentless, with late '
                                     'lung metastases; follow patients for many years.',
                      'curveball': 'Which cranial neuropathies can reveal occult proximal perineural spread '
                                   'from minor salivary primaries?',
                      'curveball_answer': 'Palatal and sinonasal tumors spread along V2, causing cheek and '
                                          'upper lip numbness. Tumors near the mandible or masticator space '
                                          'spread along V3, causing chin and lip numbness and masticator '
                                          'weakness. Facial weakness signals spread along the facial nerve, '
                                          'and tongue tumors can spread along the hypoglossal or lingual '
                                          'nerves. Any new neuropathy needs MRI.'},
 'v239_tps_acc_app': {'stem': 'A 49-year-old man has adenoid cystic carcinoma of the left submandibular '
                              'gland. He reports numbness and tingling of the left side of his tongue for 3 '
                              'months. Contrast MRI shows thickening and enhancement of the lingual nerve '
                              'extending superiorly through the masticator space toward an enlarged foramen '
                              'ovale, with no intracranial extension. What is the best management principle?',
                      'choices': ['Submandibular gland excision alone with negative soft tissue margins',
                                  'Submandibular excision with bilateral modified radical neck dissection',
                                  'Plan resection and radiation along the lingual nerve to foramen ovale',
                                  'Radiation limited to the submandibular bed and the level I nodes'],
                      'answer': 2,
                      'explanation': 'The lingual nerve runs directly above the submandibular gland and '
                                     'joins the mandibular division, providing a route from the gland to '
                                     'foramen ovale. Symptoms and MRI findings indicate gross perineural '
                                     'spread, so the true tumor extent follows the nerve. Curative treatment '
                                     'requires resection that traces the lingual nerve and V3 proximally, '
                                     'often through an infratemporal approach with frozen sections, and '
                                     'postoperative radiation covering the full pathway to the skull base.',
                      'why_wrong': ['Gland excision alone ignores gross spread along the lingual nerve, '
                                    'which is a common cause of recurrence at the skull base.',
                                    'Nodal spread is not the main route for adenoid cystic carcinoma, and '
                                    'bilateral neck dissection does not address the nerve.',
                                    'Correct.',
                                    'Radiating only the gland bed leaves the involved nerve pathway to '
                                    'foramen ovale outside the treatment field.'],
                      'board_pearl': 'Adenoid cystic carcinoma of the submandibular gland can spread along '
                                     'the lingual nerve to V3 and foramen ovale.',
                      'curveball': 'How does skull-base extension affect surgical margins and adjuvant '
                                   'radiation design?',
                      'curveball_answer': 'Once spread reaches the skull base, clear surgical margins become '
                                          'difficult because the nerve enters the cranial cavity. Surgery '
                                          'aims for frozen-section-negative proximal margins where feasible, '
                                          'and radiation fields extend to the Gasserian ganglion and '
                                          'cavernous sinus. Particle therapy can improve dose coverage near '
                                          'critical structures.'},
 'v239_tps_acc_snr': {'stem': 'A 59-year-old woman underwent superficial parotidectomy with facial nerve '
                              'preservation for a 3.5-cm adenoid cystic carcinoma. Pathology shows a close '
                              'deep margin of 1 mm along the facial nerve, extensive perineural invasion '
                              'including a named branch, and a predominantly cribriform pattern. A selective '
                              'neck dissection showed no nodal metastases. Facial function is normal. What '
                              'is the most appropriate next step?',
                      'choices': ['Observation with serial MRI, because the neck dissection was negative',
                                  'Adjuvant cisplatin-based chemotherapy without any radiation',
                                  'Completion facial nerve sacrifice to obtain a wider margin',
                                  'Postoperative radiation to the bed and the facial nerve pathway'],
                      'answer': 3,
                      'explanation': 'Local and perineural recurrence drives outcomes in adenoid cystic '
                                     'carcinoma, and nodal status does not capture that risk. Close margins, '
                                     'T3 size, and named-nerve perineural invasion are strong indications '
                                     'for postoperative radiation. The field covers the operative bed and '
                                     'the facial nerve pathway through the stylomastoid foramen toward the '
                                     'skull base. Long-term surveillance with MRI and chest imaging is '
                                     'needed because local and distant recurrences can appear 10 years or '
                                     'more later.',
                      'why_wrong': ['Negative nodes do not offset the high local and perineural recurrence '
                                    'risk from close margins and named-nerve invasion.',
                                    'Chemotherapy has no established adjuvant role in adenoid cystic '
                                    'carcinoma, and it does not replace radiation.',
                                    'Sacrificing a functioning nerve for a close margin causes permanent '
                                    'paralysis when radiation can control microscopic disease.',
                                    'Correct.'],
                      'board_pearl': 'Adenoid cystic carcinoma with close margins or named-nerve PNI: '
                                     'adjuvant radiation along the nerve pathway, then prolonged '
                                     'surveillance.',
                      'curveball': 'How would unresectable skull-base perineural extension change the '
                                   'balance among radiation, systemic therapy, and symptom-directed care?',
                      'curveball_answer': 'Unresectable skull-base disease shifts treatment to definitive '
                                          'radiation, often with particle therapy, aiming for local control '
                                          'while preserving function. Systemic therapy has limited response '
                                          'rates and is reserved for clinical trials or symptomatic '
                                          'progression. Symptom-directed care, including pain control for '
                                          'neuropathic pain, becomes central as disease progresses.'}}
