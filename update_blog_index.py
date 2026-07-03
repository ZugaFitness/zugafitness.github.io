import re

content = open("Blog/index.html", "r", encoding="utf-8").read()

new_card = """
            <!-- New Blog: Dance Fitness for Weight Loss Real Results -->
            <a href="dance-fitness-weight-loss-real-results.html" class="blog-card" data-category="dance-fitness">
                <div class="blog-image">
                    <img src="../assets/images/default-yoga-class.jpg" alt="Dance Fitness for Weight Loss" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <div class="blog-content">
                    <div>
                        <div class="blog-meta">
                            <span><i class="far fa-calendar"></i> July 3, 2026</span>
                            <span class="blog-category">Dance Fitness</span>
                        </div>
                        <h3 class="blog-title">Dance Fitness for Weight Loss: Real Results from Real Students</h3>
                        <p class="blog-excerpt">For the modern professional aged 25–45, the quest for weight management is often a cycle of failed gym memberships and unsustainable restrictive diets. Discover how dance fitness offers a vibrant, community-driven alternative.</p>
                    </div>
                    <span class="read-article-cue">Read Article →</span>
                </div>
            </a>
"""

new_content = content.replace("<!-- Start of blog cards -->", "<!-- Start of blog cards -->\n" + new_card)

with open("Blog/index.html", "w", encoding="utf-8") as f:
    f.write(new_content)
