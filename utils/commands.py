import json, requests
import string, random
import os

try:
    import pwd
except:
    print('')


def generate_id(length):
    possibilities = string.ascii_letters
    user_id = ''
    for i in range(length):
        user_id += random.choice(possibilities)
    return user_id


def get_location():
    fetch = 'http://freegeoip.net/json'
    r = requests.get(fetch)
    j = json.loads(r.text)
    return j

# location = get_location()
# print(location['city'])
# print(location['region_code'])
