"""ENT Mastery v491 rewrites: Facial Plastics / Trauma (fps2)."""

REWRITES = {'v132_fprs_11': {'stem': 'A 76-year-old man undergoes wide excision of a recurrent cutaneous squamous cell '
                          'carcinoma of the vertex, leaving a 9 x 7 cm defect. Frozen sections are clear, '
                          'the pericranium is intact and bleeding briskly, and there is no exposed bone. He '
                          'has heart failure, wants a single short procedure, and the team wants an easily '
                          'surveilled site. Which reconstruction is most appropriate?',
                  'choices': ['Split-thickness skin graft from the thigh with a bolster',
                              'Full-thickness skin graft from the supraclavicular skin',
                              'Secondary-intention healing with moist dressings alone',
                              'Staged tissue expansion of the remaining hair-bearing scalp'],
                  'answer': 0,
                  'explanation': 'Intact, well-perfused pericranium is a vascular bed that supports graft '
                                 'take. A split-thickness graft has lower metabolic demand than a '
                                 'full-thickness graft, so it takes reliably, and a thigh donor can supply '
                                 'the large surface needed while healing by re-epithelialization. The thin, '
                                 'flat graft also allows easy clinical surveillance for recurrence in a '
                                 'high-risk cSCC. For a frail patient who wants one short operation, STSG is '
                                 'the practical choice; its poorer color match and lack of hair matter less '
                                 'than safety and monitoring.',
                  'why_wrong': ['Correct.',
                                'A full-thickness donor site must close primarily, so no supraclavicular '
                                'harvest can supply a 9 x 7 cm graft without creating a second large wound.',
                                'Pericranium can granulate, but a defect this large would need months of '
                                'dressing care in a frail patient, with prolonged open-wound risk.',
                                'Expansion needs several procedures over weeks to months, which conflicts '
                                'with his wish for a single short operation.'],
                  'board_pearl': 'Large scalp defect over intact pericranium: split-thickness graft gives '
                                 'reliable take, large coverage and easy surveillance.',
                  'curveball': 'At the end of the case you find a 2 x 2 cm island of bare calvarium where '
                               'the pericranium was resected with the tumor. Will the graft take there?',
                  'curveball_answer': 'No. Bare cortical bone without pericranium cannot vascularize a '
                                      'graft. Options are to elevate a local pericranial or galeal flap over '
                                      'the island before grafting, to burr the outer table down to bleeding '
                                      'diploe and allow granulation before delayed grafting, or to place a '
                                      'dermal regeneration template and graft once it vascularizes.'},
 'v147_fp_15': {'stem': 'A 63-year-old woman has a 1.2 cm defect of the left nasal sidewall after Mohs '
                        'surgery for a nodular basal cell carcinoma. The base is healthy, bleeding '
                        'subcutaneous tissue with intact perichondrium beneath, and the defect is shallow. '
                        'She does not smoke and prefers to avoid additional facial incisions. Which property '
                        'of a full-thickness graft makes it preferable to a split-thickness graft here?',
                'choices': ['Lower metabolic demand that tolerates a marginal recipient bed',
                            'Better skin match with less secondary contraction after healing',
                            'Donor site that re-epithelializes without needing primary closure',
                            'Larger surface area available from a single harvest site'],
                'answer': 1,
                'explanation': 'A full-thickness graft carries the entire dermis, which resists secondary '
                               'contraction and preserves texture, adnexal character and color closer to '
                               'native facial skin. On the nasal sidewall, near the medial canthus and alar '
                               'groove, contraction and a shiny, pale patch are the main aesthetic risks, so '
                               'the FTSG advantages matter. The trade-off is greater metabolic demand, which '
                               'this healthy, vascular, nonirradiated bed in a nonsmoker can support. '
                               'Preauricular or postauricular skin is a common donor.',
                'why_wrong': ['Lower metabolic demand is an advantage of the thinner split-thickness graft, '
                              'and her bed is healthy rather than marginal.',
                              'Correct.',
                              'Re-epithelialization of the donor site describes split-thickness harvest; a '
                              'full-thickness donor site generally must be closed primarily.',
                              'Large harvest area is a split-thickness advantage; FTSG size is limited by '
                              'how much donor skin can be closed primarily.'],
                'board_pearl': 'FTSG keeps full dermis: better facial match and less secondary contraction, '
                               'at the cost of needing a robust bed.',
                'curveball': 'When the tumor is cleared, a 5 mm patch of exposed cartilage without '
                             'perichondrium lies at the center of the defect. Can you still graft it?',
                'curveball_answer': 'A small bare cartilage area can sometimes be bridged by bed vessels '
                                    'from the surrounding perichondrium, but take over the center is '
                                    'unreliable. Options are to fenestrate the cartilage with small punch '
                                    'holes so vascular tissue can grow through, delay grafting until '
                                    'granulation covers it, or switch to a local flap if the bare area is '
                                    'larger.'},
 'v259_fpt_graft_fnd': {'stem': 'A 71-year-old man has a 2.5 cm Mohs defect of the right temple after '
                                'clearance of a basal cell carcinoma. The bed is healthy subcutaneous fat. '
                                'The junior resident proposes a split-thickness graft from the thigh because '
                                'it is quicker, while the attending prefers a full-thickness graft from the '
                                'supraclavicular skin. Which comparison correctly states the trade-off '
                                'between these grafts?',
                        'choices': ['STSG takes more easily but contracts more and matches poorly',
                                    'STSG contracts less after healing because it contains less dermis',
                                    'FTSG has lower metabolic demand and takes better on marginal beds',
                                    'FTSG shows more secondary contraction but gives a better color match'],
                        'answer': 0,
                        'explanation': 'Graft thickness changes biology. A split-thickness graft has less '
                                       'dermis, so it imbibes and revascularizes more easily and takes on '
                                       'less ideal beds, but it undergoes more secondary contraction and '
                                       'heals with pigment and texture mismatch. A full-thickness graft has '
                                       'more primary contraction at harvest but resists secondary '
                                       'contraction and gives a better facial match, at the cost of higher '
                                       'metabolic demand. With a healthy bed on a visible facial site, the '
                                       "attending's FTSG choice uses those strengths.",
                        'why_wrong': ['Correct.',
                                      'Less dermis means more secondary contraction, not less; dermis is the '
                                      'layer that resists wound contraction after healing.',
                                      'This reverses the biology: FTSG has higher metabolic demand and needs '
                                      'a robust bed, while STSG tolerates marginal beds better.',
                                      'FTSG has more primary contraction at harvest, but secondary '
                                      'contraction after healing is greater with STSG.'],
                        'board_pearl': 'Primary contraction is greater in FTSG; secondary contraction is '
                                       'greater in STSG because of less dermis.',
                        'curveball': 'He asks why the supraclavicular skin was chosen. Which donor sites '
                                     'best match facial skin for full-thickness grafts, and what drives the '
                                     'choice?',
                        'curveball_answer': 'Preauricular and postauricular skin match the face best in '
                                            'color and thickness and are favored for nasal and periocular '
                                            'defects; upper eyelid skin suits thin eyelid defects; '
                                            'supraclavicular skin offers more surface and acceptable color '
                                            'for larger facial defects. Choice depends on the size needed, '
                                            'the thickness and sebaceous quality of the recipient site, '
                                            'hair-bearing donor skin to avoid, and a donor site that closes '
                                            'primarily.'},
 'v259_fpt_graft_app': {'stem': 'A 58-year-old woman has a 1.8 cm Mohs defect of the upper left nasal '
                                'sidewall, 2 mm deep, after clearance of a superficial basal cell carcinoma. '
                                'Healthy perichondrium covers the entire base, and the defect does not '
                                'involve the alar rim, tip or medial canthus. She is a nonsmoker and wants a '
                                'single-stage repair with minimal added scars. Which reconstruction is most '
                                'reasonable?',
                        'choices': ['Preauricular full-thickness graft under a bolster',
                                    'Paramedian forehead flap with division at 3 weeks',
                                    'Bilobed transposition flap from the lower nasal dorsum',
                                    'Meshed split-thickness graft from the anterior thigh'],
                        'answer': 0,
                        'explanation': 'This defect is shallow, lies on the sidewall rather than a free '
                                       'margin, and has a vascularized perichondrial base, so it needs '
                                       'resurfacing rather than bulk or structural support. The concave '
                                       'sidewall accepts full-thickness grafts well, and preauricular skin '
                                       'gives a good color and thickness match in one stage without new '
                                       'nasal incisions. Success depends on close graft-to-bed contact, '
                                       'careful defatting, hemostasis and a bolster to prevent hematoma, '
                                       'seroma and shear during imbibition and inosculation.',
                        'why_wrong': ['Correct.',
                                      'A two-stage interpolated flap is excessive for a shallow sidewall '
                                      'defect and conflicts with her wish for a single-stage repair.',
                                      'A bilobed flap suits lower-third defects up to about 1.5 cm and adds '
                                      'incisions she wants to avoid on an upper sidewall.',
                                      'Meshed STSG leaves a pebbled, poorly matched surface with more '
                                      'contraction, which is unacceptable on a visible nasal subunit.'],
                        'board_pearl': 'Shallow nasal sidewall defect on healthy perichondrium: a bolstered '
                                       'preauricular FTSG gives single-stage, well-matched coverage.',
                        'curveball': 'On postoperative day 1 she asks how the graft survives before it has '
                                     'blood vessels. Describe the phases of graft take and their timing.',
                        'curveball_answer': 'During the first 24 to 48 hours the graft survives by plasmatic '
                                            'imbibition, absorbing nutrients from bed exudate. Inosculation '
                                            'follows around days 2 to 3, when graft and bed capillaries '
                                            'connect end to end. Revascularization with true vessel ingrowth '
                                            'and lymphatic drainage continues over the first week. Fluid or '
                                            'shear in this period breaks the contact all three phases need.'},
 'v259_fpt_graft_snr': {'stem': 'A 64-year-old woman has a 1.4 cm Mohs defect of the left ala that extends '
                                'through soft tissue and removes part of the lateral crus; the vestibular '
                                'lining is intact. The caudal edge lies 3 mm from the nostril margin, and '
                                'the remaining ala collapses on deep inspiration. She is otherwise healthy '
                                'and accepts staged surgery. Which reconstruction is most appropriate?',
                        'choices': ['Full-thickness preauricular skin graft placed directly on the remaining '
                                    'crus',
                                    'Composite helical root graft of skin and cartilage sutured into the '
                                    'defect',
                                    'Conchal cartilage batten graft with staged melolabial flap coverage',
                                    'Secondary-intention healing with a nostril stent worn during wound '
                                    'contracture'],
                        'answer': 2,
                        'explanation': 'Reconstruction must replace what is missing. This defect has lost '
                                       'structural support and lies near a free margin, so resurfacing alone '
                                       'will let the ala collapse and retract. A conchal cartilage batten or '
                                       'rim graft restores support for the external valve and resists '
                                       'contraction, and a vascularized melolabial interpolation flap gives '
                                       'the bulk and blood supply to nourish the cartilage and match alar '
                                       'thickness. A skin graft can resurface but cannot replace framework, '
                                       'and its secondary contraction would notch the rim.',
                        'why_wrong': ['A skin graft gives no structural support, and its contraction near '
                                      'the free margin would worsen alar retraction and valve collapse.',
                                      'Composite grafts are limited to small defects, generally around 1 cm, '
                                      'because they rely on diffusion; a deep 1.4 cm defect risks necrosis.',
                                      'Correct.',
                                      'Secondary intention works for concave sites, but near the alar free '
                                      'margin contraction pulls the rim upward despite stenting and leaves '
                                      'the valve unsupported.'],
                        'board_pearl': 'Alar defect with lost cartilage near the rim: replace support with '
                                       'cartilage and cover with a vascularized flap.',
                        'curveball': 'Which nasal areas are least forgiving of secondary contraction because '
                                     'they border the external nasal valve, and how is the rim protected?',
                        'curveball_answer': 'The alar rim, soft triangle and lower ala are free margins that '
                                            'border the external valve, so contraction there causes '
                                            'notching, retraction and inspiratory collapse. Surgeons protect '
                                            'the rim with nonanatomic alar rim or batten grafts under any '
                                            'coverage, use vascularized flaps rather than grafts for deeper '
                                            'defects, and avoid secondary intention within a few millimeters '
                                            'of the margin.'},
 'v132_fprs_12': {'stem': 'A 41-year-old woman has 2 years of right-sided nasal obstruction despite 3 months '
                          'of daily intranasal steroid. Anterior rhinoscopy shows the caudal septum deviated '
                          'into the right nostril. On deep inspiration the right upper lateral cartilage '
                          'moves toward the septum, and airflow improves when a curette supports the lateral '
                          'wall at the internal valve. Turbinates shrink normally with decongestant. Which '
                          'operation most directly treats both findings?',
                  'choices': ['Caudal septoplasty with inferior turbinate submucous reduction',
                              'Bilateral alar batten grafts without any septal surgery',
                              'Caudal septoplasty with bilateral spreader graft placement',
                              'Posterior submucous resection preserving the caudal strut'],
                  'answer': 2,
                  'explanation': 'Two fixed mechanisms explain her obstruction: caudal septal deviation '
                                 'narrowing the right nostril and dynamic internal valve collapse, confirmed '
                                 'by improvement with lateral wall support at the valve on modified Cottle '
                                 'testing. Caudal septoplasty repositions or reconstructs the caudal '
                                 'L-strut, and spreader grafts widen the valve angle and stiffen the upper '
                                 'lateral cartilages. Normal turbinate decongestion and failed steroid '
                                 'therapy point away from mucosal disease as the main problem.',
                  'why_wrong': ['Her turbinates decongest normally, and reduction does nothing for the valve '
                                'collapse confirmed on modified Cottle testing.',
                                'Batten grafts can support the lateral wall, but omitting septal surgery '
                                'leaves the caudal deviation that blocks the right nostril.',
                                'Correct.',
                                'Classic posterior resection leaves the caudal strut untouched, so the '
                                'caudal deviation and valve collapse both persist.'],
                  'board_pearl': 'Name each failed structure: caudal septum needs caudal septoplasty; '
                                 'internal valve collapse needs spreader-type support.',
                  'curveball': 'Six months later her internal valve looks open, but the right ala now '
                               'collapses at the nostril on deep inspiration. What structural cause should '
                               'you consider?',
                  'curveball_answer': 'This is external valve or lateral wall insufficiency, usually from '
                                      'weak, over-resected or cephalically malpositioned lateral crura. '
                                      'Check for prior cephalic trim and tip work. Treatment is structural: '
                                      'alar rim grafts, lateral crural strut grafts, alar batten grafts, or '
                                      'lateral crural repositioning, chosen according to which segment of '
                                      'the lateral wall collapses.'},
 'v141_fpt_05': {'stem': 'A 35-year-old man has worsening bilateral nasal obstruction 3 years after '
                         'rhinoplasty with dorsal hump reduction. Frontal view shows an inverted-V deformity '
                         'with a pinched middle third. On inspiration both upper lateral cartilages collapse '
                         'medially, and a modified Cottle maneuver at the internal valve relieves symptoms. '
                         'The septum is straight and turbinates decongest well. Which reconstruction best '
                         'addresses the mechanism?',
                 'choices': ['Bilateral spreader grafts to restore middle-vault width',
                             'Bilateral submucous reduction of the inferior turbinates',
                             'Lateral crural strut grafts beneath the lower laterals',
                             'Medial and lateral osteotomies to narrow the bony vault'],
                 'answer': 0,
                 'explanation': 'Hump reduction removes the roof that joins the upper lateral cartilages to '
                                'the dorsal septum. Without that support the cartilages fall medially, '
                                'narrowing the internal valve angle and producing the inverted-V deformity. '
                                'Spreader grafts placed between the dorsal septum and upper lateral '
                                'cartilages restore middle-vault width, reestablish the valve angle and '
                                'stiffen the sidewall. Because his septum is straight and turbinates '
                                'decongest normally, the fixed problem is the middle vault itself.',
                 'why_wrong': ['Correct.',
                               'His turbinates decongest normally, and reducing them does not reopen a '
                               'middle vault that has collapsed after roof removal.',
                               'Lateral crural struts support the lower lateral cartilages at the external '
                               'valve, not the collapsed upper laterals of the middle vault.',
                               'Osteotomies narrow the bony vault further and would worsen the pinched '
                               'middle third and internal valve narrowing.'],
                 'board_pearl': 'Inverted-V after hump reduction means middle-vault collapse; spreader '
                                'grafts restore width and the internal valve angle.',
                 'curveball': 'If his collapse were instead at the alar lobule with a normal middle vault, '
                              'which maneuvers treat external valve lateral-wall insufficiency?',
                 'curveball_answer': 'External valve collapse is treated by stiffening or repositioning the '
                                     'lateral wall at the nostril: alar batten grafts placed in a pocket '
                                     'over the area of maximal collapse, lateral crural strut grafts under '
                                     'weak crura, alar rim grafts for notching, or lateral crural '
                                     'repositioning when the crura are cephalically malpositioned. Spreader '
                                     'grafts do not reach this segment.'},
 'v260_fpt_fsr_fnd': {'stem': 'A 47-year-old woman has persistent bilateral nasal obstruction 2 years after '
                              'endonasal septoplasty. Exam shows the caudal septum dislocated off the nasal '
                              'spine into the left nostril, a drooping tip that lifts with improved '
                              'breathing, and both alae collapsing on gentle inspiration. The posterior '
                              'septum is straight, turbinates decongest normally, and topical steroids have '
                              'not helped. Which approach best fits her problem?',
                      'choices': ['Revision endonasal septoplasty of the bony and vomerine septum',
                                  'Radiofrequency reduction of both inferior turbinates',
                                  'Absorbable lateral wall implants without septal work',
                                  'Septorhinoplasty fixing caudal septum, tip and lateral walls'],
                      'answer': 3,
                      'explanation': 'Functional septorhinoplasty is chosen when obstruction comes from the '
                                     'nasal framework beyond the reach of an isolated septoplasty. Her '
                                     'caudal septal dislocation, loss of tip support and lateral wall '
                                     'collapse are fixed structural failures. Correction usually needs open '
                                     'or extended exposure to reposition or replace the caudal septum, '
                                     'restore tip support with a septal extension graft or strut, and '
                                     'support the lateral walls with rim, batten or strut grafts. Her '
                                     'straight posterior septum and normal turbinates explain why the first '
                                     'septoplasty failed.',
                      'why_wrong': ['Her bony septum is already straight; the dislocated caudal septum, tip '
                                    'ptosis and alar collapse would all remain.',
                                    'Her turbinates decongest normally, so turbinate reduction treats a '
                                    'mucosal problem she does not have.',
                                    'Implants can support the lateral wall, but they do not reposition the '
                                    'dislocated caudal septum or restore tip support.',
                                    'Correct.'],
                      'board_pearl': 'When obstruction arises from caudal septum, tip support or lateral '
                                     'wall, isolated septoplasty fails; septorhinoplasty addresses the '
                                     'framework.',
                      'curveball': 'Which traumatic nasal deformities typically require correction of both '
                                   'the septum and the external framework rather than septoplasty alone?',
                      'curveball_answer': 'The twisted C- or S-shaped nose with deviation of the bony '
                                          'pyramid and dorsal septum, the saddle nose after septal hematoma '
                                          'or L-strut fracture, caudal septal dislocation off the spine with '
                                          'tip deviation, and old malunited nasal bone fractures that narrow '
                                          'the internal valve. Each needs osteotomies, L-strut '
                                          'reconstruction, or grafting of the middle vault or tip, not only '
                                          'septal resection.'},
 'v260_fpt_fsr_app': {'stem': 'During open functional septorhinoplasty for a crooked nose in a 28-year-old '
                              'man with thin skin and short nasal bones, a 4 mm component dorsal hump '
                              'reduction is performed. The upper lateral cartilages separate from the septum '
                              'and fall medially, and the middle vault looks narrow after the dorsal septum '
                              'is straightened. Preoperatively he had internal valve collapse. Which step '
                              'best addresses this risk?',
                      'choices': ['Spreader grafts or flaps fixed between septum and upper laterals',
                                  'Trimming the excess upper lateral cartilage height along the dorsum',
                                  'Lateral osteotomies to close the open roof without further steps',
                                  'Onlay crushed cartilage camouflage placed over the middle vault'],
                      'answer': 0,
                      'explanation': 'Hump reduction separates the upper lateral cartilages from the dorsal '
                                     'septum. In a patient with short nasal bones, thin skin and preexisting '
                                     'valve collapse, unsupported cartilages heal medially into an '
                                     'inverted-V deformity with a narrow internal valve. Reconstituting the '
                                     'middle vault with spreader grafts, or autospreader flaps when upper '
                                     'lateral height allows, restores the septal-upper lateral relationship, '
                                     'widens the valve angle, splints the straightened dorsal septum and '
                                     'keeps dorsal aesthetic lines smooth.',
                      'why_wrong': ['Correct.',
                                    'Trimming upper lateral cartilage removes tissue that could serve as '
                                    'autospreader flaps and further weakens the valve.',
                                    'Osteotomies close the bony open roof but do not support the '
                                    'cartilaginous middle vault, which can still collapse inward.',
                                    'Camouflage hides an irregular contour on thin skin but does not widen '
                                    'or support the internal valve against collapse.'],
                      'board_pearl': 'After hump reduction, rebuild the middle vault with spreader grafts or '
                                     'flaps to prevent inverted-V and valve collapse.',
                      'curveball': 'His upper lateral cartilages have ample height after the hump is '
                                   'lowered. When are autospreader flaps reasonable, and when are separate '
                                   'grafts preferable?',
                      'curveball_answer': 'Autospreader flaps work when hump reduction leaves enough upper '
                                          'lateral height to fold inward, the dorsal septum is reasonably '
                                          'straight and the valve needs modest widening. Separate spreader '
                                          'grafts are better when there is no hump to lower, the dorsal '
                                          'septum is crooked and needs asymmetric splinting, collapse is '
                                          'severe, or the upper laterals are thin or damaged from prior '
                                          'surgery.'},
 'v260_fpt_fsr_snr': {'stem': 'A 52-year-old woman has bilateral nasal obstruction after two prior '
                              'septorhinoplasties. Exam shows severe caudal septal deviation, a ptotic tip '
                              'with poor recoil, and external valve collapse on quiet breathing. Palpation '
                              'and CT confirm almost no residual septal cartilage, and the conchal bowls '
                              'were harvested previously. She is a nonsmoker and wants both breathing and '
                              'shape improved. Which operative strategy is best?',
                      'choices': ['Costal cartilage caudal septal replacement with lateral wall support',
                                  'Porous polyethylene septal extension implant with tip suturing',
                                  'Caudal septal repositioning sutures with absorbable lateral wall implants',
                                  'Irradiated homologous rib struts for the tip and alar rims only'],
                      'answer': 0,
                      'explanation': 'Revision functional rhinoplasty with a depleted framework requires '
                                     'rebuilding rather than more reduction. A deviated, weak caudal septum '
                                     'must be replaced or reinforced to create a stable foundation for tip '
                                     'projection, and lateral wall collapse needs support with lateral '
                                     'crural strut, batten or rim grafts. With septum and conchae already '
                                     'used, autologous costal cartilage supplies the volume and strength '
                                     'needed. Rib warping is managed by carving balanced cross-sections or '
                                     'using laminated grafts.',
                      'why_wrong': ['Correct.',
                                    'Alloplastic implants in a scarred revision nose carry meaningful risks '
                                    'of infection and extrusion, and the lateral walls remain unsupported.',
                                    'Sutures cannot straighten or strengthen a caudal septum that is mostly '
                                    'absent, and implants alone will not restore tip support.',
                                    'Irradiated homograft is an option for some, but resorption is a concern '
                                    'and the deviated caudal septal foundation remains uncorrected.'],
                      'board_pearl': 'Revision with depleted septum: rebuild caudal support with costal '
                                     'cartilage; do not add more resection.',
                      'curveball': 'Her colleague suggests ear cartilage instead of rib. What trade-offs '
                                   'distinguish auricular from costal cartilage in major nasal '
                                   'reconstruction?',
                      'curveball_answer': 'Auricular cartilage is curved, flexible and limited in volume, '
                                          'with low donor morbidity; it suits alar rim, lateral crural and '
                                          'tip grafts but is weak for caudal septal replacement. Costal '
                                          'cartilage is abundant and strong, suited to septal extension, '
                                          'caudal replacement and dorsal grafts, but it warps, calcifies '
                                          'with age, and carries chest scar, pain and pneumothorax risk.'},
 'v137_fpt_01': {'stem': 'A 31-year-old woman requests reduction rhinoplasty. Standardized frontal, oblique, '
                         'lateral and basal photographs show a mild leftward tip deviation and a shorter '
                         'left hemiface with a lower left oral commissure, none of which she had noticed. '
                         'Septal examination is normal. She wants surgery in 2 months. What is the most '
                         'appropriate step regarding these findings?',
                 'choices': ['Plan asymmetric osteotomies to correct the hemifacial difference',
                             'Postpone the photographs until after her surgical consent',
                             'Avoid discussing the asymmetry to keep her anxiety down',
                             'Show her the asymmetry and record it in the consent discussion'],
                 'answer': 3,
                 'explanation': 'Standardized photographs create a reproducible record of baseline anatomy, '
                                'proportions and asymmetry. Facial asymmetry is common and is often first '
                                'noticed by patients after surgery, when it is easily blamed on the '
                                'operation. Reviewing the photographs with her before surgery shows what '
                                'rhinoplasty can and cannot change, sets realistic expectations, and '
                                'documents the preexisting state for planning and later comparison.',
                 'why_wrong': ['Nasal osteotomies cannot correct hemifacial skeletal asymmetry, and '
                               'promising this sets an expectation surgery cannot meet.',
                               'Photographs are taken before consent so findings shape the discussion; '
                               'delaying them removes their value in counseling.',
                               'Undisclosed asymmetry noticed after surgery is likely to be blamed on the '
                               'operation and erodes trust and consent quality.',
                               'Correct.'],
                 'board_pearl': 'Point out and document preexisting facial asymmetry before rhinoplasty; '
                                'patients often notice it only afterward.',
                 'curveball': 'Her photographs also show thick, sebaceous nasal skin. How does thick versus '
                              'thin skin change rhinoplasty planning and counseling?',
                 'curveball_answer': 'Thick, sebaceous skin hides framework changes, limits tip definition, '
                                     'swells longer and risks supratip fullness, so the framework must be '
                                     'strong and projecting, and skin care or isotretinoin may be '
                                     'considered. Thin skin shows every edge, so grafts are smoothed or '
                                     'camouflaged with crushed cartilage or fascia, and irregularities show '
                                     'early.'},
 'v147_fp_01': {'stem': 'A 38-year-old man asks for rhinoplasty because his nose looks too large. Lateral '
                        'photographs show a small dorsal hump, nasal length proportionate to the midface, '
                        'and a chin well behind a vertical line dropped from the lower lip. His lower face '
                        'is short, his skin is thick, and occlusion is Class I. What is the best principle '
                        'for his preoperative analysis?',
                'choices': ['Compare absolute nasal length and width with published millimeter norms',
                            'Assess the nose in the context of the whole face and envelope',
                            'Match his nose to a reference photograph he has brought in',
                            'Use computer morphing to set the target before measuring'],
                'answer': 1,
                'explanation': 'Aesthetic analysis is relational. A nose can look large because the chin is '
                               'retrusive or the lower third is short, while its own dimensions are '
                               'proportionate to the midface. Thick skin also limits how much refinement '
                               'will show. Analyzing the nose in context of facial thirds, profile, chin '
                               'projection, the skin envelope and his goals identifies where the imbalance '
                               'truly lies. Here it points toward the chin and lower face, not a large nasal '
                               'reduction.',
                'why_wrong': ['Absolute measurements ignore facial context; his nose is proportionate to the '
                              'midface, and the imbalance lies in the chin.',
                              'Correct.',
                              'A reference photo describes his goal but does not analyze his anatomy, skin '
                              'thickness or whether that result is achievable.',
                              'Morphing is a counseling aid after analysis; using it first skips the '
                              'structural diagnosis that should guide planning.'],
                'board_pearl': 'Analyze the nose in context: chin projection, facial thirds and skin '
                               'thickness change perceived nasal size.',
                'curveball': 'Explain to the resident how weak chin projection changes perceived nasal size '
                             'and why it matters for the plan.',
                'curveball_answer': 'A retrusive chin shortens the profile below the nose, so the nose '
                                    'dominates and looks overprojected. Advancing the chin balances the '
                                    'profile and makes the nose look smaller without changing it. Reducing a '
                                    'proportionate nose to fit a weak chin risks overresection, a scooped '
                                    'dorsum, valve problems and an unnatural result.'},
 'v262_fpt_analysis_fnd': {'stem': 'A 56-year-old woman requests neuromodulator for horizontal forehead '
                                   'lines. A single frontal photograph at rest shows well-positioned brows. '
                                   'On exam, when she relaxes her forehead with eyes closed, both brows drop '
                                   'below the orbital rim and upper eyelid skin hoods the lashes; she raises '
                                   'her brows constantly to see. Which part of the analysis matters most '
                                   'before treatment?',
                           'choices': ['Fitzpatrick skin type and photodamage grading of the forehead',
                                       'Brow position with the frontalis relaxed versus animated',
                                       'Glogau classification of static forehead wrinkles at rest',
                                       'Horizontal facial fifths measured on the frontal photograph'],
                           'answer': 1,
                           'explanation': 'Dynamic analysis separates resting anatomy from compensation. Her '
                                          'forehead lines come from chronic frontalis recruitment to lift '
                                          'heavy upper eyelid skin and ptotic brows off her visual axis. '
                                          'Weakening the frontalis would drop the brows and worsen hooding '
                                          'and the visual field. Comparing brow position with the frontalis '
                                          'relaxed and animated shows the true problem, which points to '
                                          'blepharoplasty or brow lift evaluation rather than forehead '
                                          'neuromodulator alone.',
                           'why_wrong': ['Skin type guides resurfacing and pigment risk but does not reveal '
                                         'that her lines come from compensatory brow elevation.',
                                         'Correct.',
                                         'Wrinkle grading describes severity but misses that frontalis '
                                         'activity is holding her brows up and must not be weakened.',
                                         'Facial fifths assess width proportion for nasal and eye analysis '
                                         'and do not address dynamic brow compensation.'],
                           'board_pearl': 'Analyze faces at rest and in animation; compensatory frontalis '
                                          'activity can mask brow ptosis and dermatochalasis.',
                           'curveball': 'She later asks about her profile as well. Which profile '
                                        'relationships are useful when evaluating nasal projection, chin '
                                        'projection and cervicomental balance?',
                           'curveball_answer': 'Useful profile measures include the nasofrontal angle and '
                                               'radix position, the nasolabial angle for rotation, the Goode '
                                               'ratio of tip projection to nasal length of about 0.55 to '
                                               '0.6, chin position relative to a vertical from the lower lip '
                                               'or a Frankfort-based zero meridian, and the cervicomental '
                                               'angle with hyoid position for neck definition.'},
 'v262_fpt_analysis_app': {'stem': 'A 26-year-old woman requests a smaller nose. Standardized profile '
                                   'photographs show a mild 2 mm dorsal hump, normal nasal length and '
                                   'rotation, and a chin lying 12 mm behind a vertical line from the lower '
                                   'lip. Occlusion is Class I with normal dentition, and the labiomental '
                                   'fold is normal. She has never considered her chin. What is the best '
                                   'counseling approach?',
                           'choices': ['Plan a large dorsal reduction to bring the profile into balance',
                                       'Refer for orthognathic surgery and mandibular advancement first',
                                       'Offer isolated chin augmentation and decline any nasal surgery',
                                       "Explain the chin's role and discuss combined conservative "
                                       'correction'],
                           'answer': 3,
                           'explanation': 'Facial aesthetics are relational. With normal occlusion, the '
                                          'retrusive chin reflects microgenia rather than mandibular '
                                          'retrognathia, and it makes a nearly proportionate nose look '
                                          'prominent. Showing her how chin projection affects perceived '
                                          'nasal size lets her choose between conservative rhinoplasty, chin '
                                          'augmentation with an implant or sliding genioplasty, or both. '
                                          'Aggressive nasal reduction to compensate for the chin would '
                                          'overcorrect the nose.',
                           'why_wrong': ['Reducing a nearly normal nose to offset a weak chin risks '
                                         'overresection and leaves the true imbalance uncorrected.',
                                         'With Class I occlusion this is microgenia; mandibular advancement '
                                         'is for skeletal malocclusion and is unnecessarily invasive here.',
                                         'She has a real, if mild, hump and nasal concern; refusing to '
                                         'discuss it ignores her stated goal.',
                                         'Correct.'],
                           'board_pearl': 'Normal occlusion with a weak chin suggests microgenia; consider '
                                          'chin augmentation before reducing a proportionate nose.',
                           'curveball': 'She asks to see computer morphs of combined surgery. How can '
                                        'morphing help counseling without becoming a guarantee of the '
                                        'outcome?',
                           'curveball_answer': 'Use conservative morphs based on her own standardized '
                                               'photographs to show direction and proportion, not exact '
                                               'results. State, document and have her acknowledge that '
                                               'morphs are communication tools, not promises. Avoid changes '
                                               'beyond what tissue and skin thickness allow, and use the '
                                               'session to test whether her goals are realistic.'},
 'v262_fpt_analysis_snr': {'stem': 'A 33-year-old man requests a third revision rhinoplasty. On examination '
                                   'and standardized photographs his nose is straight with only a 1 mm alar '
                                   'asymmetry. He reports checking mirrors for several hours a day, avoiding '
                                   'work meetings, and says two prior surgeons ruined his life. He rejects '
                                   'any explanation of normal asymmetry. What is the best decision?',
                           'choices': ['Perform a limited alar revision under local anesthesia to restore '
                                       'confidence',
                                       'Proceed with revision once a second surgeon confirms the asymmetry',
                                       'Offer filler camouflage of the asymmetry as a low-risk trial',
                                       'Defer surgery, screen for body dysmorphic disorder and refer for '
                                       'care'],
                           'answer': 3,
                           'explanation': 'His distress, time spent checking, social avoidance and blame of '
                                          'prior surgeons are out of proportion to a minimal deformity, '
                                          'which strongly suggests body dysmorphic disorder. Patients with '
                                          'BDD rarely improve after cosmetic procedures and often shift '
                                          'preoccupation, seek more surgery, or become hostile. Safe '
                                          'practice is to screen with a validated tool, decline or defer '
                                          'elective surgery, and refer for psychiatric care, where cognitive '
                                          'behavioral therapy and SSRIs are effective.',
                           'why_wrong': ['Even a small revision reinforces the preoccupation and rarely '
                                         'relieves BDD symptoms, which often worsen or shift afterward.',
                                         'A second opinion on a 1 mm asymmetry does not address his '
                                         'disproportionate distress or the BDD contraindication.',
                                         'Filler is still a cosmetic procedure; it typically does not '
                                         'relieve BDD and can feed further requests.',
                                         'Correct.'],
                           'board_pearl': 'Distress out of proportion to deformity suggests body dysmorphic '
                                          'disorder; screen and defer elective surgery.',
                           'curveball': 'Which history and behavioral features should prompt BDD screening '
                                        'at a first aesthetic consultation, before any revision request?',
                           'curveball_answer': 'Red flags include minimal or imperceptible deformity with '
                                               'severe distress, hours spent on mirror checking or '
                                               'camouflage, avoidance of work or social contact, many prior '
                                               'procedures or surgeon shopping, vague or shifting goals, '
                                               'unrealistic demands for perfection, and hostility toward '
                                               'prior surgeons. Validated tools such as the BDDQ-AS help.'},
 'v137_fpt_02': {'stem': 'A 49-year-old woman with Fitzpatrick type II skin wants to look less tired. She '
                         'has deep vertical glabellar lines when she frowns that largely soften at rest, '
                         'plus fine crosshatched rhytids, rough texture and scattered lentigines across both '
                         'cheeks. Midface volume and jawline are well preserved, and she has no history of '
                         'herpes labialis or keloids. Which treatment plan best matches mechanism to '
                         'modality?',
                 'choices': ['Glabellar hyaluronic filler with topical tretinoin alone',
                             'Lower-face rhytidectomy with glabellar neuromodulator',
                             'Glabellar neuromodulator with fractional laser resurfacing',
                             'Cheek calcium hydroxylapatite with a superficial peel'],
                 'answer': 2,
                 'explanation': 'Treatment should match the layer causing each problem. Her glabellar lines '
                                'are dynamic, produced by corrugator and procerus contraction, so a '
                                'neuromodulator that weakens those muscles is the targeted fix. Her cheek '
                                'findings are photodamage of the epidermis and superficial dermis, which '
                                'respond to skin-directed resurfacing such as fractional laser. Volume loss '
                                'and tissue descent are absent, so fillers and lifting address problems she '
                                'does not have. Fair skin lowers pigment risk from resurfacing.',
                 'why_wrong': ['Her glabellar lines are dynamic and soften at rest, and the glabella is a '
                               'high-risk filler site for vascular occlusion and vision loss.',
                               'She has a well-preserved jawline without jowling, so a facelift treats '
                               'laxity she does not have and leaves cheek photodamage untouched.',
                               'Correct.',
                               'Her midface volume is preserved, and a superficial peel is too shallow to '
                               'meaningfully improve crosshatched rhytids and texture.'],
                 'board_pearl': 'Match modality to layer: neuromodulator for dynamic lines, resurfacing for '
                                'photodamage, filler for volume, surgery for laxity.',
                 'curveball': 'Next year she asks for filler in the glabella for residual static lines. '
                              'Which vascular complication requires immediate recognition there, and why is '
                              'this site risky?',
                 'curveball_answer': 'The glabella carries one of the highest risks of arterial occlusion '
                                     'and blindness. Supratrochlear and supraorbital branches connect to the '
                                     'ophthalmic artery, so retrograde embolization can occlude the central '
                                     'retinal artery. Warning signs are immediate pain, blanching, livedo, '
                                     'and any visual change, ocular pain or ophthalmoplegia, which demands '
                                     'emergency ophthalmology involvement.'},
 'v147_fp_02': {'stem': 'A 57-year-old woman requests filler for deep nasolabial folds. Exam shows flattened '
                        'malar prominences, a visible lid-cheek junction and hollowing of the medial and '
                        'lateral cheek. When the cheek is lifted gently upward and outward with a fingertip, '
                        'the folds soften markedly. She also has fine rhytids and dyspigmentation. Which '
                        'plan best addresses her concern?',
                'choices': ['Layered high-volume filler placed directly into both folds',
                            'Deep midface volume restoration, then skin treatment as needed',
                            'Fractional ablative resurfacing alone to tighten the folds',
                            'Neuromodulator to the lip elevators to flatten the folds'],
                'answer': 1,
                'explanation': 'Her folds deepen because the midface has deflated and descended, which is '
                               'confirmed when lifting the cheek softens them. Restoring support in the deep '
                               'midface fat compartments and over the zygoma addresses the cause, often with '
                               'less total product than filling the crease, and lowers the bulk and '
                               'migration risk of overfilling the fold. Photodamage is a separate skin '
                               'problem treated with resurfacing or topical therapy. Vascular anatomy, '
                               'especially the angular and facial arteries, guides depth and technique.',
                'why_wrong': ['Overfilling the crease ignores midface deflation, creates heaviness, and '
                              'concentrates product near the facial and angular arteries.',
                              'Correct.',
                              'Resurfacing improves skin texture and fine lines but cannot restore lost '
                              'midface volume or lift the folds.',
                              'Weakening the lip elevators can flatten the upper lip and alter the smile, '
                              'and it does not restore cheek volume.'],
                'board_pearl': 'Deep nasolabial folds that soften with cheek lift reflect midface deflation; '
                               'restore support before filling the crease.',
                'curveball': 'She asks which facial regions are most dangerous for filler-related vision '
                             'loss. Which areas carry the greatest risk, and why?',
                'curveball_answer': 'The glabella, nasal dorsum and side, nasolabial fold, forehead and '
                                    'periorbital region are highest risk. Supratrochlear, supraorbital, '
                                    'dorsal nasal and angular arteries connect with the ophthalmic system, '
                                    'so retrograde flow from an injection can embolize the central retinal '
                                    'artery. Aspiration is unreliable; use low pressure, small aliquots, '
                                    'correct depth and cannulas where appropriate.'},
 'v262_fpt_aging_fnd': {'stem': 'A 62-year-old woman asks what has made her face look older over the past '
                                'decade. Exam shows thin, finely wrinkled skin, hollow temples, deep tear '
                                'troughs, descent of malar fat with jowling, perioral rhytids, and a less '
                                'defined mandibular border. She has not lost weight and is otherwise '
                                'healthy. Which explanation of her changes is most accurate?',
                        'choices': ['Gravity drawing skin down over an otherwise stable facial skeleton',
                                    'Loss of skin elasticity alone, with the deeper facial layers unchanged',
                                    'Combined change in skin, fat compartments, ligaments, muscle and bone',
                                    'Uniform fat hypertrophy that adds weight and heaviness to the lower '
                                    'face'],
                        'answer': 2,
                        'explanation': 'Facial aging is multilayered. Skin thins and loses elasticity, deep '
                                       'fat compartments atrophy while some superficial compartments '
                                       'descend, retaining ligaments attenuate so tissue slides, muscle '
                                       'activity etches dynamic lines, and the skeleton remodels with '
                                       'orbital enlargement, maxillary retrusion and mandibular resorption. '
                                       'Her temple and tear-trough hollowing, malar descent with jowling and '
                                       'perioral rhytids show several layers at once. Naming the dominant '
                                       'layer for each complaint guides treatment choice.',
                        'why_wrong': ['Gravity contributes to descent, but the facial skeleton itself '
                                      'remodels and recedes, reducing support for overlying soft tissue.',
                                      'Skin change explains fine wrinkles but not her temple hollowing, tear '
                                      'troughs or jowling, which come from deeper layers.',
                                      'Correct.',
                                      'Facial fat atrophies and shifts between compartments with age rather '
                                      'than hypertrophying uniformly, and she has not gained weight.'],
                        'board_pearl': 'Facial aging involves skin, fat compartments, ligaments, muscle and '
                                       'bone; treat the dominant layer for each complaint.',
                        'curveball': 'She asks which of her concerns are best treated by neuromodulator, by '
                                     'volumization and by resurfacing. How do you map them?',
                        'curveball_answer': 'Dynamic perioral and periorbital lines from muscle action '
                                            'respond to neuromodulator. Temple hollowing, tear troughs and '
                                            'malar deflation respond to volumization with filler or fat. '
                                            'Fine rhytids and thin, damaged skin respond to resurfacing. Her '
                                            'jowling and mandibular border laxity reflect tissue descent and '
                                            'are best addressed by surgical lifting.'},
 'v262_fpt_aging_app': {'stem': 'A 44-year-old woman receives hyaluronic acid filler to the glabella. Within '
                                'a minute she reports severe pain, and the skin above the right brow '
                                'blanches, then develops a reticulated violaceous pattern over the medial '
                                'forehead. Visual acuity, eye movements and pupils are normal, and she has '
                                'no headache or weakness. Which response is most appropriate now?',
                        'choices': ['Stop injecting and flood the ischemic area with high-dose hyaluronidase',
                                    'Apply warm compresses and nitroglycerin paste, then observe overnight',
                                    'Start oral prednisone and aspirin, then review her in clinic in 24 '
                                    'hours',
                                    'Massage the area firmly and reassess the skin color at 1 week'],
                        'answer': 0,
                        'explanation': 'Pain, blanching and livedo after filler signal arterial occlusion. '
                                       'Because the product is hyaluronic acid, the key step is to stop '
                                       'injecting and infiltrate generous hyaluronidase throughout the '
                                       'ischemic territory, repeating at short intervals until capillary '
                                       'refill and color return. Warm compresses, massage and aspirin are '
                                       'adjuncts. Vision and neurologic status must be rechecked repeatedly, '
                                       'because the glabella connects to the ophthalmic circulation and any '
                                       'visual change needs emergency ophthalmology care.',
                        'why_wrong': ['Correct.',
                                      'Warmth and topical vasodilators are adjuncts only; without '
                                      'hyaluronidase the occluding filler remains and skin necrosis can '
                                      'progress.',
                                      'Delaying treatment for 24 hours loses the window to reverse ischemia; '
                                      'steroids and aspirin do not dissolve the filler.',
                                      'Massage alone does not clear an intra-arterial embolus, and waiting a '
                                      'week allows full-thickness necrosis to develop.'],
                        'board_pearl': 'Pain and blanching after HA filler mean vascular occlusion: stop, '
                                       'flood with hyaluronidase, and monitor vision.',
                        'curveball': 'How would management change if the product were calcium '
                                     'hydroxylapatite, and which symptoms would demand immediate emergency '
                                     'transfer?',
                        'curveball_answer': 'Non-HA fillers cannot be dissolved, so care is supportive: stop '
                                            'injecting, warm compresses, massage, aspirin, close wound care '
                                            'and sometimes hyperbaric oxygen. Any visual loss, ocular pain, '
                                            'ptosis, ophthalmoplegia, or stroke signs such as weakness or '
                                            'speech change require immediate transfer for ophthalmology and '
                                            'stroke evaluation, whatever the product.'},
 'v262_fpt_aging_snr': {'stem': 'A 64-year-old woman with Fitzpatrick type II skin requests full-face and '
                                'neck carbon dioxide laser resurfacing to avoid surgery. She has deep '
                                'perioral rhytids and photodamage, but also marked jowling, loss of the '
                                'jawline, platysmal banding and loose submental skin. She has no smoking '
                                'history or prior facial procedures. What is the best counseling?',
                        'choices': ['Fully ablative resurfacing of the neck will tighten the platysmal bands',
                                    'Serial ablative passes along the jawline can tighten the jowls over '
                                    'time',
                                    'Jawline filler alone can substitute for lifting in her degree of laxity',
                                    'Resurfacing can improve her skin but will not correct jowls or neck '
                                    'laxity'],
                        'answer': 3,
                        'explanation': 'Resurfacing removes and remodels epidermis and dermis, improving '
                                       'texture, dyspigmentation and fine to moderate rhytids such as her '
                                       'perioral lines. It produces only modest skin tightening and cannot '
                                       'reposition descended SMAS, jowl fat or platysma. Her jowling, lost '
                                       'jawline and platysmal bands are structural and are best addressed by '
                                       'rhytidectomy and neck lift, possibly combined with perioral '
                                       'resurfacing. Neck skin heals poorly after aggressive ablation, so '
                                       'treatment there must be conservative.',
                        'why_wrong': ['Neck skin has few adnexal structures and heals poorly after fully '
                                      'ablative treatment, risking scarring; it does not tighten platysma.',
                                      'Repeated deep ablation increases scarring and hypopigmentation risk '
                                      'and still will not lift descended jowl tissue.',
                                      'Filler can refine a jawline in mild laxity, but her marked jowling '
                                      'and neck banding need lifting rather than volume.',
                                      'Correct.'],
                        'board_pearl': 'Resurfacing treats skin quality; jowling and platysmal banding are '
                                       'structural and need lifting.',
                        'curveball': 'Which patient factors increase the risk of postinflammatory '
                                     'hyperpigmentation, scarring or delayed healing after ablative '
                                     'resurfacing?',
                        'curveball_answer': 'Higher Fitzpatrick types and recent sun exposure raise '
                                            'hyperpigmentation risk. Recent isotretinoin, prior radiation, '
                                            'scleroderma or other collagen disease, keloid history, smoking, '
                                            'and prior deep resurfacing or facelift undermining reduce '
                                            'adnexal reserve or perfusion and slow healing. A herpes history '
                                            'requires antiviral prophylaxis, and the neck and chest need '
                                            'gentler settings.'},
 'v427-peels-depth-classification-01': {'stem': 'A 55-year-old woman with Fitzpatrick type II skin and '
                                                'moderate photodamage undergoes a Jessner solution plus 35% '
                                                'trichloroacetic acid peel. After the TCA application, the '
                                                'treated skin develops a uniform white frost with pink '
                                                'erythema still visible through it, and the skin wrinkles '
                                                'freely when gently pushed together. To which depth of '
                                                'injury does this endpoint correspond?',
                                        'choices': ['Stratum corneum and granular layer only',
                                                    'Full epidermis into the papillary dermis',
                                                    'Mid reticular dermis around adnexal bases',
                                                    'Deep reticular dermis near the subcutis'],
                                        'answer': 1,
                                        'explanation': 'Frost reflects coagulation of epidermal and dermal '
                                                       'proteins by TCA, and its appearance tracks depth. A '
                                                       'uniform white frost with erythema showing through is '
                                                       'the expected endpoint of a medium-depth peel such as '
                                                       'the Monheit Jessner-TCA combination, corresponding '
                                                       'to injury through the full epidermis into the '
                                                       'papillary dermis. Light, patchy frost indicates a '
                                                       'superficial peel, while a solid enamel-white frost '
                                                       'without pink warns of deeper penetration and greater '
                                                       'risk of scarring and pigment change.',
                                        'why_wrong': ['Injury limited to the stratum corneum and granular '
                                                      'layer produces only erythema or light, patchy '
                                                      'frosting, as in superficial peels.',
                                                      'Correct.',
                                                      'Mid reticular injury is the target of deep phenol '
                                                      'peels and would show a solid gray-white frost rather '
                                                      'than pink through frost.',
                                                      'Deep reticular injury exceeds safe peel depth and '
                                                      'would risk scarring; it does not match this '
                                                      'endpoint.'],
                                        'board_pearl': 'Medium-depth peels reach the papillary dermis; white '
                                                       'frost with pink showing through is the classic '
                                                       'endpoint.',
                                        'curveball': 'Why is 35% TCA typically combined with Jessner '
                                                     'solution or glycolic acid rather than used alone at '
                                                     'medium depth?',
                                        'curveball_answer': 'TCA alone at concentrations above about 35% '
                                                            'penetrates unevenly and carries a high risk of '
                                                            'scarring and pigment change. Priming with '
                                                            'Jessner solution in the Monheit peel or 70% '
                                                            'glycolic acid in the Coleman peel breaks the '
                                                            'epidermal barrier first, so a safer 35% TCA '
                                                            'reaches the papillary dermis evenly with a '
                                                            'controllable frost endpoint.'},
 'v427-peels-phenol-cardiac-monitoring-01': {'stem': 'A 66-year-old woman with Fitzpatrick type I skin and '
                                                     'deep perioral and periorbital rhytids is scheduled for '
                                                     'a full-face phenol-croton oil deep chemical peel. She '
                                                     'has hypertension controlled with amlodipine and normal '
                                                     'renal function. Compared with a TCA-based medium-depth '
                                                     'peel, which safety measure is specifically required '
                                                     'for this procedure?',
                                             'choices': ['Antiviral prophylaxis started before the peel and '
                                                         'continued through healing',
                                                         'Topical tretinoin priming for several weeks before '
                                                         'the day of the peel',
                                                         'Continuous ECG monitoring with IV fluids and '
                                                         'staged subunit application',
                                                         'Hydroquinone pretreatment to reduce '
                                                         'postinflammatory pigment change'],
                                             'answer': 2,
                                             'explanation': 'Phenol is rapidly absorbed through skin and is '
                                                            'directly cardiotoxic, causing arrhythmias, and '
                                                            'it is also hepatotoxic and nephrotoxic. A '
                                                            'full-face phenol-croton oil peel therefore '
                                                            'requires continuous cardiac monitoring, IV '
                                                            'access with hydration to promote phenol '
                                                            'excretion, and staged application by cosmetic '
                                                            'subunit with pauses between units to limit the '
                                                            'systemic load at any time. These precautions '
                                                            'are specific to phenol peels; antiviral '
                                                            'prophylaxis and skin priming apply to '
                                                            'medium-depth peels as well.',
                                             'why_wrong': ['Antiviral prophylaxis is standard for all medium '
                                                           'and deep peels, so it is not specific to phenol.',
                                                           'Tretinoin priming is used for many peel depths '
                                                           'to even penetration and speed healing; it is not '
                                                           'phenol-specific.',
                                                           'Correct.',
                                                           'Pigment-modifying pretreatment matters most in '
                                                           'darker skin and applies to other peels; it does '
                                                           'not address phenol toxicity.'],
                                             'board_pearl': 'Phenol peels are cardiotoxic: monitor ECG, '
                                                            'hydrate through an IV, and apply in staged '
                                                            'subunits.',
                                             'curveball': 'She took isotretinoin for acne 4 months ago. How '
                                                          'should this affect timing of her deep peel?',
                                             'curveball_answer': 'Traditional teaching is to wait roughly 6 '
                                                                 'to 12 months after isotretinoin before '
                                                                 'medium or deep peels or ablative '
                                                                 'resurfacing because of concern for '
                                                                 'impaired healing and atypical scarring. A '
                                                                 '2017 dermatologic surgery consensus found '
                                                                 'insufficient evidence to delay superficial '
                                                                 'procedures, but deferring a deep phenol '
                                                                 'peel remains the expected conservative '
                                                                 'answer.'},
 'v137_fpt_03': {'stem': 'A 45-year-old man has left nasal obstruction and a raised left nostril margin 2 '
                         'years after reduction rhinoplasty. The left alar rim sits 3 mm higher than the '
                         'right, and the left ala collapses on moderate inspiration. Vestibular lining is '
                         'supple with no scar band, and the left lateral crus feels thin and narrow. Another '
                         'surgeon offered to lower the right rim instead. Which treatment is most '
                         'appropriate?',
                 'choices': ['Excision of the right alar margin to match the higher left side',
                             'Left alar rim graft with lateral crural strut reinforcement',
                             'Left inferior turbinate reduction to widen the nasal airway',
                             'Further left cephalic trim to release the retracted alar rim'],
                 'answer': 1,
                 'explanation': 'His retraction and external valve collapse come from loss of lateral crural '
                                'support after overresection. With supple, adequate lining, the deficient '
                                'layer is cartilage, so the fix is to restore support: a lateral crural '
                                'strut graft stiffens the weak crus, and an alar rim graft along the margin '
                                'lowers and supports the rim against inspiratory collapse. Removing more '
                                'tissue on either side worsens obstruction or creates new asymmetry, and '
                                'turbinate work does not address the external valve.',
                 'why_wrong': ['Excising the normal side creates bilateral deformity and leaves the left '
                               'external valve unsupported and still collapsing.',
                               'Correct.',
                               'Turbinates do not cause external valve collapse at the nostril, and '
                               'reduction leaves the retracted, weak ala unchanged.',
                               'More cephalic trim further weakens the lateral crus, worsening retraction '
                               'and collapse rather than releasing it.'],
                 'board_pearl': 'Postrhinoplasty alar retraction with good lining: restore lateral crural '
                                'and rim support; do not resect more.',
                 'curveball': 'Which grafts can support the alar rim or a weak lateral crus, and how do they '
                              'differ?',
                 'curveball_answer': 'Alar rim grafts are thin cartilage strips in a pocket along the margin '
                                     'to correct mild retraction or notching. Lateral crural strut grafts '
                                     'are sutured under the crus to stiffen or reposition it. Alar batten '
                                     'grafts sit at the point of maximal collapse to splint the lateral '
                                     'wall. Composite grafts add lining when lining is short.'},
 'v147_fp_03': {'stem': 'A 39-year-old woman has bilateral nasal obstruction 1 year after rhinoplasty that '
                        'included alar base wedge excisions. Both nostrils are small and slit-like, narrowed '
                        'at the sill by firm, webbed scar. The lateral crura are strong, the alae do not '
                        'collapse on deep inspiration, and the internal valve opens normally. Which '
                        'reconstruction best addresses her obstruction?',
                'choices': ['Bilateral alar batten grafts to stiffen the lateral nasal walls',
                            'Release of sill scar with composite auricular graft inset',
                            'Scar excision at the sill with direct primary closure',
                            'Bilateral spreader grafts to widen the internal nasal valves'],
                'answer': 1,
                'explanation': 'Her obstruction is fixed vestibular stenosis at the sill after overresection '
                               'of alar base tissue, with normal lateral wall support and internal valve. '
                               'The deficient layer is skin and lining, so durable correction releases the '
                               'scar and adds tissue. A composite auricular graft of skin and cartilage '
                               'inset into the released sill restores lumen and resists recontracture. '
                               'Excising the scar and closing primarily removes more tissue, and grafts '
                               'aimed at the lateral wall or middle vault treat structures that are working.',
                'why_wrong': ['Her alae do not collapse, so stiffening the lateral walls does not enlarge a '
                              'sill narrowed by scar and tissue deficit.',
                              'Correct.',
                              'Primary closure after scar excision further shortens the deficient sill '
                              'tissue and tends to recontract into the same stenosis.',
                              'Her internal valves open normally; spreader grafts widen the middle vault, '
                              'not the scarred nostril sill.'],
                'board_pearl': 'Vestibular stenosis from tissue deficit needs added lining or skin; excising '
                               'scar alone recontracts.',
                'curveball': 'When is a composite auricular graft a good choice for nasal rim or vestibular '
                             'reconstruction, and what limits its use?',
                'curveball_answer': 'Composite grafts of conchal or helical skin and cartilage suit small '
                                    'defects of the alar rim, soft triangle, columella or sill that need '
                                    'both lining and support. They survive by diffusion from the edges, so '
                                    'size is limited to about 1 to 1.5 cm, the bed must be well '
                                    'vascularized, and smoking or prior radiation sharply reduces survival.'},
 'v262_fpt_alarstenosis_fnd': {'stem': 'A 44-year-old woman has new nasal obstruction 18 months after '
                                       'rhinoplasty for a wide tip. Her preoperative photographs show normal '
                                       'alar rims. The operative note describes aggressive cephalic trim '
                                       'leaving 3 mm rim strips. She now has bilateral alar notching and '
                                       'collapse of the alae on gentle inspiration. Intranasal lining is '
                                       'supple, and the middle vault is wide. Which structural problem is '
                                       'most likely?',
                               'choices': ['Weakened lateral crura from overresection during cephalic trim',
                                           'Cephalic malposition of the lateral crura present before surgery',
                                           'Middle-vault collapse from upper lateral cartilage '
                                           'disarticulation',
                                           'Vestibular lining contracture from an intranasal scar band'],
                               'answer': 0,
                               'explanation': 'Aggressive cephalic trim removes the lateral crural cartilage '
                                              'that supports the alar lobule. The thin remnants cannot '
                                              'resist inspiratory negative pressure, and scar contracture '
                                              'during healing pulls the rim upward, producing notching and '
                                              'external valve collapse. Her normal preoperative rims, the '
                                              'documented 3 mm remnants, supple lining and a wide middle '
                                              'vault place the failure in lateral crural support rather than '
                                              'in lining or the internal valve. Correction restores support '
                                              'with strut, rim or batten grafts.',
                               'why_wrong': ['Correct.',
                                             'Her preoperative photographs show normal rims, and the '
                                             'operative note documents overresection, so this is acquired '
                                             'rather than malposition.',
                                             'Her middle vault is wide, and collapse occurs at the alar '
                                             'lobule, which places the failure at the external valve.',
                                             'Her intranasal lining is supple without a scar band, so lining '
                                             'shortage is not the main mechanism here.'],
                               'board_pearl': 'Alar notching and collapse after aggressive cephalic trim '
                                              'reflect loss of lateral crural support.',
                               'curveball': 'Which bedside maneuvers help distinguish internal from external '
                                            'nasal valve collapse in this patient?',
                               'curveball_answer': 'Watch the nose on quiet and deep inspiration to see '
                                                   'whether collapse occurs at the alar lobule or at the '
                                                   'upper lateral cartilage. A modified Cottle maneuver, '
                                                   'supporting the lateral wall with a curette at each site '
                                                   'in turn, localizes the segment that relieves symptoms. '
                                                   'Anterior rhinoscopy and nasal endoscopy before and after '
                                                   'decongestion exclude septal and mucosal causes.'},
 'v262_fpt_alarstenosis_app': {'stem': 'A 48-year-old woman has right nasal obstruction after three prior '
                                       'rhinoplasties. The right alar rim is retracted 3 mm, a firm web of '
                                       'vestibular scar tethers the rim to the lateral crus, and the right '
                                       'ala collapses on inspiration. Pulling the rim down by hand is '
                                       'limited by the scar. She is a nonsmoker with healthy skin and no '
                                       'history of radiation. Which reconstructive plan is most appropriate?',
                               'choices': ['Scar release, lining graft and lateral crural or rim support',
                                           'Alar rim graft alone through a marginal pocket incision',
                                           'Scar release with silicone stenting and no cartilage support',
                                           'Vestibular Z-plasty of the scar band without cartilage grafts'],
                               'answer': 0,
                               'explanation': 'This revision has two deficient layers: lining shortened and '
                                              'tethered by scar, and inadequate lateral wall support. '
                                              'Durable correction releases the scar so the rim can descend, '
                                              'fills the resulting lining gap with a composite auricular or '
                                              'skin graft, and adds structural support with a lateral crural '
                                              'strut, rim or batten graft. Scar release without support '
                                              'tends to recontract, while support grafting without enough '
                                              'lining leaves the rim tethered and the vestibule narrow.',
                               'why_wrong': ['Correct.',
                                             'A rim graft alone cannot lower a rim tethered by vestibular '
                                             'scar because the shortened lining is still pulling it up.',
                                             'Stenting helps maintain release, but without cartilage support '
                                             'the weak ala still collapses and the rim tends to recontract.',
                                             'A Z-plasty can lengthen a narrow scar band but adds no '
                                             'support, so her inspiratory collapse would persist.'],
                               'board_pearl': 'Treat every deficient layer: release scar, replace lining and '
                                              'add support, or alar retraction recurs.',
                               'curveball': 'She admits she resumed smoking a pack a day before surgery. How '
                                            'does that change your reconstructive plan?',
                               'curveball_answer': 'Composite and free grafts depend on diffusion and '
                                                   'inosculation, which smoking impairs, so failure rises '
                                                   'sharply. Postpone elective surgery and require several '
                                                   'weeks of cessation, ideally confirmed. If she cannot '
                                                   'stop, favor vascularized lining such as a bipedicle '
                                                   'vestibular advancement or septal mucosal flap, keep '
                                                   'grafts small, and counsel her about higher recurrence '
                                                   'and necrosis risk.'},
 'v262_fpt_alarstenosis_snr': {'stem': 'A 29-year-old man has severe circumferential stenosis of the left '
                                       'nasal vestibule 1 year after a motorcycle crash with a degloving '
                                       'vestibular laceration. Six months ago, radial scar excision with 2 '
                                       'weeks of stenting reopened the vestibule, but it narrowed to a 3 mm '
                                       'opening within 6 weeks of stent removal. The lateral crus is intact. '
                                       'What is the best next step?',
                               'choices': ['Repeat radial scar excision with another 2 weeks of stenting',
                                           'Serial triamcinolone injections into the scar without release',
                                           'Alar batten graft to stiffen and open the left lateral wall',
                                           'Scar excision, lining replacement and months of stenting'],
                               'answer': 3,
                               'explanation': 'Rapid recurrence after release shows that the problem is a '
                                              'lining deficit; raw surfaces left to heal by contraction '
                                              'close the lumen again. The revision must change the biology '
                                              'by excising scar and resurfacing the vestibule with new '
                                              'lining, using a full-thickness skin or composite graft or '
                                              'local mucosal or melolabial flaps, then maintaining the lumen '
                                              'with a stent for several months while the scar matures. '
                                              'Cartilage support is added if the rim is weak, but his crus '
                                              'is intact.',
                               'why_wrong': ['Repeating the same release leaves a raw lining defect that '
                                             'will contract again, as it did after the first attempt.',
                                             'Steroid injection can soften scar but cannot recreate a lumen '
                                             'in severe circumferential stenosis that needs new lining.',
                                             'His lateral crus is intact; stiffening the wall does not add '
                                             'lining to a circumferentially scarred vestibule.',
                                             'Correct.'],
                               'board_pearl': 'Recurrent vestibular stenosis needs new lining plus prolonged '
                                              'stenting; repeating scar release alone fails.',
                               'curveball': 'Native vestibular skin and septal mucosa are scarce after his '
                                            'injury. Which lining options can be used instead?',
                               'curveball_answer': 'Options include full-thickness skin grafts from '
                                                   'postauricular or supraclavicular skin, composite '
                                                   'auricular grafts for smaller segments, buccal mucosal '
                                                   'grafts, inferior turbinate mucosal flaps, and turn-in '
                                                   'melolabial or nasolabial flaps for larger defects. Any '
                                                   'graft needs a vascular bed and stenting until it is '
                                                   'mature; vascularized flaps are preferred when the bed is '
                                                   'poor.'},
 'v137_fpt_04': {'stem': 'A 66-year-old man has a 1.0 cm round Mohs defect of the left supratip, 9 mm above '
                         'the alar rim, with intact perichondrium. The surrounding tip skin is moderately '
                         'thick, while the upper dorsum and sidewall are lax. The resident sketches a '
                         'bilobed flap with both lobes the same width as the defect and a 180-degree total '
                         'arc. Which lobe sizing is best?',
                 'choices': ['First lobe wider than the defect, second lobe equal to the first',
                             'Both lobes smaller than the defect, closed under deliberate tension',
                             'First lobe narrower than the defect, second lobe wider than the first',
                             'First lobe about the defect width, second lobe narrower and tapered'],
                 'answer': 3,
                 'explanation': 'In the modern Zitelli design the first lobe matches or is slightly smaller '
                                'than the defect, because the lax upper skin stretches into the rigid tip, '
                                'and the second lobe is narrower and elongated so its donor site closes '
                                'primarily in mobile dorsal or sidewall skin. Total rotation is reduced to '
                                'about 90 to 100 degrees. This sizing keeps tension away from the alar rim, '
                                'shrinks standing cones and lowers the risk of pincushioning and trapdoor '
                                'deformity.',
                 'why_wrong': ['An oversized first lobe bunches in the defect and promotes pincushioning, '
                               'and a large second lobe leaves a harder donor closure.',
                               'Undersized lobes put the repair under tension, which distorts the tip and '
                               'ala and risks distal flap necrosis.',
                               'An undersized first lobe leaves tension at the defect while a wider second '
                               'lobe enlarges the final donor wound unnecessarily.',
                               'Correct.'],
                 'board_pearl': 'Bilobed flap: first lobe near defect size, smaller tapered second lobe, '
                                'total arc about 90 to 100 degrees.',
                 'curveball': 'If the resident keeps the classic 180-degree total arc, which complications '
                              'become more likely?',
                 'curveball_answer': 'A wide arc creates larger standing cones at the pivot, more redundancy '
                                     'in each lobe and more pincushioning or trapdoor deformity, and it can '
                                     'pull the alar rim or tip off axis. Reducing the arc to about 90 to 100 '
                                     'degrees with wide submuscular undermining keeps the lobes flat and '
                                     'tension away from the free margin.'},
 'v147_fp_05': {'stem': 'A 69-year-old woman has a 1.2 cm Mohs defect of the left lateral nasal tip after '
                        'clearance of a basal cell carcinoma. The defect is superficial with intact '
                        'perichondrium, and its lower edge sits 8 mm from the alar rim. The tip skin is '
                        'moderately sebaceous and immobile, but the upper dorsal and sidewall skin is lax. '
                        'She wants a single stage. Which reconstruction is most appropriate?',
                'choices': ['Primary closure along the long axis of the tip',
                            'Preauricular full-thickness skin graft with bolster',
                            'Bilobed transposition flap from the dorsum and sidewall',
                            'Paramedian forehead flap with division at 3 weeks'],
                'answer': 2,
                'explanation': 'The lower-third skin is thick and immobile, so a 1.2 cm defect cannot close '
                               'primarily without distorting the tip or ala. A bilobed flap borrows lax skin '
                               'from the upper dorsum and sidewall through two transposition lobes, '
                               'distributing tension into mobile tissue and giving a good color and '
                               'thickness match in one stage. Her defect size of about 1.5 cm or less, '
                               'superficial depth and safe distance from the rim make her a good candidate.',
                'why_wrong': ['The lower-third skin cannot stretch enough to close a 1.2 cm defect without '
                              'tip distortion or alar elevation.',
                              'A graft on sebaceous tip skin often heals depressed, shiny and poorly matched '
                              'compared with an adjacent flap.',
                              'Correct.',
                              'A two-stage interpolated flap is excessive for a superficial 1.2 cm defect '
                              'with good local tissue, and she wants one stage.'],
                'board_pearl': 'Lower-third nasal defects up to about 1.5 cm with lax upper skin are classic '
                               'bilobed-flap indications.',
                'curveball': 'Which bilobed design error most commonly causes alar retraction, and how do '
                             'you prevent it?',
                'curveball_answer': 'Alar retraction usually comes from closing the defect or donor site '
                                    'with tension vectors that pull the rim upward, often from a defect too '
                                    'close to the rim, wrong pivot placement or inadequate undermining. Keep '
                                    'the pivot and closure vectors away from the margin, undermine widely '
                                    'and place an alar rim graft when the defect edge approaches the rim.'},
 'v259_fpt_bilobed_fnd': {'stem': 'A 73-year-old man has a 1.1 cm superficial defect of the right nasal tip '
                                  'after Mohs surgery. The tip skin cannot be advanced at all on pinch '
                                  'testing, while the upper dorsal skin pinches up easily. A junior resident '
                                  'asks why a bilobed flap is planned instead of a single rhombic '
                                  'transposition flap from the adjacent lateral tip. Which explanation is '
                                  'correct?',
                          'choices': ['It moves closing tension into mobile upper nasal skin through two '
                                      'lobes',
                                      'Its axial blood supply supports a longer flap than a rhombic design '
                                      'allows',
                                      'It carries vascularized cartilage and lining to rebuild a deeper tip '
                                      'defect',
                                      'Its full 180-degree rotation arc eliminates standing cones at the '
                                      'pivot point'],
                          'answer': 0,
                          'explanation': 'The bilobed flap is a random-pattern double transposition flap. '
                                         'The first lobe fills the defect from nearby skin, and the second '
                                         'lobe fills the first-lobe donor site from a more distant, more '
                                         'mobile area, so the final closure falls where skin is lax. A '
                                         'single rhombic flap would take tissue from equally immobile '
                                         'lower-third skin, leaving a tight donor closure that distorts the '
                                         'tip or ala. Two lobes spread tension over a wider area of mobile '
                                         'skin.',
                          'why_wrong': ['Correct.',
                                        'The bilobed flap is a random-pattern flap without a named axial '
                                        'vessel; its length is limited by subdermal perfusion.',
                                        'It carries skin and soft tissue only; cartilage and lining must be '
                                        'supplied separately when the defect is deep.',
                                        'A wide arc enlarges standing cones and pincushioning; modern '
                                        'designs reduce total rotation to about 90 to 100 degrees.'],
                          'board_pearl': 'The bilobed flap moves the final donor closure into lax upper '
                                         'nasal skin, sparing the rigid lower third.',
                          'curveball': 'Which nasal regions usually provide more recruitable skin than the '
                                       'rigid lower third, and why?',
                          'curveball_answer': 'The upper dorsum, upper and mid sidewalls and glabella have '
                                              'thinner, less sebaceous skin loosely attached over the nasal '
                                              'bones and upper lateral cartilages, so it moves easily. The '
                                              'tip and alae have thick sebaceous skin bound tightly to the '
                                              'lower lateral cartilages, which resists stretch and distorts '
                                              'the free margins under tension.'},
 'v259_fpt_bilobed_app': {'stem': 'A 70-year-old woman has a 1.3 cm Mohs defect of the left lateral tip '
                                  'whose lower edge is 4 mm from the alar rim. A bilobed flap is designed '
                                  'with a 180-degree total arc, a first lobe narrower than the defect, '
                                  'limited undermining, and inset under visible tension pulling toward the '
                                  'medial canthus. She has thick sebaceous nasal skin. Which outcome is most '
                                  'likely over the next 2 months?',
                          'choices': ['Distal tip necrosis of the second lobe from venous congestion',
                                      'Left alar rim elevation with trapdoor pincushioning of the flap',
                                      'Epidermal inclusion cysts forming along the lobe incision lines',
                                      'Hypopigmented scarring confined to the second-lobe donor site'],
                          'answer': 1,
                          'explanation': 'Bilobed outcomes depend on lobe size, arc, undermining and tension '
                                         'vector. An undersized first lobe inset under tension, a wide arc '
                                         'and minimal undermining, with a defect only 4 mm from the rim, '
                                         'concentrate pull on the free margin and lift the ala. Thick '
                                         'sebaceous skin with a curvilinear scar and limited undermining '
                                         'favors trapdoor pincushioning as the scar contracts. Prevention '
                                         'uses a reduced arc, adequate lobe size, wide submuscular '
                                         'undermining and rim support when needed.',
                          'why_wrong': ['Necrosis can follow excessive thinning or tension, but the dominant '
                                        'risk of this design is rim distortion and contour deformity.',
                                        'Correct.',
                                        'Inclusion cysts can occur along any incision but are not the '
                                        'typical consequence of excessive arc and tension.',
                                        'Donor site pigment change is uncommon in nasal skin and does not '
                                        'reflect the tension and arc errors in this design.'],
                          'board_pearl': 'Wide arc, undersized lobe and tension near the rim cause alar '
                                         'elevation and pincushioning after a bilobed flap.',
                          'curveball': 'How do wide undermining and careful lobe sizing reduce tension and '
                                       'pincushioning, and what can be done once pincushioning appears?',
                          'curveball_answer': 'Undermining in the submuscular plane above perichondrium '
                                              'across the dorsum and sidewalls lets the whole nasal envelope '
                                              'share tension and spreads scar contracture evenly. Proper '
                                              'lobe sizing avoids bunching. Established pincushioning is '
                                              'treated with intralesional triamcinolone, massage and time, '
                                              'then flap defatting or dermabrasion if it persists beyond '
                                              'several months.'},
 'v259_fpt_bilobed_snr': {'stem': 'A 72-year-old man has a 2.3 cm Mohs defect of the nasal tip and supratip '
                                  'that extends through soft tissue and removes part of both domes; '
                                  'vestibular lining is intact. His nasal skin is thick, sebaceous and '
                                  'immobile on pinch testing. He is otherwise healthy, accepts staged '
                                  'surgery and wants the best long-term shape. Which reconstruction is most '
                                  'appropriate?',
                          'choices': ['Bilobed flap with wide undermining up to the glabella',
                                      'Paramedian forehead flap with cartilage grafting',
                                      'Full-thickness skin graft over the dome remnants',
                                      'Dorsal nasal rotation flap without cartilage grafts'],
                          'answer': 1,
                          'explanation': 'Bilobed flaps have a finite indication, roughly lower-third '
                                         'defects up to about 1.5 cm with recruitable upper skin. This '
                                         'defect is larger, crosses subunits, has lost dome cartilage and '
                                         'sits in thick, immobile skin, so local tissue cannot cover it '
                                         'without flattening the tip and distorting the alae. A paramedian '
                                         'forehead flap supplies abundant, well-vascularized, matching skin, '
                                         'and cartilage grafts restore tip support and projection. He '
                                         'accepts the staged approach, and the result is more reliable.',
                          'why_wrong': ['Stretching a bilobed flap over a 2.3 cm defect in immobile skin '
                                        'flattens the tip and pulls the alae upward.',
                                        'Correct.',
                                        'A skin graft cannot replace lost dome cartilage, and over cartilage '
                                        'remnants it heals depressed and poorly matched.',
                                        'A dorsal nasal flap can resurface some tip defects, but omitting '
                                        'cartilage leaves the lost domes unsupported and the tip flattened.'],
                          'board_pearl': 'Large, deep or multi-subunit distal nasal defects outgrow the '
                                         'bilobed flap; use a forehead flap plus cartilage.',
                          'curveball': 'Which defect characteristics push you toward a paramedian forehead '
                                       'flap instead of a bilobed flap?',
                          'curveball_answer': 'Defects larger than about 1.5 cm on the lower nose, depth '
                                              'with exposed or missing cartilage, loss of lining, location '
                                              'within a few millimeters of the alar rim, thick immobile '
                                              'skin, involvement of multiple subunits, or prior scarring or '
                                              'failed local flaps all favor a forehead flap with any needed '
                                              'cartilage grafts or lining.'},
 'v137_fpt_05': {'stem': 'A 74-year-old woman has a 5 x 4 cm defect of the right lateral cheek and '
                         'preauricular region after Mohs clearance of an infiltrative basal cell carcinoma. '
                         'The base is subcutaneous fat with intact parotid fascia, and no bone, nerve or '
                         'lining is exposed. She has lax jowl and neck skin and wants the best color and '
                         'texture match. Which reconstruction is most appropriate?',
                 'choices': ['Split-thickness skin graft from the anterior thigh',
                             'Paramedian forehead flap based on the supratrochlear artery',
                             'Cervicofacial rotation-advancement flap from the neck',
                             'Anterolateral thigh free flap with microvascular transfer'],
                 'answer': 2,
                 'explanation': 'A cervicofacial flap recruits the broad reservoir of lax cheek and neck '
                                'skin to resurface large lateral cheek defects with excellent color, '
                                'thickness and texture match in one stage. Her defect is superficial over '
                                'parotid fascia, so it needs cover rather than bulk, and her jowl and neck '
                                'laxity provide tissue. Incisions follow the preauricular crease and extend '
                                'into the neck, and elevation in a subcutaneous or deep plane protects the '
                                'facial nerve.',
                 'why_wrong': ['A thigh graft on the cheek heals with a shiny, depressed, poorly matched '
                               'patch when adjacent lax skin is available.',
                               'A forehead flap is designed for nasal reconstruction and cannot reach or '
                               'cover a lateral cheek and preauricular defect.',
                               'Correct.',
                               'Free tissue adds bulk, poor skin match and microsurgical morbidity for a '
                               'superficial defect that local tissue can cover.'],
                 'board_pearl': 'Large superficial lateral cheek defects: the cervicofacial flap uses lax '
                                'cheek and neck skin for one-stage, well-matched cover.',
                 'curveball': 'She had neck radiation for a prior parotid cancer. How does that change '
                              'elevation of the flap?',
                 'curveball_answer': 'Irradiated skin has a poorer subdermal plexus, raising distal necrosis '
                                     'risk with a thin subcutaneous flap. Elevating in a deep plane beneath '
                                     'SMAS and platysma carries perforators from the facial and submental '
                                     'vessels and is more reliable. Minimize tension, avoid excessive '
                                     'length, consider a back cut and counsel about delayed healing.'},
 'v147_fp_06': {'stem': 'A 68-year-old man has a 5 cm defect of the left lateral cheek over parotid fascia '
                        'after wide excision of a cutaneous squamous cell carcinoma with margins cleared on '
                        'frozen section. No bone is exposed. A colleague suggests an anterolateral thigh '
                        'free flap, but the patient has abundant jowl and neck laxity. Which advantage most '
                        'favors a cervicofacial flap instead?',
                'choices': ['It carries a named axial artery that supports a flap of any length',
                            'It brings vascularized fascia that can protect exposed nerve branches',
                            'It adds bulk that fills a parotidectomy contour defect in one stage',
                            'It gives color-matched skin with scars placed in facial creases'],
                'answer': 3,
                'explanation': 'The main advantage of a cervicofacial flap is tissue match: it moves '
                               'adjacent cheek and neck skin of similar color, thickness and texture, and '
                               'its incisions follow the preauricular crease, mandibular border and neck '
                               'creases. A free flap adds microvascular risk, a distant donor site and a '
                               'mismatched skin paddle. Cervicofacial reliability depends on design, plane, '
                               'tension, smoking and radiation, because it is largely random-pattern in the '
                               'subcutaneous plane.',
                'why_wrong': ['In the subcutaneous plane it is largely random-pattern, so excessive length '
                              'or tension risks distal necrosis.',
                              'A subcutaneous cervicofacial flap carries skin and fat only; its main value '
                              'is surface match rather than nerve coverage.',
                              'It is relatively thin; a contour defect after parotidectomy often needs added '
                              'fat or other tissue for volume.',
                              'Correct.'],
                'board_pearl': "The cervicofacial flap's main advantage is color and texture match from "
                               'adjacent tissue with crease-hidden scars.',
                'curveball': 'Final pathology shows a positive deep margin after the flap is inset. How has '
                             'the flap complicated management, and what should be done?',
                'curveball_answer': 'Rotating and advancing tissue rearranges the field, so the original '
                                    'margin location is hard to map and re-excision becomes larger. Use the '
                                    'specimen orientation and operative map to localize the margin, then '
                                    'discuss re-excision versus adjuvant radiation at tumor board. Confirm '
                                    'clear margins before large local flaps, or delay reconstruction when '
                                    'margins are uncertain.'},
 'v259_fpt_cervico_fnd': {'stem': 'A 66-year-old man has a 4 x 4 cm defect of the right mid cheek after Mohs '
                                  'clearance of a basal cell carcinoma, with a healthy subcutaneous fat '
                                  'base. He asks why you recommend a large flap extending into his neck '
                                  'instead of a skin graft from his thigh. He has lax neck skin, no '
                                  'radiation history, and does not smoke. Which explanation is correct?',
                          'choices': ['It brings adjacent cheek and neck skin with matching color and '
                                      'contour',
                                      'It restores a muscle layer that improves animation of the mid cheek',
                                      'It has lower necrosis rates than grafts in patients who smoke heavily',
                                      'It avoids any incision near the lower eyelid or facial nerve '
                                      'branches'],
                          'answer': 0,
                          'explanation': 'A cervicofacial flap mobilizes a wide skin and soft tissue '
                                         'reservoir from the cheek and neck to resurface a large defect with '
                                         'tissue that matches facial color, thickness and texture, and it '
                                         'fills contour better than a thin graft. It avoids a distant donor '
                                         'site and places scars in natural lines. A thigh graft would heal '
                                         'pale, shiny and depressed. His lax neck, nonsmoking status and '
                                         'nonirradiated skin make the flap reliable.',
                          'why_wrong': ['Correct.',
                                        'The flap moves skin and fat or SMAS, not functioning mimetic '
                                        'muscle, so it does not change facial animation.',
                                        'Smoking greatly increases distal necrosis in large random-pattern '
                                        'skin flaps, so it is not an advantage over grafts.',
                                        'Elevation passes near facial nerve branches, and anterior designs '
                                        'approach the lower lid, so planning must protect both.'],
                          'board_pearl': 'Adjacent tissue gives the best facial match; the cervicofacial '
                                         'flap recruits it for large cheek defects.',
                          'curveball': 'Which tissue planes can be used to elevate a cervicofacial flap, and '
                                       'how do they differ in vascularity and facial nerve risk?',
                          'curveball_answer': 'The subcutaneous plane is quick and keeps dissection '
                                              'superficial to the facial nerve, but relies on the subdermal '
                                              'plexus, so distal necrosis is more likely in smokers or '
                                              'irradiated skin. A deep plane beneath SMAS and platysma '
                                              'carries musculocutaneous perforators and is more robust, but '
                                              'dissection lies closer to facial nerve branches and needs '
                                              'care anterior to the parotid.'},
 'v259_fpt_cervico_app': {'stem': 'A 78-year-old woman has a 4 cm defect of the left infraorbital cheek '
                                  'whose upper edge lies 5 mm below the lower lid margin. On exam the lower '
                                  'lid snaps back slowly and can be pulled 8 mm from the globe. A '
                                  'cervicofacial flap is planned to close the defect by advancing tissue '
                                  'upward and medially. Which modification is most important to prevent '
                                  'ectropion?',
                          'choices': ["Suture the flap's leading edge to the lower lid margin for stability",
                                      'Limit undermining so the flap remains thick, short and well perfused',
                                      'Suspend the flap to orbital rim periosteum and tighten the lateral '
                                      'canthus',
                                      'Close the defect vertically along the nasojugal groove beneath the '
                                      'lid'],
                          'answer': 2,
                          'explanation': 'A cervicofacial flap advancing toward the lid transmits a downward '
                                         'pull as it settles and contracts, and her slow snap-back and lid '
                                         'distraction show laxity that will not resist it. Suspending the '
                                         "flap's deep tissue to periosteum of the infraorbital or lateral "
                                         'orbital rim takes weight off the lid. A lateral canthopexy or '
                                         'tarsal strip tightens the lid itself. Wide undermining and a high '
                                         'lateral incision toward the canthus keep the tension vector '
                                         'horizontal.',
                          'why_wrong': ['Anchoring the flap to the lid margin transfers flap weight and '
                                        'contraction directly onto the lax lid, causing ectropion.',
                                        'Limited undermining increases closing tension, and that tension is '
                                        'transmitted to the lid as the flap is advanced.',
                                        'Correct.',
                                        'A vertical closure below the lid creates a downward vector that '
                                        'pulls the lax lower lid into ectropion.'],
                          'board_pearl': 'Cheek flaps near the lid: suspend to orbital rim periosteum and '
                                         'support a lax lid with canthopexy.',
                          'curveball': 'Which patient factors should lower your threshold for prophylactic '
                                       'lower lid support in cheek reconstruction?',
                          'curveball_answer': 'Horizontal lid laxity on snap-back or distraction testing, '
                                              'older age, prior lower blepharoplasty, existing scleral show '
                                              'or ectropion, a negative-vector globe and malar relationship, '
                                              'facial paralysis with weak orbicularis, and prior radiation '
                                              'or scarring all reduce resistance to downward pull and favor '
                                              'canthopexy or tarsal strip.'},
 'v259_fpt_cervico_snr': {'stem': 'A 70-year-old man on daily aspirin undergoes a cervicofacial flap for a 6 '
                                  'cm cheek defect. On postoperative day 1, the neck beneath the flap is '
                                  'tense and swollen, and the distal flap near the nasolabial fold is purple '
                                  'and edematous. Pinprick of the distal flap yields rapid dark blood, and '
                                  'capillary refill is brisk. Vital signs are stable. What is the priority?',
                          'choices': ['Return to the operating room to evacuate the hematoma and control '
                                      'bleeding',
                                      'Apply medicinal leeches to the distal flap and observe it for 48 '
                                      'hours',
                                      'Place a compressive dressing and ice packs, then reassess the next '
                                      'morning',
                                      'Aspirate the collection with a needle at the bedside and continue '
                                      'observation'],
                          'answer': 0,
                          'explanation': 'Brisk dark bleeding on pinprick with rapid refill indicates venous '
                                         'congestion, and the tense neck shows a hematoma compressing the '
                                         "flap's base and venous outflow. This is a correctable mechanical "
                                         'cause. Prompt operative evacuation, hemostasis and release of '
                                         'tension restore outflow before microvascular thrombosis makes '
                                         'necrosis irreversible. Leeches or other decongestion are adjuncts '
                                         'only after mechanical causes are corrected or excluded.',
                          'why_wrong': ['Correct.',
                                        'Leeches treat venous congestion without a mechanical cause; here '
                                        'the hematoma keeps compressing outflow and will keep expanding.',
                                        'Compression over a tense hematoma further reduces flap perfusion '
                                        'and risks necrosis by the next morning.',
                                        'Needle aspiration cannot reliably clear clotted blood or stop '
                                        'active bleeding, so congestion persists and the collection '
                                        'reaccumulates.'],
                          'board_pearl': 'Congested flap with a tense collection: evacuate the hematoma and '
                                         'fix the cause before using adjuncts.',
                          'curveball': 'How do the bedside appearances of venous congestion and arterial '
                                       'insufficiency differ in a skin flap?',
                          'curveball_answer': 'Venous congestion looks purple, swollen and warm, with rapid '
                                              'capillary refill and brisk dark blood on pinprick. Arterial '
                                              'insufficiency looks pale or mottled, cool and flat, with slow '
                                              'or absent refill and little or no bleeding on pinprick. Both '
                                              'need urgent assessment for a correctable cause such as '
                                              'hematoma, tension, kinking or a tight dressing.'},
 'v137_fpt_07': {'stem': 'A 52-year-old woman had Bell palsy 10 months ago and has recovered good voluntary '
                         'movement. Over the past 3 months her left eye narrows whenever she smiles or '
                         'speaks, and her left cheek feels tight. Eye closure is complete, the cornea is '
                         'clear, and resting tone is near symmetric. She is distressed by her appearance in '
                         'photographs. What is the best initial treatment?',
                 'choices': ['Selective neurectomy of the left zygomatic branches',
                             'Neuromuscular retraining with targeted botulinum toxin',
                             'Daily electrical stimulation of the left facial muscles',
                             'Gold weight implantation into the left upper eyelid'],
                 'answer': 1,
                 'explanation': 'Eye narrowing with smiling after Bell palsy recovery is oral-ocular '
                                'synkinesis from aberrant regeneration, with axons reinnervating unintended '
                                'muscles. First-line treatment is facial neuromuscular retraining, which '
                                'teaches selective movement and relaxation, combined with targeted botulinum '
                                'toxin to the overactive orbicularis oculi. Toxin also reveals which muscles '
                                'drive the problem. Surgery such as selective neurectomy or myectomy is '
                                'reserved for patterns that remain disabling despite both.',
                 'why_wrong': ['Neurectomy is reserved for stable synkinesis refractory to retraining and '
                               'toxin; at 10 months it is premature and irreversible.',
                               'Correct.',
                               'Electrical stimulation strengthens muscles nonselectively and may reinforce '
                               'mass movement, so it is generally avoided in synkinesis.',
                               'Her eye closure is complete and the cornea is clear; gold weights treat '
                               'lagophthalmos, not synkinetic eye narrowing.'],
                 'board_pearl': 'Synkinesis after Bell palsy: start with neuromuscular retraining and '
                                'targeted botulinum toxin; surgery for refractory cases.',
                 'curveball': 'She read online that electrical stimulation speeds recovery. How should you '
                              'counsel her?',
                 'curveball_answer': 'Evidence for electrical stimulation in facial nerve recovery is '
                                     'limited and mixed. Because it drives contraction of many muscles at '
                                     'once rather than selective control, there is concern it may reinforce '
                                     'mass movement in synkinesis, so most facial nerve centers avoid it and '
                                     'favor mirror-guided neuromuscular retraining instead.'},
 'v147_fp_07': {'stem': 'A 46-year-old man had right Bell palsy 14 months ago. He now has right eye closure '
                        'when he smiles, a smile that pulls downward at the commissure, and painful '
                        'tightness of the right neck with visible platysmal bands during speech. Voluntary '
                        'movement is fair, eye closure is complete, and EMG shows reinnervation. Which '
                        'treatment plan is most appropriate?',
                'choices': ['Static fascia lata sling suspending the right commissure',
                            'Repeat high-dose oral prednisone followed by observation',
                            'Hypoglossal-facial nerve transfer to the lower division',
                            'Therapy with toxin to the orbicularis, platysma and DAO'],
                'answer': 3,
                'explanation': 'This is postparalytic synkinesis with oral-ocular coupling and hyperactive '
                               'platysma and depressor anguli oris, which pull the commissure down and '
                               'oppose the smile. Neuromuscular retraining and targeted botulinum toxin to '
                               'the overactive orbicularis oculi, platysma and DAO reduce co-contraction, '
                               'release the smile and relieve neck pain. The reinnervated face has useful '
                               'native function, so nerve transfers or slings are not indicated. Selective '
                               'myectomy or neurolysis is reserved for refractory patterns.',
                'why_wrong': ['A static sling corrects resting asymmetry in flaccid paralysis but does '
                              'nothing for co-contraction and neck tightness.',
                              'Steroids help acute Bell palsy within 72 hours; they have no role 14 months '
                              'later in synkinesis.',
                              'Nerve transfer replaces input to a denervated face; his reinnervated face has '
                              'useful voluntary movement that would be sacrificed.',
                              'Correct.'],
                'board_pearl': 'Platysma and DAO overactivity in synkinesis oppose the smile; targeted toxin '
                               'plus retraining often improves it.',
                'curveball': 'How would management differ if he instead had complete flaccid paralysis with '
                             'no recovery potential?',
                'curveball_answer': 'Complete flaccid paralysis is not synkinesis, and chemodenervation will '
                                    'not help. Priorities become eye protection with lubrication, gold or '
                                    'platinum weight and lid tightening, then resting symmetry with static '
                                    'slings, and dynamic reanimation chosen by duration: nerve transfer when '
                                    'muscles are still viable, or free gracilis transfer when they are '
                                    'atrophic.'},
 'v261_fpt_synkinesis_fnd': {'stem': 'A 45-year-old man had left facial paralysis from Ramsay Hunt syndrome '
                                     '8 months ago. Movement has returned, but now his left eye narrows when '
                                     'he purses his lips, and the left corner of his mouth twitches when he '
                                     'blinks. His left nasolabial fold is deeper at rest, and his smile '
                                     'excursion is reduced. MRI at onset showed only facial nerve '
                                     'enhancement. What is the most likely mechanism?',
                             'choices': ['Ephaptic transmission from vascular compression at the root exit '
                                         'zone',
                                         'Persistent partial conduction block with incomplete facial nerve '
                                         'recovery',
                                         'Misdirected axonal regeneration reaching several facial muscles at '
                                         'once',
                                         'Compensatory overactivity of the contralateral face masking '
                                         'weakness'],
                             'answer': 2,
                             'explanation': 'Synkinesis follows facial nerve injury severe enough to cause '
                                            'axonal degeneration. Regenerating axons cross into wrong '
                                            'endoneurial tubes and reach unintended muscles, so one '
                                            'voluntary movement triggers co-contraction elsewhere, such as '
                                            'eye narrowing with lip pursing. Nuclear hyperexcitability and '
                                            'ephaptic crosstalk may contribute. The deeper fold and reduced '
                                            'excursion reflect hypertonic synkinetic muscles opposing each '
                                            'other, which explains why resting tone can look better while '
                                            'the smile is worse.',
                             'why_wrong': ['Vascular compression at the root exit zone causes hemifacial '
                                           'spasm, which produces paroxysmal clonic twitching rather than '
                                           'movement-linked co-contraction after palsy.',
                                           'Conduction block causes weakness that recovers without '
                                           'misdirection; it does not explain involuntary movement linked to '
                                           'voluntary action.',
                                           'Correct.',
                                           'Contralateral overactivity can exaggerate asymmetry but does not '
                                           'cause ipsilateral eye closure triggered by lip movement.'],
                             'board_pearl': 'Synkinesis is misdirected regeneration after axonal injury; it '
                                            'causes co-contraction, hypertonicity and a weaker smile.',
                             'curveball': 'Why can a patient with synkinesis look more symmetric at rest yet '
                                          'still have a worse smile?',
                             'curveball_answer': 'Synkinetic muscles are hypertonic, which deepens the '
                                                 'nasolabial fold, narrows the palpebral fissure and '
                                                 'restores resting tone so the face looks balanced. During '
                                                 'smiling, simultaneous contraction of antagonists such as '
                                                 'the depressor anguli oris, platysma, buccinator and '
                                                 'orbicularis oris opposes the zygomaticus, reducing '
                                                 'excursion and producing a tight, asymmetric smile.'},
 'v261_fpt_synkinesis_app': {'stem': 'A 58-year-old woman had Bell palsy 2 years ago with stable recovery to '
                                     'House-Brackmann grade III. Her right eye closes when she smiles, the '
                                     'right neck tightens with platysmal bands during speech, and her smile '
                                     'has moderate excursion. She has received no treatment of any kind so '
                                     'far. She saw online videos of smile surgery and requests it. What is '
                                     'the best initial treatment?',
                             'choices': ['Therapy and targeted toxin to orbicularis and platysma',
                                         'Free gracilis transfer driven by the masseteric nerve',
                                         'Masseteric-to-facial nerve transfer of the main trunk',
                                         'Static temporalis tendon transfer to the commissure'],
                             'answer': 0,
                             'explanation': 'Her synkinesis is stable with useful native movement and has '
                                            'not been treated. First-line care is facial neuromuscular '
                                            'retraining to improve selective control, combined with '
                                            'botulinum toxin individualized to her pattern, here the '
                                            'orbicularis oculi and platysma. This reduces co-contraction and '
                                            'often improves smile excursion. Free muscle transfer and nerve '
                                            'transfer are for absent or nonrecoverable movement, and would '
                                            'sacrifice her existing function. Selective surgery is '
                                            'considered only if therapy and toxin fail.',
                             'why_wrong': ['Correct.',
                                           'Free muscle transfer is for absent smile with nonrecoverable '
                                           'muscle; it would sacrifice her moderate native excursion.',
                                           'Nerve transfer to the main trunk would replace her useful native '
                                           'input and is meant for denervated, nonrecovering faces.',
                                           'Static or tendon transfers address flaccid paralysis and do not '
                                           'reduce synkinetic co-contraction.'],
                             'board_pearl': 'Stable synkinesis with useful movement: retraining and targeted '
                                            'toxin first, not reanimation surgery.',
                             'curveball': 'If her symptoms persist despite treatment, when might selective '
                                          'neurectomy, neurolysis or myectomy enter her ladder?',
                             'curveball_answer': 'Consider them when synkinesis is stable, typically more '
                                                 'than a year after onset, and remains disabling despite '
                                                 'optimized retraining and repeated toxin. Examples include '
                                                 'selective neurolysis of synkinetic branches, platysmectomy '
                                                 'for neck tethering and DAO myectomy to release the '
                                                 'commissure. Prior toxin response helps predict benefit.'},
 'v261_fpt_synkinesis_snr': {'stem': 'A 50-year-old woman has severe ocular-oral synkinesis and platysmal '
                                     'tethering 3 years after Bell palsy, despite 18 months of guided '
                                     'retraining and five rounds of targeted botulinum toxin. Each toxin '
                                     'round to the platysma and DAO clearly improved her smile for about 3 '
                                     'months, and toxin to the orbicularis relieved eye narrowing. Her '
                                     'pattern has been stable for a year. What is the best next step?',
                             'choices': ['Broad division of the cervical and marginal mandibular branches',
                                         'Free gracilis transfer to replace her native synkinetic smile',
                                         'Selective procedures on the muscles her toxin response identified',
                                         'Hypoglossal-facial jump graft to strengthen the lower face'],
                             'answer': 2,
                             'explanation': 'Surgery for refractory synkinesis must be selective. Her '
                                            'repeated toxin responses act as reversible trials, showing that '
                                            'weakening the platysma and DAO frees her smile and that '
                                            'orbicularis activity drives eye narrowing. With a stable '
                                            'pattern and good responses, options include platysmectomy, DAO '
                                            'myectomy and selective neurolysis of synkinetic branches, '
                                            'preserving the muscles that create her smile and eye closure. '
                                            'Mapping which muscles drive the unwanted movement before '
                                            'surgery predicts the outcome.',
                             'why_wrong': ['Broad branch division causes new weakness, including lower lip '
                                           'and neck paralysis, beyond the targeted synkinetic muscles.',
                                           'Her smile has native excursion that toxin unmasks; replacing it '
                                           'with free muscle sacrifices function and is not indicated.',
                                           'Correct.',
                                           'Jump grafts add axonal input to a denervated face; adding input '
                                           'to an already synkinetic face does not reduce co-contraction.'],
                             'board_pearl': 'Refractory synkinesis: let toxin response map the culprit '
                                            'muscles, then choose selective myectomy or neurolysis.',
                             'curveball': 'How does her botulinum toxin response serve as a reversible trial '
                                          'before permanent selective surgery?',
                             'curveball_answer': 'Toxin temporarily weakens a specific muscle, so the result '
                                                 'previews what permanent weakening would do. Improved smile '
                                                 'after platysma and DAO injection predicts benefit from '
                                                 'platysmectomy or DAO myectomy, while unwanted weakness or '
                                                 'no change warns against that target. Documenting dose, '
                                                 'site and functional change makes the plan more precise.'},
 'v137_fpt_08': {'stem': 'A 69-year-old man has a 3.5 cm Mohs defect involving the nasal tip, left ala and '
                         'soft triangle, with loss of the left lateral crus and part of the dome. Vestibular '
                         'lining is intact. He is a former smoker who quit 5 years ago and accepts staged '
                         'surgery. Which reconstruction is most appropriate?',
                 'choices': ['Bilobed flap from the dorsum over conchal cartilage grafts',
                             'Paramedian forehead flap over auricular cartilage grafts',
                             'Full-thickness preauricular graft over conchal cartilage',
                             'Melolabial interpolation flap over conchal cartilage grafts'],
                 'answer': 1,
                 'explanation': 'This defect is large, crosses tip, ala and soft triangle, and has lost '
                                'framework. Reconstruction must replace each missing layer: lining is '
                                'intact, cartilage grafts restore tip and alar support, and external cover '
                                'must be robust enough to nourish those grafts. The paramedian forehead flap '
                                'is an axial interpolated flap based on the supratrochlear artery that '
                                'supplies abundant, well-matched, well-vascularized skin for multi-subunit '
                                'distal nasal defects. It is staged, with pedicle division usually after '
                                'about 3 weeks.',
                 'why_wrong': ['A bilobed flap is limited to defects up to about 1.5 cm and cannot cover a '
                               '3.5 cm multi-subunit defect without distortion.',
                               'Correct.',
                               'A skin graft cannot nourish an underlying cartilage graft and heals '
                               'depressed and mismatched on the tip.',
                               'A melolabial flap suits defects of the alar subunit but lacks the size to '
                               'cover tip, ala and soft triangle together.'],
                 'board_pearl': 'Large multi-subunit distal nasal defects with cartilage loss: paramedian '
                                'forehead flap cover over cartilage grafts.',
                 'curveball': 'Which vessels supply the paramedian forehead flap, and where is the pedicle '
                              'centered?',
                 'curveball_answer': 'The flap is an axial flap based on the supratrochlear artery, which '
                                     'exits the orbit at the medial brow about 1.7 to 2.2 cm from midline '
                                     'and runs vertically in the frontalis and subcutaneous tissue. '
                                     'Anastomoses with the angular and dorsal nasal arteries add inflow. A '
                                     'pedicle about 1 to 1.5 cm wide centered at the medial brow is '
                                     'standard.'},
 'v141_fpt_03': {'stem': 'A 64-year-old woman undergoes the first stage of a paramedian forehead flap for a '
                         '3 cm tip and supratip defect, with a septal cartilage tip graft. She has smoked '
                         "half a pack daily for 30 years and quit only 2 weeks ago. The flap's frontalis and "
                         'subcutaneous fat make it much thicker than her tip skin. How should flap thinning '
                         'be managed?',
                 'choices': ['Thin the entire flap to the subdermal plexus now',
                             'Thin only the distal flap now and refine it at an intermediate stage',
                             'Divide the pedicle at 1 week so the flap can be thinned early',
                             'Replace the distal flap with a full-thickness graft to avoid thinning'],
                 'answer': 1,
                 'explanation': 'At the first stage, the flap depends entirely on its supratrochlear '
                                'pedicle, and distal tissue is the most vulnerable. Aggressive thinning '
                                'removes the frontalis and fat that carry the axial vessels and subdermal '
                                'plexus, risking distal necrosis, especially in a recent smoker. '
                                'Conservative distal thinning protects perfusion. Once the flap has picked '
                                'up blood supply from the recipient bed, an intermediate stage can safely '
                                'thin and sculpt it, and the pedicle is divided after that.',
                 'why_wrong': ['Thinning the whole flap at first transfer strips the vessels that perfuse '
                               'the distal end and risks necrosis in a recent smoker.',
                               'Correct.',
                               'Recipient-bed revascularization takes weeks; dividing the pedicle at 1 week, '
                               'especially in a recent smoker, risks loss of the flap.',
                               'A skin graft cannot nourish the underlying cartilage graft and heals '
                               'depressed and mismatched compared with the flap.'],
                 'board_pearl': 'Thin a forehead flap conservatively at the first stage; refine it after '
                                'recipient-bed blood supply develops.',
                 'curveball': 'Three weeks later she asks when the pedicle can be cut. What determines the '
                              'timing of pedicle division?',
                 'curveball_answer': 'Division depends on how well the flap is perfused from the recipient '
                                     'bed, usually adequate at about 3 weeks but often delayed in smokers, '
                                     'irradiated beds or after an intermediate stage. A clamp test occluding '
                                     'the pedicle and checking color and capillary refill of the distal flap '
                                     'helps confirm independence before division and inset.'},
 'v261_fpt_forehead_fnd': {'stem': 'A 64-year-old woman has a full-thickness Mohs defect of the left ala and '
                                   'soft triangle measuring 2.5 cm, with loss of the lateral crus and a 1.5 '
                                   'cm defect in the vestibular lining. Septal mucosa and cartilage are '
                                   'healthy. She does not smoke and accepts staged surgery. Which '
                                   'reconstructive plan is most appropriate?',
                           'choices': ['Forehead flap cover alone, leaving the lining to mucosalize',
                                       'Composite auricular graft spanning the full alar defect',
                                       'Cartilage graft and forehead flap without lining repair',
                                       'Lining flap, cartilage graft and forehead flap cover'],
                           'answer': 3,
                           'explanation': 'Major nasal reconstruction is a three-layer problem. Missing '
                                          'lining must be replaced with vascularized tissue, such as a '
                                          'septal mucoperichondrial hinge flap, or contraction will collapse '
                                          'the nostril. Cartilage grafts restore alar support and resist '
                                          'contracture, and a forehead flap provides external cover. Each '
                                          'layer depends on the others; cover over an incomplete foundation '
                                          'contracts, and grafts without vascularized lining or cover fail.',
                           'why_wrong': ['Raw lining left to heal secondarily contracts, pulling the ala '
                                         'upward and narrowing the nostril beneath the flap.',
                                         'Composite grafts survive by diffusion and are limited to about 1 '
                                         'to 1.5 cm; a 2.5 cm defect would likely necrose.',
                                         'A cartilage graft placed over a lining defect lacks vascular '
                                         'support and is likely to become exposed, infected or resorbed.',
                                         'Correct.'],
                           'board_pearl': 'Full-thickness nasal defects need lining, structural support and '
                                          'cover reconstructed as separate layers.',
                           'curveball': 'Why is the paramedian forehead flap particularly useful for large '
                                        'distal nasal skin defects?',
                           'curveball_answer': 'It is an axial flap based on the supratrochlear artery, so '
                                               'it reliably carries a large, well-vascularized skin paddle '
                                               'that matches nasal color and texture and can nourish '
                                               'underlying cartilage grafts and lining. It reaches the tip, '
                                               'ala and columella, covers several subunits at once, and the '
                                               'donor site heals acceptably.'},
 'v261_fpt_forehead_app': {'stem': 'A 70-year-old man has a subtotal defect of the nasal tip and both alae '
                                   'after Mohs surgery, with loss of both domes and lateral crura but intact '
                                   'lining. His forehead skin is thick and sebaceous. Reconstruction with a '
                                   'paramedian forehead flap over costal cartilage grafts is planned. He '
                                   'asks why his surgeon recommends three stages instead of two. Which '
                                   'explanation is correct?',
                           'choices': ['Three stages allow the pedicle to be divided early, at 1 week',
                                       'An intermediate stage allows safe thinning and graft refinement',
                                       'Three stages let the flap be fully thinned at the first operation',
                                       'The extra stage is needed to expand the forehead before harvest'],
                           'answer': 1,
                           'explanation': 'With a large defect, thick forehead skin and multiple cartilage '
                                          'grafts, a three-stage approach balances perfusion and contour. At '
                                          'the first stage the flap is thinned only conservatively because '
                                          'it depends on the supratrochlear pedicle. At an intermediate '
                                          'stage, roughly 3 weeks later, the flap has gained blood supply '
                                          'from the bed, so it can be elevated, thinned and the cartilage '
                                          'framework sculpted while the pedicle remains. Division follows '
                                          'weeks later, giving better definition with less necrosis risk.',
                           'why_wrong': ['Pedicle division at 1 week is too early in any approach, because '
                                         'the flap still depends on its pedicle for perfusion.',
                                         'Correct.',
                                         'Full thinning at the first stage endangers distal perfusion; the '
                                         'three-stage method exists to delay that thinning.',
                                         'Tissue expansion is an occasional adjunct for large donor sites, '
                                         'not the reason for the intermediate stage.'],
                           'board_pearl': 'Three-stage forehead flap: an intermediate stage allows safe '
                                          'thinning and framework refinement before division.',
                           'curveball': 'How does the extent of flap thinning differ between the '
                                        'intermediate stage and pedicle division?',
                           'curveball_answer': 'At the intermediate stage the flap is elevated off the nose '
                                               'except at the pedicle, and frontalis and fat are excised to '
                                               'thin it to final thickness while cartilage grafts are '
                                               'sculpted. At pedicle division, thinning is limited to the '
                                               'proximal inset and brow end, because the newly divided flap '
                                               'relies entirely on its recipient-bed blood supply.'},
 'v261_fpt_forehead_snr': {'stem': 'A 61-year-old woman had a paramedian forehead flap for a full-thickness '
                                   'left alar defect 8 months ago. The vestibular defect was left to heal '
                                   'secondarily, and no framework graft was placed. Her left nostril has '
                                   'contracted to half its original size, the ala collapses on inspiration, '
                                   'and the flap is bulky. Another surgeon proposed debulking. Which plan is '
                                   'most appropriate?',
                           'choices': ['Debulk the flap and treat the alar scar with fractional laser',
                                       'Serial nostril dilation with stents worn over several months',
                                       'Repeat flap thinning through the original alar incision lines',
                                       'Rebuild the lining with a local flap and add alar cartilage support'],
                           'answer': 3,
                           'explanation': 'Her stenosis is a three-layer reconstructive failure. The lining '
                                          'defect healed by contraction and no cartilage was placed, so scar '
                                          'has pulled the ala inward and the unsupported wall collapses. '
                                          'Debulking the external cover does not fix missing lining or '
                                          'framework. Revision should release the scar, restore lining with '
                                          'vascularized tissue such as a septal hinge or turnover flap, add '
                                          'an alar batten or rim graft, and reinset or thin cover only after '
                                          'the foundation is rebuilt.',
                           'why_wrong': ['Debulking and laser treat the cover only; contracted lining and '
                                         'absent support will keep the nostril narrow and collapsing.',
                                         'Stents can maintain a lumen after repair, but alone they cannot '
                                         'overcome a lining deficit and absent framework.',
                                         'Thinning the flap again reduces bulk but leaves the contracted '
                                         'lining and unsupported ala that cause the stenosis.',
                                         'Correct.'],
                           'board_pearl': 'Nostril stenosis after forehead flap usually means missing lining '
                                          'or support; rebuild the foundation, not just the cover.',
                           'curveball': 'Which lining options can be considered for major alar or columellar '
                                        'defects during revision?',
                           'curveball_answer': 'Options include an ipsilateral septal mucoperichondrial '
                                               'hinge flap, a composite septal chondromucosal pivot flap, '
                                               'turnover flaps of adjacent scar or skin, a bipedicle '
                                               'vestibular advancement flap, inferior turbinate flaps, '
                                               'full-thickness skin grafts under a vascularized cover, a '
                                               'folded distal forehead flap, and a radial forearm free flap '
                                               'for subtotal defects.'},
 'v137_fpt_09': {'stem': 'A 42-year-old man with Norwood IV androgenetic alopecia has taken finasteride for '
                         '2 years with stable loss. Trichoscopy shows miniaturized hairs across the frontal '
                         'scalp but uniform terminal hairs over the back and sides of the scalp. He asks '
                         'whether hair moved from the back of his head will eventually fall out like the '
                         'hair in front. Which principle answers his question?',
                 'choices': ['Occipital follicles keep their androgen resistance after transfer',
                             'Grafted follicles take on the miniaturization of the recipient site',
                             'Grafts survive only where some terminal recipient hair remains',
                             'Finasteride must continue to protect the transplanted follicles'],
                 'answer': 0,
                 'explanation': 'Donor dominance underlies hair transplantation. Follicles from the '
                                'permanent occipital and parietal donor zone are relatively resistant to '
                                'dihydrotestosterone-driven miniaturization, and they keep that behavior '
                                'when moved to the balding frontal scalp. His uniform terminal donor hair on '
                                'trichoscopy suggests a stable donor zone. Medical therapy remains important '
                                'to slow loss of the surrounding native hair, but the grafts themselves '
                                'behave like occipital hair.',
                 'why_wrong': ['Correct.',
                               'This describes recipient dominance, which is not how grafts behave; donor '
                               'follicles keep their native androgen sensitivity.',
                               'Grafts can grow in completely bald scalp if the bed is healthy and well '
                               'vascularized; surrounding terminal hair is not required.',
                               'Finasteride slows loss of native androgen-sensitive hair; transplanted '
                               'occipital follicles do not depend on it.'],
                 'board_pearl': 'Donor dominance: permanent-zone occipital follicles keep their androgen '
                                'resistance after transplantation.',
                 'curveball': 'A different patient has diffuse thinning over the whole scalp, including the '
                              'occiput, with miniaturization in the donor zone. How does that change his '
                              'candidacy?',
                 'curveball_answer': 'Diffuse unpatterned alopecia involves the donor zone, so harvested '
                                     'follicles are themselves androgen-sensitive and will thin after '
                                     'transfer, and harvesting further depletes a weak donor area. These '
                                     'patients are generally poor transplant candidates. Treat medically, '
                                     'consider camouflage, and check donor miniaturization with trichoscopy '
                                     'before surgery.'},
 'v147_fp_08': {'stem': 'A 48-year-old man with stable Norwood V androgenetic alopecia has taken finasteride '
                        'for 4 years and has good occipital donor density. He shows you photographs of a '
                        'transplant with a straight, dense hairline that looks like a wig, and asks how to '
                        'avoid that result. Which surgical plan best produces a natural long-term result?',
                'choices': ['Irregular hairline of single-hair grafts set at native angles',
                            'Straight, dense hairline of multi-hair grafts at the juvenile position',
                            'Grafts placed perpendicular to the scalp for maximum density',
                            'Rows of round punch grafts placed in rows across the front'],
                'answer': 0,
                'explanation': 'A natural transplant depends on design and placement as much as graft '
                               'survival. The hairline should be set at an age-appropriate level, with an '
                               'irregular, feathered transition zone of single-hair follicular units, and '
                               'multi-hair units placed behind for density. Grafts are angled acutely and '
                               'directed to match native hair flow. A conservative design also preserves '
                               'donor supply for future loss, because native hair loss continues and the '
                               'donor reserve is finite.',
                'why_wrong': ['Correct.',
                              'A straight, dense line of multi-hair grafts produces the abrupt wig-like edge '
                              'he wants to avoid, especially as surrounding hair thins.',
                              'Perpendicular grafts stand straight up and look unnatural; native frontal '
                              'hair exits at an acute, forward-directed angle.',
                              "Large punch grafts in rows create the obsolete doll's-hair or plug appearance "
                              'that follicular-unit grafting replaced.'],
                'board_pearl': 'Natural hairline: irregular, single-hair follicular units at native angle, '
                               'set at an age-appropriate height.',
                'curveball': 'He asks whether strip harvest or follicular-unit extraction is better. How do '
                             'FUT and FUE differ in scarring and donor management?',
                'curveball_answer': 'Strip harvest leaves one linear occipital scar, yields many intact '
                                    'follicular units with low transection and preserves surrounding '
                                    'density, but limits very short hairstyles. FUE leaves scattered dot '
                                    'scars that allow short hair, but risks higher transection and patchy '
                                    'overharvesting if extraction is spread beyond the safe zone.'},
 'v262_fpt_hair_fnd': {'stem': 'A 30-year-old man with Norwood III frontotemporal recession plans follicular '
                               'unit transplantation. His father has a Norwood VI pattern with a persistent '
                               'horseshoe of hair over the back and sides of the scalp. On exam he has '
                               'dense, uniform terminal hair over the mid occiput and parietal scalp. From '
                               'which donor region should grafts be harvested?',
                       'choices': ['Upper occipital scalp just beneath the expected vertex border',
                                   'Low nape hair along the posterior hairline of the neck',
                                   'Mid occipital and side scalp within the permanent zone',
                                   'Crown hair bordering the area of early vertex thinning'],
                       'answer': 2,
                       'explanation': 'Grafts should come from the safe donor zone, the mid occipital and '
                                      'parietal scalp that remains even in advanced Norwood VI to VII '
                                      "patterns, as his father's horseshoe shows. Follicles there are "
                                      'relatively androgen resistant and keep that property after transfer. '
                                      'Hair at the upper border, near the crown or in the low nape may later '
                                      'thin, so grafts from those areas can be lost and harvest scars may '
                                      'become visible.',
                       'why_wrong': ['The upper border of the donor zone can recede with progression, so '
                                     'grafts from there may miniaturize and scars become exposed.',
                                     'Low nape hair is finer and may thin with age, making it an unreliable '
                                     'source for permanent frontal grafts.',
                                     'Correct.',
                                     'Crown hair lies in the androgen-sensitive zone and will likely '
                                     'miniaturize, both before and after transfer.'],
                       'board_pearl': 'Harvest from the mid occipital and parietal safe donor zone, which '
                                      'persists even in advanced Norwood patterns.',
                       'curveball': 'Ten years after transplantation, some of his transplanted hairs are '
                                    'thinning. What explanations should you consider?',
                       'curveball_answer': 'Grafts taken from the edges of the donor zone may have been '
                                           'androgen-sensitive and are now miniaturizing. He may also have '
                                           'developed diffuse unpatterned alopecia or retrograde thinning of '
                                           'the donor zone. Also exclude telogen effluvium, thyroid disease, '
                                           'iron deficiency and lichen planopilaris before planning more '
                                           'surgery.'},
 'v262_fpt_hair_app': {'stem': 'A 23-year-old man has Norwood III recession that has progressed noticeably '
                               'over 18 months. His father and older brother have Norwood VI patterns, and '
                               'trichoscopy shows miniaturization extending behind the frontal hairline. He '
                               'has never tried finasteride or minoxidil and requests a low, dense hairline '
                               'matching his teenage photographs. What is the best plan?',
                       'choices': ['Single large session restoring the juvenile hairline using most donor '
                                   'grafts',
                                   'Crown transplantation first, to treat the area he cannot easily see',
                                   'Large FUE session to outpace progression before it reaches the crown',
                                   'Start medical therapy, defer or limit surgery, and plan a mature '
                                   'hairline'],
                       'answer': 3,
                       'explanation': 'Young patients with rapid progression and a strong family history are '
                                      'likely to reach advanced patterns, so transplantation is a lifetime '
                                      'donor management problem. A low, dense juvenile hairline made now '
                                      'becomes an isolated island as native hair recedes behind it, and the '
                                      'finite donor reserve may be exhausted. Starting finasteride or '
                                      'minoxidil stabilizes loss and clarifies his pattern, and any later '
                                      'surgery uses a conservative, age-appropriate hairline that will look '
                                      'natural at age 50.',
                       'why_wrong': ['A juvenile hairline built with most of his donor supply leaves no '
                                     'reserve and becomes unnatural as hair behind it is lost.',
                                     'Early crown grafting uses donor hair in an area that will keep '
                                     'expanding, leaving too few grafts for the frontal hairline.',
                                     'Transplanting cannot outpace progression, and a large FUE session can '
                                     'deplete and visibly thin his donor zone.',
                                     'Correct.'],
                       'board_pearl': 'Young, rapidly progressing alopecia: stabilize medically and design a '
                                      'conservative, mature hairline; conserve donor hair.',
                       'curveball': 'After 12 months of finasteride his loss has stabilized. How does '
                                    'medical stabilization affect timing and graft-number decisions?',
                       'curveball_answer': 'Stabilization shows his true pattern and lets the planned zone '
                                           'be defined, so surgery can be timed once loss is no longer '
                                           'rapid. Graft numbers should be modest, front-weighted and '
                                           'conservative, keeping a reserve for future sessions. He must '
                                           'understand that stopping therapy will speed native loss around '
                                           'the grafts.'},
 'v262_fpt_hair_snr': {'stem': 'A 55-year-old man with Norwood VI alopecia has had three prior FUE sessions '
                               'elsewhere totaling about 6,000 grafts. His occipital donor zone now shows '
                               'visible patchy thinning and scattered white dot scars with short hair. He '
                               'requests another session to achieve dense coverage from the hairline to the '
                               'crown. What is the best decision?',
                       'choices': ['Assess remaining donor density and counsel limited, front-weighted goals',
                                   'Perform another large FUE session from the remaining permanent zone',
                                   'Harvest from the upper scalp above the safe zone to spare the occiput',
                                   'Perform a strip harvest through the thinned zone for 3,000 more grafts'],
                       'answer': 0,
                       'explanation': 'Donor supply is finite, and his visible donor thinning shows it has '
                                      'been heavily used. Before any surgery, measure remaining donor '
                                      'density and laxity and counsel realistically: full coverage of '
                                      'Norwood VI is not possible, and further overharvesting would create a '
                                      'permanent donor deformity. Goals should shift toward framing the face '
                                      'with a modest frontal session, and alternatives such as scalp '
                                      'micropigmentation, medical therapy and styling should be discussed.',
                       'why_wrong': ['Correct.',
                                     'Another large extraction from a visibly depleted zone risks a '
                                     'permanent moth-eaten donor deformity with little cosmetic gain.',
                                     'Hair above the safe zone is likely to be lost with progression, so '
                                     'grafts there fail and leave visible scars.',
                                     'Strip harvest through a heavily extracted, scarred donor area yields '
                                     'fewer grafts and risks a wide, visible scar.'],
                       'board_pearl': 'Depleted donor zone: measure reserve, limit goals to frontal framing '
                                      'and avoid donor deformity.',
                       'curveball': 'What findings make body or beard hair a possible adjunct, and why is it '
                                    'not equivalent to scalp donor hair?',
                       'curveball_answer': 'Beard or chest hair may help when scalp donor reserve is '
                                           'exhausted, the patient has dense, coarse body hair, and the goal '
                                           'is crown density or scar camouflage. It differs in caliber, '
                                           'curl, growth cycle and length, has lower and less predictable '
                                           'survival, and looks unnatural at the hairline.'},
 'v137_fpt_10': {'stem': 'A 70-year-old woman is referred directly from Mohs surgery with a nasal defect '
                         'that the referral note describes as 1.4 cm and asks for a forehead flap. On '
                         'examination the defect lies on the supratip, is 3 mm deep with intact '
                         'perichondrium, spares the alar margins, and is surrounded by lax upper dorsal '
                         'skin. Margins are clear. What is the best first step?',
                 'choices': ['Proceed with the forehead flap the referral note requested',
                             'Close the defect primarily after wide undermining of nasal skin',
                             'Apply a full-thickness skin graft as the default for nasal defects',
                             'Assess depth, subunit, missing layers and nearby tissue laxity'],
                 'answer': 3,
                 'explanation': 'Mohs reconstruction starts with defect analysis, not a preferred flap. The '
                                'same diameter can represent very different problems depending on depth, '
                                'subunit, missing lining or framework, proximity to free margins and nearby '
                                'laxity. Here, analysis shows a superficial supratip defect with intact '
                                'perichondrium, spared margins and lax upper dorsal skin, which points to a '
                                'local flap such as a bilobed or dorsal nasal flap rather than a forehead '
                                'flap.',
                 'why_wrong': ['The referral request is not a defect analysis; this superficial defect with '
                               'lax adjacent skin likely does not need a staged forehead flap.',
                               'Primary closure of a 1.4 cm supratip defect in tight lower-third skin risks '
                               'tip distortion; the plan should follow analysis first.',
                               'A graft is one option, but choosing it by default skips the analysis that '
                               'may favor a better-matched local flap.',
                               'Correct.'],
                 'board_pearl': 'Analyze each Mohs defect by depth, subunit, missing layers and adjacent '
                                'laxity before choosing a repair.',
                 'curveball': 'If the defect had exposed cartilage without perichondrium, how would that '
                              'affect graft take and your choice?',
                 'curveball_answer': 'Cartilage without perichondrium is a poorly vascularized bed, so a '
                                     'skin graft is likely to fail except over small areas that can bridge '
                                     'from edges. Preserve perichondrium when possible; otherwise fenestrate '
                                     'the cartilage, delay grafting until granulation forms, or choose a '
                                     'vascularized local flap.'},
 'v147_fp_11': {'stem': 'A 66-year-old man is sent for repair of a 1.5 cm left alar defect after Mohs '
                        'surgery for an invasive squamous cell carcinoma. The Mohs note states that the '
                        'final stage showed tumor tracking along a small nerve at the deep margin, and the '
                        'specimen is pending further review. The defect is deep with exposed lateral crus. '
                        'What should be done first?',
                'choices': ['Confirm clearance with the Mohs surgeon and plan more excision first',
                            'Proceed with a melolabial flap and send the tissue for permanent sections',
                            'Place a full-thickness graft to allow surveillance before final reconstruction',
                            'Arrange adjuvant radiation to the ala before any reconstructive surgery'],
                'answer': 0,
                'explanation': 'Reconstruction should begin only after oncologic clearance is established '
                               'and the full three-dimensional defect is known. Perineural tumor at the deep '
                               'margin means clearance is uncertain and further excision is likely, which '
                               'could change the defect and the required repair. Definitive flaps rearrange '
                               'tissue and obscure the margin. The surgeon should confirm margin status with '
                               'the Mohs surgeon and pathologist and plan imaging or further resection when '
                               'indicated.',
                'why_wrong': ['Correct.',
                              'Inset of a flap over an uncleared margin hides residual tumor and complicates '
                              'later re-excision of rearranged tissue.',
                              'A graft can help surveillance after clearance, but placing it over a known '
                              'positive perineural margin delays needed resection.',
                              'Radiation may be indicated later, but it should not replace clarification and '
                              'clearance of a positive margin.'],
                'board_pearl': 'Confirm margins before Mohs reconstruction; perineural invasion at a margin '
                               'may require more resection first.',
                'curveball': 'Once margins are clear, the defect proves to be full thickness through the '
                             'ala. How does full-thickness alar loss change the reconstructive ladder?',
                'curveball_answer': 'All three layers must be rebuilt: lining with a septal hinge, bipedicle '
                                    'vestibular or folded flap; a conchal cartilage batten or framework '
                                    'graft to prevent notching and collapse; and vascularized cover such as '
                                    'a melolabial interpolation or paramedian forehead flap. A skin-only '
                                    'repair contracts and narrows the nostril.'},
 'v259_fpt_mohs_fnd': {'stem': 'A 74-year-old woman has two Mohs defects after clearance of basal cell '
                               'carcinomas: a 2.5 cm superficial defect on the convex mid cheek and a 0.8 cm '
                               'defect of the right ala whose lower edge lies 2 mm from the nostril rim, '
                               'extending to the cartilage. Margins are clear on both. The resident assumes '
                               'the cheek is the harder repair. What most determines the complexity of the '
                               'alar reconstruction?',
                       'choices': ['Its longest surface diameter compared with the cheek defect',
                                   'Her age and the degree of overall facial skin laxity she has',
                                   'How deep it is and how close it sits to a free edge',
                                   'Basal cell histologic subtype and her Fitzpatrick skin type'],
                       'answer': 2,
                       'explanation': 'Mohs defects are defined by depth, subunit, exposed structures and '
                                      'nearby free margins, not just diameter. A small alar defect reaching '
                                      'cartilage within 2 mm of the rim risks notching, retraction and '
                                      'external valve compromise with any contracting repair, so it may need '
                                      'a rim graft and flap. The larger convex cheek defect has abundant lax '
                                      'tissue nearby and no free margin, so a simple advancement or rotation '
                                      'flap often suffices.',
                       'why_wrong': ['Diameter alone underestimates the alar defect, which is smaller but '
                                     'sits near a free margin and reaches cartilage.',
                                     'Laxity helps choose a donor, but the free margin and depth set the '
                                     'alar risk regardless of age or laxity.',
                                     'Correct.',
                                     'Histology mattered for clearance, which is complete; skin type affects '
                                     'scars but not the structural demands of this defect.'],
                       'board_pearl': 'Small defects near free margins, such as alar rim or eyelid, can be '
                                      'harder than large convex cheek defects.',
                       'curveball': 'Why can a 6 mm defect of the lower eyelid margin be more demanding than '
                                    'a 3 cm defect of the lateral cheek?',
                       'curveball_answer': 'The lid margin is a functional free edge: any vertical tension '
                                           'or contraction can cause ectropion, retraction, exposure '
                                           'keratopathy or notching, and full-thickness loss needs layered '
                                           'tarsoconjunctival and skin reconstruction. A convex cheek has '
                                           'broad laxity, so even a large defect closes with an advancement '
                                           'flap without distortion.'},
 'v259_fpt_mohs_app': {'stem': 'A 67-year-old man has a 1.6 cm full-thickness defect of the left ala after '
                               'Mohs surgery for basal cell carcinoma, with loss of skin, part of the '
                               'lateral crus and 1 cm of vestibular lining. The alar rim remains intact. '
                               'Margins are clear, he does not smoke, and he accepts staged surgery. Which '
                               'reconstruction is most appropriate?',
                       'choices': ['Composite auricular graft replacing all three layers in one piece',
                                   'Lining flap, conchal cartilage graft and melolabial flap',
                                   'Full-thickness skin graft outside with lining left to heal',
                                   'Conchal cartilage with a skin graft placed on each surface'],
                       'answer': 1,
                       'explanation': 'Full-thickness nasal defects need layered reconstruction. Missing '
                                      'lining is replaced with vascularized tissue such as a bipedicle '
                                      'vestibular advancement or septal hinge flap. A conchal cartilage '
                                      'graft restores alar support and prevents notching. A vascularized '
                                      'melolabial interpolation flap gives matching cover and nourishes the '
                                      'cartilage. Missing any layer leads to contraction, alar retraction, '
                                      'vestibular stenosis and external valve collapse even if early skin '
                                      'cover looks acceptable.',
                       'why_wrong': ['Composite grafts survive by diffusion and are reliable only to about 1 '
                                     'to 1.5 cm; at 1.6 cm full thickness, necrosis risk is high.',
                                     'Correct.',
                                     'Lining left to heal secondarily contracts, and no support is restored, '
                                     'so the ala will retract and the nostril narrow.',
                                     'Cartilage sandwiched between two grafts has no vascularized layer, so '
                                     'the grafts and cartilage are likely to fail.'],
                       'board_pearl': 'Full-thickness alar defects need lining, cartilage support and '
                                      'vascularized cover, each layer reconstructed.',
                       'curveball': 'Which cartilage donor sites are commonly used for alar structural '
                                    'grafting, and what are their characteristics?',
                       'curveball_answer': 'Conchal cartilage is curved, flexible and well suited to alar '
                                           'battens and rim grafts. Septal cartilage is straight and strong, '
                                           'used for struts and battens when available. Costal cartilage '
                                           'provides large volume when septum and ear are unavailable, but '
                                           'is stiffer, can warp and adds chest donor morbidity.'},
 'v259_fpt_mohs_snr': {'stem': 'A 60-year-old woman has a Mohs defect that removes about 70% of the nasal '
                               'tip subunit, leaving a 4 mm crescent of residual tip skin along the left '
                               'dome that is tethered and distorted. Margins are clear, perichondrium is '
                               'intact, and a paramedian forehead flap is planned. She is a nonsmoker. How '
                               'should the residual strip of tip skin be handled?',
                       'choices': ['Preserve the strip and inset the flap closely around its margins',
                                   'Excise the strip so the flap resurfaces the entire tip subunit',
                                   'Advance the strip over the dome so the scar crosses the tip',
                                   'Close part of the defect primarily before inset of the flap'],
                       'answer': 1,
                       'explanation': 'When a defect involves most of a convex subunit such as the tip, the '
                                      'subunit principle suggests excising the remaining skin so the flap '
                                      'replaces the whole subunit. Scars then fall at subunit borders, where '
                                      "shadows hide them, and the flap's contraction produces a smooth, "
                                      'convex tip rather than a pincushioned patch. Her 4 mm crescent is '
                                      'small, distorted and tethered, so keeping it adds a visible scar line '
                                      'and an uneven contour.',
                       'why_wrong': ['Keeping a small, distorted strip leaves a scar across the convex tip '
                                     'and a patchwork contour as the flap contracts.',
                                     'Correct.',
                                     'Pulling distorted skin over the dome places the scar on the most '
                                     'visible convex surface and adds tension.',
                                     'Primary closure of the lower nasal tip distorts its shape and alar '
                                     'margins and does not make the defect a better subunit fit.'],
                       'board_pearl': 'Large convex nasal subunit defects: consider completing the subunit '
                                      'so scars fall at subunit borders.',
                       'curveball': 'When would you preserve residual subunit skin instead of completing the '
                                    'subunit?',
                       'curveball_answer': 'Preserve native skin when the defect involves less than about '
                                           'half of the subunit, lies in flat or concave subunits such as '
                                           'the sidewall, when residual skin is healthy and not distorted, '
                                           'or when enlarging the defect would force a bigger flap or staged '
                                           'repair. The subunit principle is a guide, not a mandate.'},
 'v137_fpt_11': {'stem': 'A 30-year-old woman has a bifid, asymmetric nasal tip with a knuckle on the left '
                         'dome 3 years after closed rhinoplasty elsewhere. Exam shows the domes at different '
                         'heights, a buckled left lateral crus and weak tip recoil. She will need dome '
                         'repositioning, tip grafts and a columellar strut or septal extension. Which '
                         'approach best suits her deformity?',
                 'choices': ['Endonasal delivery approach avoiding a columellar incision',
                             'Cartilage-splitting approach preserving the rim strip intact',
                             'Retrograde approach via intercartilaginous incisions alone',
                             'Open approach with direct bilateral framework exposure'],
                 'answer': 3,
                 'explanation': 'Complex, asymmetric tip deformities and revisions benefit from the open '
                                'approach because it gives broad, direct, bilateral exposure of the lower '
                                'lateral cartilages in their natural position. This allows precise diagnosis '
                                'of asymmetry and buckling, sutured graft placement, and symmetric suture '
                                'modification under direct vision. The trade-offs are more dissection, '
                                'longer tip edema and a transcolumellar scar, so approach choice should '
                                'match complexity.',
                 'why_wrong': ['The delivery approach exposes each crus separately and out of position, '
                               'limiting comparison and precise fixation of tip grafts.',
                               'Cartilage splitting suits modest cephalic trim but gives poor exposure for '
                               'dome repositioning and complex grafting.',
                               'Retrograde access is limited to cephalic trim and offers too little exposure '
                               'for dome repositioning or tip grafting.',
                               'Correct.'],
                 'board_pearl': 'Open rhinoplasty: best exposure for complex or revision tip work, at the '
                                'cost of edema and a columellar scar.',
                 'curveball': 'During her revision, a cephalic trim is planned. Which maneuvers preserve or '
                              'restore tip support afterward?',
                 'curveball_answer': 'Preserve a lateral crural rim strip of at least about 6 mm, protect '
                                     'the scroll region when possible and avoid unnecessary interruption of '
                                     'medial crural footplate attachments. Restore support with a columellar '
                                     'strut, septal extension graft or tongue-in-groove fixation, and '
                                     'stabilize the crura with lateral crural struts if they are weak or '
                                     'buckled.'},
 'v142_fpt_01': {'stem': 'A 33-year-old man with thin nasal skin is undergoing open rhinoplasty. After the '
                         'transcolumellar and marginal incisions, the resident elevates the tip skin with '
                         'scissors and notes yellow fat on the cartilage side of the flap, small bleeding '
                         'vessels and a visibly thin, translucent dermis over the domes. Which correction '
                         'best restores safe exposure?',
                 'choices': ['Continue in the current plane to thin the skin envelope evenly',
                             'Cauterize both columellar arteries and widen the exposure',
                             'Convert to an endonasal approach and close the columellar incision',
                             'Redirect dissection deep to the SMAS, onto the perichondrium'],
                 'answer': 3,
                 'explanation': 'The proper open rhinoplasty plane is deep to the nasal SMAS, immediately on '
                                'the perichondrium of the lower and upper lateral cartilages, which is '
                                'relatively avascular and keeps the subdermal plexus and the lateral nasal '
                                'arteries in the flap. Fat on the cartilage side and thin, bleeding dermis '
                                'show dissection too superficial. Returning to the supraperichondrial plane '
                                'gives clean exposure, protects tip skin perfusion, and reduces edema and '
                                'contour irregularities.',
                 'why_wrong': ['Continuing superficially injures the subdermal plexus and risks tip skin '
                               'necrosis, especially in thin skin.',
                               'The columellar arteries are divided routinely, so the flap relies on the '
                               'lateral nasal arteries carried in the correct deep plane.',
                               'The open approach is still appropriate; the error is plane depth, which is '
                               'easily corrected without abandoning exposure.',
                               'Correct.'],
                 'board_pearl': 'Open rhinoplasty dissection belongs deep to the SMAS on perichondrium, '
                                "protecting the tip skin's blood supply.",
                 'curveball': 'Which vascular or skin factors make aggressive tip-skin thinning especially '
                              'hazardous?',
                 'curveball_answer': 'Smoking, prior rhinoplasty with scarring, prior radiation, cocaine '
                                     'use, very thin skin, diabetes or vasculitis, and simultaneous alar '
                                     'base excisions all reduce perfusion. The columellar arteries are '
                                     'divided in the open approach, so alar base excisions that injure the '
                                     'lateral nasal arteries further threaten the tip skin.'},
 'v260_fpt_open_fnd': {'stem': 'A 27-year-old woman with medium-thickness skin plans primary rhinoplasty for '
                               'a 4 mm dorsal hump and a broad, poorly defined tip that will need dome '
                               'sutures and a columellar strut. She asks what she gains and what she gives '
                               'up if her surgeon uses an open rather than an endonasal approach. Which '
                               'statement best summarizes the trade-off?',
                       'choices': ['Better framework exposure, but longer tip swelling and a columellar scar',
                                   'Less postoperative edema because dissection is done under direct vision',
                                   'Unchanged tip support, since the open approach leaves ligaments intact',
                                   'Shorter operating time than endonasal surgery for most primary noses'],
                       'answer': 0,
                       'explanation': 'The open approach gives direct, symmetric, bilateral exposure of the '
                                      'lower lateral cartilages, septum and dorsum in their native position, '
                                      'which helps diagnosis and precise suture and graft work. The costs '
                                      'are wider dissection with longer tip edema, a transcolumellar scar '
                                      'that usually heals well, and disruption of some tip support '
                                      'attachments that must be restored with struts or sutures. Exposure '
                                      'does not eliminate edema, scarring or the need to protect support.',
                       'why_wrong': ['Correct.',
                                     'Wider dissection of the skin envelope causes more and longer-lasting '
                                     'tip edema than endonasal approaches.',
                                     'Degloving divides some support attachments, such as interdomal and '
                                     'scroll connections, which must be rebuilt.',
                                     'Opening and closing add steps, so the open approach is not faster; its '
                                     'value is exposure, not speed.'],
                       'board_pearl': 'Open approach trades a columellar scar, more edema and some support '
                                      'loss for superior exposure.',
                       'curveball': 'During her open approach, which major and minor tip-support structures '
                                    'are vulnerable to the dissection?',
                       'curveball_answer': 'Major supports are the size, shape and strength of the lower '
                                           'lateral cartilages, the attachment of the medial crural '
                                           'footplates to the caudal septum, and the scroll attachment '
                                           'between upper and lower laterals. Minor supports include the '
                                           'interdomal ligament, the dorsal septum, the membranous septum, '
                                           'the nasal spine, sesamoid cartilages and the skin envelope.'},
 'v260_fpt_open_app': {'stem': 'A 25-year-old woman is undergoing open rhinoplasty for a dorsal hump, a '
                               'bulbous tip and a wide bony vault. Exposure is complete. The plan includes '
                               'component hump reduction, cephalic trim, lateral osteotomies and dome '
                               'sutures. The resident proposes performing all resections first and then '
                               'evaluating the nose at the end. Which principle best prevents postoperative '
                               'deformity?',
                       'choices': ['Complete all planned resections first, then assess the final result',
                                   'Make incremental changes and reassess the nose after each maneuver',
                                   'Judge progress mainly on the profile, since frontal views change with '
                                   'edema',
                                   'Rely on the skin envelope to camouflage small framework asymmetries'],
                       'answer': 1,
                       'explanation': 'Rhinoplasty is iterative structural surgery. Each maneuver changes '
                                      'forces and relationships elsewhere: hump reduction opens the roof and '
                                      'affects the middle vault, cephalic trim weakens lateral crura, '
                                      'osteotomies narrow the vault and dome sutures change tip width and '
                                      'rotation. Making conservative incremental changes and reassessing '
                                      'dorsal height and width, tip support, valve function and symmetry '
                                      'from several views prevents cumulative overresection and valve '
                                      'compromise.',
                       'why_wrong': ['Removing all planned tissue before reassessing allows errors to '
                                     'compound and leaves no chance to stop before overresection.',
                                     'Correct.',
                                     'Frontal symmetry, dorsal aesthetic lines and valve function cannot be '
                                     'judged on a profile view alone.',
                                     'Thin or medium skin shows framework irregularities as edema resolves, '
                                     'so the envelope cannot be relied on to hide them.'],
                       'board_pearl': 'Rhinoplasty is iterative: change conservatively, then reassess '
                                      'dorsum, tip support, valves and symmetry each time.',
                       'curveball': 'Why should the surgeon recheck the airway after dorsal and tip '
                                    'maneuvers?',
                       'curveball_answer': 'Hump reduction can drop the upper lateral cartilages into the '
                                           'internal valve, cephalic trim and dome sutures can weaken or '
                                           'medialize the lateral crura and cause external valve collapse, '
                                           'and osteotomies narrow the bony vault. Recognizing these '
                                           'intraoperatively lets spreader grafts or flaps, lateral crural '
                                           'struts or rim grafts be added before closure.'},
 'v260_fpt_open_snr': {'stem': 'Near the end of open rhinoplasty in a 34-year-old man with no preoperative '
                               'valve symptoms, a cephalic trim and tight transdomal sutures have narrowed '
                               'the tip. The remaining lateral crura are now concave, the nostrils look '
                               'pinched, and gentle intranasal pressure shows the lateral walls buckling '
                               'inward. Which action is best before closure?',
                       'choices': ['Close as planned and reassess the airway after one year of healing',
                                   'Trim more of the concave lateral crura to remove the buckled segment',
                                   'Add lateral crural strut or rim grafts to restore lateral wall support',
                                   'Pack the nose firmly to splint the lateral crura while they heal'],
                       'answer': 2,
                       'explanation': 'The narrowing maneuvers have created a structural deficit: weakened, '
                                      'concave lateral crura that will collapse into the external valve with '
                                      'inspiration. A functional deficit created intraoperatively should be '
                                      'corrected when recognized, while exposure is open. Lateral crural '
                                      'strut grafts flatten and stiffen the crura, and alar rim grafts '
                                      'support the margin. Loosening overtight dome sutures may also help. '
                                      'Accepting iatrogenic valve collapse for a narrower tip is not '
                                      'appropriate.',
                       'why_wrong': ['Collapse from concave, weakened crura will not improve with healing; '
                                     'scar contracture usually worsens it, leaving revision surgery.',
                                     'Resecting more lateral crus removes remaining support and worsens '
                                     'external valve collapse and alar retraction.',
                                     'Correct.',
                                     'Packing gives only temporary support; once removed, the weakened crura '
                                     'still collapse, and scar can fix them inward.'],
                       'board_pearl': 'Fix iatrogenic valve weakness before closure; do not trade airway '
                                      'function for a narrower tip.',
                       'curveball': 'Which structural grafts can rescue internal versus external valve '
                                    'collapse found intraoperatively?',
                       'curveball_answer': 'Internal valve collapse at the middle vault is treated with '
                                           'spreader grafts or autospreader flaps, flaring sutures, or a '
                                           'butterfly graft in revisions. External valve collapse at the '
                                           'alar lobule is treated with lateral crural strut grafts, alar '
                                           'rim grafts, alar batten grafts or lateral crural repositioning, '
                                           'matched to the segment that collapses.'},
 'v137_fpt_12': {'stem': 'A 7-year-old girl is teased about prominent ears. Both ears protrude widely, with '
                         'an absent antihelical fold and superior crus, and a deep conchal bowl that keeps '
                         'the helical rim far from the scalp even when the antihelix is folded back by hand. '
                         'Lobules sit normally. The cartilage is soft, and hearing is normal. Which '
                         'operative plan is most appropriate?',
                 'choices': ['Mustarde antihelical sutures alone, tightened to set the concha back',
                             'Postauricular skin excision alone to draw both ears toward the scalp',
                             'Mustarde antihelical sutures with Furnas conchomastoid setback',
                             'Conchal cartilage excision with fishtail lobule repositioning'],
                 'answer': 2,
                 'explanation': 'Prominent-ear surgery is deformity specific. This child has two separate '
                                'causes: an absent antihelical fold and conchal excess, shown by persistent '
                                'protrusion when the antihelix is folded manually. Mustarde horizontal '
                                'mattress sutures recreate the fold, and Furnas conchomastoid sutures set '
                                'the deep concha back toward the mastoid, with limited conchal reduction if '
                                'needed. Treating only one component leaves residual prominence or forces '
                                'overtightening, while the normal lobules need no surgery.',
                 'why_wrong': ['Overtightening fold sutures to hide conchal excess produces a sharp, '
                               'unnatural antihelix and still leaves the concha prominent.',
                               'Skin excision alone does not reshape cartilage, so the ear relapses forward '
                               'as the skin stretches.',
                               'Correct.',
                               'Her lobules are normal, and conchal excision alone leaves the absent '
                               'antihelical fold uncorrected.'],
                 'board_pearl': 'Diagnose each component of ear prominence: antihelix with Mustarde sutures, '
                                'concha with Furnas setback.',
                 'curveball': 'Her parents ask what can go wrong if the permanent otoplasty sutures are tied '
                              'too tightly. What complications can follow?',
                 'curveball_answer': 'Overtight sutures can create a sharp, unnatural antihelical ridge, '
                                     'cartilage cut-through, overcorrection with the ear pinned flat, and a '
                                     'telephone-ear deformity when the middle third is set back more than '
                                     'the poles. Permanent sutures under tension are also more likely to '
                                     'extrude, form granulomas or seed infection and chondritis.'},
 'v147_fp_12': {'stem': 'A 16-year-old boy has bilateral prominent ears from an underdeveloped antihelical '
                        'fold. Conchal depth is normal, and the lobules are normal. When the fold is pressed '
                        'back with a finger, the ear sets back well, but the cartilage is stiff and springs '
                        'forward as soon as pressure is released. Which maneuver best targets his deformity?',
                'choices': ['Furnas conchomastoid sutures with conchal bowl resection',
                            'Postauricular skin excision alone, without cartilage work',
                            'Lobule setback with a fishtail postauricular excision',
                            'Anterior cartilage scoring combined with Mustarde sutures'],
                'answer': 3,
                'explanation': 'His prominence comes from an underdeveloped antihelix, and the concha and '
                               "lobule are normal. Adolescent cartilage is stiffer than a young child's, so "
                               'mattress sutures alone may cut through or relapse. Weakening the anterior '
                               'cartilage surface by light scoring makes the cartilage bend away from the '
                               'scored side, as described by Gibson, and Mustarde sutures then hold a '
                               'smooth, rounded fold. Correction is directed at the antihelix, not at normal '
                               'structures.',
                'why_wrong': ['His concha is normal in depth; setback and resection would overcorrect the '
                              'middle third without creating the missing fold.',
                              'Skin excision does not reshape stiff cartilage, so the ear springs forward '
                              'again after healing.',
                              'His lobules are normal; lobule setback does not address the missing '
                              'antihelical fold.',
                              'Correct.'],
                'board_pearl': 'Stiff adolescent cartilage: anterior scoring plus Mustarde sutures creates a '
                               'smooth, lasting antihelical fold.',
                'curveball': 'What are the drawbacks of anterior cartilage scoring, and how are they '
                             'minimized?',
                'curveball_answer': 'Scoring needs anterior skin elevation, which raises hematoma risk, and '
                                    'overly deep or uneven scoring can leave sharp edges, visible '
                                    'irregularities or a kinked fold. Using light, controlled scoring over a '
                                    'limited area, combining it with sutures rather than relying on it '
                                    'alone, and using careful bolster dressings reduce these problems.'},
 'v262_fpt_otoplasty_fnd': {'stem': 'A 10-year-old boy has bilaterally prominent ears. The antihelical fold '
                                    'and superior crus are flat, while conchal depth is normal and the '
                                    'lobules lie flat. Gentle finger pressure on the scapha recreates a '
                                    'natural fold and brings the helical rim close to the scalp. The '
                                    'cartilage is soft and pliable. Which correction most directly addresses '
                                    'his deformity?',
                            'choices': ['Furnas conchomastoid sutures with conchal bowl reduction',
                                        'Excision of the lobules with posterior skin reduction',
                                        'Mustarde horizontal mattress sutures through the cartilage',
                                        'Postauricular skin excision as the only maneuver'],
                            'answer': 2,
                            'explanation': 'Prominent-ear analysis separates antihelical underfolding, '
                                           'conchal excess and lobular prominence because each needs a '
                                           'different correction. His concha and lobules are normal, and '
                                           'digital pressure recreates the fold and sets the ear back, which '
                                           'isolates the antihelix as the cause. In a child with soft, '
                                           'pliable cartilage, Mustarde horizontal mattress sutures placed '
                                           'through the scapha and concha recreate a smooth fold without '
                                           'cartilage cutting.',
                            'why_wrong': ['His concha is normal in depth; conchal setback and reduction '
                                          'would overcorrect without creating the missing fold.',
                                          'His lobules lie flat, so lobule excision addresses a deformity he '
                                          'does not have.',
                                          'Correct.',
                                          'Skin excision alone does not reshape the flat antihelix and tends '
                                          'to relapse as the skin stretches.'],
                            'board_pearl': 'Isolated antihelical underfolding with soft cartilage: Mustarde '
                                           'mattress sutures recreate the fold.',
                            'curveball': 'How would conchal hypertrophy change the operative plan compared '
                                         'with his isolated antihelical underfolding?',
                            'curveball_answer': 'Conchal hypertrophy or a wide conchomastoid angle needs a '
                                                'separate conchal maneuver, usually Furnas conchomastoid '
                                                'sutures and sometimes limited conchal cartilage excision. '
                                                'Without it, surgeons tend to overtighten the fold sutures '
                                                'to compensate, producing a sharp ridge or telephone-ear '
                                                'deformity. Conchal sutures must avoid pushing the concha '
                                                'into the canal.'},
 'v262_fpt_otoplasty_app': {'stem': 'A 12-year-old girl is seen 3 months after bilateral otoplasty with '
                                    'permanent Mustarde sutures. Both ears are set back, but each antihelix '
                                    'has a sharp, knife-edge ridge rather than a rounded fold. A suture knot '
                                    'is palpable through thin skin on the left, and a small cartilage step '
                                    'is visible along the fold. Which technical error most likely explains '
                                    'these findings?',
                            'choices': ['Insufficient postauricular skin excision at the original operation',
                                        'Furnas sutures placed too far anteriorly on the mastoid fascia',
                                        'Absorbable rather than permanent suture material for the fold',
                                        'Overtightened, closely spaced sutures with narrow cartilage bites'],
                            'answer': 3,
                            'explanation': 'Mustarde sutures should be broad horizontal mattress sutures, '
                                           'spaced to distribute force and recreate a smooth, rounded fold. '
                                           'Overtightening a few closely spaced sutures with small cartilage '
                                           'bites concentrates tension on narrow strips of cartilage, which '
                                           'produces a sharp ridge, can cut through cartilage and pushes '
                                           'knots against thin skin. Gradual, balanced tightening while '
                                           'checking frontal and oblique views prevents these problems.',
                            'why_wrong': ['Skin excision affects ear position only modestly and does not '
                                          'create a sharp cartilage ridge or step.',
                                          'Anterior Furnas placement narrows or distorts the canal; it does '
                                          'not create a sharp antihelical ridge.',
                                          'Absorbable sutures risk relapse of prominence, not a sharp ridge '
                                          'with a palpable knot and cartilage step.',
                                          'Correct.'],
                            'board_pearl': 'Broad, well-spaced Mustarde bites tightened gradually give a '
                                           'smooth fold; tight narrow bites give ridges and cut-through.',
                            'curveball': 'Two weeks later the palpable knot extrudes through the skin with '
                                         'mild redness. How should you manage it?',
                            'curveball_answer': 'Remove the extruded suture, culture any drainage and treat '
                                                'local infection, covering Pseudomonas if chondritis is '
                                                'suspected. Once healed, the fold often keeps much of its '
                                                'shape because scar has formed, but relapse can occur. If '
                                                'prominence returns, revise later with new, well-buried '
                                                'sutures.'},
 'v262_fpt_otoplasty_snr': {'stem': 'A 9-year-old girl has bilateral otoplasty in the morning. That evening '
                                    'her parents call because her left ear has severe, throbbing pain '
                                    'unrelieved by acetaminophen and ibuprofen, and blood is seeping at the '
                                    'edge of the head dressing. The right ear is comfortable. She has no '
                                    'fever. What is the best next step?',
                            'choices': ['Remove the dressing now, inspect the ear and evacuate any hematoma',
                                        'Increase oral analgesia and keep the dressing on until '
                                        'postoperative day 7',
                                        'Reinforce the head bandage more tightly to tamponade the bleeding',
                                        'Start oral antibiotics and review the ear at the 48-hour visit'],
                            'answer': 0,
                            'explanation': 'Severe unilateral pain in the hours after otoplasty is a '
                                           'hematoma until proven otherwise. Blood under the skin separates '
                                           'perichondrium from cartilage, which threatens cartilage '
                                           'viability and can lead to infection, necrosis and cauliflower '
                                           'deformity. The dressing should be removed promptly for '
                                           'inspection, and a hematoma should be evacuated with bleeding '
                                           'controlled, followed by a well-padded, nonconstrictive dressing. '
                                           'Analgesia should not mask the problem.',
                            'why_wrong': ['Correct.',
                                          'Waiting until day 7 lets a hematoma devascularize cartilage and '
                                          'raises the risk of infection and deformity.',
                                          'A tighter bandage cannot evacuate clot and increases pressure on '
                                          'already threatened skin and cartilage.',
                                          'Antibiotics do not address a blood collection, and a 48-hour '
                                          'delay risks cartilage necrosis.'],
                            'board_pearl': 'Severe unilateral pain after otoplasty means hematoma until '
                                           'proven otherwise: remove the dressing and evacuate.',
                            'curveball': 'How does perichondritis differ from an acute hematoma in timing '
                                         'and management priorities?',
                            'curveball_answer': 'Hematoma appears within hours to a day as tense, painful '
                                                'swelling and needs prompt evacuation and a padded dressing. '
                                                'Perichondritis usually develops days later with spreading '
                                                'redness, warmth and tenderness, often sparing the lobule, '
                                                'and needs antipseudomonal antibiotics such as '
                                                'ciprofloxacin, plus drainage or debridement of abscess or '
                                                'nonviable cartilage.'},
 'v137_fpt_13': {'stem': 'A 72-year-old man has a full-thickness defect of the central lower eyelid '
                         'involving about 60% of the lid width after Mohs surgery for basal cell carcinoma. '
                         'The lateral and medial canthi are intact. Vision is good in both eyes, and he '
                         'accepts a period of eye closure. Margins are clear. Which reconstruction is most '
                         'appropriate?',
                 'choices': ['Direct closure with lateral canthotomy and inferior cantholysis',
                             'Free tarsoconjunctival graft covered by a full-thickness skin graft',
                             'Hughes tarsoconjunctival flap with full-thickness skin graft',
                             'Healing by secondary intention with lubrication and taping'],
                 'answer': 2,
                 'explanation': 'Large full-thickness lower lid defects require reconstruction of both '
                                'lamellae and stable horizontal support to protect the globe. A Hughes flap '
                                'advances vascularized tarsus and conjunctiva from the upper lid to replace '
                                'the posterior lamella, and a full-thickness skin graft replaces the '
                                'anterior lamella. Because one layer is vascularized, the other can be a '
                                'free graft. The flap is divided after several weeks, and he accepts '
                                'temporary closure because his other eye sees well.',
                 'why_wrong': ['Canthotomy with cantholysis extends direct closure only to moderate defects; '
                               'a 60% defect would close under excessive tension.',
                               'Two free grafts lack any vascularized layer to nourish each other, so '
                               'failure and lid retraction are likely.',
                               'Correct.',
                               'A full-thickness margin defect will notch, retract and expose the cornea if '
                               'left to heal on its own.'],
                 'board_pearl': 'Large full-thickness lower lid defects: rebuild both lamellae, with at '
                                'least one vascularized.',
                 'curveball': 'Why should at least one lamella be vascularized when the other is a free '
                              'graft?',
                 'curveball_answer': 'Free grafts survive only by imbibition and inosculation from an '
                                     'adjacent blood supply. In an eyelid, the two lamellae lie against each '
                                     'other, so one must carry its own circulation, such as a Hughes flap or '
                                     'myocutaneous advancement flap, to nourish the other. Two free grafts '
                                     'together lack a bed and usually fail or contract.'},
 'v142_fpt_03': {'stem': 'A 68-year-old woman has a full-thickness defect of the lateral lower eyelid '
                         'involving about 55% of the lid width after Mohs surgery. Her fellow eye has poor '
                         'central vision from macular degeneration, so she relies on the operated eye and '
                         'cannot tolerate weeks of lid closure. Direct closure with cantholysis is too '
                         'tight. Which reconstruction is most appropriate?',
                 'choices': ['Free tarsoconjunctival graft beneath a myocutaneous advancement flap',
                             'Hughes tarsoconjunctival flap with a skin graft over the flap',
                             'Free tarsoconjunctival graft with a full-thickness skin graft over it',
                             'Direct closure under tension with a temporary tarsorrhaphy suture'],
                 'answer': 0,
                 'explanation': 'Both lamellae must be rebuilt, with at least one vascularized. A Hughes '
                                'flap would close her better-seeing eye for weeks, which she cannot '
                                'tolerate. A single-stage option uses a free tarsoconjunctival graft from '
                                'the upper lid for the posterior lamella, nourished by a vascularized '
                                'orbicularis myocutaneous advancement flap or a semicircular rotation flap '
                                'for the anterior lamella. Lateral canthal fixation provides horizontal '
                                'support while vertical tension is avoided.',
                 'why_wrong': ['Correct.',
                               'A Hughes flap occludes the visual axis for several weeks, which is '
                               'unacceptable when this is her better-seeing eye.',
                               'Two free grafts without a vascularized layer are likely to fail, contract '
                               'and retract the lid.',
                               'Closing a 55% defect under tension risks dehiscence, notching and lid '
                               'malposition even with temporary tarsorrhaphy.'],
                 'board_pearl': 'When lid closure is unacceptable, use a free tarsal graft under a '
                                'vascularized myocutaneous flap.',
                 'curveball': 'How would involvement of the medial canthus change your concern for the '
                              'lacrimal drainage system?',
                 'curveball_answer': 'Medial defects can transect the inferior canaliculus or detach the '
                                     'medial canthal tendon. Probe and irrigate to identify injured '
                                     'canaliculi, repair them over a silicone stent such as a '
                                     'monocanalicular or bicanalicular tube, reattach the tendon to the '
                                     'posterior lacrimal crest, and warn about epiphora if the system cannot '
                                     'be preserved.'},
 'v261_fpt_periocular_fnd': {'stem': 'An 80-year-old man has a 1.5 cm vertical by 2 cm horizontal anterior '
                                     'lamellar defect of the right lower eyelid after Mohs surgery, '
                                     'beginning 2 mm below the lash line. Tarsus and conjunctiva are intact. '
                                     'He has mild lid laxity. The resident proposes closing it vertically '
                                     'from adjacent cheek skin because the color match is excellent. Which '
                                     'repair best fits his priorities?',
                             'choices': ['Vertical primary closure using cheek skin for color match',
                                         'Secondary-intention healing with antibiotic ointment alone',
                                         'Split-thickness skin graft from the anterior thigh with bolster',
                                         'Upper eyelid full-thickness graft with lateral canthal support'],
                             'answer': 3,
                             'explanation': 'Periocular reconstruction protects the globe first: blink, '
                                            'closure, lid margin position and apposition matter before '
                                            'cosmetic refinement. A vertical closure or secondary healing '
                                            'just below the lash line pulls the lid down, causing ectropion, '
                                            'exposure keratopathy and epiphora, especially with laxity. An '
                                            'upper eyelid full-thickness graft gives thin, matching anterior '
                                            'lamella with less contraction, and lateral canthal support '
                                            'resists downward pull while it heals.',
                             'why_wrong': ['A vertical closure below the lash line pulls the lax lid margin '
                                           'down and risks ectropion despite the good color match.',
                                           'Secondary healing near the margin contracts vertically and is '
                                           'likely to cause ectropion and exposure.',
                                           'A thigh split-thickness graft is thick, poorly matched and '
                                           'contracts more, which risks lid retraction.',
                                           'Correct.'],
                             'board_pearl': 'Protect lid position before cosmesis: avoid vertical tension on '
                                            'the lower lid margin in anterior lamellar repair.',
                             'curveball': 'Which structures form the anterior and posterior lamellae of the '
                                          'eyelid, and why does the distinction matter?',
                             'curveball_answer': 'The anterior lamella is skin and orbicularis oculi. The '
                                                 'posterior lamella is tarsus and conjunctiva, with the lid '
                                                 'retractors attaching to it. The orbital septum lies '
                                                 'between them. Defects are classified by lamella so each '
                                                 'missing layer is replaced; replacing only skin over a '
                                                 'missing tarsus produces an unstable, retracting lid.'},
 'v261_fpt_periocular_app': {'stem': 'A 75-year-old woman has a large anterior lamellar defect of the left '
                                     'lower eyelid extending 3 cm onto the upper cheek after Mohs surgery. '
                                     'Tarsus is intact. Snap-back is slow, and the lid distracts 9 mm from '
                                     'the globe. A Mustarde cheek rotation flap is planned. Which design '
                                     'feature best reduces postoperative ectropion risk?',
                             'choices': ['A low lateral incision that starts below the level of the lateral '
                                         'canthus',
                                         'A high lateral arc, periosteal anchoring and a lateral canthal '
                                         'tightening',
                                         'Reliance on a temporary Frost suture as the only lid support',
                                         'A vertical closure of the cheek part of the defect toward the jaw'],
                             'answer': 1,
                             'explanation': 'Lower lid and cheek reconstruction must resist gravity and scar '
                                            'contracture. A Mustarde flap should begin with a high arc above '
                                            'the lateral canthus toward the temple, so rotation lifts rather '
                                            'than drags the lid. Deep sutures anchor the flap to periosteum '
                                            'of the lateral orbital rim to take weight off the lid. Her '
                                            'marked laxity needs a lateral canthoplasty or tarsal strip, and '
                                            'wide undermining keeps tension horizontal.',
                             'why_wrong': ['A low lateral incision creates a downward rotation vector that '
                                           'pulls the lid margin into ectropion.',
                                           'Correct.',
                                           'A Frost suture supports the lid only briefly; once removed, her '
                                           'lax lid will be pulled down by the heavy flap.',
                                           'Vertical closure creates a downward vector on the lid and adds '
                                           'to ectropion risk.'],
                             'board_pearl': 'Mustarde cheek flaps need a high lateral arc, periosteal '
                                            'anchoring and canthal support to prevent ectropion.',
                             'curveball': 'When is a canthopexy sufficient, and when is a canthoplasty such '
                                          'as a lateral tarsal strip preferred?',
                             'curveball_answer': 'A canthopexy tightens the intact lateral canthal tendon '
                                                 'with sutures and suits mild laxity or prophylactic '
                                                 'support. A canthoplasty, usually a lateral tarsal strip, '
                                                 'divides and shortens the lid, then reattaches it to '
                                                 'lateral orbital rim periosteum, and is preferred for '
                                                 'marked laxity or existing ectropion, as in this patient.'},
 'v261_fpt_periocular_snr': {'stem': 'A 66-year-old man taking clopidogrel underwent lower eyelid '
                                     'reconstruction 6 hours ago. He now has severe left eye pain, '
                                     'proptosis, a tense orbit resistant to retropulsion, and vision reduced '
                                     'from 20/25 to counting fingers, with a left relative afferent '
                                     'pupillary defect. Intraocular pressure is 52 mm Hg. What is the best '
                                     'immediate response?',
                             'choices': ['Obtain an urgent CT of the orbits before deciding on any '
                                         'intervention',
                                         'Start IV mannitol and acetazolamide and wait for the imaging '
                                         'results',
                                         'Perform a lateral canthotomy and inferior cantholysis at the '
                                         'bedside',
                                         'Remove the skin sutures and reassess the vision the next morning'],
                             'answer': 2,
                             'explanation': 'Pain, proptosis, a tense orbit, falling vision, an afferent '
                                            'pupillary defect and high pressure after eyelid surgery '
                                            'indicate orbital compartment syndrome, usually from retrobulbar '
                                            'hemorrhage. Optic nerve and retinal ischemia become '
                                            'irreversible quickly, so decompression should not wait for '
                                            'imaging. Remove constricting dressings and open the closure, '
                                            'then perform lateral canthotomy with inferior cantholysis, '
                                            'reassess vision and pressure, and escalate if the orbit stays '
                                            'tight.',
                             'why_wrong': ['Imaging delays decompression when the clinical diagnosis is '
                                           'clear, and vision loss may become permanent during that delay.',
                                           'Medical therapy is an adjunct only and cannot decompress a '
                                           'hemorrhage in the closed orbital compartment.',
                                           'Correct.',
                                           'Waiting until morning allows irreversible optic nerve ischemia; '
                                           'skin suture removal alone does not decompress the orbit.'],
                             'board_pearl': 'Orbital compartment syndrome is a clinical diagnosis: perform '
                                            'canthotomy and cantholysis without waiting for CT.',
                             'curveball': 'Which bedside findings support immediate lateral canthotomy and '
                                          'cantholysis rather than further observation?',
                             'curveball_answer': 'Decreasing visual acuity, a new afferent pupillary defect, '
                                                 'proptosis with a tense globe resistant to retropulsion, '
                                                 'markedly raised intraocular pressure, restricted eye '
                                                 'movements, and severe pain after surgery or trauma. In an '
                                                 'unresponsive patient, a tense orbit with high pressure is '
                                                 'enough to proceed.'},
 'v137_fpt_14': {'stem': 'A 40-year-old woman has bilateral nasal obstruction after a prior reduction '
                         'rhinoplasty. The middle third is pinched with narrowed dorsal aesthetic lines, the '
                         'upper lateral cartilages collapse inward on inspiration, and a modified Cottle '
                         'maneuver at the internal valve relieves her symptoms. Her tip is well supported, '
                         'and her alar rims are normal. Which graft most directly corrects her problem?',
                 'choices': ['Columellar strut graft placed between the medial crura',
                             'Alar rim grafts placed in pockets along both nostril margins',
                             'Diced cartilage in fascia as an onlay over the dorsum',
                             'Spreader grafts fixed along both sides of the septum'],
                 'answer': 3,
                 'explanation': 'Her problem is middle-vault collapse with internal valve narrowing after '
                                'reduction rhinoplasty, confirmed by the modified Cottle maneuver. Spreader '
                                'grafts placed between the dorsal septum and upper lateral cartilages '
                                'restore middle-vault width, widen the internal valve angle and stiffen the '
                                'sidewall, while also restoring dorsal aesthetic lines. Her tip and alar '
                                'rims are normal, so grafts aimed there do not address the failure.',
                 'why_wrong': ['A columellar strut supports tip projection, which is already adequate, and '
                               'does not widen the internal valve.',
                               'Rim grafts support the alar margin at the external valve; her rims are '
                               'normal and the collapse is at the middle vault.',
                               'Dorsal onlay grafts restore height and contour, but placed over the dorsum '
                               'they do not widen or stiffen the valve.',
                               'Correct.'],
                 'board_pearl': 'Pinched middle vault with internal valve collapse: spreader grafts widen '
                                'the valve and restore dorsal lines.',
                 'curveball': 'Her septal cartilage was depleted at the prior surgery. Which materials can '
                              'be used for spreader grafts instead?',
                 'curveball_answer': 'Autologous costal cartilage is the most reliable alternative, '
                                     'providing straight, strong stock that can be carved into thin '
                                     'spreaders. Conchal cartilage can be used but is curved and weaker. '
                                     'Irradiated homologous costal cartilage is an option in selected '
                                     'patients, with some concern about resorption.'},
 'v143_fpt_05': {'stem': 'A 37-year-old man has left nasal obstruction 2 years after a nasal fracture. The '
                         'cartilaginous dorsum deviates to the right, the left middle vault is narrow with a '
                         'concave left dorsal aesthetic line, and the left internal valve opens with a '
                         'modified Cottle maneuver. The caudal septum and tip are midline. Which graft '
                         'strategy best addresses his deformity?',
                 'choices': ['Columellar strut graft to reinforce tip support',
                             'Shield tip graft to camouflage the deviated dorsum',
                             'Asymmetric spreader grafts to splint the dorsal septum',
                             'Temporalis fascia onlay over the concave dorsal side'],
                 'answer': 2,
                 'explanation': 'His crooked cartilaginous dorsum and narrow left middle vault come from a '
                                'deviated dorsal septum. Spreader grafts, often thicker or doubled on the '
                                'concave side, splint and straighten the dorsal septum, widen the narrow '
                                'internal valve and even out the dorsal aesthetic lines. Septal scoring or '
                                'release may be added to the deviated segment. His caudal septum and tip are '
                                'midline, so grafts there are not needed.',
                 'why_wrong': ['His tip and caudal septum are midline and supported, so a strut does not '
                               'correct dorsal deviation or the narrow left valve.',
                               'A tip graft changes tip definition and does not straighten the dorsum or '
                               'widen the internal valve.',
                               'Correct.',
                               'Fascia can smooth a contour but cannot straighten the dorsal septum or '
                               'support the collapsing valve.'],
                 'board_pearl': 'Deviated dorsal septum with a narrow valve: asymmetric spreader grafts '
                                'straighten the dorsum and open the valve.',
                 'curveball': 'When might autospreader flaps or lateral wall suspension sutures be '
                              'preferable or additive to spreader grafts?',
                 'curveball_answer': 'Autospreader flaps suit patients having hump reduction, where excess '
                                     'upper lateral height can be folded in, but they straighten a crooked '
                                     'dorsal septum less well. Lateral wall suspension or flaring sutures '
                                     'add support when sidewall collapse persists despite a widened valve '
                                     'angle, and are often combined with spreaders.'},
 'v260_fpt_grafts_fnd': {'stem': 'A 32-year-old woman undergoing primary septorhinoplasty needs a caudal '
                                 'septal extension graft for tip rotation and projection, plus bilateral '
                                 'alar rim grafts for mild notching. The plan uses straight septal cartilage '
                                 'for the extension graft and curved conchal cartilage for the rim grafts. A '
                                 'junior resident asks why one donor is not used for both. Which principle '
                                 'best explains the plan?',
                         'choices': ['Use septal cartilage for every graft, as it is the best donor',
                                     'Take ear cartilage for all grafts to avoid weakening the septum',
                                     'Choose the donor that leaves the least visible scar for each graft',
                                     "Match each donor's strength and shape to the graft's mechanical job"],
                         'answer': 3,
                         'explanation': 'Graft selection is task specific. A septal extension graft bears '
                                        'load to set tip position, so it needs straight, stiff cartilage, '
                                        'which septum provides. Rim grafts need small, flexible pieces that '
                                        'follow the curve of the alar margin, which conchal cartilage '
                                        'provides. Septal supply is finite and must leave an adequate '
                                        'L-strut, and choosing material for each job uses it efficiently. '
                                        'Costal cartilage is reserved for large load-bearing needs when '
                                        'septum is lacking.',
                         'why_wrong': ['Septal cartilage is finite and must leave an adequate L-strut; using '
                                       'it for every graft wastes stock where curvature helps.',
                                       'Conchal cartilage is curved and weaker, so it is a poor choice for a '
                                       'load-bearing caudal septal extension graft.',
                                       'Scar visibility matters, but the deciding factor is whether the '
                                       'cartilage can do the mechanical job required.',
                                       'Correct.'],
                         'board_pearl': 'Choose cartilage by mechanical job: straight, stiff septum for load '
                                        'bearing; curved concha for contour.',
                         'curveball': 'Which donor is especially useful when a curved alar or lateral wall '
                                      'contour is desired, and why?',
                         'curveball_answer': 'Conchal cartilage has a natural curvature that matches the '
                                             'alar lobule and lateral wall, so it is well suited to alar '
                                             'batten grafts, rim grafts and some lateral crural '
                                             'replacements. It is harvested through an anterior or posterior '
                                             'incision with little deformity if the antihelix is preserved, '
                                             'but it is weaker than septum or rib.'},
 'v260_fpt_grafts_app': {'stem': 'A 29-year-old woman with no prior nasal surgery has bilateral obstruction '
                                 'on exertion. The lateral crura are concave, lie in a normal orientation, '
                                 'and buckle inward on moderate inspiration, narrowing the nostrils. Tip '
                                 'projection and rotation are good, the septum is straight, and the internal '
                                 'valve is normal. Which graft most directly addresses the problem?',
                         'choices': ['Columellar strut graft to increase tip projection and support',
                                     'Cephalic trim to reduce the concave lateral crural segment',
                                     'Spreader grafts to widen the internal valve at the middle vault',
                                     'Lateral crural strut grafts to flatten and stiffen the crura'],
                         'answer': 3,
                         'explanation': 'Her external valve collapse comes from intrinsically weak, concave '
                                        'lateral crura in a normal orientation. Lateral crural strut grafts '
                                        'are sutured to the undersurface of the crura to flatten the '
                                        'concavity and stiffen them against inspiratory collapse, and can be '
                                        'extended to the piriform aperture if needed. Her tip, septum and '
                                        'internal valve are normal, so grafts aimed there do not address the '
                                        'failing segment. Removing cartilage would weaken the crura further.',
                         'why_wrong': ['Tip projection is already good, and a columellar strut does not '
                                       'stiffen the collapsing lateral crura.',
                                       'Trimming weak, concave crura removes support and worsens external '
                                       'valve collapse.',
                                       'Her internal valve is normal, so spreader grafts do not address '
                                       'collapse at the alar lobule.',
                                       'Correct.'],
                         'board_pearl': 'Concave, weak lateral crura causing external valve collapse: '
                                        'lateral crural strut grafts flatten and stiffen them.',
                         'curveball': 'How do alar batten grafts and lateral crural strut grafts differ in '
                                      'position and mechanical effect?',
                         'curveball_answer': 'Lateral crural struts are sutured directly to the undersurface '
                                             'of the lateral crura, reshaping and stiffening the crus itself '
                                             'and sometimes repositioning it. Alar batten grafts sit in a '
                                             'pocket over or caudal to the crus at the point of maximal '
                                             'collapse, often reaching the piriform aperture, and splint the '
                                             'lateral wall without reshaping the crus.'},
 'v260_fpt_grafts_snr': {'stem': 'A 45-year-old woman has had three prior rhinoplasties and now has a low, '
                                 'irregular dorsum, a deviated, weak caudal septum and nasal obstruction. '
                                 'Palpation and CT show only a thin residual septal plate, and both conchae '
                                 'were harvested before. She wants a stable long-term result and is a '
                                 'nonsmoker. Which graft source is most appropriate for major dorsal and '
                                 'caudal reconstruction?',
                         'choices': ['Scarred residual septal remnants harvested for all the grafts',
                                     'Autologous costal cartilage carved to limit graft warping',
                                     'Laminated conchal remnants for the caudal septal replacement graft',
                                     'Porous polyethylene implants for the dorsum and caudal septum'],
                         'answer': 1,
                         'explanation': 'Major revision reconstruction of the dorsum and caudal septum needs '
                                        'abundant, straight, strong cartilage. With septum and conchae '
                                        'depleted, autologous costal cartilage is the preferred source. Its '
                                        'drawbacks are warping, a chest donor site with pain and small '
                                        'pneumothorax risk, and calcification with age. Careful carving of '
                                        'balanced cross sections, observation for warping before fixation, '
                                        'laminated or diced constructs and stable fixation reduce these '
                                        'risks.',
                         'why_wrong': ['A thin, scarred residual plate cannot supply the volume or strength '
                                       'needed and harvesting it risks L-strut collapse.',
                                       'Correct.',
                                       'Conchal remnants are curved, weak and limited, so even laminated '
                                       'they cannot reliably replace a load-bearing caudal septum.',
                                       'Alloplastic implants in a thin, multiply operated envelope carry '
                                       'real risks of infection and extrusion.'],
                         'board_pearl': 'Depleted septum and ear in revision rhinoplasty: costal cartilage '
                                        'supplies strong, abundant graft material.',
                         'curveball': 'Her surgeon worries about rib grafts bending after placement. What '
                                      'strategies reduce clinically significant costal cartilage warping?',
                         'curveball_answer': 'Carve balanced, concentric cross sections from the central '
                                             'core, waiting before final fixation to see how pieces warp. '
                                             'Laminate opposing segments or splint with thin bone or a fine '
                                             'wire, and use diced cartilage wrapped in fascia for dorsal '
                                             'augmentation, which does not warp. Rigid fixation to stable '
                                             'structures limits drift.'},
 'v137_fpt_15': {'stem': 'A 35-year-old woman with Fitzpatrick type III skin had a jawline laceration '
                         'repaired 4 months ago. The scar is raised, pink and itchy but stays within the '
                         'original wound edges, and it does not tether the lip or limit movement. She has no '
                         'personal or family history of keloids and asks what can be done now. What is the '
                         'most appropriate first-line plan?',
                 'choices': ['Excision and re-closure now, under similar tension',
                             'Excision followed by adjuvant superficial radiation',
                             'Silicone, sun protection and steroid injection if it persists',
                             'Ablative CO2 resurfacing of the entire cheek subunit'],
                 'answer': 2,
                 'explanation': 'A raised scar that stays within the wound edges is a hypertrophic scar, '
                                'which often regresses as it matures over 12 to 18 months. First-line care '
                                'is conservative: silicone gel or sheeting, massage and pressure where '
                                'practical, strict sun protection to limit hyperpigmentation, and '
                                'intralesional triamcinolone for persistent thickness or itching. Surgical '
                                'revision is deferred until the scar matures unless there is a functional '
                                'problem, and radiation is reserved for keloids.',
                 'why_wrong': ['Revising an immature hypertrophic scar under the same tension tends to '
                               'recreate the same scar and loses the benefit of maturation.',
                               'Radiation carries long-term risks and is reserved for recurrent or high-risk '
                               'keloids, not a maturing hypertrophic scar.',
                               'Correct.',
                               'Full-subunit ablative resurfacing adds pigment risk in type III skin and '
                               "does not address a raised scar's dermal thickening."],
                 'board_pearl': 'Hypertrophic scars stay within the wound; treat with silicone, sun '
                                'protection and steroid before considering revision.',
                 'curveball': 'If this scar were instead a true keloid, how would recurrence counseling and '
                              'adjuvant treatment change?',
                 'curveball_answer': 'Keloids recur frequently after excision alone, so excision is combined '
                                     'with adjuvant therapy such as serial intralesional triamcinolone, with '
                                     'or without 5-fluorouracil, pressure earrings for lobule keloids, or '
                                     'postoperative radiation for refractory cases. Counsel that recurrence '
                                     'remains possible despite treatment and that follow-up lasts at least a '
                                     'year.'},
 'v147_fp_14': {'stem': 'A 28-year-old man with Fitzpatrick type II skin had a forehead laceration repaired '
                        '4 months ago. The scar is mildly raised and itchy, stays within the original wound '
                        'borders, and is strikingly red, blanching with pressure. He has no history of '
                        'keloids and wants the redness improved before his wedding in 3 months. Which '
                        'management is most reasonable?',
                'choices': ['Weekly intralesional 5-fluorouracil mixed with triamcinolone',
                            'Pulsed dye laser with silicone gel and strict sun protection',
                            'Scar excision with a running W-plasty closure performed now',
                            'Topical hydroquinone applied twice daily to bleach the red scar'],
                'answer': 1,
                'explanation': 'This is a maturing hypertrophic scar whose main problem is persistent '
                               'erythema from vascular proliferation. Pulsed dye laser targets hemoglobin '
                               'and reduces redness, itching and some thickness, and works well in fair '
                               'skin. Silicone gel and sun protection support maturation and limit pigment '
                               'change. Hypertrophic scars differ from keloids by staying within the wound '
                               'and often regressing, so treatment is staged around maturation, symptoms and '
                               'the vascular or pigment component.',
                'why_wrong': ['Weekly 5-FU with steroid is an aggressive regimen for keloids or resistant '
                              'scars and risks atrophy in a mildly raised scar.',
                              'Correct.',
                              'Revising an immature scar at 4 months risks recreating an active scar, and he '
                              'has no tension or orientation problem to correct.',
                              'His redness is vascular, not pigmentary; hydroquinone treats melanin and will '
                              'not reduce blanching erythema.'],
                'board_pearl': 'Red, maturing hypertrophic scar: pulsed dye laser treats the vascular '
                               'component; add silicone and sun protection.',
                'curveball': 'What clinical feature would make a keloid diagnosis more likely than a '
                             'hypertrophic scar?',
                'curveball_answer': 'A keloid extends beyond the original wound margins into normal skin, '
                                    'keeps enlarging after the first several months rather than regressing, '
                                    'and recurs often after excision alone. It is more common in darker '
                                    'skin, on the earlobe, jawline, chest and shoulders, and in patients '
                                    'with a personal or family history.'},
 'v261_fpt_scar_fnd': {'stem': 'A 22-year-old woman had a 3 cm cheek laceration from broken glass repaired 6 '
                               'weeks ago after thorough irrigation, and ultrasound showed no retained '
                               'fragments. The scar is now pink, firm and mildly raised along its whole '
                               'length but stays within the original wound edges. It is mildly itchy, and '
                               'she has no keloid history. Which diagnosis best fits?',
                       'choices': ['Immature hypertrophic scar during active remodeling',
                                   'Keloid that has not yet spread beyond the wound',
                                   'Foreign-body granuloma from a retained glass fragment',
                                   'Mature scar whose final appearance is now fixed'],
                       'answer': 0,
                       'explanation': 'At 6 weeks, scars are in the proliferative and early remodeling '
                                      'phases, when collagen deposition and vascularity peak, so pink, firm, '
                                      'mildly raised scars confined to the wound are common and often '
                                      'improve. This is an immature hypertrophic scar. Initial care includes '
                                      'sun protection, silicone therapy and massage, with intralesional '
                                      'steroid considered for progressive thickening. Final appearance is '
                                      'judged after maturation, usually 12 to 18 months.',
                       'why_wrong': ['Correct.',
                                     'A keloid is defined by growth beyond the wound edges; a scar confined '
                                     'to the wound at 6 weeks is hypertrophic or simply immature.',
                                     'A granuloma is usually a focal nodule, and ultrasound found no '
                                     'fragment; uniform thickening along the whole scar suggests healing.',
                                     'Scars keep remodeling for 12 to 18 months, so a 6-week scar is far '
                                     'from mature and will change.'],
                       'board_pearl': 'Pink, firm scars confined to the wound in the first months are '
                                      'immature or hypertrophic, not keloids.',
                       'curveball': 'How do silicone products and massage help a maturing scar, and when '
                                    'should she start them?',
                       'curveball_answer': 'Silicone gel or sheeting occludes and hydrates the stratum '
                                           'corneum, which reduces keratinocyte signaling to fibroblasts and '
                                           'lowers collagen production, flattening and softening the scar. '
                                           'Massage helps remodel collagen and reduce tethering. Both can '
                                           'begin once the wound is fully epithelialized and should continue '
                                           'daily for several months.'},
 'v261_fpt_scar_app': {'stem': 'A 40-year-old man has a 4 cm scar of the left cheek from a bicycle crash '
                               'repaired in the emergency department 2 years ago. The scar runs '
                               'perpendicular to the relaxed skin tension lines, is widened to 5 mm, and is '
                               'depressed below the surrounding skin. It is pale, flat, soft and not '
                               'contracted. He wants it less noticeable. Which revision plan is most '
                               'appropriate?',
                       'choices': ['Excise and close in a single layer as at the original repair',
                                   'Inject intralesional triamcinolone into the depressed scar',
                                   'Fractional ablative laser as the sole revision treatment',
                                   'Excise, evert in layers and reorient with geometric closure'],
                       'answer': 3,
                       'explanation': 'Scar revision succeeds when the cause of poor appearance is '
                                      'corrected. This mature scar is wide and depressed because it lies '
                                      'across tension lines and was closed under tension without enough deep '
                                      'support. Revision should excise the scar, undermine, close in layers '
                                      'with deep dermal sutures and eversion to reduce tension and restore '
                                      'contour, and reorient or break up the line with a Z-plasty, W-plasty '
                                      'or geometric broken-line closure so segments fall closer to the '
                                      'tension lines.',
                       'why_wrong': ['Repeating the same single-layer closure across tension lines will '
                                     'widen and depress the scar again.',
                                     'Steroid thins and depresses tissue further; it is used for raised '
                                     'scars, not atrophic, widened ones.',
                                     'Laser can refine texture after revision but cannot narrow a widened '
                                     'scar or change its orientation.',
                                     'Correct.'],
                       'board_pearl': 'Revise scars by fixing the cause: reduce tension, evert in layers and '
                                      'reorient toward relaxed skin tension lines.',
                       'curveball': 'When are Z-plasty or geometric broken-line techniques useful in scar '
                                    'revision, and when are they unnecessary?',
                       'curveball_answer': 'Z-plasty lengthens contracted scars and reorients a limb toward '
                                           'relaxed skin tension lines, useful for webbing or scars crossing '
                                           'tension lines. W-plasty and geometric broken lines camouflage '
                                           'long straight scars by breaking up light reflection. They are '
                                           'unnecessary for short scars already in tension lines or natural '
                                           'creases, where simple fusiform excision suffices.'},
 'v261_fpt_scar_snr': {'stem': 'A 45-year-old woman had a total thyroidectomy 3 months ago. Her transverse '
                               'cervical scar is red and firm but lies in a natural skin crease and does not '
                               'tether or limit neck movement. She has no keloid history. She is unhappy '
                               'with its appearance and requests surgical revision now. What is the best '
                               'counseling?',
                       'choices': ['Immediate excision and re-closure to restart scar healing',
                                   'Biweekly intralesional steroid injections until the scar flattens',
                                   'Prophylactic superficial radiation to prevent keloid formation',
                                   'Continue silicone and sun protection, and reassess after maturation'],
                       'answer': 3,
                       'explanation': 'At 3 months the scar is still remodeling, and redness and firmness '
                                      'usually improve over 12 to 18 months. Without contracture, webbing or '
                                      'distortion, revision now would cut through active scar and may '
                                      'recreate the same problem. Silicone, massage, sun protection and '
                                      'pulsed dye laser for persistent redness can optimize the scar while '
                                      'it matures, after which the final result can be judged and revised if '
                                      'still needed.',
                       'why_wrong': ['Revising a 3-month scar without a functional indication interrupts '
                                     'maturation and often reproduces an active, red scar.',
                                     'Frequent steroid injections into a flat, nonhypertrophic scar risk '
                                     'atrophy, hypopigmentation and telangiectasia.',
                                     'Radiation has long-term risks, including in the thyroid bed region, '
                                     'and is not indicated without a keloid history.',
                                     'Correct.'],
                       'board_pearl': 'Allow scars to mature before revision unless contracture or '
                                      'distortion demands earlier intervention.',
                       'curveball': 'Which functional problems would justify earlier surgical intervention '
                                    'on a scar despite its immaturity?',
                       'curveball_answer': 'Contracture limiting neck extension or jaw opening, webbing '
                                           'across a flexion crease, ectropion or lagophthalmos from an '
                                           'eyelid or cheek scar, lip eversion or oral incompetence, and '
                                           'alar or nostril distortion threatening the airway justify '
                                           'earlier release with Z-plasty, grafts or flaps, rather than '
                                           'waiting for full maturation.'},
 'v431-laryngeal-fracture-01': {'stem': 'A 31-year-old man rode a dirt bike into a wire fence 1 hour ago. He '
                                        'speaks calmly in full sentences with mild hoarseness and anterior '
                                        'neck tenderness. There is no stridor, hemoptysis or subcutaneous '
                                        'emphysema, and oxygen saturation is 99% on room air. The cervical '
                                        'spine is immobilized pending imaging. What is the most appropriate '
                                        'next step?',
                                'choices': ['Discharge home with voice rest, as he is breathing normally',
                                            'Flexible laryngoscopy in a monitored area with airway backup',
                                            'Rapid-sequence oral intubation to protect against later edema',
                                            'Plain neck radiographs, with discharge if no fracture is shown'],
                                'answer': 1,
                                'explanation': 'Symptom severity does not reliably grade laryngeal injury. A '
                                               'patient speaking calmly after a clothesline mechanism can '
                                               'develop progressive edema or hematoma over hours. Evaluation '
                                               'proceeds in a monitored setting with the team prepared to '
                                               'secure the airway: flexible laryngoscopy assesses mucosa, '
                                               'hematoma, fold mobility and airway caliber, followed by '
                                               'fine-cut CT of the larynx once safe. Cervical spine '
                                               'precautions continue, and trauma, anesthesia and ENT '
                                               'coordinate care.',
                                'why_wrong': ['Mild symptoms do not exclude serious injury, and edema can '
                                              'progress after discharge to life-threatening obstruction.',
                                              'Correct.',
                                              'Intubating a stable airway blindly risks converting a partial '
                                              'injury into complete obstruction or a false passage.',
                                              'Plain films miss most laryngeal fractures and do not assess '
                                              'mucosa, hematoma or fold mobility.'],
                                'board_pearl': 'Calm speech after anterior neck trauma does not exclude '
                                               'laryngeal injury; scope him with airway backup ready.',
                                'curveball': 'If laryngoscopy shows a clearly unstable framework with a '
                                             'narrowing airway, which airway approach is favored?',
                                'curveball_answer': 'A controlled surgical airway below the injury, usually '
                                                    'awake tracheostomy under local anesthesia, is favored '
                                                    'with an unstable framework or major disruption. '
                                                    'Controlled fiberoptic intubation with immediate '
                                                    'surgical backup is an alternative in selected stable '
                                                    'patients, chosen by anatomy and expertise. Blind '
                                                    'rapid-sequence intubation should be avoided.'},
 'v431-laryngeal-fracture-02': {'stem': 'A 36-year-old woman struck her neck on a steering wheel 10 hours '
                                        'ago. After an awake tracheostomy, she is hemodynamically stable. '
                                        'Flexible laryngoscopy shows massive endolaryngeal edema, a mucosal '
                                        'tear with exposed cartilage and an immobile left vocal fold, and '
                                        'fine-cut CT shows a displaced thyroid cartilage fracture. When '
                                        'should operative exploration and repair be performed?',
                                'choices': ['Within the first 24 to 48 hours of the injury',
                                            'After 7 to 10 days, once the endolaryngeal edema settles',
                                            'Only if serial laryngoscopy shows no recovery with steroids',
                                            'At 6 weeks, once the mucosal tear has healed and matured'],
                                'answer': 0,
                                'explanation': 'Exposed cartilage, a mucosal tear, vocal fold immobility and '
                                               'a displaced fracture make this a Schaefer-Fuhrman group III '
                                               'injury that requires operative repair. Expeditious '
                                               'exploration, ideally within the first 24 to 48 hours once '
                                               'the airway is secure and life-threatening injuries are '
                                               'addressed, allows mucosal closure over exposed cartilage, '
                                               'fracture reduction and fixation before granulation, '
                                               'infection and fibrosis develop. Delays are associated with '
                                               'more stenosis, webbing and poorer voice outcomes.',
                                'why_wrong': ['Correct.',
                                              'Waiting for edema to settle allows granulation and fibrosis '
                                              'over exposed cartilage, increasing stenosis and poor voice '
                                              'outcomes.',
                                              'Exposed cartilage and a displaced fracture need repair; '
                                              'steroids and observation are for group I or selected stable '
                                              'group II injuries.',
                                              'Exposed cartilage will not heal properly in 6 weeks; it '
                                              'becomes infected or fibrotic, producing stenosis and fixed '
                                              'deformity.'],
                                'board_pearl': 'Displaced laryngeal fractures with exposed cartilage need '
                                               'prompt repair, ideally within 24 to 48 hours.',
                                'curveball': 'What late complications can result from delayed repair or '
                                             'malrepair of this injury?',
                                'curveball_answer': 'Glottic or subglottic stenosis, anterior glottic web '
                                                    'from a disrupted anterior commissure, persistent '
                                                    'dysphonia, vocal fold immobility or arytenoid fixation, '
                                                    'chronic aspiration and dysphagia, and failure to '
                                                    'decannulate. Accurate reduction, mucosal coverage of '
                                                    'exposed cartilage and restoring the anterior '
                                                    'commissure, with a stent when needed, reduce these '
                                                    'risks.'},
 'v464_fp_laryngealfx_fnd': {'stem': 'A 26-year-old man struck a clothesline while riding a motorcycle at '
                                     'speed. He has anterior neck tenderness, crepitus over the larynx, a '
                                     'flattened thyroid prominence and mild dysphonia, but he speaks in full '
                                     'sentences without stridor, and oxygen saturation is 97% on room air. '
                                     'He is in a cervical collar. What is the most important next step?',
                             'choices': ['Contrast CT of the neck before any airway evaluation is attempted',
                                         'Blind nasotracheal intubation at the bedside to secure the airway',
                                         'Rapid-sequence oral intubation by the emergency department team',
                                         'Senior-led airway assessment with a tracheostomy setup ready'],
                             'answer': 3,
                             'explanation': 'Crepitus, a flattened thyroid prominence and dysphonia after a '
                                            'clothesline mechanism are red flags for laryngeal fracture, '
                                            'even when he speaks comfortably. Symptoms do not reliably grade '
                                            'injury, and edema can progress rapidly. The priority is a '
                                            'coordinated airway assessment by senior ENT, anesthesia and '
                                            'trauma staff with cervical spine precautions, flexible '
                                            'laryngoscopy, and equipment ready for awake tracheostomy if the '
                                            'airway is unstable. Imaging follows once the airway is safe.',
                             'why_wrong': ['Sending a patient with red flags for fracture to CT before '
                                           'airway assessment risks obstruction in the scanner.',
                                           'Blind instrumentation across a fractured larynx can create a '
                                           'false passage or complete laryngotracheal separation.',
                                           'Rapid-sequence induction removes spontaneous breathing and may '
                                           'convert a partial injury into a lost airway.',
                                           'Correct.'],
                             'board_pearl': 'Crepitus or a flattened thyroid prominence after neck trauma '
                                            'signals laryngeal fracture; secure the airway in a controlled '
                                            'setting.',
                             'curveball': 'Which additional injuries should be assessed as part of the same '
                                          'multidisciplinary trauma evaluation?',
                             'curveball_answer': 'Evaluate the cervical spine, carotid and vertebral '
                                                 'arteries and jugular veins with CT angiography, and the '
                                                 'pharynx and esophagus for perforation using esophagoscopy '
                                                 'or contrast swallow. Also look for chest injuries, '
                                                 'including pneumothorax and tracheal or bronchial injury, '
                                                 'and closed head injury.'},
 'v464_fp_laryngealfx_app': {'stem': 'A 33-year-old woman was struck in the anterior neck by a softball 3 '
                                     'hours ago. She is stable and cooperative with mild hoarseness. '
                                     'Flexible laryngoscopy shows mild supraglottic edema and a small left '
                                     'aryepiglottic fold hematoma, intact mucosa without exposed cartilage, '
                                     'and normal vocal fold mobility. The airway is widely patent. What is '
                                     'the most appropriate next step?',
                             'choices': ['Fine-cut CT of the larynx with multiplanar reconstruction',
                                         'Discharge home with voice rest and no imaging',
                                         'Elective direct laryngoscopy and bronchoscopy in about 3 weeks',
                                         'Open exploration through a thyrotomy in the next 24 hours'],
                             'answer': 0,
                             'explanation': 'A reassuring flexible examination can miss an underlying '
                                            'framework fracture, which changes grading and management. '
                                            'Fine-cut CT of the larynx with multiplanar reconstruction '
                                            'identifies displaced or nondisplaced thyroid and cricoid '
                                            'fractures once the airway is safe. Schaefer-Fuhrman grading '
                                            'relies on both endoscopy and CT. If CT shows no fracture or a '
                                            'nondisplaced fracture with intact mucosa, she can be observed '
                                            'rather than taken for exploration.',
                             'why_wrong': ['Correct.',
                                           'Discharge without imaging could miss a fracture, and edema or '
                                           'hematoma can progress over the first 24 hours.',
                                           'Delaying evaluation for weeks misses the window for prompt '
                                           'repair if a displaced fracture is present.',
                                           'Exploration is reserved for displaced fractures, exposed '
                                           'cartilage or major lacerations, none of which have been shown.'],
                             'board_pearl': 'Even with a reassuring laryngoscopy, obtain fine-cut laryngeal '
                                            'CT after significant anterior neck trauma.',
                             'curveball': 'CT shows a nondisplaced thyroid cartilage fracture with intact '
                                          'mucosa and no airway compromise. How should she be managed?',
                             'curveball_answer': 'This is a group I or stable group II injury. Admit for '
                                                 'monitored observation with head elevation, humidified air, '
                                                 'voice rest, analgesia and a swallowing assessment, with '
                                                 'serial flexible laryngoscopy. Steroids and antireflux '
                                                 'therapy are optional adjuncts. Operate only if the airway '
                                                 'worsens or emphysema progresses.'},
 'v464_fp_laryngealfx_snr': {'stem': 'A 24-year-old man struck his anterior neck on a handlebar during an '
                                     'all-terrain vehicle crash. In the trauma bay he has inspiratory '
                                     'stridor, worsening dyspnea, extensive cervical crepitus and loss of '
                                     'palpable laryngeal landmarks. Oxygen saturation is 90% on a '
                                     'nonrebreather mask, and he is sitting up in a cervical collar. Which '
                                     'airway strategy is most appropriate?',
                             'choices': ['Rapid-sequence oral intubation with standard direct laryngoscopy',
                                         'CT of the neck to define the fracture before an airway decision',
                                         'Awake tracheostomy under local anesthesia below the injury',
                                         'Open reduction and fixation of the larynx before securing the '
                                         'airway'],
                             'answer': 2,
                             'explanation': 'Stridor, worsening dyspnea, extensive emphysema and loss of '
                                            'laryngeal landmarks indicate a disrupted laryngeal framework '
                                            'with impending obstruction. Rapid-sequence intubation risks a '
                                            'false passage, complete laryngotracheal separation or loss of '
                                            'the airway once spontaneous breathing stops. A controlled '
                                            'surgical airway below the injury, typically awake tracheostomy '
                                            'under local anesthesia with the patient breathing '
                                            'spontaneously, is favored. Imaging and repair follow once the '
                                            'airway is secure.',
                             'why_wrong': ['Paralysis removes his spontaneous breathing, and laryngoscopy '
                                           'across a disrupted larynx risks a false passage and complete '
                                           'obstruction.',
                                           'Sending a desaturating patient with stridor to CT delays airway '
                                           'control and risks obstruction outside a controlled setting.',
                                           'Correct.',
                                           'Repair follows airway security; operating on the larynx first '
                                           'risks losing the airway entirely.'],
                             'board_pearl': 'Unstable laryngeal fracture with stridor: awake tracheostomy '
                                            'below the injury; avoid blind rapid-sequence intubation.',
                             'curveball': 'The trauma attending suggests an emergency cricothyrotomy instead '
                                          'because it is faster. Why is tracheostomy preferred here?',
                             'curveball_answer': 'A cricothyrotomy passes through the cricothyroid membrane '
                                                 'at the level of the injured larynx, so it can enter a '
                                                 'false passage, worsen cricoid or thyroid fractures, or '
                                                 'miss a laryngotracheal separation, and it raises '
                                                 'subglottic stenosis risk. A tracheostomy below the injury '
                                                 'bypasses the damaged segment.'},
 'v431-blepharoplasty-eyelid-01': {'stem': 'A 58-year-old man complains of heavy upper eyelids that hood his '
                                           'lashes and tire him by evening. His brows sit below the superior '
                                           'orbital rim, and he raises his forehead constantly. When the '
                                           'brows are lifted manually to their normal position, most of the '
                                           'excess upper lid skin disappears. Margin-reflex distance 1 is 4 '
                                           'mm and levator function is 15 mm. Which plan is most '
                                           'appropriate?',
                                   'choices': ['Aggressive upper blepharoplasty skin excision alone',
                                               'Levator aponeurosis advancement on both upper lids',
                                               'Brow elevation with conservative skin excision if needed',
                                               'Neuromodulator to the brow depressors as sole treatment'],
                                   'answer': 2,
                                   'explanation': 'A droopy eyelid is not one diagnosis. His normal '
                                                  'margin-reflex distance and levator function exclude true '
                                                  'ptosis, and the resolution of hooding when the brows are '
                                                  'lifted shows that brow ptosis is the main failing layer, '
                                                  'with frontalis overactivity compensating. Elevating the '
                                                  'brow treats the cause, and only conservative skin '
                                                  'excision is added if real excess remains. Excising lid '
                                                  'skin alone would pull the brows lower and risk '
                                                  'lagophthalmos.',
                                   'why_wrong': ['Removing lid skin when the brow is the cause pulls the '
                                                 'brow down further and can cause lagophthalmos and dry eye.',
                                                 'His lid margin height and levator function are normal, so '
                                                 'there is no ptosis for levator surgery to correct.',
                                                 'Correct.',
                                                 'Toxin can give a small temporary brow lift but cannot '
                                                 'correct significant brow ptosis like his.'],
                                   'board_pearl': 'Identify the failing layer: brow ptosis, dermatochalasis '
                                                  'and true ptosis need different operations.',
                                   'curveball': 'Which complications must specifically be avoided during '
                                                'blepharoplasty and eyelid malposition surgery?',
                                   'curveball_answer': 'Overresection of upper lid skin with lagophthalmos '
                                                       'and exposure keratopathy; lower lid retraction or '
                                                       'ectropion after skin excision without lid support; '
                                                       'ptosis from levator injury; diplopia from inferior '
                                                       'oblique injury; and retrobulbar hematoma with vision '
                                                       'loss, which needs prompt canthotomy and '
                                                       'cantholysis.'},
 'v431-blepharoplasty-eyelid-02': {'stem': 'A 70-year-old woman with prior LASIK and daily use of artificial '
                                           'tears requests upper blepharoplasty because heavy lids block her '
                                           'upper vision. She hopes insurance will cover it. On exam she has '
                                           'dermatochalasis and possible mild ptosis, a weak Bell phenomenon '
                                           'and mild punctate staining of both corneas. Which preoperative '
                                           'assessment is essential?',
                                   'choices': ['Intraocular pressure measurement and corneal pachymetry',
                                               'Hertel exophthalmometry with a CT scan of both orbits',
                                               'MRD1, levator function, tear testing and visual fields',
                                               'Standardized photographs alone, with no other testing'],
                                   'answer': 2,
                                   'explanation': 'Measuring margin-reflex distance and levator function '
                                                  'separates dermatochalasis from true ptosis and guides '
                                                  'whether levator surgery is needed. Her dry eye, prior '
                                                  'LASIK, corneal staining and weak Bell phenomenon raise '
                                                  'the risk of exposure keratopathy, so tear testing and '
                                                  'ocular surface assessment determine how conservative '
                                                  'surgery must be. Formal visual fields with lids taped and '
                                                  'untaped document functional obstruction for insurance. '
                                                  'Pupils, motility and lower lid laxity should also be '
                                                  'checked.',
                                   'why_wrong': ['Pressure and pachymetry relate to glaucoma and refractive '
                                                 'surgery and do not characterize lid position or surface '
                                                 'risk.',
                                                 'Exophthalmometry and CT are for proptosis or orbital '
                                                 'disease, which she does not have.',
                                                 'Correct.',
                                                 'Photographs help document but cannot measure lid function '
                                                 'or dry eye risk, or provide visual field evidence.'],
                                   'board_pearl': 'Before blepharoplasty, measure MRD1 and levator function, '
                                                  "assess dry eye and Bell's, and document fields.",
                                   'curveball': 'If she chooses to delay surgery, which nonsurgical options '
                                                'can bridge her symptoms safely?',
                                   'curveball_answer': 'Aggressive lubrication with preservative-free tears '
                                                       'and nighttime ointment, punctal plugs for aqueous '
                                                       'deficiency, treatment of meibomian gland disease, '
                                                       'and lid taping at night protect her cornea. '
                                                       'Oxymetazoline drops can lift mild ptosis '
                                                       'temporarily. None corrects dermatochalasis, which '
                                                       'still needs surgery.'},
 'v464_fp_bleph_fnd': {'stem': 'A 68-year-old woman reports heavy upper eyelids that block the top of her '
                               'vision, worse at the end of the day when she reads. Redundant upper lid skin '
                               'rests on the lashes. When the skin is lifted with a cotton swab, '
                               'margin-reflex distance 1 is 4 mm on both sides and levator function is 15 '
                               'mm. Brows sit at the orbital rim, and pupils are normal. Which diagnosis '
                               'best fits?',
                       'choices': ['Aponeurotic ptosis from levator dehiscence',
                                   'Dermatochalasis without true blepharoptosis',
                                   'Brow ptosis with compensatory frontalis action',
                                   'Ocular myasthenia with fatigable lid ptosis'],
                       'answer': 1,
                       'explanation': 'Her lid margin sits at a normal height and levator function is '
                                      'excellent once redundant skin is lifted, so the lid itself is not '
                                      'ptotic. Excess upper lid skin overhanging the lashes is '
                                      'dermatochalasis, which can obstruct the superior visual field and '
                                      'worsen with fatigue. Her brows are in normal position. Separating '
                                      'dermatochalasis from ptosis, brow ptosis and other causes determines '
                                      'the operation: upper blepharoplasty rather than levator surgery.',
                       'why_wrong': ['Aponeurotic ptosis lowers the lid margin, whereas her margin-reflex '
                                     'distance is normal once the skin is lifted.',
                                     'Correct.',
                                     'Her brows sit at the orbital rim, so brow descent is not the cause of '
                                     'her hooding.',
                                     'Myasthenia causes a low, fatigable lid margin and often diplopia; her '
                                     'lid margin is normal and the problem is overhanging skin.'],
                       'board_pearl': 'Dermatochalasis is excess skin with a normal lid margin; true ptosis '
                                      'lowers the margin itself.',
                       'curveball': 'What measurements should be obtained before assuming this is purely '
                                    'dermatochalasis and proceeding to skin excision?',
                       'curveball_answer': 'Margin-reflex distance 1 and levator function, lid crease '
                                           'height, brow position, Bell phenomenon and tear testing for dry '
                                           'eye, pupils and motility, and lower lid laxity. Formal visual '
                                           'fields, taped and untaped, document functional obstruction when '
                                           'needed.'},
 'v464_fp_bleph_app': {'stem': 'A 52-year-old man has had a drooping left upper eyelid for 4 days with a '
                               'left-sided headache. He has no prior eye surgery. Left margin-reflex '
                               'distance 1 is 0 mm and levator function is 6 mm. The left pupil is 6 mm and '
                               'reacts sluggishly, the right is 3 mm, and he has double vision on looking '
                               'right and upward. Which next step is most appropriate?',
                       'choices': ['Levator aponeurosis advancement after a period of observation',
                                   'Urgent CT or MR angiography for a compressive third nerve palsy',
                                   'Ice pack test with acetylcholine receptor antibody testing first',
                                   'Apraclonidine drop testing to confirm Horner syndrome'],
                       'answer': 1,
                       'explanation': 'New ptosis with reduced levator function, a dilated sluggish pupil '
                                      'and impaired ocular motility is a third nerve palsy until proven '
                                      'otherwise. With pupil involvement and headache, a compressive lesion '
                                      'such as a posterior communicating artery aneurysm must be excluded '
                                      'urgently with CT or MR angiography. Neurogenic ptosis must not be '
                                      'mistaken for age-related aponeurotic ptosis, which has good levator '
                                      'function and normal pupils and motility.',
                       'why_wrong': ['Aponeurotic ptosis has good levator function and normal pupils; '
                                     'operating would miss a possibly life-threatening aneurysm.',
                                     'Correct.',
                                     'Myasthenia spares the pupil; his dilated, sluggish pupil points to a '
                                     'third nerve lesion rather than a neuromuscular cause.',
                                     'Horner syndrome causes mild ptosis with a small pupil, whereas his '
                                     'affected pupil is dilated.'],
                       'board_pearl': 'Ptosis with a dilated pupil or diplopia is a third nerve palsy until '
                                      'proven otherwise; image urgently.',
                       'curveball': 'If workup instead showed aponeurotic ptosis with normal pupils and '
                                    'motility, what does the operation specifically target?',
                       'curveball_answer': 'Repair targets the levator mechanism: external levator '
                                           'aponeurosis advancement and reattachment to the tarsus, or '
                                           'posterior Muller muscle-conjunctival resection when '
                                           'phenylephrine raises the lid well. This differs from '
                                           'blepharoplasty, which removes skin, and from frontalis '
                                           'suspension, which is for poor levator function.'},
 'v464_fp_bleph_snr': {'stem': 'A 77-year-old man has a tearing, irritated right eye. The right lower lid is '
                               'everted along its full length with mild conjunctival keratinization. '
                               'Distraction test shows 10 mm laxity and snap-back is slow. The lid returns '
                               'to normal position when pushed up, the skin is not tight on upward gaze or '
                               'mouth opening, and the medial canthal tendon is stable. Facial nerve '
                               'function is normal. Which operation is most appropriate?',
                       'choices': ['Full-thickness skin graft to lengthen the anterior lamella',
                                   'Medial spindle excision of tarsoconjunctiva beneath the punctum',
                                   'Lateral tarsal strip to correct the horizontal lid laxity',
                                   'Quickert everting sutures with lower lid retractor plication'],
                       'answer': 2,
                       'explanation': 'This is involutional ectropion from horizontal laxity, confirmed by '
                                      'marked distraction and slow snap-back. Normal skin length rules out a '
                                      'cicatricial cause, a stable medial tendon makes medial canthal repair '
                                      'unnecessary, and normal facial function rules out paralytic '
                                      'ectropion. A lateral tarsal strip shortens the lid and reattaches it '
                                      'to the lateral orbital rim periosteum, restoring apposition to the '
                                      'globe. Treating the ocular surface helps as well.',
                       'why_wrong': ['Skin grafting treats cicatricial ectropion from a short anterior '
                                     'lamella, but his skin length is normal.',
                                     'Medial spindle excision corrects isolated punctal eversion and does '
                                     'not fix full-length ectropion from horizontal laxity.',
                                     'Correct.',
                                     'Quickert sutures and retractor plication treat inward-turning '
                                     'entropion, the opposite malposition.'],
                       'board_pearl': 'Involutional ectropion with marked horizontal laxity: lateral tarsal '
                                      'strip; skin grafts are for cicatricial ectropion.',
                       'curveball': 'Why must the ocular surface and lower lid support be assessed before '
                                    'any eyelid procedure, and which complications must be prevented?',
                       'curveball_answer': 'Dry eye, weak Bell phenomenon and poor lower lid tone raise the '
                                           'risk that small changes cause exposure keratopathy, retraction '
                                           'or ectropion, so surgery may need to be more conservative or '
                                           'include lid support. Complications to prevent include '
                                           'overcorrection, lagophthalmos, lid retraction, canthal '
                                           'distortion and retrobulbar hematoma.'}}
