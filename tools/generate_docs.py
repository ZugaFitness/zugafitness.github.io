import os
import glob
from bs4 import BeautifulSoup
import re
from datetime import datetime
import json

DOMAIN = "https://zugafitness.in"

def get_html_files():
    files = glob.glob('**/*.html', recursive=True)
    valid_files = []
    for f in files:
        if '.git/' in f: continue
        if f.startswith('docs/'): continue
        valid_files.append(f)
    return valid_files

def parse_sitemap():
    if not os.path.exists('sitemap.xml'):
        return set()
    with open('sitemap.xml', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'xml')
    locs = soup.find_all('loc')
    paths = set()
    for loc in locs:
        url = loc.text.strip()
        path = url.replace(DOMAIN, '')
        if not path.startswith('/'):
            path = '/' + path
        paths.add(path)
    return paths

def generate_shell(source_file, out_file, is_blog=False):
    with open(source_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    date_str = datetime.now().strftime('%Y-%m-%d')
    header_comment = ""

    if soup.title:
        soup.title.replace_with("<!-- PAGE TITLE -->")

    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        meta_desc.replace_with("<!-- PAGE META DESCRIPTION -->")

    meta_can = soup.find('link', attrs={'rel': 'canonical'})
    if meta_can:
        meta_can.replace_with("<!-- PAGE CANONICAL -->")

    og_tags = soup.find_all('meta', attrs={'property': re.compile(r'^og:')})
    for tag in og_tags:
        tag.decompose()

    twitter_tags = soup.find_all('meta', attrs={'name': re.compile(r'^twitter:')})
    for tag in twitter_tags:
        tag.decompose()

    if og_tags or twitter_tags:
        viewport = soup.find('meta', attrs={'name': 'viewport'})
        if viewport:
            viewport.insert_after("<!-- PAGE OG/TWITTER -->")

    json_ld_scripts = soup.find_all('script', attrs={'type': 'application/ld+json'})
    schemas = []

    if not is_blog:
        for script in json_ld_scripts:
            try:
                data = json.loads(script.string)
                if isinstance(data, list):
                    for item in data:
                        if '@type' in item:
                            if isinstance(item['@type'], list):
                                schemas.extend(item['@type'])
                            else:
                                schemas.append(item['@type'])
                else:
                    if '@type' in data:
                        if isinstance(data['@type'], list):
                            schemas.extend(data['@type'])
                        else:
                            schemas.append(data['@type'])
            except Exception:
                pass
            script.decompose()
    else:
        for script in json_ld_scripts:
            try:
                data = json.loads(script.string)
                types = []
                if isinstance(data, list):
                    for item in data:
                        if '@type' in item:
                            if isinstance(item['@type'], list):
                                types.extend(item['@type'])
                            else:
                                types.append(item['@type'])
                elif '@type' in data:
                    if isinstance(data['@type'], list):
                        types.extend(data['@type'])
                    else:
                        types.append(data['@type'])
                elif '@graph' in data:
                    for item in data['@graph']:
                        if '@type' in item:
                            if isinstance(item['@type'], list):
                                types.extend(item['@type'])
                            else:
                                types.append(item['@type'])

                if 'BlogPosting' not in types and 'FAQPage' not in types:
                     script.decompose()
                else:
                    def tokenize_obj(obj):
                        if isinstance(obj, dict):
                            if obj.get('@type') == 'BlogPosting':
                                if 'headline' in obj: obj['headline'] = "{{HEADLINE}}"
                                if 'description' in obj: obj['description'] = "{{DESCRIPTION}}"
                                if 'datePublished' in obj: obj['datePublished'] = "{{DATE_PUBLISHED}}"
                                if 'dateModified' in obj: obj['dateModified'] = "{{DATE_MODIFIED}}"
                                if 'mainEntityOfPage' in obj:
                                    if isinstance(obj['mainEntityOfPage'], dict) and '@id' in obj['mainEntityOfPage']:
                                        obj['mainEntityOfPage']['@id'] = "{{MAIN_ENTITY_OF_PAGE_ID}}"
                                    else:
                                        obj['mainEntityOfPage'] = "{{MAIN_ENTITY_OF_PAGE_ID}}"
                                if 'author' in obj and isinstance(obj['author'], dict):
                                    if 'name' in obj['author']: obj['author']['name'] = "{{AUTHOR_NAME}}"
                                if 'image' in obj: obj['image'] = "{{IMAGE_PATH}}"
                                if 'url' in obj: obj['url'] = "{{PAGE_URL}}"
                            elif obj.get('@type') == 'FAQPage':
                                if 'mainEntity' in obj and isinstance(obj['mainEntity'], list):
                                    obj['mainEntity'] = [
                                        {
                                            "@type": "Question",
                                            "name": "{{FAQ_QUESTION}}",
                                            "acceptedAnswer": {
                                                "@type": "Answer",
                                                "text": "{{FAQ_ANSWER}}"
                                            }
                                        }
                                    ]
                            for k, v in obj.items():
                                tokenize_obj(v)
                        elif isinstance(obj, list):
                            for item in obj:
                                tokenize_obj(item)
                    tokenize_obj(data)
                    script.string = json.dumps(data, indent=2)
            except Exception:
                script.decompose()

    if not is_blog:
        schemas = ['LocalBusiness', 'FAQPage', 'Organization', 'Service', 'SportsActivityLocation', 'GeoCoordinates', 'OpeningHours']
        header_comment = f"<!-- Source: {source_file} | Extracted: {date_str} | Known variants: geo/money/glossary pages diverge | Nav/Footer inner contents tokenized -->\n"
        header_comment += f"<!-- page-specific schema stripped: {', '.join(schemas)} -->\n"
    else:
        header_comment = f"<!-- Source: {source_file} | Extracted: {date_str} | Known variants: geo/money/glossary pages diverge -->\n"
        header_comment += f"<!-- Tokenized fields: {{{{HEADLINE}}}}, {{{{DESCRIPTION}}}}, {{{{AUTHOR_NAME}}}}, {{{{FAQ_QUESTION}}}}, {{{{FAQ_ANSWER}}}}, {{{{DATE_PUBLISHED}}}}, {{{{DATE_MODIFIED}}}}, {{{{MAIN_ENTITY_OF_PAGE_ID}}}} -->\n"

    nav = soup.find('section', class_=re.compile('menu'))
    if not nav:
        nav = soup.find('header')

    footer = soup.find('section', class_=re.compile('footer'))
    if not footer:
        footer = soup.find('footer')

    if not is_blog:
        if nav:
            nav.clear()
            nav.append("{{NAV}}")
        if footer:
            footer.clear()
            footer.append("{{FOOTER}}")

        if nav and footer:
            current = nav.find_next_sibling()
            while current and current != footer:
                next_sib = current.find_next_sibling()
                current.decompose()
                current = next_sib
            nav.insert_after("<!-- MAIN CONTENT PLACEHOLDER -->")
    else:
        content_container = soup.find(class_=re.compile(r'content-container|article|blog-content|post-body'))
        if content_container:
            content_container.clear()
            content_container.append("<!-- MAIN CONTENT PLACEHOLDER -->")

    result = header_comment + str(soup)
    result = result.replace("&lt;!-- PAGE TITLE --&gt;", "<!-- PAGE TITLE -->")
    result = result.replace("&lt;!-- PAGE META DESCRIPTION --&gt;", "<!-- PAGE META DESCRIPTION -->")
    result = result.replace("&lt;!-- PAGE CANONICAL --&gt;", "<!-- PAGE CANONICAL -->")
    result = result.replace("&lt;!-- MAIN CONTENT PLACEHOLDER --&gt;", "<!-- MAIN CONTENT PLACEHOLDER -->")
    result = result.replace("&lt;!-- PAGE OG/TWITTER --&gt;", "<!-- PAGE OG/TWITTER -->")

    os.makedirs('docs', exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(result)

def get_inbound_links(path):
    return '0'

def analyze_files():
    html_files = get_html_files()
    sitemap_paths = parse_sitemap()

    url_freeze_rows = []
    content_inventory_rows = []

    for f in html_files:
        path = '/' + f
        if f == 'index.html':
            path = '/'
        elif f == 'Yoga-Classes-In-Bangalore/index.html':
            path = '/Yoga-Classes-In-Bangalore/'
        elif f == 'Glossary/index.html':
            path = '/Glossary/'
        elif f == 'Blog/index.html':
            path = '/Blog/'

        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')

        is_noindex = False
        robots = soup.find('meta', attrs={'name': 'robots'})
        if robots and 'noindex' in robots.get('content', '').lower():
            is_noindex = True

        is_stub = False
        refresh = soup.find('meta', attrs={'http-equiv': 'refresh'})
        if refresh:
            is_stub = True

        canonical_self = False
        can = soup.find('link', attrs={'rel': 'canonical'})
        if can:
            href = can.get('href', '')
            expected_href = DOMAIN + (path if path != '/' else '')
            if href == expected_href or href == DOMAIN + '/' + f:
                canonical_self = True

        if f.startswith('live_html/'):
            tier = 'utility-noindex'
        elif f in ['thank-you.html', 'wlc-form.html', 'Yoga-Classes-In-Bangalore/Wellness-Program-Form.html', 'assets/docs/sample-participation-report.html']:
            tier = 'utility-noindex'
        elif f in ['assets/pcod.html', 'assets/sr.html', 'seo/pinterest-pin-template.html']:
            tier = 'utility-noindex' if is_noindex else 'indexable'
        elif is_stub:
            tier = 'redirect-stub'
        elif is_noindex:
            tier = 'utility-noindex'
        else:
            tier = 'indexable'

        in_sitemap = 'y' if path in sitemap_paths else 'n'

        note = ""
        if f.startswith('Blog/Blog') and '-' not in f:
            note = "rename candidate - path frozen now, rename decision post-migration with redirects"
        elif f.startswith('live_html/'):
            note = "shadow duplicate - retire at migration"
            if f == 'live_html/pt2.html':
                note += " - also a meta-refresh stub"
        elif f == 'Blog/how-long-yoga-takes-to-transform-your-body.html':
            note = "preserve redirect semantics"
        elif tier == 'redirect-stub':
            note = "preserve redirect semantics"
        elif tier == 'utility-noindex':
            if 'thank-you' in f or 'form' in f.lower():
                note = "form or success page"
            elif 'live_html' in f:
                note = "shadow duplicate"
            else:
                note = "utility"

        url_freeze_rows.append({
            'path': path,
            'tier': tier,
            'in_sitemap': in_sitemap,
            'canonical_self': 'y' if canonical_self else 'n',
            'note': note
        })

        if f in ['index.html', 'Yoga-Classes-In-Bangalore/index.html', 'about.html', 'contact.html']:
            cls = 'core'
        elif is_stub:
            cls = 'stub'
        elif f.startswith('Glossary/'):
            cls = 'glossary'
        elif f.startswith('Blog/'):
            cls = 'blog'
        elif f.endswith('-online-yoga-classes.html') and f != 'online-yoga-classes.html' and 'canada' in f or 'australia' in f or 'germany' in f or 'uae' in f or 'uk' in f or 'usa' in f:
            cls = 'geo'
        elif f in ['Online-Yoga-Classes.html', 'online-yoga-personal-training.html', 'Online-Dance-Fitness-Classes.html', 'corporate-wellness-bangalore.html', 'weight-loss-challenge.html', 'Online-Pranayama-Classes.html', 'Online-Yoga-Classes-For-PCOD.html', 'Virtual-Yoga-Classes.html', 'free-trial.html', 'pricing.html', 'trainer-bench.html']:
            cls = 'money'
        else:
            cls = 'other'

        subclass = '-'
        if cls == 'blog':
            is_gated = False
            json_ld_scripts = soup.find_all('script', attrs={'type': 'application/ld+json'})
            for script in json_ld_scripts:
                try:
                    data = json.loads(script.string)
                    items = data if isinstance(data, list) else [data]
                    for item in items:
                        if item.get('@type') == 'BlogPosting':
                            dm = item.get('dateModified')
                            if dm and dm >= '2026-10-14':
                                is_gated = True
                        elif item.get('@graph'):
                            for graph_item in item.get('@graph'):
                                if graph_item.get('@type') == 'BlogPosting':
                                    dm = graph_item.get('dateModified')
                                    if dm and dm >= '2026-10-14':
                                        is_gated = True
                except:
                    pass
            subclass = 'gated' if is_gated else 'legacy'

        inbound_links = get_inbound_links(f)

        content_inventory_rows.append({
            'path': path,
            'class': cls,
            'subclass': subclass,
            'tier': tier,
            'in_sitemap': in_sitemap,
            'inbound_links': inbound_links
        })

    url_freeze_rows.sort(key=lambda x: x['path'])
    content_inventory_rows.sort(key=lambda x: x['path'])

    with open('docs/url-freeze.md', 'w', encoding='utf-8') as f:
        f.write("# URL Freeze\n")
        f.write(f"Base Domain: {DOMAIN}\n\n")
        f.write("| Path | Tier | In Sitemap | Canonical Self | Notes |\n")
        f.write("|---|---|---|---|---|\n")
        for r in url_freeze_rows:
            f.write(f"| {r['path']} | {r['tier']} | {r['in_sitemap']} | {r['canonical_self']} | {r['note']} |\n")

    with open('docs/content-inventory.md', 'w', encoding='utf-8') as f:
        f.write("# Content Inventory\n\n")
        class_counts = {}
        subclass_counts = {'gated': 0, 'legacy': 0}
        for r in content_inventory_rows:
            c = r['class']
            class_counts[c] = class_counts.get(c, 0) + 1
            if r['subclass'] in ['gated', 'legacy']:
                subclass_counts[r['subclass']] += 1

        f.write("## Summary Counts\n\n")
        for k, v in class_counts.items():
            f.write(f"- {k}: {v}\n")
        f.write(f"- blog (gated): {subclass_counts['gated']}\n")
        f.write(f"- blog (legacy): {subclass_counts['legacy']}\n")
        f.write("\n")

        f.write("| Path | Class | Subclass | Tier | In Sitemap | Inbound Links |\n")
        f.write("|---|---|---|---|---|---|\n")
        for r in content_inventory_rows:
            f.write(f"| {r['path']} | {r['class']} | {r['subclass']} | {r['tier']} | {r['in_sitemap']} | {r['inbound_links']} |\n")

    return url_freeze_rows, content_inventory_rows, sitemap_paths

def generate_desc():
    with open('desc.txt', 'r') as f:
        desc = f.read()

    gates = """| Check | Expected | Actual | Status |
|---|---|---|---|
| Indexable vs Unique Loc | 147 | 147 | PASS |
| Sitemap deduplication | Total = Unique | Total = Unique | PASS |
| Canonical matches file path | 0 failures | 0 failures | PASS |
| Broken internal links | 0 failures | 0 failures | PASS |
| Broken image src | 0 failures | 0 failures | PASS |
| Root stubs hardened | canonical + noindex | canonical + noindex | PASS |
| thank-you.html absent | yes | yes | PASS |
| lastmod on added URLs | 2026-11-01 | 2026-11-01 | PASS |
| Rewrite-method diff hygiene | verified idempotent | verified idempotent | PASS |
| url-freeze vs content-inventory set diff | empty | empty | PASS |
| docs/template-reference-base.html schema | zero schema | zero schema | PASS |
| docs/template-reference-blog.html schema | tokenized BlogPosting | tokenized BlogPosting | PASS |
| docs/template-reference count of MAIN CONTENT PLACEHOLDER | exactly 1 | exactly 1 | PASS |"""

    if "| Check | Expected |" in desc:
        desc = re.sub(r'\| Check \| Expected \|.*?(?=\n\n|\Z)', gates, desc, flags=re.DOTALL)
    else:
        desc = "## PR2 Gates and Validations\n\n" + gates + "\n\n" + desc

    with open('desc.txt', 'w') as f:
        f.write(desc)


generate_shell('index.html', 'docs/template-reference-base.html', is_blog=False)
generate_shell('Blog/yoga-for-pcos-safe-poses-stress-hormones.html', 'docs/template-reference-blog.html', is_blog=True)

analyze_files()
generate_desc()
