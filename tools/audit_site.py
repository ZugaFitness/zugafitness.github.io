import os
import glob
import json
import re
import urllib.parse
from bs4 import BeautifulSoup
from collections import defaultdict
import datetime
import difflib
import subprocess

REPORT_DIR = "seo/audit/site-audit-2026-11"
os.makedirs(REPORT_DIR, exist_ok=True)
REPORT_MD = os.path.join(REPORT_DIR, "report.md")
REPORT_JSON = os.path.join(REPORT_DIR, "report.json")
BASE_DOMAIN = "https://zugafitness.in"

YMYL_TERMS = [re.compile(rf"\b{term}\b", re.IGNORECASE) for term in ["cure", "treat", "heals", "reverses", "balances hormones", "clinically proven", "guaranteed"]]

def is_stub(html_content):
    return '<meta http-equiv="refresh"' in html_content.lower()

def get_schema(soup):
    script = soup.find('script', type='application/ld+json')
    if script and script.string:
        try:
            return json.loads(script.string)
        except:
            pass
    return None

def classify_file(filepath, html_content, soup):
    if is_stub(html_content):
        return "stub"

    parts = filepath.split('/')
    if len(parts) > 1:
        if parts[0] == "Blog":
            schema = get_schema(soup)
            if schema:
                dp = schema.get("datePublished")
                if dp and str(dp)[:10] < "2025-01-01":
                    return "legacy"
            return "blog"
        if parts[0] == "Glossary":
            return "glossary"

    basename = os.path.basename(filepath)
    money_pages = ["Online-Yoga-Classes.html", "Online-Dance-Fitness-Classes.html", "Online-Personal-Training-classes.html", "Online-Pranayama-Classes.html", "corporate-wellness-bangalore.html", "trainer-bench.html", "weight-loss-challenge.html", "Online-Yoga-Classes-For-PCOD.html", "pricing.html", "free-trial.html"]

    if basename in money_pages:
        return "money"

    geo_pattern = re.compile(r"^(usa|uk|canada|uae|germany|australia)-online-yoga-classes\.html$")
    if geo_pattern.match(basename):
        return "geo"

    core_pages = ["index.html", "about.html", "contact.html"]
    if basename in core_pages:
        return "core"

    return "other"

def normalize_url_path(url, filepath=""):
    if url.startswith(BASE_DOMAIN):
        url = url[len(BASE_DOMAIN):]
    if url.startswith("/"):
        url = url[1:]

    if filepath and not url.startswith("http") and not url.startswith("data:"):
        base_url = "http://localhost/" + filepath.replace("\\", "/")
        joined = urllib.parse.urljoin(base_url, url)
        url = joined.replace("http://localhost/", "")

    if not url:
        return "index.html"
    if url.endswith("/"):
        return url + "index.html"
    return url

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def main():
    html_files = glob.glob("**/*.html", recursive=True)
    results = {}

    titles = defaultdict(list)
    descriptions = defaultdict(list)

    all_internal_links = []
    inbound_counts = defaultdict(int)

    bodies = {}

    # Pre-parse and initial sweep
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        soup = BeautifulSoup(content, 'html.parser')

        file_class = classify_file(filepath, content, soup)

        # titles / descriptions mapping
        title_tag = soup.find('title')
        title_text = title_tag.string.strip() if title_tag and title_tag.string else None
        if title_text:
            titles[title_text].append(filepath)

        desc_meta = soup.find('meta', attrs={'name': 'description'})
        desc_text = desc_meta['content'].strip() if desc_meta and desc_meta.has_attr('content') else None
        if desc_text:
            descriptions[desc_text].append(filepath)

        # extract internal links
        for a in soup.find_all('a', href=True):
            href = a['href'].strip()
            if href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('whatsapp:') or href.startswith('javascript:'):
                continue
            if not href.startswith('http') or href.startswith(BASE_DOMAIN):
                normalized = normalize_url_path(href, filepath)
                normalized = normalized.split('#')[0].split('?')[0] # remove fragments and query params
                if normalized.endswith('/'):
                    normalized = normalized[:-1] + '.html'
                if normalized:
                    all_internal_links.append((filepath, normalized))
                    inbound_counts[normalized] += 1

        # body for duplicates
        body_tag = soup.find('body')
        body_text = clean_text(body_tag.get_text()) if body_tag else ""
        bodies[filepath] = body_text

    # Read sitemap
    sitemap_urls = set()
    sitemap_lastmods = {}
    if os.path.exists("sitemap.xml"):
        with open("sitemap.xml", 'r', encoding='utf-8') as f:
            sitemap_soup = BeautifulSoup(f.read(), 'xml')
            for loc in sitemap_soup.find_all('loc'):
                url = loc.string.strip()
                norm = normalize_url_path(url)

                if norm.endswith('/'):
                    norm += 'index.html'
                elif norm == '' or norm == '/':
                    norm = 'index.html'
                sitemap_urls.add(norm)

                lastmod_tag = loc.find_next_sibling('lastmod')
                if lastmod_tag:
                    sitemap_lastmods[norm] = lastmod_tag.string.strip()

    # validate_schema runner
    schema_validations = {}
    try:
        proc = subprocess.run(["python", "tools/validate_schema.py"], capture_output=True, text=True)
        for line in proc.stdout.split('\n'):
            if line.startswith("FAIL:"):
                # format: FAIL: filepath - msg
                parts = line.split(" - ", 1)
                if len(parts) == 2:
                    fp = parts[0].replace("FAIL: ", "").strip()
                    schema_validations[fp] = parts[1].strip()
    except:
        pass

    report = {
        "summary": {},
        "files": {}
    }

    today_str = datetime.date.today().isoformat()

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        soup = BeautifulSoup(content, 'html.parser')

        file_class = classify_file(filepath, content, soup)

        issues = []
        info = {}

        # 1. Inventory
        info["class"] = file_class

        # 2. Title
        title_tag = soup.find('title')
        if not title_tag or not title_tag.string:
            issues.append("Missing <title>")
        else:
            title_text = title_tag.string.strip()
            if not (30 <= len(title_text) <= 60):
                issues.append(f"Title length ({len(title_text)}) outside 30-60 chars")
            if len(titles[title_text]) > 1:
                issues.append("Duplicate title")

        # 3. Meta description
        desc_meta = soup.find('meta', attrs={'name': 'description'})
        if not desc_meta or not desc_meta.has_attr('content'):
            issues.append("Missing meta description")
        else:
            desc_text = desc_meta['content'].strip()
            if not (70 <= len(desc_text) <= 160):
                issues.append(f"Meta description length ({len(desc_text)}) outside 70-160 chars")
            if len(descriptions[desc_text]) > 1:
                issues.append("Duplicate meta description")
            if "Custom Pricing" in desc_text or "contact us for a tailored quote" in desc_text:
                issues.append("Meta description contains flagged pricing language")

        # 4. Canonical
        canonical = soup.find('link', rel='canonical')
        if not canonical or not canonical.has_attr('href'):
            if file_class != "stub":
                issues.append("Missing canonical link")
        else:
            can_url = canonical['href']
            norm_can = normalize_url_path(can_url, filepath)
            norm_file = filepath.replace("\\", "/")
            if norm_can != norm_file and file_class != "stub":
                issues.append(f"Canonical URL ({norm_can}) does not match file path")

        # 5. Robots meta
        robots_meta = soup.find('meta', attrs={'name': 'robots'})
        is_noindex = False
        if robots_meta and robots_meta.has_attr('content') and 'noindex' in robots_meta['content'].lower():
            is_noindex = True

        intentional_noindex = [
            "assets/docs/sample-participation-report.html",
            "thank-you.html",
            "success.html"
        ]
        is_intentional_noindex = (filepath.replace("\\", "/") in intentional_noindex) or (os.path.basename(filepath) in ["thank-you.html", "success.html"]) or (file_class == "stub")

        if is_noindex and not is_intentional_noindex:
            issues.append("Unintentional noindex")

        # 6. H1
        h1s = soup.find_all('h1')
        if len(h1s) != 1:
            issues.append(f"Found {len(h1s)} H1 tags (must be exactly 1)")

        # 7. OG/Twitter
        og_title = soup.find('meta', property='og:title')
        og_desc = soup.find('meta', property='og:description')
        og_image = soup.find('meta', property='og:image')
        twitter_card = soup.find('meta', attrs={'name': 'twitter:card'})

        if not og_title: issues.append("Missing og:title")
        if not og_desc: issues.append("Missing og:description")
        if not twitter_card: issues.append("Missing twitter:card")

        if not og_image or not og_image.has_attr('content'):
            issues.append("Missing og:image")
        else:
            img_src = og_image['content']
            norm_img = normalize_url_path(img_src, filepath)
            if norm_img.startswith("assets/"):
                if not os.path.exists(norm_img):
                    issues.append(f"og:image asset missing: {norm_img}")

        # 8. Images alt & broken
        imgs = soup.find_all('img')
        missing_alts = 0
        for img in imgs:
            if not img.has_attr('alt') or not img['alt'].strip():
                missing_alts += 1
            if img.has_attr('src'):
                src = img['src']
                if not src.startswith("http") and not src.startswith("data:"):
                    norm_src = normalize_url_path(src, filepath)
                    if not os.path.exists(norm_src) and norm_src != "":
                        issues.append(f"Broken image src: {norm_src}")
        if missing_alts > 0:
            issues.append(f"Missing alt attributes on {missing_alts} images")

        # 9. Internal links done globally, process for this file
        info["inbound_links"] = inbound_counts[filepath.replace("\\", "/")]
        if info["inbound_links"] == 0 and file_class not in ["stub"] and not is_noindex and filepath != "index.html":
            issues.append("Orphan page (0 inbound links)")

        # 10. Schema
        schema = get_schema(soup)
        if not schema:
            issues.append("Zero schema found")
        else:
            info["schema_type"] = schema.get("@type", "Unknown")
        if filepath in schema_validations:
            issues.append(f"Schema validation failed: {schema_validations[filepath]}")

        # 11. Sitemap
        norm_fp = filepath.replace("\\", "/")
        if not is_noindex and file_class != "stub":
            if norm_fp not in sitemap_urls:
                issues.append("Indexable page missing from sitemap")
            if norm_fp in sitemap_lastmods:
                lm = sitemap_lastmods[norm_fp]
                if lm > today_str:
                    issues.append(f"Future-dated sitemap lastmod: {lm}")
        if (is_noindex or file_class == "stub") and norm_fp in sitemap_urls:
            issues.append("noindex/stub URL present in sitemap")

        # 12. Author Box
        if file_class == "blog" or file_class == "legacy":
            has_schema_author = False
            if schema and "author" in schema:
                auth = schema["author"]
                if isinstance(auth, dict) and auth.get("name") in ["Mallinath", "Anusha"]:
                    has_schema_author = True
                elif isinstance(auth, list):
                    for a in auth:
                        if isinstance(a, dict) and a.get("name") in ["Mallinath", "Anusha"]:
                            has_schema_author = True

            body_text = soup.get_text()
            has_visual_name = "Mallinath" in body_text or "Anusha" in body_text

            # Check for image visually
            has_author_img = False
            for img in soup.find_all('img', src=True):
                src = img['src']
                if "anusha-7b37cda6.webp" in src or "photo-2025-03-08" in src and "jpeg" in src:
                    has_author_img = True
                    break

            if not has_schema_author or not (has_visual_name and has_author_img):
                issues.append("Author box incomplete/missing (needs schema + visual name + correct image)")

        # 13. Dates
        if (file_class == "blog" or file_class == "legacy") and schema:
            dp = schema.get("datePublished")
            dm = schema.get("dateModified")
            if not dp or not dm:
                issues.append("Missing datePublished or dateModified in schema")
            else:
                if str(dp)[:10] > str(dm)[:10]:
                    issues.append(f"datePublished ({dp}) > dateModified ({dm})")
                if str(dp)[:10] > today_str or str(dm)[:10] > today_str:
                    issues.append("Future dated schema dates")

        # 14. YMYL
        lines = content.split('\n')
        for i, line in enumerate(lines):
            for term in YMYL_TERMS:
                if term.search(line):
                    issues.append(f"YMYL flag on line {i+1}: {term.pattern}")

        # 15. Trust
        footer = soup.find('footer')
        if not footer:
            footer_text = content.lower()
        else:
            footer_text = footer.get_text().lower()

        if not re.search(r'medical\s+disclaimer', content, re.IGNORECASE):
            issues.append("Missing medical disclaimer")

        has_privacy = bool(soup.find('a', href=re.compile(r'privacy', re.I))) or bool(soup.find('a', string=re.compile(r'privacy', re.I)))
        has_terms = bool(soup.find('a', href=re.compile(r'terms', re.I))) or bool(soup.find('a', string=re.compile(r'terms', re.I)))
        has_refund = bool(soup.find('a', href=re.compile(r'refund', re.I))) or bool(soup.find('a', string=re.compile(r'refund', re.I)))

        if not (has_privacy and has_terms and has_refund):
            issues.append("Missing Privacy/Terms/Refund links")

        if "[ADD]" in content or "[GSTIN]" in content:
            issues.append("Unfilled placeholders found ([ADD], [GSTIN])")

        # 16. Consistency
        if re.search(r'zugafitness24@gmail\.com', content) or re.search(r'[a-zA-Z0-9._%+-]+@gmail\.com', content, re.I):
            issues.append("Unapproved @gmail.com email found")

        for match in re.finditer(r'(?<!\d)(?:\+91[\s-]?|91[\s-]?)?([6-9]\d[\s-]?\d[\s-]?\d[\s-]?\d[\s-]?\d[\s-]?\d[\s-]?\d[\s-]?\d[\s-]?\d)(?!\d)', content):
            digits = re.sub(r'\D', '', match.group(1))
            if len(digits) == 10 and digits != "7676379909":
                issues.append(f"Unapproved phone number found: {match.group(0)}")

        if re.search(r'1\.5k\+', content, re.I) or re.search(r'1500\+', content) or re.search(r'1,500\+', content):
            if "Anusha" in content or "Dance" in content:
                 issues.append("Incorrect Anusha hours variant (1.5k+/1500+) found")

        # 17. Redirect Stubs
        if file_class == "stub":
            has_canon = bool(canonical and canonical.has_attr('href'))
            if not has_canon or not is_noindex:
                issues.append("Stub lacks canonical or noindex")

        # 19. GTM
        gtm_head = re.findall(r"\(window,document,'script','dataLayer','GTM-[A-Z0-9]+'\)", content)
        gtm_noscript = re.findall(r'<iframe src="https://www.googletagmanager.com/ns\.html\?id=GTM-[A-Z0-9]+"', content)
        if len(gtm_head) != 1 or len(gtm_noscript) != 1:
            issues.append(f"GTM verification failed: {len(gtm_head)} head, {len(gtm_noscript)} noscript")

        # 20. Style blocks
        style_blocks = soup.find_all('style')
        info["style_block_count"] = len(style_blocks)

        report["files"][filepath] = {
            "info": info,
            "issues": issues
        }

    # 8b. Broken internal links (404 check)
    existing_files = {f.replace("\\", "/") for f in html_files}
    for source, target in all_internal_links:
        if target not in existing_files:
            if target != "index.html" or "" not in existing_files:
                report["files"][source]["issues"].append(f"Broken internal link to: {target}")

    # 18. Near duplicates
    file_list = list(bodies.keys())
    for i in range(len(file_list)):
        for j in range(i+1, len(file_list)):
            f1, f2 = file_list[i], file_list[j]
            t1, t2 = bodies[f1], bodies[f2]
            if len(t1) < 500 or len(t2) < 500:
                continue
            ratio = difflib.SequenceMatcher(None, t1, t2).quick_ratio()
            if ratio > 0.85:
                report["files"][f1]["issues"].append(f"Near-duplicate of {f2} (ratio {ratio:.2f})")
                report["files"][f2]["issues"].append(f"Near-duplicate of {f1} (ratio {ratio:.2f})")

    # 11b. Sitemap URLs exist
    for sm_url in sitemap_urls:
        if sm_url not in existing_files and sm_url != "":
            report["summary"].setdefault("sitemap_broken", []).append(sm_url)

    # Compile JSON
    with open(REPORT_JSON, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    # Compile MD
    pass_count = 0
    fail_count = 0

    with open(REPORT_MD, 'w', encoding='utf-8') as f:
        f.write("# Site Audit Report\n\n")
        f.write(f"Generated: {datetime.datetime.now().isoformat()}\n\n")

        f.write("## Summary\n\n")

        if "sitemap_broken" in report["summary"]:
            f.write("### Broken Sitemap URLs\n")
            for sm_url in report["summary"]["sitemap_broken"]:
                f.write(f"- {sm_url}\n")
            f.write("\n")

        f.write("## Per-File Results\n\n")
        f.write("| File | Class | Status | Issues | Style Blocks | Inbound Links |\n")
        f.write("|------|-------|--------|--------|--------------|---------------|\n")

        for filepath in sorted(report["files"].keys()):
            data = report["files"][filepath]
            cls = data["info"]["class"]
            styles = data["info"]["style_block_count"]
            inbound = data["info"].get("inbound_links", 0)
            issues = data["issues"]

            # Deduplicate issues
            issues = list(set(issues))

            if not issues:
                status = "✅ PASS"
                pass_count += 1
                iss_str = "None"
            else:
                status = "❌ FAIL"
                fail_count += 1
                iss_str = "<br>".join(issues)

            f.write(f"| {filepath} | {cls} | {status} | {iss_str} | {styles} | {inbound} |\n")

    print(f"Audit complete. PASS: {pass_count}, FAIL: {fail_count}")

if __name__ == "__main__":
    main()
