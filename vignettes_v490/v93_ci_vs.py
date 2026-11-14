"""v93: middle-ear fluid found during cochlear implantation; speech discrimination as the predictor
of long-term hearing in observed vestibular schwannoma."""

CI = "v6-otology-neurotology-cochlear-implant-surgery"
VS = "v6-otology-neurotology-vestibular-schwannoma"

VIGNETTES = [
    {
        "topic": "Cochlear Implant Surgery",
        "concept_id": CI,
        "stem": "A 2-year-old with profound bilateral sensorineural hearing loss is undergoing cochlear implantation. Preoperative otoscopy two weeks ago was normal. When the facial recess is opened, the middle ear contains thin, clear, nonpurulent fluid; the mucosa is not inflamed and the child has had no fever. What is the best management?",
        "choices": [
            "Abort the case, place a tympanostomy tube, and implant in 2 to 3 months",
            "Proceed with implantation after irrigating the middle ear with saline, with topical antibiotic drops and a course of postoperative antibiotics",
            "Close without implanting and repeat the operation only after the effusion has cleared on otoscopy",
            "Implant and place a tympanostomy tube in the same ear to ventilate the middle ear",
        ],
        "answer": 1,
        "explanation": "A sterile serous effusion found at surgery does not prevent cochlear implantation. The middle ear is irrigated with saline before the cochleostomy or round window is opened, and topical and postoperative antibiotics are given to treat the potentially contaminated field. Series of children implanted with an effusion show more intraoperative difficulty (edematous mucosa, bleeding, poorer view) but no increase in postoperative complications, and delaying implantation in a young child costs auditory development.",
        "why_wrong": [
            "Aborting is the answer for purulent acute otitis media, not for a clear, uninfected effusion; an unnecessary delay worsens language outcomes.",
            "Correct.",
            "Waiting for the effusion to clear delays hearing in a critical language window and is not needed when the fluid is not infected.",
            "Most surgeons avoid placing a new tube at the time of implantation, because an open drum exposes the middle ear around the fresh electrode to the ear canal; it does not address the decision in front of you.",
        ],
        "board_pearl": "Clear, uninfected effusion at cochlear implantation: irrigate and proceed. Purulent acute otitis media: abort, place a tube, implant later.",
        "curveball": "What if the middle ear held thick, purulent fluid with red, swollen mucosa?",
        "curveball_answer": "That is acute otitis media. Do not open the cochlea, because the cochleostomy or round window opening would let bacteria into the inner ear and risk labyrinthitis and meningitis. Culture the fluid, place a tympanostomy tube, treat the infection, and implant once the ear has been free of infection for at least about 2 weeks.",
        "learning_stage": "application",
        "focus": "management",
    },
    {
        "topic": "Cochlear Implant Surgery",
        "concept_id": CI,
        "stem": "A 3-year-old is scheduled for cochlear implantation next week. Today she has ear pain and fever, and the tympanic membrane on the side to be implanted is red and bulging. What is the best plan?",
        "choices": [
            "Proceed as scheduled with perioperative intravenous antibiotics",
            "Treat the acute otitis media and postpone implantation until the ear has been free of infection, placing a tympanostomy tube if infections recur",
            "Switch the implant to the other ear on the same day without examining it",
            "Cancel implantation permanently, since recurrent otitis media is a contraindication",
        ],
        "answer": 1,
        "explanation": "Active acute otitis media is a contraindication to cochlear implantation, because the opening into the cochlea gives middle ear bacteria a route to the inner ear and meninges. The infection is treated first and the operation rescheduled once the ear is quiet, generally after at least about 2 weeks free of infection. Children with recurrent otitis media or persistent effusion are often given tympanostomy tubes first, and implanted once the ear is dry and stable.",
        "why_wrong": [
            "Antibiotics do not make it safe to open the cochlea through an infected middle ear.",
            "Correct.",
            "Changing sides without examining that ear ignores the reason for choosing the original side and does not address a possibly infected ear.",
            "Recurrent otitis media delays implantation but does not rule it out; it is managed with treatment and tubes, then implantation.",
        ],
        "board_pearl": "Active acute otitis media: treat first and implant once the ear has been infection-free for at least about 2 weeks; recurrent otitis media is controlled with tubes, not a reason to refuse implantation.",
        "curveball": "Why must children with cochlear implants be vaccinated against pneumococcus?",
        "curveball_answer": "Implant recipients have a higher risk of bacterial meningitis, mostly from Streptococcus pneumoniae, which can spread from the middle ear along the electrode. CDC recommends age-appropriate pneumococcal vaccination for all implant candidates and recipients, ideally completed at least 2 weeks before surgery.",
        "learning_stage": "foundation",
        "focus": "management",
    },
    {
        "topic": "Vestibular Schwannoma",
        "concept_id": VS,
        "stem": "A 52-year-old has a 7-mm intracanalicular vestibular schwannoma found during workup for mild right tinnitus. The right pure-tone average is 25 dB and word recognition is 100%. He chooses observation with serial MRI. Which finding at diagnosis best predicts that he will keep serviceable hearing over the next decade?",
        "choices": [
            "The tumor is confined to the internal auditory canal",
            "His age at diagnosis",
            "His 100% word recognition (speech discrimination) score",
            "The small tumor size",
        ],
        "answer": 2,
        "explanation": "In large wait-and-scan series, word recognition at diagnosis is the strongest predictor of long-term hearing. In the Danish cohort, 69% of patients with 100% speech discrimination at diagnosis kept good hearing after more than 10 years of observation, compared with only 38% of those with even a small loss of discrimination at diagnosis. Tumor location, size and patient age have not consistently predicted hearing outcome.",
        "why_wrong": [
            "An intracanalicular location was once thought to worsen hearing by compressing the nerve in a closed space, but large studies have not confirmed it as an independent predictor.",
            "Age has not been a strong predictor of long-term serviceable hearing.",
            "Correct.",
            "Size has not consistently predicted hearing outcome, and hearing can decline even in small tumors that do not grow.",
        ],
        "board_pearl": "In observed vestibular schwannoma, speech discrimination at diagnosis is the best predictor of long-term serviceable hearing: 100% is favorable, while even a small loss predicts much worse hearing over time.",
        "curveball": "During observation his tumor does not grow, but his word recognition falls from 100% to 80% over 3 years. What does this tell you?",
        "curveball_answer": "Hearing can deteriorate without tumor growth, so serial audiograms are needed along with MRI. A falling word recognition score worsens the outlook for hearing and may change the discussion: patients who value hearing preservation may consider earlier treatment (middle fossa or retrosigmoid hearing-preservation surgery for small tumors, or radiosurgery) while hearing is still serviceable.",
        "learning_stage": "mastery",
        "focus": "counseling",
    },
    {
        "topic": "Vestibular Schwannoma",
        "concept_id": VS,
        "stem": "Two patients have small vestibular schwannomas and choose observation. Patient A has a pure-tone average of 30 dB and 100% word recognition. Patient B has a pure-tone average of 30 dB and 88% word recognition. How do their long-term hearing outlooks compare?",
        "choices": [
            "They are the same, because their pure-tone averages are equal",
            "Patient B is more likely to keep serviceable hearing, because some loss has already occurred",
            "Patient A is considerably more likely to keep good hearing over a decade of observation",
            "Neither is likely to keep serviceable hearing beyond 2 years",
        ],
        "answer": 2,
        "explanation": "Speech discrimination at diagnosis predicts long-term hearing better than the pure-tone average. Patients with 100% discrimination usually keep good hearing for many years under observation, whereas those with even a small loss of discrimination at diagnosis lose good hearing much more often. This difference is useful when counseling about observation versus early hearing-preservation treatment.",
        "why_wrong": [
            "Equal pure-tone averages do not mean equal prognosis; discrimination is the stronger predictor.",
            "A loss of discrimination already present predicts further decline, not stability.",
            "Correct.",
            "Most patients with 100% discrimination keep good hearing well beyond 2 years of observation.",
        ],
        "board_pearl": "Two vestibular schwannoma patients with the same pure tones but different word recognition do not share a prognosis: the one with 100% word recognition is far more likely to keep good hearing.",
        "curveball": "Which hearing classification uses only the word recognition score?",
        "curveball_answer": "The word recognition score classification proposed by Gurgel and colleagues in 2012 (classes I to IV) grades hearing on word recognition alone, whereas the AAO-HNS classes A to D combine pure-tone average and word recognition. Many recent observation studies report both.",
        "learning_stage": "application",
        "focus": "counseling",
    },
]
