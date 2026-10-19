import re

with open("sitemap.xml", "r", encoding="utf-8") as f:
    xml = f.read()

new_entry = """  <url>
    <loc>https://zugafitness.in/Blog/zumba-vs-gym-vs-yoga-weight-loss.html</loc>
    <lastmod>2026-10-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""

# Add only if not exists
if "zumba-vs-gym-vs-yoga-weight-loss" not in xml:
    xml = re.sub(r'(</urlset>)', new_entry + '\n\\1', xml)
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)
