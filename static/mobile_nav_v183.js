(function(){
  function closeNav(){ document.body.classList.remove('mobile-nav-open'); }
  function openNav(){ document.body.classList.add('mobile-nav-open'); }
  document.addEventListener('DOMContentLoaded',function(){
    var btn=document.querySelector('[data-mobile-nav-toggle]');
    var backdrop=document.querySelector('[data-mobile-nav-backdrop]');
    var close=document.querySelector('[data-mobile-nav-close]');
    var panel=document.querySelector('[data-mobile-nav-panel]');
    if(btn) btn.addEventListener('click',openNav);
    if(backdrop) backdrop.addEventListener('click',closeNav);
    if(close) close.addEventListener('click',closeNav);
    if(panel) panel.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeNav)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape') closeNav();});
    window.addEventListener('resize',function(){if(window.innerWidth>900) closeNav();});
  });
})();
