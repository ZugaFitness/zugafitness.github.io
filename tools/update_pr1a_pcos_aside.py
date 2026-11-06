import re

def main():
    with open("Blog/yoga-for-pcos-safe-poses-stress-hormones.html", "r", encoding="utf-8") as f:
        html = f.read()

    aside_html = """
<aside role="note" aria-label="Medical note"
style="margin:24px 0;padding:14px 18px;border:1px solid #d8d2c6;border-left:4px solid #b08d57;background:#faf7f2;font-size:14px;line-height:1.6;color:#4a4a4a;border-radius:6px;">
A note before you practise: PCOS is a medical condition. The sequences in this guide are educational movement practice, not treatment. They complement - never replace - care from your endocrinologist or gynaecologist. If you are pregnant, trying to conceive, on medication, or managing another condition alongside PCOS, consult your doctor before beginning this or any new practice. Stop any pose that causes pain, dizziness or unusual discomfort.
</aside>
"""
    html = re.sub(
        r'(<h2 class="section-title">)',
        aside_html + r'\1',
        html,
        count=1
    )

    with open("Blog/yoga-for-pcos-safe-poses-stress-hormones.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()
