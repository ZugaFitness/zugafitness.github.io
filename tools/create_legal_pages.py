import json

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta}">
    <link rel="canonical" href="{url}">
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
        header, footer {{ background: #f8f9fa; padding: 20px; text-align: center; }}
        main {{ max-width: 800px; margin: 40px auto; padding: 0 20px; }}
        h1 {{ color: #222; }}
    </style>
    <script type="application/ld+json">
    {schema}
    </script>
</head>
<body>
    <header>
        <a href="/">Zuga Fitness</a>
    </header>
    <main>
        {body}
    </main>
    <footer>
    </footer>
</body>
</html>"""

def make_schema(title, url):
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{url}#webpage",
                "url": url,
                "name": title
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{url}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": "https://zugafitness.in/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": title,
                        "item": url
                    }
                ]
            }
        ]
    }
    return json.dumps(schema, indent=4)

privacy_body = """<h1>Privacy Policy</h1>
<p>We are Zuga Fitness, Bengaluru, India. Contact: hello@zugafitness.in / +91 76763 79909.</p>
<p>What we collect: your name, email, phone or WhatsApp number, city and timezone; any health, pregnancy or injury information you choose to share in booking or intake forms so we can keep sessions safe; payment records handled by our payment provider (we never store card details); attendance and feedback notes from your sessions.</p>
<p>How we use it: to schedule and deliver your classes; to screen for safety and adapt sessions; to send session links, schedules and practice notes you opted into; to produce participation reports for corporate bookings (attendance, department split and quotes, anonymised unless you agree otherwise); to improve our classes; and to meet legal obligations.</p>
<p>What we never do: we do not sell your personal data, and we do not share it except with service processors (video conferencing, payments, WhatsApp, email, analytics) bound by confidentiality.</p>
<p>Cookies and analytics: we use Google Tag Manager, Google Analytics and Meta Pixel to understand site usage. You can block these in your browser settings.</p>
<p>Retention: booking records for 3 years; health disclosures only as long as needed for session safety and deleted on request; marketing consent until you withdraw it.</p>
<p>Your rights: access, correction, deletion, export and withdrawal of consent - email hello@zugafitness.in and we will respond within 30 days.</p>
<p>Children: classes are for ages 16+; children's sessions require parental consent and supervision.</p>
<p>Changes: updates are posted on this page with a new date.</p>
<p>Last updated: 2026-11-01</p>"""

terms_body = """<h1>Terms of Service</h1>
<p>1. Our services. Zuga Fitness delivers live online and onsite (Bengaluru) yoga, breathwork and dance fitness classes, workshops and corporate programmes. These are educational movement practice, not medical or psychological treatment, and they complement - never replace - care from a qualified physician or therapist. Consult your doctor before beginning, particularly during pregnancy, postpartum, or while managing an existing health condition.</p>
<p>2. Bookings and access. Session links are sent per your schedule; onsite sessions run per confirmed booking. Recordings, where offered, are licensed for your personal use only and may not be redistributed.</p>
<p>3. Your commitments. Provide accurate health and safety information; follow instructor modifications; practise in a safe space; treat participants and instructors with respect.</p>
<p>4. Payments. Prices are as published or quoted; GST applies where applicable; corporate and agency engagements are governed by their contract.</p>
<p>5. Cancellations. You may reschedule a live class up to 12 hours before start, subject to your pack's validity. Sessions cancelled by us are credited or rescheduled in full.</p>
<p>6. Changes. Schedules and formats may change with notice; a substitute instructor of equivalent certification may be assigned where necessary.</p>
<p>7. Liability. You participate at your own risk and must disclose relevant conditions. To the extent permitted by law, our liability is limited to fees paid and excludes indirect losses.</p>
<p>8. Intellectual property. All class content and site materials are owned by Zuga Fitness; no recording or republication without written permission.</p>
<p>9. Governing law. Laws of India; courts of Bengaluru, Karnataka. Contact: hello@zugafitness.in. Last updated: 2026-11-01</p>"""

refund_body = """<h1>Refund Policy</h1>
<p>Class packs: unused sessions are refundable pro-rata within 90 days of purchase, minus attended sessions at the single-class rate; packs expire at their stated validity.</p>
<p>Memberships: cancel anytime by email, effective at the end of the paid period; the first 7 days of a first membership are fully refundable if you attended no more than 2 classes.</p>
<p>Cohorts and programmes (Weight Loss Challenge, PCOS, Postpartum): full refund within 7 days of start if you attended 2 or fewer sessions; thereafter pro-rata for unstarted weeks, excluding materials already delivered.</p>
<p>Single classes: reschedulable up to 12 hours before start; no-shows are not refundable.</p>
<p>Onsite and corporate bookings: per contract - 50% deposit on confirmation; free cancellation more than 72 hours before the session; 50% within 72 hours; emergency deployment surcharge is non-refundable once deployed.</p>
<p>Processing: approved refunds reach the original payment method in 5-7 business days. Request via hello@zugafitness.in with your order details; we respond within 3 business days.</p>
<p>Exceptions: medical emergencies are considered case by case with documentation; instructor-cancelled sessions are always refunded or credited in full. Last updated: 2026-11-01</p>"""

pages = [
    {
        "file": "privacy-policy.html",
        "title": "Privacy Policy | Zuga Fitness",
        "meta": "How Zuga Fitness collects, uses and protects your data - bookings, health disclosures, payments, cookies and your rights.",
        "url": "https://zugafitness.in/privacy-policy.html",
        "body": privacy_body
    },
    {
        "file": "terms-of-service.html",
        "title": "Terms of Service | Zuga Fitness",
        "meta": "The terms on which Zuga Fitness delivers live online and onsite yoga, breathwork and dance fitness classes.",
        "url": "https://zugafitness.in/terms-of-service.html",
        "body": terms_body
    },
    {
        "file": "refund-policy.html",
        "title": "Refund Policy | Zuga Fitness",
        "meta": "How refunds work for class packs, memberships, cohorts and corporate bookings at Zuga Fitness.",
        "url": "https://zugafitness.in/refund-policy.html",
        "body": refund_body
    }
]

for p in pages:
    schema = make_schema(p["title"].split(" | ")[0], p["url"])
    content = base_html.format(
        title=p["title"],
        meta=p["meta"],
        url=p["url"],
        schema=schema,
        body=p["body"]
    )
    with open(p["file"], "w", encoding="utf-8") as f:
        f.write(content)
