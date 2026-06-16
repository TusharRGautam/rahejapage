import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

idx_bottom = idx[idx.find('</main>'):]

for page in ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html', 'live.html']:
    with open(page, 'r', encoding='utf-8') as f:
        tgt = f.read()

    tgt_bottom = tgt[tgt.find('</main>'):]
    
    # We want to use idx_bottom, but replace home_url values to point to the correct page
    # index.html has value="https://www.rahejasprimetwo.com/" or something similar.
    # Let's replace 'https://www.rahejasprimetwo.com/' with 'https://www.rahejasprimetwo.com/page'
    # Actually, we can just replace 'value="https://www.rahejasprimetwo.com/"' with 'value="https://www.rahejasprimetwo.com/' + page + '"'
    
    new_bottom = idx_bottom
    new_bottom = re.sub(
        r'name="home_url"\s+value="[^"]*"', 
        f'name="home_url" value="https://www.rahejasprimetwo.com/{page}"', 
        new_bottom
    )
    
    tgt = tgt.replace(tgt_bottom, new_bottom)

    with open(page, 'w', encoding='utf-8') as f:
        f.write(tgt)
    print(f"Synced bottom for {page}")
