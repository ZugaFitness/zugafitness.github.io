from bs4 import BeautifulSoup
import json
import os

with open("Blog/yoga-for-back-pain-relief.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 1. Update Title and Meta Tags
title_str = "Yoga for Desk Workers: A 12-Minute Routine for Back & Neck Pain"
desc_str = "Sitting at a desk in Bangalore all day? This 12-minute, no-mat yoga routine reverses tech-neck, opens the hips, and resets your nervous system between Zoom calls."
url_str = "https://zugafitness.in/Blog/yoga-for-desk-workers-bangalore-12-minute-routine.html"
image_str = "https://zugafitness.in/assets/images/corporate-wellness-bangalore-1.webp"

if soup.title: soup.title.string = title_str
meta_desc = soup.find('meta', attrs={'name': 'description'})
if meta_desc: meta_desc['content'] = desc_str

og_title = soup.find('meta', attrs={'property': 'og:title'})
if og_title: og_title['content'] = title_str

og_desc = soup.find('meta', attrs={'property': 'og:description'})
if og_desc: og_desc['content'] = desc_str

og_image = soup.find('meta', attrs={'property': 'og:image'})
if og_image: og_image['content'] = image_str

og_url = soup.find('meta', attrs={'property': 'og:url'})
if og_url: og_url['content'] = url_str

twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
if twitter_title: twitter_title['content'] = title_str

twitter_desc = soup.find('meta', attrs={'name': 'twitter:description'})
if twitter_desc: twitter_desc['content'] = desc_str

twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
if twitter_image: twitter_image['content'] = image_str

canonical = soup.find('link', rel='canonical')
if canonical: canonical['href'] = url_str


# 2. Body Header / Metadata
h1 = soup.find('h1')
if h1: h1.string = "Yoga for Desk Workers: The 12-Minute \"Between Meetings\" Routine"

# Update date in blog-meta
blog_meta = soup.find('div', class_='blog-meta')
if blog_meta:
    # First span is date
    spans = blog_meta.find_all('span')
    if spans:
        spans[0].string = ""
        icon = soup.new_tag("i")
        icon['class'] = "far fa-calendar"
        spans[0].append(icon)
        spans[0].append(" October 23, 2026")
        spans[2].string = "Corporate Wellness"

# Key Takeaways
takeaways_div = soup.find('div', class_='key-takeaways')
if takeaways_div:
    ul = takeaways_div.find('ul')
    if ul:
        ul.clear()

        li1 = soup.new_tag("li")
        li1.append("You don't need a mat or a 60-minute block to fix desk posture; 12 minutes of targeted mobility resets the thoracic spine and hips.")
        ul.append(li1)

        li2 = soup.new_tag("li")
        li2.append("\"Tech-neck\" and lower back stiffness are rarely flexibility issues; they are nervous system tension and sustained isometric loading.")
        ul.append(li2)

        li3 = soup.new_tag("li")
        li3.append("Doing this routine at 3 PM prevents the \"afternoon slump\" better than a second cup of coffee by regulating cortisol and blood flow.")
        ul.append(li3)

# Main Hero Image
hero_img = soup.find('img', alt="Yoga for back pain relief asanas guide")
if hero_img:
    hero_img['src'] = "../assets/images/corporate-wellness-bangalore-1.webp"
    hero_img['alt'] = "Yoga for Desk Workers: The 12-Minute Between Meetings Routine"

# 3. Main Content Replacement
blog_content = soup.find('div', class_='blog-content')
if blog_content:
    # Clear existing content after the hero image
    for elem in list(blog_content.children):
        if elem.name and elem.name not in ['h1', 'img', 'div'] and not (elem.name == 'div' and ('key-takeaways' in elem.get('class', []) or 'blog-meta' in elem.get('class', []))):
            elem.extract()
        elif elem.name == 'div' and 'blog-section' in elem.get('class', []):
            elem.extract()
        elif elem.name == 'section' and 'faq-section' in elem.get('class', []):
            elem.extract()
        elif elem.name == 'div' and 'author-section' in elem.get('class', []):
            elem.extract()

    # The new body HTML to append
    new_body_html = """
<div class="blog-section">
    <h2 class="section-title">1. The 3 PM Slump: Why Your Back Hurts and Your Brain Fogs</h2>
    <p>We've all experienced it. It's 3 PM, you've been in back-to-back Zoom calls, and suddenly your lower back feels like a block of concrete. Your neck aches, and your focus completely evaporates. You might think reaching for a second cup of coffee or pushing through another hour is the answer, but the real issue isn't fatigue—it's posture and nervous system tension.</p>
    <p>Sitting at a desk all day creates sustained isometric loading on your spine and hips. Stretching your hamstrings alone won't fix it. What you need is a targeted mobility protocol to reverse "tech-neck", open up the hips, and flush oxygen back into your system. If you want to see how we tackle this organization-wide, check out our <a href="/corporate-wellness-bangalore.html">corporate wellness programs in Bangalore</a>.</p>
</div>

<div class="blog-section">
    <h2 class="section-title">2. The 12-Minute Protocol: 4 Poses, 3 Minutes Each</h2>
    <p>You don't need a yoga mat or a full hour. This 12-minute, desk-friendly routine is designed to be done right in your office chair or standing beside your desk.</p>

    <h3>Seated Cat-Cow (Thoracic Mobility)</h3>
    <p>While seated, place your hands on your knees. As you inhale, arch your back and open your chest (Cow). As you exhale, round your spine and tuck your chin (Cat). This simple movement restores mobility to the thoracic spine, which gets locked up from hunching over a keyboard.</p>

    <h3>Chair Pigeon (Hip Opener for Sitting)</h3>
    <p>Still seated, cross your right ankle over your left knee. Keeping your spine straight, gently hinge forward from the hips until you feel a deep stretch in your right glute. Switch sides. This reverses the hip compression caused by hours in a chair.</p>

    <h3>Seated Thread the Needle (Shoulder/Neck Release)</h3>
    <p>Take your right arm and gently cross it over your body, using your left hand to pull it closer. Look over your right shoulder. This releases the deep tension accumulating in the upper back and neck from staring at a screen.</p>

    <h3>Standing Desk Forward Fold (Decompress the Spine)</h3>
    <p>Stand up, place your hands flat on your desk, and walk your feet back until your torso is parallel to the floor, forming an "L" shape. Let your head hang between your arms. This decompresses the spine and provides a much-needed stretch for the entire back body.</p>
</div>

<div class="blog-section">
    <h2 class="section-title">3. How to Build the Habit: Trigger Stacking</h2>
    <p>The secret to consistency isn't willpower; it's trigger stacking. Attach this 12-minute routine to an existing daily habit. Do it while your daily standup meeting runs over (just turn off your camera), or commit to doing it immediately after lunch before opening your email.</p>
    <p>Frequency beats duration. Doing this small reset every single workday is vastly superior to doing a single 60-minute class on Sunday.</p>
</div>

<section class="faq-section" id="faq-section">
    <div class="section-header">
        <h2 class="section-title text-center">Frequently Asked Questions</h2>
    </div>
    <div class="faq-container">
        <div class="faq-item">
            <div class="faq-question" data-bs-target="#faq-q1" data-bs-toggle="collapse" style="cursor: pointer; display: flex; justify-content: space-between;"><strong>Can I do yoga at my office desk without looking weird?</strong> <span>+</span></div>
            <div class="collapse mt-3" id="faq-q1">
                <p class="faq-answer">Yes. Seated cat-cow, neck rolls, and seated spinal twists are invisible to your coworkers but highly effective for reversing the damage of sitting for 8 hours.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-question" data-bs-target="#faq-q2" data-bs-toggle="collapse" style="cursor: pointer; display: flex; justify-content: space-between;"><strong>How often should desk workers do yoga?</strong> <span>+</span></div>
            <div class="collapse mt-3" id="faq-q2">
                <p class="faq-answer">Frequency beats duration. Doing a 10-minute mobility reset every single workday is vastly superior to doing a 60-minute class once a week on Sunday.</p>
            </div>
        </div>

        <div class="faq-item">
            <div class="faq-question" data-bs-target="#faq-q3" data-bs-toggle="collapse" style="cursor: pointer; display: flex; justify-content: space-between;"><strong>Does yoga help with desk-job fatigue?</strong> <span>+</span></div>
            <div class="collapse mt-3" id="faq-q3">
                <p class="faq-answer">Yes. Desk fatigue is often shallow breathing and restricted blood flow from compressed hips. Opening the chest and hips restores oxygen flow and down-regulates the stress response.</p>
            </div>
        </div>
    </div>
</section>

<div class="author-section">
    <div class="author-image">
        <img alt="Mallinath Beelur" loading="lazy" src="../assets/images/photo-2025-03-08-15-59-42jpg-518x921.jpeg"/>
    </div>
    <div class="author-info">
        <h3>Mallinath Beelur</h3>
        <p>Mallinath Beelur is the co-founder of Zuga Fitness. He works with HR and people-ops teams on live online and hybrid corporate wellness programs across Bangalore, the Gulf and English-speaking markets.</p>
    </div>
</div>

<div class="blog-section">
    <p>Want to bring this to your whole office? Explore our <a href="/trainer-bench.html">instructor bench</a> to see how our corporate wellness team can revitalize your workplace.</p>
</div>
"""
    new_soup = BeautifulSoup(new_body_html, 'html.parser')
    blog_content.append(new_soup)

# 4. Schema Update
schema_script = soup.find('script', type='application/ld+json')
if schema_script:
    schema_data = {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "BlogPosting",
          "headline": title_str,
          "description": desc_str,
          "author": {
            "@type": "Person",
            "name": "Mallinath Beelur"
          },
          "publisher": {
            "@type": "Organization",
            "name": "Zuga Fitness",
            "logo": {
              "@type": "ImageObject",
              "url": "https://zugafitness.in/assets/images/zuga-logo.webp"
            }
          },
          "datePublished": "2026-10-23",
          "dateModified": "2026-10-23",
          "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": url_str
          }
        },
        {
          "@type": "FAQPage",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "Can I do yoga at my office desk without looking weird?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Seated cat-cow, neck rolls, and seated spinal twists are invisible to your coworkers but highly effective for reversing the damage of sitting for 8 hours."
              }
            },
            {
              "@type": "Question",
              "name": "How often should desk workers do yoga?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Frequency beats duration. Doing a 10-minute mobility reset every single workday is vastly superior to doing a 60-minute class once a week on Sunday."
              }
            },
            {
              "@type": "Question",
              "name": "Does yoga help with desk-job fatigue?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Desk fatigue is often shallow breathing and restricted blood flow from compressed hips. Opening the chest and hips restores oxygen flow and down-regulates the stress response."
              }
            }
          ]
        }
      ]
    }
    schema_script.string = json.dumps(schema_data, indent=2)

with open("Blog/yoga-for-desk-workers-bangalore-12-minute-routine.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Created Blog/yoga-for-desk-workers-bangalore-12-minute-routine.html")
