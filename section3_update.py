import re

with open('corporate-wellness-productivity.html', 'r', encoding='utf-8') as f:
    content = f.read()

search_pattern = r'<section class="py-xl px-margin-mobile md:px-margin-desktop reveal" id="international-wellness">.*?</section>'
replace_str = '''<section class="py-xl px-margin-mobile md:px-margin-desktop reveal" id="delivery-options">
<div class="max-w-4xl mx-auto mb-16">
<h2 class="font-headline-lg text-on-surface mb-6 text-center">Flexible Delivery for Global Teams</h2>
<p class="font-body-md text-on-surface-variant mb-6 text-lg text-center">Whether your team is in Bangalore, London, or New York, we deliver live, interactive sessions tailored to your timezone.</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8 text-center">
  <div class="p-6 bg-surface-container-low rounded-3xl">
    <span class="material-symbols-outlined text-4xl text-primary mb-3 block" data-icon="corporate_fare">corporate_fare</span>
    <strong class="text-on-surface block mb-2 text-lg">On-Site</strong>
    <span class="text-on-surface-variant">High-energy activations at your office.</span>
  </div>
  <div class="p-6 bg-surface-container-low rounded-3xl">
    <span class="material-symbols-outlined text-4xl text-primary mb-3 block" data-icon="devices">devices</span>
    <strong class="text-on-surface block mb-2 text-lg">Virtual</strong>
    <span class="text-on-surface-variant">Live Zoom sessions for distributed remote teams.</span>
  </div>
  <div class="p-6 bg-surface-container-low rounded-3xl">
    <span class="material-symbols-outlined text-4xl text-primary mb-3 block" data-icon="hub">hub</span>
    <strong class="text-on-surface block mb-2 text-lg">Hybrid</strong>
    <span class="text-on-surface-variant">Unified experiences connecting office and remote employees.</span>
  </div>
</div>
<p class="font-body-md text-on-surface-variant max-w-2xl mx-auto mb-4 p-6 bg-surface-container-lowest rounded-2xl border-l-4 border-secondary text-center"><strong>Takeaway:</strong> Distance is not a barrier to building a unified, high-performing wellness culture.</p>
</div>
</section>'''

content = re.sub(search_pattern, replace_str, content, flags=re.DOTALL)

with open('corporate-wellness-productivity.html', 'w', encoding='utf-8') as f:
    f.write(content)
