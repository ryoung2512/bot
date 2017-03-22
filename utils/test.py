import urllib2, urllib, json
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"guelph, on\") and u='c'"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
results = data['query']['results']['channel']['item']['condition']
print "Temperature is: " + results['temp']
print "It is " + results['text'] + " outside"
