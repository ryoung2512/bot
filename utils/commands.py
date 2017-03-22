import requests
import json


def get_location():
    fetch = 'http://freegeoip.net/json'
    r = requests.get(fetch)
    j = json.loads(r.text)
    return j


location = get_location()
print(location['city'])
print(location['region_code'])
