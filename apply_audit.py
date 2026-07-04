import os
import re

def process_html_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add lang="en" to <html> if not present or empty
    content = re.sub(r'<html(?![^>]*lang=)([^>]*)>', r'<html lang="en"\1>', content, flags=re.IGNORECASE)
    content = re.sub(r'<html([^>]*)lang=""([^>]*)>', r'<html\1lang="en"\2>', content, flags=re.IGNORECASE)

    # 2. Images: loading="lazy", decoding="async", fetchpriority="high", alt
    img_pattern = r'<img\s+[^>]*>'
    imgs = list(re.finditer(img_pattern, content, re.IGNORECASE))

    for i, match in enumerate(imgs):
        img_tag = match.group(0)

        # Determine if image is above the fold (logo, brand, or first image)
        is_above_fold = False
        img_tag_lower = img_tag.lower()
        if i == 0 or 'logo' in img_tag_lower or 'brand' in img_tag_lower or 'hero' in img_tag_lower:
            is_above_fold = True

        new_img_tag = img_tag

        if not is_above_fold:
            if 'loading=' not in new_img_tag:
                new_img_tag = new_img_tag.replace('<img ', '<img loading="lazy" ')
            if 'decoding=' not in new_img_tag:
                new_img_tag = new_img_tag.replace('<img ', '<img decoding="async" ')
        else:
            if 'fetchpriority=' not in new_img_tag:
                new_img_tag = new_img_tag.replace('<img ', '<img fetchpriority="high" ')

        # Ensure alt attribute exists
        if 'alt=' not in new_img_tag:
            new_img_tag = new_img_tag.replace('<img ', '<img alt="Zuga Fitness Image" ')

        content = content.replace(img_tag, new_img_tag)

    # 3. Target blank links need rel="noopener noreferrer"
    content = re.sub(r'<a([^>]*?)target="_blank"([^>]*?)(?<!rel="noopener noreferrer")>', r'<a\1target="_blank" rel="noopener noreferrer"\2>', content, flags=re.IGNORECASE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    for root, dirs, files in os.walk('.'):
        if 'assets' in root or 'verification' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    process_html_file(filepath)
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == '__main__':
    main()
