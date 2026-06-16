with open('assets/js/commercialchatv25.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all Pooja Agarwal occurrences with Shreya Shetty
content = content.replace('Pooja Agarwal', 'Shreya Shetty')
content = content.replace('Pooja\\x20Agarwal', 'Shreya\\x20Shetty')

# Also check header in HTML - handled in index.html
count = content.count('Pooja')
print(f'Remaining Pooja occurrences: {count}')

with open('assets/js/commercialchatv25.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
