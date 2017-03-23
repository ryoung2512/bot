import sys
from wit import Wit

# The token needed to communicate with our bot
token = "TU2KA4CPBA2ZH53L3E2GGXXXOAKNHQFL"

def fact(request):
    context = request['context']
    entities = request['entities']
    context['random_fact'] = "This is a test"
    return context

def send(request, response):
    print(response['text'])

actions = { 'send' : send, 'fact' : fact}

client = Wit(access_token=token, actions=actions)
client.interactive()
