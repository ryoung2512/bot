import requests, json

def getLocation():
    fetch = 'http://freegeoip.net/json'
    r = requests.get(fetch)
    j = json.loads(r.text)
    return j
location = getLocation()
print(location['city'])
print(location['region_code'])
