import re

with open("Blog/index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_card = """        <!-- Blog Card -->
        <div class="col-md-6 col-lg-4 blog-card" data-category="health">
          <a class="card-link" href="/Blog/zumba-vs-gym-vs-yoga-weight-loss.html">
            <div class="card-image">
              <img
                alt="Zumba vs Gym Cardio vs Yoga: Which Actually Burns More Fat?"
                loading="lazy"
                onerror="
                  this.onerror = null;
                  this.src =
                    '../assets/images/online-zumba-classes-at-home.webp';
                "
                src="../assets/images/online-zumba-classes-at-home.webp"
              />
            </div>
            <div class="card-content">
              <h3>Zumba vs Gym Cardio vs Yoga: Which Actually Burns More Fat?</h3>
              <p>
                Choosing between Zumba, gym cardio and yoga for weight loss? Here is the honest calorie math, the muscle-protection truth, and how to combine them for real body recomposition.
              </p>
              <span class="read-more"
                >Read Article <i class="fas fa-arrow-right"></i
              ></span>
            </div>
          </a>
        </div>
"""

# Let's find: `        <!-- Blog Card -->\n        <div class="col-md-6 col-lg-4 blog-card" data-category="health"></div>`
# and insert the new card there.
html = re.sub(
    r'(        <!-- Blog Card -->\n        <div class="col-md-6 col-lg-4 blog-card" data-category="health"></div>)',
    r'\g<1>\n' + new_card,
    html,
    count=1
)

with open("Blog/index.html", "w", encoding="utf-8") as f:
    f.write(html)
