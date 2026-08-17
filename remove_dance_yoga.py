import re

with open('Online-Yoga-Classes.html', 'r') as f:
    content = f.read()

# We need to find the "Starter Dance" or "Group Dance Fitness" column and remove it.
# The card seems to be inside a <div class="col-md-3 mb-4"> or similar. Let's look for the structure.

# Looking at the earlier grep:
# <!-- Starter Dance -->
# <div class="col-md-3 mb-4">
# ...
# </div>

pattern_dance_card = re.compile(r'<!--\s*Starter Dance\s*-->\s*<div class="col-md-3 mb-4">.*?</div>\s*<!--', re.DOTALL)
# It's probably followed by another comment like <!-- Growth Plan -->. We can be safer by just writing a regex.

# Let's extract the pricing row to be safe and manually fix it.
