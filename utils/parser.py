import plugins
import sys


def parse_intent(input, intent, entities):
    response = sys.modules['plugins.' + intent].process(input, entities)
    return response
