import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = re.compile(r'</script>.*?<!-- Single High-Ticket CTA -->.*?</section>', re.DOTALL)
html = pattern.sub(r'</script>', html)

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
