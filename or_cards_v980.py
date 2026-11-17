"""v98.0: OR Tomorrow card for active transcutaneous bone-conduction implant (Cochlear Osia).

The site had no card for bone-conduction implant surgery. Technique follows the manufacturer's
OSI300 Physician's Guide (in our own words) and the FDA 510(k) indications; linked to the
Hearing Aids and Bone-Conduction Devices topic. Installed before or_merge_v610.
"""

SLUG = "osia-implant"
TOPIC = "Hearing Aids and Bone-Conduction Devices"
SOURCE_LABEL = "the Cochlear Osia OSI300 Implant Physician's Guide and FDA 510(k) indications"

VIDEOS = [
    {"url": "https://vimeo.com/911602115",
     "label": "Cochlear Osia OSI300 implant surgical video, step by step (narrated, Cochlear Americas)"},
]

STEPS = [
    ["Mark the implant position",
     "With the processor template on the skin, mark the actuator in line with or slightly above the ear canal, "
     "close to the canal for better sound transfer but clear of the pinna, with the coil behind it as close to a "
     "straight line as possible (deviation no more than about 45 degrees). Keep any other implant coil at least "
     "10 cm away."],
    ["Measure soft-tissue thickness",
     "Measure flap thickness at several points over the planned coil without compressing the tissue. The distance "
     "from processor to implant should be 9 mm or less for a reliable magnetic and radiofrequency link; plan to thin "
     "the flap or move the coil if it is thicker, and avoid making the skin so thin it breaks down."],
    ["Incision",
     "Use a postauricular incision with a superior or inferior extension, a posterior C-shaped incision, or an "
     "inverted U, placed at least 15 mm from the edge of the actuator so the scar never lies over the device. Infiltrate "
     "with local anesthetic and epinephrine; use bipolar cautery only."],
    ["Raise the flap and make the pocket",
     "Elevate the skin flap, then either incise the periosteum for a snug subperiosteal pocket or stay superficial "
     "to it for a lateral pocket over periosteum or muscle. Offset the skin and periosteal incisions to reduce "
     "breakdown risk, and create the coil pocket by blunt dissection, checking its size and the actuator site with "
     "the template."],
    ["Thin the flap if needed",
     "If the measured tissue over the coil exceeds about 9 mm, carefully thin the subcutaneous tissue under the flap, "
     "preserving the hair follicles and dermal blood supply. Recheck thickness before placing the coil."],
    ["Prepare the fixture site",
     "At the actuator center, clear periosteum with a small cruciate incision and smooth any irregular bone. "
     "Drill perpendicular to the bone at about 2000 rpm with constant irrigation using the guide drill with its "
     "3-mm spacer, checking the floor of the hole for dura or sigmoid sinus. If the bone is thick enough, remove the "
     "spacer and deepen to 4 mm."],
    ["Widen and countersink",
     "Use the matching widening drill at the same speed and angle with irrigation, keeping the countersink shallow "
     "and never enlarging the hole beyond the drill size. A wobbling or oversized hole risks a loose fixture and "
     "failed osseointegration."],
    ["Insert the BI300 fixture",
     "Insert the titanium fixture with the inserter at low speed, dry for the first two turns and then with "
     "irrigation, keeping it perpendicular. Set insertion torque to about 40 to 50 Ncm in compact bone and 20 to 30 "
     "Ncm in soft or thin bone (often the case in children). If it fails to seat, back out one thread and retry; after a second failure, "
     "choose a new site and seal the unused hole."],
    ["Clear the bone bed",
     "Screw the 17-mm bone bed indicator onto the fixture by hand and turn it clockwise; wherever it catches, remove "
     "periosteum and then bone with a burr until it rotates a full 360 degrees freely. Only the fixture may touch "
     "bone: an actuator resting on bone misaligns the screw, damages the fixture threads and degrades the "
     "transmitted vibration."],
    ["Attach the actuator",
     "Preload the fixation screw into the actuator, center the actuator over the fixture until the screw drops into "
     "the fixture, hand-start it, and tighten to 25 Ncm with the torque wrench. Lay the coil into its pocket without "
     "kinking or overbending the lead, and keep sharp instruments away from the silicone."],
    ["Confirm the device",
     "Hold the sound processor or a coil over the skin to confirm that it couples with the implant and identifies "
     "it correctly, and confirm that the magnet retains the processor through the flap. Correct coil depth or "
     "position now rather than after the wound heals."],
    ["Close",
     "Close in two layers where possible, offsetting the periosteal and skin suture lines so neither lies over the "
     "device, then apply a pressure dressing for at least 24 hours to prevent a hematoma under the flap."],
    ["Activation and follow-up",
     "Fit the processor only after the wound has healed, about 4 weeks after surgery (later if the flap is still "
     "swollen). Teach the patient to check the skin under the processor and to report redness, pain or loss of "
     "retention early."],
]

CARD_V980 = {
    "title": "Active Transcutaneous Bone-Conduction Implant (Cochlear Osia)",
    "domain": "Otology",
    "linked_topic": TOPIC,
    "or_family_v190": "otology",
    "indications": (
        "Patients 5 years or older (FDA, 2024) with conductive or mixed hearing loss whose bone-conduction pure-tone "
        "average (0.5, 1, 2 and 3 kHz) is 55 dB HL or better (up to 65 dB HL with the newest Osia 3 processor), or "
        "single-sided sensorineural deafness with a pure-tone average of 20 dB HL or better in the hearing ear. Typical "
        "candidates have aural atresia or microtia, chronic ear disease or a mastoid cavity that cannot use a hearing "
        "aid, failed middle-ear reconstruction, or single-sided deafness, and have tried a conventional or "
        "bone-conduction hearing aid or a softband trial first. Bilateral fitting needs symmetric bone conduction "
        "(less than 10 dB difference on average). The active transcutaneous design keeps the skin intact, avoiding the "
        "abutment care and skin reactions of percutaneous devices, but needs enough bone and an appropriate flap thickness."
    ),
    "setup": [
        "Confirm candidacy: bone-conduction thresholds within the device range, the expected benefit on a softband "
        "or headband trial, the side to implant, and in single-sided deafness, normal hearing in the better ear.",
        "Review a temporal bone CT when bone thickness is in doubt (children, atresia, prior mastoid surgery or "
        "irradiated bone) to plan the fixture site away from the sigmoid sinus, dura and any mastoid cavity.",
        "Discuss MRI: the implant is MR conditional. Scans at 1.5 T can be done with the magnet in place using the "
        "manufacturer's MRI kit, while 3 T requires surgical removal of the magnet cassette and replacement with a "
        "nonmagnetic insert; expect an image artifact around the device.",
        "Coordinate with any planned atresia or microtia reconstruction: placing the coil where it will not "
        "interfere with the reconstructed ear or future rib-graft flaps, and accepting a higher infection risk if both "
        "are done together.",
        "Set up bipolar cautery only, the device template, the drill system with guide and widening drills, the "
        "torque-limited inserter and wrench, the bone bed indicator, and the implant kept sterile until needed.",
    ],
    "landmarks": [
        "External auditory canal and pinna",
        "Temporal line and mastoid tip",
        "Sigmoid sinus and posterior fossa dura",
        "Middle fossa dura (tegmen)",
        "Planned coil site behind and above the ear",
        "Flap thickness over the coil",
    ],
    "danger": [
        "Sigmoid sinus or dura breach while drilling",
        "Thin flap leading to skin breakdown or extrusion",
        "Thick flap causing poor retention or link",
        "Actuator touching bone",
        "Subcutaneous hematoma under the flap",
        "Monopolar cautery near the implant",
    ],
    "exit_check": [
        "Fixture seated perpendicular at the intended torque, bone bed cleared so the actuator touches only the "
        "fixture, actuator tightened to 25 Ncm, and coil lying flat without kinks.",
        "Processor couples and identifies the implant through the closed flap, incisions are offset from the device, "
        "and a pressure dressing is in place.",
    ],
    "postop": [
        "Pressure dressing for at least 24 hours, then a standard dressing; check for hematoma, seroma and early wound "
        "separation at the first visit.",
        "Do not wear the processor until the wound has healed, usually about 4 weeks; fitting and programming are done "
        "by audiology.",
        "Teach skin checks under the magnet; persistent redness or pain suggests too strong a magnet or a thin flap and "
        "should prompt a weaker magnet or a review before the skin breaks down.",
        "Give the patient the device card with its MRI conditions; no monopolar cautery on the head or neck, and no "
        "therapeutic diathermy or ultrasound over the implant in future procedures.",
    ],
    "complications": {
        "early": [
            "Subcutaneous hematoma or seroma under the flap.",
            "Wound infection or dehiscence.",
            "CSF leak or dural injury from drilling.",
            "Numbness of the skin around the incision.",
        ],
        "late": [
            "Skin irritation, breakdown or device extrusion, especially with a thin flap or strong magnet.",
            "Poor processor retention or weak sound with a thick flap.",
            "Failed osseointegration of the fixture.",
            "Device failure (no, intermittent or uncomfortably loud sound) needing replacement.",
        ],
    },
    "attending_followup": [
        ["How does an active transcutaneous device differ from a percutaneous or passive transcutaneous bone-conduction device?",
         "A percutaneous device (abutment through the skin) transmits vibration best but needs daily skin care and causes skin "
         "reactions and soft-tissue overgrowth. A passive transcutaneous device (magnet under intact skin, vibrator outside) "
         "is cosmetically better but loses high-frequency gain through the skin. An active transcutaneous device such as "
         "Osia puts the piezoelectric actuator under intact skin, fixed to bone, so it avoids the abutment and the skin "
         "attenuation, at the cost of more surgery and an MRI-conditional magnet."],
        ["Why must only the fixture touch bone?",
         "The actuator vibrates the bone through the fixture. If the actuator rests on bone, the fixation screw seats at "
         "an angle, the fixture threads can be damaged, and vibration transfer becomes unpredictable. The bone bed "
         "indicator is turned a full circle to confirm clearance."],
        ["What flap thickness do you want over the coil, and why?",
         "About 9 mm or less between processor and implant. Thicker tissue weakens magnetic retention and the radiofrequency "
         "link; tissue that is too thin risks pressure necrosis and extrusion. Thin a thick flap but preserve its blood supply."],
        ["Who is a candidate with single-sided deafness?",
         "A patient with severe-to-profound loss in one ear and a pure-tone average of 20 dB HL or better in the other. The "
         "device routes sound from the deaf side to the hearing cochlea by bone conduction; it does not restore hearing in the "
         "deaf ear or true binaural hearing, which a cochlear implant may offer instead."],
        ["Your patient needs a 3-T MRI of the brain. What do you do?",
         "At 3 T the magnet cassette must be removed through a small incision under sterile conditions and replaced with a "
         "nonmagnetic insert, then reinserted afterward. At 1.5 T the scan can be done with the magnet in place using the "
         "manufacturer's MRI kit. External parts are never taken into the scanner, and an artifact around the device is expected."],
    ],
    "source_basis": [
        "Cochlear Osia OSI300 Implant Physician's Guide (Cochlear Ltd).",
        "FDA 510(k) K220922 and K240155: Cochlear Osia 2 System indications (12 years and older, extended to 5 years and older in 2024).",
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — implantable hearing devices and bone-conduction implants.",
    ],
}


def install_or_cards_v980(data, app_mod):
    import textbook_curriculum_v470
    registry = data.OR_PREP_REGISTRY
    if SLUG not in registry:
        c = {k: (list(v) if isinstance(v, list) else dict(v) if isinstance(v, dict) else v) for k, v in CARD_V980.items()}
        c["attending_followup"] = [list(p) for p in CARD_V980["attending_followup"]]
        c["complications"] = {k: list(v) for k, v in CARD_V980["complications"].items()}
        c["steps_v840"] = [list(s) for s in STEPS]
        c["steps"] = [f"{t}. {d}" for t, d in STEPS]
        c["steps_source_v840"] = SOURCE_LABEL[0].upper() + SOURCE_LABEL[1:]
        c["video_links_v980"] = [dict(v) for v in VIDEOS]
        c.update({"slug": SLUG, "status": "authored-v98.0", "review_status_v190": "operative-depth reviewed",
                  "sequence_status_v200": "procedure-specific", "sources": list(CARD_V980["source_basis"])})
        registry[SLUG] = c
    m = textbook_curriculum_v470.TOPIC_OR_MAP_V470.setdefault(TOPIC, [])
    if SLUG not in m:
        m.insert(0, SLUG)
    if getattr(app_mod, "OR_PREP_REGISTRY", None) is not registry:
        app_mod.OR_PREP_REGISTRY = registry
    return {"added": [SLUG]}
