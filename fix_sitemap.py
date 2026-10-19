with open("sitemap.xml", "r", encoding="utf-8") as f:
    xml = f.read()

# find first </urlset>
idx = xml.find("</urlset>")
if idx != -1:
    xml = xml[:idx + len("</urlset>")]

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml)
