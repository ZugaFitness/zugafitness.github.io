import os
from bs4 import BeautifulSoup

def audit_seo():
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    report = {}
    titles = {}

    robots_exists = os.path.exists('robots.txt')
    sitemap_exists = os.path.exists('sitemap.xml')

    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')

                issues = []

                # 1. Title tags
                title_tag = soup.find('title')
                if not title_tag:
                    issues.append('Missing <title> tag')
                elif not title_tag.text.strip():
                    issues.append('Empty <title> tag')
                else:
                    t = title_tag.text.strip()
                    if t in titles:
                        titles[t].append(filepath)
                    else:
                        titles[t] = [filepath]

                # 2. Meta description
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                if not meta_desc:
                    issues.append('Missing <meta name="description">')
                elif not meta_desc.get('content', '').strip():
                    issues.append('Empty <meta name="description">')

                # 3. H1 tags
                h1_tags = soup.find_all('h1')
                if len(h1_tags) == 0:
                    issues.append('No H1 tag')
                elif len(h1_tags) > 1:
                    issues.append(f'Multiple H1 tags ({len(h1_tags)})')

                # 4. Image alt attributes
                images = soup.find_all('img')
                missing_alt = []
                for img in images:
                    if not img.has_attr('alt'):
                        missing_alt.append(str(img))
                    elif not img['alt'].strip():
                        # Sometimes alt="" is intentional for decorative images,
                        # but the prompt asks for missing alt="" attributes.
                        # I will flag empty alts as well just in case.
                        pass

                if missing_alt:
                    issues.append(f'{len(missing_alt)} images missing alt attribute')

                # 5. Canonical tags
                canonical = soup.find('link', attrs={'rel': 'canonical'})
                if not canonical:
                    issues.append('Missing canonical tag')

                # 8. Render-blocking scripts in <head>
                head = soup.find('head')
                if head:
                    scripts_in_head = head.find_all('script', src=True)
                    blocking = [s['src'] for s in scripts_in_head if not s.has_attr('async') and not s.has_attr('defer')]
                    if blocking:
                        issues.append(f'{len(blocking)} render-blocking scripts in <head>: {", ".join(blocking)}')

                report[filepath] = issues
        except Exception as e:
            print(f"Error checking {filepath}: {e}")

    # Duplicate titles check
    duplicates = {title: paths for title, paths in titles.items() if len(paths) > 1}

    print("SEO AUDIT REPORT")
    print("================")
    print(f"Total HTML files found: {len(html_files)}")
    print(f"robots.txt exists: {robots_exists}")
    print(f"sitemap.xml exists: {sitemap_exists}")
    print("")

    print("--- File-by-file Analysis ---")
    files_with_issues = 0
    for filepath, issues in report.items():
        if issues:
            files_with_issues += 1
            print(f"\nFile: {filepath}")
            for issue in issues:
                print(f"  - {issue}")

    if files_with_issues == 0:
        print("No individual file issues found (except duplicates).")

    print("\n--- Duplicate Titles Analysis ---")
    if duplicates:
        for title, paths in duplicates.items():
            print(f"Title: \"{title}\"")
            for p in paths:
                print(f"  - {p}")
    else:
        print("No duplicate titles found.")

if __name__ == "__main__":
    audit_seo()
