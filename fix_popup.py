import re

pages = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the chat-pop-sm div that appears in body (old popup, not needed)
    # It appears right after </head><body>
    content = re.sub(
        r'<div class="chat-pop-sm">.*?</div>\s*<!-- Small Chatbot -->',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Removed chat-pop-sm from {page}')
    print(f'  Pooja remaining: {content.count("Pooja")}')
    print(f'  chat-pop-sm remaining: {content.count("chat-pop-sm")}')
