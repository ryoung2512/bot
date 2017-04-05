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
token = "621738afe2e845978091c0fde5f660bf"


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
            print(self.response)
        except:
            self.response = {}

    def get_resolved_query(self):
        return self.response['result']['resolvedQuery']

    def get_new_session_id(self):
        self.session_id = util.generate_id(20)

    def get_confidence(self):
        if self.response:
            return self.response['result']['score']
        return 0.0

    def get_intent(self):
        if self.response:
            return self.response['result']['action']
        return 'empty'

    def get_action(self):
        return self.response['result']['action']

    def get_speech(self):
        return self.response['result']['fulfillment']['speech']

    def get_params(self):
        return self.response['result']['parameters']

    def get_message(self):
        msg = "sorry I don\'t know how to handle that yet"
        if self.get_confidence() > 0.5:
            if self.get_action() in plugins.__all__:
                query = self.get_resolved_query()
                action = self.get_action()
                params = self.get_params()
                msg = parse.parse_intent(query, action, params)['msg']
            else:
                msg = self.get_speech()
        return msg

    def print_message(self):
        print('serena: ' + self.get_message())
        self.response = {}
