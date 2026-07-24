from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    # The files are static HTML. Let's serve them locally on port 8000
    # and visit them.
    page.goto("http://localhost:8000/Blog/index.html")
    page.wait_for_timeout(1000)

    # Scroll to see the blog cards
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/index_cards.png")
    page.wait_for_timeout(1000)

    # Click on Moorcha Pranayama card
    page.get_by_role("link", name="Moorcha Pranayama Benefits").click()
    page.wait_for_timeout(1000)

    # Scroll to the bottom to see the CTA
    page.evaluate("window.scrollTo(0, document.body.scrollHeight - 1000)")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/moorcha_cta.png")
    page.wait_for_timeout(1000)

    # Go to Sheetkari Pranayama page directly
    page.goto("http://localhost:8000/Blog/sheetkari-pranayama-benefits.html")
    page.wait_for_timeout(1000)

    # Scroll to the bottom to see the CTA
    page.evaluate("window.scrollTo(0, document.body.scrollHeight - 1000)")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/sheetkari_cta.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
