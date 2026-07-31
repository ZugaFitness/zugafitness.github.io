import re

with open("corporate-wellness-bangalore.html", "r") as f:
    content = f.read()

# The image shows some layout issues. It looks like the programs and form didn't render correctly within the grid/container, or some CSS from Mobirise broke.
# Let's check how the new programs block was inserted.
# Ah, I replaced the whole section with a new section, but it seems there was an unclosed div or missing col- class that caused layout breaking.

programs_broken = """<section class="zuga-section" id="programs" style="background: var(--brand-bg);">
<div class="container">
<h2 class="display-4 text-center mb-5">Our Year-Round Corporate Wellness Programs</h2>

<div class="row mb-5">
  <div class="col-12">
    <h2 class="display-5 mb-3" style="font-family: 'Playfair Display', serif;">Corporate Yoga: Stress Relief &amp; Posture Correction</h2>
    <p class="brand-sans" style="font-size: 1.1rem; color: var(--brand-text);">Our corporate yoga sessions are designed to counteract the negative effects of prolonged sitting and high-stress environments. We focus on mindfulness techniques to calm the nervous system and targeted stretches for desk-posture relief, including neck, shoulder, and lower back release.</p>
    <p><strong>Takeaway:</strong> Corporate yoga provides essential stress relief and posture correction to help employees stay focused and physically comfortable at their desks.</p>
  </div>
</div>

<div class="row mb-5">
  <div class="col-12">
    <h2 class="display-5 mb-3" style="font-family: 'Playfair Display', serif;">Corporate Zumba: High-Energy Team Building</h2>
    <p class="brand-sans" style="font-size: 1.1rem; color: var(--brand-text);">Inject fun and vitality into your workplace with our high-energy corporate Zumba sessions. It's an excellent cardiovascular workout that breaks the ice, encourages group bonding, and leaves your team feeling energized and motivated.</p>
    <p><strong>Takeaway:</strong> Corporate Zumba is a fun, high-energy cardio workout that doubles as an effective team-building activity.</p>
  </div>
</div>

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
</div>
</section>"""

# Checking what was actually replaced. Maybe the regex replaced too much or too little?
