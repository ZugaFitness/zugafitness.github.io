import os
from bs4 import BeautifulSoup
from collections import defaultdict

def audit_website():
    html_files = []
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'assets' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    html_files.sort()

    titles = defaultdict(list)
    report = []

    robots_txt = os.path.exists('robots.txt')
    sitemap_xml = os.path.exists('sitemap.xml')

    for path in html_files:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            file_issues = []

            # 1. Title
            title_tag = soup.find('title')
            if not title_tag or not title_tag.text.strip():
                file_issues.append("Missing <title> tag")
            else:
                titles[title_tag.text.strip()].append(path)

            # 2. Meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if not meta_desc or not meta_desc.get('content', '').strip():
                file_issues.append("Missing <meta name=\"description\"> tag")

            # 3. H1 tags
            h1s = soup.find_all('h1')
            if len(h1s) == 0:
                file_issues.append("Missing H1 tag")
            elif len(h1s) > 1:
                file_issues.append(f"Incorrect H1 tags: {len(h1s)} found")

            # 4. Image alt
            imgs = soup.find_all('img')
            missing_alt = [img for img in imgs if not img.has_attr('alt')]
            if missing_alt:
                file_issues.append(f"Images missing alt attribute: {len(missing_alt)} images")

            # 5. Canonical
            canonical = soup.find('link', rel='canonical')
            if not canonical:
                file_issues.append("Missing canonical tag")
            elif not canonical.get('href', '').strip():
                file_issues.append("Canonical tag has empty href")

            # 8. Render-blocking scripts in head
            head = soup.find('head')
            if head:
                scripts = [s for s in head.find_all('script') if s.get('src') and not (s.has_attr('async') or s.has_attr('defer'))]
                if scripts:
                    file_issues.append(f"Render-blocking scripts in <head>: {len(scripts)}")

            report.append((path, file_issues))

    # Check for duplicate titles
    duplicate_titles = {t: p for t, p in titles.items() if len(p) > 1}

    print("SEO AUDIT REPORT")
    print("================")
    print(f"robots.txt: {'Exists' if robots_txt else 'MISSING'}")
    print(f"sitemap.xml: {'Exists' if sitemap_xml else 'MISSING'}")
    print()

    if duplicate_titles:
        print("Duplicate Titles Found:")
        for t, p in duplicate_titles.items():
            print(f"- \"{t}\"")
            for path in p:
                print(f"  - {path}")
        print()
    else:
        print("Duplicate Titles: None found")
        print()

    for path, issues in report:
        print(f"File: {path}")
        if not issues:
            print("  - No issues found")
        else:
            for issue in issues:
                print(f"  - {issue}")
        print()

if __name__ == "__main__":
    audit_website()
