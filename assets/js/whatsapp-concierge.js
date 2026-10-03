// whatsapp-concierge.js
(function() {
  const ZWC_DISMISSED_KEY = 'zuga_wc_dismissed';
  const ZWC_SUBMITTED_KEY = 'zuga_wc_submitted';
  const ZWC_PHONE = '917676379909';

  const isDismissed = () => {
    const dismissedTime = localStorage.getItem(ZWC_DISMISSED_KEY);
    if (!dismissedTime) return false;
    const now = new Date().getTime();
    if (now - parseInt(dismissedTime, 10) > 7 * 24 * 60 * 60 * 1000) {
      localStorage.removeItem(ZWC_DISMISSED_KEY);
      return false;
    }
    return true;
  };

  const isSubmitted = () => localStorage.getItem(ZWC_SUBMITTED_KEY) === 'true';

  if (isSubmitted() || isDismissed()) return;

  const EXCLUDED_PAGES = [
    '/free-trial.html',
    '/thank-you.html',
    '/personal-training-consultation.html',
    '/weight-loss-challenge.html',
    '/wlc-form.html',
    '/wlc-thank-you.html',
    '/wlc-vault.html'
  ];

  if (EXCLUDED_PAGES.some(page => window.location.pathname.toLowerCase().endsWith(page.toLowerCase()))) {
    return; // Do not show on excluded pages
  }


  const countries = [
    { name: "Australia", code: "+61", tz: "Australia/" },
    { name: "Brazil", code: "+55", tz: "America/Sao_Paulo" },
    { name: "Canada", code: "+1", tz: "America/Toronto" },
    { name: "Denmark", code: "+45", tz: "Europe/Copenhagen" },
    { name: "France", code: "+33", tz: "Europe/Paris" },
    { name: "Germany", code: "+49", tz: "Europe/Berlin" },
    { name: "India", code: "+91", tz: "Asia/Kolkata" },
    { name: "Ireland", code: "+353", tz: "Europe/Dublin" },
    { name: "Italy", code: "+39", tz: "Europe/Rome" },
    { name: "Japan", code: "+81", tz: "Asia/Tokyo" },
    { name: "Kenya", code: "+254", tz: "Africa/Nairobi" },
    { name: "Malaysia", code: "+60", tz: "Asia/Kuala_Lumpur" },
    { name: "Mexico", code: "+52", tz: "America/Mexico_City" },
    { name: "Netherlands", code: "+31", tz: "Europe/Amsterdam" },
    { name: "New Zealand", code: "+64", tz: "Pacific/Auckland" },
    { name: "Nigeria", code: "+234", tz: "Africa/Lagos" },
    { name: "Norway", code: "+47", tz: "Europe/Oslo" },
    { name: "Philippines", code: "+63", tz: "Asia/Manila" },
    { name: "Poland", code: "+48", tz: "Europe/Warsaw" },
    { name: "Portugal", code: "+351", tz: "Europe/Lisbon" },
    { name: "Saudi Arabia", code: "+966", tz: "Asia/Riyadh" },
    { name: "Singapore", code: "+65", tz: "Asia/Singapore" },
    { name: "South Africa", code: "+27", tz: "Africa/Johannesburg" },
    { name: "South Korea", code: "+82", tz: "Asia/Seoul" },
    { name: "Spain", code: "+34", tz: "Europe/Madrid" },
    { name: "Sweden", code: "+46", tz: "Europe/Stockholm" },
    { name: "Switzerland", code: "+41", tz: "Europe/Zurich" },
    { name: "United Arab Emirates", code: "+971", tz: "Asia/Dubai" },
    { name: "United Kingdom", code: "+44", tz: "Europe/London" },
    { name: "United States", code: "+1", tz: "America/New_York" }
  ].sort((a, b) => a.name.localeCompare(b.name));

  const injectHTML = () => {
    if (document.getElementById('zuga-whatsapp-concierge')) return;

    // Dynamically inject fonts so page LCP is untouched
    if (!document.getElementById('zwc-fonts')) {
      const preconnect1 = document.createElement('link');
      preconnect1.rel = 'preconnect';
      preconnect1.href = 'https://fonts.googleapis.com';

      const preconnect2 = document.createElement('link');
      preconnect2.rel = 'preconnect';
      preconnect2.href = 'https://fonts.gstatic.com';
      preconnect2.crossOrigin = 'anonymous';

      const link = document.createElement('link');
      link.id = 'zwc-fonts';
      link.rel = 'stylesheet';
      link.href = 'https://fonts.googleapis.com/css2?family=Caveat:wght@400&family=Lora:ital,wght@0,700;1,700&display=swap';

      document.head.appendChild(preconnect1);
      document.head.appendChild(preconnect2);
      document.head.appendChild(link);
    }

    const modalHTML = `
      <div id="zuga-whatsapp-concierge" role="dialog" aria-modal="true" aria-labelledby="zwc-title">
        <div class="zwc-modal" tabindex="-1">
          <div class="zwc-layout">
            <div class="zwc-photo-panel">
              <div class="zwc-blob zwc-blob-tl" aria-hidden="true"></div>
              <div class="zwc-blob zwc-blob-bl" aria-hidden="true"></div>
              <div class="zwc-note zwc-note-photo">
                Small steps make big changes
                <svg class="zwc-heart" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
              </div>
            </div>
            <div class="zwc-content-panel">
              <button class="zwc-close" aria-label="Close">
                <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="24" height="24"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
              </button>

              <div class="zwc-header">
                <h3 id="zwc-title">
                  <svg class="zwc-icon-dart" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>
                  Text us your goal.<br>We'll text back <span class="zwc-highlight">your plan.</span>
                  <svg class="zwc-sparkle zwc-sparkle-tr" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>
                </h3>
                <p class="zwc-sub">That's it. One message and your classes are sorted.</p>
              </div>

              <div class="zwc-body">
                <form id="zwc-form">
                  <div class="zwc-form-group">
                    <label for="zwc-goal">
                      <svg class="zwc-icon-dart-small" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>
                      What is your main goal?
                    </label>
                    <input type="text" id="zwc-goal" class="zwc-form-control" placeholder="e.g. Weight loss, better sleep, back pain, classes for my child" required maxlength="120">
                  </div>
                  <div class="zwc-form-group">
                    <label for="zwc-country">
                      <svg class="zwc-icon-wa" aria-hidden="true" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.489-1.761-1.663-2.06-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"></path></svg>
                      Your WhatsApp number
                    </label>
                    <div class="zwc-phone-row">
                      <select id="zwc-country" class="zwc-form-control" required>
                        ${countries.map(c => `<option value="${c.name}|${c.code}">${c.code} (${c.name})</option>`).join('')}
                      </select>
                      <input type="tel" id="zwc-phone" class="zwc-form-control" placeholder="98765 43210" required inputmode="tel" pattern="[0-9 ]{6,15}">
                    </div>
                  </div>
                  <div class="zwc-btn-wrapper">
                    <svg class="zwc-sparkle zwc-sparkle-bl" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>
                    <button type="submit" class="zwc-submit">
                      <svg class="zwc-icon-wa" aria-hidden="true" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.888-.788-1.489-1.761-1.663-2.06-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"></path></svg>
                      Get My Plan on WhatsApp
                      <svg class="zwc-icon-chevron" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
                    </button>
                    <svg class="zwc-sparkle zwc-sparkle-br" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"></path></svg>
                  </div>

                  <p class="zwc-micro">
                    <svg class="zwc-icon-clock" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    Trainers reply personally, 9 am - 9 pm IST.
                  </p>
                </form>
              </div>

              <div class="zwc-blob zwc-blob-br" aria-hidden="true"></div>
              <svg class="zwc-leaf" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="#2c5f2d" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"></path><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"></path></svg>
              <div class="zwc-note zwc-note-content">
                Your health goals matter
                <svg class="zwc-heart" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    const userTz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const countrySelect = document.getElementById('zwc-country');

    let defaultIndex = countries.findIndex(c => c.name === 'India');

    if (userTz) {
      const matchIndex = countries.findIndex(c => userTz.startsWith(c.tz));
      if (matchIndex !== -1) defaultIndex = matchIndex;
    }

    countrySelect.selectedIndex = defaultIndex;

    const modal = document.getElementById('zuga-whatsapp-concierge');
    const closeBtn = modal.querySelector('.zwc-close');
    const form = document.getElementById('zwc-form');
    const focusableElements = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
    const firstFocusable = focusableElements[0];
    const lastFocusable = focusableElements[focusableElements.length - 1];

    const closeModal = () => {
      modal.classList.remove('visible');
      localStorage.setItem(ZWC_DISMISSED_KEY, new Date().getTime().toString());
    };

    closeBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('visible')) {
        closeModal();
      }

      if (e.key === 'Tab' && modal.classList.contains('visible')) {
        if (e.shiftKey) {
          if (document.activeElement === firstFocusable) {
            lastFocusable.focus();
            e.preventDefault();
          }
        } else {
          if (document.activeElement === lastFocusable) {
            firstFocusable.focus();
            e.preventDefault();
          }
        }
      }
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const goal = document.getElementById('zwc-goal').value;
      const tzVal = document.getElementById('zwc-country').value;
      // Extract country name and code from "Name|Code"
      const [countryName, countryCode] = tzVal.split('|');

      let message = `Hi Zuga! My goal: ${goal}. My timezone: ${countryName} (${countryCode}).`;

      const encodedMessage = encodeURIComponent(message);
      const waUrl = `https://wa.me/${ZWC_PHONE}?text=${encodedMessage}`;

      localStorage.setItem(ZWC_SUBMITTED_KEY, 'true');

      if (typeof gtag !== 'undefined') {
        gtag('event', 'whatsapp_lead', {
          'event_category': 'engagement',
          'event_label': 'concierge_modal'
        });
      }

      window.open(waUrl, '_blank', 'noopener,noreferrer');
      modal.classList.remove('visible');
    });
  };

  let isMobile = window.innerWidth <= 768;
  window.addEventListener('resize', () => { isMobile = window.innerWidth <= 768; });

  let modalShown = false;
  window.showModal = () => {
    if (modalShown || isSubmitted() || isDismissed()) return;
    modalShown = true;
    injectHTML();

    setTimeout(() => {
      const modal = document.getElementById('zuga-whatsapp-concierge');
      modal.classList.add('visible');

      if (!isMobile) {
        document.getElementById('zwc-goal').focus();
      }
    }, 50);
  };

  document.addEventListener('mouseleave', (e) => {
    if (!isMobile && e.clientY <= 0) {
      window.showModal();
    }
  });

  document.addEventListener('scroll', () => {
    if (isMobile) {
      const scrollPos = window.scrollY + window.innerHeight;
      const threshold = document.documentElement.scrollHeight * 0.5;
      if (scrollPos >= threshold) {
        window.showModal();
      }
    }
  });

  let dwellTime = 0;
  const targetDwellTime = isMobile ? 75000 : 60000;
  let dwellInterval;

  const startDwellTimer = () => {
    if (dwellInterval) return;
    dwellInterval = setInterval(() => {
      if (document.visibilityState === 'visible') {
        dwellTime += 1000;
        if (dwellTime >= targetDwellTime) {
          clearInterval(dwellInterval);
          window.showModal();
        }
      }
    }, 1000);
  };

  const stopDwellTimer = () => {
    if (dwellInterval) {
      clearInterval(dwellInterval);
      dwellInterval = null;
    }
  };

  if (document.visibilityState === 'visible') {
    startDwellTimer();
  }

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') {
      startDwellTimer();
    } else {
      stopDwellTimer();
    }
  });

})();
