import re

def main():
    with open("sitemap.xml", "r", encoding="utf-8") as f:
        sitemap = f.read()

    today = "2026-11-01"

    new_entries = f"""
  <url>
    <loc>https://zugafitness.in/privacy-policy.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://zugafitness.in/terms-of-service.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://zugafitness.in/refund-policy.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>"""

    sitemap = sitemap.replace("</urlset>", new_entries)

    touched_urls = [
        "https://zugafitness.in/Blog/index.html",
        "https://zugafitness.in/Blog/yoga-and-strength-training-for-pcod.html",
        "https://zugafitness.in/Online-Pranayama-Classes.html",
        "https://zugafitness.in/Blog/yoga-for-pcos-safe-poses-stress-hormones.html",
        "https://zugafitness.in/trainer-bench.html",
        "https://zugafitness.in/Blog/zumba-vs-gym-vs-yoga-weight-loss.html"
    ]

    for url in touched_urls:
        pattern = re.compile(rf'(<loc>{re.escape(url)}</loc>\s*<lastmod>)[^<]+(</lastmod>)')
        sitemap = pattern.sub(rf'\g<1>{today}\g<2>', sitemap)

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

if __name__ == "__main__":
    main()
