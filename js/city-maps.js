/* =====================================================
   VIVRE EN SUÈDE - Interactive City Maps (Leaflet.js)
   ===================================================== */

const CityMaps = {

  /* ---------- CONFIGURATION : 19 VILLES SUÉDOISES ---------- */
  cities: {

    stockholm: {
      center: [59.3293, 18.0686],
      zoom: 12,
      neighborhoods: [
        { name: 'Södermalm', lat: 59.3150, lng: 18.0710, badge: 'Tendance', price: '12 000-16 000 SEK' },
        { name: 'Östermalm', lat: 59.3380, lng: 18.0850, badge: 'Familial', price: '16 000-25 000 SEK' },
        { name: 'Vasastan', lat: 59.3450, lng: 18.0520, badge: 'Central', price: '13 000-18 000 SEK' },
        { name: 'Kungsholmen', lat: 59.3340, lng: 18.0350, badge: 'Familial', price: '11 000-15 000 SEK' },
        { name: 'Hammarby Sjöstad', lat: 59.3050, lng: 18.1000, badge: 'Émergent', price: '11 000-14 000 SEK' },
        { name: 'Gamla Stan', lat: 59.3258, lng: 18.0716, badge: 'Business', price: '14 000-20 000 SEK' }
      ]
    },

    goteborg: {
      center: [57.7089, 11.9746],
      zoom: 12,
      neighborhoods: [
        { name: 'Haga', lat: 57.6980, lng: 11.9550, badge: 'Tendance', price: '10 000-14 000 SEK' },
        { name: 'Linné', lat: 57.6950, lng: 11.9500, badge: 'Central', price: '9 000-13 000 SEK' },
        { name: 'Majorna', lat: 57.6920, lng: 11.9350, badge: 'Émergent', price: '8 000-11 000 SEK' },
        { name: 'Örgryte', lat: 57.7000, lng: 11.9950, badge: 'Familial', price: '9 000-13 000 SEK' },
        { name: 'Långedrag', lat: 57.6770, lng: 11.8950, badge: 'Familial', price: '11 000-16 000 SEK' },
        { name: 'Centrum', lat: 57.7089, lng: 11.9746, badge: 'Business', price: '10 000-15 000 SEK' }
      ]
    },

    malmo: {
      center: [55.6050, 13.0038],
      zoom: 13,
      neighborhoods: [
        { name: 'Västra Hamnen', lat: 55.6150, lng: 12.9780, badge: 'Tendance', price: '10 000-15 000 SEK' },
        { name: 'Möllevången', lat: 55.5920, lng: 13.0020, badge: 'Émergent', price: '7 000-10 000 SEK' },
        { name: 'Limhamn', lat: 55.5830, lng: 12.9380, badge: 'Familial', price: '9 000-13 000 SEK' },
        { name: 'Davidshall', lat: 55.5970, lng: 13.0000, badge: 'Central', price: '9 000-13 000 SEK' },
        { name: 'Ribersborg', lat: 55.6020, lng: 12.9800, badge: 'Familial', price: '9 000-12 000 SEK' },
        { name: 'Gamla Staden', lat: 55.6050, lng: 13.0000, badge: 'Business', price: '10 000-14 000 SEK' }
      ]
    },

    uppsala: {
      center: [59.8586, 17.6389],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 59.8586, lng: 17.6389, badge: 'Central', price: '9 000-13 000 SEK' },
        { name: 'Luthagen', lat: 59.8650, lng: 17.6250, badge: 'Familial', price: '9 000-12 000 SEK' },
        { name: 'Fålhagen', lat: 59.8600, lng: 17.6550, badge: 'Émergent', price: '8 000-11 000 SEK' },
        { name: 'Sunnersta', lat: 59.8350, lng: 17.6300, badge: 'Familial', price: '7 500-10 000 SEK' },
        { name: 'Eriksberg', lat: 59.8750, lng: 17.6200, badge: 'Familial', price: '8 000-11 000 SEK' },
        { name: 'Svartbäcken', lat: 59.8620, lng: 17.6500, badge: 'Universitaire', price: '7 000-10 000 SEK' }
      ]
    },

    linkoping: {
      center: [58.4108, 15.6214],
      zoom: 13,
      neighborhoods: [
        { name: 'Innerstaden', lat: 58.4108, lng: 15.6214, badge: 'Central', price: '8 000-12 000 SEK' },
        { name: 'Ryd', lat: 58.3950, lng: 15.5750, badge: 'Universitaire', price: '5 500-8 000 SEK' },
        { name: 'Lambohov', lat: 58.3900, lng: 15.6400, badge: 'Familial', price: '7 000-10 000 SEK' },
        { name: 'Hjulsbro', lat: 58.3800, lng: 15.6100, badge: 'Familial', price: '7 500-10 000 SEK' },
        { name: 'Tornby', lat: 58.4250, lng: 15.6100, badge: 'Moderne', price: '6 500-9 000 SEK' },
        { name: 'Ekholmen', lat: 58.3950, lng: 15.6500, badge: 'Familial', price: '6 000-8 500 SEK' }
      ]
    },

    vasteras: {
      center: [59.6162, 16.5528],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 59.6162, lng: 16.5528, badge: 'Central', price: '7 000-10 000 SEK' },
        { name: 'Öster Mälarstrand', lat: 59.6100, lng: 16.5800, badge: 'Moderne', price: '8 000-11 000 SEK' }
      ]
    },

    orebro: {
      center: [59.2753, 15.2134],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 59.2753, lng: 15.2134, badge: 'Central', price: '7 000-10 000 SEK' },
        { name: 'Wadköping', lat: 59.2700, lng: 15.2250, badge: 'Historique', price: '7 500-10 500 SEK' }
      ]
    },

    norrkoping: {
      center: [58.5942, 16.1826],
      zoom: 13,
      neighborhoods: [
        { name: 'Industrilandskapet', lat: 58.5942, lng: 16.1826, badge: 'Central', price: '6 500-9 000 SEK' },
        { name: 'Kneippen', lat: 58.5900, lng: 16.1700, badge: 'Résidentiel', price: '6 000-8 500 SEK' }
      ]
    },

    helsingborg: {
      center: [56.0465, 12.6945],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 56.0465, lng: 12.6945, badge: 'Central', price: '8 000-12 000 SEK' },
        { name: 'Söder', lat: 56.0380, lng: 12.7050, badge: 'Familial', price: '7 500-10 500 SEK' }
      ]
    },

    jonkoping: {
      center: [57.7826, 14.1618],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 57.7826, lng: 14.1618, badge: 'Central', price: '7 000-10 000 SEK' },
        { name: 'Huskvarna', lat: 57.7860, lng: 14.2600, badge: 'Résidentiel', price: '6 500-9 000 SEK' }
      ]
    },

    umea: {
      center: [63.8258, 20.2630],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 63.8258, lng: 20.2630, badge: 'Central', price: '7 000-10 000 SEK' },
        { name: 'Ålidhem', lat: 63.8200, lng: 20.3000, badge: 'Universitaire', price: '5 500-8 000 SEK' }
      ]
    },

    lund: {
      center: [55.7047, 13.1910],
      zoom: 14,
      neighborhoods: [
        { name: 'Centrum', lat: 55.7047, lng: 13.1910, badge: 'Central', price: '8 000-12 000 SEK' },
        { name: 'Lund Öster', lat: 55.7080, lng: 13.2100, badge: 'Universitaire', price: '7 000-10 000 SEK' }
      ]
    },

    gavle: {
      center: [60.6749, 17.1413],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 60.6749, lng: 17.1413, badge: 'Central', price: '6 000-9 000 SEK' },
        { name: 'Söder', lat: 60.6680, lng: 17.1500, badge: 'Résidentiel', price: '5 500-8 000 SEK' }
      ]
    },

    karlstad: {
      center: [59.3793, 13.5036],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 59.3793, lng: 13.5036, badge: 'Central', price: '6 500-9 500 SEK' },
        { name: 'Rud', lat: 59.3750, lng: 13.5300, badge: 'Familial', price: '6 000-8 500 SEK' }
      ]
    },

    sundsvall: {
      center: [62.3908, 17.3069],
      zoom: 13,
      neighborhoods: [
        { name: 'Stenstaden', lat: 62.3908, lng: 17.3069, badge: 'Central', price: '6 500-9 500 SEK' },
        { name: 'Nacksta', lat: 62.3850, lng: 17.2900, badge: 'Résidentiel', price: '5 500-8 000 SEK' }
      ]
    },

    vaxjo: {
      center: [56.8777, 14.8091],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 56.8777, lng: 14.8091, badge: 'Central', price: '6 000-9 000 SEK' },
        { name: 'Söder', lat: 56.8700, lng: 14.8200, badge: 'Familial', price: '5 500-8 000 SEK' }
      ]
    },

    halmstad: {
      center: [56.6745, 12.8578],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 56.6745, lng: 12.8578, badge: 'Central', price: '7 000-10 000 SEK' },
        { name: 'Tylösand', lat: 56.6500, lng: 12.7300, badge: 'Plages', price: '8 000-12 000 SEK' }
      ]
    },

    boras: {
      center: [57.7210, 12.9401],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 57.7210, lng: 12.9401, badge: 'Central', price: '6 000-9 000 SEK' },
        { name: 'Norrby', lat: 57.7250, lng: 12.9300, badge: 'Résidentiel', price: '5 500-8 000 SEK' }
      ]
    },

    eskilstuna: {
      center: [59.3712, 16.5100],
      zoom: 13,
      neighborhoods: [
        { name: 'Centrum', lat: 59.3712, lng: 16.5100, badge: 'Central', price: '6 000-9 000 SEK' },
        { name: 'ReTuna-kvarteret', lat: 59.3680, lng: 16.5200, badge: 'Moderne', price: '5 500-8 000 SEK' }
      ]
    }
  },

  /* ---------- STATE ---------- */
  map: null,
  markers: [],
  activeMarkerIndex: null,

  /* ---------- COLORS for marker badges ---------- */
  badgeColors: {
    'Central': '#1E3A5F',
    'Familial': '#2D5016',
    'Tendance': '#C1272D',
    'Abordable': '#48752B',
    'Nature': '#2D5016',
    'Moderne': '#4299E1',
    'Historique': '#8B6914',
    'Universitaire': '#6B46C1',
    'Étudiant': '#6B46C1',
    'Résidentiel': '#1E3A5F',
    'Émergent': '#ECC94B',
    'Business': '#4A5568',
    'Plages': '#4299E1'
  },

  /* ---------- INIT ---------- */
  init: function() {
    var mapContainer = document.querySelector('.city-map');
    if (!mapContainer) return;

    var cityKey = mapContainer.getAttribute('data-city');
    if (!cityKey || !this.cities[cityKey]) return;

    // Remove placeholder
    var placeholder = mapContainer.querySelector('.city-map-placeholder');
    if (placeholder) placeholder.remove();

    // Create Leaflet container
    var mapDiv = document.createElement('div');
    mapDiv.id = 'city-leaflet-map';
    mapDiv.style.width = '100%';
    mapDiv.style.height = '100%';
    mapDiv.style.borderRadius = 'inherit';
    mapContainer.appendChild(mapDiv);

    this.createMap(cityKey, mapDiv);
    this.bindCardInteractions();
  },

  /* ---------- CREATE MAP ---------- */
  createMap: function(cityKey, container) {
    var city = this.cities[cityKey];

    this.map = L.map(container.id, {
      center: city.center,
      zoom: city.zoom,
      scrollWheelZoom: false,
      zoomControl: true
    });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      maxZoom: 18
    }).addTo(this.map);

    this.addMarkers(city);

    // Fit bounds to show all markers
    if (this.markers.length > 0) {
      var group = L.featureGroup(this.markers);
      this.map.fitBounds(group.getBounds().pad(0.15));
    }
  },

  /* ---------- CUSTOM ICON ---------- */
  createIcon: function(active) {
    var cls = active ? 'custom-map-marker map-marker-active' : 'custom-map-marker';
    return L.divIcon({
      className: cls,
      html: '<div class="map-marker-pin"><div class="map-marker-dot"></div></div>',
      iconSize: [32, 42],
      iconAnchor: [16, 42],
      popupAnchor: [0, -44]
    });
  },

  /* ---------- ADD MARKERS ---------- */
  addMarkers: function(city) {
    var self = this;

    city.neighborhoods.forEach(function(hood, index) {
      var marker = L.marker([hood.lat, hood.lng], {
        icon: self.createIcon(false)
      }).addTo(self.map);

      // Popup content
      var badgeColor = self.badgeColors[hood.badge] || '#1E3A5F';
      var popupHTML =
        '<div class="map-popup">' +
          '<h4 class="map-popup-title">' + hood.name + '</h4>' +
          '<span class="map-popup-badge" style="background-color:' + badgeColor + '22; color:' + badgeColor + ';">' + hood.badge + '</span>' +
          '<span class="map-popup-price">' + hood.price + '</span>' +
        '</div>';

      marker.bindPopup(popupHTML, {
        className: 'custom-leaflet-popup',
        maxWidth: 240,
        closeButton: true
      });

      // On marker click: highlight corresponding card
      marker.on('click', function() {
        self.highlightCard(index);
        self.setActiveMarker(index);
      });

      self.markers.push(marker);
    });
  },

  /* ---------- BIND CARD INTERACTIONS ---------- */
  bindCardInteractions: function() {
    var self = this;
    var cards = document.querySelectorAll('.neighborhoods-grid .neighborhood-card');

    cards.forEach(function(card, index) {
      card.addEventListener('click', function(e) {
        if (e.target.tagName === 'A') return;

        if (self.markers[index]) {
          self.map.setView(self.markers[index].getLatLng(), self.map.getZoom(), {
            animate: true
          });
          self.markers[index].openPopup();
          self.setActiveMarker(index);

          var mapEl = document.querySelector('.city-map');
          if (mapEl) {
            mapEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
      });
    });
  },

  /* ---------- HIGHLIGHT CARD ---------- */
  highlightCard: function(index) {
    var cards = document.querySelectorAll('.neighborhoods-grid .neighborhood-card');

    cards.forEach(function(c) {
      c.classList.remove('neighborhood-card-active');
    });

    if (cards[index]) {
      cards[index].classList.add('neighborhood-card-active');
      cards[index].scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  },

  /* ---------- SET ACTIVE MARKER ---------- */
  setActiveMarker: function(index) {
    if (this.activeMarkerIndex !== null && this.activeMarkerIndex !== index && this.markers[this.activeMarkerIndex]) {
      this.markers[this.activeMarkerIndex].setIcon(this.createIcon(false));
    }

    if (this.markers[index]) {
      this.markers[index].setIcon(this.createIcon(true));
    }

    this.activeMarkerIndex = index;
  }
};

/* ---------- INITIALIZE ON DOM READY ---------- */
document.addEventListener('DOMContentLoaded', function() {
  CityMaps.init();
});
