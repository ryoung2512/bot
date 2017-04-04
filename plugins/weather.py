"""
Simple Weather Function
Displays basic information
Using Yahoo Weather
"""
import json
import utils.commands as commands
from urllib.parse import urlencode
from urllib.request import urlopen


def process(input, entities):
    if 'address' in entities:
        try:
            loc = ''
            for k, v in entities['address'].items():
                loc = loc + ' ' + v
        except:
            loc = next(iter(entities['address'].values()))
    else:
        location = commands.get_location()
        loc = location['city'] + "," + location['region_name'] + "," + location['country_name']

    msg = get_weather(loc.strip())
    output = {
        'input': input,
        'msg': msg,
        'success': True
    }
    return output


def get_weather(location):
    # print(location)
    baseurl = 'https://query.yahooapis.com/v1/public/yql?'
    yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="' + location + '")'
    default_msg = "Sorry, I could not find that for you, are you sure that is a real place?"
    try:
        yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
        result = urlopen(yql_url).read()
        data = json.loads(result)
    except:
        return default_msg

    # print(data)

    if data['query']['count'] is 0:
        return default_msg

    results = data['query']['results']['channel']
    loc = results['location']['city'] + "," + results['location']['region'] + ", " + results['location']['country']
    condition = results['item']['condition']
    return "The current weather in " + loc + " is " + condition['text'] + " and " + condition['temp'] + chr(
        176) + "F"
