from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("file:///app/Online-Personal-Training-classes.html")
    page.wait_for_timeout(500)

    # Scroll to Takeaways
    page.evaluate("window.scrollTo(0, document.body.scrollHeight/2)")
    page.wait_for_timeout(500)

    # Check updated color of Apply button
    page.screenshot(path="/app/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/app/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
