# labs_v532/sinus_fungal.py: added 2026-11-01 after viewing each image in Chrome. License and legend confirmed on the PMC page.
LAB = None
TARGET_LAB = 'sinus-ct'
CASES = [
    {
        "id": "sx_black_turbinate_v545",
        "level": 4,
        "concept_id": "sinus:invasive-fungal-mri",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/f56e/8894831/228825a0ce5a/43055_2022_735_Fig1_HTML.jpg",
        "image_credit": "Aggarwal A, Raj N, Bhardwaj K, et al. Egypt J Radiol Nucl Med. 2022;53:60 (CC BY 4.0) — Fig. 1",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8894831/",
        "prompt": "A 60-year-old man who had COVID-19 a month ago (treated with steroids) has nasal discharge and headache. These are contrast-enhanced axial (a) and coronal (b) T1-weighted MRI. Look at the right turbinates (arrows).",
        "answer": "The right middle (arrowhead) and inferior (arrow) turbinates do not enhance, while the surrounding mucosa does: the 'black turbinate' sign. Loss of enhancement means devitalized, ischemic tissue from angioinvasive fungal infection, here mucormycosis.",
        "why": "Mucorales invade blood vessels, causing thrombosis and infarction. Non-enhancing mucosa on MRI can precede bony erosion on CT, so MRI catches early invasive disease. The risk groups are uncontrolled diabetes (especially ketoacidosis), steroid exposure, neutropenia and transplant.",
        "reason_prompt": "What is the next step once you suspect this?",
        "reason_answer": "Urgent endoscopy with biopsy of pale, insensate or black mucosa (frozen section showing broad, ribbon-like, non-septate hyphae), immediate liposomal amphotericin B, prompt surgical debridement back to bleeding tissue, and reversal of the underlying risk (glucose control, stopping steroids where possible). Delay worsens survival.",
        "teach_prompt": "Teach a junior why a normal-looking CT does not exclude invasive fungal sinusitis.",
        "teach_answer": "CT shows bone erosion and fat stranding late; early disease may only thicken the mucosa. Contrast MRI shows the non-enhancing devitalized mucosa and spread into the orbit, pterygopalatine fossa or brain earlier. In a high-risk patient, endoscopy and biopsy should not wait for imaging.",
        "follow": "Which hyphae shape separates Mucorales from Aspergillus on histology?",
        "follow_answer": "Mucorales: broad, ribbon-like, pauci-septate hyphae with right-angle branching. Aspergillus: narrow, septate hyphae with acute-angle (about 45 degree) branching.",
        "mcq": {
            "question": "A diabetic patient recently treated with steroids has nasal discharge and facial pain. Contrast MRI shows the right middle and inferior turbinates fail to enhance, as here. What is the most appropriate next step?",
            "choices": [
                "A 3-week course of oral antibiotics and nasal steroids, then reassess",
                "Urgent nasal endoscopy with biopsy, systemic liposomal amphotericin B and surgical debridement",
                "Allergy testing and immunotherapy",
                "Repeat MRI in 6 weeks"
            ],
            "answer": 1,
            "explanation": "Non-enhancing ('black') turbinates in a high-risk host indicate devitalized tissue from angioinvasive fungal sinusitis such as mucormycosis. This is an emergency: endoscopic biopsy for diagnosis, immediate amphotericin B, urgent debridement and correction of the underlying risk factors.",
            "domain": "Rhinology / Allergy / Skull Base",
            "topic": "Acute invasive fungal sinusitis MRI"
        },
        "verify_note": "PMC8894831: CC BY 4.0 link on the article page; Fig. 1 legend '...Contrast-enhanced axial (a) and coronal T1 W (b) images showing non enhancing right middle (arrowhead) and inferior turbinates (arrow) indicative of \"Black turbinate sign\"'. Image viewed in Chrome.",
        "variant_type": "interpret"
    },
    {
        "id": "sx_retroantral_fat_v545",
        "level": 4,
        "concept_id": "sinus:invasive-fungal-ct",
        "image_url": "https://cdn.ncbi.nlm.nih.gov/pmc/blobs/f56e/8894831/998777e8a528/43055_2022_735_Fig2_HTML.jpg",
        "image_credit": "Aggarwal A, Raj N, Bhardwaj K, et al. Egypt J Radiol Nucl Med. 2022;53:60 (CC BY 4.0) — Fig. 2",
        "image_source": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8894831/",
        "prompt": "A 35-year-old recovering from moderate COVID-19 has left facial pain and sinus symptoms. Axial CT (a, b). Compare the fat behind the left maxillary sinus with the right side.",
        "answer": "The left maxillary sinus is opacified, its posterior wall is eroded (arrow), and the retroantral fat behind it is obliterated, whereas the right retroantral fat is preserved. Loss of the retroantral fat plane signals spread of infection beyond the sinus toward the pterygopalatine and infratemporal fossae, which is consistent with invasive fungal sinusitis.",
        "why": "Retroantral (and preantral) fat stranding is an early CT sign of invasion. It can appear before obvious bone destruction, because angioinvasive fungi spread along vessels through intact-looking bone.",
        "reason_prompt": "Which spaces does disease reach next from here, and what clinical signs suggest it?",
        "reason_answer": "Through the pterygopalatine fossa to the infratemporal fossa, orbit (through the inferior orbital fissure) and cavernous sinus. Watch for cheek numbness (V2), loss of vision, ophthalmoplegia, proptosis, trismus and palatal discoloration.",
        "teach_prompt": "Teach a junior the three fat planes to check on every sinus CT in an immunocompromised patient.",
        "teach_answer": "Retroantral (behind the maxillary sinus), preantral (in front of the maxilla, in the cheek) and orbital fat. Stranding or loss of any of them suggests spread beyond the sinus and needs urgent endoscopy.",
        "follow": "What does palatal ulceration or black eschar suggest about the extent of disease?",
        "follow_answer": "Spread to the palate through the maxilla or greater palatine vessels, meaning advanced invasive disease that usually needs wide debridement, sometimes including a maxillectomy.",
        "mcq": {
            "question": "An immunocompromised patient has left maxillary sinus opacification on CT with erosion of the posterior wall and loss of the fat behind the sinus, while the right side is normal. What does the loss of this fat plane most strongly suggest?",
            "choices": [
                "Simple acute bacterial sinusitis",
                "Spread of invasive fungal infection beyond the sinus",
                "Allergic fungal rhinosinusitis",
                "A normal anatomic variant"
            ],
            "answer": 1,
            "explanation": "Obliteration of the retroantral fat with posterior wall erosion indicates spread beyond the sinus toward the pterygopalatine and infratemporal fossae, a hallmark of invasive fungal sinusitis in a high-risk host. Bacterial sinusitis and allergic fungal sinusitis stay within the sinus; allergic fungal disease expands and thins bone rather than infiltrating the fat.",
            "domain": "Rhinology / Allergy / Skull Base",
            "topic": "Invasive fungal sinusitis CT"
        },
        "verify_note": "PMC8894831: CC BY 4.0 link on the article page; Fig. 2 legend 'Axial CT images (a, b) showing left maxillary sinusitis with the erosion of the posterior wall of the left maxillary sinus (orange arrow) and obliterating the retroantral fat, consistent with invasive fungal sinusitis'. Image viewed in Chrome.",
        "variant_type": "interpret"
    }
]
