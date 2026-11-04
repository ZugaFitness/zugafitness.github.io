import re
with open('hybrid-fitness.html', 'r', encoding='utf-8') as f:
    html = f.read()

# [Membership / Pricing Section] fixes
membership_head_regex = r'<div class="sec-head reveal">.*?<p class="eyebrow">Membership</p>.*?<h2 class="title">Simple, Transparent <em>Pricing.</em></h2>.*?</div>.*?</div>'
# Need to make sure the toggle is removed. The previous replacement might not have caught it because of linebreaks or exact string matches. Let's use a simpler regex on the unmodified kkk.html if it didn't match.

# Wait, let's just do a simpler search and replace for the membership header.
membership_header_old = '''      <div class="sec-head reveal">
        <div>
          <p class="eyebrow">Membership</p>
          <h2 class="title">One simple <em>price.</em></h2>
        </div>
        <div class="bill-toggle">
          <span class="on" id="lblMonthly">Monthly</span>
          <button class="switch" id="billSwitch" role="switch" aria-checked="false" aria-label="Toggle annual billing"></button>
          <span id="lblAnnual">Annual</span>
          <span class="save-tag">SAVE 20%</span>
        </div>
      </div>'''
membership_header_new = '''      <div class="sec-head reveal">
        <div>
          <p class="eyebrow">Membership</p>
          <h2 class="title">Simple, Transparent <em>Pricing.</em></h2>
        </div>
      </div>'''
html = html.replace(membership_header_old, membership_header_new)


# Let's fix the footer Zuga Fitness name since that might have missed tags.
html = html.replace('An online yoga studio for people with real lives', 'An online hybrid fitness studio for people with real lives')
html = html.replace('Made with breath in Lisbon.', 'Made with ❤️ by Zuga Fitness.')
html = html.replace('Stillpoint Studio', 'Zuga Fitness')
html = html.replace('The Stillpoint Playlist', 'The Zuga Fitness Playlist')
html = html.replace('stillpoint.studio', 'zugafitness')


with open('hybrid-fitness.html', 'w', encoding='utf-8') as f:
    f.write(html)
