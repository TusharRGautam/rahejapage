
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Find the developer section in index.html
start_marker = 'id="developer"'
idx = index_content.find(start_marker)

# Go backward to find the opening <section tag
section_start = index_content.rfind('<section', 0, idx)
section_end = index_content.find('</section>', idx) + len('</section>')

footer_section = index_content[section_start:section_end]
print("Extracted footer section:")
print(footer_section[:500])
print("...")

# Policy pages to fix
policy_files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for fname in policy_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has developer section
    if 'id="developer"' in content:
        print(f'{fname}: already has developer section, skipping')
        continue

    # Find where to insert: just before </main>
    main_end = content.find('</main>')
    if main_end == -1:
        print(f'{fname}: no </main> found!')
        continue

    # Insert footer section before </main>
    new_content = content[:main_end] + '\n' + footer_section + '\n' + content[main_end:]
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'{fname}: footer section added successfully')

print("Done!")
