import os
import re

def extract_head(content):
    head_match = re.search(r'(<head[^>]*>)', content, flags=re.IGNORECASE)
    if head_match:
        head_tag_end = head_match.end()
        head_end_match = re.search(r'</head>', content, flags=re.IGNORECASE)
        if head_end_match:
            head_content = content[head_tag_end:head_end_match.start()]
            return head_tag_end, head_end_match.start(), head_content
    return None, None, None

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return

    original = content
    is_blog_dir = 'Blog' in filepath
    is_blog_post = is_blog_dir and not filepath.endswith('index.html')

    start, end, head_content = extract_head(content)
    if head_content is not None:
        if is_blog_post:
            # We already ran the other script, but it might have missed adding OG meta tags because of regex matching logic for title/desc.
            title_match = re.search(r'<title>(.*?)</title>', head_content, flags=re.IGNORECASE | re.DOTALL)
            title_text = title_match.group(1).strip() if title_match else ""

            desc_match = re.search(r'<meta[^>]*?name="description"[^>]*?content="([^"]*?)"[^>]*?>', head_content, flags=re.IGNORECASE)
            desc_text = desc_match.group(1).strip() if desc_match else ""

            if not desc_text:
                desc_match = re.search(r'<meta[^>]*?content="([^"]*?)"[^>]*?name="description"[^>]*?>', head_content, flags=re.IGNORECASE)
                desc_text = desc_match.group(1).strip() if desc_match else ""

            has_og_title = 'property="og:title"' in head_content
            has_og_desc = 'property="og:description"' in head_content

            if not has_og_title and title_text:
                head_content += f'\n  <meta property="og:title" content="{title_text}">'
            if not has_og_desc and desc_text:
                head_content += f'\n  <meta property="og:description" content="{desc_text}">'

            has_og_title = 'property="og:title"' in head_content
            has_og_desc = 'property="og:description"' in head_content

            if 'name="twitter:card"' not in head_content:
                head_content += '\n  <meta name="twitter:card" content="summary_large_image">'

            if 'name="twitter:site"' not in head_content:
                head_content += '\n  <meta name="twitter:site" content="@zugafitness">'

            if 'name="twitter:title"' not in head_content and has_og_title:
                head_content += f'\n  <meta name="twitter:title" content="{title_text}">'

            if 'name="twitter:description"' not in head_content and has_og_desc:
                head_content += f'\n  <meta name="twitter:description" content="{desc_text}">'

        # Task 7 Preconnect fix for fonts.googleapis.com
        if 'https://fonts.googleapis.com' not in head_content:
            head_content += '\n  <link rel="preconnect" href="https://fonts.googleapis.com">'

        content = content[:start] + head_content + content[end:]

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed meta in {filepath}")

def main():
    for root, _, files in os.walk('.'):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                fix_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
