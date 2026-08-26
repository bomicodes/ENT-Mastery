"""v20.0 procedure-specific OR Tomorrow operative sequences.

This layer replaces the generic v19 sequence wrapper with concise, resident-level
operative choreography. Content is original paraphrase/synthesis from standard
operative references already supplied by the user; no textbook prose is copied.
"""

GENERIC_PHRASES = (
    "perform the planned exposure",
    "procedure-appropriate approach",
    "same principles",
    "same nerve and parathyroid principles",
    "reinspect the operative field for hemostasis, anatomic integrity",
)


def _text(slug, op):
    return (str(slug) + " " + str(op.get("title", "")) + " " + str(op.get("domain", ""))).lower()


def _has(t, *needles):
    return any(n in t for n in needles)


# Each branch returns an explicit sequence, not a generic family shell.
def _sequence_for(slug, op):
    t = _text(slug, op)

    # ---------- THYROID / PARATHYROID ----------
    if _has(t, "reoperative parathyroid", "reop-parathyroid", "reoperative-parathyroid"):
        return [
            "Re-review prior operative notes and localization, then enter through the previous central-neck incision while anticipating scarred planes and displaced RLN/parathyroid anatomy.",
            "Raise subplatysmal flaps only as needed and develop the least-scarred route toward the localized target rather than performing broad blind scar dissection.",
            "Identify a reliable RLN landmark away from the densest scar—often lower in the tracheoesophageal groove or at the laryngeal entry point—and define the nerve before mobilizing tissue attached to it.",
            "Correlate the suspected gland with the carotid sheath, tracheoesophageal groove, thyrothymic tract, retroesophageal space, mediastinal descent, and prior clips or scar.",
            "Dissect directly on the abnormal gland, preserving the RLN and avoiding unnecessary devascularization of any remaining normal parathyroid tissue.",
            "Control the gland's vascular pedicle and remove the target intact; send tissue confirmation when localization or scar makes identity uncertain.",
            "Interpret intraoperative PTH against the pre-excision baseline and the patient's disease pattern; if the fall is inadequate, reassess localization and multigland disease before extending the exploration.",
            "Perform meticulous hemostasis in the reoperative bed, confirm nerve integrity when monitoring is used, and close without compressing the trachea or nerve.",
        ]
    if _has(t, "four-gland", "bilateral exploration", "bilateral parathyroid", "4-gland"):
        return [
            "Open the central neck through a low transverse incision, raise subplatysmal flaps, separate the strap muscles in the midline, and expose both thyroid lobes sufficiently for bilateral exploration.",
            "Begin on one side by mobilizing the thyroid medially and identifying the RLN and inferior thyroid artery relationship before searching directly behind the lobe.",
            "Identify the superior gland near the posterior upper/mid thyroid and the inferior gland along the lower pole–thyrothymic tract; preserve each gland's vascular pedicle while judging size and morphology.",
            "Repeat the same anatomic survey on the opposite side so that all four expected glands are accounted for before deciding what to remove.",
            "If a gland is missing, search embryologic ectopic pathways systematically—thyrothymic ligament/thymus, tracheoesophageal groove, retroesophageal space, carotid sheath, and mediastinal direction as indicated.",
            "Perform the planned subtotal resection or targeted removal of abnormal glands while leaving well-vascularized parathyroid tissue when clinically appropriate.",
            "Use intraoperative PTH in the context of multigland disease rather than as a substitute for a complete bilateral anatomic assessment.",
            "Recheck RLN integrity, remaining gland perfusion, and hemostasis bilaterally before strap and skin closure.",
        ]
    if _has(t, "parathyroidectomy", "focused parathyroid", "minimally invasive parathyroid"):
        return [
            "Confirm the localized side and depth before incision; position and expose the central neck through a focused transverse opening that can be extended if localization fails.",
            "Separate the strap muscles and retract the thyroid lobe medially just enough to enter the expected parathyroid plane without stripping the thyroid capsule broadly.",
            "Identify the RLN or a dependable nerve-safe landmark before dividing tissue in the tracheoesophageal groove or near the inferior thyroid artery.",
            "Find the abnormal gland using its expected embryologic location—superior gland posterior to the upper/mid lobe; inferior gland near the lower pole or thyrothymic tract—and distinguish it from fat, thyroid, and lymph node.",
            "Develop the gland circumferentially while preserving the recurrent nerve and controlling the terminal vascular pedicle last, minimizing capsule violation.",
            "Remove the abnormal gland intact and obtain intraoperative PTH after excision using the planned timing protocol; interpret the result against the appropriate baseline.",
            "If PTH fails to fall appropriately, reassess localization, ectopic sites, double adenoma, and multigland disease before converting to broader exploration.",
            "Confirm hemostasis, nerve integrity when monitored, and absence of an expanding central-neck space before layered closure.",
        ]
    if _has(t, "completion thyroid", "reoperative thyroid", "reop-thyroid"):
        return [
            "Enter through the prior low transverse incision and raise only the flaps necessary to obtain safe exposure of the remaining thyroid bed.",
            "Separate the strap muscles through the least-scarred plane and mobilize the residual lobe while preserving the option to identify the RLN away from dense scar.",
            "Control the superior pole close to the thyroid capsule, protecting the external branch of the superior laryngeal nerve.",
            "Identify the RLN at a reliable point—often inferiorly in the tracheoesophageal groove or at its laryngeal entry—and trace it through scar before dividing Berry-region attachments.",
            "Identify and preserve viable parathyroid tissue and its blood supply; autotransplant clearly devascularized parathyroid tissue when appropriate.",
            "Divide terminal thyroid vessels on the capsule and release Berry ligament only under direct knowledge of the RLN course.",
            "Remove the remaining thyroid tissue/specimen, orient as needed, and address indicated central nodes only when part of the oncologic plan.",
            "Reassess nerve signal/function, parathyroid viability, and hemostasis with Valsalva before closure.",
        ]
    if _has(t, "total thyroidectomy"):
        return [
            "Make a low transverse cervical incision, raise superior and inferior subplatysmal flaps, and divide the linea alba between the strap muscles to expose the thyroid.",
            "Choose the first lobe, free the strap muscles from its capsule, mobilize the lateral surface, and divide the middle thyroid vein when present to permit medial rotation.",
            "Develop the superior pole and control individual superior thyroid vessels close to the capsule while keeping the external branch of the superior laryngeal nerve out of the ligature/energy field.",
            "Mobilize the inferior pole and identify the inferior parathyroid/thyrothymic tissue, preserving its vascular supply rather than skeletonizing the gland.",
            "Identify the recurrent laryngeal nerve in a safe segment and trace it toward the cricothyroid joint/laryngeal entry as the thyroid is rotated medially.",
            "Identify the superior parathyroid on the posterior capsule, preserve its pedicle, and divide terminal inferior-thyroid branches directly on the thyroid capsule.",
            "Release Berry ligament and the final tracheal attachments under direct visualization of the RLN, then remove the first lobe/isthmus as planned.",
            "Before committing to the opposite side, reassess RLN function/monitoring if used; if there is unexplained loss of signal, consider staged completion rather than risking bilateral paralysis.",
            "Repeat the complete capsular dissection on the contralateral side—superior pole, parathyroids, RLN, terminal vessels, then Berry ligament—rather than treating it as a shorthand repeat step.",
            "Inspect both beds for hemostasis with Valsalva, confirm parathyroid viability and nerve integrity, then reapproximate straps/platysma and close the skin.",
        ]
    if _has(t, "thyroid lobectomy", "hemithyroid", "thyroidectomy", "thyroid lobectomy"):
        return [
            "Make a low transverse incision, elevate subplatysmal flaps, and open the strap-muscle midline to expose the involved thyroid lobe.",
            "Separate the strap muscles from the capsule, mobilize the lateral lobe, and divide the middle thyroid vein when present to allow medial rotation.",
            "Control the superior pole vessels individually and close to the thyroid capsule while protecting the external branch of the superior laryngeal nerve.",
            "Mobilize the inferior pole while preserving the inferior parathyroid and its vascular pedicle.",
            "Identify the recurrent laryngeal nerve in a safe segment and follow it toward the laryngeal entry point as the lobe is rotated medially.",
            "Identify and preserve the superior parathyroid; divide terminal inferior-thyroid branches on the capsule rather than away from the gland.",
            "Divide Berry ligament and final tracheal attachments under direct RLN visualization, then divide the isthmus and remove/orient the lobe.",
            "Confirm hemostasis with Valsalva and reassess nerve integrity before layered closure.",
        ]
    if _has(t, "central neck dissection", "central-neck"):
        return [
            "Expose the central compartment from hyoid/thyroid cartilage level to the innominate region as indicated, defining the trachea and carotid sheaths bilaterally.",
            "Identify the recurrent laryngeal nerve on the side of dissection before mobilizing nodal tissue from the tracheoesophageal groove.",
            "Preserve viable parathyroid glands and their blood supply; separate nodal tissue from glands rather than sacrificing the vascular pedicle with the packet.",
            "Remove prelaryngeal and pretracheal nodal tissue in continuity with the intended paratracheal compartment, keeping dissection on known anatomic planes.",
            "On the right, remain aware of the recurrent nerve's more oblique course; on the left, follow the nerve within the tracheoesophageal groove and protect the thoracic inlet structures.",
            "Control small inferior thyroid/thymic vessels as the specimen is released inferiorly, avoiding blind energy use near the RLN.",
            "Orient/specimen-label by compartment as required and inspect the tracheoesophageal grooves for residual target nodes without unnecessary nerve skeletonization.",
            "Confirm RLN integrity, parathyroid perfusion, and meticulous central-neck hemostasis before closure.",
        ]

    # ---------- SALIVARY ----------
    if _has(t, "total parotid"):
        return [
            "Use a preauricular/cervical parotid incision, elevate the skin flap in the appropriate plane, and expose the parotid fascia, tragal cartilage, SCM, and posterior digastric landmarks.",
            "Develop the facial-nerve trunk using a reliable combination of tragal pointer, tympanomastoid suture, and posterior digastric landmarks rather than a single landmark alone.",
            "Trace the facial nerve into upper and lower divisions, releasing the superficial lobe from the branches while controlling retromandibular/external carotid tributaries as encountered.",
            "After the superficial lobe is mobilized, dissect the deep-lobe component from between/around the facial-nerve branches with the nerve continuously visualized and protected.",
            "Control the parotid duct and deep vascular attachments as required by tumor location, maintaining oncologic margins without unnecessary branch sacrifice.",
            "If a facial-nerve branch is involved by tumor, define proximal/distal control and the reconstructive plan before intentional sacrifice.",
            "Remove and orient the specimen, then stimulate/inspect the main trunk and divisions when monitoring is used.",
            "Obtain hemostasis, consider contour reconstruction, place a drain when indicated, and close without compressing the facial nerve.",
        ]
    if _has(t, "superficial parotid", "parotidectomy"):
        return [
            "Design the preauricular/cervical incision and elevate a thick skin flap superficial to the parotid fascia while protecting the greater auricular nerve when oncologically appropriate.",
            "Expose the tragal cartilage, mastoid tip/tympanomastoid suture, SCM, and posterior belly of digastric to triangulate the facial-nerve trunk.",
            "Identify the facial-nerve trunk and confirm it before dividing parotid tissue in the expected nerve plane.",
            "Trace upper and lower divisions/peripheral branches in the direction required by the lesion, lifting the superficial lobe away from the nerve rather than pulling the nerve out of the gland.",
            "Control the retromandibular vein/external carotid branches and Stensen duct only as required by the resection.",
            "Remove the superficial-lobe specimen with an intact tumor capsule and appropriate margin, avoiding tumor spillage.",
            "Reinspect and stimulate the facial-nerve trunk/branches when used, then secure meticulous hemostasis.",
            "Place drain/contour reconstruction selectively and close the flap without excessive tension or pressure on the nerve.",
        ]
    if _has(t, "submandibular gland", "submandibular excision"):
        return [
            "Place the cervical incision below the mandibular border and elevate the flap in a plane that protects the marginal mandibular branch.",
            "Identify the submandibular gland capsule and develop the inferior/lateral surface, controlling facial vein/artery branches as needed.",
            "Retract the mylohyoid anteriorly to expose the deep lobe and identify the lingual nerve with the submandibular ganglion/duct relationship.",
            "Separate the gland from the lingual nerve, dividing the ganglion branches close to the gland while preserving the nerve.",
            "Identify Wharton duct and the hypoglossal nerve deep/inferior to it before dividing the duct.",
            "Control the glandular facial-artery pedicle and release the remaining attachments without thermal injury to lingual or hypoglossal nerves.",
            "Remove the gland/specimen and inspect the wound for nerve integrity and bleeding.",
            "Irrigate, obtain hemostasis, place a drain selectively, and close in layers.",
        ]
    if _has(t, "sialendosc"):
        return [
            "Identify the papilla and gently dilate the ductal orifice in graduated fashion rather than forcing the endoscope through a tight opening.",
            "Enter the duct with continuous irrigation and advance under direct visualization, keeping the lumen centered to avoid false passage/perforation.",
            "Survey the main duct and accessible branch points while noting stenosis, mucus plugs, stones, and duct-wall injury.",
            "For a mobile stone, pass the basket beyond it, capture it under vision, and withdraw without avulsing the duct.",
            "For an impacted stone or stenosis, use the planned dilation, laser/pneumatic fragmentation, or combined transoral approach while protecting lingual nerve anatomy when working in the floor of mouth.",
            "Reinspect the treated segment for residual stone fragments and confirm free irrigation/salivary flow.",
            "Place a duct stent only when indicated by stenosis, ductotomy, or mucosal injury and secure it without obstructing the papilla.",
            "Finish with oral hemostasis and document duct patency and any combined incision.",
        ]

    # ---------- RHINOLOGY / SKULL BASE ----------
    if _has(t, "maxillary antrostomy"):
        return [
            "Decongest the nasal cavity and identify the middle turbinate, uncinate process, ethmoid bulla, and expected maxillary natural ostium region before cutting.",
            "Incise and remove the uncinate in a controlled anterior-to-posterior/superior-to-inferior fashion while staying aware of the lacrimal system anteriorly and orbit laterally.",
            "Identify the natural maxillary ostium with a probe or angled endoscope; do not create a separate accessory opening and assume it is the ostium.",
            "Enlarge the natural ostium posteriorly and inferiorly as indicated, joining any accessory ostium to the natural ostium to prevent mucus recirculation.",
            "Keep the anterior limit behind the nasolacrimal duct and the superior dissection oriented to the orbital floor/lamina.",
            "Use angled visualization to inspect the sinus and remove only disease that requires direct treatment rather than stripping healthy sinus mucosa.",
            "Confirm that the antrostomy is circumferentially patent and clearly incorporates the natural ostium.",
            "Obtain hemostasis while preserving middle-meatal landmarks and minimizing opposing raw mucosal surfaces.",
        ]
    if _has(t, "ethmoidectomy", "anterior ethmoid", "posterior ethmoid"):
        return [
            "After uncinectomy/maxillary identification as appropriate, identify the ethmoid bulla, lamina papyracea, middle turbinate, and skull-base orientation.",
            "Open the ethmoid bulla in its safe medial/inferior portion and remove partitions while keeping the orbit continuously defined laterally.",
            "Progress through anterior ethmoid cells toward the basal lamella, maintaining a known superior limit rather than blindly following disease toward the skull base.",
            "Enter the posterior ethmoid through the basal lamella at a controlled inferomedial location when posterior dissection is indicated.",
            "Identify posterior ethmoid landmarks and the sphenoid face; recognize that the skull base slopes and may be asymmetric.",
            "Skeletonize rather than violate the lamina/skull base, and treat the anterior ethmoid artery region only with deliberate awareness of its orbital and skull-base attachments.",
            "Remove residual obstructing partitions while preserving middle-turbinate stability and mucosa where possible.",
            "Perform a final orbit, skull-base, and hemostasis inspection before leaving the ethmoid cavity.",
        ]
    if _has(t, "sphenoidotomy", "sphenoid sinus"):
        return [
            "Identify the superior turbinate and sphenoethmoidal recess, then locate the natural sphenoid ostium medial to the superior turbinate rather than drilling blindly into the face.",
            "Confirm the ostium with direct visualization and enter it with an instrument directed safely away from the orbit and skull base.",
            "Enlarge the opening inferiorly and medially first, preserving orientation to the posterior septum and choana.",
            "Remove the inferior portion of the superior turbinate only as required for exposure and preserve olfactory mucosa superiorly.",
            "Inspect the sphenoid cavity and identify carotid/optic prominences, sellar/clival landmarks, and any Onodi-cell anatomy before lateral or superior instrumentation.",
            "Enlarge the sphenoidotomy to the size required for drainage or skull-base access without unnecessary mucosal stripping.",
            "Treat intrasinus disease under direct visualization, keeping powered instrumentation away from the optic nerve/carotid unless their course is unequivocally defined.",
            "Confirm a widely patent ostium and hemostasis before completion.",
        ]
    if _has(t, "draf iii", "draf 3", "modified lothrop"):
        return [
            "Complete bilateral frontal-recess exposure and identify the orbit, skull base/first olfactory fiber region, frontal beak, and frontal sinus drainage pathways on both sides.",
            "Resect the superior nasal septum below the frontal recess to create a common working corridor while preserving adequate structural support inferiorly.",
            "Remove the frontal sinus floor from one orbit to the other, staying anterior to the skull base and posterior to the frontal beak/nasal bones as the common cavity is developed.",
            "Drill the frontal beak and intersinus septum under constant endoscopic orientation, using the frontal sinus posterior table/skull base as the posterior safety boundary.",
            "Connect the right and left frontal outflow tracts into a single common neo-ostium, removing obstructing partitions rather than circumferentially stripping mucosa.",
            "Smooth exposed bone and preserve/transplant mucosa where feasible to reduce restenosis.",
            "Inspect the entire common frontal opening with angled scopes and verify bilateral sinus access without residual obstructing frontal cells.",
            "Secure hemostasis and place stent/packing only when specifically indicated, with a postoperative debridement/patency plan.",
        ]
    if _has(t, "draf iib", "draf 2b", "draf ii", "frontal sinusotomy", "frontal recess"):
        return [
            "Expose the frontal recess after completing the necessary anterior ethmoid dissection and identify the agger nasi/frontal cells, orbit, middle turbinate, and skull base.",
            "Use multiplanar CT orientation to determine whether drainage is medial/lateral to individual frontal cells before removing partitions.",
            "Open cells from below upward, keeping the orbit as the lateral boundary and the skull base/posterior table as the posterior boundary.",
            "Identify the true frontal sinus lumen and enlarge the drainage pathway without circumferential mucosal stripping.",
            "For a Draf IIb-type opening, extend medially to the nasal septum and laterally toward the lamina while preserving the posterior skull-base boundary.",
            "Remove residual frontal-beak or cell partitions only to the extent needed for a stable, widely visible outflow tract.",
            "Inspect with angled endoscopes to confirm the entire intended frontal opening and absence of residual obstructing cells.",
            "Obtain hemostasis and preserve mucosa/avoid opposing raw surfaces to limit cicatricial restenosis.",
        ]
    if _has(t, "csf leak", "nasoseptal flap", "skull base repair"):
        return [
            "Map the defect on preoperative imaging and endoscopy, then obtain complete endoscopic exposure while defining the orbit, skull base, sphenoid, carotid/optic structures, and planned vascularized-flap pedicle.",
            "Harvest the nasoseptal or alternative flap before sacrificing its pedicle territory when a vascularized reconstruction is planned, preserving the posterior septal vascular supply.",
            "Localize the actual CSF defect and remove only enough mucosa/bone around it to create a stable reconstruction bed.",
            "Reduce herniated tissue only as required and obtain controlled hemostasis without injuring intracranial or neurovascular structures.",
            "Place the chosen inlay/onlay grafts with broad contact to healthy margins, tailoring multilayer reconstruction to defect size, flow, and location.",
            "Rotate the vascularized flap without pedicle twist or compression and cover the entire defect with viable tissue.",
            "Support the reconstruction with the planned buttress/packing while avoiding excessive pressure on the flap pedicle or orbit.",
            "Perform a final leak/reconstruction inspection and document postoperative CSF precautions and lumbar-drain strategy when used.",
        ]
    if _has(t, "spa ligation", "sphenopalatine", "epistaxis ligation"):
        return [
            "Create middle-meatal access and elevate a mucoperiosteal flap along the posterior lateral nasal wall toward the crista ethmoidalis.",
            "Identify the sphenopalatine foramen by direct anatomy rather than following bleeding blindly posteriorly.",
            "Expose the arterial branches as they emerge from the foramen, recognizing that multiple branches/foramina may be present.",
            "Clip or cauterize each identified branch under direct visualization, protecting surrounding mucosa and avoiding uncontrolled deep thermal spread.",
            "Inspect superior and inferior to the main foramen for accessory branches if bleeding control is incomplete.",
            "Return the mucosal flap to cover exposed bone and treated vessels.",
            "Reinspect the nasal cavity and nasopharynx for persistent bleeding from a second source.",
            "Pack selectively and document blood-loss/resuscitation needs and recurrence plan.",
        ]
    if _has(t, "orbital abscess", "subperiosteal orbital"):
        return [
            "Review CT to define medial versus superior/inferior collection and associated sinus disease, then decongest the nose and establish endoscopic orientation to the orbit and skull base.",
            "Complete the necessary ethmoid/maxillary/frontal drainage to expose the diseased lamina papyracea without destabilizing uninvolved anatomy.",
            "Skeletonize the lamina over the abscess and remove a controlled segment of bone while preserving periorbita until the intended drainage site is defined.",
            "Incise/elevate the periorbita at the collection, drain purulence, and obtain cultures before irrigation when feasible.",
            "Avoid unnecessary orbital-fat manipulation and protect the medial rectus while ensuring the subperiosteal pocket is fully decompressed.",
            "Reopen all causative sinus pathways and remove obstructing disease needed for durable drainage.",
            "Confirm orbital decompression/hemostasis and avoid tight packing against the orbit.",
            "Document immediate postoperative vision, pupils, color vision, and extraocular movement with urgent escalation for deterioration.",
        ]
    if _has(t, "septoplasty"):
        return [
            "Infiltrate the septum, make the planned hemitransfixion/Killian-type incision, and elevate a subperichondrial flap with the cartilage continuously visible.",
            "Cross to the opposite side only at a controlled point and preserve an intact contralateral mucoperichondrial flap whenever possible.",
            "Define the deviated cartilage/bone and the maxillary crest while maintaining an adequate dorsal and caudal L-strut.",
            "Resect or reshape only the obstructing septal components; avoid opposing mucosal tears and uncontrolled high posterior dissection.",
            "Address the bony-cartilaginous junction and spurs under direct visualization, protecting the skull base superiorly.",
            "Reposition remaining cartilage so the caudal septum is stable in the midline and the airway is improved bilaterally.",
            "Close mucosal incisions and quilting sutures to eliminate dead space and reduce hematoma risk.",
            "Place splints only when indicated and confirm bilateral airway patency and hemostasis.",
        ]
    if _has(t, "turbinate", "inferior turbinate reduction"):
        return [
            "Decongest and inspect the full inferior turbinate, confirming that septal deviation or valve collapse is not the sole source of obstruction.",
            "Infiltrate the turbinate and create the planned submucosal entry while preserving the surface mucosa.",
            "Develop a submucosal tunnel along the turbinate bone, keeping the instrument within the turbinate rather than entering the lateral wall.",
            "Reduce submucosal soft tissue and/or turbinate bone in a controlled fashion while preserving enough tissue for humidification and mucociliary function.",
            "Outfracture the turbinate laterally when part of the plan, avoiding excessive force at the turbinate attachment.",
            "Treat focal posterior bleeding under direct visualization rather than broadly cauterizing the mucosal surface.",
            "Inspect the entire turbinate for mucosal tears, exposed bone, and symmetry of reduction.",
            "Confirm hemostasis and a patent nasal airway without over-resection.",
        ]

    # ---------- OTOLOGY / NEUROTOLOGY ----------
    if _has(t, "stapedotomy", "stapedectomy"):
        return [
            "Elevate the tympanomeatal flap and enter the middle ear while preserving the annulus and chorda tympani as anatomy allows.",
            "Curette/sculpt the posterosuperior canal wall only enough to visualize the incus long process, stapes superstructure, pyramidal eminence, and facial nerve.",
            "Confirm ossicular mobility and stapes fixation before committing to footplate fenestration.",
            "Measure the incus-to-footplate distance and select the prosthesis length before disrupting the stapes superstructure.",
            "Divide the stapedial tendon and posterior crus/superstructure in a controlled sequence, minimizing manipulation of the footplate.",
            "Create the footplate fenestra at the planned site with laser/drill/perforator while avoiding suction or instrument plunge into the vestibule.",
            "Place and secure the prosthesis from incus to fenestra, confirm free piston/ossicular motion, and seal the fenestra as indicated.",
            "Return the tympanomeatal flap, ensure hemostasis and atraumatic canal packing, and avoid pressure that displaces the prosthesis.",
        ]
    if _has(t, "cochlear implant", "cochlear-implant"):
        return [
            "Plan the postauricular incision/receiver position and expose mastoid cortex while protecting soft-tissue thickness over the future receiver-stimulator.",
            "Perform cortical mastoidectomy and identify tegmen, sigmoid sinus, lateral semicircular canal, incus, and facial recess landmarks.",
            "Open the facial recess between facial nerve and chorda tympani to obtain a direct line of sight to the round-window niche.",
            "Prepare the receiver-stimulator well/pocket and secure the device so the electrode reaches the cochlea without tension.",
            "Expose the round-window membrane or create the planned cochleostomy while avoiding unnecessary trauma to the osseous spiral lamina/inner ear.",
            "Insert the electrode slowly to the intended depth, managing resistance rather than forcing the array.",
            "Seal the cochlear entry, coil excess lead safely in the mastoid cavity, and complete impedance/neural-response testing when used.",
            "Reinspect facial-nerve/chorda integrity and hemostasis, then close the soft tissue in layers without pressure over the implant.",
        ]
    if _has(t, "ossiculoplasty"):
        return [
            "Elevate the tympanomeatal flap and expose the ossicular chain while preserving viable tympanic membrane and middle-ear mucosa.",
            "Assess malleus, incus, stapes superstructure/footplate mobility, and disease before selecting partial versus total ossicular reconstruction.",
            "Remove only nonviable or disease-involved ossicular segments and clear the prosthesis path of adhesions/cholesteatoma.",
            "Measure the required reconstruction height with the tympanic membrane returned toward its physiologic position rather than estimating an overlong prosthesis.",
            "Place cartilage protection when indicated and seat the prosthesis securely on the stapes head or footplate with stable contact to the tympanic membrane/malleus.",
            "Check that the reconstruction moves freely and is not impinging on the promontory, facial canal, or canal wall.",
            "Return the tympanomeatal flap and confirm the graft/prosthesis relationship before packing.",
            "Pack the canal gently enough to support the repair without displacing the reconstruction.",
        ]
    if _has(t, "cholesteatoma", "tympanomastoid", "mastoidectomy"):
        return [
            "Use the planned canal/postauricular approach, elevate the tympanomeatal flap as needed, and define disease extent in the middle ear before drilling toward hidden spaces.",
            "Perform cortical mastoidectomy with constant orientation to the tegmen, sigmoid sinus, ear canal, lateral semicircular canal, and mastoid segment of the facial nerve.",
            "Open the antrum and epitympanum, identify the short process/body of incus, and connect mastoid and middle-ear disease pathways under direct vision.",
            "Remove cholesteatoma matrix systematically from epitympanum, facial recess, sinus tympani, hypotympanum, and mastoid while preserving labyrinth, facial nerve, and dura.",
            "Assess ossicular erosion and remove/reconstruct only as required for complete disease clearance and hearing goals.",
            "If canal-wall-down surgery is required, lower the facial ridge and exteriorize disease spaces while creating a smooth, self-cleaning cavity; if canal-wall-up, preserve/reconstruct the posterior canal wall appropriately.",
            "Reinspect all hidden recesses with microscope/angled endoscope, ensuring no residual matrix remains on critical structures.",
            "Complete tympanic membrane/ossicular reconstruction as planned, obliterate/reconstruct selectively, and pack/close without obstructing drainage.",
        ]
    if _has(t, "tympanoplasty"):
        return [
            "Freshen the perforation edge and choose transcanal/endaural/postauricular exposure that gives complete visualization of the perforation and annulus.",
            "Elevate the tympanomeatal flap in the correct canal-wall plane and lift the annulus to enter the middle ear without tearing remaining drum.",
            "Inspect the middle ear, ossicular chain, chorda tympani, and disease; address adhesions or ossicular problems only as indicated.",
            "Prepare the graft and middle-ear support so the graft will contact a vascularized drum remnant without blocking the Eustachian tube or round window.",
            "Place the graft using the planned underlay/overlay/cartilage technique, ensuring secure anterior and inferior support where failures commonly occur.",
            "Return the tympanomeatal flap over the graft and verify that the graft remains flat, medial/lateral as intended, and free of folds.",
            "Support the reconstruction with minimal middle-ear/canal packing needed to prevent migration.",
            "Confirm canal hemostasis and close the approach without creating canal stenosis or pressure injury.",
        ]
    if _has(t, "canalplasty", "exostosis"):
        return [
            "Establish circumferential canal skin exposure and elevate skin flaps so the bony lesion can be removed without sacrificing healthy canal epithelium.",
            "Identify the tympanic membrane/annulus medially and the temporomandibular joint/anterior canal boundary before drilling.",
            "Reduce obstructing bone with controlled drilling/chiseling directed away from the tympanic membrane and facial nerve, keeping the canal lumen centered.",
            "Work sequentially around the canal rather than creating a deep blind trough beside the annulus.",
            "Smooth the bony canal and ensure adequate diameter from meatus to annulus while avoiding over-thinning the anterior wall.",
            "Replace preserved canal skin to cover exposed bone and minimize circumferential raw surfaces.",
            "Inspect the tympanic membrane for injury and confirm hemostasis.",
            "Pack the canal to support skin flaps without excessive pressure and close any postauricular incision.",
        ]
    if _has(t, "tegmen", "encephalocele"):
        return [
            "Define the tegmen defect and CSF/encephalocele extent on imaging, then obtain transmastoid and/or middle-fossa exposure appropriate to defect size/location.",
            "Perform mastoidectomy with the tegmen, sigmoid sinus, labyrinth, ossicles, and facial nerve continuously defined.",
            "Skeletonize the defect margins and separate herniated dura/encephalocele from epithelium or middle-ear disease without violating uninvolved dura.",
            "Reduce or excise nonfunctional herniated tissue as planned and prepare healthy bony/dural margins for reconstruction.",
            "Place multilayer grafts/bone/cartilage with broad overlap while preserving ossicular and Eustachian-tube function when possible.",
            "If using middle-fossa access, protect temporal-lobe dura and avoid traction injury to the greater superficial petrosal nerve/facial nerve region.",
            "Confirm a stable watertight reconstruction and eliminate any epithelial entrapment under the repair.",
            "Complete mastoid/middle-ear reconstruction, hemostasis, and layered closure with postoperative CSF precautions.",
        ]
    if _has(t, "vestibular schwannoma", "acoustic neuroma"):
        return [
            "Position and expose according to the chosen retrosigmoid, translabyrinthine, or middle-fossa corridor, confirming hearing-preservation intent before irreversible labyrinthine work.",
            "Obtain the bony corridor with constant orientation to sigmoid/transverse sinus, labyrinth, IAC, facial nerve, and lower cranial nerves as relevant to approach.",
            "Open dura and release CSF to achieve cerebellar/temporal-lobe relaxation rather than relying on fixed retraction.",
            "Identify the tumor–nerve interface and internally debulk large tumor before circumferential capsule dissection.",
            "Dissect the capsule from brainstem, cochlear nerve, and facial nerve in small segments, using stimulation and preserving the facial-nerve vascular supply.",
            "Open the IAC to the required extent and remove the intracanalicular component while protecting labyrinth and fundal nerves when hearing preservation is intended.",
            "Inspect for residual tumor in the fundus/brainstem interface and decide deliberately if a tiny adherent remnant is safer than nerve injury.",
            "Achieve watertight dural/air-cell closure, obliterate opened petrous air cells, and complete approach-specific reconstruction.",
        ]

    # ---------- LARYNGOLOGY / AIRWAY ----------
    if _has(t, "microflap", "phonomicrosurgery"):
        return [
            "Obtain atraumatic suspension-laryngoscopy exposure with the lesion centered and document the contralateral fold before manipulation.",
            "Use magnification to define lesion depth and the relationship to epithelium, superficial lamina propria, vocal ligament, and anterior commissure.",
            "Create the epithelial incision just lateral to the lesion at a site that preserves the vibratory edge and maximizes usable epithelium.",
            "Elevate the microflap within the superficial lamina propria, separating epithelium from the lesion without entering vocal ligament.",
            "Dissect/remove the lesion while preserving normal superficial lamina propria and avoiding unnecessary tissue on the medial edge.",
            "Control pinpoint bleeding with the least traumatic method possible; avoid broad cautery that stiffens the fold.",
            "Redrape the microflap and trim only clearly redundant/nonviable epithelium so the edge lies smooth without tension.",
            "Reinspect both folds, document the final contour, and end suspension before pressure injury to tongue/teeth becomes significant.",
        ]
    if _has(t, "cordotomy", "arytenoidectomy"):
        return [
            "Obtain full posterior-glottic exposure and confirm which side is planned for airway enlargement based on preoperative motion, voice, and aspiration considerations.",
            "Identify the vocal process, membranous vocal fold, ventricle, and posterior commissure before laser or powered instrumentation.",
            "For posterior cordotomy, create the transverse opening just anterior to the vocal process through the vocal fold toward the thyroid cartilage/perichondrium to establish a lateral airway channel.",
            "For arytenoid reduction when planned, expose and remove only the intended arytenoid component while protecting posterior mucosa and avoiding bilateral scar surfaces.",
            "Control bleeding and char with minimal collateral thermal injury, keeping the opposite fold untouched.",
            "Assess the resulting posterior airway under direct visualization and remove only additional tissue necessary for an adequate lumen.",
            "Reinspect the subglottis and posterior commissure for loose tissue or flap that could obstruct after extubation.",
            "Plan postoperative airway observation and counsel that voice quality may trade off against airway gain.",
        ]
    if _has(t, "medialization", "thyroplasty"):
        return [
            "Expose the thyroid cartilage through a horizontal neck incision and preserve perichondrium/strap anatomy needed for stable framework work.",
            "Mark the true vocal-fold level using external laryngeal landmarks and create the thyroplasty window without violating the inner perichondrium.",
            "Elevate the inner perichondrium carefully and test medialization with the patient phonating when awake technique is used.",
            "Shape/position the implant to medialize the membranous fold while avoiding excessive posterior pressure or airway narrowing.",
            "Use voice quality and/or flexible laryngoscopy to adjust implant depth, anterior-posterior position, and height.",
            "Secure the implant so it cannot migrate into the airway or soft tissues.",
            "Reinspect the larynx for airway caliber, vocal-fold position, edema, and mucosal integrity.",
            "Obtain neck hemostasis and close without a compressive hematoma around the framework.",
        ]
    if _has(t, "injection laryngoplasty", "vocal fold injection"):
        return [
            "Confirm the target fold and glottic insufficiency pattern endoscopically before injection.",
            "Choose the approach and needle trajectory that places material lateral to the thyroarytenoid rather than superficially in the vibratory epithelium.",
            "Enter the posterolateral or mid-membranous injection site under continuous endoscopic visualization.",
            "Inject in small increments while watching medialization and avoiding intravascular, subepithelial, or trans-airway extrusion.",
            "Distribute material as needed to correct the specific gap rather than simply maximizing fold bulk.",
            "Stop at the planned degree of correction, accounting for expected early overcorrection with some injectates.",
            "Reassess phonation, airway, and swallowing as appropriate to anesthetic setting.",
            "Observe for edema, bleeding, or airway compromise before discharge.",
        ]
    if _has(t, "laryngeal botox", "botox", "botulinum"):
        return [
            "Confirm the dystonia/tremor phenotype and target muscle before injection; review prior dose/response and breathiness or dysphagia history.",
            "Position for EMG-guided or endoscopic injection and identify the cricothyroid membrane/cartilage landmarks.",
            "Advance the needle into the intended thyroarytenoid/lateral cricoarytenoid or alternative target while monitoring EMG activity when used.",
            "Confirm target activation with phonation/sniff task rather than injecting based on surface anatomy alone.",
            "Deliver the planned low-volume dose and avoid traversing the airway more than necessary.",
            "Repeat contralaterally only if the treatment plan is bilateral and symmetric.",
            "Observe briefly for bleeding, vasovagal symptoms, or airway reaction.",
            "Document exact muscle, side, dose, dilution, and prior-response context for future titration.",
        ]
    if _has(t, "zenker"):
        return [
            "Expose the diverticular septum with the chosen rigid diverticuloscope or flexible platform and clearly identify the esophageal lumen versus pouch.",
            "Center the common wall containing the cricopharyngeus and ensure adequate visualization to the distal end of the septum before dividing it.",
            "Divide the septum/cricopharyngeal muscle with stapler, laser, or endoscopic knife in a controlled distal progression.",
            "Maintain the cut in the midline of the septum to avoid lateral perforation into the neck.",
            "Extend the myotomy adequately to relieve the functional obstruction while stopping before an uncontrolled mediastinal entry.",
            "Inspect the divided edges for bleeding and for a residual muscular bridge that would cause persistent symptoms.",
            "Confirm a common channel between pouch and esophagus without obvious perforation.",
            "Set postoperative diet and perforation-monitoring strategy based on technique and intraoperative findings.",
        ]
    if _has(t, "cricopharyngeal myotomy", "cricophary"):
        return [
            "Expose the cervical esophagus through the planned side while identifying and protecting the recurrent laryngeal nerve.",
            "Rotate the pharyngoesophageal segment to expose the posterior/lateral cricopharyngeus and proximal cervical esophageal muscle.",
            "Identify the muscle fibers of the cricopharyngeus and define the intended myotomy length before cutting.",
            "Divide muscle fibers down to intact mucosa over the full planned segment, extending onto adjacent inferior constrictor/esophageal muscle as required.",
            "Inspect the mucosa for inadvertent perforation and repair immediately if present.",
            "Ensure the myotomy is complete without a residual constricting muscle bridge.",
            "Obtain hemostasis while avoiding thermal injury to the exposed mucosa or recurrent nerve.",
            "Close the neck and institute the planned postoperative swallow/diet pathway.",
        ]
    if _has(t, "tracheoesophageal puncture", "tep"):
        return [
            "Visualize the posterior tracheal wall and anterior esophageal wall with rigid/flexible esophagoscopy so the puncture site is clearly transilluminated/palpated.",
            "Choose a puncture site centered in the posterior tracheal wall with adequate distance from the stoma edge and party wall anatomy.",
            "Pass the puncture needle/catheter into the esophageal lumen under direct visualization rather than blind force.",
            "Guide the wire/catheter through the mouth or use the planned retrograde/anterograde system.",
            "Dilate the tract only to the size required for the prosthesis.",
            "Seat the voice prosthesis with both flanges fully deployed on the tracheal and esophageal sides.",
            "Confirm prosthesis rotation/patency and absence of leakage around or through the device.",
            "Reinspect for bleeding or false passage and document prosthesis type/size.",
        ]
    if _has(t, "direct laryngoscopy bronchoscopy", "dlb", "airway endoscopy"):
        return [
            "Coordinate spontaneous versus controlled ventilation and perform atraumatic direct laryngoscopy with the larynx fully exposed before sizing or instrumentation.",
            "Document supraglottis, glottis, posterior commissure, subglottis, and trachea systematically, including dynamic findings when relevant.",
            "Pass the telescope through the cords under direct vision and examine to the carina/bronchi when bronchoscopy is part of the case.",
            "Size the airway with calibrated endotracheal tubes only when clinically needed, using a standardized leak-pressure method rather than forcing a tight tube.",
            "Measure stenosis location, length, diameter, and relationship to the vocal folds/cricoid/tracheostomy.",
            "Perform any biopsy, balloon dilation, scar division, or granulation removal only after the diagnostic anatomy is documented.",
            "Reinspect the airway after intervention for bleeding, mucosal injury, edema, and lumen gain.",
            "Define extubation versus postoperative airway support before leaving the OR.",
        ]
    if _has(t, "airway dilation", "balloon dilation", "subglottic dilation"):
        return [
            "Obtain suspension/direct-laryngoscopic exposure and document stenosis level, length, grade, and mature versus inflammatory character before treatment.",
            "Protect the posterior glottis and identify any scar bands that should be radially divided before dilation.",
            "Place the balloon centered across the stenosis under direct vision, avoiding distal migration and vocal-fold injury.",
            "Inflate to the planned diameter/pressure for a controlled interval while maintaining the agreed ventilation/apnea strategy.",
            "Deflate completely and reassess mucosa, bleeding, and lumen before deciding on additional dilation.",
            "Repeat only as needed, avoiding progressive mucosal tearing or cartilage injury from oversized dilation.",
            "Apply adjunctive steroid/mitomycin only when part of the specific protocol and with careful dose/contact control.",
            "Reinspect the entire airway and determine postoperative steroid, observation, and rescue-airway plan.",
        ]
    if _has(t, "laryngotracheal reconstruction", "peds-ltr", " ltr"):
        return [
            "Expose the larynx/trachea through the existing or planned cervical airway incision, preserving strap and recurrent-nerve anatomy and defining the cricoid/tracheal framework.",
            "Open the airway in the midline and directly inspect the stenotic segment to confirm the required anterior, posterior, or combined expansion.",
            "For posterior expansion, split the posterior cricoid plate in the midline without extending into the esophageal mucosa; for anterior expansion, divide the anterior cricoid/tracheal scar as planned.",
            "Harvest and shape rib cartilage with perichondrial orientation appropriate to the graft surface and size it to expand without excessive tension.",
            "Inset the posterior and/or anterior cartilage graft securely into the split framework, ensuring it is stable and not protruding dangerously into the lumen.",
            "Place the stent or appropriately sized ETT as planned to support the reconstruction while avoiding pressure injury.",
            "Close the airway/framework and soft tissues around the reconstructed lumen, maintaining graft position and a tension-free tracheal/skin relationship.",
            "Confirm tube/stent position endoscopically and document the postoperative airway, sedation, reflux, and extubation/stent-removal plan.",
        ]
    if _has(t, "cricotracheal resection", " ctr"):
        return [
            "Expose the cricoid and proximal trachea widely enough to define the entire stenotic segment and permit a tension-free anastomosis while protecting both recurrent laryngeal nerves.",
            "Mobilize the cervical trachea circumferentially only to the degree necessary, preserving lateral blood supply and avoiding unnecessary nerve dissection.",
            "Transect the trachea below the stenosis and establish cross-field ventilation as needed.",
            "Resect the stenotic trachea and diseased anterior/lateral cricoid while preserving the posterior cricoid plate and recurrent-nerve entry regions.",
            "Prepare healthy proximal and distal mucosal/cartilaginous edges and perform posterior then lateral/anterior anastomotic suturing with accurate mucosal apposition.",
            "Release additional tracheal/laryngeal attachments only if needed to remove tension rather than accepting a tight anastomosis.",
            "Tie/complete the anastomosis with the neck flexed, then test for air leak and inspect the lumen endoscopically.",
            "Maintain neck-flexion precautions and establish the postoperative airway plan with explicit concern for dehiscence and bilateral RLN function.",
        ]
    if _has(t, "tracheal resection"):
        return [
            "Expose the cervical trachea and map the stenotic segment relative to the cricoid, recurrent laryngeal nerves, thyroid, and innominate region.",
            "Mobilize only enough trachea to achieve resection and a low-tension anastomosis, preserving segmental lateral blood supply.",
            "Transect below the stenosis and transition to cross-field ventilation when required.",
            "Resect the diseased rings to healthy mucosal/cartilage edges, avoiding excessive circumferential devascularization.",
            "Place posterior anastomotic sutures first with precise mucosal apposition, then complete lateral and anterior sutures.",
            "Use release maneuvers selectively if tension remains rather than over-resecting or tightening the suture line.",
            "Test the anastomosis under saline/positive pressure and inspect the lumen endoscopically.",
            "Close with the neck flexed and institute explicit anti-extension/anastomotic precautions postoperatively.",
        ]
    if _has(t, "tracheostomy"):
        return [
            "Position with controlled neck extension, mark the cricoid/sternal notch, and make a horizontal or vertical cervical incision over the upper trachea.",
            "Divide subcutaneous tissue/platysma and separate the strap muscles in the midline, keeping dissection centered on the trachea.",
            "Retract or divide the thyroid isthmus as needed to expose approximately the second through fourth tracheal rings, controlling thyroid vessels before airway entry.",
            "Communicate with anesthesia, reduce inspired oxygen when cautery is no longer needed, and confirm the intended tracheal level before opening the airway.",
            "Create the tracheal opening/flap without injuring the posterior wall and suction blood/secretions under direct vision.",
            "Insert the tracheostomy tube with the obturator, remove the obturator promptly, and connect ventilation.",
            "Confirm end-tidal CO2, chest rise, tube depth, and absence of a false passage; bronchoscopy may confirm position when uncertainty exists.",
            "Secure the flange with sutures/ties, ensure hemostasis, and document tube type/size and first-change plan.",
        ]

    # ---------- PEDIATRIC ----------
    if _has(t, "tonsillectomy and adenoidectomy", "adenotonsillectomy", "t&a"):
        return [
            "Place the mouth gag with tongue and teeth protected, suspend only enough for exposure, and inspect the palate for submucous cleft before adenoid work.",
            "Expose the first tonsil, grasp it medially, enter the peritonsillar plane at the superior pole, and dissect along the capsule toward the lower pole while preserving pharyngeal muscle.",
            "Control tonsillar-bed bleeding with targeted technique rather than broad deep thermal injury, paying particular attention to the lower pole.",
            "Repeat complete capsular or planned intracapsular dissection on the opposite tonsil with the same attention to the tonsillar capsule and constrictor plane.",
            "Retract the palate and visualize the adenoid pad/choanae; identify Eustachian-tube orifices and posterior choanal margins before removal.",
            "Remove obstructing adenoid tissue while leaving a safe cuff near Passavant/velopharyngeal structures when clinically indicated and avoiding injury to the torus tubarius.",
            "Irrigate/suction, release suspension briefly, then re-examine both tonsillar fossae and nasopharynx for bleeding under physiologic blood pressure.",
            "Remove instruments after confirming no loose tooth, lip/tongue injury, retained packing, or active hemorrhage.",
        ]
    if _has(t, "tonsillectomy"):
        return [
            "Insert and suspend the mouth gag with tongue/teeth protected, confirming full visualization of both tonsils and the posterior pharynx.",
            "Grasp the first tonsil medially and make the superior-pole mucosal incision to enter the plane between capsule and superior constrictor.",
            "Follow the tonsillar capsule inferiorly with traction-countertraction, keeping dissection on the capsule and out of pharyngeal muscle.",
            "Release the lower pole under direct vision and control feeding vessels without deep lateral thermal injury.",
            "Inspect the entire fossa and obtain targeted hemostasis, then repeat the complete dissection on the opposite side.",
            "Irrigate/suction and release suspension briefly so occult bleeding appears at a more physiologic pressure.",
            "Re-suspend and inspect superior pole, mid-fossa, and lower pole bilaterally; control any persistent bleeding point directly.",
            "Remove the gag after confirming no dental/oral injury, retained sponge, or active hemorrhage.",
        ]
    if _has(t, "adenoidectomy"):
        return [
            "Insert the mouth gag, palpate/inspect the palate for submucous cleft risk, and retract the soft palate atraumatically.",
            "Visualize the adenoid pad, choanae, vomer, and both Eustachian-tube orifices with mirror or endoscope before removal.",
            "Remove the central obstructing adenoid tissue from superior to inferior using the planned curette/microdebrider/suction cautery technique.",
            "Preserve tissue around the torus tubarius and avoid deep lateral dissection that could scar the Eustachian tube.",
            "Avoid an excessively aggressive inferior resection when velopharyngeal competence is at risk.",
            "Inspect the nasopharynx endoscopically/mirror for residual choanal obstruction and focal bleeding.",
            "Control bleeding with targeted cautery/packing and then remove all packing.",
            "Recheck the oral cavity/nasopharynx and release suspension before emergence.",
        ]
    if _has(t, "thyroglossal"):
        return [
            "Make the transverse incision over the cyst, elevate subplatysmal flaps, and identify the cyst/tract without rupturing it.",
            "Dissect the tract superiorly toward the hyoid while separating it from strap muscles and preserving normal laryngeal framework.",
            "Expose the central hyoid body and divide it on each side of the tract, removing the central hyoid segment with the specimen.",
            "Continue the tract dissection superiorly through the tongue-base direction toward the foramen cecum, taking a small core of tissue rather than stopping at the hyoid.",
            "Avoid entry into pharyngeal mucosa; if entered, close the defect primarily.",
            "Remove the cyst, central hyoid, and superior tract as one specimen.",
            "Inspect for bleeding and confirm no residual epithelial tract remains in the operative field.",
            "Reapproximate strap tissues and close the neck in layers, with drain selectively based on dead space.",
        ]
    if _has(t, "branchial"):
        return [
            "Design a skin-crease incision over the lesion and expose the cyst/sinus tract while preserving capsule integrity.",
            "Develop the lesion circumferentially and identify its relationship to SCM, carotid sheath, and cranial nerves before following the tract deeply.",
            "For a second-branchial tract, anticipate passage between internal/external carotids toward the tonsillar fossa and protect hypoglossal/glossopharyngeal structures.",
            "For first-branchial anomalies, define the relationship to parotid and facial nerve before tract removal.",
            "Control feeding vessels and divide scarred attachments under direct visualization rather than traction avulsion.",
            "Follow the epithelial tract to its endpoint and remove the cyst/tract completely to minimize recurrence.",
            "Inspect the carotid sheath/nerve structures and obtain meticulous hemostasis.",
            "Close the wound in layers and place a drain only when the dead space warrants it.",
        ]

    # ---------- HEAD & NECK ONCOLOGY ----------
    if _has(t, "total laryngectomy"):
        return [
            "Raise apron/neck flaps and perform the planned neck dissection or central exposure while preserving recipient vessels and uninvolved cranial nerves needed for reconstruction.",
            "Mobilize the larynx by releasing strap/thyroid attachments and identify/protect carotid sheaths, hypoglossal/vagus structures, and viable parathyroid tissue when thyroid is partially preserved.",
            "Divide the trachea below tumor with adequate margin, mature/control the distal tracheal airway, and transition ventilation through the neck.",
            "Enter the pharynx at a tumor-safe site and perform circumferential mucosal cuts under direct visualization to obtain oncologic margins.",
            "Release the larynx from the tongue base/hypopharynx and remove the specimen en bloc with indicated thyroid/pharyngeal components.",
            "Send/confirm margins as indicated and perform primary TEP at this stage only when planned and oncologically/reconstructively appropriate.",
            "Close the pharynx with a watertight tension-free closure or inset flap reconstruction, then test the closure as appropriate.",
            "Create a wide permanent tracheostoma without tension, secure drains/flap monitoring, and remember the patient can thereafter be ventilated only through the neck stoma.",
        ]
    if _has(t, "neck dissection"):
        return [
            "Raise subplatysmal flaps to the planned superior/inferior limits and define the anterior border of SCM, midline, mandible, and clavicle.",
            "Identify and preserve the greater auricular nerve when appropriate, then expose the posterior belly of digastric and locate CN XI near its SCM entry or jugular relationship.",
            "Open the fascia along SCM and mobilize the lymphatic packet medially while preserving the carotid sheath unless oncologic involvement requires sacrifice.",
            "Clear level II around the upper IJV/CN XI, protecting hypoglossal nerve and avoiding traction injury to the accessory nerve.",
            "Continue inferiorly through levels III and IV, keeping the specimen on the deep cervical fascia and protecting phrenic nerve/brachial plexus at the floor.",
            "On the left low neck, identify and control the thoracic duct/major lymphatics before dividing tissue near the venous angle; on the right, remain alert to the right lymphatic duct.",
            "Clear level V or level I only when included in the planned dissection, with deliberate protection of CN XI, marginal mandibular nerve, hypoglossal/lingual nerves, and submandibular structures as applicable.",
            "Deliver the specimen by oriented levels, inspect preserved IJV/carotid/vagus/CN XI and the low-neck lymphatic bed, then obtain hemostasis and place drains.",
        ]
    if _has(t, "tors", "transoral robotic"):
        return [
            "Obtain stable transoral exposure with the target centered and protect teeth, tongue, lips, and endotracheal tube before docking.",
            "Identify the tumor margins and deep muscular plane, then plan mucosal cuts with orientation to lingual artery, glossopharyngeal nerve, carotid/parapharyngeal space, and mandible.",
            "Make the mucosal incision around the lesion and develop the deep plane under three-dimensional visualization, maintaining an intact specimen when possible.",
            "Control named or sizable arterial branches before transection rather than relying on delayed postoperative hemostasis.",
            "Complete the superior/inferior/deep cuts with adequate oncologic margin while preserving uninvolved functional tongue-base/pharyngeal tissue.",
            "Remove and orient the specimen and send additional margins from the patient bed when indicated.",
            "Inspect the deep bed for exposed carotid/parapharyngeal structures and secure meticulous hemostasis with Valsalva.",
            "Determine whether the defect needs secondary-intention healing, local flap, or free-flap reconstruction and set the postoperative airway/bleeding plan.",
        ]
    if _has(t, "oral composite", "composite resection", "mandibulectomy"):
        return [
            "Perform the planned neck exposure/dissection first when needed to control vessels, identify recipient vessels, and define the deep oncologic boundary.",
            "Mark mucosal margins around the oral cavity primary and identify the relationship to mandible, floor of mouth, tongue musculature, lingual/hypoglossal nerves, and Wharton duct.",
            "Make mucosal and soft-tissue cuts around the tumor, maintaining specimen orientation and controlling lingual/facial vessels as encountered.",
            "Perform marginal or segmental mandibulectomy at oncologically appropriate bony margins when bone is involved or required for access.",
            "Release the deep tongue/floor-of-mouth attachments while protecting uninvolved carotid-space and nerve structures.",
            "Deliver the specimen en bloc, orient it, and obtain mucosal/deep/bony margins as indicated.",
            "Prepare the defect and recipient vessels, then reconstruct lining, mandibular continuity, tongue/floor volume, and external cover according to the defect.",
            "Confirm airway, flap perfusion, hemostasis, occlusion when relevant, and drain/feeding access before closure.",
        ]
    if _has(t, "free flap"):
        return [
            "Define the defect requirements and recipient vessels before flap harvest; position so tumor ablation and donor-site teams can work without compromising either field.",
            "Harvest the chosen flap from known anatomic planes, identifying and preserving the vascular pedicle to adequate length while protecting critical donor nerves/tendons.",
            "Complete the recipient-site resection and prepare artery/vein branches with healthy adventitia-free ends and enough length to avoid tension or kinking.",
            "Transfer and inset the flap loosely enough to establish three-dimensional position before the pedicle is fixed in a compressed path.",
            "Perform venous and arterial microvascular anastomoses under magnification, then release clamps and assess inflow/outflow immediately.",
            "Correct twist, tension, vasospasm, or technical anastomotic problems before committing to final inset.",
            "Complete inset of lining/skin/bone while protecting the pedicle from compression by mandible, drains, closure, or neck position.",
            "Confirm clinical/Doppler perfusion, donor-site neurovascular status, hemostasis, and a clear postoperative flap-monitoring/re-exploration plan.",
        ]

    # ---------- FACIAL TRAUMA / RECONSTRUCTION ----------
    if _has(t, "orbital floor"):
        return [
            "Perform and document preoperative visual acuity, pupils, color vision, EOM, globe position, and CT-defined defect/entrapment before incision.",
            "Use the planned transconjunctival/subciliary approach and dissect to the orbital rim in the correct plane while protecting the globe and infraorbital nerve.",
            "Elevate periorbita from the orbital floor and identify intact posterior/lateral bony ledges around the defect.",
            "Reduce herniated orbital tissue completely from the maxillary sinus, freeing entrapped muscle/periorbita without aggressive traction.",
            "Measure the defect and shape the implant to rest on stable bony margins without impinging the optic canal or extraocular muscles.",
            "Place the implant under direct visualization and verify that no soft tissue is trapped beneath or around it.",
            "Repeat forced ductions and inspect globe position; revise the implant if restriction persists.",
            "Close the approach and immediately repeat vision, pupils, and EOM assessment; new proptosis/vision loss is an emergency.",
        ]
    if _has(t, "mandible orif", "mandibular fracture", "mandible fracture"):
        return [
            "Establish preinjury occlusion using dentition/arch relationships and secure maxillomandibular fixation or an equivalent occlusal reference before plating.",
            "Expose the fracture through intraoral or external access while protecting mental/inferior alveolar/facial nerve structures appropriate to the site.",
            "Debride only clearly nonviable tissue and reduce the fracture anatomically with the condyles seated and occlusion maintained.",
            "Place fixation along tension/compression zones appropriate to fracture location, keeping screws away from tooth roots and the inferior alveolar canal.",
            "For comminution/segmental instability, use load-bearing fixation with adequate screw purchase on both sides of the injury.",
            "Release or test MMF and verify stable reproducible occlusion through opening/closing.",
            "Irrigate and inspect for hardware conflict, nerve entrapment, or unstable fragments.",
            "Close intraoral/external incisions and set postoperative diet, oral hygiene, and fixation plan.",
        ]
    if _has(t, "zmc", "zygomaticomaxillary"):
        return [
            "Assess malar projection, ocular exam, trismus, and CT displacement at zygomaticofrontal, infraorbital rim, zygomaticomaxillary buttress, and arch interfaces.",
            "Expose the required fixation points through intraoral/lateral brow/transconjunctival approaches while protecting facial nerve and globe.",
            "Mobilize the zygoma and reduce it in three dimensions, using the sphenozygomatic region/arch/buttress alignment to judge rotation.",
            "Secure the most reliable reference point first, then sequentially fix additional buttresses while repeatedly checking malar symmetry.",
            "Inspect the orbital floor when the fracture pattern requires it and reconstruct any defect after the zygoma is reduced.",
            "Confirm infraorbital rim alignment, orbital volume, and absence of soft-tissue entrapment.",
            "Check forced ductions and ocular position before closure.",
            "Irrigate, obtain hemostasis, and close each approach in layers.",
        ]
    if _has(t, "nasal reduction", "closed nasal"):
        return [
            "Examine the external nose and septum under anesthesia, identifying sidewall depression, dorsal deviation, septal hematoma, and airway obstruction.",
            "Decongest the nose and use intranasal/external palpation to map mobile fracture segments.",
            "Elevate depressed nasal bones from inside the nose while applying counterpressure externally.",
            "Reduce laterally displaced fragments toward the midline in a controlled sequence and reassess dorsal width/projection.",
            "Address an acutely displaced septum when necessary for stable reduction and airway, avoiding aggressive septal resection in the trauma setting.",
            "Palpate the bony pyramid and inspect intranasally for mucosal injury, persistent obstruction, or septal hematoma.",
            "Apply internal support only when needed and mold an external splint to maintain the reduction.",
            "Document final alignment and postoperative precautions against repeat trauma.",
        ]
    if _has(t, "noe", "naso-orbito-ethmoid"):
        return [
            "Define the NOE fracture pattern and medial canthal tendon attachment on thin-cut CT before exposure.",
            "Expose the central midface through the required coronal/transconjunctival/intraoral or existing-wound approaches while protecting lacrimal structures.",
            "Identify the central fragment carrying the medial canthal tendon and determine whether the tendon remains attached to bone.",
            "Reduce the nasal/medial orbital buttresses in three dimensions using stable frontal/nasal/maxillary reference points.",
            "Fix the central fragment rigidly; if the medial canthal tendon is avulsed or attached to a non-fixable fragment, perform transnasal canthopexy to a stable position.",
            "Reconstruct associated orbital/nasal/frontal defects after central projection and intercanthal distance are restored.",
            "Confirm symmetric canthal position, nasal projection, globe position, and lacrimal considerations.",
            "Obtain hemostasis and close approaches with attention to soft-tissue redraping.",
        ]
    if _has(t, "laryngeal fracture"):
        return [
            "Secure the airway using the safest route for the injury pattern, avoiding traumatic trans-laryngeal intubation when the framework is unstable.",
            "Expose the laryngeal framework through a cervical incision and identify displaced thyroid/cricoid fractures and strap-muscle disruption.",
            "Open the larynx only when needed to repair mucosal tears, arytenoid displacement, or exposed cartilage.",
            "Reduce mucosal injury first so cartilage will not remain exposed to the airway.",
            "Reduce and rigidly fix displaced framework fractures to restore laryngeal height, width, and anterior commissure geometry.",
            "Repair vocal-fold/epiglottic/arytenoid injuries as indicated while preserving viable mucosa.",
            "Use an endolaryngeal stent only when necessary for severe mucosal disruption/anterior-commissure stabilization, recognizing stent morbidity.",
            "Reinspect endoscopically, confirm airway patency and hemostasis, and establish postoperative airway/voice/swallow surveillance.",
        ]

    # ---------- SLEEP ----------
    if _has(t, "hypoglossal", "inspire", "upper airway stimulation"):
        return [
            "Expose the submandibular upper neck and identify the hypoglossal nerve distal to the digastric tendon while protecting marginal mandibular and lingual structures.",
            "Use stimulation to distinguish protrusor branches from retrusor branches and select the inclusion branches that produce tongue protrusion without retraction.",
            "Place the stimulation cuff around the selected hypoglossal branches without nerve compression or inclusion of undesired branches.",
            "Create the chest generator pocket and expose the planned intercostal space for the respiratory-sensing lead.",
            "Place the sensing lead in the correct intercostal plane and secure it while avoiding pleural entry.",
            "Tunnel and connect stimulation and sensing leads to the generator with strain relief and no sharp kinks.",
            "Test the system for respiratory sensing and symmetric tongue protrusion, revising cuff/lead position if activation is retrusive or asymmetric.",
            "Obtain hemostasis, close neck/chest incisions without compressing hardware, and document delayed activation/titration plan.",
        ]
    if _has(t, "lingual tonsil"):
        return [
            "Obtain transoral exposure of the tongue base and identify the epiglottis, vallecula, circumvallate region, and lateral pharyngeal boundaries.",
            "Define the hypertrophic lingual-tonsil tissue and planned extent of reduction, preserving enough tongue-base mucosa to limit scar.",
            "Begin reduction centrally and work laterally under direct visualization with awareness of lingual-artery branches deep/lateral to the tongue base.",
            "Avoid deep muscle injury and uncontrolled thermal spread toward the epiglottis or neurovascular bundle.",
            "Remove obstructing lymphoid tissue symmetrically to achieve the planned airway space rather than pursuing complete lymphoid ablation.",
            "Control focal bleeding points directly and irrigate away char/debris.",
            "Reinspect the vallecula/epiglottis and confirm no dependent clot or tissue threatens the airway.",
            "Set postoperative airway observation and swallowing/bleeding precautions based on OSA severity and extent of resection.",
        ]
    if _has(t, "hyoid suspension", "hyoid myotomy"):
        return [
            "Expose the hyoid through a cervical incision and identify its body/greater cornua while protecting hypoglossal nerve and superior laryngeal neurovascular structures.",
            "Release the planned infrahyoid/suprahyoid attachments sufficiently to mobilize the hyoid without destabilizing swallowing structures unnecessarily.",
            "Advance the hyoid in the planned direction toward the thyroid cartilage or mandible depending on technique.",
            "Place suspension sutures/fixation symmetrically through robust hyoid and target framework/bone.",
            "Tension the suspension to enlarge the hypopharyngeal airway without excessive laryngeal elevation or asymmetry.",
            "Secure fixation and reassess hyoid/laryngeal position.",
            "Inspect for bleeding and nerve injury in the submandibular/laryngeal field.",
            "Close in layers and set postoperative airway/swallow observation.",
        ]
    if _has(t, "geniogloss", "genial tubercle"):
        return [
            "Expose the anterior mandible through the planned intraoral approach while protecting mental nerves and tooth roots.",
            "Map the genial tubercle/genioglossus attachment on the lingual cortex and define a safe osteotomy below dental roots.",
            "Create the rectangular/circular osteotomy around the genial tubercle without violating the inferior mandibular border.",
            "Mobilize the bone segment with the genioglossus attachment intact and advance it anteriorly.",
            "Rotate/secure the segment in the advanced position with rigid fixation while preventing posterior recoil.",
            "Confirm stable fixation and mandibular integrity.",
            "Obtain oral hemostasis and close the mucosa without trapping the mentalis.",
            "Set diet, oral-hygiene, and airway observation instructions.",
        ]

    # ---------- EMERGENCY / FOREIGN BODY ----------
    if _has(t, "button battery"):
        return [
            "Treat esophageal button battery as an immediate removal problem: secure the airway and proceed to rigid/flexible esophagoscopy without delaying for nonessential testing.",
            "Identify the battery location under direct endoscopic visualization and assess surrounding mucosal necrosis before grasping.",
            "Grasp and remove the battery along the axis of the esophagus, avoiding fragmentation or prolonged manipulation against injured mucosa.",
            "Reinsert the scope and inspect the entire injury zone circumferentially for depth, perforation, bleeding, and proximity to the aorta/airway.",
            "Do not aggressively debride adherent necrotic tissue that could open a contained perforation or vascular injury.",
            "Assess for additional foreign bodies and document exact injury level and severity.",
            "Institute the appropriate NPO, antibiotics/imaging, feeding-access, and vascular surveillance pathway based on depth/location of injury.",
            "Maintain a low threshold for multidisciplinary escalation because delayed fistula/hemorrhage can occur after apparently successful removal.",
        ]
    if _has(t, "airway foreign body", "bronchial foreign body", "foreign body airway"):
        return [
            "Coordinate a shared-airway anesthetic that preserves oxygenation while allowing rigid bronchoscopy; have age-appropriate rescue bronchoscopes/forceps immediately available.",
            "Perform direct laryngoscopy and pass the rigid bronchoscope under direct vision through the glottis.",
            "Survey trachea and both main bronchi before manipulating the object so its location and distal airway are understood.",
            "Choose forceps matched to the object's shape and grasp it securely under direct vision rather than pushing it distally.",
            "Withdraw foreign body and bronchoscope as a controlled unit when necessary to keep the object secured through the glottis.",
            "Reinsert the bronchoscope to inspect for a second object, mucosal injury, granulation, bleeding, and distal secretions.",
            "Suction obstructing secretions and treat airway edema/bronchospasm as required.",
            "Confirm bilateral ventilation and set postoperative observation based on hypoxia, pneumonia, edema, or difficult extraction.",
        ]
    if _has(t, "esophageal foreign body", "foreign body esophagus"):
        return [
            "Secure the airway as indicated and position for rigid or flexible esophagoscopy based on object, location, and perforation risk.",
            "Advance under direct visualization to the foreign body without blindly pushing it distally.",
            "Assess object orientation and surrounding mucosa before selecting the retrieval device.",
            "Grasp the object at a stable edge and withdraw it with the scope/protective hood as needed to protect mucosa and airway.",
            "Re-examine the impaction site for ulceration, laceration, perforation, or retained fragments.",
            "Survey the remaining esophagus when safe, particularly if ingestion history is uncertain.",
            "If perforation is suspected, stop routine feeding and obtain the appropriate imaging/surgical consultation rather than continuing traumatic instrumentation.",
            "Document object, location, mucosal injury, and postoperative diet/observation plan.",
        ]
    if _has(t, "peritonsillar", "pta drainage"):
        return [
            "Position with suction and airway equipment available, identify the tonsil, soft palate, uvula, and maximal bulge, and confirm that the airway is stable enough for bedside/OR drainage.",
            "Topically anesthetize/infiltrate the drainage site while keeping the needle depth controlled to avoid deep lateral vascular injury.",
            "Aspirate the superior pole region or image-defined collection and confirm pus before enlarging the opening.",
            "Incise the mucosa at the confirmed abscess site and bluntly spread into the cavity rather than cutting deeply laterally.",
            "Break loculations with blunt instrumentation and suction the cavity.",
            "Obtain cultures when clinically useful and irrigate selectively.",
            "Reassess airway, bleeding, hydration, and ability to tolerate oral intake.",
            "Escalate to quinsy tonsillectomy or deeper-neck evaluation when drainage is inadequate or disease pattern warrants it.",
        ]
    if _has(t, "deep neck", "neck abscess", "parapharyngeal abscess", "retropharyngeal abscess"):
        return [
            "Secure a potentially difficult airway before deep manipulation and review contrast imaging to map the collection relative to carotid sheath, aerodigestive tract, and mediastinum.",
            "Choose transoral versus transcervical access based on the compartment and obtain exposure that permits dependent drainage without crossing uninvolved spaces.",
            "Enter the abscess bluntly after the carotid/nerve relationships are defined; obtain cultures as purulence is encountered.",
            "Break loculations with blunt dissection and suction/irrigate the cavity, avoiding blind deep clamping toward the carotid sheath.",
            "Explore connected spaces only when imaging/operative findings show extension rather than creating unnecessary communication between fascial planes.",
            "Debride clearly nonviable tissue and address a dental/pharyngeal/salivary source when part of the same operation.",
            "Place a dependent drain for a cervical cavity when indicated and secure it away from major vessels.",
            "Confirm airway stability and define postoperative ICU, antibiotic, repeat-imaging, and mediastinal-surveillance needs.",
        ]

    # ---------- RECONSTRUCTION / FACIAL PLASTICS ----------
    if _has(t, "forehead flap"):
        return [
            "Template the nasal/facial defect and design the paramedian forehead flap around the supratrochlear vascular axis with sufficient length and width.",
            "Incise the distal flap and elevate in the appropriate subcutaneous/subgaleal plane, transitioning deeper near the pedicle to protect the supratrochlear vessels.",
            "Complete the flap elevation without narrowing, twisting, or skeletonizing the pedicle.",
            "Thin the distal flap selectively while preserving the subdermal plexus needed for perfusion.",
            "Rotate the flap into the defect without tension and reconstruct lining/support separately when required.",
            "Inset the flap precisely along aesthetic subunits and secure the pedicle bridge without compression.",
            "Close the forehead donor site primarily where possible and manage the residual superior defect appropriately.",
            "Check flap color/capillary refill and document the staged pedicle-division/refinement plan.",
        ]
    if _has(t, "bilobed flap"):
        return [
            "Measure the defect and design the first and second lobes around a pivot point that recruits lax adjacent skin while respecting nasal aesthetic subunits.",
            "Incise the flap and elevate in a plane thick enough to preserve the subdermal plexus.",
            "Undermine the surrounding recipient/donor area sufficiently to distribute tension and reduce pincushioning.",
            "Rotate the first lobe into the primary defect and the second lobe into the first-lobe donor defect without excessive torsion.",
            "Trim standing cones conservatively only after the flap is seated and perfusion is confirmed.",
            "Secure deep sutures to offload skin tension and align contour.",
            "Close skin with precise edge eversion and avoid strangulating the narrow flap base.",
            "Recheck flap perfusion and contour before dressing.",
        ]
    if _has(t, "melolabial", "nasolabial flap"):
        return [
            "Design the flap within the melolabial crease with dimensions matched to the defect and a base that preserves the intended subdermal/facial-artery blood supply.",
            "Incise and elevate the flap at the planned thickness, protecting the vascular base and avoiding unnecessary facial-nerve injury.",
            "Create the transfer path so the flap reaches the defect without pedicle compression or a conspicuous dog-ear.",
            "Thin the distal flap only as needed for contour while maintaining perfusion.",
            "Inset the flap into the recipient defect with deep sutures that restore three-dimensional support.",
            "Close the donor site along the melolabial fold with tension distributed away from the alar margin/lip.",
            "Check oral/nasal lining if the flap traverses a full-thickness defect.",
            "Confirm flap perfusion and document staged division if an interpolated design is used.",
        ]
    if _has(t, "cervicofacial"):
        return [
            "Design a broad rotation-advancement flap along relaxed skin/neck boundaries so the arc recruits enough laxity for a tension-free facial closure.",
            "Elevate the flap in a safe subcutaneous/SMAS-related plane appropriate to the region, protecting facial-nerve branches.",
            "Undermine widely rather than narrowing the pedicle to gain reach.",
            "Rotate/advance the flap into the defect and identify where deep anchoring sutures can shift tension to fixed fascia/periosteum.",
            "Trim only clearly redundant tissue after final position is established.",
            "Secure deep sutures to reduce pull on the eyelid, lip, or nasal margin.",
            "Close the donor and recipient sites in layers with drain placement only if dead space requires it.",
            "Confirm distal flap perfusion and absence of ectropion/oral commissure distortion.",
        ]

    return None


def apply_or_procedure_sequences_v200(registry):
    report = {"total": 0, "replaced": 0, "unmatched": [], "generic_removed": 0}
    for slug, op in (registry or {}).items():
        report["total"] += 1
        seq = _sequence_for(slug, op)
        old = [str(x) for x in (op.get("steps") or [])]
        report["generic_removed"] += sum(
            1 for step in old if any(p in step.lower() for p in GENERIC_PHRASES)
        )
        if seq:
            op["steps"] = seq
            op["sequence_status_v200"] = "procedure-specific"
            report["replaced"] += 1
        else:
            # Preserve the original pre-v20 sequence rather than inventing generic filler.
            op["steps"] = [
                step for step in old
                if not any(p in step.lower() for p in GENERIC_PHRASES)
            ]
            op["sequence_status_v200"] = "needs-procedure-review"
            report["unmatched"].append({"slug": slug, "title": op.get("title", "")})
        op["review_status_v200"] = "procedure-sequence deep pass"
    return report
