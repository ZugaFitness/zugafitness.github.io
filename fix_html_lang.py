import os
import re

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return

    original = content
    html_match = re.search(r'<html([^>]*)>', content, flags=re.IGNORECASE)
    if html_match:
        html_tag_attrs = html_match.group(1)
        if 'lang=' not in html_tag_attrs.lower():
            content = content[:html_match.start()] + f'<html{html_tag_attrs} lang="en">' + content[html_match.end():]
        else:
            new_attrs = re.sub(r'lang\s*=\s*(?:\"[^\"]*\"|\'[^\']*\')', 'lang="en"', html_tag_attrs, flags=re.IGNORECASE)
            content = content[:html_match.start()] + f'<html{new_attrs}>' + content[html_match.end():]

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed lang in {filepath}")

def main():
    for root, _, files in os.walk('.'):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                fix_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
