"""Rhinology / Allergy / Skull Base (part A): mechanism-level teaching content."""

CONTENT = {
"Allergic Rhinitis": dict(
overview=(
"Allergic rhinitis is IgE-mediated inflammation of the nasal mucosa after allergen exposure, causing sneezing, itching, rhinorrhea, and congestion. "
"It affects up to a third of adults, worsens asthma and sinus disease, and is managed by avoidance, intranasal steroids, antihistamines, and immunotherapy."),
physiology=(
"**Nasal functions**: the nose warms, humidifies, and filters about 10,000 liters of air daily. "
"**Mucosa**: pseudostratified ciliated columnar epithelium with goblet cells and seromucous glands, over a rich venous erectile system in the turbinates. "
"**Nasal cycle**: alternating sympathetic tone causes cyclical congestion and decongestion between sides every few hours. "
"**Autonomic control**: sympathetic tone constricts venous sinusoids (decongestion); parasympathetic (vidian nerve) input drives glandular secretion. "
"**Immune surveillance**: dendritic cells sample inhaled antigens and present them to T cells in regional lymphoid tissue."),
pathophysiology=(
"**Sensitization**: in atopic individuals, dendritic cells present allergen to naive T cells that differentiate into Th2 cells; IL-4 and IL-13 drive B cells to make allergen-specific IgE that binds mast cells and basophils. "
"**Early phase (minutes)**: re-exposure cross-links IgE on mast cells, releasing histamine, tryptase, leukotrienes, and prostaglandins; histamine stimulates sensory nerves (itch, sneeze), glands (rhinorrhea), and vessels (congestion). "
"**Late phase (about 4-10 hours, peak near 6)**: cytokines (IL-4, IL-5, IL-13) recruit eosinophils, basophils, and Th2 cells, producing sustained congestion. "
"**Priming**: repeated exposure lowers the threshold for later reactions, so symptoms build across a pollen season. "
"**Unified airway**: the same Th2 inflammation affects the lower airway, so uncontrolled rhinitis worsens asthma. "
"**Drug logic**: antihistamines block early-phase itch and sneeze but help congestion less; intranasal steroids suppress both phases and are the most effective single therapy; immunotherapy shifts the response toward tolerance (regulatory T cells, IgG4)."),
),

"CRS Phenotyping": dict(
overview=(
"Chronic rhinosinusitis (CRS) is 12 weeks or more of sinonasal inflammation confirmed by endoscopy or CT. "
"Phenotyping (with or without polyps) and endotyping (type 2 versus non-type 2 inflammation) predict response to steroids, surgery, and biologics."),
physiology=(
"**Mucociliary clearance**: cilia beat at about 10-15 Hz, moving the mucus blanket toward natural ostia and then the nasopharynx. "
"**Ostiomeatal complex**: the shared drainage pathway of the maxillary, anterior ethmoid, and frontal sinuses through the middle meatus. "
"**Epithelial barrier**: tight junctions and innate defenses (antimicrobial peptides, nitric oxide) keep microbes and allergens out. "
"**Immune tone**: healthy sinonasal mucosa maintains low-level, balanced immune surveillance."),
pathophysiology=(
"**Multifactorial inflammation**: CRS is not simply blocked ostia or infection; barrier dysfunction, dysregulated immunity, and microbial factors interact. "
"**Type 2 endotype**: eosinophils, IL-4, IL-5, IL-13, and high IgE; associated with polyps, asthma, AERD, recurrence, and good response to steroids and biologics. "
"**Non-type 2 endotypes**: neutrophilic (type 3, IL-17) or type 1 (interferon-gamma) inflammation, more common in CRSsNP and some Asian populations. "
"**Barrier breakdown**: impaired tight junctions allow antigen and bacterial products to penetrate and perpetuate inflammation. "
"**Biofilms and S. aureus**: biofilms resist antibiotics, and S. aureus enterotoxins can act as superantigens that amplify type 2 inflammation. "
"**Why phenotype matters**: type 2 disease recurs after surgery without ongoing topical steroid, while biologics target specific type 2 cytokines."),
),

"AERD": dict(
overview=(
"Aspirin-exacerbated respiratory disease (AERD, Samter triad) is CRS with nasal polyps, asthma, and respiratory reactions to aspirin and other COX-1 inhibitors. "
"It produces the most aggressive, recurrent polyp disease and is treated with complete surgery followed by aspirin desensitization or biologics."),
physiology=(
"**Arachidonic acid pathways**: cyclooxygenase (COX) makes prostaglandins and thromboxane; 5-lipoxygenase makes leukotrienes. "
"**Prostaglandin E2 brake**: PGE2 normally inhibits mast cells and 5-lipoxygenase, restraining leukotriene production. "
"**Cysteinyl leukotrienes**: potent mediators of bronchoconstriction, mucus secretion, and eosinophil recruitment."),
pathophysiology=(
"**Baseline dysregulation**: patients overproduce cysteinyl leukotrienes and underproduce PGE2, with upregulated leukotriene receptors. "
"**COX-1 inhibition reaction**: aspirin or NSAIDs remove the remaining PGE2 brake, causing a surge of leukotrienes and mast-cell mediators typically within minutes to a few hours, producing congestion, rhinorrhea, and bronchospasm. "
"**Platelet contribution**: platelet-adherent leukocytes supply extra leukotriene production. "
"**Type 2 inflammation**: dense eosinophilic polyps with high IL-5 and IL-13 drive rapid recurrence and anosmia. "
"**Desensitization logic**: controlled aspirin exposure followed by daily high-dose aspirin downregulates leukotriene receptors and reduces polyp regrowth. "
"**Leukotriene modifiers**: montelukast or zileuton blunt the pathway; respiratory reactions to alcohol are a common clue (reported by most AERD patients in the literature)."),
),

"Frontal Recess / Frontal Sinus": dict(
overview=(
"The frontal recess is the narrow, cell-crowded hourglass-shaped pathway draining the frontal sinus into the middle meatus. "
"It is the most technically demanding area of endoscopic sinus surgery and the most common site of iatrogenic stenosis and revision."),
physiology=(
"**Development**: the frontal sinus pneumatizes from the anterior ethmoids after early childhood, reaching adult size in adolescence. "
"**Drainage path**: the frontal ostium narrows into the recess, bounded by the agger nasi anteriorly, the ethmoid bulla and skull base posteriorly, the lamina papyracea laterally, and the middle turbinate medially. "
"**Uncinate attachment**: whether the uncinate attaches to the lamina papyracea, skull base, or middle turbinate determines whether drainage enters the ethmoid infundibulum or middle meatus. "
"**Frontal cells**: agger nasi, supra-agger, supra-bullar, and frontal septal cells (IFAC classification) shape the pathway. "
"**Mucociliary pattern**: frontal sinus mucus circulates up the medial wall, across the roof, and down the lateral wall to exit the ostium."),
pathophysiology=(
"**Obstruction**: cells, edema, polyps, or scar narrowing the recess block drainage and ventilation, causing frontal sinusitis. "
"**Mucocele formation**: long-standing obstruction lets mucus accumulate under pressure, slowly expanding and remodeling bone. "
"**Iatrogenic stenosis**: stripping mucosa circumferentially exposes bone, leading to osteitis and scar contracture across the narrow outflow. "
"**Complication routes**: the posterior table and skull base lie directly behind (CSF leak, intracranial spread), and the anterior ethmoid artery runs along the posterior recess boundary. "
"**Why mucosal preservation matters**: preserved mucosa heals with functional cilia, whereas denuded bone heals with fibrosis and neo-osteogenesis."),
),

"CSF Rhinorrhea": dict(
overview=(
"CSF rhinorrhea is cerebrospinal fluid leaking into the nose through a skull-base defect, from trauma, surgery, elevated intracranial pressure, tumor, or congenital defects. "
"It carries a lifetime risk of meningitis and needs confirmation with beta-2 transferrin, localization, and usually endoscopic repair."),
physiology=(
"**CSF dynamics**: about 500 mL is produced daily by the choroid plexus and absorbed by arachnoid granulations; normal opening pressure is about 10-15 cm H2O (spontaneous leaks often 25-27 cm H2O). "
"**Weak skull-base sites**: the lateral lamella of the cribriform plate (thinnest bone, Keros classification), the cribriform plate itself, the ethmoid roof, the sphenoid lateral recess, and the frontal sinus posterior table. "
"**Meningeal barrier**: dura and arachnoid separate CSF from the sinonasal tract."),
pathophysiology=(
"**Traumatic leaks**: skull-base fractures tear dura; many close within 7-10 days with conservative care. "
"**Iatrogenic leaks**: injury to the lateral lamella or skull base during sinus or skull-base surgery. "
"**Spontaneous leaks**: idiopathic intracranial hypertension transmits chronically elevated pressure through thin bone, creating arachnoid pits and meningoencephaloceles, often at the cribriform plate or a pneumatized sphenoid lateral recess; patients are often obese women. "
"**Positional drainage**: leakage increases with leaning forward or straining (Valsalva). "
"**Meningitis risk**: an open path from the nasal cavity to the subarachnoid space allows bacterial ascent, so closure is recommended. "
"**Repair failure**: untreated elevated ICP raises recurrence risk, so ICP management (acetazolamide, weight loss, shunting) accompanies repair in spontaneous leaks."),
),

"Nasal Anatomy for Endoscopy": dict(
overview=(
"Endoscopic nasal anatomy (septum, turbinates, meatuses, ostiomeatal complex, sphenoethmoidal recess, and skull base) is the map behind every rhinology diagnosis and procedure. "
"Knowing the landmarks and variants is what keeps sinus surgery safe."),
physiology=(
"**Lateral wall**: the inferior, middle, and superior turbinates overlie meatuses; the nasolacrimal duct opens in the inferior meatus. "
"**Middle meatus**: holds the uncinate process, ethmoid infundibulum, maxillary ostium, ethmoid bulla, and hiatus semilunaris. "
"**Basal lamellae**: the middle turbinate basal lamella divides anterior from posterior ethmoid cells. "
"**Posterior drainage**: posterior ethmoids drain to the superior meatus; the sphenoid drains to the sphenoethmoidal recess medial to the superior turbinate. "
"**Skull base**: slopes downward from anterior to posterior; the lamina papyracea forms the lateral wall of the ethmoids. "
"**Arteries**: the sphenopalatine artery enters behind the middle turbinate; anterior and posterior ethmoid arteries cross the ethmoid roof."),
pathophysiology=(
"**Variants that obstruct**: concha bullosa, paradoxical middle turbinate, Haller (infraorbital) cells, and large agger nasi cells narrow drainage pathways. "
"**Variants that endanger**: Onodi (sphenoethmoidal) cells can surround the optic nerve; dehiscent carotid or optic canals in the sphenoid; a deep Keros type III olfactory fossa makes the lateral lamella vulnerable; a dehiscent lamina papyracea risks orbital entry. "
"**Maxillary ostium location**: the natural ostium is hidden behind the uncinate; accessory ostia cause recirculation if not joined to it. "
"**Why the CT checklist**: preoperative review of each danger variant (e.g., the teaching mnemonic CLOSE: cribriform, lamina, Onodi, sphenoid, ethmoid arteries) prevents complications."),
),

"Inferior Turbinate Hypertrophy": dict(
overview=(
"Inferior turbinate hypertrophy is enlargement of the turbinate mucosa or bone that obstructs nasal airflow, often from rhinitis. "
"Treatment balances airway improvement against preserving the turbinate's warming and humidifying function to avoid empty nose syndrome."),
physiology=(
"**Erectile tissue**: venous sinusoids in the submucosa engorge and shrink under autonomic control, regulating airway resistance. "
"**Internal valve region**: the head of the inferior turbinate sits near the internal nasal valve, the narrowest point of the airway. "
"**Air conditioning**: the turbinates create turbulence that maximizes mucosal contact for warming, humidification, and particle deposition. "
"**Sensation of airflow**: TRPM8 cold receptors in the mucosa sense airflow cooling, which is perceived as nasal patency."),
pathophysiology=(
"**Mucosal hypertrophy**: chronic allergic, nonallergic, or medication-induced inflammation causes submucosal edema, fibrosis, and glandular hyperplasia. "
"**Bony hypertrophy**: a large conchal bone contributes in some patients and does not respond to medical therapy. "
"**Compensatory hypertrophy**: the turbinate opposite a septal deviation enlarges to fill the extra space. "
"**Rhinitis medicamentosa**: rebound vasodilation after topical decongestant overuse causes persistent swelling. "
"**Surgical rationale**: submucosal reduction shrinks the erectile tissue or bone while preserving the mucosal surface; aggressive resection destroys airflow sensation and conditioning."),
),

"Septal Deviation": dict(
overview=(
"Septal deviation is displacement of the cartilaginous or bony septum causing nasal obstruction when it narrows the valve or airway. "
"It is extremely common; it needs correction only when it causes symptoms or blocks access, and septoplasty preserves an L-strut for support."),
physiology=(
"**Components**: quadrangular cartilage anteriorly, perpendicular plate of the ethmoid posterosuperiorly, vomer posteroinferiorly, and the maxillary crest inferiorly. "
"**Support**: the caudal and dorsal septum form an L-shaped strut that supports the nasal dorsum and tip. "
"**Internal valve**: the angle between the septum and upper lateral cartilage (normally 10-15 degrees) is the narrowest airway segment. "
"**Poiseuille physics**: airway resistance rises steeply as radius falls (to the fourth power in laminar flow), so small narrowing at the valve matters greatly."),
pathophysiology=(
"**Origins**: developmental asymmetry or trauma (including birth trauma) displaces cartilage, often with spurs at the vomer-cartilage junction. "
"**Obstruction**: anterior and caudal deviations near the valve produce more obstruction than posterior deviations. "
"**Secondary effects**: compensatory turbinate hypertrophy, sinus outflow obstruction, mucosal drying and crusting on the convex side, and epistaxis. "
"**Septal cartilage memory**: cartilage tends to return to its deviated shape unless intrinsic stresses are released. "
"**Support loss**: overresection of the L-strut causes saddle nose and columellar retraction, which is why at least about 1 cm of dorsal and caudal strut is preserved."),
),

"Recurrent Acute Rhinosinusitis": dict(
overview=(
"Recurrent acute rhinosinusitis is four or more episodes of acute bacterial rhinosinusitis per year with symptom-free intervals. "
"Evaluation looks for anatomic obstruction, allergy, and immune deficiency, and selected patients benefit from targeted sinus surgery."),
physiology=(
"**Normal recovery**: after a viral cold, mucociliary clearance and ostial patency restore within days to weeks. "
"**Ostial narrowness**: natural maxillary ostia are small, so modest edema can close them. "
"**Host defenses**: secretory IgA, antimicrobial proteins, and intact cilia clear bacteria."),
pathophysiology=(
"**Viral trigger**: each episode usually starts with a viral infection that inflames mucosa, impairs cilia, and blocks ostia. "
"**Bacterial superinfection**: stasis allows S. pneumoniae, H. influenzae, and M. catarrhalis to multiply. "
"**Predisposing anatomy**: Haller cells, concha bullosa, uncinate variants, and septal deviations narrow the ostiomeatal complex so normal edema causes obstruction. "
"**Host factors**: allergy, immunodeficiency (low IgA, IgG subclass, specific antibody deficiency), and ciliary disorders raise episode frequency. "
"**Why surgery helps selected patients**: widening the outflow tract means the same mucosal swelling no longer closes the ostium."),
),

"CRSsNP": dict(
overview=(
"CRS without nasal polyps (CRSsNP) is chronic sinonasal inflammation with congestion, discharge, pressure, or smell loss and no polyps. "
"It is more often non-type 2 and is managed with saline, topical steroids, culture-directed antibiotics when infected, and sinus surgery when medical therapy fails."),
physiology=(
"**Drainage and ventilation**: each sinus depends on a patent natural ostium and mucociliary clearance moving mucus toward it. "
"**Ostiomeatal complex**: the shared middle-meatal outflow for the maxillary, anterior ethmoid, and frontal sinuses, where small amounts of swelling cause obstruction. "
"**Epithelial barrier**: tight junctions and antimicrobial peptides keep microbes and antigens out of the submucosa. "
"**Balanced mucosal immunity**: healthy mucosa maintains low-level surveillance without chronic inflammation. "
"**Sinus bone**: thin bone beneath the mucosa remodels in response to chronic inflammation."),
pathophysiology=(
"**Inflammatory profile**: often neutrophilic and type 1 inflammation with fibrosis and basement membrane thickening rather than edema. "
"**Ostial obstruction cycle**: inflammation narrows ostia, stasis promotes infection, and infection deepens inflammation. "
"**Osteitis**: chronically inflamed bone thickens and may itself perpetuate inflammation and resist medical therapy. "
"**Contributors**: anatomic obstruction, odontogenic sources, biofilms, immunodeficiency, and environmental exposures. "
"**Surgical logic**: surgery restores drainage and creates access for topical therapy, which is critical for long-term control."),
),

"CRSwNP": dict(
overview=(
"CRS with nasal polyps (CRSwNP) is chronic sinonasal inflammation with edematous polyps arising from the middle meatus and ethmoids. "
"In Western patients it is usually type 2 (eosinophilic), associated with asthma and AERD, and treated with steroids, complete surgery, and biologics."),
physiology=(
"**Ethmoid origin**: polyps arise most often from the ethmoid and middle meatus mucosa. "
"**Mucosal homeostasis**: epithelial barrier integrity and balanced immune signals prevent excessive tissue edema."),
pathophysiology=(
"**Type 2 inflammation**: epithelial alarmins (TSLP, IL-33, IL-25) activate ILC2s and Th2 cells; IL-5 recruits and sustains eosinophils, while IL-4 and IL-13 drive IgE and tissue remodeling. "
"**Edema formation**: albumin and fibrin accumulate in the stroma, and reduced tissue plasminogen activator impairs fibrin breakdown, trapping fluid and forming polyps. "
"**Symptoms**: mechanical obstruction plus olfactory cleft inflammation cause congestion and anosmia. "
"**S. aureus enterotoxins**: act as superantigens driving local polyclonal IgE. "
"**Recurrence**: inflammation continues after surgery, so long-term topical steroid (often high-volume irrigation) is required. "
"**Biologic targets**: dupilumab (IL-4Ralpha), omalizumab (IgE), mepolizumab (IL-5), and tezepelumab (TSLP) interrupt specific steps of type 2 inflammation."),
),

"AFRS": dict(
overview=(
"Allergic fungal rhinosinusitis (AFRS) is a noninvasive, intensely allergic reaction to fungi colonizing the sinuses, producing eosinophilic mucin and expansile polyposis. "
"It occurs in immunocompetent, atopic young patients, often in warm humid climates, and needs complete surgery plus postoperative steroids."),
physiology=(
"**Universal fungal exposure**: everyone inhales fungal spores that deposit on sinonasal mucus. "
"**Mucociliary clearance**: removes spores within hours in a healthy sinus. "
"**Immune tolerance**: healthy mucosa does not mount IgE responses to fungal antigens. "
"**Th2 immunity**: in atopic individuals, IL-4, IL-5, and IL-13 drive IgE production and eosinophil recruitment. "
"**Sinus expansion**: sinus walls remodel under sustained pressure."),
pathophysiology=(
"**Hypersensitivity**: fungi (often dematiaceous species such as Bipolaris and Curvularia, and Aspergillus) trigger IgE-mediated (type I) and immune complex (type III) reactions. "
"**Allergic mucin**: thick, peanut-butter-like mucin full of eosinophils, Charcot-Leyden crystals (eosinophil breakdown), and fungal hyphae without tissue invasion. "
"**Expansion**: mucin accumulates under pressure and expands sinuses, thinning bone and causing proptosis or telecanthus. "
"**Imaging**: heterogeneous hyperdensity on CT (metallic and protein concentrations) and signal void on T2 MRI. "
"**Why surgery is essential**: removing mucin and fungal antigen reduces the antigen load; recurrence is common without postoperative steroids and close follow-up."),
),

"Invasive Fungal Rhinosinusitis": dict(
overview=(
"Acute invasive fungal rhinosinusitis is angioinvasive fungal infection (Mucorales, Aspergillus) in immunocompromised hosts that spreads in hours to days. "
"It is a surgical emergency requiring early biopsy, debridement, antifungals, and reversal of immunosuppression."),
physiology=(
"**Neutrophil defense**: neutrophils and macrophages kill inhaled spores and hyphae. "
"**Iron sequestration**: transferrin binds free iron, limiting fungal growth. "
"**Vascular supply**: rich mucosal blood supply of the turbinates, septum, and palate."),
pathophysiology=(
"**Host susceptibility**: neutropenia, uncontrolled diabetes with ketoacidosis, steroids, and transplant immunosuppression impair killing. "
"**Ketoacidosis**: acidosis releases iron from transferrin, and Mucorales use iron to grow; these fungi also have ketone reductase. "
"**Angioinvasion**: hyphae invade vessel walls, causing thrombosis, infarction, and necrotic tissue, which appears pale or black and insensate. "
"**Early sign**: loss of mucosal sensation and pallor of the middle turbinate or septum precede black eschar. "
"**Spread**: through vessels and perineural routes to the orbit (vision loss, ophthalmoplegia), cavernous sinus, and brain. "
"**Treatment logic**: necrotic tissue has no blood supply so antifungals cannot reach it, which is why debridement to bleeding tissue is essential."),
),

"Mucocele": dict(
overview=(
"A mucocele is an epithelium-lined, mucus-filled sac that expands a sinus after outflow obstruction, most often frontal or frontoethmoid. "
"It remodels bone slowly and can push into the orbit or cranium, and is treated by endoscopic marsupialization."),
physiology=(
"**Ventilation and drainage**: sinus mucus is constantly produced and cleared through patent ostia. "
"**Bone remodeling**: bone responds to pressure by resorption on one side and new formation on the other."),
pathophysiology=(
"**Obstruction**: prior surgery, trauma, polyps, tumor, or chronic inflammation block an outflow tract. "
"**Expansion**: continued mucus secretion into a closed space raises pressure and stimulates bone remodeling through osteoclast-activating factors. "
"**Mass effect**: frontoethmoid mucoceles cause proptosis, diplopia, and orbital displacement; sphenoid mucoceles can compress the optic nerve. "
"**Mucopyocele**: infection adds urgency, with pain and orbital or intracranial complications. "
"**Treatment logic**: marsupialization opens the sac widely into the nasal cavity, restoring drainage; the lining can be left in place."),
),

"Sinonasal Inverted Papilloma": dict(
overview=(
"Inverted papilloma is a benign but locally aggressive epithelial tumor of the lateral nasal wall with a recurrence risk and about 5-15 percent association with squamous cell carcinoma. "
"Treatment is complete endoscopic resection including the attachment site."),
physiology=(
"**Schneiderian membrane**: the ectodermally derived ciliated respiratory mucosa lining the nose and sinuses, distinct from the endodermal mucosa of the lower airway. "
"**Epithelial turnover**: basal cells continuously renew the epithelium, a process that viral infection and carcinogens can dysregulate. "
"**Basement membrane**: a structural barrier between epithelium and stroma; benign tumors respect it, while invasive carcinoma crosses it. "
"**Lateral wall**: the middle meatus and maxillary sinus are exposed to the highest inhaled particle and viral load."),
pathophysiology=(
"**Endophytic growth**: epithelium grows inward (inverts) into the stroma while keeping an intact basement membrane. "
"**Origin site**: usually the lateral nasal wall or maxillary sinus; the attachment pedicle often shows focal hyperostosis on CT, which helps locate it. "
"**Molecular drivers**: activating EGFR mutations are typical of inverted papilloma and persist in carcinomas arising from it; low-risk HPV is found in some, and high-risk HPV is linked to transformation. "
"**Recurrence mechanism**: residual disease at the attachment site regrows, so subperiosteal dissection and drilling of the attachment bone matter. "
"**Malignancy**: synchronous or metachronous SCC occurs, so all tissue is sent for pathology and surveillance is long-term."),
),

"Sinonasal Malignancy": dict(
overview=(
"Sinonasal malignancies are a diverse group (SCC, adenocarcinoma, esthesioneuroblastoma, SNUC, mucosal melanoma, and others) that present late with unilateral symptoms. "
"Histology drives treatment more than in most head and neck sites."),
physiology=(
"**Confined spaces**: the sinuses are bony boxes adjacent to the orbit, skull base, and pterygopalatine fossa. "
"**Lymphatics**: the sinonasal tract drains to retropharyngeal and level II nodes, but early nodal spread is uncommon. "
"**Olfactory epithelium**: specialized neuroepithelium at the cribriform plate."),
pathophysiology=(
"**Occupational exposures**: wood dust (intestinal-type adenocarcinoma, ethmoid), leather dust, nickel, and formaldehyde. "
"**Silent growth**: tumors fill air spaces before causing symptoms, so they present late with unilateral obstruction, epistaxis, facial numbness, proptosis, or trismus. "
"**Spread paths**: orbital invasion, skull base and dural invasion, and perineural spread along V2 into the pterygopalatine fossa. "
"**Histology matters**: esthesioneuroblastoma arises from olfactory neuroepithelium (Kadish/Hyams grading); SNUC and SMARCB1-deficient carcinomas are aggressive and often treated with induction chemotherapy; mucosal melanoma has poor survival. "
"**Treatment logic**: complete resection (often endoscopic) with adjuvant radiation for most, guided by histology."),
),

"Endoscopic Maxillary Antrostomy": dict(
overview=(
"Endoscopic maxillary antrostomy widens the natural maxillary ostium after uncinectomy to restore drainage and access for topical therapy. "
"Its key principle is incorporating the natural ostium to prevent mucus recirculation."),
physiology=(
"**Natural ostium**: located in the posterior ethmoid infundibulum, behind the uncinate, angled superiorly and medially. "
"**Mucociliary direction**: cilia drive maxillary mucus toward the natural ostium regardless of any accessory openings. "
"**Fontanelles**: anterior and posterior membranous areas of the medial maxillary wall may contain accessory ostia."),
pathophysiology=(
"**Recirculation**: an antrostomy not joined to the natural ostium (or an accessory ostium left separate) lets mucus exit the natural ostium and re-enter through the other opening, causing persistent infection. "
"**Ostial obstruction**: inflammation or anatomic variants block the natural ostium, causing stasis and infection. "
"**Complication anatomy**: the orbit lies superior, the nasolacrimal duct anterior (risk of epiphora if the antrostomy is extended too far forward), and the sphenopalatine vessels posterior. "
"**Surgical logic**: removing the uncinate and widening the natural ostium posteriorly and inferiorly restores physiologic drainage."),
),

"Ethmoidectomy": dict(
overview=(
"Endoscopic ethmoidectomy removes ethmoid air-cell partitions to restore drainage and open the ethmoid sinus for topical therapy and surveillance. "
"It requires precise knowledge of the skull base, lamina papyracea, and ethmoid arteries."),
physiology=(
"**Labyrinth**: multiple air cells divided by lamellae; the middle turbinate basal lamella separates anterior and posterior cells. "
"**Boundaries**: lamina papyracea laterally, skull base superiorly, middle turbinate medially, sphenoid face posteriorly. "
"**Skull base slope**: it descends from anterior to posterior and is lowest medially at the lateral lamella."),
pathophysiology=(
"**Disease reservoir**: obstructed cells harbor inflammation and polyps and block frontal and maxillary drainage. "
"**Complications**: orbital injury through the lamina (orbital fat exposure, medial rectus injury), anterior ethmoid artery injury (retro-orbital hematoma), and skull-base injury (CSF leak). "
"**Retro-orbital hematoma mechanism**: an injured anterior ethmoid artery retracts into the orbit and bleeds, raising orbital pressure and compressing the optic nerve. "
"**Mucosal preservation**: stripping mucosa causes osteitis and scarring; complete but mucosa-sparing dissection improves outcomes."),
),

"Sphenoidotomy": dict(
overview=(
"Endoscopic sphenoidotomy opens the sphenoid sinus through its natural ostium (transnasal) or through the posterior ethmoids (transethmoidal). "
"The sphenoid's walls carry the optic nerve and carotid artery, making anatomic precision essential."),
physiology=(
"**Natural ostium**: in the sphenoethmoidal recess, medial to the superior turbinate, about 1.5 cm above the choana. "
"**Lateral wall**: optic nerve superolaterally and internal carotid inferolaterally, with the opticocarotid recess between. "
"**Pneumatization**: conchal, presellar, or sellar types; extensive pneumatization can involve the pterygoid processes and lateral recess. "
"**Septations**: intersinus septa often insert onto the carotid canal."),
pathophysiology=(
"**Isolated sphenoid disease**: fungal ball, mucocele, inflammation, or tumor causes deep headache and, with lateral extension, optic or cranial nerve symptoms. "
"**Danger**: dehiscent carotid or optic canals (in a meaningful minority) and septations attached to the carotid mean twisting a septum can lacerate the artery. "
"**Onodi cell**: a posterior ethmoid cell lateral and superior to the sphenoid can carry the optic nerve, misleading the surgeon. "
"**Safe entry**: opening medially and inferiorly at the natural ostium avoids the lateral wall structures."),
),

"Epistaxis Surgical Control": dict(
overview=(
"Surgical control of epistaxis (endoscopic sphenopalatine artery ligation, anterior ethmoid artery ligation, or embolization) is used when packing fails. "
"Choosing the target depends on bleeding location and arterial anatomy."),
physiology=(
"**External carotid supply**: the sphenopalatine artery (from the internal maxillary) supplies the posterior lateral wall and septum; the greater palatine and superior labial arteries contribute anteriorly. "
"**Internal carotid supply**: anterior and posterior ethmoid arteries (from the ophthalmic) supply the superior septum and lateral wall. "
"**Kiesselbach plexus**: anterior septal anastomosis (Little area), source of most anterior bleeds. "
"**Woodruff plexus**: posterior lateral venous plexus implicated in posterior bleeds."),
pathophysiology=(
"**Posterior bleeding**: from sphenopalatine branches, harder to pack, common in older and hypertensive or anticoagulated patients. "
"**Why SPA ligation works**: clipping the artery and its branches at the crista ethmoidalis reduces flow to the posterior nose with high success. "
"**Collateral failure**: ethmoid artery bleeding (internal carotid territory) is not controlled by SPA ligation or external carotid embolization. "
"**Embolization risks**: external carotid embolization can spread emboli to the internal circulation through anastomoses, causing stroke or blindness, which is why ethmoid arteries are ligated surgically instead."),
),

"Acute Bacterial Rhinosinusitis": dict(
overview=(
"Acute bacterial rhinosinusitis (ABRS) is bacterial sinus infection, usually after a viral cold, diagnosed by symptoms lasting 10 days or more, severe onset, or worsening after improvement (double worsening). "
"Most acute rhinosinusitis is viral, so diagnostic criteria guide antibiotic use."),
physiology=(
"**Sterility and clearance**: the sinuses are normally kept nearly sterile by mucociliary clearance and patent ostia. "
"**Viral colds**: most cause transient sinus mucosal inflammation visible on CT, which resolves within 7-10 days."),
pathophysiology=(
"**Viral phase**: rhinovirus and other viruses damage cilia, cause edema, and block ostia. "
"**Bacterial superinfection**: stasis allows S. pneumoniae, H. influenzae, and M. catarrhalis to proliferate in a minority of colds. "
"**Time course logic**: symptoms persisting beyond 10 days or a second worsening indicate bacterial infection rather than a resolving virus. "
"**Complications**: spread through thin bone or valveless veins causes orbital (via the lamina papyracea) and intracranial complications. "
"**Treatment logic**: amoxicillin-clavulanate covers beta-lactamase-producing H. influenzae and M. catarrhalis; watchful waiting is valid for uncomplicated cases."),
),

"Odontogenic Sinusitis": dict(
overview=(
"Odontogenic sinusitis is maxillary sinus infection from a dental source: periapical infection, oroantral fistula, or dental implant and graft complications. "
"It is often unilateral and foul-smelling, and it fails unless the dental source is treated."),
physiology=(
"**Root proximity**: the roots of the maxillary premolars and molars (especially the first and second molars) lie just beneath, and sometimes project into, the maxillary sinus floor, separated by thin bone or only mucosa. "
"**Schneiderian membrane**: lines the sinus floor and is all that separates some roots from the sinus. "
"**Drainage path**: maxillary mucus must climb to the natural ostium high on the medial wall, so floor infections drain poorly. "
"**Oral vs sinus flora**: normally separated by bone and mucosa."),
pathophysiology=(
"**Spread**: periapical abscess or periodontal infection erodes the thin floor and spreads to the sinus. "
"**Polymicrobial anaerobes**: oral anaerobes cause foul-smelling, unilateral purulent drainage. "
"**Iatrogenic routes**: extractions creating oroantral fistulas, implants, or bone grafts in the sinus. "
"**Why ENT treatment alone fails**: an ongoing dental source reseeds the sinus, so coordinated dental treatment and often endoscopic surgery are needed. "
"**Imaging clue**: unilateral maxillary disease with periapical lucency or dental pathology on CT."),
),

"Fungal Ball": dict(
overview=(
"A fungal ball (mycetoma) is a noninvasive mass of densely packed fungal hyphae in a sinus, usually maxillary, in an immunocompetent person. "
"It is cured by endoscopic removal and does not need antifungals."),
physiology=(
"**Spore exposure is universal**: everyone inhales Aspergillus and other spores daily, and they land on sinus mucus. "
"**Mucociliary clearance**: cilia move the mucus blanket and trapped spores to the natural ostium within minutes to hours, so spores never stay long enough to grow. "
"**Ventilation**: an open ostium keeps the sinus aerated and near atmospheric oxygen tension, which is unfavorable for dense fungal growth in stagnant secretions. "
"**Maxillary drainage**: the maxillary ostium sits high on the medial wall, so drainage depends entirely on ciliary transport rather than gravity, making the maxillary sinus the most vulnerable site."),
pathophysiology=(
"**Poor clearance**: impaired drainage allows spores to accumulate and grow into a mass (usually Aspergillus). "
"**Dental association**: root canal sealers containing zinc may promote fungal growth in the maxillary sinus. "
"**No invasion**: hyphae stay in the lumen without tissue or vascular invasion and without a strong allergic response. "
"**Imaging**: a single sinus opacification with central hyperdensities or calcifications on CT. "
"**Why surgery cures**: removal of the mass and restoring drainage eliminates it; antifungals are unnecessary."),
),

"Orbital Complications of Sinusitis": dict(
overview=(
"Orbital complications of sinusitis range from preseptal cellulitis to orbital cellulitis, subperiosteal abscess, orbital abscess, and cavernous sinus thrombosis (Chandler classification). "
"They are most common in children with ethmoiditis and threaten vision."),
physiology=(
"**Lamina papyracea**: the paper-thin lateral ethmoid wall, with natural dehiscences and neurovascular foramina. "
"**Orbital septum**: separates preseptal tissues from the orbit proper. "
"**Valveless veins**: ophthalmic veins connect the face, sinuses, orbit, and cavernous sinus without valves."),
pathophysiology=(
"**Spread**: infection crosses the lamina papyracea or travels through valveless veins from the ethmoids into the orbit. "
"**Preseptal cellulitis**: anterior to the septum, eyelid swelling with normal vision and eye movement. "
"**Orbital cellulitis**: postseptal, causing chemosis, proptosis, painful or limited eye movement. "
"**Subperiosteal abscess**: pus collects between the lamina and periorbita, displacing the globe. "
"**Vision threat**: rising orbital pressure compresses the optic nerve and its blood supply; decreased acuity, color vision loss, or an afferent pupillary defect demand urgent drainage. "
"**Cavernous sinus thrombosis**: bilateral findings, cranial neuropathies (III, IV, V1, V2, VI), and sepsis."),
),

"Intracranial Complications of Sinusitis": dict(
overview=(
"Intracranial complications of sinusitis (epidural, subdural, and brain abscess, meningitis, venous sinus thrombosis, and Pott puffy tumor) are most common in adolescent boys with frontal sinusitis. "
"They require neurosurgical and sinus drainage plus prolonged IV antibiotics."),
physiology=(
"**Frontal sinus posterior table**: separates the sinus from the frontal lobe dura. "
"**Diploic veins of Breschet**: valveless veins connect the sinus mucosa, frontal bone marrow, and dural venous system. "
"**Adolescent frontal sinus**: rapidly pneumatizing with a rich diploic venous supply."),
pathophysiology=(
"**Spread**: retrograde thrombophlebitis through valveless diploic veins or direct erosion through bone. "
"**Osteomyelitis**: frontal bone infection with subperiosteal abscess produces Pott puffy tumor (forehead swelling). "
"**Intracranial collections**: epidural abscess, subdural empyema (rapidly progressive), and frontal lobe abscess, often with subtle early symptoms (headache, behavior change). "
"**Microbiology**: Streptococcus anginosus group and anaerobes. "
"**Treatment logic**: drainage of the intracranial collection and the source sinus plus prolonged antibiotics."),
),

"Revision FESS": dict(
overview=(
"Revision endoscopic sinus surgery treats persistent or recurrent CRS after prior surgery, most often from incomplete dissection, scarring, or uncontrolled type 2 inflammation. "
"Success depends on identifying why the first operation failed."),
physiology=(
"**Healing**: sinus mucosa regenerates with functional cilia if preserved; exposed bone heals with fibrosis. "
"**Stable landmarks**: in revision cases, the skull base, lamina, maxillary sinus roof, and medial orbital wall remain reliable even when turbinates are gone."),
pathophysiology=(
"**Common failure patterns**: residual uncinate, unopened agger nasi or frontal cells, missed maxillary ostium with recirculation, lateralized middle turbinate, retained ethmoid partitions. "
"**Scar and synechiae**: adhesions between the middle turbinate and lateral wall obstruct drainage. "
"**Osteitis and neo-osteogenesis**: inflamed bone thickens and narrows outflow tracts, especially the frontal recess. "
"**Disease biology**: eosinophilic CRSwNP, AERD, and AFRS recur despite good surgery, so medical maintenance and biologics matter. "
"**Revision risk**: distorted landmarks increase the danger of skull-base and orbital injury, which favors image guidance."),
),

"Frontal Sinusotomy / Draf Procedures": dict(
overview=(
"Draf procedures progressively widen frontal drainage: Draf I (recess clearance), Draf IIa and IIb (ostium widening), and Draf III (endoscopic modified Lothrop, connecting both frontal sinuses). "
"They match the size of the opening to the severity of disease."),
physiology=(
"**Frontal outflow**: narrow, variable, and surrounded by the skull base, orbit, and ethmoid cells. "
"**Frontal beak**: the anterior bony boundary of the outflow tract, drilled in extended procedures. "
"**Mucosal healing**: openings shrink as they heal, most with circumferential mucosal loss."),
pathophysiology=(
"**Restenosis**: circumferential mucosal stripping and exposed bone lead to fibrosis and new bone that close the neo-ostium. "
"**Rationale for Draf III**: a common frontal opening is large enough to stay patent despite scarring and allows high-volume irrigation access. "
"**Indications follow failure**: recalcitrant frontal disease, mucoceles, tumors, and failed prior surgery. "
"**Complications**: CSF leak at the first olfactory neuron, orbital injury, and restenosis."),
),

"Endoscopic CSF Leak Repair / Nasoseptal Flap": dict(
overview=(
"Endoscopic CSF leak repair closes skull-base defects with grafts (fat, fascia, mucosa) or vascularized flaps, most commonly the pedicled nasoseptal flap. "
"Vascularized reconstruction dramatically lowered leak rates after endoscopic skull-base surgery."),
physiology=(
"**Nasoseptal flap supply**: the posterior septal artery, a branch of the sphenopalatine artery, enters across the sphenoid face. "
"**Healing**: vascularized tissue heals faster and resists CSF pressure better than free grafts. "
"**Layered closure**: inlay and onlay grafts reconstruct dura and skull base."),
pathophysiology=(
"**High-flow vs low-flow leaks**: opening a cistern or ventricle creates high-flow leaks that need vascularized flaps. "
"**Pressure and failure**: elevated ICP, obesity, and high-flow leaks increase failure. "
"**Flap viability**: the pedicle must be protected during sphenoidotomy and posterior septectomy, or the flap may be lost. "
"**Donor-site morbidity**: crusting and septal changes, with a small risk of perforation. "
"**Lumbar drains**: used selectively to reduce CSF pressure in high-risk leaks."),
),

"Juvenile Nasopharyngeal Angiofibroma": dict(
overview=(
"Juvenile nasopharyngeal angiofibroma (JNA) is a benign but locally aggressive, highly vascular tumor in adolescent males, arising near the sphenopalatine foramen. "
"It presents with unilateral obstruction and severe epistaxis and is resected endoscopically after embolization."),
physiology=(
"**Sphenopalatine foramen region**: connects the nasal cavity to the pterygopalatine fossa, where the internal maxillary artery branches. "
"**Pterygoid base**: the vidian canal and pterygoid plates lie just below."),
pathophysiology=(
"**Hormonal influence**: androgen receptors in tumor cells explain occurrence in adolescent males. "
"**Vascular malformation component**: irregular vessels without smooth muscle cannot contract, causing severe bleeding. "
"**Spread**: grows along paths of least resistance into the nasopharynx, pterygopalatine fossa, infratemporal fossa, sphenoid, orbit, and middle cranial fossa. "
"**Imaging signs**: anterior bowing of the posterior maxillary wall (Holman-Miller sign) and widening of the pterygopalatine fossa. "
"**Recurrence**: residual tumor in the vidian canal and pterygoid base causes recurrence, so drilling the basisphenoid matters. "
"**No biopsy in clinic**: biopsy can cause life-threatening bleeding."),
),
}
