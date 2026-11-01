# labs_v532/sinus_ct.py — Sinus CT & Pre-FESS Planning. Every image verified via WebFetch on 2026-10-31.
LAB = {
    "slug": "sinus-ct",
    "title": "Sinus CT & Pre-FESS Planning Lab",
    "icon": "🧭",
    "subtitle": "Read the coronal CT like the operating surgeon: CLOSE checklist first, then the drainage pathways, then the disease pattern.",
    "framework": [
        "C — Cribriform plate: Keros depth of the olfactory fossa, lateral lamella asymmetry, skull-base slope",
        "L — Lamina papyracea: dehiscence, orbital fat herniation, medialized orbit",
        "O — Onodi (sphenoethmoidal) cell: optic nerve (and carotid) relationship",
        "S — Sphenoid sinus: pneumatization pattern, intersinus septum insertion on the ICA, ICA/optic canal dehiscence, pneumatized anterior clinoid",
        "E — anterior Ethmoid artery: below the skull base on a mesentery vs. in the skull base",
        "Ostiomeatal complex: uncinate attachment, infundibulum, Haller cell, concha bullosa, septal deviation",
        "Frontal recess: agger nasi, frontal cells (IFAC classification), drainage pathway",
        "Disease pattern: OMC vs sphenoethmoidal recess vs sinonasal polyposis vs isolated sinus; Lund-Mackay score",
        "Density and bone: hyperdense contents, expansion/thinning, focal hyperostosis, erosion",
        "Red flags: orbital or intracranial extension, unilateral disease, mass effect — decide if MRI is needed",
        "Surgical consequence: extent of surgery, navigation, image-guided targets and danger zones",
    ],
    "source_note": "Images are open-access CC BY figures hotlinked from PubMed Central or Wikimedia Commons and credited on each case. Radiopaedia is linked only as a reading resource; its images are not reproduced.",
    "resources": [
        {"name": "O'Brien, Hamelin & Weitzel, Radiology 2016 — the CLOSE pre-FESS CT checklist",
         "url": "https://pubs.rsna.org/doi/10.1148/radiol.2016152230",
         "note": "Structured pre-operative sinus CT review: cribriform plate, lamina papyracea, Onodi cell, sphenoid, ethmoid artery"},
        {"name": "Radiopaedia — Keros classification",
         "url": "https://radiopaedia.org/articles/19069",
         "note": "Olfactory fossa depth (type I 1–3 mm, II 4–7 mm, III 8–16 mm) and why type III raises skull-base injury risk"},
        {"name": "Radiopaedia — International frontal sinus anatomy classification (IFAC)",
         "url": "https://radiopaedia.org/articles/83904",
         "note": "Anterior, posterior and medial frontal recess cells by the 2016 IFAC scheme"},
    ],
}
TARGET_LAB = "sinus-ct"
CASES = [
  {
    "id": "sx_afrs_v532",
    "level": 4,
    "concept_id": "sx:afrs",
    "variant_type": "interpret",
    "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8b26/9586708/8f5b046bc3cd/rjaa564f1.jpg",
    "image_credit": "Almomen A, Al-enzi O, Alshammari R, Molani F, Alshakhs AA, Al Ameer MA, Alarim RA, Alfalah MA, Marhoon JA. J Surg Case Rep. 2022;2022(10):rjaa564 (CC BY 4.0) — Fig. 1",
    "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9586708/",
    "prompt": "Non-contrast sinus CT (axial and coronal) in a 35-year-old man with years of nasal obstruction and new bilateral proptosis. Before you name it: describe the sinus contents (density), what the disease has done to the bony walls, and where it has gone beyond the sinuses.",
    "answer": "Pansinus opacification with expanded, remodeled sinuses whose contents are mixed iso- and hyperdense, with thinned/dehiscent bony walls and extension into both orbits and intracranially (pushing, not invading), producing bilateral proptosis. In a young immunocompetent atopic patient this is allergic fungal rhinosinusitis (AFRS): the hyperdense, heterogeneous contents reflect allergic mucin (heavy metals such as iron and manganese, and calcium salts), and the expansion with bony remodeling reflects slow, expansile pressure rather than tissue invasion.",
    "why": "Boards love the AFRS CT triad — unilateral or asymmetric pansinusitis, heterogeneous hyperdense contents ('double density'), and expansion with bone thinning. For the OR, the dehiscent lamina and skull base mean the orbit and dura may lie directly against the mucin with no bone between.",
    "reason_prompt": "A colleague worries that bone 'destruction' with orbital and intracranial extension means invasive fungal sinusitis or malignancy. What CT and clinical features separate AFRS from acute invasive fungal sinusitis and from a sinonasal malignancy here?",
    "reason_answer": "AFRS remodels and thins bone by slow expansion; the walls bow outward and the dura and periorbita stay intact (the MRI in this case showed no invasion of orbital tissue or brain). Acute invasive fungal sinusitis occurs in immunocompromised patients (neutropenia, DKA), often shows only mild mucosal thickening with early soft-tissue stranding of the periantral fat, and has necrotic, insensate mucosa on endoscopy. Malignancy tends to cause aggressive bony destruction with an enhancing solid mass. MRI is the tie-breaker: AFRS mucin is T1 variable and markedly T2 hypointense (can mimic air), with peripheral mucosal enhancement only.",
    "teach_prompt": "Give a junior the 20-second AFRS CT script.",
    "teach_answer": "Young atopic patient, often one-sided or asymmetric; sinuses packed and expanded; contents bright on soft-tissue window with swirls of higher density; walls thinned or bowed, not chewed. That is AFRS until proven otherwise. Confirm with MRI if the orbit or skull base is involved, then plan complete surgical clearance of mucin and wide marsupialization, followed by steroids.",
    "follow": "Which criteria define AFRS (Bent and Kuhn), and why are dehiscent orbital and skull-base walls not a contraindication to endoscopic surgery?",
    "follow_answer": "Bent–Kuhn major criteria: type I hypersensitivity to fungi, nasal polyposis, characteristic CT findings, eosinophilic mucin without tissue invasion, and positive fungal stain or culture. Endoscopic surgery is still standard because the disease is non-invasive and the dehiscences are from remodeling; the surgeon removes mucin gently off the periorbita and dura without stripping them, and the bone often remodels back after decompression.",
    "mcq": {
      "question": "This 35-year-old man with chronic nasal obstruction and bilateral proptosis has the sinus CT pictured. Which feature most supports allergic fungal rhinosinusitis over acute invasive fungal sinusitis?",
      "choices": [
        "Soft-tissue stranding of the periantral fat with minimal mucosal thickening",
        "Expanded sinuses with heterogeneous hyperdense contents and smoothly thinned, remodeled bone",
        "Air-fluid levels in both maxillary sinuses",
        "Isolated sphenoid opacification with a calcified fungal ball"
      ],
      "answer": 1,
      "explanation": "AFRS fills and expands sinuses with hyperdense allergic mucin and remodels bone by pressure. Periantral fat stranding with minimal mucosal disease in an immunocompromised host suggests acute invasive fungal sinusitis. A single-sinus calcified mass is a fungal ball (mycetoma), not AFRS.",
      "domain": "Rhinology / Allergy / Skull Base",
      "topic": "Allergic fungal rhinosinusitis CT"
    },
    "verify_note": "PMC9586708 (J Surg Case Rep), license on page: Creative Commons Attribution License, CC BY 4.0. Fig. 1 legend: 'CT paranasal sinuses axial (a, b) and coronal (c) show sinus expansion, bony remodeling and dehiscence with intra-orbital and intracranial extension. Bilateral orbital proptosis.' Text: 'The contents of the sinuses show mixed iso and hyperdense material.'"
  },
  {
    "id": "sx_lamina_dehisc_v532",
    "level": 2,
    "concept_id": "sx:lamina_papyracea_dehiscence",
    "variant_type": "interpret",
    "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/a470/11211170/3a2e16d3d573/405_2024_8538_Fig1_HTML.jpg",
    "image_credit": "Deniz MA, Tekinhatun M. Eur Arch Otorhinolaryngol. 2024;281(7):3649-3654 (CC BY 4.0) — Fig. 1",
    "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11211170/",
    "prompt": "Pre-FESS sinus CT, coronal (a) and axial (b), in a 45-year-old man. Run the 'L' of CLOSE: trace the medial orbital wall on both sides from front to back. What is wrong on the side marked by the arrow, and what is sitting where bone should be?",
    "answer": "There is a gap in the left lamina papyracea, with orbital soft tissue (fat ± medial rectus) bulging medially into the ethmoid labyrinth — lamina papyracea dehiscence. In this CT series of 1000 patients it was found in 2%, and 60% of dehiscences had herniated orbital contents (fat in 10, medial rectus in 2 of 20).",
    "why": "The lamina is paper-thin even when intact; a dehiscence means the periorbita, and sometimes the medial rectus, lies directly in the path of the microdebrider during uncinectomy and ethmoidectomy. Orbital injury — hematoma, medial rectus transection, diplopia — is a classic FESS complication, and missing this on the pre-op CT is indefensible.",
    "reason_prompt": "How do you tell a congenital or idiopathic dehiscence from an old healed medial-wall blowout fracture or bone erosion from disease, and does the cause change what you do in the OR?",
    "reason_answer": "A history of facial trauma, a step-off, or a depressed bone fragment with an enlarged orbit suggests an old fracture. Erosion from tumor or mucocele comes with an adjacent mass or expansile lesion. A dehiscence with no history, smooth edges and a small fat bulge is usually a developmental variant. Whatever the cause, the operative rule is the same: mark the side, keep the microdebrider blade facing away from the orbit, palpate the eye during dissection (the press test) to see whether orbital fat moves, and identify the lamina early rather than late.",
    "teach_prompt": "Give a junior the 20-second rule for the 'L' in CLOSE.",
    "teach_answer": "On every coronal slice, follow the medial orbital wall front to back on both sides. If it is broken, bowed into the ethmoids, or has fat poking through, say so and say which side. In the OR, find the lamina early, keep the blade facing medially, and press on the globe while watching the endoscope. If yellow fat appears, stop: do not debride it.",
    "follow": "Intra-operatively you see yellow fat in the ethmoid cavity after an uncinectomy. What do you do immediately and over the next hour?",
    "follow_answer": "Stop powered instrumentation in that area, do not pull or debride the fat, and finish the case with cold instruments away from the breach if safe. Check the eye: pupil, proptosis, globe tension. Avoid tight packing. Watch for a developing orbital hematoma (proptosis, tense globe, rising IOP, vision loss), which needs a lateral canthotomy and cantholysis without delay. Document it and tell the patient; ophthalmology review if there are motility or vision concerns.",
    "mcq": {
      "question": "This 45-year-old man's pre-operative sinus CT is shown, with the arrow on the left medial orbital wall. Which intra-operative maneuver is most specifically indicated by this finding?",
      "choices": [
        "Routine use of a powered microdebrider facing laterally to complete the ethmoidectomy",
        "Pre-operative embolization of the anterior ethmoid artery",
        "Identifying the lamina early and using intermittent globe pressure (press test) while watching the ethmoid wall",
        "Converting to an external Lynch approach"
      ],
      "answer": 2,
      "explanation": "A dehiscent lamina papyracea leaves the periorbita and medial rectus exposed. Identifying the wall early, keeping blades away from it, and pressing on the globe to watch for fat movement reduce the risk of orbital injury. The finding does not require embolization or open surgery.",
      "domain": "Rhinology / Allergy / Skull Base",
      "topic": "Lamina papyracea dehiscence"
    },
    "verify_note": "PMC11211170 (Eur Arch Otorhinolaryngol 2024), license on page: 'This article is licensed under a Creative Commons Attribution 4.0 International License.' Fig. 1 legend: '45-Year-old male patient with left (arrow) lamina papyracea dehiscence on coronal (a) and axial (b) paranasal CT image'. Text: '20 patients (2%) were found to have LPD'; herniated tissue in 12/20 (10 orbital fat, 2 medial rectus)."
  },
  {
    "id": "sx_orbital_abscess_v532",
    "level": 5,
    "concept_id": "sx:orbital_complication_chandler",
    "variant_type": "interpret",
    "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7cc3/7475137/68c20184a229/12348_2020_213_Fig2_HTML.jpg",
    "image_credit": "Abtahi SMB, Eghtedari M, Hosseini S, Shirvani M, Talebi A, Masihpoor N, Mohaghegh S, Hamidianjahromi A, Hosseini M. J Ophthalmic Inflamm Infect. 2020;10:22 (CC BY 4.0) — Fig. 2",
    "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7475137/",
    "prompt": "Orbital CT, coronal (a) and axial (b), in a 19-year-old diabetic with orbital cellulitis and a dental infection. Before staging: where in the orbit is the collection (medial, inferior, superior; against the bone or within the fat?), and what do the maxillary sinus and the retromaxillary tissues show?",
    "answer": "Focus on panel a: a fluid collection sits along the orbital floor (red arrow), i.e. an inferior orbital abscess, not the usual medial one. Panel b shows mild maxillary mucosal thickening and a retromaxillary soft-tissue opacity, pointing to an odontogenic or maxillary source spreading upward. If the collection lies against the bone under elevated periorbita, it is a subperiosteal abscess (Chandler III); if it is within the orbital fat, it is an orbital abscess (Chandler IV).",
    "why": "Most subperiosteal abscesses are medial, from ethmoiditis through the thin lamina papyracea and its valveless veins. A non-medial collection (superior, from the frontal sinus; inferior, from the maxillary sinus or teeth) is less likely to resolve with antibiotics and usually needs a different approach — often external or combined rather than purely endoscopic.",
    "reason_prompt": "Your junior wants to keep this patient on IV antibiotics alone because 'small subperiosteal abscesses in kids settle'. Why does that rule not apply here, and what findings would trigger drainage in any patient?",
    "reason_answer": "Medical treatment of a subperiosteal abscess is reasonable mainly in young children (under about 9) with a small medial abscess, normal vision and no systemic toxicity. This patient is an adult diabetic with a non-medial collection and a dental source — older age, a non-medial site and a likely anaerobic or polymicrobial infection all argue for drainage. Drain in anyone with reduced visual acuity, an afferent pupillary defect, worsening ophthalmoplegia, a large abscess, no improvement after 24–48 hours of IV antibiotics, or a superior or inferior location. In a diabetic, also keep invasive fungal sinusitis on the differential.",
    "teach_prompt": "Give a junior the Chandler classification in 20 seconds.",
    "teach_answer": "Chandler I is preseptal cellulitis, outside the septum. II is orbital cellulitis: fat stranding, no pus. III is subperiosteal abscess: pus between bone and periorbita, lens-shaped against the wall. IV is orbital abscess: pus inside the orbital fat. V is cavernous sinus thrombosis: bilateral signs and cranial nerve palsies. On CT, ask two questions: is there a collection, and is it against the bone or in the fat?",
    "follow": "Which bedside findings do you check and document every few hours while this patient is on IV antibiotics, and which one changes the plan most urgently?",
    "follow_answer": "Visual acuity, color vision (red desaturation), pupils for an afferent pupillary defect, extraocular movements, proptosis, intraocular pressure, and mental status / bilateral signs. A falling acuity or a new afferent pupillary defect means the optic nerve is compromised, and the abscess goes to the OR now (with ophthalmology). Bilateral findings or cranial nerve III/IV/VI palsies mean cavernous sinus thrombosis: get MRI/MRV and involve neurosurgery and infectious disease.",
    "mcq": {
      "question": "This 19-year-old with diabetes and a dental infection has the orbital CT shown (collection along the orbital floor; mild maxillary mucosal thickening). Vision is normal. What is the most appropriate management?",
      "choices": [
        "IV antibiotics and drainage of the collection, with treatment of the dental source",
        "Oral antibiotics and outpatient review in one week",
        "IV antibiotics alone, repeat CT in 7 days",
        "Systemic corticosteroids and observation"
      ],
      "answer": 0,
      "explanation": "An adult with diabetes and a non-medial orbital collection from an odontogenic/maxillary source is unlikely to settle with antibiotics alone. Drain the collection, give IV antibiotics that cover anaerobes, and treat the dental source. Medical therapy alone is reserved mainly for young children with small medial abscesses and normal vision.",
      "domain": "Rhinology / Allergy / Skull Base",
      "topic": "Orbital complications of sinusitis (Chandler)"
    },
    "verify_note": "PMC7475137 (J Ophthalmic Inflamm Infect 2020), license on page: 'This article is licensed under a Creative Commons Attribution 4.0 International License.' Fig. 2 legend: 'A 19 year-old diabetic patient with inferior orbital cellulitis secondary to dental abscess, a Orbital CT scan coronal view revealed inferior orbital abscess (red arrow), b axial view revealed mild mucosal thickening of maxillary sinus (yellow arrow) and retro-maxillary opacity (red arrow)'. Both panels are CT; no clinical photograph."
  },
  {
    "id": "sx_lamina_position_v532",
    "level": 1,
    "concept_id": "sx:normal_coronal_medial_orbital_wall",
    "variant_type": "interpret",
    "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/74a3/9443057/a74c89b0eddf/gr3.jpg",
    "image_credit": "Açar G, Büyükmumcu M, Güler İ. Braz J Otorhinolaryngol. 2019;85(5):551-559 (CC BY 4.0) — Fig. 3",
    "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9443057/",
    "prompt": "Coronal sinus CT through the anterior ethmoid and maxillary sinus, with lines drawn on it. Name, from medial to lateral, the structures you meet going from the nasal septum to the orbit at this level (turbinates, meatus, uncinate region, ethmoid, medial orbital wall). Then: what does the white vertical line through the inferior turbinate attachment tell the surgeon about where the orbit is?",
    "answer": "Septum, middle and inferior turbinates, middle meatus with the uncinate/infundibulum region, ethmoid cells, then the lamina papyracea (medial orbital wall), with the maxillary sinus below the orbit. The vertical line through the attachment of the inferior turbinate is a reference for where the lamina sits: type A is within 2 mm of the line (80.5% of 200 orbits), type B is more than 2 mm medial (16%), and type C is more than 2 mm lateral (3.5%).",
    "why": "A medially placed lamina (type B) lies right behind the uncinate process and is the one most easily entered during uncinectomy and maxillary antrostomy. Checking how far medial the medial orbital wall sits on the coronal CT before surgery is part of the 'L' in CLOSE.",
    "reason_prompt": "Why does a medially positioned lamina (type B) raise orbital-injury risk at the very first step of FESS, while a laterally placed one (type C) raises a different problem?",
    "reason_answer": "The uncinectomy is cut just in front of the lamina. If the lamina bulges medially toward the uncinate, a back-biter or sickle knife aimed laterally can go straight into the orbit. A laterally placed lamina (type C) leaves a wider ethmoid labyrinth, so the risk is incomplete clearance of lateral cells; the authors also link inadequate clearance to lamina penetration. The inferior turbinate attachment is also the lower limit of the middle meatal antrostomy.",
    "teach_prompt": "Give a junior the 20-second coronal orientation script for the anterior ethmoid slice.",
    "teach_answer": "Start at the septum and move outward: middle turbinate, middle meatus, uncinate, infundibulum, bulla, then the lamina papyracea. Drop a vertical line through the inferior turbinate attachment. If the lamina sits medial to that line, the orbit is directly behind your uncinectomy, so cut and bite with the instrument facing medially.",
    "follow": "What is the maxillary line, and how is it used intra-operatively to find the uncinate and protect the orbit?",
    "follow_answer": "The maxillary line is the curvilinear ridge on the lateral nasal wall, running from the middle turbinate axilla to the root of the inferior turbinate, formed by the frontal process of the maxilla over the lacrimal region. The uncinate attaches just behind it, so the incision is placed just posterior to the line. The nasolacrimal duct lies anterior to it, and the lamina sits lateral and posterior to the uncinate.",
    "mcq": {
      "question": "On this pre-operative coronal CT, the lamina papyracea on one side lies more than 2 mm medial to a vertical line through the inferior turbinate attachment. At which step of FESS is the orbit at greatest risk?",
      "choices": [
        "Sphenoidotomy through the sphenoethmoidal recess",
        "Frontal recess dissection with a 70-degree endoscope",
        "Septoplasty",
        "Uncinectomy and middle meatal antrostomy"
      ],
      "answer": 3,
      "explanation": "A medially displaced lamina (type B in this classification) sits directly behind the uncinate process, so the orbit is most exposed at the start of the operation, during uncinectomy and antrostomy. Identify the lamina early and keep instruments facing medially.",
      "domain": "Rhinology / Allergy / Skull Base",
      "topic": "Coronal anatomy: lamina papyracea position"
    },
    "verify_note": "PMC9443057 (Braz J Otorhinolaryngol 2019), license on page: 'This is an open access article under the CC BY license' (CC BY 4.0). Fig. 3 legend: 'Coronal image shows the lamina papyracea variations related with inferior nasal turbinate (white vertical axis) to the lateral nasal wall. Type A ... within 2 mm on either side of the vertical axis; Type B ... medial to axis by >2 mm; Type C ... lateral to axis by >2 mm.' Frequencies 80.5/16/3.5% of 200 orbits from the text."
  },
]
