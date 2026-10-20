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

ICON_SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
ICON_USER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>'
ICON_BAG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M5 8h14l-1 13H6L5 8Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>'
ICON_MENU = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 7h18M3 12h18M3 17h18"/></svg>'

esc = html.escape


def img(url, width):
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}width={width}"


def price(v):
    return f"{float(v):.2f} €".replace(".", ",")


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
    # couleurs sœurs (même nom de modèle)
    for h, p in out.items():
        p["siblings"] = [(o["color"], k) for k, o in out.items() if o["name"] == p["name"]]
    return out


def jsonld(data):
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def faq_ld(faq):
    return jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})


def crumbs_ld(items):
    return jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": C.SITE["url"] + "/" + u} for i, (n, u) in enumerate(items)]})


def crumbs_html(items, r):
    parts = [f'<a href="{r}">Accueil</a>'] + [f'<a href="{r}{u}">{esc(n)}</a>' for n, u in items[:-1]] + [esc(items[-1][0])]
    return '<nav class="crumbs wrap" aria-label="Fil d’Ariane">' + " / ".join(parts) + "</nav>"


def faq_html(faq):
    if not faq:
        return ""
    rows = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)
    return f'<div class="faq">{rows}</div>'


def layout(path, title, meta, body, r, extra_head="", current=""):
    nav = "".join(f'<a href="{r}{u}"{" aria-current=page" if u == current else ""}>{esc(n)}</a>' for n, u in C.NAV)
    mnav = "".join(f'<a href="{r}{u}">{esc(n)}</a>' for n, u in C.NAV + [("Guide des tailles", "pages/guide-des-tailles/")])
    cols = "".join(
        f"<div><h4>{esc(t)}</h4><ul>" + "".join(f'<li><a href="{r}{u}">{esc(n)}</a></li>' for n, u in links) + "</ul></div>"
        for t, links in C.FOOTER.items())
    canonical = C.SITE["url"] + "/" + path
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta)}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(meta)}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400&family=Red+Hat+Text:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/elya.css">
{extra_head}
</head>
<body>
<div class="demo-ribbon">Maquette de démonstration — aperçu du futur site ELYA</div>
<div class="announce">{esc(C.SITE["announce"])}</div>
<header class="header">
  <div class="wrap header-in">
    <button class="burger" aria-label="Menu" onclick="document.querySelector('.mnav').classList.toggle('open')">{ICON_MENU}</button>
    <nav class="nav" aria-label="Navigation principale">{nav}</nav>
    <a class="logo" href="{r}" aria-label="ELYA Collection, accueil"><img src="{img(C.SITE["logo"], 300)}" alt="ELYA Collection" width="120" height="30"></a>
    <div class="icons"><a href="#" aria-label="Rechercher" data-demo>{ICON_SEARCH}</a><a href="#" aria-label="Compte" data-demo>{ICON_USER}</a><a href="#" aria-label="Panier" data-demo>{ICON_BAG}</a></div>
  </div>
  <nav class="mnav" aria-label="Menu mobile">{mnav}</nav>
</header>
<main>
{body}
</main>
<section class="newsletter">
  <div class="narrow">
    <p class="eyebrow" style="color:var(--sable)">Liste privée</p>
    <h2>Rejoins la liste privée ELYA</h2>
    <p>Sois la première informée des nouvelles collections et des réassorts, et reçois nos conseils de style.</p>
    <form class="nl-form" onsubmit="event.preventDefault();demo('Inscription simulée : dans la version Shopify, ton e-mail rejoindra la liste privée.')"><input type="email" required placeholder="Ton adresse e-mail" aria-label="Adresse e-mail"><button>S’inscrire</button></form>
  </div>
</section>
<footer class="footer">
  <div class="wrap">
    <div class="foot-grid">
      <div><img src="{img(C.SITE["logo"], 300)}" alt="ELYA Collection" width="110" height="28" style="margin-bottom:14px"><p class="muted">Le vestiaire modeste, autrement. Tuniques longues et ensembles modestes aux lignes fluides.</p><p><a href="{C.SITE["instagram"]}">Instagram</a> · <a href="{C.SITE["tiktok"]}">TikTok</a></p></div>
      {cols}
    </div>
    <div class="legal"><span>© 2026 ELYA Collection</span><span><a href="{r}pages/mentions-legales/">Mentions légales</a> · <a href="{r}pages/conditions-generales-de-vente/">CGV</a> · <a href="{r}pages/livraison-et-retours/">Livraison et retours</a></span></div>
  </div>
</footer>
<div class="toast" id="toast"></div>
<script>
function demo(t){{var e=document.getElementById('toast');e.textContent=t;e.classList.add('show');clearTimeout(window._t);window._t=setTimeout(function(){{e.classList.remove('show')}},3200)}}
document.querySelectorAll('[data-demo]').forEach(function(a){{a.addEventListener('click',function(ev){{ev.preventDefault();demo('Fonction disponible dans la version Shopify du site.')}})}});
</script>
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
    badge = "" if p["available"] else '<span class="badge">Épuisé</span>'
    return (f'<a class="card" href="{r}products/{p["handle"]}/"><div class="ph">{badge}'
            f'<img src="{img(p["images"][0], 700)}" alt="{esc(p["alt"])}" loading="lazy">{alt2}</div>'
            f'<h3>{esc(p["name"])}</h3><div class="sub">{esc(p["kind"])} · {esc(p["color"])}</div>'
            f'<div class="price">{price(p["price"])}</div></a>')


def clean_body(body_html):
    b = re.sub(r'\s(style|data-[\w-]+|class)="[^"]*"', "", body_html)
    b = re.sub(r"<(/?)h[1-6]>", r"<\1p>", b)
    b = re.sub(r"<span>|</span>|<meta[^>]*>", "", b)
    b = re.sub(r"<p>\s*(<br>)?\s*</p>", "", b)
    return b


def build_products(P):
    for h, p in P.items():
        path = f"products/{h}/"
        r = rel(path)
        coll = "ensembles-modestes" if "Ensemble" in p["kind"] else "tuniques-longues-femme"
        coll_name = C.COLLECTIONS[coll]["title"]
        crumbs = [(coll_name, f"collections/{coll}/"), (f'{p["name"]} — {p["color"]}', path)]
        gallery = "".join(
            f'<img src="{img(u, 1100)}" alt="{esc(p["alt"])} – vue {i + 1}"{"" if i == 0 else " loading=lazy"}>'
            for i, u in enumerate(p["images"]))
        colors = "".join(
            f'<a class="chip{" on" if k == h else ""}" href="{r}products/{k}/">{esc(c)}</a>' for c, k in p["siblings"])
        sizes = "".join(
            f'<button class="chip{"" if s in p["available_sizes"] else " off"}" type="button" onclick="this.parentNode.querySelectorAll(\'.chip\').forEach(function(c){{c.classList.remove(\'on\')}});this.classList.add(\'on\')">{esc(s)}</button>'
            for s in p["sizes"])
        cta = ('<button class="btn block" type="button" onclick="demo(\'Panier simulé : dans la version Shopify, la pièce sera ajoutée à ton panier.\')">Ajouter au panier</button>'
               if p["available"] else
               '<button class="btn block" type="button" onclick="demo(\'Alerte simulée : tu seras prévenue dès le retour en stock.\')">Me prévenir du retour en stock</button>')
        related = [q for k, q in P.items() if k != h and q["name"] != p["name"]][:4]
        body = f"""
{crumbs_html(crumbs, r)}
<div class="wrap pdp">
  <div class="gallery">{gallery}</div>
  <div class="info">
    <p class="eyebrow">{esc(p["kind"])}</p>
    <h1>{esc(p["name"])} — {esc(p["color"])}</h1>
    <div class="price">{price(p["price"])}</div>
    <div class="perk">Livraison en point relais offerte sur ta première commande</div>
    <div class="opt"><div class="lbl">Couleur</div><div class="chips">{colors}</div></div>
    <div class="opt"><div class="lbl">Taille <a href="{r}pages/guide-des-tailles/">Guide des tailles</a></div><div class="chips">{sizes}</div></div>
    {cta}
    <div class="acc">
      <details open><summary>Description</summary><div class="body">{clean_body(p["body"])}</div></details>
      <details><summary>Livraison et retours</summary><div class="body"><p>Préparation sous 1 à 3 jours ouvrés. Retours acceptés sous 14 jours. <a href="{r}pages/livraison-et-retours/">En savoir plus</a></p></div></details>
      <details><summary>Matière et entretien</summary><div class="body"><p>Retrouve la composition dans la description ci-dessus et nos conseils dans la page <a href="{r}pages/nos-matieres/">Nos matières</a>.</p></div></details>
    </div>
  </div>
</div>
<section style="padding-top:20px">
  <div class="wrap"><div class="sec-head"><h2>Tu aimeras aussi</h2><a class="link" href="{r}collections/{coll}/">Voir tout</a></div>
  <div class="grid">{"".join(card(q, r) for q in related)}</div></div>
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
        body = f"""
{crumbs_html(crumbs, r)}
<div class="wrap coll-head"><h1>{esc(c["title"])}</h1><p>{esc(c["intro"])}</p></div>
<div class="wrap"><div class="toolbar"><span>{len(items)} pièces</span><span>Trier : nouveautés</span></div>
<div class="grid">{"".join(card(p, r) for p in items)}</div></div>
<section><div class="narrow rich">{fill(c["body"], r)}{('<h2>Questions fréquentes</h2>' + faq_html(c["faq"])) if c["faq"] else ""}</div></section>"""
        ld = crumbs_ld(crumbs) + (faq_ld(c["faq"]) if c["faq"] else "")
        write(path, layout(path, c["seo_title"], c["meta"], body, r, ld, current=path))


def build_pages():
    for h, pg in C.PAGES.items():
        path = f"pages/{h}/"
        r = rel(path)
        crumbs = [(pg["title"], path)]
        content = fill(pg.get("body", ""), r) + faq_html(pg.get("faq", []))
        image = f'<img class="article-hero" src="{img(pg["image"], 1600)}" alt="ELYA, mode modeste élégante" style="aspect-ratio:16/8">' if pg.get("image") else ""
        body = f"""
{crumbs_html(crumbs, r)}
<div class="narrow" style="padding-top:30px"><h1>{esc(pg["title"])}</h1></div>
<div class="wrap">{image}</div>
<div class="narrow rich" style="padding-bottom:70px">{content}</div>"""
        ld = crumbs_ld(crumbs) + (faq_ld(pg["faq"]) if pg.get("faq") else "")
        write(path, layout(path, pg["seo_title"], pg["meta"], body, r, ld, current=path))


def build_blog(P):
    base = "blogs/conseils/"
    r = rel(base)
    arts = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)

    def post_card(a, r):
        return (f'<a class="post" href="{r}blogs/conseils/{a["slug"]}/"><img src="{img(a["image"], 800)}" alt="{esc(a["image_alt"])}" loading="lazy">'
                f'<h3>{esc(a["h1"])}</h3><p>{esc(a["excerpt"])}</p></a>')

    body = f"""
{crumbs_html([("Conseils de style", base)], r)}
<div class="wrap coll-head"><h1>Conseils de style</h1><p>Idées de tenues, conseils pour porter tes pièces et inspirations pour une allure modeste et élégante.</p></div>
<div class="wrap" style="padding-bottom:80px"><div class="posts">{"".join(post_card(a, r) for a in arts)}</div></div>"""
    write(base, layout(base, "Conseils de style et idées de tenues modestes | ELYA",
                       "Idées de tenues femme voilée chic, conseils pour porter une jupe longue ou une cape, tenues de mariage et d’hiver : le journal de style ELYA.",
                       body, r, current=base))
    for a in arts:
        path = f"{base}{a['slug']}/"
        r = rel(path)
        crumbs = [("Conseils de style", base), (a["h1"], path)]
        rel_products = [P[k] for k in a.get("related", []) if k in P]
        others = [o for o in arts if o["slug"] != a["slug"]][:3]
        body = f"""
{crumbs_html(crumbs, r)}
<article class="article">
  <div class="narrow" style="padding-top:30px"><p class="meta">Conseils de style · {a["date"][8:10]}/{a["date"][5:7]}/{a["date"][:4]}</p><h1>{esc(a["h1"])}</h1></div>
  <div class="wrap"><img class="article-hero" src="{img(a["image"], 1600)}" alt="{esc(a["image_alt"])}"></div>
  <div class="narrow rich">{fill(a["body"], r)}</div>
</article>
<section><div class="wrap"><div class="sec-head"><h2>Les pièces de l’article</h2></div><div class="grid">{"".join(card(p, r) for p in rel_products)}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><h2>À lire aussi</h2></div><div class="posts">{"".join(post_card(o, r) for o in others)}</div></div></section>"""
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
             ("Tenue femme voilée chic", "collections/tenue-femme-voilee-chic/", C.IMG + "photo_2026-09-07_21-52-24.jpg")]
    tiles_html = "".join(f'<a class="tile" href="{r}{u}"><img src="{img(i, 900)}" alt="{esc(n)} ELYA" loading="lazy"><span>{esc(n)}</span></a>' for n, u, i in tiles)
    posts = "".join(
        f'<a class="post" href="{r}blogs/conseils/{a["slug"]}/"><img src="{img(a["image"], 800)}" alt="{esc(a["image_alt"])}" loading="lazy"><h3>{esc(a["h1"])}</h3><p>{esc(a["excerpt"])}</p></a>'
        for a in arts[:3])
    home_faq = [
        ("Qu’est-ce que la mode modeste ?", "La mode modeste propose des vêtements couvrants, longs et amples, sans renoncer au style. Chez ELYA, elle se traduit par des lignes fluides, des matières agréables et une allure contemporaine."),
        ("Les pièces ELYA conviennent-elles à toutes les morphologies ?", "Nos pièces sont amples et souvent proposées en taille unique du 36 au 42. Le guide des tailles détaille les longueurs de chaque modèle."),
        ("Où sont fabriqués les vêtements ELYA ?", "Notre première collection, L’Aube, est fabriquée en Turquie."),
    ]
    body = f"""
<section class="hero" style="padding:0">
  <img src="{img(hm["hero_img"], 2000)}" alt="Femme voilée portant une cape bordeaux au vent, collection L’Aube ELYA">
  <div class="hero-in"><p class="eyebrow" style="color:var(--sable)">L’Aube — Collection I</p><h1>{esc(hm["h1"])}</h1><p>{esc(hm["hero_text"])}</p>
  <a class="btn light" href="{r}collections/laube-collection-i/">Découvrir la collection</a></div>
</section>
<section><div class="wrap"><div class="tiles">{tiles_html}</div></div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">Les pièces de L’Aube</p><h2>Tuniques longues et ensembles modestes</h2></div><a class="link" href="{r}collections/laube-collection-i/">Tout voir</a></div>
  <div class="grid">{"".join(card(p, r) for p in best)}</div>
</div></section>
<section style="padding-top:0"><div class="wrap split">
  <img src="{img(hm["story_img"], 1200)}" alt="Cape blanche ELYA portée devant une façade en pierre" loading="lazy">
  <div><p class="eyebrow">Le vestiaire modeste, autrement</p><h2>Ne plus choisir entre élégance, pudeur et confort</h2>
  <p>ELYA imagine des pièces longues, fluides et couvrantes, pensées pour accompagner les femmes au quotidien. Des coupes faciles à porter, des détails qui font la différence et une palette intemporelle.</p>
  <p>Notre première collection, L’Aube, réunit des tuniques au détail travaillé et des ensembles déjà assortis.</p>
  <a class="btn ghost" href="{r}pages/notre-histoire/">Notre histoire</a></div>
</div></section>
<div class="wrap"><div class="values">
  <div><b>Coupes couvrantes</b><span>Longues, amples et opaques</span></div>
  <div><b>Matières choisies</b><span>Tencel et coton</span></div>
  <div><b>Du 36 au 42</b><span>Guide des tailles détaillé</span></div>
  <div><b>Point relais offert</b><span>Sur ta première commande</span></div>
</div></div>
<section><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">Conseils de style</p><h2>Inspirations et idées de tenues</h2></div><a class="link" href="{r}blogs/conseils/">Tous les conseils</a></div>
  <div class="posts">{posts}</div>
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
