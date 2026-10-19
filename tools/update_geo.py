import re

def update_geo(filepath, new_title, new_meta):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    html = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', html, flags=re.DOTALL)
    html = re.sub(r'<meta property="og:title" content="[^>]+>', f'<meta property="og:title" content="{new_title}">', html)
    html = re.sub(r'<meta name="twitter:title" content="[^>]+>', f'<meta name="twitter:title" content="{new_title}">', html)

    html = re.sub(r'<meta name="description" content="[^>]+>', f'<meta name="description" content="{new_meta}">', html)
    html = re.sub(r'<meta property="og:description" content="[^>]+>', f'<meta property="og:description" content="{new_meta}">', html)
    html = re.sub(r'<meta name="twitter:description" content="[^>]+>', f'<meta name="twitter:description" content="{new_meta}">', html)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

update_geo('usa-online-yoga-classes.html', 'Live Online Yoga for US Timezones (EST/PST) | Zuga Fitness', 'Skip the 3 AM YouTube videos. Join live, interactive yoga and dance fitness classes timed perfectly for US mornings and evenings. Real instructors, real corrections.')
update_geo('canada-online-yoga-classes.html', 'Live Online Yoga Classes in Canada (EST/PST) | Zuga Fitness', 'Live, interactive yoga and Zumba classes scheduled for Canadian timezones. Build strength, mobility and stress relief with real-time coaching from certified instructors.')
update_geo('uae-online-yoga-classes.html', 'Online Yoga & Zumba Classes in Dubai & UAE | Zuga Fitness', 'Premium live online yoga and dance fitness for the UAE. Flexible scheduling for Dubai and Abu Dhabi professionals looking to reverse desk-posture and manage stress.')
update_geo('australia-online-yoga-classes.html', 'Live Online Yoga in Australia (Sydney/Melb Time) | Zuga Fitness', 'Live yoga and Zumba classes scheduled for AEST/AEDT. Join certified instructors for morning flows and evening dance cardio, broadcast live from India to your living room.')
update_geo('uk-online-yoga-classes.html', 'Live Online Yoga Classes in the UK (GMT/BST) | Zuga Fitness', 'Interactive online yoga and dance fitness timed for UK mornings and evenings. Get real-time posture corrections and nervous system regulation from certified instructors.')
update_geo('germany-online-yoga-classes.html', 'Live Online Yoga Classes in Germany (CET) | Zuga Fitness', 'Live, interactive yoga and Zumba classes scheduled for Central European Time. Build mobility and burn calories with real-time coaching from certified instructors.')
