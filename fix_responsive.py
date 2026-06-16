import re

pages = ['terms-conditions.html', 'privacy-policy.html', 'cookies-policy.html']

# Responsive CSS to add inside the page <style> block
responsive_css = """
/* ===== Policy Page Responsive Fixes ===== */
#developer {
    padding: 20px 15px !important;
}
#developer .thankyou-text {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 10px;
    line-height: 1.8;
    font-size: 15px;
}
#developer .thankyou-text b {
    color: #333;
    display: inline-block;
    margin-top: 5px;
}
#developer .thankyou-text p {
    text-align: left !important;
}
@media (max-width: 768px) {
    #developer {
        padding: 15px 10px !important;
    }
    #developer .thankyou-text {
        font-size: 14px;
        line-height: 1.7;
        padding: 0 5px;
    }
}
/* Chat square position on mobile - don't overlap brochure button */
@media (max-width: 767px) {
    #chat-square {
        bottom: 70px !important;
        right: 15px !important;
    }
    #chat-close {
        bottom: 70px !important;
        right: 15px !important;
    }
    .chat-wrapper {
        bottom: 130px !important;
    }
}
"""

for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert responsive CSS before </style> that has the download-brochure styles
    # The </style> right before </head>
    target = '.download-brochure .mob_brochure a {\n  display: block;\n  text-align: center;\n  text-decoration: none;\n}\n</style>'
    replacement = '.download-brochure .mob_brochure a {\n  display: block;\n  text-align: center;\n  text-decoration: none;\n}\n' + responsive_css + '\n</style>'
    
    if target in content:
        content = content.replace(target, replacement)
        print(f'Added responsive CSS to {page}')
    else:
        print(f'Target not found in {page}, trying alternate...')
        # Try inserting before </head>
        if '</head>' in content:
            content = content.replace('</head>', f'<style>{responsive_css}</style>\n</head>', 1)
            print(f'Added via </head> in {page}')
    
    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done!')
