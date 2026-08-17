import os

files_to_update = [
    'Online-Yoga-Classes.html',
    'Online-Dance-Fitness-Classes.html',
    'Online-Personal-Training-classes.html',
    'Online-Pranayama-Classes.html'
]

for filepath in files_to_update:
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()

        content = content.replace('>Starter Plan<', '>Group Classes<')
        content = content.replace('>Starter Yoga<', '>Group Yoga<')
        content = content.replace('>Starter Dance<', '>Group Dance Fitness<')
        content = content.replace('"Starter Plan"', '"Group Classes"')
        content = content.replace('"Starter Yoga"', '"Group Yoga"')

        with open(filepath, 'w') as f:
            f.write(content)

print("Renamed Starter across all files successfully.")
