import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

new_bio_edu = """
<section class="py-20 bg-[#f8f5f0] relative overflow-hidden fade-in-section">
  <!-- Decorative blob -->
  <div class="absolute top-0 right-0 w-64 h-64 bg-orange-200 rounded-full mix-blend-multiply filter blur-3xl opacity-50 transform translate-x-1/2 -translate-y-1/2"></div>

  <div class="container mx-auto px-4 max-w-6xl relative z-10">
    <div class="flex flex-col lg:flex-row gap-12 items-center">

      <!-- Bio Text -->
      <div class="lg:w-1/2">
        <h2 class="text-sm font-bold tracking-widest text-orange-500 uppercase mb-3">About Anusha</h2>
        <h3 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6" style="font-family: 'Source Serif 4', serif;">
          Strength, Flexibility, and Resilience
        </h3>
        <p class="text-lg text-gray-700 leading-relaxed mb-6 font-light">
          With over <span class="font-semibold text-gray-900">500 hours</span> of specialized training, Anusha is an expert in building functional strength, flexibility, and resilience.
        </p>
        <p class="text-lg text-gray-700 leading-relaxed mb-6 font-light">
          While she is highly sought after for safe postpartum and hormonal health programs, she designs highly effective, personalized 1-on-1 strength and mobility protocols for clients of all backgrounds. Her warm, encouraging coaching style ensures every client feels supported and empowered.
        </p>
      </div>

      <!-- Education Cards -->
      <div class="lg:w-1/2 w-full grid gap-6">
        <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl transition-shadow duration-300 transform hover:-translate-y-1">
          <div class="flex items-center gap-4 mb-3">
            <div class="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center text-orange-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5" />
              </svg>
            </div>
            <div>
              <h4 class="text-xl font-bold text-gray-900">MA Yoga & 500 Hours TTC</h4>
              <p class="text-gray-500 text-sm">Karnatak University & Yoga Alliance</p>
            </div>
          </div>
        </div>

        <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl transition-shadow duration-300 transform hover:-translate-y-1">
          <div class="flex items-center gap-4 mb-3">
            <div class="w-12 h-12 bg-teal-100 rounded-full flex items-center justify-center text-teal-600">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.362 5.214A8.252 8.252 0 0112 21 8.25 8.25 0 016.038 7.048 8.287 8.287 0 009 9.6a8.983 8.983 0 013.361-6.867 8.21 8.21 0 003 2.48z" />
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 18a3.75 3.75 0 00.495-7.467 5.99 5.99 0 00-1.925 3.546 5.974 5.974 0 01-2.133-1A3.75 3.75 0 0012 18z" />
              </svg>
            </div>
            <div>
              <h4 class="text-xl font-bold text-gray-900">Functional Movement</h4>
              <p class="text-gray-500 text-sm">Specialized in rhythmic movement, mobility, and functional cardiovascular health.</p>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
"""

# Replace the old Education & Credentials section
pattern = re.compile(r'<section class="py-8 bg-gray-50">.*?</section>', re.DOTALL)
html = pattern.sub(new_bio_edu, html)

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
