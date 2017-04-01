import pyttsx


def bot_speak(message):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 40)
    engine.say(message)
    engine.runAndWait()

