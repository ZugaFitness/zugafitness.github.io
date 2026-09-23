import os
import re

html_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

preconnect_tags = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://www.googletagmanager.com">
"""

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # If already has fonts preconnect, maybe skip or just add what's missing
    new_content = content
    if "https://fonts.googleapis.com" not in content or "preconnect" not in content:
        # Add after <head>
        new_content = re.sub(r'<head>', f'<head>{preconnect_tags}', new_content, count=1, flags=re.IGNORECASE)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
