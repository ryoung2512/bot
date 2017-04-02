from plugins import *


def action_to_function(action, args):
    functions = {
        'alarm': alarm.alarm,
        'reminder': reminder.reminder,
        'weather': weather.get_weather,
        'music': music.play_music,
        'sports': sports.get_sports,
        'web_search': web.web_search,
        'paste': pastebin.paste_file,
        'define': dictionary.dictionary_define
    }
    return functions.get(action)(args)
