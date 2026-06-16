import re
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

forms = re.findall(r'<form.*?</form>', idx, flags=re.DOTALL)
for i, form in enumerate(forms):
    print(f'--- Form {i} ---')
    inputs = re.findall(r'<input.*?>', form)
    for inp in inputs:
        name_match = re.search(r'name="([^"]+)"', inp)
        if name_match:
            print(name_match.group(1))
