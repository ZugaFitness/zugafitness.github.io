import os

filepath = 'Online-Pranayama-Classes.html'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # The original instructions said: "1-on-1 Pranayama PT: ₹3,499 (Foundation) / ₹4,999 (Transformation)"
    # We should make sure these values are correct in the HTML if they are mentioned.
    pass
