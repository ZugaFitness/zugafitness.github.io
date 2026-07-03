import re

content = open("sitemap.xml", "r", encoding="utf-8").read()

new_url = """
  <url>
    <loc>https://zugafitness.in/Blog/dance-fitness-weight-loss-real-results.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

new_content = content.replace("</urlset>", new_url)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(new_content)
