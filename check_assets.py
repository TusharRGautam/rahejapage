import os
import re
from urllib.parse import urlparse

def check_missing_assets():
    base_dir = 'd:/Tushar/OFFICE/navneet project/Landingpage2'
    
    missing = []
    
    # Check index.html
    html_file = os.path.join(base_dir, 'index.html')
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Regex to find src="..." and href="..."
    sources = re.findall(r'(?:src|href)="([^"]+)"', html_content)
    for src in sources:
        if src.startswith('http') or src.startswith('//') or src.startswith('#') or src.startswith('data:') or src.startswith('mailto:') or src.startswith('tel:'):
            continue
        # Remove query parameters if any
        src_path = src.split('?')[0]
        # Resolve relative to base_dir
        # Assuming index.html is in base_dir
        full_path = os.path.join(base_dir, src_path.lstrip('/'))
        if not os.path.exists(full_path):
            missing.append(f"HTML: {src_path}")

    # Check CSS files
    css_dir = os.path.join(base_dir, 'assets', 'css')
    for root, _, files in os.walk(css_dir):
        for file in files:
            if file.endswith('.css'):
                css_file = os.path.join(root, file)
                with open(css_file, 'r', encoding='utf-8') as f:
                    css_content = f.read()
                
                urls = re.findall(r'url\((["\']?)([^)"\']+)\1\)', css_content)
                for _, url in urls:
                    if url.startswith('http') or url.startswith('//') or url.startswith('data:'):
                        continue
                    url_path = url.split('?')[0].split('#')[0]
                    # resolve relative to css_file directory
                    full_path = os.path.abspath(os.path.join(root, url_path))
                    if not os.path.exists(full_path):
                        missing.append(f"CSS ({file}): {url_path}")
                        
    return missing

missing_assets = check_missing_assets()
if missing_assets:
    print("Missing assets found:")
    for asset in set(missing_assets):
        print("-", asset)
else:
    print("No missing local assets detected.")
