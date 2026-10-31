"""General ENT / Emergencies (part A): mechanism-level teaching content."""

CONTENT = {
"Post-Tonsillectomy Hemorrhage": dict(
overview=(
"Post-tonsillectomy hemorrhage is primary (within 24 hours) or secondary (after 24 hours, typically days 5-10 when the eschar separates). "
"It is the most common serious complication of tonsillectomy and can be fatal through airway compromise and hypovolemia, especially in small children."),
physiology=(
"**Tonsillar blood supply**: mainly the tonsillar branch of the facial artery, plus the ascending pharyngeal, dorsal lingual, ascending palatine, and lesser palatine arteries; the paratonsillar (external palatine) vein drains it. "
"**Tonsillar fossa**: the tonsil lies on the superior constrictor; the internal carotid lies about 2.5 cm posterolateral. "
"**Wound healing by secondary intention**: a fibrinous exudate (white eschar) covers the fossa, then granulation tissue forms underneath. "
"**Pediatric blood volume**: about 80 mL/kg in infants and roughly 70-80 mL/kg in older children, so a small child loses a large proportion of volume with modest bleeding. "
"**Coagulation**: platelet plug and fibrin clot seal small vessels."),
pathophysiology=(
"**Primary hemorrhage**: incomplete hemostasis or a slipped tie, often from a larger vessel at the lower pole. "
"**Secondary hemorrhage**: separation of the eschar around days 5-10 exposes vessels in granulating tissue; dehydration, infection, and reduced oral intake contribute. "
"**Swallowed blood**: children swallow blood and present with hematemesis or tachycardia before obvious bleeding, so hypotension is late. "
"**Airway risk**: blood and clot can be aspirated, and induction of anesthesia in a bleeding child requires rapid sequence technique. "
"**Coagulopathy**: undiagnosed von Willebrand disease or NSAID effects may contribute; ibuprofen is not associated with significant increased risk in modern evidence. "
"**Management logic**: assess volume status, examine, remove clot, and control bleeding under anesthesia when bleeding is active or recurrent."),
),

"Deep Neck Space Infection": dict(
overview=(
"Deep neck space infections spread along fascial planes from dental, tonsillar, salivary, or nodal sources. "
"They threaten the airway, mediastinum, and great vessels, and are managed with airway control, antibiotics, and drainage."),
physiology=(
"**Cervical fascia**: the superficial layer of the deep cervical fascia invests the SCM, trapezius, and glands; the middle layer surrounds the viscera (pretracheal); the deep layer has prevertebral and alar divisions. "
"**Key spaces**: submandibular (sublingual above and submaxillary below the mylohyoid), parapharyngeal (pre- and poststyloid), retropharyngeal, danger, prevertebral, and carotid space. "
"**Danger space**: between alar and prevertebral fascia, extending from skull base to diaphragm. "
"**Dental anatomy**: roots of the second and third mandibular molars lie below the mylohyoid line."),
pathophysiology=(
"**Source**: odontogenic infection is the most common adult source; tonsillitis and lymphadenitis are common in children. "
"**Fascial spread**: infection follows planes of least resistance, from the submandibular space to parapharyngeal and retropharyngeal spaces, then through the danger space into the mediastinum. "
"**Airway compromise**: floor-of-mouth swelling displaces the tongue upward and backward; pharyngeal wall edema narrows the airway. "
"**Vascular complications**: internal jugular thrombophlebitis (Lemierre), carotid erosion, and septic emboli. "
"**Microbiology**: polymicrobial streptococci, anaerobes, and S. aureus. "
"**Treatment logic**: secure the airway first; CT distinguishes phlegmon from abscess; drainage for abscess and failure of medical therapy."),
),

"Tracheostomy Emergency": dict(
overview=(
"Tracheostomy emergencies (decannulation, tube obstruction, bleeding) are a leading cause of preventable airway deaths. "
"Response depends on whether the patient has a patent upper airway and how mature the tract is."),
physiology=(
"**Tract maturation**: the stoma tract matures over about 3-7 days (Pasha 3-5; 5-7 in children per Bluestone; at least 7 after percutaneous placement), after which the tube can usually be replaced through it. "
"**Upper airway status**: a laryngectomy patient has no connection between the mouth and trachea; a tracheostomy patient usually does. "
"**Humidification**: the upper airway normally humidifies air; bypassing it dries secretions. "
"**Cuff function**: an inflated cuff seals the trachea for ventilation and limits aspiration."),
pathophysiology=(
"**Accidental decannulation in an immature tract**: tissue planes collapse, and blind reinsertion can create a false passage into the pretracheal space. "
"**Obstruction**: dried mucus plugs the inner cannula, especially without humidification. "
"**False passage**: inability to ventilate, subcutaneous emphysema, and loss of end-tidal CO2. "
"**Tracheoinnominate fistula**: tube or cuff erosion into the innominate artery, usually within the first weeks after placement (Cummings: most between 3 and 4 weeks), often preceded by a sentinel bleed; cuff overinflation and digital pressure temporize. "
"**Management algorithm**: oxygenate via face and stoma, remove the inner cannula, pass a suction catheter, deflate the cuff, and remove the tube if needed; orally intubate if the upper airway is patent (not in laryngectomy)."),
),

"Epistaxis": dict(
overview=(
"Epistaxis is very common; most is anterior from Kiesselbach plexus and controlled with pressure, vasoconstrictors, cautery, or packing. "
"Posterior bleeding is less common but heavier, often in older and anticoagulated patients, and may need endoscopic ligation or embolization."),
physiology=(
"**Dual carotid supply**: the external carotid (sphenopalatine, greater palatine, superior labial) and internal carotid (anterior and posterior ethmoid arteries) supply the nose. "
"**Kiesselbach plexus**: anastomosis on the anterior septum of sphenopalatine, anterior ethmoid, greater palatine, and superior labial branches. "
"**Mucosal humidity**: nasal mucosa is thin and highly vascular, protected by humidification. "
"**Hemostasis**: vasoconstriction, platelet plug, and coagulation cascade."),
pathophysiology=(
"**Anterior bleeds**: mucosal drying, digital trauma, and inflammation expose Kiesselbach vessels. "
"**Posterior bleeds**: sphenopalatine branches in older patients with hypertension and atherosclerosis; harder to visualize and pack. "
"**Systemic factors**: anticoagulants, antiplatelets, coagulopathy, liver disease, and hereditary hemorrhagic telangiectasia. "
"**HHT**: autosomal dominant fragile telangiectasias (ENG, ACVRL1) cause recurrent bleeding. "
"**Unilateral recurrent bleeding with obstruction**: in an adolescent male suggests JNA. "
"**Management logic**: direct pressure and vasoconstrictors; targeted cautery; packing for diffuse bleeding; SPA ligation for refractory posterior bleeding; ethmoid artery ligation for superior bleeding."),
),

"Peritonsillar Abscess": dict(
overview=(
"Peritonsillar abscess is pus between the tonsillar capsule and the superior constrictor, the most common deep neck infection in young adults. "
"It causes trismus, muffled voice, and uvular deviation, and is treated with drainage and antibiotics."),
physiology=(
"**Peritonsillar space**: potential space between the tonsil capsule and the superior constrictor muscle. "
"**Weber glands**: minor salivary glands in the supratonsillar space that drain to the tonsil surface. "
"**Neighbors**: the pterygoid muscles (trismus) and parapharyngeal space lie laterally; the internal carotid is posterolateral. "
"**Superior pole**: most abscesses form at the superior pole."),
pathophysiology=(
"**Spread from tonsillitis**: infection extends through the tonsillar capsule into the peritonsillar space. "
"**Weber gland theory**: obstruction and infection of Weber glands may explain abscess formation even without preceding tonsillitis. "
"**Trismus**: inflammation irritates the medial pterygoid. "
"**Hot potato voice**: palatal swelling alters resonance. "
"**Uvular deviation**: displacement away from the abscess. "
"**Microbiology**: Group A strep, Fusobacterium, and anaerobes. "
"**Treatment logic**: needle aspiration or incision and drainage; quinsy tonsillectomy for recurrence or failure."),
),

"Ludwig Angina": dict(
overview=(
"Ludwig angina is rapidly spreading cellulitis of the bilateral submandibular, sublingual, and submental spaces, usually odontogenic. "
"It threatens the airway by pushing the tongue up and back, and airway control comes first."),
physiology=(
"**Mylohyoid muscle**: divides the sublingual space (above) from the submaxillary space (below). "
"**Tooth roots**: second and third molar roots extend below the mylohyoid line, draining infection into the submaxillary space. "
"**Floor of mouth**: confined by the mandible and hyoid, so swelling displaces the tongue. "
"**Communication**: spaces communicate around the posterior mylohyoid."),
pathophysiology=(
"**Odontogenic source**: infection from lower molars spreads into the submandibular spaces bilaterally. "
"**Cellulitis more than abscess**: woody, indurated swelling without a discrete collection early. "
"**Airway obstruction**: tongue elevation and posterior displacement and supraglottic edema. "
"**Spread**: to parapharyngeal and retropharyngeal spaces and the mediastinum. "
"**Management logic**: secure airway (awake fiberoptic intubation or awake tracheostomy), IV antibiotics, steroids in selected cases (case-series evidence), and drainage plus tooth extraction."),
),

"Angioedema": dict(
overview=(
"Angioedema is deep dermal or submucosal swelling of the lips, tongue, and larynx; it may be histaminergic (allergic) or bradykinin-mediated (ACE inhibitor, hereditary). "
"Mechanism determines treatment, and airway management is the priority."),
physiology=(
"**Vascular permeability**: histamine and bradykinin increase postcapillary venule permeability. "
"**Bradykinin metabolism**: angiotensin-converting enzyme degrades bradykinin. "
"**C1 esterase inhibitor**: regulates the kallikrein-kinin and complement systems. "
"**Airway tissues**: loose submucosa of the tongue, floor of mouth, and supraglottis swells easily."),
pathophysiology=(
"**Histaminergic angioedema**: mast-cell degranulation with urticaria and itching; responds to epinephrine, antihistamines, and steroids. "
"**ACE-inhibitor angioedema**: reduced bradykinin degradation causes swelling (more common in Black patients), often of the tongue and lips, without urticaria; it often responds poorly to epinephrine and antihistamines (although K.J. Lee lists them with steroids in initial management); the core of care is stopping the drug and protecting the airway, and icatibant was not superior to placebo in a randomized trial (Sinert et al., J Allergy Clin Immunol Pract 2017). "
"**Hereditary angioedema**: C1 inhibitor deficiency or dysfunction causes recurrent episodes; treated with C1 inhibitor, icatibant, or ecallantide. "
"**Airway assessment**: flexible laryngoscopy determines laryngeal involvement; awake fiberoptic intubation or surgical airway for progressive airway swelling."),
),

"Caustic Ingestion": dict(
overview=(
"Caustic ingestion of alkalis or acids injures the upper aerodigestive tract and esophagus, ranging from mucosal burns to perforation. "
"Endoscopy at about 24-48 hours (not before 12 hours, which can underestimate injury) grades injury and predicts stricture."),
physiology=(
"**Esophageal wall**: mucosa, submucosa, and muscularis without serosa. "
"**Healing**: inflammation, granulation, and collagen deposition over weeks, with stricture formation by 3 weeks onward. "
"**Esophageal narrowings**: sites where caustics pool."),
pathophysiology=(
"**Alkali**: liquefactive necrosis penetrates deeply, causing full-thickness esophageal injury (drain cleaners, button batteries). "
"**Acid**: coagulative necrosis forms an eschar that limits penetration, but acid causes gastric injury. "
"**Zargar grading**: grade 2b and 3 predict stricture and perforation. "
"**Stricture**: collagen deposition and contraction cause stenosis weeks later. "
"**Long-term risk**: increased esophageal carcinoma risk decades later."),
),

"Esophageal Foreign Body": dict(
overview=(
"Esophageal foreign bodies lodge at narrowings, most often at the cricopharyngeus in children and over strictures or food boluses in adults. "
"Button batteries and sharp objects require urgent removal."),
physiology=(
"**Physiologic narrowings**: cricopharyngeus, aortic arch, left main bronchus, and lower esophageal sphincter. "
"**Esophageal motility**: peristalsis moves food; reduced in certain disorders. "
"**Esophageal wall**: thin with no serosa."),
pathophysiology=(
"**Impaction**: objects lodge at narrowings or pathologic strictures (EoE, rings, cancer). "
"**Food bolus impaction**: in adults, often reveals EoE or stricture. "
"**Pressure necrosis**: prolonged impaction injures mucosa and can cause perforation. "
"**Button batteries**: generate hydroxide and cause rapid necrosis. "
"**Sharp objects**: perforation risk."),
),

"Airway Foreign Body": dict(
overview=(
"Airway foreign bodies in adults and children cause choking, cough, and wheeze, sometimes presenting late as pneumonia. "
"Rigid bronchoscopy remains the standard for removal in children; flexible bronchoscopy is often used in adults."),
physiology=(
"**Airway branching**: the right main bronchus is wider and more vertical in adults, favoring right-sided aspiration. "
"**Cough reflex**: clears foreign material. "
"**Ventilation**: partial obstruction creates ball-valve effects."),
pathophysiology=(
"**Check-valve (often called ball-valve) obstruction**: partial obstruction allows inspiration but traps air on expiration, causing hyperinflation and mediastinal shift away. "
"**Complete obstruction**: distal atelectasis and pneumonia. "
"**Organic materials**: nuts and seeds swell and cause intense inflammation. "
"**Delayed presentation**: recurrent pneumonia, wheeze, or bronchiectasis. "
"**Removal**: rigid bronchoscopy allows ventilation and secure extraction."),
),

"Postoperative Neck Hematoma": dict(
overview=(
"Postoperative neck hematoma after thyroid, parathyroid, or neck surgery can rapidly compromise the airway. "
"Immediate bedside wound opening is lifesaving when the airway is threatened."),
physiology=(
"**Closed neck compartment**: the strap muscles and deep cervical fascia confine the central neck. "
"**Venous and lymphatic drainage**: the larynx and pharynx depend on low-pressure venous and lymphatic outflow. "
"**Airway structures**: the larynx and trachea are central."),
pathophysiology=(
"**Venous and lymphatic obstruction**: hematoma compresses veins and lymphatics, causing laryngeal and pharyngeal edema; this, rather than direct tracheal compression, is the main mechanism of airway compromise. "
"**Timing**: most occur early (the first hours to a day), but some occur up to several days after surgery (K.J. Lee). "
"**Risk factors**: hypertension, coughing or vomiting at emergence, anticoagulation, and large goiters. "
"**Management**: SCOOP (skin exposure, cut sutures, open skin, open muscles, pack; DAS/BAETS consensus, Iliff et al., Anaesthesia 2022) at the bedside, then OR evacuation."),
),

"Chyle Leak": dict(
overview=(
"Chyle leak follows injury to the thoracic duct or its tributaries during neck dissection, typically left level IV. "
"It causes milky drainage that increases with enteral feeding and can lead to malnutrition and immunodeficiency."),
physiology=(
"**Thoracic duct**: carries lymph and chylomicrons from the intestines, ascending to the left venous angle (internal jugular-subclavian junction). "
"**Chyle composition**: triglycerides, lymphocytes, proteins, and fat-soluble vitamins. "
"**Flow**: high-volume lymph flow that increases sharply after fatty meals."),
pathophysiology=(
"**Injury**: duct or tributaries injured at the left venous angle, sometimes right-sided. "
"**Diagnosis**: milky drainage with triglycerides over 100 mg/dL and above the serum level, or chylomicrons. "
"**Consequences**: fluid and electrolyte loss, hypoproteinemia, lymphopenia, and wound breakdown. "
"**Medium-chain triglycerides**: absorbed directly into the portal vein, bypassing lymphatics, reducing chyle flow. "
"**Treatment**: diet modification, octreotide, pressure, and re-exploration or thoracic duct embolization for high output."),
),

"Deep Neck Abscess Drainage": dict(
overview=(
"Deep neck abscess drainage evacuates pus from neck spaces through transcervical or transoral approaches. "
"It requires airway planning and knowledge of fascial spaces and great vessel relationships."),
physiology=(
"**Fascial spaces**: contain infection until pressure or erosion spreads it. "
"**Carotid sheath**: lies within the space being drained. "
"**Transoral access**: suitable for medial collections (retropharyngeal, peritonsillar)."),
pathophysiology=(
"**Abscess**: walled-off pus with poor antibiotic penetration requires drainage. "
"**Phlegmon**: may respond to antibiotics. "
"**Approach selection**: medial collections transorally; lateral collections transcervically. "
"**Vessel risk**: carotid and jugular are at risk. "
"**Airway**: often secured before drainage."),
),

"Carotid Blowout Syndrome": dict(
overview=(
"Carotid blowout is rupture of the carotid artery or its branches, usually after radiation, surgery, wound breakdown, or tumor erosion. "
"It is often preceded by a sentinel bleed and is managed with pressure, airway control, and endovascular treatment."),
physiology=(
"**Arterial wall layers**: intima, media (smooth muscle and elastin, the main strength layer), and adventitia (collagen plus vasa vasorum). "
"**Vasa vasorum**: small vessels in the adventitia that nourish the outer media of large arteries. "
"**Soft-tissue coverage**: healthy, well-vascularized tissue around the carotid protects it from saliva, bacteria, and desiccation. "
"**Pressure load**: the carotid carries high systemic pressure, so any wall weakness can rupture."),
pathophysiology=(
"**Radiation and surgery**: devascularize the adventitia, weakening the wall. "
"**Wound breakdown and fistula**: saliva and infection erode the exposed artery. "
"**Classification**: threatened (exposed artery), impending (sentinel bleed), and acute (rupture) (Chaloupka et al., AJNR 1996). "
"**Management**: pressure, airway control (cuffed tube), resuscitation, and endovascular stenting or occlusion."),
),

"Esophageal Perforation / Cervical Mediastinitis": dict(
overview=(
"Esophageal perforation (iatrogenic, foreign body, Boerhaave) leaks contents into the neck and mediastinum, causing rapidly progressive infection. "
"Early diagnosis and drainage reduce high mortality."),
physiology=(
"**No serosa**: unlike the stomach and intestine, the esophagus lacks a serosal layer, so leaks are not contained. "
"**Killian dehiscence**: a weak triangle between the thyropharyngeus and cricopharyngeus, a common site of instrument perforation. "
"**Fascial continuity**: the retropharyngeal and danger spaces connect the neck to the posterior mediastinum. "
"**Saliva and gastric contents**: carry heavy bacterial loads and digestive enzymes."),
pathophysiology=(
"**Iatrogenic perforation**: endoscopy and dilation, most often near the cricopharyngeus (Killian dehiscence). "
"**Boerhaave syndrome**: forceful vomiting ruptures the distal esophagus. "
"**Mediastinitis**: saliva, bacteria, and gastric contents cause necrotizing infection. "
"**Signs**: pain, crepitus, fever, and pneumomediastinum. "
"**Treatment**: NPO, antibiotics, drainage, and repair."),
),

"ENT Perioperative Anesthesia / Difficult Airway Planning": dict(
overview=(
"Airway planning in ENT anticipates difficult mask ventilation, intubation, and surgical airway, coordinating with anesthesia. "
"Shared airway cases and obstructing pathology demand clear plans."),
physiology=(
"**Airway assessment**: Mallampati, mouth opening, thyromental distance, neck mobility. "
"**Oxygen reserve**: preoxygenation extends safe apnea time. "
"**Spontaneous ventilation**: maintains airway patency in obstructing lesions."),
pathophysiology=(
"**Obstructing tumors**: induction removes muscle tone and can convert partial to complete obstruction. "
"**Spontaneous ventilation**: preserved in awake techniques to maintain airway patency. "
"**Awake approaches**: awake fiberoptic intubation or awake tracheostomy under local anesthesia. "
"**Can't intubate, can't oxygenate**: emergency front-of-neck access via cricothyroidotomy. "
"**Shared airway**: surgeon and anesthesiologist coordinate ventilation strategy."),
),

"Hemostasis / Coagulopathy / Antithrombotic Management in ENT": dict(
overview=(
"Perioperative hemostasis requires assessing bleeding risk, managing antithrombotics, and recognizing coagulopathy. "
"Head and neck surgery has bleeding complications that can obstruct the airway."),
physiology=(
"**Primary hemostasis**: von Willebrand factor tethers platelets to exposed collagen, and platelets aggregate via thromboxane A2 and ADP. "
"**Secondary hemostasis**: the coagulation cascade converges on thrombin, which converts fibrinogen to fibrin. "
"**Fibrinolysis**: plasmin breaks down clot; tranexamic acid inhibits this. "
"**Mucosal surfaces**: the nose and pharynx have high fibrinolytic activity, which favors bleeding."),
pathophysiology=(
"**Antiplatelets**: aspirin irreversibly inhibits COX-1; clopidogrel blocks P2Y12. "
"**Anticoagulants**: warfarin (vitamin K antagonist), DOACs (factor Xa or thrombin inhibitors). "
"**von Willebrand disease**: most common inherited bleeding disorder. "
"**Bridging**: depends on thrombotic risk. "
"**Reversal**: vitamin K and four-factor PCC for warfarin, idarucizumab for dabigatran, and PCC for factor Xa inhibitors in the US (andexanet alfa was withdrawn from the US market in December 2025). **Bridging**: most patients with atrial fibrillation do not need heparin bridging when warfarin is held (CHEST 2022)."),
),
}
