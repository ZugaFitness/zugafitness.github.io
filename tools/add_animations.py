import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

# I will add the CSS styles to the <head> section
animation_css = """
<style>
  /* Elite Scroll Animations */
  .fade-in-section {
    opacity: 0;
    transform: translateY(40px);
    visibility: hidden;
    transition: opacity 1s ease-out, transform 1s ease-out;
    will-change: opacity, visibility;
  }
  .fade-in-section.is-visible {
    opacity: 1;
    transform: none;
    visibility: visible;
  }
</style>
"""

# Find </head> and insert CSS right before it
html = html.replace('</head>', animation_css + '\n</head>')

# Add JS logic right before </body>
animation_js = """
<!-- Intersection Observer for Scroll Animations -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const observerOptions = {
      root: null,
      rootMargin: "0px",
      threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    document.querySelectorAll('.fade-in-section').forEach((section) => {
      observer.observe(section);
    });
  });
</script>
"""

# In the previous steps, we already added the `fade-in-section` class to our new sections.
html = html.replace('</body>', animation_js + '\n</body>')

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
