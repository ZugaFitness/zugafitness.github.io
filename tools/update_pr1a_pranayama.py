import re

def main():
    with open("Online-Pranayama-Classes.html", "r", encoding="utf-8") as f:
        html = f.read()

    html = re.sub(
        r'<h1([^>]*)>Clinical Nervous System Regulation for the High-Performance Executive</h1>',
        r'<h2\1>Nervous-System-Regulating Breathwork for High-Performance Executives</h2>',
        html
    )

    with open("Online-Pranayama-Classes.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()
