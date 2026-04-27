import os
from bs4 import BeautifulSoup

def audit():
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    html_files.sort()

    titles = {}
    report = []

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            # Title
            title_tag = soup.find('title')
            title = title_tag.text.strip() if title_tag else None
            if title:
                if title in titles:
                    titles[title].append(filepath)
                else:
                    titles[title] = [filepath]

            # Meta Description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            has_desc = bool(meta_desc and meta_desc.get('content', '').strip())

            # H1
            h1_tags = soup.find_all('h1')
            h1_count = len(h1_tags)

            # Images Alt
            images = soup.find_all('img')
            missing_alt_count = 0
            for img in images:
                if not img.has_attr('alt'):
                    missing_alt_count += 1

            # Canonical
            canonical = soup.find('link', attrs={'rel': 'canonical'})
            has_canonical = bool(canonical and canonical.get('href', '').strip())

            # Scripts in Head
            head = soup.find('head')
            blocking_scripts = []
            if head:
                scripts = head.find_all('script', src=True)
                for s in scripts:
                    if not s.has_attr('async') and not s.has_attr('defer'):
                        blocking_scripts.append(s['src'])

            report.append({
                'file': filepath,
                'title': title,
                'has_desc': has_desc,
                'h1_count': h1_count,
                'missing_alt': missing_alt_count,
                'has_canonical': has_canonical,
                'blocking_scripts': blocking_scripts
            })

    # Duplicate titles
    duplicates = {t: paths for t, paths in titles.items() if len(paths) > 1}

    print("# SEO AUDIT REPORT")
    print("\n## 1. Summary")
    print(f"- Total HTML files: {len(html_files)}")
    print(f"- robots.txt exists: {os.path.exists('robots.txt')}")
    print(f"- sitemap.xml exists: {os.path.exists('sitemap.xml')}")

    print("\n## 2. Duplicate Titles")
    if duplicates:
        for t, paths in duplicates.items():
            print(f"- Title: \"{t}\"")
            for p in paths:
                print(f"  - {p}")
    else:
        print("None found.")

    print("\n## 3. Detailed File Report")
    for r in report:
        print(f"\n### File: {r['file']}")

        # Title check
        if not r['title']:
            print("- [ ] MISSING <title> tag")
        else:
            print(f"- [x] Title: {r['title']}")
            if r['title'] in duplicates:
                print("  - DUPLICATE title detected")

        # Description check
        if not r['has_desc']:
            print("- [ ] MISSING <meta name=\"description\">")
        else:
            print("- [x] Meta description exists")

        # H1 check
        if r['h1_count'] == 0:
            print("- [ ] MISSING H1 tag")
        elif r['h1_count'] > 1:
            print(f"- [ ] MULTIPLE H1 tags ({r['h1_count']})")
        else:
            print("- [x] Single H1 tag exists")

        # Alt check
        if r['missing_alt'] > 0:
            print(f"- [ ] {r['missing_alt']} images MISSING alt attribute")
        else:
            print("- [x] All images have alt attributes (if any)")

        # Canonical check
        if not r['has_canonical']:
            print("- [ ] MISSING canonical tag")
        else:
            print("- [x] Canonical tag exists")

        # Scripts check
        if r['blocking_scripts']:
            print(f"- [ ] {len(r['blocking_scripts'])} render-blocking scripts in <head>:")
            for s in r['blocking_scripts']:
                print(f"  - {s}")
        else:
            print("- [x] No render-blocking scripts in <head>")

if __name__ == "__main__":
    audit()
