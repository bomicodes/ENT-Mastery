"""v41.7: data-driven Audiology/Vestibular labs and testing fundamentals."""
from copy import deepcopy

AUDIO_DATA = {
 "aud1":[["Right AC 250/500/1k/2k/4k/8k","5, 5, 10, 5, 10, 10 dB HL"],["Left AC","10, 5, 5, 10, 5, 15 dB HL"],["BC","≤10 dB HL; no air-bone gap"],["SRT/WRS","5 dB HL bilateral; 100% right, 96% left"],["Tympanometry/reflexes","Type A; reflexes present bilateral"]],
 "aud2":[["Right AC","45, 50, 45, 40, 35, 30 dB HL"],["Right BC","5, 5, 10, 10, 10 dB HL"],["Right air-bone gap","~35-40 dB"],["Left AC=BC","10 dB HL"],["Tympanometry","Type B normal volume right; Type A left"],["WRS","96% right; 100% left"]],
 "aud3":[["Right AC=BC","10, 15, 20, 35, 55, 65 dB HL"],["Left AC=BC","10, 15, 20, 35, 55, 60 dB HL"],["SRT/WRS","20 dB HL; 88% bilateral"],["Tympanometry","Type A bilateral"]],
 "aud4":[["Right AC=BC","10, 10, 15, 20, 25, 30 dB HL"],["Left AC=BC","15, 20, 35, 55, 70, 75 dB HL"],["SRT","10 dB right; 45 dB left"],["WRS","100% right; 60% left (disproportionately poor)"],["Tympanometry","Type A bilateral"]],
}
VEST_DATA = {
 "vest1":[["Right warm/cool SPV","25/20°/s"],["Left warm/cool SPV","10/8°/s"],["Jongkees unilateral weakness","43% left"],["Fixation suppression","Intact"]],
 "vest2":[["Right horizontal gain","0.95; no saccades"],["Left horizontal gain","0.55; overt corrective saccades"],["Vertical canal gains","0.85-0.95 bilateral"],["Reference","Horizontal normal commonly ≥0.8; use device/lab norms"]],
 "vest3":[["Right Dix-Hallpike","Positive after 3-5 seconds"],["Nystagmus","Upbeating right torsional"],["Duration/fatigue","<60 seconds; fatigable"]],
 "vest4":[["Smooth pursuit","Saccadic bilateral"],["Gaze nystagmus","Direction-changing"],["Saccades","Normal velocity/accuracy"],["Spontaneous nystagmus","None"]],
}

def _case(cid, concept, prompt, answer, why, follow, follow_answer, level=2, study=None):
    row={"id":cid,"level":level,"variant_type":"interpret","concept_id":concept,"prompt":prompt,"answer":answer,"why":why,"follow":follow,"follow_answer":follow_answer}
    if study: row["study_summary"]=study
    return row

AUDIO_FUNDAMENTALS = [
 _case("audfund1","audiology:fundamentals-air-conduction","How is pure-tone air-conduction threshold measured?","Present calibrated tones through earphones and bracket down 10/up 5 dB; threshold is the lowest dB HL detected on at least half of ascending trials.","Threshold is a repeatable psychophysical estimate, not a single yes/no presentation.","When is masking needed?","When crossover could let the non-test cochlea respond; masking isolates the test ear."),
 _case("audfund2","audiology:fundamentals-bone-conduction","What does bone conduction test?","A mastoid oscillator largely bypasses outer/middle ear and estimates cochlear sensitivity; because interaural attenuation is near 0 dB, masking is often essential.","Masked AC-versus-BC comparison classifies conductive, sensorineural, or mixed loss.","What is an air-bone gap?","AC poorer than BC beyond test-retest/lab criteria, commonly >10-15 dB at a frequency, indicates a conductive component."),
 _case("audfund3","audiology:fundamentals-speech","Distinguish SRT from word recognition.","SRT is the lowest level for ~50% spondee recognition and should agree with PTA; WRS tests monosyllable understanding at a defined suprathreshold level.","Speech measures check reliability and functional clarity.","What suggests retrocochlear disease?","Disproportionately poor or asymmetric WRS warrants clinical correlation and often MRI rather than amplification alone."),
 _case("audfund4","audiology:fundamentals-tympanometry","Interpret Jerger tympanograms.","A: normal peak; As: shallow/stiff; Ad: hypercompliant; B: flat—use canal volume to separate effusion from perforation/tube; C: negative-pressure peak.","Tympanometry measures mechanics, not hearing, and requires otoscopy/audiometry correlation.","Why report canal volume?","It distinguishes intact-drum effusion from perforation or patent tube in a flat trace."),
 _case("audfund5","audiology:fundamentals-reflexes","What does the acoustic reflex arc test?","It samples cochlea/CN VIII, brainstem crossings, CN VII/stapedius, and middle-ear mobility; interpret ipsi/contra patterns with tympanometry.","Patterns may localize dysfunction but reflex decay is an insensitive historical retrocochlear screen and does not replace MRI.","Why absent in conductive loss?","Sound transmission and measurable compliance change are impaired."),
 _case("audfund6","audiology:fundamentals-oae","What does an OAE measure?","Outer-hair-cell-generated sound returning through a functioning middle ear; it does not directly test inner hair cells, CN VIII, or central pathways.","Present OAEs with abnormal ABR suggests auditory neuropathy spectrum disorder.","Why can effusion cause refer?","It attenuates both stimulus and returning emission."),
 _case("audfund7","audiology:fundamentals-abr","What does ABR measure?","Scalp electrodes record synchronized auditory-nerve/brainstem responses; waves and interpeak timing use age- and lab-specific norms.","ABR estimates thresholds when behavioral testing is unavailable; MRI remains definitive when retrocochlear imaging is indicated.","Why pair ABR with OAE?","Their mismatch distinguishes preserved outer-hair-cell function from impaired neural synchrony."),
 _case("audfund8","audiology:fundamentals-systematic","Give a systematic audiogram read.","Check reliability/SRT-PTA agreement; classify AC/BC type; describe severity/configuration and symmetry; then integrate WRS, tympanometry, reflexes and history.","A fixed sequence prevents pattern-matching errors.","What requires escalation?","Sudden loss, unexplained asymmetry, or disproportionately poor WRS."),
]
VEST_FUNDAMENTALS = [
 _case("vestfund1","vestibular:fundamentals-hit","What does bedside head impulse test assess?","During small unpredictable head turns, corrective saccades indicate deficient VOR on the side of rotation.","In acute vestibular syndrome, abnormal HIT supports peripheral loss; normal HIT may be central.","When is HINTS appropriate?","Only in continuous acute vestibular syndrome with spontaneous nystagmus, performed by a trained examiner—not brief episodic/positional dizziness."),
 _case("vestfund2","vestibular:fundamentals-calorics","What do calorics test?","Warm/cool irrigation tests each horizontal canal at very low frequency; Jongkees asymmetry uses absolute interaural difference divided by total response, with lab cutoff commonly 20-25%.","Calorics uniquely lateralize ears but sample an artificial low frequency.","What is COWS?","Fast phase: cold opposite, warm same."),
 _case("vestfund3","vestibular:fundamentals-vhit","What does vHIT add?","It measures canal-specific eye/head velocity gain and overt/covert saccades at high acceleration; horizontal gain near ≥0.8 is common, but device/lab norms govern.","vHIT and calorics sample different frequencies and may legitimately disagree.","Why test all canals?","It can localize canal or nerve-division deficits."),
 _case("vestfund4","vestibular:fundamentals-vemp","Compare cVEMP and oVEMP.","cVEMP chiefly samples saccule/inferior nerve via SCM; oVEMP chiefly samples utricle/superior nerve via extraocular response.","Enhanced low-threshold responses may indicate a third window; absent responses require age/technique context.","Why use both?","They map different otolith organs and nerve divisions."),
 _case("vestfund5","vestibular:fundamentals-rotary-chair","What does rotary chair add?","It measures bilateral VOR gain/phase/time constant across low-middle frequencies; useful for bilateral hypofunction but weak for side localization.","It bridges caloric and vHIT frequency ranges.","When especially useful?","Suspected bilateral loss or when calorics are infeasible."),
 _case("vestfund6","vestibular:fundamentals-positional","Match positional tests to canals.","Dix-Hallpike tests posterior-canal BPPV; supine roll tests horizontal-canal BPPV. Treat the identified canal with the matching repositioning maneuver.","Typical posterior BPPV is delayed, transient, fatigable torsional-upbeat; horizontal BPPV produces geotropic/apogeotropic horizontal nystagmus.","What suggests a central mimic?","Pure vertical (especially downbeat), persistent/nonfatiguing or canal-incongruent nystagmus, or accompanying neurologic/ocular-motor signs—not horizontal nystagmus by itself."),
 _case("vestfund7","vestibular:fundamentals-bedside","What does subjective visual vertical assess?","It samples utricular/graviceptive function; acute unilateral peripheral loss often tilts toward the affected side. Add head-shake, dynamic visual acuity and gait testing.","Bedside findings build localization but none alone is diagnostic.","Does normal Romberg exclude vestibular disease?","No; unilateral compensated or acute disease may have a near-normal Romberg."),
 _case("vestfund8","vestibular:fundamentals-synthesis","How should a vestibular battery be selected?","Start with history/bedside localization, then use calorics/vHIT for canal function, VEMPs for otolith/third-window questions, rotary chair for bilateral loss, and positional tests for BPPV.","Tests answer different organ/frequency questions; synthesize rather than count abnormalities.","What is a central HINTS result?","In the proper acute-vestibular-syndrome population, any central sign—normal HIT, direction-changing gaze nystagmus, or skew—raises concern and warrants urgent stroke evaluation."),
]
AUDIO_NEW=[
 _case("audnew1","audiology:noise-notch","Interpret this occupational-noise audiogram.","Bilateral symmetric SNHL with a 4-kHz notch and 8-kHz recovery, typical of noise injury.","The corrected data place the nadir at 4 kHz, not 2 kHz.","Best prevention?","Source control and consistently fitted hearing protection.",3,[["Frequencies","250/500/1k/2k/4k/8k Hz"],["Right AC=BC","10, 10, 15, 20, 45, 20 dB HL"],["Left AC=BC","10, 15, 15, 20, 50, 25 dB HL"],["WRS/tympanometry","96% bilateral; Type A bilateral"]]),
 _case("audnew2","audiology:pediatric-ome","Interpret this 4-year-old's testing.","Bilateral mild conductive loss with flat normal-volume tympanograms, consistent with OME.","Persistent hearing difficulty can affect language access.","When offer tubes?","Bilateral OME for ≥3 months with documented hearing difficulty supports offering tubes; individual risks and shared decision-making matter.",2,[["AC","30-35 dB HL bilateral"],["BC","5-10 dB HL"],["Tympanometry","Type B, normal volume bilateral"],["Otoscopy","Dull immobile TMs with fluid"]]),
]
VEST_NEW=[
 _case("vestnew1","vestibular:neuritis","Interpret continuous vertigo without hearing loss.","Severe left unilateral vestibular hypofunction with a peripheral acute HINTS pattern and normal hearing, consistent with vestibular neuritis.","Labs quantify the later deficit; HINTS was performed during the acute symptomatic phase.","Why can symptoms improve despite weakness?","Central compensation is partly independent of peripheral recovery.",4,[["Calorics","~62% left weakness"],["Left vHIT","0.45 with catch-up saccades"],["Audiogram","Normal"],["Acute bedside HINTS","Abnormal left HIT; unidirectional right-beating nystagmus; no skew"]]),
 _case("vestnew2","vestibular:meniere","Interpret 30-60 minute recurrent vertigo with right fluctuating aural symptoms.","Documented fluctuating low-frequency right SNHL plus 20-minute-to-12-hour spontaneous attacks and no better diagnosis meets the clinical pattern for definite Ménière disease.","Electrocochleography may support but is not required; asymmetric SNHL often prompts MRI based on the clinical context.","Why image?","To exclude retrocochlear pathology when asymmetric SNHL warrants it.",4,[["Right AC=BC 250-1k","40, 35, 30 dB HL"],["Right 2k-8k","15, 15, 10 dB HL"],["Calorics","~30% right weakness"],["ECoG","Elevated SP/AP ratio; supportive only"]]),
]

def _data(lab, datasets, prefix, visuals):
    byid={c.get("id"):c for c in lab.get("cases",[])}; fixed=[]
    for base, rows in datasets.items():
        for cid in (base, base+"_reason", base+"_teach"):
            case=byid.get(cid)
            if case is None: raise RuntimeError("v41.7: missing case "+cid)
            if not case.get("study_summary"):
                case["study_summary"]=deepcopy(rows); fixed.append(cid)
                if case.get("visual") in visuals: case.pop("visual",None); case.pop("visual_note",None)
    return fixed

def _add(lab, rows):
    ids={c.get("id") for c in lab.get("cases",[])}; added=[]
    for row in rows:
        if row["id"] not in ids: lab["cases"].append(deepcopy(row)); added.append(row["id"])
    return added

def apply_interpretation_labs_audiology_vestibular_rebuild_v417(data_module, app_module=None):
    source=getattr(data_module,"INTERPRETATION_LABS",None)
    if not isinstance(source,dict): raise RuntimeError("v41.7: INTERPRETATION_LABS unavailable")
    labs=deepcopy(source); aud=labs.get("audiology"); vest=labs.get("vestibular")
    if not aud or not vest: raise RuntimeError("v41.7: missing audiology or vestibular lab")
    af=_data(aud,AUDIO_DATA,"aud",{"lab_assets/audio_normal.svg","lab_assets/audio_conductive.svg","lab_assets/audio_snhl.svg","lab_assets/audio_asym.svg"})
    vf=_data(vest,VEST_DATA,"vest",{"lab_assets/vest_caloric.svg","lab_assets/vest_vhit.svg"})
    out={"audiology_study_data_fixed":af,"vestibular_study_data_fixed":vf,"audiology_fundamentals_added":_add(aud,AUDIO_FUNDAMENTALS),"vestibular_fundamentals_added":_add(vest,VEST_FUNDAMENTALS),"audiology_new_cases_added":_add(aud,AUDIO_NEW),"vestibular_new_cases_added":_add(vest,VEST_NEW)}
    data_module.INTERPRETATION_LABS.clear(); data_module.INTERPRETATION_LABS.update(labs)
    if app_module is not None: app_module.INTERPRETATION_LABS=data_module.INTERPRETATION_LABS
    return out
