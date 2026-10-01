# It looks like my previous attempt to add the specialties grid got lost or wasn't added properly,
# let's add it back using a robust method.

import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

new_specialties = """
<section class="py-20 bg-white fade-in-section">
  <div class="container mx-auto px-4 max-w-6xl">
    <div class="text-center mb-16">
      <h2 class="text-sm font-bold tracking-widest text-teal-600 uppercase mb-3">Expertise</h2>
      <h3 class="text-3xl md:text-5xl font-bold text-gray-900" style="font-family: 'Source Serif 4', serif;">
        Core Specialties
      </h3>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <!-- Specialty 1 -->
      <div class="group relative bg-gray-50 rounded-3xl p-8 overflow-hidden hover:bg-orange-500 transition-colors duration-500">
        <div class="absolute -right-4 -top-4 w-24 h-24 bg-orange-100 rounded-full group-hover:bg-orange-400 transition-colors duration-500"></div>
        <div class="relative z-10">
          <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mb-6 shadow-sm group-hover:text-orange-500 text-teal-600 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-8 h-8">
              <path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-1.218 0l4.204-3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" />
            </svg>
          </div>
          <h4 class="text-xl font-bold text-gray-900 group-hover:text-white mb-3 transition-colors">Functional Strength</h4>
          <p class="text-gray-600 group-hover:text-white/90 transition-colors">
            Building resilience and functional flexibility for all body types and levels.
          </p>
        </div>
      </div>

      <!-- Specialty 2 -->
      <div class="group relative bg-gray-50 rounded-3xl p-8 overflow-hidden hover:bg-teal-600 transition-colors duration-500">
        <div class="absolute -right-4 -top-4 w-24 h-24 bg-teal-100 rounded-full group-hover:bg-teal-500 transition-colors duration-500"></div>
        <div class="relative z-10">
          <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mb-6 shadow-sm group-hover:text-teal-600 text-orange-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-8 h-8">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418" />
            </svg>
          </div>
          <h4 class="text-xl font-bold text-gray-900 group-hover:text-white mb-3 transition-colors">Postpartum Recovery</h4>
          <p class="text-gray-600 group-hover:text-white/90 transition-colors">
            Safe core rebuilding and mindful movement for postnatal wellness.
          </p>
        </div>
      </div>

      <!-- Specialty 3 -->
      <div class="group relative bg-gray-50 rounded-3xl p-8 overflow-hidden hover:bg-orange-500 transition-colors duration-500">
        <div class="absolute -right-4 -top-4 w-24 h-24 bg-orange-100 rounded-full group-hover:bg-orange-400 transition-colors duration-500"></div>
        <div class="relative z-10">
          <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center mb-6 shadow-sm group-hover:text-orange-500 text-teal-600 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-8 h-8">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z" />
            </svg>
          </div>
          <h4 class="text-xl font-bold text-gray-900 group-hover:text-white mb-3 transition-colors">Hormonal Balance</h4>
          <p class="text-gray-600 group-hover:text-white/90 transition-colors">
            Stress management protocols designed to support hormonal health.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# Let's insert the specialties section right before the reels section
html = html.replace('<section class="py-20 bg-gray-50 overflow-hidden fade-in-section">', new_specialties + '\n<section class="py-20 bg-gray-50 overflow-hidden fade-in-section">')

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
