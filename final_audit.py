import os
from bs4 import BeautifulSoup
from collections import defaultdict

def audit():
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html') and 'assets' not in root:
                html_files.append(os.path.join(root, file))

    html_files.sort()

    titles = defaultdict(list)
    results = {}

    for path in html_files:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            # 1. Title
            title_tag = soup.find('title')
            title_val = title_tag.text.strip() if title_tag else None
            if title_val:
                titles[title_val].append(path)

            # 2. Meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            desc_val = meta_desc.get('content', '').strip() if meta_desc else None

            # 3. H1 tags
            h1s = soup.find_all('h1')
            h1_count = len(h1s)

            # 4. Image alt
            imgs = soup.find_all('img')
            missing_alt_count = sum(1 for img in imgs if not img.has_attr('alt'))
            # Some might have alt="" which is technically an attribute but empty.
            # Usually "missing alt" means the attribute itself is missing.
            # Let's check both.
            empty_alt_count = sum(1 for img in imgs if img.has_attr('alt') and not img['alt'].strip())

            # 5. Canonical
            canonical = soup.find('link', rel='canonical')
            canonical_val = canonical.get('href', '').strip() if canonical else None

            # 8. Render-blocking scripts in <head>
            head = soup.find('head')
            rb_scripts = []
            if head:
                rb_scripts = [s.get('src') for s in head.find_all('script') if s.get('src') and not (s.has_attr('async') or s.has_attr('defer'))]

            results[path] = {
                'title': title_val,
                'description': desc_val,
                'h1_count': h1_count,
                'missing_alt': missing_alt_count,
                'empty_alt': empty_alt_count,
                'canonical': canonical_val,
                'rb_scripts': rb_scripts
            }

    # Check for duplicate titles
    duplicates = {t: p for t, p in titles.items() if len(p) > 1}

    print("# SEO Audit Report\n")

    print("## Global Files")
    print(f"- **robots.txt:** {'✅ Exists' if os.path.exists('robots.txt') else '❌ Missing'}")
    print(f"- **sitemap.xml:** {'✅ Exists' if os.path.exists('sitemap.xml') else '❌ Missing'}\n")

    if duplicates:
        print("## Duplicate Titles")
        for t, p in duplicates.items():
            print(f"- \"{t}\" found in:")
            for path in p:
                print(f"  - `{path}`")
        print()
    else:
        print("## Duplicate Titles: None found\n")

    print("## Detailed Page Audit\n")
    for path in html_files:
        res = results[path]
        print(f"### `{path}`")

        # 1. Title
        if not res['title']:
            print("- ❌ **Title:** Missing")
        else:
            print(f"- ✅ **Title:** \"{res['title']}\"")

        # 2. Description
        if not res['description']:
            print("- ❌ **Meta Description:** Missing")
        else:
            print(f"- ✅ **Meta Description:** Present")

        # 3. H1
        if res['h1_count'] == 0:
            print("- ❌ **H1 Tag:** Missing")
        elif res['h1_count'] > 1:
            print(f"- ❌ **H1 Tag:** Incorrect ({res['h1_count']} found)")
        else:
            print("- ✅ **H1 Tag:** 1 found")

        # 4. Alts
        if res['missing_alt'] > 0 or res['empty_alt'] > 0:
            print(f"- ⚠️ **Images:** {res['missing_alt']} missing alt attribute, {res['empty_alt']} empty alt value")
        else:
            print("- ✅ **Images:** All have alt attributes")

        # 5. Canonical
        if not res['canonical']:
            print("- ❌ **Canonical Tag:** Missing")
        else:
            print(f"- ✅ **Canonical Tag:** Present")

        # 8. Render-blocking scripts
        if res['rb_scripts']:
            print(f"- ⚠️ **Render-blocking scripts in <head>:** {len(res['rb_scripts'])} found")
            # for s in res['rb_scripts']:
            #    print(f"  - `{s}`")
        else:
            print("- ✅ **Render-blocking scripts:** None in <head>")
        print()

if __name__ == "__main__":
    audit()
