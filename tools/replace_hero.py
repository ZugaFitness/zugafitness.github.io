import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the article07 section which contains the current bio block
new_hero = """
<section class="relative w-full h-screen min-h-[600px] flex items-center justify-center overflow-hidden bg-black mt-20">
  <!-- Video Background -->
  <div class="absolute inset-0 w-full h-full">
    <video id="heroVideo" class="absolute inset-0 w-full h-full object-cover opacity-60" autoplay loop playsinline muted>
      <source src="/assets/Video%20Project%20(1).mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-black/30"></div>
  </div>

  <!-- Content -->
  <div class="relative z-10 container mx-auto px-4 flex flex-col items-center text-center">
    <img loading="lazy" src="assets/images/anusha-7b37cda6.webp" alt="Anusha" class="w-32 h-32 md:w-40 md:h-40 object-cover rounded-full border-4 border-orange-500 shadow-2xl mb-6 transform transition duration-500 hover:scale-105">
    <h1 class="text-5xl md:text-7xl font-bold text-white mb-4 tracking-tight drop-shadow-lg" style="font-family: 'Source Serif 4', serif;">
      Meet Anusha
    </h1>
    <p class="text-xl md:text-2xl text-gray-200 max-w-2xl font-light mb-8 drop-shadow-md">
      Empowering women through functional strength, hormonal balance, and conscious movement.
    </p>
    <div class="flex flex-col sm:flex-row gap-4">
      <a href="/Online-Personal-Training-classes.html#inquiry" class="bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 px-8 rounded-full transition-all transform hover:-translate-y-1 hover:shadow-lg text-lg">
        Start Your Journey
      </a>
      <button id="muteBtn" class="bg-white/20 hover:bg-white/30 backdrop-blur-sm border border-white/50 text-white font-semibold py-3 px-6 rounded-full transition-all flex items-center justify-center gap-2">
        <svg id="muteIcon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M19.114 5.636a9 9 0 010 12.728M16.463 8.288a5.25 5.25 0 010 7.424M6.75 8.25l4.72-4.72a.75.75 0 011.28.53v15.88a.75.75 0 01-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.01 9.01 0 012.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75z" />
        </svg>
        <span>Unmute</span>
      </button>
    </div>
  </div>
</section>

<!-- Smooth Scroll & Video Logic -->
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('heroVideo');
    const muteBtn = document.getElementById('muteBtn');
    const muteIcon = document.getElementById('muteIcon');

    // Mute/Unmute Toggle
    muteBtn.addEventListener('click', () => {
      if (video.muted) {
        video.muted = false;
        muteBtn.querySelector('span').textContent = 'Mute';
        muteIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" d="M19.114 5.636a9 9 0 010 12.728M16.463 8.288a5.25 5.25 0 010 7.424M6.75 8.25l4.72-4.72a.75.75 0 011.28.53v15.88a.75.75 0 01-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.01 9.01 0 012.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75z" />';
      } else {
        video.muted = true;
        muteBtn.querySelector('span').textContent = 'Unmute';
        muteIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" d="M17.25 9.75L19.5 12m0 0l2.25 2.25M19.5 12l2.25-2.25M19.5 12l-2.25 2.25m-10.5-6l4.72-4.72a.75.75 0 011.28.53v15.88a.75.75 0 01-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.01 9.01 0 012.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75z" />';
      }
    });
  });
</script>
"""

# The section we want to replace starts with <section data-bs-version="5.1" class="article07 and ends right before <section class="py-8 bg-gray-50">
pattern = re.compile(r'<section data-bs-version="5\.1" class="article07.*?</section>', re.DOTALL)
html = pattern.sub(new_hero, html)

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
