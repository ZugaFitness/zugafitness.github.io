import re

with open('docs/US_Page_Audit_Report.md', 'r') as f:
    content = f.read()

# Add a third competitor for the second query
new_competitor = """
3. **My Vinyasa Practice**
   - **Title Tag:** 1-On-1 Yoga Training | My Vinyasa Practice
   - **Meta Description:** Connect with our Lead Trainers to support your continuing education online. Schedule 1-on-1 yoga training sessions to expand your practice...
   - **Why they are outranking us:** They position their offering slightly differently by focusing on "continuing education" and "Lead Trainers", appealing to a specific niche of practitioners seeking deeper engagement.
"""

# Find the section and append the new competitor
content = content.replace("matching the intent.\n\n\n## 3. Action Plan", "matching the intent.\n" + new_competitor + "\n\n## 3. Action Plan")

with open('docs/US_Page_Audit_Report.md', 'w') as f:
    f.write(content)
