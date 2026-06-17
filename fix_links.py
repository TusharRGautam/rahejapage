import os

files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']
for f in files:
    if not os.path.exists(f):
        print(f'{f} not found, skipping')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Prepend index.html to hash links in navbar
    content = content.replace('href="#home"', 'href="index.html"')
    content = content.replace('href="#pricing"', 'href="index.html#pricing"')
    content = content.replace('href="#sitefloorplan"', 'href="index.html#sitefloorplan"')
    content = content.replace('href="#amenities"', 'href="index.html#amenities"')
    content = content.replace('href="#gallery"', 'href="index.html#gallery"')
    content = content.replace('href="#address_section"', 'href="index.html#address_section"')
    content = content.replace('href="#sitevisit"', 'href="index.html#sitevisit"')
    
    # Fix logo link
    content = content.replace('href="/"', 'href="index.html"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Navbar links updated in {f}')
