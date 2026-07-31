import re

with open("corporate-wellness-bangalore.html", "r") as f:
    content = f.read()

# 1. Update the first <h1>
content = re.sub(
    r'<h1 class="display-3 mb-4" style="font-family: \'Playfair Display\', serif; font-weight: 700;">Corporate Wellness &amp; Yoga Programs in Bangalore</h1>',
    r'<h1 class="display-3 mb-4" style="font-family: \'Playfair Display\', serif; font-weight: 700;">Corporate Wellness Programs in Bangalore</h1>',
    content,
    count=1
)

# 2. Downgrade other <h1> to <h2>
content = re.sub(
    r'<h1([^>]*)>Bring Yoga to Your Bangalore Office</h1>',
    r'<h2\1>Bring Yoga to Your Bangalore Office</h2>',
    content
)

# 3. Replace the programs section with new H2 sections
# The programs section starts around line 920 with <section class="zuga-section" id="programs"
# Let's use a regex to replace that section.
programs_regex = re.compile(
    r'<section class="zuga-section" id="programs".*?</section>',
    re.DOTALL
)

new_programs_html = """<section class="zuga-section" id="programs" style="background: var(--brand-bg);">
<div class="container">
<h2 class="display-4 text-center mb-5">Our Year-Round Corporate Wellness Programs</h2>

<div class="row mb-5">
  <div class="col-12">
    <h2 class="display-5 mb-3" style="font-family: 'Playfair Display', serif;">Corporate Yoga: Stress Relief &amp; Posture Correction</h2>
    <p class="brand-sans" style="font-size: 1.1rem; color: var(--brand-text);">Our corporate yoga sessions are designed to counteract the negative effects of prolonged sitting and high-stress environments. We focus on mindfulness techniques to calm the nervous system and targeted stretches for desk-posture relief, including neck, shoulder, and lower back release.</p>
    <p><strong>Takeaway:</strong> Corporate yoga provides essential stress relief and posture correction to help employees stay focused and physically comfortable at their desks.</p>
  </div>
</div>

<div class="row mb-5">
  <div class="col-12">
    <h2 class="display-5 mb-3" style="font-family: 'Playfair Display', serif;">Corporate Zumba: High-Energy Team Building</h2>
    <p class="brand-sans" style="font-size: 1.1rem; color: var(--brand-text);">Inject fun and vitality into your workplace with our high-energy corporate Zumba sessions. It's an excellent cardiovascular workout that breaks the ice, encourages group bonding, and leaves your team feeling energized and motivated.</p>
    <p><strong>Takeaway:</strong> Corporate Zumba is a fun, high-energy cardio workout that doubles as an effective team-building activity.</p>
  </div>
</div>
</div>
</section>"""

content = programs_regex.sub(new_programs_html, content)


# 4. Add takeaway to all other H2s
# This is tricky because H2s can have various structures. We can just add the takeaway before the closing </div> of the section containing the H2, or right after the introductory paragraph.
# Let's inspect where to add takeaways for existing H2s.
with open("corporate-wellness-bangalore.html", "w") as f:
    f.write(content)
