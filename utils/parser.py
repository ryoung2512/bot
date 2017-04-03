import plugins
import sys


def parse_intent(intent, entities):
    response = sys.modules['plugins.' + intent].process(intent, entities)
    return response
