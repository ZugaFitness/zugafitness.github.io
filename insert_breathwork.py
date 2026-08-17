import re

with open('Online-Pranayama-Classes.html', 'r') as f:
    content = f.read()

# We need to inject a new "Group Breathwork" section immediately AFTER the "Why 30 Minutes?" section
# and BEFORE the "1-on-1 Protocol Tracks" section.

# Looking at the earlier grep:
#    </div>
#
#    <!-- Protocol Tracks -->
#    <div class="row text-center mb-4">
#      <div class="col-12">
#        <h2 style="color: #333; font-weight: bold;">Choose Your Nervous System Protocol Track</h2>

target_text = '<!-- Protocol Tracks -->'

new_section = """<section id="group-breathwork" style="padding: 40px 0; background-color: #ffffff; border-bottom: 1px solid #e0e0e0;">
  <div class="container">
    <div class="row text-center mb-4">
      <div class="col-lg-8 mx-auto">
        <h2 style="color: #333; font-weight: bold;">Foundational Group Breathwork Sessions</h2>
        <p style="color: #555; line-height: 1.8;">New to breathwork? Start with our live, instructor-led group sessions. Build a consistent daily habit, learn foundational techniques like Nadi Shodhana and Bhramari, and experience the power of collective nervous system regulation.</p>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-md-6 col-lg-5">
        <div class="card text-center" style="border: 2px solid #E8690A; border-radius: 10px; padding: 30px;">
          <h4 style="color: #333; margin-bottom: 10px;">Community Breathwork</h4>
          <h2 style="color: #E8690A; font-weight: bold; margin: 15px 0;">₹1,499<span style="font-size: 16px; color: #666;">/mo</span></h2>
          <p style="color: #666; font-size: 14px; margin-bottom: 20px;">(Just ₹70 per session)</p>
          <ul style="text-align: left; color: #555; line-height: 1.8; list-style: none; padding-left: 0;">
            <li>✔ Live Group Sessions (30 mins)</li>
            <li>✔ Foundational Breathwork Techniques</li>
            <li>✔ Global Community & Accountability</li>
            <li>✔ Perfect for beginners & daily practice</li>
          </ul>
          <a href="#pt-application" class="btn btn-primary" style="background-color: #E8690A; border: none; width: 100%; padding: 12px; font-weight: bold;">Join Group Sessions</a>
        </div>
      </div>
    </div>
    <div class="row text-center mt-4">
      <div class="col-lg-8 mx-auto">
        <p style="color: #555; font-style: italic;">Looking for advanced CO2 tolerance training and personalized nervous system protocols? <a href="#pranayama-pt" style="color: #E8690A; font-weight: bold;">Explore our 1-on-1 Clinical Tracks below.</a></p>
      </div>
    </div>
  </div>
</section>

"""

if target_text in content:
    content = content.replace(target_text, new_section + target_text)

with open('Online-Pranayama-Classes.html', 'w') as f:
    f.write(content)

print("Injected Group Breathwork successfully.")
