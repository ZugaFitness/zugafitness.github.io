import re
from datetime import date

with open("corporate-wellness-bangalore.html", "r") as f:
    content = f.read()

# Current date in ISO format
today = date.today().isoformat()

# Find the schema section
# We have two schemas, one at the top (which seems like an incomplete duplicate from previous edits or Mobirise) and one at the bottom. Wait, let's look at all application/ld+json blocks.

schema_matches = list(re.finditer(r'<script type="application/ld\+json">.*?</script>', content, re.DOTALL))

# The actual one to replace is likely the Service schema at the bottom.
schema_replacement = f"""<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Corporate Wellness & Yoga Programs in Bangalore",
    "serviceType": "Corporate Wellness, Corporate Yoga, and Corporate Zumba",
    "description": "Transform your workplace with Zuga Fitness. We offer premium Corporate Yoga for stress relief and high-energy Corporate Zumba for team building in offices across Bangalore.",
    "provider": {{
      "@type": "Organization",
      "name": "Zuga Fitness",
      "url": "https://zugafitness.in"
    }},
    "areaServed": "Bangalore, Karnataka, India",
    "url": "https://zugafitness.in/corporate-wellness-bangalore.html",
    "dateModified": "{today}",
    "offers": {{
      "@type": "Offer",
      "price": "5000",
      "priceCurrency": "INR",
      "description": "Flat rate per corporate wellness event or session in Bangalore."
    }}
  }}
  </script>"""

# Find the schema block that has "Service" and "Corporate Wellness & Yoga Programs"
def replace_service_schema(match):
    text = match.group(0)
    if '"@type": "Service"' in text and 'Corporate Wellness' in text:
        return schema_replacement
    return text

content = re.sub(r'<script type="application/ld\+json">.*?</script>', replace_service_schema, content, flags=re.DOTALL)

with open("corporate-wellness-bangalore.html", "w") as f:
    f.write(content)
