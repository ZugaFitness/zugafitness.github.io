from playwright.sync_api import sync_playwright
import os

def verify_forms():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        base_path = os.getcwd()

        # Check free-trial.html form
        page.goto(f'file://{base_path}/free-trial.html')
        page.wait_for_selector('#zuga-free-trial-form')
        page.screenshot(path='/home/jules/verification/free_trial_form_v2.png', full_page=False)
        print("Captured screenshot of free-trial.html form.")

        # Check index.html contact form
        page.goto(f'file://{base_path}/index.html')
        page.wait_for_selector('#zuga-contact-form')
        page.evaluate("document.getElementById('zuga-contact-form').scrollIntoView()")
        page.screenshot(path='/home/jules/verification/contact_form_v2.png', full_page=False)
        print("Captured screenshot of index.html contact form.")

        # Check thank-you.html
        page.goto(f'file://{base_path}/thank-you.html')
        page.screenshot(path='/home/jules/verification/thank_you_page_v2.png', full_page=True)
        print("Captured screenshot of thank-you.html.")

        browser.close()

if __name__ == "__main__":
    os.makedirs('/home/jules/verification', exist_ok=True)
    verify_forms()
