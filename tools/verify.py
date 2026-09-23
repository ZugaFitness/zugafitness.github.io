import re

files = [
    'pricing.html',
    'Online-Yoga-Classes.html',
    'Online-Dance-Fitness-Classes.html',
    'Online-Personal-Training-classes.html',
    'Online-Pranayama-Classes.html'
]

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    issues = []
    if '2,000' in content or '"2000"' in content: issues.append("Old price 2,000 found")
    if '3,500' in content or '"3500"' in content: issues.append("Old price 3,500 found")
    if '8,000' in content or '"8000"' in content: issues.append("Old price 8,000 found")
    if '10,000' in content or '"10000"' in content: issues.append("Old price 10,000 found")

    if issues:
        print(f"Issues in {file}: {issues}")
    else:
        print(f"No old prices found in {file}")
