import re

with open("weight-loss-challenge.html", "r") as f:
    html = f.read()

# Extract original form action ID
original_form_action = re.search(r'action="(https://formspree.io/f/[a-zA-Z0-9]+)"', html)
form_action_url = "https://formspree.io/f/mnnakbyz" # fallback
if original_form_action:
    form_action_url = original_form_action.group(1)

# Replace the title and add schema
html = re.sub(
    r'<title>.*?</title>',
    '<title>Best Online 90-Day Weight Loss Challenge | Zuga Fitness</title>',
    html,
    flags=re.IGNORECASE
)

# Insert the JSON-LD schema
schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "The 90-Day Post-Diwali Reset",
      "description": "Join our exclusive 5-day-a-week live cohort starting November 1st. 90 Days. 3 Timezone Batches. 1 Goal.",
      "provider": {
        "@type": "Organization",
        "name": "Zuga Fitness",
        "sameAs": "https://zugafitness.in/"
      },
      "hasCourseInstance": {
        "@type": "CourseInstance",
        "courseMode": "online",
        "courseWorkload": "PT5H"
      },
      "offers": {
        "@type": "Offer",
        "category": "Paid",
        "priceCurrency": "INR",
        "price": "12000",
        "priceValidUntil": "2026-11-01",
        "availability": "https://schema.org/LimitedAvailability"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Is this a pre-recorded course?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. This is a live, instructor-led transformation. All sessions are conducted live over Zoom."
          }
        },
        {
          "@type": "Question",
          "name": "What if I miss a live session?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Every session is recorded and uploaded to your private Member Vault within 24 hours."
          }
        }
      ]
    }
  ]
}
</script>
"""

# Replace all existing json-ld blocks with the new one
html = re.sub(r'<script type="application/ld\+json">.*?</script>', '', html, flags=re.DOTALL)
html = html.replace("</head>", schema + "\n</head>")


new_content = """
<!-- HERO SECTION -->
<section style="padding: 120px 20px 80px; background: var(--light-brand); text-align: center;">
    <div class="container" style="max-width: 800px; margin: 0 auto;">
        <h1 style="font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 700; color: var(--primary-brand); margin-bottom: 20px;">The 90-Day Post-Diwali Reset.</h1>
        <p style="font-size: 1.2rem; margin-bottom: 30px; font-weight: 500;">90 Days. 3 Timezone Batches. 1 Goal.<br>Join our exclusive 5-day-a-week live cohort starting November 1st.</p>
        <a href="#reservation-form" style="background: var(--gradient-brand); color: var(--white); padding: 15px 30px; border-radius: 30px; text-decoration: none; font-weight: 600; font-size: 1.1rem; box-shadow: var(--shadow-md); display: inline-block;">Reserve My Spot (Only 30 Seats)</a>
    </div>
</section>

<!-- THE PROBLEM & THE PROMISE -->
<section style="padding: 80px 20px; background: var(--white);">
    <div class="container" style="max-width: 800px; margin: 0 auto; text-align: center;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 600; color: var(--dark-brand); margin-bottom: 20px;">The Festival Hangover Ends Here.</h2>
        <p style="font-size: 1.1rem; line-height: 1.8;">Diwali means celebration, but the weeks after usually mean lethargy, bloating, and abandoned routines. We built the 90-Day Post-Diwali Reset to flip that script. This isn't a pre-recorded video library. This is a live, instructor-led transformation.</p>
    </div>
</section>

<!-- THE BLUEPRINT -->
<section style="padding: 80px 20px; background: var(--light-brand);">
    <div class="container" style="max-width: 800px; margin: 0 auto;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 600; color: var(--dark-brand); margin-bottom: 20px; text-align: center;">Your Weekly Training Blueprint</h2>
        <p style="font-size: 1.1rem; line-height: 1.8; text-align: center; margin-bottom: 30px;">Weight loss requires burning calories today and building muscle for tomorrow. Your 5-day live schedule:</p>
        <ul style="list-style: none; padding: 0; font-size: 1.1rem; line-height: 1.8;">
            <li style="margin-bottom: 10px;"><strong>Mon & Wed:</strong> Dance Fitness (High-Energy Cardio Burn)</li>
            <li style="margin-bottom: 10px;"><strong>Tue & Thu:</strong> Strength & Conditioning (Muscle Build & Metabolism)</li>
            <li style="margin-bottom: 10px;"><strong>Fri:</strong> Yoga & Mobility (Active Recovery & Joint Health)</li>
            <li style="margin-bottom: 10px;"><strong>Sat & Sun:</strong> Rest & Integration</li>
        </ul>
    </div>
</section>

<!-- THE COHORT MODEL -->
<section style="padding: 80px 20px; background: var(--white);">
    <div class="container" style="max-width: 800px; margin: 0 auto;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 600; color: var(--dark-brand); margin-bottom: 20px; text-align: center;">Small Batches. Global Timezones.</h2>
        <p style="font-size: 1.1rem; line-height: 1.8; text-align: center; margin-bottom: 30px;">We cap this challenge at exactly 30 members to ensure you get real-time form corrections. Choose the batch that fits your life:</p>
        <ul style="list-style: none; padding: 0; font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px;">
            <li style="margin-bottom: 10px;"><strong>Batch 1:</strong> UK & Europe (Timed for your evenings)</li>
            <li style="margin-bottom: 10px;"><strong>Batch 2:</strong> US & Canada (Timed for your mornings/evenings)</li>
            <li style="margin-bottom: 10px;"><strong>Batch 3:</strong> India, Aus & Gulf (Flexible evening slots)</li>
        </ul>
        <p style="font-size: 0.95rem; font-style: italic; text-align: center; color: #666;">*Note: Can't make a live session? Every session is recorded and uploaded to your private Member Vault within 24 hours.*</p>
    </div>
</section>

<!-- THE INVESTMENT & SCARCITY -->
<section style="padding: 80px 20px; background: var(--light-brand); text-align: center;">
    <div class="container" style="max-width: 800px; margin: 0 auto;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 600; color: var(--dark-brand); margin-bottom: 20px;">Secure Your Transformation</h2>
        <div style="margin-bottom: 20px;">
            <span style="font-size: 1.5rem; text-decoration: line-through; color: #888; margin-right: 15px;">₹15,000</span>
            <span style="font-size: 3rem; font-weight: 700; color: var(--primary-brand);">₹12,000</span>
        </div>
        <p style="font-size: 0.95rem; color: #666; margin-bottom: 20px;">(Approx. $145 USD for international members)</p>
        <p style="font-size: 1.1rem; font-weight: 600; color: #D32F2F;">Strictly limited to 10 members per batch. Once the 30 spots are filled, enrollment closes until 2027.</p>
    </div>
</section>

<!-- THE RESERVATION FORM -->
<section id="reservation-form" style="padding: 80px 20px; background: var(--white);">
    <div class="container" style="max-width: 600px; margin: 0 auto;">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 600; color: var(--dark-brand); margin-bottom: 30px; text-align: center;">Reserve Your Spot</h2>

        <form id="wlc-form" action="FORM_ACTION_URL_PLACEHOLDER" method="POST" style="background: var(--light-brand); padding: 40px; border-radius: 12px; box-shadow: var(--shadow-sm);">
            <input type="hidden" name="_next" value="https://zugafitness.in/wlc-thank-you.html">
            <input type="hidden" name="_subject" value="New 90-Day WLC Reservation!">

            <div style="margin-bottom: 20px;">
                <label for="name" style="display: block; font-weight: 500; margin-bottom: 8px;">Full Name *</label>
                <input type="text" id="name" name="name" required style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Poppins', sans-serif;">
            </div>

            <div style="margin-bottom: 20px;">
                <label for="phone" style="display: block; font-weight: 500; margin-bottom: 8px;">WhatsApp Number (with Country Code) *</label>
                <input type="tel" id="phone" name="phone" required style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Poppins', sans-serif;" placeholder="+91...">
            </div>

            <div style="margin-bottom: 20px;">
                <label for="email" style="display: block; font-weight: 500; margin-bottom: 8px;">Email Address *</label>
                <input type="email" id="email" name="email" required style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Poppins', sans-serif;">
            </div>

            <div style="margin-bottom: 20px;">
                <label for="batch" style="display: block; font-weight: 500; margin-bottom: 8px;">Preferred Batch / Timezone *</label>
                <select id="batch" name="batch" required style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Poppins', sans-serif;">
                    <option value="" disabled selected>Select a batch</option>
                    <option value="UK_EU">Batch 1: UK & Europe</option>
                    <option value="US_CA">Batch 2: US & Canada</option>
                    <option value="IN_AU_Gulf">Batch 3: India, Aus & Gulf</option>
                </select>
            </div>

            <div style="margin-bottom: 30px;">
                <label for="goal" style="display: block; font-weight: 500; margin-bottom: 8px;">What is your primary goal for the next 90 days?</label>
                <textarea id="goal" name="goal" rows="4" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-family: 'Poppins', sans-serif; resize: vertical;"></textarea>
            </div>

            <button type="submit" id="wlc-submit-btn" style="width: 100%; background: var(--gradient-brand); color: var(--white); padding: 15px; border: none; border-radius: 6px; font-weight: 600; font-size: 1.1rem; cursor: pointer; transition: opacity 0.3s;">Submit Reservation & Get Payment Details</button>
            <p id="wlc-form-status" style="display: none; margin-top: 15px; text-align: center; font-weight: 500; color: #D32F2F;"></p>
        </form>
    </div>
</section>

<script>
document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("wlc-form");
    var status = document.getElementById("wlc-form-status");
    var submitBtn = document.getElementById("wlc-submit-btn");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        var batchSelect = document.getElementById("batch");
        var selectedBatch = batchSelect.options[batchSelect.selectedIndex].value;

        // Fire GA4 Event if gtag is available
        if (typeof gtag === 'function') {
            gtag('event', 'wlc_reservation', {
                'batch': selectedBatch
            });
        }

        var data = new FormData(event.target);
        submitBtn.disabled = true;
        submitBtn.style.opacity = 0.7;
        submitBtn.innerText = "Submitting...";

        fetch(event.target.action, {
            method: form.method,
            body: data,
            headers: {
                'Accept': 'application/json'
            }
        }).then(response => {
            if (response.ok) {
                window.location.href = "/wlc-thank-you.html";
            } else {
                response.json().then(data => {
                    if (Object.hasOwn(data, 'errors')) {
                        status.innerHTML = data["errors"].map(error => error["message"]).join(", ");
                    } else {
                        status.innerHTML = "Oops! There was a problem submitting your form. Please try again.";
                    }
                    status.style.display = "block";
                    submitBtn.disabled = false;
                    submitBtn.style.opacity = 1;
                    submitBtn.innerText = "Submit Reservation & Get Payment Details";
                })
            }
        }).catch(error => {
            // Graceful fallback if JS fetch fails: we will manually submit via standard form submission
            console.error("Fetch failed, falling back to standard submit.", error);
            form.submit();
        });
    });
});
</script>
"""
new_content = new_content.replace("FORM_ACTION_URL_PLACEHOLDER", form_action_url)

import re

menu_end_match = re.search(r'</nav>\s*</section>', html)
if not menu_end_match:
    print("Could not find the end of the menu")
else:
    menu_end_idx = menu_end_match.end()

    footer_start_match = re.search(r'<section[^>]*class="[^"]*footer[^"]*"', html)
    if not footer_start_match:
        print("Could not find the start of the footer")
    else:
        footer_start_idx = footer_start_match.start()

        new_html = html[:menu_end_idx] + "\n" + new_content + "\n" + html[footer_start_idx:]

        with open("weight-loss-challenge.html", "w") as f:
            f.write(new_html)
        print("Successfully updated weight-loss-challenge.html")
