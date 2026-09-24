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
            <h2 id="zwc-title">
              <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
              Zuga Concierge
            </h2>
            <button class="zwc-close" aria-label="Close modal">&times;</button>
          </div>
          <div class="zwc-body">
            <p>Request a private consultation and bespoke itinerary. We usually reply within 5 minutes.</p>
            <form id="zwc-form">
              <div class="zwc-form-group">
                <label for="zwc-goal">Primary Goal</label>
                <select id="zwc-goal" class="zwc-form-control" required>
                  <option value="" disabled selected>Select your main focus...</option>
                  <option value="Weight Loss & Toning">Weight Loss & Toning</option>
                  <option value="Flexibility & Mobility">Flexibility & Mobility</option>
                  <option value="Stress Relief & Mindfulness">Stress Relief & Mindfulness</option>
                  <option value="Postnatal Recovery">Postnatal Recovery</option>
                  <option value="General Fitness">General Fitness</option>
                  <option value="Condition Management (e.g. PCOD, Back pain)">Condition Management</option>
                </select>
              </div>
              <div class="zwc-form-group">
                <label for="zwc-country">Country / Timezone Context</label>
                <select id="zwc-country" class="zwc-form-control" required>
                  ${countries.map(c => `<option value="${c.name} ${c.code}">${c.name} ${c.code}</option>`).join('')}
                </select>
              </div>
              <div class="zwc-form-group">
                <label for="zwc-note">Additional Note (Optional)</label>
                <textarea id="zwc-note" class="zwc-form-control" placeholder="Any injuries, preferences, or specific timings?"></textarea>
              </div>
              <button type="submit" class="zwc-submit">
                <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
                Continue to WhatsApp
              </button>
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
      const tz = document.getElementById('zwc-country').value;
      const note = document.getElementById('zwc-note').value;

      let message = `Hello Zuga Concierge. I am requesting a private consultation. My primary goal is ${goal}. My current timezone is ${tz}.`;
      if (note.trim()) {
        message += ` ${note.trim()}`;
      }
      message += ` Please share my bespoke itinerary and assessment details.`;

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
