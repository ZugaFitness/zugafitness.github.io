import asyncio
from playwright.async_api import async_playwright
import os
import json

# Define the data for the 5 pins
PINS = [
    {
        "slug": "zumba-vs-gym-vs-yoga-weight-loss",
        "badge": "health",
        "headline": "Zumba vs Gym Cardio vs Yoga",
        "subhead": "Which Actually Burns More Fat?",
        "bg_image": "../assets/images/online-zumba-classes-at-home.webp"
    },
    {
        "slug": "online-yoga-classes-for-pcod",
        "badge": "Women's Health",
        "headline": "Manage PCOD Naturally with Yoga",
        "subhead": "Discover specific asanas that help balance hormones and reduce symptoms.",
        "bg_image": "../assets/images/yoga-for-pcos-balance.webp"
    },
    {
        "slug": "postpartum-yoga-when-to-start",
        "badge": "Postnatal Care",
        "headline": "When to Start Postpartum Yoga",
        "subhead": "A safe timeline for new moms to rebuild core strength after childbirth.",
        "bg_image": "../assets/images/postpartum-yoga-when-to-start.webp"
    },
    {
        "slug": "is-zumba-good-for-weight-loss",
        "badge": "Cardio Dance",
        "headline": "Is Zumba Good for Weight Loss?",
        "subhead": "How dancing burns calories while feeling more like a party than a workout.",
        "bg_image": "../assets/images/online-zumba-classes-at-home.webp"
    },
    {
        "slug": "yoga-for-desk-workers",
        "badge": "Office Relief",
        "headline": "Quick Yoga Fixes for Desk Workers",
        "subhead": "Relieve neck tension, open tight hips, and fix posture without leaving your chair.",
        "bg_image": "../assets/images/yoga-for-back-pain-asanas-guide.webp"
    },
    {
        "slug": "can-yoga-help-with-sleep",
        "badge": "Better Rest",
        "headline": "Can Yoga Actually Help You Sleep?",
        "subhead": "Calm your nervous system tonight with these simple bedtime breathing techniques.",
        "bg_image": "../assets/images/yoga-for-better-sleep.webp"
    }
]

async def main():
    # Make sure output directory exists
    os.makedirs("seo/pins", exist_ok=True)

    # Absolute path for local file viewing
    # The file path in the workspace needs to be absolute
    current_dir = os.path.abspath(os.getcwd())
    template_path = f"file://{current_dir}/seo/pinterest-pin-template.html"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Set exact dimensions
        page = await browser.new_page(viewport={"width": 1000, "height": 1500})

        for pin in PINS:
            print(f"Generating pin for {pin['slug']}...")
            await page.goto(template_path)

            # Inject data using parameterized evaluation
            await page.evaluate("""([bg, badge, headline, subhead]) => {
                document.getElementById('dynamic-bg').src = bg;
                document.getElementById('dynamic-badge').innerText = badge;
                document.getElementById('dynamic-headline').innerText = headline;
                document.getElementById('dynamic-subhead').innerText = subhead;
            }""", [pin["bg_image"], pin["badge"], pin["headline"], pin["subhead"]])

            # Wait a moment for image to load and fonts to render
            await page.wait_for_timeout(2000)

            # Take screenshot
            output_path = f"seo/pins/{pin['slug']}.png"
            await page.screenshot(path=output_path, full_page=True)
            print(f"  -> Saved {output_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
