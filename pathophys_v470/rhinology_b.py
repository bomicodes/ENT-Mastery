"""Rhinology / Allergy / Skull Base (part B): mechanism-level teaching content."""

CONTENT = {
"Olfactory Dysfunction": dict(
overview=(
"Olfactory dysfunction ranges from reduced smell (hyposmia) to total loss (anosmia) and distorted smell (parosmia). "
"It is common after viral infection, with CRS, after head trauma, and in neurodegenerative disease, and it affects safety, nutrition, and quality of life."),
physiology=(
"**Olfactory epithelium**: high in the nasal vault (olfactory cleft) along the cribriform plate, superior septum, and superior turbinate. "
"**Receptor neurons**: bipolar neurons with cilia carrying odorant receptors (about 400 functional types); each neuron expresses one receptor type. "
"**Regeneration**: olfactory neurons are replaced from basal stem cells throughout life, which is unusual for neurons. "
"**Pathway**: axons pass through the cribriform plate to glomeruli in the olfactory bulb, then to piriform cortex, amygdala, and entorhinal cortex without a thalamic relay. "
"**Retronasal smell**: odors from the mouth reach the epithelium through the nasopharynx and create most of what we call flavor."),
pathophysiology=(
"**Conductive loss**: polyps, edema, or obstruction prevent odorants from reaching the olfactory cleft; this is often reversible with steroids or surgery. "
"**Post-viral loss**: viruses damage supporting (sustentacular) cells and receptor neurons; SARS-CoV-2 targets sustentacular cells, and recovery depends on regeneration. "
"**Parosmia**: miswired regenerating neurons produce distorted, often unpleasant perceptions during recovery. "
"**Post-traumatic loss**: shearing of olfactory axons at the cribriform plate or contusion of the bulbs and frontal lobes; recovery is less likely. "
"**Neurodegenerative link**: early smell loss precedes Parkinson and Alzheimer disease because pathology involves olfactory structures early. "
"**Olfactory training**: repeated structured exposure to odors may promote neural regeneration and plasticity."),
),

"Nonallergic Rhinitis / Rhinitis Medicamentosa": dict(
overview=(
"Nonallergic rhinitis is chronic nasal symptoms without allergic sensitization: vasomotor, gustatory, drug-induced, hormonal, and atrophic types. "
"Rhinitis medicamentosa is rebound congestion from overuse of topical decongestants."),
physiology=(
"**Autonomic balance**: sympathetic tone keeps venous sinusoids constricted; parasympathetic tone drives secretion and congestion. "
"**Sensory nerves**: trigeminal C fibers with TRPV1 receptors respond to irritants, temperature, and chemicals. "
"**Adrenergic receptors**: alpha receptors on vessels mediate decongestion."),
pathophysiology=(
"**Vasomotor rhinitis**: neural hyperreactivity to irritants, temperature, and odors through TRPV1 and parasympathetic reflexes. "
"**Gustatory rhinitis**: eating triggers vagal cholinergic reflexes, producing watery rhinorrhea (responsive to ipratropium). "
"**Rhinitis medicamentosa**: repeated alpha-agonist use downregulates receptors and causes rebound vasodilation and tolerance, creating a cycle of escalating use. "
"**Drug-induced rhinitis**: antihypertensives, PDE5 inhibitors, and hormones alter vascular tone. "
"**Hormonal rhinitis**: estrogen increases vascular congestion in pregnancy. "
"**Atrophic rhinitis**: loss of mucosa and glands after aggressive surgery or radiation causes crusting and paradoxical obstruction."),
),

"Unilateral Sinonasal Disease": dict(
overview=(
"Unilateral sinonasal disease (one-sided obstruction, epistaxis, discharge, or opacification) must be considered neoplastic until proven otherwise. "
"The differential includes inverted papilloma, malignancy, fungal ball, odontogenic sinusitis, AFRS, mucocele, CSF leak, and foreign body."),
physiology=(
"**Symmetric inflammation**: inflammatory CRS is usually bilateral because the drivers (immune dysregulation, environment) affect both sides. "
"**Localized causes**: unilateral findings imply a local process."),
pathophysiology=(
"**Neoplasms**: tumors grow from one site, causing progressive one-sided obstruction, bleeding, and later neuro-ophthalmic findings. "
"**Local infection**: dental sources and fungal balls are unilateral. "
"**Imaging clues**: bone erosion suggests malignancy; focal hyperostosis suggests inverted papilloma attachment; central calcifications suggest fungal ball; expansion suggests mucocele or AFRS. "
"**Why MRI is added**: it distinguishes tumor from retained secretions and shows orbital, dural, and perineural involvement."),
),

"Pediatric Chronic Rhinosinusitis": dict(
overview=(
"Pediatric CRS is chronic sinonasal inflammation in children, where adenoids play a central role and immune, ciliary, and genetic disorders must be considered. "
"Treatment escalates from medical therapy to adenoidectomy, then sinus surgery."),
physiology=(
"**Sinus development**: maxillary and ethmoid sinuses are present at birth, the sphenoid pneumatizes in early childhood, and the frontal sinus in later childhood and adolescence. "
"**Adenoids**: nasopharyngeal lymphoid tissue that peaks in size at about 4-7 years."),
pathophysiology=(
"**Adenoid reservoir**: adenoids harbor bacterial biofilms that seed the sinuses and obstruct the posterior nasal airway. "
"**Why adenoidectomy first**: removing the reservoir resolves many cases, especially in younger children. "
"**Underlying conditions**: allergy, immunodeficiency, cystic fibrosis, and primary ciliary dyskinesia are more likely in children with severe or refractory disease. "
"**Polyps in children**: suggest cystic fibrosis until proven otherwise. "
"**Facial growth concerns**: early concerns that sinus surgery impairs facial growth have not been strongly confirmed, but surgery remains limited."),
),

"CF / Primary Ciliary Dyskinesia Sinonasal Disease": dict(
overview=(
"Cystic fibrosis and primary ciliary dyskinesia cause universal, lifelong CRS from failed mucociliary clearance. "
"Sinus disease reseeds the lungs, so sinus care is part of lung care, and CFTR modulators have changed the disease course."),
physiology=(
"**CFTR channel**: chloride and bicarbonate channel that hydrates airway surface liquid. "
"**Mucociliary escalator**: needs normal cilia beating in a properly hydrated periciliary layer. "
"**Ciliary structure**: 9+2 microtubules with dynein arms that power beating."),
pathophysiology=(
"**CF mechanism**: defective CFTR dehydrates airway surface liquid, producing thick mucus that cilia cannot clear, leading to obstruction, chronic infection (Pseudomonas), and polyps. "
"**PCD mechanism**: structural defects in cilia (often dynein arm mutations) impair beating despite normal mucus, causing neonatal respiratory distress, chronic wet cough, otitis, and situs inversus in about half (Kartagener). "
"**Lung reservoir**: the sinuses act as a reservoir for Pseudomonas, which seeds the lungs after transplant. "
"**CFTR modulators**: elexacaftor-tezacaftor-ivacaftor improves channel function, reducing sinus disease severity. "
"**Diagnostics**: sweat chloride and genetics for CF; nasal nitric oxide (low in PCD), ciliary electron microscopy, and genetics for PCD."),
),

"Immunodeficiency-Associated Chronic Rhinosinusitis": dict(
overview=(
"Immunodeficiency underlies a meaningful share of refractory or recurrent rhinosinusitis, especially antibody deficiencies. "
"Recognizing it changes treatment (immunoglobulin replacement, vaccines, prophylaxis)."),
physiology=(
"**Antibody defense**: IgA protects mucosal surfaces; IgG opsonizes encapsulated bacteria. "
"**Specific antibody response**: vaccine responses to polysaccharide antigens test functional antibody production."),
pathophysiology=(
"**Common variable immunodeficiency**: low IgG, IgA, and often IgM with poor vaccine responses, causing recurrent sinopulmonary infections. "
"**Specific antibody deficiency**: normal immunoglobulin levels but poor responses to pneumococcal polysaccharides. "
"**Selective IgA deficiency**: common, often mild, but can raise sinopulmonary infection risk. "
"**Encapsulated organisms**: S. pneumoniae and H. influenzae require antibody opsonization, explaining recurrent infections. "
"**HIV and iatrogenic immunosuppression**: increase both bacterial and fungal sinusitis risk."),
),

"Objective Assessment of Nasal Function": dict(
overview=(
"Objective tests (acoustic rhinometry, rhinomanometry, peak nasal inspiratory flow, and smell testing) supplement symptoms and exam in nasal obstruction and olfactory loss. "
"They help explain discordance between what patients feel and what clinicians see."),
physiology=(
"**Airflow and resistance**: the nose contributes about two-thirds of total airway resistance (Cummings), and the internal valve accounts for about half of nasal resistance (Pasha). "
"**Cross-sectional area**: acoustic rhinometry uses reflected sound to map area along the nasal cavity. "
"**Pressure-flow relationship**: rhinomanometry measures transnasal pressure and flow to calculate resistance."),
pathophysiology=(
"**Mismatch of perception and measurement**: patency sensation depends on mucosal cooling (TRPM8 receptors) as much as on actual resistance, so measurements and symptoms often correlate poorly. "
"**Decongestion testing**: comparing before and after decongestant distinguishes mucosal (reversible) from structural (fixed) obstruction. "
"**Smell testing**: validated scratch-and-sniff tests (UPSIT) and threshold-discrimination-identification tests quantify loss and detect malingering. "
"**Empty nose context**: patients with large airways may still report obstruction because of lost sensation."),
),

"Facial Pain / Headache vs Rhinogenic Disease": dict(
overview=(
"Many patients with \"sinus headache\" have migraine or tension-type headache rather than sinus disease. "
"Distinguishing them prevents unnecessary antibiotics and surgery."),
physiology=(
"**Trigeminal convergence**: sinus, dural, and facial pain all converge on the trigeminal nucleus caudalis. "
"**Autonomic symptoms**: migraine activates trigeminal-autonomic reflexes, causing nasal congestion and rhinorrhea."),
pathophysiology=(
"**Misattribution**: migraine-related facial pain, congestion, and weather triggers mimic sinus disease. "
"**Rhinogenic pain**: true sinus pain usually accompanies purulence, obstruction, smell loss, and objective findings on endoscopy or CT. "
"**Contact point headache**: controversial; mucosal contact points are common in asymptomatic people. "
"**Diagnostic logic**: facial pain without endoscopic or CT evidence of inflammation should prompt headache evaluation and treatment."),
),

"Benign Sinonasal Tumor Framework": dict(
overview=(
"Benign sinonasal tumors (inverted papilloma, osteoma, fibrous dysplasia, ossifying fibroma, hemangioma, schwannoma, JNA) are classified by tissue of origin and treated by complete resection when symptomatic or growing. "
"Imaging helps predict histology before surgery."),
physiology=(
"**Tissue types**: the sinonasal tract contains respiratory epithelium, bone, fibro-osseous tissue, vessels, nerves, and minor salivary glands, each of which can give rise to benign tumors. "
"**Craniofacial bone growth**: facial bones grow through childhood and adolescence, influencing fibro-osseous lesion behavior. "
"**Confined spaces**: sinuses are bony boxes, so slow growth causes obstruction and remodeling before symptoms. "
"**Imaging signatures**: CT shows bone characteristics, while MRI separates tumor from retained secretions."),
pathophysiology=(
"**Osteoma**: slow-growing dense bone, most often frontal or ethmoid; obstruction or growth toward the orbit or skull base indicates removal. "
"**Fibrous dysplasia**: GNAS mutation replaces bone with fibro-osseous tissue (ground-glass on CT); usually stabilizes after puberty. "
"**Ossifying fibroma**: well-circumscribed, more aggressive fibro-osseous neoplasm requiring complete removal. "
"**Lobular capillary hemangioma**: friable bleeding septal lesion, often in pregnancy. "
"**Treatment logic**: endoscopic resection is guided by attachment site and extent; observation suits asymptomatic stable lesions."),
),

"Systemic Disease of the Nose / Sinuses": dict(
overview=(
"Systemic diseases (granulomatosis with polyangiitis, sarcoidosis, EGPA, lymphoma, and infections) can present with sinonasal symptoms, crusting, septal perforation, or saddle nose. "
"They require biopsy, labs, and systemic therapy rather than routine sinus surgery."),
physiology=(
"**Septal cartilage nutrition**: septal cartilage is avascular and depends on diffusion from the overlying mucoperichondrium, so anything that damages that blood supply destroys cartilage. "
"**Small-vessel richness**: the nasal mucosa has a dense submucosal microvasculature, a natural target for small-vessel vasculitis. "
"**Shared airway mucosa**: the same respiratory epithelium lines the nose, sinuses, middle ear, larynx, and bronchi, which is why systemic airway diseases appear in several sites at once. "
"**Mucosal healing**: crusting and bleeding reflect epithelium that cannot regenerate over inflamed or ischemic tissue."),
pathophysiology=(
"**GPA**: ANCA-associated necrotizing granulomatous vasculitis causes crusting, bleeding, septal perforation, and saddle nose from cartilage ischemia. "
"**EGPA**: eosinophilic vasculitis with asthma and polyps. "
"**Sarcoidosis**: noncaseating granulomas produce crusting and nodularity. "
"**NK/T-cell lymphoma**: angiocentric destructive lesions of the midline face that mimic GPA; biopsy must be deep and repeated if needed. "
"**Cocaine**: vasoconstriction and cutting agents (levamisole) cause midline destruction and false-positive ANCA."),
),

"Allergy Testing & Interpretation": dict(
overview=(
"Allergy testing (skin prick, intradermal, and serum specific IgE) identifies sensitization, which becomes clinical allergy only when it matches symptoms and exposure. "
"Correct interpretation drives avoidance and immunotherapy decisions."),
physiology=(
"**IgE arming**: allergen-specific IgE binds high-affinity Fc\u03b5RI receptors on mast cells and basophils. "
"**Skin mast cells**: introducing allergen into the epidermis cross-links IgE, releasing histamine within minutes. "
"**Wheal and flare**: histamine causes local edema (wheal) and an axon-reflex vasodilation (flare). "
"**Serum specific IgE**: measures circulating IgE independent of mast-cell function or antihistamines. "
"**Controls**: histamine (positive) and saline (negative) confirm skin reactivity."),
pathophysiology=(
"**Sensitization vs allergy**: a positive test without matching symptoms is sensitization only. "
"**Skin testing interference**: antihistamines suppress the histamine-mediated wheal, so they are held before testing; positive (histamine) and negative (saline) controls validate the test. "
"**Serum testing role**: useful with dermatographism, extensive skin disease, inability to stop antihistamines, or anaphylaxis risk. "
"**Intradermal testing**: more sensitive but less specific, with more false positives. "
"**Component testing**: distinguishes cross-reactive proteins (e.g., pollen-food) from primary sensitization."),
),

"Allergen Immunotherapy — SCIT / SLIT": dict(
overview=(
"Allergen immunotherapy (subcutaneous or sublingual) is the only disease-modifying treatment for allergic rhinitis, reducing symptoms and medication needs and sustaining benefit after stopping. "
"It requires correct allergen selection and monitoring for systemic reactions."),
physiology=(
"**Tolerance is the default**: most people inhale pollen without reacting because regulatory T cells (Tregs) and IL-10 and TGF-beta actively suppress responses to harmless antigens. "
"**Antigen-presenting route**: subcutaneous dosing presents allergen through skin dendritic cells, whereas sublingual dosing uses oral mucosal dendritic cells, which are naturally tolerogenic. "
"**Antibody classes**: IgE arms mast cells, whereas IgG4 is a non-inflammatory antibody that binds antigen without triggering mast cells or complement. "
"**Dose dependence**: tolerance requires reaching and sustaining an adequate maintenance dose over years."),
pathophysiology=(
"**Immune deviation**: repeated controlled exposure shifts the response from Th2 toward regulatory and Th1 responses. "
"**Blocking IgG4**: binds allergen before it reaches mast-cell IgE. "
"**Reduced mast-cell and eosinophil recruitment**: lowers both early and late phase reactions. "
"**Duration**: 3-5 years of therapy produces benefit lasting years after stopping. "
"**Safety**: SCIT carries risk of systemic reactions and anaphylaxis, requiring observation and epinephrine availability; SLIT has mainly local oral side effects. "
"**Uncontrolled asthma**: increases risk of severe reactions."),
),

"Local Allergic Rhinitis": dict(
overview=(
"Local allergic rhinitis is allergic-type rhinitis with negative skin and serum testing but local nasal IgE production and a positive nasal allergen challenge. "
"It explains some patients labeled nonallergic who respond to allergy treatments."),
physiology=(
"**Mucosal immune tissue**: the nasal mucosa contains dendritic cells, T cells, B cells, and mast cells that sample inhaled allergens directly. "
"**Local class switching**: B cells in the nasal mucosa can switch to IgE production in place, without that IgE reaching the bloodstream in measurable amounts. "
"**Mast-cell arming**: locally produced IgE binds Fc\u03b5RI receptors on nasal mast cells, which is all that is needed for an allergic response at that site. "
"**Systemic tests sample elsewhere**: skin prick tests sample skin mast cells and serum tests sample circulating IgE, so a purely mucosal process can be missed."),
pathophysiology=(
"**Local sensitization**: specific IgE is produced in the nasal mucosa without systemic sensitization. "
"**Same effector pathway**: mast-cell activation produces typical allergic symptoms on exposure. "
"**Diagnosis**: nasal allergen provocation testing, as systemic tests are negative. "
"**Treatment**: responds to standard allergic rhinitis medications and possibly immunotherapy."),
),

"Empty Nose Syndrome": dict(
overview=(
"Empty nose syndrome is paradoxical nasal obstruction and suffocation sensation after turbinate reduction, despite a widely patent airway. "
"It reflects lost airflow sensation and conditioning rather than physical blockage."),
physiology=(
"**Airflow sensation**: TRPM8 cold receptors in turbinate mucosa sense cooling from airflow, which the brain interprets as breathing freely. "
"**Air conditioning**: turbinates warm and humidify air and direct flow."),
pathophysiology=(
"**Loss of sensory surface**: aggressive turbinate resection removes cold receptors, so airflow is not perceived despite low resistance. "
"**Abnormal airflow**: altered flow patterns and dryness cause crusting and discomfort. "
"**Psychological overlay**: anxiety, depression, and sleep disturbance are common and amplify symptoms. "
"**Diagnosis**: clinical, supported by the ENS6Q questionnaire and a cotton test (cotton placed in the inferior meatus temporarily relieves symptoms; Pasha describes the same test for atrophic rhinitis). "
"**Treatment logic**: humidification, and implants to restore airway volume and redirect flow toward mucosa."),
),

"Silent Sinus Syndrome": dict(
overview=(
"Silent sinus syndrome is painless, progressive enophthalmos and hypoglobus from collapse of the maxillary sinus after chronic ostial obstruction. "
"It is treated by maxillary antrostomy, with orbital floor repair if needed."),
physiology=(
"**Orbital floor = sinus roof**: the maxillary sinus roof is a thin plate that forms the orbital floor and carries the infraorbital nerve. "
"**Gas exchange**: sinus mucosa continuously absorbs oxygen and nitrogen into the bloodstream, just as middle-ear mucosa does. "
"**Ostial ventilation**: an open natural ostium lets nasal air replace absorbed gas, holding the sinus near atmospheric pressure. "
"**Wall compliance**: the sinus walls are thin bone that can remodel under sustained pressure differences, in either direction."),
pathophysiology=(
"**Ostial occlusion**: closure traps the sinus. "
"**Negative pressure**: gas absorption creates sustained negative pressure, pulling the sinus walls inward. "
"**Atelectasis**: the walls thin and retract, and the orbital floor sags into the sinus. "
"**Eye findings**: enophthalmos and hypoglobus develop without pain or diplopia early. "
"**Treatment logic**: restoring ventilation stops progression; floor reconstruction corrects persistent globe malposition."),
),

"Endoscopic Pituitary / Anterior Skull Base Approach": dict(
overview=(
"The endoscopic endonasal approach reaches the sella and anterior skull base through the nose and sphenoid. "
"It requires precise sphenoid anatomy, vascularized reconstruction, and care of the carotids and optic nerves."),
physiology=(
"**Sella**: sits in the sphenoid roof, bordered by the cavernous sinuses and carotids laterally and the optic chiasm superiorly. "
"**Pituitary function**: the anterior pituitary secretes ACTH, TSH, GH, prolactin, LH, and FSH; the posterior releases ADH and oxytocin. "
"**Sphenoid landmarks**: sellar floor, carotid prominences, optic protuberances, opticocarotid recesses, and clival recess."),
pathophysiology=(
"**Tumor effects**: macroadenomas compress the chiasm (bitemporal hemianopia) and cause hypopituitarism; functional adenomas cause hormonal syndromes. "
"**Carotid injury**: catastrophic hemorrhage from lateral dissection, especially with dehiscent carotid canals. "
"**Diabetes insipidus**: posterior pituitary or stalk manipulation reduces ADH. "
"**SIADH**: can occur later, causing hyponatremia. "
"**CSF leak**: from opening the arachnoid; reconstruction with a nasoseptal flap reduces leak rates."),
),

"Orbital Apex Syndrome": dict(
overview=(
"Orbital apex syndrome is dysfunction of the optic nerve plus cranial nerves III, IV, V1, and VI from a lesion at the orbital apex. "
"Causes include invasive fungal sinusitis, inflammation, tumor, and trauma."),
physiology=(
"**Superior orbital fissure**: transmits CN III, IV, V1 branches, VI, and the superior ophthalmic vein. "
"**Optic canal**: transmits the optic nerve and ophthalmic artery. "
"**Proximity**: both lie at the posterior orbit adjacent to the sphenoid and posterior ethmoid sinuses."),
pathophysiology=(
"**Combined deficits**: vision loss, ophthalmoplegia, ptosis, and V1 numbness. "
"**Superior orbital fissure syndrome**: the same deficits without vision loss (some older texts use orbital apex syndrome as a synonym). "
"**Cavernous sinus extension**: adds V2 and sympathetic involvement. "
"**Causes**: invasive fungal sinusitis (especially in diabetes and immunosuppression), bacterial infection, IgG4-related or idiopathic inflammation, malignancy, and fractures. "
"**Urgency**: optic nerve compression causes irreversible vision loss, so rapid diagnosis is needed."),
),

"Anaphylaxis": dict(
overview=(
"Anaphylaxis is a severe, rapid systemic hypersensitivity reaction causing airway, breathing, circulatory, and skin involvement. "
"Intramuscular epinephrine is the first and most important treatment, relevant to allergy testing, immunotherapy, and perioperative care."),
physiology=(
"**Mast cells and basophils**: store histamine and tryptase and synthesize leukotrienes and prostaglandins on activation. "
"**Epinephrine receptors**: alpha-1 (vasoconstriction), beta-1 (cardiac output), and beta-2 (bronchodilation, mast-cell stabilization)."),
pathophysiology=(
"**Trigger**: IgE-mediated (foods, venom, drugs, immunotherapy) or non-IgE (contrast, opioids) mast-cell activation. "
"**Mediator release**: histamine and leukotrienes cause vasodilation, capillary leak, bronchospasm, and edema. "
"**Shock**: distributive vasodilation plus fluid shift reduce preload, causing hypotension. "
"**Airway compromise**: laryngeal and tongue edema obstruct the upper airway. "
"**Biphasic reactions**: symptoms recur after resolution in about 1-20 percent, up to 72 hours later; severe initial reactions, needing more than one epinephrine dose, and delayed epinephrine raise the risk, so observation is extended for these patients. "
"**Why epinephrine first**: it reverses vasodilation and bronchospasm and stabilizes mast cells; antihistamines and steroids are adjuncts only and do not prevent biphasic reactions. Intramuscular thigh dosing (0.01 mg/kg up to 0.5 mg) remains standard, and an epinephrine nasal spray (FDA-approved 2024) is an alternative for community use. "
"**Beta-blockers**: blunt epinephrine response, sometimes requiring glucagon."),
),

"Oral Allergy Syndrome (Pollen-Food Syndrome)": dict(
overview=(
"Oral allergy syndrome is itching and swelling of the mouth and throat after eating raw fruits or vegetables in pollen-allergic patients. "
"It results from cross-reactivity between pollen and heat-labile food proteins."),
physiology=(
"**Pan-allergens**: plants share conserved defense proteins (PR-10 proteins such as Bet v 1, profilins, lipid transfer proteins) with similar three-dimensional shapes. "
"**Conformational epitopes**: IgE recognizes the folded shape of a protein, so a related protein from a different plant can bind the same IgE. "
"**Heat and digestion**: PR-10 proteins and profilins unfold with cooking and are degraded quickly by saliva and gastric acid, while lipid transfer and storage proteins are stable. "
"**Oral mast cells**: the oropharyngeal mucosa contains mast cells that react on first contact with food protein."),
pathophysiology=(
"**Cross-reactivity**: birch pollen (Bet v 1) antibodies cross-react with apple, cherry, carrot, and others; ragweed with melon and banana. "
"**Heat-labile proteins**: cooking denatures these proteins, so cooked foods are tolerated. "
"**Localized reaction**: proteins are digested quickly, limiting symptoms mainly to the mouth. "
"**Risk of systemic reactions**: stable proteins (lipid transfer proteins, storage proteins) can cause systemic reactions, which component testing identifies."),
),
}
