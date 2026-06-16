import urllib.request
js = urllib.request.urlopen('https://www.rahejaprime.in/assets/js/app1_min.js').read().decode('utf-8')
if 'modal("show")' in js:
    print('UPDATED')
else:
    print('NOT_UPDATED')
