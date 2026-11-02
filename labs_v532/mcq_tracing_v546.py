# labs_v532/mcq_tracing_v546.py: board-style MCQs for the six tracing/report labs
# (audiology, audiologic electrophysiology, vestibular, CT/MRI, allergy testing, sleep), plus
# source-text corrections found while writing them (2026-11-01). Each key was checked by
# reading the keyed choice against its explanation.
MCQ_BY_CASE = {'aud1': {'question': 'An adult has right air-conduction thresholds of 5, 5, 10, 5, 10, 10 dB HL and left '
                      'thresholds of 10, 5, 5, 10, 5, 15 dB HL (250 Hz to 8 kHz). Bone conduction is 10 dB '
                      'HL or better with no air-bone gap. SRT is 5 dB HL in each ear, word recognition is '
                      '100% right and 96% left, tympanograms are Type A and acoustic reflexes are present '
                      'bilaterally. Which interpretation is most accurate?',
          'choices': ['Mild left high-frequency sensorineural loss at 8 kHz that warrants MRI of the '
                      'internal auditory canals',
                      'Slight bilateral conductive loss, because bone thresholds are better than air '
                      'thresholds at several frequencies',
                      'Hearing sensitivity and middle-ear function are within normal limits bilaterally, '
                      'with no meaningful asymmetry',
                      'Asymmetric word recognition of 4% that suggests early left retrocochlear dysfunction '
                      'needing follow-up'],
          'answer': 2,
          'explanation': 'All thresholds fall in the normal range, air and bone agree, speech results match '
                         'the pure-tone average, and immittance is normal, so this is a normal template. A '
                         '5-10 dB difference between ears or between air and bone falls within test-retest '
                         'variability, and a 4% difference in word recognition is not significant. Pearl: '
                         'call an evaluation normal only after the whole battery agrees, including '
                         'thresholds, speech, tympanometry and reflexes.',
          'domain': 'Otology / Neurotology',
          'topic': 'Normal audiologic template'},
 'aud2': {'question': 'Right air conduction is 45, 50, 45, 40, 35 dB HL (250 Hz to 4 kHz) with bone '
                      'conduction of 5-10 dB HL, giving an air-bone gap of roughly 35-40 dB. The left ear is '
                      'normal with no gap. Right tympanometry is Type B with normal ear-canal volume; the '
                      'left is Type A. Right word recognition is 96%. Which explanation best fits the right '
                      'ear?',
          'choices': ['Middle-ear effusion behind an intact tympanic membrane',
                      'Tympanic membrane perforation with a patent middle-ear space',
                      'Otosclerotic stapes fixation with a Carhart notch',
                      'Superior canal dehiscence producing a pseudoconductive gap'],
          'answer': 0,
          'explanation': 'A flat tympanogram with normal canal volume means poor membrane mobility behind an '
                         'intact drum, and together with a conductive gap and normal cochlear reserve this '
                         'most often means fluid in the middle ear. A perforation would give a flat tracing '
                         'with a large canal volume. Otosclerosis and third-window lesions typically leave a '
                         'Type A or As tracing. Pearl: confirm with otoscopy, and in an adult with new '
                         'unilateral effusion, examine the nasopharynx.',
          'domain': 'Otology / Neurotology',
          'topic': 'Conductive loss with Type B tympanogram'},
 'aud3': {'question': 'Right thresholds are 10, 15, 20, 35, 55, 65 dB HL and left thresholds are 10, 15, 20, '
                      '35, 55, 60 dB HL (250 Hz to 8 kHz), with air equal to bone at every tested frequency. '
                      'SRT is 20 dB HL and word recognition is 88% in each ear. Tympanograms are Type A. How '
                      'should this audiogram be described?',
          'choices': ['Bilateral mixed loss, with a sensorineural component plus a small high-frequency '
                      'air-bone gap',
                      'Bilateral conductive loss of the high frequencies, with normal low-frequency bone '
                      'conduction',
                      'Asymmetric left sensorineural loss that needs retrocochlear imaging because of the 8 '
                      'kHz threshold',
                      'Bilateral symmetric, sloping high-frequency sensorineural loss with speech scores '
                      'consistent with the thresholds'],
          'answer': 3,
          'explanation': 'Air and bone fall together with no gap, so the loss is sensorineural; the ears are '
                         'within 5 dB of each other, and 88% word recognition is what you would expect for '
                         'this degree of loss. A single 5 dB difference at 8 kHz is not clinically '
                         'meaningful asymmetry, and without an air-bone gap the loss cannot be conductive or '
                         'mixed. Pearl: describe every audiogram by type, degree, configuration and '
                         'symmetry, then check that the speech scores match.',
          'domain': 'Otology / Neurotology',
          'topic': 'Audiogram type and configuration'},
 'aud4': {'question': 'A 52-year-old reports gradual left hearing loss and left tinnitus. Right thresholds '
                      'are 10, 10, 15, 20, 25, 30 dB HL and left are 15, 20, 35, 55, 70, 75 dB HL (250 Hz to '
                      '8 kHz), with air equal to bone. Word recognition is 100% right and 60% left. '
                      'Tympanograms are Type A bilaterally. What is the most appropriate next step?',
          'choices': ['Fit a left hearing aid and repeat the audiogram in 12 months',
                      'Obtain gadolinium-enhanced MRI of the internal auditory canals',
                      'Start a course of high-dose oral corticosteroids',
                      'Order a noncontrast CT scan of the temporal bones'],
          'answer': 1,
          'explanation': 'Asymmetric sensorineural loss with unilateral tinnitus and word recognition out of '
                         'proportion to the thresholds calls for a retrocochlear evaluation, and '
                         'gadolinium-enhanced MRI of the internal auditory canals is the reference test for '
                         'vestibular schwannoma. Amplification alone would delay a possible tumor diagnosis. '
                         'CT does not show small lesions in the canal. Steroids are for sudden loss, not '
                         'gradual loss. Pearl: in asymmetric SNHL, poor word recognition increases concern '
                         'for a retrocochlear lesion.',
          'domain': 'Otology / Neurotology',
          'topic': 'Asymmetric SNHL workup'},
 'aud_mixed_v42': {'question': 'A patient with chronic ear disease has right bone-conduction thresholds of '
                               '30-35 dB HL and air-conduction thresholds of 60-65 dB HL from 500 Hz to 4 '
                               'kHz. The contralateral ear is normal and masking was adequate. How should '
                               'the right ear be classified, and what is the best realistic hearing result '
                               'after successful ossicular reconstruction?',
                   'choices': ['Conductive loss; closing the gap should bring air thresholds back to normal',
                               'Sensorineural loss; ossicular reconstruction would not be expected to change '
                               'air thresholds',
                               'Mixed loss; at best, air thresholds approach the current 30-35 dB HL bone '
                               'thresholds',
                               'Mixed loss; reconstruction should improve both air and bone thresholds to '
                               'normal'],
                   'answer': 2,
                   'explanation': 'Elevated bone thresholds show a sensorineural component, and an air-bone '
                                  'gap of about 30 dB adds a conductive component, so the loss is mixed. '
                                  'Surgery addresses only the conductive part, so the best case is closing '
                                  'the gap to the bone line, not normal hearing. A pure conductive label '
                                  'ignores the abnormal bone thresholds. Pearl: when counseling patients, '
                                  'frame the surgical goal as closing the air-bone gap to the cochlear '
                                  'reserve.',
                   'domain': 'Otology / Neurotology',
                   'topic': 'Mixed hearing loss'},
 'aud_carhart_v42': {'question': 'A 38-year-old woman has progressive left hearing loss and a '
                                 'normal-appearing tympanic membrane. Left air conduction is 45-50 dB HL '
                                 'across frequencies. Bone conduction is 5-10 dB HL except 25 dB HL at 2 '
                                 'kHz. Tympanometry is Type As and the left acoustic reflexes are absent. '
                                 'What does the 2 kHz bone-conduction finding most likely represent?',
                     'choices': ['A true cochlear sensorineural dip that sets a hard limit on hearing after '
                                 'surgery',
                                 'A mechanical artifact of stapes fixation that often improves after '
                                 'successful stapes surgery',
                                 'A noise-induced cochlear notch that is coincidentally present in the same '
                                 'ear',
                                 'An early third-window effect that makes stapes surgery contraindicated'],
                     'answer': 1,
                     'explanation': 'A bone-conduction dip centered near 2 kHz in a conductive ear with '
                                    'stapes fixation is the Carhart notch, a mechanical change in the '
                                    "ossicular chain's contribution to bone conduction rather than true "
                                    'cochlear loss. It often improves after stapedotomy. Calling it a fixed '
                                    'sensorineural loss underestimates the expected benefit. Pearl: the '
                                    'notch supports otosclerosis but does not prove it; correlate with the '
                                    'history, reflexes and imaging when needed.',
                     'domain': 'Otology / Neurotology',
                     'topic': 'Carhart notch in stapes fixation'},
 'aud_thirdwindow_v42': {'question': 'A 45-year-old hears his own voice and eye movements loudly in the '
                                     'right ear. Right audiometry shows a 20-25 dB air-bone gap at 250-500 '
                                     'Hz with bone thresholds better than 0 dB HL. Tympanometry is Type A '
                                     'and right acoustic reflexes are present. Which explanation best fits?',
                         'choices': ['Otosclerotic stapes fixation producing a low-frequency air-bone gap',
                                     'Ossicular discontinuity producing a hypermobile middle-ear system',
                                     'Middle-ear effusion that is too small to change the tympanogram',
                                     'A third-window inner-ear lesion producing a pseudoconductive gap'],
                         'answer': 3,
                         'explanation': 'A low-frequency air-bone gap with supranormal bone thresholds, a '
                                        'normal tympanogram and present acoustic reflexes points to an '
                                        'inner-ear third window, such as superior canal dehiscence, rather '
                                        'than true middle-ear disease. In stapes fixation, the acoustic '
                                        'reflexes are usually absent. Ossicular discontinuity gives a '
                                        'hypermobile (Ad) tracing with absent reflexes. Pearl: check '
                                        'reflexes before stapes surgery, because present reflexes in a '
                                        'conductive-looking ear should prompt VEMPs and high-resolution CT.',
                         'domain': 'Otology / Neurotology',
                         'topic': 'Pseudoconductive loss in third-window disorder'},
 'aud_soundfield_v42': {'question': 'An 18-month-old with delayed speech has normal thresholds on visual '
                                    'reinforcement audiometry in the sound field. The child would not '
                                    'tolerate earphones. What is the most accurate conclusion?',
                        'choices': ['The results reflect only the better ear, so ear-specific testing is '
                                    'still needed',
                                    'Both ears can be considered normal because sound-field thresholds were '
                                    'normal',
                                    'The results exclude unilateral hearing loss but not mild conductive '
                                    'loss',
                                    'No further testing is needed unless speech delay persists past age '
                                    'three'],
                        'answer': 0,
                        'explanation': 'A loudspeaker stimulates both ears, so normal sound-field thresholds '
                                       'show only that at least one ear hears normally; a unilateral loss '
                                       'can be missed. Ear-specific data from insert earphones, or from '
                                       'objective tests such as ABR and OAEs, are required. A child with '
                                       'speech delay should not have testing deferred. Pearl: always ask '
                                       'whether a pediatric result is ear-specific before calling both ears '
                                       'normal.',
                        'domain': 'Pediatric Otolaryngology',
                        'topic': 'Sound-field testing limitations'},
 'aud_presby_v42': {'question': 'A 74-year-old has symmetric, downsloping high-frequency sensorineural '
                                'hearing loss and difficulty understanding speech in noise. You are about to '
                                'counsel her about age-related hearing loss and amplification. Which '
                                'additional finding should most prompt further evaluation before you '
                                'attribute the loss to age?',
                    'choices': ['Bilateral high-pitched tinnitus that is worse in quiet rooms',
                                'Word recognition of 84% in each ear at a comfortable level',
                                'Type A tympanograms with present acoustic reflexes bilaterally',
                                'Word recognition of 92% in the right ear and 56% in the left ear'],
                    'answer': 3,
                    'explanation': 'Clearly asymmetric word recognition with symmetric thresholds is a red '
                                   'flag for retrocochlear or other non-routine pathology and calls for '
                                   'further evaluation, usually MRI. Bilateral tinnitus, matched speech '
                                   'scores consistent with the thresholds, and normal immittance all fit '
                                   'typical presbycusis. Pearl: presbycusis is a diagnosis of exclusion, and '
                                   'asymmetry, sudden change, disproportionately poor word recognition or '
                                   'neurologic symptoms should change the plan.',
                    'domain': 'Otology / Neurotology',
                    'topic': 'Red flags in presumed presbycusis'},
 'aud_wordrec_v42': {'question': 'Pure-tone thresholds are mild and nearly identical between the ears. Word '
                                 'recognition at a comfortable level is 96% in the right ear and 52% in the '
                                 'left ear, and this is confirmed on retest with appropriate masking. Which '
                                 'interpretation is most appropriate?',
                     'choices': ['The thresholds are symmetric, so the difference is clinically unimportant',
                                 'The finding raises concern for left neural or retrocochlear dysfunction',
                                 'The pattern most strongly suggests a left conductive middle-ear lesion',
                                 'The pattern proves a nonorganic hearing loss in the left ear'],
                     'answer': 1,
                     'explanation': 'Detecting tones and processing speech test different parts of the '
                                    'auditory pathway, and word recognition far below what the thresholds '
                                    'predict suggests neural or retrocochlear dysfunction even when the '
                                    'audiogram is symmetric. Conductive lesions lower audibility but '
                                    'preserve clarity once speech is loud enough. A reproducible score '
                                    'obtained with masking does not by itself suggest a nonorganic loss. '
                                    'Pearl: interpret the audiogram as a battery, because the pure-tone '
                                    'graph alone can look reassuring when the speech score is not.',
                     'domain': 'Otology / Neurotology',
                     'topic': 'Disproportionate word recognition'},
 'a8': {'question': 'A 10-month-old has present otoacoustic emissions and absent ABR waves at maximum '
                    'stimulus levels bilaterally. Tympanograms are normal, and MRI shows normal cochlear '
                    'nerves. Which management approach is most appropriate?',
        'choices': ['Fit hearing aids immediately using the ABR thresholds, then adjust them when the child '
                    'is older',
                    'Avoid amplification because the present emissions show that the cochlea is working '
                    'normally',
                    'Base amplification on behavioral thresholds and aided speech outcomes, and refer for '
                    'cochlear implant evaluation if benefit is poor',
                    'Proceed directly to cochlear implantation because hearing aids never help in this '
                    'condition'],
        'answer': 2,
        'explanation': 'In auditory neuropathy spectrum disorder, the ABR cannot estimate thresholds, so '
                       'fitting decisions rely on behavioral thresholds (when reliable) and on demonstrated '
                       'aided benefit. Some children do well with hearing aids, while those with '
                       'persistently poor speech perception are referred for cochlear implant evaluation. '
                       'Withholding amplification because OAEs are present misreads outer-hair-cell function '
                       'as useful hearing. Pearl: never program hearing aids from ABR thresholds in '
                       'neuropathy.',
        'domain': 'Pediatric Otolaryngology',
        'topic': 'ANSD rehabilitation'},
 'a9': {'question': 'An adult has bilateral severe sensorineural hearing loss on the audiogram. With '
                    'properly fitted hearing aids, standardized sentence recognition in the best-aided '
                    'condition is high and has been stable, and the patient reports good daily '
                    'communication. What is the most appropriate interpretation?',
        'choices': ['Candidacy depends on aided speech performance, so optimizing hearing aids and '
                    'monitoring is reasonable',
                    'The severe thresholds alone qualify the patient, so implantation should be scheduled',
                    'Implant candidacy is based on the pure-tone average, so speech testing is not needed',
                    'Good aided scores suggest a nonorganic loss, so objective ABR thresholds are required'],
        'answer': 0,
        'explanation': 'Cochlear implant candidacy rests on functional benefit from well-fitted hearing '
                       'aids, measured with standardized aided speech testing, not on thresholds alone. '
                       'Patients with similar audiograms can understand speech very differently. Strong '
                       'aided performance argues against implantation for now. Pearl: document ear-specific '
                       'and best-aided scores under defined conditions, apply current device and payer '
                       'criteria, and retest if performance declines.',
        'domain': 'Otology / Neurotology',
        'topic': 'Cochlear implant candidacy'},
 'a10': {'question': 'A patient has profound sensorineural hearing loss in the right ear and normal hearing '
                     'in the left. He is comparing a CROS hearing aid with a bone-conduction device. Which '
                     'statement is accurate?',
         'choices': ['A bone-conduction device stimulates the right cochlea directly and restores sound '
                     'localization',
                     'A CROS aid restores binaural squelch, while a bone-conduction device restores only '
                     'audibility',
                     'A bone-conduction device is appropriate only if the left ear also has a conductive '
                     'component',
                     'Both route sound from the deaf side to the left cochlea and reduce head shadow without '
                     'true binaural hearing'],
         'answer': 3,
         'explanation': 'CROS sends sound by air to the better ear, and a bone-conduction device sends it by '
                        'vibration to the better cochlea, so both overcome head shadow but neither restores '
                        'binaural cues to the deaf ear. Bone conduction cannot help a profoundly deaf '
                        'cochlea, and a conductive component in the better ear is not a universal '
                        'requirement for choosing a device. Pearl: when restoring input to the deaf ear is '
                        'the goal, consider cochlear implant evaluation, and use a trial of each rerouting '
                        'device before committing.',
         'domain': 'Otology / Neurotology',
         'topic': 'Single-sided deafness rehabilitation'},
 'a11': {'question': 'A 4-year-old who had tympanostomy tubes placed 8 months ago has a flat Type B '
                     'tympanogram in the right ear. The measured ear-canal volume is markedly larger than in '
                     'the left ear and above normal limits for age. What is the most likely explanation?',
         'choices': ['The tube is patent, so the probe is measuring middle-ear space as well as the canal',
                     'The tube is blocked and there is effusion behind an intact membrane',
                     'Cerumen or the probe tip against the canal wall is blocking the measurement',
                     'The ossicular chain is disrupted, producing a hypermobile membrane'],
         'answer': 0,
         'explanation': 'A flat tracing with a large equivalent volume means the probe is measuring through '
                        'an opening in the drum, as with a patent tube or perforation. A blocked tube with '
                        'effusion gives a flat tracing with normal canal volume. Cerumen or probe occlusion '
                        'gives an abnormally small volume. Ossicular discontinuity gives a high-peaked Ad '
                        'tracing, not a flat one. Pearl: confirm on otoscopy, because a flat tracing with '
                        'large volume after tube placement is the expected finding for an open tube.',
         'domain': 'Pediatric Otolaryngology',
         'topic': 'Tympanogram ear-canal volume'},
 'a12': {'question': 'A 3-year-old with a mild bilateral conductive hearing loss has flat Type B '
                     'tympanograms with ear-canal volumes in the normal range for age. Which interpretation '
                     'is most appropriate?',
         'choices': ['The tracings suggest bilateral tympanic membrane perforations, so the child needs '
                     'ototopical drops',
                     'The tracings confirm patent ventilation tubes, so no further action is needed',
                     'The tracings indicate reduced mobility behind intact membranes, most often effusion, '
                     'and need otoscopic confirmation',
                     'The tracings indicate probe occlusion, so the test is invalid and should be repeated'],
         'answer': 2,
         'explanation': 'A flat tracing with normal canal volume indicates poor mobility of an intact '
                        'tympanic membrane, and middle-ear effusion is the most common cause in children. A '
                        'perforation or patent tube would raise the volume, and probe occlusion would make '
                        'it abnormally small. The tympanogram does not show fluid directly. Pearl: confirm '
                        'with pneumatic otoscopy, then base management on hearing level, symptoms and '
                        'duration.',
         'domain': 'Pediatric Otolaryngology',
         'topic': 'Type B tympanogram with normal volume'},
 'a13': {'question': 'A patient receiving cisplatin had a pretreatment baseline audiogram. Which change from '
                     'baseline meets ASHA criteria for a significant ototoxic threshold shift?',
         'choices': ['A 10 dB shift at 4 kHz only, with no change at the other frequencies',
                     'A 15 dB shift at 8 kHz only, with no change at the other frequencies',
                     'A 10 dB shift at 6 kHz and at 8 kHz, confirmed on repeat testing',
                     'A 5 dB shift at each of 2, 3 and 4 kHz, confirmed on repeat testing'],
         'answer': 2,
         'explanation': 'ASHA defines a significant shift as at least 20 dB at one frequency, at least 10 dB '
                        'at two adjacent frequencies, or loss of response at three consecutive frequencies '
                        'that were previously responsive, confirmed on retest. Two adjacent 10 dB shifts '
                        'qualify. A single 10 or 15 dB shift does not, and 5 dB changes fall within '
                        'test-retest variability. Pearl: obtain a baseline before treatment, because '
                        'ototoxicity is judged by change over time, not by one absolute audiogram.',
         'domain': 'Otology / Neurotology',
         'topic': 'Ototoxicity monitoring criteria'},
 'audio-v126-masking-cross-hearing': {'question': 'Testing with supra-aural earphones shows right air and '
                                                  'bone thresholds of 10 dB HL. Unmasked left air conduction '
                                                  'is 60 dB HL and unmasked bone conduction, with the '
                                                  'oscillator on the left mastoid, is 10 dB HL. What is the '
                                                  'most appropriate next step?',
                                      'choices': ['Repeat left air- and bone-conduction testing with masking '
                                                  'noise in the right ear',
                                                  'Report a left conductive loss with a 50 dB air-bone gap '
                                                  'and order a CT scan',
                                                  'Order MRI of the internal auditory canals for asymmetric '
                                                  'sensorineural hearing loss',
                                                  'Repeat right-ear testing with masking noise delivered to '
                                                  'the left ear'],
                                      'answer': 0,
                                      'explanation': "The left air signal exceeds the right cochlea's bone "
                                                     'threshold by more than the roughly 40 dB interaural '
                                                     'attenuation of supra-aural phones, so the right ear '
                                                     'may be responding. Bone conduction has essentially no '
                                                     'interaural attenuation, so the unmasked 10 dB HL bone '
                                                     'threshold could come from either cochlea. Reporting a '
                                                     '50 dB conductive gap or ordering imaging before '
                                                     'masking risks acting on a shadow curve. Pearl: mask '
                                                     'the non-test ear whenever cross-hearing is possible, '
                                                     'and insert earphones raise air-conduction interaural '
                                                     'attenuation.',
                                      'domain': 'Otology / Neurotology',
                                      'topic': 'Masking and cross-hearing'},
 'audio-v126-masking-dilemma': {'question': 'A patient has large air-bone gaps in both ears. When masking '
                                            'noise is introduced in the non-test ear to obtain masked bone '
                                            'thresholds, the noise level needed to rule out cross-hearing '
                                            'crosses over to the test cochlea before a stable plateau can be '
                                            'reached. What is the most appropriate approach?',
                                'choices': ['Report the unmasked bone thresholds as belonging to the test '
                                            'ear',
                                            'Conclude that the hearing loss is nonorganic and request a '
                                            'Stenger test',
                                            'Keep raising the masking level until responses stop and report '
                                            'that level',
                                            'Use insert earphones and plateau methods, and report thresholds '
                                            'as indeterminate if no plateau exists'],
                                'answer': 3,
                                'explanation': 'This is the masking dilemma: with large bilateral conductive '
                                               'components, the masking needed to prevent cross-hearing '
                                               'overmasks the test ear, so no plateau exists. Insert '
                                               'earphones increase interaural attenuation and may resolve '
                                               'it. If they do not, the threshold should be documented as '
                                               'indeterminate, supported by immittance and objective '
                                               'testing. Raising masking until responses stop measures '
                                               'overmasking, not the threshold. Pearl: the dilemma reflects '
                                               'the limits of testing, not a functional loss.',
                                'domain': 'Otology / Neurotology',
                                'topic': 'Masking dilemma'},
 'audio-v126-stenger-functional': {'question': 'A patient reports profound right hearing loss, but responses '
                                               'are inconsistent. During a Stenger test, a tone of the same '
                                               'frequency is presented to both ears at once: louder to the '
                                               'right ear and at a clearly audible level to the normal left '
                                               'ear. The patient does not respond. How should this result be '
                                               'interpreted?',
                                   'choices': ['Negative Stenger, which confirms that the right-ear loss is '
                                               'organic',
                                               'Positive Stenger, which supports a nonorganic component in '
                                               'the right ear',
                                               'Positive Stenger, which indicates a right retrocochlear '
                                               'lesion',
                                               'Positive Stenger, which proves that the patient is '
                                               'deliberately malingering'],
                                   'answer': 1,
                                   'explanation': 'The tone is heard only in the ear where it is louder, so '
                                                  'a patient with true right deafness would still hear the '
                                                  'audible left-ear tone and respond. Not responding means '
                                                  'the louder tone was perceived in the supposedly deaf ear, '
                                                  'which is a positive Stenger and shows the reported right '
                                                  'threshold is not valid. The test assesses whether '
                                                  "responses are valid, not the patient's intent. Pearl: use "
                                                  'neutral language, and confirm true thresholds with '
                                                  'objective tests such as OAEs and ABR.',
                                   'domain': 'Otology / Neurotology',
                                   'topic': 'Stenger test interpretation'},
 'audnew1': {'question': 'A 48-year-old has right thresholds of 10, 10, 15, 20, 45, 20 dB HL and left '
                         'thresholds of 10, 15, 15, 20, 50, 25 dB HL (250 Hz to 8 kHz), with air equal to '
                         'bone. Word recognition is 96% bilaterally and tympanograms are Type A. Which '
                         'audiometric feature most supports noise exposure rather than age as the main '
                         'cause?',
             'choices': ['Symmetric thresholds with word recognition consistent with the pure-tone average',
                         'A notch at 4 kHz with recovery of thresholds at 8 kHz',
                         'Normal thresholds at 250 and 500 Hz with Type A tympanograms',
                         'A sensorineural loss without an air-bone gap at 4 kHz'],
             'answer': 1,
             'explanation': 'A notch with its lowest point near 3-6 kHz and recovery at 8 kHz is the classic '
                            'sign of noise injury. Age-related loss typically keeps sloping downward, with 8 '
                            'kHz the worst. Symmetry, normal low frequencies and the absence of an air-bone '
                            'gap fit either cause and do not distinguish them. Pearl: the best prevention is '
                            'controlling noise at its source plus consistently and properly fitted hearing '
                            'protection.',
             'domain': 'Otology / Neurotology',
             'topic': 'Noise-induced hearing loss pattern'},
 'audnew2': {'question': 'A 4-year-old has air-conduction thresholds of 30-35 dB HL bilaterally with bone '
                         'conduction of 5-10 dB HL, Type B normal-volume tympanograms, and dull immobile '
                         'tympanic membranes with fluid on otoscopy. If the bilateral effusion has persisted '
                         'for 3 months, what is the most appropriate management?',
             'choices': ['Observe for at least 6 more months, because tubes are not considered before 9 '
                         'months of effusion',
                         'Prescribe intranasal corticosteroids and a course of oral antibiotics to clear the '
                         'effusion',
                         'Offer bilateral tympanostomy tubes, given 3 months of bilateral effusion with '
                         'documented hearing loss',
                         'Place tubes only if the child also develops recurrent acute otitis media with '
                         'effusion'],
             'answer': 2,
             'explanation': 'The AAO-HNS tympanostomy tube guideline supports offering bilateral tubes to '
                            'children with bilateral OME lasting 3 months or longer and documented hearing '
                            'difficulty, which this child has. The guideline recommends against intranasal '
                            'or systemic steroids and antibiotics for OME. Prolonged observation is not '
                            'required once the duration and hearing criteria are met. Pearl: shared '
                            "decision-making and the child's individual risk factors still shape the timing.",
             'domain': 'Pediatric Otolaryngology',
             'topic': 'Tympanostomy tube indications for OME'},
 'ae1': {'question': 'An infant has robust otoacoustic emissions bilaterally, but click ABR shows no '
                     'reproducible neural waveform at 90 dB nHL. Tympanograms are Type A and acoustic '
                     'reflexes are absent bilaterally. Which interpretation best explains these findings?',
         'choices': ['Preserved outer-hair-cell function with abnormal neural synchrony',
                     'Bilateral conductive loss from middle-ear dysfunction',
                     'Severe outer-hair-cell loss with an intact auditory nerve',
                     'Normal hearing with a technically failed ABR recording'],
         'answer': 0,
         'explanation': 'Present OAEs show working outer hair cells, while an absent ABR and absent reflexes '
                        'show failed synchronous neural transmission. This discordance localizes the problem '
                        'and fits auditory neuropathy spectrum disorder. Outer-hair-cell loss would abolish '
                        'the OAEs, and normal tympanometry argues against a conductive cause. Pearl: look '
                        'for a cochlear microphonic that inverts when stimulus polarity is reversed, and get '
                        'MRI to assess for cochlear nerve deficiency.',
         'domain': 'Pediatric Otolaryngology',
         'topic': 'OAE-ABR discordance'},
 'ae2': {'question': 'A patient with similar behavioral thresholds in both ears undergoes ABR testing. Right '
                     'waves I/III/V are 1.7/4.1/6.3 ms (I-V interval 4.6 ms, prolonged for the lab). Left '
                     'waves are 1.6/3.7/5.4 ms (I-V 3.8 ms). The interaural I-V difference of 0.8 ms is '
                     'abnormal, and waveforms are reproducible. What is the most appropriate next step?',
         'choices': ['Repeat the ABR in one year, because the thresholds are symmetric',
                     'Obtain gadolinium-enhanced MRI of the internal auditory canals and brainstem',
                     'Obtain a noncontrast CT scan of the temporal bones',
                     "Fit a right hearing aid and reassess the patient's word recognition"],
         'answer': 1,
         'explanation': 'A reproducibly prolonged I-V interval on one side, with similar peripheral '
                        'sensitivity, points to slowed conduction in the eighth nerve or brainstem. MRI with '
                        'gadolinium is the definitive test. Symmetric thresholds do not exclude a '
                        'retrocochlear lesion, and CT cannot show small tumors in the internal auditory '
                        'canal. Pearl: interpeak intervals measure neural conduction, so a cochlear loss '
                        'alone should not prolong them.',
         'domain': 'Otology / Neurotology',
         'topic': 'ABR interpeak latency asymmetry'},
 'ae3': {'question': 'A 2-month-old referred from newborn screening has tone-burst ABR thresholds of 30 dB '
                     'nHL (right) and 35 dB nHL (left) at 500 Hz, 1, 2 and 4 kHz. OAEs are present and 1 kHz '
                     'tympanometry is normal bilaterally. Which statement about using these results is most '
                     'accurate?',
         'choices': ['Treat the nHL values as behavioral dB HL and fit hearing aids for a mild loss',
                     'Defer all management decisions until reliable behavioral testing at age three',
                     'Convert to estimated HL with frequency-specific corrections, and confirm with VRA when '
                     'feasible',
                     'Repeat a click ABR, because it gives more accurate frequency-specific thresholds'],
         'answer': 2,
         'explanation': 'Tone-burst ABR estimates frequency-specific sensitivity in infants, but nHL values '
                        'must be converted to estimated hearing levels with lab-specific frequency and '
                        'transducer corrections before management decisions. These estimates allow '
                        'amplification to start early when needed. Using nHL directly as HL overestimates '
                        'the loss, and click ABR is not frequency-specific. Pearl: OAEs and 1 kHz '
                        'tympanometry strengthen interpretation, and visual reinforcement audiometry should '
                        'confirm the estimates once development allows.',
         'domain': 'Pediatric Otolaryngology',
         'topic': 'Tone-burst ABR threshold estimation'},
 'ae4': {'question': 'A toddler has absent OAEs bilaterally. Tympanograms are Type B with normal ear-canal '
                     'volume bilaterally, and diagnostic ABR has not yet been done. Which interpretation is '
                     'most appropriate?',
         'choices': ['The absent emissions with flat tympanograms establish auditory neuropathy spectrum '
                     'disorder',
                     'The absent emissions confirm permanent bilateral outer-hair-cell sensorineural loss',
                     'OAEs are unaffected by middle-ear status, so the tympanograms can be set aside',
                     'Middle-ear effusion can abolish OAEs, so the site of the lesion is still undetermined'],
         'answer': 3,
         'explanation': 'OAEs must travel back through the middle ear, so effusion can produce a refer '
                        'result even with a normal cochlea. Auditory neuropathy cannot be diagnosed from '
                        'absent OAEs; its classic pattern is present OAEs with an abnormal ABR. Permanent '
                        'sensorineural loss cannot be assumed until middle-ear function is addressed. Pearl: '
                        'interpret OAEs together with tympanometry, and use diagnostic ABR with air and bone '
                        'conduction to separate conductive from sensorineural causes.',
         'domain': 'Pediatric Otolaryngology',
         'topic': 'Absent OAEs and middle-ear status'},
 'ae6': {'question': 'During skull-base surgery with intraoperative ABR monitoring, wave V shifts from 6.2 '
                     'ms and 0.35 microvolts at baseline to 7.4 ms and 0.15 microvolts right after a '
                     'retraction maneuver. That is a 1.2 ms latency increase and a 57% amplitude drop, which '
                     "meets the program's alert criteria. What is the most appropriate immediate response?",
         'choices': ['Notify the surgeon, pause or reverse the maneuver, check technical and physiologic '
                     'factors, then reassess',
                     'Continue the dissection and repeat the ABR at closure to see whether the change has '
                     'recovered',
                     'Attribute the change to anesthetic depth and keep going without informing the surgeon',
                     'Stop monitoring, because one large change means hearing is already lost'],
         'answer': 0,
         'explanation': 'A significant change in a monitored response is useful only if it leads to '
                        'immediate communication and action: tell the surgeon, relieve the provoking '
                        'maneuver when possible, and rule out technical, temperature, blood pressure and '
                        'anesthetic causes. Delaying until closure loses the chance to reverse the injury. '
                        'ABR is relatively resistant to anesthetic agents, so blaming anesthesia without '
                        'checking is unsafe. Pearl: trends against baseline matter more than any single '
                        'amplitude.',
         'domain': 'Otology / Neurotology',
         'topic': 'Intraoperative ABR monitoring'},
 'ae7': {'question': 'A term newborn refers in the right ear and passes in the left on a two-stage OAE/AABR '
                     'screening protocol before discharge. What is the most appropriate next step?',
         'choices': ['Reassure the family, because one normal ear supports speech development',
                     'Arrange a diagnostic audiologic evaluation, including ABR, before 3 months',
                     'Repeat the screen at the 12-month well-child visit',
                     'Obtain a CT scan of the temporal bones before any further hearing testing'],
         'answer': 1,
         'explanation': 'A refer result on screening shows risk, not a diagnosis, and it needs a diagnostic '
                        'audiologic evaluation under the EHDI 1-3-6 benchmarks (screen by 1 month, diagnose '
                        'by 3 months, intervene by 6 months). Programs increasingly aim for 1-2-3. '
                        'Unilateral hearing loss matters for development and should not be dismissed, and '
                        'imaging comes after the loss is confirmed. Pearl: loss to follow-up is the main '
                        'systems failure, and testing for congenital CMV must be done within the first 21 '
                        'days to diagnose it as congenital.',
         'domain': 'Pediatric Otolaryngology',
         'topic': 'Newborn hearing screen follow-up'},
 'ae8': {'question': 'A patient has behavioral thresholds of 70-90 dB HL bilaterally and absent OAEs. ABR '
                     'thresholds are elevated, with waveform morphology appropriate for a cochlear loss. MRI '
                     'of the internal auditory canals shows cochlear nerves of normal caliber bilaterally. '
                     'Which interpretation best integrates these findings?',
         'choices': ['Auditory neuropathy spectrum disorder, because the OAEs are absent',
                     'Cochlear nerve deficiency, because the ABR thresholds are elevated',
                     'Bilateral conductive loss, because both OAEs and ABR are abnormal',
                     'Severe cochlear sensorineural loss, with all tests in agreement'],
         'answer': 3,
         'explanation': 'Absent OAEs, an elevated ABR with cochlear-type morphology, severe behavioral '
                        'thresholds and normal cochlear nerves all point to severe cochlear sensorineural '
                        'loss. Auditory neuropathy classically shows preserved outer-hair-cell function, '
                        'such as present OAEs or a cochlear microphonic, along with an abnormal neural '
                        'response. The normal MRI argues against cochlear nerve deficiency. Pearl: start '
                        'with well-fitted amplification, and move to cochlear implant evaluation if aided '
                        'speech benefit is limited.',
         'domain': 'Otology / Neurotology',
         'topic': 'Integrated cochlear loss localization'},
 'vest1': {'question': 'Bithermal caloric testing shows peak slow-phase velocities of 25 deg/s (warm) and 20 '
                       'deg/s (cool) on the right, and 10 deg/s (warm) and 8 deg/s (cool) on the left. The '
                       'Jongkees unilateral weakness formula gives 43%, and fixation suppression is intact. '
                       'Which interpretation is most accurate?',
           'choices': ['A right-sided unilateral weakness, since the right responses are the more extreme '
                       'values',
                       'A left peripheral horizontal-canal (superior vestibular pathway) weakness',
                       'Bilateral vestibular hypofunction, because both sides respond below 30 deg/s',
                       'A central vestibular lesion, shown by the asymmetry between the two ears'],
           'answer': 1,
           'explanation': 'The left responses are much smaller than the right, and a 43% weakness is well '
                          'above common lab cutoffs, indicating reduced left horizontal-canal and superior '
                          'vestibular nerve function. Intact fixation suppression argues against a central '
                          'cause. Per-side totals of this size are far above those used to define bilateral '
                          'vestibulopathy. Pearl: calorics test each ear separately at a very low stimulus '
                          "frequency, so always apply your own lab's norms.",
           'domain': 'Otology / Neurotology',
           'topic': 'Caloric unilateral weakness'},
 'vest2': {'question': 'Video head impulse testing shows right horizontal canal gain of 0.95 with no '
                       'saccades and left horizontal canal gain of 0.55 with overt corrective saccades. '
                       'Vertical canal gains are 0.85-0.95 bilaterally. Device norms for horizontal gain are '
                       'about 0.8 or higher. Which interpretation is most accurate?',
           'choices': ['Right horizontal canal hypofunction, because the eyes drift toward the right',
                       'A central lesion, because only one canal plane is affected',
                       'A normal study, because overt saccades are expected during fast impulses',
                       'Reduced high-frequency VOR function of the left horizontal canal'],
           'answer': 3,
           'explanation': 'Low gain on head impulses toward the left, plus corrective saccades, shows the '
                          'left horizontal-canal VOR cannot stabilize gaze, which means peripheral '
                          'hypofunction on that side. The saccades are a compensating catch-up movement, not '
                          'a normal finding. vHIT gain is reported for the side toward which the head is '
                          'turned. Pearl: also check for covert saccades and tracing artifacts, and remember '
                          'that vHIT and calorics test different frequencies.',
           'domain': 'Otology / Neurotology',
           'topic': 'vHIT interpretation'},
 'vest3': {'question': 'A 62-year-old has brief vertigo when rolling over in bed. Right Dix-Hallpike testing '
                       'produces upbeating nystagmus with torsion toward the right ear, beginning after a '
                       '3-5 second latency and lasting less than 60 seconds, and it fatigues with '
                       'repetition. Neurologic exam is otherwise normal. What is the best next step?',
           'choices': ['Perform a right-sided canalith repositioning (Epley) maneuver',
                       'Perform a barbecue roll maneuver toward the right side',
                       'Prescribe meclizine and reassess the patient in two weeks',
                       'Obtain MRI of the brain before attempting any treatment'],
           'answer': 0,
           'explanation': 'A brief, latent, fatigable upbeating torsional nystagmus with the right ear down '
                          'is diagnostic of right posterior-canal BPPV, and the AAO-HNS guideline recommends '
                          'canalith repositioning. The barbecue roll is for horizontal-canal BPPV, which '
                          'gives direction-changing horizontal nystagmus on the supine roll test. Routine '
                          'vestibular suppressants and imaging are not recommended for typical BPPV. Pearl: '
                          'the upper pole of the eye beats toward the affected, downward ear.',
           'domain': 'Otology / Neurotology',
           'topic': 'Posterior canal BPPV treatment'},
 'vest4': {'question': 'A patient with chronic dizziness has VNG showing saccadic smooth pursuit in both '
                       'directions and gaze-evoked nystagmus that changes direction with the direction of '
                       'gaze. Saccade velocity and accuracy are normal, and there is no spontaneous '
                       'nystagmus. Which interpretation and next step are most appropriate?',
           'choices': ['Right peripheral vestibular hypofunction, so begin vestibular rehabilitation',
                       'Bilateral peripheral loss, so order rotary chair testing to confirm it',
                       'Central oculomotor dysfunction, so review sedating drugs and obtain brain MRI',
                       'Expected age-related change, so reassure the patient and repeat testing in a year'],
           'answer': 2,
           'explanation': 'Saccadic pursuit and direction-changing gaze-evoked nystagmus are signs of '
                          'central dysfunction, typically involving the cerebellum or brainstem, rather than '
                          'labyrinthine disease. Peripheral lesions produce unidirectional nystagmus that '
                          'does not change direction with gaze. Anticonvulsants, sedatives and alcohol can '
                          'cause the same signs and should be reviewed. Pearl: the oculomotor part of the '
                          'VNG tests central pathways, so abnormal findings there should lead to a '
                          'neurologic evaluation.',
           'domain': 'Otology / Neurotology',
           'topic': 'Central oculomotor signs on VNG'},
 'v8': {'question': 'A patient with recurrent episodic vertigo has a 40% right caloric weakness, but video '
                    'head impulse testing shows normal horizontal canal gains bilaterally with no corrective '
                    'saccades. Both studies are technically adequate. What is the best explanation?',
        'choices': ['The caloric result must be wrong, because vHIT is more objective',
                    'The two tests measure VOR at different frequencies, which disease can affect '
                    'differently',
                    'The dissociation indicates a central lesion that has spared the labyrinth',
                    'The normal vHIT result must be wrong, because calorics are the reference standard'],
        'answer': 1,
        'explanation': 'Calorics test very low-frequency horizontal-canal function, while vHIT tests '
                       'high-frequency, high-acceleration responses, and disease or compensation can affect '
                       'these ranges differently. This mismatch is well described in Meniere disease. '
                       'Treating either test as automatically wrong discards real physiologic information, '
                       'and the mismatch does not suggest a central lesion. Pearl: interpret calorics, vHIT, '
                       'VEMPs and hearing together as a frequency-specific test battery.',
        'domain': 'Otology / Neurotology',
        'topic': 'Caloric-vHIT dissociation'},
 'v9': {'question': "After an episode of acute continuous vertigo, a patient's video head impulse testing "
                    'shows left horizontal canal gain of 0.5 with corrective saccades. Left posterior canal '
                    'gain and all right-sided canal gains are normal. Which pathway is most likely affected?',
        'choices': ['The left superior vestibular nerve',
                    'The left inferior vestibular nerve',
                    'The left cochlear nerve and the saccule',
                    'The right vestibular nucleus in the brainstem'],
        'answer': 0,
        'explanation': 'The superior vestibular nerve supplies the horizontal and anterior canals and the '
                       'utricle, so a horizontal-canal deficit with a spared posterior canal localizes to '
                       'that division. The inferior vestibular nerve supplies the posterior canal and the '
                       'saccule, which are normal here. Pearl: map the affected canals, then add cVEMP '
                       '(saccule and inferior nerve) and oVEMP (utricle and superior nerve) to define how '
                       'much of the nerve is involved.',
        'domain': 'Otology / Neurotology',
        'topic': 'Vestibular nerve division localization'},
 'v10': {'question': 'A 40-year-old has an absent left air-conducted cVEMP despite adequate, symmetric '
                     'sternocleidomastoid contraction confirmed by EMG monitoring. Air and bone thresholds '
                     'are equal in both ears, with no conductive component. Which pathway does this result '
                     'primarily implicate?',
         'choices': ['The left utricle and superior vestibular nerve, through the ocular reflex',
                     'The left horizontal semicircular canal and its vestibulo-ocular reflex',
                     'The left cochlear nerve, through the acoustic stapedial reflex arc',
                     'The left saccule and inferior vestibular nerve, through the vestibulocollic reflex'],
         'answer': 3,
         'explanation': 'cVEMP is an inhibitory response in the sternocleidomastoid on the same side, driven '
                        'mainly by the saccule and inferior vestibular nerve. The utricle and superior nerve '
                        'are tested mainly by oVEMP. Poor muscle activation, older age and conductive '
                        'hearing loss can all abolish an air-conducted VEMP, so those factors had to be '
                        'excluded here. Pearl: combine cVEMP with oVEMP, vHIT and calorics to map which '
                        'vestibular end organs and nerve divisions are affected.',
         'domain': 'Otology / Neurotology',
         'topic': 'cVEMP pathway'},
 'v11': {'question': 'A patient reports autophony, hearing her own footsteps, and vertigo triggered by loud '
                     'sounds in the right ear. On the right, oVEMP amplitudes are markedly enhanced and VEMP '
                     'thresholds are abnormally low; left responses are normal. What is the best next step '
                     'to evaluate this?',
         'choices': ['Gadolinium-enhanced MRI of the internal auditory canals',
                     'Electrocochleography to measure the SP/AP ratio',
                     'Thin-section temporal bone CT with superior canal reformats',
                     'Exploratory tympanotomy with a planned stapedotomy'],
         'answer': 2,
         'explanation': 'Enhanced, low-threshold VEMPs together with sound- and pressure-induced symptoms '
                        'support third-window physiology, and the diagnosis needs thin-section temporal bone '
                        'CT reformatted in the Poschl and Stenvers planes. MRI does not reliably show thin '
                        'bone over the canal. A stapedotomy for a pseudoconductive gap would not help and '
                        'can worsen symptoms. Pearl: CT can overcall dehiscence, so require symptoms, '
                        'physiology and imaging to agree before diagnosing superior canal dehiscence '
                        'syndrome.',
         'domain': 'Otology / Neurotology',
         'topic': 'Superior canal dehiscence evaluation'},
 'v12': {'question': 'A patient with positional dizziness undergoes positional testing. The nystagmus begins '
                     'without latency, persists as long as each position is held, does not fatigue, and does '
                     'not match the plane of any single semicircular canal. Direction-changing gaze-evoked '
                     'nystagmus is also present while sitting. Two prior repositioning maneuvers did not '
                     'help. What is the most appropriate next step?',
         'choices': ['Repeat the repositioning maneuvers weekly until the nystagmus resolves',
                     'Prescribe a vestibular suppressant and reassess the patient in one month',
                     'Perform a careful neurologic examination and obtain brain MRI',
                     'Teach the patient Brandt-Daroff exercises for home habituation'],
         'answer': 2,
         'explanation': 'Positional nystagmus with no latency, no fatigue, no fit to a canal plane, and '
                        'accompanying gaze-evoked nystagmus is a central pattern. It warrants neurologic '
                        'evaluation and imaging of the posterior fossa. Repeating maneuvers or using '
                        'suppressants delays diagnosis of lesions such as cerebellar tumors, demyelination '
                        'or stroke. Pearl: not all positional vertigo is BPPV, and an atypical pattern that '
                        'fails treatment should prompt a search for a central cause.',
         'domain': 'Otology / Neurotology',
         'topic': 'Central positional nystagmus'},
 'v13': {'question': 'A 66-year-old with hypertension has had continuous vertigo, nausea and spontaneous '
                     'nystagmus for 10 hours. The bedside head impulse test is normal in both directions, '
                     'the gaze-evoked nystagmus changes direction with gaze, and alternate cover testing '
                     'shows a skew deviation. What is the most appropriate next step?',
         'choices': ['Start oral corticosteroids for presumed vestibular neuritis and arrange outpatient '
                     'follow-up',
                     'Perform canalith repositioning maneuvers and recheck the patient after the maneuver',
                     'Obtain a noncontrast head CT and discharge the patient if it is normal',
                     'Activate the stroke pathway with urgent MRI including diffusion-weighted imaging'],
         'answer': 3,
         'explanation': 'In acute vestibular syndrome, a normal head impulse, direction-changing nystagmus '
                        'or skew deviation is a central HINTS pattern, and posterior circulation stroke must '
                        'be presumed. A normal noncontrast CT does not exclude posterior fossa stroke, and '
                        'early diffusion-weighted MRI can also miss small infarcts. Steroids or '
                        'repositioning would treat the wrong disease. Pearl: HINTS applies only to '
                        'continuous acute vestibular syndrome with ongoing nystagmus, not to brief episodic '
                        'or positional dizziness.',
         'domain': 'General ENT / Emergencies',
         'topic': 'HINTS central pattern'},
 'vest-v126-bilateral-vestibulopathy': {'question': 'After a course of IV gentamicin, a patient has chronic '
                                                    'unsteadiness when walking, oscillopsia during head '
                                                    'movement, and much worse balance in darkness and on '
                                                    'uneven ground. Symptoms are absent when sitting still. '
                                                    'vHIT shows horizontal gain below 0.6 bilaterally with '
                                                    'corrective saccades, and bithermal caloric responses '
                                                    'are markedly reduced on both sides. Which statement is '
                                                    'most accurate?',
                                        'choices': ['This is bilateral vestibulopathy, and a low '
                                                    'unilateral-weakness percentage would not exclude it',
                                                    'A unilateral-weakness percentage within normal limits '
                                                    'would make vestibular loss unlikely',
                                                    'The pattern indicates persistent postural-perceptual '
                                                    'dizziness rather than a structural loss',
                                                    'The pattern indicates a unilateral peripheral loss that '
                                                    'should be lateralized with cVEMP'],
                                        'answer': 0,
                                        'explanation': 'Chronic unsteadiness and oscillopsia that worsen '
                                                       'when vision or footing is limited, with bilaterally '
                                                       'reduced VOR on vHIT and calorics, fits the Barany '
                                                       'criteria for bilateral vestibulopathy, and '
                                                       'aminoglycosides are a classic cause. The '
                                                       'unilateral-weakness formula compares the two ears '
                                                       'with each other, so two equally weak ears can '
                                                       'produce a near-normal percentage. PPPD does not '
                                                       'cause objective bilateral VOR loss. Pearl: look at '
                                                       'the absolute caloric responses on each side, not '
                                                       'just the asymmetry.',
                                        'domain': 'Otology / Neurotology',
                                        'topic': 'Bilateral vestibulopathy'},
 'vest-v126-rotational-chair': {'question': 'A 3-year-old with delayed walking and a history of bacterial '
                                            'meningitis is suspected of bilateral vestibular loss. The child '
                                            'cannot cooperate with video head impulse testing and cannot '
                                            'tolerate caloric irrigation. Which test is most useful for '
                                            'quantifying horizontal VOR function?',
                                'choices': ['Cervical VEMP testing with air-conducted tone bursts',
                                            'Rotational chair testing with whole-body rotation',
                                            'Computerized dynamic posturography with sensory organization',
                                            'Repeat caloric testing using ice-water irrigation'],
                                'answer': 1,
                                'explanation': 'Rotational chair testing measures horizontal VOR gain, phase '
                                               'and time constant across low-to-middle frequencies, with the '
                                               "child seated on a parent's lap if needed, and is especially "
                                               'good for detecting bilateral loss. cVEMP tests the saccule '
                                               'rather than the horizontal VOR, and posturography measures '
                                               'balance function rather than the reflex. Because both '
                                               'labyrinths are stimulated together, the chair is weaker than '
                                               'calorics at lateralizing a one-sided lesion. Pearl: after '
                                               'meningitis, also check hearing urgently, because cochlear '
                                               'ossification can narrow the window for cochlear '
                                               'implantation.',
                                'domain': 'Pediatric Otolaryngology',
                                'topic': 'Rotational chair testing'},
 'vestnew1': {'question': 'A 45-year-old developed continuous vertigo, nausea and imbalance over several '
                          'days, without hearing loss. Acute bedside HINTS showed an abnormal left head '
                          'impulse, unidirectional right-beating nystagmus and no skew. Later testing shows '
                          'about 62% left caloric weakness, left horizontal vHIT gain of 0.45 with catch-up '
                          'saccades, and a normal audiogram. Which diagnosis best fits?',
              'choices': ['Right vestibular neuritis, because the nystagmus beats toward the right',
                          'Left labyrinthitis, because the deficit includes both canal and caloric loss',
                          'Left vestibular neuritis involving the superior vestibular nerve',
                          'Posterior circulation stroke, because the nystagmus was unidirectional'],
              'answer': 2,
              'explanation': 'Continuous vertigo with a peripheral HINTS pattern, nystagmus beating away '
                             'from the weak side, objective left horizontal-canal loss and normal hearing '
                             'fits left vestibular neuritis. Labyrinthitis would also cause sensorineural '
                             'hearing loss. In a peripheral lesion, the fast phase beats away from the '
                             'affected ear, and unidirectional nystagmus with an abnormal head impulse and '
                             'no skew is the reassuring pattern. Pearl: symptoms can improve through central '
                             'compensation even when caloric or vHIT loss persists, so vestibular '
                             'rehabilitation matters.',
              'domain': 'Otology / Neurotology',
              'topic': 'Acute unilateral vestibulopathy'},
 'vestnew2': {'question': 'A 50-year-old has had several spontaneous attacks of vertigo lasting 30-60 '
                          'minutes, with fluctuating right fullness, tinnitus and hearing loss. Right '
                          'thresholds are 40, 35 and 30 dB HL at 250, 500 and 1000 Hz, with air equal to '
                          'bone, and 15, 15 and 10 dB HL at 2, 4 and 8 kHz; the left ear is 10 dB HL at 250, '
                          '500 and 1000 Hz. Calorics show about 30% right weakness, and ECoG shows an '
                          'elevated SP/AP ratio. Which statement is most accurate?',
              'choices': ['Definite disease cannot be diagnosed without a caloric weakness of at least 50%',
                          'An elevated SP/AP ratio is required to move from probable to definite disease',
                          'Attacks of 30-60 minutes are too short, which points to vestibular migraine',
                          'The clinical criteria for definite disease are met, and ECoG is supportive only'],
              'answer': 3,
              'explanation': 'Two or more spontaneous attacks of 20 minutes to 12 hours, with '
                             'audiometrically documented low-to-medium-frequency sensorineural loss in the '
                             'affected ear and fluctuating aural symptoms, and no better explanation, meet '
                             'the Barany/AAO-HNS criteria for definite Meniere disease. ECoG and calorics '
                             'may support the diagnosis but are not required, and there is no caloric '
                             'threshold for diagnosis. Pearl: asymmetric sensorineural loss still usually '
                             'warrants MRI to exclude a retrocochlear lesion.',
              'domain': 'Otology / Neurotology',
              'topic': 'Meniere disease diagnostic criteria'},
 'ct1': {'question': 'Axial contrast-enhanced neck CT shows a well-defined suprahyoid mass. The internal '
                     'carotid artery and internal jugular vein are pushed together as a single unit, with no '
                     'widening of the space between the two vessels. What does this displacement pattern '
                     'most strongly indicate?',
         'choices': ['The mass arises from the vagus nerve, which lies between the artery and the vein',
                     'The mass arises outside the carotid sheath and displaces the sheath as a whole',
                     'The mass is a carotid body tumor arising at the bifurcation of the carotid artery',
                     'The mass arises from the wall of the internal jugular vein within the sheath'],
         'answer': 1,
         'explanation': 'When the carotid artery and jugular vein move together, the lesion is pushing the '
                        'carotid sheath from outside rather than growing between its contents. A vagal '
                        'schwannoma or paraganglioma arises within the sheath and characteristically '
                        'separates the artery from the vein, while a carotid body tumor splays the internal '
                        'and external carotid arteries. Pearl: read the direction of vessel displacement and '
                        'the epicenter before you think about tumor names.',
         'domain': 'Head & Neck Oncology',
         'topic': 'Carotid sheath displacement and space of origin'},
 'ct_sliceviewer_v44': {'question': 'On a single axial slice of a contrast-enhanced neck CT, a 1.5 cm round '
                                    'structure lies just lateral to the right carotid artery, deep to the '
                                    'sternocleidomastoid. It enhances to the same degree as the '
                                    'contralateral internal jugular vein, and the right internal jugular '
                                    'vein is not obviously seen at that level. What is the best next step?',
                        'choices': ['Report a necrotic level III lymph node and recommend fine-needle '
                                    'aspiration',
                                    'Recommend MRI with gadolinium to characterize the round enhancing '
                                    'structure',
                                    'Scroll through contiguous slices to see if it is continuous with the '
                                    'jugular vein',
                                    'Recommend ultrasound-guided core biopsy because the lesion is solid and '
                                    'enhancing'],
                        'answer': 2,
                        'explanation': 'A round structure that matches venous enhancement in the expected '
                                       'position of the jugular vein is most often the vein itself, '
                                       'sometimes asymmetrically large, and following it on adjacent slices '
                                       'shows that it is a continuous tube rather than a nodule. Calling it '
                                       'a node and biopsying it misreads normal anatomy that only looks like '
                                       'a mass on one static image. Pearl: scroll in three dimensions before '
                                       'calling a mass; tubular continuity across slices means vessel.',
                        'domain': 'Head & Neck Oncology',
                        'topic': 'Scrolling CT anatomy: vessel versus node'},
 'ct2': {'question': 'A 45-year-old has a painless, pulsatile mass at the carotid bifurcation. Contrast CT '
                     'shows an avidly enhancing 3 cm mass that splays the internal and external carotid '
                     'arteries apart. The patient is scheduled for a clinic visit to discuss tissue '
                     'diagnosis. What is the most appropriate next step?',
         'choices': ['Perform an open incisional biopsy to confirm the histology before planning',
                     'Perform ultrasound-guided core needle biopsy to obtain a firm tissue diagnosis',
                     'Perform fine-needle aspiration under ultrasound guidance in the clinic today',
                     'Avoid biopsy, check plasma free metanephrines, and plan based on imaging'],
         'answer': 3,
         'explanation': 'Splaying of the internal and external carotid arteries by an avidly enhancing mass '
                        'is the classic appearance of a carotid body paraganglioma, which is diagnosed by '
                        'imaging and should not be biopsied because of bleeding risk. Screening for '
                        'catecholamine secretion before any intervention is standard, since an unrecognized '
                        'secreting tumor can cause a hypertensive crisis. Pearl: before touching a deep neck '
                        'mass, confirm its vascular relationships and vascularity because they decide '
                        'whether biopsy is safe at all.',
         'domain': 'Head & Neck Oncology',
         'topic': 'Pre-biopsy imaging: vascular relationship of a neck mass'},
 'ct3': {'question': 'A patient with adenoid cystic carcinoma of the hard palate has new numbness of the '
                     'cheek. Contrast-enhanced, fat-suppressed MRI shows the primary tumor plus loss of the '
                     'normal fat in the pterygopalatine fossa and enlargement and enhancement of the '
                     'maxillary nerve to the foramen rotundum. How does this finding most change the '
                     'treatment plan?',
         'choices': ['It suggests reactive inflammation, so the treatment fields can stay at the primary '
                     'site',
                     'It indicates spread along the nerve, so surgery and radiation must cover the nerve '
                     'path to the skull base',
                     'It indicates hematogenous spread, so systemic therapy should replace local treatment',
                     'It reflects postbiopsy change, so imaging should be repeated in six months before '
                     'planning'],
         'answer': 1,
         'explanation': 'Nerve enlargement and enhancement with effacement of the pterygopalatine fossa fat '
                        'is the imaging hallmark of perineural tumor spread, and it extends the disease well '
                        'beyond the visible primary. Treatment must address the nerve course toward the '
                        "foramen and possibly Meckel's cave, so dismissing it as inflammation would "
                        'undertreat the tumor. Pearl: in adenoid cystic carcinoma and cutaneous or mucosal '
                        'squamous carcinoma, trace each named nerve to the skull base on contrast '
                        'fat-suppressed MRI.',
         'domain': 'Head & Neck Oncology',
         'topic': 'Perineural spread on MRI'},
 'ct_ethmoid_map_v42': {'question': 'During review of a preoperative sinus CT, you trace the basal lamella '
                                    'of the middle turbinate from its lateral attachment. During surgery you '
                                    'have completed the anterior ethmoidectomy and now pass posterior to '
                                    'this lamella. Which relationship becomes most important to track as you '
                                    'continue?',
                        'choices': ['The frontal recess and the anterior ethmoid artery as it crosses the '
                                    'ethmoid roof',
                                    'The nasolacrimal duct running in the bone anterior to the maxillary '
                                    'sinus ostium',
                                    'The posterior ethmoid cells near the sphenoid, posterior skull base, '
                                    'and optic nerve',
                                    'The uncinate process and the natural ostium of the maxillary sinus at '
                                    'the infundibulum'],
                        'answer': 2,
                        'explanation': 'The basal lamella divides the anterior from the posterior ethmoid, '
                                       'so crossing it places you in the posterior ethmoid next to the '
                                       'superior turbinate, sphenoid, posterior skull base, and optic nerve. '
                                       'The frontal recess, anterior ethmoid artery, uncinate, and '
                                       'nasolacrimal duct are anterior structures you have already passed. '
                                       'Pearl: keep the lamina papyracea laterally and the skull base '
                                       'superiorly in view at all times, and know which compartment you are '
                                       'in.',
                        'domain': 'Rhinology / Allergy / Skull Base',
                        'topic': 'Basal lamella and posterior ethmoid boundaries'},
 'ct_onodi_v42': {'question': 'Preoperative CT for endoscopic sinus surgery shows a posterior ethmoid cell '
                              'that pneumatizes superior and lateral to the sphenoid sinus, with the optic '
                              'nerve bulging into its lateral wall. Which statement best guides the '
                              'operative plan?',
                  'choices': ['The optic nerve is at risk in the posterior ethmoid, so identify the true '
                              'sphenoid before working laterally',
                              'The optic nerve is at risk only in the sphenoid sinus, so the posterior '
                              'ethmoid cells can be cleared freely',
                              'Image guidance makes this anatomy safe, so landmark-based identification is '
                              'no longer necessary',
                              'This cell protects the optic nerve, so its lateral wall can be removed '
                              'aggressively without concern'],
                  'answer': 0,
                  'explanation': 'A sphenoethmoidal (Onodi) cell can put the optic nerve, and sometimes the '
                                 'carotid, in the lateral wall of what looks like the last ethmoid cell, so '
                                 'a surgeon who assumes optic risk begins at the sphenoid can injure the '
                                 'nerve. The true sphenoid usually lies medial and inferior to this cell and '
                                 'should be confirmed before lateral dissection. Image guidance supports, '
                                 'but does not replace, CT review and landmark recognition. Pearl: look for '
                                 'this cell on every coronal CT before posterior ethmoid surgery.',
                  'domain': 'Rhinology / Allergy / Skull Base',
                  'topic': 'Onodi cell and optic nerve risk'},
 'ct_chol_v42': {'question': 'A patient has chronic otorrhea. Temporal bone CT shows nondependent soft '
                             'tissue in the epitympanum and mastoid. Which additional CT finding most '
                             'supports a keratinizing destructive process rather than simple fluid or '
                             'mucosal opacification?',
                 'choices': ['Blunting of the scutum with erosion of the ossicles',
                             'A dependent air-fluid level in the mastoid air cells',
                             'Diffuse opacification of the middle ear with intact bone',
                             'A well-pneumatized mastoid with intact bony septa'],
                 'answer': 0,
                 'explanation': 'Soft tissue paired with focal scutal blunting and ossicular erosion is the '
                                'CT pattern that raises concern for cholesteatoma, because simple effusion '
                                'or inflamed mucosa does not usually erode bone. An air-fluid level or '
                                'opacification with intact bone points toward fluid or mucosal disease. CT '
                                'maps bone and complications but cannot reliably identify the soft tissue '
                                'itself, which is where non-echo-planar diffusion-weighted MRI helps. Pearl: '
                                'CT gives the bony map; otoscopy and diffusion MRI identify the tissue.',
                 'domain': 'Otology / Neurotology',
                 'topic': 'Temporal bone CT signs of cholesteatoma'},
 'ct_sgs_v42': {'question': 'A 3-year-old with a history of prolonged intubation has biphasic stridor. Neck '
                            'CT shows a short segment of subglottic narrowing, and the family asks about '
                            'airway reconstruction. What is the most appropriate next step before planning '
                            'the operation?',
                'choices': ['Proceed with reconstruction planned from the CT measurements of length and '
                            'diameter',
                            'Repeat the CT with three-dimensional reconstruction to grade the stenosis more '
                            'precisely',
                            'Perform direct microlaryngoscopy and bronchoscopy to stage the airway in full',
                            'Obtain an MRI of the neck to assess the cartilage framework before deciding'],
                'answer': 2,
                'explanation': 'Direct laryngoscopy and bronchoscopy are needed to determine the grade and '
                               'length of the stenosis, whether the scar is mature, glottic and posterior '
                               'involvement, vocal fold mobility, and any synchronous airway lesions. Better '
                               'cross-sectional imaging cannot provide this functional and mucosal '
                               'information. CT can still add framework and extraluminal detail when those '
                               'questions matter. Pearl: no airway reconstruction is planned without '
                               'endoscopy.',
                'domain': 'Pediatric Otolaryngology',
                'topic': 'Subglottic stenosis: endoscopy before reconstruction'},
 'ct_neckspace_v42': {'question': 'Contrast-enhanced CT shows a suprahyoid mass centered posterior to the '
                                  'styloid process. It displaces the parapharyngeal fat anteriorly and '
                                  'pushes the internal carotid artery anteriorly. Which space does the mass '
                                  'most likely arise from?',
                      'choices': ['The prestyloid parapharyngeal space',
                                  'The masticator space',
                                  'The retropharyngeal space',
                                  'The carotid (poststyloid) space'],
                      'answer': 3,
                      'explanation': 'A mass centered behind the styloid that pushes the parapharyngeal fat '
                                     'and internal carotid artery forward is arising in the carotid space, '
                                     'where paragangliomas and nerve sheath tumors are common. A prestyloid '
                                     'mass usually pushes the carotid backward, and a retropharyngeal mass '
                                     'pushes the carotid sideways. Pearl: the space of origin predicts which '
                                     'vessels and cranial nerves (here IX to XII and the sympathetic chain) '
                                     'are at risk during surgery.',
                      'domain': 'Head & Neck Oncology',
                      'topic': 'Localizing the space of origin by displacement'},
 'ctnew1': {'question': 'Contrast CT of a soft left level II neck mass shows a smooth-walled, homogeneous '
                        'lesion measuring -85 HU, with no enhancement and no internal soft-tissue component. '
                        'Which additional finding, if present, would most justify further workup such as MRI '
                        'or biopsy?',
            'choices': ["Attenuation equal to that of the patient's subcutaneous fat",
                        'Thick or nodular septa with enhancing nonfatty components',
                        'A thin, smooth capsule that separates the lesion from muscle',
                        'Mild displacement of the sternocleidomastoid without invasion'],
            'answer': 1,
            'explanation': 'A homogeneous, nonenhancing, smooth mass of fat attenuation fits a simple '
                           'lipoma. Thick or nodular septa, enhancing nonfat tissue, incomplete fat '
                           'suppression on MRI, or infiltrative margins raise concern for a '
                           'well-differentiated liposarcoma and warrant further evaluation. A thin capsule, '
                           'fat-equivalent attenuation, and simple displacement are expected features of a '
                           'benign lipoma. Pearl: pure fat with no enhancing soft tissue is reassuring; '
                           'nodular enhancing components are not.',
            'domain': 'Head & Neck Oncology',
            'topic': 'Fat-attenuation neck mass: lipoma versus liposarcoma'},
 'allergy1': {'question': 'A 30-year-old has sneezing, nasal itch, and rhinorrhea only during grass pollen '
                          'season. Skin-prick testing shows: saline control 0 mm, histamine control 5 mm, '
                          'grass 8 mm, cat 4 mm, dust mite 3 mm (wheal diameters). She has no symptoms '
                          'around cats or at home outside the season. What is the best interpretation?',
              'choices': ['The test is invalid because the histamine control wheal is too small to read',
                          'Grass, cat, and mite are all clinically relevant and should be treated equally',
                          'The test is valid; grass is concordant, and cat and mite are likely asymptomatic '
                          'sensitization',
                          'Only the grass result is positive, because cat and mite fall below the 3 mm '
                          'threshold'],
              'answer': 2,
              'explanation': 'The negative control is 0 mm and the histamine control is clearly reactive, so '
                             'the test is valid and a wheal of 3 mm or more over the negative control counts '
                             'as positive. Grass is both the largest wheal and matches the seasonal history, '
                             'while cat and mite are positive by size but do not match her exposures, so '
                             'they represent sensitization that may not cause disease. Pearl: confirm both '
                             'controls first, then treat only the positives that fit the history.',
              'domain': 'Rhinology / Allergy / Skull Base',
              'topic': 'Skin-prick test validity and clinical relevance'},
 'allergy2': {'question': 'Skin-prick testing shows a 4 mm saline (negative) control wheal, a 4 mm histamine '
                          'control wheal, and allergen wheals of 3 to 5 mm. The patient stopped '
                          'antihistamines a week ago. What is the most appropriate interpretation and next '
                          'step?',
              'choices': ['The test cannot be interpreted; consider serum specific IgE or retest after '
                          'addressing the cause',
                          'All allergens of 3 mm or more are positive, so begin allergen immunotherapy for '
                          'each one',
                          'Residual antihistamine effect explains the pattern, so stop the drug longer and '
                          'read the same grid',
                          'Subtract the histamine wheal from each allergen wheal and treat any allergen with '
                          'a positive result'],
              'answer': 0,
              'explanation': 'A reactive negative control means the skin is responding nonspecifically, as '
                             'with dermatographism or poor placement or reading technique, so allergen '
                             'wheals cannot be separated from background and the test is uninterpretable. '
                             'Antihistamines cause the opposite problem, a weak or absent histamine '
                             'response, and would not make the saline control positive. Pearl: when skin '
                             'testing is unreliable, serum specific IgE is a useful alternative.',
              'domain': 'Rhinology / Allergy / Skull Base',
              'topic': 'Failed negative control on skin testing'},
 'allergy3': {'question': 'A patient has rhinitis symptoms only in late spring. Serum specific IgE results: '
                          'timothy grass 12.5 kUA/L, dust mite 3.2 kUA/L, ragweed 0.9 kUA/L. She has no '
                          'perennial or fall symptoms. Which allergen is most clinically relevant for '
                          'treatment planning?',
              'choices': ['Dust mite, because a perennial allergen should be treated first regardless of '
                          'history',
                          'Ragweed, because any positive value should be included in immunotherapy',
                          'All three equally, because each value is above the usual positive cutoff',
                          'Timothy grass, because it matches the seasonal symptoms and is the highest level'],
              'answer': 3,
              'explanation': 'Specific IgE shows sensitization, and the level raises the probability of '
                             'clinical allergy but does not by itself prove disease; relevance comes from '
                             'matching results to exposure and symptoms. Grass pollen fits a late-spring '
                             'pattern, whereas mite would be expected to cause perennial symptoms and '
                             'ragweed fall symptoms. Treating every positive on a broad panel leads to '
                             'overdiagnosis. Pearl: no single number decides treatment; the history does.',
              'domain': 'Rhinology / Allergy / Skull Base',
              'topic': 'Serum specific IgE: sensitization versus allergy'},
 'allergy4': {'question': 'A patient with birch pollen allergy (birch specific IgE 12 kUA/L) has oral '
                          'itching within minutes of eating raw apple but tolerates cooked apple. '
                          'Prick-to-prick testing with fresh apple is 6 mm, while commercial apple extract '
                          'is negative. Which component-testing result would most change counseling toward a '
                          'higher risk of systemic reactions?',
              'choices': ['Sensitization to the birch-related PR-10 protein in apple (Mal d 1)',
                          'Sensitization to the heat-stable lipid transfer protein in apple (Mal d 3)',
                          'Sensitization to the major birch pollen allergen alone (Bet v 1)',
                          'A negative result to the apple protein that matches birch pollen'],
              'answer': 0,
              'explanation': 'This is pollen-food syndrome caused by birch-related PR-10 proteins, which are '
                             'destroyed by heat and processing; that explains why cooked apple and '
                             'commercial extract are tolerated while fresh fruit is positive. Lipid transfer '
                             'proteins are stable to heat and digestion and are linked to more systemic '
                             'reactions, so sensitization to Mal d 3 would change counseling. PR-10 or Bet v '
                             '1 sensitization alone fits the low-risk, localized pattern. Pearl: use '
                             'fresh-food prick-to-prick testing for labile allergens, and components to '
                             'separate low-risk from higher-risk sensitization.',
              'domain': 'Rhinology / Allergy / Skull Base',
              'topic': 'Pollen-food syndrome and component testing'},
 'allergy5': {'question': 'A patient has rhinorrhea, sneezing, and nasal itch with dust exposure. Skin-prick '
                          'and serum specific IgE testing to aeroallergens are negative. Nasal provocation '
                          'with dust mite reproduces sneezing, itching, and rhinorrhea within 15 to 30 '
                          'minutes. Other causes have been excluded. Which phenotype best fits?',
              'choices': ['Nonallergic vasomotor rhinitis',
                          'Rhinitis medicamentosa',
                          'Local allergic rhinitis',
                          'Nonallergic rhinitis with eosinophilia'],
              'answer': 2,
              'explanation': 'A positive nasal allergen challenge with negative skin and serum tests points '
                             'to an allergic response confined to the nasal mucosa, known as local allergic '
                             'rhinitis. Vasomotor rhinitis is triggered by irritants and temperature '
                             'changes, not reproduced by a specific allergen challenge. Pearl: negative '
                             'systemic tests lower the chance of systemic sensitization but do not exclude '
                             'allergy in the nose, so do not label such patients nonallergic by default.',
              'domain': 'Rhinology / Allergy / Skull Base',
              'topic': 'Local allergic rhinitis'},
 'allergy6': {'question': 'A patient on subcutaneous allergen immunotherapy arrives for a scheduled '
                          'injection. His baseline FEV1 is 88% predicted, but today he is wheezing and his '
                          'peak flow is 62% of his personal best. What is the most appropriate action?',
              'choices': ['Give the scheduled dose after an oral antihistamine and observe for 30 minutes',
                          'Give half the scheduled dose and extend the observation period to 60 minutes',
                          'Withhold the injection, assess and treat the asthma, and resume once controlled',
                          'Give the scheduled dose because his baseline FEV1 is above the usual threshold'],
              'answer': 2,
              'explanation': 'Poorly controlled asthma is a major risk factor for severe and fatal systemic '
                             'reactions to immunotherapy, so the injection should be held until the asthma '
                             'is assessed and stabilized. Lowering the dose or premedicating does not remove '
                             'that risk, and his prior good spirometry does not reflect his status today. '
                             'Pearl: check asthma control before every injection, and keep epinephrine ready '
                             'with an observation period for every dose.',
              'domain': 'Rhinology / Allergy / Skull Base',
              'topic': 'Immunotherapy safety: uncontrolled asthma'},
 'allergy7': {'question': 'A 42-year-old has asthma with bronchodilator-responsive obstruction, diffuse '
                          'nasal polyps on sinus CT, and wheeze with nasal congestion 30 to 180 minutes '
                          'after taking ibuprofen. Which management option is most specific to this '
                          'phenotype?',
              'choices': ['Aspirin desensitization followed by daily aspirin in selected patients',
                          'Subcutaneous allergen immunotherapy to the most common aeroallergens',
                          'Avoiding leukotriene modifiers because they worsen this respiratory disease',
                          'Oral antihistamines alone as long-term maintenance for the nasal polyps'],
              'answer': 0,
              'explanation': 'Asthma, nasal polyps, and respiratory reactions to COX-1 inhibitors define '
                             'aspirin-exacerbated respiratory disease, and aspirin desensitization with '
                             'daily aspirin, often after sinus surgery, is a treatment specific to this '
                             'condition. Leukotriene modifiers are useful rather than harmful here because '
                             'the disease involves leukotriene overproduction. Biologics and surgery when '
                             'indicated are also part of the long-term plan. Pearl: AERD is a chronic '
                             'inflammatory airway disease, not just a drug allergy label.',
              'domain': 'Rhinology / Allergy / Skull Base',
              'topic': 'Aspirin-exacerbated respiratory disease'},
 'allergy8': {'question': 'A patient has itching and sneezing around cats and in spring, congestion without '
                          'itch from perfume and cold air, and has used a topical decongestant spray daily '
                          'for 3 months with worse congestion as each dose wears off. Skin testing is '
                          'positive only to cat and tree pollen. Which step should come first for the '
                          'rebound congestion?',
              'choices': ['Begin subcutaneous immunotherapy to cat and tree pollen extracts',
                          'Stop the topical decongestant, using an intranasal steroid to bridge',
                          'Add an oral antihistamine and continue the decongestant spray as needed',
                          'Refer for inferior turbinate reduction to relieve the fixed congestion'],
              'answer': 1,
              'explanation': 'Congestion that rebounds as each dose of a topical decongestant wears off is '
                             'rhinitis medicamentosa, and the first step is stopping the spray, usually with '
                             'an intranasal corticosteroid to ease withdrawal. Immunotherapy targets the '
                             'allergic itch-and-sneeze triggers but will not fix rebound from the spray, and '
                             'the irritant triggers are nonallergic. Pearl: sort symptoms by trigger, '
                             'because one patient can have allergic, nonallergic, and medicamentosa '
                             'components at once.',
              'domain': 'Rhinology / Allergy / Skull Base',
              'topic': 'Rhinitis phenotypes by trigger'},
 'psg-normal-primary-snoring': {'question': 'A 7-year-old with nightly snoring has an attended polysomnogram '
                                            'with good signal quality: total sleep time 420 minutes, AHI '
                                            '0.8/h, obstructive AHI 0.5/h, central apnea index 0.3/h, SpO2 '
                                            'nadir 94%, and no sustained CO2 elevation. What is the best '
                                            'interpretation?',
                                'choices': ['Mild obstructive sleep apnea, because the AHI is above zero',
                                            'No significant sleep apnea on this night, consistent with '
                                            'primary snoring',
                                            'Central sleep apnea, because central apneas were scored during '
                                            'the study',
                                            'Moderate obstructive sleep apnea, because snoring was present '
                                            'every night'],
                                'answer': 1,
                                'explanation': 'In children an AHI below 1/h is normal, and with a normal '
                                               'oxygen nadir and no hypercapnia this study does not show '
                                               'obstructive or central sleep apnea; snoring without abnormal '
                                               'indices fits primary snoring. Pediatric mild OSA begins at '
                                               'an AHI of 1/h, and a central index of 0.3/h with no '
                                               'gas-exchange effect is within normal limits. Pearl: snoring '
                                               'is a symptom, not a PSG diagnosis, so confirm sleep time, '
                                               'REM, position, and signal quality before signing out a '
                                               'normal study.',
                                'domain': 'Sleep Surgery',
                                'topic': 'Normal pediatric PSG and primary snoring'},
 'psg-pediatric-obstructive': {'question': 'A healthy 6-year-old with snoring, witnessed pauses, and 3+ '
                                           'tonsils has a PSG showing AHI 11.4/h, obstructive AHI 10.8/h, '
                                           'central apnea index 0.6/h, SpO2 nadir 86%, and REM-predominant '
                                           'events in which airflow stops while chest and abdominal effort '
                                           'continue. What is the most appropriate interpretation and plan?',
                               'choices': ['Mild OSA; watchful waiting with a repeat PSG in 6 months',
                                           'Moderate OSA; adenotonsillectomy as a same-day outpatient',
                                           'Central sleep apnea; brain MRI before any airway surgery',
                                           'Severe OSA; adenotonsillectomy with overnight inpatient '
                                           'monitoring'],
                               'answer': 3,
                               'explanation': 'Absent airflow with continued effort defines obstructive '
                                              'events, and a pediatric AHI of 10/h or more is severe. The '
                                              'AAO-HNS 2019 tonsillectomy guideline recommends overnight '
                                              'inpatient monitoring after tonsillectomy for children younger '
                                              'than 3 years or with severe OSA (AHI 10/h or more, SpO2 nadir '
                                              'below 80%, or both), so routine same-day discharge is not '
                                              'appropriate. Pearl: use pediatric cut-offs of 1, 5, and 10 '
                                              'per hour, and report the obstructive index, oxygenation, CO2, '
                                              'and REM or position dependence, not just the total AHI.',
                               'domain': 'Sleep Surgery',
                               'topic': 'Pediatric OSA severity and postoperative monitoring'},
 'psg-central-apnea': {'question': 'A 10-year-old is referred for witnessed breathing pauses without '
                                   'prominent snoring. PSG: total sleep time 390 minutes, AHI 7.2/h, '
                                   'obstructive AHI 0.9/h, central apnea index 6.3/h, SpO2 nadir 89%. During '
                                   'events, airflow and thoracoabdominal effort are both absent. What is the '
                                   'most appropriate next step?',
                       'choices': ['Evaluate for causes of central apnea, including neurologic imaging and a '
                                   'medication review',
                                   'Proceed with adenotonsillectomy, because the total AHI places him in the '
                                   'moderate range',
                                   'Start a trial of intranasal steroid and montelukast, then repeat the PSG '
                                   'in 3 months',
                                   'Reassure the family that central events are normal in children and need '
                                   'no further workup'],
                       'answer': 0,
                       'explanation': 'When airflow and effort disappear together, the events are central, '
                                      'and here central apneas make up nearly all of the respiratory burden. '
                                      'This calls for a central differential, such as brainstem or Chiari '
                                      'malformation, medications, cardiopulmonary disease, or a congenital '
                                      'ventilatory disorder, usually with sleep medicine involvement, rather '
                                      'than surgery for obstruction. Occasional brief central pauses can be '
                                      'normal in children, but a central index this high, with desaturation, '
                                      'is not. Pearl: effort during the airflow pause separates obstructive '
                                      'from central events.',
                       'domain': 'Sleep Surgery',
                       'topic': 'Central apnea on pediatric PSG'},
 'psg-mixed-apnea': {'question': 'In an 8-year-old with complex sleep-disordered breathing, one apnea shows '
                                 'airflow absent throughout. In the first part of the event there is no '
                                 'chest or abdominal effort; effort then resumes while airflow remains '
                                 'absent, and SpO2 falls from 92% to 87%. How should this event be '
                                 'classified?',
                     'choices': ['Central apnea, because the event begins with no respiratory effort',
                                 'Obstructive apnea, because effort is present before airflow returns',
                                 'Mixed apnea, because it has an absent-effort and a resumed-effort phase',
                                 'Obstructive hypopnea, because the event causes a 3% or more desaturation'],
                     'answer': 2,
                     'explanation': 'An apnea that starts without inspiratory effort and then continues with '
                                    'effort against an absent airflow is a mixed apnea, containing both a '
                                    'central and an obstructive component. Calling it central reads only the '
                                    'beginning, and calling it obstructive reads only the end. It is not a '
                                    'hypopnea because airflow is absent rather than reduced. Pearl: classify '
                                    'events by following airflow and effort across the whole event, and do '
                                    'not assume that many mixed events mean a primary central disorder.',
                     'domain': 'Sleep Surgery',
                     'topic': 'Mixed apnea classification'},
 'psg-severe-pediatric-osa-gas-exchange': {'question': 'A 4-year-old with loud snoring, retractions, and '
                                                       'restless sleep has a PSG showing obstructive AHI '
                                                       '28.6/h and central apnea index 0.4/h, with REM '
                                                       'clustering and partial obstruction between discrete '
                                                       'apneas. Which additional finding most increases the '
                                                       'concern for postoperative respiratory compromise '
                                                       'after adenotonsillectomy?',
                                           'choices': ['A total sleep time of 410 minutes with normal sleep '
                                                       'efficiency',
                                                       'A low central apnea index of 0.4 events per hour',
                                                       'A history of restless sleep reported by the parents',
                                                       'An SpO2 nadir of 74% with sustained CO2 elevation'],
                                           'answer': 3,
                                           'explanation': 'The AHI counts how often events occur, but deep '
                                                          'desaturation and sustained hypercapnia show the '
                                                          'physiologic cost of obstruction, including '
                                                          'hypoventilation from prolonged partial '
                                                          'obstruction, and they predict respiratory '
                                                          'problems after surgery. An SpO2 nadir below 80% '
                                                          'alone meets the AAO-HNS threshold for severe OSA '
                                                          'that calls for overnight inpatient monitoring. A '
                                                          'low central index and adequate sleep time make '
                                                          'the study reliable but do not add risk. Pearl: '
                                                          'always report the oxygen nadir and CO2 pattern '
                                                          'alongside the AHI in a preoperative read.',
                                           'domain': 'Sleep Surgery',
                                           'topic': 'Gas exchange and perioperative risk in pediatric OSA'},
 'psg-rem-positional-osa': {'question': 'A 15-year-old with intermittent symptoms has a PSG showing overall '
                                        'obstructive AHI 6.1/h, REM obstructive AHI 18.4/h, NREM 2.2/h, '
                                        'supine 14.0/h, nonsupine 1.8/h, and central apnea index 0.5/h. '
                                        'Before relying on the REM and supine indices, what should you check '
                                        'first?',
                            'choices': ['Whether the arousal index is higher in REM than in NREM sleep',
                                        'How many minutes of REM sleep and supine sleep were recorded',
                                        'Whether the central apnea index rises during REM sleep',
                                        'Whether the patient slept longer on the lab night than at home'],
                            'answer': 1,
                            'explanation': 'Obstruction here is concentrated in REM and supine sleep, so the '
                                           'overall index averages vulnerable and protected periods together '
                                           'and can understate the worst physiology. Subgroup indices are '
                                           'only reliable when enough REM and supine time was sampled, '
                                           'because a few minutes can make those numbers unstable. A night '
                                           'with little REM or supine sleep may also underestimate disease, '
                                           'which should be stated as a limitation. Pearl: always ask when '
                                           'events occur and how much time was spent in each stage and '
                                           'position, not just how many events occurred.',
                            'domain': 'Sleep Surgery',
                            'topic': 'REM and positional OSA and sampling adequacy'},
 'psg-central-events-not-csa': {'question': 'A 5-year-old with adenotonsillar hypertrophy and classic '
                                            'obstructive symptoms has a PSG showing AHI 14.2/h, obstructive '
                                            'AHI 12.9/h, central apnea index 1.3/h, and SpO2 nadir 84% '
                                            'during obstructive clusters. The central events are scattered '
                                            'and mostly occur near arousals or sleep transitions. What is '
                                            'the best interpretation?',
                                'choices': ['Central sleep apnea; obtain a brain MRI before any airway '
                                            'surgery',
                                            'Obstructive sleep apnea, with the central events noted but not '
                                            'driving care',
                                            'Mixed sleep apnea syndrome; begin PAP and avoid '
                                            'adenotonsillectomy',
                                            'An indeterminate study; repeat the PSG before making any '
                                            'decision'],
                                'answer': 1,
                                'explanation': 'The obstructive burden dominates, and the gas-exchange '
                                               'disturbance occurs with obstructive clusters, so this is '
                                               'severe obstructive sleep apnea with a few incidental central '
                                               'events. Scattered centrals near arousals or sleep-stage '
                                               'transitions are common in children and do not define central '
                                               'sleep apnea, so delaying airway treatment for a central '
                                               'workup is not justified. A much higher central burden, '
                                               'central events with desaturation, periodic breathing, or '
                                               'persistent centrals after treatment would raise concern. '
                                               'Pearl: report obstructive and central indices separately so '
                                               'the dominant physiology guides treatment.',
                                'domain': 'Sleep Surgery',
                                'topic': 'Incidental central events in obstructive OSA'},
 'psg-systematic-read': {'question': 'A 12-year-old with obesity has persistent snoring 1 year after '
                                     'adenotonsillectomy. PSG has adequate REM and supine sleep and shows '
                                     'AHI 16.8/h, obstructive AHI 15.9/h, central apnea index 0.9/h, SpO2 '
                                     'nadir 82%, intermittent CO2 elevation without sustained '
                                     'hypoventilation, and events worse in REM and supine sleep. What is the '
                                     'most appropriate next step?',
                         'choices': ['Evaluate for a central ventilatory disorder with brain MRI and a '
                                     'neurology referral',
                                     'Reassure the family and repeat the PSG in 1 year, since surgery has '
                                     'already been done',
                                     'Treat persistent OSA with PAP and weight management, and look for '
                                     'residual obstruction sites',
                                     'Treat with intranasal steroids alone, since adenoid regrowth is the '
                                     'most likely cause'],
                         'answer': 2,
                         'explanation': 'The study shows severe residual obstructive sleep apnea, not '
                                        'central apnea, so the next steps are PAP, weight management, and a '
                                        'targeted search for residual sites such as nasal obstruction, '
                                        'adenoid regrowth, lingual tonsils, or tongue-base collapse, '
                                        'sometimes with drug-induced sleep endoscopy. A central workup is '
                                        'not supported by a central index of 0.9/h, and observation leaves '
                                        'severe disease untreated. Pearl: read in a fixed order (quality, '
                                        'architecture, event type, separate indices, gas exchange, '
                                        'clustering, then clinical context) so the headline AHI does not '
                                        'become the diagnosis.',
                         'domain': 'Sleep Surgery',
                         'topic': 'Persistent OSA after adenotonsillectomy'}}

CASE_FIXES = {'vestnew2': {'study_summary': [['Right AC=BC 250-1k', '40, 35, 30 dB HL'],
                                ['Left AC=BC 250-1k', '10, 10, 10 dB HL'],
                                ['Right 2k-8k', '15, 15, 10 dB HL'],
                                ['Calorics', '~30% right weakness'],
                                ['ECoG', 'Elevated SP/AP ratio; supportive only']]},
 'v12': {'prompt': 'Positional testing produces persistent, non-fatiguing, direction-changing nystagmus with '
                   'no latency that does not fit the plane of any single canal. What changes?'},
 'aud2': {'study_summary': [['Right AC', '45, 50, 45, 40, 35, 30 dB HL'],
                            ['Right BC', '5, 5, 10, 10, 10 dB HL'],
                            ['Right air-bone gap', '~25-45 dB'],
                            ['Left AC=BC', '10 dB HL'],
                            ['Tympanometry', 'Type B normal volume right; Type A left'],
                            ['WRS', '96% right; 100% left']]},
 'aud3': {'study_summary': [['Right AC (250-8k)',
                             '10, 15, 20, 35, 55, 65 dB HL; BC equals AC where tested (to 4 kHz)'],
                            ['Left AC (250-8k)',
                             '10, 15, 20, 35, 55, 60 dB HL; BC equals AC where tested (to 4 kHz)'],
                            ['SRT/WRS', '20 dB HL; 88% bilateral'],
                            ['Tympanometry', 'Type A bilateral']]},
 'audio-v126-stenger-functional': {'reason_answer': 'A positive Stenger (no response when the louder tone is '
                                                    'in the reportedly deaf ear) means the patient hears the '
                                                    'tone in the better ear but suppresses responses, which '
                                                    'supports a functional or nonorganic component. It does '
                                                    'not establish intent or cause. Recheck behavioral '
                                                    'consistency and use objective measures (OAEs, ABR) to '
                                                    'estimate true thresholds.'},
 'allergy3': {'study_summary': [['Timothy grass IgE', '12.5 kUA/L'],
                                ['Ragweed', '0.9 kUA/L'],
                                ['Dust mite', '3.2 kUA/L'],
                                ['Symptoms', 'Late spring/early summer only'],
                                ['Interpretation',
                                 'Sensitization magnitude does not equal clinical allergy; correlate '
                                 'exposure and symptoms']],
              'follow': 'What matters most when symptoms occur only in late spring and early summer?',
              'follow_answer': 'The allergen whose season matches the symptoms (here grass pollen) is the '
                               'clinically meaningful one; mite and ragweed sensitization without matching '
                               'symptoms is likely not.'},
 'psg-normal-primary-snoring': {'reason_answer': 'Every index is normal for a child: AHI and obstructive AHI '
                                                 'under 1/h, a normal oxygen nadir and no hypoventilation. '
                                                 'Snoring without apnea or gas-exchange problems is primary '
                                                 'snoring. Management is driven by symptoms and examination, '
                                                 'not by this study.'},
 'psg-central-apnea': {'reason_answer': 'In central events, airflow and inspiratory effort stop together, so '
                                        'there is no drive to breathe; in obstructive events, effort '
                                        'continues against a closed airway. A central apnea index of 6.3/h '
                                        'with desaturation is abnormal in a 10-year-old and calls for a '
                                        'search for a cause (brainstem or Chiari imaging, medications, '
                                        'cardiopulmonary and neuromuscular disease), not '
                                        'adenotonsillectomy.'},
 'ct_sliceviewer_v44': {'follow_answer': 'Name the cause: an atypical variant (such as an asymmetric jugular '
                                         'vein), a transition level (hyoid, cricoid or thoracic inlet), or a '
                                         'structure you only know from one level. Then re-scroll that '
                                         'segment slowly until you can follow the structure above and '
                                         'below.'},
 'ae1': {'follow_answer': 'Debris in the canal, middle-ear effusion or negative pressure can abolish OAEs, '
                          'and electrical artifact or a large cochlear microphonic can be mistaken for '
                          'neural waves. Check tympanometry, reverse polarity to separate microphonic from '
                          'neural response, and repeat a poor-quality recording.'},
 'ae2': {'follow_answer': 'A single trace can reflect noise or artifact. Replicate waveforms to confirm that '
                          'peaks and latencies are reproducible before calling a delay abnormal.'},
 'ae3': {'follow_answer': 'Tympanometry (1 kHz in young infants), OAEs, bone-conduction ABR when a '
                          'conductive component is possible, and later behavioral confirmation with visual '
                          'reinforcement audiometry.'},
 'ae4': {'follow_answer': 'Tympanometry with ear-canal volume, plus otoscopy. Effusion can abolish OAEs, so '
                          'absent OAEs with a flat tympanogram do not localize the loss until the middle ear '
                          'clears or ABR (including bone conduction) is done.'},
 'ae6': {'follow_answer': 'Absolute values vary between patients and setups; a sustained change from the '
                          "patient's own baseline (such as a latency shift of 1 ms or more, or an amplitude "
                          'drop of 50 percent or more) is more meaningful than any single reading.'},
 'ae7': {'follow_answer': 'The 1-3-6 benchmarks: screening by 1 month, diagnosis by 3 months and '
                          'intervention by 6 months. Early access to sound supports language development, '
                          'and delays harm outcomes.'},
 'ae8': {'follow_answer': 'Agreement between behavioral, OAE and ABR findings with normal cochlear nerves '
                          'supports a cochlear loss, so hearing aids and, if benefit is limited, cochlear '
                          'implant evaluation are appropriate.'}}
