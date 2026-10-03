import re

with open("assets/js/whatsapp-concierge.js", "r") as f:
    js = f.read()

# Add the exclusion list logic right after the initial checks
exclusion_code = """
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
"""

# Let's see where to inject it. Right after `if (isSubmitted() || isDismissed()) return;`
if "EXCLUDED_PAGES" not in js:
    js = js.replace("if (isSubmitted() || isDismissed()) return;", "if (isSubmitted() || isDismissed()) return;\n" + exclusion_code)

    with open("assets/js/whatsapp-concierge.js", "w") as f:
        f.write(js)
    print("Successfully added exclusions to whatsapp-concierge.js")
else:
    # It might already have EXCLUDED_PAGES, we need to append the new urls.
    pass
