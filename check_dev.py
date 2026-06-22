
with open('terms-conditions.html', 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'id="developer"'
idx = content.find(marker)
if idx == -1:
    print("Not found!")
else:
    section_start = content.rfind('<section', 0, idx)
    section_end = content.find('</section>', idx) + len('</section>')
    print("Developer section content:")
    print(content[section_start:section_end])
    print()
    print(f"Length: {section_end - section_start} chars")
