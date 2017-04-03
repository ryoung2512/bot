import sys
import os
import json
import utils.commands as util
import requests
import utils.speech as talk
import utils.parser as parse
import plugins

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

# The token needed to communicate with our bot

token = "07924bd190424e6caa2a5c5b63ff227b"


class Communicator(object):
    def __init__(self):
        self.serena = apiai.ApiAI(token)
        self.session_id = util.generate_id(20)
        self.response = {}

    def talk(self, message):
        try:
            self.request = self.serena.text_request()
            self.request.lang = 'en'  # can change language later if we want
            self.request.session_id = self.session_id
            self.request.query = message
            callback = self.request.getresponse()
            self.response = json.loads(callback.read())
        except:
            self.response = {}

    def get_new_session_id(self):
        self.session_id = util.generate_id(20)

    def get_confidence(self):
        if self.response:
            return self.response['result']['score']
        else:
            return 0

    def get_intent(self):
        if self.response:
            return self.response['result']['action']
        else:
            return 'empty'

    def print_message(self):
        if self.get_confidence() > 0.5:
            msg = self.response['result']['fulfillment']['speech']
            print('serena: ' + msg)
           # talk.bot_speak(msg)
        else:
            print('serena: sorry I don\'t know how to handle that yet')
        self.response = {}
