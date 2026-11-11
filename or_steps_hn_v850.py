"""v85.0: richer operative steps for the head and neck OR cards.

Rewritten in our own words from Simo, Pracy & Fernandes (eds), Atlas of Head and Neck Surgery
(Springer Surgery Atlas Series, 2024), with standard practice kept from the earlier cards where the
atlas is silent (reoperative surgery, flap salvage, fistula repair). Installed through
or_steps_v840.install_or_steps_v840(data, extra=[this module]).
"""

SOURCE_LABEL = "Simo, Pracy & Fernandes, Atlas of Head and Neck Surgery (Springer, 2024)"

STEPS = {'central-neck': [['Set up nerve monitoring and baselines',
                   'Confirm preoperative glottic function on laryngoscopy, since a nerve can be invaded yet '
                   'still move the cord. Use an EMG endotracheal tube so recurrent laryngeal nerve (RLN) '
                   'signals guide decisions; a starting amplitude of 500 µV or more is a good normal '
                   'baseline. Position supine with the neck extended on a shoulder roll.'],
                  ['Open the central neck',
                   'Use a standard thyroidectomy collar incision and raise subplatysmal flaps, typically '
                   'from the thyroid notch to the sternal notch. Divide the midline raphe vertically all the '
                   'way from hyoid to sternal notch so the straps retract fully laterally; this exposure '
                   'matters for the low paratracheal and upper mediastinal work later.'],
                  ['Know what counts as a central neck dissection',
                   'By American Thyroid Association consensus, a central neck dissection removes the '
                   'prelaryngeal and pretracheal nodes plus at least one paratracheal basin, as a '
                   'compartment rather than node picking. State whether it is therapeutic (clinically or '
                   'radiologically positive nodes) or prophylactic, and unilateral or bilateral, because '
                   'bilateral paratracheal clearance roughly doubles the hypoparathyroidism risk.'],
                  ['Judge the strap planes',
                   'Look at the plane between sternohyoid and sternothyroid and between sternothyroid and '
                   'the gland. A few patchy adhesions are common after needle biopsy; a plane that is '
                   'broadly lost suggests extrathyroidal extension. In that case remove the adherent '
                   'sternothyroid, and sternohyoid if needed, with the gland as the front margin. After wide '
                   'bilateral strap removal, a dermal graft or local flap prevents skin-to-trachea '
                   'tethering.'],
                  ['Mobilize the thyroid, sparing the external branch',
                   'As the superior pole is taken and the gland rolled off the larynx, cricothyroid and '
                   'cricopharyngeus come into view, with the external branch of the superior laryngeal nerve '
                   'on the cricothyroid fascia. Divide upper-pole vessels close to the gland. Be fluent in '
                   'more than one route to the RLN (inferior, superior, lateral, medial) for scarred or '
                   'invaded fields.'],
                  ['Assess the trachea and esophagus at Berry ligament',
                   'While freeing the gland off the trachea, look for perichondrial or cartilage invasion. '
                   'Superficial disease may be shaved with acceptable margins. Full-thickness invasion needs '
                   'window or segmental resection, ideally planned from preoperative imaging and endoscopy. '
                   'For esophageal muscle invasion, a dilator in the lumen helps define the plane and '
                   'protect mucosa; bolster resected muscle with a flap or dermis.'],
                  ['Decide what to do with an invaded RLN',
                   'Tumor confined to the epineurium can usually be shaved off with good recovery of '
                   'function. Deeper invasion seldom allows clearance without gross residual disease. '
                   'Preserve a nerve that still works preoperatively unless histology is aggressive and '
                   'adjuvant options are poor. If the cord was already weak, stimulate proximally; a '
                   'response favors preservation. Discuss this trade-off before surgery.'],
                  ['Interpret loss of signal',
                   'Loss of signal means an amplitude under about 100 µV. First rule out equipment problems: '
                   'check tube depth, electrode and ground leads, stimulator settings, a laryngeal twitch on '
                   'palpation and the contralateral vagus. If it is a true loss and does not recover above '
                   'half of baseline (about 250 µV) within 20 minutes, paralysis is likely, roughly 80%. Let '
                   'this decide whether to proceed to the second side.'],
                  ['Clear the prelaryngeal (Delphian) compartment',
                   'This is often done while removing the pyramidal lobe. Take tissue from the old upper '
                   'isthmus position up to the thyroid notch, including nodes on the cricothyroid membrane '
                   'or on the cricothyroid fascia. Remember the external branch lies on that fascia; vessels '
                   'bridging the upper pole and cricothyroid need control without blind cautery.'],
                  ['Clear the pretracheal compartment',
                   'Start at the former lower isthmus and work down to the innominate artery, which must be '
                   'located before deep inferior dissection. Staying directly on the anterior tracheal wall '
                   'keeps you away from both RLNs, particularly the medially placed left nerve. Leave the '
                   'thymus: it rarely holds nodes, may carry the inferior parathyroid, and removing it only '
                   'adds hypocalcemia.'],
                  ['Never cross into the paratracheal space blind',
                   'The paratracheal compartment lies between the common carotid laterally and trachea '
                   'medially, from the cricoid down to the innominate artery. Moving sideways from the '
                   'pretracheal plane before the RLN is seen is how nerves are injured, especially on the '
                   'left. Identify the nerve first, then define the compartment boundaries.'],
                  ['Expose the carotid and stimulate the vagus',
                   'Open the medial carotid sheath from cricoid to thoracic inlet. Stimulating the vagus '
                   'here proves the monitor is working and that the full length of the recurrent nerve '
                   'conducts, which probing the nerve alone cannot show. Record this as the vagal baseline, '
                   'and repeat vagal stimulation when each side is finished to document an intact circuit.'],
                  ['Handle the right RLN',
                   'The right nerve loops around the subclavian artery, so it enters the low paratracheal '
                   'space more anteriorly and runs obliquely upward; nodal tissue lies both in front of and '
                   'behind it. Free the nerve circumferentially, starting at the lower cricoid border and '
                   'moving caudally, so the dorsal nodes can be passed beneath it. Circumferential '
                   'mobilization raises traction neuropraxia risk; handle gently.'],
                  ['Handle the left RLN',
                   'The left nerve runs up within the tracheoesophageal groove, parallel and medial. It '
                   'usually does not need circumferential mobilization: the packet can be cleared lateral '
                   'and anterior to it with less handling. Keep the nerve in view continuously and avoid '
                   'energy devices close to it.'],
                  ['Remove the paratracheal packet into level VII',
                   'Work caudally from the lower cricoid, lifting the tissue off prevertebral fascia, '
                   'dividing it laterally behind the carotid and freeing it medially from the esophagus. '
                   'Retract the trachea medially and carotid laterally to reach the deepest nodes. Level VII '
                   'lies below the sternal notch down to the innominate artery and vein; because that artery '
                   'is right-sided, the left lower limit is less defined.'],
                  ['Protect the parathyroids',
                   'The superior gland can usually be kept in place on its own pedicle. The inferior gland '
                   'lies close to the nodal packet and is often at risk, so inspect the specimen before it '
                   'leaves the field. If a gland cannot keep its blood supply, confirm it on frozen section '
                   'of a small fragment, mince it into 1 mm pieces and implant it in an SCM pocket marked '
                   'with a clip.'],
                  ['Check the first side before starting the second',
                   'Before bilateral paratracheal dissection or completing the contralateral lobe, confirm '
                   'the first RLN still gives a good signal. If amplitude is below about 250 µV, consider '
                   'staging the second side to avoid bilateral cord paralysis. For differentiated cancer, '
                   'delaying completion up to about 25 weeks appears oncologically safe; reassess function '
                   'before returning.'],
                  ['Orient, inspect and close',
                   'Label the specimen by compartment (prelaryngeal, pretracheal, right and left '
                   'paratracheal, level VII) for pathology. Inspect the tracheoesophageal grooves for '
                   'residual target nodes, confirm parathyroid color and final RLN signal, then secure '
                   'hemostasis with a Valsalva check. A drain is not routinely needed after thyroidectomy '
                   'with or without central dissection.']],
 'completion-thyroidectomy': [['Review the first operation',
                               'Obtain the prior operative note and final pathology. Note whether the '
                               'recurrent laryngeal nerve was seen and stimulated, whether the signal was '
                               'lost, which parathyroids were seen, removed or autotransplanted, whether the '
                               'isthmus and pyramidal lobe were taken, and whether any central neck '
                               'dissection was done. This predicts parathyroid reserve and scar on the '
                               'remaining side.'],
                              ['Laryngoscopy and timing',
                               'Examine the vocal folds before surgery. If the first-side nerve is weak, the '
                               "remaining nerve is the patient's only working one, so a bilateral palsy "
                               'would threaten the airway; discuss waiting for recovery, since delay of '
                               'several months is acceptable for differentiated cancer, and consent for '
                               'possible tracheostomy. A contralateral palsy also rules out same-day '
                               'discharge.'],
                              ['Monitoring and positioning',
                               'Place an electromyographic endotracheal tube with electrodes at the vocal '
                               'folds and use a short-acting paralytic. Position with shoulder roll, head '
                               'ring and the head of the bed up 15 to 30 degrees. Obtain baseline vagal and '
                               'recurrent nerve signals before dissecting, so any later change can be '
                               'interpreted.'],
                              ['Incision and flaps',
                               'Reopen the previous transverse scar, which usually gives adequate access. '
                               'Raise subplatysmal flaps superficial to the anterior jugular veins to the '
                               'thyroid notch and sternal notch, using countertension. Scar from the first '
                               'operation often makes these planes stickier than usual, so stay deliberately '
                               'on the platysma undersurface.'],
                              ['Enter the remaining side through fresh planes',
                               'The midline raphe and the previously operated bed are usually scarred. If '
                               'the midline is dense, approach the remaining lobe laterally, between the '
                               'strap muscles and the SCM, to reach virgin tissue over the carotid sheath '
                               'and thyroid. Partial division of the upper sternothyroid improves access to '
                               'the superior pole.'],
                              ['Lateral mobilization',
                               'Sweep fascia off the lateral lobe toward the carotid sheath with a pledget '
                               'and divide the middle thyroid vein. Assess strap adherence: focal adhesions '
                               'are expected, but dense fixation may represent extrathyroidal extension and '
                               'warrants taking a strap cuff with the specimen as a ventral margin.'],
                              ['Superior pole',
                               'Open the pocket between the medial upper pole and the inferior constrictor, '
                               'retract the pole downward, and ligate the pole vessels one at a time close '
                               'to the gland, keeping energy tips visible. This protects the external branch '
                               'of the superior laryngeal nerve, which lies on the cricothyroid and inferior '
                               'constrictor.'],
                              ['Preserve the remaining parathyroids',
                               "These may now be the patient's only functioning glands. Follow the upper "
                               'pole contour down to the superior parathyroid, look for the inferior one '
                               'near the lower pole, and dissect on the capsule so each is pushed away on '
                               'its pedicle. Divide terminal inferior thyroid branches on the gland, beyond '
                               'the parathyroid supply.'],
                              ['Find the recurrent laryngeal nerve in unscarred territory',
                               'On a previously undissected side, the inferior paratracheal route or the '
                               'lateral route at the inferior thyroid artery near the tubercle of '
                               'Zuckerkandl usually works. If those segments are distorted, use the superior '
                               'approach: the laryngeal entry point deep to the lower edge of the inferior '
                               'constrictor, behind the cricothyroid joint, then trace caudally. Confirm '
                               'with the probe.'],
                              ['Nerve anatomy reminders',
                               'The left nerve lies more medially, parallel within the tracheoesophageal '
                               'groove; the right runs obliquely from lateral. The nerve may lie in front '
                               'of, behind or between inferior thyroid artery branches and may branch before '
                               'entry; preserve every branch.'],
                              ['Berry ligament',
                               'Apply minimal traction on the lobe, which otherwise stretches the adherent '
                               'nerve. Divide the ligament with fine instruments and careful bipolar or '
                               'sharp dissection while the nerve is followed into the larynx. Any isthmus '
                               'stump or tissue on the trachea from the first operation is scarred here; '
                               'dissect it with the nerve course already known.'],
                              ['Remove all remaining thyroid',
                               'Take the pyramidal lobe, any isthmus remnant and tissue at the old resection '
                               'margin. Residual thyroid undermines radioactive iodine ablation and '
                               'thyroglobulin surveillance. Inspect the specimen for parathyroid tissue '
                               'before it leaves the field.'],
                              ['Autotransplant with confirmation',
                               'If a parathyroid is devascularized or found on the specimen, send a small '
                               'fragment for frozen section to confirm it is parathyroid, not thyroid, node '
                               'or tumor, then mince and place it in an SCM pocket marked with a '
                               'nonabsorbable suture or clip.'],
                              ['Central neck dissection if indicated',
                               'When nodal disease is present or the oncologic plan requires it, clear the '
                               'pretracheal tissue staying on the trachea down to the innominate artery and '
                               'the paratracheal basin after exposing the carotid and nerve, leaving the '
                               'thymus. Weigh parathyroid risk carefully because previous surgery may '
                               'already have reduced reserve.'],
                              ['Confirm the nerve',
                               'Stimulate the recurrent nerve and the vagus after resection and record the '
                               'final amplitude. Compare with baseline; a well-preserved signal predicts '
                               'normal fold movement, and a documented intact circuit helps interpret any '
                               'postoperative stridor.'],
                              ['Hemostasis',
                               'Irrigate and clear clots, lower the head of the bed and ask for Valsalva at '
                               'least twice. Use bipolar carefully near the nerve, and lay oxidized '
                               'cellulose over minor ooze on the nerve rather than cauterizing it.'],
                              ['Closure',
                               'Drains are not routine, though a large dead space or anticoagulation can '
                               'justify one. Approximate the straps with interrupted absorbable sutures '
                               'leaving a small inferior gap so a hematoma can decompress, then close '
                               'platysma and skin in a way that allows quick reopening.'],
                              ['Postoperative calcium and airway',
                               'Treat a completion as a hypocalcemia risk: check calcium at about 6 and 12 '
                               'hours and PTH, and supplement per protocol. Watch for stridor and neck '
                               'swelling; an expanding hematoma with airway trouble is opened at the bedside '
                               'at once. Start or hold levothyroxine according to the radioiodine plan, and '
                               'examine the vocal folds after surgery.']],
 'conservation-laryngectomy': [['Re-stage on the table',
                                'Once the airway is secure, repeat direct laryngoscopy with 0-, 30- and '
                                '70-degree telescopes, both with and without the tube, to confirm the tumor '
                                'still fits the plan. Recheck the anterior and posterior commissure, '
                                'arytenoid mobility, and subglottic and inferior paraglottic extent. Consent '
                                'must already cover converting to total laryngectomy during the case.'],
                               ['Airway, tubes and position',
                                'For the vertical operation, choose with anesthesia between routine '
                                'intubation, awake fiberoptic intubation, and an awake tracheostomy under '
                                'local anesthesia. Place a nasogastric tube. For the supracricoid operation, '
                                'intubate orally, place a nasogastric tube, and delay the tracheostomy until '
                                'resectability is confirmed. Position supine with a shoulder roll for full '
                                'neck extension. A urinary catheter and good venous access suit this long '
                                'case.'],
                               ['Vertical: low tracheostomy first',
                                'Make a short transverse incision halfway between cricoid and sternal notch. '
                                'Open a wide transverse tracheotomy between rings, held open with a cricoid '
                                'hook, and place a reinforced tube. Stitch the tube to the sternal skin so '
                                'it stays out of the field. At the end, exchange it for a standard '
                                'tracheostomy tube sutured to the neck skin.'],
                               ['Vertical: expose the framework',
                                'Make a transverse incision over the middle of the thyroid cartilage. Raise '
                                'flaps subplatysmally up to the hyoid and down, keeping this wound separate '
                                'from the tracheostomy. Part the sternohyoid and sternothyroid at the '
                                'midline raphe with both pedicles intact. Expose the larynx from hyoid to '
                                'cricoid and keep the superior laryngeal neurovascular bundles out of harm.'],
                               ['Vertical: raise the outer perichondrial flap',
                                'Incise the outer thyroid perichondrium in the midline and along the upper '
                                'and lower cartilage borders on both sides, then reflect it back to the '
                                'posterior edge of each ala. Keep it attached to the overlying strap muscles '
                                "as one composite flap, and tack its free edges to the straps so it doesn't "
                                'dry out. Over cartilage invaded by tumor, do not preserve this layer.'],
                               ['Vertical: laryngofissure and inspection',
                                'Cut the thyroid cartilage in the midline with an oscillating saw, stopping '
                                'short of the lumen. Enter the airway through a transverse cricothyroid '
                                'membrane incision well clear of the tumor. Spread the cartilage halves and '
                                'inspect the anterior commissure and tumor directly before committing to the '
                                'resection lines.'],
                               ['Vertical: resect and check margins',
                                'Separate the inner perichondrium from the cartilage around the tumor, or '
                                'take the involved thyroid lamina with the specimen when the margin needs '
                                'it. Keep the arytenoid if the vocal process is free. Loupes or the '
                                'microscope help. Most US surgeons send frozen sections from all mucosal '
                                'margins routinely, not only when conversion is considered. Orient the '
                                'specimen for pathology and re-resect any positive margin.'],
                               ['Vertical: reconstruct and close',
                                'The outer perichondrium now lines the airway, with vascularized strap '
                                'muscle placed behind it or in place of the excised lamina. Close the '
                                'thyroid laminae anteriorly with fine absorbable monofilament on a taper '
                                'needle. If the opposite anterior commissure was taken, place a keel or '
                                'Montgomery stent against webbing. Leave a passive drain and the nasogastric '
                                'tube.'],
                               ['Supracricoid: apron flap and the strap decision',
                                'Raise a U-shaped bilateral (Roux-Berger) apron flap subplatysmally from 2–3 '
                                'cm above the sternal notch to both mastoids, exposing 2–3 cm above the '
                                'hyoid. Resect the straps when there is any hint of extralaryngeal spread '
                                '(cartilage, cricothyroid membrane, Delphian node). Otherwise split the '
                                'fascia in the midline, ligate the anterior jugular veins, and turn the '
                                'straps down off the hyoid and oblique line.'],
                               ['Supracricoid: Delphian node and tracheal release',
                                'Clear the prelaryngeal fat and Delphian node from the hyoid down to the '
                                'thyroid isthmus and send it for frozen section. A positive node without '
                                'airway invasion pushes you toward a supratracheal extension. Invasion of '
                                'the laryngotracheal axis means converting to total laryngectomy. Bluntly '
                                'free the front of the trachea down to the carina with a finger so it can '
                                'rise for the pexy.'],
                               ['Supracricoid: skeletonize and protect nerves',
                                'Rotate the larynx down to show the constrictors, then ligate the superior '
                                'laryngeal vessels or coagulate them as you go, preserving the sensory '
                                'superior laryngeal nerve branch to the pyriform sinus. Cut the constrictors '
                                'along the thyroid ala. On the arytenoid-sparing side, cut through the '
                                'inferior cornu so the recurrent laryngeal nerve below is never approached. '
                                'On the sacrifice side, disarticulate the cricothyroid joint.'],
                               ['Supracricoid: free the inner contents',
                                'Gently release the pyriform sinus mucosa and paraglottic contents from the '
                                'inside of the thyroid cartilage on both sides. Detach the cricothyroid '
                                'muscle from the upper lateral edge of the cricoid. Work carefully here, '
                                'because tears in the pyriform mucosa weaken the later reconstruction and '
                                'swallow.'],
                               ['Supracricoid: inferior entry above the cricoid',
                                'Enter the airway just above the cricoid ring so you can see the subglottis '
                                'and how far the tumor is from your cut. If the tumor reaches a few '
                                'millimeters into the anterior subglottis, lift the cricoid mucosa in a '
                                "subperichondrial plane and enter lower, at the cricoid's inferior border, "
                                'for a safer mucosal margin.'],
                               ['Supracricoid: superior entry by pexy type',
                                'For cricohyoidopexy, incise the inner hyoid periosteum and dissect '
                                'subperiosteally, taking the entire pre-epiglottic space down until the '
                                'vallecular submucosa shows through, then enter at the vallecula. For '
                                'cricohyoidoepiglottopexy, keep the suprahyoid epiglottis and cross it with '
                                'a transepiglottic cut perpendicular to the upper thyroid border, through '
                                'the pre-epiglottic space.'],
                               ['Supracricoid: lateral cuts and go/no-go',
                                'Starting on the less-involved side, cut down through the aryepiglottic '
                                'fold, the false fold in front of the arytenoid, thyroarytenoid in front of '
                                'the vocal process, and conus elasticus to meet the inferior cut. Tracking '
                                'the epiglottic edge protects the superior laryngeal nerves. Open the larynx '
                                'to inspect, then move ventilation to a sterile tube passed through the '
                                'inferior opening. Tumor below the cricoid means total laryngectomy.'],
                               ['Supracricoid: finish resection, frozen sections, tracheostomy',
                                'Complete the resection under direct vision, either joining cuts in front of '
                                'the contralateral arytenoid or taking one arytenoid through its '
                                'cricoarytenoid joint with the lateral cricoarytenoid. Dissect the pyriform '
                                'and postcricoid mucosa submucosally while a finger relaxes the sinus. Check '
                                'all margins by frozen section. While waiting, make a skin-sutured '
                                'tracheostomy between rings four and five.'],
                               ['Supracricoid: arytenoid set and pexy',
                                'Pull each kept arytenoid forward with a fine stitch from above the vocal '
                                'process to the cricoid, and tack the constrictor fascia to reposition the '
                                'sinuses. Pass three heavy absorbable sutures under the cricoid and up '
                                'through tongue base around the hyoid, adding epiglottis for '
                                'cricohyoidoepiglottopexy. Lateral stitches hug the hyoid to spare the '
                                'lingual artery and hypoglossal nerve. Flex the head and tie symmetrically.'],
                               ['Close and set rehabilitation goals',
                                'If an arytenoid was removed, rebuild that pyriform sinus before tying the '
                                'pexy. Reattach the constrictors, cover with straps or the thyroid gland, '
                                'place suction drains, and close in layers. Vertical: about a week of tube '
                                'feeding, then an instrumental swallow study. Supracricoid: the atlas '
                                'authors decannulate around day 4–6; many US centers decannulate later, '
                                'often in the second or third week, once airway and aspiration allow.']],
 'cp-myotomy': [['Indication and side',
                 'Open myotomy treats dysphagia from cricopharyngeal hypertrophy, stricture, or spasm, with '
                 'or without a Zenker diverticulum. Most surgeons approach from the left, because the pouch '
                 'usually bulges to the left and a nonrecurrent laryngeal nerve occurs only on the right. A '
                 'right-sided approach works the same way and is worth considering for revision through an '
                 'unscarred side.'],
                ['Anesthesia and tube placement',
                 'Use general anesthesia with an oral endotracheal tube secured toward the right corner of '
                 'the mouth, away from a left-sided field. Agree with anesthesia that a pharyngoscope and '
                 'bougie will be passed alongside the tube at both the start and the end of the case. '
                 'Recurrent laryngeal nerve monitoring is optional and may help in revision or scarred '
                 'necks.'],
                ['Pharyngoscopy and bougie',
                 'Begin with rigid pharyngoscopy to find the pouch, switching to a short esophagoscope if '
                 'access is difficult. The cricopharyngeal segment lies in front of the pouch neck. Dilate '
                 'it with an esophageal bougie of suitable size and leave the bougie in place for the whole '
                 'case, as a firm backstop for cutting. Packing the pouch helps identify it, but packs often '
                 'fall out.'],
                ['Position the neck',
                 'Place a shoulder cushion and head ring so the lower cervical spine is flexed and the head '
                 'is extended at the atlanto-occipital joint. Turn the head toward the right for a '
                 'left-sided approach. This opens the space between the SCM and the laryngotracheal column.'],
                ['J-shaped incision',
                 'Incise along the anterior border of the SCM from about the level of the hyoid, curving '
                 'medially to end about 1 cm below the cricoid. Deepen through platysma and the investing '
                 'layer of deep cervical fascia. Mark the cricoid level beforehand, because it is the center '
                 'of the operation.'],
                ['Develop the lateral corridor',
                 'Retract the SCM laterally to find the carotid sheath. Divide omohyoid, and ligate and '
                 'divide the middle thyroid vein if present. Retract the carotid sheath laterally until the '
                 'prevertebral fascia is exposed. This separates the midline visceral column (larynx, '
                 'thyroid, trachea, pharynx, esophagus) from the great vessels and opens the retropharyngeal '
                 'approach.'],
                ['Rotate the larynx to protect the nerve',
                 'Rotate the laryngeal framework away from you to bring the posterolateral fibers of the '
                 'inferior constrictor and the pouch into view. This rotation is the key nerve-protection '
                 'maneuver. It keeps the dissection behind the recurrent laryngeal nerve in the '
                 'tracheoesophageal groove. Avoid dissecting in the groove itself, and use bipolar near it.'],
                ['Find the pouch neck',
                 'Separate the pouch from the surrounding hypopharyngeal and esophageal wall to locate its '
                 'neck at the Killian dehiscence, the gap between the oblique thyropharyngeus above and the '
                 'horizontal cricopharyngeus below. If the neck is easy to identify, the myotomy can start '
                 'there. Often it is not obvious, and then you start from below.'],
                ['Start the myotomy in esophageal muscle',
                 'Begin the vertical cut in the posterolateral esophageal muscle below the cricopharyngeus. '
                 'Stroke a 15 blade lightly across the fibers while retraction above and the bougie inside '
                 'keep them taut. Cut fiber by fiber rather than with deep strokes, so the mucosa is seen '
                 'before it can be breached.'],
                ['Find and use the submucosal plane',
                 'Once the esophageal mucosa appears, spread gently perpendicular to it to lift the muscle '
                 'off the mucosa, and carry this plane upward ahead of the blade. Where the plane does not '
                 'open, continue dividing carefully with the scalpel until the mucosa is exposed. The bougie '
                 'gives counterpressure throughout.'],
                ['Complete a generous myotomy',
                 'Continue upward through all of the horizontal cricopharyngeal fibers and on into the lower '
                 'thyropharyngeus, for a total length of about 3–4 cm. The divided muscle edges should fall '
                 'apart, leaving a strip of bulging mucosa along the whole length. Fibers left near the '
                 'pouch neck are the common reason for a persistent bar.'],
                ['Manage the pouch',
                 'For small pouches (under about 2 cm), myotomy alone is enough. For larger pouches, many US '
                 'surgeons add a diverticulopexy, suspending the pouch upside down to the prevertebral '
                 'fascia, or a stapled diverticulectomy. The atlas authors usually leave the pouch, arguing '
                 'that a suture line in a frail patient adds risk and that a fully divided sphincter stops '
                 'the pouch acting as a reservoir.'],
                ['Check the mucosa',
                 'Inspect the whole myotomy for a mucosal breach. A useful test is to fill the wound with '
                 'saline while anesthesia insufflates air through a tube or scope, watching for bubbles. '
                 'Repair any hole immediately in layers with fine absorbable sutures.'],
                ['Re-scope to confirm the bar is gone',
                 'Remove any pouch pack, repeat pharyngoscopy, and pass the scope into the esophagus. There '
                 'should be no residual cricopharyngeal bar. If one remains, return to the neck and divide '
                 'the missed fibers, which usually lie toward the pouch neck.'],
                ['Feeding tube and closure',
                 'Pass a nasogastric tube if there is any doubt about mucosal integrity. Get hemostasis with '
                 'bipolar cautery, keeping heat off the exposed mucosa and away from the tracheoesophageal '
                 'groove. Close platysma with absorbable sutures and skin with clips or sutures.'],
                ['Watch for perforation, then feed',
                 'Check vital signs frequently for the first few hours. Fever, tachycardia, back or chest '
                 'pain, and surgical emphysema suggest an esophageal leak and need urgent contrast imaging. '
                 'After myotomy alone with intact mucosa, liquids can start that evening and a normal diet '
                 'the next day. After a mucosal repair or diverticulectomy, many surgeons hold oral intake '
                 'until a contrast study shows no leak.']],
 'ctr': [['Stage the stenosis and choose the resection type',
          "Use endoscopy to grade the narrowing (Myer–O'Connor–Cotton grade and Lano–Netterville subsites). "
          'Record vocal fold motion, distance from glottis and stoma, length, and remaining normal trachea. '
          'CT shows scar thickness in a complete stenosis. Resect anterior cricoid only for Type B, add '
          'inner posterior plate for Type C, use a posterior split with graft for Type D, and use '
          'hemicricoidectomy for Type E tumors.'],
         ['Secure the airway at induction',
          'Intubate with whatever gets past the stenosis safely, such as video laryngoscopy, a flexible '
          'scope, serial bougie dilation, or rigid bronchoscopy. Use the smallest tube that ventilates '
          'adequately. If none of these works, perform a tracheostomy through the stenosis. Avoid that route '
          'for a tumor, because it risks seeding, bleeding, and pushing tumor fragments into the distal '
          'airway.'],
         ['Position and open',
          'Hyperextend the head. Make a collar incision centered on the existing stoma or the stenosis, and '
          'extend it laterally if a neck dissection is needed. Raise subplatysmal flaps up toward the '
          'thyroid cartilage and down toward the sternal notch to expose the larynx and cervical trachea.'],
         ['Expose the laryngotracheal junction',
          'Open the midline fascia and pull the strap muscles aside. Divide the thyroid isthmus and peel '
          'each thyroid lobe away while staying right on the tracheal perichondrium. This keeps the '
          'recurrent laryngeal nerves (RLNs) lateral and safe without dissecting them out, which is not '
          'routine unless a thyroidectomy is also needed. Expose the whole stenotic segment before cutting.'],
         ['Respect where the RLN enters the larynx',
          'Each recurrent laryngeal nerve enters against the posterolateral cricoid lamina, just behind and '
          'inside the cricothyroid joint, under cricopharyngeus. Full-thickness removal of the anterior '
          'cricoid arch is safe forward of the cricothyroid joints. Behind the joints, and behind the '
          'posterior cricoarytenoid muscles, the nerve is at real risk.'],
         ['Protect the tracheal blood supply',
          'The trachea is fed segmentally from the side and, once the isthmus is divided, largely from the '
          'esophagus. So do not mobilize far below the stenosis, and separate the membranous wall from the '
          'esophagus for only about 1 to 1.5 cm beyond the cut, especially on the distal stump. Avoid '
          'lateral dissection, which threatens both vessels and nerves.'],
         ['Open the airway and set up cross-field ventilation',
          'Open the trachea below the stenosis to look inside. Pull the oral tube back to the glottis and '
          'tie a stitch to its tip so it can be advanced later. Pass a sterile tube through the field into '
          'the distal trachea and ventilate through it. Divide the trachea caudally where the rings are '
          'healthy.'],
         ['Resect the anterior cricoid (Type B)',
          'Remove the stenotic upper rings together with the anterior cricoid arch, taking it full thickness '
          'out toward, but not past, the cricothyroid joints. Bevel the distal tracheal stump so its leading '
          'edge fits under the lower border of the thyroid cartilage and between the cut ends of the '
          'cricoid.'],
         ['Treat posterior plate disease (Type C)',
          'When scar involves the mucosa and cartilage of the posterior cricoid plate, remove or drill it '
          'from inside the lumen, working outward. Stop at the posterior perichondrium and the posterior '
          'cricoarytenoid muscles. Cover the bare plate with a flap of membranous wall from the distal '
          'stump. In idiopathic subglottic stenosis this can extend up to the cricoarytenoid joints and '
          'conus elasticus.'],
         ['Re-tension the vocal folds when the conus is resected',
          'After extended resection up to the conus elasticus, pass one or two 3-0 or 4-0 polyglactin '
          'stitches to tether the underside of each vocal fold to the lower edge of the thyroid lamina on '
          'that side. This restores fold tension and a straight glottic edge before the main anastomosis is '
          'placed.'],
         ['Extended variants (Types D and E)',
          'For posterior glottic scar, split the thyroid cartilage in the front and the cricoid plate in the '
          'back, wedge a flanged rib graft between the plate halves, cover it with a membranous tracheal '
          'flap, and leave a stent for weeks. For a hemicricoid tumor, remove half the cricoid and '
          'disarticulate the arytenoid there, sacrificing that recurrent nerve. Then rotate an '
          'asymmetrically cut tracheal stump into the gap.'],
         ['Release the distal trachea',
          'Free the anterior and side surfaces of the distal stump by blunt finger dissection in the '
          'pretracheal plane, down toward the carina and the innominate artery origin. This usually gains '
          '1.5 to 2 cm of upward reach. Keep the finger anterior, because sweeping laterally causes bleeding '
          'and RLN injury.'],
         ['Place stay sutures and test tension',
          'Pass 2-0 polyglactin stay sutures around a full ring on each side of the distal stump, at least '
          'two rings below the cut. For cricoid resections, place matching upper stays into the lower '
          'thyroid alae, outside the mucosa. Bring each pair together to judge tension. If tension remains, '
          'usually beyond about 4 cm, add a laryngeal release; most US surgeons prefer the suprahyoid '
          "(Montgomery) release to the atlas's thyrohyoid release."],
         ['Lay the anastomotic sutures before tying',
          'Place four or five 4-0 polyglactin sutures joining the membranous tracheal wall to the posterior '
          'cricoid mucosa or plate. Then place ten to twelve 2-0 and 3-0 sutures around the sides and front, '
          'bringing them out on the outer laryngeal surface in a subperichondrial plane. Clip and organize '
          'them in order before any are tied.'],
         ['Switch tubes, flex, and tie in order',
          'Remove the distal field tube and advance the oral tube across the suture line. Flex the head with '
          'a pillow under the occiput. Tie the 2-0 stay sutures first, then the 4-0 posterior row, then the '
          'anterolateral sutures working from the sides toward the midline. Check for an air leak under '
          'positive pressure before closing.'],
         ['Close and immobilize the neck',
          'After Types D and E, a tracheostomy at least two to three rings below the anastomosis is '
          'mandatory. Bring the isthmus and straps back together in the midline and place a drain '
          'superficial to the straps. Place chin-to-chest guardian sutures to keep the head flexed. Wake the '
          'patient with a transnasal scope to check fold motion, airway space, and edema.'],
         ['Run anastomosis-protective postoperative care',
          'Give antiemetics, cough suppression, and acid suppression, and humidify generously. The atlas '
          'avoids steroids because they impair healing; some US teams give a short perioperative course for '
          'airway edema. Watch for a leak: dry cough, subcutaneous emphysema, or skin redness. Start oral '
          'feeding around day 2, remove the drain around day 3, cut the guardian sutures around day 7–8, and '
          'plan follow-up endoscopy.']],
 'deep-neck-drain': [['Assess the airway first',
                      'Do flexible fiberoptic laryngoscopy at the first examination. Sublingual, '
                      'parapharyngeal and retropharyngeal collections, and bilateral floor-of-mouth '
                      'cellulitis (Ludwig angina), carry the greatest airway threat. If the patient is short '
                      'of breath or the airway looks narrowed, give oxygen, intravenous steroids and '
                      'nebulized epinephrine as a temporizing measure while the operating room is arranged.'],
                     ['Plan the airway with anesthesia',
                      'For drainage with any airway narrowing, an experienced anesthesiologist should run '
                      'the induction while a surgeon stands scrubbed with a tracheostomy tray open. Agree '
                      'beforehand on awake fiberoptic intubation or awake tracheostomy under local '
                      'anesthesia, and on the fallback if the first plan fails. Avoid paralysis until the '
                      'airway is secured, since a relaxed obstructed airway may become impossible to '
                      'ventilate.'],
                     ['Map the collection on contrast imaging',
                      'Contrast CT shows which spaces are involved, separates abscess from phlegmon, shows '
                      'airway deviation, and reveals complications such as mediastinal fat stranding, '
                      'gas-fluid levels or internal jugular vein thrombosis. Ultrasound also distinguishes '
                      'collection from inflammation and can guide needle drainage. Check coagulation and '
                      'glucose; diabetes and immunosuppression predict multispace and atypical infection.'],
                     ['Decide whether to operate now',
                      'A significant abscess in an adult warrants urgent incision and drainage. Selected '
                      'children can first be managed medically. A retropharyngeal collection under about 2 '
                      'cm² can be watched, with drainage for airway compromise or no improvement after 24–48 '
                      'hours. Prestyloid parapharyngeal infection may settle medically. Case-by-case '
                      'judgment governs.'],
                     ['Choose the route by space',
                      'Peritonsillar collections drain transorally. Retropharyngeal abscess medial to the '
                      'great vessels is best drained transorally. Masticator space: medial to the mandible '
                      'go intraorally, lateral go externally. Prestyloid parapharyngeal collections can be '
                      'drained transorally or transcervically. Poststyloid, carotid sheath, visceral, danger '
                      'and prevertebral space infections need an external approach. Submandibular/sublingual '
                      'collections may need both routes.'],
                     ['Drain transorally when appropriate',
                      'With the airway secured and the head extended and lower than the body to protect '
                      "against aspiration, aspirate with a needle first to confirm the pocket's depth. Then "
                      'make a vertical mucosal incision over the point of maximal bulge, spread bluntly, and '
                      'keep a large suction ready for the pus.'],
                     ['Make an adequate transcervical incision',
                      'Place a skin-crease incision over the collection, long enough for wide exposure and '
                      'dependent drainage, usually along or across the anterior SCM border at the level of '
                      'the abscess. Superficial abscesses above the investing fascia drain through an '
                      'incision along the skin lines.'],
                     ['Find the carotid sheath before entering the abscess',
                      'Open the investing fascia, retract the SCM laterally and identify the carotid sheath. '
                      'For parapharyngeal collections, work up along the posterior digastric belly toward '
                      'the styloid. Keep the sheath lateral or posterior and enter the cavity with a blunt '
                      'clamp or finger, not a blade.'],
                     ['Obtain cultures',
                      'Getting pus for culture is one of the aims of surgery. Send it for aerobic and '
                      'anaerobic culture; these infections are usually polymicrobial with oral and dental '
                      'flora. Add fungal and mycobacterial cultures in immunocompromised patients, or when '
                      'spinal tuberculosis (Pott disease) with a cold prevertebral abscess is possible. Send '
                      'tissue as well as pus if necrosis is present.'],
                     ['Break up loculations and irrigate',
                      'Open every pocket with a finger or blunt instrument, following extensions shown on CT '
                      'into adjacent spaces, then irrigate the cavity copiously. Avoid deep blind clamping '
                      'toward the carotid sheath and cranial nerves IX–XII.'],
                     ['Debride necrotizing fasciitis aggressively',
                      'If fascia is gray, nonbleeding and liquefied, debride back to bleeding, viable tissue '
                      'while preserving vital nerves and vessels. Mortality approaches 20–30% even with '
                      'treatment, so expect critical care support and a planned return to the operating room '
                      'for a second look.'],
                     ['Address mediastinal extension',
                      'Spread along the retropharyngeal, danger and prevertebral planes reaches the '
                      'mediastinum. Upper mediastinal collections can be drained through the neck. Involve '
                      'thoracic surgery and strongly consider thoracotomy or a thoracoscopic approach when '
                      'disease extends below the upper mediastinum or into more than one mediastinal '
                      'compartment.'],
                     ['Treat Lemierre syndrome and the source',
                      'Drain any collection in septic internal jugular vein thrombophlebitis; ligate or '
                      'excise the vein if the course worsens despite medical treatment or an abscess forms. '
                      'Remove the cause in the same sitting where possible: odontogenic disease, the most '
                      'common source in adults (often the lower second or third molar), or a pharyngeal or '
                      'salivary source.'],
                     ['Leave dependent drainage',
                      'Place a soft drain (Penrose or similar) from the deepest part of the cavity out '
                      'through the most dependent part of the wound, secured away from the great vessels. '
                      'Close the skin loosely or leave it partly open so the cavity keeps draining.'],
                     ['Decide on the airway and aftercare',
                      'At the end, choose extubation, staying intubated in intensive care, or tracheostomy, '
                      'based on edema and the spaces involved. Continue intravenous antibiotic treatment for '
                      'the infection and narrow it to the culture results. Repeat imaging if the patient is '
                      'not improving within 48–72 hours. Watch for mediastinitis (spreading swelling, chest '
                      'pain), septic jugular thrombophlebitis and carotid erosion or sentinel bleeding.']],
 'four-gland': [['Confirm the indication',
                 'Bilateral exploration needs a clear biochemical diagnosis of primary, secondary (renal) or '
                 'tertiary hyperparathyroidism; exclude familial hypocalciuric hypercalcemia first with a '
                 'urine calcium-to-creatinine clearance ratio. Typical reasons to explore both sides are '
                 'negative or discordant localization or likely multigland disease: secondary disease on '
                 'dialysis, tertiary disease after transplant, lithium use, familial isolated disease, MEN 1 '
                 'and MEN 2A.'],
                ['Review imaging and the thyroid',
                 'Have every study in the room. Small adenomas, deep posterior superior glands and '
                 'coexisting thyroid nodules are common causes of negative scans. Check the ultrasound for '
                 'thyroid nodules that may need concurrent lobectomy or thyroidectomy, and consent the '
                 'patient for it, along with failure to cure, voice change, bleeding and '
                 'hypoparathyroidism.'],
                ['Anesthesia and positioning',
                 'General anesthesia is usual. Local anesthesia with sedation and cervical plexus blocks is '
                 'possible, but take care with bilateral blocks, since spread to the phrenic nerves (mainly '
                 'a deep-block problem) can weaken both hemidiaphragms. Position supine or semi-upright with '
                 'mild neck extension. Recurrent laryngeal nerve monitoring with an EMG tube is commonly '
                 'used for bilateral work. Mark a symmetric skin crease.'],
                ['Incision and flaps',
                 'Make a 3 to 4 centimeter transverse incision about 1 to 2 centimeters below the cricoid; '
                 'lengthen it for high body mass index or a coexisting goiter. Divide platysma and raise the '
                 'avascular subplatysmal flaps superficial to the anterior jugular veins.'],
                ['Midline and a dry field',
                 'Separate the strap muscles along the midline raphe, which is nearly bloodless; cauterize '
                 'the small vessels that sometimes cross it, mostly near the top by the thyroid cartilage. '
                 'The first aim is to expose landmarks in a dry field, not to hunt for the adenoma, because '
                 'blood-stained tissue makes parathyroid, fat and lymph node look the same.'],
                ['Mobilize the thyroid lobe',
                 'Lift sternohyoid and sternothyroid off the lobe; in a short neck, divide the upper '
                 'sternothyroid insertion to free the superior pole. Divide the middle thyroid vein, which '
                 'may be absent, tiny or multiple, and free the entire lateral border from the superior pole '
                 'down to the lateral edge of the thyrothymic ligament, then rotate the lobe medially off '
                 'the carotid.'],
                ['Isolate the thyrothymic ligament',
                 'Separate it anterolaterally from the sternohyoid and posteriorly from the level VI nodal '
                 'tissue so it is clean and intact. This is the key step for not missing an inferior '
                 'parathyroid that has descended low into the ligament or upper thymus.'],
                ['Expose the landmark trio',
                 'Clearly identify the prevertebral fascia, the inferior thyroid artery and the recurrent '
                 'laryngeal nerve. With the dorsal lobe surface exposed, most glands, and particularly '
                 'enlarged ones, are now visible without further dissection.'],
                ['Superior gland first',
                 'It is the most constant in location and quickest to find: usually within a centimeter of '
                 'the cricothyroid joint, near where the inferior thyroid artery crosses the nerve, and '
                 'dorsal to the nerve. A normal superior gland shows what normal looks like in this patient. '
                 'If absent, look posteriorly in the para or retroesophageal space; an intercricothyroid '
                 'gland may need upper pole vessel division.'],
                ['Inferior gland',
                 'Typically caudal to the inferior thyroid artery, ventral to the recurrent nerve and '
                 'lateral to the midline. If not found, suspect a flat gland lying under the thyroid capsule '
                 'at the lower pole, or a low gland within the thyrothymic ligament; trace the ligament '
                 'downward.'],
                ['Repeat on the other side',
                 'Perform the same mobilization, ligament isolation, landmark exposure and '
                 'superior-then-inferior survey on the contralateral side. Account for all four glands, '
                 'judging size, color and consistency, before removing anything; handle normal glands '
                 'minimally to preserve their blood supply.'],
                ['Resect only abnormal glands',
                 'Remove the enlarged gland or glands with their pedicle controlled, leaving normal, '
                 'well-perfused glands undisturbed. Send resected tissue for frozen section if its identity '
                 'is in doubt, for example a possible lymph node or thyroid nodule.'],
                ['Four-gland hyperplasia: build the remnant first',
                 'When all four glands are abnormal, a subtotal resection leaves a remnant about the size of '
                 'a normal gland on its pedicle; make it and confirm it stays viable before removing the '
                 'other three. Mark it with a long nonabsorbable suture for any future surgeon. Total '
                 'parathyroidectomy with forearm or SCM autotransplant is an alternative, especially in '
                 'renal disease; cryopreserve tissue if available.'],
                ['Dedicated search for a missing gland',
                 'Check the descended superior gland in the paraesophageal or retroesophageal space by the '
                 'nerve, a gland just medial to the superior pole, a low inferior gland in the thymus, and '
                 'the carotid sheath up to the bifurcation for an undescended gland. Behind the tubercle of '
                 'Zuckerkandl a low superior adenoma can mimic it. Consider an intrathyroidal gland: '
                 'ultrasound the lobe or remove it on the missing side.'],
                ['Renal and hereditary disease',
                 'Supernumerary glands occur in up to about one in ten patients, mostly inferior glands in '
                 'or near the thymus. Explore carefully around the lower pole and perform a transcervical '
                 'thymectomy to reduce recurrence; in MEN 1, subtotal parathyroidectomy with transcervical '
                 'thymectomy is the preferred operation.'],
                ['Intraoperative PTH',
                 'The atlas finds no good evidence for intraoperative PTH once all four glands are '
                 'positively identified, and warns that it adds cost and may prompt needless exploration. '
                 'Many US surgeons still use it during bilateral exploration, especially for multigland '
                 'disease, subtotal resection or when fewer than four glands are found, to confirm enough '
                 "tissue was removed. Know your institution's criterion."],
                ['Know when to stop',
                 'After a competent bilateral search, failure to find the adenoma should be rare, under '
                 'about 3 percent. Stop rather than continue tissue-damaging dissection; reconsider the '
                 'diagnosis, especially familial hypocalciuric hypercalcemia if glands look normal, then '
                 'relocalize and plan targeted reoperation, since major ectopia is often unreachable through '
                 'a cervical incision.'],
                ['Hemostasis, closure and aftercare',
                 'Achieve full hemostasis and, if monitoring was used, confirm both recurrent nerves still '
                 'stimulate. Drains are not needed. Close straps, platysma and skin, and watch for neck '
                 'swelling for several hours. Hypocalcemia, usually at 48 to 72 hours, is more likely after '
                 'removing more than two glands, reoperation, added thyroidectomy, or very high calcium, PTH '
                 'or alkaline phosphatase; discharge these patients on supplements.']],
 'free-flap-basics': [['Define the defect, not the flap',
                       'The cancer decides how much is resected; never shape the resection around a '
                       'preferred flap. For each defect list what is missing: lining, skin cover, bone, '
                       'bulk, and dead space. Note the functional goals of speech, swallowing, oral '
                       'competence, and protection of the great vessels. Choose the most effective flap '
                       'directly rather than climbing a reconstructive ladder.'],
                      ['Match tissue to subsite',
                       'Oral cavity defects need a thin, pliable fasciocutaneous flap (MSAP, thin ALT, or '
                       'RFF) with a 4 to 6 cm paddle and a short pedicle. Subtotal or total glossectomy '
                       'needs bulk such as ALT, keeping in mind that muscle atrophies after radiation. A '
                       'circumferential pharyngeal defect needs a paddle about 9.4 cm wide to tube to a 3 cm '
                       'lumen.'],
                      ['Decide whether bone is required',
                       'Ask four questions. Is the patient dentate? Is the defect anterior to the mental '
                       'foramen? Is the soft tissue poor or irradiated? Is postoperative radiation likely? '
                       'Anterior continuity defects must be rebuilt with vascularized bone. A plate alone '
                       'across a continuity gap tends to expose or fracture, especially after radiation. Use '
                       'virtual planning with cutting guides and pre-bent or custom plates.'],
                      ['Screen the donor site preoperatively',
                       'Use the nondominant arm for a radial forearm flap after an Allen test, with duplex '
                       'if it is equivocal. For a fibula, get CT or MR angiography to rule out peronea '
                       'magna, which is an absolute contraindication. Avoid ALT on a side with a hip or knee '
                       'replacement, MSAP with varicose veins, and iliac crest (DCIA) with chronic cough. '
                       'Plan a second-choice flap.'],
                      ['Run an expanded team checklist',
                       'Beyond the standard surgical safety checklist, confirm the airway plan during and '
                       'after surgery, the ablative plan, and the donor site with its laterality and prep. '
                       'Also confirm the contingency flap, tourniquet use and pressure, and that planning '
                       'models are in the room with someone who can explain them. Warm the patient from '
                       'before induction and keep fluids euvolemic.'],
                      ['Select the recipient artery',
                       'Ask the resecting surgeon early to preserve vessel length. Prefer medial branches of '
                       'the external carotid. The superior thyroid artery lies best, while the facial and '
                       'lingual arteries usually have better caliber. In a vessel-depleted neck use the '
                       'transverse cervical artery or the contralateral neck. Without a neck dissection, '
                       'expose the facial artery through a 3 cm incision at the mandibular border, or use '
                       'the superficial temporal artery.'],
                      ['Select the recipient vein',
                       'First choice is a large internal jugular vein (IJV) tributary such as the common '
                       'facial or superior thyroid vein. Next is end-to-side onto the IJV, or the external '
                       'jugular vein, which compresses easily and needs careful postoperative positioning. '
                       'In a depleted or salvage neck, consider the transverse cervical vein, a vein graft '
                       'to the opposite side, a cephalic vein turnover, or the internal mammary vein.'],
                      ['Plan pedicle reach',
                       'After prior free flaps, radiation, or neck dissection, choose a flap with a long '
                       'pedicle to reach vessels outside the scarred field. ALT pedicles commonly run 10–12 '
                       'cm; a fibula pedicle lengthens when proximal bone is discarded. Reach matters most '
                       'for the maxilla, where nearby recipients are scarce. If length falls short, plan '
                       'vein grafts, cephalic vein transposition, or an arteriovenous loop.'],
                      ['Harvest an anterolateral thigh flap',
                       'Mark a line from the anterior superior iliac spine to the lateral patella; most '
                       'perforators lie within 3 cm of its midpoint, and a handheld Doppler confirms them. '
                       'Open along the medial edge of the planned paddle, go beneath the fascia, and look '
                       'laterally for perforators. If none are suitable, look higher for a tensor fascia '
                       'lata perforator, use an anteromedial thigh flap, or switch legs.'],
                      ['Harvest a radial forearm or calf perforator flap',
                       'For the radial forearm, start the paddle about 1 cm proximal to the wrist crease and '
                       'include the cephalic vein. Dissect suprafascially toward the flexor carpi radialis '
                       'and brachioradialis, and peel superficial radial nerve branches off the paddle. For '
                       'an MSAP, mark perforators by Doppler with the patient standing, about 10 to 15 cm '
                       'below the fibular head. Then incise 2 to 3 cm anterior to them.'],
                      ['Harvest a fibula flap',
                       'Flex the hip and knee and rotate the leg internally. Mark the fibular head and '
                       'lateral malleolus, and leave 6 cm of bone at each end to protect the common peroneal '
                       'nerve and the syndesmosis. Use the contralateral leg when the skin paddle will line '
                       'the mouth. Dissect subfascially to the posterior septum and keep a muscle cuff on '
                       'the bone to protect the periosteum.'],
                      ['Find the peroneal pedicle safely',
                       'Enter the anterior compartment close to the bone. Protect the anterior tibial '
                       'vessels and deep peroneal nerve there, which can be mistaken for the pedicle. Take '
                       'extensor muscles off the interosseous membrane, cut the bone with the pedicle '
                       'shielded behind it, then incise the membrane. Split tibialis posterior to follow the '
                       'peroneal vessels up to the posterior tibial bifurcation, and ligate large soleal '
                       'branches.'],
                      ['Harvest other bone flaps',
                       'For scapula, use lateral decubitus positioning and find the circumflex scapular '
                       'vessels in the triangular space. Finish the pedicle dissection before any osteotomy, '
                       'and reattach teres major at closure. For iliac crest (DCIA), protect the ascending '
                       'branch and lateral femoral cutaneous nerve, and repair the abdominal wall with mesh. '
                       'Osteocutaneous radial forearm bone is limited to 40% of the radius circumference, '
                       'with prophylactic plating.'],
                      ['Divide the pedicle and close the donor site',
                       'Ligate the pedicle as close to its parent vessel as possible to gain length and '
                       'caliber, and divide it only once the recipient vessels are prepared. Shape the bone '
                       'to the plan and fix it to the plate. Close the donor site primarily when the tension '
                       'allows, otherwise skin graft. Quilt back donor sites to reduce seroma.'],
                      ['Perform the microvascular anastomoses',
                       'Lay out the flap and pedicle first so the vessels run without twist, kink, or '
                       'tension. Trim donor and recipient vessels back to healthy intima and remove loose '
                       'adventitia without injuring the wall. Then complete the venous and arterial '
                       'anastomoses under magnification; many US surgeons use a coupler for the vein. Some '
                       'teams give a small intravenous heparin bolus if an arterial anastomosis must be '
                       'redone.'],
                      ['Confirm perfusion and place monitoring',
                       'After releasing the clamps, check flap color, capillary refill, and dermal bleeding, '
                       'and listen with a Doppler. Consider an implantable Doppler on the artery, the vein, '
                       'or both. For buried or intraoral flaps, a small de-epithelialized monitoring patch, '
                       'or an exteriorized loop for jejunum, makes bedside checks possible. In bony flaps, '
                       'the skin can fail while the bone survives.'],
                      ['Inset and protect the pedicle',
                       'Inset oropharyngeal flaps through the neck as far as possible and parachute the '
                       'remainder into place. In pharyngeal repair, make the closure watertight and cover '
                       'the great vessels with vascularized tissue. Keep the pedicle away from plate edges '
                       'and drains. Secure the tracheostomy with sutures rather than tapes, or keep any tie '
                       'very loose, so nothing presses on the pedicle.'],
                      ['Hand off a flap-protective postoperative plan',
                       'Most thromboses occur in the first 3–5 days, so check the flap hourly for the first '
                       '24–48 hours in an ICU or trained flap unit and re-explore promptly for any change. '
                       'Nurse head-up, avoid neck ties, keep the patient warm, target hematocrit around '
                       '25–30% and urine output 0.5–1 mL/kg/h, start VTE prophylaxis, and mobilize early.']],
 'free-flap-takeback': [['Recognize compromise early',
                         'Check color, temperature, swelling or turgor, and capillary refill. Prick the skin '
                         'with a 25 to 30 gauge needle: rapid dark bleeding suggests venous congestion, and '
                         'no bleeding suggests arterial inflow failure. Use a handheld Doppler as an '
                         'adjunct. Loss of an implantable Doppler signal is a strong warning, although these '
                         'devices produce more false alarms.'],
                        ['Interpret the signs in context',
                         'Most thromboses happen in the first 3 to 5 days, and venous problems outnumber '
                         'arterial ones. Early failures in bony flaps tend to be arterial and later ones '
                         'venous. For intraoral flaps, check the de-epithelialized patch. In a fibula, the '
                         'skin paddle can die from perforator thrombosis while the main pedicle and bone '
                         'stay alive, so assess the pedicle directly.'],
                        ['Act on suspicion, not certainty',
                         'Salvage succeeds more often the sooner compromise is caught. Once a flap looks '
                         'threatened, go straight to the operating room for exploration rather than waiting '
                         'for more tests. Make sure ward staff know they can call surgeons at once, and log '
                         'when the change was first noticed.'],
                        ['Relieve external compression at the bedside',
                         'While the OR is being arranged, check for tight tracheostomy tapes, dressings, or '
                         'ties around the neck. Correct head rotation or flexion that kinks the pedicle, and '
                         'sit the patient up to about 45 degrees. A tense hematoma threatening the flap or '
                         'airway may need sutures released right away.'],
                        ['Prepare for every salvage outcome',
                         'Before going back, plan for vein grafts and for a second flap if the first cannot '
                         'be saved. Waiting to reconstruct later is rarely an option in head and neck '
                         'defects. Consent for a new free flap or a pedicled flap such as pectoralis major. '
                         'Choose a donor site and have the microscope and microvascular instruments ready.'],
                        ['Secure the airway and position',
                         'Use the existing tracheostomy or confirm a safe intubation plan before reopening. '
                         'Lay the neck in a position that does not stretch or twist the pedicle while you '
                         'work. Keep the patient warm and euvolemic during the procedure to support flap '
                         'perfusion.'],
                        ['Reopen and evacuate',
                         'Open the neck incision and remove any hematoma and clot gently, without pulling on '
                         'the pedicle. Find the bleeding source and control it. Then follow the pedicle from '
                         'the flap to the recipient vessels along its whole course before touching the '
                         'anastomoses.'],
                        ['Correct mechanical causes first',
                         'Look for a twisted or kinked pedicle, compression by a plate edge or the mandible, '
                         'a drain lying on the vessels, or an inset or skin closure that is too tight. Fix '
                         'each problem you find, then reassess flow before deciding the anastomosis itself '
                         'has failed.'],
                        ['Assess artery and vein separately',
                         'Check arterial pulsation and the outflow from the vein. Use a patency test or '
                         'Doppler on each limb to locate the problem: an engorged, dark flap with good '
                         'inflow points to the vein, while a pale flap with no pulse points to the artery.'],
                        ['Remove thrombus and revise',
                         'Take down the thrombosed anastomosis and clear clot completely from the vessel and '
                         'the flap side, using gentle milking or a fine embolectomy catheter. Irrigate the '
                         'lumen with heparinized saline, and trim back to healthy, undamaged intima rather '
                         'than resewing onto injured wall. A systemic heparin bolus is commonly given before '
                         'revising the arterial anastomosis.'],
                        ['Change the recipient vessel or bridge the gap',
                         'If the original vessel is poor or the geometry is still unsafe, move to a fresh '
                         'recipient. For the vein, options are an end-to-side anastomosis onto the internal '
                         'jugular vein, the transverse cervical vein, or a vein graft to the contralateral '
                         'neck. A cephalic vein turnover or the internal mammary vein are last resorts. On '
                         'the arterial side, consider the transverse cervical artery or the contralateral '
                         'neck.'],
                        ['Use adjuncts only by protocol',
                         'Consider intra-arterial thrombolytics or topical vasodilators only after the '
                         "mechanical or technical cause is corrected, and only within your unit's salvage "
                         'protocol, since thrombolytics raise bleeding risk. Routine postoperative aspirin '
                         'has not been shown to improve flap survival and may add complications, so do not '
                         'rely on it to rescue a failing flap.'],
                        ['Confirm durable reperfusion, or convert',
                         'After revising, watch the flap long enough to see sustained bleeding, color, and '
                         'Doppler flow. If the flap is clearly dead, debride it and reconstruct the same day '
                         'with a second free flap or a pedicled pectoralis major flap. This matters '
                         'especially when the great vessels or the mouth-to-neck seal are exposed.'],
                        ['Re-inset, close, and resume monitoring',
                         'Re-inset the flap so the repaired pedicle runs a protected course, and close '
                         'loosely enough that swelling does not compress it. Avoid ties around the neck. '
                         'Restart hourly flap checks for at least 24 to 48 hours. Document the vessels used, '
                         'the ischemia time, and the anticoagulation plan, and keep a very low threshold to '
                         're-explore.']],
 'neck-dissection': [['Position and plan the extent',
                      'Supine with a shoulder roll and the neck extended and turned away; a 30-degree '
                      'head-up tilt lowers venous bleeding. Turning the table away from anesthesia frees '
                      'room for both teams and any extra equipment. Confirm which levels are planned before '
                      'incision, because a selective dissection removes only the at-risk levels and every '
                      'later step is optional by plan.'],
                     ['Choose the incision',
                      'For a unilateral selective dissection, a curved incision in a skin crease from over '
                      'the sternocleidomastoid (SCM) toward the midline is usual; a short 4–5 cm scar can '
                      'suit a thin neck with lax skin. Bilateral work suits an apron incision from mastoid '
                      'to mastoid, crossing a few centimeters above the sternal notch. Level V needs a '
                      'posterior limb. Plan around old scars and reconstruction.'],
                     ['Raise subplatysmal flaps',
                      'Elevate flaps just under platysma so the skin keeps its blood supply: up to the lower '
                      'border of the mandible, down to the clavicle, and back to trapezius if level V is '
                      'planned. The external and anterior jugular veins and the greater auricular nerve '
                      'should stay on the deep side of your plane. Behind the SCM, CN XI is very superficial '
                      'and easily cut.'],
                     ['Strip the fascia off the SCM',
                      'Incise the investing fascia longitudinally along the muscle, staying in front of the '
                      'greater auricular nerve; the transverse cervical nerve is sacrificed. Hold the fascia '
                      'medially under steady tension and peel it with a #10 blade through this largely '
                      'avascular plane, coagulating perforators on the deep surface. CN XI enters the deep '
                      'surface near the junction of the upper and middle thirds.'],
                     ['Clear level Ia when planned',
                      'Lift submental fibrofatty tissue off both anterior digastric bellies, off the '
                      'mandibular symphysis above and off mylohyoid deep, clipping the submental vessels and '
                      'sweeping the packet down toward the hyoid. Elevating the specimen sharply off the '
                      'infrahyoid muscles can open an anterior jugular vein, which bleeds troublesomely if '
                      'not anticipated.'],
                     ['Protect the marginal mandibular nerve in level Ib',
                      'The marginal branch travels in the fascia covering the submandibular gland, below the '
                      "mandible near the facial vessels. Incise that fascia low along the gland's lower "
                      'border. Tie and cut the facial vein low, leave the upper tie long, and use it to lift '
                      'the fascia and nerve upward toward the mandible (the Hayes Martin maneuver), keeping '
                      'the nerve out of the field.'],
                     ['Clear the submandibular triangle',
                      'Divide the facial artery at the upper border of the gland. Clean the lateral face of '
                      'mylohyoid, tying the ranine veins before cutting them so they cannot retract and '
                      'bleed. Retract mylohyoid forward to show the lingual nerve pulled down into a V by '
                      'the submandibular ganglion. Divide the ganglion at the apex, let the nerve rise away, '
                      'then tie and cut Wharton duct.'],
                     ['Finish level Ib and save recipient vessels',
                      'Pull the gland down, find the proximal facial artery as it emerges beneath the '
                      'posterior digastric belly and ligate it again. The hypoglossal nerve enters the lower '
                      'fossa deep to the digastric; keep it in view. If free-flap reconstruction is planned, '
                      'freeing the artery off the gland gains 1–3 cm; preserve common facial vein, external '
                      'jugular vein and superior thyroid artery.'],
                     ['Open the upper limit of level II',
                      'Cut the fascia covering the posterior digastric and release the stylomandibular '
                      'ligament to open the top of the field. Tie the retromandibular, posterior auricular '
                      'and external jugular veins as you meet them. Remove no more than the lowest tip of '
                      'the parotid, since a larger excision worsens facial swelling. Retract the digastric '
                      'up and the SCM back to expose level II.'],
                     ['Expose CN XI',
                      'Level II has no fascial plane, so use scissors to open a tunnel through the fat along '
                      'the nerve from the SCM back to the internal jugular vein (IJV). The nerve usually '
                      'crosses lateral to the vein but can pass deep to it or even through it; the palpable '
                      'C1 transverse process marks the crossing. Handle the nerve minimally, since even mild '
                      'trauma causes shoulder pain and weakness.'],
                     ['Clear level IIb under the nerve',
                      'Dissect the tissue above and behind CN XI down to the prevertebral fascia over '
                      'splenius capitis and levator scapulae, controlling the occipital artery or its SCM '
                      'branch when needed. Free it from the lateral wall of the IJV, then pass the packet '
                      'beneath the lifted nerve so levels I–II come down in continuity. Avoid traction '
                      'injury while doing this.'],
                     ['Set the inferior limit of levels III–IV',
                      'With SCM held laterally and omohyoid pulled down, expose the lower IJV and cut '
                      'through the fibrofatty tissue with scissors, freeing it from the SCM laterally and '
                      'the vein medially. Divide it horizontally around the clavicle level. Preserve the '
                      'transverse cervical vessels; watch for a high-riding subclavian vein and, on either '
                      'side, thoracic or right lymphatic duct branches.'],
                     ['Release the deep floor and posterior strip',
                      'Retract SCM laterally and free the remaining posterior attachment. Stay superficial '
                      'to the prevertebral fascia, above the cervical rootlets, to spare the phrenic nerve '
                      'on anterior scalene and the brachial plexus between the scalenes. Cut the anterior '
                      'sensory branches but keep the deep C2–C4 contributions to CN XI and phrenic nerve. '
                      'Stop at the carotid sheath; the sympathetic trunk lies medial.'],
                     ['Peel the carotid sheath',
                      'With the packet retracted medially, open the sheath over the vagus with a fresh #10 '
                      'blade and stroke it off the IJV with the edge angled away from the wall; Kittner or '
                      'gauze blunt dissection is an alternative. Securely ligate the four to six '
                      'tributaries, since a missed one causes postoperative hemorrhage. Traction folds the '
                      'vein at the top and bottom ends, where it is easily nicked.'],
                     ['Finish medially and at the straps',
                      'Continue over the carotid, keeping the specimen inclusive of nodes behind the vein. '
                      'Protect the hypoglossal nerve crossing the carotids high and preserve the superior '
                      'thyroid and superior laryngeal arteries. Open the strap fascia in the midline and '
                      'work lateral, freeing sternohyoid and omohyoid and tying the anterior jugular and any '
                      'communicating vein; this step may be done earlier if convenient.'],
                     ['Clear level V when planned',
                      'Find CN XI in the posterior triangle where it exits the posterior SCM border, roughly '
                      '1 cm above Erb point where the great auricular nerve wraps the muscle. Dissect along '
                      'the nerve to trapezius, then sweep the fibrofatty tissue off splenius, levator '
                      'scapulae and the scalenes, staying above the prevertebral fascia. Preserve the '
                      'transverse cervical vessels and pass the packet beneath the nerve to join levels '
                      'II–IV.'],
                     ['Convert when the selective plan fails',
                      'Fixed nodes, suspected extranodal spread through fascia, or a previously operated or '
                      'irradiated neck without reliable planes call for a broader dissection. A modified '
                      'radical dissection clears levels I–V but keeps one or more of CN XI, the internal '
                      'jugular vein and the SCM. A classic radical dissection removes all three: '
                      'suture-ligate the vein high and low, divide the SCM and resect the nerve.'],
                     ['Check the low neck for chyle and vessel injury',
                      'Ask for a sustained Valsalva and inspect deep left level IV and the right venous '
                      'angle; clear rather than milky fluid can be chyle in a fasted patient. Oversew a leak '
                      'now with nonabsorbable suture and fibrin sealant. Repair any great-vessel tear with '
                      'vascular suture; for an IJV hole, compress above and below to prevent air embolism.'],
                     ['Inspect, deliver and close',
                      'Before closing, confirm the preserved structures are intact: CN XI (stimulate if a '
                      'monitor is used), vagus, hypoglossal and marginal mandibular nerves, and a nonleaking '
                      'internal jugular vein. Tag the specimen by level and laterality for pathology. '
                      'Irrigate, look for bleeding and retained sponges, place a suction drain on each '
                      'operated side, close platysma then skin, and apply light supraclavicular pressure.']],
 'oral-composite': [['Airway plan and anesthesia setup',
                     'Nasotracheal intubation is preferred so the mouth is free and occlusion can be '
                     'checked. Pre-existing trismus or a distorted, bleeding airway calls for awake '
                     'fiberoptic intubation or awake tracheostomy. Ask anesthesia to avoid long-acting '
                     'paralysis so facial, lingual, and hypoglossal branches can still be stimulated during '
                     'the soft-tissue approach. Give intravenous steroids before incision.'],
                    ['Confirm the bony plan',
                     'Review contrast CT for cortical erosion and MRI for marrow or perineural spread along '
                     'the lingual or inferior alveolar nerve. Marginal resection fits tumor that abuts bone '
                     'without erosion. Choose segmental resection for CT erosion, tumor arising in bone, '
                     'tooth-root involvement, or an edentulous or atrophic mandible. Have virtual surgical '
                     'planning guides and a pre-bent plate ready when occlusion is distorted.'],
                    ['Design the incision',
                     'Bilateral necks get an apron incision at least two fingerbreadths below the mandible. '
                     'A unilateral case can use a midline chevron lip split, which gives the most direct '
                     'exposure for buccal, retromolar, masticator, or oropharyngeal extension. The '
                     'alternative is carrying the crease incision across the midline so the flap lifts over '
                     'the jaw. Counsel the patient about lip-split scarring.'],
                    ['Handle involved skin',
                     'If tumor reaches the skin, include a skin island with the specimen and send its '
                     'circumferential margins at the start. Expect to sacrifice the marginal mandibular '
                     'branch in this situation. Bring the neck incision to the edge of the skin excision at '
                     'a right angle. A crease-friendly incision matters less than keeping the remaining skin '
                     'perfused.'],
                    ['Raise flaps and protect the marginal nerve',
                     'Raise the upper flap just deep to platysma up to the lower mandibular border. The '
                     'marginal mandibular branch runs on the deep cervical fascia over the submandibular '
                     'gland, so keep that fascia down, or incise it low and lift it upward with the ligated '
                     'facial vein (Hayes Martin maneuver). With a lip split, identify the nerve and lift it '
                     'above the mandibular border.'],
                    ['Level I dissection and vessel preservation',
                     'Dissect level I first, sparing the marginal mandibular, lingual, and hypoglossal '
                     'nerves when oncologically safe. With deep floor-of-mouth spread, leave level Ib '
                     'attached so it comes out en bloc with the mandible. When a free flap is planned, save '
                     'long segments of the facial artery and the common facial and external jugular veins '
                     'for the microvascular team.'],
                    ['Expose the outer mandible',
                     'Retract superiorly with gauze and incise periosteum along the inferior border with '
                     'needle-tip cautery. Strip subperiosteally only where the buccal cortex is tumor-free. '
                     'Elsewhere, leave a soft-tissue cuff on the specimen as the buccal margin. Release '
                     'masseter with cautery for hemostasis, and expose only the bone needed for plating '
                     'because periosteum feeds the cortex.'],
                    ['Intraoral exposure and buccal mucosal cuts',
                     'Place a cheek retractor and a side bite block. Mark mucosal cuts 1 to 1.5 cm around '
                     'the tumor with the tongue relaxed, and plan osteotomies at least 1 cm from it. Extract '
                     'teeth that sit on the osteotomy lines. Make labial and buccal cuts with protected '
                     'needle cautery, but save the lingual and floor-of-mouth cuts until the bone is free.'],
                    ['Preplate when the buccal cortex allows',
                     'Contour a 2.0 to 2.5 mm reconstruction plate to the lower border so that at least '
                     'three bicortical screws sit on each side of the planned defect. Leave one spare hole '
                     'on each side in case the margin has to grow. Drill, place measured screws, then remove '
                     'the plate and keep the screws in order so they can go back in the same holes.'],
                    ['Hold occlusion when preplating is impossible',
                     'When the buccal cortex is involved, use intermaxillary fixation screws if dentate '
                     'segments remain on both sides. Otherwise apply an external fixator with two pins on '
                     'each side of the defect, placed so they stay clear of the later plate and screw holes. '
                     'Alternatively, use virtual-planning cutting guides with a model-bent or custom plate.'],
                    ['Make the osteotomies',
                     'Cut with an oscillating saw under constant irrigation. Expect brisk inferior alveolar '
                     'artery bleeding and control it with cautery or bone wax. For a marginal (rim) '
                     'resection, leave at least 1 cm of mandibular height, with the cut just above the '
                     'inferior alveolar canal, and round the corners to avoid stress points that fracture. '
                     'If marrow involvement appears, convert to a segmental resection.'],
                    ['Lingual cuts and lingual nerve',
                     'Retract the freed bone segment to put tension on the floor of mouth and tongue, then '
                     'cut the lingual mucosa with 1 to 1.5 cm margins. When floor-of-mouth involvement is '
                     'substantial, divide the lingual nerve and send its proximal end for frozen section. If '
                     'that margin is positive, follow the nerve toward the infratemporal fossa and '
                     're-margin. Then divide the floor-of-mouth contents and mylohyoid.'],
                    ['Deep margin and hypoglossal nerve',
                     'In anterior floor-of-mouth and mandible disease, take mylohyoid as the deep margin. '
                     'Find the hypoglossal nerve proximally in the neck and follow it forward over '
                     'hyoglossus, dividing mylohyoid above it to keep it safe. Resect it with a proximal '
                     'frozen margin if tumor involves it. Then release genioglossus and the anterior '
                     'digastric to deliver the specimen.'],
                    ['Posterior and parotid extension',
                     'For ramus, coronoid, or condyle resection, free the medial and lateral pterygoids and '
                     'detach temporalis from the coronoid. Keep the condylar head unless oncology requires '
                     'it, because it supports the glenoid fossa. If it goes, plan resuspension or '
                     'soft-tissue-only repair. With buccal soft tissue over the ramus, trace a buccal branch '
                     'back to the facial nerve trunk before dividing masseter.'],
                    ['Specimen orientation and margins',
                     'Inspect the specimen for a cuff of normal tissue at every mucosal and deep surface. '
                     'Take frozen margins from the specimen rather than the wound bed, and re-resect from '
                     'the patient wherever a margin looks close. Consider marrow cytology for bony margin '
                     'assessment. Orient the specimen for the pathologist yourself, aiming for final margins '
                     'wider than 5 mm.'],
                    ['Use the frozen-section wait',
                     'While frozens are pending, finish the neck dissections and prepare recipient vessels. '
                     'Replace the preplated plate in its original holes, or bend a new plate to the planned '
                     'neomandible contour before removing the external fixator. Start bony reconstruction '
                     'only after margins are confirmed negative and the necks are complete. This saves time '
                     'for the reconstructive team.'],
                    ['Reconstruct, drain, and decide on tracheostomy',
                     'Defects anterior to the mental foramen need vascularized bone to prevent an Andy Gump '
                     'deformity. Use thin, pliable lining so the tongue is not tethered, and seal the mouth '
                     'from the neck to prevent orocervical fistula. Place lateral neck suction drains and a '
                     'nasogastric tube. Tracheostomy is favored for anterior mandibulectomy, bulky or '
                     'oropharyngeal reconstruction, trismus, or withdrawal risk.'],
                    ['Final checks before leaving the room',
                     'Confirm occlusion, hemostasis in the oral cavity and neck, flap perfusion, and a '
                     'secure airway with a clear overnight plan before the drapes come down. For small '
                     'lateral defects, extubation at the end or overnight nasotracheal intubation can be a '
                     'safe alternative to tracheostomy.']],
 'parathyroidectomy': [['Confirm candidacy for a focused approach',
                        'Require a firm biochemical diagnosis and concordant localization, usually '
                        'ultrasound plus sestamibi or four-dimensional CT pointing to the same gland. Review '
                        'the images yourself for side and depth. Negative or discordant studies, or a likely '
                        'multigland setting such as lithium use, familial disease or MEN, call for bilateral '
                        'exploration. Thyroid nodules can cause false-positive sestamibi uptake.'],
                       ['Anesthesia and baseline PTH',
                        'General anesthesia, or local with sedation and a superficial cervical plexus block '
                        'on the target side. Draw a baseline intraoperative PTH before incision or before '
                        'manipulating the gland. Recurrent laryngeal nerve monitoring with an '
                        'electromyographic tube is optional but helpful for deep posterior targets.'],
                       ['Positioning and marking',
                        'Place the patient supine or semi-upright with mild neck extension. Mark a symmetric '
                        'low skin crease about 1 to 2 centimeters below the cricoid, positioned so the '
                        'focused incision can be lengthened into a standard bilateral exploration incision '
                        'if localization fails.'],
                       ['Incision and flaps',
                        'Make a short transverse incision, divide platysma, and raise limited subplatysmal '
                        'flaps superficial to the anterior jugular veins, just enough to expose the target '
                        'side, preserving the option to extend the exposure across the midline later.'],
                       ['Midline entry and strap mobilization',
                        'Open the bloodless midline raphe, controlling small crossing vessels near the '
                        'thyroid cartilage. Lift the sternohyoid and sternothyroid off the lobe on the '
                        'target side; dividing the upper sternothyroid insertion helps in a short neck or '
                        'for a high superior gland.'],
                       ['Rotate the lobe medially',
                        'Divide the middle thyroid vein, which may be absent or multiple, and free the '
                        'lateral border so the lobe rolls medially off the carotid to expose its dorsal '
                        'surface. Avoid stripping the thyroid capsule broadly; aim for a dry field, since '
                        'blood makes parathyroid, fat and node look alike.'],
                       ['Landmarks before the target',
                        'Identify the prevertebral fascia, the inferior thyroid artery and the recurrent '
                        'laryngeal nerve before dissecting in the tracheoesophageal groove. Knowing where '
                        'the nerve lies is what makes it safe to work around a posterior adenoma.'],
                       ['Superior adenoma',
                        'Expect it dorsal to the plane of the recurrent nerve, usually within a centimeter '
                        'of the cricothyroid joint near the artery-nerve crossing. Enlarged superior glands '
                        'frequently descend into the para or retroesophageal space, ending up behind the '
                        'nerve and the inferior thyroid artery pedicle, low enough to be mistaken for an '
                        'inferior gland. In goiter, check behind the tubercle of Zuckerkandl.'],
                       ['Inferior adenoma',
                        'Expect it caudal to the inferior thyroid artery, ventral to the nerve and lateral '
                        'to the midline, near the lower pole. If not at the pole, separate the thyrothymic '
                        'ligament from the sternohyoid and the level VI nodes and follow it down; also '
                        'consider a flat gland under the lower-pole capsule.'],
                       ['Identify the gland correctly',
                        'Distinguish the adenoma from fat, thyroid nodule and lymph node by its tan-brown '
                        'color, discrete capsule, consistency and vascular pedicle. If a normal ipsilateral '
                        "gland is seen, use it as a reference for this patient's normal glands."],
                       ['Dissect and remove intact',
                        'Develop the gland circumferentially in the plane against its capsule, staying away '
                        'from the nerve, and avoid rupturing it, since spillage can seed parathyromatosis. '
                        'Control and divide the vascular pedicle last, after the nerve is confirmed clear. '
                        'Do not devascularize a normal gland nearby.'],
                       ['Intraoperative PTH after excision',
                        'Draw PTH at set times after the gland is removed, commonly 5 and 10 minutes. The '
                        'widely used Miami criterion is a fall of more than 50% from the highest '
                        'pre-incision or pre-excision value by 10 minutes; some surgeons also require a '
                        'value back in the normal range. A slow or partial fall means keep the operation '
                        'open and consider another abnormal gland.'],
                       ['Confirm the tissue',
                        'Send the gland for frozen section, or confirm with an aspirate PTH, when its '
                        'identity is uncertain, the gland looks atypical, or the PTH fall is borderline or '
                        'slow.'],
                       ['Inadequate PTH fall: convert',
                        'Lengthen the incision and look at the second gland on the same side, then explore '
                        'the other side using the bilateral sequence. Check the descended superior position, '
                        'the space just medial to the superior pole, a low inferior gland in the thymus, the '
                        'carotid sheath and behind the tubercle of Zuckerkandl. Keep double adenoma and '
                        'four-gland hyperplasia in mind.'],
                       ['Stop rather than over-dissect',
                        'If a competent exploration does not find the culprit, end the operation instead of '
                        'causing tissue damage and nerve or parathyroid injury. Reconsider the diagnosis, '
                        'including familial hypocalciuric hypercalcemia, then relocalize; major ectopia is '
                        'the commonest cause of persistent disease and is often beyond a cervical incision.'],
                       ['Hemostasis and closure',
                        'Achieve complete hemostasis; drains are not needed. Confirm the nerve stimulates if '
                        'monitoring is used. Reapproximate the straps, platysma and skin with absorbable '
                        'sutures and a cosmetic subcuticular closure.'],
                       ['Aftercare',
                        'Observe for neck swelling for at least a few hours; same-day discharge suits '
                        'selected patients. Calcium and PTH can be checked before discharge. Patients with '
                        'very high preoperative calcium or PTH or raised alkaline phosphatase risk hungry '
                        'bone syndrome and should go home on replacement with a calcium check within two '
                        'weeks.']],
 'parotid-total': [['Plan resection and reconstruction together',
                    'Confirm the indication: deep-lobe cancer, intraparotid nodal metastasis, extensive '
                    'tumor, bulky neck disease, cutaneous metastasis to the parotid, multifocal recurrent '
                    'pleomorphic adenoma, or a high deep-lobe tumor stretching the nerve. Before incising, '
                    'have a reconstructive plan so margins are not compromised and donor nerves (greater '
                    'auricular) and recipient vessels are not sacrificed carelessly. Counsel about possible '
                    'sacrifice and reanimation.'],
                   ['Decide on nerve sacrifice before surgery where possible',
                    'Preoperative facial weakness is an absolute indication to resect the involved nerve, '
                    'except in lymphoma, which should be excluded on cytology or frozen section. Gross '
                    'infiltration along the nerve on MRI is a relative indication. A normally functioning '
                    'nerve should be preserved whenever the tumor can be peeled off it, even if microscopic '
                    'residual disease is left for postoperative radiotherapy.'],
                   ['Use facial nerve monitoring selectively but deliberately',
                    'Monitoring is especially worthwhile in revision cases, after radiotherapy, for '
                    'extensive tumors, and in radical cases where distal branches must be found and tagged '
                    'for grafting. Pooled data suggest one immediate palsy is prevented for roughly every '
                    'nine monitored patients. Avoid paralytic agents once intubated.'],
                   ['Use a modified Blair incision',
                    'For total or radical surgery, a lazy-S (modified Blair) incision, with or without a '
                    'limb behind the tragus, gives more room than a facelift incision and runs straight into '
                    'a neck dissection if needed. Include any involved skin as an ellipse left on the '
                    'specimen. Raise the flap deep to the SMAS unless the tumor reaches that layer.'],
                   ['Find and protect the greater auricular nerve',
                    'Pick it up on the SCM and follow it upward, keeping the posterior branches where '
                    'oncologically safe to limit numbness. If nerve sacrifice is possible, preserve a '
                    'generous length with its cervical plexus connections as a ready cable-graft donor.'],
                   ['Identify the trunk',
                    'Free the gland from the tragal perichondrium and the anterior SCM. Find the trunk using '
                    'the tympanomastoid suture, the most dependable landmark, together with the upper border '
                    'of the posterior digastric belly; the tragal pointer is an adjunct. For tumors arising '
                    'around the stylomastoid foramen, identify a distal branch and dissect back toward the '
                    'trunk.'],
                   ['Complete a superficial parotidectomy first',
                    'Whether the tumor is superficial or deep, begin by removing the lateral lobe (levels I '
                    'and II) and exposing every branch from the pes to the gland edge. If a neck dissection '
                    'is planned, it can be completed at this point, before the deep lobe, which also opens '
                    'the field inferiorly.'],
                   ['Microdissect the branches off the deep lobe',
                    'Under loupes with microvascular instruments, lift each branch off the deep parenchyma '
                    'so the nerve lies free above it. A small branch running into the deep lobe toward the '
                    'auriculotemporal nerve at the back edge of masseter is always present; it can be '
                    'divided without motor loss.'],
                   ['Mobilize the deep lobe anteriorly and inferiorly',
                    'Free its front edge off masseter. Inferiorly, release it from stylohyoid, '
                    'stylopharyngeus and the posterior digastric. Ligate and divide the external carotid '
                    'artery and the retromandibular (retrofacial) vein low in the field; this inferior '
                    'vascular control is what makes an orderly en bloc deep-lobe removal possible.'],
                   ['Release the deep lobe superiorly and off the mandible',
                    'Tie the superficial temporal artery and vein at the upper pole, then roll the deep lobe '
                    'down off the temporomandibular joint capsule. Lift it off the back edge of the '
                    'mandibular ramus, tying the maxillary artery and its veins as they appear. Finally, '
                    'slide the deep lobe out from under the nerve branches in one piece, keeping all '
                    'branches in view.'],
                   ['Make the intraoperative nerve decision',
                    'A functioning nerve that can be separated from tumor is kept, accepting close margins '
                    'for radiotherapy to treat. Tumor can be cleared from the nerve by cutting it, yet still '
                    'recur elsewhere if other margins are close, so a wide nerve margin is pointless when '
                    'the rest of the field is tight. A nerve encased by carcinoma is sacrificed, preferably '
                    'only the involved branch.'],
                   ['Perform a radical parotidectomy when the nerve must go',
                    'Identify the trunk at the stylomastoid foramen where possible and divide it, leaving a '
                    'stump for grafting. Find each distal branch, using the stimulator if helpful, and tag '
                    'it. Check proximal margins on frozen section and follow the nerve into the temporal '
                    'bone as needed. Then remove the gland as in a total conservative parotidectomy.'],
                   ['Extend the resection for invaded structures',
                    'Take involved skin, masseter, mandible, external carotid or mastoid tip en bloc as '
                    'needed. Disease in the ear canal or the intratemporal nerve calls for a lateral '
                    'temporal bone resection. Extended radical parotidectomy is usually combined with an '
                    'appropriate neck dissection, and reconstruction is done in the same sitting.'],
                   ['Graft the facial nerve immediately',
                    'The greater auricular nerve is the preferred cable graft: it lies in the field, is '
                    'close in diameter, and has a single-fascicle structure. Its branching pattern helps '
                    'match several distal targets. Sural nerve is the alternative but has more fascicles, '
                    'little branching and a separate donor site. Trim each end until axons and epineurium '
                    'are flush, then perform tension-free epineurial repairs.'],
                   ['Expect better results with distal branch grafting',
                    "Grafting a peripheral branch defect preserves the facial muscles' normal map and "
                    'recovers better than bridging trunk-to-all-branches, where that map is lost. If an '
                    'accidental transection occurs, stop traction and heat, define healthy ends, and choose '
                    'primary repair when the ends meet without tension.'],
                   ['Protect the eye and add static support',
                    'Reinnervation takes many months, so protect the eye from day one: lubricants, night '
                    'taping or a moisture chamber, and early ophthalmology input if Bell phenomenon is poor. '
                    'Upper-lid loading with a gold or platinum weight, lower-lid tightening, and fascia or '
                    'tendon slings for the nasolabial fold and commissure restore closure, airway and oral '
                    'competence while grafted nerve recovers.'],
                   ['Restore volume and skin',
                    'For contour loss, a de-epithelialized anterolateral thigh (ALT) flap, alone or under a '
                    'cervicofacial rotation flap, restores volume. Small skin defects close primarily or '
                    'with a cervicofacial flap; larger ones need a cervicodeltopectoral or ALT flap, or a '
                    'supraclavicular or keystone island flap in unfit patients. If the ramus is resected but '
                    'the condyle is kept, a fibula flap can rebuild it.'],
                   ['Close and confirm',
                    'Secure hemostasis around the branches with bipolar, stimulate the trunk and branches if '
                    'the nerve was kept, and place a suction drain away from the nerve. Close the SMAS and '
                    'skin without tension or pressure over the nerve. Postoperative radiotherapy is usual '
                    'after extended radical surgery and for high-grade or T3–T4 tumors, close or positive '
                    'margins, perineural invasion or nodal disease, but not for every cancer.']],
 'parotidectomy': [['Set up for facial nerve monitoring',
                    'Ask anesthesia to avoid paralytic agents after intubation. Place monitoring electrodes '
                    'in the ipsilateral facial muscles, usually four channels covering the temporal, '
                    'zygomatic, buccal and marginal territories. Drape so the whole half-face stays visible. '
                    'Position supine and head-up, with a sandbag under the opposite shoulder and the head '
                    'turned; a cotton plug in the ear canal keeps blood out.'],
                   ['Infiltrate and incise',
                    'Inject 1:100,000 epinephrine along the incision before draping. Use a lazy-S (modified '
                    'Blair) incision in the preauricular crease, around the lobule and down into a neck '
                    'crease. A facelift incision, hidden in the sideburn and the occipital hairline, gives a '
                    'better scar. Cut down to the subcutaneous plane with a scalpel.'],
                   ['Elevate the skin flap above the SMAS',
                    'Lift the skin with scissors or blade, leaving the superficial musculoaponeurotic system '
                    '(SMAS) on the gland, since it continues the superficial cervical fascia into the face '
                    'around the mimetic muscles. Carry the flap anteriorly only as far as the planned '
                    'resection requires. Keep the flap thickness even to avoid distal postauricular flap '
                    'necrosis.'],
                   ['Save the posterior greater auricular branch and raise an SMAS flap',
                    'The anterior branch of the greater auricular nerve usually must be divided because it '
                    'runs into the gland. Dissect the posterior branch from the SCM up to the pinna and keep '
                    'it, which limits ear numbness. Then design an SMAS flap and raise it anteroinferiorly '
                    'off the gland, to be laid back later against Frey syndrome.'],
                   ["Free the gland's posterior and inferior borders",
                    'Separate the gland from the anterior border of the SCM and from the cartilaginous ear '
                    'canal. Find the posterior belly of the digastric deep to the lower gland, in front of '
                    'the SCM. Its upper edge tells you the depth at which the facial nerve trunk will be '
                    'found.'],
                   ['Open the preauricular plane to the landmarks',
                    'With sharp-tipped scissors, dissect along the tragal perichondrium, which is nearly '
                    'bloodless, to reach the deepest anterior point of the canal cartilage (the pointer) and '
                    'the tympanomastoid suture. The suture is a groove you can feel with an instrument tip '
                    'and is the most dependable landmark for the trunk.'],
                   ['Triangulate the trunk',
                    'The trunk leaves the skull just deep and inferior to the tympanomastoid suture. It lies '
                    'superficial to, and roughly bisects the angle of, the digastric at its mastoid '
                    'attachment. It also lies about 1 cm deep and 1 cm inferior to the tragal pointer, but '
                    'the pointer moves and can mislead. Do not aim for the styloid: it lies deeper than the '
                    'nerve.'],
                   ['Expose the trunk methodically',
                    'Spread a fine mosquito into the tissue between cartilage and gland, lift it and divide '
                    'only what lies over it. Coagulate small overlying vessels with fine bipolar. Fibrous '
                    'bands can mimic nerve; tease them apart under loupes until the unmistakable trunk '
                    'appears. Confirm with the stimulator, but avoid repeated stimulation, which can cause '
                    'temporary weakness.'],
                   ['Go retrograde when the trunk is unsafe',
                    'With a large or soft tumor over the trunk, or in revision surgery, find a peripheral '
                    'branch and trace it back. The marginal branch crosses superficial to the facial vessels '
                    'at the lower mandibular border; a buccal branch runs alongside Stensen duct; the '
                    'frontal branch crosses the zygomatic arch within about 2 cm in front of the superficial '
                    'temporal vessels. Rarely the nerve is found in the mastoid.'],
                   ['Follow the trunk to the bifurcation',
                    'Tunnel a mosquito along the outer surface of the nerve, open it, and divide the parotid '
                    'tissue above it while keeping the nerve in sight. Bipolar gives fine control with '
                    'little heat spread; a harmonic device is an alternative for a dry field. Reach the pes '
                    'and decide which division the tumor requires.'],
                   ['Respect the tumor-nerve interface',
                    'Remove the tumor with a cuff of normal gland and its capsule intact, because spillage '
                    'or incomplete excision causes recurrence. Where tumor touches a branch, slow down and '
                    'find a real plane rather than tearing or stripping the nerve; a working nerve is not '
                    'cut for adherence alone. For small low-grade cancers a partial resection with about 1.5 '
                    'cm of margin may do; otherwise plan a total conservative parotidectomy.'],
                   ['Perform the superficial partial parotidectomy',
                    'The atlas uses parotid levels, not neck levels: I and II are the upper and lower '
                    'superficial lobe, III and IV the lower and upper deep lobe. For a lower superficial '
                    'tumor, follow the lower division, starting with the cervical, marginal and lower buccal '
                    'branches, lifting the specimen up and forward. The retromandibular vein is usually deep '
                    'to the branches and can often stay. Stop at Stensen duct.'],
                   ['Approach a deep-lobe tumor',
                    'Expose the trunk and bifurcation, then follow the branches about 2 cm further forward. '
                    'Fold the superficial lobe forward on its anterior attachment to show the nerve over the '
                    'deep lobe. Lift the trunk and lower division gently up and medially to remove a level '
                    'III tumor, exposing the external carotid. For level IV, retract the upper division down '
                    'and medially.'],
                   ['Deliver a dumbbell tumor',
                    'When the deep component extends into the parapharyngeal space, release the deep lobe as '
                    'above. Then find and cut the stylomandibular ligament so the mandible can be drawn '
                    'forward and outward. This widens the stylomandibular tunnel enough to free the '
                    'parapharyngeal portion with gentle blunt finger dissection while the nerve stays '
                    'protected.'],
                   ['Know when extracapsular dissection fits',
                    'Extracapsular dissection suits a mobile tail lesion or small superficial benign tumor, '
                    'not inflammation, large or deep tumors, or suspected cancer; many US surgeons still '
                    'prefer partial parotidectomy with nerve dissection. If used, monitor the nerve, open '
                    'the fascia over the lesion, follow the capsule and any projections with traction and '
                    'countertraction, and convert to formal parotidectomy if the pathology or nerve position '
                    'is unclear.'],
                   ['Manage an unexpected transection',
                    'Stop traction and energy use, define healthy proximal and distal ends, and measure the '
                    'gap before finishing the resection. Do a tension-free epineurial repair when the ends '
                    'meet without stretch; otherwise place an interposition cable graft, often the greater '
                    'auricular nerve. If no proximal stump is usable, plan a nerve transfer or reanimation '
                    'rather than accepting the deficit.'],
                   ['Confirm the nerve and secure hemostasis',
                    'Control bleeding with bipolar cautery. Stimulate the trunk and each exposed division at '
                    'low current to confirm function before closing, and record the response in the '
                    'operative note. Cauterize the cut end of the anterior greater auricular branch to '
                    'reduce the chance of a painful neuroma later. Confirm the eye closes fully if any '
                    'branch was handled extensively, and plan eye care if not.'],
                   ['Reconstruct the layers and drain',
                    'After deep or dumbbell resection, return the superficial lobe and suture it in place. '
                    'Re-drape and suture the SMAS flap to limit Frey syndrome. Place a drain under the SMAS, '
                    'plus a second one under the skin if the dissection was wide. Close subcutaneous and '
                    'intradermal layers, consider fibrin glue, and apply a light compression dressing.']],
 'pharyngocutaneous-fistula': [['Know the high-risk patient',
                                'Fistula is more likely after prior radiation, with poor nutrition, '
                                'hypothyroidism, diabetes, ongoing smoking, or positive surgical margins. '
                                'Before the index laryngectomy and again before any repair, correct what you '
                                'can: optimize nutrition, check thyroid function, control glucose, and stop '
                                'smoking. A salvage case should be planned on the assumption that a leak may '
                                'happen.'],
                               ['Prevent it at the index closure',
                                'Close the pharynx with inverting sutures in a watertight, tension-free '
                                'line, saving as much healthy pharyngeal mucosa as the tumor allows. Both '
                                'T-shaped and straight closures are accepted, but a T-shaped closure creates '
                                'a three-point junction that is more likely to leak, so many surgeons prefer '
                                'a straight or horizontal closure without a triple point when feasible.'],
                               ['Consider stapled closure',
                                'For tumors fully confined inside the larynx, a linear stapler can close the '
                                'pharynx quickly, with a tight seal and little contamination, and series '
                                'report fewer fistulas. Do not use it when tumor extends beyond the '
                                'endolarynx, because the closed stapling technique hides the tumor during '
                                'resection and risks a close or positive margin.'],
                               ['Buttress irradiated closures',
                                'In a previously irradiated larynx and pharynx, cover the suture line with a '
                                'pectoralis major myofascial or myocutaneous flap. This is now the standard '
                                'of care because simple closure in irradiated tissue so often breaks down '
                                'into fistula and wound infection. The muscle can be skin-grafted where it '
                                'is left exposed.'],
                               ['Drains and early feeding plan',
                                'Bring suction drains out through separate stab wounds and route them so '
                                'they do not lie directly on the pharyngeal suture line. Feed through a '
                                'nasogastric tube, which avoids the repair. Delay oral intake to about day '
                                '4–7 in non-irradiated patients and day 12–14 after prior radiation, '
                                'provided there are no signs of leak or infection.'],
                               ['Recognize the early leak',
                                'Fever, neck erythema, swelling, or flap tenderness after laryngectomy '
                                'usually means the pharyngeal closure is leaking, and most such infections '
                                'progress to an overt fistula. Get a contrast swallow study when these signs '
                                'appear. A negative study does not exclude a leak, and routine studies '
                                'without clinical signs are of uncertain value. Stop oral intake while you '
                                'evaluate.'],
                               ['Assess before any repair',
                                'Define the tract and its pharyngeal opening, the amount of salivary '
                                "soiling, whether the carotid is exposed or threatened, the patient's "
                                'nutrition and thyroid status, prior radiation, and whether recurrent tumor '
                                'could be the cause. Image or biopsy if recurrence is suspected. These '
                                'answers decide between conservative care and the operating room.'],
                               ['Let timing and size pick the pathway',
                                'The atlas advises early operative re-closure for a fistula that appears '
                                'early, and conservative care for one appearing after about 5–7 days, which '
                                'usually closes with no oral intake, tube feeding, and local wound care. In '
                                'US practice most fistulas get conservative care first, with surgery '
                                'reserved for large or persistent tracts, carotid exposure, sepsis, or '
                                'failed wound care.'],
                               ['Conservative wound care',
                                'Keep the patient off oral intake with tube feeding, divert saliva away from '
                                'the stoma, and pack the tract with saline-moistened gauze under a pressure '
                                'dressing, changed regularly. Some teams add negative-pressure wound '
                                'therapy, a salivary bypass tube, or glycopyrrolate to reduce saliva. Many '
                                'tracts close this way. Escalate if the tract grows, the patient becomes '
                                'septic, or the carotid is exposed.'],
                               ['Open, drain and debride',
                                'For a surgical repair, open the wound enough to drain all infected '
                                'collections. Excise necrotic tissue and nonviable fistula and skin edges '
                                'back to bleeding, healthy tissue. A repair sewn into infected or '
                                'devitalized tissue will fail. Send tissue for histology if recurrence is a '
                                'possibility.'],
                               ['Protect the carotid first',
                                'Before more dissection, identify the carotid, the internal jugular vein, '
                                'and any flap pedicle. An exposed or threatened carotid needs prompt cover '
                                'with well-vascularized tissue, usually a pectoralis major or free flap, '
                                'because saliva bathing an irradiated vessel wall can lead to blowout. Treat '
                                'any sentinel bleed as a warning of rupture and have a bleed plan ready.'],
                               ['Mucosal re-closure when tissue allows',
                                'In an early fistula with healthy tissue, mobilize the pharyngeal mucosa '
                                'around the defect and close it watertight and tension-free with inverting '
                                'sutures, the same principle as the index closure. Do not force a closure '
                                'under tension. Tension or poor-quality tissue is the signal to bring in a '
                                'flap.'],
                               ['Bring in vascularized tissue',
                                'For large or long-standing fistulas, or poor irradiated tissue, close or '
                                'reinforce the pharyngeal defect with a pedicled regional flap, most often '
                                'pectoralis major, with trapezius or supraclavicular flaps as alternatives. '
                                'A free flap such as radial forearm or ALT is preferred when regional '
                                'options are used up, the defect is large, or a thin, pliable patch is '
                                'needed.'],
                               ['Separate saliva from the neck',
                                'The repair must leave a sealed barrier between the salivary stream and both '
                                "the neck skin and the great vessels. Fill dead space with the flap's muscle "
                                "bulk, but don't compress or kink a flap pedicle doing so. Plan skin closure "
                                'so the suture lines of pharynx and skin do not overlie each other.'],
                               ['Drains and closure',
                                'Place suction drains through separate stab incisions, away from the '
                                'pharyngeal repair, the carotid, and any microvascular anastomosis. Confirm '
                                'hemostasis before closing the skin. Close in layers without tension, using '
                                'a flap skin paddle or a skin graft where neck skin is short. Avoid tight '
                                'closures or dressings that could compress a flap pedicle.'],
                               ['After repair: feeding, monitoring, bleed plan',
                                'Continue tube feeding that avoids the repair and keep the patient nil by '
                                'mouth until clinical healing is clear. Restart oral intake cautiously, '
                                'typically later than after the index operation. Watch the wound daily. Make '
                                'sure nursing staff know the carotid-bleed emergency response: pressure, '
                                'airway control through the stoma, and immediate call for surgical help.']],
 'reop-parathyroid': [['Reconfirm the diagnosis',
                       'Before any reoperation, reconsider the biochemistry; familial hypocalciuric '
                       'hypercalcemia in particular must be excluded, especially if the first operation '
                       'found four normal or borderline glands. Distinguish persistent disease after a '
                       'failed first operation from recurrence after initial cure, such as remnant '
                       'hyperplasia in renal or MEN 1 patients.'],
                      ['Review the first operation',
                       'Read the prior operative note and pathology: how many glands were seen, which were '
                       'removed or biopsied, whether a remnant was left and marked, whether a thymectomy or '
                       'thyroid surgery was done, and which side was explored. This tells you where the '
                       'missing gland is most likely to be.'],
                      ['Convincing relocalization',
                       'Reoperate only after imaging convincingly identifies the target, then plan a '
                       'targeted operation. Concordance of at least two studies, such as ultrasound, '
                       'sestamibi or four-dimensional CT, is the usual threshold. If they are negative, '
                       'consider selective venous sampling or ultrasound-guided aspiration with PTH washout. '
                       'Major ectopia beyond the reach of a neck incision needs a planned mediastinal '
                       'approach.'],
                      ['Laryngoscopy and consent',
                       'Examine vocal fold function before surgery, since a prior exploration may have left '
                       'a silent palsy that changes the risk to the remaining nerve. Consent for failure to '
                       'cure, permanent hypoparathyroidism and voice change, which are all more likely in a '
                       'reoperative field.'],
                      ['Anesthesia, monitoring and baseline PTH',
                       'Use an electromyographic tube with short-acting paralysis and obtain a baseline '
                       'vagal signal. Draw a baseline intraoperative PTH before dissecting the target, '
                       'because in reoperation it is the main confirmation of cure.'],
                      ['Incision and limited flaps',
                       'Reopen the previous incision. Raise subplatysmal flaps only as far as needed toward '
                       'the localized target, staying on the platysma undersurface through scar and avoiding '
                       'wide undermining that adds dead space and bleeding.'],
                      ['Lateral or backdoor approach',
                       'Avoid the scarred midline: develop the plane between the anterior SCM border and the '
                       'lateral edge of the strap muscles, retract straps and thyroid medially, and enter '
                       'the tracheoesophageal groove and retroesophageal space from lateral through '
                       'less-disturbed tissue.'],
                      ['Lateral boundary and nerve first',
                       'Expose the carotid sheath as a safe lateral boundary, with the prevertebral fascia '
                       'behind. Find the recurrent laryngeal nerve in a segment the first operation did not '
                       'touch, either low in the tracheoesophageal groove or at laryngeal entry behind the '
                       'cricothyroid joint. Define how it relates to the inferior thyroid artery before '
                       'freeing any tissue attached to it.'],
                      ['Descended superior gland',
                       'The commonest missed superior gland lies deep in the para or retroesophageal space '
                       'close to the nerve, often behind the nerve and the inferior thyroid artery pedicle. '
                       'Retract the esophagus gently medially and search along the prevertebral fascia; in '
                       'goiter, also look behind the tubercle of Zuckerkandl.'],
                      ['Other missed-gland sites',
                       'Check the space just medial to the superior pole (may need upper pole vessel '
                       'division), the carotid sheath, and the thyrothymic ligament and upper thymus, where '
                       'transcervical thymectomy retrieves a low inferior gland. Find a marked neck remnant '
                       'by its suture. After prior autotransplant, a high PTH from the grafted arm points to '
                       'graft recurrence, treated by removing graft tissue under local anesthesia.'],
                      ['Dissect on the target',
                       "Work directly against the gland's capsule, keeping the nerve in view and avoiding "
                       'rupture. Use prior clips and scar only to orient; they do not substitute for seeing '
                       'the nerve. Preserve any remaining normal parathyroid with its blood supply, since '
                       'after earlier resections it may be the only functioning tissue left.'],
                      ['Remove and confirm',
                       'Control the pedicle and remove the gland intact. Confirm parathyroid identity by '
                       'frozen section, as scar, nodes and thyroid nodules are easily mistaken in a '
                       'reoperative field. Consider cryopreserving tissue if the patient may be left '
                       'aparathyroid.'],
                      ['Interpret intraoperative PTH',
                       'Compare post-excision values with the pre-excision baseline using the planned '
                       'criterion. If the fall is inadequate, reassess localization and multigland disease '
                       'before extending the dissection into further scarred territory.'],
                      ['Stop rather than over-dissect',
                       'If the target cannot be found after a reasoned search, end the operation instead of '
                       'blind scar dissection that risks the nerve, esophagus and remaining parathyroids. '
                       'Relocalize and consider a mediastinal approach for ectopia below the cervical '
                       'reach.'],
                      ['Hemostasis and closure',
                       'Achieve meticulous hemostasis in the scarred bed and confirm nerve stimulation. '
                       'Drains are generally not needed. Close straps, platysma and skin without compressing '
                       'the trachea or nerve beneath a tight strap closure.'],
                      ['Aftercare',
                       'Observe for neck swelling for several hours. Reoperative surgery is a recognized '
                       'risk factor for hypocalcemia, typically at 48 to 72 hours; discharge on replacement '
                       'therapy and check calcium within two weeks. Assess vocal fold function after '
                       'surgery.']],
 'reop-thyroid': [['Define the target and review history',
                   'Get the prior operative notes and pathology, and localize what remains with ultrasound '
                   'and contrast CT, including its relation to the trachea, esophagus and great vessels. '
                   'Small recurrent nodes can be marked before surgery (ultrasound-guided charcoal or dye) '
                   'or found with intraoperative ultrasound. Recurrent goiter reaching or passing the aortic '
                   'arch may need sternotomy, so book thoracic standby.'],
                  ['Laryngoscopy and consent',
                   'Document vocal fold function before surgery; nearly half of patients with nerve invasion '
                   'still move normally, so normal mobility does not exclude involvement. If one fold is '
                   'already paralyzed, the remaining nerve is critical: discuss tracheostomy risk and a more '
                   'limited, unilateral plan.'],
                  ['Airway and monitoring plan',
                   'For compressive recurrent goiter, review imaging with anesthesia and agree on intubation '
                   'strategy, possibly a smaller tube or awake fiberoptic intubation. Place an '
                   'electromyographic tube with short-acting paralysis; monitoring is especially valuable '
                   'when anatomy is distorted. Obtain a baseline vagal signal.'],
                  ['Incision and limited flaps',
                   'Reopen the prior incision, extending it if a lateral neck or sternotomy component is '
                   'foreseeable. Raise subplatysmal flaps only as wide as needed to reach the target, '
                   'staying on the platysma undersurface through scar.'],
                  ['Choose the least-scarred plane',
                   'Rather than reopening a dense midline, use the lateral, or backdoor, approach: develop '
                   'the plane between the anterior SCM border and the lateral strap edge, retract the straps '
                   'medially, and reach the thyroid bed and tracheoesophageal groove from the side through '
                   'tissue the first operation did not enter.'],
                  ['Expose the carotid and vagus first',
                   'Define the common carotid from the cricoid level down to the thoracic inlet. This sets a '
                   'safe lateral boundary in scar and puts the vagus in reach for stimulation, confirming '
                   'the monitoring circuit before any dissection near the expected nerve course.'],
                  ['Find the recurrent laryngeal nerve away from scar',
                   'Choose an undisturbed segment: inferiorly in Beahr triangle (carotid, inferior thyroid '
                   'artery, nerve) below the old field; laterally at the inferior thyroid artery near the '
                   'tubercle of Zuckerkandl; or superiorly at laryngeal entry, deep to the lower edge of the '
                   'inferior constrictor behind the cricothyroid joint. Use the probe to map the likely '
                   'course before cutting scar. The left runs parallel and medial, the right obliquely.'],
                  ['Trace the nerve through scar',
                   'Tunnel along the nerve with a fine mosquito clamp, opening tissue parallel to it, and '
                   'control it gently with a vessel loop if helpful. Avoid traction and broad '
                   'circumferential stripping, which raise neuropraxia risk. Stimulate periodically to check '
                   'the signal remains stable.'],
                  ['Superior pole remnant',
                   'If upper-pole tissue remains, ligate its vessels individually against the capsule. Look '
                   'for the external branch of the superior laryngeal nerve on the cricothyroid and inferior '
                   'constrictor, especially when clearing prelaryngeal nodes bridging toward the '
                   'cricothyroid.'],
                  ['Parathyroid tissue',
                   'Remaining parathyroids are often displaced and stuck to scar. Dissect on the thyroid '
                   'remnant capsule so they fall away on their pedicles. Inspect every specimen for '
                   'parathyroid; confirm by frozen section, then mince and autotransplant into a marked SCM '
                   'pocket.'],
                  ['Invasive recurrence',
                   'Tumor adherent to trachea may be shaved if superficial; full-thickness involvement needs '
                   'planned window or segmental resection. Use an esophageal bougie to define a superficial '
                   'esophageal plane. Epineurial nerve involvement can usually be shaved; a functioning '
                   'nerve should generally be preserved, while sacrifice is reserved for aggressive '
                   'histology after prior discussion.'],
                  ['Berry region and remnant removal',
                   'Release the Berry ligament region and residual tissue on the trachea only once the nerve '
                   'course is known, with minimal traction and fine bipolar or sharp dissection. Remove all '
                   'residual thyroid so radioiodine and thyroglobulin follow-up are not compromised.'],
                  ['Central compartment dissection when indicated',
                   'Do a compartment-oriented clearance rather than picking out single nodes. Stay on the '
                   'trachea in the pretracheal space to protect both nerves, identify the innominate artery '
                   'inferiorly, and divide the paratracheal packet dorsal to the carotid and free of the '
                   'esophagus. Leave the thymus, which can hold an inferior parathyroid.'],
                  ['Substernal recurrence',
                   'Mobilize the cervical part fully, freeing it from trachea and esophagus down into the '
                   'thoracic inlet, and deliver with blunt dissection inside the capsule. Retrotracheal, '
                   'multicompartment or below-arch disease may need sternotomy or thoracotomy with the '
                   'thoracic team.'],
                  ['Signal checkpoint',
                   'Stimulate the nerve and vagus after each side. If loss of signal persists below half '
                   'baseline at 20 minutes, do not operate on the opposite side that day; stage it.'],
                  ['Hemostasis',
                   'Irrigate and clear clots, lower the head of the bed and ask for Valsalva at least twice. '
                   'Use bipolar sparingly near nerves; oxidized cellulose for ooze along the nerve. Confirm '
                   'nerves and parathyroids are intact and record final signals.'],
                  ['Drain and closure',
                   'A suction drain is reasonable after wide reoperative dissection with dead space or '
                   'anticoagulation, remembering that a drain neither prevents hematoma nor proves its '
                   'absence. Close straps with a small inferior gap, platysma, and skin so the wound can be '
                   'reopened fast.'],
                  ['Postoperative priorities',
                   'Reoperation carries higher hypocalcemia risk: check calcium and PTH and treat per '
                   'protocol. Suspect bilateral palsy if stridor follows bilateral surgery or surgery on the '
                   'only working nerve; laryngoscopy confirms, and management ranges from observation to '
                   'reintubation or tracheostomy. Watch for hematoma and reopen at once if it expands.']],
 'sialendoscopy': [['Time the case and choose the airway',
                    'Operate after acute sialadenitis has settled, because instrumenting an infected duct '
                    'raises the risk of perforation and spreading infection. Short cases tolerate local '
                    'anesthesia. Long, instrument-heavy cases and deep hilar stones need general anesthesia '
                    'with nasotracheal intubation, which keeps the floor of mouth clear; for parotid work a '
                    'contralateral oral tube may suffice. Re-palpate bimanually just before starting to '
                    'confirm the stone has not moved.'],
                   ['Set up the tower and instruments',
                    "Stand on the patient's right with the assistant opposite and the tower at the head in "
                    'direct view. Check camera orientation so scope movement matches the screen image, '
                    'avoiding disorientation. Have the right scope sizes, conical dilators, probes, '
                    'guidewire, baskets, graspers and fragmentation equipment open, and remember the scopes '
                    'are fragile. Loupes help at the papilla.'],
                   ['Dilate the submandibular papilla',
                    'Use a bite block for endoscopy-only cases. Steady the mucosa with fine-toothed forceps '
                    'behind and above the papilla, or push the tongue to the far side with a finger to '
                    'straighten the duct. Pass probes and conical dilators of increasing size, alternating '
                    'between sizes. A very tight papilla may need a guidewire and Seldinger dilation; if '
                    'cannulation fails, make a minimal ductotomy for the scope.'],
                   ['Dilate the parotid papilla',
                    'Find Stensen papilla opposite the upper second molar. Pull the cheek forward and '
                    'outward at the commissure; this both steadies the buccal mucosa and straightens the '
                    "duct's bend around masseter. Dilate with the same probe and dilator sequence. When the "
                    'papilla is narrow, a guidewire first shows whether a true stenosis lies behind it.'],
                   ['Navigate under irrigation',
                    'Pick a scope suited to patient size and to the instruments needed. Irrigate '
                    'continuously with saline, usually keeping total volume under about 20 mL; dilute '
                    'steroid may be used in chronic sialadenitis and lidocaine under local anesthesia. '
                    'Advance slowly with the lumen centered. If the view is lost to a stricture or the wall, '
                    'pull back until lumen reappears rather than pushing.'],
                   ['Characterize the stone and match the tool to it',
                    'Note location, size relative to the duct, and whether it floats or is impacted; an '
                    'apparently fixed stone may prove mobile up close. In general, stones up to about 4 mm '
                    '(submandibular) or 3 mm (parotid) suit basket removal. Larger ones need fragmentation '
                    '(laser, intracorporeal or extracorporeal lithotripsy) or an open or combined approach. '
                    'Large stones may need staged sessions.'],
                   ['Basket the stone safely',
                    'Pass the closed basket beyond the stone, have the assistant open it on the far side, '
                    'then draw it back while working the wires around the stone. Close and withdraw; some '
                    'baskets instead open in front of the stone. If a basket is trapped on an impacted '
                    'stone, never yank it, which can avulse the duct; convert to open removal, as discussed '
                    'at consent.'],
                   ['Enlarge the exit only where safe',
                    'A small papillotomy to deliver a basketed stone from Wharton duct causes little harm. '
                    'Avoid papillotomy at the parotid papilla; if it is unavoidable, place a stent afterward '
                    'because Stensen duct is prone to stenosis. Reinspect the treated segment for fragments '
                    'and confirm free irrigation flow.'],
                   ['Remove a distal submandibular stone transorally',
                    'Infiltrate local anesthetic with vasoconstrictor over the palpable stone. Pass a suture '
                    'around the duct behind the stone so it cannot slip back. Cut through the mucosa '
                    'directly onto the stone and lift it out. Marsupialize the duct edges to the mucosa with '
                    'fine absorbable sutures, then irrigate to clear pus trapped behind the obstruction.'],
                   ['Expose the floor of mouth for a hilar stone',
                    'Put a Ferguson-type mouth prop on the opposite side instead of a bite block, so the '
                    'tongue can be pushed away. Retract the tongue with your nondominant index finger over a '
                    'gauze. Inject local anesthetic with epinephrine into the superficial submucosa along '
                    'the planned line, both for hemostasis and to open the plane by hydrodissection.'],
                   ['Make a retropapillary incision',
                    'Start about 5 mm behind the papilla, leaving the natural opening intact to avoid '
                    'stenosis. Run the incision just medial to the sublingual gland, seen as a yellowish '
                    'crescent, back to the first or second molar. Cut mucosa only: incising the sublingual '
                    'gland risks a ranula, and entering tongue muscle puts you in a bleeding wrong plane. '
                    'Use bipolar only.'],
                   ['Follow Wharton duct back',
                    'Look for the duct on the deep (medial) side of the sublingual gland. A stay suture '
                    'through the sublingual gland, pulled forward and outward, lifts the duct toward you. '
                    'Follow the duct back toward the hilum in the loose areolar tissue around it, keeping '
                    'your dissection right on the duct wall so the lingual nerve stays out of harm.'],
                   ['Separate the lingual nerve in the danger zone',
                    'Around the first and second molars the lingual nerve crosses the duct, passing from its '
                    'lateral side to its medial side; from the transoral view it lies right against, and may '
                    'overlie, the duct. Hilar stones usually sit here. Inflammation often binds nerve to '
                    'duct, so identify the nerve before any ductotomy. Deep work also risks the ranine veins '
                    'and, more seriously, the lingual artery.'],
                   ['Push the hilum forward and open onto the stone',
                    'Have the assistant press the gland firmly upward and forward from the neck; this brings '
                    'the hilum and stone into the mouth and is the key maneuver. Keep the pressure steady '
                    'through the ductotomy. Incise the duct directly over the stone, on the side away from '
                    "the nerve, and extend the cut past the stone's leading edge. Have irrigation, a dental "
                    'excavator and fine suture ready.'],
                   ['Extract, irrigate and check for more stones',
                    'Lift the stone out with the excavator, then irrigate into the duct; this often flushes '
                    'out further small proximal stones. Do not lose small stones into the floor of mouth, '
                    'where they cause infection. Irrigate the bed well if pus drains. With a scope through '
                    'the papilla, inspect the hilum and intraglandular ducts for retained stones.'],
                   ['Repair and close the floor of mouth',
                    'Approximate the ductotomy edges with 6-0 absorbable suture when feasible; leaving a '
                    'proximal ductotomy open is generally harmless. Close the mucosa with 4-0 absorbable '
                    'suture. Submucosal dexamethasone and a tranexamic acid rinse of the bed may reduce '
                    'swelling and bleeding.'],
                   ['Remove an anterior parotid duct stone transorally',
                    'Pass a probe up Stensen duct until it meets the stone, grasp papilla and probe '
                    'together, and cut an ellipse around the papilla. Dissect along the duct to the stone, '
                    'open the wall over it, deliver it and massage out retained saliva. Repair the duct over '
                    'a stent with 6-0 nonabsorbable suture, or marsupialize the opening to buccal mucosa.'],
                   ['Use a combined external approach for mid or posterior parotid stones',
                    'Under general anesthesia, locate the stone endoscopically and mark the transilluminated '
                    'skin point. Monitor the facial nerve, since the buccal branch follows the duct. Through '
                    'a parotidectomy or facelift incision, raise an anteriorly based SMAS flap, open the '
                    'duct over the stone and remove it. Repair over a stent secured near the papilla; remove '
                    'stents at about two weeks.'],
                   ['Finish, stent and plan aftercare',
                    'Place a stent when the duct was stenotic, sutured or injured, and secure it without '
                    'blocking the papilla; remove it at about two weeks. Document the stones removed, '
                    'residual fragments, duct patency and any incision. Admit overnight for airway watch if '
                    'floor-of-mouth or neck swelling develops. Encourage hydration, sialogogues and gland '
                    'massage, and follow up for recurrent obstruction.']],
 'submandibular-gland': [['Set up for marginal nerve monitoring',
                          'If facial nerve monitoring is used (optional; many US surgeons do not monitor '
                          'routinely), ask anesthesia to avoid muscle relaxant after intubation and place '
                          'electrodes in the lower lip depressors. Position supine with the neck extended '
                          'and head turned away. Drape so the lower lip and mandibular border remain '
                          'visible, since a lip twitch is an early warning that the nerve is near.'],
                         ['Infiltrate and place a low incision',
                          'Inject local anesthetic with 1:100,000 epinephrine along the planned line. Make a '
                          'horizontal curvilinear incision in a relaxed skin tension line about two '
                          'fingerbreadths (3–4 cm) below the mandibular border, or at hyoid level, running '
                          '5–6 cm forward from the anterior SCM border. A low incision keeps the marginal '
                          'branch, which may sag up to 3 cm below the mandible, above your work.'],
                         ['Open the layers over the gland',
                          'Divide subcutaneous tissue, platysma and then the superficial layer of the deep '
                          'cervical fascia over the lower gland. The marginal branch, often as several '
                          'parallel twigs, runs inside this fascia over the gland and crosses superficial to '
                          'the facial artery and vein. Avoid monopolar cautery anywhere near the nerve.'],
                         ['Lift the nerve away with the facial vein',
                          'Find the facial vein on the outer surface of the gland near its lower border. Tie '
                          'and divide it there, and lift the upper stump with the investing fascia toward '
                          'the mandible by blunt dissection. From this point stay directly on the gland '
                          'capsule, so the marginal branch remains in the elevated layer above your work.'],
                         ['Confirm the nerve rather than assume it',
                          'The safest protection is to identify the marginal branch with the stimulator '
                          'where it crosses the facial vessels, not to trust vessel elevation alone. '
                          'Platysmal twigs can be followed back to it. Formal exposure of the nerve is '
                          'required when a level I neck dissection is added, because the perifacial nodes '
                          'must be cleared.'],
                         ['Define the posterior and superior gland',
                          'The posteroinferior gland lies over the posterior digastric belly just in front '
                          'of the SCM. At the upper border, bluntly clear the fat to show the facial artery '
                          'and vein running over the top of the gland toward the mandible. Retract the soft '
                          'tissue at the mandible with blunt hooks to keep the nerve protected.'],
                         ['Divide glandular branches close to the gland',
                          'Ligate the facial artery and vein branches that enter the gland right at the '
                          'capsule rather than out in the surrounding tissue. Keep the facial artery trunk '
                          'when it may be needed, for example as the pedicle of a buccinator myomucosal '
                          'flap. Double ligatures or suture ligatures are preferred, because an inadequately '
                          'tied vessel causes hematoma and laryngeal edema.'],
                         ['Release the anterior gland',
                          'Grasp the gland with an Allis or Babcock clamp and pull it down and back to free '
                          'its front edge from the anterior digastric belly. Lifting that edge shows the '
                          'mylohyoid artery and vein; tie or cauterize them. Then pull the gland laterally '
                          'and sweep its deep surface off mylohyoid, whose outer surface carries no '
                          'important structures.'],
                         ['Keep the hypoglossal nerve in mind below',
                          'Trace the digastric through its tendon to the anterior belly. The hypoglossal '
                          'nerve runs deep to the tendon on hyoglossus, under a thin fascia separate from '
                          'the gland capsule, often close to the inferior border of the gland. Its thin '
                          'accompanying veins tear easily; tearing them causes bleeding that tempts blind '
                          'clamping near the nerve.'],
                         ['Expose the lingual nerve',
                          'Retract mylohyoid forward while drawing the gland gently down. The lingual nerve '
                          'appears above the deep lobe, pulled down into a V by the submandibular ganglion; '
                          'the bottom of the V marks where it crosses the deep lobe and the duct. Keep your '
                          'dissection tight against the gland and duct here so the nerve is not stretched or '
                          'heated.'],
                         ['Divide the ganglion without catching the nerve',
                          'Secure the ganglion branches near the gland with bipolar cautery, small clips or '
                          'a fine ligature, then divide them so the lingual nerve springs up and away from '
                          'the gland. Never place a tie or clip across the main nerve trunk. Bipolar only, '
                          'at low settings, near any nerve to prevent thermal injury.'],
                         ['Ligate Wharton duct as far forward as possible',
                          'Follow the duct anteriorly in the floor of the mouth and ligate or clip it as '
                          'distally as you can before dividing it; a long retained stump can harbor stones '
                          'or debris and cause infection. If a hilar stone has slipped forward and cannot be '
                          'found, follow the duct into the floor of mouth or open it transorally.'],
                         ['Control the facial artery proximally and remove the gland',
                          'Reflect the gland down. Where needed, ligate and divide the facial artery as it '
                          'emerges from behind the posterior digastric belly, using a double tie. Free the '
                          'gland from the digastric tendon and posterior belly and remove it. The cleared '
                          'bed shows the hypoglossal nerve, lingual nerve and duct stump on hyoglossus, plus '
                          'the facial artery.'],
                         ['Send frozen section when tumor is possible',
                          'If a neoplasm is possible, frozen section on the gland can guide same-sitting '
                          'decisions, though salivary frozen sections are not always definitive. For a '
                          'confirmed carcinoma, most US surgeons extend to at least a level I–III neck '
                          'dissection rather than level I alone. Formal level I clearance means dissecting '
                          'the marginal branch over the facial vessels and removing the perifacial nodes.'],
                         ['Check nerves and bleeding',
                          'Inspect the lingual and hypoglossal nerves for continuity, stimulate the marginal '
                          'branch if monitored, and look for bleeding along the ranine veins, the mylohyoid '
                          'vessels and the facial artery stumps. A Valsalva maneuver helps reveal venous '
                          'bleeding before closure. Hemostasis matters because neck hematoma can cause '
                          'airway edema.'],
                         ['Drain and close in layers',
                          'Place a suction drain and close subcutaneous tissue and platysma with 3-0 '
                          'absorbable sutures, then skin with a 5-0 intracutaneous suture. Leave the drain '
                          'at least 36 hours and remove it once 24-hour output falls below 30 mL. Remove '
                          'skin sutures around day seven.']],
 'tep': [['Plan voice rehabilitation early',
          'Introduce the patient to a speech-language pathologist before laryngectomy, address expectations, '
          'and if possible show them valved speakers or videos. Valved tracheoesophageal speech is the '
          'preferred method: it is lung-powered and easy to learn. Esophageal speech is hard to master and '
          'comes in short phrases. An electrolarynx sounds mechanical. Keep both as fallbacks when a valve '
          'is not possible.'],
         ['Choose primary or secondary puncture',
          'Primary puncture at laryngectomy is standard for most patients. The atlas favors a delayed '
          '(secondary) puncture after salvage surgery, where fistula risk is higher, and after '
          'circumferential pharyngectomy; many US centers still perform primary TEP in these cases, because '
          'published series show similar complication rates. A secondary puncture is also needed when the '
          'tract of a lost prosthesis has closed.'],
         ['Primary: insert the pharyngeal protector',
          'Once the laryngectomy specimen is out and before any pharyngeal closure, pass the pharyngeal '
          'protector through the open pharynx into the upper esophagus. Turn its beveled end to face forward '
          'against the party wall. The protector catches the trocar so the posterior esophageal wall cannot '
          'be speared.'],
         ['Primary: pick the puncture site',
          'Puncture in the midline of the posterior tracheal (party) wall, about 1–1.5 cm below the cut '
          'tracheal edge. Too close to the mucocutaneous junction and the prosthesis sits on the stoma rim '
          'and is unstable; too far down and it is hard for the patient and clinician to see, clean, and '
          'change. Midline placement keeps the tract centered in the party wall.'],
         ['Primary: puncture and pass the wire',
          'Drive the puncture needle or trocar through the party wall into the bevel of the protector under '
          'direct vision, never by blind force. Thread the guidewire through the needle and out through the '
          "open pharynx. Then, following the specific manufacturer's system, pull the prosthesis through "
          'into the newly created tract.'],
         ['Primary: seat and verify the valve',
          'Confirm both retention flanges have fully opened, the esophageal flange inside the upper '
          'esophagus and the tracheal flange against the posterior tracheal wall. Check that the device '
          'rotates freely. An alternative is to stent the tract with a feeding catheter and swap it for a '
          'valve once oral feeding is established. Record the prosthesis type, diameter and length.'],
         ['Cricopharyngeal myotomy for voice',
          'Before closing, do a posterior myotomy from just below the puncture up through the '
          'cricopharyngeus, dividing the upper esophageal sphincter musculature. Cut every muscle fiber '
          'until the submucosal vessels are visible. An incomplete myotomy leaves a hypertonic, spasming '
          'pharyngoesophageal segment, which produces strained or absent voice and worse swallowing.'],
         ['Close the pharynx with voice in mind',
          'The atlas voice chapter reports better speech and swallowing after horizontal than vertical '
          'closure, and notes that T-shaped closures, with their three-point junction, leak more often; the '
          'evidence is limited and either closure is accepted. A leak causes fibrosis and stricture that '
          'stiffen the vibrating segment, so aim for a watertight, tension-free closure that avoids a weak '
          'triple point.'],
         ['Rebuild the vibrating segment',
          'Repair the thyropharyngeus remnants over the closure to restore toned muscle that vibrates well '
          'for voice. Then suture this layer up to the suprahyoid muscles divided at vallecular entry, which '
          'include the middle constrictor. Restoring that sling makes the early pharyngeal phase of the '
          'swallow more efficient.'],
         ['Shape the stoma',
          'Divide the sternal head of each SCM to flatten the skin around the stoma. A flat surface makes it '
          'easier to handle the prosthesis and to attach a baseplate for a heat and moisture exchanger, and '
          'it may lower the risk of stomal stenosis. The stoma should be wide enough for digital occlusion '
          'and for inserting and cleaning the prosthesis.'],
         ['Secondary: assess the segment first',
          'If time has passed since laryngectomy or a valve has been lost, get a videofluoroscopic swallow '
          'study of the neopharynx and pharyngoesophageal segment. Stricture or spasm can then be treated '
          'with dilation or botulinum toxin during the same anesthetic. Office puncture is possible, but a '
          'brief general anesthetic is often easier.'],
         ['Secondary: position the esophagoscope',
          'Pass a rigid pharyngoscope or esophagoscope through the mouth down to the level of the stoma. '
          'Rotate it so the beveled opening faces forward toward the trachea. Light from the scope should '
          'shine through the tracheal mucosa, confirming the scope is in the right spot behind the party '
          'wall before any puncture.'],
         ['Secondary: puncture, size and insert',
          'Puncture the party wall 1–1.5 cm below the skin-mucosa junction, with the trocar entering the '
          "scope's bevel to protect the back wall of the esophagus. Use the kit's sizer to choose prosthesis "
          'length. Pull the guidewire out through the mouth rather than the pharynx, draw the valve in, and '
          'confirm both flanges are fully deployed.'],
         ['Secondary: difficult access options',
          'Poor mouth opening, limited neck extension, or neopharyngeal stenosis may stop a rigid scope '
          'after salvage surgery. Use a videolaryngoscope to dilate and to aim botulinum toxin. '
          'Alternatively, pass an endotracheal tube through the mouth, run a nasendoscope inside it for '
          'transillumination, and puncture onto the bevel of that tube.'],
         ['Problem-solving: central leak',
          'Ask whether fluid comes through the valve or around it. A central leak (through the device) means '
          "valve failure from debris, Candida biofilm, or reflux, and usually marks the end of the valve's "
          'life, so replace it. If valves fail early, add nystatin cleaning and antireflux therapy. Devices '
          'generally last 3–6 months and need regular brushing.'],
         ['Problem-solving: peripheral leak',
          'A leak around the device usually means the prosthesis is too long for a thinned party wall and '
          'pistons in the tract; radiation and poor nutrition thin the wall. Refit to the correct length '
          'first. Options include an added silicone collar or larger flange, or filler or fat injected '
          'around the tract. The atlas suggests a narrower 16–17 French valve for walls under 8 mm. Avoid '
          'serial upsizing.'],
         ['Problem-solving: aphonia and granulation',
          'No voice or strained voice calls for videofluoroscopy of the pharyngoesophageal segment. A '
          'hypertonic or spasming segment responds to botulinum toxin, given under fluoroscopy or at '
          'pharyngoscopy, and a stricture needs dilation. A hypotonic segment gives a weak voice that '
          'digital neck pressure can help. Granulation tissue that disturbs prosthesis fit may need '
          'excision.'],
         ['Problem-solving: extruded or missing valve',
          'If the prosthesis comes out, place a catheter in the tract right away to keep it from closing, '
          'and replace the valve as soon as possible. Stop if passing it meets resistance or the tract is '
          'uncertain. If the device cannot be accounted for, assume aspiration: a normal chest film does not '
          'exclude it, and bronchoscopy should be used to find and retrieve it.']],
 'thyroglossal': [['Confirm a normal thyroid and a quiet cyst',
                   'Check that preoperative ultrasound shows a normally placed thyroid; removing an ectopic '
                   'gland mistaken for a cyst leaves the patient hypothyroid for life. Check thyroid '
                   'function if the history suggests hypothyroidism. If the cyst is infected, treat it and '
                   'wait roughly six weeks; aspirate if needed rather than incising, which risks a fistula.'],
                  ['Position and infiltrate',
                   'Under general anesthesia, place the patient supine with a gel roll or folded blankets '
                   'under the shoulders to extend the neck. After skin preparation, infiltrate local '
                   'anesthetic with dilute epinephrine (1:200,000) along the planned incision to reduce '
                   'bleeding in the superficial layers.'],
                  ['Place the incision',
                   'Use a transverse skin-crease incision across the midline in the upper neck, roughly at '
                   'the upper border of the thyroid cartilage or over the cyst. If there is a sinus opening, '
                   'an old drainage scar or adherent skin, include it in an ellipse that stays with the '
                   'specimen. Lengthen the incision on either side for larger cysts.'],
                  ['Raise flaps above the hyoid',
                   'Deepen through fat and, laterally, platysma. Elevate subplatysmal flaps, with the '
                   'superior flap carried above the hyoid so the suprahyoid dissection is fully exposed. An '
                   'inferior flap toward the thyroid cartilage is raised as far as needed. Retain an ellipse '
                   'of skin on the cyst if a sinus is present.'],
                  ['Separate the straps from the cyst',
                   'Find the midline between the strap muscles, divide it, and retract the straps laterally '
                   'with blunt retractors. Free the cyst from the straps by sharp and blunt dissection. Keep '
                   'a cuff of surrounding soft tissue on the cyst and tract rather than skeletonizing it. '
                   'Stay near the midline, since the important structures lie laterally.'],
                  ['Clear the inferior extent without entering the airway',
                   'Dissect the cyst off the thyroid cartilage and thyrohyoid membrane until it is attached '
                   'only to the hyoid above. Keep the thyroid notch and membrane in view, since cutting '
                   'through the membrane opens the airway and can cause subcutaneous emphysema. Carry the '
                   'dissection down to the pyramidal lobe so any lower extension of the tract comes with the '
                   'specimen.'],
                  ['Contain a ruptured cyst',
                   'If the wall tears, suction the contents immediately before they spread, then close the '
                   'tear with a stitch so the cyst keeps its shape and remains easy to follow. If contents '
                   'have spilled, irrigate the field thoroughly before continuing, because remnant '
                   'epithelium is a source of recurrence.'],
                  ['Free the central hyoid',
                   'Grasp the hyoid body with a tenaculum or bone-holding forceps and strip the muscle '
                   'attachments off the central body with a periosteal elevator or needle-tip cautery. Avoid '
                   'deep sharp cuts just above or below the bone, where the tract is easily transected. Keep '
                   'the soft-tissue dissection medial to the anterior digastric bellies.'],
                  ['Divide the hyoid medial to the lesser cornua',
                   'Cut the hyoid with a bone cutter on each side of the midline, staying medial to the '
                   'lesser cornua; a lateral cut risks the hypoglossal nerve. The resected segment is '
                   'commonly about 1–1.5 cm wide. Lift the freed central segment forward and upward with '
                   'forceps, keeping the cyst and tract attached.'],
                  ['Bring the tongue base to you',
                   'An assistant, or your own gloved finger in the mouth, presses down on the tongue base '
                   'near the foramen cecum. This brings the tongue base up into the neck wound, so the '
                   'suprahyoid muscles are closer and easier to core out. The finger also tells you how '
                   'close the core is to the mucosa, which helps you avoid an unplanned entry.'],
                  ['Core out the suprahyoid tract',
                   'Above the hyoid, remove the tract inside a core of surrounding muscle rather than the '
                   'tract alone, heading back and up at about 45 degrees toward the foramen cecum. '
                   "Sistrunk's core was about 3 mm in radius. The atlas prefers to include the foramen "
                   'cecum; many US surgeons stop at the tongue-base mucosa. Stay midline to protect the '
                   'lingual arteries and hypoglossal nerves.'],
                  ['Consider the extended Sistrunk variant',
                   'For a more complete resection, take a strip of the adjacent strap muscles from the '
                   'thyroid isthmus up to the hyoid. Above the hyoid, take the epimysium of the suprahyoid '
                   'muscles with the tract. In this variant the dissection ends at the tongue base without '
                   'breaching it. Reported recurrence is lower than with the classic procedure.'],
                  ['Repair any pharyngeal or airway entry',
                   'If you open the vallecula or pharynx, close the hole with interrupted or purse-string '
                   'absorbable sutures. If the thyrohyoid membrane is breached, repair it airtight in '
                   'layers: invert the mucosa, close the fibrous layer, then bring strap muscle over it. A '
                   'missed breach can produce marked subcutaneous emphysema or a salivary leak after '
                   'surgery.'],
                  ['Deliver and check the specimen',
                   'Remove the cyst, tract, central hyoid and tongue-base core as one specimen and send it '
                   'for histology, since carcinoma, usually papillary, occasionally arises in these cysts. '
                   'Inspect the field for residual epithelial tract or cyst wall. Irrigate copiously with '
                   'saline and secure hemostasis, because a neck hematoma here can threaten the airway.'],
                  ['Drain and close in layers',
                   'The atlas drains routinely; many US surgeons drain selectively, based on dead space and '
                   'cyst size. Bring the strap muscles together over the midline, then close platysma and '
                   'skin with absorbable sutures. Observe overnight if a drain is used or the airway was '
                   'entered. Remove the drain once output is under about 20 mL in 24 hours, and watch for '
                   'hematoma.']],
 'thyroid-lobectomy': [['Preoperative checks and airway plan',
                        'Confirm the operative side against the ultrasound and cytology reports and mark it. '
                        'Document preoperative vocal fold mobility and a euthyroid state. A known '
                        'contralateral recurrent laryngeal nerve palsy changes the risk profile and argues '
                        'against same-day discharge. Review CT if retrosternal extension is suspected, since '
                        'it changes incision length and may need thoracic backup.'],
                       ['Nerve monitoring setup',
                        'Anesthesia places an electromyographic endotracheal tube with its electrodes '
                        'sitting at the level of the vocal folds, confirmed with a video laryngoscope if the '
                        'direct view is poor. Request only a short-acting paralytic at induction so the '
                        'monitor works once the nerve is reached. Place the ground electrode on the upper '
                        'chest or shoulder and test the system before prepping.'],
                       ['Positioning',
                        'Once the tube is secured, move the patient without dislodging it. Place a shoulder '
                        'roll and soft head ring, and extend the neck only as far as habitus and cervical '
                        'spine allow, never leaving the head hanging unsupported. Raise the head of the bed '
                        '15 to 30 degrees to lower venous pressure and reduce bleeding.'],
                       ['Marking and incision',
                        'Palpate and mark the thyroid notch, cricoid, sternal notch and medial borders of '
                        'the sternocleidomastoid muscles. Choose a natural skin crease; tailor length to '
                        'neck build, lobe size, retrosternal extension and any old scar. Optional local '
                        'anesthetic with epinephrine can be infiltrated while the team scrubs. Cut with the '
                        'blade held perpendicular to the skin to avoid beveled edges.'],
                       ['Subplatysmal flaps',
                        'Divide the platysma across the full incision width. Raise the upper flap to the '
                        'thyroid notch and the lower flap to the sternal notch in the plane just superficial '
                        'to the anterior jugular veins, with the surgeon pulling the strap fascia down for '
                        'countertension. Ligate anterior jugular veins that cross medially. Hold flaps with '
                        'elastic hook stays or stay sutures.'],
                       ['Open the midline',
                        'Divide the raphe between the strap muscles from the thyroid notch down to the '
                        'sternal notch, with assistants lifting each end. Take care at the top, where the '
                        'overlying skin and flap are thinnest and easy to perforate. Keep the field dry from '
                        'the beginning: blood staining the tissues is what later makes the recurrent '
                        'laryngeal nerve and parathyroids hard to see.'],
                       ['Isthmus division, early or late',
                        'If dividing first, define the upper and lower isthmus borders, then pass a clamp in '
                        'the plane between isthmus and trachea, sparing the tracheal rings and cricothyroid '
                        'membrane. At the lower border watch for a high-riding innominate vessel at the '
                        'thoracic inlet. Clamp and suture-ligate or seal with an energy device; for an '
                        'isthmic nodule, divide lateral to it. Early division particularly helps large or '
                        'substernal lobes.'],
                       ['Strap muscles and lateral mobilization',
                        'The straps usually stay intact; for a large lobe, partly divide the upper '
                        'sternothyroid to reach the superior pedicle. Sweep the fascia off the lobe '
                        'laterally until the carotid sheath is seen, then stimulate the vagus to record a '
                        'baseline signal. Tie, clip or seal the middle thyroid vein. Handle large glands '
                        'gently, since rough traction can tear the internal jugular vein.'],
                       ['Superior pole and external branch of the superior laryngeal nerve',
                        'With retractors pulling up and out, open the fascial pocket between the medial '
                        'upper pole and the inferior constrictor with fine forceps, avoiding shearing small '
                        'vessels or the external branch. Pull the pole down and lateral with an Allis or '
                        'Babcock clamp and divide the pedicle vessels close to the capsule, keeping '
                        'energy-device tips fully visible. Look for the superior parathyroid posteriorly '
                        'before sealing.'],
                       ['Capsular dissection and inferior parathyroid',
                        'Dissect right on the thyroid capsule with a fine instrument, and keep out of the '
                        'tracheoesophageal groove until the lobe has been rolled forward and toward the '
                        'midline. The inferior parathyroid is frequently stuck to the lower lobe; tease it '
                        'off so it stays on its inferior thyroid artery branch instead of leaving its blood '
                        'supply with the specimen.'],
                       ['Find the recurrent laryngeal nerve',
                        'Near the lower lobe and inferior thyroid artery, the nerve may run in front of, '
                        'behind or between the arterial branches. Use the tracheoesophageal groove, the '
                        'artery, Berry ligament and the tubercle of Zuckerkandl as guides. On the right, '
                        'about 1 in 100 nerves is nonrecurrent and runs straight in from the vagus; suspect '
                        'it when no nerve is found low. Preserve every branch.'],
                       ['Superior parathyroid and terminal vessels',
                        'Preserve the superior parathyroid on the posterior upper capsule, usually near the '
                        'cricothyroid joint, with its pedicle intact. Divide the terminal inferior thyroid '
                        'branches directly on the capsule, distal to the parathyroid supply, rather than '
                        'ligating the main trunk.'],
                       ['Berry ligament and specimen delivery',
                        'Use minimal traction on the lobe here, because pulling stretches the adherent '
                        'nerve. Divide the ligament with fine instruments, judicious bipolar and sharp '
                        'dissection while the nerve is seen entering the larynx at the cricothyroid joint. '
                        'Include the pyramidal lobe, which more commonly sits on the left, with the '
                        'specimen. Then complete isthmus division if deferred.'],
                       ['Specimen handling and parathyroid rescue',
                        'Inspect the specimen surface for a parathyroid before handing it off. Send in '
                        'formalin unless lymphoma is suspected, which needs fresh tissue. A removed or '
                        'clearly devascularized parathyroid is dissected off, a fragment confirmed by frozen '
                        'section, then minced and placed in a small pocket in the sternocleidomastoid marked '
                        'with a nonabsorbable suture or clip.'],
                       ['Confirm nerve function',
                        'Stimulate the recurrent laryngeal nerve with the probe to document an intact signal '
                        'after the lobe is out; stimulating the vagus as well confirms the whole circuit and '
                        'distinguishes true nerve injury from an equipment problem.'],
                       ['Hemostasis',
                        'Wash the bed and clear clots. Lower the head of the bed and have anesthesia hold a '
                        'Valsalva maneuver, ideally twice, to raise venous pressure and reveal bleeding '
                        'points. Use bipolar cautiously near the nerve; for low-grade ooze on the nerve, lay '
                        'oxidized cellulose gently along the tracheoesophageal groove rather than '
                        'cauterizing.'],
                       ['Closure',
                        'Drains are not routine after lobectomy unless bleeding risk or a chyle leak is a '
                        'concern. Reapproximate the straps in the midline with interrupted absorbable '
                        'sutures, leaving a small gap at the lower end so a hematoma can decompress and be '
                        'evacuated quickly; this also prevents the trachea tethering to the skin. Close '
                        'platysma, then subcuticular suture or skin glue.'],
                       ['Recovery checks',
                        'Before discharge, check the neck for swelling and the airway for stridor. An '
                        'expanding hematoma with breathing difficulty is opened at the bedside, cutting '
                        'skin, platysma and strap sutures to release the clot, then the patient returns to '
                        'the OR. Assess vocal folds before discharge or at the first visit. Calcium checks '
                        'are not needed after lobectomy. Check thyroid function at 4 to 6 weeks.']],
 'tonsillectomy': [['Plan the shared airway',
                    'Agree on a primary and backup airway plan with the whole team, especially when '
                    'malignancy is suspected or the airway may be difficult. A south-facing oral RAE tube is '
                    'the standard because it protects against airway soiling. A reinforced laryngeal mask '
                    'works in well-chosen cases when the team is trained. Look for pulsation on the '
                    'posterior pharyngeal wall, which suggests a retropharyngeal carotid.'],
                   ['Position and protect',
                    'Bring the head to the end of the table and place a shoulder roll to extend the neck. '
                    'Tape and protect the eyes, and drape so both nose and mouth are exposed. Check and '
                    'focus the headlight before scrubbing. Inspect lips, teeth, and oral cavity, and record '
                    'any loose or damaged teeth so you can confirm the same at the end.'],
                   ['Seat the mouth gag',
                    'Center the tongue under the tube, then insert a mouth gag (Crowe-Davis or McIvor in '
                    'most US rooms) whose blade length matches the curve of the tongue base without pressing '
                    'on the back of the throat. Seat the tube in the blade groove and the tooth guard on the '
                    'upper incisors; use moist gauze over bare gums. Pull the lower lip out from under the '
                    'guard.'],
                   ['Open and suspend safely',
                    'If the tongue has slid to one side, push it back under the tube with a finger, '
                    'otherwise that lower pole will be hard to reach. Open the gag only as far as needed and '
                    'suspend it on rods or a Mayo stand. Recheck the tube, since suspension can move it. '
                    'Keep the head resting on the table rather than hanging from the cervical spine.'],
                   ['Set energy and fire precautions',
                    'Run bipolar at the lowest effective setting, because higher power has been linked to '
                    'more bleeding. Ask anesthesia to lower inspired oxygen to what monitoring allows '
                    'whenever cautery is used. If you inject local anesthetic for postoperative comfort, '
                    'aspirate first, because the external carotid branches sit close by.'],
                   ['Steroid and analgesia plan',
                    'Give a single intravenous dexamethasone dose at induction, which US guidelines '
                    'recommend to reduce nausea and speed return to eating. Plan postoperative analgesia '
                    'with acetaminophen and ibuprofen, which does not meaningfully raise bleeding risk. Do '
                    'not give codeine or tramadol to children under 12. Encourage early, frequent fluids, '
                    'since dehydration from pain drives many return visits.'],
                   ['Grasp and medialize the tonsil',
                    'Hold the tonsil with a tonsil tenaculum or Allis clamp (the atlas uses Denis Browne '
                    'forceps) and pull it toward the midline, avoiding repeated regrasping that tears '
                    'tissue. Steady medial traction opens the space between the capsule and the pillars, so '
                    'the plane becomes visible before you cut.'],
                   ['Make the anterior mucosal incision',
                    'Use scissors to cut a curved incision just inside the anterior pillar, lifting the '
                    'mucosa on the blade so the peritonsillar plane shows quickly and little mucosa is lost. '
                    'A bipolar coagulate-then-pull method is an acceptable alternative. Extend the cut up '
                    'beside the uvula but separate from it, and avoid heat, suction, and handling there.'],
                   ['Develop the capsular plane',
                    'Spend time here finding the true peritonsillar plane; the rest goes faster once it is '
                    'found. Put one limb of the forceps into the pocket and keep pulling medially. Sweep '
                    'fascia and vessels off the capsule with a tonsil dissector, working against the '
                    'traction. Stay on the tonsil to keep superior constrictor fibers intact.'],
                   ['Release the posterior pillar',
                    'Follow the curve of the tonsil backward and peel the posterior pillar off the capsule '
                    'while preserving its mucosa and muscle. A swab placed between the pillar and the '
                    'dissector helps sweep adhesions away. Keeping both pillars intact reduces pain and '
                    'velopharyngeal insufficiency, and lets you sew them together later if bleeding '
                    'persists.'],
                   ['Ligate the lower pole',
                    'Near the end, only a narrow band of tissue holds the lower pole, carrying the facial '
                    "artery's tonsillar branches. Clamp it with a curved tonsil clamp, cut along the clamp, "
                    'and tie it, or seal it with bipolar cautery or a snare, as many US surgeons do. Keep '
                    'instruments off the posterior wall. Stay superficial here, because the glossopharyngeal '
                    'nerve lies deep to the lower fossa.'],
                   ['Control bleeding during the dissection',
                    'Cold dissection can bleed enough to obscure the view. Find the responsible vessel with '
                    'a swab and suction, then use focused bipolar or clamp and tie it. Do not cauterize '
                    'blindly or deep into constrictor, because larger external carotid branches lie just '
                    'lateral to the muscle. Pack the fossa with a tonsil swab before moving to the other '
                    'side.'],
                   ['Repeat on the opposite side',
                    'Remove the second tonsil the same way: medialize, make the anterior pillar incision, '
                    'find the capsular plane, sweep from medial to lateral, release the posterior pillar, '
                    'and ligate the lower pole. Use the same lowest energy settings and the same care around '
                    'the uvula and both pillars, then pack that fossa.'],
                   ['Remove packs and pause',
                    'Slowly remove each tonsil sponge and treat any obvious bleeding point. Release the gag '
                    'and wait a minute or two, so bleeding hidden by suspension pressure can show. Use the '
                    'pause to suction clot from the nasopharynx through the mouth, or gently with a soft '
                    'catheter through the nose, taking care not to injure the septum or turbinates.'],
                   ['Re-inspect both poles under Valsalva',
                    'Re-open the gag and examine each fossa, focusing on the upper and lower poles that '
                    'palate and tongue-base mucosa tend to hide. Ask anesthesia for a Valsalva. For stubborn '
                    'bleeding, place a hemostatic agent and close the pillars with interrupted 2-0 Vicryl. '
                    'This supplements direct control and does not replace it.'],
                   ['Remove the gag and complete counts',
                    'Hold the tube steady while taking out the gag. Check lips, teeth, and tongue against '
                    'your starting notes, and confirm the swab and instrument count and the blood loss. '
                    'After significant bleeding, decompress the stomach with an orogastric tube and clear '
                    'clot. Plan a smooth extubation without straining, and consider a nasal trumpet for '
                    'obstructive sleep apnea.'],
                   ['Set disposition by risk',
                    'For children, US guidelines call for overnight admission under age 3, with severe OSA '
                    'on sleep study (AHI 10 or more, or oxygen nadir below 80%), or with significant '
                    'comorbidities. Consider admitting adults with severe OSA, poor intake or pain control, '
                    'or saturations below 92% on room air. Discharge requires drinking fluids and a '
                    'responsible adult for 24 hours. Bleeding occurs within 24 hours or around days 5–10.']],
 'tors': [['Confirm candidacy and repeat the exam',
           'Selection rests on clinic endoscopy, CT/MRI, and an exam under anesthesia with the intended '
           'retractor to test access and palpate depth and fixation. Exclude a medialized or retropharyngeal '
           'internal carotid artery, carotid encasement, tumor across the tongue-base midline (both lingual '
           'arteries at risk), or spread lateral to the hyoid. Repeat palpation after the retractor is in, '
           'because it distorts the tongue base.'],
          ['Neck first, with feeding-vessel ligation',
           'Do the neck dissection before the primary, either at the same sitting or 7–10 days earlier when '
           'a pharyngocervical communication is likely. Ligate the external carotid branches feeding the '
           'resection: facial for tonsil, lingual for tongue base, and both for the glossotonsillar sulcus; '
           'some surgeons ligate both routinely plus the ascending pharyngeal. If the constrictor will be '
           'breached, pack gauze over the vessels from the neck side.'],
          ['Airway and protection before docking',
           'Use the smallest oral tube that ventilates adequately, or a contralateral nasal tube. Sew the '
           'tube to the opposite retromolar trigone. Keep the inspired oxygen fraction (FiO2) low because of '
           'monopolar fire risk, and rehearse rapid undocking. Fit foam-and-plastic eye shields, thin '
           'vacuum-formed dental guards, and a lip retractor. Require full paralysis and secure all lines '
           'beforehand, since sudden jaw closure against the arms is dangerous.'],
          ['Retraction, positioning and docking',
           'Place a tongue-tip traction stitch and tag it outside the mouth so it is removed at the end. For '
           'tonsil, use a mouth gag such as Crowe-Davis or an FK retractor (the atlas uses a Boyle-Davis '
           'gag); use the Feyh-Kastenbauer retractor with a 30-degree scope for tongue base. Avoid a '
           'shoulder roll and over-extension. Docking side depends on the robotic platform; monopolar goes '
           'on the tumor side.'],
          ['Read the inside-out anatomy',
           'Think in levels. At the tonsil, lateral to the superior constrictor, there are no named external '
           'carotid branches, but the internal carotid lies posterolaterally in the parapharyngeal fat, '
           'behind the styloid muscles. Lower down, the facial artery runs between the superior and middle '
           'constrictors, medial to stylohyoid. The lingual artery lies lateral to the middle constrictor '
           'just above the greater hyoid cornu. Glossopharyngeal branches enter between the constrictors.'],
          ['Mark mucosal margins',
           'Mark the cut lines on the surface first, allowing about 1 cm of normal mucosa, because mucosa '
           'shrinks substantially once excised and fixed. Plan the sequence so tissue already freed does not '
           'fall into and obscure the next cut. Make the steps that define the margin early, while the '
           'anatomy is still undistorted.'],
          ['Lateral oropharyngectomy: incision and parapharyngeal entry',
           'Cut through buccal mucosa along the pterygomandibular raphe and up through soft palate mucosa, '
           'curving the upper limb laterally. At the top outer corner, open the plane between medial '
           'pterygoid and superior constrictor into the parapharyngeal space. Pull the constrictor medially '
           "and sweep parapharyngeal fat laterally off the specimen. That fat pad is the internal carotid's "
           'cushion, so keep it.'],
          ['Superior and medial limits',
           'Carry the cut up to where palatoglossus and palatopharyngeus meet, keeping a generous cuff, '
           'because cut muscle retracts and can bare the upper tonsil pole. Extend lateral to the uvula and '
           'through into the nasopharynx if needed. Early on, score index cuts in the posterior pharyngeal '
           "wall mucosa only, so the medial-to-lateral dissection doesn't take too much posterior wall."],
          ['Handle fascia and small vessels',
           'Meeting fascia, spread bluntly to show what lies beneath instead of cutting through it. Expect '
           'tonsillar, ascending palatine, and ascending pharyngeal branches feeding the constrictor. '
           'Cauterize small ones and clip named vessels before dividing them. Internal carotid pulsation may '
           'be felt beneath the parapharyngeal fat, and any visible pulsation means you are too lateral.'],
          ['Styloglossus and stylopharyngeus',
           'Styloglossus comes first, superficial and lateral, running obliquely. Divide it about 1 cm out '
           'from the constrictor plane, where the gap between superior and middle constrictors otherwise '
           'risks a close margin. The lingual artery lies 5–8 mm deep to it, so clip that vessel along its '
           'exposed length. Then separate stylopharyngeus from prevertebral fascia and divide it with the '
           'constrictor as one layer, sparing the glossopharyngeal nerve.'],
          ['Lateral oropharyngectomy: inferior cuff',
           'Inferiorly, include about 1 cm of tongue-base muscle between the pillars, and more if the tonsil '
           'cancer reaches onto the tongue base. Push the tongue base back with the Maryland while the '
           'assistant retracts forward, and cut medial to lateral. Stay superficial to styloglossus until '
           'exposure is wide, so a narrow field never has to absorb a major bleed.'],
          ['Tongue base: lateral and anterior cuts',
           'Secure the tube to the opposite side with a tongue-to-retromolar stitch and expose with the '
           'Feyh-Kastenbauer and 30-degree scope. Cut laterally first, taking the lower tonsil if needed, '
           'down only to styloglossus depth. Continue medially as the anterior horizontal cut just behind '
           'the blade, about 1 cm deep and angled toward the hyoid, keeping the blade tip off the margin.'],
          ['Tongue base: midline cut sets depth',
           'From the medial end of the horizontal cut, incise in the midline down to the vallecula. This is '
           'a safe corridor with no major vessels, and it shows the final depth. Then dissect medial to '
           'lateral at that depth until the dorsal lingual loop or the lingual trunk appears. Clip it before '
           'dividing. The hypoglossal nerve runs deeper and more lateral than the artery.'],
          ['Tongue base: inferior cut and bleeding control',
           'Cut the inferior mucosa at the vallecula to spare epiglottic mucosa, and keep the epiglottis in '
           'view throughout. This cut can be made earlier to fix the lower limit. When the specimen hangs '
           'only by its inferior mucosa, pull it toward the instrument to finish. If the lingual artery '
           'bleeds, the assistant presses externally at the greater hyoid cornu until clips are on.'],
          ['Tongue base mucosectomy for unknown primary',
           'Incise vertically in the midline from the circumvallate papillae to the vallecula, just into '
           'muscle. Then cut horizontally to the glossotonsillar sulcus. Dissect medial to lateral in the '
           'avascular plane deep to lingual tonsil and superficial to minor salivary glands and muscle. Use '
           'the Maryland as a retracting claw, not a grasper. Take each side separately, orienting it before '
           'starting the other side.'],
          ['Orient, mount and take margins',
           'Reorient the specimen before the final cut so the assistant removes it the right way up. Pin it '
           'on cork with its convex deep surface up, stretching the edges to limit shrinkage. Photograph and '
           'label it, mark edges with colored pins, and send bed margins or frozen sections where uncertain. '
           'Tell pathology that retracted muscle can make the deep margin look falsely close.'],
          ['Inspect the bed and decide on coverage',
           'Look for an exposed internal carotid artery or large named vessel, a communication with the '
           'neck, and residual bleeding, and test with a Valsalva maneuver before undocking. Most defects '
           'heal well by secondary intention. Use a pedicled or free flap for a pharyngocervical '
           'communication, exposed major arteries, or a salvage or irradiated field. Fibrin glue or matrix '
           'are lesser options.'],
          ['Airway, feeding and bleed plan',
           'Choose between extubation and overnight intubation based on tongue swelling; routine '
           'tracheostomy is rarely needed for early cases. Place a nasogastric tube and have speech-language '
           "pathology clear oral intake. Use multimodal analgesia, plus steroids if your unit's practice "
           'includes them. Warn that bleeding peaks around days 5–10, give written instructions (head down, '
           'call emergency services), and plan anticoagulant timing carefully.']],
 'total-laryngectomy': [['Agree the airway handover',
                         'Before induction, settle with anesthesia how the airway moves from mouth to neck: '
                         'an oral tube for the dissection, then a fresh cuffed tube placed straight into the '
                         'opened distal trachea just before the larynx is detached. A patient who is already '
                         'obstructing gets an awake tracheostomy under local first, and that tube stays for '
                         'the whole case.'],
                        ['Position, feeding tube, and surface marks',
                         'Supine with a shoulder roll and a head ring holding the head midline and extended. '
                         'Place a nasogastric feeding tube and confirm its position. Prep the neck and the '
                         'oral cavity and drape so anesthesia can still reach the mouth. Palpate and mark '
                         'the SCM borders, hyoid, thyroid notch, cricoid, sternal notch, and a stoma site '
                         'about halfway between cricoid and notch.'],
                        ['Incision and subplatysmal flaps',
                         'With bilateral neck dissection, use an apron incision running mastoid to mastoid '
                         'and dipping to roughly the cricoid arch. The stoma goes at its lower edge or '
                         'through a separate opening 3–4 cm lower. Without a neck dissection, a transverse '
                         'incision at thyroid cartilage level plus a stomal incision is enough. Infiltrate '
                         'with lidocaine-epinephrine and raise the upper flap subplatysmally to 3–4 cm above '
                         'the hyoid.'],
                        ['Neck dissection before the larynx',
                         'For untreated disease, finish the planned unilateral or bilateral neck dissection '
                         'before you mobilize the larynx. This defines the carotid, IJV, vagus, and '
                         'hypoglossal nerve on each side, which become the lateral limits of the laryngeal '
                         'dissection. If a free flap may be needed, keep candidate recipient vessels '
                         'intact.'],
                        ['Divide the strap muscles',
                         'Find the prelaryngeal strap muscles at the hyoid and divide them above and below '
                         'with monopolar cautery to limit oozing. This opens the anterior laryngeal '
                         'framework from hyoid to trachea. Where tumor has broken through the cartilage '
                         'anteriorly, leave the overlying straps on the specimen rather than peeling them '
                         'off the tumor.'],
                        ['Free the hyoid',
                         'Grasp the hyoid body and pull it down and forward to show its upper edge. Release '
                         'mylohyoid, geniohyoid, the digastric sling, and hyoglossus from medial to lateral, '
                         'staying on bone; the lingual artery and hypoglossal nerve sit just beyond '
                         'hyoglossus near the greater cornu. The atlas usually removes the hyoid separately, '
                         'but many US surgeons routinely keep it on the specimen so the pre-epiglottic space '
                         'stays en bloc.'],
                        ["Decide the thyroid gland's fate",
                         'Divide the isthmus. For anterior tumors invading cartilage and for most pyriform '
                         "sinus primaries, the ipsilateral lobe goes with the larynx, so ligate that side's "
                         'superior and inferior thyroid vessels. Otherwise peel both lobes off the larynx '
                         'and trachea while keeping their inferior blood supply intact. Look for and keep '
                         'viable parathyroid tissue on the retained side.'],
                        ['Superior cornua and laryngeal pedicles',
                         'Divide the superior cornu of the thyroid cartilage on each side. Rotate the larynx '
                         'to expose the opposite superior laryngeal neurovascular bundle, then ligate and '
                         'divide it, keeping the main superior thyroid artery intact when that thyroid lobe '
                         'stays or the vessel may serve as a free-flap recipient. Repeat on the other side, '
                         'hugging the laryngeal framework with the carotid sheaths kept lateral.'],
                        ['Save pyriform sinus mucosa',
                         'Divide the constrictor muscles sharply along the lateral edge of the thyroid ala. '
                         'When the tumor allows, bluntly lift the pyriform sinus mucosa off the inner '
                         'lateral and upper surface of the thyroid cartilage so that it stays with the '
                         'patient. Every bit of healthy pharyngeal mucosa kept here makes the later closure '
                         'looser and safer.'],
                        ['Open the trachea and secure the stoma edge',
                         'Enter the trachea between the second and third rings, or lower if there is '
                         'subglottic extension. Before completing the cut, stitch the anterior tracheal wall '
                         'to the inferior skin flap so a dislodged tube can be replaced quickly. If a '
                         'tracheostomy is already present, excise it with a cuff of surrounding skin to '
                         'lower the risk of peristomal recurrence.'],
                        ['Check the inferior margin, then switch tubes',
                         'Look up into the subglottis from the tracheotomy to confirm enough tumor-free '
                         'airway below the lesion. Only then withdraw the oral tube and pass a new cuffed '
                         'tube into the distal trachea, with the sterile circuit run across the field. From '
                         'this point, ventilation is through the neck only. Never finish dividing the '
                         'trachea before this tube is secure.'],
                        ['Complete the tracheal cut and separate the party wall',
                         'Divide the membranous posterior wall with a cut that bows slightly upward in the '
                         'middle, leaving extra posterior mucosa for a roomier stoma. Then bluntly separate '
                         'the back of the cricoid and trachea from the front of the esophagus and '
                         'hypopharynx, working upward while keeping the esophageal wall intact.'],
                        ['Enter the pharynx where the tumor is not',
                         'For glottic and subglottic tumors, enter through a transverse vallecular cut '
                         'between tongue base and epiglottis. Grasp the epiglottis tip, divide the folds on '
                         'each side, and run the cuts down both sides to meet behind the cricoid, sparing '
                         'the esophageal inlet. For tumors at the vallecula or tongue base, enter from below '
                         'at the interarytenoid level instead, so the tumor stays in view.'],
                        ['Margins and frozen sections',
                         'Take only as much pharyngeal mucosa and muscle as oncology demands. Send frozen '
                         'sections from the tongue base cut, both pyriform sinus edges, and the postcricoid '
                         'edge, and resect more if any are involved. Orient the specimen for pathology. Then '
                         'irrigate and get meticulous hemostasis before reconstruction begins.'],
                        ['Primary TEP and cricopharyngeal myotomy',
                         'If voice restoration is planned, create the primary tracheoesophageal puncture '
                         'now, before the pharynx is closed (see the TEP card). With a finger in the '
                         'esophagus, cut the cricopharyngeus in or near the posterior midline down to, but '
                         'not through, the mucosa. This lowers the risk of a spasming segment that blocks '
                         'prosthetic voice, and it also helps swallowing.'],
                        ['Close the pharynx watertight',
                         'Close with inverting sutures in either a T or a straight vertical line, aiming for '
                         'a tension-free, watertight seal. A linear stapler gives a quick, tight closure '
                         'with fewer fistulas, but only for tumors confined inside the larynx, because the '
                         'tumor is not seen during closed stapling. Test the closure, for example with '
                         'saline or air through the nasogastric tube, and reinforce any leak.'],
                        ['Reinforce or reconstruct',
                         'In a previously irradiated neck, cover the pharyngeal suture line with '
                         'vascularized tissue, because simple closures there often leak and become infected. '
                         'The atlas uses a pectoralis major myofascial onlay; many US centers use either '
                         'pectoralis or a free fasciocutaneous onlay such as radial forearm or ALT. If too '
                         'little mucosa remains after partial or total pharyngectomy, replace it with a '
                         'regional or free flap, or a gastric pull-up.'],
                        ['Drains, stoma, and early plan',
                         'Bring suction drains out through separate stab wounds, away from the pharyngeal '
                         'closure. Sew the tracheal edge to skin circumferentially, covering bare cartilage. '
                         'Post signs that the patient is a neck breather who cannot be intubated through the '
                         'mouth, and keep stoma supplies at the bedside. Remove drains under about 20 '
                         'mL/day. Check calcium and PTH early and TSH later. Start oral intake around day '
                         '4–7, later after radiation.']],
 'total-thyroidectomy': [['Preoperative planning',
                          'Document vocal fold function by laryngoscopy, confirm a euthyroid state, and '
                          'review imaging for extrathyroidal extension, nodal disease, tracheal or '
                          'esophageal invasion and substernal extent. Decide in advance whether central neck '
                          'dissection is therapeutic, elective or not indicated. Discuss with the patient '
                          'the possibility of staging the second side and, when invasion is suspected, nerve '
                          'or airway resection.'],
                         ['Airway and nerve monitoring',
                          'Place an electromyographic endotracheal tube with electrodes at the vocal folds, '
                          'confirmed with video laryngoscopy if needed, and use only a short-acting '
                          'paralytic. For large compressive goiters, plan the airway jointly with anesthesia '
                          'beforehand: a smaller tube or awake fiberoptic intubation may be chosen. Aim for '
                          'an initial vagal or recurrent nerve amplitude of roughly 500 microvolts or more.'],
                         ['Positioning and incision',
                          'Place a shoulder roll and head ring, extend the neck within safe limits, and '
                          'raise the head of the bed 15 to 30 degrees. Mark the thyroid notch, cricoid, '
                          'sternal notch and the borders of the sternocleidomastoid (SCM) muscles, then '
                          'place the incision in a low skin crease. Lengthen it for substernal goiters so '
                          'that a sternotomy, if needed, adds little neck scar.'],
                         ['Flaps and midline',
                          'Raise subplatysmal flaps from the thyroid notch to the sternal notch, superficial '
                          'to the anterior jugular veins, which may be engorged in large goiters. Split the '
                          'midline raphe vertically from the hyoid to the sternal notch so the straps can be '
                          'pulled well laterally.'],
                         ['Assess the strap planes for invasion',
                          'Small focal adhesions from prior fine-needle aspiration are expected; dense loss '
                          'of the normal areolar plane is suspicious for extrathyroidal extension. When '
                          'unsure, take a cuff of sternothyroid, and sternohyoid if needed, en bloc as the '
                          'ventral margin. If both strap layers are resected bilaterally, consider an '
                          'acellular dermal graft or local flap to prevent laryngotracheal tethering to '
                          'skin.'],
                         ['Pick the first side',
                          'For asymmetric goiters start with the smaller lobe; removing it and the isthmus '
                          'first frees the dominant lobe, relieves tension, and makes its nerve and '
                          'parathyroids easier to find. In very large goiters, divide the isthmus early so '
                          'the operation becomes two lobectomies. Obtain a baseline vagal signal in the '
                          'carotid sheath before dissection.'],
                         ['Lateral mobilization',
                          'Strip the strap fascia off the lobe laterally to the carotid sheath; divide the '
                          'sternothyroid partially if needed to reach the superior pole in a big gland. '
                          'Ligate the middle thyroid vein. Avoid forceful handling, which can avulse the '
                          'internal jugular vein.'],
                         ['Superior pole',
                          'Develop the space between the medial pole and the cricothyroid and inferior '
                          'constrictor, then ligate the pole vessels individually and close to the capsule. '
                          'As the lobe comes off the lateral larynx, the cricothyroid, cricopharyngeus and '
                          'external branch of the superior laryngeal nerve come into view. Resecting an '
                          'invaded cricothyroid has voice and swallowing consequences; dorsal invasion of '
                          'the constrictors is best addressed after tracing the nerve upward.'],
                         ['Parathyroid preservation',
                          'Follow the posterior contour of the upper pole down to the superior parathyroid, '
                          'usually within about a centimeter of the cricothyroid joint. Seek the inferior '
                          'gland near the lower pole and thyrothymic tissue. Stay on the capsule or '
                          'pseudocapsule so glands are pushed off on their pedicles, not skeletonized; large '
                          'goiters often displace them unpredictably.'],
                         ['Recurrent laryngeal nerve: choose an approach',
                          'Know three routes. Inferior: low in the paratracheal space within Beahr triangle '
                          '(common carotid, inferior thyroid artery and nerve), then follow it up. Lateral: '
                          'at the inferior thyroid artery near the tubercle of Zuckerkandl. Superior: after '
                          'the upper pole is freed, at its laryngeal entry deep to the lower edge of the '
                          'inferior constrictor behind the cricothyroid joint. Use whichever segment is '
                          'undistorted.'],
                         ['Right versus left nerve course',
                          'The left nerve runs nearly parallel in the tracheoesophageal groove and lies more '
                          'medially; the right enters more laterally and crosses obliquely toward the '
                          'cricoid. On the right, roughly 1 in 100 nerves is nonrecurrent, running directly '
                          'from the vagus at the level of the larynx; suspect it if no low nerve is found. '
                          'Preserve all branches and divide terminal arterial branches on the capsule.'],
                         ['Berry ligament and invasion',
                          'Use minimal traction; free the ligament from the nerve with fine instruments, '
                          'bipolar and sharp dissection. Examine the trachea for perichondrial or cartilage '
                          'invasion: superficial disease may be shaved with clear margins, while '
                          'full-thickness invasion needs a planned window or segmental resection. For '
                          'esophageal muscle involvement, a bougie in the lumen helps define planes and '
                          'protect mucosa.'],
                         ['Nerve invasion decisions',
                          'Epineurial tumor can usually be shaved off with good functional recovery; deeper '
                          'invasion rarely clears without leaving tumor. Try to preserve a nerve that still '
                          'had some function preoperatively, accepting sacrifice mainly for aggressive or '
                          'poorly treatable histology after prior discussion. A preoperatively paralyzed '
                          'nerve that still stimulates proximally should be kept when possible.'],
                         ['Checkpoint before the second side',
                          'Remove the first lobe and stimulate. Loss of signal is an amplitude below about '
                          '100 microvolts. First exclude equipment or tube displacement problems. If the '
                          'signal does not recover above half baseline, around 250 microvolts, within 20 '
                          'minutes, paralysis is likely: stop and stage the contralateral side. Delaying '
                          'completion several months is oncologically acceptable for differentiated cancer.'],
                         ['Contralateral lobe',
                          'Repeat the full sequence rather than shortcutting it: lateral mobilization, '
                          'superior pole close to the capsule, both parathyroids on their pedicles, '
                          'recurrent nerve identified and followed to laryngeal entry, terminal vessels on '
                          'the capsule, then Berry ligament with minimal traction.'],
                         ['Central neck dissection when indicated',
                          'Clear prelaryngeal tissue up to the thyroid notch, mindful of the external branch '
                          'on the cricothyroid. Clear pretracheal tissue down to the innominate artery while '
                          'staying on the trachea, leaving the thymus, which may hold an inferior '
                          'parathyroid. For paratracheal clearance expose the carotid from cricoid to inlet; '
                          'on the right, nodes lie dorsal to the nerve, so mobilize it circumferentially, '
                          'accepting traction risk; the left often needs less.'],
                         ['Specimen and parathyroid handling',
                          'Orient the specimen and inspect for parathyroids. An inferior gland that cannot '
                          'keep its blood supply, or one found on the specimen, is confirmed by frozen '
                          'section and autotransplanted in small pieces into an SCM pocket marked with '
                          'clips. Assess function of the first-side nerve before clearing the second '
                          'paratracheal basin.'],
                         ['Hemostasis, final checks and closure',
                          'Irrigate, clear clots, and do at least two Valsalva maneuvers. Confirm both '
                          'nerves and the remaining parathyroids are intact and record final vagal signals. '
                          'Drains are not routine. Close straps leaving a small gap at the bottom. After '
                          'surgery, check calcium and PTH, and watch for stridor and swelling; an expanding '
                          'hematoma with airway compromise is opened at the bedside immediately.']],
 'tracheal-resection': [['Confirm the indication and map the segment',
                         'Endoscopy defines the grade, the distance to the cricoid, glottis, and any stoma, '
                         'the length of the stenosis, how much normal trachea is left, and vocal fold '
                         'motion. CT measures scar thickness in a complete stenosis and shows any outside '
                         'compression. Thin, mature webs under 1 cm with intact cartilage suit endoscopic '
                         'treatment. Longer stenoses, or those with fracture or malacia, need resection, up '
                         'to about 5.5 cm.'],
                        ['Plan induction with the airway team',
                         'Intubate safely past the stenosis using video laryngoscopy, a flexible scope, '
                         'serial bougie dilation, or rigid bronchoscopy, with the smallest tube that '
                         'ventilates. If that fails, place a tracheostomy through the stenotic segment so it '
                         'is removed with the specimen. Never do this through a tracheal tumor, which can '
                         'seed and bleed.'],
                        ['Position and incise',
                         'Hyperextend the head on a shoulder roll. Make a collar incision centered on the '
                         'existing stoma or over the stenosis; it can be extended laterally for a neck '
                         'dissection in cancer cases. Raise subplatysmal flaps up toward the larynx and down '
                         'to the sternal notch.'],
                        ['Expose the trachea in the midline',
                         'Open the midline fascia and retract the strap muscles. Divide the thyroid isthmus, '
                         'then sweep each lobe laterally, staying on the tracheal perichondrium; the lobes '
                         "are tethered to the upper rings by Berry's ligament. This keeps the recurrent "
                         'laryngeal nerves (RLNs) safe in the tracheoesophageal grooves without dissecting '
                         'them out routinely.'],
                        ['Expose the full stenosis before cutting',
                         'Dissect enough to see healthy rings above and below the scar. Do not clear trachea '
                         'far beyond the planned cut lines, because the blood supply is segmental and '
                         'lateral. Confirm the external extent against the endoscopic findings, for example '
                         'by passing a needle while the scope watches inside.'],
                        ['Open the stenosis and look inside',
                         'Make a horizontal cut through the middle of the stenotic segment to inspect the '
                         'lumen directly and see where healthy mucosa begins above and below. This shows '
                         'exactly how many rings need to come out at each end.'],
                        ['Set up cross-field ventilation',
                         'Pull the oral endotracheal tube back to the glottis and tie a stitch to its tip so '
                         'it can be advanced again. Pass a sterile cuffed tube through the operative field '
                         'into the distal trachea and connect it to a sterile circuit. Keep the field tube '
                         'out of the way while sutures are placed.'],
                        ['Resect to healthy airway',
                         'Excise the stenotic segment until healthy cartilage and mucosa are reached at both '
                         'ends. Separate the membranous wall from the esophagus only about 1 to 1.5 cm '
                         'beyond each cut, especially at the distal stump. Once the isthmus is divided, the '
                         "esophagus is the stump's main blood supply. Avoid lateral stripping."],
                        ['Release the distal trachea',
                         'Bluntly free the front of the distal stump with a finger in the pretracheal plane, '
                         'down to the carina or until you feel the innominate artery leaving the aortic '
                         'arch. This usually gains 1.5 to 2 cm. Keep the finger in front of the trachea, '
                         'protect the innominate artery and vein, and avoid sweeping laterally.'],
                        ['Place stay sutures and assess tension',
                         'On each side of the distal stump, pass a 2-0 polyglactin stay suture around a full '
                         'ring at least two rings below the cut, with matching stays on the upper stump. If '
                         'the resection starts at the first ring, place the upper stays through the cricoid, '
                         'well anterior to where the recurrent laryngeal nerves enter. Bring the pairs '
                         'together to judge tension.'],
                        ['Add laryngeal release only if needed',
                         'If tension remains, usually after resections longer than about 4 cm, lower the '
                         'larynx with a release. The atlas uses a thyrohyoid release, dividing the '
                         'thyrohyoid muscles, membrane, and lateral ligaments. Most US surgeons prefer the '
                         'suprahyoid (Montgomery) release, which gives similar length with less dysphagia '
                         'and aspiration. Either can cause temporary swallowing trouble, so use one only '
                         'when needed.'],
                        ['Place the posterior row',
                         'Join the membranous wall of the lower stump to the membranous wall, or posterior '
                         'cricoid mucosa, of the upper stump with four or five interrupted 4-0 polyglactin '
                         'sutures. Place every suture before tying any, spacing them evenly and matching '
                         'mucosa to mucosa so the posterior line stays watertight and the knots sit outside '
                         'the lumen.'],
                        ['Place the lateral and anterior rows',
                         'Complete the circle with ten to twelve 2-0 and 3-0 polyglactin sutures through the '
                         'cartilage along the sides and front. Bring each one out on the outer surface in a '
                         'subperichondrial plane so the knots sit outside the lumen. Keep the sutures in '
                         'order so they can be tied in sequence.'],
                        ['Exchange tubes, flex, and tie',
                         'Remove the distal field tube and advance the oral tube across the suture line, '
                         'keeping its cuff away from the anastomosis. Flex the head with a pillow under the '
                         'occiput. Tie the stay sutures first, then the posterior 4-0 row, then the '
                         'anterolateral sutures from the sides toward the midline.'],
                        ['Test the anastomosis',
                         'Fill the wound with saline and give positive-pressure breaths to look for an air '
                         'leak, reinforcing any leaking point. Check the lumen endoscopically if there is '
                         'any question about alignment or narrowing.'],
                        ['Close and hold the neck in flexion',
                         'Bring the isthmus and straps back together in the midline over the anastomosis, '
                         'and place a drain superficial to the straps. Place chin-to-chest guardian sutures '
                         'to keep the neck flexed. Wake the patient with a transnasal fiberoptic check of '
                         'vocal fold motion, airway space, and edema.'],
                        ['Postoperative anastomotic protection',
                         'Prevent vomiting, coughing, and reflux with antiemetics, cough suppression, and '
                         'acid suppression, and humidify generously. The atlas avoids steroids because they '
                         'impair healing; some US teams give a short course for airway edema. Watch for a '
                         'leak: dry cough, subcutaneous emphysema, or skin redness. Start oral feeding '
                         'around day 2, remove the drain around day 3, cut the guardian sutures around day '
                         '7–8, and plan endoscopic follow-up.']],
 'tracheostomy': [['Prepare consent, labs, and tubes',
                   'Consent should mention that the tracheostomy may become permanent and that the patient '
                   'will lose their voice for a time. Correct any coagulopathy beforehand. Open the chosen '
                   'tube plus one size larger and one size smaller. Do not start until any special tube the '
                   'anatomy needs, such as extra length or reinforcement, is in the room.'],
                  ['Choose the technique and setting',
                   'Use an open approach in the operating room for children, emergencies or impending '
                   'obstruction, laryngeal tumors, obese or short necks, goiters, and anyone who would be '
                   'hard to reintubate. General anesthesia is preferred. If general anesthesia is unsafe, '
                   'perform the open tracheostomy under local anesthesia. Percutaneous tracheostomy has no '
                   'place in an acute airway emergency.'],
                  ['Position and drape',
                   'Place the patient supine with a shoulder roll and the head centered on a head ring to '
                   "extend the neck. Do not hyperextend a child's neck, because the great vessels at the "
                   'thoracic inlet rise into the field. Use square drapes that leave the mouth accessible so '
                   'anesthesia can manage the endotracheal tube.'],
                  ['Mark landmarks and incise',
                   'Mark the thyroid notch, cricoid, and sternal notch. Draw a 3 cm horizontal incision '
                   'halfway between the lower edge of the cricoid and the sternal notch. An incision too '
                   'high or too low makes the case harder, so lengthen it in difficult necks. Infiltrate '
                   'local anesthetic with epinephrine before cutting.'],
                  ['Dissect to the strap muscles',
                   'Go through subcutaneous fat to the straps. Platysma may be thin or absent in the '
                   'midline. Self-retaining retractors hold the skin edges apart. In a heavy neck, remove '
                   'excess fat rather than just retracting it, and bring an assistant for exposure.'],
                  ['Split the straps in the midline',
                   'Open the linea alba vertically and push the straps aside bluntly, sparing the anterior '
                   'jugular veins. Feel for the cricoid at every depth, because it is the key landmark. '
                   "Staying exactly in the midline keeps the carotid sheath and great vessels out of harm's "
                   'way.'],
                  ['Manage the thyroid isthmus',
                   'A small isthmus can be retracted upward and the trachea entered below it. Many surgeons '
                   'prefer to divide it between clamps with transfixion sutures or with cautery, which makes '
                   'later tube reinsertion faster and safer. With a large isthmus, take time to divide it in '
                   'the midline, suture-ligate each cut edge, and confirm hemostasis before opening the '
                   'airway.'],
                  ['Expose and confirm the tracheal level',
                   'Clear the anterior trachea and coagulate any inferior thyroid veins. Count down from the '
                   'cricoid and plan the opening at about the third and fourth rings, staying off the '
                   'cricoid and first ring. Going too low makes a long, deep tract and brings the innominate '
                   'artery closer.'],
                  ['Pre-entry checks with anesthesia',
                   "Inflate the new tube's cuff to test it, then deflate it. Anesthesia takes control of the "
                   'endotracheal tube at the head of the bed. Before opening the airway, ask anesthesia to '
                   'lower the inspired oxygen and stop using monopolar cautery near the trachea. Low-power '
                   'bipolar is acceptable on the tracheal edges.'],
                  ['Open the trachea',
                   'Open the trachea at the third and fourth rings with a small window, an inferiorly based '
                   '(Björk) flap, or a slit; no one method is proven best. Avoid the cuff and the posterior '
                   'wall. Hook the upper edge with a cricoid hook. In children and many adults, place stay '
                   'sutures on each side and tape them to the chest so the stoma can be opened if the tube '
                   'dislodges.'],
                  ['Swap the tubes',
                   'Have anesthesia deflate the endotracheal cuff and withdraw the tube until its tip sits '
                   'just above the window, without removing it. Suction blood and secretions. Insert the '
                   'lubricated tracheostomy tube with its obturator, entering from the side and rotating '
                   'down into the lumen under direct vision. Remove the obturator immediately, insert the '
                   'inner cannula, inflate the cuff, and connect the sterile circuit.'],
                  ['Confirm placement before letting go',
                   'Keep the cricoid hook and retractors in until end-tidal CO2 appears and breath sounds '
                   'are heard on both sides. Only then withdraw the endotracheal tube completely. The '
                   'assistant holds the flange against the skin the whole time. If there is any doubt, pass '
                   'a flexible scope through the tube to confirm it is in the trachea and check its distance '
                   'above the carina.'],
                  ['Achieve hemostasis and close loosely',
                   'Look at the wound edges, the divided isthmus, and the thyroid veins, and control '
                   'bleeding with cautery. Close the skin loosely around the tube so air can escape and does '
                   'not track into surgical emphysema. Secure the flange with skin sutures plus ties or '
                   'Velcro tapes, loose enough to fit one finger. In free-flap patients, avoid neck ties.'],
                  ['Select percutaneous candidates',
                   'Before a percutaneous tracheostomy, the patient must be easy to reintubate orally, '
                   'extend the neck well, and have palpable cartilages. They also need a '
                   'cricoid-to-sternal-notch distance of at least 3 to 4 cm and no coagulopathy, local '
                   'infection, goiter, or midline pulsation. Scan with ultrasound to check for aberrant '
                   'vessels, and make sure a surgeon who can convert to an open case is available.'],
                  ['Perform the percutaneous technique',
                   'Work as a three-person team handling ventilation, bronchoscopy, and the procedure. Pull '
                   'the endotracheal tube back to the cricoid under bronchoscopic view. Make a 2 cm incision '
                   'below the cricoid and pass a needle on a saline syringe at the first-to-second ring in '
                   'the midline; air bubbles confirm entry and the scope confirms position. Pass the wire, '
                   'dilate once without rotating, and railroad the tube.'],
                  ['Hand off and plan aftercare',
                   'Get a chest X-ray and nurse head-up. Keep the obturator, a spare tube of the same size '
                   'and one smaller, and suction at the bedside, with airway signage. Keep cuff pressure '
                   'about 20–30 cm H2O, humidify, and suction regularly. Early bleeding usually comes from '
                   'the window edges, isthmus, or thyroid veins; late bleeding raises concern for innominate '
                   'erosion. First tube change: around day 5–7 open, at least day 7 percutaneous.']],
 'transoral-laser-laryngeal-cancer': [['Map the tumor yourself first',
                                       'The operating surgeon does the endoscopic assessment. Before any '
                                       'laser use, examine the lesion with 0- and 30-degree rigid telescopes '
                                       'to build a three-dimensional picture: anterior commissure, '
                                       'ventricle, subglottis, arytenoid, and any hint of pre-epiglottic '
                                       'spread. Decide in advance between an en bloc excision and a planned '
                                       'transtumoral (Steiner) approach, and which cordectomy type the '
                                       'extent demands.'],
                                      ['Choose the ventilation strategy',
                                       'The airway is shared, so agree on the mode beforehand. A laser-safe '
                                       'reinforced microlaryngeal tube with a saline-filled double cuff '
                                       'gives the most reliable ventilation and protects the lungs from '
                                       'blood, but it hides the posterior glottis. Jet ventilation or '
                                       'tubeless total intravenous anesthesia opens the view, at the cost of '
                                       'airway protection and CO2 monitoring, plus barotrauma risk with '
                                       'jet.'],
                                      ['Laser safety setup',
                                       'Everyone wears eye protection matched to the CO2 wavelength and '
                                       "plume-filtering masks. Cover the patient's face with wet swabs and "
                                       'keep a 50 mL saline syringe on the field. Test the alignment of the '
                                       'visible aiming beam on a wet wooden tongue depressor. Run a laser '
                                       'time-out and keep the inspired oxygen fraction (FiO2) as low as the '
                                       'patient tolerates.'],
                                      ['Know the fire drill',
                                       'In an airway fire, at once remove the endotracheal tube, stop all '
                                       'airway gas flow, remove sponges or other burning material, and pour '
                                       'saline into the airway. Then restore ventilation by mask or '
                                       'reintubation, avoiding extra oxygen if possible, and examine the '
                                       'airway with bronchoscopy for injury and debris. Prevent fire by '
                                       'never aiming across an exposed tube and by shielding the cuff with '
                                       'wet cottonoids.'],
                                      ['Exposure and equipment',
                                       'Pick the laryngoscope size and shape that shows the whole lesion and '
                                       'suspend it for hands-free work. Use the microscope with a '
                                       'micromanipulator, or a fiber handpiece. Keep two suctions running, '
                                       'one on the scope for plume and one for blood and secretions, plus '
                                       'microlaryngeal graspers to manipulate the tumor.'],
                                      ['Set the laser',
                                       'Use CO2 at roughly 2–8 W, continuous or pulsed. Pulsed delivery lets '
                                       'tissue cool between bursts, which means less char and a cleaner '
                                       'margin for pathology. Choose a spot under 1 mm or a straight or '
                                       'curved line pattern. Save defocused continuous high power for '
                                       'debulking an obstructing tumor, not for the oncologic cut.'],
                                      ['Superficial cordectomies (types I–II)',
                                       'Type I (subepithelial) removes epithelium only and is reserved for '
                                       'dysplasia or carcinoma in situ; keep the cut clear of the anterior '
                                       'commissure to avoid a web. Type II (subligamental) removes '
                                       'epithelium, Reinke space, and vocal ligament, with vocalis muscle '
                                       'forming the deep floor. It fits microinvasive cancer. Saline '
                                       'injected under the ligament can help separate it from muscle.'],
                                      ['Transmuscular and total cordectomy (types III–IV)',
                                       'Type III goes through vocalis and handles most T1a cancers without '
                                       'deep muscle invasion. Trim the false fold if it blocks the view. '
                                       'Type IV takes the whole fold from vocal process to just short of the '
                                       'anterior commissure, down to the inner thyroid perichondrium. Its '
                                       'anterior vocal ligament attachment to the thyroid lamina must be cut '
                                       'to free the specimen.'],
                                      ['Extended cordectomies (type V)',
                                       'Va extends across the anterior commissure onto the opposite cord and '
                                       'has largely been replaced by type VI. Vb includes the arytenoid for '
                                       'posterior lesions. Be radical on the first pass there, because '
                                       'margins off the arytenoid are often involved. Vc includes ventricle '
                                       'and false fold. Vd extends onto subglottic mucosa down to the inner '
                                       'cricoid perichondrium.'],
                                      ['Anterior commissure resection (type VI)',
                                       'Start above the vocal ligament insertions at the epiglottic petiole '
                                       'and cut down through the ligaments, detaching them from the thyroid '
                                       'lamina. Remove some false fold for access if needed. Take thyroid '
                                       'cartilage with the specimen if invasion is suspected, and subglottic '
                                       'mucosa or cricothyroid membrane when clearance needs it. Counsel the '
                                       'patient that webbing and voice compromise are likely.'],
                                      ['Transtumoral cut for depth',
                                       'In the Steiner approach, cut through the tumor with the laser and '
                                       'read the cut surface: tumor chars heavily, while normal tissue cuts '
                                       'cleanly. This shows true depth toward the ligament, paraglottic '
                                       'space, or cartilage. Carry the deep cut just beyond tumor and remove '
                                       'it in two or more oriented blocks. Published series have not shown '
                                       'worse local control from planned transection.'],
                                      ['Suprahyoid supraglottic lesions',
                                       'Tumors on the free edge or lingual surface of the epiglottis, the '
                                       'aryepiglottic fold, or the ventricle are well suited to laser work '
                                       'and can usually be taken en bloc because access is good. Bulky '
                                       'lesions can be split to reach their inferior parts. Margins are '
                                       'easier to get in the supraglottis than at the glottis without '
                                       'costing function.'],
                                      ['Infrahyoid epiglottis and pre-epiglottic space',
                                       'Assume pre-epiglottic spread may be present even when imaging is '
                                       'negative. Approach through the vallecula: divide the median '
                                       'glossoepiglottic fold and split the suprahyoid epiglottis in the '
                                       'sagittal plane to expose the pre-epiglottic fat and the laryngeal '
                                       "surface. Then cut through the fat to define the tumor's anterior "
                                       'limit. Never remove both arytenoids, which leaves an incompetent, '
                                       'aspirating larynx.'],
                                      ['Control bleeding before vessels retract',
                                       'Coagulate or clip sizable vessels as they come into view, before '
                                       'they are divided and retract out of reach, especially in the '
                                       'supraglottis and paraglottic space. Avoid building up char that '
                                       'hides the true deep margin. Keep suction on the bleeding point and '
                                       'use the second suction for plume.'],
                                      ['Orient and mount the specimen',
                                       'Check every specimen for margin adequacy. Small glottic pieces '
                                       'cannot be pinned, so lay them flat on a carrier such as card or foam '
                                       '(some European units use a cucumber slice) and mark orientation. Add '
                                       'operative photos and a labeled diagram to the pathology form, and '
                                       'label each separately sent margin by site. Review orientation with '
                                       'the pathologist directly when possible.'],
                                      ['Take patient-side margins',
                                       "Laser coagulation at the cut edge can make the pathologist's margin "
                                       'read unreliable. Take separate marginal biopsies from the bed of the '
                                       'resection, especially wherever there is doubt, and label them by '
                                       'site. Before taking down the exposure, re-examine the airway '
                                       'caliber, hemostasis, exposed cartilage, and any raw opposing '
                                       'surfaces at the anterior commissure that could web.'],
                                      ['Airway plan at the end',
                                       'Give intravenous dexamethasone at induction and repeat if needed. '
                                       'Watch for stridor in recovery and treat with nebulized epinephrine '
                                       '(US units often use racemic epinephrine; the atlas lists 5 mL of '
                                       '1:1000). Most limited glottic resections go home the same day on '
                                       'simple analgesia. Supraglottic resections need speech-language '
                                       'pathology assessment before and after surgery because of aspiration '
                                       'risk.'],
                                      ['Pathology-driven next steps',
                                       'Review the invasive cancer at the tumor board. Close or involved '
                                       'margins call for a re-look microlaryngoscopy, with re-resection as '
                                       'needed, at about six weeks. Follow every patient with serial '
                                       'flexible laryngoscopy and photographs for comparison, and add '
                                       'narrow-band imaging where available. Laser surgery leaves repeat '
                                       'laser, open partial surgery, total laryngectomy, and radiotherapy '
                                       'all available for salvage.']],
 'zenker': [['Confirm the diagnosis and predict exposure',
             'Review the barium swallow to confirm a Zenker diverticulum and estimate the pouch size. At the '
             'bedside, look for features that make the bar hard to expose: limited mouth opening, prominent '
             'upper incisors, retrognathia, and a stiff cervical spine. Long-term success depends heavily on '
             'how well the bar can be exposed, so these findings shape the plan and the consent.'],
            ['Consent for alternatives and conversion',
             'Consent for stapler and CO2 laser division, and for conversion to an open transcervical '
             'approach if the bar cannot be exposed. Discuss flexible endoscopic division by '
             'gastroenterology for patients unfit for general anesthesia, and cricopharyngeal botulinum '
             'toxin in selected cases. Most patients are elderly, so review comorbidities and anticoagulants '
             'with anesthesia.'],
            ['Have every tool in the room',
             'Have both a large spreadable Weerda-type diverticuloscope and a thinner non-spreadable one, an '
             'endoscopic linear stapler (Endo GIA 30 type, with a shortened tip where local rules allow), a '
             'CO2 laser with microscope, and 0- and 30-degree telescopes. A small pouch (under about 3 cm) '
             'or narrow anatomy often admits only the thin scope, and that means laser rather than stapler.'],
            ['Anesthesia and setup',
             'Use general anesthesia with a cuffed endotracheal tube protecting the airway, patient supine. '
             'Fit a dental guard and protect the lips, because the diverticuloscope levers against the upper '
             'teeth. If the laser may be used, apply laser precautions: a laser-safe tube or protected cuff, '
             'wet eye and face cover, and low inspired oxygen.'],
            ['Inspect and empty the pouch',
             'Pass a rigid endoscope and inspect the diverticular sac. Suction and pick out retained food '
             'and tablet debris so the floor and walls are clearly visible. This also lowers contamination '
             'of the cut edges and gives you a clear view of the true esophageal lumen, which lies anterior '
             'to the pouch.'],
            ['Seat the diverticuloscope',
             'Advance the spreadable diverticuloscope slowly and gently, guiding one lip into the pouch and '
             'the other into the esophageal lumen, then open the lips. Forcing the scope causes mucosal '
             'tears or perforates the thin pouch wall. When seated, suspend the scope so both hands are '
             'free.'],
            ['Identify the bar',
             'The bar is the shared wall between pouch and esophagus: pouch lining on its back surface, '
             'esophageal lining on its front, and the cricopharyngeus muscle in the middle. Center it '
             'between the scope lips. If you cannot see it clearly all the way to its lower end, switch to '
             'the thinner scope or convert to an open approach rather than dividing blind.'],
            ['Look at the pouch floor',
             'Before dividing anything, examine the bottom of the pouch with a rigid telescope to exclude a '
             'hidden squamous cell carcinoma. Cancer in a Zenker pouch is rare, roughly 1% or less, but it '
             'is missed if nobody looks. Biopsy any mucosal irregularity, ulcer, or mass, and do not staple '
             'across a suspicious lesion.'],
            ['Position the stapler',
             'Pass the stapler so its shortened tip goes into the pouch and the staple cartridge into the '
             'esophageal lumen, straddling the bar in the midline. Advance until the tips reach the pouch '
             'floor; traction sutures placed in the bar, used by many US surgeons, pull it further into the '
             'jaws. Confirm with an angled telescope before closing that no lateral wall or tube is caught.'],
            ['Fire the stapler',
             'Close and fire. In one action the device divides the common wall, including the '
             'cricopharyngeus, and seals each cut edge with three staggered rows of staples. Sealing the '
             'mucosal edges is the main reason the stapler is preferred, because it cuts the risk of '
             'infection tracking down into the neck and mediastinum.'],
            ['Deal with the residual spur',
             'After removing the stapler, inspect the divided bar. A small residual septum at the bottom, '
             'beyond the reach of the staples, can be cut with microscissors or a few CO2 laser passes. In a '
             'very large pouch, reload and fire a second cartridge to complete the division. A remaining '
             'muscular ridge is the classic cause of persistent symptoms.'],
            ['Laser division through the thin scope',
             'When only the thin diverticuloscope fits, divide the common wall and cricopharyngeus with the '
             'CO2 laser through the microscope. Stay exactly in the midline of the septum and work downward '
             'until the muscle fibers are fully divided, without going through the fascia beyond them. '
             'Lateral drift risks neck perforation, and going too deep risks entering the mediastinum.'],
            ['Confirm one common channel',
             'At the end, the pouch and esophagus should form one lumen with no residual bar. Check the cut '
             'edges for bleeding and the floor for any defect suggesting perforation. Remove the scope '
             'gently and inspect the teeth, lips, and posterior pharyngeal wall for instrument injury.'],
            ['Convert when exposure fails',
             'If neither diverticuloscope shows the bar well, do not attempt a partial blind division. '
             'Proceed to the consented open approach (see the cricopharyngeal myotomy card), or stop and '
             'replan. Poor exposure of the bar is the strongest predictor of a failed endoscopic division, '
             'so document what limited the view for the next surgeon.'],
            ['Postoperative diet and observation',
             'Keep the patient off oral intake the day of surgery, then liquids for a day, then soft foods '
             'for about a week. A feeding tube is rarely needed, and most elderly patients stay one night. '
             'Many US surgeons obtain a contrast esophagram before starting diet, especially after laser '
             'division. Fever, tachycardia, neck crepitus, or worsening chest or back pain suggest '
             'perforation and need prompt imaging.'],
            ['Pain and follow-up',
             'Laser division in particular can cause severe pain behind the sternum that mimics a heart '
             'attack; work it up rather than dismissing it, and treat with analgesia for a few days. Judge '
             'long-term success by symptoms; a routine later swallow study is not required once the patient '
             'eats well. Symptomatic recurrence is uncommon and can usually be treated with repeat '
             'endoscopic division.']]}

ATLAS_CHAPTERS = {'central-neck': '46 (Total Thyroidectomy with Level VI and VII Neck Dissection; Fundakowski, Nixon, Kamani '
                 'and Randolph)',
 'completion-thyroidectomy': '44 (Total Unilateral Lobectomy and Isthmusectomy); 46 (Total Thyroidectomy '
                             'with Level VI and VII Neck Dissection). Neither chapter is dedicated to '
                             'completion surgery; completion-specific points are carried from the old card '
                             'and marked where the atlas is silent. Chapter 48 consulted for postoperative '
                             'calcium and laryngoscopy points.',
 'conservation-laryngectomy': '38 (Vertical Partial Laryngectomy) and 39 (Horizontal Partial Supracricoid '
                              'Laryngectomy with Crico-Hyoidopexy or Crico-Hyoido-Epiglottopexy). Steps 3–8 '
                              'cover the vertical operation; steps 9–18 cover the supracricoid operation.',
 'cp-myotomy': '11 (Open Approach to Pharyngeal Pouch and Cricopharyngeal Myotomy). Pharyngeal pouch = '
               'Zenker diverticulum.',
 'ctr': '5 (Tracheal and Cricotracheal Resection and Anastomosis for Subglottic and/or Proximal Tracheal '
        'Stenoses), using the cricotracheal content (resection types B to E).',
 'deep-neck-drain': '7 (Incision and Drainage of Deep Neck Space Infections; Vaz, Rovira-Casa and Dias)',
 'four-gland': '49 (Bilateral Exploration Parathyroidectomy).',
 'free-flap-basics': '50 (Principles of Soft Tissue Free Flap Reconstruction in Head and Neck Cancer) and 51 '
                     '(Bony Reconstruction in the Head and Neck).',
 'free-flap-takeback': '50 (Principles of Soft Tissue Free Flap Reconstruction in Head and Neck Cancer), '
                       'mainly the post-operative care and flap monitoring sections; 51 (Bony Reconstruction '
                       'in the Head and Neck), post-operative care and flap monitoring sections; 27 (Floor '
                       'of the Mouth Cancer) for the pectoralis major fallback after flap failure.',
 'neck-dissection': "12 (Radical and Modified Radical Neck Dissection; Morlandt and D'Cruz), 13 (Functional "
                    'Neck Dissection; Rodrigáñez, Castro and Gavilán)',
 'oral-composite': '31 (Composite Resection and Segmental Mandibulectomy) as primary source; supplemented by '
                   '30 (Perioral Marginal Mandibulectomy), 27 (Floor of the Mouth Cancer), 32 (Access '
                   'Procedures: Visor Flap, Lip Split, Mandibulotomy, and Lingual Release), and 26 '
                   '(Transoral Partial Glossectomy) for margin marking.',
 'parathyroidectomy': '49 (Bilateral Exploration Parathyroidectomy). The chapter is written for bilateral '
                      'exploration; its anatomy, landmark sequence and gland locations apply directly, while '
                      'focused-approach steps (intraoperative PTH protocol, limited exposure, conversion) '
                      'are carried from the old card and marked where the atlas does not cover them.',
 'parotid-total': '17 (Total Conservative and Radical Parotidectomy; Vander Poorten and Elliott)',
 'parotidectomy': '16 (Partial Parotidectomy Including Deep Lobe and Dumb Bell Tumours; Roland, Casasayas '
                  'and Quer)',
 'pharyngocutaneous-fistula': '37 (Total Laryngectomy), fistula prevention and complication-management '
                              'sections only. One closure-pattern point is cross-referenced from 40 (Voice '
                              'Restoration Following Laryngectomy).',
 'reop-parathyroid': '49 (Bilateral Exploration Parathyroidectomy). The chapter covers failed exploration, '
                     'ectopic sites, remnant marking and relocalization but has no dedicated reoperative '
                     'technique; reoperative steps from the old card are kept and marked where the atlas is '
                     'silent. Chapter 48 consulted for routine pre- and postoperative laryngoscopy.',
 'reop-thyroid': '46 (Total Thyroidectomy with Level VI and VII Neck Dissection) for nerve approaches, '
                 'invasion decisions and central compartment dissection; 48 (Surgery for Intrathoracic '
                 'Goitres) for recurrent goiter, airway planning and extracervical approach criteria; 44 '
                 '(Total Unilateral Lobectomy and Isthmusectomy) for basic lobe technique. No chapter is '
                 'devoted to reoperative central neck surgery; reoperative-specific strategy from the old '
                 'card is kept and marked where the atlas is silent.',
 'sialendoscopy': '15 (Transoral Removal of Salivary Stones; Edkins and Fagan), 18 (Transoral Removal of '
                  'Intracanalicular Stones in the Submandibular Glands; Gottlieb and Cascarini)',
 'submandibular-gland': '19 (Submandibular Gland Excision; Kaschke and Schulz-Schönhagen)',
 'tep': '40 (Voice Restoration Following Laryngectomy).',
 'thyroglossal': '9 (Thyroglossal Duct Cyst; Rajaram, Smith and Hilmi)',
 'thyroid-lobectomy': '44 (Total Unilateral Lobectomy and Isthmusectomy); 48 (Surgery for Intrathoracic '
                      'Goitres) for substernal-extension, isthmus-timing and Berry-ligament pearls.',
 'tonsillectomy': '33 (Standard Tonsillectomy).',
 'tors': '34 (Transoral Resection for Oropharyngeal Neoplasms, covering transoral ultrasonic and laser '
         'techniques, transoral anatomy, and specimen handling) and 35 (Robotic Surgery: lateral '
         'oropharyngectomy, tongue base mucosectomy, tongue base resection).',
 'total-laryngectomy': '37 (Total Laryngectomy). Primary TEP step cross-referenced to 40 (Voice Restoration '
                       'Following Laryngectomy) of the same atlas.',
 'total-thyroidectomy': '46 (Total Thyroidectomy with Level VI and VII Neck Dissection); 44 (Total '
                        'Unilateral Lobectomy and Isthmusectomy) for the shared lobe technique; 48 (Surgery '
                        'for Intrathoracic Goitres) for substernal extension, smaller-lobe-first strategy '
                        'and closure checks.',
 'tracheal-resection': '5 (Tracheal and Cricotracheal Resection and Anastomosis for Subglottic and/or '
                       'Proximal Tracheal Stenoses), using the Type A tracheal resection content.',
 'tracheostomy': '4 (Percutaneous Tracheostomy and Open Standard Surgical Tracheostomy).',
 'transoral-laser-laryngeal-cancer': '36 (Transoral Laser Resection for Glottic and Supraglottic Tumours).',
 'zenker': '10 (Endoscopic Approaches to the Pharyngeal Pouch: Stapling Technique). Pharyngeal pouch = '
           'Zenker diverticulum.'}
