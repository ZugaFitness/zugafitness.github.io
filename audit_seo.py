import os
from bs4 import BeautifulSoup

def audit_seo():
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    print(f"Found {len(html_files)} HTML files.")

    report = []
    titles = {}

    robots_exists = os.path.exists('robots.txt')
    sitemap_exists = os.path.exists('sitemap.xml')

    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')

                file_report = {'file': filepath, 'issues': []}

                # 1. Title tags
                title_tag = soup.find('title')
                if not title_tag or not title_tag.text.strip():
                    file_report['issues'].append('Missing <title> tag')
                else:
                    title_text = title_tag.text.strip()
                    if title_text in titles:
                        titles[title_text].append(filepath)
                    else:
                        titles[title_text] = [filepath]

                # 2. Meta description
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                if not meta_desc or not meta_desc.get('content', '').strip():
                    file_report['issues'].append('Missing <meta name="description">')

                # 3. H1 tags
                h1_tags = soup.find_all('h1')
                if len(h1_tags) == 0:
                    file_report['issues'].append('No H1 tag')
                elif len(h1_tags) > 1:
                    file_report['issues'].append(f'Multiple H1 tags ({len(h1_tags)})')

                # 4. Image alt attributes
                images = soup.find_all('img')
                missing_alt = [img for img in images if not img.has_attr('alt') or not img['alt'].strip()]
                if missing_alt:
                    file_report['issues'].append(f'{len(missing_alt)} images missing alt attribute')

                # 5. Canonical tags
                canonical = soup.find('link', attrs={'rel': 'canonical'})
                if not canonical:
                    file_report['issues'].append('Missing canonical tag')

                # 8. Render-blocking scripts in <head>
                head = soup.find('head')
                if head:
                    scripts_in_head = head.find_all('script', src=True)
                    blocking_scripts = [s for s in scripts_in_head if not s.has_attr('async') and not s.has_attr('defer')]
                    if blocking_scripts:
                        file_report['issues'].append(f'{len(blocking_scripts)} render-blocking scripts in <head>')

                if file_report['issues']:
                    report.append(file_report)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

    duplicate_titles = {title: files for title, files in titles.items() if len(files) > 1}

    print("\nSEO AUDIT REPORT")
    print("================")
    print(f"Robots.txt exists: {robots_exists}")
    print(f"Sitemap.xml exists: {sitemap_exists}")
    print("\nFile-by-file Issues:")
    for item in report:
        print(f"\nFile: {item['file']}")
        for issue in item['issues']:
            print(f"  - {issue}")

    if duplicate_titles:
        print("\nDuplicate Titles Found:")
        for title, files in duplicate_titles.items():
            print(f"  Title: \"{title}\"")
            for f in files:
                print(f"    - {f}")

if __name__ == "__main__":
    audit_seo()
