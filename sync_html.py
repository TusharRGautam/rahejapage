import re

def get_block(html, start_marker, end_marker):
    start = html.find(start_marker)
    if start == -1: return None
    end = html.find(end_marker, start)
    if end == -1: return None
    return html[start:end+len(end_marker)]

def sync_page(target_file):
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    with open(target_file, 'r', encoding='utf-8') as f:
        tgt = f.read()

    # 1. Sync <head> but keep original title, meta description, and canonical
    idx_head = get_block(idx, '<head>', '</head>')
    tgt_head = get_block(tgt, '<head>', '</head>')
    
    if idx_head and tgt_head:
        title = get_block(tgt_head, '<title>', '</title>')
        desc = get_block(tgt_head, '<meta name="description"', '>')
        canonical = get_block(tgt_head, '<link rel="canonical"', '>')
        
        new_head = idx_head
        if title: new_head = re.sub(r'<title>.*?</title>', title, new_head, flags=re.DOTALL)
        if desc: new_head = re.sub(r'<meta name="description".*?>', desc, new_head, flags=re.DOTALL)
        if canonical: new_head = re.sub(r'<link rel="canonical".*?>', canonical, new_head, flags=re.DOTALL)
        
        tgt = tgt.replace(tgt_head, new_head)

    # 2. Sync <header> (navbar)
    idx_header = get_block(idx, '<header class="micro-nav', '</header>')
    tgt_header = get_block(tgt, '<header class="micro-nav', '</header>')
    if idx_header and tgt_header:
        tgt = tgt.replace(tgt_header, idx_header)

    # 3. Sync Chatbot HTML
    idx_chat = get_block(idx, '<!-- Chatbot -->', '<!-- Chatbot -->')
    tgt_chat = get_block(tgt, '<!-- Chatbot -->', '<!-- Chatbot -->')
    if idx_chat and tgt_chat:
        tgt = tgt.replace(tgt_chat, idx_chat)
        
    # 4. Sync Small Chatbot HTML
    idx_sm_chat = get_block(idx, '<!-- Small Chatbot -->', '<!-- Small Chatbot -->')
    tgt_sm_chat = get_block(tgt, '<!-- Small Chatbot -->', '<!-- Small Chatbot -->')
    if idx_sm_chat and tgt_sm_chat:
        tgt = tgt.replace(tgt_sm_chat, idx_sm_chat)

    # 5. Sync Download Brochure Floating button
    idx_brochure = get_block(idx, '<div class="download-brochure">', '</div>\n                </div>\n            </div>')
    tgt_brochure = get_block(tgt, '<div class="download-brochure">', '</div>\n                </div>\n            </div>')
    if idx_brochure and tgt_brochure:
        tgt = tgt.replace(tgt_brochure, idx_brochure)
        
    # 6. Drift CSS links might be different
    idx_drift = get_block(idx, '<!-- Drift Start -->', '<!-- Chatbot -->')
    tgt_drift = get_block(tgt, '<!-- Drift Start -->', '<!-- Chatbot -->')
    if idx_drift and tgt_drift:
        tgt = tgt.replace(tgt_drift, idx_drift)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(tgt)
    print(f"Synced {target_file}")

for page in ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']:
    sync_page(page)
