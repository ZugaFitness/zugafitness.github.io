import glob
import re

def main():
    modified = 0
    for filepath in glob.glob("**/*.html", recursive=True):
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()

        original = html

        # Phone numbers: use word boundaries for the ones with spaces, and lookarounds for numbers that might be in an SVG viewbox or path, but wait, SVGs have coordinates like 16.9706...
        # so \b9706\b or similar should not match decimal points directly before.
        # Let's be very safe.
        html = re.sub(r'(?<![\d\.])9706 20 12 20(?![\d\.])', '+91 76763 79909', html)
        html = re.sub(r'(?<![\d\.])9706 21 21 16(?![\d\.])', '+91 76763 79909', html)
        html = re.sub(r'\+91 98765 43210', '+91 76763 79909', html)
        html = re.sub(r'\+91 9876543210', '+91 76763 79909', html)
        html = re.sub(r'\+91 70222 07304', '+91 76763 79909', html)
        html = re.sub(r'\+91 76763 79099', '+91 76763 79909', html)

        # Clean URLs if they had spaces stripped
        html = re.sub(r'tel:\+?919706201220', 'tel:+917676379909', html)
        html = re.sub(r'tel:\+?919706212116', 'tel:+917676379909', html)
        html = re.sub(r'wa\.me/919706201220', 'wa.me/917676379909', html)
        html = re.sub(r'wa\.me/919706212116', 'wa.me/917676379909', html)

        # Gmail
        html = re.sub(r'[a-zA-Z0-9_.+-]+@gmail\.com', 'hello@zugafitness.in', html)

        # Anusha's hours.
        # Specifically target the Anusha's profile cards or blocks.
        # Usually these blocks contain Anusha's name and her 1.5k+ hours.
        # Let's replace ONLY if the string is close to "Anusha" or "Dance", OR if it is Anusha-Portfolio or Online-Dance-Fitness-Classes.
        def replacer(match):
            m = match.group(0)
            context_start = max(0, match.start() - 600)
            context_end = min(len(html), match.end() + 600)
            context = html[context_start:context_end].lower()

            # If mallinath is prominently closer or if it's mallinath's file, preserve it!
            if filepath == "Mallinath-Portfolio.html":
                return m

            # Anusha context
            if 'anusha' in context or 'zumba' in context or 'dance' in context or filepath == "Anusha-Portfolio.html":
                # Ensure we don't accidentally replace Mallinath's explicitly, if both are mentioned.
                # Since Mallinath's is 1,500+ and Anusha's is 1.5k+ or 1500+ generally, wait...
                # The instructions say: Anusha hours "1.5k+"/"1500+"/"1,500+" -> "500+" in Anusha/dance contexts.
                # So we replace.
                return "500+"
            return m

        hours_variants = [r"1\.5k\+", r"1500\+", r"1,500\+"]
        for h in hours_variants:
            html = re.sub(h, replacer, html)

        if html != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            modified += 1
            print(f"Normalized {filepath}")

if __name__ == "__main__":
    main()
