import json, requests
import string, random
import getpass


def action_to_function(action):
    functions = {
        'alarm' : alarm,
        'reminder' : reminder,
        'weather' : get_weather,
        'music' : play_music,
        'sports' : get_sports,
        'web_search' : web_search,
        'paste' : paste_file,
        'define' : dictionary_define
    }
    return functions.get(action)

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
