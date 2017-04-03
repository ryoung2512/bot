import urllib.request

url = "https://www.youtube.com/watch?v=Cagho3pCjoI"
req = urllib.request.Request(url)
f = urllib.request.urlopen(req)

f.read()