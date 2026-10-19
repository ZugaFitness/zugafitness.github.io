import re

with open("tools/generate_pins.py", "r", encoding="utf-8") as f:
    content = f.read()

new_pin = """    {
        "slug": "zumba-vs-gym-vs-yoga-weight-loss",
        "badge": "health",
        "headline": "Zumba vs Gym Cardio vs Yoga",
        "subhead": "Which Actually Burns More Fat?",
        "bg_image": "../assets/images/online-zumba-classes-at-home.webp"
    },"""

# Insert at the beginning of the PINS list
content = re.sub(
    r'(PINS = \[)',
    r'\g<1>\n' + new_pin,
    content
)

with open("tools/generate_pins.py", "w", encoding="utf-8") as f:
    f.write(content)
