from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
numlist=list()
for tag in tags:
    tag = int(tag.contents[0])
    numlist.append(tag)
print(sum(numlist))
    #print(tag.contents[0])
    #print(tag.get('href', None))
    #print('Contents:',tag.contents[0])
