import os
from bs4 import BeautifulSoup
from collections import defaultdict

def audit():
    html_files = []
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'assets' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    html_files.sort()

    titles = defaultdict(list)
    file_data = {}

    robots_exists = os.path.exists('robots.txt')
    sitemap_exists = os.path.exists('sitemap.xml')

    for path in html_files:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')

            # Title
            title_tag = soup.find('title')
            title_text = title_tag.get_text().strip() if title_tag else None
            if title_text:
                titles[title_text].append(path)

            # Meta Description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            description = meta_desc.get('content', '').strip() if meta_desc else None

            # H1
            h1s = soup.find_all('h1')
            h1_texts = [h.get_text(strip=True) for h in h1s]

            # Alt attributes
            imgs = soup.find_all('img')
            missing_alt_attr = [img for img in imgs if not img.has_attr('alt')]
            empty_alt_attr = [img for img in imgs if img.has_attr('alt') and not img.get('alt', '').strip()]

            # Canonical
            canonical = soup.find('link', rel='canonical')
            canonical_href = canonical.get('href', '').strip() if canonical else None

            # Render-blocking scripts in head
            head = soup.find('head')
            rb_scripts = []
            if head:
                # Script tags with src but without async or defer
                rb_scripts = [s.get('src') for s in head.find_all('script') if s.get('src') and not (s.has_attr('async') or s.has_attr('defer'))]

            file_data[path] = {
                'title': title_text,
                'description': description,
                'h1s': h1_texts,
                'missing_alt_count': len(missing_alt_attr),
                'empty_alt_count': len(empty_alt_attr),
                'canonical': canonical_href,
                'rb_scripts': rb_scripts
            }

    print("SEO AUDIT REPORT\n")
    print(f"Robots.txt exists: {robots_exists}")
    print(f"Sitemap.xml exists: {sitemap_xml}\n")

    duplicate_titles = {t: p for t, p in titles.items() if len(p) > 1}
    if duplicate_titles:
        print("Duplicate Titles Found:")
        for title, paths in duplicate_titles.items():
            print(f"- \"{title}\"")
            for p in paths:
                print(f"  - {p}")
        print()
    else:
        print("No duplicate titles found.\n")

    for path, data in file_data.items():
        print(f"--- File: {path} ---")

        # 1. Title
        if not data['title']:
            print("  [X] Missing <title> tag")
        else:
            print(f"  [OK] Title: \"{data['title']}\"")

        # 2. Meta Description
        if not data['description']:
            print("  [X] Missing <meta name=\"description\"> tag")
        else:
            print("  [OK] Meta description found")

        # 3. H1 Tags
        if len(data['h1s']) == 0:
            print("  [X] Missing H1 tag")
        elif len(data['h1s']) > 1:
            print(f"  [X] Multiple H1 tags found ({len(data['h1s'])}): {data['h1s']}")
        else:
            print(f"  [OK] Single H1 found: \"{data['h1s'][0]}\"")

        # 4. Image Alt
        if data['missing_alt_count'] > 0:
            print(f"  [X] {data['missing_alt_count']} images missing 'alt' attribute entirely")
        if data['empty_alt_count'] > 0:
            print(f"  [-] {data['empty_alt_count']} images have empty 'alt=\"\"' (decorative or missing content)")
        if data['missing_alt_count'] == 0 and data['empty_alt_count'] == 0:
            print("  [OK] All images have non-empty alt text")

        # 5. Canonical
        if not data['canonical']:
            print("  [X] Missing canonical tag")
        else:
            print(f"  [OK] Canonical tag found: {data['canonical']}")

        # 8. Render-blocking scripts
        if data['rb_scripts']:
            print(f"  [X] {len(data['rb_scripts'])} render-blocking scripts in <head>:")
            for s in data['rb_scripts']:
                print(f"    - {s}")
        else:
            print("  [OK] No render-blocking scripts in <head>")
        print()

if __name__ == "__main__":
    audit()
