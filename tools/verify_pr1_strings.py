import glob
import re

def verify():
    phones = [r"(?<![\d\.])9706 20 12 20(?![\d\.])", r"(?<![\d\.])9706 21 21 16(?![\d\.])", r"\+91 98765 43210", r"\+91 9876543210", r"\+91 70222 07304", r"\+91 76763 79099"]
    gmail = r'[a-zA-Z0-9_.+-]+@gmail\.com'
    hours = [r"1\.5k\+", r"1500\+", r"1,500\+"]

    issues = 0
    for filepath in glob.glob("**/*.html", recursive=True):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        for p in phones:
            if re.search(p, content):
                print(f"Found {p} in {filepath}")
                issues += 1
        if re.search(gmail, content):
            print(f"Found gmail in {filepath}")
            issues += 1

        # For hours, we only care if it's in Anusha contexts
        # We can loosely check if Anusha/zumba/dance is in file and 1.5k+ is there,
        # but actually, if it's Anusha-Portfolio and has 1.5k+, it's an issue.
        if "Anusha-Portfolio" in filepath or "Dance" in filepath:
            for h in hours:
                if re.search(h, content):
                    print(f"Found {h} in {filepath}")
                    issues += 1

    if issues == 0:
        print("PASS: Zero occurrences of un-normalized strings found.")
    else:
        print(f"FAIL: {issues} un-normalized strings found.")

if __name__ == "__main__":
    verify()
