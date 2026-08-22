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
    panel.innerHTML=`<b>${d.correct?"✓ Correct":"Not quite"}</b><p>${d.explanation}</p>`;
  }));
  card.querySelectorAll("[data-miss]").forEach(btn=>btn.addEventListener("click",async()=>{
    await fetch("/api/classify-miss",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({question_id:card.dataset.qid,miss_type:btn.dataset.miss})});
    card.querySelectorAll("[data-miss]").forEach(x=>x.classList.remove("selected"));btn.classList.add("selected");
  }));
});
document.querySelectorAll(".reveal-btn").forEach(b=>b.addEventListener("click",()=>{b.nextElementSibling.classList.remove("hidden");b.style.display="none";}));
