import re

with open('Online-Yoga-Classes.html', 'r') as f:
    content = f.read()

# We need to replace the entire row of pricing cards.
# Find the start of the row inside the pricing section.
section_start = content.find('<!-- SECTION 8 — PRICING -->')
if section_start != -1:
    row_start = content.find('<div class="row">', section_start)
    row_end = content.find('</div>\n    </div>\n  </div>\n</section>', row_start)

    if row_start != -1 and row_end != -1:
        new_row = """<div class="row justify-content-center">
      <!-- Starter Yoga -->
      <div class="col-md-5 mb-4">
        <div class="pricing-card" style="height: 100%;">
          <h3 class="display-5">Group Yoga</h3>
          <div class="price-value">₹1,999<small class="text-muted" style="font-size: 1rem;">/month</small></div>
          <ul class="display-7 mb-4" style="list-style: none; padding: 0; line-height: 1.8;">
            <li>✅ 20 live classes/mo</li>
            <li>✅ 1 timezone slot</li>
            <li>✅ Hatha, Vinyasa or Meditation</li>
            <li>✅ Community WhatsApp group</li>
          </ul>
          <div class="mt-auto">
            <a href="https://zugafitness.in/free-trial.html" class="btn btn-orange display-4 w-100">Free Trial →</a>
          </div>
        </div>
      </div>
      <!-- Private -->
      <div class="col-md-5 mb-4">
        <div class="pricing-card" style="border: 2px solid var(--teal); height: 100%;">
          <h3 class="display-5">1-on-1 Private Yoga</h3>
          <div class="price-value">₹7,999<small class="text-muted" style="font-size: 1rem;">/month</small></div>
          <ul class="display-7 mb-4" style="list-style: none; padding: 0; line-height: 1.8;">
            <li>✅ Premium Tier A: 3 sessions/week</li>
            <li>✅ Elite Tier B: ₹9,999/mo (5 sessions/week)</li>
            <li>✅ Tailored specifically to your body & goals</li>
            <li>✅ Your preferred time slot</li>
          </ul>
          <div class="mt-auto">
            <a href="/Online-Personal-Training-classes.html#pt-application" class="btn btn-teal display-4 w-100">Apply for PT →</a>
          </div>
        </div>
      </div>"""

        content = content[:row_start] + new_row + content[row_end:]

with open('Online-Yoga-Classes.html', 'w') as f:
    f.write(content)

print("Yoga pricing cards updated successfully.")
