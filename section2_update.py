import re

with open('corporate-wellness-productivity.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I need to replace the entire old services-container with the new 3-card structure.
# First, let's find the start and end of the #framework section to replace its content.
# The previous script replaced up to: <div class="w-24 h-1.5 bg-primary-container mx-auto rounded-full"></div>\n</div>\n
# So we can search for the end of that block and then the end of the section (or just replace the `<div class="relative max-w-6xl...` block)

search_pattern = r'<div class="relative max-w-6xl mx-auto flex flex-col md:flex-row gap-gutter overflow-hidden h-\[800px\] md:h-\[650px\]" id="services-container">.*?</section>'
replace_str = '''<div class="relative max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6" id="services-container">

  <div class="bg-white rounded-3xl p-8 shadow-sm border border-outline-variant/30 flex flex-col hover:shadow-xl transition-all duration-300">
    <div class="mb-6 h-48 rounded-2xl overflow-hidden">
      <img alt="Corporate physical reset and movement" class="w-full h-full object-cover" loading="lazy" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCNi4gJN8mCr3vc2aeoCr7LGIdZuGXJCsWWxe8WEm10yBWfI2g4LZdOjUY81OKdRHMFSny1MOVGhC1bmnvTeQJSps01WtH3QLri83bwnpz9f3ea67zFy6Qjuffqm6XYeq3Xkd9SK-Or76e_Sce8JuZ5ek_BoVpHRmdaWhCLRoNrWkylkqbW7YjVRWerUclKOVsn9Cm10ShgF1J22LLJd4zIxcvLgNjKF1fb0sTEBhGScnAKGazqb191"/>
    </div>
    <h4 class="font-headline-md text-primary mb-3">MOVE (Physical Reset)</h4>
    <p class="font-body-md text-on-surface-variant">Counter 8 hours of desk work with targeted mobility, posture correction, and functional movement.</p>
  </div>

  <div class="bg-white rounded-3xl p-8 shadow-sm border border-outline-variant/30 flex flex-col hover:shadow-xl transition-all duration-300">
    <div class="mb-6 h-48 rounded-2xl overflow-hidden">
      <img alt="Nervous system regulation and breathwork" class="w-full h-full object-cover" loading="lazy" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCTeJ7z6Oib-H1pC94zB39P01L5H6_5T5V3QvM5j1L7857J8Q8Ym4B_Q8_22O7x94H81K31_W93O4w2u29rU48uYv0V3x8_z6y2Z00Y3W7o8J03o_P1Kz_K9Vw4Y4o5w6Q3U4s5S9I3r7u187z66q4K2l8B5h3I_k3D8B0s_v3O1a5W7F6Q8q9a3j8U1U5t5R_4"/>
    </div>
    <h4 class="font-headline-md text-primary mb-3">BREATHE (Nervous System Regulation)</h4>
    <p class="font-body-md text-on-surface-variant">Clinical breathwork and mindfulness to lower stress, improve sleep, and sharpen focus.</p>
  </div>

  <div class="bg-white rounded-3xl p-8 shadow-sm border border-outline-variant/30 flex flex-col hover:shadow-xl transition-all duration-300">
    <div class="mb-6 h-48 rounded-2xl overflow-hidden">
      <img alt="Founder team building and connection" class="w-full h-full object-cover" loading="lazy" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCJ22j407Z_r70q-47Y5Z_M5Y9z637S5x_k_F0r9w4y_4w3q82y7q-1W7T13l4T9_n5N2y2Q1w5w6e_X9s_8_k8_7L_7b3R_2_4w4J_5Q1m9_L1v7X49_L_M3x_x8P6m1V9s9L2k4h5y3N7m2y6T0m1"/>
    </div>
    <h4 class="font-headline-md text-primary mb-3">CONNECT (Team Cohesion)</h4>
    <p class="font-body-md text-on-surface-variant">Shared, live experiences that build culture and break down silos between remote and in-office teams.</p>
  </div>

</div>
</section>'''

content = re.sub(search_pattern, replace_str, content, flags=re.DOTALL)

with open('corporate-wellness-productivity.html', 'w', encoding='utf-8') as f:
    f.write(content)
