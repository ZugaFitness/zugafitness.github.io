import re

with open("corporate-wellness-bangalore.html", "r") as f:
    content = f.read()

# I see the problem. The `#programs` section is missing the wrapping `<section>` tag in my replacement, or rather I opened the container but never wrapped it properly.
# Looking at the code:
# <section class="zuga-section" style="padding: 60px 0 20px 0; background: var(--brand-bg);">
# ...
# </section><section class="zuga-section" id="programs" style="background: var(--brand-bg);">
# <div class="container">
# <h2 class="display-4 text-center mb-5">Our Year-Round Corporate Wellness Programs</h2>
# ...
# <div class="row mb-5 justify-content-center"> ... </div>
# </div>
# </section><section class="zuga-section" id="roi" style="background: var(--brand-bg);">

# Wait, `</div>\n</section><section class="zuga-section" id="roi"`
# Actually, the replacement code I wrote earlier was:
# """
# ...
# </div>
# </div>
# </div>
# </div>
# </section>"""

# BUT, the replacement code didn't perfectly match the structure expected.
# Actually, the problem is in `value-carousel-container`. The previous section `#programs` had `<div class="value-carousel-container">` which was NOT closed in the regex match maybe?
# Wait! In the original file:
# <section class="zuga-section" id="programs" style="background: var(--brand-bg);">
# <div class="container"><h2 class="display-4 text-center mb-5">Our Year-Round Corporate Wellness Programs</h2>
# <div class="value-carousel-container">
# <div class="value-carousel-grid">
# ...
# </div></div>
# </div>
# </div>
# </section><section class="zuga-section" id="roi" style="background: var(--brand-bg);">

# The new HTML in my `corporate-wellness-bangalore.html` looks correct:
# </section><section class="zuga-section" id="programs" style="background: var(--brand-bg);">
# <div class="container">
# ... [content] ...
# </div>
# </section><section class="zuga-section" id="roi" style="background: var(--brand-bg);">
# <div class="container"><h2 class="display-4 text-center mb-5">Why Invest in Corporate Wellness?</h2>

# Why is it overlapping?
# Look at the screenshot carefully.
# The text "Bring Yoga to Your Bangalore Office" is the hero section!
# Ah!! The `value-carousel-container` is overlapping upwards?
# Or is the `programs` section floating?
# Wait, "Bring Yoga to Your Bangalore Office" is the hero section text.
# The screenshot shows the pricing form and Zumba text ON TOP of the "Bring Yoga to Your Bangalore Office" section!
# How can it overlap the hero?
# Maybe there is a missing closing `</div>` in the Hero section?

# Let's check the Hero section `id` or structure.
