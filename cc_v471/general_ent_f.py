"""v47.1 authored Concept Checks — General ENT / Emergencies (part F)."""

CHECKS = [
("Lemierre Syndrome",
 "A 19-year-old has persistent fever and right neck tenderness 1 week after a sore throat. CT shows internal jugular vein thrombosis, and chest CT shows multiple cavitating nodules. Which organism is most likely?",
 "Fusobacterium necrophorum",
 [("Streptococcus pyogenes", "Group A strep causes pharyngitis but is not the classic cause of septic jugular thrombophlebitis."),
  ("Staphylococcus aureus", "S. aureus can cause septic emboli, but this syndrome is classically Fusobacterium."),
  ("Epstein-Barr virus", "EBV causes mononucleosis, not septic thrombophlebitis with cavitating emboli.")],
 "Pharyngeal infection spreads to the parapharyngeal space and causes septic thrombophlebitis of the internal jugular vein. Fusobacterium promotes platelet aggregation and thrombosis, seeding the lungs with septic emboli. Treatment is prolonged antibiotics.",
 "Sore throat, then neck tenderness and lung nodules = Lemierre syndrome."),

("Penetrating and Blunt Neck Trauma",
 "A stab wound to the left neck violates the platysma. The patient is stable, with no expanding hematoma, bleeding, stridor, or neurologic deficit. What is the modern initial evaluation?",
 "CT angiography of the neck",
 [("Mandatory neck exploration", "Mandatory exploration is reserved for hard signs or instability."),
  ("Discharge with outpatient follow-up", "Platysma violation requires evaluation for occult injuries."),
  ("Plain neck radiograph only", "Plain films are inadequate for vascular and aerodigestive injury.")],
 "The no-zone approach evaluates stable patients with CT angiography regardless of zone, reserving surgery for hard signs (expanding hematoma, pulsatile bleeding, air bubbling, airway compromise). Esophageal injury may need additional study.",
 "Stable penetrating neck trauma: CTA, not reflex exploration."),

("Cervical Necrotizing Fasciitis",
 "A diabetic patient with an odontogenic infection has rapidly spreading neck erythema with dusky skin, crepitus, and severe pain out of proportion to the exam. CT shows gas tracking along fascial planes. What is the essential treatment?",
 "Urgent wide surgical debridement",
 [("High-dose IV antibiotics alone", "Antibiotics cannot reach necrotic tissue without debridement."),
  ("Needle aspiration of the gas", "Necrotizing infection is not a drainable collection."),
  ("Hyperbaric oxygen as primary therapy", "Hyperbaric oxygen is at most an adjunct.")],
 "Polymicrobial infection spreads along fascia, thrombosing perforating vessels and causing skin necrosis and gas. Early radical debridement, repeated as needed, plus broad antibiotics reduce mortality.",
 "Pain out of proportion + crepitus + gas = necrotizing fasciitis: operate."),

("Ear and Nasal Foreign Body Removal",
 "A 3-year-old has had foul-smelling discharge from one nostril for 2 weeks. Exam shows a button battery in the anterior nasal cavity. Why must it be removed urgently?",
 "It causes rapid tissue necrosis",
 [("It will block the Eustachian tube", "Nasal batteries cause local necrosis rather than ear disease."),
  ("It causes sinusitis within minutes", "Sinusitis is not the main concern."),
  ("It will migrate into the brain", "Migration into the brain is not the mechanism of harm.")],
 "Button batteries generate hydroxide at the negative pole, causing liquefactive necrosis and septal perforation within hours. Unilateral foul discharge in a child suggests a foreign body.",
 "Button battery anywhere = emergency removal."),
]
