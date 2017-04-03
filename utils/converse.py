from wit import Wit
import utils.commands as util
import requests
import utils.speech as talk
import utils.parser as parse
# The token needed to communicate with our bot

token = "TU2KA4CPBA2ZH53L3E2GGXXXOAKNHQFL"


class Communicator(object):
    def __init__(self):
        self.client = Wit(access_token=token)
        self.response = {}
        self.session_id = util.generate_id(20)

    def request(self, input):
        try:
            r = requests.get('https://api.wit.ai/message?v=20160526&session_id=123abc&q=' + input, headers={
                'Authorization': 'Bearer %s' % token
            })
            data = r.json()
            print(data)
            entities = data['entities']
            intent = entities['intent'][0]['value']
            confidence = entities['intent'][0]['confidence']

            import plugins
            if intent in plugins.__all__ and confidence > 0.5:
                msg = parse.parse_intent(intent, entities)
            else:
                msg = None
            return msg
        except:
            return None, {}

    def talk(self, message):
        #self.response = self.client.converse(self.session_id, message, {})
        self.response = self.request(message)
        #return self.request(message)

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

