import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<div[^>]*class=\"[^\"]*fixed-bottom[^\"]*\".*?(?=<!-- Chatbot -->)', html, re.DOTALL)
if match:
    bar_html = match.group(0).strip()
    
    files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']
    for file_name in files:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'fixed-bottom' not in content:
            content = content.replace('<!-- Chatbot -->', bar_html + '\n<!-- Chatbot -->', 1)
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Added fixed-bottom bar to {file_name}')
else:
    print('Failed to find fixed-bottom bar in index.html')
