
# Replace the 2-button mob-action with the exact 3-button version from index.html
# Floor Plan and Brochure will be direct download links (no modal needed on policy pages)

old_mob_action = '''<div class="mob-action d-md-none d-block" style="background-color: #3d8f61; padding-top: 8px; padding-bottom: 8px;">
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

new_mob_action = '''<div class="mob-action d-md-none d-block" style="background-color: #3d8f61; padding-top: 8px; padding-bottom: 8px;">
    <ul class="nav d-flex align-items-center justify-content-between" style="margin-bottom: 6px; flex-wrap: nowrap;">
        <li class="nav-item text-center" style="border-right: 1px solid rgba(255,255,255,0.4); width: 33.33%; padding: 0;">
            <a href="tel:+916292151107" class="d-flex align-items-center justify-content-center" style="text-decoration: none; color: #fff !important; font-size: 13px;">
                <i class="fa-solid fa-phone" style="font-size: 13px; color: #fff !important; margin-right: 5px;"></i> Call
            </a>
        </li>
        <li class="nav-item text-center" style="border-right: 1px solid rgba(255,255,255,0.4); width: 33.33%; padding: 0;">
            <a href="brochure.pdf" download class="d-flex flex-column align-items-center justify-content-center" style="text-decoration: none; color: #fff !important; font-size: 13px; line-height: 1.2;">
                <i class="fa-solid fa-download" style="font-size: 15px; color: #fff !important; margin-bottom: 3px;"></i> Floor Plan
            </a>
        </li>
        <li class="nav-item text-center" style="width: 33.33%; padding: 0;">
            <a href="brochure.pdf" download class="d-flex align-items-center justify-content-center" style="text-decoration: none; color: #fff !important; font-size: 13px;">
                <span style="background: #e23a3a; border-radius: 2px; padding: 2px; margin-right: 5px; display: inline-flex; align-items: center; justify-content: center; height: 18px; width: 18px;"><i class="fa-solid fa-file-pdf" style="color: white !important; font-size: 12px;"></i></span> Brochure
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
        print(f'{fname}: updated to 3-button version (Call, Floor Plan, Brochure)')
    else:
        idx = content.find('mob-action d-md-none')
        if idx != -1:
            print(f'{fname}: mob-action found but pattern did not match exactly')
            print('Current content:')
            print(repr(content[idx-5:idx+500]))
        else:
            print(f'{fname}: no mob-action found')

print("Done!")
