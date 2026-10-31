"""Atlas review fixes for corrections_atlas_part5a.csv (CONFLICT rows)."""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-peds-ltr.pimp5 (CONFLICT, Janfaza 1e p 583)
    ("peds-ltr",
     "Sixth arch in most board texts (the laryngeal cartilages other than the epiglottis arise from fused fourth and sixth arch mesenchyme, so some sources say fourth and sixth)",
     "Fused caudal arch mesenchyme: fourth and sixth arch by most board texts (Janfaza counts the laryngeal cartilages as fourth/fifth arch); the epiglottis instead arises from the hypobranchial eminence"),
    # A-tonsillectomy.supply2 (CONFLICT, Janfaza 1e p 379)
    ("tonsillectomy",
     "Paratonsillar (external palatine) vein to the pharyngeal plexus and facial vein",
     "Tonsillar branch of the lingual vein (chief drainage per Janfaza) and accessory tonsillar veins to the pharyngeal plexus; the paratonsillar (external palatine) vein drains the upper tonsillar bed, pierces the superior constrictor (to the pharyngeal plexus or facial vein by other texts) and may be the main source of post-tonsillectomy bleeding"),
    # A-tonsillectomy-adenoidectomy.supply2 (CONFLICT, Janfaza 1e p 379)
    ("tonsillectomy-adenoidectomy",
     "Paratonsillar (external palatine) vein in the lateral bed draining to the pharyngeal plexus and facial vein",
     "Tonsillar branch of the lingual vein (chief drainage per Janfaza) and accessory tonsillar veins to the pharyngeal plexus; the paratonsillar (external palatine) vein in the lateral (upper) bed pierces the superior constrictor (to the pharyngeal plexus or facial vein by other texts) and may be the main source of post-tonsillectomy bleeding"),
    # A-cervicofacial-flap.landmark2 (CONFLICT, Janfaza 1e p 44)
    ("cervicofacial-flap",
     "to about 1.5 cm above the lateral brow (Pitanguy line)",
     "to about 1.5-2 cm above the lateral brow (Pitanguy line; Janfaza uses 2 cm)"),
    # A-cervicofacial-flap.pimp5 (CONFLICT, Janfaza 1e p 44)
    ("cervicofacial-flap",
     "to about 1.5 cm above the lateral brow, approximating the frontal branch course",
     "to about 1.5-2 cm above the lateral brow (Janfaza uses 2 cm), approximating the temporal (frontal) branch course"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
