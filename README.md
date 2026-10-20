# ELYA Collection — site de démonstration

Maquette du futur site elyacollection.com : direction artistique ELYA, nouvelles pages SEO, blog. Elle sert à valider le rendu avant l'intégration dans Shopify.

- Non indexée (`robots.txt` + balise `noindex` sur chaque page) pour ne pas concurrencer le vrai site.
- Les photos produits sont chargées depuis le CDN Shopify d'ELYA.
- Panier, recherche et inscription sont simulés.

## Contenu

| Dossier | Pages |
|---|---|
| `/` | Accueil |
| `collections/` | Tuniques longues femme, Ensembles modestes, Tenue femme voilée chic, L'Aube |
| `products/` | 11 fiches produits (nouvelles adresses SEO) |
| `pages/` | Guide des tailles, Notre histoire, Nos matières, FAQ, Livraison et retours, Contact, Mentions légales, CGV |
| `blogs/conseils/` | 5 articles de conseils |

La liste complète est dans `plan-du-site.txt`.

## Modifier et régénérer

Les textes sont dans `_src/site_content.py` (produits, collections, pages) et `_src/blog_content.py` (articles). Le design est dans `assets/elya.css`.

```
python -I _src/build.py
python -I _src/check_links.py
```

## Intégration dans Shopify

- Textes, titres SEO, méta-descriptions, textes alternatifs et adresses : à saisir dans l'admin Shopify (produits, collections, pages, blog), avec une redirection 301 pour chaque ancienne adresse produit.
- Design (couleurs, typographies, blocs de texte, FAQ, guide des tailles) : à reproduire dans une copie du thème Atelier reliée à GitHub.
