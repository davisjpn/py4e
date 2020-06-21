import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
countlist = list()
url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
data = ET.fromstring(html)
top = data.findall('comments/comment')
print('Count:',len(top))
for item in top:
    value = int(item.find('count').text)
    countlist.append(value)
print(sum(countlist))
