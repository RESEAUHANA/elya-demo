"""Génère le site de démonstration ELYA (HTML statique) à partir des données Shopify publiques et des contenus SEO.

Usage : python -I _src/build.py   (depuis la racine du dépôt)
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_src"))
import site_content as C  # noqa: E402

try:
    from blog_content import ARTICLES  # noqa: E402
except Exception as exc:  # le blog est optionnel tant qu'il n'est pas rédigé
    print("Blog non chargé :", exc)
    ARTICLES = []

esc = html.escape


def svg(path, extra=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"{extra}>{path}</svg>'


ICON = {
    "search": svg('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>'),
    "user": svg('<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>'),
    "bag": svg('<path d="M5 8h14l-1 13H6L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>'),
    "heart": svg('<path d="M12 20s-7-4.4-9.2-8.6C1.3 8.4 3 5 6.3 5c2 0 3.2 1.1 3.9 2.2.4.6 1.2.6 1.6 0C12.5 6.1 13.7 5 15.7 5 19 5 20.7 8.4 19.2 11.4 17 15.6 12 20 12 20Z"/>'),
    "menu": svg('<path d="M3 7h18M3 12h18M3 17h18"/>'),
    "close": svg('<path d="M5 5l14 14M19 5 5 19"/>'),
    "left": svg('<path d="M15 5l-7 7 7 7"/>'),
    "right": svg('<path d="M9 5l7 7-7 7"/>'),
    "swipe": '<svg viewBox="0 0 28 14" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M1 7h24M20 2l5 5-5 5"/></svg>',
    "filter": svg('<path d="M4 6h16M7 12h10M10 18h4"/>'),
    "sort": svg('<path d="M7 4v16M3 16l4 4 4-4M17 20V4M13 8l4-4 4 4"/>'),
    "truck": svg('<path d="M2 6h12v10H2zM14 10h4l3 3v3h-7z"/><circle cx="6" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/>'),
    "return": svg('<path d="M4 9h11a5 5 0 0 1 0 10H8"/><path d="M8 5 4 9l4 4"/>'),
    "pin": svg('<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.4"/>'),
    "drape": svg('<path d="M12 3c-3 4-7 6-8 18h16C19 9 15 7 12 3Z"/><path d="M12 3v18"/>'),
    "thread": svg('<circle cx="12" cy="12" r="8"/><path d="M5 9c4 1 10 1 14 0M5 15c4-1 10-1 14 0"/>'),
    "ruler": svg('<path d="M3 17 17 3l4 4L7 21z"/><path d="m7 13 2 2M10 10l2 2M13 7l2 2"/>'),
}
IG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">'
      '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor"/></svg>')
TT = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 3c.4 2.2 1.8 3.6 4 3.8v3.1c-1.5 0-2.8-.4-4-1.2v6.1'
      'c0 3.2-2.4 5.7-5.6 5.7S5.4 18 5.4 14.8s2.6-5.6 5.8-5.5v3.2c-1.4-.2-2.6.8-2.6 2.3 0 1.4 1.1 2.4 2.4 2.4 1.4 0 2.4-1 2.4-2.6V3h3.2Z"/></svg>')

VIDEOS = {
    "lenvol-tunique-cape-asymetrique-blanc": "envol-blanc-porte",
    "lepure-ensemble-jupe-bordeaux": "epure-bordeaux",
    "ensemble-horizon-marron": "horizon-marron",
    "le-sillage-tunique-a-liens-beige": "sillage-beige",
}

DRAWER_TILES = [("Tuniques", "collections/tuniques-longues-femme/", C.IMG + "photo_2026-09-04_14-29-40.jpg"),
                ("Ensembles", "collections/ensembles-modestes/", C.IMG + "E1DA6969-3AFF-43D4-B73F-5246318E74DE.jpg"),
                ("Tenue chic", "collections/tenue-femme-voilee-chic/", C.IMG + "photo_2026-09-07_21-52-24.jpg"),
                ("L’Aube", "collections/laube-collection-i/", C.IMG + "photo_2026-09-11_10-25-40.jpg")]


def img(url, width):
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}width={width}"


def price(v):
    return f"{float(v):.2f} €".replace(".", ",")


def video(r, name, cls="", extra=""):
    return (f'<video{cls} data-auto muted loop playsinline preload="metadata" poster="{r}assets/video/{name}.jpg" {extra}>'
            f'<source src="{r}assets/video/{name}.mp4" type="video/mp4"></video>')


def socials(light=False):
    c = " light" if light else ""
    return (f'<div class="socials"><a class="soc{c}" href="{C.SITE["instagram"]}" target="_blank" rel="noopener">{IG}<span>Instagram <b>@elyacollection__</b></span></a>'
            f'<a class="soc{c}" href="{C.SITE["tiktok"]}" target="_blank" rel="noopener">{TT}<span>TikTok <b>@elyacollection_</b></span></a></div>')


def rail(items, cls=""):
    return (f'<div class="rail-wrap"><div class="rail {cls}" data-rail>{items}</div>'
            f'<div class="rail-ui"><button class="arrow" data-prev aria-label="Précédent">{ICON["left"]}</button><div class="dots"></div>'
            f'<button class="arrow" data-next aria-label="Suivant">{ICON["right"]}</button></div>'
            f'<div class="swipe-hint">Glisse pour voir plus {ICON["swipe"]}</div></div>')


def load_products():
    raw = json.load(open(os.path.join(ROOT, "_src", "products.json"), encoding="utf-8"))["products"]
    out = {}
    for p in raw:
        seo = C.PRODUCTS[p["handle"]]
        images = [i["src"].split("?")[0] for i in p["images"]]
        variants = p["variants"]
        sizes, available_sizes = [], []
        size_idx = next((i for i, o in enumerate(p["options"]) if o["name"].lower().startswith("taille")), None)
        for v in variants:
            s = v.get(f"option{size_idx + 1}") if size_idx is not None else "Taille unique"
            if s not in sizes:
                sizes.append(s)
            if v["available"] and s not in available_sizes:
                available_sizes.append(s)
        out[seo["handle"]] = dict(seo, images=images, price=variants[0]["price"], body=p["body_html"],
                                  sizes=sizes, available_sizes=available_sizes,
                                  available=any(v["available"] for v in variants), old_handle=p["handle"])
    for h, p in out.items():
        p["siblings"] = [(o["color"], k, o["images"][0]) for k, o in out.items() if o["name"] == p["name"]]
    return out


def jsonld(data):
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def faq_ld(faq):
    return jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})


def crumbs_ld(items):
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": C.SITE["url"] + "/" + u} for i, (n, u) in enumerate(items)]})


def crumbs_html(items, r, cls=""):
    parts = [f'<a href="{r}">Accueil</a>'] + [f'<a href="{r}{u}">{esc(n)}</a>' for n, u in items[:-1]] + [esc(items[-1][0])]
    return f'<nav class="crumbs wrap {cls}" aria-label="Fil d’Ariane">' + " / ".join(parts) + "</nav>"


def band(eyebrow, text, link=None, dark=False):
    more = f'<a class="link" href="{link[1]}">{esc(link[0])}</a>' if link else ""
    return (f'<aside class="band{" dark" if dark else ""}"><div class="narrow"><span class="orn" aria-hidden="true"></span>'
            f'<p class="eyebrow">{esc(eyebrow)}</p><p class="band-text">{esc(text)}</p>{more}</div></aside>')


def faq_html(faq):
    if not faq:
        return ""
    rows = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)
    return f'<div class="faq">{rows}</div>'


def layout(path, title, meta, body, r, extra_head="", current=""):
    nav = "".join(f'<a href="{r}{u}"{" aria-current=page" if u == current else ""}>{esc(n)}</a>' for n, u in C.NAV)
    dtiles = "".join(f'<a href="{r}{u}"><img src="{img(i, 400)}" alt="" loading="lazy"><span>{esc(n)}</span></a>' for n, u, i in DRAWER_TILES)
    dlinks = "".join(f'<a href="{r}{u}">{esc(n)}</a>' for n, u in C.NAV + [("Guide des tailles", "pages/guide-des-tailles/"), ("Contact", "pages/contact/")])
    cols = "".join(
        f'<details open><summary>{esc(t)}</summary><ul>' + "".join(f'<li><a href="{r}{u}">{esc(n)}</a></li>' for n, u in links) + "</ul></details>"
        for t, links in C.FOOTER.items())
    canonical = C.SITE["url"] + "/" + path
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta)}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#F6F2EB">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(meta)}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&family=Red+Hat+Text:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/elya.css">
<script>document.documentElement.classList.add('js')</script>
{extra_head}
</head>
<body>
<div class="demo-ribbon">Maquette de démonstration — aperçu du futur site ELYA</div>
<div class="announce">{esc(C.SITE["announce"])}</div>
<header class="header">
  <div class="wrap header-in">
    <div><button class="icon-btn burger" data-menu="open" aria-label="Ouvrir le menu">{ICON["menu"]}</button><nav class="nav" aria-label="Navigation principale">{nav}</nav></div>
    <a class="logo" href="{r}" aria-label="ELYA Collection, accueil"><img src="{img(C.SITE["logo"], 300)}" alt="ELYA Collection" width="120" height="30"></a>
    <div class="icons">
      <a class="icon-btn" href="#" aria-label="Rechercher" data-demo="La recherche sera active dans la version Shopify.">{ICON["search"]}</a>
      <a class="icon-btn hide-m" href="#" aria-label="Mon compte" data-demo>{ICON["user"]}</a>
      <a class="icon-btn" href="#" aria-label="Mes favoris" data-demo="Tes favoris seront enregistrés dans ton compte sur la version Shopify.">{ICON["heart"]}<span class="count fav-count"></span></a>
      <a class="icon-btn" href="#" aria-label="Panier" data-demo="Le panier sera actif dans la version Shopify.">{ICON["bag"]}</a>
    </div>
  </div>
</header>
<div class="overlay"></div>
<aside class="drawer" aria-hidden="true" aria-label="Menu">
  <div class="drawer-top"><img src="{img(C.SITE["logo"], 300)}" alt="ELYA"><button class="icon-btn" data-menu="close" aria-label="Fermer le menu">{ICON["close"]}</button></div>
  <div class="drawer-tiles">{dtiles}</div>
  <nav class="drawer-links">{dlinks}</nav>
  <div class="drawer-social"><p class="eyebrow">Suis ELYA</p>{socials()}</div>
</aside>
<main>
{body}
</main>
<section class="newsletter" id="liste-privee">
  <div class="narrow">
    <p class="eyebrow" style="color:var(--sable)">Liste privée</p>
    <h2>Rejoins la liste privée ELYA</h2>
    <p>Sois la première informée des nouvelles collections et des réassorts, et reçois nos conseils de style.</p>
    <form class="nl-form" onsubmit="event.preventDefault();demo('Inscription simulée : dans la version Shopify, ton e-mail rejoindra la liste privée.')"><input type="email" required placeholder="Ton adresse e-mail" aria-label="Adresse e-mail"><button>S’inscrire</button></form>
  </div>
</section>
<footer class="footer">
  <div class="wrap">
    <div class="foot-social"><p>Rejoins-nous sur les réseaux</p>{socials()}</div>
    <div class="foot-grid">
      <div class="brand"><img src="{img(C.SITE["logo"], 300)}" alt="ELYA Collection" width="110" height="28" style="margin-bottom:14px"><p class="muted">Le vestiaire modeste, autrement. Tuniques longues et ensembles modestes aux lignes fluides, confectionnés en Turquie.</p></div>
      {cols}
    </div>
    <div class="legal"><span>© 2026 ELYA Collection</span><span><a href="{r}pages/mentions-legales/">Mentions légales</a> · <a href="{r}pages/conditions-generales-de-vente/">CGV</a> · <a href="{r}pages/livraison-et-retours/">Livraison et retours</a></span></div>
  </div>
</footer>
<div class="toast" id="toast" role="status"></div>
<script src="{r}assets/elya.js" defer></script>
</body>
</html>"""


def write(path, content):
    full = os.path.join(ROOT, path.replace("/", os.sep), "index.html") if path else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def rel(path):
    depth = path.count("/") if path else 0
    return "../" * depth if depth else "./"


def fill(text, r):
    return text.replace("{root}", r)


def card(p, r):
    alt2 = f'<img class="alt" src="{img(p["images"][1], 700)}" alt="" loading="lazy">' if len(p["images"]) > 1 else ""
    tags = ""
    if not p["available"]:
        tags += '<span class="tag top out">Épuisé</span>'
    if len(p["siblings"]) > 1:
        tags += '<span class="tag bottom">Plus de couleurs</span>'
    url = f'{r}products/{p["handle"]}/'
    return (f'<div class="card"><a class="ph" href="{url}" tabindex="-1">{tags}'
            f'<img src="{img(p["images"][0], 700)}" alt="{esc(p["alt"])}" loading="lazy">{alt2}</a>'
            f'<button class="heart" data-heart="{p["handle"]}" aria-label="Ajouter {esc(p["name"])} aux favoris">{ICON["heart"]}</button>'
            f'<a class="meta" href="{url}"><h3>{esc(p["name"])}</h3><div class="sub">{esc(p["kind"])} · {esc(p["color"])}</div>'
            f'<div class="price">{price(p["price"])}</div></a></div>')


def post_card(a, r):
    return (f'<a class="post" href="{r}blogs/conseils/{a["slug"]}/"><img src="{img(a["image"], 800)}" alt="{esc(a["image_alt"])}" loading="lazy">'
            f'<h3>{esc(a["h1"])}</h3><p>{esc(a["excerpt"])}</p></a>')


def clean_body(body_html):
    b = re.sub(r'\s(style|data-[\w-]+|class)="[^"]*"', "", body_html)
    b = re.sub(r"<(/?)h[1-6]>", r"<\1p>", b)
    b = re.sub(r"<span>|</span>|<meta[^>]*>", "", b)
    b = re.sub(r"<p>\s*(<br>)?\s*</p>", "", b)
    return b


def mosaic(items, r):
    out = []
    for kind, val in items:
        if kind == "video":
            out.append(f'<a href="{C.SITE["tiktok"]}" target="_blank" rel="noopener" aria-label="Voir sur TikTok">{video(r, val)}<span class="net">{TT}</span></a>')
        else:
            out.append(f'<a href="{C.SITE["instagram"]}" target="_blank" rel="noopener" aria-label="Voir sur Instagram"><img src="{img(val, 700)}" alt="Tenue ELYA sur Instagram" loading="lazy"><span class="net">{IG}</span></a>')
    return f'<div class="mosaic">{"".join(out)}</div>'


def story_html(s, P, r):
    picks = "".join(
        f'<a class="pick" href="{r}products/{h}/"><img src="{img(P[h]["images"][0], 700)}" alt="{esc(P[h]["alt"])}" loading="lazy">'
        f'<div class="t"><p class="k">{esc(k)}</p><b>{esc(P[h]["name"])} — {esc(P[h]["color"])}</b><p>{esc(line)}</p><span class="go">Découvrir</span></div></a>'
        for h, k, line in s["picks"])
    return f"""
<section class="story"><div class="wrap">
  <div class="story-a">
    <img class="big" src="{img(s["img_big"], 1000)}" alt="Tenue ELYA, mode modeste" loading="lazy">
    <div class="txt"><p class="eyebrow">Le mot d’ELYA</p><h2>{esc(s["h2"])}</h2><p>{fill(s["p"], r)}</p></div>
    <img class="small" src="{img(s["img_small"], 600)}" alt="Détail de matière ELYA" loading="lazy">
  </div>
  <div class="picks-head"><h3>{esc(s["picks_title"])}</h3></div>
  {rail(picks, "picks")}
  <div class="story-b">
    {mosaic(s["mosaic"], r)}
    <div class="txt"><p class="eyebrow">Vu sur nos réseaux</p><h2>{esc(s["h2b"])}</h2><p>{fill(s["pb"], r)}</p>
    <p class="handle-line">Plus de tenues sur <a href="{C.SITE["instagram"]}" target="_blank" rel="noopener">Instagram</a> et <a href="{C.SITE["tiktok"]}" target="_blank" rel="noopener">TikTok</a></p></div>
  </div>
</div></section>"""


def build_products(P):
    for h, p in P.items():
        path = f"products/{h}/"
        r = rel(path)
        coll = "ensembles-modestes" if "Ensemble" in p["kind"] else "tuniques-longues-femme"
        coll_name = C.COLLECTIONS[coll]["title"]
        crumbs = [(coll_name, f"collections/{coll}/"), (f'{p["name"]} — {p["color"]}', path)]
        media = [f'<img src="{img(u, 1100)}" alt="{esc(p["alt"])} – vue {i + 1}"{"" if i == 0 else " loading=lazy"}>' for i, u in enumerate(p["images"])]
        if h in VIDEOS:
            media.insert(1, video(r, VIDEOS[h], extra=f'aria-label="{esc(p["name"])} porté, en vidéo"'))
        swatches = "".join(
            f'<a class="{"on" if k == h else ""}" href="{r}products/{k}/" aria-label="{esc(c)}" title="{esc(c)}"><img src="{img(im, 160)}" alt=""></a>'
            for c, k, im in p["siblings"])
        sizes = "".join(f'<button class="chip{"" if s in p["available_sizes"] else " off"}" type="button">{esc(s)}</button>' for s in p["sizes"])
        if p["available"]:
            action = "demo('Panier simulé : dans la version Shopify, la pièce sera ajoutée à ton panier.')"
            label = "Ajouter au panier"
        else:
            action = "demo('Alerte simulée : tu seras prévenue dès le retour en stock.')"
            label = "Me prévenir du retour"
        related = [q for k, q in P.items() if k != h and q["name"] != p["name"]][:8]
        body = f"""
{crumbs_html(crumbs, r, "pdp-crumbs")}
<div class="wrap pdp">
  <div class="gallery-wrap"><div class="gallery">{"".join(media)}</div><span class="gal-count">1 / {len(media)}</span><div class="dots"></div></div>
  <div class="info">
    <p class="eyebrow">{esc(p["kind"])}</p>
    <h1>{esc(p["name"])} — {esc(p["color"])}</h1>
    <div class="price">{price(p["price"])}</div>
    <div class="perk">{ICON["truck"]}Livraison en point relais offerte sur ta première commande</div>
    <div class="opt"><div class="lbl"><span>Couleur <b>{esc(p["color"])}</b></span></div><div class="swatches">{swatches}</div></div>
    <div class="opt"><div class="lbl"><span>Taille <b data-size-label></b></span><a href="{r}pages/guide-des-tailles/">Guide des tailles</a></div><div class="chips" data-sizes>{sizes}</div></div>
    <div class="buy"><button class="btn block" type="button" onclick="{action}">{label}</button><button class="heart" data-heart="{h}" aria-label="Ajouter aux favoris">{ICON["heart"]}</button></div>
    <ul class="reassure">
      <li>{ICON["truck"]}Préparée sous 1 à 3 jours ouvrés</li>
      <li>{ICON["return"]}Retours acceptés sous 14 jours</li>
      <li>{ICON["pin"]}Confectionnée en Turquie</li>
    </ul>
    <p class="seen">Vois-la portée sur <a href="{C.SITE["instagram"]}" target="_blank" rel="noopener">{IG}Instagram</a> et <a href="{C.SITE["tiktok"]}" target="_blank" rel="noopener">{TT}TikTok</a></p>
    <div class="acc">
      <details open><summary>Description</summary><div class="body">{clean_body(p["body"])}</div></details>
      <details><summary>Livraison et retours</summary><div class="body"><p>Préparation sous 1 à 3 jours ouvrés. Retours acceptés sous 14 jours. <a href="{r}pages/livraison-et-retours/">En savoir plus</a></p></div></details>
      <details><summary>Matière et entretien</summary><div class="body"><p>Retrouve la composition dans la description et nos conseils dans <a href="{r}pages/nos-matieres/">Nos matières</a>.</p></div></details>
    </div>
  </div>
</div>
<div class="sticky-buy"><div class="t"><b>{esc(p["name"])} — {esc(p["color"])}</b><span>{price(p["price"])}</span></div><button class="btn" type="button" onclick="{action}">{"Ajouter" if p["available"] else "Me prévenir"}</button></div>
{band("Confectionnée en Turquie", "Une pièce pensée pour se porter longue, couverte et légère, saison après saison.")}
<section style="padding-top:clamp(40px,6vw,70px)">
  <div class="wrap"><div class="sec-head"><h2>Tu aimeras aussi</h2><a class="btn ghost small" href="{r}collections/{coll}/">Voir tout</a></div>
  {rail("".join(card(q, r) for q in related))}</div>
</section>"""
        ld = jsonld({
            "@context": "https://schema.org", "@type": "Product", "name": f'{p["name"]} — {p["kind"]} {p["color"]}',
            "image": p["images"][:4], "description": p["meta"], "brand": {"@type": "Brand", "name": "ELYA"},
            "color": p["color"], "offers": {"@type": "Offer", "price": p["price"], "priceCurrency": "EUR",
                                             "availability": "https://schema.org/" + ("InStock" if p["available"] else "OutOfStock"),
                                             "url": C.SITE["url"] + "/" + path}}) + crumbs_ld(crumbs)
        write(path, layout(path, p["seo_title"], p["meta"], body, r, ld))


def build_collections(P):
    for h, c in C.COLLECTIONS.items():
        path = f"collections/{h}/"
        r = rel(path)
        items = [P[k] for k in c["products"]]
        crumbs = [(c["title"], path)]
        chips = "".join(f'<a href="{r}collections/{k}/"{" aria-current=page" if k == h else ""}>{esc(o["title"])}</a>' for k, o in C.COLLECTIONS.items())
        story = story_html(C.STORIES[h], P, r) if h in C.STORIES else f'<section><div class="narrow rich">{fill(c["body"], r)}</div></section>'
        faq = f'<section style="padding-top:0"><div class="narrow"><h2 class="center">Questions fréquentes</h2>{faq_html(c["faq"])}</div></section>' if c["faq"] else ""
        body = f"""
{crumbs_html(crumbs, r)}
<div class="wrap">
  <div class="coll-head"><h1>{esc(c["title"])}</h1><p class="intro clamp">{esc(c["intro"])}</p><button class="readmore" type="button">Lire plus</button></div>
  <nav class="chips-row" aria-label="Autres collections">{chips}</nav>
  <div class="toolbar"><button type="button" data-demo="Le tri sera actif dans la version Shopify.">{ICON["sort"]}Trier</button><button type="button" data-demo="Les filtres (taille, couleur, matière) seront actifs dans la version Shopify.">{ICON["filter"]}Filtrer</button><span class="count">{len(items)} pièces</span></div>
  <div class="grid">{"".join(card(p, r) for p in items)}</div>
</div>
{band(c["band"][0], c["band"][1]) if c.get("band") else ""}
{story}
{faq}"""
        ld = crumbs_ld(crumbs) + (faq_ld(c["faq"]) if c["faq"] else "")
        write(path, layout(path, c["seo_title"], c["meta"], body, r, ld, current=path))


def build_pages():
    for h, pg in C.PAGES.items():
        path = f"pages/{h}/"
        r = rel(path)
        crumbs = [(pg["title"], path)]
        if pg.get("editorial"):
            write(path, layout(path, pg["seo_title"], pg["meta"], fill(pg["body"], r), r, crumbs_ld(crumbs), current=path))
            continue
        content = fill(pg.get("body", ""), r) + faq_html(pg.get("faq", []))
        image = f'<img class="article-hero" src="{img(pg["image"], 1600)}" alt="ELYA, mode modeste élégante" style="aspect-ratio:16/8">' if pg.get("image") else ""
        body = f"""
{crumbs_html(crumbs, r)}
<div class="narrow" style="padding-top:26px"><h1>{esc(pg["title"])}</h1></div>
<div class="wrap">{image}</div>
<div class="narrow rich" style="padding-bottom:70px">{content}</div>"""
        ld = crumbs_ld(crumbs) + (faq_ld(pg["faq"]) if pg.get("faq") else "")
        write(path, layout(path, pg["seo_title"], pg["meta"], body, r, ld, current=path))


def build_blog(P):
    base = "blogs/conseils/"
    r = rel(base)
    arts = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
    body = f"""
{crumbs_html([("Conseils de style", base)], r)}
<div class="wrap coll-head"><h1>Conseils de style</h1><p class="intro">Idées de tenues, conseils pour porter tes pièces et inspirations pour une allure modeste et élégante.</p></div>
<div class="wrap" style="padding-bottom:80px"><div class="posts-grid">{"".join(post_card(a, r) for a in arts)}</div></div>"""
    write(base, layout(base, "Conseils de style et idées de tenues modestes | ELYA",
                       "Idées de tenues femme voilée chic, conseils pour porter une jupe longue ou une cape, tenues de mariage et d’hiver : le journal de style ELYA.",
                       body, r, current=base))
    for a in arts:
        path = f"{base}{a['slug']}/"
        r = rel(path)
        crumbs = [("Conseils de style", base), (a["h1"], path)]
        rel_products = [P[k] for k in a.get("related", []) if k in P]
        others = [o for o in arts if o["slug"] != a["slug"]]
        body = f"""
{crumbs_html(crumbs, r)}
<article class="article">
  <div class="narrow" style="padding-top:26px"><p class="meta">Conseils de style · {a["date"][8:10]}/{a["date"][5:7]}/{a["date"][:4]}</p><h1>{esc(a["h1"])}</h1></div>
  <div class="wrap"><img class="article-hero" src="{img(a["image"], 1600)}" alt="{esc(a["image_alt"])}"></div>
  <div class="narrow rich">{fill(a["body"], r)}</div>
</article>
<section><div class="wrap"><div class="sec-head"><h2>Les pièces de l’article</h2></div>{rail("".join(card(p, r) for p in rel_products))}</div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><h2>À lire aussi</h2></div>{rail("".join(post_card(o, r) for o in others), "posts")}</div></section>"""
        ld = jsonld({"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["h1"], "datePublished": a["date"],
                     "image": a["image"], "author": {"@type": "Organization", "name": "ELYA"},
                     "publisher": {"@type": "Organization", "name": "ELYA", "logo": {"@type": "ImageObject", "url": C.SITE["logo"]}}})
        ld += crumbs_ld(crumbs) + (faq_ld(a["faq"]) if a.get("faq") else "")
        write(path, layout(path, a["title"], a["meta"], body, r, ld))
    return arts


def build_home(P, arts):
    r = "./"
    hm = C.HOME
    best = [P[k] for k in ["lenvol-tunique-cape-asymetrique-blanc", "lepure-ensemble-jupe-bordeaux", "laurore-tunique-longue-noir",
                           "ensemble-horizon-bordeaux", "le-sillage-tunique-a-liens-beige", "leveil-tunique-ceinturee-marron",
                           "laurore-tunique-longue-blanc", "lepure-ensemble-jupe-marron"]]
    tiles = [("Tuniques longues", "collections/tuniques-longues-femme/", C.IMG + "photo_2026-09-04_14-29-40.jpg"),
             ("Ensembles modestes", "collections/ensembles-modestes/", C.IMG + "E1DA6969-3AFF-43D4-B73F-5246318E74DE.jpg"),
             ("Tenue femme voilée chic", "collections/tenue-femme-voilee-chic/", C.IMG + "photo_2026-09-07_21-52-24.jpg"),
             ("L’Aube — Collection I", "collections/laube-collection-i/", C.IMG + "IMG-1352.png")]
    tiles_html = "".join(f'<a class="tile" href="{r}{u}"><div class="ph"><img src="{img(i, 700)}" alt="{esc(n)} ELYA" loading="lazy"></div><span>{esc(n)}</span></a>' for n, u, i in tiles)
    reels = "".join(
        f'<a class="reel" href="{r}products/{h}/">{video(r, v)}<span class="cap">{esc(t)}<small>{esc(s)}</small></span></a>'
        for v, h, t, s in [("envol-blanc-porte", "lenvol-tunique-cape-asymetrique-blanc", "L’Envol", "Tunique à cape · Blanc"),
                           ("epure-bordeaux", "lepure-ensemble-jupe-bordeaux", "L’Épure", "Ensemble jupe longue · Bordeaux"),
                           ("sillage-beige", "le-sillage-tunique-a-liens-beige", "Le Sillage", "Tunique à liens · Beige"),
                           ("horizon-marron", "ensemble-horizon-marron", "L’Horizon", "Ensemble 3 pièces · Marron"),
                           ("envol-blanc-cape", "lenvol-tunique-cape-asymetrique-blanc", "L’Envol", "Le tombé de la cape")])
    feed_items = [("img", C.IMG + "photo_2026-09-11_10-25-40.jpg"), ("video", "collection-02-teaser"), ("img", C.IMG + "6CE7616A-CD52-4038-8399-4AD3EEAF9384.png"),
                  ("img", C.IMG + "photo_2026-09-07_21-52-24.jpg"), ("img", C.IMG + "IMG-1361.png"), ("img", C.IMG + "43203146-5DE7-482D-AE3F-4FE2625B03EF.jpg")]
    feed = "".join(
        (f'<a href="{C.SITE["tiktok"]}" target="_blank" rel="noopener" aria-label="Voir sur TikTok">{video(r, v)}<span class="net">{TT}</span></a>' if k == "video" else
         f'<a href="{C.SITE["instagram"]}" target="_blank" rel="noopener" aria-label="Voir sur Instagram"><img src="{img(v, 500)}" alt="Publication ELYA sur Instagram" loading="lazy"><span class="net">{IG}</span></a>')
        for k, v in feed_items)
    home_faq = [
        ("Qu’est-ce que la mode modeste ?", "La mode modeste propose des vêtements couvrants, longs et amples, sans renoncer au style. Chez ELYA, elle se traduit par des lignes fluides, des matières agréables et une allure contemporaine."),
        ("Les pièces ELYA conviennent-elles à toutes les morphologies ?", "Nos pièces sont amples et souvent proposées en taille unique du 36 au 42. Le guide des tailles détaille les longueurs de chaque modèle."),
        ("Où sont fabriqués les vêtements ELYA ?", "Notre première collection, L’Aube, est confectionnée en Turquie, avec des tissus sélectionnés sur place."),
    ]
    body = f"""
<section class="hero">
  <img src="{img(hm["hero_img"], 2000)}" alt="Femme voilée portant une cape bordeaux au vent, collection L’Aube ELYA">
  {video(r, "envol-blanc-cape", "", 'aria-hidden="true"')}
  <div class="hero-in"><p class="eyebrow" style="color:var(--sable)">L’Aube — Collection I</p><h1>{esc(hm["h1"])}</h1><p>{esc(hm["hero_text"])}</p>
  <a class="btn light" href="{r}collections/laube-collection-i/">Découvrir la collection</a></div>
</section>
<section><div class="wrap">
  <div class="sec-head"><div><h2>Shopper par catégorie</h2><p class="sub">Trouve ta prochaine pièce préférée</p></div></div>
  <div class="tiles">{tiles_html}</div>
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-head"><div><h2>Les pièces de L’Aube</h2><p class="sub">Tuniques longues et ensembles modestes</p></div><a class="btn ghost small" href="{r}collections/laube-collection-i/">Shopper</a></div>
  {rail("".join(card(p, r) for p in best))}
</div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-head"><div><h2>Le tombé, en vrai</h2><p class="sub">Nos pièces en mouvement</p></div><a class="btn ghost small" href="{C.SITE["tiktok"]}" target="_blank" rel="noopener">TikTok</a></div>
  {rail(reels, "reels")}
</div></section>
{band("L’esprit ELYA", "Des lignes longues, des matières qui respirent, une allure qui ne s’excuse pas d’être discrète.")}
<section><div class="wrap split">
  <img src="{img(hm["story_img"], 1200)}" alt="Cape blanche ELYA portée devant une façade en pierre" loading="lazy">
  <div><p class="eyebrow">Le vestiaire modeste, autrement</p><h2>Ne plus choisir entre élégance, pudeur et confort</h2>
  <p>ELYA imagine des pièces longues, fluides et couvrantes, confectionnées en Turquie dans des tissus choisis pour leur tombé et leur douceur.</p>
  <p>Notre première collection, L’Aube, réunit des tuniques au détail travaillé et des ensembles déjà assortis.</p>
  <a class="btn ghost" href="{r}pages/notre-histoire/">Notre histoire</a></div>
</div></section>
<div class="wrap"><div class="values">
  <div>{ICON["drape"]}<b>Coupes couvrantes</b><span>Longues, amples et opaques</span></div>
  <div>{ICON["thread"]}<b>Tissus de Turquie</b><span>Tencel et coton</span></div>
  <div>{ICON["ruler"]}<b>Du 36 au 42</b><span>Guide des tailles détaillé</span></div>
  <div>{ICON["truck"]}<b>Point relais offert</b><span>Sur ta première commande</span></div>
</div></div>
<section><div class="teaser">
  {video(r, "collection-02-teaser")}
  <div class="txt"><p class="eyebrow" style="color:var(--sable)">Bientôt</p><h2>Collection 02</h2>
  <p>De nouvelles silhouettes, la même exigence : des matières choisies, des lignes fluides et des pièces pensées pour durer. Quantités limitées.</p>
  <p><a class="btn light" href="#liste-privee">Rejoindre la liste privée</a></p></div>
</div></section>
<section class="social-sec"><div class="wrap">
  <div class="social-head"><div><p class="eyebrow">Suis-nous</p><h2>ELYA, au quotidien</h2><p class="handle">@elyacollection__ · @elyacollection_</p></div>{socials()}</div>
  <div class="feed">{feed}</div>
</div></section>
<section><div class="wrap">
  <div class="sec-head"><div><h2>Conseils de style</h2><p class="sub">Idées de tenues et inspirations</p></div><a class="btn ghost small" href="{r}blogs/conseils/">Tout lire</a></div>
  {rail("".join(post_card(a, r) for a in arts), "posts")}
</div></section>
<section style="padding-top:0"><div class="narrow"><h2 class="center">Questions fréquentes</h2>{faq_html(home_faq)}<p class="center" style="margin-top:26px"><a class="link" href="{r}pages/questions-frequentes/">Toutes les questions</a></p></div></section>"""
    ld = jsonld({"@context": "https://schema.org", "@type": "Organization", "name": "ELYA Collection", "url": C.SITE["url"],
                 "logo": C.SITE["logo"], "sameAs": [C.SITE["instagram"], C.SITE["tiktok"]]}) + faq_ld(home_faq)
    write("", layout("", hm["seo_title"], hm["meta"], body, r, ld))


def build_misc(P, arts):
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("# Maquette de démonstration : ne pas indexer\nUser-agent: *\nDisallow: /\n")
    urls = [""] + [f"collections/{h}/" for h in C.COLLECTIONS] + [f"products/{h}/" for h in P] + \
           [f"pages/{h}/" for h in C.PAGES] + ["blogs/conseils/"] + [f"blogs/conseils/{a['slug']}/" for a in arts]
    with open(os.path.join(ROOT, "plan-du-site.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join("/" + u for u in urls) + "\n")
    print(len(urls), "pages générées")


if __name__ == "__main__":
    P = load_products()
    build_products(P)
    build_collections(P)
    build_pages()
    arts = build_blog(P) if ARTICLES else []
    build_home(P, arts)
    build_misc(P, arts)
