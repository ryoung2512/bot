import plugins
import sys


def parse_intent(intent, entities):
    print("intent- ", intent)
    response = sys.modules['plugins.' + intent].process(intent, entities)
    print("response", response)
    return response
