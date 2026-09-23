import os
import re

files_to_update = [
    'pricing.html',
    'Online-Yoga-Classes.html',
    'Online-Dance-Fitness-Classes.html',
    'Online-Personal-Training-classes.html',
    'Online-Pranayama-Classes.html'
]

replacements = {
    '2,000': '1,999',
    '3,500': '3,499',
    '8,000': '7,999',
    '10,000': '9,999'
}

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()

        # Only replace prices in certain files, but keep schema valid (like "price": "2000" to "price": "1999").
        # We will handle schema in a separate regex or script step for safety.
        for old_price, new_price in replacements.items():
            content = content.replace(f'₹{old_price}', f'₹{new_price}')

        # Update meta descriptions specifically
        for old_price, new_price in replacements.items():
            content = content.replace(f'₹{old_price}', f'₹{new_price}')

        with open(filepath, 'w') as f:
            f.write(content)

print("Prices updated successfully.")
