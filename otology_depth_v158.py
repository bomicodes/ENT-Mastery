"""v15.8 — Otology deep-curriculum enrichment.

First focused pass after the new scannable Deep Curriculum UI exposed that some
modules were structurally present but incomplete as teaching references.

This patch enriches two high-yield Otology topics in place:
- Sudden Sensorineural Hearing Loss: adds an etiologic framework without
  encouraging shotgun laboratory testing.
- Chronic Otitis Media / Cholesteatoma: adds acquired pathogenesis, congenital
  disease, CWU-vs-CWD decision-making, surveillance, complications, and timing
  of ossicular reconstruction.

No new canonical topics are created. The existing curriculum homes are updated
in place so concept IDs, mastery history, and related-case links remain stable.
"""

OTOLOGY_DOMAIN_V158 = "Otology / Neurotology"

SSNHL_TOPIC_CANDIDATES_V158 = (
    "Sudden Sensorineural Hearing Loss",
    "Sudden SNHL",
)

CHOLESTEATOMA_TOPIC_CANDIDATES_V158 = (
    "Chronic Otitis Media / Cholesteatoma",
    "Cholesteatoma",
)

SSNHL_DEPTH_V158 = {
    "recognize": (
        "Treat a sudden unilateral sensorineural change as time-sensitive even when the patient describes fullness or a blocked ear. "
        "First distinguish SNHL from conductive loss with otoscopy, bedside tuning forks, and prompt audiometry. Important etiologic buckets are idiopathic (most common), viral/inflammatory, autoimmune inner-ear disease, vascular/ischemic, infectious (for example syphilis or Lyme disease when exposure/risk makes them plausible), traumatic/barotrauma, ototoxic, cochlear hydrops/Meniere-spectrum disease, and retrocochlear pathology such as vestibular schwannoma. Bilateral, recurrent, fluctuating, neurologic, or systemic-inflammatory presentations should broaden the differential beyond typical idiopathic SSNHL."
    ),
    "localize": (
        "Use the history, otoscopy, tuning forks, and audiogram to separate external/middle-ear conductive disease from cochlear or retrocochlear SNHL. "
        "Cochlear clues include tinnitus, recruitment, or associated vertigo; asymmetric speech discrimination, focal neurologic findings, or other cranial neuropathies increase concern for retrocochlear or central disease. A normal ear canal and tympanic membrane do not by themselves prove SSNHL — the audiogram localizes the loss."
    ),
    "workup": (
        "Obtain audiometry as soon as possible and within 14 days of onset to document SSNHL. Evaluate for retrocochlear pathology with MRI of the internal auditory canals/brain (or ABR when MRI cannot be obtained). "
        "Do not routinely order head CT or indiscriminate laboratory panels for otherwise typical idiopathic SSNHL. Targeted testing is appropriate when the history suggests a specific cause — for example autoimmune symptoms, infectious exposure, bilateral/recurrent disease, trauma, ototoxic exposure, or another systemic process. Document baseline and follow-up speech understanding as well as pure-tone thresholds."
    ),
    "manage": (
        "Counsel that many cases remain idiopathic and that spontaneous recovery can occur, but treatment is time sensitive. Corticosteroids may be offered as initial therapy within 2 weeks of onset. Hyperbaric oxygen with steroids may be offered within 2 weeks initially or within 1 month as salvage in selected patients. "
        "Offer intratympanic steroid salvage for incomplete recovery approximately 2–6 weeks after onset. Do not routinely prescribe antivirals, thrombolytics, vasodilators, or vasoactive drugs. Treat an identified secondary cause specifically when one is found, and address residual hearing loss/tinnitus with rehabilitation."
    ),
    "operate": (
        "SSNHL is not primarily an operative disorder. The main procedure is intratympanic steroid delivery for appropriate initial or salvage treatment. Counsel about access/anesthesia, transient vertigo, otalgia, and tympanic-membrane perforation risk while avoiding delay in the treatment window. "
        "Persistent severe/profound loss with poor aided speech understanding later shifts the discussion from salvage therapy to hearing rehabilitation, including conventional amplification, CROS/BiCROS, bone-conduction options, or cochlear implantation when candidacy criteria are met."
    ),
    "teach": (
        "Board framework: first prove the loss is sensorineural, then treat promptly, then ask whether the presentation is truly idiopathic or whether a specific cause is being signaled. Idiopathic is the most common final category, but it is not a reason to skip retrocochlear evaluation. "
        "Know the treatment windows: initial steroids within 2 weeks, salvage intratympanic steroids roughly 2–6 weeks, and selected hyperbaric oxygen within the early treatment/salvage window. Recheck hearing at treatment completion and within 6 months, and rehabilitate persistent hearing loss/tinnitus."
    ),
    "tags": [
        "SSNHL", "sudden sensorineural hearing loss", "steroids", "intratympanic steroid",
        "retrocochlear", "vestibular schwannoma", "autoimmune", "viral", "vascular",
        "ototoxicity", "Meniere", "hearing rehabilitation"
    ],
}

CHOLESTEATOMA_DEPTH_V158 = {
    "recognize": (
        "Acquired cholesteatoma is keratinizing squamous epithelium within the middle ear/mastoid that accumulates keratin and causes progressive inflammation and bony erosion. Recognize pars-flaccida/attic or pars-tensa retraction pockets with keratin, chronic foul otorrhea, conductive hearing loss, granulation, or visible white debris. "
        "Primary acquired cholesteatoma develops behind an intact tympanic membrane, usually from a retraction pocket. Secondary acquired cholesteatoma occurs when squamous epithelium reaches the middle ear through a pre-existing perforation or after trauma/surgery. Congenital cholesteatoma classically presents as a pearly white middle-ear mass behind an intact tympanic membrane without a history that explains epithelial implantation; children may present with conductive loss or an incidental white mass rather than chronic drainage."
    ),
    "localize": (
        "Track disease in three dimensions. Pars-flaccida disease commonly enters Prussak space/epitympanum and can extend through the aditus into mastoid; pars-tensa disease can involve mesotympanum, sinus tympani, facial recess, hypotympanum, and other hidden recesses. "
        "High-risk relationships include the ossicles, facial nerve, lateral semicircular canal, tegmen, sigmoid sinus, dural plate, and labyrinth. Congenital disease is often described in the anterior-superior middle ear early in its course but can arise elsewhere and may extend posteriorly, involve ossicles, or reach mastoid as it advances."
    ),
    "workup": (
        "Microscopic or endoscopic ear examination and audiometry are foundational. CT temporal bone defines bony anatomy, scutum/ossicular erosion, mastoid aeration, labyrinthine fistula, tegmen or facial-canal dehiscence, and surgical landmarks; CT does not reliably distinguish cholesteatoma from all other soft tissue. "
        "Non-echo-planar diffusion-weighted MRI is useful for selected residual/recurrent disease surveillance and can reduce the need for routine second-look surgery in some patients, but very small lesions may escape detection. Facial weakness, vertigo, severe headache, fever, neurologic symptoms, or other cranial neuropathy should trigger evaluation for complications."
    ),
    "manage": (
        "Definitive management is usually surgical because cholesteatoma is locally destructive and cannot be cured by topical therapy alone. Treat active infection/otorrhea enough to make surgery safer, but do not confuse temporary drying of the ear with eradication of disease. "
        "For congenital cholesteatoma, surgery is also the definitive treatment; the approach is tailored to extent. Small localized middle-ear lesions may be removed transcanally/endoscopically, whereas posterior, ossicular, or mastoid extension requires a broader tympanotomy/tympanomastoid approach. The goals are complete epithelial removal, a safe dry maintainable ear, preservation of the facial nerve/labyrinth, and hearing rehabilitation when it can be done without compromising disease control."
    ),
    "operate": (
        "Pathogenesis matters: primary acquired disease is best explained by retraction-pocket/invagination mechanisms driven by poor middle-ear ventilation plus inflammatory remodeling; the mucosal-traction theory adds that inflamed middle-ear mucosa/adhesions can physically tether the tympanic membrane medially and propagate retraction. Secondary acquired disease is explained by epithelial migration or implantation through a tympanic-membrane perforation or surgical/traumatic defect. Basal-cell hyperplasia and squamous metaplasia are additional historical theories but are less useful than the retraction/migration framework for operative reasoning. "
        "Choose canal-wall-up (CWU) when complete clearance is achievable while preserving the posterior canal wall, anatomy is favorable, and reliable surveillance/possible second-look or non-EPI DWI follow-up is realistic; advantages include more normal canal anatomy and easier water tolerance, but residual/recurrent disease risk and surveillance burden are higher. Choose canal-wall-down (CWD) when safe complete clearance would otherwise be compromised — for example extensive or recurrent disease, difficult hidden extension, unfavorable/contracted anatomy, major bony erosion/complication, or unreliable long-term follow-up. CWD improves exposure and disease control but creates a cavity that may require lifelong maintenance; obliteration/reconstruction can reduce cavity morbidity in selected cases. These are judgment frameworks rather than absolute rules. "
        "Ossicular reconstruction comes after disease control. Single-stage ossiculoplasty is reasonable when cholesteatoma has been completely cleared, the middle-ear mucosa is healthy/stable, and residual-disease risk is low. Stage reconstruction when clearance is uncertain, disease is extensive, mucosa is inflamed/poorly aerated, a planned second-look is expected, or the stapes/footplate environment is unsafe. If the stapes superstructure is intact, a PORP or cartilage/interposition strategy may be used; if the superstructure is absent but the footplate is mobile, a TORP may be required. Never trade complete cholesteatoma clearance for hearing reconstruction."
    ),
    "teach": (
        "Boards/chief framework: cholesteatoma is a three-dimensional destructive epithelial disease, not simply 'skin behind the eardrum.' Primary acquired disease usually begins with retraction; secondary acquired disease gains access through a perforation/implantation pathway; congenital disease begins without either mechanism and often presents behind an intact tympanic membrane. "
        "The operative hierarchy is safe ear → dry/maintainable ear → hearing. CWU versus CWD is chosen by whether disease can be eradicated safely and whether surveillance is dependable, not by prestige or a single imaging finding. Hidden sites such as sinus tympani and facial recess drive residual disease. Hearing reconstruction may be simultaneous only when clearance and the middle-ear environment are favorable; otherwise stage it. Surveillance is part of the operation: second-look surgery and/or serial non-EPI DWI MRI are tools for detecting residual/recurrent disease."
    ),
    "tags": [
        "cholesteatoma", "primary acquired", "secondary acquired", "congenital cholesteatoma",
        "retraction pocket", "mucosal traction", "epithelial migration", "canal wall up",
        "canal wall down", "CWU", "CWD", "ossiculoplasty", "PORP", "TORP",
        "non-EPI DWI", "second look", "labyrinthine fistula", "facial nerve"
    ],
}


def _find_topic(modules, candidates):
    for module in modules:
        if module.get("topic") in candidates:
            return module
    return None


def apply_otology_depth_v158(deep_modules):
    """Enrich existing Otology topics in place; never create duplicates."""
    modules = deep_modules.get(OTOLOGY_DOMAIN_V158, [])
    if not modules:
        raise RuntimeError("v15.8: Otology / Neurotology domain is missing")

    ssnhl = _find_topic(modules, SSNHL_TOPIC_CANDIDATES_V158)
    if ssnhl is None:
        raise RuntimeError(
            "v15.8: could not find the canonical Sudden Sensorineural Hearing Loss topic"
        )
    ssnhl.update(SSNHL_DEPTH_V158)

    chol = _find_topic(modules, CHOLESTEATOMA_TOPIC_CANDIDATES_V158)
    if chol is None:
        raise RuntimeError(
            "v15.8: could not find the canonical Cholesteatoma topic"
        )
    chol.update(CHOLESTEATOMA_DEPTH_V158)

    return {
        "ssnhl": ssnhl.get("topic"),
        "cholesteatoma": chol.get("topic"),
    }
