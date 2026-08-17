import re

with open('Online-Yoga-Classes.html', 'r') as f:
    content = f.read()

# Fix the duplicate </div> issue created in the last step
content = content.replace('      </div></div>\n    </div>\n  </div>\n</section>', '      </div>\n    </div>\n  </div>\n</section>')

with open('Online-Yoga-Classes.html', 'w') as f:
    f.write(content)
