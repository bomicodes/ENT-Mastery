"""v31.0 — source-grounded congenital hearing-loss Concept Hub rebuild.

Separates congenital CMV hearing loss from genetic hearing loss. The CMV card owns the
infection-specific diagnostic window, progression/surveillance, antiviral decision context,
and hearing rehabilitation. The genetic card owns phenotype/inheritance analysis, modern
molecular testing, syndrome-directed workup, counseling, and genotype-informed prognosis.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")
TARGETS = {
    "congenital cmv hearing loss",
    "genetic hearing loss",
}


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


CONGENITAL_HEARING_REBUILD_V310 = {
    "congenital cmv hearing loss": {
        "recognize": (
            "Recognize congenital CMV (cCMV) as an ACQUIRED CONGENITAL INFECTION that can cause unilateral or bilateral sensorineural hearing loss even when the newborn otherwise appears well. The hearing phenotype is unusually dynamic: loss may be present at birth or delayed, and may be progressive or fluctuating. Do not collapse cCMV into the generic congenital-SNHL differential, because confirming congenital infection has a narrow postnatal diagnostic window and changes longitudinal surveillance, medical evaluation, and counseling. Symptomatic disease may also include petechiae/purpura, jaundice or hepatosplenomegaly, thrombocytopenia, microcephaly, seizures, chorioretinitis, growth restriction, and neuroimaging abnormalities."
        ),
        "localize": (
            "Localize the hearing deficit to the cochlea/auditory system while simultaneously grading SYSTEMIC cCMV severity. Audiometry/ABR defines ear-specific degree and configuration; the rest of the examination asks whether this is isolated hearing involvement or multisystem/CNS disease. Brain imaging in symptomatic infants may show periventricular calcifications, ventriculomegaly, white-matter injury, cortical malformations, or other abnormalities that alter prognosis. A normal external/middle-ear examination does not make the loss 'genetic'; cCMV often produces SNHL without a structural otoscopic clue."
        ),
        "workup": (
            "The boards-level diagnostic pearl is TIME. To establish congenital rather than postnatally acquired CMV, obtain CMV NAAT/culture from an appropriate infant specimen during the first 21 days of life; urine is confirmatory, and a positive saliva screen should be confirmed with urine because breast-milk contamination can create false-positive saliva results. After that window, a newly positive saliva/urine test cannot reliably prove congenital acquisition; retrospective newborn dried-blood-spot testing can sometimes help but has lower sensitivity, so a negative archived specimen does not fully exclude cCMV. Once cCMV is established, complete diagnostic audiology and assess CBC/platelets, liver function/bilirubin, ophthalmologic findings, neurologic status, growth, and neuroimaging as clinically indicated to distinguish asymptomatic infection, isolated SNHL, and symptomatic disease."
        ),
        "manage": (
            "Management has TWO PARALLEL TRACKS: cCMV disease management and hearing-development management. Infants with symptomatic cCMV—particularly CNS involvement—should be evaluated promptly with pediatric infectious disease for valganciclovir/ganciclovir therapy, balancing evidence of developmental/hearing benefit against neutropenia and other toxicity and monitoring CBC/liver/renal parameters. Do not teach antiviral treatment of otherwise asymptomatic isolated SNHL as an automatic standard: evidence and recommendations are less certain, so this decision belongs in specialist/shared decision-making rather than a reflex prescription. Regardless of antiviral use, establish serial ear-specific audiologic surveillance because hearing can deteriorate after a normal newborn screen, and move early on hearing aids, communication/language intervention, and educational support when loss is identified."
        ),
        "operate": (
            "Surgery treats the CONSEQUENCE of severe hearing loss, not the CMV infection. Children with severe-to-profound SNHL who receive inadequate benefit from appropriately fit amplification should undergo timely cochlear-implant candidacy evaluation rather than waiting for the hearing trajectory to declare itself indefinitely. Review neurodevelopmental status and imaging when counseling because CNS disease can affect developmental outcome, but cCMV itself is not a contraindication to cochlear implantation. Preserve the distinction between an ear-level rehabilitation decision and the infectious-disease decision about antivirals."
        ),
        "teach": (
            "Chief/boards framework: cCMV = NARROW DIAGNOSTIC WINDOW + POTENTIALLY DELAYED/PROGRESSIVE SNHL. A failed newborn hearing screen should trigger etiologic thinking while CMV testing can still prove congenital infection. Confirm saliva positives with urine and aim for testing within 21 days. Then separate three questions: (1) Is congenital CMV proven? (2) Is disease symptomatic/CNS-involved enough to support antiviral therapy? (3) What hearing surveillance and rehabilitation does each ear need? Do not assume a normal newborn screen excludes later cCMV-related hearing loss, and do not assume all congenital SNHL should be routed directly to genetics before time-sensitive CMV testing is considered."
        ),
        "tags": [
            "congenital CMV", "cytomegalovirus", "sensorineural hearing loss",
            "newborn hearing screen", "21 days", "urine PCR", "saliva PCR",
            "delayed hearing loss", "valganciclovir", "cochlear implant"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — congenital and pediatric sensorineural hearing loss, congenital infection, etiologic evaluation, and hearing rehabilitation",
            "K.J. Lee's Essential Otolaryngology, 12e, Ch. 17 Congenital Hearing Loss — congenital CMV within the acquired/nongenetic congenital hearing-loss differential",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — pediatric otology, congenital disorders, and hearing-loss evaluation",
            "CDC 2024 congenital CMV case definition — congenital infection testing within 21 days and urine confirmation of saliva detection",
            "Current cCMV treatment literature — antiviral therapy for symptomatic disease; isolated-SNHL treatment remains a specialist evidence-based decision rather than a universal default",
        ],
    },
    "genetic hearing loss": {
        "recognize": (
            "Recognize genetic hearing loss as an ETIOLOGIC/PROGNOSTIC diagnosis, not shorthand for 'congenital bilateral SNHL.' Genetic loss may be congenital or later-onset, unilateral or bilateral, stable or progressive, syndromic or nonsyndromic. Family history can be absent because autosomal-recessive disease and de novo variants are common enough that normal-hearing parents do not exclude genetics. Start with the audiophenotype and associated features: congenital severe-profound loss, mild-moderate loss, progressive or fluctuating loss, auditory neuropathy, enlarged vestibular aqueduct, pigmentary/ocular/renal/cardiac/thyroid findings, vestibular dysfunction, and medication-triggered susceptibility each narrow the biologic hypothesis."
        ),
        "localize": (
            "Localize at THREE LEVELS: auditory site, phenotype, and inheritance. Confirm conductive versus sensorineural versus auditory-neuropathy physiology; define laterality, severity, frequency configuration, and progression; then build a three-generation pedigree and syndromic review. High-yield genotype-phenotype anchors include GJB2-related recessive nonsyndromic SNHL; STRC as a common cause of mild-to-moderate recessive SNHL; SLC26A4 with enlarged vestibular aqueduct/Pendred-spectrum disease; OTOF with auditory synaptopathy/neuropathy and preserved cochlear structure; Usher-spectrum genes with retinal disease; EYA1/SIX1-related branchio-oto-renal spectrum; and MT-RNR1 variants that confer marked aminoglycoside ototoxic susceptibility. These anchors guide interpretation but should not turn the workup into one-gene guessing."
        ),
        "workup": (
            "Confirm hearing with age-appropriate diagnostic audiology/ABR and examine the child for syndromic clues before ordering molecular testing. Modern etiologic evaluation generally favors a comprehensive hearing-loss multigene panel with sequence plus deletion/duplication coverage, or exome/genome testing when appropriate, rather than serial single-gene testing based only on prevalence. Interpret pathogenic/likely pathogenic variants in the phenotype and inheritance context; a variant of uncertain significance does NOT establish or exclude the diagnosis. Add targeted studies when the phenotype demands them—for example ophthalmology for Usher concern, renal evaluation for branchio-oto-renal features, ECG for long-QT/Jervell-Lange-Nielsen concern, and thyroid surveillance for Pendred-spectrum disease. CT/MRI answers structural and cochlear-implant questions; it does not replace molecular testing. In a neonate, also remember time-sensitive acquired etiologies such as cCMV rather than labeling every early SNHL 'genetic.'"
        ),
        "manage": (
            "Use the genetic diagnosis to change care, not merely to name a gene. Provide genetics/genetic-counseling referral for inheritance, recurrence risk, cascade testing, reproductive implications, and interpretation of uncertain results. Anticipate syndromic complications before symptoms when the genotype supports them, avoid genotype-specific hazards such as aminoglycosides in individuals with pathogenic MT-RNR1 susceptibility variants when alternatives exist, and counsel whether hearing is usually stable or progressive. Hearing management remains function-based: early language access, appropriately fit amplification, remote-microphone/educational support, and cochlear-implant evaluation when audibility and speech/language progress remain inadequate."
        ),
        "operate": (
            "For cochlear implantation, combine auditory performance with anatomy and GENOTYPE-informed expectations. Many cochlear genetic causes preserve the cochlear nerve and central auditory pathway and can have excellent CI performance; a genetic diagnosis should not be used to delay implantation when functional criteria are met. Imaging remains essential when malformation, cochlear-nerve deficiency, or surgical anatomy is suspected. Conversely, a poor or absent cochlear nerve changes the rehabilitation pathway regardless of whether a molecular diagnosis is also present. Emerging gene-directed therapies make precise molecular diagnosis increasingly clinically relevant, but they complement rather than replace established hearing rehabilitation unless the child meets a validated treatment indication."
        ),
        "teach": (
            "Chief/boards framework: GENETIC HEARING LOSS = PHENOTYPE → PEDIGREE/SYNDROMIC SCREEN → BROAD MOLECULAR TEST → INTERPRET → ACT. Do not equate 'no family history' with nongenetic disease, do not call a VUS diagnostic, and do not order a parade of isolated genes when an appropriately designed multigene/genomic test is available. Know the classic associations—GJB2, STRC, SLC26A4/EVA, OTOF/auditory neuropathy, Usher, branchio-oto-renal, long-QT, and MT-RNR1—but use them to understand mechanisms and clinical consequences rather than as a memorization-only gene list. Most importantly, keep this card distinct from cCMV: genetics owns inheritance, molecular diagnosis, syndromic surveillance, and counseling; cCMV owns congenital-infection confirmation, the 21-day testing window, antiviral context, and delayed/progressive infection-related hearing surveillance."
        ),
        "tags": [
            "genetic hearing loss", "GJB2", "STRC", "SLC26A4", "OTOF",
            "Usher syndrome", "branchio-oto-renal", "MT-RNR1", "multigene panel",
            "genetic counseling", "cochlear implant"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — genetic and congenital hearing loss, syndromic/nonsyndromic etiologies, molecular diagnosis, and rehabilitation",
            "K.J. Lee's Essential Otolaryngology, 12e, Ch. 17 Congenital Hearing Loss — inheritance patterns, GJB2/GJB6, syndromic hearing loss, and genetic evaluation",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — pediatric otology and congenital/syndromic hearing-loss evaluation",
            "ACMG Clinical Practice Resource: Clinical evaluation and etiologic diagnosis of hearing loss (Genetics in Medicine, 2022)",
            "GeneReviews Genetic Hearing Loss Overview, revised June 2, 2026 — current genotype-phenotype framework and preference for multigene/genomic testing",
            "CPIC Guideline for aminoglycosides based on MT-RNR1 genotype (2022) — avoidance of aminoglycosides in high-risk pathogenic-variant carriers when clinically feasible",
        ],
    },
}


def apply_congenital_hearing_rebuild_v310(data_module, app_module=None):
    """Patch exact concept titles wherever they live without moving their domain/IDs."""
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = CONGENITAL_HEARING_REBUILD_V310.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v310"] = True
            module["semantic_role_v310"] = (
                "congenital CMV infection confirmation, hearing trajectory, antiviral context, and rehabilitation"
                if key == "congenital cmv hearing loss"
                else "genetic etiology, molecular diagnosis, syndromic surveillance, counseling, and genotype-informed rehabilitation"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
