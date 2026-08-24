document.addEventListener("keydown", e => {
  if (e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") {
    e.preventDefault(); const el=document.querySelector(".global-search input"); if(el) el.focus();
  }
});
document.querySelectorAll(".reveal-btn").forEach(b=>b.addEventListener("click",()=>{b.nextElementSibling.classList.remove("hidden");b.style.display="none";}));


// Otoscopy Interpretation Lab
(()=>{const deck=document.querySelector('[data-oto-deck]');if(!deck)return;const cards=[...deck.querySelectorAll('[data-oto-case]')];let idx=0;function show(n){if(!cards.length)return;idx=(n+cards.length)%cards.length;cards.forEach((c,i)=>c.classList.toggle('hidden',i!==idx));cards[idx].scrollIntoView({behavior:'smooth',block:'start'});}cards.forEach((card,i)=>{const reveal=card.querySelector('.oto-reveal'),ans=card.querySelector('.oto-answer');if(reveal)reveal.addEventListener('click',()=>{ans.classList.remove('hidden');reveal.disabled=true;reveal.textContent='Answer revealed';});card.querySelector('.oto-next')?.addEventListener('click',()=>show(i+1));card.querySelector('.oto-prev')?.addEventListener('click',()=>show(i-1));});})();


// Adaptive Interpretation Lab stage navigation, reveal, and self-rating
window.addEventListener('click', async (e) => {
  const tab=e.target.closest('.interp-stage-tab');
  if(tab){
    const card=tab.closest('.interp-case');
    if(!card) return;
    const stageName=tab.dataset.stage;
    card.querySelectorAll('.interp-stage-tab').forEach(x=>x.classList.toggle('active',x===tab));
    card.querySelectorAll('.interp-stage').forEach(panel=>panel.classList.toggle('active',panel.dataset.stagePanel===stageName));
    return;
  }

  const reveal=e.target.closest('.stage-reveal-btn');
  if(reveal){
    const stage=reveal.closest('.interp-stage');
    if(!stage) return;
    stage.querySelector('.stage-reveal-content')?.classList.remove('hidden');
    reveal.disabled=true;
    reveal.hidden=true;
    return;
  }

  const b=e.target.closest('.lab-self-rate button');
  if(!b) return;
  const card=b.closest('.interp-case');
  if(!card) return;
  b.parentElement.querySelectorAll('button').forEach(x=>x.disabled=true);
  try{
    const r=await fetch('/api/lab-rate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({
      lab_slug:card.dataset.lab, case_id:card.dataset.caseId, concept_id:card.dataset.conceptId,
      rating:Number(b.dataset.rating), variant_type:card.dataset.variantType, domain:card.dataset.domain
    })});
    if(!r.ok) throw new Error('save failed');
    b.parentElement.classList.add('rated');
    b.parentElement.querySelector('span').textContent='Saved — this will change when the concept returns.';
    b.classList.add('selected-rating');
  }catch(err){
    b.parentElement.querySelectorAll('button').forEach(x=>x.disabled=false);
    b.parentElement.querySelector('span').textContent='Could not save rating — try again.';
  }
});

document.addEventListener('click', async (e) => {
  const reveal=e.target.closest('.reveal-stage');
  if(reveal){const stage=reveal.closest('.progressive-stage');stage.querySelector('.stage-answer')?.classList.remove('hidden');reveal.disabled=true;return;}
  const next=e.target.closest('.next-stage');
  if(next){const stage=next.closest('.progressive-stage');const nxt=stage.nextElementSibling;if(nxt&&nxt.classList.contains('progressive-stage')){nxt.classList.remove('stage-locked');nxt.scrollIntoView({behavior:'smooth',block:'start'});}return;}
  const rate=e.target.closest('.demonstrated-rating button[data-score]');
  if(rate){const stage=rate.closest('.progressive-stage');const shell=stage.closest('.progressive-case');const score=Number(rate.dataset.score);rate.parentElement.querySelectorAll('button').forEach(x=>x.disabled=true);if(score<=1)stage.querySelector('.miss-classifier')?.classList.remove('hidden');try{const r=await fetch('/api/mastery-event',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({concept_id:shell.dataset.conceptId,domain:shell.dataset.domain,dimension:stage.dataset.dimension,score:score,source_type:'integrated_case',source_id:shell.dataset.caseId+':'+stage.dataset.stage})});if(!r.ok)throw new Error();rate.classList.add('selected-rating');}catch(err){rate.parentElement.querySelectorAll('button').forEach(x=>x.disabled=false);}return;}
  const miss=e.target.closest('.miss-classifier button[data-miss]');
  if(miss){const stage=miss.closest('.progressive-stage');const shell=stage.closest('.progressive-case');try{await fetch('/api/mastery-miss',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({concept_id:shell.dataset.conceptId,domain:shell.dataset.domain,dimension:stage.dataset.dimension,miss_type:miss.dataset.miss,source_type:'integrated_case',source_id:shell.dataset.caseId+':'+stage.dataset.stage})});miss.parentElement.querySelectorAll('button').forEach(x=>x.disabled=true);miss.classList.add('selected-rating');}catch(err){}return;}
  const ar=e.target.closest('button[data-attending-score]');
  if(ar){const card=ar.closest('.attending-card');if(!card)return;ar.parentElement.querySelectorAll('button').forEach(x=>x.disabled=true);try{const r=await fetch('/api/mastery-event',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({concept_id:card.dataset.conceptId,domain:card.dataset.domain,dimension:'reasoning',score:Number(ar.dataset.attendingScore),source_type:'attending_mode',source_id:location.search||'resident'})});if(!r.ok)throw new Error();ar.classList.add('selected-rating');}catch(err){ar.parentElement.querySelectorAll('button').forEach(x=>x.disabled=false);}}
});
