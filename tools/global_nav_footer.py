import os
from bs4 import BeautifulSoup

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Skip files that don't have basic structure or are stubs
    if "http-equiv=\"refresh\"" in html.lower() or not "<html" in html.lower():
        return False

    soup = BeautifulSoup(html, "html.parser")
    lines = html.splitlines(keepends=True)

    modified = False

    # 1. Header Nav Injection
    if "<!-- zuga:nav-hybrid-v1 -->" not in html:
        # Find Dance link in header nav
        for nav in soup.find_all(["nav", "ul"]):
            dance_li = None
            for li in nav.find_all("li"):
                text = li.get_text().lower()
                if "dance" in text or "zumba" in text:
                    dance_li = li
                    break

            if dance_li and dance_li.sourceline:
                # We know the sourceline of the <li> tag (1-indexed)
                line_idx = dance_li.sourceline - 1
                # we want to insert after the </li>. Let's find it.
                # we search forward for </li>
                for i in range(line_idx, len(lines)):
                    if "</li>" in lines[i]:
                        # Insert after this line
                        # Header nav format:
                        if nav.name == "ul" and nav.parent and nav.parent.name == "nav":
                            lines.insert(i + 1, '        <!-- zuga:nav-hybrid-v1 --><li><a href="/hybrid-fitness.html" class="nav-link">Hybrid</a></li>\n')
                        else:
                            # Footer nav format
                            lines.insert(i + 1, '            <!-- zuga:nav-hybrid-v1 --><li><a href="/hybrid-fitness.html">Hybrid</a></li>\n')
                        modified = True
                        break

    # Rejoin to reflect nav changes before finding footer
    if modified:
        html = "".join(lines)
        soup = BeautifulSoup(html, "html.parser")
        lines = html.splitlines(keepends=True)

    footer = soup.find("footer")
    if footer:
        # 3. Footer Social Links
        if "linkedin.com" not in html:
            social_row = footer.find(class_=lambda c: c and ("social" in c or "icons" in c))
            if social_row and social_row.sourceline:
                # find the closing </div> or container for social row
                line_idx = social_row.sourceline - 1

                # find the closing tag of this div
                closing_idx = -1
                for i in range(line_idx, len(lines)):
                    if "</div>" in lines[i]:
                        closing_idx = i
                        break

                if closing_idx != -1:
                    social_str = '\n          <a href="https://www.linkedin.com/company/zuga-fitness/" aria-label="LinkedIn" class="social-icon"><i class="fab fa-linkedin"></i></a>'
                    social_str += '\n          <a href="https://medium.com/@zugafitness" aria-label="Medium" class="social-icon"><i class="fab fa-medium"></i></a>'
                    social_str += '\n          <a href="https://www.pinterest.com/zugafitness/" aria-label="Pinterest" class="social-icon"><i class="fab fa-pinterest"></i></a>'
                    social_str += '\n          <a href="https://www.youtube.com/@zugafitness" aria-label="YouTube" class="social-icon"><i class="fab fa-youtube"></i></a>\n'

                    lines.insert(closing_idx, social_str)
                    modified = True

        # Rejoin if modified
        if modified:
            html = "".join(lines)
            soup = BeautifulSoup(html, "html.parser")
            lines = html.splitlines(keepends=True)
            footer = soup.find("footer")

        # 4. Footer Trust Block (Disclaimer)
        if "zuga:footer-trust-v1" not in html and footer:
            # find </footer>
            for i in range(len(lines) - 1, -1, -1):
                if "</footer>" in lines[i].lower():
                    disclaimer_html = '  <!-- zuga:footer-trust-v1 --><p class="footer-disclaimer text-sm text-gray-500 mt-4"><strong>Medical Disclaimer:</strong> The content provided in this article is for informational purposes only and is not intended as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition before starting any new exercise program.</p>\n'
                    lines.insert(i, disclaimer_html)
                    modified = True
                    break

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("".join(lines))
        return True
    return False

if __name__ == "__main__":
    count = 0
    for root, dirs, files in os.walk("."):
        if "node_modules" in root or ".git" in root or "live_html" in root or "assets/docs" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                if process_file(path):
                    count += 1
    print(f"Updated {count} files.")
