import os
import glob
from html.parser import HTMLParser

# Because beautiful soup is not available and destructive to massive files, we will use a safe string injection that exactly finds the right node.
import re

def process_file(filepath):
    # Exclusions
    exclusions = [
        "thank-you.html",
        "assets/docs/sample-participation-report.html",
        "Online-Personal-Training-classes.html",
        "Blog/when-to-start-yoga-after-childbirth.html",
        "Blog/yoga-results-timeline-how-long-to-see-changes.html", # retiring how-long post
        "live_html/pt2.html"
    ]
    if any(filepath.endswith(excl) for excl in exclusions):
        return False
    if "live_html/" in filepath.replace("\\", "/"):
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    if '<meta name="robots" content="noindex"' in html or '<meta name="robots" content="noindex, follow"' in html:
        return False
    if '<meta http-equiv="refresh"' in html:
        return False
    if '<!-- zuga:footer-trust-v1 -->' in html:
        return False

    trust_html = """<!-- zuga:footer-trust-v1 -->
<div style="font-size:12px; line-height:1.5; opacity:.85; max-width:900px; margin:24px auto; padding:0 16px;">
  <div style="text-align:center; margin-bottom:12px;">
    <a href="/privacy-policy.html" style="color:inherit;text-decoration:underline;">Privacy Policy</a> |
    <a href="/terms-of-service.html" style="color:inherit;text-decoration:underline;">Terms of Service</a> |
    <a href="/refund-policy.html" style="color:inherit;text-decoration:underline;">Refund Policy</a>
  </div>
  <p style="text-align:center;">Zuga Fitness provides movement, breathwork and dance fitness education and practice. We do not diagnose or treat medical or psychological conditions. Our sessions complement - never replace - care from a qualified physician or therapist. Consult your doctor before beginning any new exercise programme, particularly during pregnancy, postpartum, or while managing an existing health condition.</p>
</div>"""

    # Check if </footer> exists
    if re.search(r'</footer>', html, re.IGNORECASE):
        # Insert before the LAST </footer> to be safe
        parts = re.split(r'(</footer>)', html, flags=re.IGNORECASE)
        if len(parts) >= 3:
            new_html = "".join(parts[:-2]) + trust_html + parts[-2] + parts[-1]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_html)
            return True

    # Check if </body> exists
    if re.search(r'</body>', html, re.IGNORECASE):
        parts = re.split(r'(</body>)', html, flags=re.IGNORECASE)
        if len(parts) >= 3:
            new_html = "".join(parts[:-2]) + f"\n<section>\n{trust_html}\n</section>\n" + parts[-2] + parts[-1]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_html)
            return True

    return False

def main():
    for filepath in glob.glob("**/*.html", recursive=True):
        process_file(filepath)

if __name__ == "__main__":
    main()
