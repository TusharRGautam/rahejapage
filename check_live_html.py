import urllib.request
html = urllib.request.urlopen('https://www.rahejaprime.in').read().decode('utf-8')
if 'rahejasprimetwo.com' in html:
    print('HTML_NOT_UPDATED')
else:
    print('HTML_UPDATED')
