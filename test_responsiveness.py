# The user's prompt mentions "Ensure mobile responsiveness for all new pricing cards."
# Let's check `Online-Yoga-Classes.html` pricing cards we modified.

with open('Online-Yoga-Classes.html', 'r') as f:
    content = f.read()

# We used <div class="col-md-5 mb-4"> which stacks naturally on mobile. So that's already responsive.
# The breathwork section in Online-Pranayama-Classes.html also uses <div class="col-md-6 col-lg-5"> which stacks on mobile.
