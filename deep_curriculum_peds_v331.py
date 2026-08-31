"""v33.1 — source-grounded congenital CMV versus genetic hearing-loss rebuild.

Congenital CMV owns the time-critical infectious diagnosis, serial audiology, systemic disease
assessment, antiviral-selection nuance, and rehabilitation of delayed/progressive SNHL.
Congenital hearing-loss genetics owns etiologic pattern recognition, molecular testing,
syndrome-directed evaluation, counseling, prognosis, and gene-informed rehabilitation.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


CONGENITAL_HEARING_REBUILD_V331 = {
    "congenital cmv hearing loss": {
        "recognize": (
            "Use this card for the INFECTIOUS cCMV pathway, not as a generic congenital-SNHL workup. Congenital CMV can cause unilateral or bilateral SNHL that is present at birth, delayed-onset, fluctuating, or progressive; therefore a normal newborn hearing screen does not exclude later cCMV-associated hearing loss. Look for symptomatic congenital infection—microcephaly, petechiae/purpura, hepatosplenomegaly, jaundice, growth restriction, seizures, chorioretinitis or characteristic CNS imaging—but remember that hearing loss can occur in infants who otherwise appeared asymptomatic."
        ),
        "localize": (
            "Localize two things separately: AUDITORY phenotype and SYSTEMIC cCMV burden. Define ear-specific thresholds and trajectory with age-appropriate diagnostic audiology/ABR, while assessing neurologic, ophthalmologic, hepatic/hematologic and developmental involvement when congenital infection is confirmed. cCMV is a cochlear/inner-ear infectious injury and does not require an anatomic malformation; if imaging, examination, family history, or the longitudinal phenotype suggests a second etiology, do not stop the workup merely because CMV is present—genetic and infectious causes can coexist."
        ),
        "workup": (
            "The diagnostic clock is the boards-critical point: confirm congenital infection with CMV nucleic-acid testing from SALIVA or URINE collected within the first 2-3 weeks of life (classically <=21 days); CDC favors saliva PCR with urine confirmation. After that window, a positive specimen cannot reliably distinguish congenital from postnatal acquisition. CMV IgG/IgM does NOT establish congenital infection. In a newborn who refers on hearing screening, follow local/state targeted-cCMV pathways immediately rather than waiting for the later diagnostic-audiology visit and missing the congenital-testing window. Once cCMV is confirmed, obtain the disease-severity assessment needed to decide whether infectious-disease antiviral therapy is indicated and establish serial audiologic follow-up because hearing can deteriorate after infancy."
        ),
        "manage": (
            "Separate ANTIVIRAL CANDIDACY from HEARING REHABILITATION. Infants with clinically significant symptomatic congenital CMV, particularly CNS involvement, should be evaluated promptly with pediatric infectious disease for valganciclovir-based therapy and toxicity monitoring. Do not teach valganciclovir as routine treatment for every infant with isolated SNHL: CDC notes limited evidence for hearing-loss-only disease, and a randomized trial found no hearing benefit when valganciclovir was initiated after 1 month of age. Regardless of antiviral choice, manage the hearing loss on its own merits with timely amplification, speech/language and early-intervention services, and cochlear-implant evaluation when thresholds and aided benefit warrant it."
        ),
        "operate": (
            "There is no operation that treats CMV itself. The otologic procedure question is AUDITORY REHABILITATION: children with severe-to-profound loss and inadequate aided speech access should enter a pediatric cochlear-implant pathway without waiting for hearing to become permanently stable, because cCMV loss may fluctuate or progress. Pre-CI imaging and multidisciplinary developmental assessment are individualized; neurologic/developmental comorbidity can affect rehabilitation expectations but is not by itself a reason to deny useful auditory access. Continue surveillance of the contralateral/better ear because asymmetric disease can later become bilateral."
        ),
        "teach": (
            "Chief/boards discriminator: cCMV = TIME-CRITICAL ETIOLOGIC CONFIRMATION + LONGITUDINAL HEARING RISK. Saliva/urine PCR must be obtained in the first 2-3 weeks to prove congenital infection; antibody testing does not do it. A passed newborn screen does not end follow-up because loss can be delayed/progressive. Antivirals are for appropriately selected congenital disease, not an automatic response to isolated SNHL. This differs from the genetics card, whose core question is WHICH MOLECULAR/SYNDROMIC DIAGNOSIS explains the hearing phenotype and what that means for the child and family."
        ),
        "tags": ["congenital CMV", "cCMV", "congenital hearing loss", "progressive SNHL", "delayed-onset hearing loss", "saliva PCR", "urine PCR", "21 days", "valganciclovir", "cochlear implant"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — congenital/pediatric hearing loss, congenital infection, diagnostic audiology, and rehabilitation framework",
            "K.J. Lee's Essential Otolaryngology, 12e — congenital CMV as a major infectious cause of congenital SNHL; delayed/progressive/fluctuating hearing loss; PCR before day 21; hearing rehabilitation",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — pediatric hearing-loss evaluation; CMV PCR from urine/saliva before 3 weeks; progressive cCMV hearing loss",
            "CDC Congenital CMV clinical/laboratory guidance, 2024-current — saliva PCR with urine confirmation within 2-3 weeks; serology does not diagnose congenital infection; serial hearing follow-up",
            "Kimberlin et al. congenital CMV antiviral evidence — valganciclovir for selected symptomatic congenital disease with toxicity monitoring",
            "Kimberlin et al., J Pediatr 2024 — valganciclovir started beyond 1 month did not improve cCMV-associated SNHL in a randomized trial",
        ],
    },
    "congenital hearing loss genetics": {
        "recognize": (
            "Use this card for the MOLECULAR ETIOLOGY pathway once congenital/early-onset hearing loss is confirmed. Genetic hearing loss may be syndromic or nonsyndromic, recessive, dominant, X-linked, mitochondrial, de novo, or variably penetrant; the absence of affected parents does not make a genetic cause unlikely. Pattern the phenotype before ordering tests: congenital versus delayed/progressive, unilateral versus bilateral, severity/configuration, vestibular symptoms, family history/consanguinity, pigmentation, vision, renal/branchial, thyroid, cardiac, craniofacial, neurologic and skeletal findings."
        ),
        "localize": (
            "Localize the PHENOTYPE TO A GENE/SYNDROME FAMILY rather than memorizing a disconnected gene list. GJB2/GJB6-related DFNB1 is a classic nonsyndromic autosomal-recessive cause; SLC26A4 can produce Pendred/DFNB4 with enlarged vestibular aqueduct; Usher couples hearing loss with retinal disease +/- vestibular dysfunction; branchio-oto-renal syndromes link ear/branchial findings with renal disease; Jervell-Lange-Nielsen links congenital severe SNHL with long-QT risk; mitochondrial variants can confer aminoglycoside susceptibility. Imaging anatomy such as EVA or cochlear malformation can therefore sharpen—not replace—the genetic differential."
        ),
        "workup": (
            "After diagnostic audiology, obtain a three-generation family history and syndrome-directed examination, then use contemporary comprehensive genetic testing rather than reflexively stopping after a single connexin assay. ACMG's etiologic-evaluation framework supports genetic evaluation because a molecular diagnosis can change prognosis, recurrence counseling, surveillance for extra-auditory disease, and management. A broad hearing-loss panel with copy-number and relevant mitochondrial analysis is often higher-yield than serial single-gene testing; targeted testing is reasonable when the phenotype strongly points to one diagnosis. Order ECG, ophthalmology, renal studies, thyroid assessment, or other tests when the phenotype/gene result makes them actionable rather than as an indiscriminate laboratory battery. In a neonate, do not let genetic testing delay time-sensitive cCMV testing."
        ),
        "manage": (
            "A genetic diagnosis is clinically useful only if it CHANGES COUNSELING OR CARE. Explain inheritance and recurrence risk with genetics professionals; identify relatives who need testing or audiology; anticipate progression and vestibular risk; institute syndrome-specific surveillance (for example retinal, renal, thyroid, or cardiac evaluation when indicated); and avoid preventable exposures when a genotype creates susceptibility. Do not promise auditory outcome from genotype alone—hearing phenotype and progression can vary even within families. Continue standard early hearing intervention in parallel with etiologic testing; children should not wait for a molecular answer before receiving amplification, language access, educational support, or CI evaluation."
        ),
        "operate": (
            "For cochlear implantation, the genetic result can refine EXPECTATIONS and associated-risk planning but rarely replaces audiologic candidacy. Some cochlear-limited genetic causes have favorable CI performance because the auditory nerve and central pathways are preserved, whereas syndromes with neuropathy, major neurodevelopmental disease, cochlear nerve deficiency, or complex malformation require individualized counseling and surgical planning. Use CT/MRI when anatomy or CI planning requires it. A gene result does not justify prophylactic ear surgery and does not eliminate the need to evaluate an unexpected asymmetric/progressive course for acquired causes such as cCMV."
        ),
        "teach": (
            "Chief/boards discriminator: GENETIC CONGENITAL HEARING LOSS = PHENOTYPE -> PEDIGREE -> MOLECULAR DIAGNOSIS -> ACTIONABLE SYNDROME/RECURRENCE COUNSELING. GJB2 is important but 'Connexin 26 negative' is not the endpoint of modern evaluation. Use multigene testing when appropriate and chase extra-auditory findings selectively. Most importantly, etiologies are not mutually exclusive: a child can have cCMV plus a genetic contributor, so a discordant course deserves reconsideration rather than diagnostic anchoring."
        ),
        "tags": ["congenital hearing loss genetics", "GJB2", "GJB6", "SLC26A4", "Pendred", "Usher", "branchio-oto-renal", "Jervell Lange-Nielsen", "hearing loss panel", "genetic counseling", "ACMG"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — hereditary hearing loss, syndromic/nonsyndromic etiologies, pediatric diagnostic evaluation, and cochlear implantation",
            "K.J. Lee's Essential Otolaryngology, 12e — congenital hearing-loss genetics; GJB2/GJB6 and next-generation sequencing; syndrome-directed evaluation and counseling",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — hereditary versus acquired congenital hearing loss; GJB2/GJB6, Pendred, Usher, BOR and long-QT patterns; increasing role of multigene testing",
            "Li et al. ACMG Clinical Practice Resource, Genetics in Medicine 2022 — clinical and etiologic genetic evaluation of deaf and hard-of-hearing individuals",
            "Joint Committee on Infant Hearing 2019 position statement — timely diagnosis/intervention and medical/etiologic evaluation after confirmed infant hearing loss",
        ],
    },
}


def apply_congenital_hearing_rebuild_v331(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            payload = CONGENITAL_HEARING_REBUILD_V331.get(_norm(module.get("topic")))
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v331"] = True
            module["semantic_role_v331"] = (
                "time-critical congenital CMV confirmation, longitudinal hearing surveillance, antiviral nuance, and rehabilitation"
                if _norm(module.get("topic")) == "congenital cmv hearing loss"
                else "molecular and syndromic etiologic diagnosis, actionable surveillance, family counseling, and gene-informed rehabilitation"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
