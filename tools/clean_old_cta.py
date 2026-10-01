import re

with open("Anusha-Portfolio.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to remove this orphaned block without killing the rest of the page:
# </script>
# <p class="text-center text-gray-500 text-sm mt-2 md:hidden">← Swipe to see more →</p>
# ...
# </section>
# <section class="py-8 bg-gray-50"> ... (Actually that was replaced by Bio)
# We need to carefully remove the chunk that follows </script> of the hero, up to <section class="py-20 bg-[#f8f5f0]"
pattern = re.compile(r'(</script>).*?(<section class="py-20 bg-\[#f8f5f0\])', re.DOTALL)
html = pattern.sub(r'\1\n\2', html)

with open("Anusha-Portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
