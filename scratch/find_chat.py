with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'<div id="chat-close.*?</div>\s*</div>', html, re.DOTALL)
if match:
    print('chat-close:', match.group(0))
