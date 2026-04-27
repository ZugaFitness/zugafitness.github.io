import os
from bs4 import BeautifulSoup
from collections import defaultdict

def audit_seo():
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    report = defaultdict(list)
    titles = defaultdict(list)

    # Global checks
    robots_exists = os.path.exists('robots.txt')
    sitemap_exists = os.path.exists('sitemap.xml')

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')

            # 1. Title tags
            title_tag = soup.find('title')
            if not title_tag or not title_tag.text.strip():
                report[filepath].append("Missing <title> tag")
            else:
                title_text = title_tag.text.strip()
                titles[title_text].append(filepath)

            # 2. Meta description
            desc = soup.find('meta', attrs={'name': 'description'})
            if not desc or not desc.get('content', '').strip():
                report[filepath].append("Missing <meta name=\"description\"> tag")

            # 3. H1 tags
            h1s = soup.find_all('h1')
            if len(h1s) == 0:
                report[filepath].append("Missing H1 tag")
            elif len(h1s) > 1:
                report[filepath].append(f"Incorrect H1 tags: Found {len(h1s)}")

            # 4. Image alt attributes
            imgs = soup.find_all('img')
            missing_alt = []
            for i, img in enumerate(imgs):
                if not img.has_attr('alt'):
                    missing_alt.append(f"Image {i+1} (no alt attribute)")
                elif not img['alt'].strip():
                    # Check if it's explicitly alt="" which is sometimes okay for decorative,
                    # but the prompt asks for images missing alt="" (meaning missing the attribute or value).
                    # Usually "missing alt" means the attribute is not there.
                    # "alt=""" is an empty alt. Let's report both as potential issues if they aren't decorative.
                    missing_alt.append(f"Image {i+1} (empty alt value)")

            if missing_alt:
                report[filepath].append(f"Missing alt attributes: {len(missing_alt)} images")

            # 5. Canonical tags
            canonical = soup.find('link', rel='canonical')
            if not canonical or not canonical.get('href', '').strip():
                report[filepath].append("Missing canonical tag")

            # 8. Render-blocking scripts in <head>
            head = soup.find('head')
            if head:
                scripts_in_head = [s for s in head.find_all('script') if s.get('src') and not (s.has_attr('async') or s.has_attr('defer'))]
                if scripts_in_head:
                    report[filepath].append(f"Render-blocking scripts in <head>: {len(scripts_in_head)}")

    # Format the report
    print("# SEO Audit Report\n")
    print(f"**Robots.txt:** {'✅ Found' if robots_exists else '❌ Missing'}")
    print(f"**Sitemap.xml:** {'✅ Found' if sitemap_exists else '❌ Missing'}\n")

    # Duplicate titles
    duplicate_titles = {t: p for t, p in titles.items() if len(p) > 1}
    if duplicate_titles:
        print("## Duplicate Titles Found")
        for title, paths in duplicate_titles.items():
            print(f"- **Title:** \"{title}\"")
            for p in paths:
                print(f"  - `{p}`")
        print()

    print("## File-by-File Issues")
    if not report:
        print("No major on-page SEO issues found in the scanned files.")
    else:
        for filepath in sorted(html_files):
            issues = report.get(filepath)
            if issues:
                print(f"### `{filepath}`")
                for issue in issues:
                    print(f"- {issue}")
                print()
            else:
                # Still list the file but say it's clean if we want a full report
                # print(f"### `{filepath}`\n- ✅ No issues found\n")
                pass

if __name__ == "__main__":
    audit_seo()
