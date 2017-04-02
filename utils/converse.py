from wit import Wit
import utils.commands as util
import utils.speech as talk
# The token needed to communicate with our bot

token = "TU2KA4CPBA2ZH53L3E2GGXXXOAKNHQFL"


class Communicator(object):
    def __init__(self):
        self.client = Wit(access_token=token)
        self.response = {}
        self.session_id = util.generate_id(20)

    def talk(self, message):
        self.response = self.client.converse(self.session_id, message, {})
        print(self.response)

    def get_type(self):
        if 'type' in self.response:
            return self.response['type']
        else:
            return 'empty'

    def get_confidence(self):
        if 'confidence' in self.response:
            return self.response['confidence']

    def get_intent(self):
        if 'entities' in self.response and 'intent' in self.response['entities']:
            return self.response['entities']['intent'][0]['value']
        else:
            return 'empty'

    def print_message(self):
        if 'msg' in self.response:
            print('serena: ' + self.response['msg'])
            talk.bot_speak(self.response['msg'])

