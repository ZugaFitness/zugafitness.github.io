import os
import re

files_to_update = [
    'pricing.html',
    'Online-Yoga-Classes.html',
    'Online-Dance-Fitness-Classes.html',
    'Online-Personal-Training-classes.html',
    'Online-Pranayama-Classes.html'
]

schema_replacements = {
    '"price": "2000"': '"price": "1999"',
    '"price": "3500"': '"price": "3499"',
    '"price": "8000"': '"price": "7999"',
    '"price": "10000"': '"price": "9999"'
}

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()

        for old, new in schema_replacements.items():
            content = content.replace(old, new)

        with open(filepath, 'w') as f:
            f.write(content)

print("Schema prices updated successfully.")
