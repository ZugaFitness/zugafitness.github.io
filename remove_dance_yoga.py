import re
import sys

def remove_dance_card(html_content):
    # To reliably remove the exact column block starting with the comment,
    # we can use a more precise regex.
    # We are looking for:
    # 1. the comment `<!-- Starter Dance -->` (or similar)
    # 2. the opening `<div class="col-md-3 mb-4">`
    # 3. the nested content (we know it's a card)
    # 4. We want to remove up to the NEXT comment, or the closing of the row.

    # Let's try this: match the comment and then match `<div ...`
    # then match non-greedily up to a point where either `<!--` follows or `</div` follows without opening a new div.
    # Actually, the simplest approach for a one-off script is to match up to a specific number of closing divs
    # if we know the structure.
    # But since the prompt gives a snippet with:
    # `<!-- Starter Dance -->`
    # `<div class="col-md-3 mb-4">`
    # We can match `<!-- Starter Dance -->` and then `<div class="col-md-3 mb-4">` and then we want to stop
    # matching just before the next element of the list. The next element is usually another comment `<!-- ... -->`
    # or the end of the list `</div>`.

    # A regex that matches the comment, the div, and then any characters non-greedy until `\s*<!--` or `\s*</div>\s*$`
    # Wait, the problem with `.*?` is it might match too little or too much.

    # A very common pattern for this is matching everything up to the next sibling element.
    # Let's use:
    pattern = re.compile(r'\s*<!--\s*Starter Dance\s*-->\s*<div class="col-md-3 mb-4">.*?(?=\s*(?:<!--|\s*</div>\s*(?:</div>|</section>)))', re.DOTALL)

    # A safer alternative is extracting exactly 2 or 3 closing divs, assuming the structure is static.
    # But let's try a regex that just replaces the specific block.
    # The tests use a simplified structure:
    # <div class="col-md-3 mb-4">
    #     <div class="card...">...</div>
    # </div>
    # So there are 2 closing divs.

    # Let's implement a small python logic to count divs!

    start_idx = html_content.find('<!-- Starter Dance -->')
    if start_idx == -1:
        start_idx = html_content.find('<!--Starter Dance-->')

    if start_idx == -1:
        return html_content

    # We want to remove the whitespace before it too.
    # Find the last newline before start_idx
    ws_start = html_content.rfind('\n', 0, start_idx)
    if ws_start != -1 and html_content[ws_start:start_idx].isspace():
        start_idx = ws_start + 1 # keep the newline

    # Find the end of the div
    # Look for the opening <div
    div_start = html_content.find('<div', start_idx)
    if div_start == -1:
        return html_content

    # Count divs
    div_count = 0
    i = div_start
    while i < len(html_content):
        if html_content.startswith('<div', i):
            div_count += 1
            i += 4
        elif html_content.startswith('</div', i):
            div_count -= 1
            if div_count == 0:
                # Found the matching closing div!
                end_idx = html_content.find('>', i) + 1
                return html_content[:start_idx] + html_content[end_idx:]
            i += 5
        else:
            i += 1

    return html_content

def main():
    try:
        with open('Online-Yoga-Classes.html', 'r') as f:
            content = f.read()

        new_content = remove_dance_card(content)

        with open('Online-Yoga-Classes.html', 'w') as f:
            f.write(new_content)

        print("Successfully processed Online-Yoga-Classes.html")
    except FileNotFoundError:
        print("File Online-Yoga-Classes.html not found.")
        sys.exit(1)

if __name__ == '__main__':
    main()
