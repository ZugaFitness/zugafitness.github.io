import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # file path needs to be absolute
        filepath = os.path.abspath('Blog/zumba-vs-gym-vs-yoga-weight-loss.html')
        await page.goto(f'file://{filepath}')

        # Scroll to bottom
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight/2)')
        await asyncio.sleep(1) # wait a little
        print("Page rendered and scrolled to bottom successfully")
        await page.screenshot(path="verification_scroll.png")
        await browser.close()

asyncio.run(run())
