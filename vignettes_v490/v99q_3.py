"""v99: board vignettes built from the textbook gap-review additions (batch 3)."""
VIGNETTES = [
    {
        "topic": "Free-Flap Monitoring / Compromise / Salvage",
        "concept_id": "v6-head-neck-oncology-free-flap-monitoring-compromise-salvage",
        "stem": "A 62-year-old man is returned to the OR 20 hours after a fibula free flap because the skin paddle is congested and dusky. A venous thrombus is removed and the anastomosis revised, yet skin-edge bleeding remains sluggish, suggesting residual microvascular clot within the flap. Which adjunct specifically addresses formed microemboli in the capillary bed?",
        "choices": [
            "Intra-arterial thrombolytic infusion (urokinase or tPA) into the flap",
            "Dextran 40 infusion for 5 days",
            "Topical heparin irrigation at 100 U/mL",
            "A systemic unfractionated heparin bolus and infusion"
        ],
        "answer": 0,
        "explanation": "After thrombectomy and revision, residual capillary microemboli are treated with an intra-arterial thrombolytic delivered through the flap artery. Heparin prevents new thrombus but does not dissolve clot that has already formed. Dextran 40 showed no outcome benefit in a prospective trial and carries anaphylaxis, volume-overload and renal risks. Topical heparin irrigation has not improved flap survival. Venous thrombosis is the more common cause of failure and damages the flap more than arterial insufficiency.",
        "why_wrong": [
            "Correct.",
            "Dextran 40 failed to improve outcome and risks anaphylaxis and pulmonary edema.",
            "Topical heparin irrigation at 100 U/mL showed no measurable flap benefit.",
            "Systemic heparin prevents propagation but cannot lyse thrombus already lodged in capillaries."
        ],
        "board_pearl": "Heparin prevents clot; only thrombolytics dissolve formed microemboli after flap thrombectomy.",
        "curveball": "If venous congestion persists after salvage and leeches are applied, which infection must you anticipate?",
        "curveball_answer": "Medicinal leeches relieve congestion through salivary anticoagulants such as hirudin, but they carry Aeromonas hydrophila. Plan for that organism when leech therapy is used. Hyperbaric oxygen helps only after the thrombus is cleared. Remember that most anastomotic thromboses occur within the first 48 to 72 hours.",
        "learning_stage": "senior_decision",
        "focus": "management"
    },
    {
        "topic": "Frontal Recess / Frontal Sinus",
        "concept_id": "v6-rhinology-allergy-skull-base-frontal-recess-frontal-sinus",
        "stem": "A 34-year-old man reports a slowly enlarging forehead bulge over 3 years without pain or infection. CT shows a fully aerated right frontal sinus expanded beyond its normal bony margins, with thin intact walls, no fluid, no ground-glass matrix and no dural mass. What is the most appropriate treatment once mimics are excluded?",
        "choices": [
            "Osteoplastic flap with fat obliteration of the sinus",
            "Endoscopic opening of the frontal ostium to relieve the outflow valve",
            "Cranialization of the frontal sinus",
            "Observation only, since expansion of an aerated sinus is self-limited"
        ],
        "answer": 1,
        "explanation": "This is pneumosinus dilatans, a rare benign over-expansion of an air-filled sinus beyond its normal margin, usually noticed as forehead deformity. A one-way ostial valve is the proposed mechanism, so opening the ostium typically stops expansion and may shrink the sinus. Fibrous dysplasia and an underlying dural meningioma must be excluded first. It differs from a mucocele, which is fluid-filled. Obliteration and cranialization are far more morbid than needed.",
        "why_wrong": [
            "Obliteration is unnecessary because relieving the ostial valve halts the expansion.",
            "Correct.",
            "Cranialization is for shattered posterior tables, not a benign aerated expansion.",
            "The deformity keeps progressing while the valve persists, so observation is inappropriate."
        ],
        "board_pearl": "Pneumosinus dilatans: aerated over-expansion from an ostial valve; open the ostium.",
        "curveball": "Which two lesions must be ruled out before labeling an expanded aerated frontal sinus pneumosinus dilatans?",
        "curveball_answer": "Fibrous dysplasia and an underlying dural meningioma can both cause adjacent sinus hyperpneumatization. Contrast MRI and the CT bone pattern help exclude them. Only then should the expansion be attributed to an ostial valve. Pneumosinus dilatans is usually discovered because of forehead deformity or mass effect rather than infection.",
        "learning_stage": "application",
        "focus": "diagnosis"
    },
    {
        "topic": "Frontal Sinus Fracture",
        "concept_id": "v6-facial-plastics-trauma-frontal-sinus-fracture",
        "stem": "A 28-year-old man has an isolated anterior table frontal sinus fracture after an assault, with an intact posterior table. CT 2 weeks later shows persistent fluid filling only the right frontal sinus; the right outflow tract appears injured while the left outflow tract and left sinus are normal. Which management best restores drainage?",
        "choices": [
            "Cranialization with removal of the posterior table",
            "Osteoplastic flap with obliteration of both frontal sinuses",
            "Intersinus septectomy so the right sinus drains through the left outflow tract",
            "Discharge without imaging follow-up because mucoceles do not follow anterior table fractures"
        ],
        "answer": 2,
        "explanation": "Fluid persisting more than about 10 days after injury suggests outflow obstruction. When only one outflow tract is injured, removing the intersinus septum lets the obstructed side drain through the healthy one. Obliteration is reserved for injury to both outflow tracts or severe comminution, and cranialization for a shattered posterior wall. Outflow injury is the most common cause of post-traumatic mucocele, which can appear years later, so long-term imaging follow-up is required.",
        "why_wrong": [
            "Cranialization is for a shattered posterior wall, which this patient does not have.",
            "Obliteration is reserved for bilateral outflow injury or severe comminution.",
            "Correct.",
            "Outflow injury is the leading cause of post-traumatic mucocele, which may appear years later."
        ],
        "board_pearl": "One injured frontal outflow tract: intersinus septectomy; both injured: obliterate or Draf III.",
        "curveball": "Why are frontal sinus fractures uncommon in a 4-year-old, and what does that do to the fracture pattern?",
        "curveball_answer": "The frontal sinus is not radiographically present until about age 5 to 6, so there is no crumple zone. Fractures are greenstick and run toward the vertex or across the orbital roof, with high rates of brain injury.",
        "learning_stage": "application",
        "focus": "management"
    },
    {
        "topic": "Frontal Sinusotomy / Draf Procedures",
        "concept_id": "v6-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures",
        "stem": "A 47-year-old woman with CRS with nasal polyps and aspirin-exacerbated respiratory disease undergoes revision frontal sinus surgery. Neo-osteogenesis narrows the right frontal recess, and the surgeon realizes the drill will be needed to widen it. Polyps fill the frontal recess, and she required systemic steroids twice in the past year. How should the frontal procedure proceed?",
        "choices": [
            "Stop at a Draf IIa while preserving all recess mucosa, avoiding the drill",
            "Stop at a Draf IIb, because unilateral drilling suffices in inflammatory disease",
            "Convert to an osteoplastic flap with obliteration at this first revision",
            "Proceed to a full Draf III rather than stopping at a drilled unilateral opening"
        ],
        "answer": 3,
        "explanation": "Drilling the frontal recess causes unavoidable circumferential mucosal injury and stenosis. The 'all or none' rule says that once the drill is needed for inflammatory disease, the surgeon should complete a Draf III. Draf IIb is reserved for healthy-mucosa conditions such as an inverted papilloma attachment or a mucocele that has already eroded the medial recess. AERD and extensive polyposis are also accepted reasons to consider a primary Draf III.",
        "why_wrong": [
            "A Draf IIa cannot address bony neo-osteogenesis that already requires drilling.",
            "A drilled Draf IIb in inflamed mucosa invites circumferential stenosis.",
            "Osteoplastic obliteration is reserved for failures such as a failed Draf III.",
            "Correct."
        ],
        "board_pearl": "Drill in inflamed frontal recess? Go all the way to Draf III.",
        "curveball": "Six weeks after Draf III, a thick web forms at the beak. What early measure reduces neo-ostial stenosis?",
        "curveball_answer": "Neo-ostial stenosis occurs in 10 to 30%, especially with asthma, allergy, CF or prior frontal surgery. Inject steroid into an early web within the first 3 months. Established scar can be excised, optionally with mitomycin C, with final patency above 90%. Asthma, allergy, cystic fibrosis and prior frontal surgery all raise restenosis risk.",
        "learning_stage": "senior_decision",
        "focus": "surgery"
    },
    {
        "topic": "Frontal Sinusotomy / Draf Procedures",
        "concept_id": "v6-rhinology-allergy-skull-base-frontal-sinusotomy-draf-procedures",
        "stem": "A 52-year-old man with recalcitrant frontal sinusitis after two prior Draf IIa procedures is being planned for an outside-in Draf III. The surgeon reviews his sagittal and axial CT to confirm he is an anatomic candidate. He has no CSF leak history, his asthma is controlled, and his inflammatory disease is currently quiescent. Which CT finding is the only anatomic contraindication to this approach?",
        "choices": [
            "Under 5 mm between the posterior table and the skin in front of the frontal beak",
            "Frontal pneumatization extending over the far lateral orbital roof",
            "A prominent nasofrontal beak narrowing the ostium",
            "Evidence of a prior failed osteoplastic obliteration"
        ],
        "answer": 0,
        "explanation": "With the outside-in technique, the only anatomic contraindication to Draf III is an anteroposterior depth under 5 mm between the posterior table and the skin anterior to the beak. Draf III reaches nearly all of the frontal sinus except the far lateral orbital roof, which limits access but does not contraindicate surgery. Failed osteoplastic obliteration is an indication for salvage Draf III. A prominent beak is a target of extended surgery, not a barrier.",
        "why_wrong": [
            "Correct.",
            "Far lateral disease limits reach but is not a contraindication to Draf III.",
            "A prominent beak is a common reason Draf IIa fails and is drilled away.",
            "Failed osteoplastic obliteration is an indication for salvage Draf III."
        ],
        "board_pearl": "Draf III's only anatomic contraindication: under 5 mm AP depth at the beak.",
        "curveball": "When should a planned Draf III be delayed even in a good anatomic candidate?",
        "curveball_answer": "Delay surgery while inflammatory disease is very active and still needs systemic steroids. Operating into highly inflamed mucosa raises the risk of neo-ostial stenosis. Medical optimization comes first. With the outside-in technique, the only anatomic contraindication is under 5 mm of anteroposterior depth at the beak.",
        "learning_stage": "application",
        "focus": "imaging"
    },
    {
        "topic": "Functional Nasal Obstruction",
        "concept_id": "v6-facial-plastics-trauma-functional-nasal-obstruction",
        "stem": "A 36-year-old man with no prior nasal surgery, trauma or facial weakness reports fixed bilateral nasal obstruction, worse on the left. Anterior rhinoscopy shows a narrowed left internal nasal valve angle, and decongestion helps only slightly. He breathes better when he pulls his cheek laterally, and the external nose looks straight. Which is the most common cause of internal nasal valve obstruction?",
        "choices": [
            "Facial nerve paralysis with loss of nasal dilators",
            "Dorsal septal deviation",
            "Over-resection of the lateral crura",
            "Age-related weakening of the upper lateral cartilages"
        ],
        "answer": 1,
        "explanation": "The internal valve contributes about half of total nasal airway resistance, and dorsal septal deviation is its most common cause of obstruction. Other causes of valve collapse include over-resection of the lateral crus or scroll, caudal septal deflection, aging, trauma and facial nerve paralysis. The septum-upper lateral cartilage angle is about 10 to 15 degrees in White patients and typically wider in Black, Asian and Hispanic noses. This unoperated, neurologically normal patient fits the common cause.",
        "why_wrong": [
            "Facial paralysis causes collapse, but he has normal facial function.",
            "Correct.",
            "Lateral crural over-resection is iatrogenic, and this patient has no prior surgery.",
            "Aging contributes to valve collapse but is not the most common cause."
        ],
        "board_pearl": "Internal valve: about half of nasal resistance; dorsal septal deviation is the top cause.",
        "curveball": "Why does a patient with longstanding facial paralysis develop nasal obstruction on the paralyzed side?",
        "curveball_answer": "Facial nerve paralysis removes the nasal dilator muscles that stent the valve during inspiration. The lateral wall then collapses. This is one recognized cause of valve collapse alongside trauma and aging. Dorsal septal deviation remains the most common cause of internal valve obstruction overall.",
        "learning_stage": "foundation",
        "focus": "anatomy"
    },
    {
        "topic": "Functional Septorhinoplasty",
        "concept_id": "v6-facial-plastics-trauma-functional-septorhinoplasty",
        "stem": "A 29-year-old woman seeks functional septorhinoplasty for a twisted nose after a sports injury. On lateral view, her columella hangs with about 6 mm of columellar show, and the caudal septum is long and deviated off the nasal spine. Her bony vault deviates to the right, and her cartilaginous dorsum curves back to the left. Which maneuver best corrects the hanging columella?",
        "choices": [
            "Complete lateral osteotomies extending to the radix",
            "Perform asymmetric dorsal hump reduction",
            "Address the caudal septum by trimming or setting it back and fixing it to the spine",
            "Place long spreader grafts alone"
        ],
        "answer": 2,
        "explanation": "A hanging or retracted columella is corrected by addressing the caudal septum, through trimming, a setback, or an extension or plumping graft. In the twisted nose the caudal septum is also straightened and fixed to the spine with sutures or a burr hole. Ideal columellar show on lateral view is 2 to 4 mm. Spreader grafts, asymmetric hump removal and complete osteotomies treat dorsal deviation, not columellar position.",
        "why_wrong": [
            "Osteotomies realign the bony pyramid and do not change columellar position.",
            "Asymmetric hump reduction treats dorsal asymmetry, not columellar show.",
            "Correct.",
            "Spreader grafts straighten the cartilaginous dorsum but do not raise the columella."
        ],
        "board_pearl": "Hanging columella: fix the caudal septum; target 2 to 4 mm columellar show.",
        "curveball": "For her deviated cartilaginous dorsum, how should the dorsal hump be removed?",
        "curveball_answer": "Remove the hump asymmetrically, taking more from the longer side. Combine this with long, wide spreader grafts, scoring along existing angles, and transseptal coaptation sutures. Complete osteotomies, including intermediate cuts when needed, realign the bony vault. Make complete osteotomies, including cuts up to the radix when needed.",
        "learning_stage": "application",
        "focus": "surgery"
    },
    {
        "topic": "Geriatric Otolaryngology / Frailty",
        "concept_id": "v6-general-ent-emergencies-geriatric-otolaryngology-frailty",
        "stem": "A 79-year-old woman reports a dry mouth for a year that she blames on aging. She takes oxybutynin for bladder symptoms, amitriptyline for sleep and a diuretic. Oral exam shows dry mucosa without masses. Her daughter asks whether this is simply normal for her age. What is the most appropriate first step?",
        "choices": [
            "Reassure her that salivary flow normally fails after age 80",
            "Start pilocarpine without changing other medications",
            "Proceed directly to minor salivary gland biopsy",
            "Review and adjust her medications, especially the anticholinergics"
        ],
        "answer": 3,
        "explanation": "Polypharmacy, especially anticholinergic drugs, along with dehydration and systemic disease, are the main reversible causes of xerostomia in older adults. Medications should be reviewed before dryness is attributed to age. About 65% of people over 60 who complain of dry mouth have objective salivary hypofunction. Healthy unmedicated adults over 80 have lower unstimulated whole saliva, but stimulated parotid flow appears preserved, so aging alone does not explain significant dryness.",
        "why_wrong": [
            "Stimulated parotid flow appears preserved in healthy unmedicated older adults.",
            "Adding a sialagogue ignores the reversible drug cause.",
            "Biopsy is premature before reversible medication causes are addressed.",
            "Correct."
        ],
        "board_pearl": "Dry mouth in older adults: blame drugs before age; review anticholinergics first.",
        "curveball": "Which major salivary gland shows more age-related acinar atrophy and fat replacement?",
        "curveball_answer": "After about age 70, acinar atrophy, fibrosis, fat replacement, duct dilation and oncocytic change appear. These changes are greater in the submandibular gland than the parotid gland. Polypharmacy with anticholinergics remains the leading reversible cause and should be addressed first.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Glomus Tumor / Paraganglioma",
        "concept_id": "v6-otology-neurotology-glomus-tumor-paraganglioma",
        "stem": "A 52-year-old woman with a large glomus jugulare tumor undergoes angiography before planned infratemporal fossa resection. Feeders include the ascending pharyngeal artery and a stylomastoid branch. The interventionalist plans particle embolization of the stylomastoid branch. The tumor extends below the internal auditory canal, and lower cranial nerve function is intact. What should be done first?",
        "choices": [
            "Superselective injection of 1% preservative-free lidocaine as a provocative test",
            "Embolize immediately with large coils, since particles never reach the nerve",
            "Balloon occlusion testing of the internal carotid artery",
            "Skip embolization because jugulare tumors do not need it"
        ],
        "answer": 0,
        "explanation": "The stylomastoid artery can supply the facial nerve, so a provocative test with 1% preservative-free lidocaine is performed before particle embolization. A negative test is reassuring. Jugulare tumors are compartmentalized, each compartment fed by its own external carotid branch, most often the ascending pharyngeal and posterior middle meningeal arteries. Balloon occlusion testing is for planned ICA sacrifice. Glomus tympanicum, not jugulare, is usually resected without embolization.",
        "why_wrong": [
            "Correct.",
            "Embolizing without testing risks facial nerve ischemia from this branch.",
            "Balloon occlusion testing assesses ICA sacrifice, not facial nerve supply.",
            "Jugulare tumors are commonly embolized; it is tympanicum tumors that often skip it."
        ],
        "board_pearl": "Before embolizing the stylomastoid artery, do a lidocaine provocative test.",
        "curveball": "How long after embolization should the jugulare resection be scheduled, and why not later?",
        "curveball_answer": "Resect 24 to 48 hours after embolization. Waiting longer allows collateral recruitment and revascularization of the tumor. Also screen metanephrines preoperatively, since a secreting tumor can cause a hypertensive crisis. Glomus tympanicum, by contrast, is usually small enough to resect without embolization.",
        "learning_stage": "senior_decision",
        "focus": "management"
    },
    {
        "topic": "Glomus Tumor / Paraganglioma",
        "concept_id": "v6-otology-neurotology-glomus-tumor-paraganglioma",
        "stem": "A 45-year-old man has a parapharyngeal mass and a new left vocal fold paralysis. MRI shows an enhancing mass about 2 cm below the skull base that displaces the internal and external carotid arteries anteriorly without splaying them. He asks what complete removal would mean for his function. Which counseling point is most accurate?",
        "choices": [
            "Malignancy is diagnosed by atypical histology at resection",
            "Complete resection almost always sacrifices the vagus, so voice and swallowing rehabilitation are needed",
            "Embolization is contraindicated for this tumor",
            "The vagus can usually be preserved because the tumor arises outside the nerve"
        ],
        "answer": 1,
        "explanation": "Anterior carotid displacement without ICA-ECA splaying, with vocal fold paralysis, fits a vagal paraganglioma, most of which arise from the nodose ganglion about 2 cm below the skull base. Complete resection almost always sacrifices the vagus, so counseling must cover voice and swallowing rehabilitation. A transcervical approach suits nodose tumors. Preoperative embolization is commonly advised for high vagal tumors. Malignancy is defined by metastasis, not histology.",
        "why_wrong": [
            "Paraganglioma malignancy is defined by metastasis, not by histologic features.",
            "Correct.",
            "Preoperative embolization is commonly advised for high vagal tumors.",
            "The tumor arises within the vagal ganglion, so the nerve is rarely saved."
        ],
        "board_pearl": "Vagal paraganglioma: carotid pushed anteriorly without splaying; resection usually sacrifices vagus.",
        "curveball": "Which head and neck paraganglioma site has the highest malignancy rate, and how is malignancy defined?",
        "curveball_answer": "Malignancy occurs in about 2 to 4% overall and is highest in vagal tumors. It is defined by metastasis to non-neuroendocrine tissue such as nodes, bone or lung. Histology cannot define it. Preoperative alpha blockade before any beta blocker is required for secreting tumors.",
        "learning_stage": "application",
        "focus": "counseling"
    },
    {
        "topic": "Glottic Cancer",
        "concept_id": "v6-head-neck-oncology-glottic-cancer",
        "stem": "A 66-year-old man completed definitive radiation for a T1 glottic SCC 8 months ago. He still smokes. Laryngoscopy shows persistent edema of the treated fold and arytenoid without a visible exophytic mass, and his voice remains rough. His original tumor involved the mid-third of the fold with normal mobility, treated with 2.25-Gy fractions. What is the most appropriate next step?",
        "choices": [
            "Reassure him and repeat laryngoscopy in another 6 months",
            "Deliver a second course of radiation to the larynx",
            "Deep biopsy under anesthesia because persistent edema suggests deep recurrence",
            "Proceed directly to total laryngectomy without tissue diagnosis"
        ],
        "answer": 2,
        "explanation": "Edema persisting more than 6 months after radiation signals deep recurrence in about 45% of cases, so tissue diagnosis is needed rather than observation. Radiation cannot be repeated, which is one reason surgery is sometimes chosen first to keep radiation in reserve. Radical surgery requires confirmed recurrence. Continued smoking is also an adverse factor for local control. Second primaries, lung first, are the leading cause of death in early glottic cancer.",
        "why_wrong": [
            "Observation risks missing a deep recurrence, present in nearly half of such cases.",
            "Radiation for laryngeal cancer is generally not repeatable.",
            "Correct.",
            "Laryngectomy needs a confirmed recurrence before it is undertaken."
        ],
        "board_pearl": "Post-RT laryngeal edema beyond 6 months: assume deep recurrence until biopsy proves otherwise.",
        "curveball": "If his biopsy is negative, what is the most common cause of death in early glottic cancer survivors?",
        "curveball_answer": "Second primary tumors, with lung cancer first, are the leading cause of death. Five-year relative survival is about 90% for T1N0 and 75% for T2N0. Lifelong surveillance and smoking cessation matter. Late radiation risks also include hypothyroidism, carotid stenosis and radiation-induced malignancy.",
        "learning_stage": "senior_decision",
        "focus": "management"
    },
    {
        "topic": "Gradenigo Syndrome (Petrous Apicitis)",
        "concept_id": "v6-otology-neurotology-gradenigo-syndrome-petrous-apicitis",
        "stem": "A 2-year-old with acute mastoiditis still has purulent otorrhea one week after cortical mastoidectomy. She now has retro-orbital pain and a new left abducens palsy. CT shows the petrous apex is not pneumatized. Her parents ask how infection reached the apex. She has no meningeal signs, and MRI shows enhancement and fluid in the apex. Which mechanism best explains it?",
        "choices": [
            "Retrograde spread through the cochlear aqueduct",
            "Spread through well-aerated petrous air cells",
            "Hematogenous seeding from bacteremia alone",
            "Spread by thrombophlebitis or osteitis, which does not require pneumatized cells"
        ],
        "answer": 3,
        "explanation": "The petrous apex does not pneumatize before about age 3, and only about 30% of people have a well-pneumatized apex. Petrous infection can still occur because it spreads by thrombophlebitis or osteitis rather than through air cells. Suspect apical involvement when drainage persists after simple mastoidectomy. The Gradenigo triad of V1 pain, otorrhea and abducens palsy is often incomplete, and abducens palsy is a late sign.",
        "why_wrong": [
            "The cochlear aqueduct links meninges and labyrinth, not mastoid and apex.",
            "Her apex is not pneumatized, and the apex rarely aerates before age 3.",
            "Contiguous venous and bony spread, not bacteremia alone, is the described route.",
            "Correct."
        ],
        "board_pearl": "Petrositis spreads by thrombophlebitis or osteitis; apex pneumatization is not required.",
        "curveball": "How were the Pittsburgh pediatric petrositis cases managed, and was the apex opened?",
        "curveball_answer": "All four resolved with IV antibiotics and cortical mastoidectomy without opening the apex. Chronic petrous osteomyelitis from CSOM or cholesteatoma, with Pseudomonas, Proteus or TB, is now more common than acute petrositis. Abducens palsy is a late sign, and the full triad is often incomplete.",
        "learning_stage": "application",
        "focus": "mechanism"
    },
    {
        "topic": "Grafts / Implants / Biomaterials in ENT",
        "concept_id": "v6-general-ent-emergencies-grafts-implants-biomaterials-in-ent",
        "stem": "A 31-year-old man wants chin augmentation with an alloplastic implant. He asks for a material that allows soft-tissue ingrowth to stabilize it and resist migration, rather than one that becomes encapsulated. He has no history of radiation, prior implants or infection at the planned site. Which implant material best meets this goal?",
        "choices": [
            "Porous polyethylene with interconnected 100 to 200 micron pores",
            "Polymethyl methacrylate molded in situ",
            "Silicone",
            "Expanded polytetrafluoroethylene"
        ],
        "answer": 0,
        "explanation": "Porous polyethylene (Medpor) has interconnected pores of about 100 to 200 microns that allow soft-tissue ingrowth. Silicone becomes encapsulated with no ingrowth and has a high extrusion rate in the nose. PMMA is rigid and molded in situ without ingrowth. ePTFE allows only limited ingrowth and can extrude. Titanium is different again, because it osseointegrates. Matching the material's tissue behavior to the site is the key selection rule.",
        "why_wrong": [
            "Correct.",
            "PMMA is rigid and allows no ingrowth.",
            "Silicone becomes encapsulated with no tissue ingrowth.",
            "ePTFE permits only limited ingrowth and can extrude."
        ],
        "board_pearl": "Medpor pores of 100 to 200 microns allow ingrowth; silicone encapsulates.",
        "curveball": "If an autologous bone graft is used instead, what two conditions does it need to take?",
        "curveball_answer": "Bone grafts need bone-to-bone contact and about 8 to 12 weeks of immobility. Cancellous bone carries more osteoblasts, while cortical bone gives strength and bone morphogenetic proteins. Resorbable PLA and PGA plates last about 1 year and are useful in children.",
        "learning_stage": "foundation",
        "focus": "surgery"
    },
    {
        "topic": "Graves Disease / Toxic Goiter",
        "concept_id": "v6-thyroid-parathyroid-salivary-graves-disease-toxic-goiter",
        "stem": "A 38-year-old woman with Graves disease controlled on methimazole has a palpable 2-cm thyroid nodule. Scintigraphy shows the nodule is hypofunctioning (cold) within a diffusely hyperactive gland. She would prefer radioiodine because it treats the Graves disease. Her thyroid-stimulating hormone receptor antibodies are elevated, and she has mild orbitopathy. Which statement best guides management?",
        "choices": [
            "Radioiodine reliably treats both the Graves disease and the nodule",
            "About 45% of such nodules are malignant, so evaluate it and favor surgery",
            "Cancer arising in Graves glands is less aggressive and can be observed",
            "Cold nodules in Graves glands are almost always benign colloid nodules"
        ],
        "answer": 1,
        "explanation": "About 45% of palpable hypofunctioning nodules in a Graves gland are malignant. Differentiated thyroid cancer is about twice as common in Graves disease and tends to be larger, more invasive and more often node-positive, so it is managed aggressively. Suspected or proven cancer is an accepted indication for thyroidectomy rather than radioiodine. Preparation includes a thionamide for 4 to 6 weeks and inorganic iodine for 7 to 10 days.",
        "why_wrong": [
            "Radioiodine treats the toxic gland but not a cold, possibly malignant nodule.",
            "Correct.",
            "Cancer in Graves glands tends to be more invasive and node-positive.",
            "Nearly half of cold nodules in Graves glands prove malignant."
        ],
        "board_pearl": "Cold nodule in Graves: about 45% malignant; DTC there is more aggressive.",
        "curveball": "When preparing her for thyroidectomy, in what order are the thionamide and iodine started?",
        "curveball_answer": "Give a thionamide for 4 to 6 weeks, and start inorganic iodine (Lugol or SSKI) for 7 to 10 days only after the thionamide. Beta blockade with iodine for 10 to 14 days is an alternative. If the nerve monitor loses signal on the first side, stage the second side.",
        "learning_stage": "application",
        "focus": "management"
    },
    {
        "topic": "HIV-Associated Head and Neck Disease",
        "concept_id": "v6-general-ent-emergencies-hiv-associated-head-and-neck-disease",
        "stem": "A 34-year-old man with untreated HIV has right otorrhea and conductive hearing loss. Exam shows a fleshy polyp arising from the external canal wall. Biopsy of the polyp shows Pneumocystis jirovecii organisms. He has no pulmonary symptoms. Audiometry shows a 30 dB conductive loss in that ear, and his CD4 count is 150. What is the appropriate treatment for this ear lesion?",
        "choices": [
            "Intravenous amphotericin B",
            "Canal wall down mastoidectomy",
            "Oral trimethoprim-sulfamethoxazole",
            "Topical ciprofloxacin drops alone"
        ],
        "answer": 2,
        "explanation": "Pneumocystis jirovecii can cause subcutaneous canal masses or aural polyps of the canal, drum or middle ear, with conductive loss and otorrhea. It may be the first sign of AIDS. It responds to oral trimethoprim-sulfamethoxazole. Surgery is not required for this infectious polyp. HIV-related ear disease also includes SNHL in roughly 30%, from causes such as otosyphilis, CMV reactivation, cryptococcal meningitis and ototoxic drugs.",
        "why_wrong": [
            "Amphotericin targets fungi such as Cryptococcus, not Pneumocystis.",
            "Pneumocystis aural polyps respond to medical therapy without mastoidectomy.",
            "Correct.",
            "Topical fluoroquinolones do not treat Pneumocystis."
        ],
        "board_pearl": "Pneumocystis aural polyp may herald AIDS; treat with oral TMP-SMX.",
        "curveball": "How much more common is sudden SNHL in HIV-positive patients, and what infections should be sought?",
        "curveball_answer": "Sudden SNHL is about twice as common as in controls. Look for otosyphilis, CMV reactivation, cryptococcal or tuberculous meningitis and toxoplasmosis, and review ototoxic drugs. HIV neurotropism itself can also contribute. Temporal bone series also show the ear is particularly prone to CMV infection.",
        "learning_stage": "application",
        "focus": "diagnosis"
    },
    {
        "topic": "HPV-Associated Oropharyngeal SCC",
        "concept_id": "v6-head-neck-oncology-hpv-associated-oropharyngeal-scc",
        "stem": "A 58-year-old man has p16-positive SCC of the right tonsil with a 25 pack-year smoking history. Staging by AJCC 7 criteria is T2 N2b. He is treated on a chemoradiation protocol and asks how his prognosis compares with other patients. Using the Ang (RTOG 0129) risk groups, which risk category applies?",
        "choices": [
            "Low risk, because HPV positivity outweighs smoking",
            "Low risk, because his T stage is only T2",
            "High risk",
            "Intermediate risk"
        ],
        "answer": 3,
        "explanation": "In the Ang secondary analysis of RTOG 0129, HPV status was the strongest survival predictor, followed by smoking (10 or fewer vs more than 10 pack-years), then T and N stage. HPV-positive patients with more than 10 pack-years and N2b to N3 disease are intermediate risk, with about 71% 3-year OS. Low risk requires 10 or fewer pack-years, or more than 10 pack-years with N0 to N2a. High risk is HPV-negative disease with T4 or heavy smoking.",
        "why_wrong": [
            "HPV positivity does not override heavy smoking with N2b disease.",
            "Nodal stage, not T2 status, moves him out of the low-risk group.",
            "High risk applies to HPV-negative patients, not HPV-positive ones.",
            "Correct."
        ],
        "board_pearl": "HPV-positive, over 10 pack-years and N2b to N3: Ang intermediate risk.",
        "curveball": "How much did the risk of death change per pack-year in that analysis, and did HPV status modify it?",
        "curveball_answer": "Risk of death rose about 1% per pack-year regardless of HPV status. That is why smokers with HPV-positive tumors do worse than nonsmokers. De-escalation should be offered only on clinical trials. HPV-positive OPSCC carries about a 57% lower risk of death in meta-analysis.",
        "learning_stage": "application",
        "focus": "counseling"
    },
    {
        "topic": "Hair Restoration Fundamentals",
        "concept_id": "v6-facial-plastics-trauma-hair-restoration-fundamentals",
        "stem": "A 35-year-old man had follicular unit transplantation to his frontal hairline 4 weeks ago. He calls in distress because most of the transplanted hairs have fallen out, though the grafted skin looks healthy without crusting or redness. He asks whether the procedure failed. He had a 2,000-graft session and followed all postoperative instructions. What is the most appropriate response?",
        "choices": [
            "Reassure him that grafted hairs shed at 2 to 6 weeks and regrow from 3 to 4 months",
            "Book a second transplant session now to replace the lost grafts",
            "Biopsy the recipient area to exclude scarring alopecia",
            "Start oral minoxidil to rescue the failing grafts"
        ],
        "answer": 0,
        "explanation": "Transplanted hairs normally shed at 2 to 6 weeks, and new growth begins at 3 to 4 months, at about half an inch per month. Results should be judged, and another session planned, only after 12 months. Grafts are vulnerable to dislodgement only in the first week. Donor dominance means grafts keep their donor behavior. Cysts and ingrown hairs at 8 to 12 weeks are the most common problems, and infection occurs in under 1%.",
        "why_wrong": [
            "Correct.",
            "Results and further sessions should be judged only after 12 months.",
            "Healthy skin with expected shedding does not suggest scarring alopecia.",
            "Oral minoxidil remains off-label and the grafts have not failed."
        ],
        "board_pearl": "Grafts shed at 2 to 6 weeks, regrow at 3 to 4 months; judge at 12 months.",
        "curveball": "He also notices thinning of his native hair next to the grafts. What is this and when does it recover?",
        "curveball_answer": "This is shock loss, a surgical telogen effluvium of native hair near the recipient site. It usually recovers by about 3 months. Reassurance is appropriate. Grafts are vulnerable to dislodgement in the first week, and results are judged at 12 months.",
        "learning_stage": "application",
        "focus": "counseling"
    },
    {
        "topic": "Hair Restoration Fundamentals",
        "concept_id": "v6-facial-plastics-trauma-hair-restoration-fundamentals",
        "stem": "A 68-year-old man with gray hair and light skin, Norwood V pattern, requests hair transplantation. Exam shows good scalp laxity, but donor-area density measures about 40 follicular units per square centimeter. He asks whether he is a good candidate. He has a supportive spouse, no scalp inflammation and stable loss for 5 years. Which finding most argues against transplantation?",
        "choices": [
            "His age of 68 years",
            "Donor density under about 50 follicular units per square centimeter",
            "Low contrast between his gray hair and light skin",
            "His Norwood V pattern of loss"
        ],
        "answer": 1,
        "explanation": "Candidates with fewer than about 50 follicular units per square centimeter in the donor area are poor candidates, because the supply cannot achieve the 20 to 40 FU per square centimeter that usually looks full in the recipient area. Older age is not a contraindication, and young patients need more conservative planning because their final pattern is unknown. Low hair-skin color contrast, such as gray hair on light skin, is favorable because it hides thinner coverage.",
        "why_wrong": [
            "Older age is not a contraindication; youth demands more caution.",
            "Correct.",
            "Low hair-skin contrast is favorable and makes grafts look denser.",
            "Norwood V loss can be treated when donor supply is adequate."
        ],
        "board_pearl": "Donor density under 50 FU/cm2 predicts a poor transplant candidate.",
        "curveball": "Where should the lowest central point of his new frontal hairline be placed?",
        "curveball_answer": "A natural hairline is convex, with its lowest central point about 7 to 10 cm above the glabella. The frontotemporal apex sits above the lateral canthus. Placing the hairline too low is a lasting error. Grafts exit at about 15 to 20 degrees at the hairline and use single-hair units.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Hashimoto Thyroiditis",
        "concept_id": "v6-thyroid-parathyroid-salivary-hashimoto-thyroiditis",
        "stem": "A 52-year-old nonsmoking woman reports 6 months of a low, rough voice, fatigue, weight gain and constipation. Laryngoscopy shows bilateral edematous but fully mobile vocal folds with no discrete lesion. She has no reflux symptoms or voice abuse. She has no history of smoking, voice overuse or recent intubation. What is the most appropriate next step?",
        "choices": [
            "Microflap excision of the edematous folds",
            "Voice therapy alone",
            "Check a TSH level",
            "Empiric twice-daily proton pump inhibitor"
        ],
        "answer": 2,
        "explanation": "Hypothyroidism causes hoarseness through mucopolysaccharide infiltration of the vocal folds. Bilateral edematous but mobile folds, especially with systemic hypothyroid symptoms, should prompt a TSH. The voice almost always recovers with hormone replacement alone, so surgery is unnecessary. About 10% of Hashimoto hypothyroidism is transient. Hypothyroidism also causes ENT findings such as SNHL, effusion from eustachian tube edema and vertigo.",
        "why_wrong": [
            "Surgery is unnecessary because the voice usually recovers with replacement.",
            "Voice therapy does not treat mucopolysaccharide infiltration from hypothyroidism.",
            "Correct.",
            "Her systemic symptoms point to hypothyroidism rather than reflux."
        ],
        "board_pearl": "Bilateral edematous mobile folds with hypothyroid symptoms: check TSH before surgery.",
        "curveball": "What proportion of adults with myxedema have bilateral SNHL, and what conductive cause coexists?",
        "curveball_answer": "About 30 to 40% of adults with myxedema have bilateral SNHL. Conductive loss arises from eustachian tube edema with effusion. Vertigo occurs in about two thirds. About 10% of Hashimoto hypothyroidism is transient, so reassess the need for lifelong replacement.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Head & Neck Cancer Surveillance / Second Primaries",
        "concept_id": "v6-head-neck-oncology-head-neck-cancer-surveillance-second-primaries",
        "stem": "A 60-year-old man completed definitive chemoradiation for p16-positive oropharyngeal SCC 4 weeks ago. His neck exam shows resolving nodes. He is anxious and requests a PET/CT this week to confirm response. He has no new symptoms, and his post-treatment swallowing is improving with therapy. When should his baseline post-treatment PET/CT be obtained?",
        "choices": [
            "Not at all, because exam alone suffices in year 1",
            "At 12 months, once treatment effects have fully resolved",
            "Now, at 4 weeks after completing treatment",
            "No sooner than about 12 weeks after therapy, within the first 6 months"
        ],
        "answer": 3,
        "explanation": "NCCN surveillance recommends baseline post-treatment imaging of the primary and neck within 6 months, with PET/CT no sooner than about 12 weeks after definitive therapy. Earlier scans are confounded by treatment-related inflammation. History and exam with mirror or flexible laryngoscopy occur every 1 to 3 months in year 1. TSH every 6 to 12 months is added after neck irradiation, along with speech, swallow, hearing, dental and depression screening.",
        "why_wrong": [
            "Baseline post-treatment imaging is recommended within 6 months.",
            "Waiting 12 months exceeds the 6-month window for baseline imaging.",
            "Scanning at 4 weeks is confounded by post-treatment inflammation.",
            "Correct."
        ],
        "board_pearl": "Post-CRT PET/CT: no sooner than 12 weeks, within 6 months.",
        "curveball": "Which blood test is used in surveillance of nasopharyngeal carcinoma specifically?",
        "curveball_answer": "EBV DNA is monitored in nasopharyngeal carcinoma surveillance. TSH every 6 to 12 months applies to any irradiated neck. Speech, swallow, hearing, dental and depression screening also belong in every survivorship visit. History and exam continue every 1 to 3 months in year 1.",
        "learning_stage": "foundation",
        "focus": "imaging"
    },
    {
        "topic": "Head & Neck Radiation Toxicity / Survivorship",
        "concept_id": "v6-head-neck-oncology-head-neck-radiation-toxicity-survivorship",
        "stem": "A 57-year-old woman in week 4 of radiation for oral cavity SCC has painful mucosal ulcerations of the tongue and buccal mucosa. She can swallow only liquids and cannot manage soft solids, but she is still taking enough by mouth to stay hydrated. What WHO oral mucositis grade is this?",
        "choices": [
            "Grade 3",
            "Grade 2",
            "Grade 4",
            "Grade 1"
        ],
        "answer": 0,
        "explanation": "WHO grade 1 is erythema and soreness. Grade 2 is erythema and pain with solids still possible. Grade 3 is ulceration with a liquid-only diet. Grade 4 is ulceration so severe that oral intake is impossible. Mucositis begins at 2 to 3 weeks of treatment. Supportive care includes oral rinses, cool foods, topical anesthetic mixtures and stopping tobacco and alcohol. Candida, HSV and bacterial superinfection are common.",
        "why_wrong": [
            "Correct.",
            "Grade 2 still allows solid food.",
            "Grade 4 means oral intake is impossible, and she still drinks liquids.",
            "Grade 1 is erythema and soreness without ulceration."
        ],
        "board_pearl": "WHO mucositis: grade 3 is ulceration with liquids only; grade 4 is nothing by mouth.",
        "curveball": "After radiation she has severe xerostomia. When will pilocarpine help, and what side effect is common?",
        "curveball_answer": "Muscarinic agonists such as pilocarpine or cevimeline help only when residual gland parenchyma remains, and benefit takes weeks. Sweating is the classic side effect. Otherwise use water, sugar-free sialagogues and saliva substitutes. Gustatory sour stimuli are the strongest natural sialagogues.",
        "learning_stage": "foundation",
        "focus": "complication"
    },
    {
        "topic": "Head and Neck Sarcomas, Chordoma and Chondrosarcoma",
        "concept_id": "v6-head-neck-oncology-head-and-neck-sarcomas-chordoma-and-chondrosarcoma",
        "stem": "A 4-year-old boy undergoes endoscopic endonasal resection of a large clival chordoma, but residual tumor remains along the dura. His parents ask whether further treatment is needed, noting they read that chordomas grow slowly. Pathology confirms conventional chordoma, and he has recovered without new neurologic deficits. Which recommendation is most appropriate?",
        "choices": [
            "Reoperation only once symptoms recur",
            "Adjuvant radiation, advised for large or subtotally resected tumors",
            "Primary chemotherapy in place of radiation",
            "Observation, because pediatric chordomas are indolent"
        ],
        "answer": 1,
        "explanation": "In children the clivus is the most common chordoma site, and younger patients have faster growth and worse outcomes, especially under age 5. Radiation is advised for large or subtotally resected tumors. Metastases occur in 10 to 20% clinically and up to 43% at autopsy, and overall 5-year survival is about 54%. Among pediatric skull base malignancies, chordoma has intermediate survival of about 60 to 70% at 5 years.",
        "why_wrong": [
            "Waiting for symptoms ignores the advice to irradiate subtotal resections.",
            "Correct.",
            "Chemotherapy is not the stated adjuvant for subtotal chordoma resection.",
            "Chordoma in young children grows faster and behaves worse, not indolently."
        ],
        "board_pearl": "Pediatric chordoma: clivus, worse under age 5; irradiate large or subtotal resections.",
        "curveball": "Across pediatric skull base malignancies, which histologies have the worst and best survival?",
        "curveball_answer": "Histology predicts survival. SCC and salivary cancers do worst, high-grade sarcoma, esthesioneuroblastoma and chordoma are intermediate at 60 to 70% at 5 years, and low-grade sarcoma does best. Pediatric skull base malignancy shows bimodal peaks at about 3.5 and 17.5 years.",
        "learning_stage": "senior_decision",
        "focus": "pediatrics"
    },
    {
        "topic": "Hearing Aids and Bone-Conduction Devices",
        "concept_id": "v6-otology-neurotology-hearing-aids-and-bone-conduction-devices",
        "stem": "A 67-year-old man with chronically draining ears cannot wear conventional hearing aids. Audiometry shows bilateral mixed loss with a bone-conduction pure-tone average (0.5 to 3 kHz) of 52 dB HL in the better cochlea. He is evaluated for a percutaneous bone-anchored implant. His air-conduction thresholds are much worse because of the chronic middle-ear disease. Which statement about his candidacy is correct?",
        "choices": [
            "Candidacy depends on air-conduction rather than bone-conduction thresholds",
            "He is not a candidate because any BC PTA worse than 45 dB contraindicates implantation",
            "He needs at least a Power processor, since standard head-worn processors suit BC PTA of 45 dB or better",
            "A standard head-worn processor suffices because its limit is 65 dB"
        ],
        "answer": 2,
        "explanation": "For percutaneous bone-anchored implants, the bone-conduction PTA should be 45 dB HL or better for a standard head-worn processor, up to 55 dB for a Power processor and up to 65 dB for a Super Power processor. Benefit falls as BC thresholds worsen: 89% improved with BC PTA under 45 dB, 61% at 46 to 60 dB and 22% above 60 dB. BC thresholds worse than 65 dB contraindicate implantation.",
        "why_wrong": [
            "Bone-conduction thresholds govern candidacy for conductive and mixed loss.",
            "The contraindication is BC worse than 65 dB, not 45 dB.",
            "Correct.",
            "The 65 dB limit applies to Super Power processors, not standard ones."
        ],
        "board_pearl": "Bone-anchored processors: standard to 45, Power to 55, Super Power to 65 dB BC.",
        "curveball": "If he instead had single-sided deafness, what threshold must his hearing ear meet?",
        "curveball_answer": "For single-sided deafness, the hearing ear needs an air-conduction PTA of 20 dB HL or better. The device removes the head shadow and helps in noise, but it does not restore localization. An indication sometimes missed is an only-hearing ear with otosclerosis or atresia where repair is unwise.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Hearing Aids and Bone-Conduction Devices",
        "concept_id": "v6-otology-neurotology-hearing-aids-and-bone-conduction-devices",
        "stem": "A 61-year-old woman with moderate-to-severe SNHL received a totally implantable piezoelectric middle-ear device (Esteem) 5 years ago. It now must be removed because of a device failure, and she asks what her hearing will be like afterward without a hearing aid. She has been very satisfied with the device until now, and her cochlear function is stable. What should she be told?",
        "choices": [
            "Her hearing will return to her preimplant baseline",
            "She will become profoundly deaf from cochlear injury",
            "Her hearing will be unchanged because the ossicles were left intact",
            "She will have a maximal conductive loss because part of the incus was removed"
        ],
        "answer": 3,
        "explanation": "In the Esteem, a sensor on the malleus picks up sound and a driver on the stapes moves it. The incus is partly removed to stop feedback between them, so device failure or removal leaves a maximal conductive loss on top of the sensorineural loss. Its nonrechargeable battery is replaced surgically about every 5 years, and the device is not MRI compatible. The Carina, by contrast, leaves the ossicles intact.",
        "why_wrong": [
            "The deliberate ossicular discontinuity prevents return to preimplant hearing.",
            "The loss after removal is conductive, not a new cochlear injury.",
            "Leaving the ossicles intact describes the Carina, not the Esteem.",
            "Correct."
        ],
        "board_pearl": "Esteem removes part of the incus; failure or explant leaves maximal conductive loss.",
        "curveball": "Which semi-implantable device couples a floating mass transducer to the incus, and what are its FDA criteria?",
        "curveball_answer": "The Vibrant Soundbridge clips a floating mass transducer to the long process of the incus. FDA criteria are age 18 or older, moderate-to-severe SNHL, normal middle ear, word recognition of at least 50% and no retrocochlear disease. Mean functional gain is about 30 dB, and current models are 1.5 T but not 3 T MRI conditional.",
        "learning_stage": "application",
        "focus": "complication"
    },
    {
        "topic": "Hearing Aids and Bone-Conduction Devices",
        "concept_id": "v6-otology-neurotology-hearing-aids-and-bone-conduction-devices",
        "stem": "An 8-month-old with bilateral moderate SNHL is being fitted with behind-the-ear aids based on ABR thresholds. The audiologist measures the real-ear-to-coupler difference before programming. A resident asks why this step matters more in infants than adults. His parents are comfortable with the plan, and his ear canals are small but normal. What is the best explanation?",
        "choices": [
            "The small infant canal yields a much higher SPL than a 2-cc coupler, so RECD predicts real-ear output",
            "RECD sets maximum output from the infant's loudness discomfort responses",
            "RECD replaces ABR in estimating the infant's thresholds",
            "RECD converts pediatric fittings to adult NAL targets"
        ],
        "answer": 0,
        "explanation": "A small ear canal leaves little residual volume, so the same aid produces much higher SPL at the drum than in a 2-cc coupler or an adult ear. Measuring the RECD lets coupler measurements predict real-ear output with accuracy similar to probe microphone testing. Pediatric fittings use DSL v5 or NAL-NL2 for higher audibility. Maximum output is set from OSPL90 and targets, because infants cannot give loudness discomfort judgments.",
        "why_wrong": [
            "Correct.",
            "Infants cannot give loudness discomfort judgments, so output is set from targets.",
            "ABR thresholds remain the basis for fitting; RECD corrects acoustic output.",
            "DSL v5 is favored for children to give higher audibility."
        ],
        "board_pearl": "Infant fittings: measure RECD, because small canals amplify more than a 2-cc coupler.",
        "curveball": "What classroom signal-to-noise ratio and reverberation time are recommended for children with hearing loss?",
        "curveball_answer": "A classroom SNR of at least +15 to +30 dB is recommended, versus typical rooms at -6 to +6 dB. Reverberation should be no more than 0.4 seconds. Remote microphone systems are key, because omnidirectional aids do not improve SNR.",
        "learning_stage": "foundation",
        "focus": "pediatrics"
    },
    {
        "topic": "Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
        "concept_id": "v6-general-ent-emergencies-hemostasis-coagulopathy-antithrombotic-management-in-ent",
        "stem": "A 3-year-old boy has oozing from his adenotonsillectomy sites beginning on postoperative day 4. His mother recalls delayed bleeding from his umbilical stump as a newborn. PT, aPTT, platelet count and fibrinogen are all normal. He had no unusual bleeding after his vaccinations, and there is no family history of bleeding. Which test is most likely to reveal the diagnosis?",
        "choices": [
            "A bleeding time",
            "A specific factor XIII assay",
            "Platelet aggregation with ristocetin",
            "A 1:1 mixing study"
        ],
        "answer": 1,
        "explanation": "Factor XIII deficiency causes bleeding despite normal PT and aPTT, because those tests end before fibrin cross-linking. Clues are delayed bleeding after surgery or trauma, delayed umbilical stump bleeding and intracranial hemorrhage after minor trauma. Diagnosis needs a specific factor XIII assay. Factor XIII concentrate is now preferred treatment, with cryoprecipitate or FFP only when concentrate is unavailable. Its long half-life and low target level make prophylaxis practical.",
        "why_wrong": [
            "Bleeding time is no longer recommended in children and misses this defect.",
            "Correct.",
            "Ristocetin aggregation tests von Willebrand and GPIb function, which cause immediate mucosal bleeding.",
            "A mixing study evaluates a prolonged PT or aPTT, and both are normal."
        ],
        "board_pearl": "Delayed bleeding plus umbilical stump bleeding with normal labs: test factor XIII.",
        "curveball": "What half-life and target level make factor XIII prophylaxis practical?",
        "curveball_answer": "Factor XIII has a long half-life of about 11 to 14 days, and the target level is only above 5%. Infrequent dosing therefore maintains protection. Cryoprecipitate or FFP is used only when concentrate is unavailable.",
        "learning_stage": "application",
        "focus": "diagnosis"
    },
    {
        "topic": "Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
        "concept_id": "v6-general-ent-emergencies-hemostasis-coagulopathy-antithrombotic-management-in-ent",
        "stem": "A 4-year-old girl scheduled for adenotonsillectomy has an isolated prolonged aPTT on screening labs ordered by her pediatrician. She has no personal or family bleeding history and tolerated a dental extraction last year. A 1:1 mixing study with normal plasma fails to correct the aPTT. What is the most likely explanation?",
        "choices": [
            "Factor VIII deficiency (hemophilia A)",
            "Factor VII deficiency",
            "A benign nonspecific inhibitor such as a transient lupus anticoagulant",
            "Type 3 von Willebrand disease"
        ],
        "answer": 2,
        "explanation": "The most common cause of an isolated prolonged aPTT in children is a benign nonspecific inhibitor such as a transient lupus anticoagulant. It prolongs clotting in vitro without raising bleeding risk. A mixing study that corrects suggests a factor deficiency, while failure to correct indicates an inhibitor. Lupus anticoagulant is associated with thrombosis rather than bleeding. Factor XII, prekallikrein and high-molecular-weight kininogen deficiencies also lengthen the aPTT without bleeding.",
        "why_wrong": [
            "A factor deficiency would correct when mixed with normal plasma.",
            "Factor VII deficiency prolongs the PT, not an isolated aPTT.",
            "Correct.",
            "Type 3 VWD causes major bleeding, and its aPTT corrects on mixing."
        ],
        "board_pearl": "Isolated long aPTT that fails to correct on mixing in a well child: lupus anticoagulant.",
        "curveball": "Why does an acquired factor VIII inhibitor change the plan, even though it also fails to correct?",
        "curveball_answer": "Acquired factor VIII inhibitors cause dangerous expanding hematomas, including in the neck and airway. Unlike lupus anticoagulant, they cause real bleeding. Elective surgery should be postponed until the cause is clarified. Lupus anticoagulant causes thrombosis rather than bleeding.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
        "concept_id": "v6-general-ent-emergencies-hemostasis-coagulopathy-antithrombotic-management-in-ent",
        "stem": "A 70-year-old man on dabigatran for atrial fibrillation is scheduled for elective standard-bleeding-risk endoscopic sinus surgery. His creatinine clearance is 65 mL/min and he has no prior stroke. The anesthesiologist asks how long to hold the drug and whether bridging is needed. He has no history of mechanical valve, recent stroke or venous thromboembolism. Which plan is most appropriate?",
        "choices": [
            "Hold dabigatran about 24 hours, as for apixaban",
            "Hold dabigatran 5 days and bridge with enoxaparin",
            "Continue dabigatran through surgery",
            "Hold dabigatran about 48 hours with no bridging"
        ],
        "answer": 3,
        "explanation": "For standard-risk procedures, rivaroxaban, apixaban and edoxaban are held about 24 hours, but dabigatran about 48 hours because it is about 80% renally cleared. DOACs do not need heparin bridging because their offset and onset are rapid. Bridging is reserved for warfarin interruption in high thrombotic risk patients, such as those with mechanical valves or recent stroke. Low-risk procedures such as dental work may proceed without interruption.",
        "why_wrong": [
            "Dabigatran's renal clearance calls for a longer hold than factor Xa inhibitors.",
            "DOACs do not require bridging, and 5 days is excessive.",
            "Sinus surgery is not a low-risk procedure that can proceed on anticoagulation.",
            "Correct."
        ],
        "board_pearl": "Dabigatran: hold about 48 hours for standard-risk surgery; DOACs need no bridging.",
        "curveball": "How does the hold change for rivaroxaban or apixaban if creatinine clearance is under 50 mL/min?",
        "curveball_answer": "With creatinine clearance under 50, rivaroxaban and apixaban are held about 48 hours instead of 24. No bridging is needed. Coordinate restart timing with the surgeon's bleeding concerns. Dabigatran, being 80% renally cleared, is held about 48 hours even with normal renal function.",
        "learning_stage": "senior_decision",
        "focus": "pharmacology"
    },
    {
        "topic": "Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
        "concept_id": "v6-general-ent-emergencies-hemostasis-coagulopathy-antithrombotic-management-in-ent",
        "stem": "A 14-year-old girl has recurrent epistaxis since childhood and heavy menses. Platelet count and platelet size are normal. Aggregation studies show absent responses to ADP, epinephrine and collagen, with a normal response to ristocetin. Von Willebrand antigen and ristocetin cofactor activity are normal, and she takes no NSAIDs. Which diagnosis is most likely?",
        "choices": [
            "Glanzmann thrombasthenia",
            "Type 1 von Willebrand disease",
            "Bernard-Soulier syndrome",
            "Wiskott-Aldrich syndrome"
        ],
        "answer": 0,
        "explanation": "Glanzmann thrombasthenia is a defect of platelet GPIIb/IIIa, the receptor that bridges fibrinogen during aggregation. It causes early mucocutaneous bleeding, epistaxis and menorrhagia with normal platelet counts. Aggregation is absent with ADP, epinephrine and collagen but normal with ristocetin, which tests GPIb-VWF adhesion. Treatment is platelet transfusion. Bernard-Soulier is the mirror image, with giant platelets and an abnormal ristocetin response only.",
        "why_wrong": [
            "Correct.",
            "Type 1 VWD does not abolish aggregation to ADP, epinephrine and collagen.",
            "Bernard-Soulier shows giant platelets and an abnormal ristocetin response.",
            "Wiskott-Aldrich causes small platelets and thrombocytopenia."
        ],
        "board_pearl": "Glanzmann: GPIIb/IIIa; no aggregation except to ristocetin.",
        "curveball": "Which inherited syndromes cause platelet storage-pool defects with normal counts?",
        "curveball_answer": "Storage-pool defects occur with Hermansky-Pudlak and Chediak-Higashi syndromes. They cause mucocutaneous bleeding despite normal platelet numbers. Wiskott-Aldrich syndrome, by contrast, causes small platelets. Bernard-Soulier shows giant platelets with an abnormal ristocetin response.",
        "learning_stage": "application",
        "focus": "diagnosis"
    },
    {
        "topic": "Hungry Bone / Post-Thyroid Calcium Management",
        "concept_id": "v6-thyroid-parathyroid-salivary-hungry-bone-post-thyroid-calcium-management",
        "stem": "A 58-year-old woman with long-standing primary hyperparathyroidism and bone pain is scheduled for parathyroidectomy. The surgeon wants to identify preoperatively whether she is likely to develop profound, prolonged hypocalcemia from rapid skeletal remineralization afterward. Her calcium is 11.8 mg/dL and imaging shows diffuse osteopenia with subperiosteal resorption. Which preoperative laboratory finding best predicts this?",
        "choices": [
            "Low urinary calcium",
            "Elevated serum alkaline phosphatase",
            "Low serum PTH",
            "Elevated serum magnesium"
        ],
        "answer": 1,
        "explanation": "An elevated preoperative alkaline phosphatase predicts hungry bone syndrome, reflecting high bone turnover. Hypocalcemia also has nonsurgical causes, including hypomagnesemia, vitamin D deficiency, DiGeorge syndrome and pseudohypoparathyroidism, in which PTH is high because of end-organ resistance. When hypocalcemia is present, magnesium should be corrected first. Chvostek and Trousseau signs are the bedside findings of neuromuscular irritability.",
        "why_wrong": [
            "Low urinary calcium is not the described predictor of hungry bone.",
            "Correct.",
            "Primary hyperparathyroidism has a high, not low, PTH.",
            "Magnesium deficiency, not excess, worsens hypocalcemia."
        ],
        "board_pearl": "High preoperative alkaline phosphatase predicts hungry bone after parathyroid surgery.",
        "curveball": "How is a Trousseau sign elicited correctly?",
        "curveball_answer": "Inflate a blood pressure cuff 20 mm Hg above systolic pressure for 3 minutes and watch for carpal spasm. The Chvostek sign is facial twitching when the facial nerve is tapped. Correct hypomagnesemia first when hypocalcemia is present.",
        "learning_stage": "foundation",
        "focus": "workup"
    },
    {
        "topic": "Hyperacusis / Decreased Sound Tolerance",
        "concept_id": "v6-otology-neurotology-hyperacusis-decreased-sound-tolerance",
        "stem": "A 30-year-old woman with tinnitus finds ordinary sounds such as dishes and traffic intolerably loud. Her audiogram is normal, and loudness discomfort levels are reduced. She is considering tinnitus retraining therapy and asks what outcome to expect. She has no facial weakness, and stapedial reflexes are present bilaterally. Which statement is most accurate?",
        "choices": [
            "Her symptoms are recruitment, so TRT will not apply",
            "TRT does not change loudness discomfort levels",
            "TRT raised loudness discomfort levels about 12.5 dB and helped hyperacusis more often than tinnitus",
            "TRT helps tinnitus more often than hyperacusis"
        ],
        "answer": 2,
        "explanation": "Hyperacusis affects about 6 to 8% of normal-hearing people and 18 to 80% of tinnitus patients. Its severity does not track audiometric thresholds, which separates it from recruitment. Tinnitus retraining therapy raised loudness discomfort levels about 12.5 dB and widened dynamic range about 11 dB. It helped hyperacusis in 63% versus tinnitus in 47%. Nearly half of patients have a psychiatric disorder.",
        "why_wrong": [
            "Recruitment accompanies hearing loss, and her audiogram is normal.",
            "TRT measurably raised loudness discomfort levels.",
            "Correct.",
            "In that series hyperacusis improved more often than tinnitus."
        ],
        "board_pearl": "Hyperacusis doesn't track thresholds; TRT raised LDLs about 12.5 dB.",
        "curveball": "Name conditions associated with hyperacusis that should be sought in the history.",
        "curveball_answer": "Associations include loss of the stapedial reflex with facial palsy, migraine, Lyme disease, benzodiazepine withdrawal and Williams syndrome. Psychiatric comorbidity is common, affecting nearly half. Hyperacusis severity does not track audiometric thresholds, which separates it from recruitment.",
        "learning_stage": "application",
        "focus": "counseling"
    },
    {
        "topic": "Hypopharyngeal Cancer",
        "concept_id": "v6-head-neck-oncology-hypopharyngeal-cancer",
        "stem": "A 59-year-old man has a 3-cm SCC of the medial piriform sinus wall with a mobile hemilarynx. Endoscopy shows the tumor extends down into the piriform apex, and he has a single 2-cm ipsilateral level II node. He wants larynx-sparing surgery. Flexible laryngoscopy shows no postcricoid or interarytenoid involvement. Which finding excludes partial laryngopharyngectomy?",
        "choices": [
            "Origin on the medial piriform wall",
            "Tumor size of 3 cm",
            "An ipsilateral level II nodal metastasis",
            "Extension into the piriform apex"
        ],
        "answer": 3,
        "explanation": "Piriform apex involvement predicted laryngeal framework invasion in every case in Kirchner's whole-organ study, which is why apex disease excludes conservation surgery. Partial laryngopharyngectomy suits T1 to T2 medial wall tumors that stay more than 1.5 cm from the apex. Other contraindications are thyroid cartilage, postcricoid, interarytenoid or cervical esophageal involvement and fold fixation. Nodal disease is managed with neck dissection and does not exclude conservation surgery.",
        "why_wrong": [
            "Medial wall tumors are the typical candidates for partial laryngopharyngectomy.",
            "A 3-cm tumor is T2 and remains within conservation criteria.",
            "Nodal disease is treated by neck dissection, not by abandoning conservation.",
            "Correct."
        ],
        "board_pearl": "Piriform apex involvement predicts cartilage invasion and excludes conservation surgery.",
        "curveball": "What mucosal margins are recommended for hypopharyngeal resection in an unirradiated patient?",
        "curveball_answer": "About 3 cm inferiorly, 2 cm laterally and 1.5 cm superiorly, increasing to 4, 3 and 2 cm after radiation. Submucosal spread was found in 58% of specimens and is greatest inferiorly. Recommended margins rise to 4, 3 and 2 cm after radiation.",
        "learning_stage": "senior_decision",
        "focus": "surgery"
    },
    {
        "topic": "Hypopharyngeal Cancer",
        "concept_id": "v6-head-neck-oncology-hypopharyngeal-cancer",
        "stem": "A 63-year-old man has a 4.5-cm SCC confined to the piriform sinus and lateral pharyngeal wall. The hemilarynx is mobile, and CT shows no cartilage, hyoid, thyroid gland or central compartment invasion and no esophageal extension. Both vocal folds move normally, and the tumor does not reach the thyroid cartilage. What is the AJCC 8 T category?",
        "choices": [
            "T3",
            "T4a",
            "T2",
            "T1"
        ],
        "answer": 0,
        "explanation": "In the hypopharynx, size cutoffs drive T1 to T3, unlike the larynx. T1 is one subsite and 2 cm or less. T2 is more than one subsite or over 2 to 4 cm without hemilarynx fixation. T3 is over 4 cm, hemilarynx fixation or extension to esophageal mucosa. T4a involves thyroid or cricoid cartilage, hyoid, thyroid gland, esophageal muscle or central compartment soft tissue. This 4.5-cm tumor is T3 by size alone.",
        "why_wrong": [
            "Correct.",
            "T4a requires cartilage, hyoid, thyroid gland or central compartment invasion.",
            "T2 is limited to tumors 4 cm or less.",
            "T1 is one subsite and 2 cm or less."
        ],
        "board_pearl": "Hypopharynx T stage is size driven: 2 cm, 4 cm cutoffs; over 4 cm is T3.",
        "curveball": "What distinguishes T3 from T4a when the tumor reaches the esophagus?",
        "curveball_answer": "Extension to esophageal mucosa is T3, while invasion of esophageal muscle is T4a. Prevertebral fascia, carotid encasement or mediastinal involvement is T4b. In the hypopharynx, size cutoffs of 2 and 4 cm drive T1 to T3, unlike the larynx.",
        "learning_stage": "foundation",
        "focus": "diagnosis"
    },
    {
        "topic": "Immunocompromised Host in Otolaryngology",
        "concept_id": "v6-general-ent-emergencies-immunocompromised-host-in-otolaryngology",
        "stem": "A 29-year-old man reports 6 months of painless bilateral parotid swelling. Ultrasound shows multiple cysts in both parotid glands, and he has cervical lymphadenopathy. He has no dry eyes or mouth and has never been tested for sexually transmitted infections. He feels otherwise well and has no history of transfusion or immunosuppression. What is the most appropriate next step?",
        "choices": [
            "Sialendoscopy with ductal dilation",
            "HIV testing",
            "Bilateral superficial parotidectomy",
            "Low-dose radiation to both parotids"
        ],
        "answer": 1,
        "explanation": "Benign lymphoepithelial cysts occur in about 1 to 10% of HIV patients, can be the first sign of infection and are bilateral in about 80%. They are rare in HIV-negative people, so finding them should prompt HIV testing. Management favors antiretroviral therapy, observation, serial aspiration or sclerotherapy rather than routine parotidectomy. Low-dose radiation is an option only after diagnosis. Rapid growth calls for FNA to exclude lymphoma.",
        "why_wrong": [
            "Sialendoscopy does not address the likely underlying HIV infection.",
            "Correct.",
            "Routine parotidectomy is avoided for benign lymphoepithelial cysts.",
            "Radiation is a management option only after the diagnosis is established."
        ],
        "board_pearl": "Bilateral cystic parotid enlargement: test for HIV; avoid routine parotidectomy.",
        "curveball": "How does diffuse infiltrative lymphocytosis syndrome differ from Sjogren syndrome?",
        "curveball_answer": "DILS shows circulating CD8 lymphocytosis and involves organs outside the glands, such as lung, GI tract and kidney. It lacks SSA and SSB antibodies, unlike Sjogren syndrome. Management options include observation, aspiration, antiretroviral therapy, sclerotherapy or low-dose radiation.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Immunodeficiency-Associated Chronic Rhinosinusitis",
        "concept_id": "v6-rhinology-allergy-skull-base-immunodeficiency-associated-chronic-rhinosinusitis",
        "stem": "A 6-year-old boy has had recurrent cervical lymph node abscesses and liver abscesses, and now has invasive Aspergillus sinusitis. Sweat chloride and serum immunoglobulin levels are normal. Cultures have grown Staphylococcus aureus and Serratia. His older brother had similar infections, and no other family members are affected. Which test is most likely to confirm the diagnosis?",
        "choices": [
            "IgG subclass levels",
            "Repeat sweat chloride testing",
            "Dihydrorhodamine neutrophil oxidative burst assay",
            "Serum IgE level"
        ],
        "answer": 2,
        "explanation": "Chronic granulomatous disease impairs phagocyte oxidative killing, causing recurrent abscesses and granulomas from catalase-positive bacteria and fungi. About two thirds of cases are X-linked. It is diagnosed with neutrophil function testing, by dihydrorhodamine or nitroblue tetrazolium assay. Long-term care is directed by immunology and includes interferon gamma, avoidance of live vaccines such as BCG, and stem cell transplant for cure. Job syndrome causes staphylococcal cold abscesses with high IgE.",
        "why_wrong": [
            "IgG subclass deficiency causes sinopulmonary infections, not deep abscesses with fungi.",
            "Normal sweat chloride already makes cystic fibrosis unlikely.",
            "Correct.",
            "High IgE suggests Job syndrome, which lacks this pattern of fungal and liver abscesses."
        ],
        "board_pearl": "Catalase-positive abscesses plus Aspergillus in a boy: CGD, diagnose with DHR.",
        "curveball": "Which vaccine category must be avoided in chronic granulomatous disease?",
        "curveball_answer": "Live vaccines, including BCG, should be avoided. Long-term management by immunology also includes interferon gamma, and stem cell transplant offers cure. About two thirds of CGD cases are X-linked, which fits an affected brother.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Inducible Laryngeal Obstruction / PVFM",
        "concept_id": "v6-laryngology-voice-swallowing-inducible-laryngeal-obstruction-pvfm",
        "stem": "A 45-year-old woman wakes in the PACU after microlaryngoscopy for bilateral vocal fold lesions with inspiratory stridor and distress. Oxygen saturation is 93%. Flexible laryngoscopy shows no hematoma or edema, but the folds adduct paradoxically on inspiration. She had been intubated uneventfully, and extubation was smooth before symptoms began. What is the most appropriate first intervention?",
        "choices": [
            "Reintubation without any trial of other measures",
            "Emergent tracheotomy",
            "Immediate return to the OR for re-exploration",
            "A trial of CPAP or BiPAP"
        ],
        "answer": 3,
        "explanation": "Paradoxical vocal fold adduction can follow airway surgery, especially with preexisting bilateral fold disease, and can cause acute distress needing reintubation. CPAP or BiPAP should be tried first. Breathing through a short 3 to 4 inch straw moves the constriction to the mouth and often breaks the pattern. Flexible laryngoscopy in the PACU rules out a structural cause such as hematoma or edema before attributing distress to PVFM.",
        "why_wrong": [
            "Noninvasive measures should be tried before reintubation when she is oxygenating.",
            "Tracheotomy is excessive for a functional, often rapidly reversible pattern.",
            "Laryngoscopy showed no structural cause needing re-exploration.",
            "Correct."
        ],
        "board_pearl": "Post-procedure PVFM: try CPAP or BiPAP first; a short straw helps break it.",
        "curveball": "What simple bedside device can break the paradoxical pattern, and why does it work?",
        "curveball_answer": "Breathing through a short 3 to 4 inch straw moves the point of constriction to the mouth. That often interrupts the laryngeal pattern without medications. Also confirm with flexible laryngoscopy that no structural cause is present.",
        "learning_stage": "application",
        "focus": "complication"
    },
    {
        "topic": "Infantile Hemangioma / PHACE Syndrome",
        "concept_id": "v6-pediatric-otolaryngology-infantile-hemangioma-phace-syndrome",
        "stem": "A 6-week-old girl has a plaque-like segmental hemangioma covering her chin, jawline and preauricular skin. Over the past week she has developed biphasic stridor and noisy breathing with feeds. She is otherwise well. She has no other cutaneous lesions, and she was born at term with normal weight. What is the most important next step to evaluate her stridor?",
        "choices": [
            "Airway endoscopy to look for subglottic hemangioma",
            "Incisional biopsy of the facial lesion for GLUT-1",
            "Abdominal ultrasound for hepatic hemangiomas",
            "Observation, since most hemangiomas involute by age 4"
        ],
        "answer": 0,
        "explanation": "Segmental hemangiomas in a beard distribution have a high rate of airway involvement, about 60 to 65%, usually supraglottic or subglottic. Subglottic lesions cause biphasic stridor, so this infant needs airway endoscopy. Segmental lesions also carry PHACE risk. Abdominal ultrasound is triggered by five or more cutaneous lesions under current AAP guidance, not by a single segmental lesion. The clinical picture makes biopsy unnecessary.",
        "why_wrong": [
            "Correct.",
            "The diagnosis is clinical, and biopsy does not assess the airway.",
            "Abdominal screening is triggered by five or more cutaneous lesions.",
            "Stridor in a beard-distribution hemangioma is a high-risk feature needing evaluation."
        ],
        "board_pearl": "Beard-distribution hemangioma plus stridor: endoscope for subglottic hemangioma.",
        "curveball": "Before starting propranolol in this segmental hemangioma, which imaging screens for PHACE?",
        "curveball_answer": "Brain MRI and MRA screen for posterior fossa malformations and intracranial arterial anomalies that raise stroke risk. Cardiac evaluation for coarctation and an eye exam complete PHACE screening. Intracranial arterial anomalies in PHACE raise stroke risk and influence propranolol use.",
        "learning_stage": "senior_decision",
        "focus": "pediatrics"
    },
    {
        "topic": "Infantile Hemangioma / PHACE Syndrome",
        "concept_id": "v6-pediatric-otolaryngology-infantile-hemangioma-phace-syndrome",
        "stem": "A newborn has a fully formed, warm, violaceous 4-cm vascular tumor on the cheek present at birth. Over 2 months it does not grow, and a trial of propranolol produces no response. Platelets are normal. Biopsy shows a vascular tumor that is GLUT-1 negative. What is the most likely diagnosis?",
        "choices": [
            "Infantile hemangioma",
            "Congenital hemangioma (RICH or NICH)",
            "Kaposiform hemangioendothelioma",
            "Venous malformation in Maffucci syndrome"
        ],
        "answer": 1,
        "explanation": "Congenital hemangiomas, rapidly involuting (RICH) or noninvoluting (NICH), are fully formed at birth, lack GLUT-1 staining and do not respond to propranolol or other medical therapy. RICH is observed, while NICH may need laser or excision. Infantile hemangiomas are GLUT-1 positive, often absent or only a herald patch at birth, and grow rapidly in the first months. Kaposiform hemangioendothelioma causes Kasabach-Merritt thrombocytopenia.",
        "why_wrong": [
            "Infantile hemangioma is GLUT-1 positive and proliferates after birth.",
            "Correct.",
            "Kaposiform hemangioendothelioma usually causes profound thrombocytopenia.",
            "Maffucci involves multiple venous lesions with enchondromas, not a GLUT-1 negative tumor."
        ],
        "board_pearl": "Fully formed at birth, GLUT-1 negative, propranolol-resistant: RICH or NICH.",
        "curveball": "An infant has a violaceous infiltrative tumor with profound thrombocytopenia. What is it and what is a key agent?",
        "curveball_answer": "Kasabach-Merritt phenomenon points to kaposiform hemangioendothelioma or tufted angioma, not infantile hemangioma. Diagnosis needs incisional biopsy, and extensive lesions need antiangiogenic therapy, with sirolimus now a key agent. Congenital hemangiomas, by contrast, are GLUT-1 negative and unresponsive to propranolol.",
        "learning_stage": "application",
        "focus": "diagnosis"
    },
    {
        "topic": "Inferior Turbinate Hypertrophy",
        "concept_id": "v6-rhinology-allergy-skull-base-inferior-turbinate-hypertrophy",
        "stem": "A 33-year-old man with allergic rhinitis controlled on nasal steroids still has bilateral nasal obstruction from inferior turbinate hypertrophy that shrinks well with decongestant. He wants the most durable surgical result while avoiding atrophic rhinitis. He has no history of nasal surgery, and his septum is straight. Which technique best meets these goals?",
        "choices": [
            "Total inferior turbinectomy",
            "Intramural radiofrequency reduction alone",
            "Submucosal resection of erectile tissue, with or without bone, sparing the medial mucosa",
            "Outfracture alone"
        ],
        "answer": 2,
        "explanation": "Submucosal resection of turbinate erectile tissue, with or without bone, that spares the medial mucosa gives the most durable benefit. Outfracture alone is easy but gives poor long-term results. Intramural cautery or radiofrequency is office-friendly but fades, especially if rhinitis is untreated. Long-term data show microdebrider reduction kept 93% improved at 10 years and outperformed bipolar radiofrequency. Total turbinectomy risks atrophic rhinitis and empty nose syndrome and is reserved for tumor.",
        "why_wrong": [
            "Total turbinectomy risks atrophic rhinitis and empty nose syndrome.",
            "Radiofrequency reduction alone tends to fade over time.",
            "Correct.",
            "Outfracture alone gives poor long-term results."
        ],
        "board_pearl": "Most durable turbinate reduction: submucosal resection sparing medial mucosa.",
        "curveball": "When is total inferior turbinectomy still appropriate?",
        "curveball_answer": "Total turbinectomy is reserved for tumor. For obstruction it is avoided because of atrophic rhinitis and empty nose syndrome. Submucosal resection sparing medial mucosa gives the most durable benefit.",
        "learning_stage": "foundation",
        "focus": "surgery"
    },
    {
        "topic": "Injection Laryngoplasty",
        "concept_id": "v6-laryngology-voice-swallowing-injection-laryngoplasty",
        "stem": "A 56-year-old woman has a left vocal fold paralysis 12 months after thyroidectomy, with no recovery and LEMG showing no reinnervation. Stroboscopy shows a 3-mm glottic gap during phonation with the paralyzed fold at the same vertical level. She wants a durable correction. Her voice is breathy and she tires quickly with conversation. Which approach is most appropriate?",
        "choices": [
            "Intracordal injection into the superficial lamina propria",
            "Carboxymethylcellulose gel injection",
            "Gelatin injection augmentation",
            "Framework medialization thyroplasty"
        ],
        "answer": 3,
        "explanation": "A glottic gap under about 1 mm favors injection, while a gap of 2 to 3 mm or more favors framework surgery. With permanent paralysis and a 3-mm gap, medialization thyroplasty offers durable correction. Gelatin lasts about 4 to 6 weeks and carboxymethylcellulose about 6 to 8 weeks, so both are temporary. Medialization injections go into the paraglottic space lateral to the vocalis; material in Reinke space can persist and may need removal.",
        "why_wrong": [
            "Superficial intracordal placement stiffens the mucosa and does not close a large gap.",
            "Carboxymethylcellulose is a short-lived temporary material.",
            "Gelatin lasts only weeks and suits temporary augmentation.",
            "Correct."
        ],
        "board_pearl": "Glottic gap under 1 mm favors injection; 2 to 3 mm or more favors framework surgery.",
        "curveball": "During awake office injection, why should a superior laryngeal nerve block be avoided?",
        "curveball_answer": "Blocking the superior laryngeal nerve paralyzes the cricothyroid and distorts voice feedback during injection. Topical anesthesia is used instead. Fat and PTFE should be avoided when recovery is likely. Slightly overinject resorbable materials, because resorption is expected.",
        "learning_stage": "senior_decision",
        "focus": "management"
    },
    {
        "topic": "Intracranial Complications of Sinusitis",
        "concept_id": "v6-rhinology-allergy-skull-base-intracranial-complications-of-sinusitis",
        "stem": "A 13-year-old boy with acute frontal sinusitis develops headache, vomiting and a focal seizure. Contrast MRI shows a 3-cm ring-enhancing frontal lobe abscess with mass effect, and CT shows opacified frontal and ethmoid sinuses. Neurosurgery plans stereotactic drainage. He has no neck stiffness on exam, and his blood cultures are pending. What is the best overall plan?",
        "choices": [
            "Neurosurgical drainage with endoscopic sinus drainage under the same anesthetic",
            "IV antibiotics alone, reserving surgery for failure",
            "Sinus surgery only, deferring abscess drainage",
            "Lumbar puncture first to identify the organism"
        ],
        "answer": 0,
        "explanation": "Intracranial abscesses larger than about 2.5 cm or causing significant mass effect generally need surgical drainage together with source sinus surgery. When neurosurgical drainage is planned, sinus drainage should be coordinated under the same anesthetic. Lumbar puncture is contraindicated when mass effect is possible and is usually unnecessary. Antiepileptic coverage is commonly given to children with intracranial abscesses. Steroids are reserved for severe edema or impending herniation.",
        "why_wrong": [
            "Correct.",
            "A 3-cm abscess with mass effect needs drainage, not antibiotics alone.",
            "Sinus drainage alone leaves a large abscess with mass effect untreated.",
            "Lumbar puncture risks herniation with mass effect and is usually unnecessary."
        ],
        "board_pearl": "Brain abscess over 2.5 cm or with mass effect: drain it plus sinuses, same anesthetic.",
        "curveball": "Why can a brain abscess from sinusitis follow an insidious course while the child is on oral antibiotics?",
        "curveball_answer": "The abscess wall matures around day 10. Antibiotics can mask symptoms through a quiet latent phase until expansion raises intracranial pressure. Frontal sinusitis is the main source of epidural, subdural and brain abscesses. Cavernous sinus thrombosis still carries about 30% mortality.",
        "learning_stage": "senior_decision",
        "focus": "management"
    },
    {
        "topic": "Invasive Fungal Rhinosinusitis",
        "concept_id": "v6-rhinology-allergy-skull-base-invasive-fungal-rhinosinusitis",
        "stem": "A 61-year-old man with neutropenia after chemotherapy has fever, unilateral facial pain and a pale, insensate left middle turbinate. Frozen-section biopsy of a single site on the middle turbinate is negative for fungi on H&E staining. Clinical suspicion for acute invasive fungal sinusitis remains high. What is the most appropriate next step?",
        "choices": [
            "Conclude invasive fungal disease is excluded and continue antibacterials",
            "Repeat biopsies at multiple sites with silver or calcofluor-white stains",
            "Obtain serum galactomannan and defer endoscopy for 1 week",
            "Wait for bone erosion on repeat CT before acting"
        ],
        "answer": 1,
        "explanation": "Frozen-section biopsy of the anteroinferior middle turbinate is about 85% sensitive and 100% specific, and multiple sites raise the yield. Silver (GMS) or calcofluor-white stains are needed because H&E and Gram stains can miss fungi with sparse cytoplasm. A negative biopsy does not exclude disease when suspicion is high. Bone erosion on CT is a late finding; periantral fat stranding and nonenhancing mucosa on MRI are earlier signs.",
        "why_wrong": [
            "A single negative frozen section does not exclude disease when suspicion is high.",
            "Correct.",
            "Delaying endoscopy is dangerous in a rapidly progressive, often fatal disease.",
            "Bone erosion appears late, so waiting for it delays treatment."
        ],
        "board_pearl": "Negative frozen section does not exclude invasive fungal sinusitis; rebiopsy with fungal stains.",
        "curveball": "Which MRI finding marks devitalized mucosa in acute invasive fungal sinusitis?",
        "curveball_answer": "The 'black turbinate sign' is nonenhancing, necrotic mucosa on contrast MRI. Loss of contrast enhancement maps devitalized tissue better than CT, where bone erosion appears late. Periantral fat stranding on CT is another early warning, while bone erosion is late.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Jaw Cysts and Odontogenic Tumors",
        "concept_id": "v6-head-neck-oncology-jaw-cysts-and-odontogenic-tumors",
        "stem": "A 22-year-old woman has a painless anterior mandibular swelling. Panoramic radiograph shows a multilocular radiolucency that crosses the midline. Incisional biopsy shows multinucleated giant cells in a fibrovascular stroma. Teeth are vital. Serum calcium is normal, and she has no history of kidney stones or bone pain. Before planning curettage, which test is essential?",
        "choices": [
            "Thyroid function tests",
            "Genetic testing for an autosomal dominant syndrome",
            "Serum calcium and parathyroid hormone",
            "Needle aspiration of the lesion for keratin"
        ],
        "answer": 2,
        "explanation": "Central giant cell granuloma is a multilocular lucency of patients under 30, usually in the mandible, that may cross the midline anteriorly. Its histology is identical to the brown tumor of hyperparathyroidism, so calcium and PTH must be checked in every case. Treatment is usually aggressive curettage, and medical options include intralesional steroids, calcitonin and interferon. Cherubism is a separate autosomal dominant bilateral lesion of young children.",
        "why_wrong": [
            "Brown tumor reflects parathyroid, not thyroid, disease.",
            "Cherubism presents at ages 2 to 5 with bilateral posterior lesions.",
            "Correct.",
            "Keratin aspirates suggest an OKC, but biopsy has already shown giant cells."
        ],
        "board_pearl": "Giant cell jaw lesion: check calcium and PTH to exclude brown tumor.",
        "curveball": "Why should a radiolucent jaw lesion be aspirated before open biopsy?",
        "curveball_answer": "Aspiration excludes an arteriovenous malformation, which can bleed massively. Aspirates also help: straw-colored fluid suggests a dentigerous cyst, keratin an OKC, blood an aneurysmal bone cyst, and nothing a traumatic bone cyst. Test pulp vitality, because only the periapical cyst requires a nonvital tooth.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Juvenile Nasopharyngeal Angiofibroma",
        "concept_id": "v6-rhinology-allergy-skull-base-juvenile-nasopharyngeal-angiofibroma",
        "stem": "A 16-year-old boy underwent endoscopic resection of a juvenile nasopharyngeal angiofibroma. Early postoperative and 6-month MRI show a stable 5-mm enhancing residual at the pterygoid base adjacent to the cavernous ICA. He is asymptomatic. Initial imaging showed a stage II tumor, and residual vascularity was minimal after embolization. What is the most appropriate management?",
        "choices": [
            "Extended open revision to remove the residual",
            "Hormonal therapy with flutamide",
            "Low-dose radiotherapy now",
            "Serial MRI surveillance, treating only if it grows"
        ],
        "answer": 3,
        "explanation": "JNA is thought to persist as residual disease rather than truly recur. Small residuals at the skull base can be watched with serial MRI, because most do not grow and many involute after adolescence. Treatment is reserved for growth, usually endoscopically. Aggressive surgery with major morbidity for small residuals in critical areas is not justified. Low-dose radiation is reserved for unresectable advanced or recurrent disease. Hormonal agents are not routine.",
        "why_wrong": [
            "Morbid surgery for a small stable residual near the ICA is not justified.",
            "Hormonal agents can shrink tumor but are not routine therapy.",
            "Radiation is reserved for unresectable advanced or recurrent disease.",
            "Correct."
        ],
        "board_pearl": "Small stable JNA residual: watch with MRI; treat only growth.",
        "curveball": "When should the first postoperative MRI be obtained, and when can surveillance end?",
        "curveball_answer": "Get an early gadolinium MRI, for example on postoperative day 3, before inflammation confounds it. Continue surveillance at least 3 years; it can usually stop in the early to mid 20s after adolescence. Treat only growth, since many residuals stay stable or regress after adolescence.",
        "learning_stage": "senior_decision",
        "focus": "management"
    },
    {
        "topic": "Juvenile Nasopharyngeal Angiofibroma",
        "concept_id": "v6-rhinology-allergy-skull-base-juvenile-nasopharyngeal-angiofibroma",
        "stem": "A 15-year-old boy with a JNA extending into the pterygopalatine fossa and sphenoid is scheduled for endoscopic resection. Angiography shows supply mainly from distal internal maxillary branches and the ascending pharyngeal artery. The team plans preoperative embolization. He has no intracranial extension, and both carotid systems were studied angiographically. Which plan reflects best practice?",
        "choices": [
            "Embolize within about 24 hours of surgery and still clip the maxillary artery intraoperatively",
            "Embolize 1 week before surgery to allow tumor necrosis",
            "Embolize the vidian and cavernous ICA branches as well",
            "Embolize and then omit maxillary artery control because the feeders are occluded"
        ],
        "answer": 0,
        "explanation": "Embolization is best performed within about 24 hours of surgery, because waiting allows collateral recruitment and revascularization; many centers use a 24 to 48 hour window. Even after embolization, the maxillary artery should be clipped at surgery, because recanalized vessels can bleed heavily. Supply from internal carotid branches such as the vidian and cavernous vessels cannot be embolized and predicts more blood loss and staged surgery.",
        "why_wrong": [
            "Correct.",
            "Delays allow collateral recruitment and revascularization of the tumor.",
            "Internal carotid branch supply cannot be safely embolized.",
            "Recanalized vessels can bleed heavily, so the maxillary artery is still clipped."
        ],
        "board_pearl": "JNA: embolize within 24 hours and still clip the maxillary artery.",
        "curveball": "Why do some surgeons skip embolization for small JNAs?",
        "curveball_answer": "Embolization can blur tumor margins. For small tumors, some surgeons clip the internal maxillary artery early instead. Prior embolization also makes revision cases harder. Even after embolization, the maxillary artery is still clipped at surgery.",
        "learning_stage": "application",
        "focus": "surgery"
    },
    {
        "topic": "Juvenile Recurrent Parotitis",
        "concept_id": "v6-pediatric-otolaryngology-juvenile-recurrent-parotitis",
        "stem": "A 15-year-old boy has had juvenile recurrent parotitis of the right gland since age 4. Despite hydration, sialogogues, massage and two sialendoscopies with steroid irrigation, he continues to have frequent painful episodes, and he has not outgrown it at puberty. Gland surgery is planned. Which operation is generally required?",
        "choices": [
            "Superficial parotidectomy",
            "Total parotidectomy",
            "Stensen duct ligation",
            "Excision of intraparotid lymph nodes only"
        ],
        "answer": 1,
        "explanation": "Juvenile recurrent parotitis usually stops by puberty with conservative care and selected sialendoscopy. In the rare refractory case that needs gland surgery, total rather than superficial parotidectomy is generally required, because leftover deep-lobe tissue keeps getting infected. Sialendoscopy with steroid irrigation leaves about 73% free of further episodes. Duct ligation is reserved for chronic pneumoparotitis. Associations include IgA deficiency, juvenile Sjogren and HIV.",
        "why_wrong": [
            "Retained deep-lobe tissue continues to become infected after superficial parotidectomy.",
            "Correct.",
            "Duct ligation is reserved for chronic pneumoparotitis.",
            "Node excision does not remove the diseased ductal and acinar tissue."
        ],
        "board_pearl": "Refractory JRP needing surgery: total parotidectomy, since residual deep lobe keeps flaring.",
        "curveball": "Which diagnosis should be excluded in a child with recurrent parotid swelling, and how?",
        "curveball_answer": "Juvenile Sjogren syndrome usually presents as recurrent parotid swelling rather than dryness. Check ESR, ANA, RF, anti-SSA and SSB and immunoglobulins, and consider labial or parotid biopsy. JRP itself shows nonpurulent secretions, elevated amylase and sialectasis on imaging.",
        "learning_stage": "senior_decision",
        "focus": "surgery"
    },
    {
        "topic": "Keratosis Obturans",
        "concept_id": "v6-otology-neurotology-keratosis-obturans",
        "stem": "A 25-year-old woman has bilateral ear fullness and hearing loss. Both canals are filled with dense keratin plugs that are painful to remove, requiring several visits. Under the casts the canal skin looks shiny, red and atrophic. After clearance, what is the most appropriate measure to slow reaccumulation between debridements?",
        "choices": [
            "A long course of oral antibiotics",
            "Canal wall down mastoidectomy",
            "Topical agents that slow epithelial turnover or soften keratin, such as steroid drops",
            "No treatment until the next cast forms"
        ],
        "answer": 2,
        "explanation": "Keratosis obturans is usually bilateral and seen in young and middle-aged patients. Removing a long-standing cast can be painful and may need repeated sessions. Between debridements, agents that slow epithelial turnover or soften keratin reduce how fast it builds up. Options include steroid drops, mineral oil, acetic acid rinses, a betamethasone-urea preparation and topical 5-fluorouracil. Under the cast the canal skin looks shiny, red and atrophic.",
        "why_wrong": [
            "Oral antibiotics do not slow keratin accumulation.",
            "Mastoidectomy is not indicated for a canal keratin disorder.",
            "Correct.",
            "Topical therapy between debridements slows reaccumulation."
        ],
        "board_pearl": "Keratosis obturans: serial debridement plus steroid, oil, acetic acid or topical 5-FU.",
        "curveball": "Which topical antimetabolite has been used to slow keratin buildup in refractory keratosis obturans?",
        "curveball_answer": "Topical 5-fluorouracil slows epithelial turnover. It joins steroid drops, mineral oil, acetic acid rinses and betamethasone-urea preparations as options between debridements. Removing a long-standing cast can be painful and may need repeated sessions.",
        "learning_stage": "foundation",
        "focus": "management"
    },
    {
        "topic": "Labyrinthitis / Infections of the Labyrinth",
        "concept_id": "v6-otology-neurotology-labyrinthitis-infections-of-the-labyrinth",
        "stem": "A 2-year-old recovering from pneumococcal meningitis fails her hearing screen before discharge. ABR confirms bilateral profound SNHL. High-resolution temporal bone CT 2 weeks after onset shows normal-appearing cochleae. She is otherwise neurologically intact and tolerating oral feeds. What is the most appropriate next step?",
        "choices": [
            "A 6-month hearing aid trial before considering implantation",
            "Repeat CT in 6 months before any implant discussion",
            "Repeat audiometry in 6 months to allow spontaneous recovery",
            "Heavily T2-weighted MRI and expedited cochlear implant evaluation"
        ],
        "answer": 3,
        "explanation": "Labyrinthine ossification after bacterial meningitis can begin within days to 3 weeks, and up to 70% of children with SNHL show some ossification. Early fibrous obliteration is missed on CT and is seen as loss of fluid signal on heavily T2-weighted MRI. Implant evaluation should be expedited, and bilateral simultaneous implantation may be offered. Pneumococcus causes more SNHL than other organisms. Basal-turn drill-out allows insertion in ossified cochleae.",
        "why_wrong": [
            "Profound loss with ossification risk calls for prompt implant evaluation.",
            "CT misses early fibrous obliteration, and delay risks ossification.",
            "Waiting risks ossification that makes implantation harder.",
            "Correct."
        ],
        "board_pearl": "Postmeningitic deafness: T2 MRI for early obliteration and expedite cochlear implant.",
        "curveball": "Where does postmeningitic ossification begin, and why there?",
        "curveball_answer": "Bacteria reach the cochlea through the cochlear aqueduct, which opens into the basal turn of the scala tympani near the round window. Ossification is most severe there and can keep advancing for years.",
        "learning_stage": "senior_decision",
        "focus": "imaging"
    },
    {
        "topic": "Laryngeal Anatomy",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-anatomy",
        "stem": "A 50-year-old man had his left recurrent laryngeal nerve divided and resected during an esophagectomy. A year later, laryngoscopy shows the left true fold immobile, yet the left false fold still contracts and holds tone during phonation. He is hoarse with a breathy voice, and he aspirates thin liquids occasionally. Which anatomic explanation best accounts for this?",
        "choices": [
            "Superior laryngeal nerve fibers, including the human communicating nerve, reaching the larynx",
            "Ansa cervicalis fibers innervating the false fold",
            "Phrenic nerve fibers supplying the ventricularis",
            "Spontaneous regeneration of the resected recurrent laryngeal nerve"
        ],
        "answer": 0,
        "explanation": "Besides Galen's anastomosis, the human communicating nerve runs from the external branch of the superior laryngeal nerve through the cricothyroid membrane to the internal larynx, possibly the thyroarytenoid. Other SLN-RLN links may carry motor fibers to the TA or LCA, and the ventricularis may receive SLN input. These connections explain residual false-fold contraction or tone after complete RLN transection. The cricothyroid is supplied separately by the external SLN.",
        "why_wrong": [
            "Correct.",
            "The ansa cervicalis supplies strap muscles, not the false fold.",
            "The phrenic nerve does not innervate laryngeal muscles.",
            "A resected nerve segment does not regenerate across a gap to restore tone."
        ],
        "board_pearl": "False-fold tone after RLN transection: SLN-derived fibers such as the human communicating nerve.",
        "curveball": "What does Galen's anastomosis connect, and what does it mainly carry?",
        "curveball_answer": "Galen's anastomosis links the internal SLN to the RLN over the dorsal PCA. It is mainly sensory to pharyngeal mucosa and possibly motor to the PCA. The human communicating nerve and other SLN-RLN links may also carry motor fibers.",
        "learning_stage": "application",
        "focus": "anatomy"
    },
    {
        "topic": "Laryngeal Anatomy",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-anatomy",
        "stem": "During a type I medialization thyroplasty in a 62-year-old woman, the surgeon cuts the cartilage window near the lower border of the thyroid lamina and encounters brisk bleeding from small vessels on the inner surface of the cartilage. She is awake under local anesthesia, and her blood pressure is controlled. Which artery is the most likely source?",
        "choices": [
            "The inferior laryngeal artery",
            "Branches of the cricothyroid artery",
            "The lingual artery",
            "The superior laryngeal artery"
        ],
        "answer": 1,
        "explanation": "The cricothyroid artery runs along the lower thyroid border, and its branches pierce the cricothyroid membrane and climb the inner thyroid lamina, so they can bleed when the window is cut. Standard anatomy texts describe it as a branch of the superior thyroid artery. The superior laryngeal artery enters the thyrohyoid membrane with the internal SLN. The inferior laryngeal artery enters between inferior constrictor fibers posteriorly.",
        "why_wrong": [
            "The inferior laryngeal artery enters posteriorly between constrictor fibers.",
            "Correct.",
            "The lingual artery supplies the tongue and is far from the window.",
            "The superior laryngeal artery enters high, through the thyrohyoid membrane."
        ],
        "board_pearl": "Thyroplasty window bleeding near the lower border: cricothyroid artery branches.",
        "curveball": "Where does the true vocal fold sit relative to the thyroid lamina when planning the window?",
        "curveball_answer": "The true fold lies nearer the lower than the upper border of the thyroid lamina, not at its midpoint. The window is placed accordingly to sit at fold level. The superior laryngeal artery and nerve cross about 1 cm below the superior tubercle.",
        "learning_stage": "application",
        "focus": "surgery"
    },
    {
        "topic": "Laryngeal Electromyography (LEMG)",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "stem": "A 50-year-old woman has a left vocal fold paralysis after thyroidectomy 10 months ago, with an intact nerve documented at surgery. Her surgeon orders LEMG now to decide on permanent medialization. A fellow questions whether the timing was ideal. Her voice remains breathy, and the fold is fixed in the paramedian position. When is prognostic LEMG most valuable after injury?",
        "choices": [
            "Timing does not affect its prognostic value",
            "After 12 months, once recovery is complete",
            "About 2 to 6 months after injury",
            "Within the first week after injury"
        ],
        "answer": 2,
        "explanation": "Prognostic LEMG is most valuable 2 to 6 months after injury. Most patients with unilateral paralysis who will recover motion do so by about 8 months, so LEMG later than that is rarely useful. LEMG predicts non-recovery, shown by absent reinnervation, better than it predicts good recovery. At 10 months, clinical status itself largely answers the question of recovery.",
        "why_wrong": [
            "Its prognostic value depends strongly on timing after injury.",
            "Most recovery occurs by 8 months, so late LEMG adds little.",
            "Correct.",
            "Too early, denervation and reinnervation patterns have not developed."
        ],
        "board_pearl": "Prognostic LEMG: best at 2 to 6 months; predicts non-recovery better than recovery.",
        "curveball": "If LEMG at 3 months shows good motor unit potentials, how much reassurance does that give?",
        "curveball_answer": "Less than a poor result would give, because LEMG predicts non-recovery better than good recovery. Synkinetic or nonfunctional reinnervation can still leave an immobile fold. Plan temporary injection if needed while awaiting motion. Most patients who will recover motion do so by about 8 months.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Laryngeal Fracture / External Laryngeal Trauma",
        "concept_id": "v6-facial-plastics-trauma-laryngeal-fracture-external-laryngeal-trauma",
        "stem": "A 44-year-old man is hoarse with a breathy voice after a difficult extubation following cardiac surgery. Laryngoscopy shows the left fold sitting higher than the right with reduced motion. CT shows a reduced left cricoarytenoid joint space. He was intubated for 3 days, and his neck exam is unremarkable. Which management is most appropriate?",
        "choices": [
            "Push the arytenoid backward with the laryngoscope tip",
            "Arytenoidectomy",
            "Wait 6 months and then perform permanent medialization",
            "Closed reduction under anesthesia, lifting the arytenoid anterosuperiorly with external cricoid counterpressure"
        ],
        "answer": 3,
        "explanation": "Posterior arytenoid dislocation usually follows extubation and leaves the fold higher, while anterior dislocation usually results from the laryngoscope tip during intubation and leaves the fold lower. CT shows a reduced or absent cricoarytenoid joint space, and EMG helps if paralysis is in question. A posterior dislocation is reduced under anesthesia by lifting anterosuperiorly with a straight-blade laryngoscope and external cricoid counterpressure. Anterior dislocations are pushed back.",
        "why_wrong": [
            "Pushing backward reduces an anterior dislocation, not this posterior one.",
            "Arytenoidectomy is destructive and not a treatment for dislocation.",
            "Waiting 6 months applies to unilateral paralysis after trauma, not dislocation.",
            "Correct."
        ],
        "board_pearl": "Posterior arytenoid dislocation: fold high, after extubation; lift anterosuperiorly to reduce.",
        "curveball": "Which direction of dislocation follows intubation with the laryngoscope tip, and how does the fold sit?",
        "curveball_answer": "Anterior dislocation usually results from the laryngoscope tip at intubation and leaves the fold lower. It is reduced by pushing it back with the laryngoscope tip or a balloon. CT shows a reduced or absent cricoarytenoid joint space in either direction.",
        "learning_stage": "application",
        "focus": "management"
    },
    {
        "topic": "Laryngeal Fracture / External Laryngeal Trauma",
        "concept_id": "v6-facial-plastics-trauma-laryngeal-fracture-external-laryngeal-trauma",
        "stem": "A 30-year-old man is hit in the anterior neck by a hockey stick. He is alert, hoarse and has neck tenderness but a stable airway. Flexible laryngoscopy shows a small mucosal hematoma, and CT shows a nondisplaced thyroid cartilage fracture. Which approach to his cervical spine is appropriate?",
        "choices": [
            "CT clearance of the cervical spine",
            "Clinical clearance because he is alert",
            "No spine imaging because the injury is anterior",
            "Plain cervical spine radiographs"
        ],
        "answer": 0,
        "explanation": "Concomitant cervical spine fracture occurs in roughly 10 to 13% of external laryngeal trauma. Any but the most trivial laryngeal injury counts as a distracting injury, so CT clearance of the spine is required, and plain films are insufficient. Hoarseness is the most common presenting feature, at about 85%. About 40% of these injuries can be managed without surgery, and a nondisplaced thyroid fracture does not need open exploration.",
        "why_wrong": [
            "Correct.",
            "The laryngeal injury is a distracting injury that prevents clinical clearance.",
            "Cervical spine fractures occur in roughly 10 to 13% of these patients.",
            "Plain films are insufficient for spine clearance in laryngeal trauma."
        ],
        "board_pearl": "Laryngeal trauma is a distracting injury: clear the cervical spine by CT.",
        "curveball": "Which laryngeal injuries need observation in hospital rather than discharge, even without surgery?",
        "curveball_answer": "Observe for 12 to 24 hours with laryngeal hematoma, generalized edema, or strangulation or attempted hanging, which can swell late. Airway edema can progress hours after a benign first exam. Hoarseness is the most common presenting feature, at about 85%.",
        "learning_stage": "foundation",
        "focus": "workup"
    },
    {
        "topic": "Laryngeal Preservation Decision",
        "concept_id": "v6-head-neck-oncology-laryngeal-preservation-decision",
        "stem": "A 64-year-old man has a T4a N1 glottic SCC with gross thyroid cartilage destruction. Before treatment he aspirates thin liquids and needs a tracheostomy for airway obstruction. He asks whether chemoradiation could save his larynx as effectively as surgery. He has a 50 pack-year smoking history and moderate COPD. Which recommendation is best supported?",
        "choices": [
            "Concurrent cisplatin and radiation, as in RTOG 91-11",
            "Primary total laryngectomy with neck dissection and adjuvant therapy as indicated",
            "Radiation alone with surgery for salvage",
            "Induction chemotherapy followed by radiation in responders"
        ],
        "answer": 1,
        "explanation": "ASCO guidance states that extensive T3 or T4a tumors and poor pretreatment laryngeal function may achieve better survival and quality of life with primary total laryngectomy. RTOG 91-11 largely excluded T4 tumors. In the VA trial, T4, fixed-fold and gross cartilage-invasion tumors fared worse without surgery, and 56% of T4 tumors needed salvage laryngectomy. In MD Anderson's T4 experience, 45% of organ-preservation survivors were tracheostomy-dependent and 23% aspirated.",
        "why_wrong": [
            "RTOG 91-11 largely excluded T4 tumors, so it does not support this choice.",
            "Correct.",
            "Radiation alone has the lowest larynx preservation and poor T4 control.",
            "Induction-based preservation fared poorly for T4 and cartilage-invasive tumors."
        ],
        "board_pearl": "T4a with cartilage destruction or a dysfunctional larynx: favor primary total laryngectomy.",
        "curveball": "In the RTOG 91-11 10-year update, how did larynx preservation and survival compare between arms?",
        "curveball_answer": "Larynx preservation was 82% with concurrent cisplatin, 68% with induction and 64% with RT alone. Overall survival did not significantly differ and trended worse with concurrent therapy, possibly from late non-cancer deaths. GORTEC showed induction TPF improved larynx preservation over PF without survival difference.",
        "learning_stage": "senior_decision",
        "focus": "management"
    },
    {
        "topic": "Laryngeal SCC",
        "concept_id": "v6-head-neck-oncology-laryngeal-scc",
        "stem": "A 70-year-old man presents with progressive stridor from a bulky, previously unstaged transglottic tumor that nearly fills the glottic airway. He is saturating 94% on room air and can lie flat briefly. He needs an airway before staging and definitive treatment planning. CT is not yet available, and no biopsy has been taken. Which approach is preferred?",
        "choices": [
            "Urgent radiation to shrink the tumor",
            "Emergency total laryngectomy",
            "Transoral debulking with cup forceps, microdebrider or CO2 laser",
            "Low tracheostomy near the sternal notch"
        ],
        "answer": 2,
        "explanation": "For an obstructing laryngeal tumor, transoral debulking is preferred to secure the airway and allow staging before definitive therapy. If a tracheostomy is unavoidable, it should be placed high so the later resection preserves trachea. Emergency laryngectomy offers no survival advantage over tracheostomy with planned laryngectomy. Tracheostomy itself does not increase stomal recurrence; subglottic extension does. Imaging should precede biopsy or wait 48 hours to avoid biopsy edema.",
        "why_wrong": [
            "Radiation does not provide a timely airway in an obstructing tumor.",
            "Emergency laryngectomy offers no survival advantage and precludes proper staging.",
            "Correct.",
            "A low tracheostomy wastes trachea needed at later resection; place it high."
        ],
        "board_pearl": "Obstructing laryngeal cancer: transoral debulk first; if trach, place it high.",
        "curveball": "Does a pretreatment tracheostomy raise the risk of stomal recurrence?",
        "curveball_answer": "No. Tracheostomy itself does not increase stomal recurrence; subglottic extension does. A high placement preserves trachea for the later resection. Emergency laryngectomy offers no survival advantage over tracheostomy with planned laryngectomy.",
        "learning_stage": "senior_decision",
        "focus": "management"
    },
    {
        "topic": "Laryngeal SCC",
        "concept_id": "v6-head-neck-oncology-laryngeal-scc",
        "stem": "A 68-year-old man has a bulky, warty, white exophytic mass on the left true fold. Two superficial office biopsies show only hyperkeratosis with bland epithelium and no cytologic atypia. CT shows a pushing border without cartilage invasion or nodes. He is a lifelong smoker, and his voice has worsened over a year. Which next step is most appropriate?",
        "choices": [
            "Reassurance and voice therapy",
            "Systemic cidofovir for papillomatosis",
            "Elective bilateral neck dissection",
            "A deep, generous biopsy under anesthesia"
        ],
        "answer": 3,
        "explanation": "Verrucous carcinoma makes up 1 to 2% of laryngeal cancers. It is an exophytic, well-differentiated keratinizing tumor with pushing rather than infiltrative margins and no cytologic atypia, so superficial biopsies are often read as benign. A deep, generous biopsy is needed. The pure form does not metastasize, so treatment is conservative surgical excision without neck dissection, with 5-year survival about 90%. Reactive nodes can reflect inflammation.",
        "why_wrong": [
            "A bulky warty mass with bland superficial biopsies needs deeper tissue.",
            "Nothing here establishes papillomatosis, and biopsies show no viral papilloma.",
            "Pure verrucous carcinoma does not metastasize, so neck dissection is not indicated.",
            "Correct."
        ],
        "board_pearl": "Verrucous carcinoma: bland superficial biopsy; need a deep biopsy; no neck dissection.",
        "curveball": "When would a verrucous carcinoma behave like conventional SCC and need neck treatment?",
        "curveball_answer": "Verrucous carcinoma does not metastasize unless foci of conventional SCC are present. A hybrid tumor is treated as conventional SCC. Thorough pathologic sampling of the resected specimen is therefore important. Pure verrucous carcinoma has about 90% 5-year survival after conservative excision.",
        "learning_stage": "application",
        "focus": "diagnosis"
    },
    {
        "topic": "Laryngocele",
        "concept_id": "v6-laryngology-voice-swallowing-laryngocele",
        "stem": "A 71-year-old trumpet player has symptomatic bilateral combined laryngoceles causing hoarseness and visible neck bulges with Valsalva. Microlaryngoscopy shows no ventricular tumor. External excision is planned. Both lesions enlarge visibly when he plays, and he has had no infections. Which surgical plan best limits the risk of a serious complication?",
        "choices": [
            "Stage the two sides and confirm sensation on the first side with FEES before the second",
            "Excise both sides at one sitting through a single transthyroid approach",
            "Observe both lesions because they are benign",
            "Treat both sides by needle aspiration"
        ],
        "answer": 0,
        "explanation": "Absolute surgical indications for laryngocele are a symptomatic combined lesion or suspected malignancy. For bilateral combined laryngoceles, some surgeons stage the sides and confirm sensation on the first side with FEES, because injuring both internal SLN branches causes dysphagia and aspiration. Elderly patients tolerate this sensory loss worst. At surgery, staying on the capsule at the thyrohyoid membrane protects the nerve, and the saccule base is excised with a mucosal cuff.",
        "why_wrong": [
            "Correct.",
            "Simultaneous bilateral excision risks bilateral internal SLN injury and aspiration.",
            "Symptomatic combined laryngoceles are an absolute indication for surgery.",
            "Aspiration does not remove the sac or its communication, so it recurs."
        ],
        "board_pearl": "Bilateral laryngoceles: stage them and check sensation with FEES; elderly tolerate SLN loss worst.",
        "curveball": "How does CT during Valsalva distinguish a laryngocele from a saccular cyst?",
        "curveball_answer": "Valsalva fills the sac. Air density means a laryngocele, while mucus soft-tissue density means a saccular cyst. A combined lesion is dumbbell-shaped, narrowing through the thyrohyoid membrane at the SLN foramen. Biopsy is rarely needed, but examine the anterior ventricle if malignancy is suspected.",
        "learning_stage": "senior_decision",
        "focus": "surgery"
    },
    {
        "topic": "Laryngomalacia",
        "concept_id": "v6-pediatric-otolaryngology-laryngomalacia",
        "stem": "A 3-month-old with laryngomalacia has worsening inspiratory stridor, feeding difficulty, failure to thrive and suprasternal retractions. Flexible laryngoscopy shows prolapsing arytenoid mucosa and shortened aryepiglottic folds. Supraglottoplasty is scheduled. She was born at term, and she has no cyanotic episodes or neurologic findings. What should be done at the same anesthetic?",
        "choices": [
            "Planned tracheostomy",
            "Complete airway endoscopy to look for synchronous lesions",
            "Brain MRI to exclude a posterior fossa lesion",
            "Nothing further, since flexible laryngoscopy has already defined the disease"
        ],
        "answer": 1,
        "explanation": "Synchronous airway lesions occur in up to 27% of infants with laryngomalacia. When disease is severe enough for surgery, the whole airway should be examined at the same anesthetic. Collapse patterns include prolapse of redundant arytenoid mucosa, foreshortened aryepiglottic folds and posterior displacement of the epiglottis. Laryngomalacia is not more common in premature infants, which argues against simple cartilage immaturity as the cause.",
        "why_wrong": [
            "Tracheostomy is not planned for straightforward severe laryngomalacia.",
            "Correct.",
            "Brain imaging is not routinely needed without neurologic findings.",
            "Flexible laryngoscopy does not see the subglottis and trachea well."
        ],
        "board_pearl": "Severe laryngomalacia going to surgery: scope the whole airway; synchronous lesions up to 27%.",
        "curveball": "When does laryngomalacia stridor typically peak and resolve?",
        "curveball_answer": "Stridor usually begins within the first 2 weeks, peaks and plateaus around 6 months and resolves in most infants by 18 to 24 months. Late-onset forms include feeding, sleep and exercise-induced laryngomalacia. Synchronous airway lesions occur in up to 27% of surgical cases.",
        "learning_stage": "application",
        "focus": "pediatrics"
    },
    {
        "topic": "Laryngopharyngeal Reflux (LPR)",
        "concept_id": "v6-laryngology-voice-swallowing-laryngopharyngeal-reflux-lpr",
        "stem": "A 48-year-old woman has chronic throat clearing, globus and hoarseness with a Reflux Symptom Index of 22. After 3 months of adherent twice-daily proton pump inhibitor therapy, her symptoms are unchanged. Laryngoscopy still shows posterior commissure hypertrophy. She has no heartburn, and upper endoscopy showed no esophagitis. What is the most appropriate next step?",
        "choices": [
            "Laparoscopic fundoplication",
            "Conclude reflux is excluded and stop all antireflux measures",
            "Multichannel impedance-pH testing",
            "Barium swallow to diagnose laryngopharyngeal reflux"
        ],
        "answer": 2,
        "explanation": "When empiric twice-daily PPI fails, impedance-pH testing is recommended. About 36% of empiric PPI failures still have nonacid laryngopharyngeal reflux, so treatment failure does not exclude reflux. Impedance detects nonacid and gaseous reflux, which pH probes miss. Antireflux surgery is not advised for PPI-unresponsive patients without objective acid or nonacid reflux. Barium swallow and EGD do not diagnose LPR. Laryngeal 'reflux' signs are nonspecific.",
        "why_wrong": [
            "Fundoplication is not advised without objective evidence of reflux.",
            "About a third of PPI failures still have nonacid reflux.",
            "Correct.",
            "Barium swallow and EGD do not diagnose laryngopharyngeal reflux."
        ],
        "board_pearl": "PPI failure does not exclude LPR; get impedance-pH before any surgery.",
        "curveball": "If she improves and wants to stop her PPI, how should it be stopped and why?",
        "curveball_answer": "Taper rather than stop abruptly, because about 25% develop rebound acid hypersecretion. Alginates can help nonacid reflux symptoms. Fundoplication chosen by full-column impedance helps about 80% of selected patients.",
        "learning_stage": "application",
        "focus": "workup"
    },
    {
        "topic": "Laryngotracheal Cleft",
        "concept_id": "v6-pediatric-otolaryngology-laryngotracheal-cleft",
        "stem": "An 8-month-old who had repair of esophageal atresia with distal tracheoesophageal fistula as a newborn still coughs and chokes with thin feeds and has recurrent pneumonias. Bronchoscopy shows an intact fistula repair without recurrence. Swallow study shows laryngeal penetration of thin liquids. What is the most appropriate next step?",
        "choices": [
            "Repeat esophagram only",
            "Fundoplication alone",
            "Gastrostomy and no further airway evaluation",
            "Microlaryngoscopy with palpation of the interarytenoid notch to exclude a laryngeal cleft"
        ],
        "answer": 3,
        "explanation": "Over 6% of children with TEF have a laryngeal cleft, and about three-quarters are missed until aspiration persists after TEF repair. A cleft should therefore be excluded in every TEF patient. Microlaryngoscopy with palpation of the interarytenoid notch is diagnostic; redundant mucosa between the arytenoids should raise suspicion. Strong downward pressure during palpation can create a false cleft. Clefts have associated anomalies in about 56%.",
        "why_wrong": [
            "An esophagram does not reliably show a laryngeal cleft.",
            "Fundoplication helps repair outcomes but does not diagnose a cleft.",
            "Gastrostomy without airway evaluation leaves a likely cleft undiagnosed.",
            "Correct."
        ],
        "board_pearl": "Persistent aspiration after TEF repair: palpate the interarytenoid notch for a cleft.",
        "curveball": "If a type I cleft is found, what conservative and diagnostic steps come before formal repair?",
        "curveball_answer": "Try 4 to 6 months of thickened feeds, positioning and reflux and pulmonary optimization. Interarytenoid injection augmentation of 0.2 to 0.6 mL helps more than 70% temporarily and predicts success of formal repair. Endoscopic repair is the gold standard for definitive closure, with 75 to 100% success.",
        "learning_stage": "application",
        "focus": "pediatrics"
    },
    {
        "topic": "Laryngotracheal Reconstruction",
        "concept_id": "v6-pediatric-otolaryngology-laryngotracheal-reconstruction",
        "stem": "A 6-year-old underwent laryngotracheal reconstruction through a complete laryngofissure, with division of the thyroepiglottic ligament, and was decannulated. Months later she has exercise intolerance and obstructive sleep apnea now requiring CPAP. Awake rigid endoscopy appears unremarkable. Her laryngotracheal airway was widened with an anterior costal cartilage graft. Which evaluation best identifies the likely cause?",
        "choices": [
            "Drug-induced sleep endoscopy to assess epiglottic petiole prolapse",
            "Cine MRI of the airway",
            "Laryngeal electromyography",
            "Repeat awake rigid bronchoscopy"
        ],
        "answer": 0,
        "explanation": "Dividing the thyroepiglottic ligament during a complete laryngofissure can let the epiglottic petiole fall back, causing exercise intolerance and obstructive sleep apnea, often with CPAP dependence. It is best judged by polysomnography or drug-induced sleep endoscopy, while rigid endoscopy and cine MRI are unreliable. Repair pexies the petiole to the thyroid cartilage through a laryngofissure with a high suprastomal stent. Prophylactic pexy sutures are advised whenever a full laryngofissure is done.",
        "why_wrong": [
            "Correct.",
            "Cine MRI is unreliable for assessing petiole prolapse.",
            "LEMG assesses innervation, not dynamic petiole prolapse.",
            "Rigid endoscopy is unreliable and already appeared normal."
        ],
        "board_pearl": "OSA after full laryngofissure: suspect petiole prolapse; evaluate with DISE or PSG.",
        "curveball": "How can petiole prolapse be prevented during laryngotracheal reconstruction?",
        "curveball_answer": "Place prophylactic pexy sutures securing the petiole to the thyroid cartilage whenever a full laryngofissure is performed. Established prolapse is repaired by pexy with a high suprastomal stent for at least 6 weeks. Repair and prevention both rely on securing the petiole to the thyroid cartilage.",
        "learning_stage": "senior_decision",
        "focus": "complication"
    }
]
