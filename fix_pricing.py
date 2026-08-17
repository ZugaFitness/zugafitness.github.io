import os

files_to_update = [
    'pricing.html'
]

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()

        content = content.replace('"Starter Plan"', '"Group Classes"')

        with open(filepath, 'w') as f:
            f.write(content)

print("Renamed Starter in pricing schema successfully.")
