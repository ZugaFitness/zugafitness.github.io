import os
from bs4 import BeautifulSoup
from collections import defaultdict

def audit():
    html_files = []
    for root, dirs, files in os.walk('.'):
        # Skip assets and .git
        if 'assets' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    html_files.sort()

    titles = defaultdict(list)
    file_reports = {}

    for path in html_files:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            issues = []

            # 1. Title
            title_tag = soup.find('title')
            if not title_tag or not title_tag.text.strip():
                issues.append("Missing <title> tag")
            else:
                titles[title_tag.text.strip()].append(path)

            # 2. Meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if not meta_desc or not meta_desc.get('content', '').strip():
                issues.append("Missing <meta name=\"description\"> tag")

            # 3. H1 tags
            h1s = soup.find_all('h1')
            if len(h1s) == 0:
                issues.append("Missing H1 tag")
            elif len(h1s) > 1:
                issues.append(f"Incorrect H1 tags: Found {len(h1s)}")

            # 4. Image alt attributes
            imgs = soup.find_all('img')
            missing_alt = [img for img in imgs if not img.has_attr('alt')]
            if missing_alt:
                issues.append(f"Images missing alt attribute: {len(missing_alt)} images")

            # 5. Canonical tags
            canonical = soup.find('link', rel='canonical')
            if not canonical or not canonical.get('href', '').strip():
                issues.append("Missing canonical tag")

            # 8. Render-blocking scripts in <head>
            head = soup.find('head')
            if head:
                rb_scripts = [s.get('src') for s in head.find_all('script') if s.get('src') and not (s.has_attr('async') or s.has_attr('defer'))]
                if rb_scripts:
                    issues.append(f"Render-blocking scripts in <head>: {len(rb_scripts)} found")

            file_reports[path] = issues

    # Final Report Construction
    print("# SEO Audit Report\n")

    print("## Global Assets")
    print(f"- **robots.txt:** {'✅ Exists' if os.path.exists('robots.txt') else '❌ Missing'}")
    print(f"- **sitemap.xml:** {'✅ Exists' if os.path.exists('sitemap.xml') else '❌ Missing'}")
    print()

    # Duplicate titles
    duplicate_titles = {t: p for t, p in titles.items() if len(p) > 1}
    if duplicate_titles:
        print("## Duplicate Titles")
        for title, paths in duplicate_titles.items():
            print(f"- Title: \"{title}\"")
            for p in paths:
                print(f"  - `{p}`")
        print()
    else:
        print("## Duplicate Titles: None found\n")

    print("## File-by-File Issues")
    has_any_issue = False
    for path in html_files:
        issues = file_reports[path]
        if issues:
            has_any_issue = True
            print(f"### `{path}`")
            for issue in issues:
                print(f"- {issue}")
            print()

    if not has_any_issue:
        print("No issues found in any HTML files!")

if __name__ == "__main__":
    audit()
