import utils.commands as util
import requests
import utils.speech as talk
import utils.parser as parse
import plugins
# The token needed to communicate with our bot

token = "TU2KA4CPBA2ZH53L3E2GGXXXOAKNHQFL"


class Communicator(object):
    def __init__(self):
        self.session_id = util.generate_id(20)
        self.response = {}
        self.entities = {}

    def talk(self, message):
        try:
            r = requests.get('https://api.wit.ai/message?v=20160526&session_id=' + self.session_id + '&q=' + message,
                            headers={ 'Authorization': 'Bearer %s' % token })
            self.response = r.json()
            self.entities = self.response['entities']
        except:
            self.response = {}
            self.entities = {}

    def get_new_session_id(self):
        self.session_id = util.generate_id(20)

    def get_entities(self):
        if self.entities:
            return self.entities
        else:
            return 'empty'

    def get_confidence(self):
        if self.response:
            return self.entities['intent'][0]['confidence']
        else:
            return 0

    def get_intent(self):
        if self.response:
            return self.response['entities']['intent'][0]['value']
        else:
            return 'empty'

    def print_message(self):
        if self.get_intent() in plugins.__all__ and self.get_confidence() > 0.5:
            reply = parse.parse_intent(self.get_intent(), self.get_entities())
            print('serena: ' + reply['msg'])
            talk.bot_speak(reply['msg'])
        else:
            print('serena: sorry I don\'t know how to handle that yet')
        self.response = {}
        self.entities = {}

