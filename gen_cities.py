#!/usr/bin/env python3
"""Generate 7 Swedish city HTML pages for vivre-en-suede."""
import os

BASE = '/Users/matteo-orsini/Desktop/Claude code/vivre-en-suede/pages/villes'

NAV = '''  <!-- HEADER -->
  <header class="header">
    <div class="header-container">
      <a href="/" class="header-logo"><span class="header-logo-text">🇸🇪 Vivre en <span>Suède</span></span></a>
      <nav class="main-nav">
        <ul>
          <li class="nav-mega-dropdown">
            <a href="/pages/preparer-depart/">Guides pratiques</a>
            <div class="nav-mega-menu">
              <div class="nav-mega-column">
                <span class="nav-mega-title">S'installer</span>
                <a href="/pages/preparer-depart/">Préparer son départ</a>
                <a href="/pages/preparer-depart/compte-bancaire/">Ouvrir un compte bancaire</a>
                <a href="/pages/preparer-depart/personnummer/">Obtenir le Personnummer</a>
                <a href="/pages/preparer-depart/logement/">Trouver un logement</a>
                <a href="/pages/preparer-depart/demenagement/">Déménagement</a>
                <a href="/pages/preparer-depart/travail/">Travailler en Suède</a>
                <a href="/pages/preparer-depart/creation-entreprise/">Création d'entreprise</a>
              </div>
              <div class="nav-mega-column">
                <span class="nav-mega-title">Vie quotidienne</span>
                <a href="/pages/cout-vie/">Coût de la vie</a>
                <a href="/pages/fiscalite/">Fiscalité</a>
                <a href="/pages/sante/">Santé</a>
                <a href="/pages/education/">Éducation</a>
              </div>
            </div>
          </li>
          <li class="nav-dropdown">
            <a href="/pages/villes/" class="active">Villes</a>
            <div class="nav-dropdown-menu">
              <a href="/pages/villes/stockholm/">Stockholm</a>
              <a href="/pages/villes/goteborg/">Göteborg</a>
              <a href="/pages/villes/malmo/">Malmö</a>
              <a href="/pages/villes/uppsala/">Uppsala</a>
              <a href="/pages/villes/linkoping/">Linköping</a>
              <a href="/pages/villes/">Toutes les villes →</a>
            </div>
          </li>
          <li class="nav-dropdown">
            <a href="/pages/outils/">Outils</a>
            <div class="nav-dropdown-menu">
              <a href="/pages/outils/convertisseur/">Convertisseur EUR/SEK</a>
              <a href="/pages/outils/ansokan/">Générateur d'Ansökan</a>
              <a href="/pages/outils/budget/">Simulateur de budget</a>
              <a href="/pages/outils/quiz/">Quiz : Où vivre ?</a>
            </div>
          </li>
          <li><a href="/pages/a-propos/">À propos</a></li>
        </ul>
      </nav>
      <a href="/pages/outils/quiz/" class="btn btn-primary btn-sm header-cta">Quiz : Ma ville idéale</a>
      <button class="mobile-menu-toggle" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
    </div>
  </header>

  <div class="mobile-menu" id="mobileMenu">
    <button class="mobile-menu-close" aria-label="Fermer le menu">&times;</button>
    <ul>
      <li class="mobile-nav-group">
        <button class="mobile-nav-toggle">Guides pratiques <span class="mobile-nav-arrow">›</span></button>
        <ul class="mobile-nav-sub">
          <li class="mobile-nav-subtitle">S'installer</li>
          <li><a href="/pages/preparer-depart/">Préparer son départ</a></li>
          <li><a href="/pages/preparer-depart/compte-bancaire/">Compte bancaire</a></li>
          <li><a href="/pages/preparer-depart/personnummer/">Personnummer</a></li>
          <li><a href="/pages/preparer-depart/logement/">Logement</a></li>
          <li><a href="/pages/preparer-depart/demenagement/">Déménagement</a></li>
          <li><a href="/pages/preparer-depart/travail/">Travail</a></li>
          <li><a href="/pages/preparer-depart/creation-entreprise/">Création d'entreprise</a></li>
          <li class="mobile-nav-subtitle">Vie quotidienne</li>
          <li><a href="/pages/cout-vie/">Coût de la vie</a></li>
          <li><a href="/pages/fiscalite/">Fiscalité</a></li>
          <li><a href="/pages/sante/">Santé</a></li>
          <li><a href="/pages/education/">Éducation</a></li>
        </ul>
      </li>
      <li class="mobile-nav-group">
        <button class="mobile-nav-toggle">Villes <span class="mobile-nav-arrow">›</span></button>
        <ul class="mobile-nav-sub">
          <li><a href="/pages/villes/stockholm/">Stockholm</a></li>
          <li><a href="/pages/villes/goteborg/">Göteborg</a></li>
          <li><a href="/pages/villes/malmo/">Malmö</a></li>
          <li><a href="/pages/villes/uppsala/">Uppsala</a></li>
          <li><a href="/pages/villes/linkoping/">Linköping</a></li>
          <li><a href="/pages/villes/">Toutes les villes →</a></li>
        </ul>
      </li>
      <li class="mobile-nav-group">
        <button class="mobile-nav-toggle">Outils <span class="mobile-nav-arrow">›</span></button>
        <ul class="mobile-nav-sub">
          <li><a href="/pages/outils/convertisseur/">Convertisseur EUR/SEK</a></li>
          <li><a href="/pages/outils/ansokan/">Générateur d'Ansökan</a></li>
          <li><a href="/pages/outils/budget/">Simulateur de budget</a></li>
          <li><a href="/pages/outils/quiz/">Quiz : Où vivre ?</a></li>
        </ul>
      </li>
      <li><a href="/pages/a-propos/">À propos</a></li>
      <li><a href="/pages/outils/quiz/">Quiz : Ma ville idéale</a></li>
    </ul>
  </div>'''

FOOTER = '''  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <span class="header-logo-text">🇸🇪 Vivre en <span>Suède</span></span>
          <p>Le guide complet pour réussir votre expatriation.</p>
        </div>
        <div>
          <h4 class="footer-title">Villes</h4>
          <ul class="footer-links">
            <li><a href="/pages/villes/stockholm/">Stockholm</a></li>
            <li><a href="/pages/villes/goteborg/">Göteborg</a></li>
            <li><a href="/pages/villes/malmo/">Malmö</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-title">Outils</h4>
          <ul class="footer-links">
            <li><a href="/pages/outils/convertisseur/">Convertisseur</a></li>
            <li><a href="/pages/outils/budget/">Simulateur</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-title">À propos</h4>
          <ul class="footer-links">
            <li><a href="/pages/outils/quiz/">Quiz : Ma ville idéale</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 Vivre en Suède</p>
      </div>
    </div>
  </footer>'''


def make_page(d):
    qhtml = ''
    for q in d['quartiers']:
        tags = ''.join(f'<span class="badge badge-{t[0]}">{t[1]}</span>' for t in q['tags'])
        qhtml += f'''
              <div class="neighborhood-card" data-lat="{q['lat']}" data-lng="{q['lng']}">
                <div class="neighborhood-card-body">
                  <h4>{q['name']}</h4>
                  <p>{q['desc']}</p>
                  <div class="neighborhood-tags">{tags}</div>
                </div>
              </div>'''
    crows = '\n                '.join(f'<tr><td>{c[0]}</td><td class="price">{c[1]}</td><td class="price-comparison lower">{c[2]}</td></tr>' for c in d['cout'])
    pros = '\n                  '.join(f'<li>{p}</li>' for p in d['pros'])
    cons = '\n                  '.join(f'<li>{c}</li>' for c in d['cons'])
    slinks = '\n              '.join(f'<li style="margin-bottom: var(--space-2);"><a href="/pages/villes/{s[0]}/">{s[1]}</a></li>' for s in d['sidebar'])
    mdata = ',\n        '.join(f"{{ name: '{q['name']}', lat: {q['lat']}, lng: {q['lng']}, desc: '{q['mdesc']}' }}" for q in d['quartiers'])

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="https://www.vivre-en-suede.com/pages/villes/{d['slug']}/" />
  <meta name="description" content="{d['meta']}">
  <title>Vivre à {d['name']} - Guide expatrié | Vivre en Suède</title>
  <link rel="stylesheet" href="/css/main.css">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
</head>
<body>

{NAV}

  <!-- HERO -->
  <section class="hero-mini">
    <div class="container">
      <div class="hero-content">
        <nav class="breadcrumb">
          <a href="/">Accueil</a>
          <span class="breadcrumb-separator">&rsaquo;</span>
          <a href="/pages/villes/">Villes</a>
          <span class="breadcrumb-separator">&rsaquo;</span>
          <span class="breadcrumb-current">{d['name']}</span>
        </nav>
        <h1 class="hero-title">Vivre à {d['name']}</h1>
        <p class="hero-subtitle">{d['subtitle']}</p>
      </div>
    </div>
  </section>

  <!-- KEY STATS -->
  <section class="section">
    <div class="container">
      <div class="grid grid-4">
        <div class="card" style="text-align:center; padding: var(--space-6);">
          <span style="font-size: var(--text-3xl);">👥</span>
          <div style="font-size: var(--text-2xl); font-weight: var(--font-bold); color: var(--color-primary);">{d['pop']}</div>
          <div style="color: var(--color-text-muted); font-size: var(--text-sm);">Habitants</div>
        </div>
        <div class="card" style="text-align:center; padding: var(--space-6);">
          <span style="font-size: var(--text-3xl);">🌡️</span>
          <div style="font-size: var(--text-2xl); font-weight: var(--font-bold); color: var(--color-primary);">{d['temp']}</div>
          <div style="color: var(--color-text-muted); font-size: var(--text-sm);">Temp. min/max</div>
        </div>
        <div class="card" style="text-align:center; padding: var(--space-6);">
          <span style="font-size: var(--text-3xl);">💰</span>
          <div style="font-size: var(--text-2xl); font-weight: var(--font-bold); color: var(--color-primary);">{d['budget']}</div>
          <div style="color: var(--color-text-muted); font-size: var(--text-sm);">Budget mensuel (hors loyer)</div>
        </div>
        <div class="card" style="text-align:center; padding: var(--space-6);">
          <span style="font-size: var(--text-3xl);">🏠</span>
          <div style="font-size: var(--text-2xl); font-weight: var(--font-bold); color: var(--color-primary);">{d['loyer']}</div>
          <div style="color: var(--color-text-muted); font-size: var(--text-sm);">Loyer SEK/mois (T2)</div>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN CONTENT -->
  <section class="section section-alt">
    <div class="container">
      <div class="page-layout">

        <!-- SIDEBAR -->
        <aside class="toc-sidebar">
          <div class="toc">
            <h3 class="toc-title">Sommaire</h3>
            <ul class="toc-list">
              <li><a href="#presentation">Présentation</a></li>
              <li><a href="#quartiers">Quartiers</a></li>
              <li><a href="#carte">Carte interactive</a></li>
              <li><a href="#cout-vie">Coût de la vie</a></li>
              <li><a href="#emploi">Emploi</a></li>
              <li><a href="#transports">Transports</a></li>
              <li><a href="#avantages">Avantages et inconvénients</a></li>
              <li><a href="#avis">L\'avis d\'Ingrid</a></li>
            </ul>
          </div>
          <div class="card" style="padding: var(--space-5); margin-top: var(--space-6);">
            <h4 style="margin-bottom: var(--space-4);">Autres villes</h4>
            <ul style="list-style: none; padding: 0; margin: 0;">
              {slinks}
            </ul>
            <a href="/pages/villes/" class="btn btn-secondary btn-sm" style="margin-top: var(--space-4); width: 100%; text-align: center;">Toutes les villes</a>
          </div>
        </aside>

        <!-- ARTICLE CONTENT -->
        <article class="article-content">

          <section id="presentation">
            <h2>Présentation de {d['name']}</h2>
            {d['pres']}
          </section>

          <section id="quartiers">
            <h2>Les quartiers de {d['name']}</h2>
            <p>Découvrez les principaux quartiers pour choisir votre futur lieu de vie à {d['name']}.</p>
            <div class="neighborhoods-grid">{qhtml}
            </div>
          </section>

          <section id="carte">
            <h2>Carte interactive</h2>
            <p>Explorez les quartiers de {d['name']} sur la carte. Cliquez sur un marqueur pour plus d\'informations.</p>
            <div class="city-map">
              <div id="city-leaflet-map" style="height: 100%; width: 100%;"></div>
            </div>
          </section>

          <section id="cout-vie">
            <h2>Coût de la vie à {d['name']}</h2>
            <p>{d['cout_intro']}</p>
            <table class="price-table">
              <thead><tr><th>Dépense</th><th>Montant (SEK/mois)</th><th>vs Stockholm</th></tr></thead>
              <tbody>
                {crows}
              </tbody>
            </table>
          </section>

          <section id="emploi">
            <h2>Emploi et économie</h2>
            {d['emploi']}
          </section>

          <section id="transports">
            <h2>Transports</h2>
            {d['transports']}
          </section>

          <section id="avantages">
            <h2>Avantages et inconvénients</h2>
            <div class="pros-cons">
              <div class="pros-list">
                <h3>Avantages</h3>
                <ul>
                  {pros}
                </ul>
              </div>
              <div class="cons-list">
                <h3>Inconvénients</h3>
                <ul>
                  {cons}
                </ul>
              </div>
            </div>
          </section>

          <section id="avis">
            <h2>L\'avis d\'Ingrid</h2>
            <div class="callout callout-conseil">
              <div class="callout-title">Mon conseil</div>
              <p class="callout-content">{d['avis']}</p>
              <span class="signature">— Ingrid, expatriée à Stockholm depuis 2018</span>
            </div>
          </section>

        </article>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section">
    <div class="container container-md" style="text-align: center;">
      <h2>{d['name']} est-elle faite pour vous ?</h2>
      <p style="margin-bottom: var(--space-6);">Répondez à quelques questions pour découvrir quelle ville suédoise correspond le mieux à votre profil.</p>
      <a href="/pages/outils/quiz/" class="btn btn-primary btn-lg btn-arrow">Faire le quiz</a>
    </div>
  </section>

{FOOTER}

  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="/js/main.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      var map = L.map('city-leaflet-map').setView([{d['lat']}, {d['lng']}], 13);
      L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
        attribution: '&copy; OpenStreetMap contributors'
      }}).addTo(map);
      var quartiers = [
        {mdata}
      ];
      quartiers.forEach(function (q) {{
        var icon = L.divIcon({{
          className: 'custom-map-marker',
          html: '<div class="map-marker-pin"><div class="map-marker-dot"></div></div>',
          iconSize: [32, 40], iconAnchor: [16, 40], popupAnchor: [0, -42]
        }});
        L.marker([q.lat, q.lng], {{ icon: icon }}).addTo(map)
          .bindPopup('<div class="map-popup"><div class="map-popup-title">' + q.name + '</div><span class="map-popup-price">' + q.desc + '</span></div>', {{ className: 'custom-leaflet-popup' }});
      }});
    }});
  </script>
</body>
</html>'''


# ===== CITY DATA =====
cities = [
  {
    'slug': 'orebro', 'name': 'Örebro', 'pop': '155 000', 'temp': '-4° / 21°C', 'budget': '~9 000 SEK', 'loyer': '7 000-10 000', 'lat': 59.2753, 'lng': 15.2134,
    'meta': 'Guide complet pour vivre à Örebro en Suède : quartiers, coût de la vie, emploi, transports. Conseils pratiques d\'une expatriée.',
    'subtitle': 'Au coeur de la Suède, une ville à taille humaine entre nature et innovation industrielle',
    'sidebar': [('stockholm','Stockholm'),('goteborg','Göteborg'),('malmo','Malmö')],
    'pres': '<p>Örebro est une ville du centre de la Suède, capitale du comté d\'Örebro län, située au bord du lac Hjälmaren et de la rivière Svartån. Avec ses 155 000 habitants, elle figure parmi les plus grandes communes du pays. Sa position stratégique au carrefour des voies de communication suédoises, à mi-chemin entre Stockholm et Göteborg, en fait un centre logistique majeur.</p>\n            <p>Fondée au Moyen Âge autour de son imposant château (Örebro slott) sur un îlot de la Svartån, la ville est devenue un centre industriel au XIXe siècle avant de se tourner vers les hautes technologies et l\'enseignement supérieur. Le cadre de vie est remarquable avec le parc national de Tiveden à proximité, le lac Hjälmaren et de vastes forêts propices à la randonnée.</p>',
    'quartiers': [
      {'name':'Centrum','lat':59.2753,'lng':15.2134,'desc':'Coeur historique autour du château et de la Storgatan. Commerces, restaurants, vie culturelle.','tags':[('primary','Central'),('accent','Animé')],'mdesc':'Centre historique, château'},
      {'name':'Adolfsberg','lat':59.2900,'lng':15.1850,'desc':'Résidentiel prisé au nord-ouest, maisons individuelles et jardins. Idéal familles.','tags':[('success','Familial'),('secondary','Calme')],'mdesc':'Familial, maisons'},
      {'name':'Brickebacken','lat':59.2580,'lng':15.2400,'desc':'Au sud-est, proche du campus universitaire. Bonne desserte en transports.','tags':[('secondary','Résidentiel'),('primary','Université')],'mdesc':'Proche campus'},
      {'name':'Baronbackarna','lat':59.2650,'lng':15.1800,'desc':'Au sud-ouest du centre, loyers abordables et bonne connexion bus.','tags':[('accent','Abordable'),('secondary','Pratique')],'mdesc':'Abordable'},
      {'name':'Tybble','lat':59.2820,'lng':15.2250,'desc':'Au nord du centre, cadre verdoyant. Villas et appartements, jeunes actifs.','tags':[('success','Verdoyant'),('primary','Dynamique')],'mdesc':'Verdoyant'},
      {'name':'Vivalla','lat':59.2650,'lng':15.2550,'desc':'Grand quartier est, logements abordables. En pleine rénovation urbaine.','tags':[('accent','Économique'),('secondary','En rénovation')],'mdesc':'Économique'},
    ],
    'cout_intro': 'Örebro est sensiblement moins chère que Stockholm ou Göteborg. Les loyers sont modérés et les dépenses courantes restent raisonnables.',
    'cout': [('Loyer T2 centre','8 000 - 10 000','-30%'),('Loyer T2 périphérie','6 000 - 8 000','-35%'),('Transports (abonnement)','790','-10%'),('Courses alimentaires','3 500 - 4 500','-10%'),('Restaurant (repas moyen)','120 - 180','-15%'),('Salle de sport','300 - 400','-20%')],
    'emploi': '<p>L\'économie repose sur un tissu diversifié mêlant industrie, services et secteur public.</p>\n            <ul>\n              <li><strong>Epiroc</strong> : géant de l\'équipement minier, siège mondial à Örebro.</li>\n              <li><strong>Université d\'Örebro</strong> : 17 000 étudiants, recherche en robotique et IA.</li>\n              <li><strong>Logistique</strong> : hub central pour l\'e-commerce et la distribution.</li>\n              <li><strong>Secteur public</strong> : Région et commune, santé et éducation.</li>\n              <li><strong>Agroalimentaire</strong> : centre de production alimentaire régional.</li>\n            </ul>\n            <div class="callout callout-info"><div class="callout-title">Bon à savoir</div><p class="callout-content">Örebro est le "centre logistique de la Suède" grâce au croisement des autoroutes E18 et E20.</p></div>',
    'transports': '<p>Réseau bien organisé (Länstrafiken Örebro). Ville très cyclable.</p>\n            <ul>\n              <li><strong>Bus</strong> : réseau dense, fréquences 10-20 min.</li>\n              <li><strong>Train</strong> : Stockholm (2h), Göteborg (3h) via SJ et Mälartåg.</li>\n              <li><strong>Vélo</strong> : pistes cyclables excellentes dans toute la ville.</li>\n              <li><strong>Voiture</strong> : autoroutes E18/E20, stationnement abordable.</li>\n              <li><strong>Aéroport</strong> : Örebro Airport (ORB), Arlanda à 2h.</li>\n            </ul>',
    'pros': ['Coût de la vie nettement inférieur à Stockholm','Position centrale entre Stockholm et Göteborg (2-3h)','Ville très cyclable et à taille humaine','Nature accessible (lac Hjälmaren, parc national Tiveden)','Marché de l\'emploi dynamique (Epiroc, logistique)','Université reconnue avec vie étudiante active'],
    'cons': ['Offre culturelle moins riche que les grandes métropoles','Hivers froids (moyenne -4°C en janvier)','Communauté francophone très restreinte','Vie nocturne limitée hors du centre','Pas de vols internationaux directs'],
    'avis': 'Örebro est un excellent choix si vous cherchez la qualité de vie suédoise sans le prix de Stockholm. Le château au bord de l\'eau, les pistes cyclables impeccables et le marché de Saluhallen m\'ont charmée. Si vous travaillez dans l\'industrie ou la logistique, c\'est très pertinent. La communauté francophone est quasi inexistante, comptez sur les réseaux anglophones.',
  },
  {
    'slug': 'norrkoping', 'name': 'Norrköping', 'pop': '143 000', 'temp': '-3° / 21°C', 'budget': '~9 000 SEK', 'loyer': '6 500-9 500', 'lat': 58.5942, 'lng': 16.1826,
    'meta': 'Guide complet pour vivre à Norrköping en Suède : quartiers, patrimoine industriel, emploi et coût de la vie.',
    'subtitle': 'Une ville au riche patrimoine industriel reconvertie en centre culturel et universitaire',
    'sidebar': [('stockholm','Stockholm'),('linkoping','Linköping'),('goteborg','Göteborg')],
    'pres': '<p>Norrköping, surnommée la "Manchester de la Suède", est une ville d\'Östergötland célèbre pour son patrimoine industriel textile reconverti en quartier culturel vibrant. Avec 143 000 habitants, elle forme avec Linköping (à 45 km) un pôle économique majeur de l\'est suédois.</p>\n            <p>Le centre-ville est traversé par la rivière Motala ström dont les anciennes filatures ont été transformées en musées, restaurants et bureaux. Le campus de l\'Université de Linköping (LiU) à Norrköping accueille environ 8 000 étudiants, insufflant une énergie jeune à la ville. Le tramway historique, l\'un des rares en Suède, donne à Norrköping un charme unique.</p>',
    'quartiers': [
      {'name':'Centrum','lat':58.5942,'lng':16.1826,'desc':'Centre historique avec les usines reconverties. Vie culturelle riche, restaurants, boutiques.','tags':[('primary','Central'),('accent','Culturel')],'mdesc':'Centre, patrimoine industriel'},
      {'name':'Hageby','lat':58.5750,'lng':16.1700,'desc':'Grand quartier résidentiel au sud. Appartements abordables, bien desservi par le tramway.','tags':[('accent','Abordable'),('secondary','Tramway')],'mdesc':'Résidentiel, tramway'},
      {'name':'Navestad','lat':58.5680,'lng':16.1600,'desc':'Quartier au sud-ouest avec logements sociaux. Loyers parmi les plus bas de la ville.','tags':[('accent','Économique'),('secondary','Pratique')],'mdesc':'Économique'},
      {'name':'Borg','lat':58.6050,'lng':16.1500,'desc':'Au nord du centre, résidentiel calme avec maisons individuelles et espaces verts.','tags':[('success','Familial'),('secondary','Calme')],'mdesc':'Familial, calme'},
      {'name':'Ljura','lat':58.5850,'lng':16.2000,'desc':'À l\'est du centre, quartier verdoyant prisé. Proche du parc Himmelstalund.','tags':[('success','Verdoyant'),('primary','Prisé')],'mdesc':'Verdoyant, prisé'},
      {'name':'Klockaretorpet','lat':58.6100,'lng':16.2100,'desc':'Au nord-est, quartier résidentiel tranquille avec accès rapide à la nature.','tags':[('secondary','Résidentiel'),('success','Nature')],'mdesc':'Tranquille, nature'},
    ],
    'cout_intro': 'Norrköping offre un coût de la vie très attractif, parmi les plus bas des grandes villes suédoises.',
    'cout': [('Loyer T2 centre','7 500 - 9 500','-35%'),('Loyer T2 périphérie','5 500 - 7 500','-40%'),('Transports (abonnement)','780','-11%'),('Courses alimentaires','3 500 - 4 500','-10%'),('Restaurant (repas moyen)','110 - 170','-20%'),('Salle de sport','300 - 400','-20%')],
    'emploi': '<p>L\'économie de Norrköping s\'appuie sur une reconversion réussie de l\'industrie vers les services et la technologie.</p>\n            <ul>\n              <li><strong>Visualization Center C</strong> : centre de recherche en visualisation scientifique unique en Suède.</li>\n              <li><strong>Campus Norrköping (LiU)</strong> : 8 000 étudiants, spécialités en médias, culture et communication.</li>\n              <li><strong>Logistique</strong> : port important et centre de distribution.</li>\n              <li><strong>Industrie papetière</strong> : Holmen a son siège à Norrköping.</li>\n              <li><strong>Secteur public</strong> : commune et région, hôpital Vrinnevi.</li>\n            </ul>\n            <div class="callout callout-info"><div class="callout-title">Bon à savoir</div><p class="callout-content">Norrköping et Linköping forment ensemble un bassin d\'emploi de près de 300 000 habitants, avec un trajet de seulement 25 min en train entre les deux villes.</p></div>',
    'transports': '<p>Norrköping est l\'une des rares villes suédoises à posséder un réseau de tramway.</p>\n            <ul>\n              <li><strong>Tramway</strong> : 3 lignes traversant le centre-ville, unique en Suède avec Göteborg.</li>\n              <li><strong>Bus</strong> : réseau complémentaire couvrant tous les quartiers.</li>\n              <li><strong>Train</strong> : Stockholm (1h30), Linköping (25 min), Malmö (3h30) via SJ.</li>\n              <li><strong>Vélo</strong> : bonne infrastructure cyclable en développement.</li>\n              <li><strong>Aéroport</strong> : Norrköping Airport (NRK) avec vols domestiques, Arlanda à 2h.</li>\n            </ul>',
    'pros': ['Coût de la vie très attractif','Patrimoine industriel reconverti en quartier culturel unique','Tramway historique donnant du charme à la ville','Proximité de Linköping (25 min) et son bassin d\'emploi','Campus universitaire dynamique','Stockholm accessible en 1h30 par train'],
    'cons': ['Marché de l\'emploi plus restreint qu\'à Stockholm','Communauté francophone quasi inexistante','Offre culturelle limitée comparée aux grandes villes','Certains quartiers périphériques manquent de dynamisme','Hivers assez froids (-3°C en moyenne en janvier)'],
    'avis': 'Norrköping m\'a surpris par la beauté de son centre industriel reconverti. Les anciennes filatures transformées en restaurants et musées le long de la rivière sont magnifiques. C\'est une ville qui a su garder son âme tout en se modernisant. Le duo Norrköping-Linköping offre un bassin d\'emploi intéressant à prix très abordable. Parfait si vous aimez l\'histoire et les villes à caractère.',
  },
  {
    'slug': 'helsingborg', 'name': 'Helsingborg', 'pop': '150 000', 'temp': '-1° / 20°C', 'budget': '~9 500 SEK', 'loyer': '7 000-10 500', 'lat': 56.0465, 'lng': 12.6945,
    'meta': 'Guide complet pour vivre à Helsingborg en Suède : quartiers, proximité du Danemark, emploi et coût de la vie.',
    'subtitle': 'Aux portes du Danemark, une ville côtière dynamique entre Suède et Scandinavie',
    'sidebar': [('stockholm','Stockholm'),('malmo','Malmö'),('lund','Lund')],
    'pres': '<p>Helsingborg est une ville portuaire du sud de la Suède (Skåne), située sur le détroit de l\'Öresund face à la ville danoise d\'Helsingør. Avec 150 000 habitants, c\'est la deuxième ville de Scanie après Malmö. La traversée vers le Danemark ne prend que 20 minutes en ferry, faisant de Helsingborg une porte entre les deux pays.</p>\n            <p>La ville combine patrimoine historique (la forteresse Kärnan domine le centre) et modernité avec un front de mer rénové, une scène gastronomique en plein essor et un quartier d\'affaires dynamique. Le climat doux grâce à l\'influence maritime et la proximité de Copenhague en font un lieu de vie très agréable.</p>',
    'quartiers': [
      {'name':'Centrum','lat':56.0465,'lng':12.6945,'desc':'Centre historique autour de Kärnan et Stortorget. Front de mer, commerces, restaurants.','tags':[('primary','Central'),('accent','Maritime')],'mdesc':'Centre, front de mer'},
      {'name':'Söder','lat':56.0350,'lng':12.7000,'desc':'Quartier sud branché avec cafés, galeries et ambiance bohème. Populaire chez les jeunes.','tags':[('accent','Branché'),('primary','Jeune')],'mdesc':'Branché, bohème'},
      {'name':'Norr','lat':56.0600,'lng':12.6900,'desc':'Quartier nord résidentiel. Maisons, espaces verts et proximité de Pålsjö skog.','tags':[('success','Familial'),('secondary','Verdoyant')],'mdesc':'Familial, nature'},
      {'name':'Ramlösa','lat':56.0200,'lng':12.7200,'desc':'Au sud-est, quartier calme réputé pour ses sources. Maisons individuelles, ambiance paisible.','tags':[('success','Calme'),('secondary','Résidentiel')],'mdesc':'Calme, résidentiel'},
      {'name':'Fredriksdal','lat':56.0550,'lng':12.7200,'desc':'Quartier est avec le célèbre musée en plein air. Résidentiel familial et culturel.','tags':[('secondary','Culturel'),('success','Familial')],'mdesc':'Musée, familial'},
      {'name':'Laröd','lat':56.0800,'lng':12.6500,'desc':'Au nord sur la côte, quartier prisé avec villas et vue mer. Le plus huppé de la ville.','tags':[('primary','Prisé'),('accent','Vue mer')],'mdesc':'Villas, vue mer'},
    ],
    'cout_intro': 'Helsingborg est légèrement moins chère que Malmö et nettement plus abordable que Stockholm ou Göteborg.',
    'cout': [('Loyer T2 centre','8 000 - 10 500','-28%'),('Loyer T2 périphérie','6 000 - 8 000','-35%'),('Transports (abonnement)','830','-5%'),('Courses alimentaires','3 500 - 4 500','-10%'),('Restaurant (repas moyen)','120 - 180','-15%'),('Salle de sport','300 - 450','-15%')],
    'emploi': '<p>Helsingborg est un centre économique important du sud de la Suède avec un port parmi les plus actifs du pays.</p>\n            <ul>\n              <li><strong>IKEA</strong> : le siège d\'Inter IKEA est situé à Helsingborg (Älmhult pour le retail).</li>\n              <li><strong>Port de Helsingborg</strong> : l\'un des plus grands ports suédois, secteur maritime et logistique.</li>\n              <li><strong>Industrie alimentaire</strong> : Findus et plusieurs entreprises agroalimentaires.</li>\n              <li><strong>Commerce</strong> : centre commercial régional, services aux entreprises.</li>\n              <li><strong>Santé</strong> : Helsingborgs lasarett, important hôpital régional.</li>\n            </ul>\n            <div class="callout callout-info"><div class="callout-title">Bon à savoir</div><p class="callout-content">Certains résidents de Helsingborg travaillent au Danemark grâce au ferry rapide vers Helsingør (20 min). Les salaires danois étant plus élevés, c\'est un avantage notable pour les frontaliers.</p></div>',
    'transports': '<p>Helsingborg bénéficie d\'excellentes connexions grâce à sa position stratégique.</p>\n            <ul>\n              <li><strong>Ferry</strong> : traversée vers Helsingør (Danemark) en 20 min, départs toutes les 15 min.</li>\n              <li><strong>Train</strong> : Malmö (45 min), Lund (30 min), Göteborg (2h30), Stockholm (4h30) via SJ.</li>\n              <li><strong>Bus</strong> : réseau Skånetrafiken couvrant la ville et la région.</li>\n              <li><strong>Vélo</strong> : bonne infrastructure cyclable, ville compacte.</li>\n              <li><strong>Aéroport</strong> : Ängelholm-Helsingborg Airport (AGH) à 30 min, Copenhague Kastrup à 1h30.</li>\n            </ul>',
    'pros': ['Proximité du Danemark (ferry 20 min vers Helsingør)','Climat doux grâce à l\'influence maritime','Front de mer rénové et ambiance dynamique','IKEA et port créent un bassin d\'emploi diversifié','Accès rapide à Malmö, Lund et Copenhague','Scène gastronomique en plein essor'],
    'cons': ['Loyers en hausse dans les quartiers prisés','Moins d\'opportunités tech que Stockholm ou Malmö','Communauté francophone limitée','Vent marin parfois fort sur la côte','Aéroport local avec peu de destinations'],
    'avis': 'Helsingborg est une pépite méconnue. Le front de mer rénové est superbe, et la possibilité de prendre un ferry pour le Danemark en 20 minutes est un atout unique. La ville a une vraie identité, entre son patrimoine (Kärnan) et sa modernité. Si vous travaillez dans la logistique ou l\'agroalimentaire, c\'est un choix stratégique. Le climat doux du sud est un vrai plus par rapport au reste de la Suède.',
  },
  {
    'slug': 'jonkoping', 'name': 'Jönköping', 'pop': '145 000', 'temp': '-4° / 20°C', 'budget': '~9 000 SEK', 'loyer': '6 500-9 500', 'lat': 57.7826, 'lng': 14.1618,
    'meta': 'Guide complet pour vivre à Jönköping en Suède : quartiers, lac Vättern, emploi et coût de la vie.',
    'subtitle': 'Au bord du majestueux lac Vättern, une ville entrepreneuriale au coeur du Småland',
    'sidebar': [('stockholm','Stockholm'),('goteborg','Göteborg'),('linkoping','Linköping')],
    'pres': '<p>Jönköping est située à l\'extrémité sud du lac Vättern, le deuxième plus grand lac de Suède, au coeur de la province historique du Småland. Avec 145 000 habitants, c\'est la plus grande ville de la région et un important centre commercial et industriel.</p>\n            <p>La ville est réputée pour son esprit entrepreneurial, héritier de la tradition industrieuse du Småland (la même qui a donné naissance à IKEA). Le cadre naturel est exceptionnel avec les rives du Vättern, les forêts du Småland et le parc urbain de Stadsparken. Jönköping accueille également une université dynamique et la célèbre convention gaming DreamHack.</p>',
    'quartiers': [
      {'name':'Centrum','lat':57.7826,'lng':14.1618,'desc':'Centre-ville au bord du Vättern. Commerces, allumettmuseet, vie nocturne.','tags':[('primary','Central'),('accent','Lac')],'mdesc':'Centre, bord du lac'},
      {'name':'Huskvarna','lat':57.7900,'lng':14.2700,'desc':'Ville jumelle à l\'est, intégrée à la commune. Patrimoine industriel, accès direct au Vättern.','tags':[('secondary','Historique'),('primary','Industriel')],'mdesc':'Industriel, Vättern'},
      {'name':'Råslätt','lat':57.7500,'lng':14.1500,'desc':'Au sud du centre, quartier d\'appartements avec loyers abordables. Bien desservi.','tags':[('accent','Abordable'),('secondary','Pratique')],'mdesc':'Abordable'},
      {'name':'Torsvik','lat':57.7400,'lng':14.2000,'desc':'Zone résidentielle en développement au sud-est. Nouvelles constructions, familles.','tags':[('success','Neuf'),('primary','En développement')],'mdesc':'Neuf, familles'},
      {'name':'Norrahammar','lat':57.7200,'lng':14.1200,'desc':'Au sud, ancienne commune industrielle. Logements accessibles, cadre nature.','tags':[('accent','Accessible'),('success','Nature')],'mdesc':'Accessible, nature'},
      {'name':'Grästorp','lat':57.8000,'lng':14.1200,'desc':'Au nord-ouest, quartier résidentiel calme. Maisons individuelles, proche du Vättern.','tags':[('success','Calme'),('secondary','Résidentiel')],'mdesc':'Calme, résidentiel'},
    ],
    'cout_intro': 'Jönköping offre un coût de la vie modéré, typique des villes moyennes suédoises.',
    'cout': [('Loyer T2 centre','7 500 - 9 500','-32%'),('Loyer T2 périphérie','5 500 - 7 500','-38%'),('Transports (abonnement)','770','-12%'),('Courses alimentaires','3 500 - 4 500','-10%'),('Restaurant (repas moyen)','110 - 170','-18%'),('Salle de sport','300 - 400','-20%')],
    'emploi': '<p>Jönköping est reconnue pour son dynamisme entrepreneurial et son tissu de PME innovantes.</p>\n            <ul>\n              <li><strong>Husqvarna Group</strong> : le géant mondial de l\'outillage outdoor est basé à Huskvarna.</li>\n              <li><strong>Jönköping University</strong> : université internationale réputée en business et ingénierie.</li>\n              <li><strong>Science Park</strong> : pépinière d\'entreprises et startups technologiques.</li>\n              <li><strong>Commerce</strong> : centre régional avec Asecs, A6 Center et de nombreuses enseignes.</li>\n              <li><strong>Logistique</strong> : position centrale entre Stockholm, Göteborg et Malmö.</li>\n            </ul>\n            <div class="callout callout-info"><div class="callout-title">Bon à savoir</div><p class="callout-content">Jönköping accueille DreamHack, le plus grand festival de gaming et e-sport au monde. L\'événement attire des dizaines de milliers de visiteurs et contribue à l\'identité numérique de la ville.</p></div>',
    'transports': '<p>Jönköping est un noeud routier important du sud de la Suède.</p>\n            <ul>\n              <li><strong>Bus</strong> : réseau Jönköpings Länstrafik couvrant la ville et les environs.</li>\n              <li><strong>Train</strong> : Stockholm (3h30), Göteborg (2h30), Malmö (3h) via SJ.</li>\n              <li><strong>Voiture</strong> : autoroutes E4 (nord-sud) et Rv40 (est-ouest), position centrale.</li>\n              <li><strong>Vélo</strong> : pistes cyclables en développement, ville compacte.</li>\n              <li><strong>Aéroport</strong> : Jönköping Airport (JKG) avec quelques liaisons domestiques.</li>\n            </ul>',
    'pros': ['Cadre naturel exceptionnel au bord du lac Vättern','Esprit entrepreneurial dynamique (Husqvarna, Science Park)','Coût de la vie modéré','Université internationale reconnue','Position centrale entre les trois grandes villes','Communauté gaming avec DreamHack'],
    'cons': ['Transports en commun moins développés que dans les grandes villes','Hivers froids (-4°C en janvier)','Communauté internationale plus restreinte','Marché de l\'emploi dépendant des PME locales','Vie culturelle limitée hors saison estivale'],
    'avis': 'Jönköping est une ville qui séduit par son cadre naturel incroyable au bord du Vättern. Les couchers de soleil sur le lac sont parmi les plus beaux de Suède. L\'esprit entrepreneurial hérité du Småland se ressent partout. C\'est une ville qui convient particulièrement aux familles et à ceux qui aiment la nature au quotidien. Le réseau de PME offre des opportunités intéressantes si vous êtes dans le business ou l\'ingénierie.',
  },
  {
    'slug': 'umea', 'name': 'Umeå', 'pop': '130 000', 'temp': '-10° / 18°C', 'budget': '~9 000 SEK', 'loyer': '6 000-9 000', 'lat': 63.8258, 'lng': 20.2630,
    'meta': 'Guide complet pour vivre à Umeå en Suède : quartiers, vie universitaire, aurores boréales et coût de la vie.',
    'subtitle': 'Capitale culturelle du nord, une ville universitaire vibrante entre bouleaux et aurores boréales',
    'sidebar': [('stockholm','Stockholm'),('goteborg','Göteborg'),('uppsala','Uppsala')],
    'pres': '<p>Umeå est la plus grande ville du nord de la Suède (Norrland), située sur la côte du golfe de Botnie à la latitude du cercle polaire arctique. Avec 130 000 habitants, c\'est une métropole nordique dynamique, désignée Capitale européenne de la culture en 2014.</p>\n            <p>Surnommée "la ville des bouleaux" en raison des milliers d\'arbres plantés après le grand incendie de 1888, Umeå est avant tout une ville universitaire majeure avec l\'Université d\'Umeå (environ 34 000 étudiants) qui domine la vie locale. Malgré les hivers longs et rigoureux, la ville déborde d\'énergie culturelle avec ses festivals, théâtres et musées, notamment le Bildmuseet d\'art contemporain.</p>',
    'quartiers': [
      {'name':'Centrum','lat':63.8258,'lng':20.2630,'desc':'Centre-ville compact avec commerces, restaurants et vie culturelle. Animation étudiante.','tags':[('primary','Central'),('accent','Étudiant')],'mdesc':'Centre, animation'},
      {'name':'Ålidhem','lat':63.8150,'lng':20.3000,'desc':'Quartier étudiant principal proche du campus. Appartements abordables, ambiance jeune.','tags':[('accent','Étudiant'),('secondary','Abordable')],'mdesc':'Étudiant, campus'},
      {'name':'Ersboda','lat':63.8400,'lng':20.3200,'desc':'Au nord-est, quartier résidentiel avec maisons et appartements. Cadre nature, familles.','tags':[('success','Familial'),('secondary','Nature')],'mdesc':'Familial, nature'},
      {'name':'Mariehem','lat':63.8200,'lng':20.2300,'desc':'À l\'ouest du centre, quartier résidentiel calme. Maisons individuelles, espaces verts.','tags':[('success','Calme'),('secondary','Résidentiel')],'mdesc':'Calme, maisons'},
      {'name':'Tomtebo','lat':63.8050,'lng':20.2800,'desc':'Au sud du campus, éco-quartier en développement. Constructions neuves et durables.','tags':[('primary','Éco-quartier'),('success','Neuf')],'mdesc':'Éco-quartier, neuf'},
      {'name':'Berghem','lat':63.8350,'lng':20.2400,'desc':'Au nord-ouest, quartier résidentiel traditionnel. Bonne desserte bus, ambiance tranquille.','tags':[('secondary','Traditionnel'),('accent','Pratique')],'mdesc':'Traditionnel, tranquille'},
    ],
    'cout_intro': 'Umeå est l\'une des villes les plus abordables de Suède malgré sa taille et son dynamisme.',
    'cout': [('Loyer T2 centre','7 000 - 9 000','-35%'),('Loyer T2 périphérie','5 000 - 7 000','-42%'),('Transports (abonnement)','720','-18%'),('Courses alimentaires','3 500 - 4 500','-10%'),('Restaurant (repas moyen)','110 - 170','-18%'),('Salle de sport','300 - 400','-20%')],
    'emploi': '<p>L\'économie d\'Umeå est fortement liée à l\'université et au secteur public, mais se diversifie rapidement.</p>\n            <ul>\n              <li><strong>Université d\'Umeå</strong> : 34 000 étudiants, l\'un des plus grands employeurs du nord.</li>\n              <li><strong>Hôpital universitaire Norrlands</strong> : centre hospitalier de référence pour tout le nord.</li>\n              <li><strong>Technologies</strong> : écosystème tech en croissance avec Uminova Innovation.</li>\n              <li><strong>Design et culture</strong> : Capitale européenne de la culture 2014, secteur créatif dynamique.</li>\n              <li><strong>Industrie forestière</strong> : SCA et secteur papetier importants dans la région.</li>\n            </ul>\n            <div class="callout callout-info"><div class="callout-title">Bon à savoir</div><p class="callout-content">Umeå est la ville de Suède qui croît le plus vite proportionnellement à sa taille. L\'objectif municipal est d\'atteindre 200 000 habitants d\'ici 2050, ce qui se traduit par de nombreux projets d\'infrastructure et d\'emploi.</p></div>',
    'transports': '<p>Umeå dispose d\'un bon réseau de transports malgré sa localisation nordique.</p>\n            <ul>\n              <li><strong>Bus</strong> : réseau Ultra (Umeå Lokaltrafik) couvrant toute la ville, fréquences régulières.</li>\n              <li><strong>Train</strong> : Stockholm (6h via le train de nuit ou Botniabanan), Luleå (3h).</li>\n              <li><strong>Avion</strong> : Umeå Airport (UME) avec vols quotidiens vers Stockholm (1h), aéroport très proche du centre.</li>\n              <li><strong>Vélo</strong> : pistes cyclables même en hiver (déneigées), ville très plate.</li>\n              <li><strong>Ferry</strong> : liaison avec Vaasa en Finlande.</li>\n            </ul>',
    'pros': ['Ville universitaire vibrante avec 34 000 étudiants','Aurores boréales visibles en hiver','Coût de la vie très abordable','Capitale européenne de la culture 2014, scène culturelle riche','Aéroport proche du centre avec vols quotidiens vers Stockholm','Nature arctique spectaculaire (ski, randonnée, pêche)'],
    'cons': ['Hivers très longs et froids (-10°C en janvier, peu de lumière)','Éloignement géographique du sud de la Suède','Communauté francophone quasi inexistante','Marché de l\'emploi dominé par le secteur public','Adaptation nécessaire au climat nordique extrême'],
    'avis': 'Umeå est une surprise pour qui ne connaît pas le nord de la Suède. Malgré les hivers rigoureux, la ville bouillonne d\'énergie grâce à ses étudiants et sa scène culturelle. Les aurores boréales en hiver et le soleil de minuit en été sont des expériences inoubliables. Si vous acceptez le défi climatique, Umeå offre une qualité de vie exceptionnelle à un prix très doux. L\'aéroport à 5 minutes du centre compense l\'éloignement.',
  },
  {
    'slug': 'lund', 'name': 'Lund', 'pop': '125 000', 'temp': '-1° / 21°C', 'budget': '~10 000 SEK', 'loyer': '7 500-11 000', 'lat': 55.7047, 'lng': 13.1910,
    'meta': 'Guide complet pour vivre à Lund en Suède : quartiers, université historique, recherche et coût de la vie.',
    'subtitle': 'La ville universitaire millénaire, berceau de la recherche et de l\'innovation scandinave',
    'sidebar': [('stockholm','Stockholm'),('malmo','Malmö'),('helsingborg','Helsingborg')],
    'pres': '<p>Lund est l\'une des plus anciennes villes de Scandinavie, fondée vers l\'an 990, et abrite l\'Université de Lund (Lunds universitet), fondée en 1666, l\'une des plus prestigieuses d\'Europe du Nord. Avec 125 000 habitants dont environ 40 000 étudiants, la ville vit au rythme universitaire.</p>\n            <p>Le centre historique est un bijou architectural avec sa cathédrale romane du XIIe siècle, ses ruelles pavées et ses bâtiments médiévaux. Lund est aussi un pôle de recherche mondial avec les installations MAX IV et ESS (European Spallation Source), attirant des chercheurs du monde entier. La proximité de Malmö (15 min en train) et Copenhague (50 min) en fait un lieu de vie très connecté.</p>',
    'quartiers': [
      {'name':'Centrum','lat':55.7047,'lng':13.1910,'desc':'Centre historique autour de la cathédrale. Ruelles pavées, cafés, librairies, ambiance académique.','tags':[('primary','Historique'),('accent','Académique')],'mdesc':'Historique, cathédrale'},
      {'name':'Norra Fäladen','lat':55.7200,'lng':13.1800,'desc':'Au nord, grand quartier résidentiel. Appartements variés, proche des installations de recherche.','tags':[('secondary','Résidentiel'),('primary','Recherche')],'mdesc':'Résidentiel, recherche'},
      {'name':'Klostergården','lat':55.6950,'lng':13.1700,'desc':'Au sud-ouest, quartier calme et verdoyant. Populaire auprès des familles et chercheurs.','tags':[('success','Familial'),('secondary','Calme')],'mdesc':'Familial, calme'},
      {'name':'Linero','lat':55.6900,'lng':13.2200,'desc':'Au sud-est, quartier résidentiel abordable. Mélange d\'appartements et maisons.','tags':[('accent','Abordable'),('secondary','Mixte')],'mdesc':'Abordable, mixte'},
      {'name':'Östra Torn','lat':55.7100,'lng':13.2200,'desc':'À l\'est, quartier étudiant très prisé. Nations étudiantes, ambiance festive.','tags':[('accent','Étudiant'),('primary','Festif')],'mdesc':'Étudiant, festif'},
      {'name':'Stångby','lat':55.7400,'lng':13.1900,'desc':'Au nord, village en expansion intégré à Lund. Maisons neuves, calme rural aux portes de la ville.','tags':[('success','Rural'),('primary','Neuf')],'mdesc':'Rural, neuf'},
    ],
    'cout_intro': 'Lund est plus chère que la moyenne des villes suédoises de même taille en raison de la forte demande locative étudiante.',
    'cout': [('Loyer T2 centre','9 000 - 11 000','-22%'),('Loyer T2 périphérie','7 000 - 9 000','-28%'),('Transports (abonnement)','830','-5%'),('Courses alimentaires','3 500 - 4 500','-10%'),('Restaurant (repas moyen)','120 - 180','-15%'),('Salle de sport','350 - 450','-10%')],
    'emploi': '<p>L\'économie de Lund est dominée par l\'université et la recherche, mais l\'industrie technologique est très présente.</p>\n            <ul>\n              <li><strong>Université de Lund</strong> : 40 000 étudiants, 8 facultés, l\'un des plus gros employeurs du sud.</li>\n              <li><strong>MAX IV et ESS</strong> : installations de recherche de pointe attirant des scientifiques du monde entier.</li>\n              <li><strong>Sony Mobile / Axis Communications</strong> : pôle technologique avec de nombreuses entreprises.</li>\n              <li><strong>Medicon Village</strong> : parc scientifique dédié aux sciences de la vie.</li>\n              <li><strong>Ideon Science Park</strong> : l\'un des plus anciens parcs scientifiques de Suède, berceau de startups.</li>\n            </ul>\n            <div class="callout callout-info"><div class="callout-title">Bon à savoir</div><p class="callout-content">Lund abrite Ideon Science Park, fondé en 1983, où des entreprises comme Axis Communications et Bluetooth (Ericsson) ont vu le jour. C\'est un vivier d\'innovation permanente.</p></div>',
    'transports': '<p>Lund est parfaitement connectée grâce au réseau ferroviaire de Skåne.</p>\n            <ul>\n              <li><strong>Train</strong> : Malmö (15 min), Helsingborg (30 min), Copenhague (50 min), Stockholm (4h30).</li>\n              <li><strong>Bus</strong> : réseau Skånetrafiken couvrant la ville et la région.</li>\n              <li><strong>Vélo</strong> : LE moyen de transport à Lund, ville extrêmement cyclable.</li>\n              <li><strong>Lundalänken</strong> : projet de tramway/BRT reliant la gare au nord de la ville.</li>\n              <li><strong>Aéroport</strong> : Copenhague Kastrup à 50 min en train, Malmö Airport à 30 min.</li>\n            </ul>',
    'pros': ['Université de renommée mondiale et atmosphère académique unique','Installations de recherche de pointe (MAX IV, ESS)','Centre historique magnifique avec cathédrale millénaire','Climat doux du sud de la Suède','Malmö et Copenhague très accessibles','Écosystème tech et startup dynamique (Ideon)'],
    'cons': ['Loyers élevés à cause de la pression étudiante','Trouver un logement en première main est très difficile','Ville qui peut sembler petite après quelques mois','Vie nocturne concentrée sur les nations étudiantes','Communauté francophone restreinte'],
    'avis': 'Lund est ma ville préférée en dehors de Stockholm. L\'atmosphère est unique : un mélange de tradition millénaire et d\'innovation de pointe. Se promener dans les ruelles pavées autour de la cathédrale en automne est magique. Attention : trouver un logement est un vrai défi, inscrivez-vous sur les listes d\'attente dès que possible (AF Bostäder pour les étudiants, LKF pour les autres). Le vélo est roi ici, c\'est un mode de vie.',
  },
  {
    'slug': 'gavle', 'name': 'Gävle', 'pop': '103 000', 'temp': '-6° / 20°C', 'budget': '~8 500 SEK', 'loyer': '5 500-8 500', 'lat': 60.6749, 'lng': 17.1413,
    'meta': 'Guide complet pour vivre à Gävle en Suède : quartiers, patrimoine, le célèbre Gävlebocken et coût de la vie.',
    'subtitle': 'Ville historique du Norrland, célèbre pour son bouc de Noël géant et son patrimoine préservé',
    'sidebar': [('stockholm','Stockholm'),('uppsala','Uppsala'),('umea','Umeå')],
    'pres': '<p>Gävle est la porte d\'entrée du Norrland (nord de la Suède), située sur la côte du golfe de Botnie à environ 170 km au nord de Stockholm. Avec 103 000 habitants, c\'est la plus ancienne ville du Norrland, fondée en 1446.</p>\n            <p>La ville est mondialement connue pour le Gävlebocken, un immense bouc de paille érigé chaque décembre sur la place Slottstorget, devenu un phénomène médiatique international en raison de ses destructions récurrentes par le feu. Au-delà de cette curiosité, Gävle offre un patrimoine préservé avec le vieux quartier de Gamla Gefle (maisons en bois colorées), un port historique et une proximité avec la nature du Norrland. L\'Université de Gävle (Högskolan i Gävle) accueille environ 16 000 étudiants.</p>',
    'quartiers': [
      {'name':'Centrum','lat':60.6749,'lng':17.1413,'desc':'Centre-ville avec Stortorget, commerces, théâtre et vie culturelle. Appartements variés.','tags':[('primary','Central'),('accent','Culturel')],'mdesc':'Centre, culturel'},
      {'name':'Sätra','lat':60.6600,'lng':17.1700,'desc':'Au sud-est, quartier résidentiel avec appartements. Proche du centre, bien desservi.','tags':[('secondary','Résidentiel'),('accent','Proche centre')],'mdesc':'Résidentiel, proche'},
      {'name':'Brynäs','lat':60.6650,'lng':17.1600,'desc':'Quartier historique ouvrier au sud. En rénovation, ambiance authentique.','tags':[('secondary','Historique'),('accent','Authentique')],'mdesc':'Historique, ouvrier'},
      {'name':'Andersberg','lat':60.6500,'lng':17.1300,'desc':'Au sud-ouest, quartier d\'appartements avec loyers abordables. Vue sur la rivière Gavleån.','tags':[('accent','Abordable'),('secondary','Rivière')],'mdesc':'Abordable, rivière'},
      {'name':'Stigslund','lat':60.6850,'lng':17.1700,'desc':'Au nord-est, quartier résidentiel calme. Maisons individuelles, proche nature.','tags':[('success','Calme'),('secondary','Nature')],'mdesc':'Calme, nature'},
      {'name':'Bomhus','lat':60.6950,'lng':17.2100,'desc':'Au nord-est, ancien quartier industriel en reconversion. Logements accessibles.','tags':[('accent','Accessible'),('secondary','En reconversion')],'mdesc':'Accessible, reconversion'},
    ],
    'cout_intro': 'Gävle est l\'une des villes les plus abordables de Suède, avec des loyers nettement inférieurs à la moyenne nationale.',
    'cout': [('Loyer T2 centre','6 500 - 8 500','-40%'),('Loyer T2 périphérie','4 500 - 6 500','-48%'),('Transports (abonnement)','700','-20%'),('Courses alimentaires','3 000 - 4 000','-15%'),('Restaurant (repas moyen)','100 - 160','-25%'),('Salle de sport','250 - 350','-25%')],
    'emploi': '<p>L\'économie de Gävle mêle secteur public, industrie et services.</p>\n            <ul>\n              <li><strong>Högskolan i Gävle</strong> : l\'Université de Gävle, environ 16 000 étudiants et important employeur.</li>\n              <li><strong>Korsnäs / BillerudKorsnäs</strong> : industrie papetière et emballage, employeur historique.</li>\n              <li><strong>Lantmäteriet</strong> : l\'agence nationale de cartographie a son siège à Gävle.</li>\n              <li><strong>Secteur public</strong> : commune et région Gävleborg, hôpital de Gävle.</li>\n              <li><strong>Commerce et tourisme</strong> : centre régional avec Valbo Köpcentrum.</li>\n            </ul>\n            <div class="callout callout-info"><div class="callout-title">Bon à savoir</div><p class="callout-content">Le Gävlebocken (bouc de Gävle) est érigé chaque premier dimanche de l\'Avent depuis 1966. Il mesure 13 mètres de haut et est devenu une attraction touristique internationale, avec sa propre webcam en direct.</p></div>',
    'transports': '<p>Gävle est bien desservie grâce à sa position sur la ligne ferroviaire principale Stockholm-nord.</p>\n            <ul>\n              <li><strong>Train</strong> : Stockholm (1h30), Uppsala (45 min), Sundsvall (2h) via SJ.</li>\n              <li><strong>Bus</strong> : réseau X-trafik couvrant la ville et le comté de Gävleborg.</li>\n              <li><strong>Vélo</strong> : bonne infrastructure cyclable, ville à taille humaine.</li>\n              <li><strong>Voiture</strong> : E4 (nord-sud) et E16 (vers l\'ouest), accès facile.</li>\n              <li><strong>Aéroport</strong> : Gävle-Sandviken Airport pour vols locaux, Arlanda à 1h30 en train.</li>\n            </ul>',
    'pros': ['Coût de la vie parmi les plus bas de Suède','Stockholm accessible en 1h30 de train','Patrimoine préservé (Gamla Gefle, maisons en bois)','Le célèbre Gävlebocken, tradition unique au monde','Nature du Norrland à portée de main','Université dynamique avec 16 000 étudiants'],
    'cons': ['Marché de l\'emploi plus restreint','Hivers froids et longs (-6°C en janvier)','Communauté internationale limitée','Vie culturelle moins développée que dans les grandes villes','Éloignement des grandes métropoles hors Stockholm'],
    'avis': 'Gävle est un choix malin si vous cherchez l\'authenticité suédoise à petit prix. Le vieux quartier de Gamla Gefle avec ses maisons en bois colorées est un vrai décor de carte postale. Et bien sûr, vivre la tradition du Gävlebocken chaque décembre est une expérience unique. Stockholm est à seulement 1h30 de train, ce qui permet d\'y aller facilement pour le week-end. C\'est la ville idéale pour une vie tranquille dans le Norrland sans trop s\'éloigner de la civilisation.',
  },
]

for c in cities:
    html = make_page(c)
    path = os.path.join(BASE, f"{c['slug']}.html")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    lines = html.count('\n') + 1
    print(f"{c['slug']}.html: {lines} lines, {len(html)} bytes")

print("\nAll 7 city pages generated successfully!")
