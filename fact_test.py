import sys
from wit import Wit
import utils.speech as speech

# The token needed to communicate with our bot
token = "TU2KA4CPBA2ZH53L3E2GGXXXOAKNHQFL"


def fact(request):
    context = request['context']
    entities = request['entities']
    context['random_fact'] = "This is a test"
    return context


def send(request, response):
    print(response['text'].decode('utf8'))
    speech.bot_speak(response['text'].decode('utf8'))

actions = {'send': send, 'fact': fact}

client = Wit(access_token=token, actions=actions)
client.interactive()
