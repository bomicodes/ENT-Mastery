DUPS = [
  # 0
  {"mode": "distinct", "qids": ["v490-facial-plastics-1-26", "v113-rhi-02"], "fronts": {
    "v113-rhi-02": "CT/MRI after frontal fracture: expansile, smoothly remodeled sinus, nonenhancing contents, rim enhancement only: diagnosis?"}},
  # 1
  {"mode": "merge", "keep": "v490-facial-plastics-1-5", "aliases": ["v490-rhinology-1-35", "v490-sleep-1-103"],
   "front": "Wide nasal airway that feels blocked, dry and crusted after turbinate resection, cotton test positive: diagnosis?"},
  # 2
  {"mode": "merge", "keep": "v490-rhinology-2-104", "aliases": ["v490-facial-plastics-1-40"],
   "front": "Validated questionnaire to document nasal obstruction severity before and after functional nasal surgery?"},
  # 3
  {"mode": "distinct", "qids": ["v490-facial-plastics-2-32", "v490-otology-3-90"], "fronts": {}},
  # 4
  {"mode": "merge", "keep": "v490-topup-general-11", "aliases": ["v490-pediatric-3-11"],
   "front": "Equivocal foreign body aspiration history in a stable child with normal or nonspecific chest films: next test?"},
  # 5
  {"mode": "merge", "keep": "v490-otology-3-83", "aliases": ["v490-general-ent-1-93"], "front": None},
  # 6
  {"mode": "merge", "keep": "lab_fn_topo_v532", "aliases": ["v490-general-ent-1-94"],
   "front": "Peripheral facial palsy with reduced ipsilateral tearing (plus absent stapedial reflex, reduced taste): lesion level?"},
  # 7
  {"mode": "merge", "keep": "v490-general-ent-1-96", "aliases": ["img_tb11"],
   "front": "Smooth expansile petrous apex lesion, bright on T1 and T2, no fat suppression, no restricted diffusion: diagnosis?"},
  # 8
  {"mode": "distinct", "qids": ["v490-general-ent-1-77", "v490-general-ent-1-24"], "fronts": {}},
  # 9
  {"mode": "merge", "keep": "v501-general-ent-eagle-6", "aliases": ["v490-topup-thyroid-35"],
   "front": "Paroxysmal electric throat and ear pain triggered by every swallow, pain-free between attacks: diagnosis?"},
  # 10
  {"mode": "merge", "keep": "v490-topup-general-1", "aliases": ["v490-general-ent-1-1"], "front": None},
  # 11
  {"mode": "merge", "keep": "v490-head-neck-1-52", "aliases": ["v490-head-neck-2-86"], "front": None},
  # 12
  {"mode": "distinct", "qids": ["v490-head-neck-1-54", "v490-topup-headneck-5", "v490-rhinology-4-51"], "fronts": {
    "v490-rhinology-4-51": "Krouse stage: inverted papilloma limited to the OMC, ethmoid or medial maxillary wall?"}},
  # 13
  {"mode": "distinct", "qids": ["img_path_dlbcl_v44", "v490-head-neck-1-102"], "fronts": {}},
  # 14
  {"mode": "merge", "keep": "v431-slnb-oral-cavity-01", "aliases": ["v490-head-neck-1-23"],
   "front": "cT1-T2 N0 oral cavity SCC: accepted neck staging alternative to elective neck dissection?"},
  # 15
  {"mode": "distinct", "qids": ["v490-head-neck-1-43", "v490-rhinology-1-91"], "fronts": {}},
  # 16
  {"mode": "distinct", "qids": ["v490-head-neck-1-34", "v490-topup-thyroid-1"], "fronts": {}},
  # 17
  {"mode": "distinct", "qids": ["v490-laryngology-2-4", "v490-laryngology-1-4"], "fronts": {}},
  # 18
  {"mode": "distinct", "qids": ["img_lx_epiglottic_cyst_v532", "img_aw_vallecularcyst_v532"], "fronts": {}},
  # 19
  {"mode": "distinct", "qids": ["img_sw_cp_bar_v532", "img_sw_zenker_v532", "v490-laryngology-1-61"], "fronts": {}},
  # 20
  {"mode": "distinct", "qids": ["v490-laryngology-2-27", "v490-pediatric-2-65"], "fronts": {}},
  # 21
  {"mode": "distinct", "qids": ["v124_oto_01", "v490-topup-otology-22"], "fronts": {}},
  # 22
  {"mode": "merge", "keep": "v490-otology-2-25", "aliases": ["v490-otology-1-31"], "front": None},
  # 23
  {"mode": "merge", "keep": "v431-ansd-01", "aliases": ["v490-otology-1-109", "v490-pediatric-1-21"], "front": None},
  # 24
  {"mode": "distinct", "qids": ["v490-otology-2-96", "img_pc_choanal_atresia_ct_v532"], "fronts": {}},
  # 25
  {"mode": "merge", "keep": "v124_oto_10", "aliases": ["v490-otology-1-42"], "front": None},
  # 26
  {"mode": "merge", "keep": "v490-otology-2-12", "aliases": ["v490-otology-3-97"], "front": None},
  # 27
  {"mode": "distinct", "qids": ["v490-otology-3-89", "v490-rhinology-5-4"], "fronts": {}},
  # 28
  {"mode": "distinct", "qids": ["lab_fn_hb_v532", "img_aw_sgs_grade3_v532", "v490-pediatric-2-45"], "fronts": {}},
  # 29
  {"mode": "distinct", "qids": ["lab_v9", "v490-otology-1-80"], "fronts": {}},
  # 30
  {"mode": "merge", "keep": "v490-otology-3-43", "aliases": ["v490-otology-1-23"],
   "front": "CPA mass with broad dural base, obtuse angle, dural tail, hyperostosis or calcification, normal IAC: diagnosis?"},
  # 31
  {"mode": "merge", "keep": "v490-otology-1-20", "aliases": ["v490-otology-3-45"],
   "front": "Small lateral intracanalicular vestibular schwannoma reaching the fundus, good hearing: surgical approach?"},
  # 32
  {"mode": "distinct", "qids": ["v490-otology-3-7", "v490-rhinology-5-53"], "fronts": {}},
  # 33
  {"mode": "merge", "keep": "v490-otology-1-74", "aliases": ["v490-pediatric-2-50"],
   "front": "Toddler with brief recurrent frightened vertigo spells, normal hearing and normal between attacks, family migraine: diagnosis?"},
  # 34
  {"mode": "merge", "keep": "v490-otology-1-79", "aliases": ["v490-otology-3-34"], "front": None},
  # 35
  {"mode": "merge", "keep": "v490-pediatric-3-49", "aliases": ["v490-sleep-1-86"],
   "front": "Teen boy with recurrent hypersomnia episodes plus hyperphagia or cognitive change, normal between: diagnosis?"},
  # 36
  {"mode": "distinct", "qids": ["v119-allergy-05", "v490-rhinology-1-17"], "fronts": {}},
  # 37
  {"mode": "distinct", "qids": ["v490-rhinology-1-70", "v490-rhinology-5-30"], "fronts": {}},
  # 38
  {"mode": "merge", "keep": "v490-rhinology-5-19", "aliases": ["v490-rhinology-3-9"],
   "front": "JNA: where does recurrence arise, so which areas must be drilled at the first operation?"},
  # 39
  {"mode": "distinct", "qids": ["v490-rhinology-5-34", "v490-rhinology-4-48"], "fronts": {}},
  # 40
  {"mode": "merge", "keep": "lab_allergy5", "aliases": ["v119-allergy-04"],
   "front": "Allergic-type rhinitis to a specific trigger, negative skin and serum IgE, positive nasal allergen challenge: diagnosis?"},
  # 41
  {"mode": "merge", "keep": "v490-sleep-1-105", "aliases": ["v119-allergy-06"],
   "front": "Escalating topical decongestant (oxymetazoline) use with brief relief, rebound congestion, beefy red turbinates: diagnosis?"},
  # 42
  {"mode": "distinct", "qids": ["v490-sleep-1-49", "v490-gap-fill-1-16"], "fronts": {}},
  # 43
  {"mode": "distinct", "qids": ["v490-thyroid-2-38", "v490-thyroid-1-41"], "fronts": {}},
  # 44
  {"mode": "distinct", "qids": ["img_path_mucoep_v43", "v490-thyroid-1-13"], "fronts": {}},
  # 45
  {"mode": "distinct", "qids": ["img_path_pleomorphic_v43", "v490-topup-thyroid-28"], "fronts": {}},
  # v69.0 duplicate sweep
  {"mode": "merge", "keep": "v490-topup-general-19", "aliases": ["v490-pediatric-1-16"], "front": None},
  {"mode": "merge", "keep": "v490-laryngology-2-47", "aliases": ["v490-gap-fill-2-47"], "front": None},
  {"mode": "merge", "keep": "v116-lar-03", "aliases": ["img_lx_uvfp_ortner_v532"], "front": None},
  # v69.0 retired duplicate questions: their cards merge into the kept question's cards
  {"mode": "merge", "keep": "v490-facial-plastics-1-40", "aliases": ["v490-rhinology-2-104"], "front": None},
  {"mode": "merge", "keep": "v490-rhinology-1-46", "aliases": ["v490-facial-plastics-1-41"], "front": None},
  {"mode": "merge", "keep": "v490-rhinology-1-35", "aliases": ["v490-facial-plastics-1-5", "v490-sleep-1-103"], "front": None},
  {"mode": "merge", "keep": "v490-gap-fill-1-46", "aliases": ["v490-topup-facial-31"], "front": None},
  {"mode": "merge", "keep": "v490-general-ent-1-1", "aliases": ["v490-topup-general-1"], "front": None},
  {"mode": "merge", "keep": "v490-general-ent-1-6", "aliases": ["v490-pediatric-1-71"], "front": None},
  {"mode": "merge", "keep": "v490-rhinology-5-76", "aliases": ["v490-general-ent-1-92"], "front": None},
  {"mode": "merge", "keep": "v490-thyroid-1-15", "aliases": ["v490-head-neck-2-38"], "front": None},
  {"mode": "merge", "keep": "v490-head-neck-2-53", "aliases": ["v490-rhinology-1-89"], "front": None},
  {"mode": "merge", "keep": "v490-thyroid-2-6", "aliases": ["v490-head-neck-2-97", "v490-head-neck-1-77"], "front": None},
  {"mode": "merge", "keep": "v490-pediatric-1-21", "aliases": ["v490-otology-1-109"], "front": None},
  {"mode": "merge", "keep": "v490-otology-1-20", "aliases": ["v490-otology-3-45"], "front": None},
  {"mode": "merge", "keep": "v490-otology-2-25", "aliases": ["v490-otology-1-31"], "front": None},
  {"mode": "merge", "keep": "v490-otology-1-38", "aliases": ["v490-otology-2-101"], "front": None},
  {"mode": "merge", "keep": "v490-otology-2-5", "aliases": ["v490-otology-3-23"], "front": None},
  {"mode": "merge", "keep": "v490-pediatric-1-11", "aliases": ["v490-pediatric-3-63"], "front": None},
  {"mode": "merge", "keep": "v490-sleep-1-86", "aliases": ["v490-pediatric-3-49"], "front": None},
  {"mode": "merge", "keep": "v490-rhinology-1-10", "aliases": ["v490-rhinology-2-81"], "front": None},
  {"mode": "merge", "keep": "v490-rhinology-1-61", "aliases": ["v490-rhinology-2-76"], "front": None},
  {"mode": "merge", "keep": "v490-rhinology-1-74", "aliases": ["v490-rhinology-5-77"], "front": None},
  {"mode": "merge", "keep": "v490-topup-general-29", "aliases": ["v490-rhinology-3-16"], "front": None},
  {"mode": "merge", "keep": "v490-rhinology-4-63", "aliases": ["v490-rhinology-5-74"], "front": None},
  {"mode": "merge", "keep": "v490-thyroid-1-5", "aliases": ["v490-topup-thyroid-18"], "front": None},
  {"mode": "merge", "keep": "v490-thyroid-1-69", "aliases": ["v490-thyroid-2-17"], "front": None},
]
