"""v51.0 surgical anatomy reviews, batch a4 (16 OR cases: airway, laryngology, swallowing).

Each entry: what you meet in operative order, how to find key structures,
what not to injure. Written from standard surgical anatomy references.
"""

CASES = {}

CASES["tracheostomy"] = {
    "title": "Tracheostomy",
    "region": "General ENT / Emergencies",
    "summary": (
        "A surgical tracheostomy creates an airway below the larynx through the anterior wall of the cervical trachea, usually through the second to fourth rings. "
        "Safety depends on staying in the anterior midline (the recurrent laryngeal nerves lie in the tracheoesophageal grooves and the esophagus lies behind the membranous wall), "
        "and on keeping the stoma away from the cricoid above and the innominate artery below."
    ),
    "layers": [
        {"step": "Positioning and surface landmarks", "structures": ["thyroid notch", "cricothyroid membrane", "cricoid arch", "suprasternal notch", "midline of the neck"],
         "note": "A shoulder roll and controlled extension bring the trachea out of the chest. Palpate the cricoid and suprasternal notch and mark the incision about midway between them (roughly 1-2 fingerbreadths above the notch). Extension pulls more trachea, and sometimes the innominate artery, up into the neck, so palpate the notch for a pulsatile vessel."},
        {"step": "Skin, subcutaneous fat and platysma", "structures": ["skin", "subcutaneous fat", "platysma (thin or absent in the midline)", "anterior jugular veins (paired, just off midline, superficial to the strap muscles)"],
         "note": "A horizontal incision gives a better scar; a vertical midline incision is faster in an emergency and in children. The anterior jugular veins run vertically on each side of the midline; retract them laterally or ligate them, and look for a communicating jugular venous arch low in the neck."},
        {"step": "Investing fascia and midline raphe", "structures": ["superficial (investing) layer of deep cervical fascia", "linea alba / midline raphe between the strap muscles", "suprasternal space (of Burns) low in the midline"],
         "note": "Find the avascular white raphe between the sternohyoid muscles and divide it vertically. Staying exactly in the midline keeps you away from the vessels and nerves that lie laterally."},
        {"step": "Strap muscles", "structures": ["sternohyoid (superficial, medial)", "sternothyroid (deep, attaches to the oblique line of the thyroid cartilage)"],
         "note": "Retract both strap layers laterally with equal tension so the trachea stays centered. Palpate the tracheal rings and the cricoid repeatedly; the trachea may be deviated by a goiter, mass or prior surgery."},
        {"step": "Pretracheal fascia and thyroid isthmus", "structures": ["pretracheal (visceral) layer of the middle deep cervical fascia", "thyroid isthmus over rings 2-4", "pyramidal lobe (superior, if present)", "inferior thyroid veins (descend over the trachea below the isthmus)", "thyroidea ima artery (if present)"],
         "note": "Use a cricoid hook to lift and stabilize the airway. Either retract the isthmus superiorly (incising the fascia along its lower edge) or divide it between clamps and suture-ligate each cut edge. The inferior thyroid veins and any thyroidea ima vessel lie on the anterior trachea below the isthmus and must be controlled before the airway is opened."},
        {"step": "Anterior tracheal wall", "structures": ["tracheal rings 2-4 (C-shaped hyaline cartilage)", "annular (intercartilaginous) ligaments", "tracheal mucosa (respiratory epithelium)"],
         "note": "Confirm the level by counting down from the cricoid. Agree with anesthesia on reduced FiO2 and no cautery once the airway is open. Make a window, a Björk (inferiorly based) flap, or a vertical slit without cartilage removal in children. Place stay sutures on each side in children and in any patient in whom a lost tract would be dangerous."},
        {"step": "Lumen and posterior wall", "structures": ["endotracheal tube tip and cuff", "posterior membranous wall (trachealis muscle)", "esophagus directly behind it, slightly to the left"],
         "note": "Have anesthesia withdraw the endotracheal tube under vision until its tip is just above the stoma, but not out of the larynx. Insert the tracheostomy tube along the curve of the trachea; pushing straight back can tear the membranous wall or create a false passage into the pretracheal plane."},
    ],
    "landmarks": [
        {"structure": "Cricoid cartilage", "how_to_find": "The firm complete ring just below the soft cricothyroid membrane and thyroid prominence; it is usually the most prominent ring in children and at about the C6 level in adults. A cricoid hook placed beneath its lower edge lifts the trachea.", "why": "It is the reference for counting rings. Opening the first ring or the cricoid risks perichondritis and subglottic stenosis."},
        {"structure": "Midline raphe", "how_to_find": "The thin, pale, avascular line where the left and right sternohyoid muscles meet; its fibers run vertically and it divides without bleeding", "why": "Following it keeps the dissection off the anterior jugular veins and the lateral neck"},
        {"structure": "Thyroid isthmus", "how_to_find": "A soft, reddish-brown band crossing the upper trachea just below the cricoid, deep to the strap muscles and wrapped in pretracheal fascia; lift its lower edge with a hook to see the rings beneath", "why": "It covers the usual stoma site (rings 2-4) and must be retracted or divided"},
        {"structure": "Tracheal rings 2-4", "how_to_find": "Count down from the lower edge of the cricoid with a finger or hook; rings feel like a regular corrugation under the pretracheal fascia", "why": "This is the target window: low enough to spare the cricoid, high enough to stay away from the innominate artery"},
        {"structure": "Innominate (brachiocephalic) artery", "how_to_find": "Feel for pulsation in the suprasternal notch and low on the anterior trachea before and after extension; it crosses the anterior trachea from left-inferior to right-superior near the thoracic inlet", "why": "A low stoma or a tube tip or cuff resting on it can erode into it"},
        {"structure": "Tracheoesophageal grooves", "how_to_find": "Not exposed in a standard tracheostomy; they are the posterolateral angles of the trachea where it meets the esophagus", "why": "The RLNs run here. Staying anterior and midline protects them."},
    ],
    "danger": [
        {"structure": "Posterior tracheal wall and esophagus", "where": "The membranous wall lies directly behind the lumen; the esophagus is immediately posterior and slightly to the left", "protect": "Open the trachea with a controlled shallow incision, use a hook to lift the anterior wall, and insert the tube following the tracheal curve with the obturator in place", "injury": "Tracheoesophageal fistula, mediastinitis, false passage"},
        {"structure": "Innominate artery", "where": "Crosses the anterior trachea in the lower neck or upper mediastinum, typically around the lower cervical rings; it may ride high into the neck in children, in short necks and with extension", "protect": "Avoid a stoma below the 3rd-4th ring, choose a tube whose curve keeps the tip and cuff off the anterior wall, and avoid cuff overinflation", "injury": "Tracheoinnominate fistula; a sentinel bleed may precede massive hemorrhage"},
        {"structure": "Cricoid cartilage and first ring", "where": "Immediately above the usual window", "protect": "Count rings and open at ring 2 or below; do not let the tube flange or a high incision rest on the cricoid", "injury": "Perichondritis, subglottic stenosis, difficult decannulation"},
        {"structure": "Recurrent laryngeal nerves", "where": "In or near the tracheoesophageal grooves, lateral and posterior to the trachea", "protect": "Do not dissect lateral to the trachea", "injury": "Vocal-fold paralysis; bilateral injury causes airway obstruction above the stoma"},
        {"structure": "Pleural apices", "where": "Rise above the clavicle, higher in children and in patients with emphysema", "protect": "Stay in the midline and do not dissect low and lateral in the root of the neck", "injury": "Pneumothorax"},
        {"structure": "Anterior jugular veins, inferior thyroid veins and thyroid isthmus", "where": "Superficial and anterior to the trachea along the midline", "protect": "Ligate or retract the veins and suture-ligate the divided isthmus", "injury": "Early hemorrhage and hematoma that can compress or obscure the fresh tract"},
    ],
    "variants": [
        "High-riding innominate artery palpable in the suprasternal notch or seen crossing the cervical trachea",
        "Thyroidea ima artery ascending on the anterior trachea from the brachiocephalic trunk or aortic arch in a small minority",
        "Enlarged isthmus or goiter displacing or covering the trachea; tracheal deviation from mass or prior surgery",
        "Low-lying larynx in older patients and deep trachea in obese or short-necked patients, which may need a longer or adjustable-flange tube",
        "In infants the cricoid is high, the trachea is soft and easily compressed, and the pleura and innominate artery sit relatively high",
    ],
    "imaging_check": [
        "Not routinely imaged for a standard elective case: palpate the cricoid, rings and suprasternal notch, check neck extension and the skin-to-trachea depth",
        "CT neck/chest when there is a goiter, mass, prior neck surgery or radiation, or tracheal deviation: trachea position, isthmus size, depth from skin",
        "Look for an innominate artery or other vessel crossing anterior to the cervical trachea on CT when available",
        "Chest radiograph after the procedure: tube position, pneumothorax and pneumomediastinum",
    ],
    "blood_nerve": [
        ["Tracheal blood supply", "Segmental branches enter laterally: inferior thyroid artery branches to the upper trachea, bronchial arteries to the lower trachea"],
        ["Thyroid isthmus", "Branches of the superior and inferior thyroid arteries; occasionally a thyroidea ima artery; inferior thyroid veins drain down to the brachiocephalic veins"],
        ["Superficial veins", "Anterior jugular veins and the jugular venous arch in the suprasternal space"],
        ["Nerves at risk", "RLNs in the tracheoesophageal grooves (motor to all intrinsic laryngeal muscles except cricothyroid)"],
    ],
    "pimp": [
        {"q": "Which tracheal rings does the thyroid isthmus usually cover?", "a": "Roughly the 2nd to 4th rings"},
        {"q": "At what vertebral level is the cricoid cartilage in an adult?", "a": "About C6"},
        {"q": "Why avoid the first ring and cricoid?", "a": "Higher risk of perichondritis and subglottic stenosis; the cricoid is the only complete ring"},
        {"q": "What is the immediate maneuver for a tracheoinnominate fistula bleed?", "a": "Overinflate the cuff; if that fails, pass a finger through the stoma and compress the artery anteriorly against the sternum (Utley maneuver), then go to the OR"},
        {"q": "Where does a thyroidea ima artery usually arise?", "a": "Brachiocephalic trunk most often; also the aortic arch or right common carotid"},
        {"q": "What is a Björk flap?", "a": "An inferiorly based flap of anterior tracheal wall sutured to the inferior skin edge to guide tube reinsertion"},
        {"q": "Why a vertical tracheal incision without cartilage excision in children?", "a": "Removing cartilage weakens the small, soft trachea and increases stenosis and suprastomal collapse"},
        {"q": "What lies in the suprasternal space of Burns?", "a": "The jugular venous arch, lymph nodes and fat between two layers of investing fascia above the manubrium"},
        {"q": "What lies directly behind the membranous tracheal wall?", "a": "The esophagus, slightly to the left of midline"},
    ],
    "atlas_topics": ["Tracheostomy / Cervical Trachea Anatomy", "Thoracic Inlet / Root of Neck", "Pediatric Laryngotracheal Airway"],
    "sources": [
        ["Cummings Otolaryngology 7e — Tracheotomy chapter", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Airway and tracheotomy", ""],
        ["Myers Operative Otolaryngology — Tracheotomy", ""],
        ["Bailey's Head and Neck Surgery — Otolaryngology — Tracheotomy", ""],
    ],
}

CASES["airway-dilation"] = {
    "title": "Endoscopic Airway Dilation",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Endoscopic dilation treats a narrowed subglottis or cervical trachea from scar (idiopathic, post-intubation, autoimmune) by stretching or radially cutting and then stretching the scar ring. "
        "Safety depends on knowing where the stenosis sits relative to the vocal folds and cricoid, sizing the balloon to the normal adjacent airway, and protecting the thin posterior membranous wall that separates the airway from the esophagus."
    ),
    "layers": [
        {"step": "Oral cavity and suspension", "structures": ["upper incisors and dentition", "tongue base", "vallecula", "epiglottis"],
         "note": "Protect the teeth with a guard and suspend a laryngoscope so the glottis and subglottis are in line. Avoid excessive tongue-base pressure (lingual nerve and tongue injury)."},
        {"step": "Supraglottis and glottis", "structures": ["false folds", "true vocal folds", "anterior commissure", "posterior commissure / interarytenoid area", "arytenoids and cricoarytenoid joints"],
         "note": "Inspect and palpate the arytenoids for mobility. Note any posterior glottic scar, which changes the diagnosis and treatment. The proximal end of the balloon must not sit on the vocal folds or anterior commissure."},
        {"step": "Subglottis", "structures": ["conus elasticus", "inner surface of the cricoid ring", "subglottic mucosa"],
         "note": "The subglottis runs from just below the true folds to the lower edge of the cricoid. It is bounded by the only complete cartilaginous ring, so its caliber cannot expand outward. Idiopathic stenosis usually sits here and in the first tracheal rings."},
        {"step": "Stenotic segment", "structures": ["scar ring or web", "distance from the vocal folds", "craniocaudal length", "residual lumen", "cartilage support (firm vs collapsing)"],
         "note": "Measure with a telescope or a sized endotracheal tube or bougie: distance from the folds, length, grade (Myers-Cotton) and whether the wall is firm scar, soft inflamed tissue or cartilage collapse (malacia does not respond to dilation)."},
        {"step": "Radial incisions (when used)", "structures": ["scar band", "submucosa", "underlying cricoid or tracheal cartilage"],
         "note": "Radial cuts with CO2 laser or cold knife are usually placed at several clock positions through the scar only, not into cartilage. Many surgeons avoid deep posterior cuts because the membranous wall and esophagus lie directly behind."},
        {"step": "Balloon dilation", "structures": ["stenotic ring", "normal trachea above and below", "posterior membranous wall"],
         "note": "Center the balloon across the stenosis with its distal end visible or measured so it does not migrate into a bronchus. Choose a diameter close to the normal adjacent airway for the patient's size, not larger. Watch the tracheal wall and ventilation during the inflation interval."},
        {"step": "Distal airway survey", "structures": ["mid and distal trachea", "carina", "main bronchi"],
         "note": "Inspect after dilation for mucosal tears, bleeding and second stenoses. Look especially at the posterior wall for a tear through the trachealis."},
    ],
    "landmarks": [
        {"structure": "True vocal folds", "how_to_find": "Pale white bands at the glottis, below the ventricles and false folds, meeting at the anterior commissure", "why": "The upper reference point for measuring the stenosis; the balloon must sit below them"},
        {"structure": "Lower border of the cricoid", "how_to_find": "Seen endoscopically as the end of the smooth, ring-shaped subglottic wall before the first corrugated tracheal ring appears", "why": "Separates a subglottic (cricoid) stenosis from a tracheal one; the cricoid cannot be expanded by dilation as much as scar can"},
        {"structure": "Tracheal rings", "how_to_find": "Regular horseshoe-shaped anterior and lateral ridges with a flat posterior membranous wall; count them below the stenosis", "why": "Documents stenosis length and confirms the cartilage is intact"},
        {"structure": "Posterior membranous wall", "how_to_find": "The flat or slightly bulging posterior surface without cartilage ridges, which moves with respiration and coughing", "why": "Thinnest part of the airway and the site of dangerous tears"},
        {"structure": "Carina", "how_to_find": "Sharp midline ridge at the bottom of the trachea where the right and left main bronchi diverge", "why": "Limits distal balloon placement and confirms the full airway survey"},
    ],
    "danger": [
        {"structure": "Posterior membranous trachea and esophagus", "where": "Directly behind the airway lumen; no cartilage support", "protect": "Avoid deep posterior radial cuts, do not oversize the balloon, and inspect the posterior wall after each dilation", "injury": "Tracheal tear, pneumomediastinum, tracheoesophageal fistula, mediastinitis"},
        {"structure": "Vocal folds and anterior commissure", "where": "Immediately above a high subglottic stenosis", "protect": "Place the balloon so its proximal shoulder is below the glottis; avoid laser near the anterior commissure", "injury": "Glottic scar, web, voice change"},
        {"structure": "Cricoid and tracheal cartilage", "where": "Deep to the scar ring", "protect": "Cut through scar only, not into cartilage; avoid excessive dilation pressures", "injury": "Cartilage exposure, chondritis and worse restenosis, or fracture with collapse"},
        {"structure": "Airway (oxygenation and fire)", "where": "Shared field between surgeon and anesthesia during apnea, jet ventilation or tubeless technique", "protect": "Agree on the apnea interval and target saturation; keep FiO2 as low as tolerated with laser and keep flammable material out of the beam path", "injury": "Hypoxia, airway fire"},
        {"structure": "Main bronchi and distal airway", "where": "Below the stenosis", "protect": "Keep the distal balloon tip in view or at a measured depth", "injury": "Bronchial injury or obstruction of ventilation by a migrated balloon"},
    ],
    "variants": [
        "Idiopathic subglottic stenosis: almost always adult women, centered at the cricoid and upper trachea, with a normal glottis",
        "Post-intubation stenosis may extend into the posterior glottis (interarytenoid scar), which dilation alone does not treat",
        "Granulomatosis with polyangiitis: subglottic stenosis with inflamed mucosa that may need medical control",
        "Pediatric congenital subglottic stenosis from a small or elliptical cricoid, and complete tracheal rings, which should not be dilated like scar",
        "Tracheomalacia or A-frame deformity at an old tracheostomy site: cartilage collapse, not scar",
    ],
    "imaging_check": [
        "Prior endoscopy or CT: distance of the stenosis from the vocal folds and from the carina, length, and narrowest diameter",
        "CT neck/chest in suspected long, multilevel or extraluminal (mass, goiter) narrowing",
        "Flow-volume loop pattern (fixed obstruction flattens both limbs) and PFT trend if available",
        "Clinically: vocal-fold mobility on awake laryngoscopy before general anesthesia",
    ],
    "blood_nerve": [
        ["Subglottic and tracheal mucosa", "Inferior thyroid artery branches (cricothyroid branches of the superior thyroid artery anteriorly near the cricoid)"],
        ["Sensory", "Subglottis and trachea: RLN sensory fibers (supraglottis is internal branch of SLN)"],
        ["Motor around the field", "RLN to intrinsic laryngeal muscles; not usually at risk in endoscopic dilation"],
    ],
    "pimp": [
        {"q": "What is the only complete cartilaginous ring of the airway?", "a": "The cricoid"},
        {"q": "Give the Myers-Cotton grades.", "a": "I: 0-50% obstruction; II: 51-70%; III: 71-99%; IV: no detectable lumen"},
        {"q": "What are the boundaries of the subglottis?", "a": "From just below the true vocal folds to the lower border of the cricoid cartilage"},
        {"q": "Which patient population typically has idiopathic subglottic stenosis?", "a": "Adult women"},
        {"q": "What diameter in a full-term neonate defines subglottic stenosis?", "a": "A subglottic lumen under about 4 mm"},
        {"q": "Why is the posterior tracheal wall at particular risk?", "a": "It is membranous (trachealis) with no cartilage and the esophagus lies directly behind it"},
        {"q": "What flow-volume loop pattern does a fixed subglottic stenosis produce?", "a": "Flattening of both the inspiratory and expiratory limbs"},
        {"q": "Which vasculitis classically causes subglottic stenosis?", "a": "Granulomatosis with polyangiitis"},
    ],
    "atlas_topics": ["Pediatric Laryngotracheal Airway", "Tracheostomy / Cervical Trachea Anatomy", "Laryngeal Framework / Intrinsic Muscles"],
    "sources": [
        ["Cummings Otolaryngology 7e — Chronic airway stenosis / subglottic stenosis chapters", ""],
        ["Myer CM, O'Connor DM, Cotton RT. Proposed grading system for subglottic stenosis. Ann Otol Rhinol Laryngol 1994", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Laryngotracheal stenosis", ""],
    ],
}

CASES["medialization"] = {
    "title": "Medialization Thyroplasty",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Medialization (Isshiki type I) thyroplasty treats glottic insufficiency, usually from vocal-fold paralysis, by placing an implant through a window in the thyroid ala to push the paraglottic tissue and vocal fold medially. "
        "Success depends on placing the window at the level of the vocal fold rather than the ventricle or false fold, and keeping the inner perichondrium intact so the implant stays outside the airway."
    ),
    "layers": [
        {"step": "Incision and flaps", "structures": ["skin", "platysma", "anterior jugular veins"],
         "note": "A horizontal incision in a skin crease over the lower half of the thyroid ala gives access to the window. Raise subplatysmal flaps up to the thyroid notch and down to the cricoid."},
        {"step": "Strap muscles", "structures": ["sternohyoid (superficial, split in the midline)", "thyrohyoid (deep, attaches to the oblique line)", "sternothyroid (inserts on the oblique line)"],
         "note": "Separate the sternohyoid in the midline and retract it laterally. Divide or elevate the thyrohyoid and sternothyroid off the lower thyroid ala along the oblique line on the operated side to expose the outer cartilage."},
        {"step": "Outer perichondrium and thyroid ala", "structures": ["outer perichondrium", "thyroid lamina", "thyroid notch", "inferior border of thyroid cartilage", "oblique line"],
         "note": "Incise the outer perichondrium and elevate it to expose the ala. Mark the midline, notch, inferior border and estimated level of the vocal fold. Ossified cartilage in older patients needs a drill instead of a knife or punch."},
        {"step": "Thyroplasty window", "structures": ["anterior strut of cartilage (preserved)", "inferior strut of cartilage (preserved)", "window over the paraglottic space"],
         "note": "Place the window parallel to and about 3-4 mm above the inferior border, with its anterior edge about 5-10 mm behind the midline (the smaller offset in women, the larger in men); typical windows are about 4 x 8 to 5 x 10 mm and vary by implant system. Keep anterior and inferior struts so the ala does not fracture."},
        {"step": "Inner perichondrium", "structures": ["inner perichondrium", "paraglottic space fat"],
         "note": "Elevate the inner perichondrium from the cartilage around the window, often incising it to allow medial displacement. Do not tear through the paraglottic tissues into the ventricle or airway."},
        {"step": "Paraglottic space and implant pocket", "structures": ["thyroarytenoid muscle (vocalis medially)", "lateral cricoarytenoid (posteroinferior)", "ventricle and saccule (superior)", "conus elasticus (inferior)"],
         "note": "The implant pushes the TA medially. Medialize at and slightly below the vocal-fold level; placing it too high bulges the false fold and ventricle. The deepest point is usually posterior along the membranous fold toward the vocal process, but posterior pressure is limited by the arytenoid."},
        {"step": "Endoscopic and voice check, then closure", "structures": ["vocal fold position", "glottic gap", "airway caliber"],
         "note": "Adjust implant size and position with the patient phonating under local anesthesia when possible and with flexible laryngoscopy. Close strap muscles and skin over a drain if needed."},
    ],
    "landmarks": [
        {"structure": "Thyroid notch and midline", "how_to_find": "Palpate the V-shaped superior notch; drop a vertical line from it to the inferior border along the prominence", "why": "All window measurements are taken from this line"},
        {"structure": "Level of the vocal fold", "how_to_find": "Classically taught as about the midpoint of the vertical midline height of the thyroid cartilage (notch to inferior border), running back roughly parallel to the inferior border. Cadaver series vary: one dissection study put the anterior commissure nearer the junction of the upper two-fifths and lower three-fifths, and in many men the fold slopes down posteriorly. Confirm with a needle passed through the cartilage under endoscopic view.", "why": "The window and implant must be at this level; a window placed too high medializes the false fold and ventricle"},
        {"structure": "Inferior border of the thyroid ala", "how_to_find": "The lower free edge of the cartilage just above the cricothyroid membrane and cricothyroid muscle", "why": "The window lies parallel to it and a few millimeters above it"},
        {"structure": "Oblique line", "how_to_find": "A ridge running down and forward on the outer ala where the sternothyroid and thyrohyoid attach", "why": "The sternothyroid and thyrohyoid attach here and are released along it to expose the ala for the window"},
        {"structure": "Inner perichondrium", "how_to_find": "A smooth white membrane seen once cartilage is removed; it separates the cartilage from the yellow paraglottic fat", "why": "Keeping it intact keeps the implant extraluminal"},
    ],
    "danger": [
        {"structure": "Laryngeal mucosa (ventricle and airway)", "where": "Medial to the inner perichondrium and paraglottic tissue; the ventricle lies just above the fold level", "protect": "Elevate the inner perichondrium carefully and do not place the window too high", "injury": "Airway entry, implant exposure, infection and extrusion"},
        {"structure": "Airway", "where": "The glottis narrows with medialization, more so with edema or hematoma", "protect": "Avoid overmedialization, control bleeding, and observe overnight when edema is a concern", "injury": "Stridor or airway obstruction from edema or hematoma"},
        {"structure": "Thyroid ala integrity", "where": "Anterior and inferior struts around the window", "protect": "Preserve struts of a few millimeters and drill ossified cartilage gently", "injury": "Cartilage fracture, unstable implant, change in voice"},
        {"structure": "Branches of the superior thyroid artery (including the cricothyroid artery)", "where": "On the lower ala and across the cricothyroid membrane", "protect": "Cauterize or ligate before making the window", "injury": "Hematoma in the paraglottic space"},
        {"structure": "Pyriform sinus mucosa", "where": "Posterior to the posterior thyroid ala", "protect": "Do not extend the window or pocket posteriorly beyond the ala", "injury": "Pharyngeal fistula, infection"},
    ],
    "variants": [
        "Smaller female larynx: smaller ala, so the window is smaller and sits closer to the midline",
        "Ossified thyroid cartilage in older men: needs a drill and makes the window harder to shape",
        "Vocal-fold height mismatch or a large posterior gap from arytenoid malposition: medialization alone may not close it (consider arytenoid adduction)",
        "Prior radiation or neck surgery: fibrotic paraglottic tissue and higher complication risk",
    ],
    "imaging_check": [
        "Not routinely imaged: confirm the cause of paralysis is evaluated (CT skull base to chest in unexplained paralysis)",
        "Stroboscopy and laryngoscopy: glottic gap pattern, vertical height mismatch, posterior gap and contralateral fold function",
        "Clinically: airway status and contralateral fold mobility before any medialization",
    ],
    "blood_nerve": [
        ["Arterial supply", "Superior thyroid artery (superior laryngeal and cricothyroid branches); inferior thyroid artery (inferior laryngeal branch)"],
        ["Motor", "RLN to all intrinsic muscles except cricothyroid; external branch of SLN to cricothyroid"],
        ["Sensory", "Internal branch of SLN above the folds; RLN below the folds"],
    ],
    "pimp": [
        {"q": "Name the four Isshiki thyroplasty types.", "a": "I medialization, II lateralization, III relaxation (shortening), IV tensioning (lengthening)"},
        {"q": "What is the only abductor of the vocal fold?", "a": "Posterior cricoarytenoid"},
        {"q": "Which intrinsic muscle is not innervated by the RLN?", "a": "Cricothyroid (external branch of the superior laryngeal nerve)"},
        {"q": "Where is the vocal fold relative to the external thyroid cartilage?", "a": "Classically at about the midpoint of the vertical midline height, running back roughly parallel to the inferior border (individual variation is large, so confirm endoscopically)"},
        {"q": "Why preserve the inner perichondrium?", "a": "It keeps the implant out of the airway and lowers extrusion and infection risk"},
        {"q": "Why might a large posterior glottic gap persist after medialization?", "a": "The implant medializes the membranous fold but does not rotate the arytenoid or correct vocal process position or height"},
        {"q": "What attaches to the oblique line of the thyroid cartilage?", "a": "Sternothyroid, thyrohyoid and the thyropharyngeal part of the inferior constrictor"},
        {"q": "What is the paraglottic space bounded by?", "a": "Thyroid cartilage laterally, conus elasticus inferomedially, quadrangular membrane superomedially, and pyriform sinus mucosa posteriorly"},
    ],
    "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles", "Laryngeal Neurovascular Anatomy", "Superior Laryngeal Nerve / Cricothyroid Space"],
    "sources": [
        ["Cummings Otolaryngology 7e — Laryngeal framework surgery chapter", ""],
        ["Isshiki N. Phonosurgery: theory and practice (thyroplasty classification)", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Laryngology: vocal-fold paralysis", ""],
    ],
}

CASES["zenker"] = {
    "title": "Endoscopic Zenker Treatment",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "A Zenker diverticulum is a pulsion pseudodiverticulum of mucosa and submucosa herniating through Killian's dehiscence, the posterior weak area between the thyropharyngeus and cricopharyngeus, above a noncompliant cricopharyngeus. "
        "Endoscopic treatment divides the party wall (the septum containing the cricopharyngeus) to make the pouch and esophagus one channel; safety depends on staying in the midline of the septum and stopping before the cut breaches the apex into the retrovisceral space and mediastinum."
    ),
    "layers": [
        {"step": "Oral cavity and hypopharynx exposure", "structures": ["upper incisors", "tongue base", "posterior pharyngeal wall", "postcricoid area", "cervical spine (behind)"],
         "note": "Protect the teeth and extend the neck as far as the spine allows. Pass the diverticuloscope behind the larynx along the posterior pharyngeal wall."},
        {"step": "Two lumens", "structures": ["esophageal lumen (anterior, behind the cricoid)", "diverticulum (posterior, usually blind pouch)", "septum (party wall) between them"],
         "note": "Place one lip of the diverticuloscope in the esophagus (anterior) and the other in the pouch (posterior), so the septum lies horizontally in the scope. The esophagus is the anterior opening; the pouch is posterior and often holds retained food."},
        {"step": "Septum (party wall)", "structures": ["esophageal mucosa (anterior surface)", "cricopharyngeus muscle (horizontal fibers)", "diverticular mucosa (posterior surface)"],
         "note": "The septum contains the cricopharyngeus. Its free edge is the upper border of the muscle. Confirm the septal depth to the pouch floor before cutting."},
        {"step": "Septal division", "structures": ["midline of the septum", "lateral walls of the pouch and esophagus"],
         "note": "Cut exactly in the midline with stapler, CO2 laser or flexible knife, advancing down toward the bottom of the pouch. Lateral deviation enters the parapharyngeal and retrovisceral tissue of the neck."},
        {"step": "Apex of the pouch", "structures": ["diverticular floor", "retrovisceral (retroesophageal) space behind", "upper mediastinum below"],
         "note": "Stop the division a few millimeters above the pouch floor. A stapler leaves a residual spur at its tip because the anvil and staples do not reach the end; traction sutures or laser can reduce it."},
        {"step": "Inspection", "structures": ["divided muscle edges", "common lumen", "remaining spur"],
         "note": "Check for bleeding, gaps in the staple line, mucosal tears and residual muscle bridge."},
    ],
    "landmarks": [
        {"structure": "Esophageal lumen", "how_to_find": "The anterior, collapsible opening directly behind the cricoid; it continues distally and accepts a bougie or nasogastric tube", "why": "Confirms which side of the septum is the true esophagus before cutting"},
        {"structure": "Diverticular pouch", "how_to_find": "The posterior blind opening, often with retained food or secretions, ending in a smooth fundus", "why": "The septum lies between it and the esophagus"},
        {"structure": "Cricopharyngeal bar", "how_to_find": "The firm horizontal muscle at the free edge of the septum, felt as resistance when the scope lips are spread", "why": "This is the muscle the procedure divides"},
        {"structure": "Pouch floor", "how_to_find": "Measure depth from the septal edge with the scope or a ruler; compare with preoperative swallow study", "why": "Sets the safe length of division and predicts whether a stapler will fit (very small pouches are hard to staple)"},
    ],
    "danger": [
        {"structure": "Retrovisceral space and mediastinum", "where": "Behind and below the pouch floor; the retropharyngeal/retrovisceral space continues into the posterior mediastinum", "protect": "Stop above the floor, stay in the midline, test for leak, and keep a low threshold for contrast study", "injury": "Cervical abscess, mediastinitis"},
        {"structure": "Lateral pharyngeal and esophageal wall", "where": "On each side of the septum", "protect": "Keep the septum centered in the scope and the cut in the midline", "injury": "Lateral perforation into the neck; RLN at risk in the tracheoesophageal groove"},
        {"structure": "Teeth and cervical spine", "where": "Fulcrum of the rigid diverticuloscope", "protect": "Use a tooth guard; assess neck extension and mouth opening preoperatively; convert to open or flexible technique if exposure is poor", "injury": "Dental fracture, lip injury, cervical spine injury"},
        {"structure": "Septal vessels", "where": "Small branches from the inferior thyroid artery run in the cricopharyngeus and submucosa", "protect": "Staple or coagulate before cutting; inspect edges", "injury": "Bleeding"},
    ],
    "variants": [
        "Diverticulum most often projects to the left of midline",
        "Killian-Jamieson diverticulum: arises from the anterolateral cervical esophagus below the cricopharyngeus near the RLN entry; not suitable for septal division",
        "Small pouch (under about 2-3 cm): limited room for a stapler, and lower chance of symptom relief with stapling alone",
        "Coexisting cervical osteophytes or limited neck extension that prevents rigid exposure",
    ],
    "imaging_check": [
        "Barium esophagram: pouch size, side, depth, and level relative to the cricopharyngeal bar",
        "Rule out a Killian-Jamieson diverticulum or a mass in the pouch",
        "Clinically: mouth opening, dentition and cervical spine mobility for rigid exposure",
    ],
    "blood_nerve": [
        ["Arterial supply", "Inferior thyroid artery branches to the cricopharyngeus and upper esophagus"],
        ["Motor", "Pharyngeal plexus (vagus) and RLN branches to the cricopharyngeus"],
        ["Sensory", "Vagal branches (pharyngeal plexus, RLN)"],
    ],
    "pimp": [
        {"q": "What are the boundaries of Killian's triangle?", "a": "The oblique thyropharyngeus fibers above and the transverse cricopharyngeus fibers below, posteriorly"},
        {"q": "What layers make up a Zenker diverticulum wall?", "a": "Mucosa and submucosa only (a pseudodiverticulum)"},
        {"q": "Where does a Killian-Jamieson diverticulum arise?", "a": "Anterolateral cervical esophagus below the cricopharyngeus, lateral to the longitudinal esophageal muscle"},
        {"q": "What is Laimer's triangle?", "a": "The area below the cricopharyngeus bounded by the longitudinal esophageal muscle"},
        {"q": "What does the septum (party wall) contain?", "a": "The cricopharyngeus muscle between esophageal and pouch mucosa"},
        {"q": "Why does a stapler leave a residual spur?", "a": "The anvil tip extends beyond the last staples, so the distal septum is not divided"},
        {"q": "Which side does a Zenker usually project?", "a": "Left"},
        {"q": "Which nerve supplies the cricopharyngeus?", "a": "Vagal fibers via the pharyngeal plexus and RLN"},
    ],
    "atlas_topics": ["Pharynx / UES / Cervical Esophagus", "Pharyngeal Constrictors / Superior Laryngeal Neurovascular Relationships", "Mediastinal Continuity of Deep Neck Spaces"],
    "sources": [
        ["Cummings Otolaryngology 7e — Zenker diverticulum / UES disorders chapter", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Esophagus and swallowing", ""],
        ["Myers Operative Otolaryngology — Endoscopic stapling of Zenker diverticulum", ""],
    ],
}

CASES["tep"] = {
    "title": "Tracheoesophageal Puncture",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "After total laryngectomy the trachea ends at a permanent stoma and the pharynx drains into the esophagus with no connection between them. "
        "A tracheoesophageal puncture makes a controlled fistula through the shared party wall so a one-way valve can route lung air into the esophagus, where the pharyngoesophageal segment vibrates as the new voice source. "
        "Safety depends on a midline puncture about 5-10 mm below the stomal mucocutaneous junction and on protecting the posterior esophageal wall from the needle."
    ),
    "layers": [
        {"step": "Stoma survey", "structures": ["mucocutaneous junction of the stoma", "posterior (12 o'clock) tracheal wall", "stomal size and depth", "crusting, granulation, prior TEP tract"],
         "note": "Inspect the stoma before scoping. A small or deep stoma limits prosthesis access; a prior tract or prosthesis must be accounted for before a new puncture. A dislodged prosthesis that cannot be found must be assumed aspirated until bronchoscopy shows otherwise."},
        {"step": "Esophagoscopy", "structures": ["neopharynx", "pharyngoesophageal (PE) segment (cricopharyngeus and lower inferior constrictor remnant)", "upper cervical esophagus behind the stoma"],
         "note": "Pass a rigid esophagoscope (or a flexible scope with transillumination) to the level of the stoma. Rotate the open bevel anteriorly so it tents the party wall forward toward the trachea. The scope's back wall now shields the posterior esophageal wall."},
        {"step": "Party wall", "structures": ["posterior tracheal mucosa", "membranous trachealis", "areolar plane between trachea and esophagus", "esophageal muscularis (circular and longitudinal)", "esophageal mucosa"],
         "note": "Transillumination and palpation through the stoma confirm the site. The party wall is usually several millimeters thick and thicker after radiation or with a flap; a puncture that stops between the layers creates a false submucosal tract."},
        {"step": "Puncture", "structures": ["midline posterior tracheal wall about 5-10 mm below the stomal mucocutaneous junction", "esophageal lumen inside the scope"],
         "note": "Pass the needle straight posteriorly through the midline into the visible lumen of the scope, not angled up or down. Too high or too close to the edge risks tract migration into the stoma and extrusion; too low makes the prosthesis hard to reach and clean."},
        {"step": "Tract dilation and prosthesis", "structures": ["tracheal flange", "esophageal flange", "prosthesis shaft length"],
         "note": "Pass a wire or catheter retrograde or anterograde as the system requires, dilate only to the prosthesis size, and seat the prosthesis so both flanges are fully deployed. The shaft length must match party-wall thickness; too short tents the tissue and leaks around, too long pistons."},
        {"step": "Final check", "structures": ["esophageal flange position", "valve opening", "periprosthetic seal"],
         "note": "Confirm with endoscopy that the esophageal flange is open in the lumen, rotate to check seating, and test for leakage with colored water when awake."},
    ],
    "landmarks": [
        {"structure": "Mucocutaneous junction at 12 o'clock", "how_to_find": "The line where stomal skin meets tracheal mucosa on the posterior wall; measure about 5-10 mm down from it in the midline", "why": "Standard puncture site that keeps the tract away from the stoma edge and accessible for care"},
        {"structure": "Esophageal lumen behind the stoma", "how_to_find": "Light from the scope transilluminates the posterior tracheal wall; pressing on the tracheal side moves the tip of the scope", "why": "Confirms the needle will enter the lumen and not the party-wall plane"},
        {"structure": "Pharyngoesophageal segment", "how_to_find": "The narrowing above the stoma level through which the scope passes, formed by the cricopharyngeus and lower inferior constrictor remnant", "why": "This is the vibrating sound source; spasm here causes poor voice (assessed by the insufflation test)"},
        {"structure": "Midline of the posterior tracheal wall", "how_to_find": "Center of the flat membranous wall between the horseshoe ends of the last tracheal ring", "why": "Lateral punctures move toward the tracheoesophageal groove and are harder to maintain"},
    ],
    "danger": [
        {"structure": "Posterior esophageal wall and prevertebral space", "where": "Directly behind the esophageal lumen, in line with the needle", "protect": "Turn the esophagoscope bevel so its solid back wall lies behind the puncture site; puncture into a visible lumen", "injury": "Through-and-through perforation, retroesophageal cellulitis, mediastinitis"},
        {"structure": "Party-wall plane", "where": "Between the tracheal and esophageal walls", "protect": "Confirm the needle tip is in the esophageal lumen before dilating", "injury": "False passage, abscess, failed prosthesis"},
        {"structure": "Stoma edge", "where": "Above the puncture site", "protect": "Keep about 5-10 mm below the mucocutaneous junction", "injury": "Tract migration into the stoma, prosthesis extrusion, enlarged fistula"},
        {"structure": "Tracheal airway", "where": "Prosthesis and fragments can fall into the trachea", "protect": "Secure the prosthesis safety strap or inserter; account for every component", "injury": "Aspirated prosthesis, distal airway obstruction"},
        {"structure": "Recurrent laryngeal nerve remnants and thyroid", "where": "Laterally in the tracheoesophageal grooves and paratracheal tissue", "protect": "Stay midline", "injury": "Bleeding and difficult tract; nerves are no longer functional for voice after laryngectomy"},
    ],
    "variants": [
        "Thick, fibrotic party wall after radiation or with a pectoralis or free flap pharyngeal reconstruction",
        "Gastric pull-up or jejunal interposition reconstruction changes the tissue behind the stoma; puncture needs individual planning",
        "Small or retracted stoma that limits access",
        "Hypertonic PE segment (pharyngoesophageal spasm) that needs myotomy, plexus neurectomy or botulinum toxin for fluent speech",
    ],
    "imaging_check": [
        "Not routinely imaged: assess stoma size and depth clinically",
        "Insufflation (Taub) test before secondary puncture to predict fluent PE-segment vibration",
        "Videofluoroscopy if insufflation fails: spasm vs stricture of the PE segment",
        "Chest imaging and bronchoscopy if a dislodged prosthesis is unaccounted for",
    ],
    "blood_nerve": [
        ["Arterial supply", "Inferior thyroid artery branches to the upper trachea and cervical esophagus"],
        ["Motor to PE segment", "Pharyngeal plexus (vagus) to the constrictor remnant; this is the target of plexus neurectomy"],
        ["Sensory", "Vagal branches; stoma skin from cervical plexus (transverse cervical nerve)"],
    ],
    "pimp": [
        {"q": "Where is the standard puncture site?", "a": "Midline posterior tracheal wall (12 o'clock) about 5-10 mm below the stomal mucocutaneous junction"},
        {"q": "What is the voice source in TEP speech?", "a": "Vibration of the pharyngoesophageal segment driven by pulmonary air"},
        {"q": "What does the party wall consist of?", "a": "Posterior membranous tracheal wall and anterior esophageal wall"},
        {"q": "What test predicts fluent TE speech before secondary puncture?", "a": "Esophageal insufflation (Taub) test"},
        {"q": "Name three treatments for PE-segment spasm.", "a": "Botulinum toxin injection, pharyngeal constrictor myotomy, pharyngeal plexus neurectomy"},
        {"q": "Who introduced TEP with a voice prosthesis?", "a": "Singer and Blom (1980)"},
        {"q": "Leak through the valve versus around it: what does each suggest?", "a": "Through: valve failure or debris; around: tract enlargement or wrong shaft length"},
        {"q": "What muscle forms most of the PE segment?", "a": "Cricopharyngeus with the lower inferior constrictor"},
    ],
    "atlas_topics": ["Pharynx / UES / Cervical Esophagus", "Tracheostomy / Cervical Trachea Anatomy"],
    "sources": [
        ["Cummings Otolaryngology 7e — Vocal and speech rehabilitation after laryngectomy", ""],
        ["Singer MI, Blom ED. An endoscopic technique for restoration of voice after laryngectomy. Ann Otol Rhinol Laryngol 1980", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Laryngeal cancer and rehabilitation", ""],
    ],
}

CASES["ctr"] = {
    "title": "Cricotracheal Resection",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Cricotracheal resection removes a subglottic stenosis by excising the anterior cricoid arch with the diseased upper trachea, while keeping the posterior cricoid plate, and joining the healthy trachea to the thyroid cartilage and cricoid plate. "
        "The key relationship is that each RLN enters the larynx just behind the cricothyroid joint, so the lateral cuts must pass anterior to those joints; the second is that the trachea's blood supply arrives laterally, so circumferential mobilization must be limited."
    ),
    "layers": [
        {"step": "Incision and flaps", "structures": ["skin", "platysma", "anterior jugular veins", "existing tracheostoma (if present)"],
         "note": "A low collar incision, often including an existing stoma, with subplatysmal flaps up to the hyoid and down to the sternal notch."},
        {"step": "Strap muscles and thyroid isthmus", "structures": ["sternohyoid", "sternothyroid", "thyroid isthmus", "pretracheal fascia"],
         "note": "Separate the straps in the midline and divide the isthmus so each lobe can be retracted laterally off the trachea."},
        {"step": "Anterior larynx and trachea", "structures": ["thyroid cartilage", "cricothyroid membrane", "cricothyroid muscles", "anterior cricoid arch", "upper tracheal rings"],
         "note": "Expose the anterior surface of the airway from the thyroid notch to below the stenosis. Dissect directly on the anterior trachea, where the plane is avascular and can be opened bluntly into the upper mediastinum."},
        {"step": "Lateral cricoid", "structures": ["cricothyroid muscle (detached)", "cricothyroid joint", "inferior cornu of the thyroid cartilage", "RLN entering behind the joint"],
         "note": "Detach the cricothyroid muscles and stay on the cartilage (subperichondrial on the lateral cricoid). Do not dissect behind the cricothyroid joint, where the RLN enters the larynx."},
        {"step": "Tracheal transection and distal airway", "structures": ["tracheal rings below the stenosis", "posterior membranous wall", "esophagus behind", "cross-field ventilation tube"],
         "note": "Divide the trachea at the lower edge of the stenosis and intubate the distal trachea across the field. Separate the membranous trachea from the esophagus only as far as needed."},
        {"step": "Resection of the anterior cricoid and stenosis", "structures": ["anterior and lateral cricoid arch", "posterior cricoid plate (preserved)", "subglottic scar over the plate"],
         "note": "The cut runs obliquely from just below the thyroid cartilage anteriorly to the lower edge of the cricoid plate posteriorly, anterior to the cricothyroid joints. Remove scar from the inner surface of the plate and thin the plate if needed, keeping its posterior perichondrium."},
        {"step": "Anastomosis and closure", "structures": ["distal tracheal ring (shaped with a posterior membranous flap)", "thyroid cartilage", "cricoid plate", "release maneuvers if tense"],
         "note": "The membranous flap of the distal trachea resurfaces the bare cricoid plate. Place posterior sutures first, then lateral and anterior. Use a suprahyoid release if tension remains, then hold the neck flexed."},
    ],
    "landmarks": [
        {"structure": "Cricothyroid joint", "how_to_find": "Follow the inferior border of the thyroid ala posteriorly to the inferior cornu, which articulates with a small facet on the lateral cricoid", "why": "The RLN enters the larynx just posterior to this joint; resection lines stay anterior to it"},
        {"structure": "Lower edge of the stenosis", "how_to_find": "Use endoscopy with a needle passed through the anterior trachea under vision to mark the first normal ring", "why": "Defines the distal transection without leaving scar or removing healthy trachea"},
        {"structure": "Posterior cricoid plate", "how_to_find": "The tall, signet-shaped posterior part of the cricoid, felt behind the airway once the anterior arch is removed", "why": "It is preserved; it carries the cricoarytenoid joints and the posterior cricoarytenoid muscles"},
        {"structure": "Pretracheal plane", "how_to_find": "Finger dissection on the anterior trachea from the neck down into the mediastinum, in front of the rings and behind the innominate artery", "why": "Mobilizes the trachea without disturbing the lateral blood supply"},
        {"structure": "Tracheoesophageal groove", "how_to_find": "Angle between the lateral tracheal wall and the esophagus, seen by rotating the trachea", "why": "Contains the RLN; avoid dissection here beyond the area of resection"},
    ],
    "danger": [
        {"structure": "Recurrent laryngeal nerves", "where": "In the tracheoesophageal grooves, entering the larynx behind the cricothyroid joints", "protect": "Stay subperichondrial on the lateral cricoid, keep resection lines anterior to the joints, and limit lateral tracheal dissection", "injury": "Unilateral or bilateral vocal-fold paralysis; bilateral injury causes airway obstruction"},
        {"structure": "Esophagus", "where": "Directly behind the posterior membranous trachea and cricoid plate", "protect": "Separate the membranous wall carefully and keep a bougie or nasogastric tube in place if helpful", "injury": "Esophageal perforation, tracheoesophageal fistula"},
        {"structure": "Lateral tracheal blood supply", "where": "Segmental vessels enter the trachea laterally", "protect": "Limit circumferential mobilization to about 1-2 cm beyond the cut edges; mobilize anteriorly and posteriorly instead", "injury": "Ischemic anastomosis, dehiscence, restenosis"},
        {"structure": "Anastomosis", "where": "Thyrotracheal and cricotracheal suture line", "protect": "Use release maneuvers instead of tight sutures; keep the neck flexed (chin stitch or brace)", "injury": "Dehiscence, mediastinitis, restenosis"},
        {"structure": "Innominate artery", "where": "Anterior to the lower cervical trachea", "protect": "Stay on the trachea when dissecting into the mediastinum", "injury": "Hemorrhage, late fistula"},
    ],
    "variants": [
        "Stenosis that extends up into the glottis or near the vocal folds may require an extended resection with posterior laryngofissure and grafting",
        "Pediatric partial CTR: the posterior cricoid plate is thin and the margin under the folds is small",
        "Nonrecurrent right inferior laryngeal nerve (aberrant right subclavian artery): enters the larynx from a more horizontal course",
        "Prior tracheostomy or prior resection with scarred planes",
    ],
    "imaging_check": [
        "Endoscopy: distance from the vocal folds to the stenosis, its length, and the distance to the carina",
        "CT neck/chest: stenosis length, cartilage status and relationship to the innominate artery",
        "Vocal-fold mobility exam before surgery (RLN baseline)",
        "Assess and treat active inflammation (e.g., granulomatosis with polyangiitis) before resection",
    ],
    "blood_nerve": [
        ["Tracheal supply", "Segmental lateral vessels from the inferior thyroid artery (upper trachea) and bronchial arteries (lower trachea)"],
        ["Laryngeal supply", "Superior and inferior laryngeal arteries; cricothyroid branch of the superior thyroid artery"],
        ["Motor", "RLN to intrinsic laryngeal muscles; external branch of the SLN to cricothyroid"],
        ["Sensory", "RLN to the subglottis; internal branch of the SLN to the supraglottis"],
    ],
    "pimp": [
        {"q": "Where does the RLN enter the larynx?", "a": "Just posterior to the cricothyroid joint, deep to the inferior constrictor"},
        {"q": "Why is the posterior cricoid plate preserved?", "a": "It supports the cricoarytenoid joints and posterior cricoarytenoid muscles and protects the RLN entry"},
        {"q": "How does the trachea receive its blood supply?", "a": "Segmental vessels entering laterally (inferior thyroid and bronchial arteries)"},
        {"q": "Name two laryngeal release maneuvers.", "a": "Suprahyoid (Montgomery) and infrahyoid (thyrohyoid, Dedo) release"},
        {"q": "Which laryngeal release is associated with more postoperative dysphagia?", "a": "Infrahyoid (thyrohyoid) release"},
        {"q": "How much adult trachea can be resected?", "a": "Roughly up to half with full mobilization and release maneuvers; much less without"},
        {"q": "What is the Grillo stitch?", "a": "A chin-to-chest suture holding the neck flexed to protect the anastomosis"},
        {"q": "What does the distal tracheal membranous flap do in a CTR?", "a": "Resurfaces the denuded posterior cricoid plate"},
    ],
    "atlas_topics": ["Pediatric Laryngotracheal Airway", "Laryngeal Neurovascular Anatomy", "Tracheostomy / Cervical Trachea Anatomy"],
    "sources": [
        ["Cummings Otolaryngology 7e — Laryngotracheal stenosis: open reconstruction", ""],
        ["Grillo HC. Surgery of the Trachea and Bronchi", ""],
        ["Monnier P. Pediatric Airway Surgery (partial cricotracheal resection)", ""],
    ],
}

CASES["tracheal-resection"] = {
    "title": "Tracheal Resection / Anastomosis",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Tracheal resection removes a stenotic or tumor-involved segment of trachea and rejoins the ends end to end. "
        "The trachea's blood supply is segmental and lateral, so the ends are mobilized anteriorly and posteriorly but only minimally around the sides; the RLNs run in the tracheoesophageal grooves and the innominate artery crosses the lower cervical trachea anteriorly."
    ),
    "layers": [
        {"step": "Incision and flaps", "structures": ["skin", "platysma", "existing stoma (included if present)"],
         "note": "Low collar incision, with an upper partial sternotomy reserved for lesions low in the trachea."},
        {"step": "Straps and thyroid", "structures": ["sternohyoid", "sternothyroid", "thyroid isthmus", "pretracheal fascia"],
         "note": "Separate the straps in the midline and divide the isthmus so each lobe can be pushed laterally."},
        {"step": "Anterior tracheal plane", "structures": ["anterior tracheal rings", "innominate artery (anterior, lower)", "pretracheal plane into the mediastinum"],
         "note": "Free the anterior trachea with finger dissection down toward the carina, staying directly on the rings, behind the innominate artery."},
        {"step": "Lesion and level", "structures": ["stenotic or tumor segment", "normal rings above and below", "cricoid above"],
         "note": "Mark the upper and lower limits with needles under bronchoscopy. Encircle the trachea only just below the lesion, staying close to the tracheal wall to spare the RLNs."},
        {"step": "Transection and cross-field ventilation", "structures": ["distal trachea", "membranous wall", "esophagus behind"],
         "note": "Divide the trachea below the lesion, intubate the distal segment across the field, then resect to healthy edges."},
        {"step": "Posterior wall and esophagus", "structures": ["membranous trachea", "esophagus (posterior, slightly left)", "tracheoesophageal grooves with RLNs"],
         "note": "Separate the membranous wall from the esophagus only along the resected segment and a short distance beyond."},
        {"step": "Anastomosis and closure", "structures": ["tracheal ends", "release maneuvers (suprahyoid, hilar)", "neck flexion"],
         "note": "Place posterior then lateral and anterior sutures with the knots outside the lumen. Interpose tissue (e.g., strap muscle or thyroid) between the anastomosis and innominate artery if they touch."},
    ],
    "landmarks": [
        {"structure": "Cricoid", "how_to_find": "The firm complete ring at the top of the trachea, below the cricothyroid membrane", "why": "The upper limit for counting rings and for tension on the proximal end"},
        {"structure": "Innominate artery", "how_to_find": "Pulsation felt on the anterior trachea as the finger enters the upper mediastinum, crossing from left-inferior to right-superior", "why": "Must be kept anterior to the dissection finger and separated from the anastomosis"},
        {"structure": "Tracheoesophageal grooves", "how_to_find": "Rotate the trachea and look at the angle where its side wall meets the esophagus", "why": "RLN location; the dissection should stay on the tracheal wall"},
        {"structure": "Lesion limits", "how_to_find": "Bronchoscopy with transillumination and needles passed through the anterior trachea", "why": "Sets resection length and avoids over-resection"},
        {"structure": "Carina", "how_to_find": "Felt with a finger in the pretracheal plane as the bifurcation at about the level of the sternal angle", "why": "Defines how much distal trachea is available"},
    ],
    "danger": [
        {"structure": "Recurrent laryngeal nerves", "where": "In or near the tracheoesophageal grooves on both sides", "protect": "Dissect directly on the tracheal wall and do not search for the nerves", "injury": "Vocal-fold paralysis, bilateral airway obstruction"},
        {"structure": "Lateral tracheal blood supply", "where": "Segmental vessels entering along the lateral walls", "protect": "Limit circumferential dissection to about 1-2 cm from each cut end", "injury": "Ischemia, dehiscence and restenosis"},
        {"structure": "Innominate artery", "where": "Anterior to the lower cervical trachea", "protect": "Stay on the trachea; interpose tissue if the artery lies on the anastomosis", "injury": "Tracheoinnominate fistula, hemorrhage"},
        {"structure": "Esophagus", "where": "Directly behind the membranous trachea", "protect": "Keep a bougie or tube in it; separate gently", "injury": "Perforation, tracheoesophageal fistula"},
        {"structure": "Anastomotic tension", "where": "Suture line", "protect": "Release maneuvers rather than more resection or tighter knots; neck flexion postoperatively", "injury": "Dehiscence, mediastinitis, restenosis"},
    ],
    "variants": [
        "Nonrecurrent right inferior laryngeal nerve (with aberrant right subclavian artery)",
        "High-riding innominate artery or a bovine arch that brings vessels close to the cervical trachea",
        "Short neck, kyphosis or prior sternotomy limiting cervical exposure",
        "Tumor (adenoid cystic, squamous) with submucosal spread beyond the visible margin",
    ],
    "imaging_check": [
        "CT neck/chest: lesion length, distance from the cricoid and carina, extraluminal extent",
        "Relationship of the innominate artery and aortic arch branches to the planned anastomosis",
        "Bronchoscopy: mucosal margins and airway caliber below the lesion",
        "Vocal-fold mobility exam (RLN baseline)",
    ],
    "blood_nerve": [
        ["Tracheal supply", "Inferior thyroid artery branches (upper), bronchial arteries (lower), plus small contributions from the subclavian, internal thoracic and innominate arteries"],
        ["Motor", "RLNs for intrinsic laryngeal muscles"],
        ["Autonomic", "Vagal and sympathetic tracheal plexus"],
    ],
    "pimp": [
        {"q": "How many tracheal rings and how long is the adult trachea?", "a": "About 16-22 rings (sources vary; about 2 rings per cm) over roughly 10-13 cm, averaging about 11 cm"},
        {"q": "At what level is the carina?", "a": "About the sternal angle (T4-T5)"},
        {"q": "What is the hilar release?", "a": "Division of the inferior pulmonary ligament and pericardial release around the hilum to gain distal tracheal length"},
        {"q": "How far can you dissect circumferentially around each end?", "a": "About 1-2 cm, to preserve lateral blood supply"},
        {"q": "Why put a muscle flap between the anastomosis and innominate artery?", "a": "To reduce the risk of tracheoinnominate fistula"},
        {"q": "Where does the left RLN loop?", "a": "Under the aortic arch, just behind the ligamentum arteriosum"},
        {"q": "Where does the right RLN loop?", "a": "Under the right subclavian artery"},
        {"q": "Which tracheal tumor is known for submucosal and perineural spread?", "a": "Adenoid cystic carcinoma"},
    ],
    "atlas_topics": ["Tracheostomy / Cervical Trachea Anatomy", "Thoracic Inlet / Root of Neck", "Laryngeal Neurovascular Anatomy"],
    "sources": [
        ["Grillo HC. Surgery of the Trachea and Bronchi", ""],
        ["Cummings Otolaryngology 7e — Tracheal stenosis and resection", ""],
        ["Bailey's Head and Neck Surgery — Otolaryngology — Laryngotracheal stenosis", ""],
    ],
}

CASES["injection-laryngoplasty"] = {
    "title": "Injection Laryngoplasty",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Injection laryngoplasty bulks a weak or paralyzed vocal fold by placing material in the paraglottic space, lateral to the thyroarytenoid muscle, so the fold moves medially and the glottic gap closes. "
        "The material must go deep (lateral to TA) and not into the superficial lamina propria, which would stiffen the vibrating cover."
    ),
    "layers": [
        {"step": "Approach choice", "structures": ["peroral (transoral, under GA or awake)", "transcricothyroid membrane", "transthyroid cartilage", "transthyrohyoid membrane"],
         "note": "Choose the route by patient tolerance, cartilage ossification and target. Every route aims for the same space."},
        {"step": "Skin and external landmarks (percutaneous)", "structures": ["thyroid notch", "inferior border of thyroid ala", "cricothyroid membrane", "cricoid arch"],
         "note": "Palpate the thyroid notch, inferior thyroid border and cricoid. The cricothyroid artery crosses the upper membrane, so a low entry is used for the transcricothyroid route."},
        {"step": "Transcricothyroid route", "structures": ["cricothyroid membrane just off midline", "subglottic submucosa", "conus elasticus", "paraglottic space under the fold"],
         "note": "Enter the membrane a few millimeters lateral to midline and angle superiorly and laterally toward the fold. Watch endoscopically for the needle tip bulging under the fold; seeing it in the subglottic lumen means it is too medial."},
        {"step": "Transthyroid route", "structures": ["thyroid lamina at the fold level", "inner perichondrium", "paraglottic space"],
         "note": "Pass through the lower half of the ala at the estimated fold level; this is easier in younger patients with unossified cartilage."},
        {"step": "Transthyrohyoid route", "structures": ["thyrohyoid membrane above the notch", "pre-epiglottic space and petiole region", "laryngeal vestibule", "superior surface of the fold"],
         "note": "Enter in or near the midline above the notch and angle down; the needle enters the endolarynx and then the fold under direct view. Staying near midline avoids the superior laryngeal neurovascular bundle, which pierces the membrane laterally."},
        {"step": "Target: paraglottic space", "structures": ["lateral to the thyroarytenoid muscle", "lateral to the vocal process (posterior target)", "mid-membranous lateral fold (anterior target)"],
         "note": "Most surgeons inject first lateral to the vocal process, then mid-membranous if needed. Medialization is seen as the fold edge moving in and the gap closing."},
        {"step": "Assessment", "structures": ["glottic closure", "fold contour", "airway"],
         "note": "Overinject slightly only with materials that resorb partially; check airway and swallowing before discharge."},
    ],
    "landmarks": [
        {"structure": "Vocal process", "how_to_find": "The white, pointed tip of the arytenoid at the posterior end of the membranous fold, seen with endoscopy", "why": "The posterior injection site is lateral to it"},
        {"structure": "Cricothyroid membrane", "how_to_find": "Soft gap between the inferior thyroid border and the cricoid arch, palpated in the midline", "why": "Entry point for the transcricothyroid approach"},
        {"structure": "Thyroid notch", "how_to_find": "V-shaped notch at the top of the thyroid prominence", "why": "The transthyrohyoid entry is just above it; the fold level is classically about halfway down from it (individual variation; confirm endoscopically)"},
        {"structure": "Superficial lamina propria (Reinke's space)", "how_to_find": "A whitish wheal or blanching of the epithelium during injection signals superficial placement", "why": "Stop and redirect deeper; superficial injection stiffens the cover"},
    ],
    "danger": [
        {"structure": "Superficial lamina propria", "where": "Just under the vibratory epithelium along the free edge", "protect": "Inject lateral to the TA muscle, keep the needle deep and watch for blanching", "injury": "Stiff fold with dysphonia"},
        {"structure": "Airway", "where": "Glottis and subglottis", "protect": "Avoid overmedialization, avoid bilateral injection in a narrow glottis, monitor for edema", "injury": "Airway obstruction"},
        {"structure": "Cricothyroid artery and other laryngeal vessels", "where": "Across the upper cricothyroid membrane; superior laryngeal artery through the thyrohyoid membrane", "protect": "Use a low entry in the membrane; stay near the midline when crossing the thyrohyoid membrane; aspirate before injecting", "injury": "Hematoma; intravascular injection"},
        {"structure": "Superior laryngeal neurovascular bundle", "where": "Pierces the thyrohyoid membrane laterally, below the greater horn of the hyoid", "protect": "Use a midline transthyrohyoid entry", "injury": "Bleeding, supraglottic sensory loss"},
    ],
    "variants": [
        "Ossified thyroid cartilage in older men: transthyroid route difficult",
        "Vocal-fold height mismatch or large posterior gap from arytenoid malposition: injection may not fully correct",
        "Narrow glottis or bilateral impairment: risk of airway compromise",
        "Scar or sulcus where the problem is vibratory stiffness rather than gap",
    ],
    "imaging_check": [
        "Not routinely imaged: confirm the workup of the paralysis cause has been done",
        "Stroboscopy: gap shape, fold height, mucosal wave",
        "Clinically: airway and the contralateral fold's mobility",
    ],
    "blood_nerve": [
        ["Arterial supply", "Superior laryngeal artery (via thyrohyoid membrane), inferior laryngeal artery (with RLN), cricothyroid artery"],
        ["Motor", "RLN to TA, LCA, IA and PCA; external branch of SLN to cricothyroid"],
        ["Sensory", "Internal branch of SLN above the folds; RLN below the folds"],
    ],
    "pimp": [
        {"q": "Name the layers of the vocal fold.", "a": "Epithelium, superficial lamina propria (Reinke's space), intermediate and deep lamina propria (vocal ligament), thyroarytenoid muscle"},
        {"q": "Where should injectate be placed?", "a": "In the paraglottic space lateral to the thyroarytenoid muscle"},
        {"q": "What does the body-cover theory say?", "a": "Cover (epithelium and SLP) vibrates over a stiffer body (vocal ligament and TA)"},
        {"q": "Which material is classically overinjected because it resorbs?", "a": "Autologous fat"},
        {"q": "Which artery crosses the cricothyroid membrane?", "a": "The cricothyroid branch of the superior thyroid artery"},
        {"q": "Through which membrane does the internal branch of the SLN enter the larynx?", "a": "Thyrohyoid membrane, with the superior laryngeal artery"},
        {"q": "Which intrinsic laryngeal muscle receives bilateral innervation?", "a": "Interarytenoid (transverse and oblique arytenoid)"},
    ],
    "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles", "Superior Laryngeal Nerve / Cricothyroid Space", "Laryngeal Neurovascular Anatomy"],
    "sources": [
        ["Cummings Otolaryngology 7e — Injection laryngoplasty / phonosurgery", ""],
        ["Hirano M. Morphological structure of the vocal cord as a vibrator (body-cover concept)", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Vocal-fold paralysis and phonosurgery", ""],
    ],
}

CASES["arytenoid-adduction"] = {
    "title": "Arytenoid Adduction",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Arytenoid adduction rotates a paralyzed arytenoid so its vocal process moves medially and down to the level of the healthy fold, closing a posterior glottic gap that a medialization implant cannot reach. "
        "It works through the muscular process, found behind the posterior thyroid ala deep to the pyriform sinus; safety depends on keeping the pyriform mucosa intact and not overrotating or overtensioning the suture, which narrows the posterior airway."
    ),
    "layers": [
        {"step": "Incision and straps", "structures": ["skin", "platysma", "sternohyoid", "thyrohyoid", "sternothyroid"],
         "note": "A horizontal incision on the paralyzed side over the thyroid ala, often the same incision as a medialization. Retract or divide the straps to see the whole ala to its posterior border."},
        {"step": "Posterior thyroid border", "structures": ["posterior border of the thyroid ala", "inferior constrictor (thyropharyngeus) attached along it", "superior and inferior cornua"],
         "note": "Divide the inferior constrictor along the posterior border and lift the border with a hook, rotating the larynx toward the opposite side. Some surgeons separate the cricothyroid joint to improve exposure; this places the RLN, which lies just behind the joint, at greater risk."},
        {"step": "Pyriform sinus", "structures": ["pyriform sinus mucosa", "posterior thyroid lamina (inner surface)", "posterior cricoid lamina"],
         "note": "Elevate the pyriform sinus mucosa off the inner surface of the posterior ala and the cricoid lamina, pushing it superiorly and posteriorly. It is thin; a tear risks a pharyngeal leak."},
        {"step": "Posterior cricoarytenoid and muscular process", "structures": ["PCA muscle fibers on the posterior cricoid lamina", "muscular process of the arytenoid", "lateral cricoarytenoid (anterior to the process)"],
         "note": "Follow the PCA fibers upward and laterally from the posterior cricoid lamina; they converge onto the muscular process, which is felt as a firm knob on the upper lateral cricoid rim, roughly where a line extended back from the vocal-fold level meets the posterior border of the ala."},
        {"step": "Cricoarytenoid joint", "structures": ["joint capsule", "superolateral facet of the cricoid lamina"],
         "note": "Some surgeons open the joint deliberately to free the arytenoid; others leave it intact. Either way, know that the arytenoid is now mobile and can be overrotated."},
        {"step": "Suture placement and tensioning", "structures": ["muscular process (suture purchase)", "thyroid ala anteriorly (fixation point)", "vocal process position on endoscopy"],
         "note": "Pass a permanent suture through the muscular process and bring it forward through the paraglottic space to the anterior thyroid ala. Depending on technique it is passed through drill holes in the anterior-inferior ala or tied at the anterior edge of a thyroplasty window, so the pull is anterior and somewhat inferior, mimicking the LCA. Tension it gradually while watching the vocal process move medially and inferiorly."},
        {"step": "Closure", "structures": ["constrictor reattachment", "straps", "drain"],
         "note": "Reapproximate the constrictor and straps. Airway edema can increase overnight, so plan observation."},
    ],
    "landmarks": [
        {"structure": "Posterior border of the thyroid ala", "how_to_find": "The smooth vertical edge of the ala between the superior and inferior cornua, palpated behind the oblique line", "why": "The working corridor lies just deep to it"},
        {"structure": "Muscular process", "how_to_find": "Follow PCA fibers superolaterally from the posterior cricoid plate to their insertion; it is a firm knob at roughly the vocal-fold level projected back to the posterior border of the ala, deep to that border and above the cricothyroid joint", "why": "The suture must hold here"},
        {"structure": "Cricothyroid joint", "how_to_find": "Inferior cornu of the thyroid cartilage meeting the lateral cricoid", "why": "RLN entry point is just behind it; stay above it when possible"},
        {"structure": "Pyriform sinus mucosa", "how_to_find": "Thin, smooth, gray-pink membrane lining the inner posterior ala; it lifts away with gentle blunt dissection", "why": "Must be elevated, not entered"},
    ],
    "danger": [
        {"structure": "Pyriform sinus mucosa", "where": "Deep to the posterior thyroid ala, directly over the dissection", "protect": "Elevate bluntly and inspect for tears; repair any tear", "injury": "Pharyngocutaneous fistula, deep neck infection"},
        {"structure": "Airway", "where": "Posterior glottis narrows as the arytenoid is adducted", "protect": "Avoid overtensioning; monitor endoscopically; plan overnight observation", "injury": "Stridor, edema, need for tracheostomy"},
        {"structure": "RLN", "where": "Just behind the cricothyroid joint and in the tracheoesophageal groove", "protect": "Avoid dissecting behind the joint if possible", "injury": "Loss of any remaining nerve function (relevant for reinnervation plans)"},
        {"structure": "Superior laryngeal neurovascular bundle", "where": "Enters the thyrohyoid membrane near the superior cornu", "protect": "Do not extend dissection to the superior cornu", "injury": "Bleeding, supraglottic sensory loss"},
        {"structure": "Arytenoid position", "where": "Vocal process", "protect": "Tension gradually; aim to match the healthy side, not overcorrect", "injury": "Overrotation with the vocal process too low or too medial; poor voice, airway narrowing"},
    ],
    "variants": [
        "Ossified thyroid cartilage making the window and suture passage harder",
        "Fixed cricoarytenoid joint (from trauma or intubation) rather than paralysis: suture will not rotate the arytenoid well",
        "Previous medialization implant that crowds the posterior ala",
        "Vertical height mismatch between the vocal processes, which medialization alone does not correct",
    ],
    "imaging_check": [
        "Stroboscopy: posterior gap and vocal process height",
        "CT larynx if cartilage ossification or framework distortion is suspected",
        "Clinically: confirm paralysis vs joint fixation (palpation or EMG)",
    ],
    "blood_nerve": [
        ["Arterial supply", "Inferior laryngeal artery (from the inferior thyroid artery) near the posterior cricoid; superior laryngeal artery above"],
        ["Motor", "RLN to PCA, LCA, IA and TA"],
        ["Sensory", "Internal branch of SLN above the folds"],
    ],
    "pimp": [
        {"q": "Which muscles attach to the muscular process?", "a": "Posterior cricoarytenoid (posteriorly) and lateral cricoarytenoid (anteriorly)"},
        {"q": "What attaches to the vocal process?", "a": "The vocal ligament"},
        {"q": "Which muscle does the arytenoid adduction suture imitate?", "a": "Lateral cricoarytenoid"},
        {"q": "What is the main motion of the cricoarytenoid joint?", "a": "Rocking (rotation) with some gliding"},
        {"q": "Why do arytenoid adduction instead of thyroplasty alone?", "a": "Large posterior gap or height mismatch that the implant cannot correct"},
        {"q": "Where does the RLN enter the larynx?", "a": "Just behind the cricothyroid joint"},
        {"q": "Which muscle is divided along the posterior thyroid border?", "a": "Inferior constrictor (thyropharyngeus part)"},
    ],
    "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles", "Laryngeal Neurovascular Anatomy", "Pharyngeal Constrictors / Superior Laryngeal Neurovascular Relationships"],
    "sources": [
        ["Isshiki N, Tanabe M, Sawada M. Arytenoid adduction for unilateral vocal cord paralysis. Arch Otolaryngol 1978", ""],
        ["Cummings Otolaryngology 7e — Laryngeal framework surgery", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Phonosurgery", ""],
    ],
}

CASES["cordotomy"] = {
    "title": "Posterior Cordotomy / Arytenoidectomy",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Posterior cordotomy and arytenoidectomy enlarge a glottis narrowed by bilateral vocal-fold immobility by removing tissue from the posterior glottis, the intercartilaginous part often called the respiratory glottis because it contributes much of the airway in quiet breathing. "
        "The key relationship is the vocal process: a cordotomy is cut just in front of it, an arytenoidectomy removes some of the arytenoid itself. Gaining airway trades against voice and aspiration."
    ),
    "layers": [
        {"step": "Exposure", "structures": ["suspension laryngoscope", "vocal folds", "posterior commissure", "interarytenoid area", "arytenoids"],
         "note": "Expose the entire posterior glottis. Palpate both arytenoids to tell paralysis (mobile joint) from posterior glottic stenosis or joint fixation."},
        {"step": "Vocal process and membranous fold", "structures": ["vocal process (posterior end of membranous fold)", "membranous fold", "ventricle", "false fold"],
         "note": "The vocal process divides the anterior membranous glottis from the posterior cartilaginous glottis. Identify it before cutting."},
        {"step": "Cordotomy cut", "structures": ["vocal fold epithelium and lamina propria", "vocal ligament", "thyroarytenoid muscle", "lateral paraglottic tissue toward the thyroid perichondrium"],
         "note": "A transverse cut about 1-2 mm anterior to the vocal process, carried laterally through the vocal ligament and TA muscle toward the thyroid lamina, lets the fold retract forward and opens a C-shaped wedge posteriorly. The Kashima description removes a wedge of roughly 4 mm at the free edge and extends a few millimeters onto the ventricular band; series vary in how far they go. Do not expose the vocal process cartilage."},
        {"step": "Arytenoidectomy (if planned)", "structures": ["arytenoid mucosa", "arytenoid body (medial or total)", "vocal process", "muscular process"],
         "note": "Medial arytenoidectomy removes the medial part of the body; total removes most of the cartilage. Preserve posterior and interarytenoid mucosa to reduce scar."},
        {"step": "Hemostasis", "structures": ["vessels in the TA and lateral paraglottic tissue"],
         "note": "Bleeding comes from small laryngeal vessels within the muscle; use pinpoint coagulation."},
        {"step": "Final inspection", "structures": ["airway lumen", "posterior commissure", "subglottis"],
         "note": "Look for loose tissue and exposed cartilage, and confirm the opposite fold is untouched."},
    ],
    "landmarks": [
        {"structure": "Vocal process", "how_to_find": "The white pointed end of the arytenoid at the posterior edge of the membranous fold; it moves when the arytenoid is palpated", "why": "The cordotomy is cut just in front of it"},
        {"structure": "Posterior commissure", "how_to_find": "Mucosa between the arytenoids at the back of the glottis, above the cricoid plate", "why": "Raw surfaces here scar and close the airway"},
        {"structure": "Arytenoid body", "how_to_find": "Palpated as a firm mobile structure behind the vocal process; the corniculate cartilage sits on its apex", "why": "Target in arytenoidectomy; palpation tests joint mobility"},
        {"structure": "Ventricle", "how_to_find": "The recess between true and false folds; lateral to it is the paraglottic space", "why": "Orients the lateral extent of the cut: the wedge is carried laterally through the TA, under the ventricle floor, and may extend a few millimeters onto the ventricular band"},
    ],
    "danger": [
        {"structure": "Posterior commissure and interarytenoid mucosa", "where": "Behind the operated arytenoid", "protect": "Preserve mucosa and avoid raw surfaces facing each other", "injury": "Posterior glottic scar or web"},
        {"structure": "Vocal process cartilage", "where": "Behind the cordotomy cut", "protect": "Cut anterior to it and keep it covered", "injury": "Granuloma, chondritis"},
        {"structure": "Opposite fold", "where": "Across the glottis", "protect": "Protect with a moist pledget", "injury": "Bilateral injury, web formation"},
        {"structure": "Airway fire", "where": "Endotracheal tube or oxygen near the laser beam", "protect": "Laser-safe tube, saline-filled cuff, low FiO2, wet cottonoids", "injury": "Airway burn"},
        {"structure": "Supraglottic protection", "where": "Arytenoid and aryepiglottic fold", "protect": "Limit the size of resection, especially total arytenoidectomy", "injury": "Aspiration"},
    ],
    "variants": [
        "Bilateral vocal-fold paralysis after thyroidectomy (most common cause) vs posterior glottic stenosis",
        "Cricoarytenoid joint fixation from intubation or rheumatoid arthritis",
        "Partial recovery possible after nerve injury; delay irreversible surgery if within the expected recovery window",
    ],
    "imaging_check": [
        "Not routinely imaged: confirm bilateral immobility on laryngoscopy and palpate joints in the OR",
        "EMG may help predict recovery or show joint fixation",
        "Clinically: aspiration risk and baseline voice",
    ],
    "blood_nerve": [
        ["Arterial supply", "Superior and inferior laryngeal arteries"],
        ["Motor", "RLN (PCA is the only abductor)"],
        ["Sensory", "Internal branch of SLN supraglottic; RLN subglottic"],
    ],
    "pimp": [
        {"q": "What is the Bogdasarian classification?", "a": "Posterior glottic stenosis: I interarytenoid adhesion; II posterior commissure scar; III with unilateral cricoarytenoid fixation; IV bilateral fixation"},
        {"q": "Who described transverse posterior cordotomy?", "a": "Dennis and Kashima (1989)"},
        {"q": "What is the most common cause of bilateral vocal-fold paralysis?", "a": "Thyroid surgery"},
        {"q": "What is the only vocal-fold abductor?", "a": "Posterior cricoarytenoid"},
        {"q": "Why remove posterior tissue to enlarge the airway?", "a": "The posterior (cartilaginous) glottis, the respiratory glottis, contributes a large share of the airway in breathing, while the membranous fold is more important for voice"},
        {"q": "How do you tell paralysis from joint fixation in the OR?", "a": "Palpate the arytenoid; a fixed joint does not move"},
        {"q": "What cartilage sits on the arytenoid apex?", "a": "Corniculate cartilage"},
    ],
    "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles", "Laryngeal Neurovascular Anatomy"],
    "sources": [
        ["Dennis DP, Kashima H. Carbon dioxide laser posterior cordectomy for treatment of bilateral vocal cord paralysis. Ann Otol Rhinol Laryngol 1989", ""],
        ["Bogdasarian RS, Olson NR. Posterior glottic laryngeal stenosis. Otolaryngol Head Neck Surg 1980", ""],
        ["Cummings Otolaryngology 7e — Bilateral vocal-fold paralysis", ""],
    ],
}

CASES["cp-myotomy"] = {
    "title": "Cricopharyngeal Myotomy",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Cricopharyngeal myotomy cuts the cricopharyngeus, the main tonic muscle of the upper esophageal sphincter, when it does not relax or is fibrotic. "
        "The open approach is usually from the left, behind the larynx and in front of the prevertebral fascia; the myotomy is posterior or posterolateral so it stays away from the RLN in the tracheoesophageal groove, and it stops at intact mucosa."
    ),
    "layers": [
        {"step": "Incision", "structures": ["skin", "platysma", "external jugular vein (lateral)"],
         "note": "A horizontal incision at about the cricoid level or along the anterior border of the left SCM."},
        {"step": "Investing fascia and SCM", "structures": ["investing fascia", "anterior border of the SCM", "omohyoid (crosses the field)"],
         "note": "Retract the SCM laterally and divide or retract the omohyoid."},
        {"step": "Carotid sheath and thyroid", "structures": ["carotid sheath (lateral)", "middle thyroid vein", "thyroid lobe and larynx (medial)", "inferior thyroid artery (crossing transversely)"],
         "note": "Ligate the middle thyroid vein. Retract the carotid sheath laterally and the thyroid and larynx medially. The inferior thyroid artery and RLN may be seen deep to the lobe."},
        {"step": "Retrovisceral space", "structures": ["prevertebral fascia (posterior)", "buccopharyngeal fascia over the pharynx", "cervical spine"],
         "note": "Bluntly open the space behind the pharynx and esophagus along the prevertebral fascia. Rotate the larynx toward the opposite side so the posterolateral pharyngoesophageal junction faces you."},
        {"step": "Pharyngoesophageal segment", "structures": ["inferior constrictor (thyropharyngeus, oblique fibers)", "cricopharyngeus (horizontal fibers)", "upper esophageal circular and longitudinal muscle"],
         "note": "A bougie or scope in the lumen tents the wall. The cricopharyngeus is the band of horizontal fibers at about the cricoid level between the oblique thyropharyngeus above and the esophageal muscle below."},
        {"step": "Myotomy", "structures": ["muscle fibers", "submucosa", "intact mucosa"],
         "note": "Divide all muscle layers vertically down to bulging mucosa, from the lowest inferior constrictor fibers through the full cricopharyngeus onto the upper cervical esophagus; the total length is commonly about 4-5 cm, though reported lengths vary. Cut posteriorly or posterolaterally, away from the RLN."},
        {"step": "Mucosal check and closure", "structures": ["mucosa", "drain"],
         "note": "Insufflate air or fill with saline to test the mucosa; repair any tear. Close with a drain when appropriate."},
    ],
    "landmarks": [
        {"structure": "Cricoid cartilage", "how_to_find": "Palpable posterolaterally once the larynx is rotated; the cricopharyngeus attaches to the sides of the cricoid lamina", "why": "The muscle sits at this level"},
        {"structure": "Cricopharyngeus", "how_to_find": "Horizontal muscle band, often thicker and firmer than the surrounding muscle, tented by the intraluminal bougie", "why": "Target of myotomy"},
        {"structure": "Prevertebral fascia", "how_to_find": "Smooth fascia on the front of the vertebral bodies and longus colli muscles, behind the retrovisceral space", "why": "Defines the safe blunt plane behind the esophagus"},
        {"structure": "Tracheoesophageal groove", "how_to_find": "Angle between the trachea and esophagus medially, below the inferior thyroid artery", "why": "The RLN runs here; keep the myotomy posterior to it"},
        {"structure": "Inferior thyroid artery", "how_to_find": "Runs transversely from behind the carotid sheath toward the lower thyroid lobe", "why": "A landmark for the RLN, which crosses near it"},
    ],
    "danger": [
        {"structure": "Esophageal mucosa", "where": "Directly under the divided muscle", "protect": "Cut in thin layers with a bougie in place; test for leaks", "injury": "Perforation, fistula, mediastinitis"},
        {"structure": "RLN", "where": "In the tracheoesophageal groove, anteromedial to the myotomy", "protect": "Keep the myotomy posterior or posterolateral; avoid deep retraction against the groove", "injury": "Vocal-fold paralysis, worse dysphagia and aspiration"},
        {"structure": "Carotid sheath", "where": "Lateral to the dissection", "protect": "Use gentle lateral retraction", "injury": "Vascular injury, vagal injury"},
        {"structure": "Thoracic duct", "where": "Low left neck, lateral to the esophagus near the thoracic inlet", "protect": "Stay above the low neck when the incision is high; inspect for chyle", "injury": "Chyle leak"},
        {"structure": "Retrovisceral space contamination", "where": "Behind the esophagus, continuous with the posterior mediastinum", "protect": "Repair any mucosal tear and drain", "injury": "Mediastinitis"},
    ],
    "variants": [
        "Nonrecurrent right inferior laryngeal nerve with aberrant right subclavian artery (relevant in a right-sided approach)",
        "Cervical osteophytes behind the pharyngoesophageal segment",
        "Coexisting Zenker diverticulum, which can be excised, suspended or inverted with the myotomy",
    ],
    "imaging_check": [
        "Videofluoroscopic swallow: cricopharyngeal bar, UES opening, and pharyngeal contraction",
        "Barium esophagram for diverticulum",
        "High-resolution manometry in selected patients to confirm UES dysfunction with adequate pharyngeal propulsion",
    ],
    "blood_nerve": [
        ["Arterial supply", "Inferior thyroid artery branches"],
        ["Motor", "Pharyngeal plexus (vagus) and RLN fibers"],
        ["Sensory", "Vagal branches"],
    ],
    "pimp": [
        {"q": "What are the attachments of the cricopharyngeus?", "a": "Both sides of the cricoid lamina, forming a sling around the back of the pharyngoesophageal junction"},
        {"q": "Why approach from the left?", "a": "The cervical esophagus lies slightly to the left of midline, and the left RLN is consistently recurrent"},
        {"q": "What are the components of the UES?", "a": "Cricopharyngeus, lower inferior constrictor and upper cervical esophageal muscle"},
        {"q": "What vertebral level is the cricopharyngeus at?", "a": "About C5-C6, at the cricoid"},
        {"q": "Which muscle forms the upper border of Killian's triangle?", "a": "Thyropharyngeus (oblique part of the inferior constrictor)"},
        {"q": "What relationship does the RLN have to the inferior thyroid artery?", "a": "It crosses the artery, passing in front of, behind or between its branches (variable)"},
        {"q": "Why must pharyngeal propulsion be intact before myotomy?", "a": "Myotomy only lowers outflow resistance; it cannot help a weak pharynx"},
    ],
    "atlas_topics": ["Pharynx / UES / Cervical Esophagus", "Pharyngeal Constrictors / Superior Laryngeal Neurovascular Relationships", "Thyroid / RLN / EBSLN Anatomy"],
    "sources": [
        ["Cummings Otolaryngology 7e — Upper esophageal sphincter disorders", ""],
        ["Myers Operative Otolaryngology — Cricopharyngeal myotomy", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Dysphagia", ""],
    ],
}

CASES["laryngeal-botox"] = {
    "title": "Laryngeal Botulinum Toxin Injection",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Botulinum toxin weakens the overactive laryngeal muscles of spasmodic dysphonia: the thyroarytenoid (and sometimes lateral cricoarytenoid) in adductor type and the posterior cricoarytenoid in abductor type. "
        "Accuracy depends on reaching the target through the cricothyroid membrane or behind the thyroid ala and confirming it with EMG activation; safety depends on avoiding bilateral abductor weakness and diffusion into swallowing muscles."
    ),
    "layers": [
        {"step": "Positioning and landmarks", "structures": ["thyroid notch", "inferior border of thyroid cartilage", "cricothyroid membrane", "cricoid"],
         "note": "Neck slightly extended. Palpate and mark the midline, the cricothyroid space and the cricoid. Local anesthetic is optional; injecting into the airway causes cough."},
        {"step": "Cricothyroid membrane (TA approach)", "structures": ["skin", "subcutaneous tissue", "cricothyroid membrane just off midline", "cricothyroid muscle (lateral, on the outside of the membrane)"],
         "note": "Pass the hollow EMG needle through the membrane a few millimeters lateral to midline. Angle superiorly and laterally toward the fold, staying submucosal."},
        {"step": "Thyroarytenoid target", "structures": ["TA muscle under the vocal fold", "subglottic mucosa"],
         "note": "Ask the patient to say 'eee'. A brisk EMG burst means the tip is in TA. Loss of signal and cough suggest the needle is in the airway."},
        {"step": "Lateral cricoarytenoid target (if used)", "structures": ["LCA muscle (posterolateral to TA)"],
         "note": "Angle more laterally and posteriorly; LCA also activates with phonation."},
        {"step": "Posterior cricoarytenoid target (abductor type)", "structures": ["posterior border of the thyroid ala", "posterior cricoid lamina", "PCA muscle"],
         "note": "Rotate the larynx by hooking the posterior thyroid border, pass the needle behind the ala to the cricoid lamina, then withdraw slightly. Confirm with a sniff (PCA activates). An alternative (transtracheal) route passes through the cricothyroid membrane, across the subglottic airway and through the posterior cricoid lamina into the PCA."},
    ],
    "landmarks": [
        {"structure": "Cricothyroid membrane", "how_to_find": "Soft gap between the inferior thyroid border and the cricoid arch", "why": "Entry point for TA and LCA injections"},
        {"structure": "Posterior border of the thyroid ala", "how_to_find": "Palpable edge behind the oblique line, felt when the larynx is rotated", "why": "PCA approach passes behind it"},
        {"structure": "Cricoid lamina", "how_to_find": "Hard surface felt by the needle tip behind the larynx", "why": "PCA lies on it; withdraw slightly after touching it"},
        {"structure": "EMG activation", "how_to_find": "Phonation ('eee') for TA/LCA; sniff for PCA; upward pitch glide for cricothyroid", "why": "Confirms the target muscle before injecting"},
    ],
    "danger": [
        {"structure": "Bilateral PCA", "where": "Behind the larynx on both sides", "protect": "Inject one side at a time, stagger sides, and check abduction before treating the other", "injury": "Bilateral abductor weakness, stridor"},
        {"structure": "Pharyngeal constrictors", "where": "Next to the PCA and posterior larynx", "protect": "Use a small volume and accurate EMG placement", "injury": "Dysphagia and aspiration"},
        {"structure": "Cricothyroid muscle", "where": "On the outer surface of the cricothyroid membrane, anterolaterally", "protect": "Check that the EMG signal is not a pitch-glide signal", "injury": "Lower pitch, poor pitch range"},
        {"structure": "Cricothyroid artery", "where": "Across the upper cricothyroid membrane", "protect": "Use a low entry and aspirate", "injury": "Bleeding, hematoma"},
        {"structure": "Airway", "where": "Subglottic lumen", "protect": "Stay submucosal; watch for cough", "injury": "Cough, laryngospasm, airway injection"},
    ],
    "variants": [
        "Calcified or ossified cartilage that changes needle path",
        "Short neck or obesity making landmarks hard to palpate",
        "Mixed or tremor phenotypes needing different target muscles",
    ],
    "imaging_check": [
        "Not routinely imaged: check airway and swallowing history and previous dose response",
        "Laryngoscopy to confirm diagnosis and to rule out structural lesions",
    ],
    "blood_nerve": [
        ["Motor", "RLN to TA, LCA and PCA; external branch of SLN to cricothyroid"],
        ["Arterial supply", "Superior and inferior laryngeal arteries; cricothyroid artery across the membrane"],
    ],
    "pimp": [
        {"q": "Which muscles are injected in adductor spasmodic dysphonia?", "a": "Thyroarytenoid, sometimes with the lateral cricoarytenoid"},
        {"q": "Which muscle is injected in abductor spasmodic dysphonia?", "a": "Posterior cricoarytenoid"},
        {"q": "How does botulinum toxin A work?", "a": "Cleaves SNAP-25 and blocks presynaptic acetylcholine release"},
        {"q": "What is the activation task for the PCA on EMG?", "a": "Sniff"},
        {"q": "What is the activation task for the cricothyroid?", "a": "Upward pitch glide"},
        {"q": "How long does a typical injection last?", "a": "About 3-4 months"},
        {"q": "Why stagger PCA injections?", "a": "To avoid bilateral abductor weakness and airway obstruction"},
    ],
    "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles", "Superior Laryngeal Nerve / Cricothyroid Space"],
    "sources": [
        ["Cummings Otolaryngology 7e — Neurologic disorders of the larynx (spasmodic dysphonia)", ""],
        ["Blitzer A, Brin MF. Botulinum toxin in laryngeal dystonia", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Voice disorders", ""],
    ],
}

CASES["microflap"] = {
    "title": "Microlaryngoscopy / Microflap for Benign Vocal-Fold Lesion",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Benign vocal-fold lesions (polyps, cysts, some nodules) live in the superficial lamina propria, the soft gel layer that lets the cover vibrate. "
        "A microflap lifts the epithelium off the lesion through an incision lateral to the vibrating edge, removes the lesion and lays the epithelium back. Voice outcome depends on preserving superficial lamina propria and epithelium and staying out of the vocal ligament."
    ),
    "layers": [
        {"step": "Mouth and oropharynx", "structures": ["upper incisors", "lips", "tongue (lingual nerve on its lateral floor)", "tongue base", "vallecula"],
         "note": "Protect teeth with a guard; avoid prolonged heavy suspension pressure on the tongue."},
        {"step": "Supraglottis", "structures": ["epiglottis", "aryepiglottic folds", "false folds", "ventricles"],
         "note": "Position the laryngoscope to see the whole membranous fold from the anterior commissure to the vocal process."},
        {"step": "Vocal-fold surface", "structures": ["epithelium (squamous)", "superior surface", "free (vibrating) edge", "inferior surface"],
         "note": "Palpate the lesion and the contralateral fold. Infusing saline with dilute epinephrine into the superficial lamina propria can separate the layers and show how deep the lesion goes."},
        {"step": "Incision", "structures": ["superior surface, lateral to the lesion"],
         "note": "Cut on the superior surface lateral to the lesion, away from the vibrating medial edge."},
        {"step": "Microflap plane", "structures": ["superficial lamina propria (Reinke's space)", "lesion", "vocal ligament (intermediate and deep lamina propria) below"],
         "note": "Elevate the epithelium medially within the superficial lamina propria. Stay above the shiny white vocal ligament."},
        {"step": "Lesion removal and redraping", "structures": ["lesion", "residual SLP", "epithelial flap"],
         "note": "Remove the lesion, keep normal SLP, and redrape the epithelium. Trim only redundant epithelium."},
    ],
    "landmarks": [
        {"structure": "Vocal ligament", "how_to_find": "Shiny, white, firm fibers deep to the gel-like superficial lamina propria; it resists dissection", "why": "The deep limit of the microflap"},
        {"structure": "Superior arcuate line", "how_to_find": "The lateral edge of Reinke's space on the superior surface, seen as the line where infused saline stops spreading", "why": "Lateral limit of the incision and flap"},
        {"structure": "Anterior commissure", "how_to_find": "The point where the two folds meet anteriorly, attached to the thyroid cartilage by Broyles ligament", "why": "Avoid opposing raw surfaces here (web risk)"},
        {"structure": "Vocal process", "how_to_find": "The posterior end of the membranous fold, white and firm", "why": "Posterior end of the vibratory fold"},
        {"structure": "Mid-membranous fold", "how_to_find": "Midpoint of the membranous fold, between the anterior commissure and vocal process", "why": "Usual site of nodules and many polyps (point of greatest contact)"},
    ],
    "danger": [
        {"structure": "Vocal ligament", "where": "Deep to the superficial lamina propria", "protect": "Stay in the SLP plane; use saline infusion and gentle dissection", "injury": "Scar, stiff fold, poor voice"},
        {"structure": "Free edge epithelium", "where": "Medial vibrating edge", "protect": "Incise laterally on the superior surface and preserve medial epithelium", "injury": "Scar and loss of mucosal wave"},
        {"structure": "Anterior commissure", "where": "Front of the glottis", "protect": "Avoid bilateral raw surfaces anteriorly; stage bilateral surgery", "injury": "Anterior glottic web"},
        {"structure": "Teeth and tongue", "where": "Under the laryngoscope", "protect": "Tooth guard; limit suspension time", "injury": "Dental injury, tongue numbness or taste change (lingual nerve), tongue edema"},
    ],
    "variants": [
        "Epidermoid cyst adherent to the vocal ligament",
        "Sulcus vocalis (invagination down to the ligament)",
        "Vascular ectasias on the fold that bleed or cause hemorrhagic polyps",
        "Limited exposure from small mouth, retrognathia or limited neck extension",
    ],
    "imaging_check": [
        "Not imaged: stroboscopy for lesion location, mucosal wave and contralateral lesion",
        "Clinically: dentition, mouth opening and neck extension for exposure",
    ],
    "blood_nerve": [
        ["Arterial supply", "Superior and inferior laryngeal arteries; microvessels run parallel to the free edge"],
        ["Sensory", "Internal branch of SLN above the folds"],
        ["Motor", "RLN (TA forms the body of the fold)"],
    ],
    "pimp": [
        {"q": "Name the vocal-fold layers from superficial to deep.", "a": "Epithelium, superficial lamina propria, intermediate lamina propria, deep lamina propria, thyroarytenoid muscle"},
        {"q": "What forms the vocal ligament?", "a": "Intermediate and deep lamina propria"},
        {"q": "Where are nodules usually found?", "a": "Mid-membranous fold (junction of anterior and middle thirds of the full fold)"},
        {"q": "Why incise lateral to the lesion?", "a": "To keep the medial vibrating edge intact"},
        {"q": "What is Broyles ligament?", "a": "The anterior commissure tendon attaching the vocal ligaments to the thyroid cartilage"},
        {"q": "What lies at the anterior and posterior ends of the vocal fold lamina propria?", "a": "The maculae flavae"},
        {"q": "Which nerve is commonly injured by suspension laryngoscopy pressure on the tongue?", "a": "Lingual nerve (tongue numbness, taste change)"},
    ],
    "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles"],
    "sources": [
        ["Hirano M. Phonosurgery: basic and clinical investigations (layered structure)", ""],
        ["Cummings Otolaryngology 7e — Benign vocal fold mucosal disorders", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Benign laryngeal lesions", ""],
    ],
}

CASES["rrp-debridement"] = {
    "title": "RRP Debridement / Laser-Safety Framework",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Recurrent respiratory papillomatosis is HPV-driven (mostly types 6 and 11) and tends to grow where squamous and ciliated epithelium meet. "
        "Surgery removes papilloma to keep the airway open and voice usable, not to cure; safety depends on preserving vocal-fold layers, avoiding anterior commissure webs, and preventing airway fire."
    ),
    "layers": [
        {"step": "Exposure", "structures": ["teeth", "tongue base", "epiglottis", "vallecula"],
         "note": "Use atraumatic suspension and tooth guard. Agree with anesthesia on airway: laser-safe tube, jet ventilation or apnea."},
        {"step": "Supraglottis survey", "structures": ["laryngeal surface of epiglottis", "aryepiglottic folds", "false folds", "ventricles"],
         "note": "Map disease at squamociliary junctions: limen vestibuli, laryngeal surface of the epiglottis, and the margins of the ventricles."},
        {"step": "Glottis", "structures": ["true vocal folds (superior and undersurface)", "anterior commissure", "posterior commissure"],
         "note": "True-fold papilloma usually sits in the epithelium and superficial lamina propria. Treat it superficially with microdebrider or angiolytic laser, staying above the vocal ligament, and preserve as much normal epithelium as possible."},
        {"step": "Anterior commissure", "structures": ["anterior ends of both folds", "Broyles ligament", "petiole of the epiglottis above"],
         "note": "When both sides of the commissure are diseased, clear one side fully and leave the other partly treated, or leave a strip of untreated mucosa at the apex, then return at the next session. Raw opposing surfaces here form a web."},
        {"step": "Subglottis and trachea", "structures": ["subglottis", "trachea", "carina", "tracheostomy site (if present)"],
         "note": "Inspect the distal airway with a telescope. Treat only what is safely reachable. Tracheostomy sites and the carina are prone to papilloma; avoid seeding by keeping debris out of the distal airway."},
        {"step": "Hemostasis and debris clearance", "structures": ["raw mucosal surfaces", "loose papilloma fragments"],
         "note": "Use topical vasoconstrictor pledgets rather than broad cautery. Suction all fragments so none are aspirated."},
    ],
    "landmarks": [
        {"structure": "Anterior commissure", "how_to_find": "Front of the glottis where both folds meet", "why": "Treat one side or leave a strip of normal mucosa to avoid web"},
        {"structure": "Vocal ligament", "how_to_find": "White, firm layer below the gel-like SLP", "why": "Deep limit of debridement"},
        {"structure": "Squamociliary junctions", "how_to_find": "Limen vestibuli, ventricle margins, laryngeal epiglottis, undersurface of folds", "why": "Common disease sites"},
        {"structure": "Endotracheal tube cuff", "how_to_find": "Seen in the subglottis or upper trachea", "why": "Must be protected from laser with wet cottonoids and saline-filled cuff"},
    ],
    "danger": [
        {"structure": "Airway (fire)", "where": "Laser beam path, ETT and oxygen", "protect": "Low FiO2 (as low as tolerated, about 30% or less), laser-safe tube, saline-filled cuff, wet pledgets", "injury": "Airway burn"},
        {"structure": "Anterior commissure", "where": "Front of the glottis", "protect": "Avoid bilateral raw surfaces", "injury": "Web"},
        {"structure": "Vocal ligament", "where": "Deep to SLP", "protect": "Superficial debridement only", "injury": "Scar and dysphonia"},
        {"structure": "Airway edema", "where": "Glottis and subglottis", "protect": "Minimal thermal injury; consider steroids", "injury": "Postoperative airway compromise"},
    ],
    "variants": [
        "Juvenile-onset RRP is usually more aggressive than adult-onset, with more frequent surgery",
        "Distal tracheal or pulmonary spread (more aggressive disease)",
        "Tracheostomy site seeding",
    ],
    "imaging_check": [
        "Not routinely imaged: laryngoscopy and staging (Derkay)",
        "CT chest in suspected pulmonary spread",
    ],
    "blood_nerve": [
        ["Arterial supply", "Superior and inferior laryngeal arteries"],
        ["Sensory", "Internal branch of SLN supraglottic; RLN subglottic"],
    ],
    "pimp": [
        {"q": "Which HPV types cause most RRP?", "a": "HPV 6 and 11"},
        {"q": "Where does papilloma tend to grow?", "a": "At squamociliary junctions"},
        {"q": "What is the fire triad?", "a": "Oxidizer, fuel, ignition source"},
        {"q": "CO2 laser wavelength and target?", "a": "10,600 nm, absorbed by water"},
        {"q": "KTP laser wavelength and target?", "a": "532 nm, absorbed by oxyhemoglobin"},
        {"q": "Why avoid tracheostomy in RRP?", "a": "It may promote distal spread to the stoma and trachea"},
        {"q": "Which systemic adjuvant is now used for severe RRP?", "a": "Bevacizumab"},
        {"q": "What staging system is common for RRP?", "a": "Derkay (Coltrera-Derkay) staging"},
        {"q": "What vaccine is thought to reduce juvenile-onset RRP?", "a": "Quadrivalent or 9-valent HPV vaccine (covers types 6 and 11)"},
    ],
    "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles", "Pediatric Laryngotracheal Airway"],
    "sources": [
        ["Derkay CS et al. A staging system for assessing severity of disease and response to therapy in RRP. Laryngoscope 1998", ""],
        ["Kashima H et al. Sites of predilection in RRP. Ann Otol Rhinol Laryngol 1993", ""],
        ["Cummings Otolaryngology 7e — Recurrent respiratory papillomatosis", ""],
    ],
}

CASES["lingual-tonsillectomy"] = {
    "title": "Lingual Tonsillectomy / Tongue-Base Reduction",
    "region": "Sleep Surgery",
    "summary": (
        "Lingual tonsillectomy and tongue-base reduction enlarge the retrolingual airway by removing lymphoid tissue or muscle from the posterior tongue. "
        "The lingual tonsil is a superficial layer on the tongue base without a true capsule; the lingual artery and hypoglossal nerve lie deep and lateral, so the midline and superficial planes are safest."
    ),
    "layers": [
        {"step": "Exposure", "structures": ["teeth", "oral tongue", "circumvallate papillae", "sulcus terminalis"],
         "note": "Use a mouth gag or laryngoscope, or TORS/coblation with angled telescopes. Pull the tongue forward to show the base."},
        {"step": "Lingual tonsil", "structures": ["lymphoid tissue on the tongue base", "foramen cecum (midline apex of sulcus terminalis)", "vallecula (inferior)"],
         "note": "The lymphoid layer sits on the tongue muscle behind the circumvallate papillae and extends to the vallecula."},
        {"step": "Deep plane", "structures": ["intrinsic and genioglossus muscle", "dorsal lingual artery branches"],
         "note": "Remove lymphoid tissue down to muscle; for tongue-base reduction, remove muscle in the midline."},
        {"step": "Lateral limits", "structures": ["lateral tongue base", "glossotonsillar sulcus", "lingual artery and hypoglossal nerve deep and lateral"],
         "note": "Stay medial and superficial; lateral and deep dissection approaches the neurovascular bundle."},
        {"step": "Inferior limit", "structures": ["vallecula", "epiglottis", "glossoepiglottic fold"],
         "note": "Avoid injuring the epiglottis and vallecula to prevent scarring and supraglottic stenosis."},
    ],
    "landmarks": [
        {"structure": "Circumvallate papillae", "how_to_find": "V-shaped row of large papillae in front of the sulcus terminalis", "why": "Anterior limit of the lingual tonsil"},
        {"structure": "Foramen cecum", "how_to_find": "Midline pit at the apex of the sulcus terminalis", "why": "Origin of thyroid descent; lingual thyroid sits here"},
        {"structure": "Vallecula", "how_to_find": "Pockets between the tongue base and epiglottis, separated by the median glossoepiglottic fold", "why": "Inferior limit"},
        {"structure": "Lingual artery", "how_to_find": "Doppler or deep lateral pulsation; in TORS found deep and lateral at the tongue base", "why": "Major hemorrhage risk"},
    ],
    "danger": [
        {"structure": "Lingual artery", "where": "Deep and lateral in the tongue base", "protect": "Stay medial and superficial; use Doppler when needed", "injury": "Major hemorrhage"},
        {"structure": "Hypoglossal nerve", "where": "Lateral to hyoglossus, deep and lateral to the tongue base", "protect": "Avoid deep lateral dissection", "injury": "Tongue weakness"},
        {"structure": "Glossopharyngeal nerve (lingual branches)", "where": "Lateral tongue base and posterior tongue", "protect": "Avoid deep lateral thermal injury", "injury": "Taste and sensory change"},
        {"structure": "Epiglottis and vallecula", "where": "Inferior limit", "protect": "Stay above the vallecula", "injury": "Scarring, dysphagia, supraglottic stenosis"},
        {"structure": "Airway", "where": "Tongue base edema", "protect": "Steroids; monitor", "injury": "Airway obstruction"},
    ],
    "variants": [
        "Lingual thyroid at the foramen cecum (may be the only thyroid tissue)",
        "Thyroglossal duct remnant",
        "Large lingual tonsil after palatine tonsillectomy",
    ],
    "imaging_check": [
        "Confirm normal thyroid in the neck before removing midline tongue-base tissue (ultrasound or prior imaging)",
        "Drug-induced sleep endoscopy: tongue-base collapse pattern",
        "Consider CT/MRI for asymmetric or suspicious tongue-base masses",
    ],
    "blood_nerve": [
        ["Arterial supply", "Lingual artery (dorsal lingual branches) and tonsillar branches"],
        ["Sensory", "Glossopharyngeal nerve (posterior third) and internal branch of SLN near the vallecula"],
        ["Motor", "Hypoglossal nerve"],
    ],
    "pimp": [
        {"q": "What is the sensory and taste supply to the posterior third of the tongue?", "a": "Glossopharyngeal nerve"},
        {"q": "Where does the lingual artery run relative to hyoglossus?", "a": "Deep (medial) to hyoglossus"},
        {"q": "What lies superficial (lateral) to hyoglossus?", "a": "Hypoglossal nerve, lingual nerve and lingual vein"},
        {"q": "What is the foramen cecum?", "a": "Origin of the thyroid diverticulum at the apex of the sulcus terminalis"},
        {"q": "Name the components of Waldeyer's ring.", "a": "Adenoid, tubal tonsils, palatine tonsils, lingual tonsil"},
        {"q": "Does the lingual tonsil have a capsule?", "a": "No true capsule"},
        {"q": "What divides the vallecula into two pockets?", "a": "The median glossoepiglottic fold"},
        {"q": "What is the most important preoperative check before removing a midline tongue-base mass?", "a": "Confirm normal thyroid tissue in the neck (to avoid removing a lingual thyroid)"},
    ],
    "atlas_topics": ["Tongue Base / Hyoid / Suprahyoid Relationships", "Oral Tongue / Floor of Mouth", "Hypoglossal Nerve / HNS Surgical Anatomy"],
    "sources": [
        ["Cummings Otolaryngology 7e — Sleep surgery: tongue base procedures", ""],
        ["K.J. Lee Essential Otolaryngology 12e — Sleep apnea surgery", ""],
    ],
}

CASES["laryngeal-fracture"] = {
    "title": "Laryngeal Fracture Repair",
    "region": "Laryngology / Voice / Swallowing",
    "summary": (
        "Laryngeal fracture repair restores the cartilage framework and mucosal lining after blunt or penetrating trauma. "
        "Airway first (often tracheostomy), then repair mucosa so no cartilage is exposed, resuspend the anterior commissure, and fix fractures to restore height and width."
    ),
    "layers": [
        {"step": "Airway", "structures": ["tracheostomy site (rings 2-4)", "cricoid"],
         "note": "Avoid intubation through an unstable larynx; awake tracheostomy is often safest."},
        {"step": "Exposure", "structures": ["skin", "platysma", "strap muscles", "thyroid cartilage", "cricoid", "cricothyroid membrane"],
         "note": "A horizontal incision at about the level of the cricothyroid membrane. Separate the straps in the midline, then lift them off the thyroid ala to see every fracture line and the cricoid."},
        {"step": "Laryngofissure (if needed)", "structures": ["midline thyroid cartilage", "anterior commissure", "vocal folds"],
         "note": "Midline thyrotomy, entering through the cricothyroid membrane and cutting up through the anterior commissure under vision."},
        {"step": "Mucosal repair", "structures": ["endolaryngeal mucosa", "arytenoids", "vocal folds"],
         "note": "Close mucosal tears with fine absorbable sutures, cover exposed cartilage with local mucosa, and reduce a dislocated arytenoid. Resuspend the anterior ends of the vocal folds to the outer thyroid perichondrium or cartilage so the commissure sits at its original height."},
        {"step": "Framework fixation", "structures": ["thyroid cartilage fractures", "cricoid fractures"],
         "note": "Reduce thyroid and cricoid fractures and fix them with miniplates (or wire or sutures in a soft cartilage). Restoring the anterior thyroid angle and cricoid ring maintains glottic and subglottic size."},
        {"step": "Stent (if required)", "structures": ["endolaryngeal stent"],
         "note": "Use for severe mucosal disruption or anterior commissure instability."},
    ],
    "landmarks": [
        {"structure": "Thyroid notch", "how_to_find": "V-shaped notch on top of the thyroid cartilage", "why": "Midline for laryngofissure"},
        {"structure": "Anterior commissure", "how_to_find": "Classically about the midpoint of the midline thyroid cartilage height (cadaver studies place it at or somewhat above the midpoint); match the uninjured side and the original attachment", "why": "Must be resuspended at its original height"},
        {"structure": "Cricoid", "how_to_find": "Complete ring below the cricothyroid membrane", "why": "Injury causes subglottic stenosis"},
        {"structure": "RLN entry", "how_to_find": "Behind the cricothyroid joint", "why": "At risk with lateral cricoid fractures and laryngotracheal separation"},
    ],
    "danger": [
        {"structure": "Airway", "where": "Larynx and subglottis", "protect": "Tracheostomy before manipulation", "injury": "Airway loss"},
        {"structure": "Anterior commissure", "where": "Midline glottis", "protect": "Resuspend", "injury": "Web, dysphonia"},
        {"structure": "RLN", "where": "Behind the cricothyroid joint", "protect": "Avoid dissection posteriorly", "injury": "Vocal-fold paralysis"},
        {"structure": "Cricoid", "where": "Below the thyroid cartilage", "protect": "Repair and stabilize", "injury": "Subglottic stenosis"},
        {"structure": "Esophagus and pharynx", "where": "Behind the larynx", "protect": "Inspect for injury", "injury": "Perforation and mediastinitis"},
    ],
    "variants": [
        "Children: flexible cartilage, more soft-tissue injury than fracture",
        "Older adults: ossified, brittle cartilage with comminuted fractures",
        "Laryngotracheal separation with bilateral RLN injury",
    ],
    "imaging_check": [
        "CT larynx: fracture lines, displacement, cricoid integrity",
        "CT angiography if vascular injury suspected",
        "Esophagram or esophagoscopy for associated injury",
        "Cervical spine imaging",
    ],
    "blood_nerve": [
        ["Arterial supply", "Superior and inferior laryngeal arteries"],
        ["Motor", "RLN (intrinsic muscles); EBSLN (cricothyroid)"],
        ["Sensory", "Internal branch of SLN supraglottic; RLN subglottic"],
    ],
    "pimp": [
        {"q": "What is the Schaefer classification?", "a": "Group I minor hematoma or laceration; II edema, hematoma, minor mucosal disruption, nondisplaced fracture; III massive edema, mucosal tear, exposed cartilage, displaced fracture, immobile fold; IV as III with unstable framework or anterior commissure disruption; V laryngotracheal separation"},
        {"q": "When should repair be done?", "a": "Early: ideally within 24 hours and generally within 48 hours, once the airway is secure (some advocate waiting a few days for edema, but delayed repair is associated with worse voice and airway outcomes)"},
        {"q": "Why repair mucosa before cartilage?", "a": "To avoid exposed cartilage and chondritis"},
        {"q": "What are the indications for a stent?", "a": "Severe mucosal disruption, anterior commissure instability, comminuted fractures"},
        {"q": "What happens in laryngotracheal separation?", "a": "Distal trachea retracts into the mediastinum; RLNs often injured"},
        {"q": "Why avoid intubation in an unstable larynx?", "a": "It can worsen injury or create a false passage"},
        {"q": "Why are children less likely to fracture the larynx?", "a": "Their larynx sits higher under the mandible and their cartilage is more elastic"},
        {"q": "Which cartilage injury most threatens long-term airway?", "a": "Cricoid fracture (the only complete ring), leading to subglottic stenosis"},
    ],
    "atlas_topics": ["Laryngeal Framework / Intrinsic Muscles", "Laryngeal Neurovascular Anatomy", "Tracheostomy / Cervical Trachea Anatomy"],
    "sources": [
        ["Schaefer SD. Management of acute blunt and penetrating external laryngeal trauma. Laryngoscope 2014", ""],
        ["Cummings Otolaryngology 7e — Laryngeal trauma", ""],
    ],
}

