import re

with open("corporate-wellness-bangalore.html", "r") as f:
    content = f.read()

# Add takeaways to existing H2s where missing.
# Let's target the known H2 sections.

# H2: Why Invest in Corporate Wellness?
if "Why Invest in Corporate Wellness?" in content and "<p><strong>Takeaway:</strong> Investing in corporate wellness" not in content:
    content = re.sub(
        r'(<h2 class="display-4 text-center mb-5">Why Invest in Corporate Wellness\?</h2>)',
        r'\1\n<p class="text-center mb-4"><strong>Takeaway:</strong> Investing in corporate wellness yields tangible returns by reducing absenteeism, boosting productivity, and improving employee retention.</p>',
        content
    )

# H2: Bring Yoga to Your Bangalore Office
if "Bring Yoga to Your Bangalore Office" in content and "<p><strong>Takeaway:</strong> Our certified" not in content:
    content = re.sub(
        r'(<p class="mb-5"[^>]*>We send certified yoga instructors directly to your Bangalore workplace — for regular team wellness sessions your employees will actually enjoy\.</p>)',
        r'\1\n        <p><strong>Takeaway:</strong> Our certified instructors deliver engaging wellness sessions directly to your Bangalore workplace.</p>',
        content
    )

# H2: Our Onsite Sessions in Action
if "Our Onsite Sessions in Action" in content and "<p><strong>Takeaway:</strong> See how" not in content:
    content = re.sub(
        r'(<h2 class="gallery-header">Our Onsite Sessions in Action</h2>)',
        r'\1\n<p class="text-center mb-4"><strong>Takeaway:</strong> See how our onsite sessions transform ordinary workspaces into vibrant wellness environments.</p>',
        content
    )

# H2: Simplified Corporate Pricing
if "Simplified Corporate Pricing" in content and "<p><strong>Takeaway:</strong> We offer" not in content:
    content = re.sub(
        r'(<p style="font-family: \'Poppins\', sans-serif; color: #666; font-weight: 400;">Hover over a card to experience the premium depth and inclusions\.</p>)',
        r'\1\n<p class="mt-2"><strong>Takeaway:</strong> We offer transparent, flat-rate pricing for premium corporate wellness sessions.</p>',
        content
    )

# H2: Meet Your Instructors
if "Meet Your Instructors" in content and "<p><strong>Takeaway:</strong> Learn from" not in content:
    content = re.sub(
        r'(<h2 class="display-4 text-center mb-5">Meet Your Instructors</h2>)',
        r'\1\n<p class="text-center mb-4"><strong>Takeaway:</strong> Learn from our highly experienced and certified wellness professionals.</p>',
        content
    )

# H2: What Our Corporate Clients Say
if "What Our Corporate Clients Say" in content and "<p><strong>Takeaway:</strong> Discover why" not in content:
    content = re.sub(
        r'(<h2 class="display-4 text-center mb-5">What Our Corporate Clients Say</h2>)',
        r'\1\n<p class="text-center mb-4"><strong>Takeaway:</strong> Discover why forward-thinking companies trust Zuga Fitness with their team\'s wellbeing.</p>',
        content
    )

# H2: Trusted by Forward-Thinking HR Leaders
if "Trusted by Forward-Thinking HR Leaders" in content and "<p><strong>Takeaway:</strong> Join the" not in content:
    content = re.sub(
        r'(<h2 class="display-4 text-center mb-5">Trusted by Forward-Thinking HR Leaders</h2>)',
        r'\1\n<p class="text-center mb-4"><strong>Takeaway:</strong> Join the growing list of HR leaders who prioritize employee wellness.</p>',
        content
    )

# H2: Book Your Weekday Slot (appears twice)
if "Book Your Weekday Slot" in content:
    content = re.sub(
        r'(<p class="mb-5 brand-sans">Fill out the form below and our team will get back to you within 24 hours to confirm your Corporate [^<]+ session\.</p>)',
        r'\1\n<p class="mb-4"><strong>Takeaway:</strong> Secure your preferred time slot easily by filling out our quick booking request form.</p>',
        content
    )

# H2: Common Questions (appears twice)
if "Common Questions" in content:
    content = re.sub(
        r'(<h2 class="display-4 text-center mb-5">Common Questions</h2>)',
        r'\1\n<p class="text-center mb-4"><strong>Takeaway:</strong> Find quick answers to the most frequently asked questions about our corporate programs.</p>',
        content
    )

# H2: Book Your Wellness Session Today (Final CTA)
if "Book Your Wellness Session Today" in content:
    content = re.sub(
        r'(<p class="lead mb-5 text-white brand-sans">Bangalore companies are booking fast for Corporate Wellness Programs\. Slots for peak corporate hours \(9 AM and 6 PM\) are filling up fast — don\'t miss out\.</p>)',
        r'\1\n<p class="text-white mb-4"><strong>Takeaway:</strong> Book now to secure premium wellness sessions during peak corporate hours.</p>',
        content
    )

# H2: Ready to bring wellness to your office? (Final CTA duplicated)
if "Ready to bring wellness to your office?" in content:
    content = re.sub(
        r'(<p class="lead mb-5 text-white brand-sans">Bangalore companies book sessions throughout the year — check availability for your team\.</p>)',
        r'\1\n<p class="text-white mb-4"><strong>Takeaway:</strong> Check our availability today and transform your workplace wellness.</p>',
        content
    )

# H2: Corporate Wellness Services Across Bangalore
if "Corporate Wellness Services Across Bangalore" in content:
    content = re.sub(
        r'(<p class="lead text-center mb-5">We serve companies across all major business districts in Bangalore:</p>)',
        r'\1\n<p class="text-center mb-4"><strong>Takeaway:</strong> We provide comprehensive wellness services directly to offices across all major districts in Bangalore.</p>',
        content
    )


with open("corporate-wellness-bangalore.html", "w") as f:
    f.write(content)
