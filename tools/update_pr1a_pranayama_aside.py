import re

def main():
    with open("Online-Pranayama-Classes.html", "r", encoding="utf-8") as f:
        html = f.read()

    aside_html = """
    <aside role="note" aria-label="Medical note"
    style="margin:24px 0;padding:14px 18px;border:1px solid #d8d2c6;border-left:4px solid #b08d57;background:#faf7f2;font-size:14px;line-height:1.6;color:#4a4a4a;border-radius:6px;">
    Practice safely: our breathwork sessions are educational movement practice, not medical or psychological treatment. If you have unmanaged hypertension, glaucoma, a cardiac or respiratory condition, are pregnant, or experience dizziness or anxiety with breath retention, consult your doctor before joining, and skip retention practices until cleared. Stop immediately if you feel light-headed, tingling or chest tightness.
    </aside>
"""
    html = re.sub(
        r'(<p class="lead mb-5" style="font-size: 1\.25rem;">Expert 1-on-1 online breathwork for stress relief, deep sleep, and cognitive clarity\. Live sessions tailored to your schedule\.</p>)',
        r'\1' + aside_html,
        html
    )

    with open("Online-Pranayama-Classes.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()
