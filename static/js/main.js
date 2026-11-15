const burger = document.querySelector('.burger');
const nav = document.getElementById('nav');

if (burger && nav) {
  burger.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });
  nav.addEventListener('click', e => {
    if (e.target.tagName === 'A') {
      nav.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      nav.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });
}

// Scroll-triggered reveals with staggering.
// Motion follows the device setting, but visitors can override it from the
// footer switch (stored in localStorage).
const root = document.documentElement;
const revealItems = document.querySelectorAll('[data-reveal]');
const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
const toggle = document.querySelector('.motion-toggle');
const toggleText = toggle && toggle.querySelector('.motion-text');

let stored = null;
try {
  stored = localStorage.getItem('se-motion');
} catch (err) {
  stored = null;
}
let motionOn = stored ? stored === 'on' : !motionQuery.matches;
let observer = null;

function reflectMotion() {
  root.classList.toggle('motion-off', !motionOn);
  root.classList.toggle('motion-on', motionOn);
  if (!toggle) return;
  toggle.hidden = false;
  toggle.setAttribute('aria-pressed', String(motionOn));
  if (toggleText) toggleText.textContent = motionOn ? 'Motion on' : 'Motion off';
}

function showEverything() {
  revealItems.forEach(item => item.classList.add('is-visible'));
}

function setupReveals() {
  if (observer) {
    observer.disconnect();
    observer = null;
  }
  revealItems.forEach(item => item.classList.remove('is-visible'));

  if (!motionOn || !('IntersectionObserver' in window)) {
    showEverything();
    return;
  }

  observer = new IntersectionObserver((entries, io) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -6% 0px' });

  revealItems.forEach(item => observer.observe(item));
}

reflectMotion();
setupReveals();

if (toggle) {
  toggle.addEventListener('click', () => {
    motionOn = !motionOn;
    try {
      localStorage.setItem('se-motion', motionOn ? 'on' : 'off');
    } catch (err) {
      /* storage can be blocked in private mode */
    }
    reflectMotion();
    setupReveals();
  });
}

if (motionQuery.addEventListener) {
  motionQuery.addEventListener('change', e => {
    if (stored) return; // an explicit choice wins over the device setting
    motionOn = !e.matches;
    reflectMotion();
    setupReveals();
  });
}
