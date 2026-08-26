(function(){
  function closeNav(){ document.body.classList.remove('mobile-nav-open'); }
  function toggleNav(){ document.body.classList.toggle('mobile-nav-open'); }
  document.addEventListener('DOMContentLoaded',function(){
    var btn=document.querySelector('[data-mobile-nav-toggle]');
    var backdrop=document.querySelector('[data-mobile-nav-backdrop]');
    if(btn) btn.addEventListener('click',toggleNav);
    if(backdrop) backdrop.addEventListener('click',closeNav);
    document.querySelectorAll('.modern-sidebar a').forEach(function(a){a.addEventListener('click',closeNav)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape') closeNav();});
  });
})();
