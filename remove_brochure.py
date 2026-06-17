from bs4 import BeautifulSoup
import os

files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Remove elements by class
    for element in soup.select('.floating-brochure-btn, .mobile-bottom-bar'):
        element.decompose()
        
    # Remove nav item for Download Brochure
    for a_tag in soup.find_all('a', string=lambda text: text and 'Download Brochure' in text):
        parent_li = a_tag.find_parent('li')
        if parent_li:
            parent_li.decompose()
        else:
            a_tag.decompose()
            
    for a_tag in soup.find_all('a'):
        if a_tag.get('data-title') == 'Download brochure' or a_tag.get('data-title') == 'Download Brochure':
            parent_li = a_tag.find_parent('li')
            if parent_li and 'nav-item' in parent_li.get('class', []):
                parent_li.decompose()
            else:
                a_tag.decompose()
                
        # Also remove the "Download Price Sheet" buttons if they exist as they are similar CTA
        elif a_tag.get('data-title') == 'Download Price Sheet':
            if 'navbar-right-buttons' in (a_tag.parent.get('class') or []):
                a_tag.decompose()

    # Make sure we don't accidentally leave dangling mobile bottom bar brochure links
    for a_tag in soup.find_all('a', {'data-enquiry': 'Download Brochure Mobile Bar'}):
        a_tag.decompose()
        
    for a_tag in soup.find_all('a', {'data-enquiry': 'Download Floor Plan Mobile Bar'}):
        a_tag.decompose()

    with open(f, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    print(f'Processed {f}')
