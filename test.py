#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import time
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '07924bd190424e6caa2a5c5b63ff227b'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    start_time = time.time()
    request.query = "Hello"

    response = request.getresponse()
    response = json.loads(response.read())
    print (response)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()