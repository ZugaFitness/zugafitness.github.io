import re
from datetime import datetime

with open("sitemap.xml", "r") as f:
    sitemap = f.read()

# Update the lastmod for weight-loss-challenge.html and make sure priority is 0.8
today = datetime.now().strftime("%Y-%m-%d")

# The block looks like:
#  <url>
#    <loc>https://zugafitness.in/weight-loss-challenge.html</loc>
#    <lastmod>2026-07-08</lastmod>
#    <changefreq>weekly</changefreq>
#    <priority>0.8</priority>
#  </url>

pattern = r'(<loc>https://zugafitness.in/weight-loss-challenge\.html</loc>\s*<lastmod>)[^<]+(</lastmod>)'
sitemap = re.sub(pattern, rf'\g<1>{today}\g<2>', sitemap)

# Check if priority exists for this URL block
if '<priority>0.8</priority>' not in sitemap[sitemap.find('weight-loss-challenge.html'):sitemap.find('weight-loss-challenge.html')+200]:
    # Replace the block to add priority
    pass

# Alternatively, a safer regex specifically for this block:
block_pattern = r'(<url>\s*<loc>https://zugafitness\.in/weight-loss-challenge\.html</loc>.*?)</url>'
def replace_block(match):
    block = match.group(1)
    if '<priority>' not in block:
        block += '\n    <priority>0.8</priority>\n  '
    return block + '</url>'

sitemap = re.sub(block_pattern, replace_block, sitemap, flags=re.DOTALL)

with open("sitemap.xml", "w") as f:
    f.write(sitemap)
print("Sitemap updated.")
