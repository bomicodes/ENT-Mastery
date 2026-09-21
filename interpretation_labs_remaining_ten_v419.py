"""v41.9: add real data and test/report fundamentals to the other ten labs."""
from copy import deepcopy


AE_DATA = {
 "ae1":[["OAE","Present and robust bilaterally"],["ABR","No reproducible waveform through 90 dB nHL clicks"],["Tympanometry","Type A bilateral"],["Reflexes","Absent bilateral"]],
 "ae2":[["Right I/III/V","1.7/4.1/6.3 ms"],["Right I-V","4.6 ms; prolonged for this lab"],["Left I/III/V","1.6/3.7/5.4 ms"],["Left I-V","3.8 ms"],["Interaural I-V difference","0.8 ms; abnormal for this lab"],["Behavioral thresholds","Similar between ears"]],
 "ae3":[["Right tone-burst ABR 500/1k/2k/4k","30 dB nHL each"],["Left tone-burst ABR","35 dB nHL each"],["Important conversion","Apply frequency/transducer/lab correction factors before estimating dB eHL"],["OAE/1-kHz tympanometry","Present; normal bilateral"]],
 "ae4":[["OAE","Absent bilateral"],["Tympanometry","Type B, normal canal volume bilateral"],["Interpretation","Middle-ear dysfunction can cause an OAE refer"],["Diagnostic ABR","Not yet obtained"]],
 "ae6":[["Baseline wave V","6.2 ms; 0.35 µV"],["After maneuver","7.4 ms; 0.15 µV"],["Change","+1.2 ms latency; -57% amplitude"],["Action","Meets this program's alert criteria; pause, troubleshoot, notify surgeon"]],
 "ae7":[["Right screen","Refer on two-stage OAE/AABR protocol"],["Left screen","Pass"],["EHDI benchmark","Screen by 1 month, diagnose by 3 months, intervene by 6 months; programs increasingly target 1-2-3"]],
 "ae8":[["Behavioral thresholds","70-90 dB HL bilateral"],["OAE","Absent bilateral"],["ABR","Elevated threshold with morphology consistent with cochlear loss"],["MRI IAC","Cochlear nerves present, normal caliber"]],
}

ALLERGY_DATA = {
 "allergy1":[["Saline/histamine","0/5 mm wheal"],["Grass/cat/mite","8/4/3 mm"],["Interpretation","Use validated local criteria; commonly ≥3 mm over negative control"]],
 "allergy2":[["Saline control","4 mm: invalid reactive negative control"],["Histamine control","4 mm"],["Allergens","3-5 mm; cannot distinguish from control"],["Likely issue","Dermatographism or placement/reading technique; antihistamine instead causes an inadequate histamine response"]],
 "allergy3":[["Timothy grass IgE","12.5 kUA/L"],["Ragweed","0.9 kUA/L"],["Dust mite","3.2 kUA/L"],["Symptoms","Spring only"],["Interpretation","Sensitization magnitude does not equal clinical allergy; correlate exposure and symptoms"]],
 "allergy4":[["Birch IgE","12 kUA/L"],["Fresh apple prick-to-prick","6 mm"],["Commercial apple extract","Negative"],["Cooked apple","Tolerated"]],
 "allergy5":[["Skin/serum aeroallergen testing","Negative"],["Nasal mite challenge","Sneezing, itching and rhinorrhea in 15-30 minutes"],["Pattern","Local allergic rhinitis after exclusion of alternatives"]],
 "allergy6":[["Prior FEV1","88% predicted"],["Today's peak flow","62% personal best with wheeze"],["SCIT decision","Defer injection; assess and stabilize asthma—do not rely on one universal numeric cutoff"]],
 "allergy7":[["Spirometry","Obstruction with bronchodilator response"],["Sinus CT","Diffuse CRSwNP"],["History","Respiratory reaction 30-180 minutes after COX-1 NSAID"],["Pattern","AERD clinical triad"]],
 "allergy8":[["Cat/spring pollen","Itch and sneeze; allergic pattern"],["Perfume/cold/weather","Congestion without itch; nonallergic pattern"],["Topical decongestant overuse","Rebound; rhinitis medicamentosa"],["Testing","Positive only to cat/tree pollen"]],
}

def case(cid, concept, prompt, answer, why, follow, follow_answer, level=2, study=None):
    out={"id":cid,"level":level,"variant_type":"interpret","concept_id":concept,"prompt":prompt,"answer":answer,"why":why,"follow":follow,"follow_answer":follow_answer}
    if study: out["study_summary"]=study
    return out

NEW = {
 "pathology":[
  case("pathfund1","pathology:frozen","What can frozen section answer, and what belongs on permanent section?","Frozen section can rapidly confirm representative diagnostic tissue and sample an inked margin. Fine nuclear detail, subtle dysplasia, many definitive subtypes, and diagnoses requiring extensive sampling—such as capsular/vascular invasion in follicular thyroid neoplasms—belong on formalin-fixed permanent sections.","Freezing artifact and limited sampling constrain the intraoperative answer.","Why can a negative frozen margin become positive on permanent section?","Only part of the margin is sampled intraoperatively; deeper or broader permanent sampling can find a small focus."),
  case("pathfund2","pathology:ihc","How is an IHC panel built for a poorly differentiated neck mass?","Start with morphology and broad lineage markers such as pancytokeratin, CD45 and SOX10/S100, then add focused markers such as p40, thyroglobulin/TTF-1/PAX8, EBV testing, or p16 plus HPV-specific testing according to site and differential.","Concordant morphology and a marker pattern are safer than a shotgun panel or one positive stain.","Why is one stain insufficient?","Markers can be nonspecific or aberrantly expressed; controls, morphology, site and a coherent panel determine the diagnosis.",3),
  case("pathfund3","pathology:report","How should a surgeon read a final head-and-neck cancer report?","Confirm diagnosis/subtype, size and site-specific staging features, DOI where applicable, margins, PNI/LVI, grade, nodal yield/positive nodes, pathologic ENE, and AJCC pathologic stage; then map findings to re-resection or adjuvant therapy.","This checklist carries the specimen into tumor-board management.","What most strongly triggers postoperative chemoradiation discussion?","Positive margin or pathologically confirmed ENE, balanced against patient fitness and disease context.",3),
  case("pathnew1","pathology:unknown-primary","Interpret this cervical-node IHC panel.","Metastatic squamous carcinoma is supported by keratin and p40. Block-positive p16 raises an HPV-associated oropharyngeal primary, but p16 alone is not a site-independent HPV test; correlate with anatomy and perform recommended HPV-specific testing in an unknown primary.","The result directs a focused oropharyngeal search without pretending one surrogate stain proves the primary site.","Next step?","Complete directed exam and imaging; use HPV-specific testing and institution-appropriate palatine/lingual tonsil evaluation if no primary is seen.",4,[["AE1/AE3","Positive"],["p40","Positive"],["p16",">70% block-positive"],["TTF-1/PAX8/CD45/SOX10","Negative"]]),
 ],
 "ct-mri":[
  case("ctfund1","ct:windowing","What changes between bone and soft-tissue windows?","Window width and level remap fixed HU data: sharp bone reconstructions and wide/high windows show cortex and fine bone; narrower soft-tissue windows show enhancement, fat planes, fluid and nodes.","Both display settings and the underlying reconstruction kernel matter.","Why request a bone reconstruction?","A high-spatial-frequency kernel preserves fine edges that windowing alone cannot recover."),
  case("ctfund2","ct:hu","What are Hounsfield units used for?","HU quantify attenuation relative to water 0 and air -1000. Fat is usually strongly negative, simple fluid near water, soft tissue positive, acute blood higher, and cortex very high; ROI technique and contrast phase matter.","Numbers make tissue characterization reproducible but do not replace morphology.","What distorts a small lesion's HU?","Partial-volume averaging, beam hardening, contrast phase and poorly placed ROIs."),
  case("ctnew1","ct:lipoma","Interpret this neck mass.","A smooth nonenhancing homogeneous -85 HU mass is compatible with simple lipoma.","Objective fat attenuation narrows the diagnosis.","What is worrisome?","Thick/nodular septa, nonfat enhancing components, incomplete fat suppression or infiltrative margins warrant further evaluation.",2,[["Location","Left level II"],["Attenuation","-85 HU"],["Enhancement","None"],["Margins","Smooth"],["Internal soft tissue","None"]]),
 ],
 "laryngeal-endoscopy":[
  case("laryngfund1","larynx:stroboscopy","What does stroboscopy assess?","Using flashes phase-locked near fundamental frequency, report periodicity, closure, amplitude, mucosal wave, phase/vertical-level symmetry and nonvibrating segments. It reconstructs apparent slow motion rather than recording every true cycle.","Severe aperiodicity can make the reconstruction unreliable.","What should happen when vibration is too irregular to synchronize?","State the limitation and use real-time/high-speed imaging when clinically needed."),
  case("laryngfund2","larynx:voice-outcomes","What do GRBAS/CAPE-V and VHI contribute?","GRBAS/CAPE-V structure clinician perceptual ratings; VHI captures patient-reported functional, physical and emotional burden. Interpret alongside acoustic measures, demands and laryngoscopy.","Anatomic appearance and lived disability can diverge.","Why may imaging improve without patient-perceived success?","Voice demands, compensation and psychosocial impact are not fully captured by the image."),
 ],
 "airway-bronchoscopy":[
  case("airwayfund1","airway:myer-cotton","How is Myer–Cotton grade assigned?","Size the stenosis with endotracheal tubes using a standardized leak-pressure method and compare the tube that passes with the age-appropriate reference according to validated Myer–Cotton tables/area estimates. Grades are I 0-50%, II 51-70%, III 71-99%, IV no detectable lumen. Do not square ETT internal-diameter labels as though they were measured airway diameters; tube outer diameter varies by manufacturer.","Standardized sizing avoids visual guessing and incorrect ID-based math.","What else must be documented?","Length, level, circumferential extent, scar maturity, glottic involvement and dynamic disease.",3),
  case("airwayfund2","airway:flex-rigid","When should flexible versus rigid bronchoscopy be used?","Spontaneous-breathing flexible examination best characterizes dynamic collapse and distal airways; rigid bronchoscopy provides ventilation, sizing, large-channel suction, foreign-body retrieval and intervention. Anesthetic depth and positive pressure can alter dynamics.","Tool and ventilation state must match the clinical question.","Why combine them?","Flexible examination maps function/distal disease; rigid examination precisely sizes and treats structural lesions."),
  case("airwaynew1","airway:myer-cotton-worked","Assign the grade from standardized operative sizing.","The stenosis is 56% obstructed using the institution's validated tube outer-diameter/reference-area table, so it is Myer–Cotton Grade II.","The supplied percent comes from validated OD/area data, not the nominal tube ID ratio.","What else changes reconstruction planning?","Stenosis length/location, vocal-fold mobility, posterior glottis, cricoid integrity, tracheomalacia and comorbidity.",3,[["Expected reference tube","4.5 ID; manufacturer OD 6.2 mm"],["Largest tube through stenosis","3.0 ID; manufacturer OD 4.1 mm"],["Standardized leak","Documented at 20 cm H2O"],["Validated table/area estimate","56% obstruction"],["Grade","II (51-70%)"]]),
 ],
 "thyroid-ultrasound":[case("thyfund1","thyroid:tirads","Score this ACR TI-RADS nodule: solid 2, hypoechoic 2, taller-than-wide 3, smooth 0, punctate foci 3. Does 1.2 cm need FNA?","Ten points is TR5. ACR TI-RADS recommends FNA at ≥1.0 cm, so 1.2 cm qualifies.","Feature-by-feature scoring links morphology to size-based action.","What if it is 0.8 cm?","No FNA by ACR TI-RADS; because TR5 is ≥0.5 cm, ultrasound follow-up is recommended, with clinical context superseding the scoring system when appropriate.",3)],
 "temporal-bone-imaging":[case("tbfund1","temporal-bone:protocol","What makes a temporal-bone CT surgically useful?","Use submillimeter acquisition, high-resolution bone reconstruction, small field of view, axial/coronal reformats and targeted obliques. Pöschl is parallel to the superior canal and Stenvers perpendicular. Routine osseous evaluation is usually noncontrast; use contrast for a specific soft-tissue/vascular/infectious question.","A generic head CT cannot reliably resolve ossicles, facial canal or thin canal roofs.","Why use orthogonal superior-canal planes?","They reduce partial-volume false positives and show the canal roof along and across its true axis.")],
 "head-neck-imaging":[case("hnfund1","head-neck:report","What makes a head-and-neck tumor imaging report actionable?","State primary site/epicenter, three-dimensional extent and site-specific staging structures, deep spaces, cartilage/bone, named nerve/perineural pathways, vessel contact angle/narrowing/encasement, nodal levels with suspicious ENE features, and distant/second-primary findings.","The sequence addresses staging, resectability and reconstruction rather than merely naming a mass.","Why quantify vessel contact?","Contact angle, contour change, narrowing and thrombosis communicate risk more reproducibly than vague 'near' or 'encasing' language; thresholds and resectability remain vessel- and center-specific.",3)],
 "sleep":[case("sleepfund1","sleep:montage","Why does PSG need more than oximetry?","EEG/EOG/chin EMG establish sleep stage and arousals; airflow plus thoracoabdominal effort distinguishes obstructive from central events; oximetry measures consequence, while ECG, snoring, position and leg EMG add context.","Both obstructive and central events can desaturate, but require different evaluation and treatment.","Why does EEG staging matter?","Indices use actual sleep time and disease may be REM-predominant; recording time alone can underestimate severity.")],
}

def _backfill(lab, rows, label):
    by={x.get("id"):x for x in lab.get("cases",[])}; fixed=[]
    for cid,data in rows.items():
        if cid not in by: raise RuntimeError("v41.9: missing "+label+" case "+cid)
        if not by[cid].get("study_summary"): by[cid]["study_summary"]=deepcopy(data); fixed.append(cid)
    return fixed

def _append(lab, rows):
    ids={x.get("id") for x in lab.get("cases",[])}; added=[]
    for row in rows:
        if row["id"] not in ids: lab["cases"].append(deepcopy(row)); ids.add(row["id"]); added.append(row["id"])
    return added

def apply_interpretation_labs_remaining_ten_v419(data_module, app_module=None):
    source=getattr(data_module,"INTERPRETATION_LABS",None)
    if not isinstance(source,dict): raise RuntimeError("v41.9: INTERPRETATION_LABS unavailable")
    labs=deepcopy(source)
    ae=labs.get("audiologic-electrophysiology"); allergy=labs.get("allergy-testing")
    if not ae or not allergy: raise RuntimeError("v41.9: required labs unavailable")
    ae_fixed=_backfill(ae,AE_DATA,"audiologic-electrophysiology")
    allergy_fixed=_backfill(allergy,ALLERGY_DATA,"allergy-testing")
    added={}
    for key,rows in NEW.items():
        if key not in labs: raise RuntimeError("v41.9: missing lab "+key)
        added[key]=_append(labs[key],rows)
    data_module.INTERPRETATION_LABS.clear(); data_module.INTERPRETATION_LABS.update(labs)
    if app_module is not None: app_module.INTERPRETATION_LABS=data_module.INTERPRETATION_LABS
    return {"audiologic_electrophysiology_data_fixed":ae_fixed,"allergy_testing_data_fixed":allergy_fixed,"new_cases_added":added}
