import sys
import requests
from wit import Wit

access_token = "TU2KA4CPBA2ZH53L3E2GGXXXOAKNHQFL"
# Quickstart example
# See https://wit.ai/ar7hur/Quickstart


def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val


def send(request, response):
    print(response['text'])


def get_forecast(request):
    context = request['context']
    entities = request['entities']

    loc = first_entity_value(entities, 'location')
    if loc:
        context['forecast'] = 'sunny'
        if context.get('missingLocation') is not None:
            del context['missingLocation']
    else:
        context['missingLocation'] = True
        if context.get('forecast') is not None:
            del context['forecast']

    return context

actions = {
    'send': send,
    'getForecast': get_forecast,
}

#client = Wit(access_token=access_token, actions=actions)
#client.interactive()


def process_query(input):
    try:
        r = requests.get('https://api.wit.ai/message?v=20160420&q=' + input, headers={
            'Authorization': 'Bearer %s' % access_token
        })
        data = r.json()
        intent = data['outcomes'][0]['intent']
        entities = data['outcomes'][0]['entities']
        confidence = data['outcomes'][0]['confidence']
        #if intent in src.__all__ and confidence > 0.5:
        return [intent, entities, confidence]
        #else:
        #    return None, {}
    except:
        return None, {}

print(process_query("weather in washington"))

