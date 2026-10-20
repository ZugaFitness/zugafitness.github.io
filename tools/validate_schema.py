import json
import glob
from bs4 import BeautifulSoup

def validate_schema():
    html_files = glob.glob('**/*.html', recursive=True)
    failures = 0

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        scripts = soup.find_all('script', type='application/ld+json')

        for idx, script in enumerate(scripts):
            try:
                data = json.loads(script.string)

                # Check required fields based on @type
                if isinstance(data, dict) and '@graph' in data:
                    items = data['@graph']
                elif isinstance(data, list):
                    items = data
                else:
                    items = [data]

                for item in items:
                    if not isinstance(item, dict):
                        continue

                    item_type = item.get('@type')
                    if item_type == 'BlogPosting':
                        if 'headline' not in item:
                            print(f"FAIL: {file} - Block {idx} - BlogPosting missing 'headline'")
                            failures += 1
                        if 'datePublished' not in item:
                            print(f"FAIL: {file} - Block {idx} - BlogPosting missing 'datePublished'")
                            failures += 1
                        if 'author' not in item:
                            print(f"FAIL: {file} - Block {idx} - BlogPosting missing 'author'")
                            failures += 1
                    elif item_type == 'FAQPage':
                        if 'mainEntity' not in item:
                            print(f"FAIL: {file} - Block {idx} - FAQPage missing 'mainEntity'")
                            failures += 1
                        else:
                            main_entity = item['mainEntity']
                            if not isinstance(main_entity, list):
                                main_entity = [main_entity]
                            for q in main_entity:
                                if isinstance(q, dict) and q.get('@type') == 'Question':
                                    if 'acceptedAnswer' not in q:
                                        print(f"FAIL: {file} - Block {idx} - FAQPage Question missing 'acceptedAnswer'")
                                        failures += 1

            except json.JSONDecodeError as e:
                print(f"FAIL: {file} - Block {idx} - JSONDecodeError: {e}")
                failures += 1
            except Exception as e:
                print(f"FAIL: {file} - Block {idx} - Error: {e}")
                failures += 1

    if failures > 0:
        print(f"\nTotal failures: {failures}")
        exit(1)
    else:
        print("All schema blocks valid.")

if __name__ == '__main__':
    validate_schema()
