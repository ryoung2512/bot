"""
Simple Weather Function
Displays basic information
Using Yahoo Weather
"""
import json
from urllib.parse import urlencode
from urllib.request import urlopen


def process(input, entities):
    loc = entities['location'][0]['value']
    msg = get_weather(loc)

    output = {
        'input': input,
        'msg': msg
        'success': True
    }
    return output

def get_weather(location):
    baseurl = 'https://query.yahooapis.com/v1/public/yql?'
    yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="' + location + '")'
    yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    result = urlopen(yql_url).read()
    data = json.loads(result)

    if data['query']['count'] is 0:
        return "Sorry, I could not find that for you :("

    results = data['query']['results']['channel']
    loc = results['location']['city'] + "," + results['location']['region'] + ", " + results['location']['country']
    condition = results['item']['condition']
    return "The current weather in " + loc + " is " + condition['text'] + " and " + condition['temp'] + " " + chr(176) + "C"

