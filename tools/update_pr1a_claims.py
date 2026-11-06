import re

def main():
    with open("Blog/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    html = re.sub(
        r'Why Strength Training \+ Yoga is the Science-Backed (?:Cure|Management Guide) for PCOD',
        r'Strength Training + Yoga for PCOS: What a Consistent Practice Can Support',
        html
    )

    html = re.sub(
        r'Struggling with PCOS symptoms\? Discover how safe yoga for pcos\s*can help balance hormones and reduce stress\. Book your free\s*1-on-1 session today!',
        r"How safe, sequenced yoga for PCOS supports stress management and consistent movement - alongside your doctor's care.",
        html, flags=re.IGNORECASE | re.DOTALL
    )

    html = re.sub(
        r'PCOD Yoga Poses: Natural Hormone Balance for Busy Women',
        r'PCOD Yoga Poses: How a Gentle Practice May Support Hormonal Health for Busy Women',
        html
    )

    with open("Blog/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    with open("Blog/yoga-and-strength-training-for-pcod.html", "r", encoding="utf-8") as f:
        html2 = f.read()

    html2 = re.sub(
        r'Why Strength Training \+ Yoga is the Science-Backed (?:Cure|Management Guide) for PCOD',
        r'Strength Training + Yoga for PCOS: What a Consistent Practice Can Support',
        html2
    )
    with open("Blog/yoga-and-strength-training-for-pcod.html", "w", encoding="utf-8") as f:
        f.write(html2)

    print("Blog/index.html and Blog/yoga-and-strength-training-for-pcod.html updated.")

if __name__ == "__main__":
    main()
