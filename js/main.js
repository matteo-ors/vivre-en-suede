/* =====================================================
   VIVRE EN NORVÈGE - Main JavaScript
   ===================================================== */

document.addEventListener('DOMContentLoaded', function() {

  // ==========================================
  // MOBILE MENU
  // ==========================================
  const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileMenuClose = document.querySelector('.mobile-menu-close');

  if (mobileMenuToggle && mobileMenu) {
    mobileMenuToggle.addEventListener('click', () => {
      mobileMenu.classList.add('active');
      document.body.style.overflow = 'hidden';
    });

    if (mobileMenuClose) {
      mobileMenuClose.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
      });
    }

    // Close on click outside
    mobileMenu.addEventListener('click', (e) => {
      if (e.target === mobileMenu) {
        mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  // ==========================================
  // SMOOTH SCROLL FOR ANCHOR LINKS
  // ==========================================
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerOffset = 80;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });

        // Close mobile menu if open
        if (mobileMenu && mobileMenu.classList.contains('active')) {
          mobileMenu.classList.remove('active');
          document.body.style.overflow = '';
        }
      }
    });
  });

  // ==========================================
  // ACCORDION
  // ==========================================
  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const isActive = item.classList.contains('active');

      // Close all other items in the same accordion
      const accordion = item.parentElement;
      accordion.querySelectorAll('.accordion-item').forEach(i => {
        i.classList.remove('active');
      });

      // Toggle current item
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // ==========================================
  // TABS
  // ==========================================
  const tabBtns = document.querySelectorAll('.tab-btn');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.dataset.tab;
      const tabContainer = btn.closest('.tabs');

      // Update buttons
      tabContainer.querySelectorAll('.tab-btn').forEach(b => {
        b.classList.remove('active');
      });
      btn.classList.add('active');

      // Update content
      tabContainer.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
      });
      document.getElementById(tabId).classList.add('active');
    });
  });

  // ==========================================
  // CHECKLIST INTERACTIVE
  // ==========================================
  const checklistItems = document.querySelectorAll('.checklist-checkbox');

  checklistItems.forEach(checkbox => {
    checkbox.addEventListener('change', () => {
      const item = checkbox.closest('.checklist-item');
      if (checkbox.checked) {
        item.classList.add('checked');
      } else {
        item.classList.remove('checked');
      }

      // Save to localStorage
      const checklistId = checkbox.closest('.checklist').id;
      if (checklistId) {
        saveChecklistState(checklistId);
      }
    });
  });

  // Load saved checklist state
  function loadChecklistState(checklistId) {
    const saved = localStorage.getItem(`checklist_${checklistId}`);
    if (saved) {
      const checked = JSON.parse(saved);
      const checklist = document.getElementById(checklistId);
      if (checklist) {
        checklist.querySelectorAll('.checklist-checkbox').forEach((checkbox, index) => {
          if (checked[index]) {
            checkbox.checked = true;
            checkbox.closest('.checklist-item').classList.add('checked');
          }
        });
      }
    }
  }

  function saveChecklistState(checklistId) {
    const checklist = document.getElementById(checklistId);
    if (checklist) {
      const checked = [];
      checklist.querySelectorAll('.checklist-checkbox').forEach(checkbox => {
        checked.push(checkbox.checked);
      });
      localStorage.setItem(`checklist_${checklistId}`, JSON.stringify(checked));
    }
  }

  // Initialize checklists
  document.querySelectorAll('.checklist[id]').forEach(checklist => {
    loadChecklistState(checklist.id);
  });

  // ==========================================
  // TABLE OF CONTENTS - Active Section Tracking
  // ==========================================
  const toc = document.querySelector('.toc');
  if (toc) {
    const tocLinks = toc.querySelectorAll('a');
    const sections = [];

    tocLinks.forEach(link => {
      const targetId = link.getAttribute('href').slice(1);
      const section = document.getElementById(targetId);
      if (section) {
        sections.push({ link, section });
      }
    });

    function updateActiveTocLink() {
      const scrollPosition = window.scrollY + 100;

      let activeSection = sections[0];
      sections.forEach(({ link, section }) => {
        if (section.offsetTop <= scrollPosition) {
          activeSection = { link, section };
        }
      });

      tocLinks.forEach(link => link.classList.remove('active'));
      if (activeSection) {
        activeSection.link.classList.add('active');
      }
    }

    window.addEventListener('scroll', updateActiveTocLink);
    updateActiveTocLink();
  }

  // ==========================================
  // NEWSLETTER FORM
  // ==========================================
  const newsletterForms = document.querySelectorAll('.newsletter-form');

  newsletterForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const email = form.querySelector('input[type="email"]').value;
      const firstname = form.querySelector('input[name="firstname"]')?.value || '';

      // Here you would typically send to your email service
      // For now, just show a success message
      form.innerHTML = `
        <div style="text-align: center; padding: 20px;">
          <p style="font-size: 1.25rem; color: var(--color-white); margin-bottom: 10px;">🎉 Merci ${firstname} !</p>
          <p style="color: rgba(255,255,255,0.9);">Vérifiez votre boîte mail pour recevoir votre guide gratuit.</p>
        </div>
      `;
    });
  });

  // ==========================================
  // SCROLL TO TOP BUTTON
  // ==========================================
  const scrollTopBtn = document.getElementById('scrollTopBtn');

  if (scrollTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 500) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    });

    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // ==========================================
  // LAZY LOADING IMAGES
  // ==========================================
  if ('loading' in HTMLImageElement.prototype) {
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
      img.src = img.dataset.src;
    });
  } else {
    // Fallback for browsers that don't support lazy loading
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
    document.body.appendChild(script);
  }

  // ==========================================
  // DROPDOWN MENUS - TOUCH DEVICES
  // ==========================================
  const dropdowns = document.querySelectorAll('.nav-dropdown, .nav-mega-dropdown');

  dropdowns.forEach(dropdown => {
    const link = dropdown.querySelector('a');

    link.addEventListener('click', (e) => {
      if (window.innerWidth >= 1024) {
        // On desktop, allow navigation
        return;
      }

      // On mobile, toggle dropdown
      e.preventDefault();
      dropdown.classList.toggle('active');
    });
  });

  // ==========================================
  // MOBILE MENU - ACCORDION GROUPS
  // ==========================================
  const mobileNavToggles = document.querySelectorAll('.mobile-nav-toggle');

  mobileNavToggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
      const group = toggle.parentElement;
      const isActive = group.classList.contains('active');

      // Close all other groups (accordion behavior)
      document.querySelectorAll('.mobile-nav-group.active').forEach(g => {
        if (g !== group) g.classList.remove('active');
      });

      // Toggle current group
      group.classList.toggle('active', !isActive);
    });
  });

  // ==========================================
  // PRINT FUNCTIONALITY FOR CHECKLISTS
  // ==========================================
  const printBtns = document.querySelectorAll('.print-checklist');

  printBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const checklistId = btn.dataset.checklist;
      const checklist = document.getElementById(checklistId);

      if (checklist) {
        const printWindow = window.open('', '_blank');
        printWindow.document.write(`
          <!DOCTYPE html>
          <html>
          <head>
            <title>Checklist - Vivre en Suède</title>
            <style>
              body { font-family: Arial, sans-serif; padding: 20px; }
              h2 { color: #1E3A5F; }
              ul { list-style: none; padding: 0; }
              li { padding: 10px 0; border-bottom: 1px solid #eee; }
              li::before { content: '☐ '; }
            </style>
          </head>
          <body>
            <h2>Checklist - Vivre en Suède</h2>
            ${checklist.outerHTML}
          </body>
          </html>
        `);
        printWindow.document.close();
        printWindow.print();
      }
    });
  });

});

// ==========================================
// CURRENCY CONVERTER
// ==========================================
const CurrencyConverter = {
  rate: 11.5, // Default EUR to SEK rate

  init: function() {
    const converter = document.querySelector('.converter');
    if (!converter) return;

    const eurInput = document.getElementById('eurInput');
    const nokInput = document.getElementById('nokInput');
    const swapBtn = document.querySelector('.converter-swap');

    if (eurInput && nokInput) {
      eurInput.addEventListener('input', () => this.convert('eur'));
      nokInput.addEventListener('input', () => this.convert('nok'));
    }

    if (swapBtn) {
      swapBtn.addEventListener('click', () => this.swap());
    }

    // Fetch live rate (simulated)
    this.fetchRate();
  },

  convert: function(from) {
    const eurInput = document.getElementById('eurInput');
    const nokInput = document.getElementById('nokInput');

    if (from === 'eur') {
      const eur = parseFloat(eurInput.value) || 0;
      nokInput.value = (eur * this.rate).toFixed(2);
    } else {
      const nok = parseFloat(nokInput.value) || 0;
      eurInput.value = (nok / this.rate).toFixed(2);
    }
  },

  swap: function() {
    const eurInput = document.getElementById('eurInput');
    const nokInput = document.getElementById('nokInput');
    const tempValue = eurInput.value;
    eurInput.value = nokInput.value;
    nokInput.value = tempValue;
  },

  fetchRate: function() {
    // In production, this would fetch from an actual API
    // For now, using a static rate
    const rateDisplay = document.querySelector('.converter-rate');
    if (rateDisplay) {
      rateDisplay.textContent = `1 EUR = ${this.rate} SEK (taux mis à jour automatiquement)`;
    }
  }
};

// Initialize converter on page load
document.addEventListener('DOMContentLoaded', () => CurrencyConverter.init());

// ==========================================
// BUDGET SIMULATOR
// ==========================================
const BudgetSimulator = {
  baseValues: {
    single: { housing: 12000, food: 4000, transport: 800, leisure: 2000, other: 2000 },
    couple: { housing: 14000, food: 6000, transport: 1200, leisure: 3000, other: 3000 },
    family: { housing: 18000, food: 9000, transport: 1500, leisure: 4000, other: 4000 }
  },

  cityMultipliers: {
    stockholm: 1.2,
    goteborg: 1.0,
    malmo: 0.9,
    uppsala: 0.92,
    linkoping: 0.85,
    umea: 0.88
  },

  init: function() {
    const simulator = document.querySelector('.budget-simulator');
    if (!simulator) return;

    const sliders = simulator.querySelectorAll('input[type="range"]');
    const citySelect = document.getElementById('citySelect');
    const familySelect = document.getElementById('familySelect');

    sliders.forEach(slider => {
      slider.addEventListener('input', () => this.calculate());
    });

    if (citySelect) {
      citySelect.addEventListener('change', () => this.calculate());
    }

    if (familySelect) {
      familySelect.addEventListener('change', () => this.calculate());
    }

    this.calculate();
  },

  calculate: function() {
    const familyType = document.getElementById('familySelect')?.value || 'single';
    const city = document.getElementById('citySelect')?.value || 'stockholm';

    const base = this.baseValues[familyType];
    const multiplier = this.cityMultipliers[city];

    let total = 0;
    for (const key in base) {
      total += base[key] * multiplier;
    }

    // Convert to EUR (approximate)
    const totalEur = Math.round(total / 11.5);

    const resultEl = document.querySelector('.budget-amount');
    if (resultEl) {
      resultEl.textContent = `${totalEur.toLocaleString('fr-FR')} €`;
    }

    // Update chart if exists
    this.updateChart(base, multiplier);
  },

  updateChart: function(base, multiplier) {
    const chartItems = document.querySelectorAll('.budget-chart-item');
    if (!chartItems.length) return;

    const categories = ['housing', 'food', 'transport', 'leisure', 'other'];
    let total = 0;
    for (const key in base) {
      total += base[key] * multiplier;
    }

    categories.forEach((cat, index) => {
      if (chartItems[index]) {
        const value = base[cat] * multiplier;
        const percentage = (value / total) * 100;
        const fill = chartItems[index].querySelector('.budget-chart-fill');
        const valueEl = chartItems[index].querySelector('.budget-chart-value');

        if (fill) fill.style.width = `${percentage}%`;
        if (valueEl) valueEl.textContent = `${Math.round(value / 11.5).toLocaleString('fr-FR')} €`;
      }
    });
  }
};

// Initialize budget simulator on page load
document.addEventListener('DOMContentLoaded', () => BudgetSimulator.init());

// ==========================================
// QUIZ
// ==========================================
const Quiz = {
  questions: [
    {
      question: "Quel climat préférez-vous ?",
      options: [
        { text: "Doux et maritime au sud", points: { malmo: 3, goteborg: 2 } },
        { text: "Continental avec 4 saisons marquées", points: { stockholm: 3, uppsala: 2 } },
        { text: "Froid avec aurores boréales", points: { umea: 3 } },
        { text: "Tempéré près de la côte ouest", points: { goteborg: 3 } }
      ]
    },
    {
      question: "Quelle est votre priorité ?",
      options: [
        { text: "Opportunités professionnelles", points: { stockholm: 3, goteborg: 2 } },
        { text: "Qualité de vie et nature", points: { goteborg: 3, umea: 2 } },
        { text: "Vie étudiante et culturelle", points: { uppsala: 3, stockholm: 2 } },
        { text: "Proximité avec le Danemark", points: { malmo: 3, goteborg: 1 } }
      ]
    },
    {
      question: "Quel type de ville recherchez-vous ?",
      options: [
        { text: "Grande métropole internationale", points: { stockholm: 3 } },
        { text: "Ville moyenne à taille humaine", points: { goteborg: 3, malmo: 2 } },
        { text: "Ville universitaire dynamique", points: { uppsala: 3, umea: 2 } },
        { text: "Proche de la nature sauvage", points: { umea: 3, goteborg: 2 } }
      ]
    }
  ],

  currentQuestion: 0,
  scores: { stockholm: 0, goteborg: 0, malmo: 0, uppsala: 0, umea: 0 },

  init: function() {
    const quizContainer = document.querySelector('.quiz-container');
    if (!quizContainer) return;

    this.container = quizContainer;
    this.render();
  },

  render: function() {
    if (this.currentQuestion >= this.questions.length) {
      this.showResults();
      return;
    }

    const q = this.questions[this.currentQuestion];
    const progress = ((this.currentQuestion) / this.questions.length) * 100;

    this.container.innerHTML = `
      <div class="quiz-progress">
        <p class="quiz-progress-text">Question ${this.currentQuestion + 1} sur ${this.questions.length}</p>
        <div class="progress">
          <div class="progress-bar" style="width: ${progress}%"></div>
        </div>
      </div>
      <div class="quiz-question">
        <h2>${q.question}</h2>
      </div>
      <div class="quiz-options">
        ${q.options.map((opt, i) => `
          <button class="quiz-option" data-index="${i}">${opt.text}</button>
        `).join('')}
      </div>
    `;

    this.container.querySelectorAll('.quiz-option').forEach(btn => {
      btn.addEventListener('click', (e) => this.selectAnswer(e));
    });
  },

  selectAnswer: function(e) {
    const index = parseInt(e.target.dataset.index);
    const q = this.questions[this.currentQuestion];
    const points = q.options[index].points;

    for (const city in points) {
      this.scores[city] += points[city];
    }

    this.currentQuestion++;
    this.render();
  },

  showResults: function() {
    let maxCity = 'stockholm';
    let maxScore = 0;

    for (const city in this.scores) {
      if (this.scores[city] > maxScore) {
        maxScore = this.scores[city];
        maxCity = city;
      }
    }

    const cityNames = {
      stockholm: 'Stockholm',
      goteborg: 'Göteborg',
      malmo: 'Malmö',
      uppsala: 'Uppsala',
      umea: 'Umeå'
    };

    const totalPoints = this.questions.length * 3;
    const matchPercent = Math.round((maxScore / totalPoints) * 100);

    this.container.innerHTML = `
      <div class="quiz-result">
        <h2>Votre ville idéale est...</h2>
        <p class="quiz-result-city">${cityNames[maxCity]}</p>
        <span class="quiz-result-match">${matchPercent}% de compatibilité</span>
        <p>Découvrez tout ce qu'il faut savoir sur ${cityNames[maxCity]} pour préparer votre expatriation.</p>
        <a href="/pages/villes/${maxCity}/" class="btn btn-primary btn-lg btn-arrow">Découvrir ${cityNames[maxCity]}</a>
        <button class="btn btn-secondary mt-4" onclick="Quiz.restart()">Refaire le quiz</button>
      </div>
    `;
  },

  restart: function() {
    this.currentQuestion = 0;
    this.scores = { stockholm: 0, goteborg: 0, malmo: 0, uppsala: 0, umea: 0 };
    this.render();
  }
};

// Initialize quiz on page load
document.addEventListener('DOMContentLoaded', () => Quiz.init());
