from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Check the newly added blog post
    page.goto("http://localhost:3000/Blog/dance-fitness-weight-loss-real-results.html")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/blog_post.png", full_page=True)
    page.wait_for_timeout(1000)

    # Check the blog index page
    page.goto("http://localhost:3000/Blog/")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/screenshots/blog_index.png", full_page=True)
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    import os
    os.makedirs("/home/jules/verification/videos", exist_ok=True)
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
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
