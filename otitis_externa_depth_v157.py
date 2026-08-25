"""v15.7 — Acute otitis externa depth enrichment.

Keeps the existing canonical Acute Otitis Externa topic intact while enriching
its deep-curriculum teaching with the clinically important spectrum:
furunculosis (focal/circumscribed OE), otomycosis, necrotizing/malignant OE,
and the distinction between NOE and skull-base osteomyelitis (SBO).

This is intentionally an in-place curriculum enrichment rather than a new
canonical topic: these distinctions belong inside the AOE framework.
"""

AOE_TOPIC_CANDIDATES_V157 = (
    "Acute Otitis Externa",
    "Acute Otitis Externa / Furunculosis",
    "Furunculosis / Acute Otitis Externa",
    "Furunculosis with Acute Otitis Externa",
)

AOE_DEPTH_V157 = {
    "recognize": (
        "Acute otitis externa is an inflammatory/infectious process of the external auditory canal, usually presenting with otalgia, canal edema/erythema or debris, and pain with tragal or pinna manipulation. Distinguish diffuse bacterial AOE from focal furunculosis, otomycosis, and necrotizing (malignant) otitis externa. Furunculosis is a localized infection of a hair follicle in the hair-bearing lateral/cartilaginous canal, classically Staphylococcus aureus, producing a focal exquisitely tender pustule or swelling rather than diffuse canal inflammation. Otomycosis more often causes prominent pruritus/fullness with characteristic fungal debris. Necrotizing/malignant OE should be suspected when severe persistent deep otalgia/otorrhea, granulation tissue, treatment failure, or cranial neuropathy occurs in a high-risk host, classically an older patient with diabetes or an immunocompromised patient."
    ),
    "localize": (
        "The lateral cartilaginous EAC contains hair follicles and is therefore where furunculosis occurs; the medial bony canal does not contain hair follicles. Diffuse AOE involves the canal skin more broadly. Necrotizing OE begins as an invasive infection centered on the external canal and can spread through soft-tissue planes and fissures into the temporal bone and skull base. Skull-base osteomyelitis (SBO) describes osteomyelitis of skull-base bone itself: classic/typical SBO commonly represents deep extension of NOE, but SBO is not synonymous with NOE because atypical/central SBO can arise without an external-ear source, including from sinonasal or other deep head-and-neck infection."
    ),
    "workup": (
        "Uncomplicated diffuse AOE and a typical furuncle are usually clinical diagnoses. Clean the canal sufficiently to assess the tympanic membrane when safe and consider a wick when edema prevents topical medication delivery. Otomycosis is suggested by characteristic debris and disproportionate pruritus; microscopy/culture is useful when the diagnosis is uncertain or disease is refractory. For suspected NOE, obtain culture before systemic therapy when feasible, assess inflammatory markers such as ESR/CRP for baseline and follow-up, and use imaging to define soft-tissue and bony extent; CT is useful for cortical/bony change and MRI for marrow, soft-tissue, skull-base, neural, and intracranial extension. Granulation or atypical tissue may require biopsy to exclude malignancy. Perform and document a cranial-nerve examination."
    ),
    "manage": (
        "Diffuse uncomplicated AOE is treated primarily with topical antimicrobial therapy, often combined with a steroid, plus analgesia, canal toilet when needed, water precautions, and a wick when marked edema prevents delivery; systemic antibiotics are not routine unless infection extends beyond the canal or host/disease factors warrant them. Furunculosis is treated as a focal staphylococcal follicular infection with analgesia/warm compresses and drainage and/or systemic anti-staphylococcal therapy when severe or fluctuant. Otomycosis management emphasizes meticulous debridement/aural toilet, keeping the canal dry, and topical antifungal or acidifying therapy as appropriate rather than simply escalating antibacterial drops. Suspected NOE requires urgent specialist evaluation, culture-directed systemic antipseudomonal therapy in the classic bacterial phenotype, control of predisposing factors, serial clinical/cranial-nerve assessment, and follow-up guided by symptoms, inflammatory markers, and imaging when appropriate."
    ),
    "operate": (
        "Routine diffuse AOE is not a surgical disease beyond canal toilet or wick placement, and a mature focal furuncle may require incision/drainage. NOE is primarily treated medically; extensive debridement is not the default operation for skull-base infection. Surgery is reserved for selected needs such as obtaining diagnostic tissue, draining a discrete abscess, removing clearly devitalized tissue, or addressing a complication. New facial or lower-cranial-nerve deficits, intracranial extension, or progressive skull-base disease indicate advanced infection and should trigger escalation rather than routine outpatient OE management."
    ),
    "teach": (
        "Think of external-canal infection as a spectrum, but keep the anatomic labels precise: focal lateral-canal follicle = furunculosis; diffuse inflamed canal = ordinary AOE; fungal debris/pruritus = otomycosis; persistent invasive EAC infection in a high-risk host = necrotizing/malignant OE. NOE can progress to temporal-bone/skull-base osteomyelitis, but NOE and SBO are not interchangeable terms: NOE names the invasive external-ear clinical syndrome, whereas SBO names bone infection and can occur without an external-ear source. The key clinical pivot is failure of apparently routine OE to behave routinely."
    ),
    "tags": [
        "acute otitis externa", "furunculosis", "otomycosis",
        "necrotizing otitis externa", "malignant otitis externa",
        "skull base osteomyelitis", "cranial neuropathy", "diabetes"
    ],
}


def apply_aoe_depth_v157(deep_modules):
    """Enrich AOE, then run the focused v15.8/v16.x curriculum enrichments.

    The existing production integration already calls this function early in
    startup, so chaining later in-place curriculum enrichments here avoids
    another fragile entrypoint dependency. v15.8 remains strict for known
    Otology targets; the cross-domain passes are conservative and report
    unmatched titles rather than taking down the application.
    """
    domain = "Otology / Neurotology"
    modules = deep_modules.get(domain, [])
    for module in modules:
        if module.get("topic") in AOE_TOPIC_CANDIDATES_V157:
            module.update(AOE_DEPTH_V157)
            from otology_depth_v158 import apply_otology_depth_v158
            apply_otology_depth_v158(deep_modules)
            from deep_curriculum_v160 import apply_cross_domain_depth_v160
            apply_cross_domain_depth_v160(deep_modules)
            from deep_curriculum_v161 import apply_cross_domain_depth_v161
            apply_cross_domain_depth_v161(deep_modules)
            return module.get("topic")
    raise RuntimeError(
        "v15.7: could not find the existing Acute Otitis Externa/Furunculosis "
        "module in Otology / Neurotology; refusing to create a duplicate topic"
    )
