import re

pricing_and_form_html = """
<div class="row mb-5 justify-content-center">
  <div class="col-lg-8">
    <div style="background: var(--brand-white); border-radius: 20px; padding: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); border-top: 5px solid var(--brand-teal);">
      <h3 class="display-5 mb-4 text-center" style="font-family: 'Playfair Display', serif;">Transparent B2B Pricing</h3>
      <p class="brand-sans text-center mb-5" style="font-size: 1.1rem; color: var(--brand-text);">We believe in making employee wellness straightforward and budget-friendly. Book a certified Zuga Fitness instructor for your office for a flat rate of <strong>₹5,000 per event/session</strong>. No complicated per-headcount math—just premium wellness for your entire team.</p>

      <div class="b2b-form-container" style="background: var(--brand-bg); padding: 30px; border-radius: 12px;">
        <h3 class="mb-4 text-center" style="font-family: 'Playfair Display', serif;">Book Your Corporate Wellness Session</h3>
        <form action="#" method="POST" class="d-flex flex-column gap-3">
          <input type="text" name="hr_name" placeholder="Your Name (HR / Admin)" required class="form-control p-3" />
          <input type="text" name="company_name" placeholder="Company Name" required class="form-control p-3" />
          <input type="email" name="company_email" placeholder="Official Company Email" required class="form-control p-3" />
          <input type="tel" name="phone" placeholder="Phone Number" required class="form-control p-3" />
          <select name="service_interest" required class="form-control p-3">
            <option value="" disabled selected>Select a Service</option>
            <option value="yoga">Corporate Yoga (Stress Relief)</option>
            <option value="zumba">Corporate Zumba (High Energy)</option>
            <option value="both">Custom Hybrid Package</option>
          </select>
          <button type="submit" class="btn btn-brand-cta w-100 mt-3" style="font-weight: bold; background-color: var(--brand-orange) !important; color: white !important;">Request Callback & Book Event</button>
        </form>
      </div>
    </div>
  </div>
</div>
"""

def add_pricing_form_to_html(content):
    # Insert it immediately after the new Zumba section (before the closing div/section of #programs)
    return re.sub(
        r'(<p><strong>Takeaway:</strong> Corporate Zumba is a fun, high-energy cardio workout that doubles as an effective team-building activity\.</p>\n  </div>\n</div>)',
        r'\1\n' + pricing_and_form_html,
        content
    )

def main():
    with open("corporate-wellness-bangalore.html", "r") as f:
        content = f.read()

    content = add_pricing_form_to_html(content)

    with open("corporate-wellness-bangalore.html", "w") as f:
        f.write(content)

if __name__ == "__main__":
    main()
