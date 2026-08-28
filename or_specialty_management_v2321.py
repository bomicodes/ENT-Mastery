"""v23.21 focused specialty OR Tomorrow management review.

Adds procedure-specific planning and postoperative rescue to five remaining specialty
modules: canalplasty/exostosis, central neck dissection, cricotracheal resection,
maxillary antrostomy, and tegmen CSF leak/encephalocele repair. Existing anatomy,
operative sequence and prior high-consequence safety content remain intact. The v23.22
final review is chained through this tail to preserve one ordered runtime mutation path.
"""

from or_final_management_v2322 import apply_or_final_management_v2322

TARGETS = [
    {
        "slug": "canalplasty",
        "title_terms": ("canalplasty",),
        "setup": [
            "Before canalplasty/exostosis surgery, document the indication and baseline hearing: recurrent water trapping/otitis externa, conductive hearing loss, debris retention or near-obstructive disease should be correlated with otoscopy and audiometry rather than operating on canal narrowing alone. Review CT when medial extent, middle-ear disease or anatomy is uncertain, and plan the approach according to lesion location while preserving canal skin and avoiding unnecessary manipulation of the tympanic membrane and ossicles.",
            "Counsel that adequate bony widening must be balanced against preservation of healthy canal skin, because circumferential skin loss and exposed bone increase postoperative stenosis risk. Identify the facial nerve, temporomandibular joint/anterior canal wall and tympanic membrane as structures that can become vulnerable as drilling proceeds medially.",
        ],
        "postop": [
            "After canalplasty, protect canal skin grafts/flaps and packing and monitor for infection, hematoma, persistent otorrhea or severe vertigo/hearing change. Sudden sensorineural hearing loss, facial weakness, marked vertigo or tympanic-membrane injury is not expected and warrants prompt otologic assessment rather than waiting for packing removal.",
            "Long-term follow-up should assess epithelialization and canal caliber. Recurrent narrowing, granulation or chronic debris trapping suggests scar/restenosis or inadequate skin coverage; persistent conductive loss should trigger reassessment of the canal, tympanic membrane and middle ear rather than assuming it is residual edema indefinitely.",
        ],
        "marker": "canalplasty_management_v2321",
    },
    {
        "slug": "central-neck",
        "title_terms": ("central", "neck", "dissection"),
        "setup": [
            "Before central neck dissection, define the exact oncologic indication and intended compartment—typically level VI with level VII when indicated—using the primary tumor/pathology, ultrasound and cross-sectional imaging as appropriate. Review prior thyroid/central-neck surgery, baseline vocal-fold mobility when recurrent-laryngeal-nerve risk is elevated, and the status/location of remaining parathyroid tissue; do not import lateral-neck levels or spinal-accessory/jugular anatomy into a central-compartment operation.",
            "Plan the dissection around both recurrent laryngeal nerves, tracheoesophageal grooves, prelaryngeal/pretracheal/paratracheal nodal basins and parathyroid vascular preservation. Bilateral central dissection, reoperation, invasive disease and a pre-existing unilateral vocal-fold deficit materially increase airway, nerve and hypocalcemia risk and should change counseling and postoperative surveillance.",
        ],
        "postop": [
            "After central neck dissection, an expanding neck hematoma, stridor or respiratory distress is an airway emergency. New dysphonia, weak cough or aspiration should prompt vocal-fold assessment when recurrent-laryngeal-nerve dysfunction is possible; bilateral dysfunction can present primarily as airway compromise rather than voice change.",
            "Follow calcium/PTH according to the extent of thyroid/parathyroid manipulation and patient risk. Perioral/acral paresthesias, cramps or tetany should prompt evaluation and treatment for hypocalcemia, while persistent chyle-type drainage should not be expected from a routine central dissection and should trigger reconsideration of the actual dissection field or another source.",
        ],
        "marker": "central_neck_management_v2321",
    },
    {
        "slug": "ctr",
        "title_terms": ("cricotracheal", "resection"),
        "setup": [
            "Before cricotracheal resection, define the stenosis precisely by endoscopy and imaging: subglottic/cricoid involvement, length, posterior cricoid plate status, distance to the vocal folds, tracheal involvement and vocal-fold mobility determine whether CTR is appropriate and how much framework can be safely resected. Review prior airway reconstruction, tracheostomy, inflammatory disease and pulmonary/swallow reserve, and distinguish a reconstructable fixed stenosis from active inflammation or diffuse disease that may need a different strategy.",
            "Coordinate a shared-airway and distal-ventilation plan with anesthesia and anticipate the release maneuvers required for a low-tension anastomosis before committing to resection. Preservation of recurrent-laryngeal-nerve function and a viable posterior mucosal framework is critical; the operation should not trade an open airway for bilateral vocal-fold dysfunction or an untenable anastomosis.",
        ],
        "postop": [
            "After CTR, new stridor, subcutaneous emphysema, hemoptysis, neck swelling, air leak, respiratory distress or sudden voice change should raise concern for anastomotic compromise, edema, hematoma or recurrent-laryngeal-nerve dysfunction. Avoid repeated traumatic transanastomotic instrumentation and escalate early to the airway surgeon/anesthesia team if respiratory status deteriorates.",
            "Maintain the planned neck-position/tension-reduction strategy and monitor swallowing, secretion clearance and pulmonary status. Fever, progressive neck/mediastinal pain, wound air, increasing oxygen need or sepsis should prompt evaluation for anastomotic leak/deep infection; later recurrent dyspnea should be evaluated for restenosis or granulation rather than managed as nonspecific postoperative breathing difficulty.",
        ],
        "marker": "ctr_management_v2321",
    },
    {
        "slug": "maxillary-antrostomy",
        "title_terms": ("maxillary", "antrostomy"),
        "setup": [
            "Before endoscopic maxillary antrostomy, confirm why the maxillary sinus is diseased and whether surgery addresses the cause: inflammatory CRS, odontogenic disease, fungal ball, antrochoanal polyp, mucocele or unilateral atypical disease have different source-control and pathology implications. Review CT/endoscopy for the natural ostium, uncinate/infundibulum, accessory ostia, nasolacrimal duct and orbital floor/lamina, and investigate unilateral disease that is atypical for routine inflammatory sinusitis rather than assuming every opacified maxillary sinus is the same operation.",
            "The surgical target is incorporation of the natural maxillary ostium into a durable opening, not creation of a separate posterior fontanelle hole that leaves two competing pathways. Recognize and connect an accessory ostium when appropriate to avoid mucus recirculation, and coordinate dental source control when odontogenic disease is driving the sinus process.",
        ],
        "postop": [
            "After maxillary antrostomy, brisk epistaxis, new orbital pain/swelling or visual symptoms, clear rhinorrhea or progressive facial swelling is not routine postoperative congestion and requires targeted reassessment. Persistent unilateral purulence or recurrent maxillary disease should prompt evaluation for retained odontogenic source, fungal material, foreign body, tumor or ostial restenosis rather than repeated antibiotics alone.",
            "At follow-up, confirm that the natural ostium is incorporated and patent and look for synechiae or recirculation between natural/accessory openings. Persistent symptoms with a technically open antrostomy should trigger reconsideration of the original diagnosis rather than reflexively enlarging the opening further.",
        ],
        "marker": "maxillary_antrostomy_management_v2321",
    },
    {
        "slug": "tegmen-repair",
        "title_terms": ("tegmen", "csf"),
        "setup": [
            "Before tegmen CSF leak/encephalocele repair, confirm the leak/defect and review high-resolution temporal-bone CT plus MRI when encephalocele or soft-tissue differentiation is important. Document hearing, middle-ear status and prior meningitis and assess whether the defect is isolated or multifocal; spontaneous lateral-skull-base leaks should prompt consideration of the broader intracranial-pressure/obesity context because untreated pressure physiology can contribute to recurrence.",
            "Choose transmastoid, middle-fossa or combined repair according to defect size/location, multiplicity, encephalocele extent, ossicular/hearing considerations and need for direct dural access rather than using one corridor for every tegmen defect. Plan multilayer closure and protection of the ossicles, facial nerve and temporal lobe before opening the defect.",
        ],
        "postop": [
            "After tegmen repair, persistent clear otorrhea/rhinorrhea, enlarging pseudomeningocele, severe headache, fever/meningismus, altered mental status or neurologic change should prompt urgent evaluation for recurrent CSF leak, meningitis or intracranial complication. New facial weakness, substantial hearing loss or severe vertigo also requires focused otologic assessment rather than routine observation.",
            "Long-term follow-up should address recurrent leak/encephalocele, hearing outcome and the underlying pressure context when relevant. A dry ear immediately after surgery does not alone prove durable closure, particularly in spontaneous or multifocal skull-base disease.",
        ],
        "marker": "tegmen_repair_management_v2321",
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in target["title_terms"]):
            return slug, op
    return None, None


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_specialty_management_v2321(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v2322 = apply_or_final_management_v2322(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v2322": v2322}
