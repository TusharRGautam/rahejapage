
from bs4 import BeautifulSoup

# The RERA/Disclaimer footer HTML to add (same as index.html's newlist section)
rera_footer = '''
<section style="text-align:justify;background:#f7f7f7 !important;" class="section shadow-sm" id="rera-footer">
<small>
    <style>
.newlist { list-style: none; line-height: 28px; padding-left: 24px; text-align: left; }
.newlist li:before { content: '\\2714'; color: #1a6b4a; font-weight: 800;  margin-right: 10px;  font-size: 13px;  margin-left: -24px; }
    </style>
    <ul class="newlist">
        <li>Project Registered under Government of India RERA Act 2016</li>
        <li>MAHA RERA Project Registration No.: P51700046572</li>
        <li>Aur marketing partner Name:- Caifu Wealth Creators Private Limited <br> Rera number: A51700045963</li>
        <li>Authorised Marketing Partner: CIN:- P51700046572</li>
        <li>Site Address: Raheja Prime Two: World Trade Center, Vashi NX, Juinagar, Navi Mumbai, Maharashtra 400705</li>
        <li>Contact Us: Corporate Office: Raheja Universal: Unit No. 5C, 5th Floor, Raheja Centre-Point, 294, C.S.T. Road, Kalina, Santacruz (E), Mumbai - 400098</li>
    </ul>
<b>Disclaimer:</b>
We are an authorised marketing partner for this project. Provided content is given by respective owners and this website and content is for information purpose only and it does not constitute any offer to avail for any services. Prices mentioned are subject to change without prior notice and properties mentioned are subject to availability. You can expect a call, SMS or emails on details registered with us.<hr>
</small>
</section>
'''

policy_files = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

for fname in policy_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has the rera-footer
    if 'rera-footer' in content:
        print(f'{fname}: already has rera-footer, skipping')
        continue
    
    # Find the copyright paragraph - insert rera_footer BEFORE it
    # The copyright line looks like: <p style="text-align:center; padding-bottom:20px;">Copyright
    copyright_marker = '<p style="text-align:center; padding-bottom:20px;">'
    idx = content.find(copyright_marker)
    if idx == -1:
        # Try alternate
        copyright_marker = '<p style="text-align:center;">'
        idx = content.find(copyright_marker)
    
    if idx == -1:
        print(f'{fname}: copyright section not found!')
        continue
    
    # Insert rera footer right before copyright paragraph
    new_content = content[:idx] + rera_footer + '\n' + content[idx:]
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'{fname}: RERA footer added successfully')

print("Done!")
