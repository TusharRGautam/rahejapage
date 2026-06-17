from bs4 import BeautifulSoup
import os

files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Remove chat script links if any remain
    for link in soup.find_all('link', href='./assets/css/chatv25.css'):
        link.decompose()
        
    for link in soup.find_all('link', href=lambda x: x and 'chatv25' in x):
        link.decompose()
        
    # Remove chatbot and forms
    for element in soup.select('.micro-side, #enqModal, #enqModal233, .lightbox2, #chat-square, .drift-open-chat'):
        element.decompose()
        
    # Remove other modal scripts we might have missed
    for script in soup.find_all('script'):
        if script.string and ('chatbotApiInput' in script.string or 'commercialchat' in script.string or 'PopupShown' in script.string):
            script.decompose()

    # Make sure we don't accidentally leave dangling buttons that open modals if they are floating
    for element in soup.select('.modal-call-btn, .popcallbtn'):
        if element.find_parent('div', class_='modal') is None:
            # We already deleted modals, but just in case
            pass

    with open(f, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    print(f'Processed {f}')
