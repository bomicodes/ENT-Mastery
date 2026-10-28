"""v47.1 authored Concept Checks — General ENT / Emergencies (part D)."""

CHECKS = [
("ENT Imaging Fundamentals",
 "A 40-year-old with chronic otorrhea and prior mastoidectomy has a middle-ear soft-tissue mass on CT. On MRI, the mass shows bright signal on diffusion-weighted imaging (restricted diffusion). What does this suggest?",
 "Recurrent cholesteatoma",
 [("Postoperative granulation tissue", "Granulation tissue does not restrict diffusion and enhances on delayed contrast imaging."),
  ("Simple serous effusion", "Fluid does not restrict diffusion."),
  ("Cholesterol granuloma", "Cholesterol granuloma is bright on T1 and T2 rather than restricting diffusion.")],
 "Keratin in cholesteatoma restricts water diffusion, appearing bright on non-echo-planar DWI. This allows imaging surveillance after canal-wall-up surgery and can avoid some second-look operations.",
 "Restricted diffusion in the middle ear after surgery = recurrent cholesteatoma."),

("Wound Healing / Scar Biology in Head & Neck Surgery",
 "A patient who smokes a pack a day and had neck radiation 2 years ago develops wound breakdown and a fistula after salvage neck surgery. What single mechanism do both risk factors share?",
 "Reduced oxygen delivery to the wound",
 [("Excess collagen synthesis causing tension", "Both factors impair, rather than increase, collagen synthesis."),
  ("An exaggerated inflammatory phase", "Both blunt effective healing; neither speeds closure through inflammation."),
  ("Hypersensitivity to suture material", "Suture allergy is rare and unrelated to smoking or radiation.")],
 "Smoking causes vasoconstriction and carbon monoxide binding to hemoglobin; radiation causes obliterative endarteritis and fibrosis. Fibroblast collagen synthesis, angiogenesis, and neutrophil killing all depend on oxygen, so both impair healing; vascularized flaps help in irradiated beds.",
 "Wound healing needs oxygen: smoking and radiation both starve it."),

("Grafts / Implants / Biomaterials in ENT",
 "One year after dorsal augmentation with a porous polyethylene implant, a patient with thin dorsal skin develops redness and then exposure of the implant. Why did it fail?",
 "Thin cover cannot protect an alloplast",
 [("Porous implants are rejected by antibodies", "Immunologic rejection is not the usual mechanism of alloplast failure."),
  ("The implant resorbed and shifted", "Porous polyethylene does not resorb."),
  ("The implant was too vascularized", "Tissue ingrowth helps stability; inadequate coverage is the problem.")],
 "Alloplastic implants depend on thick, well-vascularized soft tissue cover. Thin, scarred, or irradiated skin lets implants become exposed, colonized by biofilm, and extrude. Autologous cartilage tolerates thin coverage better.",
 "Alloplasts need generous, healthy coverage."),

("Systemic / Granulomatous Disease Manifestations in ENT",
 "A 35-year-old has bilateral parotid enlargement, uveitis, fever, and facial nerve palsy. What is the diagnosis?",
 "Sarcoidosis (Heerfordt)",
 [("Sjögren syndrome", "Sjögren causes gland enlargement and dryness but not facial palsy with uveitis."),
  ("Mumps parotitis", "Mumps is acute viral parotitis without uveitis."),
  ("Parotid lymphoma", "Lymphoma would not cause uveitis and fever in this pattern.")],
 "Uveoparotid fever (Heerfordt syndrome) is a form of sarcoidosis with noncaseating granulomas involving parotid glands, uvea, and facial nerve.",
 "Parotid enlargement + uveitis + facial palsy = sarcoidosis."),

("Common ENT Consult Triage / Disposition",
 "Four ENT consults arrive at once: a stable peritonsillar abscess, a closed nasal fracture, uncomplicated otitis externa, and a facial trauma patient with a tense proptotic eye and worsening vision. Which needs attention first?",
 "The proptotic, failing eye",
 [("The stable peritonsillar abscess", "A stable PTA needs drainage soon, but vision can be lost within minutes."),
  ("The closed nasal fracture", "Nasal fractures are typically reduced days later after swelling settles."),
  ("The uncomplicated otitis externa", "Otitis externa is treated as an outpatient.")],
 "Retrobulbar hematoma causes optic nerve ischemia and permanent vision loss within about 90 minutes, so lateral canthotomy and cantholysis take priority. Triage by what can be lost irreversibly in minutes: airway, vision, and uncontrolled bleeding.",
 "Airway, vision, bleeding: triage by what can be lost in minutes."),

]
