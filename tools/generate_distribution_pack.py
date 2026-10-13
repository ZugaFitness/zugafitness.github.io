import sys
import os
import re
from bs4 import BeautifulSoup
import urllib.parse

def extract_core_keyword(h1_text):
    # Very basic heuristic for core keyword
    if "is zumba good for weight loss" in h1_text.lower():
        return "Zumba for weight loss"
    if "yoga for teenagers" in h1_text.lower():
        return "Yoga for teenagers"
    if "can yoga lower blood pressure" in h1_text.lower():
        return "Yoga for blood pressure"

    return h1_text.split("?")[0].split(":")[0].strip()

def process_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    filename = os.path.basename(filepath)
    slug = filename.replace('.html', '')
    original_zuga_url = f"https://zugafitness.in/Blog/{filename}"

    # 1. Extract H1
    h1_tag = soup.find('h1', class_='blog-title')
    if not h1_tag:
        h1_tag = soup.find('h1')
    h1 = h1_tag.get_text(strip=True) if h1_tag else "[H1 Missing]"

    core_keyword = extract_core_keyword(h1)

    # 2. Extract Meta Description
    meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
    meta_desc = meta_desc_tag['content'] if meta_desc_tag else "[Meta Description Missing]"

    # 3. Extract first 2 paragraphs
    intro_p = soup.find('p', class_='blog-intro')
    if intro_p:
        p1 = intro_p.get_text(strip=True)
    else:
        blog_content_div = soup.find('div', class_='blog-content')
        if blog_content_div:
             p1_tag = blog_content_div.find('p')
             p1 = p1_tag.get_text(strip=True) if p1_tag else "[Paragraph 1 Missing]"
        else:
             p1 = "[Paragraph 1 Missing]"

    p2 = "[Paragraph 2 Missing]"
    blog_sections = soup.find_all('div', class_='blog-section')
    if blog_sections:
        for section in blog_sections:
            first_p = section.find('p')
            if first_p:
                p2 = first_p.get_text(strip=True)
                if p2 != p1:
                    break

    # 4. Extract Key Takeaways
    key_takeaways_div = soup.find('div', class_='key-takeaways')
    if not key_takeaways_div:
        # Check for headings that look like Key Takeaways
        for h3 in soup.find_all('h3'):
            if 'Key Takeaways' in h3.get_text():
                key_takeaways_div = h3.parent
                break

    takeaways = []
    if key_takeaways_div:
        ul = key_takeaways_div.find('ul')
        if ul:
            takeaways = [li.get_text(strip=True) for li in ul.find_all('li')]

    first_takeaway = takeaways[0] if len(takeaways) > 0 else "[First Key Takeaway Missing]"

    # 5. Extract FAQ
    faq_questions = soup.find_all('div', class_='faq-question')
    faq_answers = soup.find_all('p', class_='faq-answer')

    first_faq_q = faq_questions[0].get_text(strip=True).replace('+', '').strip() if len(faq_questions) > 0 else "[FAQ Question Missing]"
    first_faq_a = faq_answers[0].get_text(strip=True) if len(faq_answers) > 0 else "[FAQ Answer Missing]"

    # 6. Extract full inner HTML of the blog post body
    blog_content_div = soup.find('div', class_='blog-content')
    if not blog_content_div:
        # Fallback to body content wrapper
        blog_content_div = soup.find('div', class_='blog-post')

    full_html = str(blog_content_div) if blog_content_div else "[Blog Content Missing]"

    # Append author section if exists and not inside blog-content
    author_section = soup.find('div', class_='author-section')
    if author_section and str(author_section) not in full_html:
        full_html += "\n" + str(author_section)

    # 7. Extract Clinical Sentence
    clinical_sentence = "[Clinical Sentence Missing]"
    paragraphs = soup.find_all('p')
    clinical_keywords = ['study', 'physiology', 'metabolism', 'nervous system', 'percent', '%', 'research', 'hormone', 'blood pressure', 'calorie', 'burn']

    for p in paragraphs:
        text = p.get_text(strip=True)
        # Avoid intro and takeaways and faqs and subtitle
        if text == p1 or text == p2 or text == first_takeaway or text == first_faq_a or p.get('class') == ['blog-subtitle']:
            continue

        sentences = re.split(r'(?<=[.!?])\s+', text)
        for s in sentences:
            if any(k in s.lower() for k in clinical_keywords) or any(char.isdigit() for char in s):
                # Ensure it's not a short subtitle-like string
                if len(s) > 30 and 'updated' not in s.lower():
                    clinical_sentence = s
                    break
        if clinical_sentence != "[Clinical Sentence Missing]":
            break

    # GENERATE PACK
    pack_md = f"""# Distribution Pack for {h1}

## 1. LinkedIn Article Version

{h1}

{p1}

{p2}

---
[INSERT 1-2 SENTENCES OF FOUNDER'S PERSONAL TAKEAWAY HERE]
---

What has been your experience with {core_keyword}? Let me know in the comments.
(Link to the full clinical guide in the comments below: {original_zuga_url})


## 2. Medium Version

```html
<!-- CANONICAL INSTRUCTION: When pasting into Medium, go to Settings -> Advanced Settings -> Canonical Link and paste: {original_zuga_url} -->
{full_html}
```

## 3. Quora Answer Seed

Based on my experience as a certified yoga instructor at Zuga Fitness, here is the honest answer:

- {first_takeaway}

{first_faq_a}

[INSERT 1 SENTENCE CONNECTING THIS TO A REAL CLIENT STORY HERE]

For a deeper clinical breakdown, you can read our full guide here: {original_zuga_url}


## 4. Pinterest Pin Text

**Pin 1 (Direct):**
- **Title:** {h1[:100]}
- **Description:** {meta_desc[:480]} #yoga #wellness

**Pin 2 (Question):**
- **Title:** How long does {core_keyword} take?
- **Description:** {first_takeaway[:450]} Read the full timeline at Zuga Fitness.

**Pin 3 (Listicle/Benefit):**
- **Title:** 3 truths about {core_keyword}
"""

    pin3_desc = ""
    for i, t in enumerate(takeaways[:3]):
        pin3_desc += f"{i+1}. {t[:50]}... "
    pin3_desc += "#yoga #wellness"

    pack_md += f"- **Description:** {pin3_desc.strip()[:500]}\n\n"

    pack_md += f"""
## 5. Expert Quote Angles

**Quote 1:** "{clinical_sentence} In my practice coaching online cohorts, I've found this is the missing link for most desk-workers." - Anusha YP, Co-Founder Zuga Fitness

**Quote 2:** "{first_faq_a} This is the exact framework we use in our 90-day metabolic reset." - Mallinath Beelur, Co-Founder Zuga Fitness
"""

    os.makedirs('seo/distribution_packs', exist_ok=True)
    out_path = f"seo/distribution_packs/{slug}-pack.md"

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(pack_md)

    print(f"Generated distribution pack: {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_distribution_pack.py <filepath_or_url> [<filepath_or_url> ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        process_file(arg)
