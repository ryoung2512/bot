import json
import requests
import string
import random
import getpass


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


def get_username():
    return getpass.getuser()
