import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for idempotency
    if 'GTM-K2QTDPJ2' in content:
        return False

    gtm_script = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-K2QTDPJ2');</script>
<!-- End Google Tag Manager -->"""

    gtm_noscript = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K2QTDPJ2"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

    # We shouldn't use capture groups and \1 in string concatenation if we just want to replace
    # We will use re.sub with a function or just replace the string

    def head_repl(match):
        return match.group(0) + gtm_script

    def body_repl(match):
        return match.group(0) + gtm_noscript

    head_pattern = re.compile(r'(<head[^>]*>)', re.IGNORECASE)
    content, num_subs_head = head_pattern.subn(head_repl, content, count=1)

    if num_subs_head == 0:
        print(f"Warning: Could not find <head> in {filepath}")
        return False

    body_pattern = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
    content, num_subs_body = body_pattern.subn(body_repl, content, count=1)

    if num_subs_body == 0:
        print(f"Warning: Could not find <body> in {filepath}")
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    root_dir = '.'
    modified_count = 0
    total_html_files = 0

    for root, dirs, files in os.walk(root_dir):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')

        for file in files:
            if file.endswith('.html'):
                total_html_files += 1
                filepath = os.path.join(root, file)
                if process_file(filepath):
                    modified_count += 1

    print(f"Processed {total_html_files} HTML files.")
    print(f"Injected GTM into {modified_count} files.")

if __name__ == '__main__':
    main()
