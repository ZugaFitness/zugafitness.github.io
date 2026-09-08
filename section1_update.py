import re

with open('corporate-wellness-productivity.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <section id="services"> to the start of <div id="services-container">
search_pattern = r'<section class="py-xl px-margin-mobile md:px-margin-desktop reveal" id="services">.*?(?=<div class="relative max-w-6xl mx-auto flex flex-col md:flex-row gap-gutter overflow-hidden h-\[800px\] md:h-\[650px\]" id="services-container">)'
replace_str = '''<section class="py-xl px-margin-mobile md:px-margin-desktop reveal" id="business-case">
<div class="max-w-4xl mx-auto mb-16">
<h2 class="font-headline-lg text-on-surface mb-6 text-center">The Business Case for Workplace Wellness</h2>
<p class="font-body-md text-on-surface-variant mb-6 text-lg">Forward-thinking founders are replacing generic gym memberships with structured, live wellness interventions. Why?</p>
<ul class="space-y-4 mb-8">
  <li class="flex items-start gap-3">
    <span class="material-symbols-outlined text-primary mt-1" data-icon="check_circle">check_circle</span>
    <div>
      <strong class="text-on-surface">Reduced Burnout:</strong>
      <span class="text-on-surface-variant"> Structured movement and breathwork lower cortisol, preventing executive and team fatigue.</span>
    </div>
  </li>
  <li class="flex items-start gap-3">
    <span class="material-symbols-outlined text-primary mt-1" data-icon="check_circle">check_circle</span>
    <div>
      <strong class="text-on-surface">Higher Focus:</strong>
      <span class="text-on-surface-variant"> 30-minute nervous system resets improve cognitive clarity and decision-making.</span>
    </div>
  </li>
  <li class="flex items-start gap-3">
    <span class="material-symbols-outlined text-primary mt-1" data-icon="check_circle">check_circle</span>
    <div>
      <strong class="text-on-surface">Better Retention:</strong>
      <span class="text-on-surface-variant"> Companies with strong wellness cultures see significantly lower turnover rates.</span>
    </div>
  </li>
</ul>
<p class="font-body-md text-on-surface-variant max-w-2xl mx-auto mb-4 p-6 bg-surface-container-low rounded-2xl border-l-4 border-primary"><strong>Takeaway:</strong> Investing in your team's physical and mental regulation directly impacts your bottom line.</p>
</div>
</section>

<!-- Our Services -->
<section class="py-xl px-margin-mobile md:px-margin-desktop reveal bg-surface-container-low" id="framework">
<div class="text-center mb-16">
<h2 class="font-headline-lg text-on-surface mb-4">What We Deliver (The MOVE • BREATHE • CONNECT Framework)</h2>
<div class="w-24 h-1.5 bg-primary-container mx-auto rounded-full"></div>
</div>
'''

content = re.sub(search_pattern, replace_str, content, flags=re.DOTALL)

with open('corporate-wellness-productivity.html', 'w', encoding='utf-8') as f:
    f.write(content)
