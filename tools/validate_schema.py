import os
import glob
from bs4 import BeautifulSoup
import json

def validate_schema(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    schema_script = soup.find('script', type='application/ld+json')
    if schema_script:
        try:
            schema_data = json.loads(schema_script.string)
            return True, None
        except json.JSONDecodeError as e:
            return False, f"JSONDecodeError: {e}"
        except Exception as e:
            return False, f"Exception: {e}"
    return True, "No schema found"

html_files = glob.glob("**/*.html", recursive=True)
all_valid = True

for file in html_files:
    valid, msg = validate_schema(file)
    if not valid:
        print(f"FAIL: {file} - {msg}")
        all_valid = False

if all_valid:
    print("PASS: All JSON-LD schemas in repository are valid.")
else:
    print("FAIL: Found invalid schema(s).")
