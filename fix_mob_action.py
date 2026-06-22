
# Replace the single-button mob-action bar in policy pages with a 2-button version
# Call + WhatsApp (since form-based buttons can't be used on policy pages)

old_mob_action = '''<div class="mob-action d-md-none d-block" style="background-color: #3d8f61; padding-top: 8px; padding-bottom: 8px;">
<ul class="nav d-flex align-items-center justify-content-center" style="margin-bottom: 6px; flex-wrap: nowrap; list-style: none; padding: 0; margin: 0;">
<li class="nav-item text-center" style="width: 100%; padding: 0;">
<a class="d-flex align-items-center justify-content-center" href="tel:+916292151107" style="text-decoration: none; color: #fff !important; font-size: 13px; font-weight: bold;">
<i class="fa-solid fa-phone" style="font-size: 13px; color: #fff !important; margin-right: 5px;"></i> Call
            </a>
</li>
</ul>
</div>'''

new_mob_action = '''<div class="mob-action d-md-none d-block" style="background-color: #3d8f61; padding-top: 8px; padding-bottom: 8px;">
<ul class="nav d-flex align-items-center justify-content-between" style="margin-bottom: 0; flex-wrap: nowrap; list-style: none; padding: 0; margin: 0;">
<li class="nav-item text-center" style="border-right: 1px solid rgba(255,255,255,0.4); width: 50%; padding: 6px 0;">
<a class="d-flex align-items-center justify-content-center" href="tel:+916292151107" style="text-decoration: none; color: #fff !important; font-size: 13px; font-weight: bold;">
<i class="fa-solid fa-phone" style="font-size: 13px; color: #fff !important; margin-right: 5px;"></i> Call
</a>
</li>
<li class="nav-item text-center" style="width: 50%; padding: 6px 0;">
<a class="d-flex align-items-center justify-content-center" href="https://wa.me/916292151107" target="_blank" style="text-decoration: none; color: #fff !important; font-size: 13px; font-weight: bold;">
<i class="fa-brands fa-whatsapp" style="font-size: 15px; color: #fff !important; margin-right: 5px;"></i> WhatsApp
</a>
</li>
</ul>
</div>'''

policy_files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for fname in policy_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_mob_action in content:
        content = content.replace(old_mob_action, new_mob_action)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'{fname}: mob-action updated to 2-button version')
    else:
        # try to find what's in the file
        idx = content.find('mob-action d-md-none')
        if idx != -1:
            print(f'{fname}: mob-action found but pattern did not match. Manual check needed.')
            print(repr(content[idx:idx+300]))
        else:
            print(f'{fname}: no mob-action found')

print("Done!")
