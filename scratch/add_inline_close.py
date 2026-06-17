import re

css_to_replace = '''    #chat-close {
        top: 15px !important;
        right: 15px !important;
        bottom: auto !important;
        z-index: 10001 !important;
    }'''

css_new = '''    #chat-close {
        display: none !important;
    }'''

html_to_replace = '''<div class="chat-header-name">Shreya Shetty </div>'''
html_new = '''<div class="chat-header-name">Shreya Shetty </div>
        <span class="chat-header-close" onclick="$('#chat-close').click()" style="position: absolute; right: 15px; top: 12px; font-size: 28px; cursor: pointer; color: white; line-height: 1; z-index: 100000;">&times;</span>'''

files = ['index.html', 'terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace CSS
    if css_to_replace in content:
        content = content.replace(css_to_replace, css_new)
        
    # Replace HTML
    if html_to_replace in content:
        content = content.replace(html_to_replace, html_new)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print('Updated', f)
