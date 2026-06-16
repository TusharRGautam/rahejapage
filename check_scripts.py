import re
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()
scripts = re.findall(r'<script.*?src=["\']([^"\']+)["\']', idx)
print('External scripts:', scripts)
