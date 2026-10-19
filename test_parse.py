from bs4 import BeautifulSoup
import sys

with open("Blog/zumba-vs-gym-vs-yoga-weight-loss.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

if len(soup.find_all('h1')) != 1:
    print("Error: more than one h1 found")
    sys.exit(1)

ids = [t['id'] for t in soup.find_all(id=True)]
if len(ids) != len(set(ids)):
    print("Error: duplicate ids found")
    sys.exit(1)

if not soup.find(class_='navbar'):
    print("Error: missing navbar")
    sys.exit(1)

print("Parse check passed.")
