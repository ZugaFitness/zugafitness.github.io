import re
import sys
import xml.etree.ElementTree as ET

with open("Blog/zumba-vs-gym-vs-yoga-weight-loss.html", "r", encoding="utf-8") as f:
    html = f.read()

def assert_present(name, pattern):
    if not re.search(pattern, html):
        print(f"Error: {name} not found")
        sys.exit(1)

def assert_absent(name, pattern):
    if re.search(pattern, html):
        print(f"Error: {name} was found")
        sys.exit(1)

# Grep-presence
assert_present("The Raw Calorie Math", r'The Raw Calorie Math')
assert_present("Internal Link 1", r'/Online-Dance-Fitness-Classes\.html')
assert_present("Internal Link 2", r'/weight-loss-challenge\.html')
assert_present("Anusha Bio", r"Anusha is a Certified Yoga &amp; Zumba Instructor at Zuga Fitness, specialising in women's wellness and postnatal-safe movement")
assert_present("Anusha Image", r'anusha-7b37cda6\.webp')

# Grep-absence
assert_absent("Back pain", r'back(-|\s)pain')
assert_absent("Old date", r'2026-08-22')

# Sitemap XML validation
try:
    tree = ET.parse("sitemap.xml")
    print("Sitemap parsed successfully.")
except Exception as e:
    print("Error parsing sitemap:", str(e))
    sys.exit(1)

print("All grep gates and sitemap validation passed.")
