import re
import os

chatbot_html = """<!-- Chatbot -->
<div id="chat-square" class="btn"></div>
<div id="chat-close" class="btn chat-box-toggle">
    <div class="close-img"></div>
</div>

<div class="chat-wrapper">
    <div class="chat-header">
        <div class="chat-header-photo">
            <span class="active-circle"></span>
        </div>
        <div class="chat-header-name">Shreya Shetty </div>
    </div>

    <div class="chat-box-body">
        <div class="chat-box-overlay"></div>
        <div class="chat-logs">
            <div id="hb-chat-bot">
                <div class="chat-container">
                    <div class="chat-messages-time"></div>
                    <div class="chat-messages-container"></div>
                    <div class="chat-actions-container"></div>
                    <div class="chat-footer"></div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Chatbot -->"""

files = ['index.html', 'terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove ALL existing chatbot blocks
    content = re.sub(r'<!-- Chatbot -->.*?<!-- Chatbot -->', '', content, flags=re.DOTALL)
    
    # Insert it right before </body>
    content = content.replace('</body>', chatbot_html + '\n</body>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print('Cleaned and standardized chatbot in', f)
