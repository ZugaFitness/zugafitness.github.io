import re

def demote_second_h1(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    h1_pattern = re.compile(r'<h1([^>]*)>(.*?)</h1>', flags=re.IGNORECASE | re.DOTALL)
    matches = list(h1_pattern.finditer(html))
    if len(matches) > 1:
        m = matches[1]
        start, end = m.span()
        new_tag = f'<h2{m.group(1)}>{m.group(2)}</h2>'
        html = html[:start] + new_tag + html[end:]
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

def main():
    demote_second_h1("trainer-bench.html")
    demote_second_h1("Blog/zumba-vs-gym-vs-yoga-weight-loss.html")

if __name__ == "__main__":
    main()
