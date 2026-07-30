import re

# Look at this duplication in the hero section:
# 1017:<section class="hero-section zuga-section" style="background: var(--brand-bg); padding-top: 40px;">
# 1018-<div class="container">
# 1019-<div class="row align-items-center">
# ...
# 1034-</div>
# 1035-</div>
# 1036-  <div class="container">
# 1037-    <div class="row align-items-center">
# 1038-      <!-- Left Grid Content -->
# 1039-      <div class="col-lg-6 mb-5 mb-lg-0">
# 1040:        <h2 class="display-3 mb-4" ...>Bring Yoga to Your Bangalore Office</h2>
# ...
# 1055-</section>

# Ah, the whole page has duplicated sections from previous edits or Mobirise!
# "Bring Yoga to Your Bangalore Office" is inside the SAME <section> as "Corporate Wellness Programs in Bangalore".
# Wait, look at the screenshot again.
# The screenshot says "Bring Yoga to Your Bangalore Office" and "Programs in Bangalore" ON TOP of "Why Invest in Corporate Wellness?".
# How did my `update_headings.py` break the layout?
# In `update_headings.py`, I did:
# programs_regex = re.compile(r'<section class="zuga-section" id="programs".*?</section>', re.DOTALL)
# new_programs_html = ...
# content = programs_regex.sub(new_programs_html, content)

# But wait, did `re.DOTALL` match from the FIRST `<section class="zuga-section" id="programs"` to the LAST `</section>` in the file?!
# YES!!! `.*` is greedy by default! `.*?` is non-greedy.
# BUT wait, I used `.*?`! It is non-greedy.
# Let's check what was replaced.
