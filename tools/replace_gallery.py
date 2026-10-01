import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

new_gallery = """
<section class="py-20 bg-white fade-in-section">
  <div class="container mx-auto px-4 max-w-6xl">
    <div class="text-center mb-16">
      <h2 class="text-sm font-bold tracking-widest text-teal-600 uppercase mb-3">Gallery</h2>
      <h3 class="text-3xl md:text-5xl font-bold text-gray-900" style="font-family: 'Source Serif 4', serif;">
        Practice & Methodology
      </h3>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="group relative overflow-hidden rounded-3xl shadow-sm hover:shadow-xl transition-all duration-500 h-80">
        <img loading="lazy" src="/assets/images/anusha-7b37cda6.webp" alt="Anusha leading functional movement session" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700">
        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex items-end">
          <div class="p-6">
            <h4 class="text-white font-bold text-xl mb-1">Functional Movement</h4>
            <p class="text-gray-200 text-sm">Building core resilience</p>
          </div>
        </div>
      </div>

      <div class="group relative overflow-hidden rounded-3xl shadow-sm hover:shadow-xl transition-all duration-500 h-80">
        <img loading="lazy" src="/assets/images/picsart-25-02-11-13-27-01-991jpg-518x690.jpg" alt="Anusha guiding safe postpartum recovery" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700" style="object-position: top;">
        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex items-end">
          <div class="p-6">
            <h4 class="text-white font-bold text-xl mb-1">Postpartum Safe</h4>
            <p class="text-gray-200 text-sm">Gentle guided recovery</p>
          </div>
        </div>
      </div>

      <div class="group relative overflow-hidden rounded-3xl shadow-sm hover:shadow-xl transition-all duration-500 h-80">
        <img loading="lazy" src="/assets/images/picsart-25-02-10-01-25-57-872jpg-518x518.jpg" alt="Anusha demonstrating hormonal balance breathwork" class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700">
        <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex items-end">
          <div class="p-6">
            <h4 class="text-white font-bold text-xl mb-1">Hormonal Balance</h4>
            <p class="text-gray-200 text-sm">Mindful breathwork integration</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# The current gallery looks like this:
# <section class="py-20 bg-white">
#  <div class="container mx-auto px-4 max-w-5xl">
#    <h3 class="text-2xl font-bold text-center text-gray-800 mb-6">Practice Gallery</h3>

html = re.sub(r'<section class="py-20 bg-white">.*?<h3 class="text-2xl font-bold text-center text-gray-800 mb-6">Practice Gallery</h3>.*?</div>\s*</div>\s*</section>', new_gallery, html, flags=re.DOTALL)

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
