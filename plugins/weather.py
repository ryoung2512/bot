"""
Simple Weather Function
Displays basic information
Using Yahoo Weather
"""
import json
import urllib.parse
import urllib.request


def process(input, entities):
    loc = entities['location'][0]['value']
    baseurl = 'https://query.yahooapis.com/v1/public/yql?'
    yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="' + loc + '")'
    yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
    result = urllib.request.urlopen(yql_url).read()
    data = json.loads(result)
    results = data['query']['results']['channel']
    location = results['location']
    display_loc = location['city'] + "," + location['region'] + ", " + location['country']
    condition = results['item']['condition']

    #print(results)
    output = {
        'input': input,
        'msg': "The current weather in " + display_loc + " is " + condition['text'] + " and " + condition['temp'] + " " + chr(176) + "C",
        'success': True
    }
    return output

def get_weather_city(city, region_code):
    baseurl = 'https://query.yahooapis.com/v1/public/yql?'
    yql_query = "select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"" + city + ", " + region_code + "\") and u='c'"
    yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
    result = urllib.request.urlopen(yql_url).read()
    data = json.loads(result)
    results = data['query']['results']['channel']['item']['condition']
    print("The current temperature for " + city + ", " + region_code + " is " + results['temp'] + " " + chr(176) + "C")
    print("It is " + results['text'] + " outside.")
