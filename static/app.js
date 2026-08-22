document.addEventListener("keydown", e => {
  if (e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") {
    e.preventDefault(); const el=document.querySelector(".global-search input"); if(el) el.focus();
  }
});
document.querySelectorAll(".question").forEach(card=>{
  let confidence=3, locked=false;
  card.querySelectorAll("[data-conf]").forEach(b=>b.addEventListener("click",()=>{
    card.querySelectorAll("[data-conf]").forEach(x=>x.classList.remove("selected")); b.classList.add("selected"); confidence=Number(b.dataset.conf);
  }));
  card.querySelectorAll(".choice").forEach(btn=>btn.addEventListener("click",async()=>{
    if(locked) return; locked=true;
    const choice=Number(btn.dataset.choice);
    const res=await fetch("/api/answer",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({question_id:card.dataset.qid,choice,confidence})});
    const d=await res.json();
    card.querySelectorAll(".choice").forEach((x,i)=>{x.disabled=true;if(i===d.answer)x.classList.add("correct");});
    if(!d.correct){btn.classList.add("wrong");card.querySelector(".miss-panel").classList.remove("hidden");}
    const panel=card.querySelector(".answer-panel"); panel.classList.remove("hidden");
    panel.innerHTML=`
      <div class="answer-verdict"><b>${d.correct?"✓ Correct":"Not quite"}</b><p>${d.explanation}</p></div>
      ${d.why_it_matters ? `<div class="reason-layer"><span class="reason-label">WHY DOES THIS MATTER?</span><p>${d.why_it_matters}</p></div>` : ""}
      ${d.what_to_look_for ? `<div class="reason-layer"><span class="reason-label">WHAT AM I LOOKING FOR?</span><p>${d.what_to_look_for}</p></div>` : ""}
      ${d.management_change ? `<div class="reason-layer"><span class="reason-label">HOW DOES IT CHANGE MANAGEMENT?</span><p>${d.management_change}</p></div>` : ""}
      ${d.board_pearl ? `<div class="reason-pearl"><b>Board / OR pearl</b><p>${d.board_pearl}</p></div>` : ""}
      ${d.attending_followup ? `<div class="followup-box"><span class="reason-label">ATTENDING FOLLOW-UP</span><h4>${d.attending_followup}</h4><p>Answer this aloud before moving to the next question.</p></div>` : ""}
    `;
  }));
  card.querySelectorAll("[data-miss]").forEach(btn=>btn.addEventListener("click",async()=>{
    await fetch("/api/classify-miss",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({question_id:card.dataset.qid,miss_type:btn.dataset.miss})});
    card.querySelectorAll("[data-miss]").forEach(x=>x.classList.remove("selected"));btn.classList.add("selected");
  }));
});
document.querySelectorAll(".reveal-btn").forEach(b=>b.addEventListener("click",()=>{b.nextElementSibling.classList.remove("hidden");b.style.display="none";}));


// Otoscopy Interpretation Lab
(()=>{const deck=document.querySelector('[data-oto-deck]');if(!deck)return;const cards=[...deck.querySelectorAll('[data-oto-case]')];let idx=0;function show(n){if(!cards.length)return;idx=(n+cards.length)%cards.length;cards.forEach((c,i)=>c.classList.toggle('hidden',i!==idx));cards[idx].scrollIntoView({behavior:'smooth',block:'start'});}cards.forEach((card,i)=>{const reveal=card.querySelector('.oto-reveal'),ans=card.querySelector('.oto-answer');if(reveal)reveal.addEventListener('click',()=>{ans.classList.remove('hidden');reveal.disabled=true;reveal.textContent='Answer revealed';});card.querySelector('.oto-next')?.addEventListener('click',()=>show(i+1));card.querySelector('.oto-prev')?.addEventListener('click',()=>show(i-1));});})();
