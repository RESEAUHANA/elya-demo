"""Descriptions produit « éditoriales » : une histoire visuelle sous la fiche, pièce par pièce.

Chaque entrée de STORIES est indexée par le handle du produit. Les faits (mesures, matière, détails)
viennent uniquement de la fiche Shopify de la cliente : rien n'est inventé.
"""
IMG = "https://elyacollection.com/cdn/shop/files/"

STORIES = {
    "lenvol-tunique-cape-asymetrique-blanc": dict(
        kicker="L’Envol · Tunique à cape",
        title=("Le haut qui fait", "la tenue."),
        lead="Une longue cape asymétrique, un tombé fluide, des manches oversize. Tu la poses sur tes basiques, et ta tenue change d’allure.",
        hero=IMG + "photo_2026-09-11_10-25-40.jpg",
        hero_alt="L’Envol blanc portée avec un jean et un sac chocolat devant une façade claire",
        badge=("95", "cm de cape"),
        packshot=IMG + "9EC3ED46-C0AE-42C3-AE0B-14F8320C112C.png",
        packshot_alt="L’Envol blanc sur fond blanc, cape asymétrique et manches oversize",
        # Points d'intérêt sur le packshot : (x %, y %, titre, texte)
        spots=[
            (55, 17, "Deux boutons", "Un bouton ferme le haut, un second maintient la cape en place."),
            (44, 46, "Un tombé fluide", "Le Tencel glisse sur le corps et accompagne chaque mouvement."),
            (84, 66, "Manches oversize", "Larges et souples, elles donnent du volume sans alourdir."),
            (21, 82, "La cape asymétrique", "95 cm de longueur. Une épingle suffit pour la ramener vers l’arrière et couvrir davantage."),
        ],
        # Cotes dessinées sur le packshot : (x1, y1, x2, y2 en %, libellé)
        measures=[
            (50, 14, 50, 70, "Devant 52 cm"),
            (13, 14, 13, 94, "Cape 95 cm"),
            (92, 14, 92, 80, "Dos 63 cm"),
        ],
        figures=[("95", "cm", "de cape asymétrique"), ("52", "cm", "devant, 63 cm au dos"),
                 ("86", "%", "de Tencel"), ("36–42", "", "en taille unique")],
        fabric=dict(img=IMG + "photo_2026-09-11_10-25-45.jpg", alt="Gros plan sur le tombé de la cape L’Envol blanc",
                    pct=86, title="Tencel, la douceur qui tombe juste",
                    text="Une fibre issue du bois, douce et fluide. Elle donne à L’Envol ce tombé souple qui suit tes gestes.",
                    split=[("Tencel", 86), ("Polyester", 14)]),
        looks=[
            (IMG + "photo_2026-09-11_10-25-40.jpg", "En ville", "Jean droit, sac chocolat, baskets sable."),
            (IMG + "9204F988-FAC8-46A7-BCE8-8D05447768E5.jpg", "Ton sur ton", "Jupe ivoire et petit sac noir pour un look tout en lumière."),
            (IMG + "E3368205-1187-4DE8-81CE-142D3893B790.jpg", "Plus couvrante", "Cape ramenée vers l’arrière avec une épingle."),
        ],
        model="Le mannequin mesure 1,65 m et porte la taille unique.",
        other=("lenvol-tunique-cape-asymetrique-aubergine", "Aubergine"),
    ),
}


def render(s, p, P, r, img, esc):
    """Construit la section éditoriale d'une fiche produit."""
    t1, t2 = s["title"]
    words = " ".join(f'<span class="w"><span>{esc(w)}</span></span>' for w in t1.split())
    words += " " + " ".join(f'<span class="w"><em>{esc(w)}</em></span>' for w in t2.split())
    spots = "".join(
        f'<button class="spot" type="button" style="--x:{x}%;--y:{y}%" data-spot="{i}" aria-label="{esc(t)}"><span>{i + 1}</span></button>'
        for i, (x, y, t, _) in enumerate(s["spots"]))
    spot_list = "".join(
        f'<li data-spot="{i}"><b><i>0{i + 1}</i>{esc(t)}</b><p>{esc(d)}</p></li>' for i, (_, _, t, d) in enumerate(s["spots"]))
    lines = "".join(
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" pathLength="1"/>'
        f'<circle cx="{x1}" cy="{y1}" r=".9"/><circle cx="{x2}" cy="{y2}" r=".9"/>'
        for x1, y1, x2, y2, _ in s["measures"])
    labels = "".join(
        f'<span class="cote" style="--x:{x1}%;--y:{(y1 + y2) / 2}%">{esc(l)}</span>' for x1, y1, x2, y2, l in s["measures"])
    figs = "".join(
        f'<div class="fig"><b><span data-count="{n}">{esc(n)}</span><small>{esc(u)}</small></b><p>{esc(t)}</p></div>'
        for n, u, t in s["figures"])
    f = s["fabric"]
    bars = "".join(f'<li><span>{esc(n)}</span><i style="--v:{v}%"></i><b>{v} %</b></li>' for n, v in f["split"])
    looks = "".join(
        f'<figure class="look"><img src="{img(u, 900)}" alt="L’Envol portée : {esc(t.lower())}" loading="lazy">'
        f'<figcaption><i>0{i + 1}</i><b>{esc(t)}</b><span>{esc(d)}</span></figcaption></figure>'
        for i, (u, t, d) in enumerate(s["looks"]))
    oh, oc = s["other"]
    o = P[oh]
    return f"""
<section class="ps" id="histoire" aria-label="L’histoire de la pièce">
  <div class="ps-hero wrap">
    <div class="ps-hero-txt">
      <p class="ps-kicker">{esc(s["kicker"])}</p>
      <h2 class="ps-title">{words}</h2>
      <p class="ps-lead">{esc(s["lead"])}</p>
      <a class="ps-link" href="#details">Explorer la pièce<span class="arr">→</span></a>
    </div>
    <figure class="ps-hero-img" data-parallax>
      <img src="{img(s["hero"], 1200)}" alt="{esc(s["hero_alt"])}" loading="lazy">
      <figcaption class="ps-badge"><b data-count="{s["badge"][0]}">{s["badge"][0]}</b><span>{esc(s["badge"][1])}</span></figcaption>
    </figure>
  </div>

  <div class="ps-explore wrap" id="details">
    <div class="ps-board" data-mode="spots">
      <div class="ps-tabs" role="tablist">
        <button type="button" role="tab" aria-selected="true" data-mode-btn="spots">Les détails</button>
        <button type="button" role="tab" aria-selected="false" data-mode-btn="measures">Les mesures</button>
        <span class="ps-tab-ink"></span>
      </div>
      <div class="ps-canvas">
        <img src="{img(s["packshot"], 1000)}" alt="{esc(s["packshot_alt"])}" loading="lazy">
        <div class="ps-spots">{spots}</div>
        <svg class="ps-lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">{lines}</svg>
        <div class="ps-cotes">{labels}</div>
      </div>
    </div>
    <div class="ps-side">
      <p class="ps-kicker">Ce qui la rend unique</p>
      <ol class="ps-list">{spot_list}</ol>
      <p class="ps-model">{esc(s["model"])}</p>
    </div>
  </div>

  <div class="ps-figs"><div class="wrap">{figs}</div></div>

  <div class="ps-fabric wrap">
    <figure class="ps-fabric-img"><img src="{img(f["img"], 1000)}" alt="{esc(f["alt"])}" loading="lazy"></figure>
    <div class="ps-fabric-txt">
      <div class="ring" style="--p:{f["pct"]}"><svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="52"/><circle class="v" cx="60" cy="60" r="52" pathLength="100"/></svg>
        <b><span data-count="{f["pct"]}">{f["pct"]}</span>%</b></div>
      <h3>{esc(f["title"])}</h3>
      <p>{esc(f["text"])}</p>
      <ul class="bars">{bars}</ul>
    </div>
  </div>

  <div class="ps-looks wrap">
    <div class="ps-looks-head"><p class="ps-kicker">Trois façons de la porter</p><h3>Une pièce, trois allures</h3></div>
    <div class="ps-looks-row">{looks}</div>
  </div>

  <div class="ps-end wrap">
    <p class="ps-kicker">Ta couleur</p>
    <h3>Blanc lumineux ou aubergine profond&nbsp;?</h3>
    <div class="ps-colors">
      <a class="ps-color on" href="#top" data-top><img src="{img(p["images"][0], 600)}" alt="" loading="lazy"><span>{esc(p["color"])}<em>Tu la regardes</em></span></a>
      <a class="ps-color" href="{r}products/{oh}/"><img src="{img(o["images"][0], 600)}" alt="" loading="lazy"><span>{esc(oc)}<em>Découvrir</em></span></a>
    </div>
  </div>
</section>"""
