import re

pages = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix Pooja Agarwal in small chatbot popup
    content = content.replace('"Hey, I\'m Pooja Agarwal!" <strong>How can I help you?</strong>', 
                              '"Hey, I\'m Shreya Shetty!" <strong>How can I help you?</strong>')
    content = content.replace("Hey, I'm Pooja Agarwal!", "Hey, I'm Shreya Shetty!")
    content = content.replace('Pooja Agarwal', 'Shreya Shetty')
    
    # 2. Remove the DUPLICATE chatbot block (the old one that appears right after </head><body>)
    # The structure is: </head><body>...<div class="chat-pop-sm">...<!-- Small Chatbot --><!-- Chatbot -->...<!-- Chatbot --> 
    # We want to keep only one chatbot block (the first one in <head>) and remove the duplicate in <body>
    # Remove duplicate chat-square, chat-close divs and chat-wrapper in body (after <!-- Small Chatbot -->)
    
    # Remove the old chatbot block that comes right after <!-- Small Chatbot -->
    old_dup_pattern = r'<!-- Chatbot -->\s*<div id="chat-square" class="btn"></div>\s*<div id="chat-close" class="btn chat-box-toggle">\s*<div class="close-img"></div>\s*</div>\s*<div class="chat-wrapper">.*?</div>\s*</div>\s*</div>\s*<!-- Chatbot -->\s*\n'
    
    # Find all <!-- Chatbot --> blocks and check how many
    chatbot_blocks = list(re.finditer(r'<!-- Chatbot -->(.*?)<!-- Chatbot -->', content, re.DOTALL))
    print(f'{page}: Found {len(chatbot_blocks)} chatbot blocks')
    
    # If there are 2 chatbot blocks, remove the second one  
    if len(chatbot_blocks) == 2:
        second_block = chatbot_blocks[1]
        content = content[:second_block.start()] + content[second_block.end():]
        print(f'  -> Removed duplicate chatbot block')
    
    # 3. Add proper padding to main content area for policy pages
    # The <main class="pload"> section needs top padding since header is fixed
    content = content.replace('<main class="pload">', '<main class="pload" style="padding-top: 70px;">')
    
    # 4. Make the content section responsive
    content = content.replace('<section class="section shadow-sm lazyload" id="developer">', 
                              '<section class="section shadow-sm lazyload" id="developer" style="padding: 20px 15px; max-width: 1000px; margin: 0 auto;">')
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Fixed: {page}')
