import re

with open("corporate-wellness-bangalore.html", "r") as f:
    content = f.read()

# Currently, we have some unclosed tags or layout bugs. In the screenshot, the "Why Invest in Corporate Wellness?" section overlaps into the programs section.
# The layout is broken because `<section class="zuga-section" id="roi"` overlaps or there is some missing layout structure.
# Let's inspect the original Programs section to see how it was nested.

# Earlier, I replaced:
# <section class="zuga-section" id="programs" ...>
# ...
# </section>
# But wait, looking closely at the original HTML:
# <section class="zuga-section" id="programs" style="background: var(--brand-bg);">
# <div class="container"><h2 class="display-4 text-center mb-5">Our Year-Round Corporate Wellness Programs</h2>
# <div class="value-carousel-container">
# ...
# </div></div></section><section class="zuga-section" id="roi" style="background: var(--brand-bg);">

# In my replacement, I replaced the entire <section class="zuga-section" id="programs" ...> ... </section>.
# Did I miss closing a div?
# <div class="container">
# ...
# <div class="row">...</div>
# ...
# </div>
# </section>

# It seems correct structurally. Wait, maybe the overlap is because of the `value-carousel-container` not being closed properly if my regex replaced too little/too much?
# The regex was: r'<section class="zuga-section" id="programs".*?</section>' with re.DOTALL.
# It should have replaced exactly one section tag.
