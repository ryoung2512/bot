import json
import requests
import string
import random
import getpass
from plugins import *

def action_to_function(action, args):

    functions = {
        'alarm': alarm,
        'reminder': reminder,
        'weather': weather.get_weather,
        'music': music.play_music,
        'sports': sports.get_sports,
        'web_search': web.web_search,
        'paste': pastebin.paste_file,
        'define': dictionary.dictionary_define
    }
    return functions.get(action)(args)

# to all a function do functions[function](args) not sure how to change it like that for this


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

# location = get_location()
# print(location['city'])
# print(location['region_code'])
