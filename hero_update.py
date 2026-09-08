import re

with open('corporate-wellness-productivity.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace H1
content = re.sub(
    r'<h1 class="font-headline-xl text-5xl md:text-headline-xl text-on-background mb-6 leading-none">\s*Corporate Wellness Programs in Bangalore\s*</h1>',
    '<h1 class="font-headline-xl text-5xl md:text-headline-xl text-on-background mb-6 leading-none">\n                    Wellness Isn\'t a Perk. It\'s a Productivity Multiplier.\n</h1>',
    content,
    flags=re.DOTALL
)

# Replace Subtitle
content = re.sub(
    r'<p class="font-body-lg text-xl md:text-body-lg text-on-surface-variant mb-10 max-w-xl">\s*Revolutionary Corporate Yoga &amp; Zumba experiences designed to ignite peak performance and employee joy in the heart of Bangalore.\s*</p>',
    '<p class="font-body-lg text-xl md:text-body-lg text-on-surface-variant mb-10 max-w-xl">\n                    Your team is your most valuable asset. Burnout, chronic stress, and desk-induced fatigue are silently killing your company\'s productivity. We don\'t just teach yoga; we build structured, live wellness programs that reset your team\'s nervous system, improve focus, and drive measurable performance.\n                </p>',
    content,
    flags=re.DOTALL
)

# Replace "BANGALORE'S VIBRANT ENERGY" text
content = re.sub(
    r'BANGALORE\'S VIBRANT ENERGY',
    'HIGH-PERFORMANCE WELLNESS',
    content
)

# Update buttons
content = re.sub(
    r'<a class="bg-primary-container text-on-primary-container font-headline-md px-10 py-5 rounded-xl shadow-xl hover:scale-105 active:scale-95 transition-all duration-300 animate-pulse-slow inline-block text-center" href="#inquiry">\s*REQUEST PROPOSAL\s*</a>',
    '<a class="bg-primary-container text-on-primary-container font-headline-md px-10 py-5 rounded-xl shadow-xl hover:scale-105 active:scale-95 transition-all duration-300 animate-pulse-slow inline-block text-center" href="/contact.html">\n                        REQUEST TAILORED QUOTE\n                    </a>',
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<a class="border-2 border-primary text-primary font-headline-md px-10 py-5 rounded-xl hover:bg-primary/5 transition-all inline-block text-center" href="#services">\s*VIEW SERVICES\s*</a>',
    '<a class="border-2 border-primary text-primary font-headline-md px-10 py-5 rounded-xl hover:bg-primary/5 transition-all inline-block text-center" href="#framework">\n                        EXPLORE THE FRAMEWORK\n                    </a>',
    content,
    flags=re.DOTALL
)

with open('corporate-wellness-productivity.html', 'w', encoding='utf-8') as f:
    f.write(content)
