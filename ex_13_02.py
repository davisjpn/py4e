import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
countlist = list()
url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
count = 0
info = json.loads(html)
for item in info["comments"]:
    value = int(item["count"])
    count = count + value
print(count)
