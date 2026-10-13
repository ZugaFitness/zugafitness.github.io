import os

# Define the domain
DOMAIN = "https://zugafitness.in"

# Top level pages that are article-like
top_level_pages = [
    "Online-Yoga-Classes-For-PCOD.html",
    "Online-Postpartum-Yoga-Classes.html",
    "Online-Pranayama-Classes.html",
    "australia-online-yoga-classes.html",
    "canada-online-yoga-classes.html",
    "germany-online-yoga-classes.html",
    "uae-online-yoga-classes.html",
    "uk-online-yoga-classes.html",
    "usa-online-yoga-classes.html",
    "apartment-wellness-bangalore.html",
    "corporate-wellness-bangalore.html",
]

# Get all Blog pages
blog_pages = []
for file in os.listdir("Blog"):
    if file.endswith(".html") and file != "index.html" and not file.startswith("Blog"):
        blog_pages.append(f"Blog/{file}")

# Combine and sort
all_pages = top_level_pages + blog_pages
all_pages.sort()

# Generate Markdown
md_content = """# Zuga to Medium Canonical Mapping

**Instruction:** Only rows with a filled Medium URL need a canonical check; blank rows = never syndicated, no action.

| Zuga Original URL | Medium Story URL | Canonical Set? (Y/N) |
| --- | --- | --- |
"""

for page in all_pages:
    url = f"{DOMAIN}/{page}"
    md_content += f"| {url} | [PARTNER: paste Medium story URL] | |\n"

os.makedirs("seo", exist_ok=True)
with open("seo/medium-canonical-map.md", "w") as f:
    f.write(md_content)

print("Generated seo/medium-canonical-map.md")
