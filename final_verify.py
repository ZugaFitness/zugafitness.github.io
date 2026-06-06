import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Test Pricing Page
        file_path = "file://" + os.path.abspath("pricing.html")
        await page.goto(file_path)

        # 1. Check Toggle Buttons
        await page.wait_for_selector("#pricing-yoga", state="visible")
        await page.click("#btn-dance")
        await page.wait_for_selector("#pricing-dance", state="visible")
        print("Toggle Buttons: OK")

        # 2. Check Billing Switch (Dance)
        starter_dance_price = await page.inner_text("#price-starter-dance")
        print(f"Starter Dance Price (Monthly): {starter_dance_price}")

        # Annual toggle
        await page.click(".slider")
        await asyncio.sleep(0.5)

        starter_dance_annual = await page.inner_text("#price-starter-dance")
        print(f"Starter Dance Price (Annual): {starter_dance_annual}")

        annual_label_dance = await page.evaluate("document.getElementById('annual-starter-dance').style.display")
        print(f"Annual Label Dance Visibility: {annual_label_dance}")

        # 3. Check Billing Switch (Yoga)
        await page.click("#btn-yoga")
        await page.wait_for_selector("#pricing-yoga", state="visible")

        starter_yoga_annual = await page.inner_text("#price-starter-yoga")
        print(f"Starter Yoga Price (Annual): {starter_yoga_annual}")

        annual_label_yoga = await page.evaluate("document.getElementById('annual-starter-yoga').style.display")
        print(f"Annual Label Yoga Visibility: {annual_label_yoga}")

        # 4. Check Dance Page
        dance_file_path = "file://" + os.path.abspath("Online-Dance-Fitness-Classes.html")
        await page.goto(dance_file_path)
        pricing_text = await page.inner_text("p:has-text('Plans from ₹2,000/month')")
        print(f"Dance Page Pricing Text: {pricing_text}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
