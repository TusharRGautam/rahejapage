import os, re

files=['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove chat script
    content = re.sub(r'<script src="\./assets/js/commercialchatv25\.js" defer ></script>', '', content)
    
    # Remove chatbotApiInput
    content = re.sub(r'<script type="text/javascript">\s*var chatbotApiInput = \{.*?\};\s*var timer = 0;\s*</script>', '', content, flags=re.DOTALL)
    
    # Remove exit intent and scroll popup
    content = re.sub(r'<script>\s*var c, a = window\.location\.pathname,.*?\}\s*\}\s*\);\s*\}\s*</script>', '', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Processed {f}')
