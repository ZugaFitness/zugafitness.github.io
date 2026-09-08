import re

with open('corporate-wellness-productivity.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title
content = re.sub(
    r'<title>.*?</title>',
    '<title>Corporate Wellness for Founders: Boost Productivity &amp; Retention | Zuga Fitness</title>',
    content,
    flags=re.DOTALL
)

# Update description
content = re.sub(
    r'<meta content=".*?" name="description"/>',
    '<meta content="Workplace wellness isn\'t a perk; it\'s a productivity multiplier. Live, instructor-led wellness programs designed to reduce burnout and boost team performance. Custom corporate quotes." name="description"/>',
    content,
    flags=re.DOTALL
)

# Update og:title
content = re.sub(
    r'<meta content=".*?" property="og:title"/>',
    '<meta content="Corporate Wellness for Founders: Boost Productivity &amp; Retention | Zuga Fitness" property="og:title"/>',
    content,
    flags=re.DOTALL
)

# Update og:description
content = re.sub(
    r'<meta content=".*?" property="og:description"/>',
    '<meta content="Workplace wellness isn\'t a perk; it\'s a productivity multiplier. Live, instructor-led wellness programs designed to reduce burnout and boost team performance. Custom corporate quotes." property="og:description"/>',
    content,
    flags=re.DOTALL
)

# Update og:url
content = re.sub(
    r'<meta content="https://zugafitness.in/corporate-wellness-bangalore.html" property="og:url"/>',
    '<meta content="https://zugafitness.in/corporate-wellness-productivity.html" property="og:url"/>',
    content,
    flags=re.DOTALL
)

# Update twitter:title
content = re.sub(
    r'<meta content=".*?" name="twitter:title"/>',
    '<meta content="Corporate Wellness for Founders: Boost Productivity &amp; Retention | Zuga Fitness" name="twitter:title"/>',
    content,
    flags=re.DOTALL
)

# Update twitter:description
content = re.sub(
    r'<meta content=".*?" name="twitter:description"/>',
    '<meta content="Workplace wellness isn\'t a perk; it\'s a productivity multiplier. Live, instructor-led wellness programs designed to reduce burnout and boost team performance. Custom corporate quotes." name="twitter:description"/>',
    content,
    flags=re.DOTALL
)

# Update canonical
content = re.sub(
    r'<link href="https://zugafitness.in/corporate-wellness-bangalore.html" rel="canonical"/>',
    '<link href="https://zugafitness.in/corporate-wellness-productivity.html" rel="canonical"/>',
    content,
    flags=re.DOTALL
)

# Replace Service JSON-LD
schema_regex = re.compile(r'<script type="application/ld\+json">\s*{\s*"@context": "https://schema\.org",\s*"@type": "Service".*?}\s*</script>', re.DOTALL)
new_schema = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Corporate Wellness & Productivity Programs",
  "description": "Live, instructor-led corporate wellness programs designed to boost productivity, reduce burnout, and improve team retention.",
  "provider": {
    "@type": "Organization",
    "name": "Zuga Fitness",
    "url": "https://zugafitness.in"
  },
  "areaServed": "Global",
  "url": "https://zugafitness.in/corporate-wellness-productivity.html"
}
</script>"""

content = schema_regex.sub(new_schema, content)

with open('corporate-wellness-productivity.html', 'w', encoding='utf-8') as f:
    f.write(content)
