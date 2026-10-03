import re

promo_bar_html = """
<!-- WLC PROMO BAR -->
<div id="wlc-promo-bar" style="display: none; width: 100%; background-color: var(--primary-brand, #E8690A); color: white; text-align: center; padding: 12px 10px; font-family: 'Poppins', sans-serif; font-weight: 500; font-size: 0.95rem; z-index: 9999; position: relative; box-sizing: border-box; min-height: 48px;">
  The 90-Day Post-Diwali Reset - Cohort starts Nov 1. 30 spots. <a href="/weight-loss-challenge.html" style="color: white; text-decoration: underline; font-weight: 600;">Reserve yours &rarr;</a>
  <button id="wlc-promo-close" aria-label="Close" style="position: absolute; right: 15px; top: 50%; transform: translateY(-50%); background: none; border: none; color: white; font-size: 1.2rem; cursor: pointer; padding: 5px;">&times;</button>
</div>
<script>
document.addEventListener("DOMContentLoaded", function() {
  const WLC_LIVE = false; // Launch Gate - flip to true when real payment details are added
  if (WLC_LIVE && !sessionStorage.getItem('wlc_promo_dismissed')) {
    // Also check if we are past Nov 1, 2026
    if (new Date() < new Date('2026-11-02')) {
      const bar = document.getElementById('wlc-promo-bar');
      bar.style.display = 'block';
      document.getElementById('wlc-promo-close').addEventListener('click', function() {
        bar.style.display = 'none';
        sessionStorage.setItem('wlc_promo_dismissed', 'true');
      });
    }
  }
});
</script>
<!-- /WLC PROMO BAR -->
"""

files_to_update = ["index.html", "Online-Dance-Fitness-Classes.html"]

for filename in files_to_update:
    with open(filename, "r") as f:
        content = f.read()

    # We will inject right before `<section class="menu`
    if "WLC PROMO BAR" not in content:
        content = re.sub(r'(<section[^>]*class="menu)', promo_bar_html + r'\n\1', content, count=1)
        with open(filename, "w") as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Promo bar already in {filename}")
