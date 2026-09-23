import re

with open('Online-Yoga-Classes.html', 'r') as f:
    content = f.read()

# 1. Remove the Starter Dance card entirely
# 2. Update col-md-3 to col-md-4 for the remaining 3 cards (Starter Yoga, Growth Bundle, 1-on-1 Private) to ensure they look good if we just removed one. Wait, the prompt says "100% dedicated to Group Yoga (₹1,999) and 1-on-1 Yoga PT." This might imply removing Growth Bundle as well, OR renaming it to just Yoga if it had Dance. The Growth Bundle says:
# "✅ Yoga + Dance Fitness"

# Prompt: "REMOVE all Dance Fitness pricing tables, cards, and mentions from this page.
# This page must now be 100% dedicated to Group Yoga (₹1,999) and 1-on-1 Yoga PT.
# Ensure internal links to the Dance page remain intact, but strip all Dance pricing/sales copy from this specific file."

# Let's remove Starter Dance card and Growth Bundle card, leaving only Group Yoga and 1-on-1 Private.
# We'll make them col-md-6 instead of col-md-3.
pass
