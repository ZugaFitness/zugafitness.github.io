import sys
import os
import urllib.parse
from playwright.sync_api import sync_playwright

def generate_screenshot(html_path, output_image_path):
    # Get the absolute path to the HTML file
    abs_html_path = os.path.abspath(html_path)

    # Convert it to a file:// URL
    file_url = "file://" + urllib.parse.quote(abs_html_path)
    print(f"Loading {file_url}")

    with sync_playwright() as p:
        # Launch Chromium browser
        browser = p.chromium.launch(headless=True)
        # Create a new page
        page = browser.new_page(viewport={'width': 1280, 'height': 1500})

        # Navigate to the local file URL
        page.goto(file_url, wait_until="networkidle")

        # Take a screenshot
        page.screenshot(path=output_image_path, full_page=True)

        # Close the browser
        browser.close()
        print(f"Screenshot saved to {output_image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_screenshot.py <path_to_html> <output_image_path>")
        sys.exit(1)

    html_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(html_file):
        print(f"Error: HTML file '{html_file}' not found.")
        sys.exit(1)

    generate_screenshot(html_file, output_file)
