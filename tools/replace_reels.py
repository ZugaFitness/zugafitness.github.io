import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

# Current reels section:
# <section class="py-8 mt-8 border-t border-gray-100">
#    <h3 class="text-xl font-bold text-center text-gray-800 mb-6">See the Coaching in Action</h3>
#    ...
#    <p class="text-center text-gray-500 text-sm mt-2 md:hidden">← Swipe to see more →</p>
#  </section>

# New animated reels section:
new_reels = """
<style>
  /* Auto-sliding marquee animation for reels */
  @keyframes marquee {
    0% { transform: translateX(0%); }
    100% { transform: translateX(-50%); } /* Translate by -50% because we'll duplicate the track to make it infinite */
  }
  .marquee-container {
    overflow: hidden;
    white-space: nowrap;
    position: relative;
    width: 100vw;
    margin-left: 50%;
    transform: translateX(-50%);
    padding: 1rem 0;
  }
  .marquee-track {
    display: inline-flex;
    gap: 1.5rem;
    animation: marquee 35s linear infinite;
    /* Pause animation on hover for better user experience */
    /* Note: Instagram embeds are complex iframes, so hover pausing on mobile can be tricky, but works on desktop */
  }
  .marquee-track:hover {
    animation-play-state: paused;
  }
  .marquee-item {
    flex: 0 0 auto;
    width: 300px;
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
  /* Ensure blockquotes fill the item */
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

# Replace the old reels section
# Let's find it. It's the section with `border-t border-gray-100` right after Specialties,
# and it ends before the "Practice Gallery" section (but we also have the old CTA block inside it, or wait...
# Wait, the CTA block is right below the reels in the original HTML:
#   <p class="text-center text-gray-500 text-sm mt-2 md:hidden">← Swipe to see more →</p>
#  </section>
#  <!-- Single High-Ticket CTA -->

# Actually in our previous replace, the HTML was restructured. Let's read the current HTML to be safe.
html = re.sub(r'<section class="py-8 mt-8 border-t border-gray-100">.*?</section>', new_reels, html, flags=re.DOTALL)

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
