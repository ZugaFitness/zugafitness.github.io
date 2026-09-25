import os
import glob

EXCLUDE = [
    'free-trial.html',
    'thank-you.html',
    'weight-loss-challenge.html',
    'wlc-form.html',
    'personal-training-consultation.html',
    'Online-Personal-Training-classes.html',
    '404.html'
]

CSS_TAG = '<link rel="stylesheet" href="/assets/css/whatsapp-concierge.css">'
JS_TAG = '<script defer src="/assets/js/whatsapp-concierge.js"></script>'

def is_excluded(filepath):
    filename = os.path.basename(filepath)
    if filename in EXCLUDE:
        return True
    if filename.startswith('google') and filename.endswith('.html'):
        return True
    return False

def inject_tags(filepath):
    if is_excluded(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if CSS_TAG in content and JS_TAG in content:
        return False

    if '</head>' in content:
        if CSS_TAG not in content:
            content = content.replace('</head>', f'{CSS_TAG}\n</head>')
        if JS_TAG not in content:
            content = content.replace('</head>', f'{JS_TAG}\n</head>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

if __name__ == "__main__":
    count = 0
    root_html = glob.glob('*.html')
    for f in root_html:
        if inject_tags(f): count += 1
    blog_html = glob.glob('Blog/*.html')
    for f in blog_html:
        if inject_tags(f): count += 1
    blr_html = glob.glob('Yoga-Classes-In-Bangalore/*.html')
    for f in blr_html:
        if inject_tags(f): count += 1
    print(f"Successfully injected WhatsApp Concierge into {count} files.")
