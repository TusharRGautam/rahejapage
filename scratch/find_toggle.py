import re

with open('assets/js/commercialchatv25.js', 'r', encoding='utf-8') as f:
    js = f.read()

matches = re.finditer(r'\$\([\'"][^\'"]*toggle[^\'"]*[\'"]\)', js)
for m in matches:
    print('Match:', m.group(0))
