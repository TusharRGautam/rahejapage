import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ul_start = html.rfind('<div class="', 0, html.rfind('<ul class="nav d-flex'))
end = html.find('</div>', html.rfind('</ul>')) + 6
bar_html = html[ul_start:end]
print('Found bar_html:', bar_html[:100])

files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']
for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'margin-bottom: 6px; flex-wrap: nowrap;' not in content:
        content = content.replace('<!-- Chatbot -->', bar_html + '\n\n<!-- Chatbot -->', 1)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Added bar to {file_name}')
