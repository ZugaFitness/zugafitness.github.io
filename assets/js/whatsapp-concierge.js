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

    const modalHTML = `
      <div id="zuga-whatsapp-concierge" role="dialog" aria-modal="true" aria-labelledby="zwc-title">
        <div class="zwc-modal" tabindex="-1">
          <div class="zwc-header">
            <h3 id="zwc-title">Text us your goal. We'll text back your plan.</h3>
            <p class="zwc-sub">That's it. One message and your classes are sorted.</p>
            <svg class="zwc-sunrise-svg" aria-hidden="true" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              <path d="M10,100 A40,40 0 0,1 90,100" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
              <line x1="50" y1="50" x2="50" y2="20" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
              <line x1="25" y1="60" x2="10" y2="40" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
              <line x1="75" y1="60" x2="90" y2="40" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
              <line x1="15" y1="85" x2="0" y2="80" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
              <line x1="85" y1="85" x2="100" y2="80" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/>
            </svg>
            <button class="zwc-close" aria-label="Close">&times;</button>
          </div>
          <div class="zwc-body">
            <form id="zwc-form">
              <div class="zwc-form-group">
                <label for="zwc-goal">What is your main goal?</label>
                <input type="text" id="zwc-goal" class="zwc-form-control" placeholder="e.g. Weight loss, better sleep, back pain, classes for my child" required maxlength="120">
              </div>
              <div class="zwc-form-group">
                <label for="zwc-country">Your WhatsApp number</label>
                <div class="zwc-phone-row">
                  <select id="zwc-country" class="zwc-form-control" required>
                    ${countries.map(c => `<option value="${c.name}|${c.code}">${c.code} (${c.name})</option>`).join('')}
                  </select>
                  <input type="tel" id="zwc-phone" class="zwc-form-control" placeholder="98765 43210" required inputmode="tel" pattern="[0-9 ]{6,15}">
                </div>
              </div>
              <button type="submit" class="zwc-submit">Get My Plan on WhatsApp</button>
              <p class="zwc-micro">Trainers reply personally, 9 am–9 pm IST.</p>
            </form>
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
