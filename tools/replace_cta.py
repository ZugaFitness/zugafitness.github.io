import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

new_cta = """
<section class="py-24 bg-gradient-to-br from-teal-800 to-teal-900 relative overflow-hidden fade-in-section">
  <!-- Decorative background elements -->
  <div class="absolute inset-0 opacity-10">
    <svg class="absolute right-0 top-0 transform translate-x-1/3 -translate-y-1/4 h-[800px] w-[800px] text-white" fill="currentColor" viewBox="0 0 100 100">
      <circle cx="50" cy="50" r="50"></circle>
    </svg>
    <svg class="absolute left-0 bottom-0 transform -translate-x-1/4 translate-y-1/4 h-[600px] w-[600px] text-orange-500" fill="currentColor" viewBox="0 0 100 100">
      <circle cx="50" cy="50" r="50"></circle>
    </svg>
  </div>

  <div class="container mx-auto px-4 max-w-4xl relative z-10 text-center">
    <h2 class="text-4xl md:text-5xl font-bold text-white mb-6" style="font-family: 'Source Serif 4', serif;">
      Ready to Transform Your Practice?
    </h2>
    <p class="text-xl text-teal-100 mb-10 max-w-2xl mx-auto font-light leading-relaxed">
      Whether you are navigating postpartum recovery, seeking hormonal balance, or looking to build functional strength, Anusha is here to guide your journey.
    </p>
    <a href="/Online-Personal-Training-classes.html#inquiry" class="inline-flex items-center justify-center bg-orange-500 hover:bg-orange-600 text-white font-bold py-4 px-10 rounded-full transition-all transform hover:-translate-y-1 hover:shadow-xl text-lg group">
      <span>Book a 1-on-1 Consultation</span>
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5 ml-2 transform group-hover:translate-x-1 transition-transform">
        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
      </svg>
    </a>
  </div>
</section>
"""

# Find the location just before the footer section to insert the new CTA
# Footer starts with: <section data-bs-version="5.1" class="footer3
html = html.replace('<section data-bs-version="5.1" class="footer3', new_cta + '\n<section data-bs-version="5.1" class="footer3')

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
