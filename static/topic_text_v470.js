/* v47.0 shared renderer: turns a topic section's prose into short bulleted lines.
   Usage: structureTopicText(rootElement). Any element with class "tt-source"
   (hidden, holding raw text) is expanded into the sibling ul.tt-list. */
(function(){
  var segmenter = ('Segmenter' in Intl) ? new Intl.Segmenter('en', {granularity: 'sentence'}) : null;
  function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  function mdInline(s){return esc(s).replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>');}
  // Keep "**Label.**" pairs in one segment (period read as a sentence boundary).
  function normalizeBoldBoundary(s){return s.replace(/\.(\*\*)(\s|$)/g,'$1.$2');}
  function splitLongClause(piece){
    if(piece.length < 170) return [piece];
    var parts = piece.split(/;\s+/).map(function(p){return p.trim();}).filter(Boolean);
    if(parts.length < 2) return [piece];
    return parts.map(function(p,i){return i < parts.length-1 ? p.replace(/[.;]?$/,';') : p;});
  }
  function sentences(text){
    var out = [];
    text.split(/\n\s*\n/).forEach(function(para){
      para = para.trim(); if(!para) return;
      var segs = segmenter ? Array.from(segmenter.segment(para)).map(function(x){return x.segment.trim();}).filter(Boolean) : [para];
      // Re-join fragments that split inside a bold span.
      var merged = [];
      segs.forEach(function(s){
        var prev = merged.length ? merged[merged.length-1] : null;
        if(prev && ((prev.match(/\*\*/g)||[]).length % 2 === 1)) merged[merged.length-1] = prev + ' ' + s;
        else merged.push(s);
      });
      out = out.concat(merged);
    });
    return out;
  }
  window.structureTopicText = function(root){
    (root || document).querySelectorAll('.tt-source').forEach(function(src){
      if(src.dataset.done) return; src.dataset.done = '1';
      var list = src.nextElementSibling; if(!list || !list.classList.contains('tt-list')) return;
      var text = normalizeBoldBoundary((src.textContent || '').trim()); if(!text) return;
      sentences(text).flatMap(splitLongClause).forEach(function(piece){
        var li = document.createElement('li'); li.innerHTML = mdInline(piece); list.appendChild(li);
      });
    });
  };
  document.addEventListener('DOMContentLoaded', function(){ window.structureTopicText(document); });
})();
