import re

with open('terms-conditions.html', 'r', encoding='utf-8') as f:
    tc = f.read()
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

tc_bottom = tc[tc.find('</main>'):]
idx_bottom = idx[idx.find('</main>'):]

tc_urls = set(re.findall(r'href="([^"]+)"', tc_bottom))
idx_urls = set(re.findall(r'href="([^"]+)"', idx_bottom))
print('terms urls:', tc_urls - idx_urls)

tc_vals = set(re.findall(r'value="([^"]+)"', tc_bottom))
idx_vals = set(re.findall(r'value="([^"]+)"', idx_bottom))
print('terms values:', tc_vals - idx_vals)
