import os
from playwright.sync_api import sync_playwright

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Free Trial Page
        page.goto(f"file://{os.getcwd()}/free-trial.html")
        page.set_viewport_size({"width": 1280, "height": 1600})
        # Scroll to form
        page.evaluate("document.querySelector('#zuga-free-trial-form').scrollIntoView()")
        page.screenshot(path="verification/free_trial_form_v2.png")
        print("Captured free_trial_form_v2.png")

        # Contact Form on Index
        page.goto(f"file://{os.getcwd()}/index.html")
        page.set_viewport_size({"width": 1280, "height": 2000})
        # Scroll to contact form
        page.evaluate("document.querySelector('#form02-6').scrollIntoView()")
        page.screenshot(path="verification/contact_form_v2.png")
        print("Captured contact_form_v2.png")

        browser.close()

if __name__ == "__main__":
    capture_screenshots()
