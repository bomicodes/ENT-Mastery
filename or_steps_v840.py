"""v84.0: richer operative steps for the otology and neurotology OR cards.

Each card's operative sequence is rewritten, in our own words, from Robert K. Jackler's Stanford
online atlases (Otologic Surgery Atlas, otosurgeryatlas.stanford.edu; Skull Base Surgery Atlas,
skullbasesurgeryatlas.stanford.edu, illustrations by Christine Gralapp). Where an atlas page could
not be opened, standard technique fills the gap. Steps are (title, detail) pairs; the plain `steps`
list is kept in sync as "Title. detail" so search, audits and older templates still work.
"""

SOURCE_LABEL_V840 = "Jackler, Stanford Otologic & Skull Base Surgery Atlases"

STEPS_V840 = {'canalplasty': [['Indication and approach',
                  'Exostoses are usually multiple, broad-based, and medial, near the drum; an osteoma is '
                  'single and pedunculated, sits more laterally, and often comes out transcanal. Operate '
                  'when the canal is nearly closed, debris and wax keep getting trapped with conductive '
                  'loss, or infection keeps coming back. Use a postauricular approach unless the canal is '
                  'wide enough to work through.'],
                 ['Postauricular exposure',
                  'Incise in or slightly behind the crease, find the linea temporalis under retractor '
                  'tension with the blade angled upward, and raise a periosteal flap toward the canal. Free '
                  'meatal skin from the bony meatus before opening the canal-spanning self-retainer to avoid '
                  'tearing it.'],
                 ['Design incisions to save skin',
                  'The overriding principle is maximal skin conservation. Plan canal incisions so skin can '
                  'be draped back. When raising a posterior canal flap, cut vertical limbs medial-to-lateral '
                  'at about 45 degrees, toward yourself, with needle cautery for the dermis, and thin the '
                  'flap.'],
                 ['Retrograde skin elevation',
                  'Peel the canal skin off the exostoses, working from lateral to medial, and keep it as '
                  'flaps that you will lay back at the end. The skin is thinnest and most easily torn over '
                  'the domes of the lesions, so slow down there and use a round knife rather than suction to '
                  'lift it.'],
                 ['Protect the elevated skin',
                  'Shield the skin flap while drilling — some surgeons lay a thin silicone sheet over it, '
                  'and a fenestrated suction can hold it out of the way.'],
                 ['Anterior and superior lesions first',
                  'Take down the anterior and superior exostoses first. This opens a view of the drum early, '
                  'so every later cut is made with the annulus in sight. Drilling without seeing the drum '
                  'leads to off-axis troughs, which is how the facial nerve is injured posteriorly and the '
                  'temporomandibular joint is entered anteriorly.'],
                 ['Hollow out each lesion',
                  'Core each exostosis from the inside, starting with a cutting burr for bulk and changing '
                  'to a diamond as you near skin, drum, or the facial nerve. Leave a thin eggshell of bone '
                  'against the skin. Keep the shaft of the spinning burr off the elevated skin, which can '
                  'wind onto it and tear.'],
                 ['Curette the rim',
                  'Remove the thin remaining shell with a curette rather than the drill, peeling it off the '
                  'medial meatal skin; this preserves canal skin and keeps the burr off the drum and '
                  'annulus.'],
                 ['Posteroinferior lesion last',
                  'Leave the posteroinferior exostosis until the posterior annulus is clearly seen. Here the '
                  'mastoid segment of the facial nerve can lie lateral to the plane of the annulus, so '
                  'drilling straight back is dangerous. Thin this lesion with a diamond under heavy '
                  'irrigation, keep the drum in view, and curette the final shell.'],
                 ['Anterior bulge',
                  'When an anterior bony bulge hides the anterior drum, raise the anterior canal skin as a '
                  'flap, retract it, and drill the bulge down in stages with a diamond. Bone just inside the '
                  'anterosuperior canal is tightly stuck to skin; free it sharply first. The '
                  'temporomandibular joint lies directly in front, so stop if soft tissue or joint capsule '
                  'appears.'],
                 ['Extent of canalplasty',
                  'Widen until the whole drum and annulus can be seen in one microscope view and the '
                  'narrowest point of the canal is at the annulus, not lateral to it. Smooth all ledges '
                  'where debris could collect. Do not thin the anterior wall so far that the '
                  'temporomandibular joint is exposed.'],
                 ['Final check',
                  'Before packing, look at the whole drum for tears or a burr injury and repair any '
                  'perforation with a small underlay graft. Confirm the annulus is intact all the way around '
                  'and that bleeding has stopped. If facial nerve monitoring was used, check for any '
                  'responses during posterior drilling and note them.'],
                 ['Replace the skin',
                  'Lay the preserved skin flaps back over the drilled bone. Small patches of bare bone heal '
                  'well on their own; a ring of bare bone around the whole canal is what causes stenosis, so '
                  'make sure skin covers at least part of every wall. A split-thickness skin graft is rarely '
                  'needed.'],
                 ['Pack and close',
                  'Pack the canal with gelatin sponge or a lubricated wick, firmly enough to hold the skin '
                  'flaps against bone but not so tight that it pushes on the drum. Close the postauricular '
                  'wound in layers and place an anti-lop-ear suture to the antihelical fold, which matters '
                  'most in children.']],
 'cochlear-implant': [['Setup and safety',
                       'Set up facial nerve monitoring and ask anesthesia to avoid long-acting paralytics. '
                       'Confirm pneumococcal vaccination is up to date. '
                       'Have the correct device and a backup in the room. Use monopolar cautery only before '
                       'the implant is opened; once it is in the field, use bipolar only.'],
                      ['Plan device position',
                       'Mark the receiver-stimulator so a behind-the-ear processor will sit comfortably '
                       'beside the auricle — roughly 3–4 cm behind the canal, angled about 45 degrees above '
                       "the linea temporalis — using the manufacturer's template. Minimal hair shave is fine "
                       'if drapes seal well.'],
                      ['Incision',
                       'Use a modified postauricular incision that can be carried up into the '
                       'supra-auricular hairline when more room is needed for the well and fixation. Keep at '
                       'least 1.5 cm between the incision line and the device edge to lower extrusion risk.'],
                      ['Periosteal flap',
                       'Raise the skin flap, then cut a separate, anteriorly based periosteal flap over the '
                       'mastoid, extended back along the linea temporalis. Later it closes over the mastoid '
                       'and device so the incision does not sit directly on the implant. In small children '
                       'the tissue is thin, so raise skin and periosteum carefully to avoid holes.'],
                      ['Subperiosteal pocket and flap thickness',
                       'Make a snug pocket under the periosteum, sized with the device template, and mark '
                       'the well site through it. A tight pocket is the first defense against migration. '
                       "Check scalp thickness over the magnet; thin it to the manufacturer's maximum if "
                       'needed, but do not thin it so much that the skin breaks down.'],
                      ['Mastoidectomy without saucerization',
                       'Do a cortical mastoidectomy, but do not saucerize the edges as in chronic ear '
                       'surgery. Leave bony overhangs at the posterior, superior, and inferior margins so '
                       'the lead can be tucked under them. Identify the tegmen, sigmoid sinus, lateral '
                       'semicircular canal, and short process of the incus.'],
                      ['Facial recess',
                       'Open the facial recess, the triangle between the facial nerve medially, the chorda '
                       'tympani laterally, and the incus buttress above. Use a diamond with plenty of '
                       'irrigation, leave thin bone over the nerve, and keep the chorda when possible. '
                       'Drilling too far laterally hits the annulus. Extend low enough to see the round '
                       'window niche.'],
                      ['Drill the well and lead trough',
                       'Drill a well that fits the electronics case snugly, checking position and depth '
                       'repeatedly with templates. In thin calvaria or children, dura may be reached (use a '
                       'diamond); a mobile island of bone can be pushed medially to let the case seat. Cut a '
                       'trough from the well to the mastoid for the lead, using the preserved overhangs.'],
                      ['Expose the round window landmark',
                       'Drill the superior lip of the round window niche to bring the anterior edge of the '
                       'membrane into view — this edge orients the cochleostomy.'],
                      ['Open the cochlea',
                       'Choose round-window insertion, an extended round window, or a cochleostomy just '
                       'anterior and inferior to the window. For a cochleostomy, use a small diamond aimed '
                       'slightly upward into scala tympani, away from the basilar membrane. Control '
                       'bleeding, wash out bone dust, and open the membrane or endosteum last. Never suction '
                       'directly over the opening.'],
                      ['Harvest sealing tissue and seat the device',
                       'Take a small piece of temporalis fascia or muscle for sealing, from a spot that does '
                       'not weaken the flap needed for closure. Seat the receiver in its well and, if you '
                       'use fixation, tie it down with nonabsorbable suture through bone tunnels or to small '
                       'screws. Keep knots off the outer surface. Bipolar cautery only from here on.'],
                      ['Insert the electrode',
                       "Follow the manufacturer's technique for the specific array. Insert slowly and "
                       'steadily toward the depth marker. If you feel resistance, stop; do not force it, '
                       'because that causes tip fold-over, scalar shift, or a basilar membrane tear. For '
                       'precurved arrays, advance off the stylet while holding the stylet still. Note the '
                       'final depth.'],
                      ['Seal cochleostomy and facial recess',
                       'Pack the harvested muscle/fascia around the array at the cochleostomy, tucking edges '
                       'between array and bone with a straight pick — careful sealing guards against '
                       'middle-ear infection tracking into the inner ear and subarachnoid space. Fill the '
                       'facial recess with larger tissue pieces to stabilize the lead.'],
                      ['Test, inspect, and close',
                       'Run impedances and neural response telemetry; get an X-ray or other imaging if '
                       'position is in doubt. Check the facial nerve, chorda, and hemostasis. Coil spare '
                       'lead under the bony overhangs, close the periosteal flap over the mastoid, then '
                       'close skin in layers. Apply a light dressing without hard pressure over the '
                       'magnet.']],
 'jugular-foramen-tumor': [['Workup, embolization, and monitoring',
                            'Check plasma or urine metanephrines; a secreting paraganglioma needs '
                            'alpha-blockade before surgery. Embolize paragangliomas one to three days before '
                            'surgery. If the carotid is encased, get balloon occlusion testing. Document '
                            'lower cranial nerve function, swallowing, and hearing. Monitor VII and the '
                            'lower nerves: tongue, palate, vocal folds by EMG tube, and trapezius for XI.'],
                           ['Choose the corridor',
                            'Match the approach to tumor extent. A transmastoid-neck approach with a '
                            'fallopian bridge covers the bulb, hypotympanum, and neck. Add a transjugular '
                            'craniotomy for intracranial extension. Infratemporal fossa type A, with ear '
                            'canal closure and anterior facial nerve rerouting, gives the widest carotid '
                            'access. Before any sinus or jugular sacrifice, confirm good venous drainage on '
                            'the other side.'],
                           ['Incision',
                            'Use a curved incision from behind the ear down into an upper neck skin crease; '
                            'it can be extended forward or toward the midline if needed. The greater '
                            'auricular nerve usually has to be divided to join the fields. Tag a good length '
                            'of it and keep it moist in case the facial nerve needs a cable graft.'],
                           ['Neck control',
                            "Loop the IJV and ICA (don't put traction on the ICA). Retract SCM backward and "
                            'digastric/styloid muscles forward. Moving toward the skull base, ligate '
                            'ascending pharyngeal, occipital, and other ECA feeders. Find and protect IX–XI '
                            '(and XII nearby) as they leave the foramen.'],
                           ['Canal flap and mastoidectomy',
                            'Raise a tympanomeatal flap with lower-than-usual canal incisions to expose the '
                            'hypotympanum. Do a full mastoidectomy, open the antrum widely, and skeletonize '
                            'the sigmoid. Follow the digastric ridge forward to the stylomastoid foramen and '
                            'identify the nerve there before you detach and remove the mastoid tip from the '
                            'digastric muscle.'],
                           ['Skeletonize the descending facial nerve',
                            'Use cutting, then diamond burrs, to thin bone over the mastoid segment of the '
                            'facial nerve down to the stylomastoid foramen. The upper limit of drilling is '
                            'the posterior semicircular canal; in a poorly pneumatized bone, find that '
                            'semicircular canal first. Remove hypotympanic bone in front of the nerve to '
                            'show the dome of the jugular bulb.'],
                           ['Fallopian bridge rather than rerouting',
                            'Leave the facial nerve in a thin bony bridge and drill under it, joining the '
                            'window in front of the nerve to the window behind it. If there is little room '
                            'in front, work only from behind. Reroute the nerve only for extensive carotid '
                            'involvement; rerouting usually leaves at least temporary facial weakness.'],
                           ['Control the sigmoid sinus',
                            'Expose the lower sigmoid and 1 to 2 cm of dura behind it. Leave a bony shelf '
                            'above if the tumor is only extracranial; open fully if it goes intracranial. '
                            'Occlude the sinus by packing oxidized cellulose between bone and sinus wall, '
                            'not with a blind suture that can tear cerebellar veins. Cover the packing so '
                            'the drill cannot catch it.'],
                           ['Ligate the internal jugular vein late',
                            'Tie the internal jugular vein in the neck only when you are ready to remove the '
                            'tumor. Tied too early, venous outflow from the tumor is blocked while inflow '
                            'continues, so the tumor swells and bleeds more. Tie it above the facial vein '
                            'and keep the accessory nerve in view.'],
                           ['Open sinus and bulb',
                            'Open the sigmoid sinus and jugular vein lengthwise along their lateral walls. '
                            'Remove the remaining bone over the bulb from behind the facial nerve, angling '
                            'the microscope backward, so the upper and lower exposures join. With good '
                            'exposure the facial nerve can stay in its canal.'],
                           ['Remove tumor',
                            'Tumor usually invades the dome and medial wall of the bulb with intra- and '
                            'extraluminal parts; intraluminal tumor generally lifts free of intima. Take the '
                            'hypotympanic part (cup forceps, laser, or delivering it into the hypotympanum) '
                            '— often last. Tumor may extend into the transverse sinus. With intracranial '
                            'extension (transjugular craniotomy), remove the extracranial part first so the '
                            'intracranial part is relatively avascular; doing it first invites torrential '
                            'bleeding.'],
                           ['Inferior petrosal sinus bleeding',
                            'When you clear the medial wall of the bulb, the inferior petrosal sinus bleeds '
                            'back from several openings. Lay a pack firmly over them rather than stuffing it '
                            'into the openings, and keep bipolar to a minimum, because IX, X, and XI lie '
                            'just under this wall. If no back-bleeding appears, suspect residual tumor '
                            'blocking the sinus.'],
                           ['Carotid and lower cranial nerves',
                            'Most tumors peel off the carotid; where the plane is unclear, leave a '
                            'cauterized cuff on the artery and use Doppler when tumor hides it. The lower '
                            'cranial nerves lie on the medial wall of the bulb. If they still work, leave '
                            'adherent tumor on them and plan imaging surveillance or radiation for the '
                            'remnant.'],
                           ['Check for a medial remnant',
                            'A smooth medial surface can hide residual tumor, a common cause of recurrence. '
                            'Compare what you see with the preoperative MRI, and treat absent inferior '
                            'petrosal sinus back-bleeding as a warning sign. Inspect the medial wall '
                            'carefully before closing.'],
                           ['Close and plan aftercare',
                            'Wax open air cells, close the Eustachian tube if the ear canal was closed, '
                            'repair dura watertight, and fill the defect with fat or a muscle flap. Document '
                            'VII and IX to XII function. Keep patients nil by mouth until a swallow study; '
                            'acute vagal palsy may need early vocal fold medialization. Watch blood pressure '
                            'in secreting tumors.']],
 'mastoidectomy': [['Set up and decide the plan',
                    'Use facial nerve monitoring. Review the CT for tegmen height, sigmoid position, a '
                    'dehiscent facial nerve, and a lateral semicircular canal fistula. Decide whether you '
                    'expect canal-wall-up or canal-wall-down surgery, but be ready to convert. Steps marked '
                    'CWU or CWD below apply only to that path.'],
                   ['Postauricular incision and periosteal flap',
                    'Incise in, or 5 to 10 mm behind, the postauricular crease. In children under about two, '
                    'keep the lower end short because the facial nerve exits superficially. Cut the '
                    'periosteum along the linea temporalis and down to the tip, elevate it forward to the '
                    'canal, free the muscle attachments, and place self-retaining retractors.'],
                   ['Canal flap for cholesteatoma',
                    'Elevate posterior canal skin from the spine of Henle toward the drum, cutting adhesions '
                    'at the suture lines sharply. For cholesteatoma, make only the superior canal incision, '
                    'carried into the retraction pocket, so the tympanomeatal flap is based inferiorly. Then '
                    'cut around the neck of the sac so it stays with the disease, not the flap.'],
                   ['CWD: take down the scutum early',
                    'In canal-wall-down cases, remove the scutum early with a diamond and a curette rotated '
                    'outward, so you see the oval window and learn right away whether the chain is intact. '
                    'An intact chain means the rest of the attic must be worked gently to avoid incus '
                    'dislocation. In real cases the incus and stapes are often eroded.'],
                   ['Cortical mastoidectomy and antrum',
                    'Use the largest cutting burr that fits, with suction-irrigation. Outline the tegmen '
                    "above, sigmoid behind, and posterior canal wall in front, then deepen through Macewen's "
                    'triangle to the antrum. Find the lateral semicircular canal and short process of the '
                    "incus. Thin bone parallel to the nerve's expected course, and use the digastric ridge "
                    'to predict it.'],
                   ['Know where the nerve is at risk',
                    'Posterior attic and posterior mesotympanic disease threatens the tympanic segment just '
                    'above the stapes. Anterior attic disease threatens the upper tympanic segment and '
                    'geniculate ganglion. Matrix often drapes over the nerve above the oval window, where '
                    'the bony canal is frequently dehiscent. Never peel matrix there blindly; use '
                    'stimulation and a gentle plane.'],
                   ['Always look anterior to the malleus head',
                    'Because anterior epitympanic extension is possible, every cholesteatoma operation '
                    'should include exposure anterior to the malleus head rather than assuming disease stops '
                    'at the incus.'],
                   ['CWU: open the facial recess',
                    'In canal-wall-up surgery, open the facial recess between the facial nerve and chorda '
                    'tympani, below the incus buttress. Drill with a diamond and heavy irrigation, as heat '
                    'injures the nerve, and leave thin bone on it. Staying too lateral damages the annulus. '
                    'The opening shows the stapes, pyramidal eminence, and round window niche.'],
                   ['Incus absent: remove the buttress',
                    'When the incus is gone, drill away the remaining incus buttress so mastoid and middle '
                    'ear become one open space; this lowers the risk of aditus block and trapped disease.'],
                   ['CWD: take down the canal wall',
                    'Begin removing the posterior canal wall and finish with a rongeur; remove the bony '
                    'bridge over the epitympanum, switching from drill to curette for its last remnant — '
                    'especially if the chain is intact — to bring the sac into view. Then remove the '
                    'anterior and posterior buttresses.'],
                   ['CWD: lower the facial ridge',
                    'The facial ridge, the base of the old canal wall, covers the mastoid segment of the '
                    'facial nerve. Lower it until it is nearly level with the floor of the canal and middle '
                    'ear, leaving a protective layer of bone over the nerve. A high ridge traps debris; '
                    'drilling flush to the nerve leaves a narrow cavity and a bare nerve.'],
                   ['CWD: optional tip removal',
                    'In a very large, pneumatized mastoid, removing the tip lets soft tissue fill in and '
                    'shrinks the cavity. Find the digastric ridge first: the facial nerve leaves the skull '
                    'at its anterior end, so detach the tip working posteriorly and laterally, away from the '
                    'stylomastoid foramen.'],
                   ['Check the hidden recesses',
                    'The sinus tympani, facial recess, anterior epitympanum, and hypotympanum are classic '
                    'sites of residual disease. Look into each with a 30- or 45-degree endoscope before '
                    'closing. Keep landmarks in view while drilling; a lost surgeon most often injures a '
                    'normal facial nerve at the second genu or in the mastoid segment.'],
                   ['Remove matrix and handle a fistula',
                    'Remove the matrix in one piece where you can, working from the mastoid toward the '
                    'middle ear and sweeping toward the facial nerve, not away from it. If matrix covers a '
                    'lateral semicircular canal fistula, leave that part for last, lift it under irrigation, '
                    'and cover the fistula immediately, or leave it and stage.'],
                   ['Choose the reconstruction type',
                    'Most canal-wall-down cases get a modified radical cavity, with the middle ear rebuilt '
                    'using fascia and cartilage. A radical cavity, middle ear left open, is for matrix stuck '
                    'to the tympanic segment of the facial nerve or footplate, or extending into the '
                    'Eustachian tube. A Bondy procedure suits attic disease lateral to the ossicles with '
                    'good hearing.'],
                   ['Decide on staging',
                    'Plan a second look at 9 to 12 months, or non-echo-planar diffusion MRI surveillance, '
                    'when matrix was fragmented, left on the stapes or a fistula, or the canal wall was kept '
                    'up. Write down exactly where any matrix was left. Silicone sheeting in the middle ear '
                    'helps keep space for a staged reconstruction.'],
                   ['Rebuild hearing',
                    'In a canal-wall-down ear the middle ear is shallow, so a rotated incus or cartilage '
                    'alone often bridges the gap. Never lay the drum or fascia directly on the stapes head; '
                    'put a thin cartilage disc between them. If the middle ear mucosa is poor or disease was '
                    'left behind, plan to stage the reconstruction instead.'],
                   ['CWD: meatoplasty and closure',
                    'Make the meatoplasty big enough that you can see and clean the whole cavity in clinic; '
                    'remove conchal cartilage as needed and keep enough skin to line it. Pack the cavity and '
                    'canal with gelatin sponge and an antibiotic-coated wick. Close the postauricular wound '
                    'in layers and apply a mastoid dressing.']],
 'middle-fossa-skull-base': [['Setup',
                              'Patient supine with the head turned away; surgeon at the head of the table. A '
                              'pinned holder is optional. Place facial EMG needles in orbicularis oris and '
                              'oculi, and add ABR or direct VIII nerve recording for hearing preservation. '
                              'Ask anesthesia for brain relaxation: mannitol, mild hyperventilation, and a '
                              'lumbar drain if you use one.'],
                             ['Incision and temporalis',
                              'Use an inferiorly based U-flap or a vertical incision curving forward, with a '
                              'narrow shave. Lift temporalis muscle with the skin flap as one layer so its '
                              'nerve and blood supply stay intact. Splitting the muscle in an inverted T '
                              'denervates part of it and leads to trismus and a hollow temple.'],
                             ['Orientation from above',
                              'Identify the external auditory canal from above — it lies roughly in the same '
                              'plane as the IAC and anchors orientation for the craniotomy.'],
                             ['Craniotomy',
                              'Make a craniotomy about 4 by 5 cm, centered slightly in front of the ear '
                              'canal, with its lower edge at the floor of the middle fossa just above the '
                              'zygomatic root. Cut the inferior limb with a drill rather than a craniotome '
                              'to avoid tearing thin dura, and lower the bottom edge without twisting, which '
                              'can crack the ear canal roof.'],
                             ['Extradural elevation, posterior to anterior',
                              'Lift dura off the floor from the back toward the front. Working forward from '
                              'the arcuate eminence keeps you from lifting the GSPN and avulsing it, which '
                              'can drag on a geniculate ganglion with no bone over it. Free dura sharply '
                              'where it sticks along the petrosquamous suture, and pack venous bleeding near '
                              'the posterior edge.'],
                             ['Floor landmarks',
                              'Arcuate eminence (variable, sometimes absent — a flat floor); GSPN anteriorly '
                              "(cut it sharply free if it clings to dura, don't avulse); geniculate "
                              'ganglion, whose bony cover may be missing — elevate gently. Foramen spinosum '
                              'veins bleed and chasing them can open the MMA: bipolar plus bone wax into the '
                              'foramen; a large Surgicel pack under Telfa, removed at the end.'],
                             ['Retractor placement',
                              'Seat a rigid middle fossa retractor with its tip on the petrous ridge, in the '
                              'groove of the superior petrosal sinus. Malleable blades will not hold the '
                              'temporal lobe. Position the arm so it does not block the drill, and release '
                              'it periodically during long cases.'],
                             ['Locate the IAC: choose a strategy',
                              'House: follow the GSPN back to the geniculate ganglion, then the labyrinthine '
                              'segment to the fundus; this risks the geniculate and the cochlea. Fisch: '
                              'blue-line the superior semicircular canal; the IAC lies about 60 degrees '
                              'forward of it. Medial-first: drill near the porus, where there is no inner '
                              'ear, then follow the canal laterally.'],
                             ['Skeletonize medial to lateral',
                              'Once found medially, unroof the IAC toward the fundus. Near the porus you can '
                              'expose most of the circumference; laterally, narrow the exposure to the top '
                              'of the canal because the cochlea lies anteriorly and the superior '
                              "semicircular canal ampulla lies posteriorly. At the fundus, find Bill's bar; "
                              'the facial nerve lies in front of it.'],
                             ['Open IAC dura and orient',
                              'Open IAC dura along its posterior edge, away from the facial nerve, which '
                              'lies in front and often directly on top of the tumor in this view. Confirm '
                              'the nerve with the stimulator before cutting anything. Expect blind spots: '
                              'the inferior compartment sits behind the transverse crest, and the '
                              'labyrinthine segment hides part of the anterior fundus.'],
                             ['Tumor removal',
                              'Debulk to make room, but develop the tumor–facial nerve interface first, '
                              'before removing tumor from under the nerve. A tumor that separates easily is '
                              'rotated beneath the nerve and delivered without displacing it; an adherent '
                              'one must be rotated to present the interface for sharp dissection, raising '
                              'neurapraxia risk. Then free the capsule from the cochlear nerve, preserving '
                              'VII and the cochlear nerve.'],
                             ['Extension to the CPA (selected cases)',
                              'For CPA extension under ~1.5 cm, remove additional bone in front of and '
                              'behind the porus, elevating the superior petrosal sinus from its groove at '
                              'the apex. Up to ~2 cm: divide the SPS (bipolar, clips if needed) and cut the '
                              'tentorial edge a few millimeters to see the upper pons and V/VII/VIII root '
                              'entry zones. Inferior exposure stays limited — not for larger tumors.'],
                             ['Seal and obliterate',
                              'Press bone wax into every opened air-cell tract with a blunt instrument or '
                              'cottonoid. Fill the IAC defect with a small piece of abdominal fat taken '
                              'through a 2 to 3 cm incision; muscle is an alternative.'],
                             ['Rebuild the tympanic roof if opened',
                              'If the epitympanic roof was widely opened, lay a bone sheet (thin lower flap '
                              'edge or a saw-split piece) to keep dura from sagging onto the ossicles and '
                              'causing conductive loss.'],
                             ['Other uses of this exposure',
                              'The same exposure is used for superior semicircular canal dehiscence: find '
                              'the dehiscent arcuate eminence, then plug or resurface it with fascia and '
                              'bone without opening the membranous labyrinth. It is also used to decompress '
                              'the labyrinthine segment and geniculate ganglion of the facial nerve, and to '
                              'repair tegmen defects.'],
                             ['Replace the flap and assess',
                              'Check dura for tears and hemostasis and let the temporal lobe re-expand. Fix '
                              'the bone flap with plates, pushed against two edges to help it fuse. Close in '
                              'layers. After waking, document facial function, hearing, balance, and any '
                              'speech or neurologic change; temporal lobe retraction can cause aphasia or '
                              'seizures.']],
 'ossiculoplasty': [['Exposure',
                     'Raise a tympanomeatal flap (inject at the bony-cartilaginous junction, crush-then-cut '
                     'the incision, divide the vascular strip with scissors), enter the middle ear '
                     'inferiorly first to stay away from the ossicles, and keep bone contact while lifting '
                     "the annulus so the flap and drum don't tear."],
                    ['Classify the deficiency',
                     'Describe the defect. The Austin groups are: A, malleus and stapes present; B, malleus '
                     'present, stapes arch absent; C, malleus absent, stapes present; D, both absent. Also '
                     'note incudostapedial separation, an eroded incus long process, and malleus or stapes '
                     'fixation from tympanosclerosis or otosclerosis. The pattern decides the '
                     'reconstruction.'],
                    ['Expose the stapes fully if needed',
                     'If the scutum hides the stapes, thin it with a diamond and finish with a curette '
                     'rotated outward; pushing inward can dislocate the incus. Stop when the facial nerve '
                     'and stapedial tendon are visible. Then check that the stapes and footplate move, using '
                     'the round window reflex.'],
                    ['Harvest the incus for an autograft',
                     'Gently separate and remove a nonfunctional incus. Look at it under the microscope: '
                     'reuse it only if it is free of disease. In cholesteatoma, many surgeons avoid reusing '
                     'the incus because matrix can hide on it; use cartilage or a prosthesis instead.'],
                    ['Clear the path or stage',
                     'Remove adhesions, granulation, and any cholesteatoma between the drum and stapes '
                     'before measuring. If the mucosa is badly diseased, the Eustachian tube works poorly, '
                     'or disease may remain, place silicone sheeting and rebuild hearing at a second stage.'],
                    ['Sculpt the incus',
                     'Hold the incus firmly in an ossicle holder and shape it with a small diamond under '
                     'cool irrigation. Remove the long process, drill a shallow cup in the body to sit on '
                     'the stapes head, and cut a notch for the malleus handle so the graft locks between the '
                     'two.'],
                    ['Rotated incus mainly for canal-wall-down ears',
                     'A rotated incus works best after canal-wall-down surgery, where the middle ear is '
                     'shallow. In a normal-depth middle ear the distance from stapes head to drum is usually '
                     'too great for it to reach without a sculpted or prosthetic option.'],
                    ['Malleus-head option and its weakness',
                     'Another option is to cut the malleus head off at the neck, drill a cup in it, and seat '
                     'it on the stapes head. It tends to be top-heavy and can tip over, so stabilize it '
                     'well. Avoid reusing the malleus head when cholesteatoma involved the attic, because '
                     'matrix can remain on it.'],
                    ['Cartilage-only reconstruction in a shallow (CWD) ear',
                     "Where the middle ear is narrow after CWD, cartilage alone may suffice. Don't lay the "
                     'drum or graft directly on the capitulum — poor contact gives a high failure rate; '
                     'interpose a cartilage sheet. For gaps of several millimeters, stack cartilage, leaving '
                     'perichondrium on so the layers hold together.'],
                    ['Cartilage cap for prostheses',
                     'Harvest tragal cartilage (Brown-Adson forceps, not toothed Adsons), separate '
                     'perichondrium with a stapes knife, and bevel the surface facing the drum. The disc can '
                     'cover an ossicular prosthesis or repair an epitympanic defect.'],
                    ['Place a prosthesis',
                     'Use a partial prosthesis on a mobile stapes head, or a total one on the footplate when '
                     'the arch is gone. Measure with the drum in its natural position. Seat it under the '
                     'malleus handle if possible, cover the head with cartilage, and keep it clear of the '
                     'promontory, facial canal, and canal wall. Steady it with gelatin sponge.'],
                    ['Test and return the flap',
                     'Press gently on the malleus or graft and watch the round window reflex to confirm '
                     'sound reaches the inner ear. Lay the tympanomeatal flap back and check that the '
                     'prosthesis is still in place under the drum. Pack lightly with gelatin sponge so it is '
                     'supported but not pushed out of position.']],
 'retrosigmoid-skull-base': [['Position and monitoring',
                              'Supine with a shoulder roll on the operated side, or lateral, with the head '
                              'in pins and turned away. Avoid twisting the neck so far that jugular drainage '
                              'is blocked. Monitor the facial nerve and, when relevant, V and the lower '
                              'cranial nerves; add ABR or direct VIII nerve recording for hearing '
                              'preservation.'],
                             ['Incision',
                              'Make a curved incision a few centimeters behind the mastoid, placed forward '
                              'so you cut less neck muscle and are less likely to injure the occipital '
                              'nerve. Expose the bone behind the mastoid. If you are not using fat, a piece '
                              'of neck muscle can be saved to plug the IAC defect later.'],
                             ['Craniotomy against the sinuses',
                              'The transverse-sigmoid junction lies under the asterion. Make burr holes '
                              'there and along the back edge of the sigmoid sinus, and open bone right up to '
                              'both sinuses; this gives a view of the angle with much less cerebellar '
                              'retraction. Save bone chips for cranioplasty and wax the mastoid emissary '
                              'vein and any opened air cells.'],
                             ['Dural opening',
                              "Incise dura about 5 mm inside the bony edge so there's a cuff for suture "
                              'closure; add relaxing cuts to make small flaps and tack them up — these flaps '
                              'also give purchase at closure.'],
                             ['Release CSF before retracting',
                              'Before any real retraction, gently lift the lower cerebellum and open the '
                              'arachnoid over the cisterna magna to drain CSF. Retracting a tense cerebellum '
                              'first can cause severe swelling that makes the operation unsafe. Wait until '
                              'the cerebellum falls away.'],
                             ['Retraction and veins',
                              'Apply a malleable blade on an Apfelbaum-type arm over Telfa to the lateral '
                              "cerebellum, lifting the lateral lobe and flocculus off the tumor's posterior "
                              "surface. The petrosal (Dandy's) vein complex tethers the superior cerebellum: "
                              'preserve it in small tumors where possible; bipolar and divide it in large '
                              'ones.'],
                             ['Debulk the CPA component first (large tumors)',
                              'Stimulate the back of the capsule to make sure the facial nerve is not there, '
                              'open a window, and core the tumor with an ultrasonic aspirator, keeping the '
                              'capsule intact. At the lower pole, protect the AICA branch and the '
                              'glossopharyngeal and vagus nerves under cottonoids.'],
                             ['Prepare the posterior IAC wall',
                              'Find the porus (palpate with a ball hook if hidden). Cut and elevate anterior '
                              'and posterior dural flaps over the canal with a #11 blade and stapes knife, '
                              'and free dura from the inferolateral endolymphatic sac. Pack Gelfoam into the '
                              'posterior fossa to catch bone dust.'],
                             ['Drill the canal: inner ear limit',
                              'Drill the posterior wall of the IAC with a coarse diamond, staying medial to '
                              'where the endolymphatic duct enters bone; beyond that lie the posterior '
                              'semicircular canal and vestibule. Usually the medial two thirds of the IAC '
                              'can be opened safely; check the MRI for how far the tumor goes. Wax opened '
                              'air cells as you go.'],
                             ['Find VII at the brainstem',
                              'Find the root entry zones of VII and VIII at the brainstem, just above the '
                              'flocculus and the choroid plexus at the foramen of Luschka; an AICA loop '
                              'often runs between them. VII lies in front of VIII, so it is usually reached '
                              'from below. Confirm it with the stimulator before dissecting tumor off the '
                              'pons.'],
                             ['Intracanalicular tumor and fundus',
                              'Stimulate the posterior canal wall/dura to exclude VII, dissect the '
                              'tumor–facial nerve interface with angled instruments. If tumor fills the '
                              'lateral fundus, direct vision requires opening part of the inner ear; blind '
                              'angled-instrument removal risks a vascular remnant. Endoscopic fundal '
                              'inspection is an option, but bloodied vestibular nerve stumps can mimic '
                              'tumor.'],
                             ['Adherent tumor at the porus lip',
                              'The nerve bends sharply over the anterior porus lip — usually the stickiest '
                              'zone. Cut arachnoid bands sharply, develop the plane from both medial and '
                              'lateral ends, and accept near-total removal (thin and cauterize the remnant) '
                              'rather than risk the nerve.'],
                             ['Seal air cells',
                              'Feel along the drilled petrous bone with a blunt hook for opened air cells '
                              'and seal each one with bone wax. Unsealed cells let CSF reach the middle ear '
                              'and leak out the nose through the Eustachian tube. Leak rates of up to about '
                              '15% are reported with this approach, so be meticulous.'],
                             ['Fill the defect and close dura',
                              'Plug the petrous defect with abdominal fat (preferred — fat-suppressed MRI '
                              'distinguishes recurrence) or a nuchal muscle plug, held with a stay suture '
                              'through the dural flaps. Close dura as completely as possible, often '
                              'watertight.'],
                             ['Cranioplasty and layered closure',
                              'Restore the bony defect — replaced bone chips often fuse solidly in 4–8 '
                              'weeks, or plate/wire a flap — to reduce persistent postoperative headache; '
                              'close soft tissue in multiple secure layers against CSF leak.'],
                             ['Postoperative checks',
                              'Document facial function, hearing, and lower cranial nerve function, '
                              'including swallow and voice, as soon as the patient wakes. Watch for clear '
                              'rhinorrhea or wound leak, headache, and cerebellar signs. Get an early CT if '
                              'consciousness drops, to look for hemorrhage or hydrocephalus.']],
 'stapedotomy': [['Setup and hand position',
                  'Steady the speculum with the third and fourth fingers of both hands (holder optional); '
                  'microinstrument in the right hand, suction in the left. Inject lidocaine-epinephrine '
                  'circumferentially at the bony-cartilaginous junction, using less anteriorly (transient '
                  'facial palsy risk), and avoid the bony canal except a bleb under the vascular strip with '
                  'a 27-gauge needle, bevel to bone.'],
                 ['Tympanomeatal flap incision',
                  'Cut a posteriorly based flap about 6 to 7 mm lateral to the annulus, running from just '
                  'above the short process of the malleus down to the floor of the canal. Make the superior '
                  'limb longer so the flap will cover the bone you remove from the scutum. Score the line '
                  'with a round knife first, then complete it.'],
                 ['Enter the middle ear inferiorly',
                  'Elevate to the annulus with suction kept above the knife. Enter inferiorly first to keep '
                  'away from the ossicles, lifting the annulus from its groove with steady downward-inward '
                  'pressure on bone; losing bone contact tears flap or drum. Lyse mucosa with a curved '
                  'needle and promptly suction any lidocaine from the round window niche.'],
                 ['Free the flap superiorly and find the chorda',
                  'Lift the annulus superiorly with a curved needle until it clears the notch of Rivinus so '
                  'the flap folds over the manubrium and rests on the umbo, exposing the incus long process. '
                  'Identify and free the chorda. If the flap sags, look for clot beneath it; a '
                  'gelatin-epinephrine cube controls inferior-edge bleeding.'],
                 ['Remove the scutum',
                  'Thin it with a ~2.3 mm diamond and finish the shell with a curette (diamond is slower but '
                  'kinder to chorda, flap, drum). Brace the curette on the speculum and rotate it outward, '
                  'away from the incus — never push inward, since a sudden release can dislocate the incus. '
                  'End-point: entire facial nerve visible above and the tendon-pyramid junction visible '
                  'behind.'],
                 ['Finish the exposure',
                  'A bony bump where the chorda enters often hides the back of the footplate; reduce it with '
                  'a 1 mm diamond and curette. Cut the mucosal folds between incus and malleus and over the '
                  'footplate. Make room in front of the incus for the prosthesis, and confirm you can see '
                  'the footplate from above, behind, and below.'],
                 ['Confirm fixation and decide',
                  'Touch the stapes lightly; heavy pressure can loosen a barely fixed footplate. Push the '
                  'malleus gently outward to check the lateral chain, which is fixed in about 1 in 200 '
                  'cases. Look for a facial nerve hanging over the oval window, a persistent stapedial '
                  'artery, or a thick obliterated footplate, and change plan if the footplate cannot be '
                  'safely opened.'],
                 ['Measure before disrupting the stapes',
                  'Measure from the lateral surface of the incus to the footplate, targeting the '
                  'center-to-posterior third; about 4.5 mm in most patients. Use a feather-light touch to '
                  'avoid perforating a thin footplate.'],
                 ['Separate the incudostapedial joint',
                  'Identify it by slight outward pressure on the incus, then divide it with an anterior '
                  '"worming" motion that lifts the incus outward; avoid pushing the stapes head down and '
                  'avoid side-to-side motion, which can fracture the footplate transversely.'],
                 ['Divide tendon and down-fracture the arch',
                  'Cut the stapedial tendon with microscissors angled posteriorly (shaft resting on the '
                  'anterior speculum) to spare the posterior crus. Fracture the superstructure briskly '
                  'toward the promontory, away from the nerve, using a curved needle on both crura with more '
                  'force on the anterior one; a slow push can mobilize the footplate. Confirm the footplate '
                  'is still intact and fixed.'],
                 ['Hemostasis on the oval window',
                  'Lay an epinephrine-soaked gelatin sponge on the oval window for about a minute to blanch '
                  'vessels before opening the footplate.'],
                 ['Make the fenestra',
                  'Use a diamond burr slightly larger than the piston, such as 0.7 mm for a 0.6 mm piston; '
                  'never a cutting burr. Ask the room to be still and quiet. Get the burr to full speed over '
                  "the posterior central footplate, touch just to the burr's widest point, and withdraw. "
                  'Some surgeons make the fenestra before removing the arch.'],
                 ['Laser alternative',
                  'With a laser, overlap small spots in a rosette over the posterior footplate. For KTP or '
                  'argon lasers, a drop of blood on the white footplate helps it absorb energy. Remove the '
                  'char, irrigate with cool saline, and use the lowest power that works; repeated high-power '
                  'shots can heat the inner ear or facial nerve.'],
                 ['Gusher or floating footplate',
                  'If perilymph gushes, raise the head, wait for flow to slow, and plug the fenestra with '
                  'tissue before placing the piston; consider a lumbar drain. If the whole footplate comes '
                  'loose, do not try to remove it through a small hole; stop, or place a tissue graft and '
                  'prosthesis, and accept a higher risk of hearing loss.'],
                 ['Insert and crimp the prosthesis',
                  "Carry it with smooth alligator forceps, engage the shepherd's crook on the incus long "
                  'process (missing the incus allows the piston to plunge too deep), position with a notched '
                  'strut guide. Brace the crimper on the speculum, align exactly with the wire, hold the '
                  'back tine still while closing the front tine. Leave slight play — a hermetic crimp risks '
                  'incus necrosis.'],
                 ['Test and seal',
                  'Move the malleus once or twice and check that the piston rides freely in the fenestra. If '
                  'it lifts out, replace it with one 0.25 mm longer. Seal around the piston with a little '
                  'tissue from the vascular strip or a blood patch. Never suction over the open vestibule; '
                  'use a 24-gauge tip at low suction beside it.'],
                 ['Return the flap and check',
                  'Lay the tympanomeatal flap back over the scutum defect and support it with a few pieces '
                  'of gelatin sponge, without packing against the prosthesis. If the patient is awake, ask '
                  'about vertigo and test hearing with a tuning fork. Check facial movement before leaving '
                  'the room.']],
 'tegmen-repair': [['Confirm and map the defect',
                    'Spontaneous leaks, linked to obesity, sleep apnea, and raised intracranial pressure, '
                    'are now the most common cause; trauma and prior mastoid surgery are others. Confirm CSF '
                    'with beta-2 transferrin. Use thin-slice temporal bone CT to find every defect, as '
                    'multiple defects are common, and MRI when brain may have herniated. Look for empty '
                    'sella or papilledema.'],
                   ['Choose the approach',
                    'Use transmastoid repair for small defects over the mastoid or easily reached tegmen. '
                    'Use a middle fossa craniotomy for large, multiple, or anterior tegmen tympani defects '
                    'and most encephaloceles, especially when hearing and the ossicles must be protected. '
                    'Combine the two when neither alone gives a reliable seal.'],
                   ['Position and incision for middle fossa',
                    'Supine with the head turned away and the surgeon at the head of the table. Use a '
                    'U-shaped flap or a vertical incision curving forward. Raise temporalis with the skin '
                    'flap as one layer, so the muscle keeps its nerve and blood supply and does not cause '
                    'trismus or a hollow temple.'],
                   ['Small temporal craniotomy',
                    'Center it slightly in front of the ear canal (the canal is a useful planar landmark '
                    'from above) and bevel posteriorly to limit mastoid air-cell entry. Cut the inferior '
                    'limb with a drill rather than a craniotome to spare thin dura; take the lower rim down '
                    'to the floor with rongeur or drill without torquing (EAC roof fracture risk).'],
                   ['Extradural elevation to the defect',
                    'Lift dura from back to front along the petrous face, freeing it sharply where it sticks '
                    'at the suture lines. Find the neck of the herniation and look across the whole floor '
                    'for more defects. Protect the arcuate eminence, the GSPN, a geniculate that may lack '
                    'bone, and the middle meningeal artery.'],
                   ['Handle the herniated brain',
                    'If the herniated tissue looks healthy and comes back easily, reduce it into the middle '
                    'fossa. If it is gliotic, necrotic, or stuck, coagulate its stalk with bipolar and cut '
                    'it flush with the floor. Close any dural tear directly or with a fascia graft.'],
                   ['Size-matched reconstruction',
                    'Narrow bony defects: soft-tissue graft alone. Wider defects: bone graft plus a '
                    'connective-tissue sheet. Large dural defects: add an intradural fascia graft — the '
                    "brain's own weight seats it against surrounding dura."],
                   ['Multilayer closure for larger defects',
                    'Commonly combine intradural and/or extradural fascia, a rotated temporalis muscle flap, '
                    'and a free bone graft. Split the thick upper part of the craniotomy flap with a '
                    'reciprocating saw to get a bone plate that spans a wide floor defect.'],
                   ['Protect the ossicles from dural sag',
                    'If the tympanic roof was widely opened, rebuild it with a bone sheet (from the thin '
                    "lower craniotomy edge or split flap) so middle fossa dura doesn't settle onto the "
                    'ossicular heads and cause conductive loss.'],
                   ['Seal air cells and replace the flap',
                    'Press bone wax into opened air-cell tracts with a blunt dissector or cottonoid. Fix the '
                    'craniotomy flap with wire or miniplates, butting it against two edges (not centered '
                    'with an even gap) to encourage bony union; the lowest margin can be left open because '
                    'temporalis and the zygomatic arch cover it.'],
                   ['Transmastoid repair',
                    'Do a cortical mastoidectomy and thin the tegmen around the defect until healthy bone '
                    'shows on all sides. Bipolar and cut any herniated tissue. Place fascia above the bone '
                    'defect, between dura and bone, then a rigid layer of cartilage or bone, then fascia '
                    'below. Protect the incus in the attic and avoid drilling on bare dura.'],
                   ['Salvage: obliterate the ear',
                    'For a leak that keeps recurring in a non-hearing ear, obliterate the middle ear. Remove '
                    'all canal skin, drum, and annular epithelium so no cholesteatoma forms, strip the '
                    'mucosa, and seal the Eustachian tube with bone wax and tissue. Be gentle at the tube, '
                    'as the carotid wall can be bare. Counsel that the ear will be permanently deaf to air '
                    'conduction.'],
                   ['Complete obliteration and canal closure',
                    'Cover the tube opening and aditus with fascia, fill the middle ear with a muscle plug, '
                    'and close the ear canal as a blind sac: evert the canal skin and suture it in two '
                    'layers. In a hearing ear, seal the air cells around the labyrinth with wax instead.'],
                   ['Aftercare',
                    'Keep the head up and avoid straining, nose blowing, and heavy lifting for several '
                    'weeks. Use a lumbar drain only selectively. In spontaneous leaks, look for raised '
                    'intracranial pressure; refer for weight loss, acetazolamide, and neuro-ophthalmology '
                    'review, since untreated pressure drives recurrence.']],
 'translabyrinthine-skull-base': [['Set up and harvest grafts',
                                   'Set up facial nerve monitoring and ask anesthesia to avoid long-acting '
                                   'paralytics. Harvest abdominal fat at the start and keep it moist, so you '
                                   'do not stop later. Take fascia too, from temporalis or rectus sheath, or '
                                   'fascia lata for large defects.'],
                                  ['Incision and soft tissue',
                                   'Incise about 4 cm behind the postauricular crease down to bone. Leave '
                                   'the posterior temporalis attached to the subcutaneous/periosteal layer '
                                   'for a sturdier closure. Expose the mastoid widely including occipital '
                                   'bone behind the sigmoid; divide emissary veins and wax them.'],
                                  ['Wide mastoidectomy and sigmoid decompression',
                                   'Remove cortex widely with a large cutting burr, from the posterior canal '
                                   'wall to 1 to 2 cm behind the sigmoid. Thin bone over the sinus with a '
                                   'large diamond and take it off, exposing 1 to 2 cm of dura behind the '
                                   'sinus. Small smooth fragments can stay on the sinus if it can still be '
                                   'pushed back.'],
                                  ['Antrum, dural plates, and tegmen',
                                   'Open the antrum until you see the whole lateral semicircular canal and '
                                   'short process of the incus, but do not widely open the attic, which '
                                   'raises the risk of CSF leaking through the middle ear. Expose posterior '
                                   'fossa dura between sinus and labyrinth. Thin or remove the tegmen bone '
                                   'and take the ledge along the superior petrosal sinus.'],
                                  ['Retract the sinus',
                                   'Elevate dura off the petrous bone and place retractors — this widens the '
                                   'corridor and keeps the drill off the sigmoid.'],
                                  ['Labyrinthectomy',
                                   'Start at the sinodural angle, cutting deep troughs parallel to dura and '
                                   'using the side of the burr, since this hard bone makes the burr skate. '
                                   'Open the lateral and posterior semicircular canals first, then the '
                                   'superior semicircular canal. Keep a bony shell under the lateral '
                                   "semicircular canal's front end, because the facial nerve lies directly "
                                   'beneath.'],
                                  ['Endolymphatic system and facial nerve',
                                   'With the canals opened, the endolymphatic duct is seen wrapping the '
                                   'common crus. Switch to diamond to define the horizontal segment and '
                                   'second genu of VII, leaving a thin bone shell, and drill down to nerve '
                                   'level so the lower IAC can be reached later. For big tumors, skeletonize '
                                   'the vertical segment for anterior CPA access.'],
                                  ['Vestibule',
                                   'Open the vestibule widely until you see the three ampullae and the '
                                   'recess that holds the utricle. You usually have to drill a little under '
                                   'the facial nerve. Near the ampulla of the superior semicircular canal, '
                                   'the labyrinthine segment of the facial nerve is close by, so slow down '
                                   'there.'],
                                  ['Toward the jugular bulb',
                                   'With the facial nerve found, take bone off the rest of the sigmoid down '
                                   'to the jugular bulb. Divide the endolymphatic duct where it enters dura '
                                   'so the dura can drop down toward the bulb. A high bulb can block the '
                                   'lower trough; press it down with wax and oxidized cellulose rather than '
                                   'drilling into it.'],
                                  ['IAC troughs',
                                   'Start drilling near the porus with a cutting burr, leaving the lateral '
                                   'end for later. Drill troughs above and below the IAC. Below, stop at the '
                                   'cochlear aqueduct: CSF may gush from it, and the glossopharyngeal nerve '
                                   'lies just beneath. Above, do not go too far laterally or you will reach '
                                   'the labyrinthine segment of the facial nerve early.'],
                                  ['Finish the canal',
                                   'Remove the last eggshell of bone over IAC dura with a diamond. Take the '
                                   'bony lip of the porus off dura in one or more pieces, and widen the '
                                   'porus so no ledge hides the tumor-nerve plane. Clear bone over about two '
                                   'thirds of the IAC circumference, taking extra care on the superior side, '
                                   'where the facial nerve runs.'],
                                  ['Find VII at the fundus',
                                   'At the fundus the transverse crest splits the upper and lower parts of '
                                   "the canal. In the upper part, Bill's bar separates the facial nerve in "
                                   'front from the superior vestibular nerve behind. Feel the bar with a '
                                   'hook, or find the nerve where it enters its bony canal. Stimulate before '
                                   'dividing the superior vestibular nerve.'],
                                  ['Dural opening',
                                   'Medium/large tumors: H-shaped incision — superior limb from near the '
                                   'sigmoid along the SPS into the supra-IAC trough; inferior limb over the '
                                   'bulb in the infra-IAC trough (thicker where the sac is divided). '
                                   'Coagulate, nick with a #11, elevate with a blunt dissector, finish with '
                                   'heavy scissors; open IAC dura with up-biting scissors and join at the '
                                   'porus. Small tumors: a limited Y may suffice.'],
                                  ['Tumor removal',
                                   'The facial nerve is usually pushed along the front of the tumor. Drain '
                                   'CSF from the cisterna magna if the cerebellum is tight. Stimulate the '
                                   'back of the capsule, core it with the ultrasonic aspirator, find the '
                                   'nerve at the brainstem and fundus, and finish at the sticky porus. Leave '
                                   'a thin remnant if the nerve will not come free.'],
                                  ['Closure',
                                   'Seal the fossa incudis with fascia (or remove the incus and pack muscle '
                                   'into the epitympanum, or open the facial recess and close the Eustachian '
                                   'tube between promontory and drum). Lay fat strips in one at a time, '
                                   'pushing earlier strips back with a retractor — fill the bony defect, not '
                                   'the intracranial space. Cover the dural opening with fascia and narrow '
                                   'it with sutures where possible.'],
                                  ['Wound closure and aftercare',
                                   'Close the soft tissue in layers over the fat and apply a mastoid '
                                   'pressure dressing. Document facial function on waking and protect the '
                                   'eye if closure is weak. Watch for clear nasal drainage or wound leak, '
                                   'which may come through the Eustachian tube. Start vestibular '
                                   'rehabilitation early.']],
 'tympanoplasty': [['Choose the approach',
                    'Pick the approach that shows the whole perforation edge and annulus. Small posterior '
                    'perforations can be done transcanal with a microscope or endoscope. An endaural or '
                    'postauricular approach suits anterior or large perforations, a narrow or bulging canal, '
                    'or the need for canalplasty. Endoscopic tympanoplasty avoids an external incision.'],
                   ['Anesthesia and middle-ear numbing',
                    'The case can be done under local. If lidocaine is run into the middle ear to numb the '
                    'mucosa, suction it out promptly, particularly from the round window niche where it '
                    'pools; residual anesthetic reaching the labyrinth causes postoperative vertigo.'],
                   ['Postauricular incision',
                    'Place the skin incision in the postauricular crease or set back 5–10 mm behind it '
                    '(set-back scars heal better and retract less). Carry the upper limb forward so the '
                    'auricle can be rotated anteriorly; in young children keep the inferior limb short '
                    'because the undeveloped tip leaves the facial nerve superficial.'],
                   ['Temporalis fascia harvest',
                    'Under retractor tension, find the linea temporalis keeping the blade angled upward '
                    '(angling down cuts into fascia or the canal roof). Incise above the linea temporalis, '
                    'leaving about 1 cm of fascia at the margin for later closure; elevate fascia in its '
                    'true plane off muscle (less bleeding, cleaner graft) using curved scissors; trim to '
                    'shape on a Teflon block.'],
                   ['Periosteal exposure for canal access',
                    'Incise along the linea temporalis toward the anterior canal (control the posterior '
                    'branch of the superficial temporal vessel at the front end). For tympanoplasty without '
                    'mastoidectomy, the periosteal cut can sit just behind the canal. Raise periosteum with '
                    'a Lempert-type elevator and free meatal skin from the bony meatus before opening the '
                    'self-retainer to avoid tearing it.'],
                   ['Posterior canal skin flap',
                    'From the spine of Henle, lift the posterior canal skin in the plane under periosteum '
                    'toward the drum, cutting adhesions at the suture lines sharply with needle cautery. '
                    'Make the side cuts from inside out at about 45 degrees so you enter the canal without '
                    'cutting the anterior skin. Thin the flap and hold it forward with a retractor.'],
                   ['Tympanomeatal flap incisions',
                    'The tympanomeatal flap for tympanoplasty is longer than a stapes flap. Crush the '
                    'planned incision line first to reduce bleeding and give a clean edge; tunnel under the '
                    'vascular strip superiorly and divide it with microscissors. From behind, the flap can '
                    'be cut briskly with scissors or blade rather than microinstruments.'],
                   ['Prepare the perforation edge',
                    'Freshen the edge of the perforation by removing the thin rim of epithelium with a pick '
                    'and cup forceps, so the edge can heal onto the graft and no skin is trapped behind it. '
                    'Some experienced surgeons skip this with similar results. Either way, roughen the inner '
                    'mucosal surface of the remnant so the graft gains blood supply.'],
                   ['Elevate flap and annulus',
                    'Raise the flap to the annulus, lift the annulus from its sulcus, and lyse middle-ear '
                    'mucosa with a curved needle. Inferiorly use the side of the annulus elevator pressed '
                    'firmly on bone, not its tip, to avoid tears. Keep the exposure open by pressing the '
                    'flap onto the anterior canal wall with the back of the elevator; surface tension holds '
                    'it.'],
                   ['Inspect the middle ear',
                    'Fold the flap forward to see the underside of the drum. Check that the ossicles are '
                    'intact and move, find the chorda tympani, and look for cholesteatoma, adhesions, or '
                    'tympanosclerosis. Do any ossicular reconstruction now, before the graft goes in.'],
                   ['Anterior perforation adjustments',
                    'Anterior perforations fail more often because the graft has little to hold onto in '
                    'front. Drill down a bulging anterior canal wall if it hides the edge, roughen the '
                    'mucosa near the Eustachian tube opening, cut the graft long enough to tuck forward, and '
                    'consider reinforcing it with cartilage.'],
                   ['Place the medial graft',
                    'Fill the middle ear under the perforation with small pieces of gelatin sponge, keeping '
                    'them off the Eustachian tube opening and round window. Slide the fascia under the drum '
                    'remnant so it overlaps the edge widely on all sides. Expect to adjust it. Use a small '
                    'suction with an instrument between it and the graft.'],
                   ['Lateral-graft variant (when chosen)',
                    'Superior incisions outline a vascular strip; the medial cut sits just lateral to the '
                    'annulus. Remove remaining canal skin as a free graft, strip all squamous epithelium '
                    'from the remnant (to prevent pearls), drill the anterior bulge so the narrowest point '
                    'is the annulus, place fascia lateral to the remnant but medial to the malleus handle, '
                    'then return the strip and free skin overlapping the fascia.'],
                   ['Cartilage harvest when needed',
                    'Harvest cartilage before placing the graft. Incise on the inner side of the tragus, '
                    'leaving 2 to 3 mm at the dome so the tragus keeps its shape. Free the cartilage with '
                    'scissors, lift off perichondrium on one side, and thin or bevel the side that will face '
                    'the drum. Close the skin with a couple of absorbable sutures.'],
                   ['Flap return and packing',
                    'Lay the tympanomeatal flap back and check that the graft lies flat, without folds, and '
                    'touches the remnant all around, especially in front. For medial grafts, support the '
                    'drum with gelatin sponge in the canal. For lateral grafts, pack firmly to prevent '
                    'blunting and lateralization.'],
                   ['Closure and anti-lop-ear suture',
                    'After reapproximating soft tissue, tunnel to the antihelical fold and place an '
                    'anchoring suture; push the auricle toward the head from its front surface while tying '
                    "so the stitch doesn't cut through perichondrium. Children, with floppier cartilage, are "
                    'most prone to a protruding "lop" ear after postauricular surgery.']],
 'vestibular-schwannoma': [['Frame the decision',
                            'Observation with MRI and stereotactic radiosurgery are standard for many small '
                            'tumors. For surgery, serviceable hearing (about PTA 50 dB or better and word '
                            'score 50% or better) and tumor size drive the approach: middle fossa for small '
                            'intracanalicular tumors, retrosigmoid for hearing attempts or any size, '
                            'translabyrinthine when hearing is poor. Confirm hearing intent before drilling '
                            'the labyrinth.'],
                           ['Read the MRI for fundal depth',
                            'Contrast MRI shows how far tumor reaches into the IAC. Tumor size in the angle '
                            'does not predict this. A bright fluid cap at the fundus on T2 imaging favors '
                            'hearing preservation. Depth matters most for retrosigmoid surgery, where only '
                            'the medial two thirds of the canal can be opened without entering the posterior '
                            'semicircular canal or vestibule.'],
                           ['Middle fossa limits',
                            'Best for intracanalicular tumors; the extended version handles CPA components '
                            'under ~1.5 cm (extra bone around porus) to ~2 cm (divide SPS and nick '
                            'tentorium). Inferior exposure is poor, so not for larger tumors. Blind spots: '
                            'inferior compartment behind the transverse crest; anterior fundus behind '
                            "labyrinthine VII. The facial nerve usually sits on the tumor's superior surface "
                            '— directly in the path.'],
                           ['Translabyrinthine strengths',
                            'This approach gives up hearing but opens the whole IAC to the fundus, lets you '
                            'find the facial nerve where it enters its bony canal, and handles even very '
                            'large tumors with little cerebellar retraction. It can be extended toward the '
                            'petrous apex and clivus, where the abducens nerve and basilar artery come into '
                            'view.'],
                           ['Retrosigmoid trade-offs',
                            'Opening abuts the transverse-sigmoid sinuses; cisterna magna must be opened '
                            'before retraction (massive swelling risk). Hearing can be attempted; fundal '
                            'tumor requires opening inner ear or blind angled removal (risk of residual); '
                            'CSF leak around 15% from perimeatal air cells; cranioplasty reduces '
                            'postoperative headache.'],
                           ['Monitoring plan',
                            'Place facial EMG needles in orbicularis oris and oculi; add temporalis for V, '
                            'and lower cranial nerve monitoring for large tumors. Ask anesthesia to avoid '
                            'long-acting paralytics. For hearing preservation, a recording electrode on the '
                            'VIII nerve gives faster feedback than ABR, which needs averaging and lags.'],
                           ['Decompress before retracting',
                            'Once dura is open, elevate the cerebellum and open the lateral cisterna magna '
                            'early. Identify V, IX, X in the field; dissect the lateral cerebellar lobe off '
                            'the tumor. Preserve the petrosal vein in small/medium tumors if possible; '
                            'bipolar before dividing if necessary.'],
                           ['Stimulate, then debulk',
                            "Sweep the posterior capsule with the stimulator to confirm VII isn't there, cut "
                            'a capsule window, and core with the ultrasonic aspirator — without breaching '
                            'the capsule, since a breached capsule makes nerve separation harder. Dissect '
                            'the collapsed capsule off cerebellum and trim it.'],
                           ['Lower pole and AICA',
                            'The inferior AICA branch usually runs on the lower pole; dissect it free and '
                            'protect it under a cottonoid.'],
                           ['Find VII at the brainstem first',
                            'Work inferiorly to locate the VII/VIII root entry zones — the AICA branch '
                            'between them is a reliable landmark — and confirm VII with stimulation. Split '
                            'VII from VIII; in non-hearing cases divide VIII near the brainstem. Only then '
                            'strip tumor off the middle cerebellar peduncle and pons; starting on the pons '
                            'early risks injuring a nerve that runs superiorly before turning to the porus.'],
                           ['Find VII at the fundus',
                            'Stimulate the back wall of the IAC to make sure the nerve is not there, then '
                            'open canal dura and peel it off the tumor. At the fundus, the superior '
                            'vestibular nerve may lie over the facial nerve; stimulate both at low current '
                            'and cut the vestibular nerve. In non-hearing cases, divide the cochlear nerve '
                            'too, then work fundal tumor medially.'],
                           ['The porus-lip danger zone',
                            'VII bends acutely over the anterior porus lip — usually the most adherent '
                            'segment. Cut the superior/inferior IAC dural "shoulders" (after stimulating), '
                            'divide porus dura, and work the plane from whichever end (proximal or distal) '
                            'dissects more easily. Sharp-cut arachnoid bands; reflect tumor with fenestrated '
                            'suction; leave the stickiest part for last.'],
                           ['Accept near-total removal',
                            'If the capsule is fused to the facial nerve, leave a thin remnant and cauterize '
                            'it lightly; regrowth is uncommon but needs MRI follow-up. A triangle of tissue '
                            'that widens toward the brainstem usually means you are on VIII strands, in the '
                            'wrong plane. Dissect the upper pole off V.'],
                           ['Approach-specific closure',
                            'Translab: fascia over fossa incudis, fat strips filling the bony defect only, '
                            'fascia over dura. Retrosigmoid: wax air cells found with a blunt hook, fat plug '
                            'held by stay suture, watertight dura, cranioplasty. Middle fossa: wax cells, '
                            'small fat graft, bone sheet over opened tympanic roof, flap fixed against two '
                            'edges.'],
                           ['After surgery',
                            'Document facial function and protect the eye with lubricant and taping if '
                            'closure is weak. Watch for CSF leak from the wound or nose, headache, and lower '
                            'cranial nerve problems. Get a baseline MRI and continue surveillance, '
                            'especially after near-total resection.']]}

ATLAS_URLS_V840 = {'canalplasty': ['https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/external-ear/anterior-canalplasty/',
                 'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/external-ear/exostoses-of-the-ear-canal/',
                 'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/fundamentals-of-ear-surgery/incision-closure/',
                 'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/fundamentals-of-ear-surgery/postauricular-canal-flap-design/',
                 'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/fundamentals-of-ear-surgery/postauricular-incision/'],
 'cochlear-implant': ['https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/cochlear-implantation/',
                      'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/facial-nerve-surgery/cholesteatoma-and-the-facial-nerve/'],
 'jugular-foramen-tumor': ['https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/approaches-to-jugular-foramen-and-infratemporal-fossa/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/approaches-to-jugular-foramen-and-infratemporal-fossa/infratemporal-fossa/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/approaches-to-jugular-foramen-and-infratemporal-fossa/jugular-foramen-approach/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/approaches-to-jugular-foramen-and-infratemporal-fossa/transjugular-craniotomy/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/cranial-nerve-monitoring/'],
 'mastoidectomy': ['https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/cholesteatoma/canal-wall-down-mastoidectomy-2',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/fundamentals-of-ear-surgery/postauricular-canal-flap-design/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/fundamentals-of-ear-surgery/postauricular-incision/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/ossiculoplasty/autologous-ossiculoplasty/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/tympanoplasty/medial-graft-tympanoplasty/',
                   'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/facial-nerve-surgery/cholesteatoma-and-the-facial-nerve/'],
 'middle-fossa-skull-base': ['https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/cranial-nerve-monitoring/',
                             'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/middle-fossa-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/',
                             'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/middle-fossa-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/extended-middle-fossa-approach-to-the-cerebellopontine-angle/',
                             'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/middle-fossa-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/middle-fossa-approach-to-the-internal-auditory-canal/'],
 'ossiculoplasty': ['https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/ossiculoplasty/autologous-ossiculoplasty/',
                    'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/ossiculoplasty/patterns-of-ossicular-deficiency/',
                    'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/stapes-surgery/exposure/',
                    'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/tympanoplasty/tragal-cartilage-harvesting/'],
 'retrosigmoid-skull-base': ['https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/cerebrospinal-fluid-leak/',
                             'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/cranial-nerve-monitoring/',
                             'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/microsurgical-resection-of-acoustic-neuroma/',
                             'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/retrosigmoid-approach/'],
 'stapedotomy': ['https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/stapes-surgery/exposure/',
                 'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/stapes-surgery/stapedotomy/'],
 'tegmen-repair': ['https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/cerebrospinal-fluid-leak/',
                   'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/encephalocoele/',
                   'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/middle-fossa-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/middle-fossa-approach-to-the-internal-auditory-canal/'],
 'translabyrinthine-skull-base': ['https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/cerebrospinal-fluid-leak/',
                                  'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/lateral-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/',
                                  'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/lateral-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/translabyrinthine-approach/',
                                  'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/microsurgical-resection-of-acoustic-neuroma/'],
 'tympanoplasty': ['https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/fundamentals-of-ear-surgery/incision-closure/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/fundamentals-of-ear-surgery/postauricular-canal-flap-design/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/fundamentals-of-ear-surgery/postauricular-incision/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/tympanoplasty/anterior-perforation-repair/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/tympanoplasty/fascia-harvesting/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/tympanoplasty/lateral-graft-tympanoplasty/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/tympanoplasty/medial-graft-tympanoplasty/',
                   'https://otosurgeryatlas.stanford.edu/otologic-surgery-atlas/tympanoplasty/tragal-cartilage-harvesting/'],
 'vestibular-schwannoma': ['https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/cranial-nerve-monitoring/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/lateral-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/lateral-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/translabyrinthine-approach/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/microsurgical-resection-of-acoustic-neuroma/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/middle-fossa-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/middle-fossa-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/extended-middle-fossa-approach-to-the-cerebellopontine-angle/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/middle-fossa-approaches-to-the-internal-auditory-canal-and-cerebellopontine-angle/middle-fossa-approach-to-the-internal-auditory-canal/',
                           'https://skullbasesurgeryatlas.stanford.edu/illustrations-of-skull-base-surgery-and-neurotology/retrosigmoid-approach/']}


def install_or_steps_v840(data, extra=None):
    registry = data.OR_PREP_REGISTRY
    table = dict(STEPS_V840)
    labels = {slug: SOURCE_LABEL_V840 for slug in table}
    for mod in extra or ():
        table.update(mod.STEPS)
        labels.update({slug: mod.SOURCE_LABEL for slug in mod.STEPS})
    done, missing = [], []
    for slug, steps in table.items():
        card = registry.get(slug)
        if not card:
            missing.append(slug)
            continue
        card["steps_v840"] = [list(s) for s in steps]
        card["steps"] = [f"{t}. {d}" for t, d in steps]
        card["steps_source_v840"] = labels[slug]
        src = card.get("source_basis")
        if isinstance(src, list) and labels[slug] not in src:
            src.insert(0, labels[slug])
        done.append(slug)
    return {"updated": done, "missing": missing}
