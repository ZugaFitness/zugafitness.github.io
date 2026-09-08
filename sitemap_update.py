import re

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

new_entry = """  <url>
    <loc>https://zugafitness.in/corporate-wellness-productivity.html</loc>
    <lastmod>2023-10-27T00:00:00+00:00</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

content = content.replace('</urlset>', new_entry)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(content)
