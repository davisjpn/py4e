import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
address = input('Enter location: ')
#if len(address) < 1:
    #break
url = serviceurl + urllib.parse.urlencode({'address':address})
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None
print(js)
if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
else:
    #print(json.dumps(js, indent=4))
    id = js['results'][0]['place_id']
    print(id)
    #lat = js['results'][0]['geometry']['location']['lat']
    #lng = js['results'][0]['geometry']['location']['lng']
    #print('lat', lat, 'lng', lng)
    #location = js['results'][0]['formatted_address']
    #print(location)
