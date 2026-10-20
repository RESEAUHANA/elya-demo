# Contenus du site de démonstration ELYA (textes SEO, collections, pages).
# Les liens internes utilisent {root}, remplacé par le générateur.

SITE = {
    "name": "ELYA Collection",
    "url": "https://elyacollection.com",
    "logo": "https://elyacollection.com/cdn/shop/files/ELYA_logo_transparent.png?width=400",
    "announce": "Livraison offerte en point relais sur ta première commande",
    "email": "contact@elyacollection.com",
    "instagram": "https://www.instagram.com/elyacollection__",
    "tiktok": "https://www.tiktok.com/@elyacollection_",
}

IMG = "https://elyacollection.com/cdn/shop/files/"

# Ancien identifiant Shopify -> nouvelles données SEO
PRODUCTS = {
    "l-envol-tunique-asymetrique-blanc": dict(
        handle="lenvol-tunique-cape-asymetrique-blanc", name="L’Envol", kind="Tunique à cape asymétrique", color="Blanc",
        seo_title="L’Envol – Tunique à cape asymétrique blanche | ELYA",
        meta="Tunique modeste à longue cape asymétrique, manches oversize et tombé fluide. Tencel, taille unique du 36 au 42. Blanc. Livraison en France.",
        alt="tunique à cape asymétrique L’Envol blanche, mode modeste femme"),
    "l-envol-tunique-asymetrique": dict(
        handle="lenvol-tunique-cape-asymetrique-aubergine", name="L’Envol", kind="Tunique à cape asymétrique", color="Aubergine",
        seo_title="L’Envol – Tunique à cape asymétrique aubergine | ELYA",
        meta="Tunique modeste à longue cape asymétrique, manches oversize et tombé fluide. Tencel, taille unique du 36 au 42. Aubergine. Livraison en France.",
        alt="tunique à cape asymétrique L’Envol aubergine, mode modeste femme"),
    "l-eveil-tunique-ceinturee-a-col-montant-copie": dict(
        handle="leveil-tunique-ceinturee-olive", name="L’Éveil", kind="Tunique ceinturée à col montant", color="Vert olive",
        seo_title="L’Éveil – Tunique longue ceinturée vert olive | ELYA",
        meta="Tunique longue et opaque à col montant, ceinture à nouer pour marquer la taille. Tencel, taille unique du 36 au 42. Vert olive.",
        alt="tunique longue ceinturée à col montant L’Éveil vert olive, tenue femme voilée"),
    "l-eveil-tunique-ceinturee-a-col-montant": dict(
        handle="leveil-tunique-ceinturee-marron", name="L’Éveil", kind="Tunique ceinturée à col montant", color="Marron",
        seo_title="L’Éveil – Tunique longue ceinturée marron | ELYA",
        meta="Tunique longue et opaque à col montant, ceinture à nouer pour marquer la taille. Tencel, taille unique du 36 au 42. Marron foncé.",
        alt="tunique longue ceinturée à col montant L’Éveil marron, tenue femme voilée"),
    "laurore-tunique-longue": dict(
        handle="laurore-tunique-longue-noir", name="L’Aurore", kind="Tunique longue lacée au dos", color="Noir",
        seo_title="L’Aurore – Tunique longue femme noire lacée | ELYA",
        meta="Tunique longue femme de 139 cm, laçage au dos pour marquer la taille, coupe opaque et élégante. Coton, du S au L. Noir.",
        alt="tunique longue noire L’Aurore avec laçage au dos, mode modeste femme"),
    "laurore-tunique-longue-copie": dict(
        handle="laurore-tunique-longue-blanc", name="L’Aurore", kind="Tunique longue lacée au dos", color="Blanc",
        seo_title="L’Aurore – Tunique longue femme blanche lacée | ELYA",
        meta="Tunique longue femme de 139 cm, laçage au dos pour marquer la taille, coupe opaque et élégante. Coton, du S au L. Blanc.",
        alt="tunique longue blanche L’Aurore avec laçage au dos, mode modeste femme"),
    "le-sillage-tunique-a-liens": dict(
        handle="le-sillage-tunique-a-liens-beige", name="Le Sillage", kind="Tunique à liens", color="Beige",
        seo_title="Le Sillage – Tunique à liens beige à superposer | ELYA",
        meta="Haut à superposer sur tes basiques, coupe originale et liens sur le devant. Taille unique (S, M, petit L). Beige. Mode modeste élégante.",
        alt="tunique à liens Le Sillage beige portée en superposition, mode modeste"),
    "ensemble-horizon-marron-copie": dict(
        handle="ensemble-horizon-bordeaux", name="L’Horizon", kind="Ensemble 3 pièces", color="Bordeaux",
        seo_title="L’Horizon – Ensemble modeste 3 pièces bordeaux | ELYA",
        meta="Ensemble modeste 3 pièces : tunique longue, pantalon fluide et ceinture à nouer. Opaque et léger, du 38 au 42. Bordeaux.",
        alt="ensemble modeste 3 pièces L’Horizon bordeaux, tunique longue et pantalon"),
    "ensemble-horizon-3-pieces": dict(
        handle="ensemble-horizon-marron", name="L’Horizon", kind="Ensemble 3 pièces", color="Marron",
        seo_title="L’Horizon – Ensemble modeste 3 pièces marron | ELYA",
        meta="Ensemble modeste 3 pièces : tunique longue, pantalon fluide et ceinture à nouer. Opaque et léger, du 38 au 42. Marron.",
        alt="ensemble modeste 3 pièces L’Horizon marron, tunique longue et pantalon"),
    "lepure-ensemble-jupe": dict(
        handle="lepure-ensemble-jupe-bordeaux", name="L’Épure", kind="Ensemble jupe longue", color="Bordeaux",
        seo_title="L’Épure – Ensemble jupe longue et haut bordeaux | ELYA",
        meta="Ensemble jupe longue et haut assortis, 100 % coton, opaque, taille à nouer. Du 36 au 42. Bordeaux. Une tenue modeste prête en un instant.",
        alt="ensemble jupe longue et haut L’Épure bordeaux, tenue modeste en coton"),
    "lepure-ensemble-jupe-copie": dict(
        handle="lepure-ensemble-jupe-marron", name="L’Épure", kind="Ensemble jupe longue", color="Marron",
        seo_title="L’Épure – Ensemble jupe longue et haut marron | ELYA",
        meta="Ensemble jupe longue et haut assortis, 100 % coton, opaque, taille à nouer. Du 36 au 42. Marron. Une tenue modeste prête en un instant.",
        alt="ensemble jupe longue et haut L’Épure marron, tenue modeste en coton"),
}

TUNIQUES = ["lenvol-tunique-cape-asymetrique-blanc", "leveil-tunique-ceinturee-marron", "laurore-tunique-longue-noir",
            "le-sillage-tunique-a-liens-beige", "laurore-tunique-longue-blanc", "lenvol-tunique-cape-asymetrique-aubergine",
            "leveil-tunique-ceinturee-olive"]
ENSEMBLES = ["lepure-ensemble-jupe-bordeaux", "ensemble-horizon-bordeaux", "lepure-ensemble-jupe-marron", "ensemble-horizon-marron"]

COLLECTIONS = {
    "tuniques-longues-femme": dict(
        band=("La tunique ELYA", "Une seule pièce, et la tenue prend une autre allure : une cape, un laçage, une ceinture."),
        title="Tuniques longues femme",
        seo_title="Tunique longue femme élégante et couvrante | ELYA",
        meta="Tuniques longues femme élégantes, fluides et opaques : cape asymétrique, laçage au dos, ceinture à nouer. Mode modeste en Tencel et coton.",
        intro="Longues, fluides et opaques, nos tuniques donnent de l’allure à tes basiques sans multiplier les couches.",
        products=TUNIQUES,
        image=IMG + "IMG-1352.png",
        body="""
<h2>La tunique longue, la pièce maîtresse d’un vestiaire modeste</h2>
<p>Une tunique longue bien coupée suffit à construire une tenue élégante : un pantalon large ou une jupe fluide, et c’est prêt. Chez ELYA, chaque tunique est pensée pour être <strong>couvrante sans être lourde</strong>, avec un détail qui fait la différence : une cape asymétrique, un laçage au dos ou une ceinture à nouer.</p>
<h3>Comment choisir ta tunique longue ?</h3>
<ul>
<li><strong>Pour un look qui ne passe pas inaperçu</strong> : <a href="{root}products/lenvol-tunique-cape-asymetrique-blanc/">L’Envol</a> et sa longue cape asymétrique.</li>
<li><strong>Pour une silhouette très longue</strong> : <a href="{root}products/laurore-tunique-longue-noir/">L’Aurore</a>, 139 cm, avec un laçage au dos pour marquer la taille.</li>
<li><strong>Pour le quotidien</strong> : <a href="{root}products/leveil-tunique-ceinturee-marron/">L’Éveil</a>, longue, opaque et ceinturée.</li>
<li><strong>Pour réveiller un basique</strong> : <a href="{root}products/le-sillage-tunique-a-liens-beige/">Le Sillage</a>, à porter en superposition.</li>
</ul>
<h3>Des matières choisies pour durer</h3>
<p>Nos tuniques sont confectionnées en Tencel ou en coton, des matières agréables à porter toute la journée. Découvre pourquoi dans notre page <a href="{root}pages/nos-matieres/">nos matières</a>, et trouve ta taille grâce au <a href="{root}pages/guide-des-tailles/">guide des tailles</a>.</p>
<p>Besoin d’idées pour les porter ? Lis nos <a href="{root}blogs/conseils/tenue-femme-voilee-chic-idees-looks/">10 idées de tenues femme voilée chic</a>.</p>
""",
        faq=[
            ("Avec quoi porter une tunique longue ?", "Avec un pantalon large et fluide pour un look moderne, ou avec une jupe longue pour une silhouette très couvrante. Garde des couleurs unies et assorties à ton hijab pour un rendu élégant."),
            ("Les tuniques ELYA sont-elles opaques ?", "Oui. Toutes nos tuniques sont pensées pour être opaques et couvrantes, sans avoir besoin d’ajouter une couche en dessous."),
            ("Quelle taille choisir pour une tunique taille unique ?", "Nos tuniques en taille unique conviennent du 36 au 42. Les mesures exactes de chaque modèle sont indiquées sur sa fiche et dans le guide des tailles."),
        ]),
    "ensembles-modestes": dict(
        band=("Déjà assortis", "Haut et bas pensés ensemble, pour une silhouette harmonieuse en un seul geste."),
        title="Ensembles modestes",
        seo_title="Ensemble modeste femme : jupe longue et 3 pièces | ELYA",
        meta="Ensembles modestes femme déjà assortis : ensemble jupe longue et haut, ensemble 3 pièces tunique et pantalon. Opaques, élégants, du 36 au 42.",
        intro="Haut et bas déjà assortis : une tenue complète, élégante et couvrante, prête en un instant.",
        products=ENSEMBLES,
        image=IMG + "E1DA6969-3AFF-43D4-B73F-5246318E74DE.jpg",
        body="""
<h2>L’ensemble modeste, la tenue qui te simplifie les matins</h2>
<p>Un ensemble, c’est la garantie d’une tenue harmonieuse sans réfléchir à ce qui va avec quoi. Nos <strong>ensembles modestes</strong> sont longs, opaques et pensés pour être portés aussi bien complets que dépareillés.</p>
<h3>Ensemble jupe longue et haut</h3>
<p><a href="{root}products/lepure-ensemble-jupe-bordeaux/">L’Épure</a> associe un haut et une jupe longue en 100 % coton, avec une taille à nouer pour l’ajuster. Une tenue élégante pour le quotidien comme pour une occasion, notamment pour un <a href="{root}blogs/conseils/tenue-femme-voilee-invitee-mariage/">mariage</a>.</p>
<h3>Ensemble 3 pièces tunique et pantalon</h3>
<p><a href="{root}products/ensemble-horizon-bordeaux/">L’Horizon</a> réunit une tunique longue, un pantalon fluide et une ceinture à nouer. Porte-le complet, ceinturé ou non, ou dépareille chaque pièce avec ton dressing.</p>
<h3>Bien choisir sa taille</h3>
<p>Nos ensembles sont proposés du 36 au 42. Consulte le <a href="{root}pages/guide-des-tailles/">guide des tailles</a> pour comparer les longueurs.</p>
""",
        faq=[
            ("Peut-on porter les pièces d’un ensemble séparément ?", "Oui. La tunique, le haut, la jupe ou le pantalon de nos ensembles se portent aussi avec d’autres pièces de ton dressing."),
            ("Quel ensemble choisir pour un mariage ?", "L’Épure, avec sa jupe longue en coton, et L’Horizon ceinturé sont deux options élégantes. Ajoute un hijab assorti et un sac structuré pour un rendu habillé."),
            ("Les ensembles sont-ils opaques ?", "Oui, tous nos ensembles sont confectionnés dans des tissus opaques."),
        ]),
    "tenue-femme-voilee-chic": dict(
        band=("Le luxe discret", "Peu de pièces, mais les bonnes : unies, longues, et un hijab ton sur ton."),
        title="Tenue femme voilée chic",
        seo_title="Tenue femme voilée chic et moderne | ELYA",
        meta="Toutes nos tenues pour femme voilée, chic et modernes : tuniques longues, ensembles jupe longue, pièces à cape. Mode modeste haut de gamme.",
        intro="Des silhouettes couvrantes, fluides et élégantes, pensées pour la femme voilée d’aujourd’hui.",
        products=TUNIQUES[:4] + ENSEMBLES[:2] + TUNIQUES[4:] + ENSEMBLES[2:],
        image=IMG + "382695EE-06F6-47FF-BF79-BA5D6B139ADB.png",
        body="""
<h2>Une tenue de femme voilée chic, sans compromis</h2>
<p>Être couverte, à l’aise et élégante en même temps : c’est l’idée de départ d’ELYA. Toutes nos pièces sont longues, opaques et coupées dans des matières fluides, pour une <strong>tenue de femme voilée chic et moderne</strong> au quotidien.</p>
<h3>Les codes d’une tenue élégante</h3>
<ul>
<li><strong>Des couleurs unies</strong> et chaudes : chocolat, bordeaux, ivoire, sable.</li>
<li><strong>Un hijab assorti</strong> à la tenue, pour une silhouette harmonieuse.</li>
<li><strong>Une pièce forte</strong> par tenue : une cape, un laçage, une ceinture.</li>
<li><strong>Des accessoires sobres</strong> : sac structuré, gants en cuir, bottines.</li>
</ul>
<p>Pour aller plus loin, découvre nos <a href="{root}blogs/conseils/tenue-femme-voilee-chic-idees-looks/">10 idées de looks</a> et nos conseils pour une <a href="{root}blogs/conseils/tenue-modeste-hiver-superposition/">tenue modeste en hiver</a>.</p>
""",
        faq=[
            ("Comment avoir une tenue de femme voilée chic ?", "Mise sur des pièces longues et unies, un hijab assorti à la tenue et un seul détail fort, comme une cape ou une ceinture. Les accessoires sobres finissent le look."),
            ("Où sont fabriquées les pièces ELYA ?", "Les pièces de notre première collection, L’Aube, sont fabriquées en Turquie et sélectionnées avec attention par ELYA."),
            ("Livrez-vous partout en France ?", "Oui, nous livrons en France métropolitaine, avec la livraison en point relais offerte sur ta première commande."),
        ]),
    "laube-collection-i": dict(
        band=("L’Aube — Collection I", "Ivoire, sable, chocolat, bordeaux : une palette chaude et silencieuse, faite pour durer."),
        title="L’Aube — Collection I",
        seo_title="L’Aube, première collection de mode modeste | ELYA",
        meta="L’Aube, la première collection ELYA : tuniques longues et ensembles modestes aux lignes fluides, en Tencel et coton. Fabriquée en Turquie.",
        intro="Notre première collection : des lignes fluides, des silhouettes couvrantes et une allure contemporaine.",
        products=TUNIQUES + ENSEMBLES,
        image=IMG + "photo_2026-09-11_10-25-40.jpg",
        body="""
<h2>L’Aube, le début de l’histoire ELYA</h2>
<p>L’Aube réunit nos premières pièces : des <a href="{root}collections/tuniques-longues-femme/">tuniques longues</a> au détail travaillé et des <a href="{root}collections/ensembles-modestes/">ensembles modestes</a> faciles à porter. Une collection pensée autour de silhouettes élégantes et intemporelles, dans une palette chaude : ivoire, sable, chocolat, bordeaux et noir.</p>
<p>Découvre <a href="{root}pages/notre-histoire/">notre histoire</a> et la façon dont nous imaginons le vestiaire modeste.</p>
""",
        faq=[]),
}

NAV = [
    ("Tuniques", "collections/tuniques-longues-femme/"),
    ("Ensembles", "collections/ensembles-modestes/"),
    ("L’Aube", "collections/laube-collection-i/"),
    ("Conseils", "blogs/conseils/"),
    ("Notre histoire", "pages/notre-histoire/"),
]

HOME = dict(
    seo_title="ELYA Collection | Mode modeste femme : tuniques et ensembles",
    meta="Tuniques longues, ensembles jupe longue et pièces à cape pour une allure modeste, élégante et contemporaine. Découvre L’Aube, la première collection ELYA.",
    hero_img=IMG + "382695EE-06F6-47FF-BF79-BA5D6B139ADB.png",
    h1="Mode modeste élégante pour femme",
    hero_text="Des lignes fluides, des silhouettes couvrantes, une allure contemporaine. Découvre L’Aube, notre première collection.",
    story_img=IMG + "photo_2026-09-11_10-25-40.jpg",
)

PAGES = {
    "guide-des-tailles": dict(
        title="Guide des tailles",
        seo_title="Guide des tailles – Tuniques et ensembles | ELYA",
        meta="Trouve ta taille ELYA : correspondances 36 à 42, mesures de chaque tunique et ensemble, conseils pour les modèles en taille unique.",
        body="""
<p>Nos pièces sont pensées pour être amples et couvrantes. Voici comment trouver la bonne taille, et les mesures exactes de chaque modèle.</p>
<h2>Correspondance des tailles</h2>
<div class="table-wrap"><table>
<tr><th>Taille ELYA</th><th>Taille française</th><th>Tour de poitrine</th><th>Tour de taille</th><th>Tour de hanches</th></tr>
<tr><td>S</td><td>36</td><td><span class="placeholder">à compléter</span></td><td><span class="placeholder">à compléter</span></td><td><span class="placeholder">à compléter</span></td></tr>
<tr><td>M</td><td>38</td><td><span class="placeholder">à compléter</span></td><td><span class="placeholder">à compléter</span></td><td><span class="placeholder">à compléter</span></td></tr>
<tr><td>L</td><td>40</td><td><span class="placeholder">à compléter</span></td><td><span class="placeholder">à compléter</span></td><td><span class="placeholder">à compléter</span></td></tr>
<tr><td>XL</td><td>42</td><td><span class="placeholder">à compléter</span></td><td><span class="placeholder">à compléter</span></td><td><span class="placeholder">à compléter</span></td></tr>
</table></div>
<h2>Les mesures de chaque modèle</h2>
<div class="table-wrap"><table>
<tr><th>Modèle</th><th>Tailles</th><th>Longueurs</th><th>Mannequin</th></tr>
<tr><td><a href="{root}products/lenvol-tunique-cape-asymetrique-blanc/">L’Envol</a></td><td>Taille unique (36 au 42)</td><td>Devant 52 cm · dos 63 cm · cape 95 cm</td><td>1,65 m, taille unique</td></tr>
<tr><td><a href="{root}products/leveil-tunique-ceinturee-marron/">L’Éveil</a></td><td>Taille unique (36 au 42)</td><td>Devant 70 cm · dos 74 cm</td><td>1,65 m, taille unique</td></tr>
<tr><td><a href="{root}products/laurore-tunique-longue-noir/">L’Aurore</a></td><td>S, M, L</td><td>Tunique 139 cm</td><td>1,65 m, taille S</td></tr>
<tr><td><a href="{root}products/le-sillage-tunique-a-liens-beige/">Le Sillage</a></td><td>Taille unique (S, M, petit L)</td><td>Haut 72 cm</td><td>1,65 m, taille unique</td></tr>
<tr><td><a href="{root}products/ensemble-horizon-bordeaux/">L’Horizon</a></td><td>38, 40, 42</td><td>Tunique 135 cm · pantalon 107 cm</td><td>1,66 m, taille M</td></tr>
<tr><td><a href="{root}products/lepure-ensemble-jupe-bordeaux/">L’Épure</a></td><td>36, 38, 40, 42</td><td>Haut 55 cm · jupe 97 cm</td><td>1,65 m, taille S</td></tr>
</table></div>
<h2>Nos conseils</h2>
<ul>
<li><strong>Taille unique</strong> : nos modèles en taille unique sont amples et conviennent du 36 au 42.</li>
<li><strong>Entre deux tailles</strong> : prends ta taille habituelle pour une coupe fluide, la taille au-dessus pour un rendu plus ample.</li>
<li><strong>Longueur</strong> : compare la longueur indiquée à ta taille. Une tunique de 139 cm arrive aux chevilles pour une personne d’environ 1,65 m.</li>
</ul>
<p>Une question ? Écris-nous à <a href="mailto:contact@elyacollection.com">contact@elyacollection.com</a>, nous t’aidons à choisir.</p>
"""),
    "notre-histoire": dict(
        title="Notre histoire",
        seo_title="Notre histoire – Mode modeste et tissus de Turquie | ELYA",
        meta="ELYA, la mode modeste pensée comme un vestiaire de luxe discret : tissus sélectionnés en Turquie, Tencel et coton, lignes fluides et silhouettes intemporelles.",
        editorial=True,
        body="""
<section class="edito-hero" style="padding:0">
  <video data-auto muted loop playsinline preload="metadata" poster="{root}assets/video/envol-blanc-cape.jpg" aria-hidden="true"><source src="{root}assets/video/envol-blanc-cape.mp4" type="video/mp4"></video>
  <div class="in"><p class="eyebrow" style="color:var(--sable)">Notre histoire</p><h1>La pudeur, comme une élégance</h1></div>
</section>
<nav class="crumbs wrap" aria-label="Fil d’Ariane"><a href="{root}">Accueil</a> / Notre histoire</nav>

<section><div class="narrow edito">
  <p class="lead">Il y a des vêtements que l’on porte, et d’autres qui vous portent. ELYA est née de cette nuance : l’envie d’un vestiaire où l’on n’aurait plus jamais à choisir entre <em>élégance</em>, <em>pudeur</em> et <em>confort</em>.</p>
  <p class="drop">Tout commence par un constat, partagé par tant de femmes : la mode modeste se résumait trop souvent à couvrir. Couvrir, sans sublimer. ELYA a choisi l’inverse. Des lignes longues qui allongent la silhouette, des volumes qui respirent, une taille que l’on marque d’un simple nœud. Une allure qui ne s’excuse pas d’être discrète, et qui fait de la retenue une signature.</p>
  <p>Ici, chaque pièce est pensée comme un essentiel. Elle se porte le lundi matin comme le samedi soir, sous la lumière d’un bureau ou dans l’effervescence d’un mariage. Elle s’associe, se superpose, se réinvente. Et elle traverse les saisons sans prendre une ride.</p>
</div></section>

<section style="padding-top:0"><blockquote class="pull">« Être couverte n’a jamais voulu dire s’effacer. »<cite>La philosophie ELYA</cite></blockquote></section>

<section style="padding-top:0"><div class="wrap chapter">
  <img src="https://elyacollection.com/cdn/shop/files/photo_2026-09-11_10-25-45.jpg?width=1200" alt="Gros plan sur le tombé fluide d’une cape blanche ELYA" loading="lazy">
  <div class="edito">
    <p class="num">I — La matière</p>
    <h2>Des tissus choisis en Turquie, comme on choisit un bijou</h2>
    <p>La Turquie est l’une des grandes terres textiles du monde. D’Istanbul à Bursa, ancienne capitale de la soie, des générations d’artisans y ont perfectionné l’art du tissage, du tombé et de la finition. C’est là qu’ELYA sélectionne ses étoffes et fait confectionner ses pièces.</p>
    <p>Un tissu se juge d’abord à la main. Sa douceur contre la peau, la façon dont il glisse, la lumière qu’il accroche. Puis au mouvement : une cape doit flotter, une jupe doit danser, une tunique doit tomber droit sans jamais coller. Rien n’est laissé au hasard, car c’est la matière qui fait l’allure.</p>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="fabrics">
    <div><b>Le Tencel</b><p>Une fibre née du bois, d’une douceur presque soyeuse. Respirante et fluide, elle accompagne chaque geste et reste agréable du matin au soir. L’âme de <a href="{root}products/lenvol-tunique-cape-asymetrique-blanc/">L’Envol</a> et de <a href="{root}products/leveil-tunique-ceinturee-marron/">L’Éveil</a>.</p></div>
    <div><b>Le coton</b><p>Naturel, respirant, d’une belle opacité. Il apporte la tenue d’un vêtement bien coupé et la simplicité d’une matière que la peau connaît. L’étoffe de <a href="{root}products/lepure-ensemble-jupe-bordeaux/">L’Épure</a> et de <a href="{root}products/laurore-tunique-longue-noir/">L’Aurore</a>.</p></div>
    <div><b>Les voiles fluides</b><p>Légers et peu froissables, pensés pour les journées qui s’étirent et les valises que l’on boucle vite. Le secret du drapé de <a href="{root}products/ensemble-horizon-bordeaux/">L’Horizon</a> et du <a href="{root}products/le-sillage-tunique-a-liens-beige/">Sillage</a>.</p></div>
  </div>
  <p class="center" style="margin-top:34px"><a class="link" href="{root}pages/nos-matieres/">Tout savoir sur nos matières</a></p>
</div></section>

<section><div class="wrap chapter rev">
  <video data-auto muted loop playsinline preload="metadata" poster="{root}assets/video/epure-bordeaux.jpg" aria-label="L’Épure bordeaux portée, en mouvement"><source src="{root}assets/video/epure-bordeaux.mp4" type="video/mp4"></video>
  <div class="edito">
    <p class="num">II — La coupe</p>
    <h2>Couvrante, jamais informe</h2>
    <p>La pudeur n’impose pas l’ampleur sans forme. Chez ELYA, chaque volume est dessiné. Une manche évasée qui s’ouvre comme une corolle, un laçage au dos qui sculpte la taille, une ceinture à nouer pour choisir son allure du jour.</p>
    <p>Les longueurs sont généreuses, les tissus opaques, les détails discrets mais précis : une surpiqûre, un bouton, un pli. Ce que l’on remarque à peine, et qui change tout.</p>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap chapter">
  <img src="https://elyacollection.com/cdn/shop/files/photo_2026-09-11_10-25-40.jpg?width=1200" alt="Cape blanche ELYA portée devant une façade en pierre" loading="lazy">
  <div class="edito">
    <p class="num">III — La palette</p>
    <h2>Des couleurs qui ne se démodent pas</h2>
    <p>Ivoire, sable, chocolat, bordeaux, noir. Une palette chaude et silencieuse, choisie pour durer plus d’une saison et pour s’accorder d’une pièce à l’autre. On y glisse un hijab ton sur ton, un sac structuré, une paire de gants en cuir, et la silhouette se fait magazine.</p>
    <p>C’est cela, le luxe discret : peu de choses, mais les bonnes.</p>
  </div>
</div></section>

<section><div class="narrow edito center">
  <p class="num">IV — L’Aube</p>
  <h2>Le début d’une histoire</h2>
  <p><a href="{root}collections/laube-collection-i/">L’Aube</a>, notre première collection, en pose les fondations : des <a href="{root}collections/tuniques-longues-femme/">tuniques longues</a> au détail travaillé et des <a href="{root}collections/ensembles-modestes/">ensembles</a> déjà assortis. La Collection 02 s’annonce déjà, avec la même exigence.</p>
  <p class="lead" style="margin-top:28px">ELYA — le vestiaire modeste, autrement.</p>
  <p style="margin-top:26px"><a class="btn" href="{root}collections/laube-collection-i/">Découvrir L’Aube</a></p>
</div></section>
"""),
    "nos-matieres": dict(
        title="Nos matières",
        seo_title="Nos matières : Tencel et coton | ELYA",
        meta="Tencel, coton, polyester : découvre les matières des pièces ELYA, leurs qualités et nos conseils d’entretien pour les garder longtemps.",
        body="""
<p>Le choix d’une matière change tout : le tombé, l’opacité, le confort au fil de la journée. Voici celles que nous utilisons et pourquoi.</p>
<h2>Le Tencel</h2>
<p>Le Tencel est une fibre issue du bois, douce et fluide. Il donne un <strong>tombé souple</strong> qui accompagne les mouvements et reste agréable à porter. On le retrouve dans <a href="{root}products/lenvol-tunique-cape-asymetrique-blanc/">L’Envol</a> et <a href="{root}products/leveil-tunique-ceinturee-marron/">L’Éveil</a> (86 % Tencel, 14 % polyester).</p>
<h2>Le coton</h2>
<p>Naturel et respirant, le coton apporte de la tenue et une belle <strong>opacité</strong>. <a href="{root}products/lepure-ensemble-jupe-bordeaux/">L’Épure</a> est en 100 % coton, <a href="{root}products/laurore-tunique-longue-noir/">L’Aurore</a> en 95 % coton et 5 % lycra pour plus de confort.</p>
<h2>Les mélanges polyester</h2>
<p>Le polyester, seul ou associé au lycra, rend la pièce <strong>légère, peu froissable et facile à entretenir</strong>. C’est le cas de <a href="{root}products/ensemble-horizon-bordeaux/">L’Horizon</a> et du <a href="{root}products/le-sillage-tunique-a-liens-beige/">Sillage</a>.</p>
<h2>Nos conseils d’entretien</h2>
<ul>
<li>Respecte toujours l’étiquette de ta pièce.</li>
<li>Lave à basse température et sur l’envers pour préserver la couleur.</li>
<li>Évite le sèche-linge : laisse sécher à plat ou sur cintre.</li>
<li>Repasse à basse température, ou utilise un défroisseur vapeur.</li>
</ul>
"""),
    "questions-frequentes": dict(
        title="Questions fréquentes",
        seo_title="Questions fréquentes – Tailles, livraison, retours | ELYA",
        meta="Toutes les réponses sur ELYA : choix de la taille, fabrication, délais de livraison, retours et entretien de tes pièces.",
        faq=[
            ("Comment choisir ma taille ?", "La taille disponible est indiquée sur chaque fiche produit. Certains modèles sont proposés en taille unique (du 36 au 42), d’autres en plusieurs tailles. Consulte notre guide des tailles pour comparer les mesures."),
            ("Où sont fabriquées les pièces ELYA ?", "Les pièces de la Collection I — L’Aube sont fabriquées en Turquie et sélectionnées avec attention par ELYA."),
            ("Quels sont les délais de livraison ?", "Les commandes sont généralement préparées sous 1 à 3 jours ouvrés. Les options de livraison et leurs délais estimés sont indiqués au moment de la commande."),
            ("La livraison est-elle offerte ?", "La livraison en point relais est offerte sur ta première commande. Le seuil de livraison offerte pour les commandes suivantes est indiqué au moment du paiement."),
            ("Puis-je retourner un article ?", "Oui. Tu disposes de 14 jours à compter de la réception pour exercer ton droit de rétractation. L’article peut être essayé, mais doit être retourné dans son état d’origine, avec ses étiquettes, sans avoir été lavé ni porté."),
            ("Les frais de retour sont-ils à ma charge ?", "En cas de changement d’avis, oui. Si tu reçois un article incorrect, endommagé ou défectueux, contacte-nous : les frais ne seront pas à ta charge."),
            ("Comment entretenir mes pièces ?", "Les instructions propres à chaque modèle sont sur son étiquette. Retrouve aussi nos conseils dans la page Nos matières."),
            ("Comment contacter ELYA ?", "Par e-mail à contact@elyacollection.com. Nous répondons dans les meilleurs délais."),
        ]),
    "livraison-et-retours": dict(
        title="Livraison et retours",
        seo_title="Livraison et retours | ELYA",
        meta="Livraison en France métropolitaine, préparation sous 1 à 3 jours ouvrés, point relais offert sur ta première commande, retours sous 14 jours.",
        body="""
<h2>Livraison</h2>
<ul>
<li><strong>Préparation</strong> : 1 à 3 jours ouvrés après la confirmation de ta commande.</li>
<li><strong>Zone</strong> : France métropolitaine.</li>
<li><strong>Offerte</strong> : la livraison en point relais est offerte sur ta première commande.</li>
<li><strong>Suivi</strong> : un numéro de suivi t’est envoyé dès l’expédition.</li>
</ul>
<h2>Retours</h2>
<p>Tu disposes de <strong>14 jours</strong> à compter de la réception pour retourner un article. Il doit être dans son état d’origine, non lavé, non porté, avec ses étiquettes. Écris-nous à <a href="mailto:contact@elyacollection.com">contact@elyacollection.com</a> avec ton numéro de commande : nous t’envoyons les instructions.</p>
<h2>Remboursement</h2>
<p>Après réception et vérification, le remboursement est effectué sur le moyen de paiement utilisé, dans les délais légaux.</p>
"""),
    "contact": dict(
        title="Contact",
        seo_title="Contact | ELYA",
        meta="Une question sur une commande, une taille ou une pièce ? Écris à ELYA à contact@elyacollection.com.",
        body="""
<p>Une question sur ta commande, une taille ou une pièce ? Nous sommes là pour t’accompagner.</p>
<p><strong>E-mail</strong> : <a href="mailto:contact@elyacollection.com">contact@elyacollection.com</a></p>
<p><strong>Instagram</strong> : <a href="https://www.instagram.com/elyacollection__">@elyacollection__</a> · <strong>TikTok</strong> : <a href="https://www.tiktok.com/@elyacollection_">@elyacollection_</a></p>
<p>Nous te répondons dans les meilleurs délais.</p>
"""),
    "mentions-legales": dict(
        title="Mentions légales",
        seo_title="Mentions légales | ELYA",
        meta="Mentions légales du site elyacollection.com : éditeur, hébergeur, propriété intellectuelle et données personnelles.",
        body="""
<h2>Éditeur du site</h2>
<p>Le site elyacollection.com est édité par <span class="placeholder">[nom ou raison sociale]</span>, <span class="placeholder">[forme juridique]</span>, SIRET <span class="placeholder">[numéro]</span>, dont le siège est situé <span class="placeholder">[adresse]</span>.</p>
<p>E-mail : contact@elyacollection.com · Téléphone : <span class="placeholder">[numéro]</span></p>
<p>Responsable de la publication : <span class="placeholder">[nom]</span>.</p>
<h2>Hébergeur</h2>
<p>Shopify International Limited, Victoria Buildings, 2e étage, 1-2 Haddington Road, Dublin 4, D04 XN32, Irlande.</p>
<h2>Propriété intellectuelle</h2>
<p>L’ensemble des contenus du site (textes, photographies, logo) est la propriété d’ELYA, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
<h2>Données personnelles</h2>
<p>Les données collectées sont traitées conformément à notre politique de confidentialité. Tu peux exercer tes droits d’accès, de rectification et de suppression en écrivant à contact@elyacollection.com.</p>
<p class="muted"><em>Les champs surlignés sont à compléter avec les informations de l’entreprise.</em></p>
"""),
    "conditions-generales-de-vente": dict(
        title="Conditions générales de vente",
        seo_title="Conditions générales de vente | ELYA",
        meta="Conditions générales de vente ELYA : commandes, prix, paiement, livraison, droit de rétractation de 14 jours, garanties et médiation.",
        body="""
<h2>1. Objet</h2>
<p>Les présentes conditions régissent les ventes réalisées sur elyacollection.com par <span class="placeholder">[raison sociale]</span>, SIRET <span class="placeholder">[numéro]</span>.</p>
<h2>2. Prix</h2>
<p>Les prix sont indiqués en euros, toutes taxes comprises, hors frais de livraison indiqués avant la validation de la commande.</p>
<h2>3. Commande et paiement</h2>
<p>La commande est validée après acceptation des présentes conditions et paiement complet par les moyens proposés sur le site.</p>
<h2>4. Livraison</h2>
<p>Les modalités et délais sont détaillés dans la page <a href="{root}pages/livraison-et-retours/">Livraison et retours</a>.</p>
<h2>5. Droit de rétractation</h2>
<p>Conformément au Code de la consommation, tu disposes de 14 jours à compter de la réception pour exercer ton droit de rétractation, sans avoir à te justifier.</p>
<h2>6. Garanties légales</h2>
<p>Les produits bénéficient de la garantie légale de conformité (articles L217-3 et suivants du Code de la consommation) et de la garantie des vices cachés (articles 1641 et suivants du Code civil).</p>
<h2>7. Médiation</h2>
<p>En cas de litige, tu peux recourir gratuitement au médiateur de la consommation : <span class="placeholder">[nom et coordonnées du médiateur]</span>.</p>
<p class="muted"><em>Modèle à faire valider ; les champs surlignés sont à compléter.</em></p>
"""),
}

FOOTER = {
    "Boutique": [("Tuniques longues", "collections/tuniques-longues-femme/"), ("Ensembles modestes", "collections/ensembles-modestes/"),
                 ("Tenue femme voilée chic", "collections/tenue-femme-voilee-chic/"), ("L’Aube — Collection I", "collections/laube-collection-i/")],
    "Aide": [("Guide des tailles", "pages/guide-des-tailles/"), ("Livraison et retours", "pages/livraison-et-retours/"),
             ("Questions fréquentes", "pages/questions-frequentes/"), ("Contact", "pages/contact/")],
    "ELYA": [("Notre histoire", "pages/notre-histoire/"), ("Nos matières", "pages/nos-matieres/"), ("Conseils de style", "blogs/conseils/")],
}

# Récits illustrés des collections (remplacent les blocs de texte SEO).
# Mosaïque : ("video", nom) renvoie vers TikTok, ("img", url) vers Instagram.
STORIES = {
    "tuniques-longues-femme": dict(
        img_big=IMG + "IMG-1354.png", img_small=IMG + "photo_2026-09-11_10-25-43.jpg",
        h2="La tunique longue, pièce maîtresse",
        p="""Une tunique bien coupée, un pantalon large ou une jupe fluide, et la tenue est faite. Chez ELYA, chaque <strong>tunique longue femme</strong> est couvrante sans être lourde, avec ce détail qui change tout : une cape, un laçage, une ceinture.""",
        picks_title="Laquelle est faite pour toi ?",
        picks=[("lenvol-tunique-cape-asymetrique-blanc", "Pour être remarquée", "Une cape asymétrique qui flotte à chaque pas."),
               ("laurore-tunique-longue-noir", "Pour une silhouette très longue", "139 cm et un laçage au dos qui sculpte la taille."),
               ("leveil-tunique-ceinturee-marron", "Pour chaque jour", "Longue, opaque, ceinturée : sans réfléchir."),
               ("le-sillage-tunique-a-liens-beige", "Pour réveiller un basique", "À superposer sur ce que tu as déjà.")],
        mosaic=[("video", "envol-blanc-porte"), ("img", IMG + "IMG-1361.png"), ("img", IMG + "photo_2026-09-04_14-29-35.jpg")],
        h2b="Des matières qui respirent",
        pb="""Tencel soyeux ou coton opaque : nos tuniques se portent du matin au soir. Découvre <a href="{root}pages/nos-matieres/">nos matières</a>, trouve ta taille dans le <a href="{root}pages/guide-des-tailles/">guide des tailles</a>, et pioche des idées dans nos <a href="{root}blogs/conseils/tenue-femme-voilee-chic-idees-looks/">10 looks de femme voilée chic</a>."""),
    "ensembles-modestes": dict(
        img_big=IMG + "CD54A2FF-4FCB-4D71-8FDB-3D9C17641044.png", img_small=IMG + "43203146-5DE7-482D-AE3F-4FE2625B03EF.jpg",
        h2="Déjà assortis, jamais ennuyeux",
        p="""Un <strong>ensemble modeste</strong>, c’est une tenue complète en un geste. Haut et bas pensés ensemble, longs et opaques, à porter complets les jours pressés ou dépareillés quand l’envie te prend.""",
        picks_title="Jupe longue ou trois pièces ?",
        picks=[("lepure-ensemble-jupe-bordeaux", "Ensemble jupe longue", "Haut et jupe en coton, taille à nouer."),
               ("ensemble-horizon-bordeaux", "Ensemble 3 pièces", "Tunique, pantalon fluide et ceinture."),
               ("lepure-ensemble-jupe-marron", "Pour un mariage", "La jupe longue, un hijab assorti, un sac structuré."),
               ("ensemble-horizon-marron", "Pour voyager léger", "Peu froissable, il se porte de mille façons.")],
        mosaic=[("video", "epure-bordeaux"), ("img", IMG + "photo_2026-09-07_21-52-29.jpg"), ("img", IMG + "5B0011A7-3302-447E-9FF5-3652D7FB8872.png")],
        h2b="Une tenue, plusieurs vies",
        pb="""Porte la jupe de <a href="{root}products/lepure-ensemble-jupe-bordeaux/">L’Épure</a> avec une chemise, la tunique de <a href="{root}products/ensemble-horizon-bordeaux/">L’Horizon</a> sur une jupe de ton dressing. Nos conseils pour un <a href="{root}blogs/conseils/tenue-femme-voilee-invitee-mariage/">mariage</a> et pour <a href="{root}blogs/conseils/comment-porter-une-jupe-longue/">porter une jupe longue</a> t’attendent sur le blog."""),
    "tenue-femme-voilee-chic": dict(
        img_big=IMG + "photo_2026-09-11_10-25-36.jpg", img_small=IMG + "B4A2E684-8C01-4005-A862-5472F1400F38.jpg",
        h2="Couverte, à l’aise, et chic",
        p="""Une <strong>tenue de femme voilée chic</strong> tient à peu de choses : des pièces longues et unies, un hijab ton sur ton, un seul détail fort. Le reste, c’est ton allure.""",
        picks_title="Quatre façons d’être élégante",
        picks=[("lenvol-tunique-cape-asymetrique-aubergine", "Le caractère", "La cape aubergine, avec un pantalon droit."),
               ("laurore-tunique-longue-blanc", "La lumière", "Le blanc long, lacé au dos, pour l’été comme l’hiver."),
               ("lepure-ensemble-jupe-bordeaux", "L’occasion", "La jupe longue bordeaux, pour les grands jours."),
               ("ensemble-horizon-marron", "Le quotidien", "Le marron, ceinturé, du lundi au dimanche.")],
        mosaic=[("video", "horizon-marron"), ("img", IMG + "6CE7616A-CD52-4038-8399-4AD3EEAF9384.png"), ("img", IMG + "photo_2026-09-04_22-07-39.jpg")],
        h2b="Inspire-toi, on te montre tout",
        pb="""Chaque semaine, de nouvelles tenues sur nos réseaux, et plus d’idées dans <a href="{root}blogs/conseils/tenue-femme-voilee-chic-idees-looks/">10 looks de femme voilée chic</a> et notre guide de la <a href="{root}blogs/conseils/tenue-modeste-hiver-superposition/">tenue modeste en hiver</a>."""),
    "laube-collection-i": dict(
        img_big=IMG + "photo_2026-09-11_10-25-40.jpg", img_small=IMG + "0F21475B-2023-4CB6-A6EA-8417F79F322D.jpg",
        h2="L’Aube, là où tout commence",
        p="""Notre première collection pose les bases : des <a href="{root}collections/tuniques-longues-femme/">tuniques longues</a> au détail travaillé, des <a href="{root}collections/ensembles-modestes/">ensembles</a> déjà assortis, et une palette chaude qui traverse les saisons.""",
        picks_title="Les incontournables de L’Aube",
        picks=[("lenvol-tunique-cape-asymetrique-blanc", "La signature", "L’Envol et sa cape asymétrique."),
               ("lepure-ensemble-jupe-bordeaux", "L’ensemble", "L’Épure, jupe longue en coton."),
               ("laurore-tunique-longue-noir", "La silhouette", "L’Aurore, longue et lacée."),
               ("le-sillage-tunique-a-liens-beige", "Le détail", "Le Sillage, à superposer.")],
        mosaic=[("video", "sillage-beige"), ("img", IMG + "1A8A7D15-122C-4048-82A0-77A6BA283CD7.png"), ("img", IMG + "ACCEE1D3-76FD-4146-AD8B-9AA3AC0B0FB3.jpg")],
        h2b="Une histoire à suivre",
        pb="""Découvre <a href="{root}pages/notre-histoire/">notre histoire</a> et nos tissus choisis en Turquie. La Collection 02 arrive bientôt : rejoins la liste privée pour être la première informée."""),
}
