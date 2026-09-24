import re
import json

files = ["germany-online-yoga-classes.html", "Online-Yoga-Classes.html"]

faq_html = """
        <div class="faq-item">
            <div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq-tech">What technology do I need to join an online yoga class? <span>+</span></div>
            <div id="faq-tech" class="collapse mt-3">
                <p>Just four things: a smartphone, laptop or tablet, a stable internet connection, your yoga mat, and the Zoom link we send before every session - nothing else.</p>
            </div>
        </div>
"""

faq_schema_item = {
    "@type": "Question",
    "name": "What technology do I need to join an online yoga class?",
    "acceptedAnswer": {
        "@type": "Answer",
        "text": "Just four things: a smartphone, laptop or tablet, a stable internet connection, your yoga mat, and the Zoom link we send before every session - nothing else."
    }
}

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Insert FAQ HTML
    last_faq = """<div class="faq-question" data-bs-toggle="collapse" data-bs-target="#faq4">Can I switch between yoga styles? <span>+</span></div>
          <div id="faq4" class="collapse mt-3">
            <p>Yes — Growth plan members get access to all 8 styles across all 5 timezone slots. Starter plan members choose one style per month.</p>
          </div>
        </div>"""

    html = html.replace(last_faq, last_faq + "\n" + faq_html)

    # Insert Schema
    schema_match = re.search(r'(<script type="application/ld\+json">.*?)(</script>)', html, re.DOTALL)
    if schema_match:
        schemas = html.split('<script type="application/ld+json">')
        for i, schema_content in enumerate(schemas[1:]):
            if '"@type": "FAQPage"' in schema_content:
                try:
                    schema_json_str = schema_content.split('</script>')[0]
                    schema_data = json.loads(schema_json_str)

                    if "@graph" in schema_data:
                        for item in schema_data["@graph"]:
                            if item.get("@type") == "FAQPage":
                                item["mainEntity"].append(faq_schema_item)
                    else:
                        schema_data["mainEntity"].append(faq_schema_item)

                    updated_schema_str = json.dumps(schema_data, indent=2)
                    html = html.replace(schema_json_str, updated_schema_str)
                except Exception as e:
                    print("Error updating schema for", file_path, e)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
