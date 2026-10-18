/* Scroll effects for the Nateblendz page (English and Spanish).
   Ported from the Farsight landing page's ScrollFx component.
   - Marks [data-reveal] elements with data-in once they scroll into view.
   - Marks the sticky header with data-scrolled after ~24px of scroll.
   All motion lives in the page CSS inside prefers-reduced-motion: no-preference,
   so anyone with reduced motion just sees the finished state. */
(function () {
  var header = document.querySelector('header.top');
  function onScroll() {
    if (header) header.toggleAttribute('data-scrolled', window.scrollY > 24);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  var els = document.querySelectorAll('[data-reveal]');
  if (!('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.setAttribute('data-in', ''); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.setAttribute('data-in', '');
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.15 });
  els.forEach(function (el) { io.observe(el); });
})();
