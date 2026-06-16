import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<ul class=\"nav nav-fill og-block mobile-bottom-bar.*?</ul>', html, re.DOTALL)
if match:
    bar_html = match.group(0)
    
    files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']
    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # If it's already there, skip
        if 'mobile-bottom-bar' not in content:
            content = content.replace('<!-- Chatbot -->', bar_html + '\n<!-- Chatbot -->', 1)
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Added mobile-bottom-bar to {file_name}')
else:
    print('Failed to find mobile-bottom-bar in index.html')
