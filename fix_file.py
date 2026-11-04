with open('hybrid-fitness.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Did I delete a bunch of sections? Let's check the size of the DOM in the python script.
print(f"Total characters: {len(html)}")

import re
print("Hero:", bool(re.search(r'<section class="hero">', html)))
print("Practice:", bool(re.search(r'<section class="sec" id="practice">', html)))
print("Schedule:", bool(re.search(r'<section class="sec" id="schedule">', html)))
print("Teachers:", bool(re.search(r'<section class="sec" id="teachers">', html)))
print("Membership:", bool(re.search(r'<section class="sec" id="membership".*?>', html)))
print("Voices:", bool(re.search(r'<section class="sec" id="voices">', html)))
print("FAQ:", bool(re.search(r'<section class="sec" id="faq">', html)))
print("Signup:", bool(re.search(r'<section class="sec cta" id="signup">', html)))
