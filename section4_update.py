import re

with open('corporate-wellness-productivity.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the #pricing section with the Custom Investment section
search_pattern = r'<section class="py-xl px-margin-mobile md:px-margin-desktop reveal" id="pricing">.*?</section>\s*<!-- Why Zuga\? Bento Grid -->'
replace_str = '''<section class="py-xl px-margin-mobile md:px-margin-desktop reveal" id="investment">
<div class="max-w-4xl mx-auto text-center">
<div class="bg-white p-10 rounded-[2rem] shadow-sm border border-outline-variant/30 text-center mb-4 border-l-4 border-l-primary">
<h2 class="font-headline-lg text-on-surface mb-4">Custom Investment for Organizations</h2>
<p class="font-body-md text-on-surface-variant mb-6 text-lg">We build custom wellness calendars based on your team size, frequency, and goals. Occasional sessions start at ₹5,000. Monthly and Annual partnerships are custom-quoted.</p>
<p class="font-body-md text-on-surface-variant max-w-2xl mx-auto p-4 bg-surface-container-low rounded-xl"><strong>Takeaway:</strong> Invest in a structured program that aligns with your company's scale and operational rhythm.</p>
</div>
</div>
</section>
<!-- Why Zuga? Bento Grid -->'''

content = re.sub(search_pattern, replace_str, content, flags=re.DOTALL)

# Now, we also need to change the #inquiry section (Final CTA) which is near the end.
# Search pattern: <section class="py-xl px-margin-mobile reveal" id="inquiry"> ... </section>
search_cta_pattern = r'<section class="py-xl px-margin-mobile reveal" id="inquiry">.*?</section>'
replace_cta_str = '''<section class="py-xl px-margin-mobile reveal" id="inquiry">
<div class="max-w-2xl mx-auto bg-white rounded-[2.5rem] p-12 shadow-2xl border border-outline-variant/20 relative overflow-hidden text-center">
<div class="absolute -top-10 -right-10 w-40 h-40 bg-primary/10 rounded-full blur-3xl"></div>
<div class="relative z-10">
<h2 class="font-headline-lg text-primary mb-4">Let's Build a Healthier, High-Performing Team.</h2>
<p class="font-body-lg text-on-surface-variant mb-8">Share your team size and goals. We will prepare a tailored proposal for your organization.</p>
<a href="/contact.html" class="bg-primary text-on-primary font-headline-md px-10 py-5 rounded-xl shadow-xl hover:scale-105 active:scale-95 transition-all duration-300 inline-block text-center w-full md:w-auto">Request a Corporate Proposal</a>
</div>
</div>
</section>'''

content = re.sub(search_cta_pattern, replace_cta_str, content, flags=re.DOTALL)


with open('corporate-wellness-productivity.html', 'w', encoding='utf-8') as f:
    f.write(content)
