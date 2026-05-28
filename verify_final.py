from playwright.sync_api import sync_playwright, expect
import os

def verify_canonical_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the file
        file_path = "file://" + os.path.abspath("Blog/corporate-yoga-day-bangalore.html")
        print(f"Navigating to {file_path}")

        page.goto(file_path)

        # Check if the canonical tag is present
        canonical = page.locator('link[rel="canonical"]')
        expect(canonical).to_have_attribute("href", "https://zugafitness.in/corporate-yoga-day-bangalore.html")

        # Take a screenshot to verify UI
        page.screenshot(path="/home/jules/verification/final_verification.png", full_page=False)

        # Print the canonical tag for confirmation
        href = canonical.get_attribute("href")
        print(f"Verified canonical tag: {href}")

        browser.close()

if __name__ == "__main__":
    if not os.path.exists("/home/jules/verification"):
        os.makedirs("/home/jules/verification")
    verify_canonical_page()
