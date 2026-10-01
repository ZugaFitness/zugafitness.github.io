import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

# Since the previous replacement failed (likely due to the previous regex eating the end section incorrectly, or wait... let's just use string replace on a specific chunk).
# Wait, let's look for the old reels block in the file right now.
# Actually, the file currently still has this block:
#  <section class="py-8 mt-8 border-t border-gray-100">
#    <h3 class="text-xl font-bold text-center text-gray-800 mb-6">See the Coaching in Action</h3>

# Let's replace that entire section up to </section>

new_reels = """
<style>
  /* Auto-sliding marquee animation for reels */
  @keyframes marquee {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-50%); }
  }
  .marquee-container {
    overflow: hidden;
    white-space: nowrap;
    position: relative;
    width: 100vw;
    left: 50%;
    transform: translateX(-50%);
    padding: 1rem 0;
  }
  .marquee-track {
    display: inline-flex;
    gap: 1.5rem;
    animation: marquee 35s linear infinite;
  }
  .marquee-track:hover {
    animation-play-state: paused;
  }
  .marquee-item {
    flex: 0 0 auto;
    width: 320px;
    white-space: normal;
    border-radius: 1rem;
    overflow: hidden;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    background: white;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .marquee-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  }
  .marquee-item blockquote {
    margin: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 100% !important;
  }
</style>

<section class="py-20 bg-gray-50 overflow-hidden fade-in-section">
  <div class="text-center mb-12 px-4">
    <h2 class="text-sm font-bold tracking-widest text-orange-500 uppercase mb-3">In Action</h2>
    <h3 class="text-3xl md:text-5xl font-bold text-gray-900" style="font-family: 'Source Serif 4', serif;">
      Experience the Coaching
    </h3>
    <p class="text-gray-600 mt-4 max-w-2xl mx-auto">Real results, mindful movement, and functional training clips.</p>
  </div>

  <div class="marquee-container">
    <div class="marquee-track">
      <!-- Original Set -->
      <div class="marquee-item">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/Db90UwaT8eN/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14"></blockquote>
      </div>
      <div class="marquee-item">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/Ddsm5UqT7-3/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14"></blockquote>
      </div>
      <div class="marquee-item">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/DMHQqMdRdcg/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14"></blockquote>
      </div>
      <div class="marquee-item">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/DLPQIUWPZ--/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14"></blockquote>
      </div>

      <!-- Duplicate Set for Infinite Loop -->
      <div class="marquee-item">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/Db90UwaT8eN/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14"></blockquote>
      </div>
      <div class="marquee-item">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/Ddsm5UqT7-3/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14"></blockquote>
      </div>
      <div class="marquee-item">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/DMHQqMdRdcg/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14"></blockquote>
      </div>
      <div class="marquee-item">
        <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/DLPQIUWPZ--/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14"></blockquote>
      </div>
    </div>
  </div>
</section>
"""

import re
html = re.sub(r'<section class="py-8 mt-8 border-t border-gray-100">.*?</section>', new_reels, html, flags=re.DOTALL)

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
