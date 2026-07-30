import re

with open("corporate-wellness-bangalore.html", "r") as f:
    content = f.read()

# I see what went wrong. The screenshot shows the form overlaying the "Why Invest in Corporate Wellness" section.
# Looking at the code:
# <div class="row mb-5 justify-content-center">
#  <div class="col-lg-8">
#    <div style="background: var(--brand-white); border-radius: 20px; padding: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); border-top: 5px solid var(--brand-teal);">
# ...
# The section `<section class="zuga-section" id="programs" style="background: var(--brand-bg);">` has no padding or margin defined if `.zuga-section` relies on something else, but it shouldn't overlap unless there's an absolute positioning or float issue.
# Wait, looking at the layout, the "Why Invest" section has class `value-carousel-container`.
# And our new text blocks ("Corporate Yoga: Stress Relief & Posture Correction") have `div class="row mb-5"`.
# The overlap might just be a lack of vertical padding.
# Let's add some padding-bottom to the programs section or a spacer.
# Wait, let's look at the screenshot again carefully.

# Actually, the "Our Year-Round Corporate Wellness Programs" header is cut off on the left.
# And the "Corporate Yoga: Stress Relief & Posture Correction" text is on top of "Why Invest in Corporate Wellness?".
# It looks like there's an absolute positioning issue or a fixed height on the section.
