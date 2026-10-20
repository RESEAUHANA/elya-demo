/* ELYA — interactions du site de démonstration */
(function () {
  var calm = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Notification de démonstration
  window.demo = function (t) {
    var e = document.getElementById('toast');
    e.textContent = t;
    e.classList.add('show');
    clearTimeout(window._t);
    window._t = setTimeout(function () { e.classList.remove('show'); }, 3200);
  };
  document.querySelectorAll('[data-demo]').forEach(function (a) {
    a.addEventListener('click', function (ev) {
      ev.preventDefault();
      demo(a.getAttribute('data-demo') || 'Fonction disponible dans la version Shopify du site.');
    });
  });

  // En-tête
  var header = document.querySelector('.header');
  addEventListener('scroll', function () { header.classList.toggle('scrolled', scrollY > 10); }, { passive: true });

  // Menu latéral
  var drawer = document.querySelector('.drawer'), overlay = document.querySelector('.overlay');
  function menu(open) {
    drawer.classList.toggle('on', open);
    overlay.classList.toggle('on', open);
    document.body.classList.toggle('lock', open);
    drawer.setAttribute('aria-hidden', open ? 'false' : 'true');
  }
  document.querySelectorAll('[data-menu]').forEach(function (b) {
    b.addEventListener('click', function () { menu(b.getAttribute('data-menu') === 'open'); });
  });
  overlay.addEventListener('click', function () { menu(false); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') menu(false); });

  // Favoris (mémorisés sur l'appareil)
  var favs = [];
  try { favs = JSON.parse(localStorage.getItem('elya-favs') || '[]'); } catch (e) {}
  function syncFavs() {
    document.querySelectorAll('[data-heart]').forEach(function (b) {
      var on = favs.indexOf(b.getAttribute('data-heart')) > -1;
      b.classList.toggle('on', on);
      b.setAttribute('aria-pressed', on);
    });
    var c = document.querySelector('.fav-count');
    if (c) { c.textContent = favs.length; c.classList.toggle('on', favs.length > 0); }
  }
  document.querySelectorAll('[data-heart]').forEach(function (b) {
    b.addEventListener('click', function (ev) {
      ev.preventDefault();
      var h = b.getAttribute('data-heart'), i = favs.indexOf(h);
      if (i > -1) favs.splice(i, 1); else { favs.push(h); demo('Ajouté à tes favoris'); }
      try { localStorage.setItem('elya-favs', JSON.stringify(favs)); } catch (e) {}
      syncFavs();
    });
  });
  syncFavs();

  // Carrousels : points, flèches, indication de glissement
  function setupRail(rail, ui) {
    var items = [].slice.call(rail.children);
    var dots = ui ? ui.querySelector('.dots') : null;
    var prev = ui ? ui.querySelector('[data-prev]') : null, next = ui ? ui.querySelector('[data-next]') : null;
    var count = rail.parentNode.querySelector('.gal-count');
    function pages() {
      var visible = Math.max(1, Math.round(rail.clientWidth / (items[0].getBoundingClientRect().width || 1)));
      return Math.max(1, items.length - visible + 1);
    }
    function current() {
      var w = items[0].getBoundingClientRect().width + parseFloat(getComputedStyle(rail).columnGap || 0);
      return Math.round(rail.scrollLeft / (w || 1));
    }
    function build() {
      if (!dots) return;
      var n = pages();
      dots.innerHTML = '';
      if (ui && !ui.classList.contains('keep')) ui.classList.toggle('hidden', n < 2);
      for (var i = 0; i < n; i++) {
        var d = document.createElement('button');
        d.setAttribute('aria-label', 'Aller à la diapositive ' + (i + 1));
        (function (k) { d.addEventListener('click', function () { items[k].scrollIntoView({ behavior: calm ? 'auto' : 'smooth', block: 'nearest', inline: 'start' }); }); })(i);
        dots.appendChild(d);
      }
      update();
    }
    function update() {
      var c = Math.min(current(), pages() - 1);
      if (dots) [].forEach.call(dots.children, function (d, i) { d.classList.toggle('on', i === c); });
      if (prev) prev.disabled = rail.scrollLeft < 4;
      if (next) next.disabled = rail.scrollLeft + rail.clientWidth >= rail.scrollWidth - 4;
      if (count) count.textContent = (c + 1) + ' / ' + items.length;
    }
    var step = function (dir) { rail.scrollBy({ left: dir * rail.clientWidth * 0.9, behavior: calm ? 'auto' : 'smooth' }); };
    if (prev) prev.addEventListener('click', function () { step(-1); });
    if (next) next.addEventListener('click', function () { step(1); });
    rail.addEventListener('scroll', function () { window.requestAnimationFrame(update); }, { passive: true });
    addEventListener('resize', build);
    build();
    // petit mouvement d'invitation à glisser, une fois, sur mobile
    if (!calm && matchMedia('(max-width: 1024px)').matches && rail.scrollWidth > rail.clientWidth + 10) {
      var io = new IntersectionObserver(function (en) {
        en.forEach(function (x) {
          if (x.isIntersecting) {
            io.disconnect();
            setTimeout(function () { rail.scrollBy({ left: 60, behavior: 'smooth' }); setTimeout(function () { rail.scrollBy({ left: -60, behavior: 'smooth' }); }, 550); }, 500);
          }
        });
      }, { threshold: 0.6 });
      io.observe(rail);
    }
  }
  document.querySelectorAll('[data-rail]').forEach(function (rail) {
    setupRail(rail, rail.parentNode.querySelector('.rail-ui'));
  });
  var gal = document.querySelector('.gallery');
  if (gal) setupRail(gal, document.querySelector('.gallery-wrap'));

  // Choix de taille
  document.querySelectorAll('.chips[data-sizes]').forEach(function (g) {
    g.addEventListener('click', function (e) {
      var b = e.target.closest('.chip');
      if (!b) return;
      g.querySelectorAll('.chip').forEach(function (c) { c.classList.remove('on'); });
      b.classList.add('on');
      var l = document.querySelector('[data-size-label]');
      if (l) l.textContent = b.textContent;
    });
  });

  // Barre d'achat fixe sur mobile
  var buy = document.querySelector('.buy'), sticky = document.querySelector('.sticky-buy');
  if (buy && sticky) {
    document.body.classList.add('has-sticky');
    new IntersectionObserver(function (en) {
      en.forEach(function (x) { sticky.classList.toggle('on', !x.isIntersecting && x.boundingClientRect.top < 0); });
    }).observe(buy);
  }

  // Texte d'introduction repliable
  document.querySelectorAll('.readmore').forEach(function (b) {
    b.addEventListener('click', function () {
      var p = b.previousElementSibling, open = p.classList.toggle('clamp') === false;
      b.textContent = open ? 'Lire moins' : 'Lire plus';
    });
  });

  // Pied de page : rubriques repliées sur mobile
  if (matchMedia('(max-width: 800px)').matches) {
    document.querySelectorAll('.footer details').forEach(function (d) { d.removeAttribute('open'); });
  } else {
    document.querySelectorAll('.footer summary').forEach(function (s) { s.addEventListener('click', function (e) { e.preventDefault(); }); });
  }

  // Apparitions au défilement
  var sel = '.sec-head,.tile,.grid .card,.post,.split>*,.values>div,.coll-head,.rich>*,.faq details,.info,.chapter>*,.pull,.fabrics>div,.edito>*,.teaser .txt>*,.band .narrow>*,.story-a>*,.story-b>*,.picks-head,.social-head,.feed>a';
  var els = [].slice.call(document.querySelectorAll(sel));
  els.forEach(function (e) {
    var sib = [].slice.call(e.parentNode.children).filter(function (c) { return c.matches(sel); });
    e.style.setProperty('--d', Math.min(sib.indexOf(e), 6) * 0.08 + 's');
    e.classList.add('rv');
  });
  var ro = new IntersectionObserver(function (en) {
    en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); ro.unobserve(x.target); } });
  }, { rootMargin: '0px 0px -6% 0px' });
  els.forEach(function (e) { ro.observe(e); });

  // Vidéos : lecture seulement quand elles sont visibles
  var vo = new IntersectionObserver(function (en) {
    en.forEach(function (x) {
      var v = x.target;
      if (x.isIntersecting && !calm) v.play().catch(function () {}); else v.pause();
    });
  }, { threshold: 0.25 });
  document.querySelectorAll('video[data-auto]').forEach(function (v) { v.muted = true; vo.observe(v); });
})();
