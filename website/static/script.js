const formTag = document.getElementById('form');
const anotherPredBtn = document.getElementById('anotherpred');
const firstInp = document.getElementById('floatingInput');

formTag.addEventListener('submit', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

anotherPredBtn.addEventListener('click', () => {
  firstInp.focus();
  firstInp.scrollIntoView({ behavior: 'smooth' });
});
