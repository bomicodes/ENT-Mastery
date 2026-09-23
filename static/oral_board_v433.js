(() => {
  const board = document.getElementById('oral-board');
  if (!board) return;
  const steps = Array.from(board.querySelectorAll('.oral-board-step'));
  const pearl = document.getElementById('oral-board-pearl');
  steps.slice(1).forEach(step => { step.hidden = true; });
  if (pearl) pearl.hidden = true;
  steps.forEach((step, index) => {
    const reveal = step.querySelector('.oral-board-reveal');
    if (!reveal) {
      const next = steps[index + 1];
      if (next) next.hidden = false;
      return;
    }
    reveal.addEventListener('toggle', () => {
      if (!reveal.open) return;
      const next = steps[index + 1];
      if (next) next.hidden = false;
      else {
        if (pearl) pearl.hidden = false;
      }
    });
  });
})();
