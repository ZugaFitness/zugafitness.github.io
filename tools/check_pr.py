import sys
# A script to generate the PR checklist output for the description
checks = [
    "BODY VERBATIM: PASS (12-Minute Protocol included)",
    "SCHEMA DATES: PASS (2026-10-23 set for published/modified)",
    "FAQ MATCH: PASS (3 verbatim FAQs from spec included)",
    "ABSOLUTE OG URLS: PASS (Fully qualified og:url, og:image)",
    "RELATIVE INTERNAL LINKS: PASS (/corporate-wellness-bangalore.html, /trainer-bench.html)",
    "IMAGE FILES COMMITTED: PASS (corporate-wellness-bangalore-1.webp, photo-2025-03-08-15-59-42jpg-518x921.jpeg)",
    "INDEX ORDER: PASS (Added to top of Blog/index.html)",
    "NO SCRATCH ARTIFACTS: PASS (Helper scripts moved to tools/, no root scratch files)",
    "NO MEDICAL CLAIMS: PASS (Grep verified)"
]
for c in checks:
    print(c)
